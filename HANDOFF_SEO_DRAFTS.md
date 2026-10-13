# Handoff: Audio MotorSports SEO / AIO audit and city-page rewrite

Written 2026-10-13 for Zack, Tom and the next session. Read this first.

## Hard rules (from Zack, still in force)
- Do not change, deploy or publish anything on any site. Drafts and reports only.
- Never delete, trim, merge, redirect away or noindex any city page or site. Every page stays live; fixes only improve pages.
- Zack and Tom review together before any change goes live.
- No PR, nothing to main. Pushing drafts to a non-main branch was allowed by Zack, but see "Git state".

## Business facts (owner-confirmed; use these)
- Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson CA 90745. "Avalon" is only ever a street name.
- Call AND text: (213) 429-1092. Never (310) 513-8800.
- Hours Mon-Sat 9:30-6, Sunday closed [CONFIRM: some listings show Sunday open].
- Reviews line: "Google 4.8 (654 reviews) and Yelp 4.7 (777 reviews), as of October 2026".
- Prices allowed, always "as of October 2026": Solar tint $249, Solar Ceramic $329 installed; Viper 3108V $269; Compustar 9910 from $499; AMS pods from $649 a pair; Kicker Comp box $249 box only. No Tesla model prices (site conflicts).
- No roof tint. No DJ products, wraps, PPF, glass repair, 48-state or national shipping. Financing wording only "Payment plan" / "Buy now, pay later". Products: in-store pickup or call for delivery, paid upfront.
- Carson is allowed as the shop's city on city pages. "Wait inside" wording: seating, TV with Netflix, free Wi-Fi, restroom, water fountain; mall, theaters, restaurants, Starbucks nearby; DoubleTree down the street; Cabrillo Beach ~12 min. LGBTQ-friendly, everyone welcome (clearly on Long Beach pages). Right off the 110, easy from the 405 and 710. ILWU, rail yard, refinery, Metro, SpaceX and corporate customers on matching cities, no partnership claims. Authorized 3M, Viper, Compustar dealer 20+ years and "400+ miles" [CONFIRM proof].
- Full rule list: city_rewrite/WRITER_BRIEF.md (Owner update 3 is the latest). Shared agent rules: city_rewrite/AGENT_COMMON.md.

## What exists (all under ams-seo-audit-2026-10-03/)
- Audit reports per site (8 sites), FIX_LIST.md (48 items), LAUNCH_AUDIT.md, HUB_FIRST_PLAN.md, SAFE_VS_UNSAFE_EXECUTION_GUIDE.md, MORNING_REVIEW_PACK.md, AI_VISIBILITY_QUERY_SET.md.
- hub_deep_dive/: TOMORROW_AGENDA.md, DRAFT_CONTENT_HUB.md, CITY_TEMPLATE_PILOT.md, LOCAL_CITATION_AUDIT.md, REPO_MAP.md, SERP_COMPETITOR_REPORT.md, regression harness in harness/.
- city_rewrite/<site>/drafts/<slug>.md: one draft per city page. Tools: qa_check.py (quality gate), build_index.py (REVIEW_INDEX.csv), apply_owner_corrections.py (idempotent, already run).
- llms_txt/: three cleaned llms.txt drafts + README.
- MANIFEST.md lives in the downloaded archive ams-seo-drafts-2026-10-07.tar.gz (936 files, no screenshots).

## City-page status when this was written (quality gate, `python3 -I qa_check.py <site>/drafts`)
| Set | Drafts | Target | Gate |
|---|---|---|---|
| hub | 158 | 158 | pass |
| tint | 109 | 109 | 3 fail: beverly-hills, fountain-valley, irvine still offer roof tint |
| beats | 109 | 109 | pass |
| amspods | 60 | 60 | pass |
| alarm | 77 | 145 | 1 fail (walnut meta); 68 pages unwritten |
| tesla | 119 | 124 | 40 fail; 23 reused sentences; 81 files mention roof and need roof-tint wording cleaned; 5 unwritten: monrovia, monterey-park, orange, rosemead, santa-ana |

Alarm slugs still missing are listed in city_rewrite/alarm/workorder_1..4.json. Tesla roof/fail review lists were split into three; rerun the gate to regenerate.

Eleven background writers were launched on 2026-10-13 for: alarm (4), tesla writes (1), tesla repairs (3), tint roof cleanup (1), lacarstereo /locations/ rewrite (1), Carson article + hub titles/intros/FAQs (1). Their results were NOT seen. Check what landed on disk before redoing anything: expected new files are city_rewrite/lacarstereo/LOCATIONS_PAGE_DRAFT.md, city_rewrite/carson_article/CARSON_ARTICLE.md, hub_deep_dive/HUB_MAIN_PAGE_DRAFTS.md. At handoff time none existed.

## Known issues and findings
- amspods live pages: all 60 /amspods/bagger-audio-<slug>/ URLs return 200 and canonical to amspods. An early report of the alarm template showing on 13 of them was not reproduced. 56 earlier hub-style amspods/alarm drafts were moved to _hub_style_strays/ (not deleted).
- Owner-details paragraph (marker `<!-- owner-details-2026-10-07 -->`) was inserted by script before the FAQ section of every draft before the new agents wrote; new drafts must write those lines in their own words (no marker).
- Quality gate extended to forbid: lobby, roof tint phrases, 100-day/Snap/Koalafi/EasyPay, 48 states, PPF, glass repair, old phone, 650+/770+.
- Standalone brand www hosts are blocked from this sandbox; brand pages were audited and drafted from hub-mounted copies (source line in each draft says so). Verify standalone sites from your own network.
- lacarstereo.com is live but robots-blocked and noindexed on ~124 of 127 pages; its /book/ form sent nothing. Not fixed; Zack/Tom decision.

## Open owner decisions ([CONFIRM] placeholders remain in drafts)
Price list; factory-warranty FAQ (west-covina, westmont, midway-city); City of Industry fleet offer; Sunday hours on listings; duplicate Yelp and Facebook pages; business-name spelling (AudioMotorSports with "s"); founding year (2003 vs 2015 vs 25+); indexing choices (lacarstereo, shop products, amspods city pages); Search Console access; dealer-claim proof; per-page SHOP NOTE slots for Nick; drive times are approximate.

## Git state
- Repo: audiomotorsports-sketch/ams-plugin-hub, branch claude/ams-seo-aeo-audit-saun8p. Local commits 16416ac (text drafts) and 97a1a90 (owner corrections) exist but were NOT pushed (pushes were blocked by the session's permission filter). The folder ams-seo-audit-2026-10-03 in the repo checkout is a copy of an earlier snapshot, with screenshots untracked. The container is temporary: the downloaded tar.gz is the only durable copy outside it.
- Nothing was merged, no PR opened, nothing deployed.

## Suggested next steps
1. Unpack the archive, then run the gate on every set: `cd city_rewrite && for b in hub tint beats alarm tesla amspods; do python3 -I qa_check.py $b/drafts | tail -3; done`.
2. Finish alarm (68), tesla (5 + roof cleanup + 40 fails), tint (3 roof fails).
3. Review the Carson article, hub titles/intros/FAQs, and the lacarstereo locations draft if they landed.
4. `python3 -I build_index.py <site>` per site, write PUBLISH_GUIDE.md for alarm/tesla/amspods, update MORNING_README.md.
5. Publish plan (Zack and Tom together): snapshot before and after with hub_snapshot.py / hub_diff.py, about 20 pages a day, closest cities first.
