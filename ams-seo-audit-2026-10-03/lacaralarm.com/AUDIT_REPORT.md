# SEO + GEO + AIO Audit: lacaralarm.com (LA Car Alarm)

Audit date: 2026-10-04 (UTC). Read-only. Nothing changed on any site or repo.
Companion files: SCHEMA_REPORT.md, AI_SEARCH_REPORT.md, pages.csv (57 rows), LIMITATIONS.md.
Business: LA Car Alarm, the alarm / remote start brand of Audio MotorSports Inc, 22025 S Avalon Blvd Ste A, Carson CA 90745, (310) 513-8800.

## Evidence labels (read this first)
- **[standalone-verified]**: observed directly on lacaralarm.com. Only the apex response headers qualify. www.lacaralarm.com is blocked by the egress proxy (403, retested once, not bypassed).
- **[mount-proxy]**: observed on the **hub-mounted copy, proxy for the standalone domain, standalone not verified** at https://www.audiomotorsports.com/alarm/. 56 pages fetched (home, about, services, blog, FAQ, shop, locations, es, 26 city pages). Every [mount-proxy] finding is a hypothesis about lacaralarm.com until www is reachable.

## 1. Standalone-verified facts (apex)
| Check | Result |
|---|---|
| https://lacaralarm.com/ | HTTP/2 308 to https://www.lacaralarm.com/ (Vercel) |
| http://lacaralarm.com/ | 308 to https://lacaralarm.com/, then 308 to www: two hops |
| /robots.txt, /sitemap.xml, /llms.txt on apex | each 308 to the www path; contents not readable |
| HSTS | `max-age=63072000` (2 years). No includeSubDomains or preload token on the apex response |
| TLS | TLS 1.3, Let's Encrypt cert for lacaralarm.com, valid to 2026-11-08 |
| Redirect type | 308 permanent, correct for apex-to-www consolidation |

Assessment: the apex is healthy and uses the right redirect type. Two small improvements: collapse http-to-www into one hop, and consider adding `includeSubDomains` (shop.lacaralarm.com exists) once every subdomain is HTTPS-only. Whether www serves 200, what robots says and what the canonical host is remain unverified.

## 2. Health summary (mount-proxy, heuristic, not a Lighthouse score)
| Area | Status | Note |
|---|---|---|
| Indexability (Googlebot / snippets) | Good | 56/56 fetched pages 200, no robots meta, no X-Robots-Tag, no nosnippet/max-snippet; hub robots.txt is `Allow: /` for all agents |
| Canonicals | Needs verification | All 56 canonicals are self-referencing, but to audiomotorsports.com/alarm/..., not lacaralarm.com |
| Titles | Good | All unique; 55 of 56 are 60 chars or less; one at 61 (Rancho Palos Verdes) |
| Meta descriptions | Fair | Present everywhere, unique, but short: mean 128 chars, 14 pages under 120, shortest 71 (/alarm/shop/) |
| H1 | Good | Exactly one H1 per page |
| Schema | Good coverage, inconsistent | AutoRepair + FAQPage + BreadcrumbList + Service everywhere; but 4 entity variants and URL host mismatch (see SCHEMA_REPORT.md) |
| Answer-readiness | Fair | FAQPage on 44 of 56 sampled pages; service pages reuse the home FAQ; no Carson-targeted passage |
| Local content | Mixed | City pages are unique in numbers but formulaic; contain internal-style instruction phrases; no Carson page |
| Internal linking | Good | Locations hub links 112 city pages; each city page links about 9-10 /alarm/ URLs |
| AI/GEO | Good access, thin llms | Hub robots allows all AI bots; no lacaralarm.com-specific llms.txt verified |

## 3. Findings

### F1 [mount-proxy] High: canonical, og:url and all schema URLs point at the hub host
Evidence: on all 56 pages `<link rel="canonical">` and `og:url` equal the audiomotorsports.com/alarm/... URL; the LocalBusiness `@id` is `https://www.audiomotorsports.com/alarm/#business`; `sameAs` lists audiomotorsports.com, and lacaralarm.com appears in markup only as `shop.lacaralarm.com` product links. lacaralarm.com is never declared as the brand's own URL.
Why it matters (Google): if the standalone build emits the same canonicals, Google is told lacaralarm.com's pages are copies of the hub's and may prefer the hub URL, so lacaralarm.com would not rank under its own name. Unverified for standalone.
Fix (improve, no consolidation): verify what www.lacaralarm.com emits. It should self-canonical to https://www.lacaralarm.com/<path>, with og:url, schema `url`, `@id` and breadcrumb items on the same host. Give each host its own unique introductory copy so the two copies differentiate rather than duplicate.

### F2 [mount-proxy] High: internal-style instruction text and contradictions on city pages
Evidence: city pages contain what reads like editorial guardrails, visible to users and crawlers: "Never imply nearby" / "Never claim nearby" (6 of 26 sampled), "Do not reverse that" (20 of 26), "Mickey Mouse" (20 of 26), "Zack runs the floor" (21 of 26), and "Closed today. Text Nick now and we'll hold a Monday 9:30 slot" banner in the HTML of 26 of 26. Irvine page also mentions "Spectrum" as local color. Also "we do not publish a dollar" (26 of 26) on every city page while /alarm/faq/ publishes "Viper 3108V is $269 installed. Compustar 9910 is $499 installed".
Why it matters: quoted by AI engines as-is, these read as unprofessional or contradictory and weaken trust; a price contradiction between pages lowers answer confidence.
Fix: rewrite those sentences as customer-facing copy (for example "Plan the drive: Irvine is 27 miles, 40 to 60 minutes; book a 9:30 slot") and add the two published prices to city/service pages, matching the FAQ.

### F3 [mount-proxy] High: no Carson-intent page or passage
Evidence: /alarm/car-alarm-carson/ returns 404. Carson appears only in the address, footer and a "Carson bay" line; the home H1 is "Car alarm and remote start in Los Angeles". West Carson (1.8 mi) has a page. The closest-to-shop query "remote start installation carson ca" has no page that answers it directly.
Fix (additive): add a "Remote start and car alarm in Carson" section with address, hours, drive directions from the 405/110, and published prices to /alarm/ (home) and /alarm/services/remote-start/ and link it from /alarm/car-alarm-west-carson/. A separate Carson URL is a project-level decision for the owner (hub policy says no shop-city doorway page); adding the section carries no such conflict. Do not substitute LA wording for Carson wording.

### F4 [mount-proxy] Medium: service pages repeat the homepage FAQ
Evidence: 12 pages (home, es home, services index and all 9 service pages sampled) carry the identical 8-question FAQPage: "Viper or Compustar — which do I need?", "Why are Jeeps, Kias, and Hondas stolen so often?", etc. Remote start, GPS, door actuators, fleet and dash cam pages do not answer their own topic's questions in FAQ form.
Fix: keep the shared 3 general questions, replace the other 5 per page with topic questions (see AI_SEARCH_REPORT.md, queries 1, 4, 6).

### F5 [mount-proxy] Medium: city pages share about 60 percent of text; local specifics thin
Evidence: word-sequence similarity after masking the city name is 0.58 to 0.65 across five compared pairs (Torrance, Gardena, Irvine, Newport Beach, Wilmington). Distinct parts: mileage, drive time, 8 city-named FAQs (answers use the template, for example "Torrance is 4.4 miles"). Few pages (26 sampled) have only 2 images.
Fix: add per page: nearest freeways and exits, one named neighborhood or landmark, a vehicle theft angle for that area only where supported by a source, 1 install photo from a car owned in that area, and keep the 40-80 word answer-first answer at the top. No page is removed.

### F6 [mount-proxy] Medium: short meta descriptions, generic city titles
Evidence: mean meta length 128 chars (range 71 to 167); 14 pages under 120. City titles all follow "Car Alarm Installation for <City> | LA Car Alarm" (50 to 61 chars) and omit remote start and Viper/Compustar. Home title "Car Alarm & Remote Start LA | Viper & Compustar" is good. Blog index title is 19 chars.
Fix: extend metas toward 140-155 chars with the drive distance and a published price (for example "Torrance to our Carson bay: 4.4 miles. Viper 3108V alarm $269 installed. Call (310) 513-8800."). Lengthen the blog title.

### F7 [mount-proxy] Medium: blog thin on freshness and authors
Evidence: only 3 posts; BlogPosting `datePublished` 2026-08-13 on the sampled post; no dateModified on pages, no visible author byline beyond staff names in the home schema (Albert, Richard are named in copy).
Fix: add visible "Reviewed by Richard (Remote Start Alarm System Certified), updated <date>" and a dateModified to service and blog pages; add posts for the queries in AI_SEARCH_REPORT.md.

### F8 [mount-proxy] Low: Spanish version is homepage-level only
Evidence: /alarm/es/ with hreflang en/es/x-default on the home; es pages exist for 9 info pages (per sitemap); city and service pages have no hreflang. No issue, just an opportunity: add es versions and reciprocal hreflang for the 6 service pages.

### F9 [standalone-verified] Low: redirect chain and HSTS scope
Evidence: http://lacaralarm.com goes 308, 308 (two hops) to www; HSTS on apex has no includeSubDomains/preload. Fix: configure a single-hop http-to-https-www redirect where the platform allows it, and add includeSubDomains after confirming shop.lacaralarm.com and other subdomains are HTTPS-only.

### F10 [mount-proxy] Low: images and internal links
Evidence: home 33 images with alt text, none missing; city pages only 2 images; 37 links from the home page point to shop.lacaralarm.com (product pages) — good cross-linking between www and shop. Opportunity: add install photos per city. Product schema on shop.lacaralarm.com unverified.

## 4. What is working (keep)
Unique titles and exactly one H1 on every page; BreadcrumbList on all inner pages; FAQPage on 44 of 56 fetched pages (every page type except info and shop pages) with matching visible `<details>`; consistent phone +13105138800 (46 of 52 blocks; 6 use "(310) 513-8800" formatting); consistent NAP; YouTube VideoObject with 2026-09-25 uploadDate; hub robots allows every crawler; locations hub links 112 cities.

## 5. Prioritized list
Format: page | problem | report | impact | effort | exact next step | tag. All steps improve pages; none remove, merge, redirect or noindex anything.

| # | Page | Problem | Report | Impact | Effort | Exact next step | Tag |
|---|---|---|---|---|---|---|---|
| 1 | www.lacaralarm.com (all) | Cannot verify canonical host, robots, sitemap, llms | LIMITATIONS | google+ai | quick | Allow www.lacaralarm.com and shop.lacaralarm.com in the proxy, then re-run the crawl and fill pages.csv | [standalone-verified] |
| 2 | All pages | Canonical, og:url, schema url/@id point to audiomotorsports.com/alarm | AUDIT F1, SCHEMA S1 | google | medium | On the standalone build set canonical/og:url/schema to https://www.lacaralarm.com/<path>; add unique intro per host | [mount-proxy] |
| 3 | /alarm/car-alarm-* (26 sampled of 145) | Visible internal instructions ("Never imply nearby", "Do not reverse that"), "Closed today" banner, "we do not publish a dollar" contradicting FAQ prices | AUDIT F2 | google+ai | medium | Rewrite 6 phrases into customer-facing copy in the city template; add Viper 3108V $269 and Compustar 9910 $499 installed | [mount-proxy] |
| 4 | /alarm/ and /alarm/services/remote-start/ | No Carson passage for "remote start installation carson ca" | AI Q1, AUDIT F3 | google+ai | quick | Add the Carson answer block (60 words, in AI_SEARCH_REPORT Q1) under an H2 "Remote start installation in Carson, CA" | [mount-proxy] |
| 5 | /alarm/services/* (9) | Identical 8-question FAQ copied from home | AUDIT F4, SCHEMA S3 | google+ai | medium | Swap 5 of 8 questions per page for topic questions; keep schema in sync with visible details | [mount-proxy] |
| 6 | City pages (145) | ~60 percent shared text | AUDIT F5 | google | project | Add per-city freeways, landmark, photo, one local FAQ; roll out Carson-near and South Bay first | [mount-proxy] |
| 7 | Entity schema (home vs city pages) | 4 LocalBusiness variants, mixed phone formats, AutomotiveBusiness+AutoRepair vs LocalBusiness | SCHEMA S2 | google | quick | Use one @type array and one `@id` block; telephone +13105138800 everywhere | [mount-proxy] |
| 8 | City + service titles/metas | Short metas (mean 128), templated titles | AUDIT F6 | google | quick | Rewrite metas to 140-155 chars with drive distance and a price | [mount-proxy] |
| 9 | llms.txt (lacaralarm.com) | Not verifiable; hub llms.txt covers AMS only | AI_SEARCH | ai | quick | Publish/verify a lacaralarm.com/llms.txt with address, prices, services, drive-in areas | [standalone-verified] gap |
| 10 | Blog (3 posts), service pages | No dateModified/author; thin freshness | AUDIT F7 | ai+google | medium | Add visible "updated" date, reviewer line, dateModified; write 4 posts from sample queries | [mount-proxy] |
| 11 | http://lacaralarm.com | Two redirect hops; HSTS without includeSubDomains | AUDIT F9 | google | quick | Single-hop redirect to https://www; add includeSubDomains after subdomain check | [standalone-verified] |
| 12 | /alarm/es/ + service pages | hreflang only on home | AUDIT F8 | google | medium | Add es service pages with reciprocal hreflang | [mount-proxy] |
