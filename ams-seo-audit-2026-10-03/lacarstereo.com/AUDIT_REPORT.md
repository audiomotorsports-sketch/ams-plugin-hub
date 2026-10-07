# SEO + GEO Audit: lacarstereo.com

Audit date: 2026-10-04 (UTC). Read-only audit; nothing was changed on any site or repo.
Business: LA Car Stereo, an Audio MotorSports Inc shop, 22025 S Avalon Blvd Ste A, Carson CA 90745.
Companion files: SCHEMA_REPORT.md, AI_SEARCH_REPORT.md, pages.csv (127 URLs).

## Method and evidence limits

- Fetched with curl through the sandbox proxy on 2026-10-04: homepage, robots.txt, sitemap.xml, llms.txt, and every one of the 127 URLs in sitemap.xml (fetched on the apex host, lacarstereo.com). Parsed titles, meta, H1, robots meta, canonical, JSON-LD, images and links from the raw HTML.
- NOT verified (blocked or unavailable): the www host (www.lacarstereo.com returns a proxy 403, so I cannot confirm which host is primary or how www and apex redirect to each other); http:// to https:// redirect (proxy 403); Core Web Vitals and Lighthouse (PageSpeed API returned 429 quota exceeded; no field data); Google Search Console, GBP and Yelp data (no access); sister domains lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com (proxy blocked). Anything marked "(unverified)" below is inference.
- The earlier STATUS.md said the site was unreachable. That was true at the time; the site was reachable on this run, so STATUS.md was removed.

## Health summary (heuristic, not a Lighthouse score)

| Area | Status | Note |
|---|---|---|
| Indexability | Critical | 124 of 127 sitemap URLs carry `noindex, nofollow`; robots.txt disallows all crawlers |
| Technical | Mixed | Fast HTML (TTFB about 160 ms, cached), solid security headers, clean 404, but missing canonicals on 26 pages and host mismatch |
| On-page | Fair | Unique titles and descriptions on 126 of 127 pages, but product pages are thin and templated |
| Schema | Fair | Valid JSON-LD everywhere but no Product, no FAQPage, conflicting entity on /locations/ (see SCHEMA_REPORT.md) |
| Local SEO | Fair | NAP consistent and matches sister sites; only one indexable page; no city landing pages |
| AI / GEO | Critical | All AI crawlers blocked by robots.txt, no llms.txt (see AI_SEARCH_REPORT.md) |

Overall: the site content is reasonably well built, but as deployed today it asks every search engine and AI crawler not to index it. If this is a pre-launch or staged state, treat finding 1 as a launch checklist item and confirm intent with the owner before changing anything (unverified: no evidence in the fetched files states the intent).

## Findings

### 1. Critical: sitewide noindex, nofollow (Google)
Evidence: `<meta name="robots" content="noindex, nofollow">` on 124 of 127 sitemap URLs, including home, all 6 shop categories, all 7 install pages, /packages/, /faq/, /about/, /book/ and all 100+ product pages. Only /locations/, /privacy/ and /terms/ return `index, follow`. Extra pages not in the sitemap (/contact/, /reviews/, 4 spot-checked /packages/<car>/ pages) are also noindex; /fit/ is `noindex, follow`. No X-Robots-Tag header was present. Result: these pages cannot rank. Note the policy pages are indexable while the money pages are not, which looks inverted.
Fix: remove the noindex in the page metadata template for pages that should rank; keep it on /cart/, /book/ confirmation states and /fit/ if desired. Re-verify with a fresh crawl.

### 2. Critical: robots.txt blocks everything except AdsBot (Google, AI)
Evidence (full file, 197 bytes):
```
User-Agent: AdsBot-Google        Allow: /
User-Agent: AdsBot-Google-Mobile Allow: /
User-Agent: Googlebot            Allow: /locations/
User-Agent: *                    Disallow: /
Sitemap: https://www.lacarstereo.com/sitemap.xml
```
Bingbot, GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot and all others fall under `*` and are disallowed from the whole site. Googlebot has its own group containing only an Allow line; under RFC 9309 that group has no Disallow, so Googlebot is effectively allowed everywhere and then meets the noindex meta tags. The file looks intended as "only /locations/ for Google" but does not express that. A robots Disallow also stops crawlers from seeing a noindex, so the two controls conflict for Bing and others.
Fix: replace with a single `User-agent: *` group using `Allow: /` plus `Disallow: /cart/` and `/book/` as needed (the sister site audiomotorsports.com documents why named allow-only groups should be avoided), and the www/apex-correct Sitemap line.

### 3. High: host mismatch between apex and www (Google)
Evidence: sitemap.xml, og:url, JSON-LD @id and product canonicals all use https://www.lacarstereo.com, but https://lacarstereo.com serves the pages with HTTP 200 and no redirect to www (verified on apex; www not reachable from here, unverified). Paths without a trailing slash 308-redirect to the slash version (verified for /contact and /reviews).
Fix: pick one host, 301 the other, and make robots Sitemap, sitemap, canonicals, og:url and schema agree.

### 4. High: 26 pages have no canonical tag (Google)
Evidence: the 101 product pages include a self-referencing www canonical; the homepage, all category pages, all 7 install pages, /packages/, /faq/, /about/, /locations/ and the policy pages have none (26 pages, listed in pages.csv with an empty canonical column).
Fix: emit a self-referencing absolute canonical in the shared layout for every indexable page.

### 5. High: product pages are thin and templated (Google, AI)
Evidence: about 245 words per product URL, nearly all shared header/footer boilerplate; unique content is a price, "Mono 600W RMS", and one sentence. H1 omits the brand (for example "Club A600", "X502-1", "46CXA800.1T") while the title has it. No specs, compatibility, fitment or install-time copy, no Product schema. Titles for 50 pages exceed 60 characters (max 89). Titles use "Installed in Los Angeles" although the shop is in Carson.
Fix: add brand-inclusive H1s, 100 to 200 words of per-product copy (what it fits, what the install includes, time), Product/Offer JSON-LD, and shorten titles to roughly 60 characters.

### 6. High: /locations/ is a 123-city drive-time list (Google)
Evidence: 123 city names with miles (verified count), no per-city content, no map embed, H1 is just "LA Car Stereo", title is "Locations | LA Car Stereo | LA Car Stereo" (brand repeated). It is also currently the only indexable page. A bare list of 123 towns risks being treated as a doorway-style page and gives no local relevance signal beyond town names; the claim "We serve the entire LA area" is stretched by Lancaster at 86.8 mi.
Fix: make the page an honest service-area page (shop details, directions, map, 10 to 15 nearby cities with real drive-time guidance) and consider a few genuine pages for South Bay, Long Beach and OC with unique content. Confirm no doorway pattern.

### 7. Medium: sitemap quality (Google)
Evidence: 127 URLs, all with the identical lastmod 2026-10-04T01:43:08.821Z (a build timestamp, not a real modification date); every listed URL except 3 is noindex, which Search Console reports as "Submitted URL marked noindex"; /brands/ is orphaned (in the sitemap, not linked from crawled pages); 7 /packages/<car>/ pages, 5 dash-camera products, /reviews/, /contact/ are linked but missing from the sitemap.
Fix: generate lastmod from real content changes, include only indexable URLs, add the missing indexable ones.

### 8. Medium: title and meta description issues (Google)
Evidence: home and /faq/ share the identical meta description ("Car stereo, subwoofers, amps and speakers, priced with install, in Carson."); /gallery/ description is 34 characters and /about/ 63; home title is only "LA Car Stereo: Car Stereo, Installed" with no location. No og:image or twitter:image on the pages checked (twitter:card is summary_large_image but no image is supplied).
Fix: unique descriptions of 120 to 155 characters, add Carson/Los Angeles to the homepage title, add a 1200x630 og:image.

### 9. Medium: price consistency (Google, trust)
Evidence: install pages and product pages say labor "from $149"; the F-150 package page lists "Installation $300" and "About 2 hours in the bay". May be a legitimate difference (package vs minimum) but is unexplained on-page.
Fix: state what drives the labor figure, or reconcile.

### 10. Medium: no first-hand proof content (Google, AI)
Evidence: /about/ is about 237 words with no named people; "Nick" appears only on /locations/; the homepage deliberately does not reproduce reviews ("We have not reprinted the reviews here"); /reviews/ and /gallery/ are noindex and thin (217 words on /gallery/). Reviews live only on Google, so neither search engines nor AI crawlers can quote them from this site.
Fix: add named installer(s), years of experience, certifications if any, a few quoted reviews with attribution and a link to the Google profile, and indexable gallery captions (vehicle, parts, time).

### 11. Low: security headers (Google, minor)
Evidence from the homepage response: HSTS max-age 63072000 (no includeSubDomains or preload), X-Content-Type-Options nosniff, X-Frame-Options DENY, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy set. No Content-Security-Policy. `access-control-allow-origin: *` is set on HTML. Good baseline; CSP is the main gap.

### 12. Low: performance and mobile signals (unverified lab data)
Evidence: viewport meta present; Next.js on Vercel; homepage HTML 118 KB with 13 script tags, CSS 38 KB, TTFB about 0.16 s from the sandbox (cache HIT); product images served via /_next/image (about 13 KB at w=3840 for a sample). /packages/ car pages are about 185 to 240 KB of HTML. Real CWV (LCP, INP, CLS) was not measured because the PageSpeed API was quota-limited. Run PageSpeed Insights or CrUX once the site is indexable.

### 13. Low: images
Evidence: every page has one logo image with `alt=""` (decorative, acceptable); product images carry alt text equal to the model name; /retrofit-screens/ has 101 images (all with alt except the logo). No broken internal links found among 365 unique hrefs sampled; all tested internal URLs returned 200; the 404 template returns a real 404 status.

## What is working
- Clean, hand-written titles and H1s on all 26 non-product pages; one H1 per page.
- Consistent NAP across site, schema and sister sites: 22025 S Avalon Blvd Ste A, Carson CA 90745, (310) 513-8800, Mon to Sat 9:30 to 6:00.
- Transparent installed pricing, a strong differentiator for both users and AI answers.
- Valid JSON-LD on every page; Service schema on install pages; BreadcrumbList on the 7 install detail pages and /locations/.
- google-site-verification tag present on the homepage (Search Console ownership appears set up, unverified).

## Sister-domain overlap
Fetched and compared: audiomotorsports.com, shop.audiomotorsports.com, teslatintla.com. Not reachable: lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com (unverified).
- Identical NAP, phone, hours and "Google 4.8 from 654" claim across all four sites; the reviews belong to one Google profile shared by the network. The text line (213) 429-1092 appears on the sister sites and as the sms: link here but is never shown on lacarstereo.com.
- Shared boilerplate: payment-provider copy (Snap Finance, Koalafi, EasyPay, Synchrony), "one bay in Carson" phrasing. Distinctive lacarstereo.com phrases ("Drive out loud", "Order in, 2 to 3 days", "priced with install") did not appear on the three sister pages checked, so the main copy is not duplicated verbatim.
- Product overlap risk: shop.audiomotorsports.com sells the same car-audio products (for example Kicker 46CSC654, also on lacarstereo.com) and its homepage H1 is "Shop car stereo in Carson". Its homepage canonical points to https://www.audiomotorsports.com/ rather than itself (verified on the homepage; product-level canonicals not checked). Decide which domain owns "car stereo Carson" and keep the others from competing.
- Entity: audiomotorsports.com declares `AutoRepair` with @id https://www.audiomotorsports.com/#business; lacarstereo.com declares its own `AutoPartsStore` @id and lists the hub as parentOrganization and sameAs. Reasonable structure, but see SCHEMA_REPORT.md for conflicts.
- audiomotorsports.com and teslatintla.com publish llms.txt; lacarstereo.com does not.

## Prioritised fix order
1. Decide launch intent, then remove sitewide noindex on ranking pages (finding 1).
2. Rewrite robots.txt (finding 2).
3. Fix host redirect and canonicals (findings 3, 4).
4. Upgrade product pages and /locations/ (findings 5, 6).
5. Clean sitemap (7), titles and descriptions (8), then schema and AI items in the companion reports.
