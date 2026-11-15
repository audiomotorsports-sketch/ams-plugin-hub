import asyncio,json
from playwright.async_api import async_playwright
exec(open('scratch/perf.py').read().split('async def run')[0])
async def go(path,rate):
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
    pg=await ctx.new_page(); cdp=await ctx.new_cdp_session(pg)
    if rate>1: await cdp.send('Emulation.setCPUThrottlingRate',{'rate':rate})
    await pg.add_init_script(JS_INIT)
    await pg.goto('https://shop.audiomotorsports.com'+path,wait_until='load',timeout=90000); await pg.wait_for_timeout(3000)
    fac=await pg.evaluate("[...document.querySelectorAll('[data-shop-facet]')].map(a=>[a.dataset.shopFacet,a.dataset.shopFacetValue,a.innerText.trim().replace(/\\s+/g,' ')])")
    # open filter drawer if collapsed
    tog=pg.locator('text=SHOP FILTERS, text=Shop filters').first
    out=[]
    for i,f in enumerate([x for x in fac if x[1]][:4]):
      loc=pg.locator(f'[data-shop-facet="{f[0]}"][data-shop-facet-value="{f[1]}"]').first
      try:
        await loc.evaluate("el=>el.scrollIntoView()")
        t0=await pg.evaluate("performance.now()")
        await loc.dispatch_event('click')
        await pg.wait_for_timeout(1500)
        vis=await pg.evaluate("[...document.querySelectorAll('.product-card')].filter(c=>!c.hidden&&c.offsetParent).length")
        out.append((f[:2],'visible cards',vis))
      except Exception as e: out.append((f,str(e)[:60]))
    # real tap on a card button (reserve opens modal, no submit)
    m=await pg.evaluate("window.__m")
    await b.close()
    return dict(path=path,rate=rate,nfacets=len(fac),out=out,events=sorted(m['ev'],key=lambda x:-x[1])[:8],lt=m['lt'])
async def main():
  for a in [('/shop/car-stereos/',4),('/shop/car-stereos/retrofit/',4),('/shop/speakers/',4)]:
    try: print(json.dumps(await go(*a))[:1500]);print()
    except Exception as e: print(a,e)
asyncio.run(main())
