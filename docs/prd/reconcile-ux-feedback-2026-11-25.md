# Input reconciliation — PRD update 2026-11-25

Reviewer extract (Finalize step 2). Inputs: UX spine `ux-AIcoach-2026-11-11/EXPERIENCE.md` (+ `.memlog.md`), teacher feedback `tilbakemelding-prd.md` (2026-11-12). PRD decision log entries from 2026-11-25 govern. Line numbers refer to `prd.md` as of this review unless prefixed `UX` (EXPERIENCE.md). Visual matters ignored.

Severity: **high** = blocks stories/tests or leaves a promised behaviour unreachable; **medium** = ambiguity an implementer will have to guess; **low** = wording/copy/stale reference.

---

## A. UX spine vs PRD — gaps and contradictions in the PRD

| # | Sev | Topic | UX relies on | PRD state | Suggested fix |
|---|---|---|---|---|---|
| A1 | **high** | Orphan analyses after "delete clip, keep analysis" | UX L196–198: account page lists "Your analyses" with "clip deleted" meta; delete analysis from Account (L197, Flow 4). Rail "Swings" + "See all n analyses" (UX L56, OQ6). | FR-19 (L326) lets the player keep an analysis whose clip is deleted, and FR-3 (L134–139) lets him delete any analysis. But the only P1 list is the swing library (FR-19, clips); the analysis list is FR-16, which is **stretch** (L294–299; §4.7 L290 says history "adds the analyses whose swing clip was deleted"). In P1 a kept analysis without a clip is unreachable and cannot be deleted from the UI. | Either (a) make a minimal "your analyses" list (FR-16's list part) P1, leaving comparison stretch; or (b) state that in P1 a kept analysis remains reachable via the rail/thread list and the account page; or (c) drop "keep analysis" until P3. Also answers UX OQ6. |
| A2 | medium | Unverified observation on a result *with* a verified fault | UX L114 places the observation card only on the "No verified fault found" surface; result-thread layout has no slot for it. | §4.5 (L248) motivates it for the no-fault case, but FR-13 (L253–260) does not restrict it to no-fault results — any result may show one if an extra measurement passes (only same-as-active-fault is excluded, L260). | Decide: observation only when no verified fault is found, or on any result. If any result, UX needs a slot and a rule against contradicting the verdict (teacher 4.1 "contradicts"). |
| A3 | medium | Key frames given to the language model | UX L236: chat sees "key frames as references". | §4.9 (L337) says the chat "sees … key frames"; §6.1 (L372) says the LLM never receives key frames. Internal PRD contradiction. | Say in §4.9 "key-frame references (swing event, time, overlay description), not images", consistent with §6.1. |
| A4 | medium | "Club" on swing-library rows | UX L49, L196, Flow 6 L337: rows show "date · club" ("7-iron"). | Club is never captured: FR-5 (L157–164) has no club input, nothing measures it; FR-19 (L322) lists date + main finding only. | Either add an optional club field at upload (FR-5) or remove club from UX rows. |
| A5 | medium | System failure / timeout state | UX L167: after 3 min "This is taking longer…" + Try again; a system failure is never shown as a rejection or result. | FR-5 (L163) only covers "in progress until a result or rejection". No FR says a crash is distinct from a rejection, whether a failed run is stored as an analysis, or whether its clip enters the library (FR-18 L317 says "after an analysis finishes"). Also affects the 50-clip count. | Add an FR-5/FR-8 consequence: a processing failure shows a retry, is never presented as a rejection or result, and (decide) does/does not keep the clip. |
| A6 | low–medium | Single fault other than over the top fails SM-1 | — | §4.4 Notes (L244) covers OTT failing (swap to sway) and two faults failing; not early extension or loss of posture failing alone (is sway swapped in for it?). | One sentence in Notes. |
| A7 | low | Library-status after clip deletion | UX L104: result header reads "Clip deleted" (not a link) once the clip is gone. | FR-18 (L318) only requires the result screen to state the clip is in the library. | Add "or that the clip was deleted". |
| A8 | low | Library row for a clip whose analysis was deleted | UX L196: row reads "Analysis deleted". | FR-19 (L322) defines rows as main finding or "Cannot analyse" only. | Add the third row state to FR-19. |
| A9 | low | Account deletion confirmation | UX L321 / L73: sheet with plain consequences. | FR-3 (L139) requires confirmation only for deleting an analysis; account deletion has none. | Add "Deleting the account asks for confirmation and states what will be removed." |
| A10 | low | Low-confidence "what to film better" | UX L176, Flow 1 edge: low band adds a line on what to film better, linked to the guide step. | Only in UJ-1 edge case (L55); no FR consequence. | Optional FR-7 consequence. |
| A11 | low | UJ-2 frame rate | UX Flow 2 L301 deliberately changed to 24 fps because 30 fps is analysed, not rejected. | UJ-2 (L58) still says "at 30 fps". Not wrong (fps isn't listed as a reason), but misleading next to FR-8 L196. | Change to "at 24 fps" or drop fps from UJ-2. |

**Covered at requirement level (no gap):** library consent unticked/required (FR-1 L122, §6.1 L370); automatic library incl. rejections, no save toggle (FR-18 L317–319, FR-8 L197); 50-clip limit incl. rejections (FR-5 L164, FR-19 NFR L331); delete coupling both ways with confirmation (FR-3 L138–139, FR-19 L326); chat scope, grounding, no confidence upgrade, no drill for possible/unverified, 80 words, "Based on", refusals incl. pain/competitive round, stored and deleted with analysis, LLM-unavailable and mock behaviour, not on rejection (FR-20 L345–351); fps rule <30 reject / 30–119 warn, no "high" (FR-7 L187, FR-8 L196); over-the-top cap (L188); possible fault: no drill, not counted (FR-9 L216–218); no-fault screen lists faults checked (FR-12 L241–242); medical notice (FR-11 L235); deleting the account removes chats too (FR-3 L140).

---

## B. Places where the UX must now be updated (PRD decided differently or more precisely)

| # | Sev | UX location | Now in PRD | Update needed |
|---|---|---|---|---|
| B1 | **high** | UX L48, L114 ("exactly one when no verified fault is found"), L180 (no-fault state "one unverified observation card"), Flow 3 L311, OQ7 | Observation is optional, closed-list: shown only when an extra measurement passes its threshold; otherwise none (FR-13 L253–256, UJ-3 L61). | Add a **no-fault, no-observation state**: no dashed card, no "Ask the coach about this" link on the card — chat entry must come from the composer/suggested prompt instead. Change "exactly one" to "at most one, only when an extra measurement passes". Close OQ7. |
| B2 | medium | Flow 3 L311–313 copy "Weight appears to move toward the trail side at the top"; refusal "weight shift" | The only extra measurement is sway (trail ankle-to-hip angle) and the text is a fixed template per measurement (§4.5 L248, FR-13 L258, addendum §B); UJ-3 wording "your hips appear to move away from the target in the backswing". | Rewrite the observation and the refusal example around the sway template; mock mode shows the template unchanged (L261). |
| B3 | medium | Consent copy UX L72, Consent checkbox L146, Flow 8 L356 | FR-1 L123: sign-up screen must state what is stored — swing clips, results, key frames, chat — and that any of it can be deleted. | UX consent text/helper mentions only clips; add the helper line listing results, key frames and chat. (Copy sign-off OQ13.) |
| B4 | low | Delete-analysis sheet L197, Flow 4 L320; delete-account sheet L73, L321 | FR-3 L138/L140: deleting an analysis also removes its coach chat; account deletion removes chats. | Mention the coach chat in both sheets. |
| B5 | low | "Checked: early extension · loss of posture · over the top" L180, Flow 3 L310 | Checked list = active rule table; sway may replace over the top (§4.4 L244). | Make the checked list data-driven, not hardcoded. |
| B6 | low | Stale references: Foundation table L23–29 ("Replaces in the PRD"), AI Coach Chat L234 ("PRD still lists chat as a non-goal"), Flow 7 L342 ("PRD update pending"), L168 "FR-19 assumption; Open Question 2", L198 "FR-19 assumption", OQ1–3, OQ7, OQ11 | All now decided in PRD (FR-18–20, §4.8–4.9, NFR-6, §8.1). | Update/close; answer-length limit (80 words) settled; cost per question stays open (PRD OQ2). |
| B7 | low | Flow 1 L295 "rest of the bucket" | PRD UJ-1 L54 now "rest of his range session" (teacher §5). | Align wording. |
| B8 | low | UX L106/L179 several verified faults ordering `[ASSUMPTION]` | PRD allows zero or more faults (glossary L87) but sets no order. | No PRD change needed; keep as UX assumption. |

---

## C. Teacher feedback (tilbakemelding-prd.md) — status

| Point | Status | Evidence | Residual |
|---|---|---|---|
| **4.1** Unverified observation not testable ("may" vs "always", data source, grounding, mock, "never repeats/contradicts") | **Addressed** (option b chosen) | §4.5 L248; FR-13 L253–263 (closed list, threshold, template, LLM only rephrases, at most one, none when nothing passes, low band, no drill, grounding check same as FR-14, active-fault exclusion is mechanically checkable, mock shows template); UJ-3 L61 now consistent; glossary L96–97; addendum §B sway row; OQ2 L470 updated. | "Contradicts a verified fault" is not covered — only "repeats" (L260); see A2. If sway is swapped in, the list may be empty and the observation never appears (OQ7 L475) — acceptable but worth one line. Whether the grounding check runs against the real LLM path or only mock is unspecified (FR-14 L275 "fixed analysis inputs"). |
| **4.2** FRs with SM references instead of testable consequences (FR-9, FR-12, FR-16) | **Addressed** | FR-9 L216–221; FR-12 L241–242 (teacher's wording almost verbatim); FR-16 L298–299. | FR-7 L189 still has an evaluation-set aggregate ("see SM-5") as a consequence — same pattern the teacher flagged; minor. |
| **4.3** FR-6 tolerance in ms vs 30 fps floor | **Addressed** | FR-6 L178: ±1 frame impact, ±2 frames top, at the clip's frame rate; fps rule FR-8 L196. | — |
| **4.4** Scope too large; no checkpoints; P2 library *or* history; FR-16 vs FR-19 | **Partly** | Checkpoint dates §8.1 L398–402 (P1 by 2026-12-01, P2 by 2026-12-08, last week reserved); FR-16/FR-19 distinction stated in §4.7 L290. | Scope **grew**, against the advice: the swing library moved *into* P1 (L398) and chat (FR-20) was added as P2 — now 20 FRs, P1 = 17 FRs due 6 days after this update. No rule says what happens if P1 is not done by 2026-12-01 (e.g. chat is cut). The FR-16/FR-19 split leaves orphan analyses unreachable in P1 (A1). Decisions are logged as user overrides (memlog), so this is a conscious trade-off, but the PRD should state the slip rule. |
| **4.5** Sway not in rule table; threshold basis weak; two-faults-fail rule; SM-5 minimum | **Addressed / partly** | Sway reserve row L208, FR-9 L221, addendum §B L24; two-faults-fail rule L244; SM-5 minimum L450; OTT hand-path cap L188, addendum §B L23; posture angle-error note addendum §B L21. | Measurement definitions for early extension (body-relative unit) and loss of posture remain open (OQ3 L471) — the teacher listed these under "must clarify before UX/architecture/epics" (§6). Single non-OTT fault failing not covered (A6). |
| **§5** Mechanical: IDs; undefined glossary terms (visitor, examiner, history, potential/fault threshold); "rest of the bucket"; may/always | **Addressed** | Glossary L77, L79, L94, L107; UJ-1 L54; UJ-3/FR-13 aligned. IDs now UJ-1–7, FR-1–20, SM-1–13, SM-C1–C3, NFR-1–7, contiguous; Assumptions Index (L479–485) matches the 7 inline tags. | Front matter `updated: 2026-11-03` (L5) not bumped to 2026-11-25. |
| **§6** Must clarify before UX/architecture/epics | **Partly** | Observation basis and MVP status — done (§4.5). Tolerance in frames — done. P1 with hard date — done. Sway row — done. | Measurement definitions for early extension and posture — still OQ3. "Can wait" items: cost (OQ2, open, OK), storage limit (decided: 50, L331), coach verification (OQ1), competitor re-check (OQ5) — all tracked. Reflection Q1 (patent misread / own clips contradict) only implicitly answered by tuning-set adjustment (FR-9 L219–220); Reflection Q2 answered by FR-13 low band + FR-20 "never raise a confidence band". |

---

## D. Top items for the PM

1. **A1 (high)** — kept analyses whose clip is deleted are unreachable/undeletable in P1 because the analysis list is stretch.
2. **B1 (high, UX)** — UX has no state for "No verified fault found" without an observation; the observation is now optional.
3. **C 4.4 (medium–high)** — scope grew (library to P1, chat added) against teacher advice; add a slip rule for 2026-12-01.
4. **A2 (medium)** — decide whether an observation can appear next to a verified fault.
5. **A3 / A4 / A5 (medium)** — key frames to LLM contradiction; "club" never captured; system-failure state undefined.
6. **C 4.5 / §6 (medium)** — EE and posture measurement definitions still open (OQ3).
