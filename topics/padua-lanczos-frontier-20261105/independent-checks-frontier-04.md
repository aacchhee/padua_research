# Supplementary mathematical review — frontier handoff04

Reviewer: `/root/g0_review`, configured gpt-6-astra high. Main reference
`aff30e8`, integration/read head `bb67c1ee830d468fa33007e15008d5574d00ccf4`.
No Git mutations or silent model substitution. Initial ownership is this
report; root subsequently authorized `code/g4_independent*` and
`evidence/g4-independent*` for the separate stopped G4 diagnosis. No earlier
L1/L2/L4 accepted proof or successful check is rerun or changed here.

## Reading and protocol boundary

Rule SHA256 values match the previous complete reads:
AGENTS `c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b`,
WORKFLOW `423e1bc005d61aaaec38a9d38660f48644618850590c53110b595898a41bde21`,
CODEX `28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b`.
The first commentary named supplied main aff30e8; the actual integrated
branch read head is bb67c1e as recorded above.

Read the complete handoff04, saved attempts/L3, all424 lines of
ideas-l3-l4 including historical corrections and final dispositions, and
new ideas-l3-continuation before reviewing the stable L3 claim. The prior
complete registry/source gate and later handoff03 delta reads are retained.
For this continuation, read the entire main registry delta since0e493be:
the revised IDEA117 and all new IDEA376–379 entries/dispositions. Read all
four canonical NN-MOP candidate entries, the full PD-N100 literal-dictionary
counterexample, and complete PD-T288/289 divisor/reconstruction records.
Read the entire corresponding PROOF_STATUS and literature INDEX additions.
The new exact divisor theorem supplies nonvanishing, not magnitude bounds;
the reconstruction supplies no stability or finite-error selection theorem.
The fixed-site failure does not refute commuting diagonal coordinates.
No global novelty or primary-literature clearance is inferred.

Fresh complete predecessor reads for L3: PD-T142, PD-T143 including its
family-dependent remainder correction, PD-T046 with its near-breakdown
factor/correction, and PD-T054's staircase/acyclicity theorem and limits.
A combined PD-T046/054/ideas display was truncated in the middle; the
missing PD-T046 ending and PD-T054 beginning were recovered in bounded
views, and the remaining ideas ledger was read separately. Unseen truncated
text is not credited. Prior full IDEA246–267 and relevant obstruction
reading remains inherited, rather than another fresh read. The historical
prospective-gate timing deviation remains for Claude's explicit disposition.

The saved L5 attempt was read as preparation only; no L5 reduction or
certificate is accepted in this report yet. No new primary paper or old
experiment was executed during these reads.

## L3: explicit finite-error selection proof

Complete reviewed initial draft:
`theory/l3-finite-u-selection.md`, SHA256
`cdcf4214a6ae251db66954baeb3cfce41a2c17340ab2a85220dfd988164c3a8a`.
**Mathematical disposition: independent reconstruction passes.** This is an
analytic check, with no numerical/symbolic experiment and no scientific code
required. No substantive mathematical defect was found; the developer proof
was not silently edited by the reviewer.

The checked model is exact full projection/normalization with the sole local
source budget `||e_k||<=u lambda_k ||A_k qhat_parent||`. Errors can be arbitrary,
history-dependent and nonsmooth. This is stronger than PD-T143's derivative-
only Hres assumption and distinct from a scalar/IEEE implementation.

Independent reconstruction:

1. Equal-rank orthogonal projector distance is the largest principal-angle
   sine, hence at most the difference of the corresponding orthonormal frames.
   This gives the prefix bound uH from already constructed columns. The
   residual difference splits into the current raw-product/source difference
   and the projector difference acting on the exact product of norm v_k.
   With u<=1 these are precisely the saved C_k terms. No unknown current
   pivot or coefficient is used in this estimate.
2. Reverse triangle inequality gives betahat_k>=beta_k^*(1-ub)>=beta_k^*/2
   before normalization. The normalized vector difference is at most twice
   the residual difference divided by the exact beta_k^*, so h_k=2C_k/beta_k^*
   closes the induction. Exact projection supplies orthonormality at each
   completed step. Zero source budgets and zero radius denominators are
   handled by the stated infinity convention.
3. Expanding the coefficient difference with one exact raw product gives
   D_kl. Perturbing the pivot denominator adds the two stated inverse-pivot
   factors; the creator's parent entry contributes the separate
   `2|alpha_ki|C_k/(beta_k^*)^2` term. Summing squared entry bounds supplies
   the Frobenius-to-spectral Delta bound, so Neumann inversion applies when
   uKDelta<=1/2. The normalized node matrix, rather than an unnormalized
   propagator, is used consistently.
4. The source norms satisfy
   `epsilon_s<=u(F+uJ)/(1-ub)` by the perturbed-parent bound and Minkowski.
   The exact orthonormal computed columns make PD-T142's smallest-singular-
   value factor one. Inserting the Neumann bound gives B_R(u). Subtracting
   uKF leaves the exact numerator
   `u^2 K[J+F(b+d)-uFbd]`; denominators are at least1/4, giving the displayed
   uniform quadratic coefficient. No C²-family or hidden second-order source
   constant is assumed.
5. For lambda_k=C_loc the leading F bound agrees with the chi-explicit
   PD-T143 coefficient under the stated filters. For arbitrary finite
   selection classes, the maximum positive radius guarantees at least one
   accepted path. The tolerance refinement follows from
   `B_R(u)<=4uK(F+J)` and preserves positive finite-degree acceptance radii.
   The exact comparison/computability claim is correctly limited to suitable
   represented inputs; certified upper enclosures give conservative acceptance,
   not automatic exact minimizer decisions at unresolved ties.
6. The adaptive corollary proves the next pivot using a complete admissible
   extension of the currently chosen prefix before referring to a completed
   realized path. Shared prefix constants depend only on that prefix and the
   fixed per-column budgets. Taking the minimum over all path radii therefore
   makes every next step valid; only then does the realized complete path
   enter the fixed-path theorem. Exact-data ties and discontinuous choices
   require no branch gap or derivative. Non-(C) paths acquire no implicit-
   section interpretation.

The initial scope wording is being sharpened to distinguish proved
finite-degree positive-radius existence from unproved degree-uniform useful
radii, polynomial score/radius bounds, or acceptance at a prescribed u
uniformly in degree. This is a scope clarification, not a formula repair.
A final metadata impact check will be recorded once the developer updates
status after reading this report. The required later Claude audit remains
separate; this scoped theorem does not settle the broader L3 safety target.
No unresolved structural issue here requires an xhigh escalation.

## G1: exact common-denominator representation review

Read complete `g1-optimization.md` and the155-line initial `code/g1_fast.py`
(source hash supplied before execution:7dbc7ecb609ee5db9ebcb9a52bf39f13e5273ccfebc330791223ca2923f49f3b).
**The mathematical representation/reordering is sound; implementation/run
acceptance remains with the distinct technical checker.**

The vector value is integer row divided by a positive common denominator.
Sign normalization, zero handling, division by common content, lcm addition,
rational scalar multiplication, exact integer dot products and componentwise
products/squares preserve each component. Arbitrary-precision integers avoid
machine overflow. Maxima compare integers only after conversion to one
positive denominator; equality retains the earlier source.

The source accumulation is mathematically unchanged. At each degree endpoint,
all sources through that endpoint have contributed before `finish` runs.
The trace is the dot product of the common normal diagonal with the full
source-energy sum. The row upper is its unprojected node maximum. The impulse
lower may take the source maximum before multiplying by the nonnegative
source-independent normal diagonal, then take the node maximum. Witness ties
use minimum(source,node), matching original source-major strict updates.
No node/source compression, parity assumption, gauge change or floating
comparison is introduced. Fresh-degree/pivot/full-Gram controls and all88
old endpoints, followed by the bounded BJ14 benchmark, remain required.
This reviewer has performed no G1 computation and accepts no new row or fit.

## G4: stopped replay and pending independent attribution

Root separately authorized a bounded explanation check after all12 saved gap
screens failed. Read full g4-methods.md, compact g4-replay.json and the first
prospective attribution source. The unchanged old/new tables include large
BJ/xy changes, rotpi4 mirror near-unit gaps, and materially distinct small
alt/adapt discrepancies. Only dev is entrywise identical to upstream_yx.
Consequently yx evidence alone cannot resolve every failed method class;
this missing coverage was raised with the developer and root before any
acceptance. The developer is extending the bounded controls to the other
classes. Historical Q/H/dispatch remain unavailable; prior G0 acceptance is
context, not a blanket waiver.

One diagnostic harness issue was caught by the developer: regenerating the
rotated coordinates inside different BLAS kernels changes the inputs. The
rejected artifact is retained; workers now load one frozen P/w/n input and
must match the original replay input hash. This is separate from the initial
replay mismatch. A class-level explanation must quantify reference error,
local residual scales and their normal propagation on the actual high-degree
instances, together with precision/kernel controls and their limitations.
The registered explanation-quality screens are not replacement replay
tolerances. Actual distinct independent execution is still pending; no G4
resolution or L7 suite authorization is issued here.

## L3 final metadata impact

Accepted final theorem SHA256
`d42f4e89795349c94e59209527e05f8b41039142bac4e78d8eed39e892768a96`.
The final review/status metadata and sharpened scope preserve the accepted
formulas and proof. In particular, fixed-degree acceptance at the explicit
positive radius is proved; useful degree-uniform radius/score control or
acceptance at prescribed u/filters uniformly in degree is not. This is the
intended scope of the initial mathematical PASS, not a new claim or rerun.

## L5 analytic finite-certificate reduction

Reviewed full `theory/l5-01-finite-optimal-radius-certificates.md`, SHA256
`c684b6bbbedc44a8d23730dd9a43ef5aaf75d8f63848c282c4306a2bf20a26ce`,
full attempts/L5.md and ideas-l5-continuation.md, and fresh full PD-T075,
PD-T059 and PD-T065. The inherited relevant full gate and this handoff's
registry/linked-record delta remain as recorded above. No new primary source
or priority claim is introduced. This is a bounded high-allocation analytic
review; no new structural mechanism requiring xhigh was found.

**PASS for the stated analytic reduction, not for any finite bracket.**
A matrix over the specified real algebraic field has the same rank over R,
by its minors. Thus the certified full first-jet kernel controls arbitrary
real polynomials. Nonnegativity on full positive-radius balls forces their
node gradients to vanish. Positive balance and nonnegative evaluations
force every supported evaluation to zero; full column rank then excludes
any nonzero candidate. Monotonicity gives the upper bound on the optimal
radius, without restricting to a generator image or to field coefficients.

At an infeasible positive radius, every coefficient-sphere direction has a
strictly negative evaluation. Moving that point to an interior rational
translation preserves strict negativity. A finite subcover gives a finite
set whose evaluation vectors surround zero in their full-dimensional convex
hull. Their cone is all of R^d; representing each negative vector and adding
the relations produces a dependence positive at every selected point.
An F-nullspace basis and rational approximation of its real coordinates
preserve both exact dependence and strict positivity. This proves existence
of a finite certificate, not completion within the proposed search grids.

The lower proof uses all Taylor coefficients, |h_x|,|h_y|<=||h|| and
lambda_min(H)>=det(H)/trace(H)>0. The displayed coefficient-sum inequality
therefore gives nonnegativity on every direction and boundary of every
full ball, including zero exactly. It is a sufficient lower certificate,
not an optimality statement. PD-T065 does not supply the missing general
kernel equality; the new full-J/rank checks correctly avoid assuming it.
The known Taylor validation component is identified as a predecessor.

A minor general-definition convention was sent to the owner: for arbitrary
Z the feasible radius set can be empty, so defining the supremum in
[0,+infinity] with sup(empty)=0 removes an edge ambiguity. The Padua
application is unaffected. This is not a blocking flaw in either certificate
implication. Actual G3 brackets require exact code, data and distinct executed
checking; none was run or accepted here. Original U2 and the all-degree gate
remain OPEN/blocked.

## G1 revision2 representation impact

Reviewed revised full code/g1_fast.py, SHA256
`963d61bc13e4bfe90776be3d76f1b613a3191f3447e3ce0b918c0cdca1be5a22`.
Lazy cached integer tuples are safe under the implementation's immutable row
usage. Keeping unreduced positive-denominator pairs per original node and
comparing by integer cross multiplication preserves exact maxima. Strict
source updates preserve the earliest source at a node; the final exact
normal-weighted comparison and lexicographic(source,node) tie rule preserve
the original positive endpoint witness. The all-source stage accumulation
is unchanged. No new mathematical concern, own execution, or endpoint/fit
approval is asserted; the distinct technical port remains separate.

## G4 actual independent execution and supplementary disposition

**RESOLVED at arithmetic-kernel/roundoff-amplification class scope.** This
supplementary assessment is based on the actual high-degree inputs and all
five distinct method classes on each of the two cases. It is not an automatic
waiver from G0. The original replay discrepancies, failed diagnostic screens
and STOP history remain true and must be retained. Root owns the final gate
record and any authorization to start the L7 suite. No theorem is invalidated
or upgraded here; later Claude audit remains separate.

Executed own `code/g4_independent.py`, SHA256
`a7d0274b0f93d4d3ba32d6ebf34042f728f90f4ce6c7ac5cf250e2326520ac0b`,
with compact receipt `evidence/g4-independent.json`, SHA256
`d0a0a27d00345fed86cdb09500e3bea62b9eee0df2ee01efddbd2e35fdc601f7`.
Elapsed118.303 seconds, exit0. This is genuinely new independent arithmetic
on the saved producer Q/H arrays, not a second algorithm execution. No
producer reference or propagation helper was imported. The unchanged frozen
E6 reference was regenerated and then checked against an independently built
384-bit Arb full-monomial projector on each actual binary64 node set. All
local source pins and saved baseline input hashes were checked. Inputs have
1681 nodes, n24/325 columns (rotpi4) and n20/231 columns (triangle).

Reproduction command, from repository root:

```
OPENBLAS_NUM_THREADS=1 OPENBLAS_CORETYPE=Haswell PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B topics/padua-lanczos-frontier-20261105/code/g4_independent.py --raw-root /tmp/padua-lanczos-frontier-l7 --receipt topics/padua-lanczos-frontier-20261105/evidence/g4-independent.json
```

That command requires the manifested external Q/H arrays (or fresh developer
regeneration of them); it is not a claim that temporary files were archived.
The small receipt contains each loaded Q/H hash and path. Historical Q/H and
historical runtime dispatch remain unavailable.

The independent calculation forms every local recurrence defect with
long-double explicit component sums, then solves the normalized frozen
triangular error recurrence. It removes the checked polynomial reference
space from both the observed Q and propagated error. This implements the
polynomial identity behind PD-T142 independently of the developer's dot-based
routine. For upstream yx, parents were reconstructed independently from the
multi-indices and reversed coordinate ordering. Other actual parent paths
are loaded from the per-column guarded producer artifacts; all paths agreed
between the two binary64 kernels, including adapt. The developer's extended
path comparisons were also inspected and agree on these instances.

Measured outcomes:

| Independent quantity | Rotpi4 n24 | Triangle n20 |
|---|---:|---:|
| Reference component outside exact-node monomial span | 6.69944e-13 | 8.42832e-14 |
| Maximum Arb entry radius in that check | 1.59065e-77 | 4.59665e-67 |
| Reference Gram discrepancy | 1.68852e-15 | 1.61609e-15 |
| Largest local residual / (u times operation norm sum), all binary64 classes | 0.724399 | 0.755995 |

All20 binary64 cases, spanning10 distinct case/method pairs, pass the
prospectively stated explanation-quality test. The largest independent
normal reconstruction defect divided by the smaller of actual normal error
and interkernel normal change is0.00162416. The largest corresponding
reference-noise ratio is0.000226020, from the smallest triangle adapt case.
Both are below0.01, with no changed cutoff. Own reconstruction differs
slightly from developer results because its long-double summation ordering
is different; agreement at this scale is measured, not bitwise asserted.
The original small-gap method classes were checked individually; they were
not inferred from yx. Rotated mirror near-unit normal error was also checked.

Together with the inspected developer controls, this gives three distinct
pieces of evidence: local recurrence defects have ordinary u-scale size;
the actual frozen recurrence amplifies them into the observed normal errors
with much smaller reconstruction defect; and changing binary64 arithmetic
kernels changes those normal errors materially while extended precision
substantially suppresses them. The latter is corroborating developer evidence,
not an independent extended-precision rerun by this reviewer. The developer's
extended inverse reconstructions are themselves precision limited and are
not offered as exact accounts of the much smaller extended errors.

The historical gaps are compatible in scale with this demonstrated
mechanism. Their precise historical trajectories are neither recovered nor
bounded by the two-kernel sample. In particular, no empirical min/max envelope
is used to enclose an unknown historical result. The reference errors are far
too small to explain the replay variation, while the measured local-source
propagation accounts for the current errors and the kernel changes at the
actual degrees/methods. This supports explaining the mismatch class under
the existing 'any unexplained mismatch stops' criterion, without replacing
that criterion with bit equality or relaxed tolerances. The exact historical
provenance limitation is retained explicitly rather than mislabeled as a
successful historical replay. Final singular values are binary64 diagnostics;
this entire attribution remains MEASURED, not a certified numerical theorem.

### L5 convention impact

Owner implemented the nonnegative extended supremum convention and recorded
its origin; reviewed updated definition/history at SHA256
`8a43ca4dcf1283fd7b9fcab8a6d0713696daff2167fd8402547b92d7646e84db`.
This closes the nonblocking arbitrary-Z empty-set ambiguity. The certificate
implications, proof and Padua application are unchanged; analytic PASS stands.
No finite data execution or G3 claim is added by this metadata impact review.

### G4 receipt packaging and final scope check

Compacted JSON whitespace only: receipt 13777 bytes, SHA256
`d0a0a27d00345fed86cdb09500e3bea62b9eee0df2ee01efddbd2e35fdc601f7`. Parsed data equality with the original
19,026-byte receipt was checked before replacement; no scientific field,
number or result changed and no numerical rerun occurred. The original
pretty-printed receipt hash was `06c6b4e8f748d547992281e24361567987c40a725cc9486c56f35816b26688c7`.
Read full g4-disposition-04.md: its class-level resolution, historical
limitations, actual independent-execution description and still-unrun
natural-suite boundary agree with this acceptance.

## G1 fit specification: bounded analytic check only

Read full g1-fit-spec.md initial7cb9d2fd version, full saved attempts/L1.md
and g1-methods.md, then final bounded guard/status clarifications. Accepted
final specification SHA256
`a922144e93fdc0394b712b569d0d93d2990c6b7916932063f2f104dea956c314`
for analytic correctness and preservation of the preregistered finite rule.
No fit, log computation, trend examination, code execution or finite gate
verdict was performed by this reviewer. All152 complete rows remain the
entry gate, with independent endpoint checking still required.

Independently reconstructed: the comparator minima yield valid ratio bounds
and their squared-input logs need the factor1/2. OLS with intercept gives
the stated training-to-holdout weights. Centered squared sums are60 on2–10
and165/2 on11–20, hence the early/late coefficients and their D1320 signed
integer product exponents are correct. Exact products distinguish strict
early positivity from the nonstrict late inequality, including equality.
The universal SSE condition is exactly2*SSE_P-SSE_E<=0, with no division
by a possibly zero error. Both models are fitted to log ordinates, with
training2–14 and holdout15–20; no raw-scale SSE substitution occurs.

The atanh-series tail encloses positive rational logs after dyadic scaling;
negative powers of2 require endpoint reversal as stated. The quadratic
residual matrix construction is correct. Expanding around a rational box
center proves bound(9): linear and off-diagonal terms use absolute bounds,
and omitting negative diagonal contributions conservatively upper-bounds
them. Rational tau vectors specify admissible witnesses despite enclosing
log errors. A complete finite certified cover proves the universal clause;
a strict admissible counterchoice disproves it. A bounded unresolved cover
or denominator guard gives only an unaccepted/INCONCLUSIVE outcome. No
vertex-only sufficiency, convexity assumption or transcendental equality
decision is imported. The finite operational KILL retains its original
scope and proves no asymptotic rate. High allocation suffices for this
standard linear/quadratic interval verification specification.

## L5 final verification-metadata impact

Read changed acceptance/checks/open-items/history metadata at final theorem
SHA256 `6beeb3f07eaa7fd0e401f94257c3afa9902d556324dc7cb18bc234ebe2cdfde6`.
It accurately reports the prior analytic acceptance and convention update;
no mathematical definition, proof or certificate inequality is newly changed.
No finite n3 certificate or G3 verdict is accepted through this metadata.
