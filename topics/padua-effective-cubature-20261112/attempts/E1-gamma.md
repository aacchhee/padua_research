# Attempt E1-γ — explicit γ (campaign authorised by AC: up to seven rounds)

AC (2026-11-12): "I authorize up to seven rounds to make gamma explicit". Claude (Opus 5.5 xhigh, orchestrator). Gates: `../gates.md` addendum G, pushed at `5ad0a5f` before any run.

## Round 1 — literature (done)

- **Observation.** By record -04's argument read in reverse, γ_A > 0 explicit is equivalent to an explicit Cohn–Elkies density bound < 1 for translative packings of the octahedron. The Cohn–Elkies admissibility conditions for K = O/2 are exactly Delsarte admissibility for int(K−K).
- **Found and read:** Dostert–Guzmán–de Oliveira Filho–Vallentin (arXiv:1510.02331v3), with the rigorous bound 0.972912750 for B¹₃, blowup 1.001 (LIT?…-claude-02).
- **Result:** record -07. γ_A ≥ 1/b − 1 > 1/36, so N ≥ 37n³/216 for every n. No package exists for n ≥ 218. The bound improves on Fisher for n ≥ 109.
- **Status:** PROVED with LITERATURE dependency (computer-assisted literature certificate).

## Round 2 — local certificate (planned)

- **Data.** The DGOV ancillary evaluator gives F[g] as 123 rational (decimal) coefficients in the B3 invariants s₁, s₂, s₃. Take P := F[g] exactly as these decimals, and f := P·e^{−π|x|²}. Compute f̂ = G·e^{−π|u|²} exactly: G ∈ ℚ[π^{−1}][u], with even exponents only.
- **Obligations, all by rigorous enclosure (interval or ball arithmetic) plus explicit tail bounds:**
  1. G ≥ 0 on ℝ³. MEASURED minimum ≈ 0.09 on samples, so the margin looks large.
  2. P ≤ 0 on {|x|₁ ≥ α′}. MEASURED maximum ≈ −1.8·10⁻⁴, near ‖x‖ = 1 in edge directions, so the margin is tight.
  3. The value: (3/4)(2/α′)³G(0)/P(0) − 1.
- **Exploration.** The exploration script is in the session scratchpad. The ancillary files are third-party: they are not committed, and the committed checker fetches them by URL and verifies their SHA-256.
