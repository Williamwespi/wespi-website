"""Lokale controle van compact modellenoverzicht en rastergalerij."""
import json
from playwright.sync_api import sync_playwright
URL = 'http://127.0.0.1:8765/productfotografie/kledingfotografie/ai-modelfotografie'
with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    for width in [1440, 768, 430, 375, 320]:
        page = browser.new_page(viewport={'width': width, 'height': 900}, is_mobile=width < 500, has_touch=width < 500)
        errors, failures, videos = [], [], []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        page.on('response', lambda r: failures.append(r.url) if r.status >= 400 else None)
        page.on('request', lambda r: videos.append(r.url) if '.mp4' in r.url else None)
        page.goto(URL)
        page.locator('.ai-galerij').scroll_into_view_if_needed()
        assert page.locator('.ai-video-preview').count() == 5
        assert not videos
        columns = page.locator('.ai-galerij').evaluate('(e) => getComputedStyle(e).gridTemplateColumns.split(" ").length')
        assert columns == (5 if width > 1000 else 3 if width > 760 else 1)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        def equal_boxes(selector, ratio, same_row=False):
            boxes = page.locator(selector).evaluate_all('(es) => es.map(e => {const r=e.getBoundingClientRect();return {w:r.width,h:r.height,y:r.y};})')
            assert boxes
            assert max(b['w'] for b in boxes)-min(b['w'] for b in boxes) < 1, boxes
            assert max(b['h'] for b in boxes)-min(b['h'] for b in boxes) < 1, boxes
            assert all(abs(b['w']/b['h']-ratio)<0.002 for b in boxes), boxes
            if same_row: assert max(b['y'] for b in boxes)-min(b['y'] for b in boxes) < 1, boxes
        def aligned_cards():
            cards = page.locator('.ai-modelkaart').evaluate_all("""cards => cards.map(card => {
                const rect = e => { const r=e.getBoundingClientRect(); return {x:r.x,y:r.y,w:r.width,h:r.height}; };
                return {video:rect(card.querySelector('.ai-video-vlak')), photos:rect(card.querySelector('.ai-model-fotos')),
                        title:rect(card.querySelector('h3')), link:rect(card.querySelector('.ai-alles'))};
            })""")
            for start in range(0, len(cards), columns):
                row = cards[start:start+columns]
                for kind in ['video','photos','title','link']:
                    assert max(c[kind]['y'] for c in row)-min(c[kind]['y'] for c in row)<1, (width,kind,row)
                for c in row:
                    assert abs(c['video']['w']-c['photos']['w'])<1
                    assert abs(c['photos']['y']-c['video']['y']-c['video']['h']-8)<1
            assert page.locator('.ai-model-fotos .ai-media').evaluate_all('(es) => es.every(e => getComputedStyle(e).backgroundColor === "rgb(255, 255, 255)")')
        # Every photo pair has identical dimensions and shares the video edges.
        assert page.locator('.ai-model-fotos').evaluate_all("""pairs => pairs.every(pair => {
            const [left,right]=[...pair.children].map(e=>e.getBoundingClientRect());
            const video=pair.previousElementSibling.getBoundingClientRect();
            return Math.abs(left.width-right.width)<1 && Math.abs(left.height-right.height)<1 &&
                   Math.abs(left.top-right.top)<1 && Math.abs(left.left-video.left)<1 &&
                   Math.abs(right.right-video.right)<1 &&
                   [...pair.querySelectorAll('img')].every(i=>getComputedStyle(i).objectFit==='contain');
        })""")
        assert page.locator('.ai-vakwerk').evaluate('(e) => getComputedStyle(e).backgroundColor') == 'rgb(250, 243, 217)'
        aligned_cards()
        equal_boxes('.ai-video-vlak', 9/16, width>1000)
        equal_boxes('.ai-model-fotos .ai-media', 2/3, width>1000)
        models = json.loads(page.locator('#ai-modelgegevens').text_content())
        for model in models:
            opener = page.locator(f'.ai-alles[data-ai-model="{model["id"]}"]')
            opener.click()
            grid = page.locator('.ai-lightbox-media')
            assert grid.locator('img').count() == len(model['fotos']) + len(model['originelen'])
            assert grid.locator('img').evaluate_all('(images) => Promise.all(images.map(i => i.decode())).then(() => true)')
            equal_boxes('.ai-galerij-fotovlak', 2/3)
            assert grid.locator('img').evaluate_all('(images) => images.every(i => i.naturalWidth === 800 && i.naturalHeight === 1200)')
            if width in (1440,375):
                page.locator('.ai-lightbox').first.evaluate('(d) => d.scrollTop = 0')
                page.screenshot(path=f'docs/ai-uniform-{model["id"]}-{width}.png')
            assert page.locator('.ai-lightbox').first.evaluate('(d) => getComputedStyle(d).backgroundColor') == 'rgba(0, 0, 0, 0)'
            assert page.locator('.ai-lightbox').first.evaluate('(d) => d.scrollWidth <= d.clientWidth')
            grid.locator('a').first.click()
            assert page.locator('.ai-detail').evaluate('(d) => d.open')
            page.locator('.ai-detail img').evaluate('(i) => i.decode()')
            page.keyboard.press('Escape')
            assert grid.locator('a').first.evaluate('(e) => e === document.activeElement')
            page.wait_for_timeout(100)
            page.locator('.ai-lightbox-sluiten').focus()
            page.keyboard.press('Shift+Tab')
            assert grid.locator('a').last.evaluate('(e) => e === document.activeElement')
            page.keyboard.press('Escape')
            assert opener.evaluate('(e) => e === document.activeElement')
        assert not videos
        # Both thumbnail types open the complete grid.
        for link in page.locator('.ai-model-fotos a').all():
            link.click()
            assert page.locator('.ai-lightbox').first.evaluate('(d) => d.open')
            page.keyboard.press('Escape')
        page.wait_for_timeout(100)
        page.locator('.ai-alles').first.focus()
        page.evaluate('document.activeElement.blur()')
        page.locator('.ai-galerij img').evaluate_all('(images) => Promise.all(images.map(i => { i.loading="eager"; return i.decode(); }))')
        page.locator('.ai-galerij').screenshot(path=f'docs/ai-compact-{width}.png', style='header { visibility: hidden !important; }')
        assert page.locator('.ai-model-fotos img').evaluate_all('(images) => images.every(i => i.naturalWidth === 800 && i.naturalHeight === 1200)')
        assert page.locator('.ai-video-preview img').evaluate_all('(images) => images.every(i => Math.abs(i.naturalWidth/i.naturalHeight-9/16)<0.002)')
        while page.locator('.ai-video-preview').count():
            page.locator('.ai-video-preview').first.click()
            video = page.locator('.ai-inline-video').last
            page.wait_for_function('(v) => v.readyState >= 2', arg=video.element_handle(), timeout=15000)
            assert video.evaluate('(v) => !v.autoplay && v.muted && !v.paused && v.videoHeight > v.videoWidth')
            assert video.evaluate('(v) => {const r=v.getBoundingClientRect();return Math.abs(r.width/r.height-v.videoWidth/v.videoHeight)<0.002;}')
            equal_boxes('.ai-video-vlak',9/16,width>1000)
            aligned_cards()
            video.evaluate('(v) => v.pause()')
        if width in (1440,375):
            page.locator('.ai-alles').first.click()
            page.locator('.ai-lightbox-media img').evaluate_all('(images) => Promise.all(images.map(i => i.decode()))')
            page.screenshot(path=f'docs/ai-raster-{width}.png')
            page.keyboard.press('Escape')
        page.locator('.ai-vakwerk').screenshot(path=f'docs/ai-accent-{width}.png', style='header { visibility: hidden !important; }')
        assert not errors, errors
        assert not failures, failures
        print(f'{width}px OK: {columns} kolommen, alle 46 fotos, 5 videos na klik, focus/Escape, geen overflow/consolefouten', flush=True)
        page.close()
    browser.close()
