import json,sys
for f in sys.argv[1:]:
  for r in json.load(open(f)):
    d=r.get('dom') or {};p=r.get('perf') or {}
    bad=[ (l['href'],l.get('status')) for l in (d.get('link_status') or [])] if False else None
    keys=[k for k in d.keys()]
    print(r['url'].replace('https://www.audiomotorsports.com',''),r['view'],r['status'],'lcp',round(p.get('lcp',0)),'cls',round(p.get('cls',0),3),'tbt',round(p.get('longtask_ms',0)),'ttfb',round(p.get('ttfb',0)),'kb',p.get('transfer_kb'),'req',p.get('requests'),'ovx',d.get('overflow_x'),'tap',d.get('small_tap'),'broken',len(d.get('broken_images') or []),'noalt',d.get('imgs_missing_alt'),'console',[c['text'][:90] for c in r['console']][:4])
