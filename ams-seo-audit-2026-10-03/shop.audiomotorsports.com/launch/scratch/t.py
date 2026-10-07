import asyncio,sys
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=await b.new_page(viewport={'width':390,'height':844})
    reqs=[]
    pg.on('response',lambda r: reqs.append((r.status,r.url)) if r.status>=400 else None)
    await pg.goto('https://shop.audiomotorsports.com/shop/amplifiers/',wait_until='load')
    await pg.wait_for_timeout(3000)
    print(await pg.evaluate("[...document.querySelectorAll('.product-card')].slice(0,3).map(c=>[c.dataset.sku,[...c.querySelectorAll('a')].map(a=>a.getAttribute('href'))])"))
    print(reqs)
    scripts=await pg.evaluate("[...document.scripts].map(s=>s.src||('inline:'+s.textContent.length))")
    print(scripts)
    await pg.click('.product-card a.product-card__media-link')
    await pg.wait_for_timeout(2500)
    print('after click',pg.url, await pg.title())
    await b.close()
asyncio.run(main())
