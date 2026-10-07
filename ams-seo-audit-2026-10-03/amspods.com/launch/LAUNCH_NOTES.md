# amspods.com Phase 2 launch audit (2026-10-04)
All findings are [mount-proxy]: audited https://www.audiomotorsports.com/amspods/ (hub mount). www.amspods.com / shop.amspods.com are proxy-blocked, so nothing here proves how the apex serves.

## Apex headers (recorded)
- `curl -I https://amspods.com/` -> HTTP/2 308, location https://www.amspods.com/, refresh 0;url=..., server Vercel, HSTS max-age=63072000, cache-control public,max-age=0,must-revalidate. Same 308 -> www for /robots.txt, /sitemap.xml, /llms.txt. www.amspods.com unreachable (proxy) = unverifiable.
- Mount /amspods/ -> 200, text/html, x-vercel-cache HIT, x-frame-options SAMEORIGIN, nosniff, referrer-policy strict-origin-when-cross-origin, permissions-policy locks geo/mic/camera.
- Mount has no /amspods/robots.txt or /amspods/sitemap.xml (404; site-level hub files are served from root). Apex robots/sitemap unverifiable.

## Scope covered
Crawled 175 mount pages (home, services x20 incl. Road Glide/Street Glide/Road King/bagger-builds/harley-radio, catalog x14, shop, build-your-own, faq, about, specials, reviews, gallery, payment-plan, contact, locations, blog index + 4 posts, 9 /es/ pages, 111 city pages). Lab-probed 29 URLs phone+desktop (probe1-4 folders: screenshots + probe.json). Linked 460 root/hub targets status-checked: all 200 or 308 (no 404).
Note: there is no /amspods/pods/ (404; pods live at /amspods/services/ams-pods/, /amspods/shop/, /amspods/catalog/). /amspods/es/locations/, /privacy-policy/, /terms-of-service/ are 404 but nothing links to them. No separate product pages on the mount: product links go to shop.amspods.com (blocked, unverifiable; 14 product/category links on /amspods/shop/ and home).
City pages are /amspods/bagger-audio-<city>/ (West Carson, Torrance, Irvine, Rancho Cucamonga probed). Spanish hreflang en/es/x-default present on es pages.

## (a) Visual phone + desktop
- NICE: Home phone (probe1/amspods_phone.png): the 9:16 hero poster is followed by a large empty black band (~y 950-1230 of 1688 at 2x) before the Jessie banner; H1 "AMS Pods / Harley bagger audio in Carson" starts at the fold and is partly covered by the fixed Text us / Call bar; hero CTA buttons are not above the fold on phone. Next step: shorten the poster/black gradient block so H1 + Quote button sit above the fold. Desktop hero is fine (Call / Text us / Quote visible).
- NICE: Road Glide page phone screenshot shows a blank white box where a Hertz pod/speaker card image should be (probe1/amspods-services-road-glide-bagger-audio_phone.png). Unverified whether image is lazy-load timing in the lab; check the card image URL.
- No horizontal overflow on any probed page/viewport (overflow_x = 0). No broken images (0), 0 images missing alt on all probed pages.
- Chat widget "Talk to me" bubble and sticky bottom Call/Text bar overlay content on phone (by design); small tap targets reported 8-28 per phone page by probe (NICE: raise to 44px on dense nav/footer link lists).
- Desktop heros/forms render cleanly on home, shop, build-your-own.

## (b) Click-through
- All internal /amspods/* links return 200 (nav, footer, CTAs, 111 city links). Hub links /tesla/, /alarm/, /tint/, /stereo/, /services/* resolve 200 or 308 to the canonical hub path (e.g. /services/ams-pods/ -> /amspods/services/ams-pods/).
- YouTube, Google Maps, shop.amspods.com: 403 = proxy, unverifiable from here. Probe "err Timeout" link rows in probe.json were proxy congestion (I re-checked all with requests: 200/308).
- Six known links (montrose, burbank, san-marino, rowland-heights, encino, hollywood): they are root-relative footer links `href="/montrose/"` etc. in the hub-wide "Car Stereo, Tint & Alarm for <city>" list. They appear on ALL 172 mount pages that carry the hub footer (every /amspods/ page incl. home, shop, faq, about, specials, blog, es, 111 city pages; the 3 es-less 404 pages excepted). On the mount they return 200 (hub pages). `/amspods/bagger-audio-<those>/` do not exist (404; no pages link to those). Likely 404 on the amspods apex if root-level city paths do not exist there: UNVERIFIABLE. [mount-proxy]
  - MUST-FIX (conditional): on www.amspods.com, test /montrose/, /burbank/, /san-marino/, /rowland-heights/, /encino/, /hollywood/. If 404, either point those footer links to the hub's absolute URLs (https://www.audiomotorsports.com/<city>/) or create /amspods/bagger-audio-<city>/ pages for them (add, never remove).
  - Also hub footer lists /la-crescenta-montrose/, /north-hollywood/, /west-hollywood/ (200).
- Forms inspected, not submitted: build-your-own "Quote the pair": POST via JS ajax (action="", fetch to /api/quote in amspods-main.js); fields name*, phone*, email*, bike (select), year*, finish (select), notes_short, message; honeypot `_honey` (hidden, tabindex -1), `_captcha`=false hidden, `_subject` hidden, product hidden. Model pages (Road Glide / Street Glide / Road King / bagger-builds) have a quote form: name*, phone*, email*, service, year*, make*, model*, message, same honeypot. Chat widget posts to /api/chat. Success-state markup not visible without submit. NICE: action="" means no-JS submit posts to the page itself; add action="/api/quote".
- Redirects: apex 308 -> www only. Hub /services/bagger-audio/ 308 -> /amspods/.

## (c) Bugs / meta
- MUST-FIX: Leaked internal copy "Google shows 4.8 from 654 reviews — that is the schema aggregate only. We do not invent bagger counts or a "from <City>" quote." Visible body text on 38 city pages (23 indexable: bellflower, compton, gardena, harbor-city, hawthorne, hermosa-beach, lakewood, lawndale, lomita, long-beach, los-angeles, lynwood, manhattan-beach, palos-verdes-estates, paramount, rancho-palos-verdes, redondo-beach, rolling-hills-estates, san-pedro, signal-hill, south-gate, torrance, wilmington; 15 noindex ones also). Full list: leak_sa.txt. Evidence example: /amspods/bagger-audio-el-segundo/ ("...that is the schema aggregate only. We do not invent bagger counts..."). Next step: rewrite to customer copy, e.g. "Google shows 4.8 from 654 reviews." and "Ask for Nick for a quote on your bike."
- MUST-FIX: Other visible "We do not invent..." internal-voice lines: 44 pages with that exact phrase (41 city pages, plus /amspods/specials/ "We do not invent a second pod price or a struck 'was.'", /amspods/reviews/ "We do not invent Softail prices or a Sportster program", /amspods/payment-plan/, /amspods/catalog/kenwood/ variant "We do not invent Hertz model numbers"); including West Carson-adjacent copy 'we do not invent a "from West Carson" attribution' on /amspods/bagger-audio-west-carson/ and "Nothing gets invented beyond $649". Full list leak_inv.txt (exact phrase). Also variants ("do not invent", "We do not paste fake quotes on this page") on ~113 pages total. Next step: rephrase as positive customer-facing statements ("Pods are $649 a pair; everything else is quoted on your bike."). Spanish pages did not contain the English leak.
- MUST-FIX (flag; owner decision): 85 of 111 city pages (e.g. irvine, rancho-cucamonga, el-segundo, anaheim...) ship `<meta name="robots" content="noindex, follow">`; only 26 city pages (incl. West Carson, Torrance, Long Beach, San Pedro, Wilmington) are indexable. Per rules, do NOT noindex/remove pages; recommendation is to add unique local content so these can be indexed (drive times/routes from that city to 22025 S Avalon Blvd, nearby landmarks, city-specific FAQ), then flip robots to index. As-launched they cannot earn city traffic. Ask Zack whether the noindex is intentional.
- MUST-FIX: /amspods/payment-plan/ desktop CLS = 0.508 (> 0.25), reproduced in 2 runs (phone CLS 0). Next step: reserve space (width/height / min-height) for the late-loading block above/near the fold.
- NICE: Console on most pages: "Unrecognized feature: 'web-share'" and "Allow attribute will take precedence over 'allowfullscreen'" from the YouTube iframes (harmless, remove web-share from iframe allow=). ERR_TUNNEL_CONNECTION_FAILED = GTM/YouTube blocked by proxy (environment).
- Intermittent (UNVERIFIED, likely proxy): occasional "Refused to apply style/script ... MIME type text/plain" (e.g. /assets/js/network-chrome.js, hub-menu.css) and 502 on home, blog, es, specials; curl confirms these assets serve application/javascript / text/css 200. Each page loaded fine on retry (west-carson phone LCP 11.5s then 0.85s). Treat the LCP ~10.6s rows as environment artifacts.
- Meta: all 175 pages have title, description, canonical, viewport, one H1, favicon/apple-touch-icon 200, OG tags on probed pages, JSON-LD (LocalBusiness/AutoRepair, FAQPage, BreadcrumbList, Service, BlogPosting, etc.). No mixed content found (mixed = [] on all probes).
- Canonicals are self-referencing on https://www.audiomotorsports.com/amspods/... (mount host). Expected for the mount; on www.amspods.com the canonical/og:url/hreflang/schema URLs must be the amspods.com host: UNVERIFIABLE here. MUST-VERIFY at launch.
- NICE: titles > 65 chars: /amspods/es/about/ (68), /es/faq/ (67), /es/gallery/ (69), /services/bass-amps-subwoofers/ (67). Descriptions > 160 chars: es/ (162), es/about (174), es/faq (182), es/gallery (194), es/payment-plan (178).
- NICE: /amspods/shop/ meta description is short (~70 chars) and the page links products only to blocked shop.amspods.com; no on-mount product pages to test.

## (d) Lab speed (lab != field; Chromium via proxy, phone 390 emulated / desktop 1366)
| Page | Phone LCP ms | Phone CLS | Phone TBT-proxy ms | Desk LCP | Desk CLS | TTFB ms (ph/desk) | Transfer KB (ph/desk) |
|---|---|---|---|---|---|---|---|
| /amspods/ | 2724 | 0 | 90 | 3408 | 0 | 624/637 | 924/4089 (hero mp4 ~3.2MB) |
| /shop/ | 1568 | 0 | 16 | 1332 | 0 | 285/238 | 571/799 |
| /services/bagger-builds/ | 1368 | 0 | 21 | 1076 | 0 | 338/131 | 586/1136 |
| /services/road-glide-bagger-audio/ | 1076 | 0 | 19 | 1472 | 0 | 228/134 | 396/463 |
| /services/street-glide-.../ | 1424 | 0 | 29 | 1280 | 0 | 287/358 | 389/443 |
| /services/road-king-.../ | 1240 | 0 | 92 | 1296 | 0 | 206/233 | 398/514 |
| /build-your-own/ | 1336 | 0 | 66 | 1272 | 0 | 156/179 | 396/394 |
| /faq/ | 828 | 0 | 13 | 1244 | 0 | 145/333 | 185/185 |
| /about/ | 1448 | 0 | 31 | 1924 | 0 | 331/642 | 845/977 |
| /specials/ | 1280 | 0 | 17 | 10700* | 0 | 523/284 | 188/187 |
| /blog/ | 10944* | 0 | 0 | 10844* | 0 | 312/292 | 183/182 |
| /blog/bagger-audio-speakers-amp-or-pods-first/ | 856 | 0 | 4 | 1952 | 0 | 158/208 | 188/183 |
| /es/ | 1268 (rerun) | 0 | 19 | 1040 | 0 | 387/168 | 570/707 |
| /es/faq/ | 3536 | 0 | 0 | 3128 | 0 | 616/700 | 186/186 |
| /bagger-audio-west-carson/ | 852 (rerun) | 0 | 0 | 860 | 0 | 207/160 | 300/383 |
| /bagger-audio-torrance/ | 1228 | 0 | 0 | 924 | 0 | 160/120 | 273/330 |
| /bagger-audio-irvine/ | 1416 | 0 | 0 | 10800* | 0 | 607/146 | 297/334 |
| /bagger-audio-rancho-cucamonga/ | 1064 | 0 | 0 | 1068 | 0 | 190/134 | 325/357 |
| /catalog/hertz/ | 1096 | 0 | 29 | 1452 | 0.001 | 166/218 | 463/582 |
| /services/harley-radio/ | 11484* | 0 | 182 | 1840 | 0.001 | 635/321 | 770/770 |
| /contact/ | 1144 | 0 | 22 | 1204 | 0 | 200/281 | 445/562 |
| /reviews/ | 764 | 0 | 0 | 10704* | 0 | 120/321 | 185/169 |
| /bagger-audio-el-segundo/ | 1036 | 0 | 0 | 10608* | 0 | 191/123 | 285/312 |
| /payment-plan/ | 10628* | 0 | 7 | 928 | **0.508** | 139/184 | 851/916 |
*asterisk = coincides with a "Refused to apply style (MIME text/plain)"/502 proxy glitch on that load; not reproducible, environment. Only real LCP issue: none; home desktop 3.4s is below 4s (hero video poster, 4MB transfer: NICE to lazy-load the mp4).

## MUST-FIX summary (10 lines)
1. Leaked "that is the schema aggregate only" text on 38 city pages (23 indexable); rewrite to customer copy (leak_sa.txt).
2. Leaked "We do not invent ..." internal-voice lines on 44+ pages incl. specials, reviews, payment-plan, West Carson (leak_inv.txt).
3. 85/111 city pages are noindex,follow; confirm intent and add unique local content so they can be indexed (never remove pages).
4. /amspods/payment-plan/ desktop CLS 0.508 (>0.25), reproduced twice.
5. Hub-wide footer links /montrose/ /burbank/ /san-marino/ /rowland-heights/ /encino/ /hollywood/ (on every page) must resolve on www.amspods.com; unverifiable here, test at launch.
6. Verify on www.amspods.com that canonical, og:url, hreflang and JSON-LD URLs use the amspods.com host (mount shows audiomotorsports.com/amspods).
7. Verify robots.txt/sitemap.xml at www.amspods.com (apex 308s to www; unverifiable; mount has none).
8. shop.amspods.com product/category links (14 on /shop/) unverifiable here; click-test at launch (build-your-own/quote forms posted nowhere; inspect only).
9. Confirm /api/quote form submit and success state on the real domain with a test lead (not done here per rules).
10. No other blockers: no mixed content, no phone horizontal scroll, viewport present everywhere, LCP < 4s on stable loads.
