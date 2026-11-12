# 12 Wayfinding Pictogram

**Thesis:** AIcoach treats your result like the signs in a good sports venue. Every concept has its own pictogram, every colour means exactly one thing, and every arrow takes you somewhere.

## Rationale
This is for the 2–15 handicap player standing at the range with a phone in one hand and a club in the other. They have about two seconds of attention and maybe glare on the screen. Wayfinding signage is built for exactly that: people moving, glancing, under stress, who need the right answer fast. Signage also fits an honest coach, because a sign system only works if its codes are strict. Slate always means "verified by the rule table" and yellow always means "possible or unverified", so the app cannot dress up a guess as a fact without breaking its own rules. The fault chain becomes a signposted route (likely cause, then mechanism, then fault) that runs straight into the green "what to practise" exit. The filming guide is a set of pictogram plates you can read at arm's length. "Cannot analyse" is a stop sign whose reasons point to the filming-guide step that fixes each one.

## Design plan (pass 1)
- **Colour, as sign enamel with strict meaning:** slate `#22313F` = verified; signal yellow `#F2C230` = possible / unverified / likely cause (not measured directly); green `#0B7A53` = your next move (drills, exercises, primary actions); blue `#1F5FAD` = information desk (AI coach, filming guide); red `#C8312A` = stop (cannot analyse, delete). Neutral structure: concourse grey `#E4E7E5` walls, white `#FFFFFF` sign blanks, metal `#8C979D` hanging rods.
- **Type:** Overpass (its letterforms come from US highway-sign lettering) at 700–800 for every sign face. Atkinson Hyperlegible for body text, chat and small print. It was drawn for low-vision legibility and has distinct 0/O and I/l/1.
- **Layout:** a modular sign system. Panels bolt together with 6 px gaps, each row is one fact, and the pictogram plate always sits at the left. Everything is left-aligned, as in directional signage. Station labels on route lines are centred under their stations, the only centred text.
- **Pictograms:** an original family on a 100-unit grid with 8-unit round strokes and a detached disc head. The golfer is always in down-the-line profile, which matches the camera view. The plate always inverts the panel colour.
- **Principles:** one meaning per colour; arrows only where they navigate; a pictogram for every concept; nothing shown without its confidence band.

```
LANDING                                  RESULT
[logo]   links ............ [Create]     [logo] ........ Upload  Library  Guide  (Rory)
                    ||          ||       < Swing library   Result: 7-iron   [o] Save
 Film one swing.  ==================      +--------------------------+  +-----------+
 Get directions,  | Example result   |    |[PICT] Verified fault     |  | (i) INFO  |
 not guesses.     |##[pict] Early ext|    |  EARLY EXTENSION  conf ■■■|  |   DESK    |
 body copy        |%%[pict] Posture  |    +--------------------------+  | grounded  |
 [Create][Guide]  |  [pict] OTT  n/f |    [Address frame][Impact frame] | chat ...  |
                  |>>[pict] Practise->|   [feel......][....real slate]  | chips     |
 (1)---->(2)---->(3)  how it works        What's happening (text)  [ask->]| [input >] |
 [frames][scale/feel]                     [yellow]->[slate]->[slate]    +-----------+
 [yel]->[slate]->[slate]->[green]                              |        | On this   |
 legend | stop / no fault / unverified     [green drill][green mobility]  | page   <- |
 3 faults ... [ green exit sign ---> ]    [yellow possible][white n/f]   +-----------+
```

## Plan review (what I changed from my first instinct, and why)
- **First instinct: airport black with yellow text, all caps.** That is the "near-black with one bright accent" default, it reads like a real airport's trade dress, and all-caps labels are a known tell. **Changed to** a light concourse-grey world with five colours that each carry one meaning, set in sentence case. Mixed case is also more legible at a glance, which is the reason signage exists.
- **First instinct: a Helvetica-style neutral grotesk.** That would fall back to the platform look. **Changed to** Overpass, a typeface with road-sign lineage, paired with Atkinson Hyperlegible for body text. The pairing is chosen for legibility rather than being the usual safe pick.
- **First instinct: the result as a grid of rounded cards with icons** (the SaaS kit). **Changed to** a hanging directory board of bolted-together sign rows. Each row is one finding, and its colour tells you its status before you read it.
- **First instinct: green for "good / no fault" and red for "fault".** That would turn the result into a pass/fail traffic light and moralise the swing. **Changed:** a verified fault is slate, which reads as a calm fact. Green is reserved for "your next move", so the route always ends at a green sign.
- **First instinct: a floating chat bubble in the corner.** **Changed to** a docked **Information desk** with its own pictogram (a person behind a counter). It is blue because blue means information everywhere in the system.
- **Cut:** a "you are here" dot on the hero and a progress percentage on the analysing screen. The analysing screen is a route line with stations instead, because it is a real sequence.

## Palette
| Hex | Role |
|---|---|
| `#E4E7E5` | Concourse wall: page background |
| `#FFFFFF` | Sign blank: neutral panels, inputs, "not found" / "no verified fault" signs |
| `#22313F` | Slate: **verified** (rule-table facts, measured mechanism) and all text and arrows |
| `#F2C230` | Signal yellow: **possible fault, unverified observation, likely cause** (not directly measured) |
| `#0B7A53` | Green: **your next move** (drill, mobility exercise, primary buttons) |
| `#1F5FAD` | Blue: **information desk** (AI coach chat, filming guide, help links) |
| `#C8312A` | Red: **stop** (cannot analyse, delete analysis or account) |
| `#55636E` | Secondary text (meta, captions) |
| `#8C979D` | Metal: hanging-sign rods only |
| `#8DA3AE` / `#5F7A5C` / `#3E4C44` | Key-frame scene (sky, turf, mat), flat and behind the figure |

## Typography
- **Overpass** 700/800: sign faces, headings, buttons, route station names, numbers on signs. Tracking is tightened slightly (-0.02 em) at display sizes.
- **Atkinson Hyperlegible** 400/700: body text, coach explanation, chat, consent and disclaimer text. The slashed zero helps make "0:06" and "120 fps" unambiguous.

## Signature moves
1. **Original pictogram family.** Golfer at address, at impact, hips moving forward (with the dashed address line), wall drill, 90/90 stretch, phone on tripod, DTL plan view, hand height, distance, whole body in frame, one swing per clip, face-on, feet out of frame, 30 vs 120 fps, cannot analyse, information desk, likely-cause/unverified "?" and more. All share one stroke and grid, and the plate always inverts the panel colour.
2. **Colour as law.** Slate means verified, yellow possible/unverified, green next move, blue information, red stop. The landing page prints this legend, and every screen obeys it, down to the swing-library chips.
3. **The fault chain as a signposted route** (yellow likely cause, then slate mechanism, then slate fault). A thick route arrow drops straight into the green practise signs.
4. **The split feel-cue sign.** "It may feel like you stay down," sits on a white blank and "but at impact your hips have moved toward the ball." on slate, so the perceived and the verified are literally two different sign colours.
5. **The analysing screen as a route line** with five stations (pose, swing events, measurements, rule table, explanation). Done, current and waiting stations look different.

## How the AI chat lives here
The chat is the **Information desk**, a docked blue-headed panel beside the result with a person-behind-a-counter pictogram. Directly under the header, a blue strip with a lock pictogram says: "Answers are based only on this analysis. No new faults, numbers or drills." Each coach answer ends with **Based on** tags that name the evidence it used ("Hips moved 7%", "Impact key frame", "Wall drill"). Suggested questions are outlined blue chips. The "What's happening" text has a blue pointer sign whose arrow aims at the desk. On mobile the desk becomes a blue bar at the bottom of the screen. On Nelly's no-fault result it offers to explain what "unverified" means.

## Risks / trade-offs
- **Pictograms need learning.** A plan-view "down the line" glyph or a 90/90 stretch is not instantly readable, so every pictogram ships with a text label. The system would need user testing at the range before any glyph is allowed to stand alone.
- **Key frames drawn as pictograms.** In this sketch the key frames are rendered in the pictogram language. The real product shows video stills with body lines drawn over them, which will look busier than the signs around them. The overlay style (white dashed address line, slate impact line, joint dots) is designed to carry over.
- **Strict colour codes constrain branding.** Green cannot become a "success" colour and red cannot mark a fault, so marketing and states have fewer options. Anyone extending the system has to respect the legend, or the honesty argument falls apart.
