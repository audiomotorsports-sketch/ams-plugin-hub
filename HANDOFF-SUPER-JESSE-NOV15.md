# Handoff: Super Jesse (as of Nov 15, 2026)

Paste this whole file as the first message of a new project or conversation.

## What this is

Jesse is the Grok sales bot for Audio MotorSports. He runs on AMS-1. He does sales chat only and answers as Nick, Sales Manager. "Super Jesse" is the plan to rebuild what runs around him so he answers fast, costs little and never loops.

Everything so far is research and writing. Nothing has been built, changed, restarted, sent, posted, signed in to or bought.

## Where things stand

- **Current report (use this one):** "PUT IT IN CLAUDE DUET - Super Jesse v4 Report - Nov 15"
  https://docs.google.com/document/d/17_bapB9jhUr2l8HcTfQEqRhrI8IXQxdWi-n-dMIlrIU/edit
- **Repo copy:** `audiomotorsports-sketch/ams-plugin-hub`, branch `claude/ams-seo-aeo-audit-saun8p`, file `super-jesse-research/super-jesse-v4-report-nov15.md`.
- **Older reports (replaced by v4):** `super-jesse-research/super-jesse-v3-results-and-build-spec-nov15.md` and `super-jesse-research/super-jesse-research-v3-nov15.md`.
- **Next step:** Zack pastes the Duet prompt (bottom of this file) into Claude Duet. Duet finalizes the build plan. Nothing is built until Zack types GO.

## What v4 holds

| Section | What is in it |
|---|---|
| 0 to 1 | Limits of the research and the verdict |
| 2 | Decisions Zack makes before the build |
| 3 | Five hand tests a person runs first |
| 4 | Build spec: build order, files, lead store, pre-filter, send gate, bot-question rule, alerts, missed-call text, caps, Stereo Specialist, proof tests |
| 5 to 6 | The website as Jesse's brochure; where the site, the Bible and old skills disagree |
| 7 | 10 example replies, fact-checked |
| 8 | Steps to read the real xAI spend, and a table to fill in |
| 9 to 10 | Hidden gems; Zack's full list checked line by line |
| 11 | Power saving, 17 items, ranked top 10 |
| 12 | Sales skills top 10 as topic file drafts |
| 13 | Two tasks for the website coding agent |

## Open items for Zack

1. **Bot disclosure.** The rule stops Jesse from lying to anyone who asks. It does not cover customers who never ask and still get "Nick here" messages written by software. California's bot law may reach that (UNVERIFIED, not legal advice). Three setups are in section 2. Lowest risk: one line in the first message saying it is the shop's automated assistant working with Nick.
2. **Crutchfield look-ups.** Section 4.11 is written Zack's way. Crutchfield's terms reportedly ban automated or AI look-ups, even one car at a time (UNVERIFIED). Recommended until Zack reads the terms himself: a person does the Crutchfield check, Jesse does Metra and the rest.
3. **Where the watcher lives.** Recommended: Google Apps Script in the shop's Google account.
4. **Texting number.** Registration takes 1 to 7 business days, so it is build step 1. It needs the website text terms page first (section 13, task A).
5. **Marketplace and OfferUp.** Recommended: Jesse drafts, a person pastes.
6. **Discount days.** The Bible says Tuesday to Friday. The site names no days. Pick one.
7. **Review ask.** Google link only, every customer, never Yelp.
8. **Price conflicts** in section 6. The higher price wins.
9. **Real cost.** The "about $16 a day" figure in v3 was an estimate. Section 8 has the steps to read the real number.
10. **The 10 example replies** in section 7 need approve, change or cut.

## Not verified

The official pages of California's legislature, the FTC, Google, xAI, Yelp, Telnyx, Crutchfield, Metra and Pushover were blocked from the research session. Facts about them come from search extracts and third-party summaries. Each is marked UNVERIFIED in the Doc. A person must check them before anyone builds on them.

Also not seen: AMS-1 itself, Jesse's past chats, the xAI bill, and site analytics.

## Standing rules (never break)

- Research and planning only until Zack types GO. No code changes, restarts, customer messages, posts, sign-ins or purchases.
- Jesse answers as Nick, Sales Manager. Zack is Operational Manager. Nick is never "owner".
- "Are you real or a bot?": Jesse sends nothing, marks the lead human, alerts Nick and Zack. He never says he is a bot and never says he is a person.
- Call (310) 513-8800. Text (213) 429-1092. Never 513-6800.
- Say "payment plan", never "financing".
- No emojis.
- No labor or install prices.
- Warranty stays vague: "Brand new, with the manufacturer's warranty". No lengths, no return or refund terms.
- Where two prices disagree, the higher price wins.
- One link per message. No links on Yelp.
- Stereo Specialist: one car at a time, look up only, never buy, never bulk scrape or crawl. The parts list goes to Nick and Zack as a suggestion, never as a quote to the customer.
- Hours: Mon-Sat 9:30 AM-6 PM, closed Sunday. Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745.
- Never mention Twilio. Do not touch social media. Do not submit live forms.
- No secrets, keys, passwords or account numbers in chat or in any Doc.
- Website changes are preview only. Kareem deploys, only on Zack's GO.

## Related: the website

Website status is in `HANDOFF-AMS-WEBSITE-NOV15.md` in the same repo. Short version: the live site runs commit `f82438aa`; commit `25e6884c` on `claude/website-audit-fix-nov12` is pushed and waiting for Zack's GO. The two website tasks in section 13 of the v4 Doc have not been started.

## Prompt for Claude Duet

```
Read this whole Doc before you plan anything:
https://docs.google.com/document/d/17_bapB9jhUr2l8HcTfQEqRhrI8IXQxdWi-n-dMIlrIU/edit

It is the Super Jesse v4 research and build spec. Your job is to finalize the build plan from it, not to start building.

1. Do not change code, restart anything, send any customer message, post, sign in anywhere or buy anything until Zack types GO.
2. First, give Zack the list in section 2 as plain yes/no questions, one line each, and wait for his answers.
3. Ask Zack or Nick to run the hand tests in section 3 and report pass or fail. Do not design around anything marked UNVERIFIED until its test passes.
4. Then write the build plan in the order in section 4.0, using section 4 as the spec. For each step say what gets built, where it runs, what it costs, and what proof Zack will see (section 4.13).
5. Draft CORE.md, INDEX.md and the topic files from the AMS Bible using section 4.2 and the ten drafts in section 12. Settle every conflict in section 6 with Zack's answers. Where sources disagree on a price, the higher price wins.
6. Jesse is sales chat only. Anything that needs code goes to Claude Code as a task. The two website tasks in section 13 go to the website coding agent.
7. Standing rules stay as written in the AMS Bible: call (310) 513-8800, text (213) 429-1092, "payment plan", no labor or install prices, warranty stays vague, Nick is Sales Manager, Zack is Operational Manager, no emojis, no secrets in chat or Docs.
8. Show Zack the 10 example replies in section 7 and get each one approved, changed or cut before any goes into a topic file.

Report back in plain words, short: what is decided, what is waiting on Zack, and what you will build first.
```
