# AI Search (GEO) Report: audiomotorsports.com

Date 2026-10-04. Evidence from live fetches. Not run: actual queries in ChatGPT/Perplexity/Gemini (no access), so brand presence and citation rates are **[unverified]**.

## AI crawler access (verified)
robots.txt has one group (`User-agent: *`, `Allow: /`, `Disallow: /admin/`, `/planner/`) and so allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Google-Extended, Applebot-Extended, Bingbot (none blocked). The file comment explains why named groups were removed (they would not inherit the Disallow lines). Live UA test: requests with UA strings GPTBot, ClaudeBot, PerplexityBot, Google-Extended and the full GPTBot/ClaudeBot strings returned HTTP 200 (one full-ClaudeBot attempt had a transient TLS reset, a retry returned 200), so there is no WAF block. Pages are server-rendered HTML (title, H1, JSON-LD, body text present in the raw response), good for crawlers that do not run JS.

## llms.txt (verified, 4.6 KB)
Present with: business facts (address, phones, hours), service area, "how to answer" guidance, published prices, what the shop does not do, key links, and the network of 6 sites. Very strong for entity clarity. Issues:
- It tells AI not to mention warranty, not to quote APR/monthly amounts, and not to recommend Rockford Fosgate. Instructions to models inside llms.txt are non-standard and some engines may ignore or distrust them; also withholding warranty info can cost trust. Judgement call for the owner.
- It lists prices "verified September 2026"; keep the date current, and keep it consistent with the FAQ page (which says "no public prices").
- It references `data/drive-in-cities.json`, which is not a public URL (not checked; **[unverified]**).
- No `llms-full.txt` (404). Optional.

## Entity clarity
Strong: consistent name "Audio MotorSports Inc", address, phones, hours; `AutoRepair` node with `@id`, sameAs to Google Maps, Yelp, YouTube, social, and the five sister domains; founders/staff named (Zack, Nick). Weaknesses:
- Six brand names for one shop (LA Car Tint, LA Car Beats, LA Car Stereo, LA Car Alarm, AMS Pods, Tesla Tint LA) and duplicate `@id`s across hub mounts and standalone domains may split or confuse entity resolution. lacarstereo.com is not listed in llms.txt or any hub link, while `/stereo/` mounts "LA Car Stereo".
- Homepage has the least entity data (see SCHEMA_REPORT item 1) and a title that does not say what the business does.

## Passage citability
Strengths: direct-answer FAQs ("Are you in Long Beach? No. ...", drive distances in miles and minutes, prices with what is included), 1,500-2,000-word service and city pages, question-format headings, explicit "what we do not do" statements.
Weaknesses:
- Very long FAQ answers repeating the address and promotional lines (the Long Beach "How do I drive" answer repeats the same pin sentence twice); passages over about 150 words are less likely to be quoted.
- Boilerplate text repeated across 60+ city pages reduces the uniqueness a model sees per URL.
- Homepage has about 256 words, nothing quotable beyond the meta description.
- Thin pages (177 under 300 words) offer little to cite; blog has 4 posts at 235-548 words.
- Many pages identical across mounts (32 hash groups), so an engine may cite the wrong host.
- Reviews page (306 words) lists Google 4.8/654 and Yelp 4.7/777, which is good third-party-backed content, but ratings are not tied to dated review excerpts on the same URL.

## Brand and third-party signals
Linked profiles: Google Maps, Yelp, YouTube (119 pages link), Facebook, Instagram, TikTok, OfferUp. Presence on Reddit, Wikipedia/Wikidata, press, or forum mentions is **[unverified]** (not reachable). Recommendation: build real mentions on car-audio forums and local press; consider a Wikidata item only if notability exists.

## Recommendations
1. Resolve duplicate/mounted-site entity structure so each brand has one canonical host and one `@id` (project).
2. Add an answer-first intro (2-3 sentences: what, where, price, hours) at the top of the homepage and each service page; keep FAQ answers under ~80 words (medium).
3. Align the FAQ page text with llms.txt prices (quick).
4. Publish more dated, bylined, first-hand posts with measurable detail (install times, film specs, vehicle examples) (project).
5. Add `lastmod` accuracy and "Last updated" dates on price pages (quick).
6. Optionally add `llms-full.txt`; keep llms.txt free of model-behaviour instructions you are not comfortable with (quick).
