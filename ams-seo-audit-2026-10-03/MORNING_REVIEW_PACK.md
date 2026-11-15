# AMS morning review pack (for Zack + Tom)

> **CORRECTION 2026-10-07: lacarstereo.com is already LIVE (confirmed by the team).** Earlier text that says "pre-launch", "if launching" or "intent unknown" is superseded. Re-checked the same day: robots.txt still blocks all crawlers except Google's ad bots and `/locations/`, and the home, FAQ, /book/ and most pages are still `noindex, nofollow` (sitemap rebuilt 2026-10-04, so the site is being deployed). A live site in this state is invisible to Google and AI Overviews, and its `/book/` form sends nothing, so booking requests are being lost now. Since noindex is not approved, treat both as live defects to review first.

Date: 2026-10-07. **Nothing in this file has been applied.** No site, repo or account was changed. Rules in force: every page and site stays live; fixes only improve pages; no delete, trim, merge or noindex; nothing goes live without Zack and Tom reviewing it together first.

Companion files in this folder: `FIX_LIST.md` (48 SEO/AIO items), `LAUNCH_AUDIT.md` (launch blockers), `AI_VISIBILITY_QUERY_SET.md` (queries to track).

---
## 1. Decision on the five Vibha guides (SEO + GEO Autopilot, Backlink Engine, Backlinks From Zero, Content Engine, AI Search Tracker)

**Verdict: yes, in phases, and only the safe parts.** None of the guides asks to delete a page.

| Phase | What | Needs |
|---|---|---|
| 1 | Fix the broken things (this pack, section 2) | Zack + Tom review |
| 2 | Use the claude-seo skills already installed (they are the "skills" all five guides run on) | nothing new |
| 3 | Search Console, read-only | Zack's Google login; check the connector's GitHub address first |
| 4 | AI-visibility baseline (~$2 per sweep) | review of `search.html` source first; dedicated DataForSEO account, small balance, auto top-up off |
| Hold | GitHub Pages hosting of the board, DNS changes, Windsor.ai/Composio, the unnamed "humanizer" skill, startup-directory backlink list, Reddit/directory outreach without disclosure, scheduled weekly jobs, mass AI-written pages, the paid session | not now |

Limits: only the pasted text was read. Link addresses, `search.html`, the tracker page and DataForSEO pricing were not seen. Nothing here guarantees rankings or AI citations.

---
## 2. Draft changes, ready for review (NOT applied)

Where a file location is unknown, the draft says "find"; I did not have access to the sites' code. After each change, re-run the check named in the last column.

| # | Change | Exact draft | Gate / caution | Verify with |
|---|---|---|---|---|
| D1 | Aftercare footer link (LAUNCH M4) | Find the shared hub footer/nav that outputs `/aftercare/` and change it to `/tint/aftercare/`. | None. | `curl -sI https://www.audiomotorsports.com/tint/aftercare/` returns 200; footer no longer links `/aftercare/`. |
| D2 | Dev comments in public source (FIX B1) | Remove the HTML comments containing "INSERT after" / "quote plugin" and "TODO Zack" from the shared hero partial. | None (not visible today). | View-source on `/tint/` and `/beats/`. |
| D3 | "Closed today" banner (FIX B2) | Add `data-nosnippet` to the banner element: `<div class="..." data-nosnippet>`. Reserve its height so the header does not jump on Sundays. | Banner class name unknown; find it in the shared script. | Force-clock Sunday; header does not shift. |
| D4 | teslatintla Carson page (LAUNCH M6, FIX B4) | Title: `Tesla Window Tint Carson, CA \| Tesla Tint LA`. H1: `Tesla Window Tint in Carson, CA`. Replace the city-name "Avalon" in breadcrumb, description and FAQ with "Carson". | **Do not find-and-replace "Avalon" blindly.** The street address is "22025 S Avalon Blvd", and "Avalon" there is correct and must stay. Change only city-name uses. Add a link to this page from home, footer and /locations/. | Re-count: address still reads "Avalon Blvd"; "Carson" appears in title/H1/breadcrumb. |
| D5 | Hub home title/H1 (FIX B5) | Title: `Car Audio, Window Tint & Alarms in Carson, CA \| Audio MotorSports`. H1 saying what and where. Add a 2-3 sentence intro using facts already on the site. | Intro wording needs shop confirmation. | Title under 60 chars; H1 present. |
| D6 | Brand home titles (FIX B6) | lacarbeats: `Car Subwoofer Install in Carson, CA \| LA Car Beats`. lacartint: `Window Tint Carson CA \| 3M Ceramic, Hand-Cut \| LA Car Tint`. Others: service + Carson, under 60 chars, H1 to match. | Confirm brand names to use (see FIX D5). | Titles under 60 chars. |
| D7 | City-page schema (FIX B15/B16) | On city pages, point to the main business node instead of declaring a second one: `"provider": { "@id": "https://teslatintla.com/#business" }`. Same pattern for the other brands. Keep the verified facts: Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745, (310) 513-8800, Mon-Sat 9:30-18:00. | Pick one business type per entity (decision). `sameAs` URLs must come from the shop; none are invented here. | Run a JSON-LD validator on 3 pages. |
| D8 | lacarstereo robots.txt (LAUNCH G1) | `User-agent: *` / `Allow: /` / `Disallow: /cart/` / `Sitemap: <final canonical host>/sitemap.xml` | **The site is live, so this is a live defect.** Replacing robots.txt without removing the page-level noindex does nothing; both are one decision. Training-bot rules (GPTBot, ClaudeBot) are a separate business choice. | `curl https://lacarstereo.com/robots.txt`; a test URL returns indexable. |
| D9 | lacarstereo `/book/` form (LAUNCH M1) | Make the form POST name, phone, vehicle and requested time to `/api/quote/`, as the package quote form already does, keeping the honeypot. | Needs the page's code. Send one real test lead after the fix. | Test lead arrives; success message only after a 200 response. |
| D10 | Sitemaps (FIX B12) | Remove only URLs that 308-redirect and `/cart/` pages. Add real per-page `lastmod`. Add missing real pages. | Never remove a city or location page. | Count of redirecting URLs = 0. |
| D11 | Price consistency (FIX B8) | One price source per service; align meta, FAQ, schema, llms.txt; add "last verified {date}". | Needs the shop's confirmed prices. No drafts, because none are verified. | Same price in all four places. |
| D12 | llms.txt rewrites (FIX B13) | Clean public-facing drafts already exist in `teslatintla.com/AIO_REPORT.md` and `lacarstereo.com/AIO_REPORT.md`. Remove file paths and "do not mention" directives. | Facts marked [CONFIRM] must be verified. Google Search does not use llms.txt. | File has no internal paths or directives. |

---
## 3. Safe-apply routine (every change, every time)
1. Zack and Tom approve the specific item together.
2. Save a copy of the current page/template text first, so it can be reverted.
3. Make one change at a time, on a preview or staging copy where one exists.
4. Re-run the named check, then `probe.py` (phone + desktop) on the page.
5. Only then publish. Keep a dated note of what changed.
6. Never touch `noindex`, robots or sitemaps without the two-person approval above, and never remove a page.

## 4. Running the audit on your own network (if that is what "help my network" meant)
This removes the limits of the cloud sandbox: the four brand `www` hosts load, speed numbers are trustworthy, and PageSpeed works with your own key.
1. Install the claude-seo plugin: `/plugin marketplace add AgriciDaniel/claude-seo`, then `/plugin install claude-seo@agricidaniel-claude-seo`, then `/seo setup`.
2. Run `/seo audit <url>` and `/seo geo <url>` for each of the 8 sites.
3. For screenshots and link checks: copy `_phase2/probe.py` to your machine, install Playwright (`pip install playwright` then `playwright install chromium`), remove the sandbox-specific browser path and proxy arguments, and run `python3 probe.py out_folder URL1 URL2`. It inspects forms and never submits them.
4. Compare your results with `FIX_LIST.md` and `LAUNCH_AUDIT.md` to confirm each finding, especially everything tagged [mount-proxy].
5. Keep API keys on your machine only. Do not paste them into chat or a hosted web page.
