# 06 — The Coach Talks

**Thesis:** The whole app is one conversation per swing. The coach asks for the clip, watches it and answers in plain language. Every number it says is pinned to evidence you can check.

## Rationale

This is for Rory: an 11-handicap who has not had a lesson in three years. He wants to be *told* what is wrong, not handed a dashboard. A real lesson is a conversation. The coach asks you to hit one, watches, says what it saw and gives you one thing to work on. So that is the structure here: upload, analysis progress and result all arrive as messages in one thread. The honesty is in the typography. The coach speaks in a warm serif, and anything measured is set in mono and teal with a numbered pin. Every pin shows up in a sticky **Evidence** panel with its key frame, value and confidence band. A sentence without a pin is explanation, never measurement, and the reader can see that at a glance. Faults and drills stay easy to scan because the coach does not deliver them as prose. They arrive as structured cards inside the thread (verdict, fault chain, practice, other checks), and a "Jump to" chip bar at the top of the thread indexes them.

## Palette

| Hex | Role |
|---|---|
| `#F4EFE6` | Paper: page ground, the conversation surface |
| `#EBE3D5` | Paper 2: left rail, disabled composer, quiet bands |
| `#FFFCF6` | Card: verdict, chain and practice cards, inputs |
| `#25201B` | Ink: text, player bubbles, primary dark |
| `#62584D` | Ink 2: secondary text |
| `#A4462A` | Clay: the coach's colour (mark, name, feel-cue quotes, drill names, CTA) |
| `#1E5368` | Evidence teal: measured values, pins, grounding note |
| `#E2ECEC` | Evidence tint: pins referenced by the latest answer |
| `#2D6A4A` / `#8C5D0F` / `#8E3F33` | Confidence high / medium / low (always with the word and 3 bars) |
| `#36312B` + `#8ED3E6` | Key-frame ground + body lines drawn on the golfer |

## Typography

- **Newsreader** (400/500/600, italic): the coach's voice. Coach messages, headlines, the coach's name, the feel cue in italic.
- **Figtree** (400–700): interface, player messages, card titles, labels.
- **IBM Plex Mono** (500/600): measured evidence only (values, thresholds, swing-event times, step logs). It is used for measurement, not decoration.

## Signature moves

1. **Two voices, one rule.** The coach writes in serif. Every measured number is mono and teal with a superscript pin `[3]`, which matches a pin in the Evidence panel. The grounded chat answer ends with a "Based on: [3] hip movement · [2] impact frame" footnote.
2. **Persistent Evidence panel.** It stays beside the thread while you scroll: key frames 1–2, measurements 3–6 and clip checks. Pins the coach just cited are lit up. During analysis the pins fill in live. On the phone the panel becomes a pull-up **evidence tray**.
3. **Dashed means inferred.** The likely-cause link, the unverified observation and placeholders use dashed outlines. Anything measured gets a solid outline.
4. **Upload is a message.** The filming checklist is the coach's message, the composer turns into the drop zone, and progress streams in as a step log.

## How the AI chat lives here

The chat is the product, not a widget added to a result page. Each swing has its own conversation, and that conversation is scoped to that swing's analysis. Under the composer, a lock note says "Answers are based only on this analysis — no new faults, numbers or drills." Suggested-prompt chips sit above the input. The landing page shows the grounding with a refusal ("I didn't measure your grip in this clip, so I can't tell you"). Nelly's no-fault thread shows the coach declining to invent a drill.

## Risks / trade-offs

- Chat as the frame can feel slow to someone who only wants the verdict. The "Jump to" chips and the structured cards keep it scannable, but returning users may still want a compact summary view.
- The three-column desktop layout (rail, thread, evidence) is dense at 1280 px. On narrow laptops the evidence panel probably needs to collapse into a drawer.
- A coach persona with a voice risks implying a human coach or more authority than the rule table has. The pins, confidence bands and dashed "inferred" language carry that honesty, so copy has to stay disciplined.
