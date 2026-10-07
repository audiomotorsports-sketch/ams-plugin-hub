# LAUNCH NOTES: lacartint.com (Phase 2), 2026-10-04
All page findings are [mount-proxy]: www.lacartint.com is refused by the egress proxy (CONNECT 403, retested), so the hub-mounted copy https://www.audiomotorsports.com/tint/ was audited. The standalone may differ. Lab numbers (Playwright, proxy, headless) are not field data. Probe data: b1/ b2/ b3/ rr/ (probe.json + screenshots), banner/ (Sunday/Monday clock emulation), linkstatus.txt, retry.txt.

## Apex headers (verified on the real domain) - apex_headers.txt
- https://lacartint.com/ -> HTTP/2 308, location https://www.lacartint.com/, server Vercel, cache-control public,max-age=0,must-revalidate, refresh 0;url=..., HSTS max-age=63072000 (no includeSubDomains/preload).
- http://lacartint.com/ -> 308 to https://lacartint.com/ -> 308 to www (two hops before the final host). NICE: http goes through 2 hops; fine functionally.
- https://www.lacartint.com/ unverifiable from here (000 / CONNECT 403).

## Pages probed (phone 390x844 + desktop 1366x900), all HTTP 200 [mount-proxy]
/tint/, /tint/services/ceramic-film/, /tint/services/hand-cut/, /tint/tesla-tint/, /tint/specials/, /tint/faq/, /tint/locations/, /tint/shop/, /tint/blog/, /tint/blog/california-70-vlt-fronts/, /tint/es/, city: west-carson, irvine (OC), rancho-cucamonga (far-out), manhattan-beach (South Bay), /tint/contact/, /tint/book/ (inspected only, no submits). Standalone /tint/ceramic-film does not exist on the mount; ceramic-film lives at /tint/services/ceramic-film/.

## Phase 1 re-confirmation on /tint/ [mount-proxy]
1. Stray hero comment: raw source (line ~121) has `<!-- LA Car Tint quote plugin / INSERT after </section> of class="hero-banner" / BEFORE page-short (after you MOVE offer-cards) / Pair with /assets/css/ams-plugin-tint.css -->`. It is a well-formed HTML comment. Rendered innerText on phone and desktop does NOT contain "BEFORE page-short", "INSERT after", "ams-plugin-tint" or "-->". So it is NOT visible text in the browser; Phase 1's "visible leak" is NOT reproduced. It is still developer text shipped in public source (also a "TODO Zack" comment at line ~408). NICE-TO-HAVE: strip both comments from the template. Next step: remove the two comment blocks from the tint hub template. (Not MUST: nothing visible.)
2. 'Closed today' banner: present in static HTML as `<div id="sunday-banner" hidden>` (first body element, before the header). lacartint-main.js un-hides it only when Pacific day is Sunday. Verified with clock emulation: Sunday 11:00 PT -> shown (phone height 132px, desktop 67px, sticky header sits below it, no overlap, no horizontal scroll); Monday -> display:none. At fetch time (Sat evening PT) not shown, so it was not visible in my default screenshots. Phase 1's "first text node" claim is true of source order only; for Googlebot rendering on a Sunday it would be first text. NICE-TO-HAVE: add data-nosnippet to the banner and keep it hidden for crawlers. Phone note: on Sunday the banner takes ~16% of the first screen and pushes the hero down.

## (a) Visual phone + desktop
- NICE /tint/ phone: the hero is a portrait video/poster block that fills the first screen with a dark empty fade; the H1 and in-hero Text Nick / Book buttons sit below the fold (H1 starts at the bottom edge, partly covered by the sticky bottom Text Nick/Call bar and the chat bubble). Call/Text still reachable in the header and sticky bar, so not blocking. Next step: shorten the phone hero (e.g. 60-70vh) so the H1 and CTA show above the fold.
- NICE all pages phone: chat bubble ("Talk to me") and sticky bottom bar overlap lower-right content on first screen.
- NICE: small tap targets (<32px) counted on phone: /tint/ 24, es 23, irvine 32, manhattan-beach 21, west-carson 17, contact 18, others 8-17 (mostly footer/nav links). Next step: raise footer/nav link padding to 44px height.
- /tint/specials/ phone: YouTube/video embed area renders black (youtube blocked here: unverifiable). Layout otherwise clean, no overflow.
- Phone horizontal overflow: 0px on every page. Viewport meta present everywhere (width=device-width, initial-scale=1).

## (b) Click-through
- Checked 589 unique hub links found on these pages with curl: 334 200, 226 308 (hub redirects that resolve; /shop/..., /services/... legacy paths), 1 404, 28 timeouts on first pass; retry at low concurrency resolved 23 (200/308); 5 still timed out (shop/brand/hifonics, shop/dash-cameras/kicker-drone-xc-lte, shop/speakers/, tint/window-tint-inglewood (a direct curl returned 200), vehicles/ford) = proxy flakiness, treated as unverified not broken. Playwright "err APIRequest" entries in probe.json are my link-checker timeouts under load, not site errors.
- MUST-FIX [mount-proxy] https://www.audiomotorsports.com/aftercare/ returns 404 (confirmed twice). It is linked from the runtime-injected hub footer/nav on /tint/, /tint/specials/, /tint/faq/, /tint/blog/*, /tint/book/, /tint/contact/, /tint/tesla-tint/. The page exists at /tint/aftercare/ (200). Next step: point the injected link to /tint/aftercare/ (or add a hub-root /aftercare/ page). Standalone link unverified.
- Hub-wide links on /tint/ and /tint/es/ to https://shop.lacartint.com/... (18) and lacarbeats / lacaralarm / youtube / maps / facebook / offerup / share.google / yelp.to return 403 here = environment (blocked), unverifiable.
- Forms (inspected, never submitted):
  - /tint/contact/: POST /api/quote/; required phone, year, make, model, old_tint (select), service (select), name, email; optional message; honeypot text field `company`; hidden _captcha, source_page, _subject. Success markup not visible without a submit.
  - /tint/book/: POST /api/quote/; required service, year, make, model, day (date), slot (radio 10:00/12:00), name, phone; honeypot `company`; hidden source_page, message. Note: second slot radio is not flagged required (group is, fine).
  - A GET textarea with no name/action on every page is the Jessie chat widget (not a form to submit).
  - No forms on the other sampled pages; CTAs there are sms:/tel:/links to /tint/book/ and /tint/contact/.
- Redirect: tint legacy hub paths (/tesla-tint/, /tint-estimator/, /services/tesla-window-tint/) 308 to targets; fine.

## (c) Bugs
- MUST-FIX [mount-proxy] /tint/tesla-tint/: the price simulator assets all 404 (verified by curl): /tint/tesla-tint/assets/sim/sim.css?v=ttl-r9, app.js?v=ttl-r9, prices.js?v=ttl-r9, img/model-yl.png, img/model-yl.webp. Console: "Refused to apply style ... sim.css" + two 404s; broken image model-yl.png; the sim is non-functional. Desktop run also showed 59px horizontal overflow and LCP 10.7s (phone: 0 overflow, LCP 1.9s). Next step: publish the sim asset folder under the mount path (or fix the paths in the tesla-tint template), then re-test overflow and LCP. (Overflow/LCP seen on desktop only; a re-run would confirm the overflow cause is the unstyled sim.)
- Intermittent (not reproduced on direct curl): on several loads, static assets from the mount returned 502 or text/plain and were refused by Chrome: lacartint-main.js (west-carson phone), style.css + ams-chat.css (irvine phone, LCP 10.5s that run), page-short.css (contact phone, west-carson rerun), 502 on /tint/locations/. On re-run irvine phone LCP 0.98s. All of these assets return 200 with correct types via curl. Likely proxy/edge flakiness under concurrent load, so classed NICE-TO-HAVE/monitor, but if real users hit it the page loses all styling. Next step: check hub edge logs for 502s on /sites/lacartint/assets/* and /assets/js/lacartint-main.js.
- NICE: console warnings on most pages: "Unrecognized feature: 'web-share'" and "Allow attribute will take precedence over 'allowfullscreen'" (YouTube iframe allow attribute). Remove web-share from allow and drop allowfullscreen duplicate.
- NICE: hero image preload unused warnings (/tint/es/ tint-hero-mobile/desktop.jpg, /tint/contact/ ams-lot-night.jpg, /tint/shop/ banner): preloaded but unused within a few seconds. Fix: preload only the image actually used per viewport (the hero is video on /tint/).
- NICE: /tint/services/hand-cut/ phone: 4 YouTube thumbnails (i.ytimg.com) not loaded = blocked here, unverifiable.
- ERR_TUNNEL_CONNECTION_FAILED for googletagmanager.com on every page and youtube.com on pages with embeds = environment, unverifiable.
- No page errors (JS exceptions) and no mixed content on any page. No noindex/robots meta on any page. Canonicals are self-referencing hub URLs (https://www.audiomotorsports.com/tint/...). That is expected for the mount; confirm the standalone canonicals are https://www.lacartint.com/... (unverifiable).
- Meta/OG: title, og:image, canonical, viewport present on all; favicon + apple-touch-icon links present (2 icons) and /favicon status 200 on all pages. Images without alt: 0 on the probed pages.
- Phase 1 items re-seen: "no visible updated date" and FAQPage-without-visible-FAQ flags on blog/ceramic pages remain per pages.csv; not re-tested here.

## (d) Lab speed (LCP ms / CLS / long-task TBT proxy ms / TTFB ms / transfer KB) phone | desktop. Lab != field.
- /tint/: 1572/0/40/445/2223 | 1336/0/127/285/2811
- ceramic-film: 1676/0/54/250/529 | 1844/0/212/569/2020
- hand-cut: 2088/0/242/633/340 | 1172/0/83/244/938
- tesla-tint: 1900/0/0/507/410 | 10716(!)/0/49/132/1632 (and 59px overflow desktop)
- specials: 1008/0/32/152/256 | 928/0/18/165/984
- faq: 1120/0/0/354/255 | 1208/0/34/146/905
- locations: 1468/0/40/349/189 | 1092/0/35/208/268
- shop: 1564/0/41/331/3221 | 1544/0/180/353/3064
- blog: 1304/0/48/391/236 | 1292/0/73/293/930
- blog post: 1000/0/31/321/187 | 1076/0/38/200/187
- /tint/es/: 1536/0/60/236/5263 | 1668/0.002/224/339/5499 (heaviest, 5.3-5.5 MB)
- west-carson: 1940/0/12/345/3685 (rerun; first 1180) | 872/0/20/158/894
- irvine: 984/0/9/234/3687 (rerun; first run 10524 with CSS refused) | 1436/0/65/355/895
- rancho-cucamonga: 860/0/7/131/3687 | 1132/0/55/176/894
- manhattan-beach: 1120/0/2/157/3687 | 1304/0/23/365/895
- contact: 1144/0/112/211/775 | 1240/0/109/300/894
- book: 1396/0/25/299/186 | 976/0/15/247/186
- NICE: /tint/es/ transfers ~5.3 MB and city/shop phone pages ~3.7 MB (hero imagery/video). Compress/serve smaller phone variants. No page has CLS above 0.002.

## MUST-FIX summary (10 lines)
1. [mount-proxy] /aftercare/ (hub-root) 404 linked from injected footer/nav on many /tint/ pages; target /tint/aftercare/ is 200.
2. [mount-proxy] /tint/tesla-tint/ simulator assets (sim.css, app.js, prices.js, model-yl.png/webp) all 404: sim broken, console errors, broken image.
3. [mount-proxy] /tint/tesla-tint/ desktop: 59px horizontal overflow and LCP 10.7s (probably from 2); re-test after fixing 2.
4. [mount-proxy] Watch item (not reproduced via curl): intermittent 502/text-plain on mount CSS/JS made pages unstyled in several headless loads; check edge logs before launch.
5. Phase 1 "visible stray hero comment text" NOT reproduced: it is a valid HTML comment, not visible (NICE: remove from source).
6. Phase 1 'Closed today' banner confirmed: hidden unless Pacific Sunday; shows correctly with no overlap when emulated; NICE: data-nosnippet.
7. Apex lacartint.com: 308 to www (http: 2 hops), HSTS 2y; www unverifiable (proxy block).
8. No noindex, no missing viewport, no mixed content, no JS page errors, no phone horizontal scroll, no CLS issue on any sampled page.
9. Forms on /tint/contact/ and /tint/book/ inspected only: POST /api/quote/, honeypot present, required fields sensible.
10. Unverifiable here: www.lacartint.com, shop.lacartint.com, GTM, YouTube embeds/thumbs, maps, sister domains.
