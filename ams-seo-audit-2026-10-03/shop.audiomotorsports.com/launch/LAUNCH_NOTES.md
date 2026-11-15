# Launch notes: shop.audiomotorsports.com (Phase 2, read-only)

Run 2026-10-04 with `_phase2/probe.py` (phone 390x844 + desktop 1366x900, TLS verified) plus extra Playwright scripts (scratch/). Raw data: `b1/ b2/ b3/` (probe.json + screenshots), `perf_grid.json`, `broken_card_links.json`. Nothing was submitted, no orders, no forms posted. Cart: the only add-to-cart path is a localStorage cart (`ams-cart.js`), but its buttons never rendered (see M3), so nothing was clicked.
Environment artifacts (unverifiable from here, not site bugs): 403/tunnel failures for youtube, maps.google, share.google, instagram, lacarbeats/lacartint/lacaralarm/amspods (incl. /build/, /shop/), GTM (`gtm.js` tunnel failure). Intermittent socket resets/timeouts on the probe's link checker were retried/confirmed with curl and are not listed as bugs.

URLs probed (22, both viewports): `/`, `/shop/`, car-stereos, car-stereos/retrofit, amplifiers, dash-cameras, alarms-remote-start, `/checkout/`, products (speakers/kicker-46csc654, amplifiers/jbl-club-a600, car-stereos/jvc-kw-m56bt, dash-cameras/momento-momento-ic6, alarms-remote-start/viper-3108v), brands (kicker, pioneer, compustar), `/contact/ /about/ /privacy-policy/ /terms-of-service/ /payment-plan/ /brands-we-love/`, `/nonexistent-xyz/`. Curl only: `/faq/` (200, canonical www, FAQPage schema), `/cart/` 404, `/returns/` 404, robots.txt 200, sitemap.xml 301 to shop-sitemap.xml.

## Decision gate (MUST-FIX if launch wants products to rank)
- **G1. ~282 of ~285 product pages are `noindex, follow`** (Phase 1 AIO_REPORT 1.1). Re-confirmed in this run: `<meta name="robots" content="noindex, follow">` on speakers/kicker-46csc654, amplifiers/jbl-club-a600, car-stereos/jvc-kw-m56bt, alarms-remote-start/viper-3108v. Only the Momento dash-cam products (momento-momento-ic6 checked) have no robots meta. If launch intends products to rank in Google/AI Overviews/Shopping, this is a launch blocker: noindex pages cannot appear in results or AIO. Next step: owner decides yes/no. If yes, stage opening (priced products with richest copy first), swap the templated meta description (identical on all products) and add the products to the sitemap. If no, record it as intentional and rely on collection/brand pages. Never suggest removing pages; this is about indexing intent only.
- **G2. Shop root `/` serves the hub homepage**: title "Car Window Tint & Car Audio in Carson", H1 "Shop car stereo in Carson", canonical `https://www.audiomotorsports.com/`, og:url www, 3 JSON-LD blocks. Title (tint) and H1/content (shop) disagree. The shop landing page the team probably wants indexed is `/shop/` (canonical to itself, title "Shop Parts & Install"). Next step: decide whether `/` should get shop-specific title/H1/canonical, or keep the hub consolidation; at minimum align the title with the H1. NICE unless the owner wants `/` to rank for the shop.

## (a) Visual, phone + desktop
- No horizontal overflow on any page (overflow_x 0 on all 44 page/viewport runs), viewport meta present everywhere, no broken images, all images have alt, CLS 0 to 0.003 everywhere.
- Home phone: hero/H1 and CTAs above the fold; header Call/Menu fine; sticky bottom bar Call / Text us / Quote on every page.
- **V1 (NICE). Chat launcher bubble overlaps card content on phone** (home product grid, amplifiers grid): it sits over the "Pickup available in Carson" text and the right edge of "Reserve for pickup" buttons (`b1/home_phone.png`, `b1/shop-amplifiers_phone.png`). Next step: offset the launcher above the sticky action bar and away from the card button column, or give it a lower z-index than card buttons.
- **V2 (NICE). Car stereos phone: header thumbnail leaves an empty left column** with title block squeezed right (`b1/shop-car-stereos_phone.png`). Cosmetic.
- **V3 (NICE). `/checkout/` opened directly shows a red error "Your cart didn't come through. Please go back to the site and try again."** (`b1/checkout_phone.png`). Expected with no cart payload, but a visitor who types the URL sees an error. Next step: show an empty-cart message with a link to /shop/ when there is no handoff payload. Page is noindex,nofollow (good).
- Tap targets: probe counts many "small" targets (e.g. 808 on `/shop/` phone, 368 car-stereos). Mostly card/facet links; not itemized. NICE: review facet links and card text links for 44px height.

## (b) Click-through
- Nav/footer/CTA links checked on every page by the probe. Internal: all nav, footer, service, brand, policy links 200 (the few resets were re-fetched fine with curl). `/faq/` 200, `/terms-of-service/` 200. No `/cart/` or `/returns/` page (404); there is no standalone cart page, the cart is a drawer (NICE: confirm that is intended; no returns/policy page beyond privacy and terms; pickup-only "we don't ship" lives on product copy).
- **MUST-FIX B1. 52 product-card links 404 after JavaScript runs.** `shop-landing.js` re-renders the cards from `/api/catalog/` and builds each product URL as `/shop/<category>/<row.id>/`. For SKUs whose id prefix is not the live slug the link 404s, while the server-rendered HTML had the right link (e.g. static `/shop/amplifiers/jbl-club-a600/` becomes `/shop/amplifiers/kicker-club-a600/`). Confirmed by loading collections in Chromium, collecting rendered card hrefs, and curling each (full list in `broken_card_links.json`; all 404; I clicked nothing that posts):
  - car-stereos: 8 (Kenwood Excelon KDC-X304, KDC-X304 refurb, KMM-X705, DMX809S, DMX1057XR, DMX1057XR refurb, DMX1058XR; JVC Legend 700 as `jvc-legend-700`)
  - amplifiers: 4 (JBL Club A600, A1000, A5055, 4505 as `kicker-club-*`)
  - dash-cameras: 7 of 7 (Thinkware U1000, U1000 Plus, Q1000, Momento IC6, M7 Wi-Fi, M7 MD-7200, Compustar Drone XC LTE as `kicker-*`)
  - enclosures: 15 (all as `audiocontrol-*`)
  - installation-parts: 18 (PAC/Metra/etc. as `kicker-*`)
  - speakers, alarms, retrofit: 0 broken. The Compustar brand page also carries `kicker-drone-xc-lte` (404). The real pages exist at the static slugs (e.g. `/shop/dash-cameras/thinkware-u1000/`, `/shop/dash-cameras/momento-ic6/`).
  Impact: real shoppers clicking those cards on collection and brand pages hit a 404; Googlebot renders JS and will see these links too. Next step: in `shop-landing.js` use the slug from the catalog row (or keep the server-rendered hrefs and do not overwrite them) instead of `row.id`. Verify by re-running the card-href check above.
- Dash-cam slug inconsistency (NICE): sitemap lists `/shop/dash-cameras/momento-momento-ic6/` (200, no noindex, self-canonical) but collection cards link to `/shop/dash-cameras/momento-ic6/`. Next step: make the sitemap and the card link point to the same URL.
- Forms: none on shop pages other than a 1-textarea chat form (`ams-chat`) and `/checkout/` `#stripe-form` (no fields, JS-driven). Reserve-for-pickup is a JS modal (`ams-reserve.js`) posting to `/api/reserve/` with fields name, phone (required), year, make, model (required), honeypot `company`; not opened/submitted. `/contact/` form action `/api/quote/`, 13 fields including `_captcha`, honeypot `company`, hidden `source_page`/`_subject`; not submitted. Text-to-check-stock uses `sms:` links.
- Third-party hosts unverifiable (see top).

## (c) Bugs
- **MUST-FIX C1. `/_vercel/insights/script.js` returns 404 HTML on every page** (curl 404 text/html), console error "Refused to execute script ... MIME type 'text/html'" on all 22 pages, both viewports. Analytics (Vercel Web Analytics) is referenced but not enabled/served, so analytics data is lost and every page logs a console error. Next step: enable Vercel Web Analytics for this project or remove the tag.
- **MUST-FIX C2 (decision on severity). `GET /api/checkout/?action=catalog&site=hub` returns HTTP 500** `{"error":{"code":"server_error",...}}` (curl x3 and in-browser on every shop page; `site=shop` also 500). `ams-cart.js` needs it to put "Add to cart" buttons on cards, so no Add-to-cart ever appears and the console logs a 500 on every page. Cause unknown (may be that nothing is marked "Sell online"). If online cart is part of launch this blocks it; if launch is reserve/call only, still fix the 500 so it returns an empty list. Unverified: whether the catalog endpoint works from the hub origin.
- C3 (NICE). `/assets/css/paylater-note.css` once served as text/plain with a 502 during the amplifiers phone run (CSS refused); curl later returned 200 text/css. Transient (also saw a 502), re-test; if it recurs, treat as a deploy/edge issue.
- C4 (NICE). Home preload warning: `hub-hero-mobile.jpg` preloaded but unused on desktop. Add `media` attribute to the preload link.
- C5 (NICE). Console warnings from YouTube embed (`web-share`, `allowfullscreen` attribute) on the home page; harmless.
- Meta: all pages have viewport, lang=en, title, favicon (`/assets/img/favicon.png` 200, apple-touch-icon 200, `/favicon.ico` 200). Canonicals: shop/collection/brand/product pages self-canonical on the shop host; `/`, `/contact/`, `/about/`, `/faq/`, policies, payment-plan, brands-we-love, 404 page canonical to `www.audiomotorsports.com` (404 page canonical is `https://www.audiomotorsports.com/404.html`: NICE, drop canonical on error pages). No mixed content, no page errors (uncaught JS exceptions) anywhere.
- C6 (NICE). `/shop/` meta description is a single line ("Twenty years, one address...") with no product terms; H1 reads lowercase "car stereo and speakers at Audio MotorSports". Improve for launch.
- C7 (NICE). Product pages share one meta description, thin templated copy (Phase 1 finding, unchanged).
- Mount-proxy: not needed; all sister-domain pages were not audited here.

## (d) Speed / lab numbers (Chromium, proxied; lab != field)
| Page (phone / desktop) | LCP ms | CLS | long-task over 50ms (TBT proxy) | TTFB | transfer KB |
|---|---|---|---|---|---|
| `/` | 1380 / 1464 | 0 | 120 / 149 | 416 / 443 | 583 / 776 |
| `/shop/` | 1628 / **4116** | 0 | 47 / 149 | 436 / 308 | 1812 / 2058 |
| car-stereos (146 cards) | 1536 / 1480 | 0 | 273 / 396 | 444 / 415 | 1517 / 2663 |
| retrofit (125 cards) | 1028 / 1336 | 0 | 277 / 195 | 170 / 428 | 954 / 1074 |
| amplifiers | **5716** / 1140 | 0 | 14 / 112 | 228 / 348 | 479 / 1996 |
| dash-cameras | 1052 / 988 | 0 | 65 / 139 | 253 / 326 | 758 / 765 |
| alarms | 1380 / 1152 | 0 | 0 / 181 | 400 / 348 | 1269 / 1617 |
| product pages (5) | 1040-2080 / 1032-**10940** (jvc), 3808 (viper) | 0 | 0-152 | 137-619 | 206-258 |
| brand kicker/pioneer/compustar | 884-1108 / 992-**10824** (pioneer), 1160 | 0 | 37-121 | 143-317 | 290-1032 |
| `/contact/` | 1084 / **10824** | 0 | 27 / 0 | 325 / 314 | 437 / 545 |
| `/about /privacy /terms /payment-plan /brands-we-love` | 952-2112 | 0 to 0.001 | 0-106 | 165-467 | 177-1168 |
| `/checkout/` | 864 / 1108 | 0 / 0.003 | 0 | 323 / 387 | 124 |

- **LCP outliers (amplifiers phone 5.7 s, desktop 4.1 s on /shop/, ~10.8 s on several desktop pages)**: three different pages gave nearly the same value (10.8 s), and each page is fast on the other viewport and on re-runs (car-stereos desktop was 1.5 s in the first run, 11.2 s in a later run, mobile 1.3 s), so I treat them as proxy/network stalls, not confirmed site faults. The LCP element in the grid runs was a text paragraph (`P`), not an image. Label: unverified; re-test from a clean network or with CrUX before launch. If real, LCP>4 s is MUST-FIX.
- **Card grid, car-stereos (146 cards, 2,286 DOM nodes, 154 buttons)**: LCP 1.3-2.0 s (phone, normal vs 4x CPU throttle), CLS 0. Long tasks: 3 totaling ~345 ms over 50 ms at normal CPU (max 302 ms); with 4x CPU throttle 8 tasks, 1,387 ms over 50 ms, max 1,048 ms. A 900 ms task at ~1.0 s after load is the card render + facet pass. Interactions: facet filters (`data-shop-facet`) run client-side on all cards; I could not obtain real INP because scripted `dispatch_event` is not trusted input, so Event Timing recorded nothing. Facet clicks produced 100-300 ms long tasks only at 4x throttle. INP: unmeasured; expect "needs work" risk on low-end phones from the >1 s startup task. NICE.
- **Card grid, retrofit (125 cards, 3,644 nodes)**: LCP 1.0-1.3 s, CLS 0; long tasks 2 / 148 ms (normal), 11 / 1,413 ms over 50 ms (max 760 ms) at 4x throttle. 
- **Image weight (NICE, but heavy)**: car-stereos subcategory tiles and cards load full-size original `product.jpg/png` (naturalWidth up to 3000 px, displayed at 117-247 px) instead of the 400/800 px WebP variants used elsewhere: 40-47 oversized images; after a scroll test, phone image transfer was ~7.9-8.3 MB (32-35 JPEG, 7-9 PNG, 4 WebP) vs ~1.0 MB on retrofit. 151 of 153 images are `loading=lazy` there (good), but the first tile image has `fetchpriority=high`. Next step: use the existing `product-400.webp` srcset on the car-stereos tiles and cards. This is the largest speed gain for the grid.
- **Retrofit images (NICE)**: 40 of 128 images are `loading=eager` with `fetchpriority=high` (should be lazy except the first few); several images report 0x0 natural size (not yet loaded), `width=1200` attributes on 175 px sources.
- Cache: HTML `max-age=0, must-revalidate` (Phase 1), OK. Field Core Web Vitals not available (PageSpeed 429 in Phase 1); lab only.

## Summary of MUST-FIX items
1. G1 (decision gate): ~282 product pages are `noindex, follow`; confirm intent before launch, since they cannot rank or appear in AI Overviews while noindexed.
2. G2 (decision gate): shop root `/` serves the hub homepage (canonical www, tint title vs shop H1); decide the shop's indexable landing page.
3. B1: 52 product-card links on collection pages 404 after JS re-render (car-stereos 8, amplifiers 4, dash-cameras 7, enclosures 15, installation-parts 18); fix `shop-landing.js` to use the slug, not `row.id`.
4. C1: `/_vercel/insights/script.js` 404 (text/html) on every page produces a console error and loses analytics.
5. C2: `/api/checkout/?action=catalog` returns 500 on every shop page; add-to-cart never renders; fix or make it return an empty list.
6. LCP outliers of 4.1-10.8 s on some runs: unconfirmed lab flakes, re-test; if real they are MUST-FIX (LCP>4 s).
7. Car-stereos image weight (~8 MB on phone, 3000 px originals) and an unmeasured INP on a 146-card grid: NICE now, but fix before paid traffic.
8. No horizontal scroll, mixed content, missing viewport, page errors, CLS issues, or form/CTA breakage found on the pages tested.
9. Dash-cam product slug mismatch (sitemap `momento-momento-ic6` vs card `momento-ic6`): NICE.
10. All third-party/sister links (YouTube, Maps, Instagram, sister domains) are unverifiable from here.
