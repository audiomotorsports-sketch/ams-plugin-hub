# SEO + GEO + AIO Audit: amspods.com (Harley-Davidson audio pods)
Date: 2026-10-04. Method: claude-seo (seo-audit, seo-technical, seo-schema, seo-ecommerce, seo-geo checks applied by hand to fetched HTML). Read-only. Rules: every page stays live; all recommendations improve pages.

> **Evidence labels.** `[standalone-verified]` = fetched from amspods.com. `[mount-proxy]` = fetched from the hub-mounted copy at `https://www.audiomotorsports.com/amspods/` (130 URLs, all HTTP 200), used as a proxy for the standalone domain. **The standalone site was not verified**: `www.amspods.com` is refused by the egress proxy (CONNECT 403, retested once, not bypassed). See LIMITATIONS.md. Companion files: SCHEMA_REPORT.md, AI_SEARCH_REPORT.md, pages.csv.

## 1. Executive summary
- The mounted copy is technically clean at the basics: 130/130 pages return 200, one H1 each, unique titles and meta descriptions, self-referencing canonicals, valid JSON-LD (all 130 parse), no `noindex`, no `nosnippet`, hreflang en/es reciprocal on 12 page pairs. [mount-proxy]
- Biggest gaps, in order: (1) no `Product`/`Offer` markup anywhere although the core offer is a priced product (AMS pod pair, starting at $649); (2) FAQPage markup on 12 pages whose questions are not visible on the page (Google structured-data policy mismatch); (3) the on-page FAQ and service schema say "No public prices / Do you publish prices? No" while the same pages say pods start at $649; (4) internal-note phrasing leaks into public copy on at least 69 pages (e.g. "that is the schema aggregate only", "We do not invent a Long Beach motorcycle counter"); (5) 60 city pages share roughly 70% of their sentences; (6) fitment content stops at generation level (1998-2013, 2014-2023, 2024+) with no model-by-year table for pods; (7) 6 broken internal city links and ~85 live city URLs missing from the sitemap. [mount-proxy]
- Only two standalone facts are verified: apex `amspods.com` returns a single path-preserving permanent 308 to `https://www.amspods.com/...` for `/`, `/robots.txt`, `/sitemap.xml`, `/llms.txt`; HSTS `max-age=63072000`; served by Vercel. [standalone-verified]
- Unresolved question that changes the plan once www is reachable: the mounted pages canonical to `www.audiomotorsports.com/amspods/...`, not to amspods.com. If the standalone serves the same templates, two indexable copies exist. The answer is differentiation and clear cross-linking, never canonical-away or removal.

## 2. Health snapshot (mount-proxy, 130 URLs: 60 city, 25 services, 13 catalog, 12 Spanish, 5 blog/index, 15 other)
| Check | Result |
|---|---|
| HTTP status | 130 x 200 (one transient connection reset on first pass, 200 on retry) |
| `<title>` | 130 present, 0 duplicates; 7 over 60 chars (5 Spanish, 2 services); 3 under 30 |
| Meta description | 130 present, 0 duplicates; 6 over 160 chars (all Spanish, up to 194); 2 under 70 (blog index 69, shop 68) |
| H1 | exactly 1 on every page |
| Canonical | present and self-referencing on 130/130, host = www.audiomotorsports.com |
| Meta robots / X-Robots-Tag | none set (indexable, snippet-eligible) |
| Hreflang | 24 pages (12 en + 12 es), reciprocal, x-default to en |
| JSON-LD | 130/130 valid; 93 pages carry FAQPage; 62 carry AggregateRating (4.8 / 654, identical everywhere); 0 Product |
| Images without alt | 113 of 1,077 (109 on /locations/, 4 on /shop/) |
| Internal links | home 13 links; /locations/ 112; 24 pages have 0 inbound links from other crawled amspods pages |
| Dates | BlogPosting has datePublished (Aug 2026), no dateModified; visible dates found on 2 pages |

## 3. Findings (by area)

### 3.1 Technical / crawl (mount-proxy unless stated)
1. **Apex redirect is healthy.** `amspods.com` -> 308 -> `www.amspods.com`, one hop, path preserved for robots/sitemap/llms. HSTS 2 years without `includeSubDomains`/`preload` (low priority). [standalone-verified]
2. **Sitemap gap.** Hub sitemap lists 60 amspods city pages. Internal links point to 91 more `/amspods/bagger-audio-*` URLs not in the sitemap: 85 return 200 (live but unlisted), 6 return 404 (see 3.1.3). The standalone sitemap could not be read.
3. **6 broken internal links (404):** `bagger-audio-montrose`, `-burbank`, `-san-marino`, `-rowland-heights`, `-encino`, `-hollywood`, linked from 15 city pages. Fix by publishing differentiated pages for those cities or repointing each link to the nearest live city page.
4. **Orphans.** 0 inbound links from other amspods pages: `/shop/`, `/faq/`, `/about/`, `/specials/`, `/2024/`, `/all-services/`, `/privacy/`, `/terms/`, all es sub-pages except home, and city pages `sylmar`, `del-aire`, `alondra-park`, `brentwood`, `midway-city`. `/shop/` and `/2024/` are conversion pages and should be in the main nav.
5. **Rendering/weight.** Homepage HTML 107 KB, GTM loaded in head; no JS-render check was possible. Core Web Vitals not measured (no field data supplied).
6. **Canonical relationship with the hub.** See summary; verify on the standalone once reachable (title, canonical, schema `@id`/`url` should be amspods.com, not audiomotorsports.com).

### 3.2 On-page
1. **Boilerplate headings injected by template:** FAQ page H2 "car stereo shop in Carson on a Saturday at Audio MotorSports" (also Spanish FAQ); blog post H2 "bagger stereo on this Harley-Davidson in Los Angeles"; Road Glide page H2 "bagger stereo lid speakers on Harley Street Glide and Road Glide"; shop H1 "bagger stereo for Harley-Davidson" (lowercase, not matching title "Shop AMS Pods | Harley Bagger Audio"). Replace with specific, human headings.
2. **Titles/metas:** shorten the 7 long titles and 6 long Spanish descriptions; lengthen shop and blog-index descriptions (add price, models, call to action). Several blog titles are generic ("Road Glide, Street Glide, Road King | AMS Pods"). Lead titles with the query ("Road Glide Speaker Pods, Chrome or Gloss | AMS Pods").
3. **Leaked internal notes (69 pages match "invent"/"schema aggregate only"; 2024 page: "Cards fill the text. They do not send you to another shop's checkout.", "Kit photos are the manufacturer shots we host at /assets/img/2024/"; shop: "Built here, not bought in."). Rewrite as customer-facing copy. These read as spam/unfinished to users and are quoted verbatim by AI answer engines.
4. **Contradictions that hurt trust and AI extraction:**
   - Price: FAQ "Do you publish prices? No" and Service description "No public prices" vs "AMS pods start at $649 a pair" in the same pages and in meta descriptions. Make one consistent statement: pods from $649/pair, full systems quoted.
   - Model scope: 60 city pages say "Street Glide, Road Glide, and Road King. Those three only." Home/FAQ schema/services say Softail is included; shop says "Softail is allowed." Pick one rule and state it everywhere.
   - Brands: catalog meta lists "Rockford" and `/catalog/rockford-fosgate/` exists, while hub llms.txt says the shop "does not stock or recommend Rockford". Align wording.
5. **Car-service pages under the Harley brand** (window tint, Tesla tint, alarms, backup/dash cameras, remote start, GPS, door actuators, head unit, bass amps, etc.; 16 of 25 `/services/*` pages are titled "... | AMS Pods"). Improve, do not remove: add Harley/bagger framing where relevant, or a clear "same Carson shop; full car page at <sister site>" block, so the entity (Harley pods) stays clear.
6. **Images:** add descriptive alt to 113 images (109 on /locations/ are city tiles: alt "Harley bagger audio drive-in from <City>, Carson shop").

### 3.3 City pages (60 in sitemap, ~85 live)
- Median 30% of sentences are unique to the page (range 27% to 91%; West Carson is 91%, the model to copy). Titles/H1s differ only by city name. Word count per page is high (3,000-3,500 including chrome) but mostly shared.
- Differentiate, do not consolidate: for each city add (a) drive route and time from that city to 22025 S Avalon Blvd, with named freeways; (b) 2-3 real jobs/customer quotes from that area or its nearest verified neighbor; (c) local riding context (e.g. PCH, Angeles Crest, Palos Verdes loops) tied to model use; (d) a city-specific FAQ visible and in schema; (e) links to 3 nearest city pages, the model pages and `/2024/`.
- Remove internal-note copy first (3.2.3); it appears on every city page.

### 3.4 Fitment (Harley model/year coverage)
Coverage observed in mounted copy (mentions across 130 pages): Road Glide 853, Street Glide 840, Road King 751, Softail 70, CVO 20, Ultra Limited 1, Electra Glide 0, Tri Glide 0, Low Rider 0, Fat Boy 0, Heritage 0, Freewheeler 0; no model codes (FLTRX, FLHX, FLHR, FLTRXS, FLHXS). Year ranges appear only as 1998-2013, 2014-2023, 2024+ on catalog/radio kits (Diamond, Cicada, Hertz) and `/2024/`.
- The product that matters (the pod pair) has no stated model-year fitment: no table of which crash-bar/mustache-bar combinations, years, model codes, speaker size, amp location and lead time. Only prose ("mustache bar uses a different mount").
- Add a visible fitment table to `/services/ams-pods/` and each model page (Road Glide, Street Glide, Road King, Softail), and a short "Does it fit my year?" block. Include model codes and the generations (1998-2013, 2014-2023, 2024+) the shop already uses. Mark the shop's "no Sportster/Dyna/Indian" boundary explicitly; it is an asset for AI answers.
- Terms riders search and the site never uses: "Ultra Limited", "Electra Glide", "Tri Glide", "saddlebag lid speakers", "fairing speakers", "tour-pak". Add only where the shop does the work; if it does not, say so in one line (the existing "not Sportster/Dyna" pattern).

### 3.5 E-commerce (seo-ecommerce lens)
- No `Product`, `Offer` with price, `brand`, `sku`, `shippingDetails` or `hasMerchantReturnPolicy` anywhere (SCHEMA_REPORT.md). `/shop/` is a `CollectionPage` listing "AMS Chrome pod pair / Gloss pod pair, starting at $649" with no product pages of its own; catalog pages are `ItemList` pointing off-site (hertz-audio.com) with no on-site detail.
- 385 `Offer` nodes in Service/OfferCatalog carry no price, currency or availability, so they validate as empty offers and earn nothing.
- Add dedicated, indexable product sections or pages for "AMS Chrome pod pair" and "AMS Gloss pod pair" (price from $649, made to order about three weeks, crash-bar bracket and screws included, ships nationwide per the shop page, fitment table, photo/video, reviews with source). Link them from nav, home, model pages and `/shop/`.
- Standalone `shop.amspods.com` exists (linked from the home page for amps/speakers) and is also unreachable here. [mount-proxy for the link; shop host not verified]

### 3.6 Trust / E-E-A-T
- Strengths: named maker (Richard, in-house since 2003; in trade since 1998), named service lead, address/phone/hours consistent in schema and copy, Google 4.8/654 with source text, YouTube job videos with VideoObject.
- Gaps: blog `author` is `Organization`, not a Person; no `dateModified`; only 4 posts (Aug 2026) and no visible "updated" dates on commercial pages; AggregateRating of the business marked up on 62 pages where the visible review text is only a page-level excerpt; a `Review` node count of 10 versus 654 claimed reviews.
- Add a visible bio block for Richard (Person schema, sameAs to YouTube/Instagram), "Reviewed/Updated <date>" on pricing/fitment pages, and a link from each rating to the Google Business Profile.

### 3.7 Spanish pages (12)
English FAQ schema on Spanish pages (`/es/`, `/es/faq/` questions are English while visible Q&A is Spanish); Spanish titles 61-69 chars and descriptions up to 194. Translate the schema to match visible Spanish text and trim lengths. Hreflang itself is correct. Spanish coverage stops at 12 pages (no es model pages or es city pages) - extend with Spanish versions of Road Glide/Street Glide/Road King pages.

## 4. What good looks like (keep)
Single-H1 discipline, unique titles/descriptions, self canonicals, valid JSON-LD with a consistent `@id` business entity and sameAs including GBP, YouTube and sister sites, breadcrumbs everywhere except home, answer-first FAQ phrasing in schema, and clear "not Sportster/Dyna/Indian/metric" scope statements.

## 5. Prioritized list
Sorted by impact then effort. Impact = who benefits (google | ai). Effort: quick (under a day), medium (days), project (weeks). Source tag shows evidence.

| # | Page | Problem | Report | Impact | Effort | Exact next step | Tag |
|---|---|---|---|---|---|---|---|
| 1 | /services/ams-pods/, /shop/, /build-your-own/, home | No Product/Offer schema for a priced product; Offer nodes have no price | SCHEMA_REPORT, AUDIT 3.5 | google, ai | medium | Add Product JSON-LD for "AMS Chrome pod pair" and "AMS Gloss pod pair": brand AMS Pods, offers price 649 USD (priceSpecification minPrice, "starting at"), availability PreOrder/made to order, itemCondition New, shippingDetails (nationwide), image, description, review/aggregateRating only if visible | [mount-proxy] |
| 2 | /services/ams-pods/, road-glide, street-glide, road-king, bagger-builds, /blog/ + 4 posts, /es/, /es/faq/ | FAQPage schema questions not visible on page (12 pages) | SCHEMA_REPORT 3.2 | google | quick | Render every schema Q&A as a visible accordion/section on the same page; for es pages translate the schema to Spanish | [mount-proxy] |
| 3 | /services/ams-pods/ FAQ + Service description, home FAQ, /2024/ | "No public prices" contradicts "$649 a pair" | AUDIT 3.2.4 | ai, google | quick | Rewrite Q "Do you publish prices?" answer: "Pods start at $649 a pair, chrome or gloss. Systems with speakers, amp and install are quoted by year and model." Update schema text to match | [mount-proxy] |
| 4 | 69 pages incl. all city pages, /2024/, /shop/ | Internal/dev notes in public copy ("schema aggregate only", "We do not invent...") | AUDIT 3.2.3 | google, ai | medium | Search templates for these strings and rewrite as customer-facing sentences (e.g. "Google shows 4.8 from 654 reviews; read them on Google") | [mount-proxy] |
| 5 | /services/ams-pods/ and 4 model pages | No model-by-year fitment table for pods | AUDIT 3.4, AI_SEARCH Q1-Q7 | ai, google | project | Add table: model, years, model code, mount (crash/mustache bar), speaker, amp location, lead time; add "Does it fit my year?" answer block | [mount-proxy] |
| 6 | 60 city pages (+85 live unlisted) | ~70% shared copy; city name swapped | AUDIT 3.3 | google, ai | project | Add per-city route/time, 2-3 local jobs or reviews, local riding context, city FAQ (visible+schema), 3 nearest-city links; start with Long Beach, Torrance, Anaheim Hills | [mount-proxy] |
| 7 | 15 city pages linking to montrose, burbank, san-marino, rowland-heights, encino, hollywood | 6 internal links return 404 | AUDIT 3.1.3 | google | quick | Publish the 6 pages with differentiated content, or repoint each link to nearest live city (e.g. montrose -> la-crescenta-montrose) | [mount-proxy] |
| 8 | sitemap | 85 live city URLs absent from sitemap; standalone sitemap unknown | AUDIT 3.1.2 | google | quick | Add all live `/bagger-audio-*` URLs with lastmod; on standalone confirm sitemap lists every page | [mount-proxy] |
| 9 | /shop/, /faq/, /2024/, /about/, /specials/, 5 city pages | 0 inbound internal links | AUDIT 3.1.4 | google, ai | quick | Add Shop, FAQ, 2024+, About, Specials to header/footer nav; add each orphan city to its nearest neighbors' "nearby" lists | [mount-proxy] |
| 10 | 62 pages | AggregateRating (4.8/654) on business entity, repeated, with only 10 Review nodes | SCHEMA_REPORT 3.3 | google | quick | Keep the visible rating with GBP link; mark Review/AggregateRating only on pages that show the reviews (home, /reviews/); source it to Google Business Profile | [mount-proxy] |
| 11 | /faq/, blog posts, /shop/, Road Glide page | Template headings ("car stereo shop in Carson on a Saturday...", lowercase shop H1) | AUDIT 3.2.1 | google | quick | Replace with specific human headings matching the title | [mount-proxy] |
| 12 | Titles/descriptions (7 long, 2 short, 6 long Spanish) | Truncation/weak snippets | AUDIT 3.2.2 | google | quick | Rewrite to <=60 / 120-155 chars, query-first, with $649 and models | [mount-proxy] |
| 13 | 25 services pages (16 car-service) | Car services titled "| AMS Pods"; entity dilution | AUDIT 3.2.5 | google, ai | medium | Add Harley/bagger context or sister-site cross-link block to each; keep pages | [mount-proxy] |
| 14 | /locations/, /shop/ | 113 images without alt | AUDIT 3.2.6 | google | quick | Add descriptive alt text | [mount-proxy] |
| 15 | blog index + 4 posts | Org author, no dateModified, 4 posts only | AUDIT 3.6 | ai, google | medium | Add visible byline (Richard) and Person schema, dateModified, and posts for each model/year question in AI_SEARCH_REPORT | [mount-proxy] |
| 16 | Spanish pages | English FAQ schema; titles/metas too long; few es pages | AUDIT 3.7 | google | medium | Translate schema, trim lengths, add es model pages | [mount-proxy] |
| 17 | catalog index, /catalog/rockford-fosgate/, hub llms.txt | Rockford listed vs "does not recommend Rockford" | AUDIT 3.2.4 | ai | quick | Align wording on page and llms.txt (e.g. "available on request, not our recommendation") | [mount-proxy] |
| 18 | www.amspods.com (all), robots.txt, sitemap.xml, llms.txt | Standalone unverified | LIMITATIONS | google, ai | quick | Allow www.amspods.com in the proxy, then re-run this audit's checks on the standalone (canonical host, schema `url`/`@id`, sitemap, robots, AI bots) | [standalone-verified] gap |
| 19 | amspods.com apex | HSTS has no includeSubDomains/preload | AUDIT 3.1.1 | google | quick | After confirming all subdomains serve HTTPS, add `includeSubDomains` and consider preload | [standalone-verified] |
| 20 | llms.txt (standalone) | Unknown; hub llms.txt gives amspods one root line | AI_SEARCH | ai | quick | Publish `https://www.amspods.com/llms.txt` with pods price, models/years, build time, ship policy, key pages (not used by Google Search) | [mount-proxy] |
