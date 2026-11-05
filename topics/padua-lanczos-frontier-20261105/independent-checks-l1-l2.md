# Supplementary L2 mathematical review — handoff03

Rules/read head: `0e493be7f9883e00e6260cf6b081c607a230177f`; continuation
head: `79c3d6a211325eca6e8311b3ae03187c100a1d8a`.
Reviewer: supplementary gpt-6-astra, configured high effort. No Git mutations.
Initial ownership was this report only; root later authorized
`code/g2_independent.py` and `evidence/g2-independent*.json`. Mathematical
reconstruction and actual exact-arithmetic executions are distinguished below.

## Scope and current disposition

**FINITE REDUCTION, BOTH GRID W/R G2 PREDICATES, THE WEIGHTED BRIDGE,
AND THE SAVED FORMAL ALL-DEGREE W/R THEOREMS PASS REVIEW.**
G1 remains outside this acceptance. All-degree review occurred only after
actual G2 acceptance and separate authorization. The parent assigned
the new SH_n structural theorem to a separate gpt-6-astra xhigh adversarial
reviewer. This report does not approve that theorem. Its initial scope was the
finite W/R rule-class reduction, the genuine X-closure observable, normalized
versus monic source factors, and the interpretation of subsequent finite
certificates. The later authorized all-degree L2 review is recorded separately
below. The stable finite developer text and actual independent G2 computations
have now been checked as recorded below. The original
PD-T055 remains OPEN.

The inherited prospective-gate timing deviation remains disclosed. Subsequent
reading is not a repair of that timing; Claude's later explicit protocol
disposition remains separate. High effort is adequate for the finite induction
and projector calculation reviewed here; no unresolved new structural mechanism
has yet justified a separate xhigh allocation for this part.

## Reading ledger and boundaries

The previous full `state/IDEAS.md` baseline through line889 and the full relevant
L1/L2, L3/L4 saved-candidate gate are inherited reading. For this continuation,
the entire merged registry delta from684849d to0e493be was read in bounded
pieces, including the changed dispositions and new PR19/20/23 entries. A large
initial diff view was truncated and was not credited; the later bounded views
covered the delta. The current 0e493be-to79c3d6a committed delta changes only
LOG, plan and manifest, not the registry, rules or frozen Lanczos sources.

Full current task reads: handoff03, LOG, attempts/L1 and attempts/L2,
ideas-l1-l2 including its continuation, and ideas-l2-continuation. Complete
pertinent predecessor entries read: canonical IDEA130–144 in the old L1
candidate file with their audit/correction tables; the old L2 candidate file,
including IDEA148/151 and dispositions; PD-T033/035/036/038/039/041/044,
PD-T053/055/136/137, PD-N009/013/015/062. The complete IDEA246–267 candidate
sources were read in the previous gate and remain unchanged. The relevant
literature INDEX rows089/090/096/098/099/114,237–257,278–285 were read; this is
repository record reading, not primary-paper or external-priority clearance.

A bounded mechanism-term search of the merged additions found no replacement
for the saved W/R quotient/closure obligation. This is a statement about that
searched repository scope, not an absence-of-prior-art claim. PD-T136 does not
claim arbitrary-rule invariance; PD-N062 fixes a prefix and one degree;
PD-T053 runs from closure to drift, not conversely. None of those missing
implications is adopted as a premise.

## Prospective acceptance checks supplied before developer proof review

1. Keep the exact-base differentiable class R_smooth, fixed BJ parents/products,
   unchanged stored parents, and the declared raw-product source. Both
   coefficient derivatives and normalization derivatives must enter the proof.
2. Show their difference from a frozen response stays in the appropriate
   complete polynomial evaluation space at every step, including multiplication
   of earlier parent differences. A one-degree fixed-prefix argument is
   insufficient.
3. Differentiate both projectors in `(I-P_hat_(s+1)) X P_hat_s`. Distinguish the
   actual operator derivative from a span-angle surrogate and from any raw
   coefficient residual.
4. Justify the infimum over every permitted rule pointwise; do not assume a
   uniform nonbreakdown neighborhood or interchange an infimum with a limit.
5. Include all source columns and the exact normalized-to-monic source weights.
   The sign-law trace must include the source/node count, all Gram factors,
   every specified prefix, and normalization by `||X||_2^2`.
6. A certified W lower needs a normalized source and an actual closure output
   readout. A certified W negative needs an upper covering all sources. For R,
   evaluate the exact expectation under the preregistered independent sign law.
   Frobenius expectation does not establish a spectral probability statement.
7. Preserve T24/rotQ24 degree12 predicates `C_12>=256` and `E_12>=16` separately.
   No all-degree L2 proof may start until the corresponding G2 predicate has a
   certified decision and actual independent execution. G1 finite fits and
   endpoint comparisons do not supply that decision.

## Independent reconstruction before stable developer text

The following is a finite-dimensional reconstruction, not approval of an
unread draft. Let exact orthonormal columns be q_k, complete-prefix matrices
Q_s, and their exact spaces S_s. At zero, expansion coefficients and positive
normalizations are uniquely fixed by the exact raw product and the prescribed
q_k. Differentiating a permitted rule gives

`beta_k u_k = A_k u_parent - sum_(l<k)c_kl u_l + f_k
             - sum_(l<k)cdot_kl q_l - betadot_k q_k`.

Subtract the frozen normalized response with the same f. The last two terms
belong to S_deg(k); each prior difference does also, and multiplication of the
parent difference raises its degree by at most one. An induction on the
actual column order therefore puts the difference in S_deg(k). This step
must explicitly cover same-degree earlier columns. It uses fixed products,
fixed parents, and exact-base differentiability, not working-precision storage.

Write W_s for the frozen response columns and
`Z_s=(I-P_s)W_s`. Then every rule has the same normal derivative Z_s, and

`Pdot_s = Z_s Q_s^T + Q_s Z_s^T`.

With `H_s=Q_(s+1)^T X Q_s`, differentiating the actual closure operator at its
zero exact value yields

`Fdot_s = [ (I-P_(s+1)) X Z_s - Z_(s+1) H_s ] Q_s^T`.

The second projector term is essential. The bracket has the same spectral
norm as Fdot_s. Equivalently it is

`(I-P_(s+1)) [ X W_s - W_(s+1) H_s ]`.

A differentiable orthonormal frame for the perturbed prefix gives the same
bracket: its additional tangential frame derivative is killed by exact
closure. A nonorthonormal stored-column derivative must not be inserted as
an orthonormal frame without this argument.

For each fixed rule and fixed source direction, differentiability and finite
prefix count give the requisite first-order limit. Since that derivative is
rule-independent pointwise, every rule has the same source supremum and the
same sign-law expectation. Thus an infimum can be removed after this proof;
no uniform neighborhood across rules and no infimum/limit exchange is needed.
The rule class must be nonempty; exact all-prior orthogonalization supplies a
local differentiable member when exact pivots are positive.

For exact orthogonal monic columns b_k with squared norms d_k, the derivative
conversion is `w_k=sqrt(d_k)u_k`, and normalized raw source f_k becomes
`F_k=sqrt(d_parent)f_k`. Its monic source scale squared is
`||A_k b_parent||^2=d_parent*sigma_k^2`, so the original relative source metric
is preserved exactly. Monic closure entries use
`Hmon_lk=(b_l^T X b_k)/d_l` and divide output column k by `sqrt(d_k)`.
For independent signs, monic source covariance is diagonal with entries
`||A_k b_parent||^2/((N_n-1)M)`; the expectation additionally divides by
`||X||_2^2`. This is a rational trace once the exact projector/Gram factors
are retained. There is no need to replace the independent sign law with a
Monte Carlo estimate or to claim its realizations are IEEE rounding paths.

## Stable finite theorem review

Read the complete362-line
[finite reduction](theory/l2-smooth-rule-closure-reduction.md), SHA256
`44498c6230d0a59bbd0cfc4bc96600f0b401eb92ba9302b5c1d54cc569c8d5f9`,
after the preceding independent reconstruction. No mathematical defect found.
The statement matches the saved smooth exact-base class and W/R quantities.
The following checks go beyond matching displayed formulas:

- Equation(9)'s coefficients follow uniquely from orthonormal expansion;
  multiplying the normalized derivative by sqrt(d_parent) gives precisely
  the monic h_k in(10), including the normalization derivative. Same-degree
  earlier columns remain within the induction space. Nonemptiness and
  pointwise finite-prefix nonbreakdown are supplied.
- Equations(12)–(14) retain both moving projector effects. Orthogonalizing a
  stored frame changes its derivative by a tangential term, and its product
  with the zero exact closure matrix vanishes. The spectral norm in W is
  therefore the actual operator-defect derivative, not a span surrogate.
- In(15), an individual source/node impulse produces a rank-one output, so
  its spectral square equals ell exactly. The total Hilbert–Schmidt square
  is H_s^2. The unprojected response is a direct sum over node rows; each
  row-map spectral norm is at most its displayed Frobenius norm, and final
  projection contracts. This justifies U_s^2 without neglecting sources.
- In(16), substituting the unit output direction
  D_s^(1/2)t/sqrt(t^T D_s t) cancels all output square roots. Maximizing the
  resulting scalar functional over the joint unit source vector gives its
  squared coefficient norm, exactly J_s. Quantifying the remaining node
  readout yields the PSD statement(17). This is a characterization, not an
  implemented efficient decision procedure.
- The prescribed signs have covariance I/((N_n-1)M), even though every
  realization has unit joint norm. Linearity of the common derivative makes
  all cross terms vanish in expectation; the sum of H_s^2 divided by
  (N_n-1)M||X||^2 is exactly the saved R observable. This does not give a
  probability bound or a per-realization lower.
- The frozen implementation specification correctly includes stages0–11,
  all90 sources (later zero columns included by coverage), and next-degree
  sources in the negative projector term. It retains C_12>=256 and E_12>=16;
  squared W comparisons use65536. Exact equality passes; overlapping W
  endpoints are INCONCLUSIVE, not a negative decision.

**Disposition:** supplementary mathematical check passes for this analytic
finite reduction and its stated exact endpoint/trace specification. It is
sufficient to proceed to the separately authorized G2 producer and distinct
independent computation. It does not certify any degree12 predicate.
No theorem or source edit was made by this reviewer to obtain this result.

## Pre-execution computational boundary (historical checkpoint)

At the analytic-only checkpoint the following remained pending. Review producer/checker coverage, exact identities and actual independent
execution when available. No code, certificate or G2 run was produced by
this reviewer during this mathematical reconstruction. The G1 endpoint and
fit interpretation remains limited to the frozen finite predicate; no G1
operational decision is made here. No SH theorem approval, all-degree L2
bound, original PD-T055 resolution or Claude audit is implied.


## Actual independent G2 execution — 2026-11-05

After the analytic acceptance and root's G2 START, implemented
[code/g2_independent.py](code/g2_independent.py) without importing the producer.
The sole shared mathematical implementation is the frozen exact BJ baseline
builder `tracks/bivariate-lanczos/code/drift/e1_exact.py`, pinned to
`19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`.
It was read in full. Each independent run regenerated the exact baseline;
this is not a relabeled read of developer evidence.

The checker forms the full exact Gram matrix and full X multiplication
expansion, including degree12. It reconstructs the selected-source recurrence
and the signed closure-response matrix independently by matrix multiplication.
At the winning source/node it also directly applies both differentiated
projectors to every monic prefix column using their exact low-rank factors.
The full squared Frobenius gain equals the rank-one spectral gain ell; both
projector contributions are nonzero on each accepted witness. The source
conversion and total relative budget1 are checked with all90 source positions
in the domain, only one of them nonzero. No span certificate substitutes for
this closure calculation.

Small-degree controls use a distinct3x3 rational grid. The checker
differentiates `B^T(BB^T)^(-1)B` without initially simplifying any term and
checks stages0,1 against the reduced formula. A separate monic derivative run
adds both coefficient and normalization derivative terms `-b_k-b_0`; its
completed-prefix projector and closure derivatives agree exactly. Three
malformed derivatives are rejected: omit the next-projector term, omit the
current-projector term, and reverse the next-projector sign.

The prospective partial-R certificate was read in attempts/L2.md before its
numerical calculation. Its implication was independently accepted: every
omitted trace contribution is nonnegative, so the stage11/source6 all-node
sum divided by the original `90*M*||X||^2` is a lower for the unchanged full
sign law. No full expectation or one-source random law is asserted. The
independent small-grid checker additionally differentiates full projectors
for all45 source/node directions and both stages; its weighted exact trace
equals the independently formed omega trace, giving the control expectation
`43/135` with global denominator45.

All degree12 results below are exact integer lower bounds (the floors of the
actual rational certificates):

| Grid | Fixed W source/stage/node | Lower for C_12^2 | Lower for full-law E_12 | R total denominator |
|---|---|---:|---:|---:|
| T24 | h6 / s11 / node22=(-1,5/6) | 17525752205103 | 6457695691 | 29250 |
| rotQ24 | h6 / s11 / node1=(2/15,-27/20) | 6324995264 | 2606606 | 110250 |

Thus both unchanged W predicates `C_12>=256` and both unchanged R predicates
`E_12>=16` pass. Source6 already suffices, so sources4,3,5 were not screened.
No upper bound or full E_12 value was computed. The independent exact W gains,
all325/all625 node ell values, and both exact partial-R rationals were compared
with the separately generated developer artifacts and agree exactly.

The original W-only independent runs used source2aefb490... (T24 3.85s,
rotQ24 100.58s). Adding the prospectively specified R certificate and its
small-grid trace control justified the next independent runs under668baf6b...
(T24 2.99s, rotQ24 94.95s). The final optional fixed-certificate packaging
adds checks of the declared source/stage/node, global denominator, and integer
floors; it changes no recurrence, closure formula or search. Final runs with
that packaging actually regenerated both grids again. They had already been
dispatched when root advised reusing the earlier verified arrays for packaging;
no further assembly was performed after these runs.

The committed compact certificate is
[evidence/g2-fixed-certificate.json](evidence/g2-fixed-certificate.json), SHA256
`6bec42971911fb3f86081a13042b6c7029290702c2536c128c0a6f1bf0b746cf`.
Five malformed certificate cases are rejected on each grid: reduced global
source count, denominator for a one-source law, changed W node, inflated W
integer floor, and inflated R integer floor. Original producer receipt or raw
artifact paths are never opened by the independent checker; historical
metadata is not a mathematical acceptance dependency. The final command uses
only this repository, its pinned baseline source and installed python-flint:

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps python -B \
  topics/padua-lanczos-frontier-20261105/code/g2_independent.py \
  --set triangle --partial-r \
  --fixed-certificate topics/padua-lanczos-frontier-20261105/evidence/g2-fixed-certificate.json \
  --output /tmp/g2-independent-triangle.json \
  --exact-output /tmp/g2-independent-triangle-exact.json
```

Repeat with `--set rotated` and distinct output names. The PYTHONPATH is this
session's dependency installation location; a normal installation of
python-flint0.9.0 can replace it. No old temporary evidence is an input.
The exact regenerated arrays/certificate details are temporary working
artifacts with hashes in the small receipts; delivery/retention remains
root-owned.

The finite analytic proof plus these actual independent computations support
finite computer-assisted acceptance of both saved W/R G2 predicates on each
specified grid. They do not resolve original working-precision PD-T055,
actual IEEE behavior, a high-probability conclusion or an all-degree target.
Only after root accepted G2 was a weighted extension/all-degree L2 review
requested; that is a separate pending mathematical review, not a consequence
silently imported from the uniform-grid finite theorem. The earlier protocol
timing issue and later Claude audit remain unchanged.

Final immutable execution identities:

- `code/g2_independent.py`: SHA256 `e88536c7156256de09f907923d7a51437055b685f3ccbaee62fcff4b50589ca8`.
- `evidence/g2-independent-triangle.json`: SHA256 `6c42af6af8b2e1bba5da5f92918a2d63f8be25b26e9fd2d9ff7fd43f0ce6215c`.
  Actual final regeneration elapsed 1.76s; fixed-certificate controls passed.
- `evidence/g2-independent-rotated.json`: SHA256 `ba85d9e9b79c4d61dd96b4141a4675e952f83e57b96077c57f08a7708f5e7d12`.
  Actual final regeneration elapsed 99.90s; fixed-certificate controls passed.

## Bounded post-G2 mathematical review: finite record and positive weights

After root accepted the actual G2 executions, read the complete finite
certificate record and the positive-weight bridge. This review used the same
configured gpt-6-astra high allocation; there was no silent model substitution
and no scientific rerun. The already accepted G2 code and receipts are unchanged.

- `theory/l2-g2-degree12-certificates.md`, final reviewed SHA256
  `d002cffdb9f874796983dbc5b9696c221dbf08a563b1810b88f9ee9f94648ecd`:
  mathematical statement agrees with the actual independently checked integer
  lower certificates, full source law and finite analytic reduction. Both W/R
  finite conclusions pass review. One minor provenance finding was sent to the
  developer and root: the removal control deletes top-level nonessential keys,
  while ignored nested historical receipt objects remain. The initial wording
  suggested broader deletion. The developer corrected that wording, and the
  correction was read. No source, arithmetic or acceptance criterion changed;
  the checker never reads those historical objects or their paths.
- `theory/l2-positive-weight-embedding.md`, reviewed SHA256
  `c84368610d33030f6f50480488fc9135c34c275e3bdab91dfbfb4b8e81e2949e`:
  analytic mathematical check passes. Positive diagonal embedding is invertible
  and commutes with coordinate multiplication, so the entire polynomial-error
  induction survives. Parent norm factors in the monic source conversion are
  unchanged. The Euclidean projector derivative still has both terms, and the
  same pointwise argument removes the rule infimum. Arbitrary positive weights
  need not sum to one; the stated initial normalized vector handles this.

The weighted random law remains isotropic in represented-node coordinates;
it acquires neither an extra sqrt(weight) factor nor diagonal weight covariance.
Cross-source contributions are discarded only after taking expectation.
Rational weights/nodes yield rational monic coefficients, norms, scalar response
functions and normal projector diagonals, hence rational ell/trace endpoints.
Off-diagonal Euclidean projector entries can contain square roots; the bridge
correctly refrains from declaring them rational. Its optional substitution
r=Wz gives rational weighted quadratic forms without losing test directions,
since W is invertible. No substantive mathematical finding remains.

For the later all-degree review, additionally read the full checked SH theorem
(hash9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d)
and the separate xhigh SH audit report as dependency/context, and completed
full PD-T042/043 reading to maintain the distinction between coefficient/Gram
noise measurements and the present closure/source-law theorem. Those older
experiments were not rerun. The new post-G2 prospective W/R entries in attempts
and ideas-l2-continuation were read. The SH theorem retains its separate
reviewer's acceptance; this report does not duplicate that approval. Actual
all-degree L2 statements still await complete stable developer text and their
own independent check. No unresolved difficulty in this finite bridge required
an additional xhigh allocation.


## Independent all-degree L2 mathematical reconstruction after G2

Read the complete separate stable proofs:

- `theory/l2-sh-worst-case-closure-growth.md`, SHA256
  `30cc4c6bab3c7dfd9dc617379f63e1a62f76bf4c0a098dbb0f5940beee9a3b74`;
- `theory/l2-sh-random-closure-growth.md`, SHA256
  `6a96b9e001e1e359aca4be418bb799f4bd284c3e39c1688014fe69c129b0e045`.

**Mathematical disposition: both pass in exactly their stated formal model.**
No new numerical/symbolic run was performed for these analytic results. The
same high allocation sufficed for this bounded reconstruction: the new closure
block is an explicit consequence of the already reviewed creator identities
and two-projector formula, with no unresolved structural step warranting
another xhigh allocation. The separate SH family/selection theorem retains
its own xhigh audit.

The reconstruction is as follows. For the sole normalized raw source f at
h=(n,0), every earlier frozen response is zero. The final-degree BJ chain has
columns `2*(-2)^j f`, j=0,...,n. Quotient invariance therefore gives
`Z_(n-1)=0` and the corresponding normal final-degree columns of Z_n. This
statement does not force earlier tangential stored-column derivatives to
vanish for every permissible rule.

In the actual closure derivative
`R_n X Z_(n-1)-Z_n H_X,n-1`, the first term vanishes for this source. For
input column `(n-1-j,j)`, physical X=S raises the first tensor index with
coefficient1/2; its other term has lower degree and hence zero Z_n response.
Thus the output column is `-(-2)^j R_n f` for j=0,...,n-1. Inputs of lower
degree have zero output. The last degree-n response `(0,n)` is not in the
raising image of an admissible X parent, which is why the geometric sum
ends at n-1, not n. This directly proves the closure block without reversing
any span-to-closure estimate or dropping a nonzero projector term.

For W, `e=q_(n+1,0)` is a represented unit normal vector, since m=n+2
includes this highest permitted U mode and weighted evaluation is injective
through n+1. The source `f=e/sqrt(2)` has exactly unit relative budget:
its BJ raw-product scale squared is1/2 for every n>=2. Its rank-one closure
matrix has squared spectral gain `(4^n-1)/6`. Dividing by
`||X||=cos(pi/(n+3))` gives the stated lower for C_n. The source works
pointwise for every saved smooth exact-base rule by the weighted quotient
proof, so the every-rule infimum is respected. The comparison to2^(n-4)
reduces to `250*4^n>=256`, valid throughout the stated range.

For R, use the same source-block linear map but retain its original random
block from the full law. It has covariance `I/(2 H M)`, where
`H=N_n-1`, rather than covariance for a newly normalized one-source law.
Independent centered blocks remove cross terms only after expectation;
other blocks may cancel in a particular realization. The selected block
therefore contributes
`(4^n-1)(M-N_n)/(6 H M ||X||^2)` to the nonnegative expected trace. This
uses `trace(R_n)=M-N_n` in the Euclidean represented space. It does not
rotate the Rademacher law or assume rotation invariance of its distribution;
isotropic second moments are sufficient.

For this exact family,
`(M-N_n)/(H M)=1/[n(n+2)]`, giving the stated expectation lower. The induction
`2^n>=n(n+2)/2` starts with equality at n=2 and advances because n^2-3>=0.
Together with `4^n-1>=(3/4)4^n`, it yields the stronger intermediate
`E_n>=2^n/16`, hence the unchanged target2^(n-8). The sum over stages in R
and the maximum in W are never interchanged. No exact full expectation,
per-realization lower or probability statement follows from this proof.

A minor provenance wording suggestion was sent to the developer and root:
W's phrase “metadata-only acceptance” for the SH report can be read as
understating that report's full analytic and executed supplementary review.
It does not affect the proof or mathematical disposition; any clarification
is recorded below with its final hash. No substantive mathematical finding
remains. Original literal working-precision PD-T055, deterministic F, IEEE
activation and finite-epsilon uniformity remain outside these acceptances.
The later Claude scientific/protocol audit, including the earlier timing
deviation, remains required.


Final metadata impact review: the developer clarified the SH acceptance wording
and recorded the accepted supplementary checks in the weighted/W/R theorem
metadata. The complete final three files were read again; statements, source
laws and proofs are unchanged. The minor provenance wording suggestion is
closed. Accepted final immutable file hashes are:

| Record | Final SHA256 |
|---|---|
| Finite G2, `l2-g2-degree12-certificates.md` | `d002cffdb9f874796983dbc5b9696c221dbf08a563b1810b88f9ee9f94648ecd` |
| Weighted bridge, `l2-positive-weight-embedding.md` | `62ad28fa8b0fb8ca392cffa6f093ba9ba89d52bd10cfae090142e2d7fcec1c6c` |
| W, `l2-sh-worst-case-closure-growth.md` | `84dd00ec23e52dd9d73a86379dbfd30daef0bdc0cdba9834618b4db6f69fd8c5` |
| R, `l2-sh-random-closure-growth.md` | `f9320ca0ebed3134e8183e95c352d56086ba0edb9ae459b761b0b6ca37f94138` |

No further scientific execution was performed during this bounded review.
The finite uniform reduction remains at44498c... and the accepted G2 checker,
receipts and fixed certificate retain their already recorded final hashes.
All mathematical findings are closed within the stated formal scope; required
Claude review and original working-precision PD-T055 remain separate.
