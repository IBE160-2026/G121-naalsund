# r3-06 · Quiet Paper

**Idea:** The most minimal version of the family. One centred column of paper, with type and whitespace doing the work. The evidence stays hidden until Rory taps a pin, and then it opens in place.

## Text budget

The hard limit is **about 40 visible words per screen section**: a heading, at most two short sentences, and the confidence word. Three things fall outside the limit, and each is noted where it appears:
- copy that must be there (the mobility safety note and the swing-library consent line);
- an evidence panel after the player opens it;
- one coach chat answer, which gets its own budget of about 40 words.

## Layout rules

- Desktop uses one reading column, 640 px wide and centred. There are no side panels, chip bars, cards or rails.
- A section is separated from the next by whitespace (150–230 px) and a small uppercase label. Rules and outlines are not used for this.
- Only three kinds of border remain:
  - the dashed outline, which means inferred or unverified;
  - the phone bezel;
  - outline buttons.
- The landing page has 4 sections: thesis, one example result, "When it can't tell, it says so", and "Film. Send. Read." with the CTA.

## Taken from the sources

- **06:** the full palette, the wordmark geometry and the type roles. Newsreader is the coach (headlines, coach lines, the clay feel cue), Figtree is the UI, and IBM Plex Mono in teal is used only for measured values, each with a `[n]` pin. Also kept: dashed = inferred, the grounded chat note ("Answers are based only on this analysis") and the "Based on:" footnote.
- **09:** one idea per section, short copy, actions in thumb reach on the phone, and phone screens with one main thing each. "Also checked" is shown in full on the result page, so nothing is hidden behind a step.
- **02:** the pose model. The keypoint coordinates come from 02's address and impact plots. Here the figure is drawn in ink on paper, with soft paper-2 body capsules, a teal hip keypoint, a dashed address-hip line and a dashed address ghost pose. The impact frame shows the 7 % gap as a teal arrow. During analysis the same skeleton draws itself as each step finishes.

## Removed to stay simple

- 06's Evidence panel, left rail, "Jump to" chips, card frames, message bubbles for the coach and the step log detail.
- The chain cards became a three-node vertical line: a dashed node for the likely cause, a solid node for the measurement and a filled node for the verified fault.
- The suggested prompts became two plain text links.
- The key frames sit on paper and do not use the dark key-frame ground.

## Honesty kept

Every confidence band shows its word and its 3 bars. Every measured number is mono teal with a pin. Pins open the key frames, the value, the threshold and the band inline. The "possible" and "not found" checks stay visible. Nelly's unverified observation is the only dashed box on her page.

## Risks

- The page gets long. With this much whitespace, the result page runs to about 3,800 px, and a player who stops scrolling may never reach "Also checked" or the chat. A sticky "Ask the coach" link may be needed.
- Hidden evidence relies on people noticing the small `[1]` pins. If they never tap one, they see the verdict without the proof. The first pin may need to open by default on the first visit, as drawn here.
