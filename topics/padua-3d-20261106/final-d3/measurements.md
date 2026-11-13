# PD-T?padua-3d-20261106-codex-D3-measured — sampled cubic Lebesgue constant

ID kind: PD-T. Aliases: D3 quality diagnostic. Split from/into: none.

## Statement and status

Status: **MEASURED**. For the dyadic center of the enclosed rule, the
sampled cubic Lebesgue maximum is **30.012095658454324**, at
(1, -0.40673664307580004, 1), on 31^3 endpoint cosine queries plus
20000 random-angle queries with seed 20261113 (49791 queries total).
This is a finite floating computation on rounded centers, without a
certified continuum upper or exact-root transfer.

## Definitions and checks

For cubic monomial evaluation V at the 20 nodes, evaluate cardinals by
solving V^T L=v(query); the Lebesgue function is sum(abs(L)). Maximum,
witness, query count, software versions and seed are in fd3-producer.json.
No optimization or growth-law fit is authorized. Commands and complete
limits are in [protocol](protocol.md); certificate theorem in [theory](theory.md).

## Scope

The measurement records the quality of this one finite rule. It proves
no universal lower bound from positive cubature and no asymptotic law.
It does not claim the optimal n=3 Lebesgue constant. External benchmark
reading belongs to D5 and retains its source-specific coverage limits.

## History

2026-11-12 Codex, assigned gpt-6.1-sol high, rules/input 04ef28b;
prospective measurement record followed by the authorized one-round run
at `db8c3cc`, with result recorded above. Exact producer pins: [runs](runs.md).
