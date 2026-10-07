# SEO Audit: audiomotorsports.com (hub site)

Audit date: 2026-10-04 (UTC). Read-only. Method: live fetches through the egress proxy (curl/requests), full crawl of every URL in sitemap.xml (1,090 URLs: 1,057 HTTP 200, 33 HTTP 308). Raw data in `pages.csv`. Not run: Lighthouse/CrUX/GSC (no access), so Core Web Vitals are signals only. Lines marked **[unverified]** could not be confirmed from this network (only audiomotorsports.com and shop.audiomotorsports.com were reachable; lacartint.com, lacaralarm.com etc. returned connection failures).

## Overall assessment
Technically clean, very well structured, and unusually thorough on local schema and AI-facing files. The main risks are structural, not hygiene: (1) the hub hosts about 775 path-mounted copies of the other AMS brand sites with self-canonicals, (2) near-duplicate and thin template pages at scale, (3) weak homepage on-page targeting, and (4) hreflang and sitemap inconsistencies. No indicative numeric score is given because CWV and index data were not available.

## What passed (verified)
- HTTPS everywhere, apex 308 to www, HSTS (max-age 31536000 on www). Brotli, Vercel CDN cache HIT, homepage HTML 59.8 KB, TTFB about 0.19 s from the audit host.
- robots.txt valid: single `User-agent: *` group, `Allow: /`, disallows `/admin/` and `/planner/`, declares sitemap. No page-level `noindex`, no `X-Robots-Tag` on any crawled page.
- Every one of the 1,057 HTML pages has: a unique title, a meta description, exactly one H1, a self-referencing canonical (0 mismatches), viewport meta, `lang`, Open Graph tags. 0 invalid JSON-LD blocks. 0 `<img>` without an alt attribute (6,404 images).
- Real 404 status for unknown URLs. llms.txt present and detailed. Sitemap has no duplicate URLs and no non-www or http entries.
- Security headers present: HSTS, X-Content-Type-Options nosniff, X-Frame-Options SAMEORIGIN, Referrer-Policy, Permissions-Policy.

## Findings

### Critical / High
1. **Hub hosts ~775 mounted copies of the brand sites, all self-canonical** (sections /alarm 203, /beats 196, /tesla 152, /tint 141, /stereo 138, /amspods 130 URLs; 71% of the sitemap). Their JSON-LD names them as "LA Car Tint", "LA Car Beats" etc. with `@id` on audiomotorsports.com (e.g. `/tint/#business`), while the hub's own pages declare `lacartint.com/#business` as a subOrganization. Whether lacartint.com etc. serve the same content **[unverified, domains unreachable]**, but the structure strongly suggests cross-domain duplication and a split entity. Impact: signal dilution, brand sites and hub competing for the same queries, ambiguous entity for AI engines. Next step: decide which host owns each page; canonicalize the other, or noindex the mounts, and remove them from the sitemap.
2. **Same page mounted several times with identical text.** 32 content-hash groups of identical body text, e.g. `/services/remote-start/`, `/alarm/services/remote-start/`, `/beats/services/remote-start/`, `/amspods/services/remote-start/` (4 URLs, one text). 75 pages share a meta description with another page. Next step: collapse to one canonical per service (hub `/services/...`) and canonical the mounts to it.
3. **Homepage on-page targeting is weak.** Title `Audio MotorSports | Carson Shop` (31 chars, no service or "Carson car audio / tint" terms); H1 is `Pick a skill`; only ~256 words of body text; only 3 headings (H1, 2 H2). Next step: title like "Car Audio, Window Tint & Alarms in Carson, CA | Audio MotorSports", H1 stating what and where, add a short factual paragraph.
4. **hreflang not reciprocal on the homepage.** `/es/` declares en/es/x-default pointing at `/`, but `/` and `/long-beach/` contain no hreflang tags (checked; `/services/`, `/locations/`, `/tint/`, `/reviews/` do). Google ignores hreflang without return tags. Next step: add alternate links to `/`.

### Medium
5. **Sitemap lists 33 URLs that 308 to shop.audiomotorsports.com** (all `/shop/...` including brand and category pages). Redirecting URLs should not be in the sitemap. The shop subdomain's own sitemap URL `shop.audiomotorsports.com/sitemap.xml` also 301s (target not followed). Next step: remove the 33 URLs; submit the shop host separately.
6. **Thin pages in sitemap:** 177 pages under 300 words, 129 of them in /stereo/. 112 `/stereo/shop/...` product pages are ~100 words each, typed `AutoPartsStore` with no Product/Offer markup (see SCHEMA_REPORT). `/stereo/cart/` (67 words) is indexable and in the sitemap. Next step: noindex cart, enrich or consolidate product pages, or point them to the shop host.
7. **Template city pages.** 60 hub city pages (~2,030 words each, all unique by hash) plus per-brand city pages (`/tint/window-tint-{city}/`, `/tesla/tesla-tint-{city}/`, `/amspods/bagger-audio-{city}/`). The hub copy is honest ("there is no shop in that city"), which reduces doorway risk, but llms.txt cites 123 drive-in cities; volume of templated pages is a quality-review risk. Next step: keep pages that carry real local detail (drive time, local FAQs); consolidate the rest.
8. **Title length:** 157 pages have titles over 60 chars (e.g. product pages up to ~85 chars, "... Installed in Los Angeles | LA Car Stereo") and 24 descriptions exceed 160 chars (max 211); 7 are under 70 (e.g. `/reviews/` description is just "Google 4.8 from 654. Yelp 4.7 from 777."). Next step: trim and rewrite.
9. **Sitemap quality:** only 6 distinct `lastmod` values across 1,090 URLs (looks batch-stamped), `changefreq`/`priority` are ignored by Google. 188 KB, within limits.
10. **Message inconsistency across pages:** FAQ meta says "no public prices"; llms.txt and city FAQs publish $249/$329 tint prices. Align copy so users and AI answers agree.

### Low
11. No Content-Security-Policy header. HSTS on apex is `max-age=63072000` but www is `31536000`, and no `includeSubDomains`/`preload`.
12. No `/.well-known/security.txt`, `ai.txt`, `ai-catalog.json`, `llms-full.txt` (all 404; optional).
13. Hero images and skill thumbnails on the homepage have empty alt (acceptable if decorative; the six skill-tile images link to key sections, so descriptive alt would help). Home hero uses two `<video autoplay>` elements with `preload="none"` and poster images preloaded (good for LCP; **CWV unmeasured**).
14. Email `audiomotorsports@gmail.com` is published in schema on every page (spam-harvest risk; consider a domain address).
15. Blog is small: 4 hub posts (235-548 words) plus brand blogs; thin for topical authority.

## Internal linking and network (verified from crawl)
- Every page links to `shop.audiomotorsports.com` (1,057/1,057). 
- Pages linking to other AMS domains: lacarbeats.com 389 pages, lacartint.com 370, lacaralarm.com 340, teslatintla.com 86, amspods.com 44, plus shop.lacarbeats.com, shop.lacaralarm.com, shop.lacartint.com, shop.amspods.com (lower counts).
- **Not linked anywhere:** lacarstereo.com (the brief lists it; only lacarbeats.com appears, and the hub mounts `/stereo/` as "LA Car Stereo" and `/beats/` as "LA Car Beats"). Naming confusion: two stereo brands (stereo and beats) exist on the hub. Next step: confirm whether lacarstereo.com is a redirect or legacy domain.
- Duplicated-content domains: structurally, the six hub mounts mirror lacartint, lacarbeats (and /stereo likely lacarstereo), lacaralarm, amspods, teslatintla. Exact duplication with those hosts is **[unverified]**.
- Payment-plan partner links (Synchrony, Snap, Koalafi, EasyPay) appear on 12 pages, external, fine.
- Other outbound: Google Maps/share.google (profile links), Yelp short link (490 pages), YouTube (119), Facebook, Instagram, offerup.com (11).

## Local SEO summary (see SCHEMA_REPORT for detail)
NAP is consistent: address string `22025 S Avalon Blvd Ste A` identical on 1,049 schema blocks; phone `+13105138800` / `(310) 513-8800` consistent in format variants; hours Mon-Sat 9:30-18:00 identical. Rating 654 reviews identical on 620 blocks and matches the `/reviews/` copy (Google 4.8 from 654). Service-area coverage is extensive: hub city pages for Long Beach, Torrance, Gardena, San Pedro, Rancho Palos Verdes, Hermosa Beach, Redondo Beach, Compton, Los Angeles etc., with Orange County and Inland Empire in the locations hub. GBP is linked via maps.google.com ftid and share.google; GBP completeness itself is **[unverified]**.

## Prioritized actions
See the findings list at the end of the chat reply, plus SCHEMA_REPORT.md and AI_SEARCH_REPORT.md.
