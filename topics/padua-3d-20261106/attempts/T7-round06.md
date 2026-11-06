# T7 restarted-budget work

Rules/input7afa6a54a4db4652267e38cd48658ba435d20481,2026-11-06.
Assigned Codex gpt-6.1-sol xhigh, runtime metadata unexposed. Parent owns
Git, shared gates/LOG/round counts and all legacy corrections. Gate and
preregistration were saved before mechanism runs; first Part B count
depends on Part A publication. No rounds counted by this worker.

## Retained candidate records (prospective)

All records inherit the exact scopes, parameter ranges, controls, seeds,
objectives and kill rules in [preregistration](../preregistration-T7-round06.md).
They are continuations, with no historical novelty claim.

| Provisional IDEA | Question/mechanism | Closest entries and separation/kill | Initial disposition / resume |
|---|---|---|---|
| IDEA?padua-3d-20261106-codex-T7-R06-C | Execute T7-03 full mixed-stratum symbolic census n2/n3 | T7-03; coverage and exact symbolic decisions, not sampled deficiency | Active; incomplete coverage remains OPEN |
| IDEA?padua-3d-20261106-codex-T7-R06-Q | Measure explicit20-node T7-06 and discovered survivors | T7-06/T9; common-mesh measured quality only | Active; no asymptotic inference |
| IDEA?padua-3d-20261106-codex-T7-R06-Phi | Optimize noncyclic orderN subgroup phases n3..6 | T7-06/T8; rank2/3 invariant factors separate; torsion dimension may kill types | Active; bounded-sample failure never kills full class |
| IDEA?padua-3d-20261106-codex-T7-R06-U | Optimize2–4 noncyclic coset unions of exact sizeN | IDEA181/182/PD-N034; independent phases escape fixed involution; exact cardinality/rank first | Active; record every failed sample |

Literature limits and applicable obstructions are in the linked gate and
ledger. Raw parameter rows inherit these records and retain all outcomes.
No theorem is rejected because a proof or implementation is unfinished.

## Completed boundary1 (root publishes/counts)

D0 PASS: fixed T7-06 exact order=count=rank20 through inherited and new
actual-node evaluators. New sampled n3 fallback:256 rational-phase
draws,54 exact modular rank20 witnesses, each measured on21³ mesh.
Fixed T7-06 Lambda21=1998.95021415685, condition≈1482.51; best sampled
survivor12.29342557261. Independent check06 reconstructs every sample
and agrees with the fixed and best-survivor quality values.

Phi n3..6 was executed under the frozen algorithm. Best optimized
Lambda21 is9.74240738057 at n3 and47.63356182473 at n5, with exact
rationalized count/rank20/56 respectively. Rank>=2 order35 does not
exist; all order84 no-fold cosets are obstructed by the hand-proved
half-period imbalance. The same proof excludes rank3 order56.
The whole Phi class is not killed: its n3/n5 finite survivors remain.

Common-H U:128 starts each at n5/n6;4/128 floating full ranks at n5,
0/128 at n6. The best n5 two-coset winner has exact56-node count,
modular rank56 and measured Lambda21=49.01637726965. No common-H
noncyclic equal-size U class exists at n3/n4; unequal-size U is now
preregistered separately and remains to execute.

Canonical measured home: [quality](../theory/t7-r06-quality.md).
Analytic negative home: [torsion](../theory/t7-r06-torsion-obstruction.md).
Evidence: t7-r06-d0/sample/quality/phi/unions/baselines.json. Every raw
failed input is preserved by the seeded regenerating commands.

Commands actually executed (prefix `OPENBLAS_NUM_THREADS=1 python`):

```
topics/padua-3d-20261106/code/t7_r06_search.py d0 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-d0.json
topics/padua-3d-20261106/code/t7_r06_search.py sample --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-sample.json
topics/padua-3d-20261106/code/t7_r06_search.py quality --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-quality.json
topics/padua-3d-20261106/code/t7_r06_search.py phi --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-phi.json
topics/padua-3d-20261106/code/t7_r06_search.py unions --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-unions.json
topics/padua-3d-20261106/code/t7_r06_baselines.py --receipt topics/padua-3d-20261106/evidence/t7-r06-baselines.json
```

## C feasibility and fallback attempt (not completion)

Executed120-second n2 all-strata symbolic pilot:18 groups visited,
12 killed by projected-axis length,41980 strata counted exactly,
40964 with target count10. Six all-free strata were symbolically
deficient;40958 deficient specializations remain unresolved. Cursor:
order10, HNF-index17. This is an actual attempt at the required n2
fallback and measured evidence against the naive algorithm. It is
not a completed n2 census and not a valid strict stop reason.

## Runs needed / next independent work

Complete the unequal-size U extension; refine selected quality maxima;
improve C with proved phase-orbit/representation pruning and retry the
full n2 fallback. T7.C remains OPEN. Ceiling25 and strict handoff06
stop rule remain binding; no scope-exhaustion stop is claimed.

## Completed boundary2 development (root publishes/counts)

The phase-quotient and fixed-node-trace reductions were proved in
[C reductions](../theory/t7-r06-census-reductions.md); check06 independently
reconstructed the hand arguments. A second120-second n2 pilot visited
10733 HNF groups and2,195,749 quotient strata, with2352 target-count
strata:2336 exact fixed-trace kills,12 exact short-relation kills,
4 exact full-rank witnesses, and ZERO unresolved rank cases. Cursor
order26/HNF-index562. This completes neither the full n2 class nor
the full n3 class. Receipt: t7-r06-census-n2-reduced-pilot.json.

The complete prime-order block at n2 was separately executed through
all18 primes11..79, including every labelled HNF subgroup. Only p19
can have10 folded nodes. Its324 nonzero-coordinate-projection groups
have exact ranks {3:4,5:24,6:72,7:24,8:48,9:120,10:32}. Every folded
phase is sign-equivalent to the zero-phase set by the hand proof.
The exact deficiency decisions use rational rank of the integer
Fourier dictionary, not deficient finite-field specializations.
Receipt: t7-r06-primes-n2.json. Independent replay requested; no
finite-count PROVED upgrade made in this ledger before that replay.

Unequal-group U was actually executed at all n3..6 after its prospective
extension:640/640/1152/1152 rational starts,44/176/64/36 floating full
ranks. Selected winners have exact rationalized counts/ranks20/35/56/84
and Lambda21=13.5537233/69.1404064/41.1293089/216.1669274. Sizes are
(4,4,12), (4,4,27), (4,52), (9,75), respectively. Thus generic unequal
noncyclic unions escape the equal-common-H n6 failures; they remain
poor in these measurements. Receipt: t7-r06-unions-unequal.json.

Selected maxima were refined from the largest8 angular mesh starts:
fixed T7-06≥1999.1657353; Phi3≥9.7489664; Phi5≥47.6782918; equal U5
≥49.0679023; unequal U3/4/5/6≥13.6025795/69.1404064/41.1293089/
219.1077684. These are floating lower samples, not rigorous bounds.
All32 prime-block n2 survivors were mesh-measured; their raw catalogue
is regenerate-only. Receipt: t7-r06-refined-quality.json.

Additional commands actually executed (same single-thread prefix):

```
topics/padua-3d-20261106/code/t7_r06_census.py --n 2 --seconds 120 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-census-n2-pilot.json
topics/padua-3d-20261106/code/t7_r06_census_reduced.py pilot --n 2 --seconds 120 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-census-n2-reduced-pilot.json
topics/padua-3d-20261106/code/t7_r06_census_reduced.py primes --n 2 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-primes-n2.json
topics/padua-3d-20261106/code/t7_r06_unions_unequal.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-unions-unequal.json
topics/padua-3d-20261106/code/t7_r06_refine.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-refined-quality.json
```

The required full n2 fallback is now running with an additional proved
group-level projection upper cap. No result of that run is yet claimed.
