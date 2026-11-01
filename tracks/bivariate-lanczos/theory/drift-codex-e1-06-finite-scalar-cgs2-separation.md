# PD-T?drift-codex-06 — Certified finite BJ/comparator separation of the formal scalar-CGS2 capacity on T24 and rotQ24 at degree twelve

ID kind: PD-T.
Aliases: finite formal scalar-CGS2 separation; full-graph comparator upper versus explicit BJ node-sign witness; K_inf,BJ > 800 K_inf,pivot on T24 and K_inf,BJ > 7 K_inf,alt on rotQ24; post-hoc scalar-capacity thresholds (computer-assisted finite proof).
Split from: PD-T?drift-codex-05 — its exact finite bounds table (full-graph comparator uppers, explicit multinode BJ lower witnesses, squared ratio lower bounds about 657331.08 and 62.0855) and its post-hoc consequences K_inf,BJ > 800 K_inf,pivot on T24 and K_inf,BJ > 7 K_inf,alt on rotQ24, which that MEASURED file carried until response-02 (audit-02 A02-M2 / E1-R1). The measured exploratory experiment, its post-hoc history and the INCONCLUSIVE both-grid factor-ten test outcome stay in PD-T?drift-codex-05, which also keeps the factor-ten target.
Split into: none.

## Statement

**Model.** Exactly the formal scalar-CGS2 model of PD-T?drift-codex-03: the fixed-choice, left-to-right dense-matrix-vector classical Gram-Schmidt-twice implementation of its steps 1–5, with exact q_0, in which every scalar operation with exact value w is replaced by w(1+epsilon delta_o) with independent formal parameters |delta_o|<=1 (an **l-infinity** source condition). Let Phi(delta)=R_s V D_s^(-1/2) be the first-order normal-quotient map of record 03, so that theta_s(epsilon)=|epsilon| ||Phi(delta)||_2+O(epsilon^2) for each fixed delta, with **spectral** output norm, and let

    K_inf = sup_(max_o |delta_o| <= 1) ||Phi(delta)||_2

for the stated node set, degree and parent rule. Write K_rule(set).

**Data.** As in PD-T?drift-codex-04: T24={(i/12-1,j/12-1): i,j>=0, i+j<=24} (M=325) and rotQ24={((3x-4y)/5,(4x+3y)/5): x=i/12-1, y=j/12-1, 0<=i,j<=24} (M=625); Euclidean (uniform-weight) node inner product; graded monomials x^(t-j)y^j with j increasing; degree s=12, N_12=91 columns and all 90 source columns h=1,...,90. Rules: BJ (X iff j=0), alternating (X iff 2j<t) and exact pivot (larger d_k/||A_k b_parent||^2, ties X), choices frozen at the exact data. T24 pivot has no tie at any degree 2..12 (smallest relative margin 0.008426, column (8,5)); its frozen sequence is listed in `topics/padua-lanczos-drift-20261101/checks/audit-02/E1.md`. rotQ24 pivot is not used.

Let U_T, U_R, G_T and G_R be the exact rationals recorded in `evidence/e1-scalar-cgs2.json` (`full_graph_upper_runs[*].upper_squared.exact`, T24/pivot and rotQ24/alt) and `evidence/e1-multinode-certificates.json` (`witnesses[*].explicit_greedy_sign_lower_squared.exact`, T24 and rotQ24 BJ). Then:

**(a) Full-graph comparator uppers.**

    K_pivot(T24)^2  <= U_T = 2.39848144359...e10 < 24000000000,
    K_alt(rotQ24)^2 <= U_R = 1.35329448642...e10 < 13600000000.

**(b) Explicit BJ lower witnesses.** For the node signs s in {+1,-1}^325 (T24) and {+1,-1}^625 (rotQ24) recorded in `e1-multinode-certificates.json`, and target output columns t=86 (monomial (12,8), x^4y^8) on T24 and t=90 ((12,12), y^12) on rotQ24, the admissible formal error vector delta*_hio=s_i sign(g_th(z_i)m_hio) for h<=t, and delta*=0 otherwise, has first-order output whose column t has squared norm exactly G_T (respectively G_R), the value G_t^2 of the Definitions. Hence

    K_BJ(T24)^2    >= G_T = 1.57659639156...e16 > 15700000000000000,
    K_BJ(rotQ24)^2 >= G_R = 8.40200144892...e11 > 840000000000.

**(c) Ratio consequences.**

    T24:    K_BJ(T24)^2 >= (G_T/U_T) K_pivot(T24)^2,  G_T/U_T = 657331.0774535... in (657331, 657332),
            hence K_BJ(T24) > 800 K_pivot(T24),
            and in particular K_BJ(T24) > 10 min(K_alt(T24), K_pivot(T24));
    rotQ24: K_BJ(rotQ24)^2 >= (G_R/U_R) K_alt(rotQ24)^2,  G_R/U_R = 62.0855366898... in (62, 63),
            hence K_BJ(rotQ24) > 7 K_alt(rotQ24) >= 7 min(K_alt(rotQ24), K_pivot(rotQ24)).

The integer forms follow from 15700000000000000 > 800^2 * 24000000000 and 840000000000 > 7^2 * 13600000000; no division by a condition number is needed. For display only: sqrt(G_T/U_T) lies in (810, 811) and sqrt(G_R/U_R) in (7.87, 7.88).

**(d) Certificate limitation (exact fact about these endpoints, not about K).** G_R/U_R < 100. Hence (a)–(b) do not establish K_BJ(rotQ24) > 10 K_alt(rotQ24). They also do not establish its negation: no upper bound on K_BJ(rotQ24) and no lower bound on K_alt(rotQ24) enters. Whether the factor-ten comparison holds on rotQ24 is not decided here.

**Provenance (post hoc; does not qualify the status).** The thresholds 800 and 7, and the displayed integer thresholds, were chosen after the endpoints were known. The comparators (E1's decisive comparators: pivot on T24, alternating on rotQ24), the target columns (selected from earlier one-node witnesses) and the greedy node order were chosen during exploratory, post-E1 work; no pre-registration is claimed. None of these choices enters the validity of (a)–(d): (a) holds for every admissible delta, and (b) holds for every sign vector in {+1,-1}^M, however it was found.

## Definitions

Use record 03's local amplitudes m_hio, absolute radii rho_hi=sum_o|m_hio| (coordinate product, first-pass products and partial sums, two subtractions and the component division), frozen responses g_kh, normal projector R_s, and

    U_inf^2 = sum_(i,k) [sum_(h<=k) |g_kh(z_i)| rho_hi]^2 / d_k,
    S_ti    = sum_(h<=t) |g_th(z_i)| rho_hi,
    c_l     = sum_i b_l(i) S_ti s_i,
    G_t^2   = [sum_i S_ti^2 - sum_l c_l^2/d_l] / d_t,

with sign(0)=0. The recorded signs come from the deterministic greedy rule of record 03 (node order 0..M-1, sign(-sum_l b_l(i)c_l/d_l) with +1 at a tie). That rule only guarantees G_t^2 >= E_t^2=sum_i R_s,ii S_ti^2/d_t; it is not needed for (b).

## Assumptions

All assumptions of PD-T?drift-codex-03: exact positive pivots, injectivity through degree 12, choices fixed under perturbation, no overflow, underflow or data perturbation, independent formal relative operation errors, exact q_0. Injectivity holds for both grids (they are injective through degree 24; see PD-T?drift-codex-04 Assumptions). The formal model also assigns a relative error to the second residual subtraction, whose right operand is exactly zero at the baseline; it is included in the upper bound (permissive). Actual IEEE arithmetic need not realize such errors.

## Status by part

Overall status: PROVED (finite exact computer-assisted statement in the formal model: written reduction to finite exact computations via PD-T?drift-codex-03, exact rational producer outputs in committed essential evidence, a committed exact checker with committed output, and independent executions referenced under Checks. Created by split from PD-T?drift-codex-05 in Claude response-02 for audit-02 A02-M2; Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) T24/pivot and rotQ24/alternating full-graph uppers | PROVED | Exact producer output in e1-scalar-cgs2.json; independent reruns identical (independent-scalar-01.json); independent implementation exact on T24 and Arb-enclosed on rotQ24 (audit-01 ind_scalar.py; audit-02 rerun) |
| (b) Explicit BJ node-sign lower witnesses | PROVED | Exact producer output and signs in e1-multinode-certificates.json; separate explicit-projection checks; independent reruns identical; independent implementation reproduces gains and all 950 signs |
| (c) Squared ratio bounds and the >800 (T24) and >7 (rotQ24) consequences, T24 factor ten | PROVED | Exact Fraction comparisons in the committed checker; independent exact/Arb decisions agree |
| (d) G_R/U_R < 100 (certificate limitation) | PROVED (minor routine exact fact about the endpoints; it is not a statement about K) | Committed checker; the audit-02 rotQ24 ratio enclosure alone also lies in (49, 100) |

Candidate / claim disposition: retained finite result. It contains no target statement. The both-grid factor-ten target, its INCONCLUSIVE test outcome and the measured experiment are in PD-T?drift-codex-05.

## Depends on

PD-T?drift-codex-03 (PROVED, analytic): the first-order normal-quotient map of the declared scalar graph, K_inf<=U_inf, and the exact attained target-column gain of any admissible node-sign pattern. PD-T?drift-codex-01: exact frozen recurrence, responses g, projector R_s and the graph-angle argument. The grids and injectivity are those of PD-T?drift-codex-04, whose aggregate-model constants are **not** used. No dependence on the measured interpretation in PD-T?drift-codex-05.

## Checks

**Producers** (exact rationals, CPython + python-flint fmpq), unchanged since the scientific snapshot b09e1db and pinned in the evidence: `tracks/bivariate-lanczos/code/drift/e1_exact.py` (`19ce7b77…`, exact basis, recurrence, frozen choices), `e1_cgs2.py` (`426630eb…`, rho and U_inf^2), `e1_cgs2_witness.py` (`06dff7f4…`, one-node witnesses, used only to select t), `e1_cgs2_multinode.py` (`32b9e827…`, S_t, greedy signs, G and E), `e1_sign_check.py` (`0a3717f7…`, final norm by explicit normal projection, a separate formula), `e1_reproduce.py` (`4381f336…`, regeneration wrapper). The `e1_cgs2.py` commands are recorded in `e1-scalar-cgs2.json`, `full_graph_upper_runs[*].command`, and in PD-T?drift-codex-05, Regeneration path.

**Essential committed evidence** (`topics/padua-lanczos-drift-20261101/evidence/`): `e1-scalar-cgs2.json` (444008 bytes, SHA-256 `e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8`; exact U_T, U_R), `e1-multinode-certificates.json` (55328 bytes, `fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0`; exact G, E, node signs, targets, exact ratios), `e1-sign-check-triangle.json`, `e1-sign-check-rotated.json` (explicit projection PASS), `e1-posthoc-scalar-ratios.json` (post-hoc decision booleans), and the new checker output `response-02-e1-scalar-finite.json`.

**Checker** (new, response-02): `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py`, SHA-256 recorded in its output. It verifies the input pins and, in `fractions.Fraction` with `sys.set_int_max_str_digits(0)` (no float in a decision), every inequality in (a)–(d): U>0, G>=E>0, signs in {+1,-1} with counts 325/625, targets 86/90, the four displayed thresholds and both integer chains, G/U>800^2 and >7^2, the factor-ten flag (true on T24, false on rotQ24), G_R/U_R<100, the integer and square-root brackets, and exact equality with the committed comparisons and post-hoc booleans. It also checks exact agreement with the reused independent evidence below. It does not recompute S_t; regeneration is the separate step 4 below. Since response-03 (audit-03 A03-L1), `--regenerated DIR` requires all four outputs (two comparator uppers, two reproductions). A missing directory or file fails the check and gives exit status 1; the mode without `--regenerated` is unchanged. Negative and positive cases, with a fresh developer regeneration: `response-03-e1-regeneration-check.json`. Command:

    PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py --regenerated /workspace/padua-drift-runs/response-02/E1 --regeneration-notes /workspace/padua-drift-runs/response-02/E1/regeneration-notes.json --output topics/padua-lanczos-drift-20261101/evidence/response-02-e1-scalar-finite.json

Result: all 65 checks PASS (31 T24, 34 rotQ24), plus the regeneration comparison; CPython 3.13.18.

**Independent executions — reused, not re-executed in response-02.**

1. `evidence/independent-scalar-01.json` (186681 bytes, SHA-256 `2d06b3b4e04956f9c9e2f4127c3937543dc92ee071de2926589d0a40c9bf6a10`): Codex supplementary checker (requested gpt-6-astra xhigh), rules `6920ba63`, generated 2026-11-01T11:32:54Z. It separately executed `e1_cgs2.py` for both comparators and `e1_cgs2_witness.py`, `e1_cgs2_multinode.py` and `e1_sign_check.py` on both sets, with source pins preserved in its `inputs` list (among them e1_exact `19ce7b77…`, e1_cgs2 `426630eb…`, witness `06dff7f4…`, multinode `32b9e827…`, sign check `0a3717f7…`, reproducer `4381f336…`, its own receipt checker `check_independent_scalar.py` `b711a103…`, e1-scalar-cgs2 `e215556a…`, multinode certificates `fae9c874…`, and record 03 at `38a58ef2…`). All exact uppers, gains, capacities and 950 node signs are IDENTICAL to the developer records, and both projection checks PASS. These are independent executions of the inspected producers, not an independent implementation.
2. Claude audit-01 E1 reviewer, `checks/audit-01/scripts/E1/ind_scalar.py` (`9da84661…`, with `ind_basis.py` `c3b210eb…` and `ind_aggregate.py` `c6117f49…`): an independent implementation importing no producer code (canonical monomial-Gram LDL basis, per-node inverse of the frozen-recurrence matrix, own rho, U_inf, S_t and greedy signs). T24 exact equality of U, G and E; rotQ24 512-bit Arb enclosures containing them; its own greedy signs equal all committed signs with 0 ambiguous decisions. Report: `checks/audit-01/E1-records-01-05.md`, item 6 (CPython 3.13.18, python-flint 0.9.0); the raw outputs are not committed.
3. Codex audit-02 E1 reconstruction: `checks/audit-02/E1/reaudit.py` (`36fbd70d…`) `scalar --set triangle --mode exact` and `scalar --set rotated --mode arb`, fresh calls of the unchanged audit-01 `ind_scalar.py` (CPython 3.12.14, python-flint 0.9.0, Arb 512 bits). Compact outputs: `evidence/audit-02-e1-checks.json` (SHA-256 `7bb3e3b566d7d25d369ee812c007b690b46bbdcc54b55ceb54f18fec9390d0ee`), `checks.scalar-triangle` and `checks.scalar-rotated`. Exact T24 equality, rotQ24 enclosures containing every committed rational, ratio enclosure [62.0855366898587744… ± 5.6e-147] in (49, 100), 325+625 signs equal with 0 ambiguous decisions.

**New execution in response-02 (developer, Claude Opus 5.5; not independent).**

4. 2026-11-01, 16:42:20–16:49:50 UTC, CPython 3.13.18, python-flint 0.9.0, outputs under `/workspace/padua-drift-runs/response-02/E1/` (regenerable working files, not committed): `e1_reproduce.py --set triangle` (PASS, 3.0 s wall), `e1_cgs2.py --set triangle --degree 12 --rule pivot` (3.6 s), `e1_reproduce.py --set rotated` (PASS, 174.8 s wall, run concurrently with another job), and `e1_cgs2.py --set rotated --degree 12 --rule alt` (252.7 s). Both regenerated uppers equal U_T and U_R exactly. Both reproductions regenerated all target capacities from the explicit nodes and choices, matched the committed gains and signs, and passed the explicit projection check. Output hashes, commands and times are in `response-02-e1-scalar-finite.json`, `new_regeneration`.

**Trusted dependencies.** CPython (`fractions`, integers), python-flint (fmpq exact arithmetic in the producers; Arb ball arithmetic in the audit reconstructions). For rotQ24 the exact rationals come from the producer (reproduced identically by run 1). The independent implementation (runs 2–3) supplies rigorous enclosures, and its enclosure alone also gives G_R/U_R in (49, 100).

## Sources

Only PD-T?drift-codex-03's explicitly restated standard formal relative-error model. Context predecessors, not dependencies: PD-T?drift-codex-04 (same grids, aggregate Hilbert source model), PD-T041 (raw recurrence-entry growth), PD-T042/043 (coefficient-channel Gram outputs). No literature or historical novelty claim.

## Proof or evidence

*Upper (a).* By PD-T?drift-codex-03, f_h(i)=sum_o m_hio delta_hio, so |f_h(i)|<=rho_hi whenever max|delta|<=1. Each entry of V_k=sum_(h<=k) diag(g_kh)f_h is bounded by sum_h|g_kh(z_i)|rho_hi. Projection by R_s does not increase the Frobenius norm, and the spectral norm is at most the Frobenius norm. Hence ||Phi(delta)||_2^2 <= U_inf^2 for every admissible delta, and K_inf^2 <= U_inf^2. For T24/pivot and rotQ24/alternating at degree 12, U_inf^2 is the exact rational U_T or U_R, computed by `e1_cgs2.py` from the exact basis, recurrence coefficients and responses.

*Lower (b).* Fix t and any s in {+1,-1}^M. Put delta*_hio=s_i sign(g_th(z_i)m_hio) for h<=t and every local operation o, and delta*=0 otherwise. This is admissible. Since m sign(g m)=sign(g)|m|, f_h(i)=s_i sign(g_th(z_i))rho_hi, and therefore g_th(z_i)f_h(i)=s_i|g_th(z_i)|rho_hi, also when g_th(z_i)=0. Summing over h<=t gives V_t=v with v_i=s_iS_ti. Column t of Phi(delta*) is R_s v/sqrt(d_t). Because the b_l are exactly orthogonal, R_s=I-sum_l b_l b_l^T/d_l, so ||R_s v||^2=||v||^2-sum_l c_l^2/d_l with c_l=b_l^T v and ||v||^2=sum_i S_ti^2. Thus the column has squared norm G_t^2. The spectral norm of a matrix is at least the norm of any column, so K_inf^2 >= G_t^2. This uses only s in {+1,-1}^M, not the greedy property. `e1_cgs2_multinode.py` computes S_t, s, c_l and G_t^2 exactly; `e1_sign_check.py` recomputes the final squared norm by an explicit normal projection of v and checks equality, and checks G>=E.

*Ratios (c), (d).* From (a) and (b), K_BJ^2 >= G = (G/U) U >= (G/U) K_cmp^2 for the relevant comparator. The checker compares exact rationals: G_T>15700000000000000>800^2*24000000000>800^2 U_T, and G_R>840000000000>7^2*13600000000>7^2 U_R. Hence K_BJ(T24)^2 > 800^2 U_T >= 800^2 K_pivot(T24)^2 and K_BJ(rotQ24)^2 > 7^2 U_R >= 7^2 K_alt(rotQ24)^2, strictly, with no division by a condition number. Directly, G_T/U_T>640000 and >100, and 49<G_R/U_R<100. Because min(K_alt,K_pivot)<=K_cmp, the T24 factor-ten and both min-forms in (c) follow. Statement (d) is the exact inequality G_R/U_R<100 together with the observation that a bound from below on a ratio cannot refute a larger value.

*Finite computation identity.* Exact orthogonality B^TB=D and the recurrence identity were checked exactly at degree 12 for T24 BJ/pivot and rotQ24 BJ/alt in `evidence/response-01-e1-checks.json` (it imports the producer) and independently by the audit-01 reviewer with a canonical-LDL basis. The independently implemented `ind_scalar.py` reproduces U, G and E (exact on T24, rigorous enclosures on rotQ24) and the signs. Together with the reruns this discharges WORKFLOW's computer-proof obligations for this finite statement: proved reduction, exact arithmetic, committed code and evidence, and an independent rerun.

## Scope

The quantities are formal **capacities**: bounds on the supremum of the first-order span-normal output over formal relative operation errors in one declared implementation. This record gives

- no IEEE lower bound: an actual IEEE run need not realize delta* (for example, subtraction of an exact zero, or an exactly representable result, is exact), so nothing follows about an actual implementation, actual drift or a deterministic floating-point output;
- no finite-epsilon remainder estimate and no exact value of K_inf;
- no other node set, degree, rule, operation order or BLAS implementation;
- no all-degree, asymptotic or explicit-family rate (E2 remains OPEN).

Its source domain (l-infinity over scalar operations) differs from PD-T?drift-codex-04's aggregate Hilbert source norm; the two sets of constants are not interchangeable.

## Open items

The factor-ten comparison on rotQ24 in this model (the OPEN rotQ24 conjunct of PD-T?drift-codex-05's target); tighter lower certificates (other targets or sign patterns) or upper certificates; actual-rounding realizability; explicit-family all-degree rates (E2, OPEN).

## History

- 2026-11-01 (Claude response-02, Opus 5.5 xhigh): created by splitting from PD-T?drift-codex-05 for audit-02 A02-M2 / E1-R1 (WORKFLOW split-by-default rule: substantive finite PROVED claims get their own file and PROVED status). The endpoints, model, comparators, targets, signs, thresholds and essential evidence are unchanged. New in this file are the written reduction, the integer-threshold chains, the exact checker `e1_scalar_finite_check.py` with output `response-02-e1-scalar-finite.json`, and a developer regeneration, step 4 under Checks. Wording moved from record 05: «These bounds certify a factor greater than 10 on T24, while the factor-ten comparison on **both** sets remains **INCONCLUSIVE**. …» and «As an explicitly **post-hoc exploratory consequence**, exact comparisons show K_inf,BJ >800 K_inf,pivot on T24 and K_inf,BJ >7 K_inf,alt on rotQ24. …». The post-hoc provenance is preserved above.
- 2026-11-01 (Claude response-03, Opus 5.5 high): A03-L1. The checker's `--regenerated` mode now fails when any required output is absent, with explicit `missing_required` and exit status 1. The four-case demonstration and the fresh 2026-11-01 regeneration (18:40–18:45 UTC) are in `response-03-e1-regeneration-check.json`. The theorem, reduction, evidence pins and response-02 receipt are unchanged. The response-02 receipt was produced by the earlier checker, whose `--regenerated` branch tolerated missing files; its recorded file entries show all four outputs present at that time.
