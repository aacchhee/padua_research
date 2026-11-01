# PD-T?argmax-alln-codex-02 — Exact degree-two Padua global maximum

ID kind: PD-T.
Aliases: P0; T5; n=2 global argmax; quadratic Bernstein certificate.
Split from: PD-T099, the assertion for every integer n≥2 that the Padua Lebesgue function attains its maximum only at the non-node corners.
Split into: none.

## Statement

For the even-checkerboard degree-two Padua set on [−1,1]²,

\[
\max\lambda_2=3,\qquad
\{(x,y):\lambda_2(x,y)=3\}=\{(-1,-1),(1,-1)\}.
\]

Both equality points are non-node corners. Thus P0, the n=2 part of PD-T099, holds.

## Definitions

The nodes, in the order used below, are

\[
(1,1),\ (1,-\tfrac12),\ (0,\tfrac12),\ (0,-1),\
(-1,1),\ (-1,-\tfrac12).
\]

They are precisely (cos(jπ/2),cos(kπ/3)) with 0≤j≤2,
0≤k≤3 and j+k even. The cardinal polynomials L₁,…,L₆ belong to the space of bivariate polynomials of total degree at most two and satisfy Lᵢ(nodeⱼ)=δᵢⱼ. The Lebesgue function is λ₂=Σᵢ|Lᵢ|.

## Assumptions

Real x,y in [−1,1]. Exact rational arithmetic is used in the optional checker. No numerical hypothesis or unproved all-degree formula is required.

## Status by part

Overall status: **PROVED** (written finite algebraic proof below; independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| max λ₂=3, with exactly the two stated equality points | PROVED | Explicit rational cardinals, four Bernstein bounds and strictness argument |

Candidate disposition: retained instance of IDEA?argmax-alln-claude-05. No historical novelty claim.

## Depends on

No substantive external theorem. The even-checkerboard convention agrees with PD-T101, but the cardinal construction and all inequalities are verified here directly.

## Checks

Producer/checker: `../code/part3/finite_n2_exact.py` (Python standard library only).
Pinned input head: `328be35e55143013047ec03a70e9906e82b95353`.
Executed from the repository root:

```
python -B topics/padua-argmax-alln-20261101/code/part3/finite_n2_exact.py --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n2_exact.json
```

Result: exit 0; accepted=true; all predicates rational and exact. Checker SHA256:
`a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2`.
Evidence SHA256: `8c3e9948db4b09d9eec5a2aaf3f8e5c0f8ec3e710e6ab63c72598613aa3e49c9`.
The JSON contains every cardinal and all 216 rational Bernstein coefficients, not a sampling grid.
The orchestrator reports a different-agent exact execution and independent
mathematical/code inspection passed. The independently written output
`../outputs/part3/finite_n2_independent.json` is byte-identical to the
developer JSON (same SHA256 above). Required Claude topic audit remains
pending; the independent Astra check supplements it.

## Sources

No literature claim and no transferred literature technique. Tensor Bernstein positivity is proved in the following elementary calculation.

## Proof

In the stated node order the six cardinals are

\[
\begin{aligned}
6L_1&=x^2+2xy+x+2y^2+y-1,\\
6L_2&=2x^2-2xy+2x-2y^2-y+1,\\
3L_3&=-2x^2-2y^2+y+3,\\
3L_4&=-x^2+2y^2-y,\\
6L_5&=x^2-2xy-x+2y^2+y-1,\\
6L_6&=2x^2+2xy-2x-2y^2-y+1.
\end{aligned}
\]

Substitution verifies the cardinal equations. In monomial order
(1,x,y,x²,xy,y²), the node Vandermonde determinant is −27/2≠0,
so these are the unique total-degree-two cardinal polynomials.

Put B₀(u)=(1−u)², B₁(u)=2u(1−u), B₂(u)=u². For u∈[0,1]
these numbers are nonnegative and sum to one. On a unit quadrant with
lower-left corner (a,b), put x=a+u, y=b+v and write

\[
L_\ell(a+u,b+v)=\sum_{i,j=0}^2 c_{\ell,ij}^{a,b}B_i(u)B_j(v).
\]

Every L has degree at most two in each variable, so the expansion is exact.
For clarity, its coefficients can be calculated without inversion: if
L(a+u,b+v)=Σ pᵣₛuʳvˢ, then

\[
c_{\ell,ij}^{a,b}=\sum_{r\le i,\,s\le j}
p_{rs}\frac{\binom{i}{r}}{\binom{2}{r}}
\frac{\binom{j}{s}}{\binom{2}{s}}.
\]

Indeed uʳ=Σᵢ₌ᵣ²[binom(i,r)/binom(2,r)]Bᵢ(u) for r=0,1,2,
as direct expansion shows. Set Aᵃᵇᵢⱼ=Σₗ|cₗ,ᵢⱼᵃ,ᵇ|. Direct rational substitution in the displayed cardinals gives the following four matrices (row index i, column index j):

\[
A^{-1,-1}=\begin{pmatrix}3&5/3&2\\11/6&2&5/3\\1&2&5/3\end{pmatrix},\qquad
A^{0,-1}=\begin{pmatrix}1&2&5/3\\11/6&2&5/3\\3&5/3&2\end{pmatrix},
\]
\[
A^{-1,0}=\begin{pmatrix}2&5/2&1\\5/3&11/6&7/3\\5/3&5/3&7/3\end{pmatrix},\qquad
A^{0,0}=\begin{pmatrix}5/3&5/3&7/3\\5/3&11/6&7/3\\2&5/2&1\end{pmatrix}.
\]

The triangle inequality and positivity imply

\[
\lambda_2(a+u,b+v)\le\sum_{i,j}A^{a,b}_{ij}B_i(u)B_j(v)\le3.
\]

On either upper quadrant every entry is strictly less than 3, so equality
is impossible. On the lower-left quadrant the only coefficient equal to 3
is A₀₀. Equality in the second inequality forces B₀(u)B₀(v)=1,
which forces u=v=0 and hence (x,y)=(−1,−1). On the lower-right quadrant
the only such coefficient is A₂₀; equality forces u=1,v=0 and hence
(x,y)=(1,−1). This handles quadrant boundaries as well as interiors.

At (1,−1) the cardinal values are
(0,1,−2/3,2/3,1/3,−1/3), whose absolute values sum to 3;
x-reflection permutes L₁↔L₅ and L₂↔L₆ while fixing L₃,L₄, so the
same holds at (−1,−1). Neither point is in the node list. This proves
the maximum, attainment, and strict equality characterization. ∎

## Scope

Only n=2. Together with the already certified n=3,…,7 results, this fills the missing smallest-degree case. It supplies no inference for n=8 or for all n.

## Open items

Claude audit of the exact checker/proof package. PD-T099 for the remaining degrees stays OPEN. A larger-degree finite certifier is a separate correctness record and computation.

## History

2026-11-01, Codex development subagent, gpt-6.1-sol xhigh: developed the rational four-quadrant proof and executed the self-contained Fraction checker. Rules/source read at `328be35e55143013047ec03a70e9906e82b95353`; no Git operations performed by this subagent.
