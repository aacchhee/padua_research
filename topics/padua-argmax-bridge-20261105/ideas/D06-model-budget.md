# D06 — Quantitative application of the accepted D05 bound

Rules/input: `7db857380ab99e19998e01e4ce9832496b222a31` supplied by root;
rules were read at `a6d7a788b3ce457a4631bbb507624303240c570c`, unchanged
instructions. D05 accepted report SHA256
`dd0cc60b9d84b6b288d2d508ee60f032d63e2a1fb6b20d36fdda51a2f39e7276`.
Scope: quantitative application of the existing gated D05 candidate,
not a new mechanism/novelty claim. D05's two new proofs were reported
accepted unchanged by distinct Astra xhigh review before this task.

## Preregistration before evaluation

Keep R=2, delta=pi/8 exactly. Evaluate precisely
N={512,1000,2048,4096,10000,20000,50000,100000}, and radian phases
(0,0),(1/4,1/4),(69/50,0),(29/20,29/20),(pi/2,pi/2).
Rational entries are exact rational radians; midpoint entries are
symbolic multiples of pi. No labels treat irrational radians as rational.

Evaluate every D05 error component, without retuning. Actual-phase
values use mpmath80dps and actual a,p,P,d,|U0|,H_n; they are MEASURED
floating planning evaluations, not outward enclosures. The boundary
a=0 and integer Phi_0 limits are implemented literally.

A separate conservative uniform row uses a=1,p=1,P=2,d=1,|U0|=8 and
H_n<=1+log n. All terms are increasing in these nonnegative inputs:
for the entropy term use monotonicity of u[1+log(1+S/u)] in u,S.
This row is evaluated by directed 50-digit Decimal interval arithmetic.
Every logarithm is enclosed between adjacent Decimal values around
its correctly rounded ln value. Pi is enclosed independently by the
alternating rational Machin series 16atan(1/5)-4atan(1/239).
The saved uniform values are upper endpoints rounded toward +infinity.
Their numerical guarantee is conditional on Python Decimal's documented
correct-rounding arithmetic/ln contract and the reviewed scalar code;
they are not an interval phase cover or a kernel computation.

Frozen command before execution:

    python code/post_audit_D06_model_budget/evaluate.py

Run from this topic directory. One process, CPU soft9/hard10 seconds,
including imports/helpers, no native/build/board/integration/phase-grid
call. Save one compact CSV evidence file (<16KiB). Source and output
hashes, actual CPU, every component and results go in the attempt.

Compare totals to 1/32 (usable defect floor from n160) and 1/16
(from n4096), as BUDGET comparisons only. Neither bound alone compares
M_infty with the actual corner; no sampled far margin is a premise.
No all-n inference from sampled degrees: monotonicity must be separately
proved before claiming an entire degree range. No parameter rescue.

## Outcome

One scalar run, .097311284 CPU; all components retained in11121B CSV.
At n10000 actual-phase formula totals are MEASURED .153--.171; uniform
directed upper .277965464778. Exact lower bounds on the frozen e_rows
and quarter-phase I_n prove this formula cannot meet the useful1/32
or1/16 error allowances through n10000. These are failures of the
explicit allowance, not of the true approximation or accepted rate.
The candidate's quantitative useful-budget gate fails in this scope;
no parameter rescue or validated phase-cover release follows. See the
attempt for source/evidence hashes, all degree totals and exact scope.
