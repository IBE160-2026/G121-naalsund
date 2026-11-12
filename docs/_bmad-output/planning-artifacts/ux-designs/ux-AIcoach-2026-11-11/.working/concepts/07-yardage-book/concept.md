# 07 · Yardage Book

**Thesis:** every fault has a route. AIcoach surveys one swing the way a yardage book surveys a hole, and draws the route from likely cause to fault, marking what it measured, what it only infers and what it could not see.

## Rationale
This is for the 2 to 15 handicap who already carries a yardage book or a rangefinder and trusts numbers they can check against the ground. A survey map is the most honest picture we have: it separates measured from inferred, it has a legend, and it leaves blank what nobody surveyed. That maps straight onto the product's edge. Confidence bands use map-line conventions (solid, dashed, dotted), "Cannot analyse" is an unsurveyed plot, and "No verified fault found" is a map with no route drawn. The user journey is played as a hole: tee (film), fairway (upload), green (result), next tee (practise). This journey strip runs at the top of every signed-in page. The look is outdoorsy and crafted but precise, so it reads like a tool a golfer can trust rather than a gamified app.

## Palette
| Hex | Role |
|---|---|
| `#F2ECDF` | Paper: page background, the yardage-book page |
| `#E9E1CE` | Panel paper: side panels, feel-cue box, action box |
| `#22291F` | Survey ink: text, route lines, primary buttons, caption strips |
| `#4D5343` | Secondary ink: meta text, captions (5.9:1 on paper) |
| `#5B7849` | Fairway: tee boxes, completed steps, check marks |
| `#CCD6B2` | Light fairway: fairway fill, key-frame ground |
| `#A9BF88` | Putting green: green, fault waypoint (3) |
| `#DCC797` | Sand: bunkers, the "possible" zone on rulers |
| `#A27F56` | Contour brown: contour lines, hatching on figures |
| `#B23A2B` | Cartographic red: annotations only (body lines, thresholds, swing arc, "Verified" stamp, leaders, current step, destructive actions) |
| `#6E8E9E` | Water: notebook ruling in Caddie notes |

## Typography
- **Saira Condensed** (500–800): display headlines, labels, map legends, numbers, buttons. It is condensed and technical, like the lettering on a survey sheet.
- **Source Serif 4** (400, 600, italic): body copy, coach explanation, feel cue (italic), chat answers. It is the human coach voice next to the surveyor's labels.

## Signature moves
1. **Contour hero generated from a swing arc.** The landing hero is a marching-squares contour field computed from the distance to a down-the-line club path. The red arc carries survey triangles at takeaway, top, address/impact and finish, with a map legend and scale bar.
2. **Fault chain as a route on a hole map.** Waypoint 1 (likely cause, tee), 2 (mechanism, landing area) and 3 (fault, pin) each have an evidence callout on a red leader. The cause leg is **dashed** (medium, inferred). The measured leg is **solid** (high). Yardage plates on the route show 31° and 7%.
3. **Map-legend confidence.** Solid, dashed and dotted lines mean high, medium and low everywhere: tags, routes, borders (a possible fault has a dashed frame, an unverified observation a dotted one) and the analysing progress route.
4. **Neatline sheet frame** with graticule letters and numbers around every page, so each screen is a map sheet.

## How the AI chat lives here
The chat is **Caddie notes**: a ruled notebook page with a binding margin, docked beside the result on desktop and a dark bar at the bottom of the phone result. A boxed note in its header says "Answers are based only on this analysis." Answers are tied to the evidence: each one ends with reference tags ("Impact key frame", "Waypoint 2 · 7%", "Wall drill") that point back to parts of the page. The sample also shows a refusal: asked for clubhead speed, the caddie says the analysis does not measure it and will not guess. Suggested prompts sit at the bottom as "Ask next" chips.

## Risks / trade-offs
- The map metaphor needs a legend, and some users won't read one. Dashed for medium is learned, not obvious, so the confidence words must always sit next to the line (they do in this concept). Line style alone is never enough.
- Contours, hatching and stipple are dense. On a phone in sunlight at the range they can turn into noise, so the mobile screens deliberately drop texture and keep only the journey strip and line conventions.
- The landing scroll is long (~4000 px). The Rule table and Honesty sections could be merged if the page needs to be shorter.
