# Schema Report: audiomotorsports.com

Date 2026-10-04. Source: JSON-LD parsed from all 1,057 crawled 200-OK pages. 1,054 pages have JSON-LD; 0 blocks failed to parse. Not run: Google Rich Results Test (unreachable); validity below is structural/JSON-parse plus manual review against schema.org and Google guidelines.

## Missing schema
Pages with no JSON-LD: `/services/`, `/alarm/book/`, `/beats/book/`.

## Types in use (page counts, approximate)
- AutoRepair + FAQPage + BreadcrumbList + AggregateRating + GeoCoordinates: ~700 city, service and brand pages.
- AutoPartsStore + Organization (LA Car Stereo mount): 128 pages (112 are product pages).
- CollectionPage + WebSite (shop/collection pages): 47. BlogPosting: ~11. VideoObject: ~160 pages. Service + Offer: ~100 pages. Person (Zack, Nick as employees). AboutPage, Review/Rating on `/reviews/`.

## Strengths
- Homepage declares `AutoRepair` with a stable `@id` (`https://www.audiomotorsports.com/#business`), full PostalAddress, openingHoursSpecification, telephone, logo, image.
- City pages add `geo` (33.8270, -118.2650), `areaServed` City, `sameAs` (YouTube, Instagram, Facebook, TikTok, Yelp, Google Maps ftid, and the five sister domains) and `subOrganization` links. This is a good entity graph.
- FAQPage content is specific and consistent with page text.

## Issues
1. **Homepage schema is thinner than city pages:** no `geo`, `sameAs`, `areaServed`, `aggregateRating`, `priceRange`, `hasMap`, `description`, or `subOrganization`. Homepage is the page that should carry the canonical entity. Fix: copy the city-page business node to `/`. (quick)
2. **Mounted brand sites assert separate businesses on the hub's own host:** `/tint/#business` ("LA Car Tint"), `/beats/#business`, `/stereo/#business` ("LA Car Stereo", type AutoPartsStore, `url` without trailing slash) all share the same address and phone but are different `@id`s; hub pages instead reference `https://www.lacartint.com/#business`. Result: two `@id`s per brand. Fix: one `@id` per brand, on its canonical host. (medium)
3. **Product pages (112 under /stereo/shop/) have no Product/Offer markup**, only the AutoPartsStore business node. Prices are visible in copy, so Product + Offer (price, priceCurrency, availability, brand, sku) is eligible for merchant listings. Fix: add Product JSON-LD or move to the shop host. (project)
4. **Self-serving `aggregateRating` on the business node** (4.8 / 654, 620 blocks, same value everywhere, sourced from Google). Google does not show review stars for LocalBusiness/Organization self-markup, so no rich-result benefit, and a stale count across 620 pages is a maintenance risk. Fix: keep only where reviews are shown on the page, and mark sources; or remove. (quick)
5. **Mixed `@type` forms:** some pages use `["AutomotiveBusiness","AutoRepair"]`, others `AutoRepair` only, the stereo mount `AutoPartsStore`. Pick one primary type for the entity (AutoRepair is valid and consistent with the car audio/tint/alarm services; `LocalBusiness` subtype alternatives such as `AutoPartsStore` or `AutomotiveBusiness` are acceptable but should not alternate per URL). (medium)
6. **FAQPage:** Google restricts FAQ rich results to well-known government/health sites since 2023, so no rich result. Markup is harmless and useful for AI parsing; ensure the answers also appear visibly. Several answers are very long, repeat the same address sentence, and reuse promotional text. (low)
7. **Email in schema** is a Gmail address on every page. (low)
8. `latitude`/`longitude` are strings ("33.8270"); numbers are preferred. 4-decimal precision is fine. (low)
9. `foundingDate` appears only on stereo mount (2003); add to the main node. `priceRange` absent everywhere. (quick)
10. `WebSite` node (with SearchAction if site search exists) is only on collection pages, not the homepage. (quick)

## Suggested homepage node (illustrative)
```json
{"@context":"https://schema.org","@type":"AutoRepair","@id":"https://www.audiomotorsports.com/#business",
 "name":"Audio MotorSports","url":"https://www.audiomotorsports.com/","telephone":"+13105138800",
 "foundingDate":"2003","priceRange":"$$","geo":{"@type":"GeoCoordinates","latitude":33.8270,"longitude":-118.2650},
 "sameAs":["<same list as city pages>"],"areaServed":[{"@type":"City","name":"Carson"},{"@type":"City","name":"Long Beach"},{"@type":"City","name":"Torrance"}]}
```
Verify the geo coordinates against the real pin before use (the value above is copied from the site, not independently verified).
