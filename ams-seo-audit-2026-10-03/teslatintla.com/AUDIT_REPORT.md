# SEO + GEO Audit: teslatintla.com

Audit date: 2026-10-04 (UTC). Read-only. Nothing was modified, committed or deployed.
Business: Audio MotorSports (Tesla window-tint site), 22025 S Avalon Blvd Ste A, Carson CA 90745.
Companion files: SCHEMA_REPORT.md, AI_SEARCH_REPORT.md, pages.csv (143 sitemap URLs).

## 0. Method and evidence limits

Fetched with curl and python requests through the egress proxy: homepage, robots.txt, sitemap.xml, llms.txt, and **all 143 sitemap URLs** (all HTTP 200, parsed for title/H1/meta/canonical/JSON-LD/images/links), plus /es/, /es/gallery/, a 404 URL, asset headers, and the home pages of shop.audiomotorsports.com and lacarstereo.com.

Not verifiable (blocked by proxy, not bypassed):
- www.teslatintla.com (403 at proxy): **whether www redirects to apex is UNVERIFIED**.
- http://teslatintla.com (proxy "host_not_allowed"): **http to https redirect UNVERIFIED** (HSTS header is present on https).
- shop.teslatintla.com (403 at proxy): linked from every page; status UNVERIFIED.
- www.lacartint.com, www.audiomotorsports.com, www.lacarbeats.com, www.lacaralarm.com, www.amspods.com: denied. Their apex domains answer 308 to www. Sister-site comparison is therefore based on what teslatintla.com says about them plus the two sister homepages that did load.
- PageSpeed Insights returned 429 (shared quota) twice. **Core Web Vitals field/lab numbers are UNVERIFIED**; only static signals below.
- Google Search Console, GBP, backlinks, rankings: no access. Anything about them is UNVERIFIED.
- One note on data hygiene: an early homepage fetch landed in a shared /tmp folder and was overwritten with another site's HTML by a parallel process. I discarded it and re-fetched into a private folder; every number here comes from the clean re-fetch (homepage etag 21c63a7a..., 47,239 bytes).

## 1. Summary (heuristic scoring, not a Google metric)

| Area | Score /10 | One-line |
|---|---|---|
| Crawlability / indexability | 8 | Clean robots, sitemap, canonicals, no noindex, all 143 URLs 200 |
| On-page | 6 | Unique titles/H1/meta everywhere, but city titles are bare and the Carson page is titled "Avalon" |
| Content / E-E-A-T | 6 | Real prices, real hours, honest copy; 124 templated city pages, thin personal authorship |
| Schema | 6 | Valid JSON-LD everywhere; self-serving review/rating markup and entity duplication (see SCHEMA_REPORT) |
| Local SEO | 6 | NAP perfectly consistent; but the shop's own city (Carson) is mis-named and orphaned |
| Technical / perf signals | 7 | HTTP/2, brotli, immutable asset caching; 10 render-blocking CSS, 500 KB hero, no CSP |
| GEO / AI readiness | 7 | All AI crawlers allowed, llms.txt exists, FAQ-rich; llms.txt leaks internal notes |
| Sister-domain overlap | 6 | Deliberate Tesla-only vs lacartint split, but 124 doorway-style pages and a shared GBP/entity |

## 2. Crawl and indexability (evidence)

- robots.txt (379 bytes): `User-agent: * Allow: /`, Sitemap line points to https://teslatintla.com/sitemap.xml, explicit Allow for GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot. No Disallow anywhere. (Good. Nothing blocks assets, so rendering is safe.)
- sitemap.xml: 143 URLs, all returned 200 on fetch. No stale or redirecting entries. Composition: 124 city pages (`/tesla-tint-{slug}/`), 8 blog posts, blog index, gallery, locations, about, contact, book, payment-plan, privacy, terms, all-services, home.
- Weakness: every `lastmod` is 2026-09-19 or 2026-09-24 although the homepage Last-Modified header is 2026-10-02. Uniform dates look auto-stamped; Google tends to ignore them. `changefreq`/`priority` are ignored by Google.
- **Spanish pages are not in the sitemap.** Homepage declares hreflang en/es/x-default (reciprocal, correct) and /es/ plus 8 more /es/* URLs return 200 with `lang="es"` and self-canonicals, but none are in sitemap.xml. Evidence: homepage `<link rel=alternate hreflang=es href=/es/>`, sitemap contains zero /es/ URLs.
- Canonicals: all 143 pages have exactly one self-referencing canonical on the apex, trailing-slash form. No robots meta noindex on any page. No X-Robots-Tag on any page.
- Trailing slash: `/locations` and `/all-services` return 308 to the slash version (fine, permanent).
- Soft 404: an unknown URL returns a real 404 with `noindex, follow` and a branded page.
- Internal links: 1 orphan. `/tesla-tint-carson/` has zero inbound internal links from any of the 143 pages (including /locations/, which links to 121 city pages). The 123 other city pages have only 1 inbound link each (the /locations/ grid), i.e. three clicks deep with no cross-linking.
- Footer/header links to sister sites are site-wide: lacarbeats.com ~1,004 link occurrences (summed across all 143 pages), lacaralarm.com ~861, lacartint.com 293, audiomotorsports.com 289, amspods.com 288, shop.teslatintla.com 286 (UNVERIFIED target). These are normal "network chrome" links but they dominate the outbound profile.

## 3. On-page (all 143 pages parsed)

- Titles: 0 duplicates, 0 over 60 characters, 2 under 30 (privacy: 30/terms: 32 are fine; about = 21 chars is thin). Meta descriptions: all present, none duplicated, none over 160.
- H1: exactly one per page, no duplicates.
- Homepage title "Tesla Window Tint LA | Model 3, Y, S, X" (39 chars) is decent but has no "Carson", "ceramic", or price hook.
- City pages: `Tesla Window Tint {City} | Tesla Tint LA`, H1 `Tesla Window Tint for {City}`, meta `Tesla window tint for {City} — Solar Ceramic and 3M IR Ceramic on Avalon. Ask for Nick. (310) 513-8800.` One template, 124 times.
- **The shop's own page is mis-named.** `/tesla-tint-carson/` has title "Tesla Window Tint Avalon", H1 "Tesla Window Tint for Avalon", and breadcrumb "Tesla Window Tint for Avalon". The word "Carson" only appears in the address. This is the single page that should be the strongest local landing page for "tesla tint carson", and it neither says Carson in the title nor receives internal links.
- Utility pages have weak titles: /book/ "Book a Slot", /about/ "About", /privacy/, /terms/ (cosmetic, quick).
- Images: 0 missing alt on all pages except /locations/, where 121 of 123 city tile images have `alt=""`. They sit in a link grid; whether the adjacent link text carries the name was not verified, so treat as minor. Hero image has descriptive alt with address. Homepage `width/height` set on images; city tiles are lazy-loaded (122 of 123).
- Open Graph and Twitter tags present on all 143 pages.

## 4. Content and E-E-A-T

Positives (evidence on homepage, /about/, blog):
- Published installed prices, hours, appointment slots, named person (Nick), real-sounding process detail (hand-cut on a glass board, 70% VLT legal fronts, overnight drop-off policy).
- /about/ claims 20+ years, Google 4.8 from 654 reviews, Yelp 4.7 from 777 reviews, eight verbatim Yelp quotes (some dated 2019).
- 8 blog posts at 1,177 to 1,782 words, each with BlogPosting schema; model pages also have FAQPage.

Gaps:
- Authorship is a first name only ("Nick", "Zack runs the floor"). No surname, role, bio page, certifications (e.g., 3M/Llumar dealer status) are shown in the fetched text. Any such claims would need to come from the business; none were verified.
- The review quotes are 2019-era in the sample read. Fresh reviews/dates would help trust.
- Blog posts carry template-style repetition across models (same structure and numbers by design). Fine for users, light on unique insight (no photos of the actual car, no install timelines per VIN year).
- City pages (see 6) are 1,762 to 2,443 words but mostly templated: sampled 8-word-shingle Jaccard between random city pairs averaged 0.32 (range 0.15 to 0.58). Long Beach vs Torrance 0.43; Brea vs Irvine 0.45. Local colour (streets, drive time, "mall asphalt heat") is unique per page, but the skeleton is shared.

## 5. Technical and performance signals

Headers (homepage, HTTPS):
- Present: `strict-transport-security: max-age=31536000` (no includeSubDomains/preload), `x-content-type-options: nosniff`, `x-frame-options: SAMEORIGIN`, `referrer-policy: strict-origin-when-cross-origin`, `permissions-policy: geolocation=(), microphone=(), camera=()`.
- **Missing: Content-Security-Policy** (0 matches). Also `access-control-allow-origin: *` on HTML (harmless for a public site but unnecessary).
- HTTP/2, brotli (`content-encoding: br` confirmed), Vercel edge cache HIT. HTML `cache-control: public, max-age=0, must-revalidate`; assets `max-age=31536000, immutable` (good).
- Mobile: `<meta name=viewport content="width=device-width, initial-scale=1">` on all pages. Responsive hero uses separate mobile/desktop preload. Real mobile rendering was not run; **mobile usability = UNVERIFIED beyond viewport tag**.

Core Web Vitals signals (static only, PSI blocked, so UNVERIFIED as measured values):
- Homepage loads **10 stylesheets** in `<head>` (fonts, style, homepage-hero, offer-cards, ams-chat, sim, shop-white-banners, network-chrome, ams-plugin-tesla, paylater-note), all render-blocking. 5 scripts, all at the end of body (4 with defer).
- LCP candidate: hero JPG `tesla-hero-desktop.jpg` is 500,992 bytes (declared 2560x1440), preloaded with fetchpriority=high. Mobile hero 249,244 bytes. Reasonable to compress further (WebP/AVIF).
- Logo `ams-coin-gold.png` is 115,490 bytes at its 256w full size; the `<img>` has a 144w srcset variant and sizes=72px, so browsers should pick the small file (minor, only the fallback is large).
- GTM (GTM-5G9HJLQ) in head on every page; a chat widget (`ams-chat.js`) loads site-wide. Both add main-thread work (INP risk, UNVERIFIED).
- Largest HTML: /all-services/ at 96,868 bytes; average 30,951 bytes. Fine.

URL hygiene: lowercase, hyphenated, slash-terminated, flat structure (`/tesla-tint-{city}/`). Blog under `/blog/`. No parameters in internal links.

## 6. Local SEO

NAP (checked across all 143 pages):
- Phone `(310) 513-8800` appears on 143/143 pages; address string `22025 S Avalon Blvd Ste A` on all pages with city "Carson" and ZIP 90745 in header/schema. The only other numbers are the SMS line (213) 429-1092 (3 pages, labelled "Text") and two form placeholders ("(310) 555-1234", "(310) 000-0000", harmless).
- Hours Mon-Sat 9:30-18:00 are consistent in text and schema. Sunday closed.
- Entity name is inconsistent by design: schema `name` = "Audio MotorSports" (home) vs "Tesla Tint LA" (city pages) vs "Audio MotorSports" in parent. Needs one canonical name pattern matching the GBP.
- Same GBP map link (ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a) is in sameAs on teslatintla.com and the shop network; the Tesla site has no separate GBP evidence. **GBP category, reviews, photos, Tesla service attributes: UNVERIFIED (no access).**

Geo coverage:
- Homepage schema areaServed lists 27 cities (Carson, Wilmington, Harbor City, Torrance, Gardena, Compton, Lomita, San Pedro, Long Beach, Signal Hill, Lakewood, Paramount, Lynwood, South Gate, Hawthorne, Lawndale, Redondo, Hermosa, Manhattan Beach, PV Estates, RPV, Rolling Hills Estates, Bellflower, Inglewood, Irvine, Anaheim, Santa Ana) plus a 16,093 m (10 mi) GeoCircle. That contradicts the 21.8-mile Brea drive and the 124 pages that cover Malibu, Rancho Cucamonga, Chino, Pomona, Pasadena, Santa Monica and others. A 10-mile radius with pages for 40-mile cities is internally inconsistent.
- South Bay coverage is strong (Torrance, Redondo, Hermosa, Manhattan, Hawthorne, Lawndale, Lomita, San Pedro, PV, RH, RHE, El Segundo all have pages). Long Beach/Orange County: Long Beach, Lakewood, Signal Hill, Cerritos, Anaheim, Irvine, Santa Ana, Costa Mesa, Huntington Beach, Fullerton, Brea present. LA westside, SGV, IE also present.
- City pages are explicit that "We are not in {City}", with drive time and route. Honest and good for users and for AI answers ("where is X"), but they are by definition location-landing pages for places without a presence, the pattern Google calls doorway-style when thin. They are long and have unique detail, so risk is moderate, not high.
- `/contact/`, `/locations/` and the footer show the Carson address; embedding of a Google Map was not verified.

## 7. Sister-domain overlap and cannibalization

What was verified:
- teslatintla.com says explicitly: this site is Tesla glass only, "Other vehicles go to LA Car Tint" (FAQ), and it links "Automotive Window Tint" to https://www.lacartint.com/ on every page (293 links). lacartint.com was not fetchable (www denied), so its titles/pages could not be compared directly. **Overlap with lacartint.com = UNVERIFIED on their side; the stated intent is a clean split (Tesla vs everything else).** Risk areas to check once reachable: lacartint pages for "Tesla window tint", "ceramic tint Carson", "Los Angeles window tint prices", and whether lacartint has city pages that mirror these 124.
- shop.audiomotorsports.com (fetched): title "Car Window Tint & Car Audio in Carson | Audio MotorSports", canonical points to https://www.audiomotorsports.com/ (so it is a duplicate-host canonicalized to the main site, good). Its nav has "Window Tint / Tesla Tint / Automotive Window Tint / Tint Removal" and says "Tesla glass is Tesla Tint LA, same tint bay, specialty site." Overlap with teslatintla is low and defers to it.
- lacarstereo.com (fetched): `<meta name="robots" content="noindex, nofollow">` on the homepage, og:url www.lacarstereo.com, JSON-LD listing teslatintla.com in sameAs. It is intentionally not indexable at the time of fetch (maybe pre-launch). No cannibalization possible while noindexed. Flag for the owner to confirm this is intended.
- lacarbeats.com, lacaralarm.com, amspods.com: apex redirects to www (308); www denied. Overlap UNVERIFIED. They are stereo/alarm/Harley topics, so topical overlap with Tesla tint is low by design.
- All of these sites share the same NAP, the same legal entity ("Audio MotorSports Inc" in the lacarstereo schema), the same phone, the same GBP link and cross-reference each other in `sameAs`. For Google Local that is one business, one listing; the Tesla site cannot earn its own local pack position separate from the main GBP. For organic it means all six domains compete for "Carson" brand-adjacent queries from one entity.
- Within-site cannibalization: homepage, 124 city pages and 6 model blog posts all target "tesla window tint {place|model}". No keyword duplicates in titles, but the homepage vs `/tesla-tint-los-angeles/` and `/tesla-tint-carson/` are the likeliest to split "tesla tint Los Angeles/Carson" intent. Model Y L / Model Y blog posts vs the homepage simulator vs the city-page FAQs repeat the same price matrix in 100+ places, so no single page is the clearly canonical price source for search.

## 8. Prioritized findings

Critical
1. Carson page mis-named and orphaned (/tesla-tint-carson/).
2. Spanish pages (9 /es/ URLs) exist and are hreflang-linked but are missing from the sitemap.

High
3. 124 templated city pages for a one-bay shop: doorway risk and crawl-budget dilution; each has only one inbound link.
4. areaServed (10-mile GeoCircle) contradicts the 40+ mile city pages.
5. Self-serving AggregateRating/Review markup on 126 business nodes (no Google rich result, policy risk). See SCHEMA_REPORT.md.
6. llms.txt leaks internal instructions and contradicts site counts. See AI_SEARCH_REPORT.md.

Medium
7. 10 render-blocking CSS files plus 500 KB hero plus 115 KB logo on the homepage (CWV unverified).
8. No Content-Security-Policy header; HSTS lacks includeSubDomains/preload.
9. Homepage title has no Carson/ceramic/price qualifier; /book/, /about/ titles generic.
10. Uniform sitemap lastmod and unneeded changefreq/priority.
11. Entity name inconsistent (Audio MotorSports vs Tesla Tint LA) across schema nodes.

Low
12. 121 empty alts on /locations/ tiles.
13. Reviews quoted are old (2019 in sample).
14. Sister-site internal outlink volume (~2,700 sister-domain link occurrences across the 143 pages, about 19 per page).

## 9. Priority actions with next steps

See the findings list in the final message and each report for exact steps.
