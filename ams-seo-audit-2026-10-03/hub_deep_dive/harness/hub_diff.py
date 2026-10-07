#!/usr/bin/env python3
"""hub_diff.py - compare two hub_snapshot.py JSON files. Offline: makes no network requests.

Usage: python3 hub_diff.py BEFORE.json AFTER.json [--max-list 25] [--report diff_report.txt]
Exit code: 0 = PASS, 1 = REVIEW, 2 = FAIL.

FAIL   : a URL that was 200 is not 200 now (or errored), new noindex (meta or X-Robots-Tag),
         canonical changed, JSON-LD became invalid (more invalid blocks than before).
REVIEW : title / meta description / H1 changed, H1 count changed, lost JSON-LD, new leaked phrases,
         FAQ parity regression, more images missing alt, 'Avalon' in title/meta/H1 increased,
         hreflang changed, redirect target changed, big word-count or internal-link drops, URLs
         added/removed from the sitemap.
INFO   : smaller changes (word count, internal links, schema types, empty alt, body 'Avalon').
URLs are compared only when present in BOTH snapshots (so a --sample snapshot can be diffed
against a full one); URLs missing from one side are listed separately.
"""
import argparse, json, sys

FAIL, REVIEW, INFO = "FAIL", "REVIEW", "INFO"


def load(p):
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    return d["meta"], d["pages"]


def has_noindex(r):
    return "noindex" in (r.get("meta_robots", "") or "").lower() or "noindex" in (r.get("x_robots_tag", "") or "").lower()


def labels(s):
    return set(x for x in (s or "").split(";") if x)


def compare(old, new):
    findings = []  # (severity, category, url, detail)

    def add(sev, cat, url, detail):
        findings.append((sev, cat, url, detail))

    for url in sorted(set(old) & set(new)):
        o, n = old[url], new[url]
        os_, ns = o.get("status", 0), n.get("status", 0)
        if os_ == 200 and ns != 200:
            extra = (" (%s)" % n["error"]) if n.get("error") else ""
            if ns == 0 or ns >= 500:
                extra += " - may be transient; re-run this URL with --urls-file before trusting"
            add(FAIL, "stopped returning 200", url, ("%s -> %s%s %s" % (os_, ns, extra, n.get("redirect_to", ""))).strip())
            continue
        if os_ != 200 and ns == 200:
            add(INFO, "now returns 200", url, "%s -> 200" % os_)
        elif os_ != ns:
            add(REVIEW, "status changed (non-200)", url, "%s -> %s" % (os_, ns))
        if ns != 200:  # both non-200 (e.g. the 308 shop redirects)
            if 300 <= ns < 400 and o.get("redirect_to", "") != n.get("redirect_to", ""):
                add(REVIEW, "redirect target changed", url, "%s -> %s" % (o.get("redirect_to"), n.get("redirect_to")))
            continue

        # new noindex
        if has_noindex(n) and not has_noindex(o):
            add(FAIL, "NEW noindex", url, "meta_robots=%r x_robots_tag=%r" % (n.get("meta_robots"), n.get("x_robots_tag")))
        if os_ == 200 and o.get("canonical", "") != n.get("canonical", ""):
            add(FAIL, "canonical changed", url, "%r -> %r" % (o.get("canonical"), n.get("canonical")))
        if n.get("jsonld_invalid", 0) > o.get("jsonld_invalid", 0):
            add(FAIL, "JSON-LD became invalid", url, "invalid blocks %s -> %s" % (o.get("jsonld_invalid", 0), n.get("jsonld_invalid", 0)))
        if os_ != 200:
            continue

        for field, cat in (("title", "title changed"), ("meta_description", "meta description changed"), ("h1_text", "H1 changed")):
            if o.get(field, "") != n.get(field, ""):
                add(REVIEW, cat, url, "%r -> %r" % (o.get(field, ""), n.get(field, "")))
        if o.get("h1_count") != n.get("h1_count"):
            add(REVIEW, "H1 count changed", url, "%s -> %s" % (o.get("h1_count"), n.get("h1_count")))
        if n.get("jsonld_valid", 0) < o.get("jsonld_valid", 0) and n.get("jsonld_invalid", 0) <= o.get("jsonld_invalid", 0):
            add(REVIEW, "lost JSON-LD", url, "valid blocks %s -> %s" % (o.get("jsonld_valid"), n.get("jsonld_valid")))
        lost_types = labels(o.get("schema_types")) - labels(n.get("schema_types"))
        if lost_types:
            add(REVIEW, "schema types lost", url, ", ".join(sorted(lost_types)))
        gained = labels(n.get("schema_types")) - labels(o.get("schema_types"))
        if gained:
            add(INFO, "schema types added", url, ", ".join(sorted(gained)))
        new_leaks = labels(n.get("leaked_phrases")) - labels(o.get("leaked_phrases"))
        if new_leaks:
            add(REVIEW, "NEW leaked phrase visible", url, ", ".join(sorted(new_leaks)))
        gone_leaks = labels(o.get("leaked_phrases")) - labels(n.get("leaked_phrases"))
        if gone_leaks:
            add(INFO, "leaked phrase removed", url, ", ".join(sorted(gone_leaks)))
        if n.get("faq_missing_count", 0) > o.get("faq_missing_count", 0):
            add(REVIEW, "FAQ parity regression", url, "FAQ questions not in visible text %s -> %s: %s" %
                (o.get("faq_missing_count", 0), n.get("faq_missing_count", 0), (n.get("faq_missing") or "")[:200]))
        if o.get("faq_questions", 0) and n.get("faq_questions", 0) < o.get("faq_questions", 0):
            add(REVIEW, "FAQ questions lost from schema", url, "%s -> %s" % (o.get("faq_questions"), n.get("faq_questions")))
        if n.get("imgs_missing_alt", 0) > o.get("imgs_missing_alt", 0):
            add(REVIEW, "more images missing alt", url, "%s -> %s" % (o.get("imgs_missing_alt", 0), n.get("imgs_missing_alt", 0)))
        if n.get("avalon_in_head", 0) > o.get("avalon_in_head", 0):
            add(REVIEW, "'Avalon' (not Avalon Blvd) in title/meta/H1 increased", url, "%s -> %s" % (o.get("avalon_in_head", 0), n.get("avalon_in_head", 0)))
        elif n.get("avalon_misuse_count", 0) != o.get("avalon_misuse_count", 0):
            add(INFO, "body 'Avalon' mentions changed", url, "%s -> %s" % (o.get("avalon_misuse_count", 0), n.get("avalon_misuse_count", 0)))
        if n.get("avalon_in_jsonld", 0) > o.get("avalon_in_jsonld", 0):
            add(REVIEW, "'Avalon' in JSON-LD text increased", url, "%s -> %s" % (o.get("avalon_in_jsonld", 0), n.get("avalon_in_jsonld", 0)))
        if o.get("hreflang_count", 0) != n.get("hreflang_count", 0):
            add(REVIEW, "hreflang count changed", url, "%s -> %s" % (o.get("hreflang_count", 0), n.get("hreflang_count", 0)))
        if o.get("canonical_count", 1) != n.get("canonical_count", 1):
            add(REVIEW, "canonical tag count changed", url, "%s -> %s" % (o.get("canonical_count"), n.get("canonical_count")))
        if (o.get("meta_robots") or "") != (n.get("meta_robots") or "") and not (has_noindex(n) and not has_noindex(o)):
            add(REVIEW, "meta robots changed", url, "%r -> %r" % (o.get("meta_robots"), n.get("meta_robots")))
        if (o.get("x_robots_tag") or "") != (n.get("x_robots_tag") or "") and not (has_noindex(n) and not has_noindex(o)):
            add(REVIEW, "X-Robots-Tag changed", url, "%r -> %r" % (o.get("x_robots_tag"), n.get("x_robots_tag")))
        ow, nw = o.get("words", 0), n.get("words", 0)
        if ow and nw < ow * 0.8:
            add(REVIEW, "word count dropped >20%", url, "%s -> %s" % (ow, nw))
        elif ow and abs(nw - ow) > max(10, ow * 0.05):
            add(INFO, "word count changed", url, "%s -> %s" % (ow, nw))
        ol, nl = o.get("internal_links", 0), n.get("internal_links", 0)
        if ol and nl < ol * 0.8:
            add(REVIEW, "internal links dropped >20%", url, "%s -> %s" % (ol, nl))
        elif ol != nl:
            add(INFO, "internal link count changed", url, "%s -> %s" % (ol, nl))
        if o.get("imgs_empty_alt", 0) != n.get("imgs_empty_alt", 0):
            add(INFO, "empty-alt image count changed", url, "%s -> %s" % (o.get("imgs_empty_alt", 0), n.get("imgs_empty_alt", 0)))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("before")
    ap.add_argument("after")
    ap.add_argument("--max-list", type=int, default=25, help="max URLs printed per category (counts are always complete)")
    ap.add_argument("--report", help="also write the full (untruncated) report to this file")
    a = ap.parse_args()
    mo, old = load(a.before)
    mn, new = load(a.after)
    findings = compare(old, new)
    only_old = sorted(set(old) - set(new))
    only_new = sorted(set(new) - set(old))
    partial = bool(mo.get("sampled") or mn.get("sampled"))
    if not partial:  # one-sided URLs only mean something when both snapshots are full
        findings += [(REVIEW, "URL not in AFTER snapshot", u, "was status %s" % old[u].get("status")) for u in only_old]
        findings += [(REVIEW, "URL new in AFTER snapshot", u, "status %s" % new[u].get("status")) for u in only_new]

    out = []
    p = out.append
    p("HUB SNAPSHOT DIFF")
    p("BEFORE: %s  (%s, %d URLs%s)" % (a.before, mo.get("started"), len(old), ", SAMPLE" if mo.get("sampled") else ""))
    p("AFTER : %s  (%s, %d URLs%s)" % (a.after, mn.get("started"), len(new), ", SAMPLE" if mn.get("sampled") else ""))
    p("Compared on %d URLs present in both." % len(set(old) & set(new)))
    if mo.get("sampled") or mn.get("sampled"):
        p("NOTE: at least one snapshot is a sample; coverage is partial (%d URLs present in only one snapshot are not listed)." % (len(only_old) + len(only_new)))
    p("")
    order = {FAIL: 0, REVIEW: 1, INFO: 2}
    for sev in (FAIL, REVIEW, INFO):
        group = [f for f in findings if f[0] == sev]
        p("=" * 78)
        p("%s: %d finding(s)" % (sev, len(group)))
        p("=" * 78)
        cats = {}
        for f in group:
            cats.setdefault(f[1], []).append(f)
        for cat, items in sorted(cats.items(), key=lambda kv: -len(kv[1])):
            p("- %s (%d URLs)" % (cat, len(items)))
            for _, _, u, d in items[:a.max_list]:
                p("    %s  %s" % (u, d))
            if len(items) > a.max_list:
                p("    ... %d more (use --max-list or --report for all)" % (len(items) - a.max_list))
        p("")
    nf = sum(1 for f in findings if f[0] == FAIL)
    nr = sum(1 for f in findings if f[0] == REVIEW)
    verdict = "FAIL" if nf else ("REVIEW" if nr else "PASS")
    p("RESULT: %s  (%d FAIL, %d REVIEW, %d INFO findings)" % (verdict, nf, nr, sum(1 for f in findings if f[0] == INFO)))
    text = "\n".join(out)
    # printed output is truncated per category; the report file is complete
    print(text)
    if a.report:
        lines = []
        for sev in (FAIL, REVIEW, INFO):
            group = [f for f in findings if f[0] == sev]
            lines.append("%s: %d" % (sev, len(group)))
            for f in group:
                lines.append("  [%s] %s | %s | %s" % (f[0], f[1], f[2], f[3]))
        with open(a.report, "w", encoding="utf-8") as fh:
            fh.write(text + "\n\nFULL LIST\n" + "\n".join(lines) + "\n")
        print("Full report written to", a.report)
    return {"PASS": 0, "REVIEW": 1, "FAIL": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
