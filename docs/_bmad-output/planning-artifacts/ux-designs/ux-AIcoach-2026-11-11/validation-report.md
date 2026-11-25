# Validation Report — AIcoach

- **DESIGN.md:** `D:/IBE160 Prog m KI/IBE160/AIcoach/G121-naalsund/docs/_bmad-output/planning-artifacts/ux-designs/ux-AIcoach-2026-11-11/DESIGN.md`
- **EXPERIENCE.md:** `D:/IBE160 Prog m KI/IBE160/AIcoach/G121-naalsund/docs/_bmad-output/planning-artifacts/ux-designs/ux-AIcoach-2026-11-11/EXPERIENCE.md`
- **Run at:** 2026-11-24T20:45

## Overall verdict

The pair is a usable contract. Every token reference resolves, every color has a hex value, all six UJs have Key Flows with protagonists and climaxes, and the invented AI Coach Chat section commits the grounding and refusal rules well. Nothing is critical. The main risk is the 2026-11-24 swing-library decision, which was only partly carried through. DESIGN.md still specifies the save toggle and the "Save to swing library" button. The sign-up consent has no committed form. Superseded mockup copy, including a privacy claim on the landing page, is not overridden. Fix the five high findings before story-dev starts. They sit on the upload, result, sign-up and landing surfaces.

Finalize pass (2026-11-24): all 33 findings are fixed (5 high, 13 medium, 15 low; none critical). The save toggle and save button are gone from both spines and all five mockups. Sign-up has one unticked, required consent checkbox, and "Create account" stays disabled until it is ticked. The fps threshold follows FR-8, and evidence-idle passes AA at 4.82:1. Fixes that needed a product decision are tagged [ASSUMPTION] and collected in EXPERIENCE.md → Open Questions (13). Before stories are written, run the PRD Update for chat and for the automatic swing library with sign-up consent.

## Category verdicts

- Flow coverage — adequate → strong. Every UJ, plus chat and sign-up (new Flow 8), has a flow with a protagonist, a climax and a failure line where one applies. The fps threshold now follows FR-8.
- Token completeness — adequate → strong. 79 distinct token references resolve, every type size in the Components prose has a token, evidence-idle passes at 4.82:1, and the overlays are tokens.
- Component coverage — thin → adequate. Every component has one name and a row in both spines, and the save UI is gone. It stays adequate because Clip detail, the Evidence drawer, the upload progress bar and the mock-mode label are specified only in the spines, as [ASSUMPTION], with no mockup.
- State coverage — adequate → strong. Cold load, medium confidence, consent not ticked, both delete directions, desktop send-on-drop, the signed-out guide and the return URL are covered.
- Visual reference coverage — adequate → strong. The mockups now match the decisions, every mockup is linked per component group and per surface, and precedence is stated once (DESIGN → Brand & Style).
- Bloat & overspecification — adequate → adequate. Prose references tokens, the lineage is told once, and the toggle dead weight is deleted. It stays adequate because DESIGN.md is still long: the key-frame construction and the component anatomy are load-bearing.
- Inheritance discipline — adequate → strong. Swing library is redefined once in Foundation, the post-PRD decisions are listed in one table, and names match across files. The PRD conflicts are logged, not resolved: the PRD Update is still pending.
- Shape fit — strong → strong. Key Flows now come last, and Open Questions are split into visual and product lists with no overlap.

## Findings by severity

Every finding below is fixed. Each ends with how it was fixed.

### Critical (0)

None.

### High (5)

**Flow coverage** — Flow 2 gives "Filmed at 30 fps" as a rejection reason (EXPERIENCE L199, also drawn in `mockups/05-other-pages.svg`).
That contradicts FR-8's acceptance criterion (30 fps is the hard floor; clips at 30–119 fps are analysed with a warning) and the spine's own "Frame-rate warning (30–119 fps)" state (L134). A dev or test author will build the wrong threshold.
Fix: change the reason to "Filmed at 24 fps" or to an FR-8 reason such as "too dark or blurred", and note that the mockup is superseded.
Fixed: reason is now "Filmed at 24 fps" (under FR-8's 30 fps floor) in Flow 2, with a note on PRD UJ-2; `mockups/05-other-pages.svg` and `mockups/01-landing.svg` edited to match; a Frame-rate warning state says 30–119 fps is analysed with a warning.

**Token completeness** — `evidence-idle` `#7A6F63` on `paper-2` `#EBE3D5` computes to **3.85:1**. (EXPERIENCE L168)
That fails AA text contrast, which the spine itself sets as the floor (EXPERIENCE L168). It is used for the pre-analysis "Evidence · 0" chip text (DESIGN L439, L505), and the combination is missing from the contrast list (L441).
Fix: darken it to about `#6A6056`, or use `ink-2` (5.45:1 on paper 2), and add the pair to the contrast list.
Fixed: `evidence-idle` darkened to `#6A6056` (4.82:1 on paper 2); pair added to the contrast table; new `evidence-chip-idle` component.

**Component coverage** — DESIGN still specifies the removed save UI. (DESIGN L515)
The Upload drop zone anatomy ends with "then the save toggle with its consent text" (DESIGN L515). Buttons → Quiet = "Save to swing library" in the result header (L529). EXPERIENCE replaces that button with an "In your swing library" status line (L106), which has no visual spec.
Fix: remove the toggle from the drop zone anatomy and reassign or remove `button-quiet`. Add a DESIGN row for the "In your swing library" status line.
Fixed: toggle removed from Drop zone anatomy (replaced by a library note); `button-quiet` and the Quiet button removed; new `library-status` component and "Library status" rows in both spines; `mockups/02`, `03`, `04` edited to match.

**Component coverage** — "Library consent" (EXPERIENCE L105) has no DESIGN row.
It also doesn't commit whether consent is a required checkbox that enables "Create account" or a passive statement. PRD §6.1 requires *explicit* consent, so this decides the form logic and the legal posture. Bottom sheet (L115) and Interaction Primitives (L160) still list "consent" as a sheet.
Fix: commit the form (for example, a required checkbox with the stated text, so "Create account" stays disabled until it is ticked). Add a DESIGN row, and remove "consent" from both sheet lists.
Fixed: committed an unticked, required Consent checkbox that keeps "Create account" disabled until ticked: `consent-checkbox` and `button-primary-disabled` tokens, DESIGN row, EXPERIENCE row, "Consent not ticked" state, Flow 8; "consent" removed from the Bottom sheet row and Interaction Primitives; checkbox drawn in `mockups/05-other-pages.svg`.

**Visual reference coverage** — Superseded mockup copy is only partly overridden. (L36)
The spine flags the toggle (L36) and rewrites the rejection footer (L139) and the delete-account sheet (L215). But `mockups/01-landing.svg` still says "Your clips are private. **Unsaved clips are deleted after analysis.**", which is a privacy claim that is now false. DESIGN → Landing blocks (L545) gives no replacement. `mockups/05-other-pages.svg` still has "5 saved swings", "clip saved / no clip kept" and "Nothing was saved."
Fix: add a "Superseded mockup copy" list (string → replacement) in EXPERIENCE, including the landing privacy line.
Fixed: edited the mockups instead of listing overrides: landing privacy line and "Not kept unless you ask"; toggles and "keep it" copy in 02/03; "not saved" echo; "Save to swing library" button in 04; "Nothing was saved", "5 saved swings", "clip saved / no clip kept", "saved clip(s)" in 05. All SVGs well-formed and rendered without overlaps.

### Medium (13)

**Flow coverage** — Flow 2 step 2 says "the clip-check step fails" (L198), but the Step log has five fixed steps with no clip-check step (L107, DESIGN L519).
How a rejection appears in the step log is undefined.
Fix: add a "Clip checks" step, or state which step fails and how the log ends on a rejection.
Fixed: Step log gains a "stopped" state: the log stops at the step that found the problem, later rows stay pending `[ASSUMPTION]` (Step log in both spines, Rejection state, Flow 2 step 2; Open Question 4).

**Flow coverage** — Flow 5 step 5 says "Chat, if present in the build" (L226), which contradicts the MVP decision in AI Coach Chat (L246) and `.memlog.md`.
This is the only place the spines treat chat as optional.
Fix: "Chat answers with fixed sample answers in mock mode."
Fixed: Flow 5 step 5 now: the examiner asks a question and chat answers with fixed sample answers in mock mode.

**Flow coverage** — No flow walks account creation with the new one-time library consent, which is the main reversal of FR-18.
Flow 5 step 2 covers it in one clause, and Flow 6 step 1 only refers back to it.
Fix: add beats to Flow 6 or a short flow: sign-up screen, consent text and its required action, then the failure path ("email in use").
Fixed: added Flow 8 (sign-up, consent checkbox, disabled button, email-in-use failure); Flow 5 and Flow 6 point to it.

**Token completeness** — Many type styles in Components prose have no token: drop zone title Figtree 21/600 (L515), Also checked title 15.5px (L493), key frame name 13.5/600 (L499), disclosure row 14.5/600 (L533), rejection reason 13/600 (L525), filming step label 13/600 (L537), wordmark 24/34px (L479), quote mark 60/40px (L487).
Code will hard-code them.
Fix: add tokens such as `title-drop`, `label-sm` and `wordmark`, or map each to an existing token.
Fixed: added tokens `wordmark`, `wordmark-large`, `quote-mark(-mobile)`, `card-title-lg`, `card-title-sm`, `step-name`, `row-title`, `frame-label`, `label-strong`, `label-sm`; Components prose references them.

**Token completeness** — The status chip token uses `{typography.meta}` (12.5/**400**, L307), but the prose says the word is 12.5/**600** (L535).
The input label is also 12.5/600 (L531) with no token.
Fix: add a `label-sm` 12.5/600 token and point `status-chip.typography` at it.
Fixed: `status-chip.typography` now `{typography.label-sm}` (12.5/600); `text-input.label` uses it too.

**Component coverage** — Several behavioural surfaces and states have no visual spec: Saved clip detail (video player, "Open analysis", "Delete clip"), the phone "Ready to send" clip preview (L128), the upload-progress bubble (L129), the narrow-laptop Evidence **drawer** and its page-header "Evidence · n" chip (L277; DESIGN only specifies the phone chip), the frame-rate warning (L134), the mock-mode label (L141) and the "taking longer" line with "Try again" (L131).
Fix: add short DESIGN rows, or map each one explicitly to an existing component (Inline message, Bottom sheet, Evidence chip).
Fixed: DESIGN rows added for Clip detail, Ready-to-send preview, upload progress (Player message), Evidence drawer + header Evidence chip, frame-rate warning and "taking longer" (Inline message), Mock-mode label; new ones marked `[ASSUMPTION]`.

**Component coverage** — Component names drift between the files. (L117, also used in chat)
DESIGN "Upload drop zone" vs EXPERIENCE "Drop zone". DESIGN "Inputs and list rows" vs "Text input" and "List row". YAML `unverified-card` vs "Unverified observation card". `measurement-card-cited` and `evidence-placeholder` have no EXPERIENCE row. "Typing indicator" is an EXPERIENCE row (L117, also used in chat) but appears in DESIGN only inside Step log.
Fix: use one canonical name per component across the YAML key, the DESIGN heading and the EXPERIENCE row.
Fixed: one canonical name per component across YAML key, DESIGN heading and EXPERIENCE row (Drop zone, Text input, List row, Unverified observation card / `unverified-observation-card`, Measurement card / `measurement-card`, Evidence placeholder, Typing indicator).

**State coverage** — No cold-load or loading state for opening an existing thread (from the rail or library), the swing library, the account page or the saved clip detail.
Fix: add one row, for example "content loads behind dashed placeholders; no spinners", which reuses the existing dashed = not-yet-there language.
Fixed: added "Cold load" state: dashed placeholders in the final layout, no spinners, inline load-failure line `[ASSUMPTION]`.

**State coverage** — The automatic library leaves clip and analysis deletion uncoupled. (L214)
Flow 4 deletes the analysis "9 Nov · Cannot analyse" (L214), but it is not said whether its clip stays. Flow 6 asks "Keep its analysis?" when a clip is deleted (L234). The library row for a rejected clip ("Cannot analyse", shown in `mockups/05`) isn't specified in IA (L41 says "main finding"). Account rows in `mockups/05` still show "clip saved / no clip kept".
Fix: commit both directions of the delete coupling and the row content for rejected clips, and drop the clip-status line from account rows.
Fixed: committed both directions as `[ASSUMPTION]` (Deleting an analysis keeps the clip; Deleting a clip offers keep/delete analysis per FR-19), library and account row content incl. rejections; Open Question 3. Account rows in `mockups/05` now read "clip in swing library".

**State coverage** — Desktop has no pre-send state. (L128)
The phone has "Ready to send" (L128). The desktop Drop zone says "dropping a second replaces the first before sending" (L104), which implies a pending state that isn't specified.
Fix: add a desktop ready-to-send row, or state that dropping a clip sends it.
Fixed: Drop zone: on desktop a valid clip sends at once `[ASSUMPTION]`; the "replaces the first" clause removed; Open Question 5.

**Visual reference coverage** — DESIGN → Components cites no mockup per component; there is only the blanket list at L427, plus `04` in Colors.
A consumer can't tell which file draws, say, the step log (02 desktop vs 03 phone) or the filming guide step.
Fix: add a "→ `mockups/0x`" pointer to each component or component group.
Fixed: Components grouped (Identity and conversation, Result, Evidence, Upload and analysis, Forms/lists/navigation, Landing), each with a → `mockups/0x` pointer; Layout table names the mockup per frame.

**Bloat & overspecification** — DESIGN Components prose restates YAML values as pixels next to the tokens: composer 56px, bars 4 × 11 / 2px, pin 18px, buttons 52/56px.
Two sources for the same value drift, and the status chip weight already has.
Fix: make the prose reference tokens and keep pixel values in the YAML only.
Fixed: Components prose now references tokens; pixel values kept in YAML only (construction details without tokens remain).

**Inheritance discipline** — EXPERIENCE says glossary terms are used verbatim (L23).
But the PRD §3 definition of **swing library** ("saved swing clips… unsaved swing clips are deleted after analysis") no longer holds, and the spine doesn't restate the new meaning. Terms like "Saved clip detail" (L42) and "saved" carry the old model forward.
Fix: state the redefined term once in Foundation and rename the surface to "Clip detail".
Fixed: Foundation redefines **swing library** once and lists the post-PRD decisions; "Saved clip detail" renamed "Clip detail"; "saved" banned from UI copy.

### Low (15)

**Flow coverage** — Flow 6's climax depends on stretch FR-17 (`[ASSUMPTION]`, L233).
The MVP path ("he switches between the two") is a parenthetical, not a step.
Fix: make the MVP version the climax step and mark side-by-side as the stretch variant.
Fixed: climax is now the MVP path (open both analyses and compare); side-by-side is a parenthetical stretch note.

**Flow coverage** — Flows 3 and 7 (chat) have no failure line. ("LLM unavailable" L140, "Network lost" L150)
The states exist ("LLM unavailable" L140, "Network lost" L150), but the flows don't point to them.
Fix: add one "Failure:" line to Flow 7.
Fixed: Failure lines added to Flow 3 (LLM unavailable) and Flow 7 (network lost, LLM unavailable).

**Flow coverage** — Copy drift: Flow 1 step 5 says "Got it. (L130)
A clean clip. Watching now." but Analysing state (L130) says "Got it — a clean down-the-line clip at 120 fps. Watching now."
Fix: use one string.
Fixed: Flow 1 step 5 uses the Analysing state string "Got it — a clean down-the-line clip at 120 fps. Watching now."

**Token completeness** — Typography tokens use `fontStyle` (L93, L98, L104), which is outside the spec's allowed keys.
Resolvers may drop it.
Fix: keep it, but note it as an extension in Typography, or use a separate italic family name.
Fixed: Typography section states `fontStyle` is an extension and names the fallback (load Newsreader Italic).

**Token completeness** — Some raw values sit outside tokens: the bottom-sheet scrim `rgba(37,32,27,0.42)` (L417), the hero shadow "#25201B at 6%" (L469), the step log's "white check" and the ghost-body opacities.
Fix: add `scrim` and `shadow-hero` tokens.
Fixed: added `scrim` (#25201B6B), `shadow-hero` (#25201B0F) and `on-confidence` (step-log check); bottom sheet and Elevation reference them. Ghost-body opacities stay as key-frame construction values.

**Token completeness** — `ruler-track` on `evidence-tint` is 1.63:1, and no ratio is stated for it.
The meaning is carried by the teal fill, the tick and the labels, so this is acceptable.
Fix: state that the track is decorative.
Fixed: Colors states the ruler track (1.6:1) and hairline are decorative and carry no state.

**Component coverage** — The DESIGN "Save toggle" row (L517) and the `toggle` / `toggle-off` / `toggle-knob` tokens are kept "in case".
That is dead spec, and a consumer may build it anyway.
Fix: delete them, and DESIGN Open Q 2 with them.
Fixed: Save toggle row, `toggle` component, `toggle-off`/`toggle-knob` tokens and the toggle Open Question deleted.

**State coverage** — Chat history is contradictory. (L270)
AI Coach Chat assumes the conversation is stored with the analysis (L270), but Open Q 1 (L294) lists "whether chat history is stored" as open. What a revisited thread shows depends on this.
Fix: pick one.
Fixed: picked: stored with the analysis, shown on reopen, deleted with it `[ASSUMPTION]`; removed from Open Questions.

**State coverage** — There is no result state row for medium confidence (only high L132 and low L133), although wording exists at L71 and over the top is capped at medium.
Fix: add the row.
Fixed: added "Result: medium confidence" row.

**State coverage** — The public filming guide has no signed-out header or navigation defined, and the return-to-URL after sign-in from a protected link is unstated (L50, L32).
Fix: add one line each.
Fixed: Protection paragraph: signed-out guide uses the landing header; sign in returns to the requested URL `[ASSUMPTION]`.

**Bloat & overspecification** — Dead weight from the removed toggle: the Save toggle row, the toggle tokens and DESIGN Open Q 2.
Fix: delete them.
Fixed: deleted with the toggle row, tokens and Open Question.

**Bloat & overspecification** — The concept lineage (06 / 09 / 02) is told twice, in DESIGN Brand & Style (L425) and EXPERIENCE Inspiration (L287).
Fix: keep it in Inspiration, and keep only the posture sentence in Brand & Style.
Fixed: lineage kept only in EXPERIENCE → Inspiration & Anti-patterns; Brand & Style keeps the posture and points there.

**Inheritance discipline** — Component names differ across sections and files (see §3, finding 4).
Fix: 
Fixed: fixed with §3 finding 4.

**Shape fit** — EXPERIENCE puts Key Flows before AI Coach Chat, Responsive and Inspiration.
The examples end on Key Flows.
Fix: optionally move Key Flows last. Flow 7 then reads after the chat contract it relies on.
Fixed: Key Flows moved last before Open Questions.

**Shape fit** — Each file has its own Open Questions list, with overlap: dark mode appears in both.
Fix: keep cross-cutting questions in one file and point to it from the other.
Fixed: visual questions only in DESIGN, product/behaviour only in EXPERIENCE, each pointing to the other; dark mode appears once.

## Mechanical notes

- Residual (low, pre-existing, not a finding): when Newsreader is not installed and Georgia substitutes, the mockups render "Coach" touching its timestamp. This is font fallback only.
- Residual (low): the analysing panel in `mockups/03-upload-mobile.svg` still says "Got it. A clean clip. Watching now.", and `mockups/02-upload.svg` draws the drop-zone title at 19px instead of `card-title-lg` 21px. The spine wins.
- Token references: 79 distinct, all resolve (both files). Removed: `toggle-off`, `toggle-knob`, `toggle`, `button-quiet`. Added: `scrim`, `shadow-hero`, `on-confidence`, ten type tokens, `button-primary-disabled`, `evidence-chip-idle`, `library-status`, `consent-checkbox`.
- Mockup edits: copy changes, plus the consent checkbox and disabled button in 05. All five SVGs parse as well-formed XML and were rendered in headless Chrome to check for overlaps.
- Frontmatter: both spines have `status: final` and `updated: 2026-11-24`.

## Reviewer files

- `review-rubric.md`
