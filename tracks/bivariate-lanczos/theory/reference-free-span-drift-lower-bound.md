# PD-T?bivariate-lanczos-claude-208 — Reference-free span-drift lower bound: for any computed nested spans Ŝ_s and the exact graded spaces S_s, ‖(I − Π̂_{s+1})AΠ̂_s‖₂ ≤ ‖A‖₂(θ_s + θ_{s+1}) for A ∈ {X, Y}; hence max(θ_s, θ_{s+1}) ≥ δ_A(s)/(2‖A‖₂), and θ_LB(n) bounds max_{s≤n} θ_s (not θ_n alone)

ID kind: PD-T.
Aliases: drift lower bound θ ≥ δ_J/(2‖J‖); θ_LB; reference-free drift certificate; J-defect/Y-defect bound; former PD-T?…-202 part 5; former second sentence of PD-T?…-205 part 4; "max-over-stages bound".
Split from: (1) PD-T?bivariate-lanczos-claude-202 part 5, exact claim: "5. **(Drift lower bound.)** [EXACT, for the exact graded spaces] Assume U(s+1) (no nonzero polynomial of degree ≤ s+1 vanishes on all nodes) and let P_s be the orthogonal projector onto S_s = {p(X,Y)√w : deg p ≤ s}, θ_s := ‖Π̂_s − P_s‖₂ (sine of the largest principal angle; dim Ŝ_s = dim S_s = N_s). Then ‖(I − Π̂_{s+1})JΠ̂_s‖₂ ≤ ‖J‖₂(θ_s + θ_{s+1}); in particular max(θ_s, θ_{s+1}) ≥ δ_J(s)/(2‖J‖₂)." (2) PD-T?bivariate-lanczos-claude-205 part 4, second sentence, exact claim: "Independently of (C), (W) and of Ĥ (any computed nested spans, any selection): under U(s+1), max(θ_s, θ_{s+1}) ≥ max_{A∈{X,Y}} δ_A(s)/(2‖A‖₂), δ_A(s) the A-defect of the computed nested spans (PD-T?…-202 part 5, verbatim for each operator); in particular θ_LB(n) := max_{s<n} max_A δ_A(s)/(2‖A‖₂) bounds max_{s≤n} θ_s from below (not θ_n alone)." Split after Codex audit-01 finding L2-F4 (a substantive proved part on which other results depend, previously labelled "minor routine").
Split into: none.

## Statement

[EXACT] Nodes z_i = (x_i, y_i), i = 1, …, M, positive weights w_i; X := diag(x_i), Y := diag(y_i) on R^M; S_s := {(p(x_i, y_i)√w_i)_{i=1..M} : deg p ≤ s} with orthogonal projector P_s; N_s := (s+1)(s+2)/2. Let Ŝ_0 ⊆ Ŝ_1 ⊆ ⋯ be **any** nested subspaces of R^M with dim Ŝ_s = N_s — in particular the spans of the computed columns of degree ≤ s of any run of a graded recurrence, whatever its selection rule, window, orthogonalization or reorthogonalization — with orthogonal projectors Π̂_s, and θ_s := ‖Π̂_s − P_s‖₂. For A ∈ {X, Y} let

  δ_A(s) := ‖(I − Π̂_{s+1})AΠ̂_s‖₂ = max{‖(I − Π̂_{s+1})Aw‖₂ : w ∈ Ŝ_s, ‖w‖₂ = 1}.

(a) For every s ≥ 0 and A ∈ {X, Y}: δ_A(s) ≤ ‖A‖₂(θ_s + θ_{s+1}); hence max(θ_s, θ_{s+1}) ≥ δ_A(s)/(2‖A‖₂).
(b) Under U(s+1) (no nonzero polynomial of degree ≤ s+1 vanishes at all nodes), dim S_s = N_s and dim S_{s+1} = N_{s+1}, so θ_s and θ_{s+1} are the sines of the largest principal angles between Ŝ_s, S_s and between Ŝ_{s+1}, S_{s+1}.
(c) Consequently, under U(n), θ_LB(n) := max_{s<n} max_{A∈{X,Y}} δ_A(s)/(2‖A‖₂) ≤ max_{s≤n} θ_s. The bound concerns the maximum over stages, not θ_n alone: e.g. if M = N_n then Ŝ_n = S_n = R^M and θ_n = 0, while earlier stages may have drifted (Codex audit-01).

Any unit vectors w ∈ Ŝ_s give lower bounds for δ_A(s); the original PD-T?…-202 form uses the orthonormal degree-s columns of W = Q̂R⁻¹ with A = J (the injecting operator X of the BJ ordering), and the code (`l2_core.defects`) uses the degree-s columns of a Householder Q-factor of Q̂ — both are such lower bounds, so the computed θ_LB is a valid lower bound up to its floating-point evaluation error (of order u‖A‖₂ times a modest polynomial factor; negligible against the √u-level thresholds where the bound is used, but not certified).

## Definitions

‖A‖₂ = max_i |a_i| for A = diag(a_i). Principal angles as in Golub–Van Loan §6.4.3 (standard; used only for the interpretation (b), not in the proof of (a)).

## Assumptions

Nested subspaces with dim Ŝ_s = N_s; U(s+1) only for the principal-angle interpretation (b) and for (c). The inequality (a) itself needs neither U nor any property of the recurrence (if dim S_s < N_s, then θ_s = 1 and (a) is trivial).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) defect–drift inequality | PROVED | proof below (unchanged from PD-T?…-202 part 5, written for both operators) |
| (b) dimensions / principal-angle reading | PROVED (routine) | proof below |
| (c) θ_LB bounds the maximum over stages | PROVED (routine) | immediate from (a) |

## Depends on

None (elementary linear algebra). Results that depend on this file: PD-N?…-201 (b), PD-N?…-203, PD-N?…-204 (c), PD-T?…-205 (former part 4), PD-T?…-206, PD-T?…-207 (b).

## Checks

Supplementary exact/high-precision checks (not part of the proof): Codex audit-01 reran reconstruction 01's checker (`tracks/bivariate-lanczos/code/review_L2/rl2_exact.py` → `topics/bivariate-lanczos-20261031/audit-01/L2/exact-rerun.log`): in 80-digit arithmetic, δ_J(s)/(2‖J‖) ≤ max(θ_s, θ_{s+1}) true for s = 0..3 in four BJ cases (one-pass window, CGS2-against-all, partial reorthogonalization, and an injected relative error 10⁻³, where max(θ_s, θ_{s+1}) exceeds the bound by factors 5.5–8.9). Audit-01's independent stable-reference experiment (`audit-01/L2/independent_drift.py`, `independent-drift.log`) computed the running defect bound 2.817e-4 (rotated square, n = 24) and 7.768e-4 (triangle, n = 20) against direct drifts 4.105e-3 and 1.016e-2 at the last degree, consistent with (c).

## Sources

None.

## Proof or evidence

(a) A·S_s ⊆ S_{s+1}, because x·p and y·p have degree ≤ s+1 when deg p ≤ s, and A commutes with diag(√w_i). Hence (I − P_{s+1})AP_s = 0 and
  (I − Π̂_{s+1})AΠ̂_s = (P_{s+1} − Π̂_{s+1})AΠ̂_s + (I − P_{s+1})AΠ̂_s = (P_{s+1} − Π̂_{s+1})AΠ̂_s + (I − P_{s+1})A(Π̂_s − P_s),
so δ_A(s) ≤ θ_{s+1}‖A‖₂ + ‖A‖₂θ_s. ∎
(b) Under U(s+1) the evaluation map p ↦ (p(z_i)√w_i)_i is injective on polynomials of degree ≤ s+1, so dim S_{s+1} = N_{s+1} and dim S_s = N_s. For two subspaces of equal dimension the spectral distance of their orthogonal projectors is the sine of the largest principal angle. ∎
(c) For each s < n, (a) gives max(θ_s, θ_{s+1}) ≥ δ_A(s)/(2‖A‖₂) with s, s+1 ≤ n. ∎

## Scope

A reference-free, selection-independent certificate: a computable defect of the computed nested spans bounds from below how far some computed space Ŝ_s, s ≤ n, is from the exact graded space S_s. It is a lower bound only (measured drift exceeds it by 5–15× on the rotated squares and the triangle, PD-T?…-206) and it says nothing about θ_n alone. It is not a statement about any particular algorithm.

## Open items

None for the inequality. (Upper bounds on θ_s from the defects would need a separate argument.)

## History

- 2026-11-01T08:32:22+01:00: created by split from PD-T?…-202 part 5 and the second sentence of PD-T?…-205 part 4 (Codex audit-01, finding **L2-F4**: the drift bound is substantive — other results depend on it and the report advertises it — and needs its own ID; status kept PROVED, no demotion). The original wordings are quoted verbatim in "Split from" above. Changes against the originals: stated for both operators and any nested subspaces in one statement (as the PD-T?…-205 sentence already did), with the equality δ_A(s) = ‖(I − Π̂_{s+1})AΠ̂_s‖₂ as the definition (the PD-T?…-202 form, a max over the orthonormal degree-s columns of W, is a lower bound for it, so the original inequality follows); the remark that (a) needs no U-hypothesis; the M = N_n example for the max-over-stages reading (from audit-01). The proof is the original part-5 proof (Claude Opus 5.5, xhigh; L2 developer, response to audit-01, `directions/L2/response-audit-01.md`; rules read at 8b61391613045f547589e48dcb8037a266bad8aa).
