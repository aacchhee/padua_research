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

## Round 2 — local certificate (done, developer run)

- **Code.** `code/gamma_certificate.py`, a rigorous float branch and bound. It uses Taylor-shift enclosures in y = x², with an a-priori error bound, the exact ℓ₁-region test, and a ray-shift tail test from |x|_∞ ≥ 4. Arb is used for the value.
- **Transform check.** `code/gamma_ft_check.py` (MEASURED; quadrature cross-check of the exact transform), with agreement 7·10⁻¹².
- **Result: PASS in 121 s.** The certified value is γ₁ = 0.02784156869… > 1/36 (`evidence/gamma-certificate.json`), at the same α = 1.001 as DGOV.
- **Rejected before the final design (no claims):**
  - A naive tail bound using |lower parts| fails: the lower parts are about 10⁶, against a leading part of 8.6·10⁻⁴ on the axis.
  - Natural and mean-value enclosures are too loose because of cancellation.
  - The tail shift test at |x|_∞ ≥ 2–3 failed under interval coefficients; it passes at 4.
- **Margins (MEASURED):**
  - P on |x|₁ = 1.0 has a maximum of +3.2·10⁻³, so α = 1 fails; P on |x|₁ = 1.0005 still has a positive maximum, +1.3·10⁻³.
  - At α = 1.001 the boundary maximum is −6.1·10⁻⁴.
  - The interior maximum is ≈ −1.8·10⁻⁴, near (0, 0.71, 0.72).
  - So α cannot be lowered below roughly 1.0007 with this function.
- **Independent rerun:** delegated to a separate Opus agent, with its own code path written from the specification only. Pending.

## Round 3 — bounded improvement attempt (empty; no claim)

- **Idea.** Replace DGOV's SOS restriction with a sampled cut-plane LP in the same class: f = P·e^{−π|x|²}, P in B3 invariants of degree ≤ 26. Maximise 6G(0)/P(0) − 1 subject to P ≤ 0 on |x|₁ ≥ α and G ≥ 0. Code: `code/lp_gamma_explore.py`, HiGHS, raw invariant basis with column scaling.
- **Outcome: numerically unreliable.**
  - With α = 1.001 the cut-plane optimum fell to 0.0150 after 25 rounds and was still falling. A known feasible point of that very LP, the DGOV function, has value 0.030926 (orchestrator check: its rows satisfy all sampled constraints, max P·w < 0, min G·w > 0).
  - An LP relaxation cannot fall below a feasible point, so the solver results are wrong. The likely cause is the ill-conditioned basis: coefficients range over ±10⁶ with heavy cancellation.
  - No value from this run is reported.
- **Disposition.** The improvement direction is stopped after this one empty round, with γ₁ = 1/36 (certified) kept as the campaign result. Resume conditions:
  - a well-conditioned basis (Hermite functions or Laguerre × harmonics) with a high-precision solver (SDPA-GMP or an exact-rational LP);
  - or a different template (not polynomial × fixed Gaussian).
  
  DGOV report that degrees above 26 did not improve their bound (`README_SOSChecking`). The cap remains 1/18 (record -04).
- **Campaign rounds used:** 3 of 7. Round 1, literature: γ ≥ 1/36 with LITERATURE dependency. Round 2: local certificate. Round 3: empty.
