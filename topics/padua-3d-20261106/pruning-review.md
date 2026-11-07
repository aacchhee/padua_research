# Pruning campaign — independent supplementary review

2026-11-07. Rules personally read at
`c7afc444fabab45081b087bdde583d5631a8d1a1`: AGENTS, WORKFLOW and CODEX.
Assigned distinct reviewer: Codex gpt-6-astra xhigh; provider runtime metadata
unexposed. Reviewer owns only this file and `pruning-review/`; no producer edits.

**Final disposition through P5 and the n12/n16 certificates:** no unresolved material
finding in the covered scope. Independent executions corroborate P1/P2's
failed P1/P2/P5 goals and P3/P4's registered fixed-count tradeoff passes.
The exported ideal-cosine n12/n16 sets have verified column rank455/969
at546/1163 sites. Rounded quality remains MEASURED.
This supplement does not replace formal Claude audit04 or confer readiness.
All reviewer/engineering/certificate checks consume zero research rounds.

## Scope and evidence

Read handoff16, pruning brief/gate/theory/protocol/results, relevant LOG
continuation, code dependencies and the certificate reduction, including
`theory/t8-r06-certification.md`. This is a mathematical normalization,
implementation, provenance and finite-execution review of registered known
methods. No complete IDEAS/literature gate was independently repeated here:
no novelty, priority, exhaustive predecessor or source-paper clearance is
supplied. The separate gate records that reading. Finite failures imply no
universal obstruction; numerical searches certify no continuous supremum.

The receipts below contain actual commands, complete code/input hashes,
versions, scopes, outputs and limitations. Their code/data pins remain in the
assigned auditor namespace outside the producer master. Raw scratch files
are regeneration-only, not archival delivery. Python3.12.14/NumPy2.3.5/
SciPy1.17.0 and one OpenBLAS/OMP/MKL thread were used for numerical checks;
exact rational algebra used SymPy1.14.0. Formal Claude review stays pending.

| Scope | Independent code | Compact evidence |
| --- | --- | --- |
| Manifest | [check_codec.py](pruning-review/check_codec.py) | [codec.json](pruning-review/codec.json) |
| Exact deletion algebra | [check_algebra.py](pruning-review/check_algebra.py) | [algebra.json](pruning-review/algebra.json) |
| P1 | [check_pilot.py](pruning-review/check_pilot.py) | [pilot.json](pruning-review/pilot.json) |
| P2 | [check_constrained.py](pruning-review/check_constrained.py) | [constrained.json](pruning-review/constrained.json) |
| P3 | [check_frontier.py](pruning-review/check_frontier.py) | [frontier12.json](pruning-review/frontier12.json) |
| P4 | [check_transfer.py](pruning-review/check_transfer.py) | [transfer16.json](pruning-review/transfer16.json) |
| P5 synthetic | [check_pair_preflight.py](pruning-review/check_pair_preflight.py) | [pair-preflight.json](pruning-review/pair-preflight.json) |
| P5 actual | [check_pair.py](pruning-review/check_pair.py) | [pair.json](pruning-review/pair.json) |
| Exact rank/delivery | [check_certificate.py](pruning-review/check_certificate.py) | [n12](pruning-review/certificate12.json), [n16](pruning-review/certificate16.json) |
| Repository-only rank replay | [check_cert_algebra.py](pruning-review/check_cert_algebra.py) | [n12](pruning-review/certificate12-algebra.json), [n16](pruning-review/certificate16-algebra.json) |

## Prospective findings and developer dispositions

All material findings were returned to development and reinspected before
science. No in-place MINOR producer fixes were made by this reviewer.

1. P1's first protocol described inverse updates while code used QR downdates
   plus triangular map solves. Checkpoint events also preceded fresh maps.
   The developer reconciled the protocol, moved fresh maps before events,
   added map/risk refactor comparisons, physical-node checks and cost fields.
2. **MAJOR, fixed:** the first control predicate allowed risk to beat one
   control and amplification to beat the other. It now requires one common
   metric to improve against both, with the other-metric bound preserved.
3. **MAJOR, fixed:** rounded worst-risk ordering did not implement the
   promised absolute1e-8 tie-to-A. The explicit absolute-difference rule does.
4. **MAJOR, fixed:** the numerical gate initially omitted degree4. It now
   checks all three degrees and assessed rule checkpoints.
5. P2's initially proposed assessment seeds duplicated already reported P1
   audit clouds. They were prospectively replaced by1520/1530 seeds below.
6. P2 cap edges could return an accepted support before saving it, or label a
   post-trial cap as numerical exhaustion. Accepted support/events are now
   saved immediately; post-trial caps explicitly retain `cpu_cap`. Focused
   inspection confirmed both corrections and36 producer mocked-cap branches.

Full source hashes are pinned in each receipt. Inspection, developer tests and
actual independent executions are distinguished; changed sources inherit no result.

## Manifest and exact algebra

The independent codec reader reconstructed every path/size/full SHA-256 from
v6 prefix encoding and v7 column encoding and recovered the same v4 map.
The290-entry baseline is commit6d894d5, master SHA-256
`3523daba8032c5a50ee28ec5fbfaa3fe27e8379352f1c7a4e22517d9c175c06f`.
Frozen-tree v7 generation/list/verify and v4/v5/v6 backward list/verify passed.
Content/size/omission/recursive unknown-suffix addition/inherited-input and
schema/payload mutations were rejected. The producer's45 checks were also
separately executed on frozen sources. This295-entry snapshot occupied15721
bytes; plus40 correctly fails16KiB. This is finite capacity, not headroom for
arbitrary future files. One complete producer master remains required.

Codec inspection covers encodings, identities and stream bounds; malformed
mutations exercise the producer CLI. No archival/security guarantee follows. Rational fixtures check12 weighted/
unweighted deletions,60 cardinal entries and60 leverage updates: determinant,
inverse/trace, output mass, physical covariance and common-scale invariance.
Weighted iid covariance is correctly distinguished from inverse Gram. These
are routine identities, not a new theorem or parity-quality result.

## P1 independent numerical result

Protocol a05fa01e preceded science. The5.31CPU-second audit checks129 raw
files, nine sources and compact-object equality. Frozen n4 reruns reproduce
all44 states across four rules. Independent Chebyshev recurrence/fresh SVD
check404 states across12 n4/n6/n8 paths: scores, admissibility/order, support
transitions, trace increments, integer risks, training norms and decisions.
All103 eligible maps (including Haar's actual weighted map), both Sobol norms/
variances and all12-target/sigma tables pass. Nineteen consequential maps also
receive21/41 meshes and2048 fresh points per measure, seeds1020+n/1030+n.
All short seed prefixes in this report mean202611.

Map errors<2.75e-12; norm/variance<7.35e-13; trace/risk/training<8.45e-11.
Deletion-increment discrepancy2.87e-8 at rejected n8lex-M166 is within1e-7;
lexN165's reproduction failure stays ineligible. An initial reviewer absolute
oracle failed on lex-M174's huge target/MSE values:3.05e-8/7.26e-6 at scales
10498.7/2.14e6. The disclosed revision retains absolute diagnostics and uses
per-entry max(1,abs(value)) scaling; scaled errors<8e-11. No producer change.

Both useful gates fail. At n8, A223/D222 save0.89%/1.33% with original norm
ratios1.65522/1.60783; new angular clouds give1.67372/1.61881. This is not useful
10%saving under P1 and proves no broader pruning impossibility. Full-N tails
stay diagnostic. Science finished before the serializer refused24756bytes;
its separate collector made16349bytes from unchanged raw data. Collection
identity and lost exact launch/exit UTC remain explicit in results; filesystem
times are not process timestamps.

## P2 independent numerical result

Corrected protocol143b5d0 uses assessment seeds2026111520+n/1530+n; the reviewer
reserved1720+n/1730+n. The3.59CPU-second independent run checked27 raw files,
all references/ten sources, compact object and UTC metadata. Every337 candidate
score, reason and feasibility decision was replayed from recurrence/SVD maps.
Every terminal one-row deletion was also freshly SVD-factored without a
cardinal-update shortcut. Actual frozen reruns reproduce both stop reasons.

All ten assessed maps, original21/41 meshes/Sobol families, target/repeat/MSE
tables and fresh2048-point clouds per measure pass. Candidate amplification
agrees to1.61e-14 relative, maps to2.58e-15. No numerical rejection caused a stop.

| n | Candidates / noise-feasible | Amplification-feasible | Minimum training norm ratio | Corresponding risk ratio / original row |
| ---: | --- | ---: | ---: | --- |
| 6 | 112 / 112 | 0 | 1.286955794542 | 1.016871257476 /69 |
| 8 | 225 / 225 | 0 | 1.444398676589 | 1.008680911798 /61 |

All candidates satisfy1.10noise; none satisfies1.25training amplification.
Minimum risk over amplification-feasible candidates is undefined. Both paths
save0sites and fail the registered goal. This exhausts the stated floating
first-step candidates, not multirow/nonnested subsets or all-degree designs.

## P3 independent tradeoff result

Protocol650b49dc prospectively fixed ceil(1.20N); old failures stay failed.
Preflight checked unchanged A arithmetic, validated durable prefix timing,
rectangular-map orthonormal scaling,28-start sample/initial/final maxima,
restricted-QR two-metric gates and minimum-count dominance predicates. The
455-node input SHAade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f
matches the inherited6d894d5artifact.

The11.49CPU audit checks75 raw files, all input/source pins and compact object.
All61 n8states match P1 and a frozen checkpointed rerun. Fresh SVD checks16
listed n12score stages, every support transition and12 saved maps. Prefix
clock placement/arithmetic passes; hardware timing is not replicated.
All23 maps/noise/Sobol/target/MSE tables,1288 recorded searchpoint values and
28-start schedules pass. Nine maps receive21/41 meshes and252 independent
refinements; all maps receive2048 fresh points per measure (2120/2130/2140+n).
Gradient differences<2.11e-9; other values<1.34e-13. Extra search preserves gates.

| n / sites | Risk / same-count QR | Searched norm / same-count QR | Recorded prefix CPU |
| --- | ---: | ---: | ---: |
| 8 /198 | 0.878582672 | 0.806102928 | 0.068833 |
| 12 /546 | 0.801238030 | 0.856606819 | 1.195763 |

Both gates pass. A546risk0.931099789/norm35.4607677 trades against storedU2's
455sites/risk1.172706357/norm26.0073232: fewer sites/lower norm versus lower
noise. No tested minimal control wins both metrics. Full-grid norm is much
better; diagnostic counts and function regressions remain. This finite
tradeoff supplies no global Pareto theorem, unknown-target selector or norm
certificate. MINOR returned prose error: n8A198calibration said0.905549;
P1/P3 raw risk is0.9055518679715243. No choice/gate changed or silent edit occurred.

## Independent exact rank and delivery verification

Read the complete [certificate reduction](pruning-certificate.md) and inherited
T8 homomorphism proof. Verified compatible primes and exact-order roots define
maps from Z[zeta_L,1/2] to finite fields. Nonzero monomial minors prove full
column rank of the ideal real cosine matrices; M>N is not square interpolation.
The independent code uses its own mixed-radix decoder, lexical monomials,
largest-residue row pivots and independently selected square minors.

| n / M / N | L | Producer prime/root/determinant | Independent prime/root/determinant |
| --- | ---: | --- | --- |
| 12 /546 /455 | 312 | 313 /10 /106 | 937 /15 /702 |
| 16 /1163 /969 | 544 | 5441 /4639 /330 | 6529 /58 /1257 |

Complete integer trial division proves each independent prime; factor tests
establish exact root order. Pairwise products are reduced before multiplying
again; elimination uses normalized rows and no unreduced dot accumulation.
The int64 product/difference bounds are877032/42621312. Powers and determinant
accumulation use Python integers. This proof uses no floating rank decision.

All exported IDs match their selected P3/P4 checkpoint/path, and regenerated
binary64 coordinates exactly match assessed bytes in this runtime. Payload
SHA-256 identities are
n12 `ddf19d3d0ee13125ee9db4a6f6175ed2279ad5b2272aa06a456d1e572df3d0cd`
and n16 `ef79d6094cbb1655c82c66666b0fef440990ca5a3059dab1465c03d86f5ebc84`.
Each disposable producer checker/payload/scientific-receipt copy verifies and
loads without raw scratch; eight malformed mutations reject. Full n16 review
uses5.485CPU. Each independent algebra-only checker also actually passed in
its own three-file copy (own checker/helper plus payload), with no producer,
receipt, Git or raw read: n12/n16 use0.434/2.674CPU. Historical measurement
linkage is recorded separately; repository-only algebra replays need none of
those temporary files. Old n12 payload, checker and receipts stay immutable;
current producer code accepts its historical creator/source identity.

These exported exact sets are Pi12/Pi16-determining, so positive-weight LS has
a unique coefficient minimizer. No exact dyadic rank, conditioning, norm,
error/covariance bound or all-degree claim follows. Quality remains MEASURED
and formal Claude audit04 remains pending.

## P4 independent degree16 transfer

Focused preflight cleared unchanged core/collector and driver4766e79d:
fixedM1163/B1377, fresh2420/2430/2440 seeds, mandatory modernU2/fineDetC4
and C3/C4 pins. Actual46.322CPU audit checks47 raw files, all source/input
identities, compact-object equality, six checkpoint maps/prefix arithmetic,
16 fresh-SVD score stages and all408 support transitions. Thirteen assessed
maps receive independent reconstruction/risks/targets/Sobol checks; six
consequential maps receive21/41 meshes and168 independent refinements.
Fresh seeds2620/2630/2640 preserve the result. Hardware timings are not rerun.

A1163 risk0.9480038875/norm40.88505841 gives restricted-QR ratios
0.7994329564/0.6697573053; recorded complete prefix is14.231638CPU. ModernU2
risk1.674587191/norm71.70774570 and fineDetC4risk1.585150703/norm80.12014027
are worse on both quality metrics but use969 sites. The registered gate
passes; all diagnostic/regression data remain. This is finite measured evidence.

Reported-value discrepancies are below3.44e-13. The auditor's first captured
run failed its gradient oracle: h1e-6 crossed a modernU2 cardinal zero.
The corrected checker records sign changes and uses a stable stencil;
gradients agree to8.96e-9. No producer change resulted. An earlier terminal
outcome was lost at compaction and is unclaimed; scratch reuse stopped before
numerics. These limits, failed-source/log pins and successful run are explicit
in transfer16.json. No full408-deletion driver replay is claimed.

## P5 independent reflection-pair result

Prospective corrections returned and fixed: nonfinite diagnostic ordering now
filters invalid scores; per-degree gates require complete assessments/no unrun.
Own synthetic checks cover114 fresh-SVD block/cardinal/risk cases,15 rank
rejects, seven ordering branches and three cap stops (0.049CPU). That receipt
pins driver9a0b42e8; final cap-label change5133f213 was separately inspected.

Actual3.500CPU audit checks49 raw files/all pins,148 independently fresh-SVD
pairs and both frozen screen reruns, including operational/diagnostic labels.
All17 fits/18 aliases, singleton/P2 comparisons, targets/noise and952 recorded
search values pass; ten maps receive21/41 meshes and280 new refinements using
3020/3030/3040+n. Maximum value error2.15e-14, gradient7.52e-10.

At n6/n8,45/100 pairs meet noise constraints, but0/0 meet amplification.
Minimum training ratios1.4051603053/1.4384221414 exceed1.25. Best-pair gains over
best singleton are−9.1848%/+0.4138%. Diagnostic held-out ratios1.45645836/
1.53205089 fail1.30; new searches give1.45645836/1.53294691. Both gates fail,
no operational deletion occurs, and no continuation is supported. This finite
48/100-pair failure is not impossibility for other blocks/subsets/degrees.

All assigned actual checks are complete; no material issue remains in scope.
Five research rounds is the stopping point, not a requirement to fill15.
Proof/measurement limits above and pending formal Claude audit remain explicit.
