# Shared brief: AIcoach design concepts (read fully before drawing)

You are one of 10 designers each producing ONE divergent design concept for AIcoach. Chris (the product owner) will compare all 10 side by side before choosing a direction, so your concept must be **unmistakably its own world**, fully committed, not a safe middle. Your assigned direction is in your prompt. Push it hard; breadth across the 10 is the point.

Source of truth for product facts: `D:\IBE160 Prog m KI\IBE160\AIcoach\G121-naalsund\docs\prd\prd.md` (sections 1–4 are enough). Skim it. Use its glossary terms verbatim in UI copy.

Design craft: read `C:\Users\chris\.claude\skills\impeccable\reference\craft-floor.md` (quality floor + absolute bans) and section 6 of `C:\Users\chris\.claude\skills\impeccable\reference\new-work.md` before drawing. Key points: the first viewport is a thesis, not a header; prove, don't claim (show the product working with authored demo data); author the assets (no generic icon tiles, no gradient/glass filler, no lorem ipsum); no fake testimonials, user counts or ratings — the product is pre-launch.

## The product in one paragraph

AIcoach is a web app that acts as a golf coach. A golfer (+2 to 15 handicap, practising at the range with a phone) films ONE swing **down the line** (from behind, along the target line), uploads it, and gets back what a good coach would say: **what the fault is, where it comes from (fault chain), how sure the app is (confidence band high/medium/low on every measurement), and what to practise — one drill and one mobility exercise.** Honesty is the edge: it refuses to guess on bad video ("Cannot analyse"), says "No verified fault found" instead of forcing one, and labels anything outside its rule table as "Unverified — confirm with a coach". The coach voice is plain language with a **feel cue** ("It may feel like you stay down, but at impact your hips have moved toward the ball").

NEW (from Chris, not in PRD yet): on the result page the player can **talk to the AI coach** (chat) about the result. The chat is grounded: it only answers from this analysis — it must not invent faults, numbers or drills. Show this honestly in the UI (e.g. a small note "Answers are based only on this analysis").

## Pages to sketch (all pages of the app)

Priority (full fidelity, desktop 1440 wide unless your direction says mobile-first):
1. **Landing page** (signed-out, marketing). Explain the promise, show the mechanism (a real-looking result), the honesty angle, how it works (film → upload → result), the 3 faults covered, a CTA to create account. Long scroll ok.
2. **Upload page** — upload one swing clip (mp4/mov, max 15 s), filming checklist essentials visible (DTL only, hand height, 2.4–3.7 m away, 120 fps recommended, whole body + club in frame, one swing per clip), opt-in "Save to my swing library" (default off, with consent text "stored on the AIcoach server until you delete it"). Also show the **analysing/progress state** (pose → swing events → measurements → rule table → explanation). The player is often on a phone at the range: also draw the mobile version.
3. **Result page** — the climax. Must contain: the verified fault, its measurement + confidence band, key frames (address and impact) with body lines drawn on a golfer figure, the fault chain (likely cause → mechanism → fault, each link with its evidence + confidence), the plain-language explanation with feel cue, ONE drill + ONE mobility exercise (mobility carries "Generic guidance, not medical advice — see a physiotherapist if you feel pain"), the "possible fault" if any, "Save to swing library", and the **AI coach chat**.

Secondary (lower fidelity is fine, all on one contact sheet): Sign in / Create account · Filming guide (phone) · Analysing (if not already shown) · Rejection "Cannot analyse" (UJ-2: reasons + links to filming guide steps) · "No verified fault found" + unverified observation (UJ-3, Nelly) · Swing library (UJ-6, list of saved clips with date + main finding) · Account page with delete analysis / delete account (UJ-4).

## Demo content (authored, synthetic — use it, extend it consistently)

- Player: **Rory**, 34, 11 handicap, 7-iron, filmed at 120 fps, 11 Nov 2026, range after work.
- Result: **Early extension — verified — confidence: high.** Measurement: hips moved toward the ball **by 7% of body height** from address to impact (threshold 4%).
- Fault chain: **Restricted hip rotation** (likely cause — not measurable directly; pointed to by: lead hip turned 31° at impact vs ~45° typical, confidence medium) → **Hips move toward the ball** (measured: 7% of body height, confidence high, key frames address + impact) → **Early extension** (verified, high).
- Feel cue: "It may feel like you stay down, but at impact your hips have moved toward the ball."
- Explanation (≤150 words, coach voice, no jargon). Write it.
- Drill: **Wall drill** — set up with your backside touching a wall (or golf bag); make slow half swings keeping your trail glute on the wall through impact. 3 × 10 reps.
- Mobility: **90/90 hip rotation** — 2 × 8 each side, slow.
- Possible fault: **Loss of posture — possible — confidence: medium** (posture angle changed 6°, potential threshold 5°, fault threshold 9°). No drill.
- Other fault checked: **Over the top — not found** (capped at medium confidence while measured from hand path).
- Chat sample: Rory: "Why does it feel like I'm staying down when I'm not?" — Coach answers grounded in the 7% and the impact frame, references the wall drill. Suggested prompts chips e.g. "How do I know the drill is working?", "What does 'likely cause' mean?", "Can I do this drill in a net?".
- Rejection sample (UJ-2): face-on view detected; feet out of frame; 30 fps. Each reason links to a filming guide step.
- No-fault sample (UJ-3): **Nelly**, 4 hcp: "No verified fault found" + unverified observation "Weight appears to move toward the trail side at the top — Unverified, confirm with a coach — confidence: low", no drill.
- Swing library: 4–6 saved clips with dates (Oct–Nov 2026) and main finding (e.g. "Early extension · high", "No verified fault found", "Cannot analyse").
- All demo data is synthetic; you may label the landing's example "Example result".

Language: UI copy in **English** (PRD terms). Brand name: **AIcoach**. Do not imitate any real golf brand, app, broadcaster or magazine (no logos, names, trade dress).

## Deliverables (write to your folder: `D:\IBE160 Prog m KI\IBE160\AIcoach\_bmad-output\planning-artifacts\ux-designs\ux-AIcoach-2026-11-11\.working\concepts\<NN-slug>\`)

1. `01-landing.svg` — width 1440, height as needed (≈2400–3600).
2. `02-upload.svg` — desktop upload page incl. or alongside the analysing state; width 1440.
3. `03-upload-mobile.svg` — phone frames (390×844 each) side by side: at least (a) choose clip + checklist, (b) analysing progress, optionally (c) result summary on phone. Canvas ≈ 1300×1000.
4. `04-result.svg` — full result page with chat, width 1440, height as needed (≈1800–2800).
5. `05-other-pages.svg` — contact sheet of the secondary pages (≈ 2400 wide), each frame labelled with the page name.
6. `concept.md` — name, one-line thesis, 4–6 sentence rationale (who it is for, why this world fits an honest coach), palette (hex + role), typography (Google Fonts families + roles), signature move(s), how the AI chat lives in this concept, risks/trade-offs (2–3 honest bullets).
7. `concept.json` — `{"id":"NN","slug":"...","name":"...","tagline":"...","fonts":["Family:wght@400;700", ...],"swatches":["#hex",...]}` (fonts must be Google Fonts family names in css2 syntax).

## Hard technical rules for the SVGs (they will be INLINED together in one gallery page)

- Valid standalone SVG 1.1 with `xmlns="http://www.w3.org/2000/svg"` and a `viewBox`; set `width`/`height` equal to the viewBox.
- **No `<style>` elements, no `class` attributes, no CSS.** Use presentation attributes only (`fill`, `stroke`, `font-family`, `font-size`, `font-weight`, `letter-spacing`, `opacity`, …).
- **Every `id` must be prefixed `c<NN>-`** (e.g. `c03-tracer-grad`) — ids from 50 SVGs share one document. Reference them as `url(#c03-...)`.
- `font-family` = your Google Font first, then a generic fallback, e.g. `font-family="Fraunces, Georgia, serif"`. Use straight quotes inside attributes carefully (escape `&` as `&amp;`, apostrophes fine inside double-quoted attributes).
- No external images, no `<image>` hrefs, no `<foreignObject>`, no scripts. Draw everything: golfer figures (silhouette, skeleton, line-art — your concept decides), key frames, pose lines, icons, textures.
- Text must be real, legible copy (min 12px at 1:1 on desktop frames). Wrap text manually with `<tspan x dy>`; check lines do not overflow their boxes.
- Keep each file under ~250 KB. Prefer reused `<symbol>`/`<use>` (prefixed ids) for repeated golfer figures.
- After writing, validate each file is well-formed XML: `python -c "import xml.dom.minidom,sys;[xml.dom.minidom.parse(f) for f in sys.argv[1:]];print('ok')" <files>` and grep that no `<style` or `class=` is present and all `id="` values start with your prefix. If you can render SVG → PNG with any available local tool (e.g. `python -c "import cairosvg"`, Inkscape, ImageMagick, a headless browser), look at the PNG with Read and fix overlaps/overflow; if none is available, carefully re-read coordinates for overflow instead.

## Return to the parent (short, ≤120 words)

Folder path, file list, concept name + one-line thesis, the signature move, anything you could not finish. Do NOT paste SVG content.
