<a id="pd-tlanczos-nonproduct-codex-p5-02--padua-bj-and-mirror-capacity-is-polynomial"></a>

# PD-T486 — Padua BJ and mirror capacity is polynomial

Provisional alias: `PD-T?lanczos-nonproduct-codex-p5-02`.

ID kind: PD-T.
Aliases: Chebyshev impulse upper; top-x normal witness; unsaturated Padua
aggregate drift bound; polynomial BJ/best ratio.
Split from: prescribed P5 capacity target.
Split into: admission/cubature hypotheses in PD-T485; arbitrary-rule upper
target remains separate and OPEN in the candidate record.

## Statement

For every pair of integers m>=2 and 1<=s<m, take the exact positive Padua
probability measure ν_m and weighted Euclidean representation of PD-T485.
Order (a,b) by increasing a+b and then increasing b. For either fixed rule

- BJ: choose X from (a-1,0) for b=0; choose Y from (a,b-1) for b>0;
- mirror: choose X from (a-1,b) for a>0; choose Y from (0,b-1) for a=0,

start from the exact constant vector and create each subsequent column by
forming A_h q_parent(h)(ε)+ε f_h, projecting exactly against all prior
perturbed columns, and normalizing with positive residual norm. Define
σ_h=||A_h q_parent(h)(0)||_2 and the relative aggregate source norm

    ||f||_src²=sum_(h≠0) ||f_h||_2²/σ_h².

Let P_s be the exact weighted polynomial projector and P_s(ε;f) the
perturbed first-N_s-column projector. In the same normalized weighted
aggregate model and spectral output as PD-T324, put

    κ_R(s;m)=sup_(||f||_src=1) lim_(ε→0+)
                       ||(I-P_s)P_s(ε;f)||_2 / ε.

Then both rules satisfy the all-degree bounds

    sqrt(ceil(s/2)) <= κ_R(s;m)
                    <= 2sqrt(2)(s+1)(N_s-1).              (1)

Thus along every admitted sequence m(s)>s these capacities are unbounded
but bounded by a fixed polynomial in s, independent of m. In particular
BJ has no exponential aggregate-capacity growth on this Padua family.
No matching polynomial exponent is asserted.

For every fixed admissible parent rule R', κ_R'(s;m)>=1. Consequently, for
any nonempty finite collection of such rules (which may include
alternating and frozen pivot choices), κ_best=min_R' κ_R' satisfies

    κ_BJ/κ_best <= 2sqrt(2)(s+1)(N_s-1).                  (2)

This upper on a BJ/best ratio does not upper-bound the other rules'
capacities or differentiate through adaptive switching.

## Definitions

Weighted polynomial vectors, X,Y,N_s and q_ab=p_a(x)p_b(y) are as in
PD-T485. All sources are arbitrary represented vectors in R^M, with no
polynomial restriction. All nonconstant source positions through s are
included. Matrix output uses the spectral norm. The two rules use their
own exact σ_h, in the identical relative-raw-product convention.

## Assumptions

Exact real coordinate operators; exact full projection and normalization;
unperturbed start; frozen admissible parents; fixed m,s,f when ε tends to
zero. M=N_m>N_s, so the normal space is nonzero. No scalar-operation,
actual IEEE, random-source, finite-ε uniformity or closure-defect claim.

## Status by part

Overall status: PROVED (complete written analytic argument).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Two-sided polynomial capacity bounds for BJ and mirror | PROVED | Explicit all-source upper and legal normal lower below |
| Minor consequence: universal capacity floor and BJ/best ratio upper | PROVED | Last-column source below; no all-rule upper inferred |

Candidate disposition: retained variant IDEA-582.
The supporting product-factorization mechanism is inherited from
PD-T033/039; the explicit quotient/source bound and non-product admission
are the present application. No historical novelty assertion.

## Depends on

PD-T485, at its exact unsaturated cubature and orthonormal-basis scope.
The normalized weighted quotient calculation is rederived below rather
than applying uniform monic PD-T136 outside its hypotheses. PD-T324 fixes
the comparison model only; its exponential result is not a proof premise.

## Checks

Supplementary exact m=2..5 cases passed:60 creators for BJ/mirror,20 pure-x
readout squares,44 symbolic Chebyshev identities, and124 full-projection
versus frozen normal-derivative coordinate directions at m=2,3. The latter
is a finite monic-gauge corroboration with explicit base norms, not an
independent derivation of the normalized source model. See
[attempts/P5](../attempts/P5.md) and
[exact receipt](../evidence/p5-exact-checks.json). The theorem is analytic,
not a finite computer proof. Distinct reconstruction/rerun is
coordinator-owned.

## Sources

No external theorem used. Chebyshev identities and projector facts are
proved explicitly. See the prospective gate for predecessor/source scope.

## Proof

Write β_1=1/sqrt(2), β_l=1/2 for l>=2 and β_0=0. At the exact base the
chosen creator of (a,b) has residual β_a q_ab for an X parent or β_b q_ab
for a Y parent. All β are positive. Thus the perturbed algorithm is smooth
near zero, for each fixed source array, by finite induction through the
projection denominators and residual norms.

If β_h q_h=A_h q_parent-sum_(l<h)c_hl q_l is an exact creator, define

    β_h V_h=A_h V_parent-sum_(l<h)c_hl V_l+f_h, V_0=0.    (3)

Differentiating the perturbed recursion adds to (3) only derivatives of
its scalar coefficients multiplying base polynomial vectors, including
the derivative of its normalization times q_h. Inductively the difference
dot(q_h)-V_h is a polynomial vector of degree <=deg(h): multiplication
raises the parent's degree by one and all subtracted base/earlier vectors
have degree <=deg(h). Hence

    (I-P_s)dot(Q_s)=(I-P_s)[V_h]_(deg(h)<=s).              (4)

Since Q_s(ε) is orthonormal, ||(I-P_s)P_s(ε)||_2 equals
||(I-P_s)Q_s(ε)||_2. Taylor expansion and (4) show that the limit defining
κ_R is ||(I-P_s)[V_h]||_2. This establishes the weighted normalized source
and output scaling directly.

For a univariate Chebyshev chain started at zero, an injection f at index
c>=1 has response at index a>=c equal to K_ac(X)f, where

    K_a1(z)=sqrt(2) U_(a-1)(z),
    K_ac(z)=2 U_(a-c)(z) for c>=2.                        (5)

Here U_0=1,U_1=2z,U_(l+1)=2zU_l-U_(l-1). Formula (5) follows immediately
at the injection and subsequent indices from (3); beyond the first pivot
all β equal1/2. A chain with initial vector v at index0 and no injections
has response p_a(X)v, by the same three-term relation.

For BJ, (3) therefore has the complete solution

    V_a0=sum_(c=1)^a K_ac(X) f_c0,
    V_ab=p_b(Y)V_a0+sum_(d=1)^b K_bd(Y)f_ad (b>=1).       (6)

Every source appears at most once in an individual output. For mirror the
formula swaps the roles of a/X and b/Y, starting on the y axis and then
propagating horizontally. These are exact formulas for the frozen normal
response, not formulas for perturbed coefficients or finite errors.

At every node, |p_b(y)|<=sqrt(2), and |U_l(z)|<=l+1 on [-1,1]. For the
latter bound write z=cosθ and use the finite sum
U_l(cosθ)=exp(ilθ)+exp(i(l-2)θ)+...+exp(-ilθ), with endpoints by continuity.
Consequently every individual source coefficient operator in (6), and in
the mirror formula, has norm at most C_s=2sqrt(2)(s+1). Also σ_h<=1,
because ||X||_2,||Y||_2<=1 and all exact parents have norm one.
Put H=N_s-1 and u_h=f_h/σ_h. On the unit source sphere,

    ||V_ab|| <= C_s sum_h σ_h||u_h|| <= C_s sqrt(H).

There are H nonconstant output columns. Spectral norm <= Frobenius norm
and orthogonal projection is a contraction, giving

    ||(I-P_s)[V_h]||_2 <= ||[V_h]||_F <= C_s H.

This is the upper in (1), uniformly over all source positions and vectors.

For the lower let e_m be the weighted evaluation vector of T_m(x).
At x_j, T_m(x_j)=(-1)^j, so ||e_m||_2²=ν_m(1)=1. For any p∈Pi_s,
the product T_m(x)p has total degree <=m+s<=2m-1. By cubature its ν_m
integral equals its μ integral, which is zero by univariate Chebyshev
orthogonality and s<m. Thus e_m is normal to S_s.

Use only the source at h=(1,0), taking f_10=e_m/sqrt(2). Both rules use
the X parent there; σ_10²=ν_m(x²)=1/2. Therefore this source has exactly
unit budget. The pure x-axis output columns, shared by both rules, obey

    V_a0=U_(a-1)(X)e_m, 1<=a<=s.                         (7)

Their scalar components along e_m are

    e_m^T V_a0 = ν_m(T_m(x)² U_(a-1)(x))
               = ν_m(U_(a-1)(x))
               = 1 for a odd, and 0 for a even.           (8)

The middle equality is the nodal identity T_m²=1. The final equality uses
the degree a-1 cubature and the elementary expansions

    U_(2r)=1+2(T_2+T_4+...+T_(2r)),
    U_(2r-1)=2(T_1+T_3+...+T_(2r-1)).

These expansions follow from the same exponential sum used above. As e_m
is unit and normal, left multiplication of (I-P_s)[V_h] by e_m^T cannot
increase its spectral norm. Its row restricted to the x-axis columns has
ceil(s/2) entries equal to one. Its Euclidean norm is sqrt(ceil(s/2)),
proving the lower. The argument does not infer normal survival from raw
growth: (8) is an explicit surviving normal readout.

Finally consider any fixed admissible rule. Inject only into its last
column a unit-budget source f_last=σ_last e_m. Earlier V vanish, so the
last output is σ_last e_m/β_last. The exact raw product has an orthogonal
target component β_last q_last, whence σ_last>=β_last>0. Its normal
spectral output is at least one. Thus every such rule has capacity>=1,
and dividing the proved BJ upper by this floor proves (2).

## Scope

The bounds hold for all m>s, including m=s+1 arbitrarily close to square
saturation, on a genuinely non-affine-product measure. They classify BJ
and mirror as unbounded with polynomial upper growth. They do not prove
a precise exponent, bounded BJ/mirror ratio, an all-rule polynomial upper,
or any failure of actual floating-point computation. They do rule out an
exponential BJ/best capacity ratio under the stated finite-rule model.

## Open items

Sharp polynomial orders; alternating and frozen-pivot capacity upper
bounds; adaptive switching beyond fixed branches. Required distinct
mathematical reconstruction is coordinated separately. No further bulk
Padua scan is needed to establish this analytic classification.

## History

2026-11-05: Codex `/root/p5_padua`, assigned gpt-6.1-sol xhigh; rules/input
`cafb74ab6f7738c8af83d0cd0f518b81af16f253`. Prospective gate and candidate
saved before new derivation. Bounds sent to coordinator before the exact
supplementary execution. No finite-sample trend is used in the proof.
