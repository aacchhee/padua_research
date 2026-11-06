# PD-T?padua-3d-20261106-codex-r08-T9-measurements — frozen refinements through degree16

ID kind: PD-T.
Aliases: historical MEAS?padua-3d-20261106-codex-T9-r06-01; T9-R06-M; T9-R06-M05.
Split from: none; whole measurement record re-homed under a standard PD-T provisional namespace.
Split into: none. No mathematical statement or measurement is changed and no final ID is allocated.

## Statement (response08 template completion)

The frozen procedures below produced the recorded finite mesh values,
local-refinement lower samples and descriptive fit residuals for QR,
one-sweep localdet, supplied T8 snapshots and the specified T10 extractions.
No certified continuous maximum or asymptotic rate is claimed.

## Definitions (response08 template completion)

N=binom(n+3,3), Pi_n is the three-dimensional total-degree space, and
Lambda_q is the sampled cardinal absolute sum on the q^3 tensor Lobatto
mesh. A refined value is the largest value found by the frozen local
search, also only a lower sample. The inherited-basis extraction and the
owner’s lexicographic-basis extraction are distinct as described below.

## Assumptions (response08 template completion)

Precisely the frozen algorithms, inputs, degree ranges, selection identities,
meshes, inverse guards and fit windows in preregistration-T9-round06.md and
the original receipts. The supplied T8 snapshots stop at n9. Finite rank
certificates belong to their owners; numerical inverse guards are not exact
unisolvence proofs for newly extracted nodes.

Status: **MEASURED lower samples only**. Neither the sampled maxima nor the local optimizations enclose the true supremum. The numerical inverse checks are not exact unisolvence proofs for newly extracted QR/localdet nodes.

## Frozen procedures and feasibility

`preregistration-T9-round06.md` fixes degrees2..16, meshes21^3 and41^3, four best mesh starts and eight corners, L-BFGS-B limits/tolerances, inverse guards, and fit windows before the n13..16 runs. QR uses tensor Lobatto(2n+1) and inherited degree-ordered basis. Localdet uses one determinant-increasing sweep with four cardinal mesh starts plus the current node. The new one-sweep family is distinct from the inherited two-sweep control; the latter is separately reproduced at n2. QR n4/n8 reproduce inherited refined maxima to <1e-10.

QR completed all15 degrees in38.999 CPU seconds; one-sweep localdet in219.363 CPU seconds. The n8 localdet cost probe was2.667 CPU seconds and its frozen cubic n16 estimate stayed below1200 seconds, so no single-exchange fallback was needed. All rows passed condition<1e12 and inverse-residual<=1e-7, and all12 final local starts reported success. These success flags do not certify global maximality. Raw node NPY and all initial/final local optimizer values are retained in unique scratch directories recorded by each receipt and are regenerate-only.

T8 snapshots were selected by their **pre-existing21^3 score** among certified rows from phi2/union2/union3/union4 before refined maxima were computed. They cover n2..9; no optimized T8 snapshots n10..16 were supplied because the owner hit its registered finite quality gates. Missing degrees are explicit, and the13..16 holdout is INCONCLUSIVE. Exact rank certificates belong to the input owner; only quality was recomputed here.

T10's finite census supplies full-rank folded parity-anisotropic cubature supports at n2..16. A deterministic unweighted QR extraction using the inherited basis was frozen and measured at every degree; this is a T9 benchmark and is **distinct** from the owner's frozen lexicographic-basis extraction. The owner's n2..7 extraction was separately regenerated/refined, reproducing its n6/n7 mesh41 controls. QR tie choices can depend on basis order and floating arithmetic, so the two extraction families are not pooled or silently substituted. Exact folded-node payload hashes were checked; minimal extracted-set nonsingularity is checked numerically only. T10's census does not prove global determinant optimality above n3.

## Refined values

| n | QR | One-sweep localdet | Best supplied T8 | T10 inherited-basis extraction |
|---:|---:|---:|---:|---:|
|2|7.000000|4.153631|7.101763|8.750000|
|4|11.263055|11.140116|54.225018|23.596762|
|6|22.508222|17.669650|137.483323|30.654015|
|8|45.564648|24.124151|492.877315|45.460651|
|10|66.720286|34.870367|not supplied|82.584511|
|12|117.738030|55.677884|not supplied|144.342601|
|14|115.566993|64.206906|not supplied|148.106389|
|16|168.339955|93.638481|not supplied|258.414904|

At n16, QR mesh21/mesh41/refined are151.354837/161.502651/168.339955; localdet83.124880/90.643538/93.638481; T10 extraction251.811096/255.709296/258.414904. The refinements materially raise some mesh samples, so the mesh alone should not be treated as a maximum. Localdet has the lowest measured values among these supplied finite candidates in all tested degrees; this is a benchmark comparison, not an asymptotic theorem or a claim of optimality.

## Frozen fit comparisons

The dependent variable is log of the refined sample. Each model has a freely fitted intercept. Polynomial means alpha log n with alpha>=1; logarithmic powers mean k log log n, k=1,2,3,4. SSE is descriptive.

| Family, window | Count | Power alpha | Power SSE | Best k in1..4 | Log-power SSE |
|---|---:|---:|---:|---:|---:|
|QR,4..16|13|2.061682|0.141318|4|0.304445|
|localdet,4..16|13|1.690372|0.281843|3|0.633937|
|T10 extraction,4..16|13|1.861446|0.523563|4|0.967261|
|QR,13..16|4|1.935909|0.014956|4|0.019934|
|localdet,13..16|4|1.708828|0.062255|4|0.063588|
|T10 extraction,13..16|4|2.527182|0.104957|4|0.130762|

The T8 partial4..9 sample has only6 points (no13..16 holdout): alpha3.330891, power SSE0.406097, best fixed log-power k4 SSE1.050203. The owner-frozen T10 n2..7 family has only4 points in the4..16 window and no holdout; it is not evidence for the complete-degree fits. Finite fit preferences do not prove or refute O(log^3 n), O(log^4 n), or any polynomial asymptotic rate.

## Evidence and boundaries

Receipts: `t9-r06-qr.json`, `t9-r06-localdet.json`, `t9-r06-snapshots.json`, `t9-r06-t10-owner.json`, and `t9-r06-controls.json`, each <16KiB. Hashes, versions, seed0, sources, exact commands, raw policy, and replay instructions are in the receipts and `t9-r06-run-manifest.json`. Snapshot refinement cost16.799 CPU seconds plus0.652 seconds for owner controls; no missing-data extrapolation or asymptotic gate kill was performed. This completes the registered refinement/fit route with measured outcomes; certified global suprema remain a separate open problem.


## Status by part, dependencies and history — response08

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Frozen finite mesh/refinement values and descriptive fits | MEASURED | Original receipts and actual historical reruns |
| Certified continuous supremum or asymptotic growth law | OPEN, outside statement | No enclosure or all-degree proof |

## Depends on

The frozen numerical definitions, source/input hashes and owner
selection identities in [t9-r06-run-manifest.json](../evidence/t9-r06-run-manifest.json).
Imported exact-rank certificates remain the input owners' results; no
external source theorem is used to upgrade measured norms. The established
QR/Fekete baseline is attributed in the [gate/source supplement](../novelty-gate-supplement-round08.md).

## Checks

This worker reviewed the old body and receipt identities but did not
rerun optimizers. Audit03/T9 executed the historical replays. This standard
PD-T namespace represents a measured mathematical claim, not a new proof or
an administrative negative result. The old MEAS header is retained as an
alias, and root may add its pointer without changing historical evidence.

## Sources

The established QR/Fekete baseline and bounded reading coverage are in the
[gate supplement](../novelty-gate-supplement-round08.md). No external theorem
is load-bearing for these floating observations.

## Proof or evidence

The original detailed tables, raw-identity/command manifest and historical
replays above are the evidence; this namespace completion supplies no new run.

## Open items

Certified continuous suprema and any asymptotic assertion remain
unresolved. No additional run is required merely to change this namespace.

## History

2026-11-06, Codex records worker, assigned gpt-6.1-sol xhigh, runtime
metadata not independently exposed; rules/input9042e1c42964150f30fdbe8563c12ba6c6a8692a.
The old measurement narrative is preserved above. The changed title/namespace,
aliases and separately marked template fields supply the record completion;
no observation, fit or scientific claim changes and no new execution is claimed.
