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

## Completed boundary3 development (root publishes/counts)

2026-11-06 dated gate qualification: all new T7 registrations retain the canonical [reading-coverage qualification](../response-deviations-02.md#new-t7-round06-reading-coverage-qualification--2026-11-06); later completeness checks do not cure the qualified initial chronology.

The full n2 fallback ACTUALLY completed in173.688seconds, separately
from both earlier pilots: all344054 labelled HNF subgroups of orders
10..80,2,705,380 nonprime quotient phase strata,2358 target-count
strata,2342 fixed-trace kills,12 compatible short-relation kills,
4 full-rank classes, ZERO unresolved cases. The complete prime block
adds32 full-rank order19 groups. Every positive nonprime phase stratum
is zero-dimensional at phase[0,0,0], so no exceptional phase locus
remains to classify. The complete compact certificate lists all36
positive representatives. See [exact classification](../theory/t7-r06-n2-census.md),
t7-r06-census-n2-complete.json and t7-r06-certificate.json.

Distinct check06 actually reran the full producer in179.102seconds:
all scientific fields and BOTH rejection-catalogue hashes match. Its
separate implementation independently covered all344054 groups and
matched every count, with own actual-node monomial rank10 proofs for
the four order16 sets. Its separately reconstructed integer Fourier
dictionary census matches all324 nonzero-projection order19 groups
and32 full-rank cases. Evidence: independent-r06-t7-census.json,
independent-r06-t7-primes.json, independent-r06-t7-replays.json.

The required n3 feasibility measurement also ACTUALLY ran. Static
enumeration finds2,723,067 HNF groups of orders20..160, with159400
passing the necessary projection bounds. The120-second symbolic
pilot reached3373 groups/726864 quotient strata at order24/HNF62,
with36100 unresolved rank cases. It is explicitly NOT a full n3
census. The allowed fallback is now complete exact n2 plus the earlier
256-draw exact rational-phase n3 sample; no incomplete n2 excuse or
scope-exhaustion stop is used. Receipt: t7-r06-feasibility.json.

Q measured every one of the36 complete n2 positive representatives,
every one of the54 full-rank random n3 sample witnesses, and EVERY
one of the13478 exact-positive rational witness phases from the n3
pilot (7965 distinct node sets). The latter range from Lambda21
12.50888586428 to2587225.50612, with maximum inverse residual9.59e-10.
The four order16 n2 representatives give≈7 and the32 order19 groups
range7.05325615906..8.13406903712. Primary inherited degree2 QR and
Leja both measure7. Final8-start best-witness refinements give7
(n2),12.31150701225 (n3 random sample),12.54192067336 (n3 pilot).
All floating quality claims remain MEASURED. See the updated
[quality record](../theory/t7-r06-quality.md) for limitations.

Final route dispositions under handoff06:

| Route | Actual result / class limit | Broader status |
|---|---|---|
| D0 | Direct actual-node rank20 certificate and distinct monomial replay pass | Finite validation only |
| C | Complete exact n2 all-phase classification; actual n3 cost/unresolved pilot;256-draw exact random-phase n3 fallback | Full all-phase n3 OPEN |
| Q | All36 n2 classes,54 n3 sample positives,13478 n3 pilot positive witnesses and fixed T7-06 measured; controls and selected refinements run | Degree-uniform quality OPEN |
| Phi | Frozen phase optimization n3/n5 gives exact rationalized full-rank witnesses; n4 rank>=2 class empty; whole no-fold n6 and rank3 n5 obstructed by proved trace theorem | Rank2 n3/n5 not universally killed; no competitive early-kill claim; no degree-uniform H_n was proposed or prospectively saved (only n3/n5 have nonempty rank>=2 no-fold classes in n3..6) |
| U | Equal common-H and unequal noncyclic2–4-coset screens actually run n3..6; exact minimal full-rank unequal winners at every degree | Samples do not exclude all unions; only generic no-fold phases were screened — folded special-phase unions and unequal/mixed cyclic unions were not screened by T7 |

Every listed handoff06 route therefore has its actual finite result,
permitted fallback, or proved class obstruction. This permits the
route-completion stop after root's round3 publication under condition(a),
with the broader Padua-type construction/quality goal OPEN. It does
not claim a theorem excluding the whole direction or invoke the
unmet competitive two-consecutive-n>=6 kill condition. Root alone
records the count and stop in LOG; no fourth round is started here.

2026-11-06 source-pin audit: the original published t7-r06-d0.json
records an early search-source hash da4c5339… whose exact source snapshot
was not preserved before other route functions were appended. That
historical receipt remains unchanged and is not claimed to regenerate
from the final source hash. The NEW t7-r06-d0-frozen-replay.json actually
reruns D0 against the committed frozen a3960922… source; count/rank and
the actual-node certificate agree. Every later route also reran D0 and
the distinct checker independently verified its monomial matrix. All
other source pins and every raw hash passed the final receipt audit.

Additional commands actually executed (same single-thread prefix):

```
topics/padua-3d-20261106/code/t7_r06_search.py d0 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-d0-frozen-replay.json
topics/padua-3d-20261106/code/t7_r06_census_finish.py --n 2 --seconds 1200 --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-census-n2-complete.json
topics/padua-3d-20261106/code/t7_r06_certificate.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-certificate.json
topics/padua-3d-20261106/code/t7_r06_feasibility.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-feasibility.json
topics/padua-3d-20261106/code/t7_r06_census_quality.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-census-quality.json
topics/padua-3d-20261106/code/t7_r06_n3_survivor_quality.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-n3-pilot-quality.json
topics/padua-3d-20261106/code/t7_r06_final_refine.py --output-dir /tmp/padua-t7-r06-7afa6a54 --receipt topics/padua-3d-20261106/evidence/t7-r06-final-refinements.json
```
