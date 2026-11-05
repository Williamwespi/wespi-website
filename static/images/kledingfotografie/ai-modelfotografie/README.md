# Media AI-modelfotografie

Hero: `ai-modelfotografie-hero.jpg`. De pagina gebruikt een uitsnede vanaf de bovenzijde, afzonderlijk ingesteld voor desktop en mobiel.

De centrale lijst `voorbeelden` in `ai_modelfotografie` (`routes/paginas.py`) bereidt vijf modellen voor. Alleen modellen met bestaande media worden getoond; ontbrekende onderdelen blijven verborgen.

Voor elk nummer 01 t/m 05:
- `ai-model-01-video.mp4`: verticale, webgeschikte MP4; bij voorkeur H.264 met faststart.
- `ai-model-01-voor.jpg`: foto van de voorkant.
- `ai-model-01-achter.jpg`: foto van de achterkant.
- `ai-model-01-poster.jpg`: optionele poster; anders wordt de voorkant gebruikt.

Vervang 01 door het modelnummer. Afbeeldingen worden zonder vervorming weergegeven. Kaarten laden de video niet vooraf (`preload="none"`); alleen de vergrote speler gebruikt `preload="metadata"`. Sluiten stopt de video en verwijdert de bron. De medialinks werken ook zonder JavaScript.

De poster voor Model 01 is een frame op 3,2 seconden uit de bestaande video, verkleind naar 600 pixels breed. De tariefsectie hergebruikt `ai-model-01-voor.jpg` als aanvullend sfeerbeeld links, met zachte overgangen naar de witte achtergrond.

Prijzen blijven centraal in `AI_MODELFOTOGRAFIE_TARIEVEN` in `routes/paginas.py`.
