"""Controle van aangeleverde media en de afgebakende AI-pagina."""
import asyncio
import hashlib
import json
import unittest
import zipfile
from pathlib import Path
from test_livegang_fase1 import Markup, request

class AIModellenTests(unittest.TestCase):
    def setUp(self):
        self.models = json.loads(Path('routes/ai_modellen.json').read_text(encoding='utf-8'))

    def test_complete_media_and_preview_paths(self):
        self.assertEqual([len(m['fotos']) for m in self.models], [4, 6, 6, 6, 6])
        self.assertEqual(sum(len(m['originelen']) for m in self.models), 18)
        for model in self.models:
            self.assertEqual(len(model['media']), 1 + len(model['fotos']) + len(model['originelen']))
            for media in model['media']:
                self.assertTrue((Path('static') / media['src']).is_file())
                self.assertTrue(media['alt'])
                if media['type'] == 'image':
                    self.assertTrue((Path('static') / media['preview']).is_file())
                    self.assertGreater(media['width'], 0)
                    self.assertGreater(media['height'], 0)
                    self.assertEqual('origineel-' in media['src'], media['original'])

    def test_archived_media_are_preserved_byte_for_byte(self):
        for archive in Path('.').glob('wespi_ai_*.zip'):
            with zipfile.ZipFile(archive) as z:
                for name in z.namelist():
                    if name.startswith(('images/', 'videos/')) and not name.endswith('/'):
                        self.assertEqual(hashlib.sha256(z.read(name)).digest(), hashlib.sha256((Path('static') / name).read_bytes()).digest(), name)

    def test_white_product_variants_preserve_colors_and_sources(self):
        from PIL import Image, ImageChops
        variants = [i for m in self.models for i in m['originelen'] if 'source' in i]
        self.assertEqual(len(variants), 4)
        for item in variants:
            source = Image.open(Path('static') / item['source']).convert('RGBA')
            white = Image.new('RGBA', source.size, 'white')
            expected = Image.alpha_composite(white, source).convert('RGB')
            actual = Image.open(Path('static') / item['src']).convert('RGB')
            self.assertEqual(actual.size, source.size)
            # The compositing libraries can round semi-transparent edge pixels by one level.
            difference = ImageChops.difference(expected, actual)
            self.assertLessEqual(max(high for low, high in difference.getextrema()), 1)
            self.assertEqual(actual.getpixel((0, 0)), (255,255,255))

    def test_uniform_variants_and_source_preservation(self):
        from PIL import Image
        manifest = json.loads(Path('docs/ai-presentatie-media.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest), 46)
        self.assertEqual(len({item['output'] for item in manifest}), 46)
        for item in manifest:
            source = Path('static') / item['source']
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), item['source_sha256'])
            with Image.open(Path('static') / item['output']) as image:
                self.assertEqual(image.size, (800,1200))
                if item['operation'] == 'white-packshot':
                    self.assertEqual(image.convert('RGB').getpixel((0,0)), (255,255,255))
            if item['operation'] == 'portrait-crop':
                # Full source height is retained: no head, shoes or clothing cut at top/bottom.
                self.assertEqual(item['crop_box'][1],0)
                self.assertEqual(item['crop_box'][3],item['source_size'][1])
        for model in self.models:
            for image in model['fotos'] + model['originelen']:
                self.assertEqual((image['presentatie']['width'],image['presentatie']['height']),(800,1200))
                self.assertTrue((Path('static') / image['presentatie']['src']).is_file())

    def test_page_previews_do_not_load_video_sources(self):
        status, _, html = asyncio.run(request('/productfotografie/kledingfotografie/ai-modelfotografie'))
        self.assertEqual(status, 200)
        tags = Markup(html).tags
        self.assertEqual(sum(t == 'article' and a.get('class') == 'ai-modelkaart' for t, a in tags), 5)
        self.assertEqual(sum(t == 'a' and 'ai-video-preview' in a.get('class', '') for t, a in tags), 5)
        self.assertEqual(sum(t in ('video', 'source') for t, a in tags), 0)
        self.assertIn('Handmatig waar het moet.', html)
        self.assertNotIn('??n', html)
        for price in ['9,99','24,99','19,99','39,99']:
            self.assertIn(price, html)

if __name__ == '__main__':
    unittest.main()
