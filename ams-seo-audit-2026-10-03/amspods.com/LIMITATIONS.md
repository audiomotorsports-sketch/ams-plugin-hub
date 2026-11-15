# amspods.com audit limitations (2026-10-04)

## What was blocked
- `https://www.amspods.com/` (re-tested once at start): the egress proxy returns `CONNECT tunnel failed, response 403`. Not bypassed.
- `https://shop.amspods.com/` (linked from the mounted home page): same, `curl` exit 000 / CONNECT refused. Not bypassed.
- Consequence: no page of the standalone domain was fetched. Titles, H1s, canonicals, schema, internal links, rendering, Core Web Vitals, robots.txt, sitemap and llms.txt of the standalone site are **not verified**.

## Evidence that IS standalone-verified (apex only, 2026-10-04 04:24 UTC)
- `https://amspods.com/` -> HTTP/2 308, `location: https://www.amspods.com/`, `server: Vercel`, `strict-transport-security: max-age=63072000` (2 years; no includeSubDomains/preload token seen), `cache-control: public, max-age=0, must-revalidate`, `refresh: 0;url=...` header present. TLS handshake to apex succeeded.
- `/robots.txt`, `/sitemap.xml`, `/llms.txt` on the apex each 308 to the same path on `www`. So their content is unknown; only the redirect is verified. The redirect is a single hop for each path, path-preserving, permanent (good).
- Not checked: whether `www` then redirects, serves 200, or has its own HSTS/TLS config.

## Evidence used as a proxy (everything else)
- Hub-mounted copy: `https://www.audiomotorsports.com/amspods/` and 129 sub-URLs (all `<loc>` entries containing `/amspods` in the hub `sitemap.xml`; 130 pages, 130 returned HTTP 200 after one retry for a transient connection reset).
- Every finding drawn from it is tagged `[mount-proxy]`. The hub copy may differ from the standalone domain (different canonical, different templates, different sitemap). In particular **the mounted pages all declare `rel=canonical` to `www.audiomotorsports.com/amspods/...`, not to amspods.com**, so the mount is not evidence of what the standalone domain declares.
- Also used: hub `robots.txt`, hub `llms.txt`, and a link scan of the 960 non-amspods hub URLs (some fetches failed with transient SSL resets; counts are lower bounds).

## Discrepancy with the brief
- The hub said ~44 pages link to amspods.com. The scan found **849 hub pages linking to `https://www.amspods.com/`** (footer/network link, root only) and 3 linking to `/build-your-own/` (some fetches failed, so counts are lower bounds). Deep standalone URLs get almost no hub links.

## Not done / out of scope
- No Google Search Console, PageSpeed, CrUX or analytics data (not provided); no live SERP or AI-answer checks; no JavaScript rendering (raw HTML only).
- Product/inventory facts (fitment years, prices, shipping) are as stated on the mounted pages; none were independently verified. Passages proposed in AI_SEARCH_REPORT.md must be confirmed by the shop before publishing.
- Read-only: nothing was changed, committed or deployed.
