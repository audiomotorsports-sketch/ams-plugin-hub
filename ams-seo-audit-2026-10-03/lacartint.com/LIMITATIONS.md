# LIMITATIONS: what was and was not verified for lacartint.com

Audit date: 2026-10-04 (UTC). Read-only. Nothing was modified, committed or deployed. Only files in this folder were written.

## The core limit

`https://www.lacartint.com/` is refused by the egress proxy (CONNECT 403). It was retested once at the start of the run and again at the end (curl exit 56, then HTTP code 000). It was not bypassed. Every content page of the standalone domain lives on www, so **no page of the standalone domain was fetched or audited.**

Every on-page, schema, FAQ, link and content finding in these reports comes from the **hub-mounted copy at https://www.audiomotorsports.com/tint/**. It is labelled "hub-mounted copy, proxy for the standalone domain, standalone not verified" throughout. The hub mount may differ from the standalone (canonicals, `@id`, links, sitemap, robots, llms.txt, templates, freshness).

## VERIFIED on the standalone domain (apex only)

| Check | Result |
|---|---|
| `https://lacartint.com/` | HTTP/2 308 to `https://www.lacartint.com/`, `server: Vercel`, `cache-control: public, max-age=0, must-revalidate`, `refresh: 0;url=...` header present |
| `http://lacartint.com/` | HTTP/1.1 308 to `https://lacartint.com/` (then the 308 above), so a 2-hop chain http apex, https apex, https www |
| Path preservation | `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/tint/`, `/window-tint-torrance/` each 308 to the same path on www |
| User-agent independence | Googlebot and GPTBot user agents get the same 308 as the default agent (no UA-based blocking at the apex) |
| HSTS | `strict-transport-security: max-age=63072000` (2 years). No `includeSubDomains` and no `preload` on the apex response |
| TLS | Let's Encrypt (CN YR1) certificate for `CN=lacartint.com`, valid 2026-08-10 to 2026-11-08 (about 35 days left; Vercel normally auto-renews, renewal not verified). SAN list and the www certificate were not checked |
| robots.txt, sitemap.xml, llms.txt content | **Not obtainable.** The apex answers each with a 308 body of "Redirecting..." |

## NOT VERIFIED (standalone)

- The final status, content, title, H1, meta, canonical, hreflang and robots meta of any www.lacartint.com page.
- www `robots.txt` (and so Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot access), `sitemap.xml`, `llms.txt`, `ai.txt`.
- The schema `@id` actually used on the standalone (`https://www.lacartint.com/#business` is only inferred, from the hub's own JSON-LD, which references it).
- The standalone URL structure. The mount uses `/tint/window-tint-{city}/`; the standalone is probably `/window-tint-{city}/` (apex 308 preserved that path but the target was not fetched).
- Whether the www host redirects to apex or the reverse (www is the target of the apex 308, so www is the canonical host, but this is the only evidence).
- Core Web Vitals (PageSpeed was not run for the standalone; the hub copy was not measured either, so all performance statements are static-signal only).
- Search Console, GBP, rankings, backlinks, index coverage. No access to any of them.
- How many of the hub's ~370 pages that link to lacartint.com were fetched: only a sample of 11 hub pages was grepped (see AUDIT_REPORT.md section 8). The 370 figure is the hub audit's, not re-measured here.

## What WAS fetched (all through the proxy, all HTTP 200)

- Hub-mounted copy: **all 141** `/tint/` URLs in the hub sitemap (109 city pages, 6 Spanish pages, 5 service pages, 4 blog pages, 1 home, 1 Tesla page, 15 utility pages). That is more than the ~40 requested. Raw data: `pages.csv`.
- Hub: `/robots.txt`, `/sitemap.xml` (1,090 URLs, 141 under /tint/), `/llms.txt`, and 11 other hub pages for link and `@id` checks. `/tint/robots.txt`, `/tint/sitemap.xml` and `/tint/llms.txt` return 404 (expected for a mount, not evidence about the standalone).
- Comparison site: teslatintla.com home, `/tesla-tint-carson/`, `/tesla-tint-torrance/`, `/tesla-tint-long-beach/`, `/locations/`, `/blog/` (all 200 first try or after a retry). The earlier 143-URL audit of teslatintla.com in the sibling folder was reused for site-wide numbers.

## Method notes and tool limits

- Parsing used Python (requests, BeautifulSoup, json) plus the claude-seo `parse_html.py` script. The Rich Results Test and the schema.org validator are not reachable, so "valid" means well-formed JSON-LD with sensible types, not confirmed Google eligibility.
- "Unique local words" on city pages is a sentence-level estimate: sentences of 6+ words, city name masked, counted as unique if they appear on 3 or fewer of the 109 city pages. It is a heuristic.
- "Visible FAQ" parity: a schema question counts as visible if its exact text appears in the rendered text (not inside `<script>`).
- The previous hub audit (`../FIX_LIST.md` item 36) recommended canonicalizing or noindexing the mounts. That recommendation is **not** carried into this audit, under the owner's rule that no page is removed, merged or noindexed. Duplication between mount and standalone is recorded as an open question only.
