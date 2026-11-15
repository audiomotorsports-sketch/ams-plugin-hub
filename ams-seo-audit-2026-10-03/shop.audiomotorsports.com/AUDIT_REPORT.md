# SEO + GEO Audit: shop.audiomotorsports.com

Audited 2026-10-04 (UTC). Read-only. Nothing was modified anywhere.

## Method and limits (read first)

- Fetched with curl through the egress proxy. Fetches were intermittently flaky (TLS resets and timeouts) and were retried up to 4 times. All pages below were eventually fetched.
- Fetched: homepage, robots.txt, llms.txt, shop-sitemap.xml, all 42 sitemap URLs, 3 facet/parameter URLs, 14 product detail pages (sampled across 9 categories), the hub homepage / robots.txt / sitemap.xml / llms.txt on www.audiomotorsports.com, and a few hub `/stereo/`, `/beats/`, `/alarm/` shop pages.
- NOT verified: Core Web Vitals (PageSpeed API returned 429 quota exceeded; no lab run was done), the sister domains (lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com all returned 403 from the egress proxy), Search Console indexation, Merchant Center feed status, plain-HTTP to HTTPS redirect (the proxy returned 403 for `http://`), rendered/JS view (HTML is server-rendered; no browser render was run).
- Scores are my own estimates from fetched evidence, not tool output.
- `pages.csv` has url, title, H1, meta description for 61 URLs (42 sitemap URLs, 3 parameter variants, checkout, and 14 sampled product pages; the homepage is not a row because it is the hub page).

## Business context

Per the site's own pages: a single Carson, CA bay (22025 S Avalon Blvd Ste A) selling car audio and security parts for **in-store pickup only** ("We don't ship"), with installation. About 285 product detail pages are linked from the collections. Hosting: Vercel. The shop is a sub-host of the main site; it is the canonical home of the catalog (the www host 308-redirects `/shop/...` to it).

## Estimated scores

| Area | Score | Basis |
|---|---|---|
| Technical | 78/100 | Clean 200s, HTTPS and HSTS, 308 trailing-slash, self-canonicals, noindex on checkout, fast TTFB (0.15-0.45 s). Docked for the missing homepage and products in the sitemap, and the http 403 (unverified) |
| Content / on-page | 70/100 | Unique titles and H1s on collections; products have thin boilerplate descriptions and 17 identical meta descriptions |
| Schema | 55/100 | Valid JSON-LD, but every URL points at the wrong host, and many Products lack Offers (see SCHEMA_REPORT.md) |
| E-commerce | 55/100 | No product feed signals, sitemap omits all products, about two thirds of products show "Call to confirm" with no price |
| GEO / AI | 75/100 | Open crawler access, a good llms.txt, FAQ content. Docked for entity and URL fragmentation (see AI_SEARCH_REPORT.md) |

## Findings

### 1. Product pages are not in the sitemap (High, Google)
`shop-sitemap.xml` has 42 URLs, all dated lastmod 2026-09-24: `/shop/`, 12 category pages, 18 brand pages, 4 subcategory pages, and 3 dash-camera products. The 285 product detail pages linked from the collections (for example `/shop/speakers/kicker-46csc654/`) are in no sitemap. I extracted the product-card links from the 42 sitemap pages (285 unique) and compared them with the sitemap: none is listed. The only 3 product pages in the sitemap are Momento dash cams (e.g. `/shop/dash-cameras/momento-momento-ic6/`). Discovery relies on internal links only.

### 2. The shop homepage canonicalizes to the hub, and is missing from the sitemap (High, Google)
`https://shop.audiomotorsports.com/` returns the hub's homepage (title "Car Window Tint & Car Audio in Carson", H1 "Shop car stereo in Carson", FAQPage, AutoRepair schema) with `<link rel="canonical" href="https://www.audiomotorsports.com/">`, `og:url` of www and a hub OG image. That is a consolidation signal and is acceptable on its own, but it means the shop host has no indexable homepage of its own and the sitemap's top entry is `/shop/`. Title/H1 also mismatch (title promises window tint, H1 and content are the shop).

### 3. A parallel catalog on www competes with the shop catalog (High, Google and AI)
The hub sitemap (`www.audiomotorsports.com/sitemap.xml`, 1,090 URLs) lists 148 shop-like URLs under `/stereo/shop/` (112), `/beats/shop/` (27), `/alarm/shop/` (7), plus `/amspods/shop/` and `/tint/shop/` (1 each). I fetched 4: all return 200 with self-referencing canonicals and different titles ("Amplifiers | LA Car Stereo", "Kicker Car Audio ... | LA Car Beats", "Compustar Remote Start & Security | LA Car Alarm"). They sell or describe the same brands and products as the shop host (for example Kicker, Focal, Compustar, Metra). Result: product and brand intent is split across two hosts with different brand names, which risks keyword cannibalization and duplicate-content clustering. Whether these are intentional mirrors of the sister domains is unverified (sister domains were blocked).

### 4. Hub sitemap lists 181 URLs that redirect (Medium, Google)
`www.audiomotorsports.com/sitemap.xml` includes 181 `https://www.audiomotorsports.com/shop/...` URLs. I confirmed `/shop/`, `/shop/brand/jbl/` and a product URL return 308 to the shop host. The rest are unverified but share the pattern. Sitemaps should list final 200 URLs only.

### 5. Structured data URLs point to www, not the canonical shop host (High, Google; detail in SCHEMA_REPORT.md)
On every page checked, `Product.url`, `Offer.url`, `image`, BreadcrumbList items and CollectionPage `url` use `https://www.audiomotorsports.com/shop/...`, which 308-redirects to the page being viewed. The page canonical and `og:url` use the shop host. This conflicts with the canonical, and Merchant/Product rich results expect the Offer URL to match the landing page.

### 6. Most products show no price and have no Offer (Medium, Google)
Priced cards in sampled collections: speakers 25/33, amplifiers 9/20, enclosures 9/15, subwoofers 10/16, car-stereos 18/146, retrofit radios 0/125, dash cameras 0/7, alarms 5/15. Where there is no price the page says "Call to confirm" and the Product JSON-LD has no `offers` (4 of the 14 sampled product pages lacked it: JVC KW-M56BT, Kicker 43DCWR122, Kicker CVR12-2, Kicker CVR12-4). Those products cannot qualify for price-based product rich results or merchant listings. This may be a deliberate business choice, but it limits Shopping visibility.

### 7. Duplicate meta descriptions and titles (Medium, Google)
- 17 of the 17 product pages fetched (14 sampled plus the 3 dash-cam products in the sitemap) share one identical 127-character meta description: "People ask for this. About 90% on the shelf in Carson. Call (310) 513-8800 ...".
- Product titles are just the model name plus "| Audio MotorSports" ("Kicker 46CSC654"); no product type, size or "Carson" qualifier.
- "Car Speakers in Our Carson Shop | Audio MotorSports" appears for the speakers page and its two parameter variants (same canonical, so benign).
- Product H1s are the model name only, and the on-page description is a short templated paragraph ending "We stock it in Carson for pickup and we fit it here ..." (word count not measured).

### 8. Parameter URLs are canonicalized but still crawlable (Low, Google)
`/shop/?sort=price`, `/shop/speakers/?brand=jbl` and `?page=2` all return 200 with identical HTML to the base page and a canonical to the clean URL. Facet links (`?size=4`, `?size=4x6`, ...) are rendered as plain `<a>` links in the sidebar. Canonicals contain it. Note `?page=2` returns the same 33 products as page 1 (no real pagination, no rel next/prev), so nothing is lost. robots.txt does not block parameters. Low crawl-budget risk at this catalog size.

### 9. Images and alt text (Low, Google)
Product and collection images have alt text and width/height attributes, are lazy-loaded below the fold with `fetchpriority="high"` on the first item, and use WebP `srcset` on cards. The exception: `/shop/` has 13 `alt=""` banner images (decorative, arguably fine) and `/shop/car-stereos/` has 4 images without alt. Product alt text is the model name only. Images are served from `www.audiomotorsports.com/assets/` while the page is on the shop host (cross-host, no issue for indexing but affects Offer image consistency).

### 10. Security and technical headers (Low)
Present: `strict-transport-security: max-age=31536000`, `x-content-type-options: nosniff`, `x-frame-options: SAMEORIGIN`, `referrer-policy: strict-origin-when-cross-origin`, `permissions-policy`. Missing: `Content-Security-Policy`; HSTS has no `includeSubDomains` or `preload`. `access-control-allow-origin: *` is set on HTML pages. Cache is `max-age=0, must-revalidate` with Vercel edge caching (x-vercel-cache: HIT), which is fine. `http://shop.audiomotorsports.com/shop/` returned 403 through the proxy; this is probably the proxy and not the site, so the http-to-https redirect is unverified.

### 11. Error handling (Pass)
Missing URLs (`/nonexistent-xyz/`, `/products.json`, `/cart/`, `/llms-full.txt`) return a real HTTP 404 with a branded not-found page ("Page not found | Audio MotorSports"). `/checkout/` returns 200 with `noindex, nofollow`. `/shop` 308s to `/shop/`; `/sitemap.xml` 301s to `/shop-sitemap.xml`.

### 12. Mobile and performance signals (partially verified)
Pass: `<meta name="viewport">`, responsive CSS, mobile hero image preload with `fetchpriority="high"`, self-hosted preloaded fonts, TTFB 0.15-0.45 s from the test location, HTML 6-20 KB compressed for most collections (car-stereos 19.8 KB, ZZ-2 brand 14 KB). Concerns: the car-stereos and retrofit collections render 146 and 125 cards in one DOM (roughly 65-72 KB of visible text each; DOM size not measured), which may hurt INP/LCP on mobile; a chat widget stylesheet (`ams-chat.css`) and GTM load on all pages. No lab or field CWV data was obtained (PageSpeed 429).

### 13. Internal linking and breadcrumbs (Pass with note)
Visible breadcrumbs (Home / Shop / Category / Product) and BreadcrumbList JSON-LD exist on 57 of the 61 fetched URLs. Collections link to products and cross-link to hub `/services/` pages. Note product-card links use root-relative URLs, so they stay on the shop host.

### 14. Robots.txt (Pass)
`User-agent: *`, `Allow: /`, `Disallow: /admin/`, `Disallow: /planner/`, `Sitemap: https://shop.audiomotorsports.com/shop-sitemap.xml`. No AI-bot-specific blocks.

## What is working

Server-rendered HTML (no JS needed to see products and prices), unique collection titles and H1s, self-canonical on every collection and product, noindex on checkout, valid JSON-LD with no parse errors on any of the 61 pages, good alt text, clean 404s, fast TTFB, and strong llms.txt.

## Priority list

| # | Page | Problem | Report | Impact | Effort | Next step |
|---|---|---|---|---|---|---|
| 1 | All product and collection pages | Schema URLs (Product, Offer, Breadcrumb, CollectionPage) use www host, which 308s to shop host; canonical is shop host | SCHEMA_REPORT | google | quick | In the template that builds JSON-LD, use the shop origin for url, item, Offer.url |
| 2 | shop-sitemap.xml | 285 product pages absent (only 3 Momento products) | AUDIT_REPORT | google | quick | Add all product URLs to the sitemap generator, resubmit in Search Console |
| 3 | www sitemap + /stereo/shop/, /beats/shop/, /alarm/shop/ | 148 parallel shop URLs with self-canonicals duplicate the shop catalog; 181 www /shop/ URLs in hub sitemap redirect | AUDIT_REPORT, AI_SEARCH_REPORT | both | medium | Decide canonical host per product; canonical or noindex the mirrors; drop redirecting URLs from the hub sitemap |
| 4 | Product pages without price (e.g. /shop/car-stereos/jvc-kw-m56bt/) | No Offer; retrofit 0/125 and car-stereos 18/146 priced | SCHEMA_REPORT | google | project | Publish real prices or accept no merchant rich results; never fake a price |
| 5 | All product pages | Identical meta description and name-only titles | AUDIT_REPORT | google | medium | Generate titles like "Brand Model - type, fits ... | Audio MotorSports Carson" and unique descriptions |
| 6 | https://shop.audiomotorsports.com/ | Homepage is the hub page with www canonical, not in sitemap; title/H1 mismatch | AUDIT_REPORT | google | quick | Make a shop landing page or 301 / to /shop/; align title with H1 |
| 7 | /llms.txt | Hub copy, drifts from hub version, has imperative directives to AI, no shop catalog detail | AI_SEARCH_REPORT | ai | quick | Write shop-specific llms.txt with factual statements; sync both copies |
| 8 | Product pages | Templated body text, little unique passage content | AI_SEARCH_REPORT | ai | project | Add fitment, what is in the box, install notes on top 50 SKUs |
| 9 | Product Offers | Missing priceValidUntil, return/pickup policy, mpn | SCHEMA_REPORT | google | medium | Add fields to the Offer template |
| 10 | Response headers | No CSP, HSTS without includeSubDomains | AUDIT_REPORT | google | quick | Add CSP and extend HSTS in Vercel headers config |
