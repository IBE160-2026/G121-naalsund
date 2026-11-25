# Round 3 brief: AIcoach merged direction (read fully before drawing)

Rounds 1–2 produced 15 divergent concepts. Chris (the product owner) has now chosen a direction. Round 3 = **10 variations inside ONE chosen design language**. These are not new worlds. Every round-3 design must look like it belongs to the same product family. The 10 differ in **composition, layout, information hierarchy and interaction pattern**, not in identity.

Base folder: `D:\IBE160 Prog m KI\IBE160\AIcoach\G121-naalsund\docs\_bmad-output\planning-artifacts\ux-designs\ux-AIcoach-2026-11-11\.working\`

## Chris's decisions (verbatim intent, translated)

1. **Main design = concept 06 "The Coach Talks"** (`concepts/06-conversation-first/`). Use it for the overall design: colours, logo/wordmark, typography, text sizes. He liked its **landing page** and its **03-upload-mobile**. Its **02-upload** also has a good, clean layout.
2. **From concept 09 "Cairn"** (`concepts/09-calm-mobile/`): the **simplicity**. Not crowded with text, tidy and clean. Its **upload mobile** was very good. Its **other pages** sheet was very clean and did not have too much information per page.
3. **Golfer figure = concept 02's pose model** (`concepts/02-lab-instrument/`): the golfer drawn as a skeleton with **keypoint dots and connecting lines** (see 02's 04-result key frames). Use that figure construction, restyled in the 06 palette (e.g. 06's key-frame ground `#36312B` with body lines `#8ED3E6`, or 06 ink lines on paper; your variation decides). Do not bring along 02's graph paper or its lab look. Bring only the figure.

## Study the sources first (required)

Read `concepts/06-conversation-first/concept.md`, `concepts/09-calm-mobile/concept.md` and `concepts/02-lab-instrument/concept.md`. Then **look at the actual drawings**: render these SVGs to PNG with headless Chrome or Edge (e.g. `"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --screenshot=out.png --window-size=1440,4000 file:///...svg`, or the Edge equivalent `msedge.exe`) and view the PNGs with Read:
- 06: `01-landing.svg`, `02-upload.svg`, `03-upload-mobile.svg`, `04-result.svg`
- 09: `03-upload-mobile.svg`, `05-other-pages.svg`, `04-result.svg`
- 02: `04-result.svg` (the skeleton figure only)
Reuse the 06 symbol/wordmark geometry and the 02 skeleton geometry from the SVG source where useful (copy and re-prefix ids).

## The fixed design language (all 10 must keep this)

- **Palette (06):** paper `#F4EFE6`, paper-2 `#EBE3D5`, card `#FFFCF6`, ink `#25201B`, ink-2 `#62584D`, clay `#A4462A` (coach colour, CTA), evidence teal `#1E5368`, evidence tint `#E2ECEC`. Confidence high `#2D6A4A`, medium `#8C5D0F`, low `#8E3F33`, always shown with the word. Key-frame ground `#36312B`, body lines `#8ED3E6`.
- **Type (06):** Newsreader for the coach's voice and headlines, Figtree for the UI, IBM Plex Mono **only** for measured values. Keep 06's text sizes.
- **06 rules kept:** the coach speaks in serif; measured numbers are mono teal with an evidence pin; dashed outline = inferred/unverified, solid = measured; the chat is grounded ("Answers are based only on this analysis").
- **09 simplicity rules:** one main thing per screen or section, generous whitespace, short copy (cut every sentence that does not help Rory act), progressive disclosure instead of showing everything at once, big touch targets on the phone. Each page must look clearly calmer and emptier than 06's result page. 06's result page was the most crowded part, so simplify it the most.
- No new colours, fonts or motifs beyond the above. No cairn stones from 09 (take the calm, not the motif). No 02 graph paper.

## Product facts and demo content

Same as rounds 1–2. Read `concept-brief.md` in the same `.working\` folder for product facts, the page list, demo data (Rory, Nelly, rejection, swing library) and the hard SVG rules. Everything there still applies, **except**: the id prefix is the one given in your prompt, and the folder is `.working\round3\<NN-slug>\`.

## Deliverables (same five SVGs + notes)

`01-landing.svg`, `02-upload.svg` (with analysing state), `03-upload-mobile.svg` (3–4 phones), `04-result.svg` (result + AI coach chat, desktop; add a phone strip if your variation is mobile-led), `05-other-pages.svg` (sign in, filming guide, rejection, no verified fault, swing library, account; 09-style one-idea-per-frame), `concept.md`, `concept.json`.

In concept.md: name, the one-line idea of your variation, what you took from 06 / 09 / 02 and how, what you deliberately removed to stay simple, risks (2 bullets). Keep it short. In concept.json, list the 06 fonts and palette (the gallery groups by them).

## Return (≤100 words)
Folder, files, variation name + one-line idea, anything unfinished. No SVG content.
