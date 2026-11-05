# Besluiten

## Livegang fase 4 - 5 november 2026

- De expliciet goedgekeurde fase 4 voegt uitsluitend afgebakende SEO-, veiligheids- en toegankelijkheidsverbeteringen toe, met behoud van fase 1–3 en het herstelde vlagbeeld.
- De sitemap bevat alleen de 14 afgeronde publieke pagina's. Slimmer werken V2 blijft noindex en buiten de sitemap; onafgeronde pagina's krijgen geen zelfstandige publicatie-, navigatie- of indexeringsbeslissing.
- Publicatieomgeving is expliciet: `WESPI_ENV=production`; development/staging krijgen crawlblokkade en noindex-header. Staging heeft daarnaast toegangsbeveiliging op hostingniveau nodig.
- Drie bestaande redirects blijven behouden; aanvullende oude URL's vereisen bevestiging. Native kleding-/packshotdialogen verbeteren toetsenbordbediening zonder galerijherbouw.
- Geen livewijziging of echte mailtest uitgevoerd. Publicatie vereist apart akkoord en de productievoorwaarden uit [LIVEGANG_FASE_4.md](./LIVEGANG_FASE_4.md), [migratie](./LIVEGANG_MIGRATIE.md) en [deployment](./LIVEGANG_DEPLOYMENT.md).

## Livegang fase 3 - 5 november 2026

- De eigenaar bevestigt dat alle bestaande bedragen voor Kledingfotografie, Packshotfotografie, losse Productdata en Slimmer werken exclusief btw zijn. Alleen de btw-vermelding is toegevoegd; bedragen en eenheden blijven gelijk.
- Geoptimaliseerde bestaande beelden gebruiken proportionele WebP-varianten; detailvergrotingen behouden voldoende resolutie en waar nodig de oorspronkelijke bron. Originele bestanden blijven behouden.
- Huisstijlgoud blijft behouden voor accenten en vlakken; onvoldoende contrasterende informatieve tekst krijgt lokaal een donkere variant. Mobiele compactheid wordt uitsluitend gericht verbeterd.
- Dubbele algemene contactuitnodigingen vervallen alleen bij een duidelijke bestaande contactmogelijkheid. Fase 1 en 2 blijven behouden; fase 4 vereist akkoord. Zie [LIVEGANG_FASE_3.md](./LIVEGANG_FASE_3.md).

## Livegang fase 2 — 5 november 2026

- Op expliciet verzoek staat AI-modelfotografie als zelfstandige link direct onder Kledingfotografie binnen de bestaande groep Productfotografie. Geen extra hoverlaag. Beeldbewerking toont Autobeeldbewerking, Kledingbeeldbewerking en de bestaande inactieve Productbeeldbewerking.
- De desktop-dropdown is links onder Beeld uitgelijnd en gebruikt één open/dicht-status voor hover, klik, aanraking en toetsenbord. Escape sluit ook bij hover; focus keert waar passend terug naar de trigger.
- De mobiele afwijkingen uit audit B1 zijn gericht hersteld: titel → bestaand beeld → overige inhoud. Dit actualiseert uitsluitend de mobiele volgorde uit eerdere beeldplaatsingsbesluiten. Desktopindelingen, hero's, inhoud, beelden en prijzen blijven behouden. De bestaande omslagpunten voor gestapelde weergave blijven leidend.
- Fase 1 blijft behouden. Er is geen algemene optimalisatie van sectiehoogtes, witruimte of huisstijl uitgevoerd. Zie [LIVEGANG_FASE_2.md](./LIVEGANG_FASE_2.md). Fase 3 begint pas na akkoord.

## Livegang fase 1 — 5 november 2026

- Offerteaanvragen worden server-side verwerkt via dezelfde SMTP-configuratie en transportlogica als Contact, naar `info@wespi.nl`. Alle bestaande offertevelden en dienstselectie via de URL blijven behouden. Het bezoekersadres wordt uitsluitend Reply-To; de afzender komt uit de serveromgeving. Verzending is uitsluitend gesimuleerd getest; een echte testmail vereist toestemming.
- De eigenaar heeft postcode **7122 LC** bevestigd. In de privacyverklaring zijn alleen de postcode en onjuiste e-maillinks hersteld; overige juridische inhoud blijft ongewijzigd.
- Drie bevestigde oude URL's krijgen een 301: `/beeldbewerking/auto` → `/beeldbewerking/automotive`, `/terms` → `/algemene-voorwaarden`, `/privacystatement` → `/privacyverklaring`. Andere mogelijke oude URL's worden eerst beoordeeld; zie [LIVEGANG_FASE_1.md](./LIVEGANG_FASE_1.md).
- Footerplaceholders zonder bestaande bestemming zijn verwijderd, Over Wespi en de praktijksectie krijgen bestaande bestemmingen en de footer krijgt een expliciete contactlink. Geen wijziging aan de hoofdnavigatie. Fase 2 begint pas na akkoord.

## Autobeeldbewerking — 5 november 2026

- Grote volumes gebruikt na vergelijking met de overige Wespi-pagina's een egale lichtgrijze sectieachtergrond (`#e9eaec`, zoals Projecten op de homepage). Dit vervangt het wit-gele verloop. De bestaande gele bestelbus staat links, tekst en gouden contactknop rechts binnen de gebruikelijke 1180px-container; mobiel staan ze onder elkaar. Geen binnenkaart, kader of schaduw. Kop, tekst, voordelen en contactroute zijn behouden. De gebruiker heeft bevestigd dat de bestaande gele bestelbus correct is en de eerdere bestandsnaam een typefout was.
- Vervolgopdracht: de reguliere online tarieven worden nu wel getoond, zonder Premium of andere abonnementsvormen. De gebruiker heeft expliciet bevestigd dat de bedragen exclusief btw zijn. Dit vervangt de eerdere keuze hieronder om uitsluitend prijzen op aanvraag te tonen.
- Gepubliceerde reguliere tarieven: één foto € 2,49; 5 foto's € 6,99; 10 foto's € 9,99; 15 foto's € 12,99; 20 foto's € 14,99 (staffels als totaalbedragen). Aanvullingen: gepersonaliseerde nummerplaat +€ 0,99 per foto, logo +€ 4,99 per auto, persoonlijke achtergrond € 75,00 eenmalig. Bron: `https://www.wespi.nl/beeldbewerking/auto`, gecontroleerd op 5 november 2026. De btw-basis wordt ook ondersteund door artikel 14 van `https://www.wespi.nl/terms`.
- De losse online claim ‘vanaf € 0,60’ is niet overgenomen: de voorwaarden daarvoor volgen niet uit de reguliere prijstabel. Grote volumes en terugkerende opdrachten blijven op offerte.
- Bij de laatste visuele verfijning is expliciet gekozen voor dezelfde gele Peugeot in alle zes achtergrondvoorbeelden: wit, moderne showroom, lichte studio, industrieel, lichte parkeergarage en eigen huisstijl. Alleen korte achtergrondnamen staan onder de beelden. Dit vervangt de eerdere keuze voor verschillende voertuigen binnen dit overzicht.
- De zwarte SUV (`auto-voorbeeld-showroom.jpg`) staat groot naast de zes compacte mogelijkheden. Werkwijze bevat uitsluitend introductie en stappen. Op het laatste verzoek is de brede KroezEN-foto (`auto-achtergrond-gepersonaliseerde-showroom.jpg`, 1536 × 1024) van Grote volumes naar het kaartje Eigen huisstijl verplaatst. Grote volumes gebruikt nu de volledig zichtbare vrijstaande bedrijfswagen (`auto-voorbeeld-vrijstaand.jpg`); een bestand met de opgegeven naam `auto-voorbeeld0-vrijstaand` is niet aangetroffen. Teksten en indeling zijn behouden, evenals de hero, de overige achtergrondvoorbeelden, tarieven en voor-en-na-slider.

### Eerste opbouw

- De dienstenpagina is op expliciet verzoek opnieuw opgebouwd op de bestaande lokale route `/beeldbewerking/automotive`. Header, footer, navigatie en andere pagina's blijven behouden.
- De bestaande online pagina `https://www.wespi.nl/beeldbewerking/auto` vormt de inhoudelijke bron voor achtergrondbewerking, digitale showrooms, huisstijlachtergronden, nummerplaatcorrectie en logo/tekst. De gebruikelijke doorlooptijd is 24 uur; bij grote aantallen of maatwerk wordt de planning vooraf afgestemd.
- De oude online prijstabel en het Premium-abonnement worden niet overgenomen. De prijsstructuur blijft te beoordelen; de lokale pagina biedt uitsluitend tarieven op aanvraag via de bestaande offertepagina.
- Alleen bestaande lokale autofoto's worden gebruikt. Het originele en bewerkte Mercedes-beeld vormen een echte voor-en-na-vergelijking met de bestaande sliderfunctionaliteit. Het slot combineert grote volumes en de offerte-uitnodiging, zonder afzonderlijk extra contactblok vóór de bestaande footer.

## Visuele samenhang Kledingfotografie — 5 november 2026

- Op expliciet verzoek is het AI-promotieblok op Kledingfotografie opnieuw vormgegeven: een compacte zachtgele sectie met gouden accenten en de bestaande AI-modelfoto volledig zichtbaar, zonder vervaging.
- De titel ‘Van productfoto naar modelbeeld’ en verwijzing naar AI-modelfotografie blijven behouden. De bestaande paginabreedte, typografie en knopstijl vormen de basis; op mobiel staan tekst en foto onder elkaar.
- Dit verzoek staat de gerichte visuele aanpassing van Kledingfotografie toe, aanvullend op het besluit van 4 november om bij de introductie van de AI-dienstpagina bestaande pagina's ongemoeid te laten.

## AI-modelfotografie — 4 november 2026

- Een zelfstandige dienstpagina onder Kledingfotografie op `/productfotografie/kledingfotografie/ai-modelfotografie`, zonder wijzigingen aan bestaande pagina's of navigatie.
- AI-modelfotografie is primair een aanvulling op kledingfotografie bij Wespi: de originele productfoto vormt de basis voor aanvullende modelbeelden, lifestylefoto's en video's. Bestaande professionele kledingfoto's aanleveren blijft een secundaire mogelijkheid. Wespi verzorgt de uitvoering en kwaliteitscontrole; dit is geen AI-zelfbediening.
- De tarieven op de AI-pagina gelden uitsluitend voor de AI-dienst. Eventuele kledingfotografie wordt afzonderlijk berekend.
- Voorlopige verkoopprijzen exclusief btw: één AI-modelfoto €9,99; drie foto's van hetzelfde kledingartikel €24,99 (op verzoek aangepast van €25,00); AI-video van circa 10 seconden €19,99; drie foto's plus één video €39,99. Centraal aanpasbaar in `routes/paginas.py`.
- Vijf beeldseries met elk één video en twee lifestylefoto's zijn voorbereid. Ontbrekende media blijven herkenbare placeholders, geen fictief portfolio.
- Geen vaste levertijd, correctierechten of commerciële gebruiksrechten toegezegd; toepassing en voorwaarden worden vooraf afgestemd.
- Laatste pagina-aanpassing: het aanvullende sfeerbeeld staat links in de bestaande tariefsectie `#ai-tarieven`, met de vier prijskaarten rechts en zachte overgangen naar de witte sectieachtergrond. De oude positie in het voorbeeldenblok is verwijderd. Het afzonderlijke afsluitende blok ‘Even overleggen?’ is op verzoek verwijderd; de bestaande footer blijft behouden.

Deze besluiten beschrijven de afgesproken richting. Ze zijn geen bewijs dat toekomstige functionaliteit al is gebouwd of beschikbaar is.

## Besluiten van 26 oktober 2026

1. Wespi presenteert zich met drie actieve hoofddiensten, primair gericht op retail en e-commerce:
   - **Beeld:** professionele productfotografie en beeldbewerking.
   - **Data:** productinformatie verwerken, structureren en verrijken als dienst.
   - **Slimmer werken:** terugkerende werkprocessen vereenvoudigen met praktische automatisering en digitale toepassingen, zodat klanten zelf efficiënter kunnen werken.
2. Wespi wil herkenbaar zijn als specialist, niet als algemeen softwarebedrijf. Het onderscheid tussen Data als gegevensverwerkingsdienst en Slimmer werken als oplossingen voor efficiënter eigen werk moet duidelijk blijven.
3. De dienst Web wordt voorlopig niet verder ontwikkeld of actief aangeboden. Dit is geen definitieve afwijzing: Web blijft als toekomstig idee bewaard. Op 26 oktober 2026 is de actieve Web-presentatie op de website verwijderd; zie de uitvoering hieronder.
4. Slimmer werken begint met kleine, afgebakende automatiseringsoplossingen. Bestaande Excel- en Access-werkwijzen kunnen aanleiding zijn voor procesverbetering.
5. Wespi positioneert zich niet actief als ontwikkelaar van allerlei maatwerksoftware.
6. Universele, herbruikbare applicaties die via abonnementen worden aangeboden blijven een mogelijke latere richting. Toekomstige producten worden pas actief aangeboden wanneer ze beschikbaar zijn.
7. De bestaande pagina **Slimmer werken** blijft behouden. Er komt een afzonderlijke pagina **Slimmer werken V2**, gebaseerd op de bestaande vormgeving en relevante inhoud. Deze pagina is nog niet gebouwd.
8. De prijsstructuur voor Slimmer werken V2 is niet definitief vastgesteld. De bestaande prijzen op de huidige pagina — € 249 en € 499 — blijven voorlopig ongewijzigd.

## Eerdere besluiten en status

De onderstaande besluiten zijn op 26 oktober 2026 aangescherpt. Eerdere besluitgeschiedenis blijft behouden; waar de formulering is vervangen, staat dat hieronder vermeld.

1. We beginnen met kleine, praktische webapplicaties en automatisering.
2. We richten ons primair op terugkerende processen in retail en e-commerce.
3. Op termijn willen we herbruikbare applicaties ontwikkelen die via abonnementen kunnen worden aangeboden.
4. De bestaande pagina **Slimmer werken** blijft behouden.
5. Er komt een afzonderlijke V2-versie van de pagina **Slimmer werken**; de bestaande pagina wordt niet stilzwijgend vervangen.
6. De website mag toekomstige diensten presenteren, maar mag niet suggereren dat deze al beschikbaar zijn als dat niet zo is.
7. Een vanafprijs van **€ 495** is besproken, maar is nog niet definitief vastgesteld. Dit bedrag is dus geen goedgekeurde prijs.

### Vervangen of nader afgebakend op 26 oktober 2026

- Het eerdere besluit om te beginnen met kleine webapplicaties en automatisering is **nader afgebakend**: begin met kleine, afgebakende automatiseringsoplossingen; positioneer Wespi niet actief als ontwikkelaar van allerlei maatwerksoftware.
- De eerdere richting rond herbruikbare abonnementsapplicaties blijft een mogelijke latere ontwikkeling, niet het huidige actieve aanbod.
- De eerdere V2-richting blijft gelden en is **nader afgebakend**: baseer V2 op de bestaande vormgeving en relevante inhoud; de V2-prijzen zijn niet definitief en de huidige bedragen blijven voorlopig staan.
- De eerdere bespreking van € 495 blijft niet vastgesteld. Voor V2 wordt geen prijs vastgelegd totdat daarover een nieuw besluit is genomen.
- De afspraak om toekomstige diensten niet als beschikbaar te presenteren is **nader afgebakend**: toekomstige producten worden pas actief aangeboden wanneer ze daadwerkelijk beschikbaar zijn.
- Voor Web is geen eerder expliciet besluit tot actieve ontwikkeling vastgelegd. De huidige positionering zet Web nu op pauze; dit vervangt geen afwijzing, want Web blijft een toekomstig idee.

## Uitvoering stap 3 — 26 oktober 2026

De actieve verwijzingen naar Web als afzonderlijke dienst zijn uit de website verwijderd: de homepage-dienstkaart, de Web-vermelding in de footer, de actieve dienstbenamingen in de paginatitels en hero en de Web-optie bij het aanvragen van een offerte. Het dienstenraster is aangepast aan de drie overgebleven dienstkaarten. De bestaande website-opmaak en overige pagina's zijn behouden. Web blijft als mogelijk toekomstig idee opgenomen in [IDEEEN.md](./IDEEEN.md); er is geen pagina of bestand verwijderd.

## Verschil met de aangetroffen website

De bestaande pagina **Slimmer werken** toont in de broncode een prijs vanaf € 249 en een tweede bedrag vanaf € 499. Dit zijn de bestaande bedragen en ze blijven voorlopig ongewijzigd. De besproken € 495 is geen vastgestelde prijs. Web wordt niet actief aangeboden en blijft een mogelijk toekomstig idee.
