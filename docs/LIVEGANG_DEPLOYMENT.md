# Publicatie- en rollbackchecklist

5 november 2026. **Niets is gedeployd.** Onderstaande stappen worden pas uitgevoerd na expliciet publicatieakkoord.

## Voorbereiding

- [ ] Besluiten over de onafgeronde Beeldbewerking- en Productbeeldbewerking-pagina's vastleggen: technische beschikbaarheid, navigatie en indexering afzonderlijk beoordelen.
- [ ] [Migratieoverzicht](./LIVEGANG_MIGRATIE.md) controleren en ontbrekende oude routes bevestigen.
- [ ] Back-up maken van de huidige livebestanden, hosting-/proxyconfiguratie, redirects en benodigde omgevingsinstellingen. Geheimen alleen beveiligd bewaren. Leg herstelcommando en verantwoordelijke vast.
- [ ] Oude website, eventuele database, uploads en door de oude website gebruikte diensten inventariseren. Niet aannemen dat de nieuwe FastAPI-app alle oude backendfuncties vervangt.
- [ ] Nieuwe release in een aparte map installeren; vorige werkende versie beschikbaar houden. Geen bestaande livebestanden overschrijven voordat terugschakelen aantoonbaar kan.
- [ ] Alleen applicatiecode, `templates/`, `static/` en dependencies overbrengen. Geen lokale `.venv`, `.git`, caches, testartefacten, attachments of lokale geheimen publiceren. De bestaande getrackte `.venv` is niet opgeschoond in deze fase.
- [ ] Alle 179 WebP-varianten uit fase 3, de originele zoombronnen en het afbeeldingenregister meenemen. De drie vlag-WebP's moeten de reeds herstelde rechtopstaande versies zijn.

## Runtime en dependencies

Lokaal getest met Python 3.12 en onderstaande geïnstalleerde versies. Geen dependency toegevoegd of bijgewerkt in fase 4.

| Pakket | Geteste versie |
|---|---|
| FastAPI | 0.141.1 |
| Starlette | 1.6.0 |
| Uvicorn | 0.52.4 |
| Jinja2 | 3.1.6 |
| python-multipart | 0.0.32 |

`requirements.txt` bestaat en is nog niet vastgepind. Voor deployment een geïsoleerde omgeving maken, een beoordeelde set directe én transitieve versies vastleggen en die exacte installatie in staging opnieuw testen. De meegeleverde lokale virtuele omgeving niet hergebruiken. Een volledige dependency-/kwetsbaarhedenscan is niet uitgevoerd.

Installatie vanuit de projectroot, in de gekozen virtuele omgeving:

```text
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Voorbeeldstart achter een **lokale** reverse proxy op dezelfde machine:

```text
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --workers 2 --proxy-headers --forwarded-allow-ips 127.0.0.1
```

Geen `--reload`; debug en publieke API-documentatie staan uit. De projectroot moet de werkdirectory zijn vanwege de relatieve template-/staticpaden. Bij containers of een proxy op een andere host de bindinterface en vertrouwde proxy-IP's expliciet aanpassen; niet blind alle forwarded headers vertrouwen. Procesbeheer, automatische herstart en aantal workers afstemmen op de hosting.

## Omgevingsvariabelen

| Variabele | Gebruik |
|---|---|
| `WESPI_ENV` | `development` (standaard), `staging` of `production`. Andere waarden weigeren de start. Alleen na akkoord `production` instellen |
| `SMTP_HOST` | Mailserver van de provider; verplicht voor verzenden |
| `SMTP_PORT` | STARTTLS-poort; standaard 587 |
| `SMTP_FROM` | Vast toegestaan afzenderadres; verplicht |
| `SMTP_USERNAME` | Providergebruiker indien authenticatie nodig is |
| `SMTP_PASSWORD` | Bijbehorend geheim; samen met gebruikersnaam ingesteld of beide leeg |

De variabelen moeten beschikbaar zijn in het daadwerkelijke serverproces. Alleen een `.env` neerzetten is onvoldoende: de app laadt die niet automatisch. Geheimen horen buiten broncode en publieke mappen. Na wijzigingen het proces herstarten.

- `development` en `staging`: `robots.txt` blokkeert crawlen; antwoorden hebben `X-Robots-Tag: noindex, nofollow`.
- `production`: robots laat crawlen toe en verwijst naar `https://www.wespi.nl/sitemap.xml`; de algemene noindex-header vervalt. Het bestaande V2-noindex blijft.
- Canonicals en deel-URL's blijven het bevestigde `https://www.wespi.nl` gebruiken; staging verandert deze niet.

**Staging vóór externe toegang achter authenticatie of een netwerkbeperking plaatsen.** Robots/noindex zijn geen toegangsbeveiliging of garantie dat een publiek bekende URL nooit als URL in zoekresultaten verschijnt. Test met een geautoriseerde browser; controleer vóór publicatie dat productie niet per ongeluk de staging-noindex krijgt.

## Hosting en mail

- [ ] Domein en geldig TLS-certificaat voor www en eventuele niet-www-host controleren. HTTP/HTTPS- en hostredirects samen testen, zonder lussen.
- [ ] Alleen de vertrouwde proxy aan de applicatiepoort koppelen. Publieke hostnamen en forwarded headers aan de proxy begrenzen.
- [ ] Securityheaders verifiëren, inclusief door proxy gegenereerde foutantwoorden. HSTS pas na bevestigde HTTPS-inrichting beoordelen; CSP eerst tegen aanwezige inline-styling/scripts testen. Beide zijn voorstellen, niet blind toegevoegd.
- [ ] App-Gzip voor gewone GET-pagina's controleren; geen dubbele compressie. Beelden/video en Contact/Offerte worden niet door app-Gzip gecomprimeerd. Eventuele CSS/JS-compressie op de proxy apart configureren.
- [ ] Cachebeleid controleren: HTML herbevestigen, formulieren/fouten `no-store`, bestaande statische bestanden maximaal één uur en ETag/Last-Modified. Bij aangepaste assets cache wissen of versieparameters wijzigen.
- [ ] Proxyverzoeklimieten en time-outs instellen; een formulierbodylimiet van bijvoorbeeld 64 KiB eerst tegen normale aanvragen testen. Rate limiting voor beide POST-routes beoordelen met verwachte aantallen en gedeelde bedrijfsnetwerken. Er is geen IP-limiter/CAPTCHA of externe dienst toegevoegd.
- [ ] Logs niet onnodig formulierinhoud, queryparameters, SMTP-reacties of geheimen laten bewaren; bewaartermijn en toegang vastleggen.
- [ ] SMTP-host bereikbaar, STARTTLS-certificaat geldig en afzender toegestaan. SPF/DKIM/DMARC bij de provider controleren.
- [ ] Met afzonderlijke toestemming één echte Contact- en Offerteaanvraag versturen, ontvangst/spammap in `info@wespi.nl` en Reply-To controleren. Lokale tests simuleren alleen SMTP en bewijzen geen aflevering.

## Omschakelen en direct controleren

- [ ] Publicatieakkoord en geplande omschakeling vastleggen; back-up en rollback beschikbaar.
- [ ] Exact geteste release activeren en `WESPI_ENV=production` controleren.
- [ ] Home, alle 14 sitemapbestemmingen, media, stylesheets en JavaScript controleren op de publieke HTTPS-host.
- [ ] Robots zonder algemene blokkade/noindex; sitemap XML correct. V2 blijft uitgesloten; besluit over onafgeronde pagina's correct verwerkt.
- [ ] Drie bevestigde oude routes: 301 naar juiste bestemming, eindstatus 200. Host/HTTPS-redirects afzonderlijk controleren.
- [ ] Eigen 404 geeft werkelijk 404; API-fouten blijven JSON en geven geen 200.
- [ ] Navigatie, mobiel menu, AI-link, sliders, fotovergrotingen, video en formulieren controleren op desktop en mobiel.
- [ ] Over Wespi: vlag rechtop, juiste hero-uitsnede; hero's en tarieven onveranderd.
- [ ] Canonicals, OG-beeld-URL's en echte sociale deelvoorbeelden controleren. Search Console/sitemap pas na akkoord indienen.
- [ ] Publieke /docs, /redoc en /openapi.json geven geen API-documentatie.
- [ ] Reële console-/serverfouten en foutpercentages beoordelen; geen formuliergegevens in normale logging.

## Rollback

1. Bij wezenlijke storingen de omschakeling stoppen en het verkeer/de releaseverwijzing terugzetten naar de vastgelegde vorige versie.
2. Bijbehorende proxy-/redirectconfiguratie en procesomgeving herstellen; templates, media en code als één versie terugzetten.
3. Processen herstarten en relevante caches verversen. DNS alleen terugzetten als het bij de gekozen omschakeling gewijzigd is; rekening houden met de vastgelegde TTL.
4. Oude homepage, belangrijke routes en bestaande contactafhandeling controleren. Tijdens de overgang ontvangen e-mails en eventuele andere bedrijfsdata bewaren; geen formulieraanvragen wissen.
5. Tijdstip, oorzaak en controles vastleggen; pas na herstel en nieuw akkoord opnieuw publiceren.

Een daadwerkelijke rollback is lokaal niet uitgevoerd: de oude liveomgeving en haar hostingconfiguratie zijn niet beschikbaar in dit project.
