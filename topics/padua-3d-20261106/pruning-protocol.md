# Adaptive parity-grid pruning — prospective protocol

2026-11-07. Rules/input `6d894d50efd8167c5b10f3d5b0da4d8cf214b681`.
Codex developer, gpt-6.1-sol high (configured metadata; provider runtime
metadata unexposed). Root owns Git/shared records. New authorization is
**up to fifteen total pruning research rounds**, independent of old U1/U2/U3
counters. Engineering checks and independent verification consume zero.
Only P1 below is allocated; later rounds require a published prospective
appendix after the actual preceding result. A ceiling is not a quota.

## Gate, objective, and retained candidates

The completed [pruning gate](pruning-gate.md) clears known backward
experimental-design variants, with no algorithmic novelty or priority claim.
T9's extraction lemma leaves inverse control unresolved. T10's frozen
restricted-QR and boundary-removal failures remain intact: the new tested
path recomputes deletion scores on the current support, rather than
renaming either old selector. Broad minimal-node/asymptotic goals stay OPEN.

All pruning fits use physical observations and **unweighted OLS**, W=I,
in the continuous product-Chebyshev orthonormal basis. Haar weights are
used only for the separately labeled inherited full-grid Haar baseline.
This does not assert that AC's data have equal variance, repeats, equal
site cost, or product-Chebyshev prediction measure. Those are explicit
hypothetical comparison assumptions. A weighted leverage objective will
not silently substitute for physical iid noise risk or row-l1 amplification.

Retain all four rule records, including failed/deferred outcomes:

|Provisional idea|Rule and closest predecessor|Separation / cheapest falsifier|
|---|---|---|
|IDEA?padua-3d-20261106-prune-A|Backward A-optimal deletion: minimize increase of tr((A^T A)^-1). Known backward design / inherited OLS risk.|Current support score, not frozen QR. A fresh QR map must agree with predicted risk and reproduce polynomials; failure invalidates the numerical path.|
|IDEA?padua-3d-20261106-prune-D|Backward determinant deletion: minimize current leverage h_i. Known backward D-optimal design / approximate Fekete.|Different objective from A: minimize determinant loss, not iid integrated variance. Identical observed paths remain equivalent finite outcomes, not distinct gains.|
|IDEA?padua-3d-20261106-prune-random|Seeded random deletion among currently rank-admissible rows; control only.|Same initial nodes/count/solver; no optimization claim. Rank failure is retained rather than repaired by a quality-driven restart.|
|IDEA?padua-3d-20261106-prune-lex|Canonical-order rank-admissible deletion; deterministic control only.|Separates score benefit from deleting any rows. It is not T10's boundary priority rule.|

For full-column-rank current A and raw row a_i, G=A^T A,
h_i=a_i^T G^-1 a_i, u_i=G^-1 a_i, deletion is admissible only when
1-h_i>1e-10. A's score is ||u_i||²/(1-h_i); D's is h_i.
Finite near-ties within 1e-12*max(1,abs(best score)) choose the smallest
original canonical node index. Controls use their frozen priority order
restricted to admissible rows. No query/function/noise realization selects
a deletion. The common hypothesis and exact identities are recorded in
root's separate pruning theory; floating scores are engineering heuristics.

## P1: bounded small-degree path and implementation discrimination

Question: do backward A or D deletion provide a useful finite count/noise/
amplification frontier at degrees **4,6,8**, enough to justify one retained-rule
larger-degree transfer? This is one research round, not one per degree/rule.
Start each rule from the identical anisotropic parity grid
m=(n,n+1,n+1), in inherited canonical order. N=binom(n+3,3).
Random priority seed is 2026110900+n. No restarts or seed search.

Run each path down to N if all numerical rank/update guards permit.
Report every deletion's count, predicted/fresh risk as applicable, elapsed
construction CPU, and training amplification. These are **diagnostic curves**:
continuing past the operational quality boundary does not recommend those
points. An active recommendation stops at the smallest count in the
initial connected quality-preserving prefix; later re-entry is retained
only as diagnostic information. No exact-N endpoint is forced if guards fail.

Training set is 128 angular Sobol points with seed2026110910+n, union
with the eight cube corners. At each deletion record actual physical map
row-l1 amplification on that fixed set. The operational prefix requires
training amplification <=1.25 times initial OLS training amplification
and optimal integer-repeat risk at fixed B=M_start <=1.10 times initial
OLS risk. Selection uses only these construction/training quantities.
Record the first failing count and all later diagnostic outcomes.

Use economic Householder QR initially and scipy.linalg.qr_delete row
downdates. Compute the physical map by a triangular solve after every downdate;
use its actual columns for A scores and Q row norms for leverages.
No formed Gram inverse or inverse-update heuristic is used. Refactor at
least every16 deletions, and at every assessment checkpoint.
Fresh factorization reconstructs the physical map C=R^-1 Q^T. Before
quality, require distinct cube nodes, positive singular minimum,
condition2(A)<1e10, ||CA-I||_infinity<=1e-8, QR reconstruction relative
infinity residual<=1e-10 and orthogonality infinity residual<=1e-9.
At refactors compare the downdated map/risk against fresh QR (relative
map Frobenius error<=1e-7; risk relative error<=1e-7); retain any failure and
stop that path, without relabeling singular subsets as feasible designs.
Fresh recomputation supplies all reported checkpoint risks/quality.

Checkpoints: full start; ceil(1.30N), ceil(1.20N), ceil(1.10N),
ceil(1.05N), N where <=M_start, deduplicated; and the selected operational
prefix. Every per-deletion training/count/risk curve stays in raw output.
The compact receipt contains complete checkpoint norm/noise/guards,
per-checkpoint aggregate target regressions and selected decisions. Every
individual target/measure/sigma table is retained in hash-inventoried raw
regenerable output; no logical test is split across receipts to evade16KiB.
The complete compact logical object may use reversible zlib/base85 encoding.
Full precision raw margins, all regressions, and decisions remain inspectable.

## Comparators, held-out quality, noise, and costs

Every checkpoint uses the same held-out query sets, generated only for
assessment: nested angular Lobatto21^3 and41^3; 2048 fresh angular Sobol
points (seed2026110920+n); 2048 fresh uniform Sobol points
(seed2026110930+n). Include both maxima by query family and their union.
Norm values are lower samples, never certified continuous suprema.
Do not select a deletion, rule parameter, or stopping count using held-out
queries. All measured deterministic errors and regressions remain visible.

Compare full-grid OLS and Haar; restricted QR from the same starting grid
(first k pivots of QR(A^T), with inherited unscaled selection basis), at
each checkpoint count; global QR on inherited Lobatto(2n+1)^3 at N;
and one unchanged inherited full localdet sweep from global QR at N.
Restricted QR is retained as a previously unsuccessful known control,
not offered as a new method. QR prefixes beyond N use the actual complete
SciPy pivot permutation, without a quality-selected extension.

Function set is the twelve frozen U1-continuation targets (including its
four original targets), all evaluated on both fresh measures. Record
per-target maximum and RMS error on each measure. For iid mean-zero
unit-variance physical-observation noise report tr(CC^T), which cannot
improve on deleting a row in exact OLS, and measured pointwise noise
variance max on each held-out query family. Report also M*tr(CC^T) as
the ideal-balanced effort coefficient, explicitly **not** an integer
allocation at B=M_start. For feasible common integer B=M_start, allocate
at least one repeat/site greedily by actual squared C-column norms;
report exact integer repeat counts, sum and risk sum_i||C_i||²/r_i.
This uses repeated independent measurements with the fixed map, not a
covariance-aware refit. Noise sigma in {0,1e-4,.01,.1,1} gives calibrated
expected integrated MSE = empirical Chebyshev bias² + sigma²*integer-risk;
all targets/settings are reported, with no claim of unknown-function
bias estimation. Keep unit-noise and equal-budget conclusions separate.

Record process CPU and wall costs for node generation, basis/initial QR,
score selection, downdates, refactors, training, checkpoints/map setup,
complete construction, and held-out assessment. Include common starting
cost and checkpoint I/O in construction. Record source/input SHA256,
commands, actual start/end UTC, Python/NumPy/SciPy versions, seeds,
OPENBLAS/OMP/MKL threads=1, and source snapshots/raw inventory hashes.
Use a root-granted exclusive CPU window for timed construction/comparators.
Raw coordinate/map/curve arrays go to a unique /tmp directory and are
regeneration-only; the stored455-node artifact remains unchanged.

P1 total execution allowance:900 process CPU seconds including all pilots,
controls and assessment. Check at operation boundaries, retain actual
completed overshoots, and mark unrun work explicitly. A cap hit is not
convergence or an automatic license to rerun a cheaper variant. Output
compact evidence/pdpr-pilot.json (<16KiB), with full raw details/inventory.

## P1 continuation gate and planned command

Numerical pass requires every retained A/D checkpoint map pass guards
and no score-update verification failure. A rule earns larger-degree
consideration iff at **both n6 and n8** its selected connected prefix
removes >=10% of starting nodes, has held-out union amplification <=1.30
times initial OLS's, and integer-budget risk<=1.10 times initial OLS's.
Additionally at one of those degrees it improves either equal-budget
risk or held-out amplification by >=5% over **both** random and lex
controls at the same selected count; the other metric must be no worse
than1.10 times each control's. Recompute those same-count control maps
from their existing trajectories; do not alter their deletion orders.
Degree4 is implementation/pattern evidence, not the useful-transfer gate.

If both pass, choose the one with smaller worst n6/n8 integer-risk ratio
to the full OLS baseline, ties within1e-8 to A. This is explicitly a pilot-
calibrated rule choice, not unseen-function validation. Preserve the other
rule and all failed endpoints. A pass permits a separately published
retained-rule **degree12** transfer (with degree8 reproduction), followed
by degree16 only if that transfer passes. New objectives/constraints,
weights or mechanism changes require a separately gated/registered round.
A fail stops these specific paths; root may register a genuinely distinct
promising question from actual evidence, without spending unused slots
as a quota. No larger-degree run is authorized by this paragraph alone.

Planned after root publication and CPU-window release:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/pdpr_run.py --round pilot --protocol-commit <published-sha> --scratch <unique-new-dir> --output topics/padua-3d-20261106/evidence/pdpr-pilot.json`

Engineering synthetic-matrix update/QR checks precede science and count0.
Their separate receipt records actual commands and does not claim a
consequential independent rerun. Root coordinates independent review.
