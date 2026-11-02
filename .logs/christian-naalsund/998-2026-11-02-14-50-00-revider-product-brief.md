# Revider product brief

## 2026-11-02 kl. 14:50 — Christian Naalsund

### Oppgave
Revidere `docs/product-brief/brief.md` etter faglærers tilbakemelding (2026-10-06), slik at briefen kan brukes som grunnlag for PRD.

### Plan
- Gå gjennom punktene i `docs/product-brief/tilbakemelding-product-brief.md` og dekke hvert av dem i briefen.
- Føre beslutningene i `docs/product-brief/.memlog.md`.

### Resultat
- `brief.md` (status `revised`): nytt sammendrag, brukssituasjon, brukerflyt i seks steg, utkast til tabell over tre feil (early extension, loss of posture, over the top) med måling, feilkjede, drill og mobilitetsøvelse, 8 testbare suksesskriterier, kvalitetssikring (testvideoer med fasit, regler som tabeller, LLM-testmodus), «ikke med»-liste, ny fasetabell og oppdaterte åpne spørsmål.
- Kurs-MVP avgrenset til én down-the-line-video, lokal 2D-positur og tre regelbaserte feil. Fri chat, face-on og 3D flyttet til senere faser.
- `.memlog.md` oppdatert med beslutningene.
- Endringene i `brief.md` og `.memlog.md` er ikke committet.

### Åpne punkter
- Bekreft valget av de tre feilene og drill/mobilitet per feil (utkast laget av Claude).
- Skriv egen golfbakgrunn i briefen (grunnlag for å vurdere fasit på testvideoene).
- Legg opplastingsmappen for brukervideoer i `.gitignore` når teknologistakken er valgt.
