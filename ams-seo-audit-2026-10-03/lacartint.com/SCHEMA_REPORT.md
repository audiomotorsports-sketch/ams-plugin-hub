# Schema Report: lacartint.com

**Evidence label: hub-mounted copy (https://www.audiomotorsports.com/tint/), proxy for the standalone domain, standalone not verified.** Date 2026-10-04. Source: JSON-LD parsed from all 141 `/tint/` sitemap URLs (0 parse errors). The standalone domain's JSON-LD could not be fetched (www blocked). Rich Results Test not reachable, so "valid" means well-formed with sensible types, not Google-eligibility confirmed.

## 1. Inventory (141 pages)

| Item | Count | Note |
|---|---|---|
| Pages with a business node | 139 of 141 | The 2 exceptions are `/tint/privacy/` and `/tint/terms/`, which carry `WebPage` nodes instead |
| Business node typed `LocalBusiness` | 71 | All on city pages (71 of 109) |
| Business node typed `["AutomotiveBusiness","AutoRepair"]` | 68 | 38 city pages plus all non-city pages |
| `@id` on the business node | `https://www.audiomotorsports.com/tint/#business` on all 139 | Single id, but typed two ways (see 2.2) |
| FAQPage | 128 pages, 1,222 Q&A | 10 questions on 71 city pages, 9 on 42 |
| BreadcrumbList | 139 pages | City pages: Home > Locations > City |
| Service | 4 | ceramic-film, full-vehicle-ceramic-tint, hand-cut, california-legal-fronts, each with its own `#service` id |
| BlogPosting | 3 | The 3 posts (`/blog/` index carries FAQ only) |
| Product / Offer / Review (array) | 0 / 0 / 0 | Prices are not in structured data |
| `aggregateRating` (4.8 / 654) on the business node | 111 pages | 109 city pages (71 LocalBusiness, 38 AutoRepair), `/tint/` home and `/tint/es/` |
| `sameAs` containing lacartint.com | 0 | See 2.1 |
| `lacartint.com` anywhere in the mount's JSON-LD | 0 | The brand domain is never named in the mount's own schema |

## 2. Findings

### 2.1 Entity: `@id` lacartint.com/#business versus /tint/#business (the question asked)

- The **mount** names its business `https://www.audiomotorsports.com/tint/#business` (name "LA Car Tint at Audio MotorSports", `url` = the page itself, `parentOrganization` = `https://www.audiomotorsports.com/#business`).
- The **hub's other pages** reference a different node: on `/locations/` and `/torrance/` a `subOrganization` entry reads `{"@type":"AutoRepair","name":"LA Car Tint","url":"https://www.lacartint.com/","@id":"https://www.lacartint.com/#business"}`. The hub `sameAs` lists `https://www.lacartint.com/` and `https://teslatintla.com/`.
- Result, as seen from the hub side: **two `@id`s for one entity** (`.../tint/#business` and `lacartint.com/#business`). The mount's `sameAs` has 12 links including teslatintla.com and the hub, but **not lacartint.com**, so the mount never says "I am the same entity as lacartint.com".
- Standalone: `@id` on www.lacartint.com is **not verified**. The hub's references suggest `https://www.lacartint.com/#business` (with or without www is itself unknown; the hub writes it as `https://www.lacartint.com/#business`).
- Improve (do not remove any page): on the standalone use exactly one id, `https://www.lacartint.com/#business`, on every page, with `parentOrganization` pointing at `https://www.audiomotorsports.com/#business`. On the hub mount keep its own id but add `lacartint.com/#business` to `sameAs` (or `"@id"` cross-reference) so the two nodes are declared as the same entity. The GBP share link and Maps `ftid` are already in `sameAs` and should be identical on all three sites (they are on the mount and on teslatintla).

### 2.2 Same `@id` typed two ways

71 city pages emit the node as `LocalBusiness`, 38 city pages and all other pages as `AutomotiveBusiness/AutoRepair`, all with the same `@id`. A graph merge sees one id with conflicting types. Pick one type for the whole site (`AutoRepair` or `AutomotiveBusiness`; the more specific `AutoRepair`/`AutomotiveBusiness` is already the majority). Pages affected are marked in `pages.csv` column `issues`.

### 2.3 Self-serving `aggregateRating` (111 pages)

The 4.8 / 654 rating sits on the business node itself, on 110 pages besides the home (109 city pages and `/tint/es/`). Google does not show review stars for self-serving ratings on LocalBusiness/Organization nodes, and the count will go stale. Improve: keep the rating as visible text with a link to the Google Business Profile reviews, and keep structured rating markup only where the reviews are actually listed on the page (`/tint/reviews/`), driven from the live number rather than hard-coded.

### 2.4 FAQPage schema with no visible FAQ (12 pages)

Google requires FAQ markup to match visible content. These 12 pages have FAQPage JSON-LD but the questions do not appear in the rendered text (checked by exact string):

`/tint/about/`, `/tint/all-services/`, `/tint/gallery/`, `/tint/reviews/`, `/tint/blog/` (index), the 3 blog posts (`california-70-vlt-fronts`, `solar-and-solar-ceramic-weekly-special`, `tesla-glass-hand-cut`), `/tint/es/`, `/tint/es/about/`, `/tint/es/faq/`, plus `/tint/tesla-tint/` partially (7 schema questions, 1 visible).

On the 3 blog posts the schema carries the same 9 site-wide questions (for example "Do you computer-cut the film?") on every post. On `/tint/es/faq/` the schema questions are English ("How long does tint take?") while the visible page is Spanish. Improve: add a visible FAQ block on each page that matches its schema (or write post-specific questions), and write Spanish schema text for the Spanish pages. On the other 116 FAQ pages parity is exact: **1,139 of 1,222 questions and all answers are visible** (the 83 gap is these 12 pages).

### 2.5 Other schema notes

- `url` on the business node equals the current page URL on city pages, which makes the "business" url change per page. The `url` should be the entity home (`https://www.lacartint.com/`), with the page in `mainEntityOfPage`/`WebPage`.
- `areaServed` is a single `City` (the page's city, e.g. "West Carson"). The page copy says the shop is not in that city, which is honest, but the node would be more accurate as a `GeoCircle` or a list of areas, in line with the real service area (Carson plus South Bay, LA, OC). A consistent service radius should match `/tint/locations/` (which says "109 drive-ins"; the hub llms.txt says 123).
- Address: `streetAddress` 22025 S Avalon Blvd Ste A, Carson, CA 90745, phone (310) 513-8800, geo 33.8317, -118.2645 are consistent on the pages checked. (teslatintla.com uses geo 33.8270587, -118.2641283 for the same address: two coordinates for one shop. Use the GBP pin on all sites.)
- `openingHours` is a string "Mo-Sa 09:30-18:00" (valid). `openingHoursSpecification` is the more robust form.
- `email` is a personal-looking Gmail address in the business node on every page. Consider a role address.
- The 4 `Service` nodes have their own `#service` ids and a provider reference: a good pattern. Add `offers` with the published prices (Solar $249, Solar Ceramic $329 installed) so the schema carries the same prices as the page and llms.txt.
- Spanish pages have `hreflang` en/es/x-default on 6 pairs, which is good.

## 3. Schema fixes in priority order (all improve, nothing removed)

1. Single `@id` and a cross-declared `sameAs` between standalone, mount and hub. [mount-proxy]
2. Visible FAQ blocks for the 12 pages whose schema has no visible match. [mount-proxy]
3. Move the aggregateRating off city pages; keep text + GBP link. [mount-proxy]
4. One business `@type` everywhere. [mount-proxy]
5. `offers` with prices on the 4 Service nodes and the home. [mount-proxy]
6. Run the same extraction on https://www.lacartint.com/ once the proxy allows it, and diff against this report. [standalone-verified step pending access]
