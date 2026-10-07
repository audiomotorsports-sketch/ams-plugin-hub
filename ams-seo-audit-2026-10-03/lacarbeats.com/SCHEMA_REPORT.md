# Schema Report: lacarbeats.com

Date 2026-10-04. **Evidence: hub-mounted copy (`https://www.audiomotorsports.com/beats/`), a proxy for the standalone domain. Standalone www.lacarbeats.com NOT verified** (egress proxy blocks it). Source: JSON-LD parsed from all 196 `/beats/` URLs (200 OK); 0 parse errors. Not run: Google Rich Results Test (unreachable). Tag for everything below: [mount-proxy].

## Key finding: no JSON-LD points to lacarbeats.com
The expectation was JSON-LD referencing `https://lacarbeats.com/#business`. On the mount it does not:
- Business node `@id` on all 196 pages: `https://www.audiomotorsports.com/beats/#business` (type `["AutomotiveBusiness","AutoRepair"]` on 93 pages, `AutoRepair` on 164 incl. nested). `url` is `https://www.audiomotorsports.com/beats/`.
- A second node on all 196 pages: `https://www.audiomotorsports.com/#business` (Audio MotorSports, hub) used as parentOrganization/ reference.
- The string `lacarbeats.com` appears nowhere in JSON-LD. In HTML the only hostname is `shop.lacarbeats.com` (62 links, 28 pages).
- `sameAs` (12 URLs) includes Instagram, Facebook, TikTok, YouTube, Yelp short link, Google Maps ftid, share.google, audiomotorsports.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com. It does not include lacarbeats.com or lacarstereo.com.
- Result: the same shop has at least `/beats/#business` and `/#business` on the hub, and (unverified) whatever ID the standalone uses. If the standalone also emits `https://www.lacarbeats.com/#business` **[standalone unverified]**, that is a third ID for one real-world business.

## Types in use [mount-proxy]
| Type | Pages | Note |
|---|---|---|
| BreadcrumbList / ListItem | 193 | Good |
| AutoRepair (+ PostalAddress, GeoCoordinates, City areaServed) | 164 | Good NAP, geo and 40+ cities in areaServed |
| FAQPage / Question / Answer | 146 | Answers match visible text (spot-checked Torrance and subwoofer-install: all visible) |
| AggregateRating | 111 | Self-serving on the business node (4.8 / 654) |
| AutomotiveBusiness + OpeningHoursSpecification + Person | 93 | Hours Mon-Sat 09:30-18:00 |
| Service + Offer | 55 | On `/services/*` pages |
| LocalBusiness | 71 | Mixed with AutoRepair |
| WebSite, CollectionPage | 34, 27 | Shop pages |
| VideoObject | 6, BlogPosting 3, Blog 1, OfferCatalog 7, Review 4 | |
| Product / Offer on products | 0 | Product detail is on shop.lacarbeats.com (unverified) |

## Issues
1. **No lacarbeats.com identity** (above). Improve: on the standalone, one `@id` `https://www.lacarbeats.com/#business`, `url` = standalone home, `sameAs` including the Google Business Profile and Yelp, and `parentOrganization` -> `https://www.audiomotorsports.com/#business`. Do not change the mount without checking the standalone first. (medium)
2. **Mixed `@type` forms** across pages: `["AutomotiveBusiness","AutoRepair"]` on 93, `AutoRepair` on others, `LocalBusiness` on 71. Pick one array and use it everywhere. (quick)
3. **Subwoofer page markup lists non-services as Service nodes.** `/beats/services/subwoofer-install/` has 13 `Service` nodes, among them "Sealed or ported enclosure", "Amplifier and wiring with the subwoofer install", "Dual Kicker Comp loaded box, house special, box only" (a product/offer), "AudioControl LC7 Pro / LC5 Pro" (a product). Improve: one `Service` (serviceType "Car subwoofer installation") with `hasOfferCatalog`; model the $249 box as `Offer` of a `Product` with price 249 USD, `availability` InStock, `priceValidUntil`. (medium)
4. **Self-serving `AggregateRating` on the business node** (111 pages). Google does not show stars for LocalBusiness self-markup; stale counts across pages are a maintenance risk. Keep only where the reviews are shown and cite the source (Google/Yelp). (quick)
5. **`/beats/shop/subwoofers/` has no ItemList/Product.** 16 products shown (e.g. Kicker CVR12-2, CVR12-4, 44CVX122, 51CWQ122); schema is only BreadcrumbList/CollectionPage/WebSite. Add `ItemList` with name, URL, brand. (medium)
6. **FAQPage:** no Google rich result for this site type (restricted since 2023), but valid and useful for AI parsing. Average answer 34 words (1,263 answers), max 108; 4 over 80 words. City-page answers are often too short to carry a fact, e.g. "Yes. A payment plan is available through our payment plan partner." Improve: lead with the fact. (see AI_SEARCH_REPORT)
7. **Latitude/longitude as strings** ("33.8270", "-118.2650"); use numbers. (quick)
8. **Missing:** `priceRange` is present ("$$") on the home node; `hasMap` (Google Maps URL), `foundingDate` (2003, stated in text), `aggregateRating` source, `knowsAbout`, `makesOffer` are absent. `Person` nodes exist on 93 pages (not inspected in detail). (quick)
9. **Email** (Gmail address) in every business node. (low)
10. **areaServed** lists City names without `@id`s except Los Angeles (Wikipedia). Add `@id`/`sameAs` Wikipedia/Wikidata for Carson, Torrance, Long Beach etc. so engines resolve places. (quick)
11. **BlogPosting** (3): dates present (2026-08-11 to 08-13). Check `author` is a `Person` with url. (quick)

## Suggested subwoofer-page JSON-LD (illustrative; every value must come from the owner, placeholders in braces)
```json
{
 "@context":"https://schema.org",
 "@type":"Service",
 "@id":"https://www.lacarbeats.com/services/subwoofer-install/#service",
 "name":"Car subwoofer installation in Carson, CA",
 "serviceType":"Car subwoofer installation",
 "provider":{"@id":"https://www.lacarbeats.com/#business"},
 "areaServed":["Carson","Torrance","Long Beach","San Pedro","Wilmington","Gardena"],
 "offers":{"@type":"Offer","name":"Dual Kicker Comp loaded box (box only, install quoted)","price":"249","priceCurrency":"USD","availability":"https://schema.org/InStock"}
}
```
Verify the real standalone path and IDs on www.lacarbeats.com first.

## Prioritized schema actions
| Page | Problem | Impact | Effort | Exact next step | Tag |
|---|---|---|---|---|---|
| All | No lacarbeats.com `@id`/sameAs | ai | medium | Add `@id` `https://www.lacarbeats.com/#business` on the standalone, sameAs to GBP/Yelp; keep one ID per entity | [mount-proxy] |
| /services/subwoofer-install/ | 13 Service nodes incl. products | google, ai | medium | Reduce markup to one Service plus Offer for the $249 box (markup change only, page content stays) | [mount-proxy] |
| /shop/subwoofers/ | No ItemList/Product | google | medium | Add ItemList of 16 subs | [mount-proxy] |
| All | Mixed business @type | ai | quick | Standardize | [mount-proxy] |
| All | Lat/long strings, no hasMap | google | quick | Numbers; add hasMap | [mount-proxy] |
| City pages | Short FAQ answers | ai | medium | Rewrite to 40-80 words | [mount-proxy] |
