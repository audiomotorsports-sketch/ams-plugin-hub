#!/usr/bin/env python3
"""Build a per-page review index for one site's drafts. usage: build_index.py SITE"""
import sys,os,re,glob,json,csv
site=sys.argv[1]; base=f'/root/ams-seo-audit-2026-10-03/city_rewrite/{site}'
rows=[]
for f in sorted(glob.glob(f'{base}/drafts/*.md')):
    t=open(f,encoding='utf-8').read()
    m=re.search(r'^---\n(.*?)\n---',t,re.S); fm=dict(re.findall(r'^(\w+):\s*(.*)$',m.group(1),re.M)) if m else {}
    body=t[m.end():] if m else t
    jm=re.search(r'```json',body); vis=body[:jm.start()] if jm else body
    wc=len(re.findall(r"[A-Za-z0-9'’-]+",re.sub(r'\[SHOP NOTE[^\]]*\]','',vis)))
    notes=len(re.findall(r'\[SHOP NOTE',vis)); conf=len(re.findall(r'\[CONFIRM',t))
    rows.append({'slug':os.path.basename(f)[:-3],'url':fm.get('url',''),'city':fm.get('city',''),'miles':fm.get('miles',''),'lead_service':fm.get('lead_service',''),'title':fm.get('title',''),'words':wc,'shop_note_slots':notes,'confirm_items':conf})
with open(f'{base}/REVIEW_INDEX.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(site,len(rows),'pages; avg words',sum(r['words'] for r in rows)//max(1,len(rows)),'; shop-note slots',sum(r['shop_note_slots'] for r in rows))
