# PD-T?proof-attempts-codex-02 — The generic pattern commutant is three-dimensional in every degree

Final ID: **PD-T102** (2026-11-01; provisional heading retained as alias; reservation published at `020dcddd36fa1e3254cbf288701d5ab02d27c580`).

ID kind: PD-T.
Aliases: T-B5; cyclic-first-column argument; simple x-spectrum pattern commutant; generic affine span.
Split from: the genericity question B5 in `topics/programme-ideas-20261031/OPEN_TARGETS.md` at `cadb35066160e466cb1704b9791ad6f374446422`; positive complement to `PD-N?programme-ideas-claude-04`, not a weakening of that counterexample.
Split into: none. Source and crosswalk integration applied during authorized PR finalization; see `../finalization/id-map.json`.

## Statement

Fix any integer n≥2 and N=(n+1)(n+2)/2. Use the graded order

    1; x,y; x²,xy,y²; …; xⁿ,xⁿ⁻¹y,…,yⁿ

and exactly the patterns defined below. For every Π_n-unisolvent set of N real nodes z_k=(x_k,y_k), with positive weights w_k summing to one, form the commuting positive-pivot section pair (H_x,H_y) in the graded orthonormal basis with positive leading coefficients. **If the x_k are pairwise distinct, then**

\[
 \mathcal C_y(H)=\{E\in\mathbb R^{N\times N}:E^\mathsf T=E,
       \operatorname{supp}(E)\subseteq P_y,[H_x,E]=0\}
       =\operatorname{span}\{I,H_x,H_y\}.
\]

In particular, B5 is true for every n≥2 outside the proper real-algebraic (hence real-analytic) subset

\[
 \mathcal Z=\left\{\prod_{i<j}(x_i-x_j)^2=0\right\}
\]

of the unisolvent positive normalized parameter domain. No assertion is made that all points of this larger exceptional set have dimension greater than three.

## Definitions

Indices are zero-based; m_0=1,m_1=x,m_2=y. For deg(m_j)<n, π_x(j) and π_y(j) are the indices of x m_j and y m_j. If deg(m_j)=n, that column has no corresponding upper cutoff. Define the symmetric structural masks

\[
 (i,j)\in P_\alpha\iff
 [\deg m_j=n\text{ or }i\leq\pi_\alpha(j)]\ \text{and}\
 [\deg m_i=n\text{ or }j\leq\pi_\alpha(i)],\qquad\alpha=x,y.
\]

These are structural masks, including allowed positions that happen to have value zero on a particular pair; `pattern(H_y)` in the target has this meaning. It does not mean the numerical nonzero support of H_y.

Let V_kj=m_j(z_k), W=diag(w_k). The positive-diagonal QR factorization W^(1/2)V=QR gives H_x=Qᵀdiag(x_k)Q and H_y=Qᵀdiag(y_k)Q. There are exactly N nodes, so Q is square and the pair commutes. e_0 is the constant basis vector, since Σw_k=1.

## Assumptions

The fixed graded order, structural patterns, exactly N nodes, Π_n-unisolvence, positive normalized weights and exact arithmetic. The sufficient additional condition for the pointwise conclusion is distinct x coordinates. Other orders, measures with more than N nodes and approximate commutation are outside this statement.

## Status by part

Overall status: **PROVED** (written all-n proof; Claude audit-01 ACCEPTED; minor wording dispositions in response-01.md).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Pointwise span equality whenever x coordinates are distinct, every n≥2 | PROVED | Cyclicity plus three-entry first column, below |
| Global real-analytic parameter dependence and dense open genericity, every n≥2 | PROVED | Explicit positive Cholesky construction and polynomial exceptional set, below |
| Exact rational instances n=2,…,6 | Verification evidence | Rational LDL section pair, exact support/commutation and reduced rank, `../code/b5_exact_instances.py` |

The containment, pivot independence and analytic formulas are routine steps of B5. This proves the target itself in all degrees, not only supporting lemmas. The existing universal claim remains refuted by the Padua example, which has repeated x coordinates.

## Depends on

Elementary linear algebra, positive-diagonal Cholesky factorization, polynomial root counting by Rolle's theorem. `PD-T?programme-ideas-claude-01` supplies the source definitions/context; the properties needed here are derived explicitly below, so its global manifold claim is not an inherited proof dependency.

## Checks

Command, from the repository root:

```text
python topics/padua-proof-attempts-20261101/code/b5_exact_instances.py > topics/padua-proof-attempts-20261101/outputs/b5_exact_instances.json
```

Producer code uses only exact integers and rationals in SymPy; it builds nodes (t,t^(n+1)), t=1,…,N, with weights 1/N. The rational unit-leading orthogonal basis is obtained by LDLᵀ. Its multiplication matrices A_x,A_y are checked for exact commutation, D-self-adjointness, structural support, positive diagonal norms and unit monic pivots. Diagonal similarity converts them to the real symmetric positive-pivot pair without changing zero positions or ranks, as proved below. The code computes the rank of the **reduced rational constraint matrix** consisting of rows 3,…,N−1 of V⁻¹, and checks that its kernel is exactly the node values of span{1,x,y}. The full original commutator-map rank is deduced by the proved equivalence below; it is not reported as a directly computed radical-valued matrix rank. Executed results, versions and hashes appear in the receipt and attempt note; independent rerun is recorded separately by the orchestrator.

The mathematical proof in this record does not depend on finite computation. In particular, the last N−3 rows of any invertible V⁻¹ necessarily have rank N−3; that reduced-rank calculation is a consistency check, not an independent test of the commutant dimension. The rational witness checks establish unisolvence, positive norms/pivots, pattern and commutation; dimension three follows from the all-n proof. Claude audit-01 additionally computed full-system nullities by a separate checker (`../audit-support/claude-audit-01/aud_b5.py`), in its stated finite scope.

Developer execution completed with Python 3.12.14, SymPy 1.14.0, no seeds or numerical tolerances:

| n | N | Symmetric P_y variables | Computed reduced rank | Full map rank by proof | Commutant dimension (by the proof) |
|---|---|---|---|---|---|
| 2 | 6 | 17 | 3 | 14 | 3 (by the proof) |
| 3 | 10 | 36 | 7 | 33 | 3 (by the proof) |
| 4 | 15 | 65 | 12 | 62 | 3 (by the proof) |
| 5 | 21 | 106 | 18 | 103 | 3 (by the proof) |
| 6 | 28 | 161 | 25 | 158 | 3 (by the proof) |

All exact pair checks passed. Script SHA-256: `fb56be6166ce10ecae213cd1c4e169594a52b0a922058e52934b88ccd0edf18b`. Developer receipt `../outputs/b5_exact_instances.json` is 5,327 bytes, SHA-256 `251496a1a117054608dd55d32c7dfa5441c5af34cf7cb00d1f99ec0e9e80da02`.

## Sources

No external theorem is used. Relevant source records read at the pinned base: programme finite Favard -01, universal-commutant counterexample -N04, OPEN_TARGETS B5, `m2_common.py`, `m2_favard_commutant.py`, the exact Padua counterexample code, and programme IDEA-08. No historical novelty claim follows from this elementary proof.

## Proof or evidence

### 1. Structural containment and independence

Within degree d, write m_j=x^(d−b)y^b with b increasing from 0 to d. Multiplication by x gives index offset b in degree d+1; multiplication by y gives offset b+1. Hence π_y(j)=π_x(j)+1 whenever deg(m_j)<n. It follows immediately from the two mask inequalities that P_x⊆P_y. Every diagonal position is in both masks.

Gram–Schmidt of this multiplicatively compatible monomial order gives p_j with leading monomial m_j and positive leading coefficient κ_j. The expansion of x p_j has no modes later than x m_j whenever deg(m_j)<n. Its coefficient at p_(π_x(j)) is κ_j/κ_(π_x(j))>0. Symmetry supplies the other mask inequality. The same applies to y. Thus H_x and H_y have the stated masks and positive pivots. At top degree the entire function space on the N nodes is already Π_n, so multiplication is defined and H_x,H_y commute by their displayed simultaneous diagonalization.

Therefore I,H_x,H_y lie in the domain and commute with H_x. They are linearly independent: in column zero, H_x has a positive row-1 pivot and zero row 2, while H_y has a positive row-2 pivot. For aI+bH_x+cH_y=0, row 2 of column zero gives c=0, row 1 then gives b=0, and row 0 gives a=0. This proves dim C_y≥3 for every permitted data set, even when x coordinates coincide.

### 2. A cyclic constant vector makes the first column determine the commutant

Because p_0=1, Qe_0=(√w_1,…,√w_N)ᵀ. Thus the Krylov matrix

\[
 [e_0,H_xe_0,\ldots,H_x^{N-1}e_0]
   =Q^\mathsf T\operatorname{diag}(\sqrt{w_k})
     [x_k^{r}]_{k=1,\ldots,N;\ r=0,\ldots,N-1}
\]

is invertible when the x_k are distinct. In particular e_0 is cyclic for H_x.

On all matrices commuting with H_x, the map E↦Ee_0 is injective. Indeed, if Ee_0=0, then E H_x^r e_0=H_x^r E e_0=0 for every r, so cyclicity gives E=0. But column zero of P_y is supported exactly at rows 0,1,2: π_y(0)=2 and the other mask inequality imposes no further restriction on those positions. Consequently, for E∈C_y(H), Ee_0 belongs to span{e_0,e_1,e_2}. Injectivity yields dim C_y≤3. Step 1 supplies equality and the asserted span. This proves the pointwise theorem for every n≥2.

### 3. Real-analytic dependence and genuine genericity

On labelled nodes and weights, the entries of G=VᵀWV are polynomials in the coordinates and weights. Unisolvence and strict weight positivity make G positive definite. Its upper-triangular Cholesky factor R with positive diagonal is real-analytic: the usual recursive formulas use addition, multiplication, division by positive pivots, and the positive square root of strictly positive analytic functions. Then

\[
 H_x=R^{-\mathsf T}V^\mathsf TW\operatorname{diag}(x_k)VR^{-1}
\]

and its y analogue are real-analytic. The same proof establishes the needed part of the source's analytic dependence directly. In particular the coefficient matrix of the fixed-domain map E↦[H_x,E] is real-analytic. A nonzero rank minor remains nonzero locally; equivalently rank is lower semicontinuous. By Step 1 its rank is at most |P_y|_sym−3 everywhere, and Step 2 attains that rank for every distinct-x input.

For global density one need not assume the unisolvent parameter domain is connected. The discriminant Δ=∏_(i<j)(x_i−x_j)^2 is a nonzero polynomial on the ambient coordinate space. Its zero set has empty interior, and the unisolvent positive domain is open within the weight-normalization hyperplane. Hence its complement is dense and open in that entire domain, component by component. It is nonempty; an explicit witness in every degree is supplied in Step 4. Since Δ is permutation-invariant, the statement descends from labelled nodes to unordered node sets. This proves the target's genericity with an explicit sufficient exceptional set, avoiding a gap from a local rank witness to a disconnected-domain density claim.

### 4. Rational witnesses exist in every degree

Take t=1,…,N and z_t=(t,t^(n+1)), w_t=1/N. Restricting a monomial x^a y^b to this curve gives t^(a+(n+1)b). These N exponents are distinct for a+b≤n: equality would force a−c=(n+1)(d−b), with |a−c|≤n, hence a=c,b=d.

A nonzero real polynomial with k nonzero monomial terms has at most k−1 distinct positive roots. For completeness, divide by its smallest power of t. The quotient has a nonzero constant term and k−1 other terms. Its derivative has k−1 terms; by induction it has at most k−2 distinct positive roots. Rolle's theorem then bounds the quotient's roots by k−1. The case k=1 is immediate. Therefore a nonzero linear combination of the N restricted monomials cannot vanish at the N distinct positive t values. V is invertible, proving Π_n-unisolvence of this rational witness for every n. All weights are positive, and the x coordinates are distinct. Step 2 gives dim C_y=3 for every such witness, including n=2,…,6 requested for finite evidence.

### 5. Exact rational scaling and the reduced rank checked by code

For rational nodes and weights let G=L D Lᵀ be its exact LDLᵀ factorization, with L unit lower triangular and D positive diagonal. Set C=L⁻ᵀ and P=VC, so PᵀWP=D. The monic orthogonal-basis multiplication matrices are

\[
 A_x=D^{-1}P^\mathsf TW\operatorname{diag}(x_k)P,\qquad
 A_y=D^{-1}P^\mathsf TW\operatorname{diag}(y_k)P.
\]

They are rational and D-self-adjoint. With S=D^(1/2), the symmetric orthonormal pair is H_α=S A_α S⁻¹. This similarity preserves zero positions and multiplication pivots' positivity (the latter equal √(D_(π(j))/D_j) in this unit-leading basis). It also sends any unknown E to S⁻¹ES, preserving commutation, and turns symmetry into D-self-adjointness. It is a linear isomorphism on the corresponding patterned domains and codomains, so the relevant ranks are unchanged. Square roots never have to be represented in a rational checker.

For distinct x, an alternative exact reduction is smaller still. Every matrix E commuting with H_x has the form Qᵀdiag(e_k)Q, since H_x has simple spectrum. Column zero's coordinates are the discrete orthonormal coefficients of the node value vector e=(e_k):

\[
 (Ee_0)_j=\sum_k w_k p_j(z_k)e_k.
\]

They vanish for j≥3 exactly when e belongs to the node evaluations of span{p_0,p_1,p_2}=span{1,x,y}. This is equivalent to the last N−3 entries of V⁻¹e being zero. Conversely such affine e gives E=aI+bH_x+cH_y, so all the remaining P_y conditions hold automatically. Thus the full patterned commutant is isomorphic to the nullspace of the rational (N−3)×N matrix (V⁻¹)_[3:N,:]. Its rank is N−3 and its kernel has dimension three. The full commutator map on |P_y|_sym independent symmetric variables therefore has rank |P_y|_sym−3 by rank-nullity. This is the precise proved reduction used by the script; no full-radical rank calculation is claimed. ∎

## Scope

B5 is closed for every n≥2, with a sufficient pointwise condition stronger and more explicit than an unspecified generic set. Repeated x coordinates are allowed in the original domain; they are excluded only from this sufficient condition. The Padua n=2 six-dimensional commutant remains a valid exception and its existing PD-N is unchanged. Description of the commutant on collision strata remains unresolved.

## Open items

Claude audit-01 ACCEPTED; the completed independent exact-run record is in independent-checks.md. No all-n stretch remains for B5. No stability, coordinate-collision classification or different-pattern theorem is claimed. The earlier source/ID deferral was superseded by AC’s finalization request; the source changes and final-ID mapping are now applied.

## History

2026-11-01, Codex developer `/root/a1_develop`, requested gpt-6.1-sol xhigh; runtime-resolved metadata not independently exposed. Rules/base `cadb35066160e466cb1704b9791ad6f374446422`. Root proposed the cyclic-first-column route after A1 completed; this file develops that proof and the rational verification reduction. The original all-n B5 statement is retained; the sufficient distinct-x theorem proves it rather than narrowing the target silently.
