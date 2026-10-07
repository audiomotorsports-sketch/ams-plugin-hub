# LAUNCH NOTES: lacarstereo.com (Phase 2 pre-launch audit)

Date: 2026-10-04 (UTC). Read-only. No form submitted, no POST sent (only GET/HEAD; one GET to /api/quote/ returned 405). Host audited: apex https://lacarstereo.com (200). Evidence: curl re-fetch of all 127 sitemap URLs today, plus Playwright probe (phone 390x844, desktop 1366x900) of 28 URLs. Screenshots in `shots/`, raw data in `shots/*/probe.json`, link table in `link_status.tsv`.

## Limitations
- https://www.lacarstereo.com is blocked by the egress proxy, so the www host, www-to-apex or apex-to-www redirect, and www TLS are UNVERIFIED. Note: everything on the site declares www as canonical host (sitemap, og:url, JSON-LD, robots Sitemap line, canonicals) while the apex serves 200 with no redirect. http://lacarstereo.com 308s to https://lacarstereo.com/ (verified).
- Sister sites lacarbeats/lacartint/lacaralarm/amspods return 403 via proxy: unverifiable from here. bit.ly/4ivQhAz (Google Maps short link on /locations/) 403: unverifiable.
- The sandbox network is flaky: about 5% of requests (even sequential curl) end in connection timeout or TLS reset (6 of 120 in my repeat test, no HTTP 502 seen in curl). The probe also logged sporadic 502 "text/plain" JS chunk responses and `/fit/?_rsc` ERR_ABORTED (prefetch cancellations, normal). Treat these as probable proxy artifacts, not site bugs; re-test from a real network before launch. After a sequential retry, all 69 reachable nav/footer/CTA links return 200.
- Lab numbers are not field data (no CrUX available).

## Re-verified today: indexing controls (intent unconfirmed)
Intent is NOT confirmed by any file: this may be a deliberate staging state. For a pre-launch audit these are MUST-FIX-BEFORE-LAUNCH items that must be removed at go-live.

1. MUST-FIX-BEFORE-LAUNCH. Sitewide meta robots `noindex, nofollow`. Where: 124 of 127 sitemap URLs (re-fetched all 127 today; 122 first pass plus 2 retried after transient resets). Also /cart/, /contact/, /reviews/, /packages/<car>/ and /retrofit-screens/ (noindex, nofollow), /fit/ (noindex, follow), 404 template (noindex, fine). Indexable (`index, follow`): /locations/, /privacy/, /terms/ only. No X-Robots-Tag header on any page. Next step: remove the noindex in the shared metadata at go-live, keep it deliberately only on /cart/ and /fit/ if wanted, then re-crawl all 127 and confirm.
2. MUST-FIX-BEFORE-LAUNCH. robots.txt (197 bytes, 200, today): AdsBot-Google and AdsBot-Google-Mobile `Allow: /`; Googlebot `Allow: /locations/` only; `User-Agent: *` `Disallow: /`; Sitemap line points to www host. All of Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot are blocked. Googlebot's group has no Disallow so it can crawl everything (and sees the noindex). Next step: at go-live replace with one `User-agent: *` group that allows the site (optionally disallow /cart/ and /api/), and a Sitemap line on the chosen canonical host. While `Disallow: /` stays, crawlers cannot even see a noindex removal.

## Launch-readiness checklist (status today)
| Item | Status | Evidence |
|---|---|---|
| Remove noindex | FAIL (blocking) | see above |
| robots.txt open | FAIL (blocking) | see above |
| Canonical host + www redirect | FAIL, partly unverifiable | Apex 200, no redirect to www; every canonical/og:url/sitemap/JSON-LD uses www. www unreachable from here. Pick one host, 301 the other, make all references agree. |
| Canonical tags | FAIL | 26 of 127 pages have no canonical (home, 6 categories, /install/ + 7 install pages, /packages/, /faq/, /about/, /gallery/, /brands/, /locations/, /book/, etc.). 101 product pages have self canonical on www. |
| og:url | FAIL (MUST) | og:url is `https://www.lacarstereo.com/` (the home page) on 124 of 125 fetched pages; only /locations/ differs. Every share/preview of an inner page claims the home page URL. Fix the metadata template to emit per-page URL. |
| og:image / twitter:image | FAIL | 0 of 125 sitemap pages have og:image or twitter:image (twitter:card=summary_large_image is set, so previews are image-less). /packages/<car>/ pages do have a generated og:image. Add a default og:image (1200x630) in the layout. |
| Favicon | PASS | /favicon.ico 200 (25,931 bytes, 256x256), `<link rel=icon>` present. |
| apple-touch-icon / manifest | NICE | /apple-touch-icon.png, /apple-icon.png, /manifest.webmanifest all 404; no `<link rel=apple-touch-icon>`. |
| Sitemap lastmod | NICE | 127 URLs, every lastmod is the same value `2026-10-04T01:43:08.821Z` (build timestamp), so it carries no signal. Use true per-page modification dates. Sitemap also lists www URLs, not apex. |
| llms.txt | FAIL (NICE) | /llms.txt returns 404 (served as the custom 404 page). Not used by Google Search; still part of the checklist. Publish a short factual llms.txt (shop, NAP, services, key URLs). Also no /ai.txt. |
| Analytics | FAIL (verify) | No GA4/GTM/gtag script found in page HTML or loaded chunks; events (`book_install`, `quote_request`, call/text clicks) only push to `window.dataLayer`, which nothing consumes. Add the tag at launch or conversion tracking is blank. Unverified whether it is injected by a consent tool. |
| Search Console verification | PASS | `google-site-verification` meta present on home. |
| Viewport, lang, JSON-LD | PASS | viewport on all probed pages, `<html lang>` on all 125, JSON-LD on all 125. |
| Security headers, HTTPS | PASS | HSTS, nosniff, DENY framing, referrer and permissions policy present. |
| 404 handling | PASS | Unknown path returns real 404 (noindex). No-slash URLs 308 to slash. |

## (a) Visual: phone + desktop
No horizontal overflow on any page, either viewport (overflow_x = 0 on all 56 probes). No broken images (0). No layout shift problems (max CLS 0.034).
- Home, phone. NICE-TO-HAVE/verify. The hero is a 9:16 baked-in poster image (about 1500 px tall at 2x) containing "CHAT WITH JESSIE", the phone numbers and a large empty dark area. The real H1 "Wireless CarPlay, installed today." and the year/make/model picker are below the fold on phone; only the sticky Call/Text/Book bar is an above-the-fold CTA. Text is embedded in the image (not readable by crawlers or screen readers; alt was empty on logo). Next step: shorten the phone hero to about 60% viewport so H1 and the fit picker show, and put the phone numbers in live text. A "Jessie" chat/arrow in the image points at a control I could not see in the screenshot (unverified).
- Home, desktop: hero, nav, CTA fine; picker visible above fold at 1366x900.
- Sticky bottom bar (Call / Text / Book) on phone covers the bottom of content in full-page captures. NICE: confirm the page has bottom padding so the last form button on /book/ and package forms is not hidden behind it when scrolled to the end (capture shows the submit button partly under the bar mid-page, which is a full-page screenshot artifact; verify on a device).
- /cart/, /gallery/, /shop/dash-cameras/: amber "TBD, Zack" notes visible (see bugs).
- /book/ phone: clean, labels readable, inputs full width.
- Install pages, category pages, product pages, /packages/, /packages/2010-2014-ford-mustang/, /faq/, /about/, /brands/, /locations/: no clipped text or overlap spotted in the screenshots viewed (cart, gallery, dash, book, home, plus structural metrics for all). Not every screenshot was visually inspected; the remainder are judged on metrics (no overflow, no broken images) and are labeled so.
- Small tap targets: 17 to 20 links/buttons under 32 px on phone per page (mostly footer text links and nav). NICE: pad footer links to 44 px.

## (b) Click-through
Link statuses (sequential re-test, 74 unique hrefs gathered from all probed pages): 69 x 200, 0 x 404, 0 x 3xx unresolved. The other 5 are unverifiable here (three sister sites 403, bit.ly 403, amspods 403); teslatintla.com 200 and audiomotorsports.com 200.
- Primary nav (CarPlay Stereos, Subwoofers, Amps, Speakers, Packages, Install, Gallery, Cart) and footer (Install, Packages, Dash screens, Pay Later, Gallery, FAQ, About, Contact, Where we are, Reviews, Book, Privacy, Terms): all 200.
- Header phone `tel:+13105138800`; "Text us" `sms:+12134291092` (a different number, (213) 429-1092, which is also baked into the home hero). NICE: confirm the SMS number is intentional and listed as a contact point (schema telephone is only the 310 number).
- Package pages "Request an install day" goes to /book/. Mailto fallback uses audiomotorsports@gmail.com (a personal-style Gmail address on a public page): NICE confirm intended.
- /retrofit-screens/ page is 431 KB HTML and returns 200 (not in primary nav; in sitemap).
- /locations/: 123 cities counted (West Carson 1.8 mi through Lancaster 86.8 mi). Cities are plain list items, not links; no per-city URLs exist. Per the rules no page removal is suggested; improvement path is unique local content and links per city or region, a map embed, and honest copy ("We serve the entire LA area" vs 86.8 mi).

Forms (inspected only):
- /book/ (MUST-FIX). Fields: service (select, req), vehicle (text, req), day (select, req), slot (select, req), name (req), phone (tel, req). No action, method GET, no captcha, no honeypot. Source of the JS handler (chunk loaded by /book/): `onSubmit` calls preventDefault, pushes `{service, slot}` to `window.dataLayer` (`book_install`) and shows the success state, with no fetch/XHR/beacon. Name, phone and vehicle are never transmitted. The success message says "will text you ... Nothing is booked until you get that text", but no one is notified. As deployed, every booking request is silently lost. Next step: wire the form to the same backend as /api/quote/ (or an equivalent) and have success appear only after a 2xx; add the same honeypot and consent as the package form; test by submitting from staging, not from this audit.
- /book/ day list is hard-coded in the page HTML (Mon Oct 5 to Sat Oct 10, generated at build). Unverified whether it regenerates; if the site is not rebuilt daily, the dates go stale (NICE/verify; the sitemap lastmod suggests a single build time).
- /packages/<car>/ lead form (e.g. 2010-2014 Ford Mustang): fields want, name, how (text or email), contact (tel, required), note, sms_consent checkbox (not required), `company` (honeypot), hidden renderedAt timestamp; it POSTs JSON to /api/quote/ with an error fallback "Call (310) 513-8800". GET /api/quote/ is 405 (route exists). Not submitted. NICE: when "Email me" is chosen the field is still a type=tel "Mobile number" required input, so an email address would not be collected correctly; verify.
- Home year/make/model fit picker: a form (1) present; not submitted.
- /cart/: no form; text says cart is not built (see bugs).

## (c) Bugs
MUST-FIX
1. /book/ submit sends nothing (above).
2. Leaked internal text on live pages, rendered in amber boxes:
   - https://lacarstereo.com/cart/: "TBD, Zack (cart + checkout: blocked on the ams-commerce order API and Stripe setup)"
   - https://lacarstereo.com/gallery/: "TBD, Zack (gallery: needs the bay shoot (30-40 photos) + 6-10s silent video loops cut from the YouTube installs)". The gallery page is an empty placeholder, and Gallery is in the primary nav and footer.
   - https://lacarstereo.com/shop/dash-cameras/: "TBD, Zack (dash camera prices: all 7 are 'call to confirm' on the old shop, see ZACK-QUESTIONS #27)". Also 5 of 7 cameras show "Call to confirm" with no price.
   Elements carry `data-tbd` attributes; searching the other 124 fetched pages found no other TBD, TODO, lorem or "Zack" text. Next step: remove or hide the `data-tbd` notice component in production, finish or hide the placeholder content, and gate Cart and Gallery in nav until real. (Never remove the page itself.)
3. og:url points to the home page on 124 pages (see checklist).
4. noindex and robots Disallow (see above).
NICE-TO-HAVE
5. No og:image / twitter:image on any sitemap page; no apple-touch-icon.
6. 26 pages lack canonical; host www vs apex mismatch.
7. Title and heading polish: /locations/ title is "Locations | LA Car Stereo | LA Car Stereo" (brand repeated) and its H1 is only "LA Car Stereo". /locations/ also has two LocalBusiness-type JSON-LD blocks with different @id and areaServed (home: 10 cities; locations: State of California) and a Sunday `opens 00:00 closes 00:00` specification that can read as open 0 hours or all day; use closed (no entry) instead.
8. Home hero images: baked text, phone hero too tall (see (a)). Home loads `lacarstereo-banner-1003-jessie-long-*.mp4` which the probe logged as ERR_ABORTED (video request cancelled after load; likely normal range request cancel, verify playback).
9. Product image `src` fallback is the 3840 px variant (`_next/image?...w=3840`) in `<img src>` with srcset; fine on modern browsers but old clients download the largest size. NICE.
10. Console: 0 page errors and 0 mixed-content requests on all 56 probes. Console errors seen (502 + "Refused to execute script ... MIME text/plain") occurred on 8 of 56 probes, on different chunk files each time, never reproduced in 120 follow-up curl fetches: probable proxy artifact, re-test from a real network.
11. Intermittent connection resets to the apex from this sandbox (about 5%); verify with an external uptime check before launch.

## (d) Speed / lab CWV (Chromium, via proxy, no throttling; lab is not field)
Worst case across all 56 probes: LCP 1,984 ms (/shop/wiring-dsp/ desktop), CLS 0.034 (home desktop), longest TBT-proxy 543 ms (/install/stereo/ phone, a single run; others 0 to 144 ms), TTFB 113 to 743 ms (home phone 743 ms cold). No page reaches the MUST-FIX thresholds (LCP > 4 s, CLS > 0.25). Home phone transfer 762 KB / 32 requests; home desktop 793 KB / 62 requests; category pages 240 to 595 KB.

| URL | view | LCP ms | CLS | TBT-proxy ms | TTFB ms | transfer KB | requests | H-overflow px | small taps |
|---|---|---|---|---|---|---|---|---|---|
| / | phone | 1696 | 0 | 17 | 743 | 762 | 32 | 0 | 20 |
| / | desktop | 1028 | 0.034 | 27 | 365 | 793 | 62 | 0 | 35 |
| /install/ | phone | 724 | 0 | 46 | 131 | 292 | 32 | 0 | 19 |
| /install/ | desktop | 712 | 0 | 37 | 236 | 334 | 53 | 0 | 33 |
| /install/carplay/ | phone | 936 | 0 | 43 | 304 | 309 | 31 | 0 | 20 |
| /install/carplay/ | desktop | 680 | 0 | 0 | 197 | 372 | 62 | 0 | 36 |
| /install/stereo/ | phone | 1276 | 0 | 543 | 540 | 321 | 35 | 0 | 20 |
| /install/stereo/ | desktop | 720 | 0 | 0 | 163 | 375 | 64 | 0 | 36 |
| /install/subwoofer/ | phone | 892 | 0 | 67 | 372 | 321 | 35 | 0 | 20 |
| /install/subwoofer/ | desktop | 788 | 0.017 | 15 | 275 | 375 | 64 | 0 | 36 |
| /install/amplifier/ | phone | 748 | 0.0 | 11 | 170 | 299 | 35 | 0 | 20 |
| /install/amplifier/ | desktop | 672 | 0.017 | 0 | 124 | 375 | 64 | 0 | 36 |
| /install/speakers/ | phone | 888 | 0 | 0 | 396 | 322 | 35 | 0 | 20 |
| /install/speakers/ | desktop | 1040 | 0.017 | 20 | 378 | 375 | 64 | 0 | 36 |
| /install/dsp/ | phone | 548 | 0 | 14 | 163 | 316 | 32 | 0 | 20 |
| /install/dsp/ | desktop | 676 | 0.017 | 10 | 260 | 205 | 14 | 0 | 36 |
| /install/luxury/ | phone | 1052 | 0 | 101 | 418 | 308 | 31 | 0 | 20 |
| /install/luxury/ | desktop | 1064 | 0 | 0 | 653 | 372 | 62 | 0 | 36 |
| /packages/ | phone | 432 | 0 | 2 | 137 | 338 | 34 | 0 | 17 |
| /packages/ | desktop | 1280 | 0 | 12 | 269 | 362 | 46 | 0 | 32 |
| /packages/2010-2014-ford-mustang/ | phone | 696 | 0 | 68 | 274 | 364 | 40 | 0 | 28 |
| /packages/2010-2014-ford-mustang/ | desktop | 1008 | 0.0 | 106 | 186 | 341 | 55 | 0 | 43 |
| /shop/carplay-stereos/ | phone | 760 | 0 | 5 | 293 | 445 | 26 | 0 | 17 |
| /shop/carplay-stereos/ | desktop | 716 | 0.0 | 30 | 160 | 430 | 86 | 0 | 32 |
| /shop/subwoofers/ | phone | 788 | 0 | 3 | 393 | 301 | 28 | 0 | 17 |
| /shop/subwoofers/ | desktop | 932 | 0.007 | 85 | 272 | 455 | 90 | 0 | 32 |
| /shop/amplifiers/ | phone | 700 | 0 | 13 | 277 | 381 | 45 | 0 | 17 |
| /shop/amplifiers/ | desktop | 992 | 0.001 | 37 | 247 | 403 | 80 | 0 | 32 |
| /shop/speakers/ | phone | 784 | 0 | 0 | 368 | 575 | 50 | 0 | 17 |
| /shop/speakers/ | desktop | 1344 | 0.001 | 119 | 281 | 594 | 96 | 0 | 32 |
| /shop/wiring-dsp/ | phone | 724 | 0 | 32 | 235 | 476 | 50 | 0 | 17 |
| /shop/wiring-dsp/ | desktop | 1984 | 0.001 | 57 | 436 | 559 | 100 | 0 | 32 |
| /shop/dash-cameras/ | phone | 1072 | 0 | 93 | 257 | 368 | 42 | 0 | 17 |
| /shop/dash-cameras/ | desktop | 452 | 0 | 0 | 113 | 380 | 68 | 0 | 32 |
| /shop/carplay-stereos/pioneer-dmh-1800nex/ | phone | 1216 | 0 | 13 | 440 | 291 | 25 | 0 | 19 |
| /shop/carplay-stereos/pioneer-dmh-1800nex/ | desktop | 1608 | 0.001 | 36 | 490 | 340 | 54 | 0 | 34 |
| /faq/ | phone | 640 | 0 | 0 | 179 | 273 | 23 | 0 | 18 |
| /faq/ | desktop | 740 | 0.001 | 0 | 310 | 294 | 38 | 0 | 33 |
| /about/ | phone | 712 | 0 | 0 | 263 | 308 | 42 | 0 | 17 |
| /about/ | desktop | 676 | 0 | 41 | 239 | 329 | 56 | 0 | 32 |
| /gallery/ | phone | 916 | 0 | 14 | 200 | 308 | 42 | 0 | 18 |
| /gallery/ | desktop | 1140 | 0 | 49 | 350 | 329 | 56 | 0 | 33 |
| /locations/ | phone | 824 | 0 | 0 | 306 | 278 | 23 | 0 | 17 |
| /locations/ | desktop | 1040 | 0.005 | 17 | 530 | 294 | 34 | 0 | 33 |
| /cart/ | phone | 992 | 0 | 0 | 305 | 308 | 42 | 0 | 20 |
| /cart/ | desktop | 448 | 0 | 0 | 115 | 329 | 56 | 0 | 35 |
| /book/ | phone | 888 | 0 | 144 | 384 | 273 | 23 | 0 | 19 |
| /book/ | desktop | 628 | 0 | 19 | 244 | 330 | 56 | 0 | 34 |
| /brands/ | phone | 612 | 0 | 82 | 132 | 242 | 14 | 0 | 17 |
| /brands/ | desktop | 600 | 0 | 0 | 276 | 301 | 40 | 0 | 32 |
| /shop/amplifiers/jbl-club-a600/ | phone | 724 | 0 | 0 | 184 | 285 | 25 | 0 | 19 |
| /shop/amplifiers/jbl-club-a600/ | desktop | 948 | 0 | 22 | 370 | 333 | 54 | 0 | 34 |
| /shop/subwoofers/kicker-loose-woofers-48cwrt122/ | phone | 1056 | 0 | 0 | 302 | 285 | 25 | 0 | 19 |
| /shop/subwoofers/kicker-loose-woofers-48cwrt122/ | desktop | 1000 | 0.001 | 81 | 237 | 335 | 54 | 0 | 34 |

Note: the phone numbers above come from a proxied sandbox; real-device LCP will differ. Install pages /install/dsp/ show 14 requests on desktop because a JS chunk failed (probe artifact).

## Pages and routes covered
Home; /install/ and all 7 children (carplay, stereo, subwoofer, amplifier, speakers, dsp, luxury); /packages/ and /packages/2010-2014-ford-mustang/; 6 category pages (carplay-stereos, subwoofers, amplifiers, speakers, wiring-dsp, dash-cameras); 3 product pages (pioneer-dmh-1800nex, jbl-club-a600, kicker-loose-woofers-48cwrt122); /faq/, /about/, /gallery/, /locations/, /cart/, /book/, /brands/. Plus curl-only: /contact/, /reviews/, /fit/, /payment-plan/, /retrofit-screens/, all 127 sitemap URLs for robots/canonical/og checks. Note: /locations/ is a single page listing 123 cities, there are no per-city URLs, and no blog exists, so the standard "3 city pages" and "blog" samples do not apply.

## MUST-FIX summary (10 lines)
1. Remove `noindex, nofollow` from 124 of 127 pages at go-live (intent unconfirmed; keep only deliberately on /cart/ and /fit/).
2. Replace robots.txt (`Disallow: /` for all non-Google bots, Googlebot allow-only /locations/) with an open policy; fix the Sitemap host.
3. Choose one canonical host, 301 the other (www unverifiable here), and make canonical, og:url, sitemap, JSON-LD and robots agree.
4. /book/ form transmits nothing (dataLayer only) yet shows a success message: wire it to a backend before launch.
5. Remove the visible "TBD, Zack (...)" dev notes on /cart/, /gallery/ and /shop/dash-cameras/.
6. Fix og:url (home URL on 124 pages) and add per-page canonicals on the 26 pages that lack one.
7. Resolve /cart/ (not built) and /gallery/ (empty) being primary nav and footer destinations; finish or label honestly.
8. Add an og:image/twitter:image default (0 of 125 pages), plus apple-touch-icon (404).
9. Install analytics (none found; dataLayer events go nowhere) and publish llms.txt (404) and real per-page sitemap lastmod values (all identical).
10. Re-test from a real network for the intermittent connection resets and 502-on-chunk errors seen via the sandbox proxy, and verify www.
