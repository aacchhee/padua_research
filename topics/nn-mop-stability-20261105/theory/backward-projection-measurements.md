# PD-T442 — full common-data stationary fits

## Binary64 provenance — response dated 2026-11-06

All binary64 measurements in this record, including displayed errors, gains,
fit metrics, condition estimates, diagnostics and precision-stall outcomes,
are platform-dependent. Historical values below are retained from the
producer platform: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0.
Runs are deterministic on the recorded platform; this does not promise
bitwise reproduction on another numerical stack. The audit platform
(Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, mpmath 1.4.1) gave Krawtchouk
N4 nodeqr eta_c = 30.78u, still <100u. N4 native mixed pairs remain below
100u and N8 native pairs still fail that threshold. No run was reselected
or retuned; historical tables and their receipt identities are preserved.

ID kind: PD-T. Aliases: whole-array Gauss–Newton shadow witness; positive
common-data fit. Split from: [stable-solver-target.md](stable-solver-target.md), as a separate
supporting, scoped-negative or measured result, not a solved target case.
Split into: none.

## Statement and status

Overall status: **MEASURED**. Round2 fitted the complete NN arrays from
frozen C4, native LU and native nodeqr, at N4/8 on both frozen families.
Every returned input was frozen as exact rational common nodes and two
exactly normalized positive weight vectors. All14/44 defining mixed
systems at N4/8 were nonsingular by exact rational elimination. The
entire coefficient triangle was rebuilt from each such input.

For N4 native LU, the measured input perturbations are0.98455u (Kraw)
and1.57883u (Hahn), and whole-array corrections are1.93038u and3.06170u.
For N4 nodeqr, both components are below100u on both families. The frozen
C4 N4 correction is877.04u/5599.74u under this fit. N8 native corrections
and input perturbations exceed100u. These are finite feasible mixed pairs,
not a stability theorem, certified nearest points, or finite strict
input-only backward errors for the raw arrays.

## Definition of the measured pair

Let p0 be the exact original input, y the frozen binary64 output and
s_f=max_nu|F(p0)_(nu,f)| for f=a1,a2,b1,b2. These four scales are fixed
and positive. The optimization objective is the fixed SPD coefficient
metric

    Q(p)=sum_(nu,f) ((y_(nu,f)-F(p)_(nu,f))/s_f)^2.

It includes every site and all four fields, including structural zeros
and terminal coefficients. No path-only coefficient restriction is used.
For the frozen rational witness q report separately

    eta_c=max_f max_nu |y_(nu,f)-F(q)_(nu,f)|/s_f,
    eta_d=max(max_i|q.x_i-p0.x_i|,
              max_(j,i)|q.w_(j,i)-p0.w_(j,i)|/p0.w_(j,i)).

Weights in this definition have mass1. Original node sup norm is1, so the
code's division by that norm agrees with absolute scale1 here. The record
also emits sqrt(Q(q)). Minimizing Q is not minimizing eta_c, eta_d or a
combined mixed objective. The result is a feasible pair even when the
optimizer does not terminate at its numerical stationarity threshold.
Strict beta(y;p0)=inf{||p-p0||:F(p)=y} is unchanged. The exact dyadic
obstruction in PD-N163 is not repaired by relabeling
eta_d as beta.

## Algorithm actually executed

The chart has N unconstrained node coordinates and two sets of N-1
logits. In each weight vector the last logit is fixed0, and
w_i=w0_i exp(theta_i)/sum_l w0_l exp(theta_l). This removes both mass
gauges and preserves positivity. Strict node ordering is checked in each
trial. The initial chart is the exact original input. D1's analytic full
Jacobian is chained through the softmax chart; the derivative for one
logit is w_i(g_i-sum_l w_l g_l).

At each iteration solve the full scaled least-squares linearization by
real Householder QR, then try up to24 step halvings for strict decrease
of Q. Stop at normalized ||J^T r||/(||J|| ||r||)<1e-55 or chart step
sup<1e-70; at most10 iterations. The implementation uses sign(0)=+1
in the real reflector. Initial mpmath1.3.0 qr_solve failed on a structural
zero diagonal because its sign(0)=0; no reported result uses that failed
run. This explicit QR remedy is standard linear algebra, not a new method.

Fit at100dps and160dps separately. Freeze each final node and weight to
70 decimal significant digits as a rational, then renormalize the weights
exactly. Rebuild that actual rational input at180dps. The exact positivity,
ordering and nonsingularity checks concern this frozen input. Optimizer
history concerns the unrounded chart iterate; it is not a certified
stationarity bound for the rational witness.

## Results and precision checks

u=2^-53. Historical Nov-5 receipts, whose temporary bytes are now lost,
reported that all12 fits met the stated numerical stationarity threshold at
160dps. Their input perturbation, eta_c and sqrt(Q) reported binary64
values agreed exactly between the100/160dps runs. This was a numerical
precision check, not an interval enclosure. Three100dps fits stopped on
line-search precision limits (KrawN8 C4, HahnN8 C4 and nodeqr); those
failures were recorded in those raw histories. The160dps runs took10.19s
and19.29s for Kraw/Hahn in the final concurrent rerun; timing is not a
cost claim. These optimizer flags/history and the100dps runs are historical
receipt claims only: the committed response reference omits them and cannot
independently establish convergence or100/160dps agreement.

| Family | N | Method | eta_d/u | eta_c/u | sqrt(Q(q)) |
|---|---:|---|---:|---:|---:|
| Kraw | 4 | C4 | 72.1010 | 877.039 | 1.73432e-13 |
| Kraw | 4 | LU | .984547 | 1.93038 | 4.89907e-16 |
| Kraw | 4 | nodeqr | 6.84863 | 29.8852 | 9.31404e-15 |
| Kraw | 8 | C4 | 8222.74 | 16453919 | 4.02885e-9 |
| Kraw | 8 | LU | 1258.75 | 5692.26 | 2.29206e-12 |
| Kraw | 8 | nodeqr | 2019.75 | 31904.7 | 9.61772e-12 |
| Hahn | 4 | C4 | 1014.48 | 5599.74 | 1.22700e-12 |
| Hahn | 4 | LU | 1.57883 | 3.06170 | 8.38061e-16 |
| Hahn | 4 | nodeqr | 4.85990 | 9.68657 | 2.03896e-15 |
| Hahn | 8 | C4 | 311320429 | 1237432021 | 2.47295e-7 |
| Hahn | 8 | LU | 3880.88 | 14956.2 | 3.81816e-12 |
| Hahn | 8 | nodeqr | 8215.55 | 48357.9 | 1.13073e-11 |

The lost Nov-5 receipts reported normalized last-iterate stationarity
values at160dps ranging from
2.63e-64 to7.79e-56. No Hessian positivity, interval solve, global
minimum, nearest-point certification or rounding-error theorem is claimed.
The analytic local theorem in PD-T441 is separate
and supplies no certified radius containing these numerical iterates.

## Executed checks, provenance and scope

Two targeted implementation checks ran at100dps: a rectangular QR example
with leading structural zeros gave normal-equation residual5.90e-100;
a centered finite difference for the first N4 Kraw weight logit, step1e-30,
agreed with the complete analytic coefficient derivative within2.96e-58.
These are developer diagnostics, not independent proof or error bounds.
The separate checker then re-executed the developer's own fit code for
all four N4 LU/nodeqr160dps cases, obtaining the same rational witnesses on
the recorded platform. Its independent exact defining-moment formulation rebuilt all40 coefficient fields per case and checked positivity,
ordering, mass1, all14 normality systems, the full residual/SPD objective,
and the input/field correction metrics. It also checked the rational chart
stationarity squared<1e-100 exactly; displayed stationarity norms are
8.34e-54,7.29e-55 (Kraw LU/nodeqr),9.39e-53,3.40e-53 (Hahn). These
rounded witnesses do not meet the pre-rounding1e-55 optimizer threshold;
the returned flag must retain its stated unrounded-iterate meaning.
The original N8 witness reconstructions are reported in audit-01.md.
The newly committed response reference has a separate developer-executed
exact checker; its focused re-audit remains in LOG.md. No global nearest
minimum is certified.

The final producer uses the explicit fields `optimizer_stationarity_converged`,
`optimizer_history`, `optimizer_iterations` and `optimizer_stop_reason`
for the unrounded fitting stage. It separately emits
`returned_witness_scaled_stationarity` and its180dps evaluation precision
for the actual rational witness. Across all12 cases the latter ranges
from6.60e-57 to3.64e-52. These output-stage changes preserve every fitted
rational input hash and pair metric from the first round2 execution.

Historical Nov-5 receipt and command, with source at commit
`4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71`:
[independent-checks-02.md](../independent-checks-02.md), section
"Full-data numerical projection follow-up". The checker at this reused path
has since changed; current identities are in
[evidence-manifest.json](../evidence-manifest.json). Historical checker
`code/independent_check_followup_projection.py` SHA256
`3d2ae221d2d641f3f6fcf94cd25362589235bb89e00ecdebd7c89ae53deebc9c`.
Command from root:

```sh
python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py > /tmp/nn-mop-independent-projection-final.json
```

Final raw4342bytes SHA256
`048f5291518071d60f89632f937e4cb3375b961176c0e4b803b7e48f421c12bb`.
This final rerun additionally compares the returned180dps stationarity
with the independent exact rational calculation. All four scientific
case payloads agree with the first independent execution. The separate
report preserves that earlier raw identity and the reporting-fix history.
This is separate execution of the developer fit code and independent exact
finite witness reconstruction,
not an independent audit of every analytic theorem.

Commands, input/source hashes, raw byte receipts and environment appear
in the round2 section of [D5](../attempts/D5.md). Producer is
`code/backward_projection.py`. Depends on frozen C4, native_mixed,
backward_joint normality checking, and D1 conditioning's analytic AD.
No new primary paper was read for this round; Gauss–Newton and normalized
weight charts are standard mechanisms, with no algorithmic novelty claim.

## Open obligations and history

General mixed backward stability remains **OPEN**. N4 finite pairs are
useful evidence under the dated mixed amendment, not an unchanged G4
strict-backward pass. N8 does not meet100u in either component for the
native variants tested. Different coefficient/input metrics, a certified
nearest fit or a uniform stable algorithm require explicit new work.

2026-11-05, requested Codex gpt-6.1-sol xhigh. Rules/source
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Round1 published at
929ef787c74afc2bedcc8327d44dddc2c3409f46; coordinator explicitly authorized
the round2 full-Jacobian N4/8 fits. Old code was frozen; this separate
script implements candidate C's already recorded full-image fit.

Parent unresolved target: [stable-solver-target.md](stable-solver-target.md); supporting results do not establish its general stability conclusion.

Response M3 reference: [projection-reference.json](../evidence/projection-reference.json) and [reference provenance](../evidence/README.md). This is a new fixed-configuration response run, not recovery of the missing original temporary bytes.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-N?nn-mop-stability-codex-31` → `PD-N163`.
- `PD-T?nn-mop-stability-codex-31` → `PD-T441`.
- `PD-T?nn-mop-stability-codex-33` → `PD-T442`.
