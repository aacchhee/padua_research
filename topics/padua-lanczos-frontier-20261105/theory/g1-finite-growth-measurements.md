# PD-T?lanczos-frontier-G1-fit — finite endpoint fitting and interval-gate measurements

ID kind: PD-T (provisional; no final ID assigned).
Aliases: G1 complete rational-grid endpoint fits; frozen finite logratio gate.
Split from: none.
Split into: none.

## Statement

On the frozen T24 and rational rotQ24 grids, all four rules BJ/mirror/alternating/exact-pivot and every integer degree2–20 have all-source exact endpoint rows independently matched before fitting (152rows). The frozen fitter actually computed the prescribed endpoint/midpoint descriptive OLS diagnostics. Each grid's unchanged universal interval kill predicate returns **INCONCLUSIVE, certified counterchoice**, because an explicit admissible logratio corner makes the late slope minus half the early slope strictly positive. The producer certifies the universal early-positive clause on both grids. Neither grid triggers KILL. The universal SSE clause is unneeded after that counterchoice and was not decided. No true condition curve or asymptotic rate is computed or inferred.

## Definitions

The source metric is PD-T137's aggregate all-source Hilbert norm and spectral normal-output condition, rather than the full scalar operation cube of L4. Rows give exact rational squared endpoints L²,H²,Urow²,U²=min(H²,Urow²), with0<L²<=U². The [saved fit specification](../g1-fit-spec.md) defines every formula and threshold without alteration.

For each degree s, the certified squared-ratio endpoints are `q_s^-=L_BJ²/min_c U_c²`, `q_s^+=U_BJ²/min_c L_c²`, with comparator minima taken separately over mirror/alt/pivot. The true logratio is enclosed by `[a_s,b_s]=[log(q_s^-)/2,log(q_s^+)/2]`. The universal test ranges over the entire independent product of these intervals. A rational tau vector represents the exact admissible point `(1-tau_s)a_s+tau_s b_s`.

Exponential and polynomial descriptive models are affine fits in predictors s and log(s+1), respectively, to log ordinates. Rule lower/upper curves are logL²/2 and logU²/2; midpoint is their mean. All-degree fits use2–20; ratio holdout predictions train only2–14 and score squared log residuals only15–20. Early/late slopes use2–10 and11–20. The universal predicate is the conjunction `2*SSE_P-SSE_E<=0`, early slope>0, and late slope−early slope/2<=0 for every admissible ordinate vector.

## Assumptions

Exact endpoint evidence and frozen source/grid/rule/tie identities, original325/625nodes and every source1,...,N_s−1. All152 producer and independent endpoint rows, complete choices/ties and input artifacts pass the entry guard before any logarithm or fit. Natural logarithms are enclosed by exact rational atanh series and sign-correct scaled log2, with dyadic outward arithmetic. Python3.12.14 standard-library Fraction supplies exact rational integer operations. Precision schedule128/256/512 fractional bits and maximum4096processed boxes per grid/precision are fixed; only128bits is needed in this actual run.

## Status by part

Overall status: MEASURED.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| Complete finite endpoint/midpoint OLS calculations | MEASURED | Actual producer report and distinct complete-report verification PASS. |
| Frozen universal-rule counterchoice on both grids | MEASURED | Explicit rational tau recipes and strict outward slope margins; distinct certified slope-sign verification PASS. |

No candidate rejection or all-degree theorem follows. KILL is not triggered on either grid.

## Depends on

The complete G1 endpoint scan and independent endpoint comparisons under PD-T137's metric; original [L1 preregistration](../attempts/L1.md); unchanged [fit specification](../g1-fit-spec.md). This measurement does not prove or refute the separate SH_n analytic theorem, every-rule stability, actual IEEE activation, or the original general exponential-separation target.

## Checks

Root authorized actual fitting only after152/152 independently matched rows. Manifest SHA256 `8bd04bb6502762a61d53d5633f6737786315d743b6e408e689d647ac7998c144` (7308bytes); producer SHA256 `18eea30277a3d2d58aab8ece2f15b33e83a1178d5b03e96180229b41a247aeac`. [Methods](../g1-fit-methods.md) records the exact command and prospective schema/resource plan. [Actual receipt](../evidence/g1-fit-actual.json) pins launch/source/manifest/report/logs. External1800s cap: exit0 in16.9720s, worker14.6305s. Fullreport1035283bytes,SHA256 `5211917f379060bfa5f477354bbe0cf29066dba76d85d428d43de34a6190176b`, retained outside Git at `/tmp/padua-lanczos-frontier-g1-fit/actual/report.json`.

The separate checker received report/receipt pins immediately after execution and is assigned actual independent reconstruction of input guards, logarithms, OLS and decisive counterchoices. The actual distinct verification now PASSes, as recorded below. Earlier40 synthetic arithmetic/guard tests are implementation checks, not this actual independent run.

## Sources

No external literature result or novelty/priority claim is added. Repository definitions and exact endpoint provenance remain explicit in the saved G1 methods and manifest. Frozen e1_exact.py source SHA256 `19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f` is required by the manifest. No unread literature is cited as independently verified.

## Evidence

Both grids use the same late-minus-half-early maximizing tau, ordered by degrees2,...,20:

`(1,1,1,1,1/2,0,0,0,0,0,0,0,0,0,1,1,1,1,1)`.

Positive coefficients choose the exact upper logendpoint; negative coefficients choose the lower, and the zero coefficient at degree6 uses midpoint. The full exact rational recipes and outward margins are retained in the report/receipt; decimals below are rounded descriptive displays, not replacement certificates.

| Grid | Minimum early slope | Counterchoice late−early/2 | Universal outcome |
|---|---:|---:|---|
| T24 | .594088615 | +1.061247932 | Certified INCONCLUSIVE |
| rotQ24 | .170682406 | +.951663459 | Certified INCONCLUSIVE |

These strict positive counterchoice margins show that the universally quantified kill predicate over the preregistered box is false. They do not say which exact ordinate choices the unknown true condition curve realizes. No box-cover computation was needed; none is claimed. The producer certifies the early-positive property separately from the failing late clause; the universal SSE clause remains undecided/unneeded.

Midpoint logratio diagnostics, explicitly **MEASURED and descriptive**, are:

| Grid | E holdout log-SSE | P holdout log-SSE | Early slope | Late slope |
|---|---:|---:|---:|---:|
| T24 | .839269770 | 47.32355168 | .880985389 | .824380405 |
| rotQ24 | 2.151288311 | 26.25284315 | .397466484 | .521318366 |

Endpoint/midpoint fits for each rule over2–20 are all retained as outward intercept/slope intervals. For a compact view, the exponential-model slopes of lower/upper/midpoint logendpoint curves are:

| Grid/rule | Lower curve slope | Upper curve slope | Midpoint slope |
|---|---:|---:|---:|
| T24 BJ | 1.534542513 | 1.646311980 | 1.590427247 |
| T24 mirror | .768600611 | .875794484 | .822197548 |
| T24 alternating | 1.033450038 | 1.115149134 | 1.074299586 |
| T24 pivot | .671399417 | .747785794 | .709592606 |
| rotQ24 BJ | 1.398267297 | 1.503091491 | 1.450679394 |
| rotQ24 mirror | 1.535599234 | 1.616803766 | 1.576201500 |
| rotQ24 alternating | .929791729 | 1.045859887 | .987825808 |
| rotQ24 pivot | 1.015065100 | 1.102737046 | 1.058901073 |

The lower/upper curve's fitted parameters are descriptive fits of those endpoints; signed OLS weights prevent treating them as universal lower/upper bounds on unknown fitted coefficients. Complete polynomial-model and intercept results, plus lower/upper logratio holdout diagnostics, remain in the pinned full report. Neither a finite positive slope nor a better finite heldout model establishes an asymptotic rate.

## Scope

Finite exact endpoint calculations plus outward numerical log/OLS verification under a saved operational rule. Certified counterchoice means only that this interval rule cannot kill continued exponential-separation development on that grid. It supplies no proof of exponential behavior of the true conditions, subexponential behavior, capacity ratios from lower/lower endpoints, IEEE activation, or every-platform numerical behavior. The source model and uncomputed trueK remain explicit.

## Open items

Actual distinct fit verification is complete and PASS; required later Claude scientific/protocol audit remains pending. Archive raw manifest/report/logs through root's cold-storage workflow; Windows delivery remains pending and temporary retention is not guaranteed. General/asymptotic targets remain separate open obligations. No final ID or merge readiness is implied.

## History

2026-11-05, Codex gpt-6.1-sol medium: implemented the frozen specification with prospective plan and synthetic checks only; after root's explicit complete-scan START actually executed unchanged producer and drafted this finite MEASURED record, subsequently accepted at distinct actual verification scope. No scientific threshold, dataset, model or source change was made.

### Actual distinct verification addendum

The separately implemented checker SHA256 `0bbcf38542e077806b8d2f9c36c7b0bdf8ca19105f562b7b4369aefaed70750c` actually verified the complete pinned report in29.717486s under its own1800s cap. It independently rebuilt the complete input/coverage guards, outward logarithms, OLS endpoint/midpoint intercept/slope intervals, heldout diagnostics, comparator-minimum recipes and both admissible late-minus-half-early counterchoices. The independently certified slope signs are positive on both grids, equivalently the rational-product signs are positive. The receipt field `exact_product_compare_to_one=1` records that sign: the checker can resolve it from outward logarithm bounds before its expanded-product fallback, so this field does not establish that an expanded rational product was evaluated. On this counterchoice branch the distinct checker does not separately re-evaluate the producer-certified universal early-minimum clause; its independently verified decisive late sign suffices for the INCONCLUSIVE verdict. It reports **PASS independent complete G1 descriptive report/certificate verification**, with both grid outcomes **INCONCLUSIVE, certified counterchoice**.

[Independent report](../independent-checks-g1-fit.md) and the independent receipt identity in [actual receipt](../evidence/g1-fit-actual.json) retain its separate command/source/input/report pins. This closes the preceding distinct-verification obligation; it does not replace required later Claude audit or strengthen the finite operational verdict into an asymptotic result. No further fitting, source change, cover run or precision increase occurred.
