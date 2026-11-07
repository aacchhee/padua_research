# Supplementary independent check: D01 frozen corner envelope

2026-11-06. Rules/review input:
`e6549177fe48c7fea8436cece8a04b411dc544e1`.
Developer source/rules input:
`4cf68980fa0538b53e2aea7174ed6e5782a34908`.
Distinct Codex reviewer; requested `gpt-6-astra high`; serving model/effort
metadata unexposed. This supplements the later Claude audit and does not
approve other campaign work. Root alone controls Git and shared records.

## Verdict and coverage

**PASS within the stated scope; no BLOCKING, MAJOR or MINOR finding.**
The primary failure of the specified fully charged C07 envelope is
**PROVED** at n=1000. The finite numerical table and the n=20000 kill
remain **MEASURED**. The failure does not reject every corner estimate,
the optimal actual-function constant, the actual-corner inequality or
global argmax. It establishes no new degree coverage.

Read AGENTS, WORKFLOW, CODEX, handoffs09/08 (including retained taskB),
audit-01-ideas gate section1 and P4, D01 corner idea/attempt/theory,
the complete frozen SPEC, measure.cpp, run.py, build_closure.py and
run-record.md. Read C07-corner-million-onset in full and C05's derivative,
regular normalization and odd sine-channel sections2/4/5. Inspected the
original receipt, manifest, preregistration and build closure. The
upstream all-degree theorems and final campaign audit are outside this
bounded check.

No new mechanism or historical novelty claim is made. This review checks
the already gated Claude P4 implementation under handoff09's explicit
gate-reuse authority; it does not claim a fresh full registry/literature
review. Independently checked that state/IDEAS.md retains the gate's SHA256
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.

## Independent analytic reconstruction

For n=1000, (j,r)=(0,1),(1,0) lie on the odd board and outside the removed
strip r=j+1,2j>=n. At these indices S-1/6=5/6 and g-1/6 equals 5/6 or
5/6+1/1000. Both are positive and strictly below21/25. Every A1,A2,A3
summand at either index exceeds (25/21)^4>2, since
390625>388962. Positivity of all other summands gives A1,A2,A3>4.
With tau>1 and pi^2<10,

    C_f > (16/100)*4+(4/10)*8=96/25.

The strip j=ceil(n/2),...,n contains floor(n/2) interior weight-one
indices and the endpoint (n,n+1) of weight1/4. Thus its weight is exactly
floor(n/2)+1/4 for either parity. At1000,

    C_strip=(28/5)(500+1/4)/1001=2001/715>279/100.

The positive exponential series through degree11 equals
2959911103/2851200=41438755442/39916800>1001, hence log1001<7.
Discarding the nonnegative remainder and sine terms then gives

    K0_C07(1000)>96/25+279/100-7/3=1289/300>4.

This is an elementary exact proof from the frozen object's definitions;
no finite floating calculation is a premise. The review script also
checks the rational comparisons with Fraction arithmetic.

## Charge and normalization checks

The object is exactly K0_C07, not a phase-zero Hessian or a minimization
over possible constants. C07(3) retains the exceptional first-coordinate
mode and takes the absolute value after all four reflected copies.
Regular endpoint weights may be dropped upward, giving unweighted sums.

1. The regular factor is 2/(N n^2). Multiplying the first three terms of
   C07(7) by this factor and substituting its denominator lower bounds
   gives 16tau^3 A1/pi^4 and 4tau^3(A2+A3)/pi^2. The powers and factor4
   from reflection agree with SPEC and both implementations.
2. The remaining four terms give the full C07(13) coefficient C_rem.
   D01 correctly retains that expression instead of the million-degree
   rounding to1/100.
3. The C07(15) coefficient1/(2n^2m), multiplied by the csc^2 bounds and
   inverse-square geometric factors, gives precisely
   50m G2/(9pi^2 n^2)+m(B20+C20)/(2n^2).
4. The two strip symmetric pairs cost (14/5)n rho^2 per index. Division
   by N and rho^2<=2r2 give (28/5)W_B/m, including the endpoint1/4.

These establish the provenance of the candidate allocation. They do not
establish its actual-function inequality at smaller n: the separate
degree-floor obligation stated in SPEC is real and is not discharged by
this review. The exact negative statement needs no such extension.

## Finite reduction and independent executions

Checked the odd diagonal ranges, including l=-1 ending at
ceil(n/2)-1. On omitted k>=129, g-1/6>=k-7/6 and
S-1/6>=2t+k-1/6. Integrating decreasing powers on spacing-two grids gives
the stated H_p bounds; summing the inner t bounds gives all four tail
formulas. The finite-diagonal denominator minima yield a second valid
upper bound, so taking their minimum is legitimate. The odd-S counts
for B20/C20 remove precisely one strip element when appropriate. At the
excluded terminal endpoint the count is zero. No negative denominator
from that endpoint enters a regular sum.

Executed once, from repository root:

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_corner_review/check.py

The [review script](code/post_audit_D01_corner_review/check.py) compiles
the frozen measure.cpp afresh using g++ -O2 -std=c++17 -fno-fast-math,
then runs full native controls at17/1000/1001 and D127 truncations at
1000/1001/10000/10001/20000/20001. It independently enumerates the physical
board in Python, using Fraction at17 and rowwise fsum at1000/1001.
Its g is formed from the integer numerator |(n+1)j-nr|, and it does not
reuse the native diagonal grouping, term function, B20/C20 grouping or
the production runner. Counts and all six sums agree; maximum relative
differences are0,2.046e-16,4.092e-16, respectively. Independent full sums
lie inside the positive-tail brackets. Both parity cases are exercised.

| n | Independently recomputed K lower | K upper |
|---:|---:|---:|
|1000|9.060120982745708|9.062836218852432|
|1001|9.062020668397757|9.064737064911427|
|10000|8.956214482845258|8.960356017728555|
|10001|8.956405437248646|8.960546996951647|
|20000|8.927956689916323|8.932231475509306|
|20001|8.928052197816330|8.932326990655131|

All agree with the original receipt within1e-12. Primary<=4 and weaker
alternative<=7.8 fail. At20000 the lower endpoint exceeds the fixed kill
threshold6.506826419211471. The100000/100001 rows were inspected and
their original output identities verified, but were not rerun. No new
degree, full phase scan, original-run overwrite or rescue was attempted.

These are floating truncation envelopes, without directed-rounding
certification. Analytically justified tails do not turn their numerical
endpoints into certified intervals. The status remains MEASURED.

## Provenance, CPU and retention

The independent [receipt](evidence/d01-review-corner.json) is12087bytes;
SHA256 `21ffc47fc704a543b1c940a03380ff90c6325dc8c0fbf14e2aea33fefaa8db15`.
It pins review/production source, compiler, fresh binary, original
receipt, every executed command and raw output identity. Output is under
`local-output/argmax-bridge-20261105/post-audit-D01/corner-review/`;
physical cold-storage transfer remains pending.

The reviewer measured2.057207 aggregate CPU seconds through checks,
including Python, compilation/helpers, native runs and provenance
verification; the final printed sample was2.057652. This is below the
assigned20-second cap. Receipt writing and final process teardown are
outside the stored through-checks number, not claimed as separately timed.
All commands exited0.

Rehashed369 distinct original provenance files successfully, including
the original61,263-byte manifest, preregistration, compiler and named
gcc helpers, mapped native/Python identities and all253 build-dependency
records. Frozen source SHA256 values agree:

- measure.cpp: ab5b8154dac29336caf50ab822bbcc8b27659a4ef32102920125d669679c8891
- run.py: 6b25fc4735f0c5f9299e6e6b13da3140ca323213baf4706d3c715296e9e3b454
- SPEC.md: 5db165cee96f1011fcac0a92286632177f44d7502e9d41a6d3d08539e48c5000

The developer's2.511748 controller CPU,2.524 complete shell-tree CPU and
0.120 postrun helper CPU are separately labeled;2.644 is their recorded
shell-observed total, not a timing recreated by this reviewer. The
original missing-/usr/bin/time failure remains in run-record.md as a
pre-execution wrapper failure; no numerical failure or source retuning
is inferred. Closure describes captured checkpoints and named build
inputs, not every transient compiler mapping.

No developer mathematics, source, evidence, audit or shared record was
edited. No remaining run is needed for this bounded supplementary check.
