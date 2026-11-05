# URL-migratie bij livegang

5 november 2026. Dit overzicht is een publicatiehulpmiddel, geen toestemming voor publicatie. Er zijn in fase 4 geen nieuwe redirects toegevoegd.

## Bevestigd en lokaal getest

| Oude route | Bestemming | Status |
|---|---|---|
| `/beeldbewerking/auto` | `/beeldbewerking/automotive` | Eén 301, bestemming 200 |
| `/terms` | `/algemene-voorwaarden` | Eén 301, bestemming 200 |
| `/privacystatement` | `/privacyverklaring` | Eén 301, bestemming 200 |

De redirects staan in `routes/paginas.py`. Canonicals van de bestemmingen gebruiken `https://www.wespi.nl` en de nieuwe route. Bestaande nieuwe URL's blijven behouden. De sitemap bevat uitsluitend afgeronde canonieke pagina's.

## Eerst bevestigen

Deze oude routes zijn al in fase 1 aangetroffen; dit is geen nieuwe live-inventarisatie. Er zijn geen nieuwe bestemmingen aangenomen.

| Oude route | Mogelijke aansluiting, nog geen redirectbesluit | Nodige controle |
|---|---|---|
| `/overons` | `/over-wespi` | Inhoud, inkomende links en bestemming bevestigen |
| `/contactus` | `/contact` | Oude contactroute en migratie bevestigen |
| `/diensten` | Nog onbeslist | Oude aanbod vergelijken; niet automatisch naar Beeld omleiden |

Bron: [fase 1](./LIVEGANG_FASE_1.md). Voor een volledige inventaris zijn een export van de oude website, toegangslogs en/of Search Console nodig. Verkeersgegevens zijn niet beschikbaar in deze lokale projectmap.

## Route- en indexeringsonderscheid

| Route | Technische status | Navigatie | Sitemap / indexering |
|---|---|---|---|
| `/beeldbewerking` | 200, ongewijzigd | Bestaande link behouden | Niet in sitemap; huidige productie-indexeerbaarheid ongewijzigd. Besluit vóór livegang nodig |
| `/beeldbewerking/product` | 404; geen bestaande pagina | Productbeeldbewerking blijft inactief | Niet in sitemap. Geen pagina of redirect verzonnen |
| `/slimmer-werken-v2` | 200, bestaande testpagina | Niet toegevoegd | Niet in sitemap; bestaand `noindex, nofollow` behouden |

Uitsluiting uit de sitemap voorkomt op zichzelf geen indexering. Fase 4 neemt geen besluit om onafgeronde pagina's te verbergen, publiceren of verwijderen.

## Controles bij de daadwerkelijke omschakeling

- [ ] Volledige lijst oude URL's exporteren en laten beoordelen; alleen bevestigde koppelingen uitvoeren.
- [ ] De drie bevestigde redirects testen op de publieke host: exact 301 en de juiste locatie, zonder onverwachte keten of lus.
- [ ] Nieuwe bestemmingen, canonicals en alle sitemap-URL's op HTTP 200 controleren.
- [ ] Hostingredirects voor HTTP → HTTPS en niet-www → www controleren. De app forceert deze nog niet; voorkom dubbel ingestelde regels.
- [ ] Trailing slashes en eventuele oude queryparameters controleren tegen echte oude links; er zijn geen extra migratieregels voor verzonnen.
- [ ] Bestaande media en externe inkomende medialinks uit de oude site inventariseren. Originele lokale bestanden zijn behouden; de structuur van de oude hosting is niet bewezen gelijk.
- [ ] Sitemap indienen en de belangrijkste URL's in Search Console controleren na akkoord en publicatie.
- [ ] Na publicatie 404's en redirectverkeer volgen, zonder formulierinhoud of URL-querygegevens met persoonsgegevens op te slaan.

Rollback van routes en bestanden gebeurt samen met de vorige release; zie [deployment en rollback](./LIVEGANG_DEPLOYMENT.md).
