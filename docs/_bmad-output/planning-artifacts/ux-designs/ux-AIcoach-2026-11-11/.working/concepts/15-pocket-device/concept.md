# 15 · Pocket Device: "AIcoach swing unit CU-1"

**Thesis:** AIcoach is a small, well-made instrument you load one swing into. It answers on its own display, and the full explanation comes as printed pages from its owner's manual.

## Rationale

This concept is for the 11-handicap who practises after work and trusts tools more than talk: a rangefinder, a good wedge, a launch monitor at the shop. Turning the coach into a piece of hardware makes the honesty physical. The device has a fixed set of display messages ("cannot analyse", "no verified fault", "unverified"), a confidence meter that always shows, and a clip slot that accepts exactly one swing. A device can only show what it measured, and that is the promise PRD §1 makes. The playful object (screws, knurled dial, speaker grille, a swing clip as a labelled cartridge) makes a strict tool feel friendly instead of clinical. The reading itself happens on paper: the explanation, fault chain and drills are set as owner's-manual pages in plain proportional type, so the result page still reads like a coach's note rather than a gadget readout.

## Palette

| Hex | Role |
|---|---|
| `#E5E4EE` | Studio sweep: page background, the "product shot" backdrop |
| `#A3A7D6` | Anodised periwinkle device body (gradient `#B7BBE4` → `#8E92C4`, edge `#7B7FB3`) |
| `#2B2D54` | Recess: display bezels, slot, grille holes, switch tracks |
| `#1D1F3F` | Ink: silkscreen and printed text (secondary `#3A3D6B`, `#4A4D78`) |
| `#CDD3B6` | Reflective LCD (segment ink `#262B1E`, silhouette `#8C9476`, unlit segments `#C7CDAF`) |
| `#F4C430` | Signal yellow: the one primary key per view ("Create account", "Choose clip", "analyse swing", "Load another clip"), the active stage LED, and the switch when it is on |
| `#FBFBF8` | Manual paper (rules `#D7D7E2`) |

## Typography (Google Fonts)

- **Encode Sans Expanded** 500–800: device silkscreen, headlines, keycap labels. A wide grotesk reads like printed panel lettering. Labels stay lowercase, as small silkscreen does, with no all-caps eyebrows.
- **Encode Sans** 400–700: all reading text on manual pages, the explanation and chat. It is the same family at normal width, so the device and the manual share one voice.
- **DotGothic16**: only for short strings on the LCDs (frame times, "early extension: verified", stage names). Big numbers such as **7%** are drawn as authored 7-segment SVG, not set in a font.

## Signature moves

1. **The device itself as the hero and result screen.** The key frames sit on a reflective LCD with the wall line and the 7% arrow. A 7-segment readout shows "7%, limit 4%", with a three-bar confidence meter next to it. A rotary mode dial labelled load / analyse / result / talk / library shows where you are.
2. **Swing clip = cartridge.** Uploading means inserting a labelled cartridge (`rory_7iron.mov, 7-iron, 120 fps`) into the clip slot. The swing library is a tray of cartridge spines.
3. **Owner's-manual pages** carry everything that needs reading: "Your result p. 1", "Fault chain p. 2", "Practise p. 3", "Also checked p. 4", "Display messages p. 14". On the landing page the honesty story is told as the manual's list of display messages.
4. **Physical honesty controls.** "Save to my swing library" is a real slide switch, off by default, with the consent text printed beside it. "Delete account" sits under a lift-up guard cover.

## How the AI chat lives here

Chat is the device's **talk-back** module: a tall companion unit next to the result, with its own speaker grille and LCD. The coach's lines are set in proportional type on the LCD. Rory's lines are ink bubbles. Each answer ends with a dashed **"from this analysis"** source slip (hip measurement 7%, impact key frame 1.91 s, wall drill). The second exchange shows the grounding at work: "This analysis didn't measure your grip, so I can't say." The note "Answers are based only on this analysis. Talk-back won't invent faults, numbers or drills." is printed on the module, and the suggested prompts are physical keycaps.

## Design plan (pass 1)

- **Tokens:** sweep `#E5E4EE`, body `#A3A7D6`, recess `#2B2D54`, ink `#1D1F3F`, LCD `#CDD3B6`, signal `#F4C430`, paper `#FBFBF8`. Type: Encode Sans Expanded (silkscreen), Encode Sans (reading), DotGothic16 (LCD). Corners are graded by object, not one radius everywhere: body 48, modules 22–36, keys 10–12, paper 3.
- **Layout principles:** a 1000 × 640 canonical device on a strict internal grid (screen 560 wide on the left, readout and dial column on the right, a bottom row with grille, switch and primary key). Page content is left-aligned on an 80 px margin. Manual pages are set flush-left and ragged-right. The device is drawn once in code and reused at every size.
- **Result page wireframe:**

```
[AIcoach]                              Load a clip  Swing library  Filming guide  Account
Result for rory_7iron.mov
   ┌cartridge┐
┌──┴─────────┴──────────────── device ──────────────┐   ┌─ talk-back ─┐
│ [LCD: address | impact, wall line, 7% arrow] [7%] │   │ grille      │
│ [dot strip: early extension: verified]  (dial)    │   │ LCD chat    │
│ grille   save-switch            [analyse another] │   │ source slip │
└───────────────────────────────────────────────────┘   │ input       │
┌ p.1 Your result ───────────────────────────────────┐  │ note        │
│ Early extension [Verified] ▮▮▮ high · measurement │  │ [keycap]x3  │
│ explanation (≤150 words)        │ feel cue (tint)  │  └─────────────┘
└────────────────────────────────────────────────────┘
┌ p.2 Fault chain: cause → mechanism → fault (figure, evidence, confidence) ┐
┌ p.3 Practise: wall drill (fig) │ 90/90 (fig) + not-medical-advice note ┐
┌ p.4 Also checked: loss of posture (possible, gauge 5/6/9°) │ over the top ┐
```

- **Upload:** loaded device on the left with the cartridge in the slot, a separate switch plate for the library opt-in, the "Before you film" manual page on the right, and below them a five-frame "display sequence" strip with LEDs for pose → swing events → measurements → rule table → explanation.

## Plan review: what changed from my first instinct

- **Body colour.** My first instinct was a light-grey aluminium body with an orange signal key and all-caps silkscreen. That is the generic "designer synth" look, close to the trade dress of a well-known hardware maker, and it nearly copies concept 02's grey + `#E2471A`. I switched to an anodised periwinkle body with a signal-yellow key and lowercase silkscreen. Yellow on periwinkle is also a stronger "press me" signal.
- **What goes on the display.** At first I had everything on the dot-matrix display. Long dot-matrix text is tiring, and a golfer must be able to read the result, so the font is limited to short LCD strings. All reading moved to printed manual pages in Encode Sans.
- **Chat.** My first chat idea was a curling thermal-printer receipt. It was a gimmick that would hurt readability and scrolling, so I replaced it with a talk-back module whose prompt chips are keycaps.
- **Analysing state.** The first draft showed a shrunken second device next to a stage list. That duplicated the stage list and pushed device labels under 12 px, so I replaced it with one five-frame display-sequence strip at full size.
- **Golfer figures.** I kept them in a deliberately graphic style: a thick-stroke silhouette with the pose skeleton drawn over it, like a real device's pose overlay. The aim was no pseudo-photo rendering, and no graph-paper or error-bar science look, which keeps it away from concept 02.

## Self-critique after building

- The device hero is the one bold element. Everything around it (nav, manual pages, tables) is kept quiet.
- I checked the PNG renders and fixed several things: explanation overflow, an unreadable "7" (the unlit segments were too strong), "AIcoach" reading as "Alcoach" in the wordmark (now drawn with a serifed I), and a Nelly frame that claimed a direction a down-the-line view can't really show (now a dashed "unverified" box).

## Risks / trade-offs

- **Skeuomorphism tax.** In a real build, the shading, screws and knurling need careful CSS/SVG work and good performance on mobile. If it is done cheaply it will look like a toy rather than an instrument.
- **"Gadget" can undercut "coach".** Some golfers may read a device as a measuring tool rather than advice. The manual pages and the warm coach voice have to carry the human side.
- **Body text "AIcoach" in Encode Sans** still reads as "Alcoach" in running text. Only the wordmark is fixed. A shipped version would need a face or ligature with a serifed capital I.
