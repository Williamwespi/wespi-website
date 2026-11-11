"""Regressie van de zelfstandige Productbeeldbewerkingpagina en afgeleide media."""
import asyncio
import hashlib
import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit
from PIL import Image
from test_livegang_fase1 import request, Markup

class ProductbeeldbewerkingTests(unittest.TestCase):
    def test_page_navigation_and_real_examples(self):
        status, _, html = asyncio.run(request('/beeldbewerking/product'))
        self.assertEqual(status,200)
        tags = Markup(html).tags
        self.assertEqual(sum(t=='h1' for t,a in tags),1)
        self.assertEqual(sum(t=='input' and a.get('type')=='range' for t,a in tags),1)
        self.assertTrue(any(t=='a' and a.get('href')=='/beeldbewerking/product' for t,a in tags))
        self.assertIn('https://www.wespi.nl/beeldbewerking/product',html)
        self.assertNotIn('bronmateriaal/',html)
        self.assertIn('€ 2,49',html)
        self.assertIn('exclusief btw',html)
        self.assertEqual(html.count('<section class="cta"'),1)
        self.assertNotIn('CONSISTENTE PRODUCTSERIES',html)
        self.assertNotIn('PRAKTISCH',html)
        self.assertNotIn('De houder weg.',html)
        self.assertIn('Elk product verdient een sterke presentatie',html)
        self.assertNotIn('class="pb-contact"',html)
        self.assertEqual(sum(t=='details' for t,a in tags),0)
        page_tags=Markup(html.split('<div class="pb-pagina">',1)[1].split('<script src=',1)[0]).tags
        self.assertEqual(sum(t=='div' and a.get('class')=='pb-paar' for t,a in page_tags),3)
        manifest=json.loads(Path('docs/PRODUCTBEELDBEWERKING_WEBMEDIA.json').read_text(encoding='utf-8'))
        by_file={Path(v['path']).name:m for m in manifest for v in m['variants']}
        image_sources=[]
        for t,a in page_tags:
            if t=='img':
                self.assertTrue(a.get('alt'))
                self.assertTrue(a.get('width') and a.get('height'))
                self.assertTrue(Path(urlsplit(a['src']).path.lstrip('/')).is_file())
                image_sources.append(by_file[Path(urlsplit(a['src']).path).name])
        self.assertEqual(len(image_sources),13)
        self.assertEqual(len({m['source'].split('/Before/')[-1].split('/After/')[-1] for m in image_sources}),9)
        # De vier getoonde vergelijkingen zijn echte, gelijknamige bronparen.
        by_name={m['name']:m for m in image_sources}
        for name in ['horloge-groen','bord-oranje','pet-rood','kleur-top']:
            self.assertEqual(by_name[name+'-voor']['source'].replace('/Before/','/After/'),by_name[name+'-na']['source'])

    def test_derived_media_sources_and_slider_alignment(self):
        manifest=json.loads(Path('docs/PRODUCTBEELDBEWERKING_WEBMEDIA.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest),20)
        self.assertEqual(len({m['source'].split('/Before/')[-1].split('/After/')[-1] for m in manifest}),13)
        for m in manifest:
            source=Path(m['source'])
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),m['source_sha256'])
            for v in m['variants']:
                with Image.open(v['path']) as image:
                    self.assertEqual(image.size,(v['width'],v['height']))
                    self.assertEqual(image.format,'WEBP')
                self.assertLess(Path(v['path']).stat().st_size,300000)
        by_name={m['name']:m for m in manifest}
        for name in ['kleur-top']:
            self.assertEqual(by_name[name+'-voor']['crop'],by_name[name+'-na']['crop'])
            for m in [by_name[name+'-voor'],by_name[name+'-na']]:
                for v in m['variants']:
                    self.assertEqual(v['width']*5,v['height']*4)

    def test_original_material_not_publicly_accessible(self):
        status,_,_=asyncio.run(request('/bronmateriaal/productbeeldbewerking/AFTER%20Before%20Sample/BAG/Before/BG223706-RED.jpg'))
        self.assertEqual(status,404)
        self.assertIn('/bronmateriaal/',Path('.gitignore').read_text(encoding='utf-8'))

if __name__=='__main__':unittest.main()
