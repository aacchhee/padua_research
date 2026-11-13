# PD-T?mz-paper-claude-01 — sharp CC endpoint defect, condition-number asymptotics and a uniform hyperinterpolation factor

ID kind: PD-T (provisional; final ID at PR preparation).
Aliases: sharp eta deficit; CC Gram condition number asymptotic; five-thirds hyperinterpolation factor.
Split from: none. It sharpens the open item of PD-T527 ("no limiting leading coefficient") and closes the "eventual dominance" question of the manuscript remark `rem:rate`, using results proved after PD-T527 was written.
Split into: none.

## Statement

Lebesgue Clenshaw–Curtis rule Q_N at x_k=cos(kπ/N), 0≤k≤N, unnormalized dx on [−1,1], natural logarithm. For N≥2 let G_N=G_{N,N−1} be the Gram matrix on Π_{N−1} in an L²(dx)-orthonormal basis, λ_−(N), λ_+(N) its extreme eigenvalues, η_N=‖I−G_N‖_2 and κ_2(G_N)=λ_+(N)/λ_−(N).

(a) For every N≥2 with λ_−(N)≤1/3 one has 1−η_N=λ_−(N). This holds for every N≥57, and

    lim_{N→∞} (log N)² (1−η_N) = π⁴/8.

(b) lim_{N→∞} κ_2(G_N)/(log N)² = 8Λ_edge/π⁴, where Λ_edge is the endpoint constant of PD-T530. In particular the limit lies in [8·1.0044369/π⁴, 12/π⁴] ⊂ [0.08249, 0.12320].

(d) Writing 𝓘_N for interpolation at the N+1 nodes, viewed as a map from nodal data with the CC-weighted ℓ² norm (Σ w_k|u_k|²)^{1/2} to L²(−1,1), one has ‖𝓘_N‖ = λ_−(N,N)^{−1/2}, hence ‖𝓘_N‖/log N → 2√2/π².

(c) For 0≤n≤N−1 the CC hyperinterpolant of PD-T025 (V=2) satisfies, whenever Q_N is exact on Π_k·Π_n with 0≤k≤n,

    ‖f−𝓛_n f‖_{L²(−1,1)} ≤ √2 (1+√B) E_k(f),   B = min{1+ρ_{N,n}, 5/3},  ρ_{N,n}=max{2n/N−1,0}²,

so the uniform factor (1+√2)√2 of the draft improves to (1+√(5/3))√2 < 2.2910·√2. The improvement over 1+ρ_{N,n} is effective only when n/N > (1+√(2/3))/2 = 0.90824….

## Definitions and assumptions

As in PD-T013, PD-T025, PD-T526, PD-T527, PD-T530 and PD-T546. Λ_edge is the variational constant registered in PD-T528 and identified in PD-T530.

## Status by part

Overall status: **PROVED** (developer: Claude; independent check pending, flagged for the Codex audit).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) exact identity when λ_−≤1/3, and the limit π⁴/8 | PROVED | Proof below; independent check pending |
| (b) condition-number limit | PROVED | Proof below; independent check pending |
| (c) hyperinterpolation factor | PROVED | Proof below; independent check pending |
| (d) interpolation-norm form | PROVED | Proof below; added after the review, so its independent check is pending (Codex audit) |

## Depends on

PD-T013 (positivity of weights, exactness on constants, unisolvence), PD-T019 (exact U_{N−1} quotient), PD-T017 (λ_−>0), PD-T025 (general upper-Gram estimate with any admissible B), PD-T022 (B=1+ρ), PD-T526 (λ_+(N)≤5/3 on Π_{N−1}), PD-T527 (identity 1−η_N=min(λ_−,2−λ_+)), PD-T530 (λ_+(N)→Λ_edge), PD-T546 ((log N)²λ_−(N)→π⁴/8), PD-T547 (Λ_edge≥1.0044369; **computer-assisted**). Only the numerical interval in (b) uses PD-T547; without it, PD-T530's [1,3/2] gives the computer-free interval [8/π⁴, 12/π⁴] = [0.08213…, 0.12319…].

## Checks

Analytic, except that the numerical interval in (b) inherits PD-T547's computer-assisted certificate. The N≥57 threshold in (a) was checked in exact rational arithmetic, N=2…399, by the orchestrator (Python Fractions); the proof below covers all N. Written 2026-11-13 by Claude (claude-opus-5-5, configured xhigh) while restructuring the MZ-CC manuscript.

## Sources

None beyond the repository results listed.

## Proof

(a) The extreme eigenvalues determine ‖I−G_N‖_2, so 1−η_N=min{λ_−(N), 2−λ_+(N)} (PD-T527). By PD-T526, 2−λ_+(N)≥1/3 for every N≥2. Hence λ_−(N)≤1/3 implies 1−η_N=λ_−(N). By PD-T019, λ_−(N) ≤ q_N := Q_N(U_{N−1}²)/∫U_{N−1}², with q_N=1/S_N for odd N and q_N=N²/[(N²−1)S_N] for even N, S_N=Σ_{j≤N}1/(2j−1). Exact rational evaluation gives S_57>3, so q_N<1/3 for all odd N≥57, since S_N increases. Also q_58<1/3, and on even N the factor N²/(N²−1) decreases while S_N increases, so q_N<1/3 for all even N≥58. (q_56>1/3, so the U witness alone does not reach lower.) The limit follows from PD-T546.

(d) Positive weights and unisolvence give, for p=𝓘_N u, Σ_k w_k|u_k|² = Q_N(|p|²); hence ‖𝓘_N‖² = sup_{p∈Π_N} ∫|p|²/Q_N(|p|²) = 1/λ_−(N,N). PD-T546 gives (log N)²λ_−(N,N)→π⁴/8, so ‖𝓘_N‖/log N → (8/π⁴)^{1/2} = 2√2/π².

(b) λ_−(N)>0 (PD-T017), so κ_2(G_N)=λ_+(N)/λ_−(N) and κ_2(G_N)/(log N)² = λ_+(N)/[(log N)²λ_−(N)] → Λ_edge/(π⁴/8) by PD-T530 and PD-T546. PD-T547 and PD-T530's Λ_edge≤3/2 give the displayed interval (8·1.0044369/π⁴ = 0.082492…, 12/π⁴ = 0.123192…).

(c) PD-T025 holds for any B with Q(p²)≤B‖p‖² on Π_n. For n≤N−1, restriction of PD-T526 from Π_{N−1} to Π_n gives B=5/3, and PD-T022 gives B=1+ρ_{N,n}; their minimum is admissible. √(5/3)=1.29099…, so 1+√(5/3)<2.2910.

## Scope

(a) gives the sharp leading coefficient of the endpoint MZ defect, which PD-T527 left open, and the explicit range N≥57 for the identity 1−η_N=λ_−(N). No rate of convergence for the limits is given. (b) inherits the open decimal value of Λ_edge (PD-T027 decimal conjunct OPEN). (c) is a constant improvement only.

## History of this record

2026-11-13: (a) onset N≥57, part (d), the computer-assisted note and the (c) threshold were added after the independent check [check-cc-defect-corollary.md](../check-cc-defect-corollary.md) (PASS with corrections). These are changes to a provisional record before audit.

## Open items

Independent check (subagent) and the Codex audit of the MZ paper topic.

## History

2026-11-13: created in topic padua-mz-paper-20261113 (manuscript finalization), as the only new mathematical statement so far; flagged for audit in the topic log.
