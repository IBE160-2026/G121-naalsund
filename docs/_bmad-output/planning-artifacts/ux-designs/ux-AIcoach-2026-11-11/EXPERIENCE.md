---
title: AIcoach Experience
name: AIcoach
status: final
created: 2026-11-11
updated: 2026-11-24
sources:
  - ../../../../prd/prd.md
  - ../../../../prd/tilbakemelding-prd.md
  - .memlog.md
  - decisions.md
  - DESIGN.md
---

# AIcoach — Experience Spine

## Foundation

A single-surface **responsive web app** (PRD §7: no native app) used in two real contexts: a **phone browser at the range** (filming guide, upload, reading the result between balls) and a **laptop** (reading the result in depth, swing library, account). NFR-2: in the MVP the app runs on the author's or examiner's laptop and the phone reaches it over the same Wi-Fi. NFR-5: filming guide, upload and result work on a phone browser. NFR-6: UI and explanations are in English.

No UI kit is named in the PRD, and no architecture document exists yet. `[ASSUMPTION]` no component library; components are built to `DESIGN.md`, which holds the visual spec. This spine holds the behaviour. If architecture picks a library, it inherits these specs as a brand layer.

**Decisions after the PRD (2026-11-24) that this spine applies everywhere:**

| Decision | Replaces in the PRD |
|---|---|
| The AI coach chat is in the MVP (see AI Coach Chat). | §7 non-goal, §8.2 / §9 next phase |
| Every uploaded swing clip, including rejected ones, goes into the swing library automatically and stays until the player deletes it. | FR-18 opt-in per clip, §6.1 retention |
| One consent, given at sign-up through a required checkbox. No save toggle or save button anywhere. | FR-18 per-clip consent; §6.1 explicit consent is kept, moved to sign-up |

**Glossary.** Terms from PRD §3 are used verbatim in UI copy and here: player, swing clip, swing library, down the line, filming guide, analysis, result, rejection, swing event, key frame, measurement, confidence band, rule table, verified fault, possible fault, unverified observation, fault chain, feel cue, drill, mobility exercise, explanation, mock mode. One term is redefined: **swing library** = every swing clip the player has sent, each linked to its analysis (result or rejection), kept until the player deletes it. "Saved" is not used in UI copy.

**Visual references** are the five files in `mockups/` (round 3 variation 01 "Faithful Merge"), linked per surface in the IA table below. Their precedence is set once, in DESIGN.md → Brand & Style.

## Information Architecture

| Surface | Reached from | Purpose | FR / UJ | Mock |
|---|---|---|---|---|
| Landing | Root URL, signed out | Promise, mechanism, honesty, CTA to create account | FR-1 | `mockups/01-landing.svg` |
| Sign in | Landing header; any protected URL while signed out | Email + password | FR-1 | `mockups/05-other-pages.svg` |
| Create account | Landing CTA; "Create an account" on sign in | Email + password + the required library consent checkbox | FR-1, §6.1 | `mockups/05-other-pages.svg` |
| Filming guide (overview) | Rail / menu; checklist link on upload; landing secondary CTA | Six steps, one line each | FR-4 | `mockups/05-other-pages.svg` |
| Filming guide step | Overview row; rejection reason link | One rule, one diagram, one reason; Back / Next step | FR-4, FR-8 | `mockups/05-other-pages.svg` |
| New swing (upload) | "New swing" in rail / menu; "Film again" | Coach asks for one clip; checklist; drop zone with the library note | FR-5 | `mockups/02-upload.svg`, `mockups/03-upload-mobile.svg` |
| Analysing | Sending a clip (same thread, same URL) | Step log streams in; Evidence pins fill | FR-5, FR-6 | `mockups/02-upload.svg`, `mockups/03-upload-mobile.svg` |
| Result thread | End of analysing; rail swing row; swing library row | Verdict, feel cue, fault chain, practice, Also checked, chat; Evidence panel | FR-7, FR-9–FR-14 | `mockups/04-result.svg`, `mockups/03-upload-mobile.svg` |
| Rejection ("Cannot analyse") | End of analysing | Reasons, each linked to its guide step; Film again | FR-8 | `mockups/05-other-pages.svg` |
| No verified fault found | End of analysing | The answer, what was checked, one unverified observation, no drill | FR-12, FR-13 | `mockups/05-other-pages.svg` |
| Swing library | Rail / menu; library status on a result | Every swing clip, newest first: date, club, main finding ("Cannot analyse" for a rejection) | FR-19 | `mockups/05-other-pages.svg` |
| Clip detail | Swing library row; library status | Play the clip, open its analysis, delete the clip | FR-19 | spine only `[ASSUMPTION]` |
| Account | Rail / menu | Email, your analyses (delete one), sign out, delete account | FR-3 | `mockups/05-other-pages.svg` |
| Delete account (sheet) | Account → Delete account | Plain consequences, one clear choice | FR-3 | `mockups/05-other-pages.svg` |

**Navigation.** Signed in, desktop: a persistent left rail (wordmark, "New swing", recent swings, then Swing library · Filming guide · Account). Phone: the same rail opens as a sheet from the ≡ menu in the top bar; sub-pages show a back chevron instead. Landing has its own header (How it works · When it says no · Sign in · Create account). Sheets stack one level deep, never two.

**One thread per swing.** Upload, analysing and the outcome (result, rejection or no verified fault) live in one thread at one URL. The rail's "Swings" list shows the most recent threads with their main finding. `[ASSUMPTION]` the rail shows the latest 3–5; the full list lives under Account → "See all n analyses". This overlaps the stretch FR-16 (Open Question 6).

**Protection.** Upload, threads, swing library, clip detail and account require sign in (FR-1). A protected URL opened while signed out goes to Sign in and, after sign in, back to that URL `[ASSUMPTION]`. Another player's analysis or clip URL shows a plain "not found" page (FR-2). `[ASSUMPTION]` the filming guide is public, since the landing links to it; signed out, it uses the landing header.

## Voice and Tone

Brand voice lives in `DESIGN.md` → Brand & Style; this section is microcopy. Two registers: the **coach** (first person, Newsreader, short, warm, plain) and the **evidence** (third person, terse, mono, numbers with units). Copy is English (NFR-6).

| Do | Don't |
|---|---|
| "Your hips are moving toward the ball through impact. That's early extension, and I'm sure of it." | "Early extension detected (confidence 0.93)." |
| "It may feel like you stay down, but at impact your hips have moved toward the ball." (feel cue, one per verified fault) | Jargon on the blocklist: "kinematic sequence", "pelvic thrust", "degrees of spine tilt" (FR-14) |
| "One drill and one mobility exercise." | A list of drills, or "try these 5 fixes!" |
| "I won't guess from this clip. Three things got in the way:" | "Error: upload failed validation." |
| "None of my three rules fired. That's a real answer, so I won't invent a drill." | "Great swing! No problems!" |
| "I didn't measure your grip in this clip, so I can't tell you." | Any answer about something not in the analysis |
| "I agree that every swing clip I send is stored in my swing library on the AIcoach server until I delete it." | "We may retain your data to improve our services." |
| "This removes 9 analyses with their results and key frames, and 9 swing clips. It cannot be undone." | "Are you sure?" with no consequences |
| Measured values with units and a pin: `7% of body height [3]` | A number in the coach's prose without a pin |
| "Unverified — confirm with a coach" exactly | Softening it to "might be worth looking at" |
| "In your swing library" | "Saved", "Save", "Keep this clip?" |

**Refusals** are calm, first person, say *why* in one clause, and give the next useful step. They never apologise at length and never hedge into a half-answer. Patterns are in AI Coach Chat.

**Confidence in words.** high → "and I'm sure of it"; medium → "I'm fairly sure"; low → "but I can't be sure from this clip" plus what to film better. `[ASSUMPTION]` medium and low wording (only high is drawn).

## Component Patterns

Behaviour only. Visual specs are in `DESIGN.md` → Components under the same names.

### Identity and conversation

| Component | Use | Behavioural rules |
|---|---|---|
| Coach mark and wordmark | Rail, top bar, every coach message | Wordmark links home: the landing when signed out, the latest thread when signed in `[ASSUMPTION]`. The mark next to a message is not interactive. |
| Coach message | Thread | One or two sentences. Never contains a number without a pin. Arrives whole (no token streaming) `[ASSUMPTION]`, announced politely to screen readers. |
| Player message | Thread | Echo of the player's question or uploaded clip, right-aligned. The upload echo shows file name, length and fps, and upload progress while uploading. |
| Collapsed system line | Thread top after analysis | Folds the upload exchange and the checklist into one line; "Show" expands it in place, "Hide" folds it again. |
| Typing indicator | Analysing, chat | Shown while the coach is working; removed when the message arrives. Not announced repeatedly to screen readers. |
| Composer | Result thread | Enabled only once a result exists. Enter sends; Shift+Enter adds a line. Sending disables it until the answer arrives. Empty input cannot be sent. Hidden on a rejection `[ASSUMPTION]`. |
| Grounding note | Under every composer | Always visible, never dismissible. |
| Suggested prompt | Above the composer | Three on desktop, one on the phone. Tapping sends the prompt as the player's message. Refreshed after each answer `[ASSUMPTION]`. |
| "Based on" footnote | Under every grounded coach answer | Lists the pins and items the answer used; each pin is a citation link. A refusal shows what it checked ("unverified observation (confidence: low) · rule table"). |

### Result

| Component | Use | Behavioural rules |
|---|---|---|
| Library status | Result and rejection header | "In your swing library" links to the clip detail. It is a status, not an action: there is no save or unsave. If the clip has been deleted it reads "Clip deleted" and is not a link `[ASSUMPTION]`. |
| Jump-to chips | Result thread header | Each chip scrolls the thread to its section (Verdict · Why · Practise · Also checked · Ask the coach). The active chip follows scroll position. "Ask the coach" focuses the composer. |
| Verdict card | Result | Always first. Shows the verified fault, its confidence band and the one measurement that decided it. Activating the pin or value cites it in the Evidence panel. With more than one verified fault `[ASSUMPTION]`: one verdict card per fault, highest confidence first. |
| Feel cue | Result | Exactly one per verified fault (FR-14). The "[2]" link cites the impact key frame. |
| Fault chain | Result ("Why") | Three links: likely cause → mechanism → fault. Each link's value and pin cite the evidence. Likely cause is always dashed and labelled "Likely cause" (FR-10). The dashed legend line sits directly under the chain. |
| Exercise card | Result ("Practise") | One drill + one mobility exercise from the rule table (FR-11). Never shown for a possible fault or an unverified observation. On the phone it sits behind "Next: what to practise". |
| Medical notice | Every mobility exercise | Not dismissible. Same text everywhere. |
| Also checked | Result | Lists every other rule-table fault as "possible" or "not found", each with band and pin. A possible fault shows its measurement and "No drill." (PRD glossary). Always visible on desktop; on the phone one tap below practice `[ASSUMPTION]`. |
| Status chip | Also checked, library | Text label only ("possible", "not found"); never a colour-only state. |
| Confidence band | Every measurement and verified fault | Never omitted (FR-7). Clips under 120 fps never show "high". Over the top never shows above "medium". |
| Unverified observation card | No verified fault found | At most one per result; exactly one when no verified fault is found (FR-13). Always "confidence: low", never a drill. Never appears next to a verified fault it repeats or contradicts. |
| Inline message | Upload, forms, chat, network errors, frame-rate warning | One line under the control or section it concerns; cleared when the player changes the input or retries. Never a modal, never a banner. |
| Mock-mode label | Rail footer / menu sheet | Shown on every signed-in page while mock mode is on `[ASSUMPTION]`. Not interactive. |

### Evidence

| Component | Use | Behavioural rules |
|---|---|---|
| Evidence pin (and inline citation) | Thread, Evidence panel | Activating a pin or citation highlights the matching item in the Evidence panel (tint fill, teal outline) and scrolls it into view; on the phone it opens the evidence tray at that item, on a narrow laptop the Evidence drawer. The latest coach answer's citations stay lit until the next answer. |
| Key frame | Evidence panel, verdict (phone), library thumbnails | Activating a frame opens it larger in a sheet with the same overlays `[ASSUMPTION]`. The dashed address line and "+7%" arrow are part of the evidence, never optional. Frames shown match the swing events the rule uses (FR-10). |
| Measurement card | Evidence panel, tray | Shows the cited measurement: value, ruler, band. Changes when another measurement pin is activated. |
| Threshold ruler | Measurement card | Static. Shows the value against the rule's fault threshold; a possible fault also shows the potential threshold `[ASSUMPTION]`. |
| Evidence panel | Desktop upload, analysing, result | Sticky beside the thread while it scrolls. Before upload: placement diagram + placeholders. Analysing: frames and the measurement fill in as steps finish. Result: two key frames, the deciding measurement, "n more measurements", clip checks. |
| Evidence placeholder | Evidence panel, tray, cold load | Stands in for anything not yet there. Replaced in place when the item arrives; never shows a spinner. |
| Evidence chip | Phone top bar; narrow-laptop page header | Shows the pin count ("Evidence · 0" idle before any pin). Activating it opens the tray or drawer. |
| Evidence tray and Evidence drawer | Phone; narrow laptop | Tray: bottom sheet with a drag handle; swipe down or tap the scrim to close. During analysing it peeks at the bottom with live pins. Drawer: overlays the thread from the right with a scrim, traps focus, closes with Esc, the close button or a scrim tap. |
| Disclosure rows | Result, Evidence panel, phone result | All expand in place; state does not persist between visits. **Explanation:** "Read my full explanation · n words" opens the ≤150-word explanation (FR-14); collapsed by default. **More measurements:** opens the other measurements, each with value, band and pin. **Clip checks:** opens the view, frame and fps checks; a 30–119 fps warning shows here and in the thread. **Next step (phone):** "Next: what to practise" scrolls to the exercise card; Also checked follows it. |

### Upload and analysis

| Component | Use | Behavioural rules |
|---|---|---|
| Drop zone | New swing | Drag-and-drop (desktop) or "choose a file" (phone opens Photos / Files). Checks format and length before upload (FR-5). One clip at a time. On desktop, a valid dropped or chosen clip **sends at once** `[ASSUMPTION]`; on the phone it goes to the ready-to-send preview. The library note is information, not a control. |
| Ready-to-send preview | New swing (phone) | Shows the clip before sending. "Send to the coach" uploads it; "Choose a different clip" reopens the picker. |
| Step log | Analysing | Five steps in fixed order: Pose · Swing events · Measurements · Rule table · Explanation. Each turns done with a short mono detail. On a rejection `[ASSUMPTION]` the log stops at the step that found the problem (for example Pose for a face-on view or a body out of frame); that row shows "stopped", later rows stay pending, and the rejection follows. The page can be left; the thread keeps running and the rail row shows "Analysing…" `[ASSUMPTION]`. |
| Rejection reason row | Rejection | One row per reason (FR-8). The link opens the filming guide at that step. |

### Forms, lists and navigation

| Component | Use | Behavioural rules |
|---|---|---|
| Text input | Sign in, create account | Label above; errors appear under the field on submit, not while typing. |
| Consent checkbox | Create account | Required, unticked by default, never pre-ticked. The label is the full consent text and toggles the box. "Create account" stays disabled until the box is ticked; unticking disables it again. The consent is recorded with the account. It is the only consent in the app (PRD §6.1 explicit consent). |
| List row | Filming guide, swing library, account | The whole row is the target; a chevron means it navigates; a trash icon deletes (with a confirm sheet). |
| Rail swing row | Rail | Opens that thread. The active thread is highlighted. |
| Clip detail | Swing library | Native video controls, no autoplay. "Open analysis" opens the thread. "Delete clip" opens a confirm sheet (see State Patterns → Deleting a clip). |
| Filming guide step | Filming guide | Back / Next step at the bottom; step dots show position; "I'm ready to film" on the overview goes to New swing. |
| Buttons | Everywhere | One primary (clay) per screen. Destructive confirmation uses the dark button inside a sheet. |
| Bottom sheet | Delete confirmations, evidence tray, enlarged key frame | Focus moves into the sheet; Esc, swipe down or a scrim tap closes it (except while a delete is in progress). |
| Focus ring | All interactive elements | See Accessibility Floor. |
| Landing blocks | Landing | Static. The "Example result" card is labelled and not interactive except its CTA. |

## State Patterns

### Upload and analysis

| State | Surface | Treatment |
|---|---|---|
| Waiting for a clip | New swing | Coach message + checklist + drop zone with the library note. Composer disabled: "You can ask the coach once the result is ready." Evidence panel: placement diagram, placeholders, "0 pins · Nothing measured yet." |
| Clip refused before upload | New swing | Inline message under the drop zone, in the coach's voice: "That clip is 22 s. I can read up to 15 s — trim it and send it again." / "I read mp4 or mov files." Nothing is uploaded (FR-5). `[ASSUMPTION]` copy. |
| Ready to send (phone) | New swing | Clip preview with first-frame skeleton, file name, "3.8 s of 15 s · 120 fps", coach line "Looks right. Send it when you're ready.", the library note, "Send to the coach", "Choose a different clip". |
| Uploading | New swing | `[ASSUMPTION]` the player's clip bubble shows upload progress; the step log starts when the upload completes. |
| Analysing | Thread | Clip bubble, then "Got it — a clean down-the-line clip at 120 fps. Watching now." The step log fills in order with "n of 5" and the typing indicator "Coach is watching your swing…". Evidence pins fill live ("2 pins so far", "drawing lines…", "measuring…"). Composer disabled. Expected duration per NFR-1 (under 2 min for 10 s). |
| Analysis takes too long or fails | Thread | `[ASSUMPTION]` after 3 min, a coach line "This is taking longer than it should." with "Try again". A system failure is never shown as a rejection or a result. |
| Storage limit reached | New swing | `[ASSUMPTION]` drop zone disabled with "Your swing library is full (50). Delete a clip before sending a new one." (limit from the FR-19 assumption; Open Question 2). |

### Outcomes

| State | Surface | Treatment |
|---|---|---|
| Result: verified fault, high | Result thread | As `mockups/04-result.svg`. |
| Result: medium confidence | Result thread | Same layout; band "confidence: medium" everywhere it appears; coach lead uses "I'm fairly sure". Over the top is always capped here or lower (FR-7). |
| Result: low confidence | Result thread | Same layout; band "confidence: low" everywhere; coach lead adds "but I can't be sure from this clip", and one line names what to film better with a link to the guide step (UJ-1 edge case). |
| Frame-rate warning (30–119 fps) | Analysing, result | The clip is analysed. Inline warning in the thread and in clip checks: "Filmed at 60 fps — nothing can be rated 'high'." (FR-8). `[ASSUMPTION]` copy. Under 30 fps the clip is rejected instead. |
| Possible fault | Also checked | "possible" chip, measurement, band, pin, "No drill." Never in the verdict card, never counted as a fault. |
| Several verified faults | Result | `[ASSUMPTION]` one verdict card, chain and exercise card per fault, ordered by confidence; jump chips gain one entry per fault. Not mocked. |
| No verified fault found | Thread | Coach: "No verified fault found" + one line; "Checked: early extension · loss of posture · over the top"; one unverified observation card; "Ask the coach about this". No exercise card, no fault chain (FR-12, FR-13). |
| Rejection | Thread | Step log stopped; "Cannot analyse", "I won't guess from this clip. n things got in the way:", one row per reason with its guide-step link, primary "Film again", footer "No result was made. The clip is in your swing library; delete it there if you don't need it." No faults, no composer (FR-8). |
| LLM unavailable | Result | The result renders in full with the template explanation (FR-14); no error on the result itself. Composer disabled with "The coach can't answer questions right now. Your result is complete." Grounding note stays. `[ASSUMPTION]` copy. |
| Mock mode | Whole app | Works end to end (FR-15). Mock-mode label in the rail footer `[ASSUMPTION]`; chat gives fixed sample answers. |

### Library, account and access

| State | Surface | Treatment |
|---|---|---|
| Cold load | Existing thread, swing library, clip detail, account | `[ASSUMPTION]` content loads behind dashed placeholders in the final layout; no spinners. A load failure shows "Couldn't load this. Try again." inline. |
| Consent not ticked | Create account | "Create account" disabled; meta under it: "Tick the box to create your account." `[ASSUMPTION]` copy. |
| Email in use | Create account | "An account with this email already exists. Sign in instead?" (FR-1). The consent box keeps its state. |
| Sign-in error | Sign in | "That email and password don't match." under the form. |
| Empty swing library | Swing library | "No swings yet. Every clip you send lands here." + "New swing". `[ASSUMPTION]` copy. |
| Account with no analyses | Account | "No analyses yet." under "Your analyses"; sign out and delete account still shown. `[ASSUMPTION]` copy. |
| Empty rail (first visit) | Rail | No "Swings" heading; "New swing" is the only action. |
| Library and account rows | Swing library, account | Library row: thumbnail (dashed tile for a rejection), "date · club", main finding or "Cannot analyse"; a clip whose analysis was deleted reads "Analysis deleted" `[ASSUMPTION]`. Account row: "date · main finding" and a meta line "clip in swing library" or "clip deleted" `[ASSUMPTION]`. |
| Deleting an analysis | Account | `[ASSUMPTION]` confirm sheet: "Delete this analysis? Its result and key frames are removed. The swing clip stays in your swing library." On success the row disappears (FR-3). |
| Deleting a clip | Clip detail, swing library | `[ASSUMPTION]` confirm sheet: "Delete this clip?" with "Delete clip, keep analysis" and "Delete clip and analysis" (FR-19 assumption: the player chooses). The row leaves the library. |
| Delete failed | Account, library | "Couldn't delete. Nothing was removed. Try again." inline or in the open sheet. |
| Playback fails | Clip detail | `[ASSUMPTION]` "This clip can't play in this browser." The analysis can still be opened. |
| Not found / not yours | Any thread or clip URL | "This analysis doesn't exist or isn't yours." + a link to your swings (FR-2). |
| Network lost (phone at the range) | Upload, chat | `[ASSUMPTION]` inline: "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." with "Try again". |
| Focus | All | Visible focus ring on every interactive element (see Accessibility Floor). |

## Interaction Primitives

- **Tap or click to act.** Rows and cards that navigate are single targets.
- **Pins are links.** Any `[n]`, pin square or cited value focuses its evidence (panel on desktop, drawer on a narrow laptop, tray on the phone).
- **Progressive disclosure inline.** "Read my full explanation", "Show", "n more measurements" and "Clip checks" expand in place; nothing opens a new page for detail.
- **Drag-and-drop or pick** a file on desktop; pick from Photos / Files on the phone.
- **Sheets** for destructive confirmation, the evidence tray and an enlarged key frame. Swipe down, Esc or a scrim tap closes them.
- **Keyboard:** Tab order follows reading order; Space toggles the consent checkbox; Enter sends a chat message; Esc closes the topmost sheet or drawer.
- **Banned:** autoplaying video, carousels, score dials, streaks, badges, confetti, push or email re-engagement, swipe-only actions, hover-only affordances, modal stacks deeper than one, save toggles or save buttons for clips.

## Accessibility Floor

Behaviour only; contrast is in `DESIGN.md` → Colors.

- `[ASSUMPTION]` WCAG 2.2 AA on every surface (the PRD sets no level).
- Confidence is always text ("confidence: high"); colour and bars are redundant cues. Screen readers read the word, not the bars.
- Pins and citations have accessible names: "Evidence 3, hip movement toward the ball, 7% of body height, confidence high".
- Key frames have text alternatives stating the swing event, time and what the overlay shows ("Impact, 2.07 s. Hips 7% of body height closer to the ball than the dashed address line.").
- The step log, new coach answers and analysis completion are announced through a polite live region; analysing does not steal focus.
- Touch targets are at least 44 × 44px on the phone. The 34px chips, 18px pins and 22px consent box keep their visual size with a 44px hit area.
- The consent checkbox is a native checkbox with its full text as the label; the disabled "Create account" button exposes why through the meta line (`aria-describedby`).
- Focus is visible on every control (`[ASSUMPTION]` 2px `{colors.evidence-teal}` ring, 2px offset). Sheets and the Evidence drawer trap focus while open and return it on close.
- Dashed vs solid meaning is always also stated in words ("Likely cause", "Unverified", "measuring…").
- Respect reduced motion: no scroll animation on jump chips, no pulse on lit pins.
- The filming guide reads on a phone without horizontal scrolling (FR-4). Text scales to 200% without loss of content.
- Video playback has native controls and no autoplay.

## AI Coach Chat

**Status: in the MVP (decided 2026-11-24).** This overrides the PRD, which still lists chat as a non-goal (§7) and next phase (§8.2, §9). The PRD needs an Update with a new FR for grounded chat before stories are written. This section is the UX contract for it.

**Scope = one analysis.** Each thread's chat sees only that analysis: its measurements, confidence bands, key frames as references, the rule-table outcome (verified, possible, not found), the cause, drill, mobility exercise, the unverified observation and the explanation. It does not see other swings, the swing clip, the player's email or anything outside the analysis (PRD §6.1). Chat appears only on results (verified fault or no verified fault found), never on a rejection `[ASSUMPTION]`.

**Grounding rules (FR-14 applied to chat).**
- Mentions only faults, causes, drills and mobility exercises present in this analysis; no new ones.
- Uses only numbers present in the analysis; every number is cited with its pin.
- Never upgrades confidence: a medium or low band is restated as such; a possible fault stays "possible"; an unverified observation stays "Unverified — confirm with a coach".
- Never prescribes a drill or mobility exercise for a possible fault or an unverified observation.
- Same plain language and jargon blocklist as the explanation. `[ASSUMPTION]` answers of two to four sentences, at most about 80 words.
- Every answer ends with a "Based on:" footnote listing what it used.
- The language model explains; it never decides. The rule table remains the only source of verdicts.

**Refusals.** One sentence on why, one useful next step, in the coach's voice. The footnote names what was checked.

| Question type | Answer |
|---|---|
| Not measured ("Is my grip causing this?") | "I didn't measure your grip in this clip, so I can't tell you." + the current drill or "ask a coach" |
| Outside the rule table / unverified ("Give me a drill for the weight shift") | "I have no drill I can stand behind. A coach can check it in person." |
| Other swings or progress ("Is this better than last week?") | "I can only see this swing." + a pointer to the swing library `[ASSUMPTION]` |
| Pain or injury | No advice beyond the medical notice: "see a physiotherapist if you feel pain" (PRD §6.2, §7) |
| Use during a competitive round | `[ASSUMPTION]` "AIcoach is a practice tool, not for use during a round." (PRD §2.2) |
| Off topic | "I can only talk about this swing." |

**Suggested prompts.** Chosen from a fixed list per result type `[ASSUMPTION]`. Verified fault: "How do I know the drill is working?", "What does 'likely cause' mean?", "Can I do this drill in a net?". No verified fault: "What did you check in my swing?". Prompts never suggest something the coach would refuse.

**Behaviour.** Composer disabled until the result exists. One question at a time. Cited pins light in the Evidence panel. `[ASSUMPTION]` the conversation is stored with the analysis, shown again when the thread is reopened, and deleted with it (FR-3). LLM unavailable → composer disabled with a plain line; the result is untouched. Network lost → inline message with "Try again"; the unsent question stays in the composer. Mock mode → fixed sample answers.

## Responsive & Platform

| Width | Layout |
|---|---|
| ≥ 1344px | Three columns: rail (232) · thread (640 content + margins) · sticky Evidence panel (408). Designed at 1440 (`mockups/02-upload.svg`, `mockups/04-result.svg`). |
| 1024–1343px ("narrow laptop") | Rail + thread. The Evidence panel becomes the **Evidence drawer**, opened by the Evidence chip in the page header; activating a pin opens the drawer at that item. |
| 768–1023px | Rail collapses to the ≡ menu sheet; thread full width (max 640); Evidence stays a drawer. |
| < 768px (phone) | Phone layout from `mockups/03-upload-mobile.svg` and `mockups/05-other-pages.svg`: top bar (≡ or back · title + meta · Evidence chip), one column with a 20px gutter, actions in the bottom third, Evidence as the pull-up **evidence tray**. The result shows verdict, 7%, the two frames and the feel cue; practice is one tap away. |

`[ASSUMPTION]` all breakpoint values. 1344 is the narrowest width where the three designed columns fit with 32px thread margins; concepts 06 and r3-01 both flagged 1280 as too busy.

Platform: modern mobile Safari and Chrome, desktop Chrome / Edge / Firefox / Safari `[ASSUMPTION]`. Upload uses the browser file picker (Photos / Files on iOS and Android). No install, no PWA, no offline mode in the MVP. The phone reaches the laptop over local Wi-Fi (NFR-2), so network errors are expected at the range.

## Inspiration & Anti-patterns

The chosen direction is round 3 variation 01 **Faithful Merge** (`.working/round3/01-faithful-merge/`).

- **Kept from 06 "The Coach Talks":** identity, palette and type; one conversation per swing; upload as a message; structured cards in the thread; the sticky Evidence panel; pins; dashed = inferred; the grounded composer.
- **Kept from 09 "Cairn":** one main thing per screen, short copy, progressive disclosure, thumb-zone actions, the one-idea-per-phone secondary pages.
- **Kept from 02 "Lab Instrument":** only the skeleton key-frame figure.
- **Rejected:** 09's cairn stones motif; 02's graph paper, axes and lab density; 06's crowded result (six pins, clip timeline, open explanation); dashboards of measurements (PRD SM-C2); swing scores; streaks; the per-clip save toggle drawn in round 3.

## Key Flows

### Flow 1 — UJ-1. Rory finds out why he keeps hitting it thin (Rory, 34, 11 handicap, range after work, phone in hand)

1. Rory, signed in on his phone browser, taps ≡ → Filming guide and skims the six steps.
2. He props the phone on his bag at hand height, 3 m behind the hands line, and films a 7-iron at 120 fps.
3. He taps "New swing". The coach asks for one swing down the line; the checklist is the message. He taps "Choose swing clip".
4. Ready to send: he sees the clip, "3.8 s of 15 s · 120 fps", and taps "Send to the coach".
5. Analysing: "Got it — a clean down-the-line clip at 120 fps. Watching now." Pose and Swing events tick done; the Evidence chip reads "Evidence · 2" as the address and impact frames pin themselves.
6. **Climax:** the coach says "Your hips are moving toward the ball through impact. That's early extension, and I'm sure of it." Under it: **Early extension · confidence: high · 7% · rule: 4%** with the address and impact key frames, the hip ringed and the dashed address line showing the gap. The feel cue lands: "It may feel like you stay down, but at impact your hips have moved toward the ball."
7. He taps "Next: what to practise": Wall drill 3 × 10, 90/90 hip rotation 2 × 8 with the medical notice.
8. Resolution: he does the wall drill for the rest of the bucket. The header shows the clip is in his swing library.

Edge: hips only partly visible at impact → same fault, "confidence: low" everywhere, plus one line on what to film better, linked to the guide step. Failure: analysis fails → "Try again"; never a guessed result.

### Flow 2 — UJ-2. Rory's video is rejected — and he learns how to film (Rory, same range, wrong angle)

1. Rory films face-on by mistake, at 24 fps, with his feet cut off, and sends it. (PRD UJ-2 says 30 fps; under FR-8 a 30 fps clip is analysed with a warning, so this flow uses 24 fps.)
2. Analysing starts; the step log stops at Pose, which finds the problems.
3. **Climax:** "Cannot analyse. I won't guess from this clip. Three things got in the way:" Face-on view detected → Filming guide · step 1; Feet out of frame → step 5; Filmed at 24 fps → step 4.
4. He taps step 1; the guide opens at "Down the line only" with its diagram. Next step walks him through 4 and 5.
5. He taps "Film again", re-films, and Flow 1 follows. Footer: "No result was made. The clip is in your swing library; delete it there if you don't need it."

### Flow 3 — UJ-3. Nelly's swing has a fault AIcoach does not cover (Nelly, 4 handicap, reverse pivot)

1. Nelly sends a 6-iron clip; analysis runs as in Flow 1.
2. **Climax:** "No verified fault found. None of my three rules fired. That's a real answer, so I won't invent a drill." Below: "Checked: early extension · loss of posture · over the top".
3. A dashed card: "Unverified — confirm with a coach. Weight appears to move toward the trail side at the top. confidence: low. No drill: this is not in my rule table."
4. She taps "Ask the coach about this" and asks "Can you give me a drill for the weight shift?"
5. The coach refuses: "I can't. The weight shift is unverified and outside my rule table, so I have no drill I can stand behind. A coach can check it in person." Based on: unverified observation (confidence: low) · rule table.

Failure: the language model is unavailable → the composer is disabled with "The coach can't answer questions right now. Your result is complete."

### Flow 4 — UJ-4. Rory deletes his data (Rory, laptop, deciding to stop)

1. Rory opens Account from the rail.
2. Under "Your analyses" he taps the trash icon on "9 Nov · Cannot analyse". A sheet says its result is removed and the clip stays in his swing library `[ASSUMPTION]`; he confirms and the row disappears.
3. He taps "Delete account". A sheet: "Delete your account? This removes 9 analyses with their results and key frames, and 9 swing clips. It cannot be undone, and you will not be able to sign in again."
4. **Climax:** he taps "Delete everything". He is signed out to the landing page; signing in with the old email fails.

Failure: deletion fails → the sheet stays open with "Couldn't delete. Nothing was removed. Try again."

### Flow 5 — UJ-5. The examiner runs AIcoach from the README (the course examiner, ordinary laptop, no keys)

1. The examiner starts the app in mock mode per the README and opens it in a browser.
2. Creates an account (ticking the consent box), taps "New swing" and drops a bundled test clip; it sends at once.
3. Analysing runs with the same step log.
4. **Climax:** a complete result: verified fault, measurement with confidence band, key frames, fault chain, template explanation with feel cue, drill and mobility exercise (SM-4, SM-10). The rail shows "Mock mode" `[ASSUMPTION]`.
5. The examiner asks the coach a question; chat answers with fixed sample answers in mock mode.

### Flow 6 — UJ-6. Rory keeps his swings to watch his progress (Rory, two weeks later, laptop)

1. Every clip Rory sends lands in his swing library automatically; he agreed to that once, at sign-up (Flow 8).
2. Two weeks later he opens Swing library: his swings, newest first, each with date and main finding ("11 Nov 2026 · 7-iron · Early extension · high").
3. He opens the oldest early-extension row: the clip detail plays the clip with native controls and links "Open analysis".
4. **Climax:** he opens that analysis, then today's, and compares them; each has its own confidence band. (Stretch FR-17 would show the two side by side `[ASSUMPTION]`.)
5. He deletes an old, badly filmed clip; the confirm sheet lets him keep or delete its analysis `[ASSUMPTION]`, and the row leaves the library.

### Flow 7 — Rory asks the coach why it feels wrong (MVP; PRD update pending — see AI Coach Chat)

1. On his result, Rory taps the "Ask the coach" chip; the composer takes focus. The grounding note reads "Answers are based only on this analysis — no new faults, numbers or drills."
2. He types "Why does it feel like I'm staying down when I'm not?" and sends.
3. **Climax:** "The move happens below your eye line, so you don't feel it. Your hips moved 7% of body height [3] toward the ball. In the impact frame [2] you can see the gap to the dashed line. In the wall drill, a glute leaving the wall is the same move." Pins 2 and 3 light up in the Evidence panel. Footnote: "Based on: [3] hip movement · [2] impact frame · wall drill".
4. He taps the suggested prompt "Can I do this drill in a net?"
5. He asks "Should I change my grip as well?" — the coach refuses: "I didn't measure your grip in this clip, so I can't tell you. Stick with the wall drill for now, and ask a coach about grip."

Failure: the network drops at the range → inline "Can't reach AIcoach. Check you're on the same Wi-Fi as the laptop." with "Try again"; his question stays in the composer. Language model unavailable → composer disabled with the plain line; the result is untouched.

### Flow 8 — Rory creates his account (sign-up and library consent; precedes Flow 1)

1. Rory taps "Create account" on the landing page.
2. He enters his email and a password. "Create account" is disabled; under it: "Tick the box to create your account."
3. **Climax:** he reads the one consent — "I agree that every swing clip I send is stored in my swing library on the AIcoach server until I delete it." — and ticks it. "Create account" turns clay and active.
4. He taps it and lands on New swing, signed in.

Failure: the email is already in use → "An account with this email already exists. Sign in instead?"; his entries and the ticked box stay.

## Open Questions

Visual questions (dark mode, "possible" chip contrast, font loading, landing on the phone) are in DESIGN.md → Open Questions.

1. **PRD update for chat.** Chat is in the MVP; the PRD needs the new FR. Open: answer length limit and cost per question outside mock mode.
2. **PRD update for the swing library and consent.** Automatic library + one sign-up consent reverses FR-18 (opt-in per clip), §3's swing library definition, SM-11 and §6.1 retention. Open: does the 50-clip limit still hold now that every clip, including rejections, counts?
3. **Delete coupling.** Assumed: deleting an analysis keeps its clip; deleting a clip lets the player keep or delete its analysis. Confirm both, and whether single deletes need a confirm sheet.
4. **Rejection in the step log.** Assumed: the log stops at the step that found the problem. Architecture should confirm which checks run in which step (fps may be known before Pose).
5. **Desktop sends on drop.** Assumed: no ready-to-send step on desktop. Confirm.
6. **History (FR-16) overlap.** The rail's "Swings" list and Account → "See all n analyses" are effectively analysis history, which the PRD marks stretch. Is the rail list P1?
7. **Unverified observation in the MVP.** The PRD feedback (tilbakemelding §4.1) asks whether it stays, and on what data. The no-fault screen depends on it.
8. **Several verified faults on one swing.** Not mocked; ordering and layout assumed.
9. **Clip detail and compare (FR-17)** are not mocked; confirm that spine-only is enough.
10. **Narrow-laptop breakpoint.** Confirm 1344px for the Evidence drawer, and the 1024 / 768 steps.
11. **UI language.** NFR-6 says English and the mockups are English; confirm no Norwegian UI is wanted for the course demo.
12. **Mock-mode label** visible to the examiner: yes or no?
13. **Copy sign-off.** Low- and medium-confidence wording, the 30–119 fps warning, the consent text and its helper line, and the library note.
