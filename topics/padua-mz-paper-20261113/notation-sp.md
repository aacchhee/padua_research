# MZ-SP notation register (task 6; written before the PR #31 integration, per plan-sp F12)

Decisions for the MZ-SP manuscript. Source of conflicts: [review-plan-sp.md](review-plan-sp.md) §(e), the post-split text, and the PR #31 records (S3-*, P1-*). Each rename applies to the text taken from those records. A record keeps its own notation, and the correspondence table maps between the two.

## Global symbols (one meaning each in MZ-SP)

| Symbol | Meaning | Notes / renames from records |
|---|---|---|
| m | Padua construction degree; \|𝒳_m\| = (m+1)(m+2)/2 | used throughout §§2–9; record PD-T534 also uses m |
| n | degree of the polynomial space, 0 ≤ n < m | 𝒫_n = bivariate polynomials of total degree ≤ n (the Gram form lives on 𝒫_n); Π_n = univariate polynomials of degree ≤ n. Both are defined in §1. (The first version of this register listed Π_n as the total-degree space; that was wrong.) |
| N | node index of a CC mesh, N ∈ {m, m+1} only | used only in the CC recap and where a CC mesh appears (including the mesh in the carrier proofs); N_K = 2\|ℐ_K\| and N_𝒵 = \|𝒵\| are subscripted counts of patch nodes |
| 𝒳_m, (x_j, y_k), z | Padua points, generic point z | |
| w_z, w_{jk} | signed Padua weights (interpolatory, mass four) | |
| w_j^{CC}, w_j | CC weights on a mesh N | recap only; "CC" superscript where a Padua weight is nearby |
| λ^P_±(m,n) | extreme Rayleigh quotients of the signed Padua Gram form on Π_n | records write λ±(m,m−1); CC eigenvalues keep λ_±(N,n) (recap) |
| ε^{(N)}_j | endpoint halfweight factor of a Lobatto (Chebyshev–Gauss–Lobatto) mesh with N+1 points: 1/2 at j=0,N, 1 otherwise | replaces ε_j, γ_k, γ_j, η_k of SP, recap and records |
| e_j | the limiting endpoint factor of the weight asymptotics (PD-T295) | kept |
| d_j | distance min(j, N−j) to the mesh end | replaces e_k=min(k,M−k) of PD-T534/536; MZ-CC's floor index m_j is written 1+d_j |
| B | the compact selfadjoint corner operator on L²(T, ab da db) (PD-T536) | never used for a Gram bound in MZ-SP |
| B_K | its truncation | |
| c_± | inf σ(B), sup σ(B) (sharp normalized limits) | only these |
| κ^{car}_±, κ_new | carrier constants: κ^{car}_− = 1/[9·4 log 2·J_−(1/4)], κ^{car}_+ = 1/[36·4 log 2·J_+(1/8)], κ_new = c_new of PD-T533 | replaces c±^{(379)}, c_new; the corollary reads ‖B‖ ≥ κ_new |
| J_±(a) | the carrier integrals of PD-T379/533/537 | kept; the rectangle integrals become 𝒥_t |
| 𝒥_t(U,V) | rectangle integrals of PD-T541 (t = 0, 1, …) | replaces J_t; avoids Bessel J₀ |
| J₀ | Bessel function of order zero (PD-T535 kernel) | only meaning |
| **K**(k) | complete elliptic integral of the first kind (PD-T539) | bold K |
| 𝒦_{m−1} | reproducing kernel of Π_{m−1} | replaces K_{m−1} |
| K | truncation index in B_K | only meaning |
| ϱ | Abel parameter (PD-T539) | replaces ρ there |
| ρ_{jk} | the auxiliary weights of PD-T297 | the only plain ρ |
| δ_θ | angular mesh width (PD-T541) | replaces ρ there |
| ω_a(t) | arcsine density | replaces w_a(t) |
| δ_m(x,y) | the integrated cardinal density of Lemma 4.1 | replaces d_m (clash with d_j) |
| 𝖼_a | 1 for a = 0, 2 for a > 0 (§4, App. A) | replaces c_a (c_± only) |
| Ξ_R | the tail Σ_{a>R} t_a cos(2at) | replaces T_R (clash with Chebyshev T_a) |
| t̂, ŝ | min(t,π−t), min(s,π−s) in Lemma A.1 | replaces τ, σ there |
| 𝓔_K(m) | the finite-comparison error of Remark 6.4 | replaces E_K(m) (clash with E_k(f), best approximation) |
| Φ_t(a;[u,v]) | the rectangle functions of PD-T541 | replaces I_t; ℐ_K is the index set |
| μ_𝒯 | the measure ab da db on 𝒯 | the plain μ is the generic measure of §§1–2 |
| ν_Ch | the Chebyshev measure of Thm 7.1 | ν_± are the extremes of L_m[p]/\|p\|² |
| r̲, r̄ | the enclosure endpoints of Prop. 6.9 (bounds for r = \|B\|) | replace L, U |
| w̃_{jk}, Q̃_m, G̃_{m,n} | an arbitrary rule exact on 𝒫_m (§3) | the plain w_{jk}, Q^P_m, G^P_{m,n} are the interpolatory rule |
| 𝒬(r,s) | Q^P_m(T_r(x)T_s(y)) in the proof of Prop. 8.1 | replaces ϱ(r,s) |
| 𝖬, 𝖬^P | matrices of ∫p² and Q^P_m(p²) in the proof of Prop. 8.1 | replace H, Q there |
| f₀ | the positive eigenfunction of Prop. 6.7 | replaces u |
| Y₁, Y₂ | psd matrices in the square-root bound of Lemma A.4 | replace A, B (X_m, X_∞ are in the same lemma) |
| υ(x), Δ⁴υ(q) | υ(x) = x² log\|x\| (Lemma 5.5) and its fourth difference C(q) of PD-T537 | replaces h(x), C(q); h_a is kept for the Chebyshev moments ∫T_a |
| C₀ | (1+π⁴)/2 of the density estimate, if it survives integration | the only C₀; other constants get local names |
| ι | the coordinate isometry of Thm 3.1 (PD-T021) | replaces J |
| τ | degree ratio n/m in the threshold corollary | replaces θ as ratio; θ, θ_j are angles only |
| M | m+1 only | PD-T297's 2R+1 becomes M′; Schur row bounds Γ_r, Γ_c |
| X, Y | the positive matrices of PD-T536 §5 | replaces A, B there |
| B⁻ | −B (PD-T540's A) | |
| 4 log 2 | written explicitly | the record's A is not used |

## Locally reused letters (allowed only inside one proof)

κ, ν, g, U, L, S, D, d (other than d_j), H, Q, P, V, σ, r, T, E, I: each may appear inside a single proof with a meaning defined there. η is not in this list: η = ‖I−G‖₂ is the global defect (eq:eta) and η_τ is a uniform strong MZ constant (§1, Cor. 5.3). In the final text g is the Fejér profile of Lemma 5.5 (global in §5) and the Thm 7.1 function is 𝔤; κ₀ = ½ + 1/π replaces κ in Thm 7.1; the CC weights of App. A.1 are w^{CC}_{m,j}, w^{CC}_{M,k}. The integration step checks that no two such meanings occur within one section. The final consistency pass (task 6) lists any that remain.

## Cross-paper conventions

- MZ-SP cites MZ-CC by statement label after the MZ-CC freeze (AC: MZ-CC first). The recap uses MZ-CC's notation λ_±(N,n), w_j, W_N(θ) (bracket), K_N, with the "CC" superscript where needed.
- Natural logarithm throughout.

## Status

Decisions written 2026-11-13 before the PR #31 integration. The register is rechecked against the final text in task 6.

Update 2026-11-14 (internal referee round, response-internal-sp.md): the two wrong entries above (Π_n as the total-degree space; η as a locally reusable letter) are corrected, the renames in the added rows are applied in the text, and the following remain as accepted local reuses: U (cube size, rectangles U×V, U_−), r (‖B‖ and local indices), S, c (c_t, c_l, c_{jk}, corner c), P, F (Fejér F_r, F(a,b), F_a), σ (spectrum and σ_s), H (H_{m,n}, H_q), and the Appendix lemma and subsection numbers A.1, A.2, B.1, B.2 (always cited with the noun Lemma or Appendix).
