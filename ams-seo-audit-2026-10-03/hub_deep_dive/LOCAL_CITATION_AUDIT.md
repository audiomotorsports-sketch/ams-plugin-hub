# Local / Citation / Entity Audit: Audio MotorSports (Carson, CA)

Prepared 2026-10-07 for Zack and Tom. Read-only research. Nothing was changed, posted, submitted, claimed or contacted. Every page and site stays live; every action below is additive and needs Zack and Tom's joint review first.

Verified facts used as the baseline: Audio MotorSports; 22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; Mon-Sat 9:30-18:00, Sunday closed. "Avalon" is the real street name.

## 0. How to read the evidence (important limits)

- **Third-party pages could not be opened.** Every WebFetch to Yelp, Facebook, Instagram, BBB, YellowPages, Yahoo, Nextdoor, Manta, Chamber of Commerce (chamberofcommerce.com), Birdeye, Poyst, Giftly, Tint Brokers, Apple Maps, and the brand dealer locators (Kicker, Compustar) returned EGRESS_BLOCKED. I did not try to bypass it. Only audiomotorsports.com pages were fetched.
- Everything else comes from **WebSearch**. That tool returns result titles and URLs (reliable, quoted below as seen) plus a machine-written summary. The summary often blends facts from several results, so a field such as "hours" or "review count" is **search snippet, not a fetched page**, and cannot always be tied to one URL. All such values are labelled `[snippet]` and treated as `[CONFIRM]`.
- **Not visible to me at all:** the Google Business Profile itself (rating, review count, categories, hours, attributes, duplicates), Bing Places, Google Maps duplicates, the dealer locators' results (JavaScript tools), Instagram, TikTok, press and chamber member lists. These are marked UNVERIFIED, not "absent".
- Fetched from the live hub today (verified): `/contact-us/`, `/about/`, `/reviews/`, `/services/window-tinting/`, `/tesla/`, `/llms.txt`, `/brands-we-love/`, and the Torrance city page JSON-LD.

## 1. What the hub itself says (verified, fetched)

| Item | What the hub says | URL |
|---|---|---|
| Name / address / call | Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745, call (310) 513-8800 | `/contact-us/`, `/about/` |
| Text line | **(213) 429-1092** labelled "Text"; llms.txt says "that is the line that receives texts. Call stays (310) 513-8800." Call/Text are separate buttons, so this is a deliberate split, not a primary-phone mismatch on the hub | `/llms.txt`, `/contact-us/` |
| Hours | Mon-Sat 9:30 AM - 6:00 PM, Sunday closed | `/contact-us/` |
| Schema name | `AutoRepair`, name "Audio MotorSports", alternateName "Audio MotorSports", "Audio Motorsports", "AMS"; telephone +13105138800; hours 09:30-18:00 Mon-Sat | Torrance page JSON-LD |
| sameAs (hub) | YouTube channel UCHYn2FTtiBZ53EXWNBWAyeg; instagram.com/audiomotorsports/; share.google/RyQaFlk39cTTMU6TG; facebook.com/Audiomotorsports/; tiktok.com/@audiomotorsports; **yelp.to/Lm2GAc4OiS** (short link); maps.google.com ftid 0x80c33234c579b9bd:0xa886ff7f43445f0a; lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com | Torrance page JSON-LD |
| Review claims | "Google 4.8 from 654 reviews. Yelp 4.7 from 777 reviews." `/tesla/` instead says "650+ Google reviews, 700+ Yelp reviews" | `/reviews/`, `/about/`, `/tesla/` |
| Age claims | `/about/` "20+ years"; `/services/window-tinting/` and `/tesla/` "Since 2003"; llms.txt "In business 20+ years", "AMS Pods, manufactured in-house since 2003" | various |
| Authorization claims | llms.txt: "3M Authorized Dealer", "Viper (Diamond Certified dealer)", Compustar; `/tesla/`: "3M certified · Viper Diamond dealer · Compustar authorized"; `/about/`: Alex "3M Certified Tinter". But `/brands-we-love/` makes **no** authorization claim and says "as if we were the authorized dealer" | llms.txt, `/tesla/`, `/about/`, `/brands-we-love/` |
| Not offered | llms.txt: "No vehicle wraps, auto glass repair, suspension, wheels, tires" | `/llms.txt` |
| Name variants on the hub | "Why LA Car Tint" heading and "Tesla Tint LA" H1/badge appear inside the Audio MotorSports pages | `/services/window-tinting/`, `/tesla/` |

## 2. Listings found (name, address, phone, hours, category, reviews)

Legend: **FETCHED** = I opened the page. **SNIPPET** = from WebSearch result title or summary only. Match column compares to the verified facts; "partial" means a deviation that is probably cosmetic.

| # | URL | NAP / details found | Source type | Match? | Note |
|---|---|---|---|---|---|
| 1 | https://www.audiomotorsports.com/contact-us/ | Audio MotorSports; 22025 S Avalon Blvd Ste A, Carson, CA 90745; call (310) 513-8800; text (213) 429-1092; Mon-Sat 9:30-6, Sun closed | FETCHED | Yes (baseline) | Text line is labelled as text, not primary |
| 2 | https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a and https://share.google/RyQaFlk39cTTMU6TG (Google Business Profile, linked from the hub) | Not visible. A search for the name with google.com domains returned nothing relevant | UNVERIFIED | UNVERIFIED | The GBP is the entity anchor. Review count 654 / 4.8 cannot be seen from here |
| 3 | https://www.yelp.com/biz/audio-motorsports-carson-3 | Title (snippet): "AUDIO MOTORSPORTS - Updated September 2026 - 2054 Photos & 782 Reviews - 22025 S Avalon Blvd, Carson, California - Car Stereo Installation". Mobile copy titled "Updated August 2026 ... 776 Reviews" (https://m.yelp.com/biz/audio-motorsports-carson-3?start=40) | SNIPPET (title) | Yes on name and address (has "S"); no "Ste A" in title; phone and hours not seen | Looks like the current Yelp page. The "-3" slug suggests earlier slugs existed |
| 4 | https://www.yelp.com/biz/audio-motorsport-carson | Titles (snippet): "AUDIO MOTORSPORT - Updated July 2026 - 2037 Photos & 774 Reviews - 22025 Avalon Blvd ..."; same slug at "April 2026 ... 750 Reviews" (?start=80) and "May 2024 ... 626 Reviews" (?start=200) | SNIPPET (titles) | **Partial/mismatch**: name is singular "AUDIO MOTORSPORT"; address lacks "S" and "Ste A" | **Possible second Yelp profile for the same shop.** Counts keep rising on both slugs in 2026, so it is not obviously abandoned. Whether it redirects to #3, is a merged page, or is a true duplicate is UNVERIFIED |
| 5 | https://www.yelp.com/biz/audio-wrapz-carson-4 | Title (snippet): "AUDIO WRAPZ - CLOSED - Updated March 2026 - 87 Photos - 22025 Avalon Blvd, Carson, California - Car Window Tinting" | SNIPPET (title) | Different business name, same street address | A **closed** Yelp page at the same building offering tint, wraps, stereo. Ownership relationship unknown [CONFIRM with Zack/Tom] |
| 6 | https://yelp.to/Lm2GAc4OiS (the Yelp link in hub sameAs) | Could not resolve (blocked) | UNVERIFIED | UNVERIFIED | Must be checked: does it point to #3 or #4? |
| 7 | https://www.facebook.com/Audiomotorsports/ | Page title "Audio MotorSport" (singular). Summary: 22025 Avalon Blvd, Unit A; (310) 513-8800; email audiomotorsports@gmail.com; "True One Stop Shop for vehicle accessories, car stereo, audio video, window tint, alarms, and wheels" | SNIPPET | **Partial**: singular name; "Unit A", no "S"; **lists wheels** (hub says no wheels/tires) | Hub sameAs links this page |
| 8 | https://www.facebook.com/p/Audio-MotorSports-Inc-100075715795350/ | Title "Audio MotorSports Inc."; summary: 22025 Avalon Blvd; (310) 513-8800; audiomotorsports@gmail.com; website audiomotorsports.com; window tint, alarms, GPS, door locks, tire rims, car wrap, car audio | SNIPPET | **Partial**: "Inc." name; lists rims and car wrap | **Second Facebook page for the same business** (apparent). Which is official, and who admins each, is UNVERIFIED |
| 9 | https://maps.apple.com/place?place-id=I52783642D95368A4 | Title "Audio MotorSports in Carson, CA United States - Apple Maps". Summary: 22025 Avalon Blvd, Carson, CA 90745; +1 (310) 513-8800; audiomotorsports.com; Mon-Sat 9:30-6; **Sunday 10:00 AM - 4:30 PM** | SNIPPET | **Mismatch on Sunday hours** if the snippet is right; address lacks "S" and "Ste A" | Apple Maps is what Siri and iPhone users see. Fixable free via Apple Business Connect. Confirm the Sunday hours directly in the app |
| 10 | https://www.bbb.org/us/ca/carson/profile/auto-customization/audio-motorsport-1216-911730 | Summary: "Audio MotorSport"; 22025 Avalon Blvd STE A, Carson, CA 90745-3300; (310) 513-8800; category Auto Customization; not BBB accredited; file opened 1/14/2019; **business started 7/6/2015**; Zack Asad listed as CEO; no rating issued | SNIPPET | **Partial**: singular name; no "S". **Start date 2015 conflicts with "since 2003" / "20+ years" / "25+ years"** | Free to claim and correct. Do not pay for accreditation as a link tactic |
| 11 | https://www.manta.com/c/mx6l61d/audio-motorsports-inc | Title "Audio MotorSports Inc. Carson CA, 90745"; summary: 22025 Avalon Blvd, Ste A; 310-513-8800; **"permanently closed"**; lists car wrap, wheels and tires, marine audio, Lambo doors | SNIPPET | **Mismatch: shown as permanently closed**; services list includes items the hub says it does not do | Stale aggregator record. Claim and correct |
| 12 | https://www.yellowpages.com/carson-ca/mip/audio-motorsport-520363313 | Title "Audio Motorsport - Carson, CA 90745" | SNIPPET (title only; details seen only in blended summaries: 22025 S Avalon Blvd suite a, (310) 513-8800, audiomotorsports.com, 4.8 from 604 reviews, **Sunday 10:00 AM-4:00 PM**) | **Partial / hours mismatch** if the Sunday value belongs to this page | Attribution to this URL vs Yahoo vs chamberofcommerce.com is UNVERIFIED because the search tool merged them |
| 13 | https://local.yahoo.com/info-177105567-audio-motorsport-carson/ | Title "Audio MotorSport in Carson, CA" (singular) | SNIPPET (title) | Partial (name) | Same blended data as #12 |
| 14 | https://www.chamberofcommerce.com/united-states/california/carson/car-stereo-store/1331484692-audio-motorsport | Title "Audio MotorSport in Carson, CA 90745 - 310-513..." ; blended summary quoted "Chamber of Commerce: 4.8 stars from 604 reviews" | SNIPPET | Partial (name) | This is a commercial directory named "Chamber of Commerce", **not** the Carson Chamber of Commerce. Do not confuse the two |
| 15 | https://nextdoor.com/pages/audio-motorsport/ | Title "Audio MotorSport - Carson, CA - Nextdoor" (singular) | SNIPPET (title) | Partial (name) | Nextdoor Business page exists; claim status UNVERIFIED |
| 16 | https://tintbrokers.com/tint-shops/carson/audio-motorsport/7945 | Title "Audio MotorSport - Carson, California" (tint directory) | SNIPPET (title) | Partial (name) | Industry directory listing exists |
| 17 | https://reviews.birdeye.com/audio-motorsport-149441235088378 | Titles: "Audio Motorsport - 797 Reviews - Car Stereo Installation in Carson, CA" and (page 4) "800 Reviews"; summary says 4.8 stars | SNIPPET | Name variant | Aggregate across sources (likely Google + Yelp + others, unverified). It is not a Google count |
| 18 | https://audio-motorsport.wheree.com/ | Title: "AUDIO MOTORSPORT - Reviews, Photos & Phone Number - Updated June 2026 - Auto Customization Service in **Avalon Village Hamlet**, Los Angeles County" | SNIPPET (title) | **Mismatch: locality "Avalon Village Hamlet" instead of Carson** | Low-value scraper, but it shows a wrong locality |
| 19 | https://www.poyst.com/business/audio-motorsport and https://www.giftly.com/gift-card/audio-motorsport-carson | Both titled with singular "audio motorsport / Audio MotorSport"; summary: 22025 S Avalon Blvd, Suite A, Carson, CA 90745; "electronics and auto-parts" | SNIPPET | Name variant (singular). Address matches | Auto-generated aggregators; the Giftly page suggests a gift-card profile exists. Giftly/Poyst claim status UNVERIFIED |
| 20 | https://www.superpages.com/carson-ca/bpp/angel-hands-auto-repair-473950527 and https://app.openbay.com/s/j-c-s-enterprises-inc-carson-ca | "Angel Hands Auto Repair 22025 Avalon Blvd, Carson, CA 90745", phone 310-522-4157; "J C S Enterprises, Inc ... Suite A" (auto repair) | SNIPPET | **Competing/stale records at the same address**, different phone | Likely former tenants. Not ours. Cannot be edited by AMS; note only, and if Google Maps shows them as open at our suite, tell Google through the Maps "report a problem" tool [CONFIRM first] |
| 21 | https://www.youtube.com/channel/UCHYn2FTtiBZ53EXWNBWAyeg | Title "Audio Motorsports" | SNIPPET (title) | Name variant (lowercase s) | Matches hub sameAs |
| 22 | https://www.instagram.com/audiomotorsports/ | Not found by search; fetch blocked | UNVERIFIED | UNVERIFIED | |
| 23 | https://www.tiktok.com/@audiomotorsports | Not searched successfully; fetch blocked | UNVERIFIED | UNVERIFIED | |

Searched with no hit (not proof of absence): Bing Places, Angi, Thumbtack, Mapquest, Foursquare (the only Foursquare URL surfaced earlier, foursquare.com/audiomot4388551 "Audio MotorSport - 2 tips", was not reconfirmed), Reddit (the search tool refused the domain), Tesla Motors Club and Harley forums (no AMS mention surfaced), press (Daily Breeze, Easy Reader: none), Carson Chamber membership list (directory is members-only per a search summary).

## 3. NAP comparison: what matches, what does not

| Field | Verified | Variants seen | Where | Severity |
|---|---|---|---|---|
| Business name | Audio MotorSports | "Audio MotorSport" (no s) | Yelp #4, Facebook #7, BBB #10, Yahoo #13, Nextdoor #15, Tint Brokers #16, Poyst/Giftly #19, Wheree #18 | Low-medium: many directories use the singular. Needs one choice and cleanup where owners can edit |
| | | "Audio MotorSports Inc." | Facebook #8, Manta #11, hub's own AI-search report notes "Audio MotorSports Inc" | Low |
| | | "Audio Motorsports" | YouTube #21, hub alternateName | Low |
| | | "LA Car Tint", "Tesla Tint LA", "LA Car Stereo" | **Appear only on the hub's own pages** (`/services/window-tinting/`, `/tesla/`, `/stereo/`). No third-party listing under these names was found | Medium risk on-site: three brand names sit beside the main name. Not a listing mismatch |
| Address | 22025 S Avalon Blvd Ste A, Carson, CA 90745 | "22025 Avalon Blvd" (no S), "Unit A", "STE A", "suite a" | Yelp #4, Facebook, Apple #9, BBB, Manta | Low: directional "S" and suite wording vary. Fix where editable |
| | | Locality "Avalon Village Hamlet" | Wheree #18 | Low (scraper) |
| | | Old address | **None found.** No evidence of a prior address | n/a |
| Phone | (310) 513-8800 | (213) 429-1092 used as primary | **None found** in any snippet. The text line appears only on the hub and in llms.txt as a labelled text line. Search for the number itself returned nothing relevant | OK |
| | | Other phone at same address | 310-522-4157 (Angel Hands Auto Repair, Superpages #20) | Not ours |
| Hours | Mon-Sat 9:30-18:00, Sun closed | **Sunday 10:00 AM-4:30 PM** | Apple Maps #9 (snippet) | **High (customer-facing)**: wrong open day |
| | | **Sunday 10:00 AM-4:00 PM** | YellowPages/Yahoo/chamberofcommerce.com group #12-14 (attribution to a single page unverified) | High |
| | | Mon-Sat 9:30-6, Sun closed | Yelp/Facebook/Poyst summaries (not tied to one page) | OK |
| Website | audiomotorsports.com | audiomotorsports.com | Apple, YP, Facebook | OK. The `www` canonical vs apex form was not checked on listings |
| Categories | n/a | "Car Stereo Installation" (Yelp), "Auto Customization" (BBB), "Car stereo store" (chamberofcommerce.com URL), "Car Audio Service" (Apple), "Car Stereo Installation in Carson" (Birdeye), "Auto Customization Service" (Wheree) | | Fine, but window tint is a large service and only the Tint Brokers listing shows it as a category [CONFIRM on Yelp] |
| Services | llms.txt: no wraps, wheels, tires | wraps, wheels/tires, rims, Lambo doors | Manta, Facebook #7/#8, Apple summary | Medium: listings promise services the shop says it does not do |
| Year founded | hub: "since 2003", "20+ years" | BBB start 7/6/2015; Facebook/Apple/Yelp/YP text "25+ years"; one summary "established in 1993"; Nick "sales since 1992" (about page) | | **Medium: five different founding stories.** Pick one provable statement [CONFIRM] |
| Status | Open | **"permanently closed"** | Manta #11 | High for that listing |

### Review counts: claimed vs visible

| Claim on site | What I could see | Status |
|---|---|---|
| Google 4.8 from 654 | GBP not visible. Other directories (likely mirroring Google): 604 reviews at 4.8 (YP/chamberofcommerce.com group, snippet), 639 at 4.8 (one blended summary), Birdeye aggregate 797 to 800 at 4.8 (snippet) | **UNVERIFIABLE.** Nothing contradicts 654, but nothing confirms it. The counts below 654 are consistent with older mirrors |
| Yelp 4.7 from 777 | Yelp titles (snippets): 626 (May 2024), 750 (Apr 2026), 774 (Jul 2026, slug #4), 776 (Aug 2026, slug #3), 782 (Sep 2026, slug #3). A summary also stated "4.7 stars, 782 reviews" | **Plausible but stale.** 777 fits between the Aug and Sep 2026 snapshots, so the count was probably correct on some date, and is now 782 or more. Date-stamp it. The two Yelp slugs also need explaining |
| `/tesla/` "650+ Google, 700+ Yelp" | consistent in direction with the above | wording differs from `/reviews/`; unify |

## 4. Sister brands and duplicate / competing listings

- **No sister brand has its own listing that I could find.** Searches for "LA Car Beats", "LA Car Alarm", lacartint.com / "LA Car Tint", teslatintla.com / "Tesla Tint LA", "AMS Pods" / amspods.com and lacarstereo.com returned nothing identifying those brands, only competitors and unrelated businesses (e.g. Rapid Window Tinting, customspeakerpods.com, a Las Vegas business called "L A Stereo"). This also suggests the brand domains are thinly indexed or not surfaced; Search Console is the only authority. UNVERIFIED, not proven.
- **Name collisions to be aware of:** "L A Stereo" (Las Vegas, poyst.com/business/l-a-stereo), "Audio Xcellence Motorsports" (Facebook / Yelp Henderson NV, closed), "Audio Creations Motorsports" (Instagram), "Premier Motorsports" (Carson). These are different businesses; do not link or claim them.
- **Possible duplicates for the same address (need Zack/Tom confirmation):** two Yelp slugs (#3, #4); two Facebook pages (#7, #8); Manta "Inc." record flagged closed (#11); the closed "Audio Wrapz" Yelp page at the same street number (#5); older tenants (Angel Hands Auto Repair, J C S Enterprises) still attached to the address on aggregators (#20).
- **Neighbouring competitor on the same street (information only):** Pro-tech Car Stereo & Tinting, 21906 Avalon Blvd, Carson 90745 (loc8nearme.com/california/carson/pro-tech-car-stereo-and-tinting/9680721/, snippet). Also Hollywood Tint (mobile) shows up for Carson on a business.google.com result.
- **Do not create separate Google/Yelp/Facebook business listings for LA Car Tint, Tesla Tint LA, LA Car Beats, etc. at the same address.** Google treats extra same-address listings for one business as spam-prone and can suspend them. The brand sites stay live and keep their names on the page; the local listings stay under Audio MotorSports.

## 5. Dealer locator and brand-site inclusion

I could not run any locator (JavaScript tools, and the hosts are blocked), so **whether AMS is already listed is UNVERIFIED** for all of these. The Llumar, 3M, Compustar and Rockford search results returned only the locator pages themselves, not an AMS entry; the Kicker "Q-Class retailers" page and Hertz "find a dealer" page also appeared but could not be opened.

| Locator | URL surfaced by search | Hub claim it supports | Needed before asking |
|---|---|---|---|
| 3M installer finder | https://www.3m.com/3M/en_US/car-personalization-us/resources/find-an-installer (and support/find-an-installer) | "3M Authorized Dealer", Alex "3M Certified Tinter" | 3M dealer or installer account number and certificate [CONFIRM] |
| Llumar | https://dealers.llumar.com/ ; https://northamerica.llumar.com/find-a-window-tint-dealer | Search summaries of hub pages mention Llumar and 3M films; the hub pages I fetched mention only 3M [CONFIRM] | Llumar dealer status [CONFIRM]; check whether Llumar is actually carried |
| Compustar / Firstech | https://www.compustar.com/find-a-dealer/ | "Compustar authorized"; Albert "Firstech, Compustar, iDatalink" | Firstech dealer number [CONFIRM] |
| Viper / Directed | not located by search | "Viper Diamond Certified dealer" | Directed dealer number and Diamond tier proof [CONFIRM] |
| Kicker | https://www.kicker.com/q-class-retailers (Q-Class), kicker.com/motorcycle-audio | brand listed on `/brands-we-love/` | Kicker dealer status [CONFIRM] |
| Hertz | https://www.hertzaudiovideo.com/where-to-buy-hertz-car-audio/find-a-dealer/ | brand listed | status [CONFIRM] |
| Rockford Fosgate | https://rockfordfosgate.com/dealerlocator/ | Harley-bagger work; Rockford is a Harley-audio brand | status [CONFIRM] |
| JL Audio, Focal, Pioneer, Sony, Phoenix Gold, Thinkware, Momento | not located | brands listed on the hub | status [CONFIRM] for each |
| Tesla / Harley | Tesla Owners Club directory https://engage.tesla.com/pages/clubs ; Tesla Club LA / Tesla Club SoCal surfaced in news | Hub has `/tesla/` and Harley bagger content | Genuine participation only (section 7) |

Important: only request inclusion on a locator where the shop actually holds the dealer or installer status. The hub currently claims several statuses (3M authorized, Viper Diamond, Compustar authorized) that no third-party page I could reach confirms. Proof (dealer number or certificate) should be gathered before the claims are repeated anywhere new.

## 6. Local organizations and communities (real links come from real participation)

| Organization | Evidence found | Notes |
|---|---|---|
| Carson Chamber of Commerce | CalChamber lookup page and a search summary: 530 E Del Amo Blvd, Carson, CA 90746; 310-217-4590; carsonchamber.com; membership about $20; directory reserved for members | All details are snippet only [CONFIRM on carsonchamber.com] |
| South Bay Association of Chambers of Commerce | https://southbaycities.org/about/about-the-south-bay/chambers-of-commerce/ (page not openable) | Gardena Valley, Torrance, Redondo Beach, Long Beach and similar chambers are nearby [CONFIRM names] |
| Tesla clubs | Tesla Club LA / Tesla Club SoCal (news results), Tesla Owners California takeover events with exhibitors, https://engage.tesla.com/pages/clubs | Event exhibiting is genuine participation. Fit with the `/tesla/` pages |
| Harley / bagger community | No Carson-area chapter surfaced; only product pages | Needs a human lookup of local HOG chapters and bagger meets [CONFIRM] |
| Car clubs / cruise nights / car shows | None surfaced | Needs Zack/Tom's own knowledge of local shows they attend |

## 7. Recommended actions (additive only)

No paid links, no review gating, no fake reviews, no astroturfing. Nothing here deletes, merges or redirects any page or site. Every item needs Zack and Tom to decide together first. "Who" means who should do it; none of this goes to a developer.

### Priority 1: do first (customer-visible errors and the entity anchor)

| # | Action | Effort | Who | Information needed |
|---|---|---|---|---|
| 1 | Check the Google Business Profile (you own it): confirm name is exactly "Audio MotorSports", address with Ste A, (310) 513-8800 as primary, hours Mon-Sat 9:30-18:00 with Sunday closed, primary category plus tint and alarm/security as secondary categories, website URL, and whether a duplicate or "moved/closed" listing exists in Maps for 22025 Avalon Blvd | 30 min | Zack | GBP login; the category list currently set; today's review count (to settle 654) |
| 2 | Claim and correct Apple Business Connect (free): remove Sunday 10:00-4:30 if wrong, use "22025 S Avalon Blvd Ste A", name "Audio MotorSports", add website and photos | 30 min | Zack | Apple ID for business; photo; confirm Sunday really is closed |
| 3 | Claim Bing Places (free; can import from GBP) so Bing, Copilot and Edge show the same NAP | 20 min | Zack | GBP link |
| 4 | Work out the two Yelp slugs: open `yelp.to/Lm2GAc4OiS`, then `/biz/audio-motorsports-carson-3` and `/biz/audio-motorsport-carson`. If one is a stale duplicate, use Yelp's own business-owner tools to report it to Yelp; do not ask reviewers to move. Make sure the site links to the primary one in full form (replace the yelp.to short link in sameAs only after Zack and Tom pick the page) | 30-60 min | Zack | Yelp business login; which page holds the real reviews |
| 5 | Decide which Facebook page is official (`/Audiomotorsports/` vs `/p/Audio-MotorSports-Inc-100075715795350/`). Make sure the official page has correct NAP, Ste A, hours Sunday closed, and services without wraps or wheels unless the shop does them. Leave the other page alone until a decision is made | 30 min | Tom | Facebook admin access to both pages |
| 6 | Adopt one name policy (see 7.4) and update only listings the shop owns | with items above | Zack + Tom | decision |
| 7 | Add date-stamps to review counts on the site ("as of [date]") and unify `/tesla/` wording with `/reviews/`; the Yelp number is already behind the visible 782 | 15 min | Tom | read both counts on the day |

### Priority 2: claim and correct existing free listings

| # | Action | Effort | Who | Information needed |
|---|---|---|---|---|
| 8 | Manta: claim and mark the business open; fix name, "S" in address, Sunday closed, and remove wraps/wheels/rims/Lambo-door services if the shop does not do them. | 30 min | Tom | business email; services list |
| 9 | BBB: claim the free profile, correct name/address, add website, categories, hours, and correct the start date once the real founding year is chosen (BBB shows 2015). Skip paid accreditation | 30 min | Zack | BBB login; verified founding year |
| 10 | YellowPages / Yahoo Local / chamberofcommerce.com: claim each, set Sunday closed, name "Audio MotorSports", address with S and Ste A. Note the "Chamber of Commerce" name here belongs to a commercial directory | 30 min each | Tom | verification phone/email |
| 11 | Nextdoor Business page: claim, add hours, address, phone, photos | 20 min | Tom | Nextdoor account |
| 12 | Tint Brokers listing: claim if possible and add 3M film brands and tint types | 20 min | Tom | brands actually carried |
| 13 | Instagram, TikTok, YouTube: confirm handles match the hub (`audiomotorsports`), and add website and (310) 513-8800 in the bio. None could be fetched | 15 min | Tom | login |
| 14 | Yelp categories: add Window Tinting and Auto Security/alarm categories if not present, so the Yelp profile represents all three service lines | 10 min | Zack | current categories [CONFIRM] |
| 15 | Aggregators (Wheree, Poyst, Giftly, Birdeye): do not chase. Ignore unless a listing shows a wrong phone or a closed status | none | n/a | |

### Priority 3: dealer locators and supplier pages (only where genuinely authorized)

| # | Action | Effort | Who | Information needed |
|---|---|---|---|---|
| 16 | Open each locator (3M, Llumar, Compustar, Viper/Directed, Kicker, Hertz, Rockford, JL, Thinkware, Momento) from a normal browser and search "Carson, CA 90745"; record present or missing in one sheet | 1 hour | Tom | none |
| 17 | For brands with status and no listing, ask the brand's dealer rep (through your existing account, not a cold outreach) to add or correct the entry with NAP exactly as in section 8 and the website URL | 15 min per brand | Zack | dealer account numbers [CONFIRM] |
| 18 | Where a brand has a "find an installer" page with a certification tier (3M, Viper Diamond), ask the rep how to be shown on the locator | 15 min | Zack | tier proof |
| 19 | Align on-site claims with proof: keep "3M Authorized Dealer", "Viper Diamond", "Compustar authorized" only if the paperwork exists; `/brands-we-love/` currently avoids these claims | 15 min | Zack + Tom | certificates |

### Priority 4: local organizations and community (genuine participation)

| # | Action | Effort | Who | Information needed |
|---|---|---|---|---|
| 20 | Join the Carson Chamber of Commerce if Zack and Tom want the member-directory link; confirm cost and directory format on carsonchamber.com first | 1 hour | Zack | chamber fees; NAP |
| 21 | Look at the South Bay chambers (Torrance, Gardena Valley, Redondo, Long Beach) only where the shop genuinely serves customers; join only the ones that give a directory page | 1 hour each | Zack | list of chambers |
| 22 | Tesla: exhibit at, or attend, Tesla Club LA / Tesla Club SoCal / Tesla Owners California events that allow vendors; post real before/after photos on the `/tesla/` page with the club's permission | event day | Nick/Zack | event calendar, customer photo consent |
| 23 | Harley: identify local HOG chapters and bagger meets; offer a real install-day demo or a ride-in; document it on the site | event day | Richard/Zack | local chapters [CONFIRM] |
| 24 | Local car shows, cruise nights, high-school programs in Carson and the South Bay: sponsor or attend where genuinely interested. A link from the event page is welcome when it comes naturally; never pay for a link, and tag sponsor links accurately if the event uses them | variable | Zack + Tom | calendar |
| 25 | Keep asking customers for reviews the normal way (a link or QR to Google and Yelp for everyone, not only happy customers). Do not offer incentives, do not filter who gets asked | ongoing | Nick | none |

### 7.4 Name policy to adopt (proposal for Zack and Tom to approve)

1. **Entity name everywhere off-site:** `Audio MotorSports` (capital M, S, plural). This matches the hub schema, Google profile link and Apple, so it is the lowest-effort anchor.
2. **Accepted variants only as alternateName in schema:** "Audio Motorsports", "AMS". Do not add "Audio MotorSport" (the singular many directories use) as an official name; just let directories keep it until each can be edited.
3. **Legal suffix:** use "Audio MotorSports Inc." only where a legal name is required (BBB, Manta, Facebook legal info) [CONFIRM the legal name].
4. **Sister brands stay as on-site brands only** (LA Car Tint, Tesla Tint LA, LA Car Beats, LA Car Alarm, AMS Pods, LA Car Stereo). Do not create separate listings. Where a brand page needs to show NAP, show the Audio MotorSports NAP.
5. **Address string:** `22025 S Avalon Blvd Ste A, Carson, CA 90745` (spell "Ste A" the same way everywhere editable).
6. **Phone:** `(310) 513-8800` as the primary listed number everywhere. Keep the text line (213) 429-1092 as a text-only contact on the site; it is already labelled that way.
7. **Hours:** Mon-Sat 9:30 AM-6:00 PM; Sunday closed.
8. **Founding story:** choose one provable claim [CONFIRM] and use it across hub, BBB and Facebook.

## 8. Canonical citation block (for listings; every value needs Zack/Tom confirmation first)

- Name: Audio MotorSports
- Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745
- Phone: (310) 513-8800
- Website: https://www.audiomotorsports.com/
- Hours: Mon-Sat 9:30 AM-6:00 PM; Sunday closed
- Categories (to confirm on each platform): car stereo installation (primary), window tinting, car alarm/security, remote start
- Services not to list unless offered: vehicle wraps, wheels/tires/rims, auto glass

## 9. What could not be verified

- Google Business Profile contents (name, categories, hours, 654/4.8, duplicates, "permanently closed" flags). Not visible to this audit.
- Bing Places; whether a Google Maps duplicate or old listing exists.
- Which Yelp slug is current and whether `yelp.to/Lm2GAc4OiS` points to it.
- Which Facebook page is official; Instagram and TikTok pages.
- Exact hours and phone on each directory: the Sunday values (10:00-4:00 and 10:00-4:30) came from machine-written search summaries, not from fetched pages.
- Whether AMS is present in any brand dealer locator.
- Whether any chamber, club, forum, Reddit or press page mentions AMS (Reddit refused by the search tool).
- Whether any sister-brand listing exists outside what search surfaced.
- Review counts: Google 654 and Yelp 777 cannot be confirmed; only partial, mixed-date evidence above.
- Founding year, legal name, and dealer authorization statuses.
- Standalone brand domains (lacarstereo.com, teslatintla.com apex, lacartint.com `www`, etc.) are proxy-blocked and were not fetched.
