# Protect list: what is healthy on the hub, keep it healthy

Source: `HUB_FIRST_PLAN.md` section 2 ("What is already healthy on the hub"). Run the harness before and after every change (see README.md). This table says which harness check covers each item and what the diff does when it breaks.

| # | Healthy today | Harness check (field in snapshot) | Diff severity if it breaks |
|---|---|---|---|
| 1 | All sitemap pages return 200 except the 33 `/shop/...` redirects (308) | `status`, `redirect_to` | **FAIL** if a previously-200 URL is not 200; REVIEW if a 308 target changes |
| 2 | Every HTML page has a unique title | `title` (duplicates: see "Manual / spot checks" below) | REVIEW on any title change |
| 3 | Every HTML page has a meta description | `meta_description` | REVIEW on any change |
| 4 | Exactly one H1 per page | `h1_count`, `h1_text` | REVIEW on any change |
| 5 | Self-canonical on every page | `canonical`, `canonical_count` | **FAIL** if the canonical changes |
| 6 | No noindex anywhere | `meta_robots`, `x_robots_tag` | **FAIL** on any new noindex (meta or header) |
| 7 | All images have alt text (6,404 images at audit) | `imgs_missing_alt` (alt attribute absent; `alt=""` is tracked separately as `imgs_empty_alt`) | REVIEW if any page gains a missing-alt image |
| 8 | JSON-LD is valid (0 invalid blocks) | `jsonld_blocks`, `jsonld_valid`, `jsonld_invalid`, `schema_types` | **FAIL** if invalid blocks increase; REVIEW if blocks or schema types are lost |
| 9 | FAQ schema matches visible FAQ text | `faq_questions`, `faq_missing_count`, `faq_missing` | REVIEW on any parity regression |
| 10 | No prompt text or placeholders leaked onto pages | `leaked_phrases` | REVIEW on any new leaked phrase |
| 11 | "Avalon" is only the street (Avalon Blvd), never a city placeholder | `avalon_in_head`, `avalon_misuse_count`, `avalon_in_jsonld` | REVIEW if title/meta/H1/JSON-LD mentions increase; body count changes are INFO |
| 12 | Name, address, phone, hours consistent | Not auto-checked by the harness (see Manual below) | n/a |
| 13 | Content not accidentally stripped by a template change | `words`, `internal_links` | REVIEW on a drop of more than 20% |
| 14 | Hreflang not accidentally introduced/removed | `hreflang_count` (home has 0 today) | REVIEW on any change |
| 15 | Sitemap membership stable | URL set in the snapshot | REVIEW if URLs vanish from or appear in the sitemap |

## Manual / spot checks the harness does NOT cover (do these by hand after a change)
- **robots.txt is open to Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot**: open `https://www.audiomotorsports.com/robots.txt` and compare with the saved copy from before the change.
- **llms.txt still exists** (`/llms.txt` returns 200).
- **HSTS still on**: in a terminal, `curl -sI https://www.audiomotorsports.com/ | grep -i strict-transport`.
- **NAP consistency** (Audio MotorSports, 22025 S Avalon Blvd Ste A, Carson, CA 90745; (310) 513-8800; Mon-Sat 9:30-18:00): view the footer and the contact page on one page of each template.
- **Unique titles across the site**: after the diff, sort the `title` column of the new CSV and look for repeats (spreadsheet: Data > Remove duplicates preview, or `cut` and `uniq -d`).
- **Visual check** of one page per template (home, a city page, a mounted brand page, `/stereo/shop/`) on phone and desktop. The harness reads HTML only; it cannot see layout, forms, or the browser console.
- **Search Console indexing**: the harness cannot tell whether Google indexes the pages; only Search Console can.
