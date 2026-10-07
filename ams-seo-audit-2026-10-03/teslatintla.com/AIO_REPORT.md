# AIO + GEO Addendum: teslatintla.com

Date: 2026-10-04. Read-only. Companion to AUDIT_REPORT.md, AI_SEARCH_REPORT.md, SCHEMA_REPORT.md (not redone here). Applies RULES.md: AIO = Google AI Overviews; every city page stays live and is improved, never trimmed, merged, canonicalised away or noindexed.

## 0. Evidence and limits

- Fetched via curl through the egress proxy: robots.txt, llms.txt, sitemap.xml, and all 143 sitemap URLs (headers + HTML). Detailed parse: home, 8 blog posts, locations, about, contact, gallery, all-services, payment-plan, book, privacy, terms, and all 124 city pages for indexability flags; 23 city pages read in depth (the 15 named below plus 8 extras: Bradbury, Hacienda Heights, Monterey Park, Pacific Palisades, South Gate, Temple City, Downey, West Los Angeles). 42 pages sampled in depth in total.
- Connection was flaky (several "connection reset"/timeouts); each failed request was retried (up to 4) and succeeded.
- Limitation: www.teslatintla.com is blocked by the egress proxy (403). Not bypassed. www to apex redirect behaviour is UNVERIFIED (also noted in AUDIT_REPORT.md).
- UNVERIFIED (no access): Search Console index coverage, actual AIO appearance for any query, rankings, GBP, real Googlebot IP behaviour (my UA tests use the UA string only, from a non-Google IP, so a Vercel bot rule keyed on IP/verified-bot status would not be exercised).
- The 12 "winning page" mappings in section 7 are editorial recommendations, not observed AIO results.

## 1. AIO eligibility (Googlebot access, snippets, indexability)

Google's AIO eligibility = indexed + snippet-eligible. Checked on all 143 URLs (headers and HTML):

| Check | Result (evidence) |
|---|---|
| robots.txt for Googlebot | `User-agent: *` / `Allow: /`, no Disallow anywhere; Googlebot has no specific group so `*` applies. Not blocked. |
| HTTP status as Googlebot UA | 200 on /, /tesla-tint-torrance/, /robots.txt, /llms.txt; identical body size to curl UA (47,239 B home; 36,420 B Torrance), so no UA-based cloaking or block |
| Meta robots | 0 of 143 pages have a robots meta tag, so defaults apply (index, follow, full snippets) |
| X-Robots-Tag header | 0 of 143 |
| nosnippet / max-snippet / data-nosnippet | 0 of 143 (searched HTML and headers) |
| Canonical | Self-referencing apex, trailing-slash on sampled pages; no cross-page canonicals (consistent with RULES.md: none should be added) |
| Sitemap | 143 URLs, all 200 (Spanish /es/ URLs still absent; see AUDIT_REPORT) |
| Rendering | Server-rendered HTML; price and FAQ copy present in raw HTML, no JS needed |
| 404 behaviour | Real 404 + noindex for unknown URLs (from AUDIT_REPORT) |

Verdict: all 143 pages are technically AIO-eligible. No eligibility blocker found. Whether Google has actually indexed the 124 city pages is UNVERIFIED (check GSC Pages report and URL Inspection "Indexed" status). The ranking constraint is content quality and differentiation, not access.

Google-Extended: allowed in robots.txt, but it controls Gemini training/grounding only. It has no effect on AI Overviews or Search, so its Allow line is harmless but irrelevant to AIO.

## 2. Answer-readiness

### 2.1 Homepage
- Strong: 7 question-form FAQ headings (models, GPS signal, Model Y duration, windshield, payment plan, appointment, overnight). Answers are 28 to 45 words, self-contained, with entity and facts. FAQ schema matches visible questions 7/7.
- Gap: opening passage is "Ceramic tint. LA price." (4 words), not an answer-first definition. No "Tesla window tint cost" question heading even though price is the money query.
- Gap: price matrix on the homepage lives in offer cards and a JS simulator. 0 `<table>` elements. Sample promo cards ($149 Model Y fronts, $299 Model 3 six windows, $199 Cybertruck four windows) conflict visually with matrix numbers; the page explains it, but extraction can pick the wrong figure. A single dated HTML table fixes this.
- Date: "Prices verified September 2026" exists in llms.txt but not as a visible, dated line on pages I parsed.

### 2.2 Pricing content
- Prices are published everywhere as plain sentences with middots ("Model Y $349 · Model 3 $369 · ..."). Good facts, poor structure: 0 tables on all 143 pages (home, 124 city, 8 blog).
- Repeated verbatim as a "Installed Tesla tint prices" block with 3 cards (two fronts, doors+back, windshield) on city pages and as a 107-word FAQ answer on template-A city pages. Consistent numbers (no conflicts found between llms.txt, home, blog, city pages in sampled text).
- Price table gap: needed table columns = Model | Two fronts | Doors+back | Windshield | Full with windshield, rows per film (Solar Ceramic, 3M IR Ceramic), with a visible "Prices verified {Month Year}" line. Source numbers are already on the site.

### 2.3 Blog (8 posts, 1,186 to 1,794 words)
- 6 model posts: 7 question headings each, FAQPage parity 7/7. First paragraph is a price line ("Solar Ceramic doors + back $349. Windshield $189."), good for "how much" queries but not a full sentence naming the car and shop.
- 2 comparison posts (3M vs XPEL, 3M vs Llumar IRX): 0 FAQ/question headings, answer-first sentence is present ("This bay is a 3M shop. We do not run XPEL").
- Dates: BlogPosting has datePublished (2026-08-22 to 2026-09-26) but dateModified only on Model Y L; no visible "Updated" line; 0 `<time>` elements.
- Author: schema author is the Organization; no Person, no byline, no bio link. Page body mentions "Nick" only. About page shows "3M Certified Tinter" and "20+ years" text, which should be tied to the posts.
- Outbound sources: none to 3M spec sheets or California Vehicle Code 26708 in sampled posts.

### 2.4 Fifteen sample city pages
Two templates exist across the 124 pages (counted from fetched HTML): template A (55 pages) says "Tesla window-tint side of Audio MotorSports", 5 FAQs, Review/AggregateRating markup; template B (69 pages) says "Tesla glass side", 9 to 11 FAQs, `LocalBusiness`+`AutoRepair` nodes, and puts the route, miles and minutes in the opening paragraph.

| Page | Tpl | Words | Opening passage | Drive info in lead | Question headings | FAQ in schema / visible match | HTML price table | Dates | Author |
|---|---|---|---|---|---|---|---|---|---|
| carson | A | 2113 | "The bay is on Avalon... You are already on Avalon." | n/a | 1 (FAQ) | 5 / 3 of 5 questions match text | No | None | "Nick" first name |
| torrance | A | 2178 | "We are not in Torrance... One bay. One map pin." | No (4.4 mi, 10-15 min only in later section) | 1 | 5 / 4 of 5 | No | None | "Nick", "Zack" |
| long-beach | A | 2452 | same pattern | No | 1 | 5 / 4 | No | None | same |
| los-angeles | A | 2032 | same pattern | No | 1 | 5 / 4 | No | None | same |
| gardena | A | 2094 | same pattern | No | 1 | 5 / 4 | No | None | same |
| redondo-beach | A | 2096 | same pattern | No | 1 | 5 / 4 | No | None | same |
| san-pedro | A | 2031 | same pattern | No | 1 | 5 / 4 | No | None | same |
| compton | A | 2413 | same pattern | No | 1 | 6 / 4 | No | None | same |
| irvine | A | 1995 | "27 miles. About 38 minutes" | Yes | 1 | 5 / 4 | No | None | same |
| brea | A | 1949 | "21.8 miles. Thirty-five to forty-five minutes on the 57 south to the 91 west" | Yes | 1 | 5 / 4 | No | None | same |
| anaheim | A | 2044 | "22 miles. About 32 minutes" | Yes | 1 | 5 / 4 | No | None | same |
| malibu | A | 1970 | "32.6 miles. Fifty to seventy-five minutes on PCH..." | Yes | 1 | 5 / 4 | No | None | same |
| pasadena | B | 2243 | "28.6 miles, forty to fifty minutes" via Colorado Blvd / 110 | Yes | 1 | 11 / 11 | No | None | none visible |
| santa-monica | B | 1981 | "18.4 miles, thirty-five to forty minutes" | Yes | 1 | 10 / 10 | No | None | none |
| rancho-cucamonga | B | 2011 | "53.6 miles, sixty to seventy-five minutes" | Yes | 1 | 10 / 10 | No | None | none |

Findings:
1. The 4-of-5 pattern on template A is a FAQ parity defect: the schema question "Can I get a stereo or alarm on this Tesla Tint LA page?" differs from the visible heading "...on this site?". On Carson, "Where is Tesla Tint LA?" is in schema but not found as visible text. Parity matters because FAQ markup should mirror visible content. Template B pages match 100%.
2. Answer-first: the first 60 words of template-A pages for near cities contain no answer ("One bay. One map pin."). Template-B and far-city template-A pages state miles and minutes, which is the quotable passage for "is there a Tesla tint shop in X / how far".
3. Question headings: each city page has exactly 1 heading ending in "?" (the "Coming from X?" heading or the FAQ) because the FAQ questions are rendered as non-heading text. Convert the FAQ questions to `<h3>` so AIO sees them as question headings.
4. Local uniqueness: unique per page = drive time, route streets, a one-line heat/climate note on some (e.g. Pasadena "no marine layer"), nearby city links. Missing: landmarks, neighborhoods, vehicle examples, local scenario. Local-FAQ questions are mostly "from {City}" substitutions of the same 4 questions.
5. Price block: duplicated on every page, no table, no date.
6. Carson page: title/H1 say "Avalon" (see AUDIT_REPORT 3); this is the page that should answer "ceramic tint Carson CA".
7. Dates and author: no visible date or author on any city page. Only the footer "Ask for Nick".

## 3. Entity and E-E-A-T consistency

- Consistent: NAP identical on 143/143 pages (22025 S Avalon Blvd Ste A, Carson CA 90745; (310) 513-8800; Mon-Sat 9:30-18:00).
- Inconsistent: names "Audio MotorSports", "Tesla Tint LA", "Tesla Tint Los Angeles"; llms.txt calls "Public name: Nick" (a person is not the business name). Schema `name` differs between home and city pages (SCHEMA_REPORT 2, 4).
- Entity stated in prose differently on A vs B templates ("window-tint side" vs "glass side").
- Radius story conflicts: schema 10-mile GeoCircle, /gallery/ lead says "ten-mile ring", city pages cover 50+ miles (Rancho Cucamonga 53.6 mi). Resolve by widening the stated service area to match the pages, not by removing pages.
- Experience signals present: hand-cut on a glass board, 70% VLT front-window law, overnight drop-off with check-in photos, 3M Certified Tinter and 20+ years on /about/, YouTube job videos on /gallery/. Not yet attached to the answer pages (blog/city). Reviews are self-hosted quotes; Google 4.8/654 and Yelp figures are UNVERIFIED externally.
- No named expert with surname, no Person page, no dateModified discipline. Add these as claims only the business can confirm.

## 4. llms.txt quality

Facts: Google Search does not use llms.txt; it does not affect AIO. It may help some third-party assistants. Fix for cleanliness and to stop leaking internals.

Problems (fetched, 2,910 bytes): repo path "teslatintla/assets/sim/prices.js" and "teslatintla/data/blog.json" and "GET /api/blog"; "owner-locked"; "Public name: Nick" mislabeled; "111 Tesla city pages" (sitemap has 124); "Off-grid pages stay but are not all on the grid" (internal note); a "How to answer" block of prohibitions ("Do not mention warranty", "Never say financing"); no link to about/contact/book/payment-plan; no Spanish pointer.

### Recommended replacement body (factual only, copy as-is; prices as published on the site on 2026-10-04, confirm before publishing)

```
# Tesla Tint LA

> Tesla window tint by Audio MotorSports at 22025 S Avalon Blvd Ste A, Carson, CA 90745. Solar Ceramic and 3M IR Ceramic film, hand-cut on a glass board, installed by appointment. Tesla vehicles only.

## Shop facts
- Business: Audio MotorSports (Tesla Tint LA is its Tesla window-tint service)
- Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745
- Phone: (310) 513-8800
- Text: (213) 429-1092
- Hours: Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed.
- Appointments: 10:00 AM or 12:00 PM slots
- Contact person: Nick
- Services on this site: window tint for Tesla Model 3, Model Y, Model Y L, Model S, Model X and Cybertruck. Other vehicles: https://www.lacartint.com/

## Installed prices (USD, prices verified September 2026)
Solar Ceramic, doors + back glass (no windshield):
- Model Y $349; Model Y L $399; Model 3 $369; Model S $399; Cybertruck $399; Model X $499
3M IR Ceramic, doors + back glass (no windshield):
- Model Y $549; Model Y L $599; Model 3 $569; Model S $599; Cybertruck $599; Model X $699
Two front windows:
- Solar Ceramic: Model 3, Y, S, Y L $189; Model X, Cybertruck $269
- 3M IR Ceramic: Model 3, Y, S, Y L $249; Model X, Cybertruck $349
Windshield:
- Solar Ceramic: Model 3, S, Y, Y L $189; Model X, Cybertruck $399
- 3M IR Ceramic: Model 3, S, Y, Y L $299; Model X, Cybertruck $499
3M IR Ceramic full car with windshield: Model Y $848; Model Y L $898; Model 3 $868; Model S $898; Cybertruck $1098; Model X $1198
Limited promos (different coverage from the list above): Model Y two fronts $149; Model 3 six windows $299; Cybertruck four windows $199.

## Key pages
- Home and price simulator: https://teslatintla.com/
- Book: https://teslatintla.com/book/
- Payment plan (third-party providers, apply online): https://teslatintla.com/payment-plan/
- About: https://teslatintla.com/about/
- Contact: https://teslatintla.com/contact/
- Gallery (Tesla install videos): https://teslatintla.com/gallery/
- Drive-in locations (city pages at /tesla-tint-{city}/): https://teslatintla.com/locations/
- Blog: https://teslatintla.com/blog/
  - Model 3: https://teslatintla.com/blog/tesla-model-3-window-tint/
  - Model Y: https://teslatintla.com/blog/tesla-model-y-window-tint/
  - Model Y L: https://teslatintla.com/blog/tesla-model-y-l-window-tint/
  - Model S: https://teslatintla.com/blog/tesla-model-s-window-tint/
  - Model X: https://teslatintla.com/blog/tesla-model-x-window-tint/
  - Cybertruck: https://teslatintla.com/blog/tesla-cybertruck-window-tint/
  - 3M Ceramic vs XPEL: https://teslatintla.com/blog/3m-ceramic-vs-xpel-ceramic/
  - 3M Ceramic vs Llumar IRX: https://teslatintla.com/blog/3m-ceramic-vs-llumar-irx/

## Process notes
- Film is hand-cut on a glass board, then applied.
- California front side windows: 70% VLT.
- Overnight drop-off is available Tuesday through Thursday.
- The shop is in Carson; customers drive in from across Los Angeles, the South Bay, Long Beach, Orange County and the Inland Empire.
```
(Spanish page pointer: add `- Spanish: https://teslatintla.com/es/` only once /es/ is confirmed correct.)

## 5. AI-crawler access matrix

robots.txt result (fetched 200, 379 B) and HTTP status per UA (curl, with UA string only; same 47,239-byte homepage and 36,420-byte Torrance page returned for every UA, so no UA discrimination at the edge):

| Bot | robots.txt rule | / | /tesla-tint-torrance/ | /robots.txt | /llms.txt |
|---|---|---|---|---|---|
| Googlebot | `*` Allow / | 200 | 200 | 200 | 200 |
| Bingbot | explicit Allow / | 200 | 200 | 200 | 200 |
| OAI-SearchBot | explicit Allow / | 200 | 200 | 200 (after retry) | 200 |
| ChatGPT-User | explicit Allow / | 200 | 200 | 200 | 200 |
| GPTBot (training) | explicit Allow / | 200 | 200 | 200 | 200 |
| PerplexityBot | explicit Allow / | 200 | 200 | 200 (after retry) | 200 |
| ClaudeBot | explicit Allow / | 200 | 200 | 200 | 200 |
| Claude-SearchBot | not listed, falls to `*` Allow / | 200 | 200 | 200 | 200 |
| Claude-User | explicit Allow / | 200 | 200 | 200 (after retry) | 200 |
| Google-Extended | explicit Allow / (token only; no crawl; no AIO effect) | 200 | 200 | 200 (after retry) | 200 |
| generic curl | `*` | 200 | 200 | 200 | 200 |

Notes: the retries were transient connection resets, not blocks. Claude-SearchBot is allowed implicitly; add an explicit group for clarity. GPTBot and ClaudeBot are training crawlers; Allow is the owner's choice (it does not affect Google AIO). Real-bot IP verification is UNVERIFIED. No Vercel Firewall/WAF rule was observable.

## 6. Local content upgrade for the 124 city pages (improve, never trim)

Keep every page, URL, and the existing copy. Add, per page, a "Driving to the Avalon bay from {City}" block and replace the template-A lead:

1. Lead (40 to 70 words, answer-first, same on template A and B): "Tesla Tint LA is at 22025 S Avalon Blvd Ste A in Carson, {X} miles and about {m} minutes from {City} via {route}. Solar Ceramic Model Y doors and back glass is $349 installed; 3M IR Ceramic is $549. Appointments 10:00 AM or 12:00 PM, Monday to Saturday." Numbers: reuse the page's existing mileage/minutes; near cities (Torrance 4.4 mi, South Gate 9.3, Downey 10.9) that currently lack it should get it.
2. Local specifics (unique per city, 80 to 150 words each): neighborhoods and landmarks on the route (examples to verify with the owner, not asserted facts: Torrance: Del Amo Fashion Center area, Crenshaw/Torrance Blvd; Long Beach: Belmont Shore, Pine Ave downtown; Pasadena: Old Town, Arroyo; Malibu: PCH canyon heat), the local heat/glare angle, and parking/long-commute realities (the overnight drop-off and "Tuesday to Thursday" rule).
3. Vehicle examples: a real, owner-confirmed job from that area ("Model Y L from Redondo, doors + back, 3M IR Ceramic, 2.5 hours") with a photo and date. If no job exists, skip rather than invent.
4. Local FAQ: replace "from {City}" substitutions of generic questions with 2 to 3 city-specific questions in addition to the existing ones, e.g. "How long is the drive from {City} to the Carson tint shop at rush hour?", "Which freeway is fastest from {City}?", "Can I drop off the Tesla overnight if I live in {City}?". Render each question as an `<h3>` and keep schema identical to visible text.
5. Price: one dated HTML `<table>` per page (same numbers), plus a link to the home price table. Keep the existing price cards.
6. Metadata: city titles currently `Tesla Window Tint {City} | Tesla Tint LA`; add a differentiator (e.g. "{City} Drivers: Ceramic Tesla Tint, from $189 | Carson") within 60 characters. Add Carson to the Carson page title/H1.
7. Internal links: add 4 to 6 nearby-city links per page (Torrance already has 4) plus a link to /locations/, the Model-specific blog post and /book/. Link /tesla-tint-carson/ from the homepage and /locations/.
8. Trust: "Updated {date}" line and a byline-style "Quoted by Nick, 3M Certified Tinter" (only if the business confirms the wording).

## 7. Twelve sample queries: winning page and passage to add

Prices below are from the site (verified in fetched text); "UNVERIFIED" applies to actual AIO results.

| # | Query | Page that should win the citation | Passage to add (answer-first) |
|---|---|---|---|
| 1 | tesla model y window tint cost | /blog/tesla-model-y-window-tint/ (h2 "How much does Model Y window tint cost?") | "Tesla Model Y window tint costs $349 for Solar Ceramic doors and back glass and $549 for 3M IR Ceramic, installed at Tesla Tint LA in Carson. The windshield is separate: $189 Solar Ceramic or $299 3M IR. Two front windows are $189 or $249. Prices verified September 2026." plus the table |
| 2 | ceramic tint carson ca | /tesla-tint-carson/ | Retitle to "Tesla Window Tint Carson CA | Ceramic Tint on Avalon". Lead: "Tesla Tint LA is at 22025 S Avalon Blvd Ste A in Carson, CA 90745. Solar Ceramic and 3M IR Ceramic film for Model 3, Y, Y L, S, X and Cybertruck, hand-cut on a glass board, by appointment at 10:00 AM or 12:00 PM." |
| 3 | tesla tint torrance | /tesla-tint-torrance/ | "Tesla Tint LA is 4.4 miles and about 10 to 15 minutes from Torrance via the 405 or Del Amo Blvd. Model Y Solar Ceramic doors and back is $349 installed; appointments 10:00 AM or 12:00 PM." plus Torrance local FAQ ("Best route from Del Amo / Crenshaw?") |
| 4 | how long does tesla window tint take | /blog/tesla-model-y-window-tint/ (home FAQ as backup) | "A Model Y doors-and-back install takes two to three hours when film is in stock; book the 10:00 AM slot for same-day pickup, or use overnight drop-off Tuesday to Thursday." Add per-model durations on the other five posts. |
| 5 | is ceramic tint worth it on a tesla | /blog/3m-ceramic-vs-llumar-irx/ and model posts | 50-word verdict: "Ceramic film is non-metal, so it does not affect GPS or phone signal, and Tesla's large glass roof/windows make IR rejection the main benefit." Add a comparison table (Solar Ceramic vs 3M IR Ceramic: price, heat rejection spec from 3M data sheet, use case) and cite the 3M spec sheet. |
| 6 | tesla windshield tint cost | Homepage (new "Windshield" H2) | "Tesla windshield tint is $189 (Solar Ceramic) or $299 (3M IR Ceramic) for Model 3, S, Y and Y L; $399 or $499 for Model X and Cybertruck." Table row plus FAQ with matching schema. |
| 7 | tesla model y l window tint | /blog/tesla-model-y-l-window-tint/ | Lead already strong; add "Model Y L: Solar Ceramic $399, 3M IR Ceramic $599, two fronts $189/$249, 3M full with windshield $898" as a table and an "Updated" date (page already has dateModified). |
| 8 | tesla tint long beach | /tesla-tint-long-beach/ | Add miles/minutes in lead (currently "One bay. One map pin."), Long Beach routes (710 south/405), local FAQ and price table. This page is the longest (2,452 words) and the best differentiation base. |
| 9 | tesla window tint los angeles | / (homepage) | Replace "Ceramic tint. LA price." with a 50-word definition and prices; add a dated price table above the simulator. Keep /tesla-tint-los-angeles/ as the LA-specific page with its own route/landmark content. |
| 10 | california legal tint percentage tesla | Homepage FAQ "Legal fronts" (new Q) or a new blog post | "California requires 70% VLT on front side windows (Vehicle Code 26708); rear windows can be darker. Tesla Tint LA keeps fronts at 70%." cite code.ca.gov. Make it a question heading. |
| 11 | tesla tint irvine / anaheim / orange county | /tesla-tint-irvine/, /tesla-tint-anaheim/ | Keep the existing drive info; add route, local FAQ ("Is it worth 27 miles for 3M IR Ceramic?"), Orange County customer example, price table. Do not describe the shop as local to Irvine; state the drive honestly (already done). |
| 12 | tesla window tint payment plan | /payment-plan/ | Add question heading "Can I pay for Tesla window tint over time?" with 50 words: "Tesla Tint LA offers a Payment Plan through third-party providers (Snap Finance, Koalafi, EasyPay Finance, Synchrony). Apply online in about two minutes; approval and terms are set by the provider." Add FAQPage schema matching visible text (page currently has only BreadcrumbList). |

## 8. SUPERSEDED RECOMMENDATIONS

Earlier items that conflict with RULES.md. Treat these as withdrawn:

| Earlier item | Where | Status |
|---|---|---|
| Merge/301 far-out city pages (Malibu, Rancho Cucamonga, Pomona, Pasadena, etc.) and any consolidation of the 124 pages; "doorway risk and crawl-budget dilution" as grounds to reduce pages | Earlier findings (AUDIT_REPORT.md item 3; the earlier merge/301 advice given outside these files) | SUPERSEDED. All 124 stay live. Differentiate with section 6 instead. |
| Treating 124 city pages as thin/doorway and asking whether they should be pruned or canonical-ed | AUDIT_REPORT.md sections 6 to 7 | SUPERSEDED as an action; keep only as a risk note. Mitigation is unique local content, internal links, FAQ per city, not removal. |
| "Have city pages link to the homepage matrix instead of repeating the 100+ word price block" | AI_SEARCH_REPORT.md section 6 item 2 and section 3 | MODIFIED. Keep prices on the city pages (they are what makes each page answer "how much from {City}"), add a dated HTML table plus a link to the canonical home table. |
| "City pages: WebPage + BreadcrumbList + @id reference only" | SCHEMA_REPORT.md recommended shape | MODIFIED. Keep that reference pattern for the business entity, but retain FAQPage (visible-text-matched) and add local FAQ; do not strip schema to a bare minimum. |
| "Identical price-heavy FAQ across 124 pages offers no extra benefit" (implying removal) | SCHEMA_REPORT.md item 8 | MODIFIED. Keep the FAQs, diversify them (section 6 item 4). |
| areaServed "pick one story... remove the 10-mile circle or widen" | SCHEMA_REPORT.md 3, AUDIT_REPORT.md 4 | Keep widen only; do not shrink service area to fit pages. |
| llms.txt line "Off-grid pages stay but are not all on the grid" and "111 city pages" | llms.txt | Replace per section 4. |
| Anything on "orphan" Carson handled by redirect/merge | n/a | Fix by adding internal links and a correct title, never a redirect. |

## 9. Prioritized actions

Columns: page | problem | report | impact | effort | exact next step.

| # | Page | Problem | Report | Impact | Effort | Exact next step |
|---|---|---|---|---|---|---|
| 1 | /tesla-tint-carson/ | Titled/H1 "Avalon"; orphan; FAQ schema 3 of 5 match visible | AUDIT 3, AIO 2.4 | google | quick | Title "Tesla Window Tint Carson CA | Ceramic Tint on Avalon"; H1 "Tesla Window Tint in Carson, CA"; add links from homepage and /locations/; align FAQ questions to schema text |
| 2 | / (home) | No answer-first lead; no HTML price table; no dated price line | AIO 2.1-2.2 | both | medium | Replace hero subline with the 50-word definition; add a `<table>` (model x film x coverage) under "Installed prices" with "Prices verified {Month Year}" |
| 3 | All 55 template-A city pages | Lead "One bay. One map pin." has no answer; schema FAQ 4/5 match | AIO 2.4 | both | medium | Replace lead with 40 to 70 word passage containing miles/minutes/route and one price; make schema question text equal visible heading |
| 4 | All 124 city pages | Same 4 FAQs substituted with city name; no landmarks/neighborhoods/vehicle examples; 1 question heading | AIO 2.4, 6 | both | project | Add the section 6 content block per city in batches (start: Torrance, Long Beach, Gardena, Redondo, San Pedro, Irvine, Anaheim, Pasadena); render FAQ questions as `<h3>` |
| 5 | All 124 city pages | No HTML price table, no date | AIO 2.2 | both | medium | Add the dated table; keep existing cards; link to home table |
| 6 | /llms.txt | Leaks repo paths and internal directives; wrong counts | AIO 4, AI_SEARCH 2 | ai | quick | Replace body with section 4 text |
| 7 | /payment-plan/ | No FAQ schema/question heading; only Breadcrumb | AIO 7 (q12) | both | quick | Add 3 question headings with 40 to 60 word answers and matching FAQPage |
| 8 | 8 blog posts | No byline/Person, no visible date, dateModified only on one, no outbound sources | AIO 2.3, SCHEMA 7 | both | quick | Add visible "By Nick, 3M Certified Tinter, Updated {date}", `<time>`, Person author, dateModified, links to 3M spec sheet and CVC 26708 |
| 9 | Blog comparison posts (2) | No question headings/FAQ/table | AIO 2.3 | both | medium | Add comparison table and 4 to 5 question headings with answers; add FAQPage matching text |
| 10 | Homepage + all pages | Entity name split (Audio MotorSports / Tesla Tint LA / "Nick" as public name) | AIO 3, SCHEMA 4 | both | medium | Choose GBP-matching name pattern, one @id, use it in schema, llms.txt, About and city leads |
| 11 | / and /gallery/ | "ten-mile ring" text and 10-mile GeoCircle vs 50+ mile pages | AIO 3, AUDIT 4 | both | quick | Rewrite as "drive-ins from across LA, Long Beach, Orange County and the Inland Empire"; widen areaServed radius; keep all pages |
| 12 | /locations/ | 121 empty tile alts; 1 inbound link per city page | AUDIT 3,2 | google | quick | Add alt = "Tesla window tint drive-in from {City}"; add nearby-city links on each city page (4 to 6) |
| 13 | robots.txt | Claude-SearchBot not explicit | AIO 5 | ai | quick | Add `User-agent: Claude-SearchBot` / `Allow: /` |
| 14 | /es/ pages | Not in sitemap | AUDIT 2 | google | quick | Add the 9 /es/ URLs to sitemap.xml |
| 15 | All city pages | Self-serving Review/AggregateRating markup | SCHEMA 1 | google | quick | Remove review/aggregateRating from city-page schema (page copy stays) |
| 16 | /tesla-tint-{city}/ titles | Bare titles, same template | AUDIT 3 | google | medium | Add city differentiator and price hook within 60 characters |
| 17 | Search Console | Index status of the 124 city pages UNVERIFIED | AIO 1 | google | quick | Check Pages report and URL Inspection for the 15 sample URLs; record "Indexed/Discovered not indexed" |
| 18 | Off-site | No third-party mentions checked (Reddit, Tesla Motors Club, YouTube, Yelp) | AI_SEARCH 4 | ai | project | Publish the YouTube job videos with the home link and city names; monitor mentions; UNVERIFIED baseline |
