# PD-T?argmax-alln-codex-03 — Global-maximum Bernstein certificate correctness

ID kind: PD-T.
Aliases: finite global-max-only certificate; positive-coefficient corner leaf; IDEA?argmax-alln-claude-05.
Split from: none; supporting finite-certificate implication for PD-T099/P6.
Split into: none. Successful degree-specific certificate claims require separate records.

## Statement

Let L₁,…,Lₘ be specified real bivariate polynomials, each of degree at most
d in each coordinate, and λ=Σ|Lᵢ| on Q=[−1,1]². Let E be a nonempty set
of corners of Q such that λ(e)=C for every e∈E. Suppose Q is covered by a
finite binary midpoint subdivision whose closed leaf boxes have the
following verified dispositions. On a leaf R write each Lₗ in the tensor
degree-(d,d) Bernstein basis, with coefficients cₗ,ᵢⱼ(R).

1. **Bound leaf:** every coefficient absolute sum Σₗ|cₗ,ᵢⱼ(R)| is strictly
   smaller than C.
2. **Corner leaf:** R contains a specified e∈E as a vertex; every
   coefficient absolute sum except the tensor vertex index belonging
   to e is strictly smaller than C. The coefficient at that vertex is
   exactly Lₗ(e) for each l, so its absolute sum is C.

Then max_Q λ=C and {z∈Q:λ(z)=C}=E. Exact enclosures Uᵢⱼ≥Σₗ|cₗ,ᵢⱼ|
and a lower bound C₋≤C suffice whenever the strict tests use Uᵢⱼ<C₋.

## Definitions

Bᵈᵢ(u)=binom(d,i)uⁱ(1−u)ᵈ⁻ⁱ, for 0≤i≤d and 0≤u≤1.
An integer interval (a,b) at scale S=2ᵖ encloses the real interval
[a/S,b/S]. A finite binary prefix partition records path 0/1 for the
left/right child at each midpoint split, alternating x and y from the
root. Every leaf/pending path is explicit; a complete certificate has
no pending paths.

## Assumptions

d≥1, exact specified polynomials, correct real coefficient enclosures,
positive-width leaf boxes, a complete finite prefix partition of Q, and
verified equality λ(e)=C at every designated corner. No sign stability,
stationarity, Hessian assumption or number of local maxima is needed.

## Status by part

Overall status: **PROVED** (soundness implication; no successful n≥8
computation is claimed by this implication alone).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Stated finite-certificate implication | PROVED | Positivity, partition of unity, strict vertex characterization below |
| Integer interval conversion/subdivision enclosure rules | PROVED minor implementation lemma | Exact linear combination and outward midpoint rounding below |

Disposition: retained implementation of IDEA?argmax-alln-claude-05, a
global-maximum upper-bound variant of IDEA-290…302. No novelty claim.

## Depends on

No external mathematical theorem. For the n=8 implementation the exact
cardinals and principal embedding are reconstructed by the unchanged
part-2 `a5_n8_field.py` (PD-T179, provisional part-2 record 60), including
all exact interpolation and partition-of-unity checks. A successful
degree-eight claim additionally needs actual complete evidence and an
independent replay; these are not hypotheses supplied by the soundness
theorem itself.

## Checks and implementation

- `../code/part3/finite_bernstein.py`: exact coefficient conversion,
  outward integer subdivision, bound/corner predicates, source guards.
- `../code/part3/finite_bernstein_run.py`: bounded discovery and full
  leaf/pending prefix artifact. Producer always sets accepted=false.
- `../code/part3/finite_bernstein_check.py`: reconstructs the cardinals,
  checks source hashes, replays every supplied leaf, and verifies the
  complete prefix partition without invoking the search function.

Pinned source head: `328be35e55143013047ec03a70e9906e82b95353`.
Read-only part-2 field source SHA256:
`764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2`.
Every run artifact records the current producer/common source hashes,
exact target field vector, embedding precision and outward threshold.
Receipts record the raw certificate hash and checker source hash.
The replay shares arithmetic with the producer, so it is not advertised
as an independently implemented arithmetic kernel. A different-agent
execution and code/proof audit are required by the repository workflow.

## Sources

No literature or priority claim. Exact degree-eight cardinal provenance:
part-2 PD-T179 / `proof-attempts-2-codex-60-degree-eight-principal-field.md`.

## Proof

The basis functions Bᵈᵢ are nonnegative and sum to one by the binomial
theorem. Thus on each R, after its affine parametrization by (u,v)∈[0,1]²,

\[
\lambda\le\sum_{i,j}\Bigl(\sum_l|c_{l,ij}(R)|\Bigr)
B_i^d(u)B_j^d(v).
\]

A bound leaf gives strict inequality λ<C because the nonnegative
tensor weights sum to one. In a corner leaf the vertex coefficient has
absolute sum C and all others are <C. For equality λ=C all other tensor
weights must vanish, and the vertex weight must be one. At a tensor
vertex this weight is a product of uᵈ or (1−u)ᵈ with vᵈ or (1−v)ᵈ;
it equals one only at that same vertex since d≥1. Hence equality on
that leaf is possible only at e. The assumed corner values ensure
attainment at all e∈E. A complete cover of closed boxes proves the
assertion globally, including split boundaries. Overlap on boundaries
does not remove any point or introduce a new equality case. Replacing
absolute sums by upper bounds and C by a lower bound preserves all
strict inequalities. ∎

For completeness the implementation's interval rules are elementary.
For a finite exact rational linear combination Σwₖzₖ, zₖ∈[aₖ/S,bₖ/S],
choose the endpoint aₖ or bₖ according to the sign of wₖ, sum in exact
Fraction arithmetic, and round the lower endpoint down and upper
endpoint up to the integer grid. This encloses the exact result.
The conversion from power coefficients uses

\[
u^r=\sum_{i=r}^d\frac{\binom{i}{r}}{\binom d r}B_i^d(u),
\]

which follows by extracting uʳ from the binomial expansion of
(u+(1−u))ᵈ⁻ʳ; x=2u−1 is expanded exactly. Tensor products give the
bivariate formula. Exact de Casteljau at 1/2 expresses each child
coefficient as successive averages of parent coefficients. Each
integer average [a,b],[c,e] is enclosed by
[floor((a+c)/2),ceil((b+e)/2)] at the same scale. Induction over the
de Casteljau triangle and then over path depth gives valid enclosures
on every leaf. At a vertex the exact coefficient is the polynomial
value at that vertex, irrespective of enclosure width. This is why a
corner leaf may use exact equality there while testing every other
coefficient against C₋.

## Scope

This proves a sufficient certificate system, not that a bounded search
terminates for any degree. The frozen field-based implementation targets
n=8; the separately frozen general implementation has been executed
through n=16. It does not use a shifted-lattice majorant or count maxima.
Its direct λ bound is permitted by IDEA-05. Incomplete artifacts certify
only their supplied leaf inequalities, not a global maximum.

## Open items

Degree-specific complete evidence, different-agent replays, adversarial
controls and audit are recorded separately. The newly added general
constructor and its exact enclosure argument are below. No incomplete
artifact is promoted to a successful degree-specific claim.

## General constructor enclosure proof (implementation lemma)

The separate `finite_general.py`, `finite_general_run.py` and
`finite_general_check.py` retain the same Bernstein predicates while
replacing algebraic-field construction by rigorous trigonometric
enclosures. They leave all original n=8 source hashes unchanged.
Their existing mathematical dependency is PD-T101, proof §1, which
derives for every n≥1 the unique cardinals

\[
L_{jk}(x,y)=w_{jk}\sum_{p+q\le n}h_{pq}
T_p(\cos(j\pi/n))T_q(\cos(k\pi/(n+1)))T_p(x)T_q(y),
\]

where hₚq=(1 if p=0 else 2)(1 if q=0 else 2), except hₙ₀=1,
and wⱼk=2εⱼηₖ/[n(n+1)], endpoint ε,η=1/2 and otherwise one.
Thus no new unisolvence/cardinal theorem is inferred from finite tests.
The read dependency file is
`../../padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`,
SHA256 `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`.

All computed coefficients enclose those exact polynomials:

1. The alternating rational series for arctan(1/m) gives two enclosing
   partial sums differing by the first omitted term. The implementation
   uses m=5,239 and stops below 2⁻²²⁴. The identity
   π=16arctan(1/5)−4arctan(1/239) gives a rational bracket for π.
   To verify the identity directly, tan(2arctan(1/5))=5/12 and
   tan(4arctan(1/5))=120/119; the subtraction formula gives tangent one
   for 4arctan(1/5)−arctan(1/239). This angle lies in (0,π/2), selecting
   π/4. The series remainder follows from grouping the decreasing
   alternating positive terms or from the geometric series integrated
   on [0,1/m].
2. For a rational x∈[0,2], successive cosine Taylor partial sums enclose
   cos x once the next term is used as the alternating remainder. From
   the x²/2 term onward the terms decrease, since the next ratio is at
   most 4/(3·4)<1. The implementation stops only when the next term is
   below 2⁻²²⁴. Cosine is decreasing on [0,2]⊂[0,π], so endpoint
   evaluation encloses cos(π/M) for every M≥2.
3. T₀=1,T₁=z,Tᵣ=2zTᵣ₋₁−Tᵣ₋₂ gives outward interval enclosures for
   cos(rπ/M). The values at r=0,M and r=M/2 when M is even are replaced
   by the exact identities 1,−1,0. Periodicity and evenness reduce
   Tₚ(cos(jπ/M))=cos(pjπ/M) to this list without further rounding.
4. Every kernel multiplication and sum uses outward integer operations
   at scale 2¹⁹². Multiplication takes the minimum/maximum of the four
   endpoint products and rounds down/up after division by the scale.
   Rational weights are enclosed by exact Fraction floor/ceiling;
   Chebyshev polynomial coefficients are exact integers. The resulting
   power-coefficient intervals therefore enclose every exact cardinal.
   Two successive exact rational power-to-Bernstein transforms enclose
   its tensor coefficients; the preceding conversion lemma applies
   separately in each coordinate.

For even n, x↦−x permutes the nodes (j,k)↦(n−j,k); for odd n,
y↦−y permutes them by (j,k)↦(j,n+1−k). The parity is preserved in each
case. Cardinal uniqueness therefore proves invariance of λ under that
reflection. Consequently the two non-node corner values are equal:
E={(−1,−1),(1,−1)} for even n and E={(−1,−1),(−1,1)} for odd n.
Direct interval evaluation of Σ|L(e)| at both corners gives valid
enclosures of their common C, and intersecting them remains valid.
For an interval [a,b], the absolute lower bound is zero if it contains
zero and otherwise min(|a|,|b|); the upper bound is max(|a|,|b|).
No unresolved sign is treated as nonzero. This supplies C₋ and the
corner equality used by the already proved certificate implication.

The finite n=2 constructor control reconstructs its rational cardinals
by a separate Vandermonde inverse and checks that every coefficient
lies in the general constructor's interval. This is a regression,
not the justification of the all-n interval formulas above.

These proof steps establish enclosure soundness, not successful search
for any unspecified n. Degree-specific execution/replay records live in
the separate degree-eight and finite-degrees-nine-through-sixteen
theorems. Required Claude topic audit remains pending.

The general implementation's developer controls, on the actual complete
n=8 general certificate, accepted one complete and one genuinely partial
positive case and rejected 14 explicit defects: missing or duplicate
leaf, forged bound, wrong corner, changed threshold, changed π bracket,
changed source/dependency hashes, false complete flag, producer
self-approval, pending/leaf overlap, ancestor overlap, invalid path and
wrong count. The receipt is `../outputs/part3/finite_general_controls.json`.
The unchanged exact constructor result was cached once for these repeated
predicate checks; source hashes were checked before and after.
This control receipt supplements full per-degree replays and is not a
substitute for them.

## History

2026-11-01, Codex gpt-6.1-sol xhigh: wrote the exact sufficient reduction
and prepared code. The orchestrator explicitly authorized a bounded
n=8 pilot after the first-pass T1–T5 outcomes; high-degree T1 extensions
were still running concurrently. The T2/T3 local-profile forms and the
literal-existing-bound T4 effectivity projection were killed; none of
those outcomes is needed for this finite correctness implication.
