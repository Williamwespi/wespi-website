# Projectkompas Wespi

**Actuele aanvulling 11 november 2026 ? Productbeeldbewerking:** goedgekeurd sfeerbeeld toegevoegd als brede compositie met uitsluitend een fade naar links en drie WebP-formaten. Horloge zonder houdergerichte tekst compact naast de introductie; retouche zonder binnenkaart, gebogen goudaccent bij kleur en grotere detailcompositie. Hero, tas, vergelijkingen, tarief, SEO, navigatie en gedeelde footer behouden. Deze opdracht actualiseert de eerdere opbouw hieronder. Zie [PRODUCTBEELDBEWERKING_UITVOERING.md](./PRODUCTBEELDBEWERKING_UITVOERING.md). Uitsluitend lokaal.

**Actuele aanvulling 9 november 2026 — visuele kwaliteit Productbeeldbewerking:** de eigen pagina gebruikt nu grotere horlogevergelijkingen, asymmetrische retouchecases, een kleurslider die buiten een zacht goudvlak steekt, een staand/breed detailduo en een witte tariefkaart. Sandaal uitsluitend naar links en tas uitsluitend naar rechts gefade; alle verticale verlooplagen verwijderd. Nieuwe tasuitsnede houdt ruimte rond het hengsel. Echte bronparen, € 2,49 exclusief btw, bestaande teksten, SEO, navigatie en de gedeelde footer blijven behouden. Alleen de eigen pagina/CSS, twee nieuwe tas-WebP's, generator/manifest, gerichte tests en documentatie gewijzigd. Visueel beoordeeld op 375/430/768/1440 px en technisch getest op zes breedtes. Deze aanvulling actualiseert de eerdere visuele opbouw verderop. Zie [PRODUCTBEELDBEWERKING_UITVOERING.md](./PRODUCTBEELDBEWERKING_UITVOERING.md).

**Statusaanvulling fase 4, 5 november 2026:** de lokale SEO- en technische eindcontrole is afgerond met sitemap/robots, Open Graph, veilige foutafhandeling, responseheaders/cache/compressie en gerichte toegankelijkheidsverbeteringen. 34 regressietests slagen; de browsercontrole omvat 1440/768/430/375px. Geen deployment of echte mail. Productiebesluiten en voorwaarden staan in [LIVEGANG_FASE_4.md](./LIVEGANG_FASE_4.md), met afzonderlijke [migratie](./LIVEGANG_MIGRATIE.md) en [deployment-/rollbackchecklist](./LIVEGANG_DEPLOYMENT.md). Eerdere faseverslagen zijn historische momentopnamen; hun volgende-fase-wachtstatus is door de latere expliciete opdracht opgevolgd.

**Statusaanvulling fase 3, 5 november 2026:** beeldbestanden zijn geoptimaliseerd met behoud van bronbestanden en detailvergrotingen. Tekstcontrast, gerichte mobiele compactheid, dubbele contactuitnodigingen en bevestigde btw-vermeldingen zijn verbeterd. Fase 1 en 2 zijn behouden en regressietests slagen. Zie [LIVEGANG_FASE_3.md](./LIVEGANG_FASE_3.md) voor bestanden, metingen en productieaandachtspunten. Fase 4 wacht op akkoord.

**Statusaanvulling fase 2, 5 november 2026:** het Beeld-menu heeft een links uitgelijnde dropdown met consistente muis-/toetsenbordbediening en een zelfstandige AI-modelfotografielink. De mobiele beeld-tekstvolgorde uit audit B1 is gecorrigeerd op de bestaande omslagpunten; desktopindelingen en hero's zijn behouden. Zie [LIVEGANG_FASE_2.md](./LIVEGANG_FASE_2.md) voor uitvoering en verificatie. Fase 3 wacht op akkoord.

**Statusaanvulling 5 november 2026:** de oorspronkelijke broninventarisatie hieronder beschrijft een eerdere situatie. Offerte en Contact gebruiken inmiddels server-side SMTP-verwerking; de bevestigde oude automotive- en juridische routes hebben 301-redirects. Footer- en fragmentlinks zijn gericht hersteld en er zijn gesimuleerde regressietests toegevoegd. Zie [LIVEGANG_FASE_1.md](./LIVEGANG_FASE_1.md) voor de actuele uitvoering, testresultaten, SMTP-instellingen en nog te beoordelen oude URL's. Echte e-mailaflevering en productiehosting zijn nog niet geverifieerd; fase 2 vereist akkoord.

## Identiteit en positionering

Wespi richt zich primair op retail en e-commerce en presenteert zich als specialist met drie actieve hoofddiensten:

- **Beeld** — professionele productfotografie en beeldbewerking.
- **Data** — productinformatie verwerken, structureren en verrijken als dienst.
- **Slimmer werken** — terugkerende werkprocessen vereenvoudigen met praktische automatisering en digitale toepassingen, zodat klanten zelf efficiënter kunnen werken.

Data gaat over het verwerken van gegevens als dienst; Slimmer werken gaat over oplossingen waarmee klanten hun eigen werkprocessen efficiënter uitvoeren. Houd dit onderscheid in communicatie en productkeuzes duidelijk.

Wespi wil herkenbaar zijn als specialist en positioneert zich niet als algemeen softwarebedrijf. De nadruk ligt op praktische oplossingen die kwaliteit, eenvoud en efficiëntie opleveren. Bestaande werkende functionaliteit moet behouden blijven; wijzigingen aan bestaande onderdelen gebeuren alleen binnen een expliciete opdracht.

De dienst Web is voorlopig geparkeerd en wordt niet verder ontwikkeld of actief aangeboden. Dit is geen definitieve afwijzing. Zie [BESLUITEN.md](./BESLUITEN.md) en [IDEEEN.md](./IDEEEN.md).

## Aangetroffen projectstructuur

- `app.py` maakt de FastAPI-app, serveert de map `static/` onder `/static` en registreert de paginarouter.
- `routes/paginas.py` bevat de routes voor de pagina's en rendert Jinja2-templates uit `templates/`.
- `templates/` bevat 9 pagina-templates en de gedeelde layout `base.html`. `templates/onderdelen/` bevat gedeelde header- en footeronderdelen en kleinere secties die pagina's opbouwen.
- `static/css/` bevat 56 stylesheets, verdeeld over algemene stijlen en pagina- of sectiespecifieke mappen.
- `static/js/` bevat 2 JavaScript-bestanden voor de algemene navigatie-interacties en de kledingfotografie-lightbox.
- `static/images/` bevat 85 afbeeldingen: 62 PNG's, 22 JPG's en 1 SVG, geordend naar onderwerp zoals beeld, kledingfotografie, packshotfotografie, productdata en Slimmer werken.
- `requirements.txt` noemt FastAPI, Uvicorn en Jinja2.

In de repository zijn daarnaast 1.682 bestanden uit `.venv/` aangetroffen, evenals Python-cachebestanden. Deze zijn geen applicatiebroncode, maar maken wel deel uit van de aangetroffen projectbestanden.

## Bestaande pagina's en navigatie

De paginarouter definieert deze routes:

| Route | Pagina |
|---|---|
| `/` | Home |
| `/beeld` | Beeld |
| `/productfotografie/kledingfotografie` | Kledingfotografie |
| `/productfotografie/packshotfotografie` | Packshotfotografie |
| `/beeldbewerking` | Beeldbewerking |
| `/data/productdata` | Productdata |
| `/slimmer-werken` | Slimmer werken |
| `/slimmer-werken-v2` | Slimmer werken V2 (lokale testpagina, niet opgenomen in navigatie) |
| `/offerte` | Offerte aanvragen |
| `/over-wespi` | Over Wespi |

De header groepeert Beeld, Data en Slimmer werken onder **Diensten**. Daarnaast linkt de header naar de praktijksectie op de homepage, Over Wespi, Contact en Offerte aanvragen. De footer herhaalt dienstlinks en contactgegevens. Web wordt niet meer als actieve dienst getoond of als dienst aangeboden in de offertekeuze; het blijft wel als toekomstig idee vastgelegd.

De homepagina is opgebouwd uit hero-, diensten-, voordelen- en projectenonderdelen. Detailpagina's gebruiken afzonderlijke secties. De templates bevatten paginatitels, meta descriptions en op meerdere pagina's een eigen canonical-URL.

## Huidige pagina Slimmer werken

De route `/slimmer-werken` rendert `templates/slimmer-werken.html`. Deze bestaande pagina blijft behouden en bevat:

1. Een hero met de belofte “Minder handwerk. Slimmer geregeld.”, een link naar de mogelijkheden en een link naar de offertepagina.
2. Een overzicht met vijf voorbeelden: teksten maken, Excel/CSV verwerken, bestanden verwerken, gegevens controleren en beelden automatisch verwerken.
3. Een prijssectie met twee kaarten: “Kleine oplossing” vanaf € 249 en “Slimme tool” vanaf € 499.
4. Een afsluitend tussenblok dat bezoekers uitnodigt hun terugkerende handeling voor te leggen.

De pagina gebruikt afzonderlijke CSS-bestanden en twee afbeeldingen uit `static/images/slimmer-werken/`. De bestaande prijzen van € 249 en € 499 blijven ongewijzigd.

De afzonderlijke testpagina `/slimmer-werken-v2` staat in `templates/slimmer-werken-v2.html` met eigen styling in `static/css/slimmer-werken/v2.css`. Deze testpagina is niet aan de navigatie toegevoegd en krijgt `noindex, nofollow`. De inhoud legt de nadruk op vijf toepassingen van praktische procesverbetering: geautomatiseerde gegevensverwerking, controle en kwaliteitsbewaking, beeld- en bestandsworkflows, informatie-uitwisseling tussen bestaande systemen en terugkerend werk automatiseren. Een modulair onderdeel voor eigen, herbruikbare applicaties staat in `templates/onderdelen/slimmer-werken-v2/applicaties.html`. Het bevat productkaarten met naam, omschrijving, afbeelding, optionele abonnementsprijs en informatielink. Zolang er geen applicaties beschikbaar zijn, is de sectie verborgen. De V2 bevat geen vaste prijzen.

## Functionaliteit en technische aandachtspunten

**Aangetroffen in de broncode:** FastAPI-routes voor de genoemde pagina's, Jinja2-opbouw van pagina's, statische assets, mobiele navigatie-interacties, een dienst-dropdown, een lichtbox voor kledingfotografie en een offerteformulier-template. De formuliermarkup gebruikt `mailto:info@wespi.nl`; in de route is alleen een GET-handler aangetroffen.

**Niet getest:** Het starten van de applicatie, HTTP-responses van routes, het laden van pagina's en assets in een browser, het gedrag van menu en lichtbox, het versturen van het offerteformulier en mobiele weergave. De aanwezigheid van code is geen verificatie dat deze onderdelen in de huidige omgeving werken.

**Aandachtspunten en verschillen tussen afspraken en code:**

- Op 26 oktober 2026 is bevestigd dat de prijsstructuur voor Slimmer werken V2 nog niet definitief is. De bestaande bedragen van € 249 en € 499 blijven voorlopig ongewijzigd. Een eerdere bespreking van € 495 stelde geen prijs vast; zie [BESLUITEN.md](./BESLUITEN.md).
- De bestaande Slimmer werken-pagina blijft behouden. De afzonderlijke V2-testpagina staat op `/slimmer-werken-v2`; zie hierboven.
- Web is op 26 oktober 2026 uit de actieve dienstpresentatie op de homepage en footer en uit de offertekeuze verwijderd. Er is geen afzonderlijke Web-paginaroute aangetroffen; Web blijft als mogelijk toekomstig idee behouden.
- De footer bevat daarnaast diverse `#`-placeholders. Sommige fragmentlinks kunnen afhankelijk van de pagina context missen.
- Bepaalde bestaande teksten tonen mogelijke oplossingen of tools. Deze broninventarisatie heeft niet inhoudelijk geverifieerd of zulke producten beschikbaar zijn; presenteer toekomstige producten pas actief wanneer ze beschikbaar zijn.
- Het offerteformulier post niet naar een aangetroffen backendroute maar gebruikt `mailto:`. De werking daarvan is niet getest.
- `.venv/` is omvangrijk en is opgenomen in de getrackte repositorybestanden. Dit is een aandachtspunt voor repositorybeheer; hier is niets aan gewijzigd.
- Er zijn geen projecttestbestanden of testconfiguratie aangetroffen. `requirements.txt` bevat geen vastgepinde versies. Een build of test is voor deze documentatieopdracht niet uitgevoerd.

**Statusaanvulling 7 november 2026:** AI-modelfotografie is lokaal uitgebreid met vijf modellen, 28 modelbeelden, vijf video's, 18 oorspronkelijke productfoto's en een toegankelijke donkere mediagalerij. Bestaande tarieven, hero, SEO en overige pagina's blijven behouden. Zie [AI_MODELLEN_UITBREIDING.md](./AI_MODELLEN_UITBREIDING.md). Geen commit, push of deployment; wacht op beoordeling.

**Statusaanvulling 9 november 2026 — Productbeeldbewerking, na visuele herziening:** zelfstandige pagina op `/beeldbewerking/product`, met actieve link binnen Beeldbewerking. Sandaal met natuurlijke schaduw in de hero, grotere vaste vergelijkingen voor horloge/bord/pet, één kleurslider, detailbeelden, het bevestigde tarief **€ 2,49 per foto exclusief btw** en een compacte werkwijze. Acht bronaanzichten, twaalf zichtbare afbeeldingen. ‘Consistente productseries’, ‘Praktisch’ en de eigen afsluitende CTA zijn verwijderd. Twee nieuwe hero-WebP's; alle oorspronkelijke en eerdere afgeleide media behouden. Alle 212 bronbestanden blijven intact en buiten Git/publieke bestanden. De gedeelde ‘Samen aan de slag’-sectie is hersteld op dienstenpagina's; alleen Contact/Offerte behouden hun formulier als afsluiting. 42 regressietests, zes productpagina-breedtes en websitebrede footercontrole op drie breedtes geslaagd. Zie [PRODUCTBEELDBEWERKING_UITVOERING.md](./PRODUCTBEELDBEWERKING_UITVOERING.md). Geen commit, push of deployment.
