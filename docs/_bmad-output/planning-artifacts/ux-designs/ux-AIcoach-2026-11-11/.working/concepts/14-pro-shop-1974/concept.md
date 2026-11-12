# 14 · Pro Shop 1974

**Thesis:** Your swing comes back as the pro's lesson card. It's warm and a bit old-fashioned, and it never bluffs.

## Rationale

This is for the 11-handicapper who has not had a lesson in three years. He remembers the club pro's shop: a pennant wall, a counter, and a pro who wrote one thing on a card and sent you back to the mat. AIcoach keeps that ritual. The result is a printed **lesson card** with a sweater-stripe band across the top, and the drill and mobility exercise are illustrated lesson tiles like the ones in a 1970s instruction book. The warmth is there on purpose. A coach that often says "Cannot analyse", "No verified fault found" or "Unverified — confirm with a coach" needs a friendly voice, so that saying no feels like care and not like an error. The 1970s styling stays on the surface. Every honest element is drawn plainly and labelled in words: confidence bands, thresholds on a yardstick ruler, and evidence for each link of the chain.

## Palette

| Hex | Name | Role |
|---|---|---|
| `#3A2214` | Chocolate | Ink, corduroy nav, chat panel, primary buttons (mustard text), fault stripe |
| `#E0A526` | Mustard | Hero ground, rulers, CTA on dark, likely-cause stripe, done states |
| `#C4551B` | Burnt orange | Mechanism stripe, sweater stripes, cap. Used only for shapes and large text |
| `#A3410F` | Rust | Small accent text: links, thresholds, link-role labels (5.4:1 on card stock) |
| `#66702A` | Avocado felt | Felt panels (drop zone, drill tile, honesty band), Verified badge |
| `#F4ECD6` | Card stock | Only the lesson card and slips. Never used as the page background |
| `#DCD6B2` | Putty | App page background (felt-dot texture) |
| `#CFCB9C` | Sage | Background of key-frame stills |

## Typography

- **Caprasimo** (Google Fonts, 400): a fat soft serif with 1970s swagger. Used for headlines, fault names, the feel-cue quote and the "Ask the pro" title.
- **Libre Franklin** (400–800, italic 400/500): a plain American grotesque. Used for all body text, labels, measurements and chat text. Labels are in sentence case and never tracked caps.

## Signature moves

1. **The stripes carry the fault chain.** On the result page, a band of three sweater stripes (chocolate, orange, mustard) comes in from the edge of the card. Each stripe peels down in a rounded 70s bend into its own link card: mustard into the likely cause, orange into the mechanism, chocolate into the fault. The same three stripes are the brand band elsewhere, and on the analysing screen they act as the progress track.
2. **The flat 1970s instruction-book golfer.** He wears a mustard sweater with stripes, a flat cap and saddle shoes. He is drawn down the line, with body lines (white core, chocolate edge) and a dashed rust "address line" that shows how far the hips moved by impact.
3. **Honest instruments in period dress.** A wooden yardstick ruler marks the threshold and the measured value (7% against 4%). The confidence badge is a three-notch meter plus the word. Colour never carries the meaning alone. The pennant wall in the landing page's "pro shop" lists the three faults and how confident each can be. Over the top hangs there as "Capped at medium confidence".

## How the AI chat lives here

The chat is **"Ask the pro"**, a chocolate corduroy panel that stays beside the lesson card on desktop and becomes a floating "Ask the pro about this lesson" bar on the phone. Under the header it always says "Answers are based only on this analysis." Every answer from the pro carries mustard chips labelled **"From this analysis:"** (Impact key frame, 7% measurement, Wall drill), so the player can see what grounds each reply. The sample also shows a refusal: "Should I change my grip?" gets "I can't tell you that. This analysis didn't measure your grip, so I won't guess." The voice is a plain, warm club pro, not a chatbot.

## Risks and trade-offs

- **Nostalgia can read as costume.** Push it further, for example with an ochre wash on everything, and it turns into a theme-restaurant menu. It only holds if the stripes stay meaningful and the reading surfaces stay calm.
- **Caprasimo is greedy.** It is wide and heavy, so long fault names wrap early on the phone. It needs strict size limits and a rule that it is never used for body text or small labels.
- **Orange has weak contrast.** Burnt orange fails for small text on light grounds, so the system needs a separate rust for text. A developer could easily mix the two up.

## Design plan (pass 1)

- **Colour:** chocolate `#3A2214`, mustard `#E0A526`, burnt orange `#C4551B`, avocado `#66702A`, card stock `#F4ECD6`, putty `#DCD6B2`.
- **Type:** Caprasimo for display, Libre Franklin for text.
- **Layout:** Left-aligned throughout. Sections alternate grounds like the walls of a shop: mustard corduroy for the hero, chocolate corduroy for the pennant wall, putty felt for the steps, avocado felt for honesty. The result page is one long lesson card (880 wide) with "Ask the pro" pinned in a 400-wide column beside it.

```
LANDING                                   RESULT
[corduroy nav ...........................] [corduroy nav ...........................]
[Film one swing.     |  /lesson card\   ] [ LESSON CARD ==stripes==  | ASK THE PRO ]
[Get the lesson      |  | key frames |  ] [ Early extension  [V][hi] | Answers are..]
[card back.  [CTA]   |  | ruler 7%   |  ] [ [address]  [impact]      | Rory: why..  ]
[==== mustard / orange / choc band =====] [ ruler ----4%-----7%----  | Pro: ... 6°  ]
[ pennant wall: 3 faults hanging        ] [ ~~~ feel cue (mustard) ~~ | [chips]      ]
[ 1 ===== 2 ===== 3  how a lesson works ] [ What the pro says        | [input]      ]
[ honesty: slip | Nelly | conf legend   ] [ ==stripes peel into==    |              ]
[ ask the pro: copy | chat              ] [ [cause] > [mech] > [fault]              ]
[ close: Bring one swing to the counter ] [ [drill tile] [mobility tile]            ]
                                          [ also checked / save / delete            ]
```

- **Principles:** stripes carry meaning, not just decoration. Card stock appears only where something is "printed". Confidence is always written in words. One instruction-book illustrator draws every figure.

## Plan review: what I changed from my first instinct

- **I dropped the cream page with a terracotta accent.** My first instinct was a cream page with Cooper-style type and an orange accent, which is exactly cliché #1. Mustard corduroy and putty felt now carry the page. Card stock is kept for the lesson card itself, and orange is never the only accent.
- **Confidence is a notch meter, not a traffic light.** Green, yellow and red would have competed with the stripe colours that encode the chain, and would have relied on colour alone. Confidence is now a one-ink, three-notch meter plus the word.
- **No vintage-manual tracked caps.** Period instruction books lean on tracked uppercase labels, which is also cliché #5. All labels are sentence-case Libre Franklin bold.
- **The stripes were going to be pure decoration.** I first drew them as the hero's racing stripes. I moved their meaning into the product: they show the order of the fault chain on the result page and the progress on the analysing screen. On the landing page they stay as one band between sections.
- **I avoided equal slanted bars.** Three equal slanted stripes come too close to a famous sportswear trade dress. These stripes are horizontal, unequal in colour and bent in curves, and the logo is a pennant badge.
