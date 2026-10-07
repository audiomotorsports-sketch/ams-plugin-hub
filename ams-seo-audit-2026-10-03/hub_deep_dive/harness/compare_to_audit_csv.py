#!/usr/bin/env python3
"""compare_to_audit_csv.py - compare a hub_snapshot JSON to the earlier audit's pages.csv. Offline.

Usage: python3 compare_to_audit_csv.py SNAPSHOT.json PAGES.csv [--max-list 20]
Columns compared: status, redirect target, title, H1, meta description, canonical, images missing alt.
Word counts are listed only as INFO (the two tools count words differently).
"""
import argparse, csv, json, sys
from collections import defaultdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("snapshot")
    ap.add_argument("pages_csv")
    ap.add_argument("--max-list", type=int, default=20)
    a = ap.parse_args()
    snap = json.load(open(a.snapshot, encoding="utf-8"))["pages"]
    rows = {r["url"]: r for r in csv.DictReader(open(a.pages_csv, encoding="utf-8"))}
    d = defaultdict(list)
    for u in sorted(set(rows) - set(snap)):
        d["URL in audit CSV but not in current sitemap"].append((u, "audit status %s" % rows[u]["status"]))
    for u in sorted(set(snap) - set(rows)):
        d["URL in current sitemap but not in audit CSV"].append((u, "now status %s" % snap[u]["status"]))
    for u in sorted(set(rows) & set(snap)):
        r, s = rows[u], snap[u]
        if str(s["status"]) != r["status"]:
            d["status changed"].append((u, "%s -> %s" % (r["status"], s["status"])))
            continue
        if r["status"] != "200":
            if (s.get("redirect_to") or "") != r["redirect_to"]:
                d["redirect target changed"].append((u, "%s -> %s" % (r["redirect_to"], s.get("redirect_to"))))
            continue
        for col, key, cat in (("title", "title", "title changed"), ("h1", "h1_text", "H1 changed"),
                              ("meta_description", "meta_description", "meta description changed"),
                              ("canonical", "canonical", "canonical changed")):
            if (r[col] or "").strip() != (s.get(key) or "").strip():
                d[cat].append((u, "%r -> %r" % (r[col], s.get(key))))
        if str(s.get("imgs_missing_alt", 0)) != (r["imgs_missing_alt"] or "0"):
            d["images missing alt changed"].append((u, "%s -> %s" % (r["imgs_missing_alt"], s.get("imgs_missing_alt"))))
        if str(s.get("imgs_total", 0)) != (r["img_count"] or "0"):
            d["image count changed (INFO)"].append((u, "%s -> %s" % (r["img_count"], s.get("imgs_total"))))
        rw = int(r["words"] or 0)
        if rw and abs(s.get("words", 0) - rw) > max(25, rw * 0.15):
            d["word count differs >15% (INFO, methods differ)"].append((u, "%s -> %s" % (rw, s.get("words"))))
    print("Snapshot %s vs %s" % (a.snapshot, a.pages_csv))
    print("Audit CSV rows: %d | snapshot URLs: %d | in both: %d" % (len(rows), len(snap), len(set(rows) & set(snap))))
    if not d:
        print("NO DIFFERENCES")
    for cat, items in sorted(d.items(), key=lambda kv: -len(kv[1])):
        print("\n- %s: %d" % (cat, len(items)))
        for u, det in items[:a.max_list]:
            print("    %s  %s" % (u, det))
        if len(items) > a.max_list:
            print("    ... %d more" % (len(items) - a.max_list))


if __name__ == "__main__":
    sys.exit(main())
