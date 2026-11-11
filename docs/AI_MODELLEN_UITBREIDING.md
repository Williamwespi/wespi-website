# AI-modelfotografie: uitbreiding naar vijf modellen

Lokaal uitgevoerd op 7 november 2026. Geen commit, push, deployment of echte mailverzending. Wacht op beoordeling door de eigenaar.

## Visuele correcties — 11 november 2026

De expliciete vervolgopdracht actualiseert drie punten uit de oudere uitvoering hieronder:

- Bodyform: flexibele kolommen binnen de bestaande tabletregel. Op 768px circa 306,66px + 390,31px + 23,04px tussenruimte binnen een 720px-container. Alle vijf kledingbeelden passen. Desktop en de mobiele enkele kolom behouden hun maat en tussenruimte.
- AI-promotie: dezelfde bronfoto volledig en proportioneel, inclusief de schoenen. Geen beeldkader of gouden onderlijn; gecombineerde horizontale/verticale CSS-maskers laten de lege beeldranden subtiel in de bestaande zachtgouden achtergrond uitlopen. Kop, tekst, prijs, CTA en mobiele leesvolgorde behouden.
- Mobiele AI-tarieven: het bestaande modelbeeld links naast de bestaande toelichting in dezelfde gridrij. Een centrale uitsnede verwijdert lege zijruimte; zachte witte randen verbinden het beeld met toelichting en prijskaarten. Geen los afbeeldingsvlak boven de toelichting. Boven 760px blijft de presentatie ongewijzigd.

Visueel gecontroleerd op 375, 430, 768 en 1440px. Alle 42 bestaande regressietests slagen. De bestaande AI-browsercontrole slaagt op deze breedtes plus 320px: vijf modellen, 46 foto's, vijf video's na klik, uitlijning, galerijen, focus/Escape en geen overflow of console-/HTTP-fouten. Aanvullend zijn alle 46 fotovergrotingen, de vijf bodyformvergrotingen, interne links, menuverwijzingen en tarieven gecontroleerd. Alle vijf kledingbeelden liggen op de vier gevraagde breedtes binnen de viewport. Screenshots uitsluitend in de tijdelijke lokale controlemap buiten het project; geen fysieke toesteltest.

Gewijzigd: `static/css/kledingfotografie/bodyform.css`, `static/css/kledingfotografie/ai-promotie.css`, `static/css/kledingfotografie/ai-modelfotografie.css`; uitsluitend stylesheet-cacheversies in `templates/kledingfotografie.html` en `templates/ai-modelfotografie.html`; dit verslag en `docs/BESLUITEN.md`. Geen bronafbeeldingen, modelgegevens, scripts, andere pagina's, gedeelde componenten of tarieven gewijzigd. Geen commit, push of deployment.

## Resultaat

- Vijf modellen: Herenmodel, Damesmodel, Jongensmodel (4 jaar), Meisjesmodel (10 jaar), Zwangerschapsmodel.
- Respectievelijk 4/6/6/6/6 AI-modelbeelden: 28 totaal. Daarnaast 18 oorspronkelijke productfoto's en vijf video's.
- Twee modelkaarten naast elkaar op desktop/tablet; op mobiel één kaart per rij. Iedere kaart bevat een herkenbaar videovoorbeeld, twee foto's en ‘Bekijk alle beelden’.
- De galerij bevat video, alle AI-modelbeelden en daarna de bijbehorende oorspronkelijke productfoto's, met een duidelijk onderscheid in het bijschrift. Pijlen, toetsenbord, Escape, focusbegrenzing/-herstel en veegbediening zijn beschikbaar. Video's behouden hun eigen toetsenbordbediening.
- Transparante dialoog zonder wit kader, met donkere overlay en volledig zichtbare media via `object-fit: contain`.
- Vooraf worden geen videobronnen geladen. Een expliciete klik op de videopreview opent en start de video gedempt. Bij galerijnavigatie naar een video blijft deze gepauzeerd. Sluiten en bladeren ruimen de speler op.
- De gevraagde tekst over AI, Photoshop en handmatige controles staat compact tussen voorbeelden en tarieven.
- Hero, navigatie, overige pagina's, SEO-title/description/canonical, structured data, bestaande tarieven inclusief combinatiepakket, btw, werkwijze en CTA's zijn behouden. Het herenbeeld bij de tarieven gebruikt nu eveneens de nieuwe aangeleverde versie.

## Nieuwe bestanden en mappen

- `routes/ai_modellen.json`: expliciete koppeling van modellen, media, afmetingen en beschrijvende alt-teksten.
- `static/images/{herenmodel,damesmodel,jongensmodel,meisjesmodel,zwangerschapsmodel}/`: alle 46 aangeleverde WebP-bestanden met ongewijzigde namen en inhoud.
- De ondermap `preview/` van elk model: 46 aanvullende WebP-previews, proportioneel verkleind tot maximaal 480 × 720 pixels. De originele WebP's blijven beschikbaar voor vergroting; zichtbare foto's hebben responsive bronverwijzingen en lazy-loading.
- `static/videos/{herenmodel,damesmodel,jongensmodel,meisjesmodel,zwangerschapsmodel}/`: vijf ongewijzigde MP4-bestanden.
- `tests/test_ai_modellen.py`: drie regressietests voor media-inventaris, byte-identiek behoud van ZIP-media en de gerenderde pagina zonder vooraf geladen videobronnen.
- `tests/check_ai_browser.py`: herhaalbare Playwright/Chrome-controle tegen een lokaal draaiende app op poort 8765.
- `docs/ai-contactsheet.jpg`: visuele inventaris voor controle van kleding en productfoto's.
- `docs/ai-modellen-{1440,768,430,375}.png` en `docs/ai-galerij-{1440,375}.png`: screenshots van de modelkaarten en donkere vergroting.
- Dit verslag: `docs/AI_MODELLEN_UITBREIDING.md`.

De aangeleverde ZIP-bestanden blijven ongewijzigd in de hoofdmap staan. Hun LEESMIJ en CSV zijn geïnspecteerd en niet als publieke media uitgepakt.

## Aangepaste bestanden

- `routes/paginas.py`: uitsluitend de AI-route leest de expliciete modelgegevens; prijslijst en andere routes zijn behouden.
- `templates/ai-modelfotografie.html`: vijf modelkaarten, galerijgegevens/-bediening, nieuwe toelichting en nieuw herenbeeld bij tarieven.
- `static/css/kledingfotografie/ai-modelfotografie.css`: compacte media-indeling, mobiele weergave en donkere kaderloze dialoog; uitsluitend op de AI-pagina geladen.
- `static/js/ai-modelfotografie.js`: modelgebonden galerij, navigatie, video's na klik, focusbeheer en mobiele veegbediening.
- `static/images/kledingfotografie/ai-modelfotografie/README.md`: actuele mediastructuur en gedrag.
- `tests/test_livegang_fase4.py`: één regel in de bestaande ASGI-testhelper specificeert HTTP ASGI 2.4, zodat de statische-media-/compressietest niet blijft wachten in de oudere disconnect-luisterlus van Starlette. Applicatiegedrag is hiervoor niet aangepast.
- `docs/BESLUITEN.md` en `docs/PROJECTKOMPAS.md`: deze expliciet opgedragen uitbreiding en lokale beoordelingsstatus vastgelegd.

## Verwijderde oude media

Na controle op actieve bronverwijzingen zijn alleen deze twee bestanden verwijderd:

- `static/images/kledingfotografie/ai-modelfotografie/ai-model-01-video.mp4`
- `static/images/kledingfotografie/ai-modelfotografie/ai-model-01-poster.jpg`

De oude voorfoto en WebP-varianten blijven behouden omdat Kledingfotografie die nog gebruikt. De oude achterfoto en varianten blijven in het bestaande gedeelde beeldregister behouden. Er is niets aan dat register of de andere pagina gewijzigd.

## Verificatie

- **37 regressietests geslaagd**: 34 bestaande tests plus drie nieuwe tests. Hierbij blijven formulieren met gesimuleerde SMTP, routes, prijzen/btw, SEO, sitemap/robots, compressie, beveiligingsheaders en bestaande beeldvarianten gecontroleerd.
- **Browsercontrole geslaagd op 1440, 768, 430 en 375 pixels**, in Chrome via Playwright; mobiele breedtes met mobiele/touch-emulatie.
- Alle vijf modelkaarten, vijf videokoppelingen, 28 AI-modelbeelden en 18 oorspronkelijke productfoto's gecontroleerd.
- Iedere foto geopend in de galerij en gecontroleerd op succesvolle beelddecodering; iedere video expliciet gestart en gecontroleerd op gedempte weergave en succesvolle decodering.
- Geen MP4-netwerkverzoeken vóór interactie; bij galerijnavigatie naar video geen automatisch afspelen.
- Geen horizontale overflow, ontbrekende assets, HTTP-mediafouten of JavaScript-uitvoeringsfouten aangetroffen.
- Navigatie met pijlen, Escape, Tab/Shift+Tab, focusherstel en mobiele veegbediening gecontroleerd.
- Transparante dialoogachtergrond gecontroleerd; media visueel beoordeeld op verhoudingen, kledingkoppeling en oriëntatie. De witte/lichtgrijze achtergrond die deel uitmaakt van een aangeleverde foto blijft natuurlijk onderdeel van die foto.
- Alle uitgepakte bronmedia zijn met SHA-256 vergeleken met de ZIP-inhoud en zijn byte-identiek.

## Omgeving en aandachtspunten

De aanwezige `.venv` verwijst naar een niet beschikbare Python 3.12-installatie. Verificatie is daarom uitgevoerd met de beschikbare Python 3.13 en tijdelijk lokaal geïnstalleerde testdependencies. De bestaande `.venv`, requirements en reeds aanwezige wijzigingen daarin zijn niet aangepast. Tijdelijke testdependencies zijn na de controles opgeruimd. Voor herhalen van de browsercontrole zijn een werkende Python-omgeving, Playwright en Chrome nodig; regressies starten met `python -B -m unittest discover -s tests`.

De browsercontrole gebruikt emulatie en vervangt geen beoordeling op fysieke iOS-/Android-toestellen. Er is geen publicatie uitgevoerd; de pagina wacht op jouw visuele beoordeling.

## Compact modellenoverzicht — 9 november 2026

- Op expliciet verzoek vervangen vijf kolommen op desktop, drie op tablet en twee op mobiel de eerdere indeling. Per kaart een staande videopreview, daaronder links een oorspronkelijke productfoto en rechts een passend AI-voorbeeld, gevolgd door de modelnaam en Bekijk alle beelden.
- Geselecteerde kleding visueel gecontroleerd in de bestaande contact sheet: bruin herenjack (13-zdetail1), blauwe damesblouse (item4-front), groene jongenstrui (236022-01), paarse meisjessweater (91600458-front) en zwangerschapsjurk (b999063-050-1).
- Video's starten uitsluitend na klik binnen de kaart. Vooraf staat geen videobron in de DOM. Bestaande bestanden en previews blijven ongewijzigd.
- Foto's en Bekijk alle beelden openen alle productfoto's en AI-beelden van het model tegelijk in een scrollbaar raster. Individuele vergroting opent boven het raster; Escape keert terug. Donkere transparante dialogen, sluitknoppen en focusbegrenzing/-herstel blijven beschikbaar.
- Hero, AI/Photoshop-tekst, tarieven, werkwijze, routes, SEO en andere pagina's blijven behouden. Geen commit, push of deployment.
- 37 regressietests geslaagd. Browsercontrole en nieuwe screenshots: tests/check_ai_browser.py, docs/ai-compact-{1440,768,430,375,320}.png en docs/ai-raster-{1440,375}.png.
- Gewijzigd voor deze opdracht: templates/ai-modelfotografie.html, static/css/kledingfotografie/ai-modelfotografie.css, static/js/ai-modelfotografie.js, routes/ai_modellen.json, tests/check_ai_browser.py, docs/BESLUITEN.md en dit verslag; daarnaast de genoemde nieuwe screenshots.

Browsercontrole geslaagd op alle vijf breedtes (1440/768/430/375/320px), inclusief alle 46 foto's, beide thumbnailingangen, vijf expliciete videostarts, Escape, Tab/Shift+Tab en focusherstel; geen console-/HTTP-fouten of horizontale overflow. Screenshots visueel gecontroleerd. Tijdelijke testdependencies zijn opgeruimd; requirements en de bestaande .venv zijn niet gewijzigd.

## Uitlijning en media — 9 november 2026

- Expliciet opgedragen correctie: vaste videovlakken op 9:16 (de native verhouding van alle vijf video's), vaste fotovlakken op 2:3 in kaarten en galerij. Afmetingen worden door de vlakken bepaald in plaats van de intrinsieke afbeeldingsmaten. Daardoor blijven ook gemengde vierkante en staande foto's gelijk uitgelijnd. `contain` bewaart alle kledingdetails; geen stretching of extra uitsnede. Onderschriften staan apart onder de vaste galerijvlakken, met gelijke rastertussenruimtes.
- De gebruikte herenvideo is SHA-256-identiek aan `videos/herenmodel/ai-modelfotografie-herenmodel-modelvideo.mp4` in het huidige `wespi_ai_herenmodel.zip` (ZIP-datum 7 november 2026, 21:14:08; 9.632.110 bytes). Geen oudere videobronverwijzing aangetroffen in de actieve templates/scripts. De videostream is 1080 × 1920; FFmpeg cropdetect over de volledige tien seconden detecteert het volledige vlak (1080:1920:0:0). Een los frame is visueel gecontroleerd: geen ingebakken balken. Daarom geen video bijgesneden of opnieuw gecodeerd. Het juiste 9:16-vlak verwijdert de door de presentatie veroorzaakte balken. Nieuwe 9:16-poster uit de video op seconde 1, zonder uitsnede.
- Geen PNG-verwijzingen in de AI-pagina/modelgegevens. Wel vier transparante WebP-productfoto's: voor-/achterkant damesjeans 20267822 en meisjesjeans 92200500. Nieuwe `-wit.webp`-varianten met #FFFFFF en bijbehorende previews; originele bestandsnamen en inhoud blijven behouden. Alleen deze productverwijzingen zijn aangepast; model- en lifestylebeelden zijn onaangeroerd. Lossless WebP voorkomt extra kleur-/detailverlies; de kleinere bestaande previewmaat wordt behouden. Vergrotingen blijven volledig zichtbaar, proportioneel en zonder toegevoegd wit kader (de witte achtergrond binnen productfoto's is nu onderdeel van de foto).
- 38 regressietests geslaagd, inclusief kleur-/randpixelcontrole van witte varianten en byte-identiek behoud van alle ZIP-bronmedia. De nieuwe kleurtest gebruikt Pillow alleen voor verificatie; verwerking is uitgevoerd met ImageMagick, zonder generatieve aanpassing van kleding. De compositingbibliotheken verschillen maximaal één RGB-niveau op gedeeltelijk transparante randpixels.
- Wijzigingen: AI-template, AI-CSS, AI-JavaScript, routes/ai_modellen.json, beide AI-testbestanden, dit verslag en BESLUITEN.md. Nieuw: vier witte productvarianten plus vier previews, één herenvideoposter en docs/ai-heren-videocontrole.png. Bestaande ai-compact-/ai-raster-screenshots zijn vernieuwd.
- Teksten, tarieven, SEO, bronmedia, overige secties en andere pagina's blijven behouden. Geen commit, push of deployment.

Browsercontrole geslaagd op 1440/768/430/375/320px: gelijke videovlakken en fotoafmetingen (gemeten vóór en tijdens afspelen), uniforme galerijvlakken, alle 46 foto's en vijf video's, geen voorafgaande MP4-downloads, correcte focus/Escape en geen horizontale overflow, ontbrekende assets of consolefouten. Screenshots visueel beoordeeld, inclusief de nieuwe docs/ai-raster-witte-producten-375.png. Tijdelijke testdependencies na controle verwijderd.

## Gedeelde modelkaart met Grid — 9 november 2026

- Op expliciete vervolgopdracht krijgt iedere modelkaart exact vier directe kinderen: videovlak, fotopaar, titel en Bekijk alle beelden. CSS Grid met gedeelde subgrid-rijen lijnt ook de titels en links uit als een titel meerdere regels gebruikt. Eén gedeelde opmaak, geen regels per model. Vijf desktopkolommen, drie tabletkolommen en twee mobiele kolommen blijven behouden.
- De oude verspreide kaartregels zijn vervangen door één samenhangend CSS-blok. Vaste verhoudingen 9:16 en 2:3, 8px tussenruimte binnen kaarten, 5px afronding en witte voorbeeldvlakken. Beige/grijze opvulvlakken en randen zijn verwijderd. Product- en modelbeelden blijven volledig zichtbaar met contain.
- De video’s zelf zijn ongewijzigd. De vier resterende posters waren product/modelvoorbeelden met een afwijkende verhouding: contain veroorzaakte zichtbare opvulstroken binnen de 9:16-videovlakken. Nu gebruiken alle vijf modellen een 9:16-frame uit hun eigen video op seconde 1. Voor dames/jongens/meisjes/zwangerschap zijn nieuwe videoposters toegevoegd; alle eerdere media blijven behouden. Geen uitsnede of vervorming.
- De bestaande galerij houdt uniforme 2:3-miniatuurvlakken en volledige individuele vergrotingen. Teksten, tarieven, andere secties en andere pagina's blijven behouden.
- Aangepast: AI-template, AI-CSS, modelgegevens, browsercontrole en deze documentatie/BESLUITEN.md. Geen wijziging aan JavaScript, routes of oorspronkelijke media voor deze vervolgopdracht. Nieuwe posters staan uitsluitend in de vier bestaande previewmappen. Lokale controlescreenshots worden bijgewerkt. Geen commit, push of deployment.

Verificatie: 38 regressietests geslaagd. Playwright/Chrome op 1440/1024/768/430/375/320px geslaagd: bovenlijnen van video, fotopaar, titel en link per kaartrij gelijk (minder dan 1px afrondingsverschil); ook tijdens het afspelen. Alle posters exact 432 × 768, witte voorbeeldvlakken, volledige galerij/vergroting, Escape/Tab/focus, geen voorafgaande videodownloads, consolefouten, ontbrekende media of horizontale overflow. Desktop- en mobiele screenshots visueel gecontroleerd. Tijdelijke dependencies worden na afloop opgeruimd.

## Laatste visuele verbeteringen — 9 november 2026

- Op expliciet vervolgverzoek staat op mobiele breedtes tot en met 760px één modelkaart per rij, gecentreerd en maximaal 320px breed om onnodig hoge video's te voorkomen. Dit vervangt de eerdere keuze voor twee mobiele kolommen. Desktop behoudt vijf kolommen; tablet drie. Kaartvolgorde blijft video, twee foto's naast elkaar, naam, Bekijk alle beelden.
- Beide voorbeeldfoto's gebruiken dezelfde gedeelde 3:4-vlakken met expliciete breedte, nul minimummaat, witte achtergrond en gecentreerde contain-afbeeldingen. Dit maakt de fotoparen compacter dan de eerdere 2:3-vlakken zonder kleding af te snijden. Linker-/rechterrand sluiten aan op het videovlak.
- De volledige herenvideo is beoordeeld met een contact sheet van 20 frames over tien seconden (docs/ai-heren-beweging.jpg). Bij in-/uitlopen raken schoenen en lichaam de zijkanten; bij de camerazoom vullen jack en armen vrijwel de hele breedte. Daarom is een vaste extra uitsnede links/rechts niet veilig zonder verlies van relevante beeldinhoud. Video en poster blijven intact, niet uitgerekt. De 9:16-vlakken voegen geen boven-/onderbalken toe. Deze beperking is expliciet gemeld aan de eigenaar.
- Het bestaande AI/handwerk-blok heeft nu een egale achtergrond met var(--wespi-goud), zoals het volumeblok op Kledingfotografie. Tekst gebruikt var(--donkergrijs), kop de bestaande zwarte tekstkleur. De losse gouden zijlijn is verwijderd; tekstinhoud, bestaande container en sectie blijven behouden.
- Aangepast: AI-CSS, cacheversie in AI-template, tests/check_ai_browser.py, dit verslag en BESLUITEN.md. Bestaande overzicht-/galerijscreenshots bijgewerkt; accentblok-screenshots en de videobeweging-contactsheet toegevoegd. Geen mediabestanden gewijzigd of verwijderd; geen wijzigingen aan modelgegevens, JavaScript, routes of andere pagina's.
- 38 regressietests geslaagd. Geen commit, push of deployment.

Browsercontrole geslaagd op 1440/768/430/375px en aanvullend 320px. Op mobiel één kaart per rij; beide voorbeeldvlakken per kaart gelijk gemeten en uitgelijnd met de video. Alle 46 foto's en vijf video's beschikbaar, geen voorafgaande MP4-downloads, volledige vergrotingen, correcte Escape/Tab/focus en geen console-/HTTP-fouten of horizontale overflow. Nieuwe screenshots ai-modelkaart-{375,430}.png en ai-accent-{1440,768,430,375,320}.png. Mobiele kaart en geel blok visueel gecontroleerd. Tijdelijke testdependencies na verificatie verwijderd.

## Definitieve uniforme beeldpresentatie — 9 november 2026

- Op expliciete opdracht worden alle 46 foto's in het modellenoverzicht en de vijf galerijen nu daadwerkelijk als nieuwe 2:3-bestanden aangeleverd: 800 × 1200 pixels. De videoverhouding blijft 9:16, video- en posterbestanden en afspeelcode zijn ongemoeid gelaten.
- Nieuwe bestanden: static/images/{herenmodel,damesmodel,jongensmodel,meisjesmodel,zwangerschapsmodel}/presentatie/*-2x3.webp. Aantallen per map: 6, 11, 10, 10 en 9. Alle bestaande bronnen, eerdere witte varianten en previews blijven byte-identiek behouden.
- 28 modelbeelden: volledige bronhoogte behouden; uitsluitend laterale achtergrond verwijderd waar nodig, voornamelijk bij de vier bredere herenbeelden. Verkleining gebeurt proportioneel; maximaal één pixel afronding wordt weggewerkt op het uiteindelijke vlak, zonder stretching. Geen toegevoegd wit of transparant kader. Alle 28 uitsneden visueel beoordeeld op de contact sheet.
- 18 productbeelden: bestaande blanco/transparante rand gemeten tegen wit, met 20 bronpixels veiligheidsruimte rond het product; vervolgens proportioneel binnen 720 × 1080 geplaatst, gecentreerd op een witte 800 × 1200-achtergrond. Geen kleding afgesneden. De detailfoto blijft een detailfoto. Lossless WebP voor productvarianten en kwaliteit 92 voor modelvarianten. Totaal circa 12 MB voor alle 46 afgeleide bestanden samen.
- Overzicht en galerij gebruiken exact dezelfde nieuwe presentatiebestanden en dezelfde CSS-verhouding (--ai-foto-verhouding). Bij individuele vergroting opent nog altijd het bestaande volledige bronbeeld met zijn oorspronkelijke verhouding. De tarievenafbeelding en hero blijven de bestaande bronnen gebruiken.
- De achtergrond van AI/handwerk is exact #faf3d9, rechtstreeks overgenomen uit .kleding-ai-promotie in static/css/kledingfotografie/ai-promotie.css. De andere pagina is niet gewijzigd. Dit vervangt de eerdere felle goudkleur.
- De bestaande losse dubbele lightboxregels zijn samengevoegd; ongebruikte oude bladergalerijregels verwijderd. Geen CSS per model. Alle foto's staan direct in het raster; mobiele bediening, Escape en focusbeheer blijven behouden.
- Reproduceerbare verwerking: scripts/generate_ai_presentation.py. Volledig bestandsoverzicht met bron/output, bronafmetingen, uitsnede en SHA-256: docs/ai-presentatie-media.json. Visuele inspectie: docs/ai-uniform-contactsheet.jpg en galerijscreenshots ai-uniform-{model}-{1440,375}.png.
- Gewijzigd: AI-template, AI-CSS, AI-JavaScript (uitsluitend fotobron/-afmetingen), routes/ai_modellen.json (uitsluitend presentatievelden), beide AI-tests en dit verslag/BESLUITEN.md. Nieuw: generatiescript, mediainventaris, 46 presentatiebeelden en controlescreenshots. Teksten, tarieven, SEO, video's, hero en andere pagina's blijven behouden. Geen commit, push of deployment.
- 39 regressietests geslaagd, inclusief bronhashes, uniforme pixelmaten, oorspronkelijke ZIP-media en ongewijzigde video-inventaris.

Browsercontrole geslaagd op 1440/768/430/375/320px: identieke 800 × 1200-bronnen in alle galerijen en fotoparen, gelijke rastervlakken en kaartrijen, juiste achtergrond #faf3d9, alle foto's en video's, Escape/Tab/focus en volledige individuele vergroting. Geen console-/HTTP-fouten, voorafgaande MP4-downloads of horizontale overflow. Alle afgeleide beelden visueel gecontroleerd via contact sheet; galerijen en volledige pagina visueel beoordeeld op desktop/mobiel (ai-pagina-definitief-{1440,375}.png). Bronbestanden en ZIP-media zijn door de tests op behoud gecontroleerd. Tijdelijke testdependencies na controle opgeruimd.
