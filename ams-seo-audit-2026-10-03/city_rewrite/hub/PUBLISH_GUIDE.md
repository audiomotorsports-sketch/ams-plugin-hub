# Hub city pages: how to publish (Zack + Tom)

Drafts: `city_rewrite/hub/drafts/<slug>.md` (158 when complete). Index: `hub/REVIEW_INDEX.csv` (words, lead service, SHOP NOTE slots, CONFIRM items per page). QA: `python3 city_rewrite/qa_check.py city_rewrite/hub/drafts` must print FAIL=0 and reused_sentences=0 before any batch goes up.

## Before the first page
1. Run the snapshot tool once: `python3 hub_deep_dive/harness/hub_snapshot.py` (keep the file as BEFORE).
2. Save a copy of the current city-page template and of each page you replace.
3. Decide the two shop facts the drafts cite everywhere: "Google 4.8 (650+ reviews) and Yelp 4.7 (770+ reviews), as of October 2026" and the price lines. If either is wrong, fix it in the drafts first (one search-and-replace across the folder).

## Each draft file
- Frontmatter: url, title (<=60), meta (120-160), H1 in the body.
- Body: answer paragraph, services section, route block, 5 question headings, prices, nearby links, CTA.
- `[SHOP NOTE: ...]` = a slot for 2-3 sentences from Nick about that city (customers, routes, a job). Fill it or delete the bracket before publishing; never publish the bracket text.
- The JSON-LD block goes in the page head (or wherever the template puts schema). Its FAQ answers must stay byte-identical to the visible answers; if you edit a visible answer, edit the schema too.
- The existing business node on the page stays; the draft only references it by @id.

## Order (closest to the shop first, 20 pages per batch)
Batch 1: west-carson, harbor-city, wilmington, lomita, torrance, gardena, compton, long-beach, signal-hill, alondra-park, rolling-hills-estates, willowbrook, lawndale, san-pedro, redondo-beach, rolling-hills, paramount, watts, hawthorne, lakewood
Then continue down `REVIEW_INDEX.csv` sorted by miles.
After each batch: run the snapshot tool, then `hub_diff.py BEFORE AFTER`. PASS = next batch. FAIL = restore the saved copies and tell me what it reported.

## Do not
- Publish all 158 in one day. 20 a day for a week is the safe pace.
- Change titles or FAQ text by hand without re-running qa_check.
- Touch any brand mount (/tint/, /beats/ ...) in this pass; those have their own drafts.
