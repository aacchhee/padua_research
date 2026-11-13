# MZ-SP notation register (task 6; written before the PR #31 integration, per plan-sp F12)

Decisions for the MZ-SP manuscript. Source of conflicts: [review-plan-sp.md](review-plan-sp.md) §(e), the post-split text, and the PR #31 records (S3-*, P1-*). Each rename applies to the text taken from those records. A record keeps its own notation, and the correspondence table maps between the two.

## Global symbols (one meaning each in MZ-SP)

| Symbol | Meaning | Notes / renames from records |
|---|---|---|
| m | Padua construction degree; \|𝒳_m\| = (m+1)(m+2)/2 | used throughout §§2–9; record PD-T534 also uses m |
| n | total degree of the polynomial space Π_n, 0 ≤ n < m | |
| N | node index of a CC mesh, N ∈ {m, m+1} only | used only in the CC recap and where a tensor CC grid appears |
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
| Δ⁴h(q) | the fourth difference C(q) of PD-T537 | replaces C(q) |
| C₀ | (1+π⁴)/2 of the density estimate, if it survives integration | the only C₀; other constants get local names |
| ι | the coordinate isometry of Thm 3.1 (PD-T021) | replaces J |
| τ | degree ratio n/m in the threshold corollary | replaces θ as ratio; θ, θ_j are angles only |
| M | m+1 only | PD-T297's 2R+1 becomes M′; Schur row bounds Γ_r, Γ_c |
| X, Y | the positive matrices of PD-T536 §5 | replaces A, B there |
| B⁻ | −B (PD-T540's A) | |
| 4 log 2 | written explicitly | the record's A is not used |

## Locally reused letters (allowed only inside one proof)

η, κ, ν, g, h, U, L, S, D, d (other than d_j), H, Q, P, V, σ, r, T, E, I: each may appear inside a single proof with a meaning defined there. The integration step checks that no two such meanings occur within one section. The final consistency pass (task 6) lists any that remain.

## Cross-paper conventions

- MZ-SP cites MZ-CC by statement label after the MZ-CC freeze (AC: MZ-CC first). The recap uses MZ-CC's notation λ_±(N,n), w_j, W_N(θ) (bracket), K_N, with the "CC" superscript where needed.
- Natural logarithm throughout.

## Status

Decisions written 2026-11-13 before the PR #31 integration. The register is rechecked against the final text in task 6.
