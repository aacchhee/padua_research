# PD-N?drift-codex-15 — A missing J-product cannot be repaired by prior-vector subtractions in a fixed degree

ID kind: PD-N.
Aliases: degree-two quotient obstruction; projection-only adverse-source example; unformed-product closure failure.
Split from: none. This is a scoped successor of the OPEN universal target PD-T055, not its resolution.
Split into: none.

## Statement

Let μ be the uniform positive measure on the ten nodes T_3={(i,j):i,j≥0, i+j≤3}. Write [p]=(p(i,j)/sqrt(10))_(T_3), and use the BJ columns through degree two. Consider **any** rule in the following class:

1. Through degree one the rule returns the exact positive-leading orthonormal columns [1], q_x=[x−1], q_y=[(x+2y−3)/sqrt(3)].
2. At degree two it forms exactly v_20=Xq_x, v_21=Yq_x, v_22=Yq_y, in that order. Only v_21 is perturbed, to v_21+εe.
3. At each of those three steps it may subtract arbitrary linear combinations of all previously stored vectors, through any finite number of passes, with arbitrary finite coefficients, then divide by a nonzero scalar. It adds no other vector, forms no other multiplication, and never changes a previously stored column. The result has full column rank.

Define

  r(y)=y³−(30/7)y²+(29/7)y−6/35,
  e=[r]/sqrt(72/175),
  b²=28/115.

Then for **every** rule in this class, its completed degree-two span has

  θ_2=|ε|/sqrt(b²+ε²),                                                (7)
  δ_J(1) ≥ (2/sqrt(3)) b|ε|/sqrt(b²+ε²),       J=X.                    (8)

Thus full exact reorthogonalization, and even arbitrary prior-vector coefficient choices within this degree, cannot restore exact J-closure after this source. For a relative aggregate source of size u, choose ε=u||v_21||=u sqrt(3/2). For 0<u≤1/4, the source satisfies ||εe||=u||v_21|| and

  θ_2≥2u,                     δ_J(1)≥u.                              (9)

This proves a worst-case source obstruction to exact closure or an o(u) guarantee in this class. It **does not** disprove an O(u poly(s)χ) guarantee, does not establish exponential amplification, and is not a deterministic IEEE rounding example.

## Definitions

θ and δ use exact spectral projector norms. Since U(3) holds by PD-N?drift-codex-14's row-factor proof, dim S_2=6<M=10. The unit vector e is orthogonal to S_2. “Projection-only” includes every number of exact reorthogonalization passes, but even allows arbitrary coefficients in place of orthogonal projection coefficients. It excludes extra X/Y-products, replacing old vectors, restarting from a reference basis, and adding a correction vector outside the current product plus the prior span.

## Assumptions

Exact arithmetic except the one declared aggregate preprojection perturbation; exact degree-one prefix; prescribed BJ products; full rank. Scalars and coefficients may depend on all known data, including ε and e. Even that knowledge does not help using only the permitted vector operations. Vectors are exact reals in an aggregate perturbation model, so no storage or per-operation IEEE realizability assertion is hidden.

## Status by part

Overall status: PROVED (explicit analytic finite example; independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Every-rule span identity and angle (7) | PROVED | Quotient-space proof below |
| Defect bound (8), relative-budget specialization (9) | PROVED | Explicit unit-vector witness below |

Candidate / claim disposition: REJECTED for the claim that prior-vector subtractions alone guarantee exact J-closure against every admissible source.
Rejection reason: refuted in precisely this fixed-degree rule class. The stronger PD-T055 target remains OPEN.

## Negative-result scope

Attempted mechanism: repair the unformed J-product by choosing additional prior-vector projection coefficients, while leaving the parent vectors, product set and already computed columns fixed.
Parameter range: this explicit non-product measure, degree two, any ε≠0, and every rule satisfying 1–3. It does not quantify over rules which intentionally corrupt or rotate the degree-one prefix, revise old vectors, use extra products, or inject additional arbitrary errors chosen to cancel this source.

## Depends on

Elementary linear algebra and finite rational sums only. PD-T053 explains the general defect–drift context but is unnecessary for the direct angle calculation. PD-T047's implicit-section error is a different quantity and is not inferred from (8).

## Checks

The exact expressions were developed using a temporary SymPy calculation of finite rational Gram matrices. The proof below supplies the full ten-row arithmetic certificate, so this is an analytic proof with explicitly checkable finite sums, not a computer-proof status claim. Supplementary developer command used Python/SymPy to compute the projections of xy−y against {1,x,y,x²,xy+2y²} and y³ against Π_2; it returned b²=28/115 and ||[r]||²=72/175. The parent's distinct mathematical checker reports an independently executed Fraction calculation of the polynomial values, all zero projection moments, both squared norms, ||v_21||²=3/2, the Jq_y decomposition and the two u≤1/4 inequalities: PASS. Its durable command/output/hash record is owned by the parent and pending integration; this report is not the required Claude audit.

## Sources

PD-T047/PD-T050 (unformed residuals and coefficient dependence), PD-T053 (defect–drift context), PD-T055 (OPEN universal obstruction), PD-N013 (measured full-reorthogonalization drift). The quotient argument and this finite example have no claimed historical priority.

## Proof or evidence

**Prefix and exact arithmetic.** The finite sums give E[x]=E[y]=1, E[x²]=E[y²]=2, E[xy]=1/2. Therefore q_x and q_y as stated are orthonormal to [1] and each other and have unit norms. Also ||v_21||²=E[y²(x−1)²]=3/2.

Put

  V=span{[1],[x],[y],[x²],[xy+2y²]},
  w=[(11x²+26xy−39x+6y²−26y+18)/23].

One checks w=(I−P_V)v_21, ||w||²=b²=28/115, and [r]⊥S_2, ||[r]||²=72/175. Here is the full evaluation table; the column numerators are 23w(i,j) and 35r(j):

| (i,j) | 23w | 35r |
|---|---:|---:|
| (0,0) | 18 | −6 |
| (1,0) | −10 | −6 |
| (2,0) | −16 | −6 |
| (3,0) | 0 | −6 |
| (0,1) | −2 | 24 |
| (1,1) | −4 | 24 |
| (2,1) | 16 | 24 |
| (0,2) | −10 | −36 |
| (1,2) | 14 | −36 |
| (0,3) | −6 | 24 |

The numerator in the w column has dot product zero with each of 1,x,y,x²,xy+2y²; its squared sum is 1288, giving 1288/(10·23²)=28/115. The numerator in the r column has dot product zero with 1,x,y,x²,xy,y²; its squared sum is 5040, giving 5040/(10·35²)=72/175. Finally

  (xy−y)−w=−(11/23)x²−(3/23)(xy+2y²)+(39/23)x+(3/23)y−18/23 ∈ V.

These statements prove all the projection assertions without a numerical linear-algebra computation. U(2) gives independence of the five displayed polynomial generators of V. Thus V has dimension five and S_2=V⊕span{w}.

**Why no coefficient choice helps.** A nonzero scaling and subtraction of prior vectors preserve the enlarged span:

  span(previous,q_new)=span(previous,v_current).

The degree-one parents never change. Consequently, after all degree-two columns have been created, *every* allowed rule has

  Shat_2=span(S_1,v_20,v_21+εe,v_22)
         =V⊕span{w+εe}.                                               (10)

Here V⊥w, V⊥e, w⊥e and ||e||=1. All rule coefficients have disappeared from (10). The spaces S_2 and Shat_2 share V and differ only by the angle between w and w+εe. This proves (7).

**A J-closure witness.** The degree-one span is exact and q_y is unit. Direct polynomial arithmetic gives

  Jq_y=(2/sqrt(3))v_21+[ (x²−3x+2y)/sqrt(3) ],

with the second term in V. The distance of w to span{w+εe} is b|ε|/sqrt(b²+ε²). Applying I−Phat_2 therefore gives exactly

  ||(I−Phat_2)Jq_y||=(2/sqrt(3))b|ε|/sqrt(b²+ε²).

Taking the supremum over unit vectors in S_1 proves (8). For ε=u sqrt(3/2),

  θ_2²/u²=345/(56+345u²),
  (the witness in (8))²/u²=2b²/(b²+(3/2)u²).

For u≤1/4, the first ratio is at least four and the second at least one (substitution reduces these to 345≥224+1380u² and 28/115≥(3/2)u²). This proves (9). ∎

## Scope

The result isolates what “the product was never formed” can rigorously mean: once parents and the current degree's raw products are fixed, changing projection coefficients cannot change their joint span. A single source in an unformed J direction then creates a J-defect regardless of those coefficients. This is stronger than inspecting one reorthogonalization schedule, but substantially weaker than PD-T055's proposed exponential obstruction.

Closure and implicit-section accuracy must remain separate. A normal component of a section residual may give (8) while its projection onto Qhat is much smaller; no large in-span implicit-section error is proved here. Similarly the source model permits εe but a standard per-operation model may not generate it. There is no claimed evidence about actual deterministic IEEE runs.

## Open items

An amplification theorem with controlled χ and well-conditioned references, an adverse-source theorem allowing arbitrary changes of the noiseless degree-one gauge, and a verified per-operation generator for the exhibited source. Parent repair or extra-product rules require another class and may evade this obstruction.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed; rules 806cc7b4509fd93bae652f9545d32d95529f8281. New explicit quotient-space example. The originally hoped-for all-degree exponential theorem was not obtained and remains OPEN.
