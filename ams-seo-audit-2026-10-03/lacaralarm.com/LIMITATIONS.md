# lacaralarm.com: LIMITATIONS (replaces STATUS.md)

Audit date 2026-10-04 (UTC). Read-only; nothing was changed anywhere.

## What could not be done
- https://www.lacaralarm.com/ is refused by the egress proxy (CONNECT 403). Retested once at the start of this run: still 403. Not bypassed, per RULES.md.
- The apex https://lacaralarm.com/ answers, but every path (/, /robots.txt, /sitemap.xml, /llms.txt) returns 308 to the same path on www. So the standalone site's HTML, robots.txt, sitemap, llms.txt, schema, canonicals, titles and Core Web Vitals were NOT fetched or verified.
- shop.lacaralarm.com (linked ~17 times from the hub copy) was not fetched either; not tested, assumed same restriction.
- No Search Console, GBP, PageSpeed/CrUX or analytics access. Nothing here is a ranking or traffic claim.

## Evidence that IS standalone-verified (apex headers only, fetched 2026-10-04 04:24 UTC)
- https://lacaralarm.com/ : HTTP/2 308, `location: https://www.lacaralarm.com/`, `server: Vercel`, `strict-transport-security: max-age=63072000` (no includeSubDomains or preload token seen), `cache-control: public, max-age=0, must-revalidate`, `refresh: 0;url=https://www.lacaralarm.com/`.
- http://lacaralarm.com/ : 308 to https://lacaralarm.com/ (then a second 308 to www). Two hops before content.
- /robots.txt, /sitemap.xml, /llms.txt on apex: each 308 to the www equivalent. Contents unknown.
- TLS: TLSv1.3, cert CN=lacaralarm.com, Let's Encrypt (YR2), valid Aug 10 2026 to Nov 8 2026 (auto-renewal assumed on Vercel, not verified).

## Proxy evidence used instead (labelled everywhere "hub-mounted copy, proxy for the standalone domain, standalone not verified")
- https://www.audiomotorsports.com/alarm/ and 56 URLs under it (home, 3 blog posts, 9 service pages, 26 city pages, es home, shop and info pages). 56 returned 200; /alarm/car-alarm-carson/ returned 404.
- The hub sitemap lists 204 URLs under /alarm/ (145 city pages and 59 others: es, services, shop, blog, info). The hub's "~340 pages link to lacaralarm.com" figure was not independently counted; the 204 here is the mount's own count.
- The hub's robots.txt, sitemap.xml and llms.txt describe audiomotorsports.com, not lacaralarm.com. /alarm/robots.txt, /alarm/llms.txt, /alarm/sitemap.xml are 404 on the hub.
- Limits of the proxy: the mounted copy may differ from the standalone build (hosts, canonicals, og:url, schema @id, robots, headers). Its canonicals and schema URLs all point at audiomotorsports.com/alarm/..., which is exactly what cannot be assumed for lacaralarm.com.

## To close the gap
Allow www.lacaralarm.com (and shop.lacaralarm.com) in the environment's allowed domains, then re-run: robots.txt, sitemap.xml, llms.txt, canonical/og/schema host, header check, crawl.
