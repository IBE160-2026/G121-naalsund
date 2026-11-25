---
review: adversarial
target: ../ARCHITECTURE-SPINE.md
lens: 'Two units one level down that each obey every AD to the letter but still build incompatibly'
date: '2026-11-25'
---

# Adversarial review: ARCHITECTURE-SPINE.md

**Verdict:** The spine is strong on boundaries (engine purity, table ownership, one result document, one LLM gateway). Most of its holes are in the **seams between the steps of one job**: when the explanation is written and who writes it, deletes racing the worker, what a library row is, and which coordinate space and which thresholds the engine uses. Each of these lets two small agents build parts that compile but don't fit together. None of the fixes needs enterprise machinery. Most are one or two sentences added to an existing AD.

Severity: **critical** = the P1 flow (upload → result → library) breaks at integration. **high** = a PRD success metric (SM) or FR consequence fails, or the work has to be redone. **medium** = a visible bug or rework within a slice. **low** = friction.

Count: 1 critical, 8 high, 12 medium, 5 low.

---

## F1 — critical — The explanation step has two writers, and its status transition is undefined

**Units:** *Worker / engine pipeline* (swings) vs *Explanation writer* (coach), plus the *Analysing / result screen* (frontend).

**How they diverge while obeying the ADs:**
- AD-6's diagram says `running → result: rules done`. Its step list says `… → rules → explanation`. The worker agent flips `status=result` when the engine returns, then runs the explanation. The frontend sees `result`, stops polling, and renders a result with `explanation: null`. The explanation lands later and nobody fetches it.
- AD-9 puts "the explanation" inside `AnalysisResult`, which "is defined in the engine". AD-1 says the engine returns `AnalysisResult`. The coach agent's `ExplanationWriter` loads the row and writes `result.explanation` itself, through its own session (AD-2 says only "the worker calls an `ExplanationWriter`" and says nothing about who persists). The worker also writes `result` at the end. That is a lost update: whichever writes last wins.
- The observation rephrase (FR-13, AD-19) has the same problem. One agent overwrites `observation.text` with the LLM text. Another keeps the template text in place and stores the rephrase elsewhere. The grounding check and the mock label then disagree about which text is "the" observation.
- Rejections: FR-14 says "for a rejection … the explanation does not suggest any fault". That implies rejections may have an explanation, but AD-6 has a rejection stop at its step. One agent runs `explanation` on rejections and the other skips it.
- A non-LLM exception inside the writer (for example a grounding-check bug) is a worker exception, so AD-6's `failed` branch applies. That contradicts "never turns the analysis into `failed`".

**Closing AD wording (amend AD-2, AD-6 and AD-9):**
> `ExplanationWriter` is `async write(result: AnalysisResult) -> ExplanationOut` and never touches the database. `ExplanationOut = {explanation_text, observation_text | None, source: "llm" | "template" | "mock"}`. The engine fills `explanation = None` and `observation.template_text`. The worker alone merges `ExplanationOut` into `AnalysisResult` (`explanation`, `observation.text`) and writes the row once: terminal status, `result` and the final step together, in one UPDATE. Status stays `running` until the `explanation` step has finished. The diagram edge reads `running → result: explanation step done`. The worker catches **any** exception from the writer and uses the template (`source: "template"`). A rejection skips the `explanation` step, and its screen uses the rejection copy from `rules.yaml`.

---

## F2 — high — A band can change the outcome, and "the deciding threshold" means different things

**Units:** *Engine measurements + confidence* (`measures.py`, `confidence.py`) vs *Engine rules* (`rules.py`).

**How they diverge:** AD-12 says the band uses "how far the value is from the deciding threshold". Nothing says which threshold that is, or whether the band can change the outcome.
- Agent A computes the band for each measurement during `measurements`, against the **fault** threshold.
- Agent B computes the fault band in `rules`, against the **potential** threshold, and demotes `verified` with a `low` band to `possible`.

The result: the same value shows "high" on the measurement and "medium" on the fault. SM-5 (high bands more often correct than low) is then measured on a moving definition, and a "low verified" fault, which FR-7 implies can exist, never appears.

**Closing AD wording (amend AD-12):**
> The outcome comes from thresholds only: `value ≥ fault` → `verified`, `≥ potential` → `possible`, otherwise `absent`. A band never changes an outcome. The deciding threshold is the boundary nearest to the value of the outcome's interval. A fault's band **is** its deciding measurement's band, computed by the same single function `confidence.band(measurement, rule, events, visibility, fps)` after `rules`, and then capped. Measurements that no active rule uses get a band from their own threshold in `rules.yaml`. `possible` faults carry a band; `absent` faults don't.

---

## F3 — high — Deletes race the running job

**Units:** *Swing library delete* (`DELETE /api/clips/{id}`, `DELETE /api/analyses/{id}`, `DELETE /api/me`) vs *Analysis worker* (+ the ffmpeg playback step) vs *Chat POST* (30 s LLM call).

**How they diverge:** AD-8 has the database commit first and the files removed after. AD-5 runs a job for up to 10 min. Nothing coordinates the two.
- If the player deletes the clip while the job is `running`, the engine (in another process) loses `original.mov` mid-decode, and the job ends as `failed` on a row whose clip is gone. "Try again" then violates AD-6's "clip still stored".
- If the player deletes the analysis while it is running, the worker later writes `users/{u}/analyses/{a}/keyframes/*.jpg` and `playback.mp4` after the file cleanup. These are orphans until the next restart, which breaks SM-11 ("a deleted swing clip no longer exists on disk") in a demo.
- A worker that UPSERTs its final write brings back a deleted row.
- "Delete clip, keep analysis" on a `queued` analysis leaves a queued job with `clip_id = NULL`.
- A chat POST that inserts its answer after the analysis was deleted hits a foreign-key error and returns a 500.

**Closing AD wording (add to AD-8):**
> Deleting a clip or an analysis whose analysis is `queued` or `running` returns `409 analysis_in_progress`, and the UI disables delete while analysing. Account deletion is always allowed. The worker ends every job with a conditional update (`UPDATE analyses … WHERE id = :id AND status = 'running'`). If that updates 0 rows, the worker deletes everything it wrote for that job through FileStore. `POST /api/analyses/{id}/retry` returns `409 clip_deleted` when `clip_id` is NULL. A chat insert whose analysis has disappeared returns `404 not_found`.

---

## F4 — high — "Library row" has no defined identity, shape or main-finding rule

**Units:** *Backend list API* (`GET /api/clips`) vs *Frontend library row*, plus *Result-screen headline*.

**How they diverge:** FR-19 and AD-8 need three kinds of row: a clip with an analysis, a "clip deleted" row (an analysis whose `clip_id` is NULL, so there is **no clip**), and an "Analysis deleted" row (a clip with no analysis). The endpoint is `/api/clips`, so the backend agent lists clips and leaves out "clip deleted" rows. Or it includes them and keys rows by `analysis_id`, while the frontend keys rows by `clip_id` and links "open" to `/clips/{id}`. "Newest first" can sort on clip time or analysis time.

AD-9 says `main_finding` is computed on the server but defines no rules for:
- which fault wins when two are verified
- what shows for `queued` / `running` / `failed`
- whether the value is stored or derived

The result-screen agent picks `faults[0]` as its headline, so the library and the result screen name different faults.

**Closing AD wording (amend AD-9 and the endpoint seed):**
> `GET /api/clips` returns `LibraryRow {row_id, clip_id | null, analysis_id | null, created_at (the clip's upload time; for a "clip deleted" row the analysis creation time), status | null, has_playback, main_finding: {kind: "fault" | "no_fault" | "cannot_analyse" | "analysing" | "failed" | "analysis_deleted", label}}`, newest first by `created_at`. `row_id` is `clip_id` if there is one, otherwise `analysis_id`. The engine sets `AnalysisResult.main_finding` (the verified fault with the highest band, ties broken by `rules.yaml` order; otherwise `no_fault`). The library row and the result headline both read it. Neither recomputes it.

---

## F5 — high — The coordinate space of overlays and measurements is undefined (rotation, aspect, crop)

**Units:** *Pose adapter / VideoReader* vs *Measurements* vs *Key-frame writer + frontend SVG overlay*.

**How they diverge:** AD-13 says "image-normalised x and y" and AD-17 says "normalised image coordinates". Three gaps:
- **Rotation:** an iPhone portrait clip carries rotation metadata. The OpenCV adapter decodes it with auto-orientation on (as in recent OpenCV), but the key-frame writer saves the raw frame, or the other way round. AD-15's ffmpeg `playback.mp4` always comes out upright. The overlays are then drawn 90° off.
- **Aspect:** MediaPipe normalises x by width and y by height separately. The measurements agent computes Euclidean distances and angles (spine tilt in `deg`) straight on those coordinates, so the values depend on the clip's aspect ratio, which is exactly what FR-6 is meant to prevent. The RTMPose adapter returns pixels and divides by its own crop size.
- **Crop:** if pose runs on a person crop, the coordinates are relative to the crop, not to the stored JPEG.

**Closing AD wording (amend AD-13 and AD-17):**
> The VideoReader adapter applies the rotation metadata once, at decode. Every frame, `PoseSequence`, key-frame JPEG and overlay is in **upright display orientation of the full frame**. `PoseSequence` carries `frame_w` and `frame_h` in pixels. Coordinates are `x/frame_w` and `y/frame_h`, with the origin at the top left. Distances and angles are computed only after converting to pixels, through one helper `to_px()`. Overlay geometry is normalised to the stored key-frame JPEG, which keeps the full frame and the aspect ratio (it may be scaled, never cropped).

---

## F6 — high — The grounding check's allowed set depends on what CoachFacts contains

**Units:** *CoachFacts projection* (`coach/facts.py`) vs *Grounding check* (`coach/grounding.py`), used by *Explanation* and *Chat*.

**How they diverge:** AD-19 says the text may name "only the faults … in `facts`". The facts agent includes every checked fault with its outcome, because chat needs to answer "what did you check?" and FR-12 lists the faults checked. The grounding agent then lets anything in `facts` through. An explanation saying "you may have early extension" on a `no_fault` result passes, which breaks FR-12 and FR-14 ("names none of the faults") and SM-3/SM-7. Alternatively, the facts agent includes only verified faults, and chat can no longer say what was checked. Separately, numbers from `rules.yaml` drill text ("3 sets of 10") are not `display` values, so a correct template explanation fails its own check, and mock mode falls back to … the same template.

**Closing AD wording (amend AD-19):**
> `CoachFacts` lists every fault with its outcome and band. The allowed set depends on `kind`. For `explanation`: name verified faults only, plus their causes, drills and mobility exercises. For `observation`: name only the observation's measurement. For `chat`: may name possible or absent faults only with their outcome word ("possible", "not found"), and never with a drill. Allowed numbers are the `display` values plus the numbers inside `rules.yaml` drill and exercise text that `facts` carries. Evidence IDs (`E3`) are not numbers. `rules.yaml` templates are checked by the same function in a startup/CI test, so a template can never fail at runtime.

---

## F7 — high — Upload validation is split between the route and the engine with no line between them

**Units:** *Upload route* (`POST /api/clips`) vs *Engine ingest* (inside `pose`).

**How they diverge:** AD-16 says a "wrong format" or a clip "over 15 s" gets a 4xx with no row, while "can't be decoded" or "under 30 fps" becomes a stored rejection. AD-6 says the ingest checks "decode, duration, fps under 30 …" run in `pose`.
- One agent's "format" check is the file extension; the other's is `ffprobe format_name`. A `.mov` holding ProRes, or an HEVC stream OpenCV can't read, is a 4xx for one and a rejection for the other.
- Duration is checked twice, with two readers: route ffprobe container duration vs engine frame count / fps on a variable-frame-rate clip. A 14.9 s clip is accepted by the route and then rejected as "too long" by the engine, with a reason code that has no filming-guide step.
- If ffprobe fails outright, both "no row" and "rejection" are defensible.
- The route stores `fps` on the clip, the engine computes its own, and the two drive the 30/120 caps differently.

**Closing AD wording (amend AD-15 and AD-16):**
> The route owns exactly these checks, in this order: library count (fast pre-check, before streaming) → extension ∈ {mp4, mov} → ffprobe finds a video stream → ffprobe `format.duration ≤ 15.0 s`. Any failure returns 4xx with no row and the temp file deleted. Everything else (decodability, fps, view, framing, swing count) belongs to the engine and becomes a `rejection`. The engine never re-checks extension or duration. fps has one source: the engine's VideoReader, which records it in `AnalysisResult`. The route stores no fps.

---

## F8 — high — Playback is missing for rejected or still-processing clips, and has no state

**Units:** *Worker playback step* (ffmpeg) vs *Library row / video endpoint / player*.

**How they diverge:** AD-15 says playback is made "after the analysis ends". The worker agent runs ffmpeg **after** the terminal status is set, so for a few seconds `GET /api/clips/{id}/video` returns 404. The frontend reads 404 as "deleted / not yours" (AD-7) and shows the "clip deleted" state. A clip rejected as undecodable may not transcode at all, which breaks SM-11 ("every uploaded swing clip, including a rejected one, can be played back"). Whether an ffmpeg failure is an analysis `failed` is not defined.

**Closing AD wording (amend AD-15):**
> The playback transcode is part of the job and runs before the terminal write (F1). It does not belong to any of the five step IDs and is not shown in the step log. If it fails, the status does not change; `clips.playback_ready` is set to false. The video endpoint returns `409 playback_unavailable` (never 404) when the clip exists but has no playback, and `LibraryRow.has_playback` drives the player. If ffmpeg cannot transcode, the original is served when its codec is H.264. Otherwise the row says "Playback unavailable".

---

## F9 — high — Two schemas, or two loaders, for `rules.yaml`

**Units:** *Engine rule-table schema* (AD-1: the engine owns "the rule-table schema") vs *Coach templates / jargon blocklist / medical notice* vs *Settings limits*.

**How they diverge:** `rules.yaml` holds both engine data (thresholds, caps) and coach data (feel cues, the blocklist, the medical notice, the chat refusal text). The engine agent defines `RuleTable` with `extra="forbid"` and only engine fields. The coach agent writes `coach/rules_loader.py` with its own model for the coach keys. Now one file has two validators, and the engine's forbid stops the app at startup ("a file that doesn't pass stops the app"). Or the engine uses `extra="ignore"` and a typo in a coach key passes silently. Separately, AD-23 names both "settings and `rules.yaml`" as the source of limits. One agent puts the word limits in settings and another in `rules.yaml`. The engine cannot read app settings (AD-1), so the 30/120 fps floors **must** be in `rules.yaml`, while the upload agent reads them from settings.

**Closing AD wording (amend AD-11 and AD-23):**
> `rules.yaml` has one schema, `RuleTable` in the engine, with typed sections `faults`, `observations`, `confidence`, `coach` (templates, blocklist, notices, refusals) and `guide_steps`, and `extra="forbid"` at every level. One function, `aicoach_engine.load_rules(path)`, parses it. The app calls it once at startup and passes the object to the slices, and nothing else opens the YAML. The ownership of each limit is fixed: `rules.yaml` holds the fps floors and word limits; settings hold 15 s, mp4/mov, 300 MB, 50 clips, and the `FEATURE_*` / `LLM_*` flags. `/api/config` returns the union.

---

## F10 — medium — The chat answer's shape, its "Based on" and its citation syntax are undefined

**Units:** *Chat backend* (`POST /api/analyses/{id}/chat`, grounding) vs *Chat UI / explanation renderer*.

**How they diverge:** FR-20 says each answer "ends with a 'Based on:' note". The backend agent has the LLM write `Based on: E1, E3` into the text, and the word count includes it. The UI agent renders a "Based on" footnote from a structured field, so it appears twice (or not at all). Inline citations can be `[E1]`, `(E1)` or bare `E1`. The grounding regex and the UI's pin-link parser are written by different agents. AD-10's "a UI pin shows the item's position number" can mean the index in the whole list or the index on one key frame, so the text says "E3" while the pin on the top frame shows "1".

**Closing AD wording (amend AD-10 and AD-19):**
> The LLM output is structured: `{text, based_on: [evidence_id]}`. `based_on` is not part of `text`, and word limits count `text` only. The only citation syntax inside `text` is `[E<n>]`. One regex, defined in `coach/grounding.py` and mirrored in `frontend/src/modules/coach/citations.ts` under a shared fixture test, parses it. A pin shows `n` from its global ID `E<n>`, never a per-frame index. `chat_messages` stores `{role, text, based_on, source, created_at}`.

---

## F11 — medium — "LLM unavailable", "flag off" and "not yours" are all 404 or undefined

**Units:** *Chat backend* vs *Chat UI* (and the result screen).

**How they diverge:** AD-23 says a flag that is off makes its endpoints return 404, and AD-7 says another player's row returns 404 `not_found`. The UI agent treats any 404 on the chat endpoint as "analysis gone" and redirects to the library. FR-20 says that if the LLM is unavailable the chat is disabled with a plain message, but AD-19 says a failed answer retries and then gives the fixed refusal. Agent A returns 200 + refusal on a timeout. Agent B (the UI) expects an error so it can disable the chat.

**Closing AD wording (amend AD-19 and AD-23):**
> When a flag is off, the endpoint returns 404 with code `feature_disabled`; the UI hides by `/api/config` and never relies on the 404. A failed grounding check gives `200` + refusal (`source: "refusal"`). A transport failure or timeout to the LLM returns `503 llm_unavailable`, the UI disables the chat input with the plain message, and nothing is stored. Chat on a non-`result` status returns `409 chat_not_available`.

---

## F12 — medium — AD-7 forbids the queries the worker and the startup sweep need

**Units:** *Repository story* (strict `user_id` on every function) vs *Worker / startup reset / orphan sweep*.

**How they diverge:** AD-7 says "no query loads these rows by ID alone", but the worker must take "the oldest queued row" across all users, the startup code must mark every `running` row failed, and the sweep must list every file's owning row. Agent A writes strict repos. Agent B either breaks the rule with raw SQL in `worker.py` or adds an optional `user_id=None`, which turns the guard off for every caller.

**Closing AD wording (add to AD-7):**
> System-scope repository functions are allowed only in `swings/repo_system.py` (`claim_next_queued`, `fail_running_on_startup`, `list_all_ids_for_sweep`, `finish_job`). Only `worker.py` and the startup hook may import them, and a test asserts that no `routes.py` imports them. `user_id` is never optional in `repo.py`.

---

## F13 — medium — The 50-clip lock and the account cascade break AD-2

**Units:** *Swings upload* vs *Identity* (owner of `users`).

**How they diverge:** AD-8 says to lock the **users** row with `SELECT … FOR UPDATE` inside the swings upload transaction. AD-2 says another slice touches `users` only through identity's service functions. The swings agent writes a raw `select(User)…with_for_update()`, which breaks AD-2, or calls `identity.service.lock_user()`, which the identity agent never wrote. In the other direction, `DELETE /api/me` (identity) removes swings and coach rows through FK cascade and must remove `users/{id}/` files that swings owns. The identity agent instead calls a swings purge that doesn't exist, or deletes rows one at a time and then the cascade fails.

**Closing AD wording (amend AD-2):**
> Exceptions written down: (a) `identity.service.lock_user(session, user_id)` exists and is the only way to take the per-user lock; (b) FK `ON DELETE CASCADE`, declared in the child table's owning migration (`clips`, `analyses` → `users`; `chat_messages` → `analyses`), counts as the owner's own path; (c) `DELETE /api/me` commits the user delete, then calls `swings.service.purge_user_files(user_id)`.

---

## F14 — medium — Re-running a failed job leaves stale state, and a timeout does not stop the process

**Units:** *Retry endpoint* vs *Worker* vs *Analysing screen*.

**How they diverge:** The retry agent flips only `status = 'queued'`. The worker appends step entries to the existing log, so the Analysing screen shows `pose ✓ events ✗ pose …`. Key frames from the earlier attempt stay. Separately, `future.result(timeout=600)` marks the job `failed`, but the `ProcessPoolExecutor` process keeps running. With `max_workers=1` it blocks the next job and can still write key frames for the failed analysis.

**Closing AD wording (amend AD-5 and AD-6):**
> Retry atomically sets `status=queued` and clears `steps`, `result`, `error` and timestamps. At the start of a run, the worker deletes the analysis's key-frame directory. On timeout, the worker kills the pool's process, makes a new pool, and only then writes `failed`. The step log column is `steps: [{id, state: "pending" | "running" | "done" | "skipped" | "stopped", started_at, ended_at}]`, always all five IDs in fixed order.

---

## F15 — medium — Concurrency of the job claim depends on how uvicorn is started

**Units:** *Backend Dockerfile / Compose* vs *Worker claim*.

**How they diverge:** An agent tuning the image sets `uvicorn --workers 2`, a common default. Each process starts its own in-process worker (AD-5), so two analyses run at once, both startup hooks mark the other process's `running` rows `failed`, and a non-atomic `SELECT` then `UPDATE` claim runs the same row twice.

**Closing AD wording (amend AD-5):**
> The backend always runs as exactly one uvicorn process (no `--workers`). Claiming is one statement: `UPDATE analyses SET status='running' WHERE id = (SELECT id … WHERE status='queued' ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED) RETURNING id`.

---

## F16 — medium — Event frame indices: relative to the window or absolute?

**Units:** *Engine events* (decodes only the trimmed window, AD-15) vs *Eval harness* (`eval/labels.yaml` event frames) and *key-frame naming*.

**How they diverge:** The events agent returns frame indices relative to the trimmed window. The eval agent compares them with labels counted from the start of the clip. Every clip then misses FR-6's ±1 / ±2 frame tolerance by the window offset. On variable-frame-rate clips, "frame index" and "timestamp" also differ.

**Closing AD wording (amend AD-14 and AD-24):**
> Event frames in `EventDetector` output, `AnalysisResult` and `labels.yaml` are 0-based indices into the full decoded stream from the VideoReader, plus `t_ms`. The trimming offset is applied inside the engine before anything leaves a step.

---

## F17 — medium — Fault and measurement names: IDs in the result, labels kept in the UI

**Units:** *Engine result* vs *Result screen / library row*, across a change to `rules.yaml`.

**How they diverge:** `AnalysisResult` stores `fault_id: "over_the_top"`. The frontend agent maps IDs to names in a TypeScript constant ("Over the top"). That is coaching copy in a component (Consistency → Copy), but no AD forbids it outright. When the over-the-top → sway swap (OQ4) edits `rules.yaml`, older results either lose their names or show the new copy for an old verdict.

**Closing AD wording (amend AD-9):**
> `AnalysisResult` copies, at analysis time, the display `label` (and copy text) of every fault, measurement, cause, drill, exercise and rejection reason it references. The frontend shows only those snapshotted labels and has no ID → label maps.

---

## F18 — medium — Rejection reason → filming-guide step has no shared key

**Units:** *Filming guide* (static frontend content) vs *`rules.yaml` reason map / rejection screen*.

**How they diverge:** The guide agent anchors its steps `#step-3`. The rules author maps `not_dtl → "camera-position"`. The rejection's "see guide" link goes nowhere. AD-22 bars the frontend from reading `rules.yaml`, so only the API can carry the link.

**Closing AD wording (amend AD-6 and AD-11):**
> Guide steps are a fixed slug enum in `rules.yaml` (`view`, `height`, `distance`, `stability`, `fps`, `framing`, `one_swing`, `light`), validated by the schema. Each rejection reason in `AnalysisResult` carries its `guide_step` slug. The guide page uses exactly these slugs as element IDs, and a Vitest test checks the slugs against `/api/config.guide_steps`.

---

## F19 — medium — OpenAPI types turn into `unknown` at the JSONB boundary

**Units:** *Analysis GET route* vs *Frontend result screen* (AD-21: types are generated, never hand-written).

**How they diverge:** The route agent declares `result: dict | None` because the column is JSONB. `openapi-typescript` then produces `Record<string, unknown>`. The frontend agent casts it to a hand-written `type AnalysisResult = …`. That obeys the letter ("schema.d.ts never written by hand") but drifts from the engine model. Separately, the frontend agent can't regenerate types while the backend is down.

**Closing AD wording (amend AD-21):**
> Response models reference the engine's `AnalysisResult` (and every nested model) directly; `dict` and `Any` are forbidden in response models. `uv run python -m app.export_openapi` writes a committed `frontend/openapi.json`, and `npm run gen:api` generates `schema.d.ts` from that file. Hand-written domain types in `frontend/src` fail lint. A stored result whose `schema_version` is not the current one returns `409 result_outdated` instead of a 500.

---

## F20 — medium — Parallel stories create diverging Alembic heads

**Units:** Any two stories that add tables or columns in parallel (for example *coach `chat_messages`* vs *swings `playback_ready`*).

**How they diverge:** Each agent runs `alembic revision` from the same head. After the merge, the history has two heads, and the `alembic upgrade head` run when the backend starts fails, so the app doesn't start.

**Closing AD wording (amend Consistency → DB changes):**
> One migration per story, rebased onto the current head before merge. A pytest check asserts that `alembic heads` has exactly one entry and that `upgrade head` → `downgrade base` → `upgrade head` runs cleanly on Postgres.

---

## F21 — medium — The result screen can't tell a template explanation from an LLM one

**Units:** *Result-screen mock label* vs *Explanation writer*.

**How they diverge:** The UI agent shows the "mock mode" label from `/api/config.mock_mode`, which describes the system now. A result explained in mock mode last week then shows no label once a key is set. A result that fell back to the template after a failed grounding check shows no label in either mode.

**Closing AD wording:** covered by F1's `ExplanationOut.source`. Add to AD-23:
> The per-result label is driven by `explanation.source`, not by `/api/config.mock_mode`. The global flag is used only for the app banner.

---

## Low

- **F22 — low — Who must send the CSRF header.** The *auth* agent leaves sign-in and sign-up out of the `X-Requested-With` check, while the *frontend fetch client* sends it everywhere. Or the *upload* agent uses raw `XMLHttpRequest` (for upload progress) and forgets the header. **Fix (AD-20):** "Required on every non-GET/HEAD `/api` request, auth included, checked in one middleware. The shared fetch client and the upload XHR both set it."
- **F23 — low — A stale JWT after account deletion.** The *auth dependency* decodes the JWT without loading the user. After `DELETE /api/me`, another tab's cookie still passes, and an upload fails on the FK with a 500. **Fix (AD-20):** "The auth dependency loads the `users` row on every request. A missing user returns 401 and clears the cookie."
- **F24 — low — The engine output directory vs FileStore.** The *engine* agent writes key frames straight to `DATA_DIR/users/…` (AD-1 lets the caller pass a directory), while the *FileStore* agent expects every write to go through `FileStore.put`. That blocks the planned Supabase implementation. **Fix (AD-4):** "The worker passes the engine a per-job scratch directory under `DATA_DIR/tmp/{analysis_id}`. The worker then imports the outputs through FileStore and deletes the scratch directory."
- **F25 — low — Visibility semantics differ between pose backends.** MediaPipe `visibility` and RTMPose keypoint `score` are not on the same scale, so visibility cut-offs tuned in `rules.yaml` on one backend change the bands after the spike switches backends. **Fix (AD-13):** "Each adapter maps its score into the canonical 0–1 visibility with a calibration that lives in the adapter. Confidence thresholds are re-tuned whenever `POSE_BACKEND` changes, and the backend name is recorded in `AnalysisResult` next to the rule-table hash."
- **F26 — low — The upload holds the per-user lock while streaming.** An agent that follows AD-8 literally opens the `FOR UPDATE` transaction, then streams 300 MB inside it, and a delete in another tab blocks until the upload finishes. **Fix (AD-16):** "Pre-check the count, stream to a temp file outside any transaction, then lock, re-check, insert and move the file in one short transaction."

---

## Not findings (checked, holds)

- Table ownership, apart from the F13 exceptions, and the dependency direction coach → swings are unambiguous.
- AD-12's caps in one final function, and AD-18's single gateway, leave no second path for a band or a model call.
- AD-23's runtime flags via `/api/config` leave the frontend no build-time flag to diverge on.
