# Candidate retention addendum — audit M2 — 2026-11-06

Rules read at `e5b64450fce42262dafc88ee357b72e5f203916b`. Codex development response. These are retrospective records of already assigned or considered routes, not preregistrations. They preserve T1–T6 dispositions at the end of that batch. Handoff 04 may resume them under distinct T7/T8 records. No novelty is asserted and no unexecuted test is reported as executed.

## IDEA?padua-3d-codex-T2-a — unshifted LC alias-equivalence

Aliases: handoff 01 T2(a); Dencker–Erb spectral-index comparison; P3′.

- Question / scope: can the unshifted all-parities-equal Dencker–Erb nodes interpolate the complete total-degree simplex with exactly N=binom(n+3,3) nodes, n≥2?
- Mechanism and hypotheses: cosine images of indices i_j modulo 2m_j with all i_j of equal parity, with positive integer axis parameters m_j. This is the unshifted LC class described in literature-T1.md, not every rank-one Chebyshev lattice.
- Closest registry entries (read): IDEA-013/029/120/185; PD-T?padua-3d-codex-T1-01 and PD-N?padua-3d-codex-T1-01; LIT-014/319 (Dencker–Erb §2.1, (2.1)–(2.11)).
- Separation criterion / falsifier: LC spectral-space interpolation would answer this target only if its space is the complete Π_n and its node count is N. A rank deficiency at exact cardinality erases that possibility.
- Literature baseline and limitations: existing bounded primary reading in literature-T1.md; no new fulltext retrieval, no claim about unread LC theorems.
- Applicable obstruction: the parity condition is closed under addition in product_j Z/(2m_j). Negating any coordinate preserves every parity, so H and a=0+H are invariant under each R_j. Their cosine image is exactly the LC grid (fold i_j to 0..m_j). The accepted T1 obstruction therefore applies whenever |X|=N and n≥2. This checks class membership directly; pairwise coprimality is unnecessary for that implication.
- Novelty gate verdict: duplicate application of the accepted local obstruction; no new construction.
- Cheapest decisive test / kill criterion: verify the subgroup/reflection membership above, then apply T1. A non-member would invalidate this application and require a separate record.
- Test discriminability: this implication excludes exact-cardinality total-degree interpolation, while leaving LC interpolation in its own spectral space intact.
- Actual results and evidence: class-membership argument above; no separate spectral-index computation was launched.
- Disposition: subsumed for the specified unshifted parity LC class by PD-N?padua-3d-codex-T1-01. The broader rank-one lattice part of handoff T2(a) is deferred to T8, not excluded.
- Disposition reason / resume condition: equivalent obstruction application; resume outside this class only with an explicit lattice/phase whose whole torus set fails some R_j invariance, and a frozen dictionary/cardinality test.
- Canonical theory: theory/t1-reflection-classification.md; theory/t1-minimal-obstruction.md.
- Topic / audit / history: handoffs 01 and 04; audit-01 M2(a); retained 2026-11-06.

## IDEA?padua-3d-codex-T2-phase — translated cyclic orbits

Aliases: phase-shifted rank-one orbit; translated generating curve.

- Question / scope: escape the unshifted odd-modulus failures with an explicit phase a_n.
- Mechanism and hypotheses: X_n=cos(a_n+H_n), with exactly N nodes and a degree-uniform generator/phase rule fixed before testing.
- Closest registry entries (read): IDEA-013/029/178/185/187; T2-01; PD-N?padua-3d-codex-T2-02 and T3-02.
- Separation criterion / falsifier: the new phase must destroy the displayed unshifted null polynomial; if that polynomial still vanishes on every new node, the distinction fails.
- Literature baseline / limitations: known translated lattice mechanism; no new source result or novelty claim.
- Applicable obstructions and hypotheses broken: the M39 result assumes zero phase. Translation escapes that assumption, but does not establish cardinality or full rank.
- Novelty gate verdict: variant with the explicit phase as the proposed difference.
- Cheapest decisive test / kill criterion: exact node count and evaluation of inherited nulls; kill a fixed rule on its first certified deficiency under D2.
- Test discriminability: detects persistence of an obstruction, not quality or an all-degree success.
- Actual tests and evidence: none in T1–T6.
- Disposition / reason / resume condition: deferred, not launched; no frozen phase rule existed. Resume under T8 with a degree-uniform phase/generator prescription, exact fold cardinality and preregistration before any run.
- Canonical theory: no new result; theory/t2-normalized-screen.md gives the boundary of the existing obstruction.
- Topic / audit / history: attempts/T2.md; audit-01 M2(d); 2026-11-06.

## IDEA?padua-3d-codex-T2-omit-n3 — degree sequences omitting n=3

Aliases: even-degree subsequence; odd n≥5; skipped cubic degree.

- Question / scope: structured total-degree families on a prescribed degree sequence that omits n=3.
- Mechanism and hypotheses: a fixed rule for both the allowed degree sequence and generators, not interpolation of formulas through finite successful cases.
- Closest registry entries (read): T2-01; IDEA-013/029/185/187; normalized and full-M39 obstructions.
- Separation criterion / falsifier: a sequence omitting n=3 escapes the cubic obstruction's quantifier; it must still pass at every included degree. One included certified deficiency kills that rule.
- Literature baseline / limitations: established cyclic dictionary; no novelty inferred from changing a sequence.
- Applicable obstructions: quadratic K/T/O failures persist for those formulas. Omitting n=3 alone resolves neither n=4 quality nor any higher degree.
- Novelty gate verdict: variant, no priority claim.
- Cheapest decisive test / kill criterion: freeze a sequence and formula, then exact rank at its first untested degree and D2 comparisons where applicable.
- Test discriminability: finite success remains finite evidence and does not prove an asymptotic bound.
- Actual tests and evidence: no subsequence family run; n=2,4 survivors are the existing finite screen only.
- Disposition / reason / resume condition: deferred because no separated uniform rule was supplied; resume under T8 with such a rule and a reason for removing the n=4 quality deficit. Includes even degrees and odd n≥5.
- Canonical theory: theory/t2-normalized-screen.md; theory/t2-finite-survivors.md.
- Topic / audit / history: attempts/T2.md; audit-01 M2(d), m4; 2026-11-06.

## IDEA?padua-3d-codex-T2-02 — explicit correction / coset union

Aliases: handoff T2(b) DMVX thinning; two/three cosets; second-character mask; boundary replacement.

- Question / scope: leave a failed single-orbit variety while keeping exactly N nodes.
- Mechanism and hypotheses: at most two/three explicitly specified cosets or character-thinned parity grids; replacement/correction positions and all-degree rule must be frozen.
- Closest registry entries (read): IDEA-181; IDEA-182 and its full C1 candidate record; PD-N034 (unshifted adjacent-mod4 Chebyshev union singular on n≡2 mod4); T2-01; DMVX LIT-306/322.
- Separation criterion / falsifier: corrections must leave the inherited null variety and avoid an exact identification with IDEA-182's failed unshifted phase. Persistence of the displayed null polynomial or that identification kills the claimed escape.
- Literature baseline / limitations: known coset-union architecture; the DMVX node excess is not a universal interpolation lower bound.
- Applicable obstructions: fixed-period density PD-T081, specialized cosine rank, and exact cardinality must all be checked; changing the number of cosets is insufficient.
- Novelty gate verdict: variant with explicit hypotheses to be supplied, no novelty claim.
- Cheapest decisive test / kill criterion: exact count and old-null evaluation before a new rank or mesh scan; D2 kills only a frozen deficient family.
- Test discriminability: removal of one null is necessary, not sufficient for full rank.
- Actual tests and evidence: none; specifically handoff T2(b) DMVX thinning was **not launched**.
- Disposition / reason / resume condition: deferred, no concrete correction/mask was frozen. Resume under T8 with a written degree-uniform mask/coset rule, exact cardinality and an explicit comparison to IDEA-182/PD-N034 before testing.
- Canonical theory: no result for this route; original record novelty-gate-T2.md.
- Topic / audit / history: handoff 01 T2(b)/(d); audit-01 M2(d/e), M3; 2026-11-06. The permanent T2 gate-timing qualifier below applies.

## IDEA?padua-3d-codex-T2-c — mod-6 fibre revisit

Aliases: handoff T2(c); cardinality-valid residue mask.

- Question / scope: a new structural reason for a mod-6 or other cardinality-valid Lobatto fibre to interpolate Π_n.
- Mechanism and hypotheses: a fixed mask on exact Lobatto axes; prospective rule and genuine structural distinction from the killed PD-N037 screen required.
- Closest registry entries (read): IDEA-187/188 and PD-N037; PD-T081; T2-02.
- Separation criterion / falsifier: a new mask must escape the exact old nullspace/cardinality obstruction; renaming a failed fibre or repeating its generic-axis witness erases the distinction.
- Literature baseline / limitations: periodic-grid mechanism is known; generic axis ranks cannot certify cosine specialization.
- Applicable obstructions: inherited PD-N037 and fixed-period density apply under their written hypotheses.
- Novelty gate verdict: duplicate unless an explicit escaped hypothesis is supplied.
- Cheapest decisive test / kill criterion: exact count and old-null test before a rank run; reject the fixed mask on certified deficiency.
- Test discriminability: exact cosine nodes distinguish the proposed escape from misleading arbitrary-axis ranks.
- Actual tests and evidence: **not launched** in T1–T6.
- Disposition / reason / resume condition: deferred because no new structural reason was supplied. Resume under T8 only with a frozen rule and written hypothesis escape; no repetition of a killed family.
- Canonical theory: PD-N037, no new negative result.
- Topic / audit / history: handoff 01 T2(c); audit-01 M2(d/e); 2026-11-06.

## Permanent timing qualifier for all T2 registrations

The initial T2 gate did not read every obstruction/disposition table in full before its mechanism runs. Later reading and audit cannot repair that chronology. The initial work used a heading/alias/summary scan and selected full readings; it claimed no novelty. Every eventual T2 IDEA registration must carry this qualifier (IDEA-576 precedent), linked to the canonical LOG disclosure and audit-01 M3. The phase/union/mod-6/omit-n3 records above are retrospective retention, not proof of pre-run compliance.
