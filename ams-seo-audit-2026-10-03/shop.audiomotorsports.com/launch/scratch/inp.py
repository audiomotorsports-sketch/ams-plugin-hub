import asyncio,json
from playwright.async_api import async_playwright
exec(open('scratch/perf.py').read().split('async def run')[0])
async def go(path,mobile,rate):
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True) if mobile else await b.new_context(viewport={'width':1366,'height':900})
    pg=await ctx.new_page(); cdp=await ctx.new_cdp_session(pg)
    if rate>1: await cdp.send('Emulation.setCPUThrottlingRate',{'rate':rate})
    await pg.add_init_script(JS_INIT)
    await pg.goto('https://shop.audiomotorsports.com'+path,wait_until='load',timeout=90000); await pg.wait_for_timeout(3000)
    info=await pg.evaluate("[...document.querySelectorAll('button')].filter(b=>b.offsetParent&&!b.hasAttribute('data-reserve')).slice(0,12).map(b=>[b.innerText.trim().slice(0,25),b.className,b.getAttribute('data-filter')||b.getAttribute('data-stereo-filter')||''])")
    res=[]
    for label in ['Retrofit','Double DIN','All']:
      loc=pg.locator('button',has_text=label).first
      try:
        await loc.scroll_into_view_if_needed(timeout=3000)
        t=await pg.evaluate("performance.now()")
        await loc.click(timeout=3000) if not mobile else await loc.tap(timeout=3000)
        await pg.wait_for_timeout(1200); res.append(label)
      except Exception as e: res.append(label+' ERR '+str(e)[:50])
    m=await pg.evaluate("window.__m")
    await pg.mouse.wheel(0,3000); await pg.wait_for_timeout(500)
    await b.close()
    return dict(path=path,mobile=mobile,rate=rate,buttons=info[:8],clicked=res,events=sorted(m['ev'],key=lambda x:-x[1])[:8],longtasks=m['lt'][-6:])
async def main():
  for a in [('/shop/car-stereos/',True,4),('/shop/car-stereos/retrofit/',True,4),('/shop/car-stereos/',False,1)]:
    try: print(json.dumps(await go(*a))[:1400]);print()
    except Exception as e: print(a,e)
asyncio.run(main())
