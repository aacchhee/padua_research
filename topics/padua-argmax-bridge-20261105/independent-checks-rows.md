# Independent mathematical supplement — N1/N2/N4/N5 round 1

2026-11-05. Distinct Codex checker `/root/check_rows`, assigned
`gpt-6-astra high` by handoff01/parent; serving model and effort are not
independently exposed. Rules read at full commit
`0bca52bc1b8edf2e91d3749b710d2df285dc3e6b`. Only assigned checker files
were written; no author, shared-registry or Git mutation. This supplements,
and cannot replace, the required Claude audit.

## Disposition and frozen scope

**No substantive mathematical finding** in the six scoped theorem files:
N2 exact rows, N5 block quadrature, N1 uniform row assembly, N4 unrestricted
transport, N4 generic variance rigidity, and N4 exact diagonal positivity
classification. Their PROVED mathematical claims are supported by the
written arguments under their precise hypotheses. This is no approval of
registry changes, external novelty, PD-T099, a compact model, B3, or B5
unrestricted infeasibility.

| File in `theory/` | Reviewed SHA-256 |
|---|---|
| N2-row-decomposition.md | `40201cc3abe826e0c43d4b93f47511fc3b81bdb3a5e8b96d01ce4bc84bfa2604` |
| N5-partial-cotangent.md | `9b2e332d771be405aaed38849fa18618831313a9414b8131cd0e4cd7084eadb0` |
| N1-row-model.md | `d087ad8374c9e8274c5d228a47a7f796a8c64d412255a7362c0ea68863c14250` |
| N4-unrestricted-transport.md | `e7835c5fef239c72e3758caef6d7ec640487c29444df7583f0a72a013e5eec89` |
| N4-variance-rigidity.md | `f32de9ecd18c8d39ad04bdd1758cd0edc1839936fc331fe0d1800e63a2c3ff68` |
| N4-diagonal-translation-obstruction.md | `3fe6e396e37c523166d6da98ce46974cfb0e3b5a031c461466cf25c979b167e8` |

The original N2/N5 freezes were respectively `650a2b87c38842e5a5c26ffa572d4b4e751c1839cd5fe19aceefed96b8e7cfbe`
and `4b8438e820a5255b9c40d7a4530fa7143bd3a22218024291b6e3533bcbc00c6c`.
Reversing only the coordinator's `-codex-` provisional-prefix insertion
and removing the new normalization History section reproduces those exact
hashes. No mathematics changed. N1 was finally frozen by the parent at
commit `714f3ca`, after the checker read the earlier mathematical body;
the final file was read again. Round-2 N1 files are outside this report.

**Minor finding R1 (reproducibility only).** In `code/n2_rows.py`,
`identity` at line151 calls `path.relative_to(ROOT)` without resolving a
relative CLI path. The actual command using relative `--output` passed
all assertions and wrote its raw output but raised `ValueError` during
receipt generation. An absolute `--output` succeeded without modifying
the code. The documented default is absolute and works. Suggested author
repair: resolve the path before relativizing, or document the absolute
path requirement. This is not a mathematical or default-command blocker.

## Independent reconstruction

### N2: finite rows, sign arcs, collisions and predecessors

Summing the finite corrected Fourier polynomial over one parity row
annihilates x frequencies1 through n−1. The constant x mode leaves the
one-variable Dirichlet polynomial; the top x coefficient is exactly one.
Thus the signed row is `n[A−sin(beta)cot(v/2)]`, and summing the 2m rows
leaves `2nm cos(alpha)`. Replacing this by a symmetric cosine expression
would be wrong. The cotangent coefficients follow directly from sine
addition and `cos u−cos v=−2sin((u+v)/2)sin((u−v)/2)`.

The denominator-negative arc and numerator-negative sine arc give the
symmetric difference for regular negative entries, with at most four
arc endpoints. Numerator-zero endpoint choices contribute zero. At a
collision, differentiation of `T_n+T_(n+1)` gives exactly
`(epsilon*n*sin(alpha)−m*sin(beta))/sin(v)−cos(alpha)` for Q. The negative
part must be restored separately. A concrete check is n2, alpha=pi/5,
beta=4pi/5, j=r=1: u=v=3pi/5 and
`Q=sin(pi/5)cot(3pi/5)<0`. This also demonstrates that T226's positive
axis-collision assertion cannot be extended without the new correction.

At endpoint coincidences direct derivatives give
`G(0,0)=2nm`, `G(pi,pi)=2n(-1)^n`. For beta tending to0 the exceptional
r0 row tends to `n(A−2m)`; for beta tending to pi the last row tends to
`n(A+2m)`. Other signed rows tend to nA. These are limits of complete
finite rows. No isolated singular cotangent is evaluated.

Read T226 in full and checked its factor-two conversion Q=2F, its
beta-zero coefficients and signed endpoint row. Read T365 in full and
checked A=0, p=q reduction, the odd-board CRT bijection, absence of poles
on open edges, and the limiting vertex values1. Separate phase
reflections preserve the board; no swap of unequal meshes is used.
N2 extends the parameter/sign domain of T226, while its CRT rewriting
alone is equivalent to the inherited numerator.

### N5: exact corrected-midpoint constant and uniform pole extraction

For the functional on a cell of length h, the Taylor integral remainder
yields `K(t)=(h/2−t)^4/(24h)−h(h/2−t)^2/48`. This kernel is nonpositive.
Independent integration gives `2 integral |K|=7h^4/5760`; the exact
rational t^4 test gives `−7h^4/240`, hence the same coefficient after
dividing by24. This verifies both the correction's sign and constant.

After deleting poles0 and pi, the remaining poles lie at least
`pi(l−1/4)` from J=[−pi/4,5pi/4] in each of the two half-lattices.
The paired partial-fraction series converges uniformly, and derivative
series converge absolutely. Independently summing the first term plus
the integral tail gives `1216/243`, hence
`M4<=19456/(81pi^5)<4/5`. The local Fourier-series derivation of the
partial fraction, and W'=w including both removable endpoints, are valid.
Every centered sample cell lies in J for n>=2. Telescoping adjacent cells
therefore gives the stated `1064/(3645pi^5)` constant, strictly below
7/7200. Block count does not enter because total sample counts add.
Coefficient weighting uses absolute coefficients and remains valid with
arbitrarily small pole distances. Exact pole samples remain excluded;
no cancellation of formal zero times infinity is licensed.

### N1: all-phase weighted assembly

N1 retains rows0 and2m−1 exactly, thereby removing the only coefficients
that can diverge at beta0 or pi. Each remaining cotangent channel has at
most n nonpole samples; wraps and excluded collisions merely split those
samples into blocks. The exact polynomial collision negative parts have
zero approximation error. The bound is applied at the actual phase's
membership, so sign-set transitions require no continuity of an enumeration.

For interior rows, independently using
`|p−X|+|p+X|=2max(|p|,|X|)` with X=q+A cot(v/2) gives
`|C|+|D|<=1+a|cot(v/2)|`. Here p,q>=0 and a>=0 on the reduced diamond.
Distances from v to0/2pi are at least
`pi*min(r,2m−r−1)/m`, giving exactly two occurrences of each integer1
through m−1. Therefore the coefficient sum is at most
`2m+(4am/pi)H_n`. Multiplying the channel remainder by2, then dividing
by nm, produces exactly
`7pi^4/(1800n^4)+7pi^3 H_n/(900n^4)`.

The pi row at beta0 is finite; its possible collision is excluded from
both cotangent channels and supplied polynomially. The vertices and
other endpoint rows are covered by the exact-row prescription. The
all-phase/all-degree error claim is sound. The representation retains
O(n) outer rows and exact shifted reciprocal sums; it supplies no
fixed-size continuous model or certified maximum comparison. N1's row
identity overlaps N2 and is correctly kept as verification, not a second
independent result.

### N4: unrestricted iff, generic rigidity, and exact class restriction

For M>=0 with column sums<=1, `(Mv)^+<=M v^+` and the analogous negative
part inequality prove the two mass necessities. Conversely columns
`w^+/P(v)` on positive inputs and `w^-/Q(v)` on negative inputs give the
transport and the required column sums. Empty sign classes are skipped;
the mass conditions then force the corresponding output mass to vanish.
Thus zero inputs, zero positive mass and zero negative mass are covered.
For equal unit sums both inequalities reduce to the same l1 comparison.

Reproduction of coordinates and their squares gives
`integral |y−z|^2 dmu=0`, proving the generic probability-mixture rigidity.
The nonnegative-cardinal iff-node corollary follows by choosing the
node-supported cardinal measure. Integrability is sufficient and stated.
This excludes full evaluation-vector mixtures; it excludes neither a
nonnegative matrix on signed vectors nor other features. Retain one N4
home for this generic lemma; an N6 use is an application, not a duplicate.

In the mode-diagonal class, transport forces every eigenvalue to be
`q_ab(c)q_ab(z)` because no mode vanishes at c. This fixes the entire
operator, whose constants force column sums1. Its B00 column is L(−z);
rigidity forces −z to be a node whenever the matrix is nonnegative.
Conversely, if z lies on the complementary grid, the four cosine
translations preserve even parity after periodic reduction and folding,
so each matrix entry is an average of four cardinal zeros/ones. This
proves sufficiency including endpoints and repetitions. The center is
never a tensor node for consecutive meshes; n3's B00 entry is exactly
−1/8. This rules out only the specified exact diagonal class. Arbitrary
non-diagonal transport and PD-T099 survive. Mixing diagonal maps cannot
escape the same forced-operator argument.

## Coverage, novelty and execution

Read AGENTS, WORKFLOW and CODEX in full; bridge handoff01 and novelty
baseline; complete1015-line `state/IDEAS.md` including every obstruction
and disposition table (large truncated views were recovered by smaller
ranges). Registry SHA-256:
`948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6`.
Read full bridge N1/N2/N4/N5 gates, their candidate files, and the six
scoped theory files. Full predecessor reads include gated/CANDIDATES
(IDEA327–333), effective ideas/r1-r2-r5 (336–338), phase2 ideas/H2-H3
(455–461), effective ideas/r6-spectrum (345–346), T226, T365, N084 and
N132. Those direct comparisons support the variant/consolidation
classifications, without an exhaustive external novelty verdict. No
external paper or source theorem is a premise of this supplement.

Actual commands ran from `/workspace/padua_research`; every output uses
a new checker-owned path under `local-output/argmax-bridge-20261105/check-rows`:

- N1: `python topics/padua-argmax-bridge-20261105/code/n1_rows.py --output local-output/argmax-bridge-20261105/check-rows/n1-rerun.json > local-output/argmax-bridge-20261105/check-rows/n1-rerun.log`.
  Reproduced125 cases at n2,3,4,5,8,17,33,48, including69 collisions,
  no sign mismatches, maximum error/r_n0.005277861793469796. mpmath70
  digits; signed/cotangent residuals at most3.204e−51. The environment
  transition lost the process handle after completion; the complete raw
  JSON and final summary log were collected without restarting the run.
- N2: `python topics/padua-argmax-bridge-20261105/code/n2_rows.py --output /workspace/padua_research/local-output/argmax-bridge-20261105/check-rows/n2-rerun-absolute.json --receipt /workspace/padua_research/local-output/argmax-bridge-20261105/check-rows/n2-rerun-absolute-receipt.json`.
  Reproduced195 cases,42 collision entries,84 open-edge cases,28 vertices,
  no sign disagreements; maximum signed-row residual1.308e−11 and
  absolute-primitive reconstruction residual8.469e−13. Binary64 only.
- N5: `python topics/padua-argmax-bridge-20261105/code/n5_partial_cotangent.py --output local-output/argmax-bridge-20261105/check-rows/n5-rerun.json --receipt local-output/argmax-bridge-20261105/check-rows/n5-rerun-receipt.json`.
  Reproduced130 cases at n2,3,7,33,128; maximum error/bound
  0.1103770969823691. mpmath110digits, no outward enclosure.
- N4: `python topics/padua-argmax-bridge-20261105/code/n4_exact_invariants.py --raw local-output/argmax-bridge-20261105/check-rows/n4-rerun.json --summary local-output/argmax-bridge-20261105/check-rows/n4-rerun-receipt.json`.
  Exact rational cyclotomic rerun passed n3–8 and4871 translation columns.
- Own implementation: `python topics/padua-argmax-bridge-20261105/code/check_rows_independent.py`.
  No developer-code imports. Chebyshev recurrence evaluates every kernel;
  rational phase fractions detect collisions exactly. At100 decimal
  digits,108 cases at n2,3,5,8 include74 interior collision entries,
  of which18 are negative, vertices, axes, boundary collisions, and
  offsets10^-20 from axes/boundary. Largest model error/r_n0.004769929571;
  largest row/cotangent/collision residuals4.115e−98,5.790e−80,2.804e−99.
  Exact rational quartic and four zero-mass/transport constructions pass.

The checker-generated metadata inside unchanged developer programs still
says developer/PENDING; this report and its independent manifests identify
the actual rerun role. They do not overwrite the original developer receipts.
All numerical diagnostics are supplementary; the analytic proofs carry
the universal claims. Small receipts record source/output identities;
raw reruns remain off Git. Cold-storage archival is pending and is not a
proof dependency. Required Claude audit and full bridge closure remain pending.

Final freeze check: all six theorem hashes above were rechecked after
all executions and remain unchanged. The independent execution manifest is
[evidence/independent-rows-reruns.json](evidence/independent-rows-reruns.json);
the separate own-implementation receipt is
[evidence/independent-rows-diagnostics.json](evidence/independent-rows-diagnostics.json).
