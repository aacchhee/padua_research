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
  - The Delsarte relaxation of the LP (record -02) is bounded below by (n−½)³D(int 2O) (record -02 (c)), and Theorem 6.4 proves D(int 2O) > |O|. That the finite Delsarte LP is asymptotic to D(int 2O)·n³ is not proved (independent check m7).

## LIT?padua-effective-cubature-20261112-claude-02 — Dostert, Guzmán, de Oliveira Filho, Vallentin, "New upper bounds for the density of translative packings of three-dimensional convex bodies with tetrahedral symmetry"

- **Locator.** [arXiv:1510.02331v3](https://arxiv.org/abs/1510.02331), 10 Jan 2017, 30 pp., with ancillary files (solutions and checkers). The PDF SHA-256 is `25a24f83…901578`. The ancillary evaluator `octa_double.func.cpp` has SHA-256 `034a1aea…7bc47`. Read by the orchestrator on 2026-11-12 (explicit-γ campaign, round 1).
  - Full text read: pp. 1–9 (introduction, Theorem 1.1, Tables 1–2, computational strategy) and §6 (rigorous verification, Table 6, pp. 22–27).
  - Skimmed: §§2–5 (invariant SOS, Fourier transform, SDP formulation).
  - Ancillary files read: `README_SOSChecking`, `README_SampleChecking`, `octa.cpp`, `octa-c.dat`, `octa_double.func.cpp`.
- **Statements used.**
  - **Theorem 1.1** (Cohn–Elkies, as stated there, p. 3–4): let K be a convex body and f a continuous L¹ function with f̂(u) = ∫f(x)e^{−2πiu·x}dx, (i) f̂(0) ≥ 1, (ii) f̂ ≥ 0, (iii) f(x) ≤ 0 whenever K°∩(x+K°) = ∅. Then translative packings of K have density ≤ f(0)vol K.
  - **Template (2), p. 8:** f̂(u) = g(u)e^{−π‖u‖²}, with g a B3-invariant polynomial. Then f(x) = F[g](x)e^{−π‖x‖²}, with F[g] a polynomial.
  - **§6 and Table 6 (p. 26):** rigorous bound 0.972912750 for the regular octahedron B¹₃, with blowup factor α = 1.001. "The solutions, as well as the verification scripts and programs, can be found as ancillary files." The SOS check is a Sage script; the sample check is a C++/MPFI program. The paper says the octahedron check "took several weeks" (p. 27).
  - **Normalisation, from `README_SOSChecking`.**
    - The octahedron uses s = x²+y²+z²−1, i.e. K−K has circumradius 1, so K−K = {|x|₁ ≤ 1} (`octa-c.dat`: the eight facets ±x±y±z ≤ 1) and vol K = 1/6.
    - The bound is F[g](0)·vol K·α³ with g(0) ≥ 1. So their f is ≤ 0 on {|x|₁ ≥ α}.
- **Orchestrator transcription to record -02 (c)** (local, elementary). Put φ(ξ) = f(αξ/2)/f(0). Then φ(0) = 1, φ ≤ 0 on {|ξ|₁ ≥ 2} and φ̂ ≥ 0, and ∫φ = (2/α)³ f̂(0)/f(0) ≥ 8/(α³f(0)) = (4/3)/b with b = α³f(0)/6. Hence (3/4)∫φ − 1 ≥ 1/b − 1, with b = 0.972912750 (Table 6, nine digits). This is recorded in `theory/explicit-gamma.md`.
- **Numerical consistency check (MEASURED, orchestrator).** The 123 invariant coefficients of F[g] in `octa_double.func.cpp` give F[g](0) = 5.8199990323. Its exact Fourier transform gives g(0) = 1.00000017. So 5.8199990/1.00000017 × (1/6) × 1.001³ = 0.972913, which matches Table 6.
- **Coverage limits.**
  - The SOS-verification proof and the MPFI checker were not rerun, and Sage is not installed in this sandbox.
  - §§2–5 were not checked in detail.
  - The ancillary files are third-party and are not committed. Local code downloads them from arXiv and checks their hashes.

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
