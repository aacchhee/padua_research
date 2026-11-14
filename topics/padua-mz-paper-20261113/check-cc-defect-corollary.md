# Independent check: PD-T?mz-paper-claude-01 (theory/cc-defect-condition-corollary.md)

Checker: Claude Opus 5.5 (`claude-opus-5-5`), effort high (as assigned), 2026-11-13, head 761e884. I am an independent internal subagent and did not write the record. No repository file other than this one and review-plan-cc.md was written.

**Verdict: PASS with corrections.** The mathematics of (a), (b) and (c) is correct at the stated scope, and every numerical value checks. The corrections concern how dependencies and inputs are labelled, plus one inaccurate scope sentence. No part of any statement needs weakening.

## Dependency statements actually read

- **PD-T013** (manuscript Lemma 2.1, PROOF_STATUS row): positive weights, and exactness through degree d_N ≥ N. In particular constants lie in Π_{N−1} for N ≥ 2, and their quotient is 1.
- **PD-T017** (m2-cardinal-lower.md): for N ≥ 2 and every p ∈ Π_N, ∫p² ≤ K_N Q_N(p²). Hence λ_−(N,N−1) ≥ λ_−(N,N) ≥ 1/K_N > 0.
- **PD-T018** (m2-parity-upper.md): λ_−(N,N−1) ≤ 128000/(log N)² for every N ≥ 2.
- **PD-T019** (m2-u-witness.md): exact norms of U_{N−1} for every N ≥ 2. Used below for an improved onset.
- **PD-T022** (m3-upper-ratio.md): for N ≥ 2, 0 ≤ n < N and p ∈ Π_n, Q_N(p²) ≤ (1+ρ_{N,n})∫p², where ρ_{N,n} = max{2n/N−1, 0}².
- **PD-T025** (m3-hyperinterpolation.md):
  - Hypotheses: a positive rule of mass V and any B with Q(p²) ≤ B‖p‖² on Π_n. If Q is exact on degree ≤ n+k with 0 ≤ k ≤ n, then ‖f−𝓛_n f‖ ≤ √V(1+√B)E_k(f).
  - The CC application uses V = 2 and B = 1+ρ_{N,n}; the resulting uniform factor is (1+√2)√2, a supremum that is not attained because 1+ρ < 2.
- **PD-T526** (S2-uniform-upper.md): for every integer N ≥ 2 and every real p of degree ≤ N−1, 0 < Q_N(p²) ≤ (5/3)∫p².
- **PD-T527** (S2-eta-deficit.md): 1−η_N = min(λ_−, 2−λ_+) exactly, with min(1/K_N, 1/3) ≤ 1−η_N ≤ min(1, 128000/(log N)²). No limiting coefficient is asserted.
- **PD-T530** (S2-qualitative-limit.md): lim λ_max(G_{N,N−1}) = Λ_edge through all N, with 1 ≤ Λ_edge ≤ 3/2. The interval is [1, 3/2], confirmed, not PD-T529's [1, 5/3].
- **PD-T546** (P3-reverse-bound.md): lim (log N)² λ_min(CC, N−1) = π⁴/8 through all integers N, with the natural logarithm. The same holds on Π_N.
- **PD-T547** (P4-certified-lower.md): Λ_edge ≥ 1.0044369. This is one-sided and **computer-assisted**.

## Reconstruction

### (a)

- **Bracketing.** The constant polynomial gives λ_− ≤ 1 ≤ λ_+. So the spectrum of I−G_N lies in [1−λ_+, 1−λ_−], and η_N = max(1−λ_−, λ_+−1), i.e. 1−η_N = min(λ_−, 2−λ_+). This holds for all N ≥ 2.
- **Identity.** PD-T526 gives 2−λ_+ ≥ 1/3. Hence λ_− ≤ 1/3 implies 1−η_N = λ_−. ✓
- **Limit.** λ_− → 0 (by PD-T546, or already by PD-T018), so the identity holds eventually. Then (log N)²(1−η_N) = (log N)²λ_− for all large N, which tends to π⁴/8 through all N. ✓
- **Sufficiency only.** The condition λ_− ≤ 1/3 is sufficient, not necessary. The statement claims only sufficiency. ✓

### (b)

- **Limit.** λ_− > 0 (PD-T017), and G_N is symmetric positive definite, so κ_2 = λ_+/λ_−. Then κ_2/(log N)² = λ_+/[(log N)²λ_−] → Λ_edge/(π⁴/8) = 8Λ_edge/π⁴. Both factor limits hold through all integers N (PD-T530, PD-T546), so no parity restriction is needed. ✓
- **Interval.** [8·1.0044369/π⁴, 8·(3/2)/π⁴] = [8·1.0044369/π⁴, 12/π⁴]. ✓

### (c)

- **Admissible B.**
  - PD-T526 is stated for every polynomial of degree ≤ N−1. So for n ≤ N−1 it applies to Π_n directly; this is restriction of a supremum to a subspace, and no separate argument is needed.
  - N = 2 is covered, since PD-T526 assumes only N ≥ 2.
  - PD-T022 covers 0 ≤ n < N.
  - Both bounds are admissible B's in PD-T025, and so is their minimum. ✓
- **Exactness condition.** "Exact on Π_k·Π_n" equals "exact on Π_{n+k}" in one dimension. For CC this means k ≤ min(n, d_N − n). ✓
- **Factor.** With V = 2 the factor is √2(1+√B). ✓

## Numerical values (computed in Python, Decimal at 40 digits, π by Machin's formula; exact Fractions where stated)

| Quantity | Computed | Record | |
|---|---|---|---|
| 8·1.0044369/π⁴ | 0.0824922511308… | 0.082492… | ✓ |
| 12/π⁴ | 0.1231917870562… | 0.123192… | ✓ |
| containment in [0.08249, 0.12320] | 0.08249 ≤ 0.082492…; 0.123192… ≤ 0.12320 | | ✓ |
| π⁴/8 | 12.1761363792… | | ✓ |
| √(5/3) | 1.2909944487… | 1.29099… | ✓ |
| 1+√(5/3) | 2.2909944487… < 2.2910 | | ✓ |
| (1+√(5/3))√2 vs (1+√2)√2 | 3.23996 vs 3.41421 | | ✓ |
| √384000 | 619.67733539… | ≈ 619.7 | ✓ (e^{619.68} ≈ 10^{269.1}) |
| 128000/(log N)² ≤ 1/3 ⇔ log N ≥ √384000 | | | ✓ |

## Corrections required

1. **Depends on / Checks are inaccurate.** They say "No numerical input" and "Analytic; no computation". Parts (a), (c) and the limit in (b) are analytic. The lower end of the numeric interval in (b) uses PD-T547, which is computer-assisted (exact interval checker with receipts).
   Write instead: "(b)'s displayed interval inherits PD-T547's computer-assisted certificate. The analytic Λ_edge ≥ 1 (PD-T529/530) gives the computer-free interval [8/π⁴, 12/π⁴] = [0.082127…, 0.123192…]."
2. **The scope sentence on the onset is inaccurate.** The record says there is no effective N beyond which 1−η_N = λ_−(N) "other than through the explicit PD-T018 bound (log N ≥ 619.7)". In fact PD-T019, a proved all-N exact witness with U_{N−1} ∈ Π_{N−1}, gives λ_−(N) ≤ q_N := c_N/S_N, where c_N = 1 for odd N, c_N = N²/(N²−1) for even N, and S_N = Σ_{j≤N} 1/(2j−1). Checked in exact rational arithmetic:
   - S_57 > 3, so q_N ≤ 1/S_57 < 1/3 for every odd N ≥ 57.
   - For every even N ≥ 58, q_N ≤ (58²/57·59)/S_58 = 0.33211… < 1/3, since c_N decreases and S_N increases.
   - q_56 = 0.33406 > 1/3 and q_55 = 0.33496 > 1/3, so the witness alone does not reach below 57.

   Hence **1−η_N = λ_−(N,N−1) for every N ≥ 57, analytically.** Either add this to (a) with a three-line proof, which I recommend because it also fixes the plan's "no effective onset" remark, or at least correct the Scope sentence. There is still no effective rate for (log N)²(1−η_N) → π⁴/8.
3. **(c) clarity (minor).**
   - Note that min{1+ρ_{N,n}, 5/3} < 1+ρ_{N,n} only when 2n/N − 1 > √(2/3), i.e. n/N > 0.90825. There the admissible k ≤ d_N − n is small, so "a constant improvement only" is accurate.
   - Say "supremum" for the draft's (1+√2)√2, because it is not attained.
4. **Housekeeping.**
   - Add PD-T019 to Depends on if correction 2 is adopted.
   - Status may now cite this check. The Codex audit remains a separate, still pending obligation.

## Quantifier summary

- PD-T526 covers N = 2 and all n ≤ N−1 (directly, by its "degree at most N−1" wording): yes.
- PD-T530's interval is [1, 3/2]: yes.
- PD-T546 and PD-T530 hold through all integers N, so (a) and (b) need no parity restriction: yes.
- κ_2 is well defined for every N ≥ 2 (PD-T017): yes.
