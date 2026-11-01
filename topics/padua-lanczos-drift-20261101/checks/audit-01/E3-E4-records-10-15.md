# E34 audit findings — E3 (records 10, 11) and E4 (records 14, 15)

Auditor: Claude Opus 5.5, xhigh (one of four independent auditors; load-bearing question 5). Chosen for adversarial mathematics on new mechanisms (CLAUDE_ROLES Independent audit). Not the developer. No repository writes and no state-changing git commands; scratch only under `.../scratchpad/audit/E34/`. Repo clean after all runs (`git status --porcelain` empty).

Candidate: branch `codex/padua-lanczos-drift-20261101`, HEAD `36c93794ce02f92c76c89e5a9ec8095eb238d91d`; scientific source `b09e1db…`. `git diff --stat b09e1db HEAD` touches no E3/E4 file; the four records are last changed in `2d20672`. Audited content (sha256, identical to the hashes pinned in `evidence/independent-scalar-01.json`):

| File | sha256 |
|---|---|
| theory/drift-codex-e3-10-polynomial-span-certificate.md | 611d40f116f02baca656eb2f8f50fee9c87a4b93a3cfa766afe79f87c0cbbdc5 |
| theory/drift-codex-e3-11-selection-criterion.md | 30c3005063ee5e4ccb99279d2ac32d7e7d04a934fff11ab2620bd4e341a2c518 |
| theory/drift-codex-e4-14-noiseless-quantifier-refutation.md | 5f58acc4c70046c1f9e25321044dfed89de07388851cae710f691b4f7efcf2c8 |
| theory/drift-codex-e4-15-projection-only-closure-obstruction.md | 2b3f5c740e77b84c99477c6b82553312d7e2b8f57a96868c1a1c0ee1c377e3c4 |
| topics/…/ideas-e3-e4.md | d0803b35669f35f28e365c6c6ce1d8ed5ecca1abcf855baeb12c54e888b68003 |

## (a) Files read

- Full: AGENTS.md; agents/claude/CLAUDE_ROLES.md; handoffs/02-audit.md; topic LOG.md, plan.md, report.md, directions/E3.md, E4.md, ideas-e3-e4.md, independent-checks.md, checks/independent-math-01.md, proposed-record-changes.md, local-results-entry.md; the four records; PD-T032 (node-row-representation…), PD-T047 (commutator-shadow…), PD-T054 (condition-C-staircase…), PD-T055 (bj-universal-reorthogonalization-obstruction-open).
- Partial (statement/scope sections): handoffs/01-work.md (lines 1–80); PD-T041, PD-T050, PD-T053, PD-N013, PD-N015, PD-T051; titles only of PD-T058/059/060, PD-N020/022.
- state/IDEAS.md: rows 637–736 (IDEA-077…176) and targeted greps (minimax, staircase, surrogate, computed-coefficient, quotient, projection-only, closure, zero-error, pathwise, reorthogonali*). **Not** a full read; the full read is another auditor's job. literature/INDEX.md rows LIT-241–243 only.
- Code/evidence: tracks/bivariate-lanczos/code/drift/check_independent_math.py (lines 1–30, 140–228; `check_e4` is the only drift code that touches E3/E4; there is no E3 code); evidence/independent-math-01.json (E4 block, input hashes); evidence/independent-scalar-01.json lines 1650–1680 (pinned record hashes).
- Not read: agents/WORKFLOW.md, the old topic report/SPLITS/L2 prior-art review, any literature fulltext.

## (b) Commands actually executed and results

All are my own scripts (Fraction/NumPy), importing no campaign code, except run 4. Box: Python 3.13.18, NumPy 2.5.3, 2 CPUs. Every run took under 2 s.

1. `python3 -I e4_exact_audit.py > e4_exact_audit.out.json` (sha256 of the script 28de80fb…, of the output ad5a798d…). This is an exact-rational reconstruction of record 15, and every assert passed:
   - T_3 moments: E[x]=E[y]=1, E[x²]=E[y²]=2, E[xy]=1/2. The 10×10 degree-≤3 Vandermonde has rank 10, so U(3) holds. The prefix [1], [x−1], [(x+2y−3)/√3] is orthonormal, and ‖v_21‖²=3/2.
   - I computed w independently as (I−P_V)v_21 by an exact Gram solve, and r independently as the normal part of y³ with respect to Π_2. Both equal the record's polynomials. b²=28/115 and ‖[r]‖²=72/175. All 10 table rows match, with column sums of squares 1288 and 5040. The Jq_y identity holds with its remainder in V.
   - **(a) Same span for every rule.** I sampled 48 projection-only rules: 12 for each of η ∈ {1, 1/3, −7/2, 1/1000}, where the source is η[r], so ε²=η²·72/175. The rules mixed random rational subtraction coefficients, exact orthogonal-projection coefficients and zero passes, used 0–4 passes, and rescaled by random nonzero rationals. Every rule had rank 6, and its span equaled V⊕span{w+ηr}. The span theorem itself rests on the analytic argument; the samples only corroborate it.
   - **(b) The span differs from the exact graded space.** rank([cols, S_2]) = 7. With D=P̂_2−P_2, exactly D⁴=λD² and tr D²=2λ, where λ=ε²/(b²+ε²). So θ_2²=λ, e.g. 414/659 at η=1 and 207/122500207 at η=1/1000.
   - **(c) The J-closure defect is nonzero, with exact values.** Let G=P_1X(I−P̂_2)XP_1. Then G²=(tr G)G, so δ_X(1)²=tr G=(4/3)b²θ_2². At η=1 this is 672/3295. So bound (8) holds with **equality**. The same computation for the formed operator Y gives **δ_Y(1)²=b²θ_2²**, which is 504/3295 at η=1, so δ_Y=(√3/2)δ_X.
   - (9): at u=1/4, θ_2²/u²=5520/1241≥4 and δ_J²/u²=1792/1241≥1. The exact thresholds are u²≤121/1380 and u²≤56/345.
   - Controls (each is a source equal to the normal part of y³ added to one raw product). Q_3={0..3}² is a **product grid**; with BJ and the source in (2,1), δ_X(1)²=δ_Y(1)²=45/161. On T_3 with BJ: a source in the formed (2,0)=Xq_x gives δ_X²=672/2305 and δ_Y=0; a source in (2,2)=Yq_y gives δ_X=0 and δ_Y²=672/2305. On T_3 with the mirror selection and the source in (2,1)=Xq_y, I get the same values as BJ.
2. `python3 -I e4_rec14_zero_error.py` (script a2cc5240…). Zero-error exact Gram–Schmidt with BJ parents on T_3 (s=3) and T_5 (s=4) gives exact spans and A S_t ⊆ Ŝ_{t+1} for every t<s: PASS.
3. `OPENBLAS_NUM_THREADS=1 python3 -I e3_check.py > e3_check.out.json` (script 515cad23…, output 54e6fbba…).
   - Part A (exact Fraction): T_4, s=3, 3 trials, arbitrary admissible parents, arbitrary rational c_kl, β_k>0 and f_k. In every trial the surrogate p̂_k has a nonzero coefficient on monomial k and no later monomial. The node-row identity Lbar̂(z_i)(ξ_i−√w_i p̂(z_i))=−ζ_i holds exactly at all nodes.
   - Part B (float64, MEASURED sanity only): T_6, s=4, 300 runs. A third of the runs used coefficients with 30% relative error, a third used arbitrary random coefficients, and a third were near-exact. There were 0 violations of (2), of (3) or of the E_+ refinement. The maximum θ/bound was 0.148, and 187 of the 300 runs gave informative bounds (<1).
   - Part C (float64, MEASURED illustration): T_8, s=5. I computed K_R and χ_R for all 16 = 2^(s−1) staircases. In the aggregate model with ‖d_k‖=‖A_kq_p‖ and t=1e−7, θ(t)/t stayed below C_loc√(N−1)χ_R K_R for every staircase. For example, BJ gave 144 against a bound of 8396, and mirror gave 23.5 against 2320.
4. `python3 -B -c "...import check_independent_math as c; c.check_e4()"`. This executes the campaign checker's E4 function only, without writing bytecode, and returned PASS. That function checks polynomial identities and norms only. It does not test the every-rule span claim or the spectral norms; my run 1 does.

## (c) Per-record disposition

| Record | Claimed status | Disposition | Reason |
|---|---|---|---|
| e3-10 polynomial span certificate | PROVED | **CONFIRMED** | I reconstructed the proof independently. The surrogate is a triangular polynomial basis with nonzero leading coefficients for any coefficients, so its range is S_s. The normalized row inverse Lbar̂=diag(1,1/β)L̂ is correct (exact check). (2), (3) and the E_+ refinement are correct. No accuracy assumption is made and (C) is not used. The only defect is an editorial one in E3.md (F7). |
| e3-11 selection criterion | PROVED (fixed-degree); safety OPEN | **CONFIRMED-WITH-CORRECTIONS** | (6) is correct for each fixed smooth family. Computability is correctly restricted to represented rational/real-algebraic inputs. No text derives score bounds from (C). However, the remainder-dependence sentence omits the dependence on the family (F4), and the staircase restriction is unused in the proof and excludes the pivot rule (F5). |
| e4-14 noiseless quantifier refutation | PD-N, PROVED | **CONFIRMED-WITH-CORRECTIONS** (mathematics confirmed; PD-N vehicle not endorsed) | The logic is valid but trivial: zero error is admissible and exact Gram–Schmidt is exact. It does not claim to refute IEEE behavior or a worst-case assertion. The refuted wording is one the developer introduced, and the stated "attempted mechanism" is not engaged by the proof (F3). |
| e4-15 projection-only closure obstruction | PD-N, PROVED | **CONFIRMED-WITH-CORRECTIONS** | (7), (8) and (9) are reproduced exactly, and (8) is in fact an equality. Closure is kept separate from in-span implicit-section accuracy and from exponential amplification. However, the title and scope attribute the failure to the unformed J-product and the non-product measure, when the obstruction is generic and equal-sized for the formed F operator (F1). The span identity is PD-T055's own heuristic, uncredited (F2). |

## (d) Findings

**E34-F1 — medium — record 15's obstruction is generic, not about a "missing J-product" or non-product support.**
Locations: theory/drift-codex-e4-15…md:1 (title), :4 (alias "unformed-product closure failure"), :27, :55–56 ("repair the unformed J-product"; "this explicit non-product measure"), :128 ("isolates what 'the product was never formed' can rigorously mean … A single source in an unformed J direction then creates a J-defect"); directions/E4.md:16, :22; ideas-e3-e4.md:77, :81; inherited in report.md:78–81 and proposed-record-changes.md:18.
- **Evidence.** The source sits in the *formed* F-product v_21=Yq_x. Its direction e∝(normal part of y³) is not a J-direction. With the record's own construction (run 1), the formed operator's defect is δ_Y(1)²=b²θ_2², i.e. δ_F=(√3/2)δ_J, which is the same order. On the product grid Q_3 the same construction gives δ_X=δ_Y≠0. Sources in formed X or Y products give defects in X only or in Y only. The mirror selection gives identical values.
- **Diagnosis.** The defect lands on whichever operator's image of S_1 meets the perturbed raw column modulo the other columns. Neither formed/unformed status nor non-product support enters the proof. The J/F asymmetry that defines PD-T055 is absent here: PD-N013(b) has F-defects ≤1.5e−15 while J-defects grow.
- **Formulas.** (7)–(9) are correct as stated.
- **Required response.** Retitle and rescope as a generic fixed-degree lemma: any selection, any measure with N_2<M, and a raw-product source with a component normal to S_2. Keep T_3/BJ as the explicit instance. State δ_F(1) and the equality in (8). Delete the "never formed"/"unformed J direction" interpretation and the non-product emphasis. Update E4.md, IDEA-15, report.md and the PD-T055 proposal text accordingly.

**E34-F2 — medium — the span identity that removes all rule coefficients is uncredited prior content.**
- **Prior content.** PD-T055's own "Heuristic" (tracks/bivariate-lanczos/theory/bj-universal-reorthogonalization-obstruction-open.md:49) already states: "span Q̂_{≤k} = span(Q̂_{<k}, B_kq̂_{p(k)} − f_k), so the coefficients (h_k, g_k) of step k change the computed spans only through the rounding f_k".
- **How it is cited.** Record 15:68 cites PD-T055 only as the "OPEN universal obstruction". IDEA-15's separation (ideas-e3-e4.md:83–84) says prior records give "recursions and tested failures, not this all-coefficient finite quotient calculation" and calls the coefficient-independent joint span "a genuine every-rule statement".
- **What is new.** Only the exact fixed-prefix T_3 instance with its constants.
- **Required response.** Credit the PD-T055 heuristic in record 15 (Depends on, Sources, Scope) and in IDEA-15. Redo the novelty verdict, which is likely "variant: exact instance of the recorded heuristic".

**E34-F3 — medium — record 14 is the wrong registry vehicle as written.**
- **Evidence.**
  - The refuted statement is a reading the developer introduced. Record 14:85 says: "New proposed interpretation explicitly adds 'every allowed error realization'". PD-T055 (U) concerns "the computed run" in floating point with working-precision storage.
  - The refutation is a one-line consequence of allowing zero error. It uses no BJ structure: exact Gram–Schmidt is exact under any admissible parents, and run 2 checks the BJ case.
  - Yet :43 lists the "Attempted mechanism" as "deduce a positive drift lower bound from BJ's omission of products and the clamped commutator recursion", which nobody attempted and which the proof does not engage.
  - CLAUDE_ROLES says PD-N is only for scoped refuted/failed mechanisms, while equivalent or abandoned candidates stay IDEA dispositions. There is precedent: IDEA-175 rejected a failed explanation with "no … new PD-N".
  - The exactness of the implicit section in exact arithmetic is already PD-T032 part 2 ("In exact arithmetic Ĥ_J = H_J"), which record 14:48 does not cite.
- **My view.** Record 14 should be an IDEA disposition (REJECTED: an ill-posed formalization of PD-T055's quantifier), plus the PD-T055 note already drafted in proposed-record-changes.md:18. It should not be a PD-N.
- **Required response.** Either convert as above, or, if AC keeps a PD-N, retitle it as a quantifier clarification, rewrite :43 and cite PD-T032 part 2. In either case, record 15:35 depends on record 14 for U(3). Move that lemma into record 15, or cite principal-lattice unisolvence.

**E34-F4 — medium — record 11's remainder quantifier is incomplete.**
- **Location.** theory/drift-codex-e3-11…md:26: "The remainder constant and its neighborhood may depend on the fixed measure, selection and s."
- **Problem.** The O(t²) term also depends on the particular perturbation family: its second-order terms and the smoothness of its coefficient path. No uniformity over the class of (Hres)-families holds. For example, f_k(t)=t d_k+t²G g_k satisfies (Hres) for every G, and the second-order term grows with G. The proof (:64–74) is valid for each fixed family, and the compact-set uniformity sentence is fine.
- **Required response.** Add "and on the particular family" to the dependency list, and state that no remainder uniform over all (Hres)-families is asserted. Mirror the change in E3.md:20–22.

**E34-F5 — low — record 11's staircase restriction and minimization are unused in the proof of (6).**
- **Problem.** (6) holds for any admissible selection with K_R≤K_0 and χ_R≤χ_0. Restricting the search to (C)-staircases excludes the pivot-adaptive rule, which violates (C) (PD-T050/054) yet is E1's good comparator and PD-T051's best measured rule. Line :50 mentions the alternative only in passing.
- **Optional.** The first-order transfer is a routine continuity corollary of record 10. Consider making it a corollary section of record 10 rather than a separate PD-T (split rules: minor routine steps are not aggregated). "Settles the computable-criterion subproblem" (:80) overstates what is a definition plus finite decidability.
- **Required response.** State both facts explicitly in Scope.

**E34-F6 — low — stale or missing check provenance.**
- **Stale text.** Record 15:64 ("pending integration") and ideas-e3-e4.md:91 ("awaits parent integration") are out of date: checks/independent-math-01.md and evidence/independent-math-01.json (E4 block, `check_e4`) now exist. Record 11:54 says independent analytic checking "remain[s] to be performed", but an Astra reconstruction now exists.
- **Missing provenance.** The developer's "temporary SymPy calculation" (record 15:64) has no recorded command, script or hash. It is non-load-bearing, so mark it explicitly as non-evidence.
- **Required response.** Update the text to cite the receipt.

**E34-F7 — low (editorial) — E3.md overstates what (2) needs.**
- **Location.** directions/E3.md:14: "Near-orthogonality then converts its residual bound to a span bound."
- **Problem.** (2) needs only full column rank and σ_min(Q̂). Near-orthogonality is used only for (3).
- **Required response.** Reword.

**E34-F8 — low — the E3 target has no durable OPEN record.**
- **Problem.** The target is "some staircase/selection keeps drift polynomially bounded on a non-product family". It appears only in E3.md:5/:12, the plan.md ledger, record 11:46/:80 and IDEA-10, and partly as PD-T054's open item and IDEA-151.
- **Required response.** At preparation, map it explicitly to an existing OPEN item or register it as an OPEN target. It must not be carried only in topic prose.

**E34-F9 — low — a considered alternative is not retained as a candidate.**
- **Problem.** Parent-repair and reference-basis rules, including PD-T055's own suggested "cheapest discriminating experiment" (reorthogonalize the parent against an extended-precision basis before forming the product), are named as possibly evading the obstruction (record 15:134; E4.md:16). They appear in ideas-e3-e4.md only inside IDEA-16's kill criterion, not as a retained candidate with a kill test.
- **Required response.** Add a deferred IDEA entry.

**E34-F10 — low — consistency.**
- **Problem.** local-results-entry.md:23–25 omits record 14 entirely. The text proposed for PD-T055 (proposed-record-changes.md:18) inherits F1's J-specific wording.
- **Required response.** Update both after F1/F3 are resolved.

Checked and found acceptable:
- Record 10's basis is nonzero and triangular. Its normalized inverse score is correct (Definitions :37 match PD-T032's L̂).
- No E3 text claims polynomial score bounds from (C) (record 10:41; record 11:36, :80; E3.md:24; report.md:71–72; IDEA-10/11).
- Record 11's computability restriction is correct: exact data are real-algebraic, so threshold and minimization decisions are decidable, and no efficiency is claimed.
- The staircase count 2^(s−1) matches PD-T054(a).
- Record 14 explicitly does not refute fixed IEEE or worst-case readings (:39, :72–77). report.md:74–77, E4.md and LOG:52 agree.
- Record 15's rule class, prefix, "arbitrary subtractions" and source are fully specified and reconstructable. Closure is distinguished from in-span implicit-section accuracy (:130) and from exponential amplification (:31, :128).
- Each retained candidate (IDEA-10, 11, 14, 15, 16) has a closest predecessor, a separation criterion, a kill test and a scoped reason.
- No PARTIAL upgrade; PD-T055 stays OPEN.

## (e) Remaining uncertainty

- **Coverage of state/IDEAS.md and literature.** Not read in full (assigned elsewhere). A duplicate of the record-10 surrogate argument in the V+A literature (LIT-280–284, Barrio–Peña–Sauer §5 heuristics) is plausible. No priority is claimed, and I did not check fulltexts.
- **Evidence status of my E3 checks.** Parts B and C are float64 corroboration only, not certified. No certified K_R/χ_R evaluation exists for the frozen T_24/rotated Q_24 rules, so whether any staircase is accepted at a useful threshold is untested.
- **Status of the span claim.** Record 15's every-rule span claim rests on the analytic span identity. My 48 sampled rules corroborate it but do not prove it.
- **Brief mislabelling.** The brief calls PD-T058/059/060 "(C)/(W) staircase" records. In this repository they are moment-cone/backward results (titles read only). The (C)/(W)/staircase predecessors are PD-T050/PD-T054, which I read.
- **Not done.** No re-audit of PD-T032/047/054 themselves; their correctness is assumed where records 10, 14 and 15 lean on them.
