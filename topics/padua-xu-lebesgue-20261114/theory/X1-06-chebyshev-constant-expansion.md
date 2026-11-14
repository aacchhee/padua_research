# PD-T?padua-xu-lebesgue-20261114-claude-06 — Exact series and two-sided n⁻⁴ enclosure for the Chebyshev-zero Lebesgue constant L_n

ID kind: PD-T.
Aliases: X1-06; one-dimensional lemma of G2; sharpening of PD-T270; L_n = A_n + π/(72n²) − O(n⁻⁴).
Split from: round X1-2 target T2 (the one-dimensional lemma of the vertex expansion).
Split into: none.

## Statement

For every integer n ≥ 1 let L_n = (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)) and A_n = (2/π)(log n + γ + log(8/π)). Let

  φ₀(t) = 1/t − 1/(2 sinh(t/2)) (t > 0),  G(x) = ∫₀^∞ e^{−xt} φ₀(t) dt (x > 0).

**(a) Exact series.** G is positive and strictly decreasing, G(x) ≤ 1/(24x²), and

  L_n = A_n + (4/π) Σ_{j=1}^∞ (−1)^{j−1} G(nj).   (1)

**(b) Enclosure.** For every n ≥ 1,

  A_n + π/(72n²) − 7/(240π n⁴) < L_n < A_n + π/(72n²).   (2)

In particular 0 < L_n − A_n < π/(72 n²) < 0.0437/n², which sharpens PD-T270's |L_n − A_n| ≤ 1/(4n²).

## Definitions

γ = lim_m (H_m − log m), H_m = Σ_{r=1}^m 1/r. Natural logarithms. (G(x) equals ψ(x+½) − log x with ψ the digamma function; this identification is used only in the numerical check, not in the proof.)

## Assumptions

Exact real arithmetic; integer n ≥ 1.

## Status by part

Overall status: **PROVED** (written proof below; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (a) exact series (1) | PROVED | §§1–5 |
| (b) enclosure (2), every n ≥ 1 | PROVED | §6 |
| Numerical agreement (1): 15 values of n to 4e−41; (2): 444 values n ≤ 1991 | MEASURED (verification only) | Checks |

## Depends on

- PD-T269 (merged), §4 eq. (9): cot(πt/2) = 2/(πt) − (4t/π) Σ_{m≥1} 1/(4m² − t²), proved there locally; used for t = p/(2n) ∈ (0, 1).
- Classical facts, used with their textbook status (the same status as the ingredient Σ_{l odd} l⁻² = π²/8 of PD-T159): Σ_{j≥1} (−1)^{j−1} j⁻² = π²/12; Wallis' product Π_{m≥1} (2m−1)(2m+1)/(2m)² = 2/π. The use of Wallis' product can be replaced by PD-T270 (merged); see §5.
- Elementary: Tonelli for nonnegative integrands; power series of sinh.

## Checks

`python3 code/xu/research/x1_1d_check.py --nmax 2000` (mpmath 40 digits; run 2026-11-14, 6 s):
- (a) for n ∈ {1..12, 20, 50, 101}: partial sums S_{4000} < (L_n − A_n)π/4 < S_{4001} of the series (1) with G(x) = ψ(x+½) − log x; the accelerated sum (`mpmath.nsum`) deviates from (L_n − A_n)π/4 by at most `4.3104e-41`;
- (b) (2) holds for 444 values of n in [1, 1991]; n⁴(A_n + π/(72n²) − L_n) ∈ [0.006156, 0.008792288], below 7/(240π) = 0.009284 and increasing towards 49π³/172800 = 0.008792289 (the classical next coefficient);
- (c) 0 < t/24 − φ₀(t) < 7t³/5760 on t = 0.01..40 (4000 points); ∫₀^∞ e^{−xt}φ₀ dt = ψ(x+½) − log x to 2.6e−41 for x ∈ {1, 2, 3.5, 10, 64}.

MEASURED; no constant in the statement comes from these runs.

## Sources

LITERATURE (context; unread, not proof inputs): asymptotic expansions of the Chebyshev Lebesgue constants with leading correction π/(72 n²) are classical (Günttner, SIAM J. Numer. Anal. 17 (1980); Shivakumar–Wong 1982; Dzjadyk–Ivanov 1983), usually stated for n+1 nodes. The enclosure (2) is proved here from scratch; no novelty is claimed for it.

## Proof or evidence

**§1. Partial fractions.** For odd p ∈ {1, …, 2n−1} apply PD-T269 (9) with t = p/(2n) ∈ (0,1):
 cot(pπ/(4n)) = (4n/π) [ 1/p − Σ_{m≥1} 2p/((4nm)² − p²) ] = (4n/π) [ 1/p + Σ_{m≥1} ( 1/(4nm+p) − 1/(4nm−p) ) ],
the series being absolutely convergent. For j ≥ 0 let B_j = Σ_{i=1}^n 1/(2nj + 2i − 1), the sum of the reciprocals of the odd integers in (2nj, 2n(j+1)). As p runs over 1, 3, …, 2n−1, the numbers 4nm + p run over the odd integers in (2n·2m, 2n(2m+1)) and 4nm − p over those in (2n(2m−1), 2n·2m). Summing over p and dividing by n:

  (π/2) L_n = 2B₀ + Σ_{m=1}^∞ (2B_{2m} − 2B_{2m−1}).   (3)

**§2. Kernel inequalities.** For t > 0 and s = t/2:
 (K1) φ₀(t) > 0, because sinh s > s.
 (K2) φ₀(t) < t/24. Indeed sinh(s)(1 − s²/6) − s = Σ_{k≥1} s^{2k+1} [1 − 2k(2k+1)/6]/(2k+1)!, the k = 1 coefficient is 0 and all others are negative, so sinh(s)(1 − s²/6) < s. If 1 − s²/6 > 0 this gives 1/sinh s > 1/s − s/6; otherwise 1/sinh s > 0 ≥ 1/s − s/6. Hence 1/(2 sinh(t/2)) > 1/t − t/24.
 (K3) t/24 − φ₀(t) ≤ 7t³/5760. Equivalently 1/sinh s ≤ 1/s − s/6 + 7s³/360, i.e. (the polynomial 1 − s²/6 + 7s⁴/360 is positive, its discriminant in s² being 1/36 − 7/90 < 0) sinh(s)(1 − s²/6 + 7s⁴/360) ≥ s. The coefficient of s^{2k+1} on the left is [1 − m(m+1)/6 + 7(m+1)m(m−1)(m−2)/360]/(m+1)! with m = 2k; it is 1 for k = 0, 0 for k = 1 and k = 2 (1 − 20/6 + 840/360 = 0), and for m ≥ 6 it equals [1 + m(m+1)(7(m−1)(m−2)/360 − 1/6)]/(m+1)! > 0 because 7(m−1)(m−2) ≥ 140 > 60.

Consequently G(x) = ∫₀^∞ e^{−xt}φ₀(t)dt converges for x > 0, 0 < G(x) < ∫₀^∞ e^{−xt}(t/24)dt = 1/(24x²), and G is strictly decreasing with G(x) → 0 as x → ∞. Likewise

  H(x) := 1/(24x²) − G(x) = ∫₀^∞ e^{−xt}(t/24 − φ₀(t)) dt satisfies 0 < H(x) ≤ (7/5760)·3!/x⁴ = 7/(960x⁴), and H is strictly decreasing.   (4)

**§3. A summation formula.** For x > 0 and an integer N ≥ 1,

  Σ_{i=1}^N 1/(x + i − ½) = log((x+N)/x) − G(x) + G(x+N).   (5)

Proof. 1/(x+i−½) = ∫₀^∞ e^{−(x+i−½)t}dt and Σ_{i=1}^N e^{−(i−½)t} = (1 − e^{−Nt})/(2 sinh(t/2)), so the left side is ∫₀^∞ e^{−xt}(1 − e^{−Nt})/(2 sinh(t/2)) dt. By Tonelli, log((x+N)/x) = ∫_x^{x+N} dy/y = ∫_x^{x+N}∫₀^∞ e^{−yt} dt dy = ∫₀^∞ e^{−xt}(1 − e^{−Nt})/t dt. Subtracting, the difference log((x+N)/x) − Σ equals ∫₀^∞ e^{−xt}(1 − e^{−Nt})φ₀(t)dt = G(x) − G(x+N). ∎

**§4. The blocks.** For j ≥ 1, (5) with x = nj, N = n gives

  2B_j = Σ_{i=1}^n 1/(nj + i − ½) = log((j+1)/j) − G(nj) + G(n(j+1)).   (6)

For j = 0: for M ≥ 1, by (5) with x = n, N = M,
 Σ_{i=1}^{n+M} 1/(i − ½) = 2B₀ + log((n+M)/n) − G(n) + G(n+M).
The left side is 2H_{2K} − H_K with K = n+M, and 2H_{2K} − H_K = log K + γ + 2 log 2 + o(1) as K → ∞ by the definition of γ. Letting M → ∞ (G(n+M) → 0):

  2B₀ = log n + γ + 2 log 2 + G(n).   (7)

**§5. Summation.** Write G_j = G(nj). By (6), 2B_{2m} − 2B_{2m−1} = log((2m+1)/(2m)) + log((2m−1)/(2m)) + G_{2m+1} − 2G_{2m} + G_{2m−1}. Summing m = 1..M:
- the logarithms give log Π_{m=1}^M (2m−1)(2m+1)/(2m)² → log(2/π) (Wallis);
- Σ_{m=1}^M (G_{2m+1} − 2G_{2m} + G_{2m−1}) = 2Σ_{j=1}^{2M} (−1)^{j−1}G_j − G₁ + G_{2M+1}.
Insert this and (7) into (3). The term G(n) = G₁ of (7) cancels −G₁, G_{2M+1} → 0, and Σ(−1)^{j−1}G_j converges (alternating, terms decreasing to 0; also absolutely, G_j ≤ 1/(24n²j²)). Hence
 (π/2) L_n = log n + γ + 2 log 2 + log(2/π) + 2 Σ_{j≥1} (−1)^{j−1} G(nj),
which is (1) after multiplication by 2/π. ∎(a)

*Wallis-free variant.* The product Π(1 − 1/(4m²)) converges to some w ∈ (0,1) without any evaluation, and the argument gives L_n = (2/π)(log n + γ + 2 log 2 + log w) + (4/π)S_n with 0 < S_n < G(n) < 1/(24n²). PD-T270 proves L_n − (2/π)(log n + γ + log(8/π)) → 0. Comparing the two as n → ∞ gives 2 log 2 + log w = log(8/π). So (1) also follows from PD-T270 instead of Wallis' product.

**§6. Enclosure.** By (4), G(nj) = 1/(24n²j²) − H(nj), so
 Σ_{j≥1} (−1)^{j−1} G(nj) = (1/(24n²)) · π²/12 − S_H, S_H := Σ_{j≥1} (−1)^{j−1} H(nj).
The numbers H(nj) are positive and strictly decreasing in j, so 0 < H(n) − H(2n) < S_H < H(n) ≤ 7/(960n⁴). Therefore
 L_n = A_n + (4/π)·π²/(288n²) − (4/π)S_H = A_n + π/(72n²) − (4/π)S_H, 0 < (4/π)S_H < 7/(240π n⁴). ∎(b)

(The lower bound in (2) is positive relative to A_n: π/72 > 7/(240π), i.e. π² > 2.1, so L_n > A_n for every n ≥ 1.)

## Scope

All n ≥ 1; explicit and sign-definite. It does not give the n⁻⁴ coefficient (classically 49π³/172800, consistent with the measured values); only the enclosure (2).

## Open items

Audit. Optional: next coefficients (not needed for X1).

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher. Written because the vertex value is exactly L_n² (X1-03), so the quality of the G2 remainder is the quality of the one-dimensional estimate; PD-T270's 1/(4n²) would already suffice for G2, and (2) replaces it by a two-sided bound with the exact n⁻² coefficient.
