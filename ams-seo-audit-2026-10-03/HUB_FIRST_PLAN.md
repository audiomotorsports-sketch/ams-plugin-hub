# audiomotorsports.com first: pilot plan, then copy to the other sites

Prepared 2026-10-07 for Zack and Tom. **Nothing here has been applied.** No site, repo or account was changed. Every page and site stays live; fixes only improve pages; nothing goes live without Zack and Tom reviewing it together.

## 1. What has been run on the hub
| Audit | Scope | Where |
|---|---|---|
| SEO / technical | 1,090 sitemap URLs crawled (1,057 returned 200, 33 returned 308) | `audiomotorsports.com/AUDIT_REPORT.md`, `pages.csv` |
| Schema | all JSON-LD parsed (0 invalid blocks) | `SCHEMA_REPORT.md` |
| AI search + AI Overviews | 61 live pages, 19 crawler user-agents, 15 target queries | `AIO_REPORT.md`, `AI_SEARCH_REPORT.md` |
| Launch (phone + desktop, links, forms, console, speed) | 24 URLs, 581 links checked | `launch/LAUNCH_NOTES.md` |

**Re-checked today (2026-10-07), read-only, all still true:** home title is "Audio MotorSports | Carson Shop" with H1 "Pick a skill"; the home page has 0 hreflang tags; `/aftercare/` returns 404 while `/tint/aftercare/` returns 200; `/carson/` redirects (308) to `/locations/`; `/tesla/tesla-tint-carson/` is still titled "Tesla Window Tint Avalon"; robots.txt and llms.txt are live (200); no noindex on the home page.

**Not known:** whether Google has actually indexed the hub's city pages and `/stereo/shop/` products. Only Search Console can answer that. It is the one number that matters most for the hub and we do not have it yet.

## 2. What is already healthy on the hub (protect these during changes)
All sitemap pages return 200 except the 33 shop redirects; every HTML page has a unique title, meta description, one H1 and a self-canonical; no noindex; all 6,404 images have alt text; JSON-LD is valid; name, address, phone and hours are consistent; robots.txt is open to Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot and others; llms.txt exists; HSTS is on. **After every change, re-check this list so a fix does not break what works.**

## 3. Blast radius: read this before touching anything
The hub serves about 775 mounted copies of the brand sites (`/tint/`, `/beats/`, `/alarm/`, `/tesla/`, `/stereo/`, `/amspods/`), about 71% of its sitemap, and they share templates (footer, hero, banner, city pages). Two consequences:
- **Good:** one template fix on the hub repairs the same problem across hundreds of mounted pages. That is how the hub becomes the pilot for the other brands.
- **Risk:** one wrong template edit can break hundreds of pages at once. Change one template at a time, test on a copy first, verify with a crawl, keep the saved original.
- **Unknown:** whether the standalone domains (lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com) use the same templates, or separate copies. Check this before assuming a fix carries over (section 6).

## 4. Hub fixes in order (all improve pages; none removes anything)
| # | Fix | Where | Effort | Carries to other sites? |
|---|---|---|---|---|
| 1 | Aftercare footer link: change `/aftercare/` to `/tint/aftercare/` (404 today) | shared footer/nav on every `/tint/` page | quick | Yes if template shared (lacartint) |
| 2 | Tesla Carson page: replace the city-name "Avalon" with "Carson" in title, H1, breadcrumb, description, FAQ; refresh `datePublished`, add `dateModified`. **Never touch "Avalon Blvd" in the address.** | `/tesla/tesla-tint-carson/` | quick | Same fix needed on teslatintla.com |
| 3 | Remove developer comments from public source; add `data-nosnippet` and reserved height to the Sunday "Closed today" banner | hero partial, banner script | quick | Yes (all mounts) |
| 4 | Home page: service + Carson title, a real H1, a 50-70 word answer paragraph, 5 question headings with FAQ, and the city-page business node (geo, sameAs, areaServed) copied into the home JSON-LD | `/` | medium | Pattern for every brand home |
| 5 | FAQ text that matches its schema: eight pages with FAQPage schema but no visible FAQ (`/tint/all-services/`, `/tint/blog/california-70-vlt-fronts/`, `/alarm/blog/viper-vs-compustar/`, `/beats/brands-we-love/`, `/brands-we-love/`, `/tesla/tesla-tint-carson/`, `/tesla/tesla-tint-torrance/`, `/faq/`); on `/faq/` set 13 shortened schema answers equal to the visible answers | those pages | quick | Same rule everywhere |
| 6 | One price source: reconcile the FAQ meta ("no public prices") with llms.txt and city FAQs ($249/$329) and the `/tesla/` promo ($149/$299) vs "Matrix" ($189/$369) prices. Add one dated price table. Prices must be confirmed by the shop. | `/faq/`, `/tesla/`, `/tint/`, llms.txt | quick | Yes |
| 7 | Carson answer: add "Carson" to the `/tint/` title and a 60-word answer. Decide separately whether `/carson/` should become a real page instead of redirecting to `/locations/` (adding a page is additive, but changing that redirect is a decision). | `/tint/`, `/locations/`, `/carson/` | medium | Brands lacking Carson answers |
| 8 | hreflang: add `en`, `es`, `x-default` links on `/` and every page that has a `/es/` twin | `/` and twins | quick | Same on teslatintla `/es/` |
| 9 | Sitemap: remove only the 33 redirecting `/shop/` URLs and `/stereo/cart/`; stamp real `lastmod`. Never remove a city or location page. | `sitemap.xml` | quick | Yes |
| 10 | `dateModified` in JSON-LD and a visible "Last updated" beside prices and FAQs | templates | medium | Yes |
| 11 | Service pages (nine of them, two FAQs each): answer intro, 4-6 question headings, price/time/included table, install steps. Differentiate `/services/dash-camera/` (Thinkware) from `/services/dash-cameras/` (buyer guide) and cross-link. | `/services/*` | medium | Pattern for brands |
| 12 | `/reviews/`: date and service on each quote, "as of" date next to 654 / 777, same wording everywhere | `/reviews/` | quick | Yes |
| 13 | `/about/`: Person nodes for Alex and Richard (only Zack and Nick have them); bylines on blog posts | `/about/`, blogs | quick | Yes |
| 14 | llms.txt tidy: link `/tint/` directly, root-relative data path, list best passages, reconcile the warranty line with the visible FAQ | `/llms.txt` | quick | Yes (optional; Google Search ignores llms.txt) |
| 15 | Headers: report-only CSP, HSTS `includeSubDomains`, `security.txt`, domain email instead of Gmail in schema | server config | quick | Yes |
| 16 | City-page template (project): answer-first question headings, a 40-60 word direct answer before the address, a route/drive-time table, varied local FAQs, a dated local review | hub city pages | project | The biggest carry-over (all brands' city pages) |

## 5. How to pilot safely (so you can prove it works before copying it)
1. **Baseline first.** Zack verifies the hub in Search Console (a "Domain" property if possible) and exports Performance (queries and pages), Pages (indexing) and Core Web Vitals as CSVs. Run `AI_VISIBILITY_QUERY_SET.md` once per engine. Run `probe.py` from a normal network. Date everything.
2. **Do fixes 1-3 and 5-6 first** (quick, low risk), re-test, wait.
3. **Pilot the city template (fix 16) on 5 pages only**, for example `/torrance/`, `/long-beach/`, `/gardena/`, `/redondo-beach/` and `/san-pedro/`, and leave the rest untouched as a control group. Compare indexing, impressions and calls after 2 to 4 weeks before touching the other cities.
4. **Look at "Crawled - not indexed" in Search Console.** If hub city pages or `/stereo/shop/` products show it, the fix is more unique local content and better internal links on those pages, not removing them.
5. **Keep a dated change log** (what, where, when, saved original).

## 6. Moving to the other sites
Do this only after the hub change is tested and behaving.
| Step | Action |
|---|---|
| 1 | For each brand domain, check whether it uses the same template as its hub mount (view-source and compare the footer, hero comment, banner, city page). Do this from your own network, since the standalone `www` hosts are blocked from the audit environment. |
| 2 | Shared template: the hub fix has already carried over; verify on the standalone. Separate copy: apply the same change there, one site at a time. |
| 3 | Site-specific work after the hub pattern: **lacarstereo.com** (live, blocked from search, `/book/` loses leads), **shop.audiomotorsports.com** (52 broken card links, API 500, ~282 noindexed products), **teslatintla.com** (the "Avalon" page, phone layout), **amspods** and **lacaralarm** (leaked internal text). |
| 4 | Order after the hub: lacarstereo, then shop, then teslatintla, then the three brand mounts. Reasons: lacarstereo and the shop are losing leads or visibility today. |

## 7. Not safe on the hub
Deleting, trimming, merging or noindexing any city or location page; removing the 775 mounted copies; changing a shared template without a saved copy and a test; replacing "Avalon" blindly; mass-generating AI pages; typing API keys into unreviewed pages; any change without Zack and Tom's joint approval.

## 8. Limits
Hub findings come from fetched pages (verified) and sample checks; Search Console, GBP, field speed data and live AI-engine results were not available. Speed numbers from the sandbox were noisy. Standalone brand domains were audited through the hub's mounted copies. Draft wording that contains prices, times or distances must be confirmed by the shop.

---
## Updates from the deep dive (2026-10-07)
Six research agents ran after this plan was first written. Where they disagree with the plan above, **this section wins.** Files are in `hub_deep_dive/` (start with `TOMORROW_AGENDA.md`).

- **Item 1 (Aftercare link):** on 2026-10-07 the hub crawl found `/aftercare/` linked by **0 of 1,194** pages (pages that mention aftercare now link `/tint/aftercare/`), though `/aftercare/` still returns 404. The earlier 404 footer link may have been fixed after 2026-10-04, or it still appears on the standalone lacartint.com. Re-check before treating it as open.
- **Item 2 (Tesla Carson page):** exactly 58 uses of "Avalon" in the live HTML: 12 are the street address (must not change), 46 are city-name uses. A blind replace would also publish "There is no Carson Tesla tint storefront" on the Carson page, so that answer is rewritten in the draft.
- **Item 5 (FAQ parity) is bigger than 8 pages.** The harness found 97 pages with 369 FAQ schema questions not in the visible text (Tesla 57, amspods 12, tint 12, beats 9, alarm 6). On `/faq/`, 15 of 18 schema answers are not on the page and 8 visible answers are cut off mid-sentence.
- **Item 8 (hreflang):** only `/` lacks it. The 16 `/es/` twins already have correct tags.
- **New: leaked wording.** "We do not invent..." shows on 14 hub pages (including `/faq/`, `/tesla/` and eight `/tesla/blog/*`) and inside FAQ schema.
- **New: sitemap grew** from 1,090 to 1,194 URLs (99 root-level city pages, 4 service pages, 1 vehicles page); the new pages have not been reviewed.
- **New: the plugin repo is not the hub's source.** It is a drop-in pack for AI coding bots; the English home page was rebuilt and does not contain it. The leaked developer comment is on 8 URLs (`/tint/`, `/beats/`, `/alarm/`, `/amspods/` and their `/es/` twins) and comes from four sibling plugin files not in this repo.
- **New: city pages.** All 158 live city pages use one template: median 85% of sentences repeated on other pages, median 252 unique words, every page opens "We are not in {City}", "Carson" never named as the shop's city in main text, 49 titles over 60 characters, no `dateModified`. `/locations/` links 123 of the 158. Pilot spec and five drafts are in `CITY_TEMPLATE_PILOT.md`.
- **New: listings (from search summaries, unverified).** Sunday hours disagree between the site (closed) and Apple Maps and directories (open about 10-4); two Yelp pages (782 and 774 reviews); two Facebook pages; most listings use "Audio MotorSport" without the "s"; years in business conflict ("since 2003", "25+ years", BBB 2015). Fix these before the website changes, because they affect real customers.
- **New: SERP evidence is thin.** AMS shows strongly for brand searches; the hub did not appear for window tint Carson, Tesla tint Carson, ceramic tint Torrance, car audio Torrance, remote start LA or the Harley pod queries in the search tool (which is not a ranking tracker). A same-street Carson competitor appears.
