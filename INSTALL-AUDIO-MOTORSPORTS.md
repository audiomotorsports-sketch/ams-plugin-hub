# Cursor / Grok Bot — Audio MotorSports hub plugin

Copy everything below the line. **www.audiomotorsports.com only.** Branch **v1**. Screenshot phone before production.

---

You are BUILDING this into the **repo ROOT** of github.com/audiomotorsports-sketch/audiomotorsport. The hub Vercel root is `/`. There is **no** `sites/audiomotorsports/` folder. Do not open spoke repos. Do not invent images. Do not rewrite the homepage.

Push to **v1**. Not main.

index.html is ~63,264 bytes. Trust the measured anchors in this file.

## Job — three parts

A. INSERT the plugin directly under the banner.  
B. MOVE all **8** offer tickets OFF the homepage onto `/specials/`.  
C. ADD `/specials/` to the footer **via the generator**, so people who went looking can still find them.

The homepage asks for the car and the job, then gets out of the way. Discounts are for someone who went looking.

## Files
1. Save `ams-plugin-hub.css` as `/assets/css/ams-plugin-hub.css`
2. In homepage `<head>`, after the other stylesheets:
   `<link rel="stylesheet" href="/assets/css/ams-plugin-hub.css">`
3. Paste `ams-plugin-hub.html` using the depth-count insert below.
4. On `specials/index.html`, add if missing:
   `<link rel="stylesheet" href="/assets/css/offer-cards.css?v=hubtintcontrast1">`
5. No new photos. Use images already on this site.

## Insert method — DEPTH COUNT. Do not use a literal next-sibling string.

The tint install broke because it matched `</section>\n<section class="offer-cards"`. Removing offer-cards changes whitespace and the naive anchor misses.

Do this instead:

1. Find `<section class="hero-banner">` in `index.html`.
2. Walk forward counting `<section` (+1) and `</section>` (−1) until depth returns to 0. That `</section>` closes the banner.
3. Insert the full contents of `ams-plugin-hub.html` **immediately after that closing tag**.

Do **not** match the string that used to follow the banner. After offer-cards is gone, the next sibling is `page-short-band`. Order-independent. Cannot drift.

Do **not** touch `<section class="hero-banner">` or its images.

## Move the 8 tickets — not down, OFF

Current homepage order:

```
1  hero-banner
2  offer-cards            ← 186 lines, 11,482 chars, 8 cards. MOVE OUT.
3  page-short-band
4  stats-bar
5  section shop-drop-proof
6–13  content
14 cta-band
```

Required homepage order:

```
hero-banner
[PLUGIN]
page-short-band
stats-bar
…rest…
cta-band
```

`offer-cards` is **gone** from `index.html`. Not moved down. Removed.

The 8 cards, by title — copy as-is, do not edit contents:

1. PIONEER W3000NEX  
2. THINKWARE Q200  
3. KICKER DUAL 12 CVS  
4. KICKER COMPR 12  
5. SOLAR CERAMIC SEDAN  
6. SOLAR CERAMIC FRONTS  
7. VIPER 3108V  
8. COMPUSTAR 8910  

Keep `id="offers"`. Keep plate images. Keep offer-cards CSS.

## /specials/ already exists. Do not create it.

`specials/index.html` · ~17,096 bytes · `<h1>Shop Specials</h1>` · currently **zero** offer-card markup.

Paste the cut `offer-cards` block **after** `<section class="page-hero">` closes and **before** `<section class="page-short-band">`. Keep whatever is already on that page unless it directly duplicates a card.

`/specials/` is already in `sitemap.xml`. Do not duplicate the URL.

## Footer — generator only

`/specials/` is **not** in the footer. Do **not** hand-edit footer HTML. Hand-edits get overwritten on the next chrome run.

```
scripts/lib/network-chrome.mjs  →  SITES.hub.footerPages
add:  specials: '/specials/',
then: node scripts/apply-network-chrome.mjs
```

Expect hub pages patched. All five other sites reporting **0**. If a spoke reports a change, stop.

Put Specials after Shop, before Locations, if the generator preserves object order. If it sorts keys, leave the generator’s order — do not fight it.

## Plugin — capture the car. No prices.

Proof bar (separate cells, never merge Google + Yelp):

Google 4.8 from 654 · Yelp 4.7 from 777 · Since 2003 · Bay Carson · Walk-in Mon–Sat 9:30–6

Year / make / model. Job chips:

Car Stereo · Window Tint · Car Alarm · Tesla Tint · Harley Bagger Audio

Text us / Call with year/make/model + job prefilled into SMS. Ask for Nick.

This desk is hub gold `--accent: #C6A15B`. `theme-color` `#0A0A0A`. Same gold as pods. Not alarm steel. Not tint pale. Not Beats red.

Call `tel:+13105138800` · Text `sms:+12134291092` · Email audiomotorsports@gmail.com

Sticky: `right: 88px` on mobile so `#ams-chat` keeps the corner. **AND:**

```css
@media (min-width: 1024px) { .ams-plug-sticky { display: none; } }
```

Never `left: auto; right: auto` with a fixed width.

Plugin CSS hides `.mobile-cta-bar` only while `#ams-plug-hub` is on the page. Do not delete the old bar HTML.

### Door URLs — verified live. Network desks, not hub clones.

| Chip | href |
|---|---|
| Car Stereo | `https://www.lacarbeats.com/services/` |
| Window Tint | `https://www.lacartint.com/services/` |
| Car Alarm | `https://www.lacaralarm.com/services/car-alarms/` |
| Tesla Tint | `https://teslatintla.com/` |
| Harley Bagger Audio | `https://www.amspods.com/` |
| Specials (text link only) | `/specials/` |

Car Alarm copy on the card: **Viper, Compustar, GPS tracking, remote start.** There is **no** separate Remote Start ticket. GPS and remote start sit on the alarm desk.

Car Stereo copy: **Sound system. Stereo upgrades. Bass.**

Photos already on this site:

- `/assets/img/hero/svc-stereo-hero.jpg`
- `/assets/img/hero/svc-tint-hero.jpg`
- `/assets/img/hero/svc-alarm-hero.jpg`
- `/assets/img/inner/tesla-tint-desktop.jpg`
- `/assets/img/hero/svc-bagger-hero.jpg`

Harley door: Road King, Street Glide, Road Glide. **No Softail.**

Plugin HTML has **zero** dollar amounts.

## Prices — hub is the strictest

Homepage tickets currently show **no** prices in the HTML (they live in the plate images). Keep it that way.

Do not print any of these in the plugin. They stay on `/specials/` plates and existing FAQ copy:

- Tint Solar, full car — $249 starting  
- Tint Solar Ceramic, full car — $329 starting  
- Viper 3108V — $269 flat, installed  
- Compustar **9910** — $499 starting, most cars  
- Dual Kicker Comp box — $249 box only, install quoted  
- AMS Pod — from $649 a pair  
- 3M Color Stable / Ceramic IR — **QUOTE ONLY**. No public number.  
- **$340 is dead. Never resurrect it.**

⚠️ **FLAG, DO NOT FIX:** the homepage ticket title is **COMPUSTAR 8910**. The approved price list says **Compustar 9910**. One of those is wrong. Do not change either. Report it in the PR.

Never invent, infer, average, or do arithmetic on a price. No `<s>` / `<del>` / `<strike>` / “was $” / “reg. $”. `scripts/seo-audit.mjs` fails the build on those.

## Do not
- Touch `<section class="hero-banner">` or its images
- Edit the contents of any offer card — MOVE them
- Touch chat (`ams-chat.js`, `#ams-chat`)
- Delete `.mobile-cta-bar` HTML
- Change `:root` colours
- Use warranty / guaranteed / lifetime
- Say “financing” — the product is a **Payment Plan**
- Spell out “Los Angeles Car Beats/Tint/Alarm” as a brand. LA stays LA on the logo. Copy says “in Los Angeles”.
- Invent reviews, reviewer names, or quote text. The homepage has known placeholder names (**Marcus, Sofia, James**). Do **not** ship them and do **not** invent replacements. Leave those slots out.
- Touch any `*.php` file. They are excluded from the build.
- Hand-edit footers
- Create `/specials/`
- Bulk-noindex city pages
- Rewrite `/privacy-policy/` or `/terms-of-service/` — they already exist
- Add a separate Remote Start card or tab. Remote start and GPS sit on **Car Alarm**.

## SEO / legal — same pass

### P1 — build notes on ~124 hub pages (biggest content defect)

123 files: `Payment Plan only — never call it anything else. No 0%. No credit pitch.`  
124 files: `Google shows 4.8 from 654 reviews — that is the schema aggregate only.`

Each appears **twice** per page: FAQPage JSON-LD `acceptedAnswer.text` and the visible `<details>` accordion.

Fix **both** copies identically. Fixing one and not the other is a Google structured-data violation.

Replace:

- `"Quote the work first, then apply if a Payment Plan is the right fit. Payment Plan only — never call it anything else. No 0%. No credit pitch."`  
  → `"We quote the work first. If a Payment Plan is the right fit, you can apply at the counter."`

- `"Google shows 4.8 from 654 reviews — that is the schema aggregate only."`  
  → `"Google shows 4.8 from 654 reviews for the shop overall, not for this page alone."`

Delete these pipeline notes from **visible** copy wherever they appear:

- `Yelp stays out of that Google aggregateRating field`
- `This URL stays the network weave.`
- `Keep that line out of tint and alarm.`
- `If someone reversed that in a forum post, ignore it.`
- `This is not a Long Beach Del Amo find-replace.` (and variants)

Then fix the **hub** generators or the next build restores everything:

- `scripts/lib/hub-city-gold.mjs`
- `scripts/lib/hub-city-vivid-copy.mjs`

Hub generators only. Leave beats/alarm/pods/tint generators alone.

### P2 — live price editor in served HTML (2 files)

`<div class="admin" id="admin" hidden>` with “Shop admin — pricing”, Save prices, Reset to shop defaults, and the `tint-pricing.json` path.

Files:

- `estimator/index.html`
- `services/window-tinting/index.html`

Delete the **entire** div, matching `<div>`/`</div>` nesting. The block ends AFTER `<div class="adminmsg" id="amsg"></div>` — there is one more `</div>` to close the wrapper. Don’t stop a tag short.

Check for JS listeners (`#addfilm`, `#addveh`, `#asave`, `#areset`) before assuming none exist.

After this, served HTML must not contain “Shop admin”, “Reset to shop defaults”, or `tint-pricing.json`.

### P3 — robots.txt is actively broken

The file has ~10 named `User-agent` groups, each containing only `Allow: /`. Per RFC 9309 a crawler obeys **one** group — its most specific match — and named groups are **never** merged with `User-agent: *`. So `Disallow: /admin/` and `Disallow: /planner/` do **not** apply to GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, Applebot-Extended, or Bingbot. Those bots are invited into `/admin/`.

Fix: delete all allow-only named groups. Keep **one** group:

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /planner/
Sitemap: https://www.audiomotorsports.com/sitemap.xml
```

Document the AI-crawler stance in **comments**, not empty groups. Mention **Claude-SearchBot** in a comment (currently absent). `/admin/` is password-protected server-side (`api/admin.js` + `ADMIN_PASSWORD` → 401). This is crawl hygiene, not a breach.

### P4 — teslatintla ships inside the hub build

`.vercelignore` does not list `teslatintla`, so `https://www.audiomotorsports.com/teslatintla/` returns 200.

Mitigated (canonical to teslatintla.com, zero sitemap URLs) but it is duplication nobody chose.

**Before** adding a line: confirm nothing on the hub links to `/teslatintla/` and check whether the five `/teslatintla/api/*` rewrites in `vercel.json` are load-bearing for the hub deploy.

If they are not load-bearing: add one line to `.vercelignore`:

```
teslatintla
```

If they **are** load-bearing: **flag and skip**. Do not break the hub API.

### P5 — unused WebP twins (~450 pairs)

Optimised `.webp` files already sit beside the JPEGs. Markup still points at the heavy ones. This is a markup change, not a conversion job.

If you touch a hero/LCP image, change **preload and `<img>` together**. Copy the city-banner `<picture>` pattern. Never put a `.jpg` inside `type="image/webp"`.

If this blows the diff, **flag and skip** rather than rewrite 450 tags this pass. Plugin + tickets + P1–P4 first.

### P6 — flag only, do not act
- Same 4.8/654 `aggregateRating` on LocalBusiness. Owner decision to remove. Keep the number as visible text.
- ~183 URL paths duplicated hub vs lacarbeats (and others). Do not bulk-canonicalise.
- Hub already has `/privacy-policy/` and `/terms-of-service/`. Legal is **not** missing here.

## Done when
- Banner byte-identical
- `offer-cards` **gone** from `index.html`; all 8 cards on `/specials/`, contents byte-identical
- `/specials/` linked in the footer on every hub page, **via the generator**
- Section order: hero-banner → plugin → page-short-band → stats-bar
- chat, `.mobile-cta-bar`, GTM-5G9HJLQ intact
- Sticky hidden above 1024px
- Plugin has no `$` amounts
- Plugin does not say Softail
- `grep -ci "never call it anything else"` → 0 on this repo
- `grep -ci "schema aggregate only"` → 0
- `grep -ci "shop admin"` → 0
- `grep -ci "warrant\\|guarantee\\|financing"` → 0
- robots.txt has **one** `User-agent` group and mentions Claude-SearchBot in a comment
- Visible FAQ and FAQPage JSON-LD match word for word
- Every JSON-LD block still parses
- No placeholder reviewer names shipped (Marcus / Sofia / James)
- `node scripts/seo-audit.mjs` passes
- `git diff --shortstat`: report the deletion count and what went. Deletions are expected (offer-cards removal, admin blocks, build-note swaps, robots.txt). Unexpected deletions = stop.

## Post-deploy checks
```
curl -s https://www.audiomotorsports.com/ | grep -c 'id="ams-plug-hub"'
curl -s https://www.audiomotorsports.com/ | grep -c 'offer-cards'
curl -s https://www.audiomotorsports.com/specials/ | grep -c 'id="offers"'
curl -s https://www.audiomotorsports.com/ | grep -c 'href="/specials/"'
curl -s https://www.audiomotorsports.com/robots.txt
curl -sI https://www.audiomotorsports.com/teslatintla/ -o /dev/null -w '%{http_code}\n'
curl -sI https://www.audiomotorsports.com/privacy-policy/ -o /dev/null -w '%{http_code}\n'
```

Expect: plugin 1, homepage offer-cards 0, specials offers ≥1, specials href ≥1, robots one `User-agent: *` group, teslatintla 404 after ignore (or 200 if you flagged P4), privacy 200.

Screenshot **phone** before production merge to branch `v1`.
