# Google AI Overviews (AIO) + GEO Addendum: lacarstereo.com

Date: 2026-10-04 (UTC). Read-only. Nothing on any site or repo was changed. Rules applied: _phase1/RULES.md (no page is ever trimmed, merged, redirected, canonical-ed away or noindexed; every recommendation improves pages).
This addendum builds on AUDIT_REPORT.md, AI_SEARCH_REPORT.md, SCHEMA_REPORT.md and pages.csv; it does not repeat them. Evidence was re-fetched today from https://lacarstereo.com with curl. Items marked (unverified) are inference.

Limitation: https://www.lacarstereo.com is blocked by the egress proxy (CONNECT 403, re-tested today for /robots.txt). The www host, its headers and its redirect behaviour are NOT verified. Everything below is from the apex host. The sitemap, canonicals and JSON-LD declare www as the host.

## 1. AIO eligibility today (re-verified)

AIO eligibility = indexed by Googlebot and snippet-eligible (not noindex, no nosnippet or max-snippet:0, not blocked for Googlebot). Google-Extended is irrelevant to AIO.

| Check | Result today (apex) | Changed since earlier audit? |
|---|---|---|
| robots.txt (HTTP 200, `last-modified` Sun 2026-10-04 03:21:54 GMT, i.e. from the latest deploy) | AdsBot-Google and AdsBot-Google-Mobile `Allow: /`; Googlebot `Allow: /locations/`; `*` `Disallow: /`; Sitemap line points at www | No, identical |
| Googlebot under that file | Its own group has only an Allow line, so no Disallow applies: Googlebot may crawl every URL (RFC 9309; Google follows the most specific group). Every other bot falls under `*` and is blocked everywhere | No |
| Meta robots, fetched today | `/`, `/faq/`, `/packages/`, `/install/carplay/`, `/shop/carplay-stereos/`, `/about/`: `noindex, nofollow`. `/locations/`: `index, follow` | No (pages.csv: 124 of 127 noindex) |
| X-Robots-Tag header | None on any response checked (robots.txt, sitemap.xml, 404 and the 7 pages above) | No |
| User-agent test: curl as Googlebot and as GPTBot to /faq/ | HTTP 200 for both, so there is no server-side UA blocking (WAF/bot rules); robots.txt and meta are the only gates | New check |
| Snippet controls (nosnippet, max-snippet, data-nosnippet) | None seen in the 7 pages fetched | Same |
| llms.txt | HTTP 404 (HTML 404 page) | No |

Verdict: only /locations/ is AIO-eligible today, and it has no answer content (a list of 123 names with miles). All money pages (installs, FAQ, packages, categories, products) are ineligible because of the page-level noindex. A robots Disallow is not the blocker for Google; the meta noindex is.

Intent (intentional pre-launch or not) is still UNKNOWN. Evidence that suggests deliberate gating (unverified inference): the robots file is hand-written with an AdsBot allow (so paid ads can be reviewed) and a single Allow for /locations/; the noindex is applied uniformly by template; the robots file was regenerated at the latest deploy and kept the same content. Evidence that suggests accident: the policy pages are indexable while the money pages are not, and the sitemap is submitted listing noindex URLs. Treat "confirm launch intent with Zack" as step zero; the rest of this report is the plan for the moment the site is allowed to be indexed. Note the Search Console "Search generative AI" control also exists (per the seo-geo skill, since 2026-08-31); it was not checked (no GSC access).

## 2. What "AIO-ready" looks like once indexable

Google's own position (via the seo-geo skill): optimizing for AI search is still SEO. No special markup, chunking or llms.txt is required. The work below is ordinary SEO with passages written so they can be quoted.

### 2.1 Answer-first passages (40 to 80 words, directly under a question-style heading)

Current state, fetched today:
- /install/carplay/ has H2s "What's included", "Price and time", "Cars we already have a price for"; none is a question and there is no prose answer. About 357 words, 32 list items, 0 tables.
- /faq/ has 8 Q&As as text, one H1 and no H2/H3 (questions are not headings, so they are weaker anchors). 428 words.
- /packages/ has useful H2s ("What goes into the number") but no direct answer paragraph. 382 words.
- Category pages (e.g. /shop/carplay-stereos/) have one H2 and a single intro line; 474 words.
- /packages/<car>/ pages are the strongest (about 1,225 words for the F-150: itemised price table, "About 2 hours in the bay", a "Questions about this car" block with H3s). No visible "last updated" date anywhere (0 `<time>` elements on all 8 pages fetched).

Pattern to apply: convert the heading to the question a customer types, put a 40 to 80 word answer first with the number in it, then the detail list. Concrete drafts are in section 6. Use only facts already on the site, or mark [CONFIRM].

### 2.2 FAQ copy vs FAQPage schema parity
- Fetched today: zero `FAQPage` in /faq/ or any of the 8 pages checked (consistent with SCHEMA_REPORT.md). The F-150 page has its own visible Q&As ("Does this fit my F-150?", "What are all these parts for?", "How long does it take?") and no matching markup either.
- Parity rule when adding it: every Question/Answer in the JSON-LD must be word-for-word the visible text on the same page, and every visible Q&A should be in the markup (8 on /faq/). Do not put FAQPage on pages where the questions are not visible. Google restricts FAQ rich results for most sites, so the value is machine parsing and consistency, not a SERP feature (labelled: Google guidance, not re-verified today).
- Make the FAQ questions real headings (H2 or H3) so the visible structure matches the schema.
- Move per-service questions onto each /install/* page (3 to 5 each) with matching FAQPage; keep /faq/ as the hub. Two of the existing /faq/ answers contain the strongest quotable facts: the steering-wheel/backup-camera answer and the CarPlay-without-replacing-the-screen answer.

### 2.3 Tables for prices and labor
- 0 `<table>` on /install/*, /packages/, /faq/ and category pages; only the car package pages have one table. Prices appear as list text ("2009-2014 Ford F-150 from $629.94").
- Add to each /install/* page a real HTML table: rows = car (or job), columns = head unit / parts / labor / installed total / time in the bay. On /packages/ add one table of all priced cars.
- Reconcile "Labor from $149" (install pages) with "$300 installation, about 2 hours" on the F-150 package (AUDIT_REPORT.md finding 9) with a one-line explanation in the table caption, since AIs will quote both numbers. Add "Prices checked on <date>" (visible, `<time>`).
- Keep "plus sales tax; no shop supply or disposal fee" next to every total (this phrase is already on the F-150 page and is a good citation detail).

### 2.4 E-E-A-T and entity signals
| Signal | Today (verified) | Gap / next |
|---|---|---|
| NAP | 22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; Mon to Sat 9:30 to 6:00, Sunday closed. Consistent on page, footer and schema | Add E.164 in schema; show SMS line (213) 429-1092 only after confirming it belongs to this brand (it is used in sms: links; unverified as public) |
| Name | "LA Car Stereo, an Audio MotorSports Inc shop"; legalName and parentOrganization in schema | Good |
| sameAs | Six sister domains only | Add GBP/Maps URL, Yelp, Facebook (a Maps URL and Facebook link already exist in the /locations/ duplicate block) |
| Named people | "Ask for Nick" appears once, on /locations/; none on /about/ | Add named installers with role, years, specialties, photo; Person schema only for real people who consent |
| Experience | "Since 2003", "installed car audio in Carson since 2003", 4.8 from 654 Google reviews (claim, no markup, correct not to add aggregateRating) | Add quoted, attributed reviews with link to the Google profile; gallery captions with car, parts, hours |
| Freshness | No dates | Visible "Prices checked" and "Last updated" dates on pricing pages; real `lastmod` in sitemap |
| Other proof | Photographs of cars at check-in are mentioned in FAQ | Publish that process with photos |

### 2.5 Structure for AIO beyond passages
- Internal links: install pages link to 4 priced cars each; /packages/ links the per-car pages. Add reciprocal links: each package page to its install page, each install page to relevant FAQ answers, /locations/ region sections to the matching install pages.
- Server-rendered Next.js (full text in raw HTML, verified earlier), so no JS dependency for crawlers.
- Product pages (101): thin; see AUDIT_REPORT.md finding 5. They matter for AIO on part-specific queries ("Kicker 46CSC464 4x6 speakers").

## 3. /locations/: improve, never trim (123 cities stay)

Fetched today: H1 "LA Car Stereo", H2 "Where you drive from", 123 cities with miles (West Carson 1.8 mi up to Lancaster 86.8 mi per earlier audit), "One shop. 123 cities.", "Ask for Nick", index, follow. This is the one page Google may index today.

Superseded: AUDIT_REPORT.md finding 6 suggested reducing the page to "10 to 15 nearby cities". That conflicts with RULES.md (see section 10). The correct approach keeps all 123 cities and adds real content around them:

1. Title and H1 that say what the page is: for example H1 "Car stereo installation near you: one Carson shop, 123 cities" (title without the repeated brand).
2. An answer-first passage under "Where is LA Car Stereo and who do you serve?": address, hours, phone, one bay, drive from the 123 cities listed below, in 40 to 80 words.
3. Group the 123 cities under regional H2/H3 headings (for example South Bay, Harbor area, Gateway Cities, Westside, Central and South LA, Orange County border, Antelope Valley/far areas). Keep every city name visible. Under each group add genuine, checkable content: the nearest freeways and typical drive from that area, whether customers there usually drop off or wait (only if true), and which services are most requested from that area (needs shop data; mark [CONFIRM] until supplied).
4. Real local proof, not boilerplate: a map embed with directions, parking and drop-off notes, photos of the bay and of work, reviews from customers by city (with permission and the reviewer's visible city on Google), and named staff (Nick).
5. Link each region to relevant install pages and the packages that fit common local cars.
6. Optional later project, only where unique facts exist: individual city or region pages (for example /locations/long-beach/) with unique content (local drive guidance, customer examples, local reviews, vehicle trends from real job records). Each stays live and gets its own differentiation. No city page is ever canonical-ed to another or noindexed.
7. Schema: one `#business` entity (merge the duplicate LocalBusiness; see SCHEMA_REPORT.md), `areaServed` as a list of City objects that matches the visible regions, `geo`, `hasMap`. Visible text and schema must say the same thing (today: 123 visible vs 10 vs "California" in schema).
8. Fix the stretched claim "We serve the entire LA area" to state the real range, since Lancaster is 86.8 mi away (earlier audit).

## 4. AI-crawler access matrix (apex robots.txt, fetched today)

Each bot is listed with the capability it governs. No UA blocking at the server (Googlebot and GPTBot UA both got 200 on /faq/).

| User-agent | Governs | robots.txt result | Page-level result |
|---|---|---|---|
| Googlebot | Google Search index; source of AI Overviews and AI Mode | Allowed (own group, Allow only) | noindex on 124/127 pages, so not eligible; /locations/ eligible |
| AdsBot-Google, AdsBot-Google-Mobile | Google Ads landing page checks (not Search or AIO) | Allow: / | n/a |
| Google-Extended | Gemini/Vertex training and grounding, and models behind Search gen-AI features; NOT Search inclusion or AIO | Blocked (`*`) | n/a |
| Bingbot | Bing index, which feeds Copilot and other products | Blocked (`*`) | noindex also present |
| OAI-SearchBot | ChatGPT Search citability | Blocked | noindex also present |
| GPTBot | OpenAI training only | Blocked | Business choice |
| ChatGPT-User | User-triggered browsing; OpenAI says robots rules may not apply | Blocked in file (may not be enforced) | n/a |
| Claude-SearchBot | Claude search citability | Blocked | n/a |
| ClaudeBot | Anthropic training only | Blocked | Business choice |
| Claude-User | User-triggered fetch; honors robots | Blocked | n/a |
| PerplexityBot | Perplexity search | Blocked | n/a |
| Perplexity-User | User-triggered; generally ignores robots | Blocked in file (likely not enforced) | n/a |
| Applebot | Siri/Spotlight/Safari discovery | Blocked | n/a |
| Applebot-Extended | Apple Intelligence training opt-out only | Blocked | Business choice |
| CCBot | Common Crawl training | Blocked | Business choice |

Recommended direction (when the owner decides to launch; this is a recommendation, not a change): one `User-agent: *` group that allows the site, with `Disallow` only for cart/checkout style paths; keep search bots (Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, PerplexityBot, Applebot) allowed. Training crawlers (GPTBot, ClaudeBot, CCBot, Google-Extended, Applebot-Extended) are a licensing preference and have no effect on AIO. Remember that a Disallow prevents a bot from seeing a noindex; do not combine the two for the same bot.

## 5. llms.txt

Status: missing (404, re-verified). Google states llms.txt is not used by Google Search and does not help or hurt AIO. Publish it only as a convenience for other agents; it must be accurate and stay in sync with the site. Recommended body (factual only: every line comes from the live site or earlier audit; items in [CONFIRM] must be checked by the owner before publishing; host shown as www because that is what the site declares, adjust to the final canonical host):

```
# LA Car Stereo

> LA Car Stereo is a car audio installation shop in Carson, California, run by Audio MotorSports Inc. It has installed car audio in Carson since 2003. Prices on the site include the installation.

## Business facts
- Legal name: Audio MotorSports Inc
- Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745
- Phone: (310) 513-8800
- Hours: Monday to Saturday 9:30 AM to 6:00 PM. Sunday closed.
- One shop with one installation bay, in Carson.
- Service area: customers drive in from 123 listed cities in the Los Angeles area; see /locations/.
- Appointments: required; book online, call, or text. Same-day is possible at opening, Monday to Saturday. No deposit to book.
- Drop-off: overnight drop-off Tuesday through Thursday, by 6 PM, pick up next day.
- Google reviews: 4.8 stars from 654 reviews as shown on the site [CONFIRM current count and link to the Google profile].

## Pricing facts (from the site; confirm before publishing)
- Car stereo installation labor starts from $149; many cars are done the same day.
- Package prices show parts and labor separately, plus sales tax. No shop supply or disposal fee.
- Example: 2009-2014 Ford F-150 with a Kenwood DMX5710S: radio $459, parts $29.99, installation $300, total $788.99 plus sales tax; about 2 hours in the bay.
- Price match: on head units and install-only work when the part is the same.
- Payment plans are available; see /pay-later/ [CONFIRM path and provider names]. Do not state APR or monthly amounts.

## Key pages
- [Installed packages by car](https://www.lacarstereo.com/packages/): installed prices for specific vehicles
- [Apple CarPlay and Android Auto install](https://www.lacarstereo.com/install/carplay/)
- [Car stereo install](https://www.lacarstereo.com/install/stereo/)
- [Subwoofer install](https://www.lacarstereo.com/install/subwoofer/)
- [Amplifier install](https://www.lacarstereo.com/install/amplifier/)
- [Speaker install](https://www.lacarstereo.com/install/speakers/)
- [DSP install](https://www.lacarstereo.com/install/dsp/)
- [Luxury and factory-screen integration](https://www.lacarstereo.com/install/luxury/)
- [CarPlay and Android Auto stereos](https://www.lacarstereo.com/shop/carplay-stereos/)
- [Subwoofers](https://www.lacarstereo.com/shop/subwoofers/)
- [Amplifiers](https://www.lacarstereo.com/shop/amplifiers/)
- [FAQ](https://www.lacarstereo.com/faq/)
- [Locations and drive distances](https://www.lacarstereo.com/locations/)
- [About](https://www.lacarstereo.com/about/)

## Related brands (same company)
- Audio MotorSports: https://www.audiomotorsports.com/
- Tesla Tint LA: https://teslatintla.com/
```
(Install page slugs for stereo, subwoofer, amplifier, speakers, dsp, luxury come from the 7 /install/ URLs in pages.csv; the /pay-later/ path is a guess and must be checked.)

## 6. Ten sample queries: target page and passage to add

All passages use only site facts; [CONFIRM] marks anything to supply. Place each directly under a question-style H2, with matching FAQ schema where noted. Length targets 40 to 80 words.

1. car stereo installation carson ca. Target: homepage and /install/stereo/ (and /locations/ for the near-me intent). H2 "Where can I get a car stereo installed in Carson?" Passage: "LA Car Stereo installs car stereos at 22025 S Avalon Blvd Ste A in Carson, CA 90745, Monday to Saturday, 9:30 AM to 6:00 PM. Labor starts from $149 and most cars are done the same day. Every price on this site includes the installation, so you see the total before you book. Call (310) 513-8800 or book a slot online."
2. apple carplay install los angeles. Target: /install/carplay/. H2 "How much does Apple CarPlay installation cost in Los Angeles?" Passage: "CarPlay installation at our Carson shop starts with labor from $149. The installed price includes the head unit, dash kit and wiring harness for your car, steering wheel control interface where needed, antenna adapter, a reconnected backup camera and a routed microphone. A 2009-2014 Ford F-150 starts at $629.94 installed, plus sales tax. Most cars are done the same day."
3. how long does a car stereo install take. Target: /faq/ and /install/stereo/. H2 "How long does a car stereo install take?" Passage: "A typical head unit install takes about 2 hours in the bay; our 2009-2014 Ford F-150 package is quoted at about 2 hours. Amp installs usually finish the same day. Book a 10:00 AM or 12:00 PM slot, Monday to Saturday, and we text you when the car is ready. [CONFIRM typical range for other cars.]"
4. can i add carplay to my factory screen. Target: /faq/ plus /install/carplay/ (luxury section). H2 "Can I add CarPlay without replacing my factory screen?" Passage: the existing FAQ answer ("Yes. Wireless CarPlay adapters add CarPlay and Android Auto on the factory screen... Some cars still need a new head unit.") plus a table of which makes need an adapter vs a new unit [CONFIRM from shop knowledge]. FAQPage markup, word-for-word.
5. car stereo installation cost near me / how much does car stereo installation cost. Target: /packages/ and /install/stereo/. H2 "How much does car stereo installation cost?" Passage: "Labor starts from $149 at LA Car Stereo; the total depends on the car. Example: a Kenwood DMX5710S in a 2009-2014 Ford F-150 is $788.99 installed: $459 radio, $29.99 dash kit, $300 installation, plus sales tax, with no shop supply or disposal fee." Then the price table. Add "Prices checked <date>".
6. subwoofer and amp installation long beach. Target: /install/subwoofer/, /install/amplifier/, region section of /locations/ ("Long Beach 5.7 mi"). H2 "Do you install subwoofers and amplifiers for Long Beach drivers?" Passage: "Long Beach is 5.7 miles from our Carson shop. We install subwoofers and amplifiers in one bay, wired, fused and set properly; most amp installs finish the same day. Book a 10:00 AM or 12:00 PM slot Monday to Saturday." [CONFIRM typical drive time and any Long Beach customer example.] Repeat per region on /locations/.
7. can i bring my own car stereo to be installed. Target: /faq/. H2 "Can I bring my own equipment?" Passage: existing answer ("Yes. Bring the head unit, amp, or speakers and we install them. Tell us what you're bringing plus the year, make, and model, and we'll quote the install for that car.") plus install-only labor from $149 and the price-match statement. Keep it as a headed FAQ with schema.
8. car audio shop open sunday los angeles. Target: /faq/ and /about/. H2 "Is LA Car Stereo open on Sunday?" Passage: "No. LA Car Stereo is open Monday to Saturday, 9:30 AM to 6:00 PM, and closed on Sunday. Same-day installs are possible at opening, Monday to Saturday. You can book a slot online or call (310) 513-8800." Answers the intent honestly and removes the schema Sunday 00:00 conflict.
9. 2010 ford mustang carplay install. Target: /packages/2010-2014-ford-mustang/ (the slug pattern follows the F-150 page; verify). H2 "How much is CarPlay for a 2010-2014 Ford Mustang?" Passage: "A 2010-2014 Ford Mustang CarPlay install starts at $1,279.94 installed, plus sales tax, at our Carson shop. The price includes the stereo, the dash kit and harness for your car, and the labor. [CONFIRM time in the bay.] We confirm your exact trim at check-in before any work starts."
10. car stereo installation torrance (also Gardena, Compton, Lakewood, Inglewood). Target: /locations/ region section "South Bay" and /install/stereo/. H2 "Car stereo installation for Torrance drivers" Passage: "Torrance is 4.4 miles from LA Car Stereo in Carson. We install CarPlay stereos, subwoofers, amplifiers and speakers, with labor from $149 and most cars done the same day. Drop off Tuesday to Thursday for overnight installs, or book a morning slot." [CONFIRM route and any Torrance customer story.] Same pattern for Gardena (4.9 mi), Compton (5.4 mi), Lakewood (7.7 mi) and Inglewood (10.6 mi) from the verified distances on /locations/.

## 7. Prioritized list

Columns: page | problem | report | impact | effort | exact next step. Step zero for everything: confirm with Zack whether the noindex/robots state is intentional pre-launch.

| # | Page | Problem | Report | Impact | Effort | Exact next step |
|---|---|---|---|---|---|---|
| 0 | Sitewide | Launch intent unknown; 124/127 noindex, robots `*` Disallow (re-verified today, unchanged) | AIO_REPORT s1, AUDIT_REPORT 1-2 | google, ai | quick | Zack confirms the date the site should become indexable; record it in the report. Nothing is changed by this audit. |
| 1 | /, /install/*, /packages/*, /faq/, /shop/*, /about/ | noindex,nofollow makes them AIO-ineligible | AIO_REPORT s1 | google, ai | quick | At launch, remove the noindex from the shared metadata template for these routes; fetch 6 sample URLs and confirm no `robots` meta and no X-Robots-Tag. |
| 2 | /robots.txt | `*` Disallow blocks Bing, OAI-SearchBot, Claude-SearchBot, PerplexityBot | AIO_REPORT s4 | ai | quick | At launch, replace with one `*` group that allows the site (disallow cart/checkout only); decide separately on training bots. Re-test with a UA fetch. |
| 3 | /install/* (7 pages) | No question headings or answer-first passages; no tables; no dates | AIO_REPORT s2.1, s2.3, s6 | google, ai | medium | Per page: rename H2s to questions, add the 40-80 word passage from s6, add a price/labor table and "Prices checked <date>". |
| 4 | /faq/ | Questions are plain text not headings; no FAQPage | AIO_REPORT s2.2 | ai | quick | Make each of the 8 questions an H2/H3 and add FAQPage JSON-LD with identical text. |
| 5 | /install/* | No per-service FAQs | AIO_REPORT s2.2 | google, ai | medium | Add 3 to 5 visible Q&As per page with matching FAQPage markup (no mismatches). |
| 6 | /packages/ and /packages/<car>/ | Prices in text not tables; labor $149 vs $300 unexplained; no freshness date | AIO_REPORT s2.3; AUDIT_REPORT 9 | google, ai | medium | Add one all-cars price table and a labor explainer sentence; show "Prices checked <date>". |
| 7 | /locations/ | List of 123 cities with no local content; claim "entire LA area"; one dup LocalBusiness | AIO_REPORT s3; SCHEMA_REPORT | google, ai | project | Keep all 123; add region groupings with real local content, map, directions, named staff, local reviews; merge schema into #business with matching areaServed. |
| 8 | /locations/ | Weak title, H1 "LA Car Stereo" | AIO_REPORT s3; AUDIT_REPORT 6 | google | quick | Retitle and re-H1 as in s3 item 1; add the answer-first passage. |
| 9 | /about/ | No named people, no experience proof | AIO_REPORT s2.4 | google, ai | medium | Add named installers with years/specialties, process photos, attributed reviews with a link to the Google profile. |
| 10 | Sitewide schema | sameAs lists only sister domains; no GBP/Yelp/Facebook | SCHEMA_REPORT; AIO_REPORT s2.4 | ai | quick | Add GBP/Maps, Yelp, Facebook URLs (once confirmed by owner) to #business sameAs. |
| 11 | Category pages | One H2, one intro line, no answers | AIO_REPORT s2.1 | google | medium | Add a "How do I choose..." answer-first passage and a comparison table of the priced options. |
| 12 | /llms.txt | Missing | AIO_REPORT s5 | ai (not Google) | quick | Publish the s5 body after the owner confirms the [CONFIRM] lines. |
| 13 | Sitemap | Identical build lastmod, noindex URLs listed | AUDIT_REPORT 7 | google | quick | Use real content-change dates; do not drop any city or location page. |
| 14 | Host | www vs apex unverified (proxy block) | AUDIT_REPORT 3 | google | quick | Someone with access verifies www redirect behaviour; then align robots Sitemap, canonicals and schema to one host. |

## 8. Not measured
No Search Console, no GBP or Yelp data, no live AI-engine query results, no CWV, www host unreachable. AIO inclusion for any query cannot be predicted from here; the sample queries are targets, not forecasts.

## 9. Evidence log (today, apex)
robots.txt 200 (last-modified 2026-10-04 03:21:54 GMT); llms.txt 404; sitemap.xml 200; meta robots as in s1; no X-Robots-Tag; UA tests 200; www robots.txt proxy 403; FAQPage absent on /faq/ and 7 other pages; tables 0 except the F-150 package page (1).

## 10. SUPERSEDED RECOMMENDATIONS (conflict with RULES.md)
1. AUDIT_REPORT.md finding 6, "make /locations/ an honest service-area page (shop details, directions, map, 10 to 15 nearby cities...)" and "doorway-style" framing: superseded. Do not reduce the list. Keep all 123 cities and add real local content (s3).
2. AUDIT_REPORT.md finding 6, "consider a few genuine pages for South Bay, Long Beach and OC": kept only as additive improvements; no city page is ever merged, redirected, canonical-ed or noindexed (s3 item 6).
3. AUDIT_REPORT.md finding 7, "include only indexable URLs" in the sitemap, and "keep noindex on /cart/, /book/ confirmation states and /fit/ if desired": must never be applied to any city or location page; the sitemap should keep every location URL. Utility pages (cart, booking state) are not city or location pages, so those are unaffected.
4. SCHEMA_REPORT.md "areaServed ... 10 cities": do not shrink visible or schema coverage to 10; align schema to the full improved region structure instead (s3 item 7).
5. AI_SEARCH_REPORT.md says "Google-Extended blocked" in a bot table without saying it does not affect AIO; read it with s4 here (Google-Extended is not an AIO/Search control).
6. AI_SEARCH_REPORT.md priority "publish /llms.txt using the hub file as template": still fine, but downgraded to ai-only, not a Google/AIO factor.
