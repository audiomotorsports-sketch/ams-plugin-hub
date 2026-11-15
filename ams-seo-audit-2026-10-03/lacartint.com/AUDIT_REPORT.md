# SEO + GEO + AIO Audit: lacartint.com (LA Car Tint)

Audit date: 2026-10-04 (UTC). Read-only. Nothing was modified, committed or deployed. Companion files: SCHEMA_REPORT.md, AI_SEARCH_REPORT.md, LIMITATIONS.md, pages.csv (141 rows).

> **READ THIS FIRST.** The standalone site `https://www.lacartint.com/` is blocked by the egress proxy and was **not audited**. Everything on pages, schema, FAQ, links and local content below comes from the **hub-mounted copy at https://www.audiomotorsports.com/tint/ (proxy for the standalone domain, standalone not verified)**. Findings tagged **[standalone-verified]** are from lacartint.com itself (apex headers only). Findings tagged **[mount-proxy]** come from the mount and must be re-checked against www.lacartint.com. No page is recommended for removal, merging, redirecting or noindex. Every recommendation improves a page or adds one.

## 1. What was verified

**Standalone apex [standalone-verified]**
- `http://lacartint.com/` returns 308 to `https://lacartint.com/`, which returns HTTP/2 308 to `https://www.lacartint.com/` (`server: Vercel`). Two hops to the www host, both permanent (308 preserves method; Google treats it like a 301).
- Path-preserving: `/robots.txt`, `/sitemap.xml`, `/llms.txt` and sample paths 308 to the same path on www.
- Same 308 for Googlebot and GPTBot user agents.
- HSTS `max-age=63072000` (2 years), no `includeSubDomains`, no `preload`. TLS: Let's Encrypt (YR1), valid 2026-08-10 to 2026-11-08.
- www.lacartint.com: retested at start and end, CONNECT 403 / code 000. Blocked. Not bypassed.

**Hub-mounted copy [mount-proxy]**: all 141 `/tint/` URLs fetched (all HTTP 200): 109 city pages, 15 utility, 6 Spanish, 5 service, 4 blog, home, `/tesla-tint/`. Plus hub robots, sitemap (1,090 URLs), llms.txt, and teslatintla.com (home, 3 city pages, locations, blog). Details in LIMITATIONS.md.

## 2. Scorecard (heuristic, not a Google metric; mount only)

| Area | Score /10 | One line |
|---|---|---|
| Crawl / indexability | 7 | 141/141 return 200, self-canonical, no robots meta, in sitemap. Standalone unknown. Duplicate origin risk |
| On-page | 6 | Zero duplicate titles/H1/meta, but city titles are thin and Carson is missing from the home title |
| Local content | 6 | Honest "we are not in X" copy with real routes; no Carson page; median 51% unique copy |
| Schema | 5 | Valid JSON-LD, but split `@id`, mixed types, self-serving rating, 12 pages of invisible FAQ |
| E-E-A-T | 6 | Real names, address, prices, hand-cut method; few dates, no bylines, org-authored posts |
| AI / AIO readiness | 6 | Eligible and crawlable; weak answer-first headings, no price table, thin freshness |
| Tesla-site differentiation | 5 | Both sites target Tesla tint; tint side carries the full Tesla pitch |

## 3. Crawl and indexability [mount-proxy]

- 141 of 141 URLs HTTP 200. No meta robots on any page, no `X-Robots-Tag`. Googlebot is allowed by hub robots.txt (`User-agent: *`, `Allow: /`, Disallow `/admin/` and `/planner/`).
- Canonical: 141 of 141 self-canonical to `www.audiomotorsports.com/tint/...`. The canonical on the standalone is **not verified** and is the single most important thing to check once www is reachable.
- hreflang: 6 Spanish pages and their 6 English counterparts carry reciprocal en/es/x-default. Other pages have none (fine for single-language).
- 141 of 141 have `og:*` and `twitter:card`; 0 pages with a missing viewport.
- Images: 456 `img` elements, 113 without alt, all on `/tint/locations/` and `/tint/shop/`.
- Open question [mount-proxy, unresolved]: the same copy is live on two origins. Both cannot be confirmed canonical. The resolution is **not** to remove either: keep both live, make titles and lead paragraphs distinct, keep reciprocal cross-links, and check which origin Search Console reports as the Google-selected canonical.

## 4. On-page [mount-proxy]

| Metric | Result |
|---|---|
| Duplicate titles / H1 / meta | 0 / 0 / 0 across 141 pages |
| Title length >60 | 4 (all Spanish) |
| Meta description >160 / <70 | 4 / 1 |
| One H1 per page | 141 of 141 |

Findings:
1. **Home title** is `Ceramic Window Tint LA & Long Beach | Hand-Cut` (46 chars). It names neither Carson, where the shop is, nor the brand "LA Car Tint". Improve: `Window Tint Carson CA | 3M Ceramic, Hand-Cut | LA Car Tint` (under 60). H1 "Ceramic window tint in Los Angeles and Long Beach" can add Carson.
2. **City titles** are all `Car Window Tint {City} | LA Car Tint`. Unique, but they carry no differentiator or price, and "Car Window Tint" is not how people search. Improve: `{City} Window Tint | 3M Ceramic from $329 | LA Car Tint` (about 55 chars).
3. **City H2s** are generic ("Same bay - Audio MotorSports", "FAQ", "Coming from X?"). Improve: question-style headings that match the query ("How much is ceramic tint near {City}?") with the answer as the first sentence.
4. **No Carson page.** The mount has `West Carson` (1 inbound link) but no `window-tint-carson`. Teslatintla.com owns the Carson slug (retitled "Avalon", per the earlier audit). Add a Carson page: it is the head local query and the shop's own city.
5. **FAQ page contradictions.** Meta says "no public prices", the answers publish $249/$329; two near-identical questions (`How long does tint take?` / `How long does a tint job take?`) give different answers.
6. The home page shows card prices (`$249` Solar full car, `$149` Solar Ceramic fronts for most SUVs, `$329` Solar Ceramic full) and Pay Later copy naming four finance providers while llms.txt says "Payment Plan only". Align wording.

## 5. Local content: Carson, Los Angeles, Orange County, South Bay [mount-proxy]

Coverage (109 city pages):
- **Carson**: home page only (33 mentions) plus `West Carson` (1.8 miles, 1 inbound link). Gap.
- **South Bay / Harbor**: Torrance, Gardena, Hawthorne, Lawndale, Lomita, Redondo Beach, Manhattan Beach, Hermosa Beach, El Segundo, Palos Verdes Estates, Rancho Palos Verdes, Rolling Hills, Rolling Hills Estates, Harbor City, Wilmington, San Pedro. Good.
- **Los Angeles**: Los Angeles, Santa Monica, Culver City, Inglewood, Venice, Playa Vista, Marina del Rey, West Hollywood, Beverly Hills, Boyle Heights, many neighborhoods. Wide.
- **Orange County**: Anaheim, Irvine, Santa Ana, Huntington Beach, Fullerton, Garden Grove, Fountain Valley, Seal Beach, Buena Park, La Palma, Stanton, Cypress, Westminster. No Costa Mesa, Newport Beach, Tustin or Yorba Linda page.
- Honest framing: city pages open "We are not in Torrance. The bay is Audio MotorSports on Avalon" and give a real route (405 to Avalon, Del Amo/Crenshaw, ten to fifteen minutes). This reduces misleading-location risk and is a good base.

Uniqueness (heuristic): median 51% of sentences unique (about 751 unique words per page), range 16% to 74%. Twelve pages carry under 250 unique words: Huntington Park, Bell, Norwalk, Hawaiian Gardens, Los Alamitos, South Gate, Cerritos, El Segundo and four more (see `pages.csv`, `city_unique_words`). Improve each with local detail rather than removal: a named lot or commute heat story, a real job photo with the vehicle and city, the exact route and drive time from Google Maps, and 2 local FAQs. Link neighbouring cities to each other (median 5 inbound links per city page; 10 pages have 1 or 2).

## 6. Content and E-E-A-T [mount-proxy]

Strengths: named people (Nick quotes, Zack runs the floor) on all 141 pages, full NAP on every page, real installed prices, honest scope ("what we do not do"), 3M Authorized Dealer, hand-cut-on-glass method, 20+ years. Weaknesses: only 5 of 141 pages show a verified/updated date; the 3 blog posts have an Organization author, `datePublished` only, no `dateModified`, no image; no expert byline on legal (CA 70% VLT) content; no outbound source for the legal limit (California Vehicle Code 26708 is the usual citation). Median visible words per page is 3,826 but that includes site chrome (nav, about 210 `/shop/` product links, footer), so word count overstates real body content.

## 7. Technical signals [mount-proxy unless noted]

- Hub headers: `cache-control: public, max-age=0, must-revalidate`, HSTS `max-age=31536000`, `x-frame-options: SAMEORIGIN`, no CSP. The mount is served from Vercel (`x-vercel-cache: HIT`). Apex lacartint.com HSTS is 2 years, no includeSubDomains or preload [standalone-verified].
- Pages are heavy on links: about 480 unique links per page, roughly 210 of them `/shop/` product cards. This dilutes the local and service links. Move the product grid below the fold, lazy-load it, and keep the city and service links prominent.
- Core Web Vitals: **not measured** (PageSpeed not run; no CrUX). Signals only.
- Sitemap lastmod on hub entries starts 2026-09-19; whether they reflect real edits is unverified.

## 8. Hub linkage to lacartint.com

The earlier hub audit counted about 370 hub pages linking to lacartint.com (not re-measured). Re-sampling 11 hub pages here: lacartint.com appears in 9 (a city page, `/locations/`, `/tesla/`, a Tesla city page, `/stereo/`, `/alarm/`, `/beats/`, `/about/`, `/amspods/`) and is absent from the hub home page and `/faq/`. The links are plain-brand anchors (`<a href="https://www.lacartint.com">LA Car Tint</a>`) plus `sameAs`/`subOrganization` JSON-LD. The 141 mount pages themselves contain **zero** links to lacartint.com. Improvement: give the tint link descriptive anchors on hub city pages ("window tint in Carson at LA Car Tint"), link the hub home and `/faq/` to it, and link each mount page to the standalone page for the same topic.

## 9. Tesla overlap with teslatintla.com: where queries could split, and how to differentiate

Both sites are the same shop (22025 S Avalon Blvd Ste A, Carson) and share a GBP. teslatintla.com is reachable (all pages 200, retried once on flake); lacartint.com's side is the mount.

| Query type | teslatintla.com | lacartint.com (mount copy) | Split risk |
|---|---|---|---|
| "tesla window tint los angeles" | Home: `Tesla Window Tint LA \| Model 3, Y, S, X` | `/tesla-tint/`: `Tesla Window Tint in Los Angeles \| LA Car Tint`, H1 identical, 7 FAQ, per-model prices, 3,700 words | **High.** Near-identical title/H1 intent |
| "tesla tint {city}" (Torrance, Long Beach...) | 124 `/tesla-tint-{city}/` pages, title `Tesla Window Tint Torrance \| Tesla Tint LA` | 109 `/window-tint-{city}/` pages with a Tesla card and about 12 "Tesla" mentions each | Medium |
| "tesla model y tint cost" | Model pages and 8 blog posts; prices on home and city pages | `/tesla-tint/` carries Model 3 $369, Y $349, Y L $399, S $399, X $499, Cybertruck $399, windshield $189 | **High** and a price-parity risk if one changes |
| "tesla roof / windshield tint" | Core topic | Mentioned on `/tesla-tint/` and FAQ | Medium |
| "tesla window tint carson" | `/tesla-tint-carson/`, title "Avalon" | `/tesla-tint/` says "in Our Carson Shop"; no Carson page | Medium, and Carson is open on both |
| "window tint {city}", "ceramic tint cost" (non-Tesla) | Redirects intent: "Other vehicles go to LA Car Tint" | Owner of the topic | Low (the intended split) |

Evidence of the stated split: teslatintla says "This site is Tesla glass only. Other vehicles go to LA Car Tint" and links to lacartint 4 to 8 times per page; the tint FAQ answers "Tesla tint lives on Tesla Tint LA". 77 of 141 mount pages link to teslatintla.com, 62 do not (35 of the 109 city pages). Yet the tint side has a full Tesla page that does the whole pitch, which undercuts its own FAQ answer. Also: the hub's `/tesla-tint/` link on the mount resolves with a 308 to `/tesla/` on the hub (the hub's mounted copy of teslatintla), a third copy of the Tesla content.

How to differentiate (improve both, merge neither):
1. **Tesla owns the vehicle; LA Car Tint owns the film and the non-Tesla vehicle.** teslatintla.com: model pages (3, Y, Y L, S, X, Cybertruck), roof glass, windshield, Tesla-specific heat and signal questions, Tesla price table, the `/tesla-tint-{city}/` pages. lacartint.com: 3M film comparison (Solar, Solar Ceramic, Ceramic IR, Color Stable), California 70% VLT, hand-cut method, SUV/sedan/truck price table, non-Tesla vehicle pages, all-make city pages.
2. **Rewrite lacartint `/tesla-tint/` as a film guide for Tesla owners** (title idea: `Tesla Window Tint Film Guide: Ceramic Options | LA Car Tint`), 300 to 500 words: which film for glass roof vs doors, legal fronts, what to ask. Move the model-level price block and booking CTA to a single prominent link to teslatintla.com model pages. Keep the page live.
3. **Tesla city pages vs tint city pages:** tint city titles lead with `{City} window tint`, "all makes", price and Carson; Tesla city titles keep the `Tesla Window Tint {City}` form. Cut Tesla copy on tint city pages down to one cross-link sentence ("Driving a Tesla? Tesla Tint LA handles Model 3, Y, S, X and Cybertruck in the same bay"), and add that sentence to the 35 city pages that lack the link.
4. **One price source.** Keep Tesla prices only on teslatintla.com (or generate both from one data file with a visible "Prices verified {date}" line).
5. **Carson**: put `window-tint-carson` on lacartint (all makes) and rename teslatintla's "Avalon" page to Carson. Each links the other with the anchor "Tesla" or "all other vehicles".
6. **Entity**: `sameAs` and `@id` shared and consistent (SCHEMA_REPORT 2.1). Both sites use one GBP, which is correct: use the same NAP, and do not claim two businesses.
7. **Measure**: in Search Console on both properties, export queries containing "tesla" and check which URL ranks. If both rank on the same query, differentiate the weaker one; do not remove it.

## 10. Prioritized fix list

Format: page, problem, report, impact (google | ai), effort (quick | medium | project), exact next step, evidence tag. [standalone-verified] means checked on lacartint.com itself; [mount-proxy] means from the hub-mounted copy.

| # | Page | Problem | Report | Impact | Effort | Exact next step | Tag |
|---|---|---|---|---|---|---|---|
| 1 | www.lacartint.com (all) | Standalone not audited; allowed domain missing | LIMITATIONS | google + ai | quick | Add `www.lacartint.com` to the environment's allowed domains, then re-run this audit and diff canonical, @id, robots, sitemap, llms.txt | [standalone-verified] (apex redirect confirmed; rest blocked) |
| 2 | `/window-tint-carson/` (new) and home title | No Carson page; home title omits Carson and brand | AUDIT 4 | google + ai | medium | Write a Carson page (Carson is the shop's city: address, drive routes from 405/110, price table, 3 job photos, 6 local FAQs) and retitle home `Window Tint Carson CA \| 3M Ceramic, Hand-Cut \| LA Car Tint` | [mount-proxy] |
| 3 | `/tesla-tint/` | Duplicates the Tesla site's pitch and price list | AUDIT 9 | google | medium | Rewrite as a Tesla-owner film guide; move model prices and booking to a link to teslatintla.com; retitle `Tesla Window Tint Film Guide \| LA Car Tint`. Keep the page live | [mount-proxy] |
| 4 | 12 pages (about, all-services, gallery, reviews, blog index, 3 posts, es/, es/about, es/faq, tesla-tint) | FAQPage schema with no visible FAQ | SCHEMA 2.4 | google + ai | quick | Add a visible FAQ block per page whose questions match the schema (post-specific, Spanish on es pages) | [mount-proxy] |
| 5 | All city pages and home (110) | Self-serving `aggregateRating` 4.8/654 on business node | SCHEMA 2.3 | google | quick | Show rating as text linked to GBP; keep rating markup only on `/reviews/` driven by live data | [mount-proxy] |
| 6 | All pages | Two `@id`s for one entity; `sameAs` lacks lacartint.com; node typed two ways | SCHEMA 2.1, 2.2 | ai + google | quick | Standalone: one id `https://www.lacartint.com/#business`, parent = hub `#business`. Mount: add lacartint.com to `sameAs`; use one business `@type` | [mount-proxy] |
| 7 | Home, `/specials/`, `/services/ceramic-film/` | No HTML price table; prices in cards | AI 4, 6 | ai + google | quick | Add one dated table (Solar $249, Solar Ceramic $329, SUV fronts $149, quote-only films) with `offers` in Service JSON-LD and "Prices verified {Month Year}" | [mount-proxy] |
| 8 | Home, `/services/ceramic-film/`, `/faq/`, city pages | Question headings missing; answers inside `<details>` | AI 4 | ai + google | medium | Add the 10 passages in AI_SEARCH_REPORT section 6 under question H2/H3 headings, 40 to 80 words, answer first | [mount-proxy] |
| 9 | 109 city pages | Title formula weak; generic H2s | AUDIT 4 | google | medium | Retitle `{City} Window Tint \| 3M Ceramic from $329 \| LA Car Tint`; replace H2 "FAQ" and "Same bay" with query-style headings | [mount-proxy] |
| 10 | 12 low-unique city pages (Huntington Park, Bell, Norwalk, Hawaiian Gardens, Los Alamitos, South Gate, Cerritos, El Segundo and 4 more) | Under 250 unique words | AUDIT 5 | google | project | Add route/drive time from Maps, a local heat or lot detail, a real job photo, 2 local FAQs; link to 3 neighbouring city pages | [mount-proxy] |
| 11 | 35 city pages without a teslatintla.com link; 10 city pages with 1 or 2 inbound links | Weak cross-site and neighbour links | AUDIT 9, 5 | google | quick | Add the one-sentence Tesla Tint LA cross-link; add a "nearby cities" row of 3 links | [mount-proxy] |
| 12 | `/faq/` | Meta says "no public prices"; duplicate questions with different answers | AUDIT 4 | google + ai | quick | Rewrite meta to "published prices from $249 installed"; fold the two duplicate questions into one answer inside the page | [mount-proxy] |
| 13 | `/llms.txt` (hub) and standalone llms.txt | Hub file is network-level; AI-directive lines; city count 123 vs 109 | AI 3 | ai | quick | Standalone llms.txt: tint facts, film tiers, VLT rule, price table, links to FAQ and booking, one city count, neutral wording | [mount-proxy] |
| 14 | 3 blog posts and key pages | Org author, no `dateModified`, no visible date, no legal source | AUDIT 6 | ai + google | quick | Add Person byline (Nick or Zack), "Updated {date}", `dateModified`, and cite California Vehicle Code 26708 | [mount-proxy] |
| 15 | Mount vs standalone | Same copy at two origins, both self-canonical on the mount | AUDIT 3 | google | medium | Do not remove or noindex. Check Search Console Google-selected canonical for both; differentiate titles and lead paragraphs; keep reciprocal links | [mount-proxy] |
| 16 | All pages (about 480 links each) | ~210 `/shop/` links dilute local links | AUDIT 7 | google | medium | Lazy-load the product grid below the fold; keep city/service links prominent | [mount-proxy] |
| 17 | `/tint/locations/`, `/tint/shop/` | 113 images with no alt | AUDIT 3 | google | quick | Add descriptive alt text | [mount-proxy] |
| 18 | lacartint.com apex | HSTS without includeSubDomains/preload; cert expires 2026-11-08 | AUDIT 1 | google | quick | Confirm Vercel auto-renewal; consider `includeSubDomains` once all subdomains are HTTPS | [standalone-verified] |
| 19 | Orange County coverage | No Costa Mesa, Newport Beach, Tustin or Yorba Linda page | AUDIT 5 | google | medium | Add these city pages with real drive routes and local detail | [mount-proxy] |
| 20 | Core Web Vitals (all) | Not measured | AUDIT 7 | google | quick | Run PageSpeed/CrUX on the standalone home, a city page and a service page | [standalone-verified] step pending access |

### Note on earlier hub guidance

The hub audit (FIX_LIST item 36) suggested canonicalizing or noindexing mounted copies. That is not carried into this report. This report only improves and adds.
