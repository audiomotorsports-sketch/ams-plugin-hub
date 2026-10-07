import json,re,subprocess,concurrent.futures as cf
o=json.load(open('scratch/rendered.json'))
def st(u):
  for i in range(3):
    r=subprocess.run(['curl','-sS','-m','25','-o','/dev/null','-w','%{http_code}','https://shop.audiomotorsports.com'+u],capture_output=True,text=True)
    if r.stdout.strip() not in('000',''): return u,r.stdout.strip()
  return u,'err'
allu={}
for k,(n,h) in o.items():
  stat=subprocess.run(['curl','-sS','-m','40',f'https://shop.audiomotorsports.com/shop/{k}/'],capture_output=True,text=True).stdout
  sh=set(re.findall(r'class="product-card__(?:media|title)-link" href="([^"]+)"',stat))
  sh|=set(re.findall(r'href="(/shop/[^"]+)"',stat))
  diff=[u for u in h if u not in sh]
  print(k,'rendered',len(h),'static-card hrefs',len(sh),'rendered-not-in-static',len(diff))
  for u in diff: allu[u]=k
with cf.ThreadPoolExecutor(6) as ex: res=list(ex.map(st,allu))
bad=[(u,s,allu[u]) for u,s in res if s!='200']
print('checked',len(res),'non200',len(bad))
for b in bad: print(b)
json.dump(bad,open('scratch/bad_cards.json','w'))
