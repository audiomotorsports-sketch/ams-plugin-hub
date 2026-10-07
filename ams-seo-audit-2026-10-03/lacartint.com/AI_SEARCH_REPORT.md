# AI Search Report (GEO + AIO): lacartint.com

**Evidence label: hub-mounted copy (https://www.audiomotorsports.com/tint/), proxy for the standalone domain, standalone not verified.** Date 2026-10-04. The apex lacartint.com 308-redirects every path to www.lacartint.com, which the egress proxy blocks (not bypassed). robots.txt, sitemap.xml and llms.txt of the standalone domain could therefore **not** be read. Facts about the hub files are about the hub, not the standalone.

AIO here means Google AI Overviews.

## 1. AIO eligibility (Google AI Overviews)

Eligibility rule applied: the page is indexed by Googlebot and snippet-eligible (no noindex, no nosnippet or max-snippet:0, not blocked for Googlebot in robots.txt).

| Check | Hub-mounted copy (141 pages) | Standalone lacartint.com |
|---|---|---|
| Meta robots | None present on any of 141 pages (no noindex, no nosnippet, no max-snippet) | Not verified |
| `X-Robots-Tag` header | None seen on the `/tint/` pages checked (headers on `/tint/window-tint-torrance/`: HSTS, X-Frame-Options, referrer-policy, `x-vercel-cache`) | Not verified |
| robots.txt for Googlebot | Hub robots.txt is one group: `User-agent: *`, `Allow: /`, `Disallow: /admin/`, `Disallow: /planner/`, Sitemap line. `/tint/` is allowed | Not verified (apex returns 308) |
| Canonical | 141 of 141 self-canonical to `https://www.audiomotorsports.com/tint/...`. None points at lacartint.com | Not verified |
| HTTP status | 141 of 141 return 200, server-rendered HTML (text visible without JS) | Apex 308 only [standalone-verified] |
| Sitemap | All 141 are in the hub sitemap (1,090 URLs) | Not verified |

Conclusion: the **mount pages are technically eligible** for AI Overviews. Whether the **standalone** pages are eligible cannot be said. One real risk stays open and is not solved by removing anything: the same copy is live at two origins, each self-canonical (mount) or unknown (standalone). Which origin Google picks as the representative for a query is unverified. Improvement path without removals: make each origin's copy genuinely distinct in its lead paragraph and title (the standalone leads with the tint brand, the mount keeps the hub framing), and keep cross-links between them so both are understood as one entity (see SCHEMA_REPORT 2.1).

Google-Extended is a robots.txt token that controls Gemini training/grounding use only. It does **not** gate AI Overviews or Search, so no change to Google-Extended affects AIO eligibility. llms.txt is not used by Google Search.

## 2. AI-crawler access (hub robots.txt, applied to /tint/)

The hub file has no per-bot groups, so every crawler falls under `User-agent: *` (allow all except /admin/ and /planner/). This is the shape the hub deliberately chose (its header comment explains named allow-only groups had overridden the Disallows).

| Crawler | Allowed on /tint/ by hub robots.txt | Standalone |
|---|---|---|
| Googlebot | Yes | Not verified |
| Bingbot | Yes | Not verified |
| OAI-SearchBot | Yes | Not verified |
| ChatGPT-User | Yes | Not verified |
| GPTBot | Yes | Not verified |
| PerplexityBot | Yes | Not verified |
| ClaudeBot | Yes | Not verified |
| Claude-SearchBot / Claude-User | Yes | Not verified |
| Google-Extended, Applebot-Extended | Yes (no group, so default allow) | Not verified |

Also verified on the apex: the 308 is identical for Googlebot and GPTBot user agents (no UA-based blocking at the apex). A WAF rule on www is a separate unknown. This is robots.txt permission only; actual crawl behavior and log evidence were not available.

## 3. llms.txt

- Hub `https://www.audiomotorsports.com/llms.txt`: 200, text/plain, 4,594 bytes. Good: plain-language shop facts, address, hours, published prices with a "verified September 2026" line, what the shop does not do, the six-site network list naming LA Car Tint with the URL `https://www.lacartint.com`.
- It is **hub-level, not tint-level**. It links to `/services/window-tinting/` on the hub and has no section for window-tint films, legal VLT, hand-cut method, or the 109 tint city pages. Standalone `https://www.lacartint.com/llms.txt`: **not verified** (apex 308 only).
- Quality issues in the hub file: a few lines read as instructions to the AI ("Do not mention warranty", "Do not invent terms, APR..."), and the city count ("123") differs from the mount's own locations page ("109 drive-ins") and from teslatintla.com's 121/124. Unlike teslatintla's file there are no repo paths.
- Improve: a tint-specific llms.txt on the standalone with the price table, film tiers (Solar, Solar Ceramic, 3M Ceramic IR, 3M Color Stable), California 70% VLT rule, hours, address, how to book, links to the service pages, FAQ, and the Tesla split with teslatintla.com. Neutral factual wording, one city count. Value is for non-Google AI tools; Google Search ignores it. [mount-proxy]

## 4. Answer-ready content audit (mount, 141 pages)

| Signal | Finding |
|---|---|
| FAQ presence | 128 of 141 pages have FAQPage schema; 116 of those match visible text exactly (see SCHEMA_REPORT 2.4 for the 12 that do not) |
| Question phrasing | City FAQs are 9 to 11 conversational questions per page, in `<details><summary>`, answer median 32 words, mean 40, range 16 to 65 |
| Answer-first, 40 to 80 words under a question **heading** | **Weak.** FAQ questions are `summary` elements, not headings. 124 pages have an H2 ending in "?", but on the 109 city pages it is only the navigational "Coming from X?". Real question headings exist only on `/tint/faq/` (10) and `/tint/es/faq/` (10). City pages use H2s "Same bay - Audio MotorSports", "FAQ", "Coming from X?" |
| Lead paragraph | City pages open "We are not in Torrance. The bay is Audio MotorSports on Avalon..." (honest, local, with drive route), good for the "near me / near X" intent, but there is no 40 to 80 word price-plus-service answer in the first screen |
| Tables / lists for prices and comparisons | **0 HTML tables on 141 pages.** Prices are in card widgets. A carbon-versus-ceramic comparison exists only as prose |
| Freshness | Only 5 of 141 pages show a visible "verified/updated" date. Hub sitemap lastmod values start 2026-09-19. The 3 BlogPostings have `datePublished` but no `dateModified`, no image, and an Organization (not Person) author |
| Author / experience | Names Nick and Zack appear on all 141 pages (good first-hand voice), but no byline, credential or "who installed this" line on blog posts |
| Entity consistency | NAP identical on every page (22025 S Avalon Blvd Ste A, Carson CA 90745; (310) 513-8800; hours Mo-Sa 9:30-18:00). Name differs ("LA Car Tint" vs "LA Car Tint at Audio MotorSports" vs "Audio MotorSports"); `@id` differs (SCHEMA_REPORT 2.1) |
| Contradictions | `/tint/faq/` meta says "no public prices" while its answers publish $249 and $329; the same page asks "How long does tint take?" and "How long does a tint job take?" with different answers (2 to 3 hours vs "often same-day") |
| Local coverage | Carson: 33 mentions on the home page but **no Carson city page** (only West Carson, with 1 inbound link). South Bay: Torrance, Gardena, Hawthorne, Redondo, Manhattan, Hermosa, El Segundo, Lomita, Lawndale, Palos Verdes Estates, Rancho Palos Verdes, Rolling Hills (+Estates), Harbor City, Wilmington, San Pedro all present. LA: Los Angeles, Santa Monica, Culver City, Inglewood and more. OC: Anaheim, Irvine, Santa Ana, Huntington Beach, Fullerton, Garden Grove, Fountain Valley, Seal Beach and more (no Costa Mesa, Newport Beach or Tustin page on the mount) |
| Uniqueness | City-page sentence-level unique copy: median 51 percent (about 751 unique words), range 16 to 74 percent; 12 pages under 250 unique words (Huntington Park, Bell, Norwalk, Hawaiian Gardens, Los Alamitos, South Gate, Cerritos, El Segundo lead the low list) |
| Internal links | City pages receive a median 5 inbound links from other /tint/ pages (range 1 to 12; West Carson 1). Each page carries about 480 unique links, roughly 210 of them /shop/ product links, which dilutes the local links |

## 5. FAQ / schema parity summary

See SCHEMA_REPORT.md. Parity is exact on 116 FAQ pages and fails on 12 (blog posts carry the same 9 site-wide questions, Spanish pages have English schema text). Business node parity: NAP in schema matches NAP on page.

## 6. Ten sample queries: target page and passage to add

Each passage is 40 to 80 words, answer-first, with the price/date line the AI engines need. All improve an existing page or add a page; none removes or merges anything. These apply to the standalone when it is reachable and to the mount in the meantime [mount-proxy].

### Q1. "ceramic window tint cost carson"
**Target page:** /window-tint-carson/ (new Carson page) and /services/ceramic-film/ (add a dated table)

> How much does ceramic window tint cost in Carson? At LA Car Tint in Carson, Solar Ceramic starts at $329 installed for a sedan: four doors plus the back window, no windshield. Plain Solar starts at $249. SUVs, trucks and vans are quoted by vehicle, and 3M Ceramic IR and Color Stable are quote-only. Prices verified October 2026. Text the year, make and model to (213) 429-1092.

(67 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q2. "window tint carson ca"
**Target page:** Home (/) retitled with Carson, plus new /window-tint-carson/

> Where can I get window tint in Carson, CA? LA Car Tint is at 22025 S Avalon Blvd Ste A, Carson, CA 90745, inside Audio MotorSports. It is a 3M Authorized Dealer, film is hand-cut on a glass board, and work is done at this shop only. Hours are Monday to Saturday 9:30 AM to 6:00 PM, closed Sunday. Walk-ins are welcome; call (310) 513-8800.

(65 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q3. "ceramic vs carbon window tint"
**Target page:** /services/ceramic-film/

> What is the difference between carbon and ceramic window tint? Solar Carbon is the entry film. Solar Ceramic rejects more heat, and premium 3M Ceramic IR is the top tier, with up to 95% IR heat rejection per 3M, varying by film and shade. Ceramic is also designed not to interfere with electronics the way some metalized films can. We confirm the film when we quote your vehicle.

(68 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q4. "is 70% tint legal in california front windows"
**Target page:** /blog/california-70-vlt-fronts/ and /faq/

> In California, front side windows must let at least 70% of light through (70% VLT). Only the top 4 inches of the windshield can be tinted. Rear side windows and the back window have no darkness limit. Ceramic film can still reject up to 95% of infrared heat per 3M on legal fronts, because heat rejection and darkness are different measurements. Medical exemptions exist for documented conditions.

(67 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q5. "window tint torrance ceramic"
**Target page:** /window-tint-torrance/

> Is there a window tint shop near Torrance? LA Car Tint is not in Torrance, but it is a drive of about ten to fifteen minutes: take the 405 to Avalon in Carson, or cut across on Del Amo or Crenshaw. Solar Ceramic starts at $329 installed for a sedan, Solar at $249. Book the 10:00 AM or 12:00 PM slot and ask for Nick at (310) 513-8800.

(68 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q6. "how long does window tint take same day"
**Target page:** /faq/ (fix duplicate question) and every city page FAQ

> How long does a window tint job take? Most cars take about two to three hours in the bay, and you drive the car home when it is finished. Full-vehicle ceramic and Tesla roofs take longer than two front doors. Book the 10:00 AM or 12:00 PM slot, or drop the car the night before. Keep the windows up for 3 to 5 days while the film cures.

(68 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q7. "window tint long beach"
**Target page:** /window-tint-long-beach/

> Where can I get ceramic window tint near Long Beach? LA Car Tint is not in Long Beach. The bay is at 22025 S Avalon Blvd Ste A, Carson, about [confirm drive time] from downtown Long Beach. Solar Ceramic starts at $329 installed for a sedan and Solar at $249. Film is hand-cut on a glass board, never on the vehicle. Call (310) 513-8800 or text (213) 429-1092.

(68 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q8. "how much is window tint for an suv near me"
**Target page:** / (price table) and /specials/

> How much does window tint cost for an SUV? Solar Ceramic on the two front windows starts at $149 installed for most SUVs, using California-legal 70% shades. Full SUV, truck and van jobs are quoted by vehicle because glass area differs. Sedan packages (four doors plus back window) start at $249 for Solar and $329 for Solar Ceramic. Text the year, make and model for the exact number.

(68 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q9. "window tint irvine orange county drive"
**Target page:** /window-tint-irvine/ and /window-tint-santa-ana/

> Is it worth driving from Orange County for window tint? LA Car Tint is one bay in Carson, not in Irvine, about [confirm drive time] up the 405. The trade is hand-cut 3M film installed by the same team, with Solar Ceramic from $329 installed for a sedan. Book a 10:00 AM or 12:00 PM slot, or drop the car off the night before.

(64 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

### Q10. "tesla model y window tint los angeles"
**Target page:** /tesla-tint/ rewritten as a film guide that sends model-specific booking to teslatintla.com

> Tesla glass has its own shop. Tesla Tint LA (teslatintla.com), the same Carson bay, handles Model 3, Y, S, X and Cybertruck, including roof and windshield. Solar Ceramic on doors and back starts at Model Y $349, Model 3 $369, Model S $399, Cybertruck $399, Model X $499, Y L $399. For any other make, LA Car Tint quotes the film.

(61 words. Facts taken only from the hub copy, hub llms.txt and teslatintla.com; `[confirm drive time]` must be filled from the GBP/Maps drive time before publishing, not guessed.)

## 7. AI-readiness recommendations (priority)

1. Add the 10 passages above under question-style H2/H3 headings (not only inside `<details>`). Impact ai + google. Effort quick to medium. [mount-proxy]
2. Add one dated HTML price table (Solar, Solar Ceramic, SUV fronts, quote-only films) to the home, `/specials/` and `/services/ceramic-film/`, with `offers` in the Service JSON-LD. Impact ai + google. [mount-proxy]
3. Fix the FAQ contradictions (meta "no public prices", duplicate questions with different answers). [mount-proxy]
4. Add visible "Prices verified {Month Year}" and `dateModified` on the 3 posts and key pages. [mount-proxy]
5. Tint-specific llms.txt on the standalone (section 3). [mount-proxy] until the standalone is readable.
6. Re-run this report against www.lacartint.com (robots, sitemap, llms, headers, WAF) once the proxy allows it. [standalone-verified step pending]
