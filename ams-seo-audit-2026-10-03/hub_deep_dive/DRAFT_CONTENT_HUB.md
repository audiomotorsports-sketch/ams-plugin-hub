# DRAFT CONTENT: audiomotorsports.com hub, top pages

Prepared 2026-10-07 for Zack and Tom. **Drafts only. Nothing here has been applied.** No site, repo or account was changed. Every page stays live; every change below improves a page; nothing goes live until Zack and Tom review it together.

How this was built: each of the ten pages was fetched live on 2026-10-07 (HTTP 200) and every draft starts from its actual text. Answers use only facts found on live hub pages (or the live /llms.txt) and cite the page. Anything the site does not state, or states two different ways, is marked [CONFIRM] and collected in the checklist at the end. Numbers: titles are 60 characters or fewer, metas 120 to 160, answer-first paragraphs 50 to 70 words, question answers 40 to 60 words (all counted by script). In every JSON-LD block the FAQPage text was generated from the same string as the visible HTML and checked equal.

Verified business facts used throughout: Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; Monday to Saturday 9:30 AM to 6:00 PM. The text number (213) 429-1092 appears on the live pages as the text line. "Avalon" is the street name and is never used as a city.

### What the fetch changed in the brief (read first)

- Of the eight "FAQPage schema, no visible FAQ" pages, **five have no visible FAQ** (/tint/all-services/, the 70-VLT post, viper-vs-compustar, /beats/brands-we-love/, /brands-we-love/). **Three do have one**: /tesla/tesla-tint-carson/ and /tesla/tesla-tint-torrance/ show a 5-question FAQ whose wording differs from the schema in 2 and 1 places, and /faq/ shows all 18 questions but 15 of the 18 schema answers are not on the page (visible answers are longer, and 8 of them are cut off mid-sentence).
- The Carson Tesla page's live FAQ answer to "Is Tesla Tint LA in Avalon?" is "No. There is no Avalon Tesla tint storefront." A blind Avalon-to-Carson replacement would publish "No. There is no Carson Tesla tint storefront" on the page for the city where the shop is. The draft rewrites that answer.
- Site-wide price statements conflict ("no public prices" vs published prices; Tesla promo vs matrix; "$100 off" vs "no struck was"). Price text is drafted only where the number is identical on every page; Tesla prices are left out.
- Only `/` lacks hreflang among the hub pages checked that have a Spanish twin. The Carson and Torrance Tesla pages and /services/remote-start/ have no Spanish twin (404).
- /tesla/tesla-tint-carson/ is in the sitemap but not linked from the /tesla/locations/ grid.

Contents: pages 1 to 10 (copy-ready block each), then special cases 1 to 5, then the [CONFIRM] checklist.

---

## 1. /

Live URL: https://www.audiomotorsports.com/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Audio MotorSports \| Carson Shop` | 31 |
| H1 | `Pick a skill` | |
| Meta description | `Audio MotorSports in Carson. Tesla tint, car alarm, window tint, AMS Pods, stereo, and beats. Call (310) 513-8800 or text (213) 429-1092. Payment plan available.` | 161 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Car Stereo, Tint & Alarm Shop in Carson \| Audio MotorSports` | 59 of 60 characters |
| Meta description | `Car stereo, CarPlay, hand-cut window tint, car alarms and Harley bagger audio in Carson, CA. Mon-Sat 9:30-6:00. Call (310) 513-8800. Payment plan available.` | 156 characters (target 120 to 160) |
| H1 | `Car stereo, window tint and car alarms in Carson, CA` | |

Note: Keep the current words "Pick a skill" as a short line above the six skill tiles (an H2 or eyebrow), so the tile section keeps its label. Only the H1 changes.

### Answer-first paragraph (65 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports is a car stereo, window tint and car alarm shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. One bay handles stereo and CarPlay installs, hand-cut ceramic tint, Viper and Compustar alarms with remote start, and Harley bagger audio. Hours are Monday to Saturday, 9:30 AM to 6:00 PM, closed Sunday. Call (310) 513-8800 or text (213) 429-1092 for a quote.</p>
```

### Question headings and answers (5 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Questions about Audio MotorSports in Carson</h2>
  <h3>Where is Audio MotorSports?</h3>
  <p>Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745. It is one shop with one bay, open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 or text (213) 429-1092. The city pages on this site are drive-ins to the Carson bay, not separate shops.</p>
  <h3>What does Audio MotorSports install?</h3>
  <p>Car stereos with Apple CarPlay and Android Auto, amplifiers and subwoofers, dash cameras, ceramic window tint, car alarms and remote start, and Harley bagger audio built as AMS Pods. The shop does not do wraps, wheels, tires, auto glass repair or suspension work. Call with the year, make and model for a quote.</p>
  <h3>Does Audio MotorSports offer a payment plan?</h3>
  <p>Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept.</p>
  <h3>How do I get a quote?</h3>
  <p>Call (310) 513-8800, text (213) 429-1092, or send the Get a Quote form with your phone number, year, make, model and the skill you want. Nick texts or calls you back. Published specials are installed starting prices, not final quotes, so the shop confirms the price for your vehicle.</p>
  <h3>Do customers drive in from other cities?</h3>
  <p>Yes. Customers drive in from the harbor area, the South Bay, Long Beach, inland Los Angeles and Orange County. The Locations page lists 123 drive-in cities, and every job is done at the Carson bay. The shop does no mobile installs, so the work always happens at 22025 S Avalon Blvd Ste A.</p>
</section>
```

Where each answer comes from (live pages only):

- Where is Audio MotorSports?: /faq/ Where is the shop?; home footer
- What does Audio MotorSports install?: home nav + footer; /faq/ What services do you specialize in?; live llms.txt 'does not do'
- Does Audio MotorSports offer a payment plan?: /payment-plan/ (intro, 'Apply online below. Approval and terms are set by the provider.')
- How do I get a quote?: home 'Get a Quote' form copy; live llms.txt 'Published specials are starting points'
- Do customers drive in from other cities?: /locations/ (123 tiles, counted); /faq/ Do you do mobile installs?

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AutoRepair",
      "@id": "https://www.audiomotorsports.com/#business",
      "name": "Audio MotorSports",
      "legalName": "Audio MotorSports Inc",
      "alternateName": [
        "Audio Motorsports",
        "AMS"
      ],
      "url": "https://www.audiomotorsports.com/",
      "description": "Car audio, window tint, vehicle security, and Harley bagger audio in Carson, California.",
      "image": "https://www.audiomotorsports.com/assets/img/hero/hub-hero-desktop.jpg",
      "logo": "https://www.audiomotorsports.com/assets/img/logo/ams-coin-gold.png",
      "telephone": "+13105138800",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "22025 S Avalon Blvd Ste A",
        "addressLocality": "Carson",
        "addressRegion": "CA",
        "postalCode": "90745",
        "addressCountry": "US"
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
          ],
          "opens": "09:30",
          "closes": "18:00"
        }
      ],
      "areaServed": [
        {
          "@type": "City",
          "name": "Carson"
        },
        {
          "@type": "City",
          "name": "Los Angeles"
        },
        {
          "@type": "City",
          "name": "Long Beach"
        },
        {
          "@type": "City",
          "name": "Torrance"
        },
        {
          "@type": "City",
          "name": "Gardena"
        },
        {
          "@type": "City",
          "name": "San Pedro"
        },
        {
          "@type": "City",
          "name": "Harbor City"
        },
        {
          "@type": "City",
          "name": "Wilmington"
        }
      ],
      "sameAs": [
        "https://www.instagram.com/audiomotorsports/",
        "https://share.google/RyQaFlk39cTTMU6TG",
        "https://www.youtube.com/channel/UCHYn2FTtiBZ53EXWNBWAyeg",
        "https://www.facebook.com/Audiomotorsports/",
        "https://www.tiktok.com/@audiomotorsports",
        "https://yelp.to/Lm2GAc4OiS",
        "https://maps.google.com/maps?ftid=0x80c33234c579b9bd:0xa886ff7f43445f0a"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.audiomotorsports.com/#website",
      "url": "https://www.audiomotorsports.com/",
      "name": "Audio MotorSports",
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "inLanguage": "en-US"
    },
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/#webpage",
      "url": "https://www.audiomotorsports.com/",
      "name": "Car Stereo, Tint & Alarm Shop in Carson | Audio MotorSports",
      "description": "Car stereo, CarPlay, hand-cut window tint, car alarms and Harley bagger audio in Carson, CA. Mon-Sat 9:30-6:00. Call (310) 513-8800. Payment plan available.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "primaryImageOfPage": "https://www.audiomotorsports.com/assets/img/hero/hub-hero-desktop.jpg"
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/#faq",
      "url": "https://www.audiomotorsports.com/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Where is Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745. It is one shop with one bay, open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 or text (213) 429-1092. The city pages on this site are drive-ins to the Carson bay, not separate shops."
          }
        },
        {
          "@type": "Question",
          "name": "What does Audio MotorSports install?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Car stereos with Apple CarPlay and Android Auto, amplifiers and subwoofers, dash cameras, ceramic window tint, car alarms and remote start, and Harley bagger audio built as AMS Pods. The shop does not do wraps, wheels, tires, auto glass repair or suspension work. Call with the year, make and model for a quote."
          }
        },
        {
          "@type": "Question",
          "name": "Does Audio MotorSports offer a payment plan?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept."
          }
        },
        {
          "@type": "Question",
          "name": "How do I get a quote?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Call (310) 513-8800, text (213) 429-1092, or send the Get a Quote form with your phone number, year, make, model and the skill you want. Nick texts or calls you back. Published specials are installed starting prices, not final quotes, so the shop confirms the price for your vehicle."
          }
        },
        {
          "@type": "Question",
          "name": "Do customers drive in from other cities?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Customers drive in from the harbor area, the South Bay, Long Beach, inland Los Angeles and Orange County. The Locations page lists 123 drive-in cities, and every job is done at the Carson bay. The shop does no mobile installs, so the work always happens at 22025 S Avalon Blvd Ste A."
          }
        }
      ]
    }
  ]
}
</script>
```

Left out of the home business node on purpose, each is [CONFIRM] first: `geo` (the site uses two different coordinate sets, 33.8270 / -118.2650 on /tint/, /locations/ and the city pages and 33.8270587 / -118.2641283 on the Tesla pages), `priceRange` (the tint and locations nodes show "$$"), `aggregateRating` (4.8 / 654; Google does not show stars for self-marked local businesses), `foundingDate` ("Since 2003" appears on /tint/), `email` (the site uses a Gmail address in every node; a domain mailbox is better if one exists), the sister-domain `sameAs` URLs (present on the site's other nodes: lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com), and `subOrganization`. `sameAs` above lists only the seven profile and map URLs that already appear in the site's existing business nodes; the self-link to the hub was dropped.

### Sources and [CONFIRM] items for this page

Sources: Live home page; /faq/; /payment-plan/; /locations/; live /llms.txt.

- [CONFIRM] Home JSON-LD: geo, priceRange, aggregateRating, foundingDate and email are left out until confirmed (see list under the JSON-LD).
- [CONFIRM] Claims in the answer paragraph (Viper and Compustar, Harley bagger audio, CarPlay) are on the live site (nav, /faq/, live llms.txt); no new claims added.


---

## 2. /tint/

Live URL: https://www.audiomotorsports.com/tint/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Ceramic Window Tint LA & Long Beach \| Hand-Cut` | 46 |
| H1 | `Ceramic window tint in Los Angeles and Long Beach` | |
| Meta description | `Hand-cut ceramic window tint for Los Angeles, Long Beach, South Bay, and Orange County. Text Nick. Payment Plan available.` | 122 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Hand-Cut Ceramic Window Tint in Carson, CA \| LA Car Tint` | 56 of 60 characters |
| Meta description | `Hand-cut ceramic window tint at the Carson bay, serving Los Angeles, Long Beach and the South Bay. 3M film, California-legal fronts. Call (310) 513-8800.` | 153 characters (target 120 to 160) |
| H1 | `Hand-cut ceramic window tint in Carson, serving Los Angeles and Long Beach` | |

### Answer-first paragraph (68 words; place directly under the H1)

```html
<p class="answer-first">LA Car Tint is the window-tint desk at Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745. Every piece of film is hand-cut on a glass board, never on your glass. Solar starts at $249 and Solar Ceramic at $329 installed for a four-door sedan, doors and back glass, no windshield (verified September 2026). 3M Ceramic IR and Color Stable are quote only. Call (310) 513-8800.</p>
```

### Question headings and answers (6 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Window tint questions answered</h2>
  <h3>How much does window tint cost in Carson?</h3>
  <p>Solar starts at $249 and Solar Ceramic starts at $329 installed for a four-door sedan, covering the four doors and back glass but not the windshield. 3M Ceramic IR and 3M Color Stable are quote only, and so is the windshield. Prices verified September 2026. Text Nick the year, make and model to confirm.</p>
  <h3>How long does window tint take?</h3>
  <p>Most cars take about two to three hours in the bay. Book a 10:00 AM or 12:00 PM slot, or text Nick your year, make and model. You can drive the car when the install is finished. Keep the windows up for 3 to 5 days while the film cures.</p>
  <h3>Is 70% VLT on front windows legal in California?</h3>
  <p>California front side windows must allow at least 70% of light through, and the shop installs fronts to that spec. Rear side glass and the back glass have no limit, so they can go darker. Full windshield film is not legal in California. A windshield strip is a separate product, so text Nick before adding one.</p>
  <h3>What is the difference between hand-cut and computer-cut tint?</h3>
  <p>Hand-cut film is cut on a glass board, then applied, so the micro edge sits right to the gasket. The shop never cuts on your glass, which is how defroster lines get scratched. Plotter shops cut from a pattern database and trim the film short, which shows as a thin line of light at the edges within a season.</p>
  <h3>Can I pay for window tint over time?</h3>
  <p>Yes. A payment plan is available. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, or text Nick and he will send the link. Approval and terms are set by the provider. Booking a slot does not take a deposit.</p>
  <h3>Can I drop my car off overnight for tint?</h3>
  <p>Yes, Tuesday through Thursday. Drop your car at close, by 6 PM, and pick it up the next day. The shop photographs your car at check-in so you see its condition before work starts. Text Nick to reserve an overnight spot.</p>
</section>
```

Where each answer comes from (live pages only):

- How much does window tint cost in Carson?: /tint/ hero + cards; /faq/ 'Do you publish prices online?'; live llms.txt; city pages
- How long does window tint take?: /tint/ FAQ 'How long does tint take?' + 'How long before I roll windows down?'
- Is 70% VLT on front windows legal in California?: /tint/ FAQ 'How dark can I go legally' + estimator text 'Rears have no limit'; /faq/ 'Is your tint legal in California?'
- What is the difference between hand-cut and computer-cut tint?: /tint/ section 'Hand-cut vs computer-cut'
- Can I pay for window tint over time?: /tint/ FAQ 'Do you offer a payment plan?'; /payment-plan/
- Can I drop my car off overnight for tint?: /tint/ FAQ 'Can I drop my car off overnight?'

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/tint/#webpage",
      "url": "https://www.audiomotorsports.com/tint/",
      "name": "Hand-Cut Ceramic Window Tint in Carson, CA | LA Car Tint",
      "description": "Hand-cut ceramic window tint at the Carson bay, serving Los Angeles, Long Beach and the South Bay. 3M film, California-legal fronts. Call (310) 513-8800.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/tint/#faq",
      "url": "https://www.audiomotorsports.com/tint/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/tint/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How much does window tint cost in Carson?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Solar starts at $249 and Solar Ceramic starts at $329 installed for a four-door sedan, covering the four doors and back glass but not the windshield. 3M Ceramic IR and 3M Color Stable are quote only, and so is the windshield. Prices verified September 2026. Text Nick the year, make and model to confirm."
          }
        },
        {
          "@type": "Question",
          "name": "How long does window tint take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Most cars take about two to three hours in the bay. Book a 10:00 AM or 12:00 PM slot, or text Nick your year, make and model. You can drive the car when the install is finished. Keep the windows up for 3 to 5 days while the film cures."
          }
        },
        {
          "@type": "Question",
          "name": "Is 70% VLT on front windows legal in California?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "California front side windows must allow at least 70% of light through, and the shop installs fronts to that spec. Rear side glass and the back glass have no limit, so they can go darker. Full windshield film is not legal in California. A windshield strip is a separate product, so text Nick before adding one."
          }
        },
        {
          "@type": "Question",
          "name": "What is the difference between hand-cut and computer-cut tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Hand-cut film is cut on a glass board, then applied, so the micro edge sits right to the gasket. The shop never cuts on your glass, which is how defroster lines get scratched. Plotter shops cut from a pattern database and trim the film short, which shows as a thin line of light at the edges within a season."
          }
        },
        {
          "@type": "Question",
          "name": "Can I pay for window tint over time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. A payment plan is available. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, or text Nick and he will send the link. Approval and terms are set by the provider. Booking a slot does not take a deposit."
          }
        },
        {
          "@type": "Question",
          "name": "Can I drop my car off overnight for tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, Tuesday through Thursday. Drop your car at close, by 6 PM, and pick it up the next day. The shop photographs your car at check-in so you see its condition before work starts. Text Nick to reserve an overnight spot."
          }
        }
      ]
    }
  ]
}
</script>
```

### Held back (not drafted, with the reason)

- Appointment Q: /tint/ says 'Yes. Book a slot or text Nick' while /faq/, /locations/ and live llms.txt say walk-ins are welcome. Held until the shop answers.
- Warranty Q: /tint/ FAQ says '30-day written workmanship warranty on installed products. Film and hardware carry the manufacturer's own warranty.' Live llms.txt says 'Do not mention warranty.' Held until the shop decides.
- Carbon vs ceramic Q: the live answer names 'Solar Carbon' and 'Premium Ceramic IR' while the page cards say 'Solar' and '3M Ceramic IR'. Held until film names are confirmed.

### Sources and [CONFIRM] items for this page

Sources: Live /tint/; /faq/; /payment-plan/; /llms.txt; hub city pages.

- [CONFIRM] Price sentence uses $249 and $329 because they are identical on every page that states them; re-verify and put today's date in place of 'September 2026'.
- [CONFIRM] Page currently shows the cards '$100 off' ($249) with no 'was' price. See the price section.


---

## 3. /tesla/

Live URL: https://www.audiomotorsports.com/tesla/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Tesla Window Tint LA \| Model 3, Y, S, X` | 39 |
| H1 | `Tesla window tint in Los Angeles for Model 3, Y, S, and X` | |
| Meta description | `Tesla tint in LA from a Tesla-owning shop. Hand-cut ceramic and windshield options. Book a 10 AM or noon slot, or text Nick.` | 124 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Tesla Window Tint in Carson & LA \| Tesla Tint LA` | 48 of 60 characters |
| Meta description | `Hand-cut ceramic window tint for Tesla Model 3, Y, Y L, S, X and Cybertruck at the Carson bay. Solar Ceramic or 3M IR Ceramic. Call (310) 513-8800.` | 147 characters (target 120 to 160) |
| H1 | `Tesla window tint in Carson for Model 3, Y, Y L, S, X and Cybertruck` | |

### Answer-first paragraph (65 words; place directly under the H1)

```html
<p class="answer-first">Tesla Tint LA is the Tesla window-tint desk at Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745. The bay tints Model 3, Model Y, Model Y L, Model S, Model X and Cybertruck with hand-cut Solar Ceramic or 3M IR Ceramic film. Front windows stay at California's 70% VLT. Appointments are 10:00 AM or 12:00 PM. Call (310) 513-8800 or text Nick.</p>
```

### Question headings and answers (6 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Tesla window tint questions answered</h2>
  <h3>Which Tesla models do you tint?</h3>
  <p>Tesla Model 3, Model Y, Model Y L, Model S, Model X and Cybertruck. Film is hand-cut on a glass board, then applied to your car, and never cut on your glass. Other vehicles go to LA Car Tint, so this desk handles Tesla glass only. Call (310) 513-8800 or text Nick with the model.</p>
  <h3>Does ceramic tint affect GPS or phone signal?</h3>
  <p>No. Ceramic film is non-metal, so it does not affect GPS or phone signal. Tesla owners pick ceramic over a dyed metal film for that reason. The bay runs two ceramic films on Tesla glass, Solar Ceramic and 3M IR Ceramic. The shop does not invent a range percentage for cameras.</p>
  <h3>How long does a Model Y take?</h3>
  <p>A Model Y doors-and-back install is usually two to three hours when the film is in stock and the glass is clean. Book a 10:00 AM or 12:00 PM slot, Monday through Saturday, or text Nick the model and film you want. Same-day depends on the bay being open.</p>
  <h3>Can I tint a Tesla windshield?</h3>
  <p>Yes. Windshield film is its own option, separate from the doors and the back glass. Front side windows stay at 70% VLT under California law, and the shop keeps fronts there. Darker rear glass is legal, and the shop walks the shade with you in person rather than from a photo.</p>
  <h3>Do I need an appointment for Tesla tint?</h3>
  <p>Yes. Book a slot or text Nick; Tesla appointments are 10:00 AM or 12:00 PM. Same-day is possible if you arrive at the 9:30 opening and the bay is open. Hours are Monday through Saturday, 9:30 AM to 6:00 PM. Sunday is closed.</p>
  <h3>Can I drop my Tesla off overnight?</h3>
  <p>Yes, Tuesday through Thursday. Drop your Tesla at close, by 6 PM, and pick it up the next day. The shop photographs your car at check-in so you see its condition before work starts. Text Nick to reserve an overnight spot.</p>
</section>
```

Where each answer comes from (live pages only):

- Which Tesla models do you tint?: /tesla/ FAQ 'Which Tesla models do you tint?'
- Does ceramic tint affect GPS or phone signal?: /tesla/ FAQ 'Does ceramic tint affect GPS or phone signal?'; films section
- How long does a Model Y take?: /tesla/ FAQ 'How long does a Model Y take?' + appointment answer
- Can I tint a Tesla windshield?: /tesla/ FAQ 'Do you tint windshields?'; 'Legal fronts' section
- Do I need an appointment for Tesla tint?: /tesla/ FAQ 'Do I need an appointment?'
- Can I drop my Tesla off overnight?: /tesla/ FAQ 'Can I drop my car off overnight?'

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/tesla/#webpage",
      "url": "https://www.audiomotorsports.com/tesla/",
      "name": "Tesla Window Tint in Carson & LA | Tesla Tint LA",
      "description": "Hand-cut ceramic window tint for Tesla Model 3, Y, Y L, S, X and Cybertruck at the Carson bay. Solar Ceramic or 3M IR Ceramic. Call (310) 513-8800.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/tesla/#faq",
      "url": "https://www.audiomotorsports.com/tesla/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/tesla/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Which Tesla models do you tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tesla Model 3, Model Y, Model Y L, Model S, Model X and Cybertruck. Film is hand-cut on a glass board, then applied to your car, and never cut on your glass. Other vehicles go to LA Car Tint, so this desk handles Tesla glass only. Call (310) 513-8800 or text Nick with the model."
          }
        },
        {
          "@type": "Question",
          "name": "Does ceramic tint affect GPS or phone signal?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Ceramic film is non-metal, so it does not affect GPS or phone signal. Tesla owners pick ceramic over a dyed metal film for that reason. The bay runs two ceramic films on Tesla glass, Solar Ceramic and 3M IR Ceramic. The shop does not invent a range percentage for cameras."
          }
        },
        {
          "@type": "Question",
          "name": "How long does a Model Y take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Model Y doors-and-back install is usually two to three hours when the film is in stock and the glass is clean. Book a 10:00 AM or 12:00 PM slot, Monday through Saturday, or text Nick the model and film you want. Same-day depends on the bay being open."
          }
        },
        {
          "@type": "Question",
          "name": "Can I tint a Tesla windshield?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Windshield film is its own option, separate from the doors and the back glass. Front side windows stay at 70% VLT under California law, and the shop keeps fronts there. Darker rear glass is legal, and the shop walks the shade with you in person rather than from a photo."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need an appointment for Tesla tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Book a slot or text Nick; Tesla appointments are 10:00 AM or 12:00 PM. Same-day is possible if you arrive at the 9:30 opening and the bay is open. Hours are Monday through Saturday, 9:30 AM to 6:00 PM. Sunday is closed."
          }
        },
        {
          "@type": "Question",
          "name": "Can I drop my Tesla off overnight?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, Tuesday through Thursday. Drop your Tesla at close, by 6 PM, and pick it up the next day. The shop photographs your car at check-in so you see its condition before work starts. Text Nick to reserve an overnight spot."
          }
        }
      ]
    }
  ]
}
</script>
```

### Held back (not drafted, with the reason)

- Price Q ('How much is Tesla window tint?') is not drafted: /tesla/ shows promo prices ($149 / $299 / $199) next to 'Matrix' prices ($189 / $369 / $399) while /tesla/tesla-tint-carson/ and /torrance/ list a different 'locked' matrix. Held until the shop names one price source.
- Payment plan Q is already answered on the live page; add it back after the price decision if wanted (use the payment-plan wording in Special case 3).

### Sources and [CONFIRM] items for this page

Sources: Live /tesla/; /tesla/tesla-tint-carson/; /faq/.

- [CONFIRM] Current meta says 'from a Tesla-owning shop'. That claim is not repeated elsewhere on the site, so the draft drops it. Keep it only if true.
- [CONFIRM] Top strip says '650+ Google reviews, 700+ Yelp reviews' while hero says 654 and 777. Pick one pattern.


---

## 4. /tesla/tesla-tint-carson/

Live URL: https://www.audiomotorsports.com/tesla/tesla-tint-carson/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Tesla Window Tint Avalon \| Tesla Tint LA` | 40 |
| H1 | `Tesla Window Tint for Avalon` | |
| Meta description | `Tesla window tint for Avalon — Solar Ceramic and 3M IR Ceramic on Avalon. Ask for Nick. (310) 513-8800.` | 103 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Tesla Window Tint in Carson, CA \| Tesla Tint LA` | 47 of 60 characters |
| Meta description | `Tesla window tint in Carson, CA: hand-cut Solar Ceramic and 3M IR Ceramic at 22025 S Avalon Blvd Ste A. Ask for Nick. Call (310) 513-8800.` | 138 characters (target 120 to 160) |
| H1 | `Tesla Window Tint in Carson, CA` | |

### Answer-first paragraph (68 words; place directly under the H1)

```html
<p class="answer-first">Tesla Tint LA tints Teslas in Carson, CA, at Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745. Model 3, Model Y, Model Y L, Model S, Model X and Cybertruck get hand-cut Solar Ceramic or 3M IR Ceramic film, with California-legal 70% VLT fronts. Appointments are 10:00 AM or 12:00 PM, Monday to Saturday, 9:30 AM to 6:00 PM. Ask for Nick at (310) 513-8800.</p>
```

### Question headings and answers (5 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Tesla tint in Carson: questions answered</h2>
  <h3>Where is Tesla Tint LA in Carson?</h3>
  <p>Tesla Tint LA is the Tesla window-tint side of Audio MotorSports, in the Carson shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. It is one bay with one map pin. Walk-ins fill the floor, so text the year and model to hold a 10:00 AM or 12:00 PM slot. Ask for Nick at (310) 513-8800.</p>
  <h3>How much is Tesla window tint in Carson?</h3>
  <p>Price depends on the Tesla model, the film (Solar Ceramic or 3M IR Ceramic) and the glass: two front windows, doors plus back with no windshield, or the windshield, each priced as its own line. The installed prices for every model are in the price table on this page. Text Nick the model and film to confirm.</p>
  <h3>Do you tint the Tesla Model Y L in Carson?</h3>
  <p>Yes. Model Y L has more glass than a Model Y, and it is first in the lineup on this site. Text the year and Model Y L so Nick can hold a 10:00 AM or 12:00 PM slot, and ask for the Model Y L price from the table on this page. Bring the car if you can.</p>
  <h3>When can I book Tesla tint in Carson?</h3>
  <p>Appointments are 10:00 AM or 12:00 PM only, Monday through Saturday. The shop is open 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick, or text the year and model before you drive in. Walk-ins happen, but they fill the floor.</p>
  <h3>Can I get a stereo or alarm at Tesla Tint LA?</h3>
  <p>No. Tesla Tint LA is Tesla window tint only, with Solar Ceramic and 3M IR Ceramic. It does not sell stereo, alarm, audio, wraps, PPF or glass repair. A payment plan is available at the counter for the tint job. Stereo and alarm work is done at Audio MotorSports in the same Carson shop.</p>
</section>
```

Where each answer comes from (live pages only):

- Where is Tesla Tint LA in Carson?: Live Carson FAQ (schema Q1) with 'Avalon' city-use replaced by 'Carson'
- How much is Tesla window tint in Carson?: Carson page price table; kept number-free until the price source is confirmed
- Do you tint the Tesla Model Y L in Carson?: Live Carson FAQ Q3
- When can I book Tesla tint in Carson?: Live Carson FAQ Q4 + 'Walk-ins happen, and they fill the floor'
- Can I get a stereo or alarm at Tesla Tint LA?: Live Carson FAQ Q5; /faq/ 'desks in the same bay'

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/#webpage",
      "url": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/",
      "name": "Tesla Window Tint in Carson, CA | Tesla Tint LA",
      "description": "Tesla window tint in Carson, CA: hand-cut Solar Ceramic and 3M IR Ceramic at 22025 S Avalon Blvd Ste A. Ask for Nick. Call (310) 513-8800.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/#faq",
      "url": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Where is Tesla Tint LA in Carson?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tesla Tint LA is the Tesla window-tint side of Audio MotorSports, in the Carson shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. It is one bay with one map pin. Walk-ins fill the floor, so text the year and model to hold a 10:00 AM or 12:00 PM slot. Ask for Nick at (310) 513-8800."
          }
        },
        {
          "@type": "Question",
          "name": "How much is Tesla window tint in Carson?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Price depends on the Tesla model, the film (Solar Ceramic or 3M IR Ceramic) and the glass: two front windows, doors plus back with no windshield, or the windshield, each priced as its own line. The installed prices for every model are in the price table on this page. Text Nick the model and film to confirm."
          }
        },
        {
          "@type": "Question",
          "name": "Do you tint the Tesla Model Y L in Carson?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Model Y L has more glass than a Model Y, and it is first in the lineup on this site. Text the year and Model Y L so Nick can hold a 10:00 AM or 12:00 PM slot, and ask for the Model Y L price from the table on this page. Bring the car if you can."
          }
        },
        {
          "@type": "Question",
          "name": "When can I book Tesla tint in Carson?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Appointments are 10:00 AM or 12:00 PM only, Monday through Saturday. The shop is open 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick, or text the year and model before you drive in. Walk-ins happen, but they fill the floor."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get a stereo or alarm at Tesla Tint LA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Tesla Tint LA is Tesla window tint only, with Solar Ceramic and 3M IR Ceramic. It does not sell stereo, alarm, audio, wraps, PPF or glass repair. A payment plan is available at the counter for the tint job. Stereo and alarm work is done at Audio MotorSports in the same Carson shop."
          }
        }
      ]
    }
  ]
}
</script>
```

### Sources and [CONFIRM] items for this page

Sources: Live /tesla/tesla-tint-carson/ (every paragraph read); /tesla/; /faq/.

- [CONFIRM] All driving directions on the live page ('stay on Avalon until the bay is on the right', 'two lights up Avalon', 'two minutes if you are already on the block', 'harbor-adjacent shimmer') are unverified and not carried into the draft.
- [CONFIRM] The page is in sitemap.xml but is not linked from /tesla/locations/ (the grid links /tesla/tesla-tint-west-carson/ and /tesla/tesla-tint-torrance/ but not Carson). Adding the link is additive.


The full before-and-after for the word "Avalon" on this page is in Special case 1 below.

---

## 5. /tesla/tesla-tint-torrance/

Live URL: https://www.audiomotorsports.com/tesla/tesla-tint-torrance/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Tesla Window Tint Torrance \| Tesla Tint LA` | 42 |
| H1 | `Tesla Window Tint for Torrance` | |
| Meta description | `Tesla window tint for Torrance — Solar Ceramic and 3M IR Ceramic on Avalon. Ask for Nick. (310) 513-8800.` | 105 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Tesla Window Tint Near Torrance \| Tesla Tint LA, Carson` | 55 of 60 characters |
| Meta description | `Torrance Tesla owners drive to the Carson bay at 22025 S Avalon Blvd for hand-cut Solar Ceramic or 3M IR Ceramic tint. Ask for Nick. (310) 513-8800.` | 148 characters (target 120 to 160) |
| H1 | `Tesla Window Tint Near Torrance, at the Carson Bay` | |

### Answer-first paragraph (60 words; place directly under the H1)

```html
<p class="answer-first">Tesla Tint LA has no Torrance storefront. Torrance drivers bring their Tesla to the one shop, Audio MotorSports at 22025 S Avalon Blvd Ste A in Carson, CA 90745, for hand-cut Solar Ceramic or 3M IR Ceramic tint. Text the year and model so Nick can hold a 10:00 AM or 12:00 PM slot, Monday to Saturday. Call (310) 513-8800.</p>
```

### Question headings and answers (5 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Tesla tint for Torrance drivers: questions answered</h2>
  <h3>Is Tesla Tint LA in Torrance?</h3>
  <p>No. Tesla Tint LA has no Torrance storefront. It is the Tesla window-tint side of Audio MotorSports at 22025 S Avalon Blvd Ste A in Carson, CA 90745: one bay, one map pin. Torrance is a drive-in. Call (310) 513-8800 and ask for Nick. Zack runs the floor.</p>
  <h3>How much is Tesla window tint for Torrance drivers?</h3>
  <p>Price follows the Tesla model, the film (Solar Ceramic or 3M IR Ceramic) and the glass covered: two front windows, doors plus back with no windshield, or the windshield. The installed price for each model is in the price table on this page. Text Nick the model and film to confirm.</p>
  <h3>Do you tint the Tesla Model Y L for Torrance drivers?</h3>
  <p>Yes. Model Y L has more glass than a Model Y and is first in the lineup on this site. Text the year and Model Y L so Nick can hold a 10:00 AM or 12:00 PM slot, and ask for the Model Y L price from the table on this page. Bring the car; glass shape lies in photos.</p>
  <h3>When can Torrance drivers book Tesla tint?</h3>
  <p>Appointments are 10:00 AM or 12:00 PM only, Monday through Saturday. The shop is open 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick, or text the year and Tesla model before you leave Torrance.</p>
  <h3>Can I get a stereo or alarm at Tesla Tint LA?</h3>
  <p>No. Tesla Tint LA is Tesla window tint only, with Solar Ceramic and 3M IR Ceramic. It does not sell stereo, alarm, audio, wraps, PPF or glass repair. A payment plan is available at the counter for the tint job. Stereo and alarm work is done at Audio MotorSports in the same Carson shop.</p>
</section>
```

Where each answer comes from (live pages only):

- Is Tesla Tint LA in Torrance?: Live Torrance FAQ Q1 (route and distance sentences left out until confirmed)
- How much is Tesla window tint for Torrance drivers?: Torrance page price table; number-free until price source is confirmed
- Do you tint the Tesla Model Y L for Torrance drivers?: Live Torrance FAQ Q3
- When can Torrance drivers book Tesla tint?: Live Torrance FAQ Q4
- Can I get a stereo or alarm at Tesla Tint LA?: Live Torrance FAQ Q5

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-torrance/#webpage",
      "url": "https://www.audiomotorsports.com/tesla/tesla-tint-torrance/",
      "name": "Tesla Window Tint Near Torrance | Tesla Tint LA, Carson",
      "description": "Torrance Tesla owners drive to the Carson bay at 22025 S Avalon Blvd for hand-cut Solar Ceramic or 3M IR Ceramic tint. Ask for Nick. (310) 513-8800.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-torrance/#faq",
      "url": "https://www.audiomotorsports.com/tesla/tesla-tint-torrance/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/tesla/tesla-tint-torrance/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is Tesla Tint LA in Torrance?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Tesla Tint LA has no Torrance storefront. It is the Tesla window-tint side of Audio MotorSports at 22025 S Avalon Blvd Ste A in Carson, CA 90745: one bay, one map pin. Torrance is a drive-in. Call (310) 513-8800 and ask for Nick. Zack runs the floor."
          }
        },
        {
          "@type": "Question",
          "name": "How much is Tesla window tint for Torrance drivers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Price follows the Tesla model, the film (Solar Ceramic or 3M IR Ceramic) and the glass covered: two front windows, doors plus back with no windshield, or the windshield. The installed price for each model is in the price table on this page. Text Nick the model and film to confirm."
          }
        },
        {
          "@type": "Question",
          "name": "Do you tint the Tesla Model Y L for Torrance drivers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Model Y L has more glass than a Model Y and is first in the lineup on this site. Text the year and Model Y L so Nick can hold a 10:00 AM or 12:00 PM slot, and ask for the Model Y L price from the table on this page. Bring the car; glass shape lies in photos."
          }
        },
        {
          "@type": "Question",
          "name": "When can Torrance drivers book Tesla tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Appointments are 10:00 AM or 12:00 PM only, Monday through Saturday. The shop is open 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick, or text the year and Tesla model before you leave Torrance."
          }
        },
        {
          "@type": "Question",
          "name": "Can I get a stereo or alarm at Tesla Tint LA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Tesla Tint LA is Tesla window tint only, with Solar Ceramic and 3M IR Ceramic. It does not sell stereo, alarm, audio, wraps, PPF or glass repair. A payment plan is available at the counter for the tint job. Stereo and alarm work is done at Audio MotorSports in the same Carson shop."
          }
        }
      ]
    }
  ]
}
</script>
```

### Sources and [CONFIRM] items for this page

Sources: Live /tesla/tesla-tint-torrance/; /locations/.

- [CONFIRM] Live page says 'About 4.4 miles, roughly ten to fifteen minutes' and 'take the 405 to Avalon, or cut Del Amo, Crenshaw, or Torrance Blvd'. /locations/ also lists Torrance at 4.4 mi. Unverified; left out of the draft. Add back only after the shop confirms.
- [CONFIRM] Live text calls it 'a fake Torrance Tesla tint shop' and 'the Compton inland-110 script'. Those phrases read as internal notes; the draft does not reuse them.


---

## 6. /faq/

Live URL: https://www.audiomotorsports.com/faq/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `FAQ \| Stereo, Tint & Alarm \| Audio MotorSports` | 46 |
| H1 | `Quick answers` | |
| Meta description | `Four pillars only, no public prices, payment plans, Nick on sales, Zack on ops, Carson shop hours.` | 98 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `FAQ: Car Stereo, Tint & Alarm in Carson \| Audio MotorSports` | 59 of 60 characters |
| Meta description | `Answers on car stereo installs, ceramic tint, California 70% VLT, Compustar vs Viper, remote start, prices and the payment plan at our Carson shop.` | 147 characters (target 120 to 160) |
| H1 | `Car stereo, window tint and alarm questions, answered` | |

### Answer-first paragraph (60 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports answers the questions drivers ask before a stereo, tint or alarm job: what stays working after an install, whether ceramic tint is legal in California, Compustar or Viper, and what things cost. Every job is done in one Carson bay at 22025 S Avalon Blvd Ste A, Monday to Saturday, 9:30 AM to 6:00 PM. Call (310) 513-8800.</p>
```

### Visible short answers for all 18 questions (insert under each existing question heading)

Each existing question keeps its long answer. The line below is added directly under the question heading, and it is the exact text used in the JSON-LD, so visible text and schema match word for word. Six of the lines (marked REWRITTEN) are new 40-60 word answers; the other twelve are the live schema text, unchanged.

```html
<h2>Why not buy a cheap CarPlay radio off Amazon?</h2>
<p class="faq-short">A no-name Amazon CarPlay or Android Auto radio is not a safe buy. If it isn’t Pioneer, Sony, Kenwood, or factory premium system, you’ll likely buy another radio soon — dead spots on the screen, it won’t pair, the camera won’t integrate, and the steering-wheel controls fail. We sell and install those name brands; we’ll still install a Boss or a generic unit from Crutchfield, but we can’t service the Amazon units — it’s the part, not the install. Call first for a real game plan — a payment plan is available, so you spend once, not twice.</p>
<!-- existing long answer stays here -->
<h2>Why hire a pro for a bass amplifier install?</h2>
<p class="faq-short">On paper a bass amp is simple — power, ground, remote, and an RCA signal, and you have bass. In the car it is not: power through the firewall, fused, with the right terminals; panels off; cable routed to the amp, sometimes with the seats out; the signal and phase right; and a real ground. When it is finished it should look like it belongs there — no extra wire, nothing twisted. DIY jobs burn amps and equipment, and have put cars on fire; one mistake can kill the amp. Hiring a pro does not cost a lot next to that headache, and when the bass quits later you have someone to call.</p>
<!-- existing long answer stays here -->
<h2>Is oxygen-free copper wire worth it, or is a cheap CCA amp kit fine?</h2>
<p class="faq-short">CCA is the basic amp kit, about $50. An oxygen-free copper kit is about $200, and it is worth it when the job needs it. One sub at a few hundred watts can run on CCA; two 12s around 2,000 watts will heat CCA until it melts, takes the fuse, and causes problems. OFC does not get hot, does not melt, does not corrode, and the system sounds better — people here play for hours, three or four a day, some all night, so if you are serious about audio, use OFC.</p>
<!-- existing long answer stays here -->
<h2>Why add a GPS tracker that notifies you?</h2>
<p class="faq-short">In LA you leave the car for hours or all day — Vegas, the outlets, hotels, movie theaters. A GPS tracker with phone alerts (Viper SmartStart, Drone XC, DroneMobile) tells you if someone hits the car, opens a door, or tampers with it. A screaming alarm does not get the police called. This is peace of mind for the investment — people who leave expensive tools or equipment in the vehicle, and high-theft cars like Kia, Hyundai, Jeep, Dodge, and Chrysler. If it does get taken, you know where it is so you can get it back.</p>
<!-- existing long answer stays here -->
<h2>Compustar vs Viper — which alarm?</h2>
<p class="faq-short">Compustar and Viper both make car alarms. They are competitors, they work differently, and we use both — we pick by the car. Compustar kills the ignition when you walk away, so the car will not start without your fob; that is what we want on Jeep, Dodge, Chrysler, and some newer cars where someone can copy the arm/disarm code and steal it. Viper has an electronic ignition kill you turn on — the right call on GMC, Ford, and fleet vehicles — but on those copy-code cars, unlocking with a copied code can disarm the Viper. Dodge gets Compustar. A diesel Ford gets Viper. Both are top quality. Come in or call and we will point you to the right one.</p>
<!-- existing long answer stays here -->
<h2>What services do you specialize in?</h2>
<p class="faq-short">Four pillars: car stereo installation, ceramic window tint, Harley bagger audio, and car alarm / security. Dash cameras sit with the alarm work. No wraps, wheels, tires, performance, chrome-delete, auto glass repair, suspension, LED lighting, door locks, or in-dash DVD as a service.</p>
<!-- existing long answer stays here -->
<h2>What stays working after a car stereo installation?</h2>
<p class="faq-short">A stereo install has to keep the factory functions that already work: backup sensors, steering wheel controls, backup camera, and on some cars OnStar, the front or scene camera, the mirror camera, blind-spot assist, and the warning chimes. Maestro or iDataLink is what lets the new stereo show climate, doors, and tire pressures.</p>
<!-- existing long answer stays here -->
<h2>What is ceramic window tint?</h2> <!-- REWRITTEN, 57 words -->
<p class="faq-short">Ceramic window tint is polyester film with ceramic nanoparticles that block heat, so you do not feel the burn on your skin and a lot of the sun's heat and UV stay out. The shop hand-cuts a micro edge on a glass board in the Carson shop, then applies it. Every car takes two to three hours.</p>
<!-- existing long answer stays here -->
<h2>Do you publish prices online?</h2> <!-- REWRITTEN, 56 words -->
<p class="faq-short">Most work is quoted on the vehicle. Published starting prices, installed: Solar tint $249 and Solar Ceramic $329 for four doors and the back glass, Viper 3108V $269, Compustar 9910 $499 on most cars, and AMS pods $649 a pair. Dual Kicker Comp is $249 box only. 3M films are quote only. Prices verified September 2026.</p>
<!-- existing long answer stays here -->
<h2>Who should I contact for sales vs ops?</h2>
<p class="faq-short">Nick handles sales. Zack is Operational Manager.</p>
<!-- existing long answer stays here -->
<h2>Do you build Harley bagger audio?</h2>
<p class="faq-short">Yes — Road Glide, Street Glide, and Road King, since the early 2000s. AMS pods are built in-house, chrome or black. Bags get an AMS quick disconnect. The method is on AMS Pods.</p>
<!-- existing long answer stays here -->
<h2>Hertz Neo or DS18 on a bagger?</h2>
<p class="faq-short">DS18 is the cheap one. Huge magnet, hard and sharp, loud — not an acoustic speaker. Fine if you only want it to scream. Hertz Neo is the motorcycle speaker. Weatherproof, small magnet so it fits a bag and an AMS pod, and it stays clear when it is loud. It costs more. You hear the music, not just noise. That is what we put in the pods.</p>
<!-- existing long answer stays here -->
<h2>Hertz Neo or Cicada on a bagger?</h2>
<p class="faq-short">Cicada is a serious motorcycle brand. People speak well of it. It also costs more than Hertz, and the magnet is huge — it eats most of the space in the lid. We ran them side by side. Hertz was louder and cleaner. Better performance in the bag. Hertz Neo is weatherproof, small neo magnet, so you keep the space. That is the one we recommend.</p>
<!-- existing long answer stays here -->
<h2>Where is the shop?</h2> <!-- REWRITTEN, 55 words -->
<p class="faq-short">Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745, the only location. There is no second shop in Long Beach, Torrance, Irvine or downtown Los Angeles, and the city pages are drive-ins. Hours are Monday through Saturday, 9:30 AM to 6:00 PM, closed Sunday. Call (310) 513-8800 or text (213) 429-1092.</p>
<!-- existing long answer stays here -->
<h2>Do you do mobile installs?</h2> <!-- REWRITTEN, 60 words -->
<p class="faq-short">No. Every job is done in the Audio MotorSports bay at 22025 S Avalon Blvd Ste A, Carson. Cutting tint on the vehicle scratches glass and risks defroster lines, so every piece is hand-cut on a glass board in the shop, then applied. Stereo, alarm and bagger audio need the same bay, power and people. Drive in or trailer in.</p>
<!-- existing long answer stays here -->
<h2>Do I need an appointment?</h2>
<p class="faq-short">Walk-ins welcome Monday through Saturday, 9:30 AM – 6:00 PM. Come in before 4pm and most jobs go home the same day.</p>
<!-- existing long answer stays here -->
<h2>How long does window tint take?</h2> <!-- REWRITTEN, 52 words -->
<p class="faq-short">Most full-car window tint takes two to three hours: four doors and the back glass, hand-cut on a glass board, then applied. Teslas, glass roofs and cars that need old film removed first are booked with more time. Tint that needs a reserved slot is booked at 10:00 AM or 12:00 PM.</p>
<!-- existing long answer stays here -->
<h2>Is your tint legal in California?</h2> <!-- REWRITTEN, 55 words -->
<p class="faq-short">Yes. California requires front side windows at 70% VLT, and the shop installs fronts to that spec. The windshield can only be tinted along a strip at the top, 70, 50 or 35 when quoted. Rear side windows and the back glass have no VLT limit, so those can go as dark as you want.</p>
<!-- existing long answer stays here -->
```

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/faq/#webpage",
      "url": "https://www.audiomotorsports.com/faq/",
      "name": "FAQ: Car Stereo, Tint & Alarm in Carson | Audio MotorSports",
      "description": "Answers on car stereo installs, ceramic tint, California 70% VLT, Compustar vs Viper, remote start, prices and the payment plan at our Carson shop.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/faq/#faq",
      "url": "https://www.audiomotorsports.com/faq/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/faq/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Why not buy a cheap CarPlay radio off Amazon?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A no-name Amazon CarPlay or Android Auto radio is not a safe buy. If it isn’t Pioneer, Sony, Kenwood, or factory premium system, you’ll likely buy another radio soon — dead spots on the screen, it won’t pair, the camera won’t integrate, and the steering-wheel controls fail. We sell and install those name brands; we’ll still install a Boss or a generic unit from Crutchfield, but we can’t service the Amazon units — it’s the part, not the install. Call first for a real game plan — a payment plan is available, so you spend once, not twice."
          }
        },
        {
          "@type": "Question",
          "name": "Why hire a pro for a bass amplifier install?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "On paper a bass amp is simple — power, ground, remote, and an RCA signal, and you have bass. In the car it is not: power through the firewall, fused, with the right terminals; panels off; cable routed to the amp, sometimes with the seats out; the signal and phase right; and a real ground. When it is finished it should look like it belongs there — no extra wire, nothing twisted. DIY jobs burn amps and equipment, and have put cars on fire; one mistake can kill the amp. Hiring a pro does not cost a lot next to that headache, and when the bass quits later you have someone to call."
          }
        },
        {
          "@type": "Question",
          "name": "Is oxygen-free copper wire worth it, or is a cheap CCA amp kit fine?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "CCA is the basic amp kit, about $50. An oxygen-free copper kit is about $200, and it is worth it when the job needs it. One sub at a few hundred watts can run on CCA; two 12s around 2,000 watts will heat CCA until it melts, takes the fuse, and causes problems. OFC does not get hot, does not melt, does not corrode, and the system sounds better — people here play for hours, three or four a day, some all night, so if you are serious about audio, use OFC."
          }
        },
        {
          "@type": "Question",
          "name": "Why add a GPS tracker that notifies you?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In LA you leave the car for hours or all day — Vegas, the outlets, hotels, movie theaters. A GPS tracker with phone alerts (Viper SmartStart, Drone XC, DroneMobile) tells you if someone hits the car, opens a door, or tampers with it. A screaming alarm does not get the police called. This is peace of mind for the investment — people who leave expensive tools or equipment in the vehicle, and high-theft cars like Kia, Hyundai, Jeep, Dodge, and Chrysler. If it does get taken, you know where it is so you can get it back."
          }
        },
        {
          "@type": "Question",
          "name": "Compustar vs Viper — which alarm?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Compustar and Viper both make car alarms. They are competitors, they work differently, and we use both — we pick by the car. Compustar kills the ignition when you walk away, so the car will not start without your fob; that is what we want on Jeep, Dodge, Chrysler, and some newer cars where someone can copy the arm/disarm code and steal it. Viper has an electronic ignition kill you turn on — the right call on GMC, Ford, and fleet vehicles — but on those copy-code cars, unlocking with a copied code can disarm the Viper. Dodge gets Compustar. A diesel Ford gets Viper. Both are top quality. Come in or call and we will point you to the right one."
          }
        },
        {
          "@type": "Question",
          "name": "What services do you specialize in?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Four pillars: car stereo installation, ceramic window tint, Harley bagger audio, and car alarm / security. Dash cameras sit with the alarm work. No wraps, wheels, tires, performance, chrome-delete, auto glass repair, suspension, LED lighting, door locks, or in-dash DVD as a service."
          }
        },
        {
          "@type": "Question",
          "name": "What stays working after a car stereo installation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A stereo install has to keep the factory functions that already work: backup sensors, steering wheel controls, backup camera, and on some cars OnStar, the front or scene camera, the mirror camera, blind-spot assist, and the warning chimes. Maestro or iDataLink is what lets the new stereo show climate, doors, and tire pressures."
          }
        },
        {
          "@type": "Question",
          "name": "What is ceramic window tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ceramic window tint is polyester film with ceramic nanoparticles that block heat, so you do not feel the burn on your skin and a lot of the sun's heat and UV stay out. The shop hand-cuts a micro edge on a glass board in the Carson shop, then applies it. Every car takes two to three hours."
          }
        },
        {
          "@type": "Question",
          "name": "Do you publish prices online?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Most work is quoted on the vehicle. Published starting prices, installed: Solar tint $249 and Solar Ceramic $329 for four doors and the back glass, Viper 3108V $269, Compustar 9910 $499 on most cars, and AMS pods $649 a pair. Dual Kicker Comp is $249 box only. 3M films are quote only. Prices verified September 2026."
          }
        },
        {
          "@type": "Question",
          "name": "Who should I contact for sales vs ops?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nick handles sales. Zack is Operational Manager."
          }
        },
        {
          "@type": "Question",
          "name": "Do you build Harley bagger audio?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes — Road Glide, Street Glide, and Road King, since the early 2000s. AMS pods are built in-house, chrome or black. Bags get an AMS quick disconnect. The method is on AMS Pods."
          }
        },
        {
          "@type": "Question",
          "name": "Hertz Neo or DS18 on a bagger?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "DS18 is the cheap one. Huge magnet, hard and sharp, loud — not an acoustic speaker. Fine if you only want it to scream. Hertz Neo is the motorcycle speaker. Weatherproof, small magnet so it fits a bag and an AMS pod, and it stays clear when it is loud. It costs more. You hear the music, not just noise. That is what we put in the pods."
          }
        },
        {
          "@type": "Question",
          "name": "Hertz Neo or Cicada on a bagger?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Cicada is a serious motorcycle brand. People speak well of it. It also costs more than Hertz, and the magnet is huge — it eats most of the space in the lid. We ran them side by side. Hertz was louder and cleaner. Better performance in the bag. Hertz Neo is weatherproof, small neo magnet, so you keep the space. That is the one we recommend."
          }
        },
        {
          "@type": "Question",
          "name": "Where is the shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745, the only location. There is no second shop in Long Beach, Torrance, Irvine or downtown Los Angeles, and the city pages are drive-ins. Hours are Monday through Saturday, 9:30 AM to 6:00 PM, closed Sunday. Call (310) 513-8800 or text (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "Do you do mobile installs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Every job is done in the Audio MotorSports bay at 22025 S Avalon Blvd Ste A, Carson. Cutting tint on the vehicle scratches glass and risks defroster lines, so every piece is hand-cut on a glass board in the shop, then applied. Stereo, alarm and bagger audio need the same bay, power and people. Drive in or trailer in."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need an appointment?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Walk-ins welcome Monday through Saturday, 9:30 AM – 6:00 PM. Come in before 4pm and most jobs go home the same day."
          }
        },
        {
          "@type": "Question",
          "name": "How long does window tint take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Most full-car window tint takes two to three hours: four doors and the back glass, hand-cut on a glass board, then applied. Teslas, glass roofs and cars that need old film removed first are booked with more time. Tint that needs a reserved slot is booked at 10:00 AM or 12:00 PM."
          }
        },
        {
          "@type": "Question",
          "name": "Is your tint legal in California?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. California requires front side windows at 70% VLT, and the shop installs fronts to that spec. The windshield can only be tinted along a strip at the top, 70, 50 or 35 when quoted. Rear side windows and the back glass have no VLT limit, so those can go as dark as you want."
          }
        }
      ]
    }
  ]
}
</script>
```

This FAQPage replaces the live FAQPage block on /faq/ (same 18 questions, same order). Visible short answers now exist for all 18, so nothing in the markup is invisible.

### Held back (not drafted, with the reason)

- Appointment answer (schema 'Walk-ins welcome ... Come in before 4pm') is kept unchanged because the policy conflicts with /tint/; not rewritten.

### Sources and [CONFIRM] items for this page

Sources: Live /faq/ (all 18 answers read in full, plus the live schema); /payment-plan/; live /llms.txt.

- [CONFIRM] Price answer: Solar $249, Solar Ceramic $329, Viper 3108V $269, Compustar 9910 from $499, AMS pods from $649 and Dual Kicker Comp $249 box only are each identical on every page that states them; re-verify and re-date ('September 2026').
- [CONFIRM] Mobile installs, hours and the two-to-three-hour tint time are stated the same way on /faq/ and other pages; the 'Walk in before 4' line is kept only in the unchanged answers.
- [CONFIRM] 'Tint that needs a reserved slot is booked at 10:00 AM or 12:00 PM' follows /faq/ and /locations/; /tint/ says all tint needs an appointment. See the checklist.

Live defects found on /faq/ while drafting (each is a fix that improves the page):

- The meta description says "no public prices" but the page publishes prices (Viper 3108V $269, Compustar 9910 from $499, Solar $249, Solar Ceramic $329, AMS pods from $649). The proposed meta drops that phrase.
- 8 of the 18 visible answers are cut off mid-sentence at about 167 words, so the closing line ends in a fragment. Restore the full closing sentence: "Call (310) 513-8800 or text (213) 429-1092. Walk in before 4 and most jobs go home the same day." Live endings:
  - Why hire a pro for a bass amplifier install? ... `unday closed. Call (310) 513-8800 or text (213).`
  - Is oxygen-free copper wire worth it, or is a cheap CCA amp kit fine? ... `00 or text (213) 429-1092. Walk in before 4 and.`
  - Why add a GPS tracker that notifies you? ... `3-8800 or text (213) 429-1092. Walk in before 4.`
  - Compustar vs Viper — which alarm? ... ` (310) 513-8800 or text (213) 429-1092. Walk in.`
  - What is ceramic window tint? ... `turday, 9:30 AM to 6:00 PM. Sunday closed. Call.`
  - Hertz Neo or DS18 on a bagger? ... `092. Walk in before 4 and most jobs go home the.`
  - Hertz Neo or Cicada on a bagger? ... `Walk in before 4 and most jobs go home the same.`
  - Is your tint legal in California? ... `513-8800 or text (213) 429-1092. Walk in before.`
- The live FAQ schema answer for "Do you publish prices online?" says "AMS pods stay a quote" while the visible answer says "AMS pods start at $649 a pair". The rewritten answer above uses the visible figure.
- [CONFIRM] "Do I need an appointment?" (walk-ins welcome, come in before 4) conflicts with /tint/ ("Yes. Book a slot"). The schema text is kept as is until the shop answers.
- [CONFIRM] The services answer says no LED lighting as a service and no door locks, but the hub has /services/led-lights/ and /services/door-actuators/ pages.
- 15 of the 18 schema answers were not visible anywhere on the page. Three already matched the visible text exactly (the oxygen-free copper wire, GPS tracker and Hertz Neo or DS18 answers) and are unchanged.


---

## 7. /reviews/

Live URL: https://www.audiomotorsports.com/reviews/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Reviews \| Audio MotorSports` | 27 |
| H1 | `Customer Reviews` | |
| Meta description | `Google 4.8 from 654. Yelp 4.7 from 777.` | 39 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Customer Reviews \| Audio MotorSports in Carson, CA` | 50 of 60 characters |
| Meta description | `Google 4.8 from 654 reviews and Yelp 4.7 from 777 for Audio MotorSports in Carson, CA. Read five-star Yelp quotes on stereo, tint and dash cam installs.` | 152 characters (target 120 to 160) |
| H1 | `Customer reviews of Audio MotorSports in Carson, CA` | |

### Answer-first paragraph (67 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports in Carson, CA is rated 4.8 from 654 reviews on Google and 4.7 from 777 on Yelp, as of [CONFIRM date]. The five-star quotes below are copied from the shop's Yelp listing with the reviewer's name as shown on Yelp. They cover stereo, subwoofer and dash cam work. Open the Google or Yelp listing to read every review, or leave your own after your install.</p>
```

### Question headings and answers (4 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Questions about our reviews</h2>
  <h3>What is Audio MotorSports' Google rating?</h3>
  <p>Google shows Audio MotorSports at 4.8 from 654 reviews as of [CONFIRM date]. That rating is for the shop overall, not for one page. Yelp shows 4.7 from 777. Open the Google reviews listing from this page to read every review, including the full text of each five-star review.</p>
  <h3>Where do the quotes on this page come from?</h3>
  <p>The five quotes are five-star reviews from the Audio MotorSports Yelp listing, shown word for word with the name as it appears on Yelp. They cover honest pricing, a subwoofer purchase, a replacement for a factory premium stereo and a dash cam install in a 1979 VW bus. Google reviews stay on Google.</p>
  <h3>How do I leave a review?</h3>
  <p>After your install, leave a review on Google or Yelp using the buttons at the bottom of this page. You can also call (310) 513-8800, text (213) 429-1092 or send a quote request for your next job. The shop is open Monday through Saturday, 9:30 AM to 6:00 PM.</p>
  <h3>Are these reviews for one shop?</h3>
  <p>Yes. Every review is for the one Audio MotorSports shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The tint, stereo, alarm, Harley bagger and Tesla sites in the network are desks in the same bay, so the ratings belong to the same shop and the same Google listing.</p>
</section>
```

Where each answer comes from (live pages only):

- What is Audio MotorSports' Google rating?: /reviews/ hero + 'On Google' block; /locations/ FAQ 'What reviews should I trust?'
- Where do the quotes on this page come from?: /reviews/ Yelp block (five quotes)
- How do I leave a review?: /reviews/ 'Loved your install?' block
- Are these reviews for one shop?: /tint/ 'Same shop. Same listing.'; /faq/ 'desks in the same bay'

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/reviews/#webpage",
      "url": "https://www.audiomotorsports.com/reviews/",
      "name": "Customer Reviews | Audio MotorSports in Carson, CA",
      "description": "Google 4.8 from 654 reviews and Yelp 4.7 from 777 for Audio MotorSports in Carson, CA. Read five-star Yelp quotes on stereo, tint and dash cam installs.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/reviews/#faq",
      "url": "https://www.audiomotorsports.com/reviews/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/reviews/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is Audio MotorSports' Google rating?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Google shows Audio MotorSports at 4.8 from 654 reviews as of [CONFIRM date]. That rating is for the shop overall, not for one page. Yelp shows 4.7 from 777. Open the Google reviews listing from this page to read every review, including the full text of each five-star review."
          }
        },
        {
          "@type": "Question",
          "name": "Where do the quotes on this page come from?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The five quotes are five-star reviews from the Audio MotorSports Yelp listing, shown word for word with the name as it appears on Yelp. They cover honest pricing, a subwoofer purchase, a replacement for a factory premium stereo and a dash cam install in a 1979 VW bus. Google reviews stay on Google."
          }
        },
        {
          "@type": "Question",
          "name": "How do I leave a review?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "After your install, leave a review on Google or Yelp using the buttons at the bottom of this page. You can also call (310) 513-8800, text (213) 429-1092 or send a quote request for your next job. The shop is open Monday through Saturday, 9:30 AM to 6:00 PM."
          }
        },
        {
          "@type": "Question",
          "name": "Are these reviews for one shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Every review is for the one Audio MotorSports shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The tint, stereo, alarm, Harley bagger and Tesla sites in the network are desks in the same bay, so the ratings belong to the same shop and the same Google listing."
          }
        }
      ]
    }
  ]
}
</script>
```

### Sources and [CONFIRM] items for this page

Sources: Live /reviews/; /locations/; /tint/; /faq/.

- [CONFIRM] Replace the token [CONFIRM date] in the paragraph, in Q1 and in the JSON-LD with the same real date. The ratings (4.8 / 654, 4.7 / 777) are copied from the live page and must be re-checked on Google and Yelp the same day.
- [CONFIRM] Do not mark these counts up as aggregateRating on the business node unless the shop wants it (Google ignores self-serving ratings for local businesses); the current page does not.


---

## 8. /about/

Live URL: https://www.audiomotorsports.com/about/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `About Audio MotorSports \| Shop in Carson, CA` | 44 |
| H1 | `About the shop` | |
| Meta description | `20+ years of car stereo, window tint, car alarms and Harley audio — one Carson shop, for Los Angeles people who care how the work is done.` | 138 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `About Audio MotorSports \| Car Audio, Tint & Alarm in Carson` | 59 of 60 characters |
| Meta description | `Meet the Audio MotorSports team in Carson, CA: Zack, Nick, Alex, Richard and Albert. 20+ years of car stereo, window tint, alarms and Harley audio.` | 147 characters (target 120 to 160) |
| H1 | `About Audio MotorSports in Carson, CA` | |

### Answer-first paragraph (62 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports is a Carson, CA shop for car stereo, window tint, car alarms and Harley bagger audio, at 22025 S Avalon Blvd Ste A for 20+ years. The team is Zack, Operational Manager; Nick, sales since 1992; Alex, 3M Certified Tinter; Richard, stereo and remote start; and Albert, high-tech installer. Call (310) 513-8800, Monday to Saturday, 9:30 AM to 6:00 PM.</p>
```

### Question headings and answers (5 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">About the shop and the team</h2>
  <h3>Who works at Audio MotorSports?</h3>
  <p>The shop team goes by first names. Zack is Operational Manager and backs up Nick in sales. Nick has handled sales since 1992. Alex is the 3M Certified Tinter. Richard does stereo and remote start, classics and Harley baggers, and has been in the trade since 1998. Albert does Firstech, Compustar, iDatalink and ZZ2 CarPlay work.</p>
  <h3>Who should I contact for sales or operations?</h3>
  <p>Ask for Nick on sales. He has handled sales since 1992 and answers the quote and the walk-in. Zack is Operational Manager and makes sure the job is complete, delivered and you leave satisfied. Call (310) 513-8800 or text (213) 429-1092.</p>
  <h3>What does Audio MotorSports work on?</h3>
  <p>Four specialties: car stereo, window tint, car alarm and security, and Harley bagger audio. Dash cameras sit with the alarm work. The shop does not do wraps, wheels, tires, auto glass repair or suspension work. If it cannot help, it points you in the right direction.</p>
  <h3>Where is the shop and when is it open?</h3>
  <p>Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745, open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800. It is one shop with one bay. The other brand sites are desks in the same bay, not separate shops.</p>
  <h3>How long has Audio MotorSports been in business?</h3>
  <p>The shop describes itself as 20+ years serving Los Angeles people who care about how the work is done, in one Carson building. Harley bagger audio has been built in-house as AMS Pods since 2003. Nick has handled sales since 1992 and Richard has been in the trade since 1998.</p>
</section>
```

Where each answer comes from (live pages only):

- Who works at Audio MotorSports?: /about/ team section
- Who should I contact for sales or operations?: /faq/ 'Who should I contact for sales vs ops?'; /about/ team
- What does Audio MotorSports work on?: /about/ 'The shop'; /faq/ 'What services do you specialize in?'
- Where is the shop and when is it open?: /about/ 'Come by'; /locations/ FAQ
- How long has Audio MotorSports been in business?: /about/ intro; /faq/ 'Do you build Harley bagger audio?'; /faq/ 'What services do you specialize in?'

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": [
        "WebPage",
        "AboutPage"
      ],
      "@id": "https://www.audiomotorsports.com/about/#webpage",
      "url": "https://www.audiomotorsports.com/about/",
      "name": "About Audio MotorSports | Car Audio, Tint & Alarm in Carson",
      "description": "Meet the Audio MotorSports team in Carson, CA: Zack, Nick, Alex, Richard and Albert. 20+ years of car stereo, window tint, alarms and Harley audio.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "primaryImageOfPage": "https://www.audiomotorsports.com/assets/img/about/ams-shop-dusk.jpg",
      "mainEntity": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mentions": [
        {
          "@id": "https://www.audiomotorsports.com/about/#zack"
        },
        {
          "@id": "https://www.audiomotorsports.com/about/#nick"
        },
        {
          "@id": "https://www.audiomotorsports.com/about/#alex"
        },
        {
          "@id": "https://www.audiomotorsports.com/about/#richard"
        },
        {
          "@id": "https://www.audiomotorsports.com/about/#albert"
        }
      ]
    },
    {
      "@type": "Person",
      "@id": "https://www.audiomotorsports.com/about/#zack",
      "name": "Zack",
      "jobTitle": "Operational Manager",
      "worksFor": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "Person",
      "@id": "https://www.audiomotorsports.com/about/#nick",
      "name": "Nick",
      "jobTitle": "Sales",
      "worksFor": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "Person",
      "@id": "https://www.audiomotorsports.com/about/#alex",
      "name": "Alex",
      "jobTitle": "3M Certified Tinter",
      "worksFor": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "Person",
      "@id": "https://www.audiomotorsports.com/about/#richard",
      "name": "Richard",
      "jobTitle": "Stereo and Remote Start",
      "worksFor": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "Person",
      "@id": "https://www.audiomotorsports.com/about/#albert",
      "name": "Albert",
      "jobTitle": "High-Tech Installer",
      "worksFor": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/about/#faq",
      "url": "https://www.audiomotorsports.com/about/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/about/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Who works at Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The shop team goes by first names. Zack is Operational Manager and backs up Nick in sales. Nick has handled sales since 1992. Alex is the 3M Certified Tinter. Richard does stereo and remote start, classics and Harley baggers, and has been in the trade since 1998. Albert does Firstech, Compustar, iDatalink and ZZ2 CarPlay work."
          }
        },
        {
          "@type": "Question",
          "name": "Who should I contact for sales or operations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ask for Nick on sales. He has handled sales since 1992 and answers the quote and the walk-in. Zack is Operational Manager and makes sure the job is complete, delivered and you leave satisfied. Call (310) 513-8800 or text (213) 429-1092."
          }
        },
        {
          "@type": "Question",
          "name": "What does Audio MotorSports work on?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Four specialties: car stereo, window tint, car alarm and security, and Harley bagger audio. Dash cameras sit with the alarm work. The shop does not do wraps, wheels, tires, auto glass repair or suspension work. If it cannot help, it points you in the right direction."
          }
        },
        {
          "@type": "Question",
          "name": "Where is the shop and when is it open?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Audio MotorSports is at 22025 S Avalon Blvd Ste A, Carson, CA 90745, open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800. It is one shop with one bay. The other brand sites are desks in the same bay, not separate shops."
          }
        },
        {
          "@type": "Question",
          "name": "How long has Audio MotorSports been in business?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The shop describes itself as 20+ years serving Los Angeles people who care about how the work is done, in one Carson building. Harley bagger audio has been built in-house as AMS Pods since 2003. Nick has handled sales since 1992 and Richard has been in the trade since 1998."
          }
        }
      ]
    }
  ]
}
</script>
```

This graph replaces the live `AboutPage` block (it keeps `primaryImageOfPage` and adds the five Person nodes). Names and titles are exactly as shown on /about/; no surnames, photos or profile links are added.

### Sources and [CONFIRM] items for this page

Sources: Live /about/ (team and intro); /faq/; /locations/.

- [CONFIRM] Live page has no Person markup at all (only BreadcrumbList and AboutPage). The draft adds Person nodes for the five first names with the job titles shown on the page; no surnames, images or sameAs are added.
- [CONFIRM] '20+ years' is the site's own claim; /tint/ also shows 'Since 2003'. Confirm the founding year before adding foundingDate.


---

## 9. /services/remote-start/

Live URL: https://www.audiomotorsports.com/services/remote-start/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Remote Start \| Audio MotorSports` | 32 |
| H1 | `Remote Start` | |
| Meta description | `A warm car in winter, a cool one in August — without leaving a hole in your security. Serving Los Angeles, Long Beach and Orange County. Call (310) 513-8800.` | 157 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Remote Start Installation in Carson, CA \| Audio MotorSports` | 59 of 60 characters |
| Meta description | `Remote start installed in Carson with the vehicle-specific bypass module, every safety lockout wired, and cold and warm start tests. Call (310) 513-8800.` | 153 characters (target 120 to 160) |
| H1 | `Remote start installation in Carson, CA` | |

### Answer-first paragraph (64 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports installs remote start at 22025 S Avalon Blvd Ste A, Carson, CA. Remote start is not a plug-in: the shop installs the vehicle-specific bypass module the manufacturer intends, wires every safety lockout, and runs cold and warm start cycles before you get the keys. Add DroneMobile or Viper SmartStart for phone control. Call (310) 513-8800 or text (213) 429-1092 for a quote.</p>
```

### Question headings and answers (6 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Remote start questions answered</h2>
  <h3>Is remote start a plug-in?</h3>
  <p>No. Your car has an immobilizer built to stop it starting without the key. We install the vehicle-specific bypass module the manufacturer intends, program it to your car, and wire every safety lockout: brake shutdown, hood-open, in-gear. Then we run cold and warm start cycles before you get the keys.</p>
  <h3>Can I start my car from my phone?</h3>
  <p>Yes. Add DroneMobile or Viper SmartStart and the whole system lives on your phone from anywhere. Proximity lock and unlock is the other add: the car locks as you walk away and unlocks as you walk up, hands full. Compustar is installed in the Carson bay, and Nick quotes it for your vehicle.</p>
  <h3>Does remote start leave a hole in my security?</h3>
  <p>Not when it is done right. Your car has an immobilizer built to stop it starting without the key, and getting around it the wrong way leaves a security hole. The shop uses the vehicle-specific bypass module, so you get the convenience and you still have an immobilizer.</p>
  <h3>Which vehicles get the most from remote start?</h3>
  <p>Big engines, trucks and diesels are where remote start earns its money. So is any car that lives outside. A warm car in winter, a cool one in August. Call or message with the year, make and model for a quote on your vehicle, and ask for Nick.</p>
  <h3>How much does remote start cost?</h3>
  <p>Compustar 9910 remote start starts at $499 installed on most cars, verified September 2026. The final price depends on the vehicle and options such as DroneMobile, Viper SmartStart or proximity lock, so call or text with the year, make and model. A payment plan is available.</p>
  <h3>Can I pay for remote start over time?</h3>
  <p>Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept.</p>
</section>
```

Where each answer comes from (live pages only):

- Is remote start a plug-in?: Live /services/remote-start/ FAQ Q1 (punctuation only)
- Can I start my car from my phone?: Live FAQ Q2 + page body ('Compustar in our Carson bay')
- Does remote start leave a hole in my security?: Live page body paragraph 1-2
- Which vehicles get the most from remote start?: Live page body ('Big engines, trucks and diesels...'; hero line; CTA)
- How much does remote start cost?: /faq/ 'Do you publish prices online?'; live llms.txt; /payment-plan/ (page itself shows no price)
- Can I pay for remote start over time?: /payment-plan/

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.audiomotorsports.com/services/remote-start/#webpage",
      "url": "https://www.audiomotorsports.com/services/remote-start/",
      "name": "Remote Start Installation in Carson, CA | Audio MotorSports",
      "description": "Remote start installed in Carson with the vehicle-specific bypass module, every safety lockout wired, and cold and warm start tests. Call (310) 513-8800.",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/services/remote-start/#faq",
      "url": "https://www.audiomotorsports.com/services/remote-start/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/services/remote-start/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is remote start a plug-in?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Your car has an immobilizer built to stop it starting without the key. We install the vehicle-specific bypass module the manufacturer intends, program it to your car, and wire every safety lockout: brake shutdown, hood-open, in-gear. Then we run cold and warm start cycles before you get the keys."
          }
        },
        {
          "@type": "Question",
          "name": "Can I start my car from my phone?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Add DroneMobile or Viper SmartStart and the whole system lives on your phone from anywhere. Proximity lock and unlock is the other add: the car locks as you walk away and unlocks as you walk up, hands full. Compustar is installed in the Carson bay, and Nick quotes it for your vehicle."
          }
        },
        {
          "@type": "Question",
          "name": "Does remote start leave a hole in my security?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Not when it is done right. Your car has an immobilizer built to stop it starting without the key, and getting around it the wrong way leaves a security hole. The shop uses the vehicle-specific bypass module, so you get the convenience and you still have an immobilizer."
          }
        },
        {
          "@type": "Question",
          "name": "Which vehicles get the most from remote start?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Big engines, trucks and diesels are where remote start earns its money. So is any car that lives outside. A warm car in winter, a cool one in August. Call or message with the year, make and model for a quote on your vehicle, and ask for Nick."
          }
        },
        {
          "@type": "Question",
          "name": "How much does remote start cost?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Compustar 9910 remote start starts at $499 installed on most cars, verified September 2026. The final price depends on the vehicle and options such as DroneMobile, Viper SmartStart or proximity lock, so call or text with the year, make and model. A payment plan is available."
          }
        },
        {
          "@type": "Question",
          "name": "Can I pay for remote start over time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept."
          }
        }
      ]
    }
  ]
}
</script>
```

### Sources and [CONFIRM] items for this page

Sources: Live /services/remote-start/; /faq/; /payment-plan/; live llms.txt.

- [CONFIRM] The page itself shows no price. The $499 figure comes from /faq/, /payment-plan/ and live llms.txt ('starts at / starting at $499 installed, most cars'); /alarm/blog/viper-vs-compustar/ schema says 'is $499'. Confirm model and wording.
- [CONFIRM] Live page has no Spanish twin: /es/services/remote-start/ returns 404 (nothing to link with hreflang).


---

## 10. /locations/

Live URL: https://www.audiomotorsports.com/locations/  (fetched 2026-10-07, HTTP 200)

### Current on the live page (verbatim)

| Field | Live value | Length |
|---|---|---|
| Title | `Drive-in Locations \| One Avalon Shop \| Audio MotorSports` | 56 |
| H1 | `One Avalon shop. One hundred twenty-three drive-ins.` | |
| Meta description | `One Avalon bay. Drive in from the harbor, South Bay, Long Beach, inland, and Orange County for stereo, 3M tint, and car alarm. Call (310) 513-8800.` | 147 |

### Proposed head and H1

| Field | Proposed | Check |
|---|---|---|
| Title | `Areas Served: 123 Drive-In Cities \| Audio MotorSports Carson` | 60 of 60 characters |
| Meta description | `One Carson shop at 22025 S Avalon Blvd. Drive in from the harbor, South Bay, Long Beach, inland and Orange County for stereo, tint and alarms. (310) 513-8800` | 157 characters (target 120 to 160) |
| H1 | `One Carson shop, 123 drive-in cities` | |

### Answer-first paragraph (60 words; place directly under the H1)

```html
<p class="answer-first">Audio MotorSports has one shop, at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The 123 city pages on this site are drive-ins to that one bay, not separate storefronts, grouped by area from Harbor and South Bay to Long Beach, Inland, Westside and Orange County. Call (310) 513-8800 and text the year, make and model before you leave.</p>
```

### Question headings and answers (5 questions, 40 to 60 words each)

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Drive-in questions answered</h2>
  <h3>Where is Audio MotorSports?</h3>
  <p>One bay at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The shop is open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick; Zack runs the floor. Google Maps pins that address only, because there is no second location.</p>
  <h3>Do you have a shop in each of these cities?</h3>
  <p>No. The 123 tiles are 123 drive-ins to one Carson shop, not a storefront in each city. Pick the city you leave from and the tile shows the drive. Stereo, tint and alarm work is done at the same Carson bay, and the shop does no mobile installs.</p>
  <h3>What happens under one roof at the Carson shop?</h3>
  <p>Car stereo at LA Car Beats, window tint at LA Car Tint, and car alarm at LA Car Alarm. They are desks in the same bay with the same crew and the same address, not separate shops. Harley bagger audio is AMS Pods, and Tesla glass is Tesla Tint LA.</p>
  <h3>How much is sedan window tint?</h3>
  <p>Solar starts at $249 installed and Solar Ceramic starts at $329 installed for a four-door sedan: four doors plus the back window, no windshield. 3M Ceramic IR and Color Stable are a counter quote. Prices verified September 2026. Tint slots are 10:00 AM or 12:00 PM.</p>
  <h3>Can I pay for a job over time?</h3>
  <p>Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept.</p>
</section>
```

Where each answer comes from (live pages only):

- Where is Audio MotorSports?: Live /locations/ FAQ Q1
- Do you have a shop in each of these cities?: Live /locations/ FAQ Q2; /faq/ 'Do you do mobile installs?'
- What happens under one roof at the Carson shop?: Live /locations/ FAQ Q3 + Q8; /faq/ 'What services do you specialize in?'
- How much is sedan window tint?: Live /locations/ FAQ Q4; /faq/; live llms.txt
- Can I pay for a job over time?: /payment-plan/

### JSON-LD (copy-ready; the FAQPage text equals the visible text above, character for character)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": [
        "WebPage",
        "CollectionPage"
      ],
      "@id": "https://www.audiomotorsports.com/locations/#webpage",
      "url": "https://www.audiomotorsports.com/locations/",
      "name": "Areas Served: 123 Drive-In Cities | Audio MotorSports Carson",
      "description": "One Carson shop at 22025 S Avalon Blvd. Drive in from the harbor, South Bay, Long Beach, inland and Orange County for stereo, tint and alarms. (310) 513-8800",
      "inLanguage": "en-US",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/#website"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "publisher": {
        "@id": "https://www.audiomotorsports.com/#business"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.audiomotorsports.com/locations/#faq",
      "url": "https://www.audiomotorsports.com/locations/",
      "isPartOf": {
        "@id": "https://www.audiomotorsports.com/locations/#webpage"
      },
      "about": {
        "@id": "https://www.audiomotorsports.com/#business"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Where is Audio MotorSports?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "One bay at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The shop is open Monday through Saturday, 9:30 AM to 6:00 PM and closed Sunday. Call (310) 513-8800 and ask for Nick; Zack runs the floor. Google Maps pins that address only, because there is no second location."
          }
        },
        {
          "@type": "Question",
          "name": "Do you have a shop in each of these cities?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. The 123 tiles are 123 drive-ins to one Carson shop, not a storefront in each city. Pick the city you leave from and the tile shows the drive. Stereo, tint and alarm work is done at the same Carson bay, and the shop does no mobile installs."
          }
        },
        {
          "@type": "Question",
          "name": "What happens under one roof at the Carson shop?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Car stereo at LA Car Beats, window tint at LA Car Tint, and car alarm at LA Car Alarm. They are desks in the same bay with the same crew and the same address, not separate shops. Harley bagger audio is AMS Pods, and Tesla glass is Tesla Tint LA."
          }
        },
        {
          "@type": "Question",
          "name": "How much is sedan window tint?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Solar starts at $249 installed and Solar Ceramic starts at $329 installed for a four-door sedan: four doors plus the back window, no windshield. 3M Ceramic IR and Color Stable are a counter quote. Prices verified September 2026. Tint slots are 10:00 AM or 12:00 PM."
          }
        },
        {
          "@type": "Question",
          "name": "Can I pay for a job over time?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Every job can go on a payment plan. Apply online in about two minutes with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider, and the provider shows the exact terms before you accept."
          }
        }
      ]
    }
  ]
}
</script>
```

### Sources and [CONFIRM] items for this page

Sources: Live /locations/ (all 123 tiles counted); /faq/; /payment-plan/.

- [CONFIRM] H1 count '123' was counted from the live tiles (123 'Drive in' links). Re-count if cities are added.
- [CONFIRM] '/carson/' redirects (308) to /locations/. Whether /carson/ should become its own page is a separate decision for Zack and Tom; this draft adds the Carson answer inside /locations/ instead.
- [CONFIRM] The live FAQ says 'No 0%. No credit pitch.' while /payment-plan/ advertises '100 days same as cash' and 'deferred interest' offers. Draft uses the /payment-plan/ wording only.


---

## Special case 1. /tesla/tesla-tint-carson/: the word "Avalon"

Method: the live HTML was fetched on 2026-10-07 and every occurrence of the string "Avalon" was numbered in source order (head, JSON-LD, body, footer). There are 58. Twelve are the street address "Avalon Blvd" and must never change. The other 46 are the street name used as if it were a place name (title, H1, breadcrumb, meta, FAQ questions, "from Avalon", "a Avalon Tesla owner"), and they read as a template that had "Avalon" substituted where "Carson" belongs. "Avalon" is the real street; it is not a city, and the shop is in Carson.

### 1a. The 12 occurrences that are the street address and MUST NOT change

| # | Where | Text (keep exactly) |
|---|---|---|
| 11 | JSON-LD AutoRepair node, address.streetAddress | `"22025 S Avalon Blvd Ste A"` |
| 13 | JSON-LD FAQ answer 1 (the address inside the sentence) | `22025 S Avalon Blvd Ste A · CA 90745` |
| 23 | Lead paragraph | `22025 S Avalon Blvd Ste A · CA 90745` |
| 27 | First body paragraph (bold) | `22025 S Avalon Blvd Ste A · CA 90745` |
| 29 | Second body paragraph | `22025 S Avalon Blvd Ste A · CA 90745` |
| 37 | Route paragraph, first address | `22025 S Avalon Blvd Ste A · CA 90745` |
| 40 | Route paragraph, 'Maps pin' address | `22025 S Avalon Blvd Ste A · CA 90745` |
| 46 | 'The bay' card address block | `22025 S Avalon Blvd Ste A (line break) CA 90745` |
| 48 | 'The bay' card, directions line | `22025 S Avalon Blvd Ste A · CA 90745` |
| 52 | FAQ question 1 answer, visible | `22025 S Avalon Blvd Ste A · CA 90745` |
| 57 | Hours/NAP block (hub-nap) | `22025 S Avalon Blvd Ste A, Carson, CA 90745` |
| 58 | Site footer | `22025 S Avalon Blvd Ste A, Carson, CA 90745` |

Allowed, and recommended, around those 12: the page writes the address as `22025 S Avalon Blvd Ste A · CA 90745` (no city) in nine places while the footer and the rest of the site write `22025 S Avalon Blvd Ste A, Carson, CA 90745`. Adding `Carson,` and replacing ` · ` with `, ` makes the address match the site-wide NAP. The words "Avalon Blvd" never change.

Do not run a find-and-replace on "Avalon". It would turn the address into "22025 S Carson Blvd", which is wrong and breaks name, address and phone consistency on the one page meant to rank for Carson.

### 1b. The 46 city-name uses, before and after

Rows are grouped by element; the # column lists the occurrence numbers each row covers (all 46 are covered, none twice). "Street shorthand" means the text says "on Avalon" meaning the street, which reads as a place name; it is reworded to "in Carson, at 22025 S Avalon Blvd".

| # | Where | Before (live, verbatim) | After (proposed) | Type |
|---|---|---|---|---|
| 1, 4, 7 | Title, og:title, twitter:title | Tesla Window Tint Avalon \| Tesla Tint LA | Tesla Window Tint in Carson, CA \| Tesla Tint LA | city placeholder |
| 2, 3, 5, 6, 8, 9 | Meta description, og:description, twitter:description (two uses in each) | Tesla window tint for Avalon — Solar Ceramic and 3M IR Ceramic on Avalon. Ask for Nick. (310) 513-8800. | Tesla window tint in Carson, CA: hand-cut Solar Ceramic and 3M IR Ceramic at 22025 S Avalon Blvd Ste A. Ask for Nick. Call (310) 513-8800. | city placeholder (first use), street shorthand (second use) |
| 10 | BreadcrumbList JSON-LD, item 3 name | Tesla Window Tint for Avalon | Tesla Window Tint in Carson, CA | city placeholder |
| 19 | Visible breadcrumb | Home / Locations / Avalon | Home / Locations / Carson | city placeholder |
| 17, 18 | Hero image alt text | Tesla window tint for Avalon — Tesla Tint LA at Audio MotorSports on Avalon | Tesla window tint in Carson, CA — Tesla Tint LA at Audio MotorSports | city placeholder (first), street shorthand (second) |
| 20 | H1 | Tesla Window Tint for Avalon | Tesla Window Tint in Carson, CA | city placeholder |
| 21, 22, 24 | Lead paragraph under H1 (superseded by the answer-first paragraph if that is adopted) | The bay is on Avalon. Tesla Tint LA is the Tesla window-tint side of Audio MotorSports on Avalon — 22025 S Avalon Blvd Ste A · CA 90745. You are already on Avalon. Call (310) 513-8800. Ask for Nick. Zack runs the floor. | The bay is in Carson. Tesla Tint LA is the Tesla window-tint side of Audio MotorSports, at 22025 S Avalon Blvd Ste A, Carson, CA 90745. Call (310) 513-8800. Ask for Nick. Zack runs the floor. | city placeholder / street shorthand |
| 25, 26 | First body paragraph, opening sentences | The bay is on Avalon. Tesla Tint LA is the Tesla window-tint side of Audio MotorSports on Avalon — 22025 S Avalon Blvd Ste A · CA 90745. One bay. One map pin. | The bay is in Carson. Tesla Tint LA is the Tesla window-tint side of Audio MotorSports, at 22025 S Avalon Blvd Ste A, Carson, CA 90745. One bay. One map pin. | city placeholder / street shorthand |
| 28, 30, 31 | Second body paragraph | You are already on Avalon. This is not a hop. This is a walk-in on the shop street — 22025 S Avalon Blvd Ste A · CA 90745 — the same pin every other page on this site is driving toward. Two minutes if you are already on the block. If you came off the 405 or the 110, stay on Avalon until the bay is on the right. No second turn. The address is Avalon. The work is Tesla window tint. | This is the shop itself, not a drive-in. The pin is 22025 S Avalon Blvd Ste A, Carson, CA 90745, the same pin every other page on this site points to. Use the Google Maps pin for that address. The shop is in Carson. The work is Tesla window tint. | city placeholder; 'stay on Avalon until the bay is on the right' and 'two minutes' are unverified directions (dropped, see [CONFIRM] list) |
| 32 | Third body paragraph | Tesla Tint LA exists so a Avalon Tesla owner can read the films, the locked numbers, and the drive without wading through a car-stereo menu. | Tesla Tint LA exists so a Carson Tesla owner can read the films, the locked numbers, and the drive without wading through a car-stereo menu. | city placeholder (also fixes 'a Avalon') |
| 33 | Fourth body paragraph, first sentences | The shop-street heat is bay heat. Avalon lots, a harbor-adjacent shimmer by noon. You do not get a freeway windshield story because you did not take a freeway. You get the same oven-cabin a daily gets when it sits on this block through a lunch hour. | A Tesla parked in the Carson sun heats up like any other car. | invented local colour (unverifiable); replaced with a plain statement. The rest of the paragraph (3M IR Ceramic, Solar Ceramic, 70% VLT fronts, glass board, micro edge) stays as is. |
| 34 | Fifth body paragraph | A Model 3 that lives two lights up Avalon and a Model S that came off the 110 are not one pattern. | A Model 3 and a Model S are not one pattern. | street-direction claim, unverifiable |
| 35, 36, 38, 39, 41 | Route paragraph | The route from Avalon: You are already on Avalon — the shop street. Roll into the bay at 22025 S Avalon Blvd Ste A · CA 90745. Alternate: If you came off the 405 or the 110, stay on Avalon until the bay is on the right. No second turn. You are already on Avalon. Maps pin 22025 S Avalon Blvd Ste A · CA 90745 · (310) 513-8800 only — there is no Avalon location. Text the year and the Tesla before you leave so Nick can park a 10:00 AM or 12:00 PM slot. | Getting here: roll into the bay at 22025 S Avalon Blvd Ste A, Carson, CA 90745. Use the Google Maps pin for that address and (310) 513-8800 only; there is one shop and no second location. Text the year and the Tesla before you leave so Nick can park a 10:00 AM or 12:00 PM slot. | city placeholder; directions unverifiable (dropped) |
| 42 | Price paragraph, first sentence | Installed prices do not change because you drove from Avalon. | The installed prices for each model are in the table below. | city placeholder; 'do not change' also conflicts with the /tesla/ promo prices (see price section) |
| 43, 44 | Closing paragraph | If you are in Avalon looking for Tesla window tint, skip the search and drive the Avalon hop, ask for Nick, and get a real quote on Solar Ceramic or 3M IR Ceramic — hand-cut, micro edge, California fronts. | If you are in Carson looking for Tesla window tint, skip the search and drive to the bay at 22025 S Avalon Blvd Ste A, ask for Nick, and get a real quote on Solar Ceramic or 3M IR Ceramic — hand-cut, micro edge, California fronts. | city placeholder |
| 45 | Closing paragraph, last sentence | One Avalon shop. Book 10:00 or 12:00. | One Carson shop. Book 10:00 or 12:00. | city placeholder |
| 47 | 'The bay' card, second paragraph | You are already on Avalon — the shop street. Roll into the bay at 22025 S Avalon Blvd Ste A · CA 90745. Ask for Nick. | Roll into the bay at 22025 S Avalon Blvd Ste A, Carson, CA 90745. Ask for Nick. | city placeholder |
| 12, 49, 50, 51 | FAQ question 1, visible (#49-51) and JSON-LD answer (#12) | Q: Is Tesla Tint LA in Avalon?  A: No. There is no Avalon Tesla tint storefront. Tesla Tint LA is the Tesla window-tint side of Audio MotorSports on Avalon — 22025 S Avalon Blvd Ste A · CA 90745. One bay. One map pin. Call (310) 513-8800. Ask for Nick. Zack runs the floor.   (JSON-LD has a different Q1: "Where is Tesla Tint LA?") | Q: Where is Tesla Tint LA in Carson?  A: see the FAQ block in page 4 (answer 1). Visible and JSON-LD now use the same question and answer. | city placeholder; the old answer 'No, there is no Avalon storefront' is wrong once Avalon is replaced by Carson, because the shop IS in Carson |
| 14, 53 | FAQ question 2 (visible and JSON-LD) | How much is Tesla window tint if I drive from Avalon? | How much is Tesla window tint in Carson? | city placeholder |
| 15, 54 | FAQ question 3 (visible and JSON-LD) | Do you tint the Tesla Model Y L from Avalon? | Do you tint the Tesla Model Y L in Carson? | city placeholder |
| 16, 55 | FAQ question 4 (visible and JSON-LD) | When can I book Tesla tint from Avalon? | When can I book Tesla tint in Carson? | city placeholder |
| 56 | Call-to-action band heading | Coming from Avalon? | Ready to tint your Tesla in Carson? | city placeholder |

### 1c. Other fixes on the same page (do not involve the word Avalon)

- Replace the BreadcrumbList block with this (item 3 name and `@id` stay valid):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.audiomotorsports.com/tesla/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Locations",
      "item": "https://www.audiomotorsports.com/tesla/locations/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Tesla Window Tint in Carson, CA",
      "item": "https://www.audiomotorsports.com/tesla/tesla-tint-carson/"
    }
  ]
}
</script>
```

- In the page's AutoRepair node, `areaServed` is `City: Los Angeles`; adding `City: Carson` is accurate. The node also repeats its own `sameAs` list inside both reviews; one list on the business node is enough.
- The page is in sitemap.xml but not linked from the /tesla/locations/ grid (the grid links /tesla/tesla-tint-west-carson/ and /tesla/tesla-tint-torrance/). Add a Carson tile or a link from /tesla/ so people and crawlers reach it. This only adds a link.
- Torrance page (/tesla/tesla-tint-torrance/): "Torrance" is correct there. It has 19 uses of "Avalon" as shorthand for the shop ("on Avalon", "One Avalon shop", "405 to Avalon") and 11 uses of "Avalon Blvd" in the address. The head, H1 and FAQ already name Torrance, so no placeholder repair is needed. The meta ends "on Avalon" (proposal above: "at 22025 S Avalon Blvd"). Directions and distances there are [CONFIRM].

---

## Special case 2. The eight pages with FAQPage schema and no (or mismatched) visible FAQ

Each live page was fetched and every schema question and answer was compared with the visible text (tags removed, quotes and dashes normalised). Result: the premise "no visible FAQ" is exact for five pages; three pages (Carson, Torrance, /faq/) do have a visible FAQ, but some answers or questions differ from the schema.

| Page | Schema Qs | Visible matches | Finding | Smaller fix |
|---|---|---|---|---|
| /tint/all-services/ | 2 | 0 of 2 | no visible FAQ | Add the 2-question block (below) |
| /tint/blog/california-70-vlt-fronts/ | 9 | 0 of 9 | no visible FAQ | Add the 9-question block (below) |
| /alarm/blog/viper-vs-compustar/ | 11 | 0 of 11 | no visible FAQ | Add the 11-question block (below) |
| /beats/brands-we-love/ | 1 | 0 of 1 | the answer is on the page as a paragraph (with contractions) but has no question heading | Add one question heading and set the schema answer to the visible paragraph (below) |
| /brands-we-love/ | 1 | 0 of 1 | same as above | same |
| /tesla/tesla-tint-carson/ | 5 | 3 of 5 | visible FAQ exists; Q1 (question and answer) and Q5 (question wording) differ | Final matched FAQ is in page 4 (replaces both) |
| /tesla/tesla-tint-torrance/ | 5 | 4 of 5 | visible FAQ exists; only Q5's wording differs ("on this site" vs "on this Tesla Tint LA page") | One-string schema edit (below) |
| /faq/ | 18 | 3 of 18 answers (all 18 questions) | questions visible; 15 schema answers are not visible (visible answers are longer) | Add the schema answer as a visible line under each heading (page 6 block) |

Why a visible block rather than a schema edit: removing the FAQPage markup would be smaller on three of the pages, but it removes content instead of improving the page. Adding the visible block is additive, and it makes the answer text available to readers and answer engines.

### /tint/all-services/

Insert before the footer call-to-action (visible text equals the existing schema, character for character):

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Services we offer</h2>
  <h3>Do you show staff photos in the gallery?</h3>
  <p>No. Gallery tiles are YouTube job thumbnails of the vehicles and film — not staff faces.</p>
  <h3>Do you publish tint prices?</h3>
  <p>No. Call (310) 513-8800 or text us for a quote. A payment plan is available.</p>
</section>
```

- [CONFIRM] Answer 2 ("Do you publish tint prices? No.") contradicts /tint/, /faq/, /locations/ and live llms.txt, which publish Solar $249 and Solar Ceramic $329. Suggested replacement for BOTH the visible block and the schema: "Starting prices are posted on the LA Car Tint page: Solar $249 and Solar Ceramic $329 installed for a four-door sedan, doors and back glass, no windshield (verified September 2026). Everything else is quoted by vehicle. Call (310) 513-8800 or text us. A payment plan is available." (verify numbers and date first)
- Answer 1 is a statement about the gallery, not about the shop; keep it only if the gallery is on this page.

### /tint/blog/california-70-vlt-fronts/

Insert before the footer call-to-action (visible text equals the existing schema, character for character):

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">California 70% VLT questions</h2>
  <h3>What's the legal window tint limit in California?</h3>
  <p>California law requires front side windows to allow at least 70% of light through (70% VLT). Windshields can only be tinted along the top 4 inches. Rear side windows and the back window have no VLT restriction — you can go as dark as you want back there. California also allows a medical exemption for people with documented conditions requiring additional UV protection, which permits darker front side windows with a physician's certification. We install to legal limits by default and will walk you through your options for the rear glass when you come in.</p>
  <h3>Does ceramic tint still reject heat if the fronts stay at 70% VLT?</h3>
  <p>Yes. Visible Light Transmission (how dark it looks) is not the same as infrared heat rejection. 3M ceramic films can reject up to 95% of IR heat per 3M, varying by film and shade, even on lighter legal fronts. That is why Los Angeles and Long Beach drivers keep the fronts legal and still feel the cabin difference. Stop by for the heat-lamp demo — no appointment needed to put your hand on it.</p>
  <h3>Do you computer-cut the film?</h3>
  <p>No. Most shops feed your vehicle year and model into a plotter and let a machine cut a generic pattern. We hand-cut every piece on a glass board, then fit it to your glass with a micro edge that sits flush to the glass line. Plotter jobs are faster. They also leave gaps at the edge or film creeping past the glass. Tesla roofs, EQS windshields, and Hummer EV polycarbonate are why the extra time matters.</p>
  <h3>Do you publish prices?</h3>
  <p>Solar is $249 and Solar Ceramic is $329 — weekly specials, hand-cut micro edge. 3M Ceramic IR and Color Stable stay quote-only. Call (310) 513-8800 or text us with the year, make, and model.</p>
  <h3>Is a payment plan available?</h3>
  <p>Yes. A payment plan is available through our payment plan partner. Apply online, then schedule the install. Decision timing is controlled by that partner, not by our shop. Nick walks you through what the payments look like. See the Payment Plan page.</p>
  <h3>Do you tint Teslas?</h3>
  <p>Yes. Model 3, Y, S, X, and Cybertruck. Ceramic film, hand-cut, including one-piece roof film when the glass allows it. Fronts stay California-legal unless you have a documented medical exemption. See Tesla Window Tint.</p>
  <h3>Does ceramic film interfere with electronics?</h3>
  <p>3M ceramic and color-stable lines are designed not to interfere with electronics the way some metalized films can. We confirm the right tier when we quote your vehicle.</p>
  <h3>How long does a tint job take?</h3>
  <p>Often same-day if you arrive at opening. Full-vehicle ceramic and Tesla roofs take longer than two front doors. Call (310) 513-8800 to hold a bay.</p>
  <h3>Where is the shop?</h3>
  <p>22025 S Avalon Blvd Ste A, Carson, CA 90745. Monday–Saturday 9:30 AM – 6:00 PM. Sunday closed. We serve Los Angeles, Long Beach, Torrance, and Orange County. We do not mobile-tint.</p>
</section>
```

- [CONFIRM] Answer 4 (prices, 'weekly specials') is not on this page and 'weekly specials' conflicts with /faq/ ('We do not invent a second price or a struck was'). See the price section.
- [CONFIRM] Answer 3 ends with 'Tesla roofs, EQS windshields, and Hummer EV polycarbonate are why the extra time matters'; none of that appears on the page or elsewhere in the fetched hub pages.
- [CONFIRM] Answer 6 mentions 'one-piece roof film when the glass allows it' and answer 8 mentions Tesla roofs taking longer; neither is on the visible page.
- Answer 1 (medical exemption) is partly on the page ('unless you have a documented medical exemption'); the 'physician's certification' wording is not.

### /alarm/blog/viper-vs-compustar/

Insert before the footer call-to-action (visible text equals the existing schema, character for character):

```html
<section class="faq" id="faq" aria-labelledby="faq-heading">
  <h2 id="faq-heading">Viper and Compustar questions</h2>
  <h3>What's the difference between Viper and Compustar?</h3>
  <p>Both are top-tier brands. We recommend the right one and feature set for your vehicle. Viper is a Diamond Certified path with SmartStart when you want Directed's ecosystem. Compustar pairs with DroneMobile for phone control with no range limit. Albert flashes Firstech / Compustar anti-theft on Chargers, Challengers, and Jeep Wranglers. Richard is Remote Start Alarm System Certified on both.</p>
  <h3>What is DroneMobile?</h3>
  <p>DroneMobile is Compustar's phone app. Start, lock, unlock, locate, and control comfort from anywhere — no fob range limit. Drone XC adds a camera module. It is not a Viper SmartStart clone; the hardware families are different. We quote Compustar plus DroneMobile together when phone control is the point.</p>
  <h3>What is the difference between an immobilizer and a siren?</h3>
  <p>A siren makes noise. An immobilizer stops the engine from starting. Relay and keyless theft do not care about a speaker in the engine bay. We spec a starter interrupt or Firstech anti-theft module so a thief with a booster does not drive away. Siren, shock sensor, and pager are still useful — they are not a substitute for an immobilizer on a Charger, Challenger, or Wrangler.</p>
  <h3>Do you publish prices?</h3>
  <p>Viper 3108V is $269 installed. Compustar 9910 is $499 installed, most cars. Other security, DroneMobile, and anti-theft stay a quote. Call (310) 513-8800 or text us with the year, make, and model.</p>
  <h3>Do you offer a payment plan?</h3>
  <p>Yes. A payment plan is available through our payment plan partner. Apply online, then schedule the install. Decision timing is controlled by that partner, not by the shop.</p>
  <h3>Who installs the system?</h3>
  <p>Richard is Remote Start Alarm System Certified — in the trade since 1998. Albert is a Firstech technician for Compustar anti-theft on Chargers, Challengers, and Jeep Wranglers. Nick handles sales. Zack runs the floor. Meet the team on About.</p>
  <h3>Will this stop a relay or keyless theft?</h3>
  <p>A siren alone will not. Relay attacks clone a nearby fob. We add an immobilizer and place the modules so the car does not start for a booster. Compustar anti-theft on Dodge and Jeep is quoted that way. Bring the year, make, and model.</p>
  <h3>Do you work on Dodge Chargers, Challengers, and Jeep Wranglers?</h3>
  <p>Yes. Those are the vehicles that get targeted in Los Angeles, Long Beach, the South Bay, and Orange County. Albert handles Firstech / Compustar anti-theft and iDatalink flashes. Generic alarm copy does not help a Charger owner — the method is specific.</p>
  <h3>Do you install GPS tracking?</h3>
  <p>Yes. Tracker plus ignition kill is a common quote on classics and on cars that already got stolen once. DroneMobile Premium adds GPS on a Compustar system. We do not publish tracker prices.</p>
  <h3>What cities do you serve?</h3>
  <p>Los Angeles, Long Beach, the South Bay, and Orange County. Torrance, Gardena, San Pedro, Harbor City, Compton, Downey, Lakewood, Cerritos, Huntington Beach, Anaheim, Santa Ana, and the rest of the South Bay and OC. Call the 310 for the bay. Text us for Nick on sales. Address and hours are on Contact.</p>
  <h3>How do I get a quote?</h3>
  <p>Call (310) 513-8800, text us, or send the form on Contact. Year, make, model, and whether you want Viper, Compustar, remote start, DroneMobile, or GPS. Same-business-day replies are typical.</p>
</section>
```

- [CONFIRM] Answer 4 says 'Compustar 9910 is $499 installed, most cars'; /faq/, /payment-plan/ and live llms.txt say 'starts at / starting at $499'. Use 'starts at'.
- [CONFIRM] Answer 9 ('Tracker plus ignition kill is a common quote on classics and on cars that already got stolen once') and answer 11 ('Same-business-day replies are typical') are not on the page or elsewhere in the fetched pages.
- Answer 10 lists Downey, Lakewood, Cerritos, Huntington Beach, Anaheim and Santa Ana; all are on /locations/.

### /beats/brands-we-love/

The answer already appears on the page as a paragraph (two short paragraphs plus the "Call" line; the "We source a part to install it in your car..." paragraph sits between them and is not part of the schema answer). Smallest fix is one heading line plus one schema string:

```html
<!-- add directly above the paragraph that starts "If you’re a fan of a brand we don’t carry" -->
<h2>What if I want a brand you do not carry?</h2>
```

Schema edit: set the one Answer `text` to the visible paragraph (the only differences today are curly apostrophes, "do not" vs "don’t", "We will" vs "We’ll" and "Monday through Saturday" vs "Mon–Sat"):

```json
{
  "@type": "Question",
  "name": "What if I want a brand you do not carry?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "If you’re a fan of a brand we don’t carry through our network, don’t hesitate to call. We’ll source it for you. One phone call and we can usually get what you want. Call (310) 513-8800. Walk-ins welcome. Mon–Sat 9:30 AM – 6:00 PM, Sunday closed. 22025 S Avalon Blvd Ste A, Carson, CA 90745."
  }
}
```

- [CONFIRM] "We source a part to install it in your car... We stand behind the install the same way we would if we were the authorized dealer" is on the page below the paragraph; it is a warranty-like promise. Keep or soften per the shop.

### /brands-we-love/

The answer already appears on the page as a paragraph (two short paragraphs plus the "Call" line; the "We source a part to install it in your car..." paragraph sits between them and is not part of the schema answer). Smallest fix is one heading line plus one schema string:

```html
<!-- add directly above the paragraph that starts "If you’re a fan of a brand we don’t carry" -->
<h2>What if I want a brand you do not carry?</h2>
```

Schema edit: set the one Answer `text` to the visible paragraph (the only differences today are curly apostrophes, "do not" vs "don’t", "We will" vs "We’ll" and "Monday through Saturday" vs "Mon–Sat"):

```json
{
  "@type": "Question",
  "name": "What if I want a brand you do not carry?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "If you’re a fan of a brand we don’t carry through our network, don’t hesitate to call. We’ll source it for you. One phone call and we can usually get what you want. Call (310) 513-8800. Walk-ins welcome. Mon–Sat 9:30 AM – 6:00 PM, Sunday closed. 22025 S Avalon Blvd Ste A, Carson, CA 90745."
  }
}
```

- [CONFIRM] "We source a part to install it in your car... We stand behind the install the same way we would if we were the authorized dealer" is on the page below the paragraph; it is a warranty-like promise. Keep or soften per the shop.

### /tesla/tesla-tint-torrance/

Smallest fix is a one-string schema edit (4 of 5 pairs already match). In the FAQPage block change question 5's `name` from "Can I get a stereo or alarm on this Tesla Tint LA page?" to the visible wording:

```json
"name": "Can I get a stereo or alarm on this site?"
```

If the richer FAQ in page 5 is adopted, the visible block and schema are replaced together and this edit is not needed.

### /tesla/tesla-tint-carson/

Visible FAQ exists; mismatches are Q1 (visible "Is Tesla Tint LA in Avalon?" with answer "No. There is no Avalon Tesla tint storefront..." vs schema "Where is Tesla Tint LA?" with a different answer) and Q5 (visible "on this site" vs schema "on this Tesla Tint LA page"). Because the Avalon-to-Carson repair changes Q1 anyway, use the matched five-question block in page 4. Do not keep the live Q1 answer: "No, there is no storefront" would become false once the city name is Carson.

### /faq/

See page 6: a visible short answer under each of the 18 headings, equal to the schema text. This is smaller than rewriting 15 schema answers to the 150-plus word visible versions, and it adds an answer-first line without removing any existing text.

---

## Special case 3. Price consistency

Compiled from live pages fetched on 2026-10-07 (and live llms.txt). Prices are copied as written; nothing is added.

### 3a. Every price statement found

| Page | Wording on the live page | Price | Date shown |
|---|---|---|---|
| / (home) | No installed-service prices. Shop-inventory tiles show part prices (for example Pioneer DMH-W3000NEX $419.99, Kenwood Excelon DMX809S $599, Viper 5908V $499.99, Kicker 51KGMDL7T122 $949.99) and four tiles say "Call to confirm"; "About 90% on the shelf. Call before you drive." | parts only | none |
| /tint/ | "Solar $249 and Solar Ceramic $329 for a four-door sedan — the doors, not the windshield." "Solar starting at $249. Solar Ceramic starting at $329." Cards: SOLAR FULL CAR "Starting · most sedans $249 installed"; SOLAR CERAMIC FULL "Starting · most sedans $329 installed"; SOLAR CERAMIC FRONTS "Two front windows · Starting · most SUVs $149 installed". Weekly special: "Solar $249 — $100 off." Tabs: "Solar Starting at $249. Full car." 3M Ceramic IR and Color Stable: quote only. Windshield: separate sale, does not use the $249 / $329 door special. Estimator default: "$398 Estimate with installation". Removal: "There is no posted removal price." | $249, $329, $149, $398 | none |
| /tesla/ | Cards, "Limited promo": SOLAR CERAMIC Y FRONTS $149 ("Matrix two fronts on a Model Y is $189 installed"); MODEL 3 four doors + 2 pockets $299 ("Matrix doors + back on a Model 3 is $369"); CYBERTRUCK 2 doors + 2 pockets $199 ("Matrix doors + back on a Cybertruck is $399"). Shop notes: Model 3 doors + back $369, windshield $189; Model Y $349 / $189; Model Y L $399 / $189; Model S $399 / $189; Model X $499 / $399; Cybertruck $399 / $399. | $149, $299, $199 promo; $189, $369, $399 matrix; $349-$499 | "Prices verified September 2026." (shop notes dated 2026-08-22 to 2026-09-26) |
| /tesla/tesla-tint-carson/ and /tesla/tesla-tint-torrance/ | "These are the locked numbers." Two fronts Solar Ceramic: Model 3, Y, S, Y L $189; X and Cybertruck $269. 3M IR Ceramic fronts $249 / $349. Doors + back Solar Ceramic: Y $349, 3 $369, S $399, Y L $399, Cybertruck $399, X $499. 3M IR Ceramic doors + back: Y $549, 3 $569, S $599, Y L $599, Cybertruck $599, X $699. Windshield Solar Ceramic: 3, S, Y, Y L $189; X and Cybertruck $399. 3M IR windshield $299 / $499. "Installed prices do not change because you drove from [city]." No mention of the promo. | $189-$699 | none |
| /faq/ | Meta: "Four pillars only, no public prices". Visible: Viper 3108V special $269 installed; Compustar 9910 starts at $499 installed on most cars; Solar starts at $249 installed; Solar Ceramic starts at $329 installed (four doors and the back glass); Dual Kicker Comp $249 box only; AMS pods start at $649 a pair; CCA kit about $50, OFC kit about $200. "We do not invent a second price or a struck was." Schema answer: "AMS pods stay a quote." | $249, $329, $269, $499, $649, $249 box | "Prices verified September 2026." |
| /llms.txt (live) | "Published prices (locked specials)": Solar starting at $249 installed (4 doors + back glass); Solar Ceramic starting at $329; 3M Ceramic IR / Color Stable quote only; Viper 3108V $269 installed ("Shop cards that show $159.99 are the part only"); Compustar 9910 starting at $499 installed, most cars; Dual Kicker Comp loaded box $249 box only, install quoted; AMS Pod pair starting at $649. | $249, $329, $269, $499, $249 box, $649 | "Prices verified September 2026." |
| Hub city pages (/torrance/, /long-beach/, /gardena/, /san-pedro/, /harbor-city/) | "Solar $249 installed or Solar Ceramic $329 installed — four doors plus the back, no windshield." "Sedan weekly specials ... Solar $249 and Solar Ceramic $329." Dual Kicker Comp: "$249 house special — box only" (Long Beach, Gardena, San Pedro, Harbor City), "$249 for the box" (Torrance). | $249, $329, $249 box | none |
| /locations/ | FAQ: "Solar $249 installed and Solar Ceramic $329 installed — four-door sedan, four doors plus the back window, no windshield." "Dual Kicker Comp loaded box is $249 box-only — install quoted." | $249, $329, $249 box | none |
| /specials/ | Pioneer W3000NEX $499 installed; Thinkware Q200 $349; Kicker Dual 12 CVS $299; Kicker CompR 12 $199; Solar Ceramic Sedan $329 ("Starting · most sedans"); Solar Ceramic Fronts $149 ("Starting · most cars"); Viper 3108V $269; Compustar 8910 $399; Solar window tint $249 "$100 off" weekly special; AMS pods "starting at $649". | $149-$499 | "Prices verified September 2026." |
| /payment-plan/ | "Solar tint starts at $249 installed. Solar Ceramic starts at $329 installed. Viper 3108V is $269 installed. Compustar 9910 starts at $499 installed on most cars. Dual Kicker Comp box is $249 for the box; install is quoted. Build Your AMS Pod starts at $649 a pair." | $249, $329, $269, $499, $249 box, $649 | none |
| /tint/faq/ | "Solar is $249 and Solar Ceramic is $329 — weekly specials, hand-cut micro edge." | $249, $329 | "Prices verified September 2026." |
| /tint/all-services/ (schema only) | "Do you publish tint prices? No. Call (310) 513-8800 or text us for a quote." | none (says no) | none |
| /tint/blog/california-70-vlt-fronts/ (schema only) | "Solar is $249 and Solar Ceramic is $329 — weekly specials" | $249, $329 | none |
| /alarm/blog/viper-vs-compustar/ (schema only) | "Viper 3108V is $269 installed. Compustar 9910 is $499 installed, most cars." | $269, $499 | none |
| /services/remote-start/ | No price on the page. | none | none |

### 3b. Conflicts

- **"No public prices" vs published prices.** /faq/ meta and og:description say "no public prices"; /tint/es/faq/ meta says "sin precios públicos"; /tint/all-services/ schema says "No" to publishing prices. The same site publishes $249 / $329 on /tint/, /faq/ (visible), /locations/, /payment-plan/, /specials/, hub city pages and live llms.txt.
- **"$100 off" and "weekly special" vs "no struck was".** /tint/ and /specials/ show Solar $249 with "$100 off" (which implies a $349 regular price shown nowhere); /faq/ says "We do not invent a second price or a struck was." Hub city pages and /tint/faq/ call the same prices "weekly specials", while /faq/ and live llms.txt call them "locked specials" and "starting at".
- **Tesla: promo vs "locked" matrix.** /tesla/ advertises $149 / $299 / $199 "Limited promo" next to $189 / $369 / $399 "Matrix"; the Carson and Torrance Tesla pages call the matrix "the locked numbers" and say "Installed prices do not change because you drove from [city]". /faq/ says "Tesla tint lives on teslatintla.com with its own model matrix" (teslatintla.com is a separate host that could not be fetched). The Cybertruck promo ($199, 2 doors + 2 pockets) and the matrix ($399, doors + back) describe different coverage; a reader cannot tell if they are the same job.
- **$149 for two front windows means three things.** /tint/: "Starting · most SUVs"; /specials/: "Starting · most cars"; /tesla/: "Limited promo" for a Model Y; while the Tesla matrix lists two fronts at $189 for Model 3, Y, S and Y L. /tint/ also says Tesla glass is handled on the Tesla site.
- **Wording of the same number.** Compustar 9910: "is $499 installed" (viper-vs-compustar schema) vs "starts at / starting at $499" (/faq/, /payment-plan/, live llms.txt, /specials/ lists a different model, Compustar 8910, at $399). AMS pods: "start at $649 a pair" (/faq/ visible, /payment-plan/, /specials/, live llms.txt) vs "AMS pods stay a quote" (/faq/ schema). Dual Kicker Comp: "$249 box only" vs "$249 house special — box only" vs "$249 for the box"; /specials/ lists a different product, Kicker Dual 12 CVS, at $299 installed.
- **Dates.** Only /tesla/, /faq/, /specials/, /tint/faq/ and live llms.txt show "Prices verified September 2026". /tint/, the home page, hub city pages, /locations/, /payment-plan/, and the Carson and Torrance Tesla pages show prices with no date.
- **"$398 Estimate with installation"** appears in /tint/ source as the estimator default with no vehicle named; it matches no other price on the site.
- **Review counts, same family of issue:** home, /tint/, /reviews/, /about/ say Google 4.8 from 654 and Yelp 4.7 from 777; /tesla/ top strip says "650+ Google reviews, 700+ Yelp reviews". No "as of" date on any of them.

### 3c. One proposed wording (use everywhere a price appears)

> Prices are installed starting prices for the vehicle and coverage named. The shop confirms the final price for your year, make and model before it books the bay. Prices last verified [CONFIRM: date].

Use it as the line under every price card and table, and as the answer's last sentence in price FAQs. Drop "weekly special", "locked special", "$100 off" and "house special" unless the shop confirms a real before price and an end date. Say "starts at" for every starting price.

### 3d. Dated table skeleton

A number is filled in only where it is identical on every page that states it (checked against all pages above). Everything else is [CONFIRM]. The Verified column is [CONFIRM] for every row because the newest date on the site is September 2026.

| Service | Vehicle and coverage | Film or product | Installed price | Verified | Where it appears today |
|---|---|---|---|---|---|
| Window tint | Four-door sedan, four doors + back glass, no windshield | Solar | starts at $249 | [CONFIRM date] | /tint/, /faq/, /locations/, /payment-plan/, /specials/, city pages, llms.txt (identical) |
| Window tint | Four-door sedan, four doors + back glass, no windshield | Solar Ceramic | starts at $329 | [CONFIRM date] | same pages (identical) |
| Window tint | Two front windows | Solar Ceramic | [CONFIRM] ($149 on /tint/ and /specials/; $189 on Tesla pages) | [CONFIRM date] | conflict, see 3b |
| Window tint | Windshield (strip or full) | any | [CONFIRM] (quote only today) | [CONFIRM date] | /tint/, /faq/ |
| Window tint | any | 3M Ceramic IR, 3M Color Stable | quote only | [CONFIRM date] | /tint/, /faq/, llms.txt (identical) |
| Tint removal | with a new tint job | n/a | [CONFIRM] (no posted price) | [CONFIRM date] | /tint/ FAQ |
| Tesla tint | Model 3 / Model Y / Model Y L / Model S / Model X / Cybertruck, each: two fronts, doors + back, windshield | Solar Ceramic and 3M IR Ceramic | [CONFIRM] all 36 cells (promo vs matrix conflict) | [CONFIRM date] | /tesla/, Carson and Torrance Tesla pages |
| Car alarm | Viper 3108V | Viper | $269 | [CONFIRM date] | /faq/, /payment-plan/, /specials/, llms.txt, viper schema (identical) |
| Remote start | Compustar 9910, most cars | Compustar | starts at $499 | [CONFIRM date] | /faq/, /payment-plan/, llms.txt (identical; viper schema says 'is') |
| Car alarm | Compustar 8910 (two-way LCD pager) | Compustar | [CONFIRM] ($399 on /specials/ only) | [CONFIRM date] | /specials/ |
| Bagger audio | AMS pod pair, about three weeks to build | AMS Pods | starts at $649 a pair | [CONFIRM date] | /faq/, /payment-plan/, /specials/, llms.txt (identical) |
| Stereo | Dual Kicker Comp loaded box, box only | Kicker | $249 box only; install quoted | [CONFIRM date] | /faq/, /locations/, /payment-plan/, city pages, llms.txt (identical) |
| Stereo | Kicker Dual 12 CVS; Kicker CompR 12; Pioneer W3000NEX; Thinkware Q200 (installed) | various | [CONFIRM] ($299, $199, $499, $349 on /specials/ only) | [CONFIRM date] | /specials/ |

Tesla price grid to fill (36 cells, all [CONFIRM]): rows Model 3, Model Y, Model Y L, Model S, Model X, Cybertruck; columns Two fronts (Solar Ceramic, 3M IR Ceramic), Doors + back (Solar Ceramic, 3M IR Ceramic), Windshield (Solar Ceramic, 3M IR Ceramic). Promo rows, if kept, need a start date, an end date and the exact coverage.

---

## Special case 4. hreflang

Checked on 2026-10-07: each URL below was requested; the Spanish twin returned 200 and its own head already lists the English page as `en`, itself as `es` and the English page as `x-default`. The English home page `/` is the only one of the hub pages checked (listed in 4b) that has a Spanish twin but no hreflang tags at all, so the two pages do not point to each other (hreflang must be reciprocal to be honored).

### 4a. Add to the `<head>` of `/` (https://www.audiomotorsports.com/)

```html
<link rel="alternate" hreflang="en" href="https://www.audiomotorsports.com/">
<link rel="alternate" hreflang="es" href="https://www.audiomotorsports.com/es/">
<link rel="alternate" hreflang="x-default" href="https://www.audiomotorsports.com/">
```

### 4b. Pages with an /es/ twin, with current status

| English URL | Spanish twin (HTTP 200) | hreflang on English page | hreflang on Spanish page |
|---|---|---|---|
| https://www.audiomotorsports.com/ | https://www.audiomotorsports.com/es/ | NONE: add 4a | present (en, es, x-default) |
| https://www.audiomotorsports.com/tint/ | https://www.audiomotorsports.com/tint/es/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/tesla/ | https://www.audiomotorsports.com/tesla/es/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/faq/ | https://www.audiomotorsports.com/es/faq/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/reviews/ | https://www.audiomotorsports.com/es/reviews/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/about/ | https://www.audiomotorsports.com/es/about/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/locations/ | https://www.audiomotorsports.com/es/locations/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/services/ | https://www.audiomotorsports.com/es/services/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/contact/ | https://www.audiomotorsports.com/es/contact/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/payment-plan/ | https://www.audiomotorsports.com/es/payment-plan/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/all-services/ | https://www.audiomotorsports.com/es/all-services/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/gallery/ | https://www.audiomotorsports.com/es/gallery/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/specials/ | https://www.audiomotorsports.com/es/specials/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/privacy-policy/ | https://www.audiomotorsports.com/es/privacy-policy/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/terms-of-service/ | https://www.audiomotorsports.com/es/terms-of-service/ | present | present (en, es, x-default) |
| https://www.audiomotorsports.com/beats/brands-we-love/ | https://www.audiomotorsports.com/beats/es/brands-we-love/ | present | present (en, es, x-default) |

Brand mounts that also have twins and tags already: /alarm/ and /alarm/es/, /beats/ and /beats/es/, /amspods/ and /amspods/es/, /tint/about/, /tint/faq/, /tint/aftercare/ (each with its /tint/es/ twin), /tesla/locations/ and /tesla/es/locations/. /stereo/ has no hreflang and no /es/ twin was found.

### 4c. Pages in the request that have NO Spanish twin (do not add hreflang)

- /services/remote-start/ (the twin /es/services/remote-start/ returns 404)
- /tesla/tesla-tint-carson/ and /tesla/tesla-tint-torrance/ (/tesla/es/tesla-tint-carson/ and /tesla/es/tesla-tint-torrance/ return 404)
- /tint/blog/california-70-vlt-fronts/ and /alarm/blog/viper-vs-compustar/ (their /es/ forms return 404), /brands-we-love/ (/es/brands-we-love/ returns 404). /tint/all-services/'s twin did not answer in the check (timeout): [CONFIRM].

### 4d. Related findings

- The hub's root-level /es/ pages are not in sitemap.xml (the sitemap lists only the brand-mount twins such as /tint/es/ and /beats/es/). Adding the root /es/ URLs to the sitemap is additive.
- The Spanish locations page keeps "Avalon" as the shop's place name ("Un solo taller en Avalon"). Apply the same Carson wording when the English /locations/ title and H1 change.
- Spanish copy was not reviewed for accuracy. [CONFIRM] with a Spanish speaker on the team before the English wording changes are mirrored.

---

## Special case 5. Clean public /llms.txt body for the hub

Copy-ready body (everything between the lines). Facts come from the live site only; links are root-relative except the sister domains and the shop host, which cannot be relative. Every hub link was requested on 2026-10-07 and returns 200 (the City of Commerce, drive-in cities JSON and sitemap links included) (links that 308-redirect on the live llms.txt, such as /services/window-tinting/, now point to their final pages).

```text
# Audio MotorSports

> Car stereo, window tint, car alarms and remote start, and Harley bagger audio in Carson, California. One shop, one bay. Open Monday to Saturday.

## Shop facts
- Business: Audio MotorSports Inc (AMS)
- Address: 22025 S Avalon Blvd Ste A, Carson, CA 90745. Avalon Blvd is the street; the city is Carson.
- Phone: (310) 513-8800
- Text: (213) 429-1092 (the line that receives texts)
- Hours: Monday to Saturday, 9:30 AM to 6:00 PM. Closed Sunday.
- All work is done in the Carson bay. No mobile installs.
- In business 20+ years.
- Tint appointment slots: 10:00 AM or 12:00 PM. Call or text to confirm a slot, or to ask whether the bay is open before you drive.

## What the shop does
- Car audio: head units, Apple CarPlay and Android Auto, speakers, amplifiers, subwoofers, DSP tuning. See [Car stereo](/stereo/).
- Window tint: 3M film, hand-cut on a glass board and never cut on the vehicle. California front side windows stay at 70% VLT. See [Window tint](/tint/).
- Tesla window tint: Model 3, Model Y, Model Y L, Model S, Model X, Cybertruck. See [Tesla tint](/tesla/).
- Vehicle security: Viper, Compustar, DroneMobile, remote start, GPS tracking, dash cameras. See [Remote start](/services/remote-start/) and [Car alarms](/alarm/).
- Harley bagger audio: AMS Pods, built in-house since 2003. See [AMS Pods](/amspods/).

## What the shop does not do
- Vehicle wraps, auto glass repair, suspension, wheels, tires or performance work.
- Mobile installation.

## Published prices (installed starting prices; the shop confirms the final price for your vehicle)
- Solar window tint: starts at $249 (four-door sedan, four doors plus back glass, no windshield)
- Solar Ceramic window tint: starts at $329 (same coverage)
- 3M Ceramic IR and 3M Color Stable: quote only
- Viper 3108V alarm: $269
- Compustar 9910 remote start: starts at $499 on most cars
- AMS Pod pair: starts at $649
- Dual Kicker Comp loaded box: $249, box only; install is quoted
- Tesla tint is quoted by model, film and glass: see [Tesla tint](/tesla/)
- Prices verified September 2026.

## Payment plan
- Apply online with Snap Finance, Koalafi, EasyPay Finance or Synchrony, then bring the approval to the counter. Approval and terms are set by the provider. See [Payment plan](/payment-plan/).

## Drive-in locations
- One shop at 22025 S Avalon Blvd Ste A, Carson, CA 90745. The city pages are drive-in pages for that one shop, not separate shops.
- [Locations](/locations/): 123 drive-in cities grouped by area (Harbor, South Bay, Long Beach area, Inland, Gateway, San Gabriel Valley, San Fernando Valley, Inland Empire, Westside, Antelope Valley, Los Angeles, Orange County).
- One URL per city: `/{slug}/`, for example [Long Beach](/long-beach/) and [Harbor City](/harbor-city/). Commerce is [City of Commerce](/city-of-commerce/).
- City list as data: [drive-in cities](/data/drive-in-cities.json)

## Best passages to quote
- [FAQ](/faq/): what stays working after a car stereo installation; whether tint is legal in California; Compustar or Viper; mobile installs; where the shop is.
- [Window tint](/tint/): hand-cut versus computer-cut film; how long tint takes; how long to keep windows up after tint.
- [California 70% VLT fronts](/tint/blog/california-70-vlt-fronts/): the front-window rule and why ceramic still rejects heat.
- [Tesla tint](/tesla/): which Tesla models the bay tints; whether ceramic affects GPS or phone signal.
- [Remote start](/services/remote-start/): why remote start is not a plug-in.
- [Viper vs Compustar](/alarm/blog/viper-vs-compustar/): the two hardware families and how the shop picks.
- [About](/about/): the team and the shop.
- [Reviews](/reviews/): Google and Yelp ratings and quotes.

## Key pages
- [Services](/services/)
- [Shop parts](https://shop.audiomotorsports.com/shop/)
- [Popular installs by vehicle](/vehicles/)
- [Current specials](/specials/)
- [Install gallery](/gallery/)
- [Contact and quote request](/contact/)
- [Blog](/blog/)

## Brand desks (same bay, same address)
- Window tint: [LA Car Tint](/tint/) (also https://www.lacartint.com/)
- Car stereo: [LA Car Beats](/beats/) (also https://www.lacarbeats.com/)
- Car alarm: [LA Car Alarm](/alarm/) (also https://www.lacaralarm.com/)
- Harley bagger audio: [AMS Pods](/amspods/) (also https://www.amspods.com/)
- Tesla tint: [Tesla Tint LA](/tesla/) (also https://teslatintla.com/)

Sitemap: /sitemap.xml
```

What changed from the live file, and why:

- Removed "Do not mention warranty." and "Do not invent terms, APR, or monthly amounts. Say payment plan. Do not quote APR, 0%, or a monthly amount." These are instructions aimed at AI readers, not facts about the shop. The payment line now states what /payment-plan/ says.
- Removed "Does not stock or recommend Rockford Fosgate" and "No subwoofer boxes fabricated from scratch" from the public body; neither is stated on the pages that were fetched. [CONFIRM] whether to restore either.
- Removed "There is no shop-city doorway page" and "Each page says the shop is not in that city" (internal wording). Replaced with a plain description of the drive-in pages.
- Removed "Locked city list: data/drive-in-cities.json (15.5 mi of Avalon plus Los Angeles, Santa Ana, Irvine)": the path was not root-relative and the radius is unverified. The JSON is now a root-relative link without the distance claim.
- Replaced the link /services/window-tinting/ (308 redirect to /tint/) with /tint/; replaced "Frequently asked questions" and other pages with the same final URLs; /shop/ redirects (308) to https://shop.audiomotorsports.com/shop/, so that final URL is used.
- Added "Avalon Blvd is the street; the city is Carson" so answer engines do not read Avalon as a city.
- Added a "Best passages to quote" section pointing at the pages and headings that answer common questions; every item was found on the live pages. Heading names are used instead of anchors because the pages have no anchor ids.
- Prices: only numbers that are identical on every page that states them are listed (see Special case 3). Tesla prices are not listed because of the promo versus matrix conflict. "Prices verified September 2026" is kept from the live file and must be re-dated after the shop re-verifies.
- Walk-in wording ("Walk-ins welcome") was removed because /tint/ says an appointment is needed; the file now says to call or text to confirm. [CONFIRM] the real policy.
- Warranty: not listed. /tint/ states "30-day written workmanship warranty on installed products. Film and hardware carry the manufacturer's own warranty." Add one factual warranty line only after the shop confirms it.
- 3M "Authorized Dealer", Viper "Diamond Certified" and the "20+ years" line are on the live site; the draft keeps "3M film" and "20+ years" and drops the certification wording until [CONFIRM]ed.

---

## [CONFIRM] checklist for the shop

Answer each line (yes / no / the right number). Nothing in this file is live until Zack and Tom review it together.

### Reviews

1. [ ] Today's Google rating and review count (live page says 4.8 from 654) and Yelp (4.7 from 777). Give the date to show next to them.
2. [ ] /tesla/ top strip says "650+ Google reviews, 700+ Yelp reviews". Keep that pattern or use the exact counts everywhere?
3. [ ] Do you want aggregateRating in the schema? (Google does not show stars for a business rating its own page; the current business nodes carry 4.8 / 654 on about 620 pages.)

### Prices (one answer per row, then a date)

4. [ ] Solar $249 and Solar Ceramic $329 for a four-door sedan (doors and back, no windshield): still correct? Date verified?
5. [ ] "$100 off" on the $249 card: is there a real regular price and an end date, or should the words go?
6. [ ] Two front windows, Solar Ceramic: $149 on /tint/ (most SUVs) and /specials/ (most cars), but $189 for Tesla Model 3, Y, S, Y L. Which is right for which vehicles?
7. [ ] Tesla: is the public price the "Limited promo" ($149 Model Y fronts, $299 Model 3, $199 Cybertruck) or the "Matrix" ($189, $369, $399 and the full grid on the Carson and Torrance pages)? If promos stay: start date, end date, exact coverage. Fill the 36-cell Tesla grid.
8. [ ] Viper 3108V $269 installed; Compustar 9910 starts at $499 installed on most cars; AMS pod pair starts at $649 (about three weeks); Dual Kicker Comp loaded box $249 box only: all still current? Is it "is $499" or "starts at $499"?
9. [ ] /specials/ shows Compustar 8910 $399, Kicker Dual 12 CVS $299, Kicker CompR 12 $199, Pioneer W3000NEX $499 installed, Thinkware Q200 $349: current?
10. [ ] Estimator default "$398 Estimate with installation" on /tint/: what vehicle and coverage does it mean?
11. [ ] Tint removal: the site says there is no posted removal price. Keep it quote-only?
12. [ ] Compustar 9910 on /faq/ and /payment-plan/ is called a "remote start"; confirm model and what the $499 includes.

### Policies

13. [ ] Appointments: /tint/ says "Yes. Book a slot or text Nick" but /faq/, /locations/ and llms.txt say "Walk-ins welcome ... before 4". Which is true for tint? For Tesla (booked slots only)?
14. [ ] Are tint appointment slots only 10:00 AM and 12:00 PM?
15. [ ] Overnight drop-off Tuesday to Thursday (drop by 6 PM): still offered?
16. [ ] Warranty: /tint/ says 30-day written workmanship warranty; llms.txt says "Do not mention warranty". What do you want public?
17. [ ] Payment plan: /faq/ and /locations/ say "No 0%. No credit pitch." while /payment-plan/ shows "100 days same as cash" (Snap, Koalafi) and Synchrony deferred interest up to twelve months. Confirm the providers (Snap Finance, Koalafi, EasyPay Finance, Synchrony) and which wording to use.
18. [ ] "Booking a slot does not take a deposit" (/tint/ FAQ, /book/ meta): still true?
19. [ ] /faq/ says the shop does not do LED lighting as a service, door locks or in-dash DVD, but /services/led-lights/ and /services/door-actuators/ exist. Which is right?
20. [ ] Claims taken from the live pages and used in drafts: "does not do wraps, wheels, tires, auto glass repair, suspension"; "no mobile installs". Keep?

### Business facts and schema

21. [ ] Which coordinates are the real pin: 33.8270 / -118.2650 (home, /tint/, locations) or 33.8270587 / -118.2641283 (Tesla pages)?
22. [ ] Email in schema: audiomotorsports@gmail.com on every page. Is there a domain mailbox to use instead?
23. [ ] priceRange "$$", foundingDate (the site shows "Since 2003" and "20+ years"), legalName "Audio MotorSports Inc": confirm before they go on the home page.
24. [ ] sameAs: confirm the seven profile URLs (Instagram, Google share link, YouTube channel, Facebook, TikTok, Yelp short link, Google Maps ftid). Decide whether the five sister domains (lacarbeats.com, lacartint.com, lacaralarm.com, amspods.com, teslatintla.com) stay in sameAs or move to subOrganization.
25. [ ] Text line (213) 429-1092: confirm it is the shop's own text number (the live FAQ says so); schema lists only (310) 513-8800.
26. [ ] Certifications and authorizations quoted on the site: 3M Authorized / Certified, Viper Diamond Certified dealer, Compustar authorized, Crutchfield preferred installer, Focal, Hertz and Kenwood Excelon authorized. Which can be stated publicly?
27. [ ] Team: first names only on /about/ (Zack Operational Manager, Nick Sales, Alex 3M Certified Tinter, Richard Stereo and Remote Start, Albert High-Tech Installer). OK to mark up as Person nodes with those titles? Alex shows "15+ years" on /tint/ and "20+ years" in the tint schema: which?
28. [ ] /tesla/ meta says "from a Tesla-owning shop": true? If not it is dropped.

### Directions and distances (not used in drafts)

29. [ ] Torrance page: "About 4.4 miles, roughly ten to fifteen minutes", "405 to Avalon, or Del Amo, Crenshaw, Torrance Blvd". /locations/ lists miles for 123 cities (West Carson 1.8 up to Lancaster 86.8) and "About 15 minutes off the 405". Confirm or give the shop's own wording.
30. [ ] Carson Tesla page: "stay on Avalon until the bay is on the right", "two lights up Avalon", "two minutes if you are already on the block", "harbor-adjacent shimmer by noon". Dropped from the draft; keep any?

### Decisions for Zack and Tom

31. [ ] Home page: H1 "Pick a skill" becomes a line above the tiles and the H1 becomes the Carson sentence. OK?
32. [ ] /carson/ redirects to /locations/. Leave as is, or add a real Carson page (additive)? This draft only adds the Carson answer to /locations/, /tint/, /tesla/ and the home page.
33. [ ] Add "Carson" to the /tint/ title and H1 (draft does)? The brand name "LA Car Tint" stays.
34. [ ] Spanish pages: have a Spanish speaker review before the English changes are mirrored; add the root /es/ pages to the sitemap?
35. [ ] llms.txt: approve the cleaned body (removed lines are listed under it); confirm the "Rockford Fosgate" and "subwoofer boxes" lines should stay out.
36. [ ] teslatintla.com: the same "Avalon" substitution almost certainly exists there (not fetched, host is blocked from the audit environment); check the same page from your own network.


---

## Limits of this draft

- Hosts other than www.audiomotorsports.com were not fetched (shop.audiomotorsports.com, lacarstereo.com, teslatintla.com apex and the other standalone brand domains are proxy-blocked or out of scope here and were not requested). teslatintla.com, lacartint.com and the others were not checked for the same issues; the brand mounts on the hub (/tint/, /tesla/, /beats/, /alarm/, /amspods/) were fetched.
- No Search Console, Google Business Profile, Rich Results Test or live AI-engine data was available; nothing here claims a ranking or rich-result outcome. Google restricts FAQ rich results, so the FAQ markup is for consistency and answer-engine readability, not stars or accordions.
- Distances, drive times, directions, certifications, review counts and all prices come from the live pages as written and are [CONFIRM] until the shop answers; where the site contradicts itself the draft leaves the item out.
- `dateModified` was not added to any JSON-LD: set it to the real apply date on each page when the change goes live.
- The `WebPage` nodes reference `https://www.audiomotorsports.com/#website`, which the home-page graph on page 1 declares; apply the home change first or drop that one property.
