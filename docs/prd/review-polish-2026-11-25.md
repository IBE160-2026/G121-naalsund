# PRD polish log — 2026-11-25

BMad PRD Finalize step 5. Lenses from bmad-review: `structure`, then `prose`. Order: prd.md, then addendum.md. Polish only: no change to meaning, IDs, numbers, dates, thresholds, tags or glossary wording. Frontmatter left alone.

## Structure (prd.md)

| # | Finding | Fix |
|---|---|---|
| S1 | §3 Glossary: "Possible fault" was defined after "Unverified observation" and "Fault chain", but "Potential threshold / fault threshold" already uses the term. | MOVE: entry placed directly after "Verified fault". Wording unchanged. |
| S2 | §4.1 Description lists UJ-1 and UJ-4, but FR-1 in the same feature realizes UJ-6 (library consent). | Added UJ-6 to the §4.1 "Realizes" line. |
| S3 | FR-20 listed only UJ-7, while UJ-1's resolution uses the coach chat and the §4.9 Description lists UJ-1, UJ-7. | FR-20 now "Realizes UJ-1, UJ-7". |
| S4 | FR-9 pointed to "the Notes below". The Notes sit after FR-12, so the pointer was vague. | Changed to "the §4.4 Notes". |
| S5 | §6.1, §6.2, §6.3 and §8.2 headings had no blank line before their lists, unlike the rest of the document. | Added the blank lines. |

## Structure (addendum.md)

| # | Finding | Fix |
|---|---|---|
| S6 | §B sway row cited the patent as "US12608853", while the section intro gives the full number "US12608853B1". | Changed to "(same patent)". |
| S7 | §G said §6.1 covers "consent". After the revision, §6.1 names the legal basis as contract and has a "Legal basis and notice" bullet. | Listed the topics as "retention, legal basis and notice, language-model data, deletion". |

## Prose (prd.md)

| # | Finding | Fix |
|---|---|---|
| P1 | §1: "among the roughly a dozen competing apps" read awkwardly. | Changed to "among roughly a dozen competing apps". |
| P2 | FR-20: "uses the FR-14 jargon blocklist" was ambiguous and could be read as "uses the jargon". | Changed to "uses none of the terms on the FR-14 jargon blocklist", which matches FR-14's wording. |
| P3 | §8.1: "If the chat ... the composer is hidden". "Composer" is a UX term that the PRD does not define, and "chat" was shortened from the glossary term. | Changed to "If the coach chat ... its question box is hidden". |
| P4 | §8.1: "every clip is now kept". "Now" was left over from the revision. | Removed "now". |
| P5 | FR-19: "The row still counts as a swing library entry for listing, but not toward the 50-clip limit" was wordy. | Changed to "The row is still listed in the swing library but does not count toward the 50-clip limit." |

## Prose (addendum.md)

| # | Finding | Fix |
|---|---|---|
| P6 | §B sway row: "Trail ankle-to-trail hip line angle" did not match the PRD §4.4 term. | Changed to "Trail ankle-to-hip line angle". |
| P7 | §B over-the-top row: "uses hand-path proxy" was missing an article. | Changed to "uses a hand-path proxy". |

## Kept on purpose (PRESERVE)

- Some statements appear in more than one place. They reinforce each other rather than repeat needlessly, so they stay:
  - the §4.9 Notes and the §6.1 "Language model" bullet;
  - the mock-mode chat rule in FR-15 and FR-20;
  - the "Library consent" glossary entry and the §6.1 "Legal basis and notice" bullet.

## Not fixed (would change meaning)

- FR-1: "Upload, results and history are reachable only when signed in" does not mention the swing library or the coach chat. Adding them would add a requirement.
- "Active rule table" (§4.4 Notes, FR-13) is a term that is defined inline and is missing from the §3 Glossary. Adding a glossary entry is a content decision for the PM.
- FR-7 uses "rule threshold", and §3 defines "potential/fault threshold". Which of the two FR-7 means is a content question.
