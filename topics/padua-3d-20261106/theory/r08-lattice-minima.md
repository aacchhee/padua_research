# PD-T?padua-3d-20261106-codex-R08-minima — unrestricted determinant minima through16

ID kind: PD-T. Aliases: reopened T10.1 determinant objective.
Split from: none. Split into: [D4-minima, packing-free n4..7 cases](../final-d4/finite-minima.md). No priority claim.

## Exact statement and status

For every integer1<=n<=16, minimize det L over full-rank L<=Z³ with
shortest nonzero l1 norm>=2n. The minima are the following q. The next
column is the folded size of **every determinant minimizer**, not the
global minimum folded size. Rank or minimum-unisolvent claims do not
follow from this column.

| n | min det | minimizers | fold at min det |
|---|---:|---:|---:|
|1|2|1|2|
|2|12|12|7|
|3|38|8|20|
|4|92|24|47|
|5|178|24|90|
|6|304|8|153|
|7|486|24|244|
|8|724|24|363|
|9|1026|8|502|
|10|1412|24|707|
|11|1878|24|940|
|12|2432|8|1187|
|13|3098|24|1550|
|14|3868|24|1935|
|15|4750|8|2304|
|16|5772|24|2887|

Status n1..3: **PROVED, computer-assisted finite result**, with full
enumeration from q1 and the historical audit03 exact reruns plus round08
checks. Status n4..16: **PROVED with explicit LITERATURE dependency**,
computer-assisted finite result using the packing bound below. The
uniform source-label criterion is proposed to AC in response03; this
wording never asserts a local proof of the imported density theorem.

## Definitions, assumptions and dependencies

Use the HNF, dual group and fold conventions of
[r08-lattice-reduction.md](r08-lattice-reduction.md). Imported theorem:
Betke–Henk's octahedron lattice packing density18/19, in the normalization
primary-read in [t9-r06-packing-source.md](t9-r06-packing-source.md).
It gives det L>=38n³/27. The source theorem is LITERATURE; its complete
classification proof and Minkowski's original proof are not locally
verified. The finite searches themselves do not depend on source table
optimality labels or on which lattice supplies the initial upper bound.

## Proof and exact finite evidence

For n1..3 the unchanged compiled enumerator checks every row HNF from
q1 through the first admissible q. For n4..16 it checks every row HNF
from ceil(38n³/27) through the first admissible q, including all forms
at that q to count minimizers. The exact reduction proves exhaustive
short-vector tests and exact folds. The bound excludes all lower q.
For n6/9/12/15 the first q attains the bound, but all minimizers at that
q are still enumerated; the seed's attainment alone would not count them.

The n16 window requested q5765..5792 and stopped after fully checking
q5772; all q5765..5771 were empty. An example has HNF rows
(1,0,1671),(0,1,427),(0,0,5772). This improves the inherited seed5792,
so extending a catalogue value as a global minimum would have been wrong.

Producer receipt: `evidence/r08-lattice-min.json` (compact14560bytes at
first final serialization). Every row records the completed interval,
total unpruned HNF count, scalar-test count, count/fold distribution,
one minimizer, source identities and raw JSONL identity. The raw minimizer
lists and per-q tables are regenerate-only, in unique scratch directories.
No prose hashes are executable premises. Code source identity is the
same unchanged C++ enumeration across all scopes.

Independent execution: check_lattice08's alternate forbidden-congruence
enumeration completed every n4..16 window, including all empty n16 q and
24 q5772 minimizers, independently confirming the table. Its n16 alternate
run took70.16seconds. See `evidence/r08-lattice-check-windows.json` and
`independent-checks-round08-lattice.md`. A separate full producer replay
is an additional check, not the basis of algorithmic independence.

## Reproduction, cost and limits

Build and run, replacing scratch/binary paths with fresh ones:

```
python topics/padua-3d-20261106/code/r08_lattice.py build /tmp/r08-lattice-enum
python topics/padua-3d-20261106/code/r08_lattice.py run min --degrees 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 --binary /tmp/r08-lattice-enum --scratch /tmp/UNIQUE-r08-min --receipt /tmp/UNIQUE-r08-min.json
```

The last receipt may be serialized compactly without changing its JSON
fields. Timings are measured wall times under concurrent work, not fixed
performance guarantees. n4..12 completed in seconds in the compiled
implementation. n13/14/15/16 took16.18/35.58/11.74/146.57seconds in the
recorded run. n16 had no subprocess timeout; completion after the initial
120second reassessment marker is disclosed in the attempt record.

No phase, general positive-weight classification, global folded minimum,
unisolvence or Lebesgue norm is inferred solely from this determinant
table. The separate complement record states those finite outcomes.
Unrestricted determinant minima above16 remain OPEN.

## History

2026-11-06; input9042e1c42964150f30fdbe8563c12ba6c6a8692a; Codex,
assigned Sol xhigh. Handoff08 B5, audit03 E1; exact replication and finite
extension of the existing audit route. Companion rank/complement results
replace the former catalogue headline without rewriting historical runs.

## 2026-11-12 — settled E4 convention

The existing packing consequence retains **PROVED with explicit LITERATURE dependency** after the primary density normalization and local application were rechecked; only an actual independent lower-cutoff replay can remove that dependency from a finite range. [Primary checks and AC decision](../final-d5/e4-verification.md).
