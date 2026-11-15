# Schema report: lacaralarm.com (LA Car Alarm)

Audit date 2026-10-04. Source: **hub-mounted copy, proxy for the standalone domain, standalone not verified** (https://www.audiomotorsports.com/alarm/..., 56 pages). Nothing on www.lacaralarm.com could be fetched. Every item below is [mount-proxy].

## Inventory (56 pages fetched, all JSON-LD parsed, 0 invalid JSON)
| Type | Pages | Notes |
|---|---|---|
| BreadcrumbList | 53 | Missing on home, es home, /book/; fine |
| AutoRepair (entity) | 46 | Main entity on most pages |
| AutomotiveBusiness + AutoRepair (array) | 2 (home, es home) | Richest block: sameAs x12, areaServed 31 cities + GeoCircle, employees |
| LocalBusiness | 6 (West Carson, Anaheim, Huntington Beach, Santa Monica, Pasadena, Glendale) | Different type, name and `@id` pattern than the rest |
| FAQPage | 44 | Home, es home, services (11 incl. index), blog (4), FAQ page and 26 city pages |
| Service | 10 | Service pages, provider referenced as AutoRepair |
| BlogPosting / Blog | 3 / 1 | datePublished present (sample 2026-08-13) |
| VideoObject | 37 | uploadDate 2026-09-25 |
| ItemList / CollectionPage / WebSite | 2 / 3 / 2 | |

## Findings
### S1 [mount-proxy] High: every URL and @id is on audiomotorsports.com
`@id` = https://www.audiomotorsports.com/alarm/#business, `url` = the hub URL on all pages, breadcrumb `item` and og:url likewise. lacaralarm.com is not declared as the brand's URL or `sameAs`; sister domains lacarbeats.com, lacartint.com, amspods.com and teslatintla.com ARE in `sameAs` but lacaralarm.com is not. Impact (Google + AI): entity resolution ties the "LA Car Alarm" brand to audiomotorsports.com rather than the domain named in the brand.
Fix: on the standalone build emit `url`, `@id` (https://www.lacaralarm.com/#business) and breadcrumbs on the lacaralarm.com host, with `parentOrganization`/`sameAs` pointing to audiomotorsports.com. Verify first; the standalone output is unknown.

### S2 [mount-proxy] Medium: four entity variants for one business
- Home: `["AutomotiveBusiness","AutoRepair"]`, name "Audio MotorSports", alternateName includes "LA Car Alarm", telephone +13105138800, priceRange "$$".
- Service pages and 20 city pages: `AutoRepair`, name "LA Car Alarm".
- 6 city pages: `LocalBusiness`, name "LA Car Alarm at Audio MotorSports", telephone "(310) 513-8800", `openingHours` string instead of `openingHoursSpecification`, geo as numbers (33.8317) not strings, shared `@id` with a different `url` per page.
- West Carson geo (33.8317, -118.2645) differs from the shop geo (33.8270, -118.2650) used elsewhere; the former may be intentional as a page-center and should not be used as the business location.
Fix: one canonical entity block: `@type: ["AutomotiveBusiness","AutoRepair"]`, name "LA Car Alarm", legalName "Audio MotorSports Inc", one `@id`, telephone +13105138800 on all 52 blocks (6 use the other format), same geo, same hours format. Per-city pages should reference the entity by `@id` and add only `areaServed`.

### S3 [mount-proxy] Medium: FAQ schema repeated across service pages
Same 8 FAQ items on home, es home, services index and 9 service pages (12 pages). Schema matches visible `<details>` where tested (0 mismatches across 44 FAQPage blocks: every schema question and first 60 chars of the answer are in the visible text), so parity is good, but duplicate FAQs give no topic signal. Fix: topic-specific questions per service page; keep schema and visible text identical. Note: Google limits FAQ rich results to authoritative government/health sites since 2023, so this is for AI/answer-engine parsing, not a Google rich result.

### S4 [mount-proxy] Low: self-serving AggregateRating
`AggregateRating` 4.8 from 654 (28 blocks) matches the visible "Google 4.8 from 654" on the home page. Google does not show review stars for self-serving LocalBusiness ratings; harmless, but ensure the number tracks the GBP count and add `dateModified` when the count changes. Yelp 4.7 from 777 is shown on the page but not in schema.

### S5 [mount-proxy] Low: missing fields worth adding
- `hasMap` (the Google Maps CID URL already in sameAs), `paymentAccepted`, `knowsAbout` (Viper, Compustar, DroneMobile, remote start, immobilizer, GPS tracking).
- Service pages: `offers` with `price` for Viper 3108V ($269 installed) and Compustar 9910 (from $499 installed), `areaServed` Carson/South Bay/LA/Orange County, `hasOfferCatalog`.
- Home: `dateModified`; BlogPosting: `author` Person with `url`, `dateModified`.
- BreadcrumbList on home/book not needed.

## Validation status
Rich-results test and Schema.org validator were not run (no external fetch of a lacaralarm.com URL possible; hub URLs are not the target property). JSON syntax and field presence verified locally.
