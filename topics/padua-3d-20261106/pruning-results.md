# New pruning campaign — results and actual run ledger

2026-11-07. Rules/input6d894d50efd8167c5b10f3d5b0da4d8cf214b681.
Codex gpt-6.1-sol high developer; provider runtime metadata unexposed.
Root alone controls Git/shared records. New pruning ceiling15total;
old U1/U2/U3 counts and all prior results remain separate.

## P1 completed: noise/design deletion does not preserve amplification

P1consumes **1research round** (root publishes count boundaries); current
campaign count after P4below is4/15.
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
MEASURED. The [independent P2review](pruning-review.md) passes its actual337candidate
fresh-QR feasibility reconstruction and complete map/target/noise scope;
formal Claude review remains separate. This stops only the exact strict-constraint
singleton rule on these two initial supports. A separately registered
starting-support, matched-count/Pareto, or symmetry-block question may
escape its hypotheses. No P3science is executed or automatically licensed
by this result; the remaining thirteen slots are a ceiling, not a quota.

## P3 completed: a near-minimal count/noise/amplification tradeoff transfers

P3passed its **new fixed-count tradeoff gate**, not P1/P2's full-grid
preservation goal. It consumes one new round, bringing actual completed
research to **3/15** (root publishes the count boundary). Protocol650b49dc
preceded execution; final source checkpoint46d1e2b preserved source hashes.
The A rule is unchanged and was calibrated from known n8data to target
ceil(1.20N), without a new rule/count choice from unseen n12outcomes.
All61n8retained-index states reproduce the P1path exactly.

|degree|full sites|primary sites|saving|complete primary construction CPU|A risk / same-count QR risk|A searched norm / same-count QR norm|
|---:|---:|---:|---:|---:|---:|---:|
|8|225|198|12.00%|0.068833s|0.878583|0.806103|
|12|637|546|14.29%|1.195763s|0.801238|0.856607|

Both degrees pass numerical/cost/site-saving gates and improve **both**
fixed-total-observation-budget risk and sampled/searched amplification by
at least5%over restrictedQR at the same count. No tested N-site control
dominates the primary candidate in both noise and amplification. This is
finite nondominance among declared controls, not global Pareto optimality.

At n12the important modern control is the unchanged stored455-node U2set:

|method|sites|unit-noise trace|integer-budget B637risk|sampled/searched norm|
|---|---:|---:|---:|---:|
|full OLS|637|0.696104|0.696104|10.59258|
|A prefix|546|1.059507|0.931100|35.46077|
|same-count restrictedQR|546|1.330361|1.162076|41.39678|
|one-sweep localdet|455|2.097675|1.503942|55.67788|
|stored U2|455|1.617087|1.172706|26.00732|

The primary uses91more sites than storedU2and has36.35%worse searched
amplification, while its B637integer-repeat noise risk is20.60%lower.
StoredU2also loads quickly (0.001251CPU here) and needs no new optimizer
run; its historical offline construction cost remains in usable2.md.
Primary construction is1.195763CPU including setup, every prior operation,
fresh numerical validation and a flushed/fsynced map checkpoint. Actual
full-to-Ndiagnostic Aconstruction is2.212316CPU, reported separately.
Contemporaneous globalQR/one-sweep localdet construction costs are
1.189616/13.807300CPU. Neither point count, solver cost, noise nor norm
alone is silently substituted for the other objectives.

Against full637-node OLS, primary noise risk rises33.76%and searched norm
rises234.77%. Both old strict full-grid-preservation objectives remain
failed. Six of12targets have >1%Chebyshev-RMS regressions versus fullOLS;
worst material RMS ratio is1.75042. Compared with storedU2, all12sampled
Chebyshev-RMS values improve, but uniform-query Gaussian RMS worsens10.54%.
All target/measure/max/RMS/sigma tables and floor effects remain retained;
this is not a generic deterministic-error/noise winner.

The denser endpoints remain diagnostics: n12at501sites has searched norm
56.82292/risk1.234293; at N455it has128.02964/3.275852 and loses the stored
455-node set decisively. A near-minimal useful point does not turn the
minimum-count deletion endpoint into a success.

Actual command/source/input hashes, UTC, versions/threads/seeds and full
logical results are in [P3receipt](evidence/pdpr-frontier12.json),9223bytes.
Raw `/tmp/pdpr-frontier12-20261107a` is regeneration-only. All23distinct
map assessments,28angular searches per map, all controls/functions and
per-deletion curves completed in38.445654CPU/38.455939wall seconds of900,
with no missing/capped work and unchanged source during execution.
New queries used1920+n/1930+n and1940+n for angular search starts; neither
known P1data nor the old strict-prefix count selected n12's primary.
[Engineering](evidence/pdpr-p3-engineering.json)6556bytes adds synthetic
checkpoint-on/off bitwise-path/map/prefix-cost checks and nine finite-
difference checks of the scaled rectangular angular norm gradient to the
previous preflights (all0research rounds).

The [durable P3claim](theory/pruning-p3-frontier.md) is MEASURED. The
[independent P3review](pruning-review.md) passes all23maps/target-noise
tables, all1288stored search values, nine consequential original-mesh
replays and252additional independent searches; the registered ratios
remain unchanged. Formal Claude review remains a separate obligation. Next is a separately published
same-rule degree16transfer, including the modern969-node direct-optimization
control, if authorized by root. No P4science is executed at this boundary.
The original455-node payload remains byte-for-byte unchanged.

## P4 completed: degree16fixed-count transfer passes

P4was prospectively published at55a6a11d before its exclusive timed run.
Actual completed pruning research is now **4/15**, eleven slots unused.
The same A rule at primary1163of1377sites (N969) passes the unchanged
P3tradeoff gate:15.54%site saving; full validated/durable prefix cost
14.231638CPU/14.242147wall seconds; and both risk/norm improve by at least
5%against same-count restrictedQR. Numerical/update/reproduction checks
pass throughout the complete diagnostic path to N, with no missing/capped
work or source changes. This is a finite higher-degree tradeoff, not an
all-degree theorem or the old strict full-grid-preservation success.

|degree16method|sites|unit-noise trace|integer-budget B1377risk|sampled/searched norm|
|---|---:|---:|---:|---:|
|full OLS|1377|0.688839|0.688839|12.74056|
|A primary|1163|1.086437|0.948004|40.88506|
|same-count restrictedQR|1163|1.358398|1.185845|61.04459|
|globalQR|969|6.193240|4.105347|168.33996|
|one-sweep localdet|969|2.519920|1.780536|93.63848|
|modern U2direct C3/C4candidate|969|2.358026|1.674587|71.70775|
|C4fine-row determinant|969|2.225993|1.585151|80.12014|

The primary has20.06%lower fixed-budget risk and33.02%lower searched norm
than restrictedQR1163. Against modern U2it improves risk43.39%and norm
42.98%, **using194additional sites**. Against fineC4these improvements
are40.19%/48.97%, again at the larger count. No969-site control dominates
its risk/norm; no global Pareto optimality or count-equivalent victory is
claimed. The full1377-site grid has materially better noise/norm: primary
risk is37.62%higher and amplification3.209times as large. Old P1/P2gates
remain failed, and preserving all full-grid quality is not claimed.

All12sampled RMS errors are lower than modern U2at both query measures
(with small values near numerical floors explicitly retained). However,
the oscillatory target cos(4x−3y+2z)has **25.70%worse Chebyshev-query
maximum error** versus modern U2(2.97898e-4versus2.36989e-4), and20.45%
worse versus fineC4. Versus fullOLS, six material RMS regressions occur
on each measure, worst51.22%Chebyshev/37.12%uniform. Against same-count
restrictedQR, several sampled target maxima worsen despite better global
sampled amplification/noise. Every individual target/measure/max/RMS/noise/
sigma result remains in the raw tables; there is no universal error winner.

Diagnostic A1066has searched norm88.51708/risk1.258704; at N969it has
326.69193/4.401260, losing the modern minimum-count controls decisively.
These failures remain visible; primary1163was fixed before unseen n16data.
Actual full-to-Ndiagnostic Aconstruction is25.301732CPU, separate from the
14.231638complete primary prefix. Fresh globalQR/one-sweep localdet cost
11.045392/58.711676CPU. Modern U2and fineC4loaded in0.000274/0.000098CPU,
with mandatory original source/inventory/coordinate pins verified before
any candidate computation. Their historical124.202551CPU(C3)and
65.746077extra+58.419101commonCPU(C4)construction costs are clearly
historical, not contemporaneous equal-time comparisons.

The [P4receipt](evidence/pdpr-transfer16.json)10883bytes contains all
original executed-source/input identities, command, UTC/version/seed/thread
metadata, complete logical results and raw inventory. Raw directory
`/tmp/pdpr-transfer16-20261107a` is regeneration-only. All13distinct maps,
28angular searches per map, all original held-out meshes/fresh measures,
controls/functions/variance reports completed in152.343048CPU/
152.433746wall seconds of900. The [P4engineering receipt](evidence/pdpr-p4-engineering.json)
9741bytes adds read-only modernC3/C4provenance/shape/array-hash validation
to all prior synthetic/numerical/cap/checkpoint preflights (0research rounds).

[Durable P4claim](theory/pruning-p4-transfer.md) is MEASURED; distinct
consequential P4review is pending. A compact canonical-ID artifact and
separate exact-cosine determining-rank proof are now justified delivery
work if that review supports the result. Their exact statement must remain
separate from rounded-coordinate norm/noise measurements. Eleven remaining
research slots are a ceiling; no automatic new degree/rule/seed search follows.
The original stored455-node U2payload remains unchanged.
