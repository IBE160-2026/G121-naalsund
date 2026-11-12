# 11 · Riso Zine

**Thesis:** Every result is a small two-ink practice zine about one swing. How sure the coach is shows as how much ink it prints.

## Rationale

This is for the club golfer, +2 to 15 handicap, who already trusts the photocopied drill sheets that coaches hand out at the range. AIcoach borrows that format: a stapled zine made by the club's coaching group, printed in fluorescent pink, teal and black on grey-blue duplicator stock. A zine is a modest object. Nobody expects one to be infallible, and that is why it suits a coach whose main selling point is honesty. Confidence isn't hidden in a tooltip. It's printed: a solid ink square means high, a half screen means medium, and a light dot screen means low. The same three densities appear on every measurement, chain link, library row and chat source. The golfer figures are halftone prints with misregistered plates. The result reads like a spread about *your* swing, and the drill and mobility exercise are cut-out cards you can take to the range. The chat is the zine's letters page, but you still type into it and get an answer.

## Palette

| Hex | Role |
|---|---|
| `#E3E8EA` | Paper: grey-blue duplicator stock, the page ground (deliberately not cream) |
| `#FBFBF7` | Card stock: spreads, cut-out cards, inputs |
| `#FF48B0` | Fluorescent pink ink: the fault plate, primary buttons, backside line at address, highlighter fields (only behind black text, never as text) |
| `#00838A` | Teal ink: the body plate, headline key plate, confidence swatches, step numerals (large sizes only) |
| `#13285E` | Navy: the overprint, where pink and teal overlap. Verified stamps, measurements ("7%"), links, feel cue |
| `#1D1B20` | Riso black: body text, body lines on key frames, club, destructive buttons |
| `#F7C6E1` | Pink at about 30%: feel cue strip, current analysing pass, letters from the player |

## Typography

- **Dela Gothic One** 400: headlines, verdicts, stamps, step numerals, "3 × 10 reps". A heavy, wide Japanese-poster gothic that keeps its shape when overprinted with a misregistered second plate. Headlines are set in sentence case and never tracked out.
- **Zilla Slab** 400/500/600/700 + italic: all reading text, UI, labels and chat. Its slab serifs look like a typewritten handout. Italic carries the feel cue, captions and the player's letters.
- Scale: 88 / 58 / 40 / 34 / 24 display; 25 / 22 / 18 / 17 / 15 / 13 text. Body is 17–18 px with a 1.5 line height and lines under 75 characters.

## Signature moves

1. **Confidence printed as ink coverage.** Solid ink means high, a 50% halftone screen means medium and a 15% screen means low, and the band word is always printed beside the swatch. The landing explains it once ("Confidence is printed as ink"). After that it reads without a legend.
2. **True overprint, real misregistration.** Every headline and figure is printed as two plates: pink offset by a few pixels, teal on top, and **navy wherever they overlap** (computed with SVG masks, not faked with opacity). Golfer figures are halftone dot screens (SVG patterns at riso screen angles: 15° teal, 75° pink) over a flat pink plate. Ink speckle drops out of solid areas.
3. **Stapled-page rhythm.** Landing and result are a sequence of two-page spreads with a fold, two staples and page numbers. The result is a four-page issue about your swing: verdict + key frames, then fault chain + explanation.
4. **Cut-out practice cards.** Wall drill and 90/90 hip rotation are cards with dashed cut lines and scissors, each with its own halftone illustration (wall at the backside line, seated 90/90). The mobility card carries "Generic guidance, not medical advice — see a physiotherapist if you feel pain".

## How the AI chat lives here

The chat is **"Letters to the coach"**, the last page of the result issue. Rory's question is set as a pink-tint letter. The coach's reply is typeset on stock with a **"Based on"** row of source chips (7% of body height · Impact key frame · Wall drill), and each chip carries its confidence ink. A drawn page icon sits next to the grounding note: "Answers are based only on this analysis. The coach will not add faults, numbers or drills." Suggested prompts are **tear-off tabs**, like a noticeboard flyer, and tapping one sends it. The input is a real single-line field with a caret and a pink "Send" button. A note explains that off-topic questions get "cannot answer from your swing". On mobile the chat docks as a bar at the bottom of the result screen. The verdict spread links down to it with "Write to the coach at the end of this issue".

## Risks / trade-offs

- **Charm vs. seriousness.** Fluorescent pink and stamps could read as playful to a +2 player. The coaching content stays plain and exact, and the bold ink is kept for structure, but a more conservative audience may want a quieter variant (e.g. teal + black only).
- **Halftone costs legibility.** Dot screens under text would hurt readability, so text never sits on a screen; it sits on card stock or flat tint. In code, the halftone patterns and overprint masks need care to stay sharp and fast on low-end phones. Rendering them as pre-built SVG/PNG assets is likely.
- **Spreads vs. scrolling.** The fold-and-staple rhythm is a desktop conceit. On a phone it collapses into single pages, and the zine identity there rests mostly on the inks, stamps and cards.

---

## Design plan (pass 1)

**Tokens**
- Colour: paper `#E3E8EA`, card `#FBFBF7`, pink `#FF48B0`, teal `#00838A`, overprint navy `#13285E`, riso black `#1D1B20`.
- Type: Dela Gothic One (display, overprinted), Zilla Slab (text/UI).
- Layout: two-page spreads (1312 wide, fold at centre, staples at ¼ and ¾ height). Left page carries words or the verdict, right page carries the picture or evidence. Everything is left-aligned; centred text appears only inside stamps and buttons. Pasted items (photos, notices, cards) rotate up to ±1.6° as paste-up evidence. Data (rulers, chain, tables) is never rotated.
- Principles: (1) ink density = certainty, nowhere else; (2) one boldness spent: the overprint; everything else is quiet slab text on stock; (3) numbers only where the content really is a sequence (how-it-works steps, filming-guide steps that rejections link to, analysing passes, drill steps); (4) no text on halftone.

**Landing wireframe**
```
[AIcoach~]  a practice zine…            How it works  Example  Honesty  Sign in [Create account]
=============================================================================================
 FILM ONE         |                      ┌───────── pasted halftone print ──────────┐
 SWING.           |                      │  7% box ← ┆ │  golfer (pink+teal plates) │ [Verified stamp]
 GET ONE          |                      │           ┆ │                            │
 HONEST FIX.      |                      │  caption: impact frame, synthetic data    │
 sub (3 lines)    |                      └───────────────────────────────────────────┘
 [Create account] [See an example result]
-------------------------------- Issue 1 ---------------------- Example data is synthetic --
┌──── page 2 ───────────────┬──── page 3 ────────────────────┐
│ How it works  1 2 3       ║ Where to put the phone: ticks  │  (top-down DTL diagram)
└───────────────────────────┴────────────────────────────────┘
┌──── page 4: key frames ───┬──── page 5: verdict, ruler, chain, feel cue ┐
┌──── page 6: honesty + ink legend ║ page 7: pasted notices (reject / no fault / possible) ┐
 Three faults table (fault · measure · cause · drill · mobility)
 Back cover: "Bring one swing." [Create account]   colophon
```

**Result wireframe**
```
issue strip: date, club, fps            [ ] Save to swing library   Delete analysis
┌ p1: EARLY / EXTENSION, stamps, statement, 0–10% ruler, feel cue strip ┃ p2: address | impact key frames ┐
┌ p3: fault chain (cause→mechanism→fault, hip-turn diagram)            ┃ p4: explanation, also checked   ┐
 Take these to the range:  [✂ Wall drill card]  [✂ 90/90 card + medical disclaimer]
 Letters to the coach: letter / reply + "Based on" chips / input [Send]   |  tear-off prompts
```

## Plan review (what changed from the first instinct, and why)

- **Paper:** my first instinct was cream newsprint with red + blue riso. Nine of the ten existing concepts already sit on cream or warm off-white, and #10 owns blue + red. I switched to **grey-blue duplicator stock with fluorescent pink + teal**, which has its own overprint colour (navy) to use for meaning.
- **Hero:** I first sketched the feel-vs-real as an address/impact silhouette overlay. #10 (Kinetic Poster) already does ghost-vs-solid overlay, so I dropped it. The overlay is now only a riso *texture* (plate misregistration on one pose), and the address/impact comparison is shown as two side-by-side key frames with body lines, which is also closer to the PRD's "key frame".
- **Big-number hero:** the "7%" started as a giant stat. That is the hero-metric template, so 7% now lives on a ruler against the 4% threshold and in a small callout on the print.
- **Display face:** my first pick was a round fat face (Bagel-style), but it felt too cute for adult club golfers. Dela Gothic One is just as heavy but more poster than toy.
- **Confidence encoding:** colour-coded chips (green/amber/red) were the default. I replaced them with ink coverage, which belongs to this world and doesn't depend on hue (it also works for colour-blind readers and in black-and-white print).
- **Progress vs. confidence:** analysing passes first reused the density squares. I changed them to filled/partial/dashed circles so ink density means only certainty.
- **Rejected along the way:** all-caps labels, eyebrows above headings, middle-dot meta strings, arrows appended to buttons, and text set on halftone.

## Self-critique notes (after rendering)

- Fixed: key frames overflowed their panels, the chat reply collided with the input, notice text overlapped a stamp, and back-cover copy sat on dots (it now sits on card inside a halftone frame).
- Still a stretch: the seated 90/90 figure is schematic. A real build would commission proper halftone illustrations per drill. The first result spread has some empty space under the feel cue, which could take the hip-turn diagram on mobile.
