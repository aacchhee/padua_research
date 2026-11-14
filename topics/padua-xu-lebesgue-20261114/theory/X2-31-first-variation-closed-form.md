# PD-T?padua-xu-lebesgue-20261114-claude-31 — first variation of the Morrow–Patterson Lebesgue function at the upper vertices: closed forms, band representation, local-maximum criterion

ID kind: PD-T.
Aliases: X2-31; first variation at (±1,1); D_x, D_y; step P1 (closed-form part) of the argmax plan of X2-28.
Split from: X2-28 (plan item P1), exact-formula part.
Split into: none. The sign of D_x, D_y for 2 ≤ n ≤ 3000 is X2-32; the sign for n > 3000 is OPEN (X2-28 addendum).

## Statement

Let n ≥ 2 be even, M = n + 2, N = M(M+1), and use the notation of X2-21, X2-23 (nodes (p,q) ∈ 𝒩, x = x_p, y = y_q, ω = ω_{p,q}, A_{p,q} = (−1)^p ℓ_{p,q}(1,1), band B = {Y < X < κY}). Put d := x − y, s := 2 + x + y and

- N_x := (M(M+1)(M+2)/3) d³ − [2M² + (2M²+8M+4)x] d² + [6xs − (8M+6)(1−x²)] d + 8(1−x²)s,
- N_y := ((M−1)M(M+1)/3) d³ + [(6M+2)y − 2(M+1)² − 2M(M+1)y] d² − [6ys + (8M+2)(1−y²)] d + 8(1−y²)s.

(a) **Closed forms.** For every node, ∂_xℓ_{p,q}(1,1) = (−1)^p ω N_x/(4d⁵) and ∂_yℓ_{p,q}(1,1) = (−1)^p ω N_y/(4d⁵).

(b) **Local polynomial.** Assume ℓ_a(1,1) ≠ 0 for every node a (true for every even n ≥ 2 by X2-23 (f); certified independently of X2-23 (f) for n ≤ 3000 in X2-32). Then there is a neighbourhood 𝒰 of (1,1) in ℝ² with λ_n = P_n on 𝒰 ∩ Q, where P_n := Σ_a sgn(ℓ_a(1,1)) ℓ_a ∈ Π_n, and
P_n(x,y) = −U_n(x) − 2 Σ_{a∈B} (−1)^p ℓ_a(x,y).

(c) **Band representation.** With T_a := −(−1)^p ∂_xℓ_a(1,1) = −ωN_x/(4d⁵) and T'_a := −ωN_y/(4d⁵),
D_x := ∂_xP_n(1,1) = −n(n+1)(n+2)/3 + 2 Σ_{a∈B} T_a,  D_y := ∂_yP_n(1,1) = 2 Σ_{a∈B} T'_a.

(d) **Criterion.** Under the assumption of (b): if D_x > 0 and D_y > 0, then (1,1) and (−1,1) are strict local maxima of λ_n on Q; if D_x < 0 or D_y < 0, neither is a local maximum.

(e) **Symmetry (used in (d)).** λ_n(−x, y) = λ_n(x, y) on ℝ².

## Definitions

As in X2-21 and X2-23. 𝔇 := (1−x²)∂_x² − 3x∂_x (Gegenbauer operator, 𝔇U_i = −i(i+2)U_i). G_n(x,y) = Σ_{i+j≤n}(i+1)(j+1)U_i(x)U_j(y) (corner kernel, X2-21 part 2). Q = [−1,1]².

## Assumptions

n even, n ≥ 2. Part (b)–(d) use ℓ_a(1,1) ≠ 0 (X2-23 (f), which rests on a textbook cyclotomic fact; for n ≤ 3000 see X2-32).

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) closed forms | PROVED | proof below; checked at 40 digits and in ball arithmetic against the defining sums |
| (b) local polynomial | PROVED | X2-23 (b), (c), (f) |
| (c) band representation | PROVED | reproduction on Π_n (X2-21 part 1) |
| (d) criterion | PROVED | first-order Taylor expansion |
| (e) symmetry | PROVED | one line below (agrees with BBDM Lemma 15, LITERATURE, not used) |
| sign of D_x, D_y | not part of this record | X2-32 (n ≤ 3000, computer-assisted); n > 3000 OPEN |

Candidate / claim disposition: none.

## Depends on

X2-21 parts 1–3 (reproduction, corner kernel G_n = ¼Q_{XY}, lattice values of F, F'); X2-23 (b), (c), (f).

## Checks

- `/tmp/x2r3/explore1.py` (scratch, mpmath 40 digits, n ∈ {2,4,6,8}, all nodes): closed forms (a) against Σ i(i+1)(i+2)/3·(j+1)U_iU_j and the y-analogue: max relative error 4.3e−35.
- `python3 code/mp/research/x2r3_first_variation_arb.py --full --nmin 2 --nmax 24` (python-flint 0.9.0, 192 bits; 2026-11-14; 0.2 s): for every node of every even n ≤ 24 the ball of the closed form overlaps the ball of the defining sum (`all_closed_forms_overlap: true`); D_x, D_y from the defining sums over all nodes agree with the band representation (c) (`--band`) to all printed digits, e.g. n = 2: D_x = 4.9511320421682110891, D_y = 7.0019580831342828584; n = 24: D_x = 20690.069773390533628, D_y = 22566.557068445872937.
- Independent rerun: pending (auditor).

## Sources

None used. LITERATURE (not used): BBDM, Constr. Approx. 63 (2026), Lemma 15 (x-symmetry).

## Proof or evidence

**(e)** K_n((−x,y), z_{M−p,q}) = Σ U_i(−x)U_i(−x_p)U_j(y)U_j(y_q) = K_n((x,y), z_{p,q}) because U_i(−t) = (−1)^iU_i(t) and x_{M−p} = −x_p. Also ω_{M−p,q} = ω_{p,q}, and (p,q) ↦ (M−p,q) is a bijection of 𝒩 (M even). Hence ℓ_{M−p,q}(−x,y) = ℓ_{p,q}(x,y) and λ_n(−x,y) = λ_n(x,y). ∎

**(a)** U_i'(1) = i(i+1)(i+2)/3 = (i(i+2)/3)U_i(1) (from 𝔇U_i = −i(i+2)U_i at x = 1). So
∂_sK_n((s,1),(x,y))|_{s=1} = Σ_{i+j≤n} (i(i+2)/3)(i+1)(j+1)U_i(x)U_j(y) = −(1/3) 𝔇_x G_n(x,y).
By X2-21 part 2, G_n = ¼Q_{XY} for x ≠ y, with Q(X,Y) := (F(X) − F(Y))/(X − Y), F = T_{M+1} + T_M. Differentiating,
Q_{XXY} = F''(X)/δ² − [4F'(X) + 2F'(Y)]/δ³ + 6[F(X) − F(Y)]/δ⁴,
Q_{XXXY} = F'''(X)/δ² − 6F''(X)/δ³ + [18F'(X) + 6F'(Y)]/δ⁴ − 24[F(X) − F(Y)]/δ⁵, δ := X − Y,
and ∂_sK_n|_{s=1} = ¼[xQ_{XXY} − (1−x²)Q_{XXXY}/3] at (X,Y) = (x,y).
*Lattice values.* Let e := (−1)^p, x = cos(pπ/M). By X2-21 Lemma 2, F(x) = e(1+x), F'(x) = e(M+1); for a node, (−1)^q = −e, so F(y) = −e(1+y), F'(y) = eM. With T := T_M, S := T_{M+1}: (1−x²)T'' = xT' − M²T and (1−x²)S'' = xS' − (M+1)²S; differentiating, (1−x²)T''' = 3xT'' + (1−M²)T' and (1−x²)S''' = 3xS'' + (1−(M+1)²)S'. At x: T = e, T' = 0, S = ex, S' = e(M+1). Hence
(1−x²)F''(x) = −eM[M + (M+1)x], (1−x²)F'''(x) = −eM[3x(M + (M+1)x)/(1−x²) + (M+1)(M+2)].
Insert (F(x) − F(y) = es, F'(x) = e(M+1), F'(y) = eM, δ = d):
e·Q_{XXY} = −M[M+(M+1)x]/((1−x²)d²) − (6M+4)/d³ + 6s/d⁴,
e·Q_{XXXY} = −M[3x(M+(M+1)x)/(1−x²) + (M+1)(M+2)]/((1−x²)d²) + 6M[M+(M+1)x]/((1−x²)d³) + (24M+18)/d⁴ − 24s/d⁵.
In x·eQ_{XXY} − (1−x²)eQ_{XXXY}/3 the two terms with (1−x²)⁻¹d⁻² cancel, and the rest is
M(M+1)(M+2)/(3d²) − [x(6M+4) + 2M² + 2M(M+1)x]/d³ + [6xs − (8M+6)(1−x²)]/d⁴ + 8(1−x²)s/d⁵ = N_x/d⁵.
So ∂_xℓ_{p,q}(1,1) = ω ∂_sK_n = eωN_x/(4d⁵).
For y: ∂_tK_n((1,t),(x,y))|_{t=1} = ¼[yQ_{XYY} − (1−y²)Q_{XYYY}/3], and Q is symmetric, so the same formulas hold with X ↔ Y and δ' := y − x = −d. At y = cos(qπ/(M+1)), with e' := (−1)^q = −e: S = e', S' = 0, T = e'y, T' = −e'M, hence (1−y²)F''(y) = −e'(M+1)[(M+1) + My] and (1−y²)F'''(y) = e'(M+1)[−3y((M+1)+My)/(1−y²) + M(M−1)]. Inserting (F(y) − F(x) = −es, F'(y) = eM, F'(x) = e(M+1)), the (1−y²)⁻¹δ'⁻² terms cancel again and, using δ'³ = −d³, δ'⁵ = −d⁵,
e[yQ_{XYY} − (1−y²)Q_{XYYY}/3] = (M−1)M(M+1)/(3d²) + [(6M+2)y − 2(M+1)² − 2M(M+1)y]/d³ − [6ys + (8M+2)(1−y²)]/d⁴ + 8(1−y²)s/d⁵ = N_y/d⁵. ∎

**(b)** The ℓ_a are continuous and finitely many, so the signs are constant near (1,1). By X2-23 (b), sgn ℓ_a(1,1) = (−1)^p off B and −(−1)^p on B. By X2-21 part 1 with f = U_n(x) and U_n(x_p) = −(−1)^p (X2-22), Σ_a (−1)^pℓ_a = −U_n(x). Hence P_n = Σ_a (−1)^pℓ_a − 2Σ_B (−1)^pℓ_a = −U_n(x) − 2Σ_B(−1)^pℓ_a. ∎

**(c)** Differentiate (b) at (1,1): U_n'(1) = n(n+1)(n+2)/3 and ∂_yU_n(x) = 0. ∎

**(d)** P_n is a polynomial, so for (x,y) ∈ Q, with ρ := (1−x) + (1−y) ≥ 0: P_n(x,y) = P_n(1,1) − D_x(1−x) − D_y(1−y) + O(ρ²) ≤ λ_n(1,1) − min(D_x,D_y)ρ + Cρ². If min(D_x, D_y) > 0 this is < λ_n(1,1) for 0 < ρ < min(D_x,D_y)/C, inside 𝒰. If, say, D_x < 0, then λ_n(1−ε, 1) = λ_n(1,1) + |D_x|ε + O(ε²) > λ_n(1,1) for small ε > 0. The vertex (−1,1) follows from (e). ∎

Remark (equivalent forms, used by the certificate and by the plan). On B put ε := X/Y − 1 ∈ (0, 4/(2M−1)) and κ₀ := 4 − (2M−1)ε ∈ (0, 4). Then (direct expansion; float-checked for M ∈ {6, 20, 50}) N_x = 8Y²[a₀(ε) + a₁(ε)Y] with a₀ = κ₀(4+2ε) − ε² and a₁ = (M(M+1)(M+2)/3)ε³ − 2(M²+4M+2)(1+ε)ε² + 6(1+ε)(2+ε)ε + (8M+6)(1+ε)²ε − 8(1+ε)²(2+ε); |A_a| = 8(1+ε)(1−X)(1−Y)κ₀/(Nε³) and T_a = −8(1+ε)(1−X)(1−Y)[a₀ + a₁Y]/(Nε⁵Y). This remark is not used in the proofs above.

## Scope

Exact identities at the vertices (±1,1) for every even n ≥ 2. The signs of D_x, D_y are not claimed here.

## Open items

Sign of D_x, D_y for n > 3000 (X2-28 addendum, item P1-tail).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3, rules read at `fc0d629`; uncommitted at writing (orchestrator owns Git). First version.
