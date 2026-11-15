# Super Jesse v4 Report

PUT IT IN CLAUDE DUET

This replaces "Super Jesse v3: Research Results and Build Spec". Research and writing only: nothing was changed, restarted, sent, posted, signed in to or bought.

## Prompt for Claude Duet (paste this with the Doc link)

Read this whole Doc before you plan anything. It is the research for Super Jesse and the build spec. Your job is to finalize the build plan from it, not to start building.

1. Do not change code, restart anything, send any customer message, post, sign in anywhere or buy anything until Zack types GO.
2. First, give Zack the list in section 2 as plain yes/no questions, one line each, and wait for his answers.
3. Ask Zack or Nick to run the hand tests in section 3 and report pass or fail. Do not design around anything marked UNVERIFIED until its test passes.
4. Then write the build plan in the order in section 4.0, using section 4 as the spec. For each step say what gets built, where it runs, what it costs, and what proof Zack will see (section 4.13).
5. Draft `CORE.md`, `INDEX.md` and the topic files from the AMS Bible using the split in section 4.2 and the ten drafts in section 12. Settle every conflict in section 6 with Zack's answers. Where sources disagree on a price, the higher price wins.
6. Jesse is sales chat only. Anything that needs code goes to Claude Code as a task. The two website tasks in section 13 go to the website coding agent.
7. Standing rules stay as written in the AMS Bible: call (310) 513-8800, text (213) 429-1092, "payment plan", no labor or install prices, warranty stays vague, Nick is Sales Manager, Zack is Operational Manager, nothing sent without GO, no secrets in chat or Docs.
8. Show Zack the 10 example replies in section 7 and get each one approved, changed or cut before any goes into a topic file.

Report back in plain words, short: what is decided, what is waiting on Zack, and what you will build first.

## What changed from v3

1. **Fix 1.** "Are you real or a bot?" now stops Jesse cold: no reply, lead marked human, Nick and Zack alerted. Trigger list, gate rule, alert text and CORE line are in 4.7. A heads-up on California's bot law is in section 2.
2. **Fix 2.** How Jesse alerts Nick before a texting number exists: a push app (Pushover) with a labeled Gmail email as backup (4.8). The texting number registration moves to build step 1.
3. **Fix 3.** Stereo Specialist rewritten Zack's way: one car at a time on Crutchfield and Metra, look up only, parts list to Nick and Zack, website link to the customer (4.11). One risk on Crutchfield's terms is flagged for Zack.
4. **Fix 4.** Missed-call text-back moves to right after the texting number. The exact text is in 4.9.
5. **Fix 5.** The "before" cost is no longer a guess: steps to read the real number off the xAI console and a table to fill in (section 8).
6. **Fix 6.** Power saving goes deeper: 17 places to skip, shrink or batch an AI call, each with dollars saved and sales risk, and a ranked top 10 (section 11).
7. **Fix 7.** Ten more sales skills, each written as a short topic file draft (section 12).
8. **Fix 8.** Every fact in the 10 example replies checked against the live site. Two replies changed (section 7).
9. **Fix 9.** Zack's full list checked line by line against the plan (section 10).

## 0. Read this first

- **Where it ran.** A Claude Code cloud session on Fable 5.2, not on AMS-1. AMS-1, Jesse's past chats and the xAI bill were not visible.
- **What was read.** All 4,139 pages of the live audiomotorsports.com (copy of Nov 13), the Nov 15 checklist, the Nov 7 core reply style, the 54 old Jessie skills, and the Nov 9 and Nov 14 machine prompts.
- **Web research limit.** The official pages of California's legislature, the FTC, Google, xAI, Yelp, Telnyx, Crutchfield, Metra and Pushover were all blocked from this session. Facts about them come from search extracts, law-firm summaries and third-party pages. Every item marked UNVERIFIED must be checked by a person before anyone builds on it.
- **No analytics.** "Which pages close" is judgement.
- **Not legal advice.** The bot law, texting, recording and payment plan notes are practical heads-ups with sources. A California business lawyer can settle them in one short call.

## 1. Verdict

**Sell the most**
1. Answer in minutes, not 35. The best study (Harvard Business Review 2011, 1.25 million leads) found contact within an hour about 7 times likelier to qualify a lead than an hour later.
2. Missed-call text-back. Every missed call gets a text inside a minute. It is the feature shops pay $300 a month for, and it needs only the texting number.
3. Follow-ups back on, capped at three, plus one revival question on quiet leads.

**Cut the most cost**
1. No AI in the watcher. Jesse wakes only when a real message lands.
2. A hard spend cap and a daily wake cap, so a loop can never run up a bill.
3. Canned first replies and plain-code handling for junk, "ok", "thanks", STOP, reminders and the daily texts.

**Honest note on cost:** after the first item the AI bill is already about 50 cents a day. Everything else in section 11 adds up to under 50 cents a day more. Do those for speed and steady answers, not for the money.

## 2. Decisions Zack makes before Duet builds

1. **Bot disclosure (heads-up, UNVERIFIED, not legal advice).** California's bot law (Business and Professions Code 17940 to 17943) makes it unlawful to use a bot to talk to a person in California online, intending to mislead them about being artificial, in order to make a sale. The only safe harbor is a clear statement that it is a bot.
   - **What the hand-off rule does:** it stops Jesse from ever lying to someone who asks.
   - **What it does not do:** cover the customers who never ask. They still get "Nick here" messages written by software and aimed at a sale, with nothing disclosed.
   - **What is left to argue:** that honest prices are not "deception about the content". That is untested.
   - **Realistic exposure:** a prosecutor or a demand letter (reported at up to $2,500 per violation) and platform action. Meta's Messenger rules separately require telling users about automated replies and name California. Whether the law reaches plain texts and email is unsettled; Yelp and Marketplace chat fit it better.
   - **Three setups, lowest risk first:**
     - A. One line in the first message only: "Hi Maria, this is Audio MotorSports' automated assistant, working with Nick, our Sales Manager." Then the normal voice. Risk left: close to none.
     - B. "Hi Maria, Nick's team at Audio MotorSports here (replies are AI-assisted)." Risk left: the note may not count as clear enough.
     - C. Keep "Nick here", and Nick taps approve on every message before it sends. Risk left: low while a person approves each one; gone the moment messages send themselves.
   - Zack picks. Nothing in this Doc changes the opener on its own.
2. **Crutchfield look-ups by Jesse.** Zack wants them, and section 4.11 is written that way. One flag: Crutchfield's terms reportedly ban any "manual or automated device, tool, or process designed to mine data or scrape material", bar using its data for software or AI, and claim the fit data as its own property (UNVERIFIED; the page could not be opened from here). If it reads that way, an AI look-up on Zack's account breaks the terms even one car at a time, and the account carries the risk. Choices: (a) Jesse does it anyway, one car at a time; (b) a person does the 30-second Crutchfield check and Jesse does Metra and the rest; (c) Zack asks Crutchfield in writing. Recommended: (b) until Zack has read the terms page himself.
3. **Where the watcher lives.** Recommended: Google Apps Script in the shop's Google account. It runs in Google's cloud for free, so AMS-1, Chrome tabs and sign-outs stop mattering for texts-in, Yelp, website forms, voicemail and missed calls.
4. **How Jesse sends texts.** Google Voice has no API and its policy bans sending "through an automated process, such as a script". The supported answer is a registered business texting number. Registration starts on day 1 because it takes 1 to 7 business days.
5. **Marketplace and OfferUp.** No supported way exists to read or answer those chats by program. Recommended: Jesse drafts, a person pastes. Night auto-posting risks the accounts.
6. **Discount days.** The Bible says Tuesday to Friday only. The site says "book online and save" with no days. Pick one.
7. **Review ask.** Ask every customer once, Google link only. Never Yelp. The old skill that sends both links should be retired.
8. **The price conflicts in section 6.**

## 3. Hand tests to run first (a person does them)

| # | Test | If it passes | If it fails |
|---|---|---|---|
| 1 | Read Jesse's real cost (steps in section 8). | The before-and-after table has a real number. | If nothing shows in the xAI console, Jesse ran on a flat-fee Grok subscription, and "cost" means something else. |
| 2 | In Gmail, reply to one forwarded Google Voice text. Does the customer get it as a text? UNVERIFIED for 2026. | Jesse can answer existing threads by email until the texting number is live. Keep the volume low given Google's policy. | Texts out wait for the texting number. |
| 3 | Reply by email to a Yelp lead, then to the customer's second message. | Yelp answers need no browser. | Use Yelp's own app for later replies, or the Zapier "Yelp Leads" app. |
| 4 | In Google Voice settings, turn on: forward texts to email, missed-call email alerts, voicemail by email. Call the shop and hang up. | Missed calls and voicemails become leads. | Nothing lost. |
| 5 | Install Pushover on Nick's and Zack's phones and send one test alert. | Lead alerts work today. | Use the Gmail label alert alone. |

## 4. Build spec

### 4.0 Build order

1. **Day 1, in parallel:** the website text terms page (section 13, task A), then submit the texting number registration. It waits on carriers for 1 to 7 business days while everything else is built.
2. Hand tests (section 3).
3. Lead store (4.3).
4. Watcher with no AI, the pre-filter, the bot-question rule and the alert to Nick (4.1, 4.6, 4.7, 4.8).
5. `CORE.md`, `INDEX.md`, topic files and the canned first replies (4.2, 4.5).
6. The Grok call, the send gate and both caps (4.4, 4.6, 4.10).
7. Texting number goes live: Jesse sends texts.
8. **Missed-call text-back** (4.9).
9. Yelp leads with a phone number get a text.
10. Booking, reminders and the three daily texts (4.12).
11. Follow-ups and the review ask.
12. Stereo Specialist look-up (4.11).
13. Contact names and the daily handoff Doc.
14. Call recordings, last. No recording feed exists yet.

### 4.1 Shape

```
Gmail (Google Voice texts, missed calls, voicemail transcripts,
       Yelp leads, website forms)
        |
   Watcher on a 2-minute timer, NO AI
        |   pre-filter (4.6): junk, tapbacks, STOP, bot question,
        |   "ok" / "thanks", our own alerts
        |   group one customer's messages inside 3 minutes
        v
   Lead store: one row per customer  --->  alert Nick (4.8)
        |
   Canned first reply by script when the message is simple (4.5)
        |   otherwise
   ONE Grok call: CORE + INDEX + handoff + ONE topic file
                  + the customer's row + last 6 messages
        v
   Send gate (plain code)
        |
   Send, or queue for a person. Update the row. Log cost.
```

Recommended home: Google Apps Script. Limits on a Workspace account: 6 hours of trigger runtime a day, 6 minutes per run, 100,000 outside calls a day. A 2-minute timer that exits fast uses a few minutes a day.

Fallback on AMS-1: about 200 lines of Python under systemd, polling Gmail every 60 seconds. Same shape.

### 4.2 Files Jesse reads

| File | Size | Loaded |
|---|---|---|
| `CORE.md` | 1 page, about 600 words | Every call, always first, never edited mid-day |
| `INDEX.md` | Half a page: topic name plus one line each | Every call |
| `handoff/YYYY-MM-DD.md` | Half a page | Every call |
| `topics/*.md` (tint, tesla, stereo-carplay, alarm-remote-start, dash-cam, subs-speakers, harley, payment-plan, sales-and-black-friday, booking, objections, follow-ups, reviews, yelp, marketplace-offerup, spanish, shipping-warranty, complaints, not-offered, site-pages, plus the ten in section 12) | Half a page to 1 page each | One per call |

v3 said 2 pages for `CORE.md`. One page is enough and halves the fixed cost of every call.

### 4.3 Lead store (one row per customer)

`id, phone (E.164, unique), name, channel, language, car_year, car_make, car_model, car_trim, factory_system, want, stage, last_in_at, last_out_at, who_sent_last, replies_today, followups_sent, next_action, next_action_at, human_owner, human_reason, do_not_contact, text_consent, booked_at, bought, review_asked, sent_in_brief, summary, notes`

Stages: `new, qualifying, quoted, objection, booked, confirmed, done, quiet, dead, human`.

`summary` is two lines Jesse rewrites each call. It replaces long chat history.

### 4.4 Model settings

- Customer replies at stage `quoted`, `objection` or `booked`: the top Grok model.
- Qualifying questions and the daily handoff: the mid model.
- Sorting and look-ups: no model.
- API is OpenAI-compatible at `https://api.x.ai/v1`.
- Caching: keep `CORE.md` + `INDEX.md` first and identical every call; send the same `x-grok-conv-id` header. Log `cached_tokens` to prove it works.
- Web search off. Reasoning mode off. Output cap 200 tokens for texts, 400 for Yelp and email. JSON output.
- Dash photos bill as normal tokens. Accuracy is UNPROVEN: test on 30 real shop photos.

### 4.5 Canned first replies (script fills them, no AI call)

When a first message is simple (it names a service, asks a price that is in the price file, or is a bare "how much"), the script fills an approved template with the name, car and price. The three approved text templates from the Nov 7 Doc are the starting set. Anything with a second question, a complaint, a photo, Spanish, or a car the script cannot read goes to Grok.

Each canned reply still passes the send gate. Each needs Zack's approval before it goes in.

### 4.6 Pre-filter and send gate (plain code)

**Pre-filter, before any AI call. If a rule matches, no Grok call is made.**

| Inbound | Action |
|---|---|
| Our own machine alerts, dealer "car offer" mail, spam | Label, skip |
| Tapback or emoji only | Skip |
| STOP, "stop texting", "unsubscribe", "no me escriban" | Set do-not-contact, send nothing |
| Bot question (4.7) | Set human, alert, send nothing |
| "ok", "thanks", "gracias", "sounds good" when we did NOT just ask a question | Skip, no reply |
| "1" or "2" after a booking confirmation | Script confirms or reschedules |
| A day or time that matches the two slots Jesse offered | Script books, sends the confirmation |
| Customer is `human`, `dead` or do-not-contact | Skip |

**Send gate, before any message leaves.** Block and log if: a banned word ("financing", a warranty length, "lifetime", the wrong phone number, an emoji); any claim to be a person or a bot; a dollar amount not in the price file; a labor or hourly price; more than one link, or any link on Yelp; outside 8 AM to 9 PM Pacific; we already sent last; more than 6 replies to this customer today; the daily cap is hit; a banned payment-plan phrase ("no credit check", "guaranteed approval", "0% interest", "same as cash").

### 4.7 "Are you real or a bot?" (Zack's rule)

**Rule.** When anyone asks if Jesse is real, a person, a bot, AI or automated, Jesse sends nothing. The lead is marked `human`, Nick and Zack are alerted at once, and a person takes over. Jesse never says he is a bot and never says he is a person.

**Trigger list (case-insensitive, checked by the pre-filter).**

English:
- "is this a bot", "are you a bot", "r u a bot", "bot?"
- "is this a real person", "am I talking to a real person", "are you a real person", "are you real", "is this real"
- "is this a person", "are you human", "is this a human", "real human"
- "is this AI", "are you AI", "is this an AI", "chatgpt", "grok"
- "is this automated", "automated message", "auto reply", "is this a robot", "are you a robot", "computer talking"
- "am I talking to Nick", "is this really Nick", "is this actually Nick"
- "can I talk to a person", "let me talk to a human", "real person please"

Spanish:
- "eres un robot", "es un robot", "eres un bot", "es un bot"
- "eres una persona", "es una persona real", "hablo con una persona", "estoy hablando con una persona"
- "eres real", "es real", "eres humano"
- "es inteligencia artificial", "eres IA", "es una IA"
- "es automático", "mensaje automático", "respuesta automática"
- "de verdad eres Nick", "quiero hablar con una persona"

Pattern for the code: `\b(bot|robot|a\.?i\.?|ia|automated|autom[aá]tic[oa]|chat ?gpt|grok|real person|persona real|human[oa]?|a person|una persona)\b` together with a question mark or one of "are you", "is this", "am i", "eres", "es", "hablo", "estoy". A person reviews the first 50 hits to tune it. When in doubt, it fires: a false hand-off costs one alert, a missed one breaks the rule.

**Gate rule.** The check runs in the pre-filter, before the Grok call, so no AI call is spent. It also runs on the whole 3-minute batch: if any message in the batch triggers, the whole batch is held. Any draft already queued for that customer is dropped.

**Alert text to Nick and Zack.**
"BOT QUESTION. Maria, 2022 Camry, tint, on text. She asked: 'is this a real person?' Jesse stopped and sent nothing. Take over now: (her number)."

**CORE.md line.**
"If the customer asks whether you are real, a person, a bot, AI or automated, or asks to talk to a person: return an empty reply with handoff nick and reason bot_question. Never say you are a bot. Never say you are a person."

**Resume.** Only a person clears the `human` mark.

### 4.8 How Jesse alerts Nick today (no texting number needed)

| Option | Cost | Speed | What can break | Verdict |
|---|---|---|---|---|
| **Pushover push app** | About $5 once per phone | Seconds | Phone on Focus or battery saver; someone deletes the app; the app key leaks | **Primary.** One web call from the script. "Emergency" priority keeps re-alerting until Nick taps acknowledge. |
| **Gmail email with a "NEW LEAD" label** | $0 | Usually seconds, no promise | Buried in other mail. iPhone has no per-label sound; Android does | **Backup.** Send both every time. It also leaves a written record. |
| Email-to-text through the carrier | $0 | n/a | AT&T shut its gateway in June 2025. Verizon is shutting down now, done by March 2027. T-Mobile is unreliable. Fails silently. | **Do not use.** |
| Google Chat message | $0 with Workspace | Seconds | Phone push depends on Nick's settings; no repeat | Fine as a third option |

Alert format: "NEW LEAD. Maria, (number), 2022 Camry, tint, from Yelp. Said: 'how much for all windows'. Jesse answered at 10:42." Use emergency priority only for bot questions, complaints and "on my way" messages, 9:30 AM to 6 PM. Everything else is normal priority.

When the texting number is live, the same alert also goes by text.

### 4.9 Missed-call text-back

Trigger: a Google Voice missed-call email, shop hours or not. Sent 8 AM to 9 PM; a night call gets it at 8 AM. One per number per day. Never to a number already in an open conversation, a `human` lead, or do-not-contact.

**First text (EXAMPLE for Zack to approve):**
"Hey it's Nick at Audio MotorSports, sorry we missed your call! What are you looking to get done on your car? Reply STOP to opt out."

Spanish callers who pressed 2: "Hola, habla Carlos de Audio MotorSports, perdón que no alcanzamos su llamada. ¿Qué le gustaría hacerle a su carro? Responda STOP para no recibir mensajes."

Rules: no price, no discount, no link in this first text. It answers their call; it is not an ad. If they reply, the normal flow starts. If they do not, no follow-up. Heads-up (not legal advice): a caller did not ask for a text, so keep it to this one plain message.

Which opener it uses depends on Zack's answer to decision 1.

### 4.10 Spend cap and wake cap

1. xAI console: prepaid credits only, invoiced limit $0, auto top-up off. A hard stop.
2. Script: add up cost from each call. At $2 alert Zack. At $3 stop calling Grok for the day; canned replies and hand-offs keep working.
3. Wake cap: 80 Grok calls a day and 6 per customer. A loop hits the cap in minutes instead of running all night.

### 4.11 Stereo Specialist (Zack's way)

**What it is.** For one stereo lead, Jesse builds the parts list for that car and texts it to Nick and Zack to check. It is a suggestion for Nick. It is never a quote to the customer.

**When it runs.** Only when a stereo or CarPlay lead has year, make and model. One car, one look-up, on demand. Never a list of cars, never a crawler, never overnight batches.

**Look-up order (Zack's order, with the shop's own data first).**
1. The shop's own fit list and the site's car page (1,302 car year pages already hold verified radio type and speaker sizes). If the car is there, no outside look-up is needed.
2. Crutchfield, on Zack's own account, in the signed-in AMS Chrome on AMS-1. See decision 2 in section 2.
3. Metra (metraonline.com): the Vehicle Fit Guide, the part page (`metraonline.com/product/<part number>`) and the install PDF, which names the matching harness and antenna adapter.
4. ZZ2 and iDatalink Maestro.
5. MyFirstech (dealer login) for remote start.
6. Stinger and PAC.
Never Online Car Stereo.

**How it stays one normal look-up.**
- A person or the existing AMS Chrome parts look-up job opens the site the way a customer would: pick the car, read the result. No scripts hitting hidden addresses.
- One car per run. At least 2 minutes between runs. No more than 15 cars a day.
- Never clicks add to cart, checkout or any buy button.
- Every confirmed answer is saved to the shop's fit list with the source and date, so the same car is never looked up twice.
- If a site shows a captcha or a block page, the job stops and tells Zack. It never tries to get around it.

**What Jesse collects from the customer first.** Year, make, model, trim, body style; factory sound system (Bose, JBL, Fender and the like); factory screen and navigation; steering wheel buttons; factory backup camera. A dash photo covers most of it. A VIN settles mid-year changes.

**The text to Nick and Zack (template).**
"PARTS LIST, check me. Maria, 2015 Tacoma, wants CarPlay.
Radio: double DIN fits.
Dash kit: (part number).
Harness: (part number).
Steering wheel interface: (part number).
Antenna adapter: (part number).
Camera: keeps factory camera with (part number).
Speakers: front doors 6x9, rear doors 6.5.
Lost or kept: (chimes, factory amp).
Source: Metra fit guide and Crutchfield, Nov 15. Not confirmed on a car yet."

**When the fit is unclear.** Two sources disagree, the trim is unknown, or the car has a factory amp Jesse cannot identify: Jesse asks the customer for a dash photo, sends what he has to Nick marked "UNSURE", and hands off. He never tells a customer a part fits.

**What the customer gets.** The website as the brochure, one link per message: the car's page (`/vehicles/{make}/{model}/{years}/` or the `/alarm/` car page) for stereo and alarm, `/tint/` for tint, `/tesla/` pages for Tesla. A product picture comes from the product's own shop page; that page is the one link.

**Website data.** Adding parts and fit data to the site from these sources is task B in section 13.

### 4.12 Jobs that use no AI

- The 9:00 AM, 12:30 PM and 6:00 PM texts to Zack and Nick: read Calendar and the lead store, format, send. `sent_in_brief` stops any number repeating.
- Booking confirmation, noon-the-day-before reminder, 8 AM morning-of reminder.
- Review ask at noon the day after `bought`.
- Missed-call text-back.
- Contact naming "John Honda" through the People API.
- Follow-up timer: sets `next_action_at`; the words come from a template or one Grok call when it fires.
- The daily handoff when nothing unusual happened: a template filled from the lead store.

### 4.13 Proof before "it works"

1. Ten past real leads replayed with sending off: show Zack each reply.
2. A failing example for every pre-filter and send gate rule, including ten bot-question phrasings in English and Spanish.
3. A test text from Zack's phone answered in under 5 minutes.
4. A bot-question test: Zack texts "is this a real person?" Nothing comes back, both phones get the alert.
5. A missed-call test: the text arrives inside 2 minutes.
6. A day of logs: wakes, AI calls skipped by the pre-filter, tokens in, cached tokens, dollars.
7. The 9 AM text with real calendar data.
8. The cap test: cap at $0.01, Jesse stops, canned replies still go.

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

**Product pictures.** Each shop product page has the product's picture. When a customer asks what a radio or sub looks like, the product page is the one link.

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

## 7. Sales playbook and the 10 example replies

The playbook rules from v3 stand. The ten new skills are in section 12 as topic file drafts.

### Fact check of the 10 examples (Fix 8)

| # | Facts in it | Checked against | Result |
|---|---|---|---|
| 1 | Solar tint $349; $249 Tue to Fri | `/prices/`: Solar sedan $349; book-online $100 off | Prices correct. "Tue to Fri" is the Bible's rule; the site names no days (section 6). |
| 2 | CarPlay screens start at $189 | Shop page: BOSS BE7ACP $189, the lowest CarPlay radio | Correct. It is a product price, not labor. |
| 3 | Payment plan mention | CORE rules | **Changed.** It ended on a statement. Now ends on a question. |
| 4 | "the price on the listing" | CORE rules | **Changed.** The joke assumed a tint listing. Now fits any item. |
| 5 | None | | OK |
| 6 | Tuesday 9:30, Wednesday 10 | Nov 7 rule | OK |
| 7 | 22025 S Avalon | Live site: "22025 S Avalon Blvd Ste A, Carson, CA 90745" on all 4,139 pages and in the business schema | **Verified.** The Google Business Profile was not checked from here. |
| 8 | $150 off with the windshield overnight | `/prices/` | Correct |
| 9 | $50 off, both phone numbers, no link | `/specials/` | Correct. The site adds "when you buy the products from us"; that condition is now in the reply. |
| 10 | Google review ask | Google policy | OK. Sent to every customer. |

All ten open with or imply "Nick". That depends on Zack's answer to decision 1 in section 2.

### 10 example replies (EXAMPLES for Zack to approve, not final)

1. **New tint lead, text.** "Hi Maria, Nick here from Audio MotorSports, thanks for reaching out! That Camry is gonna look clean tinted. Solar tint is $349 but book Tuesday through Friday and it's $249, nothing upfront. What year is it?"
2. **"How much for CarPlay in my 2015 Tacoma", text.** "Good truck for it, those Tacomas take a CarPlay screen real nice and you keep your steering wheel buttons. CarPlay screens start at $189 for the radio itself and I'll get you the full number off one picture, can you send me a photo of your dash right here?"
3. **"That's too expensive".** "I hear you, nobody likes spending money on their car till they see it done. We do have a payment plan if you'd rather split it up. What did the other shop quote you, was that ceramic or regular film?"
4. **Marketplace, "can you do $150?"** "Ha, I wish, my boss would have my head. It's the price on the listing and that's already the deal, we have it in stock, come on in. What are you putting it in?"
5. **"I'll think about it".** "Totally, no rush. Is it more the price or finding a day that works?"
6. **Quote went quiet, next morning.** "Morning Mike, still got your Charger on my list for that alarm. I have Tuesday 9:30 or Wednesday 10 open, which one is yours?"
7. **Morning-of reminder.** "Morning Jessica, see you at 9:30 for the tint on the Model Y. We're at 22025 S Avalon Blvd, reply here if you're running behind."
8. **Upsell after a yes on tint.** "You're locked in for Tuesday 9:30. One thing, if you leave it with us overnight and add the windshield it's $150 off the whole package and the car stays way cooler. Want me to add it?"
9. **Yelp lead, alarm for a Charger, no links.** "Hi David, Nick here from Audio MotorSports, thanks for reaching out! Let's get that Charger protected the right way. Our alarm pricing is on our website and it's $50 off when you get it from us and book Tuesday through Friday, nothing upfront, and we have a payment plan if you need it. Stop by, call (310) 513-8800, or text me a couple pictures at (213) 429-1092 and I'll build you the right package. I can do Tuesday 9:30 AM or Wednesday 10 AM. Which one is yours?"
10. **Review ask, day after, sent to every customer.** "Hey Chris, Nick from Audio MotorSports, thanks for coming in yesterday. How's the new screen treating you? If you have a minute, a Google review would mean a lot to the family: [Google review link]"

## 8. Cost: the real number, not a guess

v3 said "about $16 a day before". That was an estimate built on assumptions. Replace it with the real number.

### Steps for Zack (10 minutes)

1. First, find out how Jesse was paid for. Open grok.com, go to Settings, then Billing. If there is a SuperGrok or Premium subscription and that is how Jesse ran, the cost was a flat monthly fee. Write that fee down and skip to step 7.
2. If Jesse ran on the API, go to console.x.ai and sign in as the team owner.
3. Open **Usage** (the Usage Explorer). The first view is cost in dollars.
4. Set the date range to the last 30 days. Set the detail level to daily if the option is there (UNVERIFIED).
5. Write down: the 30-day total, the highest single day, and a normal day. If there is a filter for API key or model, note which key and model spent the most.
6. Open **Billing**, then **Invoices**, and write down the last two invoice totals and how much prepaid credit is left.
7. While there: confirm the invoiced spending limit is $0 and auto top-up is off.

Duet should not ask Zack for a screenshot that shows any key. Totals only.

### Table to fill in

| | Before (real) | After (target) | After (real, first full week) |
|---|---|---|---|
| How Jesse is paid for (API or subscription) | | API, prepaid | |
| 30-day total | $ | about $15 | $ |
| Normal day | $ | $0.40 to $0.60 | $ |
| Highest single day | $ | under $3 (the cap) | $ |
| Messages from customers per day | | 20 to 40 | |
| Grok calls per day | | 15 to 25 | |
| AI calls skipped by plain code per day | 0 | 10 to 20 | |
| Share of input tokens billed as cached | | over 40% | |
| Top model used | | top model at 3 stages, mid model elsewhere | |

Third-party price trackers (verify in the console): top model about $2.00 in, $0.50 cached, $6.00 out per million tokens; mid model about $1.25, $0.20, $2.50. A cheaper "fast" model at about $0.20 in may or may not still exist.

Do not opt in to xAI's data-sharing credits. It cannot be undone and it would share customer conversations.

## 9. Hidden gems

| # | Gem | What it does | Why it pays | Effort | Caveat |
|---|---|---|---|---|---|
| 1 | Google Apps Script as the watcher | Free script in Google's cloud that reads Gmail on a timer, calls Grok, replies, and writes Calendar, Sheets and Contacts | Takes AMS-1 and the browser out of the main path. $0. | Medium | Timer only, 1 minute minimum; keep runs short |
| 2 | Google Voice email toggles (drives the missed-call text-back) | Texts, missed calls and voicemail transcripts all arrive as email | Missed calls become leads; this is the feature shops pay Podium for | Easy | Sending back by email is UNVERIFIED |
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
| 15 | Pushover | A push alert to Nick's phone from one web call, with repeat-until-acknowledged | Nick sees every new lead in seconds, today, with no texting number | Easy | About $5 once per phone; phone Focus mode can mute it |
| 16 | People API | Creates and renames contacts | "John Honda" on Nick's phone | Medium | Test one contact end to end first |

### Skip these

1. LangChain, CrewAI, AutoGen: layers of framework for one bot.
2. n8n self-hosted: several critical security holes in 2026, constant patching.
3. Vector databases and memory products (mem0, Letta): the Bible is a few dozen pages.
4. Browser bots for Google Voice, Yelp, Marketplace, OfferUp: against their rules and the reason the last build broke.
5. Bulk scraping or crawling Crutchfield or Metra: against their terms. One car at a time, look up only, is the rule (4.11).
6. Podium, Birdeye and similar: about $300 a month for a missed-call text and a review link.
7. RCS and Apple Messages for Business: paperwork and per-message cost for no gain at this size.
8. Gmail push through Pub/Sub: more parts than a 2-minute poll for the same result.
9. Full sales-bot frameworks (SalesGPT): take the stage list, leave the code.

## 10. Zack's full list, checked line by line (Fix 9)

| Zack's item | In v3? | In v4 |
|---|---|---|
| Yelp leads with a phone get a text | Named, no steps | Build step 9. The watcher reads the number from the Yelp email, checks do-not-contact, and sends one text from the texting number. First text names the shop and ends with "Reply STOP to opt out." Blocked until the number is live. |
| Book on Google Calendar and confirm they are coming | Yes | 4.6 and 4.12: script books, sends "Reply 1 to confirm or 2 to reschedule", reminders at noon the day before and 8 AM the day of. Customer texts the time back (skill 1). |
| Text Nick every new lead | Said, no method | 4.8: Pushover plus labeled Gmail today, a text as well once the number is live. |
| Stereo Specialist | v3 said skip Crutchfield and Metra | 4.11, Zack's way. |
| Review asks to every customer, Google only | Yes | 4.12 and skill 9. |
| Follow-ups from call recordings when the customer said "text me" | Listed as not possible yet | Still last (step 14). Needs a recording feed, the recording notice in English and Spanish, and local transcription. When built: the script finds "text me" in the transcript, logs it, and sends one text that names the shop and has the STOP line. |
| Name every contact in Google Voice | Yes | 4.12, People API, "John Honda". Test one contact first. |
| 9 AM, 12:30 PM, 6 PM texts, never repeating a number | Yes | 4.12 with the `sent_in_brief` mark. Sent by Pushover and email until the number is live. |
| Marketplace and OfferUp | Kept human | Same. Jesse drafts, a person pastes. Try Meta's own Marketplace auto-reply and Business Suite instant reply first. Night posting stays off until Facebook lifts the restriction and Zack says GO. |
| Daily handoff Doc on Drive | Yes | 4.12: template when the day was normal, one mid-model call when it was not. One file per day in "Jesse Handoffs". |
| Core rules read fresh every morning | Yes | Stronger: `CORE.md` is read on every call, so there is nothing to forget overnight. |
| One job per wake, then sleep | Yes | The watcher makes one call per customer batch and exits. Jesse has no loop of his own. Wake cap in 4.10. |
| "Are you a bot?" | Missing | 4.7. |
| Missed-call text-back | Last in the order | Step 8, text in 4.9. |

### What Jesse still cannot do

- Text a number that never texted the shop, until the texting number is live.
- Answer Marketplace or OfferUp by himself in any supported way.
- Post listings at night without risking the accounts.
- Read call recordings. No recording feed exists yet.

## 11. Power saving: every place to skip, shrink or batch an AI call (Fix 6)

Baseline after the v3 fix: about 25 Grok calls a day at about 2 cents each, so about $0.50 a day. Each saving below is against that baseline, at 20 to 40 customer messages a day. They overlap, so they do not add up to more than the baseline.

| # | Change | Saves per day | Sales risk |
|---|---|---|---|
| 1 | Watcher uses no AI; Jesse wakes only on a real message | $4 to $16 (the "before" bill, to be confirmed in section 8) | None |
| 2 | Hard spend cap and wake cap | $0 on a normal day; stops a $50 runaway day | None, if canned replies keep going when the cap hits |
| 3 | `CORE.md` + `INDEX.md` first and identical, so they bill as cached | About $0.10 | None |
| 4 | Canned first replies filled by script | About $0.10, and the reply goes in seconds | Low. A template can miss a second question, so anything not simple goes to Grok |
| 5 | History trimmed to the last 6 messages plus a 2-line summary on the lead row | About $0.08 | Low. Car and job live on the row, so they are not forgotten |
| 6 | Batch one customer's messages inside 3 minutes | About $0.07 | A reply is up to 3 minutes later. Still inside the 5-minute target |
| 7 | Pre-filter: junk, tapbacks, "ok", "thanks", STOP, bot question, our own alerts | About $0.06 | Low. "ok" right after Jesse offered two times is NOT skipped |
| 8 | Scripts for the daily texts, reminders, confirmations, review ask, contact names, missed-call text | About $0.08 against doing them with AI | None |
| 9 | Mid model for qualifying questions and the handoff; top model for quoted, objection and booked | About $0.06 | Some. A weaker opener can lose a lead, so keep the top model wherever price is discussed |
| 10 | Output cap 200 tokens for texts; reasoning mode off; web search off | About $0.04 | None. Short replies sell better by text |
| 11 | `CORE.md` cut from 2 pages to 1 | About $0.03 | None if the rules stay |
| 12 | One topic file per call, never two | About $0.03 | Low. A mixed question (tint and alarm) gets the main topic, and the other on the next message |
| 13 | Bookings from "Tuesday" or "1" handled by script | About $0.02 | None |
| 14 | Handoff by template on normal days | About $0.02 | None |
| 15 | Rules check done by code, never a second AI call | About $0.05 against a double-check call | None |
| 16 | Files kept local to the watcher, not fetched from Drive on each call | $0 in AI cost; saves seconds per call | None |
| 17 | Quiet hours: 9 PM to 8 AM messages wait and are answered in one pass at 8 AM | About $0.01 | A night lead waits till morning. The old rule already does this |

### Ranked top 10

1. No AI in the watcher.
2. Spend cap and wake cap.
3. Cached `CORE.md` and `INDEX.md`.
4. Canned first replies.
5. Trimmed history with a summary line.
6. Three-minute batching.
7. The pre-filter.
8. Scripts for every scheduled job.
9. Model by stage.
10. Output cap, reasoning off, search off.

**Blunt summary.** Number 1 is the whole game. Numbers 2 to 10 together are worth about $10 a month. Their real payoff is speed, the same answer every time, and no surprise bill. Do not let anyone chase cents at the cost of a weaker reply on a price conversation: one lost tint job is two years of AI savings.

## 12. Sales skills top 10, as topic file drafts (Fix 7)

All are drafts for Zack to approve. Each costs about 150 to 300 tokens when loaded, well under a tenth of a cent. Jesse loads one per call.

### What was searched

| Source | What it is | Use |
|---|---|---|
| louisblythe/Sales-Skills (GitHub, 206 stars, free licence) | 122 skill files: appointment booking, ghost recovery, pricing talk, upsell detection, micro-commitments, tone matching | Mined for skills 1, 2, 5 and 7. Written for office sales by email, so everything was cut down to two-line texts |
| coreyhaines31/marketingskills (GitHub, 60,000 stars) | Marketing skills; only `sms` and `pricing` apply | Length and tier ideas only |
| Dean Jackson's "9-word email" | One question to wake a dead lead | Skill 5 |
| Chris Voss, negotiation | Labels, calibrated questions, "no" questions | Skills 4 and 5. Practitioner advice, no controlled study |
| Appointment research (healthcare field studies) | A named time, and the customer repeating it, cut no-shows | Skills 1 and 10 |
| Tint World, Tint Wiz, Mobile Electronics magazine, Compustar | Trade advice: sell the visit, capture the name, one add-on per install | Skills 6 and 7 |
| Language research (CSA Research, Pew) | People buy in their own language | Skill 8 |

No open skill exists for review asks by text, no-show recovery or Spanish sales replies. Those three were written here.

### 1. `topics/close-two-slots.md`
- **What:** offer two named morning times; ask the customer to text the time back.
- **Why it sells:** studies of appointments show a named slot, and the person repeating it, raise show-up rates. Evidence is from healthcare.
- **Fits the rules:** yes. It is the Nov 7 close.
- **Draft:** "Always offer two times, Tuesday to Friday, 9:30 or 10. Ask 'which one is yours?' When they pick, say: 'Text me back the time so I lock it in.' Then the script books it. Never offer afternoons. Never confirm a time in writing on Marketplace or OfferUp."

### 2. `topics/photo-first.md`
- **What:** ask for one photo early (dash, door, the car).
- **Why it sells:** a small yes makes the next yes easier (a real but small effect), and the photo makes the quote right.
- **Fits:** yes.
- **Draft:** "On any stereo, speaker or alarm lead, ask for one photo in the first two messages: 'Can you send me a photo of your dash right here?' One ask. If no photo comes, ask year, make and model instead. Send the photo to Nick with the lead."

### 3. `topics/top-first.md`
- **What:** name the best option first, then step down.
- **Why it sells:** one pricing experiment found top-first raised revenue by up to 10%. Lab evidence on first numbers is strong; the texting use is a stretch.
- **Fits:** yes, with published prices only.
- **Draft:** "When they ask about tint, name the films top down with the price for their body type: 3M Ceramic IR, then Solar Ceramic, then Solar. Say in one line what the top one does (keeps the car cooler). Then ask which one they want. Never invent a tier."

### 4. `topics/price-pushback.md`
- **What:** name the feeling, ask one question, offer the payment plan, step down. Never discount.
- **Why it sells:** standard practice from negotiation training and auto trade advice. No controlled study.
- **Fits:** yes. Banned payment-plan phrases stay banned.
- **Draft:** "When they say it's too much: 1. 'Sounds like the price caught you off guard.' 2. One question: 'What did the other shop quote, and was that ceramic?' 3. 'We have a payment plan if you'd rather split it up, want me to text you the application?' 4. If still no, offer the next film or package down at its real price. Never lower a price. The only discount is the Tue to Fri booking one."

### 5. `topics/quiet-leads.md`
- **What:** three nudges and a last question, then stop.
- **Why it sells:** reply rates halve with each nudge, so each one must be short and about what they wanted.
- **Fits:** yes. Follow-ups are OFF today; Zack turns them on.
- **Draft:** "Next shop morning: offer the two times again. Day 3: 'Hi Maria, still looking to tint the Camry?' Nothing else. Day 7: 'Have you given up on the tint?' If no answer, mark the lead quiet and never write again unless they do. Never guilt. Never repeat a message. Stop the moment a person takes over."

### 6. `topics/sell-the-visit.md`
- **What:** for jobs with no published price, sell the stop-by, not a number.
- **Why it sells:** tint and audio trade advice agrees a bare price ends the talk, and a visit closes.
- **Fits:** yes. It is how Jesse lives with "no labor prices".
- **Draft:** "When the price is published (tint, alarms, dash cams, the sub packages), say it in the first line. When it is not (stereo, CarPlay, custom work), give the product's own price, say the full number comes from one photo or a quick stop-by, and invite them in: 'We're here till 6, come hear the displays.' Always get the name and the car before they go quiet."

### 7. `topics/one-add-on.md`
- **What:** one add-on, once, after the yes.
- **Why it sells:** trade advice: every install is a chance for one add-on. No published attach rates.
- **Fits:** yes. Published prices only.
- **Draft:** "After they agree to the main job, offer one thing: radio, then a backup camera. Tint, then the windshield overnight for $150 off the package. Alarm, then remote start, or the dash cam bundle at $488. Remote start, then the 2-way remote ('it tells you the car started'). Subs, then door speakers. One offer. If they say no, drop it."

### 8. `topics/spanish.md`
- **What:** answer in the customer's language; hand Spanish leads to Carlos.
- **Why it sells:** in a 29-country survey 76% preferred to buy with information in their own language. Not specific to Los Angeles.
- **Fits:** yes. A native speaker should check the words.
- **Draft:** "If they write in Spanish, answer in Spanish and alert Carlos. Use usted. Switch to tú only if they do. Words: polarizado, estéreo, bocinas, alarma, arranque remoto, cámara de reversa, cámara de tablero, cita, plan de pagos. Never 'financiamiento', never 'coche', never 'altavoces'. Do not guess the language from a name."

### 9. `topics/review-and-referral.md`
- **What:** check in, send the Google link to everyone, then one referral ask.
- **Why it sells:** vendor data says text beats email for reviews. Referred customers are more loyal in one bank study.
- **Fits:** yes. Google only, every customer, no reward, never Yelp.
- **Draft:** "Noon the day after the job: 'How's the new screen treating you?' with the Google review link in the same text, to every customer. If they answer unhappy, alert Nick; the link was still sent. If they answer happy: 'Know anybody else who needs tint? Have them ask for Nick.' One ask each. No rewards."

### 10. `topics/no-show.md`
- **What:** two reminders and one recovery text.
- **Why it sells:** text reminders raise show-up rates in field studies (healthcare).
- **Fits:** yes.
- **Draft:** "Noon the day before: 'See you tomorrow at 9:30 for the tint, reply 1 to confirm or 2 to reschedule.' 8 AM the day of: 'See you at 9:30, reply here if you're running behind.' 30 minutes after a miss: 'We missed you this morning, no worries. Want tomorrow at 9:30 or 10?' One recovery text. Never bring a cancelled booking back up."

## 13. PUT IT IN THE WEBSITE CODING AGENT

Two tasks. Both are preview only. Nothing deploys until Zack's GO; Kareem deploys.

### Task A: text message terms page and privacy line (needed before the texting number)

1. New page `/text-terms/` and Spanish `/es/terminos-de-texto/`. Title: "Text Message Terms". It must say, in plain words:
   - Who sends the texts: Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745.
   - What they are: answers to your questions, quotes, appointment confirmations and reminders, and a follow-up after your visit.
   - How you sign up: by texting or calling us, or by ticking the box on a form.
   - Message frequency varies. Message and data rates may apply.
   - Reply STOP to stop. Reply HELP for help, or call the shop number.
   - Carriers are not liable for delayed or undelivered messages.
   - A link to the privacy page.
2. Privacy page `/privacy/`: add one clear line: "We do not sell or share mobile phone numbers or text message consent with third parties or affiliates for marketing." The page already says the shop does not sell or share personal information; this line must name phone numbers and texting.
3. Contact form and booking form: add an unticked checkbox, not required to submit: "Text me about my request. Message frequency varies. Message and data rates may apply. Reply STOP to stop. See our Text Message Terms and Privacy Policy." with links to both pages.
4. Footer: a link to the text terms page next to Privacy and Terms.
5. Use the shop's numbers from the site's shared data, never typed digits. No warranty wording, no prices. Run the full check.
6. The exact wording should be checked against the texting provider's approval checklist before deploy (UNVERIFIED from here).

### Task B: parts and fit data on the site

1. Add a "confirmed in our bay" fit record: year, make, model, trim, factory system, radio size, dash kit, harness, steering wheel interface, antenna adapter, camera, speaker sizes, source, date, who confirmed it.
2. Show it on the car's page under the existing verified fit table, as facts in the shop's own words, with manufacturer part numbers.
3. Sources, in this order: the shop's own installs; Metra and other maker data (ask the Metra rep in writing for the dealer data file and permission to publish it); Crutchfield only as a cross-check a person reads.
4. Do not copy Crutchfield's or Metra's descriptions, photos, notes or page layout. Do not bulk-generate car pages from outside data. Part numbers and sizes are facts; the write-ups are not ours to copy.
5. Each fit line carries "confirm before ordering".
6. No labor prices. The higher price wins where a part price appears in two places.

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
- Bot law (all UNVERIFIED from here): [B&P Code 17940-17943](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&part=3.&chapter=6.), [law-firm summary](https://www.financierworldwide.com/bot-or-not-navigating-californias-bot-disclosure-law), [FTC on AI and trust](https://www.ftc.gov/business-guidance/blog/2023/05/luring-test-ai-engineering-consumer-trust), [Meta Messenger policy](https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy)
- Alerts: [Pushover pricing](https://pushover.net/pricing), [Verizon gateway shutdown](https://www.verizon.com/support/vtext-vzwpix-shutdown/), [Gmail notifications](https://support.google.com/mail/answer/10966)
- xAI usage: [Usage Explorer](https://docs.x.ai/console/usage), [billing](https://docs.x.ai/console/billing)
- Fit look-up: [Crutchfield terms](https://www.crutchfield.com/support/termsofuse.aspx), [Crutchfield vehicle selector](https://www.crutchfield.com/learn/inside-crutchfield-vehicle-selector.html), [Metra fit guide](https://metraonline.com/vehicle-fit-guide), [Metra dealers](https://www.metraonline.com/for-dealers), [Firstech dealer access](https://install.myfirstech.com/dealer-request)
- More sales sources: [9-word email](https://deanjackson.com/blog/the-9-word-email/), [no-oriented questions](https://blackswanltd.com/the-edge/negotiation-training-the-top-4-no-oriented-questions), [no-show study](https://doi.org/10.1258/jrsm.2011.110250), [Tint Wiz](https://tintwiz.com/?p=3895), [Compustar 2-way](https://www.compustar.com/blog/compustars-2-way-kits-now-include-dronemobile/), [language and buying](https://csa-research.com/Blogs-Events/CSA-in-the-Media/Press-Releases/Consumers-Prefer-their-Own-Language), [Pew on Spanish](https://www.pewresearch.org/race-and-ethnicity/2023/09/20/latinos-speaking-spanish-methodology/)
- Model routing evidence: [FrugalGPT](https://arxiv.org/abs/2305.05176)
