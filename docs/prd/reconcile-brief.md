# Reconcile: Product Brief + Teacher Feedback -> PRD

Input set: `docs/product-brief/brief.md` (revised 2026-11-02), `addendum.md` (2026-09-19), `tilbakemelding-product-brief.md` (teacher feedback 2026-10-06).
Compared against: `prd.md` + `addendum.md` (prd-AIcoach-2026-11-03).
Deliberate overrides in `.memlog.md` ignored: deadline 2026-12-15, TrackMan as next phase, research-based filming guide (hand height, 8–12 ft, 120 fps), opt-in swing library, English UI, retention default, over-the-top kept with sway fallback.

Severity: **H** = changes what gets built or tested; **M** = weakens a stated intent or graded ask; **L** = wording / traceability.

---

## 1. Qualitative ideas (tone, voice, feel)

| # | Sev | Brief / feedback says | PRD status | PRD location |
|---|---|---|---|---|
| Q1 | H | Brief addendum names the core gap: an "LLM coach layer that translates numbers into **feel-based cues** and drills". Brief Summary: "coach-style feedback". | **Missing.** No FR, glossary term or consequence asks the explanation to turn measurements into a feel cue (what the player should feel/do). FR-14 only asks for "plain language without jargon". Cue wording appears only as next-phase cue memory. | §4.6 FR-14; §9 Cue memory |
| Q2 | H | Brief Problem: "**Feel and reality often disagree** in golf, so unguided practice can reinforce the wrong thing" — the reason the product exists. | **Weakened to vision text only.** Restated in §1 Vision, but no requirement uses it: nothing asks the result/explanation to contrast what the player likely feels with what the key frame shows, or to frame key frames as "this is what actually happened". | §1 Vision; §4.4 FR-10; §4.6 FR-14 |
| Q3 | M | Brief: explanation is coach-like — "traces cause to effect, the way a coach reasons"; result reads as what a coach would say. | **Partly.** §1 says "what a good coach would say", but no tone/voice spec for the explanation (second person, direct, encouraging, short, one priority, what to practise next). "Without jargon" and "short" are untestable as written — FR-14 has no consequence checking either (e.g. length cap, banned-term list, reading level). | §4.6 FR-14 Consequences |
| Q4 | M | Teacher feedback / brief: answer should be one clear direction for the session (brief usage situation: "read the result, and practise the drill in the same session"). | **Implied, not specified.** SM-C2 says "AIcoach wins on one clear answer", but no FR defines what happens when 2–3 verified faults are found (ordering, which one to start with, whether all drills show). Result could become a list again. | §10 SM-C2 vs §4.4 FR-9–11 |
| Q5 | L | Brief addendum user-voice signal: fear of "ingraining the wrong things". | Captured in JTBD Emotional (§2.1) and addendum E; fine. No action. | §2.1 |

## 2. Constraints and analysis behaviour

| # | Sev | Brief says | PRD status | PRD location |
|---|---|---|---|---|
| C1 | M | Brief: unverified observation is shown "labelled as an unverified observation **with low confidence**". | **Missing.** FR-13 requires the "Unverified — confirm with a coach" label but no confidence band; glossary says every measurement and verified fault has a band, silent for observations. | §4.5 FR-13; §3 Glossary |
| C2 | M | Brief: open observation "names **the most important problem it sees**, whether or not it is one of the three". | **Weakened / partly contradicted.** PRD: AIcoach "may add" one observation (optional), and an `[ASSUMPTION]` forbids it from repeating a verified fault. The brief's intent (always surface the main problem) is softened. | §4.5 Description; FR-13 Consequences |
| C3 | M | Brief success criterion 4 / 1: "does not report any of the three" on out-of-scope and clean swings. | **Ambiguous.** PRD adds a third state "possible" (borderline). SM-2/SM-3 do not say whether a "possible" counts as reporting a fault — a loophole that could mask forced fits. | §4.4 FR-9 `[ASSUMPTION]`; §10 SM-2, SM-3 |
| C4 | L | Brief: rejection when "**low pose confidence**, wrong angle, body out of frame". | **Partly.** FR-8 reasons list angle, frame, no swing, multiple swings, dark/blur — low pose/landmark confidence as an explicit rejection trigger is not listed. | §4.3 FR-8 |
| C5 | L | Brief: "Thresholds and confidence rules are set and tuned against the test videos and **documented in the PRD**." | **Moved.** Starting thresholds live in PRD addendum B as "not requirements"; the PRD defers values to tuning (Open Q3). Acceptable, but the promise "documented in the PRD" is not kept — a home for final tuned values should be named. | §4.4; §11 Q3; addendum B |
| C6 | L | Brief Boundaries: recommend a physio "when a specific problem surfaces". | PRD narrows trigger to "on pain". Minor narrowing. | §4.4 FR-11 |

## 3. Success criteria

| # | Sev | Brief / feedback says | PRD status | PRD location |
|---|---|---|---|---|
| S1 | H | Brief **stretch criterion** and teacher feedback's own example criterion: "a new video can be compared with the previous one for at least one measurement". | **Missing as a metric.** FR-17 exists (stretch) but no SM validates it; FR-16/17 are not referenced from §10. The teacher explicitly named this as a model success criterion. | §4.7 FR-17; §10 |
| S2 | M | Brief criterion 5: explanation "names only the faults, **causes**, drills and exercises from the analysis". | **Weakened.** FR-14 automated check covers faults, drills and mobility exercises only — causes (and numbers, which the description forbids adding) are not in the check. | §4.6 FR-14 Consequences; §10 SM-7 |
| S3 | L | Brief criteria 1–8 map 1:1 to PRD SM-1..SM-10; no traceability table from brief criterion to SM. Teacher: examiner must follow a traceable path from plan to app (process 30 %). | Not contradicted, but no explicit mapping. | §10 |

## 4. Quality assurance (teacher change request #3, QA 15 %)

| # | Sev | Brief / feedback says | PRD status | PRD location |
|---|---|---|---|---|
| A1 | M | Brief QA: "Rules as tables, so **each rule can be unit-tested with fixed landmark data**." Teacher: write fault rules as thresholds and test them. | **Missing.** NFR-3 requires the labelled video set as an automated suite and the module runnable in isolation, but no requirement for rule-level unit tests on fixed/synthetic landmark data (independent of pose model noise). | §5 NFR-3; §4.4 FR-9 |
| A2 | L | Brief: test set "lives in the repo and is used as automated tests **throughout the project**"; includes clean swings and other-fault swings, labelled in advance. | Covered (§6.1, NFR-3, SM intro). Label-in-advance (before running the app) not stated explicitly. | §10 intro; §6.1 |
| A3 | L | Brief: labels "checked by a coach if possible". | Covered as Open Q1. | §11 Q1 |

## 5. Teacher-feedback asks

| # | Sev | Feedback asks | PRD status | PRD location |
|---|---|---|---|---|
| T1 | M | Design 10 %: "skissér opptaksveiledning og resultatvisning" (sketch filming guide and result screen). | **Deferred** to UX phase (addendum G). PRD gives no result-screen information hierarchy (order: fault -> evidence/key frame -> chain -> drill -> explanation; how unverified observation is visually separated). Acceptable if UX picks it up — flag so it is not lost. | addendum G; §4.4–4.6 |
| T2 | M | GDPR open question in brief: "how long videos are stored, and deleting a user's data". | **Partly.** Deletion covered (FR-3, FR-19); unsaved clips deleted. No retention period for results/key frames/saved clips, no consent statement at upload for storing key frames (images of the person). Addendum G calls GDPR "addressed". | §6.1 |
| T3 | L | Vision "replace the coach at every level" should be kept clearly apart from v1. | Covered; §1 separates long-term goal from MVP claim. | §1 |
| T4 | L | Drop "also usable by everyone" for v1. | Covered (§2.2 Non-Users). | §2.2 |
| T5 | L | Scope: keep history/compare as a second step if time allows; cue memory and swing score after the course. | Covered (FR-16/17 stretch, §8.2). Swing library added to MVP is a memlog override — ignored, but it adds scope the teacher warned about. | §8.1 |
| T6 | L | LLM cost plan / test mode. | Covered (§6.3, FR-15, Open Q2). | §6.3 |

## 6. Brief-addendum feature candidates not carried

| # | Sev | Item | PRD status |
|---|---|---|---|
| F1 | L | **One-tap coach handoff** (2-minute brief for a human coach) — fits "confirm with a coach" for unverified observations. | Absent, not even in §9 Next Phase. |
| F2 | L | **Drift-watch** (flag slow mechanical change). | Absent from §9. Was "pending selection", so omission is defensible. |

## 7. Covered (no action)

Summary/problem/target user; DTL-only, ≤15 s mp4/mov; local 2D pose; three faults with causes, drills, mobility exercises (table matches brief); fault chains with evidence; confidence band on every measurement; no launch-monitor claim; rejection with filming tips; no forced fit; grounded LLM with mock; speed < 2 min; privacy isolation; examiner runnability; Rules of Golf boundary; not-medical boundary; `.env`/`.env.example`; user videos outside Git; author domain expertise; out-of-scope list (face-on, 3D, chat, cue memory, score, gym plans, subscription, native app).
