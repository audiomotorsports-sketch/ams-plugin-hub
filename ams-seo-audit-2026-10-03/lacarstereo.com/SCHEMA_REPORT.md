# Schema Report: lacarstereo.com

Date: 2026-10-04. Method: extracted every `application/ld+json` block from the 127 sitemap URLs (raw HTML via curl) and parsed it as JSON. Google Rich Results Test and Schema.org validator were not run (not reachable); validity below means "parses as JSON, uses real schema.org types and properties", otherwise unverified.

## Inventory

| Pages | Blocks present |
|---|---|
| 119 pages (home, shop categories, product pages, packages hub, FAQ, about, etc.) | `AutoPartsStore` only |
| 7 install pages (/install/carplay, stereo, subwoofer, amplifier, speakers, dsp, luxury) | `AutoPartsStore` + `Service` + `BreadcrumbList` |
| /locations/ | `AutoPartsStore` + `LocalBusiness` + `BreadcrumbList` |

All blocks parsed as valid JSON; no deprecated types found. Spot-check of /packages/2009-2014-ford-f-150/ shows `AutoPartsStore`, `Service`, `BreadcrumbList`.

## Sitewide business entity (every page)
`@type AutoPartsStore`, `@id https://www.lacarstereo.com/#business`, name "LA Car Stereo", legalName "Audio MotorSports Inc", telephone "(310) 513-8800", foundingDate 2003, full PostalAddress (22025 S Avalon Blvd Ste A, Carson, CA 90745, US), openingHoursSpecification Mon to Sat 09:30 to 18:00, areaServed = 10 cities (Carson, Long Beach, Torrance, Gardena, Compton, Lakewood, San Pedro, Downey, Los Angeles, Inglewood), logo and image (ams-logo.png), parentOrganization Audio MotorSports Inc, sameAs = the six sister sites.

Good: NAP matches visible page text; the @id is reused by Service blocks via `provider`.

Gaps and errors:
1. Missing `geo` (lat/long), `priceRange`, `contactPoint` (the SMS line (213) 429-1092 is used in sms: links but is not in schema or visible text), `hasMap`, `email`, `description`.
2. `sameAs` lists only your own sister domains. It has no Google Business Profile, Yelp, Facebook or other third-party profile on the main entity (a GBP maps link and a Facebook link appear only on the /locations/ duplicate block). Third-party profiles are what help entity disambiguation.
3. `telephone` is "(310) 513-8800"; the hub and Tesla sites use E.164 "+13105138800". Use one format.
4. `image` is the logo, not a photo of the shop or work.
5. `AutoPartsStore` describes a parts retailer. The business is chiefly an installer (the hub declares `AutoRepair`). Consider `["AutoPartsStore","AutoRepair"]` or keep one type consistent across the network.
6. All URLs and @ids use www while the apex host serves pages without redirect (see AUDIT_REPORT.md finding 3).

## /locations/ conflicts
- A second entity `LocalBusiness` with `@id https://www.lacarstereo.com/locations/` describes the same shop: same address and phone, but `areaServed` is the State of California (the sitewide block lists 10 cities), different sameAs (maps URL and Facebook), and `description` "Custom car audio installation serving Southern California". Two business entities for one shop on one page is a conflict. Merge into the single `#business` entity (add the extra sameAs and a district list there).
- Sunday is given as `opens 00:00, closes 00:00`, which can be read as open 24 hours or zero hours. Omit Sunday (closed days are expressed by leaving the day out).
- The visible page claims "123 cities" while schema says California or 10 cities; align them.
- Page text says the shop is in one Carson bay; schema should not imply multi-location.

## Install pages
`Service` blocks are valid: name, description, serviceType ("Apple CarPlay Installation in Los Angeles"), provider by @id, areaServed (same 10 cities). Gaps: no `offers` or `priceSpecification` although the pages state "Labor from $149" and "Most cars: same day"; add `Offer` with price 149 and `priceCurrency USD` (or `UnitPriceSpecification` with a minimum). `serviceType` repeats the title rather than naming the service ("Car stereo installation"). BreadcrumbList on install pages omits the Home level (position 1 is "Install").

## Missing types
- Product pages (101): no `Product`/`Offer` markup at all, despite visible price, availability ("In stock in Carson", "Order in, 2 to 3 days"), brand, model. Add Product with name, brand, sku/mpn, image, offers (price, priceCurrency, availability, itemCondition; the "(refurb)" item should be RefurbishedCondition), seller = #business. This is the biggest rich-result gap (Google | AI).
- /faq/ (8 Q&A visible): no `FAQPage`. Google restricts FAQ rich results for most sites, but the markup still helps machine parsing; low effort.
- Category pages: no `ItemList`/`CollectionPage`; no `BreadcrumbList` on shop pages or products (only on install and locations pages).
- Homepage: no `WebSite` (name, url) or `Organization` logo separate from the business entity; no `SearchAction` needed.
- /about/: no `AboutPage`, no `Person` for staff.
- Reviews: the site states "4.8 stars, 654 Google reviews" but has no `aggregateRating`. Recommendation: do NOT add it. Google does not use self-served review markup for LocalBusiness, and it risks a manual action. The visible claim should link to the Google profile instead.

## Fixes (priority)
1. Merge the duplicate LocalBusiness on /locations/ into #business; fix Sunday hours. Effort quick.
2. Enrich #business: geo, priceRange, contactPoint (both phone and SMS), hasMap, GBP/Yelp/Facebook in sameAs, E.164 phone. Effort quick.
3. Add Product + Offer + BreadcrumbList to the product template. Effort medium.
4. Add Offer to Service blocks; fix Breadcrumb Home level. Effort quick.
5. Add FAQPage to /faq/. Effort quick.
6. Re-validate in Rich Results Test after the noindex is removed (nothing will show in Google until then).
