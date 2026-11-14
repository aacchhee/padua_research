# X1 round 2 — working record (researcher: Claude Fable 5.2, xhigh; 2026-11-14)

Subagent of the orchestrator; no git commands were run (rules as read by the orchestrator at `2d60e22`). Files written this round: `theory/X1-01` … `X1-08`, this file, and `code/xu/research/x1_*.py` (outputs in `/tmp/x1r2/`, not committed). Statuses follow `agents/WORKFLOW.md`; every PROVED item is "audit pending".

## 0. Outcome in one paragraph

In the rotated angles u = (θ₁+θ₂)/2, v = (θ₁−θ₂)/2 the Xu nodes are a tensor grid of 2n equispaced points per variable, and Xu interpolation is the Γ-symmetrized tensor-product trigonometric interpolation on that grid (X1-01). The Lebesgue function is therefore bounded by the product of two one-dimensional trigonometric Lebesgue functions, λ_n(x) ≤ ω_n(u)ω_n(v) ≤ L_n² (X1-04), where L_n = (1/n)Σ_{k=1}^n cot((2k−1)π/(4n)) is the Lebesgue constant of interpolation at the n zeros of T_n (X1-02). At the non-node vertices all fiber terms have one sign, so λ_n(v) = L_n² exactly (X1-03). Hence **Λ^Xu_n = L_n² for every n ≥ 1**, and a two-term sign cancellation shows that **for n ≥ 2 the maximizers are exactly V*** (X1-05). With a two-sided n⁻⁴ enclosure of L_n (X1-06) this gives the expansion with b = (8/π²)(γ + log(8/π)), c = (4/π²)(γ + log(8/π))², 0 < R_n < (log n + 1.55)/(18n²), n₂ = 1, N = n (X1-07). Both parts of BCDMV Conjecture (17) follow for even n, and the odd-n variant too.

## 1. Result table

| ID (provisional `PD-T?padua-xu-lebesgue-20261114-claude-NN`) | File | Statement | Status |
|---|---|---|---|
| 01 | theory/X1-01-tensor-lift.md | ℓ_ξ(cos(u+v), cos(u−v)) = Σ_{(p,q)∈F(ξ)} d_n(u−u_p)d_n(v−u_q); unisolvence | PROVED |
| 02 | theory/X1-02-trig-lebesgue-function.md | ω_n ≤ L_n, equality iff midpoint (n ≥ 2); midpoint signs χ; L_n = Chebyshev-zero Lebesgue constant | PROVED |
| 03 | theory/X1-03-vertex-value.md | ℓ_ξ(v) = w_ξ(−1)^{r′}(2+z_{r′}+z_{s′})/(z_{r′}−z_{s′}); λ_n(v) = L_n², v ∈ V*, n ≥ 1 | PROVED |
| 04 | theory/X1-04-exact-lebesgue-constant.md | λ_n = ω_n(u)ω_n(v) − Δ_n ≤ L_n²; Λ^Xu_n = L_n², n ≥ 1 | PROVED |
| 05 | theory/X1-05-argmax-set.md | argmax λ_n = V* for every n ≥ 2 (n = 1: λ ≡ 1) | PROVED |
| 06 | theory/X1-06-chebyshev-constant-expansion.md | L_n = A_n + (4/π)Σ(−1)^{j−1}G(nj); A_n + π/(72n²) − 7/(240πn⁴) < L_n < A_n + π/(72n²) | PROVED |
| 07 | theory/X1-07-expansion-and-conjecture-17.md | expansion, b, c, remainder, n₂ = 1; Λ ≤ ((2/π)log n + 1)²; Conjecture (17); Λ_c^{Padua}(n) − Λ^Xu_n → κ | PROVED |
| 08 | theory/X1-08-edge-deficit-measured.md | edge-centre and near-vertex deficits | MEASURED (limit formula OPEN) |

IDs 09–20 are unused.

## 2. T0 — novelty kill test (novelty-gate-X1, row X1-C1)

**Question.** Is λ^Xu_n(v) a Padua corner value Λ_c(m), or a fixed affine/integer combination of Padua corner values or of one-dimensional Lebesgue-type sums, under an index map?

**Procedure** (`code/xu/research/x1_t0_pslq.py`, 60 digits, n = 2..40; Xu value from Path B `xu_kernel.vertex_value`, Padua corner value from the exact positive sum PD-T159 (3)):
1. nearest Padua corner value among |m − n| ≤ 3;
2. PSLQ (max coefficient 10⁶) on [λ_n, Λ_c(n−1), Λ_c(n), Λ_c(n+1), 1];
3. PSLQ on [λ_n, L_n², L_n, 1].

**Results (MEASURED).**
- 1: the gap to the nearest Λ_c(m) is 0 only at n = 2 (λ₂ = 2 = Λ_c(1), a coincidence of two small rationals); for n ≥ 3 it is between 0.016 (n = 11, m = 8) and 0.62 (n = 40, m = 37), nonzero, and shows no pattern.
- 2: a relation is returned only for n = 2, 3, 4 (`[1,0,0,0,−2]`: λ₂ = 2; `[0,1,0,0,−3]`: Λ_c(2) = 3, not involving λ; `[4,−6,0,0,9]`: λ₄ = 2 + √2 and Λ_c(3) both lie in ℚ(√2)). For 5 ≤ n ≤ 40: none. These are low-degree algebraic coincidences and not an index-map identity.
- 3: the relation `[1, −1, 0, 0]`, i.e. λ_n = L_n², for all 39 values of n.
- Λ_c(n) − λ^Xu_n = 1.0, 0.99836, 0.99551, 0.99226, …, 0.94738 (n = 2, 3, 4, 5, …, 40), slowly decreasing.

**Verdict.**
- Against Padua corner values: **not killed** — λ^Xu_n(v) is not a Padua corner value nor an integer combination of neighbouring ones (measured, 5 ≤ n ≤ 40).
- Against one-dimensional sums: **reduction found and proved** — λ^Xu_n(v) = L_n² (X1-03), the square of the one-dimensional sum L_n of PD-T159/PD-T270. In fact the positive sum for λ^Xu_n(v) is literally PD-T159's "same-mesh reference" F_n (its eq. (4)), which that record proves equal to L_n² (eq. (5)). So the *vertex expansion* part of X1-C1 is a corollary of merged results (PD-T159 (5) + PD-T270) once the identification is made; with X1-06 it is sharper than PD-T270 allows.
- Structural explanation: the Padua corner value is F_n plus the deformation caused by the second mesh π/(n+1) (PD-T269 (4)), whose limit is κ. Xu points use the same mesh π/n in both variables, so the deformation is absent: Λ_c^{Padua}(n) − Λ^Xu_n → κ (X1-07 (e), PROVED from PD-T269). Same b, constants differ by κ.
- Per the gate ("a corollary relation, if found, is recorded and used, and only the residual is claimed"): the residual claims of this round are the identification itself, the exact Lebesgue constant (X1-04) and the maximizer set (X1-05), none of which follows from the Padua records.

## 3. Routes

| Route | Outcome | Obstruction / note |
|---|---|---|
| R1. Kernel route: BCDMV kernel at (1,1) ⇒ K* = (−1)^r(2+z_r+z_s)/(z_r−z_s) (correction term vanishes), signs exact, positive sum = PD-T159's F_n = L_n² | Works; kept only as a consistency remark in X1-03 | Depends on the literature kernel formula (LITERATURE + G0), so it was replaced by R2 as the proof of record |
| R2. Tensor lift (rotation by 45° in angle space; symmetrization by Γ = ⟨τ, s, c⟩) | Adopted: X1-01 to X1-05 | Equivalent identity probably published (Li–Sun–Xu 2009, digest-level read; see X1-01 Sources). No novelty claimed for the lift |
| R3. BdMV's method with sharpened constants (T3 as assigned) | Not pursued | Superseded by R2: BdMV split the kernel into pieces and bound each (factor 8); the lift gives the sharp constant by one triangle inequality |
| R4. PR #27 architecture for the argmax (corner expansion + localization + finite certificates; T4 as assigned) | Not needed; plan replaced by the proof X1-05 | Would have faced an O(1) absolute margin: the best non-vertex values are L_n² − O(1) (X1-08, MEASURED), so there is no relative margin (1 − δ). This is the hardest step such a plan would have had |
| R5. Second-order expansion of the edge-centre value (orchestrator request) | Exact deficit formula and measurements (X1-08); proof of the limit not attempted | Needs a Riemann-sum comparison for a double sum with min(·,·) and integrable singularities; route sketched in X1-08. Not needed for any registered target |
| R6. Same lift for Padua points | Considered, fails | The checkerboard of the (n+1)×(n+2) grid has meshes π/n and π/(n+1); in the oblique lattice coordinates the period group is cyclic of order 2n(n+1) (the generating-curve structure), not a product of two cyclic groups aligned with the axes, so there is no tensor factorization and no product majorant. IDEA disposition: abandoned for Padua (reason: no product structure) |

## 4. T4 — argmax (G3) and where the other maxima are

- The requested plan is replaced by the all-n proof X1-05 (onset n₃ = 2, nothing below it except the trivial n = 1). No lemma of PR #27 is used, so nothing is CONDITIONAL on it.
- Location of the second-highest values (G1 screen `evidence/xu-g1-summary.json`, n ≤ 60; orchestrator message): always on an edge, at or near the edge centre (exactly the centre for n ≡ 0 mod 4). Explanation from X1-04 (1): λ_n = ω_n(u)ω_n(v) − Δ_n; the product reaches L_n² at every complementary grid point (aπ/n, bπ/n), a + b ≡ n (mod 2), so the competition is decided by the deficit Δ_n alone. Measured (X1-08): Δ_n ≈ 0.71–0.89 at the edge centre (apparent limit ≈ 0.8913), and growing like ≈ 0.54 log n at bounded lattice distance from a vertex. So the runner-up is far from the vertices, with value L_n² − 0.89…, i.e. the same log² and log coefficients as the vertex and a smaller constant. The orchestrator's working hypothesis (smaller log coefficient) is not supported by the measurements; relative gaps g_n = Δ_n/L_n² reproduce 0.207, 0.107, 0.0697 at n = 4, 20, 60.

## 5. Checks run (all on 2026-11-14, this machine; Python 3.13.18, mpmath 1.4.1, numpy 2.5.3, python-flint 0.9.0)

| Command (from the topic directory) | Result |
|---|---|
| `python3 code/xu/research/x1_lift_exact_check.py --nmax 10` | arb 512 bits, Path A vs lift, n = 1..10, all nodes, 3 points each, and λ(v) = L_n² at V*: all enclosures contain 0, max radius 1.8e−133; `ALL OK` |
| `python3 code/xu/research/x1_lift_check.py` | 40 digits, Path B vs lift, n = 1..12, 6 points each: `WORST 1.9905e-38`; product bound asserted |
| `python3 code/xu/research/x1_vertex_check.py --nmax 200` | 60 digits, every n = 2..200 (even at (1,1), odd at (1,−1)): Path B vertex value vs L_n², worst relative deviation `3.0732e-59`; general Path B at all vertices n ≤ 12: `4.2005e-60`; sign-rule failures 0 (88 s) |
| `python3 code/xu/research/x1_argmax_check.py --nmax 12 --fmax 24` | complementary points n = 2..12: λ < L_n² off V*, witness failures 0; float grids n = 2..24: `worst lam-prod 1.05e-13; worst prod-L2 5.15e-14`, argmax = V* |
| `python3 code/xu/research/x1_1d_check.py --nmax 2000` | exact series to `4.3104e-41` (15 values of n); enclosure X1-06 (2) for 444 values n ≤ 1991; kernel inequalities; ω = P(cos u), monotone |
| `python3 code/xu/research/x1_constants.py` | arb enclosures of c₁, b, c; X1-07 bounds verified for n = 1..300 |
| `python3 code/xu/research/x1_t0_pslq.py` | §2 above |
| `python3 code/xu/research/x1_edge_deficit.py` | X1-08 tables |

Script SHA-256 (final versions; every command above was re-run on exactly these files):

```text
927bc8a2b5caaf398c229a8966e221954d63c2f9b433663f048b8ac47b947ac4  code/xu/research/x1_1d_check.py
44a6218982de838d77b5eb8a07a17c17979ffe3d57442ea0b6a071f91b6c7ec7  code/xu/research/x1_argmax_check.py
66f20600748106bfcab6758031dfcc2ed41a1cd36624ad76ea19589d2445529f  code/xu/research/x1_constants.py
b1b87d80df1f04c2501d610d8f56ac96bfc2007a965f08d9c6fff9da320eb841  code/xu/research/x1_edge_deficit.py
4051b10d9aec57502c565d879d43902d84e7fd2a27197fb43905f463f57b2cb8  code/xu/research/x1_lift.py
eccf6bbf7d543557e466e46ba75f49f0e3e2c975fa2477e21de12949d337f0c5  code/xu/research/x1_lift_check.py
6d969b2fa222f90fa7f130efb5999f3e73987a4dcf0ab8db6be143d0b7190256  code/xu/research/x1_lift_exact_check.py
a05e54bdd178ba7883056e1cd9708cee4fc44fd26793c2cfd8f11340c6b52012  code/xu/research/x1_t0_pslq.py
9160107750f9cf5bf23dc0922d473d86d5adaeef9611dff4ee0dabd2123df456  code/xu/research/x1_vertex_check.py
```

Runs needed (not executed): none for the proofs. Optional: the orchestrator's `evidence/xu-vertex-values.json` (n ≤ 400) can be compared with L_n² by a one-line extension of `x1_vertex_check.py` (`--nmax 400`, about 10 minutes).

## 6. Literature notes made this round (for the orchestrator; not LIT records)

- WebSearch (2 queries, 2026-11-14): "Xu points Lebesgue constant equals square of Chebyshev Lebesgue constant …" and "Li Sun Xu Cubature formula and interpolation on the cubic domain Lebesgue constant …": only already-known items plus Li–Sun–Xu 2009.
- Li–Sun–Xu, NMTMA 2 (2009) 119–152, arXiv:0808.0180, read **as WebFetch digests of the ar5iv HTML, characters 0–100k and 200k–500k of 905k** (not a fulltext read; no page numbers): §3.3 builds interpolation on [−1,1]² from lattice trigonometric interpolation and a symmetrization operator 𝒫 (Thm 3.9 trigonometric, Thm 3.10 algebraic); the digest reports that for odd n the scheme is that of their ref. [19] and for even n it differs from [19] by one point; it reports no Lebesgue-constant statement in §3. Consequence: X1-01 should be presented as a re-derivation; the claims to gate for novelty are X1-03 (b), X1-04 (3), X1-05.
- Classical one-dimensional facts quoted as context only (unread): Chebyshev Lebesgue constant formula and its π/(72n²) correction (Ehlich–Zeller, Günttner, Rivlin). X1-02 (d) and X1-06 prove what is used.

## 7. Open obligations

1. Audit of X1-01 … X1-07 (Opus 5.5 xhigh, separate thread). Points that deserve the closest look: X1-01 §3 (the symmetrization table, both parities); X1-02 §3 (sign pattern on [0, π/(2n)) and the monotonicity of P); X1-05 Steps 2–3 (sign identity and the two witness pairs); X1-06 §§4–5 (block bookkeeping, Wallis / PD-T270 normalization).
2. Novelty gate re-run for the exact statements Λ^Xu_n = L_n² and argmax = V* (forward citations of BCDMV/BdMV were searched by the orchestrator; add Li–Sun–Xu 2009 and its citing papers, and the Xu 2012/2017 JAT papers listed as unread in `literature-xu-mp.md` §3.3).
3. Gates: G2 and G3 verdict lines in `gates.md` are the orchestrator's to append (G2: closed form, expansion, and the 50-digit n ≤ 200 check are in X1-03/X1-07; G3: all-n analytic proof, no certificate range).
4. Global ID allocation, `ID_CROSSWALK.md` / `PROOF_STATUS.md` rows, LOG and results entries: orchestrator.
5. Optional mathematics: X1-08 (M3) limit of the edge-centre deficit; uniform O(1) bound for Δ_n away from the vertices.

## 8. Ideas preserved (not pursued)

- I-a (deferred): the deficit function Δ_n as a tool for the full landscape of λ^Xu_n (number and location of local maxima; cf. IDEA-048 interior-maxima geometry). Resume if AC wants the maxima count for Xu points.
- I-b (deferred): the Li–Sun–Xu even-n scheme with one more point, and their cube points in three variables: does a symmetrized-tensor structure give exact Lebesgue constants there? Needs the fulltext first.
- I-c (abandoned, see R6): product majorant for Padua points.

## 9. Recommendation for the next X1 round

No further Fable research round is needed for X1's registered targets: G2 and G3 are met by written proofs for every n. Next: the Opus 5.5 xhigh audit (already planned) and the novelty re-gate, both Opus-level work. A Fable round would only be justified if AC wants the optional X1-08 asymptotics (edge-centre constant) or the Xu maxima-count problem (I-a); otherwise the X1 budget can be released to X2.
