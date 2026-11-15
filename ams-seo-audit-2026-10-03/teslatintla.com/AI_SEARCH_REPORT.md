# AI Search (GEO) Report: teslatintla.com

Date: 2026-10-04. Evidence from live fetches. No citation/mention testing was run in ChatGPT/Perplexity/Gemini (no access), so **actual AI visibility is UNVERIFIED**.

## 1. AI crawler access (robots.txt, fetched 200, 379 bytes)

| Crawler | Rule | Result |
|---|---|---|
| GPTBot | Allow: / | Allowed |
| OAI-SearchBot | Allow: / | Allowed |
| ChatGPT-User | Allow: / | Allowed |
| ClaudeBot | Allow: / | Allowed |
| Claude-User | Allow: / | Allowed |
| PerplexityBot | Allow: / | Allowed |
| Google-Extended | Allow: / | Allowed |
| Applebot-Extended | Allow: / | Allowed |
| Bingbot | Allow: / | Allowed |
| CCBot, Bytespider, Meta-ExternalAgent, Amazonbot | not listed | Allowed by `User-agent: *` |

No Disallow lines, no Cloudflare/WAF challenge observed (Vercel edge served all 143 pages to a generic UA). **UNVERIFIED:** whether Vercel firewall bot rules treat GPTBot differently from my UA; no way to test as those agents.

All content is server-rendered static HTML (47 KB homepage, text visible without JS), so non-JS AI fetchers see the full copy. The price simulator is JS-driven but the price matrix is also in text and in llms.txt.

## 2. llms.txt (https://teslatintla.com/llms.txt, 200, text/plain, 2,910 bytes)

Exists and is well-structured (shop facts, price matrix, blog, gallery, locations, "How to answer"). Problems:
- **Leaks internal notes**: "Canonical matrix is teslatintla/assets/sim/prices.js", "owner-locked $599", "GET /api/blog reads teslatintla/data/blog.json. No write API.", "Do not invent other prices", "Never say financing, credit, finance, or 0%", "Do not mention warranty", "Do not offer DSP, wraps, or PPF". These read as internal agent instructions and expose repo paths. Remove paths and rewrite the compliance directives as neutral public statements (or drop them).
- **Count inconsistencies**: llms.txt says "111 Tesla city pages"; sitemap has 124 `/tesla-tint-*/` URLs; /locations/ title says "121 drive-ins". Pick one number or remove it.
- `/llms-full.txt` timed out on one request through the proxy and was not retried (UNVERIFIED whether it exists). llms.txt does not link to /about/, /contact/, /book/ or /payment-plan/.
- No Spanish pointer even though /es/ exists.
- The file claims "Prices verified September 2026"; good freshness signal, but no per-page dates on prices.

## 3. Passage citability (sampled homepage, model posts, city pages)

Strong:
- Direct, quotable facts with numbers: "Model Y doors-and-back install is usually two to three hours", "Front side windows stay at 70% VLT under California law", "Solar Ceramic doors plus back glass is $349 installed", "Appointments are 10:00 AM or 12:00 PM only. Monday through Saturday, 9:30 AM to 6:00 PM. Sunday closed."
- Q/A structure: 132 pages have FAQ blocks with 4 to 11 answers; answers are self-contained (50 to 80 words, include the entity and the price).
- Clear differentiators: "Tesla glass only", hand-cut on glass board, ceramic does not affect GPS/phone signal (an answerable question).

Weak:
- City pages repeat the same price matrix in a 100+ word FAQ answer that reads like a data dump; answer engines may choose any of 124 near-identical passages, none clearly authoritative. Make the homepage (or one /pricing/ page) the canonical source and link to it.
- Opening passages are narrative ("We are not in Brea. ... Zack runs the floor.") rather than a 1 to 2 sentence definition AI can lift.
- No comparison tables in HTML with `<table>` for price matrix (prices are in cards/JS), so tabular extraction is harder. Check: matrix present as text in FAQ only (verified); a real HTML table was not found on the homepage text.
- Blog posts (1,177 to 1,782 words) lack author byline/person, update date in visible text (schema has datePublished only) and external citations (3M, Llumar, CARB/CVC 26708 for VLT). No outbound sources were present in the sampled posts.

## 4. Entity clarity and brand signals

- One entity expressed three ways: "Audio MotorSports", "Tesla Tint LA", "Tesla Tint Los Angeles". Public contact name "Nick" appears everywhere with no surname, so AI cannot disambiguate the person.
- Cross-site consistency is high (same NAP/phone/hours on 143 pages; sister sites reference teslatintla.com in sameAs), which helps knowledge-graph reconciliation. But the same GBP/map link serves six domains.
- sameAs includes Yelp, Google Maps ftid, Instagram, YouTube, Facebook, TikTok. **Missing:** Wikipedia/Wikidata (unverified whether any exists), BBB, Tesla-owner forums/Reddit mentions, Apple Maps/Bing Places. Off-site mentions and review corpora (Reddit, Tesla Motors Club) drive a lot of AI citations; none checked (UNVERIFIED).
- Review data is self-hosted quotes (Yelp, up to 2019). AI engines weight third-party review platforms; ensure Yelp and Google profiles carry the same Tesla-specific language.

## 5. Agent readiness

- /llms.txt present; no /ai.txt (request timed out through the proxy, UNVERIFIED), no /.well-known/security.txt (404), no sitemap index (404, not required).
- A chat widget (`ams-chat.js`) loads site-wide; whether it exposes anything to agents was not tested.
- Sitemap has no /es/ URLs, so the Spanish content (an extra answer-engine audience) is not discoverable via sitemap.

## 6. Quick wins for AI citation

1. Clean llms.txt (remove internal paths/directives; fix counts; add About/Contact/Book/Payment links).
2. Add a single "Tesla window tint prices (Oct 2026)" HTML table to the homepage or /pricing/, dated, and have city pages link to it instead of repeating the 100+ word matrix.
3. Add visible byline + "Updated {date}" on blog posts, with a Person author and sources (3M/Llumar spec sheets, California Vehicle Code 26708).
4. Add Service/Offer schema (see SCHEMA_REPORT.md).
5. Put a 40 to 60 word definition ("Tesla Tint LA is the Tesla window-tint bay of Audio MotorSports in Carson, CA...") as the first paragraph of the homepage and /about/.
6. Add sitemap entries for /es/ pages.
7. Build off-site mentions: Reddit r/TeslaModelY, Tesla Motors Club, YouTube descriptions linking the homepage (YouTube gallery is already a strength: 9 jobs on the Audio MotorSports channel).
