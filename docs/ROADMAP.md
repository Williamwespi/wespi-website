# Roadmap

Deze roadmap maakt onderscheid tussen aangetroffen functionaliteit, de huidige ontwikkelfase en ideeën voor later. De ideeën zijn niet automatisch goedgekeurd of ingepland.

## 1. Bestaand — aangetroffen in de projectcode

- FastAPI-applicatie met Jinja2-templates en statische CSS-, JavaScript- en afbeeldingsbestanden.
- Pagina's: Home, Beeld, Kledingfotografie, Packshotfotografie, Beeldbewerking, Productdata, Slimmer werken, Offerte aanvragen en Over Wespi.
- Bestaande pagina **Slimmer werken** met voorbeelden van digitale werkzaamheden en prijskaarten.
- Gedeelde navigatie, footer, contact-CTA en routes voor de bestaande pagina's.

De broncode is geïnventariseerd; runtime- en browsergedrag is **niet getest**. Zie [PROJECTKOMPAS.md](./PROJECTKOMPAS.md) voor de structuur, navigatie en aandachtspunten.

## 2. Huidige ontwikkelfase — voorbereiding Slimmer werken V2

Besluiten van 26 oktober 2026:

- De bestaande pagina **Slimmer werken** behouden.
- Een afzonderlijke V2-testpagina is gebouwd op `/slimmer-werken-v2`, met eigen template en CSS, op basis van de bestaande vormgeving en relevante inhoud. De bestaande pagina blijft ongemoeid; de testpagina is niet opgenomen in de navigatie en krijgt `noindex, nofollow`.
- De V2-testpagina focust op vijf praktische toepassingsgebieden: gegevensverwerking, controle en kwaliteitsbewaking, beeld- en bestandsworkflows, informatie-uitwisseling tussen systemen en terugkerende werkzaamheden. De tekst benadrukt wat per systeem haalbaar is en doet geen algemene integratiebelofte.
- Het modulaire applicatieonderdeel is voorbereid met productkaarten voor naam, omschrijving, afbeelding, optionele abonnementsprijs en link. Het blijft verborgen zolang er geen beschikbare applicaties zijn.
- V2 benoemt mogelijke eigen, herbruikbare digitale toepassingen alleen als toekomstige richting en bevat geen vaste prijzen.
- Beginnen met kleine, afgebakende automatiseringsoplossingen. Bestaande Excel- en Access-werkwijzen kunnen aanleiding zijn voor procesverbetering.
- Aansluiten bij de specialistische positionering voor retail en e-commerce. Maak onderscheid tussen Data als dienst voor gegevensverwerking en Slimmer werken als oplossingen waarmee klanten zelf efficiënter werken.
- Wespi niet actief positioneren als ontwikkelaar van allerlei maatwerksoftware.
- Toekomstige producten pas actief aanbieden wanneer ze daadwerkelijk beschikbaar zijn.
- De prijsstructuur van V2 is nog niet definitief. De bestaande prijzen van € 249 en € 499 blijven voorlopig ongewijzigd; de eerder besproken € 495 is niet vastgesteld.
- Web voorlopig parkeren: niet verder ontwikkelen of actief aanbieden. De actieve Web-verwijzingen zijn op 26 oktober 2026 van de website verwijderd. Dit is geen definitieve afwijzing; Web blijft een mogelijk toekomstig idee, zie [IDEEEN.md](./IDEEEN.md).

Dit beschrijft de huidige ontwikkelfase. De testpagina is een afzonderlijke versie en verandert de bestaande pagina niet.

## 3. Later — ideeën en mogelijke ontwikkelingen

Mogelijke onderwerpen zijn Excel- en Access-processen, artikel- en assortimentsbeheer, productinformatie, productie- en fotoplanning, voorraadcontrole, order- en retourverwerking, herbruikbare applicaties met abonnementen en een eventuele latere heroverweging van Web.

Deze ideeën zijn niet goedgekeurd als ontwikkelopdrachten en hebben geen vastgestelde planning. Zie [IDEEEN.md](./IDEEEN.md).
