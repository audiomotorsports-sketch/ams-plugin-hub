# Schema Report: teslatintla.com

Date: 2026-10-04. Source: JSON-LD parsed from all 143 sitemap URLs (python json.loads). Rich Results Test / Schema validator not reachable, so "valid" below means well-formed JSON with sensible schema.org types, not Google eligibility confirmation (UNVERIFIED).

## Inventory (node counts across 143 pages)

| Type | Count | Notes |
|---|---|---|
| BreadcrumbList | 141 | All pages except homepage and /book/ |
| FAQPage | 132 | Homepage, locations, 124 city pages, 6 model posts |
| AutoRepair | 56 (+ nested) | City pages and /locations/ business node |
| LocalBusiness-family total | 127 business nodes | Homepage uses AutomotiveBusiness, city pages AutoRepair |
| BlogPosting | 8 | Model posts + 2 comparison posts |
| ImageObject @graph | 1 | /gallery/ (9 images, thumbnails from i.ytimg.com) |
| WebSite, AboutPage, ContactPage, ItemList, Blog, WebPage | 1-2 each | Utility pages |
| Product / Service / Offer / VideoObject | 0 | None present |

Parse errors: 0. (One apparent error in my tool was the /gallery/ `@graph` wrapper, which is valid.)

## What is good

- Homepage `AutomotiveBusiness` has `@id` https://teslatintla.com/#business, NAP matching the page, geo coordinates (33.8270587, -118.2641283), openingHoursSpecification Mon-Sat 09:30-18:00, 12 sameAs links (Instagram, YouTube, Facebook, TikTok, Yelp, Google Maps ftid, plus sister domains), logo, image, `parentOrganization` -> audiomotorsports.com/#business.
- Homepage FAQPage: 7 questions whose text matches the visible FAQ headings (Which Tesla models, GPS/phone signal, Model Y duration, windshields, payment plan, appointment, overnight drop-off).
- Breadcrumb names/URLs match visible breadcrumbs; canonical host consistent (apex).
- WebSite node present with publisher reference to the business @id.

## Problems

1. **Self-serving review and rating markup (126 nodes carry aggregateRating, 55 carry Review arrays).** Homepage, /locations/ and city pages mark the business itself with `aggregateRating` 4.8 / 654 and individual Yelp reviews (e.g., "Rudy R.", 2023-06-09, publisher Yelp). Google does not show review stars for LocalBusiness/Organization markup written by the business about itself, and mixing Google's count (654) with Yelp-sourced review text under the same node invites a mismatch/spam-policy flag. Gain: none for Google; risk: low-moderate. AI engines read the text anyway, so keep the visible reviews, drop the structured Review/aggregateRating from city pages (and keep at most one rating statement on the homepage only if you can cite the source).
2. **City pages create a second, unlinked entity.** Each city page defines an `AutoRepair` with no `@id`, `name` "Tesla Tint LA", full Carson address and the same geo, while the Review's `itemReviewed` references `https://teslatintla.com/#business`. 124 pages therefore assert 124 anonymous copies of the shop plus a reference to the real one. Fix: use `"@id": "https://teslatintla.com/#business"` (same node) or reference it with `{"@id": ...}` instead of re-declaring it.
3. **areaServed contradicts content.** Homepage lists 27 cities plus a 10-mile GeoCircle (`geoRadius` 16093 m). Pages cover Brea (21.8 mi), Malibu, Pasadena, Rancho Cucamonga etc. City pages set `areaServed` to a single City each (e.g., Brea) while their body says "We are not in Brea". Pick one story: the shop is in Carson, serves customers within X miles. Remove the 10-mile circle or widen to match.
4. **Entity naming split.** Homepage `name` = "Audio MotorSports" (alternateName includes "Tesla Tint LA"); city pages `name` = "Tesla Tint LA"; parent also "Audio MotorSports" typed `AutoRepair`. Parent/child both typed AutoRepair/AutomotiveBusiness at the same address and phone. Use one @id per real entity, with the Tesla site as `brand`/department or `ServiceChannel`, matching the single Google Business Profile name.
5. **Employee node names an individual** ("Nick", jobTitle "Sales · Acoustic Audio") on all 127 business nodes: odd job title for a tint site, no surname, and `email` (audiomotorsports@gmail.com) is exposed in markup. Remove `employee` or give a proper `Person` with role "Tesla tint specialist" only if the business agrees to be named; consider dropping the gmail address from schema.
6. **No Service/Offer markup despite published prices.** The site publishes a full price matrix (e.g., Solar Ceramic Model Y doors+back $349, 3M IR $549, windshield $189/$299) but no `Service` + `Offer` (or `hasOfferCatalog`) nodes. Add one `Service` per film package with `offers` (price, priceCurrency USD, `areaServed`), on the homepage only, not 124 copies.
7. **BlogPosting is thin.** Fields present: headline, datePublished (e.g., 2026-08-27), description, author (Organization "Tesla Tint LA"), publisher (Organization, no logo), mainEntityOfPage. Missing: `dateModified`, `image`, publisher `logo`, a Person author. Add them (quick).
8. **FAQPage rich results.** Google restricts FAQ rich results to authoritative government/health sites since 2023, so the 132 FAQPage nodes will not produce SERP snippets (UNVERIFIED for this domain, but per Google's published policy). They still help AI parsers and are harmless; but identical price-heavy FAQ text repeated across 124 city pages offers no extra benefit.
9. **Homepage has no BreadcrumbList** (fine) and **/book/** only has the business node (no `ReservationAction`/`potentialAction`). Optional: add `potentialAction` with `ReserveAction` target /book/.
10. **hreflang/inLanguage:** Spanish pages /es/* exist; checking for `inLanguage` or translated schema was not done beyond /es/ canonical/hreflang tags (reciprocal and correct).
11. /gallery/ ImageObjects point to YouTube thumbnails (i.ytimg.com) while the page shows videos: `VideoObject` (name, thumbnailUrl, uploadDate, embedUrl) would be the correct type and is eligible for video results.

## Recommended homepage JSON-LD shape (not published, example only)

One `@graph` with: `AutomotiveBusiness` (@id #business, name matching GBP, one address, geo, hours, sameAs, areaServed consistent with a stated radius), `WebSite`, `Service` x 3 (Solar Ceramic, 3M IR Ceramic, Windshield) each with `Offer`, `FAQPage`. City pages: `WebPage` + `BreadcrumbList` + `{"@id": "#business"}` reference only.
