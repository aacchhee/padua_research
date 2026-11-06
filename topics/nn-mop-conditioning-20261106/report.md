# NN MOP conditioning: metric, rates and finite solver comparison

M1 verdict: **intrinsic within the declared diagonal-gauge/fieldwise metric**, a MEASURED finite screen supported by an all-N Krawtchouk theorem. Both positive fixed gauges and positive differentiable input-dependent rescalings of the polynomial basis retain the diagonal b fields. Their gauge-infimum growth fits over N32–64 are bounded away from the gate's threshold5 for both families. This does not declare conditioning independent of every possible input/output norm.

LITERATURE: LIT-502/LIT-348's norm-balanced updating reports an algorithm's recurrence residual, whereas C1 bounds forward-map conditioning in the declared fieldwise metric; the conclusions concern different quantities. [Reading coverage](response-literature.md).

## Metric and rate results

The input box is absolute node displacement at scale one on [-1,1], with componentwise relative weights. Output is the largest of the four NN field-relative sup errors. The exact gauge definition also retains the forward coefficients after rescaling. For NN, measured fitted-ratio bounds are [9.181247,10.370243] Krawtchouk and [10.355427,13.261408] Hahn. These bound the fit of the gauge-infimum sequence without evaluating every b row using signed regression weights and pointwise lower/upper envelopes; they are not fits of a surrogate lower curve or certified outward enclosures. Step-line bounds are [9.745754,9.755463] and [11.685726,11.765132]. See [gauge theorem](theory/c1-gauge-invariants.md), [measurements](theory/c1-measurements.md), [summary](c1-summary.json) and [61-row grid](c1-grid.csv).

Both scalar marginals were evaluated at every N4–64 with monic and symmetric orthonormal outputs, including spacing-scale, componentwise-node, log-weight tangent and fixed-mass variants. Their N32–64 fitted ratios are about1.02 rather than the MOP ratios above. At N64 the orthonormal mixed conditions are about277.03/63.00 for the two Krawtchouk marginals and44.07/355.84 for Hahn. This is measured slow growth, not an all-N polynomial theorem. Exactly symmetric zero diagonal fields use absolute scale one, never division by a numerical near-zero. [Scalar derivative](theory/c1-scalar-derivative.md). The closest scalar derivative predecessor is Fischer1998 (LIT-113, Lemmas4–5, related LIT-112/365 and IDEA-087/088); these finite controls do not import the secondary-reported polynomial conditioning bounds. [Coverage](response-literature.md).

For the exact Krawtchouk pair p1=2/5,p2=1/2, the written [all-field upper proof](theory/c2-sharp-upper.md) gives

    kappa_N <= 3,000,000 N^13 (5+2sqrt(6))^(N-1), N>=2.

Together with PD-T437 this proves lim kappa_N^(1/N)=5+2sqrt(6). The proof includes arbitrary admissible common node motion, independent weight directions, every a/b field and terminal support polynomials. The prefactor is loose and supplies no uniform finite-perturbation radius. The same rate is squeezed for the NN gauge infima by the invariant diagonal lower and monic upper.

For general fixed distinct binomial parameters, the [parameter lower theorem](theory/c2-krawtchouk-parameter-lower.md) supplies the explicit lower base

    rho(p1,p2) = (p1+p2-2p1p2+2sqrt(p1p2(1-p1)(1-p2)))/abs(p2-p1).

It is a lower base, not a proved matching general formula. For Hahn, [all-N normality](theory/c2-hahn-normality.md) and a simple [all-N lower bound](theory/c2-hahn-lower.md) with base2 are proved analytically for the exact gamma=1 benchmark. A stronger [balanced-terminal theorem](theory/c2-hahn-terminal-rate.md) proves an exact terminal parity-row rate rho_H=12.1136005841…, the largest root of r^4−14r^3+24r^2−14r+1, and a full-map liminf lower bound of that base. It covers both size parities and fixed masses. This is not equality for the full Hahn condition: a matching full-map upper remains OPEN. PD-T448's remaining OPEN conjuncts in its single metric are itemized in [classification-proposal.md](classification-proposal.md).

The finite Hahn fitted ratios below rho_H are consistent with the proved asymptotic lower rate: polynomial factors affect finite ratios, so a finite fit is not a limiting-rate estimate.

The [matrix theorem](theory/c1-matrix-metric.md) separately bounds the induced box-to-spectral condition of the authenticated monic integer-node Hessenberg matrix. Neither a fieldwise row sum nor its gauge optimization equals that matrix condition. Arbitrary matrix similarities and the paper's perturbation-based conditioning experiment remain distinct quantities.

The response to audit NOTE-1 gives a [finite positive optimizing gauge](theory/response-gauge-infimum.md): for both benchmark families and each of the six stated node/mass models, K_fix=K_dep=max(kappa_b1,kappa_b2), attained by a sufficiently small positive degree taper. Thus all off-diagonal derivative sensitivity can be suppressed below the unchanged diagonal condition in this fieldwise metric. This does not optimize a relative global matrix norm or improve an algorithm's residual. The original fitted envelopes remain valid; they are not new full-b evaluations.

The registered PD-T448 record is unchanged in this response. A [PARTIAL classification proposal](classification-proposal.md) explicitly splits its solved exact Krawtchouk rate conjunct from its OPEN prefactor/radius and full-Hahn obligations, for focused audit and later reviewed registry application.

## Weak stability

A general weak-stability theorem remains **OPEN**. Independent LU residual perturbations at different mixed indices need not come from one common node/weight perturbation. The [reduction](theory/c3-weak-stability-open.md) includes direct terminal-input dependence and identifies the missing useful norm-transfer estimate; it is not a theorem with an inferred constant.

On the developer stack the [native grid](theory/c3-grid-measurements.md) completed232 measured solves: both families, every integer N4–32, four methods. On kappa*u<=1, A-LU's largest E/(kappa*u) is .809315/.469316 for Krawtchouk/Hahn. C4 reaches40533.1 at Hahn N14. Audit-01's other numerical stack completed231/232, with Krawtchouk N32 A-LU breakdown; its Krawtchouk A-LU maxima changed. The numerical home records both platform outcomes without overwriting the developer values. Large-N ill-conditioning warnings, large errors and ratios with kappa*u>=1 are retained. No C3 theorem was claimed, so M3 is unactivated, not PASS. The ratios are diagnostics, not a proof that any algorithm realizes a worst-case input direction.

## Authenticated external comparison

AC's archive matches SHA256 cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145 and all27 member pins. M4's selected actual Octave9.4 reproduction passes: CORE error2.691214553706643e-10 versus the previously authenticated paper reference6.851191e-10, log10 ratio−.4058. M2 passes against pinned exact matrix generators for both families. A solver's larger forward error was not reclassified as a normalization mismatch.

The final comparison covers116 family/size/input-coordinate configurations and348 external calls, with58 bitwise checks establishing identical normalized binary64 inputs to the native grid. Initial JSON decimal transport changed normalized node bits (first detected at Krawtchouk N12) by one ulp; those outputs were exploratory and were replaced by an IEEE754-hex rerun. Both archive integer inputs and shared normalized inputs remain labeled. [Receipt](c4-comparison-receipt.json), [source and execution](external-code.md), [C4 attempt](attempts/C4.md).

All14 tables in [c4-tables](c4-tables) report four NN field errors and integer-node monic Hessenberg spectral error. Native solvers return complete NN arrays. External solvers return one Hessenberg path: their NN-column results include an explicitly named H+d0 functional lift, with d0 computed from the actual input and postprocessing at140/220dps. This is extra high-precision postprocessing, not the external algorithm's native output, a positivity certificate, or joint backward error. The maximal final lift precision disagreement is1.698e-107. Matrix-error columns compare the direct returned/reconstructed matrices without that lift.

The separate [capacity diagnostic](c1-error-comparison.json) compares measured matrix errors with bounds on kappa_2*u. It cannot prove a universal weak-stability constant; once the local capacity is large, small ratios lose practical force. Archived Advanpix-dependent random/conditioning experiments were not reproduced without that licensed toolbox. No MATLAB or all-platform agreement is claimed.

## Evidence and remaining work

[Supplementary independent checks](independent-checks-01.md) and the [focused terminal-rate check](independent-checks-02.md) reconstruct the proofs and execute separate exact/numerical checks; they supplement the single required Claude audit. Code and small essential tables/receipts are committed. Regenerable raw arrays remain temporary with hashes and commands; no cold-storage delivery is claimed. No third-party source, PDF or paper data is committed.

Sharp Hahn growth, a matching general-parameter upper rate, a general useful weak-stability theorem, general-input gauge minimizers outside the proved b-dominance condition, outward numerical enclosures, finite-error radii and the licensed-toolbox experiments remain OPEN/unrun. This does not weaken the separate written theorems. Shared scientific registries and final-ID allocation are deferred to audited PR preparation. Only AC merges.
