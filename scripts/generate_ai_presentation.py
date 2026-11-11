"""Maak afgeleide 2:3-presentatiebeelden; bronmedia en videoposters blijven intact.
Run: python -B scripts/generate_ai_presentation.py (Pillow en ImageMagick nodig).
"""
import hashlib
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
SIZE = (800, 1200)

def generate():
    path = ROOT / 'routes/ai_modellen.json'
    models = json.loads(path.read_text(encoding='utf-8'))
    manifest = []
    for model in models:
        for item in model['fotos'] + model['originelen']:
            source = ROOT / 'static' / item['src']
            target = Path(item['src']).parent / 'presentatie' / (source.stem + '-2x3.webp')
            output = ROOT / 'static' / target
            output.parent.mkdir(parents=True, exist_ok=True)
            image = Image.open(source).convert('RGBA')
            width, height = image.size
            command = ['magick', str(source)]
            if item['original']:
                # Measure the existing product against white; keep a guard around its bounds.
                rgb = Image.alpha_composite(Image.new('RGBA', image.size, 'white'), image).convert('RGB')
                delta = ImageChops.difference(rgb, Image.new('RGB', image.size, 'white'))
                mask = ImageChops.lighter(ImageChops.lighter(*delta.split()[:2]), delta.split()[2])
                box = mask.point(lambda x: 255 if x > 8 else 0).getbbox() or (0, 0, width, height)
                guard = 20
                box = (max(0, box[0]-guard), max(0, box[1]-guard), min(width, box[2]+guard), min(height, box[3]+guard))
                operation = 'white-packshot'
                command += ['-background', '#FFFFFF', '-alpha', 'remove', '-alpha', 'off', '-crop',
                            f'{box[2]-box[0]}x{box[3]-box[1]}+{box[0]}+{box[1]}', '+repage',
                            '-resize', '720x1080', '-gravity', 'center', '-extent', '800x1200', '-define', 'webp:lossless=true']
            else:
                # Keep full height and crop only lateral background for these portrait sources.
                crop_width = min(width, round(height * 2/3))
                crop_height = min(height, round(width * 3/2))
                left, top = (width-crop_width)//2, (height-crop_height)//2
                box = (left, top, left+crop_width, top+crop_height)
                operation = 'portrait-crop'
                command += ['-crop', f'{crop_width}x{crop_height}+{left}+{top}', '+repage',
                            '-resize', '800x1200^', '-gravity', 'center', '-extent', '800x1200', '-quality', '92', '-define', 'webp:method=6']
            subprocess.run(command + [str(output)], check=True, capture_output=True)
            assert Image.open(output).size == SIZE
            item['presentatie'] = {'src': target.as_posix(), 'width': 800, 'height': 1200}
            manifest.append({'source': item['src'], 'output': target.as_posix(), 'operation': operation,
                             'source_size': [width,height], 'crop_box': list(box), 'output_size': list(SIZE),
                             'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
        by_source = {i['src']: i for i in model['fotos'] + model['originelen']}
        model['media'] = [model['video']] + [by_source[i['src']] for i in model['media'] if i['type']=='image']
    path.write_text(json.dumps(models, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (ROOT/'docs/ai-presentatie-media.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{len(manifest)} afgeleide 800x1200 WebP-beelden gemaakt; bronnen behouden.')

if __name__ == '__main__':
    generate()
