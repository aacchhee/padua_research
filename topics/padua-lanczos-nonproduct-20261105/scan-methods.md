# P6 pre-run scan specification — 2026-11-05

Written before new P6 scans. Rules/input `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
N0 passed separately. This is a technical plan, not an executed result.

## Admission and model

A case requires the owning worker's written N1 admission: genuinely
non-affine-product positive measure, exact rational/algebraic input, and
M>N_s plus injectivity through every scanned degree. For a finite positive
rational measure, supply all distinct triples (x_i,y_i,w_i), w_i>0; no
symmetry reduction or source subsampling. Generic native input is plain text:
first line M, followed by M lines `x_i y_i w_i` as canonical rational strings.
A JSON envelope records family ID, parameters, admission link, model and the
text-file SHA-256. The native implementation treats the family label as an
identifier only and performs no implicit coordinate/weight generation.

Source metric and output: PD-T136/137 aggregate Hilbert inputs and spectral
normal output. Weighted-coordinate formulas must first be proved in a math
worker's record. Exact adaptive pivot rule maximizes residual-square/raw-
product-square; X wins exact ties; choices are frozen at the base run.
The other three rules are unchanged BJ/mirror/alternating. Every case includes
all sources 1,...,N_s−1 and each complete degree2–max-degree prefix.

## Prospective output and guards

Native JSONL output has one row per degree with family/set ID, rule, degree,
source class `all`, source/node/basis counts, canonical rational strings for
L² (`Knode_squared`), H² (`KHS_squared`), Urow² and U²=`min(H²,Urow²)`,
complete pivot choices/ties, exact normal-projector trace and exact Gram
pair-check count. No logarithms or fits occur in the endpoint producer.
Check positive pivots/source scales, weighted Gram orthogonality, normal
projector diagonals in [0,1], trace M−N_s, and 0<L²≤U². Raw rows/logs stay at
`/tmp/padua-lanczos-nonproduct-20261105/p6/`. Short receipts pin inputs,
producer/checker sources, commands, environment, time limits, actual timings,
raw file size/hash and endpoint coverage. No prose hash enters checker pins.

Producer path: copied predecessor common-denominator native GMP arithmetic.
Independent arithmetic path: scalar `mpq_class` native implementation using
per-entry rational arithmetic and its own basis/source loops. Distinct-agent
rerun/audit remains additional: writing two implementations is not an
independent-agent approval.

## Cost pilots and comparisons

First admitted baseline pilot: uniform T24, all four rules, maximum degree4,
60 seconds per case, at most two concurrent native processes; match the
pinned historical sweep. After success, maximum degree16 with 600 seconds
per case. Existing N0 BJ/mirror degrees2–12 may be reused for overlap checks;
new native degree16 rows also include/check that overlap. No max-degree20
run unless degree16 cost is below60 seconds per case and the coordinator
authorizes its next round. New weighted families start at degree4 with the
same60-second cap. A timeout is INCOMPLETE, never a successful row/window.

Dated coordinator cost decision, before any P6 scan: supersede the duplicate
T24 pilot/full-run plan above by reuse of the already accepted PD-T338 full
four-rule degree2–20 evidence after P1's N1 admission. N0 already supplied a
fresh exact BJ/mirror replay. T24 therefore needs no redundant degree16 run;
the new pilot budget is reserved for admitted Hahn/disk specifications.
This changes compute scheduling only, not the endpoints or N2 rule.

For N2, follow the coordinator's frozen `plan.md`: degree8–12 and12–16
least-squares slopes of log(kappa_BJ/kappa_best) versus degree, with
kappa_best=min of the four rule capacities. From endpoint intervals,
q_s^-=L_BJ²/min_R U_R² and q_s^+=U_BJ²/min_R L_R²; take half the outward
logarithms. Extremize signed OLS coefficients at interval endpoints. Both
lower slopes>0.1 pass; both upper slopes<0.02 redirect; otherwise INCONCLUSIVE.
Never infer a verdict from missing degrees or fit before complete8–16 windows.
Outward logarithms must be checked by a distinct arithmetic path before a
certified screen. Finite fits steer proof work only.

## Formula/admission gate completion before round2 pilots

P1 triangle and P2 D36x9 admission proofs and P4-02 weighted normal-quotient
proof were read fully before native weighted implementation or execution.
Input preparation normalizes supplied weights by their exact rational sum;
H24_222 already has sum1, T24/disk equal weights become1/325 and1/324.
Native backends require sum1 and positive input weights. The unmodified
predecessor T24 machinery remains separate and supplies frozen baseline
comparison; generic input support changes only the node/weight interface
and the P4-proved weighted inner products/projector diagonal. No extra
weight is inserted into the Euclidean-source v_hi formula.

## Round3 prospective cost refinement

Coordinator instruction after round2: before degree16, benchmark H24_222 and
D36x9 through degree8 on all four rules, producer first and scalar checker
afterward if affordable, with120 seconds per native case. This is a cost
screen, not N2. Only then launch feasible degree16 cases with600 seconds per
case, prioritizing H24_222. Python's rational integer-string cap is raised
before these runs; no endpoint truncation or approximate arithmetic is used.
Keep every timeout and exact completion mask. Inherited T24 N2 reanalysis
uses the accepted compact outward log enclosures, without duplicate scans.

## Prospective disk16 resource successor

After observing fast disk16 BJ/mirror completion at277.843/313.868seconds,
the coordinator invoked the user's existing6h/run,48hCPU authorization:
preserve original600s producer outcomes, then defer unstarted scalar600s
cases and cancel any that auto-start at that boundary. Record every such
case as actually cancelled/partial or unstarted, with its output identity.
A separate wrapper `p6_disk_successor.py` may select only missing disk16
cases, use3600seconds per case and at most4native processes, and reuse
completed original producer rows without rerunning them. The original
in-flight harness/source hashes stay unchanged. Dataset, source class,
arithmetic/model, all60required rows and N2 scientific thresholds remain
unchanged. A checker speed variant requires a separately pinned exact
equivalence-control receipt and its own code hash before successor use.

The machine reports4cgroup CPU cores and18GBRAM, with~17GBfree and current
producer RSS114–140MB each, so4native processes fit the observed resources.
This is a prospective resource-plan extension, not a retrospective change
to old caps or a new mathematical family/growth criterion.

## Prospective distinct D65x9 pilot

P2's new `theory/p2-04-low-denominator-rings.md` and its delta gate were read
fully before preparation/execution. This separately admitted family has36
directions with common hypotenuse65, nine radii k/9 and equal mass1/324;
its common coordinate denominator is585. It is a different finite measure
from D36x9, whose data/attempts remain intact. New exact generator:
`p6_d65_input.py`; generic explicit-spec route in `p6_scan.py` records exact
specification/native-input hashes and an N1 link at the recorded head.
It constrains the explicit family's max_scan_degree and admission path to
the topic's theory directory; no mathematical checker pins a prose hash.

Run a fresh degree8 cost pilot, four rules and both native paths, sequential
one-worker execution,60seconds per case. The coordinator explicitly permits
this short fifth native process sharing4cores while the original successor
has4active cases; do not pause any old case or change its wall cap. No full
D65x9 degree16 run starts before actual pilot costs and scheduling are
reported. Scientific source model, exact arithmetic and N2 thresholds are
unchanged; runtime benefit is not assumed from denominator reduction.

After the D65x9 degree8 pilot actually passed all28 rows, the coordinator
requested a separate degree12 worst-rule cost benchmark: alternating only,
both backends sequentially,120seconds per case, one extra process sharing
the4cores. `p6_cost_case.py` records the explicit single-rule coverage and
every completed/partial prefix; if both finish, compare all11 exact rows.
This remains cost screening and cannot establish N2's all-four-rule window.
The original D36 successor source/input identities and3600s caps stay fixed.

For the coordinator's bounded alternative-checker resource experiment,
`p6_basis_export.cpp` exports exact basis/creator data only and never source
propagation. Independent FLINT reconstruction must verify fullweightedGram,
all creator relations/source scales and pivot/tie legality before computing
any inverse response. The separate helper's prospective schema,60second
pilot caps, actual runs, dependency/runtime setup and final no-override
decision live in `flint-check-notes.md`; they are not new P6 high endpoints.

## New dated reflection-method successor, before reduced experiments

The earlier no-symmetry runs/plans and their source hashes remain intact.
After the bounded FLINT cost screen failed, the coordinator requested one
last separate implementation variant, proved in `p6-reflection-methods.md`:
reuse squared responses only under the two independent sign flips. No
coordinate swap, measure change, removed node/source, or changed endpoint
formula is permitted. The new source is `p6_reflection_scalar.cpp`; original
producer/scalar sources and in-flight3600s jobs remain unchanged.

Before any reduced pilot, require the written proof and distinct math
review. The implementation must check exact reflected weighted permutations,
full324-node basis/Gram/creators/scales, basis parity, every mismatched-parity
coefficient zero and parent character relation. Its only reduced arrays are
source responses/energies at exact(abs(x),abs(y)) representatives. Expand
them to every original node, using each actual full-node normal diagonal
for all L/H/Urow/upper/trace calculations. All152 sourcepositions at16 and
all degree prefixes remain. Any guard failure rejects the shortcut.

After that gate, run exact degree6/8 full-field comparisons for all four
rules,60seconds per native case, one extra serial process sharing4cores.
Same-maximum-degree baseline comparisons must retain Gram-count equality;
cross-maximum-degree reference slices must separately check Gram coverage
and disclose the count difference. No degree16 adoption before successful
pilots, actual cost report and focused distinct scan/code review. This is a
new dated resource-method variant; N2's data/model/thresholds are unchanged.
