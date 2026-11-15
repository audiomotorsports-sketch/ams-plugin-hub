import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=await b.new_page(viewport={'width':390,'height':844})
    await pg.goto('https://shop.audiomotorsports.com/shop/amplifiers/',wait_until='load')
    await pg.wait_for_timeout(3000)
    print(await pg.evaluate("""[...document.querySelectorAll('a[href*="kicker-club-a600"]')].map(a=>[a.getAttribute('href'),a.className,a.parentElement.className,a.closest('[class]').className, a.closest('.product-card')?'incard':'notcard'])"""))
    print(await pg.evaluate("document.querySelectorAll('.product-card').length"))
    print(await pg.evaluate("""[...document.querySelectorAll('.product-card')].filter(c=>c.dataset.sku==='kicker-club-a600').map(c=>[...c.querySelectorAll('a')].map(a=>a.getAttribute('href')))"""))
    await b.close()
asyncio.run(main())
