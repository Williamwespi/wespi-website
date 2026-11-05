# Wespi — website-audit vóór livegang

Datum: 5 november 2026. Status: **audit en voorstel; geen goedgekeurde wijzigingsopdracht**.

## Reikwijdte, methode en oordeel

De website heeft een herkenbare basis: Arial, krachtige zwarte koppen, gouden accenten, lichte achtergronden en grote productbeelden. De homepage verbindt Beeld, Data en Slimmer werken duidelijk. De meeste dienstenpagina's leggen aanbod en doelgroep begrijpelijk uit. Een volledige herbouw is niet nodig. **Advies: nog geen definitief livegangakkoord**, vooral vanwege offerteafhandeling, zware media en het ontbreken van een gecontroleerde URL-migratie.

Onderzocht: `AGENTS.md`, de vier projectdocumenten, alle 16 GET-paginaroutes in `routes/paginas.py`, de POST-contactroute, gedeelde templates, de gerenderde pagina's en relevante CSS/JavaScript. Beeldbewerking (`/beeldbewerking`) is uitsluitend technisch gecontroleerd; inhoudelijke en visuele bevindingen daarover zijn bewust uitgesloten. Productbeeldbewerking heeft geen zelfstandige aangetroffen route en staat in het menu als inactieve tekst. Er is geen inhoudelijk oordeel over deze onafgeronde pagina's gegeven.

Uitgevoerd in lokaal Chromium tegen de bestaande FastAPI-app op `http://127.0.0.1:8765`:

- **61 pagina-/viewportcontroles:** 15 pagina's op 1440, 768, 375 en 430 pixels breed, plus één technische controle van Beeldbewerking. Viewporthoogte 1000 pixels. Screenshots van de complete pagina's; hoofd- en dienstenpagina's visueel bekeken op desktop en mobiel. Juridische pagina's op rendering, leesbaarheid en aanwezige gegevens beoordeeld, niet juridisch gevalideerd.
- **151 unieke lokale HTTP-controles** op gerenderde assets, links, systeemroutes en aanvullende URL's. Eén time-out van de Productdata-hero is afzonderlijk herhaald: HTTP 200, dus geen ontbrekende afbeelding.
- CSS-verwijzingen gecontroleerd: 24 lokale `url(...)`-verwijzingen, geen ontbrekende bestanden. Dynamisch samengestelde Jinja-afbeeldingspaden via de gerenderde pagina's gecontroleerd; losse padfragmenten zijn niet als ontbrekende bestanden aangemerkt.
- Menu, dropdown, lightboxes, AI-video en sliders interactief getest. Contactvalidatie met negen geïsoleerde ASGI-testgevallen, waarbij alle e-mailverzending was vervangen door testfuncties. **Geen echte e-mail verstuurd.**
- Bestandsgroottes, headers, metadata, mobiele volgorde en tekstcontrast onderzocht. Geen nieuwe dependencies geïnstalleerd.

Beperkingen: geen echte SMTP-aflevering, mailclient-offerteverzending, productiehosting, DNS/TLS, Search Console, echte Core Web Vitals, Safari/iOS/Firefox of volledige screenreadertest. De lokale app bewijst niet dat reverse-proxyconfiguratie of serverinstellingen in productie goed staan. Dit is geen volledige WCAG- of juridische conformiteitsverklaring.

Voor de visuele controle zijn lazy afbeeldingen tijdelijk in de browser geladen. Hieronder genoemde totale mediavolumes zijn daarom **geen gemeten eerste-paginalading of Lighthouse-score**. Losse bestandsgroottes zijn wel daadwerkelijk gemeten.

Prioriteiten: **P1** vóór livegang oplossen of expliciet aanvaarden; **P2** belangrijke verbetering; **P3** kan na livegang. Risico betekent risico op onbedoelde wijzigingen bij uitvoering van het voorstel.

## A. Kritieke punten vóór livegang

### A1 — Offerteaanvragen hebben nog geen betrouwbare webafhandeling

- **Huidig:** `/offerte` rendert `templates/oferte.html`. Het formulier gebruikt `action="mailto:info@wespi.nl"`, `method="post"` en `enctype="text/plain"`. Er is geen POST-offerteroute. De header en veel dienstknoppen sturen bezoekers hierheen.
- **Probleem:** de primaire conversie hangt af van een werkende lokale mailclient. De website kan verzending, ontvangst en foutafhandeling niet bevestigen. De afzonderlijke Contact-pagina heeft wel servervalidatie en SMTP-code, maar echte aflevering is niet getest.
- **Voorstel:** offerteaanvragen via een bestaande, expliciet gekozen serverflow verwerken, met behoud van geselecteerde dienst en offertevelden; bijvoorbeeld de contactafhandeling uitbreiden of een aparte offertehandler maken. Daarna echte aflevering en antwoordadres op staging controleren met toestemming voor een testbericht. SMTP-configuratie en afleverbaarheid zijn een open livegangvoorwaarde, geen bewezen storing.
- **Prioriteit / risico:** P1 / middel. Bestanden: `templates/oferte.html`, `templates/contact.html`, `routes/paginas.py`; eventueel tests buiten de productiecode. Niet alleen het formulier naar `/contact` laten posten zonder veldmapping.
- **Bewijs:** formuliermarkup, route-inventaris en HTTP 200 op de offertepagina. Contactvalidatie en gesimuleerde SMTP-fouten werken; dat bewijst geen externe aflevering.

### A2 — Afbeeldingen zijn veel te zwaar voor regulier webgebruik

- **Huidig:** `static/images/beeld/kleding-bodyform-jurk.png` en `static/images/packshotfotografie/accessoirefotografie-blauwe-tas-wespi.png` zijn elk **23.048.704 bytes, circa 23 MB**. Meerdere kledingbeelden zijn 8–9 MB. Home- en Slimmer werken-hero's zijn circa 2,4–2,5 MB. De AI-video is circa 9,6 MB voor 10 seconden.
- **Probleem:** hoge download- en decodeerkosten, vooral op mobiel. Met alle afbeeldingen geladen bedroegen de gemeten resourcevolumes ongeveer 46 MB op Beeld, 46 MB op Packshot en 42 MB op Kledingfotografie. Dit zijn volledige inspectieladingen, geen eerste schermmeting.
- **Voorstel:** passende webafmetingen en geoptimaliseerde formaten aanbieden, waar nodig met transparantie; responsive `srcset`/`sizes`; echte grote originelen uitsluitend op aanvraag in de lightbox. Hero's gericht optimaliseren. Videoposter en `preload="none"` behouden en video afzonderlijk optimaliseren. Na omzetting juist de kledingdetails en uitsneden visueel vergelijken.
- **Prioriteit / risico:** P1 / middel. Bestanden: genoemde assets, hun paginaonderdelen, `templates/beeld.html` en dienstonderdelen, `templates/ai-modelfotografie.html`. Geen beeldselectie of functionaliteit vervangen om alleen bytes te winnen.
- **Bewijs:** HTTP-bestandsgroottes en daadwerkelijke browserdownloads; alle gebruikte beelden konden uiteindelijk worden geladen.

### A3 — Migratie van bestaande publieke URL's is nog niet geregeld

- **Huidig:** lokaal geven `/beeldbewerking/auto`, `/terms` en `/privacystatement` HTTP 404. De vernieuwde bestemmingen zijn respectievelijk `/beeldbewerking/automotive`, `/algemene-voorwaarden` en `/privacyverklaring`. Deze oude URL's komen uit de eerder gebruikte online website/bronteksten.
- **Probleem:** bij vervanging van de live website kunnen bestaande verwijzingen en zoekresultaten op een 404 uitkomen. Geen lokale redirect bewijst nog niet dat de productieproxy dit niet regelt, maar er is geen gecontroleerd migratieplan aangetroffen.
- **Voorstel:** bestaande live URL's volledig inventariseren, per oude URL één relevante nieuwe bestemming vastleggen en permanente redirects testen. De nieuwe lokale routes behouden; geen extra URL-hernoeming voorstellen. Controleer redirectketens, canonicals en nieuwe sitemap samen.
- **Prioriteit / risico:** P1 / middel. Onderdelen: `routes/paginas.py` of productieproxyconfiguratie; apart migratieoverzicht. Voor onbevestigde oude URL's niet gokken.
- **Bewijs:** genoemde lokale 404-responses; huidige nieuwe routes geven HTTP 200.

### A4 — Enkele links en contactgegevens zijn aantoonbaar onbetrouwbaar

- **Huidig:** de footer heeft `href="#"` bij Werkwijze, Over Wespi, Kennis en Mijn Wespi. `href="#praktijk"` werkt op Home maar verwijst op andere pagina's naar een niet-bestaand fragment. De hero-CTA van Kledingfotografie wijst naar `#bodyform`, maar die ID ontbreekt. In de privacyverklaring staan `https://info@wespi.nl` en `https://william@wespi.nl` als e-maillinks. De privacyverklaring noemt postcode **7122 LX**, terwijl Contact en Algemene voorwaarden **7122 LC** noemen.
- **Probleem:** knoppen lijken functioneel maar bereiken de beloofde bestemming niet; privacycontactlinks zijn geen e-mailacties. De postcode-inconsistentie tast betrouwbaarheid aan.
- **Voorstel:** bestaande bestemmingen koppelen (`/over-wespi`, `/#praktijk`), ongebruikte diensten/portalen niet als actieve links presenteren, het bestaande bodyformonderdeel een passend doel geven en mailcontact technisch corrigeren naar `mailto:`. Juiste postcode door eigenaar laten bevestigen; geen bedrijfsgegevens verzinnen.
- **Prioriteit / risico:** P1 / laag voor links, middel voor feitelijke/juridische tekst. Bestanden: `templates/onderdelen/footer.html`, `templates/onderdelen/kledingfotografie/hero.html`, `templates/onderdelen/kledingfotografie/bodyform.html`, `templates/privacyverklaring.html`; eventueel Contact/voorwaarden na feitencontrole.
- **Bewijs:** fragmentcontrole in de browser en broncontrole. De externe verkeerde mail-URL's zijn niet bezocht en er is geen bericht verzonden.

### A5 — Gouden tekst op lichte achtergronden heeft onvoldoende contrast

- **Huidig:** `--wespi-goud: #dfb91a` wordt als tekstkleur gebruikt, onder andere in hero's en prijzen. Op wit is het berekende contrast **1,89:1**; op `#f3f4f5` circa **1,72:1**. Ook `#bd9410` op wit is met **2,84:1** onvoldoende voor gewone tekst en net onder 3:1 voor grote tekst.
- **Probleem:** belangrijke titelwoorden en bedragen zijn voor een deel van de bezoekers moeilijk leesbaar. Dit is geen oordeel dat geel als merkkleur moet verdwijnen.
- **Voorstel:** geel behouden voor vlakken, lijnen en decoratie; voor informatieve tekst een voldoende donkere variant of zwart kiezen. Eerst een klein, goedgekeurd tekstkleurpalet bepalen en alleen de betrokken selectors aanpassen. Niet blind de globale merkvariabele donkerder maken: die stuurt ook knoppen en achtergronden.
- **Prioriteit / risico:** P1 / middel tot hoog wegens gedeelde styling. Bestanden: relevante hero- en prijsstylesheets, `static/css/juridisch.css` en waar nodig een afzonderlijke tekstkleurvariabele in `basis.css` na goedkeuring. Juridische goudkleurige links eveneens meten.
- **Bewijs:** berekening op aanwezige CSS-kleuren. [W3C, contrastminimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) noemt 4,5:1 voor gewone tekst en 3:1 voor grote tekst. Foto-overlays zijn hiermee niet volledig doorgemeten. De eerder beschermde automotive-hero alleen aanpassen na expliciete afstemming over deze botsing met behoud van het ontwerp.

## B. Belangrijke verbeteringen

| ID | Huidige situatie en probleem | Voorgestelde oplossing en bestanden | Prioriteit; risico |
|---|---|---|---|
| B1 | Mobiele beeld-tekstsecties beginnen regelmatig met de afbeelding in plaats van de titel. Dat wijkt af van de nu opgegeven regel. | Paginaspecifiek volgorde titel → beeld → rest regelen; desktopindeling behouden. Zie onderstaande concrete lijst. | P2; middel: DOM/CSS-volgorde en interacties kunnen veranderen. |
| B2 | Desktopdropdown is 420px breed en gecentreerd onder het korte Beeld-label. Productfotografie begint circa 180px links van het midden van de trigger. Er is momenteel één paneel met twee groepen, geen echt derde hoverniveau. | Paneel links uitlijnen op de trigger of de navigatiekolom; groepen compact houden en een aaneengesloten hovergebied behouden. `static/css/header.css`, `templates/onderdelen/header.html`. | P2; middel: desktop- en mobiele regels samen regressietesten. |
| B3 | Hover opent het dropdownpaneel terwijl `aria-expanded` op `false` blijft. Escape sluit de JS-status, maar het paneel blijft zichtbaar zolang de muis op het hovergebied staat. | Pointer-, toetsenbord- en klikstatus consequent laten samenwerken. Escape moet echt sluiten; focus logisch teruggeven. `static/js/main.js`, `static/css/header.css`. | P2; middel. Enter en Tab werken bij de definitieve toetsenbordcontrole wel. |
| B4 | AI-modelfotografie ontbreekt in hoofdmenu en footer; bereikbaarheid hangt af van links op Kledingfotografie/Kledingbeeldbewerking. | Aanvullend menu-item binnen de groep Productfotografie, direct bij/onder Kledingfotografie. Hoofdpagina kleding blijft klikbaar; geen extra hoverlaag nodig. Beeldbewerking is een minder passende primaire plaats omdat de dienst volgens projectbesluit kledingfotografie aanvult. `header.html`, eventueel `footer.html`. | P2; laag tot middel. Dit is een voorstel, geen navigatiebesluit. |
| B5 | Packshotlightbox wordt geopend via niet-focusbare `img`-elementen. Na openen blijft de focus achter de overlay. Bij kledingfotografie verlaat Tab de geopende lightbox; dialogsemantiek/focusbegrenzing ontbreken. | Triggerbuttons en een toegankelijke dialoog met focusbeheer gebruiken, liefst volgens het aanwezige native dialogpatroon van AI. Openen, Escape, sluiten en focusherstel behouden. `main.js`, `kledingfotografie-lightbox.js`, betrokken templates/CSS. | P2; middel: toetsenbord en muis testen; geen galerijherbouw. |
| B6 | `robots.txt` en `sitemap.xml` geven lokaal 404. Publieke pagina's zijn daarmee niet automatisch geblokkeerd, maar ontdekbaarheid en releasebeleid zijn niet expliciet ingericht. | Sitemap voor definitieve publieke routes; uitsluiten V2 en onafgeronde routes. Robotsbeleid voor productie en staging afzonderlijk vastleggen. `app.py`/`routes/paginas.py`, eventueel nieuwe statische bestanden. Voor onafgeronde pagina's alleen technische indexeerbaarheid afstemmen, geen inhoud wijzigen. | P2; laag tot middel. Robots is geen toegangsbeveiliging. |
| B7 | Hero's en paginalengtes verschillen sterk; veel dienstpagina's hebben op mobiel een hero boven 1000px. Packshot toont een grote buitenkaart met extra beeldkaarten; Slimmer werken heeft zeer hoge voorbeeldkaarten. | Compactere inhoudsverdeling bij de grootste uitschieters, geen algemene margeverkleining. Hero-pluspunten/knoppen en kaartinterne witruimte gericht beoordelen; automotive-hero expliciet behouden. Zie metingen hieronder. | P2; middel: huisstijl en leesbaarheid bewaken. |
| B8 | De algemene contact-CTA wordt overal herhaald, ook vlak onder het contactformulier en na aparte contactblokken op Packshot en Kledingbeeldbewerking. | Per paginatype één logische afsluiting kiezen. De eigenlijke footer behouden. Voorwaardelijke weergave van de algemene CTA pas na goedgekeurde opdracht. `base.html`, `onderdelen/footer.html`, pagina-afsluitingen. | P2; middel: gedeeld onderdeel raakt alle pagina's. |
| B9 | Btw-vermelding staat duidelijk bij AI, kledingbeeldbewerking en automotive, maar niet direct bij diverse kleding-, packshot-, Slimmer werken- en losse Productdata-prijzen. | Btw-basis en tariefeenheid consequent vlak bij bedragen vermelden nadat eigenaar ze heeft bevestigd. Bestaande bedragen niet aanpassen. Productdata-abonnementen bestaan al en vallen niet onder het verbod op automotive-Premium. | P2; laag na feitenbevestiging; middel zonder bevestiging. Prijs-templates per dienst. |
| B10 | Dezelfde grote bundel paginastijlen wordt via `base.html` op alle pagina's geladen; CSS-imports voegen extra verzoeken toe. Zelfs juridische pagina's laden tientallen resources. | In kleine stappen stijlen per pagina laden via `extra_head`, met screenshots en interactietests. Gedeelde `.knop` en `.hero` eerst inventariseren zodat zij niet per ongeluk verdwijnen. | P2; hoog: bestaande pagina's hebben impliciete afhankelijkheden van deze bundel. |
| B11 | Privacytekst noemt zowel uitsluitend technische als analytische/trackingcookies en verwijst naar accountinstellingen, terwijl in de bekeken site geen accountflow of trackers zijn aangetroffen. | Eigenaar laten vaststellen welke verwerking/technieken daadwerkelijk gelden en tekst laten controleren. De audit bevestigt geen juridische juistheid en doet geen wettelijke uitspraak over toestemmingsplicht. `privacyverklaring.html`. | P2; middel: feitelijke en juridische controle nodig. |

### B1 — Concreet te herstellen mobiele volgorde

Waargenomen op 375px en herhaald bekeken op 430px. Deze lijst is een **voorstel** en gaat niet automatisch boven eerdere goedgekeurde beeldplaatsingen.

| Pagina | Onderdeel | Huidige volgorde / aanpak |
|---|---|---|
| Home | Waarom Wespi (`.voordelen`) | Grote barcodeafbeelding vóór de titel. Titel boven beeld plaatsen; voordelen erna. |
| Kledingfotografie | AI-promotie; Werkwijze | Beide beginnen met het beeld. Titel eerst, bestaande foto daarna. Bodyform en platte fotografie tonen al titel vóór productbeelden. |
| Packshotfotografie | Schoenen, accessoires, overige producten | De volledige fotogalerij staat vóór de titel. Titel boven galerij, beschrijving en prijs erna. |
| AI-modelfotografie | Tarieven | Sfeerbeeld vóór de tarieftitel. Titel boven het bestaande beeld; prijzen en foto inhoudelijk/desktop op hun afgesproken plek houden. |
| Kledingbeeldbewerking | Volume en werkwijze | Trui vóór de titel. Titel, foto, stappen. Interactieve vergelijking zelf behouden. |
| Autobeeldbewerking | Grote volumes | Bestelbus vóór de titel. De laatste desktopuitwerking behouden; alleen mobiele titelvolgorde ter goedkeuring voorleggen. Mogelijkheden heeft de titel wel vóór de SUV. |
| Productdata | Werkwijze; vaste tarieven | Beide beginnen met een groot sfeerbeeld. Titel eerst, daarna beeld en inhoud. |
| Slimmer werken | Prijssectie | Magazijnbeeld vóór de titel. Titel boven het beeld. |
| Over Wespi | Oorsprong; Wat we doen | Naamillustratie respectievelijk Wespi-visual vóór de titel. Ook de CSS/HTML-illustraties meenemen, niet alleen `img`-elementen. |

Voor hero's mét beeld is beeld → titel → beschrijving/knoppen op de onderzochte mobiele pagina's correct. Offerte heeft een teksthero zonder afbeelding; juridische pagina's hebben geen hero. Geen nieuwe beelden toevoegen uitsluitend om deze regel letterlijk af te vinken.

### B7 — Gemeten hoogte en witruimte

Momentopname in pixels, afgerond, 1440px desktop en 375px mobiel. Volledige paginahoogte is inclusief gedeelde contact-CTA en footer. Hoogte op zichzelf is geen fout.

| Pagina | Hero desktop / mobiel | Volledige pagina mobiel | Visuele interpretatie |
|---|---:|---:|---|
| Home | 767 / 1226 | 7989 | Beeld, lange kop, twee knoppen en gestapelde pluspunten maken eerste schermen lang. Praktijk en voordelen herhalen deels de drie diensten. |
| Beeld | 778 / 1127 | 5831 | H1 is lang en bevat twee boodschappen; kan na goedkeuring compacter. |
| Kledingfotografie | 836 / 1152 | 9075 | Compleet aanbod, maar meerdere secties zijn mobiel ruim 1200px. Kleine detailtekst contrasteert met grote koppen. |
| Packshotfotografie | 879 / 1163 | 7351 | Galerijen en kaarten binnen kaarten vergroten lengte; prijs en voordelen worden per categorie sterk herhaald. |
| AI-modelfotografie | 650 / 896 | 5476 | Desktopvoorbeelden hebben veel lege ruimte: momenteel één beschikbare modelserie in een breder galerijraster. Geen fictieve voorbeelden toevoegen. |
| Kledingbeeldbewerking | 650 / 814 | 6630 | Vergelijkingssectie alleen al 2068px mobiel. Functioneel zinvol; schaal/onderlinge afstand beoordelen, niet verwijderen. |
| Autobeeldbewerking | 650 / 843 | 8207 | Basis behouden. Vooral gestapeld tarievenoverzicht en dubbele contactuitnodiging bepalen lengte, niet opnieuw de hero ontwerpen. |
| Productdata | 785 / 1128 | 8852 | Werkwijze, vaste tarieven en abonnementen zijn elk circa 1500–1700px mobiel. Prijseenheden en essentiële uitleg behouden bij inkorten. |
| Slimmer werken | 808 / 1096 | 7708 | Voorbeeldensectie circa 3396px mobiel door grote invoer-/resultaatdiagrammen; grootste kandidaat voor compactere kaarten. |
| Over Wespi | 565 / 805 | 6357 | Persoonlijke achtergrond is waardevol; illustraties en voor-/na-ruimte kunnen selectiever. |
| Contact | 580 / 682 | 3556 | Eerst bruikbaar formulier, daarna opnieuw een grote algemene contact-CTA. |
| Offerte | 462 / 441 | 3235 | Minder zwaar visueel; betrouwbare verzending gaat vóór cosmetische gelijkmaking. |

Kleur- en typografiebasis is herkenbaar, maar `#dfb91a`, `#b99348` en warme bruintinten worden wisselend als goud gebruikt. Niet alle knoppen zijn gelijkwaardig: de pagina Beeld heeft zwarte actieknoppen waar dienstenpagina's meestal goud gebruiken. Dit hoeft geen fout te zijn, maar vraagt een bewuste rolverdeling voor primair/secundair. Leg een klein herbruikbaar palet en afstandsritme vast; geen generieke redesignopdracht afleiden uit deze audit.

## C. Kleine optimalisaties

| ID | Huidige situatie en probleem | Voorstel / bestanden | Prioriteit; risico |
|---|---|---|---|
| C1 | Geen Open Graph-metadata of JSON-LD aangetroffen op de afgeronde pagina's. Deelvoorbeelden zijn niet gericht ingericht. | Paginaspecifieke OG-title, description, image en URL via `base.html`; Organization en eventueel breadcrumbs met uitsluitend bevestigde gegevens. Geen ratings of resultaten verzinnen. | P3; laag tot middel. |
| C2 | Slimmer werken-title is 74 tekens; Packshot-description 170 en V2-description 169. Juridische descriptions zijn juist zeer kort. Lengte is geen automatische SEO-fout. | Werkelijk zoekresultaat/deelvoorbeeld beoordelen en waar zinvol compacter of specifieker formuleren. Zoekwoorden natuurlijk behouden; geen generieke herschrijving van alle titels. | P3; laag. Pagina-templates. |
| C3 | Geen eigen HTML-404; onbekende route geeft correcte 404 met JSON `{"detail":"Not Found"}`. | Bezoekersvriendelijke HTML-foutpagina met Home/Contact-links; status 404 behouden en API-fouten niet onbedoeld omzetten naar HTTP 200. | P3; middel. `app.py`, nieuw template na opdracht. |
| C4 | Lokaal zijn API-documentatie en OpenAPI publiek bereikbaar; securityheaders/compressie en expliciet cachebeleid zijn niet aangetroffen. Statische bestanden hebben wel ETag/Last-Modified. | Productieproxy/TLS/headers/compressie en caching controleren; docsbeleid bewust kiezen. HSTS alleen op correcte HTTPS-host. Geen conclusie trekken dat de uiteindelijke hosting deze voorzieningen mist. | P2 als releasecheck, uitvoering afhankelijk van hosting; middel. `app.py` en hostingconfiguratie. |
| C5 | `requirements.txt` is niet vastgepind, geen projecttests/testconfiguratie aangetroffen en 1705 `.venv`-bestanden zijn getrackt. Er is geen aangetroffen deployment-/rollbackinstructie. | Reproduceerbare installatie en beperkte regressietests voor routes/formulier vastleggen; virtuele omgeving in aparte beheertaak uit bronbeheer halen. Niet tijdens deze audit opschonen. | P3; middel. Requirements, repository-/deploymentafspraken. |
| C6 | Geen skiplink aangetroffen. Sommige eyebrows/detailteksten zijn circa 8–11px. De bewegende klantenstrook is geen werkelijk horizontaal scrollprobleem, maar kan afleiden. | Skiplink en focusweergave toetsen, kleine informatietekst leesbaarder maken; bewegingsreductie en pauzeerbaarheid van de logostrook beoordelen. | P3; middel. `base.html`, betrokken CSS. |
| C7 | Footer heeft naam, e-mail en juridische links, maar geen telefoon/adres/KvK; die staan wel op Contact. Copyright is vast 2026 en nu juist. | Directe `/contact`-link en telefoon overwegen; niet alles uit de contactpagina dupliceren. Jaar bij toekomstige jaarwisseling controleren. | P3; laag. `onderdelen/footer.html`. |
| C8 | Diverse assets hebben generieke namen (`auto-voorbeeld-showroom.jpg`) en automotive staat in `beeldbewerking/beeldbewerking/`. Alt-teksten zijn overwegend beschrijvend; ontbrekende alt-attributen zijn niet gevonden. | Pas bij noodzakelijke assetoptimalisatie namen normaliseren en verwijzingen zorgvuldig migreren. Een beschrijvende bestandsnaam is geen reden om nu bestaande assets massaal te verplaatsen. | P3; middel door paden/caching. |

## D. Controle per pagina

Alle onderstaande pagina's geven HTTP 200. Alle afgeronde pagina's hebben één H1 en een eigen title en description. De publieke pagina's hebben een zelfverwijzende HTTPS-canonical; V2 is de bewuste uitzondering met `noindex, nofollow` en zonder canonical. Er zijn geen dubbele pagina-titles of dubbele IDs aangetroffen.

| Pagina / route | Korte inhoudelijke, visuele en commerciële beoordeling | Gericht vervolg |
|---|---|---|
| Home `/` | Beeld, Data en Slimmer werken staan herkenbaar en gelijkwaardig in de hero/dienstkaarten. Praktijkverwijzingen maken de samenhang concreet. Visueel aantrekkelijk, maar mobiel lang en rijk aan kaartvormen. | A2/A5; B1/B7/B8. Met echte praktijkresultaten vertrouwen versterken zodra die beschikbaar en bevestigd zijn; huidige voorbeeldkaarten niet als bewezen cases presenteren. |
| Beeld `/beeld` | Logische ingang naar productfotografie en nabewerking. Goede interne links naar kleding en packshot. Lange hero en zeer zware kledingbeelden. | A2/A5, B7. Decoratieve accentcirkel valt buiten viewport maar is geclipt; niet als afgebroken tekst rapporteren. |
| Kledingfotografie `/productfotografie/kledingfotografie` | Duidelijk aanbod bodyform/ghost mannequin en plat, concrete prijzen en uitleg. AI-aanvulling past bij de positionering. Merkenstrook draagt bij aan vertrouwen. | A4 `#bodyform`, A2/A5, B1/B5/B7/B9. De bewegende strook heeft opzettelijk overlopende inhoud binnen een masker. |
| Packshot `/productfotografie/packshotfotografie` | Productgroepen en vanafprijs zijn concreet; veel voorbeelden. Kaart-in-kaartpresentatie en herhaling maken mobiel lang. | A2/A5, B1/B5/B8/B9. Alle negen galerijbeelden openen op muisklik; de triggers zijn niet via Tab bereikbaar. |
| AI `/productfotografie/kledingfotografie/ai-modelfotografie` | Aanvulling op kledingfotografie, uitvoering door Wespi en aparte AI-tarieven worden duidelijk uitgelegd. Alle vier prijzen aanwezig; geen aparte dubbele afsluitsectie. | B4 en B1. Er wordt één beschikbare serie getoond; overige voorbereide series worden niet als nepportfolio getoond. Video 1080×1920, circa 10,03 s: metadata geladen, dialoog opent/sluit en media wordt vrijgegeven. Volledige afspeel-/kwaliteitscontrole niet gedaan. |
| Kledingbeeldbewerking `/beeldbewerking/kleding` | Helder onderscheid: bestaande foto's bewerken. Drie echte vergelijkingen en €1,99/€3,49 met btw-toelichting. | B1/B7/B8; A5. Sliders starten bewust op volledig origineel. Deze keuze behouden. |
| Automotive `/beeldbewerking/automotive` | Herkenbaar voor autobedrijven; zes mogelijkheden, dezelfde gele auto in de achtergronden, echte Mercedes-vergelijking, bestaande staffels en toeslagen. Grote volumes heeft de laatst gekozen grijze sectie. | B1 voor mobiele titelvolgorde, A2/A5 waar van toepassing, A3 migratie. Hero en beelden niet opnieuw naar persoonlijke voorkeur aanpassen. De gele bestelbus is door eigenaar bevestigd. Doorlooptijd is gebruikelijk, geen harde garantie. |
| Productdata `/data/productdata` | Verwerken, verrijken en productcontent zijn onderscheiden; invoerbeperkingen en scope worden benoemd. Losse tarieven plus drie serviceabonnementen zijn overzichtelijk op desktop. | B1/B7/B9 en A5. Data als uitvoering van gegevenswerk behouden; geen softwareproduct suggereren. De hero-image gaf één time-out in parallelle HTTP-test en laadde bij herhaling correct. |
| Slimmer werken `/slimmer-werken` | Terugkerende handelingen worden concreet gemaakt. Bestaande €249 en €499 zijn aanwezig; geen prijswijziging nodig. De invoer-/uitvoerillustraties zijn begrijpelijk, maar nemen mobiel veel ruimte in. | B1/B7/B9, A5. Niet ongemerkt vervangen door V2. |
| Slimmer werken V2 `/slimmer-werken-v2` | Bestaande testpagina, niet in het hoofdmenu. Toepassingen passen bij procesverbetering; geen prijskaarten of beschikbare apps verzonnen. | `noindex, nofollow` behouden en uit publieke sitemap laten. Geen advies om V2 automatisch live te zetten. |
| Over Wespi `/over-wespi` | Naamverhaal, persoon en werkplek geven vertrouwen. Visueel warmer/bruingouder dan de dienstenpagina's; persoonsbeeld is relevant. Claim 15+ jaar niet onafhankelijk geverifieerd. | B1, A5 en B7 waar nuttig. Feitelijke claims alleen wijzigen na bevestiging. |
| Contact `/contact` | Telefoon, e-mail, adres, tijden en bedrijfsgegevens aanwezig. Formulier heeft labels, verplichte velden, honeypot en servervalidatie. | A1 echte levering, A4 postcodecontrole en B8 dubbele uitnodiging. Privacytoestemming bevat geen directe link naar de verklaring; die staat wel in de footer. |
| Offerte `/offerte` | Duidelijke aanvraagvelden en dienstselectie. De queryparameter voor kledingfotografie selecteert die dienst correct. | A1 is eerste prioriteit. Naar mailclient verwijzen is geen betrouwbare webverzending. Geen testaanvraag verstuurd. |
| Privacy `/privacyverklaring` | Leesbare tekstkolom en metadata. Onjuiste e-maillinks, postcodeverschil en verschillende cookieomschrijvingen. | A4/B11; gegevens en tekst door eigenaar laten controleren. |
| Voorwaarden `/algemene-voorwaarden` | Renderen, eigen H1/canonical en leesbare juridische kolom. Veel tekst: circa 41.759px hoog op 375px breed, grotendeels verklaard door documentlengte. | Niet puur voor compactheid herschrijven. Eventuele inhoudsopgave is P3; geldigheid/actualiteit niet juridisch beoordeeld. |

**Uitsluitingen:** `/beeldbewerking` geeft HTTP 200 en de navigatielink werkt. Productbeeldbewerking is een inactief menu-item, geen kapotte actieve link. De als probe geteste `/beeldbewerking/product` geeft 404; dit bewijst geen ontbrekende afgesproken route. Geen ontwerp-, tekst- of SEO-inhoudelijke beoordeling van beide onafgeronde pagina's.

## E. Technische checklist

| Onderdeel | Status | Werkelijk gecontroleerd / grens |
|---|---|---|
| 16 GET-paginaroutes | Gecontroleerd en akkoord | Alle HTTP 200; één H1 op afgeronde pagina's. |
| Beeldbewerking / Productbeeldbewerking | Gecontroleerd en akkoord binnen uitzondering | Hoofdroute bereikbaar; productitem bewust niet klikbaar en geen aangetroffen route. Geen inhoudelijk oordeel. |
| Bestaande publieke URL-migratie | Probleem gevonden | Oude automotive- en juridische URL's lokaal 404, zie A3. Productieproxy nog onbekend. |
| Interne actieve paginalinks | Gecontroleerd en akkoord | Geen ontbrekende actieve interne paginabestemming gevonden in de crawl. Ankers en placeholders apart afgekeurd. |
| Externe bestemmingen | Niet volledig getest | Websites van klantmerken, externe juridische verwijzingen en mailclients zijn niet uitputtend gecontroleerd. De audit van bereikbaarheid richt zich op lokale routes/assets; verkeerd opgebouwde e-maillinks zijn wel uit de bron vastgesteld. |
| Fragmenten en placeholders | Probleem gevonden | Footer `#praktijk` op subpagina's, vier `#`-links, kledinghero `#bodyform`. |
| Afbeeldingen/CSS/JS | Gecontroleerd en akkoord voor bereikbaarheid | Geen blijvend ontbrekende gebruikte asset gevonden; ook CSS-URLs gecontroleerd. |
| Browserconsole bij laden | Gecontroleerd en akkoord | Geen site-eigen JS-runtime-excepties/consolefouten in 61 vastgelegde paginaladingen. Fouten in tijdelijke auditprobes zijn niet als sitefout meegeteld. |
| Desktopdropdown muis | Probleem gevonden | Bereikbaar via aaneengesloten hovergebied; label ligt ver links, hover-ARIA niet bijgewerkt en Escape sluit niet zolang hover blijft. |
| Desktopdropdown toetsenbord | Gecontroleerd en akkoord voor basispad | Met volledige Enter-toetsaanslag opent het paneel; na animatie gaat Tab naar Productfotografie. Overige focus-/hoverstatus zie B3. |
| Mobiel/tabletmenu | Gecontroleerd en akkoord voor basispad | Op 375/430/768 openen menu en Beeldgroep; links aanwezig; Escape sluit. Geen echte touchhardware of complete screenreadertest. |
| Horizontaal scrollen | Gecontroleerd en akkoord | Geen daadwerkelijke viewportbrede horizontale scroll op onderzochte breedtes. Overlopende decoraties, geclipte logostrook en bewust verborgen honeypot zijn geen contentfouten. |
| Mobiele hero-volgorde | Gecontroleerd en akkoord | Op pagina's met hero-afbeelding staat deze boven de titel. |
| Mobiele overige beeld-tekstvolgorde | Probleem gevonden | Concrete afwijkingen in B1. |
| Automotive-slider | Gecontroleerd en akkoord voor geteste bediening | Start 50; ArrowLeft → 49 en correcte `aria-valuetext`. Muisbediening eveneens getest. |
| Kledingbeeldbewerking-sliders | Gecontroleerd en akkoord voor geteste bediening | Drie initialisaties gecontroleerd in rendering; eerste slider interactief 100 → 99. Niet elk paar op elk apparaat afzonderlijk bediend. |
| Kledingfotografie-lightbox | Probleem gevonden | Opent/sluit met Escape, maar focus verlaat overlay bij Tab. |
| Packshotlightbox | Probleem gevonden | Muisklik en Escape werken; beelden niet focusbaar en geen dialoogfocus. |
| AI-foto/video-lightbox | Gecontroleerd en akkoord voor geteste werking | Native dialoog opent/sluit; fotomedia ingevoegd; videometadata beschikbaar; media na sluiten verwijderd. Volledig afspelen/audio en alle browserformaten niet getest. |
| Contactvalidatie | Gecontroleerd en akkoord | Leeg, fout e-mailadres, te lange invoer, ontbrekende toestemming en controletekens: 422; honeypot: 400; escaping van scriptinvoer gecontroleerd. |
| Contactsysteem succes/fout | Gecontroleerd en akkoord met simulatie | Gesimuleerde verzending 200; gesimuleerde SMTP-fout en ontbrekende configuratie 503 met melding. |
| Echte e-mailaflevering | Niet kunnen testen binnen audit | Niet verstuurd; configuratie/ontvangst/Reply-To extern nog controleren. |
| Offerteverzending | Probleem gevonden | Mailto-flow; geen serverafhandeling of bevestiging. |
| Titel, description, H1, canonical | Gecontroleerd en akkoord voor aanwezigheid | Eigen metadata, één H1; V2 bewust noindex zonder canonical. Lengte/zoekwoordverfijning zie C2. |
| H2/H3-structuur en alt-teksten | Gecontroleerd en akkoord als basis | Geen algemene H1-dubbeling; functionele sectietitels en alt-attributen aanwezig. Kleine label-H2 bij kledingtarieven is semantisch minder fraai, geen blokkade. Geen volledige handmatige beoordeling van elk tekstfragment. |
| Indexeerbaarheid | Probleem gevonden in release-inrichting | V2 correct noindex; robots/sitemap ontbreken; nog niet afgeronde route heeft geen aangetroffen noindex. Publicatiebeleid vooraf afstemmen. |
| Open Graph / structured data | Probleem gevonden, niet blokkerend | Niet aangetroffen. Geen verplichte rankinggarantie aan koppelen. |
| Foutpagina | Probleem gevonden, niet blokkerend | Juiste 404-status, maar JSON voor bezoekers. |
| Basisbeveiliging | Deels gecontroleerd; productie niet kunnen testen | Contactvelden begrensd, e-mailvalidatie, honeypot, headercontroletekens en Jinja-escaping aanwezig. Geen app-level rate limiting of request-bodylimiet aangetroffen; TLS/headers/limieten kunnen bij proxy staan. Geen penetratietest uitgevoerd. |
| Caching/compressie | Deels gecontroleerd; productie niet kunnen testen | Lokale static ETag en Last-Modified aanwezig; geen expliciete Cache-Control/Content-Encoding op onderzochte responses. Geen browser-/CDN-beleid bewezen. |
| Performance/CWV | Probleem gevonden; CWV niet gemeten | Te zware assets bewezen. Geen Lighthouse-score of echte LCP/INP/CLS-conclusie. |
| Footer | Probleem gevonden | Naam, e-mail, privacy/voorwaarden en juist jaar aanwezig; placeholders en dubbele contactuitnodiging aanpakken. |

## F. Concreet verbeterplan

Dit plan moet eerst worden goedgekeurd. Er is geen wijziging aan websitecode uitgevoerd en niets gecommit of gepusht. Voor ieder ID staan huidige situatie, probleem, voorstel, prioriteit en risico hierboven. Onderstaande volgorde bundelt werkzaamheden om nieuwe losse ontwerpaanpassingen te voorkomen.

| Fase | Opdracht en bestanden | Bewijs nodig voor afronding |
|---|---|---|
| 1 — Conversie en feiten | A1/A4/B11: `oferte.html`, `contact.html`, `routes/paginas.py`, `onderdelen/footer.html`, kledinghero/bodyform, privacyverklaring. Eigenaar bevestigt postcode, verwerking en btw waar nodig. | Web-offerte succesvol en foutpad getest; toestemming voor echte testmail; correcte fragmenten, mailcontacten en footerbestemmingen. Geen onbevestigde bedrijfsgegevens gepubliceerd. |
| 2 — Migratie en release | A3/B6/C4/C5: bestaande URL-lijst, redirects in router of proxy, sitemap/robots, hosting-/rollbackinstructie. Onafgeronde pagina's alleen technisch behandelen. | Oude URL's bereiken de juiste nieuwe pagina zonder ketens; geen ongewenste indexeerbare staging/V2; HTTPS, SMTP en reverse proxy gecontroleerd in doelomgeving. |
| 3 — Media | A2: grootste assets eerst; responsive varianten en lightboxoriginelen scheiden; `base.html`-afhankelijkheden nog niet tegelijk herschikken. | Alle beelden bestaan en behouden detail/uitsnede; aanzienlijk kleinere mobiele downloads; sliders/video/lightboxes blijven werken. Meting onder vastgelegd netwerkprofiel. |
| 4 — Navigatie en toegankelijkheid | A5/B2/B3/B4/B5: menu-template, `header.css`, `main.js`, lightboxcode en beperkte tekstkleurselectors. | AI logisch vindbaar; vloeiende muisroute; Enter/Tab/Escape en touch; focus in geopende dialoog; contrast opnieuw meten. Behoud huisstijl vooraf afstemmen waar eerdere beschermde ontwerpen geraakt worden. |
| 5 — Eén visuele afrondingsronde | B1/B7/B8/B9: relevante paginaonderdelen en paginaspecifieke CSS. Start met mobiele titelvolgorde, hoge Slimmer werken-kaarten, Packshotkaarten en dubbele afsluitingen. | Screenshots op 375, 430, 768 en desktop; volledige paginavolgorde bekeken; bedragen/diensten/URL's ongewijzigd; automotive-hero behouden. Geen wijzigingen aan onafgeronde dienstenpagina's. |
| 6 — Zoekpresentatie en onderhoud | C1/C2/C3/C6/C7/C8/B10: OG/metadata, juiste foutpagina, skiplink en geleidelijk selectieve stylesheets. | Zelfde routes blijven werken, geen ontbrekende stijlen, correcte deelvoorbeelden en foutstatussen. Regressietests na iedere kleine technische stap. |

### Beslissingen die nog nodig zijn

1. Eén betrouwbare manier om offertes en contactberichten te versturen, plus gecontroleerde echte aflevering.
2. Definitieve lijst oude URL's en de plaats waar redirects worden beheerd.
3. Bevestiging van postcode en de feitelijk geldende privacy-/cookieomschrijving; btw bij de nog niet expliciet gemarkeerde dienstprijzen.
4. Goedkeuring van het AI-menu-item en een contrastgeschikte tekstkleur, zonder ongecontroleerde globale kleurwijziging.
5. Goedkeuring van de mobiele titelvolgorde waar dit afwijkt van eerdere beeldplaatsingskeuzes. De bestaande bedragen €249/€499, automotive-staffels, AI-prijzen, dienstpositionering en V2-teststatus blijven uitgangspunt.

### Verificatie van deze audit

De ruwe browser-/HTTP-resultaten en screenshots staan tijdelijk buiten de projectbroncode in `%TEMP%/wespi-website-audit/`; zij zijn geen blijvende projectbestanden en dit rapport bevat de relevante bewijsdetails zelfstandig. De formulierprobes gebruiken uitsluitend gesimuleerde verzending. De afsluitende hashcontrole bevestigt dat alle 147 vooraf geïnventariseerde bron- en documentatiebestanden ongewijzigd zijn gebleven; uitsluitend dit rapport is toegevoegd.

**Enig door deze opdracht toegevoegd projectbestand: `docs/WEBSITE_AUDIT.md`.** Projectbesluiten zijn niet aangepast: dit rapport bevat voorstellen, geen nieuwe besluiten.
