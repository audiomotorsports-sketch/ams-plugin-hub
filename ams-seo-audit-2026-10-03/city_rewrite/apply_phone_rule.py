#!/usr/bin/env python3
"""Owner rule of 2026-10-13: CALL = (310) 513-8800, TEXT = (213) 429-1092. Context-aware, idempotent."""
import glob,os,re,sys
T='(213) 429-1092'; C='(310) 513-8800'
Tre=re.escape(T)
PAIR=[
 (re.compile(r'\b(call|calling|Call|Calling) or (text|texting|Text|Texting)( us| Nick)?( at| on)? '+Tre),
  lambda m: f"{m.group(1)} {C} or {m.group(2)}{m.group(3) or ''}{m.group(4) or ''} {T}"),
 (re.compile(r'\b(text|texting|Text|Texting) or (call|calling|Call|Calling)( us| Nick)?( at| on)? '+Tre),
  lambda m: f"{m.group(1)} {T} or {m.group(2)}{m.group(3) or ''}{m.group(4) or ''} {C}"),
]
def ctx_fix(t):
    out=[];last=0
    for m in re.finditer(Tre,t):
        pre=t[max(0,m.start()-40):m.start()].lower()
        # nearest keyword before the number
        k=[(pre.rfind(w),w) for w in ('text','texting','sms','call','calling','phone','dial','ring')]
        k=[x for x in k if x[0]>=0]
        kind=None
        if k:
            _,w=max(k); kind='T' if w in('text','texting','sms') else 'C'
        out.append(t[last:m.start()]); last=m.end()
        out.append(T if kind=='T' else C if kind=='C' else '@@AMBIG@@')
    out.append(t[last:]); return ''.join(out)
def fix(path):
    t0=open(path,encoding='utf-8').read(); t=t0
    for rx,f in PAIR: t=rx.sub(f,t)
    # protect already-correct (310) text by only touching T occurrences
    t=ctx_fix(t)
    t=t.replace('"+1-213-429-1092"','"+1-310-513-8800"')
    if t!=t0: open(path,'w',encoding='utf-8').write(t)
    return t!=t0, t.count('@@AMBIG@@')
if __name__=='__main__':
    ch=am=n=0
    for p in sorted(glob.glob('*/drafts/*.md')+glob.glob('*/_hub_style_strays/*.md')):
        n+=1; c,a=fix(p); ch+=c; am+=a
        if a: print('AMBIG',p,a)
    print(f'files={n} changed={ch} ambiguous={am}')
