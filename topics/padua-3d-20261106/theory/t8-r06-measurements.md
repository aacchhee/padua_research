# PD-T?padua-3d-20261106-codex-T8-r06-05 — restarted cyclic witnesses and quality

ID kind: PD-T. Aliases: Phi1 finite witnesses; determinant-only F; cyclic
U2/U3/U4 quality screen; nearby-order half-grid diagnosis. Split from: none.
Split into: analytic parity, fold and union-obstruction results have their
own files and IDs; this record contains their separate measurements only.

## Statement, definitions and assumptions

The preregistered finite runs below produce the stated rational node sets
and fixed 21^3 tensor-Lobatto Lebesgue samples. Each positive selected set
has exactly N=binom(n+3,3) nodes and two nonzero exact finite-field
determinants. Selection maximizes a bounded search's orthonormal product
Chebyshev log absolute determinant; it never optimizes Lambda. 'Optimized'
means only that frozen local algorithm, not a global family optimum.

Overall status **MEASURED**; computed positive certificates and finite
censuses are not upgraded to computer-assisted PROVED without an independent
rerun. All quality values are floating sampled lower bounds, not certified
global maxima or asymptotic evidence. The broad minimal-polylog target is OPEN.

## Phi1: finite existence certificates on every parity-permitted degree <=12

The following witnesses all have M=N; phases are numerator vectors divided
by D. The analytic permission theorem is necessary only. These separate
positive finite certificates show existence at the listed degrees.

| n | N | z | phase numerators | D |
|---|---:|---|---|---:|
| 1 | 4 | (1,2,1) | (105,28,211) | 257 |
| 3 | 20 | (1,2,7) | (30,75,69) | 120 |
| 4 | 35 | (1,22,25) | (240,90,109) | 257 |
| 5 | 56 | (1,8,45) | (225,15,115) | 257 |
| 7 | 120 | (1,33,92) | (29,48,56) | 257 |
| 8 | 165 | (1,37,144) | (59,84,55) | 257 |
| 9 | 220 | (1,32,101) | (97,59,127) | 257 |
| 11 | 364 | (1,16,129) | (156,248,227) | 257 |
| 12 | 455 | (1,267,119) | (132,236,237) | 257 |

The search needed 13 trials in total, including four exact character-support
matching rejections, and no resource fallback. Per-degree measured costs
were .003,.003,.006,.008,.022,.043,.082,.379,.769 seconds. Matching
rejection is an exact support-rank obstruction for that generator, not a
degree exclusion. The largest degree certificate has rank455 at both primes.
These rank-only witnesses were not selected for quality and are not a
degree-uniform generator formula. n3 is the disclosed inherited audit control.

## Phi2: bounded determinant optimizer F and frozen D2 kill

| n | z | sampled Lambda | Leja | QR |
|---|---|---:|---:|---:|
| 3 | (1,16,5) | 19.793888 | 13.174720 | 8.320671 |
| 4 | (1,9,28) | 54.028747 | 19.498175 | 11.244878 |
| 5 | (1,8,11) | 71.879058 | 26.336615 | 13.857502 |
| 7 | (1,31,112) | 335.945252 | 49.812588 | 26.935072 |
| 8 | (1,97,12) | 727.556760 | 79.821347 | 43.886769 |

All five selected rationalizations pass exact count/full-rank certification.
The n4 QR loss excludes promising status. Eligible Leja losses at n7,n8
trigger the frozen D2 kill; n9/11/12 F quality was not run. Five rows and
four n>=4 rows cannot support the six-row growth fit. F is REJECTED: failed
under this empirical gate, without rejecting the continuous M=N family.
No new closed generator/phase formula was inferred or tested after failure;
the preregistered algorithm F itself was the uniform pattern.

## Phi3: full-orbit count and initial half-grid fallback

Generic rational phases gave M>N nodes in every tested nearby/2N-1 order.
The all-degree binary-mask fallback exhaustively tested b<c<M at n2:
N+1 had 360 candidates/0 exact-count passes; N+2 had 440/31; N+3 had
528/0; N+4 had 624/0. N+1/3/4 therefore fail their frozen selector at n2.
For N+2 the selected z=(1,4,9), mask(0,0,1), denominator24 has rank9:
its y values are 1 and -1/2, so 2y^2-y-1 is an exact nonzero quadratic
null; the modular rank9 lower bound matches it. At n3,M22 the complete
1,680 binary-mask candidates have no exact-count pass. This selector fails
there too. These are scoped count/rank outcomes, not all-phase exclusions.

For M=2N-1 the only exact-count binary-mask rows in this screen had zero
mask. Thus it found **no new translated construction**. Its n2/4/6/8
positive quality rows are inherited zero-phase baselines with sampled
Lambda 8.134069,45.715124,421.590753,676.678873. n3 is already covered
by the accepted H39 zero-phase obstruction; the modular sample is not a
reopened H39 conjecture. n5/7 modular deficiency is only a rank lower bound,
and no new exact negative is inferred there. All zero-mask diagnostics are
retained, without using them to claim a new phase family or D2 success.
The all-phase first-unit rigidity theorem now explains why this maximal
folding order leaves no continuous phase quality freedom at fixed generator.
Phi3b is a distinct prospective mixed-stratum continuation, with its own
starting degree and gate, rather than a revision of these failed rules.

## U2/U3/U4: independently translated cyclic cosets

| cosets r | tested n | sampled Lambda in that order | actual D2 kill |
|---|---|---|---|
| 2 | 2,3,5,6,7,9 | 7.101573,13.198139,121.189317,undefined,290.101685,768.826301 | n7/n9 |
| 3 | 6,7,8 | undefined,170.745168,492.877315 | n7/n8 |
| 4 | 3,5,6,7 | 19.983659,188.029232,137.483323,195.229975 | n6/n7 |

Each defined quality row is exactly certified. U2/U3 at n6 have exact node
count84 and modular rank82 at two primes; the separate common-half-period
theorem provides an analytic upper bound82. Undefined quality is intentional,
not a successful solve. Thus the no-fold common-even-order all-degree rules
already fail at n6; the subsequent admissible-degree quality diagnostics also
hit the frozen empirical kills. U4's M21,n6 set is full rank84: its odd
subgroup order escapes that sign action but gives no quality advantage.
Each r's bounded optimizer is REJECTED: failed by D2, with the broader union
class OPEN. Independent translations really leave the fixed PD-N034 phase
hypothesis; that escape alone did not supply good interpolation.

## Checks, sources, exactness and limitations

Commands: each prefixed `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python
topics/padua-3d-20261106/code/t8_r06_routes.py`, then respectively
`controls`, `witnesses`, `phi2`, `phi3`, `strata`, `union2`, `union3`, `union4`.
Every receipt evidence/t8-r06-<route>.json contains the actual command,
versions, rules SHA, source/helper hashes, rational nodes, primes, roots,
determinants, raw JSONL location/hash/size and per-degree measured costs.
Raw paths use fresh unique scratch directories. The 'samples' optimizer
field counts finite determinants, so e.g. n4 F's 63 records correspond to
64 random draws with one zero determinant. No cost budget bound was reached
in these initial routes. All scientific candidate parameters are deterministically
regenerable from the committed code and seeds; raw summary JSONL contains
the selected/result rows, not every transient optimizer evaluation.

Exact reduction: t8-r06-certification.md. Source comparison and reading limits:
literature-T8-round06.md. Special-stratum results are separate in
t8-r06-phase-strata.md. Root's independent checker is distinct and must
record executed reruns before any finite-status upgrade. No final IDs or
global registry changes are made. 2026-11-06, Codex assigned Sol xhigh,
rules/input7afa6a54; first restarted boundary prepared for root publication.
