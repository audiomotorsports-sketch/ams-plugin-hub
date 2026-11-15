# teslatintla.com Phase 2 launch audit (2026-10-04)
Tools: probe.py (batches b1, b2: 15 URLs, phone 390x844 + desktop 1366x900), plus custom read-only Playwright scripts (calculator, chat, sticky bars, throttled perf), curl for assets/links. No form submitted, no POST sent. Screenshots in b1/, b2/, and sim_*.png, chat_open_phone.png, home_sim_midscroll_phone.png.
Limits: shop.teslatintla.com, maps.google.com, share.google, youtube, instagram, lacarbeats/lacartint/lacaralarm/amspods, GTM and the financing links (syf, snapfinance, easypay, koalafi) are 403/tunnel-blocked here: UNVERIFIABLE. www.teslatintla.com not tested (blocked). The connection to the apex flakes (ECONNRESET/000/502 on static files, ~1 in 6-8 requests); every asset that 502'd in the browser returned 200 on 5 of 6 curl retries, so those are environment flakes, not site bugs. Lab numbers are noisy for the same reason (see d).

## (a) Visual phone + desktop
- Home phone: header/Call/Menu OK. The first full screen (844px) is only the 780px-wide hero photo; the real H1, "Book a Slot" and "Text Nick" sit below the fold. The mobile hero image has marketing text baked in ("AUDIO MOTORSPORTS / INSTALLED IN CARSON") which duplicates the live H1 and is not readable text. NICE.
- Home desktop: hero, nav (Services, Locations, Shop, Payment Plan), Text Nick/Call fine. No overlap.
- Calculator (home, read-only): renders (2 film cards, 4 coverage rows, 6 model chips). Works: Y L full car $399 -> Model 3 $369 -> then 3M Ceramic IR + Full car $569; windshield rows reprice ($189 -> $299). No page errors, preview warning hidden, canvas 1434x684 drawn. Calculator passes.
- Phone sticky UI around the calculator is broken (see MUST 3).
- Carson phone: hero OK; chat launcher covers the "Text Nick" button (MUST 4).
- Book phone: chat launcher sits over the Model / Year / Day inputs; footer columns overlap ("This desk" column collides with "MotorSports" and "Book a Slot").
- Locations / payment-plan / about / contact / blog / gallery: no layout defects seen except caused by CSS 502 flakes (screenshots with unstyled header are flake artifacts; locations_phone.png).
- Blog post Model Y: desktop horizontal overflow 30px (overflow_x=30). NICE (verify).
- Gallery: YouTube thumbnails (i.ytimg.com) blocked here: unverifiable.
- 404 page: see MUST 5.

## (b) Click-through
- 85 unique same-site links collected from all 15 pages, rechecked sequentially with curl and retries: 84 x 200, 1 x 404 (the intentional 404 test URL). Includes /all-services/, /gallery/, /privacy/, /terms/, /tesla-tint-south-los-angeles/, west-carson, watts, vernon, all blog posts. Sitemap lists 143 URLs, robots.txt allows all bots (Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot).
- Unverifiable external: shop.teslatintla.com (linked sitewide, 403 via proxy), maps, share.google, YouTube, Instagram, LA Car Beats/Tint/Alarm, AMS Pods, 4 financing apps on /payment-plan/.
- tel:/sms:/mailto: links well-formed: tel:+13105138800, sms:+12134291092 (prefilled bodies), mailto quote links.
- Redirects: /foo/bar/baz -> 308 -> /foo/bar/baz/ -> 404 (ok). No apex redirect loops.
- Forms: /book/ only real form: POST /api/quote/, required service(select), year, make, model, day(date, Mon-Sat), slot(radio 10:00/12:00), name, mobile; hidden source_page, message, appointment; honeypot input "company"; no captcha; email-based, "No deposit". /contact/, /payment-plan/, home, city pages: no form (only the chat textarea). Not submitted.
- /es/: single page, hreflang en/es/x-default present, but /es/ is NOT in sitemap.xml and every nav/CTA/footer link on /es/ points to the English pages (/book/, /locations/, /blog/...).

## (c) Bugs
MUST-FIX
1. /tesla-tint-carson/ (the shop's own city page): title, H1, breadcrumb, meta/OG description, BreadcrumbList and FAQ all say "Avalon" ("Tesla Window Tint Avalon | Tesla Tint LA", "Tesla Window Tint for Avalon", "Home / Locations / Avalon", "How much is Tesla window tint if I drive from Avalon?", 61 mentions vs 14 of Carson), while the hero image, canonical, sitemap and schema locality say Carson. Looks like the city token resolved to the street name. Evidence: curl of the page; carson_phone.png. Fix: render city name "Carson" in title/H1/breadcrumb/descriptions/FAQ; keep "Avalon Blvd" only in the address.
2. /es/ calculator preview broken: JS uses relative paths (assets/sim/img/...), so on /es/ they resolve to /es/assets/... Evidence: 404 /es/assets/sim/img/model-yl.png, console "tint mask failed to load: assets/sim/img/masks/model-yl-rear.png", broken_images in probe. Fix: absolute paths (/assets/sim/...) in sim app.js/markup for /es/.
3. Home phone, calculator section: the price bar and sticky CTAs break. After scrolling into the calculator the page layout width grows (scrollWidth 414-476 on a 390 screen), the fixed price bar is wider than the screen (NEXT button clipped), "Book a Slot / Text Nick / Payment Plan" buttons stack and overlap the price text, a second sticky bar (Text Nick / Call, .ams-plug-sticky) overlaps the first, and the chat bubble is cut off at the right edge. Evidence: home_sim_midscroll_phone.png, sim_after_phone.png, DOM: .sim-pricebar width 414-476; overflowing children: blog .card-link-card (right edge 475), #nextBtn (454), hidden .ams-chat-panel (right 464). Fix: contain the blog card row (overflow hidden / grid min-width:0), keep the hidden chat panel inside the viewport (visibility:hidden + max-width:calc(100vw - 32px)), merge or hide .ams-plug-sticky while .sim-pricebar shows, stack the pricebar actions with flex-wrap.
4. Chat widget on phone (ams-chat.js, ?v=ttl-r8): launcher (74px, fixed bottom-right, z-index 50) covers CTAs: "Text Nick" button on /tesla-tint-carson/ (25% overlap at top, still 5-23% down the page), Model/Year/Day inputs on /book/ (up to 61% of a field), the (310) 513-8800 footer link on Torrance. When opened the panel is 358px wide at x=106, so the right 90px is off-screen: header close button, right side of messages and the Send button are not visible on a 390px phone (chat_open_phone.png). Escape closes it; no touch-reachable close seen. Chat does not call the API until a message is sent (no POST on open; I did not send one). Fix: on max-width 480px make the panel left:8px right:8px bottom above the sticky bars, width auto; raise launcher above the sticky CTA bar and the form fields (e.g. bottom: 88px) or collapse the bubble on scroll.
5. 404 page on any nested path (e.g. /foo/bar/baz/, any broken deep URL): asset links are relative (assets/css/style.css, assets/img/logo/...), so they resolve under the bad path and 404; the page renders as unstyled Times-font text with a broken logo. Evidence: this-page-does-not-exist-xyz_phone.png, logo URL /this-page-does-not-exist-xyz/assets/img/logo/ams-coin-gold.png (404), /foo/bar/baz/assets/css/style.css (404). Fix: make every asset URL root-relative (/assets/...) in the 404 template; also add a link to Locations and Book there. Status code 404 + noindex,follow are correct.
6. Phone/mobile page CSS/JS stalls: none caused by the site proven (see limits). Not a finding.

NICE-TO-HAVE
7. /es/ hero image and baked text are English ("TESLA WINDOW TINT / HAND-CUT MICRO EDGE / INSTALLED IN CARSON"); /es/ links go to English pages; /es/ missing from sitemap (add it to improve discoverability; never remove).
8. Missing on 404: canonical none, fine. Home hero img src is the 2560x1440 desktop JPG (501 KB, no srcset/sizes between 768px and 2560px; LCP is that image on desktop). Phone gets tesla-hero-mobile.jpg (249 KB) via <source media>. Add webp/avif and 1280/1920 srcset; fetchpriority="high" already set, and a <link rel=preload as=image> is not present.
9. Tap targets: probe flags 22-57 small targets per page (<44px). Review footer/nav links on phone.
10. Mixed content: none. Viewport meta, canonical, title, description, OG on all pages OK. favicon + apple-touch-icon 200. All images have alt. robots meta absent except 404 (noindex,follow). Console errors in browser are only blocked-host/proxy flakes (GTM, YouTube, 502s) and the "Unrecognized feature: 'web-share'" iframe allow warning (YouTube embeds on /about/, /locations/, /payment-plan/) - NICE: drop web-share from the allow attribute.
11. Stray text: "Zack runs the floor." appears in intros on /locations/ and city pages; fine if intended.
12. Malibu/Irvine pages: no "Avalon" bug in titles (title "Tesla Window Tint Malibu"); Torrance fine. Only Carson is affected (and check /tesla-tint-west-carson/, not rendered here).

## (d) Speed / CWV lab (unthrottled, through the session proxy; lab != field)
| URL (phone / desktop) | LCP ms | CLS | long-task ms (TBT proxy) | TTFB ms | KB | req |
|---|---|---|---|---|---|---|
| / | 1436 / 1792 | 0 / 0 | 132 / 270 | 413 / 478 | 510 / 756 | 24 |
| /tesla-tint-carson/ | 980 / 5632* | 0 | 0 / 12 | 210 / 304 | 235 | 17 |
| /tesla-tint-torrance/ | 2720 / 1468 | 0 | 39 / 15 | 647 / 453 | 307 / 325 | 18 |
| /tesla-tint-irvine/ | 10576* / 5800* | 0 | 0 / 27 | 178 / 232 | 227 / 183 | 17 |
| /tesla-tint-malibu/ | 10556* / 11016* | 0 | 0 | 232 / 456 | 214 / 325 | 17 |
| /locations/ | 1972 / 5948* | 0 | 122 / 34 | 277 / 387 | 160 / 233 | 17-26 |
| /book/ | 1768 / 1056 | 0 | 2 / 0 | 438 / 312 | 152 / 148 | 14 |
| /payment-plan/ | 1384 / 1620 | 0 | 19 / 111 | 480 / 263 | 430 / 619 | 18 |
| /about/ | 10820* / 1420 | 0 | 15 / 20 | 486 / 406 | 458 / 580 | 19 |
| /contact/ | 1392 / 5864* | 0 | 1 / 62 | 359 / 181 | 429 / 642 | 19 |
| /blog/ | 1580 / 2232 | 0 | 0 / 12 | 506 / 385 | 153 / 149 | 14 |
| /blog/tesla-model-y-window-tint/ | 1304 / 6216* | 0 | 13 / 21 | 342 / 499 | 310 / 575 | 21 |
| /es/ | 1536 / 10668* | 0 | 32 / 0 | 426 / 167 | 519 / 764 | 25 |
| /gallery/ | 1020 / 10740* | 0 | 0 / 31 | 413 / 154 | 199 / 603 | 20 |
* values of 5.5-11 s occur at random on every page type, cluster at ~10.6 s (a stalled proxy request, same pages gave 1-2 s on other runs); treat as unreliable/environmental, not proven LCP failures. CLS is 0 everywhere; no CLS>0.25. Re-test home from Slow-4G + 4x CPU: LCP 10-22 s with the proxy stalling (unreliable); Malibu 3.5-4.1 s, Torrance 6.3-8.2 s, Carson 6.5-9.1 s: indicative only, run PageSpeed/CrUX for real numbers.
Findings that are solid regardless of noise:
- Render-blocking: home loads 10 stylesheets in <head> (renderBlockingStatus=blocking): fonts, style, homepage-hero, offer-cards, ams-chat, sim, shop-white-banners, network-chrome, ams-plugin-tesla, paylater-note. They are tiny (about 20 KB brotli total; fonts.css, homepage-hero.css, shop-white-banners.css, paylater-note.css are served uncompressed, <1.5 KB), so the cost is 10 requests/round trips, not bytes (on Slow 4G each adds a round trip before first paint). NICE: concatenate into one critical CSS file or inline above-the-fold CSS and load ams-chat.css/sim.css/paylater-note.css non-blocking. City pages use 7 CSS, blog 5-7, es 10.
- Hero: desktop hero 501 KB JPG (assets/img/hero/tesla-hero-desktop.jpg, 2560x1440, cache immutable 1 yr); mobile hero 249 KB. Home total 510 KB phone / 756 KB desktop. The hero is LCP on home. NICE: convert to AVIF/WebP, ~1600px wide, srcset.
- Caching: assets immutable 1 year; HTML max-age=0 must-revalidate (Vercel, fine). Brotli on CSS/JS.
- GTM (GTM-5G9HJLQ) is loaded in <head> async; blocked here, so its cost is unmeasured.
- Throttled home lab TBT-proxy is low (132-270 ms) and sim JS has no page errors.

## Top 10 MUST-FIX summary
1. /tesla-tint-carson/ says "Avalon" in title, H1, breadcrumb, meta, schema breadcrumb and FAQ instead of Carson.
2. /es/ calculator preview images/masks 404 (relative asset paths under /es/).
3. Home phone: sticky price bar wider than the screen, NEXT clipped, CTAs stacked on top of the price.
4. Home phone: two sticky bars (.sim-pricebar and .ams-plug-sticky) overlap each other and the content.
5. Home phone: page scrolls/grows wider than 390px after the calculator loads (blog card row and hidden chat panel overflow).
6. Chat panel on phone is clipped off the right edge (close button and Send cut off).
7. Chat launcher covers "Text Nick" (Carson/city pages) and the Model/Year/Day fields on /book/.
8. 404 page on nested URLs loads no CSS/logo (relative asset paths): unstyled page.
9. Shop link (shop.teslatintla.com) is sitewide in nav but unverifiable here; confirm manually it resolves before launch.
10. Confirm 10-request render-blocking CSS and 501 KB desktop hero on real PageSpeed/CrUX (not a block by lab numbers; NICE).
