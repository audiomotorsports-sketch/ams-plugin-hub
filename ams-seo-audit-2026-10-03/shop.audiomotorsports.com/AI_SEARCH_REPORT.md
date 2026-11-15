# AI Search (GEO) Report: shop.audiomotorsports.com

Audited 2026-10-04. Read-only. Evidence: fetched robots.txt, llms.txt, homepage, collection and product pages, hub site files. No live AI-engine queries were run, so actual citation/visibility is UNVERIFIED. Scores are my estimates.

## Summary

Crawler access and machine-readable context are strong. The weaknesses are entity and URL fragmentation (the same business and catalog appear under several host/brand names) and thin, templated product text, which gives AI systems little unique passage material.

Estimated GEO readiness: 70/100.

## 1. AI crawler access (Pass)

shop robots.txt (fetched, 121 bytes):
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /planner/
Sitemap: https://shop.audiomotorsports.com/shop-sitemap.xml
```
- No named blocks for GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, or Bingbot, so all fall under `*` and are allowed everywhere except `/admin/` and `/planner/`.
- Live check with those user agents (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) against `/shop/` returned HTTP 200 for each. No WAF block observed. (Only four were tested.)
- The hub robots.txt carries a comment explaining the deliberate single-group design.
- Google-Extended and similar are not blocking training; if you want to opt out of training but stay in AI search, that is a policy decision, not a defect.

## 2. llms.txt (Present, with caveats)

`https://shop.audiomotorsports.com/llms.txt` returns 200 `text/plain` (4,560 bytes). It is the hub's file, not shop-specific: the title is "Audio MotorSports ... The hub site for the Audio MotorSports network" and its links all go to `www.audiomotorsports.com`, with no link to the shop catalog (`/shop/`) beyond one "Shop" bullet. Good content: NAP, hours, service list, prices, "what the shop does not do", sister-brand mapping, key pages.

Caveats:
- The shop copy differs from the hub's copy on one line: the shop says "Never say financing or 0%", the hub says "Say payment plan. Do not quote APR, 0%, or a monthly amount." Two versions of the same file are drifting.
- The file contains instructions addressed to AI ("Do not mention warranty", "Never say financing", "Does not stock or recommend Rockford Fosgate"). Models generally treat site text as data, and such directives can read as manipulation; they may be ignored or, worse, make the answer look censored. Prefer factual statements ("Audio MotorSports does not stock Rockford Fosgate") over commands, and consider the legal implication of instructing models not to mention warranty.
- No `llms-full.txt` (404) and no `/.well-known/ai-catalog.json` (404). Both optional.
- Dated claim "Prices verified September 2026" is useful; keep it updated.

## 3. Entity clarity

Positive: consistent NAP everywhere (22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; Mon-Sat 9:30-6). `AutoRepair` JSON-LD with `@id` `https://www.audiomotorsports.com/#business`, `sameAs` list (Instagram, YouTube, Facebook, TikTok, Yelp, Google Maps), alternate names. Product text states "in-store pickup only, we don't ship".

Problems:
- **Host/brand fragmentation.** The same catalog exists as (a) `shop.audiomotorsports.com/shop/...` (canonical for the shop), (b) `www.audiomotorsports.com/stereo/shop/...` titled "LA Car Stereo", (c) `/beats/shop/...` titled "LA Car Beats", (d) `/alarm/shop/...` "LA Car Alarm" (4 pages fetched; all self-canonical). The sister sites lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com and teslatintla.com were not reachable, so their relationship is unverified, but the hub links to them from the shop homepage and llms.txt describes them as "same Avalon bay, not second shops". An AI engine can easily treat these as separate businesses, or cite the wrong brand name and domain for a product.
- Entity pointers in structured data use the www host while pages live on the shop host (see SCHEMA_REPORT.md S1/S5).
- The shop homepage is the hub homepage with a www canonical, so the shop host never describes itself ("who runs this shop") on a page of its own.

## 4. Passage citability

Sampled pages:
- Product pages: a short templated paragraph ("The Viper 3108V is a 1-way car alarm. It has 1320 ft of range. ... We stock it in Carson for pickup and we fit it here -- call ...") plus a spec table (Brand, Model, range, etc.). The first sentence is a clean, self-contained, citable definition. The rest is boilerplate repeated across products, which dilutes uniqueness. No comparison, fitment list, or how-to content per product. Specs lists are short.
- Useful quotable blocks: "Pick it up in Carson ... We don't ship", "About 90% on the shelf -- call before you drive", payment-plan note (Snap, Koalafi, EasyPay, Synchrony) and a "Before you drive over / Will it fit my car?" FAQ block on product pages.
- Collections: each has a short intro and the card grid. Prices appear in the text, so they are extractable where published.
- Homepage FAQ (15 Q&As) has the strongest citable passages, though the answers are long and opinionated.

Citability estimate: 60/100 for product pages, 75/100 for the FAQ/homepage.

## 5. Brand and off-site signals

`sameAs` links exist. The shop page links to a Google Maps listing, Instagram, YouTube (4 videos plus channel) and Google share link. Off-site presence (Reddit, Wikipedia, review volume, directory listings) was NOT assessed (no external access).

## 6. Technical access for AI

- Content is server-rendered; no JS needed to read products, prices or specs.
- Page weight is small; TTFB 0.15-0.45 s.
- No rate limiting or bot block seen.
- `Content-Signal` directive (for AI use preferences) is not used.
- Product feed or protocol signals for agentic commerce (ACP/UCP endpoints, `/.well-known/` files) not found (the one path tried returned 404). Not verified beyond that.

## Recommendations
1. Resolve the duplicate-catalog ambiguity: decide which host/brand is canonical per product and cross-reference the others (canonical or noindex), so AI engines see one entity (AUDIT_REPORT.md #3).
2. Fix schema URLs and link `seller` to the business `@id` (SCHEMA_REPORT.md).
3. Give the shop its own llms.txt focused on the catalog (categories, brands, the in-store-pickup policy, how to check stock), link `/shop/`, and sync the two versions. Rewrite imperative lines as facts.
4. Add unique content to top products: fitment (vehicles), what is included, who it suits, install notes.
5. Optionally publish `llms-full.txt` with the catalog summary.
