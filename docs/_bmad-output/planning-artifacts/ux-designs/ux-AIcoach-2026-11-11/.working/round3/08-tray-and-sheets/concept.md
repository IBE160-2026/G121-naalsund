# 08 · Tray and Sheets

**Idea:** The coach thread is the base layer. Everything else (evidence, practice, the chat) slides up over it as a bottom sheet with fixed heights, so one thing is in front at a time and Rory always gets back the same way: drag down.

## Sheet states (phone, 390 × 844)

| Height | px | Used by |
|---|---|---|
| Peek | 132 | One dock: the Evidence tray row (pin count and thumbnails) above the composer field. Always present on a result. |
| Half | 460 | Clip sheet (upload), Evidence tray after a pin tap (key frames and that one value), Practice sheet (Wall drill), filming-guide step, every confirmation. |
| Full | 780 | Evidence tray with all six pins, Practice sheet on the Mobility tab, Ask sheet (grounded chat). |

The Practice sheet has no peek: you open it, you don't browse it. The Ask sheet skips half because a conversation needs the room. On desktop the tray and the practice sheet become one right-side **drawer** (tabs Evidence · Practise) that is closed by default and pushes the thread left without covering it. The composer stays docked in the thread there.

## What I took

- **From 06:** the full palette, Newsreader/Figtree/IBM Plex Mono and their text sizes, the wordmark and flag mark, the serif coach voice, mono teal values with numbered pins, dashed outlines for inferred links, the grounded-chat lock note, the "upload is a message" idea (the composer becomes the clip chooser or drop zone), and the evidence tray from 06's phone version, promoted here to the main interaction.
- **From 09:** the calm upload flow (film one swing → ready when you are → analysing → answer ready), one idea per screen, actions in the bottom third, short copy, and confirmations as sheets.
- **From 02:** the pose model. Address and impact are skeletons with keypoint dots and connecting lines (02's geometry, re-projected), drawn as `#8ED3E6` lines on the `#36312B` key-frame ground. The hip keypoint is ringed, the address hip is a dashed line, and the impact frame carries a dashed address ghost and a +7% arrow. The Wall drill reuses the same skeleton in ink on paper, with the hip in clay against the wall.

## What I removed to stay simple

- The left conversation rail, the "Jump to" chip bar and the always-open Evidence column from 06's result page.
- The full explanation (only two sentences show; the rest is behind "Read the full explanation"), the possible fault and the not-found fault (collapsed into one "Also checked" row), and the clip checks (one line inside the tray).
- Repeated numbers. 7% appears once in the thread and once in the tray, not on every card.

## Risks

- Sheets hide things. A player who never drags the tray up never sees the key frames, so the peek row has to keep showing the thumbnails and the pin count.
- Two layers at peek (tray row above the composer) is a dense 132 px. It needs real-device testing for mis-taps, and the gesture rules (drag versus tap) must stay identical on every sheet.
