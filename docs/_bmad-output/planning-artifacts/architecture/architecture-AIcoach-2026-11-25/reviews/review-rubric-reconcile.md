---
title: Review — Architecture Spine AIcoach (rubric + reconcile)
reviewed: ARCHITECTURE-SPINE.md (draft, 2026-11-25)
inputs: docs/prd/prd.md, docs/prd/addendum.md, ux-AIcoach-2026-11-11/EXPERIENCE.md, .docs/planning-artifacts/architecture/technology.md
date: 2026-11-25
reviewer: independent (spine not modified)
---

# Review — Architecture Spine AIcoach

## Verdict

A strong, well-scoped spine: the engine/app split, ownership filter, status machine, single result document, evidence IDs, rule-table-as-config, LLM gateway with mock mode and the one-grounding-check rule are exactly the right invariants for a solo, AI-agent-built MVP. It adapts `technology.md` sensibly (drops Redis/Supabase/Railway/payments, keeps Caddy single origin, mock fallback, `FEATURE_*`, no-rollback rule; replaces build-time `NEXT_PUBLIC_FEATURE_*` with runtime `/api/config`, which is a good adaptation).

It is **not yet ready to hand to story agents**. No critical defects, but **8 high** findings where two units will predictably build different things: the library-row state model (incl. "Not analysed"), live progress out of a pure engine running in a subprocess, the reason-code → guide-step contract, delete/retry racing an in-flight job, a P1 screen that depends on a P3-gated endpoint, a grounding check that lets the no-fault explanation name faults, an under-specified chat contract, and `AnalysisResult` missing fields the result screen needs. Plus 19 medium and 18 low.

Severity key: **critical** = spine contradicts a hard requirement or guarantees breakage; **high** = two units will diverge, or a P1 requirement has no home; **medium** = likely rework or a quiet requirement is lost; **low** = wording, consistency, nice-to-have.

---

## Part A — Reconcile against inputs

### A.1 PRD (prd.md + addendum.md)

| Requirement / constraint | Landed? | Finding |
|---|---|---|
| FR-1 consent unticked, recorded; email-in-use refused; passwords hashed | Mostly (AD-20) | Email normalisation and password rules missing → M13. Consent text/version single source missing → M12 |
| FR-1 everything except landing/guide/auth requires sign-in | Partly | No deny-by-default auth rule on `/api` → M5 |
| FR-2 / SM-9 isolation | Yes (AD-7) | — |
| FR-3 delete analysis/account; "cannot sign in" after delete | Mostly (AD-8) | JWT cookie stays valid 30 days after account deletion → M5. Delete while job is running → H4 |
| FR-3 / UJ-4 delete one analysis from Account | **Contradiction** | Account "Your analyses" list needs `GET /api/analyses`, which spine gates behind P3 `FEATURE_HISTORY` → H5 |
| FR-4 each rejection reason links to its guide step | Partly (AD-6, Conventions) | Codes and step IDs not fixed as a shared enum; guide is static frontend content, map is in `rules.yaml` → H3 |
| FR-5 15 s, mp4/mov, 50-clip refusal; progress visible | Yes (AD-15, AD-16, AD-23) | iPhone slo-mo / VFR exports vs 15 s and fps only an ASSUMPTION → M18 |
| FR-6 events at clip's own frame rate (±1 / ±2 frames); body-relative units; CLI | Mostly (AD-1, AD-13, AD-24) | Frame basis for events (native vs subsampled) not fixed → M2 |
| FR-7 band composite + caps (<120 fps, OTT ≤ medium) | Yes (AD-12) | — |
| FR-8 reasons (not DTL, out of frame, no swing, >1 swing, dark/blurred, <30 fps); stored; clip in library | Mostly (AD-6, AD-16) | Reason list not enumerated → H3. Undecodable clip has no playback → L17 |
| FR-9 verified/possible/absent; sway reserve; thresholds in config; **"two faults fail → ship as possible only"** | Partly (AD-11) | No per-fault "possible only" status; no validation that extra-list ∩ active list = ∅ (FR-13) → M10 |
| FR-10 chain links with measurement + key frame + band; "likely cause"; key frames = events the rule uses | Mostly (AD-9, AD-17) | Thresholds for the ruler / "rule: 4%" and event timestamps not in `AnalysisResult` → H8 |
| FR-11 medical notice on every mobility exercise | Yes (AD-11) | — |
| FR-12 no forced fit: **explanation names none of the faults** | **Gap** | AD-19 allows naming any fault in `facts` (incl. possible/absent) → H6 |
| FR-13 ≤1 observation, furthest past threshold, always low, template unchanged in mock | Mostly (AD-9, AD-12, AD-19) | Where the rephrase runs / `source` flag → L9 |
| FR-14 grounded, 150 words, one feel cue, blocklist, **template fallback** | Yes in principle (AD-6, AD-19) | Fallback can be pre-empted by the 10-min job timeout if the LLM hangs → M3. Several checks not deterministic on free text → H6 |
| FR-15 mock mode end to end, no network | Mostly (AD-18, AD-23) | Pose model weights may be downloaded at runtime (rtmlib / MediaPipe task files) → M6 |
| FR-16 "clip deleted" in history | Yes (AD-8) | Row identity/state model → H1 |
| FR-17 compare same measurement | Implicit | Measurement keys must be stable across rule-table versions → L10 |
| FR-18 every clip incl. rejections stored; never without consent | Yes (AD-16, AD-20) | — |
| FR-19 list with main finding / "Cannot analyse"; play on phone + laptop; delete with keep/delete choice; "clip deleted" row not counted | Mostly (AD-8, AD-15, AD-21) | Row states incl. failed ("Not analysed") and "Analysis deleted" not modelled; thumbnails have no home → H1, M1 |
| FR-20 chat only on results; 80 words; "Based on"; refusal classes; stored+deleted; **LLM unavailable → chat disabled** | Partly (AD-18, AD-19, AD-23) | **Contradiction:** AD-19 gives a fixed refusal; FR-20/UX disable the composer. No server guard on status; refusal classes unstructured → H7 |
| §8.1 chat cut rule (12-01 / 12-08) | Yes (AD-23 `FEATURE_CHAT`) | — |
| NFR-1 10 s < 2 min, 15 s < 3 min, median of 5 | Partly (AD-5, AD-15) | What is timed, and whether transcode/LLM are inside it, is undefined → M16, M1 |
| NFR-2 local, phone on Wi-Fi, clips never leave laptop | Yes (AD-3) | — |
| NFR-3 isolated engine, test set as suite | Yes (AD-1, AD-24) | Tuning env vs demo env drift → M7 |
| NFR-4 README, no keys | Yes (AD-25, AD-20 secret) | Examiner CPU arch / wheels → M7; weights download → M6 |
| NFR-5 mobile | Partly (AD-3, AD-21 Range) | Not in the capability map; upload progress needs XHR → L6, L15 |
| NFR-6 English | Yes (AD-22) | — |
| NFR-7 licensing | Yes (AD-13, AD-14) | ffmpeg/x264 GPL note → L12 |
| §6.1 LLM gets analysis data only | Yes (AD-18) | Free-text chat history can carry personal data → L14 |
| §6.1 clips never in Git; `.env` | Yes (AD-4, Conventions) | — |
| Addendum A trim before pose, 6 Hz Butterworth | Yes (AD-13, AD-15) | — |
| Addendum C band composite | Yes (AD-12) | — |

### A.2 EXPERIENCE.md

| UX behaviour / state | Landed? | Finding |
|---|---|---|
| Step log: 5 fixed steps, stop at failing step (OQ1) | Yes (AD-6) | — |
| **Analysing: evidence pins/frames fill live as steps finish** | **Gap** | Spine only has the final `AnalysisResult`; no partial-evidence or progress-detail schema; engine runs in a subprocess with no DB access → H2 |
| "Taking longer" line after 3 min | Partly | Needs `started_at` and the threshold in `/api/config` → L5 |
| **Analysis fails → "Try again", row "Not analysed"** (OQ9) | Half | Retry is decided (AD-6); library label "Not analysed" and the rail "Analysing…" state are not → H1 |
| Rejection reason row links to guide step; low-confidence "what to film better" links to guide step | Partly | Second link (low confidence) has no code at all → H3 |
| Library rows: "Cannot analyse", "clip deleted", "Analysis deleted", thumbnails, dashed tile | Partly (AD-8) | → H1, M1 |
| Account rows "clip in swing library"/"clip deleted"; delete-account sheet counts ("9 analyses… 9 swing clips") | **Gap** | → H5 |
| Verdict card "7% · rule: 4%"; threshold ruler with potential threshold | **Gap** | → H8 |
| Clip checks (view, frame, fps) in Evidence panel | Gap | → H8 |
| Key-frame alt text "Impact, 2.07 s…" | Gap | Event timestamps → H8 |
| "Based on" lists pins **and** items (drill, rule table, unverified observation) | **Contradiction** | AD-19 says "lists only evidence IDs" → M14 |
| LLM unavailable → composer disabled with plain line | **Contradiction** | → H7 |
| Chat cut → hide composer, prompts, grounding note, chips | Yes (AD-23) | — |
| Mock-mode label | Yes (`mock_mode` in `/api/config`) | — |
| Ready-to-send shows "3.8 s of 15 s · 120 fps" | Infeasible as written | Browsers can't read fps; spine should say fps comes from the server → M18 |
| Upload echo shows file name (also on reload) | Undecided | → L4 |
| Protected URL → sign-in → back; guide public | Undecided | → L7 |
| Storage-limit state (drop zone disabled) | Mostly | Client needs count + limit → covered if H1 row endpoint returns `count`/`limit` |
| No token streaming; one question at a time | Consistent (sync POST) | — |
| Playback fails state | Partly | → M1, L17 |

### A.3 technology.md (reference stack)

| Pattern | Landed? | Finding |
|---|---|---|
| Single origin via Caddy | Yes, adapted to plain HTTP on LAN (justified for phones) | — |
| Caddy also routes `/docs`, `/openapi.json` to backend | **Dropped silently** | Spine routes only `/api/*`; FastAPI's default `/openapi.json` would hit Next.js, breaking `openapi-typescript` generation → M17 |
| Mock fallback, never fail on missing key | Yes (AD-23) | — |
| `FEATURE_*` two layers | Deliberately replaced by runtime `/api/config` | Good adaptation |
| No `rollback()` on shared session; `ON CONFLICT DO NOTHING` | Yes (Conventions) | — |
| Refuse default `JWT_SECRET` | Adapted (auto-generate in `DATA_DIR`) | Collides with the orphan-file sweep → M4 |
| Tests on aiosqlite | Adopted | Postgres-only semantics used by the spine (JSONB, `FOR UPDATE`, FK cascade) → M15 |
| Per-IP rate limits on auth/AI | Deferred (justified for LAN) | Fine |
| Seeding / demo accounts | Not adopted | Fine (UJ-5 creates an account) |
| CSP in `next.config` | Not mentioned | Low priority for LAN → L13 |
| Railway/Supabase/backup/watchdog | Deferred to next phase | Fine |

---

## Part B — Rubric

| Criterion | Judgement |
|---|---|
| Fixes the real divergence points for the level below, misses none | **Mostly.** Most important seams are fixed. Missed: library-row state model (H1), progress channel (H2), reason/guide enum and frontend routes (H3), job-vs-delete concurrency (H4), result fields the UI needs (H8), chat response contract (H7). |
| Every AD Rule is enforceable and prevents its divergence | **Mostly.** AD-5 timeout and "single worker" are not enforceable as written (M3). Several AD-19 checks cannot be done deterministically on free text (H6). AD-8 sweep conflicts with AD-20 (M4). AD-1/AD-2 would benefit from an import-linter contract (L18). |
| Nothing under Deferred could let two units diverge | **Pass with one caveat.** Deferred items are safe because ports/config absorb them. Caveat: "concrete measurement definitions" is deferred, but measurement *keys* and the canonical joint set (M9) must be fixed now so adapters, measurements, eval labels and FR-17 agree. |
| Every dimension the altitude owns is decided, deferred or open | **Mostly.** Deployment, environments, secrets, logging, migrations, testing are decided. Missing: auth default/session invalidation (M5), handedness (M9), video orientation (M8), model-weight provenance (M6), NFR-1 measurement (M16), disk/backup of the eval data (L13). No Open Questions section exists; several items above belong there if not decided. |
| Named tech plausible | **Plausible overall, with risks.** The stack is coherent and fits a solo laptop MVP. Risks: mediapipe on Python 3.13 and on linux/arm64 (an examiner's Apple-silicon Mac) (M7); several version numbers look ahead of known release cadence (e.g. onnxruntime 1.32, pydantic-ai 2.74, mediapipe 1.2.3) and can't be verified by this reviewer; the lockfiles should be the authority (L13). bcrypt 5.x rejects passwords over 72 bytes (M13). `ProcessPoolExecutor` cannot kill a running task (M3). |

---

## Findings

### High

**H1 — high — AD-8, AD-9, Seed endpoints (`GET /api/clips`) — Library-row state model and identity are undefined.**
Issue: the swing library, rail and account rows must show `Analysing…`, a main finding, `Cannot analyse`, `Not analysed` (failed, UX), `clip deleted` (analysis kept) and `Analysis deleted` (clip kept). AD-9 derives `main_finding` only from `AnalysisResult`, which doesn't exist for queued/running/failed rows or for clips whose analysis was deleted. `GET /api/clips` is said to return "library rows", but a "clip deleted" row has no clip, so the row's ID type (clip vs analysis) and which DELETE it calls are left to each unit. The "Not analysed" label named in UX is not in the spine at all.
Fix: add to AD-9 (or a new AD): "The server returns `LibraryRow {clip_id: uuid|null, analysis_id: uuid|null, created_at, state, main_finding: str|null, band: high|medium|low|null, has_playback: bool, thumbnail_url: str|null}` with `state ∈ analysing | result | rejection | failed | clip_deleted | analysis_deleted`. Labels: `analysing` → "Analysing…", `rejection` → "Cannot analyse", `failed` → "Not analysed", `analysis_deleted` → "Analysis deleted", `clip_deleted` → main finding + meta "clip deleted". `GET /api/library` returns rows newest first plus `{count, limit}`. The count excludes `clip_deleted` rows. The frontend never derives `state` or `main_finding`."

**H2 — high — AD-1, AD-5, AD-6 — No progress channel from the engine, and no partial evidence for the "Analysing" screen.**
Issue: UX has evidence pins, key frames and the measurement "fill in as steps finish", with a mono detail per step. The engine is pure (no DB) and runs in a `ProcessPoolExecutor` child, yet AD-5 says "progress is written to the row as steps". How a child process reports steps (and partial evidence) is not decided, so the worker story and the engine story will each invent one. The poll response shape during `running` is also not defined.
Fix: add to AD-5: "`analyse()` takes an optional `on_step(step_id, state, detail: str, partial: dict|None)` callback. In the worker it is a `multiprocessing` queue drained by the parent, which writes `analyses.progress = {steps:[{id, state: pending|running|done|stopped, detail}], partial_evidence:[…]}`. `GET /api/analyses/{id}` returns `status`, `progress`, `fps`, `fps_warning`, `started_at`, and `result` only when status ∈ {result, rejection}." If live pins are cut, say so explicitly as a UX deviation: "evidence fills only at the end; the step log is the only live element".

**H3 — high — AD-6, AD-11, Conventions (Enums), Capability map FR-4 — Reason codes, film-better hints and guide-step IDs are not a fixed shared contract.**
Issue: the reason → step map lives in `rules.yaml` (backend), but the guide is "static content" in the frontend, so step identifiers exist in two places with no owner. FR-8's minimum reason list isn't enumerated. The UX low-confidence state also needs "what to film better" linked to a guide step, and nothing in `AnalysisResult` carries that. Frontend routes that other units link to (thread, guide step, clip detail) are not fixed.
Fix: add to Conventions: "Guide step slugs (fixed enum, OpenAPI): `view`, `position`, `distance`, `frame_rate`, `framing`, `one_swing_light`. Rejection reason codes (fixed enum): `not_dtl`, `body_out_of_frame`, `club_out_of_frame`, `no_swing`, `multiple_swings`, `too_dark_or_blurred`, `fps_below_30`, `undecodable`. Each reason and each low-confidence `film_better` hint in `AnalysisResult` carries `{code, guide_step}`. `rules.yaml` holds the map; the frontend renders `/guide/{guide_step}` and never maps codes itself. Frontend routes: `/`, `/signin`, `/signup`, `/guide`, `/guide/{slug}` (public), `/swing/new`, `/swing/{analysis_id}`, `/library`, `/library/{clip_id}`, `/account`."

**H4 — high — AD-5, AD-6, AD-8 — Deleting (or retrying) while an analysis is queued/running is undefined.**
Issue: a player can delete the clip, the analysis or the whole account while the worker is decoding the original or writing key frames. The worker will then write into a deleted directory, update a deleted row, or (on the Windows dev host) make the file delete fail because the file is open. `POST …/retry` on a running job is also unguarded beyond the state diagram.
Fix: add to AD-8: "Deleting a clip, an analysis or an account whose analysis is `queued` or `running` is allowed: the row is deleted in the transaction; the worker checks the row still exists (`SELECT … FOR UPDATE SKIP LOCKED` on pick-up, existence re-check before every write) and discards its output if it is gone; file removal that fails is retried by the sweep. `retry` returns 409 `analysis_not_failed` unless status is `failed` and the clip row still exists."

**H5 — high — AD-23, Seed endpoints, Capability map FR-3 — P1 Account screen depends on a P3-gated endpoint.**
Issue: UX Account (FR-3, UJ-4, P1) lists "Your analyses" with delete, meta "clip in swing library / clip deleted", and the delete-account sheet states counts ("9 analyses… 9 swing clips"). The only analysis listing is `GET /api/analyses (P3 history)`, which AD-23 makes return 404 while `FEATURE_HISTORY` is off.
Fix: in Seed endpoints: "`GET /api/analyses` is P1 (Account list). `FEATURE_HISTORY` gates only the P3 `See all n analyses` / comparison UI and `GET /api/analyses/compare`." and "`GET /api/me` returns `{email, analyses_count, clips_count}` for the delete-account sheet."

**H6 — high — AD-19 — The grounding check misses FR-12 and several checks can't be done on free text.**
Issue: (a) FR-12/FR-14 say the explanation for "No verified fault found" (and for a rejection) names **none** of the faults; AD-19 only requires naming faults "in `facts`", and `facts` includes possible/absent faults for chat, so a no-fault explanation naming "possible early extension" passes. (b) "Exactly one feel cue per verified fault", "never raises a band" and "never calls a possible fault verified" are not deterministically checkable on unstructured prose. (c) "Every number matches a `display` value" will reject drill/exercise text such as "3 × 10" or "90/90" unless those are facts, pushing almost everything to the template.
Fix: amend AD-19: "`CoachLLM.explain` returns structured output `{body, feel_cues:[{fault_key, text}], cited_evidence:[id]}` (pydantic-ai result type). The check runs per `kind`: `explanation` may name only **verified** faults (none when the outcome is no-fault or rejection); `observation` may name only its measurement; `chat` may name any fault in `facts` with its outcome word. Band words next to a fault must equal that fault's band. Allowed numbers = `display` values ∪ numbers inside the drill/exercise/instruction strings in `facts`. Templates in `rules.yaml` are run through `grounding_check` in a startup test."

**H7 — high — AD-18, AD-19, AD-23, Seed endpoints (chat) — The chat contract is under-specified and contradicts FR-20 on "LLM unavailable".**
Issue: AD-19 says a failing chat answer retries once and "then gives the fixed refusal", but FR-20/UX say an unavailable LLM **disables the chat** with "The coach can't answer questions right now. Your result is complete." The frontend has no signal for that. The server isn't told to refuse chat on a rejection or before a result exists. Refusal classes (not measured, other swings, pain → physio notice only, competitive round, off topic) are untyped, so Mock and OpenRouter adapters and SM-13 can disagree.
Fix: add to AD-19: "`POST /api/analyses/{id}/chat` returns 409 `chat_unavailable_for_status` unless status = `result`. An LLM transport error or timeout returns 503 `llm_unavailable` (the frontend disables the composer with the UX line); a grounding failure after one retry returns a stored fixed refusal. `answer()` returns `{kind: answer|refusal, refusal_class: not_measured|other_swings|pain|competition|off_topic|null, text, based_on:[ref]}`; for `pain` the text is replaced by the `rules.yaml` medical notice. `/api/config` returns `chat_enabled = FEATURE_CHAT` so the frontend can hide chat (cut rule) separately from `llm_unavailable`. Mock answers are generated from `CoachFacts` and pass `grounding_check`."

**H8 — high — AD-9, AD-17 — `AnalysisResult` lacks fields the result screen needs, so the UI will read `rules.yaml` or hard-code.**
Issue: the verdict card shows "7% · rule: 4%", the threshold ruler shows fault and potential thresholds, the Evidence panel shows clip checks (view, framing, fps), key-frame alt text needs event times ("Impact, 2.07 s"), and the thread echo shows fps. None of these are in AD-9's list. Because thresholds change on the tuning set, an old analysis must show the threshold that applied when it ran.
Fix: add to AD-9's contents: "per measurement: `key`, `thresholds {potential, fault}` each with `display`; per event: `frame_index` (native fps), `t_ms`, `clarity`; `clip {fps, duration_ms, width, height, rotation}`; `clip_checks [{key: view|framing|fps|light, outcome: pass|warn|fail, display}]`; `film_better [{code, guide_step}]` (see H3). The UI never reads `rules.yaml`."

### Medium

**M1 — medium — AD-15, AD-4 — Playback transcode timing, state and thumbnails are undefined.**
Issue: "After the analysis ends, ffmpeg makes `playback.mp4`" doesn't say whether this happens before the status flips (adding to NFR-1) or after (the library offers playback that 404s), whether it holds the single CPU slot, or what happens for undecodable clips. Library thumbnails (UX) have no path; deriving them from key frames breaks for rejections and after "Delete analysis".
Fix: "Transcode runs in the same worker slot right after the status is final and is not part of NFR-1 timing. `clips.playback_state ∈ pending | ready | failed`; the video endpoint returns 409 `playback_not_ready` while pending. The transcode also writes `users/{uid}/clips/{cid}/thumb.jpg` (first frame); thumbnails belong to the clip, not the analysis."

**M2 — medium — AD-13, AD-15, AD-24 — Event frame basis vs eval labels.**
Issue: FR-6 tolerances are "at the clip's own frame rate". If pose runs on a subsampled window (a likely NFR-1 optimisation), events come back in subsampled indices while `labels.yaml` holds native indices.
Fix: "Events are always reported as native-fps `frame_index` plus `t_ms`. Any subsampling is an engine setting recorded in `AnalysisResult.step_timings`/meta; labels in `eval/labels.yaml` are native frame indices."

**M3 — medium — AD-5, AD-6 — Single worker and hard timeout aren't enforceable as written; LLM hang contradicts AD-6.**
Issue: `ProcessPoolExecutor` cannot cancel a running task, so a 10-min timeout needs killing the child. Running Uvicorn with `--workers N` (or two backend containers) gives N workers, breaking "one at a time". The `explanation` step can hang on OpenRouter until the job timeout marks it `failed`, which AD-6 forbids.
Fix: "The backend runs exactly one Uvicorn process (no `--workers`); the worker also claims rows with `FOR UPDATE SKIP LOCKED`. On timeout the parent terminates the pool's process and creates a new pool. `explain()` has its own 20 s timeout (configurable); timeout → template, never `failed`. The 10-min timeout counts from `started_at`, not queue time."

**M4 — medium — AD-8 vs AD-20 — The orphan sweep would delete the generated JWT secret.**
Issue: "a sweep removes any file that has no row", and AD-20 keeps the generated `JWT_SECRET` in `DATA_DIR`.
Fix: "The sweep only walks `DATA_DIR/users/`; system files live in `DATA_DIR/system/`. The sweep runs before the worker starts."

**M5 — medium — AD-7, AD-20 — No deny-by-default auth, and deleted accounts keep a valid session.**
Issue: the stateless 30-day JWT stays valid after account deletion; a later request with it will hit FK errors (500) instead of 401. No rule says every `/api` route requires auth except a short public list.
Fix: "Every `/api` router requires the `current_user` dependency except `POST /api/auth/signup|signin`, `GET /api/config`, `GET /api/health`. `current_user` loads the `users` row; a missing row → 401 `session_invalid` and clears the cookie."

**M6 — medium — AD-13, AD-25, Stack — Pose model weights must not be downloaded at runtime.**
Issue: rtmlib downloads ONNX weights on first use and MediaPipe Tasks needs `.task` files. FR-15/NFR-4 expect an offline, keyless run; a first-run download can fail at the examiner and is unpinned.
Fix: "Model weights are fetched at image build (or committed under `models/` if small), pinned by URL + SHA-256 and licence in `models/MANIFEST.yaml`; adapters load only from `MODELS_DIR` and never download at runtime."

**M7 — medium — AD-25, Stack — Platform and environment drift.**
Issue: (a) mediapipe on Python 3.13 and linux/arm64 (an examiner on an Apple-silicon Mac under Docker) is a real wheel-availability risk. (b) In dev the engine runs on the Windows host, in demo on Linux in Docker; OpenCV/FFmpeg builds can differ in decoded frame counts, so thresholds tuned on the host may not reproduce in the demo.
Fix: Deferred/ASSUMPTION: "Backend image is built for linux/amd64 and linux/arm64; confirm mediapipe wheels for both on Python 3.13 in the spike, else pin Python 3.12 or default to rtmlib." Rule in AD-24: "Tuning and `eval` runs use the backend container (`docker compose run backend aicoach-engine eval …`); the SM report records the engine environment."

**M8 — medium — AD-15, AD-17 — Video rotation and the coordinate frame aren't fixed.**
Issue: phone clips carry rotation metadata; ffmpeg auto-rotates the playback copy, OpenCV may or may not. Overlay geometry, key-frame JPEGs and playback can end up in different orientations.
Fix: "All pose coordinates, key-frame JPEGs and overlay geometry are in the display orientation (ffprobe rotation applied before pose). Normalised coordinates refer to the stored key-frame JPEG's width and height."

**M9 — medium — AD-13 — Canonical joint set and handedness are not decided.**
Issue: "AIcoach's own named-joint set" isn't enumerated, so two adapters and the measurement code can disagree. Measurements (trail hip, lead/trail side, sway) depend on handedness, and nothing says whether left-handed players are supported, detected or rejected.
Fix: "`Joint` enum: `nose, l/r_shoulder, l/r_elbow, l/r_wrist, l/r_hip, l/r_knee, l/r_ankle, l/r_heel, l/r_foot_index` (anatomical sides). One function maps to `lead/trail` from `handedness`. MVP `[ASSUMPTION]`: right-handed only; a left-handed swing → rejection `unsupported_handedness`, or add `handedness` to sign-up." Put in Open Questions if undecided.

**M10 — medium — AD-11 — FR-9 fallback and the FR-13 exclusion aren't representable or validated.**
Issue: FR-9 Notes: if two faults fail SM-1, ship them as "possible" only. `rules.yaml` has only active vs reserve. FR-13: an extra measurement that is an active fault must never be used for an observation.
Fix: "Each fault has `status: active | possible_only | reserve`; `possible_only` caps the outcome at `possible`. Schema validation rejects a file where an extra measurement's key equals an active or possible_only fault's measurement key."

**M11 — medium — AD-23, AD-16 — Limits have two owners.**
Issue: "settings and `rules.yaml` are the only source of limits", without saying which limit lives where; the 300 MB cap is in Caddy and the backend but not in the list or `/api/config`.
Fix: "App limits (`max_duration_s=15`, `formats`, `max_clips=50`, `max_upload_mb=300`, `slow_analysis_s=180`) live in settings. Engine and coach limits (fps floors 30/120, word limits 150/80) live in `rules.yaml`. `/api/config` returns both. The Caddyfile reads `MAX_UPLOAD_MB` from the same `.env`."

**M12 — medium — AD-20 — Consent text and version have no single source.**
Issue: the frontend label text and the stored `consent_version` can drift.
Fix: "`/api/config` returns `consent {version, text}`; the sign-up form renders that text and posts `consent_version`; the server refuses a version that isn't current."

**M13 — medium — AD-20, Conventions — Email and password rules not shared.**
Issue: if signup lowercases emails and signin doesn't, players can't sign in. bcrypt 5.x raises an error for passwords over 72 bytes, which becomes a 500.
Fix: Conventions: "Emails are trimmed and lowercased before storing and comparing (unique index on the lowercased value). Passwords: 8–72 UTF-8 bytes, validated by the same zod schema (generated limits) and by the backend, which returns 422 `password_invalid`."

**M14 — medium — AD-10, AD-19 vs EXPERIENCE — "Based on" contradiction.**
Issue: UX footnotes list pins and items ("wall drill", "rule table", "unverified observation (confidence: low)"); AD-19 says only evidence IDs.
Fix: "`based_on` is a list of refs, each `{type: evidence, id: E3}` or `{type: fact, key: drill|mobility|observation|rule_table|explanation}`; the check requires every evidence ref to be cited in the text and every fact ref to exist in `facts`."

**M15 — medium — Conventions (Tests, DB) — SQLite tests vs Postgres semantics.**
Issue: the spine relies on JSONB, `SELECT … FOR UPDATE` (ignored by SQLite) and FK cascades (off in SQLite by default). API tests on aiosqlite will pass while the limit lock and cascades are untested.
Fix: "Models use `JSON().with_variant(JSONB, 'postgresql')`; the SQLite test engine sets `PRAGMA foreign_keys=ON`; tests for the 50-clip limit, cascades and worker pick-up run against the Compose Postgres (`pytest -m pg`)."

**M16 — medium — AD-5, AD-15 — NFR-1 has no measurement definition.**
Issue: "completes analysis" can mean upload → result, queue → result, or engine only; LLM explanation and transcode may or may not count. Nothing produces the "median of 5" figure.
Fix: "NFR-1 time = `finished_at − started_at` of the job, including the `explanation` step in mock mode, excluding upload, queue and transcode. `aicoach-engine bench <clip> --runs 5` reports the median; step budgets come from the week-1 spike."

**M17 — medium — AD-21, AD-3 — OpenAPI location not under `/api`.**
Issue: Caddy routes only `/api/*` to the backend (technology.md also routed `/docs` and `/openapi.json`), so FastAPI's default schema URL is unreachable through the proxy, and the generation source for `schema.d.ts` isn't fixed.
Fix: "FastAPI serves `openapi_url=/api/openapi.json`, `docs_url=/api/docs` (docs off when `APP_ENV=demo`). `npm run gen:api` generates from `backend/openapi.json`, which `uv run python -m app.export_openapi` writes and CI checks for drift."

**M18 — medium — AD-15, AD-16, EXPERIENCE ready-to-send — Slo-mo/VFR and client-side fps.**
Issue: iPhone slo-mo exported through the browser picker can come out as a slowed 30 fps file whose duration exceeds 15 s, so valid swings get a 4xx; the ASSUMPTION has no decision path. Browsers can't read fps, so the UX "· 120 fps" on the phone preview can't be built.
Fix: AD-15: "If the spike shows slowed exports, duration is computed from capture time (`r_frame_rate` / metadata) and this AD is updated before upload stories start. The client pre-checks only extension, size and duration (fail-open if metadata can't be read); fps is shown only after the server probe (in the 'Got it — … at 120 fps' line)." Flag it to UX as a copy change.

**M19 — medium — AD-2, AD-8 — Cross-slice deletion ownership.**
Issue: account delete (identity) cascades into swings/coach tables via FK and must remove `users/{id}/` files, which `swings` owns through FileStore. AD-2 says other slices change rows only through the owner's service.
Fix: "Cross-slice row removal happens only through `ON DELETE CASCADE` FKs. `identity.delete_account` calls `swings.service.purge_user_files(user_id)` after commit; no slice other than `swings` deletes under `users/`."

### Low

- **L1 — low — AD-16 vs AD-8.** AD-16 "Prevents … a clip with no analysis" while AD-8 creates exactly that ("Analysis deleted"). Fix: "…a clip *uploaded* without an analysis".
- **L2 — low — AD-6 vs AD-16.** AD-6 lists duration among ingest checks in `pose`, AD-16 refuses >15 s at upload. Fix: "Duration and format are checked at upload (4xx); decode, fps, view and framing in `pose`."
- **L3 — low — Design Paradigm table vs Source tree.** Adapters at `backend/engine/adapters/` vs `backend/engine/aicoach_engine/adapters/`. Pick one.
- **L4 — low — AD-4.** Is the original filename stored (UX upload echo on reload)? Fix: "`clips.original_filename` is stored for display only; never in paths, logs or `CoachFacts`."
- **L5 — low — AD-5 / EXPERIENCE.** "Taking longer" at 3 min: expose `started_at` and `slow_analysis_s` (see M11).
- **L6 — low — AD-22.** Upload progress needs `XMLHttpRequest` (fetch has no upload progress). Fix: "The upload is the one call made with XHR, wrapped in a TanStack mutation."
- **L7 — low — AD-22.** Public routes and redirect-after-sign-in aren't stated (see H3 route list); state "a 401 from `/api` sends the browser to `/signin?next=…`".
- **L8 — low — AD-18.** State that the Mock adapter's sample answers and the templates are built from `CoachFacts` and pass `grounding_check` (SM-7/SM-13 in mock mode).
- **L9 — low — AD-6, AD-9.** Observation rephrase runs in the `explanation` step; `observation.text_source` and `explanation.source ∈ llm | template` are stored.
- **L10 — low — AD-9.** Policy for reading older `schema_version` rows, and stable measurement `key`s across rule-table versions (needed for FR-17).
- **L11 — low — AD-10.** "A UI pin shows the item's position number" → "the pin label is the numeric part of the evidence ID", so reordering never renumbers.
- **L12 — low — AD-15, NFR-7.** Note that distro ffmpeg with libx264 is GPL (fine as a separate CLI binary; list it for the pre-launch licence review).
- **L13 — low — Ops.** Add: Compose `healthcheck`/`depends_on` for db; README notes for the Windows firewall on port 8080 and `host.docker.internal` (Linux needs `extra_hosts`) in dev mode; disk-space note (50 × up to 300 MB × 2 copies); back up `EVAL_DATA_DIR` and `labels.yaml` (losing the author's test set before 12-15 is a project-ending risk); lockfiles are the authority for versions (several Stack versions can't be verified); CSP is deferred.
- **L14 — low — AD-18, §6.1.** Player-typed chat history may carry personal data to the LLM. Note it as accepted, or say "question text is sent as typed; nothing else from the player".
- **L15 — low — Capability map.** Add NFR-5 (AD-3, AD-21 Range, AD-22) and NFR-6 (AD-22) rows.
- **L16 — low — AD-6, FR-14.** Say whether a rejection gets an explanation (the spine's stop-early implies none). Fix: "A rejection has no explanation; its copy is per-reason templates from `rules.yaml`, and `AnalysisResult` for a rejection has no fault outcomes."
- **L17 — low — AD-15, SM-11.** An undecodable clip can't be transcoded, so SM-11 ("every clip … can be played back") fails for it; state `playback_state=failed` and accept it in SM-11's wording.
- **L18 — low — AD-1, AD-2.** Make the import rules mechanical: an `import-linter` contract (engine independent of app/fastapi/sqlalchemy/httpx/pydantic_ai; `swings` must not import `coach`) run in pytest.

---

## Summary counts

| Severity | Count |
|---|---|
| Critical | 0 |
| High | 8 |
| Medium | 19 |
| Low | 18 |
