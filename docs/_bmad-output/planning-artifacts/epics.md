---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - docs/prd/prd.md
  - docs/prd/addendum.md
  - docs/_bmad-output/planning-artifacts/architecture/architecture-AIcoach-2026-11-25/ARCHITECTURE-SPINE.md
  - docs/_bmad-output/planning-artifacts/architecture/architecture-AIcoach-2026-11-25/setup-guide.md
  - docs/_bmad-output/planning-artifacts/ux-designs/ux-AIcoach-2026-11-11/DESIGN.md
  - docs/_bmad-output/planning-artifacts/ux-designs/ux-AIcoach-2026-11-11/EXPERIENCE.md
---

# AIcoach - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for AIcoach, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

Numbering follows the source documents so stories trace back: `FR-n` / `NFR-n` / `SM-n` = PRD, `AD-n` = architecture spine, `AR-n` = additional requirement extracted here, `UX-DRn` = UX design requirement extracted here. Build tiers from PRD §8.1: **P1** core (done by 2026-12-01), **P2** coach chat (done by 2026-12-08), **P3** stretch.

## Requirements Inventory

### Functional Requirements

**Account and data ownership (P1)**

- FR-1: A visitor can create an account with email and password after ticking the library consent (unticked by default; no account without it), and a player can sign in and sign out. The sign-up screen states what is stored (swing clips, results, key frames, chat) and that the player can delete any of it. An email already in use is refused with a clear message. Passwords are never stored in plain text. Upload, results, history, swing library and coach chat require sign-in.
- FR-2: A player can see only their own analyses, results and swing clips; requesting another player's item by ID (URL or API) returns "not found"/"forbidden", never the data.
- FR-3: A player can delete any analysis (after confirmation: result, key frames and chat removed; the swing clip stays in the library) and can delete their account (all analyses, results, key frames, chats and swing clips removed; sign-in no longer possible).

**Filming guide and upload (P1)**

- FR-4: A player can view a filming guide stating: DTL view only; camera at hand height, level, on or parallel to the hands line; about 2.4–3.7 m (8–12 ft) away; tripod or stable surface; 120 fps or higher recommended; whole body and club in frame for the full swing; one swing per clip; good light. Readable on a phone without horizontal scrolling; states that AIcoach reads right-handed swings only; each rejection reason links to the guide step that addresses it.
- FR-5: A player can upload one swing clip (mp4 or mov, ≤15 s) from a mobile or desktop browser. Other formats or longer clips are refused before analysis with a message stating the limit; the player sees the analysis is in progress until a result or rejection is ready; at 50 swing clips a new upload is refused with a message to delete a clip first.

**Swing analysis (P1)**

- FR-6: The system finds the swing in the clip, detects address, top and impact (evaluation set: impact within ±1 frame, top within ±2 frames of the label, at the clip's own fps; address = last still moment before takeaway), and computes the measurements for the verified faults. Distances are relative to body size at address. The analysis module runs from a CLI/test harness without the web app or language model.
- FR-7: Every measurement and every verified fault carries a confidence band (high/medium/low) built from landmark visibility in the key frames, margin to the deciding threshold, and swing-event clarity. Never shown without a band; clips under 120 fps never get "high"; over the top capped at "medium" while measured from the hand path; on the evaluation set "high" verified faults are correct more often than "low" (SM-5).
- FR-8: The system rejects an unusable clip with "Cannot analyse", reasons and filming tips. Reasons include at least: not DTL, body or club out of frame, no swing detected, more than one swing, too dark or blurred. 30–119 fps clips are analysed with a visible warning; under 30 fps are rejected. A rejection is stored as an analysis and its clip goes into the swing library.

**Verified faults and fault chains (P1)**

- FR-9: Using the rule table, the system decides for each active fault (early extension, loss of posture, over the top; sway as reserve) whether it is verified (past fault threshold), possible (between potential and fault threshold) or absent. Possible faults get no chain, drill or mobility exercise and do not count as reported faults. Thresholds are configurable without code changes, start from the addendum §B patent values, and are tuned only on the tuning set. Sway is defined in the rule table from the start so a swap is configuration only.
- FR-10: For each verified fault, the player sees the fault chain (cause → mechanism → fault), the measurement value with its band, and at least one key frame with the relevant body lines drawn. Every chain link shows the measurement, key frame and band it rests on; an unmeasurable cause is labelled "likely cause" and names the measured mechanism pointing to it. Key frames shown match the swing events the rule uses.
- FR-11: For each verified fault, the player sees one drill and one mobility exercise from the fixed library (per the rule-table mapping), each with short instructions; every mobility exercise carries the "generic guidance, not medical advice — see a physiotherapist on pain" notice.
- FR-12: When no verified fault is present, the result says "No verified fault found", shows none of the faults as verified, lists the faults checked (possible ones labelled "possible"), and shows no chain, drill or mobility exercise; the explanation names no fault.

**Unverified observation (P1)**

- FR-13: A result shows at most one unverified observation, only when an extra measurement passes its threshold (the one furthest past its threshold if several). It is visually separated, labelled "Unverified — confirm with a coach", always band "low", never names a drill or mobility exercise, can appear with "No verified fault found" or next to a verified fault, names only its own measurement and numbers in the analysis (same check as FR-14), never uses a measurement that is a fault in the active rule table, and in mock mode shows the template text unchanged. Initial extra-measurement list: sway (while reserve).

**Explanation and mock mode (P1)**

- FR-14: The player can read a grounded, plain-language explanation: mentions only the verified faults, causes, drills, mobility exercises and numbers in the analysis (automated check); exactly one feel cue per verified fault; ≤150 words; no jargon-blocklist terms; suggests no fault for a rejection or "No verified fault found"; if the language model is unavailable the result is still shown with a template explanation.
- FR-15: AIcoach runs end to end in mock mode with no API keys, paid accounts or network access to a language model: following the README on a clean laptop, the bundled test clips produce complete results; in mock mode the coach chat gives fixed sample answers.

**History and comparison (P3, stretch)**

- FR-16: A player can list past analyses, newest first, and open any result; an analysis whose clip was deleted still appears, marked "clip deleted".
- FR-17: A player can choose two analyses and see the same measurement side by side with both confidence bands; different bands are visibly marked so the player does not read a change into noise.

**Swing library (P1)**

- FR-18: Every uploaded swing clip (including rejections) is stored in the player's swing library, linked to its analysis, until the player deletes it or the account. The result screen states the clip is in the swing library; there is no save toggle. No clip is ever stored for a player without the library consent.
- FR-19: A player can list their swing clips (newest first, with date and main finding, or "Cannot analyse"), play any of them on phone and laptop browsers, open its analysis, and delete any clip after confirmation with the choice "delete clip, keep analysis" or "delete clip and analysis" (video file removed from disk either way). A kept analysis leaves a "clip deleted" row with no playback that can be opened and deleted and does not count toward the 50-clip limit.

**AI coach chat (P2)**

- FR-20: A player can ask questions about one result and get short, grounded answers. Available on results only (verified fault or "No verified fault found"), never on a rejection, only once the result exists. Answers mention only content and numbers in that analysis (FR-14 check), cite each number, never raise a band, never call a possible fault or observation verified or prescribe for them, are ≤80 words, avoid the jargon blocklist, and end with a "Based on:" note. Not-measured, other-swings, pain/injury, competitive-round and off-topic questions are refused in one sentence with one next step (pain → physiotherapist notice only). The chat is stored with its analysis, shown on reopen, deleted with it. Language model unavailable → chat disabled with a plain message, result unchanged; mock mode → fixed sample answers.

### NonFunctional Requirements

- NFR-1 Performance: a 10 s swing clip completes analysis in under 2 minutes and a 15 s clip in under 3 minutes on the author's target laptop (median of 5 runs; measured as `finished_at − started_at` incl. mock explanation, excl. upload, queue and transcode — AD-5).
- NFR-2 Local processing and hosting: runs on a local laptop; a phone on the same Wi-Fi can open the app and upload; pose estimation runs locally; swing clips are never sent to third parties. Public hosting is next phase.
- NFR-3 Testability: the analysis module is runnable and testable in isolation; the labelled test set runs as an automated suite.
- NFR-4 Examiner runnability: installation and start-up follow the README with no paid accounts or keys (mock mode).
- NFR-5 Mobile-friendly: filming guide, upload and result screens work on a phone browser.
- NFR-6 Language: UI and explanations are in English.
- NFR-7 Licensing: all bundled models and libraries permit later commercial use; a non-commercial component (SwingNet) only as a replaceable, off-by-default fallback listed for removal before a paid launch; YOLO-pose (AGPL) banned.
- NFR-8 Repository hygiene (FR-19, §6.1): swing clips are stored outside the code repository and never committed; secrets live in git-ignored `.env`, `.env.example` is committed; bundled test clips are of the author, with consent to publish.
- NFR-9 Language-model data minimisation (§6.1): explanation, observation and chat receive analysis data only — never swing clips, key frames, email or other personal data.
- NFR-10 Cost (§6.3): zero running cost in mock mode; real model use has a known, small cost per analysis and per chat question, logged per call (OQ2).
- NFR-11 Safety and honesty (§6.2): every measurement shows a confidence band; no launch-monitor precision claims; mobility exercises carry the medical notice; AIcoach presents itself as a practice tool, not for competitive rounds.
- NFR-12 Privacy and retention (§6.1): clips, results, measurements, key frames and chats are kept until the player deletes them or the account; at most 50 swing clips per player; data export is next phase.

**Verification targets (PRD §10, measured on the evaluation set unless stated):** SM-1 detection ≥75 % with ≥4 clips per verified fault · SM-2 "No verified fault found" on ≥2 of ≥3 clean clips · SM-3 no forced fit on ≥3 clips outside the three faults · SM-4 complete early-extension result · SM-5 honest confidence (high correct more often than low, if ≥3 per band) · SM-6 face-on and out-of-frame rejections · SM-7 grounded explanation check · SM-8 speed (NFR-1) · SM-9 isolation · SM-10 examiner run from the README in mock mode · SM-11 swing-library retention · SM-12 comparison (stretch) · SM-13 grounded chat check. Counter-metrics SM-C1–C3 are not optimised.

### Additional Requirements

**Starter / scaffold (affects Epic 1 Story 1)**

- AR-1 No third-party starter template. Greenfield scaffold per `setup-guide.md` §4: uv workspace with `backend/` (app, Python 3.14) and `backend/engine/` (package `aicoach-engine`); backend deps (FastAPI, uvicorn, SQLAlchemy async + asyncpg, Alembic, pydantic-settings, PyJWT, bcrypt, python-multipart, pyyaml, pydantic-ai-slim[openrouter]); engine deps (numpy, scipy, `opencv-contrib-python-headless` as the only cv2 with uv `exclude-dependencies` for other OpenCV builds, pydantic, pyyaml, pose backend); dev deps (pytest, pytest-asyncio, httpx, aiosqlite, import-linter). Frontend via `create-next-app@16` (TS 5.x, Tailwind, ESLint, App Router, src dir), `shadcn@4.23.0 init` with the component base chosen explicitly, TanStack Query, zod, openapi-typescript, Vitest, Playwright; `next.config.ts` with `output: "standalone"` and `allowedDevOrigins` from `DEV_LAN_ORIGIN`. `.gitignore`: `.env`, `/data/`, `*.mp4`/`*.mov` except `samples/`, `backend/models/*` except `MANIFEST.yaml`, `node_modules/`, `.venv/`. Source tree as in the spine's Structural Seed.
- AR-2 Week-1 spike (setup-guide §8), before the pose and upload stories: time MediaPipe Full/Heavy vs RTMPose-m on the target laptop on the trimmed window; compare hip/shoulder/wrist stability at address/top/impact; check ffprobe fps **and duration** of an iPhone slow-motion export (amend AD-15 before upload stories if it fails); check the backend runs in `python:3.14-slim` with `ffmpeg libegl1 libgles2` and whether arm64 wheels exist; fill `models/MANIFEST.yaml` (URL, SHA-256, licence); record the choice in the architecture memlog and set `POSE_BACKEND` in `.env.example`.

**Infrastructure and environments**

- AR-3 One origin (AD-3, AD-25): Docker Compose with `db` (postgres:18, port bound to 127.0.0.1 only), `backend` (python:3.14-slim + ffmpeg/libegl1/libgles2, model files fetched at build, exactly one Uvicorn process, never `--workers`), `frontend` (Next standalone, node:26), `proxy` (Caddy 2.11 on `0.0.0.0:${HTTP_PORT:-8080}`, `/api/*` → backend with `request_body max_size 300MB`, everything else → frontend). `docker compose up` is the canonical demo/examiner run; dev runs only `db` + `proxy` with backend/frontend on the host via `BACKEND_UPSTREAM`/`FRONTEND_UPSTREAM`. `APP_ENV` local|demo (demo turns off `/api/docs` and controls sample seeding). LAN HTTP only. Images build for linux/amd64; arm64 best effort.
- AR-4 Environment variables (setup-guide §3) all present in `.env.example` with safe defaults: core (`APP_ENV`, `DATABASE_URL`, `POSTGRES_*`, `JWT_SECRET`, `ACCESS_TOKEN_EXPIRE_MINUTES`=43200, `DATA_DIR`, `HTTP_PORT`), analysis (`POSE_BACKEND`, `MODELS_DIR`, `EVENT_DETECTOR`=wrist, `RULES_PATH`, `MAX_UPLOAD_MB`=300, `MAX_CLIP_SECONDS`=15, `MAX_CLIPS_PER_PLAYER`=50, `ANALYSIS_TIMEOUT_SECONDS`=600, `SLOW_ANALYSIS_SECONDS`=180, `EVAL_DATA_DIR`), LLM (`LLM_MODE`=auto, `OPENROUTER_API_KEY`, `OPENROUTER_MODEL`, `LLM_TIMEOUT_SECONDS`=20, `AI_USD_NOK`=10.5), features/dev (`FEATURE_CHAT`=true, `FEATURE_HISTORY`=false, upstreams, `DEV_LAN_ORIGIN`). No `NEXT_PUBLIC_*` variables.
- AR-5 Phone on Wi-Fi (setup-guide §6.3): README documents finding the laptop IP, the Windows Firewall rule for port 8080 (Private profile), the Private network profile, client-isolation workaround (phone hotspot), and `DEV_LAN_ORIGIN` for dev.

**Engine (analysis core)**

- AR-6 Pure engine (AD-1): `aicoach_engine` imports nothing from `app`, FastAPI, SQLAlchemy, HTTP clients or LLM libraries; `analyse(video_path, rules, out_dir, on_step=None) -> AnalysisResult` writes only into `out_dir`; CLI `aicoach-engine analyse <clip>`, `eval --split tuning|evaluation`, `bench <clip> --runs 5`; an import-linter contract in pytest enforces AD-1 and AD-2.
- AR-7 Rule table as configuration (AD-11): `config/rules.yaml` parsed only by `load_rules(path) -> RuleTable` (Pydantic, `extra="forbid"` at every level), loaded once at startup, invalid file stops the app. Sections: `faults` (status active|possible_only|reserve, thresholds, measurement key, cause, drill, mobility, feel cue), `observations` (extra measurements + templates), `confidence` (caps, fps floors 30/120), `coach` (word limits 150/80, jargon blocklist, medical notice, refusal texts, template explanations, mock answers), `guide_steps` (slug list), `reasons` (code → guide_step). Schema rejects an observation whose key belongs to an active/possible_only fault. Swap = `status` edit.
- AR-8 Outcomes and bands (AD-12): outcome from thresholds only (past fault → verified, past potential → possible, else absent; `possible_only` caps at possible); a band never changes an outcome. One `confidence.band(measurement, rule, events, visibility, fps)` combining visibility, margin to nearest interval boundary and event clarity, with caps (<120 fps never high, over the top ≤ medium). Fault band = deciding measurement's band; absent has none; observation always low. Code outside the engine only displays bands.
- AR-9 Pose port (AD-13): `PoseEstimator` → `PoseSequence` (`frame_w`, `frame_h`, per frame `{frame_index, t_ms, joints}`); fixed `Joint` enum (nose, l/r shoulder, elbow, wrist, hip, knee, ankle, heel, foot_index) with normalised x/y (origin top-left) and visibility 0–1 mapped by each adapter; one lead/trail mapping fixed to right-handed (no handedness detection); VideoReader applies rotation once at decode (upright, full, uncropped frames everywhere); distances/angles only after `to_px()`, then body-relative units and a 6 Hz Butterworth filter; only adapters import `mediapipe` (Tasks PoseLandmarker) or `rtmlib`; `POSE_BACKEND` selects, name recorded in the result; model files from `models/MANIFEST.yaml` loaded from `MODELS_DIR`, never downloaded at runtime.
- AR-10 Event port (AD-14): `EventDetector` returns address, top, impact each with `clarity`; event frames are 0-based indices into the full decoded stream at native fps plus `t_ms` everywhere (engine, result, labels); trimming offsets removed inside the engine; default = wrist-height heuristic; SwingNet only as an optional, off-by-default adapter. Trim to the ~2 s swing window before pose (addendum §A).
- AR-11 `AnalysisResult` is the one result document (AD-9): defined in the engine with `schema_version`, stored as JSON in `analyses.result`; contains `clip`, `clip_checks` + `fps_warning`, `events`, `measurements` (key, label, value, unit, display, band, thresholds with display), `faults` (outcome, band, deciding_measurement, chain with role/label/likely/evidence_ids, drill, mobility), `observation`, `film_better`, `reasons` (code, guide_step, label, detail), `evidence`, `explanation {text, source}`, `main_finding`, `step_timings`, `rules_hash`, `pose_backend`, plus overlay geometry (AD-17). Labels and coaching text are snapshotted from `rules.yaml`; one engine formatter produces every `display`; `main_finding` set by the engine (highest-band verified fault, ties by rules order; else `no_fault`/`cannot_analyse`); old `schema_version` → `409 result_outdated`.
- AR-12 Evidence IDs (AD-10): stable `E1…En` per result (pins show the number; never renumbered); the only citation syntax is `[E<n>]`, parsed by one regex in `coach/grounding.py` mirrored in `frontend/src/shared/evidence/citations.ts`, both tested against a shared fixture; `based_on` is a structured list (`{type: evidence, id}` | `{type: fact, key: drill|mobility|observation|rule_table|explanation}`).
- AR-13 Key frames and overlays (AD-17): key frames stored as plain JPEGs of the full upright frame (scaled, never cropped); overlay geometry (points, lines, arrows, dashed address line) lives in `AnalysisResult` normalised to that JPEG; the frontend draws it as SVG with DESIGN.md tokens; alt text uses the event's `t_ms`.

**Backend application**

- AR-14 Slices and ownership (AD-2): `identity` owns `users`, `swings` owns `clips`/`analyses`, `coach` owns `chat_messages`; cross-slice access only via owner service functions; `coach` may import `swings`, never the reverse (coach registers an `ExplanationWriter` with the worker at startup); only `swings` writes under `DATA_DIR/users/`; written exceptions: `identity.service.lock_user` is the only per-user lock, cross-slice row removal only via `ON DELETE CASCADE`, `delete_account` commits then calls `swings.service.purge_user_files`.
- AR-15 FileStore (AD-4): all player files through `FileStore` rooted at `DATA_DIR`, paths from IDs only (`users/{user_id}/clips/{clip_id}/original.{ext}|playback.mp4|thumb.jpg`, `users/{user_id}/analyses/{analysis_id}/keyframes/{event}.jpg`); engine scratch in `DATA_DIR/tmp/{analysis_id}/`, imported by the worker then deleted; system files (generated JWT secret) in `DATA_DIR/system/`; `original_filename` for display only (never in paths, logs or CoachFacts); startup orphan sweep walks only `users/` and `tmp/` and retries failed deletes.
- AR-16 Analysis job (AD-5): the `analyses` row is the job; one in-process worker claims with `UPDATE … WHERE id=(SELECT … status='queued' ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED) RETURNING id`; engine runs in a one-process pool; `on_step(step_id, state, detail, partial_evidence)` via a multiprocessing queue → `analyses.progress {steps (all five, fixed order, pending|running|done|skipped|stopped), partial_evidence}`; client polls `GET /api/analyses/{id}` ~1/s; timeout `ANALYSIS_TIMEOUT_SECONDS` from `started_at` kills and recreates the pool then writes `failed`; on startup: orphan sweep → `running` rows set `failed` → worker starts.
- AR-17 Status machine and terminal write (AD-6): `queued → running → result | rejection | failed`, `failed → queued` on retry; steps `pose → events → measurements → rules → explanation`; ingest checks (decodability, fps, view, framing, swing count, light) run in `pose`; a rejection marks its step `stopped`, later `skipped`, carries `reasons [{code, guide_step}]`, gets no explanation or fault outcomes, copy from `rules.yaml`; `ExplanationWriter.write(result) -> ExplanationOut {explanation_text, observation_text|null, source: llm|template|mock}` never touches the DB, has its own 20 s timeout, any exception → templates, never produces `failed`; the worker alone does one terminal `UPDATE … WHERE id=:id AND status='running'` (0 rows → delete everything it imported); retry only from `failed` with clip present (else `409 retry_not_allowed`), atomically resets status/progress/result/error/timestamps; each run first deletes the analysis's key-frame folder.
- AR-18 Ownership and access (AD-7): every `clips`/`analyses`/`chat_messages` row has `user_id`; every `repo.py` function takes `user_id` and returns `404 not_found` for others' rows; cross-user functions (`claim_next_queued`, `fail_running_on_startup`, `finish_job`, `list_ids_for_sweep`) only in `swings/repo_system.py`, importable only by `worker.py` and the startup hook (test asserts); deny-by-default auth on `/api` except signup, signin, config, health; `current_user` reloads the user row each request, missing → `401 session_invalid` + cookie cleared.
- AR-19 Deletion, races and the limit (AD-8): delete-clip-keep-analysis (clip row deleted, `analyses.clip_id` → NULL, clip files removed), delete-clip-and-analysis (both rows, chat cascades, clip files + key frames), delete-analysis (row + chat; clip stays; key frames removed), delete-account (users row, everything cascades, `purge_user_files`); file deletes after commit; deleting a clip/analysis while queued/running → `409 analysis_in_progress`; account delete always allowed (worker's conditional terminal write cleans up); the limit = count of `clips` rows; upload does a fast pre-check, then in one short transaction `lock_user` → re-check → insert → move file.
- AR-20 Video handling (AD-15): upload route checks in order: library count, extension (mp4/mov), ffprobe finds a video stream, container duration ≤15.0 s; the engine checks everything else and never re-checks extension/duration; fps single source = engine VideoReader (`avg_frame_rate`, recorded in the result; browser never shows fps before that); after the terminal write the same worker slot runs ffmpeg to make `playback.mp4` (H.264) and `thumb.jpg` (owned by the clip, excluded from NFR-1); `clips.playback_state` pending|ready|failed; video endpoint returns `409 playback_not_ready`/`409 playback_unavailable`, never 404, for an existing clip; original served if it is H.264 and the transcode failed; media endpoints support HTTP Range (iOS).
- AR-21 Upload contract (AD-16): `POST /api/clips` multipart, the one call made with XHR (upload progress); `MAX_UPLOAD_MB` (300, decimal) enforced by Caddy and backend, frontend maps Caddy's bare 413 to `upload_too_large`; route refusals return 4xx with a code, delete the temp file, create no row; accepted uploads stream outside the transaction, then create the `clips` row (`playback_state=pending`) and a `queued` analysis together and return `{analysis_id, clip_id}`; an unusable clip becomes a stored `rejection`, not a 4xx.
- AR-22 Sessions, CSRF and consent (AD-20): HS256 JWT in an `httpOnly`, `SameSite=Lax` cookie, 30 days, `Secure` only over HTTPS; empty `JWT_SECRET` → generated once and persisted in `DATA_DIR/system/`, a known default value refused; one middleware requires `X-Requested-With: aicoach` on every non-GET/HEAD `/api` request (auth included; fetch client and upload XHR set it); emails trimmed + lowercased with a unique index; passwords 8–72 UTF-8 bytes else `422 password_invalid` before bcrypt; `/api/config` returns `consent {version, text}`, sign-up posts `consent: true` + `consent_version`, server refuses missing/outdated versions and stores version + timestamp on `users`.
- AR-23 OpenAPI contract (AD-21): response models reference engine Pydantic models (no `dict`/`Any`); `uv run python -m app.export_openapi` writes committed `frontend/openapi.json`; `npm run gen:api` generates `src/shared/api/schema.d.ts`; hand-written domain types fail lint; a test catches a stale `openapi.json`; error envelope always `{"error": {"code", "message"}}` with codes from one list in `app/core/errors.py` (422 included); `/api/openapi.json`, `/api/docs` (off in demo).
- AR-24 Runtime config and flags (AD-23): settings hold app limits (15 s, mp4/mov, 300 MB, 50 clips, `slow_analysis_s`=180), `FEATURE_CHAT`, `FEATURE_HISTORY`, `LLM_*`; `rules.yaml` holds engine and coach limits; `GET /api/config` returns both plus `mock_mode`, `chat_enabled`, `consent`, `guide_steps`. Chat off three ways: cut (`FEATURE_CHAT=false` → UI hides, endpoints `404 feature_disabled`), wrong status (`409 chat_not_available`), model down (`503 llm_unavailable`, composer disabled, nothing stored). `GET /api/analyses` (Account list) is P1; `FEATURE_HISTORY` gates only P3 history/compare UI and `GET /api/analyses/compare`. Mock mode when `LLM_MODE=mock` or key empty; never fails on a missing key; per-result label from `explanation.source`, global label from `mock_mode`.
- AR-25 Seed endpoints (spine Structural Seed): identity `POST /api/auth/signup|signin|signout`, `GET /api/me` (email, analyses_count, clips_count), `DELETE /api/me`; swings `POST/GET /api/clips`, `GET /api/clips/{id}`, `/video`, `/thumb`, `DELETE /api/clips/{id}?keep_analysis=`, `GET /api/analyses` (P1), `GET /api/analyses/{id}`, `POST /api/analyses/{id}/retry`, `DELETE /api/analyses/{id}`, `GET /api/analyses/{id}/keyframes/{event}`, `GET /api/analyses/compare` (P3); coach `GET/POST /api/analyses/{id}/chat` (P2); system `GET /api/config`, `GET /api/health`. `GET /api/clips` returns `{rows: [LibraryRow], count, limit}` newest first; `LibraryRow = {row_id, clip_id|null, analysis_id|null, created_at, state: analysing|result|rejection|failed|clip_deleted|analysis_deleted, main_finding_label|null, band|null, playback_state|null, thumbnail_url|null}`; `clip_deleted` rows don't count; the frontend never derives `state` or the finding.

**Coach (language model)**

- AR-26 One LLM gateway (AD-18): only `coach` calls the model, through `CoachLLM` with `explain(facts) -> {body, feel_cues [{fault_key, text}], observation_text|null, based_on}` and `answer(facts, history, question) -> {kind: answer|refusal, refusal_class: not_measured|other_swings|pain|competition|off_topic|null, text, based_on}`; input is only `CoachFacts` (projection of `AnalysisResult`) plus the question text — never email, user ID, clip, image or path; OpenRouter adapter (`pydantic-ai-slim[openrouter]`) built only when `OPENROUTER_API_KEY` is set; Mock adapter builds answers from `CoachFacts` + `rules.yaml` mock texts and passes the grounding check; tokens and cost logged per call. Model chosen at P2 start (OQ2).
- AR-27 One grounding check (AD-19): `grounding_check(output, facts, kind)`; allowed names per kind (`explanation`: verified faults + their causes/drills/mobility, none for no-fault; `observation`: only its measurement; `chat`: any fault in facts with its outcome word, never a drill for possible/observation); allowed numbers = `display` values + numbers inside drill/exercise text (evidence IDs excluded); band word next to a fault must match; word limits on `text`/`body`; jargon blocklist; exactly one feel cue per verified fault; cited/`based_on` evidence IDs must exist. Fail → template for explanation/observation; chat retried once then fixed refusal stored (`source: refusal`); `pain` → medical notice. Every template and mock answer in `rules.yaml` is run through the check in a test.

**Frontend**

- AR-28 Frontend is only a UI (AD-22): no DB access, no server actions or route handlers for data; all data from `/api` via TanStack Query; 401 → `/signin?next=…`; shadcn@4.23.0 primitives restyled only through Tailwind v4 `@theme` tokens from DESIGN.md; English copy; fixed routes: public `/`, `/signin`, `/signup`, `/guide`, `/guide/[slug]`; signed in `/swing/new`, `/swing/[analysisId]`, `/library`, `/library/[clipId]`, `/account`; guide step element IDs = `guide_steps` slugs from `/api/config` (test checks). Coaching copy comes from `rules.yaml` via `AnalysisResult` or `/api/config`, never from components.

**Data, conventions and quality**

- AR-29 Conventions (spine): UUIDv4 IDs generated by the backend; UTC ISO 8601 with `Z`, local date in the frontend; `value` + `unit` (`body_height_ratio`, `deg`, `ms`, `frames`) + `display`, and UI/LLM use only `display`; PRD glossary words in code; snake_case JSON with generated TS types; enums per spine; errors: not yours → 404, job-state conflict → 409, model down → 503.
- AR-30 Database: one Alembic migration per story rebased onto head; a test checks exactly one head and upgrade → downgrade → upgrade on Postgres; `alembic upgrade head` at startup; never `rollback()` on the shared session, use `ON CONFLICT DO NOTHING`; `JSON().with_variant(JSONB, "postgresql")`; SQLite tests set `PRAGMA foreign_keys=ON`; locks, cascades and claims tested on Postgres (`pytest -m pg`); FK `analyses.clip_id` nullable, unique, `ON DELETE SET NULL`; `chat_messages` → analyses `ON DELETE CASCADE`; users → children cascade.
- AR-31 Logging and observability: plain structured lines to stdout with `analysis_id`; never log emails, passwords, file contents or chat text; per-step timings stored in `AnalysisResult`; LLM tokens and cost per call. No metrics stack.
- AR-32 Test stack: pytest (engine unit tests, grounding fixed-input tests SM-7/SM-13, API tests with httpx AsyncClient on SQLite/aiosqlite, `-m pg` Postgres tests, import-linter contract), Vitest (UI logic, citation regex fixture, guide slugs), one Playwright smoke test = UJ-5 in mock mode, `aicoach-engine eval` and `bench`.
- AR-33 Evaluation harness (AD-24): `eval/labels.yaml` committed (`{clip_file, split: tuning|evaluation, faults, events {address, top, impact: frame_index}}`, frame indices per AR-10); clips read from `EVAL_DATA_DIR` (outside Git, backed up); bundled author samples in `samples/` for README/mock demo (plain Git if ~20 MB, else LFS); tuning and eval run in the backend container; the SM report records `rules_hash` and `pose_backend`; tuning tools refuse the `evaluation` split.
- AR-34 Test-set production (PRD §10, issues log — author work that gates P1 checks; tracked as stories): film at 120/240 fps, hand height, on the hands line; label separate tuning and evaluation sets (evaluation: ≥4 per fault, ≥3 clean, ≥3 outside the three faults) with swing-event frames; back up `EVAL_DATA_DIR` off the laptop.
- AR-35 Decision checkpoints (tracked as stories): over the top vs sway decided on the tuning set by 2026-12-01 (OQ4; a `status` edit) and the replacement extra measurement if swapped (OQ7); thresholds and body-relative units tuned on the tuning set (OQ3); language model and cost chosen at P2 start (OQ2); `FEATURE_CHAT=false` if chat is not done by 2026-12-08.
- AR-36 Hand-in (setup-guide §9, PRD §8.1 last week 2026-12-08 → 12-15): clean-machine `docker compose up --build` with copied `.env` gives a full mock result (SM-10); `git ls-files "*.mp4" "*.mov"` lists only `samples/`; `.env.example` complete without secrets; README links the run and phone-on-Wi-Fi sections; non-commercial components listed for removal (NFR-7); evaluation-set run and SM report; NFR-1 bench on the target laptop.

### UX Design Requirements

**Foundation and tokens**

- UX-DR1 Design tokens: implement every DESIGN.md frontmatter token in Tailwind v4 `@theme` — colours (paper, paper-2, card, hairline, ink, ink-2, ink-on-dark, ink-on-dark-2, clay, on-clay, evidence-teal, evidence-tint, on-evidence, evidence-idle, ruler-track, confidence-high/medium/low, on-confidence, keyframe-*, body-line, ghost-body, club, ball, scrim, shadow-hero), the typography scale (display-hero … mono-meta), radii (bar 1 … full) and spacing (1–8, gutter-mobile 20, panel-padding 32, card-padding 24, thread-width 640, rail-width 232, evidence-width 408, section-gap-landing 120). Light theme only. Restyle shadcn primitives only through these tokens.
- UX-DR2 Fonts: Newsreader (400, 500, 600, italic 400/500), Figtree (400–700), IBM Plex Mono (400, 500, 600) with fallbacks Georgia / Arial / Consolas; minimum size 12px; measured values inside serif text in mono at ~0.86×. Fonts must load on a phone that reaches the laptop over Wi-Fi without internet (DESIGN.md OQ3) — Decided 2026-11-25: self-host via `next/font` at build time (resolves DESIGN.md OQ3).
- UX-DR3 Colour and line semantics: teal only for measurement (values, pins, citations, "Based on", ruler fill, cited frame outline); clay only for the coach and the one primary CTA per screen; confidence colours always with word + bars; solid outline = measured, dashed = inferred/unverified/pending (dash 5 4 for chain links, unverified cards and placeholders; 7 6 drop zone; 3 3 no-thumbnail tiles; 9 7 address line); depth tonal (paper / paper-2 / card + 1px hairline), no card shadows except the landing hero card; no new hues, gradients or red error fills. "possible" chip on card with hairline border (5.6:1) rather than paper-2.
- UX-DR4 Responsive layout: ≥1344px three columns (rail 232 · thread 640 content · sticky Evidence panel 408); 1024–1343px rail + thread, Evidence becomes a right drawer opened from the header Evidence chip; 768–1023px rail collapses to the ≡ menu sheet, thread full width (max 640), Evidence drawer; <768px phone layout (top bar with ≡/back, title + meta, Evidence chip; one column, 20px gutter; actions in the bottom third; Evidence as pull-up tray).
- UX-DR5 App shell and navigation: signed-in desktop left rail (wordmark linking to latest thread, "New swing" dark button, recent swings list of the latest 3–5 rail swing rows, Swing library · Filming guide · Account, mock-mode label in the footer); phone ≡ menu sheet with the same content and back chevron on sub-pages; signed-out landing header (How it works · When it says no · Sign in · Create account), also used by the public filming guide; empty rail on first visit shows only "New swing".
- UX-DR6 Coach mark and wordmark: clay circle with paper flag on a short pin and a ground stroke; wordmark "AI" clay italic Newsreader + "coach" ink (24px rail, 34px sign-in).

**Conversation thread**

- UX-DR7 One thread per swing: upload, analysing and outcome live in one thread at `/swing/[analysisId]` (from `/swing/new` after upload); the page can be left during analysis and the rail row shows "Analysing…"; after analysis a collapsed system line (40px paper-2 pill: "Clip received · file · 3.8 s · analysed in 41 s" + Show/Hide) folds the upload exchange.
- UX-DR8 Coach message: mark + italic "Coach" + time, Newsreader body, no bubble, one or two sentences, never a number without a pin, arrives whole (no token streaming), announced politely. Typing indicator: mark + three dots + "Coach is watching your swing…" (none in chat), not re-announced.
- UX-DR9 Player message: right-aligned ink bubble (max 384px) with name · time meta; upload echo shows first-frame thumbnail, file name and length in mono (never fps) and a 4px clay progress bar while uploading.
- UX-DR10 Composer, grounding note, suggested prompts, "Based on" footnote (P2): composer card pill with ink border and clay send button, enabled only once a result exists, Enter sends / Shift+Enter newline, disabled while awaiting an answer, empty input not sendable, hidden on rejections, disabled state "You can ask the coach once the result is ready."; grounding note always visible and undismissible ("Answers are based only on this analysis — no new faults, numbers or drills."; phone short form); suggested prompts (three on desktop wrapping to two rows, one full-width on the phone) from a fixed list per result type, sent as the player's message, refreshed after each answer, never suggesting something that would be refused; "Based on:" footnote in mono teal listing pins (as citation links) and items, refusals list what was checked.
- UX-DR11 Confidence in words: high → "and I'm sure of it"; medium → "I'm fairly sure"; low → "but I can't be sure from this clip" + one line on what to film better linked to the guide step.

**Result**

- UX-DR12 Result page header: title, meta line, and the library status "In your swing library ›" (label, ink-2, no pill) linking to the clip detail; reads "Clip deleted" (not a link) when the clip is gone; on the phone under the top-bar meta. Never a save control.
- UX-DR13 Jump-to chips: "Jump to" + Verdict · Why · Practise · Also checked · Ask the coach (34px pills, active = ink); active chip follows scroll; "Ask the coach" focuses the composer; one entry per fault when several; chat chip hidden if chat is cut; no scroll animation under reduced motion.
- UX-DR14 Verdict card: always first; desktop split by a vertical hairline (left "Verified fault" label, fault name, confidence band; right pin, measurement name, value in teal mono 46px, unit, "rule: 4%"); phone one card with fault, band, value (40px) and the two key-frame thumbnails; activating pin/value cites it; one card per verified fault ordered by band.
- UX-DR15 Feel cue: clay quote mark, cue in italic Newsreader (21px / 17px phone), meta "Feel cue · check it in the impact frame [2]"; exactly one per verified fault.
- UX-DR16 Fault chain card: three links left→right with 18px ink-2 arrows — Likely cause (`chain-link-inferred`, dashed, labelled "Likely cause"), Mechanism (`chain-link-measured`), Fault · verified (`chain-link-verified`); each with label, title, inline mono teal value + pin, band; legend "Dashed = inferred from a pointer, not measured directly." directly under it.
- UX-DR17 Exercise card: two halves (Drill · for <fault> / Mobility · for the likely cause) with name (clay, 23px), dose (mono), two or three lines of instruction; the mobility half always carries the undismissible medical notice "Generic guidance, not medical advice — see a physiotherapist if you feel pain."; never shown for a possible fault or an observation; on the phone behind "Next: what to practise · 1 drill · 1 mobility".
- UX-DR18 Also checked card: title + count; one row per other rule-table fault with name, status chip ("possible" in medium colour / "not found" in ink-2, text only), band, pin; a possible fault shows its measurement and "No drill."; always visible on desktop, one tap below practice on the phone.
- UX-DR19 Confidence band component: three 4×11px bars + the word in the same colour (high 3 lit, medium 2, low 1; unlit 25 %), text always "confidence: high|medium|low", never colour-only or a percentage; screen readers read the word; never omitted; never "high" under 120 fps; over the top never above "medium".
- UX-DR20 Unverified observation card: dashed ink-2 outline on paper, label "Unverified — confirm with a coach" exactly, observation in italic Newsreader, band low, "No drill: this is not in my rule table."; at most one; placed after Also checked or on the no-fault screen, never inside verdict/chain/practice.
- UX-DR21 No-verified-fault outcome: coach "No verified fault found" + one line, "Checked: early extension · loss of posture · over the top" (possible ones labelled), optional observation card, "Ask the coach about this" (secondary); without an observation the line "None of my three rules fired, and nothing else stood out that I can measure. That's a real answer." and suggested prompt "What did you check in my swing?"; no exercise card, no chain.
- UX-DR22 Disclosure rows (expand in place, state not persisted): "Read my full explanation · n words" (collapsed by default, ≤150 words); "n more measurements ›" (each with value, band, pin); "Clip checks passed · n of n" (view, frame, fps checks; 30–119 fps warning here and in the thread); phone "Next: what to practise".

**Evidence**

- UX-DR23 Evidence pins and inline citations: teal 18px square with white mono number (1–2 key frames, 3+ measurements), inline raised `[n]`; activating highlights the matching item (tint + teal outline) and scrolls it into view — panel on desktop, drawer on narrow laptop, tray on phone; latest answer's citations stay lit until the next answer; accessible names like "Evidence 3, hip movement toward the ball, 7% of body height, confidence high".
- UX-DR24 Key frame: 322:360 frame on keyframe ground showing the stored JPEG still (scaled, never cropped) as the background, with the overlay geometry from `AnalysisResult` drawn on top as SVG (body-line skeleton 3.4px with round joins, keypoint dots, ghost-body capsules, club line with ball, floor band); hip keypoint ringed; address frame draws a dashed vertical reference line through the address hip; impact frame repeats it, overlays the address pose dashed and draws a "+n%" dimension arrow; name + event time under each frame; cited frame gets a teal outline 3px outside; activating opens it larger in a sheet with the same overlays; alt text states event, time and what the overlay shows; frames match the rule's swing events.
- UX-DR25 Measurement card and threshold ruler: tint card with teal border, name, value (52px mono), ruler (track, teal fill 0→value, ink tick at the fault threshold, card-filled marker with teal ring at the value, mono labels "0%", "rule 4%", max), band; a possible fault also shows the potential threshold tick.
- UX-DR26 Evidence panel (desktop ≥1344): sticky card column with "Evidence" title, teal pin icon, pin count, subtitle; before upload: "Where to put the phone" top-down diagram + placeholders + "0 pins · Nothing measured yet."; analysing: frames and the measurement fill in as steps finish ("2 pins so far", "drawing lines…", "measuring…"); result: two key frames side by side (164px, 16px gap), dashed-line legend, cited measurement card, "n more measurements", "Clip checks passed".
- UX-DR27 Evidence placeholders: dashed paper boxes with centred meta labels standing in for anything not yet there (also on cold load), replaced in place; never a spinner anywhere.
- UX-DR28 Evidence chip, tray and drawer: chip "Evidence · n" (teal on tint; idle paper-2 before any pin), phone top bar right / narrow-laptop header right; phone tray = bottom sheet with 40×5 grab handle, "Evidence · pinned live", horizontal row of frames and measurements, peeks with live pins during analysis, swipe down / scrim closes; drawer = panel content at 408px from the right over the scrim, traps focus, closes with Esc, close button or scrim.

**Upload and analysis**

- UX-DR29 New swing (waiting for a clip): coach message asking for one DTL swing, the checklist as the message, link to the guide, drop zone, composer disabled, Evidence panel pre-upload state.
- UX-DR30 Drop zone: 640px card with dashed ink-2 border (7 6), upload circle, "Drop your swing clip here", "or choose a file · mp4 or mov · max 15 s", hairline, library note "Goes into your swing library" + "Stored on the AIcoach server until you delete it. Only you can see it." (information, not a control); desktop drag-and-drop or pick, a valid clip sends at once; phone opens Photos/Files then goes to ready-to-send; client pre-checks format and length (advisory; server re-checks) with coach-voice inline refusals ("That clip is 22 s. I can read up to 15 s — trim it and send it again." / "I read mp4 or mov files."); one clip at a time; disabled at the limit (paper-2 fill, "Your swing library is full (50 clips). Delete a clip before sending a new one." + link to the library); maps 413 to the too-large message.
- UX-DR31 Ready-to-send preview (phone): preview card on keyframe ground with first frame and play mark, file name, "3.8 s of 15 s" (browser length), coach line "Looks right. Send it when you're ready.", library note card, "Send to the coach" (primary), "Choose a different clip" (text button).
- UX-DR32 Step log: card with five rows Pose · Swing events · Measurements · Rule table · Explanation; 10px status circles joined by a line; states done (green + check), active (clay partial ring), pending (hairline ring), stopped (ink-2 ring + ×), later rows pending/skipped; mono details right-aligned; 4px clay progress bar with "n of 5"; typing indicator under it; the coach's fps line ("Got it — a clean down-the-line clip at 120 fps. Watching now.") appears once Pose reports fps from the server; progress announced through a polite live region without stealing focus.
- UX-DR33 Analysing edge states: after `slow_analysis_s` (180 s) the coach line "This is taking longer than it should. I'm still watching." with the step log in place and no action; on `failed` the running row shows "stopped", coach line "Something went wrong on my side, not with your clip. Nothing was analysed." with "Try again" (retry same clip) and "New swing"; the library row reads "Not analysed"; a failure never looks like a rejection or result.
- UX-DR34 Rejection outcome: step log stopped; "Cannot analyse" + "I won't guess from this clip. n things got in the way:"; one rejection reason row per reason (ink-2 ×, reason, one line of explanation, clay "Filming guide · step n ›" link to that step); primary "Film again"; footer "No result was made. The clip is in your swing library; delete it there if you don't need it."; no faults, no composer.
- UX-DR35 Frame-rate warning (30–119 fps): inline warning in the thread and in clip checks, "Filmed at 60 fps — nothing can be rated 'high'." (medium-coloured `!`).

**Forms, lists, pages**

- UX-DR36 Sign in and create account: text inputs (label above, errors on submit, not while typing); sign-in error "That email and password don't match."; create account with the consent checkbox between password and button — native checkbox, 22px box, 44px hit area, unticked by default, full consent text as label ("I understand that every swing clip I send is stored in my swing library on the AIcoach server until I delete it." — text served by `/api/config`), "Create account" disabled until ticked with `aria-describedby` meta "Tick the box to create your account."; right-handed meta line "AIcoach reads right-handed swings for now."; email in use → "An account with this email already exists. Sign in instead?" keeping entries and the ticked box; success lands on New swing signed in.
- UX-DR37 Filming guide: overview with six numbered rows (paper-2 circle, rule, chevron), the right-handed meta line, and "I'm ready to film" → New swing; step pages with "Step n of 6" (clay), the rule as headline, a card with the top-down placement diagram (dashed target line, phone block, ghost-body player ellipse, teal mono "2.4–3.7 m · 8–12 ft"), two to four lines of reason, six step dots (current clay), Back (secondary) / Next step (primary); slugs and element IDs from `/api/config` `guide_steps`; public; no horizontal scroll on a phone.
- UX-DR38 Swing library: list rows newest first (46px key-frame thumbnail, dashed tile for a rejection, date, main finding or "Cannot analyse"; "Analysing…", "Not analysed", "Analysis deleted", and "clip deleted" rows with dashed thumbnail and no play control; "Preparing playback…" poster); whole row is the target; trash icon opens the delete sheet; empty state "No swings yet. Every clip you send lands here." + "New swing"; a "clip deleted" row opens the analysis and its trash deletes the analysis.
- UX-DR39 Clip detail: page header (date, finding), video frame with native controls, no autoplay, on keyframe ground; "Open analysis" (primary), "Delete clip" (secondary); "Preparing playback…" dashed poster with no play control, polled until ready; playback failure states "This clip can't be played back." (server) and "This clip can't play in this browser." (browser) with the analysis still openable.
- UX-DR40 Account: email, "Your analyses" rows ("date · main finding" + meta "clip in swing library"/"clip deleted", trash icon), empty "No analyses yet.", sign out, "Delete account" (secondary); "See all n analyses" hidden until FR-16.
- UX-DR41 Delete confirmations (bottom sheets): analysis — "Delete this analysis? Its result and key frames are removed. The swing clip stays in your swing library."; clip — "Delete this clip?" with "Delete clip, keep analysis" / "Delete clip and analysis"; account — "Delete your account? This removes n analyses with their results and key frames, and n swing clips. It cannot be undone, and you will not be able to sign in again." with dark "Delete everything" and "Keep my account"; on success the row updates/disappears (account → signed out to landing); failure keeps the sheet open with "Couldn't delete. Nothing was removed. Try again."; delete controls disabled while the analysis is waiting/running with meta "You can delete this once the analysis has finished." (409 still handled inline); account delete always available.
- UX-DR42 Bottom sheet: card with 18px top corners over the scrim, 40×5 handle, panel-title, ink-2 consequences, full-width stacked actions; focus moves in and returns on close; Esc, swipe down or scrim tap closes (not while a delete is in progress); one level deep, never stacked.
- UX-DR43 Buttons: one clay primary per screen (52px, 56px phone), disabled primary (paper-2), secondary (card, 1.4px ink border), dark (ink, 44px: "New swing", destructive confirmations).
- UX-DR44 Landing page: header; hero (62px Newsreader headline, body, primary + secondary CTA, meta "For golfers between +2 and 15 handicap. A practice tool, not for competitive rounds."); non-interactive labelled example-result card with hero shadow; "The coach talks. The evidence stays pinned." legend; film → send → read row; three fault tiles; three honesty cards (Cannot analyse, No verified fault found, grounded refusal); ink closing band with clay CTA and privacy line "Your clips are private. Each one stays in your swing library until you delete it."; phone follows the phone rules (not mocked).

**System states and copy**

- UX-DR45 Global states: cold load uses dashed placeholders in the final layout (no spinners) and "Couldn't load this. Try again." inline on failure; network lost (upload, chat) "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." + "Try again" (an unsent chat question stays in the composer); not found / not yours "This analysis doesn't exist or isn't yours." + link to your swings; protected URL while signed out → Sign in → back to the URL; LLM unavailable → result complete with template explanation, composer disabled with "The coach can't answer questions right now. Your result is complete."; chat cut → no composer, prompts, grounding note, "Ask the coach" chip or link; mock-mode label "Mock mode" (meta, ink-2) on every signed-in page while mock mode is on.
- UX-DR46 Inline message pattern: one line of ink text under the control or section it concerns, small low-colour × (or medium `!` for warnings), cleared when the input changes or on retry; never a modal or banner; used for refused files, form errors, network errors, the fps warning and the "taking longer" line.
- UX-DR47 Chat refusal patterns (P2), one sentence + one next step, footnote naming what was checked: not measured ("I didn't measure your grip in this clip, so I can't tell you." + current drill or "ask a coach"); outside the rule table/unverified ("I have no drill I can stand behind. A coach can check it in person."); other swings ("I can only see this swing." + pointer to the library); pain (medical notice only); competitive round ("AIcoach is a practice tool, not for use during a round."); off topic ("I can only talk about this swing."). Suggested prompts: verified fault — "How do I know the drill is working?", "What does 'likely cause' mean?", "Can I do this drill in a net?"; no fault — "What did you check in my swing?".
- UX-DR48 Several verified faults: one verdict card, chain and exercise card per fault, ordered by confidence; jump chips gain one entry per fault (not mocked).

**Accessibility and interaction floor**

- UX-DR49 WCAG 2.2 AA on every surface: visible focus ring (2px evidence-teal, 2px offset) on every interactive element; touch targets ≥44×44px on the phone (34px chips, 18px pins and the 22px consent box keep their size with a 44px hit area); tab order = reading order; Space toggles the consent box, Enter sends chat, Esc closes the topmost sheet/drawer; sheets and drawer trap and return focus; polite live region for step log, new coach answers and completion; key-frame alt text ("Impact, 2.07 s. Hips 7% of body height closer to the ball than the dashed address line."); dashed/solid meaning also stated in words; reduced motion respected (no scroll animation, no pulse on lit pins); text scales to 200 % without loss; native video controls, no autoplay.
- UX-DR50 Banned patterns: autoplaying video, carousels, score dials, streaks, badges, confetti, push/email re-engagement, swipe-only actions, hover-only affordances, modal stacks deeper than one, any save toggle or save button for clips, the word "Saved" in copy, dashboards of measurements.

### Decisions at requirements confirmation (2026-11-25)

- Key frames: the stored JPEG still is the background and the skeleton and hip-line overlay is drawn on top as SVG (AD-17). DESIGN.md's "no photos" rule applies to illustrations (landing, marketing), not to key frames.
- Fonts are self-hosted with `next/font` at build time, so a phone without internet still renders them (DESIGN.md OQ3).
- Non-code work that gates P1 checks (the week-1 spike AR-2, test-set filming and labelling AR-34, decision checkpoints AR-35) is tracked as stories.
- EXPERIENCE.md's 7 remaining open questions are built as their stated `[ASSUMPTION]`s; copy sign-off can change text later without changing stories.

### Decisions at story review (2026-11-26, recorded in ARCHITECTURE-SPINE.md / setup-guide.md)

- Filming guide has six steps with the slugs `view`, `position`, `distance`, `frame-rate`, `framing`, `one-swing-light`; step 6 covers "one swing per clip" and "good light" (FR-4, AD-11).
- `AnalysisResult.reasons` gains `detail`, the one-line explanation per rejection reason, copied from `rules.yaml` (AD-9, UX-DR34).
- "Not found" rows in Also checked show the band of the deciding measurement; absent faults still have no fault band (AD-12, FR-7).
- Sample-clip "seeding" is a startup check only, creating no accounts or clips (FR-18); `docker-compose.yml` sets `APP_ENV=demo` for the backend (setup-guide §3.1).
- P3 routes `/history` and `/history/compare` behind `FEATURE_HISTORY` are added to the fixed route list (AD-22).
- Playback transcode lives in `swings/library/` and is registered through the after-terminal hook that Story 3.3 adds (AD-15).

### FR Coverage Map

| FR | Epic(s) | Note |
|---|---|---|
| FR-1 | Epic 1 | Account, library consent, sign in/out, protected routes |
| FR-2 | Epic 1 → 3, 4, 5 | Pattern (deny-by-default, `user_id` repos, 404) in Epic 1; applied per endpoint in each slice; SM-9 verified in Epic 5 |
| FR-3 | Epic 1, Epic 5 | Account delete (empty account) in Epic 1; analysis delete and file purge in Epic 5 |
| FR-4 | Epic 3 | Filming guide slice |
| FR-5 | Epic 3 | Upload incl. 50-clip limit check |
| FR-6 | Epic 2 | Engine: pose, events, measurements, CLI |
| FR-7 | Epic 2, Epic 4 | Band computed in the engine; displayed in the result |
| FR-8 | Epic 2, Epic 3 | Engine checks; rejection outcome in the thread |
| FR-9 | Epic 2, Epic 4 | Outcomes from the rule table; verdict and Also checked UI |
| FR-10 | Epic 2, Epic 4 | Chain, evidence IDs, overlay geometry; chain and key-frame UI |
| FR-11 | Epic 2, Epic 4 | Mapping in `rules.yaml`; exercise card + medical notice |
| FR-12 | Epic 2, Epic 4 | No forced fit in the engine; no-fault outcome UI |
| FR-13 | Epic 2, Epic 4 | Observation selection in the engine; rephrase + card |
| FR-14 | Epic 4 | Grounded explanation via `CoachLLM` + grounding check |
| FR-15 | Epic 4, Epic 6, Epic 8 | Mock explanation; mock chat; README examiner run |
| FR-16 | Epic 7 | Analysis history (P3) |
| FR-17 | Epic 7 | Compare two analyses (P3) |
| FR-18 | Epic 3, Epic 5 | Clip stored on every upload; library status + retention checks |
| FR-19 | Epic 5 | Library list, playback, delete clip |
| FR-20 | Epic 6 | Coach chat (P2) |

## Code Organisation (vertical slices)

Decided 2026-11-25 with the user and recorded in `ARCHITECTURE-SPINE.md` (AD-2, Structural Seed). Each epic is one vertical slice with its own folders in backend, frontend and tests. Shared code lives in shared folders; slices never reach into each other's internals.

**Shared folders** (no slice owns them; slices import them, never the reverse):

| Folder | Holds | Created in |
|---|---|---|
| `backend/engine/aicoach_engine/` | The analysis library (AD-1) | Epic 2 |
| `backend/app/core/` | Settings, DB session, FileStore, auth dependency, CSRF, error envelope | Epic 1 |
| `config/rules.yaml` | Rule table, coaching copy, guide steps (AD-11) | Epic 2 |
| `frontend/src/shared/ui/` | shadcn primitives restyled with DESIGN.md tokens: button, input, checkbox, sheet, list row, inline message, placeholder, disclosure row, status chip | Epic 1 |
| `frontend/src/shared/layout/` | App shell, rail, top bar, menu sheet, landing header (with slots for slice content) | Epic 1 |
| `frontend/src/shared/api/` | Generated `schema.d.ts`, fetch client, upload XHR, query keys (AD-21; replaces `src/lib/api/`) | Epic 1 |
| `frontend/src/shared/conversation/` | Coach message, player message, typing indicator, collapsed system line | Epic 3 |
| `frontend/src/shared/evidence/` | Evidence panel / drawer / tray shells, evidence chip, placeholder, pin, confidence band (Epic 3); citation, key frame SVG, measurement card + threshold ruler (added in Epic 4) | Epic 3, extended in Epic 4 |

**Slices:**

| Epic | Backend | Frontend |
|---|---|---|
| 1 | `app/modules/identity/`, `app/modules/system/` | `src/modules/identity/`, `src/modules/landing/`, `src/modules/account/` (email, sign out, delete account) |
| 2 | `engine/` package, `eval/` | — |
| 3 | `app/modules/swings/upload/`, `app/modules/swings/analysis/` (job, worker) | `src/modules/guide/`, `src/modules/upload/` |
| 4 | `app/modules/swings/analysis/` (result read), `app/modules/coach/explanation/` | `src/modules/result/` |
| 5 | `app/modules/swings/library/` (list, playback, delete) | `src/modules/library/`; extends `src/modules/account/` with the analyses list |
| 6 | `app/modules/coach/chat/` | `src/modules/chat/` |
| 7 | `app/modules/swings/history/` | `src/modules/history/` |
| 8 | repo level (README, samples, eval report) | Playwright smoke test |

**Rules:**

1. A slice imports only `shared/`, `core/`, the engine, and another slice's **public interface** (`service.py` backend, `index.ts` frontend) — never its internals. Backend direction stays as AD-2: `coach` may use `swings`, never the reverse.
2. `shared/` never imports a slice. Where the shell needs slice content (e.g. recent swings in the rail), the route layer `frontend/src/app/` composes them; it is the only composition root.
3. DRY: a component needed by a second slice moves to `shared/` in the story that adds the second use. Components the UX spec already names as shared (confidence band, pin, key frame, coach message) start in `shared/`.
4. Enforced by import-linter contracts (backend, extends AD-1/AD-2) and ESLint `no-restricted-imports` / boundaries rules (frontend), both run by the test suite.
5. Table ownership is unchanged (AD-2): `swings` owns `clips` and `analyses` across its sub-slices; sub-slices share the `swings` models and `repo.py`/`repo_system.py`, and each keeps its own routes and service.

**Cross-epic hand-offs** (so no story depends on a later epic):

- Epic 1 deletes an account by removing the `users` row; the first story that writes player files (Epic 3 upload) adds `swings.service.purge_user_files` and wires it into `identity.delete_account` (AD-2), so files are never orphaned. Each later table joins the cascade in its own migration (`chat_messages` in Epic 6).
- Epic 2 delivers `analyse()`, `load_rules()`, `AnalysisResult` and `config/rules.yaml` (incl. `guide_steps`, `reasons`, coach templates and mock texts) with no web dependency; Epic 3 consumes them.
- Epic 3 ends an analysis with the engine result plus a template explanation from `rules.yaml` and shows a plain verdict summary (main finding + band); Epic 4 registers the `CoachLLM`-backed `ExplanationWriter` and replaces the summary with the full result view.
- Epic 3 shows a "Not analysed" / "Cannot analyse" state only in the thread; the swing library list (`GET /api/clips`, `LibraryRow`) and the rail's recent swings arrive in Epic 5. Links to `/library` may exist earlier.
- Epic 4 renders no working chat: while `chat_enabled` is true it shows only the disabled composer ("You can ask the coach once the result is ready."); when `chat_enabled` is false nothing chat-related shows (cut state, UX-DR45). Epic 6 enables the composer, grounding note, prompts and the "Ask the coach" chip and link.

## Epic List

Build order follows PRD §8.1: Epics 1–5 = P1 (2026-12-01), Epic 6 = P2 (2026-12-08, cut switch `FEATURE_CHAT`), Epic 7 = P3 stretch, Epic 8 = final week (2026-12-08 → 12-15). Epics 1 and 2 share no code and can run in parallel.

### Epic 1: Sign up and sign in, on the laptop and the phone

A visitor can open AIcoach from a phone or laptop on the same Wi-Fi, read the landing page, create an account with the library consent, sign in, sign out and delete the (still empty) account. Lays the shared base every later slice uses: scaffold, one-command `docker compose up`, design tokens and fonts, app shell, `/api/config`, cookie auth + CSRF, protected routes and the not-found page.
**FRs covered:** FR-1, FR-2 (pattern), FR-3 (account delete) · **Slice:** identity, system + shared base · **Also:** NFR-2, NFR-5, NFR-6, NFR-8 · AR-1, AR-3–AR-5, AR-14, AR-18, AR-22–AR-25, AR-28–AR-32 · UX-DR1–UX-DR6, UX-DR36, UX-DR42–UX-DR44, UX-DR46, UX-DR49, UX-DR50

### Epic 2: The analysis engine gives an honest verdict from the command line

The author (and the examiner) can run `aicoach-engine analyse <clip>` and get a complete `AnalysisResult`: swing events, measurements with confidence bands, verified / possible / absent faults with fault chains, drill and mobility, at most one unverified observation — or a rejection with reasons. Starts with the week-1 spike; includes filming and labelling the test set, the eval harness on the tuning set and the over-the-top vs sway checkpoint.
**FRs covered:** FR-6, FR-7, FR-8 (engine checks), FR-9, FR-10–FR-13 (data side) · **Slice:** engine, eval · **Also:** NFR-3, NFR-7 · AR-2, AR-6–AR-13, AR-33–AR-35

### Epic 3: Film, send, and watch the coach analyse the swing

A player reads the filming guide, sends a clip from phone or desktop, and watches the step log in a thread at one URL, ending in a rejection (reasons linked to guide steps), a failure with "Try again", or a plain verdict summary. Every clip lands in the swing library; the 50-clip limit is enforced.
**FRs covered:** FR-4, FR-5, FR-8 (UI), FR-18 (storage) · **Slice:** guide, swings/upload, swings/analysis (job) · creates `shared/conversation` and the Epic-3 part of `shared/evidence` · **Also:** NFR-1 (timings), NFR-2 · AR-15–AR-17, AR-20, AR-21 · UX-DR7–UX-DR9, UX-DR29–UX-DR35, UX-DR37, UX-DR45, UX-DR46

### Epic 4: Read the full result with its evidence and the coach's explanation

The full result thread: verdict, feel cue, fault chain, practice with medical notice, Also checked, unverified observation, the no-fault outcome, key frames with overlays, measurement ruler and the Evidence panel / drawer / tray; plus the grounded explanation through `CoachLLM` (template, mock, OpenRouter), so mock mode works end to end.
**FRs covered:** FR-7, FR-9–FR-15 (UI and explanation) · **Slice:** result, coach/explanation · extends `shared/evidence` (citation, key frame, measurement card, ruler) · **Also:** NFR-9, NFR-10, NFR-11 · AR-26, AR-27 · UX-DR11–UX-DR28, UX-DR48

### Epic 5: Keep, rewatch and delete my swings

The swing library (rows and the rail's recent swings), clip detail with playback (transcode, "Preparing playback", Range requests), deleting a clip with the keep / delete-analysis choice, the account's analysis list with delete, and account deletion that removes files. Verifies isolation and retention (SM-9, SM-11).
**FRs covered:** FR-2, FR-3, FR-18, FR-19 · **Slice:** swings/library, account · **Also:** NFR-8, NFR-12 · AR-19 · UX-DR38–UX-DR41

### Epic 6: Ask the coach about my result (P2)

A grounded chat on a result: cited answers that light the evidence pins, refusals, "Based on" notes, mock answers, and the three ways chat can be off. Model and cost chosen at epic start (OQ2).
**FRs covered:** FR-20, FR-15 (mock chat) · **Slice:** coach/chat · **Also:** NFR-9, NFR-10 · AR-24 (chat flags), AR-26, AR-27 · UX-DR10, UX-DR47

### Epic 7: See my progress across swings (P3, stretch)

Analysis history including "clip deleted" rows, and comparing two analyses on one measurement with both confidence bands, behind `FEATURE_HISTORY`.
**FRs covered:** FR-16, FR-17 · **Slice:** swings/history · **Also:** SM-12

### Epic 8: The examiner runs AIcoach from the README, and the numbers are in

Bundled sample clips, README, the Playwright UJ-5 smoke test, a clean-machine run, the evaluation-set SM report, the NFR-1 bench on the target laptop and the hand-in checklist.
**FRs covered:** FR-15 (README path) · **Slice:** repo level · **Also:** NFR-1, NFR-4, NFR-7 · AR-36 · SM-1–SM-13


## Epic 1: Sign up and sign in, on the laptop and the phone

A visitor can open AIcoach from a phone or laptop on the same Wi-Fi, read the landing page, create an account with the library consent, sign in, sign out and delete the (still empty) account. The epic also lays the shared base every later slice uses: the scaffold, a one-command `docker compose up`, design tokens and self-hosted fonts, the app shell, `/api/config`, cookie auth with CSRF, protected routes and the not-found page.

### Story 1.1: Scaffold AIcoach and serve it on the laptop and the phone with one command

As the developer (and later the examiner),
I want a greenfield repo that `docker compose up` serves through one origin on port 8080,
So that every later story builds on the same stack and a phone on the same Wi-Fi can reach the app.

**Slice:** repo root (`docker-compose.yml`, `Caddyfile`, `.gitignore`, `.env.example`, `README.md`, `config/`, `samples/`, `eval/`); `backend/` (uv workspace, `Dockerfile`, `app/main.py`, `app/core/settings.py`, `app/core/db.py`, `app/modules/system/`, `migrations/`, `models/MANIFEST.yaml`, `tests/`); `backend/engine/` (package stub); `frontend/` (create-next-app, shadcn init, `Dockerfile`, `next.config.ts`, `src/app/`, `src/shared/`, `src/modules/`)
**Requirements:** AR-1, AR-3, AR-4, AR-5, AR-25 (health), AR-30 (startup upgrade), AR-32, NFR-2, NFR-8, AD-3, AD-25

**Acceptance Criteria:**

**Given** an empty `G121-naalsund/` working tree with uv 0.13+, Node 26 LTS and Docker Engine 29.x
**When** the backend is scaffolded per setup-guide §4
**Then** `backend/` is a uv workspace app on Python 3.14 whose member `backend/engine/` is the package `aicoach-engine` (importable `aicoach_engine`, an empty stub that imports nothing from `app`, FastAPI, SQLAlchemy, HTTP clients or LLM libraries) (AR-1, AD-1)
**And** the app depends on fastapi, `uvicorn[standard]`, `sqlalchemy[asyncio]`, asyncpg, alembic, pydantic-settings, pyjwt, bcrypt, python-multipart, pyyaml and `pydantic-ai-slim[openrouter]`, and the dev group has pytest, pytest-asyncio, httpx, aiosqlite and import-linter (AR-1)
**And** the engine depends on numpy, scipy, `opencv-contrib-python-headless`, pydantic and pyyaml, and `[tool.uv] exclude-dependencies = ["opencv-python", "opencv-contrib-python", "opencv-python-headless"]` is set. `[ASSUMPTION]` the pose-backend dependency (mediapipe and/or rtmlib + onnxruntime) is added by the week-1 spike (AR-2), not here (AR-1)
**And** `uv.lock` is committed

**Given** the backend scaffold
**When** the frontend is scaffolded with `npx create-next-app@16 frontend --ts --tailwind --eslint --app --src-dir --use-npm --import-alias "@/*"` and `npx shadcn@4.23.0 init`
**Then** TypeScript stays on 5.x, the shadcn component base (Base UI or Radix) is chosen explicitly and recorded in `components.json`, `@tanstack/react-query` and `zod` are dependencies, and `openapi-typescript`, `vitest` and `@playwright/test` are dev dependencies. `[ASSUMPTION]` `jsdom`, `@testing-library/react` and `@testing-library/user-event` are added as dev dependencies for component tests (AR-1, AR-32)
**And** `next.config.ts` sets `output: "standalone"` and `allowedDevOrigins: process.env.DEV_LAN_ORIGIN ? [process.env.DEV_LAN_ORIGIN] : []` (AR-1, AD-25)
**And** `package-lock.json` is committed

**Given** both scaffolds
**When** the source tree is inspected
**Then** it matches the spine's Structural Seed: `backend/app/{core,modules/system}`, `backend/app/migrations/` (Alembic env, async engine, no revisions yet), `backend/models/MANIFEST.yaml` (`[ASSUMPTION]` `models: []` until the spike fills it, AR-2), `backend/tests/`, `frontend/src/{app,modules,shared/{ui,layout,api}}`, and `config/`, `samples/` and `eval/` at the root (`[ASSUMPTION]` kept with `.gitkeep` until Epics 2 and 8 fill them), plus `Caddyfile`, `docker-compose.yml`, `.env.example` and `README.md` (AR-1)

**Given** the root `.gitignore`
**When** `git check-ignore` runs on `.env`, `data/x.bin`, `clip.mp4`, `clip.mov`, `backend/models/pose.task`, `frontend/node_modules/x` and `backend/.venv/x`
**Then** all of them are ignored, while `samples/ee-01.mp4` and `backend/models/MANIFEST.yaml` are not (AR-1, NFR-8)
**And** `git ls-files "*.mp4" "*.mov"` lists nothing outside `samples/` (NFR-8)

**Given** `.env.example`
**When** it is compared with setup-guide §3
**Then** it lists every variable with its safe default: `APP_ENV=local`, `DATABASE_URL`, `POSTGRES_USER/PASSWORD/DB`, empty `JWT_SECRET`, `ACCESS_TOKEN_EXPIRE_MINUTES=43200`, `DATA_DIR`, `HTTP_PORT=8080`, `POSE_BACKEND` (empty, with a comment that the week-1 spike sets it), `MODELS_DIR`, `EVENT_DETECTOR=wrist`, `RULES_PATH=config/rules.yaml`, `MAX_UPLOAD_MB=300`, `MAX_CLIP_SECONDS=15`, `MAX_CLIPS_PER_PLAYER=50`, `ANALYSIS_TIMEOUT_SECONDS=600`, `SLOW_ANALYSIS_SECONDS=180`, empty `EVAL_DATA_DIR`, `LLM_MODE=auto`, empty `OPENROUTER_API_KEY`, `OPENROUTER_MODEL`, `LLM_TIMEOUT_SECONDS=20`, `AI_USD_NOK=10.5`, `FEATURE_CHAT=true`, `FEATURE_HISTORY=false`, `BACKEND_UPSTREAM=backend:8000`, `FRONTEND_UPSTREAM=frontend:3000` and empty `DEV_LAN_ORIGIN` (AR-4)
**And** it holds no secret value and no `NEXT_PUBLIC_*` variable (AR-4, NFR-8)
**And** `app/core/settings.py` (pydantic-settings) loads the core variables, ignores variables that later slices read, and starts with every optional variable empty (AR-4)

**Given** `docker-compose.yml` and `Caddyfile`
**When** they are reviewed against setup-guide §5
**Then** `db` is `postgres:18` with its port bound to `127.0.0.1:5432` only, a `pg_isready` healthcheck and the `pgdata` volume mounted on `/var/lib/postgresql` (AR-3)
**And** `backend` builds from `python:3.14-slim` with `ffmpeg libegl1 libgles2`, mounts the `data` volume on `/data` and `config/`, `samples/` and `eval/` read-only, waits for a healthy `db`, and runs exactly one process, `uvicorn app.main:app --host 0.0.0.0 --port 8000`, never with `--workers` (AR-3, AD-5)
**And** `frontend` builds a Next standalone image on `node:26-alpine` (AR-3)
**And** `proxy` is `caddy:2.11` published on `0.0.0.0:${HTTP_PORT:-8080}`, and the `Caddyfile` routes `/api/*` to `{$BACKEND_UPSTREAM:backend:8000}` with `request_body max_size 300MB`, and everything else to `{$FRONTEND_UPSTREAM:frontend:3000}` (AR-3, AD-3)
**And** images build for linux/amd64 (AR-3)

**Given** a fresh clone with `.env` copied from `.env.example` and no edits
**When** `docker compose up --build` runs
**Then** all four services start, the backend runs `alembic upgrade head` before it serves requests (a no-op with no revisions yet), and `http://localhost:8080/` serves a frontend page. `[ASSUMPTION]` this is a plain "AIcoach" placeholder that Story 1.7 replaces with the landing page (AR-3, AR-30)
**And** `GET http://localhost:8080/api/health` returns `200 {"status": "ok"}` from `app/modules/system/routes.py` after a `SELECT 1` on the database (AR-25)

**Given** the laptop on a Private Wi-Fi network with the firewall rule from the README
**When** a phone on the same Wi-Fi opens `http://<laptop-ip>:8080` and `http://<laptop-ip>:8080/api/health`
**Then** both load. This is a manual check, recorded in the story's completion notes (NFR-2, AR-5)

**Given** the README
**When** a reader follows it
**Then** it has a "Run" section (setup-guide §6.1), a "Dev" section (§6.2: `docker compose up db proxy`, `uv run alembic upgrade head`, `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`, `npm run dev`, `BACKEND_UPSTREAM`/`FRONTEND_UPSTREAM` set to `host.docker.internal`, always browsing through `http://localhost:8080`, and `DATA_DIR` outside the repo such as `D:/aicoach-data`), and a "Phone on the same Wi-Fi" section (§6.3: `ipconfig`, the exact `New-NetFirewallRule -DisplayName "AIcoach 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow -Profile Private` command, the Private network profile, the phone-hotspot workaround for client isolation, and `DEV_LAN_ORIGIN` for dev) (AR-5, AD-25, NFR-8)
**And** in dev mode the same URLs work through Caddy on :8080, and with `DEV_LAN_ORIGIN` set the phone loads the `npm run dev` assets (AD-25)

**Given** the test stack
**When** `uv run pytest` runs in `backend/`
**Then** a health test passes using httpx `AsyncClient` (ASGI transport) on SQLite/aiosqlite, `asyncio_mode` is set, the `pg` marker is registered, and `pg` tests skip with a clear reason when no Postgres URL is configured. `[ASSUMPTION]` the URL comes from a `TEST_DATABASE_URL` variable, and `uv run pytest -m pg` runs those tests against the Compose `db` (AR-32, AR-30)
**And** `npm test` in `frontend/` runs Vitest (jsdom) with one passing smoke test, and Playwright is configured with no tests yet, since the UJ-5 smoke test belongs to Epic 8 (AR-32)

### Story 1.2: Give the API one contract, a runtime config, CSRF protection and enforced slice boundaries

As the developer,
I want typed API responses generated into the frontend, one error shape, a public `/api/config`, a CSRF guard and import rules that fail the tests,
So that every later slice talks to the backend the same way and cannot reach into another slice's internals.

**Slice:** `backend/app/core/` (`errors.py`, `csrf.py`, `logging.py`, `settings.py`), `backend/app/modules/system/`, `backend/app/export_openapi.py`, `backend/.importlinter`, `backend/tests/`; `frontend/openapi.json`, `frontend/src/shared/api/` (`schema.d.ts`, `client.ts`, `queryKeys.ts`, `index.ts`), `frontend/src/app/` (providers, placeholder page), `frontend/eslint.config.mjs`, frontend Vitest
**Requirements:** AR-14, AR-22 (CSRF), AR-23, AR-24 (`mock_mode`), AR-25 (system), AR-28, AR-29, AR-31, AR-32, AD-1, AD-2, AD-21, AD-23

**Acceptance Criteria:**

**Given** `app/core/errors.py`
**When** any `/api` request fails
**Then** the response body is always `{"error": {"code": "<code>", "message": "<text>"}}`, and every code comes from the one list in `errors.py` (AR-23, AR-29)
**And** handlers cover the app's own `ApiError(status, code, message)`, Starlette `HTTPException` (unknown `/api` path → `404 not_found`, wrong method → `405 method_not_allowed` `[ASSUMPTION code]`), `RequestValidationError` (→ `422 validation_error` `[ASSUMPTION code]`), and unhandled exceptions (→ `500 internal_error` `[ASSUMPTION code]`, logged without the request body) (AR-23)
**And** a pytest test asserts that each handler emits the envelope and that every code a route can raise is a member of the list (AR-23)

**Given** the database is unreachable
**When** `GET /api/health` is called
**Then** it returns `503` with the envelope and code `database_unavailable` `[ASSUMPTION code]` (AR-23)

**Given** the CSRF middleware in `app/core/csrf.py`
**When** an `/api` request with a method other than GET or HEAD arrives without the header `X-Requested-With: aicoach`
**Then** it is refused with `403` and code `csrf_header_missing` `[ASSUMPTION code]` before routing, so even `POST /api/health` gets 403, not 405 (AR-22)
**And** the same request with the header passes on to routing (`POST /api/health` → `405 method_not_allowed`), GET and HEAD need no header, and non-`/api` paths are untouched (AR-22)

**Given** `GET /api/config` in the system slice
**When** a signed-out client calls it
**Then** it returns `200` with a typed Pydantic `ConfigOut` holding `mock_mode: bool` (AR-24, AD-23)
**And** `mock_mode` is `true` when `LLM_MODE=mock` or `OPENROUTER_API_KEY` is empty, `false` when `LLM_MODE=auto` and a key is set, and the app never fails at startup or on this route because a key is missing (pytest per combination) (AR-24, FR-15 not regressed)
**And** later stories and epics add their own fields to `ConfigOut` (consent in Story 1.4; limits, `chat_enabled`, `guide_steps` and feature flags when their slices exist), so no field is returned before its feature exists (AR-24)

**Given** the FastAPI app
**When** it is created
**Then** it uses `openapi_url="/api/openapi.json"` and `docs_url="/api/docs"`, and with `APP_ENV=demo`, `/api/docs` returns 404 while `/api/openapi.json` is still served (pytest) (AR-23, AD-3)
**And** every response model is a named Pydantic model, and a pytest test fails if any 2xx response schema in the OpenAPI document is untyped (`{}`, a bare `object`, or `additionalProperties: true`) (AR-23)
**And** the error envelope appears in the document as one `ErrorResponse` component (AR-23)

**Given** `uv run python -m app.export_openapi`
**When** it runs
**Then** it writes `frontend/openapi.json` deterministically (`[ASSUMPTION]` sorted keys, 2-space indent, trailing newline), and the file is committed (AR-23)
**And** the pytest `test_openapi_is_fresh` compares the live schema with the committed file and fails with the hint "run `uv run python -m app.export_openapi`" when they differ (AR-23)
**And** `npm run gen:api` (= `openapi-typescript openapi.json -o src/shared/api/schema.d.ts`) generates the types without a running backend, and `schema.d.ts` is committed (AR-23)

**Given** the frontend data layer in `src/shared/api/`
**When** a module calls the API
**Then** it goes through `client.ts`: same-origin `/api` paths, `credentials: "same-origin"`, `X-Requested-With: aicoach` on every non-GET/HEAD request, request and response types from `schema.d.ts`, and the error envelope parsed into a typed `ApiError {status, code, message}`. `[ASSUMPTION]` a non-JSON error body maps to code `unknown_error` (AR-22, AR-23, AR-28)
**And** query keys live in `queryKeys.ts`, and one `QueryClientProvider` is set up in `src/app/` (AR-28)
**And** Vitest tests check the header is sent on POST and DELETE but not on GET, and that the envelope is parsed (AR-32)

**Given** the placeholder home page from Story 1.1
**When** it loads with `LLM_MODE=mock`
**Then** it reads `/api/config` through the typed client and TanStack Query and shows "Mock mode". This is the end-to-end proof of the contract pipeline (AR-23, AR-24)

**Given** `backend/.importlinter`, run by a pytest test (`tests/test_architecture.py` calls `lint-imports` and asserts exit 0)
**When** the contracts are checked
**Then** `aicoach_engine` may not import `app`, `fastapi`, `starlette`, `sqlalchemy`, `httpx`, `pydantic_ai` or `openai` (AD-1); `app.core` may not import `app.modules` (Code Organisation rule 2); and a slice may import another slice only through its `service` module, never its `routes`, `repo`, `models` or `schemas` (AD-2, AR-14)
**And** the contracts name only packages that exist, and each later slice story adds its package to them (including the `coach` → `swings`, never-the-reverse layer once both exist) (AR-14)

**Given** the frontend ESLint config, run by `npm test` (`[ASSUMPTION]` `npm test` = `eslint . && vitest run`)
**When** the code is linted
**Then** `src/shared/**` may not import `@/modules/**` or `@/app/**`; `src/modules/<a>/**` may import `@/modules/<b>` only through its `index.ts` (never `@/modules/<b>/...`); no file reads `process.env.NEXT_PUBLIC_*`; no `route.ts`/`route.js` exists under `src/app/` and no file contains `"use server"` (AR-28, AD-2, AD-22, AR-4)
**And** hand-written domain types fail lint: `[ASSUMPTION mechanism]` a local ESLint rule flags any `type` or `interface` declaration outside `src/shared/api/` whose name matches a `components.schemas` key in `openapi.json` (AR-23)
**And** a Vitest test runs ESLint's Node API on small fixture snippets and asserts that each boundary rule fires (AR-32)

**Given** `app/core/logging.py`
**When** any request is served
**Then** one plain structured line (`key=value`) goes to stdout with method, path, status and duration_ms, and never request bodies, cookies or headers. A pytest `caplog` test asserts the line exists and contains no cookie value (AR-31)
**And** JSON field names are snake_case and timestamps are UTC ISO 8601 with `Z` (a shared serializer setting in `core`) (AR-29)

### Story 1.3: Make AIcoach look like itself: design tokens, self-hosted fonts, coach mark and buttons

As a player opening AIcoach on a phone at the range,
I want the app to render in its own paper, clay and teal palette and its three typefaces even without internet,
So that it reads like a calm lesson notebook on every device that reaches the laptop.

**Slice:** `frontend/src/app/globals.css` (`@theme`), `frontend/src/app/layout.tsx` (`next/font`), `frontend/src/shared/ui/` (button), `frontend/src/shared/layout/` (coach mark, wordmark), frontend Vitest
**Requirements:** UX-DR1, UX-DR2, UX-DR3, UX-DR6, UX-DR43, UX-DR49, UX-DR50, NFR-2, NFR-6, AR-28

**Acceptance Criteria:**

**Given** `src/app/globals.css`
**When** the Tailwind v4 `@theme` block is read
**Then** it defines every DESIGN.md frontmatter token with its exact value: colours (paper, paper-2, card, hairline, ink, ink-2, ink-on-dark, ink-on-dark-2, clay, on-clay, evidence-teal, evidence-tint, on-evidence, evidence-idle, ruler-track, confidence-high/medium/low, on-confidence, keyframe-ground, keyframe-floor, keyframe-floor-line, body-line, ghost-body, club, ball, scrim, shadow-hero), the typography scale display-hero … mono-meta (family, size, weight, line height, and italic where marked), radii bar … full, and spacing 1–8, gutter-mobile 20, panel-padding 32, card-padding 24, thread-width 640, rail-width 232, evidence-width 408 and section-gap-landing 120 (UX-DR1)
**And** a Vitest test parses the DESIGN.md frontmatter and fails if any colour, radius or spacing token is missing from `@theme` or has a different value (UX-DR1)
**And** the theme is light only: no dark tokens or `dark:` variants, `color-scheme: light`, and `body` on paper with ink text (UX-DR1)
**And** shadcn primitives are restyled only through these tokens: a Vitest source scan fails on any raw hex or `rgb(` colour in `src/**/*.tsx` and on shadcn's default palette classes (UX-DR1, AR-28)

**Given** `src/app/layout.tsx`
**When** fonts load
**Then** Newsreader (400, 500, 600, italic 400/500), Figtree (400–700) and IBM Plex Mono (400, 500, 600) come from `next/font/google`, self-hosted at build time, exposed as CSS variables used by the `@theme` font families, with fallbacks Georgia, Arial and Consolas (UX-DR2)
**And** a Vitest source scan finds no reference to `fonts.googleapis.com` or `fonts.gstatic.com` (UX-DR2)
**And** a phone on the laptop's Wi-Fi with mobile data off renders all three families (manual check in the completion notes) (UX-DR2, NFR-2)
**And** no typography token is below 12px, and a `measure-in-serif` utility sets IBM Plex Mono at 0.86em for measured values inside serif text (UX-DR2)
**And** `<html lang="en">` is set and all copy is English (NFR-6)

**Given** `src/shared/layout/CoachMark` and `Wordmark`
**When** they render
**Then** the mark is a clay circle with a paper flag on a short pin and a curved ground stroke, 28px by default and 26px inside the wordmark, and it is decorative (`aria-hidden`) next to messages (UX-DR6)
**And** the wordmark is "AI" in clay italic Newsreader followed by "coach" in ink, in a `rail` size (24px, `wordmark`) and a `signin` size (34px, `wordmark-large`), with the accessible name "AIcoach" (UX-DR6)

**Given** `src/shared/ui/button.tsx` (restyled shadcn Button)
**When** each variant renders
**Then** primary is clay on on-clay, `button` type, full radius, 52px high (56px below 768px); disabled primary is paper-2 with ink-2 text and the native `disabled` attribute; secondary is card with a 1.4px ink border at 52px; dark is ink with ink-on-dark text at 44px (UX-DR43)
**And** a Vitest test renders every variant and asserts its token classes and its disabled behaviour (UX-DR43)
**And** the rule "one clay primary per screen" is written as a usage comment on the component, and later page stories assert it per page (UX-DR43, UX-DR3)

**Given** the global styles
**When** any interactive element gets keyboard focus
**Then** a 2px evidence-teal outline at 2px offset shows on `:focus-visible` (UX-DR49)
**And** under `prefers-reduced-motion: reduce`, smooth scrolling and transitions are off (UX-DR49)

**Given** the colour and line rules
**When** a Vitest source scan runs over `src/`
**Then** it fails on any `shadow-*` utility other than `shadow-hero`, on gradient utilities, and on red fill classes, so depth stays tonal (paper / paper-2 / card + 1px hairline) (UX-DR3)
**And** the same scan fails on `autoPlay`/`autoplay`, on the words "Saved" or "Save" in JSX text or string literals, and on carousel packages, enforcing the banned patterns from here on (UX-DR50)

**Given** the placeholder home page
**When** it renders after this story
**Then** it shows the 34px wordmark on paper, and the Story 1.2 "Mock mode" line in `meta` ink-2, with no horizontal scroll at 390px wide (UX-DR1, UX-DR6)

### Story 1.4: Create an account with the library consent

As a visitor,
I want to create an account with my email and a password after ticking the one library consent,
So that I can start sending swings and know that every clip I send is kept in my swing library until I delete it.

**Slice:** `backend/app/modules/identity/` (`routes.py`, `service.py`, `repo.py`, `models.py`, `schemas.py`, `consent.py`), `backend/app/modules/system/` (config gains `consent`), `backend/app/core/` (`security.py`: bcrypt, JWT secret, session cookie; `db.py`), one Alembic migration, `backend/tests/`; `frontend/src/modules/identity/` (sign-up form), `frontend/src/shared/ui/` (input, checkbox, inline message), `frontend/src/app/signup/`, `frontend/src/app/(app)/swing/new/` (placeholder), `openapi.json` + `schema.d.ts`
**Requirements:** FR-1, AR-22, AR-24 (consent), AR-25, AR-29, AR-30, AR-31, UX-DR36, UX-DR46, UX-DR49, NFR-5, NFR-6

**Acceptance Criteria:**

**Given** this story's single Alembic revision
**When** `alembic upgrade head` runs (also at backend startup)
**Then** it creates `users` with `id` (UUID primary key, a UUIDv4 generated by the backend), `email` (text, not null, with a unique index on the stored trimmed and lowercased value), `password_hash` (text, not null), `consent_version` (text, not null), `consent_accepted_at` (timestamptz, not null, UTC) and `created_at` (timestamptz, not null, UTC) (AR-22, AR-29, AR-30)
**And** a pytest test asserts there is exactly one Alembic head, and a `pytest -m pg` test runs upgrade → downgrade → upgrade on Postgres 18 (AR-30)
**And** the SQLite test engine sets `PRAGMA foreign_keys=ON` on every connection (asserted in a test), and `app/core/db.py` exposes `JSON().with_variant(JSONB, "postgresql")` as the JSON column type for later tables (AR-30)

**Given** the consent defined once in `identity/consent.py` (`[ASSUMPTION]` a version string such as `"2026-11-25"` plus the text)
**When** `GET /api/config` is called signed out
**Then** it also returns `consent {version, text}`, read through `identity.service.current_consent()`, with the text exactly "I understand that every swing clip I send is stored in my swing library on the AIcoach server until I delete it." (AR-22, AR-24, UX-DR36)
**And** `openapi.json` and `schema.d.ts` are regenerated and `test_openapi_is_fresh` passes (AR-23)

**Given** a visitor posts `POST /api/auth/signup` with `X-Requested-With: aicoach` and `{email, password, consent: true, consent_version}` matching the current version
**When** the email is new
**Then** the response is `201` with `{email, analyses_count: 0, clips_count: 0}` and a session cookie, and the row stores the trimmed and lowercased email, a bcrypt hash (never the plain password; the hash starts with `$2b$`), the consent version and `consent_accepted_at` = now in UTC (FR-1, AR-22, AR-25)
**And** `" Rory@Example.COM "` is stored as `rory@example.com` (AR-22)

**Given** a sign-up request with a problem
**When** the server validates it
**Then** a password under 8 or over 72 UTF-8 bytes returns `422 password_invalid` before bcrypt runs (tests: a 72-byte multibyte password is accepted, a 73-byte one is refused, and bcrypt is not called) (AR-22)
**And** an email that is empty, lacks exactly one `@` with non-empty parts, or is over 254 characters returns `422 email_invalid` `[ASSUMPTION code and rule; no email-validator dependency]`
**And** `consent` missing or false returns `422 consent_required`, and a `consent_version` other than the current one returns `422 consent_outdated` `[ASSUMPTION codes]` (FR-1, AR-22)
**And** an email already in use, in any case or with any surrounding whitespace, returns `409 email_taken` `[ASSUMPTION code]` and leaves the existing row unchanged (FR-1)
**And** a missing `X-Requested-With` header returns `403 csrf_header_missing` (AR-22)
**And** in every case above no row is created and no cookie is set

**Given** two sign-ups with the same email at the same moment
**When** both reach the database
**Then** the insert is `INSERT … ON CONFLICT DO NOTHING RETURNING id`, so exactly one gets 201 and the other 409, with no `rollback()` on the shared session (`pytest -m pg`) (AR-30)

**Given** a successful sign-up
**When** the session cookie is issued
**Then** it holds an HS256 JWT with `sub` = user ID and `exp` = now + `ACCESS_TOKEN_EXPIRE_MINUTES` (43200), set `httpOnly`, `SameSite=Lax`, `Path=/` and `Max-Age=2592000`. `[ASSUMPTION]` the cookie is named `aicoach_session` (AR-22)
**And** `Secure` is set only when the request arrived over HTTPS (request scheme or `X-Forwarded-Proto: https`), so it is absent over the LAN's plain HTTP (AR-22)

**Given** `JWT_SECRET` is empty
**When** the backend starts for the first time
**Then** it generates a cryptographically random secret (≥32 bytes) and persists it in `DATA_DIR/system/` (`[ASSUMPTION]` file `jwt_secret`), and later restarts reuse it, so a cookie issued before a restart still verifies (pytest) (AR-22, AD-4)
**And** a `JWT_SECRET` set to a known default (`[ASSUMPTION]` deny-list: `changeme`, `change-me`, `secret`, `jwt-secret`) stops startup with a log line naming the variable, never its value (AR-22)
**And** the secret never appears in logs (AR-31)

**Given** sign-up attempts, successful or failed
**When** they are logged
**Then** the lines carry the outcome code and the user ID where one exists, never the email or password (pytest `caplog` asserts neither string appears) (AR-31)

**Given** a visitor opens `/signup` (public)
**When** the page renders from `src/modules/identity/`
**Then** it shows "Create your account", "Email, password and one consent.", an "Email" and a "Password" text input (label above, card fill, hairline border, 50px), and the consent checkbox between the password field and the "Create account" button (UX-DR36)
**And** the checkbox is native, 22px, unticked by default with a hit area of at least 44×44px, and its label is the full consent text from `/api/config`, never hard-coded. Clicking the label or pressing Space toggles it (UX-DR36, UX-DR49)
**And** while the box is unticked, "Create account" is the disabled primary (paper-2) with `aria-describedby` pointing to the meta line "Tick the box to create your account.". Ticking makes it the clay primary, and unticking disables it again (UX-DR36, FR-1)
**And** the page states what is stored and that it can be deleted. `[ASSUMPTION copy]` "AIcoach stores your swing clips, results, key frames and coach chats." is followed by "You can delete your account and every swing from the Account page at any time." (FR-1)
**And** the meta line "AIcoach reads right-handed swings for now." sits under the form, followed by "Have an account? Sign in" linking to `/signin` (UX-DR36)

**Given** the sign-up form
**When** the visitor types
**Then** no error shows. On submit, errors appear under the field concerned as the shared inline message (one line of ink text with a small confidence-low ×, never a modal or banner), and an error clears when that input changes (UX-DR36, UX-DR46)
**And** client checks mirror the server: email shape, and password length of 8–72 UTF-8 bytes measured with `TextEncoder`. `[ASSUMPTION copy]` "Enter a valid email address." / "Use a password of 8 to 72 characters." The server's `email_invalid` and `password_invalid` map to the same lines (UX-DR46)
**And** `409 email_taken` shows "An account with this email already exists. Sign in instead?" under the email field, where "Sign in instead?" links to `/signin`, and the email, password and ticked box keep their values (FR-1, UX-DR36)
**And** `422 consent_outdated` refetches `/api/config`, shows the new text, unticks the box and shows `[ASSUMPTION copy]` "The consent text has changed. Read it and tick the box again." (AR-22)
**And** a network failure shows "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." `[ASSUMPTION reuse of the UX-DR45 line]`, and the button is disabled while a request is in flight (UX-DR46)

**Given** a successful sign-up
**When** the response arrives
**Then** the browser goes to `/swing/new`, signed in. In this epic that route is a placeholder in `src/app/(app)/swing/new/` with the title "New swing" and one shared dashed placeholder box labelled "Drop zone" `[ASSUMPTION]`, which Epic 3's upload module replaces (UX-DR36)

**Given** the shared primitives `Input`, `Checkbox` and `InlineMessage` in `src/shared/ui/`
**When** their Vitest tests run
**Then** they cover: Space toggles the checkbox; the disabled button and its `aria-describedby`; no error while typing, an error on submit, and the error cleared on change; and the inline message's × mark (or medium-coloured `!` for the warning variant) (UX-DR46, UX-DR49)
**And** at 390px wide the page has no horizontal scroll, the primary button is 56px high, tab order is email → password → checkbox → "Create account" → links, and there is exactly one clay primary on the page (NFR-5, UX-DR49, UX-DR43)

### Story 1.5: Sign in and reach my protected pages

As a player,
I want to sign in with my email and password and be sent back to the page I asked for,
So that my swings stay behind my account and other people's data never shows.

**Slice:** `backend/app/core/auth.py` (`current_user`), `backend/app/modules/identity/` (signin, `GET /api/me`), `backend/tests/` (`conftest.py` player fixtures, deny-by-default test); `frontend/src/modules/identity/` (sign-in form), `frontend/src/app/signin/`, `frontend/src/app/(app)/layout.tsx` (protected group), `frontend/src/app/not-found.tsx`, `frontend/src/shared/layout/` (not-found view), `frontend/src/shared/ui/` (placeholder), `frontend/src/shared/api/` (401 handling)
**Requirements:** FR-1, FR-2 (pattern), AR-18, AR-22, AR-25, AR-28, AR-31, UX-DR36, UX-DR45, UX-DR46, UX-DR49, NFR-5

**Acceptance Criteria:**

**Given** an account created in Story 1.4
**When** `POST /api/auth/signin` is called with `X-Requested-With: aicoach` and `{email, password}`
**Then** the email is trimmed and lowercased before lookup. Correct credentials return `200 {email, analyses_count, clips_count}` with the session cookie as specified in Story 1.4 (FR-1, AR-22)
**And** an unknown email or a wrong password both return `401 invalid_credentials` `[ASSUMPTION code]` with the same message and no cookie (FR-1)
**And** a password over 72 UTF-8 bytes returns `422 password_invalid` before bcrypt runs, and a missing CSRF header returns `403 csrf_header_missing` (AR-22)
**And** failed sign-ins are logged without the email or password (AR-31)

**Given** the `current_user` dependency in `app/core/auth.py`
**When** a protected `/api` route is called
**Then** a missing, malformed or expired token returns `401 not_authenticated` `[ASSUMPTION code]` (AR-18)
**And** a valid token whose `users` row no longer exists returns `401 session_invalid` with a `Set-Cookie` that clears the session cookie (AR-18)
**And** the `users` row is loaded on every request, never cached (AR-18)

**Given** `GET /api/me`
**When** a signed-in player calls it
**Then** it returns `{email, analyses_count, clips_count}` for that player only. Both counts are 0 in this epic, and Epic 3 wires them to `swings.service` counts (AR-25)

**Given** the deny-by-default rule
**When** a pytest test walks `app.routes`
**Then** every `/api` route depends on `current_user` except `POST /api/auth/signup`, `POST /api/auth/signin`, `GET /api/config`, `GET /api/health` and FastAPI's own `/api/openapi.json` and `/api/docs`, and the test fails when a new route forgets it (AR-18, FR-2)
**And** a parametrised test calls every protected route without a cookie and expects `401` (AR-18)

**Given** the FR-2 pattern for later slices
**When** a test needs two players
**Then** `tests/conftest.py` provides a `player_client` fixture factory that signs up through the API (with consent) and returns a signed-in client, so later slices can write isolation tests with two players (FR-2, AR-32)
**And** `app/core/errors.py` provides `not_found()` (`404 not_found`), and identity's repo functions take the owner key as a required argument, the pattern later repos follow with `user_id` (AR-18)
**And** a signed-in request to an unknown `/api` path returns the `404 not_found` envelope (FR-2)

**Given** a visitor opens `/signin` (public)
**When** the page renders from `src/modules/identity/`
**Then** it shows the 34px wordmark, "Welcome back", "Sign in to see your swings.", "Email" and "Password" inputs, the primary "Sign in" and a "Create an account" link to `/signup` (UX-DR36)
**And** errors show on submit, not while typing. Wrong credentials, and `422 password_invalid` on sign-in, show "That email and password don't match." under the form as an inline message, and the email is kept (UX-DR36, UX-DR46)

**Given** a signed-out visitor opens a protected URL such as `/account?x=1` or `/swing/new`
**When** the `(app)` route-group layout queries `/api/me` and gets 401
**Then** the browser goes to `/signin?next=%2Faccount%3Fx%3D1`, and after a successful sign-in it lands back on `/account?x=1` (UX-DR45, AR-28)
**And** `next` is honoured only when it is a same-origin path (starts with `/`, not `//`), and otherwise the target is `/swing/new` (Vitest) `[ASSUMPTION]`
**And** without `next`, sign-in lands on `/swing/new` (UX-DR36)
**And** any API call that returns 401 later in the session (fetch client) clears the query cache and redirects the same way (AR-28)

**Given** a protected page is loading
**When** data is not there yet
**Then** dashed placeholders (shared `Placeholder`: paper fill, 1.4px dashed hairline border, dash 5 4) stand in for the content in the final layout, and no spinner appears anywhere (UX-DR45)
**And** a load failure other than 401 shows "Couldn't load this. Try again." inline with a secondary "Try again" that refetches (UX-DR45, UX-DR46)

**Given** a signed-in player opens `/signin` or `/signup`
**When** the page checks `/api/me`
**Then** they are redirected to `/swing/new` `[ASSUMPTION]`

**Given** any URL that does not exist, or a later slice whose API returns `404 not_found`
**When** it renders
**Then** `src/app/not-found.tsx` shows the shared not-found view from `src/shared/layout/`: "This analysis doesn't exist or isn't yours." with a link to the player's swings (`[ASSUMPTION]` "Go to your swings" → `/library`, which Epic 5 builds), the HTTP status is 404, and no data from the request is shown (FR-2, UX-DR45)
**And** a helper exported from `src/shared/layout/` lets later slices render this view when the API returns `404 not_found` (FR-2)

**Given** the sign-in and protected pages
**When** they are used on a 390px phone and with the keyboard
**Then** there is no horizontal scroll, touch targets are at least 44×44px, tab order follows reading order and the focus ring shows (NFR-5, UX-DR49)
**And** Vitest covers the `next` sanitiser, the 401 redirect builder and the sign-in error mapping (AR-32)

### Story 1.6: Find my way around: the signed-in app shell, my account page and sign out

As a player on a laptop or a phone,
I want a rail (or ≡ menu) with "New swing", my pages and a mock-mode note, plus an Account page where I can see my email and sign out,
So that I can move around AIcoach and leave it safely on any screen size.

**Slice:** `frontend/src/shared/layout/` (app shell, rail, top bar, menu sheet, page header, slots), `frontend/src/shared/ui/` (sheet), `frontend/src/modules/account/`, `frontend/src/app/(app)/layout.tsx` (composition root), `frontend/src/app/(app)/account/`; `backend/app/modules/identity/` (`POST /api/auth/signout`)
**Requirements:** FR-1 (sign out), AR-25, AR-28, UX-DR4, UX-DR5, UX-DR6, UX-DR40 (email, sign out), UX-DR42, UX-DR45 (mock label, cold load), UX-DR49, UX-DR50, NFR-5, NFR-6

**Acceptance Criteria:**

**Given** a signed-in page at 1344px or wider
**When** the shell renders
**Then** it has three columns: the left rail (232px, paper-2), the thread column (640px content starting 64px from the rail) and a third-column slot for the Evidence panel (408px), which renders nothing until a later slice fills it (UX-DR4)
**And** from 1024px to 1343px the rail and thread show with no third column; from 768px to 1023px the rail collapses into the ≡ menu sheet and the thread is full width (max 640px); below 768px the phone layout shows a top bar (≡ or back chevron · `page-title-mobile` title with meta under it · a right slot for the Evidence chip), one column with a 20px gutter, and actions in the bottom third (UX-DR4)

**Given** the rail (`<nav aria-label="Main">`)
**When** it renders
**Then** it shows the 24px wordmark, the dark "New swing" button (44px) linking to `/swing/new`, a recent-swings slot, then "Swing library" (`/library`), "Filming guide" (`/guide`) and "Account" (`/account`), with the current page marked `aria-current="page"` (UX-DR5, UX-DR6)
**And** the wordmark links to `/swing/new` until Epic 5 supplies the latest thread `[ASSUMPTION]` (UX-DR5)
**And** with no recent swings (always true in this epic) there is no "Swings" heading, and "New swing" is the only action (UX-DR5)
**And** when `/api/config` has `mock_mode: true`, the rail footer shows "Mock mode" in `meta` ink-2, not interactive and with no badge or colour, on every signed-in page; with `mock_mode: false` it is absent (UX-DR45)
**And** links to routes that later epics build (`/library`, `/guide`) render now and show the Story 1.5 not-found view until those slices exist `[ASSUMPTION]`

**Given** a phone or a 768–1023px window
**When** the player taps ≡ in the top bar
**Then** the menu opens as a sheet with the same content as the rail (wordmark, "New swing", the recent-swings slot, the three links and the mock-mode footer), and `aria-expanded` is set on the ≡ button (UX-DR5)
**And** a page that declares a back target shows a back chevron instead of ≡ (Vitest for both modes) (UX-DR5)

**Given** the shared `Sheet` primitive in `src/shared/ui/`, used here by the menu and in Story 1.8 by the delete confirmation
**When** it opens
**Then** the bottom variant is a card with 18px top corners over the `scrim` token, a 40×5px hairline handle, a `panel-title` title, ink-2 consequences and full-width stacked actions (UX-DR42)
**And** focus moves into the sheet, is trapped there, and returns to the control that opened it on close. Esc, a swipe down or a scrim tap closes it, except while its `busy` flag is set (UX-DR42, UX-DR49)
**And** only one sheet can be open at a time: opening one closes any other, so sheets never stack (UX-DR42, UX-DR50)
**And** Vitest covers focus in, focus return, Esc, scrim tap, `busy` blocking close, and no stacking (AR-32)

**Given** the composition rules
**When** the `(app)` layout composes the shell
**Then** `src/app/(app)/layout.tsx` is the only place that passes slice content into the shell's slots (rail recent swings, top-bar right, third column, page header action), and `src/shared/layout/` imports no module (the Story 1.2 lint passes) (AR-28, Code Organisation rule 2)
**And** `src/shared/layout/PageHeader` provides a title, a meta line and one action or status slot above a hairline (UX-DR4)
**And** the Story 1.4 `/swing/new` placeholder now renders inside the shell (UX-DR5)

**Given** a signed-in player opens `/account`
**When** the page renders from `src/modules/account/`
**Then** it shows the title "Account", the player's email from `/api/me`, and a secondary "Sign out" button `[ASSUMPTION variant]`. Epic 5 adds the "Your analyses" list later (UX-DR40)
**And** while `/api/me` loads, dashed placeholders hold the final layout, and a failure shows "Couldn't load this. Try again." (UX-DR45)

**Given** a signed-in player activates "Sign out"
**When** `POST /api/auth/signout` (auth required, CSRF header) returns `204` with a `Set-Cookie` that clears the session cookie
**Then** the frontend clears the query cache and goes to `/` `[ASSUMPTION target]`, and opening `/account` afterwards redirects to `/signin?next=%2Faccount` (FR-1, AR-25)
**And** if the session was already invalid (`401 session_invalid`, cookie cleared by the server), the frontend still ends signed out on `/` (AR-18)

**Given** the shell and the account page
**When** they are checked at 1440px and at 390px, and with browser text at 200%
**Then** there is no horizontal scroll at 390px, every touch target is at least 44×44px, tab order follows reading order (rail before content), the focus ring shows on every control, and no content is lost at 200% text (manual check in the completion notes) (UX-DR49, NFR-5)
**And** the shell has no hover-only affordance and no swipe-only action: every sheet also has a keyboard and tap way to close (UX-DR50)

### Story 1.7: Land on a page that explains AIcoach honestly before I sign up

As a visitor (a golfer between +2 and 15 handicap),
I want a landing page that shows what the coach says, how sure it is and when it refuses to guess,
So that I can decide to create an account knowing it is a practice tool that keeps my clips private.

**Slice:** `frontend/src/modules/landing/` (sections and static illustrations), `frontend/src/shared/layout/` (landing header with slots), `frontend/src/app/page.tsx`
**Requirements:** FR-1, UX-DR3, UX-DR5 (landing header), UX-DR44, UX-DR45, UX-DR49, UX-DR50, NFR-5, NFR-6

**Acceptance Criteria:**

**Given** a signed-out visitor opens `/`
**When** the page renders
**Then** the shared landing header (from `src/shared/layout/`, with slots so Epic 3's public filming guide can reuse it) shows the wordmark and "How it works" · "When it says no" (in-page anchors to the film → send → read row and the honesty cards) · "Sign in" (`/signin`) · "Create account" (`/signup`) (UX-DR5)
**And** the Story 1.1 placeholder is gone (UX-DR44)

**Given** the hero
**When** it renders at 1440px
**Then** it has an 80px outer margin, the `display-hero` (62px Newsreader) headline "Send one swing. Hear what a coach would tell you.", the `body-lg` text "Film one swing down the line. The coach names the fault, says how sure it is, and gives you one drill. Then you can ask it why.", a primary "Create account" (`/signup`), a secondary "Read the filming guide" (`/guide`, built in Epic 3) and the meta line "For golfers between +2 and 15 handicap. A practice tool, not for competitive rounds." (UX-DR44)
**And** to the right sits a non-interactive example-result card (720px) labelled "Example result", the only element on the site with the `shadow-hero` shadow. Its copy follows `mockups/01-landing.svg`: the coach line, "7% of body height" in mono teal at 0.86× with the pin `[3]`, the feel cue, the Evidence column with Address and Impact frames, and "confidence: high" as word + colour + bars. Its pretend composer and pins are not focusable and not announced as controls (UX-DR44, UX-DR3, UX-DR2)

**Given** the sections below the hero
**When** the page scrolls
**Then** in order, 120px apart on alternating paper and card bands, it shows: the legend "The coach talks. The evidence stays pinned." (coach / measured, pinned / "Dashed means inferred, not measured."); the film → send → read row headed "One swing fits inside a range session."; three fault tiles (Early extension, Loss of posture, Over the top with "Capped at medium confidence"), each with a static key-frame skeleton illustration, name, mono measurement and clay drill name; three honesty cards headed "When it can't tell, it says so." (Cannot analyse, No verified fault found with an "Unverified — confirm with a coach" card, a grounded refusal); and the ink closing band "Your coach is waiting for one swing." with a clay "Create account" CTA and the privacy line "Your clips are private. Each one stays in your swing library until you delete it." in ink-on-dark-2, with all copy as in `mockups/01-landing.svg` (UX-DR44)
**And** illustrations are static SVGs in `src/modules/landing/` drawn with the key-frame tokens (skeleton, no photos, no graph paper). Each has a text label, and purely decorative parts are `aria-hidden` (UX-DR44, UX-DR3)
**And** `[ASSUMPTION]` this example copy is static marketing illustration owned by the landing module. It is not coaching output, so the "coaching copy from `rules.yaml`" rule does not apply to it (AR-28)

**Given** the colour and line rules
**When** the landing is reviewed
**Then** teal appears only on measured values, pins and the ruler, clay only on the coach mark, the coach name, drill names and the CTAs, dashed lines only on inferred or unverified items, and there are no gradients, carousels, autoplaying media, score dials or badges (Story 1.3 scans pass) (UX-DR3, UX-DR50)

**Given** a 390px phone
**When** the landing renders
**Then** it follows the phone rules: one column with a 20px gutter, the example card stacked under the hero text, full-width 56px CTAs and no horizontal scroll. `[ASSUMPTION]` section gaps shrink on the phone, since the phone landing is not mocked (UX-DR44, NFR-5)
**And** text at 200% loses no content, tab order follows reading order, and the focus ring shows on header links and CTAs (UX-DR49)

**Given** a signed-in player opens `/`
**When** the page checks `/api/me`
**Then** they are redirected to `/swing/new` `[ASSUMPTION]`, and a signed-out visitor sees the landing without any flash of signed-in content (UX-DR45)

### Story 1.8: Delete my account

As a player who decides to stop,
I want to delete my account after seeing plainly what will be removed,
So that nothing of mine stays on the AIcoach server and my old sign-in stops working.

**Slice:** `backend/app/modules/identity/` (`DELETE /api/me`, `service.delete_account`, `service.lock_user`), `backend/tests/`; `frontend/src/modules/account/` (delete action and confirm sheet), `frontend/src/shared/ui/` (sheet from Story 1.6)
**Requirements:** FR-3 (account delete), AR-14, AR-25, AR-31, UX-DR40, UX-DR41 (account variant), UX-DR42, UX-DR43, UX-DR46, UX-DR49, AD-2, AD-8

**Acceptance Criteria:**

**Given** a signed-in player
**When** they call `DELETE /api/me` with `X-Requested-With: aicoach`
**Then** `identity.service.delete_account(session, user_id)` deletes their `users` row and commits, and the response is `204` with a `Set-Cookie` that clears the session cookie (FR-3, AR-25, AD-8)
**And** the service is built as "commit, then post-commit steps". It has none yet, because no player files exist in this epic, and Epic 3's upload story adds the `swings.service.purge_user_files(user_id)` call there. Child tables join the cascade in their own migrations (AR-14, cross-epic hand-off)
**And** account deletion is always allowed and has no in-progress guard (AD-8)
**And** a missing CSRF header returns `403 csrf_header_missing` and nothing is deleted; with no session it returns `401` (AR-22, AR-18)
**And** the log line carries the user ID, never the email (AR-31)

**Given** a deleted account
**When** its old cookie is used, or the old email and password are tried
**Then** the old cookie gets `401 session_invalid` and is cleared, and sign-in gets `401 invalid_credentials` (FR-3)
**And** the same email can create a new account afterwards, with a fresh consent `[ASSUMPTION]`

**Given** `identity.service.lock_user(session, user_id)`, the only per-user lock (AD-2)
**When** two transactions call it for the same user
**Then** it takes `SELECT … FROM users WHERE id = :user_id FOR UPDATE`, and a `pytest -m pg` test shows the second caller waits until the first commits. It is exported from `identity/service.py` for Epic 3's upload (AR-14)

**Given** a signed-in player on `/account`
**When** they activate the secondary "Delete account" (with the meta line "Removes every analysis, result, key frame and swing clip.")
**Then** the Story 1.6 bottom sheet opens with the title "Delete your account?", the consequences "This removes n analyses with their results and key frames, and n swing clips. It cannot be undone, and you will not be able to sign in again.", with both counts from `GET /api/me` (0 and 0 in this epic), a dark "Delete everything" and a secondary "Keep my account" (UX-DR41, UX-DR40, UX-DR43)
**And** `[ASSUMPTION]` singular forms are used for a count of 1 ("1 analysis", "1 swing clip")
**And** "Keep my account", Esc, a swipe down or a scrim tap closes the sheet, and focus returns to "Delete account" (UX-DR42, UX-DR49)

**Given** the player taps "Delete everything"
**When** the request is in flight
**Then** both actions are disabled and the sheet cannot be dismissed (`busy`) (UX-DR42)
**And** on `204` the query cache is cleared and the player lands signed out on the landing page `/` (UX-DR41)
**And** on a network error or a 5xx the sheet stays open with the inline message "Couldn't delete. Nothing was removed. Try again.", the actions are enabled again, and the account still exists (UX-DR41, UX-DR46)

**Given** the account page with the sheet
**When** it is used on a 390px phone and with the keyboard
**Then** the sheet's actions are full width with targets of at least 44px, tab order is title → consequences → "Delete everything" → "Keep my account", and the focus ring shows on each (UX-DR49, NFR-5)
**And** Vitest covers the sheet copy with counts 0 and 1, the busy state, the failure message and the redirect, and pytest covers the API cases above (AR-32)


## Epic 2: The analysis engine gives an honest verdict from the command line

The author (and the examiner) can run `aicoach-engine analyse <clip>` and get a complete `AnalysisResult`: swing events, measurements with confidence bands, verified / possible / absent faults with fault chains, drill and mobility exercise, at most one unverified observation, or a rejection with reasons. The engine is a pure package (AD-1). It runs with no database, web app, network or language model, and it leaves `explanation` empty for the app to fill. The epic starts with the week-1 spike. It also covers filming and labelling the test set, the eval and bench harness, and the 2026-12-01 over-the-top vs sway checkpoint on the tuning set.

### Story 2.1: Run the week-1 spike and record the pose backend decision

As the author,
I want a timeboxed spike that times and compares the pose backends on my own clips and checks the capture and runtime assumptions,
So that `POSE_BACKEND`, the model manifest and the video assumptions are settled before the pose and upload stories build on them.

**Slice:** `eval/spike/` (throwaway timing script and notes), `backend/models/MANIFEST.yaml`, `.env.example` (`POSE_BACKEND` line only), architecture `.memlog.md` (and `ARCHITECTURE-SPINE.md` AD-15 only if the slow-motion check fails)
**Requirements:** AR-2, NFR-7, FR-6 (speed basis for NFR-1), AD-13, AD-15

**Acceptance Criteria:**

**Given** 3–5 DTL clips filmed at 120 or 240 fps, at hand height, about 3 m behind the hands line (setup-guide §8.1)
**When** the spike script times MediaPipe Pose Full and Heavy (mediapipe 1.2.3, Tasks `PoseLandmarker`) and RTMPose-m (rtmlib 0.0.16 + onnxruntime 1.32) on the target laptop, on the trimmed ~2 s swing window only (addendum §A)
**Then** the notes record ms per frame and seconds per clip for each model, and the projected engine time for a 10 s and a 15 s clip against NFR-1 (under 2 and 3 minutes) (AR-2)
**And** they record how stable the hip, shoulder and wrist landmarks are at address, top and impact for each model, as visibility at those frames and jitter over a still address window `[ASSUMPTION: jitter = standard deviation of frame-to-frame displacement in px]`

**Given** an iPhone slow-motion clip exported through the phone's file picker
**When** `ffprobe` reads the stream's `avg_frame_rate` and the container duration
**Then** the notes record both values and whether they match the capture fps and the real-time length (AR-2, AD-15 `[ASSUMPTION]`)
**And** if the clip reads as a slowed 30 fps file or runs longer than 15 s, AD-15 in `ARCHITECTURE-SPINE.md` is amended with the chosen fix and logged in the memlog before any Epic 3 upload story starts

**Given** the chosen backend
**When** it is installed in a plain `python:3.14-slim` linux/amd64 container with `apt-get install ffmpeg libegl1 libgles2`
**Then** one pose inference on a sample frame succeeds inside that container (AR-2, AR-3)
**And** the notes record whether its wheels exist for linux/arm64; if they don't, the memlog records either "README states amd64 only" or a switch of the default to rtmlib (spine Deferred)

**Given** the chosen backend's model files
**When** `backend/models/MANIFEST.yaml` is filled in
**Then** each entry has URL, SHA-256 and licence, every licence permits later commercial use, and no YOLO-pose (AGPL) or non-commercial model is listed (NFR-7, AD-13)

**Given** the one-working-day timebox
**When** the spike ends
**Then** the architecture memlog has a dated decision entry with the measured numbers and the chosen `POSE_BACKEND` (`mediapipe` or `rtmpose`), and `.env.example` sets `POSE_BACKEND` to that value (AR-2, AR-4)
**And** `[ASSUMPTION]` if there is no clear winner when the timebox runs out, the faster backend that meets NFR-1 is chosen and the open point is logged

### Story 2.2: Define the rule table in rules.yaml with one loader

As the author,
I want every threshold, fault mapping and piece of coaching copy in one validated `config/rules.yaml`,
So that I can tune and swap faults by editing configuration, never code, and a broken file stops the engine instead of producing wrong verdicts.

**Slice:** `config/rules.yaml`, `backend/engine/aicoach_engine/rules.py`, `backend/tests/engine/`
**Requirements:** AR-7, FR-9 (configurable thresholds, sway reserve), FR-11 (mapping), FR-13 (closed list), FR-8 (reason → guide step), NFR-6

**Acceptance Criteria:**

**Given** `config/rules.yaml`
**When** `aicoach_engine.load_rules(path) -> RuleTable` parses it
**Then** the file has exactly the sections `faults`, `observations`, `confidence`, `coach`, `guide_steps` and `reasons`, and every Pydantic model sets `extra="forbid"`, so an unknown or misspelt key at any depth raises `RulesError` naming the file and the key path (AR-7, AD-11)
**And** a pytest asserts that no other module in `aicoach_engine` opens or YAML-parses the rules file

**Given** the `faults` section
**When** it is loaded
**Then** it holds, in this order, `early_extension`, `loss_of_posture` and `over_the_top` with `status: active`, and `sway` with `status: reserve`. `status` accepts only `active | possible_only | reserve` (FR-9, AD-11)
**And** each fault has `label`, `measurement {key, label}`, `thresholds {potential, fault}`, `direction` (`above` | `below`), `key_frames` (swing events), chain labels `cause` and `mechanism`, `feel_cue`, `drill` and `mobility`. `drill` and `mobility` each have `name`, `dose` and two or three lines of `instructions`, per the PRD §4.4 table: Wall drill (3 × 10) · 90/90 hip rotation (2 × 8); Alignment-stick head drill · Hip-hinge / hamstring mobility; Pump drill · Open books; Alignment stick at the trail hip ("turn without bumping it") · Trail-hip internal rotation (FR-11)
**And** the early-extension feel cue is "It may feel like you stay down, but at impact your hips have moved toward the ball." `[ASSUMPTION: the author writes the other three feel cues and the drill instructions]`

**Given** the starting thresholds
**When** they are read
**Then** they come from addendum §B, with a comment in the file naming that source: loss of posture potential 5°, fault 10° (above); early extension 3 in / 6 in; over the top fault 3 in; sway potential 0°, fault −3° (below) (FR-9)
**And** `[ASSUMPTION]` inches are converted to `body_height_ratio` as `in × 2.54 / 175` (175 cm reference height), which gives early extension 0.044 / 0.087 and over the top fault 0.044. Over the top has no potential value in the source, so its potential starts at half the fault value (0.022). All of these are tuned only on the tuning set (OQ3)

**Given** the `observations` section
**When** it is loaded
**Then** it lists the extra measurements, initially only sway's measurement, with its own `threshold` (`[ASSUMPTION]` −3°), `direction` and `template` "Your hips appear to move away from the target in the backswing." (FR-13)
**And** an observation whose measurement key belongs to a fault with status `active` or `possible_only` raises `RulesError` (AD-11)
**And** a pytest edits a copy of the file to swap the statuses (`over_the_top: reserve`, `sway: active`): with sway still under `observations` the load is refused, and with sway removed it loads. This proves the swap is a configuration edit with no code change (FR-9)

**Given** the `confidence` section
**When** it is loaded
**Then** it holds the fps floors `reject_below: 30` and `high_min: 120`, the cap `over_the_top: medium`, and `[ASSUMPTION]` the high/medium cut-offs for the three band components (visibility, margin, event clarity), so they can be re-tuned per pose backend without code changes (AR-7, AR-8, AD-13)

**Given** the `coach` section
**When** it is loaded
**Then** it holds:
- word limits: explanation 150, chat 80
- a jargon blocklist containing at least "kinematic sequence", "pelvic thrust" and "degrees of spine tilt"
- the medical notice "Generic guidance, not medical advice — see a physiotherapist if you feel pain."
- refusal texts for `not_measured`, `other_swings`, `pain`, `competition` and `off_topic`, plus the outside-rule-table line "I have no drill I can stand behind. A coach can check it in person." (EXPERIENCE.md → AI Coach Chat)
- template explanations for a verified-fault result and for a no-fault result
- mock answers for the suggested prompts "How do I know the drill is working?", "What does 'likely cause' mean?", "Can I do this drill in a net?" and "What did you check in my swing?"
- the copy "No verified fault found", "Cannot analyse", "Unverified — confirm with a coach", "No drill: this is not in my rule table." and the no-observation line "None of my three rules fired, and nothing else stood out that I can measure. That's a real answer."
- the band phrases "and I'm sure of it" / "I'm fairly sure" / "but I can't be sure from this clip"
- the fps warning "Filmed at {fps} fps — nothing can be rated 'high'."

(AR-7, NFR-6)
**And** a pytest asserts that every one of these texts is present and non-empty, and that each template uses only the placeholders the schema allows. Running them through the grounding check is Epic 4's test (AR-27); this story does not depend on it

**Given** the `guide_steps` and `reasons` sections
**When** they are loaded
**Then** `guide_steps` is the ordered list `view`, `position`, `distance`, `frame-rate`, `framing`, `one-swing-light`. `[ASSUMPTION]` The slug names are mine; the order matches the six UX guide steps and Epic 3's step assignments
**And** `reasons` maps each code to `{guide_step, label, detail}` `[ASSUMPTION: detail = the one-line explanation on the UX-DR34 reason row]`:

| Code | Guide step | Label · detail |
|---|---|---|
| `not_dtl` | `view` | "Face-on view detected" · "I read only down the line, from behind." |
| `body_out_of_frame` | `framing` | — |
| `club_out_of_frame` | `framing` | — |
| `fps_below_30` | `frame-rate` | "Filmed at {fps} fps" · "Impact blurs between frames." |
| `undecodable` | `frame-rate` `[ASSUMPTION]` | — |
| `no_swing` | `one-swing-light` | — |
| `multiple_swings` | `one-swing-light` | — |
| `too_dark_or_blurred` | `one-swing-light` | — |
| `low_visibility` (film-better hint) | `framing` | — |
| `unclear_events` (film-better hint) | `frame-rate` | — |
| `low_fps` (film-better hint) | `frame-rate` | — |

(FR-8, AD-11)
**And** a `guide_step` that is not in `guide_steps` raises `RulesError`

**Given** any byte of the file is changed
**When** it is reloaded
**Then** `RuleTable.rules_hash` (SHA-256 of the file bytes) changes, so every result can record which table decided it (AR-11)

### Story 2.3: Film and label the tuning and evaluation sets

As the author,
I want separate, labelled tuning and evaluation sets of my own swings,
So that thresholds are tuned on one set only, and SM-1 to SM-6 and the event tolerances are measured honestly on the other.

**Slice:** `eval/labels.yaml`, `backend/tests/engine/test_labels.py`, `EVAL_DATA_DIR` (outside Git)
**Requirements:** AR-34, AR-33, NFR-3, NFR-8, FR-6 (event labels)

**Acceptance Criteria:**

**Given** the filming rules (FR-4)
**When** the author films the clips
**Then** every clip is DTL at 120 or 240 fps, with the phone at hand height, on the hands line, 2.4–3.7 m away, one swing per clip, and shows only the author (AR-34, NFR-8)
**And** the clip files live in `EVAL_DATA_DIR` outside the repository, and `git ls-files "*.mp4" "*.mov"` lists none of them (NFR-8, AD-24)

**Given** `eval/labels.yaml`
**When** a clip is labelled
**Then** its entry is `{clip_file, split: tuning|evaluation, faults: [...], events: {address, top, impact}}`. Each event is a 0-based `frame_index` into the full decoded stream at the clip's own fps (AD-14), read frame by frame `[ASSUMPTION: from ffmpeg frame-numbered extraction]`. Address is the last still frame before takeaway (FR-6) (AR-33)
**And** `faults` uses the rule-table keys for rule-table faults, `[]` for a clean swing, and `[ASSUMPTION]` a free key such as `reverse_pivot` for a fault outside the rule table
**And** `[ASSUMPTION: extends the AR-33 schema for SM-6]` a clip that should be rejected carries `expect: rejection` and may leave out `events`

**Given** the evaluation split
**When** it is counted
**Then** it has at least 4 clips per verified fault (`early_extension`, `loss_of_posture`, `over_the_top`), at least 3 clean clips, at least 3 clips whose main fault is outside the three, and at least 1 face-on and 1 out-of-frame clip (SM-1, SM-2, SM-3, SM-6, AR-34)
**And** `[ASSUMPTION]` it also has at least 4 sway clips, in case the 2026-12-01 swap happens

**Given** the tuning split
**When** it is counted
**Then** none of its clips appear in the evaluation split, and `[ASSUMPTION]` it has at least 4 clips per fault including sway, plus at least 2 clean clips
**And** `[ASSUMPTION]` it is filmed and labelled by 2026-11-28, so the 2026-12-01 checkpoint can run on it

**Given** `eval/labels.yaml` is committed
**When** `pytest backend/tests/engine/test_labels.py` runs
**Then** it validates:
- the schema
- unique `clip_file` values and disjoint splits
- the minimum counts above
- that every rule-table fault key exists in `rules.yaml` (`load_rules`)
- `address < top < impact` for every labelled clip

(AR-33, NFR-3)
**And** with `EVAL_DATA_DIR` set, it also checks that every `clip_file` exists there; without it, that check is skipped

**Given** the set is complete
**When** the author backs it up
**Then** `EVAL_DATA_DIR` is copied off the laptop (USB drive or private cloud folder), and the date and place of the backup are noted in a comment at the top of `eval/labels.yaml` (AR-34, setup-guide §7)

### Story 2.4: Read a clip and print a versioned AnalysisResult from the CLI

As a developer,
I want `aicoach-engine analyse <clip>` to decode the clip upright, check that it is readable at a usable frame rate, and print a versioned `AnalysisResult` as JSON,
So that the engine's contract with the app exists end to end, with no database, web app or network.

**Slice:** `backend/engine/aicoach_engine/` (`__init__.py`, `result.py`, `formatting.py`, `ingest.py`, `cli.py`), `backend/engine/aicoach_engine/adapters/video_cv.py`, `backend/tests/engine/`
**Requirements:** AR-6, AR-11, FR-6 (CLI), FR-8 (decodability, fps), NFR-3, AD-5, AD-6, AD-15

**Acceptance Criteria:**

**Given** the engine package
**When** `AnalysisResult` is defined in `result.py`
**Then** it is a Pydantic model with every AD-9 field:
- `schema_version` (int, starting at 1)
- `clip {fps, duration_ms, width, height, rotation}`
- `clip_checks [{key, outcome: pass|warn|fail, display}]` and `fps_warning`
- `events`, `measurements`, `faults`, `observation`
- `film_better [{code, guide_step}]` and `reasons [{code, guide_step, label, detail}]`
- `evidence`, `explanation`, `main_finding`, `step_timings`, `rules_hash`, `pose_backend`
- key-frame overlay geometry

It uses the spine's enums and no `dict`/`Any`, so the app can reference it in OpenAPI (AR-11, AD-21)
**And** `explanation` is `null` in every engine output. The engine never writes an explanation; the app's `ExplanationWriter` fills `{text, source}` in the `explanation` step (AD-6, AD-9)
**And** a pytest round-trips a fully populated sample through JSON without loss

**Given** a value to display
**When** any `display` string is built
**Then** it comes from the one formatter in `formatting.py`: `body_height_ratio` 0.07 → "7% of body height", `deg` → "12°", `ms` 2070 → "2.07 s", `frames` → "3 frames", fps → "120 fps" `[ASSUMPTION: whole percents and whole degrees]` (AR-11, AR-29)
**And** a pytest asserts that every `display` in a sample result equals the formatter's output for its value and unit

**Given** a clip
**When** the VideoReader opens it
**Then** fps is the stream's `avg_frame_rate` from `ffprobe` (or the rule recorded by Story 2.1 if AD-15 was amended), and the result records it in `clip` (AD-15)
**And** rotation metadata is applied once, at decode, so every frame is upright, full and uncropped (AD-13)
**And** frames carry a 0-based `frame_index` into the full stream and `t_ms = frame_index × 1000 / fps` (AD-14)
**And** a pytest with a synthetic portrait clip, written in the test with 90° rotation metadata, gets upright frames with swapped width and height
**And** the engine never re-checks the extension or the duration (AD-15)

**Given** a clip OpenCV cannot decode
**When** it is analysed
**Then** the result is a rejection with reason `undecodable` (FR-8, AD-6)

**Given** fps below 30
**When** it is analysed
**Then** the result is a rejection with reason `fps_below_30`, label "Filmed at 24 fps" (for a 24 fps clip) and guide step `frame-rate` (FR-8)

**Given** fps of at least 30 and below 120
**When** it is analysed
**Then** the clip is analysed, its `fps` clip check is `warn`, and `fps_warning` is "Filmed at 60 fps — nothing can be rated 'high'." (for a 60 fps clip) (FR-8)

**Given** fps of 120 or more
**When** it is analysed
**Then** the `fps` check is `pass` and `fps_warning` is `null`

**Given** a rejection
**When** the result is built
**Then** `main_finding` is `cannot_analyse` and `faults` is empty
**And** `reasons` entries are `{code, guide_step, label, detail}`, copied from `rules.yaml` (AR-17)
**And** `explanation` is `null`

**Given** `analyse(video_path, rules, out_dir, on_step=None)`
**When** it runs
**Then** it calls `on_step(step_id, state, detail, partial_evidence)` with step IDs from one constant `STEP_IDS = ("pose", "events", "measurements", "rules", "explanation")` and states from `pending | running | done | skipped | stopped` (AD-5)
**And** the engine reports `pose` as `running`, then `done` with a detail that contains the fps display, or `stopped` on a rejection. On a rejection, every later step, `explanation` included, is reported `skipped`
**And** the engine never reports `explanation` as `running` or `done`; that step belongs to the worker (AD-6)
**And** `on_step=None` works
**And** `step_timings` holds ms for each engine step that ran
**And** `rules_hash` and `pose_backend` are recorded (AR-11)
**And** a pytest asserts that nothing is written outside `out_dir` (AD-1)

**Given** the CLI
**When** `aicoach-engine analyse <clip> [--rules PATH] [--out DIR]` runs
**Then** it prints the `AnalysisResult` JSON to stdout
**And** rules come from `--rules`, else `RULES_PATH`, else `config/rules.yaml`. Without `--out`, a new temp folder is used and its path is printed to stderr
**And** the exit code is 0 for a result and for a rejection, 2 with the `RulesError` message for an invalid rules file, and non-zero for any other error `[ASSUMPTION: exit codes]` (AR-6, FR-6)
**And** for a clip that passes the ingest checks, the sections this story doesn't compute are emitted empty (`events: []`, `measurements: []`, `faults: []`, `observation: null`, `evidence: []`) and `main_finding` is `null`
**And** the AD-1 import-linter contract from Epic 1 passes in pytest

### Story 2.5: Estimate pose behind a port in body-relative units

As a developer,
I want a `PoseEstimator` port with MediaPipe and RTMPose adapters that deliver the same joints, visibility scale and upright coordinates, followed by one shared smoothing and unit pipeline,
So that measurements don't depend on the pose library, the camera distance or the clip's aspect ratio.

**Slice:** `backend/engine/aicoach_engine/pose.py`, `backend/engine/aicoach_engine/adapters/mediapipe_pose.py`, `backend/engine/aicoach_engine/adapters/rtmpose.py`, import-linter contract (engine section of the backend config), `backend/tests/engine/`
**Requirements:** AR-9, FR-6 (body-relative distances), NFR-7, AD-13

**Acceptance Criteria:**

**Given** the port
**When** a backend runs on decoded frames
**Then** it returns a `PoseSequence {frame_w, frame_h, frames: [{frame_index, t_ms, joints}]}` (AR-9)
**And** joints use the `Joint` enum exactly: `nose`, and `l_`/`r_` × `shoulder`, `elbow`, `wrist`, `hip`, `knee`, `ankle`, `heel`, `foot_index`
**And** each joint has `x/frame_w`, `y/frame_h` (origin top-left) and a visibility from 0 to 1

**Given** an adapter
**When** it maps its model's output
**Then** MediaPipe (Tasks `PoseLandmarker`, VIDEO mode) uses its visibility score, and RTMPose (rtmlib) maps its keypoint score to 0–1 `[ASSUMPTION: clipped to the range]`. A joint the model lacks gets visibility 0 (AR-9)
**And** a shared contract test runs both adapters against fixture outputs
**And** `[ASSUMPTION]` a `-m models` test runs the real models when `MODELS_DIR` holds the files

**Given** `POSE_BACKEND` (`mediapipe` | `rtmpose`)
**When** `analyse()` starts
**Then** it picks that adapter and records its name in `pose_backend`. An unknown value stops with a clear error (AR-9)
**And** `[ASSUMPTION]` `analyse()` reads `POSE_BACKEND`, `MODELS_DIR` and `EVENT_DETECTOR` from the environment through one small engine config, because AD-1 fixes its signature

**Given** the model files
**When** an adapter loads them
**Then** they are read only from `MODELS_DIR` and checked against the SHA-256 in `backend/models/MANIFEST.yaml`
**And** a missing or mismatched file stops with an error that names the file and the manifest
**And** a pytest with network sockets blocked proves nothing is downloaded at runtime (AD-13)

**Given** the engine source
**When** import-linter runs in pytest
**Then** a contract fails if any module other than `aicoach_engine.adapters.*` imports `mediapipe` or `rtmlib` (AR-9)

**Given** one function that maps anatomical sides to lead and trail
**When** it is called
**Then** lead = left (`l_*`) and trail = right (`r_*`) for every clip. There is no handedness detection, and a pytest asserts the mapping is fixed (AR-9, AD-13)

**Given** normalised joints
**When** distances or angles are computed
**Then** that happens only after `to_px()`, which scales x by `frame_w` and y by `frame_h` (AR-9)
**And** a pytest shows a 45° segment stays 45° in a 1080×1920 and a 1920×1080 frame

**Given** pixel coordinates
**When** they are smoothed
**Then** a 6 Hz low-pass zero-phase Butterworth filter runs at the clip's own fps (addendum §A)
**And** `[ASSUMPTION]` gaps of low visibility (< 0.5) up to 100 ms are interpolated first
**And** a pytest shows 20 Hz synthetic jitter attenuated while 2 Hz motion is kept

**Given** a body unit
**When** distances are converted
**Then** they are divided by the body height at address, giving unit `body_height_ratio` `[ASSUMPTION: body height = px distance from nose to mid-ankle at address]` (FR-6, AR-9)
**And** a pytest shows the same synthetic swing at 0.5× scale gives identical ratios, so results don't depend on camera distance

**Given** the dependency lock and the manifest
**When** pytest runs
**Then** it fails if `uv.lock` contains `ultralytics` or another YOLO package, or if a `MANIFEST.yaml` licence is AGPL or non-commercial (NFR-7)

### Story 2.6: Find the swing and detect address, top and impact

As the author,
I want the engine to find the one swing in the clip, run full-rate pose only on that window, and detect address, top and impact with a clarity score,
So that analysis stays inside the NFR-1 budget and the events line up with my labels frame for frame.

**Slice:** `backend/engine/aicoach_engine/events.py`, `backend/engine/aicoach_engine/adapters/wrist_events.py`, `backend/engine/aicoach_engine/ingest.py` (swing count), `backend/tests/engine/`
**Requirements:** AR-10, FR-6, FR-8 (no swing, more than one swing), NFR-1, NFR-7, AD-14

**Acceptance Criteria:**

**Given** a decoded clip
**When** the `pose` step runs
**Then** a coarse pose pass over the whole clip, at about 30 samples per second `[ASSUMPTION]`, gives a smoothed wrist-height track and the swing candidates in it (takeaway, highest wrist point, lowest point after it) (AR-10)
**And** no candidate gives a rejection `no_swing`, and more than one gives `multiple_swings`, both with guide step `one-swing-light`, inside the `pose` step (FR-8, AD-6)

**Given** exactly one swing
**When** full-rate pose runs
**Then** it covers only the swing window from takeaway − 0.5 s to impact + 0.5 s `[ASSUMPTION: margins]`, about 2 s (addendum §A)
**And** a pytest on a 10 s synthetic clip counts the adapter calls and asserts that only window frames go through full-rate pose (NFR-1)

**Given** the windowed `PoseSequence`
**When** the `EventDetector` port runs with the default wrist-height heuristic (Yamamoto, after the 6 Hz filter)
**Then** it returns `address`, `top` and `impact`, each `{frame_index, t_ms, clarity 0–1}` (AR-10, AD-14)
**And** top is the highest wrist point, impact is the lowest wrist point after top, and address is the last still frame before takeaway (wrist speed below the still threshold) (FR-6)
**And** `[ASSUMPTION]` the still threshold and the clarity formula (peak prominence × wrist visibility) are named module constants, adjusted only on the tuning set

**Given** a synthetic swing placed 6.0 s into a 240 fps clip
**When** events are detected
**Then** every `frame_index` is 0-based in the full stream at native fps, with the trimming offset removed inside the engine, and `t_ms = frame_index × 1000 / fps` (AD-14)

**Given** a detector result that can't be ordered as `address < top < impact`
**When** events are checked
**Then** `[ASSUMPTION]` the clip is rejected with `no_swing` instead of guessing events

**Given** `EVENT_DETECTOR`
**When** it is unset or `wrist`
**Then** the wrist heuristic runs (AR-10)
**And** any other value stops with a clear error
**And** no SwingNet adapter is built in this epic. If one is ever added, it must be off by default and listed for removal before a paid launch (NFR-7, AD-14)

**Given** successful detection
**When** the result is built
**Then** `events` lists address, top and impact with `frame_index`, `t_ms` and `clarity`
**And** `on_step` reports `events` as `running`, then `done`
**And** `step_timings` includes `events`
**And** the tests use synthetic `PoseSequence` fixtures, so no video or model is needed

### Story 2.7: Reject clips the engine cannot read honestly

As the author,
I want the engine to reject face-on, out-of-frame, dark or blurred clips with every reason that applies and the guide step that fixes it,
So that AIcoach never guesses a fault from a clip that can't support one.

**Slice:** `backend/engine/aicoach_engine/ingest.py`, `backend/tests/engine/`
**Requirements:** FR-8 (engine checks), AR-11 (`clip_checks`, `reasons`), AD-6, SM-6

**Acceptance Criteria:**

**Given** the address pose
**When** the view check runs
**Then** a shoulder width that is wide relative to torso length (shoulders not overlapping as they do from DTL) gives reason `not_dtl` with guide step `view` `[ASSUMPTION: heuristic and cut-off]` (FR-8)

**Given** the swing window
**When** the framing check runs
**Then** body joints (nose, shoulders, hips, knees, ankles, heels, foot_index) that leave the frame or fall below a visibility cut-off in a share of window frames give `body_out_of_frame` (FR-8)
**And** hands that leave the frame, or come within a margin of its edge at top, give `club_out_of_frame` `[ASSUMPTION: the hands are the proxy, since the club is not tracked]`
**And** both reasons link to guide step `framing`

**Given** the window frames
**When** the light check runs
**Then** a mean luma below a cut-off, or a variance of the Laplacian below a cut-off, gives `too_dark_or_blurred` with its `rules.yaml` guide step (FR-8)
**And** `[ASSUMPTION]` these ingest cut-offs are named engine constants, adjusted only on the tuning set

**Given** a 24 fps face-on clip with the feet cut off
**When** it is analysed
**Then** one rejection carries all three reasons, `fps_below_30`, `not_dtl` and `body_out_of_frame`, because `fps_below_30` no longer stops the remaining checks (UX Flow 2, FR-8)
**And** only `undecodable` short-circuits

**Given** any analysed clip
**When** the result is built
**Then** `clip_checks` holds `view`, `framing`, `fps`, `light` and `swing` `[ASSUMPTION: keys]`, each `pass | warn | fail` with a formatter-made `display` (AR-11)

**Given** a rejection
**When** the result is built
**Then** the `pose` step is reported `stopped` and every later step `skipped`
**And** `events`, `measurements` and `faults` are empty and `main_finding` is `cannot_analyse`
**And** `reasons` are listed in check order, each with a `guide_step` from `guide_steps` (AD-6, AR-17)

**Given** the tests
**When** pytest runs
**Then** synthetic `PoseSequence` fixtures (face-on shape, cropped feet, hands out of frame) and synthetic dark and blurred frames each produce the expected reasons, and a clean fixture produces none (FR-8)
**And** these tests need no real clips

### Story 2.8: Measure the four faults with a confidence band on each

As the author,
I want the engine to compute the early-extension, loss-of-posture, over-the-top and sway measurements in body-relative units or degrees, each with one honest confidence band,
So that every number the coach will cite is measured the same way on every clip and never shown without its band.

**Slice:** `backend/engine/aicoach_engine/measures.py`, `backend/engine/aicoach_engine/confidence.py`, `backend/tests/engine/`
**Requirements:** FR-6, FR-7, FR-9 (sway defined from the start), AR-8 (`band()`), AR-9, AR-11 (measurement fields)

**Acceptance Criteria:**

**Given** smoothed pixel joints, events and the body unit
**When** the `measurements` step runs
**Then** it computes the four measurements below, each using the measurement key defined for its fault in `rules.yaml` `[ASSUMPTION: key names]` (FR-6, FR-9):

| Fault | Key | Definition | Unit |
|---|---|---|---|
| Early extension | `hip_toward_ball` | Horizontal mid-hip displacement from address to impact, toward the ball (the heel → foot_index direction at address), divided by body height | `body_height_ratio` |
| Loss of posture | `posture_angle_change` | Largest absolute change from address, over top → impact, of the trail-side head–hip–knee–ankle chain angles (at the hip: nose–hip–knee; at the knee: hip–knee–ankle). Same definition as the patent (addendum §B, OQ3) | `deg` |
| Over the top (hand-path proxy) | `hand_path_over_top` | Largest offset of the early-downswing hand path, outside (toward the ball) and above the backswing hand path at the same hand height, between top and the hands passing trail-shoulder height `[ASSUMPTION: window]`, divided by body height | `body_height_ratio` |
| Sway | `trail_hip_sway` | Change in the angle of the trail ankle → trail hip line from address to top. Negative means away from the target, as in addendum §B | `deg` |

**And** pytest checks each measurement on synthetic fixtures. For example, hips shifted 0.07 × body height toward the ball give `value` 0.07 and `display` "7% of body height"

**Given** a computed measurement
**When** it is added to the result
**Then** it has `key`, `label` (from `rules.yaml`), `value`, `unit`, `display` (from the formatter), `band`, and `thresholds {potential, fault}`, each threshold with its `display` (AR-11, AR-29)
**And** `[ASSUMPTION]` a measurement whose joints can't be computed raises an engine error, which the app shows as `failed`. It is never replaced by a guessed value; the framing check normally rejects such clips first

**Given** `confidence.band(measurement, rule, events, visibility, fps)`
**When** a band is computed
**Then** this is the only function that produces bands (AR-8, AD-12)
**And** it rates three components high, medium or low with the `rules.yaml` cut-offs:
- visibility: the mean visibility of the measurement's joints in its key frames
- margin: the distance from the value to the nearest boundary of the interval it falls in, as a fraction of |fault − potential| `[ASSUMPTION: normalisation]`
- clarity: the lowest `clarity` among the rule's events

**And** the band is the lowest of the three, then capped: under 120 fps it is never `high`, and over the top is at most `medium` (FR-7)

**Given** the caps
**When** pytest runs
**Then** a 119.9 fps fixture with perfect visibility, margin and clarity gets `medium`, and an over-the-top fixture with perfect inputs at 240 fps gets `medium` (FR-7, AR-8)

**Given** a measurement used only as an extra measurement (sway while it is the reserve)
**When** its band is set
**Then** it is `low`, so the measurement never disagrees with the observation built on it `[ASSUMPTION]` (FR-13, AD-12)

**Given** any finished result
**When** it is checked
**Then** every measurement has a band and none is `null` (FR-7)
**And** `on_step` reports `measurements` as `running`, then `done`, and `step_timings` includes `measurements`

### Story 2.9: Decide verified, possible and absent faults and pick the observation

As the author,
I want the rule table, and only the rule table, to decide each fault's outcome, the main finding and at most one unverified observation,
So that AIcoach reports a fault only past its threshold, says "No verified fault found" when none is, and never forces a fit.

**Slice:** `backend/engine/aicoach_engine/rules.py` (evaluation), `backend/engine/aicoach_engine/result.py`, `backend/tests/engine/`
**Requirements:** FR-9, FR-12, FR-13 (engine part), FR-7 (fault band, film better), AR-8, AR-11 (`main_finding`, `observation`, `film_better`)

**Acceptance Criteria:**

**Given** a measurement and its fault's `thresholds` and `direction`
**When** the `rules` step decides the outcome
**Then** a value past `fault` is `verified`, past `potential` is `possible`, and otherwise `absent`. "Past" means strictly beyond, in the fault's direction `[ASSUMPTION]` (FR-9, AD-12)
**And** `status: possible_only` caps the outcome at `possible`
**And** pytest checks values just below, at and just above each threshold for an `above` fault and a `below` fault

**Given** the outcomes
**When** `faults` is built
**Then** it lists every `active` and `possible_only` fault in `rules.yaml` order, as `{key, label, outcome, band, deciding_measurement}` (AR-11)
**And** a `reserve` fault is never reported as verified or possible (FR-9)
**And** the fault's band is its deciding measurement's band; an absent fault's band is `null` (AD-12)
**And** a pytest shows a verified fault with a `low` band stays verified, because a band never changes an outcome

**Given** a possible fault
**When** it is reported
**Then** it has no chain, drill or mobility exercise and does not count as a reported fault (FR-9)

**Given** a clip where every rule-table measurement is short of its potential threshold
**When** it is analysed
**Then** every fault is `absent`, `main_finding` is `no_fault`, and no chain, drill or mobility exercise appears anywhere in the result (FR-12)
**And** if some faults are possible but none verified, `main_finding` is `no_fault` and the possible faults stay listed with outcome `possible`

**Given** one or more verified faults
**When** `main_finding` is set
**Then** it is the key of the verified fault with the highest band, with ties broken by `rules.yaml` order. With none it is `no_fault`, and for a rejection it is `cannot_analyse`. It is never `null` in a finished result (AR-11, AD-9)

**Given** a verified fault with band `low`
**When** the result is built
**Then** `film_better` lists `{code, guide_step}` for each component that was low (`low_visibility` → `framing`, `unclear_events` → `frame-rate`, `low_fps` → `frame-rate`) (FR-7)

**Given** the `observations` list
**When** the observation is chosen
**Then** a candidate is an extra measurement past its own threshold whose key is not a fault in the active rule table (the engine checks this as well as the schema) (FR-13)
**And** if several pass, the one furthest past its threshold is chosen, measured as |value − threshold| / |threshold| `[ASSUMPTION: to compare across units]`
**And** the observation is `{measurement_key, template_text, text, band: "low"}`, with `text` = `template_text` in engine output `[ASSUMPTION: the app may replace text with ExplanationOut.observation_text]`
**And** with no candidate it is `null`

**Given** observation fixtures
**When** pytest runs
**Then** an observation can appear next to a verified fault and with `no_fault`
**And** it has no drill or mobility field, and its template names only its own measurement (FR-13)

**Given** the `rules` step
**When** it finishes
**Then** `on_step` reports `rules` as `running`, then `done`, and `step_timings` includes `rules`

### Story 2.10: Build the fault chain, evidence IDs, key frames and overlays

As the author,
I want each verified fault to carry its cause → mechanism → fault chain, its drill and mobility exercise, and numbered evidence with key-frame stills and overlay geometry,
So that every claim in the result points to the measurement and the frame it rests on.

**Slice:** `backend/engine/aicoach_engine/evidence.py`, `backend/engine/aicoach_engine/result.py`, `backend/tests/engine/`
**Requirements:** FR-10, FR-11 (snapshot), AR-11, AR-12 (engine part: E-IDs), AR-13, AD-5 (`partial_evidence`)

**Acceptance Criteria:**

**Given** detected events
**When** key frames are written
**Then** `out_dir/keyframes/{address|top|impact}.jpg` are plain JPEGs of the full upright frame, scaled but never cropped, with the frame's aspect ratio `[ASSUMPTION: longest side at most 1280 px]` (AR-13, AD-17)
**And** they exist in `out_dir` before `events` is reported `done`

**Given** a result
**When** evidence IDs are assigned
**Then** each item gets a stable ID `E1…En`, assigned once in a fixed order and never renumbered (AR-12, AD-10):
- `E1` = the address frame
- `E2` = the impact frame
- `E3` onwards = one ID per measurement, in `rules.yaml` order
- the top frame comes after the measurements

`[ASSUMPTION: this keeps the UX pin numbering: 1–2 key frames, 3+ measurements]`
**And** a pytest asserts that the same input gives identical IDs and that sorting the evidence list changes no ID

**Given** a key frame
**When** its overlay geometry is built
**Then** it is stored in `AnalysisResult`, normalised to that JPEG (AR-13, AD-17):
- points (joints with visibility) and body-line segments
- the hip keypoint marked to be ringed
- a dashed vertical address line through the address mid-hip on the address and impact frames
- the address pose as a dashed ghost on the impact frame
- a dimension arrow from the address line to the impact hip, labelled with the measurement's `display` (e.g. "+7%")
- `[ASSUMPTION]` backswing and downswing hand-path polylines on the top frame for over the top
- `[ASSUMPTION]` no club geometry, since the club is not tracked

**And** a pytest asserts every coordinate is in [0, 1] and matches `to_px` divided by the JPEG size

**Given** a verified fault
**When** its chain is built
**Then** it has three links in order:
- `cause`: `likely: true`, labelled from `rules.yaml`, with `evidence_ids` naming the mechanism's measurement and key frames (FR-10)
- `mechanism`: `likely: false`
- `fault`: `likely: false`

**And** every link's `evidence_ids` include the deciding measurement and at least one key frame, and the key frames are exactly the fault's `key_frames` events (early extension: address and impact) (FR-10)

**Given** a verified fault
**When** the practice items are added
**Then** `drill` and `mobility` (`name`, `dose`, `instructions`) are copied from that fault's `rules.yaml` mapping, and `mobility` carries the medical notice text (FR-11)
**And** possible and absent faults carry neither

**Given** a stored result
**When** `rules.yaml` is edited afterwards
**Then** the result's labels, chain text, drill and mobility exercise stay as they were when it ran (snapshot; pytest serialises, edits a copy of the rules, compares) (AR-11)

**Given** `on_step`
**When** `events` and `measurements` finish
**Then** `partial_evidence` holds the key-frame items after `events` and adds the measurement items after `measurements`, with the same IDs as the final `evidence` (AD-5)

**Given** a clear early-extension fixture
**When** it is analysed
**Then** the result holds the fault, the measurement with band, the three-link chain, key frames with overlay, drill and mobility exercise, i.e. SM-4's engine part; the explanation is the app's (Epic 4)

### Story 2.11: Score the engine with eval and bench

As the author and the examiner,
I want `aicoach-engine eval --split tuning|evaluation` to print the SM-1 to SM-6 report, and `aicoach-engine bench <clip> --runs 5` to print the NFR-1 median,
So that detection, honesty and speed are measured the same way every time, in the same container as the demo.

**Slice:** `backend/engine/aicoach_engine/cli.py` (`eval`, `bench`), `backend/engine/aicoach_engine/evaluation.py` `[ASSUMPTION: module name]`, `eval/`, `backend/tests/engine/`
**Requirements:** AR-33, NFR-3, NFR-1, FR-6 (event tolerances), FR-7 (SM-5), FR-9 (possible not counted), AR-6

**Acceptance Criteria:**

**Given** `EVAL_DATA_DIR` and `eval/labels.yaml`
**When** `aicoach-engine eval --split tuning|evaluation [--json PATH]` runs
**Then** it analyses every clip of that split only and prints a report headed by split, date, `rules_hash`, `pose_backend`, `EVENT_DETECTOR`, `schema_version` and clip count (AR-33, AD-24)
**And** with `EVAL_DATA_DIR` unset it exits 2 with a clear message
**And** `[ASSUMPTION]` a missing clip file is listed as missing, the run continues, and it exits 1 at the end

**Given** the report
**When** it is printed
**Then** it contains:
- **Per clip:** labelled faults, outcomes, bands, `main_finding` and event errors in frames
- **Events:** the share of clips with impact within ±1 frame and top within ±2 frames, and the address error, described only (FR-6)
- **SM-1:** per fault, verified ÷ labelled, flagged when fewer than 4 clips, against the 75 % target. A possible outcome does not count as detected (FR-9)
- **SM-2:** `no_fault` on clean clips (target at least 2 of at least 3)
- **SM-3:** none of the three verified on outside-fault clips, and any observation's band is `low`
- **SM-4:** for early-extension clips, whether fault, measurement, band, chain, key frame, drill and mobility exercise are present
- **SM-5:** how often `high` vs `low` verified faults are correct, tested only with at least 3 in each band, otherwise counts only (FR-7)
- **SM-6:** every `expect: rejection` clip is rejected with at least one reason and guide step, and never gets a fault

**Given** the backend container (Epic 1)
**When** `docker compose run --rm -v "${EVAL_DATA_DIR}:/eval-data:ro" -e EVAL_DATA_DIR=/eval-data backend aicoach-engine eval --split tuning` runs
**Then** the report is produced inside the container, which is the run whose numbers count (AD-24, setup-guide §7)

**Given** `aicoach-engine bench <clip> --runs 5`
**When** it runs
**Then** it runs `analyse()` 5 times in fresh out-dirs and prints each run's wall time, its `step_timings` and the median (NFR-1, AD-5)
**And** it reports pass or fail against 120 s for a clip of 10 s or less and 180 s for one of 15 s or less, using the clip's `duration_ms`
**And** it notes that the app's measure adds the mock explanation step
**And** `--runs` below 1 is refused

**Given** pytest
**When** the engine suite runs
**Then** the report logic is tested with synthetic results and labels, with no clips needed (NFR-3)
**And** `[ASSUMPTION]` `pytest -m eval` runs the tuning split when `EVAL_DATA_DIR` is set and skips otherwise
**And** neither `eval` nor `bench` writes to `rules.yaml` or `labels.yaml`

### Story 2.12: Tune thresholds and decide over the top vs sway by 2026-12-01

As the author,
I want a tuning tool that reads only the tuning set, and a recorded checkpoint decision on over the top vs sway,
So that thresholds stay honest and the active rule table is settled for P1 without ever looking at the evaluation set.

**Slice:** `backend/engine/aicoach_engine/cli.py` (`tune`), `config/rules.yaml`, `eval/reports/` `[ASSUMPTION: committed reports with numbers only, no clips]`, architecture `.memlog.md`, `backend/tests/engine/`
**Requirements:** AR-35 (OQ3, OQ4, OQ7), AR-33 (tuning tools refuse the evaluation split), FR-9, FR-13, AR-8 (cut-offs per backend)

**Acceptance Criteria:**

**Given** `aicoach-engine tune --split tuning [--fault KEY]`
**When** it runs
**Then** for each fault it prints every tuning clip's measurement value next to its label, plus the detection rate and the false positives on clean and outside-fault clips, at the current thresholds and over a grid of candidate thresholds (OQ3)
**And** `[ASSUMPTION]` pose output is cached outside the repository, so a sweep doesn't re-run pose

**Given** `tune --split evaluation`, or a labels entry with `split: evaluation` reaching the tool
**When** it starts
**Then** it exits 2 with "Tuning tools never read the evaluation split (AD-24)" and reads no clip (AR-33)
**And** a pytest proves this

**Given** the tuning report
**When** the author adjusts the rule table
**Then** thresholds and the body-relative conversion change only in `rules.yaml` (FR-9, OQ3)
**And** the confidence cut-offs are re-tuned for the chosen `POSE_BACKEND` (AD-13)
**And** the report also shows false positives, so detection is not bought by loosening thresholds (SM-C1)

**Given** 2026-12-01
**When** over the top's detection rate on the tuning set is compared with the SM-1 target (75 %)
**Then** if it meets the target, over the top stays active and sway stays reserve (OQ4)
**And** if it doesn't, the `status` fields are edited (`over_the_top: reserve`, `sway: active`), and the OQ7 replacement extra measurement is chosen from the tuning set and added to `observations` with its threshold and template `[ASSUMPTION: the default candidate is over the top's own hand-path measurement]` (OQ7, FR-13)

**Given** the decision
**When** it is recorded
**Then** the memlog has a dated entry with the tuning-set numbers, `rules_hash` before and after, `pose_backend` and the chosen statuses, and the tuning report is saved under `eval/reports/` (AR-35)
**And** the evaluation split has not been run before the decision
**And** the "two faults fail on the evaluation set → possible_only" fallback is left to the final-week evaluation (Epic 8)

**Given** the edited `rules.yaml`
**When** pytest and `aicoach-engine analyse` on a tuning clip run
**Then** the rules tests pass and the faults reflect the new statuses
**And** the git diff for the decision touches only `config/rules.yaml`, the report and the memlog; no code changes (FR-9, AD-11)


## Epic 3: Film, send, and watch the coach analyse the swing

A player reads the filming guide, sends a clip from phone or desktop, and watches the step log in one thread at one URL. The thread ends in a rejection (reasons linked to guide steps), a failure with "Try again", or a plain verdict summary. Every clip lands in the swing library, and the 50-clip limit is enforced.

### Story 3.1: Read the filming guide on a phone before filming

As a player at the range,
I want a six-step filming guide I can read on my phone, signed in or not,
So that I film a clip AIcoach can analyse the first time.

**Slice:** backend `app/modules/system/` (extends `/api/config`); frontend `src/modules/guide/`, routes `src/app/guide/` and `src/app/guide/[slug]/`
**Requirements:** FR-4, NFR-5, NFR-6, AR-7, AR-24, AR-28, UX-DR37, UX-DR49

**Acceptance Criteria:**

**Given** the app has started with `config/rules.yaml` loaded by `load_rules()` (Epic 2)
**When** anyone, signed in or not, calls `GET /api/config`
**Then** the response also contains `guide_steps`: the ordered list of the six slugs from `rules.yaml` `guide_steps`, typed in OpenAPI and regenerated into `frontend/openapi.json` and `src/shared/api/schema.d.ts` (AR-24, AR-23)
**And** a pytest asserts the `guide_steps` value equals `load_rules().guide_steps` and that every `reasons` entry in `rules.yaml` maps to a slug in that list (AR-7)

**Given** a visitor who is signed out
**When** they open `/guide`
**Then** the page renders with the landing header, and a signed-in player sees the same page inside the app shell with the rail or menu (UX-DR5, UX-DR37)
**And** the overview shows six numbered rows (paper-2 number circle, the rule in one line, a chevron), each row a single link target to its step page `/guide/{slug}` (UX-DR37)
**And** under the rows one mono meta line reads exactly "AIcoach reads right-handed swings for now." (FR-4)
**And** a primary "I'm ready to film" button links to `/swing/new`; a signed-out visitor goes through sign-in and back there (Epic 1 protected-route behaviour)

**Given** the six steps
**When** their text is checked against FR-4
**Then** together they state: down the line (DTL) view only; camera at hand height at address, level, on or parallel to the hands line; about 2.4–3.7 m (8–12 ft) away; on a tripod or stable surface; 120 fps or higher recommended; whole body and club in frame for the full swing; one swing per clip; good light (FR-4)
**And** `[ASSUMPTION]` the steps are, in order: 1 view (down the line only), 2 position (hand height, level, on the hands line), 3 distance (2.4–3.7 m, tripod or stable surface), 4 frame rate (120 fps or higher), 5 framing (whole body and club in frame), 6 one swing and good light — matching EXPERIENCE Flow 2 (face-on → step 1, fps → step 4, feet out of frame → step 5); the slugs themselves are whatever `rules.yaml` `guide_steps` defines
**And** `[ASSUMPTION]` the step headline and reason lines live in the guide module keyed by slug (guide copy is UI copy, not rule-table coaching copy)

**Given** a step page `/guide/{slug}` for a slug in `guide_steps`
**When** it renders
**Then** it shows "Step n of 6" in clay, the rule as the headline, a card with the top-down placement diagram (dashed target line with arrow, phone block, ghost-body player ellipse, teal mono "2.4–3.7 m · 8–12 ft"), two to four lines of reason in ink-2, six 8px step dots with the current one clay, and Back (secondary) / Next step (primary) side by side (UX-DR37, UX-DR43)
**And** the step's root element has `id="{slug}"`, and each overview row has the same slug as its `id` (AR-28)
**And** Back on step 1 returns to `/guide`; `[ASSUMPTION]` on step 6 the primary reads "I'm ready to film" and links to `/swing/new`

**Given** a URL `/guide/{slug}` whose slug is not in `guide_steps`
**When** it is opened
**Then** the Epic 1 not-found page is shown, never an empty step

**Given** the guide module's ordered slug list
**When** the Vitest suite runs
**Then** a test asserts the list equals the guide-step slugs exposed in the committed `frontend/openapi.json` (same values, same order), so a renamed slug in `rules.yaml` fails the build (AR-28, AR-32)

**Given** a phone viewport of 360px width and text zoomed to 200 %
**When** the overview and every step page are viewed
**Then** nothing scrolls horizontally (the diagram is an SVG with a `viewBox` that scales to the column), all text remains readable, Back / Next sit in the bottom third, and every control has a 44×44px hit area and the teal focus ring (FR-4, NFR-5, UX-DR49) — checked manually and recorded in the story notes

### Story 3.2: Store an uploaded clip in the swing library and queue its analysis

As a player,
I want the clip I send to be checked, stored in my swing library and queued for analysis,
So that every clip I send is kept and nothing unusable or oversized slips in.

**Slice:** backend `app/modules/swings/` (models, `repo.py`, `repo_system.py`, `service.py`), `app/modules/swings/upload/`, `app/core/` (FileStore paths, error codes), `app/modules/identity/service.py` (wiring only), one Alembic migration
**Requirements:** FR-2, FR-5, FR-18, NFR-2, NFR-8, AR-14, AR-15, AR-18, AR-19, AR-20, AR-21, AR-29, AR-30

**Acceptance Criteria:**

**Given** the migration of this story (the only one in it)
**When** `alembic upgrade head` runs
**Then** it creates `clips` (`id` UUID, `user_id` → `users` `ON DELETE CASCADE`, `original_filename`, `ext` mp4|mov, `size_bytes`, `duration_ms`, `playback_state` pending|ready|failed default `pending`, `created_at`) and `analyses` (`id` UUID, `user_id` → `users` `ON DELETE CASCADE`, `clip_id` → `clips` nullable, unique, `ON DELETE SET NULL`, `status` enum queued|running|result|rejection|failed, `progress` and `result` as `JSON().with_variant(JSONB, "postgresql")`, `error` nullable, `created_at`, `started_at`, `finished_at`), with an index on (`status`, `created_at`) (AR-30, AR-14, AR-29)
**And** the existing upgrade → downgrade → upgrade test passes on Postgres and the single-head test still passes (AR-30)

**Given** a signed-in player with fewer than 50 clips
**When** they `POST /api/clips` (multipart, field `file` `[ASSUMPTION]`, header `X-Requested-With: aicoach`) with a 4 s `.mp4` or `.MOV` clip
**Then** the file is streamed to a temp file outside any DB transaction, checked, and then in one short transaction `identity.service.lock_user` is taken, the clip count is re-checked, a `clips` row (`playback_state=pending`) and a `queued` `analyses` row are inserted together, and the file is moved to `users/{user_id}/clips/{clip_id}/original.{mp4|mov}` through FileStore (AR-19, AR-21, AR-15)
**And** the response is `201 {analysis_id, clip_id}`; the extension is stored lowercase, and the path is built from IDs only (AR-15)
**And** the new analysis has `progress = {steps: [pose, events, measurements, rules, explanation] all "pending", partial_evidence: []}` (AR-16)

**Given** an upload request
**When** the route checks it
**Then** the checks run in exactly this order and stop at the first failure: library count (fast pre-check before streaming) → extension mp4/mov (case-insensitive) → `ffprobe` finds a video stream → container duration ≤ 15.0 s (`MAX_CLIP_SECONDS`) (AR-20)
**And** the refusals return the error envelope with codes from `app/core/errors.py`: `409 library_full`, `415 unsupported_format`, `422 no_video_stream`, `422 clip_too_long` `[ASSUMPTION: code names and statuses; none are named in the sources]` (AR-21, AR-23)
**And** each refusal deletes the temp file and creates no `clips` or `analyses` row — a pytest per refusal asserts zero rows and an empty temp folder (AR-21)
**And** the route never checks fps, view or framing; those belong to the engine (AR-20)

**Given** a request body larger than `MAX_UPLOAD_MB` (300 decimal MB, 300,000,000 bytes)
**When** it reaches the backend directly (bypassing Caddy)
**Then** the backend stops reading, deletes the temp file and returns `413 upload_too_large` with no row created (AR-21)

**Given** a player who already has 50 `clips` rows
**When** they upload
**Then** the fast pre-check returns `409 library_full` before the body is streamed to disk (FR-5, AR-19)
**And** a `pytest -m pg` test with 49 clips and two concurrent uploads asserts exactly one is accepted and the other gets `409 library_full`, so the count never exceeds 50 (AR-19, AR-30)

**Given** player A's upload and the endpoint without a session
**When** an unauthenticated request posts to `/api/clips`, or a request omits `X-Requested-With`
**Then** it is refused by the Epic 1 auth dependency (`401`) or CSRF middleware respectively, and no file is written (AR-18, AR-22)
**And** every new `repo.py` function takes `user_id` as a required argument; `list_ids_for_sweep` lives only in `swings/repo_system.py` (AR-18)

**Given** a signed-in player
**When** they call `GET /api/me`
**Then** `clips_count` and `analyses_count` come from `swings.service` count functions (identity calls the swings public interface only) (AR-14, AR-25)

**Given** a player with stored clip files
**When** they delete their account through the Epic 1 `DELETE /api/me`
**Then** `identity.delete_account` commits the `users` row delete (clips and analyses cascade), then calls the new `swings.service.purge_user_files(user_id)`, which removes `DATA_DIR/users/{user_id}/` through FileStore (AR-14, AR-19)
**And** if the folder delete fails (e.g. a Windows file lock, simulated in the test), the failure is logged with the user ID only, the account delete still succeeds, and the startup orphan sweep added in this story removes the folder on the next start (AR-15)
**And** a `pytest -m pg` test asserts the cascade removes `clips` and `analyses` rows; SQLite tests run with `PRAGMA foreign_keys=ON` (AR-30)

**Given** the app starts
**When** the startup hook runs
**Then** an orphan sweep walks only `DATA_DIR/users/` and `DATA_DIR/tmp/`, removes folders with no matching `users` / `clips` / `analyses` row and all leftover temp uploads, and never touches `DATA_DIR/system/` (AR-15)

**Given** any accepted or refused upload
**When** it is logged
**Then** the log line carries `analysis_id`/`clip_id` and size, never `original_filename`, the email or file contents; the clip never leaves the laptop and no outbound network call is made (AR-15, AR-31, NFR-2)
**And** every stored clip belongs to an account that has a stored consent version (Epic 1 creates no account without it), asserted in the upload test via the signup fixture (FR-18)

### Story 3.3: Run the analysis in the background worker and report progress

As a player,
I want my queued clip analysed in the background with live step progress,
So that the app stays responsive and I end up with a stored result or rejection.

**Slice:** backend `app/modules/swings/analysis/` (`worker.py`, `routes.py`, `service.py`, `schemas.py`), `app/modules/swings/repo.py` / `repo_system.py`, app startup hook
**Requirements:** FR-2, FR-5, FR-8, FR-18, NFR-1, NFR-2, AR-14, AR-15, AR-16, AR-17, AR-18, AR-23, AR-31

**Acceptance Criteria:**

**Given** the backend starts as one Uvicorn process
**When** startup completes
**Then** the orphan sweep (Story 3.2) runs first and the in-process worker starts after it, with a one-process engine pool (AR-16)
**And** the worker claims jobs only with `UPDATE … SET status='running', started_at=now() WHERE id=(SELECT id … WHERE status='queued' ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED) RETURNING id` in `repo_system.claim_next_queued`, checking for work about once a second `[ASSUMPTION: poll interval]` (AR-16)
**And** a `pytest -m pg` test with two concurrent claimers and two queued rows asserts each row is claimed exactly once (AR-30)

**Given** a claimed analysis
**When** the worker starts the run
**Then** it first deletes the analysis's key-frame folder, then calls `aicoach_engine.analyse(original_path, rules, DATA_DIR/tmp/{analysis_id}/, on_step)` in the pool process, never on the event loop (AR-16, AR-17)
**And** every `on_step(step_id, state, detail, partial_evidence)` reaches the parent through a `multiprocessing` queue and is written to `analyses.progress = {steps, partial_evidence}`, with `steps` always listing all five IDs in the fixed order `pose → events → measurements → rules → explanation` and states `pending | running | done | skipped | stopped` (AR-16, AR-17)
**And** `[ASSUMPTION]` when the `pose` step reports `done` its detail carries the engine-read `fps` and whether the 30–119 fps warning applies; the worker stores both in `progress` so the browser never computes or shows fps before the server has read it (AR-20)

**Given** the engine returns an `AnalysisResult` with `main_finding` = a fault key or `no_fault`
**When** the `explanation` step runs
**Then** the worker marks `explanation` running, calls the registered `ExplanationWriter.write(result) -> ExplanationOut {explanation_text, observation_text|null, source}` with its own `LLM_TIMEOUT_SECONDS` (20 s) limit, and on **any** exception or timeout uses the template writer instead; the step never produces `failed` (AR-17)
**And** the default writer in this story is template-only: it takes the template explanation (and the observation's `template_text`, if any) snapshotted from `rules.yaml`, sets `source: "template"`, touches no database and makes no network call (AR-17, NFR-2)
**And** `swings.service.register_explanation_writer(writer)` is the public hook a later slice uses to replace it; `swings` imports nothing from `coach` (AR-14)

**Given** the run has finished
**When** the worker writes the outcome
**Then** it imports the key frames from the scratch folder to `users/{user_id}/analyses/{analysis_id}/keyframes/{event}.jpg` through FileStore, deletes the scratch folder, and does one terminal `UPDATE … SET status, result (ExplanationOut merged in), progress (final steps), finished_at WHERE id=:id AND status='running'` in `repo_system.finish_job` (AR-15, AR-17)
**And** if that update matches 0 rows (the row was deleted, e.g. account deleted mid-run), the worker deletes everything it imported for the job — a test deletes the row mid-run and asserts no key-frame files remain (AR-17, AR-19)
**And** `[ASSUMPTION]` after the terminal write the worker calls any hooks registered through `swings.service.register_after_terminal_hook` in the same slot; none are registered in this epic, so `clips.playback_state` stays `pending` (the transcode belongs to Epic 5)

**Given** the engine result is a rejection (`main_finding = cannot_analyse`)
**When** the worker finishes it
**Then** the status is `rejection`, the step that found the reason is `stopped` and later steps `skipped`, the writer is not called, the result carries `reasons [{code, guide_step, label}]` and no fault outcomes, and the clip row and file stay linked to the analysis (FR-8, FR-18, AR-17)

**Given** the engine raises an exception
**When** the worker catches it
**Then** the terminal write sets `failed` with an `error` code, marks the step that was running `stopped`, keeps the clip, and never writes `rejection` or a result (AR-17)

**Given** a finished `result`
**When** its timings are read
**Then** `result.step_timings` holds the engine steps plus the `explanation` step `[ASSUMPTION: the worker adds the explanation timing]`, and `started_at` / `finished_at` are stored so `finished_at − started_at` measures NFR-1 (upload, queue and transcode excluded); a log line per analysis records the total with `analysis_id` (NFR-1, AR-31)
**And** a pytest runs one bundled sample clip through the worker in mock mode and asserts it ends in `result` or `rejection`, never `failed`; the formal NFR-1 bench stays with `aicoach-engine bench` (Epic 2 / Epic 8)

**Given** a signed-in player and their analysis in any status
**When** they call `GET /api/analyses/{id}`
**Then** it returns the analysis view: `id`, `status`, `created_at`, `started_at`, `finished_at`, `clip {clip_id, original_filename, duration_ms} | null`, `progress`, `fps | null`, `fps_warning`, and `result` (the engine's `AnalysisResult` model, typed in OpenAPI, no `dict`/`Any`) or null while not terminal (AR-16, AR-23)
**And** another player's ID returns `404 not_found`, never the data (FR-2, AR-18)
**And** a stored result whose `schema_version` differs from the engine's returns `409 result_outdated` (AR-11)

**Given** the import-linter and boundary tests
**When** pytest runs
**Then** a test asserts `swings/repo_system.py` is imported only by `worker.py` and the startup hook, and the engine still imports nothing from `app` (AR-18, AR-6)

### Story 3.4: Recover from stuck or crashed analyses and retry a failed one

As a player,
I want an analysis that hangs or dies to end as "failed" and be re-runnable on the same clip,
So that a system problem never leaves me waiting forever or looks like a verdict.

**Slice:** backend `app/modules/swings/analysis/` (`worker.py`, `routes.py`, `service.py`), `app/modules/swings/repo.py` / `repo_system.py`, app startup hook
**Requirements:** FR-2, FR-5, AR-16, AR-17, AR-18, AR-31

**Acceptance Criteria:**

**Given** a running analysis whose engine call has not returned
**When** `ANALYSIS_TIMEOUT_SECONDS` (600) has passed since `started_at`
**Then** the worker kills the pool process, creates a new one-process pool, and only then writes `failed` with error code `timeout` through the conditional terminal write, deleting the scratch folder (AR-16)
**And** the next queued analysis is claimed and runs normally on the new pool — a pytest with a stub engine that sleeps and a timeout of 1 s proves both (AR-16)

**Given** the backend restarts while an analysis is `running`
**When** startup runs
**Then** the order is exactly: orphan sweep → `repo_system.fail_running_on_startup` sets every `running` row to `failed` (error `restart`, running step `stopped`) → the worker starts (AR-16)
**And** `queued` rows are left queued and are picked up by the worker

**Given** a `failed` analysis whose `clip_id` is not null
**When** its owner calls `POST /api/analyses/{id}/retry` (with `X-Requested-With: aicoach`)
**Then** in one statement the status goes back to `queued` and `progress` (all five steps `pending`, no partial evidence), `result`, `error`, `started_at` and `finished_at` are reset; the response returns the analysis view (AR-17)
**And** the worker re-runs it on the stored clip, deleting the old key-frame folder first (AR-17)

**Given** an analysis that is `queued`, `running`, `result` or `rejection`, or a `failed` one whose clip was deleted (`clip_id` null)
**When** retry is called
**Then** it returns `409 retry_not_allowed` and nothing changes (AR-17)
**And** another player's analysis ID returns `404 not_found` (FR-2, AR-18)

**Given** any failure path (exception, timeout, restart)
**When** it is logged
**Then** one line records `analysis_id`, the error code and the step that was running, without the file name or email (AR-31)

### Story 3.5: Watch the coach analyse my swing in its thread

As a player,
I want one thread per swing that shows my clip, the coach's frame-rate line and the step log filling in live,
So that I can see the analysis is progressing and can leave and come back to the same URL.

**Slice:** frontend `src/modules/upload/` (thread view, step log), `src/shared/conversation/` (created: coach message, player message, typing indicator), route `src/app/swing/[analysisId]/`; backend `app/modules/swings/analysis/` (adds `slow` to the analysis view)
**Requirements:** FR-5, AR-20, AR-28, UX-DR7, UX-DR8, UX-DR9, UX-DR32, UX-DR33, UX-DR45, UX-DR49

**Acceptance Criteria:**

**Given** the shared conversation folder
**When** this story creates it
**Then** `shared/conversation/` holds the coach message (coach mark + italic "Coach" + local time, Newsreader body, no bubble, arrives whole, announced politely), the player message (right-aligned ink bubble max 384px, meta "You · time" `[ASSUMPTION: the account has no display name]`, upload-echo variant with file name and length in mono, never fps) and the typing indicator (mark + three dots + "Coach is watching your swing…", not re-announced) (UX-DR8, UX-DR9)
**And** `shared/conversation/` imports no slice; ESLint boundary rules pass (AR-28)

**Given** a signed-in player opens `/swing/{analysisId}` for their `queued` or `running` analysis
**When** the page loads
**Then** the thread shows the coach's request for one down-the-line swing, the player's clip echo (file name and length "3.8 s" from `clip.original_filename` and `clip.duration_ms`), the step log card and the typing indicator (UX-DR7, UX-DR9)
**And** before the first response the layout shows dashed placeholders in the final positions, never a spinner; a load failure shows "Couldn't load this. Try again." inline (UX-DR45)
**And** the page polls `GET /api/analyses/{id}` about once a second through TanStack Query while the status is `queued` or `running`, and stops polling at a terminal status (AR-16, AR-28)

**Given** the step log
**When** progress arrives
**Then** it shows five rows Pose · Swing events · Measurements · Rule table · Explanation with 10px status circles joined by a line: done (high green + check), running (clay partial ring), pending (hairline ring), stopped (ink-2 ring + ×), skipped shown as pending; each row's mono detail right-aligned; a 4px clay progress bar with "n of 5" in mono (UX-DR32)
**And** the step states come only from `progress.steps`; the frontend never infers a step from time (AR-28)
**And** each change is announced once through a polite live region (e.g. "Pose done. 1 of 5.") without moving focus (UX-DR32, UX-DR49)

**Given** the server reports `fps` after the Pose step
**When** the next poll arrives
**Then** a coach message appears once: "Got it — a clean down-the-line clip at {fps} fps. Watching now." with the server's fps rounded to a whole number `[ASSUMPTION: rounding]`; before that no fps is shown anywhere (AR-20, UX-DR32)

**Given** an analysis still `running`
**When** the backend sees `now − started_at ≥ SLOW_ANALYSIS_SECONDS` (180)
**Then** the analysis view returns `slow: true` (server clock, so a phone's clock skew does not matter) `[ASSUMPTION: computed server-side]`
**And** the thread adds the coach line "This is taking longer than it should. I'm still watching." as an inline message, the step log keeps its place, the typing indicator stays, and no action is offered (UX-DR33, UX-DR46)

**Given** a player leaves the thread during analysis and comes back
**When** they reopen the same URL
**Then** the thread shows the current state from the server; the analysis kept running while they were away (UX-DR7)

**Given** an analysis ID that does not exist or belongs to another player
**When** the URL is opened
**Then** the page shows "This analysis doesn't exist or isn't yours." with a link to your swings, never the data (FR-2, UX-DR45)

**Given** a poll fails because the network dropped
**When** the next poll also fails
**Then** the last known state stays on screen with the inline message "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." and "Try again"; polling resumes on success and the message clears `[ASSUMPTION: the network-lost line also covers polling, not only upload and chat]` (UX-DR45, UX-DR46)

**Given** a phone viewport (<768px)
**When** the thread renders
**Then** it is one column with a 20px gutter and no horizontal scroll, using the Epic 1 top bar (UX-DR4, NFR-5)
**And** Vitest tests cover the step-log state mapping (each of the five states, "n of 5") and the fps-line rule (shown only once fps is present)

### Story 3.6: Send a swing clip from the New swing page, on desktop or phone

As a player,
I want to drop or pick a clip and see it upload in the thread,
So that sending a swing is one action on the laptop and a deliberate send on the phone.

**Slice:** frontend `src/modules/upload/` (new-swing view, drop zone, ready-to-send preview, client pre-checks), `src/shared/api/` (upload XHR helper), `src/shared/conversation/` (adds the disabled composer line), route `src/app/swing/new/`
**Requirements:** FR-5, FR-18, NFR-2, NFR-5, AR-21, AR-24, UX-DR9, UX-DR29, UX-DR30, UX-DR31, UX-DR45, UX-DR46, UX-DR49

**Acceptance Criteria:**

**Given** a signed-in player with fewer than 50 clips opens `/swing/new`
**When** the page renders
**Then** the thread shows a coach message asking for one down-the-line swing with the filming checklist as the message (the six guide rules taken from the guide module's public `index.ts`) and a link to `/guide` (UX-DR29)
**And** below it the drop zone: 640px card, dashed ink-2 border (7 6), upload circle, "Drop your swing clip here", "or choose a file · mp4 or mov · max 15 s", a hairline, and the library note "Goes into your swing library" + "Stored on the AIcoach server until you delete it. Only you can see it." as information, not a control — no save toggle anywhere (UX-DR30, FR-18)
**And** the composer area shows only the disabled line "You can ask the coach once the result is ready." `[ASSUMPTION: a disabled-composer component in shared/conversation; the live composer is Epic 6]` (UX-DR29)
**And** the limits (15 s, mp4/mov, 300 MB, 50 clips) are read from `/api/config`, never hard-coded (AR-24)

**Given** a desktop viewport (≥768px)
**When** the player drops or chooses a valid clip
**Then** it sends at once — no ready-to-send step — and one clip at a time: the drop zone is disabled while an upload runs (UX-DR30)

**Given** a file that is not mp4/mov, or whose browser-read length is over 15 s
**When** it is dropped or chosen
**Then** nothing is uploaded and an inline coach-voice message appears under the drop zone: "I read mp4 or mov files." or "That clip is {n} s. I can read up to 15 s — trim it and send it again." (n = browser length, whole seconds); choosing another file clears it (FR-5, UX-DR30, UX-DR46)
**And** if the browser cannot read the length (e.g. an HEVC `.mov`), the client check passes and the server decides — the pre-check is advisory only (UX-DR30, AR-20)

**Given** the upload is running
**When** progress events arrive
**Then** the upload goes through the one XHR helper in `shared/api/` with `X-Requested-With: aicoach`, and the player message echo shows a first-frame thumbnail (captured in the browser), file name and length in mono, and a 4px clay progress bar along the bubble's bottom edge — never fps (AR-21, UX-DR9)
**And** on `201 {analysis_id, clip_id}` the page replaces the URL with `/swing/{analysis_id}` and the thread continues as in Story 3.5 (UX-DR7)

**Given** the server refuses the upload
**When** the response is `415 unsupported_format`, `422 clip_too_long`, `422 no_video_stream`, `409 library_full`, `413 upload_too_large` or Caddy's bare `413` (mapped to `upload_too_large` by the client)
**Then** the matching inline message appears under the drop zone and the player can choose another clip (AR-21, UX-DR30)
**And** `[ASSUMPTION: copy not in the sources]` `clip_too_long` uses the 15 s line (with the browser length if known, else "That clip is longer than 15 s…"), `no_video_stream` reads "I couldn't find a video in that file. Send an mp4 or mov clip.", and `upload_too_large` reads "That file is over 300 MB. Trim it and send it again."

**Given** the network drops during the upload
**When** the XHR errors
**Then** the inline message "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." appears with "Try again", which re-sends the same file (UX-DR45, UX-DR46)

**Given** a player whose `GET /api/me` `clips_count` equals `max_clips_per_player` (50)
**When** `/swing/new` renders, or an upload returns `409 library_full`
**Then** the drop zone is disabled (paper-2 fill, ink-2 text) with the inline message "Your swing library is full (50 clips). Delete a clip before sending a new one." and a link to `/library` (FR-5, UX-DR30)

**Given** a phone viewport (<768px)
**When** the player taps "choose a file"
**Then** the native picker opens on Photos / Files (`accept` mp4/mov), and a valid clip goes to the ready-to-send preview: card on keyframe ground with the first frame and a play mark, file name, "{n} s of 15 s" in mono (browser length), the coach line "Looks right. Send it when you're ready.", the library note card, "Send to the coach" (primary, 56px) and "Choose a different clip" (text button, reopens the picker) (UX-DR31, UX-DR43)
**And** "Send to the coach" starts the same upload as on desktop

**Given** the app runs with `docker compose up` and a phone on the same Wi-Fi opens `http://<laptop-ip>:8080`
**When** the player sends a clip from the phone
**Then** the upload completes and the thread opens on the phone; the clip goes only to the laptop (manual check per setup-guide §6.3, recorded in the story notes) (NFR-2, NFR-5)
**And** Vitest tests cover the pre-check rules (extension case-insensitive, length over/under 15 s, unknown length passes) and the error-code → message mapping including the bare 413

### Story 3.7: See the Evidence panel, drawer and tray fill in while the swing is analysed

As a player,
I want an evidence area that shows where to put the phone before I send and pins the evidence live while the coach works,
So that I can see what is being measured without opening anything else.

**Slice:** frontend `src/shared/evidence/` (created: panel, drawer, tray shells, evidence chip, placeholder, pin, confidence band), `src/shared/ui/` (placement diagram moved from `src/modules/guide/`), `src/modules/upload/` (panel content for pre-upload and analysing), routes `src/app/swing/new/` and `src/app/swing/[analysisId]/` (fill the shell's evidence slot)
**Requirements:** UX-DR4, UX-DR19, UX-DR23, UX-DR26, UX-DR27, UX-DR28, UX-DR29, UX-DR49

**Acceptance Criteria:**

**Given** a viewport ≥1344px
**When** `/swing/new` or a thread is open
**Then** the Evidence panel is a sticky 408px card column beside the 640px thread with the title "Evidence", a teal pin icon, the pin count in mono teal and one ink-2 subtitle line (UX-DR4, UX-DR26)

**Given** a viewport of 768–1343px
**When** the page renders
**Then** the panel content lives in a right drawer (408px, over the scrim) opened from the header Evidence chip; the drawer traps focus, closes with Esc, the close button or a scrim tap, and returns focus to the chip (UX-DR4, UX-DR28, UX-DR49)

**Given** a phone viewport (<768px)
**When** the page renders
**Then** the Evidence chip sits at the top bar's right and opens a bottom-sheet tray with a 40×5 grab handle, the title "Evidence · pinned live" and a horizontal row of items; swipe down or a scrim tap closes it; during analysis the tray peeks at the bottom with the live pins (UX-DR28)

**Given** the Evidence chip
**When** there are no pins
**Then** it reads "Evidence · 0" in the idle style (paper-2); with n pins it reads "Evidence · n" teal on tint (UX-DR28)

**Given** `/swing/new` before any upload
**When** the evidence area renders
**Then** it shows the "Where to put the phone" top-down diagram (the guide's placement diagram, moved to `shared/ui/` because this is its second user), dashed placeholders labelled "Address frame", "Impact frame" and "Measurement", and "0 pins · Nothing measured yet." (UX-DR26, UX-DR27, UX-DR29)

**Given** a running analysis whose `progress.partial_evidence` grows
**When** a poll returns new items
**Then** each item appears as a pin (teal 18px square, white mono number from its `E<n>` ID, never renumbered) with its label in place of the matching placeholder; the subtitle reads "n pins so far" and the chip count updates (UX-DR23, UX-DR26, AR-12)
**And** placeholders not yet filled show a centred meta label — "drawing lines…" while Pose or Swing events run, "measuring…" while Measurements runs — and never a spinner (UX-DR26, UX-DR27)
**And** `[ASSUMPTION]` in this epic a pinned item shows its label and pin in the dashed box, not the key-frame image or the ruler; those are added by the Epic 4 key frame and measurement card
**And** each pin has an accessible name built from its ID and label (e.g. "Evidence 1, address frame"), and activating it highlights the item (tint + teal outline) and opens the drawer or tray at it (UX-DR23, UX-DR49)

**Given** the confidence band component in `shared/evidence/`
**When** it renders a band
**Then** it shows three 4×11px bars (high 3 lit, medium 2, low 1; unlit at 25 %) and the text "confidence: high|medium|low" in the same colour; screen readers read the word, never the bars; it has no "no band" variant and never shows a percentage (UX-DR19, NFR-11)
**And** Vitest tests cover the bar count per band, the text, and the chip's idle/active states

### Story 3.8: See the outcome in the thread — rejection with guide links or a plain verdict summary

As a player,
I want the thread to end with either the reasons my clip could not be analysed, each linked to the right guide step, or a short verdict with its confidence band,
So that I know what happened to my swing and what to do next.

**Slice:** frontend `src/modules/upload/` (outcome views, rejection reason row, verdict summary, fps warning), `src/shared/conversation/` (adds the collapsed system line), route `src/app/swing/[analysisId]/`
**Requirements:** FR-4, FR-5, FR-8, FR-18, UX-DR7, UX-DR8, UX-DR34, UX-DR35, UX-DR46, UX-DR49

**Acceptance Criteria:**

**Given** an analysis reaches `result` or `rejection`
**When** the poll returns the terminal status
**Then** polling stops, the typing indicator is removed, completion is announced once in the polite live region, and the coach's request and the upload echo fold into the collapsed system line: a 40px paper-2 pill "Clip received · {file name} · {3.8 s} · analysed in {n} s" (n = `finished_at − started_at`, whole seconds) with "Show" / "Hide" that expands and folds it in place (UX-DR7, UX-DR49)

**Given** a `rejection`
**When** the thread renders it
**Then** the step log stays with the stopped row (ink-2 ring + ×) and later rows pending, and a coach message says "Cannot analyse" + "I won't guess from this clip. {n} things got in the way:" `[ASSUMPTION: n written as a word, and "One thing got in the way:" for a single reason]` (FR-8, UX-DR34)
**And** one rejection reason row per `result.reasons` entry: an ink-2 × mark, the reason `label` from the result, one line of explanation, and a clay link "Filming guide · step {n} ›" to `/guide/{guide_step}`, where n is the slug's 1-based position in `/api/config` `guide_steps` — the frontend never maps reason codes itself (FR-4, FR-8, UX-DR34, AR-28)
**And** `[ASSUMPTION]` the one-line explanation comes from the reason entry snapshotted in `AnalysisResult` from `rules.yaml`; if Epic 2's reason entry carries only `label`, the row shows the label alone rather than copy written in a component
**And** a primary "Film again" links to `/swing/new`, the footer reads "No result was made. The clip is in your swing library; delete it there if you don't need it.", and no faults, verdict or composer are shown (FR-8, FR-18, UX-DR34)
**And** a component test with a three-reason rejection fixture (face-on, feet out of frame, 24 fps) asserts three rows linking to steps 1, 5 and 4 under the Story 3.1 slug order

**Given** a `result` whose `main_finding` is a fault key
**When** the thread renders it
**Then** a coach message gives a plain verdict summary: the main finding's `label` (from the matching `result.faults` entry) with that fault's confidence band component — no chain, practice, key frames or numbers without pins in this epic (UX-DR8, UX-DR19)

**Given** a `result` whose `main_finding` is `no_fault`
**When** the thread renders it
**Then** the coach message reads "No verified fault found" and names no fault (FR-12 wording; the full no-fault outcome is Epic 4)

**Given** the server reports the 30–119 fps warning (in `progress` during analysis, or `result.fps_warning` after it)
**When** the thread renders
**Then** an inline warning with a medium-coloured `!` reads "Filmed at {fps} fps — nothing can be rated 'high'." under the fps line, and it stays after the outcome (FR-8, UX-DR35, UX-DR46)
**And** a clip under 30 fps never shows this warning; it arrives as a rejection with its own reason row (FR-8)

**Given** a player reopens a finished thread later
**When** the page loads
**Then** it renders the stored outcome directly (collapsed system line, stopped step log for a rejection, summary for a result) without polling (UX-DR7)
**And** a `409 result_outdated` response shows the inline line "This result was made by an older version of AIcoach and can't be shown." `[ASSUMPTION: copy not in the sources]`

### Story 3.9: Try again after an analysis fails on our side

As a player,
I want a clear "something went wrong on my side" message with a way to re-run the same clip,
So that a system failure never looks like a verdict on my swing and I don't have to upload again.

**Slice:** frontend `src/modules/upload/` (failed outcome, retry action), route `src/app/swing/[analysisId]/`
**Requirements:** FR-5, AR-17, UX-DR33, UX-DR43, UX-DR45, UX-DR46, UX-DR49

**Acceptance Criteria:**

**Given** an analysis whose status becomes, or already is, `failed`
**When** the thread renders it
**Then** polling stops, the typing indicator is removed, the step log row that was running shows "stopped", and a coach message says "Something went wrong on my side, not with your clip. Nothing was analysed." with "Try again" and "New swing" (dark button linking to `/swing/new`) (UX-DR33, UX-DR43)
**And** no rejection reasons, filming tips, guide links, fault or band are shown — a failure never looks like a rejection or a result (UX-DR33)
**And** the failure is announced once in the polite live region (UX-DR49)

**Given** the failed analysis still has its clip (`clip` not null)
**When** the player activates "Try again"
**Then** the client calls `POST /api/analyses/{id}/retry`; on success the step log resets to five pending rows, the typing indicator returns, polling resumes, and the thread follows the new run as in Story 3.5 (AR-17)

**Given** the clip was deleted (`clip` is null)
**When** the failed thread renders
**Then** "Try again" is not offered; only "New swing" is (AR-17)
**And** if the server still answers `409 retry_not_allowed`, an inline message reads "I can't run this clip again. Send it as a new swing." `[ASSUMPTION: copy not in the sources]` (UX-DR46)

**Given** the network drops when "Try again" is pressed
**When** the request fails
**Then** the inline message "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." appears with "Try again", and nothing else changes (UX-DR45, UX-DR46)
**And** Vitest tests cover the failed view (no reason rows, Try again shown only with a clip) and the retry state transition


## Epic 4: Read the full result with its evidence and the coach's explanation

A player opens a finished analysis and reads the full result thread: the verdict with its confidence band, the feel cue, the fault chain, one drill and one mobility exercise with the medical notice, Also checked, at most one unverified observation, or the no-fault outcome. Key frames with overlays, the measurement card with its threshold ruler and the Evidence panel / drawer / tray back every number. The explanation is written through `CoachLLM` (OpenRouter, mock or template fallback) and checked by one grounding check, so mock mode works end to end and a model outage never breaks a result.

### Story 4.1: Check every coach text against the analysis

As a player,
I want everything the coach writes about my swing to be checked against my analysis before I see it,
So that the explanation never invents a fault, number or drill and never sees my personal data.

**Slice:** `backend/app/modules/coach/` (shared `facts.py`, `grounding.py`), `backend/tests/coach/`, shared citation fixture `tests/fixtures/citations.json`
**Requirements:** FR-12, FR-13, FR-14, NFR-9, AR-12, AR-26 (CoachFacts), AR-27 (explanation and observation kinds), AR-31, SM-7

**Acceptance Criteria:**

**Given** a stored `AnalysisResult` with status `result`
**When** `build_coach_facts(result, rules)` is called
**Then** it returns a `CoachFacts` Pydantic model (`extra="forbid"`) holding only analysis data: each fault's key, label, outcome, band, deciding measurement `display`, chain links (role, label, `likely`, evidence IDs), drill and mobility (name, dose, instruction text); each measurement's key, label, `display`, band and threshold displays; the observation (measurement key, label, `display`, `template_text`, band `low`) or null; evidence items (ID, kind, label, swing event and `t_ms` for key frames — labels only, never images); `main_finding` (AR-26, AD-18)
**And** the function takes only the `AnalysisResult` and the `RuleTable`, never a user, clip or analysis row

**Given** `CoachFacts` built from every SM-7 fixture
**When** the NFR-9 test serialises it to JSON
**Then** no key is named `email`, `user_id`, `clip_id`, `analysis_id`, `path`, `filename`, `original_filename` or `url`, and no string value ends in `.jpg`, `.mp4` or `.mov` or contains the `DATA_DIR` prefix (NFR-9)
**And** the test compares `CoachFacts`' field names with a committed allow-list, so a new field fails until it is reviewed

**Given** the citation syntax `[E<n>]` (AR-12, AD-10)
**When** text is parsed with the one compiled `CITATION_RE` in `coach/grounding.py`
**Then** `[E3]` and `[E12]` are found with IDs `E3` and `E12`, and `[e3]`, `[E]`, `[E 3]`, `E3` and `[3]` are not citations
**And** a pytest reads the shared fixture `tests/fixtures/citations.json` (inputs, expected citation IDs and expected word counts) `[ASSUMPTION: fixture path]`, which Story 4.6 also runs in Vitest

**Given** the signature `grounding_check(output, facts, kind)`
**When** it is called with `kind` = `explanation` or `observation`
**Then** it returns `{passed, violations: [{code, detail}]}` with codes `disallowed_name`, `unknown_number`, `band_mismatch`, `word_limit`, `jargon`, `feel_cue_count`, `unknown_evidence_id` `[ASSUMPTION: code names]`
**And** the rules are looked up per kind in one table, so Epic 6 adds `chat` without changing the explanation or observation rules; until then `kind="chat"` raises `ValueError`

**Given** an explanation for a result with a verified early extension and a possible loss of posture
**When** it names early extension, restricted hip rotation, the wall drill and 90/90 hip rotation
**Then** it passes
**And** when it names loss of posture, its cause, its drill or its mobility exercise, or any fault not verified, it fails with `disallowed_name` (FR-14)

**Given** a "No verified fault found" result
**When** an explanation names any fault, cause, drill or mobility exercise of the rule table
**Then** it fails with `disallowed_name` (FR-12, FR-14)
**And** an explanation that names none of them passes

**Given** a result whose deciding measurement shows `7%` and whose drill dose is `3 × 10 reps`
**When** an explanation contains "7%", "3 × 10" and the citation `[E3]`
**Then** it passes, because allowed numbers are the `display` values plus the numbers inside drill and exercise text, and evidence IDs do not count as numbers (AD-19)
**And** "12%" or "0.93" in the same text fails with `unknown_number`

**Given** a verified fault with band `medium`
**When** a band word (high, medium or low) stands in the same sentence as that fault's name `[ASSUMPTION: "next to" = same sentence]`
**Then** "medium" passes and "high" or "low" fails with `band_mismatch` (AD-19)

**Given** the limits and blocklist in `rules.yaml` `coach`
**When** an explanation `body` has 151 words, or contains "Kinematic sequence" in any letter case
**Then** it fails with `word_limit` or `jargon`; a body of exactly 150 words passes (FR-14)
**And** words are counted as whitespace-separated tokens with `[E<n>]` citations excluded, the same rule as the shared fixture `[ASSUMPTION]`

**Given** `feel_cues` in an explanation output
**When** a verified fault has zero or two feel cues, or a feel cue is keyed to a fault that is not verified
**Then** it fails with `feel_cue_count`; exactly one per verified fault passes, and none for "No verified fault found" passes (FR-14)

**Given** an output citing `[E9]` or listing `{type: evidence, id: E9}` in `based_on`
**When** the facts have no evidence item `E9`
**Then** it fails with `unknown_evidence_id`; a `based_on` fact key outside `drill|mobility|observation|rule_table|explanation` also fails (AR-12)

**Given** an observation built on the sway measurement
**When** its text names only that measurement and its `display` value
**Then** it passes with `kind="observation"`
**And** naming any fault of the active rule table, any drill or mobility exercise, or a number not in the analysis fails (FR-13)

**Given** the SM-7 fixed-input suite `backend/tests/coach/test_grounding_sm7.py`
**When** pytest runs with no network
**Then** it covers fixtures for early extension high, a medium fault, two verified faults, no fault with observation and no fault without observation, each with a passing output and at least one failing output per rule above (SM-7)

**Given** every explanation template, observation template and mock explanation text in `rules.yaml`
**When** a test fills each one for every fixture main finding (each fault verified alone, two verified, `no_fault`) and runs it through `grounding_check`
**Then** all pass, and a failure names the template key (AR-27)
**And** the chat refusal texts and mock chat answers join this test in Epic 6 with the `chat` kind

**Given** any check run
**When** it fails
**Then** only the violation codes and the `analysis_id` are logged, never the checked text (AR-31)

### Story 4.2: Reach the language model through one gateway, with mock mode by default

As a player (and the examiner running AIcoach with no keys),
I want the coach to write my explanation with or without a language-model key,
So that I always get a result and running AIcoach costs nothing in mock mode.

**Slice:** `backend/app/modules/coach/llm.py`, `backend/app/core/settings.py` (mock-mode resolution), `backend/app/modules/system/` (config reads it), `backend/tests/coach/`
**Requirements:** FR-14, FR-15, NFR-4, NFR-9, NFR-10, AR-24 (mock mode), AR-26 (`explain`), AR-31

**Acceptance Criteria:**

**Given** the `CoachLLM` port in `coach/llm.py`
**When** the coach slice asks for an explanation
**Then** it calls `async explain(facts: CoachFacts) -> ExplainOut {body, feel_cues: [{fault_key, text}], observation_text | null, based_on: [{type: evidence, id} | {type: fact, key}]}` (AR-26, AD-18)
**And** the adapter is chosen in one factory `get_coach_llm(settings, rules)`, so Epic 6 adds `answer(facts, history, question)` without changing callers

**Given** the settings combinations `LLM_MODE=mock` with a key, `LLM_MODE=auto` with an empty key, and `LLM_MODE=auto` with a key
**When** the app starts
**Then** the first two use the Mock adapter and the third the OpenRouter adapter, and the app never fails because a key is missing (AR-24, NFR-4)
**And** `GET /api/config` `mock_mode` comes from the same function `is_mock_mode(settings)` in `app/core/settings.py`, tested for all three combinations

**Given** an empty `OPENROUTER_API_KEY`
**When** the factory runs
**Then** no OpenRouter provider or pydantic-ai model object is constructed (AD-18)

**Given** the OpenRouter adapter (`pydantic-ai-slim[openrouter]`, model `OPENROUTER_MODEL`, timeout `LLM_TIMEOUT_SECONDS`=20)
**When** `explain` runs against a pydantic-ai `FunctionModel` that captures the request
**Then** the request holds only fixed instructions (plain words, at most 150 words, exactly one feel cue per verified fault, cite numbers as `[E<n>]`) plus the `CoachFacts` JSON, with no email, user ID, analysis ID, clip ID, path, file name or image part (NFR-9)
**And** the model's output is parsed as structured output into `ExplainOut`

**Given** the Mock adapter
**When** `explain` runs on any SM-7 fixture
**Then** it builds `ExplainOut` from `CoachFacts` and the `rules.yaml` mock texts: the mock explanation for the main finding, the rule table's feel cue for each verified fault, the observation's `template_text` unchanged (FR-13), and `based_on` with the evidence IDs it uses
**And** the same input always gives the same output, it passes `grounding_check` for every fixture, and a test with sockets blocked proves it makes no network call (FR-15)

**Given** a transport error, a timeout or output that does not parse
**When** the OpenRouter adapter's `explain` runs
**Then** it raises a typed `CoachLLMError` (`unavailable`, `timeout` or `invalid_output`) for the caller to fall back on, with no retry for explanations

**Given** any `explain` call
**When** it finishes or fails
**Then** one log line `llm_call` records `analysis_id`, adapter (`mock|openrouter`), model, kind `explanation`, input and output tokens, `cost_usd`, `cost_nok` (via `AI_USD_NOK`=10.5), duration and outcome (`ok|timeout|error|invalid_output`) (NFR-10, AR-31)
**And** the mock adapter logs 0 tokens and cost 0, and no line ever contains prompt text, output text or an email
**And** `[ASSUMPTION]` the cost is the one OpenRouter reports in the response usage; if it is missing, `cost_usd=null` is logged

**Given** a configured `OPENROUTER_API_KEY`
**When** pytest runs with the marker `-m llm`
**Then** the SM-7 fixtures run through the OpenRouter adapter and `grounding_check`, and without a key the marker is skipped (SM-7)
**And** `[ASSUMPTION]` until the model is chosen at P2 start (OQ2), `.env.example` leaves `OPENROUTER_MODEL` as a placeholder and P1 runs in mock mode

### Story 4.3: Write the grounded explanation and observation when the analysis finishes

As a player,
I want my result to arrive with a short plain-language explanation and, when there is one, a reworded unverified observation,
So that I understand what was found, even when the language model is down.

**Slice:** `backend/app/modules/coach/explanation/` (service, writer), app startup registration, `backend/tests/coach/`
**Requirements:** FR-12, FR-13, FR-14, FR-15, NFR-1, AR-14, AR-17, AR-26, AR-27

**Acceptance Criteria:**

**Given** the app starts
**When** the startup hook runs
**Then** `coach` registers its `CoachExplanationWriter` through the `swings` public registration function, replacing Epic 3's template-only writer (AR-14, AD-2)
**And** a test asserts the registered writer type, and the import-linter contract still shows that `swings` never imports `coach`

**Given** a result with a verified fault and a language model whose output passes `grounding_check(kind="explanation")`
**When** the worker's `explanation` step calls `write(result)`
**Then** it returns `ExplanationOut {explanation_text, observation_text, source: "llm"}`, and `GET /api/analyses/{id}` shows `explanation {text, source: "llm"}` (FR-14, AR-17)
**And** `[ASSUMPTION]` `explanation_text` is the `body` followed by the feel cues in fault order, and the 150-word limit applies to that text

**Given** mock mode
**When** an analysis with a stubbed engine result runs from upload to result in an API test
**Then** the result has `explanation.source = "mock"`, its text passes the grounding check, and `observation.text` equals `observation.template_text` (FR-13, FR-15)
**And** the `explanation` step adds no noticeable time, so the NFR-1 timing (which includes this step in mock mode, AD-5) is unaffected

**Given** the model raises `CoachLLMError`, raises any other exception, takes longer than `LLM_TIMEOUT_SECONDS` (tested with a short timeout and a slow fake), or returns output that fails the grounding check
**When** the writer runs
**Then** the explanation is the template from `rules.yaml` for that main finding with `source: "template"`, the `explanation` step is `done`, and the analysis ends as `result`, never `failed` (FR-14, AR-17)
**And** only the fallback reason code is logged

**Given** a result with an observation
**When** the writer runs
**Then** the observation is reworded through `explain` and checked with `kind="observation"`; if it passes it becomes `observation_text`, otherwise `observation_text` is the `template_text` unchanged (FR-13)
**And** in mock mode `observation_text` is always the `template_text` unchanged, the explanation and the observation fall back independently, and with no observation `observation_text` is null (the writer never creates one)

**Given** a "No verified fault found" result and a fake model whose text names early extension
**When** the writer runs
**Then** the grounding check fails and the template explanation, which names no fault, is used (FR-12, FR-14)

**Given** a result with two verified faults
**When** the writer runs with the Mock adapter
**Then** the explanation holds exactly one feel cue for each fault (FR-14)

**Given** a rejection
**When** the worker finishes it
**Then** the writer is never called and the rejection has no explanation (AR-17)

**Given** the writer
**When** it is tested
**Then** it runs with no database session (it takes only the `AnalysisResult`, AD-6), and the story adds no table and no migration because the text is stored in `analyses.result` by the worker's terminal write

### Story 4.4: See my key frames with my body lines drawn on them

As a player,
I want to see the key frames from my own clip with the skeleton and hip line drawn on top,
So that I can see the fault with my own eyes, not just read a number.

**Slice:** backend `app/modules/swings/analysis/` (routes, service); frontend `src/shared/evidence/` (key frame), `src/modules/result/` (Evidence panel result frames); tests
**Requirements:** FR-2, FR-10, AR-13, AR-15, AR-18, AR-25, UX-DR24, UX-DR26 (result frames), UX-DR27, UX-DR49

**Acceptance Criteria:**

**Given** a signed-in player and their analysis with status `result`
**When** the browser requests `GET /api/analyses/{id}/keyframes/{event}` for an event that has a stored key frame
**Then** the response is `200` with `Content-Type: image/jpeg`, read through `FileStore` from `users/{user_id}/analyses/{analysis_id}/keyframes/{event}.jpg` (AR-15, AR-25)
**And** the session cookie authenticates it, so a plain `<img>` works on the phone and the laptop

**Given** another player's analysis ID, a deleted analysis, an analysis that is a rejection or not finished, or an event with no key frame
**When** the key frame is requested
**Then** the response is `404 not_found` in the error envelope and no data is returned (FR-2, AR-18)
**And** an event outside the swing-event enum is refused before any path is built, so a path comes from IDs only (AR-15)
**And** signed out, the response is `401` (AR-18)

**Given** the key frame component in `shared/evidence/`
**When** it renders an event's JPEG with the overlay geometry from `AnalysisResult`
**Then** the JPEG is the background of a 322:360 box on `keyframe-ground`, scaled and never cropped, and the overlay SVG is drawn over the image's rendered area in the JPEG's normalised coordinates (AR-13, UX-DR24)
**And** the overlay uses the DESIGN.md tokens: ghost-body capsules, a 3.4px body-line skeleton with round joins, keypoint dots, the club line with the ball, the floor band, and the hip keypoint ringed

**Given** the address and impact frames of early extension
**When** they render
**Then** the address frame draws a dashed vertical reference line (dash 9 7) through the address hip, and the impact frame repeats that line, overlays the address pose dashed (7 6) and draws the "+n%" dimension arrow labelled with the result's `display` value (UX-DR24)

**Given** a rendered key frame
**When** it is read under the frame or by a screen reader
**Then** the frame name and the event time (from `t_ms`, e.g. "2.07 s" in mono) show under it `[ASSUMPTION: two decimals]`
**And** the alt text states the event, the time and what the overlay shows, e.g. "Impact, 2.07 s. Hips 7% of body height closer to the ball than the dashed address line." `[ASSUMPTION: built from the event, t_ms and the deciding measurement's label and display]` (AR-13, UX-DR49)

**Given** a key frame
**When** the player activates it (click, tap, Enter or Space)
**Then** it opens larger in a bottom sheet with the same overlays; focus moves in and returns on close, and Esc, swipe down or a scrim tap closes it (UX-DR24, UX-DR49)
**And** opened from the phone's evidence tray, the sheet replaces the tray, so sheets are never stacked `[ASSUMPTION]`

**Given** an analysis that turns `result` while the thread is open, or a cold load of a finished result
**When** the Evidence panel, drawer or tray shows the result
**Then** the frame placeholders are replaced in place by the key frames of the swing events the main finding's rule uses, side by side at 164px with a 16px gap in the panel, never with a spinner (FR-10, UX-DR26, UX-DR27)
**And** if a key frame image fails to load, its dashed placeholder stays with its frame label `[ASSUMPTION]`

**Given** a key frame that a pin or citation points to
**When** it is the cited item
**Then** it gets a teal outline 3px outside the frame (UX-DR24)

### Story 4.5: Check each measurement against its rule in the Evidence panel

As a player,
I want to see the measurement that decided my result on a ruler against the rule threshold, with my other measurements and the clip checks one tap away,
So that I can see how far past the line I am and how sure the coach is.

**Slice:** frontend `src/shared/evidence/` (measurement card, threshold ruler), `src/modules/result/` (Evidence panel, drawer and tray result contents); Vitest
**Requirements:** FR-7, NFR-11, UX-DR19, UX-DR22 (more measurements, clip checks), UX-DR25, UX-DR26, UX-DR27, UX-DR28 (result contents in the Epic 3 shells), UX-DR35 (warning in clip checks)

**Acceptance Criteria:**

**Given** a result
**When** the Evidence panel (≥1344px) shows it
**Then** it reads top to bottom: title "Evidence" with the teal pin icon, the pin count "n pins" in mono teal, one ink-2 subtitle line ("Measured from your clip. Cited pins light up."), the two key frames, the dashed-line legend, the cited measurement card, the "n more measurements" row and the "Clip checks passed · n of n" row (UX-DR26)
**And** the Evidence chip reads "Evidence · n" with n = the number of evidence items (UX-DR28)

**Given** the measurement card in `shared/evidence/`
**When** it shows the main finding's deciding measurement (the default cited measurement)
**Then** it shows the tint card with teal border, the pin, the measurement label, the `display` value in 52px mono, the unit line, the threshold ruler and the confidence band (UX-DR25)
**And** the ruler shows the track, a teal fill from 0 to the value, an ink tick at the fault threshold labelled "rule {fault threshold display}", the card-filled marker with a teal ring at the value, and mono end labels
**And** `[ASSUMPTION]` the end labels ("0%", max) come from display strings in the result, because the frontend formats no number (AD-9); positions are proportional, and a measurement whose fault side is negative fills toward the negative end

**Given** a measurement whose fault is `possible`
**When** its measurement card shows
**Then** the ruler also shows the potential threshold tick with its display label (UX-DR25)

**Given** the measurement value component
**When** it is used anywhere in the result
**Then** `band` is a required prop, so a measurement without a band is a type error, and a Vitest walks every result fixture and asserts each rendered measurement has a "confidence: …" band next to it (FR-7, NFR-11)
**And** the band shows exactly the result's band (never raised, never computed in the UI), as three bars plus "confidence: high|medium|low", never a percentage; a 60 fps fixture therefore shows no "high" (UX-DR19)

**Given** the "n more measurements" row
**When** the player opens it
**Then** it expands in place and lists every other measurement with its label, `display` value, band and pin; the collapsed row names them in one line (e.g. "lead hip turn · posture angle · hand path"); the state is not kept between visits (UX-DR22)

**Given** the "Clip checks passed · n of n" row
**When** the player opens it
**Then** it lists the view, frame and fps checks from `clip_checks` with their `display` text (UX-DR22)
**And** for a 30–119 fps clip the row also shows the frame-rate warning "Filmed at 60 fps — nothing can be rated 'high'." with the medium-coloured `!`, using the same warning line Epic 3 shows in the thread (moved to `shared/` if it lives in a slice) (UX-DR35) `[ASSUMPTION: a warn check counts as passed, with the warning shown]`

**Given** a "No verified fault found" result
**When** the panel shows it
**Then** `[ASSUMPTION]` the measurement card cites the observation's measurement if there is one, else the first measurement in evidence order, and the frames are the key frames in `evidence`

**Given** a narrow laptop (drawer) or a phone (tray)
**When** the drawer or tray opens on a result
**Then** the drawer shows the same content as the panel at 408px, and the tray shows the frames and measurement cards in one horizontal row under "Evidence · pinned live" (UX-DR28)

**Given** a cold load of a result
**When** data is not there yet
**Then** dashed placeholders with meta labels stand in for frames and the measurement card in the final layout, and a load failure shows "Couldn't load this. Try again." inline; no spinner anywhere (UX-DR27)

### Story 4.6: Follow any pin or citation to its evidence

As a player,
I want every pin and `[n]` citation to take me to the frame or measurement it points to,
So that I can check any number the coach states.

**Slice:** frontend `src/shared/evidence/` (`citations.ts`, inline citation, cite state), `src/modules/result/`; Vitest
**Requirements:** AR-12, UX-DR23, UX-DR28 (opening the drawer/tray at an item), UX-DR49

**Acceptance Criteria:**

**Given** `frontend/src/shared/evidence/citations.ts`
**When** it parses text
**Then** it uses one regex that mirrors `CITATION_RE` in `coach/grounding.py`, and a Vitest runs it against the shared fixture `tests/fixtures/citations.json` with the same expected IDs and word counts as the pytest (AR-12)
**And** it splits text into plain segments and citations for rendering

**Given** text containing `[E3]`
**When** it renders
**Then** the citation shows as a raised teal mono `[3]` link (the number from the evidence ID, never renumbered)
**And** a citation whose ID is not in the result's `evidence` renders as plain text, not a link `[ASSUMPTION]`

**Given** a pin, an inline citation or a cited value
**When** the player activates it with a click, a tap, Enter or Space
**Then** the matching evidence item is highlighted (tint fill and teal outline; a key frame gets its outside outline) and scrolled into view: in the panel at ≥1344px, by opening the drawer at that item at 768–1343px, and by opening the tray at that item under 768px (UX-DR23, UX-DR28)
**And** activating a measurement pin changes the measurement card to that measurement

**Given** the drawer opened from a pin
**When** it is open
**Then** it traps focus, closes with Esc, its close button or a scrim tap, and returns focus to the pin (UX-DR28, UX-DR49)

**Given** the cite state in `shared/evidence/`
**When** a pin is activated
**Then** that item stays lit until another is activated, and the state exposes a "set lit pins" function that Epic 6 uses to keep the latest answer's citations lit (UX-DR23)
**And** with reduced motion there is no scroll animation and no pulse on lit pins (UX-DR49)

**Given** any pin or citation
**When** a screen reader reaches it
**Then** its accessible name states the evidence number, label, value and band, e.g. "Evidence 3, hip movement toward the ball, 7% of body height, confidence high", and a key-frame pin states the frame and time `[ASSUMPTION]` (UX-DR23)
**And** the 18px pin keeps a 44px hit area on the phone and shows the focus ring (UX-DR49)

### Story 4.7: Read the verdict, the feel cue and the full explanation

As a player,
I want the result to open with what the coach found, how sure it is, one feel cue and the full explanation on request,
So that I know in seconds what is wrong with my swing and how it should feel.

**Slice:** frontend `src/modules/result/`, `src/shared/layout/` (library status in the page header), `src/app/swing/[analysisId]/` (composition); Vitest
**Requirements:** FR-7, FR-9, FR-14, FR-15, NFR-11, AR-24 (mock labels), AR-28, UX-DR11, UX-DR12, UX-DR14, UX-DR15, UX-DR22 (explanation row), UX-DR48 (several verified faults)

**Acceptance Criteria:**

**Given** the thread at `/swing/[analysisId]` and an analysis with status `result`
**When** it loads, or the analysis finishes while the thread is open
**Then** the route renders the result module's view below the collapsed system line, replacing Epic 3's plain verdict summary (AR-28)
**And** all fault names, chain labels, drill and mobility texts and coaching lines come from the `AnalysisResult`, never from component constants (AR-28)

**Given** the result page header
**When** it renders
**Then** it shows the title (the analysis date in local time), the meta line (e.g. "Analysed in 41 s · 120 fps · down the line", with fps from the server's result) and the library status "In your swing library ›" in ink-2 label text, no pill, linking to `/library/{clipId}` (UX-DR12)
**And** when the analysis has no clip (`clip_id` null) it reads "Clip deleted" and is not a link, and there is never a save control or the word "Saved" (UX-DR12, UX-DR50)
**And** the library status lives in `shared/layout/`, and the Epic 3 rejection header uses it too (rule 3)

**Given** a verified fault
**When** the coach message for it renders
**Then** it shows the fault's lead line from the result followed by the band phrase: high → "and I'm sure of it", medium → "I'm fairly sure", low → "but I can't be sure from this clip" (UX-DR11) `[ASSUMPTION: the lead line is coaching text snapshotted from rules.yaml in the result; the band phrases are UI copy from EXPERIENCE.md Voice and Tone]`
**And** for a low band one more line names what to film better from `film_better`, linking to `/guide/{guide_step}` (UX-DR11)

**Given** a result with one or more verified faults
**When** the verdict renders
**Then** it is always first, with one verdict card per verified fault ordered high → medium → low, ties in result order (UX-DR14, UX-DR48)
**And** each desktop card is split by a vertical hairline: left "Verified fault", the fault name and the confidence band; right the pin, the measurement name, the `display` value in 46px teal mono, the unit line and "rule: {fault threshold display}" in mono meta (UX-DR14)
**And** activating the pin or the value cites it through Story 4.6

**Given** a possible or absent fault
**When** the result renders
**Then** it never appears in a verdict card and is not counted as a fault (FR-9)

**Given** each verified fault
**When** its feel cue renders
**Then** exactly one feel cue shows: clay quote mark, the cue in italic Newsreader 21px, and the meta "Feel cue · check it in the impact frame [n]", whose citation points to the fault's key frame (UX-DR15, FR-14)
**And** `[ASSUMPTION]` the cue text is the fault's feel cue snapshotted from `rules.yaml` in the result

**Given** the explanation row
**When** the result renders
**Then** "Read my full explanation · n words" is collapsed by default, n is counted by the shared word-count rule, and opening it shows `explanation.text` in place with `[E<n>]` rendered as citations; the state is not kept between visits (UX-DR22, FR-14)

**Given** `explanation.source`
**When** it is `mock`
**Then** a "Mock mode" meta label (ink-2, not interactive) shows on the explanation row `[ASSUMPTION: placement]`, and the rail footer's global "Mock mode" label (driven by `/api/config` `mock_mode`, Epic 1) is also present (AR-24, FR-15)
**And** when it is `template` because the model was unavailable, the result renders complete with no error on the result itself (FR-14, UX-DR45)

**Given** a cold load
**When** the result is not there yet
**Then** the verdict, feel cue and explanation row show as dashed placeholders in their final positions, and a load failure shows "Couldn't load this. Try again." inline (UX-DR27, UX-DR45)

### Story 4.8: See why the fault happens and what to practise

As a player,
I want to see the chain from likely cause to fault, and one drill and one mobility exercise for it,
So that I know what to work on for the rest of the bucket.

**Slice:** frontend `src/modules/result/`; Vitest
**Requirements:** FR-10, FR-11, NFR-11, UX-DR3 (dashed meaning), UX-DR16, UX-DR17, UX-DR48

**Acceptance Criteria:**

**Given** each verified fault
**When** its "Why" section renders
**Then** one fault-chain card shows three links left to right joined by 18px ink-2 arrows: Likely cause (`chain-link-inferred`, dashed 5 4, labelled "Likely cause"), Mechanism (`chain-link-measured`, solid) and "Fault · verified" (`chain-link-verified`) (UX-DR16, FR-10)
**And** each link shows its label, title, its inline mono teal value with its pin, and the band, from `chain[].label`, `likely` and `evidence_ids`

**Given** a chain link
**When** it rests on several evidence items
**Then** it shows a pin for each of them (the measurement and the key frame), so every link shows the measurement, key frame and band it rests on (FR-10)
**And** a likely cause that cannot be measured shows the measured pointer it rests on (e.g. "31° [4]" with its band) and keeps the "Likely cause" label (FR-10)

**Given** the chain card
**When** it renders
**Then** the legend "Dashed = inferred from a pointer, not measured directly." sits directly under it, so the dashed meaning is also stated in words (UX-DR16, UX-DR3)

**Given** each verified fault
**When** its "Practise" section renders
**Then** one exercise card shows two halves split by a hairline: "Drill · for {fault name}" and "Mobility · for the likely cause", each with the name in clay 23px, the dose in mono and two or three lines of instruction from the result (UX-DR17, FR-11)
**And** the drill and mobility exercise are those the result maps to that fault (FR-11)

**Given** any mobility exercise
**When** it renders
**Then** it carries the undismissible medical notice "Generic guidance, not medical advice — see a physiotherapist if you feel pain." with the text taken from `rules.yaml` (through the result or `/api/config`), never typed into the component (FR-11, NFR-11, AR-28)
**And** a Vitest over every fixture asserts that no mobility exercise renders without the notice

**Given** a possible fault, an unverified observation or a "No verified fault found" result
**When** the result renders
**Then** no chain card and no exercise card appear for them (FR-11, UX-DR17)

**Given** two verified faults
**When** the result renders
**Then** each fault gets its own chain card and exercise card, in the same order as the verdict cards (UX-DR48)

### Story 4.9: See what else was checked, the unverified observation and the no-fault answer

As a player,
I want to see the other faults the coach checked, any unverified observation clearly set apart, and a plain answer when nothing is wrong,
So that I trust the result and never get a forced fault.

**Slice:** frontend `src/modules/result/`, `src/shared/ui/` (status chip variant); Vitest
**Requirements:** FR-7, FR-9, FR-12, FR-13, NFR-11, UX-DR3 ("possible" chip), UX-DR18, UX-DR20, UX-DR21

**Acceptance Criteria:**

**Given** a result with at least one verified fault
**When** the "Also checked" card renders
**Then** it shows the title, a right-aligned count, and one row for every other fault in the result: name, status chip ("possible" in the medium colour or "not found" in ink-2, text only), the band of its deciding measurement, its pin, and one ink-2 line under it (UX-DR18)
**And** the "possible" chip sits on card fill with a hairline border, not on paper-2 (UX-DR3)
**And** a reserve fault (sway) is never listed as a fault (FR-9)

**Given** a possible fault in "Also checked"
**When** its row renders
**Then** the line shows its measurement `display` against the fault threshold display and ends with "No drill." (UX-DR18, FR-9) `[ASSUMPTION: line wording; mockup: "Posture angle changed 6°, below the 9° fault line. No drill."]`

**Given** a result with an observation
**When** the observation card renders
**Then** it has a dashed ink-2 outline (5 4) on paper, the label "Unverified — confirm with a coach" exactly, `observation.text` in italic Newsreader, "confidence: low", and "No drill: this is not in my rule table." (UX-DR20, FR-13)
**And** at most one card shows, it never names a drill or mobility exercise, and with a verified fault it sits after "Also checked", never inside the verdict, chain or practice sections (FR-13)

**Given** a result with no observation
**When** it renders
**Then** no observation card shows (FR-13)

**Given** a "No verified fault found" result
**When** it renders
**Then** the coach message says "No verified fault found" plus one line, then "Checked: early extension · loss of posture · over the top" built from the result's fault labels, with possible faults labelled "possible" (UX-DR21, FR-12)
**And** no verdict card, fault chain or exercise card shows, and no fault is shown as verified (FR-12)

**Given** a "No verified fault found" result with an observation
**When** it renders
**Then** the one coach line reads "None of my three rules fired. That's a real answer, so I won't invent a drill." and the observation card follows the "Checked" line (UX-DR21)

**Given** a "No verified fault found" result without an observation
**When** it renders
**Then** the coach line reads "None of my three rules fired, and nothing else stood out that I can measure. That's a real answer." (UX-DR21)
**And** the suggested prompt "What did you check in my swing?" and the "Ask the coach about this" button are not rendered in this epic; they arrive with the chat in Epic 6

**Given** every row, card and observation
**When** it shows a measurement
**Then** a band shows with it (FR-7, NFR-11)

### Story 4.10: Jump through a long result and see where the coach chat will go

As a player,
I want chips that take me straight to the verdict, the reasons, the practice and what else was checked,
So that I can find my way through a long result, even one with two faults.

**Slice:** frontend `src/modules/result/`; Vitest
**Requirements:** UX-DR13, UX-DR45 (chat cut), UX-DR48, UX-DR49, Cross-epic hand-off (composer placeholder)

**Acceptance Criteria:**

**Given** a result with a verified fault
**When** the header renders
**Then** under it sits "Jump to" with the 34px pills Verdict · Why · Practise · Also checked, and the active pill is ink (`jump-chip-active`) (UX-DR13)
**And** "Ask the coach" is not shown in this epic; Epic 6 adds it with the working composer

**Given** a jump chip
**When** the player activates it
**Then** the thread scrolls to that section and focus moves to the section heading; with reduced motion there is no scroll animation (UX-DR13, UX-DR49)
**And** while the player scrolls, the active chip follows the section in view

**Given** two verified faults
**When** the chips render
**Then** there is one Verdict, Why and Practise entry per fault in the verdict order `[ASSUMPTION: labelled with the fault name, e.g. "Why · Loss of posture"]` (UX-DR13, UX-DR48)

**Given** a "No verified fault found" result
**When** the chips render
**Then** only chips for sections that exist show `[ASSUMPTION]`, never Why or Practise

**Given** the chips on the phone
**When** they render
**Then** each keeps its 34px look with a 44px hit area and the focus ring, in reading order (UX-DR49)

**Given** `/api/config` `chat_enabled` is true
**When** the result renders
**Then** the composer area shows only the disabled composer (`composer-disabled`) reading "You can ask the coach once the result is ready.", with no grounding note, suggested prompts or send action (Cross-epic hand-off; Epic 6 enables it)

**Given** `/api/config` `chat_enabled` is false
**When** the result renders
**Then** no composer, grounding note, suggested prompt, "Ask the coach" chip or link shows, and the rest of the result is unchanged (UX-DR45)

### Story 4.11: Read my result on the phone at the range and on a narrow laptop

As a player at the range with my phone,
I want the result to show the verdict, the value, the two frames and the feel cue first, with practice one tap away,
So that I can read it between balls without zooming or scrolling sideways.

**Slice:** frontend `src/modules/result/`, `src/shared/evidence/` (tray and drawer use); Vitest
**Requirements:** NFR-5, UX-DR4, UX-DR12 (phone), UX-DR14 (phone), UX-DR15 (phone), UX-DR17 (phone), UX-DR18 (phone), UX-DR22 (phone next step), UX-DR28, UX-DR49

**Acceptance Criteria:**

**Given** a viewport under 768px
**When** a result loads
**Then** the top bar shows ≡ or back, the title with its meta, the library status under the meta, and the Evidence chip on the right; content is one column with a 20px gutter and no horizontal scroll at 390px and 320px (UX-DR4, UX-DR12, NFR-5)

**Given** the phone verdict
**When** it renders
**Then** it is one card with the fault, the band, the value in 40px mono and the two key-frame thumbnails beside it, followed by the feel cue at 17px with the 40px quote mark (UX-DR14, UX-DR15)
**And** the coach lead uses the mobile size, and a key-frame thumbnail opens the enlarged frame sheet (Story 4.4)

**Given** the phone result
**When** the player looks below the feel cue
**Then** a "Next: what to practise · 1 drill · 1 mobility" row (card, hairline, full pill) scrolls to the exercise card, and "Also checked" follows the exercise card (UX-DR17, UX-DR18, UX-DR22)
**And** the chain card follows the practice sections and the observation card follows "Also checked" `[ASSUMPTION: phone section order]`
**And** with two verified faults the row counts every drill and mobility exercise `[ASSUMPTION]`

**Given** the phone Evidence chip "Evidence · n"
**When** the player taps it or a pin
**Then** the tray opens as a bottom sheet with the 40×5 grab handle, "Evidence · pinned live" and a horizontal row of frames and measurement cards, at the item when a pin opened it; swipe down or a scrim tap closes it (UX-DR28)

**Given** a viewport of 1024–1343px or 768–1023px
**When** a result loads
**Then** there is no Evidence panel column: the Evidence chip sits in the page header before the library status and opens the drawer (408px from the right over the scrim); at 768–1023px the rail is the ≡ menu sheet and the thread is full width up to 640px (UX-DR4, UX-DR28)

**Given** the phone layout
**When** it is checked
**Then** all touch targets are at least 44×44px, tab order follows reading order, and text scales to 200% without lost content (UX-DR49)


## Epic 5: Keep, rewatch and delete my swings

A player keeps every swing clip in a private swing library: they can browse it newest first (also from the rail's recent swings), play any clip on phone and laptop, open its analysis, delete a clip (keeping or deleting its analysis), delete an analysis from the account page, and delete the whole account with every file removed. The epic ends by proving isolation and retention (SM-9, SM-11).

### Story 5.1: Make every clip playable after its analysis

As a player,
I want every clip I send to become playable on my phone and laptop once its analysis ends,
So that I can rewatch any swing, including a rejected one, with an HEVC iPhone clip playing like any other.

**Slice:** `backend/app/modules/swings/library/` (routes, service, playback transcode registered as an after-terminal hook); `backend/app/modules/swings/repo.py`, `repo_system.py`; `backend/tests/`
**Requirements:** FR-18, FR-19, FR-2, NFR-5, AR-15, AR-18, AR-20, AR-25, AR-29, AR-31, AD-4, AD-7, AD-15, AD-21

**Acceptance Criteria:**

**Given** Epic 3 created `clips.playback_state` (default `pending`) and the worker calls hooks registered through `swings.service.register_after_terminal_hook` after every terminal write (Story 3.3)
**When** the backend starts
**Then** the library sub-slice registers its transcode as that hook, so `worker.py` itself is not edited and no second transcode path exists (AD-15, AR-20)
**And** the story adds no migration, because the column already exists (AR-30)

**Given** the worker has made the terminal write for an analysis (`result`, `rejection` or `failed`)
**When** the same worker slot continues
**Then** it runs the `ffmpeg` command line on `original.{mp4|mov}` and makes an H.264 `playback.mp4` (yuv420p, `+faststart`, upright with the rotation applied) and a `thumb.jpg` in scratch, then moves both in through FileStore to `users/{user_id}/clips/{clip_id}/` and sets `clips.playback_state=ready` (AD-4, AD-15, AR-15)
**And** the transcode time is not in `step_timings` and does not change `finished_at` (it is outside NFR-1) (AD-5)
**And** `[ASSUMPTION]` `thumb.jpg` is the frame at the address event's `t_ms` when the result has events, otherwise the first frame, scaled to 320 px wide and never cropped
**And** `[ASSUMPTION]` the transcode also runs after a `failed` terminal write, so a clip whose analysis failed can still be played (SM-11 "every uploaded clip")

**Given** `ffmpeg` exits non-zero, or hangs past `[ASSUMPTION]` 120 s and is killed
**When** the worker checks the original with `ffprobe`
**Then** if the original's video codec is `h264`, `playback_state` becomes `ready` and the video endpoint serves the original (AR-20)
**And** otherwise `playback_state` becomes `failed`, the scratch output is deleted, and one structured log line holds `clip_id`, `analysis_id` and the ffmpeg exit status, never `original_filename` or the file contents (AR-31)
**And** a transcode failure never changes the analysis `status` or `result`

**Given** the clip row (or the user) was deleted while the transcode was running
**When** the worker is about to move the outputs in
**Then** it finds no clip row, deletes the scratch outputs and writes nothing under `users/` (AD-8)

**Given** a retried analysis (`failed → queued`) reaches its terminal write again and the clip is already `ready`
**When** the worker reaches the transcode
**Then** it skips the transcode

**Given** the backend restarts while clips are `pending` and their analysis is no longer `queued` or `running` (or they have no analysis)
**When** the startup hook has run the orphan sweep and failed the `running` rows
**Then** `[ASSUMPTION]` the worker transcodes those clips before it claims new jobs, using a cross-user function in `repo_system.py` (for example `list_pending_playback`) that only `worker.py` and the startup hook import (AD-7, AR-18)

**Given** a signed-in player owns a clip with `playback_state=ready`
**When** the browser requests `GET /api/clips/{id}/video` with the session cookie and no Range header
**Then** the response is `200` with the whole `playback.mp4`, `Content-Type: video/mp4` and `Accept-Ranges: bytes` (AD-21)
**And** with `Range: bytes=0-1`, `bytes=1000-` or `bytes=-500` the response is `206` with the right `Content-Range`, `Content-Length` and bytes, which is what iOS Safari needs (AR-20)
**And** an unsatisfiable range returns `416` with `Content-Range: bytes */<size>`
**And** when the original is served (H.264 fallback), its `Content-Type` is `video/mp4` for mp4 and `video/quicktime` for mov

**Given** a clip exists but its `playback_state` is `pending`
**When** `GET /api/clips/{id}/video` or `GET /api/clips/{id}/thumb` is called
**Then** the response is `409 playback_not_ready` in the error envelope, never 404 (AD-15, AD-21)
**And** for `playback_state=failed` with no H.264 original, the response is `409 playback_unavailable`
**And** `GET /api/clips/{id}/thumb` returns `200 image/jpeg` when `thumb.jpg` exists, and `409 playback_unavailable` when the clip is `ready` but has no thumbnail `[ASSUMPTION]`

**Given** a clip ID that does not exist or belongs to another player
**When** either media endpoint is called
**Then** the response is `404 not_found` and no bytes are sent. Without a session cookie the response is `401` (FR-2, AD-7)
**And** pytest API tests on httpx AsyncClient cover: full and ranged reads, 416, both 409 codes, the H.264 fallback, 404 for another player's clip, and 401. Tests use small clips that an `ffmpeg testsrc` fixture makes (H.264 mp4 and HEVC mov), never `samples/` (AR-32)

### Story 5.2: Browse my swing library

As a player,
I want to see all my swing clips newest first, with date and main finding,
So that I can find any swing I have sent, including rejected ones and analyses whose clip I deleted.

**Slice:** `backend/app/modules/swings/library/` (routes, service, schemas); `backend/app/modules/swings/repo.py`; `frontend/src/modules/library/` (library page, list rows); `frontend/src/app/library/page.tsx` (route); `frontend/openapi.json` + `src/shared/api/schema.d.ts` (regenerated); `backend/tests/`, frontend Vitest
**Requirements:** FR-19, FR-18, FR-2, NFR-12, AR-25, AR-29, AD-9, AD-8, AD-21, AD-22, UX-DR38, UX-DR45, UX-DR49, UX-DR50

**Acceptance Criteria:**

**Given** a signed-in player
**When** the frontend calls `GET /api/clips`
**Then** the response is `{rows: [LibraryRow], count, limit}`, and `LibraryRow = {row_id, clip_id|null, analysis_id|null, created_at, state, main_finding_label|null, band|null, playback_state|null, thumbnail_url|null}` is a typed Pydantic response model (no `dict`/`Any`) exported to `frontend/openapi.json` (AD-9, AD-21, AR-25)
**And** rows are newest first by `created_at` (UTC ISO 8601 with `Z`), with `row_id` as the tie-break `[ASSUMPTION]` (AR-29)
**And** `limit` equals `MAX_CLIPS_PER_PLAYER` (50) from settings (AR-24)
**And** this story adds no migration (AR-30)

**Given** the player's clips and analyses in every combination
**When** the server builds the rows
**Then** `state` is worked out only on the server (AD-9):
- a clip whose analysis is `queued` or `running` → `analysing`
- a clip whose analysis is `result` → `result`
- `rejection` → `rejection`
- `failed` → `failed`
- an analysis with `clip_id` NULL → `clip_deleted`, with `row_id` = the analysis ID and `clip_id` null
- a clip with no analysis → `analysis_deleted`
**And** `main_finding_label` and `band` come from the stored `AnalysisResult` snapshot: the main-finding fault's label and band for `result`, "No verified fault found" with band null for `no_fault`, "Cannot analyse" for a rejection, null for `analysing`, `failed` and `analysis_deleted`. A `clip_deleted` row carries its analysis's finding (FR-12, FR-8, AD-9)
**And** `thumbnail_url` is `/api/clips/{clip_id}/thumb` only when the clip exists and `thumb.jpg` exists. Otherwise it is null
**And** a stored result with an old `schema_version` gives `state` from the status with `main_finding_label` null, and does not fail the list `[ASSUMPTION]`

**Given** a player with 3 clip rows and 1 `clip_deleted` row
**When** `GET /api/clips` is called
**Then** `rows` has 4 entries and `count` is 3, because `clip_deleted` rows don't count toward the limit (FR-19, NFR-12, AD-8)
**And** a pytest test asserts that `count` equals the `clips` row count that the upload limit check uses

**Given** two players with clips
**When** player A calls `GET /api/clips`
**Then** only A's rows come back, through `repo.py` functions that take `user_id`. Without a session cookie the response is `401` (FR-2, AD-7)

**Given** a signed-in player opens `/library` from the rail, the menu or a link
**When** the page loads
**Then** dashed placeholders in the final layout stand in for the rows, with no spinner. A load failure shows the inline "Couldn't load this. Try again." (UX-DR45)
**And** each row is one list-row target (card, chevron): a 46px thumbnail, the local date (for example "11 Nov 2026"), and the finding meta "Early extension" with the shared confidence band showing "confidence: high" (UX-DR38, UX-DR19)

**Given** rows in each state
**When** they render
**Then**:
- `result` shows the thumbnail and finding with band
- `rejection` shows a dashed "no thumbnail" tile and "Cannot analyse"
- `analysing` shows "Analysing…"
- `failed` shows "Not analysed"
- `analysis_deleted` shows "Analysis deleted"
- `clip_deleted` shows a dashed thumbnail, "date · main finding", the meta "clip deleted" and no play control
- a row with `playback_state=pending` shows a dashed "Preparing playback…" poster tile instead of the thumbnail
(UX-DR38)
**And** the frontend maps `state` and `playback_state` straight to this copy and never works out a state or finding itself (AD-9). A Vitest test covers all six states plus the pending poster

**Given** a row with a clip
**When** the player activates it
**Then** the clip detail opens at `/library/{clip_id}` (UJ-6). A `clip_deleted` row opens its analysis at `/swing/{analysis_id}` (UX-DR38)

**Given** the list contains an `analysing` row or a `pending` playback
**When** the page stays open
**Then** `[ASSUMPTION]` it refetches `GET /api/clips` about every 2 s until no row is `analysing` or `pending`

**Given** a player with no clips and no analyses
**When** `/library` loads
**Then** the page shows "No swings yet. Every clip you send lands here." and a "New swing" button to `/swing/new` (UX-DR38)
**And** the page never shows a save control or the word "Saved" (UX-DR50), every row has the visible focus ring, and the page reads at 200 % text size without horizontal scroll on a phone (UX-DR49, NFR-5)

### Story 5.3: See my recent swings in the rail

As a player,
I want my latest swings in the rail (or the phone menu), with an "Analysing…" line while one is running,
So that I can jump back to any recent thread without opening the library.

**Slice:** `frontend/src/modules/library/` (recent-swings component, exported from `index.ts`); `frontend/src/app/` signed-in layout (composes it into the Epic 1 rail and menu-sheet slot); frontend Vitest
**Requirements:** UX-DR5 (rail part), UX-DR7 (rail row "Analysing…"), FR-19, AD-2, AD-9, AD-22, UX-DR49

**Acceptance Criteria:**

**Given** the Epic 1 shell has a recent-swings slot in the rail and the ≡ menu sheet
**When** a signed-in page renders
**Then** the route layer in `frontend/src/app/` passes `RecentSwings` from `src/modules/library/index.ts` into that slot, and `src/shared/layout/` imports nothing from `src/modules/` (Code Organisation rule 2; checked by the ESLint boundary rule in the test suite)

**Given** the player has rows with an `analysis_id`
**When** the rail renders
**Then** it shows a "Swings" heading and the latest `[ASSUMPTION]` 5 rows from `GET /api/clips` (the same query key as the library). Each row has a 38px thumbnail, the local date as title (`[ASSUMPTION]` "today" / "11 Nov", since no club is recorded) and the finding meta (for example "Early extension · high") (UX-DR5)
**And** a `rejection` row shows a dashed paper tile (dash 3 3) with × and "Cannot analyse". An `analysing` row shows "Analysing…". A `failed` row shows "Not analysed" (UX-DR5, UX-DR7, UX-DR3)
**And** `[ASSUMPTION]` rows without an `analysis_id` (`analysis_deleted`) are left out, because the rail lists threads

**Given** a rail row
**When** the player activates it
**Then** it opens `/swing/{analysis_id}`. On the phone the menu sheet closes (UX-DR5)
**And** the row for the thread currently open is highlighted (on card, hairline border) and has `aria-current="page"` (UX-DR5)

**Given** the player sends a new clip and lands on its thread
**When** the pathname changes
**Then** the rail refetches, and the new row shows "Analysing…"
**And** `[ASSUMPTION]` while any listed row is `analysing`, the rail polls about every 2 s, and stops when none is left

**Given** a player with no swings (first visit)
**When** the rail renders
**Then** there is no "Swings" heading and no rows, and "New swing" is the only action (UX-DR5)

**Given** the player has at least one thread
**When** they activate the wordmark
**Then** `[ASSUMPTION]` it opens the newest row's `/swing/{analysis_id}`. With no thread it opens `/swing/new` (UX-DR5)
**And** Vitest covers the empty rail, the row cap, the active highlight, the "Analysing…" and "Cannot analyse" rows, and the wordmark target

### Story 5.4: Rewatch a swing clip

As a player,
I want to open a clip from my library and play it with normal video controls,
So that I can watch the swing again and jump to its analysis.

**Slice:** `backend/app/modules/swings/library/` (`GET /api/clips/{id}`); `frontend/src/modules/library/` (clip detail); `frontend/src/app/library/[clipId]/page.tsx` (route); regenerated API types; `backend/tests/`, frontend Vitest
**Requirements:** FR-19, FR-2, NFR-5, AR-20, AR-25, AD-7, AD-15, AD-22, UX-DR39, UX-DR45, UX-DR49, UX-DR50

**Acceptance Criteria:**

**Given** a signed-in player owns a clip
**When** the frontend calls `GET /api/clips/{id}`
**Then** `[ASSUMPTION]` the response is that clip's `LibraryRow` (the same model as the list, `state` worked out on the server) (AD-9, AR-25)
**And** another player's clip ID, an unknown ID, or the ID of an analysis whose clip was deleted returns `404 not_found`. Without a session cookie the response is `401` (FR-2, AD-7)
**And** this story adds no migration (AR-30)

**Given** the player opens `/library/{clipId}` for a clip with `playback_state=ready`
**When** the page loads (dashed placeholders while loading, no spinner, UX-DR45)
**Then** the page header shows the local date and the finding meta, as in the library row (UX-DR39)
**And** the clip plays in a `{rounded.md}` video frame on keyframe ground, using `<video controls playsInline preload="metadata">` with `src="/api/clips/{id}/video"` and the thumbnail as poster. There is no `autoplay` (UX-DR39, UX-DR49, UX-DR50)
**And** playback works through the cookie-authenticated, Range-capable endpoint from Story 5.1 on phone Safari/Chrome and desktop browsers (NFR-5, AR-20)
**And** "Open analysis" (primary) goes to `/swing/{analysis_id}` (UX-DR39)

**Given** the clip's `playback_state` is `pending`
**When** the page shows
**Then** a dashed poster tile reads "Preparing playback…" with no play control, and the page polls `GET /api/clips/{id}` about once a second until the state is `ready` or `failed`, then swaps in the video in place (UX-DR39, AD-15)
**And** "Open analysis" works while playback is being prepared

**Given** `playback_state` is `failed`
**When** the page shows
**Then** in place of the video it shows "This clip can't be played back.", and "Open analysis" still works (UX-DR39)

**Given** the browser fails to play the file (the video element's `error` event)
**When** the error fires
**Then** the frame is replaced with "This clip can't play in this browser.", and "Open analysis" still works (UX-DR39)

**Given** the clip's row state is `analysis_deleted`
**When** the page shows
**Then** the header meta reads "Analysis deleted", and `[ASSUMPTION]` "Open analysis" is not shown

**Given** the URL holds another player's clip ID or an unknown ID
**When** the page loads
**Then** it shows "This analysis doesn't exist or isn't yours." with a link to the swings, using the Epic 1 not-found pattern (FR-2, UX-DR45)

**Given** a result header links "In your swing library ›" to `/library/{clipId}` (Epic 4)
**When** the player follows it
**Then** this clip detail page opens (UX-DR12)
**And** Vitest covers the ready, pending (polling stops at ready), failed, browser-error and analysis-deleted states

### Story 5.5: Delete a clip, keeping or deleting its analysis

As a player,
I want to delete a swing clip and choose whether its analysis stays,
So that I can clear out bad clips and free library space without losing results I want.

**Slice:** `backend/app/modules/swings/library/` (`DELETE /api/clips/{id}?keep_analysis=`, service); `backend/app/modules/swings/repo.py`; orphan sweep check in `swings` (Epic 3 startup hook, only extended if needed); `frontend/src/modules/library/` (delete-clip sheet, trash on rows, "Delete clip" on clip detail); `backend/tests/` (incl. `-m pg`), frontend Vitest
**Requirements:** FR-19, FR-2, NFR-12, AR-19, AR-15, AR-29, AD-8, AD-4, AD-7, UX-DR41, UX-DR42, UX-DR38, UX-DR39, UX-DR43, UX-DR49

**Acceptance Criteria:**

**Given** a player's clip whose analysis is `result`, `rejection` or `failed`
**When** they send `DELETE /api/clips/{id}?keep_analysis=true` with `X-Requested-With: aicoach`
**Then** in one transaction the `clips` row is deleted and `analyses.clip_id` becomes NULL through the FK `ON DELETE SET NULL`. After commit, `original.*`, `playback.mp4` and `thumb.jpg` are removed with the `users/{user_id}/clips/{clip_id}/` folder, and the response is `204` `[ASSUMPTION]` (AD-8, AR-19)
**And** `GET /api/clips` then shows that analysis as a `clip_deleted` row, and `count` has gone down by one (FR-19, NFR-12)

**Given** the same clip
**When** the player sends `DELETE /api/clips/{id}?keep_analysis=false`
**Then** both the `clips` and the `analyses` rows are deleted in one transaction. Chat rows cascade through the FK that the chat table declares (AD-2). After commit, the clip folder and `users/{user_id}/analyses/{analysis_id}/` (key frames) are removed, and the row leaves the library (AD-8)

**Given** a clip with no analysis (`analysis_deleted`)
**When** the player deletes it with either value of `keep_analysis`
**Then** the clip row and its files are removed (AD-8)

**Given** the clip's analysis is `queued` or `running`
**When** either delete is called
**Then** the response is `409 analysis_in_progress`, and no row or file changes (AD-8, AR-19)
**And** a `pytest -m pg` test shows that a delete racing the worker's claim either succeeds before the claim, or gets 409 and leaves the job intact

**Given** `keep_analysis` is missing or not a boolean
**When** the request arrives
**Then** `[ASSUMPTION]` the response is `422` in the error envelope, and nothing is deleted (AD-21)

**Given** another player's clip ID
**When** either delete is called
**Then** the response is `404 not_found`, and that player's rows and files are untouched (FR-2, AD-7)

**Given** the database commit succeeds but a file delete fails (for example a locked file on Windows, simulated by a FileStore that raises)
**When** the request finishes
**Then** the response is still `204`, and one log line holds the `clip_id` (no file names) (AR-31)
**And** the next startup orphan sweep removes the left-over folder, because it walks `users/` and deletes clip and analysis folders that have no row (AD-8, AR-15). A pytest test proves this; if the Epic 3 sweep does not yet cover clip or analysis folders without a row, this story extends it

**Given** a player at 50 clips
**When** they delete one clip with `keep_analysis=true` and then upload
**Then** the upload is accepted, because the `clip_deleted` row doesn't count (FR-19, NFR-12, AD-8)

**Given** the swing library or the clip detail
**When** the player activates a row's trash icon or "Delete clip" (secondary)
**Then** a bottom sheet opens with the title "Delete this clip?" and two full-width stacked actions: "Delete clip, keep analysis" and "Delete clip and analysis" (`[ASSUMPTION]` both dark, as destructive confirmations). Focus moves into the sheet and returns on close. Esc, swipe down or a scrim tap closes it, except while the delete is running (UX-DR41, UX-DR42, UX-DR43)
**And** `[ASSUMPTION]` for a clip with no analysis, the sheet shows one action, "Delete clip"
**And** only one sheet level opens, never stacked (UX-DR42)

**Given** the delete succeeds
**When** the sheet closes
**Then** the `GET /api/clips` query is invalidated, so the library row turns into a "clip deleted" row (keep) or disappears (both), and the rail updates. From the clip detail, `[ASSUMPTION]` the player goes to `/library` (UX-DR41)

**Given** the delete fails (network error, 5xx or `409 analysis_in_progress`)
**When** the response arrives
**Then** the sheet stays open with the inline "Couldn't delete. Nothing was removed. Try again.", and the actions can be tried again (UX-DR41, UX-DR46)

**Given** a row or clip whose state is `analysing`
**When** it renders
**Then** the trash icon and "Delete clip" are disabled (`aria-disabled`, still focusable) with the meta "You can delete this once the analysis has finished." linked by `aria-describedby` (UX-DR41, UX-DR49)
**And** Vitest covers the sheet's actions, the disabled state, the failure message and the closing rules

### Story 5.6: Delete an analysis from my account or library

As a player,
I want to see my analyses on the account page and delete any of them,
So that I can remove a result I don't want while its swing clip stays in my library.

**Slice:** `backend/app/modules/swings/library/` (`GET /api/analyses`, `DELETE /api/analyses/{id}`, service, schemas); `backend/app/modules/swings/repo.py`; `frontend/src/modules/account/` ("Your analyses" list); `frontend/src/shared/ui/` (delete-analysis sheet, used by account and library, Code Organisation rule 3); `frontend/src/modules/library/` (trash on `clip_deleted` rows); `backend/tests/`, frontend Vitest
**Requirements:** FR-3, FR-2, FR-19, AR-19, AR-24, AR-25, AD-8, AD-7, AD-23, UX-DR40, UX-DR41, UX-DR42, UX-DR38, UX-DR49

**Acceptance Criteria:**

**Given** a signed-in player
**When** the frontend calls `GET /api/analyses`
**Then** the response lists only that player's analyses, newest first, as `[ASSUMPTION]` `{rows: [{analysis_id, clip_id|null, created_at, status, main_finding_label|null, band|null}]}`, a typed response model with the finding worked out on the server as in `LibraryRow` (AR-25, AD-9)
**And** the endpoint is P1 and is not gated by `FEATURE_HISTORY` (it answers with that flag false) (AR-24, AD-23)
**And** without a session cookie the response is `401`. This story adds no migration (AR-30)

**Given** a player's analysis in `result`, `rejection` or `failed`
**When** they send `DELETE /api/analyses/{id}` with `X-Requested-With: aicoach`
**Then** the `analyses` row is deleted (chat rows cascade through the FK the chat table declares), the clip row stays, and after commit `users/{user_id}/analyses/{analysis_id}/` (key frames) is removed. The response is `204` `[ASSUMPTION]` (FR-3, AD-8)
**And** afterwards `GET /api/analyses/{id}` and its key frames return `404 not_found`, its clip shows in `GET /api/clips` as `analysis_deleted`, and an analysis with no clip leaves the library completely (FR-3, FR-19)

**Given** the analysis is `queued` or `running`
**When** `DELETE /api/analyses/{id}` is called
**Then** the response is `409 analysis_in_progress`, and nothing changes (AD-8)

**Given** another player's analysis ID
**When** `DELETE /api/analyses/{id}` is called
**Then** the response is `404 not_found`, and that player's row and key frames are untouched (FR-2, AD-7)
**And** a failed key-frame delete after commit is logged and left for the startup sweep, as in Story 5.5 (AD-8)

**Given** the player opens `/account`
**When** the page loads (dashed placeholders, no spinner)
**Then** under the email, a "Your analyses" section lists one row per analysis: "date · main finding" ("Cannot analyse" for a rejection, "Not analysed" for failed, "Analysing…" while queued or running), a meta line "clip in swing library" or "clip deleted", and an ink-2 trash icon (UX-DR40)
**And** `[ASSUMPTION]` account rows are not links (no chevron, as DESIGN.md draws them)
**And** "See all n analyses" is not rendered (hidden until FR-16) (UX-DR40)
**And** sign out and "Delete account" (secondary) from Epic 1 stay on the page

**Given** a player with no analyses
**When** `/account` loads
**Then** "No analyses yet." shows under "Your analyses", and sign out and "Delete account" still show (UX-DR40)

**Given** an account row's trash icon, or the trash icon on a library `clip_deleted` row
**When** the player activates it
**Then** a bottom sheet opens with "Delete this analysis? Its result and key frames are removed. The swing clip stays in your swing library.", a dark confirm action and a way to cancel, with the Epic 1 sheet's focus and closing behaviour (UX-DR41, UX-DR42, UX-DR38)
**And** this sheet lives in `frontend/src/shared/ui/`, because two slices use it, and imports only `shared/` code (Code Organisation rule 3)

**Given** the delete succeeds
**When** the sheet closes
**Then** the account row disappears, and the `GET /api/analyses`, `GET /api/clips` and `GET /api/me` queries are invalidated, so the library row turns into "Analysis deleted" or disappears and the rail updates (UX-DR41)

**Given** the delete fails (network error, 5xx or 409)
**When** the response arrives
**Then** the sheet stays open with "Couldn't delete. Nothing was removed. Try again." (UX-DR41)

**Given** an analysis that is waiting or running
**When** its account row renders
**Then** the trash icon is disabled with the meta "You can delete this once the analysis has finished." (UX-DR41, UX-DR49)
**And** Vitest covers the account list states, the empty state, the disabled trash and the sheet's success and failure

### Story 5.7: Delete my account and every file with it

As a player,
I want the delete-account sheet to tell me exactly what will be removed, and then to remove all of it,
So that when I stop using AIcoach none of my swings, results or key frames remain.

**Slice:** `backend/app/modules/identity/` (`GET /api/me` counts via the swings public service); `backend/app/modules/swings/library/service.py` (count function, exposed through `swings/service.py`); `frontend/src/modules/account/` (delete-account sheet counts); `backend/tests/` (incl. `-m pg`), frontend Vitest
**Requirements:** FR-3, FR-18, NFR-12, AR-19, AR-14, AR-25, AD-2, AD-8, AD-6, UX-DR40, UX-DR41, UX-DR42

**Acceptance Criteria:**

**Given** a signed-in player with analyses and clips
**When** the frontend calls `GET /api/me`
**Then** the response holds `email`, `analyses_count` (the number of `analyses` rows) and `clips_count` (the number of `clips` rows, so `clip_deleted` analyses don't count). `identity` reads both through a `swings` public service function and never queries `swings` tables (AR-25, AD-2, AR-14)
**And** this replaces any placeholder counts from Epic 1. This story adds no migration (AR-30)

**Given** the player activates "Delete account"
**When** the sheet opens
**Then** it reads "Delete your account? This removes {analyses_count} analyses with their results and key frames, and {clips_count} swing clips. It cannot be undone, and you will not be able to sign in again.", with a dark "Delete everything" and "Keep my account" (UX-DR41)
**And** `[ASSUMPTION]` the counts read "1 analysis" and "1 swing clip" when the count is 1
**And** "Delete account" is never disabled, even while an analysis is waiting or running (AD-8, UX-DR41)

**Given** the player confirms "Delete everything"
**When** `DELETE /api/me` succeeds
**Then** the `users` row is deleted, `clips` and `analyses` (and chat) cascade, and after commit `swings.service.purge_user_files` removes `DATA_DIR/users/{user_id}/` (AD-2, AD-8)
**And** the player is signed out to the landing page. Signing in with the old email fails with "That email and password don't match.", and the old cookie gets `401 session_invalid` (FR-3, AD-7)
**And** if the delete fails, the sheet stays open with "Couldn't delete. Nothing was removed. Try again.", and it can't be closed while the delete is running (UX-DR41, UX-DR42)

**Given** the player has an analysis `running` in the worker
**When** they delete the account
**Then** the delete succeeds at once. The worker's conditional terminal write matches 0 rows, so it deletes everything it imported, and its transcode step finds no clip and writes nothing (AD-6, AD-8, Story 5.1)
**And** a `pytest -m pg` test shows that `DATA_DIR/users/{user_id}/` and `DATA_DIR/tmp/{analysis_id}/` do not exist once the worker has finished

**Given** `purge_user_files` fails on a locked file
**When** the account delete returns
**Then** the account is still gone, and the next startup sweep removes the left-over `users/{user_id}/` folder, because it has no `users` row (AD-8, AR-15). A pytest test proves this
**And** Vitest covers the sheet copy with the counts and the failure state

### Story 5.8: Prove my swings stay private and are kept until I delete them

As a player,
I want proof that nobody else can reach my swings and that nothing is lost or left behind,
So that I can trust the swing library with every clip I send.

**Slice:** `backend/tests/` (isolation suite, retention suite, repo hygiene check); no production code unless a test exposes a gap in this epic's endpoints
**Requirements:** FR-2, FR-18, FR-19, FR-3, NFR-8, NFR-12, SM-9, SM-11, AR-18, AR-32, AR-36, AD-7

**Acceptance Criteria:**

**Given** two players A and B, each with a clip (result), a rejection, a `clip_deleted` analysis and a clip whose analysis was deleted
**When** a parametrised pytest isolation suite has A call every ID-taking endpoint with B's IDs: `GET /api/clips/{id}`, `/video`, `/thumb`, `DELETE /api/clips/{id}?keep_analysis=true|false`, `GET /api/analyses/{id}`, `GET /api/analyses/{id}/keyframes/{event}`, `POST /api/analyses/{id}/retry`, `DELETE /api/analyses/{id}`
**Then** every call returns `404 not_found` with no data in the body, and B's rows and files are unchanged afterwards (FR-2, SM-9, AD-7)
**And** `GET /api/clips`, `GET /api/analyses` and `GET /api/me` for A contain none of B's IDs or counts
**And** the suite gets its endpoint list from the app's route table and fails if a route under `/api/clips` or `/api/analyses` with an `{id}` is missing from it, so a new endpoint can't skip the check (SM-9)
**And** every endpoint in the list returns `401` without a session cookie (AR-18)

**Given** a player who signed up with the library consent
**When** a pytest retention test uploads a valid clip and a clip that ends as a rejection, signs out, signs in again and calls `GET /api/clips` and `GET /api/clips/{id}/video` for both
**Then** both rows are listed (`result` and `rejection`), and both videos return `200`/`206` (FR-18, SM-11, NFR-12)
**And** the test makes its clips with an `ffmpeg testsrc` fixture and uses a stub engine to force the result and rejection outcomes `[ASSUMPTION]`, so it does not depend on Epic 8's `samples/`

**Given** the same player deletes one of the clips (either choice)
**When** the test checks the disk
**Then** no file under `DATA_DIR/users/{user_id}/clips/{clip_id}/` exists (FR-19, SM-11)

**Given** a sign-up request without `consent: true` or with an outdated `consent_version`
**When** it is posted
**Then** it is refused, no `users` row exists for that email, and nothing is created under `DATA_DIR/users/` (FR-1, FR-18, SM-11)

**Given** the repository
**When** a pytest repo-hygiene check runs (skipped if `git` is not available)
**Then** `git ls-files "*.mp4" "*.mov"` lists only paths under `samples/` (NFR-8, AR-36)
**And** `git check-ignore` confirms that `data/users/x/clips/y/original.mp4` and `.env` are ignored (NFR-8)
**And** the test settings' `DATA_DIR` is a temporary folder outside the repository, so no test ever writes a clip into the working tree (NFR-8, AD-4)


## Epic 6: Ask the coach about my result (P2)

A player can ask the coach short questions about one result and get grounded, cited answers that light the evidence pins, end with a "Based on:" note, and refuse anything the analysis cannot answer. The chat is stored with its analysis, works with fixed sample answers in mock mode, and can be off in three distinct ways (cut, wrong status, model down). The language model and its cost are chosen at epic start (OQ2). Cut rule: if chat is not done by 2026-12-08, `FEATURE_CHAT=false` ships, so every story leaves the app shippable with the flag off.

### Story 6.1: Choose the coach model and log the cost of every call

As the author,
I want to pick the OpenRouter model for the coach and see what each analysis and each chat question costs,
So that real model use has a known, small cost while mock mode stays the free default (OQ2).

**Slice:** `backend/app/modules/coach/` (`llm.py` cost logging only), `.env.example`, architecture decision record next to `ARCHITECTURE-SPINE.md`
**Requirements:** NFR-10, AR-26 (model choice, cost per call), AR-35 (OQ2 checkpoint), AR-24 (`LLM_*` settings, mock default), AR-31

**Acceptance Criteria:**

**Given** a checked-out repo with `.env` copied from `.env.example`
**When** I read `.env.example`
**Then** `OPENROUTER_MODEL` has the chosen model ID as its default, with a one-line comment naming the decision record
**And** `LLM_MODE=auto`, `OPENROUTER_API_KEY` is empty, `LLM_TIMEOUT_SECONDS=20` and `AI_USD_NOK=10.5`, so a fresh start is in mock mode and `GET /api/config` returns `mock_mode: true` (AR-4, AR-24, FR-15)
**And** a pytest test starts the settings from `.env.example` values and asserts mock mode with no error about a missing key (AD-23)

**Given** the candidate models were tried with a key against Epic 4's SM-7 fixed analysis inputs (explanation) and a structured-output smoke call shaped like the chat answer (`kind`, `refusal_class`, `text`, `based_on`)
**When** the author records the decision
**Then** a short decision record states the chosen model, why (structured output works, SM-7 passes, median latency under `LLM_TIMEOUT_SECONDS`), the measured cost per analysis (median of the SM-7 fixtures, USD and NOK) and an estimated cost per chat question (CoachFacts + question + 80-word answer tokens × the model's prices), and it resolves the spine's Deferred row "Language model and cost (OQ2)" (NFR-10, AR-35)
**And** if no key is available by the P2 start, the record says "mock only for the MVP" and `OPENROUTER_MODEL` stays empty without breaking start-up `[ASSUMPTION]`

**Given** any call through `CoachLLM` (explain now, answer once it exists)
**When** the call returns or fails
**Then** exactly one structured stdout line is logged with `analysis_id`, `kind` (`explanation` | `observation` | `chat`), `adapter` (`openrouter` | `mock`), `model`, `input_tokens`, `output_tokens`, `cost_usd` and `cost_nok` (= `cost_usd × AI_USD_NOK`) (AD-18, NFR-10, AR-31)
**And** `cost_usd` comes from OpenRouter's reported usage cost when the adapter can read it, otherwise from the token counts × the model's per-token prices recorded with the decision `[ASSUMPTION]`
**And** Mock adapter calls log the same line with zero tokens and `cost_usd=0`, so mock mode shows zero running cost (NFR-10) `[ASSUMPTION]`
**And** the line never contains prompt text, question text, answer text, email or file paths (AR-31) — proved by a pytest `caplog` test with a fake adapter that asserts the fields and the absence of the input strings

**Given** `FEATURE_CHAT=false`
**When** the app starts after this story
**Then** it runs exactly as before; this story adds no endpoint and no table (cut rule, AR-35)

### Story 6.2: Ground chat answers and give fixed mock answers

As a player,
I want every coach answer about my result to be checked against my analysis, with fixed sample answers when no model is configured,
So that the coach never invents faults, numbers, drills or confidence, even in mock mode.

**Slice:** `backend/app/modules/coach/` (`grounding.py` `chat` kind, `llm.py` Mock `answer`, `facts.py` chat fields), `config/rules.yaml` (`coach` section: mock answers, refusal texts), `backend/engine/aicoach_engine/` (rules schema only, if the `coach` section needs new keys), `backend/tests/coach/`
**Requirements:** FR-20, FR-15 (mock chat), NFR-9, AR-26, AR-27, AR-12, UX-DR47, SM-13 (mock mode)

**Acceptance Criteria:**

**Given** a stored `AnalysisResult`
**When** `CoachFacts` is built for chat
**Then** it holds only analysis data: verified/possible/absent faults with outcome and band, measurements as `label` + `display` + band + evidence ID, key-frame labels (which event each frame shows, never the image), cause, drill and mobility texts, the observation (`band: low`) and the explanation text (PRD §4.9, AD-9)
**And** a pytest test serialises the chat input (facts + history + question) and asserts it contains no email, user ID, clip ID, `original_filename`, file path, key-frame URL or image bytes (NFR-9, AD-18)

**Given** `grounding_check(output, facts, kind="chat")` and a fixed set of hand-written good and bad answers per rule (pytest, fixed inputs)
**When** each answer is checked
**Then** it fails when the answer names a fault, cause, drill or mobility exercise from the rule table that is not in `facts` (the observation's own measurement label excepted) (FR-20, AD-19)
**And** it fails when a possible or absent fault is named without its outcome word ("possible", "not found"), or when a possible fault or the observation is called "verified" (FR-20)
**And** it fails when a drill or mobility exercise is offered in the same sentence as a possible fault or the observation (FR-20, AD-19)
**And** it fails when a number appears that is not a `display` value or a number inside the drill/exercise text in `facts`; `[E<n>]` citations are not counted as numbers (AD-19)
**And** it fails when a measurement number is not followed in the same sentence by an `[E<n>]` citation of the evidence item that carries that `display` value (FR-20 "each number is cited") `[ASSUMPTION: same-sentence rule; drill doses need no citation]`
**And** it fails when a band word next to a fault does not match that fault's band, i.e. the answer raises (or lowers) a band (FR-20, AD-19)
**And** it fails when `text` has more than 80 words (limit read from `rules.yaml` `coach`), contains a jargon-blocklist term, cites an `[E<n>]` that does not exist, or lists a `based_on` evidence ID that does not exist (AR-27, AR-12)
**And** it fails when `based_on` is empty, so every answer can end with a "Based on:" note (FR-20)

**Given** the Mock adapter
**When** `CoachLLM.answer(facts, history, question)` is called
**Then** it returns `{kind, refusal_class, text, based_on}` built only from `CoachFacts` and the `rules.yaml` mock texts, with no network access (FR-15, AD-18)
**And** it classifies the question by keyword lists stored with the mock answers in `rules.yaml`, in this order: `pain`, `competition`, `other_swings`, `not_measured`, then an on-topic answer if the question uses analysis vocabulary, else `off_topic` `[ASSUMPTION: keyword matching; keys added to the coach schema if Epic 2's lacks them]`
**And** the on-topic sample answer fills its template from facts: for a verified fault it names the fault, its band word and the deciding measurement's `display` with its `[E<n>]`, and the drill; for "No verified fault found" it lists what was checked with outcome words (FR-12, FR-20)
**And** refusals use the `rules.yaml` refusal texts, one sentence plus one next step: not measured "I didn't measure your grip in this clip, so I can't tell you." pattern + the current drill or "ask a coach"; other swings "I can only see this swing." + pointer to the swing library; competition "AIcoach is a practice tool, not for use during a round."; off topic "I can only talk about this swing."; pain = the medical notice only (UX-DR47, FR-20)
**And** a question asking for a drill for the observation or a possible fault gets "I have no drill I can stand behind. A coach can check it in person." with `refusal_class: not_measured` and `based_on` naming the observation and the rule table `[ASSUMPTION: AD-18 has no separate class for "outside the rule table"]`

**Given** every mock answer, refusal text and fixed fallback refusal in `rules.yaml`
**When** the template test runs each one through `grounding_check(kind="chat")` against each fixed analysis fixture (verified early extension high; no verified fault with the sway observation; verified fault medium with one possible fault)
**Then** all pass, so a mock answer can never fail at runtime (AD-19)

**Given** the SM-13 fixed question set — on-topic ("Why does it feel like I'm staying down when I'm not?"), not measured ("Should I change my grip as well?"), other swings ("Is this better than last week?"), pain ("My lower back hurts after the wall drill. What should I do?"), off topic ("What driver should I buy?"), competition ("Can I use this during my club championship round?"), observation drill ("Can you give me a drill for the hip movement?")
**When** `pytest tests/coach/test_chat_sm13.py` runs in mock mode against the three fixtures
**Then** on-topic gets `kind: answer`; each other question gets `kind: refusal` with the expected `refusal_class`; the pain answer's text equals the medical notice; every output passes `grounding_check(kind="chat")` and is ≤80 words (SM-13, FR-20)

**Given** `FEATURE_CHAT=false`
**When** the app runs after this story
**Then** nothing changes for the player; no endpoint or table exists yet (cut rule)

### Story 6.3: Answer with the real model, retry once, and refuse safely

As a player,
I want the coach to answer my question with the real model when one is configured, and to fall back to a safe refusal when an answer fails the check,
So that I get useful answers without ever getting an ungrounded one.

**Slice:** `backend/app/modules/coach/` (`llm.py` OpenRouter `answer`), `backend/app/modules/coach/chat/` (`service.py` answer policy, no routes yet), `config/rules.yaml` (fixed fallback refusal), `backend/tests/coach/`
**Requirements:** FR-20, NFR-9, NFR-10, AR-26, AR-27, SM-13 (real-model mode)

**Acceptance Criteria:**

**Given** `OPENROUTER_API_KEY` is set and `LLM_MODE=auto`
**When** `CoachLLM.answer(facts, history, question)` is called on the OpenRouter adapter (`pydantic-ai-slim[openrouter]`, model `OPENROUTER_MODEL`)
**Then** it sends only the system prompt, `CoachFacts`, the prior chat turns of this analysis (role + text) and the question exactly as typed, and returns the typed structure `{kind: answer|refusal, refusal_class: not_measured|other_swings|pain|competition|off_topic|null, text, based_on}` (AD-18, NFR-9)
**And** the system prompt states the grounding rules (only this analysis, cite each number with `[E<n>]`, never raise a band, outcome words for possible/absent faults, no drill for a possible fault or the observation, ≤80 words, jargon blocklist, one-sentence refusal with one next step) (FR-20)
**And** a pytest test with a recording fake transport asserts the request carries no email, user ID, clip, image or path (NFR-9)

**Given** the chat service's answer policy `ask(facts, history, question)` used for both adapters
**When** the first answer fails `grounding_check(kind="chat")`
**Then** `answer()` is called once more with the same input; if the second answer passes it is returned with `source: llm` (or `mock`) (AR-27, AD-19)
**And** if the second answer also fails, the fixed refusal from `rules.yaml` is returned with `kind: refusal`, `refusal_class: null`, `source: refusal` and `based_on` = rule table `[ASSUMPTION: fallback key name and copy, pending copy sign-off]`
**And** when an answer that passes has `refusal_class: pain`, its text is replaced by the `rules.yaml` medical notice ("Generic guidance, not medical advice — see a physiotherapist if you feel pain.") and nothing else (FR-20, AD-19, PRD §6.2)
**And** pytest tests with a scripted fake adapter prove each path: pass first time, fail-then-pass, fail twice → `source: refusal`, pain → medical notice

**Given** the OpenRouter call raises a transport error or exceeds `LLM_TIMEOUT_SECONDS` (20) on either attempt
**When** `ask()` runs
**Then** it raises `LlmUnavailable` and returns no answer, so the caller stores nothing (AD-23); a pytest test with a fake adapter that times out proves it
**And** the Mock adapter never raises `LlmUnavailable` (FR-15)

**Given** a key is configured in the test environment
**When** `pytest -m llm tests/coach/test_chat_sm13.py` runs the SM-13 fixed question set from Story 6.2 against the real model and the three fixtures
**Then** every stored output (after retry/fallback) passes the chat check, is ≤80 words, refuses where expected and keeps every band as it is in the fixture (SM-13, same mode rule as SM-7)
**And** without a key the `llm` marker is skipped and the mock run still proves SM-13 `[ASSUMPTION: marker name]`
**And** the decision record from Story 6.1 is updated with the measured median cost per chat question from this run, replacing the estimate (NFR-10, OQ2)

**Given** `FEATURE_CHAT=false`
**When** the app runs after this story
**Then** nothing changes for the player; no endpoint or table exists yet (cut rule)

### Story 6.4: Ask, store and reopen the chat through the API

As a player,
I want to post a question about my result and get the stored conversation back when I reopen it,
So that my chat lives with its analysis and disappears when I delete it.

**Slice:** `backend/app/modules/coach/chat/` (`routes.py`, `service.py`, `schemas.py`), `backend/app/modules/coach/` (models, `repo.py` for `chat_messages`), `backend/app/migrations/` (one migration), `backend/app/core/errors.py` (codes), `frontend/openapi.json` + `frontend/src/shared/api/schema.d.ts` (generated), `backend/tests/`
**Requirements:** FR-20, FR-2, FR-3 (chat part), FR-15 (mock chat), NFR-9, AR-24 (chat flags), AR-14, AR-18, AR-23, AR-25 (coach endpoints), AR-30, AR-31

**Acceptance Criteria:**

**Given** the migrations at head
**When** this story's single Alembic migration runs
**Then** it creates `chat_messages` (`id` UUID, `user_id` → `users` `ON DELETE CASCADE`, `analysis_id` → `analyses` `ON DELETE CASCADE`, `role` player|coach, `text`, `kind` answer|refusal|null, `refusal_class` null|not_measured|other_swings|pain|competition|off_topic, `source` llm|mock|refusal|null, `based_on` `JSON().with_variant(JSONB, "postgresql")`, `created_at` UTC) with an index on (`analysis_id`, `created_at`) (AR-30, AD-2, AD-7)
**And** the migration test still finds exactly one head and runs upgrade → downgrade → upgrade on Postgres (`pytest -m pg`) (AR-30)

**Given** a player with a stored chat on an analysis (`pytest -m pg`)
**When** the analysis is deleted, the clip is deleted with its analysis, or the account is deleted (Epic 5 endpoints)
**Then** that analysis's `chat_messages` rows are gone through the cascade, and "delete clip, keep analysis" keeps them (FR-3, AD-8, AR-19)

**Given** a signed-in player and `FEATURE_CHAT=true`
**When** they `POST /api/analyses/{id}/chat` with `{question}` and header `X-Requested-With: aicoach` on their own analysis with status `result`
**Then** the response is 201 `{question: ChatMessage, answer: ChatMessage}` from the Story 6.3 policy, and both messages are stored in one short transaction after the answer returns (no transaction is held open during the model call) `[ASSUMPTION]` (FR-20)
**And** `ChatMessage` = `{id, role, text, kind, refusal_class, source, based_on: [{type: evidence|fact, id|null, key|null, label}], created_at}`, where `label` is resolved server-side from the `AnalysisResult` snapshot (e.g. "hip movement", "impact frame", the drill name, "unverified observation (confidence: low)", "rule table") so the frontend has no ID-to-label map (AD-9, AD-10) `[ASSUMPTION: label field]`
**And** in mock mode the answer has `source: mock` and is one of the fixed sample answers (FR-15)

**Given** the same player
**When** they `GET /api/analyses/{id}/chat`
**Then** the response is 200 `{messages: [ChatMessage]}` oldest first, empty for a new result (FR-20 "shown again when the result is reopened")

**Given** the coach slice reads the analysis
**When** the chat service loads status and `AnalysisResult`
**Then** it uses only `swings.service` public functions with the caller's `user_id`, and the import-linter contract passes (coach → swings service only, swings never imports coach) (AR-14, AD-2)

**Given** the error cases
**When** a request is made
**Then** another player's analysis or an unknown ID → `404 not_found` for GET and POST, and the chat repo functions all take `user_id` (FR-2, AR-18)
**And** an analysis with status `queued`, `running`, `failed` or `rejection` → `409 chat_not_available`, nothing stored (FR-20, AD-23)
**And** a stored result with an old `schema_version` → `409 result_outdated` (AR-11)
**And** `LlmUnavailable` (transport error or timeout) → `503 llm_unavailable`, and neither the question nor an answer is stored (AD-23)
**And** `FEATURE_CHAT=false` → `404 feature_disabled` for GET and POST on any analysis, nothing stored (AD-23)
**And** an empty or whitespace-only question, or one over 500 characters, → `422` with the error envelope `{"error": {"code": "question_invalid", "message"}}` `[ASSUMPTION: 500-character limit and code name]` (AR-23)
**And** a POST without `X-Requested-With: aicoach` is refused by the CSRF middleware and a signed-out request gets 401 (AR-22, AR-18)
**And** `chat_not_available`, `llm_unavailable`, `feature_disabled` and `question_invalid` exist in the one code list in `app/core/errors.py` (AR-23)
**And** each case has an httpx AsyncClient API test on SQLite with `PRAGMA foreign_keys=ON`, using a fake `CoachLLM` for the 503 case

**Given** `GET /api/config`
**When** `FEATURE_CHAT` is true or false
**Then** `chat_enabled` equals `FEATURE_CHAT` and `mock_mode` is unchanged (AR-24, AD-23); a pytest test covers both values

**Given** a chat request is handled
**When** the backend logs it
**Then** the log line holds `analysis_id`, `kind`, `refusal_class`, `source` and the attempt count, and never the question or answer text; a pytest `caplog` test posts a unique question string and asserts it appears in no log record (AR-31, PRD §6.1)

**Given** the endpoints are added
**When** `uv run python -m app.export_openapi` and `npm run gen:api` run
**Then** the committed `frontend/openapi.json` and `schema.d.ts` include both coach endpoints with typed models (no `dict`/`Any`), and the stale-OpenAPI test passes (AR-23)

**Given** `FEATURE_CHAT=false`
**When** the app is used end to end
**Then** results, deletes and every P1 flow work unchanged and the result view keeps its existing composer placeholder; only the chat endpoints answer `404 feature_disabled` (cut rule)

### Story 6.5: Talk to the coach in the result thread

As a player,
I want a composer under my result where I can ask a question and read the coach's answer in the same thread, including my earlier questions when I come back,
So that I can understand my result without leaving it.

**Slice:** `frontend/src/modules/chat/` (composer, grounding note, chat thread, states), `frontend/src/app/swing/[analysisId]/` (composition), `frontend/src/modules/result/` (public slot props only: chat slot and "Ask the coach" target), uses `frontend/src/shared/{conversation,evidence,ui,api}`
**Requirements:** FR-20, FR-15 (mock chat in UI), AR-24 (chat flags in UI), AR-12, AR-28, UX-DR10 (composer, grounding note), UX-DR46, UX-DR13 (chat part), UX-DR45 (chat states), UX-DR8, UX-DR49 (chat parts)

**Acceptance Criteria:**

**Given** a thread at `/swing/[analysisId]` whose analysis has status `result` and `/api/config` returns `chat_enabled: true`
**When** the page renders
**Then** the route layer passes the chat module into the result view's chat slot at the end of the thread; `src/modules/result/` imports nothing from `src/modules/chat/` and the ESLint boundary rules pass (Code Organisation rules 1–2)
**And** the composer is a card pill with ink border, placeholder "Ask about this result…" and a clay send circle (UX-DR10, DESIGN.md Composer)
**And** under it the grounding note with a lock icon reads "Answers are based only on this analysis — no new faults, numbers or drills." (below 768px: "Answers are based only on this analysis."), always visible and not dismissible (UX-DR10)

**Given** the thread's analysis is `queued` or `running` (or `failed`) and chat is enabled
**When** the page renders
**Then** the composer shows the disabled state "You can ask the coach once the result is ready.", and it becomes enabled without a reload when polling turns the status into `result` (UX-DR10, FR-20)
**And** for a `rejection` no composer, grounding note or prompt is rendered (FR-20, UX-DR34)

**Given** an enabled composer
**When** the player presses Enter with text
**Then** the question is posted, appears as a right-aligned player message, and the composer is disabled with the chat typing indicator (coach mark + three dots, no text) until the answer arrives (UX-DR10, UX-DR8)
**And** Shift+Enter adds a new line, and empty or whitespace-only input cannot be sent (send button disabled, Enter does nothing) (UX-DR10, UX-DR49)
**And** the answer arrives whole as a coach message (mark, italic "Coach", time, Newsreader body), is announced through a polite live region, and the typing indicator is not re-announced (UX-DR8, UX-DR49)
**And** `[E<n>]` citations in the answer text are parsed with `shared/evidence/citations.ts` and rendered as raised teal `[n]` inline citations with their accessible names, never as raw `[E3]` text (AR-12, UX-DR23)

**Given** a result with stored chat messages
**When** the player reopens the thread
**Then** `GET /api/analyses/{id}/chat` fills the thread oldest first under the result, behind dashed placeholders while loading (no spinner), and a load failure shows "Couldn't load this. Try again." inline (FR-20, UX-DR45)

**Given** the POST returns `503 llm_unavailable`
**When** the response arrives
**Then** the player message is removed, the composer is disabled with "The coach can't answer questions right now. Your result is complete.", the grounding note stays and the result is unchanged (FR-20, UX-DR45) `[ASSUMPTION: stays disabled until the page is reloaded]`

**Given** the request fails because the network is lost
**When** the fetch rejects without a response
**Then** the player message is removed, the question text stays in the composer, and one inline line under the composer reads "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." with "Try again" (UX-DR45, UX-DR46)
**And** "Try again" resends the same question, and the inline line clears on retry or when the input changes; it is never a modal or banner (UX-DR46)

**Given** `/api/config` returns `chat_enabled: false`, or a chat request returns `404 feature_disabled`
**When** the thread renders
**Then** there is no composer, suggested prompt, grounding note, "Ask the coach" jump chip or "Ask the coach about this" link, `GET …/chat` is not called, and everything else on the result is unchanged (AR-24, UX-DR45, UX-DR13) `[ASSUMPTION: a mid-session feature_disabled hides chat like the cut]`
**And** this replaces Epic 4's disabled composer placeholder for the cut case, as AD-23 requires hiding

**Given** chat is enabled on a result
**When** the player activates the "Ask the coach" jump chip, or "Ask the coach about this" on the no-fault outcome
**Then** the composer receives focus, with no scroll animation under reduced motion (UX-DR13, UX-DR49) `[ASSUMPTION: the no-fault link behaves like the chip]`

**Given** mock mode
**When** the player asks a question
**Then** the fixed sample answer from Story 6.2 is shown like any answer (FR-15)

**Given** the Vitest suite
**When** `npm test` runs the chat module tests with a mocked API client
**Then** each of the above cases is covered: enabled/disabled/hidden composer by status and flag, Enter vs Shift+Enter, empty input, disabled while answering, history on reopen, 503 line, network-lost line with the question kept, cut state hiding all five elements, chip focusing the composer

### Story 6.6: See what the answer rests on and get suggested questions

As a player,
I want each coach answer to light the evidence it cites, end with a "Based on:" note, and be followed by questions I can tap,
So that I can check every answer against my swing and know what to ask next.

**Slice:** `frontend/src/modules/chat/` (Based-on footnote, suggested prompts, lit citations), `backend/app/modules/coach/chat/` (`suggested_prompts` in responses), `config/rules.yaml` (`coach` suggested prompts), `backend/engine/aicoach_engine/` (rules schema only), uses `frontend/src/shared/evidence/`
**Requirements:** FR-20, AR-12, AR-27, AR-28, UX-DR10 (suggested prompts, "Based on" footnote), UX-DR23 (chat citations), UX-DR47 (prompts)

**Acceptance Criteria:**

**Given** `rules.yaml` `coach` holds the suggested prompts per result type — verified fault: "How do I know the drill is working?", "What does 'likely cause' mean?", "Can I do this drill in a net?"; no verified fault: "What did you check in my swing?" `[ASSUMPTION: stored in rules.yaml so copy stays out of components, AR-28]`
**When** `GET` or `POST /api/analyses/{id}/chat` responds for a result
**Then** the response includes `suggested_prompts` for that result type (from `main_finding`), minus prompts already sent as player messages in this chat `[ASSUMPTION: refresh rule]` (UX-DR10, UX-DR47)
**And** a pytest test runs every suggested prompt through the Mock adapter against the three Story 6.2 fixtures and asserts `kind: answer` and a passing chat check, so no prompt suggests something that would be refused (UX-DR10)
**And** the OpenAPI file and generated types are regenerated (AR-23)

**Given** an enabled composer
**When** the thread renders on desktop or laptop (≥768px)
**Then** up to three suggested prompts show as card pills above the composer, wrapping to two rows; below 768px one full-width pill shows (UX-DR10)
**And** tapping a prompt sends it as the player's message through the same path as the composer (disabled while answering, same 503 and network-lost handling) (UX-DR10)
**And** after each answer the prompts are replaced by the response's `suggested_prompts`; with none left, no prompt row is shown (UX-DR10)
**And** prompts are hidden while the composer is disabled and in the chat-cut state (UX-DR45)

**Given** a coach answer with `based_on`
**When** it renders
**Then** a "Based on:" footnote in mono teal sits under it, listing evidence items as citation links ("[3] hip movement · [2] impact frame · wall drill") and facts by their server `label` (UX-DR10, AR-12, FR-20)
**And** a refusal's footnote lists what was checked, e.g. "Based on: unverified observation (confidence: low) · rule table" (UX-DR10, UX-DR47)
**And** a coach message with an empty `based_on` is never rendered without a footnote; the frontend shows the stored list only and derives no labels (AR-28)

**Given** the latest coach answer cites evidence (inline `[E<n>]` or `based_on` evidence items)
**When** it arrives or the thread is reopened
**Then** those pins are lit in the Evidence panel (desktop), drawer (narrow laptop) or tray (phone) through `shared/evidence`'s lit state, and stay lit until the next answer, when the previous ones unlight (UX-DR23, FR-20) `[ASSUMPTION: on reopen the latest stored answer's pins are lit]`
**And** activating a citation in an answer or footnote highlights the matching item (tint + teal outline) and scrolls it into view, opening the drawer or tray at that item on narrower widths (UX-DR23)
**And** lit pins do not pulse under reduced motion (UX-DR49)

**Given** the Vitest suite
**When** `npm test` runs
**Then** tests cover: three prompts on desktop / one on phone, prompt tap sends, refresh after an answer, no prompts when the list is empty or chat is disabled, footnote text for an answer and a refusal, lit IDs = latest answer's citations only, and the shared citation fixture parses chat answers the same as `coach/grounding.py` (AR-12)

**Given** `FEATURE_CHAT=false`
**When** the result renders
**Then** no prompt, footnote or chat citation appears and no chat request is made (cut rule, AD-23)


## Epic 7: See my progress across swings (P3, stretch)

A player can list every past analysis newest first, including analyses whose clip was deleted, and compare two analyses on the same measurement with both confidence bands, with different bands visibly marked so a change is not read into noise. Everything new is behind `FEATURE_HISTORY` (default `false`); `GET /api/analyses` (the Account list from Epic 5) stays P1 and ungated. Builds on Epics 1–5 only.

### Story 7.1: Browse my analysis history

As a player,
I want to open a list of all my past analyses, newest first, including the ones whose clip I deleted,
So that I can go back to any result I have had.

**Slice:** backend `app/modules/system/` (config flag only); frontend `src/modules/history/`, `src/app/history/page.tsx` and the Account route `src/app/account/page.tsx` (composition only); the analysis row moves from `src/modules/account/` to `src/shared/ui/` (second use, Rule 3); tests `backend/tests/history/`, `frontend/src/modules/history/*.test.tsx`
**Requirements:** FR-16, FR-2, AR-24, AR-28, UX-DR40, UX-DR45

**Acceptance Criteria:**

**Given** `FEATURE_HISTORY=false` (the default in `.env.example`)
**When** the frontend calls `GET /api/config`
**Then** the response contains `history_enabled: false` (added to the config response model if Epic 1 did not already expose the flag) [AR-24] `[ASSUMPTION: field name history_enabled]`
**And** the Account page shows no "See all n analyses" link [UX-DR40]
**And** opening `/history` shows the existing not-found state "This analysis doesn't exist or isn't yours." with a link to the swings [UX-DR45] `[ASSUMPTION: flag off reuses the not-found page]`
**And** `GET /api/analyses` still returns the Account list unchanged [AR-24]

**Given** `FEATURE_HISTORY=true` and a signed-in player whose `GET /api/me` returns `analyses_count: 3`
**When** the player opens Account
**Then** a link "See all 3 analyses" is shown under "Your analyses" and navigates to `/history` [FR-16, UX-DR40]
**And** the count comes from `analyses_count`, never from counting rows in the browser

**Given** `FEATURE_HISTORY=true` and `analyses_count: 0`
**When** the player opens Account
**Then** the "See all n analyses" link is hidden and "No analyses yet." is shown as before `[ASSUMPTION: link hidden at 0]`

**Given** `FEATURE_HISTORY=true` and a player with two completed analyses
**When** the player opens `/history`
**Then** both analyses are listed in the order `GET /api/analyses` returns them, newest first by `created_at`, and the frontend does not re-sort them [FR-16]
**And** each row shows the local date and the main finding label and band exactly as the Account list shows them for the same analysis, with the band drawn by the `shared/evidence` confidence band component (word + bars, never colour only) [AR-29, UX-DR19]
**And** activating a row opens `/swing/[analysisId]` for that analysis [FR-16]

**Given** `FEATURE_HISTORY=true` and an analysis whose clip was deleted with "Delete clip, keep analysis"
**When** the player opens `/history`
**Then** the analysis is still listed, with the meta "clip deleted", and opening it shows the result with the header "Clip deleted" (not a link) [FR-16, FR-19, UX-DR12]
**And** rows whose clip still exists show the meta "clip in swing library" [UX-DR40]

**Given** the Account list and the history list both need the same analysis row
**When** this story is merged
**Then** the row component lives in `frontend/src/shared/ui/` and is imported by both `src/modules/account/` and `src/modules/history/`, and neither module imports the other (ESLint boundaries rule passes) [Code Organisation Rules 1–4]

**Given** two players A and B, each with analyses, and `FEATURE_HISTORY=true`
**When** A opens `/history`
**Then** none of B's analyses appear, and an API test asserts `GET /api/analyses` as A contains no row with B's `analysis_id` [FR-2]

**Given** a signed-out visitor
**When** they open `/history`
**Then** they are sent to `/signin?next=/history` and land back on `/history` after signing in [AR-28]

**Given** `/history` is loading or the request fails
**When** the page renders
**Then** dashed placeholders stand in for the rows during load (no spinner), and a failed load shows "Couldn't load this. Try again." inline [UX-DR27, UX-DR45]
**And** a player with no analyses sees "No analyses yet."

**Given** a 375 px wide phone viewport
**When** `/history` renders
**Then** there is no horizontal scroll, the whole row is the target and each row's hit area is at least 44×44 px [UX-DR49]

### Story 7.2: Compare two analyses side by side

As a player,
I want to choose two of my analyses and see the same measurement side by side with both confidence bands,
So that I can see whether a drill is working.

**Slice:** backend `app/modules/swings/history/` (`routes.py`, `service.py`, `schemas.py`, using the shared `swings` models and `repo.py`); frontend `src/modules/history/`, `src/app/history/compare/page.tsx`; regenerated `frontend/openapi.json` and `src/shared/api/schema.d.ts`; tests `backend/tests/history/`, `frontend/src/modules/history/*.test.tsx`
**Requirements:** FR-17, SM-12, FR-2, AR-11, AR-18, AR-21, AR-23, AR-24, AR-29

**Acceptance Criteria:**

**Given** `FEATURE_HISTORY=true` and two analyses with status `result` owned by the signed-in player
**When** the client calls `GET /api/analyses/compare?a={analysis_id}&b={analysis_id}` `[ASSUMPTION: query parameter names a and b]`
**Then** the response is `200` with both sides (`analysis_id`, `created_at`, `main_finding_label`, whether the clip was deleted) ordered older first `[ASSUMPTION: older = left]`, and one entry per measurement key present in both stored results [FR-17, SM-12]
**And** each entry carries, for each side, the stored `label`, `display`, `band` and threshold `display` copied from that analysis's `AnalysisResult.measurements` without recomputation or reformatting [AR-11, AR-29]
**And** the response model references the engine's Pydantic measurement model (no `dict`/`Any`), `uv run python -m app.export_openapi` and `npm run gen:api` are re-run and the stale-`openapi.json` test passes [AR-23]

**Given** `FEATURE_HISTORY=false`
**When** the client calls `GET /api/analyses/compare`
**Then** it returns `404` with error code `feature_disabled` in the standard envelope [AR-24]

**Given** the route `GET /api/analyses/{id}` already exists
**When** `GET /api/analyses/compare?a=…&b=…` is called
**Then** the compare route is matched, not `GET /api/analyses/{id}` with `id="compare"` (route registered first; a test proves it)

**Given** player A and an analysis owned by player B
**When** A calls compare with one of A's IDs and B's ID (in either position), or with an ID that does not exist
**Then** the response is `404 not_found` and the body contains no data from either analysis, A's included [FR-2, AR-18]
**And** the lookup goes through the `user_id`-scoped `repo.py` functions; `swings/history/` does not import `repo_system.py` (the existing import test passes) [AR-18]

**Given** `a` and `b` are the same ID, a parameter is missing, or a value is not a UUID
**When** compare is called
**Then** the response is `422` in the standard envelope, with the code taken from the one list in `app/core/errors.py` `[ASSUMPTION: a new code compare_same_analysis for a == b]` [AR-23]

**Given** one of the two analyses has status `queued`, `running`, `rejection` or `failed`
**When** compare is called
**Then** the response is `409` with code `compare_not_available` and no measurements `[ASSUMPTION: code name, mirrors chat_not_available]` [AR-29]

**Given** one of the two stored results has an old `schema_version`
**When** compare is called
**Then** the response is `409 result_outdated` [AR-11]

**Given** two result analyses whose stored results share no measurement key (e.g. the rule table changed between them)
**When** the compare page renders
**Then** it shows "These two analyses have no measurement in common." and no empty columns `[ASSUMPTION: copy]`

**Given** `FEATURE_HISTORY=true` and the player is on `/history`
**When** the player ticks "Compare" on two rows with a result
**Then** the primary button "Compare these two" becomes enabled and opens `/history/compare?a=…&b=…` [FR-17] `[ASSUMPTION: selection UI and route; compare is spine-only in EXPERIENCE.md]`
**And** rows for rejections, failed or running analyses have no "Compare" control
**And** while two rows are ticked the other "Compare" controls are disabled until one is unticked, and the button is disabled with fewer than two
**And** each "Compare" control has a 44×44 px hit area and its own accessible name ("Compare analysis of {date}") [UX-DR49]

**Given** the compare page has loaded
**When** the player reads it
**Then** each common measurement shows its label once and the two `display` values side by side in teal mono, each with its own confidence band from `shared/evidence` (word + bars) [FR-17, SM-12, UX-DR3, UX-DR19]
**And** no delta, percentage change, arrow, score or chart is computed or drawn; the frontend formats no number [AR-29, UX-DR50]
**And** each side's header shows its date and main finding and links to `/swing/[analysisId]`
**And** at 375 px width both columns stay side by side with wrapping text and no horizontal scroll [UX-DR49]

**Given** a player who opens `/history/compare?a=…&b=…` with another player's ID or with the flag off
**When** the page loads
**Then** it shows "This analysis doesn't exist or isn't yours." with a link to the swings [UX-DR45]

**Given** the API test fixtures of two result analyses for one player
**When** the test suite runs
**Then** an API test asserts at least one measurement is returned with both bands present (SM-12), and a Vitest test asserts both bands render as words [SM-12]

### Story 7.3: Mark comparisons whose confidence bands differ

As a player,
I want a comparison to tell me plainly when the two measurements have different confidence bands,
So that I don't read a change into what may be noise.

**Slice:** backend `app/modules/swings/history/` (`service.py`, `schemas.py`); frontend `src/modules/history/`, reusing the inline message from `src/shared/ui/` and the confidence band from `src/shared/evidence/`; regenerated `frontend/openapi.json` and `schema.d.ts`; tests `backend/tests/history/`, `frontend/src/modules/history/*.test.tsx`
**Requirements:** FR-17, SM-12, AR-23, AR-29, UX-DR3, UX-DR19, UX-DR46

**Acceptance Criteria:**

**Given** two compared analyses where a measurement has band `high` on one side and `low` on the other
**When** `GET /api/analyses/compare` returns
**Then** that measurement entry has `bands_differ: true`, computed in `swings/history/service.py`, and entries with equal bands have `bands_differ: false` [FR-17]
**And** the frontend uses `bands_differ` as given and does not compare the band values itself [AD-9 rule "the frontend never works out state or finding"]
**And** the OpenAPI export and generated types are refreshed and the stale-`openapi.json` test passes [AR-23]

**Given** a measurement row with `bands_differ: true`
**When** the compare page renders
**Then** the row shows an inline warning with the medium-coloured `!` and one line of ink text: "Different confidence (high vs low) — this difference may be noise, not a change." with the two band words taken from the response `[ASSUMPTION: copy, pending copy sign-off]` [FR-17, UX-DR46]
**And** the warning is text, not colour only, and is linked to the row with `aria-describedby` so a screen reader reads it with the values [UX-DR19, UX-DR49]
**And** it uses no new hue, no red fill, no modal and no banner [UX-DR3, UX-DR46]

**Given** a measurement row with `bands_differ: false`
**When** the compare page renders
**Then** no warning is shown for that row and both bands still show as words + bars [FR-17, SM-12]

**Given** a comparison where one clip was filmed under 120 fps (so its bands are never `high`) and the other at 120 fps with `high`
**When** the page renders
**Then** the affected rows carry the different-band warning like any other band difference, and the page states nothing about which swing is better [FR-7, FR-17]

**Given** the test suite
**When** it runs
**Then** an API test covers equal bands, each pair of different bands (high/medium, high/low, medium/low) and asserts `bands_differ`, and a Vitest test asserts the warning appears only on `bands_differ: true` rows [FR-17]

## Epic 8: The examiner runs AIcoach from the README, and the numbers are in

In the final week (2026-12-08 → 2026-12-15) the repo gets bundled author sample clips, a README that takes the examiner from clone to a complete mock-mode result (UJ-5), the one Playwright smoke test of that path, a clean-machine run, the evaluation-set SM report, the NFR-1 bench on the target laptop, the real-model grounding checks when a key is configured, and the hand-in checklist. Builds on Epics 1–6 and must work if Epic 6 was cut (`FEATURE_CHAT=false`) and if Epic 7 was never built.

### Story 8.1: Bundle the author's sample clips

As the examiner,
I want ready-made swing clips in the repository,
So that I can get a complete result without filming a swing myself.

**Slice:** repo level `samples/` (clips + `samples/README.md`), `.gitignore`, `.gitattributes` (only if LFS), `docker-compose.yml` (verify mount); backend `app/modules/system/` (startup sample check); tests `backend/tests/system/`
**Requirements:** FR-15, NFR-4, NFR-8, AR-33, AR-3 (`APP_ENV`)

**Acceptance Criteria:**

**Given** the author's own down-the-line, right-handed swing clips
**When** the samples are added
**Then** `samples/` contains `ee-01.mp4` (one swing, about 10 s, at most 15.0 s by `ffprobe`, filmed at 120 fps or higher) and one second clip whose `ffprobe` duration is between 14.0 and 15.0 s for the 15-s speed check, both mp4 or mov [FR-15, NFR-1] `[ASSUMPTION: two clips; the second clip's name is the author's choice]`
**And** every person visible in the clips is the author [NFR-8]

**Given** the samples are in place
**When** the author runs `cd backend; uv run aicoach-engine analyse ..\samples\ee-01.mp4 --out D:\tmp\ee-01`
**Then** the printed `AnalysisResult` is a result, not a rejection, with `main_finding` early extension as a verified fault, so the README demo shows a complete result (SM-4 data side) [FR-15]
**And** the second clip also produces a result, not a rejection

**Given** the samples are in place
**When** `samples/README.md` is read
**Then** it states that the clips show the author and that the author consents to publishing them in this repository [NFR-8, AR-33]
**And** for each clip it lists the file name, duration and fps (copied from the engine's `clip` output), the expected main finding in mock mode and the file's SHA-256

**Given** the total size of `samples/`
**When** it is about 20 MB or less
**Then** the clips are committed as plain Git files [AR-33]
**And** when it is larger, `.gitattributes` has `samples/*.mp4 filter=lfs diff=lfs merge=lfs -text` (and the same for `.mov` if used), the clips are committed through Git LFS, and `samples/README.md` records the measured size and the choice [AR-33]

**Given** LFS was chosen and a clone was made without Git LFS installed
**When** the examiner drops the pointer file `ee-01.mp4` on New swing
**Then** the upload is refused before analysis because `ffprobe` finds no video stream, and `samples/README.md` names `git lfs install` + `git lfs pull` as the fix [AR-20]

**Given** the `.gitignore` from the scaffold
**When** `git check-ignore -v samples/ee-01.mp4` and `git check-ignore -v data/x.mp4` are run
**Then** the sample is not ignored and the `data/` clip is ignored, and `git ls-files "*.mp4" "*.mov"` lists only paths under `samples/` [NFR-8, AR-36]

**Given** `docker compose up --build` is running
**When** `docker compose run --rm backend ls /app/samples` is run
**Then** it lists the sample clips (mounted read-only per the Compose file) [AR-33]

**Given** `APP_ENV=demo`
**When** the backend starts
**Then** it writes one structured log line listing the sample files found in `/app/samples`, or a warning line if none are found, and creates no user, clip or analysis row [AR-3] `[ASSUMPTION: "seeding of the sample clips" (setup-guide §3.1) means this check; no demo account or pre-loaded analysis, because no clip may be stored for a player without the library consent (FR-18) and the architecture review did not adopt demo accounts]`
**And** with `APP_ENV=local` the check is skipped
**And** a test starts the app with each value and asserts the row counts in `users`, `clips` and `analyses` are unchanged

### Story 8.2: Write the README so the examiner can run AIcoach

As the examiner,
I want a README that takes me from a fresh clone to a complete result with no keys or paid accounts,
So that I can assess AIcoach on an ordinary laptop.

**Slice:** repo level `README.md`
**Requirements:** FR-15, NFR-4, SM-10, AR-5, AR-36 (README links), NFR-2

**Acceptance Criteria:**

**Given** the README
**When** the examiner reads its first section, "Run AIcoach (examiner, mock mode)"
**Then** it lists the prerequisites (Docker Desktop with Engine 29.x and Compose, Git, and Git LFS only if Story 8.1 chose LFS) and says no API keys, paid accounts or network access to a language model are needed [NFR-4, FR-15]
**And** it gives exactly these steps: clone the repo; `copy .env.example .env` (Windows) or `cp .env.example .env` (macOS/Linux) with no edits; `docker compose up --build`; open `http://localhost:8080`; create an account and tick the library consent box; choose "New swing"; drop `samples/ee-01.mp4` [UJ-5, SM-10]
**And** it says what the examiner should see: a verified fault with its measurement and confidence band, key frames, the fault chain, the template explanation with a feel cue, one drill and one mobility exercise, and the "Mock mode" label [FR-15, SM-10]

**Given** the README
**When** the examiner follows its links
**Then** one link opens setup-guide §6.1 "Demo / examiner (UJ-5, the README path)" and one opens §6.3 "Phone on the same Wi-Fi (NFR-2)" in `docs/_bmad-output/planning-artifacts/architecture/architecture-AIcoach-2026-11-25/setup-guide.md`, both as relative links that resolve on GitHub [AR-36]

**Given** the README's "Open it from a phone" section
**When** it is read
**Then** it gives: find the laptop IPv4 with `ipconfig` → "Wireless LAN adapter Wi-Fi"; run once in an administrator PowerShell `New-NetFirewallRule -DisplayName "AIcoach 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow -Profile Private`; set the Wi-Fi profile to Private; open `http://<laptop-ip>:8080` on the phone; and the phone-hotspot workaround for client isolation [AR-5, NFR-2]
**And** it notes `DEV_LAN_ORIGIN` is needed only for `npm run dev`

**Given** the README's "Develop" section
**When** it is read
**Then** it gives the dev path of setup-guide §6.2 (`.env` with `localhost:5432`, a `DATA_DIR` outside the repo and the `host.docker.internal` upstreams; `docker compose up db proxy`; `uv run alembic upgrade head`; `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`; `npm run dev`) and says to browse through `http://localhost:8080`, not port 3000 [AR-3]

**Given** the README's "Engine and evaluation" section
**When** it is read
**Then** it gives `uv run aicoach-engine analyse ..\samples\ee-01.mp4 --out D:\tmp\ee-01`, `uv run pytest` (and `-m pg`), the two `docker compose run --rm -v "${env:EVAL_DATA_DIR}:/eval-data:ro" -e EVAL_DATA_DIR=/eval-data backend aicoach-engine eval --split tuning|evaluation` commands and `docker compose run --rm backend aicoach-engine bench /app/samples/ee-01.mp4 --runs 5`, and states that `EVAL_DATA_DIR` is outside Git and must be backed up [AR-33]

**Given** the README's "Options" section
**When** it is read
**Then** it explains that setting `OPENROUTER_API_KEY` in `.env` switches to the real model (`LLM_MODE=auto`), that `.env` must never be committed, that `FEATURE_CHAT` may be `false` (then no chat appears) and that `FEATURE_HISTORY` defaults to `false` [AR-24, NFR-8]

**Given** the author's own laptop after `docker compose down -v`
**When** the author follows only the README's first section, word for word
**Then** a complete mock result appears, and any step that needed knowledge not in the README is fixed in the README before the story is done [SM-10, NFR-4]
**And** a phone on the same Wi-Fi opens `http://<laptop-ip>:8080` and reaches the sign-in page [NFR-2]

### Story 8.3: Automate the examiner path as the one Playwright smoke test

As the author,
I want UJ-5 to run as one automated browser test in mock mode,
So that I know the examiner path still works after every change in the final week.

**Slice:** frontend `frontend/e2e/uj5-smoke.spec.ts`, `frontend/playwright.config.ts`, `frontend/package.json` (script); `README.md` (test command)
**Requirements:** AR-32, SM-10, SM-4, FR-15, NFR-4, AR-24

**Acceptance Criteria:**

**Given** the stack is started with `docker compose up --build` from a `.env` copied unchanged from `.env.example` (mock mode, no key)
**When** the author runs `cd frontend; npx playwright install chromium; npm run test:e2e` `[ASSUMPTION: script name test:e2e; base URL from PLAYWRIGHT_BASE_URL, default http://localhost:8080]`
**Then** exactly one spec runs: it opens `/`, creates an account with a unique email, ticks the consent box, lands on New swing, sets `../samples/ee-01.mp4` on the drop zone's file input, and waits for the step log to reach "5 of 5" with a 180 s timeout [AR-32, NFR-1]
**And** it asserts the result shows "Verified fault" with the fault name, a "confidence: high|medium|low" band, at least one key frame whose alt text contains the event time, a "Likely cause" chain link, a drill and a mobility exercise with the notice "Generic guidance, not medical advice — see a physiotherapist if you feel pain.", the "Read my full explanation" row, "In your swing library", and the "Mock mode" label [SM-4, SM-10, FR-15]

**Given** `GET /api/config` returns `chat_enabled: true`
**When** the test reaches the result
**Then** it sends the first suggested prompt and asserts a coach answer appears with a "Based on:" footnote (a fixed mock answer) [FR-15, UJ-5 step 5]

**Given** `FEATURE_CHAT=false` (or Epic 6 never shipped) and the stack restarted
**When** the same test runs
**Then** it passes, asserting there is no composer and no "Ask the coach" chip, and does not fail on the missing chat [AR-24]
**And** the result of a run with chat on and a run with chat off are both recorded in the story's dev notes

**Given** `FEATURE_HISTORY` is `true`, `false`, or the history slice was never built
**When** the test runs
**Then** its outcome does not change; the test touches no history UI

**Given** the analysis ends in a rejection or `failed`
**When** the test waits for the result
**Then** it fails at once with a message naming the state ("Cannot analyse" or "Not analysed"), not after a timeout

**Given** the test has finished, pass or fail
**When** cleanup runs
**Then** it deletes the test account with `DELETE /api/me` (header `X-Requested-With: aicoach`) so repeated runs do not fill the database or the swing library `[ASSUMPTION: cleanup through the API]`

**Given** the repository
**When** `frontend/e2e/` is listed
**Then** it holds this single spec only, and the README's test section gives the commands above [AR-32]

### Story 8.4: Run the evaluation set and record SM-1 to SM-6

As the author,
I want to run the held-back evaluation set once in the backend container and record the report,
So that the course report has honest detection numbers that were never used for tuning.

**Slice:** repo level `docs/evaluation/` (report + summary) `[ASSUMPTION: location]`; `config/rules.yaml` (fault `status` only, if the FR-9 fallback applies); `eval/labels.yaml` read only; `samples/README.md` and `frontend/e2e/uj5-smoke.spec.ts` only if the fallback changes the sample's outcome
**Requirements:** SM-1, SM-2, SM-3, SM-4, SM-5, SM-6, FR-9, AR-33, AR-36, NFR-3

**Acceptance Criteria:**

**Given** `config/rules.yaml` with thresholds frozen after tuning, `eval/labels.yaml` with the `evaluation` split, and `EVAL_DATA_DIR` holding those clips
**When** the author runs `docker compose run --rm -v "${env:EVAL_DATA_DIR}:/eval-data:ro" -e EVAL_DATA_DIR=/eval-data backend aicoach-engine eval --split evaluation`
**Then** the report covers SM-1 to SM-6 with counts per item and records `rules_hash` and `pose_backend` [AR-33, SM-1–SM-6]
**And** it is saved verbatim under `docs/evaluation/` with the run date and the Git commit hash, plus a short summary for the course report

**Given** the report
**When** SM-1 is read
**Then** each verified fault shows detected / total evaluation clips, passes at 75 % or more with at least 4 clips, and is marked "not testable (n clips)" with fewer than 4 [SM-1]
**And** possible faults are not counted as reported faults in SM-1 to SM-3 [FR-9]

**Given** the report
**When** SM-2, SM-3, SM-5 and SM-6 are read
**Then** SM-2 shows "No verified fault found" count on the clean clips (pass: at least 2 of at least 3) [SM-2]
**And** SM-3 shows that none of the three faults was reported on the clips outside the three, and that any observation is labelled unverified [SM-3]
**And** SM-5 compares how often "high" and "low" verified faults are correct when each band has at least 3, else reports the counts descriptively [SM-5]
**And** SM-6 shows a face-on clip and an out-of-frame clip each ending in a rejection with reasons and filming tips (`reasons` with `guide_step`), or "not tested" if the evaluation split has no such clip [SM-6] `[ASSUMPTION: the face-on and out-of-frame clips are labelled in the evaluation split]`

**Given** the clear early-extension evaluation clip
**When** SM-4 is assessed
**Then** the summary records the engine's fault, measurement, band, chain, key frame, drill and mobility exercise from the report, and cites the Story 8.3 smoke test for the explanation part (the engine produces no explanation) [SM-4]

**Given** the evaluation run is done
**When** `git diff` is taken on `config/rules.yaml` after the run
**Then** no threshold, unit or measurement changes; only the FR-9 `status` edit below is allowed, and the over the top vs sway choice is not revisited [FR-9, AD-24]
**And** the tuning tools still refuse `--split evaluation` [AR-33]

**Given** two of the three active faults fail SM-1
**When** the FR-9 fallback is applied
**Then** those two faults get `status: possible_only` in `config/rules.yaml` and nothing else changes [FR-9]
**And** `uv run pytest` passes, the summary documents the shortfall (which faults, their detection rates, the `rules_hash` before and after) for the course report, and the SM figures reported are those of the run before the edit
**And** if early extension is one of the demoted faults, the expected outcome in `samples/README.md` and the smoke test's assertions are updated to the new outcome and the smoke test passes again

**Given** exactly one active fault fails SM-1
**When** the result is recorded
**Then** the shortfall is documented in the summary and no `status` is changed `[ASSUMPTION: the PRD fallback names only the two-fault case]`

### Story 8.5: Measure speed on the target laptop and check grounding against the real model

As the author,
I want the NFR-1 timing measured on my target laptop and the grounding checks run against the real model when I have a key,
So that the course report states real speed and grounding results.

**Slice:** repo level `docs/evaluation/` (bench and grounding records); no code changes expected
**Requirements:** NFR-1, SM-8, SM-7, SM-13, NFR-10, AR-36

**Acceptance Criteria:**

**Given** the target laptop with the Compose images built and no other heavy load
**When** the author runs `docker compose run --rm backend aicoach-engine bench /app/samples/ee-01.mp4 --runs 5` and the same command on the 14–15 s sample
**Then** the median of 5 runs is recorded for each clip, with the laptop's CPU, RAM, OS, `pose_backend` and the commit hash [NFR-1, SM-8]
**And** the 10 s clip passes under 120 s and the 15 s clip under 180 s [NFR-1]

**Given** NFR-1 is defined as `finished_at − started_at` including the mock explanation and excluding upload, queue and transcode
**When** the author uploads each sample once through the app in mock mode
**Then** that span (from the analysis row or `step_timings`) is recorded next to the bench median, so the bench is cross-checked against the NFR-1 definition [NFR-1]

**Given** a clip misses its limit
**When** the result is recorded
**Then** the measured medians are recorded as "not met" with the numbers, and no threshold or evaluation result is changed to make it pass `[ASSUMPTION: a miss is documented, not hidden]`

**Given** mock mode (no key)
**When** `cd backend; uv run pytest` runs
**Then** the SM-7 explanation grounding tests and, if chat is shipped, the SM-13 chat grounding tests pass on the template and fixed mock outputs [SM-7, SM-13]

**Given** an `OPENROUTER_API_KEY` set only in the local `.env` or the shell and `LLM_MODE=auto`
**When** the author runs the SM-7 and SM-13 fixed-input suites built in Epics 4 and 6 against the real model `[ASSUMPTION: the suites can be pointed at the real adapter as built in those epics]`
**Then** pass or fail per fixed input is recorded with the `OPENROUTER_MODEL` name and the logged tokens and cost per call (NOK via `AI_USD_NOK`) [SM-7, SM-13, NFR-10]
**And** after the run `git status` shows no `.env` and the key appears in no tracked file [NFR-8]

**Given** no key is configured
**When** the record is written
**Then** SM-7 and SM-13 are recorded as "mock mode only; real model not run", which is not a failure [SM-7]

**Given** `FEATURE_CHAT=false` at the 2026-12-08 checkpoint or Epic 6 not shipped
**When** the record is written
**Then** SM-13 is recorded as "not applicable: chat cut", and SM-7 is still run [SM-13, AR-24]

### Story 8.6: Hand in: clean-machine run and the checklist

As the examiner,
I want the handed-in repository to start cleanly on a machine that has never run it and to contain no clips or secrets beyond the samples,
So that I can run and assess it exactly as the README says.

**Slice:** repo level `README.md` (Licences and Next phase sections), `.env.example`, `docs/evaluation/` (results table); backend `backend/tests/test_env_example.py` `[ASSUMPTION: automated check]`
**Requirements:** AR-36, SM-10, NFR-4, NFR-7, NFR-8, SM-9, SM-11, SM-12, SM-1–SM-13 (summary)

**Acceptance Criteria:**

**Given** a machine that has never built AIcoach `[ASSUMPTION: if no second machine is available, the target laptop after removing all AIcoach containers, images, volumes and build cache and cloning into a new folder]`
**When** the author clones the hand-in commit, runs `copy .env.example .env` with no edits and `docker compose up --build`, and follows only the README
**Then** a complete result appears in mock mode for `samples/ee-01.mp4` [SM-10, NFR-4, FR-15]
**And** the Playwright smoke test from Story 8.3 passes against that stack
**And** the date, machine, OS and commit hash are recorded in `docs/evaluation/`

**Given** the hand-in commit
**When** `git ls-files "*.mp4" "*.mov"` is run
**Then** it lists only paths under `samples/` [AR-36, NFR-8]

**Given** `.env.example`
**When** `uv run pytest backend/tests/test_env_example.py` runs
**Then** every variable from setup-guide §3 and every field of the app settings has a key in `.env.example` with a safe default, `JWT_SECRET` and `OPENROUTER_API_KEY` are empty, `LLM_MODE=auto`, `EVENT_DETECTOR=wrist`, `FEATURE_HISTORY=false`, and `FEATURE_CHAT` matches the 2026-12-08 decision [AR-36, AR-4, NFR-8]
**And** `git log -p --all` contains no OpenRouter key string `[ASSUMPTION: checked by searching for the key prefix sk-or-]`

**Given** the README's "Licences" section
**When** it is read
**Then** it lists the bundled pose backend and model files with their licences as recorded in `backend/models/MANIFEST.yaml`, states that YOLO-pose is not used, lists SwingNet (CC BY-NC 4.0, off by default via `EVENT_DETECTOR=wrist`) for removal before a paid launch, and lists FFmpeg/x264 (GPL, used as a separate CLI) and, if RTMPose was chosen, the RTMPose body7 weights for licence review before a paid launch [NFR-7]

**Given** the README
**When** the hand-in checklist is ticked
**Then** it links setup-guide §6.1 and §6.3 [AR-36] and has a one-line Next phase pointer to technology.md §5–§8 for public hosting (setup-guide §9)

**Given** the hand-in commit
**When** `uv run pytest`, `uv run pytest -m pg`, the Vitest suite, ESLint and the Playwright smoke test run
**Then** all pass, and the isolation tests (SM-9) and the swing library retention tests (SM-11) from Epic 5 are named in the record with their pass status [SM-9, SM-11]

**Given** `docs/evaluation/` after Stories 8.3–8.5 and this story
**When** the results table is completed
**Then** SM-1 to SM-13 each have one status (pass, fail, not testable, not applicable or not built) and a pointer to their evidence: SM-1–SM-6 from Story 8.4, SM-4's explanation part and SM-10 from Stories 8.3 and 8.6, SM-7, SM-8 and SM-13 from Story 8.5, SM-9 and SM-11 from this story [AR-36]
**And** SM-12 is "pass" with the Epic 7 tests named if `FEATURE_HISTORY` shipped, otherwise "not built (P3 stretch)" [SM-12]
**And** re-checking the competitive claims (PRD OQ5) is not part of this story
