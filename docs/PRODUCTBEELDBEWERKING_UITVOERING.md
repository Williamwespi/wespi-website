# Productbeeldbewerking — lokale uitvoering en visuele herziening

Bijgewerkt op 9 november 2026 na de expliciete opdracht tot visuele herziening, toevoeging van € 2,49 per foto en herstel van de gedeelde afsluiting. Deze uitvoering vervangt de eerste paginaopbouw met twee subtiele achtergrond-/schaduwsliders, productserie, praktische vragen en eigen afsluitende CTA. Geen commit, push, deployment of echte mailverzending.

**Vervolgopdracht visuele kwaliteit, 9 november:** de opbouw is opnieuw vergeleken met Home, Kledingfotografie, Kledingbeeldbewerking en Automotive. De huidige versie hieronder gebruikt alleen horizontale beeldverlopen, grotere beeldcomposities en terugliggende accentvlakken. De eerder herstelde gedeelde footer is in deze vervolgopdracht niet gewijzigd.

## Paginaopbouw

Route blijft **/beeldbewerking/product**. Navigatie, titel, description, canonical, Open Graph, sitemap en Service-JSON-LD blijven behouden.

1. **Hero:** groot eindbeeld van de bruine suède sandaal, inclusief de originele schaduw. Alleen horizontale vervaging naar links; geen boven-/onder-/rechterfade. De algemene `.hero`, typografie en knoppen blijven de basis. Onder 900 px staan tekst/CTA en de volledige sandaal onder elkaar op hetzelfde neutrale bronvlak.
2. **Oriëntatiebalk:** drie korte ankerlinks naar voor/na, kleur en het tarief. De compacte goudaccenten volgen de pluspuntenbalk van Home/Kledingfotografie; ze geven ook directe navigatie op langere schermen.
3. **Grote vaste horlogevergelijking:** brede kop boven twee grotere 4:5-beelden, met een terugliggend zacht goudvlak achter het resultaat. Houder en witte steunen zichtbaar vóór, vrijstaand eindbeeld ernaast. Geen verandering aan de bronparen of productgeometrie.
4. **Asymmetrische retouchepresentatie:** het bord staat groter links, de pet in een kleinere terugliggende witte kaart rechts, met een dunne gouden bovenrand zoals de diensten-/tariefkaarten elders op Wespi. Een gedeeltelijk licht vlak doorbreekt de volle rechthoekige sectie. Onder 900 px staan de cases onder elkaar zodat de vergelijkingen groot blijven. Elk paar houdt twee volledige beelden en vaste Voor/Na-labels.
5. **Kleurafstemming:** de bestaande toegankelijke slider staat links en steekt boven/onder een ingesprongen zacht goudvlak uit; toelichting rechts. Dit volgt de linksgerichte AI-promotie en overvloeiende visuals van de referentiepagina's. Mobiel eerst tekst, dan de slider. Geen geforceerde uitlijning of verandering van de bronkleuren.
6. **Afwerkingsdetails:** een staand riemdetail naast een groter breed skibrilbeeld. Bij de bril wordt alleen lege achtergrond aan boven/onderkant buiten het vlak gehouden; de volledige bril blijft zichtbaar. De riembron behoudt zijn bestaande detailuitsnede.
7. **Tarief:** de rode tas staat links en vervaagt uitsluitend naar rechts. De witte tariefkaart rechts heeft de bestaande gouden bovenrand, **€ 2,49 per foto** en **Prijzen zijn exclusief btw.** Mobiel een compacte kaart boven de tas. Geen aanvullende voorwaarden of bedragen.
8. **Vier compacte stappen:** gecentreerde introductie en gouden stapnummers zoals elders op Wespi. Alle teksten blijven behouden, gevolgd door de ongewijzigde gedeelde ‘Samen aan de slag’-afsluiting.

‘Consistente productseries’, ‘Praktisch’ en de afzonderlijke productpagina-contactsectie zijn volledig verwijderd. De bijbehorende CSS is verwijderd in plaats van overschreven met aanvullende correcties.

## Herbeoordeelde beeldselectie

Alle dertien bestaande contactbladen met 106 paren zijn opnieuw visueel beoordeeld; 102 paren bevatten een aantoonbare wijziging. De vier identieke paren blijven uitgesloten. De zichtbare ingrepen krijgen voorrang boven de subtiele achtergrondbewerking van de rode tas en contactschaduw van de zwarte loafer uit het eerste voorbeeldenblok.

Bronpaden hieronder zijn relatief aan `bronmateriaal/productbeeldbewerking/AFTER Before Sample/`. Voor elke vergelijking wordt hetzelfde bestand uit `Before/` en `After/` gebruikt.

| Gebruik | Categorie / bronbestand | Onderbouwing |
|---|---|---|
| Hero | `SHOES/After/GWDISTA6_DBR01_PZ.jpg` | Bruine sandaal met bestaande contactschaduw; helder silhouet en warme materialen |
| Hoofdvergelijking | `JWELLERY/2559-2100072398543_1.jpg` | Opnamehouder en omgeving verwijderd |
| Vaste vergelijking | `CROCKERY/2625-2100067702058_3.jpg` | Hand/steun verwijderd, oppervlak bijgewerkt, product opnieuw gepositioneerd |
| Vaste vergelijking | `CAP/2589-2100066166400_1.jpg` | Paspop verwijderd; gewijzigd perspectief blijft eerlijk naast elkaar zichtbaar |
| Kleurslider | `CC/3090-2100074884327_1.jpg` | Duidelijke plaatselijke kleurafstemming bij dezelfde productpositie |
| Ondersteunend eindbeeld | `BELT/After/2582-2100068985146_4.jpg` | Diagonale compositie en gespdetail; de uitsnede van de bron is niet uitgebreid of verzonnen |
| Ondersteunend eindbeeld | `SWIM WEAR/After/2622-2100072112798_1.jpg` | Skibril met opgeschoonde neuszone; geen badkledinglabel |
| Tariefbeeld | `BAG/After/BG223706-RED.jpg` | Rood tasbeeld met rustige achtergrond als visuele ondersteuning |

Dit zijn **acht bronaanzichten, twaalf zichtbare afbeeldingen, vier echte vergelijkingen**. Alleen de geometrisch geschikte kleurvergelijking heeft een slider. De zichtbare voor-/na-beelden behouden hun eigen productgeometrie en worden proportioneel op het gezamenlijke canvas geplaatst.

## Media

De sandaal-WebP's uit de vorige opdracht blijven ongewijzigd: `productbeeldbewerking-sandaal-bruin-na-{480,960}.webp`, uitsnede `(0, 500, 3000, 2500)` uit de 3000×3000 After-bron. De volledige sandaal en oorspronkelijke schaduw blijven zichtbaar.

Nieuw in deze vervolgopdracht: `static/images/beeldbewerking/product/productbeeldbewerking-tas-rood-visual-na-{480,960}.webp`. Afgeleid van dezelfde authentieke `BAG/After/BG223706-RED.jpg`, met ruimere uitsnede `(0, 650, 1500, 1850)` en proportionele plaatsing op 480×320 en 960×640. Het hengsel heeft meer ruimte en raakt de bovenrand niet meer. Geen gegenereerde schaduw, retouche of verandering van het bestaande resultaat. Samen 37.134 bytes. De eerdere tas-WebP's blijven behouden.

De bestaande afgeleide webbeelden blijven bewaard, inclusief ongebruikte serie-/sliderbeelden. De generator en het manifest bevatten nu negentien selecties en 38 WebP's; de pagina laadt uitsluitend twaalf foto's, met passende `srcset`/`sizes`. Alleen de hero wordt eager geladen.

**Oorzaak verkeerde beeldverlopen:** de media hadden geen vervaging. De sandaal kreeg een extra verticale `::after`-overlay en een mobiele verticale `::before`-variant. De tas kreeg twee gecombineerde verlooplagen en een mobiele verticale override. Deze regels zijn verwijderd bij het herschrijven van de eigen CSS. Alleen één horizontale laag per visual blijft over: hero naar links, tas naar rechts. De contain-ruimte gebruikt exact de egale bronkleur `#e1e1e1`, zodat geen kader of verticale fade nodig is. Op mobiel sluit de hero aan op hetzelfde bronvlak; er is geen lichte strook langs de linkerzijde.

Reproduceren: `scripts/generate_productbeeldbewerking.py` met Pillow. Bronhashes, uitsneden, afmetingen en bestandsgrootten staan in `PRODUCTBEELDBEWERKING_WEBMEDIA.json`. Alle 212 oorspronkelijke JPG's zijn opnieuw tegen de inventarisatiehashes gecontroleerd: byte-identiek, niets toegevoegd, verplaatst, hernoemd of verwijderd. `bronmateriaal/` blijft genegeerd door Git en is niet publiek gemount.

## Oorzaak en herstel gedeelde afsluiting

`base.html` bevat de gedeelde footer-include correct. Geen CSS verbergt de CTA; de `display: none`-regels in `footer.css` betreffen uitsluitend decoratieve pseudo-elementen.

De oorzaak is de padvoorwaarde bovenaan `templates/onderdelen/footer.html`. In commit `fed8247` (‘Website optimalisatie en livegangvoorbereiding fase 1-4’) werden Contact, Offerte, Packshotfotografie, Kledingbeeldbewerking en Automotive uitgezonderd. Bij de eerdere lokale productpagina-bouw is ook Productbeeldbewerking toegevoegd om een eigen afsluiting niet te dupliceren.

Op expliciet verzoek vervalt nu de uitzondering voor de vier dienstenpagina's. Alle pagina's blijven dezelfde bestaande gedeelde CTA gebruiken; er zijn geen nieuwe afwijkende CTA-templates of gedeelde CSS-regels toegevoegd. Alleen Contact en Offerte blijven uitgezonderd vanwege hun aanwezige formulier. De eigen productpagina-afsluiting is verwijderd. Andere goedgekeurde pagina-inhoud is niet aangepast.

## Controles

- **42 regressietests geslaagd**: bestaande functionaliteit uit fase 1–4, AI-modellen, routes, SEO, formulieren met gemockte mail, geldige media en de gewijzigde footerselectie. Producttests controleren het bevestigde tarief/btw, de verwijderde onderdelen, twaalf beelden uit acht bronaanzichten en echte bronparen.
- **Productpagina in Chrome/Playwright op 1440, 1024, 768, 430, 375 en 320 px:** alle beelden gedecodeerd, gelijke voor-/na-vlakken, slider via knoppen/toetsenbord/muis/touch, aria-status, menu, interne links, tarief, canonical en één H1 gecontroleerd. Geen horizontale overflow, consolefouten of HTTP-/mediafouten. Inhoud en beelden blijven ook zonder JavaScript beschikbaar.
- **Gedeelde afsluiting websitebreed:** templatecontroles op alle zeventien GET-pagina's; browsercontrole van alle vijftien geregistreerde publieke pagina's op 1440, 768 en 375 px. Op dertien pagina's is de gemeenschappelijke CTA zichtbaar en bruikbaar; Contact/Offerte behouden hun formulier. Geen dubbele contact-id's, console- of HTTP-fouten.
- Hero, hoofdvergelijking, volledige pagina, tabletindeling en mobiele weergave visueel beoordeeld. De tablet-hero is gestapeld om overlap en productafsnijding te voorkomen; de tariefafbeelding gebruikt proportionele `contain` om de hele tas te tonen.
- De vervolgopdracht is visueel beoordeeld op **375, 430, 768 en 1440 px**, naast de technische checks op 320 en 1024 px. De tablet-pet is vergroot door de cases eerder te stapelen. Het mobiele bronvlak en de leesvolgorde van de horlogetoelichting zijn verfijnd. De browsercontrole controleert nu ook de echte boven-/onderrandpixels van beide visuals: aan de ongefade kant blijven ze grijs, niet wit. Richting van de overlay, ontbreken van de extra hero-laag en geen beeldfilters gecontroleerd.
- Screenshots: `docs/productbeeldbewerking-{1440,1024,768,430,375,320}.png`, `productbeeldbewerking-hero-{breedte}.png` en `productbeeldbewerking-vergelijking-{1440,375}.png`. Dit is browseremulatie, geen test op fysieke toestellen.
- Aanvullende detailopnames van deze vervolgopdracht: `productbeeldbewerking-tarief-{1440,768,430,375}.png` en `productbeeldbewerking-kleur-{1440,768,430,375}.png`.

## Bestanden van de eerste visuele herziening en het footerherstel

- `templates/productbeeldbewerking.html`, `static/css/beeldbewerking/product.css`: herziene pagina en eigen styling.
- `templates/onderdelen/footer.html`: gedeelde CTA hersteld op dienstenpagina's.
- `scripts/generate_productbeeldbewerking.py`, `docs/PRODUCTBEELDBEWERKING_WEBMEDIA.json`: nieuwe hero-afgeleiden; twee nieuwe WebP's in `static/images/beeldbewerking/product/`.
- `tests/test_productbeeldbewerking.py`, `tests/test_livegang_fase3.py`, `tests/check_productbeeldbewerking_browser.py`, nieuw `tests/check_footer_browser.py`: gerichte regressie- en browsercontroles.
- Dit verslag, `BESLUITEN.md`, `PROJECTKOMPAS.md` en controlescreenshots.

Geen wijzigingen aan routes, navigatie, algemene styling, SEO-instellingen, andere pagina-inhoud, bestaande video's, bronbestanden, Pythonomgeving of dependencies. Alleen lokaal gewerkt: http://127.0.0.1:8765/beeldbewerking/product.

## Bestanden van de vervolgopdracht visuele kwaliteit

- `templates/productbeeldbewerking.html` en `static/css/beeldbewerking/product.css`: nieuwe compositie en uitsluitend horizontale fades; bestaande inhoud behouden, kleine navigatielabels toegevoegd.
- `scripts/generate_productbeeldbewerking.py`, `docs/PRODUCTBEELDBEWERKING_WEBMEDIA.json` en twee nieuwe `productbeeldbewerking-tas-rood-visual-na-*.webp`-bestanden.
- `tests/test_productbeeldbewerking.py` en `tests/check_productbeeldbewerking_browser.py`: actuele mediaselectie en beeldrand-/richtingcontrole.
- `docs/BESLUITEN.md`, `docs/PROJECTKOMPAS.md`, dit verslag en controlescreenshots.

Gedeelde footer, algemene navigatie, routes, alle andere pagina's en bestaande webmedia zijn in deze vervolgopdracht ongewijzigd.

## Definitieve visuele herziening ? 11 november 2026

Deze expliciete vervolgopdracht actualiseert de oudere paginaopbouw hierboven:

- Horloge: compacte tekst links en twee authentieke bronbeelden rechts; houdergerichte verkooptekst verwijderd. Retouche wordt bij bord/pet uitgelegd.
- Retouche: open asymmetrische cases op wit, zonder de eerdere binnenkaart en het gedeeltelijke grijze sectievlak.
- Sfeerbeeld: goedgekeurde PNG tussen retouche en kleur, met aangeleverde kop en beschrijving. Rechts groot beeld, links tekst, lichtgrijze achtergrond en uitsluitend horizontale fade naar links. Onder 900px tekst v??r het volledige proportionele beeld. Het mobiele beeld staat van rand tot rand zonder kaart of kader; geen verticale fade.
- Drie WebP's (640/960/1752px; 21.516/41.238/109.764 bytes), samen circa 172kB. PNG behouden; generator en bronhashmanifest bijgewerkt zonder eerdere afgeleiden opnieuw te genereren.
- Kleur: bestaande slider met gebogen terugliggend zacht goudaccent. Details: groter staand riembeeld naast een groot, lager geplaatst breed brilbeeld; mobiel een compacte riem/tekstcompositie en daarna de bril.
- Hero, sandaal- en tasverloop, werkende vergelijking, ? 2,49 exclusief btw, SEO, navigatie, CTA's en gedeelde footer behouden. Geen andere pagina's of gedeelde componenten gewijzigd.

42 bestaande regressietests geslaagd. De mediaverwachtingen zijn bijgewerkt naar 13 zichtbare beelden uit negen bronaanzichten en twintig manifestitems. Alle oorspronkelijke bronhashes blijven gecontroleerd. Browsercontrole omvat daarnaast sfeerbeeldrichting en mobiele tekstvolgorde. Bij fractionele gridbreedtes is maximaal ??n pixel afrondingsverschil tussen de vaste beeldparen toegestaan.

Gewijzigd: eigen template/CSS, generator, webmediamanifest, twee bestaande producttests, BESLUITEN.md, PROJECTKOMPAS.md, dit verslag. Toegevoegd: drie sfeer-WebP's. Controlescreenshots van de volledige pagina, hero, vergelijking, tarief, kleur en sfeer in docs bijgewerkt/toegevoegd.

De bestaande Python 3.12-startkoppeling was niet uitvoerbaar in deze sessie. Controles gebruiken de aanwezige Python 3.13 met tijdelijke testdependencies buiten de projectmap; projectomgeving en requirements zijn niet gewijzigd. De browser gebruikt de reeds draaiende lokale server op 127.0.0.1:8765. Geen commit, push, deployment of echte mail.

Visuele eindcontrole uitgevoerd op 375, 430, 768 en 1440px (volledige pagina en sectieopnames). Browsercontroles slagen ook op 320 en 1024px: beelden, richting van fades, leesvolgorde, slider via toetsenbord/knoppen/pointer/touch, interne links, SEO, prijs en gedeelde CTA. Geen overflow, console- of HTTP-/mediafouten. Screenshots zijn browseremulaties, geen fysieke toestellen.
