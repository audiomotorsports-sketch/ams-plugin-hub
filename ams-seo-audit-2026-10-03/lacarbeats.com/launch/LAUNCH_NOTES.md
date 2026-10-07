# LAUNCH NOTES: lacarbeats.com (Phase 2), run 2026-10-04
Read-only. No forms submitted. Every page finding is **[mount-proxy]**: it describes https://www.audiomotorsports.com/beats/ (hub-mounted copy), not www.lacarbeats.com, which the proxy blocks (403 CONNECT). Raw data: `r1..r11/probe.json` (parallel run), `serial/probe.json` (clean serial re-run, 8 URLs), `internal_link_status.txt` (633 links), `ext_links.json`, `apex_headers.txt`. Screenshots are in those folders.

## Method caveat
The first pass ran 11 probes in parallel. That inflated TTFB/LCP/CLS and caused self-inflicted timeouts when link-checking the hub host. So perf numbers below come from the serial re-run, and link statuses from a separate curl pass (3 retries each). The proxy also drops about 5% of connections to the hub host (curl reset/timeout seen on identical URLs). Because of that, "Refused to apply style ... MIME text/plain" console errors that hit a random different asset on each load are treated as proxy error bodies, not site bugs. The same files returned `text/css` / `application/javascript` on 15 of 15 clean curls.

## Apex redirect chain (live, standalone-verified)
- `http://lacarbeats.com/` -> 308 `Location: https://lacarbeats.com/` (server Vercel, `refresh: 0;url=` header).
- `https://lacarbeats.com/` -> HTTP/2 308 -> `https://www.lacarbeats.com/`. HSTS `max-age=63072000`, no includeSubDomains/preload. 2 hops to reach www, one permanent redirect each (good).
- `http://www.lacarbeats.com/` and `https://www.lacarbeats.com/`, `https://shop.lacarbeats.com/`: 403 from the egress proxy. Unverifiable from here: final status, headers, content, robots/sitemap, www TLS.

## Pages covered (all 200 on the mount)
/beats/, /beats/es/, /beats/services/, services/subwoofer-install/, services/window-tint/, services/remote-start/, /beats/shop/, shop/subwoofers/, shop/brand/kicker/, /beats/blog/, blog/amp-and-sub-done-right/, /beats/faq/, /beats/contact/, /beats/book/, /beats/reviews/, /beats/locations/, /beats/es/faq/, /beats/es/contact/, city pages: west-carson, irvine (OC), santa-ana (OC), rancho-cucamonga (far-out; Inland Empire). 22 URLs, phone 390x844 and desktop 1366x900.
**No product pages exist on the mount.** The shop on the mount is categories/brands only. Product links go to `shop.lacarbeats.com/shop/<cat>/<product>/` (14 distinct product URLs, e.g. kicker-44kxa2400-1, audiocontrol-spc-w12). Those are unverifiable here; shop/subwoofers/ and shop/brand/kicker/ stand in for the two product pages.

## (a) Visual, phone + desktop
- No horizontal scroll on any page (overflow_x = 0 on all 44 loads). Viewport meta `width=device-width, initial-scale=1` everywhere.
- Home phone and desktop: header, trust strip, Book a Slot / Text Nick / Call, hero all fine. City, blog, contact layouts fine.
- NICE: the hero H1 on `/beats/` and `/beats/es/` renders at 1px wide (visually hidden); the visible hero is an image with baked-in text ("Chat with Jessie"). Next step: make the H1 visible, or confirm the hidden pattern is deliberate and the image alt carries the same message.
- NICE: on phone, the fixed "Talk to me" chat bubble (74px) plus the sticky Text Nick/Call bar (48px) cover the lower right of heroes. On subwoofer-install the bubble sits over the word "SUBWOOFERS" in the hero headline. Next step: raise the hero title above the bubble zone on phone, or offset the chat widget on pages with a hero title.
- NICE (verify): `/beats/shop/` phone showed the white header with white text for "Audio MotorSports" and "Shop" (unreadable), in the same run where `shop-tickets-ams.css` was refused as text/plain. May be the transient stylesheet failure. Next step: recheck `/beats/shop/` on a clean connection; if reproducible, fix header colour on the light shop theme (then MUST-FIX).
- NOTE: header brand reads "Audio MotorSports" with Tesla/Alarm links on the mount, and the shop/nav look like hub chrome. Whether the standalone site shows the same is unverifiable.
- Phone tiny tap targets (<32px) counted by the harness: 4-26 on most pages, 58 on /beats/es/, 327 on /beats/shop/ (the mega menu/category chips). NICE: give footer/city-chip links 44px hit areas on phone.

## (b) Click-through
- Internal links: 633 unique audiomotorsports.com hrefs found across the 22 pages; **633 returned 200** (after retries); 0 404s. Some hub-root links 301/redirect to other brand sections, which is intended hub routing: /services/apple-carplay-android-auto/ -> /stereo/install/carplay/, /services/car-alarms/ -> /alarm/services/car-alarms/, /services/bagger-audio/ -> /amspods/.
- 458 of those 633 are hub-root paths (e.g. `/about/`, `/anaheim/`, `/blog/`, `/es/`, `/checkout/`), not `/beats/...`. They sit in the mount body (hub mega-menu/footer). On the mount these leave the LA Car Beats section and land on audiomotorsports.com pages. On the standalone they would resolve differently (root-relative). **Unverifiable** whether lacarbeats.com ships these; check the real www.lacarbeats.com nav/footer.
- Links to the standalone/other brand domains, unverifiable (403 by proxy): `shop.lacarbeats.com` nav (/shop/amplifiers/, /car-stereos/, /enclosures/, /speakers/, /subwoofers/) and 14 product URLs plus the root; `www.lacartint.com` (8 pages), `www.lacaralarm.com` (7 pages) and its /shop/, `www.amspods.com` (3 pages). Also `https://shop.audiomotorsports.com/` timed out in curl under load; recheck.
- Off-site, unverifiable (proxy 403, environment): youtube.com (31 watch/channel links), maps.google.com, google.com/maps, share.google, instagram.com/audiomotorsports, yelp.to/Lm2GAc4OiS.
- Forms (inspected only):
  - /beats/contact/ and /beats/es/contact/: POST `/api/quote/` (resolves to the hub on the mount). Required: phone, year, make, model, old_tint, service, name, email. Optional message. Hidden `_captcha`, `_subject`, `source_page`. Honeypot field `company`. Labels present for all.
  - /beats/book/: POST `/api/quote/`. Required: service, year, make, model, day (date), slot (radio), name, phone. Honeypot `company`. Hidden `message`, `source_page`.
  - Service pages (subwoofer-install, window-tint, remote-start): POST, **action attribute empty** (posts to the page URL itself). Honeypot `_honey`, hidden `_captcha`, `_subject`. subwoofer-install has no `source_page` field and `service` is not required, unlike window-tint/remote-start. NICE: on /beats/services/*, set an explicit action and add `source_page` so leads attribute to the page; confirm what endpoint handles the POST (not tested, rules forbid submitting). Unverifiable whether the standalone posts to the same endpoint.
  - Every page also has a GET textarea chat form (Jessie widget), no action; fine.
  - Success state markup was not visible without submitting.
- hreflang/Spanish: /beats/es/ pages have lang="es" and self canonicals (full alternate check not in this scope).

## (c) Bugs
- **Phase 1 stray hero text re-confirmed: NOT visible on /beats/ or /beats/es/.** The raw HTML contains a developer comment right after the hero section: `<!-- LA Car Beats quote plugin — guinea pig / INSERT after </section> of class="hero-banner" / BEFORE <section class="offer-cards" id="offers"> / Pair with /assets/css/ams-plugin-beats.css -->` (line ~119-125 of /beats/, ~116-122 of /beats/es/). It is a well-formed comment. A rendered-DOM text-node walk (phone and desktop, both pages) found no text node containing "hero-banner", "Pair with" or "guinea pig", and the comment is a Comment node. So the Phase 1 "visible code leak" came from a tag-stripping text extractor, not from what a browser prints. Classification: NICE-TO-HAVE. Next step: delete the internal comment (it has the words "guinea pig" and a CSS path), since any scraper or AI crawler that strips tags will surface `of class="hero-banner" BEFORE Pair with ...` as page text. Re-check the standalone copy, which is unverifiable here.
- Console/page errors: pageerrors = 0 on all loads. Real, reproducible console messages: (1) `Unrecognized feature: 'web-share'` and `Allow attribute will take precedence over 'allowfullscreen'` on YouTube iframes (blog post, contact, subwoofer-install, shop). NICE: drop `web-share` from the iframe `allow` list. (2) a `<link rel=preload>` for `lacarbeats-shop-mobile-1080x1920.jpg` on /beats/shop/ not used within a few seconds. NICE: align the preload with the actual phone hero image or drop the preload.
- Console errors from GTM (`googletagmanager.com/gtm.js?id=GTM-5G9HJLQ`) and YouTube/ytimg: ERR_TUNNEL_CONNECTION_FAILED. Environment (proxy), not site. The two broken images on subwoofer-install (phone) are `i.ytimg.com/vi/...` thumbnails, also proxy-blocked; unverifiable.
- `_vercel/insights/script.js`, a few CSS/JS: one-off MIME/aborts under load, not reproducible with curl (see caveat).
- Mixed content: 0 http:// requests on all loads.
- Meta: all 22 pages have title, description, a self-referencing canonical (to audiomotorsports.com/beats/..., so the **canonicals say nothing about the standalone**), og:image, JSON-LD (2-5 blocks; /beats/book/ has 0), no robots meta (indexable), html lang correct. NICE: short descriptions (blog 73 chars, 88 on the blog post, shop 103, subwoofers 103) and /beats/book/ has no JSON-LD. Several H1s are not keyword-led (/beats/shop/ "car stereo and speakers at LA Car Beats" in lowercase, /beats/locations/ "One Avalon shop. 109 drive-ins."); NICE: tighten.
- Favicon/apple-touch-icon: 2 icon links on every page, favicon returns 200 (two probe timeouts under load, retry succeeded elsewhere).
- NICE: /beats/book/ is the only page where the form is a different pattern (no JSON-LD); no problem otherwise.

## (d) Speed (lab, serial re-run, simulated desktop network via the sandbox proxy; lab != field)
| URL | view | LCP ms | CLS | TBT-proxy ms | TTFB ms | KB | req |
|---|---|---|---|---|---|---|---|
| /beats/ | phone | 1168 | 0 | 36 | 317 | 889 | 32 |
| /beats/ | desktop | 1244 | 0.014 | 75 | 321 | 2189 | 35 |
| /beats/es/ | phone | **10736** | 0 | 15 | 298 | 513 | 27 |
| /beats/es/ | desktop | 948 | 0.014 | 57 | 133 | 2235 | 31 |
| subwoofer-install | phone | 892 | 0 | 21 | 155 | 312 | 32 |
| subwoofer-install | desktop | 1096 | 0 | 82 | 128 | 922 | 30 |
| /beats/shop/ | phone | 1344 | 0 | 34 | 268 | 676 | 39 |
| /beats/shop/ | desktop | 1008 | 0 | 60 | 137 | 391 | 35 |
| west-carson | phone | 1008 | 0 | 0 | 271 | 304 | 25 |
| west-carson | desktop | 912 | 0 | 44 | 130 | 387 | 25 |
| blog post | phone | 788 | 0.002 | 14 | 143 | 190 | 26 |
| blog post | desktop | 1016 | 0 | 14 | 285 | 190 | 26 |
| /beats/contact/ | phone | 688 | 0 | 0 | 148 | 450 | 27 |
| /beats/contact/ | desktop | **10596** | 0 | 53 | 146 | 563 | 25 |
| santa-ana | phone | 1168 | 0 | 0 | 356 | 307 | 25 |
| santa-ana | desktop | 932 | 0 | 41 | 124 | 337 | 25 |
Two outliers (es phone 10.7s, contact desktop 10.6s) had FCP equal to LCP and coincided with a stylesheet that failed in that load (proxy artifact); the same pages were 1.2-4.5s elsewhere in the parallel pass. They need a clean re-test before being called real. The parallel pass (not trusted) showed phone CLS 0.36-0.40 on several pages (shop, kicker, west-carson, santa-ana, subwoofer-install, remote-start); the serial pass showed CLS 0 on the same pages, so that was load-induced. Other pages (services index, window-tint, remote-start, blog index, faq, reviews, locations, book, irvine, rancho, es/faq, es/contact) were measured only in the parallel pass: treat as unverified for perf. /beats/ desktop transfers 2.2 MB (hero videos/images); NICE: keep the poster-first loading.

## Classification
MUST-FIX candidates: none confirmed on the mount. Two items are conditional MUST-FIX if they reproduce on a clean connection: `/beats/shop/` phone header unreadable (white on white), and es phone / contact desktop LCP ~10.6s.

## Summary: 10 lines
1. No confirmed launch blockers on the mount: 22 URLs 200, no horizontal scroll, viewport OK, no mixed content, 0 page errors, 633/633 internal links 200 [mount-proxy].
2. Phase 1 "stray hero text" is NOT visible in a browser on /beats/ or /beats/es/; it is a valid dev comment ("guinea pig... Pair with ..."). NICE: delete it so tag-stripping scrapers do not print it.
3. CONDITIONAL MUST-FIX: /beats/shop/ phone header text white on white; recheck on clean connection.
4. CONDITIONAL MUST-FIX: LCP ~10.6s on /beats/es/ (phone) and /beats/contact/ (desktop) in one serial run, likely a failed stylesheet; re-test.
5. www.lacarbeats.com and shop.lacarbeats.com unverifiable (403); the apex does 308 http->https->www (2 hops, HSTS 2y).
6. 14 product links and the shop nav point to shop.lacarbeats.com; no product pages exist on the mount; unverifiable.
7. 458 of 633 links are hub-root paths (/about/, /anaheim/, ...); check the standalone nav/footer resolves them correctly.
8. Service-page forms post with an empty action and no source_page on subwoofer-install; verify the endpoint and attribution. Contact/book post to /api/quote/ with honeypot+captcha fields.
9. NICE: H1 on home is visually hidden (1px), chat bubble overlaps hero title on phone, `web-share` iframe warning, unused shop preload, short meta descriptions on blog/shop.
10. All city pages tested (West Carson, Irvine, Santa Ana, Rancho Cucamonga) load clean with local content, FAQ and CTAs; nothing recommends removing or noindexing any page.
