# PD-N?drift-codex-15 — In a fixed degree, no prior-vector subtraction rule removes the span drift or closure defect of a raw-product source

ID kind: PD-N.
Aliases: fixed-degree projection-only closure obstruction; fixed-degree quotient identity; exact fixed-prefix instance of PD-T055's heuristic span identity; projection-only adverse-source example (T_3 instance); degree-two quotient obstruction. Superseded title and alias, kept for search only: “A missing J-product cannot be repaired by prior-vector subtractions in a fixed degree”; “unformed-product closure failure”. Their formed/unformed-J interpretation is withdrawn (Claude audit-01, E34-F1; see History).
Split from: none. This is a scoped successor of the OPEN universal target PD-T055, not its resolution.
Split into: none.

## Statement

**Setting.** Let μ be a positive discrete measure with distinct nodes z_i=(x_i,y_i) and weights w_i>0, i=1,…,M. Write [p]=(sqrt(w_i)p(z_i))_i, X=diag(x_i), Y=diag(y_i), S_t={[p]: p∈Π_t}, N_t=(t+1)(t+2)/2, and let P_t be the orthogonal projector onto S_t. Fix t≥0 with U(t+1) and M>N_(t+1).

- *Prefix.* q_0,…,q_(N_t−1) is the exact positive-leading orthonormal basis of S_t in graded order, i.e. exact Gram–Schmidt of the monomials. Every exact, fully orthogonalized admissible recurrence returns these columns.
- *Products.* Fix an admissible selection in degree t+1: for j=0,…,t+1, an operator A_j∈{X,Y} and a degree-t parent p(j) with x^(t+1−j)y^j = a_j·(monomial of p(j)). Here a_j=x or y, and (t+1,0) uses X, (t+1,t+1) uses Y. The raw products are v_j=A_j q_(p(j)).
- *Source.* Fix one index m and a source f∈R^M whose normal part f_⊥=(I−P_(t+1))f is nonzero. The m-th raw product becomes v_m+f; the other raw products are exact.

**Rule class R (projection-only).** The degree-(t+1) columns are created one at a time, in any fixed order. Each creation:

1. starts from its raw product (v_m+f for column m);
2. subtracts arbitrary finite linear combinations of the vectors stored so far (the prefix and the degree-(t+1) columns already created), in any finite number of passes; the real coefficients are arbitrary and may depend on all data, including f;
3. multiplies the result by a nonzero scalar and stores it.

The rule adds no other vector, forms no other product and never changes a stored vector.

Put

  V_m=S_t+span{v_j: j≠m},   w=(I−P_(V_m))v_m,   b=||w||,   ŵ=w/b,   α=⟨f,w⟩/b²,

and, for A∈{X,Y},

  κ_A=||P_t A ŵ||_2 = max over unit s∈S_t of |⟨As,ŵ⟩|.

**Lemma.** For every rule in R:

(a) every processed vector is nonzero, and the N_(t+1) stored columns have full column rank;

(b) the computed span does not depend on the rule:

  Shat_(t+1)=V_m⊕span{g},   g=(1+α)w+f_⊥,   whereas S_(t+1)=V_m⊕span{w};          (10)

(c) θ_(t+1)=||Phat_(t+1)−P_(t+1)||_2 = ||f_⊥|| / sqrt((1+α)²b²+||f_⊥||²) > 0;          (11)

(d) for A∈{X,Y}, with Phat_t=P_t,

  δ_A(t)=||(I−Phat_(t+1))A P_t||_2 = κ_A θ_(t+1)   (equality).                        (12)

Moreover κ_A=0 if and only if A S_t⊆V_m, and the operator A_m that formed column m has κ_(A_m)≥b, so δ_(A_m)(t)≥bθ_(t+1)>0.

**Negative statement.** Hence no rule in R makes the degree-(t+1) span exact or removes the closure defect. θ_(t+1) and both δ_A(t) take the same value for every rule in R, and max_A δ_A(t)≥δ_(A_m)(t)≥bθ_(t+1)>0. For a normal source f=εe (e⊥S_(t+1), ||e||=1, so α=0), θ_(t+1)=|ε|/sqrt(b²+ε²). With a relative size ε=u||v_m||, u>0, for both A∈{X,Y}

  δ_A(t)/u = κ_A||v_m|| / sqrt(b²+u²||v_m||²) → (κ_A/b)||v_m||   as u→0.          (13)

For the forming operator the limit is (κ_(A_m)/b)||v_m|| ≥ ||v_m|| > 0, with equality if and only if κ_(A_m)=b. Equality holds in the T_3 instance below (source in v_21, κ_Y=b), but not in general: with the source in v_20=Xq_x of the same T_3/BJ setting, κ_X²/b²=4/3 and the squared limit is 88/15, not ||v_20||²=22/5. So no o(u) closure guarantee holds in R for this source model.

**Instance (T_3, BJ).** Let μ be uniform on the ten nodes T_3={(i,j): i,j≥0, i+j≤3}, so [p]=(p(i,j)/sqrt(10)). Take t=1 and the prefix [1], q_x=[x−1], q_y=[(x+2y−3)/sqrt(3)]. The BJ products are v_20=Xq_x, v_21=Yq_x and v_22=Yq_y. Take m=(2,1), the column formed by Y, and f=εe with

  r(y)=y³−(30/7)y²+(29/7)y−6/35,   e=[r]/sqrt(72/175),   b²=28/115.

Then V_m=V=span{[1],[x],[y],[x²],[xy+2y²]}, κ_X=(2/sqrt(3))b and κ_Y=b. For every rule in R and every ε≠0:

  θ_2=|ε|/sqrt(b²+ε²),                                                (7)
  δ_X(1)=(2/sqrt(3)) b|ε|/sqrt(b²+ε²),                                 (8)
  δ_Y(1)=b|ε|/sqrt(b²+ε²)=(sqrt(3)/2)δ_X(1).                           (8')

Thus the originally stated bound “δ_J(1)≥(2/sqrt(3))b|ε|/sqrt(b²+ε²)” holds with equality, and the formed operator Y carries a defect of the same order. For a relative aggregate source of size u, take ε=u||v_21||=u sqrt(3/2). Then ||εe||=u||v_21||, and for 0<u≤1/4

  θ_2≥2u,     δ_X(1)≥u,     δ_Y(1)≥u.                                  (9)

This is a fixed-degree O(u) obstruction to exact or o(u) closure in R. It:

- does not disprove an O(u poly(s)χ) guarantee;
- establishes no amplification across degrees;
- is not a deterministic IEEE rounding example;
- does not single out J, unformed products or non-product support. The defect lands on the operator that formed the perturbed column, and on any other operator whose image of S_t meets that column modulo the other columns.

## Definitions

θ and δ use exact spectral projector norms. δ_A(t)=||(I−Phat_(t+1))A Phat_t||_2 is PD-T053's defect, with Phat_t=P_t because the prefix is exact. “Admissible” is as in PD-T054 and PD-T?drift-codex-10: monomial(j)=a_j·monomial(p(j)). A_m is the operator in column m's relation. In BJ for t≥1, X forms only (t+1,0) and Y forms the others.

“Projection-only” means the class R. It includes every number of exact reorthogonalization passes, and it allows arbitrary coefficients in place of orthogonal projection coefficients. It excludes:

- extra X/Y-products;
- revising stored vectors, including the prefix and its gauge;
- restarting from, or injecting, a reference basis;
- repairing parents;
- adding any vector outside the raw product plus the stored span.

## Assumptions

- Exact arithmetic, except for the one declared aggregate source f in one raw product.
- Exact orthonormal prefix through degree t; fixed admissible degree-(t+1) raw products.
- U(t+1), M>N_(t+1) and f_⊥≠0. Full column rank is conclusion (a), not an assumption.
- Coefficients and scalars may depend on all data, including f. Even that knowledge does not help when only the permitted vector operations are used.
- Vectors are exact reals in an aggregate perturbation model, so no storage or per-operation IEEE realizability assertion is hidden.
- Only one raw product carries a source; simultaneous sources in several products are not treated.

## Status by part

Overall status: PROVED. This is an analytic fixed-degree lemma with an explicit T_3 instance. Claude audit-01 confirmed the original T_3 statement (CONFIRMED-WITH-CORRECTIONS, E34-F1/F2). The general lemma (a)–(d) was added in Claude response-01. Codex audit-02 confirmed (a)–(d), the T_3 instance and the qualitative no-exact/o(u) obstruction, and refuted the response-01 relative-source limit equality δ_(A_m)(t)/u→||v_m|| (finding A02-M1). Claude response-02 replaces it by (13); that correction requires re-audit.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Lemma (a)–(d): full rank, rule-independent span (10), angle (11), defect identity (12), κ_(A_m)≥b | PROVED | Proof below |
| Negative statement: no rule in R removes the drift or the closure defect; no o(u) closure guarantee; relative-source limit (13) | PROVED | Immediate from the lemma; (13) corrected in response-02 (A02-M1), re-audit pending |
| T_3/BJ instance: U(3), (7), (8) with equality, (8'), (9) | PROVED | Inline U(3) proof and ten-row arithmetic certificate below |
| Further instances: other perturbed columns, mirror selection, product grid Q_3, non-uniform weights, degree 2→3 on T_4 with three selections, random rational nodes at t=0,1 | Exact finite computations; checks only, no separate claim | [response-01-e4-closure.json](../../../topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json); the lemma already proves their qualitative conclusions |

Candidate / claim disposition: REJECTED for the claim that, within a fixed degree with fixed prefix and fixed products, prior-vector subtractions (any coefficients, any number of passes) restore exact or o(u) span and closure against every admissible raw-product source.
Rejection reason: refuted, in exactly class R and the parameter range below. The stronger PD-T055 target remains OPEN.

## Negative-result scope

Attempted mechanism: restore exact (or o(u)) span and X/Y-closure within a fixed degree, after an aggregate source in one raw product, by the choice of reorthogonalization coefficients and passes alone. The exact prefix, the parents, the products and the earlier columns stay fixed. This is the “reorthogonalize harder” repair, here allowed arbitrary coefficients.

Parameter range: the negative statement covers:

- every positive discrete measure with U(t+1) and M>N_(t+1), product or non-product;
- every t≥0 and every admissible degree-(t+1) selection;
- every single raw-product source with nonzero normal part;
- every rule in R.

It does not cover:

- rules that change the prefix or its gauge, revise stored vectors, use extra products, restart from or inject a reference basis, or repair parents (see IDEA?drift-claude-17);
- several simultaneous sources;
- propagation across several degrees;
- deterministic IEEE executions.

## Depends on

- **PD-T055's recorded heuristic** ([bj-universal-reorthogonalization-obstruction-open.md](bj-universal-reorthogonalization-obstruction-open.md), Proof or evidence, “Heuristic (not a proof)”): span Q̂_(≤k)=span(Q̂_(<k), B_kq̂_(p(k))−f_k), so the step-k coefficients change the computed spans only through f_k. Identity (10) is the exact, fixed-prefix, single-degree instance of that heuristic. Because the prefix is fixed, the heuristic's parent-change term B_kv vanishes, and no first-order caveat remains. The span step of the proof below is this identity; its credit belongs to PD-T055.
- Triangularity of admissible products modulo Π_t. This is the induction in the proof of PD-T?drift-codex-10, restated in (a) below.
- PD-T053, for the definition of δ_A.
- Elementary linear algebra and finite rational sums.

U(3) for T_3 is proved inline. It was previously cited from PD-N?drift-codex-14, which is withdrawn as a registry vehicle (IDEA?drift-codex-14). PD-T047's implicit-section error is a different quantity and is not inferred from (12).

## Checks

The result is an analytic proof; no computer proof is claimed.

- **Codex independent-math-01** ([checks/independent-math-01.md](../../../topics/padua-lanczos-drift-20261101/checks/independent-math-01.md), E4 paragraph; [evidence/independent-math-01.json](../../../topics/padua-lanczos-drift-20261101/evidence/independent-math-01.json), key `independent_own_checker.E4`, produced by `check_independent_math.py`'s `check_e4`). It reconstructed the original T_3 argument and recomputed exactly the polynomials w and r, all projection moments, 28/115, 72/175, ||v_21||²=3/2, the Jq_y identity and the two u inequalities: PASS. It did not test the every-rule span claim or any spectral norm.
- **Claude audit-01** ([audit-01.md](../../../topics/padua-lanczos-drift-20261101/audit-01.md); [checks/audit-01/E3-E4-records-10-15.md](../../../topics/padua-lanczos-drift-20261101/checks/audit-01/E3-E4-records-10-15.md), run 1, script `checks/audit-01/scripts/E34/e4_exact_audit.py`). It is an exact rational reconstruction:
  - 48 sampled rules reproduce (10);
  - θ_2² equals the closed form; δ_X(1)²=(4/3)b²θ_2², which is equality in (8); δ_Y(1)²=b²θ_2²;
  - controls on Q_3, other perturbed columns and the mirror selection.

  Its output was reproduced byte-identically in response-01 (sha256 ad5a798d…).
- **Response-01 checker** `tracks/bivariate-lanczos/code/drift/e4_closure_check.py` (sha256 b22949c6…; exact `fractions.Fraction`; standard library only; 2.9 s). Command: `python3 tracks/bivariate-lanczos/code/drift/e4_closure_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json`. Output: [response-01-e4-closure.json](../../../topics/padua-lanczos-drift-20261101/evidence/response-01-e4-closure.json) (sha256 956dfe71…). On 28 instances it checks:
  - each instance: sampled rules have full rank and span (10); θ² is computed from the projector difference (D⁴=θ²D², tr D²=2θ²) and equals (11); δ_A² is computed from a rank-one Gram matrix and equals κ_A²θ²; κ_A=0 exactly when A S_t⊆V_m; κ_(A_m)²≥b²;
  - for the record-15 instance, also w, r, b², ||[r]||², ||v_21||², V_m=V, the Jq_y identity, (7), (8) with equality and (8'), plus the exact (9) closed forms and thresholds.

  The sampled rules corroborate (b); they do not prove it.
- **Codex audit-02** ([checks/audit-02/E34.md](../../../topics/padua-lanczos-drift-20261101/checks/audit-02/E34.md); [evidence/audit-02-e34-checks.json](../../../topics/padua-lanczos-drift-20261101/evidence/audit-02-e34-checks.json), script `checks/audit-02/E34/independent_exact.py`). An independent SymPy reconstruction (15 cases, 186 rule-and-order checks, complete spectral closure operators) confirmed (a)–(d), the T_3 instance and the qualitative obstruction. Its exact symbolic counterexample (T_3/BJ, source in v_20: δ_X(1)²=672η²/(5(216η²+245)) for the source η·[r]) refuted the response-01 limit equality, now corrected to (13).
- **Response-02 regression checker** `tracks/bivariate-lanczos/code/drift/e4_response02_check.py` (sha256 6b2c0f87…; exact `fractions.Fraction`; standard library only; Python 3.13.18; 2.2 s). Command: `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/e4_response02_check.py --output topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json`. Output: [response-02-e4-creator-limit.json](../../../topics/padua-lanczos-drift-20261101/evidence/response-02-e4-creator-limit.json) (sha256 a6faea99…). It checks (13) on 25 instances. Twenty-three are the distinct measure/selection/column configurations of response-01's 28 instances; its extra source sizes and two general-source variants repeat configurations, and (13) concerns normal sources. The other two are T_3 cases with another normal direction e. For each:
  - δ_A(t)² is computed directly from the projector of the completed span, at five exact source sizes (the output of one non-orthogonal two-pass rule is checked to have that span);
  - (δ_A(t)/u)² equals the closed form exactly, and 1/(δ_A(t)/u)² is affine in u²; its value at u²=0 gives the squared limit (κ_A²/b²)||v_m||²;
  - κ_(A_m)²≥b² in every instance; κ_(A_m)>b in five of them.

  The cases with κ_(A_m)>b include T_3/BJ with the source in v_20: squared limit 88/15 against ||v_20||²=22/5. This case also reproduces audit-02's symbolic formula at every sample size. In the T_3 instance (source in v_21) κ_Y=b; the squared limits are 3/2 for Y and 2 for X, the u→0 values of the closed forms in (9). The checker also confirms the response-01 values of κ_A²/b² and b² on the 23 shared configurations. Its checks corroborate, and do not prove, the lemma.
- **Not evidence.** The original development mentions “a temporary SymPy calculation” of finite rational Gram matrices. It has no recorded command, script, output or hash, and it is **not evidence** for any claim here. The written proof and the recorded checks above replace it.

## Sources

Repository records:

- PD-T055: the heuristic span identity credited above, and the OPEN universal target.
- PD-T053: defect definition and defect–drift context.
- PD-T047/PD-T050: implicit sections and coefficient dependence.
- PD-T054: admissible and staircase selections.
- PD-N013: measured full-reorthogonalization drift. Its part (b) records F-defects ≤1.5e−15 while J-defects grow.

No historical priority is claimed for the quotient argument or the example.

## Proof or evidence

**(a) Independence and full rank.** Let p_k be the polynomial with [p_k]=q_k. Exact Gram–Schmidt gives p_k=c_k·(monomial k)+(earlier monomials), with c_k>0.

Let p(j)=(t,i). Then j=i if A_j=X and j=i+1 if A_j=Y. An earlier degree-t monomial x^(t−i')y^(i'), i'<i, becomes after multiplication a degree-(t+1) monomial with y-exponent i'<j (for x) or i'+1<j (for y). Hence the degree-(t+1) homogeneous parts of a_j p_(p(j)), j=0,…,t+1, are triangular with nonzero diagonal. These polynomials are therefore independent modulo Π_t. By U(t+1), the vectors v_0,…,v_(t+1) are independent modulo S_t, and S_t+span{v_j}=S_(t+1).

Write ṽ_j for the inputs (ṽ_m=v_m+f, ṽ_j=v_j otherwise), and W_j for the span of S_t and the inputs created before j. Suppose ṽ_j=s+Σ c_i ṽ_i with s∈S_t and i ranging over the earlier inputs. Apply I−P_(t+1); only ṽ_m has a nonzero normal part, namely f_⊥.

- If j=m, this gives f_⊥=0.
- Otherwise it gives c_m f_⊥=0 when m is earlier, so c_m=0. Then v_j∈S_t+span{v_i: i≠j}, contradicting independence.

Hence ṽ_j∉W_j.

During the creation of column j the stored span is W_j, so every processed vector equals ṽ_j minus an element of W_j and is nonzero. After the nonzero scaling, the new column q̂_j satisfies span(W_j,q̂_j)=span(W_j,ṽ_j)=W_(j+1), with dimension one larger. After t+2 creations, the N_t+t+2=N_(t+1) stored columns are independent.

**(b) Span (PD-T055's heuristic, exact here).** By the last step of (a), Shat_(t+1)=S_t+span{ṽ_j}=V_m+span{v_m+f}, whatever the coefficients and passes. Here dim V_m=N_(t+1)−1 and w≠0, by the independence in (a). Hence S_(t+1)=V_m⊕span{w} orthogonally.

Write P_(t+1)f=P_(V_m)f+αw, where α=⟨f,w⟩/b² because w⊥V_m and f_⊥⊥w. With v_m=P_(V_m)v_m+w, we get v_m+f∈V_m+g, where g=(1+α)w+f_⊥. Here g⊥V_m, because w⊥V_m and f_⊥⊥S_(t+1)⊇V_m, and g≠0. This proves (10).

**(c) Angle.** P_(t+1)=P_(V_m)+ŵŵ^T and Phat_(t+1)=P_(V_m)+ĝĝ^T, where ĝ=g/||g||. So D=Phat_(t+1)−P_(t+1)=ĝĝ^T−ŵŵ^T acts in the plane span{w,f_⊥} and vanishes on its orthogonal complement. For unit vectors with |⟨ŵ,ĝ⟩|=cos φ, this difference has eigenvalues ±sin φ in that plane.

Here cos φ=|1+α|b/||g|| and ||g||²=(1+α)²b²+||f_⊥||². Hence θ_(t+1)=sin φ=||f_⊥||/||g||, which is (11).

**(d) Defect.** For s∈S_t, As∈S_(t+1)=V_m⊕span{ŵ}, because multiplication by a coordinate raises degree by at most one. So As=P_(V_m)As+⟨As,ŵ⟩ŵ. Since V_m⊆Shat_(t+1),

  (I−Phat_(t+1))As=⟨As,ŵ⟩z,   z=(I−Phat_(t+1))ŵ=ŵ−⟨ŵ,ĝ⟩ĝ,   ||z||=sin φ=θ_(t+1).

A is symmetric, so ⟨AP_tx,ŵ⟩=⟨x,P_tAŵ⟩ for every x∈R^M. Hence

  (I−Phat_(t+1))AP_t=z(P_tAŵ)^T,

a matrix of rank at most one with norm ||z||·||P_tAŵ||=θ_(t+1)κ_A. This proves (12).

κ_A=0 means ⟨As,w⟩=0 for all s∈S_t, which is equivalent to A S_t⊆V_m because A S_t⊆V_m⊕span{w}. Finally, ⟨A_m q_(p(m)),ŵ⟩=⟨v_m,w⟩/b=b, because v_m−w∈V_m⊥w. Since q_(p(m)) is a unit vector in S_t, κ_(A_m)≥b. ∎

**Negative statement.** This follows from (b)–(d). For f=εe with e⊥S_(t+1) and ||e||=1: α=0 and ||f_⊥||=|ε|, so (11) gives θ_(t+1)=|ε|/sqrt(b²+ε²), and (12) gives δ_A(t)=κ_A|ε|/sqrt(b²+ε²). Put ε=u||v_m|| with u>0 and divide by u: this is (13), and its right side tends to (κ_A/b)||v_m|| as u→0.

For A=A_m, (d) gives κ_(A_m)≥b, hence

  δ_(A_m)(t)/u ≥ ||v_m||·b/sqrt(b²+u²||v_m||²) → ||v_m||.

The limit (κ_(A_m)/b)||v_m|| equals ||v_m|| exactly when κ_(A_m)=b. In every case it is positive, so δ_(A_m)(t) is not o(u). ∎

The lower bound alone does not identify the limit. For the source in v_20=Xq_x of the T_3/BJ setting below, A_m=X, ||v_20||²=E[x²(x−1)²]=22/5, b²=7/15 and κ_X²=28/45, so the squared limit is (4/3)(22/5)=88/15.

**T_3 instance: U(3).** (This proof is moved here from PD-N?drift-codex-14.) Let p∈Π_3 vanish on T_3.

1. On y=0 its restriction has degree ≤3 in x and the four roots x=0,1,2,3, so y divides p.
2. On y=1 the quotient has degree ≤2 and the three roots x=0,1,2, so y−1 divides it.
3. Repeating on y=2 (two roots, degree ≤1) and on y=3 (one root, degree 0) forces the factor y(y−1)(y−2)(y−3), of degree four.

Thus p=0. The same argument proves U(m) for T_m. In particular U(2) holds, dim S_2=6<M=10, and T_3 satisfies the lemma's hypotheses at t=1.

T_3 is not a Cartesian product: both marginals contain 0 and 3, and (3,0) and (0,3) are present, but (3,3) is absent. The lemma does not use this fact.

**T_3 instance: prefix and products.** The finite sums give E[x]=E[y]=1, E[x²]=E[y²]=2 and E[xy]=1/2. Therefore [1], q_x and q_y as stated are orthonormal, with positive leading coefficients, and form the exact Gram–Schmidt prefix. Also ||v_21||²=E[y²(x−1)²]=3/2.

Since v_20=[x²−x] and sqrt(3)v_22=[xy+2y²−3y], we have V_m=S_1+span{v_20,v_22}=V. Put

  w=[(11x²+26xy−39x+6y²−26y+18)/23].

One checks w=(I−P_V)v_21, ||w||²=b²=28/115, [r]⊥S_2 and ||[r]||²=72/175. The table lists the column numerators 23w(i,j) and 35r(j):

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

- **w column.** The numerators have dot product zero with each of 1, x, y, x², xy+2y². Their squared sum is 1288, giving 1288/(10·23²)=28/115.
- **r column.** The numerators have dot product zero with 1, x, y, x², xy, y². Their squared sum is 5040, giving 5040/(10·35²)=72/175.
- **Remainder.** (xy−y)−w=−(11/23)x²−(3/23)(xy+2y²)+(39/23)x+(3/23)y−18/23 ∈ V.

These statements prove all the projection assertions without a numerical linear-algebra computation. U(2) gives independence of the five generators of V. Since e⊥S_2, the source has α=0 and ||f_⊥||=|ε|, so (11) gives (7).

**T_3 instance: κ_X and κ_Y.** Direct polynomial arithmetic gives

  Jq_y=Xq_y=(2/sqrt(3))v_21+[(x²−3x+2y)/sqrt(3)],

with the second term in V. Using w⊥V and ⟨v_21,w⟩=b²:

- ⟨X[1],w⟩=⟨[x],w⟩=0, ⟨Xq_x,w⟩=⟨v_20,w⟩=0 and ⟨Xq_y,w⟩=(2/sqrt(3))b². Hence κ_X=(2/sqrt(3))b.
- ⟨Y[1],w⟩=⟨[y],w⟩=0, ⟨Yq_x,w⟩=⟨v_21,w⟩=b² and ⟨Yq_y,w⟩=⟨v_22,w⟩=0. Hence κ_Y=b.

Then (12) gives (8) with equality, and (8').

**T_3 instance: (9).** For ε²=(3/2)u²,

  θ_2²/u²=345/(56+345u²),   δ_X(1)²/u²=112/(56+345u²),   δ_Y(1)²/u²=84/(56+345u²).

These are at least 4, 1 and 1, respectively, if and only if u²≤121/1380, u²≤56/345 and u²≤28/345. All three hold for u²≤1/16, since 1380≤1936, 345≤896 and 345≤448. This proves (9). ∎

**Further exact instances** (checks only; the qualitative conclusions already follow from the lemma). Values are (κ_X²/b², κ_Y²/b²) with a unit-parent b, from response-01-e4-closure.json:

- **T_3, BJ, other perturbed columns.** Source in (2,0)=Xq_x: (4/3, 0), so δ_Y=0. Source in (2,2)=Yq_y: (0, 1).
- **T_3, mirror selection.** Source in (2,1)=Xq_y, formed by X: (1, 3/4). The mirror V_m equals the BJ V, and Xq_y is congruent to (2/sqrt(3))v_21 modulo V. So with the source scaled by the same factor, the span, θ_2, δ_X and δ_Y coincide with the BJ values (the checker's unnormalized prefix has factor 1).
- **Product grid Q_3={0,…,3}², BJ.** Source in (2,1): (1, 1). Sources in (2,0) and (2,2): (1, 0) and (0, 1).
- **T_3 with non-uniform weights ∝ 1+i+2j, BJ.** Source in (2,1): (800/447, 1).
- **T_4, degree 2→3.** Selections XYYY (BJ), XXXY (mirror) and XYXY, with a source in every column: κ_(A_m)²/b²≥1 in all twelve cases. The other operator's ratio ranges from 0 (columns (3,0) and (3,3) in BJ; (3,3) in XXXY and XYXY) to 69/20.
- **General sources and random nodes.** Sources with components along w and in V_m include the case 1+α=0, where θ=1. Twelve random rational nodes with random weights are checked at t=0 and t=1.
- **Relative-source limits (13)** (from response-02-e4-creator-limit.json; ||v_m|| for a unit parent). The forming operator's squared limit exceeds ||v_m||² in the instances with κ_(A_m)>b: T_3/BJ (2,0), ratio 4/3; T_4 XYYY (3,0), ratio 9/5; T_4 XYXY (3,0) and (3,1), ratio 7/4 each. In the other listed instances κ_(A_m)=b, so the squared limit equals ||v_m||².

## Scope

The lemma isolates what fixed parents and fixed products imply. Once the prefix and the current degree's raw products are fixed, reorthogonalization coefficients and passes cannot change their joint span; this is PD-T055's heuristic, exact in this setting. Any source with a normal component therefore leaves a rule-independent angle θ_(t+1) and rule-independent defects δ_A(t)=κ_Aθ_(t+1).

The defect lands on the operator that formed the perturbed column (κ_(A_m)≥b), and on any other operator whose image of S_t meets that column modulo the other columns. Neither non-product support nor an unformed product enters:

- in the T_3 instance the formed operator Y has δ_Y(1)=(sqrt(3)/2)δ_X(1);
- the product grid Q_3 gives δ_X=δ_Y≠0;
- sources in formed X- or Y-columns give defects in X only or in Y only.

So the lemma does not explain the J/F asymmetry recorded in PD-N013(b), where the measured F-defects stay ≤1.5e−15 while the J-defects grow across degrees. A fixed-degree O(u) defect of either operator is consistent with that measurement. The asymmetry concerns amplification across degrees, which lies outside this lemma.

The result is stronger than inspecting one reorthogonalization schedule within R, but substantially weaker than PD-T055's proposed exponential obstruction.

Closure and implicit-section accuracy must remain separate. A normal component of a section residual may give (12) while its projection onto Qhat is much smaller; no large in-span implicit-section error is proved here. Similarly, the source model permits f, but a standard per-operation model may not generate it. There is no claimed evidence about actual deterministic IEEE runs.

## Open items

- An amplification theorem across degrees with controlled χ and well-conditioned references (IDEA?drift-codex-16).
- An adverse-source theorem that allows arbitrary changes of the noiseless prefix gauge.
- Simultaneous sources in several products.
- A verified per-operation generator for an exhibited source.

Parent-repair, reference-basis and extra-product rules lie outside R. They are retained as the deferred candidate IDEA?drift-claude-17 in ideas-e3-e4.md, together with PD-T055's suggested extended-precision parent experiment. In this lemma's setting the prefix is exact, and the two parent repairs defined there leave every exact parent unchanged:

- R17a reorthogonalizes the parent against the stored columns strictly preceding its graded index;
- R17b projects it onto a reference basis of the exact span of the monomials up to and including its index.

So the products, the rule and the conclusions above are unchanged. Projecting the sourced input itself onto S_(t+1) is different: P_(t+1)(v_m+f)=P_(V_m)(v_m+f)+(1+α)w, so the completed span is S_(t+1) when 1+α≠0. That is reference-basis injection at the product, which supplies S_(t+1) itself. Whether a parent repair changes the drift across several degrees is the deferred question.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed; rules 806cc7b4509fd93bae652f9545d32d95529f8281. New explicit quotient-space example. The originally hoped-for all-degree exponential theorem was not obtained and remains OPEN.
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): audit-01 E34-F1. Retitled and rescoped from the T_3/BJ example to a proved general fixed-degree lemma (a)–(d) for any positive measure with U(t+1) and M>N_(t+1), any t≥0, any admissible selection and any single raw-product source with nonzero normal part. The T_3/BJ case is kept as the explicit instance. Provisional ID unchanged. Original title: «A missing J-product cannot be repaired by prior-vector subtractions in a fixed degree»; original alias: «unformed-product closure failure».
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F1. Statement: (8) is now stated as an equality, δ_Y(1)=b|ε|/sqrt(b²+ε²) is added as (8'), and δ_Y(1)≥u is added to (9). Original wording: «Then for **every** rule in this class, its completed degree-two span has θ_2=|ε|/sqrt(b²+ε²) (7) δ_J(1) ≥ (2/sqrt(3)) b|ε|/sqrt(b²+ε²), J=X. (8) Thus full exact reorthogonalization…».
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F1. The “never formed”/“unformed J direction” interpretation and the non-product emphasis are deleted. Original Scope wording: «The result isolates what “the product was never formed” can rigorously mean: once parents and the current degree's raw products are fixed, changing projection coefficients cannot change…» and «A single source in an unformed J direction then creates a J-defect regardless of those coefficients.» Original negative-scope wording: «Attempted mechanism: repair the unformed J-product by choosing additional prior-vector projection coefficients…»; «Parameter range: this explicit non-product measure, degree two, any ε≠0, and every rule satisfying 1–3.»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F2. PD-T055's heuristic span identity is credited in Aliases, Depends on, Sources, Proof (b) and Scope. Original Depends on: «Elementary linear algebra and finite rational sums only. PD-T053 explains the general defect–drift context but is unnecessary for the direct angle calculation.» Original Sources entry: «PD-T055 (OPEN universal obstruction)».
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F3. U(3) for T_3 is proved inline; the dependence on PD-N?drift-codex-14, now withdrawn as a registry vehicle, is removed. Original wording: «Since U(3) holds by PD-N?drift-codex-14's row-factor proof, dim S_2=6<M=10.»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F6. Checks now cite independent-math-01, audit-01 and the new exact checker; the SymPy calculation is marked as non-evidence. Original wording: «The exact expressions were developed using a temporary SymPy calculation of finite rational Gram matrices. … Its durable command/output/hash record is owned by the parent and pending integration; this report is not the required Claude audit.» The Open items now point to IDEA?drift-claude-17 (E34-F9). Original: «Parent repair or extra-product rules require another class and may evade this obstruction.»
- 2026-11-01 (Claude response-02, Claude Opus 5.5 xhigh): audit-02 A02-M1. The Negative statement's relative-source limit is corrected to (13): δ_A(t)/u=κ_A||v_m||/sqrt(b²+u²||v_m||²)→(κ_A/b)||v_m||, with (κ_(A_m)/b)||v_m||≥||v_m|| and equality iff κ_(A_m)=b. It holds with equality in the T_3 instance (v_21, κ_Y=b), but not for the source in v_20 (squared limit 88/15, not 22/5). The no-exact/o(u) conclusion, (a)–(d) and the T_3 instance are unchanged. Original wording: «With a relative size ε=u||v_m||, δ_(A_m)(t)/u→||v_m||>0 as u→0. So no o(u) closure guarantee holds in R for this source model.»
- 2026-11-01 (Claude response-02, Claude Opus 5.5 xhigh): A02-M1. The proof of the Negative statement now derives (13) from (11)–(12) and states the lower bound only as a bound, with the v_20 values. Original wording: «δ_(A_m)(t)≥bθ_(t+1)=u||v_m||·b/sqrt(b²+u²||v_m||²), and the right side divided by u tends to ||v_m||. ∎»
- 2026-11-01 (Claude response-02, Claude Opus 5.5 xhigh): A02-M1. Status paragraph and Negative-statement status row updated for audit-02 and the correction (status PROVED unchanged). Original wording: «The general lemma (a)–(d) was added in Claude response-01 and requires re-audit.»; «| Negative statement: no rule in R removes the drift or the closure defect; no o(u) closure guarantee | PROVED | Immediate from the lemma |».
- 2026-11-01 (Claude response-02, Claude Opus 5.5 xhigh): A02-M1. Checks add the Codex audit-02 reconstruction and the new exact regression checker `e4_response02_check.py` with its evidence; Further exact instances add the relative-source-limit bullet. Additions only; original wording: none replaced.
- 2026-11-01 (Claude response-02, Claude Opus 5.5 xhigh): audit-02 A02-L2. Open items: the parent repairs now defined in IDEA?drift-claude-17 (R17a, R17b) act as the identity on this lemma's exact parents, so they do not evade it. Product-level projection onto S_(t+1) restores the span when 1+α≠0 and is recorded as reference-basis injection. Original wording: «Parent-repair, reference-basis and extra-product rules lie outside R and may evade this obstruction.»
