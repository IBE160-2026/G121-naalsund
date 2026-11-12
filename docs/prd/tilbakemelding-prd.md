# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G121 – G121-naalsund |
| **PRD vurdert** | `docs/prd/prd.md` (status: final, sist endret 2026-11-03, commit 4e15813), lest sammen med `addendum.md` |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

Dette er en sterk PRD med en tydelig tese: AIcoach skal si hva feilen er, hvor sikker appen er, og når den ikke vet. Flere av hovedpunktene fra briefen er fulgt opp med substans, ikke bare overskrifter. Risikoen ligger i tre ting: den «uverifiserte observasjonen» er ikke spesifisert godt nok til å testes, flere FR-er mangler egne testbare konsekvenser, og omfanget er stort for én person med omtrent fem uker igjen til 2026-12-15.

## 2. Dette fungerer godt

- **Ærlighet bygget inn i kravene.** «Cannot analyse» (FR-8), «No verified fault found» (FR-12), konfidensnivå på hver måling (FR-7) og taket «Over the top is capped at "medium"» viser at dere har tenkt gjennom hva appen ikke vet. Det gir testere noe konkret å sjekke.
- **KI-kontroll og kjørbarhet.** Språkmodellen «explains; it never decides» (§4.6), får bare målinger, har en automatisk grounding-sjekk (FR-14), malbasert reserveforklaring (FR-14) og mock mode (FR-15, NFR-4). Skille mellom tuning set og evaluation set (§10) er riktig kvalitetssikringstenkning.
- **Reelle beslutninger og motmål.** Bygg- og kuttrekkefølgen P1–P3 (§8.1), reservevalget «sway» med frist 2026-12-08 (§4.4) og SM-C1–C3 viser avveininger, ikke bare ønsker. `[NOTE FOR PM]` om det lille utvalget (4 klipp per feil) er et ærlig flagg.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | sterk | Valg, reservevalg og åpne spørsmål er synlige og reelt åpne (§11). |
| Substans | sterk | Terskler, kilder og avgrensninger er produktspesifikke; ingen pynte-personas. |
| Strategisk sammenheng | sterk | Alt tjener «ærlig coach»-tesen; målene måler tesen. |
| Testbarhet | god | Mange gode konsekvenser, men FR-12, FR-9 og FR-16 mangler egne, og FR-13 kan ikke testes slik den står. |
| Scope og avgrensning | god | Utelatelser og kuttrekkefølge er eksplisitte, men samlet omfang er stort for én person. |
| Brukbarhet for neste fase | god | Glossar, ID-er og `Realizes UJ-x` er på plass; noen overlapp og manglende begreper. |
| Formtilpasning | sterk | UJ-er med navngitte personer passer en forbrukerapp; UJ-2 til UJ-6 er korte, og det er greit. |

## 4. Viktigste forbedringer

### 4.1 Den uverifiserte observasjonen kan ikke testes slik den er beskrevet
- **Alvorlighet:** høy
- **Hvor:** §4.5, FR-13: «When no verified fault is found, the result always includes one»; UJ-3: «It *may* show an unverified observation»
- **Problem og hvorfor det betyr noe:** UJ-3 sier «may», FR-13 sier «always». Regeltabellen måler bare tre feil, så det er uklart hvilke data observasjonen («weight appears to move toward the trail side») bygger på (åpent spørsmål 2). Grounding-sjekken i FR-14 dekker ikke observasjonen, og i mock mode er den en fast tekst, så den ekte veien testes aldri. «Never repeats or contradicts a verified fault» kan heller ikke sjekkes automatisk. Dette er den eneste delen der KI fritt kan finne på påstander.
- **Forslag:** Velg ett av to. (a) Gjør observasjonen valgfri/stretch. (b) Definer den lukket: en liten fast liste over tilleggsmålinger (f.eks. vektforflytning) med hver sin tekstmal, der språkmodellen bare omformulerer. Eksempel-FR: «Når en tilleggsmåling overstiger sin terskel, viser resultatet nøyaktig én observasjon bygget på den målingen, merket "Unverified", med konfidensnivå low og uten drill. Når ingen tilleggsmåling overstiger terskelen, vises ingen observasjon.»

### 4.2 Flere FR-er har SM-henvisninger i stedet for testbare konsekvenser
- **Alvorlighet:** høy
- **Hvor:** FR-12 («Meets SM-2 and SM-3»), FR-9 («Detection meets SM-1 and SM-2»), FR-16 (ingen konsekvenser)
- **Problem og hvorfor det betyr noe:** En SM er en målestokk over mange klipp, ikke et testtilfelle. Stories og tester trenger en betingelse per FR.
- **Forslag:** FR-12: «For en testvideo der alle tre målinger ligger under potential threshold viser resultatet teksten "No verified fault found", ingen feilkjede, drill eller mobilitetsøvelse, og forklaringen nevner ingen av de tre feilene.» FR-16: «Etter to fullførte analyser viser listen begge, nyeste først, og hver kan åpnes.»

### 4.3 Toleransen i FR-6 passer ikke med 30 fps-gulvet i FR-8
- **Alvorlighet:** medium
- **Hvor:** FR-6: «impact lies within ±20 ms»; FR-8: «at least 30 fps are analysed»
- **Problem og hvorfor det betyr noe:** Ved 30 fps er ett bilde 33 ms, så ±20 ms er under ett bilde og kan ikke oppnås. Testen blir enten umulig eller meningsløs for klipp under 120 fps.
- **Forslag:** Uttrykk toleransen i bilder («impact within ±1 frame, top within ±2 frames») eller begrens tidstoleransen til klipp ved 120 fps eller mer. Addendum §A nevner allerede ±1 bilde.

### 4.4 Omfanget er stort for én person og fem uker
- **Alvorlighet:** medium
- **Hvor:** §8.1; 19 FR-er inkl. konto, sletting, svinglibrary (FR-18–19) og eget merket testsett
- **Problem og hvorfor det betyr noe:** Svinglibrary lagrer video og drar med seg samtykke, lagringsgrense og sletting, altså akkurat den personvernbyrden §6.1 ellers unngår. Briefen anbefalte historikk som andre trinn. Kuttrekkefølgen er god, men uten sjekkpunkter kommer kuttet for sent.
- **Forslag:** Sett datoer som for over the top/sway, for eksempel «P1 ferdig og testet innen 2026-12-01; først da starter P2». Vurder å bytte rekkefølge slik at P2 er enten svinglibrary eller historikk, ikke begge. Avklar også forskjellen på FR-16 (liste over analyser) og FR-19 (liste over lagrede klipp).

### 4.5 Reservevalget «sway» er ikke klart, og terskelgrunnlaget er svakt for to av tre feil
- **Alvorlighet:** medium
- **Hvor:** §4.4 Notes; addendum §B; SM-5
- **Problem og hvorfor det betyr noe:** Sway finnes ikke i regeltabellen (ingen måling, årsak, drill eller øvelse), så byttet 2026-12-08 kan ikke gjøres uten nytt arbeid. Over the top er definert på køllestaven, men måles på håndbanen. Vinkelfeilen for posture (~9–10°) er like stor som terskelen. SM-5 («correct more often») sier ikke hvor mange klipp som trengs.
- **Forslag:** Legg sway som rad i tabellen nå, merket «reserve». Skriv hva som skjer hvis to av tre feil ikke når SM-1. Sett en minstegrense for SM-5, eller si at den bare rapporteres beskrivende.

## 5. Mekaniske funn

- ID-ene er sammenhengende og unike (UJ-1–6, FR-1–19, SM-1–12 og SM-C1–C3, NFR-1–7). Assumptions Index stemmer med de innebygde taggene.
- Glossar: «visitor» (FR-1), «examiner», «history» og terskelbegrepene «potential threshold»/«fault threshold» brukes uten å være definert. «Rest of the bucket» (UJ-1) er uformelt.
- UJ-3 («may») og FR-13 («always») er i konflikt (se 4.1).

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:**
- Hva observasjonen bygger på, og om den er med i MVP (4.1; åpent spørsmål 2).
- Toleranse i bilder i stedet for ms (4.3), og hvilke FR-er som er P1 med hard dato (4.4).
- Rad for sway i regeltabellen (4.5) og målingsdefinisjon for early extension og posture (åpent spørsmål 3).

**Kan vente:** kostnad per analyse med ekte språkmodell (§6.3 sier «known, small», men ikke hvilken modell eller grense), lagringsgrensen i svinglibrary, trenerverifisering av merkingen (åpent spørsmål 1), konkurrentkontroll 2026-12-01.

**Oppfølging av brief-tilbakemeldingen: ja.** Suksesskriterier (SM-1–12), avgrenset kjerne (én vinkel, tre feil, regeltabell), testsett med fasit, lokal kjøring og mock mode er alle på plass. Skisser av filmingsveiledning og resultatskjerm ligger til UX-fasen. Historikk ble stretch, men svinglibrary er nytt omfang.

## 7. Refleksjonsspørsmål

1. Terskelverdiene kommer fra ett patent (addendum §B). Hvordan vil dere kontrollere at KI-hjelpen ikke har tolket patentet feil, og hva gjør dere hvis egne klipp motsier tallene?
2. Observasjonen er der språkmodellen har mest frihet. Hva i PRD-en hindrer den i å høres sikker ut når den ikke er det, og hvordan ville dere oppdaget det i en test?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
