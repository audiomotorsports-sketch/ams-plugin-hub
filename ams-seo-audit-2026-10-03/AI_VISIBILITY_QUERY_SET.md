# AMS AI-visibility query set (for any GEO/AIO tracker)

Date: 2026-10-06. Report file only. Nothing was changed on any site or repo.

**Status:** prepared for the third-party tracker Zack shared (`vibha-ramprakash.github.io/seo-geo-tracker`). That tool could not be opened from this environment (network policy blocks the host), so its inputs and outputs are unknown. This list is tracker-agnostic: queries taken from the per-site `AIO_REPORT.md` / `AI_SEARCH_REPORT.md` files, each with the page that should earn the citation. These are editorial targets, not observed AI Overview results.

How to use it: for each query record, per engine (Google AI Overviews / AI Mode, ChatGPT search, Perplexity, Bing Copilot), whether Audio MotorSports is cited or mentioned, which URL, and the date. Re-run after fixes from `FIX_LIST.md` ship, using the same list, so the before/after is comparable. Take the baseline before any fix goes live.

## Queries taken verbatim from the reports
| Site | Query | Target page | Source |
|---|---|---|---|
| hub | car audio shop torrance | `/torrance/` (hub) + `/beats/car-stereo-torrance/` | audiomotorsports.com AIO #2 |
| hub | how long does window tint take | `/tint/faq/` | AIO #6 |
| hub | remote start installation los angeles | `/services/remote-start/` | AIO #8 |
| hub | apple carplay install carson / add carplay without replacing screen | `/beats/` | AIO #12 |
| hub | do you need an appointment for window tint / window tint near me open now | `/tint/`, `/contact/` | AIO #13 |
| hub | tesla tint carson | `/tesla/tesla-tint-carson/` | AIO #14 |
| shop | what amp for a 12 inch Kicker sub | `/shop/subwoofers/` + `/shop/amplifiers/` | shop AIO #5 |
| lacarstereo | car stereo installation torrance (also Gardena, Compton, Lakewood, Inglewood) | `/locations/` South Bay section, `/install/stereo/` | lacarstereo AIO #10 |
| teslatintla | tesla model y l window tint | `/blog/tesla-model-y-l-window-tint/` | teslatintla AIO #7 |
| teslatintla | california legal tint percentage tesla | homepage FAQ or new post | teslatintla AIO #10 |
| teslatintla | ceramic tint carson ca | `/tesla-tint-carson/` | teslatintla AIO note 6 |
| lacaralarm | south bay car alarm shop | `/alarm/locations/`, `/alarm/car-alarm-redondo-beach/` | lacaralarm AI_SEARCH #8 |
| amspods | harley road glide speaker pods | road-glide bagger audio page | amspods AI_SEARCH #1 |
| amspods | how much are harley speaker pods | `/services/ams-pods/` | amspods AI_SEARCH #3 |
| amspods | hertz neo vs cicada vs ds18 harley speakers | `/catalog/hertz/` | amspods AI_SEARCH #4 |
| amspods | harley bagger audio near long beach | `/bagger-audio-long-beach/` | amspods AI_SEARCH #8 |

Each report's own table has more (hub 15, teslatintla 12, lacartint 10, lacarbeats and lacaralarm and amspods 8 each, shop 10, lacarstereo 10). Pull the rest from those files when loading a tracker. Their draft answer passages carry [CONFIRM] tags: verify facts with the shop before publishing.

## Branded and entity checks (add to any tracker)
Run each as a brand query and record what the engine says (name, address, phone, hours, prices, services) against the facts below. Mismatches show where entity signals are split (see FIX_LIST B14, B15, D5).
- "Audio MotorSports Carson"
- "Tesla Tint LA"
- "LA Car Tint", "LA Car Beats", "LA Car Stereo", "LA Car Alarm", "AMS Pods"
- Ground truth from the sites: Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; hours Mon-Sat 9:30-18:00. Google rating cited on the sites: 4.8 from 654 reviews; Yelp 4.7 from 777.

## Gaps the tracker should confirm
- No Carson-targeted answer exists yet on the hub `/tint/`, lacartint, lacarbeats or lacaralarm copies; expect "carson" queries to show weak or no citation until FIX_LIST B4, B22, B26 are done.
- lacarstereo.com and the shop's product pages are noindexed today (FIX_LIST A1, A2). They cannot appear in AI Overviews or Google results while that stands, so a "not cited" result there is expected and not informative.
- Citation tracking needs live engine access. None was available in this audit.
