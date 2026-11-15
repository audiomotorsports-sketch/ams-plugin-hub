# Handoff: Audio MotorSports website (as of Nov 15, 2026)

Paste this whole file as the first message of a new project or conversation.

## Where things stand

- **Repo:** `audiomotorsports-sketch/audiomotorsport`, site root `fresh/`.
- **Live site:** audiomotorsports.com runs branch `claude/website-fix-nov12`, commit `f82438aa`.
- **Waiting for GO:** branch `claude/website-audit-fix-nov12`, commit `25e6884c` (live-audit fixes 1 to 10). Pushed, not deployed, no pull request.
- **Who deploys:** Kareem, only on Zack's GO. The coding agent never deploys to production.

## Open items for Zack

1. **Confirm the labor-price removal.** The Nov 12 Doc said "never publish install or labor prices", so `25e6884c` removes about 2,000 lines that are live today:
   - Price menu: CarPlay, backup camera, speakers, sub and amp, build-my-sound, install-only and tint removal now say "Call or text for a quote".
   - Stereo estimator: cards show the stereo's price only; no installed total, no parts-plus-labor split.
   - `/stereo/` headline has no price.
   - Jessie's chat prompt (`data/chat-prompt-ams-v2.md`) no longer gives labor or hourly prices.
   - Kept: installed package prices for tint, alarms, subs, dash cams and ignition kill.
2. **Vercel preview.** There is no preview link. The Vercel connector lost access to project `ams-21` (team "Zack", slug `zack-f599`) on Nov 13: listing and creating deployments both return 403. Either reconnect Vercel with access to that project, or Kareem opens the branch preview in the Vercel dashboard.
3. **English about page** still says "Zack owns the shop". Only the Spanish line was changed (to "Gerente de Operaciones"). Decide whether to change the English one.
4. **BMW and Mercedes-Benz** model pages have no make link, because the host redirects `/vehicles/bmw/` and `/vehicles/mercedes-benz/` to `/vehicles/`. Removing those two redirects would allow real make pages.
5. **Tint simulator captions** (three lines) still repeat on every car page; they are part of the simulator.
6. **`/contact/` speed** did not improve (largest paint about 4.5 s locally).
7. **West Carson** city pages (7) keep "West Carson" in title and H1. It is a different place from Carson; left alone.

## Standing rules (never break)

- Warranty stays vague: only "Brand new, with the manufacturer's warranty" / "Everything we sell is brand new and comes with the manufacturer's warranty." No warranty lengths, no return, refund or restocking terms, never "lifetime", never "money back".
- Never publish install or labor prices.
- No "Carson" in any title or H1. Carson stays in the address and map only.
- No "South Bay" in any title or H1 (Zack, Nov 12): headlines say Los Angeles. Body text may keep South Bay.
- Say "payment plan", never "financing".
- Yelp award years only: 2016, 2020, 2023, 2024, 2025, 2026. "Yelp award winner since 2016".
- Call (310) 513-8800. Text (213) 429-1092. Never 513-6800.
- Hours: Mon-Sat 9:30 AM-6 PM, closed Sunday.
- Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745.
- Nick is Sales Manager, never "owner". Zack is Operational Manager.
- Never delete, retire, redirect or noindex a page. Rewrite instead. New pages are fine.
- Never mention Twilio. Do not touch social media. Do not submit any live form.
- Teslas: tint only, ceramic only.
- Shipping text: "Shipping is available after you call or text us and we make the deal." Products stay InStoreOnly in schema.
- Never invent a number, price, time, fit or fact. Use only data already in the repo.
- No emojis. Preview only; never production.

## How the repo is built and checked

- Build: `node shared/scripts/build-site.mjs` (from `fresh/`), output in `fresh/site` (4,186 pages). Then `cp vercel.json site/vercel.json`.
- Full check, in order: `check-brands`, `build-site`, `build-doors`, `check-door-urls`, `check-links`, `check-copy`, `STRICT=1 rules-check`, `seo-audit`, then `node --test --test-concurrency=2 tests/*.test.mjs`, then `check-finder` (about 15 to 60 minutes).
- After any change to `shared/tokens/*.css`: run `critical-css.mjs` (needs `CHROME=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`) and `contact-critical.mjs`, then rebuild.
- After checks: `git checkout -- doors shared/data/lastmod.json; git clean -fdq doors`.
- `rules-check` bans phone digits in source (use `SHOP.phoneTel` / `SHOP.textTel`) and some words in source files.
- Last results on `25e6884c`: 778 tests, 776 pass, 0 fail, 2 skipped; 0 broken links of 592,828; car finder 651 cars, 1,953 picks, all pass.

## Key files added in the last two jobs

- `shared/scripts/lib/audit-fix.mjs`: build-time pass. Rewrites South Bay to Los Angeles in titles and H1s, strips any labor price, fixes reversed hours wording.
- `shared/scripts/lib/hours-line.mjs`: one hours spelling everywhere.
- `shared/scripts/lib/hub-answer.mjs`: answer boxes on the six hubs and the home page.
- `shared/scripts/lib/hub-headlines.mjs`: hub H1s and their "from" prices.
- `shared/scripts/lib/model-pages.mjs`: model pages and the new make pages.
- `shared/scripts/lib/car-extras.mjs`, `vehicle-layout.mjs`: car year page text.
- `shared/scripts/lib/trust-strip.mjs`, `service-ld.mjs`, `facts.mjs` (fact block, shipping line).
- Tests: `tests/website-fix-nov12.test.mjs`, `tests/website-audit-fix-nov12.test.mjs`.

## Live audit of Nov 13 (score 7.7 of 10), for reference

Scores before the `25e6884c` fixes: facts 9, warranty 10, Carson and LA reach 6, schema 8, AI readiness 8, speed 7, technical 7, car pages 6, mobile first screen 8. The ten fixes in `25e6884c` answer the audit's top ten. A re-audit after deploy would show what moved.

## Suggested first steps in the new project

1. Get Zack's answer on the labor-price removal (item 1 above).
2. Get a preview of `claude/website-audit-fix-nov12` and check 7 pages return 200 on it.
3. On GO, Kareem deploys `25e6884c`.
4. Re-run the live audit after deploy.
