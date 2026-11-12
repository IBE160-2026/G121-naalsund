# 13 · Anatomy Atlas

**Thesis:** The body is the subject. AIcoach draws your swing as an anatomical atlas plate and follows the fault back through your joints to where it starts.

## Rationale

This is for the 2 to 15 handicap player who has been told "you stand up out of it" and never told why. An atlas plate is the most trusted way people have to show cause inside a body: a precise figure, a few lettered points and a thin leader line to each label. That form suits an honest coach. Every label sits next to the evidence it points at, and the leader line itself shows how sure the app is. The fault chain stops being a list and becomes a route through the body: the lead hip (A) turns too little, the pelvis (B) slides toward the ball, and the spine (C) rises. That is early extension. Because the cause sits in the body, the mobility exercise gets its own plate, the same size as the drill. The atlas is also strict about its limits: it says it shows the pose found in the video, and the page says plainly that this is coaching, not diagnosis.

## Palette

| Hex | Role |
|---|---|
| `#E4E2DB` | Bone: page ground (greyed, cooler than cream) |
| `#EFEDE7` | Plate paper: inside atlas plate frames |
| `#25323C` | Slate ink: text, outlines, buttons, leader lines |
| `#53616C` | Secondary slate: captions, thresholds, muted text |
| `#A9BCC6` | Tissue: the translucent body (outline `#7C93A0`) |
| `#F7F3EA` | Bone fill: skeleton |
| `#B0283C` | Bodily red: **only** the joint in question and the cause route. Never a button or a heading |
| `#34444F` | Consult slate: the AI coach chat panel |

## Typography (Google Fonts)

- **Atkinson Hyperlegible Next** (400/700/800). It does all the UI, the headlines and every number. It was designed for legibility in low vision, which helps on a phone in bright sun at the range. It reads clinical without feeling cold. Headlines are 800 with slightly tight tracking.
- **Spectral italic** (400/500). It is used only for atlas annotation: plate captions ("Plate 1. Impact, seen down the line"), chain roles ("Likely cause"), scale labels ("threshold 4%") and short marginal notes. It is never used for headlines.

## Signature moves

1. **The plate:** the golfer is a translucent, side-on body outline over a simplified skeleton (pelvis, vertebrae, ribcage, femurs). The address pose stays faintly behind the impact pose. An "address line" with a red 7% dimension shows the hips moving toward the ball.
2. **Confidence is the leader line:** a solid leader means high, dashed means medium and dotted means low. The text "Confidence: …" always appears too. A "Key to the plates" legend on the landing page teaches this once.
3. **The cause route:** a red dotted route runs A → B → C through the body on the hero plate. On the result page, three plates (a pelvis seen from above with a 31° arc against ~45°, a close-up of the pelvis sliding forward, and the whole figure) are joined by red arrows.
4. **Equal-weight practice plates:** the wall drill is shown side-on with the wall hatched and the half-swing arc. The 90/90 hip rotation is shown from above with a rotation arc. They are the same size, and each says which link it works on ("Trains B", "Works on A").

## How the AI chat lives here

The chat is a slate "consult" panel next to the plates. It can **point at the body**. When the coach mentions the pelvis, a chip ("Showing B on Plate 1: pelvis at impact") lines up with the B label, a line joins them, and the B label is highlighted. That ties every answer to a lettered point that is already evidenced. "Answers are based only on this analysis. No new faults, numbers or drills" sits under the title. The secondary sheet shows the coach declining to talk about grip, because it was not measured, and sending a pain question to a physiotherapist.

## Risks and trade-offs

- An anatomical skeleton can feel medical or a little morbid to some golfers. It also risks implying a diagnosis, so the "coaching, not diagnosis" line has to stay visible, and the figure has to stay schematic.
- Drawing a figure from 2D pose estimates is an honest picture of the data, but a real build needs a solid way to fit the plate figure to the keypoints. If the fit is poor, the figure looks wrong on unusual body shapes.
- The pages are long and dense with annotation (the landing page is about 4500 px). The atlas grammar rewards close reading, while players at the range only glance, so the phone result has to stay much more compressed.

## Design plan (pass 1)

- **Color:** bone ground, plate paper, slate ink, translucent tissue blue-grey, bone fill, one bodily red for the joint in question, a consult slate for the chat.
- **Type:** a hyperlegible sans for everything people read and act on. A book italic only for the atlas's own annotations.
- **Layout:** left-aligned, ragged-right text. The plates are the largest objects on every page. Each plate's labels sit in a margin column, joined to the body by elbowed leader lines. Desktop result:

```
+-------------------------------------------------------------+-----------------+
| AIcoach                       Upload  Library  Guide  Acct  |                 |
| Early extension   Verified fault  --- Confidence: high      | ASK THE COACH   |
| +---------------------------------------------------------+ | (slate panel)   |
| | [key frame: address] [key frame: impact]   (C) Spine    | |  Rory: why...   |
| |   figure+skeleton      figure+ghost   ---  (A) Lead hip | |  Coach: ...     |
| |   address line         7% dim ------------ (B) Pelvis ==|=|= [B chip]       |
| |  scale 0..10%  threshold 4  ^7%           Plate 1 cap.  | |  ...            |
| +---------------------------------------------------------+ |  chips / input  |
| How it happened: [A dial 31°] -> [B pelvis] -> [C figure]   |                 |
| Feel cue (italic, large) | Explanation (coach voice)        |                 |
| [Plate 3 Wall drill]          [Plate 4 90/90 from above]    |                 |
| Also checked: Loss of posture (possible), Over the top      |                 |
| Save to swing library                                       |                 |
+-------------------------------------------------------------+-----------------+
```

- **Principles:** prove it on the body, never in a stat tile. Leader-line style is data. Red appears only where the fault starts. Every number sits next to its threshold.

## Plan review: what changed from first instinct

- **First instinct:** Spectral serif headlines on a warm cream plate with an oxblood accent and hairline rules. That is the cream + serif + clay cliché, with the broadsheet hairlines on top. **Changed:** the ground moved to a greyer, cooler bone (`#E4E2DB`) and the chat went onto a cool slate. Headlines are now a heavy hyperlegible sans, and the serif is demoted to italic annotation only. Red is limited to anatomy, so CTAs are slate.
- **First instinct:** coloured confidence pills (green, amber, grey). That is a generic dashboard habit, and it would compete with the red joint. **Changed:** confidence is encoded in the atlas's own device, the leader line (solid, dashed, dotted), and the word is always spelled out.
- **First instinct:** 01 / 02 / 03 section numbers. **Changed:** letters A, B and C are used only for anatomical points in chain order, because the chat refers to them. Numerals appear only where there is a real sequence: the three "Film, upload, read" steps and the filming-guide steps that rejection reasons link to.
- **First instinct:** a single big figure with a stat callout in the hero. **Changed:** the hero is a full plate with margin labels and a cause route. The 7% is shown as a dimension on the body, not as a big number.
- **First instinct:** drawing the 90/90 exercise side-on like the drill. **Changed:** it is drawn from above, the same transverse view as the 31° hip dial, so the exercise visibly trains the same rotation the measurement found lacking.

## Self-critique notes

- Rendered every file in headless Chrome and fixed the following: overlapping header labels on the contact sheet, a "6°" label colliding with the skull, a rejection card that implied a confidence band, the gap in the chat thread, and text below 12 px inside scaled diagrams.
- The figure geometry is generated from one set of joints (`pose()`), so address, impact and drills stay anatomically consistent across all files.
- Known weak spot: the 90/90 top view is schematic, and some people may need its caption ("seen from above") to read it.
