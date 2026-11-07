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

## P2 prospective appendix — exhaustive constraint-aware raw amplification

2026-11-07, after P1published at
ccab7af1ac38a6e8ec83b5d254a9260f0d57ea64. P1consumes1/15 and fails its
strict useful-transfer gate, including exact-N comparisons against the
stronger inherited controls. There is no operational-quality re-entry in
its existing full curves. Noise alone permits A only5.36%/4.89%site saving
at n6/8 under the10%fixed-B risk allowance. These observations motivate a
distinct, cheap constraint-aware deletion question, not a threshold change.

Candidate IDEA?padua-3d-20261106-prune-L: known backward deletion choosing
raw-value amplification among **all currently feasible one-row deletions**.
The closest P1A/D rules optimize noise/determinant alone; the separation is
the actual raw-cardinal objective and feasibility search. The existing
pruning gate clears this as a known variant with no priority/new-algorithm
claim. Kill test: exhaustive finite search stops with no feasible deletion,
or the useful gate below fails; do not call that a theorem about all subsets.

P2is **one** research round at n6/8, canonical identical starting grids,
physical unweighted OLS, same iid/measure/repeat assumptions and numerical
thresholds as P1. Training changes explicitly to angular Lobatto9^3
(including all faces/edges/corners) plus256angular-Sobol points, seed
2026111010+n. This declared dense training is calibrated after observing
P1's training undersampling; no unseen-parameter selection is claimed.
The quality-preserving noise/amplification thresholds remain1.10/1.25
relative to each new training full-OLS baseline; useful held-out and
site-saving thresholds remain1.30 and10% respectively.

At each state with map C, Q and training cardinal matrix L=EC, form the
physical hat matrix H=QQ^T. For every current row i with d_i=1-H_ii>1e-10,
compute **all retained columns** by the exact raw-cardinal deletion formula

`C^-_j = C_j + C_i H_ij/d_i`, j!=i,

`L^-_j = L_j + L_i H_ij/d_i`, j!=i.

For each candidate compute max training row-l1 and actual integer-repeat
risk at fixed B=M_start from its full C^- columns. Feasible means both
<=1.25*initial training maximum and <=1.10*initial unit-noise/full-budget
risk, with finite arrays. First filter **every** rank-admissible candidate
by both constraints, then choose the smallest training maximum; near-ties
within1e-12*max(1,abs(best)) choose the smallest original canonical index.
Do not choose an infeasible best-amplification row and stop while another
candidate satisfies both constraints. Record all candidate scores, feasible
counts, chosen IDs and rejection reasons at every step.

Before accepting the chosen deletion, recompute its map by fresh
Householder QR, check the original distinct-cube/rank/condition/reproduction/
QR guards, compare its map with the predicted C^- (relative Frobenius
<=1e-7), and recompute both constraints using that fresh map. If a trial
fails these checks, retain it as numerically rejected and try the next
candidate in the frozen score order; no parameter/seed repair. If the
predicted feasible list is empty, or every entry is numerically rejected,
stop and retain that exact scope/reason. This is a finite floating-rule
stopping claim, not exact infeasibility of any subset. If rank N is
reached, stop there. There is no diagnostic continuation after a constrained
stop in P2. Consequently N need not be reached or recommended.

Fresh QR supplies each accepted state's map, risk, integer repeats,
training norm and guards. The exact deletion identity is checked using
synthetic rational/real matrices before P2science (0rounds). The aggregate
selection rule receives branch checks including the case where the lowest
amplification candidate violates noise but another row is feasible.
The stored raw candidate table permits a distinct independent finite
feasible-set replay. Fresh guard disagreement is never hidden as a
quality success or an exact 'none exists' conclusion.

Assess full support, every reached standard P1count checkpoint, and the
terminal support. Fresh held-out sets keep P1's21^3/41^3nested angular
meshes and2048query sample sizes, but use new Chebyshev/uniform seeds
2026111520+n and2026111530+n. They do not select deletions/stops. Reassess
P1A/D/random/lex trajectories at P2's terminal count using P1's pinned
path-index arrays, keeping their original canonical order and all prior
failures. Full OLS/Haar, same-count restricted QR, and freshly constructed
globalQR/one-sweep localdetN controls are included. Every map gets the
same fresh queries and all12frozen targets, every noise/sigma report,
raw regression retention and actual setup/assessment cost split as in P1.
A/D path costs are labeled historical P1costs; globalQR/localdet and
PRUNE-L construction costs are contemporaneous fresh measurements.
No equal-time advantage is inferred from historical cost numbers.

P2passes its **unchanged strict quality/count goal** iff both n6/8terminal
maps pass guards, save>=10%starting sites, have held-out union norm<=1.30
full OLS, and integer-budget risk<=1.10full OLS. Additionally, at either
degree a **common metric** improves>=5%over both random and lex at the
same terminal count, and the other metric is <=1.10both. A/D and restrictedQR
comparisons are reported even when unfavorable. A cap or missing mandatory
comparison fails transfer eligibility. Failure stops this strict-goal
variant; it does not erase a finite constrained frontier or prove no
other subset can meet the goal. A distinct later matched-count/Pareto
question needs a new prospective justification/gate/publication.
No degree12/16run follows automatically from P2. A success permits a
separately registered transfer with the same retained rule and thresholds.

P2allowance600process CPU seconds including construction, controls and
assessment, operation-boundary checks with completed overshoots retained.
Root grants the exclusive timed window after publishing this appendix.
Persist actual started/ended UTC in raw before compact collection. Use
one complete compact logical receipt (<16KiB) via the corrected XZ/six-
significant-digit summary collector, with every full precision individual
result/raw/source identity retained; the P1serialization note stays canonical
in pruning-results.md. No split receipts to evade the limit and no source
identity relabeling. Original P1scientific/collector versions stay available
at ccab7af1and their recorded hashes.

Planned command after publication/review/CPU release:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/pdpr_run.py --round constrained --protocol-commit <published-P2-sha> --reference topics/padua-3d-20261106/evidence/pdpr-pilot.json --scratch <new-unique-dir> --output topics/padua-3d-20261106/evidence/pdpr-constrained.json`

## P3 prospective appendix — calibrated near-minimal tradeoff transfer

2026-11-07, after P2complete output was published at
d57b2b17a04418bb90f554b61a4ed61a6f444a0b. P1andP2consume2/15 and both
retain their failed strict full-grid-preservation gates. The10%noise and
1.30norm ratios were research tolerances, not user-supplied requirements.
P3explicitly asks a different matched-count tradeoff question; it does not
relax those old gates into a pass.

Existing n8P1data calibrate this test: at M198=ceil(1.20N), A has sampled
amplification20.39185/fixed-B225risk0.905549, against same-count restrictedQR
25.23022/1.030698; localdet at N165 has23.97261/1.167425 and full OLS225
has7.87067/0.709997. Thus a near-minimal support may offer lower noise and
amplification than tested minimum-count controls at the cost of33additional
sites. Individual function regressions and the much better full-grid
amplification remain explicit. No mathematical Pareto optimality is claimed.

Candidate IDEA?padua-3d-20261106-prune-Pareto: the known A deletion rule
at a **prespecified absolute count**, under a changed operational objective.
The gate/next-questions note clears this as finite matched-count research,
not a new method. Choose A by its already known lower noise at198sites;
D's alternative remains recorded, not retested on unseen n12then selected.
The falsifier is failure of the new fixed-count gate against strong controls,
especially the stored modern455-node U2set, not a favorable target/charge
chosen after seeing n12results.

P3is one round comprising an n8known-path reproduction and an unseen
**degree12transfer**, N455/start M637. Use the identical canonical grid,
physical unweighted OLS, A score/ties/rank guards/QR downdates/refactors
from P1. A deletes to N for diagnostic count/risk curves if numerical
checks permit. The primary operational support is **ceil(1.20N)** (198/546).
Also assess ceil(1.10N) (182/501), N (165/455), and full start; no held-out
choice changes the primary count. The old strict-prefix stopping point
is recorded only as the failed P1-style diagnostic, not P3selection.
No temporary training-norm constraint enters this fixed-count A path.

At every assessed count, save the actual node IDs, coordinates and fresh
validated physical map before proceeding, charging flush/checkpoint costs.
Record complete prefix construction CPU/wall immediately after this final
validation/checkpoint. Also record the actual full-to-N diagnostic cost;
do not charge all later diagnostic work to the usable prefix or report an
uncheckpointed early timer as complete construction cost. The prefix must
include starting-node/basis/QR preparation and all previous operations.
At n8the complete retained-index trajectory must equal P1's pinned path;
any disagreement fails reproduction, without reseeding/repair.

New held-out Chebyshev/uniform seeds are2026111920+n/2026111930+n,
2048queries per measure. Keep nested21^3/41^3angular meshes. To challenge
coarse-mesh rankings, every map additionally gets the **same** angular
L-BFGS-B row-l1 refinement rule: four largest41^3sample points, eight
corners, and16new angular-uniform starts (seed2026111940+n),28starts total.
Use inherited analytic angular derivatives and original maxiter200/maxfun5000/
ftol1e-12/gtol1e-8; retain each initial/final value and solver status. Return
the maximum of all held-out samples and every initial/final search value.
This is a sampled/searched **lower value**, not a certified supremum.
Queries/searches never select deletions, rules or counts.

All maps get the same queries/functions/noise/cost definitions as P1/P2:
12known targets on both measures, pointwise unit-noise variance by query
family, unit-noise trace, M*trace, feasible actual integer repeats at
B=M_start (225/637), every sigma/target calibration table and every
regression. Every same-count restrictedQR prefix uses the identical
canonical pool and unscaled QR pivot basis. Include newly constructed
full-grid OLS/Haar, globalQR at N and one-sweep localdet at N. At n12,
**decode and verify the unchanged committed455-node U2payload**, assess its
actual physical map on the same fresh queries/searches, and retain its
complete original source/payload identity. Its existing exact unisolvence
proof is separate from the fresh measured norm/error results. Report its
load/map cost and link original offline construction cost rather than
pretending the saved artifact requires optimization again.

P3's practical transfer gate, evaluated at primary M=ceil(1.20N), requires:

1. Successful n8whole-path reproduction and all retained numerical guards.
2. At both degrees, >=10%site saving from the full starting support; primary
   complete prefix cost<=120process CPU seconds and no missing/capped work.
3. At both degrees, **both** integer-budget risk and sampled/searched
   amplification <=0.95times same-count restrictedQR.
4. At neither degree may a tested minimum-count control dominate the primary
   point: a control at N has fewer sites already, so domination means its
   integer-budget risk and sampled/searched amplification are both <=the
   candidate (relative equality tolerance1e-10). Compare globalQR/localdet
   at both degrees and storedU2at n12. Cost is shown separately, including
   saved-artifact advantages; no universal setup/application/error winner.

Retain each failed component, all function/noise regressions, and the
old full-grid-preservation ratios. This gate supports only a finite
site/noise/amplification tradeoff, not a data-only unknown-target selector
or a global Pareto theorem. Diagnostic1.10N/Nfailures cannot be hidden by
the primary1.20Nsuccess, or vice versa. A failure stops this calibrated
near-minimal transfer variant; no degree/seed/count sweep is automatic.
A success permits a separately published degree16transfer and then a
compact canonical-ID artifact/exact-rank check if independently supported.
Reflection-pair/support experiments remain separate unallocated questions.

P3budget900process CPU seconds for both degrees, diagnostic construction,
controls and assessment. Root grants an exclusive window after publication/
focused code review. Retain completed operation overshoots, explicit unrun
work, UTC start/end/source/input/version/thread identities and one complete
compact receipt (<16KiB) with full precision hashed raw tables, as in P2.
The exact n12stored455payload remains unchanged. No scientific execution
precedes this prospective publication.

Planned command:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/pdpr_run.py --round frontier --protocol-commit <published-P3-sha> --reference topics/padua-3d-20261106/evidence/pdpr-pilot.json --scratch <new-unique-dir> --output topics/padua-3d-20261106/evidence/pdpr-frontier12.json`
