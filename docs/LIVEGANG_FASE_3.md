# Livegang fase 3 - prestaties en visuele verfijning

Uitgevoerd op 5 november 2026. Na de gebruikslimiet is de bestaande Git-diff gecontroleerd en is verdergewerkt vanaf de bewaarde fase-3-beginsituatie. Bestaande wijzigingen zijn behouden. Dit verslag beschrijft uitsluitend fase 3; de totale Git-diff bevat ook eerdere opdrachten en wijzigingen in de lokale Pythonomgeving.

## Afbeeldingen

60 gebruikte bronbeelden geoptimaliseerd: **178,952,675 naar 59,893,576 bytes** voor de volledige WebP-versies (**66.53% kleiner**). Daarnaast zijn proportionele varianten van 600 en, bij voldoende bronresolutie, 1200 pixels breed gemaakt: 179 nieuwe WebP-bestanden in totaal. Originele bestanden zijn behouden en hebben nog exact hun oorspronkelijke bestandsgrootte.

- Transparante en product-PNG-beelden gebruiken lossless WebP. De zichtbare pixels van de 8-bits lossless beelden zijn gelijk aan de bron, gecontroleerd op witte en zwarte achtergrond.
- Opaque fotografische beelden gebruiken WebP kwaliteit 94. De laagste gemeten SSIM is 0,973777; daarnaast zijn detailuitsneden en paginaweergaven visueel vergeleken.
- De zonnebrilbron is 16-bits PNG. WebP is 8-bits; de paginavariant heeft een zeer kleine kwantisatieafwijking. De lightbox gebruikt daarom het oorspronkelijke 16-bits bestand. JPEG-lightboxes behouden eveneens het oorspronkelijke detailbestand.
- Alle volledige versies behouden bronafmetingen en beeldverhouding. Transparantie is gecontroleerd. Geen nieuwe beeldinhoud, uitsneden of composities.
- Een Jinja-afbeeldingenregister levert srcset, proportionele varianten, lazy loading en afzonderlijke volledige zoombronnen. Hero- en sliderbeelden behouden volledige resolutie en bestaande CSS-uitsneden. Niet-geregistreerde toekomstige afbeeldingen blijven werken.

### Werkelijk gekozen paginabeelden

Som van unieke, door de browser gekozen afbeeldingsbestanden bij geforceerd laden van alle beelden (bytes). Dit is geen first-load-, LCP- of volledige netwerkmeting; CSS, video en andere middelen zijn niet meegerekend. Verwijderde dubbele contact-CTA-beelden tellen mee in de afname.

| Pagina | 1440px voor | 1440px na | 375px voor | 375px na |
|---|---:|---:|---:|---:|
| / | 16,044,138 | 1,922,739 | 16,044,138 | 1,255,293 |
| /productfotografie/kledingfotografie | 41,278,351 | 7,333,218 | 41,278,351 | 2,728,092 |
| /productfotografie/packshotfotografie | 45,283,606 | 7,966,056 | 45,283,606 | 3,792,044 |
| /data/productdata | 7,589,102 | 728,094 | 7,589,102 | 460,978 |
| /slimmer-werken | 6,434,310 | 753,250 | 6,434,310 | 571,170 |

### Bestandsgroottes per bronbeeld

Paden hieronder zijn relatief aan `static/`. Per bron bestaan naast de volledige `.webp` ook `-600.webp` en, indien kleiner dan de bron, `-1200.webp` met dezelfde stam. De tabel omvat daarmee alle 179 nieuwe mediabestanden.

| Bronbestand | Origineel bytes | WebP volledig bytes | 600px bytes | 1200px bytes |
|---|---:|---:|---:|---:|
| `images/beeld/kleding-bodyform-jurk.png` | 23048704 | 1465024 | 114988 | 441874 |
| `images/packshotfotografie/accessoirefotografie-blauwe-tas-wespi.png` | 23048704 | 3753278 | 314076 | 1114418 |
| `images/kledingfotografie/ghost-mannequin-jas-kledingfotografie.png` | 8965749 | 709652 | 160690 | 573946 |
| `images/kledingfotografie/bodyform-blauw-vest-achterkant-kledingfotografie.png` | 8652218 | 5528870 | 438834 | 1683816 |
| `images/beeld/kleding-bodyform-short.png` | 8580607 | 4978556 | 488430 | 1725640 |
| `images/kledingfotografie/bodyform-blauw-vest-kledingfotografie-wespi.png` | 8498733 | 5463466 | 417394 | 1620314 |
| `images/beeld/kleding-bodyform-jas.png` | 3891735 | 2569618 | 178900 | 747454 |
| `images/kledingfotografie/bodyform-broek-kledingfotografie-wespi.png` | 3835430 | 2316138 | 156266 | 637176 |
| `images/packshotfotografie/accessoirefotografie-sok-wespi.png` | 3559343 | 1805142 | 159824 | 587326 |
| `images/packshotfotografie/productfotografie-wandklok-wespi.png` | 3345791 | 1882198 | 202322 | 701122 |
| `images/beeldbewerking/kleding/productfoto-kleding-1.jpg` | 3213708 | 1386144 | 85848 | 402652 |
| `images/beeld/beeldbewerking-productfoto-broek-wespi.png` | 2675867 | 1682622 | 462590  - |
| `images/packshotfotografie/packshotfotografie-detail-accessoire.png` | 2520966 | 1535632 | 233034 | 949244 |
| `images/slimmer-werken/slimmer-werken-hero.png` | 2495264 | 387480 | 101218 | 274692 |
| `images/home/hero-kleding.png` | 2410365 | 362452 | 78852 | 239956 |
| `images/kledingfotografie/ghost-mannequin-hoodie-kledingfotografie.png` | 2244740 | 1222018 | 129482 | 465460 |
| `images/beeld/hero-beeld-productfotografie-wespi.png` | 2239560 | 267316 | 50154 | 177512 |
| `images/kledingfotografie/platte-kledingfotografie-sokken.png` | 2212305 | 1357296 | 243772 | 894344 |
| `images/packshotfotografie/packshot-schoenenfotografie.png` | 2141981 | 1341366 | 148120 | 539770 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-01-voor.jpg` | 2094868 | 1689412 | 146034 | 526440 |
| `images/home/dienst-beeld.png` | 2093085 | 258138 | 58770 | 173880 |
| `images/over-wespi/wespi-vlag.jpg` | 2077354 | 1394804 | 64258 | 136710 |
| `images/kledingfotografie/ai-modelfotografie/ai-modelfotografie-hero.jpg` | 1992405 | 444888 | 74680 | 208526 |
| `images/beeldbewerking/beeldbewerking/kleding/tshirt-blauw-voorzijde.jpg` | 1991964 | 586130 | 30162 | 139202 |
| `images/productdata/productdata-werkwijze.png` | 1991860 | 171602 | 46876 | 119606 |
| `images/contact/contact-hero.png` | 1981717 | 203934 | 46560 | 115640 |
| `images/home/cta-techniek.png` | 1978592 | 268410 | 63068 | 162358 |
| `images/home/dienst-slimmer-werken.png` | 1943223 | 211894 | 60060 | 147358 |
| `images/kledingfotografie/werkwijze-kledingfotografie-wespi.png` | 1942710 | 223738 | 50906 | 153686 |
| `images/kledingfotografie/ai-modelfotografie/ai-model-01-voor.jpg` | 1927234 | 367516 | 47040 | 121478 |
| `images/home/dienst-data.png` | 1920516 | 237314 | 60388 | 170556 |
| `images/beeld/packshot-schoen-wespi.png` | 1917289 | 833582 | 124712 | 518868 |
| `images/beeldbewerking/beeldbewerking-hero.png` | 1912159 | 216988 | 59668 | 156902 |
| `images/slimmer-werken/slimmer-werken-prijzen-magazijn.png` | 1887466 | 190718 | 47634 | 130424 |
| `images/packshotfotografie/accessoirefotografie-zonnebril-wespi.png` | 1867903 | 523914 | 75300 | 226240 |
| `images/kledingfotografie/ai-modelfotografie/ai-model-01-achter.jpg` | 1867141 | 325796 | 42014 | 106768 |
| `images/packshotfotografie/packshot-schoenen-hoofdfoto.png` | 1857481 | 1308870 | 316034 | 1213102 |
| `images/home/waarom-wespi-barcode.png` | 1816156 | 221092 | 50066 | 173096 |
| `images/productdata/productdata-prijzen.png` | 1776550 | 208496 | 54726 | 149822 |
| `images/productdata/productdata-hero.png` | 1769112 | 223320 | 54104 | 141208 |
| `images/home/slimmer-werken-workflow.png` | 1737279 | 198728 | 52310 | 131660 |
| `images/home/data-structuur.png` | 1629197 | 121658 | 32454 | 85654 |
| `images/packshotfotografie/productfotografie-keramische-schaal-wespi.png` | 1599290 | 927090 | 147882 | 601388 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-01-na.jpg` | 1536071 | 982690 | 139502 | 438364 |
| `images/packshotfotografie/packshot-schoenen-slipper.png` | 1267993 | 775610 | 108846 | 381842 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-03-na.jpg` | 1233709 | 1022882 | 67388 | 312858 |
| `images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-2.jpg` | 1085924 | 323616 | 79094 | 215802 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-03-voor.jpg` | 1029138 | 798248 | 62238 | 267422 |
| `images/beeldbewerking/kleding/kledingbeeldbewerking-werkwijze.jpg` | 1010491 | 917908 | 113956 | 447238 |
| `images/beeldbewerking/beeldbewerking/automotive/voorbeelden/auto-voorbeeld-showroom.jpg` | 941175 | 275364 | 56780 | 182702 |
| `images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-3.jpg` | 927634 | 256336 | 58716 | 178114 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-02-voor.jpg` | 908333 | 612798 | 71840 | 241036 |
| `images/packshotfotografie/packshot-accessoiresfotografie-riem.png` | 875714 | 488652 | 73156 | 217778 |
| `images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-7.jpg` | 874585 | 244818 | 59830 | 173188 |
| `images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-achtergrond-8.jpg` | 853584 | 209274 | 55590 | 147476 |
| `images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-4.jpg` | 722909 | 166022 | 41898 | 110986 |
| `images/beeldbewerking/kleding/voor-na/kledingbewerking-02-na.jpg` | 710369 | 484346 | 61576 | 190748 |
| `images/beeld/beeldbewerking-auto-wespi.png` | 659480 | 420470 | 80048 | 284114 |
| `images/packshotfotografie/packshot-schoenen-sneaker.png` | 588370 | 311818 | 79374 | 215960 |
| `images/beeldbewerking/beeldbewerking/automotive/voorbeelden/auto-achtergrond-gepersonaliseerde-showroom.jpg` | 572875 | 230424 | 62120 | 176652 |

## Gerichte visuele verbeteringen

- Onvoldoende contrasterende informatieve goudteksten zijn lokaal donker goud (`#755b0a`) of donkergrijs/zwart gemaakt; ook prijzen, juridische links en relevante grijze labels. De globale goudvariabele, gele vlakken, knoppen en decoratieve accenten blijven behouden. Foto-overlays zijn visueel beoordeeld; dit is geen volledige WCAG-certificering.
- Mobiel: Slimmer werken toont invoer en resultaat naast elkaar in compactere voorbeeldkaarten; Home heeft natuurlijk hoge projectkaarten en minder loze dienstruimte; Packshot heeft kleinere beeldvakken en padding; Kledingfotografie een compactere bodyformpresentatie en merkenruimte; Productdata gerichte kleinere sectieafstanden. Inhoud en beelden blijven aanwezig. Geen algemene verkleining of wijziging van desktopindelingen.
- Algemene contactuitnodiging weggelaten op Contact, Offerte, Packshotfotografie, Kledingbeeldbewerking en Autobeeldbewerking, omdat daar al een formulier of directe contactmogelijkheid staat. De footer en specifieke contactroutes blijven aanwezig. Op Productdata en Slimmer werken blijft de algemene uitnodiging logisch behouden.
- Na expliciete eigenaarbevestiging: exclusief btw vermeld bij bestaande Kledingfotografie-, Packshotfotografie-, losse Productdata- en Slimmer werken-prijzen. Geen bedragen of eenheden gewijzigd.
- Cacheversies van aangepaste CSS/JS en afhankelijke imports zijn bijgewerkt. Het template start weer direct met de doctype, zodat de afbeeldingenimport geen quirksmode veroorzaakt.

## Verificatie

| Controle | Resultaat |
|---|---|
| Serverregressies | 21 tests geslaagd: 15 fase-1-tests en 6 fase-3-tests |
| Formulieren | Contact en Offerte: gesimuleerd succes/falen, verplichte/ongeldige invoer, spambeveiliging, SMTP-velden en gegevensbehoud; geen echte e-mail |
| Routes, links, redirects | Bestaande routes en gewijzigde links uit fase 1 blijven slagen; bevestigde oude routes 301, bestemmingen 200 |
| Browser | 16 pagina's op 1440, 768, 430 en 375px: 64 combinaties, standards mode, geen kapotte beelden, geen horizontale overflow of vervormde beelden |
| Console | Geen nieuwe consolefouten tijdens de browserronde |
| Mobiele volgorde fase 2 | 14 concrete secties op beide mobiele breedtes: 28 controles geslaagd, geen overlap |
| Navigatie | Muisroute, vertrekvertraging, klik/buitenklik, Enter/Tab/Space/pijlen/Escape, focusherstel, AI-link, touch en breedtewissel geslaagd |
| Lage mobiele schermen | Touchscroll en onderste contactlink geslaagd op 375x667 en 768x600 |
| Interacties | 24 controles: automotive- en kledingslider toetsenbord/pointer, kleding-/packshotlightbox, AI-dialoog en Productdata-details op alle vier breedtes |
| Alle productvergrotingen | 9 packshot- en 5 bodyformbeelden geopend, correct volledig detailbestand geladen, sluiting met Escape geslaagd |
| Media | Alle 60 bron-/volledige beeldafmetingen, transparantie, oorspronkelijke bestanden en varianten gecontroleerd |
| Behoud | Alle prijsreeksen behouden; automotive-herohoogte identiek op alle vier breedtes; formulierroutecode, offerte-template, header-template en header-CSS gelijk aan begin fase 3 |
| Juridisch | Juridische inhoud gelijk aan begin fase 3; alleen stylesheetcacheversies gewijzigd |

Tests herhaalbaar met `py -3.12 -B -m unittest discover -s tests -v`. Browsercontroles zijn uitgevoerd in lokaal Chromium met muis-, toetsenbord- en touchsimulatie. Voor/na-screenshots en meetgegevens staan in de tijdelijke validatiemap `%TEMP%/wespi-fase3/`; deze zijn geen noodzakelijke applicatiebestanden.

## Gewijzigde bestanden

Onderstaande lijst vergelijkt met de beginsituatie van fase 3, inclusief nieuwe helper/test/documentatie. Sommige CSS-bundels/templates wijzigen uitsluitend vanwege cacheversies. De mediabestanden staan in de tabel hierboven.

- `docs/BESLUITEN.md`
- `docs/LIVEGANG_FASE_3.md`
- `docs/PROJECTKOMPAS.md`
- `static/css/basis.css`
- `static/css/beeld.css`
- `static/css/beeld/diensten.css`
- `static/css/beeld/hero.css`
- `static/css/beeld/waarom-beeld.css`
- `static/css/diensten.css`
- `static/css/footer.css`
- `static/css/hero.css`
- `static/css/juridisch.css`
- `static/css/kledingfotografie.css`
- `static/css/kledingfotografie/bodyform.css`
- `static/css/kledingfotografie/hero.css`
- `static/css/kledingfotografie/klanten.css`
- `static/css/kledingfotografie/platte-fotografie.css`
- `static/css/kledingfotografie/styleshoots.css`
- `static/css/kledingfotografie/werkwijze.css`
- `static/css/offerte.css`
- `static/css/over-wespi/over-wespi.css`
- `static/css/packshotfotografie/accessoires.css`
- `static/css/packshotfotografie/hero.css`
- `static/css/packshotfotografie/inhoud.css`
- `static/css/packshotfotografie/overige-producten.css`
- `static/css/packshotfotografie/packshotfotografie.css`
- `static/css/packshotfotografie/schoenen.css`
- `static/css/packshotfotografie/werkwijze.css`
- `static/css/productdata/hero.css`
- `static/css/productdata/intro.css`
- `static/css/productdata/prijzen.css`
- `static/css/productdata/service.css`
- `static/css/productdata/usp-balk.css`
- `static/css/productdata/volume.css`
- `static/css/productdata/werkwijze.css`
- `static/css/projecten.css`
- `static/css/slimmer-werken/hero.css`
- `static/css/slimmer-werken/mogelijkheden.css`
- `static/css/slimmer-werken/prijs.css`
- `static/js/main.js`
- `templates/ai-modelfotografie.html`
- `templates/algemene-voorwaarden.html`
- `templates/base.html`
- `templates/contact.html`
- `templates/kledingbeeldbewerking.html`
- `templates/onderdelen/automotive/achtergronden.html`
- `templates/onderdelen/automotive/hero.html`
- `templates/onderdelen/automotive/mogelijkheden.html`
- `templates/onderdelen/beeld/diensten.html`
- `templates/onderdelen/beeld/hero.html`
- `templates/onderdelen/beeldbewerking/diensten.html`
- `templates/onderdelen/beeldbewerking/hero.html`
- `templates/onderdelen/beeldvarianten.html`
- `templates/onderdelen/diensten.html`
- `templates/onderdelen/footer.html`
- `templates/onderdelen/hero.html`
- `templates/onderdelen/kledingfotografie/ai-promotie.html`
- `templates/onderdelen/kledingfotografie/bodyform.html`
- `templates/onderdelen/kledingfotografie/platte-fotografie.html`
- `templates/onderdelen/kledingfotografie/werkwijze.html`
- `templates/onderdelen/packshotfotografie/accessoires.html`
- `templates/onderdelen/packshotfotografie/categorieen.html`
- `templates/onderdelen/packshotfotografie/hero.html`
- `templates/onderdelen/packshotfotografie/overige-producten.html`
- `templates/onderdelen/packshotfotografie/schoenen.html`
- `templates/onderdelen/productdata/hero.html`
- `templates/onderdelen/productdata/prijzen.html`
- `templates/onderdelen/productdata/werkwijze.html`
- `templates/onderdelen/projecten.html`
- `templates/onderdelen/slimmer-werken-v2/applicaties.html`
- `templates/onderdelen/voordelen.html`
- `templates/over-wespi.html`
- `templates/privacyverklaring.html`
- `templates/slimmer-werken-v2.html`
- `templates/slimmer-werken.html`
- `tests/test_livegang_fase3.py`

## Resterende aandachtspunten

- Werkelijke SMTP-aflevering, productie-instellingen en hosting/proxyredirects blijven de productiecontroles uit fase 1. Er is geen echte e-mail verzonden.
- Fysieke iOS/Safari- en Firefoxcontroles en praktijkmetingen van Core Web Vitals zijn niet uitgevoerd. De genoemde afbeeldingsbesparing is geen gegarandeerde laadtijdwinst.
- Video is niet opnieuw gecodeerd; dit valt buiten de afgesproken afbeeldingsoptimalisatie. Ongebruikte originele grote bronbestanden zijn eveneens behouden.
- Volledige zoom kan bewust een groter origineel laden. Neem de nieuwe WebP-bestanden en macro mee bij deployment; geen losse template-update zonder bijbehorende media.
- Bestaande overige aandachtspunten uit de audit blijven staan waar zij buiten fase 3 vallen. Geen nieuwe tariefonzekerheden na de btw-bevestiging.

Fase 3 is gereed voor beoordeling. Fase 4 is niet gestart. Er is niet gecommit of gepusht.
