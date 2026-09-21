# Cursor / Grok Bot — Audio MotorSports hub plugin

Copy everything below the line. **audiomotorsports.com only.** Branch **v1**. Screenshot phone before production.

---

You are editing **sites/audiomotorsports/** on branch **v1** only. One pass. Do not open other network repos. Do not invent images. Do not rewrite the homepage.

Repo: github.com/audiomotorsports-sketch/audiomotorsport
Vercel root: sites/audiomotorsports
Push to **v1**. Not main. Not redesign-home-five-sites.

## Job

The homepage is cluttered with offer tickets. The job is to **get people into the Carson bay**.

1. Insert the quote plugin **immediately under the existing banner**.
2. **Cut** the entire homepage ticket board (`<section class="offer-cards" id="offers">`) off `sites/audiomotorsports/index.html`.
3. **Paste** that same unedited block onto `sites/audiomotorsports/specials/index.html`.
4. Add a **Specials** link in the footer (and only there, plus the one text link already in the plugin).

Homepage order after this pass:

```
hero-banner          UNCHANGED
THE NEW PLUGIN
page-short-band
stats-bar
everything else
cta-band
```

There must be **zero** `.offer-card` / ticket plates on the homepage. They live on `/specials/`.

`/specials/` already exists (title: Shop Specials). Do not invent a new URL. Do not delete the existing specials prose cards. Put the moved ticket board **after** `<section class="page-hero">` and **before** `<section class="page-short-band">`.

## Files
1. Save `ams-plugin-hub.css` as `/assets/css/ams-plugin-hub.css`
2. In the homepage `<head>`, after the other stylesheets, add:
   `<link rel="stylesheet" href="/assets/css/ams-plugin-hub.css">`
3. Paste `ams-plugin-hub.html` as specified below.
4. On `/specials/`, add if missing:
   `<link rel="stylesheet" href="/assets/css/offer-cards.css?v=hubtintcontrast1">`
   (same file the homepage already uses — do not rewrite the CSS)
5. No new photos. Use images already on this site.

## HTML insert — homepage

Find this close on `sites/audiomotorsports/index.html`:

```
</section>
<section class="offer-cards"
```

That `</section>` belongs to `<section class="hero-banner">`.

**First** cut the entire `<section class="offer-cards" id="offers"> … </section>` block out of the homepage. Keep `id="offers"`. Do not edit tickets. Do not drop plates.

**Then** paste the full contents of `ams-plugin-hub.html` where that block was — immediately under the banner, before `<section class="page-short-band">`.

Final homepage must NOT contain `class="offer-cards"`.

## Tickets → /specials/

Paste the cut `offer-cards` block into `sites/audiomotorsports/specials/index.html` between:

```
</section>
<section class="page-short-band">
```

The first `</section>` closes `<section class="page-hero">`.

Do not edit plate copy, prices, or images. Do not add struck-through "was" prices.

## Footer — Specials link

In `sites/audiomotorsports/index.html` (and the shared footer include if one exists), under the **This desk** list, add:

```
<li><a href="/specials/">Specials</a></li>
```

Put it after Shop, before Locations. Do not add Specials to the primary nav. The hunter finds it in the footer.

If the footer is a shared partial used by every page, one edit covers the site. If it is copied per page, add the same `<li>` to the specials page footer too so it does not vanish.

## Do not
- Touch `<section class="hero-banner">` or its images on the homepage
- Touch chat (`ams-chat.js`, `#ams-chat`)
- Delete `#offers` — MOVE it to `/specials/`
- Delete `.mobile-cta-bar` HTML
- Change `:root` colors. This desk is hub gold `--accent: #C6A15B`. Not Beats red. Not alarm steel. Not tint pale.
- Invent photos. Use:
  - `/assets/img/hero/svc-stereo-hero.jpg`
  - `/assets/img/hero/svc-tint-hero.jpg`
  - `/assets/img/hero/svc-alarm-hero.jpg`
  - `/assets/img/hero/svc-bagger-hero.jpg`
- Print ticket prices inside the plugin. No `$249` `$269` `$329` `$499` `$649` in `ams-plugin-hub.html`. Those numbers stay on `/specials/` and in existing FAQ copy.
- Invent, infer, average, or do arithmetic on a price
- Struck-through "was" prices
- Use the word warranty / guaranteed / lifetime / financing
- Spell the brand "Los Angeles MotorSports" — it is **Audio MotorSports**
- Invent reviews
- Add Softail to the plugin. Pods door is Road King, Street Glide, Road Glide only.
- Route plugin doors to lacarbeats / lacartint / lacaralarm / amspods. Stay on audiomotorsports.com service URLs.
- Bulk-noindex city pages
- Rewrite `/privacy-policy/` or `/terms-of-service/` — they already exist

## Prices — locked (specials page only)
Do not change these numbers. Do not put them in the plugin.

- Solar, full car / four-door sedan doors — **$249** starting
- Solar Ceramic, same — **$329** starting
- Viper 3108V — **$269** installed
- Compustar 9910 — **$499** starting, most cars
- AMS pods — **$649** a pair starting

3M Color Stable / Ceramic IR: **quote only**. Do not print JSON 3M dollars on the hub.

## Sticky bar
`.ams-plug-sticky` has `right: 88px` so `#ams-chat` keeps the bottom-right corner on mobile.
**Hide the sticky at 1024px and up:**

```css
@media (min-width: 1024px) { .ams-plug-sticky { display: none; } }
```

Do not use `left: auto; right: auto` with a fixed width.

Plugin CSS hides `.mobile-cta-bar` only while `#ams-plug-hub` is on the page. Do not delete the old bar HTML.

## Phone / email
- Call: `tel:+13105138800` — (310) 513-8800
- Text: `sms:+12134291092` — (213) 429-1092
- Email: audiomotorsports@gmail.com
- Copy: **Ask for Nick**

## Door URLs (stay on this site)
- Stereo → `/services/head-unit-installation/`
- Tint → `/services/window-tint/`
- Alarm → `/services/car-alarms/`
- Pods → `/services/harley-bagger-audio-ams-pods/`

## SEO / legal — same pass

### P1 — homepage tickets must not remain
After the move:
```
grep -c 'offer-cards' sites/audiomotorsports/index.html   → 0  (except maybe a leftover comment — delete those too)
grep -c 'offer-cards' sites/audiomotorsports/specials/index.html  → 1
```

### P2 — schema geoRadius is 40 km. Owner answer: 100 miles.
In homepage JSON-LD, replace `"geoRadius":"40000"` with `"geoRadius":"160934"` (100 miles in metres). Do not invent a new radius.

### P3 — Softail
Plugin copy: Road King, Street Glide, Road Glide only.
Homepage FAQ currently says Softail (~7 hits). If you touch that FAQ answer ("Do you build Harley bagger audio?"), drop Softail so it matches AMS Pods. Fix **both** the visible `<details>` and the FAQPage JSON-LD, word for word, or leave both alone. Do not fix only one.

### P4 — privacy / terms
`/privacy-policy/` and `/terms-of-service/` already exist and are in the footer. Do not recreate them. Do not leave them unlinked.

### P5 — build notes
If you find `never call it anything else` or `schema aggregate only` or `Not a Long Beach Del Amo find-replace` on this site, replace both visible FAQ and JSON-LD the same way as the tint pass:

- `"Payment Plan only — never call it anything else. No 0%. No credit pitch."`
  → `"We quote the job first. If a Payment Plan is the right fit, you can apply at the counter."`
- `"Google shows 4.8 from 654 reviews — that is the schema aggregate only."`
  → `"Google shows 4.8 from 654 reviews for the shop overall, not for this page alone."`

Delete the Del Amo sentence.

### Flag only — do not do in this pass
- 109 city pages, zero noindex. Owner decision.
- Unused WebP twins. Markup change later.
- audiomotorsport.com (no S) is a separate domain. Do not touch it here.

## Done when
- Banner is byte-identical
- Plugin sits directly under the banner
- Homepage has **no** offer-cards / plates
- `/specials/` has the moved `#offers` board, contents unedited
- Footer **This desk** list includes Specials → `/specials/`
- Plugin has no dollar amounts
- Sticky hidden above 1024px
- Chat, `.mobile-cta-bar`, GTM-5G9HJLQ intact
- `geoRadius` is `160934`
- Plugin does not say Softail
- Phone screenshot: Text | Call left, chatbot clear bottom-right
- SMS opens to +1 213-429-1092 with year/make/model if filled
- Call is (310) 513-8800
- Ask for Nick

## Post-deploy checks
```
curl -s https://www.audiomotorsports.com/ | grep -c 'id="ams-plug-hub"'
curl -s https://www.audiomotorsports.com/ | grep -c 'offer-cards'
curl -s https://www.audiomotorsports.com/specials/ | grep -c 'id="offers"'
curl -s https://www.audiomotorsports.com/ | grep -c 'href="/specials/"'
curl -s https://www.audiomotorsports.com/ | grep -o 'geoRadius":"[^"]*"'
curl -sI https://www.audiomotorsports.com/privacy-policy/ -o /dev/null -w '%{http_code}\n'
curl -sI https://www.audiomotorsports.com/terms-of-service/ -o /dev/null -w '%{http_code}\n'
```

Expect: plugin 1, homepage offer-cards 0, specials offers ≥1, specials href ≥1, geoRadius 160934, privacy 200, terms 200.

Screenshot **phone** before production merge to branch `v1`.
