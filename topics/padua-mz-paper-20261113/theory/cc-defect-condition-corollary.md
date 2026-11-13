# PD-T?mz-paper-claude-01 — sharp CC endpoint defect, condition-number asymptotics and a uniform hyperinterpolation factor

ID kind: PD-T (provisional; final ID at PR preparation).
Aliases: sharp eta deficit; CC Gram condition number asymptotic; five-thirds hyperinterpolation factor.
Split from: none. It sharpens the open item of PD-T527 ("no limiting leading coefficient") and closes the "eventual dominance" question of the manuscript remark `rem:rate`, using results proved after PD-T527 was written.
Split into: none.

## Statement

Lebesgue Clenshaw–Curtis rule Q_N at x_k=cos(kπ/N), 0≤k≤N, unnormalized dx on [−1,1], natural logarithm. For N≥2 let G_N=G_{N,N−1} be the Gram matrix on Π_{N−1} in an L²(dx)-orthonormal basis, λ_−(N), λ_+(N) its extreme eigenvalues, η_N=‖I−G_N‖_2 and κ_2(G_N)=λ_+(N)/λ_−(N).

(a) For every N≥2 with λ_−(N)≤1/3 one has 1−η_N=λ_−(N). This holds for all sufficiently large N, and

    lim_{N→∞} (log N)² (1−η_N) = π⁴/8.

(b) lim_{N→∞} κ_2(G_N)/(log N)² = 8Λ_edge/π⁴, where Λ_edge is the endpoint constant of PD-T530. In particular the limit lies in [8·1.0044369/π⁴, 12/π⁴] ⊂ [0.08249, 0.12320].

(c) For 0≤n≤N−1 the CC hyperinterpolant of PD-T025 (V=2) satisfies, whenever Q_N is exact on Π_k·Π_n with 0≤k≤n,

    ‖f−𝓛_n f‖_{L²(−1,1)} ≤ √2 (1+√B) E_k(f),   B = min{1+ρ_{N,n}, 5/3},  ρ_{N,n}=max{2n/N−1,0}²,

so the uniform factor (1+√2)√2 of the draft improves to (1+√(5/3))√2 < 2.2910·√2.

## Definitions and assumptions

As in PD-T013, PD-T025, PD-T526, PD-T527, PD-T530 and PD-T546. Λ_edge is the variational constant registered in PD-T528 and identified in PD-T530.

## Status by part

Overall status: **PROVED** (developer: Claude; independent check pending, flagged for the Codex audit).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) exact identity when λ_−≤1/3, and the limit π⁴/8 | PROVED | Proof below; independent check pending |
| (b) condition-number limit | PROVED | Proof below; independent check pending |
| (c) hyperinterpolation factor | PROVED | Proof below; independent check pending |

## Depends on

PD-T013 (positivity of weights, exactness on constants), PD-T017 (λ_−>0), PD-T025 (general upper-Gram estimate with any admissible B), PD-T022 (B=1+ρ), PD-T526 (λ_+(N)≤5/3 on Π_{N−1}), PD-T527 (identity 1−η_N=min(λ_−,2−λ_+)), PD-T530 (λ_+(N)→Λ_edge), PD-T546 ((log N)²λ_−(N)→π⁴/8), PD-T547 (Λ_edge≥1.0044369). No numerical input.

## Checks

Analytic; no computation. Written 2026-11-13 by Claude (claude-opus-5-5, configured xhigh) while restructuring the MZ-CC manuscript.

## Sources

None beyond the repository results listed.

## Proof

(a) The extreme eigenvalues determine ‖I−G_N‖_2, so 1−η_N=min{λ_−(N), 2−λ_+(N)} (PD-T527). By PD-T526, 2−λ_+(N)≥1/3 for every N≥2. Hence λ_−(N)≤1/3 implies 1−η_N=λ_−(N). By PD-T546, λ_−(N)→0, so this holds for all large N, and the limit follows from PD-T546.

(b) λ_−(N)>0 (PD-T017), so κ_2(G_N)=λ_+(N)/λ_−(N) and κ_2(G_N)/(log N)² = λ_+(N)/[(log N)²λ_−(N)] → Λ_edge/(π⁴/8) by PD-T530 and PD-T546. PD-T547 and PD-T530's Λ_edge≤3/2 give the displayed interval (8·1.0044369/π⁴ = 0.082492…, 12/π⁴ = 0.123192…).

(c) PD-T025 holds for any B with Q(p²)≤B‖p‖² on Π_n. For n≤N−1, restriction of PD-T526 from Π_{N−1} to Π_n gives B=5/3, and PD-T022 gives B=1+ρ_{N,n}; their minimum is admissible. √(5/3)=1.29099…, so 1+√(5/3)<2.2910.

## Scope

(a) gives the sharp leading coefficient of the endpoint MZ defect, which PD-T527 left open; it does not give an effective N beyond which 1−η_N=λ_−(N) other than through the explicit PD-T018 bound (λ_−≤128000/(log N)²≤1/3 once log N≥√384000≈619.7). (b) inherits the open decimal value of Λ_edge (PD-T027 decimal conjunct OPEN). (c) is a constant improvement only.

## Open items

Independent check (subagent) and the Codex audit of the MZ paper topic.

## History

2026-11-13: created in topic padua-mz-paper-20261113 (manuscript finalization), as the only new mathematical statement so far; flagged for audit in the topic log.
