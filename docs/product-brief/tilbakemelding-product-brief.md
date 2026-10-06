# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G121 – G121-naalsund |
| **Product brief** | `docs/product-brief/brief.md` (commit `7dcedd4`), lest sammen med `addendum.md` i samme mappe |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Bør revideres før dere går videre.** Rett punktene markert «Endre» før dere lager PRD og arkitektur.

**Det som er bra:**

1. Idéen har en tydelig og interessant kjerne: «fault chains» – i stedet for en flat liste med avvik skal AIcoach forklare årsak og virkning, for eksempel at «early extension» skyldes begrenset hoftedreining, slik en trener resonnerer. Det er et godt svar på svakheten dere peker på hos eksisterende apper: de «measure well but leave the player to interpret graphs».
2. Dere er ærlige om begrensningene: hver måling skal vise et konfidensnivå, appen påstår ikke launch-monitor-presisjon, mobilitetsråd er generelle og ikke medisinske, og golfreglene forbyr KI-råd under turneringsrunder. Fasetabellen skiller også tydelig mellom kurs-MVP, første ekte lansering og senere.

**De viktigste endringene:**

1. Skriv suksesskriterier. Briefen har ingen – de står bare som et åpent spørsmål («measurable swing improvement, or weekly return rate?»). Begge disse er vanskelige å måle i emnet. Skriv funksjonelle, testbare kriterier, for eksempel «for en testvideo med tydelig early extension viser appen denne feilen med årsak, én drill og én mobilitetsøvelse» og «en ny video kan sammenlignes med den forrige for minst én måling».
2. Avgrens den tekniske kjernen i kurs-MVP-en. 3D-positur fra to telefonvideoer, en samtalebasert trener, feilkjeder, historikk og innlogging er mye for en gruppe på én person, og teknologien for positur er fortsatt et åpent spørsmål. Start med 2D-positur fra én vinkel, et lite, fast sett med feil (for eksempel tre) og en regeltabell for feilkjeder som du selv har skrevet, og la språkmodellen forklare resultatet.
3. Beskriv hvordan du skal kontrollere at analysen er riktig. Hvis ingen kan avgjøre om appen har funnet riktig feil, blir kvalitetssikringen svak. Lag et lite sett med testvideoer der du (eller en trener) har bestemt fasit på forhånd, og bruk dem som tester.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 5) KI-styrt sensurering av eksamensoppgaver (vanskelig). Som sensureringsforslaget skal AIcoach vurdere en prestasjon mot faglige kriterier, begrunne vurderingen og gi råd – her med videoanalyse og positurestimering i tillegg. Avgrenset til 2D-positur, få feil og en fast regeltabell vil prosjektet ligge nærmere middels.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Golfbiomekanikk: måling av vinkler og bevegelser i svingen, terskler for feil, og årsakskjeder mellom feil. Må være faglig riktig. |
| Datamodell – antall entiteter og relasjoner mellom dem | Middels | Bruker, video, analyse med målinger og konfidens, feil, feilkjede, drill/øvelse og samtalehistorikk. |
| Brukere, roller og innlogging | Middels | Én rolle, men konto og privat videohistorikk per bruker. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Høy | Positurestimering (maskinlæring) pluss en samtalebasert trener som skal forklare feil og foreskrive øvelser – uten å gi feil eller skadelige råd. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Middels | Positurbibliotek og språkmodell. Launch-monitor og abonnement er klokt holdt utenfor kurs-MVP-en. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Ingen sanntid mellom brukere. Videobehandling kan ta tid, men skjer per bruker. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Høy | Opplasting, lagring og behandling av videoer fra to vinkler. Store filer og tung prosessering. |
| Sikkerhet og personvern | Høy | Videoer av personer og en «coaching memory» er personopplysninger. GDPR er nevnt som åpent spørsmål. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig – én video fra én vinkel, tre feil med regelbaserte feilkjeder, én drill og én øvelse per feil, og en forklaring fra KI – og legg resten i tydelige trinn etterpå.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Stor risiko | Kurs-MVP-en har sju deler, der positur fra to vinkler og samtalebasert trener hver er store. Med én person og frist tidlig i desember må omfanget ned. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Briefen er kort og mangler suksesskriterier, beskrivelse av brukerflyten og valg av positurteknologi. PRD-en vil få store hull. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | Risiko | Webapp, innlogging og LLM-kall er godt dokumentert. Positurestimering og videobehandling er mer nisjepreget og krever mer manuell testing. Velg et etablert bibliotek (for eksempel MediaPipe) tidlig. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Stor risiko | Krever golffaglig kunnskap for å avgjøre om feilen og årsaken er riktig. Hvis du har den kunnskapen, er det en styrke – skriv det i briefen. Uten testvideoer med fasit kan ingen kontrollere resultatet. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Regler for feil og feilkjeder kan testes når de er skrevet ned som terskler og tabeller. I dag finnes ingen suksesskriterier å teste mot. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Ikke beskrevet. Planlegg at positur kjøres lokalt uten betalt tjeneste, legg ved testvideoer, og lag testmodus for språkmodellen. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Språkmodell for samtale og forklaring koster penger, og en eventuell skytjeneste for positur også. Ingen plan for kostnad eller testmodus ennå. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Definer kurs-MVP-en som: last opp én video fra én vinkel → 2D-positur med et etablert bibliotek → oppdag tre bestemte feil med regler du selv har skrevet → vis feilkjede, én drill og én mobilitetsøvelse fra et fast bibliotek → la KI forklare dette i klart språk. Flytt to vinkler, 3D og den frie samtalen til neste trinn.
2. Behold historikk og sammenligning av to videoer som andre trinn i kurset hvis tiden tillater det, men vent med «cue memory» og swing score til etter kurset, slik du allerede har planlagt.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | Juster | Det finnes ingen egen sammendragsdel, men «Problem» og «Vision» forklarer idéen. Legg til et kort sammendrag øverst. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Konkret om dyre timer, egentrening fra video og at «feel and reality often disagree». |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | Endre | Løsningen står delvis under Vision. Beskriv brukerflyten steg for steg: hvordan spilleren filmer, laster opp, får resultatet og bruker øvelsene. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Feilkjeder, «cue memory» og ærlig måling er tydelige poenger, og konkurrentene (Sportsbox AI, Zepp, DeepSwing, HackMotion) er kartlagt i addendumet. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | OK | Golfere med handicap mellom +2 og 15 uten fast trener er en konkret primærbruker. «Also usable by everyone» kan droppes for v1. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Endre | Mangler helt. Skriv funksjonelle, testbare kriterier for analyse, forklaring og historikk. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Juster | Fasetabellen er tydelig, men kurs-MVP-en er for stor. Avgrens den, og legg til en eksplisitt «ikke med»-liste. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | Juster | «Replaces the coach … at every level» er en stor visjon. Den er greit plassert, men skill den tydeligere fra løsningsbeskrivelsen for v1. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Endre | Briefen er for kort på løsning og suksesskriterier til at PRD og stories kan bygges direkte på den. Revider den først. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Endre | Kurs-MVP-en er for stor for én person. Én video, én vinkel og få feil gir en kjerneflyt som kan bli stabil. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Endre | Ingen suksesskriterier ennå. Lag testvideoer med fasit og skriv reglene for feil som terskler. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Primærbrukeren er tydelig. Beskriv brukssituasjonen (på rangen med telefonen?) og skissér opptaksveiledning og resultatvisning. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | Juster | Teknologistakk og positurmetode er åpne. Velg et etablert bibliotek og en enkel arkitektur, og hold analyse-reglene i en egen, testbar modul. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Planlegg lokal positur, testvideoer i repoet og testmodus for språkmodellen, slik at sensor kan kjøre appen uten dine nøkler. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Ikke beskrevet. Bruk `.env.example`, bruk bare videoer du har samtykke til å publisere (for eksempel av deg selv), og hold opplastede brukervideoer utenfor Git. |

## 3. Neste steg for gruppen

1. Legg til et sammendrag, en løsningsbeskrivelse med brukerflyt og 5–8 testbare suksesskriterier i briefen.
2. Avgrens kurs-MVP-en (én vinkel, 2D-positur, tre feil med regelbaserte feilkjeder) og legg til en «ikke med»-liste.
3. Velg positurbibliotek og teknologistakk i arkitekturen, og lag et lite sett med testvideoer med fasit som du kan bruke gjennom hele prosjektet.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
