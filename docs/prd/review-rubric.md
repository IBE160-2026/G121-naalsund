# PRD Quality Review — AIcoach

Calibration: solo student project, a graded IBE160 deliverable and also meant to become a real product. MVP is due 2026-12-15, about six weeks away. The PRD feeds UX, architecture and stories, so done-ness and downstream usability carry the most weight. Rigor expectations are set for a solo MVP, not an enterprise launch.

## Overall verdict
This is a good PRD with a clear and specific thesis: honesty is the product's edge, shown through confidence on every measurement, evidenced fault chains and a refusal to guess. Glossary discipline, non-goals and counter-metrics are better than usual. Three things put it at risk. The success metrics are measured on the same clips the thresholds are tuned on. The borderline "possible" fault state is undefined, and it shapes the result screen and SM-1. Hosting and GDPR are left implicit, even though the user journeys and the teacher feedback both depend on them. With those fixed, plus an explicit cut order for the six-week scope, it is ready for UX and architecture.

## Decision-readiness — adequate
Most choices are stated as decisions, with a reason:
- DTL only, because "one angle keeps the MVP feasible solo in six weeks" (§8.2).
- Hand height replaces the brief's hip height (§4.2 Notes).
- Over the top is capped at medium confidence while there is no club tracking (FR-7).
- A dated fallback swaps over the top for sway "before 2026-12-08" (§4.4 Notes).

The Open Questions are genuinely open, and the two `[NOTE FOR PM]` callouts sit on real tensions (cue memory deferral, and the 3-of-4 sample in §10).

What is missing is the hardest decision for a solo six-week build: what gets cut first if time runs short. §8.1 puts the swing library (FR-18–19) in scope as a full feature. It needs storage, playback, per-clip retention and its own deletion semantics. History and comparison (FR-16–17), which are lighter and serve the same "film again next session" loop, are marked stretch. Nothing says what was given up to fit the library in, or how scope gets ordered when the timeline slips.

### Findings
- **[high]** No cut order for a dense solo scope (§8.1, §4.8) — The MVP bundles auth, local pose, three rule-based faults, a composite confidence band, rejection, an LLM explanation, an unverified observation, the swing library and a labelled test set into six weeks, with no priority tiers. The swing library is in scope while the lighter history feature is stretch, and §4.8 Notes justify it mostly by next-phase use ("natural home for… cue memory"). *Fix:* Add a must / should / stretch ordering to §8.1, with a named cut line (for example "if behind on 2026-12-01, drop FR-13 and FR-18–19 first"). Either justify the swing library against the thesis or move it to stretch.
- **[medium]** Unverified observation conflicts with "the language model explains; it never decides" (§4.5, §4.6, §1) — FR-13 Notes and OQ2 imply the observation comes from the LLM. UJ-3's example ("weight appears to move toward the trail side at the top") is a diagnostic claim the LLM decided on. That cuts against §4.6 and against §1's "refuses to guess". The labelling limits the damage, but the PRD never names the tension. *Fix:* Add a `[NOTE FOR PM]` on this trade-off. Either derive the observation from measurements by rule, or say outright that it is the one place the LLM makes a claim, and why that is acceptable.
- **[low]** OQ1 has no fallback (§11) — "Can a qualified coach check the test-set labels" has no deadline and no stated consequence if the answer is no. In that case labels rest on the author alone. *Fix:* Add a decide-by date and the fallback ("author-only labels; stated as a limitation in the README").

## Substance over theater — strong
There is no persona theater. Rory, Nelly and the examiner each drive specific FRs, and UJ-3 exists to test no-forced-fit. The vision is specific to this product and could not be swapped into another swing app. The differentiation claim ("no competing app shows per-measurement confidence") is backed by the addendum's competitive research (§E), and the PRD honestly flags what is "no longer unique". The NFRs have real thresholds (NFR-1 under 2 minutes, NFR-7 licence rule), and the guardrails in §6.2 are product-specific.

### Findings
- **[low]** "Ordinary laptop" is unspecified (NFR-1, SM-8, UJ-5) — The performance bound depends on a "target machine" that is never described. *Fix:* Name its CPU and RAM (and whether it has a GPU) in NFR-1 or the addendum.

## Strategic coherence — adequate
The thesis is clear and the core features follow from it: confidence bands (FR-7), fault chain evidence (FR-10), rejection (FR-8) and no forced fit (FR-12). The success metrics test the thesis rather than activity, and the counter-metrics SM-C1–C3 are well chosen. SM-C3 in particular guards the confidence band against inflation. Scope is a problem-solving MVP, and it is mostly coherent apart from the swing library noted above.

The weakness is evidential. The metrics that are supposed to prove the thesis are set up so they can pass without proving much.

### Findings
- **[high]** Thresholds are tuned on the same set the metrics measure (§4.4 Description "tuned on the test set", FR-6, OQ3, §10) — SM-1 to SM-3 are evaluated on the same author-filmed clips the thresholds are fitted to. With about 18 clips, that makes detection close to self-fulfilling. It also undercuts "verified" in the product language. *Fix:* Split the clips into a tuning set and a held-out evaluation set (even 2+2 per fault), and state that SM-1 to SM-3 are measured on the held-out clips only. If that isn't possible, state the overlap as a limitation in §10.
- **[medium]** SM-5 can pass without showing anything (§10 SM-5, FR-7) — On a set of roughly 18 clips, there may be no low-confidence verified faults at all. A tie ("at least as often") also passes. So the metric for the product's main differentiator can pass with no evidence. *Fix:* Require at least N verified faults in both the high and low bands (for example by deliberately including degraded clips, such as 30 fps or partly occluded). Or reframe SM-5 as a check that low-quality clips land in medium or low.
- **[medium]** One subject, no check against real users (§10 preamble, §2) — Every clip is of the author, a skilled player who has to produce the faults on purpose. The target users (+2–15 handicap) have different bodies and show faults naturally. For something meant to be a real product, the PRD says nothing about how far the results generalize. *Fix:* State it as a known limitation. Optionally add a secondary SM such as "2–3 other golfers' clips run end-to-end without rejection or crash".

## Done-ness clarity — adequate
Most FRs have concrete, testable consequences: ±2 frames at impact, refusal above 15 s, 30 and 120 fps floors, ID-based access returning not-found, the automated grounding check, the template fallback when the LLM is unavailable, and file absence checked on disk in SM-11. That is better than most PRDs. Two gaps will cause trouble in story writing: the "possible" state and the untested rejection reasons.

### Findings
- **[high]** The "possible" fault state is undefined (FR-9, §12) — FR-9 adds a borderline state ("present, borderline ('possible') or absent"), but the PRD never says:
  - whether a possible fault shows a fault chain, drill and mobility exercise (FR-10, FR-11 say "for each verified fault found");
  - whether it counts as a detection in SM-1, or as a false positive in SM-2 and SM-3;
  - how it appears in the Glossary's definition of a result ("zero or more verified faults").

  This affects the result screen, the rule table output and the metrics. *Fix:* Define "possible fault" in the Glossary. Specify what it displays (for example a fault chain with measurement, no drill, and "film again" guidance), and how it is scored in SM-1 to SM-3.
- **[medium]** Most rejection reasons are untested (FR-8) — Only face-on and out-of-frame have test consequences (and SM-6). "No swing detected", "more than one swing" and "too dark or blurred" have no bound and no test clip, and "too dark or blurred" is an adjective with nothing to measure against. *Fix:* Add one test clip per reason, or mark which reasons are best-effort heuristics without acceptance tests.
- **[medium]** FR-13's consequences can't be tested (FR-13) — "Never repeats or contradicts a verified fault" has no way to check it outside mock mode. It is also unclear whether an observation appears on a rejection, or on a result that already has verified faults ("may add"). *Fix:* Say when an observation is allowed (for example only on "No verified fault found" results). Make the contradiction check concrete, such as "never names any of the three verified fault terms".
- **[medium]** FR-14's grounding check is narrower than §4.6 promises (FR-14, SM-7) — §4.6 says the LLM "may not add faults, causes, drills or numbers", but the automated check covers only faults, drills and mobility exercises. Causes and numbers are not checked. "Plain language without jargon" has no bound. *Fix:* Extend the check to numbers and causes in the analysis data. Define jargon by a short banned-term list, or drop the claim from the testable consequences.
- **[medium]** No upload size bound (FR-5, NFR-1) — 15 s at 120–240 fps from a phone can be well over 100 MB. There is no size limit, and NFR-1 doesn't say whether upload time is inside the 2-minute bound. *Fix:* Add a maximum file size and say NFR-1 is measured from upload complete to result shown.
- **[low]** Small undefined targets (FR-19, FR-1, NFR-5) — FR-19's list shows the "main finding", which is undefined when there are several faults, a possible fault or a rejection. FR-1's "clear message" is acceptable. NFR-5 and FR-19 "phone browser" name no browsers. *Fix:* Define "main finding" (for example the highest-confidence verified fault, else "No verified fault" or "Rejected"). Name the browsers you will test on (for example iOS Safari and Android Chrome).

## Scope honesty — adequate
Non-goals (§7) and the out-of-scope list (§8.2) are explicit and justified. Assumptions are tagged and indexed. The total is 5 OQs, 10 assumptions and 2 notes. That is fine for a student MVP, and OQ3 (thresholds) is inherent to the method.

Two big omissions are left for the reader to infer instead of being stated.

### Findings
- **[high]** Hosting and deployment scope are never stated (UJ-1, NFR-2, NFR-5, UJ-5) — UJ-1 has Rory upload from his phone browser at the range, so AIcoach must be reachable from a phone over the network. NFR-2 refers to "the machine hosting AIcoach", but nothing says whether the MVP is publicly deployed, LAN-only, or local-only for the examiner. That choice determines HTTPS (needed for mobile upload and camera access), where clip storage lives, and whether NFR-1 runs on a server or the laptop. *Fix:* Add an explicit scope line, for example "MVP runs locally; phone upload is tested over LAN; public hosting is `[NON-GOAL for MVP]`", or the reverse with a named host.
- **[high]** GDPR is claimed as addressed but isn't covered (§6.1, addendum §G) — The addendum says the teacher's GDPR feedback is "addressed in PRD §6.1". §6.1 covers deletion and the clip retention default, but leaves out:
  - how long results and key frames (images of the person) are kept;
  - the legal basis or consent for storing saved videos;
  - data export or access;
  - what analysis data goes to the LLM provider outside mock mode. NFR-2 covers clips only, and OQ2 may send key frame images to it.

  Since this is graded feedback, the gap is visible to the examiner. *Fix:* Add retention periods, a one-line consent step at upload/save, a statement of which data, if any, leaves the host for the LLM, and either an export capability or an explicit `[NON-GOAL for MVP]` for export.

## Downstream usability — adequate
The Glossary is strong and the core terms are used consistently: swing clip, analysis, result, rejection, verified fault, confidence band. IDs are contiguous and unique (FR-1–19, UJ-1–6, NFR-1–7, SM-1–11, SM-C1–3). Every FR names the UJ it realizes, except the stretch FRs, which point to the brief's loop. Every SM names the FRs it validates. That helps story extraction.

The weak spots are terms that appear in FRs and SMs without a definition.

### Findings
- **[medium]** Terms used in FRs and SMs but missing from the Glossary (FR-9, SM-2, FR-6, FR-19, §4.4 Notes) — The missing terms:
  - "possible" and "potential threshold" (the latter defined only in addendum §B);
  - "clean swing clip" (SM-2);
  - "labelled test set" versus "bundled test clips" (FR-6, FR-15, SM-10): are they the same set, and is all of it published in the repo?
  - "main finding" (FR-19);
  - "player-author" (§4.4 Notes).

  *Fix:* Add Glossary entries, and state whether the bundled clips are the labelled set or a subset of it.
- **[low]** UJ-1's entry state doesn't match its path (UJ-1) — The entry state is "signed in on his laptop; the clip is on his phone", but the path has him filming and uploading from the phone browser. *Fix:* Change the entry state to signed in on his phone, or show the laptop step.

## Shape fit — strong
This is a consumer product with meaningful UX, and the UJs carry real weight: UJ-2 drives FR-8 and FR-4's links, UJ-3 drives FR-12 and FR-13, and UJ-6 drives FR-18–19. The examiner journey (UJ-5) is a pragmatic, honest fit for a graded deliverable and turns directly into FR-15 and NFR-4. Formality is right for a chain-top solo PRD: implementation detail sits in the addendum, and the main document stays at requirement level. No findings.

## Mechanical notes
- **Broken cross-reference:** FR-12's consequence "Meets SM-3 and SM-4" should probably read SM-2 and SM-3. SM-4 is the complete early-extension result, not no-forced-fit, and SM-2 itself says it validates FR-12.
- **Stretch leaking into core:** FR-1 says "Upload, results and history are reachable only when signed in". History is stretch (FR-16). Reword to "and the swing library".
- **NFR-7 vs addendum §A:** NFR-7 bans non-commercial components from the core, but addendum §A keeps SwingNet (CC BY-NC 4.0) as a swing-event fallback. State that using that fallback would breach NFR-7, or drop it.
- **Assumptions Index roundtrip:** all 10 inline tags are indexed and all index entries appear inline. The FR-13 inline tag is a bare `[ASSUMPTION]` with no text. Copy the index wording inline.
- **FR-16** (stretch) has no testable consequences. That's fine as long as it stays stretch, but add one if it gets promoted.
- **UJ format:** UJ-1 uses the full template, UJ-2–6 are compressed paragraphs. Each still has a protagonist and enough context, so this is acceptable.
- Required sections are all present for the stakes and product type.
