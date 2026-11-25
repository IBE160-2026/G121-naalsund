---
name: AIcoach
description: A golf coach in the browser that talks in plain language and pins every number it says to measured evidence. Warm paper, a clay coach voice, teal evidence.
status: final
created: 2026-11-11
updated: 2026-11-25
sources:
  - ../../../../prd/prd.md
  - .memlog.md
  - decisions.md
  - .working/round3/01-faithful-merge/concept.md
colors:
  # Surfaces
  paper: '#F4EFE6'
  paper-2: '#EBE3D5'
  card: '#FFFCF6'
  hairline: '#DAD0BF'
  # Ink
  ink: '#25201B'
  ink-2: '#62584D'
  ink-on-dark: '#F4EFE6'
  ink-on-dark-2: '#CFC5B4'
  # Coach
  clay: '#A4462A'
  on-clay: '#F4EFE6'
  # Evidence
  evidence-teal: '#1E5368'
  evidence-tint: '#E2ECEC'
  on-evidence: '#FFFFFF'
  evidence-idle: '#6A6056'
  ruler-track: '#A9BDC0'
  # Confidence band (always paired with the word and the 3 bars)
  confidence-high: '#2D6A4A'
  confidence-medium: '#8C5D0F'
  confidence-low: '#8E3F33'
  on-confidence: '#FFFFFF'
  # Key frame (skeleton figure)
  keyframe-ground: '#36312B'
  keyframe-floor: '#4A433A'
  keyframe-floor-line: '#5A5246'
  body-line: '#8ED3E6'
  ghost-body: '#D8CCB6'
  club: '#9A907F'
  ball: '#EFE8DA'
  # Overlays (8-digit hex: ink at 42% and 6%)
  scrim: '#25201B6B'
  shadow-hero: '#25201B0F'
typography:
  display-hero:
    fontFamily: Newsreader
    fontSize: 62px
    fontWeight: '500'
    lineHeight: 68px
  display-section:
    fontFamily: Newsreader
    fontSize: 46px
    fontWeight: '500'
    lineHeight: 54px
  wordmark:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
  wordmark-large:
    fontFamily: Newsreader
    fontSize: 34px
    fontWeight: '600'
  page-title:
    fontFamily: Newsreader
    fontSize: 23px
    fontWeight: '600'
  page-title-mobile:
    fontFamily: Newsreader
    fontSize: 18.5px
    fontWeight: '600'
  screen-headline-mobile:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
  panel-title:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
  coach-lead:
    fontFamily: Newsreader
    fontSize: 27px
    fontWeight: '500'
    lineHeight: 38px
  coach-lead-mobile:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 27px
  coach-body:
    fontFamily: Newsreader
    fontSize: 18.5px
    fontWeight: '400'
    lineHeight: 29px
  coach-name:
    fontFamily: Newsreader
    fontSize: 17px
    fontWeight: '600'
    fontStyle: italic
  feel-cue:
    fontFamily: Newsreader
    fontSize: 21px
    fontWeight: '400'
    fontStyle: italic
    lineHeight: 30px
  feel-cue-mobile:
    fontFamily: Newsreader
    fontSize: 17px
    fontWeight: '400'
    fontStyle: italic
    lineHeight: 23px
  quote-mark:
    fontFamily: Newsreader
    fontSize: 60px
    fontWeight: '400'
  quote-mark-mobile:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '400'
  fault-name:
    fontFamily: Figtree
    fontSize: 26px
    fontWeight: '600'
  exercise-name:
    fontFamily: Figtree
    fontSize: 23px
    fontWeight: '600'
  card-title-lg:
    fontFamily: Figtree
    fontSize: 21px
    fontWeight: '600'
  card-title:
    fontFamily: Figtree
    fontSize: 16px
    fontWeight: '600'
  card-title-sm:
    fontFamily: Figtree
    fontSize: 15.5px
    fontWeight: '600'
  step-name:
    fontFamily: Figtree
    fontSize: 15px
    fontWeight: '600'
  row-title:
    fontFamily: Figtree
    fontSize: 14.5px
    fontWeight: '600'
  label:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: '600'
  frame-label:
    fontFamily: Figtree
    fontSize: 13.5px
    fontWeight: '600'
  label-strong:
    fontFamily: Figtree
    fontSize: 13px
    fontWeight: '600'
  label-sm:
    fontFamily: Figtree
    fontSize: 12.5px
    fontWeight: '600'
  body:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 21px
  body-lg:
    fontFamily: Figtree
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 27px
  button:
    fontFamily: Figtree
    fontSize: 15px
    fontWeight: '600'
  chip:
    fontFamily: Figtree
    fontSize: 13.5px
    fontWeight: '500'
  player-message:
    fontFamily: Figtree
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 22px
  meta:
    fontFamily: Figtree
    fontSize: 12.5px
    fontWeight: '400'
  confidence-word:
    fontFamily: Figtree
    fontSize: 13px
    fontWeight: '600'
  measure-hero:
    fontFamily: IBM Plex Mono
    fontSize: 52px
    fontWeight: '600'
  measure-card:
    fontFamily: IBM Plex Mono
    fontSize: 46px
    fontWeight: '600'
  measure-mobile:
    fontFamily: IBM Plex Mono
    fontSize: 40px
    fontWeight: '600'
  measure-inline:
    fontFamily: IBM Plex Mono
    fontSize: 12.5px
    fontWeight: '600'
  dose:
    fontFamily: IBM Plex Mono
    fontSize: 14px
    fontWeight: '600'
  pin:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    fontWeight: '600'
  mono-meta:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    fontWeight: '400'
rounded:
  bar: 1px
  pin: 4px
  thumb: 6px
  frame: 10px
  sm: 12px
  md: 14px
  lg: 18px
  device: 44px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 20px
  '6': 24px
  '7': 32px
  '8': 64px
  gutter-mobile: 20px
  panel-padding: 32px
  card-padding: 24px
  thread-width: 640px
  rail-width: 232px
  evidence-width: 408px
  section-gap-landing: 120px
components:
  button-primary:
    background: '{colors.clay}'
    foreground: '{colors.on-clay}'
    typography: '{typography.button}'
    radius: '{rounded.full}'
    height: 52px
    height-mobile: 56px
  button-primary-disabled:
    background: '{colors.paper-2}'
    foreground: '{colors.ink-2}'
    typography: '{typography.button}'
    radius: '{rounded.full}'
    height: 52px
    height-mobile: 56px
  button-secondary:
    background: '{colors.card}'
    foreground: '{colors.ink}'
    border: '1.4px solid {colors.ink}'
    radius: '{rounded.full}'
    height: 52px
  button-dark:
    background: '{colors.ink}'
    foreground: '{colors.ink-on-dark}'
    radius: '{rounded.full}'
    height: 44px
  jump-chip:
    background: '{colors.card}'
    foreground: '{colors.ink}'
    border: '1px solid {colors.hairline}'
    typography: '{typography.chip}'
    radius: '{rounded.full}'
    height: 34px
  jump-chip-active:
    background: '{colors.ink}'
    foreground: '{colors.ink-on-dark}'
    typography: '{typography.chip}'
    radius: '{rounded.full}'
    height: 34px
  suggested-prompt:
    background: '{colors.card}'
    foreground: '{colors.ink}'
    border: '1px solid {colors.hairline}'
    typography: '{typography.chip}'
    radius: '{rounded.full}'
    height: 34px
  coach-mark:
    background: '{colors.clay}'
    foreground: '{colors.on-clay}'
    size: 28px
    size-wordmark: 26px
  coach-message:
    typography: '{typography.coach-body}'
    foreground: '{colors.ink}'
    name: '{typography.coach-name}'
    name-color: '{colors.clay}'
    timestamp: '{typography.meta}'
  player-message:
    background: '{colors.ink}'
    foreground: '{colors.ink-on-dark}'
    typography: '{typography.player-message}'
    radius: '{rounded.lg}'
    max-width: 384px
  card:
    background: '{colors.card}'
    border: '1px solid {colors.hairline}'
    radius: '{rounded.md}'
    padding: '{spacing.card-padding}'
  verdict-card:
    background: '{colors.card}'
    border: '1px solid {colors.hairline}'
    radius: '{rounded.md}'
    fault-name: '{typography.fault-name}'
    measure: '{typography.measure-card}'
    measure-color: '{colors.evidence-teal}'
  chain-link-measured:
    background: '{colors.card}'
    border: '1.2px solid {colors.ink-2}'
    radius: '{rounded.frame}'
  chain-link-inferred:
    background: '{colors.paper}'
    border: '1.2px dashed {colors.ink-2}'
    dash: '5 4'
    radius: '{rounded.frame}'
  chain-link-verified:
    background: '{colors.paper-2}'
    border: '1.4px solid {colors.ink}'
    radius: '{rounded.frame}'
  exercise-card:
    background: '{colors.card}'
    border: '1px solid {colors.hairline}'
    radius: '{rounded.md}'
    name: '{typography.exercise-name}'
    name-color: '{colors.clay}'
    dose: '{typography.dose}'
  medical-notice:
    background: '{colors.paper-2}'
    foreground: '{colors.ink-2}'
    typography: '{typography.meta}'
    radius: '{rounded.frame}'
  status-chip:
    background: '{colors.paper-2}'
    typography: '{typography.label-sm}'
    radius: '{rounded.full}'
    height: 24px
  confidence-band:
    bar-width: 4px
    bar-height: 11px
    bar-gap: 2px
    bar-radius: '{rounded.bar}'
    unlit-opacity: 0.25
    typography: '{typography.confidence-word}'
  evidence-pin:
    background: '{colors.evidence-teal}'
    foreground: '{colors.on-evidence}'
    typography: '{typography.pin}'
    size: 18px
    radius: '{rounded.pin}'
  inline-citation:
    foreground: '{colors.evidence-teal}'
    typography: '{typography.pin}'
    baseline-shift: -7px
  measurement-card:
    background: '{colors.evidence-tint}'
    border: '1.2px solid {colors.evidence-teal}'
    radius: '{rounded.md}'
    measure: '{typography.measure-hero}'
  threshold-ruler:
    track: '{colors.ruler-track}'
    track-width: 2px
    fill: '{colors.evidence-teal}'
    fill-width: 4px
    rule-tick: '{colors.ink}'
    marker-fill: '{colors.card}'
    marker-stroke: '{colors.evidence-teal}'
    marker-radius: 7px
  key-frame:
    ground: '{colors.keyframe-ground}'
    floor: '{colors.keyframe-floor}'
    floor-line: '{colors.keyframe-floor-line}'
    body-line: '{colors.body-line}'
    ghost-body: '{colors.ghost-body}'
    club: '{colors.club}'
    ball: '{colors.ball}'
    label: '{typography.frame-label}'
    radius: '{rounded.frame}'
    aspect: '322 / 360'
    cited-outline: '2px solid {colors.evidence-teal}'
  evidence-panel:
    background: '{colors.card}'
    border-left: '1px solid {colors.hairline}'
    width: '{spacing.evidence-width}'
    padding: '{spacing.panel-padding}'
    title: '{typography.panel-title}'
  evidence-placeholder:
    background: '{colors.paper}'
    border: '1.4px dashed {colors.hairline}'
    dash: '5 4'
    radius: '{rounded.frame}'
  evidence-chip:
    background: '{colors.evidence-tint}'
    foreground: '{colors.evidence-teal}'
    radius: '{rounded.full}'
    height: 30px
  evidence-chip-idle:
    background: '{colors.paper-2}'
    foreground: '{colors.evidence-idle}'
    radius: '{rounded.full}'
    height: 30px
  composer:
    background: '{colors.card}'
    border: '1.4px solid {colors.ink}'
    radius: '{rounded.full}'
    height: 56px
    send-button: '{colors.clay}'
    send-size: 36px
  composer-disabled:
    background: '{colors.paper-2}'
    foreground: '{colors.ink-2}'
    radius: '{rounded.full}'
    height: 52px
  grounding-note:
    foreground: '{colors.ink-2}'
    typography: '{typography.meta}'
    icon: lock
  drop-zone:
    background: '{colors.card}'
    border: '1.4px dashed {colors.ink-2}'
    dash: '7 6'
    radius: '{rounded.lg}'
    title: '{typography.card-title-lg}'
  library-status:
    foreground: '{colors.ink-2}'
    typography: '{typography.label}'
    icon: chevron-right
  consent-checkbox:
    box-size: 22px
    box-radius: '{rounded.pin}'
    box-background: '{colors.card}'
    box-border: '1.4px solid {colors.ink-2}'
    checked-background: '{colors.ink}'
    checked-mark: '{colors.ink-on-dark}'
    label: '{typography.body}'
    label-color: '{colors.ink}'
    hit-area: 44px
  step-log:
    done: '{colors.confidence-high}'
    done-mark: '{colors.on-confidence}'
    active: '{colors.clay}'
    pending: '{colors.hairline}'
    stopped: '{colors.ink-2}'
    name: '{typography.step-name}'
    detail: '{typography.mono-meta}'
  rail-swing-row:
    background-active: '{colors.card}'
    border-active: '1px solid {colors.hairline}'
    radius: '{rounded.sm}'
    height: 60px
  text-input:
    background: '{colors.card}'
    border: '1px solid {colors.hairline}'
    radius: '{rounded.sm}'
    height: 50px
    label: '{typography.label-sm}'
  list-row:
    background: '{colors.card}'
    border: '1px solid {colors.hairline}'
    radius: '{rounded.sm}'
    height: 56px
    title: '{typography.row-title}'
  unverified-observation-card:
    background: '{colors.paper}'
    border: '1.2px dashed {colors.ink-2}'
    dash: '5 4'
    radius: '{rounded.md}'
  bottom-sheet:
    background: '{colors.card}'
    scrim: '{colors.scrim}'
    radius: '{rounded.lg} {rounded.lg} 0 0'
    title: '{typography.panel-title}'
---

## Brand & Style

AIcoach is a coach that talks, and an instrument that shows its working. The product's promise (PRD §1) is honesty: say what the fault is, how sure the app is, and refuse to guess. The visual language makes that honesty visible through **two voices, one rule**: the coach speaks in a warm serif, and anything measured is set in teal monospace with a numbered pin that points to the evidence. A sentence without a pin is explanation, never measurement.

It should feel like a lesson notebook on warm paper, not a dashboard and not a lab report. Calm is the default: each screen holds one main thing and generous empty space. Where the direction comes from is in EXPERIENCE.md → Inspiration & Anti-patterns.

Visual references live in `mockups/` and are linked at each section below. **Where a mockup and either spine (this file or EXPERIENCE.md) disagree, the spine wins.**

## Colors

Warm neutrals carry almost everything. Three hues have fixed jobs and never swap them.

| Group | Tokens | Job |
|---|---|---|
| Surfaces | `paper` `#F4EFE6`, `paper-2` `#EBE3D5`, `card` `#FFFCF6`, `hairline` `#DAD0BF` | Paper is the page and the conversation. Paper 2 is the left rail, collapsed system lines, the disabled composer and button, status chips and the medical notice. Card holds structured content (verdict, chain, practice, Also checked, inputs, list rows, the Evidence panel). Hairline draws every 1px divider and card border. |
| Ink | `ink` `#25201B`, `ink-2` `#62584D`, `ink-on-dark` `#F4EFE6`, `ink-on-dark-2` `#CFC5B4` | Ink is text, player bubbles, the active jump chip, the dark button, a ticked checkbox and the landing's closing band. Ink 2 is secondary text, labels and chain-link outlines. Ink-on-dark 2 is secondary text on the ink band. |
| Coach | `clay` `#A4462A`, `on-clay` `#F4EFE6` | The coach mark, the "Coach" name, the feel-cue quote mark, drill and mobility names and doses, the send button and every primary CTA. Never measurements, warnings or errors. |
| Evidence | `evidence-teal` `#1E5368`, `evidence-tint` `#E2ECEC`, `on-evidence` `#FFFFFF`, `evidence-idle` `#6A6056`, `ruler-track` `#A9BDC0` | Teal is measurement only: values, pins, `[n]` citations, the "Based on:" footnote, the ruler fill and a cited key frame's outline. Tint lights the measurement card and the active Evidence chip. Idle is the Evidence chip text before any pin exists. Ruler track is the unfilled part of the threshold ruler. Never use teal for links, buttons or decoration. |
| Confidence band | `confidence-high` `#2D6A4A`, `confidence-medium` `#8C5D0F`, `confidence-low` `#8E3F33`, `on-confidence` `#FFFFFF` | Always rendered as word + colour + bars. High green also marks completed steps and passed clip checks; on-confidence is the check mark on a done step. |
| Key frame | `keyframe-ground` `#36312B`, `keyframe-floor` `#4A433A`, `keyframe-floor-line` `#5A5246`, `body-line` `#8ED3E6`, `ghost-body` `#D8CCB6`, `club` `#9A907F`, `ball` `#EFE8DA` | The skeleton figure (see Key frame). |
| Overlays | `scrim` `#25201B6B` (ink at 42%), `shadow-hero` `#25201B0F` (ink at 6%) | Bottom-sheet and drawer scrim; the landing hero card's shadow. |

**Contrast (WCAG 2.2, computed):**

| Pair | Ratio |
|---|---|
| ink on paper / on card / on paper 2 | 14.1 / 15.8 / 12.7 |
| ink 2 on paper / on paper 2 / on card | 6.1 / 5.5 / 6.8 |
| clay on paper, paper on clay / clay on card | 5.3 / 5.9 |
| teal on card / on tint; white on teal pin | 8.2 / 7.0; 8.4 |
| evidence idle on paper 2 (idle Evidence chip) | 4.8 |
| high / medium / low on card | 6.3 / 5.6 / 7.1 |
| white check on high green (step log) | 6.4 |
| body line on key-frame ground | 7.7 |
| ink on dark 2 on ink (closing band) | 9.5 |

One pair fails: medium `#8C5D0F` on paper 2 is 4.47:1, which the "possible" status chip uses in `mockups/04-result.svg`. `[ASSUMPTION]` the "possible" chip sits on `{colors.card}` with a `{colors.hairline}` border (5.6:1) instead. Two pairs are decorative and carry no state: hairline on paper (1.3:1) and the ruler track on tint (1.6:1), whose meaning is carried by the teal fill, the threshold tick and the labels.

Avoid: new hues, gradients, red error fills (the low-confidence red is a band, not an alarm), teal on non-measured content.

→ Palette in use: `mockups/04-result.svg`.

## Typography

Three families, three jobs. Load from Google Fonts: Newsreader (400, 500, 600, italic 400/500), Figtree (400–700), IBM Plex Mono (400, 500, 600). Fallbacks: Georgia serif, Arial sans, Consolas monospace.

- **Newsreader is the coach's voice:** coach messages, the italic "Coach" name, the feel cue, the wordmark, page and panel titles, sheet titles and landing headlines.
- **Figtree is the interface:** player messages, card titles, fault and exercise names, labels, buttons, chips, meta and the confidence word.
- **IBM Plex Mono is measurement only:** measured values (7%, 31°), thresholds ("rule: 4%"), pin numbers, swing-event times (0.86 s), doses (3 × 10 reps), step-log details and the "Based on:" footnote. Never decorative, never for headings.

Every size used is a token in the frontmatter; prose below refers to them by name. Minimum size anywhere is 12px. A measured value inside serif coach text stays in mono at about 0.86× the serif size (16px inside `coach-body`). `fontStyle: italic` on `coach-name`, `feel-cue` and `feel-cue-mobile` is an extension to the token spec: consumers that drop it must load Newsreader Italic for those three tokens.

## Layout & Spacing

Scale `{spacing.1}`–`{spacing.8}` (4 / 8 / 12 / 16 / 20 / 24 / 32 / 64). Cards pad `{spacing.card-padding}`, the Evidence panel `{spacing.panel-padding}`, the phone gutter is `{spacing.gutter-mobile}`, landing sections are `{spacing.section-gap-landing}` apart.

| Frame | Layout | Mockup |
|---|---|---|
| Desktop app (designed at 1440) | Left rail `{spacing.rail-width}` on paper 2 · thread on paper, content `{spacing.thread-width}` wide starting `{spacing.8}` from the rail · sticky Evidence panel `{spacing.evidence-width}` on card at the right edge. Page header (title + meta + one action or status) above a hairline, then the "Jump to" chip bar, then a second hairline. | `mockups/02-upload.svg`, `mockups/04-result.svg` |
| Phone (designed at 390 × 844) | One column, `{spacing.gutter-mobile}` gutter. Top bar: menu or back, `page-title-mobile` title with meta under it, Evidence chip right. Content, then actions in the bottom third. Full-width buttons are 350px at 390. | `mockups/03-upload-mobile.svg`, `mockups/05-other-pages.svg` |
| Landing (1440) | 80px outer margin; hero split text left / example result right (720px card); full-bleed alternating paper and card bands; closing ink band. | `mockups/01-landing.svg` |

Breakpoints and the narrow-laptop drawer are in EXPERIENCE.md → Responsive & Platform.

## Elevation & Depth

Depth is tonal, not shadowed. Paper, paper 2 and card are the three layers; a 1px hairline separates them. The only lift is the landing hero's example-result card, with a `{colors.shadow-hero}` shadow. Bottom sheets and the Evidence drawer sit on card over `{colors.scrim}`. The Evidence panel is set apart by its card fill and a hairline left edge, never by a shadow.

## Shapes

| Radius | Used by |
|---|---|
| `{rounded.bar}` | confidence bars |
| `{rounded.pin}` | evidence pins, consent checkbox |
| `{rounded.thumb}` | rail thumbnails |
| `{rounded.frame}` | key frames, chain links, inner panels, medical notice |
| `{rounded.sm}` | list rows, inputs, rail rows |
| `{rounded.md}` | cards |
| `{rounded.lg}` | player bubbles, drop zone, sheet tops |
| `{rounded.full}` | every button, chip, composer and status chip |

Line style carries meaning: **solid outline = measured; dashed outline = inferred, unverified or not yet there.** Dash patterns: 5 4 for chain links, unverified cards and evidence placeholders; 7 6 for the drop zone; 3 3 for "no thumbnail" rail tiles; 9 7 for the address reference line inside key frames.

## Components

Names match the YAML keys and EXPERIENCE.md → Component Patterns. Sizes and colours are in the YAML; prose covers anatomy and anything without a token.

### Identity and conversation

→ `mockups/04-result.svg` (desktop), `mockups/03-upload-mobile.svg` (phone)

**Coach mark and wordmark.** A clay circle with a paper flag on a short pin and a curved ground stroke. Wordmark: "AI" in clay italic Newsreader + "coach" in ink, `{typography.wordmark}` in the rail, `{typography.wordmark-large}` on sign in.

**Coach message.** Mark + "Coach" + time, 8px gap between name and time. Body in Newsreader, no bubble, left-aligned on paper. One or two sentences per message.

**Player message.** Right-aligned ink bubble with "Rory · 18:09" meta above it. The upload echo shows a first-frame thumbnail, file name and "3.8 s · 120 fps" in mono meta; while uploading `[ASSUMPTION]` a 4px clay progress bar runs along the bubble's bottom edge.

**Collapsed system line.** A 40px paper-2 pill: check circle + "Clip received · 7-iron_dtl.mov · 3.8 s · analysed in 41 s" + "Show ▾".

**Typing indicator.** Coach mark + three ink-2 dots + italic "Coach is watching your swing…" (analysing) or no text (chat).

**Composer.** Card pill with ink border, placeholder "Ask about this result…" in ink 2, clay send circle with a paper arrow. Disabled: `composer-disabled`, no border, placeholder "You can ask the coach once the result is ready."

**Grounding note.** Always under the composer: lock icon + "Answers are based only on this analysis — no new faults, numbers or drills." Phone short form: "Answers are based only on this analysis."

**Suggested prompt.** Card pills above the composer; wrap to two rows on desktop, one full-width pill on the phone.

**"Based on" footnote.** Mono teal `{typography.pin}` under every grounded coach answer: "Based on: [3] hip movement · [2] impact frame · wall drill".

### Result

→ `mockups/04-result.svg`; phone result `mockups/03-upload-mobile.svg`; no-fault and unverified card `mockups/05-other-pages.svg`

**Page header.** Title `{typography.page-title}`, meta line, and at the right the **library status** (below).

**Library status.** Replaces the removed "Save to swing library" button. Plain text "In your swing library" in `{typography.label}` ink 2 with a chevron, no pill, no border; the whole line links to the clip detail. Phone: the same line under the top-bar meta `[ASSUMPTION]`.

**Jump-to chips.** "Jump to" meta label, then pills: Verdict · Why · Practise · Also checked · Ask the coach. The active one is `jump-chip-active`.

**Verdict card.** Card split by a vertical hairline: left = "Verified fault" label, fault name, confidence band; right = pin `3`, measurement name, the value in `{typography.measure-card}` teal, unit in ink 2, and "rule: 4%" in mono meta. Phone: one card with fault, band, value (`{typography.measure-mobile}`) and the two key-frame thumbnails beside it.

**Feel cue.** Clay quote mark (`{typography.quote-mark}`, `{typography.quote-mark-mobile}` on the phone), the cue in `{typography.feel-cue}`, and a meta line "Feel cue · check it in the impact frame `[2]`".

**Fault chain.** One card, three links left to right joined by 18px ink-2 arrows: **Likely cause** (`chain-link-inferred`), **Mechanism** (`chain-link-measured`), **Fault · verified** (`chain-link-verified`). Each link: label in `{typography.label-sm}`, title in `{typography.card-title}`, measured value in inline mono teal with its pin, then the confidence band. Under the card: a dashed swatch + "Dashed = inferred from a pointer, not measured directly."

**Exercise card.** One card, two halves split by a hairline: label ("Drill · for early extension" / "Mobility · for the likely cause"), name, dose, two or three lines of instruction in ink 2. The mobility half always carries the **medical notice**: "Generic guidance, not medical advice — see a physiotherapist if you feel pain."

**Also checked.** Card with a `{typography.card-title-sm}` title and a right-aligned count. One row per other rule-table fault: name, status chip, confidence band, pin square right; one ink-2 line under it.

**Status chip.** Paper-2 pill (see the contrast note under Colors) with one word in `{typography.label-sm}`: "possible" in `{colors.confidence-medium}`, "not found" in ink 2. Text only, never an icon.

**Confidence band.** Three bars, then the word in the same colour: high = 3 lit; medium = 2 lit + 1 unlit; low = 1 lit + 2 unlit. Text always reads "confidence: high / medium / low". Never colour alone, never a percentage.

**Unverified observation card.** Dashed ink-2 outline on paper: label "Unverified — confirm with a coach", the observation in italic Newsreader, the low band, and "No drill: this is not in my rule table."

**Inline message.** `[ASSUMPTION]` One line of ink text under the control that caused it, with a small `{colors.confidence-low}` × mark. No red fills, no banners. Used for refused files, form errors, network errors, the frame-rate warning (with a medium-coloured `!` instead of ×) and the "taking longer" line (followed by a `button-secondary` "Try again").

**Mock-mode label.** `[ASSUMPTION]` "Mock mode" in `{typography.meta}` ink 2 in the rail footer (phone: menu sheet footer). No colour, no badge.

### Evidence

→ `mockups/04-result.svg` (panel), `mockups/02-upload.svg` (pre-upload and analysing panel), `mockups/03-upload-mobile.svg` (chip and tray)

**Evidence pin.** Teal square with a white mono number. Numbering is per analysis: 1–2 key frames, 3+ measurements. Inline, the same number appears as a raised teal `[n]` **inline citation** after the measured value.

**Key frame.** Drawn on keyframe ground in a 322:360 box. Construction (from concept 02): translucent ghost-body capsules (round caps, 10% opacity far side, 17% near side), a 3.4px body-line skeleton with round joins, keypoint dots of 5.6px radius (ground fill, 2.6px body-line stroke), the club as a 3.4px club-colour line with the ball at its tip, floor band at the bottom. The **hip keypoint is ringed** (13px ring at 80%, 6.5px solid dot). The address frame draws a dashed vertical reference line (paper, 2.4px, 9 7, 75%) through the address hip. The impact frame repeats that line, overlays the **address pose dashed** (body line, 2.4px, 7 6, 40%) and draws a **"+7%" dimension arrow** from the address hip line to the impact hip in body line. Under each frame: name in `{typography.frame-label}` and event time in mono meta. A cited frame gets its teal outline 3px outside the frame. No graph paper, no axes, no coordinate ticks.

**Measurement card.** Evidence tint with a teal border: measurement name, value in `{typography.measure-hero}`, threshold ruler, confidence band.

**Threshold ruler.** Inside the measurement card: track, teal fill from 0 to the value, an ink tick at the rule threshold, a card-filled marker with a 3px teal ring at the value. Mono labels "0%", "rule 4%", "10%".

**Evidence panel.** Title "Evidence" with a teal pin icon, pin count in mono teal right, one ink-2 subtitle line. Content, top to bottom: two key frames side by side (164px each, 16px gap), the dashed-line legend, the cited measurement card, a "3 more measurements" disclosure row, a "Clip checks passed · 3 of 3" disclosure row.

**Evidence placeholder.** Before and during analysis, each frame and the measurement card is a dashed paper box with a centred meta label ("Address frame", "measuring…"). Before upload the panel also shows a top-down "Where to put the phone" diagram.

**Evidence chip.** A pill reading "Evidence · n" in teal on tint (`evidence-chip`); before any pin exists, `evidence-chip-idle`. Phone: top bar right. Narrow laptop: page header right, before the library status.

**Evidence tray (phone) and Evidence drawer (narrow laptop).** Tray: a bottom sheet with a 40 × 5px hairline grab handle, "Evidence · pinned live" title in teal, frames and measurements in a horizontal row (placeholders while measuring). Drawer: the Evidence panel's content at `{spacing.evidence-width}`, sliding in from the right over `{colors.scrim}`, with a close button top right `[ASSUMPTION]`.

### Upload and analysis

→ `mockups/02-upload.svg` (desktop), `mockups/03-upload-mobile.svg` (phone)

**Drop zone.** `{spacing.thread-width}` card with a dashed ink-2 border: an upload circle (paper 2, clay arrow), "Drop your swing clip here" in `{typography.card-title-lg}`, "or choose a file · mp4 or mov · max 15 s", a hairline, then one library note: "Goes into your swing library" (`{typography.card-title-sm}`) and "Stored on the AIcoach server until you delete it. Only you can see it." in meta `[ASSUMPTION]` copy. No toggle, no save control. Disabled (storage limit) `[ASSUMPTION]`: paper-2 fill, ink-2 text, the limit message as an inline message under it.

**Ready-to-send preview (phone).** Clip preview card on keyframe ground with the first-frame skeleton and a play mark, file name in `{typography.label}`, "3.8 s of 15 s · 120 fps" in mono meta, the coach line, the same library note in a card, then "Send to the coach" (`button-primary`) and "Choose a different clip" (text button).

**Step log.** Card with five rows (Pose · Swing events · Measurements · Rule table · Explanation): a 10px status circle joined to the next by a vertical line, the step name, mono details right-aligned. Circle states: done = high green with a check; active = clay partial ring; pending = hairline ring; **stopped** (rejection) = ink-2 ring with ×. A 4px clay progress bar with "3 of 5" in mono closes the card. The typing indicator sits under it.

**Rejection reason row.** Card row: an ink-2 × mark, the reason in `{typography.label-strong}`, one line of explanation in ink 2, and a clay "Filming guide · step n ›" link. → `mockups/05-other-pages.svg`

### Forms, lists and navigation

→ `mockups/05-other-pages.svg`; rail in `mockups/02-upload.svg`

**Text input.** Card field with hairline border; label above in `{typography.label-sm}`.

**Consent checkbox.** Sits between the password field and "Create account". A 22px box, unticked by default: card fill, 1.4px ink-2 border (6.1:1 on paper). Ticked: ink fill with a paper check. The label is `{typography.body}` ink, beside the box: "I understand that every swing clip I send is stored in my swing library on the AIcoach server until I delete it." The label is part of the target; the hit area is at least 44 × 44px. Focus shows the focus ring around the box. While unticked, "Create account" is `button-primary-disabled` and a meta line under it reads "Tick the box to create your account." `[ASSUMPTION]` copy.

**List row.** Card row with a chevron right; title in `{typography.row-title}`. Library rows add a 46px key-frame thumbnail (or a dashed "no thumbnail" tile for "Cannot analyse") and a meta finding line. Account analysis rows show "date · finding" and a meta clip line, and end in an ink-2 trash icon.

**Rail swing row.** `{rounded.sm}`; the active row on card with a hairline border. 38px key-frame thumbnail, or a dashed paper tile with × for "Cannot analyse"; title "7-iron · today" in `{typography.label}`; finding "Early extension · high" in meta.

**Clip detail.** `[ASSUMPTION]` not mocked. Page header (date, meta finding; "clip deleted" rows have no clip detail) then the clip in a `{rounded.md}` video frame with native controls on keyframe ground, then "Open analysis" (`button-primary`) and "Delete clip" (`button-secondary`).

**Disclosure rows.** A chevron says it opens in place. Three forms: the "Read my full explanation · 118 words ▾" text row (`{typography.row-title}` + meta count); the Evidence panel's "3 more measurements ›" row (paper 2, `{rounded.sm}`, 66px) and "Clip checks passed · 3 of 3" row (hairline outline, 46px, green check circle, mono count); and the phone's "Next: what to practise · 1 drill · 1 mobility" row (card, hairline, full pill).

**Filming guide step.** "Step 3 of 6" in clay `{typography.label-strong}`, the rule in `{typography.screen-headline-mobile}`, a card with a top-down placement diagram (dashed target line with arrow, phone block, player ellipse in ghost body, mono distance "2.4–3.7 m · 8–12 ft" in teal), two to four lines of reason in ink 2, six 8px step dots (current = clay, others = hairline), then Back (`button-secondary`) and Next step (`button-primary`) side by side. Overview rows: a numbered paper-2 circle, the rule, a chevron.

**Buttons.** Primary = `button-primary` (one per screen). Disabled primary = `button-primary-disabled`. Secondary = `button-secondary` ("Read the filming guide", "Ask the coach about this", "Delete account", "Keep my account", "Try again"). Dark = `button-dark` ("New swing"; "Delete everything" and other destructive confirmations inside a sheet).

**Bottom sheet.** Card with `{rounded.lg}` top corners over the scrim, a 40 × 5px hairline handle, a `{typography.panel-title}` title, ink-2 consequences, then the actions stacked full width.

**Focus ring.** `[ASSUMPTION]` 2px `{colors.evidence-teal}` outline at 2px offset on every interactive element (not drawn in the mockups).

### Landing

→ `mockups/01-landing.svg`

**Landing blocks.** Hero (`{typography.display-hero}` headline, `{typography.body-lg}` body, primary + secondary CTA, meta line "For golfers between +2 and 15 handicap. A practice tool, not for competitive rounds."); the example-result card; "The coach talks. The evidence stays pinned." legend (coach / measured / dashed); a three-step film → send → read row; three fault tiles (key frame + name + mono measurement + clay drill); three honesty cards (Cannot analyse, No verified fault found, grounded refusal); an ink closing band with a clay CTA and the privacy line "Your clips are private. Each one stays in your swing library until you delete it." in ink-on-dark 2.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put every measured number in mono teal with its `[n]` pin | Set a measured number in serif or sans, or a non-measured word in teal |
| Show the confidence band as word + colour + bars, every time | Show a band as colour only, an icon only, or a percentage |
| Draw inferred, unverified and pending things dashed; measured things solid | Use dashed lines for decoration |
| Let the coach speak in Newsreader, one or two sentences per message | Write coach paragraphs; the full explanation stays behind "Read my full explanation" |
| Use clay for the coach and for the one primary action per screen | Use clay for errors, warnings or measurement |
| Draw the golfer as the 02 skeleton on the key-frame ground, hip ringed | Use photos, silhouettes, graph paper, axes or coordinate ticks |
| Keep one main thing per screen and generous paper | Add dashboards, score dials, streaks or badges |
| Keep the grounding note under every composer | Hide or shorten it below "Answers are based only on this analysis." |
| Carry the medical notice on every mobility exercise | Show a mobility exercise without it |
| Separate layers with tone and a 1px hairline | Add drop shadows to cards or panels |
| Show that a clip is in the swing library as a status line | Add a save toggle or save button anywhere |

## Open Questions

Visual questions live here; product and behaviour questions live in EXPERIENCE.md → Open Questions.

1. **Dark mode.** No decision. `[ASSUMPTION]` light only for the MVP; no `-dark` tokens defined.
2. **"possible" chip contrast.** Accept the move to card fill (5.6:1), or darken `confidence-medium`.
3. **Font loading.** Google Fonts from a CDN or self-hosted? NFR-2 runs the app on the author's laptop, and a phone on the same Wi-Fi may have no internet at the range. Decide in architecture.
4. **Landing on the phone** is not mocked; it follows the phone rules above.
