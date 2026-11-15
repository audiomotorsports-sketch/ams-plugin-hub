# AI Search (GEO) Report: lacarstereo.com

Date: 2026-10-04. Evidence: robots.txt, llms.txt probe, and the HTML of all 127 sitemap URLs fetched with curl. No live AI-engine queries were run (no access), so "would be cited" statements are inference, labelled (unverified).

## Summary
AI visibility today is effectively zero by configuration: robots.txt disallows every AI crawler, the pages are marked noindex, and there is no llms.txt. The underlying content has some strong citation raw material (installed prices, FAQ answers, NAP) but it is short and not exposed.

Score (heuristic): Crawler access 0/100, llms.txt 0/100, Passage citability 55/100, Entity clarity 50/100, Structured data 45/100, Brand/third-party signals unverified.

## 1. AI crawler access (robots.txt)
Full file fetched from https://lacarstereo.com/robots.txt:
```
User-Agent: AdsBot-Google          Allow: /
User-Agent: AdsBot-Google-Mobile   Allow: /
User-Agent: Googlebot              Allow: /locations/
User-Agent: *                      Disallow: /
Sitemap: https://www.lacarstereo.com/sitemap.xml
```

| Crawler | Group applied | Result |
|---|---|---|
| GPTBot, OAI-SearchBot, ChatGPT-User | `*` | Blocked |
| ClaudeBot, Claude-SearchBot, Claude-User | `*` | Blocked |
| PerplexityBot, Perplexity-User | `*` | Blocked |
| Google-Extended (Gemini training/grounding control token) | `*` | Blocked |
| Applebot-Extended, CCBot, Bytespider, etc. | `*` | Blocked |
| Bingbot (feeds Copilot and several AI products) | `*` | Blocked |
| Googlebot (AI Overviews source) | own group: Allow /locations/ only | Not disallowed anywhere, but every page except 3 is noindex |

Comparison: audiomotorsports.com publishes a documented single `User-agent: *` group welcoming answer engines and an llms.txt; teslatintla.com has explicit Allow groups for GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot and others. lacarstereo.com is the outlier.

Fix: open robots.txt to `*` (and keep the single-group pattern the hub site documents), allow the AI search bots (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Googlebot, Bingbot). Training bots (GPTBot, ClaudeBot, Google-Extended, CCBot) are a business choice; blocking only those is compatible with being cited by search-style bots. Remove the page-level noindex too, or the bots can fetch but not use the pages.

## 2. llms.txt
https://lacarstereo.com/llms.txt and /llms-full.txt both return 404 (the site's HTML 404 page). The hub (audiomotorsports.com/llms.txt) and teslatintla.com have working files, so a template exists to copy, including rules like "do not invent APR or monthly amounts". llms.txt is a low-weight, unproven signal; it is useful here mainly as a single place to state the facts below.
Next step: publish /llms.txt with business facts (name, legal name, address, phone, SMS line, hours, one-bay Carson shop, service area, installed-price policy, labor from $149, payment providers without terms), links to /shop/*, /install/*, /packages/, /faq/, /locations/.

## 3. Passage citability
Strong passages (short, self-contained, answer-first), all on noindex pages today:
- /faq/: 8 Q&As, for example "Will I keep my steering wheel controls and backup camera? Yes. A stereo install keeps the factory functions that already work..." and "Can you add CarPlay without replacing my screen? Yes. Wireless CarPlay adapters add CarPlay and Android Auto on the factory screen...". Each answer is 20 to 45 words, a good citation size.
- /install/carplay/: "What's included" list (head unit, dash kit and harness, steering wheel interface, antenna adapter, camera reconnected, microphone) and "Labor from $149, most cars same day".
- Homepage and package pages: concrete installed prices ("2009-2014 Ford F-150 from $629.94 installed, plus sales tax").
- Package pages (for example /packages/2009-2014-ford-f-150/, noindex): itemised price build-up (stereo $459 + parts $29.99 + install $300) and "about 2 hours in the bay". This is the most citable commercial content on the site.

Weak:
- Product pages (101) are about 245 words of mostly boilerplate; nothing quotable beyond price.
- /about/ and /gallery/ are thin; no dated content, no authors, no statistics with sources.
- Homepage intro "Wireless CarPlay, installed today." is marketing copy, not an answer.
- The homepage explicitly withholds review text, so there is nothing for an AI to quote about customer experience.
- /locations/ is a list of city names with miles, with no explanatory passages.

Next steps: add answer-first intro paragraphs of 40 to 80 words to each install page ("How much does CarPlay installation cost in Carson? ..."), 3 to 5 FAQs per install page, a visible "Last updated" date on pricing, and per-product 100 to 200 words.

## 4. Entity clarity
- Names used: "LA Car Stereo" (brand), "Audio MotorSports Inc" (legal name, in footer and schema), "Audio MotorSports" (hub), "AMS". The relationship is stated ("An Audio MotorSports Inc shop") and mirrored in schema via parentOrganization and sameAs. Good.
- Consistent NAP and hours with the hub, Tesla Tint and shop sites (verified on 3 of 7 sister domains).
- Weak: schema sameAs has no third-party profiles on the main entity (no GBP, Yelp, Facebook, social); the hub site shows Yelp 4.7 from 777 and Google 4.8 from 654, but lacarstereo.com shows only Google and does not link a Yelp page. No Wikipedia, Wikidata or press mentions were checked (unverified). A named person ("Ask for Nick") appears only on /locations/.
- Seven sibling domains share one phone, address and review count. For AI engines this can read as one entity with several brand sites, which is accurate, but each site should state clearly which service it owns to avoid answers mixing them up. shop.audiomotorsports.com also sells the same car audio under "Shop car stereo in Carson".

## 5. Brand and third-party signals (unverified)
Not measurable from here: Reddit, YouTube, Yelp, forum and directory mentions, Google Business Profile completeness, AI engine answers for "car stereo installation Carson". Recommended manual test once crawlable: ask ChatGPT, Perplexity, Gemini and Google AI Mode "best car stereo install in Carson / Long Beach / Torrance" and "how much does CarPlay install cost in LA" and record which sources appear.

## 6. Technical rendering for AI crawlers
The pages are server-rendered Next.js (full text is present in the raw HTML; I parsed all content without running JavaScript). This is good for crawlers that do not execute JS. No Markdown alternates, no ai-catalog, no /.well-known files were found (404s tested for /.well-known/security.txt only; others unverified).

## Priority actions (GEO)
1. Rewrite robots.txt and drop noindex so AI search bots can fetch pages. quick
2. Publish /llms.txt using the hub file as template. quick
3. Add answer-first intro, FAQ block and Offer schema to the 7 install pages. medium
4. Add third-party profile links (GBP, Yelp, Facebook) to schema sameAs and visible footer. quick
5. Publish a named-people About section, a few attributed reviews with links, and gallery captions. medium
6. Expand product pages with unique copy and Product schema. project
