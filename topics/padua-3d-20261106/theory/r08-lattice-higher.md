# PD-T?padua-3d-20261106-codex-R08-n7 — complete n7 positive-cubature exclusion

ID kind: PD-T. Aliases: unshifted n7 positive-cubature complement.
Split from/into: none. No novelty claim.
Overall status: **PROVED, computer-assisted finite result** for absence
of at-most120-node rules in the stated n7 class. The minor cost diagnostics
and bounded minimum128 observation below remain MEASURED. This result is
separate from n1..6 in [the complement record](r08-lattice-complement.md).

## Statement and definitions

For n7, N=120, enumerate every unrestricted row-HNF L<=Z³ with shortest
nonzero l1>=14 and det<=8N=960. In the complete independent execution,
none of its21354010 admissible lattices has at most120 unshifted cosine
nodes. The separately MEASURED minimum folded count **within det<=960**
is128, attained at q686 by rows(7,0,7),(0,7,7),(0,0,14).
Global minimum folded128 is not claimed: excluding smaller folds would
require determinants through8*127=1016. Global minimum-unisolvent size
is also OPEN.

The intended finite exclusion transfers from Haar enumeration to any
strictly positive full-support unshifted degree13 cubature by the local
positive-weight witness and q<=8|X| reduction. It excludes an n7
Padua-type set in this class;
it says nothing about arbitrary phases or general node sets.

## Exact execution, independent coverage and cost

The frozen result-bearing core is `r08_lattice_enum.cpp` SHA256
e07ad9e51d5b883e7c6d813d396ef32ea0ac24eda253a73f6137f8b8f86feaa4,
with exact reduction in [r08-lattice-reduction.md](r08-lattice-reduction.md).
The producer first hit120seconds after completed q881, then its fresh
q882..960 tail hit120seconds after completed q921. Both scopes had no
fold<=120 case. Their stopped raw bytes and completed prefixes remain
separate in `r08-lattice-higher.json` and `r08-lattice-n7tail.json`.
The final q922..960 segment completed in88.0856seconds under another
120second gate, using
`r08_lattice_finish.py`; this orchestration driver compares every completed
per-q total HNF count, post-prune test count, admissible count and small
case count against the independent full replay. The finish receipt
`evidence/r08-lattice-n7finish.json` confirms exact agreement at every
q1..960, combined584906253HNFs,456323923post-prune tests,
21354010admissible and zero small cases. The scientific per-q digest is
909f9922a468ac00745d180344299e62d35e9b17e2b16ec881bd707eece5ae39.
Thus each decisive determinant has two actual executions; the producer's
three disjoint completed segments constitute its full independent coverage.

Independent worker check_lattice08 separately executed the frozen core
from q1 through960 without a subprocess timeout:584906253 total HNFs,
456323923 post-axis/pair scalar tests,21354010 admissible, zero small
cases;304.789seconds. Exact receipt and raw identity:
`evidence/r08-lattice-check-producer-complement-n7.json`. Its own checker
also checks the finite reduction using a different forbidden-congruence
short-vector construction and monomial-Fourier ranks at lower degrees.
The full n7 replay is an actual separate execution, not a reading of the
producer's output. The local finite reduction and committed regenerating
code plus these separate actual executions support the claimed finite
computer-assisted exclusion. No packing theorem is needed.

The high cost is measured, under concurrent sessions. Fresh tails reset
the incumbent minimum-fold pruning state, so their elapsed time cannot
be estimated just by the fraction of determinants remaining. The n6
global-minimum continuation similarly capped after673..703 of720 with
no fold<=90; it does not prove global minimum91. Its complete det<=672
search does prove absence of <=84-node rules. No dense matrix memory
estimate is substituted for these actual unrestricted enumeration costs.

## Limits and next unresolved step

The proposed n8 pilot was deferred without execution after the measured
tail costs; no n8 infeasibility is asserted. Degrees8..109 stay OPEN in
the finite complement. The separate source-dependent packing obstruction
starts at110 and uses its explicit LITERATURE premise. The largest
actually observed degree with <=N positive nodes is5 (54nodes,rank48);
the largest observed Padua-type degree is2. The whole n>=3 question,
phases and omitted zero-weight support remain OPEN.

To extend computational coverage, preserve the existing capped receipts
and preregister a new complete determinant bound with a measured budget;
seed an admissible incumbent only through separately checked code rather
than silently editing the frozen producer. No additional n8 run is a
prerequisite for recording the actual n1..7 outcomes.

## History

2026-11-06; input9042e1c42964150f30fdbe8563c12ba6c6a8692a; Codex,
assigned Sol xhigh. Handoff08 B6; these measured executions replace
the former unmeasured unrestricted-census infeasibility claim. Counter
ownership and final continuation boundary are root's.

The record was initially MEASURED while the last producer segment was
running. After its actual completion and exact per-q comparison, the
n7 exclusion was upgraded as stated above; its computed minimum128 and
the unresolved global minimum were not upgraded with it. This is a
material new finite result for the focused audit.
