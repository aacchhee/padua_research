# PD-T136 — First-order span derivative is the normal quotient of the frozen recurrence

Provisional alias: `PD-T?drift-codex-01`. Final ID assigned at PR preparation, 2026-11-01 (handoff 11, after Codex audit-04 acceptance).

ID kind: PD-T.
Aliases: residual-to-span derivative; polynomial coefficient errors vanish in the normal quotient; rational orthogonal gauge.
Split from: E1's combined sensitivity-and-separation target (the latter remains OPEN).
Split into: none.

## Statement

Let distinct real nodes carry the uniform positive measure, let evaluation on polynomials of degree at most n be injective, and order monomials as (t,j) = x^(t-j)y^j, first by t and then by increasing j. Every nonconstant column k chooses one admissible coordinate A_k in {X,Y} and its degree-one-lower parent p(k). Fix these choices throughout the perturbation.

Put b_0 = 1 and, in exact arithmetic,

    z_k = A_k b_p,
    alpha_kl = (b_l^T z_k)/d_l,  l<k,
    b_k = z_k - sum_{l<k} alpha_kl b_l,
    d_k = b_k^T b_k.

For arbitrary real vectors f_k, define b_k(epsilon) recursively by replacing z_k with A_k b_p(epsilon)+epsilon f_k and orthogonally projecting against all preceding perturbed columns. The projection uses the exact Euclidean inner product and includes every preceding column. Keep b_0(epsilon)=b_0. For N_s=(s+1)(s+2)/2, put B_s=[b_0,...,b_(N_s-1)], D_s=diag(d_0,...,d_(N_s-1)), P_s=B_s D_s^(-1) B_s^T and R_s=I-P_s. Define scalar responses

    g_kh(z)=0 (k<h),  g_hh(z)=1,
    g_kh(z)=a_k(z)g_p(k),h(z)-sum_{l<k}alpha_kl g_lh(z) (k>h),

where a_k is the chosen x or y coordinate. Set

    V_0=0,  V_k=sum_{h=1}^k diag(g_kh(z_i)) f_h,
    T_s(f)=R_s [V_0,...,V_(N_s-1)] D_s^(-1/2).

Then, for s <= n, the largest principal-angle sine theta_s(epsilon)=||(I-P_s)P_s(epsilon)||_2 satisfies

    theta_s(epsilon)=|epsilon| ||T_s(f)||_2 + O(epsilon^2).

The remainder is for fixed nodes, fixed choices and fixed f as epsilon tends to zero. This is a derivative identity, with no uniform remainder claim in n or f. Every alpha, b, d, P and g value is rational when the nodes are rational. D_s^(-1/2) is used only to state the output norm; it need not be constructed for the rational certificates in PD-T137.

## Definitions

S_s is the evaluation space of all polynomials of total degree at most s. The exact P_s projects onto S_s. The perturbed P_s(epsilon) projects onto the span of the first N_s perturbed columns. Uniform weights permit the Euclidean convention without square-root weights. A common positive weight changes none of the spaces.

The perturbations are aggregate residual injections immediately before exact full orthogonalization. They are not independent scalar-operation rounding errors. The fixed-choice derivative for a pivot rule is the derivative of the choices frozen at the unperturbed data; differentiation through a tie or a choice change is outside the statement.

## Assumptions

Real diagonal coordinate operators; injectivity through degree n; fixed admissible parent choices; exact full orthogonal projection; no starting-vector perturbation. Injectivity ensures every d_k is positive and the perturbed recursion exists in a neighborhood of zero.

## Status by part

Overall status: PROVED (written analytic proof; Claude audit-01: CONFIRMED, editorial correction applied in response-01; Codex re-audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Normal derivative and angle expansion | PROVED | Proof below; no computer proof dependency |

Candidate / claim disposition: retained as an analytic reduction. E1's comparison and any rounding theorem remain separate unresolved claims.

## Depends on

No inherited scientific theorem is required. The exact graded-basis convention agrees with PD-T029. PD-T041 supplies the predecessor frozen impulse recurrence, without its projection onto the span quotient.

## Checks

Code implementation and finite-difference checks are supplementary and recorded in E1.md. No computer-assisted proof or independent rerun is asserted by this analytic file. Source/rules read at cf89b140530d5838bdb208a8c28f3e7aa676ace3; synchronized parent base 806cc7b4509fd93bae652f9545d32d95529f8281 has unchanged Lanczos definitions.

## Sources

No new external source consulted. The documented L2 prior-art review relates span accuracy to Krylov-subspace conditioning and separates it from fit/orthogonality bounds. No historical novelty claim is made here.

## Proof or evidence

First observe inductively that b_k is the evaluation of a monic polynomial with leading monomial x^(t-j)y^j and otherwise earlier monomials. Multiplication of an earlier monomial in a parent by its selected coordinate produces a monomial preceding or equal to the target. Subtracting earlier b_l preserves that triangular leading term. Injectivity therefore makes the vectors independent, and their span through any complete degree is S_s. This also shows that the exact monic b_k, although not necessarily the coefficients alpha_kl, is independent of the admissible parent choice: it is the unique monic polynomial with the stated triangular support orthogonal to all earlier monomials.

All perturbed projection coefficients are differentiable near zero because their denominators are nonzero there. Write a dot for derivative at zero. Differentiating the recursion gives

    dot b_k = A_k dot b_p - sum_l alpha_kl dot b_l + f_k
              - sum_l dot alpha_kl b_l.

The frozen response satisfies V_k=A_k V_p-sum_l alpha_kl V_l+f_k, by substitution of the scalar g recursion, including g_kk=1. Hence E_k=dot b_k-V_k satisfies

    E_0=0,
    E_k=A_k E_p-sum_l alpha_kl E_l-sum_l dot alpha_kl b_l.

Induct on k. E_p is a polynomial evaluation vector of degree at most deg p, so A_k E_p has degree at most deg k. Every earlier E_l and b_l has degree at most deg k. Therefore E_k belongs to S_(deg k). In particular R_s E_k=0 for every k<N_s, and R_s dot B_s=R_s[V_0,...,V_(N_s-1)]. This is the step missing from a raw inverse-recurrence growth certificate: polynomial coefficient-derivative terms can be large, but they contribute zero to this normal quotient.

For completeness, put Q=B_s D_s^(-1/2), so Q^T Q=I. The perturbed columns C(epsilon)=B_s(epsilon)D_s^(-1/2) have the same span as B_s(epsilon). Their tangential coordinates Q^T C(epsilon)=I+O(epsilon) are invertible near zero. Thus their span is the graph over ran Q of

    Z(epsilon)=R_s C(epsilon)(Q^T C(epsilon))^(-1)
              =epsilon R_s dot B_s D_s^(-1/2)+O(epsilon^2).

For a graph with tangent matrix Z orthogonal to ran Q, the largest principal-angle sine is ||Z||_2/sqrt(1+||Z||_2^2). This follows directly by normalizing graph vectors (Qv+Zv) and maximizing the quotient ||Zv||/sqrt(||v||^2+||Zv||^2). The derivative identity and the stated angle expansion follow.

Finally, rational data remain rational under addition, multiplication and division by the positive rational d_l. This proves the rationality claim.

## Scope

This computes span sensitivity under exact full orthogonalization even for choices violating staircase condition (C); it does not use implicit-section completion or PD-T050's acyclicity hypotheses. It does not claim that arbitrary reorthogonalization rules have this derivative, that a large derivative is activated by actual rounding, or that every error realization produces nonzero drift. Ordinary normalization of each perturbed column changes its scale, not the space; under that gauge the first-order normalized injection is f_k/||b_p||.

## Open items

Finite exact separation of BJ and good selections; an independently verified scalar-operation generator map; uniform finite-epsilon remainder bounds; all-degree explicit-family growth.

## History

- 2026-11-01: Codex mathematics developer; requested gpt-6.1-sol xhigh allocation, runtime variant/effort not independently exposed. Written as a substantive split from E1 before sensitivity computations. No final ID allocated.
- 2026-11-01 (Claude response-01, Sonnet 5.5): E1-F9: added "for s <= n" to the Statement (the stage s of the angle expansion must not exceed the injectivity degree n; the proof already used s <= n); original wording: «Then the largest principal-angle sine theta_s(epsilon)=||(I-P_s)P_s(epsilon)||_2 satisfies»
- 2026-11-01 (Claude response-01, Sonnet 5.5): status line updated for audit-01 (status PROVED unchanged); original wording: «Overall status: PROVED (written analytic proof; independent audit pending).»
