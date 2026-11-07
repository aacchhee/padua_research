# U2 continuation — prospectively frozen protocol

2026-11-07. Rules/input `97c323bfae15cf3c76f40802c3ebabedceeb0c60`.
Codex developer, assigned gpt-6.1-sol high; provider runtime metadata
unexposed. Root alone owns Git and shared records. AC authorizes up to
seven **further** U2 rounds; this is a ceiling, not a target. Historical
U2 rounds R1–R3 stay immutable. Only C1 (historical R4) is allocated now.

## C1: unchanged bounded-rule degree14 transfer/cost test

Question: at a hard limit of N=binom(17,3)=680 distinct sites, does the
already registered U2-AB recipe retain a useful norm gain at degree14
within its original budget? This changes no mechanism, objective, start,
parameter, or quality threshold. The prior novelty gate and closest
predecessors are in usable2.md and usable-gate.md. This numerical
extension makes no novelty/priority claim, so no new candidate generation
or full new-mechanism gate is invoked. Read AGENTS/WORKFLOW/CODEX,
current LOG continuation, usable2, handoff13, interim audit and U2/strategy,
the inherited code chain and fresh-assessment/cost-control implementations.
The degree12 audit (26.007323 versus comparable-cost localdet48.583269)
is a known premise, not a fresh transfer result.

Freeze degree14 only, inherited unscaled-basis QR from Lobatto29^3 and
its exact pivot ordering, one unchanged full inherited localdet sweep,
and existing lower-set Leja. U2 starts at that one-sweep localdet set.
Its training is angular Lobatto21^3; epsilon1e-8, beta40/L0,
separation-scaled projected gradient, coordinate cap r/(8 sqrt(3)),
Neumann rho<=1/2, Armijo1e-4, 25 backtracks, gtol1e-7, ftol1e-10,
200 accepted steps, no restart, as in u2_admissible.py. Select the
accepted within-budget iterate of lowest training maximum; never use
assessment for selection. Original1e-4 fallback and numerical guards
(unscaled condition2<1e12, inverse residual<=1e-7) remain.

Extra construction allowance is120 process CPU seconds. Start the
extra timer before constructing training basis E and before optimizer
initialization; training preparation, objective/gradient, guards, complete
trial checkpointing and final save are costs. Check cap before each
operation and after each completed trial. A trial completing beyond120
is retained but excluded from acceptance/selection; no interrupted
partial operation supplies a candidate. Save the last eligible accepted
prefix and report actual elapsed including overshoot, checkpoint I/O and
final guard costs separately. A cap hit is unfinished, never convergence.
The strict inherited cost gate passes only if the full extra construction
(including final guards/recording) is <120 and no CPU-cap hit occurs.
A step-cap hit is also unfinished but can pass that finite cost gate.

The matched-cost control starts from the **same** one-sweep localdet
nodes. Repeat the identical unchanged full inherited exchange(...,
limit=None), including basis/inverse and sweep checkpoint costs. The
budget is min(120, actual U2 extra CPU), fixed from construction before
assessment. Choose the last complete within-budget sweep prefix,
regardless of quality; retain the first over-budget completed sweep but
exclude it. Stop at that overshoot or a zero-exchange complete sweep.
The initial prefix is eligible if no further full sweep fits. Include QR
and initial localdet costs in total cost for both leads. Leja and map
setup costs are separate. Timing is single-thread and coordinated with
root to avoid other timed candidates. Timings are same-machine process
measurements, not hardware-independent or randomized trials.

Freeze fresh seeds2026110781 through2026110785. Each of the five square
sets (QR, Leja, localdet, U2, matched-cost repeated localdet) receives
65,536 new angular-Sobol interior points, 4,096 angular-Sobol points
on each face, and2,049 equally angular spaced points on each of twelve
edges, including corners (114,700 total). Physical-coordinate
L-BFGS-B maximizes the cardinal row-l1 norm from24 separated best
interior points,12 from each face and the combined edges, and32 random
cube starts (up to140 starts). Select starts by this frozen assessment
rule only, never nodes; retain every failed status and initial/final
value in raw. Report the largest sampled/searched value as a lower
sample, never a supremum certificate.

Use32,768 fresh uniform and32,768 fresh product-Chebyshev queries for
all original four functions and all six interim-audit functions, retaining
duplicated abs(x+y+z)/3 once (nine total). These functions and old results
are known; the new queries and candidate degree are fresh, not an unseen
function-design claim. Record max/RMS for every function/measure and
all regressions. Record16 fixed Rademacher1e-6 noise draws, their max/RMS,
orthonormal iid coefficient-risk trace and N*trace, condition numbers,
reproduction residual and log determinant. No error/noise ranking selects
nodes. New map assessment independently constructs normalized Chebyshev
basis and solves in it; source chain remains pinned.

C1 passes the useful-transfer gate iff the candidate has680 distinct
cube nodes, satisfies guards, searched norm<=.95 times **both** one-sweep
and matched-cost localdet searched norms, and passes the strict extra
cost gate above. Preserve each failed component. No extension is automatic:
a failure parks this unchanged120-second degree-extension recipe. Another
round requires a genuinely distinct prospectively registered reason after
review; unused slots alone are insufficient. Full new-mechanism novelty
gate applies if the update, objective or construction mechanism changes.
No all-degree, convergence or general error/noise superiority is claimed.

## Execution and evidence

Implementation files code/u2c_*.py; compact evidence/u2c-*.json receipts
(each<16KiB, no splitting to evade limits). One new unique /tmp raw
directory per execution, regenerate-only until AC chooses archival storage.
Store raw nodes/trajectories/full searches, hash inventory and byte sizes.
Record exact commands, code/data hashes, input head, versions, threads,
seeds, selected/excluded prefixes, costs and all outcomes. Do not hash-pin
this prose as a checker input; root's commit/publication identifies it.
Consequential independent rerun/review is root's separately assigned task;
no developer self-approval is asserted.

Planned command:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2c_transfer.py --scratch <new-unique-dir> --output topics/padua-3d-20261106/evidence/u2c-transfer14.json`

Other six further-round slots remain unallocated until C1 is assessed.

## C2 prospective append — training-only shorter-budget calibration

2026-11-07, after C1's actual degree14 outcome. C1's full120-second
recipe fails its strict cost gate and remains failed; its implementation
deviation is canonical in u2-continuation.md. Its searched norm benefit
is strong, which motivates this distinct allocation question: can a
shorter fixed accepted-step cap be selected using **training/cost only**
for a new higher-degree test? This does not change the objective/update
mechanism or claim historical novelty. It is a known stopping-schedule
variant, closest to the existing U2-AB. It is not an unseen-data claim:
C1's whole result is known, and before this registration the developer
inspected training/cost prefixes50/80/100/150 (including80 at57.1465CPU).
No new prefix quality is inspected or used in this calibration.

Count C2 as one adaptive research/calibration round only when this
registered analysis actually executes. It constructs no new optimizer
trajectory, proves no runtime bound and does not convert any recorded
prefix cost into a complete construction-cost pass.

Freeze candidate caps K={40,60,80}, target degree16 N969. For each K,
read only C1's source-pinned raw trace and select the accepted iterate
with the smallest **training** maximum among iterations0..K, preserving
the original fallback. Verify prefix geometric/accepted-Neumann/Armijo
invariants and the selected nodes' numerical condition/residual guards.
No fresh norm query, function error, or noise statistic enters this rule.

Let t_K be the recorded CPU at completion of accepted step K, which
includes all prior training preparation and trial work but not the later
complete trajectory flush. Compute the deliberately conservative heuristic
forecast T_K=(t_K+2)*(969/680)^3. The added2seconds is a reserve for
final recording/guards; cubic dimension scaling is a planning heuristic,
not a proved cost bound. A schedule is eligible iff its training maximum
is <=0.8 times C1's initial training maximum, numerical/invariant guards
pass, and T_K<=100 CPU seconds. Choose the largest eligible K, with no
quality-based choice. Preserve all candidates and their failures. If no
K qualifies, park the shorter-schedule route; do not add another K.

If and only if C2 passes, prospectively register C3 before execution:
apply the selected **fixed K** from scratch at new degree16, unchanged
U2-AB objective/update/start and all controls, new assessment seeds/clouds,
full costs, matched-cost repeated localdet and original5%/120-second
quality/guard/cost gate. C3's real cost gate, not this heuristic forecast,
decides feasibility. No automatic further round follows a C3 failure.
The changed schedule is explicitly calibrated, not an unchanged200-step
transfer or unseen stopping-parameter choice.

C2 command as planned:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2c_calibrate.py --receipt topics/padua-3d-20261106/evidence/u2c-transfer14.json --output topics/padua-3d-20261106/evidence/u2c-calibration.json`
