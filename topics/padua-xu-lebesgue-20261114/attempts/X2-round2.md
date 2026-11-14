# X2 round 2 — attempts, routes and plan (Morrow–Patterson vertex values)

Researcher: Claude Fable 5.2 (xhigh), subagent of the orchestrator; 2026-11-14. No Git operation was performed by the researcher. Durable results are in `theory/X2-21 … X2-28`, `theory/X2-N29`, `theory/X2-N30`; this file records how they were found, what was tried and dropped, and the plan for T5. Statuses here are informal; the theory records are authoritative.

## 0. Outcome by target

| Target | Outcome | Record |
|---|---|---|
| T1 λ_n(±1,−1) = n+1 | PROVED, all even n ≥ 2 | X2-22 (uses X2-21) |
| T2 closed form and signs at (±1,1) | PROVED | X2-23 |
| T3 lim λ_n(1,1)/n² = c*, explicit error | PROVED, with second term and O(log²n) remainder, explicit constants | X2-25 |
| T4(a) asymmetry, not attained at lower vertices | PROVED (negative results) | X2-24, X2-N29 |
| T4(b) explicit lower bound | PROVED: Λ_n ≥ λ_n(1,1) > c*n² for every even n ≥ 2 (finite part n ≤ 16 computer-assisted) | X2-26 |
| T4(c) vertex value ≠ (n+1)(n+2)/2 | PROVED (finite part n ≤ 40 computer-assisted) | X2-N30 |
| T5 argmax | OPEN; tool (Lemma K), conjectured scaling limits, measured first variation, plan | X2-28, §T5 below |

## 1. How the results were found (successful route)

1. **Kernel at the vertex as a mixed derivative.** (i+1)U_i = T_{i+1}', so K_n((1,1),(x,y)) = ∂_x∂_y Σ''_{a+b≤M} T_a(x)T_b(y), and the diamond sum Σ_{|a|+|b|≤M} z^aζ^b times (z + 1/z − ζ − 1/ζ) telescopes to boundary terms. This gives the divided-difference form ¼(F(x) − F(y))/(x − y), F = T_{M+1} + T_M, hence the kernel for *general* (x, y), and Beberok's eq. (2) at the nodes. The same formula at the reflected lattice points gives the other three vertices: at (±1,−1) the parity class changes and the cubic term cancels exactly, leaving −(−1)^p/(4(x ± y)²).
2. **T1.** The sign (−1)^{p+1} at the lower vertices is U_n(x_p), a polynomial of the space, so λ_n(±1,−1) = U_n(±1) = n+1. To avoid depending on the literature for the Lagrange property, the discrete orthonormality of U_iU_j on MP_n was re-proved by a parity-filtered character sum (X2-21, Lemma 0).
3. **T2.** In X = (1+x)/2, Y = (1+y)/2 the (1,1) term is 16X(1−X)Y(1−Y)[(M−½)X − (M+3/2)Y]/(N(X−Y)³): the sign is (−1)^p except on the band Y < X < κY. The same reproduction identity gives Σ(−1)^pℓ = −(n+1), hence λ = −(n+1) + 2Σ_band. Folding the four Chinese-remainder representatives ±r₁, ±r₂ of a node gives the one-sum formula.
4. **T3.** In the hyperbolic variable u = ½log(X/Y) the term is (2/N)(1−X)(1−Y)[(2M+1)sinh u − 2cosh u]/sinh³u. With the *midpoint* angle μ = (t+θ)/2 and b = t − θ one has exactly (M+½)b = jπ + μ (an equispaced grid of step η in τ̃ = (M+½)b), sinh u = sin b cot μ/(1 − ε_s), cos t cos θ = cos²μ(1 − ε_c), with ε_s, ε_c of *second* order in b. So the exact term is c_M ĥ(τ̃) up to second-order corrections, and Σ ĥ(ηr) is a trapezoid sum of a function vanishing at both ends of its first bump. This yields λ = c*(M+½)² − (M−1) + O(log²M).

## 2. Routes tried and dropped

### Route 1 — first-order parametrisation by (t, τ = jπ + t) (superseded)

- Mechanism: compare each band term with M·h(τ), h(τ) = sin²(2τ)(tan τ − τ)/τ³ evaluated at τ = (M+1)(t − θ) and the *endpoint* angle t; bound u = ∫_θ^t cot by b cot t ≤ u ≤ b cot t + b²/(2 sin²θ); Riemann sums over the grid of step π/(2M).
- Obstruction: the relative error is first order, O(b·(tan t + cot t)); it is O(1) in the vertex region t → π/2 (columns p ≲ √M, where b is comparable to w), and it sums to a genuine O(M) contribution (the formal first-order term integrates to c*M − M). With sup-type bounds the constants came out as |λ − c*M²| ≤ CM with C ≈ 20–40, and the second term was invisible.
- Disposition: abandoned in favour of the midpoint variables (equivalent target, strictly better result). The formal first-order expansion F_M(τ) ≈ (M+2)h_s(τ) + k(τ), k = [½sin²2τ − 2τ sin2τ cos2τ + sin2τ cos2τ tan τ]/τ², with k + h_s an exact derivative of a function vanishing at the band ends, was what pointed to c*M(M+1) − (M−1) and then to the variable M + ½. It is not used in any proof.

### Route 2 — Riemann-sum error by total variation of ĥ (first-order) (superseded)

- |Σ ĥ(ηr) − I/η| ≤ TV(ĥ) is O(1), which costs O(M) after multiplication by 2c_M. Replaced by the second-order trapezoid bound (Lemma R) with TV(ĥ').
- First bounds of |ĥ''| by the product rule gave 48.4 and 32.5; the integral representations of (sin 2τ − ½sin 4τ)/τ³ and (1 − cos 4τ)/(2τ²) give |h̃''| ≤ 68/15 on ℝ (measured maximum 2.89).

### Route 3 — exact summation of the band (not available)

- Column sums Σ_k (1 − y_k²)/(x − y_k)^s over a full column are computable by partial fractions of T_{M+1}(y) ∓ 1, but the Lebesgue sum needs *partial* column sums (the band), which have no closed form. Not pursued.
- The one-sum formula is a trapezoid rule on a full period of T_M(b) = (sin²c − sin²b)²[(M+½) sin c sin b − 1 + cos c cos b]/(N sin³c sin³b), c = (2M+1)b; but |T_M| has third-order poles at b = kπ/(2M+1) close to grid points (they are the images of the small-b terms under the involution r ↦ (2M+1)r), so no smoothness argument applies directly. Kept only as an identity (X2-23 (d)).

### Route 4 — lower bound from the first superdiagonal only (superseded)

- λ ≥ −(M−1) + 2Σ_{q=p+1}(−A) with a tangent-line bound gave Λ_n ≥ c₀n² − O(n), c₀ = 16/π² − (8/π)(Si π − Si 2π) = 0.516513, i.e. 99.9% of c*. Superseded by X2-25/X2-26 (the full band costs nothing extra in the midpoint variables). c₀ survives as the first term of the series for c*.

### Not attempted

- Sharp coefficient of log²n in the remainder (measured −2/π², X2-27). The proof of X2-25 bounds L_c with ζ₊(V̂) ≤ V̂⁻³ and the upper side by 0; keeping the factor (1 − V̂) and a lower bound for e₁ − L_c should give the constant. Deferred: no consequence needs it.
- Closed form for |B| (band size). Deferred.
- Odd n: MP_n = Pad_{n+2} minus edges makes sense for odd n (`lit-notes/X2-sources.md` §6.4, measured), with the large vertices at (1, ±1). The parity bookkeeping of X2-21 (M even, M+1 odd) changes; not treated. Deferred until an odd-n convention is fixed from a primary source.
- EMP points: not treated.

## 3. Literature dependence

- Beberok 2025 eq. (2) and BBDM Thm 2 are **not** used as lemmas: both are re-derived (X2-21). BBDM Lemma 1 is re-derived at the vertices (X2-21 part 4).
- The comparison with Beberok's constant (≈7.5·10⁻⁴) rests on the orchestrator's transcription of his final display (`lit-notes/X2-sources.md` §1b; the term "(n/2+n+2)" there is flagged as to be re-checked). Only the qualitative statement "existential c, tiny explicit value" is used.
- (f) of X2-23 uses the textbook fact ℚ(ζ_a) ∩ ℚ(ζ_b) = ℚ(ζ_{gcd(a,b)}); the locator given (Washington, Prop. 2.4) is from memory and should be verified or replaced before citation in a manuscript. Nothing else depends on (f) except the local-structure remark in X2-28.

## 4. Computations run (all 2026-11-14, this machine; outputs in /tmp/x2r2/, not committed)

| Command (from `code/mp/research/`) | Purpose | Wall | Result |
|---|---|---|---|
| `python3 x2_corner_checks.py` (sections ident cstar decomp table) | identities at 40 digits; c*; per-node and block inequalities of X2-25; R_n table | 28 s | all checks pass; see records |
| `python3 x2_corner_arb.py --nmax 60` | ball arithmetic: c* enclosure, λ_n(1,1) for even n ≤ 60, finite-range inequalities, thresholds | 0.3 s | all flags true |
| `python3 x2_corner_scaling_limits.py` | Lemma K check; conjectured limits vs λ_n; grid scans; first variation | 3 s | see X2-28 |

Scratch explorations (`/tmp/x2r2/explore*.py`) are superseded by these scripts and not committed.

## 5. T5 — argmax: analysis and plan (OPEN)

Observations (MEASURED): G1-MP screen (orchestrator): for even n ≤ 60 the grid maximum is the vertex value at (±1,1); the best other local maximum is on the edge x = ±1 at angular distance ≈ 5/M from the lower vertex with value ≈ 0.403·λ_n(1,1). This is reproduced by the conjectured lower-vertex profile: max_ζ L_bot(0, ζ) ≈ 0.2088 at ζ ≈ 5.0, ratio 0.4038 to c*. So λ_n is of order M² in windows of angular size O(1/M) around **all four** vertices (with a "hole" of size O(M) exactly at the lower vertices and along the anti-diagonal direction ξ = ζ there), and the competition is between the profile maxima c* (top) and ≈ 0.209 (bottom).

Where else could λ_n be large? Along the edges, the top profile decays slowly: L_top(ξ, 0) ≈ 0.143, 0.093, 0.041 at ξ = 8, 16, 32, i.e. λ_n on the edge y = 1 at angle θ₁ is still ≈ 0.04·M² at θ₁ = 32/M. In the interior BBDM state O(n). So the dangerous regions are the four vertex windows and the edges near them, not the interior.

Localization strategy (each step is a separate provable statement):

- **P1 (local maximum).** λ_n = P_n := Σ sgn(ℓ_a(1,1))ℓ_a near (1,1) (no ℓ_a vanishes there, X2-23 (f)). Show ∂_xP_n(1,1) > 0, ∂_yP_n(1,1) > 0. Closed forms: ∂_x K_n((s,1),(x,y))|_{s=1} = Σ U_i'(1)(j+1)U_i(x)U_j(y) = ∂_x∂_y of Σ'' T_a''(1)/a · … — simplest is to differentiate Lemma K twice in θ₁ at θ₁ = 0 (the formula is even in θ₁ after division by sin θ₁). Expect D_x = d₁M⁴ + O(M³), measured d₁ ≈ 0.050, with the sign pattern of X2-23 and the lattice method of X2-25. Risk: low. One round, could be Opus with the X2-25 template.
- **P2 (scaling limit with error).** Prove the L_top and L_bot limits uniformly on |(ξ, ζ)| ≤ R with an explicit error. The lattice is the same; the summand is Lemma K's four-term expression. The difficulty compared with X2-25 is that the sign set is no longer a band described by one inequality: the absolute value sits on a sum of four simple-pole terms in τ. A workable route: bound |exact − limit| termwise (no sign information needed, since ||a| − |b|| ≤ |a − b|) and sum; the first-order errors now do not cancel automatically, so expect an O(M^{3/2}) or O(M log M) error rather than O(log²M) — enough for the argmax. Risk: medium. Fable.
- **P3 (profile inequality).** L_top(ξ, ζ) < c* off the origin and sup L_bot < c*. Sub-steps: (a) near the origin, from P1-type second-order expansion of the profile; (b) on a compact annulus, a rigorous numerical enclosure of the one-dimensional integrals (interval quadrature of an explicit integrand; a computer-assisted step with its own checker); (c) for large |(ξ, ζ)|, an analytic bound from the Fourier form (the kernel [cos α cos βs − cos β cos αs]/(α² − β²) is bounded by C/(1 + |α − β|)… to be worked out). Risk: medium–high; this is the analogue of the hardest part of the Padua argmax proof.
- **P4 (between the windows).** Uniform bound on the edges and in the interior at distance ≥ R/M from the vertices: λ_n ≤ (c* − δ)M². From Lemma K with explicit constants; BBDM's Lemma 6 estimates give the structure. Risk: medium; long but routine.
- **P5 (finite n).** Certificates below the onset, independent checker.

A cheaper intermediate theorem, if P3(c)/P4 are too long: "eventually" statement lim Λ_n/n² = c* (no argmax claim) needs only P2 on compact sets, P3 as a non-strict inequality L_top ≤ c*, L_bot ≤ c*, and a soft bound in P4 (λ_n ≤ εM² far from the vertices as R → ∞, uniformly in n). That would settle the sharp constant of the MP Lebesgue constant, which is the main open quantitative question after BBDM/Beberok.

Recommendation: next round P1 (+ start of P2); researcher Fable for P2/P3, Opus sufficient for P1 and for the certified-quadrature tooling.
