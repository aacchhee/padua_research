# Preregistered finite phase projection probe

Rules `2fb2f7502bb8d1b46c0fe1089588c46a06df258d`; technical developer
gpt-6.1-sol medium. Before running, retain **rho1=.1** from the phase probe,
chosen from the inherited S-excess peak near .06. Use the same 49 distinct
phases: rho=0,.01,.03,.06,.1,.2,.3 on both signed axes and four signed diagonals
with rho=|alpha|+|beta|. Degrees are n=48,96,192. This is finite floating
sampling, with no continuum phase bound or gate pass.

The structure-gates worker supplied and verified the pair-profile formula.
Precompute H_rs=G((r*pi+alpha)/n,(s*pi+beta)/(n+1)) on the odd torus.
For N=n(n+1), sum the pair defect
`abs(H)+abs(H_reflected)-abs(H+H_reflected)` over that torus and divide by
4N: reflect s about K for Qv(K), or r about J for Qh(J), modulo the respective
even periods. Fixed points contribute zero. The mathematical triangle
inequality gives max(Qh(J),Qv(K))<=Delta for every admissible odd center (J,K).
Floating values of this expression are diagnostics, not certified lower bounds.

Plan: validate both projection profiles against the independent cosine-polynomial
lambda path at n=3,4,5,6,17, including endpoints/fixed points. Then enumerate
all physical-admissible odd centers at every sampled phase for the three A2
degrees. Preserve exact distance classes (dJ,dK) in local raw output and commit
only compact extrema, timing and input/output identities.

## Executed result

Executed once with the preregistered schedule:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/projection_probe.py
```

The [12,604-byte evidence receipt](evidence/projection-probe.json) pins the
compile command, compiler/Python/NumPy/platform versions, all four source-file
identities (including the inherited phase-probe implementation), raw output
identities, validation summary and grouped extrema. The C code received a
`-Wall -Wextra -Wpedantic -fsyntax-only` check without diagnostics. Every
recorded source/raw SHA-256 and byte count was verified after execution.

The independent cosine-polynomial path validated 262 admissible samples at
n=3,4,5,6,17, with zero and signed nonzero phases. Selected centers include
geometric endpoints, reflection fixed points, edge and interior centers. The
largest computed violation `max(Qh,Qv)-(S_direct-lambda_direct)` was 6.67e-15;
the maximum S disagreement was 1.25e-14. These are ordinary floating
residuals, with no numerical error bound. This developer cross-formula check
is not an independent agent rerun. No discrepancy beyond roundoff scale was
observed in the tested scope.

The phase-G torus is computed in O(n²) trigonometric work and stored once per
phase. Each Qh and Qv profile is then a sum of table lookups, additions and
absolute values. Computing all profiles costs O(n³) arithmetic and O(n²)
memory; the final center enumeration costs O(n²) per phase. Full lambda at
every center is neither computed nor claimed. The large-degree corner
reference Lambda_c is evaluated by the inherited C full-reflection evaluator.

| n | Distinct distance classes | Admissible center/phase samples | Wall / CPU (s) | Smallest sampled noncorner Qmax-(S-Lambda_c) |
|---|---:|---:|---:|---:|
|48|625|58,255|0.4107 / 0.4106|0.566547|
|96|2,401|229,399|1.9214 / 1.9213|0.557083|
|192|9,409|910,375|8.2281 / 8.2273|0.552633|

Here Qmax=max(Qh,Qv). Each degree has all 49 prescribed phases. At rho=0,
every odd physical center is included; boundary centers at nonzero phase are
restricted by the exact physical-angle inequalities. Thus both parity
orientations and reflected centers occur whenever physically admissible. The
smallest noncorner margin in the table occurs at alpha=beta=0 and (J,K)=
(0,25), (0,49), (0,97), respectively. It is an edge midpoint effect that the
earlier near-corner sampling alone would have missed.

The following are minimum computed projection values for the rho<=.1 sample
subset. They are **not** minima over the continuous phase region. An edge
distance is the nonzero member of (dJ,dK); for an interior center the grouped
distance is min(dJ,dK). "Rest" means distance at least four.

| n | Edge d1 | Edge d2 | Edge d3 | Edge rest | Interior min-distance rest |
|---|---:|---:|---:|---:|---:|
|48|2.272509|1.964523|1.742054|0.563218|0.982153|
|96|2.785269|2.333175|2.127451|0.553911|0.989824|
|192|3.313292|2.702603|2.524022|0.549603|0.993662|

The interior min-distance1,2,3 grouped minima equal the corresponding edge
distance1,2,3 entries to the displayed precision. Their full counts, minima
and sampled comparison margins are in the receipt. Corner Q profiles vanish
at the geometric fixed points; computed corner comparison margins as small
as -1.82e-13 reflect summation/subtraction error and establish no sign.

For each sampled phase the local raw JSONL records every represented exact
distance pair (dJ,dK), sample count, minimum computed projection, an attaining
center, minimum comparison margin and S excess. All classes and orientations
are enumerated rather than selected representatives. The summary combines
them only after enumeration. The JSONL is 115,058,253 bytes and remains
outside Git at
`local-output/argmax-effective-2-20261105/phase-probe/projection-classes.jsonl`;
the validation JSON is 82,154 bytes in the same directory. Both are hashed in
the receipt. Cold-storage transfer to AC is pending; the committed sources
regenerate both files.

This strengthens A2's finite coset sampling: the projection comparison has
positive margins for every noncorner center at each tested phase. It does
not establish A2's required class-wise lower bound on a continuum, and it does
not resolve corner descent, A1's box-count criterion, A5's continuous search,
or an all-degree claim. No inferred error bound, constant or gate pass follows
from the numerical margins. Sparse phase samples may still miss a shrinking
S-excess peak or a projection trough between samples.
