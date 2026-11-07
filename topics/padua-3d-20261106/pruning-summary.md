# Pruning campaign: results and usable point sets

2026-11-07. Rules/input6d894d50efd8167c5b10f3d5b0da4d8cf214b681.
Five of the authorized fifteen research rounds completed; ten slots remain
unused. Earlier U1/U2/U3counts4/7/5are unchanged. Exact-artifact verification,
engineering and independent reruns consume zero research rounds.

## Delivered sets

|Degree|Polynomial dimension|Starting sites|Retained sites|Sites saved|Complete prefix CPU|
|---:|---:|---:|---:|---:|---:|
|12|455|637|546|14.29%|1.20s|
|16|969|1377|1163|15.54%|14.23s|

The two small essential files contain canonical integer point IDs and
orders, so coordinates can be reconstructed without raw trajectories or
rerunning pruning. Their exact ideal-cosine matrices have independently
certified full column rank. This guarantees unique least squares for
positive weights; these oversampled sets do not interpolate arbitrary
546/1163values in dimensions455/969.

- [Degree12 points](evidence/pdpr-pruned12-nodes.json), [PROVED rank455](theory/pruning-exact12.md).
- [Degree16 points](evidence/pdpr-pruned16-nodes.json), [PROVED rank969](theory/pruning-exact16.md).
- [Loading and verification guide](pruning-artifacts.md), [complete measurements](pruning-results.md), [independent review](pruning-review.md).

Quality remains MEASURED on rounded coordinates, using sampled/searched
amplification lower values. Exact rank is not a proof of conditioning,
continuous norm bounds, global optimality or a degree-uniform construction.

## Practical tradeoffs

At degree12 the546-site set has searched amplification35.46and fixed-B637
noise risk0.9311, versus41.40/1.1621for the same-size restrictedQR control.
The optimized455-site example uses91fewer sites and has lower amplification
26.01, while its noise risk1.1727is higher. No general winner is claimed.

At degree16 the1163-site set has searched amplification40.89and fixed-B1377
noise risk0.9480, versus61.04/1.1858for same-size restrictedQR: approximately
33%lower amplification and20%lower noise risk. The modern969-site example
has71.71/1.6746but uses194fewer sites. Keeping all1377sites gives still
better12.74/0.6888. Six RMS regressions versus the full grid and a25.70%
maximum-error regression for one tested smooth target versus modern969
are retained. Lower amplification does not guarantee smaller target errors.

All noise comparisons assume iid physical observation errors, product-
Chebyshev prediction measure and the explicitly stated feasible integer
repeat budget. These are research assumptions, not facts about AC's data.
Repetition leaves each stated coefficient map fixed. Historical controls'
construction costs and current loading costs remain separate.

## What the five rounds established

1. P1backward variance/determinant deletion: the strict full-grid-preservation
   goal fails; diagnostics at exactlyNalso lose strong controls.
2. P2exhaustive amplification-aware singleton removal: every tested first
   deletion fails the25%training-amplification limit at6/8, although every
   singleton meets the10%noise limit. This is a finite support/constraint
   result, not impossibility of all smaller subsets.
3. P3calibrated fixed-count tradeoff: the prespecified1.20Nrule transfers to
   degree12and beats same-count restrictedQR on both stated metrics.
4. P4same rule at degree16: the finite tradeoff passes against fresh same-
   count and modern minimum-count controls. Full-grid preservation still fails.
5. P5reflection-pair discriminator: none of148pairs meets the unchanged
   joint constraints; no full paired trajectory is justified by that gate.

Independent actual score/map/target/noise/trajectory/refinement checks
corroborate these outcomes. Both exact-cosine certificates were replayed
with different primes/monomial bases and in repository-only copies.
The general minimum-node3DPadua target remains OPEN. Formal Claude combined
audit04is pending; no readiness, registry application or merge is requested.
