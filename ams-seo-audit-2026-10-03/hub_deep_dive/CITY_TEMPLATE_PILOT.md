# City-page template spec and 5 pilot drafts (hub: audiomotorsports.com)

Prepared 2026-10-07 for Zack and Tom. **Nothing here has been applied.** No site, repo or account was changed. Every city page stays live at its current URL; the template only improves pages. Nothing goes live until Zack and Tom have reviewed it together.

Evidence base: live fetches on 2026-10-07 of all 158 hub city pages that return 200, the hub data file `https://www.audiomotorsports.com/data/drive-in-cities.json`, `/llms.txt`, `/sitemap.xml`, `/locations/`, `/specials/`, `/tint/`, `/reviews/` and `/faq/`. Prior audit files were read first and not redone (`HUB_FIRST_PLAN.md`, `FIX_LIST.md`, hub reports). Tags: **[CONFIRM]** means the owner must verify before it is published. Facts tagged "data file" come from `drive-in-cities.json`; "live page" means copy already published on that city page; "llms.txt" and "/specials/" are cited where used.

---

## 0. What Zack and Tom need to know first

1. **The data file only holds distance.** `drive-in-cities.json` gives name, slug and miles for 159 cities, nothing else (no drive time, no routes, no coordinates per city). Drive times and route names exist only inside each city page's own copy. So the route table in the drafts is built from two sources: miles from the data file, time and routes from the live page. Everything else that would make a page unique has to come from the shop.
2. **Verified data alone gives about 130 to 200 unique words per page.** The current pages look more unique (median 252 unique words, 399 to 625 on the five pilots) only because of flavor copy that nothing on the site backs up (for example "Torrance Tuesdays", "pier meters fry OEM decks"). The spec therefore needs an owner-supplied "From the shop floor" block per page. Without it, no city can reach the proposed minimum.
3. **The city pages never say the shop is in Carson.** The word "Carson" never appears in the main content as the shop's city on any of the 158 pages (the only matches are "West Carson", on its own page and in two neighbour links). The hero says "on Avalon" and "CA 90745". Carson appears in the footer and in schema only. The first fix is a 40 to 60 word answer that says what is offered, that the shop is in Carson, and the drive time.
4. **Every city page opens with "We are not in {City}."** (158 of 158). It is honest and reduces doorway risk, which is worth keeping, but it leads with what is absent. The draft keeps the same honesty in the second sentence.
5. **158 of 158 pages share one template.** Same six blocks in the same order, 9 of the 10 FAQ answers word-for-word identical on every page, the same 11 internal links, one meta description pattern with only the city name swapped. Median 85% of sentences also appear on another page; about 965 words per page are sentences that appear on 150 or more pages.
6. **Zero questions are headings.** The 10 FAQ questions sit in collapsed `<details><summary>` elements. FAQ schema matches visible text on all 158 pages, which is good and must be kept.
7. **No leaked internal phrases on the hub.** "Never imply nearby", "Do not reverse that", "We do not invent" and similar appear on 0 of 158 hub city pages (they were found only on the lacaralarm mount). They stay on the QA list.
8. **Fixes found on the way, all additive:** 35 live city pages are missing from `/locations/` (the page says "One hundred twenty-three drive-ins" and links 123 of 158); 7 city pages have zero inbound links from other city pages; `/orange/` is in the data file but returns 308 to `/locations/` and is not in the sitemap; 49 titles are over 60 characters; "nearby" links are chosen by similar distance from the shop, not by actual neighbourhood.

**Decisions for tomorrow (details in section 7):** D1 approve the section order; D2 who supplies "From the shop floor" facts; D3 whether the old long copy stays in full below the new blocks (the draft keeps all of it); D4 which price page the table link points to; D5 approve the pilot nearby lists and the control cities.

---

## 1. The current template, measured

Method. Main content means everything from the hero (breadcrumb, H1, intro) to the end of the CTA band, excluding site header, menu and footer. A "shared" sentence is one of four or more words that, after swapping the city name for a token and digits for N, also appears on at least one other page. Counts cover all 158 live city pages unless a table says otherwise.

### 1.1 Section order (identical on 158 of 158 pages)
| # | Block | What is in it |
|---|---|---|
| 1 | Hero video + Call/Text bar | Site chrome, same everywhere |
| 2 | Breadcrumb + H1 | H1 = "Car Stereo, Tint & Alarm for {City}" (same as the title minus brand) |
| 3 | Intro paragraph (47 to 98 words, median 86) | Starts "We are not in {City}.", then address with "CA 90745" (no "Carson"), route, time, "Ask for Nick. Zack runs the floor." |
| 4 | Call / Text / Google Maps / Get a Quote buttons | Same |
| 5 | Drive paragraph + 12 more copy paragraphs (`city-copy`) | About 900 to 1,000 words. Stereo, tint, alarm paragraphs each repeat the prices and "Park once" lines |
| 6 | "Same bay" block (H2 + 3 brand cards) | Links out to lacarbeats.com, lacartint.com, lacaralarm.com |
| 7 | "Five-star notes" (H2) | 1 to 3 Yelp quotes with reviewer city, no dates, no service label |
| 8 | "FAQ" (H2) | 10 questions in collapsed `<details>` |
| 9 | "Nearby drive-ins" line + "Coming from {City}?" CTA band | 4 city links, 3 buttons |

H2s on every page: "Same bay — Audio MotorSports", "Five-star notes", "FAQ", "Coming from {City}?". Only the last contains the city.

### 1.2 Numbers across all 158 pages
| Measure | Result |
|---|---|
| Main-content words | min 1,683 / median 1,871 / max 2,218 |
| Intro wording | two variants: 110 pages read "Audio MotorSports is one Avalon bay ..."; 48 read "The bay is ... on Avalon ..." (or similar). Both open "We are not in {City}." |
| Sentences shared with at least one other page | median 85% (min 64%, max 90%) |
| Words per page in sentences found on 150+ pages | about 965 (about half the page) |
| Unique words per page (not shared) | median 252, min 175, max 735 |
| Title | pattern "Car Stereo, Tint & Alarm for {City} \| Audio MotorSports"; 49 of 158 are over 60 characters (Huntington Beach 65, Redondo Beach 62) |
| Meta description | one pattern, only the city name differs; 98 to 117 characters; no miles, no time, no Carson |
| H1 | restates the title; no Carson |
| Question headings | 0 (all 10 FAQ questions are `<summary>` text) |
| FAQ | 10 on every page, about 470 words; Q2 (the drive answer, 95 to 153 words) is the only answer that differs between pages; the other 9 answers are identical on all 158 pages (21 to 71 words each) |
| Internal links in main content | 11 on every page: home, /locations/, /contact/ x2, /payment-plan/ x2, /reviews/, 4 nearby cities. None to /specials/, /tint/, /stereo/ or /alarm/ |
| Route / drive-time table | none (time and route sit in prose; 158 of 158 give a time range) |
| Schema | BreadcrumbList + AutoRepair + FAQPage on 158 of 158. No WebPage node, no `dateModified` or `datePublished` on any page |
| FAQ schema vs visible FAQ | identical on 158 of 158 (keep) |
| Reviews | 12 distinct reviewer quotes reused across the set (parsed); only 8 of 158 pages show a quote from the page's own city; none carries a date |
| Hub pages with leaked directives ("Never imply nearby", "Do not reverse that", "We do not invent", "schema aggregate", "owner-locked") | 0 of 158 |
| Customer quote containing "Mickey Mouse" | 18 pages, inside a real Yelp quote only; not an internal phrase |

### 1.3 The five pilots and eight comparison pages (live, 2026-10-07)
Shared and unique figures use the 158-page comparison.
| Page | Miles (data file) | Main words | Intro words | Title chars | Shared sentences | Unique words | Same-city review quotes |
|---|---|---|---|---|---|---|---|
| Torrance (pilot) | 4.4 | 1,924 | 68 | 57 | 65% | 625 | 1 |
| Long Beach (pilot) | 5.7 | 1,964 | 64 | 59 | 68% | 581 | 3 |
| Gardena (pilot) | 4.9 | 1,924 | 65 | 56 | 69% | 546 | 2 |
| Redondo Beach (pilot) | 7.2 | 1,805 | 57 | 62 | 76% | 399 | 0 |
| San Pedro (pilot) | 6.5 | 1,817 | 53 | 58 | 73% | 460 | 1 |
| West Carson (near) | 1.8 | 1,846 | 87 | 60 | 85% | 246 | 0 |
| Harbor City (near) | 2.8 | 1,895 | 77 | 60 | 79% | 362 | 0 |
| Anaheim (OC) | 20.0 | 1,841 | 90 | 56 | 85% | 248 | 0 |
| Huntington Beach (OC) | 19.3 | 1,870 | 87 | 65 | 86% | 239 | 0 |
| Irvine (OC) | 27.0 | 1,909 | 60 | 55 | 70% | 530 | 0 |
| Pasadena (far) | 28.6 | 1,857 | 87 | 57 | 86% | 236 | 0 |
| Fontana (far) | 61.7 | 1,866 | 87 | 56 | 86% | 244 | 0 |
| Lancaster (farthest) | 86.8 | 1,891 | 91 | 58 | 83% | 303 | 0 |

Reading the table: the five pilots, Irvine and Harbor City are the most individually written pages (shared 65% to 79%); the rest sit at 83% to 86%. The unique words on the pilots are mostly local flavor that nothing else on the site backs up, not verifiable facts. Section 4 lists those claims for each pilot so the owner can keep or soften them.

### 1.4 "No shop in this city" versus the drive-in model
* The hero starts "We are not in {City}." on 158 of 158 pages, then repeats the idea 4 to 10 times per page in different words ("not a {City} storefront", "no second {City} row of shops", "there is no {City} location", "the pin does not move west").
* The FAQ's first question is "Are you in {City}?" with the answer "No." (identical on 158 pages), and the meta says "{City} drive-in ... one Avalon bay".
* The model is stated clearly and honestly (one shop, you drive in), which is the right protection against a doorway-page reading. The weakness is order and emphasis: the page opens with the absence, buries what is offered, and never names Carson in the visible copy. `llms.txt` says "Each page says the shop is not in that city", so keeping the statement is consistent with the site's own rule.
* Staff lines "Ask for Nick. Zack runs the floor." sit in the hero of every page; "Albert" and "Richard" appear on a few. These repeat and are not answers.

### 1.5 Site-wide inconsistencies the template depends on (all fixable by adding, not removing)
| Finding | Evidence |
|---|---|
| `/locations/` says "One hundred twenty-three drive-ins" and links 123 of the 158 live city pages | 35 live pages have no link there: Alondra Park, Altadena, Anaheim Hills, Arcadia, Brea, Brentwood, Costa Mesa, Del Aire, Diamond Bar, Duarte, Granada Hills, Hidden Hills, La Canada Flintridge, La Crescenta-Montrose, Malibu, Midway City, Newport Beach, North Hollywood, Northridge, Pacific Palisades, Placentia, Reseda, Sherman Oaks, Studio City, Sylmar, Tarzana, Temple City, Tustin, Van Nuys, Villa Park, Walnut, Westmont, Winnetka, Woodland Hills, Yorba Linda (and Orange, see next row) |
| Data file lists 159 cities; 158 pages return 200 | `/orange/` returns 308 to `/locations/` and is not in the sitemap (the file has Orange at 23.8 miles). Adding a real Orange page would be an addition; that is a decision, not part of this pilot |
| `llms.txt` says the locked list is "15.5 mi of Avalon plus Los Angeles, Santa Ana, Irvine"; the data file says `radius_mi: 35` and lists cities to 86.8 miles (Lancaster); `/locations/` says 123 | Three different statements of the service area; align them when the template ships [CONFIRM which is intended] |
| 7 city pages have zero inbound links from other city pages: Alondra Park, Del Aire, Midway City, Brentwood, Sylmar, Azusa, Lancaster; 17 have 0 or 1 | Counted from the 4 "nearby" links on each page. San Pedro, one of the pilots, has 1; Gardena and Redondo Beach have 3 each |
| "Nearby" links follow distance rank from the shop, not neighbourhood | Irvine (27.0 mi) links San Marino, Glendale, City of Industry, El Monte (all 26.6 to 27.2 mi from the shop); Huntington Beach links La Habra, Fountain Valley, Fullerton, South El Monte; Redondo Beach links Rolling Hills, Paramount, Watts, Lakewood (7.2 to 7.7 mi). The data file has no city-to-city distances, so real adjacency needs the owner's knowledge [CONFIRM] |
| Price strings differ across live pages | City pages and `/tint/` and `/specials/`: Solar $249 and Solar Ceramic $329 installed (agree). City pages: "Dual Kicker Comp loaded box $249, box only"; `/specials/`: "Kicker Dual 12 CVS $299 installed". `llms.txt`: "Compustar 9910 starting at $499"; `/specials/`: "Compustar 8910 $399". `/faq/` meta: "no public prices". The drafts use only the tint prices, which agree everywhere |
| Service links in the footer and menu redirect | `/services/car-audio/` 308 to `/stereo/`, `/services/window-tinting/` 308 to `/tint/`, `/services/auto-alarms/` 308 to `/alarm/`. The drafts link the final URLs |

---

## 2. Template spec

### 2.1 Principles
1. Every city page stays live at its URL. No page is removed, merged, redirected or noindexed. The template adds answer-first blocks and upgrades existing ones.
2. Keep the honest drive-in message. Say what is offered and where the shop is first, then say there is no shop in the city. One clear statement beats six repeats.
3. Only facts the site can back. Miles come from the data file; drive time, routes, prices and quotes come from published pages; local color comes from the owner and is tagged [CONFIRM] until verified.
4. Visible text and schema match word for word.
5. "Avalon" is a street. The address is always written "22025 S Avalon Blvd Ste A, Carson, CA 90745" and `addressLocality` stays "Carson".

### 2.2 Page anatomy, in order
| # | Block | Rule | Shared or unique |
|---|---|---|---|
| 1 | Title, meta, canonical, OG | Title at most 60 characters: `{City} Car Stereo, Tint & Alarm \| Audio MotorSports`; if over 60, use `{City} Car Stereo & Tint \| Audio MotorSports`. Meta 110 to 155 characters, must contain miles, drive time and "Carson": `{City} car stereo, window tint and car alarms at our one Carson shop: {miles} miles, about {time}. Open Mon-Sat 9:30-6. Call (213) 429-1092.` Canonical unchanged | Unique by city data |
| 2 | Site hero, breadcrumb | Unchanged | Shared |
| 3 | H1 + one-line subhead | H1 `Car Stereo, Window Tint & Car Alarms for {City} Drivers`; subhead `One shop in Carson, {miles} miles from {City}` | Unique (name, miles) |
| 4 | **Answer paragraph, 40 to 60 words** | First text on the page. Must say, in this order: what is offered; the shop is in Carson at 22025 S Avalon Blvd Ste A; there is no shop in {City}; miles and drive time; main route; hours; phone. No staff names, no jargon | Unique (city, miles, time, route) around a fixed frame |
| 5 | CTA row | Call (213) 429-1092, Text (213) 429-1092, Google Maps, Get a Quote (existing buttons, moved under the answer) | Shared |
| 6 | **Route table** "Getting to the shop from {City}" | Rows: distance (data file), typical drive (live page), main route, alternate route, destination (address, Maps link), hours, tint start times (10:00 AM or 12:00 PM). Footnote: "Drive times are our estimate for moving traffic; check Google Maps for live traffic." | Unique (miles, time, routes) around a fixed frame |
| 7 | **Five question headings** (H2, answers visible, not collapsed) | Q1 How far is the shop from {City} and which way to drive (unique); Q2 Is there a shop in {City} (frame plus city); Q3 How much is window tint for a {City} driver (price frame, linked to price table); Q4 Can I get stereo, tint and alarm in one trip from {City} (frame plus city time); Q5 What do customers from {City} say (review slot) | Q1 unique, Q2 and Q4 partly unique, Q3 shared, Q5 unique |
| 8 | **Dated local review slot** (inside Q5, replaces "Five-star notes" in place) | 1 to 3 quotes. Each shows first name and initial, the reviewer's own city, platform, service done, and the **date shown on the Google or Yelp listing**. Prefer same-city reviewers. Never label a quote with a city the reviewer did not give. Shop-wide rating line with an "as of" date | Unique |
| 9 | **From the shop floor** (owner-supplied, 80 to 120 words) | 2 to 4 facts the shop can stand behind: a real job from this city (vehicle, work, month, photo with customer's OK), the arrival cue, the commute detail customers actually mention. Each fact carries a source tag in the draft (invoice, photo, customer) and the tag is removed at publish. If nothing is supplied the block is omitted, not filled with filler | Unique, owner-supplied |
| 10 | Retained existing content | The current drive paragraph and 12 copy paragraphs, "Same bay" cards, and FAQ questions 3 to 10 (as "More questions"). Moved below the new blocks. Nothing is dropped; where a sentence is rewritten (internal voice, repeats) the replacement is at least as long. Page word count never falls below today's | Shared (today) |
| 11 | **Nearby drive-in cities** | 4 links with miles from the data file, curated for real adjacency by the owner [CONFIRM]. Reciprocal: if A lists B, B lists A. Include at least one pilot city so pilots interlink | Unique |
| 12 | **Price table link** | One sentence and a link to the current price table: `/specials/` today, the dated price table once built (see `HUB_FIRST_PLAN.md` fix 6). Also link `/tint/`, `/stereo/`, `/alarm/` once each in body copy | Shared |
| 13 | Final CTA band | Existing "Coming from {City}?" with Call, Text, Get a Quote | Shared |
| 14 | JSON-LD | See 2.5 | Mixed |

### 2.3 What stays shared and what must be unique per city
| Shared across all city pages (maintain once in the template partial) | Unique per city |
|---|---|
| Address, phone, text line, hours, Sunday closed, walk-in line | Miles (data file) and the "N cities are closer / neighbours at X and Y miles" comparison |
| What the shop does and does not do; "no mobile installs" (llms.txt) | Drive time, main route, alternate route |
| Tint price sentence and price-table link (one source) | Answer paragraph wording around those facts |
| CTA buttons, brand cards, payment-plan line | Title, meta, H1 subline |
| Q3 and Q4 answer frames (city name and time inserted) | Q1 answer; review quotes with dates; nearby list |
| Schema business node | "From the shop floor" facts (owner) |

### 2.4 Minimum unique words
Measured the same way as section 1: sentences of three or more words, city name and digits normalised, compared against every other city page.
* **New blocks (items 3 to 9, 11) must contain at least 300 sentence-unique words** for cities within 12 miles (48 cities in the data file), **at least 220** for 12 to 35 miles (97 cities), **at least 150** for beyond 35 miles (14 cities). Reason: nearer cities have more locally meaningful detail to report; far cities are destination drives and honestly have less.
* Verified data alone supplies roughly 130 to 200 words (section 4 measures it for the pilots). The rest must come from item 9 and from real dated reviews. If a city cannot reach its minimum, the page keeps the shared frame and ships the verified blocks; it is not padded.
* No more than 50% of the words in the new blocks may be sentences shared with another city page (the frames in Q3 and Q4 are the allowed shared part).
* Whole-page shared share target: below 70% (median today 85%). The retained old copy keeps it high at first; reduce it only by replacing, never by deleting.

### 2.5 Schema spec
* Keep the existing `AutoRepair` node exactly as it is on the live page (same `@id` `https://www.audiomotorsports.com/#business`, address, geo, hours, `areaServed` City, `sameAs`). Appendix A shows it once. The pilot makes no change to it so that schema effects stay separate from content effects.
* Add a `WebPage` node: `url`, `name` (= title), `description` (= meta), `about` (the business `@id`), `breadcrumb`, and `dateModified` (YYYY-MM-DD, set at publish and bumped on every real edit).
* Keep `BreadcrumbList` as is.
* `FAQPage` lists exactly the five question headings and their visible answers, word for word. The retained "More questions" accordion is not in schema in the pilot (it can be added later if its text is also visible, which it is).
* Do not mark up the quoted reviews as `Review` nodes. Do not add price `Offer` markup until the dated price table exists.
* Separate decisions, not in the pilot: geo values as numbers rather than strings; the self-serving `aggregateRating` (4.8 / 654 repeated on every page); one `@id` per brand. These are in `SCHEMA_REPORT.md`.

### 2.6 Linking spec
* Every page links: the 4 curated nearby cities, `/locations/`, `/specials/` (price table), `/tint/`, `/stereo/`, `/alarm/`, `/reviews/`, `/contact/`, `/payment-plan/` (today only the last four, plus the home page, are present).
* Reciprocity and a floor of 5 inbound links from other city pages for every pilot (today: Torrance 5, Long Beach 6, Gardena 3, Redondo Beach 3, San Pedro 1). Pilots link to each other where adjacent.
* Add the 35 unlisted city pages to `/locations/` and correct its count. This changes inbound links to those pages, so do it after the test or exclude those pages from the control group (the control list in section 5 already does).

### 2.7 Voice rules
Customer-facing sentences only. No instructions to ourselves, no "weave", "desk" or "native" jargon, no staff names in the answer block (one "Ask for Nick" in the CTA area is enough), no claims about customers' vehicles or streets unless the owner confirmed them. Say "Carson" in the first 60 words.

### 2.8 Maintenance
`dateModified` and the "as of" dates change when someone checks the times, prices or review counts; a quarterly check is proposed [CONFIRM cadence]. Shared frames live in one template partial so a price or hours change is made once. Keep a saved copy of each original page before any edit, and a dated change log.

---

## 3. QA checklist

Run the script below on every draft before Zack and Tom review it. It is read-only and standard-library only. On the live pilots today it reports 10 to 11 failures per page (baseline below), which is what the template is meant to fix.

| # | Check | Pass rule | Automated |
|---|---|---|---|
| 1 | Title length | 60 characters or fewer, contains the city | yes |
| 2 | Meta | 110 to 155 characters, contains miles and minutes, differs from every other page's meta | yes |
| 3 | One H1 | exactly 1 | yes |
| 4 | Answer paragraph | 40 to 60 words, first paragraph after the H1, names the city, Carson and Avalon, has miles and minutes, does not start "We are not in" | yes |
| 5 | Route table | a table with miles present | yes |
| 6 | Question headings | 4 to 6 H2/H3 ending in "?" | yes |
| 7 | FAQ schema equals visible text | each schema question and answer appears verbatim on the page; one FAQPage | yes |
| 8 | WebPage node | present with a valid `dateModified` | yes |
| 9 | JSON-LD parses | all blocks parse | yes |
| 10 | No leaked internal phrases | none of "Never imply", "Never claim", "Do not reverse", "We do not invent", "schema aggregate", "owner-locked", "Do not mention", "we do not publish a dollar", "Never say", "TODO", "{{" | yes |
| 11 | No unresolved placeholders | none of [CONFIRM, [DATE, [PUBLISH-DATE, [PRICE-CHECK-DATE, [REVIEW-COUNT-DATE, [OWNER, [REVIEW-DATE | yes |
| 12 | Address intact | "22025 S Avalon Blvd Ste A" in visible text; "Avalon" never used as a city ("in Avalon", "for Avalon", "Avalon, CA", "Tesla Avalon"); `addressLocality` is "Carson" | yes |
| 13 | Links | /specials/, tel:, sms:, at least 4 nearby-city links | yes |
| 14 | Dated review | a date (YYYY-MM-DD or Month YYYY) inside the review block | yes |
| 15 | Word count | visible words not lower than the saved original | print and compare |
| 16 | Facts match sources | miles equal the data file; time and routes equal the published text the owner approved; prices equal the price page on the check date; rating and counts equal the listings on the "as of" date | manual |
| 17 | Review quotes | verbatim from the listing, reviewer's own city, date copied from the listing | manual |
| 18 | Mobile view | answer paragraph and route table visible without horizontal scroll at phone width | manual |
| 19 | Nothing else changed | diff of the saved original against the draft shows only the intended blocks; the AutoRepair node is byte-identical | manual |

**Baseline on the live pilots, 2026-10-07 (script output):** Torrance 11 failures, Long Beach 11, Gardena 11, Redondo Beach 11 (adds title over 60), San Pedro 10. Failing checks on all five: meta length and content, answer content, route table, question headings, WebPage node, /specials/ link, dated review.
**Test of the drafts below:** rendered into plain HTML with the placeholders filled with test dates, all five pass the automated checks (0 failures). With placeholders left in, check 11 correctly fails, so unresolved [CONFIRM] items block publishing.

```python

#!/usr/bin/env python3
"""QA for a drafted or live hub city page. Usage: python3 -I qa_city_page.py page.html "City Name" [cities.json] [other_page.html ...]
cities.json is https://www.audiomotorsports.com/data/drive-in-cities.json saved locally (used to recognise nearby-city links).
Prints PASS/FAIL per check. Read-only. Standard library only."""
import sys,re,json,html
def text(s):
    s=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S|re.I); s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=re.sub(r'</(p|div|li|h\d|summary|tr|section)>','\n',s); s=re.sub(r'<[^>]+>',' ',s)
    return html.unescape(re.sub(r'[ \t]+',' ',s))
def main():
    f,city=sys.argv[1],sys.argv[2]; rest=sys.argv[3:]; cj=[a for a in rest if a.endswith('.json')]; others=[a for a in rest if not a.endswith('.json')]
    slugs=set(c['slug'] for c in json.load(open(cj[0]))['cities']) if cj else set()
    t=open(f,encoding='utf-8').read(); head,body=(t.split('</head>')+[''])[:2]
    res=[]
    def chk(name,ok,detail=''): res.append((name,ok,detail))
    title=html.unescape(re.search(r'<title>(.*?)</title>',head,re.S).group(1)).strip()
    meta=html.unescape((re.search(r'name="description" content="(.*?)"',head,re.S) or [None,''])[1])
    chk('title <= 60 chars',len(title)<=60,f'{len(title)}: {title}')
    chk('title has city',city.lower() in title.lower())
    chk('meta 110-155 chars',110<=len(meta)<=155,f'{len(meta)}')
    chk('meta has miles and minutes',bool(re.search(r'\d+(\.\d)? mi',meta)) and 'minute' in meta)
    for o in others:
        ot=open(o,encoding='utf-8').read(); om=re.search(r'name="description" content="(.*?)"',ot,re.S)
        chk(f'meta differs from {o}',not om or html.unescape(om.group(1))!=meta)
    h1=re.findall(r'<h1[^>]*>(.*?)</h1>',body,re.S); chk('exactly one H1',len(h1)==1,str(len(h1)))
    # first paragraph after H1
    after=body.split('</h1>',1)[1] if '</h1>' in body else ''
    ps=[re.sub(r'\s+',' ',text(p)).strip() for p in re.findall(r'<p[^>]*>(.*?)</p>',after,re.S)]
    ps=[p for p in ps if len(p.split())>=15]
    first=ps[0] if ps else ''
    n=len(first.split())
    chk('answer paragraph 40-60 words',40<=n<=60,f'{n} words')
    chk('answer says shop is in Carson + Avalon address',('Carson' in first) and ('Avalon' in first))
    chk('answer has drive time and miles',('minute' in first) and bool(re.search(r'\d+(\.\d)? miles',first)))
    chk('answer names the city',city in first)
    chk('answer does not start with "We are not in"',not first.startswith('We are not in'))
    chk('route table present (table with miles)','<table' in body and re.search(r'\d+(\.\d)? miles',body.split('<table',1)[1] if '<table' in body else '') is not None)
    qh=[re.sub(r'\s+',' ',text(h)).strip() for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>',body,re.S)]
    qh=[h for h in qh if h.endswith('?')]
    chk('4-6 question headings (H2/H3 ending ?)',4<=len(qh)<=6,f'{len(qh)}')
    ld=[]; ok=True
    for m in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S):
        try: ld.append(json.loads(m))
        except Exception as e: ok=False
    chk('all JSON-LD parses',ok)
    nodes=[]
    for b in ld: nodes+= b.get('@graph',[b]) if isinstance(b,dict) else b
    faq=[n for n in nodes if n.get('@type')=='FAQPage']
    chk('exactly one FAQPage',len(faq)==1)
    if faq:
        vis=re.sub(r'\s+',' ',text(body))
        miss=[]
        for q in faq[0]['mainEntity']:
            a=re.sub(r'\s+',' ',q['acceptedAnswer']['text']).strip(); qn=re.sub(r'\s+',' ',q['name']).strip()
            if a not in vis or qn not in vis: miss.append(qn[:50])
        chk('FAQ schema question+answer text appears verbatim on page',not miss,'; '.join(miss))
        chk('FAQ schema questions all appear as headings or summaries',all(q['name'] in qh or ('<summary>'+q['name'] in body) for q in faq[0]['mainEntity']))
    chk('WebPage node with dateModified',any(n.get('@type')=='WebPage' and re.match(r'\d{4}-\d\d-\d\d',str(n.get('dateModified',''))) for n in nodes))
    bad=[p for p in ['Never imply','Never claim','Do not reverse','We do not invent','schema aggregate','owner-locked','Do not mention','we do not publish a dollar','Never say','TODO','{{','[CONFIRM','[DATE','[PUBLISH','[PRICE-CHECK','[REVIEW-COUNT','[REVIEW-DATE','[OWNER'] if p.lower() in text(body).lower()]
    chk('no leaked internal phrases or unresolved placeholders',not bad,', '.join(bad))
    chk('"Avalon Blvd" intact in visible text','22025 S Avalon Blvd Ste A' in text(body))
    bad_av=re.findall(r'(?:\b(?:in|for|near|Tint|Stereo|Alarm|Tesla) Avalon\b(?! Blvd| Boulevard)|Avalon,? (?:CA|California|city))',text(body))
    chk('"Avalon" never used as a city',not bad_av and not re.search(r'addressLocality"\s*:\s*"Avalon"',t),str(bad_av[:3]))
    chk('schema addressLocality is Carson','"addressLocality":"Carson"' in t.replace(' ',''))
    links=re.findall(r'<a [^>]*href="([^"]*)"',body)
    chk('links: /specials/ (price table)',any(l.startswith('/specials/') for l in links))
    chk('links: tel: and sms:',any(l.startswith('tel:') for l in links) and any(l.startswith('sms:') for l in links))
    nearby=[l for l in links if re.fullmatch(r'/[a-z0-9-]+/',l) and l.strip('/') in slugs and l.strip('/')!=re.sub(r'\W+','-',city.lower())]
    chk('>= 4 nearby-city links',len(set(nearby))>=4,str(len(set(nearby))))
    rev=re.search(r'(review|Five-star)[\s\S]{0,6000}',body,re.I)
    chk('review block has a date (YYYY-MM-DD or Month YYYY)',bool(rev and re.search(r'(20\d\d-\d\d-\d\d|(January|February|March|April|May|June|July|August|September|October|November|December) 20\d\d)',rev.group(0))))
    w=len(text(body.split('<footer')[0]).split()); chk('visible words recorded (must be >= baseline)',True,str(w))
    width=max(len(r[0]) for r in res)
    for name,ok,d in res: print(('PASS' if ok else 'FAIL'),name.ljust(width),d)
    print('FAILS:',sum(1 for r in res if not r[1]))
main()
```

---

## 4. Five pilot drafts

Each draft gives the new blocks in page order. Wording in square brackets is a slot for the owner. Data sources: miles from `drive-in-cities.json`; drive time and routes copied from the live city page for the same city; prices from `/specials/`, `/tint/` and `llms.txt` (tint only); reviews quoted from the live city page (Yelp quotes already published there); hours, phone, text line and "no mobile installs" from `llms.txt` and the live pages. No new facts were added. The "N other drive-in cities are closer" sentence in Q1 comes from the data file; it matches `/locations/` only after the 35 missing tiles are added, so drop that one sentence if `/locations/` is not updated first. All five drafts' titles are 52 to 58 characters, metas 144 to 153, answer paragraphs 53 to 60 words.

Shared text used on every page (so it is written once here):
* **CTA row:** Call (213) 429-1092 · Text (213) 429-1092 · Google Maps (link as on the live page) · Get a Quote (/contact/).
* **Route table frame**, rows in this order: Distance (data file) · Typical drive · Main route · Alternate · Destination (22025 S Avalon Blvd Ste A, Carson, CA 90745) · Open (Monday to Saturday, 9:30 AM to 6:00 PM; Sunday closed; walk-ins welcome) · Tint start times (10:00 AM or 12:00 PM). Footnote: "Distances: Audio MotorSports drive-in list. Drive times are our estimate for moving traffic; check Google Maps for live traffic. [CONFIRM wording]"
* **Price-table block:** "Current prices are on our [Specials page](/specials/). Window tint details: [Window tint](/tint/). Car stereo: [Car stereo](/stereo/). Car alarms and remote start: [Car alarms](/alarm/)." (switch the first link when the dated price table exists)
* **Final CTA band:** "Coming from {City}? Call (213) 429-1092 · Text (213) 429-1092 · Get a Quote".
* **Retained blocks (unchanged), below the review slot:** current drive paragraph and 12 copy paragraphs, "Same bay" cards, FAQ questions 3 to 10 as "More questions".


### 4.1 Torrance (`/torrance/`, 4.4 miles)

| Item | Live today | Draft |
|---|---|---|
| Title | Car Stereo, Tint & Alarm for Torrance \| Audio MotorSports (57) | Torrance Car Stereo, Tint & Alarm \| Audio MotorSports (53) |
| Meta | Torrance drive-in for car stereo, 3M window tint, and car alarm — one Avalon bay. Call (213) 429-1092. (102) | Torrance car stereo, window tint and car alarms at our one Carson shop: 4.4 miles, about 10 to 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092. (148) |
| H1 | Car Stereo, Tint & Alarm for Torrance | Car Stereo, Window Tint & Car Alarms for Torrance Drivers |
| Subhead | none | One shop in Carson, 4.4 miles from Torrance |
| Intro | 68 words, starts "We are not in Torrance.", no "Carson" | 54 words, leads with what is offered and says Carson |

**Answer paragraph** (first text under the H1)

> Audio MotorSports installs car stereo, window tint and car alarms at one shop in Carson: 22025 S Avalon Blvd Ste A. There is no shop in Torrance. You drive in: 4.4 miles, about 10 to 15 minutes, via the 405 to Avalon. Open Monday to Saturday, 9:30 AM to 6:00 PM. Call (213) 429-1092.

**Route table**

| From Torrance | Detail |
|---|---|
| Distance | 4.4 miles (data file) |
| Typical drive | about 10 to 15 minutes when traffic is moving (live page) |
| Main route | The 405 to Avalon (live page) |
| Alternate | Del Amo, Crenshaw, Hawthorne Boulevard or Torrance Boulevard, then Avalon (live page) |
| Destination | 22025 S Avalon Blvd Ste A, Carson, CA 90745 ([Google Maps](https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a)) |
| Open | Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed. Walk-ins welcome. |
| Tint start times | 10:00 AM or 12:00 PM |

**H2: How far is Audio MotorSports from Torrance, and which way should I drive?**

It is 4.4 miles from Torrance to the shop at 22025 S Avalon Blvd Ste A in Carson, about 10 to 15 minutes when traffic is moving. Main route: The 405 to Avalon. Alternate: Del Amo, Crenshaw, Hawthorne Boulevard or Torrance Boulevard, then Avalon. Four drive-in cities on our list are closer to the shop: West Carson, Harbor City, Wilmington and Lomita. For comparison, Lomita is 3.7 miles and Gardena is 4.9 miles away.

**H2: Is there an Audio MotorSports shop in Torrance?**

No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Torrance customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location.

**H2: How much is window tint for a Torrance driver?**

Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the [Specials page](/specials/) or text the year, make and model to (213) 429-1092.

**H2: Can I get stereo, tint and a car alarm done in one trip from Torrance?**

Yes. All three are installed at the same shop, so one drive from Torrance (about 10 to 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held.

**H2: What do customers from Torrance say about Audio MotorSports?**

Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city.

Dated review slot (each card: quote, first name and initial, reviewer's own city, platform, service, date from the listing):

> "After talking to Nick (and other employees) and checking out their work and videos on Youtube i went in to talk to them. Instantly I realized that they knew what they were doing."
> Luis G., Torrance · Yelp · Tesla window tint prep · [REVIEW-DATE, copy from the Yelp listing]

Note: Only same-city quote on the live page. Its service is Tesla tint, so the card says so. Add a second Torrance quote if one exists on the Google or Yelp listing [CONFIRM].

**From the shop floor** (owner-supplied slot, 80 to 120 words, omitted if empty)

> [OWNER: 2 to 4 facts about this city. Suggestions to verify, not facts:]
> - Which streets do Torrance customers actually name? The live page names Del Amo, Crenshaw, Hawthorne Boulevard and Torrance Boulevard [CONFIRM each route and the 10-15 minute estimate at peak hours].
> - Arrival cue off the 405 (exit name and what you see turning onto Avalon) [CONFIRM exit wording].
> - Typical Torrance vehicles. The live page says Camrys, Accords and Ford fleet trucks; keep only if invoices support it [CONFIRM].
> - One real Torrance job: vehicle, work done, month, photo, and the customer's OK to publish [CONFIRM].

**Nearby drive-in cities** (curated by the owner for real adjacency [CONFIRM]; miles from the data file; each also links back here)

| City | Miles from shop | Link |
|---|---|---|
| Lomita | 3.7 | /lomita/ |
| Gardena | 4.9 | /gardena/ |
| Redondo Beach | 7.2 | /redondo-beach/ |
| Rolling Hills Estates | 6.0 | /rolling-hills-estates/ |

**Price-table link, final CTA:** shared text above.

**JSON-LD** (graph below is added; the live `AutoRepair` node stays as is, see Appendix A)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/torrance/#webpage",
      "url": "https://www.audiomotorsports.com/torrance/",
      "name": "Torrance Car Stereo, Tint & Alarm | Audio MotorSports",
      "description": "Torrance car stereo, window tint and car alarms at our one Carson shop: 4.4 miles, about 10 to 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092.",
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "breadcrumb": {
        "@id": "https://www.audiomotorsports.com/torrance/#breadcrumb"
      },
      "dateModified": "[PUBLISH-DATE]"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.audiomotorsports.com/torrance/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.audiomotorsports.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Locations",
          "item": "https://www.audiomotorsports.com/locations/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Car Stereo, Tint & Alarm for Torrance",
          "item": "https://www.audiomotorsports.com/torrance/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/torrance/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Audio MotorSports from Torrance, and which way should I drive?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It is 4.4 miles from Torrance to the shop at 22025 S Avalon Blvd Ste A in Carson, about 10 to 15 minutes when traffic is moving. Main route: The 405 to Avalon. Alternate: Del Amo, Crenshaw, Hawthorne Boulevard or Torrance Boulevard, then Avalon. Four drive-in cities on our list are closer to the shop: West Carson, Harbor City, Wilmington and Lomita. For comparison, Lomita is 3.7 miles and Gardena is 4.9 miles away."
          }
        },
        {
          "@type": "Question",
          "name": "Is there an Audio MotorSports shop in Torrance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Torrance customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location."
          }
        },
        {
          "@type": "Question",
          "name": "How much is window tint for a Torrance driver?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the Specials page or text the year, make and model to (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get stereo, tint and a car alarm done in one trip from Torrance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. All three are installed at the same shop, so one drive from Torrance (about 10 to 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held."
          }
        },
        {
          "@type": "Question",
          "name": "What do customers from Torrance say about Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city."
          }
        }
      ]
    }
  ]
}
```

**Live-page claims to confirm, soften or keep (nothing is removed by the pilot; owner decides):** "Del Amo lot Camrys and Ford fleet trucks share one Tuesday" and "Torrance Tuesdays" (no support on the site); "Torrance ceramic heat is Del Amo asphalt" (landmark claim); "Albert sums the amp" (staff reference without context); "Not port trucks" (unclear).

### 4.2 Long Beach (`/long-beach/`, 5.7 miles)

| Item | Live today | Draft |
|---|---|---|
| Title | Car Stereo, Tint & Alarm for Long Beach \| Audio MotorSports (59) | Long Beach Car Stereo, Tint & Alarm \| Audio MotorSports (55) |
| Meta | Long Beach drive-in for car stereo, 3M window tint, and car alarm — one Avalon bay. Call (213) 429-1092. (104) | Long Beach car stereo, window tint and car alarms at our one Carson shop: 5.7 miles, about 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092. (144) |
| H1 | Car Stereo, Tint & Alarm for Long Beach | Car Stereo, Window Tint & Car Alarms for Long Beach Drivers |
| Subhead | none | One shop in Carson, 5.7 miles from Long Beach |
| Intro | 64 words, starts "We are not in Long Beach.", no "Carson" | 56 words, leads with what is offered and says Carson |

**Answer paragraph** (first text under the H1)

> Audio MotorSports installs car stereo, window tint and car alarms at one shop in Carson: 22025 S Avalon Blvd Ste A. There is no shop in Long Beach. You drive in: 5.7 miles, about 15 minutes, via the 405 or the 710, then Avalon. Open Monday to Saturday, 9:30 AM to 6:00 PM. Call (213) 429-1092.

**Route table**

| From Long Beach | Detail |
|---|---|
| Distance | 5.7 miles (data file) |
| Typical drive | about 15 minutes when traffic is moving (live page) |
| Main route | The 405 or the 710, then Avalon (live page) |
| Alternate | Del Amo west, then Avalon (live page) |
| Destination | 22025 S Avalon Blvd Ste A, Carson, CA 90745 ([Google Maps](https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a)) |
| Open | Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed. Walk-ins welcome. |
| Tint start times | 10:00 AM or 12:00 PM |

**H2: How far is Audio MotorSports from Long Beach, and which way should I drive?**

It is 5.7 miles from Long Beach to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 minutes when traffic is moving. Main route: The 405 or the 710, then Avalon. Alternate: Del Amo west, then Avalon. Seven other drive-in cities on our list are closer to the shop. For comparison, Compton is 5.4 miles and Signal Hill is 5.8 miles away.

**H2: Is there an Audio MotorSports shop in Long Beach?**

No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Long Beach customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location.

**H2: How much is window tint for a Long Beach driver?**

Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the [Specials page](/specials/) or text the year, make and model to (213) 429-1092.

**H2: Can I get stereo, tint and a car alarm done in one trip from Long Beach?**

Yes. All three are installed at the same shop, so one drive from Long Beach (about 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held.

**H2: What do customers from Long Beach say about Audio MotorSports?**

Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city.

Dated review slot (each card: quote, first name and initial, reviewer's own city, platform, service, date from the listing):

> "Nick hooked me up, got windows tinted, new stereo with speakers and alarm. Great deal and great service."
> Casey L., Long Beach · Yelp · Tint, stereo and alarm · [REVIEW-DATE, copy from the Yelp listing]

> "I recently had to have a replacement alarm system installed to replace my fried unit. ... Nick was incredibly helpful, Only installed what we needed and didn't try to upsell a bunch of items that we didn't need."
> Charles L., Long Beach · Yelp · Replacement alarm · [REVIEW-DATE, copy from the Yelp listing]

> "They installed my Viper 3108 with DB3 sensor flawlessly, explained everything clearly, tested it on my car, and were very kind and professional."
> N M., Long Beach · Yelp · Viper 3108 install · [REVIEW-DATE, copy from the Yelp listing]

Note: Three same-city Yelp quotes exist on the live page. Show all three with service labels; dates [CONFIRM] from the Yelp listing.

**From the shop floor** (owner-supplied slot, 80 to 120 words, omitted if empty)

> [OWNER: 2 to 4 facts about this city. Suggestions to verify, not facts:]
> - Neighborhoods Long Beach customers come from (live page mentions Belmont, downtown and the pier) [CONFIRM from customer addresses].
> - Whether the 710 or the 405 is the better default from Long Beach, and the time at rush hour [CONFIRM].
> - Whether Del Amo west is a sensible alternate from Long Beach [CONFIRM; it is on the live page today].
> - One real Long Beach job with photo and customer OK [CONFIRM].

**Nearby drive-in cities** (curated by the owner for real adjacency [CONFIRM]; miles from the data file; each also links back here)

| City | Miles from shop | Link |
|---|---|---|
| Signal Hill | 5.8 | /signal-hill/ |
| Lakewood | 7.7 | /lakewood/ |
| Wilmington | 3.3 | /wilmington/ |
| Seal Beach | 10.9 | /seal-beach/ |

**Price-table link, final CTA:** shared text above.

**JSON-LD** (graph below is added; the live `AutoRepair` node stays as is, see Appendix A)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/long-beach/#webpage",
      "url": "https://www.audiomotorsports.com/long-beach/",
      "name": "Long Beach Car Stereo, Tint & Alarm | Audio MotorSports",
      "description": "Long Beach car stereo, window tint and car alarms at our one Carson shop: 5.7 miles, about 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092.",
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "breadcrumb": {
        "@id": "https://www.audiomotorsports.com/long-beach/#breadcrumb"
      },
      "dateModified": "[PUBLISH-DATE]"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.audiomotorsports.com/long-beach/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.audiomotorsports.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Locations",
          "item": "https://www.audiomotorsports.com/locations/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Car Stereo, Tint & Alarm for Long Beach",
          "item": "https://www.audiomotorsports.com/long-beach/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/long-beach/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Audio MotorSports from Long Beach, and which way should I drive?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It is 5.7 miles from Long Beach to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 minutes when traffic is moving. Main route: The 405 or the 710, then Avalon. Alternate: Del Amo west, then Avalon. Seven other drive-in cities on our list are closer to the shop. For comparison, Compton is 5.4 miles and Signal Hill is 5.8 miles away."
          }
        },
        {
          "@type": "Question",
          "name": "Is there an Audio MotorSports shop in Long Beach?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Long Beach customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location."
          }
        },
        {
          "@type": "Question",
          "name": "How much is window tint for a Long Beach driver?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the Specials page or text the year, make and model to (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get stereo, tint and a car alarm done in one trip from Long Beach?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. All three are installed at the same shop, so one drive from Long Beach (about 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held."
          }
        },
        {
          "@type": "Question",
          "name": "What do customers from Long Beach say about Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city."
          }
        }
      ]
    }
  ]
}
```

**Live-page claims to confirm, soften or keep (nothing is removed by the pilot; owner decides):** "Pier meters and downtown street parking fry OEM decks, cook glass, and steal cars the same night" (sweeping claim); "not a Harbor City stroll down the boulevard" (odd comparison); "Belmont one evening, a downtown block that cooked the factory module" (invented anecdote unless real) .

### 4.3 Gardena (`/gardena/`, 4.9 miles)

| Item | Live today | Draft |
|---|---|---|
| Title | Car Stereo, Tint & Alarm for Gardena \| Audio MotorSports (56) | Gardena Car Stereo, Tint & Alarm \| Audio MotorSports (52) |
| Meta | Gardena drive-in for car stereo, 3M window tint, and car alarm — one Avalon bay. Call (213) 429-1092. (101) | Gardena car stereo, window tint and car alarms at our one Carson shop: 4.9 miles, about 10 to 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092. (147) |
| H1 | Car Stereo, Tint & Alarm for Gardena | Car Stereo, Window Tint & Car Alarms for Gardena Drivers |
| Subhead | none | One shop in Carson, 4.9 miles from Gardena |
| Intro | 65 words, starts "We are not in Gardena.", no "Carson" | 53 words, leads with what is offered and says Carson |

**Answer paragraph** (first text under the H1)

> Audio MotorSports installs car stereo, window tint and car alarms at one shop in Carson: 22025 S Avalon Blvd Ste A. There is no shop in Gardena. You drive in: 4.9 miles, about 10 to 15 minutes, via Avalon Boulevard south. Open Monday to Saturday, 9:30 AM to 6:00 PM. Call (213) 429-1092.

**Route table**

| From Gardena | Detail |
|---|---|
| Distance | 4.9 miles (data file) |
| Typical drive | about 10 to 15 minutes when traffic is moving (live page) |
| Main route | Avalon Boulevard south, straight to the shop (live page) |
| Alternate | Rosecrans to Avalon, or the 110 if you are east of the boulevard (live page) |
| Destination | 22025 S Avalon Blvd Ste A, Carson, CA 90745 ([Google Maps](https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a)) |
| Open | Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed. Walk-ins welcome. |
| Tint start times | 10:00 AM or 12:00 PM |

**H2: How far is Audio MotorSports from Gardena, and which way should I drive?**

It is 4.9 miles from Gardena to the shop at 22025 S Avalon Blvd Ste A in Carson, about 10 to 15 minutes when traffic is moving. Main route: Avalon Boulevard south, straight to the shop. Alternate: Rosecrans to Avalon, or the 110 if you are east of the boulevard. Five drive-in cities on our list are closer to the shop: West Carson, Harbor City, Wilmington, Lomita and Torrance. For comparison, Torrance is 4.4 miles and Compton is 5.4 miles away.

**H2: Is there an Audio MotorSports shop in Gardena?**

No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Gardena customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location.

**H2: How much is window tint for a Gardena driver?**

Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the [Specials page](/specials/) or text the year, make and model to (213) 429-1092.

**H2: Can I get stereo, tint and a car alarm done in one trip from Gardena?**

Yes. All three are installed at the same shop, so one drive from Gardena (about 10 to 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held.

**H2: What do customers from Gardena say about Audio MotorSports?**

Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city.

Dated review slot (each card: quote, first name and initial, reviewer's own city, platform, service, date from the listing):

> "I also got the compustar security system installed after they broke into my car and ive never felt this comfortable leaving the car parked out. Upgraded the hell out my Jeep Gladiator. Worth every penny."
> Ruben G., Gardena · Yelp · Compustar alarm, Jeep Gladiator · [REVIEW-DATE, copy from the Yelp listing]

> "One of the services that I frequently use at Audio Motor Sport is window tinting. ... The technicians at Audio Motor Sport are experts at installing window tint, and they always use high-quality films that are durable and long-lasting."
> Jestin L., Gardena · Yelp · Window tint · [REVIEW-DATE, copy from the Yelp listing]

Note: Two same-city Yelp quotes on the live page. Ruben G. is also cited in the live body copy, which is a verified link between copy and review.

**From the shop floor** (owner-supplied slot, 80 to 120 words, omitted if empty)

> [OWNER: 2 to 4 facts about this city. Suggestions to verify, not facts:]
> - Whether Avalon Boulevard south is really the "straight shot" from most of Gardena [CONFIRM].
> - Which Gardena cross streets customers name besides Rosecrans [CONFIRM].
> - Common Gardena vehicles. Live page says Gladiators, Highlanders, Civics [CONFIRM against invoices].
> - One real Gardena job with photo and customer OK [CONFIRM].

**Nearby drive-in cities** (curated by the owner for real adjacency [CONFIRM]; miles from the data file; each also links back here)

| City | Miles from shop | Link |
|---|---|---|
| Torrance | 4.4 | /torrance/ |
| Lawndale | 6.5 | /lawndale/ |
| Hawthorne | 8.0 | /hawthorne/ |
| Compton | 5.4 | /compton/ |

**Price-table link, final CTA:** shared text above.

**JSON-LD** (graph below is added; the live `AutoRepair` node stays as is, see Appendix A)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/gardena/#webpage",
      "url": "https://www.audiomotorsports.com/gardena/",
      "name": "Gardena Car Stereo, Tint & Alarm | Audio MotorSports",
      "description": "Gardena car stereo, window tint and car alarms at our one Carson shop: 4.9 miles, about 10 to 15 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092.",
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "breadcrumb": {
        "@id": "https://www.audiomotorsports.com/gardena/#breadcrumb"
      },
      "dateModified": "[PUBLISH-DATE]"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.audiomotorsports.com/gardena/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.audiomotorsports.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Locations",
          "item": "https://www.audiomotorsports.com/locations/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Car Stereo, Tint & Alarm for Gardena",
          "item": "https://www.audiomotorsports.com/gardena/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/gardena/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Audio MotorSports from Gardena, and which way should I drive?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It is 4.9 miles from Gardena to the shop at 22025 S Avalon Blvd Ste A in Carson, about 10 to 15 minutes when traffic is moving. Main route: Avalon Boulevard south, straight to the shop. Alternate: Rosecrans to Avalon, or the 110 if you are east of the boulevard. Five drive-in cities on our list are closer to the shop: West Carson, Harbor City, Wilmington, Lomita and Torrance. For comparison, Torrance is 4.4 miles and Compton is 5.4 miles away."
          }
        },
        {
          "@type": "Question",
          "name": "Is there an Audio MotorSports shop in Gardena?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Gardena customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location."
          }
        },
        {
          "@type": "Question",
          "name": "How much is window tint for a Gardena driver?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the Specials page or text the year, make and model to (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get stereo, tint and a car alarm done in one trip from Gardena?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. All three are installed at the same shop, so one drive from Gardena (about 10 to 15 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held."
          }
        },
        {
          "@type": "Question",
          "name": "What do customers from Gardena say about Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city."
          }
        }
      ]
    }
  ]
}
```

**Live-page claims to confirm, soften or keep (nothing is removed by the pilot; owner decides):** "Compustar-after-break-in on a Gladiator is native here" (jargon; "native" is odd); "Highlanders and Civics are the mix" (unsupported); "people who already tint here and keep coming back" (no data).

### 4.4 Redondo Beach (`/redondo-beach/`, 7.2 miles)

| Item | Live today | Draft |
|---|---|---|
| Title | Car Stereo, Tint & Alarm for Redondo Beach \| Audio MotorSports (62) | Redondo Beach Car Stereo, Tint & Alarm \| Audio MotorSports (58) |
| Meta | Redondo Beach drive-in for car stereo, 3M window tint, and car alarm — one Avalon bay. Call (213) 429-1092. (107) | Redondo Beach car stereo, window tint and car alarms at our one Carson shop: 7.2 miles, about 15 to 20 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092. (153) |
| H1 | Car Stereo, Tint & Alarm for Redondo Beach | Car Stereo, Window Tint & Car Alarms for Redondo Beach Drivers |
| Subhead | none | One shop in Carson, 7.2 miles from Redondo Beach |
| Intro | 57 words, starts "We are not in Redondo Beach.", no "Carson" | 60 words, leads with what is offered and says Carson |

**Answer paragraph** (first text under the H1)

> Audio MotorSports installs car stereo, window tint and car alarms at one shop in Carson: 22025 S Avalon Blvd Ste A. There is no shop in Redondo Beach. You drive in: 7.2 miles, about 15 to 20 minutes, via Pacific Coast Highway or Torrance Boulevard east, then Avalon. Open Monday to Saturday, 9:30 AM to 6:00 PM. Call (213) 429-1092.

**Route table**

| From Redondo Beach | Detail |
|---|---|
| Distance | 7.2 miles (data file) |
| Typical drive | about 15 to 20 minutes when traffic is moving (live page) |
| Main route | Pacific Coast Highway or Torrance Boulevard east, then Avalon (live page) |
| Alternate | 190th to the 405, then Avalon (live page) |
| Destination | 22025 S Avalon Blvd Ste A, Carson, CA 90745 ([Google Maps](https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a)) |
| Open | Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed. Walk-ins welcome. |
| Tint start times | 10:00 AM or 12:00 PM |

**H2: How far is Audio MotorSports from Redondo Beach, and which way should I drive?**

It is 7.2 miles from Redondo Beach to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 to 20 minutes when traffic is moving. Main route: Pacific Coast Highway or Torrance Boulevard east, then Avalon. Alternate: 190th to the 405, then Avalon. Fourteen other drive-in cities on our list are closer to the shop. For comparison, San Pedro is 6.5 miles and Rolling Hills is 7.2 miles away.

**H2: Is there an Audio MotorSports shop in Redondo Beach?**

No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Redondo Beach customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location.

**H2: How much is window tint for a Redondo Beach driver?**

Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the [Specials page](/specials/) or text the year, make and model to (213) 429-1092.

**H2: Can I get stereo, tint and a car alarm done in one trip from Redondo Beach?**

Yes. All three are installed at the same shop, so one drive from Redondo Beach (about 15 to 20 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held.

**H2: What do customers from Redondo Beach say about Audio MotorSports?**

Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city.

Dated review slot (each card: quote, first name and initial, reviewer's own city, platform, service, date from the listing):

> "Late review, got my windows tinted and a sound system here back in July, and it has changed my life!!! Excellent quality tint and audio. Both the guys that helped me out in each of their departments were so helpful and were happy to explain everything to me with pricing."
> Crystal K., Hermosa Beach · Yelp · Tint and sound system · [REVIEW-DATE, copy from the Yelp listing]

Note: No Redondo Beach reviewer exists on the live page. The card shows a Hermosa Beach reviewer under her own city, never labelled Redondo. Ask for a real Redondo review [CONFIRM].

**From the shop floor** (owner-supplied slot, 80 to 120 words, omitted if empty)

> [OWNER: 2 to 4 facts about this city. Suggestions to verify, not facts:]
> - Which Redondo neighborhoods or streets customers name (live page mentions PCH, Torrance Boulevard, 190th, the Strand and Catalina Avenue) [CONFIRM each].
> - Whether PCH or 190th is the better default and the time at rush hour [CONFIRM].
> - A real Redondo job with photo and customer OK, and a request to one Redondo customer for a dated review [CONFIRM].
> - Whether beach-area claims (sand, salt air, parked near the pier) match what the shop sees [CONFIRM].

**Nearby drive-in cities** (curated by the owner for real adjacency [CONFIRM]; miles from the data file; each also links back here)

| City | Miles from shop | Link |
|---|---|---|
| Torrance | 4.4 | /torrance/ |
| Lawndale | 6.5 | /lawndale/ |
| Hermosa Beach | 8.1 | /hermosa-beach/ |
| Manhattan Beach | 9.3 | /manhattan-beach/ |

**Price-table link, final CTA:** shared text above.

**JSON-LD** (graph below is added; the live `AutoRepair` node stays as is, see Appendix A)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/redondo-beach/#webpage",
      "url": "https://www.audiomotorsports.com/redondo-beach/",
      "name": "Redondo Beach Car Stereo, Tint & Alarm | Audio MotorSports",
      "description": "Redondo Beach car stereo, window tint and car alarms at our one Carson shop: 7.2 miles, about 15 to 20 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092.",
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "breadcrumb": {
        "@id": "https://www.audiomotorsports.com/redondo-beach/#breadcrumb"
      },
      "dateModified": "[PUBLISH-DATE]"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.audiomotorsports.com/redondo-beach/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.audiomotorsports.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Locations",
          "item": "https://www.audiomotorsports.com/locations/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Car Stereo, Tint & Alarm for Redondo Beach",
          "item": "https://www.audiomotorsports.com/redondo-beach/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/redondo-beach/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Audio MotorSports from Redondo Beach, and which way should I drive?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It is 7.2 miles from Redondo Beach to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 to 20 minutes when traffic is moving. Main route: Pacific Coast Highway or Torrance Boulevard east, then Avalon. Alternate: 190th to the 405, then Avalon. Fourteen other drive-in cities on our list are closer to the shop. For comparison, San Pedro is 6.5 miles and Rolling Hills is 7.2 miles away."
          }
        },
        {
          "@type": "Question",
          "name": "Is there an Audio MotorSports shop in Redondo Beach?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. Redondo Beach customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location."
          }
        },
        {
          "@type": "Question",
          "name": "How much is window tint for a Redondo Beach driver?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the Specials page or text the year, make and model to (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get stereo, tint and a car alarm done in one trip from Redondo Beach?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. All three are installed at the same shop, so one drive from Redondo Beach (about 15 to 20 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held."
          }
        },
        {
          "@type": "Question",
          "name": "What do customers from Redondo Beach say about Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city."
          }
        }
      ]
    }
  ]
}
```

**Live-page claims to confirm, soften or keep (nothing is removed by the pilot; owner decides):** "There is no shop at the pier" and "The pin does not move west to the pier" (fine in intent, but pier is not otherwise on the page); "Strand and pier overnight leaves sand in speaker tracks" (unsupported); "a suction cup on Catalina Avenue" (street reference).

### 4.5 San Pedro (`/san-pedro/`, 6.5 miles)

| Item | Live today | Draft |
|---|---|---|
| Title | Car Stereo, Tint & Alarm for San Pedro \| Audio MotorSports (58) | San Pedro Car Stereo, Tint & Alarm \| Audio MotorSports (54) |
| Meta | San Pedro drive-in for car stereo, 3M window tint, and car alarm — one Avalon bay. Call (213) 429-1092. (103) | San Pedro car stereo, window tint and car alarms at our one Carson shop: 6.5 miles, about 15 to 20 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092. (149) |
| H1 | Car Stereo, Tint & Alarm for San Pedro | Car Stereo, Window Tint & Car Alarms for San Pedro Drivers |
| Subhead | none | One shop in Carson, 6.5 miles from San Pedro |
| Intro | 53 words, starts "We are not in San Pedro.", no "Carson" | 58 words, leads with what is offered and says Carson |

**Answer paragraph** (first text under the H1)

> Audio MotorSports installs car stereo, window tint and car alarms at one shop in Carson: 22025 S Avalon Blvd Ste A. There is no shop in San Pedro. You drive in: 6.5 miles, about 15 to 20 minutes, via Gaffey or Harbor Boulevard north, then Avalon. Open Monday to Saturday, 9:30 AM to 6:00 PM. Call (213) 429-1092.

**Route table**

| From San Pedro | Detail |
|---|---|
| Distance | 6.5 miles (data file) |
| Typical drive | about 15 to 20 minutes when traffic is moving (live page) |
| Main route | Gaffey Street or Harbor Boulevard north, then Avalon (live page) |
| Alternate | Pacific Coast Highway, then Avalon (live page) |
| Destination | 22025 S Avalon Blvd Ste A, Carson, CA 90745 ([Google Maps](https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a)) |
| Open | Monday to Saturday, 9:30 AM to 6:00 PM. Sunday closed. Walk-ins welcome. |
| Tint start times | 10:00 AM or 12:00 PM |

**H2: How far is Audio MotorSports from San Pedro, and which way should I drive?**

It is 6.5 miles from San Pedro to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 to 20 minutes when traffic is moving. Main route: Gaffey Street or Harbor Boulevard north, then Avalon. Alternate: Pacific Coast Highway, then Avalon. Twelve other drive-in cities on our list are closer to the shop. For comparison, Lawndale is 6.5 miles and Redondo Beach is 7.2 miles away.

**H2: Is there an Audio MotorSports shop in San Pedro?**

No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. San Pedro customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location.

**H2: How much is window tint for a San Pedro driver?**

Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the [Specials page](/specials/) or text the year, make and model to (213) 429-1092.

**H2: Can I get stereo, tint and a car alarm done in one trip from San Pedro?**

Yes. All three are installed at the same shop, so one drive from San Pedro (about 15 to 20 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held.

**H2: What do customers from San Pedro say about Audio MotorSports?**

Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city.

Dated review slot (each card: quote, first name and initial, reviewer's own city, platform, service, date from the listing):

> "Went in for a quote, Nick ended up giving me a great deal, was not expecting to get my windows tinted that same day."
> Daniel L., San Pedro · Yelp · Quote and same-day tint · [REVIEW-DATE, copy from the Yelp listing]

> "I brought my C10 in for an alarm installation, and Nick was incredibly helpful in getting everything set up. The job was done professionally and efficiently."
> Eddie G., Wilmington · Yelp · Alarm install, C10 · [REVIEW-DATE, copy from the Yelp listing]

Note: One San Pedro quote plus a Wilmington quote, each shown under the reviewer's own city.

**From the shop floor** (owner-supplied slot, 80 to 120 words, omitted if empty)

> [OWNER: 2 to 4 facts about this city. Suggestions to verify, not facts:]
> - Which San Pedro areas customers come from (live page mentions Gaffey, Harbor Boulevard, PCH and 6th Street) [CONFIRM each].
> - Whether Gaffey or Harbor Boulevard is the better default and the time at rush hour [CONFIRM].
> - Port or work-truck customers: the live page says work trucks and a hill daily; confirm what the shop sees [CONFIRM].
> - One real San Pedro job with photo and customer OK [CONFIRM].

**Nearby drive-in cities** (curated by the owner for real adjacency [CONFIRM]; miles from the data file; each also links back here)

| City | Miles from shop | Link |
|---|---|---|
| Wilmington | 3.3 | /wilmington/ |
| Harbor City | 2.8 | /harbor-city/ |
| Rancho Palos Verdes | 9.0 | /rancho-palos-verdes/ |
| Palos Verdes Estates | 8.0 | /palos-verdes-estates/ |

**Price-table link, final CTA:** shared text above.

**JSON-LD** (graph below is added; the live `AutoRepair` node stays as is, see Appendix A)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/san-pedro/#webpage",
      "url": "https://www.audiomotorsports.com/san-pedro/",
      "name": "San Pedro Car Stereo, Tint & Alarm | Audio MotorSports",
      "description": "San Pedro car stereo, window tint and car alarms at our one Carson shop: 6.5 miles, about 15 to 20 minutes. Open Mon-Sat 9:30-6. Call (213) 429-1092.",
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "breadcrumb": {
        "@id": "https://www.audiomotorsports.com/san-pedro/#breadcrumb"
      },
      "dateModified": "[PUBLISH-DATE]"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.audiomotorsports.com/san-pedro/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.audiomotorsports.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Locations",
          "item": "https://www.audiomotorsports.com/locations/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Car Stereo, Tint & Alarm for San Pedro",
          "item": "https://www.audiomotorsports.com/san-pedro/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/san-pedro/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Audio MotorSports from San Pedro, and which way should I drive?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "It is 6.5 miles from San Pedro to the shop at 22025 S Avalon Blvd Ste A in Carson, about 15 to 20 minutes when traffic is moving. Main route: Gaffey Street or Harbor Boulevard north, then Avalon. Alternate: Pacific Coast Highway, then Avalon. Twelve other drive-in cities on our list are closer to the shop. For comparison, Lawndale is 6.5 miles and Redondo Beach is 7.2 miles away."
          }
        },
        {
          "@type": "Question",
          "name": "Is there an Audio MotorSports shop in San Pedro?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745, and every job is done there. We do not do mobile installs. San Pedro customers drive in for car stereo, window tint and car alarms, and this page is a guide to that drive, not a separate location."
          }
        },
        {
          "@type": "Question",
          "name": "How much is window tint for a San Pedro driver?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our posted specials for a four-door sedan, installed, are Solar film $249 and Solar Ceramic $329. That covers four doors plus the back window, not the windshield. Prices were checked on [PRICE-CHECK-DATE]. 3M Ceramic IR is quote-only, and California front side windows are 70% VLT. See current prices on the Specials page or text the year, make and model to (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get stereo, tint and a car alarm done in one trip from San Pedro?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. All three are installed at the same shop, so one drive from San Pedro (about 15 to 20 minutes each way) can cover them. Tint appointments are at 10:00 AM or 12:00 PM, Monday to Saturday, and the shop is closed Sunday. Text the year, make and model to (213) 429-1092 before you leave so a tint slot or bay can be held."
          }
        },
        {
          "@type": "Question",
          "name": "What do customers from San Pedro say about Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Across the whole shop, Google shows 4.8 from 654 reviews and Yelp shows 4.7 from 777 (as of [REVIEW-COUNT-DATE]). Reviews below are quoted from our Yelp listing, with the reviewer's own city."
          }
        }
      ]
    }
  ]
}
```

**Live-page claims to confirm, soften or keep (nothing is removed by the pilot; owner decides):** "There is no shop on 6th Street" (street reference, unsupported); "Richard takes the older metal when a Pedro classic shows up" (staff claim); "A work truck and a hill daily are different tickets. Nick will not mix them." (internal-sounding).

### 4.6 Measured result of the drafts
Counting the new blocks only (answer, subhead, five Q&As, route table text, review quotes, nearby list), sentence-unique to each page among the five drafts, using the method in 2.4:
| Page | New-block words | Unique to the page | Share unique |
|---|---|---|---|
| Torrance | 473 | 127 | 27% |
| Long Beach | 503 | 214 | 43% |
| Gardena | 522 | 176 | 34% |
| Redondo Beach | 492 | 146 | 30% |
| San Pedro | 488 | 142 | 29% |

So verified data alone reaches about 130 to 200 unique words (127 to 202 in the table), below the proposed 300 (cities within 12 miles). The gap of about 100 to 170 words is exactly the "From the shop floor" block and real dated reviews. That is the honest finding: this template cannot make 158 pages unique from the data file; it can make them accurate, answer-first and easy to quote, and it makes room for the facts only the shop knows.

---

## 5. Control-group design

### 5.1 Principle
Five pages change; every other city page stays untouched as the comparison. No page is removed, merged or noindexed in either group. All five pilots and all controls remain live and indexable throughout.

### 5.2 Groups
| Group | Cities | Why |
|---|---|---|
| **Pilot (change)** | Torrance, Long Beach, Gardena, Redondo Beach, San Pedro | The five named as the example pilot in `HUB_FIRST_PLAN.md`; 4.4 to 7.2 miles from the shop; among the most individually written pages today |
| **Matched controls (do not touch)** | Paramount (7.4), Rolling Hills (7.2), Lynwood (7.8), Bellflower (9.3), South Gate (9.3), Inglewood (10.6), Artesia (10.8), El Segundo (10.8), Downey (10.9), Hawaiian Gardens (11.0) | Same hand-written sub-template (hero reads "We are not in {City}. The bay is on Avalon", checked on all ten) at similar distance; all are linked from `/locations/`; none is in a pilot's nearby list, so pilot links do not feed them |
| **Generated-template controls (near, OC, far)** | West Carson, Anaheim, Huntington Beach, Pasadena, Fontana | The generated sub-template (hero reads "Audio MotorSports is one Avalon bay"), one near, two OC, two far; shows whether the whole set moves for reasons unrelated to the pilot |
| **Buffer (untouched, excluded from comparison)** | Lomita, Rolling Hills Estates, Lawndale, Hawthorne, Compton, Signal Hill, Lakewood, Wilmington, Seal Beach, Hermosa Beach, Manhattan Beach, Harbor City, Rancho Palos Verdes, Palos Verdes Estates | These receive new links from the pilots, so they can gain inbound-link benefit. They stay live and unchanged but are not used as controls |
| Excluded from controls | Del Aire, Westmont, Alondra Park and the other 32 pages missing from `/locations/` | Fixing `/locations/` later would change their inbound links |

Pairing rule (set after the baseline pull): for each pilot choose the two matched controls whose 16-week impressions are closest and whose trend lines run parallel before the change; if none are within 25%, pool all ten matched controls.

### 5.3 Freeze rules during the test
* No change to the shared city template, shared footer, sitemap `lastmod`, `/locations/` or the nearby lists of any control page from the baseline date to the final readout. Site-wide fixes from `HUB_FIRST_PLAN.md` that touch every page equally (footer link, banner, price wording) go in **before** the baseline, or wait until after the readout.
* The brand mounts also have city pages for the same cities (for example `/beats/car-stereo-torrance/`, `/tint/window-tint-torrance/`, `/alarm/car-alarm-torrance/`, `/tesla/tesla-tint-torrance/`, `/amspods/bagger-audio-torrance/`). Do not edit those for pilot or control cities during the test, and record in Search Console which URL ranks for each city query so a shift between hub and mount is not read as a gain.
* Keep a saved copy of each pilot page's original and a dated change log.

### 5.4 What to measure
| Metric | Where | Unit and cadence |
|---|---|---|
| Impressions, clicks, CTR, average position | Search Console, Performance, filtered to each page URL | weekly, exported as CSV; pull 16 weeks before go-live for the baseline (Search Console keeps 16 months) |
| City queries | Search Console queries for each page: "{city} car stereo", "{city} window tint", "{city} car alarm", "car audio {city}" and misspellings; note which URL appears | weekly |
| Indexing state | Search Console, Pages report and URL Inspection for each pilot and control: indexed or not, "Crawled - currently not indexed", "Discovered - currently not indexed", last crawl date, canonical chosen by Google | baseline, then day 3, 7, 14, 28, 56 |
| Calls | Phone log: ask each caller where they are coming from and what they searched; tally by city; Google Business Profile call counts for context (not city-specific) | daily tally, weekly total |
| Texts | The text line (213) 429-1092 receives all texts; ask "which city, and how did you find us"; tally by city | daily tally, weekly total |
| Click-to-call and click-to-text | GA4 events on `tel:` and `sms:` links by landing page, if a Google Tag Manager tag for them exists [CONFIRM: a GTM container is present in the page source; whether click events are configured is not known] | weekly |
| Quote requests | `/contact/` form submissions by landing page or city field, if tracked [CONFIRM] | weekly |
| AI answers | Re-run the city queries from `AI_VISIBILITY_QUERY_SET.md` (for example "car audio shop torrance") per engine, same list, same engines, dated | baseline, week 4, week 8 |
| Guardrails | Pilot page speed and mobile layout (no new layout shift in the answer block), a crawl of the 10 pilot and control URLs | at go-live and day 14 |

### 5.5 How long
| When | Action |
|---|---|
| Baseline, before go-live | 16-week Search Console export per page, indexing state, AI query run, phone and text tally started so there is a pre-change count (minimum 2 weeks of tally) |
| Day 0 | Zack and Tom approve the drafts together; five pages published together; Zack uses URL Inspection "Request indexing" on the five |
| Day 3, 7, 14 | Indexing and crawl-date check; page-speed spot check; no other site changes |
| Day 28 | First readout, directional only |
| Day 56 | Decision readout (8 weeks gives Google time to recrawl and settle) |
| Day 84 | Final readout; used whenever the pooled pilots have fewer than 30 clicks over the first 8 weeks |

### 5.6 Decision rules (set in advance)
* **Success:** pooled pilot impressions and clicks grow at least 20% more than the pooled controls over four consecutive weeks (difference in differences against the baseline), the pilots are all indexed, and calls or texts attributed to the pilot cities do not fall.
* **Neutral:** inside 20%; keep the pilots, extend to day 84, change nothing else.
* **Harm:** any pilot drops out of the index, or loses more than 25% of impressions against its controls for three consecutive weeks. Action: put that page's saved original back (the page stays live throughout), then diagnose.
* **Low volume warning:** if the pilots' pooled clicks stay under 30 across 8 weeks, only the indexing state and impressions are used for the decision; clicks are reported but not tested.
* **Roll-out order if it works:** the other cities within 12 miles (48), then 12 to 35 miles (97), then beyond (14), in waves of about 10 pages, each wave with its own untouched comparison.

### 5.7 Confounders to log
Google algorithm updates, seasonal tint demand (summer heat), the Sunday "Closed today" banner, changes to the Google Business Profile or Yelp listings, changes on lacarbeats.com, lacartint.com, lacaralarm.com and the shop subdomain that link to the city pages, and any ad spend that points to a pilot city.

---

## 6. Appendix A: the live `AutoRepair` node (unchanged, shown once)
Copied from the live `/torrance/` page on 2026-10-07. Each city page carries the same node with its own `url` and `areaServed.name`. The email field, string coordinates and the 4.8 / 654 `aggregateRating` are separate decisions (`SCHEMA_REPORT.md`) and are deliberately not changed in the pilot.
```json

{
  "@context": "https://schema.org",
  "@type": "AutoRepair",
  "name": "Audio MotorSports",
  "alternateName": [
    "Audio MotorSports",
    "Audio Motorsports",
    "AMS"
  ],
  "url": "https://www.audiomotorsports.com/torrance/",
  "telephone": "+13105138800",
  "email": "audiomotorsports@gmail.com",
  "image": "https://www.audiomotorsports.com/assets/img/og/hub-og.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "22025 S Avalon Blvd Ste A",
    "addressRegion": "CA",
    "postalCode": "90745",
    "addressCountry": "US",
    "addressLocality": "Carson"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "33.8270",
    "longitude": "-118.2650"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ],
      "opens": "09:30",
      "closes": "18:00"
    }
  ],
  "areaServed": {
    "@type": "City",
    "name": "Torrance"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "654",
    "bestRating": "5",
    "worstRating": "1"
  },
  "employee": [
    {
      "@type": "Person",
      "name": "Zack",
      "jobTitle": "Operational Manager"
    },
    {
      "@type": "Person",
      "name": "Nick",
      "jobTitle": "Sales · Acoustic Audio"
    }
  ],
  "@id": "https://www.audiomotorsports.com/#business",
  "sameAs": [
    "https://www.youtube.com/channel/UCHYn2FTtiBZ53EXWNBWAyeg",
    "https://www.instagram.com/audiomotorsports/",
    "https://share.google/RyQaFlk39cTTMU6TG",
    "https://www.facebook.com/Audiomotorsports/",
    "https://www.tiktok.com/@audiomotorsports",
    "https://yelp.to/Lm2GAc4OiS",
    "https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a",
    "https://www.lacarbeats.com/",
    "https://www.lacartint.com/",
    "https://www.lacaralarm.com/",
    "https://www.amspods.com/",
    "https://teslatintla.com/"
  ],
  "subOrganization": [
    {
      "@type": "AutoRepair",
      "name": "LA Car Tint",
      "url": "https://www.lacartint.com/",
      "@id": "https://www.lacartint.com/#business"
    },
    {
      "@type": "AutoRepair",
      "name": "LA Car Beats",
      "url": "https://www.lacarbeats.com/",
      "@id": "https://www.lacarbeats.com/#business"
    },
    {
      "@type": "AutoRepair",
      "name": "LA Car Alarm",
      "url": "https://www.lacaralarm.com/",
      "@id": "https://www.lacaralarm.com/#business"
    },
    {
      "@type": "AutoRepair",
      "name": "AMS Pods",
      "url": "https://www.amspods.com/",
      "@id": "https://www.amspods.com/#business"
    },
    {
      "@type": "AutoRepair",
      "name": "Tesla Tint LA",
      "url": "https://teslatintla.com/",
      "@id": "https://teslatintla.com/#business"
    }
  ]
}
```

---

## 7. Decisions and [CONFIRM] list for Zack and Tom

**Decisions**
| # | Decision | Recommendation |
|---|---|---|
| D1 | Approve the block order in 2.2 | Approve; it follows the order you asked for, with the retained copy moved below |
| D2 | Who writes "From the shop floor" for each pilot, and by when | Zack or Nick, 2 to 4 true facts per city, ideally from invoices and photos; without them the pages stay below the unique-word minimum |
| D3 | Keep all existing long copy below the new blocks (as drafted) or replace the repeated paragraphs with unique local content later | Keep for the pilot so the test isolates the new blocks; consider replacement in wave 2, as a rewrite that is not shorter |
| D4 | Price table target | Link `/specials/` now; switch to the dated price table when built (`HUB_FIRST_PLAN.md` fix 6) |
| D5 | Approve the pilot nearby lists and the control and buffer cities in section 5 | Approve after the owner checks adjacency |
| D6 | Whether to make `/locations/`, `llms.txt` and the data file agree on the service area (123 / 158 / 159, 15.5 / 35 / 86.8 miles) | Yes, after the test window or on pages outside it |
| D7 | `/orange/` (in data file, redirects) | Not part of the pilot; decide separately whether to add a real Orange page |

**[CONFIRM] before anything is published**
* Every drive time and route name in the drafts (they come from the live city pages, which may themselves be template text); peak-hour times.
* The text number (213) 429-1092 as the number to show on city pages (it is on the live site and in `llms.txt`).
* The tint prices ($249 Solar, $329 Solar Ceramic, "four doors plus back window, no windshield") and a "checked on" date; `llms.txt` says "Prices verified September 2026".
* The rating lines (Google 4.8 from 654, Yelp 4.7 from 777) and an "as of" date.
* The date, service and city on each quoted review, copied from the listing; permission to publish any photo.
* Nearby-city adjacency for each pilot, and every item in the "From the shop floor" suggestions.
* "3M Authorized Dealer", "Diamond Certified Viper dealer" and similar certification wording on the live pages: not used in the drafts; confirm before they are reused.
* Quarterly review cadence.

**Limits.** Search Console, GBP and call data were not available, so nothing here says how the city pages perform today or whether Google has indexed them. Sentence-sharing is measured on exact sentence matches after normalising the city name and digits, so it understates looser repetition. "Unique words" count text that differs, not text that is true. Review parsing used the visible quote cards; the count of 12 distinct quotes is approximate. Standalone brand domains are blocked from this environment and were not checked. Neighbourhood, landmark, freeway-exit and vehicle details in the drafts are all prompts for the owner, not facts. Page fetches were made through the sandbox proxy with retries on transient resets. This file and its scripts are the only things written.
