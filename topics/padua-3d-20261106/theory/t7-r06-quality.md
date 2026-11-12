# PD-T?padua-3d-20261106-codex-T7-R06-quality — measured coset quality

ID kind: PD-T. Aliases: restarted T7 quality/survivors/phase optimization.
Status: MEASURED. No asymptotic bound or priority claim. Split from/into:
none. Broad degree-uniform minimal-node target remains OPEN.

## Definitions and finite scope

Use Pi_n, N=binom(n+3,3), normalized product arcsine measure, and its
orthonormal product-Chebyshev basis. Lambda21 is the maximum of the
sum of absolute cardinal functions on the tensor21³ Lobatto angular
mesh. It is a floating sampled lower bound for the true Lebesgue norm,
without numerical enclosure. Phase objectives use log|det| and a9³
pilot Lambda followed by21³ reporting, as implemented in the frozen
producer. Exact rationalized-phase rank certificates concern nearby
rational nodes; the floating optimum's quality is measured separately.

## Completed measurements

| Set / degree | Lambda21 | Inherited QR | Lower-set Leja |
|---|---|---|---|
| Fixed T7-06 /3 |1998.95021415685|8.32067061469|13.17471981995|
| Best of54 exact sample survivors /3 |12.29342557261|8.32067061469|13.17471981995|
| Phase-optimized noncyclic /3 |9.74240738057|8.32067061469|13.17471981995|
| Phase-optimized noncyclic /5 |47.63356182473|13.85750218512|26.33661533788|
| Two common-H noncyclic cosets /5 |49.01637726965|13.85750218512|26.33661533788|

The fixed survivor has condition2≈1482.51, so its algebraic existence
does not supply competitive quality. Phase optimization improves the
n3 sampled set by orders of magnitude while still losing to QR; the
n5 optima lose to both controls. This does not satisfy the preregistered
two-consecutive-n>=6 competitive kill condition.

The n3 random sample has256 independent seeded input draws from all
1085 labelled order20 HNF subgroups (with replacement) and rational
phase denominator1009. Exactly54 have20 distinct nodes and modular
rank20. Every such survivor was measured. Deficient finite-field ranks
are observations only, not characteristic-zero rank upper bounds.
Exact root order, prime and matrix hashes are recorded per raw row.

Phi3 sampled92 distinct embeddings of C2×C10;80 were killed by the
proved half-period condition,12 retained phase screens. Phi5 sampled
162 distinct embeddings across C2×C28 and C2×C2×C14;145 were killed,
17 retained. The top4 determinant screens at each surviving degree
were optimized; this is a bounded heuristic selection, not global
optimization over embeddings or phases. Phi4's rank>=2 class is empty,
and Phi6's full no-fold class fails by the separate proved torsion
obstruction. See [theorem](t7-r06-torsion-obstruction.md).

For common-H equal-size unions2–4 with noncyclic H, no admissible
subgroup sizes exist at n3/n4. At n5,128 independent rational starts
on two order28 cosets yielded4 floating full ranks; the selected
rationalized winner has56 distinct nodes and modular rank56. At n6,
128 starts on three order28 cosets had no floating full rank. These
finite failures do not classify all unions. Unequal-subgroup unions
are a separately preregistered extension, not covered by this table.

## Provenance, independent checks and limitations

Commands are in the small evidence receipts and attempt ledger. Raw
catalogues are regenerate-only in a configurable unique local directory;
receipts record identities. Code dependencies: NumPy2.3.5, SciPy1.17.0,
SymPy1.14.0, Python3.12.14; old QR/Leja helper files are imported
read-only. BLAS threads were fixed to1. Source identities are pinned
in receipts; no source-prose hashes are checked by the producer.

Independent check06 reconstructed all256 rational-phase samples using
a separate HNF inverse and monomial evaluator:54 full-rank cases and
best Lambda21=12.293425572605921. Its fixed T7-06 Lambda is
1998.9502141570445. Those replays corroborate the measurements;
they do not prove a Lebesgue upper bound or an all-phase census.

Canonical baseline correction: the first run's `controls.qr` used
orthonormal column scaling before QR extraction, which selects a
different node set. Those values remain as an explicitly secondary
orthonormal-QR comparator. The primary inherited unscaled-QR values
above were actually rerun in t7-r06-baselines.json, without changing
or reoptimizing family nodes. This correction affects comparisons,
not determinant objectives, which differ by a fixed basis factor.

## Subsequent unequal-union and refined-maxima measurements

The prospective unequal-subgroup extension used640/640/1152/1152
rational starts at n3/4/5/6, with44/176/64/36 floating full ranks.
Selected winners have exact rationalized node counts/ranks20/35/56/84.
Their subgroup-size partitions are(4,4,12), (4,4,27), (4,52), (9,75).
Measured Lambda21 is13.5537233,69.1404064,41.1293089,216.1669274.
Thus n6 has successful minimal unions outside the equal-common-H
sample, although their measured quality is poor. No family kill or
asymptotic negative theorem follows from this finite screen.

Refining the largest8 mesh starts by bounded angular L-BFGS-B gives
lower samples1999.1657353 (fixed T7-06),9.7489664 (Phi3),47.6782918
(Phi5),49.0679023 (equal U5), and13.6025795/69.1404064/41.1293089/
219.1077684 (unequal U3..6). These finite samples have no rigorous
rounding enclosures and do not certify global maxima. Every selected
refinement terminated successfully on all8 starts in this environment.
All32 prime-block n2 full-rank groups were mesh-measured separately;
their raw row identities and summary are in t7-r06-refined-quality.json.

## Completed census-survivor coverage

Every positive representative of the complete n2 all-phase census was
measured: four order16 representatives each give Lambda21≈7, and the
32 order19 representatives range from7.05325615906 to8.13406903712.
The degree2 inherited unscaled QR and lower-set discrete Leja controls
both give Lambda21=7. The best order16 set's largest8-start refinement
also returns7. These are measurements, including that apparent tie;
they are not certified equality or global-max claims. See
t7-r06-census-quality.json and t7-r06-final-refinements.json.

The bounded n3 mixed-stratum pilot additionally produced13478 exact
full-rank rational witness phases. All13478 were actually measured,
covering7965 distinct rational node sets. Lambda21 ranges from
12.50888586428 to2587225.50612; maximum condition2 is2.34809e6 and
maximum inverse residual is9.59e-10. The worst values therefore have
substantially weaker numerical accuracy than the best. This covers
every positive witness produced by that pilot, without claiming a
bound uniform over its positive-dimensional phase strata. Receipt:
t7-r06-n3-pilot-quality.json. The separately frozen256-draw n3 sample
and its54 full-rank witnesses remain a distinct fallback sample.

The final8-start refinements of the best random-sample and symbolic-
pilot n3 witnesses give12.31150701225 and12.54192067336, respectively;
all8 starts terminated successfully for each. Their mesh values remain
12.29342557261 and12.50888586428. The same inherited degree3 controls
apply, so both lose to QR; the random-sample mesh value is below Leja.
None of these finite measurements meets the two-consecutive-degrees
n>=6 competitive rejection rule. The broad quality target remains OPEN.
