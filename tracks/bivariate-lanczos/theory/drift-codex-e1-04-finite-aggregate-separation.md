# PD-T?drift-codex-04 — Certified finite aggregate span-sensitivity separation on a triangle and rational rotated square

ID kind: PD-T.
Aliases: E1 finite comparison; rational quotient certificate; BJ versus pivot/alternating at degree twelve.
Split from: E1 explanatory target. An all-degree family theorem and a scalar-rounding activation theorem remain OPEN.
Split into: none.

## Statement

Use the **all-source aggregate residual norm** and spectral-output condition kappa_12 from PD-T?drift-codex-01/02. Uniform weights and graded monomials x^(t-j)y^j, j increasing, are fixed. Let

    T24={(i/12-1,j/12-1):i,j>=0,i+j<=24},
    rotQ24={((3x-4y)/5,(4x+3y)/5):x=i/12-1,y=j/12-1,0<=i,j<=24}.

The choices are BJ (X at j=0, Y otherwise), alternating (X iff 2j<t), and exact pivot (choose larger d_k/||A b_parent||^2, ties X). The pivot choices are frozen at these exact data. Every source h=1,...,90 is included at degree 12 (N_12=91).

The exact rational bounds certify

    T24:    kappa_BJ^2 > 200000000000000,
            kappa_pivot^2 < 170000000,
            kappa_BJ > 1000 kappa_pivot;

    rotQ24: kappa_BJ^2 > 88000000000,
            kappa_alt^2 < 642000000,
            kappa_BJ > 11 kappa_alt.

In particular BJ exceeds the better of alternating and pivot by a factor greater than 10 on each set. This is a finite, worst-case, aggregate-residual **capacity** comparison. It asserts neither actual floating-point drift nor an asymptotic rate.

## Definitions

Use Knode as a lower bound, KHS and Urow as upper bounds, with U=min(KHS,Urow), exactly as in PD-T?drift-codex-02. The final-stage raw endpoints (rounded here only for readability) are:

| Set/rule | Knode squared | U squared |
|---|---:|---:|
| T24/BJ | 2.0493879359e14 | 1.0859728745e16 |
| T24/pivot | 1.2479403793e7 | 1.6145977113e8 |
| rotQ24/BJ | 8.8170667576e10 | 1.2841166021e12 |
| rotQ24/alternating | 3.9414606242e7 | 6.4187254242e8 |

The mathematical decisions use rational strings in the essential evidence, not these decimals. The ratios of the squared lower/upper endpoints are about 1269287.03 and 137.36476. Integer thresholds in the Statement are weaker convenient exact consequences.

## Assumptions

Exactly the injection model and source scaling of PD-T?drift-codex-01/02; rational nodes above; fixed choices. These grids are injective for degree 12. For T24, the principal triangular lattice is injective through degree 24 (iterated row-factor argument); for Q24, a polynomial of degree at most 24 vanishing on all 25x25 grid nodes vanishes identically by univariate root counting in each coordinate; an invertible linear substitution preserves that property.

## Status by part

Overall status: PROVED (finite exact computer-assisted statement; written reduction, committed essential checker/evidence and independent executed rerun present; final Claude audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| T24 degree-12 inequalities | PROVED | Exact producer/checker plus independent exact full-source execution and identical rational endpoints |
| rotQ24 degree-12 inequalities | PROVED | Same independently executed certificate for BJ and alternating decisive cases |

Candidate / claim disposition: retained finite property certificate. The **original KHS-only preregistered test is INCONCLUSIVE**; this result uses the later analytically derived Urow upper certificate and is reported as a separate strengthened certificate. The intended property survives that strengthened test; it must not be described as the original certificate passing.

## Depends on

PD-T?drift-codex-01 (normal derivative reduction) and -02 (rational bounds). No dependence on a measured asymptotic fit, an implicit-section completion, or a claimed equivalence with upstream V+A code.

## Checks

Producer: `tracks/bivariate-lanczos/code/drift/e1_exact.py` (CPython and python-flint exact rational arithmetic). Runner: `e1_batch.py`. Essential committed evidence: `topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json` (88 exact records, all sources), `e1-exact-check.json`, `e1-derivative-verification.json`, `e1-freeze.json`, and `e1-manifest.json` with commands and hashes. Checker: `e1_check.py`; separate developer derivative reconstruction: `e1_verify.py`. Those paths are repository-relative here to specify reproducible commands.

The derivative verifier checked 360 rational-vector equalities and 800 exact basis pairings at degree 3 across both sets/all rules. The evidence checker verified all 88 source counts, projector traces and rational square-root intervals. These are developer executions; they do not replace the required independently executed check.

The mathematics developer separately parsed the final exact rational endpoints using CPython `fractions.Fraction`, enabled large-integer parsing with `sys.set_int_max_str_digits(100000)`, and checked each of the six strict inequalities in the Statement by rational comparison. All returned True. This checks arithmetic on the evidence, not an independent reconstruction of the producer. An initial parse attempt hit Python's default integer-string length limit on the rotated rational; the explicit larger limit resolved it without changing any data.

Independent execution: **completed** by the supplementary Codex mathematical checker. Essential independent evidence is `topics/padua-lanczos-drift-20261101/evidence/independent-math-01.json` (161274 bytes at receipt; SHA-256 `1f2c3361d2e4f19aadef7e44f093643915eb445e7da21914eccb330bedd4026a`) and the narrative `checks/independent-math-01.md`. The JSON includes all five independently regenerated records and exact endpoint-identity comparisons, not merely local locators. The four decisive degree-12 cases plus rotated pivot were rerun separately with CPython 3.12.14/python-flint 0.9.0 using `e1_exact.py`, producer SHA-256 `19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`. All rational endpoints, source counts, projector traces, choices and maximizing witnesses matched identically. Commands and mathematical input identities are in that receipt.

The independent agent also separately executed `e1_verify.py` (360 vector equalities/800 pairings) and `e1_check.py` (all 88 evidence records). Its own `tracks/bivariate-lanczos/code/drift/check_independent_math.py`, importing no developer mathematical code, constructs monomial Gram-Schmidt with `fractions.Fraction` and checks every input coordinate on a 15-node degree-two example: 1800 exact normal-derivative identities passed across all four rules, and all 12 rational Knode/KHS/Urow endpoints matched the producer. The degree-12 checks are independent executions of the inspected producer, not independent implementations; trusted dependencies remain explicit.

## Sources

PD-T041 is the existing rational frozen-propagator predecessor; its raw-entry certificate does not prove this quotient-norm comparison. Literature comparisons and limits in the old L2 prior-art review remain context only. No historical novelty claim.

## Proof or evidence

The proved finite reduction is explicit: exact all-prior projection constructs rational b,d,alpha; exact impulse recursion constructs g; rational projector diagonals are 1-sum_k b_k(i)^2/d_k; PD-T?drift-codex-02 proves Knode^2<=kappa^2<=min(KHS^2,Urow^2). Exact comparisons of those bounds with the integer thresholds establish the first two inequalities for each set. For the ratio, 200000000000000 > 1000^2*170000000, and 88000000000 > 11^2*642000000. Strict inequalities therefore follow without relying on decimal logs or square roots. No uniform remainder is used because this is a derivative condition, not finite-epsilon drift.

The producer constructs the exact orthogonal basis by full projection and checks positivity/nonzero pivots. The independent execution and own low-degree Fraction reconstruction discharge the stated checker obligations within this finite scope; they do not remove trust in CPython/python-flint or replace the final external Claude audit.

## Scope

Only the specified rational grids, fixed rules and degree 12. The 88-run sweep and degree-two screen are broader descriptive evidence; the theorem above uses only four decisive full-source cases. The finite comparison supports E2 development, which root explicitly authorized, but proves no explicit-family all-degree rate. The scalar operation subset/full-model maps in PD-T?drift-codex-03 have different source domains and cannot inherit these aggregate numerical constants.

## Open items

Final Claude mathematical audit remains required independently of the completed supplementary Codex checks. Actual deterministic rounding and all-degree family growth remain OPEN.

## History

- 2026-11-01: Codex mathematics developer, requested gpt-6.1-sol xhigh; runtime metadata unexposed. Created with exact executed producer evidence and proved reduction; conservative CONDITIONAL pending the independent rerun. Original KHS-only outcome retained as INCONCLUSIVE; tightened certificate recorded separately. No final ID allocated.

- 2026-11-01: CONDITIONAL -> PROVED after the independent exact rerun/identity receipt above was written with essential outputs. Mathematical statement, reduction and producer data unchanged; this is completion of the named verification obligation.
