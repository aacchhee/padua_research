# PD-T?padua-3d-20261106-codex-T8-r06-06 — mixed special-phase samples

ID kind: PD-T. Aliases: resumed S strata; finite rational positives.
Split from: none. Split into: none.

## Statement, definitions, assumptions and status

For n2,n3 and M=N,N+1,2N-1,2N, the frozen S screen enumerates every
1<=b<c<M and the 27 state vectors in {0,1,2}^3. State0 means phase0;
state1 means 1/(2M); state2 means the free-coordinate rational sample1/257.
It exact-counts each rational node set, checks modular evaluation rank for
each exact N-node sample, and retains up to two positive special samples
per (n,M). Overall status **MEASURED** for this finite screen. It is not
a complete enumeration of T7-03's special points, continuous phases, or
symbolic minors; deficient specializations leave symbolic rank OPEN.

| n | M | samples | retained non-all-free full-rank samples |
|---|---:|---:|---:|
| 2 | 10 | 972 | 0 |
| 2 | 11 | 1215 | 0 |
| 2 | 19 | 4131 | 2, both zero phase (inherited baseline) |
| 2 | 20 | 4617 | 0 |
| 3 | 20 | 4617 | 2 |
| 3 | 21 | 5130 | 2 |
| 3 | 39 | 18981 | 0 |
| 3 | 40 | 20007 | 0 |

No 90s cap/fallback was needed; all stated pair/state samples completed.
The cubic M20 states (0,1,1) and (0,1,2) give exact certified20-node
sets with sampled Lambda73.055440 and84.978858. At M21, states (0,0,1)
and (0,0,2) give exact certified20-node sets with Lambda130.486681 and
792.475764. These include mixed free/special strata, so the resumed route
has positive actual outcomes. Their generators/phases and two-prime
certificates are in evidence/t8-r06-strata.json; the receipt is the
unambiguous finite construction specification. The zero-phase n2 rows
are disclosed inherited controls, not new phased constructions.

## Reduction, proof obligations and scope

T7-03 proves exact count is constant on its full collision strata, while
rank need not be. A nonzero evaluation determinant at one exact rational
sample proves a symbolic full-size minor is nonzero on the containing
stratum; the positive rows thus furnish rigorous finite certificates and
an existence route, pending independent execution under the workflow.
Conversely none of the absent/deficient samples excludes its continuous
stratum. The states include only two special coordinates per axis,
so even the all-special finite slice is not the complete T7-03 partition.
The first-unit fold theorem now supplies a sharper all-phase count reduction
for Phi3b, which was separately preregistered after seeing these positives.

## Checks, sources, open items and history

Command/source/versions/raw identities are in evidence/t8-r06-strata.json;
run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python
topics/padua-3d-20261106/code/t8_r06_routes.py strata`. Exact certificate
reduction is t8-r06-certification.md; source limits literature-T8-round06.md.
2D Padua is admitted by the general T7-03 reduction and D0 controls. No
full cyclic/all-coset stratum census, all-degree selection, or quality bound
is asserted. Independent rerun remains needed. 2026-11-06, Codex assigned
gpt-6.1-sol xhigh, rules/input7afa6a54; no new final ID allocated.
