# PD-T?padua-effective-cubature-20261112-claude-03 — Theorem A in uniform form: N ≥ (1+γ_A)(2n−1)³/48 for every n, with γ_A = (3/4)D(int 2O) − 1 > 0

ID kind: PD-T.
Aliases: uniform Theorem A; Delsarte proof of Theorem A; E1 main result.
Split from: none. It is an alternative proof and strengthening in form of PD-T?padua-3d-20261106-codex-D1-04 (Theorem A), which keeps its own ID, proof and status.
Split into: none. The explicit value of γ_A is the separate OPEN target -05.

## Statement

Let γ_A := (3/4)·D(int 2O) − 1, with D the Delsarte constant defined in record -02 (c). Then:

**(i)** γ_A > 0.

**(ii)** For every integer n ≥ 1 and every positive cubature rule with all nodes in the closed cube [−1,1]³, exact on Π_{2n−2} (in particular on Π_{2n−1}) for normalized product Chebyshev measure,

  N ≥ (1 + γ_A)(2n − 1)³/48.

**(iii)** Consequently, for every γ with 0 < γ < γ_A, there is an explicit n₀(γ, γ_A) such that N ≥ (1+γ)·binom(n+2,3) for all n ≥ n₀. Take n₀ to be the least integer such that (1 + γ_A)(n − 1/2)³ ≥ (1+γ) n(n+1)(n+2) holds for all n ≥ n₀. It exists because the two sides are cubics with leading coefficients 1+γ_A > 1+γ.

A positive "Padua-package" rule (N = binom(n+3,3), exact on Π_{2n−1}) is impossible whenever

  (1 + γ_A)(n − 1/2)³ > (n+1)(n+2)(n+3).

**(iv)** γ_A ≤ 1/18 (record -04), so this route can give at most γ = 1/18. Even with γ_A = 1/18, (iii) excludes packages only for n ≥ 138 (computed in the Check below). So it can never close 4 ≤ n ≤ 137.

The constant γ_A is a single, well-defined real number. Its value is not known. Every certified Delsarte function φ with ∫φ > 4/3 gives an explicit lower bound γ_A ≥ (3/4)∫φ − 1 and makes (ii)–(iii) fully explicit (target -05).

## Definitions

O = {|ξ|₁ ≤ 1}, |O| = 4/3; the Delsarte constant is as in record -02 (c); binom(n+2,3) = dim Π_{n−1}(ℝ³).

## Status by part

Overall status: **PROVED with explicit LITERATURE dependency** (same convention as D1-04).

| Part | Status | Evidence |
|---|---|---|
| (i) γ_A > 0 | LITERATURE-dependent, PROVED given it | KLM Theorem 6.4 with A = O, plus "O does not tile ℝ³ by translations" (below) |
| (ii) uniform bound | PROVED (local) | record -02 (c) and (i) |
| (iii) explicit n₀ in terms of γ_A | PROVED (local, routine) | cubic comparison |
| (iv) cap | PROVED (local) | record -04 |

## Depends on

- Record -02 (local, PROVED).
- **LITERATURE, KLM Theorem 6.4** (Kolountzakis–Lev–Matolcsi, arXiv:2510.10172v1, §6.5, p. 25). It reads: "Let A ⊂ ℝ^d be a convex body. The equality D(Δ(A)) = m(A) holds if and only if A tiles by translations." Here Δ(A) is the essential difference set. For an origin-symmetric convex body Δ(A) = int(2A) (KLM §6.5, p. 25), so Δ(O) = int(2O) and m(O) = 4/3. Also D ≥ m(A) always (KLM (6.2)). KLM's proof rests on their strong duality (Thm 5.4), existence of extremizers (Thm 5.6) and [KLM23, Thm 1.4] (weak tiling implies tiling for convex bodies). None of these is locally verified.
- **"O does not tile ℝ³ by translations"** (LITERATURE). Route used: if O tiled, then by the Fuglede theorem for convex bodies (Lev–Matolcsi, LIT-660) O would be spectral. That contradicts Greenfeld–Lev Thm 1.1 (LIT-659), as applied in D1-04 (O has a triangular, non-centrally-symmetric facet). The "tile ⇒ spectral" direction of Lev–Matolcsi is quoted from KLM §6.5 ("a convex body A ⊂ ℝ^d is a spectral set if and only if it can tile the space by translations"). It is not checked against the LIT-660 record, which records the "spectral ⇒ tiling" direction. An independent classical route: the Venkov–McMullen characterisation of convex translational tiles (centrally symmetric facets). Not read; recorded as an alternative only.

## Proof

**(i).** By KLM (6.2), D(int 2O) ≥ 4/3. O is a convex body that does not tile, so Theorem 6.4 gives D(int 2O) ≠ m(O) = 4/3. Hence D(int 2O) > 4/3, and γ_A > 0.

**(ii).** Record -02 (c) gives N ≥ (n − 1/2)³ D(int 2O)/8 = (n − 1/2)³ (4/3)(1+γ_A)/8 = (1+γ_A)(2n−1)³/48.

**(iii).** (ii) and the identity binom(n+2,3) = n(n+1)(n+2)/6 give N/binom(n+2,3) ≥ (1+γ_A)(n − 1/2)³/(n(n+1)(n+2)). This ratio tends to 1+γ_A, so it is ≥ 1+γ from an explicitly computable n₀ on. The package condition is the same comparison with binom(n+3,3) = (n+1)(n+2)(n+3)/6. ∎

## Relation to Theorem A (D1-04)

D1-04 proves the existence of γ, n₀ through a compactness/stationary-limit argument (D1-02/03) and Greenfeld–Lev. This record:
- replaces D1-02/D1-03 by the elementary transference -02;
- uses a different literature theorem (KLM 6.4) for strictness;
- gives the bound for every n ≥ 1, with the only unknown being the single constant D(int 2O).

D1-04's hypotheses (closed-cube nodes, positivity, exactness 2n−1) are exactly covered. Its exactness can be weakened to 2n−2. Both results remain registered separately: D1-04 does not depend on KLM, and this record does not depend on D1-02/03. Their literature dependencies overlap (LIT-659/660).

## Checks

- **Arithmetic for (iv).** With γ_A = 1/18, the least n₁ such that 19(2m−1)³ > 144(m+1)(m+2)(m+3) holds for every m ≥ n₁ is n₁ = 138, by exact integer evaluation of 19(2n−1)³ > 144(n+1)(n+2)(n+3). Command run 2026-11-12 (Python 3.13):
  `python3 -c "print(next(n for n in range(1,10**4) if all(19*(2*m-1)**3>144*(m+1)*(m+2)*(m+3) for m in range(n,n+2000))))"`, output `138`. At m = 138 the two sides are 395140625 > 395115840; at m = 137 it fails. The difference is a cubic with positive leading coefficient 152 − 144 = 8, and the window m < n+2000 lies beyond its last real root, so the inequality holds for all m ≥ 138.
- **D3.** At n = 3, (ii) gives N ≥ (1+γ_A)·125/48 ≤ 2.75; there is no conflict with the 20-node D3 rule.

## Scope

- Positive weights; nodes in the closed cube; exactness 2n−2 suffices.
- This does not decide any finite n ≤ 137, and by (iv) it cannot.
- No signed-weight conclusion is drawn.
- The value of γ_A is OPEN.
- No statement about T(int 2O) is made. Whether T(int 2O) > 4/3 is open in the literature: KLM p. 2 says no convex body other than tiles, balls and their products has known Turán constant, and even the regular octagon is open.

## Open items

- Explicit lower bound for γ_A (record -05).
- An independent check of the transcription of KLM Thm 6.4 and of the non-tiling route.

## History

2026-11-12, Claude (Opus 5.5 xhigh, orchestrator). First written in session 1 of the topic. It is a development claim that requires the Codex audit.
