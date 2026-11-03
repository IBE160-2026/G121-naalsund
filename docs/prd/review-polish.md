# Polish Review — AIcoach PRD (prd.md, addendum.md)

**Review:** bmad-review, lenses `structure` then `prose` (prose ran on top of the structure findings). Content class: docs.
**Reader:** humans (default). **Style guide:** Microsoft Writing Style Guide (default). Content is sacrosanct; findings address organization and expression only.

**Purpose read:** this document exists to help the course examiner and the downstream UX, architecture and epics/stories work understand exactly what the AIcoach MVP must do by 2026-12-15, and why.

**Structure model:** Strategic/Context (Pyramid). The PRD fits it well: purpose and vision lead, requirements are grouped by feature, metrics trace back to FRs. The addendum is a Reference/Database companion and is judged as such.

**Word counts (word_metrics.py):** prd.md 5,704 words; addendum.md 759 words.

## Findings

| # | Pass | Original Text | Revised Text | Changes |
|---|---|---|---|---|
| S1 | structure | §0, paragraph 2 (~75 words) mixes source documents and reading conventions | CONDENSE: split into one paragraph for sources and one for reading conventions | Easier to scan; no word change (~0) |
| S2 | structure | §1, paragraph 4: "Because feel and reality disagree, AIcoach tells…" | CONDENSE: drop the repeated reason (already stated in paragraph 1) and join with a colon | True redundancy within one section (saves ~5 words) |
| S3 | structure | §4.7 — no "**Functional Requirements:**" label before FR-16 | Add the label, matching every other feature | Consistent schema for random access (+2 words) |
| S4 | structure | §8.1 — numbered build/cut order followed by an unlabelled bullet list covering the same FRs | PRESERVE both (priority vs. inventory), but label the bullet list "**Included:**" | Reader otherwise cannot tell why the list repeats (+1 word) |
| S5 | structure | §12 Assumptions Index — entries out of document order (§4.6 before §4.4); first entry says "§4.1 FR-3" but the tag sits in §4.1 Out of Scope | MOVE entries into document order; relabel first entry "§4.1 Out of Scope" | Index must point to where the tag actually is (~0 words) |
| S6 | structure | §4.3 Description: "Realizes UJ-1, UJ-5." | "Realizes UJ-1, UJ-2, UJ-5." | FR-8 (in §4.3) realizes UJ-2; feature-level trace was incomplete |
| S7 | structure | §6.1 — first and last bullets have no bold label, unlike the others | Add "**Isolation:**" and "**Repository:**" labels | Consistent scanning (+2 words) |
| S8 | structure | §2.3 — UJ-1 uses the persona/entry/path/climax schema; UJ-2 to UJ-6 are prose paragraphs | QUESTION: not changed — filling the schema for UJ-2 to UJ-6 would add content | Inconsistent schema; author's call |
| S9 | structure | NFR-1 vs SM-8; §6.2 vs FR-11/§2.2; FR-13 Notes vs §6.1 | PRESERVE | Repetition serves traceability (requirement ↔ metric, guardrail summary) |
| S10 | structure | addendum §B table header: "Fault \| Potential \| Fault \| Note" — two columns named "Fault" | "Fault \| Potential threshold \| Fault threshold \| Note" | Ambiguous header; uses the Glossary's own terms (potential threshold, fault threshold) |
| S11 | structure | "test set" in §4.4 Description, FR-8, NFR-3, §8.1, OQ1, addendum §A — Glossary defines only "tuning set / evaluation set" | §4.4 "tuned on the test set" → "tuned on the tuning set" (FR-9 states this explicitly). QUESTION for the rest: "labelled test set" appears to mean the whole labelled set (tuning + evaluation); not changed | Glossary term drift; only the unambiguous case fixed |
| P1 | prose | "among the roughly dozen competing apps reviewed" | "among the roughly a dozen competing apps reviewed" | Missing article |
| P2 | prose | Glossary, Rule table: "…whether a verified fault is present, plus its cause, drill and mobility exercise." | "…plus each fault's cause, drill and mobility exercise." | Unclear antecedent of "its" |
| P3 | prose | FR-11 "The drill and exercise shown"; §4.5 "a drill or exercise"; SM-7 "exercises" | "mobility exercise(s)" | Glossary term verbatim |
| P4 | prose | Bare "clip"/"clips" in FR-6, FR-7, FR-8, NFR-1, SM-4, SM-6, SM-8, SM-C1, SM-C3 | "swing clip(s)" | Glossary term verbatim. User journeys, "bundled test clips", and text inside [ASSUMPTION]/[NOTE FOR PM] tags left as is |
| P5 | prose | FR-9: "reported as verified fault, possible fault, or absent" | "reported as a verified fault, a possible fault, or absent" | Missing articles |
| P6 | prose | FR-12 Notes: "decided by the player-author" | "decided by the author" | "player-author" used nowhere else; "the author" is the document's term |
| P7 | prose | FR-14: 'For a rejection or "no verified fault found"' | 'For a rejection or "No verified fault found"' | Match the quoted UI string used elsewhere |
| P8 | prose | §0: "Features (§4) nest globally numbered FRs." | "Each feature in §4 contains its FRs, which are numbered globally." | Compressed phrasing |
| P9 | prose | §2.2: "they are served later as a complement to their coach" | "they will be served later as a complement to their coach" | Tense: future phase |
| P10 | prose | §10: "who has five years of high-level golf and tournament play" | "who has five years of experience in high-level golf and tournament play" | Incomplete noun phrase |
| P11 | prose | addendum §A: "on own DTL clips" | "on the author's own DTL swing clips" | Missing determiner; Glossary term |
| P12 | prose | addendum §A: "YOLO-pose (AGPL-3.0 — source release or paid licence)" | "YOLO-pose (AGPL-3.0 — requires source release or a paid licence)" | Missing verb |
| P13 | prose | addendum §D: "hence the confidence cap below 120 fps." | "hence the confidence cap below 120 fps (FR-7)." | Cross-reference to the requirement it justifies |
| P14 | prose | addendum §E: "(none of ~a dozen apps)"; "but no app does in-product" | "(none of about a dozen apps reviewed)"; "but no app does so in-product" | Tilde reads as noise; missing "so" |
| P15 | prose | addendum §G: "Feedback still open from the brief: … GDPR (now covered …)" | "Feedback on the brief and where it is handled: …" | "Still open" contradicts "now covered" |

## Cross-reference check

All § references (§3, §4, §4.7, §6.1, §9, §12, addendum §A, §B), FR/NFR/SM references, UJ "Realizes" lines and Open Question numbers resolve correctly, except S5 (index label) and S6 (missing UJ-2), both fixed.

## Summary

- **Total recommendations:** 26 (structure 11, prose 15). Of these, S8 and the open part of S11 are QUESTIONs and S9 is a PRESERVE; none of those is applied.
- **Estimated reduction:** about +10 words net (≈0.2 % of 6,463). This was a polish pass, not a length cut; the document has no padding worth removing.
- **Length target:** none given.
- **Comprehension trade-offs:** none. No cut removes examples, journeys or summaries.
