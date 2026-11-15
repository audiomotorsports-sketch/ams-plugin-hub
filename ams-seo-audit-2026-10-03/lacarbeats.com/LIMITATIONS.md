# LIMITATIONS: lacarbeats.com audit (2026-10-04)

Replaces the earlier STATUS.md (same file, renamed and rewritten). Read-only audit. Nothing was changed on any site or repo.

## Verified on the standalone domain [standalone-verified]
Re-tested at the start of this run (2026-10-04 04:24 UTC):
- `https://lacarbeats.com/` connects: TLS 1.3, certificate CN=lacarbeats.com, issuer Let's Encrypt (YR2), expires 2026-11-08, hostname matches. Served by Vercel (`server: Vercel`, `x-vercel-id: iad1::...`).
- Response is **HTTP/2 308** to `https://www.lacarbeats.com/`, with `location` and `refresh: 0;url=...` headers, `cache-control: public, max-age=0, must-revalidate`. One hop at the apex; the chain beyond it could not be followed.
- `strict-transport-security: max-age=63072000` (2 years). No `includeSubDomains` or `preload` directive on the apex response.
- `/robots.txt`, `/sitemap.xml` and `/llms.txt` on the apex each return the same 308 to the www equivalent. Their content was **not** readable.
- `https://www.lacarbeats.com/` and `https://shop.lacarbeats.com/` are refused by the egress proxy (CONNECT 403). Not bypassed, per rules.

## NOT verified on the standalone domain
Everything about the content and markup of www.lacarbeats.com: titles, H1s, meta, canonicals, robots meta, `X-Robots-Tag`, JSON-LD and `@id`s, sameAs, FAQ, sitemap contents, robots.txt rules (including any AI-crawler rules), llms.txt, internal links, hreflang, page speed, whether pages are indexed. Also whether the www host is Vercel-served.

## Evidence used instead [mount-proxy]
The hub-mounted copy at `https://www.audiomotorsports.com/beats/`: all 196 `/beats/` URLs in the hub sitemap were fetched (196 of 196 returned 200; 109 city pages, 15 Spanish pages, 3 blog posts, 26 service pages, 27 shop pages). Structural fields were extracted for all 196 (pages.csv); about 25 pages were read in full. Every finding based on this is tagged **[mount-proxy]**: it describes the hub copy and is a proxy for the standalone domain. The two may differ (canonicals, `@id`s, root-relative links, robots.txt, llms.txt, sitemap).

Evidence that the mount is NOT identical to the standalone domain:
- Mount JSON-LD uses `@id` `https://www.audiomotorsports.com/beats/#business`, not `https://www.lacarbeats.com/#business`. No page on the mount references `lacarbeats.com` in JSON-LD; the only lacarbeats hostname in the mount is `shop.lacarbeats.com` (62 links in the HTML). So the "JSON-LD pointing to lacarbeats.com/#business" could not be confirmed anywhere.
- Mount canonicals point to audiomotorsports.com/beats/..., so they say nothing about the standalone canonicals.

## Not measured at all (any site)
Core Web Vitals / PageSpeed, Search Console, index status, rankings, Google Business Profile, backlinks, real citations in ChatGPT/Perplexity/Gemini/AI Overviews. Any score or estimate is inferred from HTML only.

## Other caveats
- AI-crawler tests were run against the hub mount with spoofed User-Agent strings (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, ClaudeBot, Claude-SearchBot, GPTBot all 200, identical size). That tells you about the hub's WAF, not lacarbeats.com's.
- Word counts in pages.csv include navigation/footer text (about 2,500+ words per page of which a large share is shared chrome), so they overstate body copy.
- The hub robots.txt, llms.txt and sitemap were read from audiomotorsports.com, not from lacarbeats.com.
