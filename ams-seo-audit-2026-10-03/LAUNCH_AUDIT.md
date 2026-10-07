# AMS pre-launch audit: LAUNCH_AUDIT.md

> **STATUS: FOR MORNING REVIEW (Zack + Tom). Nothing here has been applied.** No changes were made to any site or repo. Standing rules confirmed by Zack: **noindex is not approved**; every page and site stays live; fixes only improve pages (no delete, trim, merge or noindex). Items mentioning existing `noindex` tags describe what is already live and are decision gates for you both; this report adds no new noindex recommendation. Older per-site report files may still contain superseded advice; this file and the "SUPERSEDED RECOMMENDATIONS" sections in each AIO_REPORT.md are authoritative.

> **CORRECTION 2026-10-07: lacarstereo.com is already LIVE (confirmed by the team).** Earlier text that says "pre-launch", "if launching" or "intent unknown" is superseded. Re-checked the same day: robots.txt still blocks all crawlers except Google's ad bots and `/locations/`, and the home, FAQ, /book/ and most pages are still `noindex, nofollow` (sitemap rebuilt 2026-10-04, so the site is being deployed). A live site in this state is invisible to Google and AI Overviews, and its `/book/` form sends nothing, so booking requests are being lost now. Since noindex is not approved, treat both as live defects to review first.


Date: 2026-10-04. Read-only. Nothing was submitted, posted, changed, committed, pushed, deployed or deleted. No page or site is recommended for removal, merge, redirect-away or noindex.

Per-site detail (screenshots, probe.json, link checks): `~/ams-seo-audit-2026-10-03/<site>/launch/LAUNCH_NOTES.md`. SEO/AIO fixes are in `FIX_LIST.md`.

## How to read this
- **MUST-FIX** = blocks a clean launch (broken link/page/asset/CTA, form that loses leads, visible internal text, layout breakage on phone, launch-blocking robots/noindex).
- **NICE** = polish or hygiene.
- **[mount-proxy]** = the standalone domain's `www` host is blocked from this environment, so the check ran on the hub-mounted copy (`www.audiomotorsports.com/<mount>/`). The standalone may differ; its canonical host, robots, sitemap, redirects and TLS are unverified.
- **Lab numbers only.** No field data (CrUX/Search Console).
- **Environment noise, not site bugs (treated as such):** about 5% of connections through this sandbox reset or return 502, and CSS/JS sometimes loads as `text/plain` in the browser under parallel load. Those loads show LCP clustered near 10.6 s with a refused stylesheet. Each affected URL returned 200 with the right type on direct retry. Re-test performance from a real network before concluding anything. If real, LCP above 4 s becomes MUST-FIX.
- Forms were inspected only. No lead was created. Success states are unverified everywhere.

## Status by site
| Site | Audited as | Verdict |
|---|---|---|
| audiomotorsports.com (hub) | direct, 24 URLs, phone + desktop | 1 MUST-FIX (+ gate), rest NICE |
| shop.audiomotorsports.com | direct, 22 URLs | 4 MUST-FIX + 2 decision gates |
| lacarstereo.com | direct (apex), 56 probes | LIVE site with 10 MUST-FIX |
| teslatintla.com | direct (apex), 15 URLs + calculator/chat tests | 8 MUST-FIX |
| lacarbeats.com | [mount-proxy] /beats/, 22 URLs | no confirmed blockers; 2 conditional |
| lacartint.com | [mount-proxy] /tint/, 18 URLs | 3 MUST-FIX (+1 watch) |
| lacaralarm.com | [mount-proxy] /alarm/, 22 URLs | 5 MUST-FIX |
| amspods.com | [mount-proxy] /amspods/, 29 URLs, 175 crawled | 4 MUST-FIX + checks needed on real domain |

## A. MUST-FIX BEFORE LAUNCH (priority order)

### Lost leads, broken functions, wrong content
| # | Site / URL | Problem | Evidence | Exact next step |
|---|---|---|---|---|
| M1 | lacarstereo.com /book/ (live: requests lost now) | The form handler only pushes a `dataLayer` event and shows a success message. Name, phone and vehicle are never sent, so every booking request is silently lost. (The /packages/<car>/ quote form does POST to /api/quote/.) | lacarstereo launch notes | Wire /book/ to /api/quote/ (as the package form does) and test with one real lead after the fix. |
| M2 | shop.audiomotorsports.com collections | 52 product-card links 404 after JavaScript runs. `shop-landing.js` rebuilds each URL from the SKU id instead of the real slug (server HTML: `/shop/amplifiers/jbl-club-a600/`; rendered: `/kicker-club-a600/` → 404). Counts: car-stereos 8, amplifiers 4, dash-cameras 7 of 7, enclosures 15, installation-parts 18; Compustar brand page 1. Speakers, alarms, retrofit fine. | shop `broken_card_links.json` | Build card hrefs from the product slug in `shop-landing.js`. Re-run the card link check. |
| M3 | shop.audiomotorsports.com every page | `/api/checkout/?action=catalog&site=hub` and `site=shop` return HTTP 500; "Add to cart" buttons depend on it and never appear. `/_vercel/insights/script.js` returns 404 (console error, no analytics). | shop launch notes | Fix the catalog endpoint 500 (or confirm cart is intentionally off). Fix or remove the insights script tag. |
| M4 | Hub footer on all /tint/ pages (and the lacartint mount) | The "Aftercare" link goes to `/aftercare/` which 404s (confirmed twice). The page exists at `/tint/aftercare/` (200). | hub + lacartint launch notes | Change the footer/nav href to `/tint/aftercare/`. |
| M5 | lacartint mount /tint/tesla-tint/ [mount-proxy] | Tesla simulator assets all 404 under `/tint/tesla-tint/assets/sim/` (sim.css, app.js, prices.js, model-yl.png/.webp): simulator broken, console errors, broken image. Desktop shows 59 px horizontal overflow and LCP 10.7 s (probably the same cause; re-test after). | lacartint launch notes | Publish/point the simulator assets at their real path, then re-test overflow and LCP. |
| M6 | teslatintla.com /tesla-tint-carson/ | Title, H1, breadcrumb, meta description and FAQ say "Avalon" (61 mentions vs 14 for Carson). Hero image, canonical, sitemap and schema say Carson. | teslatintla launch notes | Replace Avalon with Carson in title, H1, breadcrumb, description and FAQ copy. |
| M7 | teslatintla.com /es/ | The calculator preview is broken: relative asset paths resolve under /es/ and 404 (car image, tint mask). | teslatintla launch notes | Make the asset paths root-relative. |
| M8 | Internal instruction text visible on public pages: lacaralarm mount (Irvine "Never imply nearby." ×6, "Do not reverse that." ×2, "We do not invent an Irvine storefront" ×6, "Mickey Mouse" ×3; Torrance similar; "Do not reverse that." is inside the FAQPage JSON-LD; /alarm/blog/ "We do not invent a sixth brand for a post."; likely ~100 other drive-in pages) [mount-proxy]; amspods mount ("that is the schema aggregate only" on 38 city pages; "We do not invent..." on 44 pages, ~113 with variants incl. /specials/, /reviews/, /payment-plan/) [mount-proxy] | Visible, quotable internal voice. | lacaralarm, amspods launch notes | Rewrite as customer-facing copy in the shared city/service templates and regenerate FAQ schema. Re-grep rendered pages for the phrases. |
| M9 | lacarstereo.com /cart/, /gallery/, /shop/dash-cameras/ | Visible dev notes ("TBD, Zack (...)"). Cart and Gallery are placeholders but are in the nav/footer. | lacarstereo launch notes | Remove the notes. Finish or honestly label /cart/ and /gallery/. |

### Launch gates (indexing / host / metadata)
| # | Site / URL | Problem | Next step |
|---|---|---|---|
| G1 | lacarstereo.com | `noindex, nofollow` on 124 of 127 pages, `robots.txt` `Disallow: /` for all but AdsBot; Googlebot Allow only for /locations/. Site is **live**, so it is invisible to search today. Both the page tags and robots.txt need to change (one decision). | Remove the noindex in the layout template (leave any existing tags on /cart/ and /book/ as they are; add no new noindex) and replace robots.txt with an open policy. Fix the robots Sitemap host. |
| G2 | lacarstereo.com host + metadata | Apex serves 200, no redirect to www, yet every canonical, og:url, sitemap entry, JSON-LD @id and the robots Sitemap line use www. 26 pages have no canonical. `og:url` is the home URL on 124 pages. og:image/twitter:image missing on all 125 fetched pages. apple-touch-icon and web manifest 404. No GA4/GTM tag found. llms.txt 404. All sitemap lastmod identical. | Pick one canonical host and redirect the other. Add self-canonicals and per-page og:url. Add default og:image and apple-touch-icon. Install analytics. Publish llms.txt. Use real per-page lastmod. |
| G3 | shop.audiomotorsports.com ~282 product pages | `noindex, follow` (re-confirmed on Kicker 46CSC654, JBL Club A600, JVC KW-M56BT, Viper 3108V). Only 3 Momento dash cams lack it. If launch intends products to rank, this blocks launch. | Confirm intent; if not intended, remove the tag in the product template (staged: priced products first). |
| G4 | shop.audiomotorsports.com `/` | Serves the hub homepage: hub canonical, tint title vs stereo H1. `/shop/` is self-canonical. | Decide the shop's landing page and align title, H1, canonical. |
| G5 | amspods mount | 85 of 111 city pages are `noindex, follow` (26 indexable incl. West Carson, Torrance). Phase 1's amspods report said no robots meta, so this needs one confirmation. | Confirm intent. If unintended, remove the tag and add unique local content (never remove pages). |

### Phone layout / UX breakage
| # | Site / URL | Problem | Next step |
|---|---|---|---|
| U1 | teslatintla.com home, phone | The calculator's fixed price bar is wider than the screen and clips the NEXT button; Book a Slot / Text Nick / Payment Plan buttons stack over the price. A second sticky bar (Text Nick / Call) overlaps the price bar and content. After the calculator loads the page is wider than 390 px (scrollWidth 414–476; causes: blog card row, hidden chat panel). | Constrain the price bar to viewport width, stack/merge the sticky bars, fix the overflowing blog row and hidden chat panel. |
| U2 | teslatintla.com chat | On phone the chat panel is clipped off the right edge (358 px wide at x=106), hiding Close and Send. The launcher covers "Text Nick" on city pages and Model/Year/Day fields on /book/. | Fix chat panel width/position; keep the launcher clear of CTAs and form fields. |
| U3 | teslatintla.com 404 page | On nested URLs it loads no CSS or logo (relative asset paths); renders as unstyled Times text. (404 status and noindex are correct.) | Use root-relative asset paths in the 404 template. |
| U4 | lacaralarm mount product page (hub shop) [mount-proxy] | Related-product image boxes blank; sticky bar overlaps the purchase block. | Check image sources and sticky-bar z-index/padding on product pages. |
| U5 | lacaralarm mount service-page forms [mount-proxy] | `action=""`, so they depend on JS; contact form has a required "old tint" select (tint-form leftover); honeypot named `company` on contact/book but `_honey` on service pages. | Confirm the handler attaches, remove the leftover field, standardize the honeypot name. |
| U6 | amspods mount /amspods/payment-plan/ [mount-proxy] | Desktop CLS 0.508, reproduced in two runs. | Reserve space for late-loading content on that page; re-measure. |

### Must be verified on the real domains (blocked here)
| # | Item | Why |
|---|---|---|
| V1 | `www.lacarbeats.com`, `www.lacartint.com`, `www.lacaralarm.com`, `www.amspods.com`, `www.lacarstereo.com`, `www.teslatintla.com`, and `shop.lacarbeats.com`, `shop.lacartint.com`, `shop.lacaralarm.com`, `shop.amspods.com`, `shop.teslatintla.com` | Proxy blocked. Every [mount-proxy] result above may differ on the standalone. Check canonical, og:url, hreflang, JSON-LD host, robots.txt, sitemap.xml, llms.txt, TLS and the apex-to-www redirect (http hits two 308 hops on lacartint/lacaralarm/lacarbeats). |
| V2 | amspods footer city links (montrose, burbank, san-marino, rowland-heights, encino, hollywood) | Root-relative in the hub-wide footer; 200 on the mount, likely 404 on the amspods.com apex. Test on www.amspods.com. |
| V3 | shop.amspods.com (14 links on /amspods/shop/ and home), shop.lacarbeats.com (14 product URLs), shop.teslatintla.com (linked sitewide), lacaralarm home links to shop.lacaralarm.com | Click-test each on the real hosts. |
| V4 | Forms everywhere (/book/, /contact/, quote forms) | Submit one test lead per site after fixes; confirm the `/api/quote/` success state, honeypot behavior and lead attribution (lacarbeats service form has no `source_page`). |
| V5 | Root-relative links on mounts (`/west-carson/`, `/shop/...`, `/api/quote/`, 458 of lacarbeats' 633 links are hub-root paths) | Verify they stay on the standalone domain. |
| V6 | Edge logs | The hub host returned intermittent 502/`text/plain` CSS/JS in about 12 of 48 loads in this sandbox. Check Vercel logs for 502s on the audit night to rule out a real intermittent fault. |

## B. NICE-TO-HAVE
- **Developer text in public source:** hub `/tint/` and `/beats/` (and likely all mounts) carry well-formed HTML comments ("quote plugin / INSERT after ... guinea pig") and a "TODO Zack" comment near line 408 of `/tint/`. **They are not visible on screen** (Phase 1's "visible stray text" finding is withdrawn). Strip them anyway, because tag-stripping scrapers print them.
- **"Closed today" banner:** hidden except on Pacific Sundays, then 132 px (phone) / 67 px (desktop) tall at the very top of /, /tint/, /alarm/, /beats/ (and in the DOM on /tesla/): it pushes the header and hero down (layout shift) and is the first text snippet extractors read. Add `data-nosnippet`, reserve its space or make it overlay.
- **Phone first screen:** hero is a portrait video/poster with the text baked into the image and a large empty band; H1 and in-hero CTAs sit at or below the fold and are partly covered by the sticky Text Nick / Call bar on hub /tint/, /malibu/, lacartint, lacaralarm (home and city pages), lacarbeats, amspods and lacarstereo home (9:16 poster, text in the image, real H1 below the fold). Sticky bars and the chat bubble overlap content on /beats/, /book/, shop cards, lacarbeats hero title.
- **Performance (lab, probably noisy):** teslatintla home loads 10 render-blocking stylesheets (about 20 KB brotli; cost is request count) and a 501 KB 2560 px desktop hero (mobile 249 KB; no srcset between 768 and 2560 px). Shop car-stereos (146 cards, 2,286 DOM nodes) loads originals up to 3000 px at 117-247 px display, about 7.9-8.3 MB on phone vs about 1 MB for retrofit; long tasks about 0.35 s (about 1.4 s at 4x throttle); retrofit has 40 of 128 images `eager` + `fetchpriority=high`. Tint pages 2.6-3.7 MB; /tint/es/ about 5.3 MB. amspods hero mp4 about 3.2 MB. Hub /reviews/ phone LCP 4.5 s in one run. INP not measurable with scripted clicks.
- **Metadata:** hub /stereo/ 74-char description and no OG image; /reviews/ 39 chars; lacarbeats blog/shop descriptions 73-105 chars, /beats/book/ no JSON-LD; amspods Spanish titles 68-69 chars and descriptions 162-194 chars; unused image preloads on /tint/es/, /tint/contact/, /tint/shop/; shop 404 page canonical is `www.audiomotorsports.com/404.html`; shop dash-cam sitemap URL (`momento-momento-ic6`) differs from the card link (`momento-ic6`); no `/cart/` or `/returns/` on shop; direct `/checkout/` shows an error message.
- **Cross-brand copy:** lacarstereo "Text us" number (213-429-1092) differs from the schema phone (310-513-8800); the hub `/es/` hero image is hosted on lacarbeats.com (unverified; serve from the hub); teslatintla `/es/` links and hero text are English and `/es/` is not in the sitemap; teslatintla 30 px desktop overflow on the Model Y blog post.
- **Tap targets / console noise:** small tap targets on nearly every page (8-32 per page); YouTube embeds log harmless `web-share` / `allowfullscreen` warnings; lacarbeats `/beats/shop/` header text rendered white-on-white in one run where a shop stylesheet failed (conditional, re-test).
- **Redirect hops:** http apex goes through two 308 hops on several brand apexes; HSTS has no includeSubDomains/preload. Brand apex certificates (Let's Encrypt) expire 2026-11-08; confirm auto-renewal.
- **Unlinked 404s (no action unless linked externally):** hub `/tint/window-tint-carson/`, `/alarm/car-alarm-carson/` (give it a branded 404; check GBP/old sitemaps), amspods `/amspods/es/locations/`, `/privacy-policy/`, `/terms-of-service/`, `/amspods/pods/` (pods live at /amspods/services/ams-pods/, /shop/, /catalog/).

## C. What was clean (verified)
- No mixed content and no uncaught JS page errors on any audited page.
- No horizontal scroll on phone except the items listed (teslatintla home; lacartint Tesla desktop).
- Viewport meta present everywhere; titles, descriptions and favicons present on probed pages; no broken images on probed pages (lacartint /tint/locations/ and /tint/shop/ have 113 images missing alt, an SEO item in FIX_LIST).
- CLS under 0.04 on nearly all pages (exceptions: amspods payment-plan 0.508; lacartint Tesla desktop overflow).
- Link integrity: hub 581 same-site links, 580 OK (only /aftercare/ fails); lacarstereo 69 reachable links all 200; lacarbeats 633 of 633 OK; amspods 460 hub-path links OK; teslatintla 85 same-site links OK (plus the intentional 404 test URL); lacartint 589 hub-wide links with only /aftercare/ confirmed 404.
- Forms inspected: all POST to `/api/quote/` (or `/api/reserve/`) with honeypot fields and sensible required fields; teslatintla /book/ has no visible captcha; contact forms carry a hidden `_captcha` field. Teslatintla calculator reprices correctly (Y L full car $399, Model 3 $369, 3M Ceramic IR full car $569).
- Clean-load LCP is 0.8-2.8 s on hub, lacarstereo (worst 1.98 s), lacartint, lacaralarm and lacarbeats, and 1.0-2.7 s on teslatintla.

## D. Limits of this audit
Lab-only speed; about 5% sandbox connection loss; some pages judged from metrics rather than screenshots (lacarstereo: ~10 of 56 screenshots viewed); blocked hosts (all brand `www`/`shop.*` hosts, YouTube, Google Maps/share, Instagram, Yelp, OfferUp, Facebook, GTM) unverifiable; no Search Console, GBP, CrUX or real AI-engine data; no form submissions or purchases (intentional); the four brand domains are audited through the hub's mounted copies.
