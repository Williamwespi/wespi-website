# SEO-migratie Wespi — Odoo naar FastAPI

**Controledatum: 11 november 2026 (Europe/Amsterdam).** Alleen dit rapport is aangemaakt. Geen websitecode, goedgekeurde tekst, ontwerp, redirect, DNS-, hosting- of e-mailinstelling gewijzigd. Geen commit, push of deployment.

## Uitvoeringsstatus na goedkeuring — 11 november 2026

De acht inhoudelijke redirects uit dit rapport zijn op expliciete opdracht lokaal geïmplementeerd, met absolute HTTPS-www-bestemmingen en directe 301 voor beide slashvarianten. Queryparameters blijven vóór het eventuele bestemmingsanker behouden. De drie bestaande redirects blijven behouden en hebben nu eveneens directe slashvarianten, zonder voorafgaande 307.

Rendering/3D, Vriendenprijs, Vriendenprijsaanvraag, In ontwikkeling, webshop, afsprakenmodule en kalender vervallen definitief volgens het gebruikersbesluit. Hun oude URL's geven een echte 404, zonder homepage-redirect. `/calendar` en `/appointment` hebben dezelfde afhandeling. Er zijn geen nieuwe pagina's of commerciële claims toegevoegd.

`/beeldbewerking` is toegevoegd aan PUBLIC_PAGES: de sitemap bevat nu alle 16 goedgekeurde publieke eindpagina's. Oude redirectpaden en de noindex-testpagina blijven uitgesloten. Canonicals en productie-/staging-indexeringsinstellingen zijn gecontroleerd.

**Validatie:** alle 46 regressietests slagen, inclusief de 11 redirects op beide slashvarianten (22 controles), exacte Location, directe 200-doelen, bestaande dienstpaden, bestemmingsankers, queryparameters, vervallen URL's en sitemap. Alleen lokaal via ASGI getest; geen verzoeken naar productie door redirects te volgen.

**Actueel oordeel:** de hier vastgestelde lokale redirect- en sitemapblokkades zijn opgelost en het vervalbesluit is genomen. Het onderstaande oorspronkelijke onderzoeksrapport blijft als nulmeting behouden. Het eerdere NO-GO is daarmee niet meer van toepassing op deze opgeloste punten. Een definitief productie-GO vereist nog controle op de echte hosting van TLS voor beide hosts, HTTP/HTTPS- en www-normalisatie met padbehoud zonder ketens, `WESPI_ENV=production`, publiek bereikbare robots/sitemap en ontbreken van proxy-noindex. Search Console-nulmeting/verificatie, onbekende historische URL's en eventuele oude media/backlinks blijven de aandachtspunten uit dit rapport. Geen hosting-, DNS- of e-mailinstellingen gewijzigd; geen commit, push of deployment.

## Oorspronkelijk oordeel vóór implementatie

**SEO-NO-GO voor de huidige, nog niet aangevulde migratieconfiguratie.** De belangrijkste fotografie-URL's kunnen behouden blijven en de nieuwe inhoud sluit grotendeels aan. Toch zouden acht relevante oude URL's zonder nieuwe 301 verdwijnen. Voor onder meer rendering en het vriendenprogramma ontbreekt bovendien een bevestigd afhandelingsbesluit. De host-/HTTPS-normalisatie en de nieuwe sitemap zijn nog niet compleet als migratievoorziening.

Een SEO-GO is mogelijk nadat de acht ontbrekende inhoudelijke redirects zijn goedgekeurd en ingericht, de overige oude URL's bewust zijn afgehandeld, de sitemap is aangevuld en de echte productiehost indexeerbaar en correct genormaliseerd is getest. Rankings en verkeer zijn zonder Search Console niet aantoonbaar veiliggesteld; verlies kan ook met een correct plan niet volledig worden uitgesloten.

## Afbakening en bewijskracht

- De oude website is rechtstreeks met openbare HTTP-GET-verzoeken onderzocht: sitemap, robots, HTML-metadata en links. De browsertool kon aanvankelijk niet alle live endpoints ophalen; die netwerkfout was geen bewijs dat de site onbereikbaar was. Rechtstreekse HTTPS-verzoeken leverden de website, sitemap en robots wel op.
- De sitemap bevat **23 URL's**: 22 inhoudelijke/technische HTML-antwoorden met 200 en één redirect (/calendar). Alle sitemapbestemmingen zijn afzonderlijk opgevraagd.
- Via sitemap en interne links zijn **30 unieke publieke URL's** onderzocht, inclusief zeven aanvullende technische/sociale adressen. Daarnaast zijn slash-, host-, protocol- en één trackingqueryvariant getest. Dit is de volledige aangetroffen inventaris uit deze bronnen, geen bewijs dat er geen verweesde pagina's, downloads, historische URL's of externe backlinks meer bestaan.
- Geen ingelogde Odoo-pagina's bezocht, geen formulieren ingediend en geen account, winkelmand of bestelling aangemaakt. Technische GET-redirects zijn alleen geobserveerd.
- De nieuwe routes en metadata zijn rechtstreeks tegen de lokale FastAPI-app gecontroleerd. Productiegedrag is in een afzonderlijke in-memory app-instantie met WESPI_ENV=production gesimuleerd; de draaiende server en zijn instellingen zijn niet aangepast.
- Er is geen Search Console-toegang, Odoo-pagina-export, zoekverkeerexport of volledige externe-link-/logexport beschikbaar voor deze controle.
- Dit rapport vervangt als actuele URL-inventaris de historische routeclaims in LIVEGANG_MIGRATIE.md: Productbeeldbewerking bestaat inmiddels, en de hier genoemde oude adressen zijn nu live onderzocht. Dat eerdere document is niet gewijzigd.
- Onzichtbare zero-widthtekens en herhaalde witruimte zijn in de metadatatabellen voor leesbaarheid genormaliseerd; inhoud en aangetroffen kopniveaus zijn niet herschreven.

## 1. Bestaande website: URL's en metadata

### 1.1 Sitemap en robots

[Live robots.txt](https://www.wespi.nl/robots.txt) geeft HTTP 200 en bevat:

    User-agent: *
    Sitemap: https://www.wespi.nl/sitemap.xml

Er staat geen algemene crawlblokkade in. [Live sitemap.xml](https://www.wespi.nl/sitemap.xml) geeft HTTP 200 en is één URL-set, geen sitemapindex. De 23 bestemmingen staan hieronder. Lastmod-waarden zijn Odoo-metadata, geen bewijs van werkelijke inhoudelijke wijzigingsdata of Google-crawldata.

Bij de hieronder aangetroffen 200-pagina's zijn geen robots-meta-noindex of X-Robots-Tag-noindex gemeten; de canonical verwijst naar de eigen HTTPS-www-URL zonder afsluitende slash, behalve de homepage die op / eindigt. Ze zijn daarmee technisch potentieel indexeerbaar; **dit bewijst geen opname in Google**. De canonicalkolom hieronder geeft het pad weer; de vaste prefix is https://www.wespi.nl.

### 1.2 Alle 23 sitemap-URL's

| Oude URL / bron | HTTP | Title | H1, alle aangetroffen | Meta description | Canonicalpad |
| --- | --- | --- | --- | --- | --- |
| [/beeldbewerking](https://www.wespi.nl/beeldbewerking) | 200 | Beeldbewerking | Beeldbewerking | Geoptimaliseerde productfoto's zorgen voor meer verkopen en geven een professionelere uitstraling | /beeldbewerking |
| [/beeldbewerking/auto](https://www.wespi.nl/beeldbewerking/auto) | 200 | Beeldbewerking auto | Meer verkopen / door unieke beelden | Professionele beeldbewerking van auto’s voor een perfecte presentatie. Wij retoucheren, verwijderen achtergronden en verbeteren kleuren voor een strakke, verkoopklare look. Ideaal voor autodealers en online advertenties. | /beeldbewerking/auto |
| [/beeldbewerking/auto/voorbeelden](https://www.wespi.nl/beeldbewerking/auto/voorbeelden) | 200 | voorbeelden fotobewerking auto | Kies de perfecte achtergrond / B enieuwd wat wij voor je kunnen betekenen? | Niet ingevuld | /beeldbewerking/auto/voorbeelden |
| [/contactus](https://www.wespi.nl/contactus) | 200 | Contact Us \| Wespi | Benieuwd wat wij voor jou kunnen betekenen? | Niet ingevuld | /contactus |
| [/diensten](https://www.wespi.nl/diensten) | 200 | Diensten | Al onze diensten | Alle diensten om jouw producten te versterken | /diensten |
| [/diensten/contentbeheer](https://www.wespi.nl/diensten/contentbeheer) | 200 | Contentbeheer \| Wespi | Contentbeheer | Niet ingevuld | /diensten/contentbeheer |
| [/diensten/rendering](https://www.wespi.nl/diensten/rendering) | 200 | Rendering \| Wespi | 3D-Beelden | Niet ingevuld | /diensten/rendering |
| [/inontwikkeling](https://www.wespi.nl/inontwikkeling) | 200 | inontwikkeling \| Wespi | In ontwikkeling | Niet ingevuld | /inontwikkeling |
| [/overons](https://www.wespi.nl/overons) | 200 | Over Wespi \| Wespi | Wij ontzorgen | Niet ingevuld | /overons |
| [/privacystatement](https://www.wespi.nl/privacystatement) | 200 | privacystatement \| Wespi | Geen H1 | Niet ingevuld | /privacystatement |
| [/productfotografie](https://www.wespi.nl/productfotografie) | 200 | Productfotografie | Productfotografie | Duidelijke productfoto's voor een scherpe prijs | /productfotografie |
| [/productfotografie/kledingfotografie](https://www.wespi.nl/productfotografie/kledingfotografie) | 200 | Kledingfotografie | Geen H1 | Wil jij haarscherpe, duidelijke beelden van je kledingcollectie en het liefst zo goedkoop mogelijk? | /productfotografie/kledingfotografie |
| [/productfotografie/packshotfotografie](https://www.wespi.nl/productfotografie/packshotfotografie) | 200 | packshotfotografie | Geen H1 | Professionele packshotfotografie die jouw producten laat stralen. Haarscherpe, goed belichte foto’s voor webshops, catalogi en social media. Perfecte productfoto’s die verkoop stimuleren. | /productfotografie/packshotfotografie |
| [/productfotografie/plattefotografie](https://www.wespi.nl/productfotografie/plattefotografie) | 200 | Platte fotografie | Geen H1 | Platte fotografie die jouw producten stijlvol en helder in beeld brengt. Perfect voor webshops, social media en marketing. Professionele flat lay foto’s die aandacht trekken en conversie verhogen | /productfotografie/plattefotografie |
| [/studio](https://www.wespi.nl/studio) | 200 | studio \| Wespi | Onze studio | Niet ingevuld | /studio |
| [/vriendenprijs](https://www.wespi.nl/vriendenprijs) | 200 | vriendenprijs \| Wespi | Vrienden / prijs | Niet ingevuld | /vriendenprijs |
| [/vriendenprijsaanvraag](https://www.wespi.nl/vriendenprijsaanvraag) | 200 | vriendenprijsaanvraag \| Wespi | Geen H1 | Niet ingevuld | /vriendenprijsaanvraag |
| [/terms](https://www.wespi.nl/terms) | 200 | Terms & Conditions \| Wespi | Algemene Voorwaarden Wespi | Niet ingevuld | /terms |
| [/appointment](https://www.wespi.nl/appointment) | 200 | Appointment Types \| Wespi | (leeg element) | Niet ingevuld | /appointment |
| [/calendar](https://www.wespi.nl/calendar) | 301 | — | Geen H1 | Niet ingevuld | — |
| [/shop](https://www.wespi.nl/shop) | 200 | Products \| Wespi | Geen H1 | Niet ingevuld | /shop |
| [/](https://www.wespi.nl/) | 200 | Betaalbare productfotografie | De basis op orde? / B enieuwd wat wij voor je kunnen betekenen? / Kledingfotografie / Platte fotografie / packshotfotografie / een greep uit de mogelijkheden / Werkwijze / Overige diensten | Haarscherpe, duidelijke beelden van je collectie en ook nog eens spotgoedkoop! | / |
| [/website/info](https://www.wespi.nl/website/info) | 200 | Odoo Information \| Wespi | Wespi | Niet ingevuld | /website/info |

Lege of ontbrekende H1's/descriptions zijn bevindingen van de oude site, geen opdracht om het nieuwe ontwerp te veranderen. /appointment heeft een leeg H1-element; /calendar is geen zelfstandige HTML-eindbestemming.

### 1.3 Aanvullend aangetroffen publieke adressen

De onderstaande zeven adressen staan niet in de sitemap, maar zijn via links aangetroffen. Bij de vier 200-formulier-/mandpagina's is ook geen algemene noindex aangetroffen; dit maakt ze niet automatisch waardevolle SEO-landingspagina's.

| URL / bron | HTTP | Location | Title | Canonicalpad | Metadata / type |
| --- | --- | --- | --- | --- | --- |
| [/shop/change_pricelist/3](https://www.wespi.nl/shop/change_pricelist/3) | 301 | /shop/change_pricelist/geen-afwijkende-prijzen-eur-3 | — | — | Redirect, geen inhoudelijke pagina |
| [/website/social/linkedin](https://www.wespi.nl/website/social/linkedin) | 303 | https://linkedin.com/company/wespi/ | — | — | Redirect, geen inhoudelijke pagina |
| [/shop/change_pricelist/geen-afwijkende-prijzen-eur-3](https://www.wespi.nl/shop/change_pricelist/geen-afwijkende-prijzen-eur-3) | 303 | /shop | — | — | Redirect, geen inhoudelijke pagina |
| [/shop/cart](https://www.wespi.nl/shop/cart) | 200 | — | Shopping Cart \| Wespi | /shop/cart | Geen H1; description niet ingevuld |
| [/web/login](https://www.wespi.nl/web/login) | 200 | — | Login \| Wespi | /web/login | Geen H1; description niet ingevuld |
| [/web/reset_password](https://www.wespi.nl/web/reset_password) | 200 | — | Reset password \| Wespi | /web/reset_password | Geen H1; description niet ingevuld |
| [/web/signup](https://www.wespi.nl/web/signup) | 200 | — | Sign up login \| Wespi | /web/signup | Geen H1; description niet ingevuld |

Deze technische Odoo-routes bestaan niet in het FastAPI-routebestand. Er is geen klantportaal, webshop of afsprakenmodule in de nieuwe website aangetroffen. Bevestig vóór verhuizing of daar nog bedrijfsprocessen van afhankelijk zijn. Er is geen grond om zulke adressen generiek naar een fotografiedienst of homepage te sturen. Voor beëindigde technische routes is een echte 404/410 passend; voor nog benodigde Odoo-toegang is een afzonderlijk bereikbaar Odoo-adres nodig, niet een verzonnen SEO-vervanging.

De bestaande LinkedIn-doorverwijzing kan desgewenst als 303 naar het bestaande profiel behouden blijven. Hij is geen inhoudelijke 301-migratie en de oude prijslijstacties hoeven bij het beëindigen van de webshop geen redirectketen te houden.

### 1.4 Belangrijke interne verbindingen

De oude hoofdnavigatie verwijst op de gecontroleerde pagina's naar:

- /diensten → alle diensten.
- /productfotografie → productfotografie-overzicht.
- /beeldbewerking → beeldbewerking.
- /studio → apparatuur/studio.
- /overons → bedrijfsinformatie.
- /contactus → contact.

Belangrijke inhoudelijke links:

- [Home](https://www.wespi.nl/) en [Productfotografie](https://www.wespi.nl/productfotografie) linken naar kledingfotografie, packshotfotografie en platte fotografie.
- [Diensten](https://www.wespi.nl/diensten) linkt daarnaast naar contentbeheer, rendering en inontwikkeling.
- [Beeldbewerking](https://www.wespi.nl/beeldbewerking) linkt naar /beeldbewerking/auto.
- [Autobewerking](https://www.wespi.nl/beeldbewerking/auto) linkt naar /beeldbewerking/auto/voorbeelden, ook met #Nummerplaatcorrectie en #Persoonlijk-logo.
- [Contact](https://www.wespi.nl/contactus) linkt naar /privacystatement en /terms.
- [Vriendenprijs](https://www.wespi.nl/vriendenprijs) linkt naar /vriendenprijsaanvraag.

Een ontbrekende 301 op deze adressen raakt dus niet alleen een mogelijke Google-vermelding, maar ook bestaande bookmarks, gedeelde links en externe verwijzingen.

### 1.5 Bestaande redirects en URL-varianten

| Gemeten verzoek | Huidig antwoord | Gevolg voor migratie |
| --- | --- | --- |
| https://www.wespi.nl/calendar | 301 → /appointment → 200 | Oude alias direct naar de gekozen eindafhandeling brengen; geen keten naar een verdwenen module. |
| https://www.wespi.nl/shop/change_pricelist/3 | 301 → /shop/change_pricelist/geen-afwijkende-prijzen-eur-3 → 303 → /shop | Technische Odoo-prijsactie; niet als commerciële SEO-pagina migreren. |
| https://www.wespi.nl/website/social/linkedin | 303 → https://linkedin.com/company/wespi/ | Externe profielverwijzing, geen lokale inhoudspagina. |
| HTTP met www, root en drie geteste dienst-/contactpaden | 301 → dezelfde URL op HTTPS met www | Pad blijft behouden; als uitgangspunt gebruiken. |
| HTTP zonder www, root en dezelfde drie paden | 301 → http://www.wespi.nl, daarna HTTPS | **Het oorspronkelijke pad gaat verloren**; de geteste dienst-/contactpaden belanden op home. Niet overnemen. |
| HTTPS zonder www, root en dezelfde drie paden | TLS-certificaat-hostnaammismatch | Vanaf deze controleomgeving geen geldige HTTPS-respons op wespi.nl; niet als 404 of werkende redirect classificeren. Nieuwe host moet beide namen dekken. |
| Alle 22 niet-root-sitemap-URL's met afsluitende slash | 301 → het pad zonder slash | Deze bestaande alternatieve URL's mee afhandelen. /calendar/ heeft nu bovendien de aliasstap naar /appointment. |
| Kledingfotografie met ?utm_source=migratiecontrole | 200, canonical zonder query | Trackingvarianten zijn geen aparte inhoudelijke pagina's. |

Hostpad-steekproef: /contactus, /productfotografie/kledingfotografie en /beeldbewerking/auto. De TLS-waarneming is geverifieerd met normale certificaatcontrole; verificatie is niet uitgeschakeld. De HTTP-padverliezen zijn live waarnemingen, geen aanname over de nieuwe host.

## 2. Vergelijking oude en nieuwe URL's

Nieuwe paden zijn inhoudelijke voorstellen, geen uitgevoerde redirects. De lokale HTTP-kolom toont de **huidige** nieuwe-appstatus op het oude pad, zonder redirects automatisch te volgen. Alle voorgestelde nieuwe inhoudelijke bestemmingen geven lokaal direct 200. De genoemde ankers #diensten, #platte-fotografie en #achtergronden bestaan.

| Oude URL | Nieuwe bestemming / afhandeling | Onderwerp | Status | Nu lokaal op oud pad | Benodigde actie | 301 |
| --- | --- | --- | --- | --- | --- | --- |
| `/` | `/` | Home / productfotografie | Behouden | 200 | URL en interne dienstverwijzingen behouden. | — |
| `/productfotografie/kledingfotografie` | `/productfotografie/kledingfotografie` | Kledingfotografie / ghost mannequin | Behouden | 200 | Exacte URL behouden. | — |
| `/productfotografie/packshotfotografie` | `/productfotografie/packshotfotografie` | Packshotfotografie | Behouden | 200 | Exacte URL behouden. | — |
| `/beeldbewerking` | `/beeldbewerking` | Professionele beeldbewerking | Behouden | 200 | URL behouden; toevoegen aan nieuwe sitemap. | — |
| `/productfotografie` | `/beeld` | Overzicht productfotografie | Gewijzigd | 404 | Fotografiediensten zijn hier toegankelijk; bredere beeldpagina is beste bestaande overzichtsbestemming. | 301 toevoegen |
| `/productfotografie/plattefotografie` | `/productfotografie/kledingfotografie#platte-fotografie` | Platte fotografie / flat lay | Gewijzigd | 404 | Samenvoegen met bestaande inhoudelijke sectie; anker bestaat. | 301 toevoegen |
| `/beeldbewerking/auto` | `/beeldbewerking/automotive` | Autobeeldbewerking / digitale showroom | Gewijzigd | 301 | Bestaande directe redirect behouden. | 301 bestaat |
| `/beeldbewerking/auto/voorbeelden` | `/beeldbewerking/automotive#achtergronden` | Achtergronden, logo en kentekenplaat | Gewijzigd | 404 | Bestaande automotive-pagina bevat voorbeelden en mogelijkheden; anker bestaat. | 301 toevoegen |
| `/overons` | `/over-wespi` | Over Wespi | Gewijzigd | 404 | Bedrijfs- en merkpagina rechtstreeks koppelen. | 301 toevoegen |
| `/contactus` | `/contact` | Contact | Gewijzigd | 404 | Contactpagina en oude inkomende contactlinks behouden. | 301 toevoegen |
| `/diensten` | `/#diensten` | Overzicht van alle diensten | Gewijzigd | 404 | Nieuw breed dienstenoverzicht staat op home, anker bestaat. Onderbouwde uitzondering op geen homepage-redirects. | 301 toevoegen |
| `/diensten/contentbeheer` | `/data/productdata` | Artikeldata, productteksten en contentbeheer | Gewijzigd | 404 | Sterke inhoudelijke opvolger; marketplace-focus is deels minder expliciet. | 301 toevoegen |
| `/studio` | `/productfotografie/kledingfotografie` | Studio en fotografieapparatuur | Gewijzigd | 404 | Bestaande StyleShoots/studio-uitleg is hier de meest directe opvolger; niet identiek aan een algemene studiopagina. | 301 toevoegen |
| `/privacystatement` | `/privacyverklaring` | Privacy | Gewijzigd | 301 | Bestaande directe redirect behouden. | 301 bestaat |
| `/terms` | `/algemene-voorwaarden` | Algemene voorwaarden | Gewijzigd | 301 | Bestaande directe redirect behouden. | 301 bestaat |
| `/diensten/rendering` | `Geen gelijkwaardige nieuwe bestemming` | 3D-modeling / rendering | Vervallen? besluit nodig | 404 | Niet naar fotografie of home sturen. Als dienst stopt: echte 404/410 accepteren na expliciet besluit; zoeksignalen voor dit onderwerp blijven dan niet behouden. | Geen passende 301 |
| `/inontwikkeling` | `Geen inhoudelijke opvolger` | Algemene ontwikkelaankondiging | Vervallen? bevestigen | 404 | Geen automatische koppeling aan Slimmer werken; bij definitieve verwijdering 404/410. | Geen 301 nodig |
| `/vriendenprijs` | `Geen gelijkwaardig aanbod` | Vriendenprogramma / abonnement | Vervallen? besluit nodig | 404 | Oud aanbod is openbaar. Bevestig beëindiging en eventuele bestaande afspraken; bij vervallen 404/410, geen prijs-/aanbodclaim door een redirect. | Geen passende 301 |
| `/vriendenprijsaanvraag` | `Geen gelijkwaardig aanvraagproces` | Aanvraag vriendenprogramma | Vervallen? besluit nodig | 404 | Samen met programma besluiten. Alleen /contact kiezen als expliciet bevestigd is dat dit inhoudelijk de opvolgende aanvraag-/supportbestemming is. | Geen automatische 301 |
| `/appointment` | `Geen nieuwe boekingsmodule` | Afspraaktypen, nu leeg zichtbaar | Vervallen? bevestigen | 404 | Bevestig dat geen bestaande boekingsworkflow nodig blijft; daarna 404/410. | Geen passende 301 |
| `/calendar` | `Zelfde besluit als /appointment` | Oude afspraakalias | Vervallen? bevestigen | 404 | Huidige live 301 naar /appointment niet meenemen als keten naar een ontbrekende pagina. Beide adressen direct dezelfde eindafhandeling geven. | Niet ketenen |
| `/shop` | `Geen nieuwe webshop` | Lege Odoo-catalogus | Vervallen? bevestigen | 404 | Geen producten zichtbaar tijdens controle; dit bewijst niet dat er nooit orders/gebruik waren. Na bevestigde beëindiging 404/410. | Geen passende 301 |
| `/website/info` | `Geen opvolger nodig` | Technische Odoo-informatie | Vervallen | 404 | Geen commerciële SEO-landingspagina; niet naar home omleiden. | Geen 301 nodig |

Belangrijke keuzes:

- De twee belangrijkste fotografie-dienst-URL's blijven exact behouden. Daar mag geen nieuwe brede redirect vóór worden geplaatst.
- /productfotografie verhuist naar /beeld omdat die pagina productfotografie, kledingfotografie en packshotfotografie inhoudelijk ontsluit. De nieuwe pagina is wel breder dan het oude fotografie-overzicht.
- /diensten krijgt als enige inhoudelijk onderbouwde homepage-bestemming /#diensten: de oude algemene dienstenverzameling gaat naar de nieuwe algemene dienstenverzameling. Dit is geen algemene fallback voor onbekende URL's.
- /studio verhuist in het voorstel naar de bestaande kledingfotografiepagina met haar studio-/StyleShoots-uitleg. Een deel van de oude algemenere apparatuurcontext vervalt; dit blijft een te accorderen samenvoeging.
- Voor rendering en het vriendenprogramma is **geen equivalent** aangetroffen. Een redirect naar home, AI-modelfotografie of gewone fotografie zou niet dezelfde zoekintentie bedienen. Maak hiervoor vóór livegang een expliciet behoud-/vervalbesluit; dit rapport introduceert geen nieuw aanbod of pagina.

## 3. Concreet 301-voorstel

### 3.1 Directe inhoudelijke redirects

| Oud pad | Definitieve absolute Location | Implementatiestatus | Nu lokaal | Motivering |
| --- | --- | --- | --- | --- |
| `/productfotografie` | https://www.wespi.nl/beeld | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/productfotografie/plattefotografie` | https://www.wespi.nl/productfotografie/kledingfotografie#platte-fotografie | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/beeldbewerking/auto` | https://www.wespi.nl/beeldbewerking/automotive | 301 bestaat | 301 | Inhoudelijke opvolger, directe eindbestemming. |
| `/beeldbewerking/auto/voorbeelden` | https://www.wespi.nl/beeldbewerking/automotive#achtergronden | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/overons` | https://www.wespi.nl/over-wespi | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/contactus` | https://www.wespi.nl/contact | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/diensten` | https://www.wespi.nl/#diensten | 301 toevoegen | 404 | Alle diensten zijn in home #diensten ondergebracht. |
| `/diensten/contentbeheer` | https://www.wespi.nl/data/productdata | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/studio` | https://www.wespi.nl/productfotografie/kledingfotografie | 301 toevoegen | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/privacystatement` | https://www.wespi.nl/privacyverklaring | 301 bestaat | 301 | Inhoudelijke opvolger, directe eindbestemming. |
| `/terms` | https://www.wespi.nl/algemene-voorwaarden | 301 bestaat | 301 | Inhoudelijke opvolger, directe eindbestemming. |
| `/diensten/rendering` | https://www.wespi.nlGeen gelijkwaardige nieuwe bestemming | Geen passende 301 | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/inontwikkeling` | https://www.wespi.nlGeen inhoudelijke opvolger | Geen 301 nodig | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/vriendenprijs` | https://www.wespi.nlGeen gelijkwaardig aanbod | Geen passende 301 | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/vriendenprijsaanvraag` | https://www.wespi.nlGeen gelijkwaardig aanvraagproces | Geen automatische 301 | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/appointment` | https://www.wespi.nlGeen nieuwe boekingsmodule | Geen passende 301 | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/shop` | https://www.wespi.nlGeen nieuwe webshop | Geen passende 301 | 404 | Inhoudelijke opvolger, directe eindbestemming. |
| `/website/info` | https://www.wespi.nlGeen opvolger nodig | Geen 301 nodig | 404 | Inhoudelijke opvolger, directe eindbestemming. |

**Acht redirects ontbreken nog.** De drie bestaande redirects voor auto, privacy en voorwaarden zijn getest als één 301 naar een directe 200-bestemming en moeten behouden blijven.

### 3.2 Slash-, host- en queryafhandeling

Voorstel voor de toekomstige server-/proxyconfiguratie, nog niet uitgevoerd:

1. Gewenste eindvorm: HTTPS, www.wespi.nl, zonder afsluitende slash behalve de root.
2. Laat alle vier protocol-/hostvormen werken. Zorg eerst voor geldig TLS op wespi.nl én www.wespi.nl: een browser kan bij een ongeldig certificaat niet eerst veilig een HTTPS-redirect ontvangen.
3. Beoordeel de exacte oude padmapping en slash-normalisatie samen en stuur waar uitvoerbaar **in één permanente 301** naar de uiteindelijke absolute HTTPS-www-bestemming. Geef de acht oude paden ook in hun slash-vorm expliciet dezelfde eindbestemming.
4. Laat bekende behouden URL's direct 200 geven. Geen brede /productfotografie/*-redirect die kledingfotografie, packshotfotografie of de nieuwe AI-pagina onbedoeld opvangt.
5. Pas daarna normalisatie van overige host-/slashvarianten toe. Geen regels die het pad verwijderen of een eindbestemming naar zichzelf laten terugsturen.
6. Bewaar relevante tracking-/functionele queryparameters waar dat nodig is. Canonicals van gewone dienstpagina's blijven queryloos; oude sorteer-/sessie-/shopparameters zijn geen reden om niet-bestaande functies te reconstrueren.
7. Fragmenten na # worden niet aan de server gestuurd. Maak daarom geen schijnbare 301-regels voor #Nummerplaatcorrectie of #Persoonlijk-logo. De voorgestelde expliciete #achtergronden in Location is een navigatiehulp op de samengevoegde pagina, geen afzonderlijke canonical.

De huidige FastAPI-slashafhandeling is nog niet overal dit plan: /beeldbewerking/auto/, /terms/ en /privacystatement/ geven eerst een 307 naar het oude pad zonder slash en daarna de bestaande 301. /productfotografie/kledingfotografie/ en /beeldbewerking/ geven een 307 naar hun eigen pad zonder slash. /contactus/ geeft nu 404. Dit zijn concrete gemeten situaties, geen uitgevoerde aanpassingen.

Acceptatievoorbeelden vóór omschakeling:

| Test | Vereist eindgedrag |
| --- | --- |
| http://wespi.nl/contactus/ | Eén 301 naar https://www.wespi.nl/contact, daarna 200; nooit home. |
| https://wespi.nl/overons | Geldig TLS; 301 rechtstreeks naar https://www.wespi.nl/over-wespi; daarna 200. |
| https://www.wespi.nl/beeldbewerking/auto/ | Rechtstreeks 301 naar https://www.wespi.nl/beeldbewerking/automotive; daarna 200. |
| https://www.wespi.nl/productfotografie/kledingfotografie | Direct 200 met dezelfde canonical; geen redirect naar /beeld. |
| https://www.wespi.nl/productfotografie/plattefotografie/ | 301 naar de nieuwe kledingfotografiepagina met #platte-fotografie; doelpad geeft 200. |

Controleer alle goedgekeurde mappingregels daarna op echte statuscode, Location, direct 200-doel en ontbreken van loops/ketens. Houd de redirects langdurig beschikbaar, bij voorkeur blijvend voor oude externe links. Google adviseert doorgaans minimaal één jaar. Onverwante homepage-redirects kunnen als soft 404 worden gezien; bij werkelijk verwijderde inhoud is een echte 404/410 gepaster. Zie [Google: siteverhuizingen en URL-mapping](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).

### 3.3 Vervallen en technische adressen

Voor /diensten/rendering, /vriendenprijs en /vriendenprijsaanvraag is een expliciet bedrijfsbesluit nodig; een SEO-redirect mag geen dienst suggereren die niet meer bestaat. Voor /inontwikkeling en de lege afspraak-/shopfuncties moet bewust bevestigd worden dat ze niet nodig blijven. Daarna kan een echte 404/410 worden geaccepteerd. Een 404 is niet op zichzelf een fout wanneer er geen relevante opvolger is.

Voor /calendar moet hetzelfde eindbesluit rechtstreeks gelden als voor /appointment. De bestaande calendar → appointment-stap behouden terwijl appointment verdwijnt is onjuist.

Voor de technische /web/login-, /web/signup-, /web/reset_password- en shop/cart-adressen: vóór omschakeling controleren of klanten of medewerkers deze nog via wespi.nl gebruiken. Zo ja, apart toegang/migratie afspreken; dat is een Odoo-afhankelijkheid, geen nieuwe functie die in dit rapport wordt toegevoegd. Niet zonder bewijs aannemen dat de nieuwe website die workflows vervangt.

## 4. Risico's voor bestaande vindbaarheid

| Risico | Onderbouwing | Prioriteit |
| --- | --- | --- |
| Relevante oude URL's worden 404 | Acht concrete gaten in tabel 3.1; meerdere staan in oude navigatie én sitemap. | Verplicht vóór livegang: 301's goedkeuren, uitvoeren en testen. |
| Rendering/3D valt inhoudelijk weg | Oude pagina is openbaar, potentieel indexeerbaar en gelinkt; geen gelijkwaardig nieuw aanbod. | Verplicht vóór livegang: expliciet besluit, verkeers-/linkbelang controleren of restrisico accepteren. |
| Vriendenprogramma/aanvraag verdwijnt | Openbare aanbod- en formulierpagina's; geen nieuw equivalent. | Verplicht vóór livegang: beëindiging/opvolging en afhandeling bevestigen. |
| Hostnormalisatie verliest paden; HTTPS zonder www faalt | Live HTTP-apex verliest geteste paden; HTTPS-apex heeft een certificaat-hostnaammismatch. | Verplicht voor de nieuwe hosting vóór omschakeling: geldig TLS en padbehoud. |
| Lokale blokkades worden naar productie meegenomen | Development blokkeert crawlen/noindex; productie is alleen correct als de juiste configuratie in het echte proces zit. | Verplicht vóór livegang en direct erna controleren. |
| /beeldbewerking ontbreekt in sitemap | Het is een bestaande oude SEO-URL én een goedgekeurde nieuwe pagina; mist in PUBLIC_PAGES. | Concrete migratieverbetering vóór livegang, geen tekstwijziging. |
| Homefocus wordt breder | Oude title was productfotografiegericht; nieuwe home focust Beeld, Data en Slimmer werken. | Risico rapporteren, GSC-homeverkeer vergelijken; geen goedgekeurde tekst herschrijven. |
| Zelfstandige platte-/studio-pagina wordt samengevoegd | Relevante inhoud blijft deels op andere pagina's, maar een zelfstandige landingspagina verdwijnt. | Vóór livegang redirects; na livegang prestaties van betrokken zoektermen volgen. |
| Oude Odoo-afbeeldings-/download-URL's verdwijnen | De nieuwe site gebruikt /static, Odoo gebruikt onder meer /web/image. Volledige image-/downloadmapping en afbeeldingzoekverkeer zijn niet onderzocht. | Vóór uitschakelen Odoo export/logs veiligstellen en belangrijke inkomende media-URL's bepalen; gerichte mapping indien relevant. |
| GSC-verificatie kan bij CMS-wissel verdwijnen | Bestaande verificatiemethode is niet bekend. | Vóór livegang vaststellen en behouden; geen token of DNS-record gewijzigd. |
| Onbekende verweesde of externe bestemmingen ontbreken | Sitemap/linkcrawl toont geen niet-gelinkte historische URL's. | Vóór livegang aanvullen met Odoo-export, logs of GSC-links; resterende onbekendheid expliciet accepteren. |

De nieuwe ontwerp-/inhoudskeuzes zijn goedgekeurd en worden niet heropend. Dit rapport onderscheidt functioneel werkende pagina's van het bewaren van oude URL-signalen.

## 5. Zoekwoorden en zoekintentie

### 5.1 Belangrijkste diensten afzonderlijk

| Oud onderwerp / zoekintentie | Nieuwe inhoudelijke aansluiting | Beoordeling |
| --- | --- | --- |
| Kledingfotografie, ghost mannequin, bodyform, kledingcollectie | Zelfde /productfotografie/kledingfotografie; title bevat kledingfotografie, description benoemt bodyform/ghost mannequin/platte fotografie; studio en nabewerking aanwezig. | Kernintentie behouden; URL behouden. De goedgekeurde H1 is commerciëler, niet hetzelfde als de oude kop. |
| Packshotfotografie en professionele productfoto's voor webshop/catalogus | Zelfde /productfotografie/packshotfotografie; title en description noemen packshotfotografie en concrete prijs; productvoorbeelden aanwezig. | Kernintentie behouden, geen nieuwe redirect nodig. |
| Productfotografie als overkoepelende dienst | Nieuwe /beeld heeft productfotografie in title en description en links naar kleding/packshot. | Goede maar bredere opvolger; /productfotografie moet daarheen. Home wordt breder, dus behoud van het generieke zoekverkeer is niet alleen met URL-techniek gegarandeerd. |
| Platte fotografie / flat lay, accessoires en babykleding | Bestaande sectie #platte-fotografie op Kledingfotografie, met platte fotografie, accessoires en prijs. | Inhoudelijk relevant, zelfstandige URL verdwijnt. Specifieke termen als flat lay/babykleding zijn minder expliciet in de nieuwe sectie; risico vastleggen, niet automatisch tekst wijzigen. |
| Professionele beeldbewerking, retouche, vrijstaand, kleurcorrectie | /beeldbewerking blijft, met drie duidelijke diensten; nieuwe kleding-/product-/autopagina's bieden verdieping. | Kernintentie behouden en uitgesplitst; overzicht aan sitemap toevoegen. |
| Autofoto's, digitale showroom, achtergrond, nummerplaat/logo | /beeldbewerking/automotive bevat passende voorbeelden, achtergronden en mogelijkheden. | Goede opvolger; bestaande auto-301 behouden en voorbeelden-301 toevoegen. Oude Premium-claims niet automatisch terugbrengen. |
| Sieradenbeeldbewerking | Oude /beeldbewerking benoemt sieraden expliciet; nieuwe productpagina toont onder meer een horloge, maar benoemt sieraden niet expliciet. | Mogelijk verlies van een specifieke longtailfocus. Relevantie hangt af van GSC; geen nieuwe claim/tekst opgelegd. |
| Contentbeheer, SEO-productteksten en marketplacecontent | /data/productdata verwerkt productinformatie en maakt titels/omschrijvingen. | Sterke kernaansluiting, maar oude termen contentbeheer en marketplaceplatforms zijn minder expliciet. Exacte oude zoekvraagdekking niet bewezen. |
| Studio / StyleShoots / Packshotcreator | Nieuwe kledingpagina behandelt StyleShoots/studio; geen zelfstandige /studio. | Gedeeltelijke samenvoeging; apparatuur-/studiobreedte is smaller. |
| 3D-modeling / rendering | Geen passende nieuwe dienstpagina. | Onderwerp vervalt; eventuele bestaande vindbaarheid daarvoor kan niet met een ongerelateerde redirect worden behouden. |

Voor de vier expliciet gevraagde kernthema's is relevante nieuwe inhoud aanwezig: kledingfotografie, productfotografie, packshotfotografie en professionele beeldbewerking. Het risico zit vooral in ontbrekende oude-padredirects en het wegvallen/samenvoegen van secundaire onderwerpen, niet in een compleet verdwenen fotografie-aanbod.

### 5.2 Metadata van de 16 goedgekeurde nieuwe publieke pagina's

Onderstaande metadata is lokaal gerenderd met productie-instellingen. Alle 16 geven direct 200, hebben één H1 en een zelfverwijzende HTTPS-www-canonical. Hun HTML bevat geen algemene noindex; de productie-antwoorden leveren geen algemene X-Robots-Tag-noindex.

| Nieuw pad | Title | H1 | Meta description | Canonical |
| --- | --- | --- | --- | --- |
| `/` | Wespi \| Beeld, Data & Slimmer werken | Van product tot proces. Digitaal goed geregeld. | Wespi helpt bedrijven met professionele productfotografie, beeldbewerking, data en slimme digitale processen. | https://www.wespi.nl/ |
| `/beeld` | Beeld \| Productfotografie & beeldbewerking \| Wespi | Goed beeld begint bij het product. En eindigt bij een resultaat dat direct bruikbaar is. | Productfotografie en professionele beeldbewerking voor webshops en bedrijven. Ontdek kledingfotografie, packshotfotografie en beeldbewerking bij Wespi. | https://www.wespi.nl/beeld |
| `/productfotografie/kledingfotografie` | Kledingfotografie voor webshops en merken \| Wespi | Kleding goed in beeld. Mooi, duidelijk en herkenbaar. | Professionele kledingfotografie voor webshops en merken. Bodyform, ghost mannequin en platte fotografie voor consistente collecties en e-commerce. | https://www.wespi.nl/productfotografie/kledingfotografie |
| `/productfotografie/kledingfotografie/ai-modelfotografie` | AI-modelfotografie voor kleding \| Wespi | Van kledingfoto naar modelbeeld. | Breid je kledingfotografie bij Wespi uit met AI-modelbeelden, lifestylefoto's en video's. Van professionele productfoto tot een complete collectiepresentatie. | https://www.wespi.nl/productfotografie/kledingfotografie/ai-modelfotografie |
| `/productfotografie/packshotfotografie` | Packshotfotografie vanaf €9,99 \| Wespi | Producten strak in beeld. Snel, verzorgd en klaar voor verkoop. | Professionele packshotfotografie vanaf €9,99 per product. Voor schoenen, accessoires en andere kleine tot middelgrote producten. Strak gefotografeerd en netjes nabewerkt. | https://www.wespi.nl/productfotografie/packshotfotografie |
| `/beeldbewerking/product` | Productbeeldbewerking voor webshops en e-commerce \| Wespi | Sterk product. Verzorgd beeld. | Laat je productfoto’s professioneel bewerken door Wespi. Achtergronden, retouche, schaduwen en kleurafstemming voor een consistente webshop. Bekijk het verschil. | https://www.wespi.nl/beeldbewerking/product |
| `/beeldbewerking/kleding` | Kledingbeeldbewerking voor webshops en merken \| Wespi | Kledingfoto's professioneel bewerkt | Laat bestaande kledingfoto's professioneel bewerken door Wespi. Vrijstaand maken, kleurcorrectie en retouche voor webshops, kledingmerken en retailers. | https://www.wespi.nl/beeldbewerking/kleding |
| `/beeldbewerking/automotive` | Autobeeldbewerking voor autobedrijven \| Digitale showroom \| Wespi | Elke auto in beeld. Eén herkenbare showroom. | Laat autofoto's professioneel bewerken door Wespi. Achtergrond verwijderen of vervangen, digitale showroom, kentekenplaten en logo's. Vraag een offerte aan. | https://www.wespi.nl/beeldbewerking/automotive |
| `/data/productdata` | Productdata verwerken en verrijken voor webshops \| Wespi | Veel producten. Veel data. Wij regelen het. | Wespi verwerkt en structureert leveranciersgegevens voor webshops, vult productdata aan vanuit betrouwbare bronnen en maakt producttitels en omschrijvingen. | https://www.wespi.nl/data/productdata |
| `/slimmer-werken` | Slimmer werken \| Automatisering en praktische digitale oplossingen \| Wespi | Minder handwerk. Slimmer geregeld. | Minder handmatig digitaal werk. Wespi maakt praktische oplossingen voor teksten, Excel, bestanden, beeldverwerking en terugkerende digitale werkzaamheden. | https://www.wespi.nl/slimmer-werken |
| `/over-wespi` | Over Wespi \| Beeld, productdata en slimme processen | Van product tot proces. Digitaal goed geregeld. | Maak kennis met Wespi. Ruim 15 jaar ervaring met productinformatie, beeld, marketing, databeheer en praktische digitale processen. | https://www.wespi.nl/over-wespi |
| `/contact` | Contact \| Wespi – Samen aan de slag? | Samen aan de slag? | Neem contact op met Wespi over productfotografie, productdata of slimmer werken. We denken graag met je mee. | https://www.wespi.nl/contact |
| `/offerte` | Offerte aanvragen \| Wespi | Vertel ons wat je nodig hebt. | Vraag vrijblijvend een offerte aan bij Wespi voor kledingfotografie, productfotografie, beeldbewerking, productdata en digitale oplossingen. | https://www.wespi.nl/offerte |
| `/privacyverklaring` | Privacyverklaring \| Wespi | Privacyverklaring | Privacyverklaring van Wespi. | https://www.wespi.nl/privacyverklaring |
| `/algemene-voorwaarden` | Algemene voorwaarden \| Wespi | Algemene Voorwaarden Wespi | Algemene voorwaarden van Wespi. | https://www.wespi.nl/algemene-voorwaarden |
| `/beeldbewerking` | Beeldbewerking & fotobewerking uitbesteden \| Wespi | Beeldbewerking professioneel uitbesteed. | Professionele beeldbewerking en fotobewerking voor kleding, producten en automotive. Van enkele foto's tot grotere aantallen beelden. | https://www.wespi.nl/beeldbewerking |

Descriptions uit multiline templates zijn voor deze tabel genormaliseerd. Deze inventaris is een vergelijking, geen nieuwe tekst- of titeloptimalisatie.

## 6. Publieke Google-informatie en benodigde Search Console-gegevens

### 6.1 Wat publiek is vastgesteld

Via de openbare zoektool kwamen onder andere [home](https://www.wespi.nl/), [kledingfotografie](https://www.wespi.nl/productfotografie/kledingfotografie), [packshotfotografie](https://www.wespi.nl/productfotografie/packshotfotografie), [diensten](https://www.wespi.nl/diensten), [beeldbewerking](https://www.wespi.nl/beeldbewerking), [autobewerking](https://www.wespi.nl/beeldbewerking/auto), [overons](https://www.wespi.nl/overons), [contactus](https://www.wespi.nl/contactus), privacy en voorwaarden als zoekresultaat naar voren. Die links zijn ook rechtstreeks op de huidige host onderzocht.

Dit is **geen Google-indexexport en geen rankingmeting**. Een rechtstreeks GET-verzoek aan Google voor site:wespi.nl werd met HTTP 302 naar consent.google.com doorgestuurd; een directe Google-resultatenlijst kon vanuit die route niet worden beoordeeld. Er is geen toestemming-/loginbarrière omzeild.

Er worden daarom geen aantallen geïndexeerde pagina's, bezoekers, klikken, vertoningen of posities genoemd. Een zoektoolresultaat of sitemapvermelding is geen bewijs van actuele Google-indexering. Ook een technisch indexeerbare pagina kan door Google niet geïndexeerd zijn of een andere canonical toegewezen krijgen.

### 6.2 Benodigde exports of alleen-lezen toegang

Geen wachtwoorden delen. Alleen-lezen toegang tot de bestaande relevante Search Console-property of onderstaande exports volstaat.

| Gegeven | Benodigde uitsplitsing | Doel / moment |
| --- | --- | --- |
| Zoekprestaties | Zo lang beschikbaar, bij voorkeur tot 16 maanden; aanvullend laatste 3 maanden; klikken, vertoningen, CTR en gemiddelde positie per zoekopdracht én pagina, liefst ook de combinatie | Vóór livegang nulmeting en prioritering van oude bestemmingen. |
| Best presterende pagina's | Alle landingspagina's met verkeer, niet alleen de navigatie-URL's; apparaat/land waar nuttig | Vóór livegang verweesde/historische URL's toevoegen aan mapping. |
| Afbeeldingenzoeken | Zoektype Afbeelding, betrokken pagina's en waar beschikbaar verwijzende media/loggegevens | Vóór uitschakelen Odoo beoordelen of /web/image-URL's waardevol verkeer ontvangen. |
| Pagina-indexering | Geïndexeerd/niet geïndexeerd en redenen, voorbeelden/exports | Vóór livegang vaststellen welke URL's Google werkelijk kent; daarna wijzigingen volgen. |
| URL-inspectie | Home, kleding, packshot, beeldbewerking, productfotografie, platte fotografie, studio, overons en contactus; user-/Google-selected canonical en laatste crawl | Vóór livegang nulmeting, daarna oude/nieuwe doel-URL's steekproefsgewijs controleren. |
| Links | Meest gelinkte pagina's en externe verwijzingen, met aandacht voor te vervallen routes | Vóór livegang redirectprioriteiten en eventueel media-URL's bepalen. |
| Sitemapstatus en verificatie | Bestaande ingediende sitemaps, fouten/laatste uitlezing en gebruikte eigendomsverificatie | Vóór omschakeling verificatie behouden; nieuwe sitemap na livegang indienen. |

[Google beschrijft de prestatiematen in het Search Console-prestatierapport](https://support.google.com/webmasters/answer/7576553) en de indexeringsinformatie in het [Pagina-indexeringsrapport](https://support.google.com/webmasters/answer/7440203).

Ontbrekende GSC-toegang verhindert het voorstellen van de hier al aangetoonde redirects niet. Voor een volledig onderbouwd behoud van bestaande vindbaarheid zijn de exports wel belangrijk. Als ze niet beschikbaar komen, moet het restrisico op onbekende URL's en zoektermen expliciet worden geaccepteerd; verzin geen cijfers als vervanging.

## 7. Nieuwe sitemap en productie-indexeerbaarheid

### 7.1 Sitemap

De huidige nieuwe sitemap bevat **15** canonieke publieke URL's. De nieuwe goedgekeurde site heeft **16** publieke pagina's. **/beeldbewerking ontbreekt.**

Concreet verbeterpunt vóór publicatie: voeg de bestaande overzichtspagina aan de sitemapbron PUBLIC_PAGES in siteconfig.py toe. Niet uitgevoerd. De overige 15 sitemapbestemmingen geven lokaal 200 en hebben passende canonicals. Alleen definitieve 200-eindbestemmingen opnemen, geen oude redirectadressen of URL-fragmenten.

Correct aanwezig: home, /beeld, kledingfotografie, packshotfotografie, AI-modelfotografie, productbeeldbewerking, kledingbeeldbewerking, automotive, productdata, Slimmer werken, Over Wespi, Contact, Offerte, privacy en voorwaarden.

Correct uitgesloten: /slimmer-werken-v2, de bestaande noindex-testpagina. Dat is geen ontbrekende commerciële pagina.

### 7.2 Productie versus lokaal

De in-memory productiesimulatie gaf:

    User-agent: *
    Allow: /
    Sitemap: https://www.wespi.nl/sitemap.xml

De 16 goedgekeurde pagina's hadden in die simulatie geen algemene X-Robots-Tag-noindex of robots-meta-noindex. V2 behoudt zijn eigen noindex, nofollow.

De standaardomgeving is development. Daar geeft robots.txt Disallow: / en worden antwoorden voorzien van X-Robots-Tag: noindex, nofollow. Dit is lokaal correct maar mag niet op de publieke productiehost blijven staan. WESPI_ENV=production moet in het werkelijke serverproces beschikbaar zijn; een los .env-bestand wordt niet automatisch geladen.

Deze simulatie bewijst de applicatielogica, niet de inrichting van de toekomstige hosting/proxy. Controleer op de echte productiehost direct vóór de publieke omschakeling dat HTTP-statussen, headers, robots en canonicals overeenkomen. Laat staging afgeschermd en zet niet om SEO-redenen alle ontwikkelomgevingen open.

Redirects, canonicals, interne links en sitemap moeten dezelfde eind-URL's aanwijzen. Canonicalisatie is een signaal, geen vervanging voor een benodigde oude-URL-redirect. Zie [Google: canonical-methoden](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## 8. Concrete acties en timing

| Nr. | Actie | Verplicht vóór publicatie of later? | Acceptatie |
| --- | --- | --- | --- |
| P1 | De acht ontbrekende inhoudelijke 301's uit 3.1 goedkeuren, implementeren en testen; drie bestaande behouden | **Verplicht vóór publicatie** | Alle oude paden, ook slashvormen, eindigen direct op relevante 200-bestemming. |
| P2 | Behoud/verval van rendering, vriendenprogramma, aanvraag en technische Odoo-functies bevestigen | **Verplicht vóór publicatie** | Per oud adres een bewust 301-/404-/410-/apart-toegangbesluit; geen blind homepagevangnet. |
| P3 | Padbehoud, www/HTTPS en slashnormalisatie op gekozen host regelen | **Verplicht vóór publicatie** | Geldig certificaat voor beide hostnamen, geen padverlies, geen loops en geen vermijdbare ketens. |
| P4 | /beeldbewerking toevoegen aan nieuwe sitemap | **Vóór publicatie uitvoeren als concrete migratieverbetering** | Sitemap bevat de 16 goedgekeurde eindpagina's; V2 blijft uitgesloten. |
| P5 | Werkelijke productie-indexeerbaarheid en canonicals controleren | **Verplicht vóór publiek omschakelen** | WESPI_ENV=production in serverproces, geen algemene crawl-/noindexblokkade op live, correcte HTTPS-www-canonicals. |
| P6 | Oude URL-/media-export, GSC-verificatiemethode en beschikbare prestaties veiligstellen | **Vóór publicatie/Odoo-uitschakeling** | Zoek-/linkrijke oude adressen toegevoegd aan mapping, verificatie blijft werken. Bij ontbrekende data restrisico expliciet accepteren. |
| P7 | Oude back-up, exacte nieuwe release en rollbackpad bewaren | **Verplicht vóór publicatie** | Bij foutieve redirect/indexering terug kunnen schakelen zonder oude gegevens te verliezen. |
| L1 | Na omschakeling de mapping en alle vier host-/protocolvarianten opnieuw vanaf publieke host testen | **Direct na publicatie** | Redirects geven echte 301, doelen 200, geen 404 op verhuisde relevante routes. |
| L2 | Nieuwe sitemap in Search Console indienen en oude sitemapstatus volgen | **Direct na publicatie** | Google kan de nieuwe URL-set ophalen; geen staginghost of redirect-URL's in sitemap. |
| L3 | URL-inspectie van belangrijkste nieuwe en behouden pagina's | **Na publicatie** | Google kan live pagina ophalen; canonical/indexering volgen zonder aantallen te verzinnen. |
| L4 | 404-/serverlogs en belangrijkste externe profiel-/campagnelinks controleren | **Dagelijks in eerste week, daarna periodiek** | Onbekende relevante oude URL's gericht afhandelen; geen willekeurige fallbackredirects. |
| L5 | Zoekopdrachten, landingspagina's, klikken, vertoningen en posities vergelijken | **Na 1, 2 en 4 weken; vervolgens maandelijks** | Zelfde perioden/filters vergelijken, rekening houden met seizoenen en vertraagde gegevens. |
| L6 | Redirects langdurig behouden en belangrijkste externe links waar mogelijk laten aanpassen | **Minimaal circa één jaar volgen; liever blijvend behouden** | Oude backlinks blijven bruikbaar; nieuw intern verkeer gebruikt direct eind-URL's. |

Er vindt geen domeinverhuizing plaats zolang https://www.wespi.nl de canonical host blijft. De Search Console-tool Adreswijziging is daarom niet nodig voor deze hosting-/CMS- en padmigratie. Zie [Google: wanneer Adreswijziging niet gebruiken](https://support.google.com/webmasters/answer/9370220).

## 9. Beslisbare conclusie

De bestaande vindbaarheid is **nog niet voldoende beschermd door de huidige lokale routeconfiguratie**. Dat is nu concreet onderbouwd met de live sitemap, oude interne links en gemeten nieuwe 404's, niet met veronderstelde rankings.

De belangrijkste bestaande dienst-URL's en zoekintenties zijn wél goed te behouden. Met het redirectplan, bewuste afhandeling van vervallen onderwerpen, correct TLS/hostpadbehoud en productie-indexeerbaarheid is een verantwoorde migratie mogelijk. Voor commerciële rendering-/vriendenprogramma-URL's en onbekende Google-/backlinkbestemmingen blijven aanvullende besluiten of gegevens nodig. Een correcte migratie beperkt het risico, maar kan een tijdelijke zichtbaarheidsschommeling door het al goedgekeurde herontwerp niet uitsluiten.

**Alleen dit rapport is aangemaakt. Alle redirects en codewijzigingen in dit document zijn voorstellen en wachten op een volgende expliciete opdracht.**
