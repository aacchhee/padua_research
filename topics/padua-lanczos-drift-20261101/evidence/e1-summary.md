# E1 exact aggregate-map calculation

Status: **MEASURED**, with exact rational finite bounds. This is the aggregate
local residual-injection map, not a complete scalar-operation rounding graph.
The latter remains OPEN. Rules/base were read at
`806cc7b4509fd93bae652f9545d32d95529f8281`; developer allocation is Codex
`gpt-6.1-sol`, medium (runtime model/effort metadata not independently exposed).

The completed full sweep has 88 runs: both frozen rational point sets, every
degree 2 through 12, all four rules, and all `N-1` local source blocks.
No fallback was used. A separate 24-run screen restricts sources to degree 2
at final degrees 2, 8, and 12. Restricted-source upper bounds are never used
as full-map upper bounds. All exact outputs, rational square-root intervals,
commands, versions, source hashes and artifact hashes are retained in the JSON
records and manifest alongside this file. Output outside Git is local working
storage, not a claimed final external archive.

At degree 12 the squared sensitivity intervals using the stronger of the two
valid upper bounds are:

| Set | Rule | Lower | Upper |
| --- | --- | ---: | ---: |
| T24 | BJ | 2.0493879359e14 | 1.0859728745e16 |
| T24 | mirror | 3.6550801975e8 | 1.6316358691e10 |
| T24 | alternating | 1.9412657630e10 | 3.3992362099e11 |
| T24 | pivot | 1.2479403793e7 | 1.6145977113e8 |
| rotated Q24 | BJ | 8.8170667576e10 | 1.2841166021e12 |
| rotated Q24 | mirror | 3.6591714188e11 | 3.5641872019e12 |
| rotated Q24 | alternating | 3.9414606242e7 | 6.4187254242e8 |
| rotated Q24 | pivot | 1.4877554349e9 | 1.8969265961e10 |

The original KHS-only sufficient survival criterion is **INCONCLUSIVE**:
the certified BJ-to-best-comparator squared ratio lower bound is 1,269,287.03
on T24 but 62.16361 on rotated Q24. Neither original DEAD condition fires.
The separate mathematically derived `Urow` upper bound certifies the intended
aggregate-map ratio exceeding 10 in operator norm on both sets: squared ratio
lower bounds are 1,269,287.03 and 137.36476. This strengthening was added after
the first small restricted-source run; it is not described as original
preregistration. The freeze JSON records amendment history and the later
best-comparator logical correction. The latter changes no observed verdict.

Developer verification separately differentiates every projection coefficient
and norm at degree 3, and checks equality of the final normal derivative with
the frozen-coefficient propagator. It passed 360 rational-vector equalities
across all nine sources for both sets and all rules, plus 800 pairwise exact
basis checks. This is a separate calculation, but not an independent agent
rerun. The evidence checker passed every source count, exact projector trace,
and rational square-root interval in the 88 full records.

A single-pass binary64 implementation with exact pivot choices frozen was
compared at degrees 2, 8, and 12 (24 cases). Maximum relative error in the
reported lower/upper metrics was 9.005e-8; maximum basis orthogonality
Frobenius error was 5.209e-7. This compares metric calculations, not a finite
perturbation or trajectory-level floating-point drift theorem.

The full sweep used at most four concurrent workers and a 240-second timeout
per exact run. The longest completed run took 150.51 seconds. Peak RSS was not
profiled and no hard byte cap was set. The basis plus current-source arrays
have at most 113,750 rational entries; fraction bit lengths remain variable.

The separate scalar-source follow-up uses new code and evidence. Its upper
bounds apply only to its explicitly declared operation subset; they do not
upper-bound a full arithmetic implementation.

The completed follow-up then fixed one full dense-matvec scalar-CGS2 graph,
as specified in the separate scalar-operation bridge theory. Its formal
relative scalar errors have l-infinity norm at most one. Exact local dual
numbers independently enumerated the declared vector-operation amplitudes
at every degree-3 node/source for both sets and all rules, verifying the
`rho` formula and the zero-baseline second matvec. This is a local source
check, not a full normalized-trajectory replay. The formal model includes a
safe permissive error on subtraction of zero; actual IEEE error realization
is not asserted.

For this declared graph, exact full comparator upper bounds and explicit
many-node BJ sign witnesses give:

| Set | BJ squared lower | Comparator squared upper | Certified squared ratio lower |
| --- | ---: | ---: | ---: |
| T24, pivot comparator | 1.5765963916e16 | 2.3984814436e10 | 657331.07745 |
| rotated Q24, alternating comparator | 8.4020014489e11 | 1.3532944864e10 | 62.08554 |

Thus the factor-10 comparison on **both** sets remains **INCONCLUSIVE** for
the declared full scalar graph. No DEAD inference follows from insufficient
bounds. Post-hoc weaker exact inequalities certify factors exceeding 800 on
T24 and 7 on both sets; their thresholds were chosen after these results and
do not change the original criterion.

The many-node lower uses a fixed target output column, aligns all local
operation errors at each node with it, then chooses deterministic node signs
whose final normal-column norm exceeds the random-sign diagonal expectation.
A separate explicit final projection agrees with each exact reported gain.
The fixed rotated target's preprojection squared maximum is only
1.0912512129e12, less than 100 times the comparator upper, so further sign
optimization for this same target cannot certify the requested threshold.
No more such sign searches were run.

The rotated working witness artifact is 3,626,111 bytes and stays outside Git.
The compact certificate retains exact gains, all node signs, the target
column, and artifact/code hashes. `e1_reproduce.py` reconstructs all capacities
from committed source records and producer code, compares the compact
certificate, and checks an explicitly formed normal projection. A developer
triangle reproduction passed; independent-agent reruns are coordinated by
the orchestrator. External archival of working artifacts is still pending.
