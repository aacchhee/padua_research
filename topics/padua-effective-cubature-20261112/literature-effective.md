# Literature — padua-effective-cubature-20261112

Orchestrator: Claude (Opus 5.5). Read 2026-11-12. Third-party PDFs and extracts stay in the session scratchpad; none is committed.

## LIT?padua-effective-cubature-20261112-claude-01 — Kolountzakis, Lev, Matolcsi, "The Turán and Delsarte problems and their duals"

- **Locator.** [arXiv:2510.10172v1](https://arxiv.org/abs/2510.10172), 11 Oct 2025, 29 pp., CC BY 4.0. Full text read by the orchestrator: all of pp. 1–6 and §§4.1–4.3, 5.1–5.3 and 6–7 (pp. 7–8, 15–16, 23–28). The duality proofs of §§4.5–5.7 were skimmed only, not checked.
- **Definitions used locally (§5.2, Def. 5.1).** A Delsarte admissible function is a continuous real f ∈ L¹(ℝ^d) with f(0) = 1, f ≤ 0 on U^∁ and f̂ ≥ 0. D(U) is the supremum of ∫f. The Turán constant T(U) is defined in §4.2 with f = 0 on U^∁.
- **Statements used as LITERATURE.**
  - Theorem 6.4 (p. 25): "Let A ⊂ ℝ^d be a convex body. The equality D(Δ(A)) = m(A) holds if and only if A tiles by translations."
  - §6.5: for an origin-symmetric convex body, Δ(A) is the interior of 2A.
  - (6.2): D(Δ(A)) ≥ m(A).
  - Corollary 6.5: the Delsarte packing bound is strictly better than the volume bound for non-tiling convex bodies.
- **Context statements, not used as premises.**
  - p. 2: it is a major open problem whether T(U) = 2^{−d} m(U) for every origin-symmetric convex body. T(U) is known for no convex body other than tiles, balls and their products, and "even the simplest cases, such as a regular octagon in the plane, are open."
  - Turán equality is known for convex tiles [AB02, KR03] and balls [Gor01, KR03, Gab24].
  - Theorem 6.1: the density of any packing by translates of A is ≤ D(Δ(A))^{−1}.
  - §6.5 reports Lev–Matolcsi [LM22]: a convex body is spectral iff it tiles.
- **What was independently checked.** Nothing in the KLM proofs. Locally we prove only the elementary inequalities of records -02 and -04. The proof of Theorem 6.4 depends on the source's strong duality (Thm 5.4), the existence of extremizers (Thm 5.6), Theorem 5.8 and [KLM23, Thm 1.4]. It is inherited as LITERATURE in record -03.
- **Bearing on the BRIEF.**
  - BRIEF §1.4 route E1 (plain LP ↔ T(2O)) asks whether the octahedron is a non-Turán domain. By this source that would be the first known non-Turán convex body: a major open problem, not a step to take in a topic round.
  - The Delsarte relaxation of the LP (record -02) instead asymptotes to D(2O), which Theorem 6.4 proves is > |O|.

## Existing records consulted (no new LIT entry)

- **LIT-640 (Betke–Henk; Minkowski 1904).** Used only for the displayed lattice basis. Its determinant and minimal ℓ₁ norm are checked exactly by `code/cap_critical_lattice.py`; the optimality theorem is not used (record -04).
- **LIT-663 (Kuperberg, arXiv math/0405366v2).** Re-read pp. 5 and 14–15 on 2026-11-12.
  - Theorem 3.2 (p. 5) gives the best lattice t-design count via lattice packing density, attributed possibly to Frolov. Its example: "the lattice packing density of the regular octahedron C*₃ is 18/19. So there exists an additive 5-design on T(SO(6)) with 38 points."
  - p. 15: "Xu observed that the method for t-designs also yields bounds on PI t-cubature [34]. In fact it yields an upper bound on the ℓ2 norm of the weights."
  - §7 (p. 14) asks for non-lattice positive continuous Fourier cubature that beats lattice rules.
  - Our record -02 is an instance of this classical LP method. Record -03's strictness conclusion is the new combination with KLM 2025, as far as this search goes.
- **LIT-659 (Greenfeld–Lev) and LIT-660 (Lev–Matolcsi).** Used for "O does not tile", via spectral ⇔ tile for convex bodies. The "tile ⇒ spectral" direction is taken from the KLM §6.5 report, not from LIT-660's record. Flagged in record -03.

## Searches run (2026-11-12, WebSearch)

1. "Turán problem positive definite functions octahedron cross-polytope extremal value" (extended). Found KR03, KR06, Révész 2011 (arXiv 0904.1824), Berdysheva–Ramabulana–Révész (arXiv 2412.00482), KLM 2025, and Stechkin's periodic cross-polytope estimates (snippet only). No value of T or D for the 3-D octahedron was found.
2. "Kolountzakis Révész Turán's extremal problem convex domain spectral tile |K/2| upper bound packing density" (standard). Found KR03 (PAMS 131, 2003), KR06, KLM 2025.

Coverage limits: snippet-level only for Stechkin, Gorbachev, Arestov–Berdysheva, Révész 2011 and BRR24. No fulltext search was made of the Russian-language literature on periodic Turán problems for cross-polytopes (Ivanov, Gorbachev). No priority or absence claim is made.

## Pointers for AC (not read)

- Kolountzakis–Révész, Proc. AMS 131 (2003) 3423–3430: [AMS](https://www.ams.org/proc/2003-131-11/S0002-9939-03-07023-0/) (arXiv math/0204086).
- Y. Xu, J. Complexity 19 (2003) 392–402 (LP method for positive cubature lower bounds); still unread, as recorded in `topics/padua-3d-20261106/final-d1/sources.md` L45.
