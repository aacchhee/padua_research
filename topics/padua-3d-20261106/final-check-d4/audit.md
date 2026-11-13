# D4 supplemental adversarial check

2026-11-12. Checker: Codex, assigned **gpt-6-astra xhigh** by the root
orchestrator; internal runtime metadata is not exposed to this worker.
Rules read at `613735e8a5f0e66470ca3001a3900d55e1e35022`:
AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md. This is a distinct
worker's supplemental check of Codex development, **not the required
Claude audit**. No Git mutation, developer-file edit, handoff, registry
change, or subagent delegation was performed.

## Scope and conclusion

The assigned scope is verification of the inherited finite D4 mechanism:
the exact inverse residual, evaluation error, exhaustive mesh/continuum
transfer, normalized-Gram interpretation, and local double-Lee cutoff
with the restarted n4..7 determinant enumeration. No novel mechanism,
priority comparison, new candidate, universal Riesz assertion, or new
negative mathematical claim is proposed. The workflow's no-novelty
exception therefore applies: this checker did not repeat the full IDEAS
read or the developer's literature novelty gate. It read the D4 gate,
handoffs18/19, protocol, reduction, double-Lee proof, finite minima, Gram
record, inherited R08 reduction, both C++ enumerators, and D5's explicit
source-coverage record.

**Completed: no unresolved finding within this declared scope.** All13
QR certificates, both optimized n12/m2 and m3 certificates, both Lee
enumerators, and the independent arithmetic cross-checks passed. The
initial underflow justification issue was returned to the developer and
resolved in corrected prose plus exact checks; the numerical code and
result-bearing inputs remained unchanged.

The two QR and historical-optimized scopes remain distinct. These checks
do not recover unavailable historical optimized coordinates at n4..11 or
n13..16, certify a global optimum, or turn finite Gram measurements into
an asymptotic conclusion.

## Audited implementation and reduction

Producer `code/fd4_certify.py` SHA256:
`7e1ff950b5d26338fb0cd9bbbdd7d4bb605001cd4f274c628b5dd28926fa8750`.
This hash is asserted by the supplemental checker before importing it.
Producer `code/fd4_lee.py` SHA256:
`acc2328ddafeec1cc90c76e0f97ffb7257f1f5dfa74282076f8a34eaa0f2b69e`.
The inspected corrected certificate-reduction.md SHA256 is
`595c18b7a168dd640668ca0ad4f5e4ca0d3ee0a1184ccb8c00f7d7190461fb1f`;
the double-Lee proof SHA256 is
`4f9ae14eca74f4999a88fc497865bd3c31863a2487c66991467f14399678490c`.
The root published the numerical protocol at9cf64ef before R1 GO and
published R2 at0971807 before the producer's m3 run. This checker began
execution only after the root explicitly authorized inherited verification.

The matrix orientation is correct. With rows of V indexed by nodes and
columns by basis polynomials, R=I−VW gives
V^−1=W(I−R)^−1 and pW=(pV^−1)(I−R). A row's l1 norm is controlled by
the multiplying matrix's maximum absolute row sum, so both uses of the
infinity norm, including N beta ||W||infinity, have the right orientation.
The lower denominator1+rho and upper denominator1−rho follow from these
identities; no floating inverse accuracy is trusted.

The int64 bound inner_dimension*maxabs(A)*maxabs(B)<2^63 controls each
integer product and every possible partial sum, regardless of summation
order. The separate bound S^2+maxabs(AW)<2^63 protects the diagonal
subtraction. Absolute row sums have their own guard. These preconditions
also exclude INT64_MIN before abs is used on products/residuals; integer
quantization is confined to magnitude below2^62. No overflow escape was
found. Actual unsafe product, row-sum, nonfinite-quantization, and oversized
quantization examples were rejected by the guards.

The installed NumPy2.3.5 `chebvander` source was inspected. It computes
v[k+1]=(2*x)*v[k]−v[k−1] with distinct NumPy multiplication/subtraction
operations, and the tensor basis applies two products in the stated
order. The recurrence and quantization error formulas therefore match
the actual implementation. See the underflow finding/disposition below.

The mesh coordinate conversion is conservative. Each coordinate is an
exact binary64 dyadic inside the cube, its rigorous error is at most
2^−52, and the product-Chebyshev gradient satisfies
sum_j |partial_j T_alpha| <= sum_j alpha_j^2 <= n^2. This yields the
stated beta_mesh. Exhaustive grid cardinalities are (mn+1)^3; certificate
cap failures are not promoted to continuum results.

The continuum factor is the dimension-independent sec(pi/(2m)) for
**total-degree** polynomials. The cardinal polynomials meet the operator
form in Bialas-Ciez–Kenne–Sommariva–Vianello, arXiv2311.18656v1,
Lemma1/Proposition1 pp3–4, as checked against the primary statement by D5.
The Lebesgue function itself need not be a polynomial. This supplemental
checker inspected D5's source record and the exact application; it did
not independently acquire the primary PDF or re-prove that source theorem.
The LITERATURE dependency must remain explicit. The source's factor is
not replaced by a tensor-degree estimate or a cubed factor.

The normalized Gram formula and orthonormal product-arcsine scaling are
consistent. Floating eigenvalues and the resulting Gram expression stay
MEASURED; they are not used in the certificate proof.

## Actual independent executions

All commands ran from `/workspace/padua_research`. The certificate
replays read the committed/retained base85 coordinate payloads directly;
they do not regenerate QR selections or overwrite producer payloads.
Every non-timing certificate field is compared exactly, including all
rational endpoints, residuals, maximal integer mesh norm, argmax and
number of mesh points. Environment: Python3.12.14, NumPy2.3.5,
SciPy1.17.0, mpmath1.3.0; binary64/int64; no random seed.

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fdq_certify.py --family qr --degrees 4 5 6 7 8 9 10 11 12 13 14 15 16 --m 2 --arithmetic 4 --output topics/padua-3d-20261106/evidence/fdq-qr-replay.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fdq_certify.py --family payload12 --degrees 12 --m 2 --output topics/padua-3d-20261106/evidence/fdq-payload-m2-replay.json
python topics/padua-3d-20261106/code/fd4_lee.py --scratch /tmp/padua-fdq-lee-independent --output topics/padua-3d-20261106/evidence/fdq-lee-replay.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fdq_guards.py --output topics/padua-3d-20261106/evidence/fdq-range-guards.json
python topics/padua-3d-20261106/code/fdq_underflow.py --output topics/padua-3d-20261106/evidence/fdq-underflow-slack.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fdq_certify.py --family payload12 --degrees 12 --m 3 --arithmetic 12 --output topics/padua-3d-20261106/evidence/fdq-payload-m3-replay.json
```

The QR replay evaluated all13 meshes in114.215 aggregate certificate
seconds; maximum51.925s at n16, below each120s cap. The n4 interval is
[11.24480235910147,15.90276407732308], and n16 is
[165.46451423421266,234.3402851847974]. These are display approximations;
the exact Fraction endpoints in the receipts define the enclosures.
Optimized n12/m2 separately replayed in4.151s and matched
[25.961333443235883,36.726473312530295].

The n4 extra check evaluates all1225 node/basis entries using independently
written Python Fraction Chebyshev recurrence, checks every one against
beta, verifies all1225 residual matrix-product entries with Python
unbounded integers, checks the maximal mesh row's35 integer dot products,
and reassembles the endpoint fractions independently. The largest exact
node-evaluation discrepancy is approximately2.8307490451e−8, below beta
32769/1099511627776. These are checks of exact inequalities, not numerical
agreement promoted to proof.

The scalar mesh check is independent of mpmath: it encloses pi using
Machin's identity16atan(1/5)−4atan(1/239) and80-term rational alternating
series bounds, then uses a71-term rational cosine Taylor sum with its
alternating-tail bound and the Lipschitz error from the pi enclosure.
The terms decrease by the truncation point for |argument|<=pi. Exact
rational comparisons prove both the coordinate-error allowance and the
upper secant bound. At n4/m2 all9 scalar coordinates pass; the largest
enclosing discrepancy is about4.834e−17, below2^−52.

The final optimized n12/m3 replay completed all50653 mesh points in
12.971s and matched every non-timing producer field. Its extra independent
arithmetic checks took94.211s, separate from the certificate's120s cap:
all207025 node/basis entries passed exact Fraction evaluation bounds;
3185 entries across residual rows0,1,113,227,341,453,454 matched Python
unbounded-integer dots; all455 dots at the recorded maximal mesh row
matched; and the independently assembled Fraction endpoints agreed.
The largest exact node-evaluation discrepancy is about2.9802267224e−8,
below beta32797/1099511627776. All37 scalar mesh coordinates and the m3
secant upper bound passed the rational Machin/Taylor check, with enclosing
coordinate discrepancy at most approximately5.018e−17. Thus the check is
more than a repeated invocation of the producer's arithmetic.

The m3-only display enclosure is[25.161254416506974,29.062899565240023].
Exact comparison of the m2 and m3 Fraction endpoints gives the intersection

```
122618079842671965904073/4723104077484109144832
  <= Lambda <=
12573302689962301733389339775564029/432623822056636631704459416698880.
```

The simple outward decimal form is **[25.961333,29.062900]**. A separate
exact Fraction comparison checked that both decimals point outward and
that all13 QR lower/upper decimals in lebesgue-intervals.md also point
outward; the table's N and evaluated-mesh counts matched the receipts.
The m2 and m3 meshes are not nested. Their independently valid bounds
are intersected; no monotonicity assertion is needed.

The range checker covers every retained node and every scalar/vector
operation on all15 actual meshes (QR n4..16/m2 and optimized n12/m2,m3).
It uses the input exponents of each actual multiplication to rule out
underflow before rounding, and dyadic operand spacing to rule out
nonzero subnormal cancellation results. The smallest observed nonzero
mesh intermediate is about8.854e−186, safely normal. All four invalid
arithmetic guard probes are rejected.

## Double-Lee reduction and exact enumeration

The local double-ball proof is valid including n=1. Its diameter is
2n−1, which is strictly below the admissible lattice minimum2n; distinct
points therefore occupy distinct classes of Z^3/L. Counting transverse
shells gives exactly(2/3)n(2n^2+1). The index is that of the integer
annihilator lattice, so no primal scaling or factor of2 is missing.

Independent execution recompiled and ran both frozen enumerators on the
entire windows88..92,170..178,292..304,462..486. All per-determinant
unpruned HNF/admissible counts, complete minimizer sets and fold
histograms agree with the producer receipt. Minima and HNF counts are
(92,24),(178,24),(304,8),(486,24). The two admissibility implementations
are genuinely different: one derives coordinate ranges and distances;
the other tests the explicit half-l1 ball using divisibility/residue
tables. The R08 HNF reduction and both loops cover all diagonal divisor
triples and allowed off-diagonal entries. No18/19 imported cutoff or
optimal-lattice catalogue is used. Fold counts at these determinant
minimizers are not claimed to be global folded/rank minima.

The Lee wrapper's inherited status string says that its developer ran
both implementations. This separate execution was performed by the
supplemental checker, as recorded here; it still does not replace the
formal Claude audit. Its raw JSONL/binaries are regenerate-only scratch,
and all essential exact counts/HNFs are retained in the small receipt.

## Finding, response, and preserved unsuccessful check

**F1 — MAJOR arithmetic-justification gap at inspection, RESOLVED.** The
initial explanation that all admitted dyadic inputs produce only normal
floating values was too broad: arbitrary exact binary64 inputs can be
subnormal, and zero is also allowed. This was returned to the developer,
not silently edited by this checker. No frozen numerical code changed.
The corrected reduction explicitly uses eta=2^−1074 and
|fl(z)−z|<=u|z|+eta/2. Its local recurrence allowance dominates
(5u+2u^2)(1+E)+(1+u/2)eta. The two-product underflow term is at most
eta*((1+e)(1+u)+1)/2<=2eta. The corrected text also observes the slack
3e^2+2e^3 in the product input-error bound. Independently, exact Fraction
checks verify raw_error+2eta<=the unchanged rounded-up beta(n) for every
n4..16. Thus no missing underflow term remains in these finite cases;
the corrected written inequality also explains the general dyadic case.

**Checker development failure, not a producer failure.** The first
fdq_guards run exited1 at the assertion2*log2(minimum_intermediate)>−1022
on the n4 mesh. That intentionally conservative global-minimum-square
test wrongly combined unrelated operations: a tiny final triple product
is never multiplied by another copy of itself. The checker was corrected
to inspect each actual pair of operands and subtraction spacing, then
rerun successfully. The actual failed command is the fdq_guards command
above; no partial successful receipt or producer failure was asserted.

## Trust and limitations

Trusted components remain Python integer/Fraction arithmetic, IEEE
binary64 behavior, NumPy's inspected elementary operations and guarded
int64 products, JSON/base85/SHA256 input identity, and mpmath directed
scalar intervals for meshes not separately enclosed by the rational
cross-check. The supplemental check does not trust SciPy QR, floating
inversion or eigensolvers as proofs: they propose coordinates/inverses
or produce explicitly measured diagnostics. Exact finite certificate
checks and the cited total-degree mesh theorem are both necessary.

All supplemental evidence files are individually below32KiB; the root
owns their final manifest/commit and the repository-wide storage check.
No large archive or external delivery is claimed. No assigned supplemental
rerun remains; formal Claude audit and root integration remain separate
steps. The developer's initially pending-m3 status text may now be updated
by its owner to cite this actual completion; this checker did not edit it.

## Essential supplemental evidence identities

Every receipt also identifies its actual input files and generating code.
These are independent small receipts, not pieces of a split bulk artifact.

| Artifact in evidence/ | Bytes | SHA256 |
|---|---:|---|
|fdq-qr-replay.json|19222|470ce996fa6aa2bdf85175a77b0094d28fdc5ba1fc8149f08e02574276e34a2d|
|fdq-payload-m2-replay.json|2096|e1d05f958f3b07a6df6baaca2cf5a34b8112f557175b04defb0f419227afc972|
|fdq-payload-m3-replay.json|2808|67c46f0d5dbd91e2244f33c5688d6313b0e915574ce6833aa2dec8ee754988e9|
|fdq-lee-replay.json|11418|9529e1c5bfbae33d3a853bb91e4ce37ee16c4a63cbd792321b2bb78cb8d05ff0|
|fdq-range-guards.json|9908|b36f6f278270797d972696b871d696bb5d88f3ae1dcc18d2d48d323304dd1b18|
|fdq-underflow-slack.json|3837|096bb811b760e800551497ef5f865069d03393460cd35a4eead25085c92f2537|

Supplemental source identities: fdq_certify.py
`564c163920cbe1332ff4bb63ce5761c965cc275591fc94294559719b75a5a655`;
fdq_guards.py
`0a8279084e47278f7d1649b4d0c3112dc5ed05c398fc3dc43a708e4774b03462`;
fdq_underflow.py
`edc7614e44359d2932d7b78c2edfc9c6aed4bb5b03b0a3a9442d7e71deaff708`.
