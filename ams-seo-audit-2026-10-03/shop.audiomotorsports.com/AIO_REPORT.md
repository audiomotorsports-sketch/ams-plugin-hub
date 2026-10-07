# AIO + GEO Addendum: shop.audiomotorsports.com

Audited 2026-10-04. Read-only. Builds on AUDIT_REPORT.md, SCHEMA_REPORT.md, AI_SEARCH_REPORT.md and pages.csv (not repeated here). Every recommendation below improves an existing page; none removes, merges, redirects away or noindexes anything. "AIO" = Google AI Overviews.

## Method and limits

- Fetched live with curl via the egress proxy (retries on TLS resets). Sample: 33 distinct collection/brand/product URLs from pages.csv (19 collection/brand, 14 product), plus 11 further randomly chosen product URLs and 4 hub URLs for robots/canonical checks. Robots.txt, llms.txt and per-user-agent status were fetched live.
- NOT verified: Search Console index status (so "indexed" is inferred from the page's own directives), live AIO/ChatGPT/Perplexity citations, Rich Results Test, Merchant Center diagnostics, JS-rendered view. User-agent tests were spoofed from a non-Google IP, so they prove the site and CDN do not block by UA string; they cannot prove that real bot IPs get through a WAF that verifies by IP. Scores are estimates.
- Per RULES.md: Google-Extended does not affect AI Overviews; llms.txt is not used by Google Search.

## 1. AIO eligibility

AIO eligibility = indexed by Googlebot + snippet-eligible + not blocked in robots.

### 1.1 Headline finding (NEW, High, Google + AI): ~282 of ~285 product pages carry `<meta name="robots" content="noindex, follow">`

Evidence: 22 of 25 product pages fetched had `noindex, follow` in the HTML head. The same result came for UA `Mozilla/5.0`, desktop Googlebot and Googlebot-Smartphone (not UA-dependent), with no X-Robots-Tag header. The 3 exceptions are the dash cams (Momento IC6, M7 Wi-Fi, M7 MD-7200), which have no robots meta and are the only product pages in the sitemap. Prior reports noted self-canonicals and that product pages are missing from the sitemap but did not catch the noindex; the missing-sitemap finding is probably a symptom of the same decision.

Effect: a noindex page cannot appear in AI Overviews, AI Mode shopping surfaces, free Merchant listings (web-crawled), or classic results, however good its Product/Offer schema is. All Product/Offer schema work in SCHEMA_REPORT.md currently has no Google payoff on these URLs. Collections and brand pages (the other 40 sitemap URLs) are indexable, so they carry all of the shop's AIO eligibility today. Bing, OAI-SearchBot and Claude-SearchBot also honor noindex in their own indexing, so AI-search engines that rely on those indexes are affected too (honoring varies by vendor; unverified per vendor).

Fix direction (improvement, not removal): make the product pages indexable, in stages, starting with the products that have real prices and the richest content (see priority list P1). Do not do this blindly for all 285 pages at once if the pages are still boilerplate; staging is a quality choice, and each page should carry unique content (section 2) when it is opened up. Whether the noindex was intentional (for example to avoid thin content or to avoid competing with the hub mirror) is unknown; the quality items below are what make removing it safe.

### 1.2 Checks on the 33-page sample

| Check | Result |
|---|---|
| HTTP status as Googlebot (desktop + smartphone UA) | 200 on all 33 (one transient TLS reset on `/shop/brand/focal/` succeeded on retry) |
| robots.txt for Googlebot | `User-agent: *` Allow `/`, Disallow `/admin/` and `/planner/` only; no Googlebot-specific rule; not blocked |
| Snippet directives | No `nosnippet`, `max-snippet`, `max-image-preview`, `data-nosnippet` anywhere in the sample. Default = snippet-eligible. Optional: add `max-image-preview:large` so product images can be used large in Discover/AIO cards |
| Meta robots, collections/brands (19 + `/shop/`) | none (indexable by default) |
| Meta robots, products | `noindex, follow` on 22/25; none on 3 dash cams |
| Canonical correctness | Self-referencing, shop host, correct trailing slash on all 33 + 11. Parameter URLs canonicalise to the clean URL (per AUDIT_REPORT #8). Shop homepage `/` canonicalises to `https://www.audiomotorsports.com/` (hub), so the shop host has no indexable homepage of its own |
| Canonical vs schema | Mismatch persists (SCHEMA_REPORT S1): JSON-LD URLs on www while canonical is the shop host |
| Sitemap coverage | 42 URLs; 3 products; no homepage (AUDIT_REPORT #1, #2) |
| Hub mirrors | `www/beats/shop/`, `www/alarm/shop/` return 200 self-canonical. `www/stereo/shop/` returned **404** with a 404 canonical (earlier report counted 112 `/stereo/shop/` URLs in the hub sitemap; the index path 404s, sub-pages not re-tested), so the hub sitemap may list URLs that do not resolve. Re-check these URLs |

## 2. Answer readiness

### 2.1 Product pages (sampled: Kicker 46CSC654, Viper 3108V, JBL Club A600, Momento IC6, etc.)

Structure is good: H1, spec chips, "What this is", a Specs table (5-8 rows), "Before you drive over" Q&A (fit, pickup, install), pickup address, related items. About 740-860 words of rendered text per page, of which roughly 85% is shared navigation, category/brand filter lists and boilerplate. Unique answer text per product is the 40-60 word "What this is" paragraph.

Gaps against what AIO and shopping answers quote:
- No fitment answers. The only fitment answer is "call with year, make and model". There are no vehicles named, e.g. "Fits most 2007-2018 Jeep Wrangler JK front doors with adapter X". Retrofit collection groups by vehicle make (Jeep, Ford, Chevrolet/GMC, Ram), which is a real fitment asset, but the product pages do not repeat it.
- Specs are thin and miss decision values: speaker sensitivity, frequency response, tweeter type, peak power, cutout size, grille included; amplifier channels, RMS at 4/2 ohm, fuse size, dimensions; head unit screen size, CarPlay wireless/wired, preouts voltage. Dash cams have 1 row of specs (camera count) only.
- Q&A block is identical on every product (same three questions, same text) and mixes two phone numbers ((310) 513-8800 call, (213) 429-1092 text). Not product-specific, so it cannot answer "does X fit Y".
- "What this is" is templated ("It replaces a factory door or deck speaker ... We stock it in Carson ...") and is the same sentence frame on every page.
- Price: shown on card and page; "Call to confirm" on about two thirds. A consistent "Price last verified <date>" line is absent.
- Freshness: no visible updated date on products; llms.txt carries "Prices verified September 2026", the pages do not.
- No author/experience signal on products (who tested/installed). The footer cites "Google 4.8 from 654. Yelp 4.7 from 777", which is useful social proof but is business-level, not product-level.

### 2.2 Collections and brand pages

All 19 sampled collection/brand pages: one H1, one-sentence intro ("Kicker, Focal, Hertz, and the speakers we actually install in Carson. About 90% on the shelf."), then the card grid. No H2 sections, no buying guide, no FAQ, no comparison table, no "how to choose" content. Brand pages likewise (JBL page ~1,000 words is nearly all card text). Queries such as "what size speakers fit my car" or "best amp for 12 inch sub" have nothing answer-first to cite. Notable: `/shop/brand/zz-2/` (8,030 words), `/shop/car-stereos/` (12,870) and `/shop/car-stereos/retrofit/` (11,769) are huge card dumps; they have H2s (retrofit has per-make groups) but no summarising answer passage at the top.

The homepage-derived FAQ (15 Q&A, hub page served on the shop host) is the strongest answer content, but it lives on the hub-canonical page, so it does not support shop collection URLs.

### 2.3 FAQ copy vs schema parity

- Product and collection pages: visible Q&A exists on products (3 questions), but there is **no FAQPage JSON-LD** on products. Parity is therefore "no schema, visible text only". This is fine for Google (FAQ rich results are limited to authoritative sites and are not needed for AIO). Do not add FAQ schema for rich results; if added, it must match the visible text word for word.
- Collections: neither visible FAQ nor schema.
- Homepage: FAQPage with 15 questions; per SCHEMA_REPORT S8 answers match visible text (not re-verified word-for-word here).
- Recommendation: put the visible, product-specific Q&A on the pages first. Schema is optional and secondary.

### 2.4 Passage template to add (answer-first, 40-80 words, under question-style H2)

Collections: H2 "How do I choose <category> for my car?" followed by 50-70 words stating the decision rule, then a comparison table (size/type/RMS/price band/best for) generated from catalogue data. Product: H2 "Will the <model> fit my <vehicle>?" with a 40-70 word answer naming the vehicles confirmed in the shop plus the "call to confirm" line.

## 3. Schema completeness for Merchant / AIO shopping surfaces

(Builds on SCHEMA_REPORT S1-S10; only deltas and Merchant-specific points.)

| Property | Status (priced product, e.g. Kicker 46CSC654) | Needed |
|---|---|---|
| Product.name, description, image, brand | Present; image on www host (S1) | Use shop-host absolute image URLs; add 2-4 more images (installed, box, rear) |
| sku | Internal slug (`kicker-46csc654`) | Keep as sku, add `mpn` = manufacturer part (46CSC654) and `gtin` where the manufacturer publishes one |
| Offer.price/priceCurrency | Present on priced products; absent on JVC KW-M56BT, Kicker CVR12-2, CVR12-4, Kicker 43DCWR122 and all 3 dash cams | Only add where a real price exists; do not fake |
| Offer.url | www host | Must equal the shop canonical (S1) |
| Offer.availability | `InStoreOnly` | Good fit for pickup-only. Verify against Merchant Center local inventory policy; consider `LimitedAvailability` where "call to confirm" |
| Offer.priceValidUntil | Missing | Add a real date aligned with the "prices verified" cadence |
| Offer.itemCondition | On Product, not on Offer | Move or duplicate on Offer |
| hasMerchantReturnPolicy / shippingDetails | Missing | Add `MerchantReturnPolicy` text-matching the visible Terms; for no shipping, state pickup-only in-page and in the Merchant Center settings (do not invent a shipping rate) |
| Offer.seller | `Organization` with name only | Link by `@id` to `https://www.audiomotorsports.com/#business` (S5) |
| aggregateRating / review | None | Correct: there are no product reviews. Do not use the business Google/Yelp rating on Product. If real on-site reviews are collected, add `Review` with the visible text |
| Product `@id`, `isVariantOf`/`ProductGroup` | None; the retrofit radios repeat across vehicle variants (e.g. Stinger HORIZON10 JK vs JL) | Optional: use `additionalProperty` for vehicle fitment or `ProductGroup` where variants are the same device |
| BreadcrumbList | Valid, on www host (S1). Visible breadcrumb matches | Switch to shop host |
| CollectionPage | `numberOfItems` but no items | Add `mainEntity` `ItemList` with real product URLs (S7); keep names matching cards |
| Organization/LocalBusiness | Only on hub homepage (`AutoRepair`, `#business`) | Reference by `@id` from shop pages; consider `["AutoPartsStore","AutoRepair"]` types (S6); add a `ContactPoint` for the text line (213) 429-1092 so the second phone number is machine-declared |
| Merchant feed | No evidence of a feed or Merchant Center link (unverified) | Merchant Center free listings need either a crawlable indexable page (blocked now by noindex) or a feed. Pickup-only stores can use Local inventory ads / free local listings |

Because ~97% of product pages are noindex, every row above is secondary to 1.1.

## 4. Entity consistency with the hub

- Name: product footer says "Audio MotorSports Inc"; schema says "Audio MotorSports"; llms.txt says "Audio MotorSports Inc (AMS)". Consistent enough; choose one legal/display pair and use it in the Organization `legalName`/`name`.
- NAP: address, hours and (310) 513-8800 match across shop pages, hub schema and llms.txt. A second number, (213) 429-1092, appears in product FAQ text and llms.txt as the "text" line but is not in the schema. Declare it as a ContactPoint (contactType e.g. "customer support", with a note that it receives texts) to avoid an apparent NAP conflict.
- Hub link: shop pages link to the hub in the nav and footer and to Maps/Instagram/YouTube. Schema URL host mismatch (www vs shop) remains the principal entity problem (S1/S5). The shop host has no page that describes the shop as an entity (its homepage is the hub homepage). Improvement: give `https://shop.audiomotorsports.com/` a shop-landing experience (see P5) without removing anything.
- Brand names: sister-brand footer lists LA Car Beats, LA Car Tint, LA Car Alarm, AMS Pods, Tesla Tint LA as "One bay, six desks", which states the relationship in human text. Add the same relationship to schema as `subOrganization`/`brand` or `sameAs` pointing to those sites so engines resolve them to one business. (Sister domains were blocked by the proxy; unverified from their side.)
- Differentiation of mirrors (no canonical or noindex): `www/beats/shop/` and `www/alarm/shop/` are self-canonical pages on the hub for the same catalog. Keep them. Give each a distinct angle (LA Car Beats: audio-system build guides and installed-system pricing; LA Car Alarm: security bundles, Viper/Compustar comparison) and link each to the shop-host product for specs and stock.

## 5. llms.txt quality and AI-crawler access

### 5.1 AI-crawler access matrix

robots.txt has only `User-agent: *` (Allow `/`; Disallow `/admin/`, `/planner/`). No named group exists for any bot below, so each follows the `*` group. HTTP status was tested for four URLs per UA (a collection, a product, `/llms.txt`, `/robots.txt`); all were 200 for every UA.

| Bot | Role | robots.txt rule | HTTP (collection / product / llms.txt / robots.txt) | Notes |
|---|---|---|---|---|
| Googlebot (desktop) | Search + AIO | `*` allow | 200 / 200 / 200 / 200 | Access fine; product pages carry noindex (section 1.1) |
| Googlebot-Smartphone | Mobile-first indexing | `*` allow | 200 / 200 / 200 / 200 | same |
| Google-Extended | Gemini training/grounding opt-out token only | `*` allow | 200 / 200 / 200 / 200 | Does not control AIO or Search |
| Bingbot | Bing + Copilot index | `*` allow | 200 / 200 / 200 / 200 | noindex also applies |
| OAI-SearchBot | ChatGPT search | `*` allow | 200 / 200 / 200 / 200 | |
| ChatGPT-User | user-triggered fetch | `*` allow | 200 / 200 / 200 / 200 | |
| GPTBot | OpenAI training | `*` allow | 200 / 200 / 200 / 200 | policy choice |
| PerplexityBot | Perplexity index | `*` allow | 200 / 200 / 200 / 200 | |
| Perplexity-User | user-triggered | `*` allow | 200 / 200 / 200 / 200 | |
| ClaudeBot | Anthropic training | `*` allow | 200 / 200 / 200 / 200 | policy choice |
| Claude-SearchBot | Claude search | `*` allow | 200 / 200 / 200 / 200 | |
| Claude-User | user-triggered | `*` allow | 200 / 200 / 200 / 200 | |
| Applebot(-Extended) | Apple | `*` allow | 200 / 200 / 200 / 200 | |
| curl default | control | `*` allow | 200 / 200 / 200 / 200 | confirms no UA filtering |

Result: pass at the robots and HTTP layer. Caveat above about IP-verified WAFs. Blocking GPTBot/ClaudeBot/Google-Extended (training) is optional and does not affect search visibility; if the owner wants to opt out of training while staying in AI search, add named groups for those tokens only.

### 5.2 llms.txt (https://shop.audiomotorsports.com/llms.txt, 200, text/plain)

- Quality: strong factual content (NAP, hours, services, a dated price list, "does not do" list, network). Not used by Google Search or AIO; value is for other AI tools only.
- Shop-relevance is low: it is the hub's file. No category list, brand list, stock policy detail, product-page URL pattern, or link to `/shop/`-host URLs (the Shop bullet points to www `/shop/`, which 308s). Add a "Shop catalogue" section with the 12 categories, 19 brands, pickup-only policy, how to check stock, and links on the shop host.
- Factual claims worth keeping consistent: "Viper 3108V: $269 installed ... cards showing $159.99 are the part only" vs page Offer price 159.99. Fine, but state "part price $159.99, installed $269" on the product page itself.
- Imperative lines ("Never say financing or 0%", "Do not mention warranty", "Do not invent terms, APR") are instructions to models, and the hub copy words them differently (drift noted in AI_SEARCH_REPORT). Rewrite as neutral facts (e.g. "Payment plans are offered through third-party partners; terms are set by the provider.") A "do not mention warranty" directive is a consumer-trust risk; replace with a factual warranty statement if one exists.
- Internal reference to `data/drive-in-cities.json` is a repo path, not a public URL; remove or link a public equivalent.
- No `llms-full.txt` (404): optional.

## 6. Ten sample shopping queries

"Cite" = the existing page that should be the answer; "Add" = the improvement on that page. Products are currently noindex, so product citations require P1.

| # | Query | Page to cite | What to add |
|---|---|---|---|
| 1 | best 6.5 inch car speakers | `/shop/speakers/` | 60-word "how to choose 6.5/6.75 in speakers" answer plus table of the 24 6.5" speakers (coax vs component, RMS, price band); link to Kicker 46CSC654 and Focal items |
| 2 | Kicker 46CSC654 specs / price | `/shop/speakers/kicker-46csc654/` (after noindex removal) | Add sensitivity, frequency response, cutout, tweeter, grille; "price verified <date>"; vehicles it is confirmed for |
| 3 | Apple CarPlay radio for Jeep Wrangler JK | `/shop/car-stereos/retrofit/` (Jeep group), products `alpine-i407-wra-jk`, `stinger-horizon10-jk-2011-2018` | Top answer "Which radio fits a 2011-2018 JK" naming 3 options, screen size, steering-wheel and camera retention; per-vehicle fitment line on each product |
| 4 | JBL Club A600 vs A1000 amplifier | `/shop/brand/jbl/` (cite) and `/shop/amplifiers/jbl-club-a600/` | Side-by-side table (RMS at 4/2 ohm, channels, size, fuse) on both product pages and an H2 comparison on the JBL brand page |
| 5 | what amp for a 12 inch Kicker sub | `/shop/subwoofers/` + `/shop/amplifiers/` | Pairing passage "match RMS to sub rating" with example pairings from stock (e.g. Kicker CVR12 with a matching Kicker amp), linking each other |
| 6 | Viper 3108V alarm price installed | `/shop/alarms-remote-start/viper-3108v/` | Show both prices visibly: "$159.99 part, $269 installed at Carson"; Offer plus a second installed-service Offer; range, 1-way spec |
| 7 | car stereo installation Carson CA (shopping intent) | `/shop/car-stereos/` | Answer "Can I buy and install same day?" (from existing copy: 90% on shelf, bay open before 4), install quote steps, link to hub installation service page |
| 8 | dash cam hardwire kit installed (Momento / Thinkware) | `/shop/dash-cameras/` and `/shop/dash-cameras/momento-momento-ic6/` (indexable now) | Add specs (resolution, storage, GPS, parking mode), hardwire vs socket explainer, price or price range when known; compare the 4 cams in a table |
| 9 | Kenwood Excelon head unit | `/shop/brand/kenwood-excelon/` | Short brand intro (what Excelon is, who it fits), table of the 2 units with key specs; link to Kenwood brand page |
| 10 | dash kit and wiring harness for my car | `/shop/installation-parts/dash-kits-harnesses/` and `/shop/installation-parts/` | "How to find the right dash kit" 60-word answer, vehicle-make list, PAC/Metra/iDatalink compatibility notes; unique intro per sub-collection |

## 7. Superseded recommendations (conflicts with RULES.md)

| Earlier item | Where | Why superseded | Replacement |
|---|---|---|---|
| "canonical or noindex the mirrors" (priority row 3; Finding #3) | AUDIT_REPORT.md | RULES.md forbids noindex and canonical-to-drop of live pages | Differentiate mirror pages (distinct angle, internal links to shop-host product pages); keep all pages indexable |
| "Resolve the duplicate-catalog ambiguity ... (canonical or noindex)" (Rec 1) | AI_SEARCH_REPORT.md | same | Differentiate; fix entity linking in schema (`sameAs`/`subOrganization`) |
| "Drop redirecting URLs from the hub sitemap" (row 3) | AUDIT_REPORT.md | Dropping sitemap URLs is acceptable only for URLs that redirect; confirm none is a live indexable page. Retain if any returns 200 | Replace each redirecting `/shop/...` URL entry with its final shop-host URL rather than dropping |
| "301 / to /shop/" (priority row 6) | AUDIT_REPORT.md | Redirecting a page away conflicts with RULES.md | Keep the hub-canonical homepage; add a shop landing section/page on the shop host and a self-canonical there |
| "Decide canonical host per product; canonical ... the mirrors" | AUDIT_REPORT.md | Canonical to drop a page from search | Differentiation as above |
| S2 "accept no commerce rich results for those SKUs" / #4 | SCHEMA_REPORT / AUDIT_REPORT | Compatible with RULES.md, but incomplete: product pages are noindex, so no rich results are possible regardless of price | Treat noindex removal (P1) as the prerequisite |

## 8. Prioritized list

| # | Page | Problem | Report | Impact | Effort | Exact next step |
|---|---|---|---|---|---|---|
| 1 | Product pages, all categories (e.g. `/shop/speakers/kicker-46csc654/`) | `noindex, follow` on ~282/285 products; not eligible for AIO, shopping or Merchant listings | AIO_REPORT s1.1 | google, ai | medium | Remove the robots meta from the product template in stages: first the ~100 products with a real price and the richest specs (speakers, amps, subs, enclosures, alarms), add them to the sitemap with real `lastmod`, request indexing for a sample, then the rest as each gets unique content |
| 2 | All product pages | Schema URLs/images on www host; no `mpn`, `priceValidUntil`, return policy, Offer `itemCondition`; seller not linked to `#business` | SCHEMA_REPORT, AIO_REPORT s3 | google | quick | In the JSON-LD generator use the shop origin for url/item/image/Offer.url, add `mpn`, `priceValidUntil`, `MerchantReturnPolicy`, seller `@id` |
| 3 | `/shop/speakers/`, `/shop/amplifiers/`, `/shop/subwoofers/`, `/shop/enclosures/`, `/shop/car-stereos/`, `/shop/alarms-remote-start/` | One-line intro, no answer passage, no comparison table | AIO_REPORT s2.2 | google, ai | medium | Add an H2 buying-guide answer (40-80 words), a spec comparison table generated from catalogue data, and 4 Q&A, each matching visible text |
| 4 | Top 50 products by traffic (start: Kicker 46CSC654, JBL Club A600/A1000, Viper 3108V, Stinger HORIZON10) | Templated "What this is"; thin specs; same FAQ on all | AIO_REPORT s2.1 | google, ai | project | Per product add 5-8 more spec rows, a confirmed-vehicles line, "what's in the box", install note, and one product-specific Q&A |
| 5 | `https://shop.audiomotorsports.com/` | Hub page with www canonical; no shop entity page; title/H1 mismatch | AUDIT_REPORT #2, AIO_REPORT s4 | google, ai | medium | Serve a shop-landing page on the shop host (self-canonical, in sitemap) describing the shop, pickup-only policy, categories, with Organization schema linked to `#business`. Do not redirect or remove the hub page |
| 6 | `/shop/car-stereos/retrofit/`, `/shop/car-stereos/`, `/shop/brand/zz-2/` | 8,000-12,800-word card dumps with no summarising answer | AIO_REPORT s2.2 | google, ai | medium | Put a 60-word "how to choose" answer and a jump-link list of makes at top; keep all cards |
| 7 | `/shop/dash-cameras/` and 3 Momento products (indexable now) | No price, 1 spec row, no Offer | SCHEMA_REPORT S2 | google | quick | Add resolution, storage, GPS, parking mode, price or a price range; Offer when price is real |
| 8 | `/llms.txt` | Hub copy, imperative AI directives, repo path, no catalogue section | AIO_REPORT s5.2 | ai | quick | Add a shop-catalogue section with shop-host links; reword directives as facts; sync with the hub copy |
| 9 | Business entity (all shop pages) | Text line (213) 429-1092 not in schema; relationship to sister brands only in prose | AIO_REPORT s4 | google, ai | quick | Add `ContactPoint` and `subOrganization`/`sameAs` for LA Car Beats/Tint/Alarm, AMS Pods, Tesla Tint LA to the `#business` node |
| 10 | `/shop/speakers/` (and other collections) | `CollectionPage` has no `ItemList` | SCHEMA_REPORT S7 | google | quick | Add `mainEntity: ItemList` with product URLs and positions |
| 11 | `www/beats/shop/`, `www/alarm/shop/`, hub `/stereo/shop/` URLs | Mirrors of the shop catalog; `/stereo/shop/` index returned 404 while listed in hub sitemap | AUDIT_REPORT #3, AIO_REPORT s1.2 | google, ai | medium | Re-check the hub sitemap entries; give each mirror distinct angle copy and link to the shop-host product for specs and stock |
| 12 | All pages | No `max-image-preview:large` | AIO_REPORT s1.2 | google | quick | Add `<meta name="robots" content="max-image-preview:large">` to indexable templates (leave existing noindex untouched until P1) |
| 13 | Product pages | No visible updated/price-verified date | AIO_REPORT s2.1 | google, ai | quick | Add "Price and stock verified <date>" under the price, sourced from the same date as llms.txt |
