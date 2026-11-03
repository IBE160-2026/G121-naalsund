# Teknisk recon: 2D-positur for svingfeil

## 2026-11-03 kl. 16:35 — Christian Naalsund

### Oppgave
Før PRD-en lages: finn ut hva PRD-en kan love om terskler, konfidensregler og hastighet når early extension, loss of posture og over the top skal oppdages fra én DTL-video med lokal 2D-positur. Brukeren ba også om at D1 skulle sjekke hvordan toppkonkurrentene gjør posituranalysen.

### Plan
- Kjørte `bmad-deep-recon`, type `technical`, preset `standard`, validering `normal`. Planen ble godkjent av brukeren.
- Dimensjoner:
  - D1: posemodeller (MediaPipe / RTMPose / YOLO-pose) og konkurrentene.
  - D2: bildefrekvens og normalisering.
  - D3: svingfaser.
  - D4: terskler.
- Runde 1: tre forskere parallelt. Runde 2: to forskere som verifiserte og fulgte opp spor. I tillegg gjorde jeg et eget oppslag på konkurrentene, fordi runde 2 gikk tom for budsjett på det spørsmålet.
- Avslutning:
  - sitatsjekk, både mekanisk og innholdsmessig
  - struktur- og språkgjennomgang med `bmad-review`
  - HTML-briefing

### Resultat
- Mappe: `docs/research/technical-2d-pose-golf-swing-fault-detection-2026-11-03/`, med `research.md`, `research-briefing.html`, `digests/` (6 digests og en sitatsjekk) og `.memlog.md`.
- Hovedfunn:
  - De eneste talltersklene som finnes, står i et Acushnet-patent (US12608853B1, 2026): early extension over ca. 6 in (3–6 er «potential»), loss of posture over 10° (5–10° er «potential»), og over the top over ca. 3 in over impact-planlinjen. Dette er startverdier som må tilpasses, ikke normer.
  - Keypoint-scorene fra modellene er ikke kalibrerte. Konfidens må bygges som en sammensatt verdi og testes mot testsettet.
  - Hastighetsmålet under 2 minutter er sannsynlig hvis klippet trimmes til selve svingen, men det må måles på egen laptop.
  - Over the top er det svakeste leddet, fordi både definisjonen og regelen krever køllen.
  - Filmeguiden bør kreve 120/240 fps. Svingfaser kan finnes med håndleddsheuristikk (Yamamoto 2023), med SwingNet som reserve.
  - Ingen konkurrent oppgir posemodell eller har publisert validering fra DTL.
- Påstander: 5 verifisert og 7 uverifisert av 12 bærende. Sitatsjekk: 7 støttet og 2 delvis støttet. Ordlyden ble rettet for de to.

### Åpne punkter
- Uke 1-spike: benchmark MediaPipe Full/Heavy mot RTMPose-m på egen laptop og egne DTL-klipp, både hastighet og stabilitet i hofter, skuldre og håndledd.
- Merk svingfaser (adresse, topp og treff) i testvideoene, for å måle hvor nøyaktig håndleddsheuristikken er.
- Avgjør i PRD-en hvordan over the top skal håndteres: håndbane-proxy med maks middels konfidens, køllelinje som stretch-mål, eller bytte til sway.
- Film testvideoene i 120/240 fps, med god belysning og kamera i håndhøyde på hand line.
- Ikke siter «70 % av amatører har early extension» i PRD-en. Det finnes ingen primærkilde.
