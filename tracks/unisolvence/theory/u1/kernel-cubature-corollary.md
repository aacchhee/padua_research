# PD-T003 — A field-valid Lagrange kernel and discrete-product cubature

ID kind: PD-T. Aliases: U1e; monic product-OP kernel; square-root-free checkerboard interpolation.
Split from: none. Split into: none. This is a classical direct corollary, not a novel mechanism.

## Statement and assumptions

Use the exact definitions X,Y,m,N,S_e,w_i,Δ_r of `odd-characteristic-criterion.md`. Assume char(K)≠2 and within-axis distinctness. Then, for every polynomial f of total degree≤2m,

`(L_X⊗L_Y)(f)=2 Σ_((x_i,y_j)∈S_e) w_i(X)w_j(Y) f(x_i,y_j).` (1)

For the interpolation statement assume in addition all required Hankel minors nonzero. Let p_a(t),q_b(t), 0≤a,b≤m, be the monic orthogonal polynomials for L_X,L_Y, and let

`η_a=Δ_(a+1)(X)/Δ_a(X), θ_b=Δ_(b+1)(Y)/Δ_b(Y).`

Every norm displayed is nonzero. For z=(x_i,y_j)∈S_e define

`ℓ_z(s,t)=2w_i(X)w_j(Y) Σ_(a+b≤m) [p_a(s)q_b(t)p_a(x_i)q_b(y_j)/(η_a θ_b)].` (2)

Then ℓ_z∈Π_m and ℓ_z(z′)=1 when z=z′, 0 otherwise, for z′∈S_e. Consequently the unique interpolant of data d_z is Σ_z d_zℓ_z. No square roots or positivity are needed.

## Status / dependencies / scope

Overall status: PROVED (developer proof; supplementary Astra check complete; Claude audit-01 accepted the mathematics).
Depends on: `PD-T001`, exact weighted Gram identity and characteristic≠2 iff. All proof obligations are algebraic; no source theorem is inherited.
Novelty/disposition: known reproducing-kernel argument applied to the established checkerboard factorization; no new mechanism. Closest predecessor is Harris–Simanek's kernel and cubature (reported Thms 1,5 and eq14), with classical Padua analogues. Exact source normalization is not used as a dependency.

## Proof

For each monomial x^a y^b with a+b≤2m, a<m or b<m+1. The ordinary-barycentric product sum is therefore zero by the leading-coefficient Lagrange identity. The full alternation-weighted sum splits into its two parity sums, and their difference is that zero product sum. Thus the parity sums agree and each is half the full sum. This proves (1), without assuming quasi-definiteness.

Under the extra Hankel hypotheses, ordinary monic Gram–Schmidt is defined through degree m on both axes. Its coefficients solve leading Hankel linear systems, and its norms are the displayed nonzero minor ratios. Let Φ(s,t) be the column of p_a(s)q_b(t) for a+b≤m, V its square evaluation matrix on S_e, W=diag(w_i(X)w_j(Y)), and D=diag(η_aθ_b). Formula (1) on products of degree≤m basis functions and univariate orthogonality give V^T W V=D/2. Every diagonal entry of D and W is nonzero, so V is invertible; alternatively the preceding criterion already proves this. Hence 2 V D^(−1) V^T W=I. Its column indexed by z is exactly the evaluation vector of (2), proving the cardinal identities and interpolation claim.

## Checks, limitations and history

The identities are proved directly from the previously checked Gram relation; no distinct computational claim is made here. Independent reconstructions and Claude audit-01 acceptance are recorded in the track AUDIT_LOG. This cubature is for the finite discrete product functional L_X⊗L_Y, not a statement about a continuous Chebyshev measure, positivity, or degree-2m−1 continuous Padua cubature. In characteristic 2 the factor 2 formula is inapplicable; the all-characteristic determinant criterion does not imply that this same kernel normalization survives there.

2026-10-31, Codex `gpt-6.1-sol` xhigh, rules/base d36722823441dc40c6e19d69a174459348dd309c. Round5 retained before derivation, as a direct U1 consequence without activating another direction.

2026-10-31, Codex response-01 A2: updated completed handoff references and Claude audit-01 acceptance metadata only; mathematical statements, proofs and epistemic statuses unchanged.
