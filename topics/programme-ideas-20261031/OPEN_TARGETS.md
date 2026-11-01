# Open proof targets — programme-ideas campaign

2026-11-01, response-01 addendum (claude-opus-5-5), at AC's request "state clearly what needs to be proven, we'll make a few attempts". Every item is a precise statement that is **not** proved in this repository. Each says what is known, what would count as done, and a suggested first route. Order within each group is by expected tractability. Notation and conventions are those of the cited THEORY records in `theory/`.

Conventions used throughout. Padua points of degree n (first family, as in `checks/code/gen4/gen4_tests.py:padua`): B = (cos θ_j, cos φ_k), θ_j = jπ/n, φ_k = kπ/(n+1), 0 ≤ j ≤ n, 0 ≤ k ≤ n+1, j + k even, weights w_B = 2ε_jε_k/(n(n+1)) with ε = ½ at the ends of each range and 1 otherwise. λ_n(x) = Σ_B |L_B(x)| is the Lebesgue function of total-degree interpolation on Pad_n; Λ_c(n) its maximum over the four corners; U_m(t) = sin(mt)/sin t.

## Priority 1 — short, probably within reach

### A1. Closed form of the corner value (feeds PD-T?programme-ideas-claude-04)

**Statement.** For every n ≥ 1 and every corner c = (cos θ_c, cos φ_c), θ_c, φ_c ∈ {0, π},

  λ_n(c) = Σ_B w_B | D_n(θ_c + θ_j, φ_c + φ_k) − T_n(cos θ_c)(−1)^j |,  D_n(u, v) := U_{n+1}(S)U_{n+1}(T) + U_n(S)U_n(T), S = (u+v)/2, T = (v−u)/2.

Known: MEASURED agreement with the O(Nn) Lagrange formula to 2.1e-13 for n = 3…64, all corners (`checks/code/decisive/gen4-2/t2_onepage.py`). Done when: a written proof. Route: start from the Padua Lagrange formula L_B(x) = w_B(K_n(x, B) − T_n(x_1)T_n(B_1)) (Bos–Caliari–De Marchi–Vianello–Xu 2006; LITERATURE, to be checked at the theorem level), write the product-Chebyshev reproducing kernel K_n on the rhombus j + k ≤ n of cosine products, and sum it at a corner, where cos(aθ_c) = (±1)^a turns the four-fold cosine sum into a Dirichlet-type sum in θ_c + θ_j and φ_c + φ_k.

### B5. The pattern commutant is generically span{I, H_x, H_y} (complements PD-N?programme-ideas-claude-04)

**Statement.** Fix n ≥ 2. For nodes and weights outside a proper real-analytic subset of {Π_n-unisolvent N-point sets} × {positive normalised weights}, the commutant 𝒞_y(H) = {E symmetric on pattern(H_y): [H_x, E] = 0} of the corresponding commuting positive-pivot pattern pair equals span{I, H_x, H_y}.

Known: MEASURED dimension 3 on random instances, n = 3..6 (`checks/code/adv/M2/m2_favard_commutant.py`); dimension 6 for exact Padua n = 2 (PD-N?…-04), so the exceptional set is non-empty. Done when: for each n in a stated range, one exact instance with dim 𝒞_y = 3 plus the semicontinuity argument; for all n, a structural proof. Route: (i) span{I, H_x, H_y} ⊂ 𝒞_y always (check that pattern(H_x) ⊂ pattern(H_y) in this order and that H_y commutes with H_x); (ii) the rank of E ↦ [H_x, E] is lower semicontinuous and real-analytic in the parameters (PD-T?…-01 (c)), so dim 𝒞_y ≤ 3 on a dense open set as soon as it equals 3 at one point; (iii) produce one exact rational instance per n (n ≤ 6) with `padua_pattern_commutant.py` adapted to rational nodes.

### A5-partial. Exact identities at the degenerate points of the n ≤ 8 counting search (feeds PD-T?…-06)

**Statement.** At every point z_s where the T3 search used `degenerate_max` (`checks/code/decisive/gen4-2/t3_certify.py` lines 187–207), the cardinal functions in the set Z satisfy L_B(z_s) = 0 and ∇L_B(z_s) = 0 exactly (in the angle coordinates used by the search), and the background g = Σ_{B ∉ Z} sign(L_B(z_s)) L_B has a critical point at z_s or within a rigorously enclosed neighbourhood.

Known: the one degenerate cardinal function at n = 3 is now identified exactly: L_{(2,2)} (node (−½, 0)) = (x − 1)(2x² + x + 2y² − 2)/3, so it vanishes identically on the edge x = 1 and, in the angle variable θ (x = cos θ), to second order at θ = 0 (`checks/code/response-02/padua_n3_edge_identity.py/.out`, exact). Still needed: the list of all z_s and sets Z for n = 3…8 (from `t3_maxima.json` and the log), the corresponding identities, and an enclosure of the background critical point along the edge (evenness in θ gives ∂_θ = 0 at θ = 0; the φ-location needs an interval Newton or sign-change certificate). Done when: every degenerate decision of the n ≤ 8 runs is backed by an identity or enclosure. This is one of the five obligations of A5 below.

## Priority 2 — substantial but concrete

### A2. The log-coefficient of the corner expansion (PD-T?…-04, first part)

**Statement.** Λ_c(n) = (4/π²) log² n + b log n + O(1) as n → ∞, with b = (8/π²)(γ + log(8/π)) = 2 · (2/π) · c₁, where c₁ = (2/π)(γ + log(8/π)) is the constant of the 1-D Chebyshev Lebesgue constant.

Known: leading term (4/π²) log² n and an O(log n) remainder (Kolomoitsev–Lomako 2021, Thm 2.1; LITERATURE, primary excerpt checked by the audit); the fitted b agrees with (8/π²)(γ + log(8/π)) only within a post-registration model (pre-registered fit uncertainty is too coarse to separate it, PD-T?…-04). Done when: a proof of the b-term with an explicit O(1) bound. Route: with A1, Λ_c(n) is a Riemann sum of |D_n| over a sheared lattice on the torus; split D_n into the U_{n+1}U_{n+1} and U_nU_n parts, compare with the product of two 1-D Chebyshev Lebesgue sums (each contributing (2/π) log n + c₁), and control the cross terms; Kolomoitsev–Lomako's discretisation lemma is the template (read the full paper first).

### B1. The "project two, constrain one" step for one-linear-pole-per-degree bivariate rational spaces (PD-N?…-02, part (ii))

**Statement.** Let V_t = Π_t/π_t (π_t = ℓ_1⋯ℓ_t, one linear factor per degree) on M nodes with a positive discrete inner product, W_t = V_t ⊖ V_{t−1} (dim t + 1), C_t = span{(W_{t−1} + W_t + xW_t + yW_t)/ℓ_{t+1}} and R_t = (I − P_{W_t} − P_{W_{t−1}}) C_t. For pole lines in general position and t ≥ 2: W_{t+1} = {r ∈ R_t : r ⊥ W_{t−2}}; in particular every such r is automatically orthogonal to W_0, …, W_{t−3}.

Known: MEASURED with exact blocks for five pole classes, t ≤ 9, M = 120 (`checks/code/decisive/gen1-3/window_exact.py/.out`); the three-block projection without the constraint is false (PD-N?…-02 (i)). Done when: a proof, or a counterexample with general-position poles. Route: the 1-D orthogonal-rational-function three-term recurrence (Bultheel et al.) is the template; express the degree-(t+1) block through a "top-form" functional, as in the adversary's window-parity sketch (`checks/adversarial-gen1-3.md` (ii)(1)), and identify the single linear constraint per direction that W_{t−2} imposes.

### A4. The corner argmax (PD-T?programme-ideas-claude-05)

**Statement.** For every n ≥ 2, max_{[−1,1]²} λ_n = Λ_c(n), attained only at the non-node corners.

Known: no counterexample at 75 tested degrees up to n = 200 on finite meshes; the runner-up is an edge maximum near the midpoint of x = ±1 with fitted gap ≈ 0.548 + 0.84/n (MEASURED). Because the gap stays bounded, a proof needs: (a) an expansion of the edge-midpoint value to O(1) precision, R(n) = Λ_c(n) − g + o(1) with g > 0 (a corner-type closed form along the edge, as in A1, is the first step); (b) an a-priori bound λ_n(x) ≤ Λ_c(n) − δ outside neighbourhoods of the corners and the two edge midpoints; (c) a rigorous finite verification for small n. Done when: all three, or (a)+(b) for n ≥ n₀ plus a certified computation for n < n₀.

### A5. Certification of the local-maxima counts n = 3…8 (PD-T?programme-ideas-claude-06)

**Statement.** For n = 3, …, 8 the Lebesgue function λ_n has exactly 15, 27, 25, 41, 50, 62 strict local maxima on the closed square (interior 7, 13, 14, 25, 33, 44).

Known: MEASURED candidate counts; all 220 listed points independently validated as numerical strict local maxima; completeness not certified. Obligations (audit-01 A1): (1) a proved finite reduction (λ_n is piecewise polynomial on the arrangement of the zero curves of the L_B; every local maximum lies in a cell interior, on a crease, or at a crease crossing, and the search must cover each type); (2) exact identities at the degenerate points (A5-partial above); (3) rigorous root enclosures replacing the per-pattern Newton step, with the injectivity bound applying to the region actually discarded (lines 233–234); (4) a complete box-discard argument for every sign pattern consistent with a box, without the early return at line 249; (5) exact treatment of critical points near crease crossings instead of the 1e-10 coincidence rule (lines 241, 253–257); then rigorous arithmetic and an independent checker. Done when: all five, with the certificate and checker committed (or in cold storage with a manifest). A disagreement with arXiv 2605.23299 at n = 6, 7, 8 would then be a certified correction.

### B3. δ-tolerant box counts on computed sections (complements PD-N?programme-ideas-claude-01)

**Statement to decide.** Let (H_x, H_y) be degree-n sections (size N = dim Π_n, positive pivots, e_1 cyclic) of a positive discrete measure on M > N nodes, δ = ‖[H_x, H_y]‖. Is there a count object (the symmetrised-product count or another) that equals the number of joint eigenvalues of every nearby commuting pattern pair in a box whose boundary is at distance ≥ C δ^α from both marginal spectra, with some α > ½?

Known: on general symmetric pairs α > ½ is impossible for the symmetrised-product count (PD-N?…-01, PROVED); the two measured cluster examples are not computed sections. Done when: either a counterexample inside the computed-section class at distance ≈ c√δ (which would extend PD-N?…-01 to that class), or a theorem with α > ½ under stated hypotheses. Route for a counterexample: two nodes ε apart with M > N chosen so that the recurrence's sections inherit a 45° eigenbasis rotation in the cluster.

## Priority 3 — harder or lower value

### A3. Full corner expansion (PD-T?…-04, second part)

**Statement.** Λ_c(n) = (4/π²) log² N + b log N + c − 1/N + O(log N/N²), N = n + ½, for a constant c independent of the parity of n; and a closed form or characterisation of κ = c − c₁².

Known: post-registration fits only (c = 1.846160310424 stable to ±2e-12 inside the N = n + ½ model; pre-registered spread ±3.3e-5). Done when: a proof with explicit remainder; for κ, either a closed form or a proof that it is not a small-height combination of the 1-D constants (the numerical search is not such a proof).

### B4. A converse joint-Ritz bound under hypotheses (complements PD-T?…-02 and PD-N?…-03)

**Statement to decide.** Identify hypotheses (e.g. no central symmetry through B, odd k, or a localisation condition on K_k(·, B)) under which ‖H_x u_B − x_B u_B‖ + ‖H_y u_B − y_B u_B‖ ≥ c(1 − s_k(B))^β. PD-N?…-03 shows that some hypothesis excluding symmetry centres is necessary.

### B6. Normalised Hilbert–Burch pencils (IDEA?programme-ideas-claude-10)

**Statement to decide.** For the normalised family (orthonormal generators in the Chebyshev coefficient inner product, then orthonormal syzygies), does a compact unitary staircase form with 2N free parameters exist? The GL-orbit count of the M2 adversary does not apply to this family (audit-01 A4).

### B7. Bracketing for a specified lift (IDEA?programme-ideas-claude-01)

**Statement to decide.** For f = φ ∘ g with g a fixed polynomial and the lift G = g(H_x, H_y) (or another fixed lift), do the pair-Gauss and √2-anti-Gauss values bracket the integral of f for all positive measures in a stated class? MEASURED: 196–200 of 200 instances bracket for 1/((x−a)² + (y−b)²). Word-order dependence excludes only a lift-independent theory.

## Already closed in this addendum

- The symmetrised-product count equals the box count for exactly commuting pairs (PD-N?…-01, routine proof added).
- The joint-Ritz converse fails at every symmetry centre for even k (PD-N?…-03, PROVED in general, not only for the 5 × 5 grid).
- The n = 3 degenerate cardinal function factors as (x − 1)(2x² + x + 2y² − 2)/3 (A5-partial, exact).
