# Projectkompas Wespi

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
