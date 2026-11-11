"""Afgeleide webbeelden voor Productbeeldbewerking; bronbestanden blijven intact.
Run vanuit de projectroot met Pillow: python -B scripts/generate_productbeeldbewerking.py
"""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'bronmateriaal/productbeeldbewerking/AFTER Before Sample'
OUTPUT = ROOT / 'static/images/beeldbewerking/product'
# Beide sliderhelften krijgen exact dezelfde uitsnede: geen schaal- of positiecorrectie nodig.
ASSETS = [
 ('horloge-groen-voor','JWELLERY','Before','2559-2100072398543_1.jpg',None),
 ('horloge-groen-na','JWELLERY','After','2559-2100072398543_1.jpg',None),
 ('tas-rood-voor','BAG','Before','BG223706-RED.jpg',(0,780,1500,1780)),
 ('tas-rood-na','BAG','After','BG223706-RED.jpg',(0,780,1500,1780)),
 ('tas-rood-visual-na','BAG','After','BG223706-RED.jpg',(0,650,1500,1850)),
 ('schoen-zwart-voor','SHOES','Before','GMHEBEN4_BLK01_PZ.jpg',(0,500,3000,2500)),
 ('schoen-zwart-na','SHOES','After','GMHEBEN4_BLK01_PZ.jpg',(0,500,3000,2500)),
 ('sandaal-bruin-na','SHOES','After','GWDISTA6_DBR01_PZ.jpg',(0,500,3000,2500)),
 ('bord-oranje-voor','CROCKERY','Before','2625-2100067702058_3.jpg',None),
 ('bord-oranje-na','CROCKERY','After','2625-2100067702058_3.jpg',None),
 ('pet-rood-voor','CAP','Before','2589-2100066166400_1.jpg',None),
 ('pet-rood-na','CAP','After','2589-2100066166400_1.jpg',None),
 ('kleur-top-voor','CC','Before','3090-2100074884327_1.jpg',None),
 ('kleur-top-na','CC','After','3090-2100074884327_1.jpg',None),
 ('riem-bruin-na','BELT','After','2582-2100068985146_4.jpg',None),
 ('skibril-na','SWIM WEAR','After','2622-2100072112798_1.jpg',None),
 ('serie-tas-voorzijde-na','BAG','After','BG260905_LTR_SIENNA_F.jpg',(0,900,2000,2400)),
 ('serie-tas-achterzijde-na','BAG','After','BG260905_LTR_SIENNA_B.jpg',(0,820,1768,2146)),
 ('serie-tas-detail-na','BAG','After','BG260905_LTR_SIENNA_D.jpg',(0,320,1768,1646)),
]

def sfeerbeeld():
 source=OUTPUT/'productbeeldbewerking-sfeerbeeld.png'
 variants=[]
 with Image.open(source) as image:
  image=ImageOps.exif_transpose(image).convert('RGB')
  for width in (640,960,1752):
   height=round(image.height*width/image.width)
   target=OUTPUT/f'productbeeldbewerking-sfeerbeeld-{width}.webp'
   image.resize((width,height),Image.Resampling.LANCZOS).save(target,format='WEBP',quality=88,method=6)
   variants.append({'path':target.relative_to(ROOT).as_posix(),'width':width,'height':height,'bytes':target.stat().st_size})
 return {'name':'sfeerbeeld','source':source.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'crop':None,'variants':variants}

def main():
 OUTPUT.mkdir(parents=True,exist_ok=True)
 manifest=[]
 for name,group,side,filename,crop in ASSETS:
  source=SOURCE/group/side/filename
  with Image.open(source) as image:
   image=ImageOps.exif_transpose(image).convert('RGB')
   if crop:image=image.crop(crop)
   variants=[]
   for width in (480,960):
    height=width*3//4 if name.startswith('serie-') else width*2//3 if crop else width*5//4
    # Proportionele opname op hetzelfde rustige canvas; geen kleding/product uitrekken.
    content=ImageOps.contain(image,(width,height),Image.Resampling.LANCZOS)
    canvas=Image.new('RGB',(width,height),image.getpixel((0,0)))
    canvas.paste(content,((width-content.width)//2,(height-content.height)//2))
    target=OUTPUT/f'productbeeldbewerking-{name}-{width}.webp'
    canvas.save(target,format='WEBP',quality=89,method=6)
    variants.append({'path':target.relative_to(ROOT).as_posix(),'width':width,'height':height,'bytes':target.stat().st_size})
  manifest.append({'name':name,'source':source.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'crop':crop,'variants':variants})
 manifest.append(sfeerbeeld())
 (ROOT/'docs/PRODUCTBEELDBEWERKING_WEBMEDIA.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(f'{len(manifest)} beeldselecties, {sum(len(m["variants"]) for m in manifest)} WebP-bestanden, {sum(v["bytes"] for m in manifest for v in m["variants"]):,} bytes; originelen behouden.')

if __name__=='__main__':main()
