# U3 continuation protocol — complete nonunique septic diagnostic

Rules/input: `97c323bfae15cf3c76f40802c3ebabedceeb0c60`, 2026-11-07.
Codex assigned gpt-6.1-sol xhigh; runtime metadata unexposed. Root owns
publication, Git, counts and independent review. This protocol must be
published before scientific execution. AC's current ceiling is **seven
further U3 rounds**, not a requirement to spend them. The starting completed
count is four; this diagnostic is one possible additional round.

## Question, scope and predecessor

Does the complete set of 28 already identified degree-seven full-rank
nonunique-support half-shifts contain a numerically competitive interpolant?
This is the exact retained question in [interim U3](interim-audit-01/U3.md)
and handoff13, completing an unmeasured portion of the existing family.
It introduces no new mechanism, partition, phase, determinant schedule or
selector. The four frozen S/F/M/R selectors remain parked. No historical
novelty, priority or asymptotic claim is proposed.

The published [shared gate](usable-gate.md) personally read every IDEAS
entry/table at the unchanged registry identity
`d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef`.
That existing gate is the whole-registry gate for this retained mechanism;
the present worker does not claim a new literal full-registry read. Its
personal relevant reading and source limits are recorded in
[continuation](u3-continuation.md). A genuinely new mechanism would require
its own complete gate before generation.

## Complete frozen candidate domain

Let n=7, N=120, theta_k=(2k+1)pi/240 for k=0,...,119. For each z=(1,b,c)
below use X_z={(cos(theta_k),cos(b theta_k),cos(c theta_k))}. Every tuple
label is assessed, even if several labels represent equivalent physical
sets. The frozen list is every n7 row of the already published
[block receipt](interim-audit-01/evidence/ia3-blocks.json):

```
(13,98) (13,142) (16,93) (16,147) (17,28) (17,212)
(26,37) (26,203) (28,223) (37,214) (44,113) (44,127)
(66,85) (66,155) (76,99) (76,141) (85,174) (93,224)
(98,227) (99,164) (113,196) (127,196) (141,164) (142,227)
(147,224) (155,174) (203,214) (212,223)
```

The code asserts exact equality with this list before quality. Each tuple
inherits the candidate record below. No subgroup, determinant, inverse sum
or subsequently observed norm selects a subset. All 28 cases are completed
even after an early loss; incomplete scope is reported as incomplete.

## Count, rank and numerical validation

Before any quality for a tuple, reconstruct its rational folded angles,
check exactly 120 nodes, and check actual cosine evaluation at two verified
splitting primes using the frozen inherited routines. The exact count and
coherent half-period action are unchanged from the existing proved
[half-shift theorem](theory/t8-r08-halfshift-obstruction.md). Also reconstruct
the integer C/8 alias matrix and verify its exact rational inverse against
identity. Compare exact S and inverse infinity norm to the audit receipt;
these are cross-checks, not competitive norm bounds.

Measure the inherited **unscaled** product-Chebyshev V condition number and
infinity norm residual of V V^{-1}-I. condition2>=1e12, nonfinite values or
residual>1e-7 suppress quality and fail this numerical gate. Otherwise
evaluate the complete 21^3 and 41^3 tensor Lobatto meshes, with inherited
mode order and physical coordinates. Recompute inherited ordered QR on
(2n+1)^3 Lobatto candidates and the inherited discrete-Leja lower set on
n+1 axes. Use the same source routines for every candidate and control.
Retain both mesh values, maximizers, condition/residual and all certificates.
No new continuum maximization is needed for this bounded diagnostic.

## Prospective quantitative success and stop rule

Success requires **one identical tuple** passing numerical validation and
matching or beating same-degree QR on **both** meshes. For each tuple retain
q(z)=max(L21(z)/L21(QR), L41(z)/L41(QR)); q<=1 is the competitive gate.
Also retain both Leja ratios, every unfavorable outcome and the minimum q
only as an all-domain descriptive statistic. Choosing a good tuple after
quality does not constitute a new prespecified practical selector.

If no tuple passes, stop this complete degree-seven nonunique half-shift
quality route. The result excludes neither unseen odd degrees, arbitrary
phases, other generators/folds nor mixed families. Large inverse sums are
not lower bounds; a measured norm loss supplies no asymptotic theorem.
A second round is considered only after this gate supplies positive
quantitative evidence or a separately specified useful inverse bound.
Higher-degree extension still requires structural reason and competitiveness
at two successive largest feasible degrees under a new prospective scope.
No automatic higher-degree or changed-partition run follows from one pass.

## Execution and evidence

Run only after root publication and CPU coordination (U1/U2 timed work has
priority). One thread per BLAS/OpenMP library. No seeds/random sampling.
The finite scope is the resource cap; record complete elapsed and CPU time.
The code writes a unique /tmp directory with all raw rows and source
snapshots, hashes and lengths. These are regenerate-only, not archival
deliveries. The one compact receipt is below16KiB; no split evades limits.
Code/input/receipt hashes and Python/NumPy/SciPy/SymPy versions are recorded.
No prose is a checker acceptance pin. Actual command, from repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u3c_nonunique_quality.py --receipt topics/padua-3d-20261106/evidence/u3c-nonunique-quality.json
```

Independent reconstruction/rerun is a distinct remaining obligation; this
developer execution alone yields MEASURED finite results. No extra round
is charged for such verification.
