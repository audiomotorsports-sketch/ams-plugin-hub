# AIO + GEO Addendum: audiomotorsports.com (hub)

Date 2026-10-04. Read-only. Addendum to AUDIT_REPORT, SCHEMA_REPORT and AI_SEARCH_REPORT (not repeated here). Every recommendation improves an existing page; nothing is removed, merged, redirected, canonicalized away or noindexed.

**Method (verified):** live fetches through the egress proxy of 61 hub URLs (home, services, brand hubs, hub city pages, brand city pages, FAQ, blog, reviews, utility), parsing robots meta, X-Robots-Tag, canonical, headings, JSON-LD (FAQPage, dates), visible text, lists and tables. Plus robots.txt per-bot evaluation and a 19-UA HTTP matrix. pages.csv was used for word counts (my own raw counts include inline CSS and are not used).
**Not measured:** Search Console index status and "Page indexing" reports, real AIO appearances/citations, GBP completeness, rankings. UA tests use spoofed UA strings from one IP; they cannot prove that real Googlebot/OAI IP ranges are not rate-limited or challenged by the WAF **[unverified]**.

---

## 1. AIO eligibility

AIO eligibility = indexed by Googlebot + snippet-eligible. Google-Extended does not affect AIO; llms.txt is not used by Google Search.

| Check | Result (verified) |
|---|---|
| robots.txt for Googlebot | One `User-agent: *` group: `Allow: /`, `Disallow: /admin/`, `/planner/`; sitemap declared. Googlebot may fetch everything public. (Python's robotparser reports /admin/ as allowed because it takes the first matching rule; Google uses the longest match, so /admin/ is blocked. Both are fine.) |
| HTTP status as Googlebot UA | 200 on `/`, `/tint/`, `/faq/`, `/llms.txt`. 59 of 61 sampled pages return 200 (the 2 others are below). |
| `noindex` (meta or X-Robots-Tag) | **None** on any of the 59 sampled 200 pages. No X-Robots-Tag header on any. (AUDIT_REPORT confirmed the same across all 1,057.) |
| Snippet directives | No `nosnippet`, `max-snippet`, `data-nosnippet` found in the sampled meta tags; one page (`/stereo/`) carries `index, follow` only. Default snippet and preview behaviour apply, so all sampled pages are snippet-eligible (59 of 59). `data-nosnippet` attributes in body HTML were not searched separately **[unverified]**. |
| Canonical | 59 of 59 self-referencing. |
| Server-rendered | Title, H1, headings, FAQ text and JSON-LD are all in the raw HTML. |
| Non-200 in sample | `/services/window-tinting/` 308 to `/tint/` (this URL is linked from llms.txt); `/tint/window-tint-carson/` 404 (my guess, no such page); `/carson/` 308 to `/locations/`. |

Sample by group (all eligible): home 1, services 10 (+1 redirect), brand hubs 6 (`/tint/ /tesla/ /beats/ /alarm/ /amspods/ /stereo/`), hub city pages 8 (Long Beach, Torrance, Gardena, Los Angeles, San Pedro, Redondo Beach, Compton, West Carson), brand city pages 6, FAQ 3 (`/faq/ /tint/faq/ /locations/`), blog 8, reviews 1, money/utility 14.

**Verdict:** no eligibility blocker. AIO citation is limited by passage quality, not access. Open eligibility items:
- **Index status is unconfirmed.** With ~1,090 URLs, many near-templated, Google may have "Crawled - currently not indexed" on some pages. Only GSC can confirm; check the Page indexing report for the city pages and the `/stereo/shop/` product pages. If pages show "Crawled - not indexed", the fix is differentiation (section 5), not removal.
- **Dynamic "Closed today. Text Nick now and we'll hold a Monday 9:30 slot for you." is the first text node on `/tint/`, `/tesla/`, `/beats/`, city and brand pages** (it differs by day). It is what a snippet extractor reads first, and it is time-dependent. Wrap it in `data-nosnippet` (or move it below the answer paragraph) so it is not used as the snippet.
- **Leaked developer comment visible on `/tint/`:** the rendered text contains `of class="hero-banner" BEFORE page-short (after you MOVE offer-cards) Pair with /assets/css/ams-plugin-tint.css -->` (a malformed HTML comment). It is in the opening hero text that crawlers read. Fix the comment markup on that template. (Found on `/tint/` in this sample; other brand hubs not found to have it.)

---

## 2. Answer-readiness

### 2a. Scorecard (sample of 61; money pages and city pages)

| Signal | Finding (verified) |
|---|---|
| FAQPage schema present | 38 of 59 pages. Questions and answers match the visible text on 30 (8 pages differ, listed next). |
| **FAQ schema/visible mismatches** | `/tint/all-services/` (2 Qs, 0 visible), `/tint/blog/california-70-vlt-fronts/` (9 Qs, 0 visible), `/alarm/blog/viper-vs-compustar/` (11 Qs, 0 visible), `/beats/brands-we-love/` and `/brands-we-love/` (1 Q, not visible), `/tesla/tesla-tint-carson/` (3 of 5 questions visible) and `/tesla/tesla-tint-torrance/` (4 of 5), `/faq/` (all 18 questions visible, but 13 of 18 schema answers are shortened paraphrases of the longer visible answer). Google requires structured data to reflect visible content. Parity is a trust issue, and AI engines read schema as well as text. |
| Question-style headings | Strong on `/faq/` (18 H2 questions), `/tint/faq/` (21), `/tesla/` and `/tesla` blogs (7), `/beats/`, `/alarm/`, `/amspods/` (8-12). **Weak where it matters:** hub and brand city pages have the FAQ questions in markup that is not a heading (1 question heading per page), so extractors do not see question-to-answer pairing; service pages (`/services/*`) have only a "Quick answers" H2 with 2 questions; home has 0; `/reviews/`, `/about/`, `/vehicles/`, `/specials/`, `/estimator/` have 0. |
| Answer-first (40-80 words directly under an H2/Q) | FAQ answers on brand hubs and service pages are 22-70 words (good). City-page FAQ answers are 100-125 words in the first two Qs (too long to quote whole; the answer starts with an address sentence). `/faq/` answers run 92-122 words for 5 of 18. Neither `/tint/`, `/tesla/`, `/beats/` nor the home has a plain 40-80 word "what/where/how much" paragraph as the first body text. The first body text is the "Closed today" banner, then a tagline. |
| Tables | **Zero `<table>` elements on any sampled page.** Prices, film comparison (Solar / Solar Ceramic / 3M IR / Color Stable), vehicle-by-vehicle Tesla prices and Viper vs Compustar are in cards or prose. |
| Ordered/unordered lists for steps or comparisons | Only `<ul>` for navigation/cards. One `<ol>` in the sample (`/stereo/`). No "how it works / what to expect" step lists on service pages. |
| Freshness dates | Visible "verified September 2026" only on `/faq/`, `/tint/faq/`, `/tesla/`, `/specials/`. No visible "Last updated" on `/tint/`, `/beats/`, `/alarm/`, `/amspods/`, services, city pages. JSON-LD `dateModified` on 1 page in the sample (`/payment-plan/`, 2026-09-22). `datePublished` on blog posts is 2026-08. **`/tesla/tesla-tint-carson/` says datePublished 2023-06-09 and `/tesla/tesla-tint-torrance/` 2019-09-27** (not plausible for these pages, no dateModified). |
| Prices | Visible and consistent on `/tint/` ($249 Solar, $329 Solar Ceramic, $149 fronts), `/tesla/` (promo $149/$299 vs "Matrix" $189/$369 in adjacent text, which a model can quote inconsistently), city pages. `/faq/` question "Do you publish prices online?" answers with the locked specials (good), but the page `<meta description>` still says no public prices (AUDIT_REPORT item 10). |
| Service schema | `Service` + `Offer` on brand hubs and `/services/*` (not on city pages, blog or `/tint/faq/`). |
| People / first-hand | Zack and Nick named on nearly every page. Alex (3M certified tinter), Richard (since 1998), Albert only on `/about/`. Blog posts have no visible byline. Reviews on `/reviews/` have no dates; city pages have dated Yelp quotes (e.g. "Jun 14 2026"). |

### 2b. Top money pages, page by page

| Page | Issue for AIO | Improve by |
|---|---|---|
| `/` (256 words) | Title "Audio MotorSports \| Carson Shop", H1 "Pick a skill", no FAQPage, no Service nodes, thinnest entity schema. Nothing quotable. | Add a 50-70 word answer paragraph under a real H1 ("Car audio, window tint, car alarms and Harley bagger audio in Carson, CA"), 5 question headings with FAQPage, and the homepage entity node (SCHEMA_REPORT 1). |
| `/tint/` | Best page for tint queries. Title says "LA & Long Beach" and does not say Carson. Prices in cards. First text is banner plus leaked comment. 11 FAQs match visible text. | Add a 60-word paragraph under the H1: what is included, price, time, location (Carson). Add a price/film comparison `<table>`. Add "Last updated" next to the prices. Fix the leaked comment. Add Carson to the title. |
| `/tint/faq/` | Excellent (20 Qs, answers 26-95 words, 20/20 visible). | Add "verified" date to the JSON-LD (`dateModified`) and a visible Last updated. Trim the one 95-word answer to about 70. |
| `/tesla/` | Strong FAQ (7/7 parity). Promo vs Matrix price text is confusing. No table for Model 3/Y/S/X/Cybertruck by film. | Add one `<table>` (model x film x install price), label which price is the standing price vs the limited promo, add the "verified" date next to it. |
| `/tesla/tesla-tint-carson/` | Title and H1 say "Avalon", not Carson (same issue noted on teslatintla.com). FAQ schema has 2 questions not visible. datePublished 2023. | Retitle/H1 to "Tesla window tint in Carson, CA" and make visible FAQ match schema (or schema match visible). Fix the date, add dateModified. |
| `/beats/`, `/alarm/`, `/amspods/` | Good FAQ parity (9/8/9 Qs), prices in cards, no table, no Last updated. | Add a package/price `<table>` and a dated line; Viper vs Compustar comparison table on `/alarm/`. |
| `/services/*` (9 pages) | Only 2 FAQs each, one question heading, no price on page (prices only in llms.txt). `/services/dash-camera/` and `/services/dash-cameras/` are two live pages with the same topic. | Add a 50-70 word answer-first intro per service, 4-6 more question headings with FAQ answers, a "what is included / time / price from" `<table>` or list, and a numbered "how the install goes" list. Differentiate the two dash-camera pages (one Thinkware-specific, one general buyer's guide) with their own questions and cross-link. |
| `/faq/` | Best citable page (18 Qs). 13 of 18 schema answers are paraphrases of the visible answer. 5 visible answers are over 90 words. | Make schema answer text equal the visible answer (or lead the visible answer with the schema answer). Put a 40-60 word answer first and the detail after. |
| `/reviews/` | 306 words, no `Review` dates, 4.8/654 stated. | Add dates and vehicle/service to each quote, show the "as of" date for 654/777, mark up with `Review` only for quotes shown on the page. |
| `/locations/` | 10 FAQs, parity fine. | Fine; add a table of drive time by city group (data already exists in `data/drive-in-cities.json`). |
| Blog (4 hub posts + brand blogs) | 235-548 words, no byline, FAQ schema on two posts with no visible FAQ. | Add byline and dated "reviewed by" (Alex for tint, Nick for alarm/stereo); show FAQ text visibly; add a 60-word answer at the top. |

### 2c. City pages (sample: 8 hub, 6 brand city)

Verified structure (`/torrance/`, `/tint/window-tint-torrance/`, `/alarm/car-alarm-torrance/`): H1 "{Service} for {City}", H2s "Same bay", "Five-star notes", "FAQ", "Coming from {City}?". The first FAQ is "Are you in {City}? No." and "How do I drive..." with drive miles and minutes, then price answers. Dated Yelp quotes appear (good first-hand signal). Strengths: honest answer to "are you in X", real drive time/miles, price, same visit stereo/tint/alarm. Weaknesses for AIO:
- FAQ answers 106-125 words each, starting with the pin sentence; a query like "window tint torrance" gets the address, not the answer. Lead each answer with a 40-60 word direct answer.
- Question phrasing repeats "if I drive from {City}" in 7 of 10 questions, so every city page has near-identical question headings. Vary by what is different per city: named freeway route and exit, drive time at rush hour, typical vehicles from that area, one local review.
- No table or list of "route and drive time" (data exists), no "Last updated".
- `/tesla/tesla-tint-carson/` and the `/tesla/` city pages are titled "Tesla Window Tint {City}"; for Carson the text says Avalon.
- There is no hub or tint page whose job is "Carson". The shop is in Carson but the hub has `/west-carson/` and `/carson/` redirects to `/locations/`. `/tint/`, `/beats/`, `/alarm/` and `/tesla/tesla-tint-carson/` have to carry Carson (see section 5).

---

## 3. Entity and E-E-A-T signals (verified unless marked)

| Signal | State | Gap / improvement |
|---|---|---|
| NAP | Name "Audio MotorSports", `22025 S Avalon Blvd Ste A, Carson, CA 90745`, +1 310 513 8800, identical across sampled home, brand and city JSON-LD and visible text. Text line (213) 429-1092 is in visible copy and llms.txt, not in schema as a second `ContactPoint`. | Add `contactPoint` with the text line. Home node still lacks `sameAs`, `geo`, `areaServed` (SCHEMA_REPORT 1). Entity name: the footer and hub schema say "Audio MotorSports", llms.txt says "Audio MotorSports Inc". Pick the GBP name and use it everywhere. |
| sameAs | City pages: YouTube, Instagram, Facebook, TikTok, Yelp (`yelp.to` shortlink), Google Maps ftid, `share.google` link, plus five sister domains. Homepage: none. | Put the full list on the home node. Replace `yelp.to` shortlink with the canonical Yelp business URL. Add the Google `hasMap` as a full maps.google.com place URL. |
| GBP | Linked via ftid and share.google. Completeness, categories, review responses, and whether the GBP name/phone/website match are **[unverified]**. | Manual check in GBP; make the GBP primary category and services list match the page vocabulary (tint, car stereo, car alarm, remote start). |
| Named people | Zack (Operational Manager), Nick (sales since 1992), Alex (3M Certified Tinter), Richard (since 1998), Albert, named on `/about/`; Zack and Nick on most pages. `Person` schema appears on ~all city pages for Zack/Nick only. | Add `Person` nodes with `jobTitle`, `knowsAbout` and `worksFor` for Alex and Richard. Add a visible byline and reviewer on blog and service pages. |
| Experience claims | "20+ years", "Since 2003" (tint hub), "3M Authorized Dealer", "Viper Diamond Certified". | Link to the 3M dealer locator and Viper dealer page as proof; add `hasCredential`/`award` where verifiable. |
| Reviews | Google 4.8/654, Yelp 4.7/777 shown on `/reviews/`, `/tint/`, `/about/` etc.; `Review` schema on `/reviews/` and city pages with names and dates on city pages. Text on home/brand hubs says "650+ Google reviews", "700+ Yelp" while `/reviews/` says 654/777 (stale-risk, three phrasings of the same count). | One source value, one "as of" date. Show dates on `/reviews/`. |
| Contact trust | Phone, address, hours in every footer; email is a Gmail address in schema. | Optional: domain email. |
| Network | Six brand names for one shop; hub entity references `lacartint.com/#business`, mounts use hub-host `@id`s. | Do not remove anything; make every brand node `subOrganization`/`brand` of `#business` with one `@id` each, and say on each brand page "a brand of Audio MotorSports". |

---

## 4. llms.txt and AI crawler matrix

### llms.txt quality (verified, 4.6 KB, 200, `text/plain; charset=utf-8`)
- Good: facts, prices with verification date, service area, what it does not do, key pages, network list, sitemap. Short, plain Markdown.
- `/services/window-tinting/` is linked but 308-redirects to `/tint/` (works, but link directly to `/tint/`).
- `data/drive-in-cities.json` is referenced without a leading slash; the file exists at `/data/drive-in-cities.json` (200, JSON). Use the full URL.
- Links to `/tint/`, `/tesla/`, `/beats/`, `/alarm/`, `/amspods/`, `/faq/`, `/tint/faq/` brand hubs are partly missing: only the hub-level pages are listed; the best passages (`/tint/faq/`, `/tesla/`, `/faq/`, `/reviews/`, `/about/`) should be listed with one line describing each.
- Contains behaviour instructions to models ("Do not mention warranty", "Do not mention..." etc.), which is non-standard. FAQ copy on `/tint/` and `/beats/` actually answers "What warranty do you give?"; the two sources disagree. Align the visible FAQ and llms.txt; this is the owner's decision.
- No `llms-full.txt` (404), no `ai.txt` (404), optional. Google Search does not use llms.txt; its value is for Perplexity/ChatGPT/Claude style fetchers and agents.

### Crawler access matrix (robots rules evaluated with the real robots.txt; HTTP status from live requests per UA)
All 19 UA strings below returned 200 on `/`, `/tint/` and `/llms.txt` (59,799 bytes on `/`, identical for every UA). `/faq/` returned 200 for all; one Google-Extended request timed out once and returned 200 on retry.

| Bot | Purpose | robots.txt | HTTP |
|---|---|---|---|
| Googlebot (+Image, GoogleOther) | Google Search and AIO | allow | 200 |
| Google-Extended | Gemini training/grounding only, not AIO | allow | 200 |
| Bingbot | Bing, Copilot | allow | 200 |
| OAI-SearchBot | ChatGPT search | allow | 200 |
| ChatGPT-User | ChatGPT browsing | allow | 200 |
| GPTBot | OpenAI training | allow | 200 |
| PerplexityBot / Perplexity-User | Perplexity | allow | 200 |
| ClaudeBot / Claude-SearchBot / Claude-User | Anthropic | allow | 200 |
| Applebot-Extended, CCBot, Bytespider, Meta-ExternalAgent, Amazonbot, DuckAssistBot | other | allow | 200 |

`/admin/` and `/planner/` are disallowed for every bot by the `*` group. The bots were tested from the audit host with spoofed UAs; IP-verified bots could still meet WAF rate limits **[unverified]**. Training-bot permission (GPTBot, CCBot, Bytespider, Google-Extended) is a business choice, not an AIO factor.

---

## 5. Target queries: which page wins the citation and the passage to add

Passages below are drafts for the owner to verify before publishing (price, hours and film names come from llms.txt and visible pages; confirm they are still true on the day).

| # | Query | Page that should win | Why / gap | Passage to add (answer-first, 40-80 words) |
|---|---|---|---|---|
| 1 | window tint carson ca | `/tint/` | Shop is in Carson but title says "LA & Long Beach"; no hub page or heading says Carson tint. | Under the H1: "Audio MotorSports tints cars in Carson, CA at 22025 S Avalon Blvd Ste A. A four-door sedan with Solar film starts at $249 installed (doors and back glass, no windshield); Solar Ceramic starts at $329. Film is hand-cut on a glass board, takes about 2-3 hours, and 3M is a quote-only line. Walk in Mon-Sat 9:30-6." |
| 2 | car audio shop torrance | `/torrance/` (hub city) with `/beats/car-stereo-torrance/` as the stereo-specific page | Hub page leads with a generic "Worth the drive" banner; question headings are not headings. | "Audio MotorSports is a car audio shop 4.4 miles from Torrance, in Carson. We install Apple CarPlay and Android Auto head units, speakers, amps, subs and DSP in-house. Most installs finish the same day. From Torrance take the 405 to Avalon; allow 10-15 minutes. Text the year, make and model to (213) 429-1092 for a quote." |
| 3 | tesla window tint cost los angeles | `/tesla/` | Prices are in cards and mix promo and "Matrix" figures; no table. | A table: Model (3, Y, Y L, S, X, Cybertruck) x scope (two fronts / doors + back / full) x film (Solar Ceramic, 3M IR) = install price, with "verified {date}". Lead paragraph: "Tesla window tint at Audio MotorSports starts at $149 for two front windows on a Model Y (promo; standing price $189) ...", labeled promo vs standard. |
| 4 | how much does ceramic window tint cost | `/tint/` (price section) | Price present, no comparison. | Table: Solar ($249), Solar Ceramic ($329), 3M Ceramic IR and Color Stable (quote), what is covered, heat/UV difference, time. Intro sentence: "Ceramic tint for a four-door sedan starts at $329 installed at Audio MotorSports..." |
| 5 | is 70 percent tint legal in california / california front window tint law | `/tint/blog/california-70-vlt-fronts/` | FAQ schema (9 Qs) has no visible FAQ; no byline or date shown. | "California requires front side windows to let at least 70% of visible light through (70% VLT). Rear side and back windows may be darker. Windshield film is limited to a strip at the top. We install fronts to 70% and write the shade for the rears before the car goes in." Show the 9 questions visibly; add a byline and "Updated" date. |
| 6 | how long does window tint take | `/tint/faq/` | Already good (37 words). | Add `dateModified` and a visible "Last updated". Optionally a one-line list: sedan 2-3 hours, SUV 3-4, windshield extra, cure 3-5 days. (Use only figures the shop confirms.) |
| 7 | hand cut vs computer cut tint | `/blog/hand-cut-vs-computer-cut-tint/` | 342 words, no FAQ, no byline, no table. | Add a top paragraph: "Hand-cut tint is trimmed on the glass to the exact window; computer-cut uses a plotter pattern. We hand-cut every panel on a glass board." Add a 2-column comparison table (edge gap, glass fit, time, who it suits), 3 FAQs with schema, and a byline (Alex, 3M Certified Tinter). |
| 8 | remote start installation los angeles | `/services/remote-start/` | 2 FAQs, no price, no steps. | "Audio MotorSports installs Compustar remote start in Carson. A typical car is $499 installed (Compustar 9910, most cars). We use the vehicle-specific bypass module, program it, wire brake/hood/in-gear lockouts and test cold and warm starts. Add DroneMobile or Viper SmartStart for phone control." Then a numbered "what happens at the install" list. |
| 9 | viper vs compustar | `/alarm/blog/viper-vs-compustar/` and `/faq/` ("Compustar vs Viper — which alarm?") | Blog has 11 FAQ schema Qs not visible; 248 words. | 60-word verdict plus a comparison table (range, app, brands, price from, who it fits). Show the Qs visibly. |
| 10 | dash cam install near me / hardwire dash cam carson | `/services/dash-cameras/` and `/services/dash-camera/` | Two pages cover the topic; only 2 FAQs, no price or time. | "We hardwire dash cameras into the fuse box with a low-voltage cutoff so parking mode will not drain the battery. Camera sits behind the mirror, cable runs under the headliner and A-pillar. [price from, time]." Give each page a different intent (Thinkware model page vs general hardwire guide) and cross-link. |
| 11 | harley bagger speakers install los angeles | `/amspods/` | Good FAQ (9), no table. | Table: Road Glide/Street Glide/Ultra x pod pair x starting price ($649 pair, per llms.txt) x install time. Add 60-word intro: "AMS Pods are made in house since 2003 ...". |
| 12 | apple carplay install carson / add carplay without replacing screen | `/beats/` | FAQ "Can you add CarPlay without replacing my screen?" exists. | Give that Q a visible heading and a 50-word answer first, then detail. Add a "what you keep" list (steering controls, backup camera, factory features). |
| 13 | do you need an appointment for window tint / window tint near me open now | `/tint/` and `/contact/` | First text on page is a dynamic "Closed today" banner. | Static line: "Walk-ins welcome Monday to Saturday 9:30-6, closed Sunday. For tint, book a 10:00 AM or 12:00 PM slot." Use `data-nosnippet` on the dynamic banner. |
| 14 | tesla tint carson | `/tesla/tesla-tint-carson/` | Title/H1 say Avalon; FAQ partly invisible. | "Tesla Tint LA is the Tesla window tint side of Audio MotorSports at 22025 S Avalon Blvd Ste A, Carson. Model 3, Y, Y L, S, X and Cybertruck. Two front windows from $149 (promo)..." Retitle to "Tesla Window Tint Carson, CA". |
| 15 | car window tint long beach | `/long-beach/` (hub) and `/tint/window-tint-long-beach/` | 112-word answers lead with the pin sentence. | Lead with: "Audio MotorSports is not in Long Beach; we are 12 miles north in Carson (take the 710 to 405 to Avalon, about 20 minutes). Sedan tint starts at $249 installed." (confirm distance from the page's own number). |

---

## SUPERSEDED RECOMMENDATIONS (exclude; they conflict with RULES.md)

From AUDIT_REPORT.md:
- Finding 1 "Next step: ... canonicalize the other, or noindex the mounts, and remove them from the sitemap" (the ~775 mounted copies).
- Finding 2 "Next step: collapse to one canonical per service ... and canonical the mounts to it".
- Finding 6 "noindex cart, enrich or consolidate product pages" (the **consolidate** part and any noindex of `/stereo/shop/*`; enrich is fine. Cart noindex is not a city page, but it was bundled with consolidation, so confirm separately.).
- Finding 7 "keep pages that carry real local detail ... consolidate the rest" (city pages).
- Finding 5: removing the 33 redirecting `/shop/` URLs from the sitemap is not a page removal and stays valid.

From SCHEMA_REPORT.md:
- Issue 2 "one `@id` per brand, on its canonical host": acceptable only as an entity-graph fix (reference one `@id`); not as a reason to drop either host's pages.
- Issue 3 "or move to the shop host": drop that alternative; add Product/Offer to the pages.

From AI_SEARCH_REPORT.md:
- Recommendation 1 "Resolve duplicate/mounted-site entity structure so each brand has one canonical host": rephrase as "unify `@id` and entity naming; differentiate duplicated copy". No removal or canonical swap.

From FIX_LIST.md:
- #28 "Point the mounts' rel=canonical at [hub /services/...]" (canonical-ing to drop from search).
- #36 "Canonical or noindex the mounted copies".
- #37 "Canonical or noindex the mirrors".
- #38 "or consolidate to the shop host".
- #40 "Merge or 301 the far-out ones" (teslatintla.com city pages).
- #41 "Consolidate or noindex the rest" (hub and per-brand city pages) and the "Consolidate the rest" line in the strategy section (line 79).
- Open decision #4 "Decide the canonical-host question for the mounted brand copies": reframe as differentiating the two copies; do not canonical either away.
- #18 (lacarstereo.com "Merge into #business, delete the duplicate block") is a schema-node merge, not a page removal; fine to keep.
- #1/#2 (remove lacarstereo.com noindex) are consistent with the rules; keep.

---

## Prioritized list

```json
[
  {"page":"/tint/","problem":"Leaked developer comment text in the hero ('BEFORE page-short ... ams-plugin-tint.css -->') and dynamic 'Closed today' banner is the first text a snippet extractor reads","report":"AIO","impact":"google","effort":"quick","next_step":"Fix the malformed HTML comment in the tint hub template; add data-nosnippet to the 'Closed today' banner on /tint/, /tesla/, /beats/, /alarm/ and city pages"},
  {"page":"/tint/","problem":"No answer paragraph, title omits Carson, no price/film table, no visible update date","report":"AIO","impact":"google|ai","effort":"quick","next_step":"Add a 60-word paragraph under the H1 (passage #1), a Solar/Solar Ceramic/3M comparison <table>, a 'Last updated' next to prices, and 'Carson' in the title"},
  {"page":"/tesla/tesla-tint-carson/","problem":"Title and H1 say 'Avalon', 2 of 5 FAQ schema questions not visible, datePublished 2023-06-09 with no dateModified","report":"AIO","impact":"google|ai","effort":"quick","next_step":"Retitle/H1 to 'Tesla Window Tint Carson, CA', make visible FAQ match schema, correct datePublished and add dateModified"},
  {"page":"/tesla/","problem":"Promo ($149/$299) and 'Matrix' ($189/$369) prices adjacent; no table by model and film","report":"AIO","impact":"ai","effort":"quick","next_step":"Add one table (model x scope x film x installed price) and label standing vs promo price with a verified date (passage #3)"},
  {"page":"/tint/blog/california-70-vlt-fronts/, /alarm/blog/viper-vs-compustar/, /beats/brands-we-love/, /brands-we-love/, /tint/all-services/","problem":"FAQPage schema (1-11 Qs) with no matching visible text","report":"AIO, SCHEMA","impact":"google|ai","effort":"quick","next_step":"Render the FAQ questions and answers visibly (or remove the unmatched schema entries); keep text identical to schema"},
  {"page":"/faq/","problem":"13 of 18 schema answers are shortened paraphrases of visible answers; 5 visible answers are 92-122 words","report":"AIO","impact":"ai","effort":"quick","next_step":"Set schema answer = visible answer; start each visible answer with a 40-60 word direct answer"},
  {"page":"/","problem":"256 words, no answer passage, no FAQ, no Service schema, thinnest entity node","report":"AUDIT, SCHEMA, AIO","impact":"google|ai","effort":"medium","next_step":"New H1 and 50-70 word answer paragraph, 5 question headings with FAQPage, copy city-page AutoRepair node (geo, sameAs, areaServed, priceRange, contactPoint) into home JSON-LD"},
  {"page":"/torrance/, /long-beach/, /gardena/, /los-angeles/, /san-pedro/, /redondo-beach/, /compton/ and all other hub city pages","problem":"FAQ answers 106-125 words lead with the address; questions not headings; 7 of 10 questions repeat 'if I drive from {City}'; no route/drive-time table","report":"AIO","impact":"google|ai","effort":"project","next_step":"Template change: question headings as H3, 40-60 word direct answer first, then detail; vary questions with city-specific route, drive time, nearest freeway exit and a dated local review; add a route/drive-time table from data/drive-in-cities.json"},
  {"page":"/services/remote-start/, /services/dash-cameras/, /services/dash-camera/, /services/gps-tracking/, /services/backup-cameras/, /services/tint-removal/, /services/door-actuators/, /services/fleet-asset-protection/, /services/diagnostics-checkout/","problem":"Only 2 FAQs and one question heading each; no price/time/steps; dash-camera and dash-cameras overlap","report":"AIO","impact":"google|ai","effort":"medium","next_step":"Add 50-70 word answer intro, 4-6 question headings with FAQ, a 'from price / time / included' table and a numbered install-steps list per page; differentiate /dash-camera/ (Thinkware) vs /dash-cameras/ (buyer guide) and cross-link"},
  {"page":"/beats/, /alarm/, /amspods/","problem":"Good FAQs and prices in cards but no comparison tables, no visible Last updated","report":"AIO","impact":"ai","effort":"medium","next_step":"Add package/price tables (Viper vs Compustar, CarPlay upgrade options, AMS pod pair by bike), plus a 'Last updated' date"},
  {"page":"/reviews/","problem":"306 words, undated quotes, 654/777 counts without an as-of date; home/brand pages say '650+'/'700+'","report":"AIO","impact":"ai","effort":"quick","next_step":"Add dates and vehicle/service to each quote, 'as of' date next to 654/777, use the same count wording everywhere"},
  {"page":"/blog/*, /tint/blog/*, /tesla/blog/*, /alarm/blog/*, /beats/blog/*","problem":"235-548 words, no byline or reviewer, no top answer paragraph","report":"AIO","impact":"ai","effort":"medium","next_step":"Add a visible byline and 'Reviewed by' (Alex for tint, Nick/Richard for stereo/alarm), a 60-word answer at the top and a Person node in BlogPosting.author"},
  {"page":"/llms.txt","problem":"Links to a 308 URL (/services/window-tinting/), relative data path, best passages (/tint/faq/, /tesla/, /reviews/, /about/) not listed, contradicts visible warranty FAQ","report":"AIO, AI","impact":"ai","effort":"quick","next_step":"Link /tint/ directly, use /data/drive-in-cities.json, list the best passages with one-line descriptions, align warranty statement with the visible FAQ (owner decision)"},
  {"page":"/tint/window-tint-torrance/ and other brand city pages (/tint, /alarm, /beats, /tesla, /amspods)","problem":"Same long-answer and repeated-question pattern; Tesla city pages have 2019/2023 datePublished","report":"AIO","impact":"google|ai","effort":"project","next_step":"Apply the hub city template changes; correct datePublished and add dateModified in the JSON-LD generator"},
  {"page":"Site-wide JSON-LD (Service pages, city pages)","problem":"No dateModified on almost all pages (1 in the sample); no visible Last updated","report":"AIO, SCHEMA","impact":"google|ai","effort":"medium","next_step":"Emit dateModified from a per-page content date in the template and show 'Last updated {date}' beside prices and FAQs"},
  {"page":"/about/","problem":"Team section names Alex, Richard, Albert but schema Person only for Zack and Nick","report":"AIO, SCHEMA","impact":"ai","effort":"quick","next_step":"Add Person nodes (jobTitle, knowsAbout, worksFor #business) for Alex and Richard; link credentials (3M dealer, Viper) to proof URLs"},
  {"page":"Google Search Console (all sampled URL groups)","problem":"Index status of city pages and /stereo/shop/ products not verified; AIO eligibility depends on being indexed","report":"AIO","impact":"google","effort":"quick","next_step":"Check Page indexing for the hub city pages and /stereo/shop/*; if 'Crawled - not indexed', add the differentiation above (unique local content, answer-first FAQs, schema, internal links) rather than removing pages"}
]
```
