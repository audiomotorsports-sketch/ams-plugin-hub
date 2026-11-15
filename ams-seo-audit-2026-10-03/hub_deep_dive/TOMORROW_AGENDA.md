# Tomorrow's agenda for Zack and Tom (audiomotorsports.com first)

Prepared 2026-10-07. **Nothing has been applied.** No site, repo or account was changed; the hub plugin repo is clean. Every page and site stays live; fixes only improve pages; nothing goes live without you both agreeing.

## Read in this order (about 45 minutes)
1. This agenda.
2. `../HUB_FIRST_PLAN.md` (the 16 hub fixes and the pilot design; see "Updates from the deep dive" at its end).
3. `LOCAL_CITATION_AUDIT.md` sections for hours, Yelp, Facebook (the customer-facing risks).
4. `DRAFT_CONTENT_HUB.md` (copy-ready page drafts; skim the [CONFIRM] checklist at the end).
5. `CITY_TEMPLATE_PILOT.md` sections 3-5 (spec, five pilot drafts, control design).
6. `REPO_MAP.md` section 0 and section 5 (what this repo is and is not; the install doc's risks).
7. `SERP_COMPETITOR_REPORT.md` (thin evidence; read the limits first).
8. `harness/README.md` (how to prove a change broke nothing).

## Part A: decisions only you can make (15 minutes)
1. **Sunday hours.** The site says Sunday closed. Apple Maps and some directories reportedly show Sunday open (about 10:00 to 4:00). Which is right? If closed, fix the listings first, because customers may arrive on a closed day.
2. **Founding year and legal name.** The hub says "since 2003" and "20+ years"; BBB reportedly shows 2015; some listings say "25+ years". Pick one claim you can prove.
3. **Official Yelp and Facebook pages.** Two Yelp listings (782 and 774 reviews, one without the "s") and two Facebook pages exist for the shop. Which are official?
4. **One business name** on every listing and in schema (the singular "Audio MotorSport" is widespread on third-party listings).
5. **Dealer and certification claims.** "3M Authorized Dealer", Viper Diamond, Compustar authorized: do you hold them and have proof? Don't ask dealer locators to list the shop until this is settled.
6. **Prices.** One price source per service. Confirm: Solar $249, Solar Ceramic $329, Viper 3108V $269, Compustar 9910 from $499, AMS pods from $649, Dual Kicker Comp box $249, and how the Tesla promo ($149/$299/$199) differs from the "Matrix" ($189/$369/$399). "$149 for two fronts" means different things on `/tint/`, `/specials/` and `/tesla/`.
7. **Walk-in or appointment**, warranty wording (the live 30-day workmanship answer vs "do not mention warranty"), payment-plan wording ("No 0%" vs "100 days same as cash"), whether the shop does LED lighting and door locks (pages exist but `/faq/` says no), and whether Softail is covered (46 live pages list it; the plugin says no).
8. **Indexing intent** for lacarstereo.com (live, blocked from search), the shop products (~282 noindexed) and the amspods city pages (85 noindexed).
9. **Which geo coordinates are real** (two sets on the site) and the 40,000 vs 100-mile service radius.
10. **Is `/carson/` meant to be a real page** instead of redirecting to `/locations/`? (Adding a page is additive; changing the redirect is a decision.)

## Part B: before any change (30 minutes)
1. Zack verifies the hub in Search Console and exports Performance, Pages (indexing) and Core Web Vitals as CSV. Check "Crawled - not indexed" for city pages and `/stereo/shop/`.
2. On your own network, run the harness: `python3 harness/hub_snapshot.py` (about 2-6 minutes) and keep that file as the "before". A baseline from 2026-10-07 01:20 already exists in `harness/` (1,194 URLs).
3. Check your own Google Business Profile: name, address, phone, hours (especially Sunday), categories, review count and date.
4. Save a copy of every template or page before editing it.

## Part C: first changes, safe and small (one at a time, snapshot and diff after each)
1. **Listings first (no website change):** correct Sunday hours, name and phone on Google, Apple Business Connect, Bing Places, Yelp (pick the official page), Facebook, BBB (free profile), Manta/YellowPages. See the action list in `LOCAL_CITATION_AUDIT.md`.
2. **Tesla Carson page:** replace the 46 city-name uses of "Avalon" with Carson using the before/after table in `DRAFT_CONTENT_HUB.md` page 4. Leave the 12 address uses ("Avalon Blvd") untouched.
3. **Leaked wording:** rewrite "We do not invent..." (14 pages, including `/faq/`, `/tesla/` and eight `/tesla/blog/*` pages, and inside FAQ schema) as plain customer wording.
4. **FAQ text that matches its schema**, starting with `/faq/` (15 of 18 schema answers are not on the page and 8 visible answers are cut off mid-sentence). The harness found 97 pages and 369 questions in total; start with the draft pages, then the Tesla group.
5. **Home page** title, H1, answer paragraph and schema from the draft. Apply the home change before the page-level `WebPage` nodes, because they reference the home graph's `#website`.
6. **Hreflang for `/` only** (its twins already have correct tags).
7. **Developer comments** on `/tint/`, `/beats/`, `/alarm/`, `/amspods/` and their `/es/` twins, and the "TODO" comments (`/tint/services/hand-cut/`, 62 on `/es/` pages).
8. **Closed banner:** add `data-nosnippet` and reserve space (note the sticky-bar conflict in `REPO_MAP.md` section 3).
Later: the sitemap clean-up (33 redirecting shop URLs; add the 104 new pages after a title/FAQ review), the city-template pilot on 5 cities, service-page upgrades, review dates, Person nodes, headers.

## Part D: things not to do
- Don't run the plugin install doc as written (running it twice duplicates the plugin and the `id="quote"` form; it says to paste the whole file, which leaks a header comment; it targets branch `v1`; it contains removal wording that conflicts with your rule; its raw URL is public).
- Don't find-and-replace "Avalon" (the street name must stay; the flagged 413 pages need eyes, not a script).
- Don't change a shared template without a saved copy, a test on one page, and a snapshot diff (the hub serves about 775 mounted pages from shared templates).
- Don't delete, trim, merge, redirect away or noindex anything.
- Don't enter API keys in unreviewed pages; no scheduled jobs yet.

## After each change
Run the harness again, `python3 harness/hub_diff.py before.json after.json`. PASS is fine, REVIEW means look, FAIL means restore the saved copy. Also check by eye on a phone.
