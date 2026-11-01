# PD-T?drift-codex-05 — Finite formal scalar-CGS2 capacity bounds and the unresolved factor-ten comparison

ID kind: PD-T.
Aliases: scalar operation sensitivity follow-up; multinode greedy rounding witness; formal relative-error capacity.
Split from: E2's scalar-rounding explanation route. Explicit-family matching rates and actual IEEE activation remain OPEN.
Split into: none.

## Statement

Use exactly the fixed-choice, left-to-right dense-matrix-vector scalar CGS2 implementation and the independent relative-operation model of PD-T?drift-codex-03. Every local scalar parameter has absolute value at most one; thus K_inf is an **l-infinity source** condition, unlike the Hilbert aggregate condition in PD-T?drift-codex-04. Nodes and choices are the same T24/rotQ24 at degree 12, with all 90 source columns available.

Exact rational developer execution gives the following first-order spectral-output capacity bounds:

| Set | BJ explicit greedy lower squared | Comparator full-graph upper squared | Squared ratio lower bound |
|---|---:|---:|---:|
| T24 | 1.5765963915672958e16 | pivot: 2.3984814435900658e10 | 657331.0774535049 |
| rotQ24 | 8.40200144892756e11 | alternating: 1.3532944864274591e10 | 62.08553668985878 |

The table displays decimals; decisions use exact rational strings in the essential evidence. These bounds certify a factor greater than 10 on T24, while the factor-ten comparison on **both** sets remains **INCONCLUSIVE**. The rotated lower/upper ratio below 100 does not refute factor-ten separation of the actual conditions: the bounds can be loose. There is no DEAD inference.

As an explicitly **post-hoc exploratory consequence**, exact comparisons show K_inf,BJ >800 K_inf,pivot on T24 and K_inf,BJ >7 K_inf,alt on rotQ24. These weaker thresholds were selected after the computed endpoints and are not substitutes for the factor-ten test.

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

Overall status: MEASURED (exact rational finite execution, with separate independent full endpoint/capacity reconstruction recorded; required Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Full-graph endpoints and exact ratio decisions | MEASURED | Committed producer/checkers and compact exact evidence; independent endpoints/capacities/signs reproduced in independent-scalar-01.json |

Candidate / claim disposition: retained finite evidence, with factor-ten comparison INCONCLUSIVE. The failure of these bounds to certify factor ten on rotQ24 is a limitation of this certificate, not a refutation of the comparison or a failed theorem.

## Depends on

PD-T?drift-codex-01 (exact frozen response) and -03 (proved scalar-model reduction, full-graph upper and greedy lower). It does not inherit aggregate-model numerical constants from -04.

## Checks

Core code: `tracks/bivariate-lanczos/code/drift/e1_exact.py`, `e1_scalar.py`, `e1_cgs2.py`, `e1_cgs2_witness.py`, `e1_cgs2_multinode.py`, `e1_sign_check.py`, and `e1_reproduce.py`. Exact paths and hashes are in the evidence manifests; code is not third-party vendored material.

Essential evidence under `topics/padua-lanczos-drift-20261101/evidence/`:

- `e1-scalar-cgs2.json`: separate coordinate/division subset maps, full-graph comparator uppers and coherent-node lower witnesses, with norms/model stated.
- `e1-multinode-certificates.json`: compact exact greedy gains, expected node-sign gains, every node sign, commands, code/source hashes and working-artifact hashes (55328 bytes at receipt).
- `e1-posthoc-scalar-ratios.json`: exact comparisons >49 on both sets and >640000 on T24, explicitly post-hoc thresholds.
- `e1-sign-check-triangle.json` and `e1-sign-check-rotated.json`: separate explicit normal-projection arithmetic checks, PASS.
- `e1-cgs2-graph-verification.json`: exact local primitive dual-number gradient checks, developer execution, not a full normalized trajectory replay.

The developer ran `e1_reproduce.py --set triangle` from the committed compact record and regenerated the certificate exactly, PASS. This is an additional developer calculation, not an independent agent rerun. The rotated reproduction command regenerates all capacities and checks the compact gain/sign record; it is the remaining consequential independent execution. Full local rotated capacity output is 3.626 MB and remains outside Git; the compact record identifies it by content hash. It is working output, not a claimed permanent archive. The public checker regenerates capacities from explicit nodes/choices and checks the essential compact certificate, so no hidden external input is needed.

## Sources

Only the explicitly restated standard relative-error model and the documented E1 predecessor baseline. No new original source or historical novelty claim.

## Proof or evidence

The finite reduction is PD-T?drift-codex-03: the first-order scalar graph equals the frozen recurrence with rational node/source amplitudes; absolute radii bound every allowed local source; the full comparator upper follows by absolute sums and Frobenius domination. The chosen BJ target signs give a realizable formal-error vector; exact projection evaluates its target-column norm and hence lower-bounds the spectral-output capacity. Greedy signs make all incremental off-diagonal projector contributions nonnegative, with the direct projection checker separately verifying the attained final quadratic form.

The table and strict inequalities were executed in exact rational arithmetic, while displayed decimals are summaries only. Independent full finite reproduction is required before upgrading this mathematical finite result to a completed computer-assisted proof. Supplementary independent analytic reconstruction of theorem03 does not by itself verify this finite computation.

## Scope

This closes the model gap between arbitrary aggregate injections and a fully specified formal scalar implementation at first order. It does **not** close actual IEEE activation, every-reorthogonalization universality, a degree-uniform remainder, or an all-degree matching drift rate. The original E1 KHS-only verdict and its separate aggregate Urow certificate remain unchanged. All scalar follow-ups here were exploratory after E1 setup/development; no pre-registration is claimed for the coherent/multinode sign search or weaker >7/>800 thresholds.

## Open items

Independent executed full finite reproduction; full normalized scalar-operation dual replay; tighter upper/lower certificates if the factor-ten full-model question matters; actual-rounding realizability; explicit-family matching asymptotics. The present INCONCLUSIVE comparison is retained without rejecting the underlying target.

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
