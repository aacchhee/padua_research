# PD-T?lattice-c3-codex-03 — Finite exact ranks of the C0 3D congruence catalogue

ID kind: PD-T. Aliases: C3 Round1; 412-pattern rank campaign. Split from: none. Split into: generic lifting in c3-generic-witness-reduction.md; negative scopes in c3-deficiency-observations.md and c3-rectangle-observations.md.

## Statement

For the frozen C0 catalogue (SHA256 `21cd7610051d7f51e8578051da164f73ef112d9081765cea7156b26f01441430`), filter d=3,n=1..6. The 412 admissible primitive single-congruence character fibres reduce to 364 selected-index sets up to axis reversal. With distinct independently seeded random axis lists at p=1009,1013,1019 and two trials per prime, their exact total-degree ranks are those in C3/ranks.json. There are 142 representatives attaining full rank at least once; 140 attain full rank in all six trials. Every trial uses exact modular Gaussian elimination and returns a determinant residue as well as rank.

## Definitions / assumptions

C0 lengths are sorted triples in {n+1,n+2,n+3}; k=2..6, gcd(k,a1,a2,a3)=1 and every ar!=0 modulo k. Only single congruence fibres are covered: zero coefficients, unions of cosets, boundary corrections and larger grids/moduli are excluded. Representatives sharing the same actual point set or an axis reversal are identified; every original C0 row retains an explicit reversal map. No cardinality or rank completeness beyond that finite catalogue is claimed.

## Status by part

Overall status: MEASURED (finite exact computations). The generic determinant-polynomial statement has a separate written proof in PD-T?lattice-c3-codex-01; this record deliberately reports the finite ranks. A generic nonvanishing proof may invoke that reduction and independently checked nonzero witnesses, with no axis-criterion or conditioning conclusion.

| n | C0 rows | actual-set/reversal reps | full at least once | full every trial |
|---|---:|---:|---:|---:|
| 1 | 119 | 77 | 50 | 50 |
| 2 | 68 | 62 | 19 | 19 |
| 3 | 78 | 78 | 32 | 31 |
| 4 | 45 | 45 | 18 | 18 |
| 5 | 56 | 56 | 16 | 16 |
| 6 | 46 | 46 | 7 | 6 |

## Checks

Code c3_rank.py SHA256 `a95afbb764838662358dc70d2fd5a7eddf335d3ae48254d29b717fa015143332`; canonical output ranks.json SHA256 `560471d0053fef785bcee9c64f1b7fe9a384e24c0c74ef3d4cd58b9d6c703130`. Exact commands, versions, seeds and inputs are in C3/evidence.md and the output itself. The code records all sampled axes, so its claims do not rely on reconstructing a pseudorandom implementation. Independent Astra rerun reported all2184 test payloads reproduced; the auditor owns the durable report and acceptance disposition.

Selective rational witnesses: c3_structure.py used seeded distinct integer axes in [-30,30] for all69 n<=2 rank survivors, with exact Bareiss determinants. 68 were nonzero and one was zero. The zero case C3-28a254dbd915 is a singular specialization, not a generic counterexample; its nonzero modular witnesses and nonzero symbolic n1 determinant are preserved.

## Per-pattern properties and scope

All rows are periodic by construction. Finite rank survival is only generic feasibility. Axis-factorized or other structural criteria and measured Chebyshev behavior are recorded independently in C3/pattern-outcomes.tsv. No unbounded-degree 3D family is accepted on ranks alone, and no Lanczos, MZ or cubature claim is made.

For Chebyshev axes, reversal i->L-1-i changes its physical coordinate h_i to -h_i. Coordinate reflections and coordinate permutations preserve Pi_n, the cube, and the symmetric tensor sampling mesh, and hence preserve both the exact Lebesgue constant where interpolation exists and its sampled mesh maximum. C0's unit scaling preserves the selected set; equal-length permutations/sorted-axis relabeling act by these coordinate permutations. This justifies transporting the numerical properties to original aliases.

## Dependencies / sources

Frozen C0 catalogue; exact checker; generic reduction only when explicitly invoked. Closest prior entries IDEA-013/029, lower-set interpolation and Dencker–Erb (LITERATURE with baseline reading limitations). No publication novelty claim.

## History / open items

2026-10-31, Codex C3 developer, assigned gpt-6.1-sol xhigh, rules/base e949ef06895acd5463cdf8df7e0e5f795218f70f. All412 rows retained. Required Claude audit remains after supplementary Astra reconstruction. Infinite-degree generic classification remains OPEN.
