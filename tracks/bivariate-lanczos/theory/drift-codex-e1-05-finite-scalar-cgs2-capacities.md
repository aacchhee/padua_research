# PD-T?drift-codex-05 — Exploratory formal scalar-CGS2 capacity experiment and the unresolved factor-ten comparison

ID kind: PD-T.
Aliases: scalar operation sensitivity follow-up; multinode greedy rounding witness; formal relative-error capacity; scalar factor-ten target.
Split from: E2's scalar-rounding explanation route. Explicit-family matching rates and actual IEEE activation remain OPEN.
Split into: [PD-T?drift-codex-06](drift-codex-e1-06-finite-scalar-cgs2-separation.md) (response-02, audit-02 A02-M2). It holds the finite exact inequalities formerly stated here: the full-graph comparator uppers U_inf (T24/pivot, rotQ24/alternating), the explicit multinode BJ node-sign lower witnesses, the squared ratio lower bounds, K_inf,BJ > 800 K_inf,pivot on T24 and K_inf,BJ > 7 K_inf,alt on rotQ24. Status there: PROVED, computer-assisted. This file keeps the measured exploratory experiment, its post-hoc history, the INCONCLUSIVE both-grid factor-ten test outcome and the factor-ten target.

## Statement

Use exactly the fixed-choice, left-to-right dense-matrix-vector scalar CGS2 implementation and the independent relative-operation model of PD-T?drift-codex-03. Every local scalar parameter has absolute value at most one; thus K_inf is an **l-infinity source** condition, unlike the Hilbert aggregate condition in PD-T?drift-codex-04. Nodes and choices are the same T24/rotQ24 at degree 12, with all 90 source columns available.

**Measured experiment.** After E1, the developer explored in exact rational arithmetic how far the declared formal scalar-CGS2 capacity separates BJ from E1's decisive comparators, pivot on T24 and alternating on rotQ24, at degree 12. The steps were, in order:

1. subset maps for coordinate multiplications and component divisions (`e1_scalar.py`);
2. the full-graph comparator upper U_inf (`e1_cgs2.py`);
3. coherent one-node BJ witnesses at nodes taken from the subset-map witnesses (`e1_cgs2_witness.py`);
4. multinode BJ greedy-sign witnesses at the target columns of the best one-node witness, t=86 on T24 and t=90 on rotQ24 (`e1_cgs2_multinode.py`).

The resulting endpoints and signs, and the inequalities they imply, are stated and proved in [PD-T?drift-codex-06](drift-codex-e1-06-finite-scalar-cgs2-separation.md). They are not restated as claims of this file. As part of the measured search, the one-node coherent witnesses gave squared certificate ratios of about 131256 (T24) and 5.18 (rotQ24); the multinode greedy witnesses raised them to about 657331 and 62.09. On rotQ24 neither witness family reached 100 (evidence `e1-scalar-cgs2.json`, `comparisons`; `e1-multinode-certificates.json`, `comparisons`).

**Factor-ten test outcome.** With these certificates the factor-ten sufficient test carried from E1 (BJ lower squared > 100 times the comparator upper squared, on both sets) passes on T24 and does not pass on rotQ24 (PD-T?drift-codex-06 (c), (d)). The both-grid outcome is **INCONCLUSIVE**. The rotated lower/upper ratio below 100 does not refute factor-ten separation of the actual conditions: the bounds can be loose. There is no DEAD inference.

**Factor-ten target.** The original wording of the comparison this experiment tested is "the factor-ten comparison on **both** sets". Written out, it is a two-conjunct statement: in the formal model at degree 12, K_inf,BJ > 10 min(K_inf,alt, K_inf,pivot) on T24 **and** on rotQ24. Reading the comparator as E1's decisive one (pivot on T24, alternating on rotQ24) instead of the minimum gives the same split. The T24 conjunct is PROVED in PD-T?drift-codex-06 (c). The rotQ24 conjunct is OPEN: PD-T?drift-codex-06 gives only K_inf,BJ > 7 K_inf,alt there.

**Post-hoc thresholds.** As an explicitly post-hoc exploratory step, the weaker thresholds >800 (T24) and >7 (rotQ24) were selected after the computed endpoints were known. The inequalities at these thresholds are proved in PD-T?drift-codex-06. Their post-hoc selection is provenance, and they are not substitutes for the factor-ten test.

## Definitions

The full formal graph permits local vector-operation amplitudes from coordinate products, first-pass matrix-vector products and additions, two residual subtractions, and final component divisions. Scalar coefficient/dot/norm errors are removed only by the proved first-order polynomial-quotient argument. The local absolute radius is

    rho_hi=|(A_h b_parent)_i|+sum_l|alpha_hl b_l(i)|
           +sum_(l>=1)|sum_(r<=l)alpha_hr b_r(i)|+3|b_h(i)|.

The comparator upper is the **full graph** upper U_inf in PD-T?drift-codex-03. It is not an upper bound for only coordinate-product/division sources. The BJ lower uses its deterministic greedy node signs and target column t=86 on T24 and t=90 on rotQ24:

    S_ti=sum_h |g_th(z_i)|rho_hi,
    G_t^2=[sum_i S_ti^2-sum_l c_l^2/d_l]/d_t.

These are explicit admissible formal relative-operation error choices. No claim is made that an actual IEEE run realizes those signs.

## Assumptions

All assumptions of PD-T?drift-codex-03, in particular fixed exact parent choices, exact q0, no overflow/underflow/data perturbation, and independent formal relative error parameters. The second residual subtraction has exact zero right operand at the unperturbed baseline; the permissive model includes its relative rounding for an upper bound. Actual IEEE subtraction by zero can have zero error. This is one reason formal capacity is distinct from realized rounding.

## Status by part

Overall status: MEASURED (main statement: the exploratory exact experiment and its INCONCLUSIVE both-grid factor-ten test outcome. Claude audit-01: CONFIRMED-WITH-CORRECTIONS, corrections applied in response-01. Codex audit-02 did not accept the earlier whole-file classification of the finite inequalities (A02-M2); response-02 split them into PD-T?drift-codex-06. Codex re-audit pending).

| Claim | Status | Evidence / remaining gap |
|---|---|---|
| Exploratory exact experiment: subset maps, one-node and multinode witness search, target choice, comparison history | MEASURED | e1-scalar-cgs2.json, e1-multinode-certificates.json, e1-scalar-manifest.json; independent reruns in independent-scalar-01.json |
| Factor-ten sufficient test with these certificates, on both sets | Test outcome INCONCLUSIVE (passes on T24, not on rotQ24); this is not an epistemic status | PD-T?drift-codex-06 (c), (d) |
| Finite exact inequalities: uppers, BJ witnesses, squared ratios, >800 on T24, >7 on rotQ24 | Split into PD-T?drift-codex-06: PROVED (computer-assisted) | Not restated here |
| Factor-ten target, T24 conjunct | PROVED, under PD-T?drift-codex-06 (c) | — |
| Factor-ten target, rotQ24 conjunct, K_BJ > 10 min(K_alt, K_pivot) | OPEN | Bound conventions: for each rule X, certified bounds L_X^2 <= K_X^2 <= U_X^2 (squared full-graph capacities on rotQ24, degree 12). **Proof** needs a certificate pair L_BJ^2 > 100 U_X^2 for some comparator X in {alt, pivot}; since min(K_alt, K_pivot) <= K_X, one comparator suffices. The current alt pair has squared ratio about 62.09 < 100, so it does not suffice. **Refutation** needs U_BJ^2 <= 100 min(L_alt^2, L_pivot^2), i.e. an upper bound on BJ and lower bounds on *both* comparators. A reversal against one comparator only, U_BJ^2 <= 100 L_alt^2, refutes just the separate named-comparator statement K_BJ > 10 K_alt. It does not refute this minimum target. For example, capacities K_BJ = 9, K_alt = 1, K_pivot = 1/10 satisfy that reversal while the target holds. These are logical illustrations, not rotQ24 values (audit-03 A03-L2). |

Factor-ten target classification: the target's own statement decomposes explicitly into two conjuncts, one PROVED under a split-off ID and the other OPEN. By WORKFLOW's definition its status is therefore **PARTIAL**. It is a separately labelled claim of this file and does not change the file status, which is that of the measured experiment. Response-02 proposes that preparation register the target with this status. The developer proposes this classification; the auditor checks it.

Candidate / claim disposition: retained exploratory finite experiment; the factor-ten test outcome is INCONCLUSIVE. The failure of these bounds to certify factor ten on rotQ24 is a limitation of this certificate, not a refutation of the comparison or a failed theorem.

**Split (response-02, audit-02 A02-M2).** Response-01 kept the whole file MEASURED because the factor-ten target was INCONCLUSIVE and the >800/>7 thresholds were post hoc, and it flagged a finite PROVED split for the re-audit and AC. Audit-02 did not accept that classification. Its reasons: the finite inequalities are substantive mathematical statements that meet the computer-proof obligations; post-hoc discovery does not make them nonmathematical; and an unresolved, different target does not lower their status (WORKFLOW split-by-default rule). Response-02 therefore moved them, unchanged, to PD-T?drift-codex-06 (PROVED, computer-assisted), with the written reduction, a committed exact checker and its output, and the independent execution references. This file keeps the MEASURED experiment, its post-hoc history and the INCONCLUSIVE test outcome. Response-01's rationale is preserved in History.

## Depends on

PD-T?drift-codex-01 (exact frozen response) and -03 (proved scalar-model reduction, full-graph upper and greedy lower). The finite inequalities this experiment produced are PD-T?drift-codex-06. It does not inherit aggregate-model numerical constants from -04.

## Checks

Core code: `tracks/bivariate-lanczos/code/drift/e1_exact.py`, `e1_scalar.py`, `e1_cgs2.py`, `e1_cgs2_witness.py`, `e1_cgs2_multinode.py`, `e1_sign_check.py`, and `e1_reproduce.py`. Exact paths and hashes are in the evidence manifests; code is not third-party vendored material.

Essential evidence under `topics/padua-lanczos-drift-20261101/evidence/`:

- `e1-scalar-cgs2.json`: separate coordinate/division subset maps, full-graph comparator uppers and coherent-node lower witnesses, with norms/model stated.
- `e1-multinode-certificates.json`: compact exact greedy gains, expected node-sign gains, every node sign, commands, code/source hashes and working-artifact hashes (55328 bytes at receipt).
- `e1-posthoc-scalar-ratios.json`: exact comparisons >49 on both sets and >640000 on T24, explicitly post-hoc thresholds.
- `e1-sign-check-triangle.json` and `e1-sign-check-rotated.json`: separate explicit normal-projection arithmetic checks, PASS.
- `e1-cgs2-graph-verification.json`: exact local primitive dual-number gradient checks, developer execution, not a full normalized trajectory replay.

The finite inequalities have their own committed exact checker, `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py`, with output `evidence/response-02-e1-scalar-finite.json`; see PD-T?drift-codex-06, Checks (response-02).

The developer ran `e1_reproduce.py --set triangle` from the committed compact record and regenerated the certificate exactly, PASS. This is an additional developer calculation, not an independent agent rerun. Response-02 reran `e1_reproduce.py` for both sets and `e1_cgs2.py` for both comparators: all PASS, both uppers exactly equal. This is a developer execution; PD-T?drift-codex-06, Checks step 4. The rotated reproduction command regenerates all capacities and checks the compact gain/sign record; it has since been executed independently (independent-scalar-01.json; audit-01 reran `e1_reproduce.py --set rotated` and `--set triangle`, both PASS). Full local rotated capacity output is 3.626 MB and remains outside Git; the compact record identifies it by content hash. It is working output, not a claimed permanent archive. The public checker regenerates capacities from explicit nodes/choices and checks the essential compact certificate, so no hidden external input is needed.

## Sources

Only the explicitly restated standard relative-error model and the documented E1 predecessor baseline. No new original source or historical novelty claim.

## Proof or evidence

The proof of the finite inequalities, with its reduction through PD-T?drift-codex-03, is in PD-T?drift-codex-06, Proof or evidence (response-02). As measured evidence, this file records that every step of the experiment ran in exact rational arithmetic, with displayed decimals as summaries only. It also records that the independent full finite reproduction, which this record originally required before any upgrade, has been executed and agrees. The producer reruns in independent-scalar-01.json are identical in every exact endpoint, capacity and sign. The independent implementation run by audit-01 and audit-02 is exactly equal on T24, gives rigorous Arb enclosures on rotQ24, and reproduces all signs. The status of each part is stated under Status by part. (Response-01 update; original: "Independent full finite reproduction is required before upgrading this mathematical finite result to a completed computer-assisted proof.")

## Scope

This closes the model gap between arbitrary aggregate injections and a fully specified formal scalar implementation at first order. It does **not** close actual IEEE activation, every-reorthogonalization universality, a degree-uniform remainder, or an all-degree matching drift rate. The original E1 KHS-only verdict and its separate aggregate Urow certificate remain unchanged. All scalar follow-ups here were exploratory after E1 setup/development; no pre-registration is claimed for the coherent/multinode sign search or weaker >7/>800 thresholds.

## Open items

- Independent executed full finite reproduction: done (independent-scalar-01.json; audit-01 `ind_scalar.py`, rerun by audit-02).
- Full normalized scalar-operation dual replay of record 03:
  - degree 3: run by the audit-01 reviewer and re-executed unchanged by audit-02, agreement to 1.3e-80;
  - degree 4: response-02 developer execution, not independent, agreement to 2.4e-80 (evidence/response-02-e1-replay-n4.json);
  - degree 12: no replay.
- The OPEN rotQ24 conjunct of the factor-ten target, that is, tighter upper or lower certificates on rotQ24.
- Actual-rounding realizability.
- Explicit-family matching asymptotics.

The present INCONCLUSIVE comparison is retained without rejecting the underlying target.

## Regeneration path (E1-F6; response-01)

The compact BJ lower bounds, signs and gains are regenerated by `e1_reproduce.py` (commands above and in `code/drift/README.md`). The **comparator full-graph uppers** are not covered by that wrapper; they come from `e1_cgs2.py`, whose exact commands are recorded inside `evidence/e1-scalar-cgs2.json`, `full_graph_upper_runs[*].command`:

    PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set triangle --degree 12 --rule pivot --output <out>.json
    PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set rotated --degree 12 --rule alt --output <out>.json

(The recorded commands use `--output /workspace/padua-drift-runs/e1/cgs2-triangle-n12-pivot.json` and `.../cgs2-rotated-n12-alt.json`.) The field `upper_squared.exact` of each output is U_inf^2, that is, U_T or U_R of PD-T?drift-codex-06 (a).

The `input_sha256` field inside the `explicit_projection_check` block of `e1_reproduce.py`'s output (written by `e1_sign_check.py`) hashes a **temporary** JSON file that contains timings and paths, so it is not reproducible: the committed value and a rerun differ although the check PASSES. It should be ignored as an identity; the reproducible identities in the same output are `generator_sha256`, `certificate_sha256` and `source_record_sha256`.

## History

- 2026-11-01: Codex mathematics developer, requested gpt-6.1-sol xhigh; runtime metadata unexposed. Code developer allocation requested gpt-6.1-sol medium. Created as a separate MEASURED finite result after the analytic scalar bridge and exact exploratory follow-ups; no aggregate-model claim was relabeled as a scalar-model theorem.

## Independent execution receipt — later metadata update

The separate Astra xhigh checker regenerated both comparator full uppers, both
coherent-node witnesses and both multinode witnesses from independently
regenerated prior records; all950 capacities/signs agree exactly, and both
explicit projection checks pass. See topic checks/independent-math-01.md and
evidence/independent-scalar-01.json. It did not invoke the reproducer wrapper:
it directly executed the underlying computations and compared more intermediate
exact data. It reran the local primitive verifier, not a complete normalized
trajectory checker. This supersedes the earlier pending-execution notes;
MEASURED status and the factor-ten INCONCLUSIVE conclusion are unchanged.
Root inserted this receipt after the checker's final pinned snapshot; this is
metadata only and alters no statement, proof or numerical endpoint.

Response-01 note on the immutable snapshots (E1-F5): `evidence/e1-scalar-manifest.json` (`actual_execution`: "full independent regeneration pending at developer completion"; `status`: "independent audit pending") and `evidence/e1-scalar-cgs2.json` (`developer_checks`: "independent reruns pending") are evidence snapshots taken at developer completion and are not edited. They are superseded by the receipt above and by audit-01.

Response-02 note (A02-M2): the receipt above, the audit-01 `ind_scalar.py` run and the audit-02 reconstruction are now cited as the independent execution references of PD-T?drift-codex-06. The words "MEASURED status" in the receipt describe this file before that split.

- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F5: stale "pending independent reproduction" statements reconciled and the rationale for retaining MEASURED stated (a finite PROVED split flagged, not done); original wording: «Independent full finite reproduction is required before upgrading this mathematical finite result to a completed computer-assisted proof. Supplementary independent analytic reconstruction of theorem03 does not by itself…»
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F5: Checks and Open items updated; original wording: «it is the remaining consequential independent execution.» and «Independent executed full finite reproduction; full normalized scalar-operation dual replay;»
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F6: added the Regeneration path section (e1_cgs2.py comparator-upper commands; non-reproducible input_sha256); no earlier wording replaced.
- 2026-11-01 (Claude response-01, Sonnet 5.5): status line updated for audit-01 (status MEASURED unchanged); original wording: «Overall status: MEASURED (exact rational finite execution, with separate independent full endpoint/capacity reconstruction recorded; required Claude audit pending).»
- 2026-11-01 (Claude response-02, Opus 5.5 xhigh): A02-M2 split. Title, aliases (one added) and `Split into` changed. The finite exact inequalities moved unchanged to PD-T?drift-codex-06 (PROVED, computer-assisted). The Statement was rewritten as the measured experiment, the INCONCLUSIVE test outcome, the factor-ten target with its explicit two-conjunct decomposition (T24 PROVED in -06, rotQ24 OPEN) and the post-hoc paragraph. Original wording: title «# PD-T?drift-codex-05 — Finite formal scalar-CGS2 capacity bounds and the unresolved factor-ten comparison»; «Split into: none.»; «Exact rational developer execution gives the following first-order spectral-output capacity bounds: | Set | BJ explicit greedy lower squared | Comparator full-graph upper squared | Squared ratio lower bound | … | T24 | 1.5765963915672958e16 | pivot: 2.3984814435900658e10 | 657331.0774535049 | | rotQ24 | 8.40200144892756e11 | alternating: 1.3532944864274591e10 | 62.08553668985878 |»; «The table displays decimals; decisions use exact rational strings in the essential evidence. These bounds certify a factor greater than 10 on T24, while the factor-ten comparison on **both** sets remains **INCONCLUSIVE**. …»; «As an explicitly **post-hoc exploratory consequence**, exact comparisons show K_inf,BJ >800 K_inf,pivot on T24 and K_inf,BJ >7 K_inf,alt on rotQ24. These weaker thresholds were selected after the computed endpoints and are not substitutes for the factor-ten test.»
- 2026-11-01 (Claude response-02, Opus 5.5 xhigh): A02-M2. Status by part rewritten: per-claim rows, the PARTIAL target classification (a separately labelled claim; the file status MEASURED is unchanged) and the split paragraph replacing the response-01 rationale. Original wording: «| Full-graph endpoints and exact ratio decisions | MEASURED | Committed producer/checkers and compact exact evidence; independent endpoints/capacities/signs reproduced in independent-scalar-01.json |»; «Candidate / claim disposition: retained finite evidence, with factor-ten comparison INCONCLUSIVE. …»; «**Why the status stays MEASURED (E1-F5; decision recorded in response-01).** … Neither the INCONCLUSIVE target nor the post-hoc thresholds is a theorem-shaped statement, so the record as a whole is not a computer-assisted PROVED. … That split is **not done here**; it is flagged for the re-audit and for AC's decision. …»; status line «Overall status: MEASURED (exact rational finite execution, with separate independent full endpoint/capacity reconstruction recorded; Claude audit-01: CONFIRMED-WITH-CORRECTIONS, corrections applied in response-01, Codex re-audit pending).»
- 2026-11-01 (Claude response-02, Opus 5.5 xhigh): A02-M2. Depends on: added a pointer to -06. Checks: added the new checker and the response-02 regeneration. Proof or evidence: the finite proof now points to -06. Regeneration path: the reference to "the table above" now points to -06 (a). Original wording: «The finite reduction is PD-T?drift-codex-03: the first-order scalar graph equals the frozen recurrence with rational node/source amplitudes; absolute radii bound every allowed local source; …»; «The table and strict inequalities were executed in exact rational arithmetic, while displayed decimals are summaries only. …»; «The field `upper_squared.exact` of each output is U_inf^2 of the table above.»
- 2026-11-01 (Claude response-02, Opus 5.5 xhigh): A02-L1. Open items replay coverage corrected: degree 3 only by the audits, plus a new degree-4 developer replay. The committed audit-01 `first_principles.py` calls partC only when n == 3. The degree-3-and-4 statement came from audit-01's summary (audit-01.md and its E1 report), which stays unchanged. Original wording: «Independent executed full finite reproduction (done: independent-scalar-01.json, audit-01); full normalized scalar-operation dual replay (done at degrees 3 and 4 by the audit-01 reviewer, agreement to 1e-80; no degree-12 replay); tighter upper/lower certificates if the factor-ten full-model question matters; …»
- 2026-11-01 (Claude response-03, Opus 5.5 high): A03-L2. The rotQ24-conjunct row now states the minimum target explicitly, with its bound conventions, and the correct proof and refutation conditions. The alt-only reversal is scoped to the named-comparator target K_BJ > 10 K_alt. The PARTIAL classification, MEASURED file status and INCONCLUSIVE test outcome are unchanged. Original wording: «| Factor-ten target, rotQ24 conjunct | OPEN | Needs either a certificate pair with squared ratio >100 on rotQ24, or a certified reversal U_BJ^2 < 100 L_alt^2 |».
