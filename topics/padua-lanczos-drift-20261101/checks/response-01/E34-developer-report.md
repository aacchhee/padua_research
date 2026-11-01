# Response-01, group E34 (E3/E4 records 10, 11, 14, 15)

Developer: Claude Opus 5.5 (`claude-opus-5-5`), xhigh. Repository `/home/claude/padua_research`, branch `codex/padua-lanczos-drift-20261101`, head `5df225f`. No git state was changed. Only the owned files were edited, plus one new checker and one new evidence file. The untracked `results/` directory at the repo root is not mine and was not touched.

## (a) Dispositions

| Finding | Disposition | Files and line ranges (current numbering) | Summary |
|---|---|---|---|
| E34-F1 (medium) | FIXED | record 15: whole file rewritten; title :1, aliases :4, Statement :8–70, Definitions :71–82, Assumptions :83–91, Status :92–105, Negative scope :106–123, Proof :163–266, Scope :267–282, History :292–300. directions/E4.md :1–54 (rewritten). ideas-e3-e4.md IDEA-15 :102–136 | **New general lemma, PROVED.** Setting: any positive discrete measure with U(t+1) and M>N_(t+1), any t≥0, any admissible selection, and one raw-product source with f_⊥≠0. For every projection-only rule: (a) the columns have full rank; (b) the span is the same, V_m⊕span{(1+α)w+f_⊥}; (c) θ=‖f_⊥‖/sqrt((1+α)²b²+‖f_⊥‖²); (d) δ_A(t)=κ_Aθ exactly, κ_A=0 iff AS_t⊆V_m, and κ_(A_m)≥b for the forming operator. The T_3/BJ case is kept as the explicit instance. In it, (8) is now an **equality**, δ_Y(1)=bθ_2=(√3/2)δ_X(1) is added as (8′), and δ_Y(1)≥u is added to (9). The “never formed”/“unformed J” reading and the non-product emphasis are deleted; the original wording is kept in History. Controls are reported as exact computations from the new checker (checks only). |
| E34-F2 (medium) | FIXED | record 15 Aliases :4, Depends on :124–132, Sources :151–162, Proof (b) :178, Scope :267–271; IDEA-15 closest entries, separation, verdict :104–120; E4.md :19 | PD-T055's heuristic span identity (bj-universal-…-open.md:49) is credited. Identity (10) is stated as its exact fixed-prefix, single-degree instance. The IDEA-15 verdict is now “variant — exact fixed-prefix, single-degree instance of PD-T055's recorded heuristic span identity, with closed-form angle/defect constants; no new mechanism”. |
| E34-F3 (medium) | FIXED (preferred route: IDEA disposition) | ideas-e3-e4.md IDEA-14 :65–100; record 14 banner :3 and History :88; record 15 U(3) proof :204–212, Depends :132; E4.md table :9 and :15 | Record 14 is converted to IDEA?drift-codex-14: REJECTED, refuted as an ill-posed formalization of PD-T055's quantifier; no PD-N. PD-T032 part 2 is cited, and the bogus “attempted mechanism” is withdrawn. The entry holds all of record 14's content: statement, proof, quantifier table and checks. U(3) is proved inside record 15, so record 15 no longer depends on record 14. **Orchestrator: remove `tracks/bivariate-lanczos/theory/drift-codex-e4-14-noiseless-quantifier-refutation.md`** (I did not delete it; it now carries a withdrawal banner). |
| E34-F4 (medium) | FIXED | record 11 :26, History :106; E3.md :24 | The remainder now depends on the particular family. The f=td+t²Gg example is given, and no uniformity over all (Hres)-families is asserted. Compact-family uniformity is made precise: f_k(t;ω) jointly C² on a neighbourhood of {0}×Ω, with Ω compact. |
| E34-F5 (low) | FIXED | record 11 Scope :83–97, History :107; E3.md :18; IDEA-10 :30 | Scope now states three facts: the staircase restriction is unused in proving (6); it excludes the pivot-adaptive rule; and (6) holds for all 2^(s(s−1)/2) admissible selections. The phrase “settles the computable-criterion subproblem” is replaced by “finite exact-data criterion (definition, decidable for represented inputs) plus sufficient first-order theorem”. The corollary suggestion was considered and **separate files were kept**, for three reasons: (i) record 11's subject is the criterion — its definition, decidability and acceptance semantics — which record 10 lacks; (ii) record 10 is non-asymptotic, while (6) has a family-dependent O(t²) remainder, and separation stops either quantifier being read into the other; (iii) the CONDITIONAL application and the OPEN target attach to the criterion. Record 11 now labels (6) as a routine continuity corollary of record 10. |
| E34-F6 (low) | FIXED | record 15 Checks :133–150; record 11 Status :40 and Checks :52–60; record 10 Status :45 and Checks :59–63 (consistency only); ideas-e3-e4.md :39, :43, IDEA-15 test results; E3.md :28–33; E4.md :43 | The text now cites checks/independent-math-01.md, evidence/independent-math-01.json (`independent_own_checker.E4`, `check_e4`), audit-01 and checks/audit-01/E3-E4-records-10-15.md. The “temporary SymPy calculation” is explicitly marked **not evidence**. |
| E34-F7 (low) | FIXED | E3.md :16 | “(2) needs full column rank and σ_min(Qhat); near-orthogonality only for (3).” |
| E34-F8 (low) | FIXED (mapping proposed; registry text in (c)) | E3.md :7 and :14; record 11 :46; IDEA-10 :40 | Proposed durable OPEN home: PD-T054's open item, extended to the span-drift form and to non-staircase selections, with a cross-reference from IDEA-151. Literal blocks are in (c4). |
| E34-F9 (low) | FIXED | ideas-e3-e4.md IDEA?drift-claude-17 :158–187; record 15 Open items :283–290; E4.md :13 and :45 | New deferred IDEA covering parent-repair and reference-basis rules, including PD-T055's extended-precision parent experiment. It gives closest predecessors (PD-T055 open item, PD-T043(c), IDEA-154/PD-N016, IDEA-148, IDEA-151, record 15, IDEA-16), a separation criterion, a preregistered kill test and a resume condition. The new ID uses the `claude` agent tag. |
| E34-F10 (low) | FIXED (proposed text) | not owned: report.md, local-results-entry.md, proposed-record-changes.md, plan.md, code/drift/README.md | Exact OLD/NEW text is in (c). It includes record 14's new disposition. |

## (b) Commands actually run

All runs from the repo root, on Python 3.13.18.

1. `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -I topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E34/e4_exact_audit.py > …/scratchpad/E34/e4_exact_audit.out.json`
   - Took 0.3 s; all asserts pass.
   - The output sha256 `ad5a798d7982fb63ababfb8bbdf264f72fa876ef900970afcf471398593391a5` is byte-identical to the audit's.
   - Reproduces δ_X(1)²=672/3295, δ_Y(1)²=504/3295 and the controls (Q_3 45/161 and 45/161; T_3 (2,0) 672/2305 and 0; (2,2) 0 and 672/2305; mirror equal to BJ).
2. `python3 -I …/scripts/E34/e4_rec14_zero_error.py`: T_3 s=3 and T_5 s=4 zero-error spans exact and defects zero, PASS.
3. `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 …/scripts/E34/e3_check.py`
   - Took 1.8 s with NumPy 2.3.5.
   - Part A is exact: PASS. Part B: 0 violations, 187/300 informative, max ratio 0.148, as the audit reported.
   - The output sha256 (`bc4ab5f3…`) differs from the audit's `54e6fbba…`, which used NumPy 2.5.3; the difference is in float digits only. This run is not used as evidence.
4. New checker, written by me (standard library only, exact `Fraction`):
   - First a scratch trial run to `…/scratchpad/E34/trial.json`. It first failed one assert, because it chose x³ instead of y³ as the normal direction; that was fixed. After a small addition (V_m=V and Jq_y checks), the final run:
   - `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json` gives **PASS: 28 instances, 2.9 s**.
   - Code sha256 `b22949c61d98207f950a5b8e1a8974e0eb1545f85dc5b639872bf09a987d6dac`; output sha256 `956dfe71e8b6958f54e19f2d7fb30f04c5788351b7942bf8be21b41977d3599c`, 30,826 bytes. The JSON records the command, code hash, Python version, platform and elapsed time; no packages are used.
   - Instances: T_3 BJ (2,1) at η∈{1, 1/3, −7/2, 1/1000}; T_3 BJ (2,0) and (2,2); T_3 mirror (2,1); Q_3 BJ, all three columns; T_3 with non-uniform weights; two general sources (α=−3/2, and 1+α=0 giving θ=1); T_4 degree 2→3 with XYYY, XXXY and XYXY sources in every column; and 12 random rational nodes with random weights at t=0 and t=1.
   - Each instance checks: sampled rules have full rank and the span (10); θ² from D⁴=θ²D² equals (11); δ_A² from a rank-one Gram matrix equals κ_A²θ²; κ_A=0 iff AS_t⊆V_m; and κ_(A_m)²≥b².
5. `git diff --stat` and `git status` (read-only): only the 7 owned files are modified, plus the 2 new files. The 77 old theory files are untouched.

## (c) Proposed text for files I do not own

**c1. `topics/padua-lanczos-drift-20261101/report.md`, E4 paragraph (lines 74–82).**

OLD
```text
**PD-T055 remains OPEN in its original scope.** **PD-N?drift-codex-14** refutes
a positive lower bound for every admissible error realization in a model
allowing zero errors. It refutes neither a fixed IEEE implementation nor a
worst-case-over-errors assertion. **PD-N?drift-codex-15** gives a ten-point
triangle, exact degree-one prefix and one degree-two source for which every
rule restricted to prior-vector subtractions has the same drifted span and
nonzero J-closure defect. This is an O(u) aggregate-source obstruction with
fixed parents/products. Exponential growth, parent repairs, implicit-section
accuracy and actual IEEE realization lie outside that result.
```
NEW
```text
**PD-T055 remains OPEN in its original scope.** Its pathwise reading, “for
every rule and every admissible error realization”, is false for a trivial
reason in a model allowing zero errors: the exact run is admissible, and
PD-T032 part 2 gives an exact implicit section. This is recorded as the IDEA
disposition **IDEA?drift-codex-14** (REJECTED: refuted, as an ill-posed
formalization), not as a PD-N. It refutes neither a fixed IEEE implementation
nor a worst-case-over-errors assertion. **PD-N?drift-codex-15** proves a
fixed-degree lemma. With an exact prefix and fixed admissible raw products,
take one raw-product source with a normal component. Then every rule
restricted to prior-vector subtractions has the same drifted span and closure
defects δ_A=κ_Aθ, and the defect is nonzero for the operator that formed the
perturbed column. The span identity is the exact fixed-prefix instance of
PD-T055's own heuristic. The lemma holds for any positive measure and
selection, product or not, and is not specific to J: in the ten-point triangle
instance the formed operator Y has δ_Y=(√3/2)δ_J. It is an O(u)
aggregate-source obstruction with fixed parents and products. Exponential
growth, parent repairs (deferred, IDEA?drift-claude-17), implicit-section
accuracy and actual IEEE realization lie outside that result.
```

**c2 (optional, mirrors F4/F5). `report.md`, record-11 paragraph (lines 68–72).**

OLD
```text
**PD-T?drift-codex-11** proves a computable filtered minimax criterion over the
2^(s−1) staircase selections and a fixed-degree first-order implication.
```
NEW
```text
**PD-T?drift-codex-11** proves a computable filtered minimax criterion over the
2^(s−1) staircase selections and a fixed-degree first-order implication whose
O(u²) remainder depends on the particular perturbation family. The staircase
restriction is not used for that implication, and it excludes the
pivot-adaptive rule.
```

**c3. `topics/padua-lanczos-drift-20261101/local-results-entry.md`, lines 23–28.**

OLD
```text
Analytic computed-polynomial span certificate, filtered fixed-degree selection
implication and restricted degree-two projection-only adverse-source obstruction
written. General staircase safety, original PD-T055, all-degree exponential
drift/matching bounds, and PD-T056 reading(G) remain OPEN. Explicit square
four-atom sqrt(epsilon) example quantifies nonexact residual allowances but
does not realize actual computed recurrence errors. Failed witness paths retained.
```
NEW
```text
Analytic computed-polynomial span certificate and filtered fixed-degree
selection implication written; the implication's remainder depends on the
perturbation family. A fixed-degree projection-only lemma is also written:
after one raw-product source, every prior-vector subtraction rule leaves the
same drifted span and a nonzero closure defect, on any measure and selection.
It is the exact instance of PD-T055's heuristic; the T_3 constants are given,
and the defect is not J-specific. The every-error pathwise reading of PD-T055
is trivially false with admissible zero errors. It is kept only as an IDEA
disposition, and the former draft PD-N?drift-codex-14 is withdrawn. General
staircase safety, original PD-T055, all-degree exponential drift/matching
bounds, and PD-T056 reading(G) remain OPEN. Explicit square four-atom
sqrt(epsilon) example quantifies nonexact residual allowances but does not
realize actual computed recurrence errors. Failed witness paths retained.
```
(Line 11 of the same file, “Claude Opus5.5 xhigh audit PENDING”, is also stale. That is outside E34, but the orchestrator should update it.)

**c4. `topics/padua-lanczos-drift-20261101/proposed-record-changes.md`.**

(i) The PD-T055 block. Replace line 18, the single paragraph inside the NEW fence of “## PD-T055: retain OPEN; add quantified scope distinctions”. The heading, Target line and OLD fence stay unchanged.

OLD (line 18)
```text
PD-N?drift-codex-14 refutes only a pathwise positive lower bound for every model-admissible error realization when the zero-error exact-real run is admitted. It does not refute literal working-precision storage or a fixed IEEE implementation. PD-N?drift-codex-15 gives a ten-point triangle, exact prefix, fixed degree-two BJ products and one aggregate source for which every prior-vector subtraction rule leaves the same drifted span and a nonzero J-closure defect. Its conclusion is O(u), not exponential, and neither implicit-section in-span error nor scalar-operation realizability follows. A final formalization must distinguish every-error, worst-case-error and deterministic-IEEE quantifiers. (U) remains OPEN.
```
NEW (two paragraphs replacing line 18)
```text
Quantifier note (IDEA?drift-codex-14; an IDEA disposition, not a PD-N). Read pathwise, for every rule and every error realization admitted by an upper-bound model that allows the zero error and exact-real projection, (U) is false for a trivial reason: the zero-error exact run has exact spans, δ_X=δ_Y=0, and Ĥ_J=H_J by PD-T032 part 2. This disposes only of that reading. It does not refute literal working-precision storage, a fixed IEEE implementation or a worst-case-over-errors reading. A final formalization of (U) must choose among the every-error, worst-case-error and deterministic-IEEE quantifiers rather than interchange them.

Fixed-degree instance of the heuristic in Proof or evidence (PD-N?drift-codex-15). Take an exact prefix through degree t and fixed admissible degree-(t+1) raw products. Then the span identity of the heuristic is exact for every coefficient choice: after a source f in one raw product, every rule that only subtracts prior vectors and rescales gives the same computed span. Its angle is θ_(t+1)=||f_⊥||/sqrt((1+α)²b²+||f_⊥||²). Its defects are δ_A(t)=κ_Aθ_(t+1), with κ_(A_m)≥b for the operator A_m forming the perturbed column. This holds for any positive measure with U(t+1) and M>N_(t+1), product or not, and any admissible selection. The defect is not specific to J or to unformed products: on T_3 with BJ and the source in Yq_x, δ_Y(1)=(√3/2)δ_X(1). The conclusion is a fixed-degree O(u) obstruction, not exponential amplification; neither implicit-section in-span error nor scalar-operation realizability follows. Parent-repair and reference-basis rules, including the experiment named in Open items, lie outside that class (deferred, IDEA?drift-claude-17). (U) remains OPEN.
```

(ii) New block for E34-F8. Append it after the PD-T055 section, before “## PD-T056”.
````text
## PD-T054: register the E3 polynomial-safety target in the existing open item (audit-01 E34-F8)

Target: `tracks/bivariate-lanczos/theory/condition-C-staircase-selections-acyclic-sections.md`.

OLD
```text
A residual description for selections violating (C) (PD-T?…-205 open item); whether the staircase family contains a rule whose coupled residuals stay small on non-product measures (alt is a staircase and is killed on four of six non-product sets, PD-N?…-203; mirror on four).
```

NEW
```text
A residual description for selections violating (C) (PD-T?…-205 open item); whether the staircase family contains a rule whose coupled residuals stay small on non-product measures (alt is a staircase and is killed on four of six non-product sets, PD-N?…-203; mirror on four). This item is also the durable OPEN home of the E3 target of topic padua-lanczos-drift-20261101, in polynomial span-drift form: does some staircase keep the full-reorthogonalization span drift O(u·poly(s)·χ) on a non-product family? The same question is open beyond (C), for some admissible one-relation selection such as the selection the pivot-adaptive rule makes on exact data. OPEN. PD-T?drift-codex-10/11 give a computed-data span certificate and a finite exact-data sufficient criterion with a first-order guarantee. Whether any selection passes that criterion with polynomially bounded scores is unproved, and no such bound is claimed on the triangle or rotated-square families.
```

At preparation, also add to the IDEA-151 row of `state/IDEAS.md`, at the end of its disposition cell: “Polynomial span-drift form of the safety question registered as OPEN in PD-T054's open item; sufficient criterion in PD-T?drift-codex-10/11 (padua-lanczos-drift-20261101).”
````

**c5 (optional). `topics/padua-lanczos-drift-20261101/plan.md`, lines 22–23.**

OLD
```text
| E3 | OPEN general family safety | Analytic span certificate and filtered fixed-degree criterion proved; useful uniform score bounds open | Theory10/11, E3.md |
| E4 | OPEN original PD-T055 | Quantifiers formalized and restricted projection-only adverse-source obstruction proved | Scoped negative theory14/15, E4.md |
```
NEW
```text
| E3 | OPEN general family safety | Analytic span certificate and filtered fixed-degree criterion proved (family-dependent remainder; staircase restriction unused in (6)); useful uniform score bounds open; durable home proposed: PD-T054 open item / IDEA-151 | Theory10/11, E3.md |
| E4 | OPEN original PD-T055 | Pathwise quantifier reading disposed of as IDEA?drift-codex-14 (no PD-N); fixed-degree projection-only lemma proved as the exact instance of PD-T055's heuristic; parent repair deferred (IDEA?drift-claude-17) | Scoped negative theory15, ideas-e3-e4.md, E4.md |
```

**c6. `tracks/bivariate-lanczos/code/drift/README.md`.** Insert before the line `## E5 symbolic checks`:
````text
## E4 exact closure check (response-01)

```bash
python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json
```

Standard library only (exact `fractions.Fraction`), about 3 seconds. The script evaluates the fixed-degree lemma of PD-N?drift-codex-15 on 28 instances: the rule-independent span, the angle closed form and δ_A=κ_Aθ. It also recomputes the record's T_3 constants. Sampled rules corroborate, and do not prove, the every-rule span identity.

````

**c7. Orchestrator actions (not text).**

- Remove `tracks/bivariate-lanczos/theory/drift-codex-e4-14-noiseless-quantifier-refutation.md` at preparation.
- Immutable receipts (final-validation.json:406, protocol-check.json:417, independent-math-01.json:55, independent-scalar-01.json:1667, handoffs/02-audit.md:34) and LOG.md:52 still list record 14 as a PD-N. Annotate in LOG/response-01; do not rewrite them.
- One fewer PD-N final ID is needed from the N062–071 reservation.
- `independent-checks.md:10`'s E3/E4 row could add “Claude audit-01 run 1–3; response-01 e4_closure_check.py”.

## (d) For the Codex re-audit

1. **Material scope change, record 15.** The statement is now a general fixed-degree lemma (a)–(d), PROVED, written from scratch in response-01. It covers any positive measure with U(t+1) and M>N_(t+1), any t≥0, any admissible selection and one raw-product source with f_⊥≠0, including non-normal sources via α. Check in particular:
   - the full-rank argument (a);
   - the claim that every exact fully orthogonalized admissible recurrence returns the canonical prefix;
   - the rank-one defect formula (12);
   - κ_(A_m)≥b, which needs a unit parent.

   The T_3 numbers are unchanged, but (8) is now an equality, and (8′) and δ_Y(1)≥u (for u²≤28/345) are new. The PD-N's refuted mechanism is restated as “fixed-degree coefficient/pass repair after a raw-product source”. Status stays PROVED.
2. **Record 14 vehicle change.** It is no longer a PD-N: it becomes IDEA?drift-codex-14, REJECTED: refuted, with no PD-N (reasoning: L5, the template's “PD-N optional”, the IDEA-175 precedent). Check that this reading of WORKFLOW is acceptable to AC, and that the IDEA entry preserves everything in the withdrawn file.
3. **Record 11.** There are two scope additions: (6) for non-staircase admissible selections (count 2^(s(s−1)/2)), and family-dependent, non-uniform remainders. Precise compact-family uniformity now assumes joint C². The status is unchanged.
4. **Record 10.** Metadata only: status parenthetical and Checks.
5. **New items.** IDEA?drift-claude-17 (deferred) uses a new agent tag. The new evidence file response-01-e4-closure.json and its checker are not proof dependencies.
6. **F8.** The OPEN-home mapping is only proposed. It takes effect when the PD-T054/IDEA-151 blocks are applied at preparation.

Not obtained or claimed: no multi-degree statement, no exponential amplification, no IEEE realization, no simultaneous-source version, and no run of the IDEA-17 experiment.
