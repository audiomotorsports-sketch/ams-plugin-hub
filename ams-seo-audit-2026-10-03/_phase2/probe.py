#!/usr/bin/env python3
"""READ-ONLY page probe for the launch audit.

usage: probe.py OUTDIR URL [URL ...]
For each URL and for phone (390x844) + desktop (1366x900) viewports it records:
screenshot, console errors/warnings, page errors, failed requests, mixed content,
horizontal overflow, broken images, small tap targets, meta/favicon checks,
lab perf metrics (TTFB, FCP, LCP, CLS, long-task total, bytes, requests),
every link/button/CTA (text, area, href) and the HTTP status of each unique same-site link,
and every form (fields only, NEVER submitted).
Network goes through the session proxy; TLS verification stays ON.
"""
import asyncio, json, os, re, sys, urllib.parse
from playwright.async_api import async_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
VIEWS = {
    'phone': dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True,
                  user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'),
    'desktop': dict(viewport={'width': 1366, 'height': 900}),
}

PERF_JS = """
() => new Promise(res => {
  const out = {lcp:0, cls:0, longtask_ms:0};
  try { new PerformanceObserver(l => { for (const e of l.getEntries()) out.lcp = e.startTime; }).observe({type:'largest-contentful-paint', buffered:true}); } catch(e){}
  try { new PerformanceObserver(l => { for (const e of l.getEntries()) if(!e.hadRecentInput) out.cls += e.value; }).observe({type:'layout-shift', buffered:true}); } catch(e){}
  try { new PerformanceObserver(l => { for (const e of l.getEntries()) out.longtask_ms += Math.max(0, e.duration-50); }).observe({type:'longtask', buffered:true}); } catch(e){}
  setTimeout(() => {
    const nav = performance.getEntriesByType('navigation')[0] || {};
    const fcp = (performance.getEntriesByName('first-contentful-paint')[0]||{}).startTime || 0;
    out.ttfb = nav.responseStart; out.fcp = fcp; out.dcl = nav.domContentLoadedEventEnd; out.load = nav.loadEventEnd;
    out.transfer_kb = Math.round(performance.getEntriesByType('resource').reduce((a,r)=>a+(r.transferSize||0),0)/1024 + (nav.transferSize||0)/1024);
    out.requests = performance.getEntriesByType('resource').length + 1;
    res(out);
  }, 2500);
})
"""

DOM_JS = """
() => {
  const abs = u => { try { return new URL(u, location.href).href } catch(e) { return null } };
  const area = el => el.closest('nav') ? 'nav' : el.closest('header') ? 'header' : el.closest('footer') ? 'footer' : el.closest('main') ? 'main' : 'body';
  const links = [...document.querySelectorAll('a[href], button, [role=button], input[type=submit]')].map(el => ({
    tag: el.tagName.toLowerCase(), text: (el.innerText || el.value || el.getAttribute('aria-label') || '').trim().replace(/\\s+/g,' ').slice(0,80),
    href: el.tagName === 'A' ? abs(el.getAttribute('href')) : null, area: area(el),
    visible: !!(el.offsetWidth || el.offsetHeight), inForm: !!el.closest('form'),
  }));
  const forms = [...document.querySelectorAll('form')].map(f => ({
    action: f.getAttribute('action'), method: f.method, id: f.id,
    fields: [...f.querySelectorAll('input,select,textarea')].map(i => ({name:i.name, type:i.type, required:i.required, label: (i.labels && i.labels[0] ? i.labels[0].innerText : i.getAttribute('aria-label')||i.placeholder||'').trim().slice(0,40)})),
    hasSubmit: !!f.querySelector('[type=submit],button:not([type=button])'),
  }));
  const m = n => (document.querySelector(`meta[name="${n}"]`)||{}).content || null;
  const p = n => (document.querySelector(`meta[property="${n}"]`)||{}).content || null;
  const icons = [...document.querySelectorAll('link[rel~=icon],link[rel=apple-touch-icon]')].map(l => ({rel:l.rel, href: abs(l.getAttribute('href'))}));
  const imgs = [...document.images];
  return {
    title: document.title, h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim().slice(0,100)),
    description: m('description'), viewport: m('viewport'), robots: m('robots'), canonical: (document.querySelector('link[rel=canonical]')||{}).href || null,
    lang: document.documentElement.lang, og: {title:p('og:title'), image:p('og:image'), url:p('og:url')},
    icons, jsonld_blocks: document.querySelectorAll('script[type="application/ld+json"]').length,
    overflow_x: document.documentElement.scrollWidth - window.innerWidth,
    broken_images: imgs.filter(i => i.complete && i.naturalWidth === 0 && i.src && !i.src.startsWith('data:')).map(i => i.src).slice(0,10),
    imgs_missing_alt: imgs.filter(i => !i.hasAttribute('alt')).length, imgs_total: imgs.length,
    small_tap: [...document.querySelectorAll('a[href],button')].filter(e => { const r = e.getBoundingClientRect(); return r.width>0 && r.height>0 && (r.width < 32 || r.height < 32); }).length,
    text_len: document.body.innerText.length,
    links, forms,
  };
}
"""


async def probe(browser, outdir, url, view, cfg):
    ctx = await browser.new_context(**cfg)
    pg = await ctx.new_page()
    rec = {'url': url, 'view': view, 'console': [], 'pageerrors': [], 'failed': [], 'mixed': [], 'status': None}
    pg.on('console', lambda m: rec['console'].append({'type': m.type, 'text': m.text[:300]}) if m.type in ('error', 'warning') else None)
    pg.on('pageerror', lambda e: rec['pageerrors'].append(str(e)[:300]))
    pg.on('requestfailed', lambda r: rec['failed'].append({'url': r.url[:200], 'err': (r.failure or '')[:80]}))
    pg.on('request', lambda r: rec['mixed'].append(r.url[:200]) if r.url.startswith('http://') and url.startswith('https://') else None)
    try:
        resp = await pg.goto(url, wait_until='load', timeout=60000)
        rec['status'] = resp.status if resp else None
        rec['final_url'] = pg.url
        await pg.wait_for_timeout(1500)
        rec['perf'] = await pg.evaluate(PERF_JS)
        rec['dom'] = await pg.evaluate(DOM_JS)
        slug = re.sub(r'[^a-z0-9]+', '-', urllib.parse.urlparse(url).path.lower()).strip('-') or 'home'
        shot = os.path.join(outdir, f'{slug}_{view}.png')
        h = await pg.evaluate('document.documentElement.scrollHeight')
        await pg.screenshot(path=shot, full_page=h < 9000, timeout=30000)
        rec['screenshot'] = shot
        # favicon status
        for ic in rec['dom']['icons'][:1] or [{'href': urllib.parse.urljoin(url, '/favicon.ico')}]:
            try:
                r = await ctx.request.get(ic['href'], timeout=15000)
                rec['favicon_status'] = r.status
            except Exception as e:
                rec['favicon_status'] = f'err {str(e)[:60]}'
        if not rec['dom']['icons']:
            rec['favicon_note'] = 'no <link rel=icon>; probed /favicon.ico'
        # link statuses (same registrable site + hub family), unique, max 80
        host = urllib.parse.urlparse(url).netloc
        seen, checked = set(), {}
        for l in rec['dom']['links']:
            h_ = l.get('href')
            if not h_ or not h_.startswith('http') or h_ in seen:
                continue
            seen.add(h_)
            if len(seen) > 80:
                break
            try:
                r = await ctx.request.get(h_.split('#')[0], timeout=20000, max_redirects=5)
                checked[h_] = r.status
            except Exception as e:
                checked[h_] = f'err {str(e)[:50]}'
        rec['link_status'] = checked
        rec['bad_links'] = {k: v for k, v in checked.items() if not (isinstance(v, int) and v < 400)}
    except Exception as e:
        rec['error'] = str(e)[:300]
    await ctx.close()
    return rec


async def main():
    outdir, urls = sys.argv[1], sys.argv[2:]
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        px = os.environ.get('HTTPS_PROXY')
        b = await p.chromium.launch(executable_path=CHROME, args=['--no-sandbox', '--disable-gpu'],
                                    proxy={'server': px} if px else None)
        results = []
        for u in urls:
            for v, cfg in VIEWS.items():
                r = await probe(b, outdir, u, v, cfg)
                for _ in range(3):
                    if r.get('error') or (r.get('status') or 0) >= 500:
                        await asyncio.sleep(3); r = await probe(b, outdir, u, v, cfg); r['retried'] = True
                    else:
                        break
                results.append(r)
                print(u, v, r.get('status'), 'console:', len(r['console']), 'bad_links:', len(r.get('bad_links', {})), r.get('error', ''), flush=True)
        await b.close()
    with open(os.path.join(outdir, 'probe.json'), 'w') as f:
        json.dump(results, f, indent=1)


asyncio.run(main())
