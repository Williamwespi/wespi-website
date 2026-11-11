"""Lokale Chrome/Playwright-controle; app op 127.0.0.1:8765."""
from pathlib import Path
from io import BytesIO
from urllib.parse import urlsplit
from PIL import Image
from playwright.sync_api import sync_playwright
BASE='http://127.0.0.1:8765'
URL=BASE+'/beeldbewerking/product'
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    for width in [1440,1024,768,430,375,320]:
        page=browser.new_page(viewport={'width':width,'height':900},is_mobile=width<500,has_touch=width<500)
        errors=[];failures=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
        page.on('response',lambda r:failures.append((r.url,r.status)) if r.status>=400 else None)
        page.goto(URL)
        assert page.title()=='Productbeeldbewerking voor webshops en e-commerce | Wespi'
        assert page.locator('h1').count()==1
        assert page.locator('.pb-pagina img').count()==13
        assert page.locator('link[rel="canonical"]').get_attribute('href')=='https://www.wespi.nl/beeldbewerking/product'
        page.locator('img').evaluate_all('(images)=>Promise.all(images.map(i=>{i.loading="eager";return i.decode()}))')
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),width
        assert page.locator('.pb-pagina').evaluate('(e)=>e.scrollWidth<=innerWidth'),width
        page.evaluate('scrollTo(5000,0)')
        assert page.evaluate('scrollX')==0,width
        assert page.locator('.pb-prijs strong').inner_text()=='€ 2,49'
        assert page.locator('section.cta').count()==1
        # Controleer de oorspronkelijke fout in de uiteindelijke pixels:
        # het onbedekte beeld aan boven- en onderkant blijft grijs, niet wit gefade.
        for selector,pseudo,sample_x in [('.pb-hero-beeld','::before',.97),('.pb-tarief-beeld','::after',.03)]:
            visual=page.locator(selector)
            gradient=visual.evaluate('(e,p)=>getComputedStyle(e,p).backgroundImage',pseudo)
            assert gradient.startswith('linear-gradient(90deg,'),gradient
            assert visual.locator('img').evaluate('(e)=>getComputedStyle(e).filter')=='none'
            if selector=='.pb-hero-beeld':
                assert visual.evaluate('(e)=>getComputedStyle(e,"::after").content')=='none'
            screenshot=visual.screenshot(style='header {visibility:hidden!important}')
            with Image.open(BytesIO(screenshot)).convert('RGB') as pixels:
                x=int(pixels.width*sample_x)
                for y in [3,pixels.height-4]:
                    assert all(abs(c-225)<=2 for c in pixels.getpixel((x,y))),(width,selector,x,y,pixels.getpixel((x,y)))
        sfeer=page.locator('.pb-sfeer')
        gradient=page.locator('.pb-sfeer-beeld').evaluate('(e)=>getComputedStyle(e,"::after").backgroundImage')
        assert gradient.startswith('linear-gradient(90deg,'),gradient
        if width<=900:
            assert page.locator('.pb-sfeer-beeld').bounding_box()['y']>=page.locator('.pb-sfeer-tekst').bounding_box()['y']+page.locator('.pb-sfeer-tekst').bounding_box()['height']
        else:
            assert page.locator('.pb-sfeer-tekst').bounding_box()['x']<page.locator('.pb-sfeer-beeld').bounding_box()['x']
        for pair in page.locator('.pb-paar').all():
            sizes=pair.locator('img').evaluate_all('(es)=>es.map(e=>[e.clientWidth,e.clientHeight])')
            assert all(abs(a-b)<=1 for a,b in zip(sizes[0],sizes[1])),sizes  # afronding van subpixels in ongelijke viewportbreedtes
            assert abs(sizes[0][0]/sizes[0][1]-.8)<.01,sizes
        if width<=900:
            assert page.locator('.pb-hero-beeld').evaluate('(e)=>e.getBoundingClientRect().top')>page.locator('h1').evaluate('(e)=>e.getBoundingClientRect().bottom')
        for article in page.locator('.pb-vergelijking').all():
            slider=article.locator('input[type=range]')
            article.locator('[data-pb-stand="100"]').click()
            assert slider.input_value()=='100'
            assert article.locator('[data-pb-stand="100"]').get_attribute('aria-pressed')=='true'
            assert slider.get_attribute('aria-valuetext')=='100% origineel, 0% bewerkt'
            article.locator('[data-pb-stand="0"]').click()
            assert slider.input_value()=='0'
            slider.focus();page.keyboard.press('ArrowRight')
            assert slider.input_value()=='1'
            page.keyboard.press('End');assert slider.input_value()=='100'
            page.keyboard.press('Home');assert slider.input_value()=='0'
            box=slider.bounding_box()
            if width<500:
                page.touchscreen.tap(box['x']+box['width']*.65,box['y']+box['height']*.5)
            else:
                page.mouse.move(box['x']+box['width']*.2,box['y']+box['height']*.5)
                page.mouse.down();page.mouse.move(box['x']+box['width']*.65,box['y']+box['height']*.5,steps=8);page.mouse.up()
            assert 60<=int(slider.input_value())<=70,slider.input_value()
            dimensions=article.locator('.beeldvergelijker__afbeelding img').evaluate_all('(es)=>es.map(e=>[e.clientWidth,e.clientHeight,e.naturalWidth,e.naturalHeight])')
            assert dimensions[0]==dimensions[1],dimensions
            assert abs(dimensions[0][2]/dimensions[0][3]-.8)<.01
            slider.evaluate('(e)=>{e.value=50;e.dispatchEvent(new Event("input",{bubbles:true}))}')
        # All internal destinations and fragment ids, without submitting any forms.
        links=page.locator('.pb-pagina a').evaluate_all('(es)=>es.map(e=>e.getAttribute("href"))')
        for href in set(links):
            target=urlsplit(href)
            if href.startswith('#'):assert page.locator(href).count()==1
            elif href.startswith('/'):
                response=page.request.get(BASE+href);assert response.status==200,(href,response.status)
        # Activate the existing navigation on desktop and inside the mobile menu.
        page.evaluate('scrollTo(0,0)')
        main_toggle=page.locator('[aria-controls="hoofdnavigatie"]')
        if main_toggle.is_visible():main_toggle.click()
        page.locator('[aria-controls="diensten-dropdown"]').click()
        nav=page.locator('header a[href="/beeldbewerking/product"]')
        assert nav.is_visible()
        nav.click();page.wait_for_url(URL)
        page.locator('img').evaluate_all('(images)=>Promise.all(images.map(i=>{i.loading="eager";return i.decode()}))')
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        # De bestaande decoratieve footergolf steekt buiten de viewport.
        # Neem de zichtbare paginabreedte op, zonder onzichtbare tekenruimte.
        page.screenshot(path=f'docs/productbeeldbewerking-{width}.png',full_page=True,
                        clip={'x':0,'y':0,'width':width,'height':page.evaluate('document.documentElement.scrollHeight')})
        page.locator('.pb-hero').screenshot(path=f'docs/productbeeldbewerking-hero-{width}.png',style='header {visibility:hidden!important}')
        if width in (1440,768,430,375):
            for label,selector in [('tarief','.pb-tarief'),('kleur','.pb-kleur'),('sfeer','.pb-sfeer')]:
                page.locator(selector).screenshot(path=f'docs/productbeeldbewerking-{label}-{width}.png',style='header {visibility:hidden!important}')
        if width in (1440,375):
            page.locator('.pb-hoofdvoorbeeld').screenshot(path=f'docs/productbeeldbewerking-vergelijking-{width}.png',style='header {visibility:hidden!important}')
        assert not errors,errors
        assert not failures,failures
        print(f'{width}px: beelden, vaste paren, slider (knoppen/toetsenbord/pointer), tarief, footer, menu, interne links, SEO, geen overflow/console-/mediafouten: OK',flush=True)
        page.close()
    # Content and imagery remain available without JavaScript.
    page=browser.new_page(java_script_enabled=False)
    page.goto(URL)
    assert page.locator('.pb-pagina img').count()==13
    assert page.locator('h1').is_visible()
    browser.close()
