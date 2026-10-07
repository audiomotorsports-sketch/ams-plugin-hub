# LA Car Alarm - Phase 2 launch audit (every finding is [mount-proxy])
Audited 2026-10-04 via the hub-mounted copy https://www.audiomotorsports.com/alarm/ . Standalone www.lacaralarm.com is proxy-blocked: unverifiable from here (HTTP 403 / CONNECT tunnel failure). Read-only; no form submitted. Evidence: b1/, b2/, b3/ (probe.json + screenshots), html/ (raw HTML).

## Apex headers (recorded)
- `https://lacaralarm.com/` -> HTTP/2 308, `location: https://www.lacaralarm.com/`, `refresh: 0;url=https://www.lacaralarm.com/`, server Vercel, hsts max-age=63072000, cache-control public,max-age=0,must-revalidate, content-type text/plain.
- `http://www.lacaralarm.com/` -> 403 `x-deny-reason: host_not_allowed` (egress proxy; unverifiable). `https://www.lacaralarm.com/` -> CONNECT 403 (unverifiable).
- Consequence: canonical, og:url, hreflang, robots, sitemap and redirect behaviour of the real domain are NOT verified. On the mount, canonical/og:url all point to https://www.audiomotorsports.com/alarm/... (expected for the mount; must be re-checked on the real domain at cutover). /alarm/robots.txt and /alarm/sitemap.xml are 404 on the mount (mount artifact, unverifiable).

## URLs sampled (22)
/alarm/, /alarm/services/remote-start/, /car-alarms/, /viper-installs/, /alarm/faq/, /alarm/blog/, /alarm/blog/viper-vs-compustar/, /alarm/shop/, product https://shop.audiomotorsports.com/shop/alarms-remote-start/viper-3108v/ (the mount's shop links go to the hub shop; /alarm/shop/<product> is 404 on the mount), /alarm/es/ (exists, 200), cities: car-alarm-west-carson, -irvine (OC), -pasadena (far-out), -torrance (South Bay), /alarm/contact/, /alarm/book/, /alarm/car-alarm-carson/ (404). /alarm/reviews/ was in b3 (see note at end).

## (a) Visual phone + desktop
- [mount-proxy] MUST-FIX (verify) /alarm/ desktop: screenshot b1/alarm_desktop.png renders UNSTYLED (default serif font, blue underlined links, black H1 on dark hero, nav as plain text, "Our ads:" row on white). Same moment console shows `Refused to apply style ... style.css ... MIME type ('text/plain')`. LCP 10.7s on that run. Cause is the stylesheet being served with the wrong content-type intermittently (see c1). Next step: find why /sites/lacaralarm/assets/css/* sometimes returns text/plain and fix so it is always text/css (+ `X-Content-Type-Options` consistent).
- [mount-proxy] MUST-FIX /alarm/ phone: above the fold is a tall hero image/video poster (Jessie "Chat with Jessie" banner) with a large empty black area; the H1 "Car alarm and remote start in Los Angeles" starts at the very bottom of the first viewport and is partly covered by the sticky "Text Nick / Call" bar and chat bubble. The primary CTA text buttons are below the fold. Next step: shorten hero to ~60vh or move H1 + Text Nick/Book buttons above the Jessie banner on phone.
- [mount-proxy] MUST-FIX city page phone (west-carson, irvine, pasadena, torrance): first screen is a full-height car photo with only "WEST CARSON / AUDIO MOTORSPORTS" wordmark; no H1, no phone/CTA content visible above the fold apart from the sticky bar. Next step: bring H1 + one-line answer + CTA into first viewport (do not remove the hero).
- [mount-proxy] NICE: remote-start page phone: 600px hero image before breadcrumb/H1; H1 begins at fold behind sticky bar (same pattern).
- [mount-proxy] MUST-FIX product page (shop.audiomotorsports.com viper-3108v) phone: the "More car alarm and remote start we stock" cards show blank white image boxes (images not rendered at capture; verify lazy-load) and sticky Call/Text/Quote bar sits over the price/"Reserve for pickup" block (b3 screenshot). Next step: verify related-product images load without scroll and add bottom padding so sticky bar doesn't cover the purchase area.
- Header on the mount reads "Audio MotorSports" (hub chrome), not "LA Car Alarm"; footer lists sister desks. NICE: confirm the standalone domain shows LA Car Alarm branding (unverifiable here).
- No horizontal scroll on any page tested, phone or desktop (overflow_x = 0 on all 44 probe rows). Broken images: 0. Images missing alt: 0.
- Tap targets: probe flags 8-31 small targets on phone per page (e.g. 31 on /alarm/ and /alarm/es/). NICE: enlarge hub mega-menu/footer links to >=44px.

## (b) Click-through
- Nav (hub chrome) goes to hub root paths (/tesla/, /tint/, /amspods/, /stereo/, /beats/, /contact/). Each page exposes ~467 hub mega-menu links (header + /services/* /shop/* /vehicles/*). Serial recheck (curl, one at a time) of the 67 links that timed out under parallel probe load: 31 x 200, 34 x 308, 0 x 404, 2 transient SSL resets that succeeded on retry rule-of-thumb (harness/load, not site bugs). Examples: /services/car-alarms/ 308 -> /alarm/services/car-alarms/ (good); /shop/alarms-remote-start/ 308 -> https://shop.audiomotorsports.com/shop/alarms-remote-start/ .
- 403 on youtube.com, google.com/maps, share.google, yelp.to, instagram, offerup, facebook, shop.lacaralarm.com, www.lacarbeats.com, www.lacartint.com, www.amspods.com: unverifiable from here, not site bugs.
- MUST-FIX candidate [mount-proxy]: every /alarm/ page links to `/west-carson/` (a hub page, 200) and /alarm/ home links to product URLs at `https://shop.lacaralarm.com/...` (unverifiable) while the mount's own /alarm/shop/ links to root `/shop/...` which 308s to shop.audiomotorsports.com. Mount-relative vs standalone links can't be reconciled here; verify on the real domain that shop links and /west-carson/ resolve to lacaralarm.com URLs, not hub URLs.
- /alarm/car-alarm-carson/ : 404 (title "Page not found | Audio MotorSports", canonical /404.html). It is NOT linked from any of the 16 sampled pages' HTML (grep of href: only /west-carson/ and car-alarm-west-carson). Not in pages.csv as an indexed page. Verdict: no launch blocker unless an external/GBP/old sitemap URL points there; NICE: serve the same 404 template with LA Car Alarm nav and a link to /alarm/car-alarm-west-carson/ (do not redirect-away any city page).
- Home mentions 4 hrefs to lacarbeats.com/lacartint.com (cross-brand), fine.

### Forms (inspect only, not submitted)
- /alarm/contact/: `<form class="ajax-form quote-lead-form" action="/api/quote/" method="POST">`; fields: phone*, year*, make*, model*, old_tint select*, service select*, name*, email*, message; hidden `_captcha=false`, `_subject`, `source_page=/contact`; honeypot `company` (hp-field, tabindex -1); buttons "Send My Request" + "Text My Request". No visible captcha. 
  - NICE: `autofocus` on the phone field opens the keyboard / scrolls on phone load. 
  - NICE: "old_tint" select ("old tint?") is required on an alarm quote form - a tint-form leftover; a user cannot submit without answering. Likely MUST-FIX for conversion if there is no "n/a" option: verify option list.
- /alarm/book/: `action="/api/quote/" method=POST`; service*, year*, make*, model*, day (date)*, slot radio 10:00 AM / 12:00 PM *, name*, phone*; honeypot `company`; hidden source_page=/book/, message. Button "Request this slot". Note the form posts to the shared hub endpoint /api/quote/ (mount: root-relative). Success markup not visible without submit - unverified.
- /alarm/services/remote-start/ (also car-alarms, viper-installs): `action="" method="POST"` with honeypot `_honey`, hidden `_captcha`, source_page. Empty action relies on JS (ajax-form). MUST-VERIFY that the JS handler is attached; with JS failing it posts to the page itself (POST to a static page = 405/404). Honeypot field name is `_honey` here vs `company` on contact/book - inconsistent, confirm the endpoint reads both.
- Blog/FAQ/shop/home carry a lone textarea in a GET form with no action (Jessie chat widget input) - fine.

## (c) Bugs
1. [mount-proxy] MUST-FIX (intermittent) CSS served `text/plain`: console "Refused to apply style ... MIME type ('text/plain')". Seen 9 times in 44 loads, each time a different file (style.css, paylater-note.css, page-short.css, services-tab.css, shop-tickets-ams.css, shop-mega.css). Sequential curl 25x of paylater-note.css and 3x of the others always returned `200 text/css; charset=utf-8`, immutable cache - so it appears only under parallel/HTTP2 load (and the proxy may contribute). It coincides with the 4 LCP outliers of ~10.6-10.8s (home desktop, viper-installs phone, west-carson phone, pasadena phone). Next step: reproduce from a non-proxied browser; check Vercel/Cloudflare edge for responses that fall back to text/plain under load.
2. [mount-proxy] MUST-FIX **leaked instruction text visible on city pages** (not in JSON-LD only; visible body copy, FAQ answers and schema):
   - /alarm/car-alarm-irvine/: "Never imply nearby." x6 visible (e.g. "The 405 north to Avalon. Figure forty to sixty minutes or more. Never imply nearby. We do not invent an Irvine storefront."), "Do not reverse that." x2 visible, "We do not invent an Irvine storefront" x6, "No Mickey Mouse work after 27 miles" x3, "Protect is worth the drive" x2. The FAQPage JSON-LD answer also contains "Do not reverse that."
   - /alarm/car-alarm-torrance/: "Do not reverse that." x4 visible ("Compustar for Dodge / Jeep / Chrysler. Viper for Ford / GMC fleet. Do not reverse that."), "We will not quote..." x1, "Mickey Mouse" x1; also in FAQPage JSON-LD.
   - /alarm/car-alarm-pasadena/: softened variant visible: "Platform mapping here is fixed and we do not reverse it."; no "Never imply nearby" found. /alarm/car-alarm-west-carson/: none of the phrases found.
   - /alarm/blog/: "We do not invent a sixth brand for a post." is visible in a post excerpt (writer note). Other blog/FAQ/contact/book/remote-start/reviews/es/shop pages: none.
   Next step: rewrite those sentences as customer-facing copy (e.g. "From Irvine plan on 40-60 minutes up the 405; call before you leave."), regenerate FAQPage JSON-LD to match. Pages stay live; this is copy-only. Same template is probably on the other ~100 drive-in pages: grep the templates for "Never imply", "Do not reverse", "We do not invent", "Mickey Mouse".
3. [mount-proxy] NICE: /alarm/es/ exists (200, ~5.2k words, Spanish title/meta, own canonical /alarm/es/); hreflang present on 3 hreflang tags per pages.csv for the English home (verify reciprocal tags and that Spanish text on the page has no English leftovers - see Phase 1 pages.csv).
4. Meta: all 22 pages have title, description, viewport `width=device-width, initial-scale=1`, canonical, lang=en, no robots meta (indexable), OG title/image/url, favicon (200) + apple-touch-icon. The 404 page canonical points to /404.html (NICE).
5. Console errors besides (1): only proxy-blocked hosts (YouTube embeds, googletagmanager gtm.js `ERR_TUNNEL_CONNECTION_FAILED`: unverifiable). Page errors (JS exceptions): 0 on every page. Mixed content: 0. Warnings: "Unrecognized feature: 'web-share'", "Allow attribute will take precedence over 'allowfullscreen'" (YouTube iframe, NICE).
6. NICE: West Carson page title/H1 consistent; title lengths 41-58 chars OK; some meta descriptions are 88-102 chars (short) on blog/shop - cosmetic.

## (d) Speed (lab, proxied sandbox; lab != field)
| Page (phone / desktop) | LCP ms | CLS | TBT-proxy ms | TTFB ms | KB / reqs |
|---|---|---|---|---|---|
| /alarm/ | 1504 / **10728** | 0 / 0 | 187 / 156 | 126 / 266 | 846 / 44 |
| remote-start | 2808 / 1360 | 0 | 258 / 89 | 656 / 392 | 530 / 26 |
| car-alarms | 1728 / 1664 | 0 | 59 / 13 | 423 / 503 | 543 / 26 |
| viper-installs | **10716** / 1712 | 0 | 16 / 297 | 208 / 271 | 338 / 30 (1116KB desktop) |
| faq | 1556 / 2408 | 0 | 31 / 185 | 132 / 358 | 256 / 29 |
| blog | 1488 / 1312 | 0 | 98 / 48 | 317 / 298 | 251 / 29 |
| blog viper-vs-compustar | 1304 / 1296 | 0 | 0 / 30 | 303 / 356 | 191 / 27 |
| shop | 1192 / 1508 | 0 | 37 / 150 | 359 / 332 | 290 / 38 |
| es | 1248 / 1892 | 0 | 90 / 327 | 198 / 264 | 726 / 42 |
| west-carson | **10820** / 1648 | 0 | 30 / 186 | 223 / 348 | 386 / 30 |
| irvine | 1644 / 1604 | 0 | 0 / 198 | 300 / 145 | 387 |
| pasadena | **10592** / 992 | 0 | 0 / 35 | 133 / 132 | 400 |
| torrance | 1068 / 1244 | 0 | 16 / 119 | 170 / 161 | 362 |
| contact | 1856 / 1196 | 0 | 7 / 27 | 343 / 484 | 450 |
| book | 888 / 800 | 0 | 0 / 14 | 176 / 205 | 177 |
| car-alarm-carson (404) | 2944 / 4532 | 0.001 | 62 / 206 | 615 / 776 | 176 |
- CLS is 0 everywhere (best). The four LCP outliers (>4s = MUST-FIX if real) each coincide with a refused stylesheet (issue c1), so they are likely the same root cause; typical LCP is 1.0-2.8s. Re-test from an unproxied network.
- NICE: /alarm/ ships 3 autoplaying mp4s (mopar-compustar-ad, viper-5908v-ad, lacaralarm-banner jessie 9x16; ERR_ABORTED when aborted) and 846KB on phone; lazy-start the videos below the fold.

## MUST-FIX summary (10)
1. Visible leaked instruction text on city pages: "Never imply nearby." (Irvine x6), "Do not reverse that." (Irvine, Torrance; also inside FAQPage JSON-LD), "We do not invent ...", "Mickey Mouse", "We will not quote"; softened "we do not reverse it" on Pasadena; "We do not invent a sixth brand for a post" on /alarm/blog/. Rewrite as customer copy and regenerate schema.
2. Intermittent stylesheets served as text/plain (page renders unstyled; /alarm/ desktop screenshot proves it). Fix content-type; reproduce unproxied.
3. LCP ~10.6-10.8s on 4 loads (same cause as #2); re-test after fix.
4. Phone home: H1 and CTAs sit at/below fold under the sticky bar and a big empty hero area.
5. Phone city pages: hero photo fills first screen with no H1/CTA content above the fold.
6. Product page (hub shop): related-product images blank, sticky bar overlaps purchase block.
7. Forms: confirm `action=""` forms on service pages work via JS; required "old tint" select on the contact quote form is a tint leftover; honeypot names inconsistent (`company` vs `_honey`).
8. Cross-domain links: mount root-relative links (/west-carson/, /shop/..., /api/quote/) and `shop.lacaralarm.com` product links - verify on lacaralarm.com they stay on lacaralarm.com.
9. /alarm/car-alarm-carson/ is 404 (not linked anywhere sampled); make sure no external/GBP/sitemap reference points to it; give the 404 an LA Car Alarm template.
10. Real-domain canonical, og:url, hreflang, robots.txt, sitemap.xml and apex->www redirect chain are unverifiable here (www.lacaralarm.com blocked); verify at cutover.

Note: b3 probe (viper-3108v product + /alarm/reviews/) was still running when this report was written; its phone screenshot was reviewed (b3/shop-alarms-remote-start-viper-3108v_phone.png), its probe.json may appear later. No finding recommends removing, merging, redirecting or noindexing any page.

## Addendum: b3 results (product + reviews)
- /alarm/reviews/ phone: LCP 10860ms, CLS 0, TTFB 349ms; two stylesheets refused as text/plain (style.css, page-short.css) -> confirms MUST-FIX c1/c3 (5th LCP outlier). Desktop 1284ms, clean.
- Product shop.audiomotorsports.com/shop/alarms-remote-start/viper-3108v/: LCP 1660 phone / 1328 desktop, CLS 0, no page errors, canonical self. Console errors on both viewports: a 404 resource, a 500 resource, and `Refused to execute script from .../_vercel/insights/script.js` (wrong MIME / not served). MUST-FIX (console error on a purchase page): find which asset returns 404 and 500 (see b3/probe.json `failed`) and fix/enable Vercel Insights script path.
