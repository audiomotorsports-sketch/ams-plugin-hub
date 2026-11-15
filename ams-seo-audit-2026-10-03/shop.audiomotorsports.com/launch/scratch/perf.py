import asyncio,json,sys
from playwright.async_api import async_playwright
JS_INIT="""
window.__m={lcp:null,lt:[],ev:[],cls:0};
new PerformanceObserver(l=>{for(const e of l.getEntries()){window.__m.lcp={t:e.startTime,url:e.url,el:e.element&&e.element.tagName+'.'+e.element.className,size:e.size}}}).observe({type:'largest-contentful-paint',buffered:true});
new PerformanceObserver(l=>{for(const e of l.getEntries())window.__m.lt.push([Math.round(e.startTime),Math.round(e.duration)])}).observe({type:'longtask',buffered:true});
new PerformanceObserver(l=>{for(const e of l.getEntries())window.__m.ev.push([e.name,Math.round(e.duration),Math.round(e.processingStart-e.startTime)])}).observe({type:'event',buffered:true,durationThreshold:16});
new PerformanceObserver(l=>{for(const e of l.getEntries())if(!e.hadRecentInput)window.__m.cls+=e.value}).observe({type:'layout-shift',buffered:true});
"""
async def run(url,mobile,throttle):
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    if mobile: ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
    else: ctx=await b.new_context(viewport={'width':1366,'height':900})
    pg=await ctx.new_page()
    cdp=await ctx.new_cdp_session(pg)
    if throttle: await cdp.send('Emulation.setCPUThrottlingRate',{'rate':4})
    await pg.add_init_script(JS_INIT)
    resp=[]
    pg.on('response',lambda r:resp.append(r))
    await pg.goto(url,wait_until='load',timeout=90000); await pg.wait_for_timeout(3500)
    # interactions
    btns=await pg.query_selector_all('[data-stereo-filter], .shop-filter button, button[aria-pressed]')
    for bt in btns[:5]:
      try: await bt.click(timeout=3000); await pg.wait_for_timeout(500)
      except Exception as e: pass
    for _ in range(6):
      await pg.mouse.wheel(0,2500); await pg.wait_for_timeout(250)
    try: await pg.tap('.product-card a',timeout=2000) if False else None
    except: pass
    m=await pg.evaluate("window.__m")
    dom=await pg.evaluate("""()=>{const imgs=[...document.querySelectorAll('.product-card img, img')];
      const st=imgs.map(i=>({src:i.currentSrc||i.src,nw:i.naturalWidth,cw:i.clientWidth,lazy:i.loading,w:i.getAttribute('width'),fp:i.getAttribute('fetchpriority')}));
      const over=st.filter(s=>s.cw>0&&s.nw>s.cw*2*1.0);
      return {nodes:document.getElementsByTagName('*').length,cards:document.querySelectorAll('.product-card').length,imgs:st.length,lazy:st.filter(s=>s.lazy==='lazy').length,eager:st.filter(s=>s.lazy!=='lazy').length,
        oversize:over.length,maxnw:Math.max(...st.map(s=>s.nw)),sample:st.slice(0,3),dpr:devicePixelRatio,
        sizes:[...new Set(st.map(s=>s.nw+'/'+s.cw))].slice(0,6),btnCount:document.querySelectorAll('button').length}}""")
    imgbytes=0;n=0;types={}
    for r in resp:
      ct=r.headers.get('content-type','')
      if ct.startswith('image/'):
        try:
          cl=int(r.headers.get('content-length') or 0)
        except: cl=0
        imgbytes+=cl;n+=1;types[ct]=types.get(ct,0)+1
    await b.close()
    return dict(url=url,mobile=mobile,throttle=throttle,metrics={'lcp':m['lcp'],'cls':round(m['cls'],3),'longtasks':len(m['lt']),'lt_total_over50':sum(max(0,d-50) for s,d in m['lt']),'lt_max':max([d for s,d in m['lt']] or [0]),'events':sorted(m['ev'],key=lambda x:-x[1])[:6],'nbuttons_clicked':len(btns[:5])},dom=dom,img_requests=n,img_bytes_kb=round(imgbytes/1024),img_types=types)
async def main():
  out=[]
  for path in ['/shop/car-stereos/','/shop/car-stereos/retrofit/']:
    for mobile,th in [(True,True),(True,False),(False,False)]:
      try: out.append(await run('https://shop.audiomotorsports.com'+path,mobile,th))
      except Exception as e: out.append({'url':path,'err':str(e)[:150]})
  json.dump(out,open('perf_grid.json','w'),indent=1)
  for o in out: print(json.dumps(o)[:1500]);print()
asyncio.run(main())
