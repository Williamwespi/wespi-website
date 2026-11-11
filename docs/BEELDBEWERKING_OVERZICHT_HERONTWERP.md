# Hoofdpagina Beeldbewerking — lokaal herontwerp

Uitgevoerd op 11 november 2026, op expliciete opdracht. Lokaal te beoordelen op http://127.0.0.1:8765/beeldbewerking. Niet gecommit, gepusht of gedeployd.

## Opbouw en visuele keuzes

1. De goedgekeurde hero blijft ongewijzigd, inclusief de twee bestaande CTA's en `#mogelijkheden` als bestemming.
2. Een korte introductie met drie genummerde ankerlinks geeft direct toegang tot de diensten. Deze vervangt de oude rij dienstkaarten.
3. **Autobewerking:** een groot showroombeeld links dat horizontaal naar de tekst rechts uitloopt. Kop, korte beschrijving, drie kenmerken en directe link naar `/beeldbewerking/automotive`.
4. **Kledingbeeldbewerking:** tekst links, twee vrijstaande kledingbeelden op verschillende schaal rechts, met een zachte asymmetrische goudvorm achter de beelden. De oorspronkelijke witte beeldachtergronden worden via CSS multiply in het vlak opgenomen; de bestanden zelf blijven intact. Directe link naar `/beeldbewerking/kleding`.
5. **Productbeeldbewerking:** brede presentatie met het goedgekeurde productsfeerbeeld rechts, tekst links en uitsluitend een horizontale overgang richting de tekst. Directe link naar `/beeldbewerking/product`.
6. **Volume en werkwijze:** één compacte afsluiting met de bestaande boodschap over duizenden beelden per maand, drie stappen en een link naar de bestaande offertepagina. Geen nieuwe prijs-, planning- of leveringsclaims.
7. De bestaande gedeelde ‘Samen aan de slag’-sectie en footer verzorgen de afsluiting.

Het oude vergelijkingsonderdeel met de auto is niet meer opgenomen. De oude deeltemplates, stijlen en bronmedia blijven bewaard. Op deze pagina is het vergelijkingsscript niet meer nodig en daarom niet meer geladen. De losse dienstenpagina's blijven hun vergelijkingen gebruiken.

Onder 900px staat per dienst eerst de tekst met doorklikmogelijkheid en daarna de afbeelding. Beelden behouden hun volledige verhouding op mobiel. Onder 600px staan de drie keuzelinks en de processtappen onder elkaar.

## Referenties en beeldmateriaal

Home, Kledingfotografie, Kledingbeeldbewerking, Automotive en de goedgekeurde Productbeeldbewerkingpagina zijn in broncode en browser bekeken. Het ontwerp sluit aan op hun grote zwart/gouden koppen, lichte achtergronden, open beeld-tekstcomposities, vrijstaande productbeelden en zachte beeldverlopen.

Alle media zijn bestaande WebP's, met bestaande responsieve varianten waar beschikbaar:

- `static/images/beeldbewerking/beeldbewerking/automotive/achtergronden/auto-geel-extra-achtergrond-3-{600,1200}.webp`.
- `static/images/beeldbewerking/beeldbewerking/kleding/tshirt-blauw-voorzijde-{600,1200}.webp`.
- `static/images/beeldbewerking/kleding/kledingbeeldbewerking-werkwijze-600.webp`.
- `static/images/beeldbewerking/product/productbeeldbewerking-sfeerbeeld-{640,960,1752}.webp`.

Er zijn geen nieuwe visuals nodig en geen placeholders toegevoegd. De sfeercompositie wordt als sfeerbeeld gepresenteerd, niet als authentiek voor-en-na-resultaat.

## Controle

- **42 bestaande regressietests geslaagd:** `python -B -m unittest discover -s tests -v`. Inclusief routes, SEO, statische bestanden, bestaande mediahashes, productvergelijkingen en gesimuleerde formulierverzending. Geen echte mail verstuurd.
- **Chrome/Playwright op 375, 430, 768 en 1440px:** volledige pagina en afzonderlijke diensten visueel beoordeeld, ook naast de referentiepagina's. Responsieve beelden gedecodeerd; geen console-, JavaScript-, HTTP- of mediafouten op de gewijzigde pagina.
- Alle interne links van de volledige pagina, inclusief header/footer en fragmentbestemmingen, gecontroleerd. Diensten, ankers, hero-CTA en offertebestemming werken. Focusmarkering met toetsenbord gecontroleerd. Inhoud en vier doorkliklinks blijven zonder JavaScript beschikbaar.
- Mobiel tekst vóór beeld in alle drie de diensten. Geen horizontale overflow of buiten de viewport uitstekende tekst/afbeeldingen binnen de nieuwe inhoud. De hero is expliciet ongewijzigd gebleven, ook waar de bestaande mobiele H1 aan de rand komt.
- Hero-HTML vergeleken met opnames vóór het herontwerp. Alle berekende stijleigenschappen en geometrie van de hero en zijn nakomelingen zijn identiek met en zonder de nieuwe CSS. Afzonderlijke hero-pixelvergelijkingen met en zonder die CSS zijn op alle vier de breedtes identiek.
- Bestandsvingerafdrukken vóór/na bevestigen dat van de reeds bestaande applicatiebestanden in templates, CSS, JavaScript en routes uitsluitend `templates/beeldbewerking.html` is gewijzigd. De nieuwe stylesheet staat apart en wordt uitsluitend via de extra-head van deze template geladen. Geen gedeelde componenten of andere pagina's gewijzigd.
- De controle gebruikt de bestaande lokale server en Chrome, met Python 3.13 en tijdelijke testdependencies buiten de projectmap. Projectomgeving en requirements zijn niet gewijzigd. Browseremulatie, geen fysieke toesteltest.

## Bestanden

Gewijzigd:

- `templates/beeldbewerking.html` — bestaande hero-include en SEO-blokken behouden, onderliggende pagina opnieuw opgebouwd.
- `docs/BESLUITEN.md` — deze expliciete ontwerpbeslissing vastgelegd.

Toegevoegd:

- `static/css/beeldbewerking/overzicht.css` — uitsluitend selectors voor het nieuwe overzicht onder de hero.
- `docs/BEELDBEWERKING_OVERZICHT_HERONTWERP.md` — dit uitvoeringsverslag.
- Twintig screenshots: `docs/beeldbewerking-{overzicht,diensten,auto,kleding,product}-{375,430,768,1440}.png`.

Geen afbeeldingen, bronbestanden, gedeelde stijlen, bestaande tests, navigatie, footer, routes of SEO-configuratie gewijzigd.
