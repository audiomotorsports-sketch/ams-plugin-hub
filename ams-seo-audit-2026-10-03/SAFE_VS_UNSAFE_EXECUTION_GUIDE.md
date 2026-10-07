# AMS execution guide: what to do, what is safe, what is not

> **CORRECTION 2026-10-07: lacarstereo.com is already LIVE (confirmed by the team).** Earlier text that says "pre-launch", "if launching" or "intent unknown" is superseded. Re-checked the same day: robots.txt still blocks all crawlers except Google's ad bots and `/locations/`, and the home, FAQ, /book/ and most pages are still `noindex, nofollow` (sitemap rebuilt 2026-10-04, so the site is being deployed). A live site in this state is invisible to Google and AI Overviews, and its `/book/` form sends nothing, so booking requests are being lost now. Since noindex is not approved, treat both as live defects to review first.

Prepared 2026-10-07 for Zack and Tom to execute together. **Nothing here has been applied.** No site, repo or account was touched. No page is recommended for deletion, trimming, merging, redirecting away or noindexing; every page and site stays live and fixes only improve pages.

Read with: `FIX_LIST.md` (48 SEO/AIO items), `LAUNCH_AUDIT.md` (launch blockers), `MORNING_REVIEW_PACK.md` (12 draft changes), `AI_VISIBILITY_QUERY_SET.md`.

---
## 1. What the research established

**Google's own position (verified from Google Search Central, "AI features and your website"):** to appear as a supporting link in AI Overviews or AI Mode, a page must be **indexed and eligible to appear in Search with a snippet**. Google states site owners do not need special files, special schema or AI-specific optimization; the foundation is allowing crawling, making important content indexable, useful text, and structured data that matches visible content. Consequences for AMS:
- The pages that matter most are the ones not indexed today (lacarstereo.com, ~282 shop products, 85 amspods city pages). That is the biggest AI-Overview blocker, bigger than any file or schema.
- llms.txt does not help Google Search. It may matter to other AI tools, but it is optional and low priority.
- `Google-Extended` in robots.txt does not control AI Overviews.

**Google's spam rules (verified via search summaries):** mass AI-generated pages that add no value count as *scaled content abuse*, and paid links, link exchanges and low-quality links count as link spam. So: improve the existing pages, add only a few genuinely useful new ones, and never buy or swap links.

**Caveat on this research:** Google's pages were read through search summaries, not every page in full. Re-read the primary page before acting on any policy detail: https://developers.google.com/search/docs/appearance/ai-features

---
## 2. Tool vetting (what is safe to install or connect)

| Tool | Result | Verdict |
|---|---|---|
| **claude-seo skills** (seo-audit, seo-geo, seo-content, seo-backlinks, seo-technical...) | Already installed. MIT license. Backlink scripts read: they only contact moz.com, bing.com, data.commoncrawl.org; API keys stored locally with owner-only permissions; no obfuscated code. Not a full audit of the whole repo. | **Safe to use** |
| **DataForSEO official MCP** (`dataforseo/mcp-server-typescript`) | Open source (LICENSE present), last commit 2026-10-02. No install-time scripts except a build step. Only contacts `*.dataforseo.com`. Uses your DataForSEO login/password via environment variables. DataForSEO also offers an official hosted endpoint, which means sending your key to their servers. Code read by grep, not run. | **Safe with conditions** (below) |
| **Google Search Console MCP: "mcp-gsc" is not one program.** At least four unrelated repositories use similar names: `pijusz/mcp-gsc`, `ahonn/mcp-server-gsc`, `AppsYogi-com/gsc-mcp-server`, `mikusnuz/gsc-mcp`. The guides name none of them. | The first three were cloned and scanned (no install-time scripts, only Google hosts, no hidden-code patterns): <br>• **ahonn:** read-only scope (`webmasters.readonly`), service-account login. Has a sitemap-submit tool that a read-only scope should block. <br>• **AppsYogi:** has both read-only and full modes, stores tokens in the OS keychain. <br>• **pijusz:** asks for **full** Search Console access plus the Indexing API; has tools to delete sites and sitemaps, **disabled by default** (`GOOGLE_GSC_ENABLE_WRITES`); contacts api.github.com (appears to be an update check). <br>mikusnuz was not scanned. | Prefer **read-only** access only. The safest option is no connector: export CSVs from Search Console (see section 4). |
| **`search.html` tracker** (AI Search Tracker guide) | **Not reviewed.** The page and file were never available to me (host blocked). The guide asks you to type the DataForSEO login and password into it. | **Not safe until reviewed** |
| **"humanizer" skill** | Source not named in the guide. Not reviewed. | **Not safe until reviewed** |
| **Windsor.ai, Composio** (Search Console via third party) | Not reviewed. Your Google data would pass through their servers. | **Hold** |
| **Moz, Bing Webmaster, Common Crawl** | Used by the claude-seo backlink skill (checked above). Moz and Bing keys are issued to you. | Safe, low priority |

DataForSEO pricing, as reported in search results (not independently confirmed): LLM Responses start at about $0.0006 per task plus the AI provider's token and web-search charges, pay-as-you-go. The guide's ~$1.50 for 12 prompts across 4 engines is consistent with that. Verify on dataforseo.com/pricing before topping up.

---
## 3. Do now: safe, no accounts, no new tools (Zack + Tom review each first)
Order matters: fix what is broken before measuring anything. Details and exact wording are in `MORNING_REVIEW_PACK.md` section 2 and `FIX_LIST.md`.

0. **lacarstereo.com is live but blocked from search** (noindex on 124 of 127 pages plus a robots.txt block, re-checked 2026-10-07). Highest-impact decision in this guide; it also explains why the site cannot appear in AI Overviews.
1. **Broken or lead-losing items:** lacarstereo `/book/` sends nothing (live, so requests are lost now); 52 shop product-card links 404 after JavaScript runs; shop catalog API returns 500; "Aftercare" footer link 404 on tint pages; broken simulator assets on the tint copy.
2. **Wrong or leaked content:** the teslatintla Carson page says "Avalon" (change only city-name uses, never the "Avalon Blvd" address); internal instruction text visible on alarm and amspods city pages and in some llms.txt files; "TBD, Zack" notes on lacarstereo.
3. **Phone layout on teslatintla.com:** clipped price bar and chat panel, overlapping sticky bars, 404 page without styles.
4. **Facts that conflict:** one price source per service across meta, FAQ, schema, llms.txt (prices must be confirmed by the shop).
5. **Titles and answers:** Carson-targeted titles, answer-first intros, FAQ text that matches its schema.
6. **Schema hygiene:** one business entity per brand, city pages referencing it, hours and phone consistent.
7. **Sitemaps:** remove only redirecting non-page URLs; add real `lastmod`; never remove a location page.
8. **Add, don't remove:** add Carson answers where missing; add unique local content to the existing city pages (the biggest long-term project).

---
## 4. Do with conditions (decision or approval first)

| Item | Condition |
|---|---|
| **Indexing decisions** (lacarstereo, shop products, amspods city pages) | Zack and Tom decide together whether these are meant to rank. If yes, the template-level tag change happens in stages, re-checked each time. Nobody adds a new noindex. |
| **Search Console** | Zack's login. Prefer CSV exports (Performance, Pages, Queries, Indexing) so no connector is needed. If a connector is used: read-only scope only, the author and repo address checked, and access removed afterwards under Google Account permissions. |
| **AI-visibility baseline** | Query list is ready. Needs a dedicated DataForSEO account with a small balance and auto top-up off, and a review of `search.html` source first (or use the official DataForSEO MCP / seo-dataforseo skill instead). A baseline before fixes, the same list after. |
| **llms.txt** | Optional. Publish only factual public text with confirmed details; no internal paths or "do not mention" directives. |
| **Weekly or daily scheduled tasks** | Only after connectors are vetted, and only drafts or reports. Nothing scheduled may hold a connector that can change a site. |
| **Backlinks** | Local and supplier sources only, with real information, disclosed identity, and human-sent. Sister-site links between our own domains do not count as outside votes. |
| **Content drafting with AI** | A few useful pages at most, from one confirmed fact sheet; human review for every claim; keep the original text before any rewrite. |

---
## 5. Not safe: do not do
- **Typing API keys or passwords into a hosted web page** you have not read, or into any chat.
- **Publishing the tracker/board on GitHub Pages**, or any DNS change, until reviewed (a public page can expose data or keys; a forgotten DNS entry can be hijacked).
- **Granting full or write access** to Search Console or the Indexing API to an unvetted tool.
- **Any step that deletes, trims, merges, redirects away or noindexes pages or sites.**
- **Mass-generated AI pages**, link purchases or swaps, fake reviews, undisclosed Reddit/directory promotion.
- **Auto-sending outreach**, auto-publishing content, or unattended jobs that hold deploy tools (Vercel, GitHub).
- **Blind find-and-replace** of "Avalon" on the Tesla page.
- **Booking the paid working session or installing the "humanizer" skill** without source review.

---
## 6. Measuring honestly
- Take a **baseline now**: Search Console exports, `AI_VISIBILITY_QUERY_SET.md` results for each engine, and the `probe.py` speed/layout run from a normal network (the cloud sandbox gave noisy numbers).
- Change **one group at a time** and record dates. Re-measure after 2 to 4 weeks. AI engines re-crawl slowly.
- Treat third-party scores (DA, "AI visibility %") as indicators, not results. Real outcomes are calls, texts, bookings and indexed pages.

## 7. Rollback and review routine
1. Zack and Tom approve the specific item together.
2. Save a copy of the current text/template first.
3. One change at a time, on a preview where one exists.
4. Verify with the check named in `MORNING_REVIEW_PACK.md`; re-run `probe.py` on the page.
5. Publish; write a dated note. If anything looks wrong, restore the saved copy.

## 8. Limits of all of this
I read the guides' pasted text only. I could not open the authors' page, link addresses, `search.html`, or the humanizer source. Repositories were scanned by searching their code, not by running or fully auditing them. The four brand `www` hosts were audited through the hub's mounted copies. Search Console, GBP, field speed data and live AI-engine results were not available. No guide or tool can promise rankings or citations.

### Sources
- Google Search Central, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Scaled content abuse and link spam summaries: https://ppc.land/scaled-content-abuse/ and https://www.practicalecommerce.com/google-spam-policies-explained
- DataForSEO official MCP: https://github.com/dataforseo/mcp-server-typescript and https://dataforseo.com/help-center/setting-up-the-official-dataforseo-mcp-server-simple-guide
- DataForSEO AI Optimization API: https://dataforseo.com/apis/ai-optimization-api
- Search Console MCP candidates: https://github.com/pijusz/mcp-gsc, https://github.com/ahonn/mcp-server-gsc, https://github.com/AppsYogi-com/gsc-mcp-server
