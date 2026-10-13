# AMS Pods city pages: how to publish (Zack + Tom)

Drafts: `city_rewrite/amspods/drafts/<slug>.md` (60 pages). Index: `amspods/REVIEW_INDEX.csv`. Gate: `python3 -I city_rewrite/qa_check.py amspods/drafts` (currently FAIL=0, reused_sentences=0).

## What these are
Rewrites of the live mounted pages at `/amspods/bagger-audio-<slug>/` on the hub. Each draft's frontmatter says `source: hub-mounted copy; standalone www host not verified`. The standalone site (amspods.com) is blocked from the audit sandbox: check from your own network whether it uses the same template or a separate copy before copying a change there.

## Before the first page
1. Run the hub snapshot: `python3 hub_deep_dive/harness/hub_snapshot.py` and keep it as BEFORE.
2. Save the current page or template for every page you replace.
3. Confirm the shared facts every draft cites: reviews "Google 4.8 (654 reviews) and Yelp 4.7 (777 reviews), as of October 2026"; call and text (213) 429-1092; the price lines; no roof tint; the amenity, welcome and freeway lines.

## Each draft
- Frontmatter url, title (<=60), meta (120-160). Body: answer intro, services, route block, five question headings, prices, neighbor links, CTA, JSON-LD.
- `[SHOP NOTE: ...]` slots are for 2-3 sentences from Nick about that city. Fill or delete before publishing; never publish the bracket. Drive times are approximate (25-30 mph): confirm or remove.
- Keep JSON-LD FAQ answers byte-identical to the visible text; re-run the gate after any edit.

## Order and pace
Closest to the shop first (sort `REVIEW_INDEX.csv` by miles), about 20 pages a day. After each batch: snapshot, then `hub_diff.py BEFORE AFTER`. PASS = next batch; FAIL = restore the saved copies.

## Do not
Publish everything in one day; hand-edit FAQ text without re-running the gate; touch pages outside this brand in the same pass; delete, merge or noindex any page.

## Brand notes
Street Glide, Road Glide and Road King only. Price: AMS pods from $649 a pair, as of October 2026. Earlier hub-style amspods drafts are in `amspods/_hub_style_strays/` (kept, not used).
