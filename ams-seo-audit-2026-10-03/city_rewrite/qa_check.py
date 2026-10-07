#!/usr/bin/env python3
"""Read-only QA for city-page drafts. usage: qa_check.py DRAFTS_DIR [--allsites]"""
import sys,os,re,json,glob,collections
d=sys.argv[1]; files=sorted(glob.glob(os.path.join(d,'*.md')))
FORBID=['we do not invent','do not reverse','never imply','schema aggregate','locked','placeholder','todo','we are not in']
PRICES_OK={'$249','$329','$269','$499','$649'}
SERVICES=['window tint','ceramic','car audio','car stereo','subwoofer','amplifier','carplay','android auto','alarm','remote start','gps','dash cam','tesla','harley','bagger','pods']
sent_index=collections.defaultdict(list); fails=0; warns=0; report=[]
def norm(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',s)).strip().lower()
for f in files:
    t=open(f,encoding='utf-8').read(); name=os.path.basename(f); probs=[]
    m=re.search(r'^---\n(.*?)\n---',t,re.S); fm=dict(re.findall(r'^(\w+):\s*(.*)$',m.group(1),re.M)) if m else {}
    title=fm.get('title',''); meta=fm.get('meta',''); city=fm.get('city','')
    if not (1<=len(title)<=60): probs.append(f'title length {len(title)}')
    if not (120<=len(meta)<=160): probs.append(f'meta length {len(meta)}')
    body=t[m.end():] if m else t
    jm=re.search(r'```json\n(.*?)```',body,re.S); jtxt=jm.group(1) if jm else ''
    vis=body[:jm.start()] if jm else body
    low=vis.lower()
    for p in FORBID:
        if re.search(r'(?<![a-z])'+re.escape(p)+r'(?![a-z])',low): probs.append(f'forbidden phrase "{p}"')
    for pr in set(re.findall(r'\\$\d[\d,]*?(?=[^\d,]|$)',vis)):
        if pr not in PRICES_OK: probs.append(f'price not allowed {pr}')
    if re.search(r'\$\d',vis) and 'as of october 2026' not in low: probs.append('price without "as of October 2026"')
    for mm in re.finditer(r'\bAvalon\b(?!\s+Blvd)',vis):
        probs.append('Avalon used outside "Avalon Blvd"'); break
    wc=len(re.findall(r"[A-Za-z0-9'’-]+",re.sub(r'\[SHOP NOTE[^\]]*\]','',vis)))
    if wc<400: probs.append(f'word count {wc} < 400')
    if city and city.lower() not in low: probs.append('city name missing')
    if 'carson' not in low: probs.append('Carson missing')
    if sum(1 for s in SERVICES if s in low)<4: probs.append('fewer than 4 service keywords')
    links=set(re.findall(r'\]\(/((?:[a-z0-9-]+/)*[a-z0-9-]+)/\)',vis))|set(re.findall(r'href="/((?:[a-z0-9-]+/)*[a-z0-9-]+)/"',vis))
    if len(links)<3: probs.append(f'neighbor links {len(links)} < 3')
    qs=[norm(q) for q in re.findall(r'^###\s+(.*\?)\s*$',vis,re.M)]
    if len(qs)<5: probs.append(f'question headings {len(qs)} < 5')
    if jtxt:
        try:
            j=json.loads(jtxt); nodes=j.get('@graph',[j]) if isinstance(j,dict) else j
            faq=[n for n in nodes if n.get('@type')=='FAQPage']
            if not faq: probs.append('no FAQPage in JSON-LD')
            else:
                sq=[norm(e['name']) for e in faq[0].get('mainEntity',[])]
                if sorted(sq)!=sorted(qs): probs.append('FAQ questions in schema != visible headings')
                for e in faq[0].get('mainEntity',[]):
                    a=norm(e.get('acceptedAnswer',{}).get('text',''))
                    if a and a not in norm(vis): probs.append('FAQ answer text not found verbatim in visible body'); break
            if not any(n.get('@type')=='WebPage' for n in nodes): probs.append('no WebPage node')
            if any(n.get('@type') in('AutoRepair','LocalBusiness','Organization') and n.get('address') for n in nodes): probs.append('new business node emitted (reference @id instead)')
        except Exception as e: probs.append(f'JSON-LD invalid: {e}')
    else: probs.append('no JSON-LD block')
    for s in re.split(r'(?<=[.!?])\s+',norm(re.sub(r'\[SHOP NOTE[^\]]*\]','',vis))):
        if len(s.split())>=9 and not re.search(r'(9:30|closed (on )?sunday|\$249|\$329|as of october 2026|\(310\) 513-8800|\(213\) 429-1092|22025 s avalon)',s): sent_index[s].append(name)
    if probs: fails+=1; report.append((name,probs))
dups=[(s,v) for s,v in sent_index.items() if len(set(v))>1]
print(f'files={len(files)} FAIL={fails} reused_sentences={len(dups)}')
for n,p in report: print('FAIL',n,'|','; '.join(p))
for s,v in dups[:40]: print('REUSE',sorted(set(v)),'|',s[:90])
sys.exit(1 if fails or dups else 0)
