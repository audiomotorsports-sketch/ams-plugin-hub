# AI Search Report (GEO + AIO): amspods.com
Evidence: hub-mounted copy, proxy for the standalone domain, standalone not verified (www.amspods.com blocked by egress proxy; see LIMITATIONS.md). Tags: [mount-proxy] unless stated. AIO = Google AI Overviews. All recommendations improve existing pages; nothing is removed, merged or noindexed.

## 1. AIO eligibility (Google AI Overviews)
Rule applied: eligible = indexed by Googlebot and snippet-eligible (no noindex, no nosnippet/max-snippet:0, not blocked for Googlebot). Google-Extended affects Gemini training/grounding only, not AI Overviews or Search. llms.txt is not used by Google Search.
| Check | Result |
|---|---|
| noindex / nosnippet / max-snippet | None. Meta robots absent and no X-Robots-Tag on all 130 mounted pages (checked headers on a sample + meta on all) [mount-proxy] |
| robots.txt (hub) | One group `User-agent: *`, `Allow: /`, `Disallow: /admin/`, `Disallow: /planner/`, sitemap declared. Googlebot is not blocked [mount-proxy; hub file, not amspods.com's] |
| Standalone robots.txt | Not readable. Apex `/robots.txt` 308 -> `www.amspods.com/robots.txt` [standalone-verified for the redirect only] |
| Indexability of mount | Canonical on every mounted page points to `www.audiomotorsports.com/amspods/...` (self) so Google would index the mount under the hub host; the standalone's own canonical host is unknown |
| Verdict | Mounted pages: eligible. amspods.com: **eligible status unknown** until www is fetched; the apex redirect is correct and permanent |
Note: eligibility is necessary, not sufficient; AIO selects passages that directly answer the query.

## 2. Answer-ready content
Scored against the checklist: answer-first passage (40-80 words) under a question heading; lists/tables for comparisons and prices; freshness; author/experience; entity consistency.
| Signal | Finding |
|---|---|
| Question-style headings | Present: `/faq/` has H2 questions ("Which bikes do you build for?", "Where does the amp go on a Road Glide or Street Glide?", "Will this hold up in the rain?"). Absent on model, 2024, shop, catalog and city pages (headings are statements or template boilerplate) |
| Answer-first | FAQ answers are 30-60 words and lead with the answer (good). Model pages bury it after video/hero blocks |
| Tables/lists | No fitment or price table anywhere; catalog has item lists |
| Prices | "$649 a pair" appears (home, 27 pages) but is contradicted by "No public prices" on 3 pages (AUDIT 3.2.4) |
| Freshness | Few visible dates (2 pages), blog dateModified missing; llms.txt says "Prices verified September 2026" |
| Author/experience | Richard (builds since 2003, in trade since 1998), Nick (quotes), real YouTube jobs; blog author is an Organization |
| Entity | Name, address, phone, hours consistent in schema and copy; sister-site network named in sameAs |
| Leaked notes | "schema aggregate only", "we do not invent..." read as meta commentary and can be quoted by LLMs |
| Scope statements | Strong: "Road Glide, Street Glide, Road King only; no Sportster/Dyna/Indian/metric" (but Softail inconsistently allowed) |

## 3. FAQ / schema parity
- 93 pages carry FAQPage. 81 match visible text. 12 do not (service/model pages, blog index and 4 posts, es home and es FAQ). Fix by publishing the Q&As visibly; es pages need Spanish schema. Details in SCHEMA_REPORT 3.2.
- The 10-question FAQ is reused on blog pages; per-post FAQs (2-4 questions on that post's topic) answer better.
- Product/Offer parity: none. The price lives in prose only.

## 4. llms.txt
- Hub `https://www.audiomotorsports.com/llms.txt` exists (200, text/plain, 4.6 KB). Quality: good structure (shop facts, hours, prices, what it does and does not do, locations, key pages, network list). amspods appears as one line ("AMS Pods (Harley bagger audio): https://www.amspods.com") and the price line "AMS Pod pair: starting at $649". No models/years, build time, ship policy or amspods key pages. [mount-proxy]
- `amspods.com/llms.txt`: apex 308 -> `www.amspods.com/llms.txt`; content unknown [standalone-verified for redirect only].
- Recommendation: publish an amspods llms.txt (not used by Google Search; some answer engines and agents read it) with: what AMS Pods is, price from $649/pair, chrome or gloss, built in-house since 2003, about three weeks, models served and not served (with years), ships nationwide, Carson address/phone/hours, links to `/services/ams-pods/`, model pages, `/2024/`, `/faq/`, `/shop/`. Resolve the Rockford and price-wording contradictions first.

## 5. AI-crawler access
Hub robots.txt has a single `*` group, so all named agents inherit Allow with only `/admin/` and `/planner/` disallowed. No named per-bot groups exist (the file's comment explains they were removed because named groups override `*` and re-expose disallowed paths). [mount-proxy]
| Agent | Status on hub robots.txt |
|---|---|
| Googlebot | allowed |
| Bingbot | allowed |
| OAI-SearchBot | allowed |
| ChatGPT-User | allowed |
| PerplexityBot | allowed |
| ClaudeBot | allowed |
| Claude-SearchBot | allowed |
| Google-Extended | allowed (controls Gemini use only) |
Standalone `robots.txt`: **not verified** (www blocked). Server-level blocking (Vercel firewall/bot protection) cannot be assessed; the hub responded 200 to a generic UA only (no per-bot UA tests were made). On the standalone, run the same agent list through robots and a UA-spoofed fetch once reachable.

## 6. Eight sample queries: target page and passage to add
Passages are 40-80 words, answer-first, use only facts already on the mounted pages, and must be confirmed by the shop (years/models) before publishing. Place each directly under the stated H2 (question heading). Pair each with the visible FAQ + schema.

1. **"harley road glide speaker pods"** -> `/services/road-glide-bagger-audio/`, H2 "Do AMS pods fit a Road Glide?"
   > Yes. AMS pods are built in-house in Carson, CA for Road Glide baggers and sit at an angle on the crash bar, so the shark-nose fairing stays clean. A pair starts at $649, chrome or gloss, with the crash-bar bracket and screws included. Built to order in about three weeks. Hertz Neo speakers go in the pods. Text the year for a quote.
2. **"street glide crash bar speaker pods"** -> `/services/street-glide-bagger-audio/`, H2 "What pods fit a Street Glide?"
   > AMS pods fit Street Glide crash bars. Richard builds each pair in-house in Carson, CA, chrome or gloss black, from $649 a pair with the bracket and screws included. They mount at an angle and the crash bar hides most of the pod from the front. A mustache bar uses a different mount, so confirm your bar when you text the year.
3. **"how much are harley speaker pods"** -> `/services/ams-pods/`, H2 "How much are AMS pods?"
   > AMS pods start at $649 a pair, chrome or gloss black. The price includes the crash-bar bracket and screws. Pods are built to order in the Carson shop in about three weeks and ship nationwide. Speakers, amp and install are quoted separately by year and model; Hertz Neo is the speaker the shop recommends. Call (310) 513-8800 or text (213) 429-1092.
4. **"hertz neo vs cicada vs ds18 harley speakers"** -> `/catalog/hertz/` (and the blog "Where to start with bagger audio"), H2 "Hertz Neo, Cicada or DS18 for a bagger?"
   > Hertz Neo is the shop's pick for baggers: weatherproof with a small neo magnet that fits a saddlebag lid or AMS pod, and it stays clear loud. Cicada is a respected motorcycle brand that costs more and has a larger magnet. DS18 is the budget option, loud but harsh. AMS tested Hertz and Cicada side by side and Hertz sounded louder and cleaner.
5. **"do you have to remove the tank to install an amp on a road glide"** -> `/faq/`, H2 "Where does the amp go on a Road Glide or Street Glide?" (also on both model pages)
   > On Road Glide and Street Glide builds the amplifier mounts inside the fairing, and doing it correctly means pulling the gas tank. There is no shortcut. Road King and Softail have no fairing, so the amp lives in the bag on a carpeted board and the pods do the talking. Quote the year and the shop confirms how the amp sits on your bike.
6. **"2024 street glide speaker upgrade"** -> `/2024/`, H2 "What audio upgrades fit a 2024+ Street Glide or Road Glide?"
   > For 2024 and newer Street Glide and Road Glide the shop installs Cicada 2-speaker and 4-speaker kits (24FLXPCH and 24FLXCXX series) or Hertz Neo Stage 2 and Stage 4 packages (HDPKG1441 and HDPKG1442) using the A2B interface. Installed in Carson in one bay. Ask for Nick, send the year and model, and he quotes the system.
7. **"road king speaker pods no fairing"** -> `/services/road-king-bagger-audio/`, H2 "What audio works on a Road King?"
   > A Road King has no fairing, so the pods do the talking. AMS pods in chrome or gloss from $649 a pair mount on the crash bar, and the amp lives in a bag on a carpeted board with an AMS quick disconnect. Lid speakers can be cut into the original bag lids. Weatherproof speakers, fully soldered connections. Quote the year and confirm Softail fit with the shop.
8. **"harley bagger audio near long beach"** -> `/bagger-audio-long-beach/`, H2 "Where do I get Harley bagger audio near Long Beach?"
   > AMS Pods is one shop at 22025 S Avalon Blvd Ste A in Carson, with no second Long Beach location, so Long Beach riders ride or trailer in. Street Glide, Road Glide and Road King baggers get AMS pods from $649 a pair and in-house installs. Ride in Monday to Saturday, 9:30 AM to 6 PM, or call (310) 513-8800.
   (Add the verified drive route and time from Long Beach before publishing; it is the unique-content hook for this city page.)

Each query page also needs: a fitment table (model, years, mount, amp location), a "Last updated" date, a Person-credited byline, and a visible FAQ identical to its schema.

## 7. GEO priorities
1. Single canonical facts block (price, lead time, ship, models, years, hours) repeated identically on home, `/services/ams-pods/`, `/faq/`, llms.txt and schema.
2. Fitment table and per-model question headings (queries 1, 2, 6, 7).
3. Remove internal-note phrasing and the "no prices" contradiction.
4. Product schema + visible FAQ parity.
5. Citations to third-party corroboration: Google Business Profile link beside the rating, YouTube job videos embedded with transcripts, Yelp.
6. Standalone checks once reachable (robots per-bot, UA tests, sitemap, llms.txt, canonical host).
