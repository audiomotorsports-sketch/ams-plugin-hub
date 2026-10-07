# City-page rewrite brief (every writer agent reads this first)

READ-ONLY toward the world: never change, commit, push, deploy or delete anything on any site, repo or account. Write ONLY inside ~/ams-seo-audit-2026-10-03/city_rewrite/<site>/drafts/ (one file per page: <slug>.md). Scratch in mktemp -d. No forms, no contact.

## Owner rules (Zack)
- Every page stays live. These are ADDITIVE rewrites: a page gets a new, fully unique body. Nothing is deleted, merged, redirected or noindexed. Zack and Tom review and publish; you publish nothing.
- Keywords stay in. Every page must carry the services the shop advertises, each paired with the city name and with Carson: window tint / ceramic window tint, car audio & car stereo installation, subwoofers & amplifiers, Apple CarPlay / Android Auto, car alarms & remote start, GPS tracking, dash cameras, Tesla window tint, Harley bagger audio (AMS pods). Use them naturally in headings and answers; no stuffing (no keyword repeated more than it would be in normal speech).
- Facts you may state (verified on the site): Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745; call (310) 513-8800; text (213) 429-1092; Mon-Sat 9:30-18:00, Sunday closed; one shop, one bay, customers drive in from the city (no storefront in that city, say so plainly and positively, never "We are not in X" as the opener). "Avalon" is the street name; never use it as a city or placeholder.
- Distances: use ONLY the miles figure given for the city in city_list.json (from the site's own data file). You may say "about N miles / roughly a X-minute drive outside rush hour" where X is computed at an honest 25-30 mph average; mark drive time (approx) and nothing else.
- Prices you may quote (identical across the site): window tint Solar $249, Solar Ceramic $329 (installed); Viper 3108V alarm $269 installed; Compustar 9910 remote start from $499; AMS Harley pods from $649 a pair; Dual Kicker Comp box $249 box only. Always write "as of October 2026" next to any price. No other prices. No Tesla model prices (they conflict on the site). No warranty terms, no APR/financing terms beyond "payment plan available, ask Nick".
- Do NOT invent: landmarks, freeway exits, neighborhoods, street names, local events, customer stories, named customers, vehicle jobs, review quotes, years in business, certifications, "3M authorized" or any dealer status. Where local color would help, insert exactly one slot: [SHOP NOTE: 2-3 sentences from Nick about <city> customers, routes or jobs]. Max 2 slots per page.
- No internal voice ever: never write "we do not invent", "do not reverse", "never imply", "schema", "locked", "placeholder", "TODO".

## What makes each page unique (the 85% problem)
Each page is written fresh, not from a template. Vary: the opening angle, which service leads, question wording, sentence rhythm, which neighbor cities are linked, which FAQ topics appear. Rotate the lead service by city position in the batch (tint / audio / alarm-remote-start / Tesla / Harley / CarPlay) so adjacent cities do not match. A reviewer should not be able to swap city names and get another page. Target 450-650 words of body (excluding JSON-LD). No sentence may be reused verbatim across pages in your batch; check with the dedupe step below.

## Page structure (same bones, different flesh)
1. Title <= 60 chars, pattern varies, must contain the city and one service and the brand (e.g. "Window Tint & Car Audio for Torrance Drivers | Audio MotorSports").
2. Meta description 120-160 chars, unique, includes city + Carson + a service + the phone.
3. H1 with city + lead service.
4. Answer-first paragraph (45-70 words): what the shop does for people from this city, that the shop is in Carson at 22025 S Avalon Blvd, the distance, and the lead service. Written to be quotable by an AI engine on its own.
5. "What <city> drivers bring us" section: 3-5 services with 1-2 specific sentences each (specific about the service, not about the city unless from data).
6. Route/drive block: miles from the data file, approximate time, hours, a sentence on drop-off and waiting [SHOP NOTE slot allowed here].
7. 5 question headings (H3) in natural question form, each with a 40-60 word direct answer. At least 2 questions must be city-specific in wording ("Is it worth driving from Lancaster for window tint?"), the rest service-specific. Questions must differ in wording from every other page in the batch.
8. Prices block: only the allowed prices, "as of October 2026", and a line that other work is quoted at the shop.
9. Nearby cities: 3-5 links to other hub city pages (/<slug>/) that are geographically plausible neighbors by the miles column (closest by distance difference), varied per page.
10. CTA: call, text, address, hours.
11. JSON-LD: one @graph with WebPage (name, url, dateModified "2026-10-08", about -> {"@id":"https://www.audiomotorsports.com/#business"}), BreadcrumbList (Home > Locations > City), and FAQPage whose questions AND answers are byte-identical to the visible Q&A text. Do not emit a new business node; reference the existing @id only.

## File format for each draft (<slug>.md)
---
url: https://www.audiomotorsports.com/<slug>/
city: <City>
miles: <n>
lead_service: <...>
title: <...>
meta: <...>
---
# <H1>
<body in markdown; H2/H3 as described; question headings as "### Q?">
```json
<JSON-LD>
```
[CONFIRM] list at the end (anything the shop must verify; should be only SHOP NOTE slots and drive times).

## Self-check before you finish (required, run it)
python3 ~/ams-seo-audit-2026-10-03/city_rewrite/qa_check.py <your drafts folder>  must report 0 FAIL for: title length, meta length, FAQ parity (schema == visible), forbidden phrases, price whitelist, "Avalon" used as a city, sentence reuse > 0 across the batch, word count below 400, missing keywords (city + Carson + at least 4 service keywords), missing neighbor links. Fix and rerun until clean. Report the final QA summary.

## Owner update (received mid-run, applies to every page, including ones already written)
Zack's own words, which you may paraphrase freely on every page (no [CONFIRM] needed):
- The shop is near the beach in Carson, and people already drive from much farther than any of these cities. Customers have come from Temecula and San Diego (about 120 miles) and have called from as far as San Jose. Use this to make the drive feel normal and worth it; every one of the 158 cities is closer than that. Do NOT state "Temecula/San Diego/San Jose" as recurring facts on every page; vary: some pages mention one of them, some say "customers come from over 100 miles away", some say nothing about it.
- How it works, stated plainly on every page in different words: schedule an appointment, then either drop the car off or wait at the shop while the work is done. Call (310) 513-8800 or text (213) 429-1092 to book.
- The goal of each page is for the shop's SERVICES to rank for that city: window tint, car audio and stereo installation, car alarms and remote start, GPS tracking, dash cameras, Tesla window tint, Harley bagger audio, CarPlay/Android Auto. Lead with services, support with the drive-in model.
Tone: proud, direct, no hedging about distance. Never open with what the shop is not.
If you already wrote pages before this update, revise them to match before your final QA run.

## Owner's goal (apply to tone on every page)
Zack: "People are willing to drive for good work for a good deal. People want to work with trusted people. I was well known before AI rewrote the internet; I want the same people to find me again." So: every page shows trust (real review counts with an as-of date, dated/attributed review slots), fair dated prices, and plain answers. No hype. The reviews line you may use: "Google 4.8 (650+ reviews) and Yelp 4.7 (770+ reviews), as of October 2026."

## Brand-site batches (mounted copies on the hub)
For /tint/, /beats/, /alarm/, /tesla/, /amspods/ city pages: the brand's own service leads every page (tint -> window tint/ceramic; beats -> car audio, subwoofers, CarPlay; alarm -> alarms, remote start, GPS; tesla -> Tesla window tint by model, no model prices; amspods -> Harley bagger audio, AMS pods from $649 a pair). Brand name in title (LA Car Tint, LA Car Beats, LA Car Alarm, Tesla Tint LA, AMS Pods) with "by Audio MotorSports, Carson". Mention the other services once as a cross-sell line, not more. Neighbor links point to the same brand's city slugs. Label the draft header `source: hub-mounted copy; standalone www host not verified`. File path: city_rewrite/<brand>/drafts/<slug>.md.

## Owner update 2: it is about the SERVICE, not the product (applies to every page, revise already-written ones)
Zack: "If it's something they could order online, why would they drive to me? They only drive to get the service done." So every page sells installation and labor done right, not parts. The product is the excuse; the installation is the reason to drive.
Service wording to use exactly (these are the search terms; each page should use the ones that fit its lead service plus 3-5 others, in headings or question headings, naturally):
- car window tint / window tinting / ceramic window tint
- car alarm installation / Viper alarm installation / Compustar installation
- remote start installation
- car stereo installation / head unit installation
- Apple CarPlay and Android Auto installation
- speaker replacement / speaker installation
- subwoofer installation / subwoofer upgrade
- amplifier installation
- dash camera installation
- GPS tracker installation
- Harley-Davidson motorcycle audio / bagger audio installation / AMS pods
- Tesla window tint
Each service mention should say what the install involves or protects against in one plain sentence (wiring done clean, factory look, no rattles, no drilled dash, film hand-cut on the glass, alarm wired so it cannot be bypassed from the fuse box, etc.) without inventing specs or brand claims.
Theme line you may paraphrase (never verbatim twice): bringing it to a shop that does this every day beats a cheap install that has to be redone. Do NOT insult customers or competitors; do not write "amateurs" or "destroyed". Say it as: "done once, done right", "we fix a lot of installs that were done wrong elsewhere" [this one is a claim: allowed only inside a [SHOP NOTE] slot for Nick to confirm].

## Repair pass (morning of 2026-10-08)
You are finishing an interrupted run, not starting over. Your work order JSON lists: `fix_files` (existing drafts with the QA failure text), `write_missing` (slugs with no draft yet), and `reuse_lines_involving_your_files` (sentences/questions duplicated across pages; rewrite YOUR copy of each so it differs in wording, keep the meaning). Do not rewrite pages that are not in your work order. For meta/title length fails, tighten the wording; do not drop the city, Carson, service or phone. For "no JSON-LD block", add the @graph (WebPage + BreadcrumbList + FAQPage, answers byte-identical to the visible Q&A). For beats "neighbor links", add 3-5 links in the form /beats/car-stereo-<slug>/ to nearby cities from the beats batch files. The QA reuse check now ignores the hours line, the price line, the phone and address, so those may match across pages; everything else must not.

## Brand specifics for alarm / tesla / amspods (read with "Brand-site batches" above)
- alarm (LA Car Alarm, /alarm/): lead with car alarm installation, Viper alarm installation, Compustar installation, remote start installation, GPS tracker installation, dash camera installation. Prices allowed: Viper 3108V $269 installed, Compustar 9910 from $499, "as of October 2026". Neighbor links /alarm/car-alarm-<slug>/.
- tesla (Tesla Tint LA, /tesla/): lead with Tesla window tint by model (Model 3, Model Y, S, X, Cybertruck only if the live page mentions it), ceramic film, one-piece rear glass, cameras and sensors left clear, no signal interference. NO Tesla model prices anywhere (they conflict on the live site): say "quoted by model at the shop". The general tint prices (Solar $249 / Solar Ceramic $329) may appear once as the non-Tesla reference. Neighbor links /tesla/tesla-tint-<slug>/. The street is Avalon Blvd; never use "Avalon" as a city.
- amspods (AMS Pods, /amspods/): lead with Harley-Davidson bagger audio installation, AMS lower-fairing speaker pods for Street Glide, Road Glide, Road King (name other models only if the live page does), amplifier installation and tuning on the bike. Price allowed: AMS pods from $649 a pair, "as of October 2026". Neighbor links /amspods/bagger-audio-<slug>/. Say "riders" where it fits.
- The QA link check now accepts the full brand path, so no hub cross-link is needed to pass; add one only if it helps the reader.
- "lobby": write "wait at the shop" rather than "lobby" (the shop has not confirmed a lobby).

## Owner update 3 (2026-10-07 evening; applies to EVERY page, written or not; overrides anything above that conflicts)
1. Reviews line is exactly: "Google 4.8 (654 reviews) and Yelp 4.7 (777 reviews), as of October 2026". Never "650+" or "770+".
2. Phone for Call AND Text is (213) 429-1092 (tel:+12134291092 / sms:+12134291092). Never (310) 513-8800 anywhere, including JSON-LD.
3. Product orders (when a page mentions buying gear): offer in-store pickup, or call for delivery; everything is paid upfront before delivery. Service booking stays: book by call or text, drop the car off, or wait inside.
4. Financing wording: "Payment plan" or "Buy now, pay later" only. Never 100-day, Snap, Koalafi or EasyPay.
5. Car audio focus. No DJ products.
6. NO roof tint. The shop does not film the glass roof. Pages may say the factory roof glass is already dark and that the side and rear glass are what get filmed. Never a lead angle, heading, FAQ or sentence that offers or describes tinting the roof.
7. No "48 states" or national shipping claims.
8. City pages cover car stereo, window tint and car alarm work (and the related brands: tint, beats, alarm, tesla, amspods). Never glass repair, wraps or PPF.
9. Carson IS allowed as the shop's city on every city page (owner decision, Oct 7). Avalon stays a street name only.
10. "Wait inside" wording is the owner's: the shop has seating, a TV with Netflix, free Wi-Fi, a restroom and a water fountain. A mall, movie theaters, restaurants, coffee shops and a Starbucks are within walking distance. A DoubleTree hotel with a full bar is down the street; Cabrillo Beach is about 12 minutes away. Vary these naturally; never the same sentence twice.
11. The shop is LGBTQ-friendly and everyone is welcome (it says so on Google and Yelp). Say it on every city page in a short, varied line; say it clearly on the Long Beach pages.
12. Who comes in (use on the matching cities only, plain and respectful, no partnership, discount or endorsement claims): Carson, San Pedro and Wilmington are home to ILWU longshore workers and the Union Pacific rail yard; workers from the three active local refineries; Metro bus operators; SpaceX employees and engineers (Hawthorne); engineers and staff from big corporations (Torrance, El Segundo).
13. Location: right off the 110 freeway, easy access from the 405 and the 710 (three freeways lead to it).
14. The script `apply_owner_corrections.py` inserts one marked paragraph (`<!-- owner-details-2026-10-07 -->`) with items 10, 11, 13 (and 12 where it applies) before the questions section of every existing draft. New drafts: write these lines yourself, in your own words, and do NOT add the marker.
15. Carson gets a dedicated article (not a template page): see `carson_article/` when written.
