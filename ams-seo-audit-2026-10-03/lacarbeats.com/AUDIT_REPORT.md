# SEO Audit: lacarbeats.com (car subwoofers and car audio)

Date 2026-10-04. Read-only. Skill: claude-seo (audit, technical, schema, geo methods), applied by hand to fetched HTML.

> **Evidence label.** www.lacarbeats.com is blocked by the egress proxy, so the standalone site was **not verified**. Apart from section 1, every finding below is from the **hub-mounted copy** at `https://www.audiomotorsports.com/beats/` (196 URLs, all fetched), a **proxy** for the standalone domain. Tags: **[standalone-verified]** and **[mount-proxy]**. See LIMITATIONS.md.

## 1. Standalone domain facts [standalone-verified]
| Check | Result |
|---|---|
| Apex `https://lacarbeats.com/` | HTTP/2 **308** to `https://www.lacarbeats.com/` (single hop visible) |
| TLS | TLS 1.3, Let's Encrypt YR2, CN=lacarbeats.com, valid to 2026-11-08 (renewal due in about 5 weeks; Let's Encrypt auto-renews on Vercel, just confirm) |
| HSTS | `max-age=63072000` (2 years); no `includeSubDomains`/`preload` seen on apex |
| Server | Vercel (iad1) |
| Redirect type | 308 permanent, preserves path (`/robots.txt` to `www/robots.txt`, same for sitemap.xml, llms.txt). Good practice. |
| robots.txt, sitemap.xml, llms.txt | Only the redirect was readable. Content unverified. |
| www host | Not reachable from this network. |

## 2. Hub-mounted copy: summary [mount-proxy]
Technically very clean. 196 of 196 sitemap URLs return 200; every page has a unique title, a unique meta description, exactly one H1, a self-referencing canonical (0 mismatches), no robots meta and no `X-Robots-Tag`, Open Graph tags, JSON-LD that parses (0 errors). Server-rendered HTML (content is in the raw response). Bots (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, ClaudeBot, Claude-SearchBot, GPTBot) get the same 200/72,837-byte response on the hub.

Page inventory: 1 home, 109 `car-stereo-<city>` drive-in pages, 26 service pages (incl. 3 subwoofer-related), 27 shop category/brand pages, 3 blog posts + index, reviews, FAQ, locations, about, gallery, payment plan, specials, book, contact, and 15 `/es/` Spanish pages. 30 pages carry en/es/x-default hreflang (reciprocal, checked on 2 samples).

Indexability under the rules: nothing is noindexed or blocked, so Googlebot-eligibility for AI Overviews holds on the hub copy. Whether it holds for www.lacarbeats.com is **unverified**.

## 3. Findings [mount-proxy unless noted]

### High
1. **Visible code leak on the homepage (EN and ES).** The text `of class="hero-banner" BEFORE Pair with /assets/css/ams-plugin-beats.css -->` renders in page body on `/beats/` and `/beats/es/` (a broken HTML comment). It sits in the first screen and in the text snippet engines extract. Improve: fix the comment markup so no stray text prints.
2. **No dedicated Carson page and no "Carson" in the sub page.** The shop is in Carson (22025 S Avalon Blvd Ste A, 90745) but the city set has only `car-stereo-west-carson`; there is no `car-stereo-carson`. The subwoofer page (title "Car Subwoofer Install in Los Angeles", H1 "Subwoofer Install") never targets Carson, South Bay or OC in H1/H2, and its meta says "Serving Long Beach and Orange County". The query "car subwoofer install carson ca" has no best-fit page. Improve: add a Carson page, add Carson/South Bay to the subwoofer page title, H1 and an answer block (see AI_SEARCH_REPORT sample queries).
3. **Subwoofer cluster is not interlinked.** Zero of 109 city pages link to `/beats/services/subwoofer-install/`; only 3 pages in the whole mount do (homepage, ES homepage, one blog post). City pages link out to apple-carplay and amplifier-install. The site has three overlapping sub pages (`subwoofer-install`, `amps-subwoofers`, `bass-amps-subwoofers`) plus `/shop/subwoofers/` with 16 products. Improve (do not merge): give each a distinct purpose and link them to each other and from city pages (see Section 5).
4. **City pages: opening line tells searchers the shop is not there.** Pattern "We are not in Torrance. There is no Torrance stereo storefront" is honest and fine for trust, but it comes before any service answer, and body paragraphs repeat verbatim 2 to 3 times on the same page (the Torrance page repeats its drive-directions and "$249 box" sentences about three times, 3,904 words incl. nav). About 24% of sentences on an average city page also appear on 50+ other city pages. Improve: lead with the answer (service + distance + what is done), remove in-page repeats, and add local detail unique to each city (see AI_SEARCH_REPORT).
5. **Entity does not name lacarbeats.com.** Mount JSON-LD `@id` is `.../beats/#business` and `sameAs` lists audiomotorsports.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com but not lacarbeats.com, not www.lacarstereo.com, and carries no Wikidata/Wikipedia business entity. If the standalone uses `https://www.lacarbeats.com/#business` it is a third ID for one shop **[standalone unverified]**. See SCHEMA_REPORT.

### Medium
6. **Titles/meta.** Titles are unique and city-templated ("Car Stereo Installation for X | LA Car Beats"). 5 EN titles are over 60 chars (Florence-Firestone 61, Palos Verdes Estates 63, Rancho Palos Verdes 62, Rolling Hills Estates 64, wireless-carplay 61), likely to truncate. The homepage title "CarPlay & Car Stereo Install LA | Amps, Subs" has no Carson/South Bay and no "subwoofer". 6 meta descriptions over 160 chars (all ES). Improve: shorten the 5, add Carson/South Bay to the home title.
7. **Subwoofer-intent copy is promotional but thin on facts.** `subwoofer-install` has 14 images, one $249 offer ("Dual Kicker Comp loaded box, box only; install is quoted"), no install timeframe, no price range for installed jobs, no sealed-vs-ported comparison table, no vehicle examples with specs. Improve: add those (Section 5 and AI_SEARCH_REPORT).
8. **Internal links in nav are root-relative** (`/services/...`, `/shop/...`) on the mount, so on the hub they leave `/beats/` and land on the hub's own pages. This is a mount artifact; on the standalone they would resolve to its own paths. Cannot confirm. Check on the standalone.
9. **Shop links go to `shop.lacarbeats.com`** (62 links on 28 pages incl. all 16 sub product links). That host is also proxy-blocked, so it is unverified. Product pages there should carry Product/Offer schema **[unverified]**. The on-site `/beats/shop/subwoofers/` page has only BreadcrumbList, CollectionPage and WebSite markup and no product list in JSON-LD.
10. **Images: 218 of 1,996 `<img>` lack alt** (about 11%). All 218 are on two pages: `/beats/locations/` and `/beats/es/locations/` (109 each, one per city tile). Improve: add descriptive alt to those.
11. **Stale time-dependent text baked into HTML.** Home and ES home render "Closed today. Text Nick now and we'll hold a Monday 9:30 slot" in the static response. If that is a snapshot of the time of caching, crawlers can read a wrong state. Improve: render hours statically (Mon-Sat 9:30-18:00) and make "open/closed" a client-side enhancement only.
12. **Freshness signals.** Sitemap `lastmod` is 2026-10-03 for the sampled pages (and all pages appear regenerated weekly), but only the 3 blog posts show visible dates (2026-08-11 to 08-13). Service and city pages show no "last updated". Improve: add visible "Last reviewed" on price/special pages.

### Low
13. **Spanish pages:** 15 pages; ES homepage meta is 203 chars. Fine otherwise; consider ES versions of subwoofer-install.
14. Hreflang covers only 30 of 196 URLs (the 15 EN/ES pairs); city and service pages have no ES alternate. Not an error.
15. Email address (Gmail) is published in text and schema on every page.

## 4. Strengths [mount-proxy]
- Complete Carson NAP and phone (310) 513-8800 on every page, consistent in text and schema.
- 109 city pages each with distance in miles, local street names, a 7-question FAQ with FAQPage markup that matches visible text (146 FAQPage pages; spot-checked 2 pages, 100% of answers visible).
- Honest "what we do not do" statements (no custom box fab, no mobile install).
- Review count 4.8 / 654 Google visible and consistent.
- Wide AI-crawler access with no WAF blocking on the hub.

## 5. Improvement plan for the subwoofer cluster (no page removed, merged or noindexed)
- `/beats/services/subwoofer-install/`: the install-process and price page. Add Carson to title/H1. Add answer-first block, sealed/ported table, install-time range, link to the other three pages.
- `/beats/services/amps-subwoofers/`: the "what to buy" page (matching amp to sub). Distinct angle: pairings (Kicker Comp 12 + CX1200 mono, L7 + amp), power/RMS table.
- `/beats/services/bass-amps-subwoofers/`: the wiring/quality-of-work page ("what you never see": fusing, gauge, ground). Rename H1 to reflect it.
- `/beats/shop/subwoofers/`: product listing. Add intro answer copy, fit guide, link back to install pages.
- Add `/beats/car-stereo-carson/` as an additional page (new page, nothing removed).

## 6. Prioritized list
Impact: google or ai. Effort: quick, medium, project. Tag: mount-proxy means verified on the hub copy only. No row is a removal, merge or noindex.

| # | Page | Problem | Report | Impact | Effort | Exact next step | Tag |
|---|---|---|---|---|---|---|---|
| 1 | /beats/ and /beats/es/ | Stray text `of class="hero-banner" BEFORE Pair with ... -->` prints in page body | AUDIT | google, ai | quick | Close the HTML comment in the hero partial so `-->` is not exposed; recheck view-source | [mount-proxy] |
| 2 | /beats/services/subwoofer-install/ | No Carson/South Bay in title, H1, or meta; no answer block | AI | google, ai | quick | Title "Car Subwoofer Install in Carson, CA \| LA Car Beats"; H1 "Car Subwoofer Installation in Carson, CA"; add 50-word answer under an H2 "How much does a car subwoofer install cost in Carson?" (draft in AI_SEARCH_REPORT) | [mount-proxy] |
| 3 | New /beats/car-stereo-carson/ (add) | Shop city has no page; only west-carson | AUDIT | google, ai | medium | Add page using the 109-page template plus real content: on-site shop photos, Avalon Blvd directions, 5 recent Carson-owner jobs | [mount-proxy] |
| 4 | 109 /beats/car-stereo-*/ pages | Opening says "we are not in X"; paragraphs repeat 2-3x; 24% shared sentences | AUDIT | google, ai | medium | Rewrite first 60 words as an answer (service, miles, what is done); delete in-page repeats; add 2 unique local paragraphs and 1 local vehicle example per page; do not remove any page | [mount-proxy] |
| 5 | City pages to subwoofer pages | 0 of 109 city pages link to subwoofer-install | AUDIT | google | quick | Add a "Subwoofer installs from {City}" link block to the city template linking subwoofer-install, amps-subwoofers, shop/subwoofers | [mount-proxy] |
| 6 | Schema on all pages | `@id` is hub `/beats/#business`; lacarbeats.com not in sameAs; no lacarbeats `@id` | SCHEMA | ai | medium | On the standalone, set the business `@id` to `https://www.lacarbeats.com/#business`, add url, `sameAs` to Google Maps/Yelp/YouTube and lacarbeats.com mount; verify against live www.lacarbeats.com first | [mount-proxy] |
| 7 | www.lacarbeats.com robots/sitemap/llms.txt | Cannot read; AI-crawler rules and sitemap unknown | AI | google, ai | quick | Allow www.lacarbeats.com in the egress proxy, then fetch and review robots.txt (Googlebot, OAI-SearchBot, PerplexityBot, ClaudeBot allowed), sitemap.xml, llms.txt | [standalone-verified] for the gap |
| 8 | /beats/services/subwoofer-install/ | No installed price range, install time, or sealed-vs-ported table; one box price only | AI | ai, google | medium | Add a 4-row sealed/ported/truck/SUV table with real ranges from Nick, install time, and a Service+Offer with price spec | [mount-proxy] |
| 9 | amps-subwoofers, bass-amps-subwoofers, subwoofer-install, shop/subwoofers | Overlapping topics, not linked together | AUDIT | google | quick | Give each a distinct H1 and a "related" block linking the other three (differentiate, keep all four) | [mount-proxy] |
| 10 | /beats/shop/subwoofers/ | No Product/ItemList JSON-LD; product detail lives on shop.lacarbeats.com (unverified) | SCHEMA | google | medium | Add ItemList of the 16 subs with name, brand, URL; add Product+Offer on the shop product pages once reachable | [mount-proxy] |
| 11 | City FAQ answers (146 pages) | Average answer is 34 words, none lead with the city + service + price fact | AI | ai | medium | Rewrite 2 of 7 FAQs per page as 40-80 word answers starting with the direct answer | [mount-proxy] |
| 12 | Home title and meta | No Carson/South Bay/subwoofer terms | AUDIT | google | quick | Title "Car Stereo, Subwoofer and CarPlay Install in Carson, CA \| LA Car Beats" (under 60 chars) | [mount-proxy] |
| 13 | 5 long titles | Over 60 chars | AUDIT | google | quick | Shorten Florence-Firestone, PV Estates, Rancho PV, Rolling Hills Estates, wireless-carplay titles | [mount-proxy] |
| 14 | /beats/locations/ (+ES) | 218 images without alt | AUDIT | google | quick | Add alt like "Car stereo install near {City}" per tile | [mount-proxy] |
| 15 | Home, ES home | "Closed today / hold Monday slot" baked into HTML | AUDIT | google, ai | quick | Render static hours server-side; show open/closed via JS | [mount-proxy] |
| 16 | Service and price pages | No visible last-reviewed date | AI | ai | quick | Add "Last reviewed {date}" near the $249 offer and specials | [mount-proxy] |
| 17 | Blog (3 posts) | Only 3 posts, none about subwoofer sizing or cost | AI | ai | project | Write "How to size a subwoofer box for a Silverado/Camry" and "Sub install cost in Carson" with author Zack and date | [mount-proxy] |
| 18 | https://lacarbeats.com/ | 308 to www; HSTS without includeSubDomains/preload | AUDIT | google | quick | Optional: add includeSubDomains and consider preload on the www response after checking all subdomains serve HTTPS | [standalone-verified] |
