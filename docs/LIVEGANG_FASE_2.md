# Wespi — livegang fase 2

Datum: 5 november 2026. Uitvoering van de expliciet goedgekeurde fase 2: navigatie en mobiele volgorde. [Fase 1](./LIVEGANG_FASE_1.md) blijft behouden. De [website-audit](./WEBSITE_AUDIT.md) is de oorspronkelijke momentopname en is niet herschreven.

## Navigatie

- Het desktopmenu is links uitgelijnd onder Beeld, in plaats van gecentreerd. Het paneel is 320px breed in plaats van 420px. Productfotografie begint daardoor dicht bij de trigger, met behoud van de bestaande twee groepen en huisstijl.
- De bovenrand sluit aan op de trigger. Een korte sluitvertraging van 180ms vangt kleine muisafwijkingen op. Klik kan het menu openhouden; buitenklik sluit het. Er is geen extra hoverlaag toegevoegd.
- Hover opent nu dezelfde JavaScript-status als klik en toetsenbord, inclusief correcte `aria-expanded`. CSS-hover kan het menu na Escape niet opnieuw zichtbaar houden.
- Enter/Spatie schakelen het menu; Tab volgt de bestaande links. Pijl omlaag/omhoog opent en verplaatst de focus naar de eerste/laatste link. Bij openen is de zichtbaarheid onmiddellijk beschikbaar voor focus; de bestaande overgang van opacity/positie blijft behouden.
- Escape sluit de dropdown en herstelt de focus naar Beeld als die binnen de dropdown stond. Op mobiel sluit een volgende Escape het hoofdmenu en herstelt de focus naar de menuknop. Aanraking, buitenklik, linkselectie en omschakelen tussen desktop en mobiel houden de toestand consistent.
- Op korte schermen liep de onderkant van het mobiele menu buiten de viewport: de oude maximumhoogte trok een vaste 64/72px af terwijl de werkelijke header hoger kon zijn. De maximumhoogte gebruikt nu de daadwerkelijke headercontainer en dynamische viewporthoogte, met een `vh`-fallback. De header zelf en hero's zijn niet gewijzigd.
- AI-modelfotografie is direct onder Kledingfotografie toegevoegd aan Productfotografie via de bestaande route `/productfotografie/kledingfotografie/ai-modelfotografie`. Beeldbewerking volgt de gevraagde volgorde Autobeeldbewerking, Kledingbeeldbewerking en Productbeeldbewerking; de laatste blijft een inactieve tekstvermelding.

## Mobiele volgorde

De volgende 14 onderdelen uit audit B1 tonen in hun gestapelde weergave de bestaande bovenkop/titel, het bestaande beeld en vervolgens de overige inhoud:

| Pagina | Onderdeel |
|---|---|
| Home | Waarom Wespi |
| Kledingfotografie | AI-promotie; Werkwijze |
| Packshotfotografie | Schoenen; Accessoires; Andere producten |
| AI-modelfotografie | Tarieven |
| Kledingbeeldbewerking | Volume en werkwijze |
| Autobeeldbewerking | Grote volumes |
| Productdata | Werkwijze; Vaste tarieven |
| Slimmer werken | Prijssectie |
| Over Wespi | Oorsprong; Wat we doen |

Dit is uitgevoerd in de bestaande sectiestylesheets met CSS-volgorde en `display: contents` op niet-semantische layoutdivs. Er zijn geen dubbele titels, afbeeldingen of alternatieve mobiele tekstblokken toegevoegd. Bestaande omslagpunten blijven behouden: een tabletsectie die al naast elkaar stond, blijft naast elkaar staan; secties die al gestapeld werden, krijgen de juiste volgorde. Koppen, paragrafen en interactieve onderdelen behouden hun eigen elementen.

Padding die aan een vervallen mobiele layoutbox hing is waar nodig op de betreffende sectie overgenomen. Bestaande beeldhoogtes en afbeeldingsverhoudingen zijn behouden. Er is geen algemene verkleining van kaarten, secties of witruimte uitgevoerd. Door de nieuwe titelpositie ontstaat alleen de benodigde afstand tussen titel en beeld.

Hero's zijn niet aangepast. De bestaande afbeelding → titel → tekst-volgorde van de beeldhero's blijft behouden. Routes, teksten, tarieven en afbeeldingen zijn niet veranderd. Beeldbewerking en de inactieve Productbeeldbewerking hebben geen inhoudelijke wijzigingen gekregen.

## Gewijzigde bestanden

Navigatie:

- `templates/onderdelen/header.html`
- `static/css/header.css`
- `static/js/main.js` — uitsluitend het navigatiegedeelte; bestaande packshotlightboxcode exact behouden.

Mobiele sectiestyling:

- `static/css/voordelen.css`
- `static/css/kledingfotografie/ai-promotie.css`
- `static/css/kledingfotografie/werkwijze.css`
- `static/css/packshotfotografie/inhoud.css`
- `static/css/kledingfotografie/ai-modelfotografie.css`
- `static/css/beeldbewerking/kleding.css`
- `static/css/beeldbewerking/automotive.css`
- `static/css/productdata/werkwijze.css`
- `static/css/productdata/prijzen.css`
- `static/css/slimmer-werken/prijs.css`
- `static/css/over-wespi/over-wespi.css`

Uitsluitend versieparameters van gewijzigde CSS/JavaScript en hun importbundels, zodat oude browsercache de wijzigingen niet verbergt:

- `templates/base.html`
- `templates/kledingfotografie.html`
- `templates/ai-modelfotografie.html`
- `templates/automotive.html`
- `templates/kledingbeeldbewerking.html`
- `static/css/kledingfotografie.css`
- `static/css/packshotfotografie/packshotfotografie.css`

Documentatie:

- `docs/BESLUITEN.md`
- `docs/PROJECTKOMPAS.md`
- `docs/LIVEGANG_FASE_2.md` — dit nieuwe verslag.

Geen nieuwe dependencies, afbeeldingen of pagina's toegevoegd. Niet gecommit of gepusht.

## Testresultaten

| Controle | Resultaat |
|---|---|
| Bestaande fase 1-regressies | Alle 15 tests geslaagd: gesimuleerde formulierverzending, validatie, foutpaden/invoerbehoud, links, footer en redirects. Geen echte e-mail verstuurd. |
| Routes en footer | Alle 16 bestaande GET-pagina's blijven HTTP 200 geven. Alle bestaande lokale header- en footerbestemmingen bestaan. Drie fase 1-redirects blijven 301 → 200. |
| Schermbreedtes | Chromium: alle 16 pagina's op 1440, 768, 430 en 375px gecontroleerd, 64 combinaties. Geen horizontale documentoverflow of kapotte afbeeldingen. Geen vervormde afbeeldingen met `object-fit: fill` aangetroffen. |
| Desktopbehoud | Voor/na-metingen van alle 14 betrokken secties op 1440px: identieke posities en afmetingen. Geen desktopindeling veranderd. |
| Hero's, inhoud en beelden | Voor/na op negen betrokken pagina's bij alle vier breedtes: identieke hero- en hero-inhoudposities, identieke hoofdinhoudstekst en dezelfde afbeeldingsbronnen/alt-teksten. |
| Mobiele volgorde | Alle 14 onderdelen op 430 én 375px: titel vóór beeld en overige inhoud erna; geen overlap tussen deze delen. Screenshots van de mobiele secties visueel beoordeeld. |
| Desktopmuis | Werkelijk gesimuleerd pointerpad van Beeld naar Productfotografie blijft open. Vertrek, heropenen, pinnen met klik, buitenklik en Escape terwijl de muis boven het paneel staat slagen. |
| Toetsenbord | Enter, Spatie, Tab, pijl omlaag/omhoog en Escape getest; focus herstelt naar de juiste knop. Tab buiten de dropdown sluit deze. |
| Touch/tablet | Menuknop, Beeld-submenu en AI-link via CDP-touchsimulatie op 768, 430 en 375px getest. Menu blijft binnen het scherm, scrollt indien nodig en sluit bij routewisseling. |
| Korte schermen | Extra controle op 375×667 en 768×600: het paneel eindigt binnen de viewport. Met gesimuleerde touchswipes werkelijk gescrold; onderste Contact-link blijft bereikbaar en opent de contactpagina. |
| Nieuwe AI-link | Via echte browserklik op desktop en touchsimulatie op alle drie kleinere breedtes naar de bestaande AI-pagina gegaan; pagina en gesloten menu correct. |
| Bestaande interactieve functies | Op 1440 en 375px: automotive- en kledingvergelijker reageren op toetsenbord en pointer; kleding-/packshotlightbox en AI-fotodialoog openen en sluiten met Escape; Productdata-details openen/sluiten. Alle twaalf controles slagen. |
| Scopecontrole | SMTP-/formuliercode, offerte/contacttemplates, offerte-CSS, footer, privacyverklaring, fase 1-verslag/tests en bodyformdoel zijn identiek aan de nulmeting. Bestaande lightboxcode in `main.js` is exact behouden. |

Testopdracht voor de blijvende fase 1-tests: `py -3.12 -B -m unittest discover -s tests -v`. Browsermetingen, scripts, screenshots en bronkopieën van de nulmeting staan tijdelijk buiten de projectbroncode in `%TEMP%/wespi-fase2/` en bijbehorende `wespi-fase2-*.py`-scripts.

## Resterende aandachtspunten

- Binnen de geteste fase 2-onderdelen zijn geen open functionele fouten gevonden. Dit is een lokale Chromium-controle met touchsimulatie; Safari/iOS, Firefox en fysieke touchapparaten zijn niet afzonderlijk getest.
- Bestaande auditpunten zoals zware media, goudkleurige tekst met beperkt contrast en verdere lightboxtoegankelijkheid blijven ongewijzigd. Er is geen algemene huisstijl- of toegankelijkheidsherbouw uitgevoerd.
- De echte SMTP-aflevering en hosting-/proxycontrole uit fase 1 blijven productievoorwaarden. Deze fase heeft geen mailserververbinding gemaakt of echte e-mail verstuurd.
- Algemene sectiehoogtes, kaartformaten en witruimte zijn bewust niet geoptimaliseerd. Fase 3 wacht op akkoord.
