---
title: AIcoach PRD
status: final
created: 2026-11-03
updated: 2026-11-25
---

# PRD: AIcoach

## 0. Document Purpose

This PRD defines the AIcoach MVP due **2026-12-15**. It serves two audiences at once: the IBE160 course (graded deliverable, solo project) and the first step of a real product. It is the input for UX design, architecture, and epics/stories.

It builds on the revised product brief (`docs/product-brief/brief.md`, 2026-11-02), the teacher feedback on the first brief, the competitive research (`docs/research/competitive-ai-golf-swing-coach-apps-2026-11-02/`) and the technical 2D-pose research (`docs/research/technical-2d-pose-golf-swing-fault-detection-2026-11-03/`).

**Revision 2026-11-25.** Reconciled with the finalized UX design (`docs/_bmad-output/planning-artifacts/ux-designs/ux-AIcoach-2026-11-11/`) and the teacher feedback on the PRD (`docs/prd/tilbakemelding-prd.md`). Main changes: grounded AI coach chat is in the MVP (§4.9); every swing clip goes into the swing library automatically, with one consent at sign-up (§4.8, §6.1); the unverified observation is built from a closed list of extra measurements (§4.5); sway has a reserve row in the rule table (§4.4); the cut order has checkpoint dates (§8.1).

Terms in §3 Glossary are used verbatim throughout. Each feature in §4 contains its FRs, which are numbered globally. Inferred points are tagged `[ASSUMPTION]` inline and indexed in §12. Implementation detail (pose models, filters, threshold sources, licences) lives in `addendum.md`.

## 1. Vision

Good golf coaching is expensive and hard to reach. Most golfers get a lesson now and then, or none, and try to fix their swing from videos and guesswork. Because feel and reality often disagree in golf, unguided practice can reinforce the very fault the player is trying to fix. Existing swing apps measure well but leave the player to interpret graphs and lists of deviations.

AIcoach is a web app that acts as the player's coach. The player films a swing with a phone, uploads it, and gets back what a good coach would say: **what the fault is, where it comes from, how sure the app is, and what to practise** — one drill and one mobility exercise. The long-term goal is to replace the coach for golfers who cannot afford or access one, and to grow toward coaching at every level.

The MVP proves the core claim on a narrow, honest base: from one down-the-line phone video, AIcoach detects three common faults with verified rules, explains the cause as a fault chain, shows a confidence level on every measurement, and refuses to guess when the video cannot support an answer. Honesty is the product's edge: among roughly a dozen competing apps reviewed (desk research, not hands-on), none shows per-measurement confidence or evidence for each link of its cause-and-effect reasoning.

The coach voice matters as much as the numbers: AIcoach tells the player what they probably feel and what the video actually shows, then gives one thing to practise.

## 2. Target User

**Primary:** golfers between **+2 and 15 handicap** who want to improve and lack regular access to a coach. They practise at the driving range or in a net, with a phone.

### 2.1 Jobs To Be Done

- **Functional:** "Tell me what is actually wrong with my swing and what to practise next session — without me having to interpret graphs."
- **Emotional:** "I want to trust that I'm not grooving the wrong thing. Tell me when you're unsure."
- **Contextual:** "I'm at the range with a phone and a few minutes; filming and getting an answer must fit into a practice session."
- **Economic:** "I want coach-quality direction without paying 600–1200 NOK per lesson."

### 2.2 Non-Users (v1)

- Beginners who cannot yet make a repeatable full swing — the three faults and their drills assume a functioning swing. They are not blocked, but the MVP is not designed for them.
- Elite players seeking launch-monitor-grade precision — they will be served later as a complement to their coach.
- Anyone using the app during a competitive round — the Rules of Golf restrict advice; AIcoach is a practice tool only.

### 2.3 Key User Journeys

- **UJ-1. Rory finds out why he keeps hitting it thin.**
  - **Persona + context:** Rory, 34, 11 handicap, practises twice a week at the range after work, has not had a lesson in three years. He's been fighting thin and blocked shots.
  - **Entry state:** has an account, signed in on his phone browser, connected to the same Wi-Fi as the laptop running AIcoach; the swing clip is on his phone.
  - **Path:** opens the filming guide on his phone, props the phone at hand height on his bag 3 m behind the hands line, films at 120 fps → hits a 7-iron → trims nothing, uploads the clip from the phone browser → sees a progress state while the analysis runs.
  - **Climax:** the result shows **Early extension**, with the hip movement measured toward the ball, a key frame at address and at impact with the hip line drawn, **confidence: high**, the fault chain "restricted hip rotation → hips move toward the ball → early extension", a plain-language explanation with the feel cue "it may feel like you stay down, but at impact your hips have moved toward the ball", the wall drill and the 90/90 hip rotation exercise.
  - **Resolution:** Rory asks the coach why it feels like he stays down when he doesn't; the answer points to the hip measurement and the impact frame. He does the wall drill for the rest of his range session and plans to film again next session.
  - **Edge case:** if the hips were only partly visible in the impact frame, the same fault is shown with **confidence: low** and a note on what to film better.

- **UJ-2. Rory's video is rejected — and he learns how to film.**
  Rory films from the face-on side by mistake, at 30 fps, with his feet cut off. AIcoach does not produce a guessed fault. It shows **"Cannot analyse"**, names the reasons (wrong camera angle, body out of frame), and links back to the specific steps of the filming guide. He re-films and UJ-1 follows.

- **UJ-3. Nelly's swing has a fault AIcoach does not cover.**
  Nelly, 4 handicap, has a reverse pivot — none of the three verified faults. AIcoach reports **"No verified fault found"** rather than forcing one of the three onto her, and lists what it checked. Because her hips move away from the target in the backswing past the sway threshold, it shows one **unverified observation** ("your hips appear to move away from the target in the backswing"), clearly labelled as unverified with "confirm with a coach", and with no drill prescribed. Had no extra measurement passed its threshold, no observation would be shown.

- **UJ-4. Rory deletes his data.**
  Rory wants to stop using the app. From his account page he deletes one analysis, then his whole account. All his results and key frames are gone, and he can no longer sign in.

- **UJ-5. The examiner runs AIcoach from the README.**
  The course examiner clones the repo, follows the README on an ordinary laptop with no paid accounts or API keys, starts the app in mock-LLM mode, uploads one of the bundled test clips, and gets a complete result.

- **UJ-6. Rory keeps his swings to watch his progress.**
  Rory agreed at sign-up that his swing clips are kept in his swing library, so every clip he sends lands there automatically. Two weeks later, after practising the wall drill, he opens his swing library, finds the first swing clip next to the new one, plays them both, and opens the analysis attached to each. He deletes an old, badly filmed clip and chooses to delete its analysis too.

- **UJ-7. Rory asks the coach about his result.**
  On his early-extension result, Rory asks "Why does it feel like I'm staying down when I'm not?". The coach answers in two or three sentences, citing the hip measurement and the impact frame. He then asks "Should I change my grip as well?"; the coach says it did not measure his grip in this clip, so it can't tell him, and suggests sticking with the wall drill and asking a coach about grip.

## 3. Glossary

- **Visitor** — someone using AIcoach without being signed in.
- **Player** — a person with an AIcoach account who uploads swing clips.
- **Examiner** — the course examiner who runs AIcoach from the README (UJ-5).
- **Swing clip** — one video file containing one golf swing, filmed down the line. One swing clip produces at most one analysis.
- **Swing library** — a player's private collection of every swing clip they have sent, each linked to its analysis (result or rejection). Swing clips enter it automatically, under the consent given at sign-up, and stay until the player deletes them.
- **Library consent** — the one required checkbox at sign-up: the player acknowledges that every swing clip they send is stored in their swing library on the AIcoach server until they delete it. Storing clips is part of the service, so the legal basis is the service agreement (contract), not consent in the GDPR sense; the checkbox records that the player was told.
- **Down the line (DTL)** — camera view from behind the player, pointing along the target line. The only accepted camera view in the MVP.
- **Face-on** — camera view from in front of the player. Not accepted in the MVP.
- **Filming guide** — the in-app instructions for recording a usable swing clip.
- **Analysis** — the processing of one swing clip, and its stored outcome: either a result or a rejection.
- **Result** — the player-facing outcome of a successful analysis: zero or more verified faults, at most one unverified observation, and an explanation.
- **Rejection** — an analysis outcome stating "Cannot analyse", with reasons and filming tips. A rejection never contains faults.
- **Swing event** — a detected moment in the swing: address, top, impact (finish optional).
- **Key frame** — a still image from the swing clip at a swing event, with the relevant body lines drawn.
- **Measurement** — a numeric value derived from the pose in the swing clip (e.g. hip movement toward the ball, change in posture angle). Every measurement has a confidence band.
- **Confidence band** — one of **high / medium / low**, attached to every measurement and every verified fault.
- **Rule table** — the fixed, configurable set of rules that decide whether a verified fault is present, plus each fault's cause, drill and mobility exercise.
- **Potential threshold / fault threshold** — the two configurable limits per rule-table fault. A measurement past the fault threshold makes a verified fault; one between the potential and fault threshold makes a possible fault; one short of the potential threshold means the fault is absent.
- **Active rule table** — the three verified faults in use at a given time: early extension, loss of posture and over the top, or sway in place of over the top after a swap (§4.4).
- **Verified fault** — a fault decided by the rule table. MVP set: **early extension, loss of posture, over the top**; **sway** is the reserve (§4.4).
- **Possible fault** — a fault from the rule table whose measurement lies between the potential threshold and the fault threshold. Shown with its measurement, confidence band and the label "possible", but no drill or mobility exercise. A possible fault is not a verified fault and does not count as a reported fault.
- **Extra measurement** — a measurement on a fixed, configurable list that is not a verified fault (initially sway while it is the reserve, §4.5). Each has its own threshold and text template, and is the only input an unverified observation may use.
- **Unverified observation** — a remark about the swing built from one extra measurement that passed its threshold. Always labelled unverified; never has a drill or mobility exercise.
- **Fault chain** — the cause → mechanism → fault sequence for a verified fault. Each link shows the measurement, key frame and confidence band that support it.
- **Feel cue** — one sentence contrasting what the player probably feels with what the key frame shows, e.g. "It may feel like you stay down, but at impact your hips have moved toward the ball."
- **Test set** — all labelled swing clips, filmed and labelled by the author, including the bundled examples. It is split into the tuning set and the evaluation set.
- **Tuning set / evaluation set** — two disjoint groups of labelled swing clips. Rule thresholds are adjusted only on the tuning set; success metrics are measured only on the evaluation set.
- **Drill** — a practice exercise from the fixed library, linked to one verified fault.
- **Mobility exercise** — a generic body exercise from the fixed library, linked to the cause of one verified fault. Not medical advice.
- **Explanation** — plain-language text describing the result, generated only from the analysis data.
- **Coach chat** — questions and answers about one result, grounded only in that analysis (§4.9).
- **Analysis history** — the list of a player's analyses, including those whose swing clip was deleted (stretch, FR-16).
- **Mock mode** — running AIcoach with a stand-in for the language model, requiring no keys or network.

## 4. Features

### 4.1 Account and Data Ownership

**Description:** A player creates an account with email and password, signs in, and owns their data. Each player's swing clips, analyses and results are private. The player can delete a single analysis or their whole account. Realizes UJ-1, UJ-4, UJ-6.

**Functional Requirements:**

#### FR-1: Create account and sign in
A visitor can create an account with email and password after giving the library consent, and a player can sign in and sign out. Realizes UJ-1, UJ-6.

**Consequences (testable):**
- An account cannot be created unless the library consent is ticked; the box is unticked by default.
- The sign-up screen states what is stored (swing clips, results, key frames, chat) and that the player can delete any of it.
- Registering with an email already in use is refused with a clear message.
- Passwords are never stored in plain text.
- Upload, results, history, the swing library and the coach chat are reachable only when signed in.

#### FR-2: Private data
A player can see only their own analyses and results. Realizes UJ-1.

**Consequences (testable):**
- Requesting another player's analysis by ID (URL or API) returns "not found" or "forbidden", never the data.

#### FR-3: Delete analysis and account
A player can delete any of their analyses, and can delete their account. Realizes UJ-4.

**Consequences (testable):**
- After deleting an analysis, its result, key frames and coach chat are no longer retrievable; its swing clip stays in the swing library.
- Deleting an analysis asks for confirmation first.
- After deleting the account, all the player's analyses, results, key frames, coach chats and swing clips are removed and the player cannot sign in.

**Out of Scope:** password reset by email, social login, two-factor authentication. `[ASSUMPTION: email password reset is not needed for the MVP]`

### 4.2 Filming Guide and Upload

**Description:** Before uploading, the player can open a filming guide designed for use on a phone at the range. It covers camera view, position, distance, frame rate and framing. The player uploads one swing clip from the phone or computer browser. Realizes UJ-1, UJ-2.

**Functional Requirements:**

#### FR-4: Filming guide
A player can view a filming guide that states: DTL view only; camera at hand height at address, level, on or parallel to the hands line; about 2.4–3.7 m (8–12 ft) away; on a tripod or stable surface; 120 fps or higher recommended; whole body and club in frame for the full swing; one swing per clip; good light. Realizes UJ-1.

**Consequences (testable):**
- The guide is readable on a phone screen without horizontal scrolling.
- Each rejection reason (FR-8) links to the guide step that addresses it.

#### FR-5: Upload swing clip
A player can upload one swing clip in mp4 or mov format, up to 15 seconds long. Realizes UJ-1.

**Consequences (testable):**
- Files of another format, or longer than 15 seconds, are refused before analysis with a message stating the limit.
- Upload works from a mobile browser.
- The player sees that the analysis is in progress until a result or rejection is ready.
- When the player's swing library holds 50 swing clips, a new upload is refused with a message to delete a clip first (FR-19).

**Notes:** the brief's filming instruction ("hip height") is superseded by the technical research's "hand height".

### 4.3 Swing Analysis

**Description:** AIcoach estimates the player's body pose in each frame of the swing clip, detects the swing events, and computes the measurements the rule table needs. Every measurement gets a confidence band. The analysis can be run and tested without the web app and without the language model. Realizes UJ-1, UJ-2, UJ-5.

**Functional Requirements:**

#### FR-6: Pose, swing events and measurements
The system can find the swing within the swing clip, detect address, top and impact, and compute the measurements needed for the three verified faults. Realizes UJ-1.

**Consequences (testable):**
- For each swing clip in the evaluation set, address, top and impact are reported; impact lies within ±1 frame and top within ±2 frames of the labelled frame, at the clip's own frame rate. Address is the last still moment before takeaway. `[ASSUMPTION: tolerances; confirm on the tuning set]`
- Distances are expressed relative to the player's body size at address, not in pixels, so results do not depend on camera distance.
- The analysis module runs from a command line or test harness on a swing clip without the web app or language model.

#### FR-7: Confidence band on every measurement
Every measurement and every verified fault carries a confidence band (high / medium / low), built from how clearly the relevant body points are visible in the key frames, how far the measurement is from the threshold that decided its outcome, and how clearly the swing events were detected. Realizes UJ-1.

**Consequences (testable):**
- No measurement or verified fault is displayed without a confidence band.
- Swing clips under 120 fps never receive "high" confidence on any measurement.
- Over the top is capped at "medium" while it is measured from the hand path (no club tracking).
- On the evaluation set, verified faults with "high" confidence are correct more often than those with "low" (see SM-5).

#### FR-8: Reject unusable video
The system rejects a swing clip with "Cannot analyse" when it cannot support a result, giving the reasons and filming tips. Reasons include at least: not a DTL view, body or club out of frame, no swing detected, more than one swing, too dark or blurred. Realizes UJ-2.

**Consequences (testable):**
- A face-on swing clip and an out-of-frame swing clip from the test set each produce a rejection, never a fault.
- Swing clips under 120 fps but at least 30 fps are analysed with a visible warning; swing clips under 30 fps are rejected.
- A rejection is stored as an analysis, and its swing clip goes into the swing library like any other (FR-18).

### 4.4 Verified Faults and Fault Chains

**Description:** The rule table decides whether each of the three verified faults is present. For each verified fault found, the result shows the fault chain — cause, mechanism, fault — with the supporting measurement and key frame, one drill and one mobility exercise. Thresholds are configurable starting values tuned on the tuning set, not fixed norms. AIcoach never forces a fault: if none of the three is present, it says so. Realizes UJ-1, UJ-3.

| Verified fault | Measurement | Cause | Drill | Mobility exercise |
|---|---|---|---|---|
| Early extension | Hips move toward the ball from address to impact | Restricted hip rotation | Wall drill | 90/90 hip rotation |
| Loss of posture | Posture (head/shoulder/spine) angle change in the downswing vs address | Weak hip hinge or tight hamstrings | Alignment-stick head drill | Hip-hinge / hamstring mobility |
| Over the top | Hand path in transition above the backswing path | Upper body starts the downswing | Pump drill | Open books |
| *Sway (reserve)* | Trail ankle-to-hip line angle in the backswing vs address | Limited trail-hip internal rotation | Alignment stick at the trail hip: turn without bumping it | Trail-hip internal rotation |

**Functional Requirements:**

#### FR-9: Detect verified faults
The system can decide, using the rule table, whether early extension, loss of posture and over the top are present in a swing clip. Realizes UJ-1.

**Consequences (testable):**
- Each rule-table fault is reported as a verified fault, a possible fault, or absent.
- For a test clip whose measurement is past the fault threshold, the fault is reported as verified; between the potential and fault threshold, as possible; short of the potential threshold, as absent.
- A possible fault gets no fault chain, drill or mobility exercise, and is not counted as a reported fault in SM-1–SM-3.
- Rule thresholds can be changed in configuration without code changes, and are adjusted only on the tuning set.
- Starting thresholds come from a single source (a 2026 Acushnet patent, see addendum §B) and are treated as starting values, not norms.
- Sway is defined in the rule table from the start, so the swap in the §4.4 Notes needs configuration, not new rule work.

#### FR-10: Show fault chain with evidence
For each verified fault found, a player can see the fault chain, the measurement value with its confidence band, and at least one key frame with the relevant body lines drawn. Realizes UJ-1.

**Consequences (testable):**
- Every link of the fault chain shows the measurement, key frame and confidence band it rests on; a cause that cannot be measured from the swing clip (e.g. restricted hip rotation) is labelled "likely cause" and names the measured mechanism that points to it.
- The key frames shown correspond to the swing events the rule uses (e.g. address and impact for early extension).

#### FR-11: Prescribe one drill and one mobility exercise
For each verified fault found, a player can see one drill and one mobility exercise from the fixed library, each with short instructions. Realizes UJ-1.

**Consequences (testable):**
- The drill and mobility exercise shown match the rule-table mapping for that fault.
- Every mobility exercise carries a notice that it is generic guidance, not medical advice, with a recommendation to see a physiotherapist on pain.

#### FR-12: No forced fit
When no verified fault is present, the result says "No verified fault found" and does not show any of the three. Realizes UJ-3.

**Consequences (testable):**
- For a test clip where every rule-table measurement is short of its potential threshold, the result shows "No verified fault found" and lists the faults checked, with no fault chain, drill or mobility exercise, and the explanation names none of the faults.
- Possible faults may still be listed under what was checked, labelled "possible".

**Notes:** At the P1 checkpoint (2026-12-01), the author checks over the top against the SM-1 target on the **tuning set**; if it fails, it is replaced by **sway** as the third verified fault. The evaluation set is used only afterwards, to report SM-1, and never to decide the swap. Until a swap, sway is a reserve: it is not reported as a verified or possible fault, and its measurement is used only as an extra measurement (§4.5). The **active rule table** is the three faults in use at a given time. If two of the three faults fail SM-1 on the evaluation set, the MVP ships with the faults that pass, the failing ones are reported as "possible" only, and the shortfall is documented in the course report. `[ASSUMPTION: fallback when two faults fail]`

### 4.5 Unverified Observation

**Description:** Beyond the rule table, AIcoach can add one observation about the swing, so a player with no verified fault is not left with nothing. It is built from a closed list of extra measurements, each with its own configurable threshold and text template; the language model may only rephrase the template, never choose what to say. It is visually separated from verified faults, labelled "Unverified — confirm with a coach", carries the confidence band "low", and never prescribes a drill or mobility exercise. Realizes UJ-3.

**Functional Requirements:**

#### FR-13: Show unverified observation
A player can see at most one unverified observation per result, clearly separated and labelled, shown only when an extra measurement passes its threshold. Realizes UJ-3.

**Consequences (testable):**
- For a test clip where an extra measurement passes its threshold, the result shows exactly one unverified observation built on that measurement; when none passes, no observation is shown.
- If several extra measurements pass, the one furthest past its threshold is shown.
- An observation can appear both with "No verified fault found" and next to a verified fault.
- The observation's text names only the measurement it is built on and the numbers present in the analysis (same automated check as FR-14).
- An unverified observation always shows the confidence band "low" and never names a drill or mobility exercise.
- An extra measurement that is also a fault in the active rule table is never used for an observation, so an observation cannot repeat a verified fault.
- In mock mode, the template text is shown unchanged.

**Notes:** the initial list is sway (while it is the reserve fault); others may be added from the tuning set. `[ASSUMPTION: list content]` The language model receives measurements only — never the swing clip or personal data (§6.1).

### 4.6 Explanation

**Description:** The result includes a short, plain-language explanation of what was found, why it matters for ball striking, and what to practise. The language model explains; it never decides. It receives only the analysis data and may not add faults, causes, drills or numbers that are not in it. Realizes UJ-1, UJ-5.

**Functional Requirements:**

#### FR-14: Grounded explanation
A player can read an explanation of the result written the way a coach talks: plain language, no jargon, and for each verified fault one feel cue. Realizes UJ-1.

**Consequences (testable):**
- With fixed analysis inputs, the explanation mentions only the verified faults, causes, drills and mobility exercises present in the analysis, and no numbers that are not in it (automated check).
- Each verified fault in the explanation has exactly one feel cue.
- The explanation is at most 150 words and uses none of the terms on a jargon blocklist (e.g. "kinematic sequence", "pelvic thrust", "degrees of spine tilt"). `[ASSUMPTION: 150-word limit]`
- For a rejection or "No verified fault found", the explanation does not suggest any fault.
- If the language model is unavailable, the result is still shown, with a template explanation.

#### FR-15: Mock mode
AIcoach can run end to end in mock mode, with no API keys, paid accounts or network access to a language model. Realizes UJ-5.

**Consequences (testable):**
- Following the README on a clean laptop, the bundled test clips produce complete results in mock mode.
- In mock mode, the coach chat (FR-20) gives fixed sample answers.

### 4.7 History and Comparison *(stretch)*

**Description:** A player can see a list of past analyses and compare two of them on at least one measurement, to see whether a drill is working. Realizes the brief's "practise drill, film again next session" loop. In P1, the swing library (FR-19) already lists every clip with its main finding; analysis history adds the analyses whose swing clip was deleted.

**Functional Requirements:**

#### FR-16: Analysis history *(stretch)*
A player can list their past analyses, newest first, and open any result.

**Consequences (testable):**
- After two completed analyses, the list shows both, newest first, and each can be opened.
- An analysis whose swing clip was deleted still appears, marked "clip deleted".

#### FR-17: Compare two analyses *(stretch)*
A player can choose two analyses and see the same measurement side by side, with both confidence bands.

**Consequences (testable):**
- Measurements with different confidence bands are visibly marked as such, so the player does not read a change into noise.

### 4.8 Swing Library

**Description:** Every swing clip a player sends goes into their private swing library automatically and stays there until the player deletes it. The player agrees to this once, at sign-up (library consent, FR-1); there is no per-clip save choice. The swing library lets the player re-watch their swings over time, each next to its analysis. Realizes UJ-6.

**Functional Requirements:**

#### FR-18: Keep every swing clip in the swing library
Every uploaded swing clip is stored in the player's swing library, linked to its analysis (result or rejection), until the player deletes it or the account. Realizes UJ-6.

**Consequences (testable):**
- After an analysis finishes, its swing clip is in the swing library, including when the analysis is a rejection.
- The result screen states that the clip is in the swing library; there is no save toggle.
- A swing clip is never stored for a player who has not given the library consent (FR-1).

#### FR-19: Browse, play and delete swing clips
A player can list their swing clips (newest first, with date and main finding, or "Cannot analyse" for a rejection), play any of them in the browser, open its analysis, and delete any swing clip. Realizes UJ-6.

**Consequences (testable):**
- Playback works on a phone browser and a laptop browser.
- Deleting a swing clip asks for confirmation and lets the player choose "delete clip, keep analysis" or "delete clip and analysis"; either way the video file is removed from disk.
- After "delete clip, keep analysis", the swing library keeps a row for that analysis marked "clip deleted", with no playback; the analysis can be opened and deleted from that row. The row is still listed in the swing library but does not count toward the 50-clip limit.
- Swing clips are subject to FR-2 (private) and FR-3 (removed with the account).

**Feature-specific NFRs:**
- Swing clips are stored outside the code repository and are never committed to Git.
- A player can store at most 50 swing clips; every clip counts, including rejections (FR-5 refuses the 51st).

**Notes:** the swing library is the natural home for the stretch history and comparison (§4.7) and for next-phase cue memory, which judges progress from later swing clips.

### 4.9 AI Coach Chat

**Description:** On a result, the player can ask the coach questions about that swing. The chat sees only that one analysis — its measurements, confidence bands, key frame labels (which frame shows what, never the images), rule-table outcome, cause, drill, mobility exercise, unverified observation and explanation — and follows the same grounding rules as the explanation (FR-14). The language model explains; it never decides, and the rule table remains the only source of verdicts. When a question cannot be answered from the analysis, the coach says so in one sentence and gives one useful next step. Realizes UJ-1, UJ-7.

**Functional Requirements:**

#### FR-20: Grounded coach chat on a result
A player can ask questions about one result and get short, plain-language answers grounded only in that analysis. Realizes UJ-1, UJ-7.

**Consequences (testable):**
- Chat is available on results (verified fault or "No verified fault found"), never on a rejection, and only once the result exists.
- With fixed analysis inputs, answers mention only faults, causes, drills, mobility exercises and numbers present in the analysis (same automated check as FR-14), and each number is cited.
- Answers never raise a confidence band, never call a possible fault or unverified observation verified, and never prescribe a drill or mobility exercise for them.
- Each answer is at most 80 words, uses none of the terms on the FR-14 jargon blocklist, and ends with a "Based on:" note listing what it used. `[ASSUMPTION: 80-word limit]`
- Questions about something not measured, other swings, pain or injury, use during a competitive round, or other topics are refused in one sentence with one next step; pain questions get only the physiotherapist notice (§6.2).
- The chat is stored with its analysis, shown again when the result is reopened, and deleted with it (FR-3).
- If the language model is unavailable, the chat is disabled with a plain message and the result is unchanged; in mock mode it gives fixed sample answers (FR-15).

**Notes:** the chat's language-model input follows §6.1: analysis data only, never the swing clip, email or other personal data. Cost per question outside mock mode is part of Open Question 2. The competitive research advised keeping free chat out of the MVP; chat was brought in because it is scoped to one analysis and checked like the explanation.

## 5. Cross-Cutting NFRs

- **NFR-1 Performance:** a 10-second swing clip completes analysis in under 2 minutes, and a 15-second swing clip in under 3 minutes, on an ordinary laptop — verified as an acceptance test on the author's target machine (median of 5 runs).
- **NFR-2 Local processing and hosting:** in the MVP, AIcoach runs on a local machine (the author's or examiner's laptop). A phone on the same Wi-Fi network can open the app and upload. Pose estimation runs on that machine; swing clips are not sent to third-party services. Public hosting is next phase.
- **NFR-3 Testability:** the analysis module is runnable and testable in isolation; the labelled test set runs as an automated test suite.
- **NFR-4 Examiner runnability:** installation and start-up follow the README with no paid accounts or keys (mock mode).
- **NFR-5 Mobile-friendly:** filming guide, upload and result screens work on a phone browser.
- **NFR-6 Language:** the user interface and explanations are in English.
- **NFR-7 Licensing:** all bundled models and libraries have licences that permit later commercial use. A non-commercial component may be used in the MVP only as a replaceable fallback, and is listed for removal before any paid launch (see addendum §A).

## 6. Constraints and Guardrails

### 6.1 Privacy and data

- **Isolation:** each player's data is private (FR-2).
- **Retention:** every swing clip is kept in the player's swing library (FR-18). Swing clips, results, measurements, key frames and coach chats are kept until the player deletes them or the account. `[ASSUMPTION: key frames are needed for the result screen and are acceptable to store]`
- **Legal basis and notice:** storing swing clips, results and chats is necessary to provide the service (GDPR legal basis: contract). The library consent checkbox at sign-up, unticked by default, records that the player was told; no account is created without it (FR-1). Registration states what is stored, why, and that the player can delete any of it.
- **Storage limit:** at most 50 swing clips per player (FR-19).
- **Language model:** the explanation, unverified observation and coach chat receive analysis data only — never swing clips, key frames, email or other personal data — unless architecture decides otherwise under Open Question 2.
- **Deletion:** the player can delete any analysis, any swing clip, or the whole account (FR-3, FR-19).
- **Data export** (GDPR right of access/portability) is next phase.
- **Repository:** player swing clips are never committed to Git. Secrets are kept in `.env`; `.env.example` is committed. Test clips in the repo are of the author, with consent to publish.

### 6.2 Safety and honesty

- Every measurement shows a confidence band; AIcoach makes no launch-monitor-grade precision claim.
- Mobility exercises are generic guidance, not medical advice, with a physiotherapist referral.
- AIcoach is a practice tool; it is not for use during competitive rounds.

### 6.3 Cost

- MVP running cost is zero in mock mode. Any real language-model use must have a known, small cost per analysis and per chat question (Open Question 2).

## 7. Non-Goals (Explicit)

- AIcoach is **not a launch monitor** and does not measure club path, face angle or ball flight.
- AIcoach does **not diagnose injuries** or give personalised medical, gym or mobility programmes.
- AIcoach is **not an open chat coach**: the coach chat answers only about one analysis and refuses everything else (FR-20).
- AIcoach does **not report faults outside the rule table as facts**.
- No **native mobile app** in the MVP; it is a web app.

## 8. MVP Scope

### 8.1 In Scope (due 2026-12-15)

**Build and cut order.** If time runs short, cut from the bottom. Each tier starts only when the one above is done and tested. If P1 is not done by 2026-12-01, the coach chat goes back to the next phase and all remaining time goes to P1. If the coach chat is not done by 2026-12-08, it is cut and its question box is hidden. P3 starts only if P2 is done early.
1. **P1 — core, done by 2026-12-01:** account with library consent and private data, filming guide, upload, analysis with confidence bands, rejection, verified faults with fault chains, drill and mobility exercise, unverified observation, explanation, mock mode, swing library, labelled test set (FR-1–15, FR-18–19). The swing library is P1 because every clip is kept: storing, listing and deleting clips is part of the retention promise, not an add-on.
2. **P2 — coach chat, done by 2026-12-08** (FR-20).
3. **P3 — stretch, only if time allows:** history and comparison (FR-16–17).

The last week (2026-12-08 to 2026-12-15) is reserved for evaluation-set testing, the README and the demo.

**Included:**

- Email/password account with library consent; private data; delete analysis and account (FR-1–3)
- Filming guide and upload of one DTL swing clip, mp4/mov, ≤15 s (FR-4–5)
- Local 2D pose, swing events, measurements with confidence bands; rejection of unusable video (FR-6–8)
- Three verified faults with fault chains, one drill and one mobility exercise each; sway as reserve; no forced fit (FR-9–12)
- At most one unverified observation from a closed list, labelled (FR-13)
- Grounded explanation and mock mode (FR-14–15)
- Swing library: every clip kept automatically; browsing, playback and deletion (FR-18–19)
- Grounded coach chat on a result (FR-20)
- Labelled test set and automated tests (NFR-3)
- **Stretch:** history and two-analysis comparison (FR-16–17)

### 8.2 Out of Scope for MVP

- **Face-on video, two-angle capture and 3D pose** — next phase; one angle keeps the MVP feasible solo in six weeks.
- **Chat across several swings or about progress** — next phase; the MVP chat sees one analysis only (FR-20).
- **Cue memory and alternative drills** — next phase; needs several sessions of real use first. `[NOTE FOR PM]` Cue memory is a signature feature in the vision — it should lead the next phase.
- **Rules for more faults** — next phase.
- **Swing score** — next phase, only with a confidence band; risks false precision.
- **Personalised gym/mobility plans** — out; medical and liability concerns.
- **Subscription and payment** — real launch only.
- **TrackMan / launch-monitor data** — next phase (§9).
- **Native app** — later.

## 9. Next Phase (beyond 2026-12-15)

Described for direction, not committed. Order to be decided after the MVP.

- **Launch-monitor data (TrackMan and similar).** A player can attach launch-monitor data (e.g. club path, face angle, ball speed, launch, carry) to a swing clip of the same shot, so AIcoach can link what the body did to what the ball and club did — for example, connecting over the top to an out-to-in club path. Neither research report covered this; only one competitor (DeepSwing, with its own camera-based launch monitor) links ball data to swing faults, and no competitor was found importing TrackMan data. Requires its own research (import formats, shot-to-clip matching) before it is specified.
- **Face-on view and two-angle analysis**, then 3D pose.
- **More verified faults.**
- **Cue memory**: learning which drills and wording change this player's swing, judged from the next swing clips, not from how the swing feels; trying an alternative drill when one does not work.
- **Chat across analyses**: grounded in all of the player's own analyses, so the coach can talk about progress.
- **Swing score** with confidence; **subscription**.

## 10. Success Metrics

Measured on a labelled set of swing clips filmed and labelled by the author, who has five years of experience in high-level golf and tournament play. The clips are split into a **tuning set** and an **evaluation set**; SM-1 to SM-5 are measured only on the evaluation set, which is never used to adjust thresholds.

**Primary**
- **SM-1 Detection:** with at least 4 evaluation-set swing clips per verified fault, the labelled fault is detected in at least 75 % of them. Validates FR-6, FR-9.
- **SM-2 Clean swings:** on at least 3 clean swing clips, "No verified fault found" is reported on at least 2. Validates FR-9, FR-12.
- **SM-3 No forced fit:** on at least 3 swing clips whose main fault is outside the three, none of the three is reported; any observation is labelled unverified. Validates FR-12, FR-13.
- **SM-4 Complete result:** a clear early-extension swing clip produces the full result — fault, measurement, confidence band, fault chain, key frame, drill, mobility exercise, explanation. Validates FR-10, FR-11, FR-14.

**Secondary**
- **SM-5 Honest confidence:** on the evaluation set, "high"-confidence verified faults are correct more often than "low"-confidence ones. Tested only when there are at least 3 verified faults in each of the two bands; otherwise the counts are reported descriptively. Validates FR-7.
- **SM-6 Rejection:** a face-on swing clip and an out-of-frame swing clip each produce a rejection with filming tips. Validates FR-8.
- **SM-7 Grounded, coach-like explanation:** with fixed inputs, the automated check passes — only faults, causes, drills, mobility exercises and numbers from the analysis; one feel cue per verified fault; word limit and jargon blocklist respected. Run against the real language model when a key is configured; in mock mode it checks the template and fixed outputs. Validates FR-14.
- **SM-8 Speed:** 10-second swing clip under 2 minutes, 15-second swing clip under 3 minutes on the target laptop. Validates NFR-1.
- **SM-9 Isolation:** a player cannot open another player's data. Validates FR-2.
- **SM-10 Examiner run:** a complete result in mock mode, following only the README. Validates FR-15, NFR-4.
- **SM-11 Swing library retention:** every uploaded swing clip, including a rejected one, can be played back after sign-out and sign-in; a deleted swing clip no longer exists on disk; no account exists without the library consent. Validates FR-1, FR-18, FR-19, §6.1.
- **SM-12 Comparison (stretch):** two analyses of the same player can be compared on at least one measurement, with both confidence bands shown. Validates FR-17.
- **SM-13 Grounded chat:** with fixed analysis inputs and a fixed question set (on-topic, not measured, other swings, pain, off topic), the automated check passes — only content and numbers from the analysis, no raised confidence, refusals where expected, word limit respected. Same mode rule as SM-7. Validates FR-20.

**Counter-metrics (do not optimize)**
- **SM-C1 Number of faults reported per swing clip** — more faults is not better; pushing detection up by loosening thresholds would break SM-2 and SM-3. Counterbalances SM-1.
- **SM-C2 Number of measurements shown** — competitors overwhelm players with data; AIcoach wins on one clear answer. Counterbalances SM-4.
- **SM-C3 Share of swing clips with "high" confidence** — raising it without real evidence makes the confidence band dishonest. Counterbalances SM-5.

`[NOTE FOR PM]` With 4 evaluation clips per fault, 75 % means 3 of 4 — a fragile sample. The tuning set needs its own clips on top of that. Filming more clips per fault strengthens the evidence if time allows.

## 11. Open Questions

1. Can a qualified coach check the test-set labels, in addition to the author?
2. What does the language model cost per analysis and per chat question outside mock mode, and which model is used? (The unverified observation's input is now settled: extra measurements only, §4.5.)
3. Exact rule thresholds and the body-relative unit for early extension — to be tuned on the tuning set. The loss-of-posture measurement must match how its starting threshold is defined (addendum §B).
4. Does over the top from the hand path reach SM-1, or is sway swapped in?
5. Competitive claims (root-cause chains, grounded chat, per-measurement confidence gap) are due for re-check on 2026-12-01; open leads Macro Golf Performance and Performance Golf SwingScan were not examined.
6. Is the over-the-top mobility mapping (open books) supported by TPI-style screening logic, given its cause is a movement pattern rather than a body limitation?
7. If sway is swapped in as a verified fault, what replaces it on the extra-measurement list, so the unverified observation still has input? To be chosen from the tuning set.

## 12. Assumptions Index

- §4.1 Out of Scope — password reset by email is not needed for the MVP.
- §4.3 FR-6 — swing-event tolerances of ±1 frame (impact) and ±2 frames (top).
- §4.4 Notes — if two faults fail SM-1, they ship as "possible" only.
- §4.5 Notes — the extra-measurement list starts with sway only.
- §4.6 FR-14 — explanation limit of 150 words.
- §4.9 FR-20 — chat answer limit of 80 words.
- §6.1 — storing key frames is acceptable under the retention policy.
