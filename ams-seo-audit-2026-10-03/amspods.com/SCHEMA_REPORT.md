# Schema Report: amspods.com
Evidence: hub-mounted copy, proxy for the standalone domain, standalone not verified (www.amspods.com blocked by egress proxy; see LIMITATIONS.md). 130 URLs parsed from `https://www.audiomotorsports.com/amspods/`. All tags below are [mount-proxy].

## 1. Inventory
| Type | Pages / nodes | Notes |
|---|---|---|
| JSON-LD parse validity | 130 of 130 valid | no syntax errors |
| AutoRepair (business entity) | every page, `@id` `.../amspods/#business` | parentOrganization = Audio MotorSports `@id` `https://www.audiomotorsports.com/#business` |
| BreadcrumbList | 129 (not on home) | ok |
| FAQPage | 93 pages | 12 pages not visible, see 3.2 |
| Service | ~85 pages (services, city, model, catalog) | Offer nodes unpriced |
| Offer | 385 nodes | 0 with price, priceCurrency or availability |
| Product / ProductGroup | 0 | gap |
| AggregateRating | 62 pages | always 4.8 / 654 |
| Review | 10 nodes | Person authors |
| VideoObject | 15 pages | uploadDate 2026-09-25, duration, thumbnail, contentUrl |
| BlogPosting | 5 (4 posts + index context) | author/publisher = Organization; datePublished Aug 2026; no dateModified |
| WebSite | home, shop, a few others | no SearchAction (fine) |
| CollectionPage | /shop/ | no ItemList of products |
| ItemList | catalog pages | items point to hertz-audio.com etc. |

## 2. Validation against Google rich-result eligibility
- **FAQPage:** since 2023 Google shows FAQ rich results only for well-known government/health sites, so no Google rich result is expected; value is Bing/AI extraction and entity clarity. Policy still requires marked-up Q&As to be visible. 12 pages violate this (3.2).
- **AggregateRating on AutoRepair/LocalBusiness:** Google does not show self-serving review rich results for the business's own entity; the value is only consistency. Keep, but scope it (3.3).
- **Product snippets / merchant listings:** not eligible today (no Product).
- **VideoObject:** valid, eligible for video rich results if the video is indexable on the page.
- **Breadcrumb:** valid.

## 3. Findings
### 3.1 No Product/Offer for the AMS pod (priority 1)
The offer ("AMS pods from $649 a pair, chrome or gloss", made to order about three weeks, crash-bar bracket and screws included, ships nationwide per the shop page) exists in copy only. Offers inside Service/OfferCatalog list names like "Road Glide" and "Hertz Neo speakers" with no price.
Proposed JSON-LD (fill values only from the shop; confirm before publishing). Place on `/services/ams-pods/`, `/shop/` (one per variant) and `/build-your-own/`:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://www.amspods.com/shop/ams-chrome-pod-pair/#product",
  "name": "AMS Chrome Speaker Pod Pair for Harley-Davidson Baggers",
  "description": "Chrome crash-bar speaker pods built in-house in Carson, CA since 2003. Sold as a pair, built to order in about three weeks. Crash-bar bracket and screws included. Hertz Neo speakers recommended.",
  "brand": {"@type": "Brand", "name": "AMS Pods"},
  "manufacturer": {"@id": "https://www.amspods.com/#business"},
  "color": "Chrome",
  "category": "Motorcycle speaker pods",
  "isRelatedTo": [{"@type": "Product", "name": "Hertz Neo bagger speakers"}],
  "image": ["https://www.amspods.com/<real pod photo>.jpg"],
  "audience": {"@type": "Audience", "audienceType": "Harley-Davidson Road Glide, Street Glide, Road King (and Softail if confirmed) owners"},
  "offers": {
    "@type": "Offer",
    "priceSpecification": {"@type": "UnitPriceSpecification", "priceType": "https://schema.org/MinimumAdvertisedPrice", "price": "649.00", "priceCurrency": "USD", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitText": "pair"}},
    "price": "649.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/PreOrder",
    "itemCondition": "https://schema.org/NewCondition",
    "url": "https://www.amspods.com/build-your-own/",
    "seller": {"@id": "https://www.amspods.com/#business"},
    "shippingDetails": {"@type": "OfferShippingDetails", "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"}, "deliveryTime": {"@type": "ShippingDeliveryTime", "handlingTime": {"@type": "QuantitativeValue", "minValue": 15, "maxValue": 21, "unitCode": "DAY"}}}
  }
}
```
Notes: "starting at" prices should be shown in the visible text exactly as marked up; `hasMerchantReturnPolicy` only if the shop has a written policy; do not invent SKUs or GTINs; do not add `aggregateRating` to the Product unless real product-level reviews are visible. A gloss variant is the same with `"color": "Gloss black"`.

### 3.2 FAQPage not visible (12 pages)
Questions in schema but not found in page text: `/services/ams-pods/` (4 Q), `/services/road-glide-bagger-audio/` (4), `/services/street-glide-bagger-audio/` (4), `/services/road-king-bagger-audio/` (4), `/services/bagger-builds/` (2), `/blog/` (10), `/blog/ams-pods-since-2003/` (10), `/blog/bagger-audio-speakers-amp-or-pods-first/` (10), `/blog/hertz-bagger-ships-nationwide/` (10), `/blog/road-glide-street-glide-road-king/` (10), `/es/` (9, schema in English; page Spanish), `/es/faq/` (10, schema in English; page Spanish).
Fix: publish each Q and answer in a visible FAQ section on the same page (use `<details>` or open headings), and for es pages translate the schema Q/A to match the visible Spanish. Do not delete the markup; make the page match it. Blog posts should show only questions relevant to that post, not the same generic 10.
Parity is good on the other 81 FAQ pages (city pages have 6-8 visible `<details>`; home and `/faq/` match).

### 3.3 Ratings and reviews
Identical `AggregateRating 4.8 / 654` is on the business entity of 62 pages (city pages, home, es) while city pages show two excerpt reviews and say "that is the schema aggregate only". Google's guidance excludes self-serving ratings; mismatched counts are the risk. Fix: show "4.8 from 654 Google reviews" with a link to the Google Business Profile as visible text wherever the markup appears (the copy-wording should be rewritten as customer copy), keep `Review` nodes only for reviews visible on that page, and move the richer review markup to `/reviews/` and the home page.

### 3.4 Entity modelling
- `@type: AutoRepair` for a manufacturer/installer of motorcycle audio is broad; add `additionalType` (e.g. a Wikidata/GS1 product-category URL) or `Organization` + `brand` for AMS Pods, keep AutoRepair for the shop. The same phone/address/`@id` structure is reused on every page: good.
- Business `name` is "AMS Pods" with `alternateName` "Audio MotorSports" and the same address, phone and gmail address as the hub entity; the child `@id` and `parentOrganization` link is correct, keep it. Use `https://www.amspods.com/#business` as `@id`/`url` on the standalone domain (verify; the mount uses audiomotorsports.com URLs).
- `sameAs` is strong (GBP maps URL, Yelp, YouTube, Instagram, Facebook, TikTok, sister sites). Add Richard as `founder`/`Person` with sameAs.
- `areaServed` lists cities plus a 40 km GeoCircle on home: fine; city pages should use that city as `areaServed` on their own Service, which they do.
- Blog: change `author` from Organization to Person (Richard or Nick) and add `dateModified`, `image`, `mainEntityOfPage`.
- `/shop/` `CollectionPage`: add `ItemList` of the two pod products (with URLs) once product sections exist.
- `/es/*`: set `inLanguage: es` and translate `name`/`description`.

### 3.5 Offer nodes with no price (385)
Offers inside Service/OfferCatalog have only `itemOffered`. They add noise and fail merchant/price checks. Either add `priceSpecification` where a real price exists ($649 pod pair; published locked specials per llms.txt) or remove nothing and convert unpriced items to `itemListElement` of `Service` entries without `Offer` wrappers (content stays, markup becomes valid). Do not add made-up prices.

## 4. Recommended schema map (additions only)
| Page | Add |
|---|---|
| Home | Product x2 (or ItemList of products), Person (Richard), Review visible-only, keep AutoRepair/FAQ/Video/WebSite |
| /services/ams-pods/ | Product x2, visible FAQ, HowTo-style "how a pod install works" (only if steps are visible) |
| /shop/ | ItemList of products, Product for pod pair variants |
| Model pages (Road Glide/Street Glide/Road King) | Service + `isRelatedTo` Product, visible FAQ, fitment table in HTML (tables are citable), `Vehicle`-style text only in HTML (no schema.org type fits fitment reliably) |
| City pages | per-city FAQ (visible + schema), keep Service/AutoRepair/Breadcrumb |
| Blog | BlogPosting with Person author, dateModified |
| Spanish | translated schema, `inLanguage` |
| Catalog | Product nodes for items AMS actually sells/installs with price only if public |
