#!/usr/bin/env python3
"""hub_snapshot.py - READ-ONLY snapshot of every URL in the hub sitemap.

Only issues HTTP GET requests (never POST, never follows redirects blindly: the
redirect target is recorded). Polite: max 4 concurrent, 0.2s delay per worker,
up to 3 retries on 5xx / connection reset / timeout, User-Agent AMS-audit-readonly.

Usage:
  python3 hub_snapshot.py                      # full sitemap
  python3 hub_snapshot.py --sample 60          # 60 random URLs (seeded, repeatable)
  python3 hub_snapshot.py --urls-file urls.txt # specific URLs (one per line)
  python3 hub_snapshot.py --prefix baseline_snapshot
Writes <prefix>_YYYYMMDD_HHMM.json and .csv into --outdir (default: this folder).
"""
import argparse, csv, json, os, random, re, sys, threading, time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

try:
    import requests
except ImportError:
    sys.exit("This script needs the 'requests' package: pip install requests")

UA = "AMS-audit-readonly"
SITEMAP = "https://www.audiomotorsports.com/sitemap.xml"
HUB_HOST = "www.audiomotorsports.com"
MAX_WORKERS = 4          # hard cap: never more than 4 concurrent requests
DELAY = 0.2              # seconds each worker waits before every request
RETRIES = 3              # extra attempts after the first on 5xx / reset / timeout
TIMEOUT = 30

LEAK_PHRASES = [          # (label, compiled regex)
    ("Never imply nearby", re.compile(r"never imply nearby", re.I)),
    ("Do not reverse that", re.compile(r"do not reverse that", re.I)),
    ("We do not invent", re.compile(r"we do not invent", re.I)),
    ("that is the schema aggregate only", re.compile(r"that is the schema aggregate only", re.I)),
    ("TODO", re.compile(r"\bTODO\b")),
    ("INSERT after", re.compile(r"\bINSERT after\b", re.I)),
]
# 'Avalon' that is NOT the street name 'Avalon Blvd' / 'Avalon Boulevard'
AVALON_BAD = re.compile(r"Avalon(?!\s+(?:Blvd|Boulevard)\b)", re.I)

_local = threading.local()
_print_lock = threading.Lock()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": UA, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
        _local.s = s
    return s


def polite_get(url, delay=DELAY):
    """GET without following redirects; retry 5xx / network errors. Returns (resp|None, attempts, err)."""
    err = ""
    for attempt in range(1, RETRIES + 2):
        time.sleep(delay)
        try:
            r = session().get(url, timeout=TIMEOUT, allow_redirects=False)
            if r.status_code >= 500 and attempt <= RETRIES:
                err = "HTTP %d" % r.status_code
                time.sleep(attempt * 1.5)
                continue
            return r, attempt, ""
        except (requests.ConnectionError, requests.Timeout, requests.exceptions.ChunkedEncodingError) as e:
            err = type(e).__name__ + ": " + str(e)[:120]
            if attempt <= RETRIES:
                time.sleep(attempt * 1.5)
                continue
    return None, RETRIES + 1, err


# ---------------------------------------------------------------- HTML parsing
class Page(HTMLParser):
    SKIP = {"script", "style", "noscript", "template", "svg", "head", "title"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.skip_depth = 0
        self.in_title = False
        self.in_h1 = False
        self.in_jsonld = False
        self.title = ""
        self.h1s = []
        self._h1buf = []
        self.meta = {}                 # name(lower) -> content
        self.canonicals = []
        self.hreflang = 0
        self.jsonld_raw = []
        self._jbuf = []
        self.text = []                 # visible text chunks
        self.links = []                # hrefs
        self.imgs_total = 0
        self.imgs_noalt = 0            # alt attribute absent
        self.imgs_emptyalt = 0         # alt="" (decorative, tracked, not counted as missing)
        self.alts = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            n = (a.get("name") or a.get("property") or "").lower()
            if n and n not in self.meta:
                self.meta[n] = a.get("content", "")
        elif tag == "link":
            rel = a.get("rel", "").lower().split()
            if "canonical" in rel:
                self.canonicals.append(a.get("href", ""))
            if "alternate" in rel and a.get("hreflang"):
                self.hreflang += 1
        elif tag == "script":
            if a.get("type", "").lower().strip() == "application/ld+json":
                self.in_jsonld = True
                self._jbuf = []
            else:
                self.skip_depth += 1
        elif tag in self.SKIP:
            if tag not in ("head", "title"):
                self.skip_depth += 1
        elif tag == "h1":
            self.in_h1 = True
            self._h1buf = []
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.imgs_total += 1
            if "alt" not in a:
                self.imgs_noalt += 1
            elif not a["alt"].strip():
                self.imgs_emptyalt += 1
            else:
                self.alts.append(a["alt"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            if self.in_jsonld:
                self.in_jsonld = False
                self.jsonld_raw.append("".join(self._jbuf))
            elif self.skip_depth:
                self.skip_depth -= 1
        elif tag in self.SKIP and tag not in ("head", "title"):
            if self.skip_depth:
                self.skip_depth -= 1
        elif tag == "h1" and self.in_h1:
            self.in_h1 = False
            self.h1s.append(norm("".join(self._h1buf)))

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_jsonld:
            self._jbuf.append(data)
            return
        if self.skip_depth:
            return
        if self.in_h1:
            self._h1buf.append(data)
        self.text.append(data)


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def norm_cmp(s):
    """Normalise for FAQ comparison: unify quotes/dashes, drop punctuation, lowercase."""
    s = (s or "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("&amp;", "&")
    s = re.sub(r"[^\w\s]", "", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def types_of(d):
    t = d.get("@type")
    return t if isinstance(t, list) else [t]


def analyse_html(url, body):
    p = Page(url)
    p.feed(body)
    p.close()
    text = norm(" ".join(p.text))
    title = norm(p.title)
    desc = norm(p.meta.get("description", ""))
    robots = ",".join(x for x in (p.meta.get("robots", ""), p.meta.get("googlebot", "")) if x).lower()

    # JSON-LD
    valid = invalid = 0
    types, faq_qs = [], []
    ld_text = []
    for raw in p.jsonld_raw:
        try:
            data = json.loads(raw)
            valid += 1
        except Exception:
            invalid += 1
            continue
        for d in walk(data):
            for t in types_of(d):
                if t and t not in types:
                    types.append(t)
            if "FAQPage" in types_of(d):
                for q in walk(d.get("mainEntity", [])):
                    if "Question" in types_of(q) and q.get("name"):
                        faq_qs.append(norm(str(q["name"])))
            for k in ("name", "description", "text"):
                if isinstance(d.get(k), str):
                    ld_text.append(d[k])

    # FAQ parity: each FAQPage question must appear in visible text (normalised)
    vis_norm = norm_cmp(text)
    faq_missing = [q for q in faq_qs if norm_cmp(q) not in vis_norm]

    # Leaked phrases (visible text, title, meta description, image alt text)
    haystack = " | ".join([text, title, desc] + p.alts)
    leaks = [label for label, rx in LEAK_PHRASES if rx.search(haystack)]

    # 'Avalon' outside 'Avalon Blvd' (visible text, title, meta description, h1)
    av_hay = " | ".join([text, title, desc] + p.h1s)
    av_hits = [av_hay[max(0, m.start() - 25): m.end() + 25] for m in AVALON_BAD.finditer(av_hay)]
    av_head = len(AVALON_BAD.findall(" | ".join([title, desc] + p.h1s)))   # title/meta/H1 only (high signal)
    av_ld = sum(1 for t in ld_text if AVALON_BAD.search(t))

    # Internal links
    internal = set()
    internal_total = 0
    for h in p.links:
        h = h.strip()
        if not h or h.startswith(("#", "mailto:", "tel:", "sms:", "javascript:")):
            continue
        u = urlparse(urljoin(url, h))
        if u.scheme in ("http", "https") and u.netloc.lower() == HUB_HOST:
            internal_total += 1
            internal.add(u.path)

    return {
        "title": title,
        "meta_description": desc,
        "h1_count": len(p.h1s),
        "h1_text": " || ".join(p.h1s),
        "canonical": p.canonicals[0] if p.canonicals else "",
        "canonical_count": len(p.canonicals),
        "meta_robots": robots,
        "hreflang_count": p.hreflang,
        "jsonld_blocks": len(p.jsonld_raw),
        "jsonld_valid": valid,
        "jsonld_invalid": invalid,
        "schema_types": ";".join(types),
        "faq_questions": len(faq_qs),
        "faq_missing_count": len(faq_missing),
        "faq_missing": " || ".join(faq_missing),
        "words": len(text.split()),
        "internal_links": internal_total,
        "internal_links_unique": len(internal),
        "imgs_total": p.imgs_total,
        "imgs_missing_alt": p.imgs_noalt,
        "imgs_empty_alt": p.imgs_emptyalt,
        "leaked_phrases": ";".join(leaks),
        "avalon_misuse_count": len(av_hits),
        "avalon_in_head": av_head,
        "avalon_misuse_context": " || ".join(norm(x) for x in av_hits[:3]),
        "avalon_in_jsonld": av_ld,
    }


def fetch_one(url, delay):
    t0 = time.time()
    r, attempts, err = polite_get(url, delay)
    rec = {"url": url, "status": 0, "redirect_to": "", "x_robots_tag": "", "content_type": "",
           "attempts": attempts, "error": err, "ms": 0}
    if r is None:
        rec["ms"] = int((time.time() - t0) * 1000)
        return rec
    rec["status"] = r.status_code
    rec["error"] = "" if r.status_code < 500 else "HTTP %d after %d attempts" % (r.status_code, attempts)
    rec["x_robots_tag"] = r.headers.get("X-Robots-Tag", "")
    rec["content_type"] = r.headers.get("Content-Type", "").split(";")[0].strip()
    if 300 <= r.status_code < 400:
        loc = r.headers.get("Location", "")
        rec["redirect_to"] = urljoin(url, loc) if loc else ""
    elif r.status_code == 200 and ("html" in rec["content_type"] or not rec["content_type"]):
        try:
            rec.update(analyse_html(url, r.text))
        except Exception as e:  # never let one page kill the run
            rec["error"] = "parse error: %s" % e
    rec["ms"] = int((time.time() - t0) * 1000)
    return rec


def load_sitemap(url, seen=None):
    seen = seen or set()
    if url in seen:
        return []
    seen.add(url)
    r, _, err = polite_get(url)
    if r is None or r.status_code != 200:
        sys.exit("Could not read sitemap %s (%s)" % (url, err or (r.status_code if r else "no response")))
    root = ET.fromstring(r.content)
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = []
    if root.tag == ns + "sitemapindex":
        for loc in root.iter(ns + "loc"):
            urls += load_sitemap(loc.text.strip(), seen)
    else:
        urls = [loc.text.strip() for loc in root.iter(ns + "loc")]
    return urls


CSV_COLS = ["url", "status", "redirect_to", "title", "meta_description", "h1_count", "h1_text", "canonical",
            "canonical_count", "meta_robots", "x_robots_tag", "hreflang_count", "jsonld_blocks", "jsonld_valid",
            "jsonld_invalid", "schema_types", "faq_questions", "faq_missing_count", "faq_missing", "words",
            "internal_links", "internal_links_unique", "imgs_total", "imgs_missing_alt", "imgs_empty_alt",
            "leaked_phrases", "avalon_misuse_count", "avalon_in_head", "avalon_misuse_context", "avalon_in_jsonld",
            "content_type", "attempts", "error", "ms"]


def main():
    ap = argparse.ArgumentParser(description="Read-only snapshot of the hub sitemap.")
    ap.add_argument("--sitemap", default=SITEMAP)
    ap.add_argument("--sample", type=int, help="fetch only N random URLs (seeded)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--urls-file", help="file with URLs (one per line) instead of the sitemap")
    ap.add_argument("--workers", type=int, default=MAX_WORKERS, help="1-4 (capped at 4)")
    ap.add_argument("--delay", type=float, default=DELAY, help="seconds per worker before each request (min 0.2)")
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--prefix", default="snapshot")
    a = ap.parse_args()
    workers = max(1, min(MAX_WORKERS, a.workers))
    delay = max(DELAY, a.delay)

    if a.urls_file:
        with open(a.urls_file) as f:
            urls = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        src = "urls-file:" + a.urls_file
    else:
        urls = load_sitemap(a.sitemap)
        src = a.sitemap
    urls = list(dict.fromkeys(urls))
    total_in_sitemap = len(urls)
    sampled = False
    if a.sample and a.sample < len(urls):
        random.Random(a.seed).shuffle(urls)
        urls = sorted(urls[:a.sample])
        sampled = True
    print("Fetching %d URLs (%s%s) with %d workers, %.1fs delay ..." %
          (len(urls), src, ", SAMPLE of %d" % total_in_sitemap if sampled else "", workers, delay), flush=True)

    started = datetime.now()
    pages, done = {}, 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fetch_one, u, delay): u for u in urls}
        for f in as_completed(futs):
            rec = f.result()
            pages[rec["url"]] = rec
            done += 1
            if done % 50 == 0 or done == len(urls):
                with _print_lock:
                    bad = sum(1 for r in pages.values() if r["status"] >= 500 or r["status"] == 0)
                    print("  %d/%d done (%d errors/5xx)" % (done, len(urls), bad), flush=True)
    ended = datetime.now()

    status_counts = {}
    for r in pages.values():
        status_counts[str(r["status"])] = status_counts.get(str(r["status"]), 0) + 1
    meta = {"tool": "hub_snapshot.py", "user_agent": UA, "sitemap": src,
            "started": started.isoformat(timespec="seconds"), "ended": ended.isoformat(timespec="seconds"),
            "seconds": int((ended - started).total_seconds()), "urls_in_sitemap": total_in_sitemap,
            "urls_fetched": len(urls), "sampled": sampled, "seed": a.seed if sampled else None,
            "status_counts": status_counts}
    stamp = started.strftime("%Y%m%d_%H%M")
    os.makedirs(a.outdir, exist_ok=True)
    base = os.path.join(a.outdir, "%s_%s" % (a.prefix, stamp))
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "pages": dict(sorted(pages.items()))}, f, indent=1, ensure_ascii=False)
    with open(base + ".csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS, extrasaction="ignore")
        w.writeheader()
        for u in sorted(pages):
            w.writerow(pages[u])
    print("Status counts:", status_counts)
    print("Wrote", base + ".json")
    print("Wrote", base + ".csv")
    errs = [u for u, r in pages.items() if r["status"] == 0 or r["status"] >= 500]
    if errs:
        print("WARNING: %d URLs failed after retries (throttling?). Re-run just those with --urls-file." % len(errs))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
