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
