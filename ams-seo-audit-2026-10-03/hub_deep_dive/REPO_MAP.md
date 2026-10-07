# REPO_MAP: ams-plugin-hub repo vs the live hub (audiomotorsports.com)

Prepared 2026-10-07, read-only. Nothing was changed, committed, pushed, deployed or deleted (repo, site or account). Every diff below is **written in this report only**. Nothing here goes live until Zack and Tom review it together.
Evidence tags: **[repo]** read from `/home/user/ams-plugin-hub` (all 5 files plus `git log -p`), **[live]** fetched 2026-10-07 from www.audiomotorsports.com (full sitemap crawl, 1,194 URLs: 1,161 x 200 plus 33 x 308 shop redirects), **[inferred]** reasoning from those, **[CONFIRM]** not verifiable from here.

---------------------------------------------------------------------------

## 0. Bottom line

1. **This repo is a "drop-in pack for AI coding bots", not the hub's source.** It holds 5 files (README, INSTALL doc, plugin HTML, plugin CSS, one JPG), 6 commits, all on 2026-09-21. It contains **no** `<title>`, no H1, no JSON-LD, no footer, no banner, no "Closed today", no Aftercare link, no `network-chrome.mjs`. The hub's real source is the separate repo `github.com/audiomotorsports-sketch/audiomotorsport` (INSTALL:7; a direct fetch of it returned 403 from the proxy, so I cannot tell if it is private or only blocked) [repo][live].
2. **Of the findings you listed, none of the on-page text originates in this repo's files.** The repo is related in four ways:
   - (a) it uses the same "paste the file header comment" pattern that leaks developer text on 8 live pages, but the leaked comments come from the four *sibling* plugin files (tint, beats, pods, alarm), which are not in this repo;
   - (b) its INSTALL doc is the instruction set whose steps are already visible on the live site (8 cards on `/specials/`, robots.txt single group, `/teslatintla/` 404, admin editor gone, `ams-plugin-hub.css` and the Tesla card JPG deployed byte-identical);
   - (c) its INSTALL doc is stale against the live home page (its anchors do not exist on the home page today);
   - (d) its INSTALL doc has instructions that can recreate the leak, a duplicate insert, wrong links and a mis-placed insert.
3. **Surprise: the hub plugin (hub-v2) is NOT on the English home page.** It is live only on `/es/` (the Spanish home, a translated and modified copy, not in the sitemap). The English home (`/`, 28,194 bytes, Last-Modified 2026-10-06 01:16:37 GMT) is a newer build: video hero, "Pick a skill" H1, 6-tile skill grid, shop showcase, its own `#quote` form, slim generator footer. The INSTALL doc describes the old home (~63,264 bytes, `hero-banner`, `offer-cards`, `page-short-band`, `stats-bar`, `cta-band`); none of those anchors exist there now.
4. **Do not run the INSTALL doc against the current home page as written.** It would (i) fail to find `<section class="hero-banner">`, (ii) duplicate `id="quote"` and the proof line, (iii) leak its own header comment, (iv) get its sticky bar rewritten by `main.js` (section 4).

---------------------------------------------------------------------------

## 1. Repo inventory (every file read)

| File | Bytes | Lines | What it is |
|---|---|---|---|
| `README.md` | 883 | 15 | "Repo root **is** the hub. Vercel root `/`. Branch **v1**." (README:5). Points bots at 3 raw GitHub URLs on `main`. |
| `INSTALL-AUDIO-MOTORSPORTS.md` | 14,557 | 325 | Prompt for Cursor/Grok. Job A insert plugin, B move 8 offer cards to `/specials/`, C footer via generator, plus P1-P6 "SEO / legal" tasks. |
| `ams-plugin-hub.html` | 6,345 | 145 | The plugin (`id="ams-plug-hub"`, `data-ams-plugin="hub-v2"`): proof bar, YMM inputs, 5 job chips, SMS/call, 5 door cards, sticky bar, inline JS. |
| `ams-plugin-hub.css` | 5,572 | 192 | Scoped `.ams-plug*`; gold `#C6A15B`; `body:has(#ams-plug-hub) .mobile-cta-bar{display:none!important}` (CSS:178). |
| `assets/tesla-tinted-card.jpg` | 105,588 | n/a | 1240x740 crop (matches the HTML width/height). |

History (`git log -p`, read only): `9fedc1a` initial; `b3d1d11` v1 pack (4 on-site doors, 4 chips, "sites/audiomotorsports/" layout, geoRadius 40 km to 100 mi task); `a26033d` v2 (doors flipped to 5 external network sites, depth-count insert, generator footer, SEO pack P1-P6; the v1 geoRadius and Softail tasks were dropped); `8d33b8d` Remote Start card replaced by Tesla Tint; `691d04f`, `43279eb` Beats trunk banner and Tesla lift crop. All authored as "Audio MotorSports <audiomotorsports@gmail.com>".

Public exposure: `https://raw.githubusercontent.com/audiomotorsports-sketch/ams-plugin-hub/main/INSTALL-AUDIO-MOTORSPORTS.md` returns 200 unauthenticated and is byte-identical to the local file [live]. The repo page returns 200. **The INSTALL doc is public** (see risk R9).

---------------------------------------------------------------------------

## 2. What is actually live from this repo (install status)

| Repo item | Live evidence | Status |
|---|---|---|
| `ams-plugin-hub.css` | `/assets/css/ams-plugin-hub.css` 200, `diff` identical to the repo file | Deployed. Linked only from `/es/` (line 51 of the served page); the English home does not load it. |
| `assets/tesla-tinted-card.jpg` | `/assets/img/plugin/tesla-tinted-card.jpg` 200, `cmp` byte-identical | Deployed; used on `/es/`. |
| `ams-plugin-hub.html` | `id="ams-plug-hub"` found on `/es/` only (0 of 1,194 sitemap URLs; `/es/` is not in the sitemap). Variant: Spanish copy, internal doors (`/services/car-audio/`, `/services/window-tinting/`, `/services/auto-alarms/`, `/services/tesla-tint/`, `/services/bagger-audio/`, all 308 to the mounts), bagger image `svc-bagger-hero-real.jpg`, header comment stripped, `data-sms-body` links. | Live on `/es/` as an adapted copy; **not** on `/`. The repo is not the source of truth for what is live. |
| Job B: 8 offer cards to `/specials/` | `/specials/` has `<section class="offer-cards" id="offers">`, the 8 titles in INSTALL:74-81, `offer-cards.css?v=hubtintcontrast1` linked. Home has 0 `offer-cards`. | Done. |
| Job C: `/specials/` in footer via generator | 0 of 1,022 generator-footer pages link `/specials/`. Only the 138 `/stereo/` pages (different footer) do. `/es/` has a body link only. | **Not done** (or reverted). |
| P1 build notes | `never call it anything else`: 0 pages. `schema aggregate only`: 0. But **`Payment Plan only. No 0%. No credit pitch.` still on 233 pages** and `This is not a Long Beach Del Amo find-replace` on 3 (`/tesla/tesla-tint-lakewood/`, `/alarm/car-alarm-lakewood/`, `/tesla/locations/`), `If someone reversed that in a forum post, ignore it.` on 1 (`/alarm/car-alarm-torrance/`). | Partially applied. The doc's own pass/fail greps (INSTALL:301-302) pass while remnants remain (R6). |
| P2 admin editor | "Shop admin", "Reset to shop defaults", `tint-pricing.json`: 0 pages. | Done. |
| P3 robots.txt | One `User-agent: *` group, Claude-SearchBot only in a comment. | Done. |
| P4 `.vercelignore teslatintla` | `/teslatintla/` returns **404**, but `/teslatintla/assets/css/*`, fonts and favicons return 200 and are linked by **152** hub pages (all of `/tesla/`). | Index page gone; assets still served. See R7 and section 5. |
| Doc post-deploy checks (INSTALL:313-321) | home `ams-plug-hub` = 0 (expect 1); home `href="/specials/"` = 0 (expect >=1); the other checks pass. | 2 of 7 fail. |

Cannot be inferred from the repo: why the English home lost the plugin. The served asset version tags (`skillbox`, `jessie1003`, `menu1004`, `slimfoot1005`, MMDD style) point to a redesign on 2026-10-03 to 10-05 [inferred]. The earlier audit (2026-10-04) measured the home at 59.8 KB; it is 28.2 KB now, so the home changed again after that audit.

---------------------------------------------------------------------------

## 3. Finding-by-finding map (questions 1 and 2)

Legend: **IN REPO** = the text exists in a repo file; **PATTERN** = same mechanism, text lives elsewhere; **NOT HERE**.

### 3.1 Home title "Audio MotorSports | Carson Shop" and H1 "Pick a skill"  -> NOT HERE
- Live: `<title>Audio MotorSports | Carson Shop</title>` (served line 13), og:title identical (line 18), `<h1>Pick a skill</h1>` (line 94) inside `<section class="section">` with `<p class="eyebrow">Carson shop</p>`.
- Repo: no `<title>`, no `<h1>`. The plugin's only headings are H2 (HTML:19), H3 (HTML:52), H4 per card. The INSTALL doc says "Do not rewrite the homepage" (INSTALL:7), so it would never fix this.
- Where it lives [inferred]: the hub repo's home `index.html` (hand-written; the `hub-home.css?v=skillbox` link is the page's own stylesheet). Search the hub repo for: `Carson Shop`, `Pick a skill`, `skillbox`, `hub-home.css`, `class="skill-grid"`.
- Fix already specified in FIX_LIST B5 / HUB_FIRST_PLAN fix 4 (not repeated here).

### 3.2 Hero / banner  -> PATTERN (anchor mismatch)
- Repo refers to `<section class="hero-banner">` at INSTALL:37 and :43 and :182, and HTML:3.
- Live home hero is `<section class="ams-hero" data-ams-hero="jessie-long-1003">` (video), not `hero-banner`. `hero-banner` appears on 725 crawled hub pages, but only **14** use the literal `<section class="hero-banner">`; **711** use variants (`hero-banner hero-banner--inner`, `--fold`, `--after-video`). `/es/` uses `hero-banner hero-banner--after-video`.
- So the INSTALL anchor matches 14 of 725 pages and 0 of the English home.

### 3.3 HTML comments ("quote plugin / INSERT after ... BEFORE ... Pair with ams-plugin-*.css", "TODO Zack")  -> PATTERN, text NOT HERE
- Live: the comment appears on exactly **8 URLs**: `/tint/`, `/tint/es/`, `/beats/`, `/beats/es/`, `/alarm/`, `/alarm/es/`, `/amspods/`, `/amspods/es/`. Examples [live]:
  - `/tint/` lines 131-136: `LA Car Tint quote plugin / INSERT after </section> of class="hero-banner" / BEFORE page-short (after you MOVE offer-cards) / Pair with /assets/css/ams-plugin-tint.css`
  - `/beats/` lines 120-125: `LA Car Beats quote plugin — guinea pig / INSERT after ... BEFORE <section class="offer-cards" id="offers"> / Pair with /assets/css/ams-plugin-beats.css`
  - `/alarm/` lines 325-330 and `/amspods/` lines 209-214 (same shape; `ams-plugin-alarm.css`, `ams-plugin-pods.css`).
  - The `*` in your wording is tint, beats, pods, alarm. `/tesla/` also has a plugin (`ams-plug-tesla`, `tesla-v1`) but its comment was stripped, as was the hub comment on `/es/`.
- Each leaked comment sits immediately above the plugin root (`id="ams-plug-tint"`, `-beats`, `-pods`, `-alarm`). That is the signature of "paste the whole plugin file including its header comment". **This repo's file has the identical header at HTML:1-6**, so the hub plugin would be the 9th leak if pasted whole, which INSTALL:39 tells the bot to do ("Insert the full contents").
- The comment's `Pair with /assets/css/ams-plugin-tint.css` path is also not what the page loads: the page links `/sites/lacartint/assets/css/ams-plugin-tint.css` (line 48 of `/tint/`). `/assets/css/ams-plugin-beats.css` and `-pods.css` return 404; `-tint.css`, `-alarm.css` return 200.
- "TODO Zack": **not on `/tint/` any more.** It is now at `/tint/services/hand-cut/` line 114: `<!-- TODO Zack: dedicated edge-close-up IDs. These three are tint jobs already used on lacartint. -->`. Separately, `<!-- TODO: owner should review this translation -->` appears 62 times across 15 `/es/` pages (`/tint/es/` x2, `/tint/es/faq/`, `/tint/es/payment-plan/`, `/tesla/es/`, privacy/terms in 4 mounts, etc.).
- Not here: the four sibling plugin files. Search the hub repo for: `quote plugin`, `INSERT after`, `guinea pig`, `TODO Zack`, `owner should review this translation`, `ams-plugin-tint`, `ams-plugin-alarm`, `ams-plugin-pods`, `ams-plugin-beats`; also the standalone brand repos (the same `index.html` is probably copied there [CONFIRM]).

**Proposed edit 3.3-A (this repo): neutral marker instead of instructions**

```diff
--- a/ams-plugin-hub.html
+++ b/ams-plugin-hub.html
@@ -1,6 +1,1 @@
-<!--
-  Audio MotorSports hub quote plugin  (hub-v2)
-  INSERT immediately after <section class="hero-banner"> closes.
-  Use depth-count (see INSTALL). Do not match a literal next-sibling string.
-  Pair with /assets/css/ams-plugin-hub.css
--->
+<!-- ams-plug-hub:start v2 -->
 <div class="ams-plug" id="ams-plug-hub" data-ams-plugin="hub-v2">
@@ -144,2 +139,3 @@
 })();
 </script>
+<!-- ams-plug-hub:end -->
```
(Line numbers shift by -5 after the first hunk; the end marker goes after current line 145.) Rationale: removes developer text from public source and gives installers a start/end marker for idempotent replace (section 6). The marker comments are harmless; if Zack and Tom want zero comments, drop them and use `id="ams-plug-hub"` as the marker.

### 3.4 "Closed today" banner  -> NOT HERE (but the plugin's sticky bar collides with its script)
- Live markup: `<div class="sunday-banner" id="sunday-banner" hidden role="status"><p>Closed today. Text Nick now and we'll hold a Monday 9:30 slot for you.</p><a class="btn btn-cta btn-sm" data-sms-body="Hi Nick, please hold Monday 9:30 for my [car]" ...>Text Nick</a></div>` placed **before** `<!-- hub-menu:start -->` (`/tint/` lines 63-67).
- Static in the template on `/tint/` 141 of 141 pages, `/alarm/` 203 of 203, `/book/`, plus `/tesla/`, `/tesla/es/`, `/tesla/book/`, `/beats/`, `/beats/es/`, `/beats/book/`, `/alarm/book/`, `/tint/book/`. Elsewhere (home, `/es/`, `/amspods/`, city pages) it is created by script.
- Script: `https://www.audiomotorsports.com/assets/js/main.js?v=nick20260924`, served lines 316-401, comment `/* Voted Sept 2026 — Text Nick chrome, Sunday banner, /book. Hub main.js only. */`. `pacificSunday()` (served line ~403) uses `Intl.DateTimeFormat(... 'America/Los_Angeles', weekday:'short') === 'Sun'`; the else-branch inserts the banner before `.topbar` or `document.body.firstChild`. CSS is injected by `ensureNickCss()` (id `hub-nick-css`): `.sunday-banner{display:flex;...padding:12px 16px;...}`.
- Search the hub repo for: `sunday-banner`, `pacificSunday`, `NICK_SUNDAY_BODY`, `hub-nick-css`, `Closed today. Text Nick now`.
- **Where it touches this repo:** `main.js` lines 360-379 loop over `document.querySelectorAll('.mobile-cta-bar, .ams-plug-sticky')` and, for any bar **without** `data-nick="1"`, empties it (`bar.textContent=''`) and rebuilds it as "Text Nick" + "Call" using the generic `NICK_QUOTE_BODY`. The repo's sticky bar has no `data-nick`:
  - HTML:94 `<div class="ams-plug-sticky" aria-label="Text or call">`
  - The plugin's script binds the YMM/job prefill to `[data-sms-sticky]` (HTML:143). `main.js` runs deferred on the home (`<script src="/assets/js/main.js?v=nick20260924" defer>`) and at the end of `<body>` inside `DOMContentLoaded` on `/es/`, so it runs after the page parses, deletes that anchor, and the prefill is lost. On `/es/` the Spanish label "Escríbele a Nick" would also be replaced by English "Text Nick" [inferred from code; **[CONFIRM] on a phone**]. The sibling plugins on `/tint/`, `/alarm/`, `/beats/`, `/tesla/` carry `data-nick="1"` on the sticky bar; the pods plugin and the repo's file do not.

**Proposed edit 3.4-A (this repo): opt the sticky bar out of the `main.js` rewrite**

```diff
--- a/ams-plugin-hub.html
+++ b/ams-plugin-hub.html
@@ -94,1 +94,1 @@
-<div class="ams-plug-sticky" aria-label="Text or call">
+<div class="ams-plug-sticky" data-nick="1" aria-label="Text or call">
```
For the banner itself (not in the repo; B2 in FIX_LIST): add `data-nosnippet` to `<div class="sunday-banner" ...>` in the `/tint/` and `/alarm/` templates and to the `banner` element created in `main.js` (`banner.setAttribute('data-nosnippet','')`), and reserve its height (`min-height` or overlay). Those files are not in this repo.

### 3.5 Footer network links (generator footer / `network-chrome.mjs`)  -> NOT HERE (INSTALL names the generator, nothing else)
- The only repo text: INSTALL:93-105: "Footer — generator only ... `scripts/lib/network-chrome.mjs -> SITES.hub.footerPages` add: `specials: '/specials/',` then: `node scripts/apply-network-chrome.mjs` ... Expect hub pages patched. All five other sites reporting **0**."
- Live: `<!-- hub-footer:start -->` ... `<!-- hub-footer:end -->` on 1,022 of 1,194 pages, and `<!-- hub-menu:start/end -->` for the header: the generator's output [inferred from marker comments]. The footer has four columns (Skills, Services, Shop, More). **No footer link goes to a brand domain** (lacarbeats.com etc.); the Skills column points to the internal mounts `/tesla/ /alarm/ /tint/ /amspods/ /stereo/ /beats/` plus `https://shop.audiomotorsports.com`. The Shop column (About, Contact us, Payment plan, Locations, Reviews, FAQ, Shop parts, Blog) is the likely `footerPages` object. **No Specials link** (job C not applied).
- The 138 `/stereo/` pages use a different footer that already has `<li><a href="/specials/">Shop Specials</a></li>`.
- Cross-brand links on the live pages are body "sister desk" cards, not footer links, e.g. `/tint/` lines 468, 584-594 (`https://teslatintla.com/`, `https://www.lacarbeats.com`, `https://www.lacaralarm.com`), `/beats/` 403-408, `/alarm/` 608-613.
- The repo says all five other sites are patched by the same run ("All five other sites reporting 0"), which tells us the generator spans hub + 5 spokes [repo]; a hub-only edit must not change spokes.
- Search the hub repo for: `network-chrome.mjs`, `apply-network-chrome.mjs`, `footerPages`, `hub-footer:start`, `hub-menu:start`, `slimfoot1005`, `hub-footer.css`.

**Proposed edit 3.5-A: only if Zack and Tom want the Specials link** (change is in the hub repo's `scripts/lib/network-chrome.mjs`, shown as INSTALL:98-99 describes it; the exact surrounding object is **[CONFIRM]** because that file was not available):
```diff
--- a/scripts/lib/network-chrome.mjs
+++ b/scripts/lib/network-chrome.mjs
 SITES.hub.footerPages = {
   ...
+  specials: '/specials/',
 }
```
Then run only the generator step INSTALL:99 names and require "all five other sites 0".

### 3.6 `/aftercare/` vs `/tint/aftercare/`  -> NOT HERE, and currently not reproducible on the hub
- The repo has no reference to aftercare.
- Live: `/aftercare/` returns 404; `/tint/aftercare/` returns 200. In today's crawl of all 1,194 URLs **no page links `/aftercare/`**; the 11 pages that mention aftercare link `https://www.audiomotorsports.com/tint/aftercare/` (5 pages) or `/tint/es/aftercare/` (3). The footer "Aftercare" link recorded in LAUNCH_NOTES (footer of `/tint/`, `/tint/window-tint-west-carson/`, `/tint/window-tint-anaheim/`) is gone from the served footer, which is now the slim generator footer (`hub-footer.css?v=slimfoot1005`) [live].
- So on the hub this is resolved by the footer rewrite, not by this repo. **[CONFIRM]**: the standalone `lacartint.com` (blocked from here) may still ship the old footer. Search the hub repo and `sites/lacartint/` for: `href="/aftercare/"`, `>Aftercare<`, and the footer data in `network-chrome.mjs`.

### 3.7 Card links and the five doors (repo HTML:54, 61, 68, 75, 82)  -> IN REPO
Current text, host, and what I could verify (hosts other than the hub and `teslatintla.com` are proxy-refused: `CONNECT 403`; not bypassed):

| Repo line | Chip | Current `href` | Host form | Evidence |
|---|---|---|---|---|
| HTML:54 | Car Stereo | `https://www.lacarbeats.com/services/` | www, trailing slash | Unverifiable from here (proxy). The same URL is linked from the live `teslatintla.com` home HTML. Hub mount twin `/beats/services/` is 200. Apex `lacarbeats.com` 308 to www (LIMITATIONS.md 2026-10-04), so www is the correct form. |
| HTML:61 | Window Tint | `https://www.lacartint.com/services/` | www | **Unverifiable and not linked anywhere I fetched.** All 13 live links to lacartint.com in the hub pages and the `teslatintla.com` home use only `https://www.lacartint.com/`. Hub mount twin `/tint/services/` is 200. **[CONFIRM]** that `www.lacartint.com/services/` resolves (this is the one most at risk of a 404). |
| HTML:68 | Car Alarm | `https://www.lacaralarm.com/services/car-alarms/` | www | Unverifiable (proxy). Same URL is linked from the live `teslatintla.com` home. Hub twin `/alarm/services/car-alarms/` is 200. |
| HTML:75 | Tesla Tint | `https://teslatintla.com/` | **apex** | Verified: 200 direct, canonical `https://teslatintla.com/`, title "Tesla Window Tint LA \| Model 3, Y, S, X"; `http://` 308s to the apex; `www.teslatintla.com` is unreachable from here. Apex is the right form. |
| HTML:82 | Harley | `https://www.amspods.com/` | www | Unverifiable (proxy). Linked as `https://www.amspods.com/` from live `/beats/` and `teslatintla.com`. |

Other link facts [live]:
- Card images: `svc-tint-hero.jpg`, `svc-alarm-hero.jpg`, `svc-bagger-hero.jpg` and `/assets/img/plugin/tesla-tinted-card.jpg` all return 200 on the hub. `/es/` uses `svc-bagger-hero-real.jpg` (200, 130,119 B) instead of `svc-bagger-hero.jpg` (114,593 B). **[CONFIRM]** which photo Zack wants.
- HTML:55 hot-links `https://www.lacarbeats.com/assets/img/hero/beats-hero-desktop.jpg?v=lock20260920c` (declared 2560x1440, shown in a 168 px high card, `loading="lazy"`). That is a cross-origin dependency on another domain and its `?v=lock20260920c` cache token; it could not be fetched from here. The same bytes exist on the hub at `/sites/lacarbeats/assets/img/hero/beats-hero-desktop.jpg` (200, 2560x1440, 507,579 B) with a `.webp` twin (200, 239,664 B).
- The INSTALL doc at :133 says "Door URLs — verified live". No date or tool is given, and v1 of the same doc (commit `b3d1d11`) said the opposite ("Route plugin doors to lacarbeats / lacartint / lacaralarm / amspods. **Stay on audiomotorsports.com** service URLs"). v2 flipped it. `/es/` live still uses the on-site doors. Decision for Zack and Tom: send visitors off-site (v2), or keep them on the hub mounts (v1 and `/es/`). **[CONFIRM]** intent; sending hub traffic to standalone domains also interacts with the mount-canonical question (FIX_LIST C8).
- Nothing in this repo links to a URL I could prove 404s. The risk list is: `www.lacartint.com/services/` [CONFIRM], the hot-linked Beats image [CONFIRM], and the `/specials/` text link (HTML:44), which is 200.

**Proposed edit 3.7-A (this repo): serve the Beats card image from the hub, not from another domain**
```diff
--- a/ams-plugin-hub.html
+++ b/ams-plugin-hub.html
@@ -55,1 +55,1 @@
-          <img src="https://www.lacarbeats.com/assets/img/hero/beats-hero-desktop.jpg?v=lock20260920c" width="2560" height="1440" alt="Car stereo install — trunk open" loading="lazy">
+          <img src="/sites/lacarbeats/assets/img/hero/beats-hero-desktop.webp" width="2560" height="1440" alt="Car stereo install — trunk open" loading="lazy" decoding="async">
```
Same photo, already on the hub, 239,664 B instead of 507,579 B, no cross-origin dependency. (WebP is supported by every current browser; if the team prefers a `<picture>` with the `.jpg` fallback, use the city-banner pattern INSTALL:283 mentions.) A smaller crop like the Tesla card (1240x740) would be better still, but that is a new asset, so it is a Zack/Tom call.

**Proposed edit 3.7-B (this repo): link the window-tint door to a URL proven to exist, until `www.lacartint.com/services/` is confirmed**
```diff
@@ -61,1 +61,1 @@
-        <a class="ams-plug-card" data-card="Window tint" href="https://www.lacartint.com/services/">
+        <a class="ams-plug-card" data-card="Window tint" href="https://www.lacartint.com/">
```
`https://www.lacartint.com/` is the only lacartint URL linked from the live hub (13 times). Alternative with zero cross-domain risk: `/tint/services/` (200 on the hub). **[CONFIRM] which one Zack and Tom prefer.**

### 3.8 Plugin visible copy that leaks internal wording (HTML:20, :51, :52)  -> IN REPO
Current text and problems:
- HTML:20 `<p class="lead">Stereo, tint, alarm, Tesla glass, Harley pods. One shop. Tickets live on Specials — not on this fold.</p>` ("Tickets" and "not on this fold" are developer jargon shown to customers; the sentence names no city.)
- HTML:51 `<span class="eyebrow">One bay. Four desks.</span>` over **five** cards (stereo, tint, alarm, Tesla, Harley).
- HTML:52 `<h3>Tap a door. It goes to that desk.</h3>` (jargon).
- The `/es/` copy of the same lines is also "Una bahía. Cuatro estaciones." over five cards and "Los precios están en Specials, no aquí." (prices on the page, not "tickets").

```diff
--- a/ams-plugin-hub.html
+++ b/ams-plugin-hub.html
@@ -20,1 +20,1 @@
-      <p class="lead">Stereo, tint, alarm, Tesla glass, Harley pods. One shop. Tickets live on Specials — not on this fold.</p>
+      <p class="lead">Car stereo, window tint, car alarm, Tesla tint and Harley bagger audio, all in one Carson bay. Looking for current specials? See <a href="/specials/">Shop Specials</a>.</p>
@@ -51,2 +51,2 @@
-      <span class="eyebrow">One bay. Four desks.</span>
-      <h3>Tap a door. It goes to that desk.</h3>
+      <span class="eyebrow">One bay. Five jobs.</span>
+      <h3>Pick your job. Each card opens that page.</h3>
```
No prices or new facts are added ("Carson bay" is from the verified address). If this edit is taken, the duplicate `/specials/` link at HTML:44 (`Digging for a price? <a href="/specials/">Shop specials</a>`) can stay or go; no removal is proposed.

### 3.9 Proof bar (HTML:9-13)  -> IN REPO
- `Google 4.8 from 654`, `Yelp 4.7 from 777`, `Mon–Sat 9:30–6` match the live home line ("Google 4.8 from 654. Yelp 4.7 from 777. Mon–Sat 9:30 AM – 6:00 PM", served line 95). `Bay Carson` fine.
- **`Since 2003` (HTML:11) is not supported as a shop claim.** Live pages say "AMS pods ... built in-house since 2003" and Richard "in the trade since 1998"; llms.txt says "In business 20+ years". **[CONFIRM]** with Zack what 2003 refers to before it ships as "Since 2003" in a bar labelled for the shop.
- The counts are hard-coded; the live site elsewhere already hard-codes them too (same maintenance risk as FIX_LIST B14).

### 3.10 Schema / JSON-LD  -> NOT HERE
- The repo has no JSON-LD. The plugin adds none. The INSTALL doc mentions it only in P1 (keep FAQ text and FAQPage JSON-LD identical, INSTALL:205-207, :306-307) and P6 (flag the 4.8/654 aggregateRating, INSTALL:288).
- v1 of the doc (commit `b3d1d11`) had "P2 — schema geoRadius is 40 km. Owner answer: 100 miles ... replace `"geoRadius":"40000"` with `"geoRadius":"160934"`" and "P3 Softail". **v2 silently dropped both.** Live: `"geoRadius":"40000"` is still on 75 pages; `160934` on 0. **[CONFIRM]** with Zack whether the 100-mile answer still stands (FIX_LIST B16 says widen).
- Live home JSON-LD is now a thin `AutoRepair` (keys: `@id name url image logo telephone email address openingHoursSpecification`; no geo, sameAs, areaServed, aggregateRating, priceRange, description, WebSite). `/es/` still carries the rich generated node (`data-ams-generated="primary"`, `AutomotiveBusiness+AutoRepair`, with `geo` 33.8270/-118.2650, `sameAs` x7, `areaServed` GeoCircle 40000, `aggregateRating` 4.8/654, `priceRange "$$"`, `alternateName`, `description`) plus a `WebSite` node. So the English home lost schema richness in the redesign; the node to copy already exists in the hub. Search the hub repo for: `data-ams-generated`, `"primary"`, `hasOfferCatalog`, `geoRadius`.
- sameAs includes the Yelp shortlink `https://yelp.to/Lm2GAc4OiS` (FIX_LIST B15); [CONFIRM] sameAs URLs before reuse.

### 3.11 Titles / meta  -> NOT HERE
- Repo has none. INSTALL names `/specials/` as `<h1>Shop Specials</h1>` (INSTALL:87); live `/specials/` title is "Shop Specials | Audio MotorSports".
- Live home title and meta are in 3.1. Live home meta description: "Audio MotorSports in Carson. Tesla tint, car alarm, window tint, AMS Pods, stereo, and beats. Call (310) 513-8800 or text (213) 429-1092. Payment plan available." (161 chars).

### 3.12 What explains the sitewide mounts  -> partially, by what the INSTALL doc reveals
- Repo evidence: v1 says "You are editing **sites/audiomotorsports/** ... Vercel root: sites/audiomotorsports" (commit `b3d1d11`); v2 says "repo **ROOT** ... **no** `sites/audiomotorsports/` folder ... Vercel root `/`" (INSTALL:7; README:5). So the hub repo is a monorepo that was restructured on 2026-09-21; "Do not open spoke repos" (INSTALL:7) confirms separate repos for each brand.
- Live evidence of the mount mechanism: brand pages on the hub load assets from `/sites/lacartint/assets/...`, `/sites/lacarbeats/assets/...`, `/sites/amspods/...`, `/sites/lacaralarm/...`, and the Tesla mount loads `/teslatintla/assets/...` (152 pages). INSTALL:265-269 adds: "teslatintla ships inside the hub build ... five `/teslatintla/api/*` rewrites in `vercel.json`", and :289 "~183 URL paths duplicated hub vs lacarbeats (and others)".
- Consequence: the hub's `/tint/ /beats/ /alarm/ /amspods/ /tesla/ /stereo/` mounts are folders of copied brand-site files, served under hub paths. A template or plugin comment fixed in `sites/<brand>/` fixes the mount; whether the standalone domain has its own copy is **[CONFIRM]** (blocked from here).

### 3.13 Prices (repo vs live)  -> IN REPO (doc), contradiction found
- Plugin HTML: **zero `$`** (verified by grep). Consistent with the owner rule.
- INSTALL:164: "Homepage tickets currently show **no** prices in the HTML (they live in the plate images)." **False on the live `/specials/`**: each offer card prints a price in HTML `<p class="offer-card__price">`: PIONEER W3000NEX $499 installed; THINKWARE Q200 $349; KICKER DUAL 12 CVS $299; KICKER COMPR 12 $199; SOLAR CERAMIC SEDAN $329; SOLAR CERAMIC FRONTS $149; VIPER 3108V $269; COMPUSTAR 8910 $399 (page: https://www.audiomotorsports.com/specials/). Only $329 and $269 appear in the doc's locked list (INSTALL:168-173) or in llms.txt; **$499, $349, $299, $199, $149, $399 are on the page but not in the doc's list: [CONFIRM] with the shop.**
- INSTALL:177 "FLAG: ... COMPUSTAR 8910 vs Compustar 9910. One of those is wrong." Live `/specials/` has both: card "COMPUSTAR 8910 — 2-Way LCD pager alarm — $399 installed" **and** a separate "Compustar 9910 remote start — $499 — Installed, most cars". They look like two different products, not one typo. **[CONFIRM]** with Zack. The doc's "approved price list says Compustar 9910" ($499) matches llms.txt.
- INSTALL:175 "$340 is dead": 0 occurrences live. Good.

---------------------------------------------------------------------------

## 4. Findings that do NOT originate here (question 3)

| Finding | Likely lives in (unknown; verify) | Search for |
|---|---|---|
| Home `<title>`, H1, thin LD, no hreflang | Hub repo home `index.html` (hand-written; `hub-home.css?v=skillbox`) | `Carson Shop`, `Pick a skill`, `skillbox`, `data-ams-generated`, `hreflang` |
| Home hero (`ams-hero`, jessie video) | Hub home `index.html`, `hub-hero-video.css?v=jessie1003`, `homepage-hero.css` | `data-ams-hero="jessie-long-1003"`, `ams-hero__media` |
| "Closed today" banner | Hub `assets/js/main.js` (served lines 316-401) and the static `<div id="sunday-banner" hidden>` in the `sites/lacartint` and `sites/lacaralarm` templates (and `/tesla/`, `/beats/` home) | `sunday-banner`, `pacificSunday`, `NICK_SUNDAY_BODY`, `hub-nick-css` |
| Leaked plugin comments x8 | The 4 sibling plugin files pasted into `sites/lacartint/index.html`, `sites/lacarbeats/index.html`, `sites/lacaralarm/...`, `sites/amspods/...` (+ `/es/` twins; likely also the standalone repos) | `quote plugin`, `INSERT after`, `guinea pig`, `Pair with /assets/css/ams-plugin` |
| "TODO Zack" | `/tint/services/hand-cut/` line 114 (a tint-mount page source) | `TODO Zack: dedicated edge-close-up` |
| 62x "TODO: owner should review this translation" | The `/es/` translation template(s) on tint, beats, alarm, amspods, tesla | `owner should review this translation` |
| Footer (no Specials; no brand links) | `scripts/lib/network-chrome.mjs` -> `SITES.hub.footerPages`; output by `scripts/apply-network-chrome.mjs` | `footerPages`, `hub-footer:start`, `slimfoot1005` |
| `/aftercare/` (404) | No longer linked on the hub; may remain in the standalone `lacartint.com` footer data | `href="/aftercare/"`, `>Aftercare<` |
| `Payment Plan only. No 0%. No credit pitch.` (233 pages) | Hub generators INSTALL:225-228 names: `scripts/lib/hub-city-gold.mjs`, `scripts/lib/hub-city-vivid-copy.mjs`; alarm mount city generator for the 74 `/alarm/` pages | `No 0%. No credit pitch`, `Payment Plan only` |
| `find-replace`, `reversed that in a forum post` | Same city generators (Lakewood, Torrance copy) | `Long Beach Del Amo find-replace`, `reversed that in a forum` |
| "We do not invent ..." (15 pages, e.g. `/faq/`, `/tesla/`) | FAQ and Tesla copy sources | `We do not invent` |
| geoRadius 40000 on 75 pages | Hub schema generator | `geoRadius` |
| 152 `/tesla/` pages loading `/teslatintla/assets/...` | Tesla mount templates | `/teslatintla/assets/` |
| `/teslatintla/` 404 | `vercel.json` (rewrites), `.vercelignore`, a removed `teslatintla/index.html` | `teslatintla` in `vercel.json` and `.vercelignore` |
| Warranty line vs "do not mention warranty" | Tint FAQ source (9 tint pages answer "30-day written workmanship warranty ...") vs `llms.txt` line "Do not mention warranty." | `What warranty do you give`, `Do not mention warranty` |

---------------------------------------------------------------------------

## 5. Risks inside the INSTALL doc itself (question 4)

R1. **Stale anchors, "trust" instruction.** INSTALL:11 "index.html is ~63,264 bytes. Trust the measured anchors in this file." Live home is 28,194 bytes and has no `hero-banner`, `offer-cards`, `page-short-band`, `stats-bar`, `shop-drop-proof` or `cta-band`. A bot told to trust missing anchors will improvise: it may insert at the first `<section`, or at the end, or fail silently while reporting success. Its own check "Section order: hero-banner -> plugin -> page-short-band -> stats-bar" (INSTALL:296) cannot pass on the current page.

R2. **Literal anchor fails on 98% of banner pages; depth-count fragility.** INSTALL:37 searches the literal string `<section class="hero-banner">`: 14 of 725 hub pages match, 711 use `hero-banner--inner/--fold/--after-video`. Counting itself worked on all 724 pages where I started from the real tag (my test: `<section\b` +1, `</section>` -1; all returned to 0), so the fragile part is **locating the opening tag**, not the counting. Remaining counting hazards: `<section` inside HTML comments, `<script>` strings or `<noscript>`; `</section >` with space or uppercase; `<section-foo` if matched without a word boundary; nested hero sections; a hero that is `<header>` or `<div>`; the `ams-hero` video hero on the home, which is a different class entirely.

R3. **Leak of developer text.** INSTALL:39 "Insert the full contents of `ams-plugin-hub.html`" and the file begins with a 6-line instruction comment (HTML:1-6) that reads "INSERT ... Use depth-count ... Do not match ... Pair with ...". This is exactly the live leak on 8 pages. Also INSTALL:3 "Copy everything below the line" hands the *entire* doc (with internal directives) to a bot that also edits copy.

R4. **Duplicate insertion.** Nothing in INSTALL says "if `id="ams-plug-hub"` already exists, do nothing / replace". A second run adds a second `#ams-plug-hub` (JS binds the first only), a second sticky bar, a second `<link>`; INSTALL:23-24 ("add if missing" appears only for `specials/index.html`, :26). `/es/` already contains the plugin, so an installer pointed at "all hub pages" or the home's `/es/` twin would duplicate it. On the **home** the plugin would also create a second `id="quote"` (live home already has `<section class="section" id="quote">`, served line 129) and repeat the proof line already in `home-lead`.

R5. **Wrong links.** (a) Doors flipped from on-site (v1) to five external domains (v2) without a dated verification (INSTALL:133); `www.lacartint.com/services/` is unproven (3.7). (b) INSTALL:152-153 forbids `/assets/img/inner/tesla-tint-desktop.jpg` while commit `8d33b8d` first shipped that file; the guard against overlay-type images exists only in prose. (c) INSTALL:22-28 save paths (`/assets/css/...`, `/assets/img/plugin/...`) differ from where mount pages actually load siblings (`/sites/<brand>/assets/css/...`). (d) The Specials footer step is instructed but not verified (live fails).

R6. **Exact-string cleanup with exact-string checks.** INSTALL:209-215 replaces two long exact sentences; INSTALL:301-302 verifies only those phrases. The live site shows the failure mode: the em-dash clause is gone but `Payment Plan only. No 0%. No credit pitch.` remains on 233 pages, and a `find-replace` build note remains on 3. The checks report 0 while internal text still ships.

R7. **P4 pre-check is too narrow and the action is a removal.** INSTALL:269 "confirm nothing on the hub links to `/teslatintla/`": 152 live hub pages link `/teslatintla/assets/css/style.css`, fonts, favicon, `city-pages.css` etc. A literal reading of `.vercelignore teslatintla` (INSTALL:271-275) would break styling on all 152 `/tesla/` pages. Live, `/teslatintla/` is now 404 while the assets still return 200, so something already removed the page (see section 7).

R8. **Sticky-bar collision with `main.js`** (3.4): the doc says "Plugin CSS hides `.mobile-cta-bar`" and "Touch chat" but never mentions that `main.js` rewrites `.ams-plug-sticky` unless `data-nick="1"`; the prefill promise (INSTALL:117) breaks.

R9. **Public repo exposes internal operating notes.** The doc is world-readable (raw URL 200). It states the admin location and protection (`/admin/`, `api/admin.js`, `ADMIN_PASSWORD`, INSTALL:261), the pricing editor path `tint-pricing.json`, "known placeholder names (Marcus, Sofia, James)" (:190), "$340 is dead" (:175), QUOTE ONLY items (:174), generator file names (:225-230), `vercel.json` rewrites (:269). AI engines that index public GitHub could also quote it. Also the leaked-copy style ("Payment Plan only — never call it anything else") is the same directive voice as these prompts [inferred]: bot instructions pasted into generator templates.

R10. **Deploy gate conflicts with review.** INSTALL:9 "Push to **v1**. Not main." and :325 "Screenshot phone before production merge to branch v1" - a bot pushes to a branch that may be the Vercel production branch **[CONFIRM]**. The standing rule is that nothing goes live before Zack and Tom review together.

R11. **Removal language.** INSTALL:70 ("`offer-cards` is gone ... Removed."), :217 ("Delete these pipeline notes"), :241 ("Delete the entire div"), :251 ("delete all allow-only named groups"), :271 (`.vercelignore`), :310 ("Deletions are expected ... Unexpected deletions = stop.") frame the work as deletion. Under the owner rules, these should be phrased as relocate, rewrite, or "flag and wait".

### Safeguards (proposed text for the INSTALL doc; shown here only)

S1. **Idempotency**: insert between markers and make the script refuse a second insert.
```diff
--- a/INSTALL-AUDIO-MOTORSPORTS.md
+++ b/INSTALL-AUDIO-MOTORSPORTS.md
@@ -35,5 +35,14 @@
-Do this instead:
-
-1. Find `<section class="hero-banner">` in `index.html`.
-2. Walk forward counting `<section` (+1) and `</section>` (−1) until depth returns to 0. That `</section>` closes the banner.
-3. Insert the full contents of `ams-plugin-hub.html` **immediately after that closing tag**.
+Do this instead:
+
+0. **Idempotency first.** If the target file already contains `id="ams-plug-hub"` or `<!-- ams-plug-hub:start`, STOP. Report "already installed". Never insert twice. Also stop if the file contains `id="quote"` (the plugin has its own).
+1. Locate the banner with an HTML parser (not a string match). It is the first top-level element after the header whose class list contains `hero-banner` or `ams-hero`. If none is found, STOP and report; do not guess a location. Known variants: `hero-banner`, `hero-banner--inner`, `hero-banner--fold`, `hero-banner--after-video`, `ams-hero`.
+2. Take that element's end offset from the parser (or count `<section`/`</section>` tokens while skipping comments, `<script>` and `<noscript>`, matching `<section\b` and `</section\s*>` case-insensitively) until depth is 0.
+3. Insert only the content between `<!-- ams-plug-hub:start v2 -->` and `<!-- ams-plug-hub:end -->` of `ams-plugin-hub.html` immediately after that end offset. Do not copy any other comment.
```
S2. **Do not trust stale numbers**: replace INSTALL:11.
```diff
@@ -11,1 +11,1 @@
-index.html is ~63,264 bytes. Trust the measured anchors in this file.
+Byte counts and section names in this file were measured on 2026-09-21 and can be stale. Re-measure the target page first. If an anchor named here does not exist, STOP and report; do not substitute another.
```
S3. **Deploy gate**: replace INSTALL:9.
```diff
@@ -9,1 +9,1 @@
-Push to **v1**. Not main.
+Do not push to a production branch. Commit to a review branch and open a preview. Nothing is merged or promoted until Zack and Tom have looked at it together.
```
S4. **Fix the false price claim** (INSTALL:164).
```diff
@@ -164,1 +164,1 @@
-Homepage tickets currently show **no** prices in the HTML (they live in the plate images). Keep it that way.
+The offer cards on `/specials/` print their prices in HTML (`offer-card__price`). Do not add prices to the plugin. Do not change any price on `/specials/`.
```
S5. **P4**: add the asset check (and make it flag-only).
```diff
@@ -269,1 +269,1 @@
-**Before** adding a line: confirm nothing on the hub links to `/teslatintla/` and check whether the five `/teslatintla/api/*` rewrites in `vercel.json` are load-bearing for the hub deploy.
+**Before** touching `.vercelignore`: `grep -rl '/teslatintla/' --include='*.html' .` must be empty (today 152 `/tesla/` pages load `/teslatintla/assets/*`), and the five `/teslatintla/api/*` rewrites must be shown not load-bearing. If either check fails, or the page `/teslatintla/` is live, FLAG and do nothing. Every page stays live.
```
S6. **Stronger greps** (INSTALL:299-310): replace the three exact-string greps with phrase-family greps.
```diff
@@ -301,2 +301,3 @@
-- `grep -ci "never call it anything else"` → 0 on this repo
-- `grep -ci "schema aggregate only"` → 0
+- `grep -rciE "never call it anything|schema aggregate|No 0%|No credit pitch|find-replace|reversed that in a forum|Keep that line out|network weave|stays out of that Google|We do not invent"` → 0 on the built output
```
**Post-insert verification checklist (read-only, run on the built page, not just the repo):**
1. `grep -c 'id="ams-plug-hub"' <page>` = 1; `grep -c 'ams-plugin-hub.css' <page>` = 1; `grep -c 'id="quote"' <page>` = 1.
2. `grep -ciE 'INSERT|Pair with|BEFORE|TODO|depth-count|guinea pig' <plugin block>` = 0 (the only comments left are the start/end markers).
3. Plugin block contains no `$`: `grep -c '\$' <plugin block>` = 0.
4. Order: the plugin block starts right after the banner's closing tag and before the next sibling (check with an HTML parser, print the 3 neighbouring top-level elements).
5. Every `href` in the plugin block returns a final 2xx/3xx-to-2xx: `/specials/` 200; the five doors; images; and **the repo's door list matches the doc's door table**.
6. Sticky bar has `data-nick="1"`; after load, `[data-sms-sticky]` still exists in the DOM (test on a phone or headless browser with `main.js` loaded).
7. Footer unchanged byte-for-byte except the one generator-added line; `node scripts/apply-network-chrome.mjs` reports spokes 0.
8. JSON-LD blocks before and after: same count, all parse; FAQ visible text equals FAQPage text.
9. `/es/` still contains exactly one plugin (do not reinstall there).
10. Phone screenshot of home at 390 px; chat bubble not covered; no horizontal scroll.

**Proposed minimal repo-side edit to make the markers meaningful** is 3.3-A above.

---------------------------------------------------------------------------

## 6. Does anything in this repo contradict the owner rules? (question 5)

| Owner rule | Result | Evidence |
|---|---|---|
| No prices in the plugin / never write prices not on the live site | **Consistent.** Plugin HTML has 0 `$`. | `ams-plugin-hub.html` grep. The doc lists prices (:168-175) that match llms.txt ($249, $329, $269, $499 for 9910, $249 box, $649); $340 appears nowhere live. |
| Prices on the page match the doc | **Contradiction (doc vs live).** | INSTALL:164 says tickets show no prices; `/specials/` prints 8 prices incl. $399, $349, $299, $199, $149, $499 not in the doc's list. [CONFIRM]. |
| Never noindex any page | **Consistent.** | No noindex in the plugin; INSTALL:194 "Do not Bulk-noindex city pages". Live: home has no noindex. |
| Every page and site stays live; never remove, trim, merge, redirect away | **Conflicts (instructions).** | INSTALL:70 removes the ticket board from the home (content moved to `/specials/`, which is the stated purpose, but it is a trim of the home); :241 deletes a div block from 2 pages (already done live); :251 deletes robots groups (already live; config, not a page); **:271 `.vercelignore teslatintla`** hides a path that was 200 (live now: `/teslatintla/` is 404). :310 "Deletions are expected". |
| Nothing goes live without Zack and Tom reviewing together | **Conflicts.** | INSTALL:9 and :325 push to `v1`; production branch **[CONFIRM]**. 5 of the 6 INSTALL jobs are already live, with the home out of sync (section 2). |
| Do not hand fixes to a developer | The doc is itself a developer/bot handoff prompt. Not a conflict with a rule on content; noted so the new edits above are applied by the owners' own process, not by a new handoff. |
| Facts: only use what is on the live site; unverified marked [CONFIRM] | Plugin facts: hours, phone, address ok; `(213) 429-1092` text line is on the live site; `Since 2003` **[CONFIRM]**; "Ask for Nick" is on the live site; `Harley: Road King, Street Glide, Road Glide. No Softail.` (INSTALL:158, HTML:86) **contradicts** 46 live pages that list Softail (`/amspods/` 26, `/beats/` 7, `/alarm/` 3, `/vehicles/` 2, `/tesla/` 2, `/services/` 1) and the pods copy; **[CONFIRM]** which is right (FIX_LIST C9). |
| Do not use "warranty / guaranteed / lifetime / financing" | The doc's final grep (:304) would not return 0 on the hub today: "warranty" in the privacy policy, ToS (guarantee), and a tint FAQ answer "30-day written workmanship warranty..." on 9 tint pages and `/tint/es/`. `llms.txt` says "Do not mention warranty." **[CONFIRM]** the intended rule (FIX_LIST B20). |
| `Avalon` is a real street | The plugin has no city text. Consistent. |

Items the doc already protects and that hold live: no `Marcus/Sofia/James` on any crawled page; no `financing`; no `$340`; privacy-policy 200.

---------------------------------------------------------------------------

## 7. Additional observations (not asked, evidence-based)

1. **`/teslatintla/` went from 200 (INSTALL:265, 2026-09-21) to 404 (2026-10-07).** `/teslatintla/assets/...` is still served. If this was not a decision Zack and Tom made, it breaks "every page stays live". It is not in the sitemap. Confirm intent and history of `.vercelignore` / `vercel.json` before the next change; restoring means ignoring only what is not needed, not hiding the whole folder.
2. **`/es/` (hub Spanish home) is not in `sitemap.xml`**, yet `hreflang` on `/es/` points to `/` and `/es/` while `/` carries no hreflang (FIX_LIST B9). Adding the return tags and the `/es/` URL is additive.
3. **Plugin family**: live plugin ids `hub-v2` (`/es/`), `tint-v1`, `beats-v1`, `pods-v1`, `alarm-v2`, `tesla-v1` (stylesheet `/teslatintla/assets/css/ams-plugin-tesla.css?v=cards20260926`). Six plugins, one authoring template. Fixing the header comment pattern once (3.3-A) and the `data-nick` opt-out for `pods-v1` is the repeatable fix; the siblings are not in this repo.
4. **Accessibility (additive)**: chip buttons (HTML:29-33) toggle `.is-on` visually only; adding `aria-pressed` in the script's `paint()` would expose state. The inputs are not inside a `<form>`; fine for an SMS composer. No change proposed beyond noting it.

---------------------------------------------------------------------------

## 8. Limits and [CONFIRM] list

Limits: `www.lacarbeats.com`, `www.lacartint.com`, `www.lacaralarm.com`, `www.amspods.com` returned `CONNECT 403` from the egress proxy (not bypassed), so door targets and the cross-origin Beats image could not be fetched; `github.com/audiomotorsports-sketch/audiomotorsport` (hub repo) returned 403 and its source (`index.html`, `scripts/`, `vercel.json`, `.vercelignore`, `main.js` source tree, sibling plugin files) was not read; I read the served `main.js` and `network-chrome.js` instead. No browser was available, so the `main.js` sticky-bar rewrite is from code reading. A few fetches hit transient resets and were retried (up to 3). Counts come from one crawl on 2026-10-07 (1,161 pages 200, 33 redirects).

[CONFIRM] list:
1. What "Since 2003" means (shop vs pods) before it ships as a shop-level claim.
2. Whether `https://www.lacartint.com/services/` resolves; whether `www.lacarbeats.com/services/`, `www.lacaralarm.com/services/car-alarms/`, `www.amspods.com/` and the Beats image URL are all 200.
3. Door policy: off-site network doors (v2) vs on-site mounts (v1 and `/es/`).
4. Prices on `/specials/` that are not in the doc's locked list ($499 Pioneer, $349 Thinkware, $299 Kicker Dual 12 CVS, $199 Kicker COMPR 12, $149 Solar Ceramic Fronts, $399 Compustar 8910) and whether 8910 and 9910 are two products.
5. Softail on the pods pages (46 live pages) vs "No Softail" in the plugin and doc.
6. Whether Zack still wants the 100-mile `geoRadius` (v1 doc answer; live is 40000).
7. Whether `/teslatintla/` 404 was an intended decision; whether branch `v1` is the production branch.
8. Whether the standalone domains share the leaked comments, the Aftercare footer link, the sticky-bar behaviour (all blocked from here).
9. Warranty wording rule (tint FAQ "30-day written workmanship warranty" vs llms.txt "Do not mention warranty").
10. Whether the repo should stay public.

Files used: `/home/user/ams-plugin-hub/{README.md, INSTALL-AUDIO-MOTORSPORTS.md, ams-plugin-hub.html, ams-plugin-hub.css, assets/tesla-tinted-card.jpg}` and `git log -p`; prior reports `~/ams-seo-audit-2026-10-03/{FIX_LIST.md, HUB_FIRST_PLAN.md, audiomotorsports.com/*}`; live fetches listed above.
