# Supplementary independent checks 01

2026-11-05. Codex independent checker, requested gpt-6-astra high; serving
model identity/effective effort are not independently exposed. Rules/source
`823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`, main/base
`b4d292eea5eed373002506d5e16a3761bd7ae10e`. This is supplementary verification
of Codex development, not the mandatory Claude audit or merge approval.
No developer code was silently fixed; this worker owns only its independent
checkers and reports. Complete gate/read scope: [gate](novelty-gate-independent.md).

## Current conclusion and limits

G0 replays pass exactly. The complete small NN Jacobians agree **exactly over
Fraction** between an independently constructed defining-moment derivative
and the frozen AD-C4 graph, including terminal sites and two mass gauges.
All current native methods were compared over their entire output arrays
with independent exact moments at N4/8/12/16. The forward improvements are
finite measurements, not full-array backward stability. D4 transform/flow
identities and the positive-transform normality trap have separate exact
checks. The D5 local geometry proof has no identified substantive gap in
the scope reviewed below. Work on subsequently supplied growth/projection
claims remains separate; this report does not approve unseen revisions.

**G4 scope finding, sent to coordinator.** The raw N4 Krawtchouk LU array
violates a necessary compatibility identity by an exact nonzero dyadic
residual. Hence its strict backward error to an exact full NN array is
infinite. A nearby positive input plus a coefficient correction is a
two-component mixed witness, not the raw-array backward error. Forward gains
and these witnesses cannot silently satisfy the literal backward-error limb
of G4; an explicitly dated interpretation is needed for any broader gate
verdict. This does not reject the measured forward gain or local projection
theorem. A fixed-path inverse is weaker still, as the executed trap shows.

## Execution environment and frozen sources

All commands below actually ran separately from developer executions, from
`/workspace/scratch/nn-mop-stability-20261105`, exit 0 unless the development
failure is explicitly stated. Python3.12.14, mpmath1.3.0, NumPy2.3.5,
SciPy1.17.0; Linux6.18.57-x86_64/glibc2.41. Exact checks use standard-library
Fraction; NumPy/SciPy/mpmath values are numerical observations. Deterministic
inputs; no random seeds. Primary papers and external software were not run.

SHA-256 source identities:

| Source | SHA-256 |
|---|---|
| predecessor `c4_float_baseline.py` | `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8` |
| predecessor audit01 exact checker | `13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3` |
| `conditioning.py` | `11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c` |
| `native_mixed.py`, first three-method check | `218f29e0c222ff5c0045845556437057ebfeddae4dcdde70fb3fdbd48c0065d4` |
| `native_mixed.py`, four-method check | `3aef4afb6ce48c71d69f6337ce20b4c700f98de24e9465def864881a01f0c506` |
| `stage_isolation.py` | `5b71073a127fa3aed36353f5d046eb5dab51a089b15bcbe44c529b867f928f1e` |
| `path_recovery.py` | `4f3d58541b40b6be11a56e2cbcd5f23d3318902c66f566bbe2656e602852a4e8` |
| `backward_joint.py` | `9327da0ba867b043a4e2eb81cdb082fcc6e359d8f5f3b808e413885c264019d1` |
| `backward_dyadic.py` | `40d02ef16a372cf786b89669a509f67f187d20ffde9710636153446de72967b7` |
| `integrable_transport.py` | `59043e6e84008097374a570422848cabcef810c6b30bb6e18b419079e2a6a2d0` |
| `dictionary_probe.py` | `b962375445439c2e3c41e6838449f92cb58b5e2c63f737322020922d2d038fe7` |
| `independent_check_moments.py` | `58d6da632647e309e6299f9f67890237536172694864f18f15b721f5e7ffe0d9` |
| `independent_check_diagnostics.py` | `c3c93268f362114a71cbc41a1ee9cfb103e7e6b5b7b66b6fcd188b58fdbb0d03` |
| `independent_check_backward_integrable.py` | `db6119933c4746842b7e2aa34f38c8e99178baece48cb255e23993aa61da604f` |

The new native revision adds nodeqr and warning metadata; it does not alter
the three older solvers. Their exact-reference E values agree in the two
independent executions. Checker outputs include dependency hashes, checked
again at the end to detect concurrent source changes.

## Commands and output receipts

```sh
python topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-independent-g0-krawtchouk.json
python topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family hahn --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-independent-g0-hahn.json
python topics/nn-mop-stability-20261105/code/independent_check_moments.py > /tmp/nn-mop-independent-moments.json
python topics/nn-mop-stability-20261105/code/stage_isolation.py --no-path > /tmp/nn-mop-independent-stage.json
python topics/nn-mop-stability-20261105/code/independent_check_diagnostics.py > /tmp/nn-mop-independent-diagnostics.json
python topics/nn-mop-stability-20261105/code/dictionary_probe.py > /tmp/nn-mop-independent-dictionary.json
python topics/nn-mop-stability-20261105/code/backward_dyadic.py --reproduce > /tmp/nn-mop-independent-dyadic.json
python topics/nn-mop-stability-20261105/code/integrable_transport.py --mode exact > /tmp/nn-mop-independent-integrable.json
python topics/nn-mop-stability-20261105/code/independent_check_backward_integrable.py > /tmp/nn-mop-independent-backward-integrable.json
```

Every filename below has prefix `/tmp/nn-mop-independent-` and suffix `.json`.
These raw outputs remain local/regenerable, not cold-storage archived or
committed. Byte hashes include environment/timing metadata where emitted.

| Output stem | Bytes | SHA-256 |
|---|---:|---|
| g0-krawtchouk | 7063 | `7f5ffae98ffca60f55ab70206eed8f2d31aa44cce7b03967941b3b073cd75d32` |
| g0-hahn | 7092 | `dfdec7222247e4f3ac9fe514329028fa54c7a4085bc49d892477f0c139964a59` |
| moments | 20550 | `63c7ad5f81d78664a85431947e31c8a4cbc28e9449f62d414f01b9b6fd49c5bd` |
| stage | 26891 | `c303b96ba90b4781989d5f76bbe49424bd6a02b6822ff38eca4cc6a509cde310` |
| diagnostics | 1839 | `690746cd6b0c8eb23fe9f73d05871e84a9727b33727cb55651b1738833cb2322` |
| dictionary | 906 | `ca9891b2a311d1873524c6b0cd2646eb87efc3bd525da53867b02706e9c04f54` |
| dyadic | 685 | `b18711d6477f6e235a976bfad3dea93c37d1fd537126036ebeee08b87164fda7` |
| integrable | 2107 | `7855ed92c4e6a21ea5d9a1e72753a5515671ce407e8eb767270bd0e9aeae477b` |
| backward-integrable | 6768 | `60872bd8316ec19bf4c5fdfe04c09bca8f5f1fa2c535f7082f4b7e4fbb377178` |

## G0 and D2

All twelve full case payloads exactly equal the separately produced D2
G0 payloads, with the same input hashes and E values as predecessor
`response-independent-01.md`. Relative E mismatch is zero, so G0 passes
its 1% criterion. All 48 no-path stage payloads exactly equal the matching
developer output after deleting only the path subobject. This independently
reproduces marginal errors and E, not all 48 spectral diagnoses.

On exact N4 Krawtchouk data the 100-dps path diagnostic is below2e-100 in
the mixed metric. Changing off-path b1_(0,3) by1 gives an identical diagnostic
but breaks terminal b1=b2. Thus the diagnostic cannot control the whole
array. A second check changes d0 by.01 and compensates a1/a2_(1,1) to
preserve the step-line gamma2/delta2: the path spectrum stays fixed while
second-measure weights change (mixed weight discrepancy.0364).

Checker-development history: the first anchor trial changed b2_00 alone
and incorrectly expected an unchanged Hessenberg matrix; its assertion
failed, exit1. The correction compensates gamma2/delta2 explicitly, as
above. This was an independent-checker mistake, not a developer finding.
Only the corrected successful output is a receipt. No developer file changed.

## Exact derivative construction and certification limits

The independent checker builds exact moments and their ordinary-coordinate
derivatives, solves each defining system by Fraction Gauss–Jordan inversion,
then computes `dot c=-M^-1(dot v+dot M c)` and differentiates the h/t formulas.
It checks original primal and differentiated equations. This construction
does not import developer `moment_map` or propagate C4. For comparison only,
the actual frozen developer AD graph is evaluated with Fraction scalars.

Both families at N3/4/6 pass all4,416 Jacobian-entry equalities and all
coefficient equalities. Translation yields dot a=0,dot b=1; node scaling
yields dot a=2a,dot b=b; either whole-weight scaling gives zero derivative.
Terminal b1/b2 values and derivative rows agree exactly. Signed maximizing
rows attain the mixed row-sum condition exactly; the witnesses are in the
local output. This supplies an exact finite sanity, not an all-size enclosure
of floating derivative tables.

| Family | N3 kappa | N4 kappa | N6 kappa |
|---|---:|---:|---:|
| Krawtchouk | 34.4 | 165.04 | 12305.32 |
| Hahn | 94.3289256198 | 1573.91599654 | 196180.267511 |

These are exact rational computations displayed as decimals. N4 Krawtchouk
has exact kappa4126/25, attained in a1_(2,1). The metric permits independent
relative weight changes and absolute unit-scale node changes; it is not
the fixed-mass tangent induced norm. Fully componentwise output conditioning
is infinite at sensitive exact zero coefficients such as b2_(0,0).

Reviewed `conditioning-local.md` at64374b21…a299 and the coarse all-N
Krawtchouk bound at85f7edaf…facc: differentiated defining systems, row-sign
maximization, Chebyshev-system normality, rational-height inverse estimates
and field-scale lower bounds have no identified gap. The coarse upper bound
does not establish the requested sharp growth law. Analytic derivatives are
proved formulas; high-precision numerical tables remain MEASURED.

## Native array and backward checks

Independent exact moments provide every field/site reference throughN−1,
not just a step-line. All LU/QR/SVD/nodeqr variants were tested for both
families atN4/8/12/16. Examples of measured E against this independent exact
reference are LU Kraw N8=3.096338832032919e-12 and Hahn N8=
4.238190788569583e-10; nodeqr N16 gives3.919393212744686e-4 and
2.294206296701597e-2. Exact arithmetic verifies the reference; the solver
errors and superiority comparisons remain finite MEASURED observations.

For LU and nodeqr atN4 in both families, independently rebuilt the full
triangle from the developer's frozen rational spectral-axis witness using
exact moments. Checked exact positivity, ordered common nodes, mass-one
gauges and all required nonsingular systems. Exact mixed input distances
and coefficient corrections agree with reported floating values within
1e-12 relative. Distances range1.14e-16–4.15e-16 while full coefficient
corrections range1.07e-14–5.04e-14. A feasible witness is not a minimizer.

Both `backward_dyadic.py --reproduce` and a separately written Fraction
calculation from regenerated native coefficients give

    (b2_00-b1_00)(b1_01-b1_00)+a1_10-a2_01
      =25700541873527631/649037107316853453566312041152512 !=0.

This is PD-T289 B2 atnu0 with absent-axis a's zero. It suffices to exclude
any exact normal common-support input for this precise raw array. The
floating producer and its finite reference comparison remain MEASURED;
the exact stored-tuple incompatibility reduction is separately checkable.

Reviewed `backward-local-manifold.md` at
`d9cef81be5e0fa1f682ede6d56a0b9936847233cfcd98a13e90d0d0406ac06fc`.
The two full Jacobi axes give an analytic left inverse after ordering nodes
and fixing masses. This proves rank3N−2 and excludes distant image branches
approaching the base point. A fixed SPD ambient norm gives a positive
Hessian and a unique nearby/global-near-base minimizer. The proof correctly
does not extend uniqueness to the nonsmooth PD-T290 maximum metric,
arbitrary zero-curvature arrays, nonnormal inputs or colliding/zero-weight
data. No numerical nearest projection was verified in this round.

## D4 and D6

Separate D4 developer-code exact replay passes80 fields and30 determinant
identities atN4. The independent moment checker additionally compares
Christoffel output against directly transformed exact moments and Toda's
right-hand side against `J*(0,x*w1,x*w2)` atN4/6 in both families:
248fields agree exactly in each comparison, including terminal closure.
For the N3 positive pair(11,1,1),(13,2,1) on0,1,2, every original system is
normal; multiplying byx+1 keeps positive weights but yields means1/2 for
both measures and determinant M11=0. The exponential determinant
a(9−4a−a²) also follows by direct expansion of the stated rows.

Read D4 exact proofs at hashes896077bc…2173 (Christoffel),
2da91f32…0382 (normality trap),878633d9…1563 (ratio invariant),
120488e3…98bb (Toda). No substantive algebraic gap identified: determinant
sign, finite terminal formulas and common-factor restrictions are explicit.
This does not certify the floating transport/ODE experiments or an arbitrary
target solver; no new primary-source comparison is claimed by this checker.

D6 frozen code replay passes. Independent Fraction elimination reconstructs
P11=x²−75x/23+32/23 and the missing graph x moment−30/23. The two-sheet
annihilator y²−y and selector identities are direct identities. Positive
ambient encodings survive; the scoped standard-grade identifications fail.
D6 developer prospective-gate timing qualification remains explicit.
