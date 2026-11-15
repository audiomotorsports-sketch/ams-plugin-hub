# Hub regression harness (read-only)

Proves a change to www.audiomotorsports.com did not break anything. It only does HTTP GET requests, never changes a site, and never logs in or submits a form. Polite by design: at most 4 requests at once, 0.2 s pause per worker before each request, up to 3 retries on 5xx / connection reset / timeout, User-Agent `AMS-audit-readonly`.

Files in this folder
- `hub_snapshot.py` takes a snapshot (JSON + CSV) of every URL in the sitemap.
- `hub_diff.py` compares two snapshots and prints PASS / REVIEW / FAIL. Offline, no network.
- `compare_to_audit_csv.py` compares a snapshot to the earlier audit `pages.csv`. Offline.
- `protect_list.md` the "healthy, keep it healthy" checklist and which check covers each item.
- `baseline_snapshot_20261007_0120.json/.csv` the baseline taken 2026-10-07 (1,194 URLs). `baseline_vs_audit_pages_csv.txt` its comparison to the 2026-10-04 audit.

## Requirements
Python 3.8+ and the `requests` package (`pip install requests`; it is often already installed). Nothing else.

## Run it from your own network (Zack's or Tom's laptop)
No proxy settings are needed. Do NOT set any proxy variables; on a normal home or shop connection `requests` just connects to www.audiomotorsports.com directly. (If your company network forces a proxy, `requests` honours the usual `HTTPS_PROXY` variable, but you should not need it.)

Open a terminal in this folder, then:

```
cd ~/ams-seo-audit-2026-10-03/hub_deep_dive/harness
python3 hub_snapshot.py                    # full sitemap, about 1,200 URLs
python3 hub_snapshot.py --sample 60        # quick check: 60 random URLs (same 60 every time, --seed N to change)
python3 hub_snapshot.py --urls-file my_urls.txt   # only the pages you list, one URL per line
python3 hub_snapshot.py --prefix before_footer_fix   # name the files so you can find them later
python3 hub_diff.py BEFORE.json AFTER.json
python3 hub_diff.py BEFORE.json AFTER.json --max-list 100 --report diff_report.txt   # full detail in a file
```

Output files are written next to the script as `snapshot_YYYYMMDD_HHMM.json` and `.csv` (use `--outdir` to change). The CSV opens in any spreadsheet.

### Run time
The full sitemap (1,194 URLs) took about 100 seconds from the audit environment. Allow 2 to 6 minutes from a normal connection. A 60-URL sample takes under 10 seconds. The diff takes about a second.

### Exit codes (so you can script it)
`hub_snapshot.py`: 0 = fine, 2 = some URLs failed after 3 retries (usually throttling; re-run those with `--urls-file`). `hub_diff.py`: 0 = PASS, 1 = REVIEW, 2 = FAIL.

## Per change: snapshot before, change, snapshot after, diff
1. **Before** (right before you touch anything): `python3 hub_snapshot.py --prefix before_<what>`. If you only touch one template, a full snapshot is still best because a template change can ripple to hundreds of mounted pages.
2. **Make the change** (only after Zack and Tom have reviewed it together).
3. **After**: wait until the change is live, then `python3 hub_snapshot.py --prefix after_<what>`.
4. **Diff**: `python3 hub_diff.py before_<what>_*.json after_<what>_*.json --report diff_<what>.txt`.
5. Read the result:
   - **PASS**: nothing differs. If you expected a change, this itself is a flag (the change did not go live).
   - **REVIEW**: something changed that is allowed but must be looked at. Confirm each listed category is exactly what you intended (a deliberate title edit shows as "title changed"; an accidental one shows the same way).
   - **FAIL**: a previously-200 URL is not 200, a new noindex appeared, a canonical changed, or JSON-LD became invalid. Stop, put the saved original back, and re-snapshot. If the FAIL is "stopped returning 200" with status 0 or 5xx, it may be a throttling blip: re-run just those URLs (`--urls-file`) before concluding.
6. Keep the "after" snapshot; it becomes the "before" for the next change.

You can diff a sample against a full snapshot; only URLs in both are compared and the diff says so.

## What is checked per URL
status, redirect target (not followed), title, meta description, H1 count and text, canonical (and count), meta robots, X-Robots-Tag, hreflang count, JSON-LD blocks (count, valid, invalid, @types), FAQPage question text versus visible text (normalised: case, quotes, punctuation ignored), visible word count, internal link count, images with no `alt` attribute (`alt=""` is counted separately), leaked phrases ("Never imply nearby", "Do not reverse that", "We do not invent", "that is the schema aggregate only", "TODO", "INSERT after"), and "Avalon" not followed by Blvd/Boulevard. See `protect_list.md` for what each maps to.

## Known limits (read these)
- **Reads the raw HTML only.** It does not run JavaScript, so it cannot see content added by scripts, layout, forms, console errors, or speed.
- **FAQ parity** checks that each schema question text appears in the visible page text. It does not compare answers. FAQ text inside collapsed accordions still counts as visible (it is in the HTML); text injected by JavaScript does not.
- **"Avalon" check is a flag, not a verdict.** "Avalon" is the real street, so phrases like "bay is on Avalon" or "Avalon pin" also match. The diff only escalates to REVIEW when the count in title / meta description / H1 / JSON-LD goes up; body changes are INFO. Judge each flagged context by eye (`avalon_misuse_context` in the CSV).
- **Word counts** include header, footer and navigation (the earlier audit's `pages.csv` counted fewer words), so only compare snapshots from this tool with each other.
- Does not check robots.txt, llms.txt, HSTS, or business details; see "Manual / spot checks" in `protect_list.md`.
- Only the hub (www.audiomotorsports.com). It will not follow links to other sites.
