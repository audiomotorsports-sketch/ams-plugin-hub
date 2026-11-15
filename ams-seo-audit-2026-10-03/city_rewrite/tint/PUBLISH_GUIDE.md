# LA Car Tint (/tint/) city pages: how to publish (Zack + Tom)

Drafts: `city_rewrite/tint/drafts/<slug>.md` (109). Index: `tint/REVIEW_INDEX.csv` (words, lead service, SHOP NOTE slots, CONFIRM items per page). QA: `python3 city_rewrite/qa_check.py city_rewrite/tint/drafts` must print FAIL=0 and reused_sentences=0 before any batch goes up.

## Before the first page
1. Run the snapshot tool once: `python3 hub_deep_dive/harness/hub_snapshot.py` (keep the file as BEFORE).
2. Save a copy of the current city-page template and of each page you replace.
3. Decide the two shop facts the drafts cite everywhere: "Google 4.8 (654 reviews) and Yelp 4.7 (777 reviews), as of October 2026" and the price lines. If either is wrong, fix it in the drafts first (one search-and-replace across the folder).

## Each draft file
- Frontmatter: url, title (<=60), meta (120-160), H1 in the body.
- Body: answer paragraph, services section, route block, 5 question headings, prices, nearby links, CTA.
- `[SHOP NOTE: ...]` = a slot for 2-3 sentences from Nick about that city (customers, routes, a job). Fill it or delete the bracket before publishing; never publish the bracket text.
- The JSON-LD block goes in the page head (or wherever the template puts schema). Its FAQ answers must stay byte-identical to the visible answers; if you edit a visible answer, edit the schema too.
- The existing business node on the page stays; the draft only references it by @id.

## Order
These are the hub's mounted copies (audiomotorsports.com/tint/...). Publish the hub root pages first. Then, before touching these, open the same city page on the standalone brand domain (www.lacartint.com) and check whether it shares the hub template; if it does, one change covers both, if not, apply the draft on each. Closest cities first, 20 a day, snapshot before and after, same as the hub.

## Do not
- Publish all 158 in one day. 20 a day for a week is the safe pace.
- Change titles or FAQ text by hand without re-running qa_check.
- Mix brand pages into the hub batches; finish the hub first.
