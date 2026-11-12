# PD-N?padua-3d-20261106-codex-T8-r08-02 — finite half-shift selector quality losses

ID kind: PD-N. Aliases: Hdet finite competitiveness failure; half-shift
D2 assessment; determinant-only selected quality. Split from: none.
Split into: none. The cubic classification and even-degree obstruction
are separate claims used to interpret the family, not parts split from
this finite quality-loss statement. Old finite existence is separately
split from its own original mixed record.

## Statement, definitions and assumptions

For the frozen Hdet selector in preregistration-T8-round08.md, the executed
complete first-unit b<c scans at n3/5/7 yield the exact-positive selected
sets and21^3 tensor-Lobatto sampled Lebesgue values below. At n5 andn7,
the selected set's sampled value exceeds both the same-degree QR and
discrete-Leja sampled controls. Thus Hdet fails the finite promising-status
criterion at n5. The two-consecutive-Leja-loss D2 trigger **cannot be assessed** (it has not fired):
only one eligible tested admissible degree>=6, n7, occurs within 3..8.

A sampled Lebesgue value means max of the cardinal absolute sum over the
fixed mesh, a lower bound on the true continuum maximum. No comparison
of true continuum norms, asymptotic growth or global family optimum is
claimed. The exact same-degree control definitions and graded mode order
are frozen in the preregistration and executable helper.

## Status and negative-result scope

Overall status: **MEASURED**. The negative statement concerns finite mesh
performance of this specified selector, not universal interpolation failure.

Candidate disposition: the finite competitive-performance subclaim of
IDEA?padua-3d-20261106-codex-T8-r08-Hdet is **REJECTED: failed** under
the preregistered QR promising-status test at n5; its literal two-loss D2
kill has not fired. The unrestricted odd-degree half-shift construction
and quality target remain OPEN/deferred, with a structural resume condition.
Attempted mechanism: complete determinant-only search in the stated phase
class, then exact certification and mesh comparison. Parameter range:
first-unit z=(1,b,c),1<=b<c<2N; tested n3,5,7; phase z/(4N); fixed21^3
mesh. Analytically excluded n4/6/8 have no quality value and do not count
as Leja losses.

## Results

| n | N | pairs accounted | selected z | sampled Lambda21 | Leja | QR | degree seconds(original/corrected) |
|---|---:|---:|---|---:|---:|---:|---:|
|3|20|741|(1,4,11)|9.788798269|13.174719820|8.320670615|.6001/1.4599|
|4|35|all,analytic|none|undefined|not run|not run|0|
|5|56|6105|(1,10,49)|70.372944840|26.336615338|13.857502185|1.3953/3.4098|
|6|84|all,analytic|none|undefined|not run|not run|0|
|7|120|28441|(1,17,28)|136.690399705|49.812587823|26.935072319|15.2479/17.8156|
|8|165|all,analytic|none|undefined|not run|not run|0|

The table's times include each degree's certificates/quality; the receipt
also retains separate scan times. No180s budget or4096-pair fallback bound
was reached in either execution. The prescribed all-pair universe is fully
accounted; analytically invalid sign patterns are pruned before numerical
determinants. At n5/7,2883/13095 finite determinant scores were obtained;
finite scores of singular matrices may occur by floating roundoff, so only
actual two-prime full-rank finalists are accepted. The first finalist at
each degree certifies. No global or exact determinant maximizer is claimed
at n5/7, where score ordering remains binary64-sensitive.

Selected n3/5/7 condition2 values are7.64259/31.7692/54.5710; largest
cardinal-node residual is 1.16e-13; all three conditions are far below the 1e12 guard.
Every selected set has exactly N nodes and two nonzero actual-node modular
determinants, independently replayed with distinct primes and monomial basis.
This proves finite unisolvence by the inherited exact reduction but does
not turn the floating quality observation into a proved norm statement.

## All cubic positive sets, retained without quality selection

| z | sampled Lambda21 | condition2 |
|---|---:|---:|
|(1,4,11)|9.788798269|7.64259|
|(1,4,29)|9.788798269|7.64259|
|(1,6,15)|17.249288148|13.20119|
|(1,6,25)|17.249288148|13.20119|
|(1,11,36)|9.788798269|7.64259|
|(1,15,34)|17.249288148|13.20119|
|(1,25,34)|17.249288148|13.20119|
|(1,29,36)|9.788798269|7.64259|

All8exact determinants tie, as proved separately in the cubic classification.
The original machine-score execution selected(1,6,25); the post-run exact-tie
repair selects the registered lexicographic(1,4,11). The full chronology and
post-quality timing are disclosed once in [the attempt](../attempts/T8-round08.md).
This table's full retention prevents the corrected choice from obscuring
the poorer tied sets.

## Depends on and executed checks

Exact rank reduction: PD-T?padua-3d-20261106-codex-T8-r06-04.
Even-degree obstruction: PD-N?padua-3d-20261106-codex-T8-r08-01.
Cubic exact classification/ties: PD-T?padua-3d-20261106-codex-T8-r08-01.
No external theorem is needed for these finite sampled calculations.

Executed from repository root, with one BLAS/OMP thread:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_r08_halfshift.py
    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_r08_tie_correction.py

[Original receipt](../evidence/t8-r08-halfshift.json) and
[corrected receipt](../evidence/t8-r08-halfshift-corrected.json) retain
commands, dependencies, versions, all finalists/survivors and exact
certificates. Raw tuples are regenerate-only in unique/tmp directories,
with paths/sizes/full hashes in the respective receipts; no archival
delivery is claimed. Committed receipts are below16KiB each and preserve
two genuinely different executions, not fragments of a bulk output.
Independent source/commands/evidence are in
[independent-checks-round08-t8.md](../independent-checks-round08-t8.md).
The independent quality evaluator uses separately written Chebyshev
evaluation and inverse/batched mesh evaluation, matching the frozen graded
QR mode order, and reproduces the reported samples within numerical roundoff.
Its exact rank reconstruction uses monomials at fresh splitting primes. Trust NumPy/SciPy binary64 linear algebra for quality only.

## Scope, open items and history

No growth verdict is allowed from these3rows; only2are n>=4. To resume
odd-degree quality work, preregister a separated structural rule or an
inverse/kernel estimate and unseen degrees. Another numerical det sweep
within this completed universe cannot manufacture promising status. D2's
missing second eligible degree is a scope limitation, not an implicit
permission to run n9; that would require a new prospective append/root gate.
The broader T8 target remains OPEN.

2026-11-06,Codex mathematical developer assigned gpt-6.1-sol xhigh,
rules9042e1c, gate69694f3. The exact tie repair and this new finite negative
record are material changes for focused Claude re-audit.

## History — audit04 G1, 2026-11-12

Current n7 representative is (1,17,28), the lexicographically first label
in the exactly tied reflection orbit containing the historical executed
(1,17,212). The table's time and quality remain those of that historical
execution, transferred by the exact cube/mesh reflection; no new timing
or global determinant maximality is asserted. Canonical chronology,
full orbit and symmetry argument: [T8 attempt](../attempts/T8-round08.md#audit04-g1--n7-exact-tie-label-correction-2026-11-12).
The finite MEASURED failure and D2 assessment remain unchanged.
