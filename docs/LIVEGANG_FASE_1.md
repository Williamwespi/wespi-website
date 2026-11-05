# Wespi — livegang fase 1

Datum: 5 november 2026. Technische uitvoering van de expliciet goedgekeurde fase 1, naar aanleiding van [WEBSITE_AUDIT.md](./WEBSITE_AUDIT.md). Dit verslag vervangt geen productie- of livegangakkoord. Het auditrapport blijft de oorspronkelijke momentopname.

## Formulieren

- `/offerte` heeft nu een POST-handler. Alle acht bestaande velden, labels en de vijf bestaande dienstkeuzes blijven behouden; `?dienst=...` blijft de dienst vooraf selecteren. Ontvanger is vast `info@wespi.nl`, onderwerp is `Nieuwe offerteaanvraag via Wespi`.
- Offerte en Contact delen de bestaande SMTP-configuratie en één transportfunctie. STARTTLS controleert nu ook het servercertificaat en de hostnaam. SMTP loopt in de FastAPI-threadpool, zodat de netwerkverbinding de async eventloop niet blokkeert.
- Het bezoekersadres staat in Reply-To; From komt uit `SMTP_FROM`. Er worden geen gebruikersgegevens als SMTP-inloggegevens gebruikt.
- Servervalidatie controleert verplichte velden, lengtes, e-mailadres, controletekens en bij offertes de aangeboden selectiekeuzes. Beide formulieren hebben een honeypot. De bestaande contacttoestemming blijft behouden, ook na een verzendfout.
- Succes geeft een bevestiging na acceptatie door de SMTP-server. Ontbrekende configuratie, SMTP/TLS/loginproblemen en geweigerde ontvangers geven een nette foutmelding met behoud van geldige invoer en selecties. Dat SMTP een bericht accepteert bewijst nog geen aflevering in de inbox.
- Er is geen echte e-mail verstuurd. Geen externe dependency toegevoegd.

## Links en footer

- Footer: `/#praktijk` en `/over-wespi` verwijzen naar bestaande bestemmingen. De niet-werkende placeholders Werkwijze, Kennis en Mijn Wespi zijn verwijderd. `/contact` is toegevoegd als duidelijke contactlink. Bestaande footeropmaak en contact-CTA zijn behouden.
- Kledingfotografie: uitsluitend `id="bodyform"` toegevoegd aan de bestaande bodyformsectie. Hero en de knop zelf zijn ongewijzigd.
- Privacyverklaring: twee postcodevermeldingen naar **7122 LC** en vier onjuiste HTTPS-e-maillinks naar `mailto:`. Overige juridische tekst is niet gewijzigd.

## Bevestigde redirects

| Oude route | Nieuwe bestemming | Lokaal getest |
|---|---|---|
| `/beeldbewerking/auto` | `/beeldbewerking/automotive` | 301 → 200 |
| `/terms` | `/algemene-voorwaarden` | 301 → 200 |
| `/privacystatement` | `/privacyverklaring` | 301 → 200 |

De nieuwe URL's en canonicals blijven behouden. De redirects staan in de FastAPI-router. Controleer na plaatsing achter de productieproxy dezelfde HTTP-statussen, zonder redirectketens. Eventuele host-, HTTPS- en trailing-slashredirects van de hosting zijn lokaal niet bewezen.

## Andere oude URL's: eerst controleren, geen redirects toegevoegd

Onderstaande URL's zijn aangetroffen in zoekresultaten van de bestaande Wespi-website op 5 november 2026. De huidige online sitemap kon bij deze controle niet worden opgehaald. Deze lijst is daarom geen volledige oude URL-inventaris; status, verkeer en definitieve bestemming moeten vóór livegang nog worden beoordeeld.

| Aangetroffen oude URL / bron | Te beoordelen aansluiting | Actie vóór livegang |
|---|---|---|
| [Over ons — `/overons`](https://www.wespi.nl/overons) | Huidige `/over-wespi` | Inhoud vergelijken en bestemming laten bevestigen. |
| [Contact — `/contactus`](https://www.wespi.nl/contactus) | Huidige `/contact` | Bestaande inkomende links en definitieve migratie bevestigen. |
| [Diensten — `/diensten`](https://www.wespi.nl/diensten) | Oude overzichtspagina bevat een ander aanbod dan de vernieuwde site | Geen automatische redirect naar Beeld: Data en andere oude onderwerpen eerst beoordelen. |

Daarnaast staan [Kledingfotografie](https://www.wespi.nl/productfotografie/kledingfotografie), [Packshotfotografie](https://www.wespi.nl/productfotografie/packshotfotografie) en [Beeldbewerking](https://www.wespi.nl/beeldbewerking) online onder dezelfde paden als lokaal. Deze routes lokaal gecontroleerd op HTTP 200; ook externe links en eventuele subroutes moeten nog tegen een volledige export uit de oude website, Search Console of toegangslogs worden gehouden. Geen onbevestigde oude paden of extra redirects verzonnen.

## Productie-instellingen SMTP

Stel deze variabelen in de omgeving van het daadwerkelijke websiteproces in, buiten de broncode:

| Variabele | Instelling |
|---|---|
| `SMTP_HOST` | SMTP-server van de mailprovider; verplicht. |
| `SMTP_PORT` | STARTTLS-poort van de provider; standaard `587`. |
| `SMTP_FROM` | Vast, door de provider toegestaan afzenderadres; verplicht. Gebruik een passend Wespi-adres. |
| `SMTP_USERNAME` | SMTP-gebruikersnaam indien authenticatie nodig is. |
| `SMTP_PASSWORD` | Bijbehorend geheim; uitsluitend in de serveromgeving/secretopslag. |

Gebruikersnaam en wachtwoord moeten samen ingesteld of samen leeg zijn. Het transport gebruikt STARTTLS, geen impliciete TLS op poort 465. Er is geen automatische `.env`-lader toegevoegd: alleen een `.env` neerzetten stelt deze variabelen niet in. Herstart het proces na configuratie. De server moet uitgaand de SMTP-host/poort kunnen bereiken en een geldige certificaatvertrouwensketen hebben. Controleer bij de mailprovider de toegestane afzender en SPF/DKIM/DMARC-inrichting.

Nog nodig: met toestemming één echte offerte en één contactbericht versturen, ontvangst in `info@wespi.nl` controleren, spammap controleren en vanuit de ontvangen berichten antwoorden naar het bezoekersadres. Doe dit in de beoogde productieomgeving. Een geslaagde simulatie is geen bewijs van echte aflevering.

## Verificatie

- `py -3.12 -B -m unittest discover -s tests -v`: **15 tests geslaagd**, inclusief meerdere subcases.
- Formulieren: alle velden in de mailbody, ontvanger/afzender/Reply-To, STARTTLS, verplichte velden, ongeldige e-mail, te lange invoer, headerinjectie, onbekende keuzes, honeypot en HTML-escaping gecontroleerd. Geen echte SMTP-verbinding: de SMTP-client wordt in alle tests onderschept.
- Verzending: succes, ontbrekende/ongeldige SMTP-instellingen, netwerk-/SMTP-fouten, TLS/loginfout en geweigerde ontvanger gesimuleerd. Bij fouten blijven de velden, offertekeuzes en contacttoestemming behouden.
- Alle 16 bestaande GET-pagina's geven HTTP 200. Footer- en bestaande headerlinks verwijzen naar bestaande routes/fragmenten. De drie oude routes geven 301 en hun bestemming 200. Bodyformdoel en privacy-e-maillinks gecontroleerd.
- Chromium: footer op alle 16 pagina's bij 1440, 768, 430 en 375px gecontroleerd (64 combinaties). Geen footerlinks buiten beeld; screenshots van desktop en mobiel visueel beoordeeld. Offertevelden passen en dienstselectie blijft staan. Mobiel menu opent en sluit met Escape. Footer-CSS, hoofdnavigatie en hero's zijn niet aangepast.
- Acht daadwerkelijke browserinzendingen via een tijdelijke lokale server met onderschepte SMTP: Offerte en Contact, elk succes en verzendfout, op 1440 en 375px. Bevestigingen/foutmeldingen verschijnen; bij fouten blijven e-mailadres, dienst, fotografietype en contacttoestemming waar van toepassing behouden. Screenshots van de formulierstatussen gecontroleerd. Deze testserver en scripts staan buiten de projectbroncode.
- Browserresultaten en screenshots staan tijdelijk buiten de projectbroncode in `%TEMP%/wespi-fase1-controle/`. Geen volledige test op alle browsers/toestellen of productiehosting.

## Gewijzigde bestanden

- `routes/paginas.py`
- `templates/oferte.html`
- `static/css/offerte.css` — alleen formuliermeldingen, foutstatus en onzichtbare spamval.
- `templates/onderdelen/footer.html`
- `templates/onderdelen/kledingfotografie/bodyform.html`
- `templates/privacyverklaring.html`
- `tests/test_livegang_fase1.py` — nieuw.
- `docs/BESLUITEN.md`
- `docs/PROJECTKOMPAS.md` — statusverwijzing ter aanvulling op de oorspronkelijke inventarisatie.
- `docs/LIVEGANG_FASE_1.md` — dit nieuwe verslag.

Andere ontwerpen, prijzen, diensten en de hoofdnavigatie zijn niet gewijzigd. Niets gecommit of gepusht. Fase 2 wacht op akkoord.
