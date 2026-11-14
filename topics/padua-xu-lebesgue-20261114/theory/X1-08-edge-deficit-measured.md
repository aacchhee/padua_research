# PD-T?padua-xu-lebesgue-20261114-claude-08 — Size of the cancellation deficit away from the vertices (edge centre and near-vertex points)

ID kind: PD-T (measured claim with its own home; no proof claim).
Aliases: X1-08; edge-centre competitor; localization margin; second-highest local maxima of λ^Xu_n.
Split from: round X1-2 target T4 and the orchestrator's mid-round request (2026-11-14): "an expansion of λ^Xu_n(1, 0) (or the edge-centre maximum) to second order would quantify the localization margin".
Split into: none.

## Statement

Let Δ_n = ω_n(u)ω_n(v) − λ_n(x) ≥ 0 be the deficit of X1-04 (1). At a complementary grid point x = (cos(aπ/n), cos(bπ/n)), a + b ≡ n (mod 2), it equals L_n² − λ_n(x) (PROVED: X1-02 (b), X1-04). The following are **MEASURED** (float64, scope stated per item):

**(M1) Edge centre.** For n ≡ 0 (mod 4), the edge centre (0, 1) is a complementary grid point, and for n ∈ {4, 8, 12, 16, 20, 28, 32, 36, 44, 52, 60, 64, 128, 256, 512, 1024}

 Δ_n(0,1) = L_n² − λ_n(0,1) = 0.70711, 0.84462, 0.85583, 0.86825, 0.87818, 0.88218, 0.88457, 0.88490, 0.88688, 0.88774, 0.88848, 0.88874, 0.89041, 0.89098, 0.89120, 0.89127,

increasing in n along this list and apparently convergent to ≈ 0.8913. So in the measured range

 λ_n(0,1) = L_n² − Δ_n with 0.70 < Δ_n < 0.892:

the edge-centre value has the same log² **and the same log** coefficient as the vertex value (X1-07) and differs from it only at the constant order. The relative gap is g_n = Δ_n/L_n² ≈ 0.89 π²/(4 log² n)(1 + o(1)) (measured: 0.207, 0.107, 0.0697 at n = 4, 20, 60, reproducing the G1 screen).

**(M2) Near the vertex.** For n = 2^k, 3 ≤ k ≤ 10, at the complementary edge points at lattice distance a = 2 and a = 4 from the vertex (1,1), i.e. x = (cos(2π/n), 1) and (cos(4π/n), 1), the deficit grows logarithmically: Δ_n = 1.048, 1.395, 1.759, 2.129, 2.503, 2.877, 3.251, 3.626 (a = 2, n = 8..1024) and 0.845, 1.059, 1.434, 1.811, 2.194, 2.578, 2.963, 3.348 (a = 4), with increments per unit of log n tending to ≈ 0.5403 (a = 2) and ≈ 0.5557 (a = 4) at n = 1024. (For comparison only, not claimed: 16/(3π²) = 0.54038.)

**(M3) Heuristic limit (not proved).** The limit in (M1) is expected to be
 Δ_∞ = (1/(2π²)) ∬_{S} min(A(φ, φ′), B(φ, φ′)) dφ dφ′ over φ, φ′ ∈ (−π/2, π/2),
 A = |cot(φ−π/8) cot(φ′−π/8)| + |tan(φ−π/8) tan(φ′−π/8)|, B = the same with +π/8, S = the set where the signs of the two fiber terms differ (φ and φ′ in arcs of opposite type among the four arcs cut by ±π/8, ±π/8 + π/2 mod π).
Midpoint-rule values with M = 1001, 2001, 4001 points per axis: 0.89029, 0.89080, 0.89106 (slowly increasing; the integrand has integrable singularities).

## Definitions

As in X1-01 to X1-05. On the edge θ₂ = 0 (u = v = aπ/(2n)) the lift formula X1-01 (1) gives, with e_p = d_n((a − p)π/(2n)) and E(p, q) = e_pe_q + e_{p+2n}e_{q+2n},

  λ_n(cos(aπ/n), 1) = ¼ Σ_{(p,q)∈C_n²} |E(p, q) + E(−p, −q)|.   (1)

(Proof of (1): Σ_{F(ξ)} t = (|F(ξ)|/8) Σ_{γ∈Γ} t∘γ, and on the edge the eight terms are e_pe_q, e_{−p}e_{−q}, e_{p+2n}e_{q+2n}, e_{2n−p}e_{2n−q}, each twice. This identity is PROVED and is what the script evaluates.)

## Assumptions

float64 arithmetic; n and points exactly as listed. No claim outside the listed n.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Δ_n ≥ 0, Δ_n = L_n² − λ_n at complementary grid points, formula (1) | PROVED elsewhere (X1-04; routine step above) | not part of this record's status |
| (M1) edge-centre deficits for the 16 listed n | MEASURED | Checks |
| (M2) near-vertex deficits, n = 8..1024 | MEASURED | Checks |
| (M3) value of the limit and the integral formula | OPEN (heuristic; midpoint-rule values MEASURED) | no proof of convergence of Δ_n(0,1), no error bound for the quadrature |

## Depends on

X1-01, X1-04 for the exact identities evaluated. Nothing depends on this record: the maximizer theorem X1-05 does not use any measured margin.

## Checks

`python3 code/xu/research/x1_edge_deficit.py` (numpy 2.5.3, float64; run 2026-11-14, a few seconds): prints the tables above; for n ≤ 64 formula (1) agrees with Path B (`xu_kernel.XuFloat.value`) to the printed precision (`pathB_dev 0.0`); relative gaps at n = 12, 20, 28, 36, 44, 52, 60: 0.132157, 0.106632, 0.092758, 0.084093, 0.078016, 0.073389, 0.069749, matching `evidence/xu-g1-summary.json` (g_12 = 0.13216, g_60 as reported by the orchestrator, 0.0697). Output `/tmp/x1r2/edge_deficit.json` (not committed).

## Sources

`evidence/xu-g1-summary.json` and the orchestrator's message of 2026-11-14 (best non-vertex candidate always on an edge, at or near the edge centre; g_n = 0.207, 0.149, 0.107, 0.081, 0.0697 at n = 4, 10, 20, 40, 60).

## Proof or evidence

Measured values only; see Checks. Interpretation (not proved):

- At a point with u = u_i, v = u_j the products |t_{pq}| concentrate near the lift (i, j) and its seven Γ-images ("hot spots"). Far from the vertices the hot spots are at distance of order n from each other in the lift grid, and a term that is large for one hot spot is of size O(1/n) for the others, so the cancellation Σ_F|t| − |Σ_F t| is at most twice the small terms. Summing, Δ_n stays bounded: for the edge centre one gets Δ_n ≤ ½ (Σ_p (g_p g_{−p})^{1/2})² with g_p = 1/(n |sin((p − i)π/(2n))|), a Riemann sum of an integrable function (inverse square-root singularities), which suggests Δ_n(0,1) ≤ ½ (√2 · 4 ∫₀^{π/2} cos^{−1/2} / π)² ≈ 11 for large n. This sketch is **not** a proof (the Riemann-sum comparison is not written); it only explains why the deficit is O(1) and not of order log n.
- At bounded lattice distance from a vertex the hot spots are at bounded distance from each other, the cancellation reaches into the region that produces the log² term, and the deficit is of order log n, as in (M2).

Consequence for an asymptotic localization proof in the style of PR #27 (had X1-05 not been available): there is no relative margin (1 − δ) between the vertex value and the rest; the best non-vertex values are L_n² − O(1). A localization argument would have had to resolve an O(1) absolute margin against a log² n main term. This is the "hardest step" asked for in T4; X1-05 avoids it.

## Scope

Measured values at the listed n and points. Not a theorem about the second-highest local maximum of λ_n: the true non-vertex maximum for n ≢ 0 (mod 4) is slightly off the edge centre (G1 screen) and was not analysed.

## Open items

- Prove Δ_n(0,1) → Δ_∞ with the integral formula of (M3), or at least a uniform bound Δ_n ≤ C away from the vertices (route sketched above).
- Identify the limiting constants in (M2) (the measured a = 2 slope is close to 16/(3π²)).
- These are optional context for X1; no registered X1 target depends on them.

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher, in response to the orchestrator's mid-round message. The orchestrator's hypothesis was "the edge-centre value shares the (4/π²)log² leading term with a smaller log-coefficient"; the measurements instead indicate the same log-coefficient and a constant smaller by about 0.89. Preserved here as stated, with the measured correction.
