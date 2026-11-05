# Livegang fase 4 - SEO, technische eindcontrole en publicatievoorbereiding

Datum: 5 november 2026. De veilige lokale uitvoering is afgerond; dit is **geen livegangakkoord**. Fase 1, 2 en 3 en het latere herstel van de Over Wespi-hero blijven behouden. De beginsituatie en Git-diff zijn gecontroleerd; bestaande wijzigingen buiten fase 4 zijn niet teruggedraaid. Er is niet gecommit, gepusht of gedeployd. Geen echte e-mail verstuurd.

## Uitgevoerde verbeteringen

### SEO en crawling

- Alle 14 afgeronde publieke pagina's hebben een unieke title, eigen beschrijving, precies één H1 en een zelfverwijzende HTTPS-canonical. Bestaande goedgekeurde teksten zijn behouden, ook de langere Slimmer werken-title en korte juridische beschrijvingen; een lengte alleen is geen reden voor herschrijven.
- Kopstructuur: geen overgeslagen H1/H2/H3-niveaus aangetroffen. Dezelfde H1 op Home en Over Wespi is bestaande merkpositionering; de pagina-inhoud en SEO-titles verschillen. Geen nieuwe dubbele pagina's of routes gemaakt.
- Open Graph-title en description worden uit de bestaande templateblokken hergebruikt. Iedere afgeronde pagina krijgt een vaste canonieke deel-URL, locale, sitenaam en een bestaande JPG/PNG-afbeelding. Deze openbare HTTPS-afbeeldings-URL's zijn lokaal op bestandsbestaan gecontroleerd; echte sociale crawlers moeten na publicatie worden gecontroleerd.
- Alle afbeeldingen hebben alt-attributen. Bestaande beschrijvende alt-teksten zijn behouden; decoratieve beelden hoeven geen extra zoekwoorden. Geen onbevestigde structured data, beoordelingen of bedrijfsclaims toegevoegd.
- `siteconfig.py` bevat de expliciete lijst met 14 afgeronde pagina's en hun bestaande deelbeelden. Geen automatische opname van alle routes. `/sitemap.xml` gebruikt de bestaande canonieke URL's zonder verzonnen lastmod-data.
- `/robots.txt` onderscheidt productie van development/staging. `WESPI_ENV=production` staat crawlen toe en vermeldt de sitemap. Standaard en staging blokkeren crawlen en leveren tevens `X-Robots-Tag: noindex, nofollow`. Ongeldige omgevingswaarden stoppen de start.
- Beeldbewerking, Productbeeldbewerking en Slimmer werken V2 zijn niet in de sitemap opgenomen. Hun routes, inhoud en navigatie zijn niet aangepast. De productie-indexeerbaarheid van Beeldbewerking is bewust niet zelfstandig veranderd: dit blijft een releasebesluit.
- Alle 446 gecontroleerde actieve interne pagina-/fragmentverwijzingen werken. Geen nieuwe redirects toegevoegd; de drie fase-1-redirects zijn opnieuw op één 301 en een 200-bestemming getest. Zie [apart migratieoverzicht](./LIVEGANG_MIGRATIE.md).

Robots/noindex zijn geen toegangsbeveiliging. Een crawler kan een door robots geblokkeerde pagina niet lezen om haar noindex te zien; staging daarom vóór externe toegang met authenticatie/netwerktoegang beschermen. Onderbouwing: [Google: noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) en [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro).

### Techniek en veiligheid

- FastAPI draait met `debug=False`; publieke `/docs`, `/redoc` en `/openapi.json` zijn uitgeschakeld.
- Eenvoudige Wespi-404 met links naar Home en Contact, met echte 404-status en noindex. Alleen navigatieverzoeken die HTML accepteren krijgen HTML. `/api...`, ontbrekende statische bestanden en JSON-verzoeken blijven JSON-fouten met hun foutstatus. Een 405 wordt niet omgezet in HTML/200.
- Onverwachte serverfouten geven een generiek 500-antwoord zonder exceptiondetails; HTML voor paginanavigatie en JSON voor API-verzoeken. Ook foutantwoorden worden niet opgeslagen.
- Kleine response-policy voor `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-Frame-Options: SAMEORIGIN` en een beperkte Permissions-Policy. Dezelfde headers zijn aanwezig op app-500-antwoorden. Geen HSTS, HTTPS-redirect of CSP op basis van onbewezen hostingaannames toegevoegd.
- HTML gebruikt `no-cache` (herbevestigen), Contact/Offerte en fouten `no-store`; statische bestanden maximaal één uur met bestaande ETag/Last-Modified. Assetversies zijn gericht bijgewerkt.
- Bestaande Starlette-Gzip wordt gebruikt voor gewone GET-antwoorden vanaf 1024 bytes als de client gzip accepteert. Beelden/video/statische bestanden en Contact/Offerte zijn uitgezonderd. Geen nieuwe dependency. CSS/JS-compressie kan op de productieproxy worden ingericht.
- SMTP-configuratie, Reply-To, validatie, honeypot, velden en verzendgedrag zijn behouden. Alleen de twee applicatielogs bij SMTP-falen zijn gesaneerd: geen traceback met mogelijk gevoelige SMTP-reacties. Er zijn geen geheimen toegevoegd.
- Misbruikbeperking bestaat nog uit servervalidatie, lengtegrenzen en honeypot. Proxyverzoeklimieten/rate limiting, vertrouwde hosts/proxy-IP's, TLS, HSTS en een eventueel CSP zijn concrete hostingvoorstellen in de deploymentchecklist; geen onbevestigde infrastructuurwijzigingen uitgevoerd.
- Een bestaande PNG-logo is als favicon gekoppeld; de automatische ontbrekende favicon-aanvraag veroorzaakte anders een console-404.

Implementatie is getoetst aan geïnstalleerde FastAPI/Starlette-versies en de officiële [Starlette-middlewaredocumentatie](https://www.starlette.io/middleware/).

### Toegankelijkheid en performance

- Skiplink als eerste toetsenborddoel naar focusbare hoofdinhoud, zichtbare focusranden en globale bewegingsreductie bij gebruikersvoorkeur. Geen wijziging aan de normale pagina-indeling. De bestaande logostrook kan al pauzeren via hover/focus en stopt bij reduced-motion.
- Kleding- en packshotvergrotingen gebruiken native dialogen voor modaliteit en focusbeheer. Packshotbeelden zijn bereikbaar met Tab en openen met Enter/Spatie. Escape, sluitknop, klik op donkere achtergrond, vergrotingsbron en bestaande opmaak blijven werken. Focus keert terug naar de trigger.
- Formulierlabels en bestaande foutmeldingen zijn gecontroleerd. Geen wijzigingen aan tarieven, inhoud, navigatie, sliders of hero-ontwerpen.
- Over Wespi en Kledingbeeldbewerking hadden nog een belangrijk hero-beeld met lazy-loading; dit is eager/high priority gemaakt. Alleen laad-attributen zijn veranderd.
- Alle WebP-verwijzingen, responsive varianten en detailbronnen blijven aanwezig. De reeds herstelde Over Wespi-vlag blijft rechtop op alle vier breedtes; geen WebP met afwijkende oriëntatiemetadata aangetroffen. Geen nieuwe beeldconversies of mediabestanden in fase 4.
- AI-video preview gebruikt preload=none en start niet automatisch. De video wordt pas na openen aangevraagd; afspelen is werkelijk gesimuleerd en bij sluiten wordt de bron vrijgegeven.

## Testresultaten

| Controle | Resultaat |
|---|---|
| Permanente regressietests | 34 geslaagd: 15 fase 1, 6 fase 3 en 13 fase 4 |
| SEO | 14 afgeronde pagina's: unieke metadata, één H1, juiste canonical/OG, aanwezige deelbeelden en alt-attributen |
| Interne links | 446 actieve interne pagina-/fragmentverwijzingen zonder fout; ook permanente linkregressie toegevoegd |
| Sitemap/robots | XML met exact 14 unieke 200-bestemmingen; staging en productie apart getest; V2/onafgeronde pagina's uitgesloten |
| Redirects | Drie bevestigde routes: 301 → juiste bestemming → 200, geen lokale ketens |
| Fouten/API | HTML-404, JSON-404 voor API/static/JSON, 405 en veilige HTML-/JSON-500 getest; geen fout omgezet naar 200 |
| Headers/cache/compressie | ASGI-tests en werkelijke lokale HTTP-responses gecontroleerd; gzip decodeert naar identieke HTML; media en formulieren uitgezonderd |
| Formulierverwerking | Alle bestaande succes-/fout-/validatie-/spamtests slagen; SMTP-foutlog bevat geen exceptiondetails |
| Browserformulieren | 16 inzendingen: Contact/Offerte × succes/falen × 1440/768/430/375; SMTP onderschept, invoerbehoud en meldingen correct |
| Paginaweergave | 16 bestaande pagina's × 4 breedtes = 64 combinaties; geen kapotte beelden, horizontale overflow of vervormde afbeeldingen |
| Console | Laatste volledige browserronde: 0 consolefouten |
| Mobiele volgorde | Alle 14 fase-2-onderdelen op 430 en 375px: 28 volgorde-/overlapcontroles geslaagd |
| Navigatie | Muispad, sluitvertraging, klik/buitenklik, toetsenbord inclusief Escape/focusherstel, touch, AI-link en breedtewissel geslaagd |
| Korte schermen | Touchscroll/onderste Contact-link bereikbaar op 375x667 en 768x600 |
| Bestaande functies | 24 controles op alle vier breedtes: beide typen sliders, kleding-/packshot-/AI-vergroting en Productdata-details |
| Productgalerijen | Alle 9 packshot- en 5 bodyformbeelden laden de volledige detailbron; beide AI-foto's openen/decodeerden/sloten op alle vier breedtes |
| Toegankelijkheid | Skiplink, zichtbare focus, Enter/Spatie, native modaliteit, inert achterliggende pagina, Escape/focusherstel, reduced-motion en formulierlabels op alle vier breedtes |
| Video | Op alle vier breedtes geen onnodige initiële mp4-download; werkelijk afgespeeld met voortgang, geldige dimensies/duur en opruimen na sluiten |
| Behoud | Prijsreeksen/beelden behouden; automotive-herohoogte identiek; Beeldbewerking-template, header-template/CSS, offerte-template, slider- en AI-script identiek aan fase-4-begin |

Herhaalbare broncodetests: `py -3.12 -B -m unittest discover -s tests -v`. Lokaal getest met Chromium/CDP en touchsimulatie. Screenshots van 404, vergrotingen/secties en formulierstatussen zijn beoordeeld. Tijdelijke meetgegevens staan buiten de applicatie in `%TEMP%/wespi-fase4/`; de blijvende tests staan in `tests/test_livegang_fase4.py`. `git diff --check` geeft geen whitespacefouten; bestaande CRLF-waarschuwingen van twee eerder gewijzigde automotive-templates zijn geen fase-4-wijziging.

## Gewijzigde bestanden

Dit is de fase-4-lijst ten opzichte van de vastgelegde beginsituatie, niet de veel grotere totale Git-diff uit eerdere opdrachten.

- `app.py`
- `docs/BESLUITEN.md`
- `docs/LIVEGANG_DEPLOYMENT.md`
- `docs/LIVEGANG_FASE_4.md`
- `docs/LIVEGANG_MIGRATIE.md`
- `docs/PROJECTKOMPAS.md`
- `routes/paginas.py`
- `siteconfig.py`
- `static/css/basis.css`
- `static/css/kledingfotografie.css`
- `static/css/kledingfotografie/bodyform.css`
- `static/css/packshotfotografie/inhoud.css`
- `static/css/packshotfotografie/packshotfotografie.css`
- `static/js/kledingfotografie-lightbox.js`
- `static/js/main.js`
- `templates/404.html`
- `templates/500.html`
- `templates/base.html`
- `templates/kledingbeeldbewerking.html`
- `templates/onderdelen/kledingfotografie/bodyform.html`
- `templates/over-wespi.html`
- `tests/test_livegang_fase4.py`

`templates/kledingbeeldbewerking.html` en `templates/over-wespi.html` wijzigen uitsluitend laad-attributen. De twee CSS-bundels wijzigen alleen cacheversies; de twee lightboxstylesheets bevatten uitsluitend native-dialogresets. `routes/paginas.py` wijzigt alleen twee logregels. Geen afbeeldingen, requirements, onafgeronde pagina-inhoud of navigatiebestanden gewijzigd.

## Niet lokaal vast te stellen / besluiten vóór publicatie

- **Onafgeronde pagina's:** Beeldbewerking is technisch 200, blijft in bestaande navigatie en is in productie nog indexeerbaar. Alleen sitemapuitsluiting is geen noindex. Productbeeldbewerking is een inactieve menuvermelding, de eerder onderzochte route geeft 404. Eigenaar moet technisch beschikbaar/navigatie/indexering afzonderlijk bevestigen vóór livegang.
- **Oude website:** de drie extra oude URL's en de volledigheid van de migratie vereisen bevestiging en een oude-site-/logs-/Search Console-export. Geen extra redirects verzonnen.
- **Hosting:** HTTPS/domein/proxy, productievariabelen, publieke statische bestanden, echte responseheaders, load-/rate-limits en foutlogging zijn nog niet op de beoogde hosting getest. Een stagingomgeving moet aanvullende toegangsbeveiliging krijgen.
- **SMTP:** echte aflevering, SPF/DKIM/DMARC, spammap en Reply-To in de productieomgeving vereisen aparte toestemming en een echte test.
- **Installatie:** requirements zijn niet vastgepind; de exact gekozen productie-installatie en transitieafhankelijkheden moeten in een schone stagingomgeving worden vastgelegd en getest. Geen virtuele omgeving opgeschoond of gedeployd.
- **Browsers/meting:** geen fysieke iOS/Safari-/Firefox-/screenreadertest of Core Web Vitals-/belastingmeting. Geen volledige WCAG- of securitycertificering. Echte zoekmachine-indexering en sociale deelcaches zijn pas op productie te beoordelen.

## Definitieve livegangchecklist

De praktische uitvoering met commando, omgevingsvariabelen, SMTP, back-up en rollback staat in [LIVEGANG_DEPLOYMENT.md](./LIVEGANG_DEPLOYMENT.md). Het aparte routeoverzicht staat in [LIVEGANG_MIGRATIE.md](./LIVEGANG_MIGRATIE.md).

- [ ] Besluiten over onafgeronde pagina's en aanvullende oude URL's afronden.
- [ ] Schone, reproduceerbare staginginstallatie en afgeschermde toegang valideren.
- [ ] Productiehost, HTTPS/proxy, geheimen/SMTP, limieten en logging gereedmaken.
- [ ] Back-up, vorige release en concrete rollback met verantwoordelijke vastleggen.
- [ ] Met toestemming echte mailaflevering bewijzen.
- [ ] Expliciet publicatieakkoord verkrijgen; pas dan release activeren met `WESPI_ENV=production`.
- [ ] Direct publiek routes, media, menu/formulieren/interacties, 404, canonicals/OG, redirects en robots/sitemap controleren.
- [ ] Na akkoord sitemap indienen en fouten/404's volgen.

## GEREED

Veilige lokale SEO- en technische verbeteringen, sitemap/robots, foutpagina's, toegankelijkheidsverbeteringen en alle genoemde lokale regressies. Vormgeving, tarieven, fase 1–3 en de rechtopstaande vlag zijn behouden.

## NOG TE CONTROLEREN

Fysieke browsers/screenreaders, productie-installatie en proxygedrag, echte deelvoorbeelden, zoekmachineverwerking en praktijkprestaties.

## BLOKKEREND VOOR LIVEGANG

Eigenaarbesluit over onafgeronde pagina's en aanvullende migratie; gevalideerde productie-/SMTP-inrichting; beschikbare back-up en rollback; expliciet publicatieakkoord. Deze punten blokkeren publicatie, niet de afgeronde lokale fase-4-uitvoering. Er is niets gepubliceerd.
