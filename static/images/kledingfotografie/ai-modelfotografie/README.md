# Media AI-modelfotografie

De bestaande hero blijft `ai-modelfotografie-hero.jpg`.

Sinds 7 november 2026 staat de modelindeling in `routes/ai_modellen.json`. De route leest dit bestand; de template geeft dezelfde gegevens als veilig geserialiseerde JSON aan de galerij door.

Per model staan de aangeleverde WebP-bestanden met ongewijzigde namen in `static/images/herenmodel/`, `damesmodel/`, `jongensmodel/`, `meisjesmodel/` en `zwangerschapsmodel/`. De ondermap `preview/` bevat proportioneel verkleinde WebP-versies van maximaal 480 × 720 pixels. De vijf ongewijzigde MP4-bestanden staan onder `static/videos/<model>/`.

De pagina toont een stilstaand videovoorbeeld en twee modelfoto's per model. Een videobron wordt pas bij het openen van de speler aangemaakt. Een klik op de afspeelknop start gedempt; de bezoeker kan geluid via de normale videobediening inschakelen. Bij bladeren naar een video verschijnt een gepauzeerde speler. Sluiten of bladeren stopt de video en verwijdert de bron.

De donkere galerij bevat per model eerst de video, vervolgens alle modelbeelden en daarna de bijbehorende oorspronkelijke productfoto's, herkenbaar aan het bijschrift. Pijlen, toetsenbord, Escape, focusherstel en horizontale veegbewegingen worden ondersteund. Afbeeldingen blijven volledig zichtbaar zonder vervorming of wit dialoogkader.

De oude video `ai-model-01-video.mp4` en poster `ai-model-01-poster.jpg` zijn verwijderd na controle op actieve verwijzingen. De oude voor-/achterfoto's en hun varianten blijven behouden: de voorkant wordt nog op Kledingfotografie gebruikt, en beide series staan in het bestaande gedeelde beeldregister. Dat register en andere pagina's zijn niet aangepast.

Prijzen blijven centraal in `AI_MODELFOTOGRAFIE_TARIEVEN` in `routes/paginas.py`.
