# Effective all-degree Padua argmax: campaign brief

Written by Claude (claude-opus-5-5) on 2026-11-03 at AC's request: "write a handout for codex for Effective all-n argmax … astra with ultra reasoning. Write all what you know about the problem, possible routes, and some easy gates. This campaign may be more adventurous."

This file is the knowledge base for the campaign. The binding instruction is [handoffs/01-work.md](handoffs/01-work.md). Nothing here is a new PROVED claim. The pilot numbers in §5 are MEASURED and are registered in [theory/argmax-effective-claude-01-pilot-measurements.md](theory/argmax-effective-claude-01-pilot-measurements.md).

## 1. The target

**PD-T099 (OPEN).** Use the even-checkerboard Padua points of degree n ≥ 2: B_jk = (cos θ_j, cos φ_k), with θ_j = jπ/n, φ_k = kπ/(n+1), 0 ≤ j ≤ n, 0 ≤ k ≤ n+1 and j+k even. Let λ_n = Σ_B |L_B| be the Lebesgue function of total-degree interpolation on these points. The conjecture is

  max_{[−1,1]²} λ_n = Λ_c(n), attained exactly at the two non-node corners.

The maximizing corners are (±1,−1) for even n and (−1,±1) for odd n, and the corner (−1,−1) is a non-node corner for every n.

**What is already proved** (main `440d107`):
- certified finite cases 2 ≤ n ≤ 16: PD-T209 (n = 2), PD-T162/166/169/174/177 (n = 3–7), PD-T181 (n = 8) and PD-T214 (n = 9–16), all relying on the certificate theorem PD-T210;
- the eventual theorem PD-T229, valid for n ≥ N_* with N_* existential and non-effective.

**The gap is therefore the finite bridge 17 ≤ n < N_*.** The goal is to close it, or to find a counterexample. A counterexample would be a degree n with a non-corner point where λ_n ≥ Λ_c(n). None has been seen in any measurement up to n = 400 (edges) or n = 200 (2-D, 75 degrees).

Corner values Λ_c(n) from the float64 evaluator, for scale:

| n | 2 | 3 | 4 | 8 | 12 | 16 | 17 | 20 | 24 | 32 | 48 | 64 | 96 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Λ_c | 3 | 3.7761 | 4.4097 | 6.2135 | 7.4494 | 8.4074 | 8.6179 | 9.1971 | 9.8725 | 10.9936 | 12.6888 | 13.9732 | 15.8985 |

PD-T156–159 (PROVED): Λ_c = (4/π²)log²n + b log n + O(1), with |error| ≤ 68 and b = (8/π²)(γ + log(8/π)). In addition, |Λ_c − L_n²| ≤ 54, where L_n = (2/n) Σ_{r odd ≤ n} d_r csc(rπ/2n).

## 2. Exact structure to build on

**The kernel** (PD-T101; check against `topics/padua-argmax-alln-20261101/code/maj.py` and `check.py`):
- L_B(x) = w_B Σ_{a+b≤n} c_ab T_a(x₁)T_b(x₂)T_a(B₁)T_b(B₂), with weights w_jk = 2ε_jη_k/(n(n+1)) (half factors at the range ends).
- c_ab = h_a h_b, where h_0 = 1 and h_k = 2. The exception is c_{n,0} = 1: the x-mode (n, 0) is halved.

**Reflected-lattice identity** (PD-T215 = gated-codex-01). Write G_{ση} = G_n(θ + σa_j, φ + ηb_k), with σ, η ∈ {±1}, a_j = θ_j and b_k = φ_k. Then

  λ = Σ w |¼ Σ_{σ,η} G_{ση}|,  S = Σ w ¼ Σ_{σ,η} |G_{ση}|,  Δ = S − λ ≥ 0.

Δ is bounded below by the two projected pairwise defects Q_v and Q_h. At corners the four copies coincide (λ = S = Λ_c). On edges they coincide in pairs.
- In phase form: S_n(α,β) = N⁻¹ Σ_{Γ⁻} |F_jr|, with F_jr = ½(−1)^j G_n(jπ/n + α/n, rπ/m + β/m), m = n+1, N = nm, Γ⁻ the odd cosets, and a(α,β) = ½(cos α + cos β).
- Rhombus form of the kernel (PD-T101): D_n(u,v) = U_{n+1}(S)U_{n+1}(T) + U_n(S)U_n(T), with S = (u+v)/2 and T = (v−u)/2.
- The lattice is rank-1, the generating curve s·(n+1, n)·π/(n(n+1)).

**Exact corner data** (PD-T227 = gated-13):
- the zero/sign mask of the cardinals at c = (−1,−1), exact cardinal gradients, and L_00(c) = (−1)ⁿ/m;
- the inward first variation is linear: D_{(s,t)}λ_n(c) = sA_n + tB_n, with explicit sums for A_n and B_n.

**Exact edge formula** (PD-T185) on all four edges, with every removable limit given as a Chebyshev divided difference. Exact row identities (PD-T226): signed and absolute periodic rows, a cotangent sign-interval formula, and an endpoint harmonic bound.

## 3. The eventual proof (PD-T229) and where it loses effectivity

| Step | Record | Content | Effective? |
|---|---|---|---|
| Global primitive | PD-T216 (gated-02) | S_n ≤ a(α,β)Λ_c + C log(n+1) for \|α\|+\|β\| ≤ π | No numerical C |
| Local primitive | PD-T217 (gated-03) | S_n ≤ aΛ_c + Cρ²log(n+1) + Cρ, ρ ≤ ρ₀ | No numerical C, ρ₀ |
| Explicit local primitive | PD-T221 (gated-07) | S_n ≤ aΛ_c + 242000ρ²log(n+1) + 2048ρ^{3/2} + 640ρ(1+log(n+1))/n, ρ ≤ 1/64 | Explicit, but about 10⁶ too large |
| Compact gaps | PD-T211/212, PD-T218 (gated-04), PD-T230 | sup over the complement of δ-corner squares ≤ Λ_c − c_δ + o_δ(1), with c_δ = δ²(1−cos(δ/2))/(16π²) | o(1) not explicit; c_δ tiny |
| Finite defects | PD-T219 (gated-05), PD-T222 (gated-08), PD-T224 (gated-10) | Q ≥ d_δ for n ≥ ⌈16π/δ⌉; Q ≥ 1/1536 at ≥ 4π/n from the endpoints (n ≥ 48); Δ ≥ 1/4096 at every non-corner odd coset (n ≥ 48, ρ ≤ 1/64) | Explicit, but far below the true gaps |
| Shrinking boxes | PD-T223 (gated-09) | sup outside the four 4π/n angle-corner boxes ≤ Λ_c − 1/3072 for n ≥ N_* | Non-effective (proof by contradiction along sequences) |
| Corner localization | PD-T225 (gated-11) | every global maximizer has actual-corner phase → 0 | Non-effective |
| Reflection-first local | PD-T228 (gated-14) | λ_n(z_n(α,β)) ≤ aΛ_c + 237000ρ²log(n+1), ρ = α+β ≤ 1/64, with α, β ≥ 0 inward | Explicit; strict local comparison needs log n ≥ 10⁷ |
| Assembly | PD-T229 (gated-15) | combine PD-T225 (ε = 1/64) with PD-T228 | N_* ≥ max(N_loc, e^{10⁷}) |

Two facts matter here:
- The primitive S has a **positive linear axis cusp** at the corner (PD-T220; PD-N079 refutes coset maximality and a purely quadratic gain for S). Near corners the reflections must stay inside the absolute value ("reflection first", PD-T228).
- The previous campaign's effectivity test projected about 1.33 × 10¹⁴ for the localization step of the existing proof (PD-T208, T4).

## 4. Measured quantitative landscape (all MEASURED; IDs as stated)

These numbers are what an effective proof has to beat.

- **Runner-up: the central vertical edge.** The gap Λ_c − (cell maximum) is 0.6387, 0.5832, 0.5665 and 0.5571 at n = 12, 24, 48, 96 (PD-T207), and 0.550440 at n = 399 (PD-T208, T1). The proved limit is g ≈ 0.548514842 (PD-T192), with certified bracket 0.548504986190 < g < 0.548525055355 (PD-T188).
  - The vertical-edge gap profile is smallest at the centre and rises toward both ends: about 0.87 at 25 %, 1.4–1.5 at 10 %, and growing like log n in the cells next to the node corner.
  - Centre-minimality of g_v is OPEN.
- **Horizontal edges.** Smallest gap about 0.95–0.99 (n = 12…96), near the centre (PD-T207). Centre-minimality of g_h is OPEN.
- **Interior.** Gap about 1.75 over [π/4, 3π/4]² for n = 8…48 (PD-T206). Raw scaled interior profiles do not stabilize: T2 was killed, with 32/81 positions changing by more than 0.05 between n = 64 and 128 (PD-N082).
- **Corner zone.** The raw degree-independent angular profile was killed (T3, PD-N083). There is no second near-zero point in n = 16/64/256 samples.
- **Majorant near cosets.** max S exceeds Λ_c by at most 1.4e-3 (n = 3), falling to 9.2e-5 (n = 40), at about 0.01–0.02·π/n off the coset (PD-T206). This is consistent with the O(log⁻²n) local excess of PD-T217.
- **Pilot G2** (this brief, MEASURED). The true local remainder constant is K(n) = sup_{0<ρ≤1/64} (λ_n(z_n) − aΛ_c)/(ρ² log(n+1)) at c = (−1,−1).
  - K(n) = 0.289 (n = 17), 0.278 (24), 0.259 (48), 0.246 (96), 0.237 (192), maximal on an axis (β = 0).
  - Strict local comparison on an axis needs K < Λ_c/(4 log(n+1)). That budget is 0.75 at n = 17 and 0.92 at n = 192.
  - On the diagonal both K and the deficit halve.
  - So the true margin factor is about 2.6–3.9, against the proved constant 237000. **The local corner problem is not tight; the proof constants are.**
- **Pilot G3** (MEASURED).
  - The true C in PD-T216 is sup (S − aΛ_c)/log(n+1) ≈ 1.59 (n = 17), 1.52 (48), 1.48 (96), attained at (α,β) = (π/2, −π/2), where a = 0.
  - The far-from-coset majorant margin −sup_{ρ≥1/2}(S − Λ_c) is 0.147 (n = 17), 0.253 (48), 0.340 (96).
  - So S alone separates from Λ_c away from cosets, but only by 0.15–0.34 at moderate n. Near non-corner cosets the defect Δ must do the work; there the true λ gap is at least about 0.55.

## 5. Finite certification capacity

PD-T210 is a tensor Bernstein closed-square certificate. Bound leaves need every coefficient's absolute sum below the corner lower bound. Corner leaves allow equality only at the exact corner vertex. Cardinals come from PD-T101 with rational Machin/Taylor cosine enclosures in 192-bit outward integers.

The code is `topics/padua-argmax-alln-20261101/code/part3/finite_general_run.py` (producer), `finite_general_check.py` (checker) and `finite_general_controls.py` (corruption controls).

Earlier costs: n = 9–16 needed 42–96 leaves, depth ≤ 8, and 1.3–32 s of discovery each.

**Claude pilot** (MEASURED; scratch only; no independent replay, so these degrees are **not** certified):
- n = 17: complete cover, 106 leaves (104 bound, 2 corner), depth 8, producer 35 s. `finite_general_check.py` returned accepted = true in 32 s.
- n = 20: complete, 132 leaves, depth 10, 87 s.
- n = 24 and 32: see the pilot record (still running when this brief was first written).

The cost grows roughly like n^{5–6} in this pure-Python implementation. Projection: n ≈ 32 in minutes, n ≈ 64 in hours, n ≈ 100 in days. A C/FLINT/arb port, parallel leaves or a coarser first pass with S-majorant discards (an extension of IDEA-320, the global-max-only certifier) could give 10–100×. AC has NTNU servers (syvert0/1/2) if long runs are needed; ask AC before using them.

**Realistic aim: n_cert of order 60–150.** An effective proof therefore needs a threshold n₀ ≲ n_cert. That means sharp constants, not order-of-magnitude bounds.

## 6. Retained failures and traps (do not repeat)

- **PD-N078:** the tie-inclusive nearest-corner ordering O-Lt fails at n = 4.
- **PD-N079:** coset maximality of S and a purely quadratic local gain fail.
- **PD-N080:** the common-phase centreward edge translation E-P fails at n = 12.
- **PD-N081/082/083 (MEASURED):** the O-R screening, T2 and T3 profile criteria fail.
- **PD-T226:** exact row resummation leaves negative cotangent partial sums uncontrolled. The previous campaign stopped there.
- The explicit constants 242000/2048/640 (PD-T221) and 237000 (PD-T228) are valid but useless for the bridge. Expect to redo the local analysis, not to polish it.
- Finite-defect lower bounds of 1/1536 and 1/4096 are three to four orders below the true gaps. Effective arguments must be within small constant factors of the truth.
- Raw scaled profiles converge slowly because of log-graded terms. Any profile method must expand in powers of log n (log²n·A + log n·B + C + o(1)), not in raw scaled coordinates.
- **Parity and corners:** the maximal corners depend on the parity of n. Node corners have λ = 1. Removable kernel values at coincidences must be retained, and edges carry the exceptional halved x-mode.
- Whole-cell comparisons survive where pointwise ones fail: PD-T231 proves all ten E-C comparisons at n = 7, 12. All-n E-C is OPEN.

## 7. Possible routes (adventurous; not exclusive)

**R1: effective S−Δ with sharp constants.** Re-run the PD-T229 architecture with every constant explicit and close to the truth:
- the global C ≈ 1.6 rather than "absolute";
- the local K ≈ 0.3 rather than 237000;
- defects about 0.5 rather than 1/4096;
- effective replacements for the contradiction arguments of PD-T223/225.

Tools: explicit Euler–Maclaurin or Riemann-sum remainders for shifted lattice sums of |G_n|, computed in rhombus coordinates; sharp 1-D Dirichlet-sum bounds; the PD-T159 comparison with L_n² (redone with sharp constants). Risk: getting all the error terms below about 0.15–0.5 at n ≈ 100 is very demanding.

**R2: computer-assisted uniform-in-n asymptotics (near field / far field).** Around the evaluation point, split the lattice sum into:
- a *near field*: finitely many terms within R cells of each reflected peak. Each term is an explicit smooth function of the scaled position and h = 1/n. Enclose it rigorously with Taylor models or interval arithmetic in (position, h) ∈ cell × [0, 1/n₀].
- a *far field*: an explicit smooth tail whose sum is bounded by integrals with explicit remainders. The log²n and log n structure lives here and is simple (products of harmonic-type sums).

This avoids crude constants exactly where they hurt (near the peaks). Combine with the finite certifier for n < n₀. Decide R by testing how far the far-field bound is from the truth.

**R3: exact comparison / pairing (no asymptotics).** Reduce the square to edges and corners by exact inequalities that hold for every n:
- interior cell maximum ≤ adjacent boundary maximum (measured: strip maxima lie on the boundary, PD-T207);
- along edges, the whole-cell centreward comparison E-C (PD-T231; finite proof at n = 7, 12);
- central edge envelope versus the corner, which needs only the 1-D gap g ≈ 0.55 on the explicit edge formula PD-T185. The 1-D problem may yield to classical 1-D Lebesgue-function techniques.

Avoid pointwise translations (PD-N080) and order statements (PD-N078). Whole-cell, sign-pattern or majorization comparisons are the live forms.

**R4: generating-curve / 1-D reduction (IDEA-319, never tested).** Padua points lie on the curve γ(t) = (cos(n+1)t, cos nt). The non-node corners are **not** on the curve for the parities where they are maxima (check this). In rhombus coordinates the lattice step is ((2n+1)τ/2, −τ/2), with τ = π/(n(n+1)). Product-to-sum splits sin((n+1)S)sin((n+1)T) into a lattice-independent envelope and an oscillating term. Kill test as in the IDEA: no cell-wise sign-stable envelope at n = 4.

**R5: extremal-problem / duality view (speculative).** λ_n(x) = max{|p(x)| : p ∈ Π_n, |p(B)| ≤ 1}. The corner is extremal for the sign pattern ε* = sign L_B(c), whose exact mask is PD-T227. Look for a comparison family of polynomials, or a positivity (sum-of-squares or Bernstein) certificate for Λ_c ± Σε_B L_B that is uniform in n via structure (reflection symmetry, rank-1 lattice). Treat this as a wild card; the bounded attempt is to find any all-n mechanism.

**R6: hybrid.** Use R2 or R1 for n ≥ n₀ in the corner zone only, and R3 for the rest of the square. The corner zone has the largest true margin factor (about 3), so it may be the first piece that can be made effective.

## 8. Easy gates (cheap, decisive; run first; criteria pre-registered in the handoff)

- **G0, finite extension.** Run the PD-T210 certifier for n = 17…24 (or further), with an independent replay by a different subagent. Every success is a new PROVED degree. This shrinks the bridge and measures the cost exponent.
- **G1, certifier scaling.** Fit time and leaves against n from G0. Project the feasible n_cert in 24 h and in 7 days, pure Python and estimated for a FLINT/C port.
- **G2, local corner constant** (pilot done for n ≤ 192). Extend to n ≤ 1000 and to the second corner and parity. Also measure the true physical-radius validity: the largest ρ where λ < Λ_c along each direction.
- **G3, global primitive constant and far margin** (pilot done for n ≤ 96). Extend, and map S − Λ_c over phase space to choose a ρ₀ for R1.
- **G4, true defect sizes.** Measure the minimum of λ's gap, and separately of Δ, near every non-corner odd coset class (edge, strip, interior) for n = 17…200. Compare with the proved 1/1536 and 1/4096.
- **G5, effectivity projection.** Using G2–G4, project the n₀ that R1 could reach with constants within a factor 2 of the truth. Compare with G1's n_cert.
- **G6, E-C screen.** Run the whole-cell centreward comparisons and interior-to-boundary domination for n = 13…60 (float), then exact checks at a few degrees.
- **G7, R4 kill test** at n = 4 (IDEA-319).
- **G8, literature.** Read the 1-D Lebesgue-function maximum-location literature before transferring any technique, and record LIT entries:
  - Brutman's survey (J. Inequal. Appl. 1997) and Brutman 1978 (SIAM J. Numer. Anal.);
  - Günttner on Chebyshev nodes;
  - Ehlich–Zeller;
  - the midpoint maximality of trigonometric interpolation;
  - Kolomoitsev–Lomako's discretization lemma (LIT-379).

  All citations above are to be verified; none is read yet in this repository.

**Decision rule.**
- If G5's projected n₀ is at most G1's n_cert, the main line is R1/R2 plus finite certification.
- If not, either push n_cert up (port the certifier), or put the effort into R3/R4/R5.
- In any case R6 is worth one round.
