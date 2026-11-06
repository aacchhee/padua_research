# PD-T?nn-mop-cond-codex-C1-05 — sharp NN rate survives diagonal gauge optimization

ID kind: PD-T. Aliases: gauge-infimum rate squeeze; fixed and smooth
normalizations; intrinsic Krawtchouk base.
Split from: none. Split into: none.

## Statement

For the exact Krawtchouk pair p1=2/5,p2=1/2, N nodes
x_l=2l/(N-1)-1, write rho=5+2sqrt(6). Let K_fix,N and K_dep,N be
the fixed-gauge and local C1-section infima defined in
`c1-gauge-invariants.md`, retaining all six NN coefficient fields with
separate field-sup scales. Then

    lim_(N→infinity) K_fix,N^(1/N)
      =lim_(N→infinity) K_dep,N^(1/N)=rho.

This holds for mixed node scale one, componentwise-node scale |x_l|,
natural-spacing node scale 2/(N-1), fixed-mass tangent input, and their
natural log-weight equivalent, as defined in `c1-scalar-derivative.md`.
The statement concerns exact first-order sensitivity in these fieldwise
metrics, not a rate for an algorithm's rounding error.

## Assumptions and status

Overall status: PROVED, written corollary of the two explicit proved
bounds below. Normality and the finite output domain are those of
PD-T432/433. Both gauge classes and field scales are exactly those of
`c1-gauge-invariants.md`; no arbitrary renormalization of error scales
is allowed. Candidate disposition: retained consequence of C1-01,
without a new mechanism or historical novelty claim.

## Depends on and proof

PD-T437 and `c1-gauge-invariants.md` give, for M=N-1,

    K_dep,N >= 5/(2M²)[rho^(M-1)+rho^(-(M-1))].

The parity witness changes weights only and preserves mass, so the lower
holds under every listed input variant. Every fixed gauge is a smooth
section and the monic gauge belongs to the fixed class. For N>=3 each
listed input domain is contained in the original mixed box, or is
first-order identical to it for log weights. Therefore

    K_dep,N <= K_fix,N <= kappa_monic,mixed,N.

The sharp upper theorem `PD-T?nn-mop-cond-codex-C2-hard-01` in
`c2-sharp-upper.md` proves

    kappa_monic,mixed,N <= 3,000,000 N^13 rho^(N-1).

Taking Nth roots of the lower and upper bounds gives the same limit rho,
because every displayed polynomial factor has Nth root tending to one.
The squeeze proves both limits, including the natural-spacing case whose
irrelevant N2 input scale exceeds one.

## Checks, sources, scope and open items

No numerical premise or external source theorem. This file depends on
the exact stated sharp-upper theorem, whose independent checks/audit are
recorded separately; it does not reproduce or independently approve that
proof. The gauge-invariant lower was separately checked by the topic's
supplementary checker. No exact finite-N gauge optimizer, sharp step-line
gauge rate, Hahn sharp rate, finite-epsilon radius or weak-stability
theorem is supplied by this corollary.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Added after the coordinator
supplied the finalized full-NN sharp upper; preserves the earlier
standalone lower result unchanged.
