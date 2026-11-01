# PD-T139 — Certified finite aggregate span-sensitivity separation on a triangle and rational rotated square

Provisional alias: `PD-T?drift-codex-04`. Final ID assigned at PR preparation, 2026-11-01 (handoff 11, after Codex audit-04 acceptance).

ID kind: PD-T.
Aliases: E1 finite comparison; rational quotient certificate; BJ versus pivot/alternating at degree twelve.
Split from: E1 explanatory target. An all-degree family theorem and a scalar-rounding activation theorem remain OPEN.
Split into: none.

## Statement

Use the **all-source aggregate residual norm** and spectral-output condition kappa_12 from PD-T136/02. Uniform weights and graded monomials x^(t-j)y^j, j increasing, are fixed. Let

    T24={(i/12-1,j/12-1):i,j>=0,i+j<=24},
    rotQ24={((3x-4y)/5,(4x+3y)/5):x=i/12-1,y=j/12-1,0<=i,j<=24}.

The choices are BJ (X at j=0, Y otherwise), alternating (X iff 2j<t), and exact pivot (choose larger d_k/||A b_parent||^2, ties X). The pivot choices are frozen at these exact data. Every source h=1,...,90 is included at degree 12 (N_12=91).

**Pivot-tie disclosure (E1-F1).** The producer breaks pivot ties to X silently. Exact detection (`evidence/response-01-e1-checks.json`) shows: **T24 pivot has no tie** at any degree 2..12 (smallest relative margin |sigma_X-sigma_Y|/(sigma_X+sigma_Y) = 0.008426, at column (8,5)); **rotQ24 has an exact tie at column (2,1) at every degree 2..12**, because both candidates give the same vector x∘y: the node set is invariant under rotation by 90 degrees, so b_(1,0)=x and b_(1,1)=y exactly. All rotQ24 pivot values in the 88-case sweep, in `e1-summary.md` (an immutable evidence snapshot that carries no such disclosure) and in `checks/independent-math-01.md` are therefore **X-tie-broken frozen sequences**; the adaptive pivot rule has no derivative at this data, only each frozen tie-break does. Resolving the tie to Y changes only column (2,1); at degree 12 Knode^2 is unchanged, KHS^2 rises by 12.4% and Urow^2 by 3.8% (exact rationals in the response JSON). No statement in this record uses the rotQ24 pivot: the rotQ24 decisive comparator is alternating, and the T24 decisive comparator, pivot, has no tie, so there the frozen and the adaptive derivative coincide locally.

The exact rational bounds certify

    T24:    kappa_BJ^2 > 200000000000000,
            kappa_pivot^2 < 170000000,
            kappa_BJ > 1000 kappa_pivot;

    rotQ24: kappa_BJ^2 > 88000000000,
            kappa_alt^2 < 642000000,
            kappa_BJ > 11 kappa_alt.

In particular BJ exceeds the better of alternating and pivot by a factor greater than 10 on each set. This is a finite, worst-case, aggregate-residual **capacity** comparison. It asserts neither actual floating-point drift nor an asymptotic rate.

## Definitions

Use Knode as a lower bound, KHS and Urow as upper bounds, with U=min(KHS,Urow), exactly as in PD-T137. The final-stage raw endpoints (rounded here only for readability) are:

| Set/rule | Knode squared | U squared |
|---|---:|---:|
| T24/BJ | 2.0493879359e14 | 1.0859728745e16 |
| T24/pivot | 1.2479403793e7 | 1.6145977113e8 |
| rotQ24/BJ | 8.8170667576e10 | 1.2841166021e12 |
| rotQ24/alternating | 3.9414606242e7 | 6.4187254242e8 |

The mathematical decisions use rational strings in the essential evidence, not these decimals. The ratios of the squared lower/upper endpoints are about 1269287.03 and 137.36476. Integer thresholds in the Statement are weaker convenient exact consequences.

## Assumptions

Exactly the injection model and source scaling of PD-T136/02; rational nodes above; fixed choices. These grids are injective for degree 12. For T24, the principal triangular lattice is injective through degree 24 (iterated row-factor argument); for Q24, a polynomial of degree at most 24 vanishing on all 25x25 grid nodes vanishes identically by univariate root counting in each coordinate; an invertible linear substitution preserves that property.

## Status by part

Overall status: PROVED (finite exact computer-assisted statement; written reduction, committed essential checker/evidence and independent executed rerun present; Claude audit-01: CONFIRMED-WITH-CORRECTIONS, corrections applied in response-01, Codex re-audit pending). The statement, the thresholds and the status are unchanged by response-01.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| T24 degree-12 inequalities | PROVED | Exact producer/checker plus independent exact full-source execution and identical rational endpoints |
| rotQ24 degree-12 inequalities | PROVED | Same independently executed certificate for BJ and alternating decisive cases |

Candidate / claim disposition: retained finite property certificate. The **original KHS-only frozen test is INCONCLUSIVE**; this result uses the later analytically derived Urow upper certificate and is reported as a separate strengthened certificate. The intended property survives that strengthened test; it must not be described as the original certificate passing.

**Freeze provenance (E1-F4).** The earliest committed freeze (6920ba6) already contains the Urow field under `frozen_before_run: true`, while its own text says it was "Added after initial n2 restricted-source run"; no KHS-only pre-run snapshot is committed, so Urow is not a pre-run field. The `dead` field was edited in place at c89eb6a (final-degree scope added) after T24 full n=12 for all four rules and the standalone rotated alt had been inspected. The original any-degree KHS-based DEAD rule never fires at degrees 2..12 on either set, so the original test and every claim here are unaffected; the same clause with the sharpened upper min(KHS,Urow) would fire at T24 degrees 2-4 and rotQ24 degrees 2-6 (response JSON, check d), which is why the final-degree scope matters for the tightened certificate. Per-field reconciliation: `directions/E1.md`, section "Response-01 annotations".

## Depends on

PD-T136 (normal derivative reduction) and -02 (rational bounds). No dependence on a measured asymptotic fit, an implicit-section completion, or a claimed equivalence with upstream V+A code.

## Checks

Producer: `tracks/bivariate-lanczos/code/drift/e1_exact.py` (CPython and python-flint exact rational arithmetic). Runner: `e1_batch.py`. Essential committed evidence: `topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json` (88 exact records, all sources), `e1-exact-check.json`, `e1-derivative-verification.json`, `e1-freeze.json`, and `e1-manifest.json` with commands and hashes. Checker: `e1_check.py`; separate developer derivative reconstruction: `e1_verify.py`. Those paths are repository-relative here to specify reproducible commands.

The derivative verifier checked 360 rational-vector equalities and 800 exact basis pairings at degree 3 across both sets/all rules. The evidence checker verified all 88 source counts, projector traces and rational square-root intervals. The projector-trace quantity is a **consistency identity**, not a verification: sum_i(1-sum_k b_k(i)^2/d_k) = M-N holds for any nonzero columns once d_k := ||b_k||^2, so it neither tests orthogonality nor the projector property (E1-F2). The verification of the orthogonal basis is the exact check B^T B = D (all off-diagonal Gram entries zero, diagonal equal to d_k) together with the exact recurrence identity b_k = A_k b_parent - sum_l alpha_kl b_l at every node, at degree 12 for T24 bj, T24 pivot, rotQ24 bj and rotQ24 alt (plus rotQ24 pivot and T24 alt): all PASS in `evidence/response-01-e1-checks.json`, produced by `tracks/bivariate-lanczos/code/drift/e1_response_checks.py`. That checker imports the committed producer, so it checks the committed construction and is not an independent reimplementation; the independent exact B^T B = D check at degree 12 on both grids is the audit-01 reviewer's. These are developer executions; they do not replace the required independently executed check.

The mathematics developer separately parsed the final exact rational endpoints using CPython `fractions.Fraction`, enabled large-integer parsing with `sys.set_int_max_str_digits(100000)`, and checked each of the six strict inequalities in the Statement by rational comparison. All returned True. This checks arithmetic on the evidence, not an independent reconstruction of the producer. Response-01 (E1-F3): the six strict inequalities, their integer-threshold chain (200000000000000 > 1000^2*170000000 and 88000000000 > 11^2*642000000) and the factor-100 criterion are now also checked by a committed checker, `e1_response_checks.py`, from the committed rationals of `e1-full-sweep.json` (Fraction arithmetic, no floats in any decision), with output `evidence/response-01-e1-checks.json` (all PASS; code sha256 recorded there). The rotQ24 margin is tight: U_alt^2 < 642000000 holds with relative headroom 1.99e-4 (0.02%), exactly. An initial parse attempt hit Python's default integer-string length limit on the rotated rational; the explicit larger limit resolved it without changing any data.

Independent execution: **completed** by the supplementary Codex mathematical checker. Essential independent evidence is `topics/padua-lanczos-drift-20261101/evidence/independent-math-01.json` (161274 bytes at receipt; SHA-256 `1f2c3361d2e4f19aadef7e44f093643915eb445e7da21914eccb330bedd4026a`) and the narrative `checks/independent-math-01.md`. The JSON includes all five independently regenerated records and exact endpoint-identity comparisons, not merely local locators. The four decisive degree-12 cases plus rotated pivot were rerun separately with CPython 3.12.14/python-flint 0.9.0 using `e1_exact.py`, producer SHA-256 `19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`. All rational endpoints, source counts, projector traces, choices and maximizing witnesses matched identically. Commands and mathematical input identities are in that receipt.

The independent agent also separately executed `e1_verify.py` (360 vector equalities/800 pairings) and `e1_check.py` (all 88 evidence records). Its own `tracks/bivariate-lanczos/code/drift/check_independent_math.py`, importing no developer mathematical code, constructs monomial Gram-Schmidt with `fractions.Fraction` and checks every input coordinate on a 15-node degree-two example: 1800 exact normal-derivative identities passed across all four rules, and all 12 rational Knode/KHS/Urow endpoints matched the producer. The degree-12 checks are independent executions of the inspected producer, not independent implementations; trusted dependencies remain explicit.

## Sources

PD-T041 is the existing rational frozen-propagator predecessor; its raw-entry certificate does not prove this quotient-norm comparison. Literature comparisons and limits in the old L2 prior-art review remain context only. No historical novelty claim.

## Proof or evidence

The proved finite reduction is explicit: exact all-prior projection constructs rational b,d,alpha; exact impulse recursion constructs g; rational projector diagonals are 1-sum_k b_k(i)^2/d_k; PD-T137 proves Knode^2<=kappa^2<=min(KHS^2,Urow^2). Exact comparisons of those bounds with the integer thresholds establish the first two inequalities for each set. For the ratio, 200000000000000 > 1000^2*170000000, and 88000000000 > 11^2*642000000. Strict inequalities therefore follow without relying on decimal logs or square roots. No uniform remainder is used because this is a derivative condition, not finite-epsilon drift.

The producer constructs the exact orthogonal basis by full projection and checks positivity/nonzero pivots. The independent execution and own low-degree Fraction reconstruction discharge the stated checker obligations within this finite scope; they do not remove trust in CPython/python-flint or replace the final external Claude audit.

## Scope

Only the specified rational grids, fixed rules and degree 12. The 88-run sweep and degree-two screen are broader descriptive evidence; the theorem above uses only four decisive full-source cases. The finite comparison supports E2 development, which root explicitly authorized, but proves no explicit-family all-degree rate. The scalar operation subset/full-model maps in PD-T138 have different source domains and cannot inherit these aggregate numerical constants.

## Open items

Final Claude mathematical audit remains required independently of the completed supplementary Codex checks. (Response-01 update: Claude audit-01 has been performed, CONFIRMED-WITH-CORRECTIONS; the Codex re-audit of the corrections is pending.) Actual deterministic rounding and all-degree family growth remain OPEN.

## History

- 2026-11-01: Codex mathematics developer, requested gpt-6.1-sol xhigh; runtime metadata unexposed. Created with exact executed producer evidence and proved reduction; conservative CONDITIONAL pending the independent rerun. Original KHS-only outcome retained as INCONCLUSIVE; tightened certificate recorded separately. No final ID allocated.

- 2026-11-01: CONDITIONAL -> PROVED after the independent exact rerun/identity receipt above was written with essential outputs. Mathematical statement, reduction and producer data unchanged; this is completion of the named verification obligation.

- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F1: added the pivot-tie disclosure to the Statement (T24 no tie, margin 0.008426; rotQ24 exact tie at column (2,1) from 90-degree symmetry; rotQ24 pivot rows are X-tie-broken frozen sequences); no claim or threshold changed; original wording: «The pivot choices are frozen at these exact data.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F2/E1-F3: described the projector-trace check as a consistency identity and cited the new exact B^T B = D check and the committed checker/output for the six inequalities and the factor-100 criterion (`e1_response_checks.py`, `response-01-e1-checks.json`); original wording: «The evidence checker verified all 88 source counts, projector traces and rational square-root intervals. These are developer executions; they do not replace the required independently executed check.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F4: "preregistered" replaced by "frozen" for the KHS-only test, and the freeze provenance and the low-degree sharpened-DEAD fact disclosed; original wording: «The **original KHS-only preregistered test is INCONCLUSIVE**; this result uses the later analytically derived Urow upper certificate and is reported as a separate strengthened certificate.»
- 2026-11-01 (Claude response-01, Sonnet 5.5): status line and Open items updated for audit-01 (status PROVED unchanged); original wording: «Overall status: PROVED (finite exact computer-assisted statement; ... independent executed rerun present; final Claude audit pending).»
