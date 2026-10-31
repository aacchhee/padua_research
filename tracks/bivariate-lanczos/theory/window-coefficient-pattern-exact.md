# PD-T?bivariate-lanczos-claude-101 — Exact coefficient pattern of the window recurrence: formed, structural-zero and implicit entries of H_F and H_J

ID kind: PD-T.
Aliases: window lemma; exact-support window; "which entries of H_y (H_x) are formed"; HL BIT Thm 2.3 / BJ Thm 1 re-derived for the campaign ordering; implicit-column recursion; Z = N_k identification.
Split from: none (answers part (a) of plan L1-Q1 in exact arithmetic; the [FP] part is PD-T?…-102).
Split into: none.

## Statement

[EXACT] Let z_i = (x_i, y_i), i = 1..M, be distinct, w_i > 0, X = diag(x), Y = diag(y), q_0 = √w/‖√w‖, and let n ≥ 1 with **U(n+1)**: no nonzero polynomial of total degree ≤ n+1 vanishes at all nodes. Index the columns of degree t by (t, j), j = 0..t, with leading monomial m_{t,j} = x^{t−j}y^j, ordered (t′, j′) ≺ (t, j) iff t′ < t or (t′ = t and j′ < j) (the input code's order). Generate
  q_{t,0} ∝ (I − Π_{≺(t,0)}) J q_{t−1,0},  q_{t,j} ∝ (I − Π_{≺(t,j)}) F q_{t−1,j−1} (j ≥ 1),
with J = X ("injecting" operator), F = Y ("full" operator) and Π_{≺k} the orthogonal projector onto span{q_l : l ≺ k}, normalised with positive coefficient. Then for t ≤ n:

1. **(Graded basis.)** q_{t,j} = c m_{t,j}(X,Y)q_0 + (combination of m_l(X,Y)q_0, l ≺ (t,j)) with c > 0; q_{t,j} is the Gram–Schmidt orthonormalisation of the monomial vectors in the order ≺. Hence span{q_l : l ⪯ (t,t)} = S_t := {p(X,Y)q_0 : deg p ≤ t}.
2. **(Support of F-columns.)** For p = (t, j), ⟨F q_p, q_l⟩ ≠ 0 only if l ∈ {(t−1, i) : i ≥ j−1} ∪ {(t, i) : 0 ≤ i ≤ t} ∪ {(t+1, r) : r ≤ j+1}; the entry at l = (t+1, j+1) (the child of p) is the normaliser β > 0.
3. **(Support of J-columns.)** For p = (t, j), ⟨J q_p, q_l⟩ ≠ 0 only if l ∈ {(t−1, i) : i ≥ j} ∪ {(t, i)} ∪ {(t+1, r) : r ≤ j}.
4. **(Formed vs implicit.)** The recurrence forms, for every p of degree ≤ n−1, the complete F-column p (its support in 2. equals the exact window of the child plus the child), and the J-column p only for p = (t, 0). The J-columns p = (t, j), j ≥ 1 (t of the t+1 columns of each degree block), are never formed. In the window counts: the J-product creating (t, 0) is orthogonalised against blocks t−2 and t−1 (2t−1 vectors); the F-product creating (t, 1) against 2t vectors; the F-product creating (t, j), j ≥ 2, against block t−2 from index j−2, block t−1 and (t, 0..j−1): 2t+1 vectors. (The input code's 'block' window, all of degrees t−2..t, is a superset.)
5. **(Implicit columns are fixed by commutativity.)** With h_l, β the coefficients of the F-product creating (t, j), j ≥ 1 (so β q_{t,j} = F q_{t−1,j−1} − Σ_{l∈W} h_l q_l),
  β · H_J e_{(t,j)} = H_F H_J e_{(t−1,j−1)} − Σ_{l∈W} h_l H_J e_l,
where H_A := QᵀAQ for a basis Q of S_{t+1}; all columns on the right have index ≺ (t, j), so the J-section is determined recursively from the formed columns (s, 0) and the F-section.
6. **(Minor routine lemma: the HL SIMAX section is Z.)** For any real orthonormal basis U of S_k, Z := UᵀXU + iUᵀYU = U*(X + iY)U is unitarily similar to the square part of N_k in HL SIMAX (4.2) with N = X + iY; the two have the same Ritz values and the same Ritz vectors (as vectors of C^M), hence the same Ritz residuals ‖N y − θ y‖.

The mirror convention (HL BIT table (2.1): H = x applied to every vector of cycle k−1, K = y to the first only) is obtained by exchanging x and y; then F = X is full and J = Y injects, and "only part of H_y is formed", as plan.md states.

## Definitions

N_t = (t+1)(t+2)/2; block t = columns (t, 0..t). "Formed" = an entry whose value is produced by the recurrence as an inner product or normaliser. "Structural zero" = an entry outside the supports of 2.–3. "Implicit" = an entry inside the support that is not formed.

## Assumptions

Distinct nodes; w > 0; U(n+1) (so dim S_{n+1} = N_{n+1} and the monomial vectors of degree ≤ n+1 are independent). Exact arithmetic.

## Status by part

Overall status: PROVED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 1. graded basis | PROVED (routine) | proof below |
| 2.–3. supports | PROVED | proof below; numerical check (long double) below |
| 4. formed vs implicit, window counts | PROVED (routine, from 2.–3.) | agrees with HL BIT Thm 2.3 (≤ 2k+1) in mirrored order and BJ Thm 1 (α_{j,l} = 0 for l < j″) as reported in LIT?…-106, -129 |
| 5. implicit-column recursion | PROVED (routine) | proof below |
| 6. Z = N_k identification | PROVED (minor routine) | proof below |

## Depends on

None (self-contained). Literature cross-checks only: LIT?bivariate-lanczos-claude-106 (HL BIT Thm 2.3), -116 (HL SIMAX Thm 3.7, window 2k for the (N, N*) form), -129/-130 (BJ Thm 1, Cor 3–4), -117 (HL SIMAX (4.2)).

## Checks

- Structural zeros: `tracks/bivariate-lanczos/code/L1/l1_recurrence.py` run in `np.longdouble` with the 'block' window on 300 random nodes (seed 0, uniform weights), degree ≤ 12: the largest computed coefficient outside the exact window of 4. was 1.25e-19 (long-double rounding level), i.e. no nonzero outside the derived support. Command (R01 smoke check, 2026-10-31): see `topics/bivariate-lanczos-20261031/directions/L1/R01.md` §2.
- The count 2t+1 (resp. 2t−1 for the injected product) matches the HL BIT proof on p. 398 (read in the fulltext, scratchpad copy).

## Sources

HL BIT 2002 pp. 395–398 (Algorithm 1, Thm 2.1, Thm 2.3 and its proof) read in the fulltext; HL SIMAX 2002 pp. 1079–1080 (Algorithm 1 listing) read in the fulltext; BJ 1985 via its record only.

## Proof or evidence

Write V_k = span{m_l(X,Y)q_0 : l ⪯ k}. Under U(n+1) the vectors m_l(X,Y)q_0, deg m_l ≤ n+1, are linearly independent (a vanishing combination is a polynomial of degree ≤ n+1 vanishing on the nodes, times the positive vector q_0).

*1.* Induction on k in the order ≺. Let k = (t, j) with parent p and operator A ∈ {J, F}. The multiplication maps preserve ≺ on the relevant ranges: for l = (t′, j′) ≺ p, y·m_{t′,j′} = m_{t′+1,j′+1} and (t′+1, j′+1) ≺ (t, j) when j ≥ 1; for l ≺ (t−1, 0) (i.e. t′ < t−1), x·m_{t′,j′} = m_{t′+1,j′} has degree < t. Hence A V_{≺p} ⊂ V_{≺k}, where V_{≺k} = span{m_l q_0 : l ≺ k}. By induction q_p = c_p m_p q_0 + v with c_p > 0 and v ∈ V_{≺p}, so A q_p = c_p m_k q_0 + A v ∈ c_p m_k q_0 + V_{≺k}. Since m_k q_0 ∉ V_{≺k} (independence), (I − Π_{≺k})A q_p ≠ 0 and q_k has leading coefficient c_p / β > 0 and span{q_l : l ⪯ k} = V_k.

*2.* F q_p ∈ V_{(t+1,j+1)} by the argument in 1., so ⟨F q_p, q_l⟩ = 0 for l ≻ (t+1, j+1). For l = (t′, i) with t′ ≤ t−1, ⟨F q_p, q_l⟩ = ⟨q_p, F q_l⟩ (F symmetric) and F q_l ∈ V_{(t′+1, i+1)}; q_p ⊥ V_{≺p}; hence the inner product vanishes when (t′+1, i+1) ≺ (t, j), i.e. when t′ < t−1, or t′ = t−1 and i+1 < j. What remains is the stated set. At l = (t+1, j+1): ⟨F q_p, q_l⟩ = β > 0 by 1.

*3.* As in 2. with x·m_{t′,i} = m_{t′+1,i}: J q_p ∈ V_{(t+1,j)}, and for t′ ≤ t−1 the entry vanishes when (t′+1, i) ≺ (t, j).

*4.* The child of p = (t, j) under F is (t+1, j+1), and the exact window of the child (block (t+1)−2 = t−1 from index max(j−1, 0), block t, (t+1, 0..j)) together with the child itself is exactly the support in 2. Every p of degree ≤ n−1 has an F-child of degree ≤ n, so all F-columns of S_{n−1} are formed. Only p = (t, 0) has a J-child; the J-columns with j ≥ 1 have no child and are never formed. Counts: J-product creating (t, 0): blocks t−2 and t−1 have (t−1) + t = 2t−1 columns. F-product creating (t, j): from block t−2 the columns (t−2, i) with i ≥ j−2 (t−1−max(j−2,0) columns), block t−1 (t columns), (t, 0..j−1) (j columns): 2t for j = 1 and 2t+1 for j ≥ 2.

*5.* Apply J to β q_{t,j} = F q_{t−1,j−1} − Σ_{l∈W} h_l q_l and use JF = FJ (diagonal matrices): β J q_{t,j} = F (J q_{t−1,j−1}) − Σ h_l J q_l. Expand J q_l = Q H_J e_l (exact, J S_s ⊂ S_{s+1}) and F Q = Q H_F on the relevant leading columns (F S_s ⊂ S_{s+1}); multiply by Qᵀ.

*6.* Both are compressions of N to the same subspace S_k ⊗ C: the square part of N_k is Q̂*NQ̂ with Q̂ an orthonormal basis of span_C{p(N)q_0 : p polyanalytic, deg ≤ k} (HL SIMAX (4.2), Prop. 3.1), and for real nodes span_C{z^a z̄^b} = span_C{x^c y^d} degree by degree. Two orthonormal bases of the same subspace differ by a unitary W, Q̂ = UW, so Q̂*NQ̂ = W*(U*NU)W. Ritz vectors U s and Q̂ (W* s) coincide.

## Scope

Exact arithmetic only. The statement "only one column per degree of H_J is formed" is what makes single-operator Paige theory inapplicable verbatim to J (OBST?…-03); for F it applies (PD-T?…-102, -103). Part 6 means that in exact arithmetic the frozen comparison objects Z and N_k are the same; in floating point they differ only because the two algorithms compute different spans (R01 §3).

## Open items

None for the exact statement. The [FP] counterparts (defect of the implicit columns) are PD-T?…-102 and R01/R02.

## History

- 2026-10-31: created (Claude Opus 5.5, xhigh; L1 R01). Re-derivation, no novelty claimed.
