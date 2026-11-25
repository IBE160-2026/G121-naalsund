# PRD Quality Review — AIcoach (revision 2026-11-25)

- **PRD:** `docs/prd/prd.md` + `docs/prd/addendum.md`
- **Rubric:** `.claude/skills/bmad-prd/assets/prd-validation-checklist.md`
- **Reviewed:** 2026-11-25 (rubric walker; focus on the revision's changes and internal consistency)

## Overall verdict

The PRD is still a strong, honest document. Its thesis (honest, evidence-backed coaching from one DTL clip) carries through the new parts. FR-20 copies the grounding rules from FR-14, and the closed list for FR-13 removes the earlier "LLM decides what to say" risk. The revision did add some seams that don't hold up. The 2026-12-08 over-the-top/sway decision needs SM-1 evaluation-set results, but the schedule saves evaluation-set testing for the week after that date. §4.9 says the chat "sees" key frames, while §6.1 says the language model never receives them. Sway now has three roles (reserve fault, rule-table row, extra measurement), and they are not fully separated. The automatic swing library also leaves clip/analysis states that P1 cannot show. None of these is critical. Each one would cause a story-level argument downstream, so fix them before UX and architecture start using the revision.

## Decision-readiness — adequate

Most decisions are stated as decisions, and the PRD names what it gave up. The §4.9 note admits that the competitive research advised against chat and explains why chat came in anyway (line 353). §8.1 now gives the cut order with dates (lines 398–402), and the §10 `[NOTE FOR PM]` on the 3-of-4 sample is honest. Two decisions that look settled are not. The sway swap is dated, but its trigger cannot be measured by that date without breaking the PRD's own split between tuning set and evaluation set. The checkpoint dates have no consequence: nothing says what happens if P1 is not done by 2026-12-01. The library consent is a real product and GDPR decision, but the PRD presents it as settled without naming the trade-off of making it mandatory.

### Findings
- **high** Sway-swap decision date comes before the evaluation it depends on (§4.4 Notes line 244; §8.1 line 402; §10 line 441). Over the top is swapped for sway "if over the top fails SM-1 on the evaluation set", decided "before 2026-12-08". But evaluation-set testing is scheduled for 2026-12-08 to 2026-12-15, and SM-1 is "measured only on the evaluation set, which is never used to adjust thresholds". Deciding the swap requires running the evaluation set early. After the swap, sway's thresholds are tuned and the same evaluation set is used again, so the evaluation set no longer meets its "never used to adjust" promise. *Fix:* base the swap decision on a tuning-set proxy (e.g. "over the top detects < 3 of 4 tuning-set clips by 2026-12-05"), keep the evaluation set untouched until 2026-12-08, and say so in §4.4 Notes and the Assumptions Index.
- **medium** Checkpoint dates have no consequence (§8.1 lines 397–400). "Each tier starts only when the one above is done and tested" plus the dates P1 by 2026-12-01 and P2 by 2026-12-08 do not say what happens on a miss. Does FR-20 get dropped, shortened, or does it push into the evaluation week? *Fix:* add one rule, e.g. "If P1 is not done and tested by 2026-12-03, FR-20 is cut and SM-13 is reported as not delivered; the evaluation week is never used for building."
- **medium** Mandatory "consent" is presented as settled without its trade-off (§3 line 82; FR-1 line 122; §6.1 line 370). Making account creation depend on a consent bundles that consent with the service. Under GDPR this is weak consent (it is not freely given), and the only way to withdraw it is to delete the account. That may be acceptable for a course MVP running locally, but the document says it is "the first step of a real product" (line 12). *Fix:* either restate the basis as "storage is part of the service the player signs up for (contract)", with the tick box as information plus acknowledgement, or add a `[NOTE FOR PM]` that the legal basis must be reviewed before public hosting.

## Substance over theater — strong

There is no persona theater: one protagonist (Rory) plus Nelly and the examiner, and each drives FRs. The NFRs carry thresholds (NFR-1 median of 5 runs; NFR-7 licence rule backed by addendum §A). The differentiation claim is hedged as "desk research, not hands-on" (line 26), and addendum §E openly lists grounded chat as "no longer unique". The new chat section does not overclaim.

### Findings
- **low** Vision still says the MVP proves the claim "from one down-the-line phone video … detects three common faults". With the sway reserve and the two-fault fallback (line 244), "three" is a target, not a promise. *Fix:* keep it, but §1 could say "up to three" or point to §4.4 Notes.

## Strategic coherence — strong

The new features serve the thesis rather than diluting it. Chat is scoped to one analysis and must pass the same automated grounding check as the explanation. The unverified observation is now picked by rules, not by the language model, which fits "the language model explains; it never decides". SM-13 and SM-11 tie the new features to metrics, and the counter-metrics still guard the honesty thesis. The case for making the swing library P1 is argued, not asserted (line 398).

### Findings
- **low** UJ-1 now depends on a P2 feature (UJ-1 Resolution line 54). The core journey's resolution has Rory asking the coach. If FR-20 is cut under §8.1, the flagship UJ no longer matches the product. *Fix:* move the chat question to UJ-7 only (where it already is), or mark that sentence as P2.

## Done-ness clarity — adequate

Most FRs have sharp consequences. FR-13's selection rule ("furthest past its threshold", line 257), FR-19's two-option delete (line 326) and FR-20's refusal categories (line 349) are well specified. The gaps are where the new parts meet old wording or rely on a language model.

### Findings
- **medium** Chat/explanation checks don't say which mode they run in (SM-7 line 452; SM-13 line 458; FR-15 line 286; FR-20 line 351). In mock mode the chat gives "fixed sample answers", so the automated check passes by construction. Outside mock mode the model is undecided (OQ2). SM-13 does not say whether it must pass against a real model, how many runs, or what pass rate counts as a pass for a non-deterministic model. *Fix:* state that SM-7/SM-13 run against the real model chosen under OQ2, N times per question, and pass only if all runs (or ≥ X %) pass. Add that the mock-mode run only checks the wiring.
- **medium** The refusal decision is made by the language model, which goes against "it never decides" (§4.9 line 337; FR-20 line 349). Classifying a question as "not measured / other swings / pain / competitive round / off topic" is a decision. The PRD does not say whether the LLM or a rule-based gate makes it. Pain questions are safety-relevant (physiotherapist notice only). *Fix:* say that pain/injury and competitive-round questions are caught before the LLM call (e.g. keyword or classifier gate with a fixed reply), or accept LLM classification explicitly and add pain recall to SM-13.
- **low** "Main finding" is undefined (FR-19 line 322). The library row shows "main finding", but a result can hold several verified faults, only possible faults, only an unverified observation, or "No verified fault found". *Fix:* define the rule, e.g. "the verified fault with the highest confidence band; else 'No verified fault found'".
- **low** "Uses the FR-14 jargon blocklist" (FR-20 line 348) reads as the opposite of what is meant. *Fix:* "uses none of the terms on the FR-14 jargon blocklist".
- **low** The SM-13 question set (line 458) leaves out "use during a competitive round", a refusal category in FR-20 line 349. It also doesn't check the "Based on:" note or per-number citation (line 346, 348). *Fix:* add both to SM-13.

## Scope honesty — adequate

Non-goals are explicit and now include "not an open chat coach" (line 389). §8.2 names "chat across several swings" as next phase. The Assumptions Index matches the inline tags exactly (7/7, see Mechanical notes). Open-item density (7 OQs, 7 assumptions, 2 notes) is fine for a course MVP. The gaps are states the revision created without saying where they live.

### Findings
- **medium** Library/analysis deletion creates states P1 cannot show (§3 line 81; FR-3 line 138; FR-19 line 326; §4.7 line 290). The glossary says every swing clip in the library is "linked to its analysis". FR-3 deletes an analysis but keeps its clip, so a library row then has no analysis, and FR-19's row spec (main finding or "Cannot analyse") has no state for it. FR-19's "delete clip, keep analysis" keeps an analysis that P1 has no screen to reach, because only the stretch FR-16 lists analyses whose clip was deleted. If P3 is cut, the kept analysis can't be reached, yet it is still stored personal data. *Fix:* either define a row state "analysis deleted" in FR-19 and remove "keep analysis" until FR-16 ships, or move a minimal "analyses without clip" list into P1.
- **medium** Sway's dual role is not fully settled (§4.4 table line 208; FR-9 lines 216, 221; FR-13 line 260; OQ7 line 475). Sway is "defined in the rule table from the start". FR-9 says "each rule-table fault is reported as verified, possible or absent", which suggests sway would also show up as a possible fault. FR-13 then excludes measurements that are faults "in the *active* rule table", a term that is never defined. If the swap happens, the extra-measurement list is empty, so UJ-3 cannot happen and SM-3's "any observation labelled unverified" passes without testing anything. OQ7 names the question but gives no fallback. *Fix:* define "active rule table" in the glossary (the verified-fault rows in use; reserve rows are inactive and produce no possible fault). Add a default to OQ7, e.g. "if no replacement passes the tuning set, the unverified observation is disabled and UJ-3 is reported as not shown".
- **low** UJ-3 example rests on a domain claim. A reverse pivot is usually described by weight or upper-body movement toward the target in the backswing. UJ-3 shows the sway observation ("hips move away from the target") as the visible symptom. That can be true but isn't typical, and the author should confirm it, because UJ-3 is the reference case for SM-3. *Fix:* check with the author, or pick a non-covered fault whose DTL symptom clearly matches sway.

## Downstream usability — adequate

IDs are contiguous and unique (FR-1–20, UJ-1–7, SM-1–13, SM-C1–C3, NFR-1–7, OQ1–7), and the glossary is broad. Most new terms (library consent, extra measurement, coach chat) are used verbatim. One real contradiction and some term drift would trip up architecture and story extraction.

### Findings
- **medium** Key frames given to the language model: §4.9 and §6.1 contradict each other (§4.9 line 337; §6.1 line 372; UJ-7 line 73; FR-20 line 346). §4.9 says the chat "sees … key frames", and UJ-1/UJ-7 have the coach "citing the impact frame". §6.1 says the explanation, observation and chat receive analysis data only, "never swing clips, key frames, email or other personal data". Architecture will read these differently (send images to a vision model, or not). *Fix:* in §4.9 replace "key frames" with "key-frame references (swing event and frame number)" and say that the images are never sent.
- **low** SM ↔ FR coverage gaps. No success metric validates FR-3 (delete analysis and account; SM-11 covers only clip deletion via FR-19), FR-4/FR-5, or FR-16. FR-3 matters for GDPR. *Fix:* extend SM-9 or SM-11: "after account deletion, no analysis, key frame, chat or clip of that player exists in storage, and sign-in fails".
- **low** UJ ↔ FR back-links: §4.9 description says "Realizes UJ-1, UJ-7" but FR-20 says "Realizes UJ-7" only (lines 337, 342). FR-3 (UJ-4) is not linked from UJ-6, even though UJ-6 deletes an analysis via FR-19. *Fix:* align the two.

## Shape fit — strong

The PRD is a consumer product with a single protagonist, and the UJs carry real load. UJ-1 is fully structured, the others are compact narratives, and UJ-5 covers the examiner audience. The addendum keeps implementation detail out of the requirements. The level of formality suits a solo course project that feeds UX, architecture and stories.

## Mechanical notes

- **Frontmatter not updated:** `updated: 2026-11-03` (line 5), but the body records a 2026-11-25 revision (line 16).
- **Assumptions Index roundtrip:** all 7 inline tags (lines 142, 178, 244, 263, 277, 348, 369) appear in §12 (lines 479–485) and vice versa. Some plausibly unconfirmed values are untagged: the 50-clip limit (line 331), the 15-second limit (line 158), and the checkpoint dates (lines 398–399). Tag them if they were not user-confirmed.
- **Glossary drift:**
  - "rule threshold(s)" (lines 183, 219) vs glossary "potential threshold / fault threshold".
  - "active rule table" (line 260) is undefined.
  - "reported fault" (lines 99, 218) is not in the glossary.
  - "clean swing clips" (SM-2, line 445) is undefined.
  - "fixed library" for drills (lines 103, 104, 231) collides with the glossary term "swing library". Use "drill library".
  - "the coach" (lines 54, 73, 337) for the coach chat. Acceptable as voice, but not glossary-verbatim.
  - "history" in FR-1 line 126 ("Upload, results and history") refers to the stretch analysis history. Use "swing library".
- **FR-1 stored-data list** (line 123: clips, results, key frames, chat) leaves out "measurements", which §6.1 Retention lists (line 369).
- **FR-18 last consequence** (line 319) can't fail, because no account exists without consent (FR-1). Harmless, but it could be phrased as a storage-layer invariant.
- **Addendum §B sway row** gives potential and fault thresholds, but the PRD does not say which one the extra measurement uses as "its threshold" (FR-13).
- **Addendum §G** calls the course-feedback item "consent"; check it against the legal-basis note above.
- **Required sections present:** Vision, Users/JTBD, UJs, Glossary, Features/FRs, NFRs, Constraints, Non-Goals, Scope, Next Phase, SMs with counter-metrics, OQs, Assumptions Index.
