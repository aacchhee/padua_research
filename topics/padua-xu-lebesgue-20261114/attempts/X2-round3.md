# X2 round 3 — attempts, routes and obstructions (Morrow–Patterson argmax)

Researcher: Claude Fable 5.2 (xhigh), subagent; 2026-11-14; rules read at `fc0d629`. No Git operation except read-only `git log`. The session was interrupted once by a server restart and resumed; no file was lost. Durable results: `theory/X2-31 … X2-34`, `theory/X2-N35`, addendum in `theory/X2-28`. Statuses here are informal.

## 0. Outcome by target

| Target | Outcome | Record |
|---|---|---|
| P1 closed-form first variation | PROVED | X2-31 |
| P1 sign of D_x, D_y | PROVED for even n ≤ 3000 (ball arithmetic, rerun pending); OPEN for n > 3000 | X2-32; X2-28 addendum |
| P2–P3 scaling limit, lim Λ_n/n² = c* | OPEN; tools proved (translation formula, averaged bound); heuristic limit of the shifted sums measured | X2-34, X2-N35 |
| P4 far field | PROVED: maximizers within O(log²n/n) of the vertices, explicit | X2-33 |
| P4 eventual argmax | OPEN | X2-28 addendum (W1–W3) |
| P5 odd n / EMP | not attempted | — |

## 1. P1: what worked

- ∂_sK_n((s,1),z)|_{s=1} = −(1/3)𝔇_xG_n(z) (U_i is an eigenfunction of 𝔇 = (1−x²)∂² − 3x∂), G_n = ¼Q_{XY}; the lattice values of F'', F''' follow from the Chebyshev ODEs; the (1−x²)⁻¹d⁻² terms cancel. Result: N_x, N_y (X2-31).
- Σ_a(−1)^p∂_xℓ_a(1,1) = −U_n'(1) and Σ_a(−1)^p∂_yℓ_a(1,1) = 0, so only band nodes enter (X2-31 (c)); the band is monotone in each column, which makes the certificate O(n) per degree (X2-32).

## 2. P1-tail: routes tried and why they stopped

1. **Node-wise positivity of the logarithmic derivative** ρ = ∂ℓ_a/ℓ_a at band nodes. Measured: ρ_x ≥ 0.07M² on B (M ≤ 400), ρ_y > 0 on B except at (1,2). With X2-26 this would give D_x > 0 for M ≥ 10 at once. Obstruction: in the variables ε = X/Y − 1, Y the condition is H := a₀(ε) + a₁(ε)Y < 0 (X2-31 remark), and along the first superdiagonal the node curve is tangent to {H_lead = 0} at the far end (near (−1,−1)): H = M⁻⁴ − (2/3)M⁻²θ² − (8/15)θ⁴ + …, with a₀(ε_max) = M⁻⁴ exactly at ε_max = (2M+1)/M². First-order (1/M) arguments cannot decide the sign there. Not refuted; needs a second-order two-variable analysis (hypergeometric form in the X2-28 addendum).
2. **Crude bounds for the far-end nodes.** Term-by-term bounds of N_x/d⁵ are O(M⁵) per node against a true size O(M). Markov + Cauchy–Schwarz (|ℓ_a| ≤ (ω_aK_n(P,P))^{1/2}) loses a factor M and covers only μ ≲ 0.18M^{−1/3}, while crude closed-form control starts at μ ≳ M^{−1/4}. Dead end without the exact cancellation.
3. **Symbolic structure** (sympy, scratch): with (M+½)b = τ̃ = jπ + μ, N_{x,y} = n₀ ∓ 32b sin³μ cos μ(τ̃cos μ − sin μ)² + O(b²), n₀ = (64/3) sin³μ cos²μ[τ̃³cos μ − 3τ̃² sin μ − 6τ̃cos μ + 6 sin μ] (= −(8/3)τ̃⁵ sin³μ cos²μ·(−1)^j m₄(τ̃)); near the far corner N_x = 8b⁴ − (16/3)μ⁴b² − (64/15)μ⁸ + … . Recorded as guidance only.
4. **Positivity of Chebyshev-U coefficients on the edges** (measured, n ≤ 120): P_n(x,1) = −U_n + 2Σb_iU_i, P_n(1,y) = −(n+1) + 2Σb'_jU_j with all b_i, b'_j > 0. Would give D_y > 0 immediately. No proof found (b_i is a band sum of oscillating terms). Deferred; worth one attempt (generating-function or positive-definiteness argument).
5. **Bernstein route:** D_x ≥ 2M²[λ_n(1,1) − λ_n(cos(κ/M),1) − κ⁴Λ_n/24]/κ² reduces P1-tail to a 1 %-accurate upper bound of λ_n at one edge point plus an a priori bound; needs W1 with explicit constants (onset ≳ 10⁴). Deferred.
6. Not attempted: two-dimensional interval verification of H < 0 on {(θ, 1/M)}; estimated one focused round.

## 3. P2–P4: what worked

- **Rotated product form** D_M = 𝔡_{M+1}(u)𝔡_{M+1}(v') + 𝔡_M(u)𝔡_M(v') and the **generating-curve parametrisation** r ↦ (r mod 2M, r+M+1 mod 2M+2) of the node lattice (with reflections) reduce every lattice sum of a product majorant to a one-dimensional sum over r; blocks of M consecutive r see one period in u and a nearly constant v'. This gives X2-33 with explicit constants.
- **Translation formula** (X2-34): ℓ_a(P) is a box average of the corner kernel over shifts of the node angles. Exact at second order at the vertex.

## 4. P2–P3: heuristics, measurements, failed mechanism

- Shifted corner kernel near the ridge (nodes with w = π − 2t, τ = jπ + t, shifts a_i = −φ_i/M): G_n ≈ ±cos φ̄·cos(w/2)·M³/(4 sin³w)·[cos τ'/τ'² − sin τ'/τ'³], τ' = τ + ψ, φ̄ = (φ₁+φ₂)/2, ψ = (φ₁−φ₂)/2. Summing with the weights gives Ξ_n/M² → |cos φ̄|J(ψ) (signs as in X2-N35). Measured agreement within 0.006 at M = 202.
- **Failed mechanism (X2-N35):** sup over shifts is not at 0 (J'(0) ≈ −0.087, max J ≈ 0.5606 > c*).
- **Averaged bound B(ξ,ζ)** (X2-28 addendum W2): measured B < c* off the origin and B ≥ L_top; near the origin B ≈ c* − 0.0227(ξ²+ζ²) against the true 0.0256.
- **Why Jensen cannot be used globally:** for shifts of macroscopic size in both variables the shifted nodes that land near the torus corner contribute ∫dα/α ~ log M (weights sin w sin v no longer vanish there), so Ξ_n ~ M² log M·|sin a₁ sin a₂|; and for edge points with macroscopic θ₁ the averaged bound stays of order M² (true size M log M). Hence X2-33 for the far field and X2-34 only inside boxes with θ₁θ₂ log M ≪ 1; the X2-33 boxes (ϑ_n ~ log²M/M) satisfy this.
- Four-term route (direct proof of the L_top limit and of L_top < c*): not pursued; it needs a two-parameter family of integrals of absolute values, whereas the averaged route needs the one-parameter function J.

## 5. Computations run (2026-11-14; outputs in /tmp/x2r3, not committed)

| Command (from the topic directory) | Wall | Result |
|---|---|---|
| `python3 code/mp/research/x2r3_first_variation_arb.py --full --nmin 2 --nmax 24` | 0.2 s | closed forms overlap defining sums at every node; D_x, D_y > 0 |
| `python3 code/mp/research/x2r3_first_variation_arb.py --band --nmin 2 --nmax 3000 --out /tmp/x2r3/fv_band_2_3000.json` | 106 s | all signs certified; D_x, D_y > 0 for all 1500 degrees |
| `python3 code/mp/research/x2r3_checks.py transl` | 43 s (final version, box quadrature for n = 2; a first version with n ≤ 4 took 435 s) | errors ≤ 3e−29 |
| `python3 code/mp/research/x2r3_checks.py dlimit shift ucoef` | 11 s | d = 0.0512373057615; shift table; all band U-coefficients positive, n ≤ 120 |
| `python3 code/mp/research/x2r3_checks.py farfield jensen` | 100 s | bounds hold on grids; B table |

Scratch explorations `/tmp/x2r3/explore1–9.py` (sympy was installed into /tmp/x2r3/pylib for two symbolic expansions only) are not committed; their content is summarised in §2.

Runs needed: independent rerun of X2-32 (auditor); ball-arithmetic certificate of one instance of X2-N35.
