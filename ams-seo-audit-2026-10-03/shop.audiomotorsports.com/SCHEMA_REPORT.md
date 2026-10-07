# Schema Report: shop.audiomotorsports.com

Audited 2026-10-04. Read-only. Source: JSON-LD parsed from 61 fetched URLs (42 sitemap pages, 3 parameter variants, checkout, 14 sampled product pages) plus the homepage. Rich Results Test and Merchant Center were not run (not reachable / not available), so eligibility statements are based on schema.org and Google's documented requirements as I understand them, not a live test.

## Inventory

| Page type | Count fetched | JSON-LD blocks |
|---|---|---|
| Collection / brand / subcategory | 40 | BreadcrumbList + CollectionPage |
| `/shop/` and `/shop/?sort=price` | 2 | CollectionPage only (no breadcrumb) |
| Product detail | 17 (14 sampled + 3 sitemap dash-cams) | BreadcrumbList + Product |
| Homepage `/` | 1 | AutoRepair + WebSite + FAQPage (15 questions) |
| `/checkout/` | 1 | none (noindex) |

Parse result: all JSON-LD blocks parsed as valid JSON. No block failed. (Note: a naive `<script type="application/ld+json">` regex misses the breadcrumb blocks because they carry an extra `data-ams-generated="breadcrumb"` attribute; the markup is fine.)

## Findings

### S1. All schema URLs use www, but pages are canonical on the shop host (High)
Example, `https://shop.audiomotorsports.com/shop/speakers/kicker-46csc654/`:
- page canonical and `og:url`: `https://shop.audiomotorsports.com/shop/speakers/kicker-46csc654/`
- `Product.url`, `Offer.url`, each BreadcrumbList `item`, and CollectionPage `url`: `https://www.audiomotorsports.com/shop/...`
- `Product.image`: `https://www.audiomotorsports.com/assets/img/products/...`
- `https://www.audiomotorsports.com/shop/speakers/kicker-46csc654/` returns `308 -> shop host` (verified for this product, `/shop/`, and `/shop/brand/jbl/`).

Effect: structured data names a URL that redirects, contradicting the canonical. Google expects the Offer URL to match the landing page. Breadcrumb trails point to redirecting URLs, and the "Home" item is the www homepage while the visible site is the shop host.
Fix: generate Product/Offer/Breadcrumb/CollectionPage URLs from the same origin as the canonical.

### S2. Product has no `offers` on roughly two thirds of products (Medium)
4 of 14 sampled products have no Offer (JVC KW-M56BT, Kicker 43DCWR122, Kicker CVR12-2, Kicker CVR12-4); the 3 Momento dash cams show "Call to confirm" with no price. Collection counts of priced cards: car-stereos 18/146, retrofit 0/125, dash cameras 0/7, amplifiers 9/20, alarms 5/15. A Product without price/offers is valid schema but not eligible for merchant listing or price-based product snippets. Do not add a fake price; either publish real prices or accept no commerce rich results for those SKUs.

### S3. Offer is thin for merchant eligibility (Medium)
On priced products (Kicker 46CSC654, Viper 3108V) the Offer has `price`, `priceCurrency`, `availability: InStoreOnly`, `seller`, `itemCondition: NewCondition` on the Product, and a good `availableAtOrFrom` Place with address and phone. Missing: `priceValidUntil`, `hasMerchantReturnPolicy`, `shippingDetails` (for in-store-only a pickup-only statement is appropriate), `gtin`/`mpn` (the `sku` is an internal slug like `kicker-46csc654`, not a manufacturer part number), `aggregateRating`/`review` (none exist on page; do not invent them). `price` is a string ("99.99"), which is accepted. Whether Google treats `InStoreOnly` without a shipping policy as eligible for free listings was not tested.

### S4. Viper 3108V price conflicts with the site's own statements (Medium, trust)
The Offer says `price: 159.99` with `description: "Part only. Installed at this shop: $269."`. llms.txt says "Viper 3108V: $269 installed. Shop cards that show $159.99 are the part only." This is consistent, but a machine reading only `price` gets the part price; the installed price lives in free text. Acceptable if intentional; consider a second Offer or `priceSpecification` for the installed service.

### S5. Shop pages have no Organization/LocalBusiness node of their own (Medium)
Only the homepage (the hub's) carries `AutoRepair` (`@id` `https://www.audiomotorsports.com/#business`, NAP, geo, hours, sameAs, OfferCatalog). Collection and product pages carry `seller: {Organization, name}` with no `@id` linking to that business node, and `CollectionPage.isPartOf` points to a WebSite on www. Add `"seller": {"@id": "https://www.audiomotorsports.com/#business"}` so entities connect.

### S6. Business type and details (Low)
`AutoRepair` is used for a store that sells car audio and also installs. Options: `AutoPartsStore` (sells parts) plus `AutoRepair`, or multiple `@type`. The node exposes `email: audiomotorsports@gmail.com` publicly (fine if intended). Fixed lat/long of 33.8270, -118.2650 were not checked against the address. Hours list Mon-Sat 09:30-18:00, matching the llms.txt text (consistent).

### S7. CollectionPage lacks ItemList (Low)
`/shop/speakers/` declares `numberOfItems: 33` but lists no items. Adding `mainEntity: ItemList` with product URLs is optional and helps AI/Google understand the set.

### S8. FAQPage on the homepage (Low, Google)
15 Q&A pairs. Google restricts FAQ rich results to authoritative government/health sites, so no rich-result benefit is expected; still useful as plain extractable Q&A for AI. Several answers are opinionated and long (for example the first about Amazon radios).

### S9. Breadcrumbs (Pass with the S1 caveat)
Position numbering 1..n, names match the visible trail (Home / Shop / Category / Product). Missing on `/shop/` and its sort variant (top-level, acceptable).

### S10. No Review/AggregateRating, no WebSite SearchAction (Info)
Nothing found; none should be added without real on-page reviews. Product pages do not display customer reviews.

## Sample Product JSON-LD as served (Viper 3108V, abbreviated)
`@type: Product`, `sku: viper-3108v`, `brand: Brand(Viper)`, `url`/`offers.url`: www host, `offers.availability: InStoreOnly`, `offers.price: 159.99`, `offers.availableAtOrFrom: Place(Audio MotorSports, Carson CA 90745, +1-310-513-8800)`, `image`: www host.

## Recommended fixes
1. Make every schema URL match the page canonical (S1).
2. Link `seller` and `isPartOf.publisher` to the `#business` `@id` (S5).
3. Add `priceValidUntil` and a return policy/pickup statement; add `mpn` (manufacturer model such as 46CSC654) where known (S3).
4. Decide per SKU whether to publish a price (S2).
