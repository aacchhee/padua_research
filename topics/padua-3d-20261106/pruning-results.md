# New pruning campaign — results and actual run ledger

2026-11-07. Rules/input6d894d50efd8167c5b10f3d5b0da4d8cf214b681.
Codex gpt-6.1-sol high developer; provider runtime metadata unexposed.
Root alone controls Git/shared records. New pruning ceiling15total;
old U1/U2/U3 counts and all prior results remain separate.

## P1 completed: noise/design deletion does not preserve amplification

P1consumes **1research round** (root publishes count boundaries); current
campaign count after P2below is2/15.
P1's A and D rules both fail the frozen useful-transfer gate. They preserve
numerical rank/reproduction through N, and their coefficient-noise scores
beat poor deletions, but their operational prefixes save at most two/three
of225sites at n8. Those prefixes already worsen fresh amplification by
65.52%/60.78%. Neither rule earns a degree12transfer. This does not reject
all backward deletion or all near-minimal designs.

|n|start M / N|rule|selected M|site saving|held-out amplification / start OLS|integer-budget risk / start OLS|
|---:|---:|---|---:|---:|---:|---:|
|4|45 /35|A|44|2.22%|1.36501|1.02716|
|4|45 /35|D|44|2.22%|1.41094|1.06043|
|6|112 /84|A|112|0%|1|1|
|6|112 /84|D|111|0.89%|1.37205|1.01687|
|8|225 /165|A|223|0.89%|1.65522|1.01197|
|8|225 /165|D|222|1.33%|1.60783|1.02512|

Selection used only the connected training/noise prefix from the
[published protocol](pruning-protocol.md), not the held-out ratios above.
The128interior-Sobol-plus-corners training sample under-resolves spikes
introduced by deletion. Low leverage and small trace increase do not
control raw-value row-l1 amplification. All norms are finite lower samples.
A/D first failures and every subsequent diagnostic point remain retained.

All six A/D paths pass the numerical/risk-update checks at4/6/8; exact-N
function/noise/norm outcomes are diagnostic failures, not recommendations.
The lexicographic n8N165endpoint fails reproduction (5.50e-8>1e-8), with
condition4.94e6; it is retained as ineligible, not repaired. Seeded random
and all remaining comparator cases are retained. No exact unisolvence
proof is asserted for these new binary64 arrays.

At n8, full OLS has trace0.709997 and sampled amplification7.87067.
At exact165sites, A has trace3.22591/amplification78.1873 and D has
3.99594/56.2476; inherited globalQR gives2.90584/45.5358 and one-sweep
localdet1.60513/23.9726. Fixed-B225integer-repeat risks are2.33652/3.02746
for A/D, versus2.04434/1.16742 for globalQR/localdet. Thus this endpoint
also loses the stronger inherited controls. Haar-full remains a separately
weighted baseline (trace0.740141/amplification10.2485), with no silent
weight/noise substitution.

Every12-target/measure/sigma table is retained. Individual deterministic
regressions include n8selected A's5.02% worst Chebyshev-RMS increase and
selected D's five worsening targets (worst1.82%); uniform maxima also
regress. Aggregate counts/maxima are in every checkpoint receipt row,
with full values in raw. The amplification failure is not softened by
reporting only iid noise, and no generic approximation winner is claimed.

## Existing-curve diagnosis, without new queries

The stored P1 curves have **no re-entry** into the original connected
training-amplification/10%-integer-risk admissible region for either rule
at any pilot degree. Merely choosing a later prefix cannot rescue P1.
Even ignoring amplification, the10%equal-budget-risk allowance permits
A only5.36%site saving at n6 and4.89% at n8 along these paths. At10%site
saving, A's integer risk rises21.24%/21.54%, and training amplification
rises92.38%/74.76%. D is worse in risk. This finite diagnosis does not
prove infeasibility of another deletion order.

This supports a genuinely distinct next question: exhaustively consider
all admissible deletions with the **actual raw-cardinal** update, enforcing
both noise and a denser training norm constraint before choosing a row.
The PRUNE-L variant is already cleared as a known design variant by the
[gate](pruning-gate.md); it needs a separate prospective P2appendix before
execution. All P1failures remain fixed rather than renamed as a success.

## Actual runs and technical verification

P1 protocol was published at a05fa01eefb9e187e73b870cfa74b7eb7887d42f
before science. Root granted an exclusive single-thread window. The exact
producer command, unchanged executed-source snapshots and inventory are
in [P1receipt](evidence/pdpr-pilot.json). Raw directory:
`/tmp/pdpr-pilot-20261107a`, local regeneration-only, not archival delivery.
P1 completed104distinct assessments in17.097765CPU/17.110976wall seconds,
under900CPU allowance, with no unrun cases. Source snapshots were written
at09:12:34UTC and the completed details at09:12:51UTC on2026-11-07;
these are filesystem recording times, not claimed exact process-launch/
exit timestamps. The producer's launch UTC variable was not persisted
before its later serializer failure, an explicit timing-provenance limit.

**Canonical serialization deviation:** the producer completed all science
but refused its24,756byte compact envelope. No scientific rerun occurred.
The separate `pdpr_collect.py` read every raw identity unchanged and
produced one16,349byte receipt. Its XZ/base85codec losslessly stores a
**six-significant-digit summary**, not the full-precision result. Full
precision decisions/margins/function tables/cost phases stay in the
hashed raw record; derived M*trace and union amplification are explicit.
Original executed code identities are the saved snapshots; the collector
has its own identity, and is not relabeled as the scientific producer.
This repair consumes0research rounds. Future producers must persist UTC
launch/exit and use compliant collection without relying on a failed writer.

The [engineering receipt](evidence/pdpr-engineering.json) records the final
actual preexecution command in/tmp/pdpr-engineering-20261107e. It passes
26synthetic QR deletions,21exhaustively checked integer allocations,
5common-metric control-gate branches,3absolute tie-to-A branches and
4all-degree numerical-gate branches. Earlier a/b/c/d raw directories
retain prepublication engineering iterations. Every such check consumes0
research rounds and is not an independent consequential science rerun.
The implementation computes C by triangular solve after each QR downdate;
no formed Gram inverse is used. Fresh QR/SVD guards precede checkpoint
quality. Source files stayed unchanged during the complete P1execution.

## Pending work

The distinct [P1review](pruning-review.md) passes its declared
scope:404count states with fresh SVD/recurrence, degree4all-rule node
reproductions,103eligible maps/all target-noise tables,19selected maps on
original meshes plus fresh clouds, and129raw identities. Fresh n8angular
ratios1.67372/1.61881 confirm both failed gates. This is a supplementary
Codex review; formal Claude audit remains pending. The scoped finite
negative statement is [P1boundary](theory/pruning-p1-boundary.md), MEASURED.
Next research requires prospective publication of P2, not an automatic
larger-degree rerun of the failed P1rules. Fourteen slots remain a ceiling.
The455-node stored artifact and old construction sources/data remain intact.

## P2 completed: every singleton is excluded by the norm constraint

P2was prospectively published at
143b5d0e17688d835b1e0c5f61e1ed95a5e05dbe before its exclusive timed run.
Completed new research rounds are now **2/15**, thirteen unused; neither
P1norP2passes the strict transfer gate. The new PRUNE-L rule exhaustively
scores every current row using the actual raw-cardinal update and full
integer-repeat covariance, filtering **both** constraints before choosing.
It stops immediately at112/225sites at n6/8 because no initial deletion
is feasible. Numerical guards pass and there are no rejected QR trials,
cap hits, missing comparisons or source changes during execution.

|n|rank-admissible singleton rows|10%risk-feasible rows|25%training-norm-feasible rows|joint feasible|minimum training norm / start among risk-feasible|
|---:|---:|---:|---:|---:|---:|
|6|112|112|0|0|1.28695579|
|8|225|225|0|0|1.44439868|

The minimum integer-risk ratio among norm-feasible rows is **not defined**
at both degrees because that feasible set is empty. The best-norm row's
integer-risk ratios are1.01687126/1.00868091, so the norm constraint,
not the10%noise allowance, causes this first-step obstruction. Conversely,
the best-risk rows have integer-risk ratios1.01087069/1.00588785 and
training-norm ratios1.42388232/1.68771366. Dense training has985queries:
9³angular mesh plus256fresh angular Sobol points, explicitly changed
from P1's sparse training after its under-resolution was observed.
No threshold was retroactively relaxed and no frozen P1failure erased.

The returned maps equal full OLS, so their held-out norm/noise/target
ratios are1. Fresh globalQR/localdet/restrictedQR and all same-count
P1A/D/random/lex controls were assessed on the newly frozen1520+n/1530+n
query seeds. Every individual target/sigma table and candidate score is
retained in the raw record, including all337zero-feasibility decisions.
A zero-step stop is an actual exhaustive finite single-deletion result,
not an unexecuted proposal and not a theorem about arbitrary subsets.

Actual P2command, full start/end UTC, original executed-source snapshots,
versions/threads/seeds, and the single6489byte logical receipt are in
[P2receipt](evidence/pdpr-constrained.json). Raw directory
`/tmp/pdpr-constrained-20261107a` is local regeneration-only. Full run used
4.149492873CPU/4.150582085wall seconds of600CPU, with source hashes
69c81447(core),3911ee2a(driver),4d86a43b(collector). Unlike P1, metadata
was persisted before/after science and collection completed normally.
[P2engineering](evidence/pdpr-p2-engineering.json) passed26raw-cardinal/
full-feasible-set comparisons against fresh QR, three feasibility-before-
objective branches, and36mocked CPU-cap cases covering both accepted-state
recording and post-trial-cap labeling, plus inherited QR/allocation/gate
checks. Those preflights consume0research rounds.

The [P2singleton boundary](theory/pruning-p2-singleton-boundary.md) is
MEASURED. Independent consequential P2replay is pending; formal Claude
review remains separate. This stops only the exact strict-constraint
singleton rule on these two initial supports. A separately registered
starting-support, matched-count/Pareto, or symmetry-block question may
escape its hypotheses. No P3science is executed or automatically licensed
by this result; the remaining thirteen slots are a ceiling, not a quota.
