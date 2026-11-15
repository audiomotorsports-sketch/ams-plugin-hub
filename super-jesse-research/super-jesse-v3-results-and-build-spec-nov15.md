# Super Jesse v3: Research Results and Build Spec

PUT IT IN CLAUDE DUET

This is the output of "Claude Code - Super Jesse Research v3 (Fable 5.2) - Nov 15". Research only: nothing was changed, restarted, sent, posted or bought.

## Prompt for Claude Duet (paste this with the Doc link)

Read this whole Doc before you plan anything. It is the research for Super Jesse and the build spec. Your job is to finalize the build plan from it, not to start building.

1. Do not change code, restart anything, send any customer message, post, or buy anything until Zack types GO.
2. First, give Zack the list in section 2 as plain yes/no questions, one line each, and wait for his answers.
3. Ask Zack or Nick to run the three hand tests in section 3 and report pass or fail. Do not design around anything marked UNVERIFIED until its test passes.
4. Then write the build plan in the order in section 1, using section 4 as the spec. For each step say what gets built, where it runs, what it costs, and what proof Zack will see (section 4.11).
5. Draft `CORE.md`, `INDEX.md` and the topic files from the AMS Bible using the split in section 4.2, and settle every conflict in section 6 with Zack's answers. Where the Bible and the site disagree on a price, the higher price wins.
6. Jesse is sales chat only. Anything that needs code goes to Claude Code as a task, not to Jesse.
7. Standing rules stay as written in the AMS Bible: call (310) 513-8800, text (213) 429-1092, "payment plan", no labor or install prices, warranty stays vague, Nick is Sales Manager, Zack is Operational Manager, nothing sent without GO, no secrets in chat or Docs.
8. Show Zack the 10 example replies in section 7 and get each one approved, changed or cut before any of them goes into a topic file.

Report back in plain words, short, with what is decided, what is waiting on Zack, and what you will build first.

## 0. Read this first

- **Where it ran.** A Claude Code cloud session on Fable 5.2, not on AMS-1. AMS-1, Jesse's past chats and the xAI bill were not visible.
- **What was read.** All 4,139 pages of the live audiomotorsports.com (copy of Nov 13), the Nov 15 checklist, the Nov 7 core reply style, the 54 old Jessie skills, and the Nov 9 and Nov 14 machine prompts.
- **Web research limit.** Google's, xAI's, Yelp's and Telnyx's own help pages were blocked from this session. Facts about them come from search extracts and third-party pages. Every item marked UNVERIFIED must be tested by hand before anyone builds on it.
- **No analytics.** Google Analytics and Search Console are not connected to this session, so "which pages close" is judgement.
- **Not legal advice.** The texting, recording and payment-plan notes are practical cautions with sources.

## 1. Verdict

**Sell the most**
1. Answer in minutes, not 35. The best study (Harvard Business Review 2011, 1.25 million leads) found contact within an hour about 7 times likelier to qualify a lead than an hour later.
2. Shorter texts: opener, the published price if there is one, one question. Keep the 150-word template for Yelp and email.
3. Turn follow-ups back on, capped at three: next shop morning, day 3, day 7. Reply rates drop by about half with each nudge, so more than three only earns opt-outs.

**Cut the most cost**
1. Wake Jesse only when a message lands. Never on a timer that calls the AI.
2. Core rules plus one topic file per wake, with the core rules as a byte-identical opening so Grok bills it at the cached rate (about 75% off).
3. Scripts, not AI, for the three daily texts, junk sorting, reminders and contact names.

**Order to build:** three hand tests (section 3), lead store, watcher, core rules and topic files, spend cap, daily texts, follow-ups, then a real texting number.

**Expected cost after:** about $0.40 to $0.60 a day on the top Grok model, $0 hosting.

## 2. Decisions Zack makes before Duet builds

1. **Where the watcher lives.** Recommended: Google Apps Script in the shop's Google account (section 4). It runs in Google's cloud for free, so AMS-1, Chrome tabs and sign-outs stop mattering for texts-in, Yelp, website forms, voicemail and missed calls.
2. **How Jesse sends texts.** Google Voice has no API, and its policy bans sending "through an automated process, such as a script". Driving the Google Voice web page with a bot is a suspension risk as well as the thing that kept breaking. The clean answer is a registered business texting number (Telnyx, section 9). Until then, Jesse drafts and a person taps send, or Jesse replies only by email and Yelp.
3. **Marketplace and OfferUp.** No official way exists to read or answer those chats by program, Facebook restricted the account on Nov 14, and OfferUp only works in the phone app. Recommended: keep both human for now, with Jesse writing the suggested reply for Zack to paste. Night auto-posting is the kind of activity that gets accounts restricted.
4. **Labor prices.** The live site still shows CarPlay labor $250, backup camera $199, speakers $89, sub and amp $249 and hourly rates. The waiting website branch removes them. Jesse never quotes them either way.
5. **Discount days.** The Bible says Tuesday to Friday only. The site says "book online and save" with no days. Pick one and make both match.
6. **Review ask.** Google bans asking only happy customers and bans rewards. The safe rule is ask every customer once, Google link only. Yelp: never ask. An old Jessie skill sends both links; retire it.
7. **The price conflicts in section 6.**

## 3. Three hand tests to run first (30 minutes, a person does them)

| # | Test | If it passes | If it fails |
|---|---|---|---|
| 1 | In Gmail, reply to one forwarded Google Voice text (the email from an address ending `txt.voice.google.com`). Does the customer get it as a text? UNVERIFIED for 2026: one source says replies bounce. | Jesse can answer existing text threads by email, no browser. Still do not automate it at volume given Google's policy. | Texts out need Telnyx from day one. |
| 2 | Reply by email to a Yelp lead notification, then reply by email to the customer's second message. | Yelp answers need no browser. | The checklist already says only the first email reply posts. Use Yelp's own app for later replies, or the Zapier "Yelp Leads" app (it has a reply action). |
| 3 | In Google Voice settings, turn on all three: forward texts to email, missed-call email alerts, voicemail by email. Call the shop line and hang up. | Missed calls and voicemails become leads Jesse can see. | Nothing lost; texts still forward. |

## 4. Build spec

### 4.1 Shape

```
Gmail (Google Voice texts, missed calls, voicemail transcripts,
       Yelp leads, website forms)
        |
   Apps Script time trigger, every 2 minutes, NO AI
        |   - label and skip junk, tapbacks, dealer mail, our own alerts
        |   - group messages from the same customer inside 3 minutes
        |   - if nothing new: exit in under a second
        v
   Lead store (Google Sheet or SQLite): one row per customer
        |
   ONE Grok call per customer batch
        |   input:  CORE rules + today's handoff + ONE topic file
        |           + that customer's row + last 15 messages
        |   output: strict JSON (section 4.5)
        v
   Send gate (plain code): rules check, quiet hours, who-sent-last,
   reply cap, spend cap
        |
   Send (email / Yelp relay / texting number) or queue for a person
        |
   Text Nick the new lead. Update the row. Log cost.
```

Why Apps Script: free, already inside the Google account, talks to Gmail, Calendar, Sheets and Contacts with no extra logins, calls Grok with `UrlFetchApp`, and has nothing to sign out of. Limits on a Workspace account: 6 hours of trigger runtime a day, 6 minutes per run, 100,000 outside calls a day. A 2-minute trigger that exits fast uses a few minutes a day.

Fallback if Zack wants it on AMS-1: about 200 lines of Python under systemd, polling Gmail every 60 seconds. Same shape. Polling beats Gmail push here: no public address needed and no "watch" that silently expires every 7 days. IMAP IDLE works too but Gmail drops idle connections after 10 to 15 minutes and plain-password logins ended for Workspace in May 2025, so it needs OAuth and a reconnect loop.

### 4.2 Files Jesse reads (the Bible v3 split)

Plain markdown, any model can use it. This is the open "Agent Skills" layout: only names and one-line descriptions are always loaded; a file's body loads when needed.

| File | Size | Loaded |
|---|---|---|
| `CORE.md` | 2 pages max | Every wake, always first, never edited mid-day |
| `INDEX.md` | 1 page: topic name + one line each | Every wake |
| `handoff/YYYY-MM-DD.md` | 1 page | Every wake |
| `topics/tint.md`, `tesla.md`, `stereo-carplay.md`, `alarm-remote-start.md`, `dash-cam.md`, `subs-speakers.md`, `harley.md`, `payment-plan.md`, `sales-and-black-friday.md`, `booking.md`, `objections.md`, `follow-ups.md`, `reviews.md`, `yelp.md`, `marketplace-offerup.md`, `spanish.md`, `shipping-warranty.md`, `complaints.md`, `not-offered.md`, `site-pages.md` | 1 to 2 pages each | One per wake, chosen by Jesse's first JSON field or by keyword |

`CORE.md` holds only the never-break rules: Nick, Sales Manager; call (310) 513-8800, text (213) 429-1092; "payment plan" never "financing"; no emojis; no labor or install price; no warranty length; hours; never promise "Nick will call you"; no rides; no California law; one link max, none on Yelp; hand-off triggers; scam rules; output format.

### 4.3 Lead store (one row per customer)

`id, phone (E.164, unique), name, channel, car_year, car_make, car_model, want, stage, last_in_at, last_out_at, who_sent_last, replies_today, followups_sent, next_action, next_action_at, human_owner, do_not_contact, booked_at, bought, review_asked, notes`

Stages (borrowed from the SalesGPT stage idea, not its code): `new, qualifying, quoted, objection, booked, confirmed, done, quiet, dead, human`.

A Google Sheet is fine at this size and Zack can read it. If it moves to AMS-1, use SQLite with the Sheet as a one-way mirror.

### 4.4 Model settings

- Model: top Grok model for customer replies. At this volume the gap to the cheapest model is about 40 cents a day; one extra tint job pays for a year of it.
- API: OpenAI-compatible, base address `https://api.x.ai/v1`.
- Caching: automatic and prefix-based. Keep `CORE.md` + `INDEX.md` first and identical every call; send the same conversation header (`x-grok-conv-id`) so calls land on the same cache. Log `cached_tokens` from the usage block to prove it works.
- Turn off web search and reasoning modes for normal replies. Web search costs about $5 per 1,000 calls on top of tokens; keep it for the parts look-up only.
- Cap output at 250 tokens for texts, 450 for Yelp and email.
- Ask for JSON output so a bad reply never needs a second call.
- Images (dash photos) bill as normal tokens. Accuracy at naming a factory radio from a photo is UNPROVEN: test on 30 real shop photos and treat the answer as a note for Nick, never as a quote.

### 4.5 Jesse's output (strict JSON)

```
{
  "topic": "tint",
  "stage": "quoted",
  "reply": "text to send, or empty",
  "link": "one URL or empty",
  "handoff": "none | nick | zack | carlos",
  "handoff_reason": "",
  "book": {"date": "", "time": ""},
  "lead_update": {"name": "", "car_year": "", "car_make": "", "car_model": "", "want": ""},
  "followup_at": ""
}
```

### 4.6 Send gate (plain code, no AI)

Block and log if any is true: banned word ("financing", a warranty length, "lifetime", the wrong phone number, an emoji); a dollar amount that is not in the price file; a labor or hourly price; more than one link, or any link on Yelp; outside 8 AM to 9 PM Pacific; it is the customer's turn and we already sent last; customer is `human`, `dead` or do-not-contact; more than 6 replies to this customer today; daily spend over the cap; a booking time outside Tue to Fri 9:30 to 10:15 unless the customer asked.

Never confirm a time in writing on Marketplace or OfferUp (existing rule).

### 4.7 Spend cap, two layers

1. xAI console: prepaid credits only, invoiced limit left at $0, auto top-up off. When credit runs out, calls are refused. That is a hard stop.
2. In the script: add up cost from each call's usage block. At $2 text Zack. At $3 stop calling Grok for the day and send the fixed auto-reply instead.

### 4.8 Jobs that use no AI

- 9:00 AM, 12:30 PM and 6:00 PM texts to Zack and Nick: read Calendar and the lead store, format, send. Never repeat a number (a `sent_in_brief` flag on the row).
- Noon-the-day-before reminder and an 8 AM morning-of reminder.
- Review ask at noon the day after `bought`.
- Follow-up scheduler: sets `next_action_at`; Jesse writes the words only when it fires.
- Contact naming "John Honda" through the People API (create in My Contacts, number in E.164, match on number).
- Missed-call text-back, once a texting number exists.

### 4.9 Booking

Use the Calendar API: check free/busy, then insert. Overbooking mornings is allowed by Zack, so "busy" is not a block. Zero-code option: a Google Calendar appointment schedule page gives a booking link that writes to the same calendar and emails a confirmation; automatic reminders need Business Standard or higher, and it has no text reminders.

### 4.10 Daily handoff

At 6:15 PM one cheap call writes `handoff/tomorrow.md` from the lead store: open leads with next step, booked today and tomorrow, promises owed, waiting on Zack or Nick, what failed. One page. A copy goes to the Drive folder "Jesse Handoffs".

### 4.11 Proof before "it works" (acceptance tests for Duet)

1. Ten past real leads replayed with sending off: show Zack each reply and the JSON.
2. Send gate unit tests: every block rule above has a failing example.
3. A test text from Zack's phone answered in under 5 minutes, with the Gmail alert as the screenshot.
4. A day of logs showing wakes, tokens in, cached tokens, dollars.
5. The 9 AM text arriving with real calendar data.
6. The cap test: set the cap to $0.01 and show Jesse stops and the fixed reply goes out.

## 5. The website as Jesse's brochure

### How to use it

1. Prices come from `/prices/` only. Copy it into the topic files and re-check weekly.
2. One link, at one of three moments: after stating a published price; when the customer is choosing (shade, alarm); or once on a quiet quote as proof.
3. No link on Yelp. No link in a first Marketplace message.
4. Car page first when the customer named the car. There are 1,302 car year pages and 208 model pages.
5. The 22 project pages are the only real-job proof. Use them.

### Which page for which lead

| Lead says | Send |
|---|---|
| Tint | `/tint/` (shade simulator) |
| "How much is tint" | `/tint/prices/` |
| Windshield | `/tint/windshield/` |
| Tesla | `/tesla/` or `/tesla/model-y/`, `/tesla/model-3/`, `/tesla/model-x/` |
| CarPlay | `/stereo/carplay/` or `/stereo/carplay/toyota/`, `lexus`, `mercedes-benz`, `porsche` |
| "Will it fit" | `/radio-finder/` or `/vehicles/{make}/{model}/{years}/` |
| Backup camera | `/stereo/backup-camera/` |
| Subs | `/beats/subwoofers/` |
| Trucks | `/beats/trucks/` |
| Speakers | `/beats/speakers/` |
| Alarm | `/alarm/` |
| Alarm, named car | `/alarm/dodge-charger/`, `ford-f-150`, `chevy-silverado`, `chevy-camaro`, `honda`, `toyota`, `hyundai-kia` |
| Remote start | `/alarm/remote-start/` |
| Dash cam | `/alarm/dash-cam/` |
| GPS tracker | `/alarm/gps-tracker/` |
| Harley | `/amspods/` |
| Payments | `/payment-plan/` |
| Book | `/book/` |
| "Are you legit" | `/reviews/` |
| "Done my car?" | A matching `/projects/...` page |
| "How far" | The city page, for example `/torrance/` |
| Spanish | The `/es/` twin, hand to Carlos |

### Most likely to close (judgement, no data)

`/tint/`, `/alarm/`, `/payment-plan/`, `/alarm/dash-cam/`, `/beats/subwoofers/`, `/tesla/`. Stereo pages close worse because no number can be shown; Jesse makes up for it with a photo and a fast call.

### Published product prices Jesse may quote (from the shop pages)

| Product | Range on the site | Cheapest |
|---|---|---|
| CarPlay double-DIN radios (15) | $189 to $999 | BOSS BE7ACP $189; Kenwood DMX4710S $319 |
| Floating-screen radios (11) | $498 to $1,549 | Sony XAV-AX8100 $498 |
| Factory-screen retrofit kits (92) | $469 to $1,899 | |
| Bluetooth radios (4) | $119 to $219 | JVC KD-X280BT $119 |
| Coaxial speakers (40) | $50 to $389 | |
| Component speakers (19) | $179 to $2,550 | |
| Subwoofers (76) | $99 to $1,799 | |
| Loaded sub boxes (37) | $169 to $1,499 | |
| Mono amps (21) | $199 to $1,000 | |
| Backup cameras (2) | $119, $269 | |
| Dash cams (4) | $119 to $370 | |

### Pages Jesse needs that do not exist (list only)

1. Black Friday page. The site never says "Black Friday".
2. Photo gallery of finished jobs.
3. Tint shades on real cars, by percent.
4. Alarm plus dash cam bundle ($488).
5. ZZ2 Mercedes screen deal ($1,400).
6. "Leave us a review" page with the Google link.
7. "What to expect": job times, waiting room, drop-off.
8. Text message terms page and a privacy line that phone numbers are never shared. Required for a business texting number.
9. BMW and Mercedes-Benz make pages (the host redirects those addresses).
10. Remote start pages for Nissan, Jeep, Ram, GMC, Lexus.
11. A simple quote form that asks for a dash photo.

## 6. Where the site, the Bible and the old Jessie skills disagree

Rule: the higher price wins.

| Item | Bible or old files | Live site | Jesse says |
|---|---|---|---|
| Dash cam | $189 | $249 sedan, $299 SUV or truck | $249 / $299 |
| Remote start | $549 to $1,199 | From $649; Viper with remote start from $799; 5908V + VSM550 $1,199; Compustar T13 $1,499 | Never $549 |
| Solar Ceramic sedan | $329 (old) | $429 | $429 |
| Front two windows | $149 (old, Black Friday) | $190 Solar, $229 Solar Ceramic, $299 3M | Site prices. "$149" matches nothing; Zack decides |
| Solar tint | "starting at $249 most vehicles" (old skill) | $349, or $249 with the booking discount | $349, $249 Tue to Fri |
| CarPlay labor | $250, $200 Black Friday, or never | $250 shown today | Never quoted |
| Sub and amp install | n/a | "$199 installed" and "Labor $249" | Only the $199 installed Kicker package |
| Diagnostics | "$99 to $199" (old skill) | Not on the site | Zack decides; today it is a labor price |
| Discount days | Tue to Fri | No days named | Zack decides |
| Yelp line | "for 10 years" | "since 2016" | "Yelp award winner since 2016" |
| Title | "Nick, Shop Manager" (old skill) | Sales Manager | Sales Manager |
| Spanish | "signed Albert" (old skill) | Carlos | Carlos |
| Payment plan providers | Koalafi, then Snap | Four listed | Koalafi, then Snap |
| Shipping | "No shipping" (old), "after the deal" (new) | "Yes, we ship" until the branch deploys | "Shipping is available after you call or text us and we make the deal." |
| DSP | "No DSP" (old skill) | A DSP is sold in the shop ($899) | Zack decides |
| Tint simulator link | lacartint.com, teslatintla.com (old skill) | `/tint/`, `/tesla/` | The main site |
| Appointment times | "Never offer times" (old skill) | n/a | Nov 7 rule: two morning times |
| Review ask | Google and Yelp links (old skill) | n/a | Google only, every customer |
| Front tint | "70%" | The 88% rule on 650 pages | Jesse does not raise the law |
| ZZ2 deal | "3-year warranty" | Warranty stays vague | Drop the length |

Black Friday check: four of the five bundles are the normal sale math and need no new prices. Full Tint $249 = $349 minus $100. Ceramic + Windshield $518 = $429 + $239 minus $150. 3M $798 = $549 + $399 minus $150. Alarm + Dash Cam $488 = $289 + $249 minus $50.

## 7. Sales playbook for the topic files

What is proven and what is convention is marked. Nothing here is specific to car audio in any study; the trade advice comes from tint and auto-repair sources.

1. **Speed (proven direction).** Minutes, not hours. Being first matters.
2. **Sell the visit, not the price (trade advice: Tint World, Ratchet+Wrench).** Ask about the car and the need before any number. Capture name and number on every price question.
3. **Opening text (convention).** Opener, one fact about their car, one question. One question per message. Every message ends in a question or a choice.
4. **Qualify in two messages.** Year, make, model, what they want. Then a photo for stereo jobs. A VIN works too: the free government decoder returns year, make, model and trim.
5. **"How much".** Published price: say it first, then the Tue to Fri discount, then two morning times. Stereo: give the radio's own price from the shop pages, say the full number comes from one dash photo, ask for the photo.
6. **"Too expensive" (framework, unproven but standard).** Acknowledge. Ask one question (what did the other quote include?). Offer the lower tier at its real price. Mention the payment plan once. Never discount in chat.
7. **"Cheaper?"** Hold the price. The only lever is the real booking discount. On Marketplace, a light joke first.
8. **"I'll think about it".** "Is it the price or the timing?" Then one follow-up next shop morning.
9. **Good, better, best (some evidence).** Show the top option first; one experiment found that raised revenue by up to 10%. For tint: 3M Ceramic IR, then Solar Ceramic, then Solar.
10. **Payment plan.** Once, in the middle, as an option, when price comes up. Offer to text the application. Never in the opener.
    - Never say: "no credit check", "guaranteed approval", "0% interest", "same as cash", "builds your credit". Never quote a payment amount. Regulators have fined lease-to-own companies over exactly these phrases.
    - Koalafi and Snap are lease-to-own. If asked, say so and let the application show the terms.
    - Snap's merchant portal has a "Text Application" button and Koalafi supports apply-by-text and QR. Use the merchant apply link in messages.
11. **Close.** Two morning times, "which one is yours?" Same-day drive-out matters more than the discount.
12. **Follow-ups (vendor data).** Three nudges, then stop: next morning, day 3, day 7. Each must add something: a question, a real job on their car, the discount ending Friday.
13. **No-shows (reminders proven in other fields).** Noon the day before, 8 AM the day of, one text 30 minutes after a miss.
14. **Upsell (trade advice).** One add-on, once, after the yes: radio + backup camera; tint + windshield overnight; alarm + remote start; alarm + dash cam ($488); subs + speakers; Tesla tint + roof.
15. **Reviews.** Every customer, once, Google link only, noon the day after. No reward. Never Yelp.
16. **Texting rules (not legal advice).**
    - A lead who wrote first can be answered about that request. That is not permission for marketing later.
    - Honor STOP or any plain "stop texting me" at once and set do-not-contact.
    - No texts before 8 AM or after 9 PM.
    - Recorded calls: California needs everyone's consent. Announce the recording at the start of every call, in English and Spanish.
    - A verbal "yes, text me" on a call: log it, and make the first text name the shop and end with "Reply STOP to opt out."

### 10 example replies (EXAMPLES for Zack to approve, not final)

1. **New tint lead, text.** "Hi Maria, Nick here from Audio MotorSports, thanks for reaching out! That Camry is gonna look clean tinted. Solar tint is $349 but book Tuesday through Friday and it's $249, nothing upfront. What year is it?"
2. **"How much for CarPlay in my 2015 Tacoma", text.** "Good truck for it, those Tacomas take a CarPlay screen real nice and you keep your steering wheel buttons. CarPlay screens start at $189 for the radio itself and I'll get you the full number off one picture, can you send me a photo of your dash right here?"
3. **"That's too expensive".** "I hear you, nobody likes spending money on their car till they see it done. What did the other shop quote you, was that ceramic or regular film? We also have a payment plan if you'd rather split it up."
4. **Marketplace, "can you do $150?"** "Ha, I wish, my boss would have me tinting cars in the parking lot. It's the price on the listing and that's already the deal, we have it in stock, come on in. What are you putting it in?"
5. **"I'll think about it".** "Totally, no rush. Is it more the price or finding a day that works? Either one I can probably help with."
6. **Quote went quiet, next morning.** "Morning Mike, still got your Charger on my list for that alarm. I have Tuesday 9:30 or Wednesday 10 open, which one is yours?"
7. **Morning-of reminder.** "Morning Jessica, see you at 9:30 for the tint on the Model Y. We're at 22025 S Avalon, reply here if you're running behind."
8. **Upsell after a yes on tint.** "You're locked in for Tuesday 9:30. One thing, if you leave it with us overnight and add the windshield it's $150 off the whole package and the car stays way cooler. Want me to add it?"
9. **Yelp lead, alarm for a Charger, no links.** "Hi David, Nick here from Audio MotorSports, thanks for reaching out! Let's get that Charger protected the right way. Our alarm pricing is on our website and it's $50 off when you book Tuesday through Friday, nothing upfront, and we have a payment plan if you need it. Stop by, call (310) 513-8800, or text me a couple pictures at (213) 429-1092 and I'll build you the right package. I can do Tuesday 9:30 AM or Wednesday 10 AM. Which one is yours?"
10. **Review ask, day after, sent to every customer.** "Hey Chris, Nick from Audio MotorSports, thanks for coming in yesterday. How's the new screen treating you? If you have a minute, a Google review would mean a lot to the family: [Google review link]"

## 8. Cost

Grok prices per million tokens, from third-party trackers (verify on xAI's pricing page): top model about $2.00 in, $0.50 cached, $6.00 out. Mid model about $1.25, $0.20, $2.50.

| | Assumption | Per day |
|---|---|---|
| Before: awake, checking 6 platforms | About 400 checks, about 20,000 tokens each. Cannot be checked from here; read the real number off the xAI console. | About $16, or about $4 if caching worked |
| After | 20 to 30 wakes, about 8,000 tokens in (half cached) and 250 out, plus one handoff | **About $0.40 to $0.60** |

Hosting: $0 on Apps Script. Texting number: about $2 to $5 a month plus about a cent per text.

One caution: xAI has offered free monthly credits in exchange for sharing API data. Sources disagree on whether it is still offered, opting in cannot be undone, and it would share customer conversations. Recommended: do not opt in.

## 9. Hidden gems, top 15

| # | Gem | What it does | Why it pays | Effort | Caveat |
|---|---|---|---|---|---|
| 1 | Google Apps Script as the watcher | Free script in Google's cloud that reads Gmail on a timer, calls Grok, replies, and writes Calendar, Sheets and Contacts | Takes AMS-1 and the browser out of the main path. $0. | Medium | Timer only, 1 minute minimum; keep runs short |
| 2 | Google Voice email toggles | Texts, missed calls and voicemail transcripts all arrive as email | Missed calls become leads; this is the feature shops pay Podium for | Easy | Sending back by email is UNVERIFIED |
| 3 | xAI prepaid-only billing | Invoiced limit $0, auto top-up off | A hard daily and monthly cap with no code | Easy | Load small amounts |
| 4 | Grok prompt caching | Identical opening text billed about 75% off | Cuts the biggest part of each call | Easy | Only if the opening never changes |
| 5 | Snap "Text Application" and Koalafi text or QR apply | Sends the application to the customer's phone from the merchant portal | Removes the price objection in one tap | Easy | Do not advertise the short code on the site; no way for a bot to read approvals |
| 6 | NHTSA VIN decoder | Free year, make, model, trim from a VIN | Ends the back-and-forth on what car it is | Easy | Does not know the factory sound package; still ask for a photo |
| 7 | Google Calendar appointment schedule | A booking link that writes to the shop calendar and emails a confirmation | No booking code to maintain | Easy | Reminders need Business Standard; no text reminders |
| 8 | Agent Skills file layout | Core file plus topic files loaded on demand | The whole "small reads" plan, with no library | Easy | Duet's script does the loading |
| 9 | Meta Business Suite automations | Free instant reply, away message and FAQ on the Page inbox and Instagram | A first answer in seconds with no code | Easy | Personal-profile Marketplace chats are not covered. Meta also launched its own AI auto-reply for Marketplace sellers in March 2026; worth trying before any bot |
| 10 | Telnyx texting number | Real business texting with replies delivered to a script | The only clean way to text first, text Yelp leads, and do missed-call text-back | Medium | Registration about $20 to $25, a few dollars a month, 1 to 7 business days, and needs the text terms page first. A Google Voice number can be moved to it |
| 11 | The shop's own fit list | Each time a person confirms what fits a car, save it | No fit data feed exists from Crutchfield, Metra or anyone. The site's 1,302 car pages already hold verified radio type and speaker sizes | Easy | Jesse never states a fit that is not in the list |
| 12 | faster-whisper | Call recordings to text on a normal PC, several times faster than real time, good Spanish | Free transcripts for the "text me" follow-up | Medium | Untested on phone-quality audio; try 10 real calls. If each caller is on its own channel, no speaker-splitting tool is needed |
| 13 | Google review link and QR | One short link to the review box, from the Business Profile | Reviews bring map leads | Easy | Ask everyone, no reward |
| 14 | Yelp Leads through Zapier | New-lead and new-message triggers plus a reply action | A supported way to answer Yelp without a browser | Medium | Monthly fee per task; connecting two tools at once can break the link. Yelp's own Smart Lead Reply is reported at about $30 a month; whether auto shops qualify is unconfirmed |
| 15 | People API | Creates and renames contacts | "John Honda" on Nick's phone | Medium | Test one contact end to end first |

### Skip these

1. LangChain, CrewAI, AutoGen: layers of framework for one bot.
2. n8n self-hosted: several critical security holes in 2026, constant patching.
3. Vector databases and memory products (mem0, Letta): the Bible is a few dozen pages.
4. Browser bots for Google Voice, Yelp, Marketplace, OfferUp: against their rules and the reason the last build broke.
5. Scraping Crutchfield or Metra: against their terms, and confidently wrong fit answers lose money.
6. Podium, Birdeye and similar: about $300 a month for a missed-call text and a review link.
7. RCS and Apple Messages for Business: paperwork and per-message cost for no gain at this size.
8. Gmail push through Pub/Sub: more parts than a 2-minute poll for the same result.
9. Full sales-bot frameworks (SalesGPT): take the stage list, leave the code.

## 10. What Jesse cannot do yet, plainly

- Text a number that never texted the shop (needs the texting number).
- Answer Marketplace or OfferUp by himself in any supported way.
- Post listings at night without risking the accounts.
- Read call recordings (no recording feed exists yet).
- Tell what fits a car beyond the site's verified table.

## Sources

- Lead speed: [HBR 2011](https://hbr.org/2011/03/the-short-life-of-online-sales-leads); follow-up decay: [Meera 2025](https://www.meera.ai/blogs/sms-marketing-benchmarks-2025)
- Trade sales advice: [Tint World](https://www.tintworld.com/franchise-opportunities/much-yes-no-brief-guide-sales-telephone-etiquette), [Ratchet+Wrench](https://www.ratchetandwrench.com/articles/1489-how-to-handle-the-price-shopper-phone-call)
- Tier order: [INSEAD](https://knowledge.insead.edu/marketing/small-change-big-rewards); good-better-best: [HBR 2018](https://hbr.org/2018/09/the-good-better-best-approach-to-pricing)
- Payment plan cautions: [FTC, Progressive Leasing](https://www.ftc.gov/business-guidance/blog/2020/04/when-price-wrong-175-million-ftc-settlement-progressive-leasing-shows-why-cost-clarity-key); pay-over-time lift: [Stripe](https://stripe.com/en-bg/blog/testing-the-impact-of-buy-now-pay-later)
- Reminders: [meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3419880/)
- Reviews: [Google policy](https://support.google.com/contributionpolicy/answer/7400114), [Yelp solicitation](https://searchengineland.com/yelp-increasingly-cracking-review-solicitation-across-internet-286290)
- Texting and recording: [opt-out rule](https://www.bclplaw.com/print/v2/content/1557107/the-tcpas-new-opt-out-rules-take-effect-on-april-11-2025-what-does-this-mean-for-businesses.pdf), [California recording](https://www.rcfp.org/reporters-recording-guide/california/)
- Grok: [pricing tracker](https://www.benchlm.ai/xai/api-pricing), [xAI pricing](https://docs.x.ai/developers/pricing), [caching](https://docs.x.ai/developers/advanced-api-usage/prompt-caching/maximizing-cache-hits), [billing](https://docs.x.ai/console/billing)
- Google: [Apps Script quotas](https://developers.google.com/apps-script/guides/services/quotas), [Voice email settings](https://support.google.com/voice/answer/9182115), [Gmail push](https://developers.google.com/workspace/gmail/api/guides/push), [appointment schedules](https://support.google.com/calendar/answer/11608416), [IMAPClient notes](https://imapclient.readthedocs.io/en/master/advanced.html)
- Yelp: [Leads API](https://docs.developer.yelp.com/docs/leads-api), [Zapier app](https://zapier.com/apps/yelp-leads/integrations)
- Meta: [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/overview), [Marketplace AI replies](https://techcrunch.com/2026/03/12/facebook-marketplace-now-lets-meta-ai-respond-to-buyers-messages)
- Telnyx: [10DLC fees](https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges), [sole proprietor guide](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration), [porting Google Voice](https://support.telnyx.com/en/articles/2042439-port-your-google-voice-skype-numbers)
- Payment plan tools: [Snap merchant guide](https://snapfinance.com/business-blogs/new-snap-finance-merchant-here-s-what-to-expect-before-your-first-transaction), [Koalafi](https://koalafi.com/how-it-works-for-business)
- VIN decoder: [NHTSA vPIC](https://vpic.nhtsa.dot.gov/api/)
- Skills and repos: [agentskills.io](https://agentskills.io), [Sales-Skills](https://github.com/louisblythe/Sales-Skills), [SalesGPT](https://github.com/filip-michalsky/SalesGPT), [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
