# PD-T?padua-xu-lebesgue-20261114-claude-21 — Morrow–Patterson fundamental polynomials at the four vertices (closed forms)

ID kind: PD-T.
Aliases: X2-21; "corner kernel"; MP corner closed forms; re-derivation and extension of Beberok 2025 eq. (2).
Split from: none.
Split into: none. Used by X2-22 (`…-claude-22`), X2-23 (`…-claude-23`), X2-24, X2-25, X2-26, PD-N…-29, PD-N…-30.

## Statement

Let n ≥ 2 be even, M := n + 2, N := M(M + 1). With the definitions below, for every node (p, q) ∈ 𝒩, writing x = x_p, y = y_q, ω = ω_{p,q}:

1. **(Lagrange property, self-contained.)** ℓ_{p,q}(z_{p',q'}) = δ_{pp'}δ_{qq'} for all nodes, the (n+1)(n+2)/2 nodes are pairwise distinct, and f = Σ_{(p,q)∈𝒩} f(z_{p,q}) ℓ_{p,q} for every f ∈ Π_n. So MP_n is unisolvent for Π_n, the ℓ_{p,q} are its fundamental Lagrange polynomials and λ_n is its Lebesgue function.
2. **(Corner kernel.)** For all real x ≠ y,
   G_n(x, y) := Σ_{i+j≤n} (i+1)(j+1) U_i(x) U_j(y) = ¼ [ (F'(x) + F'(y))/(x − y)² − 2 (F(x) − F(y))/(x − y)³ ],  F := T_{M+1} + T_M.
3. **(Vertex values.)** x_p ≠ ±y_q, and
   - ℓ_{p,q}(1, 1) = (−1)^p ω [ (2M+1)/(4(x − y)²) − (2 + x + y)/(2(x − y)³) ],
   - ℓ_{p,q}(−1, 1) = (−1)^p ω [ (2M+1)/(4(x + y)²) + (2 − x + y)/(2(x + y)³) ],
   - ℓ_{p,q}(1, −1) = (−1)^{p+1} ω / (4(x + y)²),
   - ℓ_{p,q}(−1, −1) = (−1)^{p+1} ω / (4(x − y)²).
4. **(Reflection.)** ℓ_{p,q}(−1, 1) = ℓ_{M−p,q}(1, 1) and ℓ_{p,q}(−1, −1)·(x−y)² = ℓ_{p,q}(1, −1)·(x+y)² ; in particular λ_n(−1, 1) = λ_n(1, 1).

(2M + 1 = 2n + 5, so the (1,1) line is Beberok's formula (2).)

## Definitions

- U_i, T_i: Chebyshev polynomials, U_i(cos γ) = sin((i+1)γ)/sin γ, T_i(cos γ) = cos(iγ). Π_n: bivariate polynomials of total degree ≤ n.
- Node index set 𝒩 := {(p, q) ∈ ℤ² : 1 ≤ p ≤ M−1, 1 ≤ q ≤ M, p + q odd}; w_p := pπ/M, v_q := qπ/(M+1), x_p := cos w_p, y_q := cos v_q, z_{p,q} := (x_p, y_q). This is the MP set of `literature-xu-mp.md` §2 with p = m and q = 2k (m odd), q = 2k − 1 (m even).
- ω_{p,q} := 8 sin²w_p sin²v_q / N = C_n(1 − x_p²)(1 − y_q²), C_n = 8/((n+2)(n+3)).
- K_n(P, Q) := Σ_{i+j≤n} U_i(x_P) U_j(y_P) U_i(x_Q) U_j(y_Q); ℓ_{p,q}(P) := ω_{p,q} K_n(P, z_{p,q}); λ_n := Σ_{(p,q)∈𝒩} |ℓ_{p,q}|.

## Assumptions

n even, n ≥ 2 (so M ≥ 4 is even and M + 1 is odd). No external result is used: part 1 replaces the dependence on the cubature theorem of the literature.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. Discrete orthonormality, Lagrange property, reproduction on Π_n | PROVED | Lemma 0 below. Agrees with BBDM Thm 2 (LITERATURE), which is not used. |
| 2. Corner kernel G_n | PROVED | Lemma 1 below |
| 3. Four vertex formulas | PROVED | Lemma 2 + Proposition below. (1,1) coincides with Beberok 2025 eq. (2) (LITERATURE, re-derived here). |
| 4. Reflection, λ_n(−1,1) = λ_n(1,1) | PROVED | from part 3 |

Candidate / claim disposition: none.

## Depends on

Nothing outside this file.

## Checks

- `python3 code/mp/research/x2_corner_checks.py ident` (mpmath, 40 digits; run 2026-11-14, python 3.13.18, mpmath 1.4.1, numpy 2.5.3). Output: orthonormality max error 6.0e−41 (n = 2, 4, 6, all index pairs); corner-kernel formula max relative error 1.5e−37 (n ∈ {2,3,4,7,10,15}, 30 random points, seed 20261114); four vertex closed forms against the defining kernel sums at every node, n ≤ 12: max abs error 7.5e−38.
- Independent rerun: pending (auditor).

## Sources

- LITERATURE (not used as a lemma): Beberok, JAT 311 (2025) 106191, eq. (2) (closed form of K(1,1,w,v); `lit-notes/X2-sources.md` §1b, orchestrator's transcription); BBDM, Constr. Approx. 63 (2026), Thm 2 p. 43 eqs. (7)–(8) (cubature and weights), Lemma 1 p. 45 (x-symmetry).

## Proof or evidence

**Lemma 0 (discrete orthonormality).** For (i, j), (i', j') with i + j ≤ n, i' + j' ≤ n,
Σ_{(p,q)∈𝒩} ω_{p,q} U_i(x_p) U_j(y_q) U_{i'}(x_p) U_{j'}(y_q) = δ_{ii'} δ_{jj'}.

*Proof.* Put α = i+1, α' = i'+1, β = j+1, β' = j'+1. Then 1 ≤ α, α', β, β' ≤ M − 1, α + β ≤ M, α' + β' ≤ M, and the left side is (8/N) Σ_𝒩 f(p, q) with
f(p, q) := sin(αpπ/M) sin(α'pπ/M) sin(βqπ/(M+1)) sin(β'qπ/(M+1)), (p, q) ∈ ℤ².
f is even in p and in q, 2M-periodic in p, 2(M+1)-periodic in q, and vanishes if M | p or (M+1) | q. Let 𝒯 := {−M < p ≤ M} × {−(M+1) < q ≤ M+1}. Both periods are even, so the parity of p + q is well defined on 𝒯, and the points of 𝒯 with M ∤ p, (M+1) ∤ q and p + q odd are exactly the four reflections (±p, ±q) of the points of 𝒩. Hence Σ_{𝒯, p+q odd} f = 4 Σ_𝒩 f, and Σ_{𝒯, p+q odd} f = ½ Σ_𝒯 (1 − (−1)^{p+q}) f.
Write sin(αx) sin(α'x) = ½[cos(a₋x) − cos(a₊x)], a₋ := α − α', a₊ := α + α', and likewise b₋ := β − β', b₊ := β + β'. For integers a, b:
Σ_{−M<p≤M} cos(apπ/M) = 2M·[2M | a], Σ_p (−1)^p cos(apπ/M) = 2M·[a ≡ M mod 2M], and the same with M + 1 in place of M for q. Therefore
Σ_𝒯 (1 − (−1)^{p+q}) cos(apπ/M) cos(bqπ/(M+1)) = 4N·( [2M | a][2(M+1) | b] − [a ≡ M (2M)][b ≡ M+1 (2M+2)] ).
Ranges: |a₋|, |b₋| ≤ M − 2 and 2 ≤ a₊, b₊ ≤ 2M − 2. So [2M | a] holds only for a = a₋ = 0, [2(M+1) | b] only for b = b₋ = 0; [a ≡ M] is possible only for a = a₊ = M, and [b ≡ M+1] only for b = b₊ = M + 1. The last two cannot hold together, because a₊ + b₊ = (α + β) + (α' + β') ≤ 2M < 2M + 1. So the second bracket never contributes and the first contributes only for (a₋, b₋) = (0, 0), with coefficient (½)(½) = ¼. Thus Σ_𝒯 (1 − (−1)^{p+q}) f = N δ_{αα'}δ_{ββ'}, Σ_𝒩 f = (N/8) δδ, and the claim follows. ∎

*Part 1.* The nodes are pairwise distinct (cos is injective on (0, π)) and |𝒩| = (M−1)·M/2 = (n+1)(n+2)/2 = dim Π_n = #{(i,j): i+j ≤ n}. Let A be the square matrix A_{z,(i,j)} := √ω_z U_i(x_z) U_j(y_z). Lemma 0 is AᵀA = I, hence AAᵀ = I, i.e. √(ω_z ω_{z'}) K_n(z, z') = δ_{zz'}. So ℓ_z(z') = ω_z K_n(z', z) = δ_{zz'}. The ℓ_z ∈ Π_n are then linearly independent, hence a basis of Π_n, and f = Σ_z f(z) ℓ_z for f ∈ Π_n by evaluating at the nodes. ∎

**Lemma 1 (diamond sum).** For α, β ∈ ℝ and an integer M ≥ 0 let Φ_M(α, β) := ¼ Σ_{(a,b)∈ℤ², |a|+|b|≤M} e^{i(aα+bβ)}. Then
(cos α − cos β) Φ_M(α, β) = ¼ [F̃(α) − F̃(β)], F̃(γ) := cos((M+1)γ) + cos(Mγ).

*Proof.* Put z = e^{iα}, ζ = e^{iβ}, 1_M(a, b) := [|a| + |b| ≤ M]. Then (z + z⁻¹ − ζ − ζ⁻¹) Σ 1_M(a,b) z^a ζ^b = Σ c(a,b) z^a ζ^b with c(a,b) = 1_M(a−1,b) + 1_M(a+1,b) − 1_M(a,b−1) − 1_M(a,b+1). If a ≠ 0 ≠ b then {|a−1|, |a+1|} = {|a|−1, |a|+1} and likewise for b, so c = 0. If b = 0 ≠ a: c = [|a| ≤ M+1] + [|a| ≤ M−1] − 2[|a| ≤ M−1] = [|a| ∈ {M, M+1}]. If a = 0 ≠ b: c = −[|b| ∈ {M, M+1}]. If a = b = 0: c = 0. Hence the product is 2F̃(α) − 2F̃(β), and z + z⁻¹ − ζ − ζ⁻¹ = 2(cos α − cos β). ∎

Grouping (±a, ±b) gives Φ_M(α, β) = Σ_{a,b≥0, a+b≤M} c_a c_b cos(aα) cos(bβ) with c_0 = ½, c_a = 1 (a ≥ 1). So the polynomial P_M(x, y) := Σ_{a,b≥0, a+b≤M} c_a c_b T_a(x) T_b(y) satisfies (x − y) P_M(x, y) = ¼ [F(x) − F(y)] on [−1,1]², hence identically, with F = T_{M+1} + T_M.

*Part 2.* T_a' = a U_{a−1} for a ≥ 1 and T_0' = 0, so ∂_x∂_y P_M = Σ_{a,b≥1, a+b≤M} ab U_{a−1}(x) U_{b−1}(y) = G_{M−2} = G_n. For x ≠ y, with Q := (F(x) − F(y))/(x − y): ∂_yQ = −F'(y)/(x−y) + (F(x)−F(y))/(x−y)², and ∂_x∂_yQ = (F'(x) + F'(y))/(x−y)² − 2(F(x) − F(y))/(x−y)³. ∎

**Lemma 2 (lattice values).** For 1 ≤ p ≤ M − 1 and x = cos(pπ/M): F(x) = (−1)^p (1 + x), F'(x) = (−1)^p (M + 1). For 1 ≤ q ≤ M and y = cos(qπ/(M+1)): F(y) = (−1)^q (1 + y), F'(y) = −(−1)^q M.

*Proof.* F' = (M+1)U_M + M U_{M−1}. With w = pπ/M: T_M(x) = (−1)^p, T_{M+1}(x) = cos(pπ + w) = (−1)^p x, U_{M−1}(x) = sin(pπ)/sin w = 0, U_M(x) = sin(pπ + w)/sin w = (−1)^p. With v = qπ/(M+1): T_{M+1}(y) = (−1)^q, T_M(y) = cos(qπ − v) = (−1)^q y, U_M(y) = 0, U_{M−1}(y) = sin(qπ − v)/sin v = −(−1)^q. ∎

**Proposition (lattice values of G_n).** Let 1 ≤ p ≤ M−1, 1 ≤ q ≤ M, x = cos(pπ/M), y = cos(qπ/(M+1)). Then x ≠ y, and
- if p + q is odd: G_n(x, y) = (−1)^p [ (2M+1)/(4(x−y)²) − (2 + x + y)/(2(x−y)³) ];
- if p + q is even: G_n(x, y) = −(−1)^p / (4(x−y)²).

*Proof.* x = y would give p(M+1) = qM, so M | p, impossible. If p + q is odd, (−1)^q = −(−1)^p, so F(x) − F(y) = (−1)^p(2 + x + y) and F'(x) + F'(y) = (−1)^p(2M + 1). If p + q is even, F(x) − F(y) = (−1)^p(x − y) and F'(x) + F'(y) = (−1)^p, so G_n = ¼(−1)^p[1/(x−y)² − 2/(x−y)²]. Insert in part 2. ∎

*Part 3.* U_i(±1) = (±1)^i (i+1) and (±1)^i U_i(x) = U_i(±x), so K_n((ε₁, ε₂), (x, y)) = G_n(ε₁x, ε₂y) for ε₁, ε₂ ∈ {±1}. Moreover −x_p = cos((M−p)π/M) with M − p ≡ p (mod 2) (M even), and −y_q = cos((M+1−q)π/(M+1)) with M + 1 − q ≡ q + 1 (mod 2) (M + 1 odd). For (p, q) ∈ 𝒩:
- (1, 1): lattice point (p, q), odd: the first formula.
- (−1, 1): lattice point (M−p, q), odd: G_n(−x, y) = (−1)^p[(2M+1)/(4(x+y)²) − (2 − x + y)/(2(−x−y)³)], the second formula.
- (1, −1): lattice point (p, M+1−q), even: G_n(x, −y) = −(−1)^p/(4(x+y)²).
- (−1, −1): lattice point (M−p, M+1−q), even: G_n(−x, −y) = −(−1)^p/(4(x−y)²).
Multiply by ω. The Proposition also gives x_p ≠ ±y_q. ∎

*Part 4.* K_n((−1,1), z_{p,q}) = G_n(x_{M−p}, y_q) = K_n((1,1), z_{M−p,q}), ω_{M−p,q} = ω_{p,q}, and (p, q) ↦ (M−p, q) is a bijection of 𝒩. Hence ℓ_{p,q}(−1,1) = ℓ_{M−p,q}(1,1) and λ_n(−1,1) = λ_n(1,1). The second identity is read off part 3. ∎

## Scope

Exact identities for every even n ≥ 2 at the four vertices only. Part 2 is a polynomial identity valid for every integer n ≥ 0 (M = n + 2). Nothing is claimed at other points of Q.

## Open items

None for this record. A four-term closed form at general points is recorded (with proof sketch and numerical check) in X2-28 as a tool for the argmax problem.

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-2; uncommitted at writing (orchestrator owns Git). First version.
