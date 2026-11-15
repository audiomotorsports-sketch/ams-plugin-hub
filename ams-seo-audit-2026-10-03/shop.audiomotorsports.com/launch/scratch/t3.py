import asyncio,json,re,urllib.request
from playwright.async_api import async_playwright
PAGES=['car-stereos','car-stereos/retrofit','amplifiers','dash-cameras','alarms-remote-start','speakers','subwoofers','enclosures','installation-parts']
async def main():
  out={}
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    for pgname in PAGES:
      pg=await b.new_page(viewport={'width':390,'height':844})
      try:
        await pg.goto(f'https://shop.audiomotorsports.com/shop/{pgname}/',wait_until='load',timeout=60000)
        await pg.wait_for_timeout(3000)
        hrefs=await pg.evaluate("[...new Set([...document.querySelectorAll('.product-card a[href^=\"/shop/\"]')].map(a=>a.getAttribute('href')))]")
        n=await pg.evaluate("document.querySelectorAll('.product-card').length")
        out[pgname]=(n,hrefs)
      except Exception as e: out[pgname]=(str(e)[:80],[])
      await pg.close()
    await b.close()
  json.dump(out,open('scratch/rendered.json','w'))
asyncio.run(main())
