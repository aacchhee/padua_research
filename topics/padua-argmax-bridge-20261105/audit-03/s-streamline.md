# S — Streamlining the proof architecture of the journal paper

Rules read at `f366535e1fa4ede566cb83bdc554220c12b307cf` (AGENTS.md, agents/WORKFLOW.md,
agents/claude/CLAUDE_ROLES.md, claude-audit-brief-20261108.md). Branch
`codex/padua-argmax-bridge-20261105`, head `f366535e…`. Role: independent mathematical editor /
proof architect, a special task inside the handoff-28 Claude audit. Model: Claude Opus 5.5, xhigh.
No repository file was edited and no state-changing git command was run. Outputs are this file and
`s-code/`. The scope adds no novelty content: no new mechanism or priority claim is made, so the
IDEAS gate does not apply. All proposed proofs reuse estimates the paper already proves.

Labels: **[I]** inspection of the TeX and records; **[D]** my own derivation; **[E]** executed
(scripts and logs in `s-code/`; Python 3.13.18, mpmath 1.3.0, python-flint 0.9.0 Arb). Within [E],
MEASURED means floating-point or grid planning, and ENCLOSED means Arb balls or exact `Fraction`
arithmetic at the stated base degrees. **No all-n monotone transfer of a new gate is proved here.**
Those transfers are listed as obligations. The certificate engine was not run.

Sources read in full: main.tex and all six sections, CONSOLIDATION.md, small-degree-unification.md.
Read in part: consolidation-audit.md (budget, deletions, final verdict); G01, E14-assembly320, the
D37/E07/E09 headers, D29-floor512, D39 (cost); final_hybrid_engine SPEC.md and checker.py (guards,
floor tiers); compact-return.md and statistics.json; the sampled primary certificates n199 and n238;
audit-02-ideas.md §2. I used the compiled PDF (`build/paper/main.pdf`, 48 pp) to map pages.

---------------------------------------------------------------------------------------------------

## 0. Summary

1. **The paper is already near the floor for its current onset 320.** [I] I agree with the
   consolidation audit (§"Final verdict"). At 320 every remaining branch has a consumer: the near
   column (the half-near margin is 1/20000), the outer geometry block, far-192 and corner-256
   (consumed by the returned certificates), and the one-sided origin bound.

   With no new computation about **1.5 pp** can still be saved (architecture **A′**, §4.3).

2. **The binding constraint is the onset, not the exposition.** [E] At **N0 = 512**, the whole
   tail closes with two closed-form gates built from estimates the paper already proves:
   - one radius-one relative polynomial P_n(ρ) together with a uniform floor 1/20;
   - one absolute gate G(n,ρ₁).

   Taking N0 = 512 removes the near column of the relative table, the radius-dependent tail
   floors, the annulus with its seams 3/5, 21/40, π/4, the outer-geometry block, and the separate
   far-192 derivation, which becomes the same gate at ρ₁ = π/2.

   The base margins grow from 5·10⁻⁵ to about 9·10⁻³ (near) and 0.53 (outer). The cost is
   **191 more certified degrees (320–510)** on the frozen engine. Its guard is 41..4095 and its
   floor tiers already cover n < 512. The projected cost is about 1 CPU-h and about 25 MB of cold
   evidence. This is architecture **B**; it saves about **5 pp** (to about 43 pp). B is my
   recommended architecture, provided AC accepts an onset change, which is material.

3. **The PD-T271 computational input can be removed outright, at either onset.** [E] The only
   consumed constant inequalities are κ > 9/10 (giving j > 23/250) and C_* < 1.8516 (giving
   C_∞ < 9/4). The paper's own series (uc:kappa-series), truncated at **K = 3** with elementary
   bounds for π, γ, log 2, log π, ζ(3), ζ(5), ζ(7), ζ(9), gives 0.91720 < κ < 0.92151 and
   C_* < 1.84802. κ < 23/25 has margin only 2.9·10⁻⁴ (κ = 0.919710…) and feeds only an H₀ upper
   bound that nothing consumes.

   With this change the analytic part of Theorem 1.1 has no computational dependency at all.

4. **Bolder options are not clearly better** (§4.4–4.7). An absolute-only tail would save about
   6 more pages but closes only near n ≈ 5000–6000, needs two engine changes and about 115 CPU-h,
   and loses the paper's most genuinely analytic mechanism. An effective corner expansion would
   lengthen Section 3 by 2–3 pp and barely moves the binding near gate. Replacing the 2..40
   Bernstein scheme by phase covers needs new small-n defect floors. I recommend none of these.

5. **Restructure the presentation around four objects:** one kernel/row calculus, one comparison
   theorem, two gates, one corner lemma (§6 gives the outline).

   **Hidden cost:** `check_correspondence.py` enforces 1:1 structure with the 162-page companion.
   Every restructuring above must therefore be mirrored there, or that constraint relaxed by AC.

---------------------------------------------------------------------------------------------------

## 1. True dependency graph [I] (label census over all `\label/\ref/\eqref`, then the proofs)

### 1.1 Main chain (→ means "is consumed by")

| Node (label) | Content | Consumers |
|---|---|---|
| Lem 2.1 `lem:cardinal-kernel` | corrected kernel, coefficient one, unisolvence | §3 (cu:positive); `eq:angular-kernel` → (ul:cardinal-reflection); §5.1 Bernstein |
| symmetry ¶ (prelim l.78–83) | the two non-node corners have equal values | Thm 1.1 proof, §5 |
| (cu:positive)→(cu:exact) | exact corner row sum | Prop 3.2, Thm 1.2 |
| (cu:square),(cu:deform)→(cu:kappa) | Λ_c − A(n)² → κ (integral form) | **Thm 1.2** (C = κ) **and §4** (uc:origin-identity) |
| Lem 3.1, (cu:psi-est),(cu:center),(cu:row-expand),(cu:H-to-M),(cu:w-sum) | quadrature and digamma | Prop 3.2 only |
| Prop 3.2 `cu:aggregate` (never \ref'd by name) | β_H, β_B, C_H, C_B | proof of Thm 1.2 |
| (ul:cardinal-reflection)→(ul:charts)→(ul:primitive)→(ul:defect),(ul:projections) | λ = S − Δ, Δ ≥ max(Q_h,Q_v) | floors; all gates; §5.2 |
| Lem 4.1 `uc:cancellation-lemma` | R ≤ 0; R_s, R_e bounds; E ≤ Z | Lem 4.3 (R ≤ 0); variation table of Prop 4.5 (R_s, R_e); Lem 4.4 (E ≤ Z) |
| Lem 4.2 `uc:scalar-maximum` | f bounds, cusp atom, H ≤ H₀ | Lem 4.3 (j); Prop 4.5 (N_s variation; V_s, P_s in relative table) |
| (uc:completed-model),(uc:endpoint-envelope) | M_∞, uniform finite part | Lem 4.3; E_out holes |
| Lem 4.3 `uc:master` | (uc:model-loss); central decomposition (uc:Ec); (uc:regular-loss); constants j, t₀, C_∞ < 9/4 | model-loss → outer gate, far-192, corner δ_D; regular-loss → (uc:relative-comparison); 9/4 → M(n) |
| (uc:origin-identity)+(uc:coarse-input)[**PD-T271**]+(uc:kappa-series) | H₀ = κ/2 + …; 9/10 < κ < 23/25; C_* < 1847/1000 | only H₀ > 7/25 ⇒ j > 23/250, and C_* ⇒ C_∞ < 9/4. **κ < 23/25 and H₀ < 8/25: no consumer** |
| Lem 4.4 `uc:central-pair` | E_c ≤ c·p^{3/2}/√a − B_β | 3/8 and B_β ≥ 1679y²/8000 → near gate only; 5/12 → wide gate; general form → corner δ_A (E_c(h,0) < 1/4) and δ_D (≤ 4/15 on closed ρ ≤ π/2) |
| Prop 4.5 `uc:finite-bounds` | (uc:global-error) with phase-dependent C_{E,φ}; (uc:analytic-norm); (uc:origin-lower); (uc:relative-comparison) N and W columns | global-error → outer, far-192, corner δ_D, origin identity; norm → corner-256 only; origin-lower → all gates; N column → near gate only; W column → wide/annulus **and corner-256 δ_A** |
| Lem 4.6 floors: (ul:finite-floors) | tiers 41/64/160 (n < 512) | **§5.2 certificates only** |
| Lem 4.6 floors: (ul:tail-floors) | F_near, F_small, F_h, F_w | near gate and annulus only |
| (ul:near-base)…(ul:near-exclusion), (ul:annulus), (ul:wide-exclusion) | gates for 320 | Thm 1.1 proof only |
| (ul:outer-geometry)→(ul:outer-gate)→(ul:outer-exclusion) | outer gate 320 | Thm 1.1 proof only |
| (ul:far192) | S < Λ_c − 3/100 for n ≥ 192, ρ ≥ π/2 | **§5.2 only** (the tail does not use it) |
| (ul:squared-peano) | squared-variable Peano descent | corner-256; §5.2 numerical corner witnesses (41..255) |
| (ul:corner256) | descent (A²+B²)/30 for n ≥ 256 | Thm 1.1 tail; §5.2 (n ≥ 256) |
| Lem 5.1 `cert:positive` and the norms (cert:tree-norm),(cert:grid-norm) | positive interpolation | §5.1, §5.2; TREE only without f leaves, GRID otherwise |

**External records consumed:** PD-T271 (κ, C_* enclosure); the compact return (41..319 plus 511)
under FREEZE `0d9ce0a5…`; the 2..40 Bernstein witnesses (2..16 fresh, 17..40 reused); trusted
Arb/FLINT/MPFR/GMP, compiler and checker.

### 1.2 Do the hybrid analytic branches belong to the logical proof? [I]

Yes, as executed. Both sampled certificates (n199, n238) have tree preorder ending in `fff`, with
`ANALYTIC_FAR = 3` and `norm/method = GRID`. The frozen producer emits an `f` leaf whenever a box
satisfies the guard (SPEC.md l.131–152), and the corner switch at 256 is unconditional (checker;
SPEC l.188–214).

So (ul:far192) is a premise for the returned degrees 192..319, and (ul:corner256) for 256..319.
Removing either from the paper requires a new engine freeze and a rerun of those degrees.
That is not worth it: in B, far-192 becomes a one-line instance of the absolute gate, and
corner-256 is needed by the tail anyway (only its base degree 256 is "extra", and it is free).

### 1.3 Statements stronger than any use; once-used results; dead statements [I]

**Dead (no consumer):** κ < 23/25 (l.409); H₀ < 1633/5125 < 8/25 (l.454); the parenthetical
"(608/27 is also convenient)" (l.121). **Stronger than needed:** (ul:far192) proves 79/2000 while
the certificates consume 3/100 (harmless). **Used once:** Lem 3.1 (should become the shared
quadrature lemma), Prop 3.2, (ul:far192) (§5 only), (uc:analytic-norm) (corner only),
(uc:origin-identity).

**Formal statements never cited by name:** Lem 4.1–4.4, Prop 3.2 and Prop 4.5 are used only
through their equation labels. Cite them at use (editorial).

**Phrasing that misstates the logic:** "For clarity the logarithmic coefficient can be checked
independently" (comparison l.288) is in fact the only proof of b_full. Rephrase it.

### 1.4 Constants and thresholds with historical provenance [I]

| Constant | Origin | Consumer | May change? |
|---|---|---|---|
| 320 | first n where the E14 recipes closed (half-near margin 2.4·10⁻⁴) | tail | **yes** (B: 512) |
| 192, π/2, 3/100 | E15 far closed at 181; engine guard | returned certificates | **no** (frozen); the proof can change |
| 256, π/4×π/4, 1/30 | E12 corner closed at 239 | certificates, tail | **no** |
| 41/64/160 floor tiers; 1/512, 1/64, 1/32, 1/20 | C02/D29 proofs per range | certificates | **no** |
| 512 tier (1/20) | D29-floor512 (cut from the paper) | engine for n ≥ 512 only | needed only if certificates or the tail use n ≥ 512 |
| u′ = 1/32, v′ = 9/512, rectangle π/4×3π/16 | D08/D32 numerical corner witness | certificates 41..255 | **no** |
| 784/663, quarter grid, 157/50 < π < 22/7 | D14 norm, checker bracket | certificates | **no** |
| 1/20000, 3/1000, 99/2500, 13/500 | tail gap artifacts | strictness only | yes |
| seams 1/8, 1/2, 3/5, 1; guards 21/40, π/4 | recipe artifacts | tail | yes (B keeps 1/2, 1) |
| j_* = 23/250, t_* = 221/500, u₁, a₀, w₀, p₀, P₀, η | E13 outer recipe | outer | yes (B: only j, t₀) |
| 9/10 < κ < 23/25, C_* < 1847/1000, K = 64 Arb at 320 bits | PD-T271 record | j, C_∞ | **replace** (K = 3 by hand) |
| 2..40 / 41.. split | Bernstein cost; floor geometry needs M, L ≥ 41 | two engines | no |

---------------------------------------------------------------------------------------------------

## 2. Computations

### 2.1 κ without PD-T271 [E ENCLOSED, `kappa_hand*.py`, `kappa_runs.txt`]

Elementary inputs: π ∈ (333/106, 355/113); γ ∈ (0.57721, 0.57722) (the N = 10 harmonic bound from
the paper's own 0 ≤ log w − 1/(2w) − ψ(w) ≤ 1/(8w²) also suffices, since the C_* margin tolerates
±0.003 in γ); log 2, log π to 10⁻⁶ via (ul:log-series); ζ(2r) exact in π; odd ζ(s) from the
partial sum to 10 plus convexity tails (e.g. ζ(3) ∈ [1.202031986, 1.202067133]).

The paper's tail bound 8/(3(K+2)4^{K+1}) gives:

| K | κ enclosure | κ > 9/10 | C_* upper | needed C_* < 1.85161 (for C_∞ < 9/4) |
|---|---|---|---|---|
| 2 | [0.907276, 0.928236] | yes | 1.854744 | no |
| **3** | **[0.917200, 0.921508]** | **yes** | **1.848016** | **yes** (also < 1849/1000) |
| 4 | [0.919166, 0.920187] | yes | 1.846695 | yes (also the paper's < 1847/1000) |

Supporting values: mpmath κ = 0.919710118388, C_* = 1.846160310; c₀..c₃ = 1.0517998, 0.1394531,
0.0319855, 0.0078553; (8/π²)Σ_{k≤3} c_k/(k+1) = 0.9193090, consistent with the tail bound
≤ 0.0020833; the paper's |c_k| ≤ 2·4^{-k} holds with factor 0.526 (k ≤ 24); H₀ = 0.31000 and
j = 0.14354 (the paper uses j > 0.092).

**Proposed text (≈10 lines, after eq:main-kappa in §3):** the series with K = 3, displayed
rational bounds for ζ(3), ζ(5), ζ(7), ζ(9), and the conclusion 0.917 < κ < 0.922; then, in §4,
"κ > 9/10 and C_* < 1849/1000". The C_∞ < 9/4 step needs δ² + δj > t₀², which holds since
9/4 − 1.849 = 0.401 > 0.3988.

Delete: κ < 23/25, H₀ < 1633/5125, the Arb K = 64 sentence, and every "trusted computational
input to the location proof" phrase (intro l.103–104; §4 l.555–558; G01 l.75–77).

### 2.2 An absolute-only tail (bold option C) [E MEASURED grid, `abs_tail.py`]

Gate: Λ_c − S_n ≥ u(T+j) − t₀ sin x − C̄_E − K_D P − e₀, with e₀ = ē from (uc:origin-lower).

| n | 320 | 1024 | 2048 | 4096 | 6000 | 8192 |
|---|---|---|---|---|---|---|
| C̄_E | 1.149 | 0.399 | 0.212 | 0.112 | 0.079 | 0.059 |
| near, noncorner, tail floors | −1.25 | −0.36 | −0.13 | −0.017 | **+0.023** | +0.046 |
| near, uniform 1/32 floor | −1.30 | −0.44 | −0.22 | −0.10 | −0.066 | −0.042 (closes about 25000) |
| far ρ ≥ 1/2 | −1.13 | −0.056 | +0.29 | +0.55 | | |
| corner (absolute losses) | −0.42 | +1.22 (already +0.34 at 512) | | | | |

Replacing ē by C̄_E roughly doubles the onset. Variant B instead keeps the wide relative column
(§2.3).

### 2.3 The radius-one polynomial and the closed-form absolute gate [E ENCLOSED Arb, `b_arch_arb.py`, `b_onsets.py`]

**Relative gate [D].** Combining (uc:relative-comparison) W column, E_c ≤ (5/12)x^{3/2}
(Lemma 4.4, ρ ≤ 1), x^{3/2} ≤ x² + x/4, u ≥ 11(x²+y²)/48 and (ul:radial-quadratic) gives, on ρ ≤ 1,

  **S_n − Λ_c ≤ P_n(ρ) = C₄ + g + fρ − eρ²**, with ℓ₁ = k_Wx + 5/48, ℓ₂ = k_Wy, U = T − ē + A₄ + j,
  d₁ = 11U/48 − 5/12, d₂ = 11U/48.

**Absolute gate [D].** From (uc:global-error) with uniform C̄_E, (uc:origin-lower) and
(uc:model-loss), with x = ρ/2 + δ, y = ρ/2 − δ: Λ_c − S_n ≥ Θ − [A cos δ + B sin δ] − C̄_E − ē,
where Θ = T + j, A = Θ cos(ρ/2) + (t₀+2K_D) sin(ρ/2), B = t₀ cos(ρ/2). Use
A cos δ + B sin δ ≤ √(A²+B²), which decreases in ρ once tan(ρ/2) ≥ (t₀+2K_D)/Θ, and linearize the
root. For ρ ≥ ρ₁:

  **G(n,ρ₁) = Θ(1 − cos(ρ₁/2)) − (t₀+2K_D) sin(ρ₁/2) − t₀² cos(ρ₁/2)/(2Θ) − C̄_E − ē**,

which is manifestly increasing in n.

Base values (ENCLOSED, ball radius < 10⁻⁵⁰); my transcription reproduces the recorded
M(256) = 25.393, T(320) = 11.7319, ē(320) = 0.15407.

| check | value | first closing n (base only) |
|---|---|---|
| uniform floor: (ul:tail-floors) at r = 1/2 gives > 1/20 | F_h(320,½) ≈ 0.0516; F_h(512,½) = 0.0581; F_near 0.0902; F_small 0.0822 | **295** |
| near noncorner: 1/20 − max_ρ P_n | **+0.009214 at 512** | **457** |
| ρ ∈ [½,1]: −P_n(½), with vertex f/(2e) | +0.143070, vertex 0.147 < ½ | 343 |
| outer: G(n,1) | +0.534 at 512; the fully crude u₁(T+j) − t₀ − C̄_E − 2K_D − ē gives +0.195 | 365 (crude form: 453) |
| far leaves: G(n,π/2) − 3/100 | G(192,π/2) = **0.098958** | 189 |
| one wide column on the half-near region at 320 | −0.0059 (MEASURED, exact u) | about 340 |

The last row confirms that the near column is necessary at 320, but only there.

---------------------------------------------------------------------------------------------------

## 3. Architecture B (recommended): exact new statement list

Unchanged: Lem 2.1, the corner section's results, Lem 4.1, Lem 4.2, the completed model,
Lem 5.1, both norms, and the 2..40 scheme.

**Comparison statements.**
- **Lem 4.3′ (model).** As now: (uc:model-loss), C_∞ < 9/4, the central decomposition with
  (uc:regular-loss), and C_* = c₁² + κ via (uc:origin-identity). The constants (j > 23/250,
  t₀ < 221/500, C_* < 1849/1000) now come from the K = 3 enclosure. Delete the dead bounds.
- **Lem 4.4′ (central pair).** Keep the general form, E_c(0,y) = −B_β ≤ 0, and the 5/12 case
  (ρ ≤ 1). Drop the 3/8 case and B_β ≥ 1679y²/8000.
- **Thm 4.A (comparison with the completed model).** For integer n ≥ 32 and absolute phases in the
  closed triangle (signed diamond with separate absolute phases): (i) |S_n − M_∞| ≤
  C̄_E + K_D(sin x + sin y), with C̄_E, K_D decreasing; (ii) |complete signed sums| ≤ M(n);
  (iii) for n ≥ 160, Λ_c = S_n(0) > M_∞(0) − ē; (iv) for n ≥ 160 and ρ ≤ 1,
  S_n − Λ_c ≤ E_c − uU_W + C₄ + k_Wx x + k_Wy y.

  This absorbs Prop 4.5. It drops the near column, the phase-dependent statement and the
  fixed-phase monotonicity claims. Those quantities stay as intermediates in the proof, together
  with the correlated 3H/n saving. That saving is needed: without it G(192,π/2) drops to 0.001 and
  corner-256 fails.
- **Cor 4.B (absolute gate).** For n ≥ 160, 0 < ρ₁ ≤ π and tan(ρ₁/2) ≥ (t₀+2K_D)/(T+j): every phase
  with ρ₁ ≤ ρ ≤ π has Λ_c − S_n ≥ G(n,ρ₁), and G increases in n.
  Instance (a): G(n,π/2) > 3/100 for n ≥ 192, exactly the certificates' analytic far leaves,
  replacing (ul:far192). Instance (b): G(n,1) > 1/2 for n ≥ 512, replacing (ul:outer-exclusion).
- **Cor 4.C (relative gate).** For n ≥ 160 and ρ ≤ 1, S_n − Λ_c ≤ P_n(ρ). For n ≥ 512,
  max_ρ P_n < 1/20 − 9/1000 and P_n(1/2) < −1/7, with vertex f/(2e) < 1/2.

**Localization statements.**
- **Lem 5.1′ (selected-pair floors).** (i) Finite tiers for 41 ≤ n < 512, verbatim (the
  certificates need them). (ii) For n ≥ 320 and ρ ≤ 1/2, every eligible projection exceeds 1/20:
  classes 1 and 2 by the finite argument (> 1/20 for n ≥ 64); class 3 by the c = 2 band
  [π/100, π/4] at r = 1/2, F_h(n,½) = (539/1936)I − 726.38…/(157n) − 175.83…/n² > 1/20.

  This absorbs D29-floor512 and drops F_near, F_small, F_w, η_r, the A_g concavity argument and
  the radius dependence.
- **Lem 5.2 (actual-corner descent).** Unchanged (ul:squared-peano) and (ul:corner256) for n ≥ 256.
- **Thm 5.3.** Theorem 1.1 holds for n ≥ 512. Proof (≈12 lines): noncorner charts with ρ ≤ 1/2
  give λ ≤ Λ_c + P_n − 1/20 < Λ_c; all charts with ½ ≤ ρ ≤ 1 give S_n < Λ_c; all charts with
  ρ ≥ 1 by Cor 4.B(b); actual corners by Lem 5.2; then parity and compactness as now.

**Section 6.** 2..40 Bernstein as now. Phase covers for **41..511**. A short table lists the
analytic-leaf interface: far leaves = Cor 4.B(a), corner = Lem 5.2, plus the floor tiers, u′/v′,
the norms and the π bracket.

**New proof obligations** (short scalar lemmas from existing estimates): P_n's maximum and
P_n(½) decrease for real n ≥ 512 (k_W, C₄, ē decrease, e increases, f needs one line); G(n,ρ₁)
increases under the tangent condition; F_h(n,½) increases (already in the lemma); one exact
Fraction evaluation of each gate at its base.

**New computation.** Frozen-engine certificates for 320–510 (511 already passed as a control).
Projected 2 passes × 191 × 8–12 s ≈ 1 CPU-h (from the 511 control, 7.35/7.53 s, and the observed
10.1–23.2 s at 41..319; not a cost law). About 25 MB cold (≈129 KB per pair). Recheck the
committed-evidence footprint against AC's 10 MB cap (now 9.77 MB conservative).

---------------------------------------------------------------------------------------------------

## 4. Options evaluated

### 4.1 (a) Onset versus finite completion

History [I]: onsets were lowered 1024 (D37) → 768 → 640 → 512 (E07) → 384 (E09) → 320 (E14) by
sharpening components and adding assembly pieces. D37 at 1024 still had 5 gates, near and wide
relative allowances, and 59 validated scalar intervals, so it was not simpler. The new trade-off in
B keeps E14's sharpest components but raises the onset to 512 to buy the simplest assembly.

Above 512 nothing structural improves until about 5000: the relative column stays necessary
(§2.2). So 512 = 2⁹ is the sweet spot. It also coincides with the engine's floor-tier boundary,
so the certificates need no 512 tier.

Projected cost per extra degree is about 2 + 0.011·n CPU-s per pass, from the per-S-call scaling of
about 2.4·10⁻⁴·n s at n = 1023/2048/6912 (D39, D23). On that basis:

| N0 | degrees 320..N0−1 | CPU-h (2 passes) | cold MB | paper effect |
|---|---|---|---|---|
| 512 | 192 (191 new) | about 1 | about 25 | B, −5 pp |
| 1024 | 704 | about 4 | about 90 | same as B plus uniform 1/32 floor possible; no further structural gain; certificates ≥ 512 need the 1/20 tier (Lem 5.1′(ii) supplies it) |
| 4096 | 3776 | about 55 | about 490 | still needs the relative column (near absolute gate −0.017); engine cap 4095 |
| about 6000 | about 5700 | about 115 | about 740 | C: −11 pp, needs a corner switch 256→512 and a raised degree cap (two engine changes, re-freeze, rerun from 256) |

### 4.2 (b) A master comparison and one ρ-parameterization

At 320 [E], near and wide need different columns, the outer region needs phase-dependent
majorants (G(320,1) = −0.232), and only far-192 can become G(n,π/2). At 512 the paper becomes
exactly Thm 4.A plus two ρ-parameterized corollaries: far-192 and the outer exclusion are the same
lemma at ρ₁ = π/2 and ρ₁ = 1, and near and wide are one polynomial.

Selected-pair floors stay one lemma, with a finite part and a one-constant tail part. The
reflection geometry is essential and unchanged.

Do not drop far-192 or corner-256 from the narrative; re-express them as instances (§1.2).

### 4.3 A′: no new computation, onset kept at 320

Steps: K = 3 κ enclosure (§2.1); delete the dead statements; prove far-192 by Cor 4.B(a)
(about 30 lines, l.433–464, become about 6) and move it to §5, its only consumer; the row-calculus
merge (§4.6); cite statements by name; trim §5.3 overlap with "Data and code availability".

The outer gate at 320 keeps its phase-dependent block. The near and wide columns stay. This saves
about 1.5 pp, to about 46–47 pp.

### 4.4 Option C (absolute only)

C is not clearly better. It removes the relative comparison's 4.3 pp proof (p30–34) plus Lem 4.4
and the central decomposition, but the analytic part becomes an n ≳ 6000 afterthought, the
computer part grows about 12×, the near margin is tight even at 6000 (+0.023), it needs two engine
changes and about 0.7 GB of evidence, and it discards the matched-relative idea, the paper's
distinctive analytic device. Mention C at most as a remark.

### 4.5 (c) Using Theorem 1.2 inside the argmax proof

The argmax needs an explicit E_n(0) ≥ −e(n) for every n ≥ N0. The O(log N/N²) remainder has an
unspecified constant and cannot supply this.

[D] From Theorem 1.2 and M_∞(0,L) = A(n)² + κ:
E_n(0) = Λ_c − M_∞(0) = (a²(L+d) − 1)/n + O(L/n²). This is ≈ +0.0061 at 320 and +0.0040 at 512,
consistent with audit-02's measured +0.006/+0.004. So −ē (0.154 at 320) is far from sharp.

Making Section 3 effective needs explicit constants in Lemma 3.1, (cu:psi-est), (cu:center), the
Q_{m,r} bound, the e_r/u_r tails, the endpoint moduli of R, B″ on [−¼, 5/4], the H_{m−1} and
Σ log r/r expansions and the N transfer: about +2–3 pp. The gain is small for the binding near gate
(ē enters u-weighted) and larger for outer/far (audit-02: e₀→0 moves the outer to 277); it saves no
pages. Recommendation: isolate the only §3 → §4 interface as one lemma ("C_* = c₁² + κ and
0.917 < κ < 0.922"), add one remark comparing E_n(0) with Theorem 1.2, and leave the effective
expansion (valuable on its own, as explicit bounds for Λ_n) as future work.

The PD-T271 dependence is removed entirely by §2.1, not merely isolated.

### 4.6 (d) One theorem pair and a shared row calculus

Both arguments use the same objects: the angular kernel G_n and its P_n divided difference; the
reflection formula; the cotangent row identity (−1)^δ G_n/2 = C cot((u−v)/2) + D cot((u+v)/2),
which at phase zero is exactly F_r of §3.1 (C = −w/2, D = w/2); Σ cot(z+ℓπ/n) = n cot nz and its
csc² derivative (§3.1 and again the origin paragraph, l.1023); ψ, defined twice (§3 (cu:psi);
comparison l.89), with C(t) = −ψ(t) − ψ(1−t) and ψ(1−t) − ψ(t) = π cot πt; the harmonic estimate
(O form in §3, effective in §4 l.750); the cotangent partial fraction (derived §3 l.257–265, used
throughout §4); and two quadrature tools (Lem 3.1, the BV centered-cell rule).

Proposal: put these in §2 ("Kernel and row calculus"). Derive (cu:positive) from S_n(0,0) and the
row identity, replacing the D_n diamond computation (l.25–52). The collision value
G_n(π,π) = (−1)^n·2n follows from P_n′(−1). This saves about 0.5 pp and makes the introduction's
"one kernel" claim literal.

Order the results as Theorem A (corner expansion, analytic), Theorem B (location), and a
Corollary (the expansion for Λ_n); this removes the forward use of Thm 1.1 inside Thm 1.2.

### 4.7 (e) One finite mechanism

Do not merge the mechanisms. Phase covers below 41 need new defect floors: the class counts in
the proof of Lem 4.6 require M, L ≥ 41 (e.g. (29/492)², γ < 1/3, s ≥ 5 ⇒ γ > 4π/L), so small n
would need a new per-chart defect certificate and checker. Bernstein at n ≥ 41 is infeasible
([D] estimate: O(n⁴) coefficient sums per leaf times O(n²) leaves, about n⁶).

Lemma 5.1 already unifies the two at the right level. Keep both mechanisms (≈1 page each). The
degree-one formula may stay (5 lines) or move to the companion.

---------------------------------------------------------------------------------------------------

## 5. Change register (pages from the PDF map: model p13–21, finite-row proof p21–34 with relative charges p30–34, floors p34–36, near/annulus p36–38, outer/far p38–40)

| # | Change | Δpp | Kind | Correctness risk | Re-review / invalidated checks | Changes a claimed constant? |
|---|---|---|---|---|---|---|
| 1 | K = 3 κ enclosure; drop PD-T271; delete dead κ/H₀ bounds | ±0 | small new proof (exact arithmetic) | very low | focused check of one paragraph plus a script; G01/E14/intro/data statements | dependency removed (material, improvement) |
| 2 | Far-192 via Cor 4.B(a) | −0.4 | new short proof; same guard and gap | low | E15 acceptance stays valid for the old proof; new focused review; no certificate change | no |
| 3 | §2 row calculus; Thm A/B/Cor order; cite lemma names | −0.5 | restructuring | low–moderate (rewrite of §3.1) | consolidation and style reviews; **companion correspondence** | no |
| 4 | Split §4 into "Comparison" and "Localization"; Thm 4.A as one interface | ±0 | restructuring | low | companion structure | no |
| 5 | Onset 512: Cor 4.B(b), Cor 4.C, Lem 5.1′(ii); drop near column, tail floors, annulus, outer block | −4.5 | new short proofs plus 191 certificates | low (margins 9·10⁻³ / 0.14 / 0.53, compared with 5·10⁻⁵ now) | new tail review; compact-return verification and fresh pass for 320–510; G01 decomposition; E14 becomes a companion/record | **onset 320 → 512** (material; AC) |
| 6 | Lem 4.4′ trims (drop 3/8, B_β bound) [needs #5] | −0.15 | deletion | none | none | no |
| 7 | §5.3 de-duplication with the declarations; remove run narration (l.99–100) | −0.3 | editorial | none | style review | no |
| 8 | Intro trims (stray last line "The onset 320 is sufficient…"; repeated boundary sentences) | −0.2 | editorial | none | none | no |

---------------------------------------------------------------------------------------------------

## 6. Prioritized plan, target length, outline

**Plan:** (1) change #1 in every scenario: cheap, and it makes the analytic part fully analytic;
(2) change #2; (3) AC decides on onset 512 (#5); if yes, the developer writes Cor 4.B, Cor 4.C and
Lem 5.1′(ii) with monotone transfers and an exact-Fraction check script, and root preregisters and
runs 320–510 on the frozen engine, followed by the usual fresh/verify/compact review; (4) #3 and #4;
(5) #6, then #7 and #8; (6) update the companion in the same pass, or have AC relax the 1:1
correspondence (§7).

**Target length:** about 43 pp with B, about 46–47 pp with A′, about 37 pp with C (not
recommended). The finite-row comparison (about 12 pp) is irreducible under any architecture that
keeps a relative estimate, and B keeps one. Further cuts beyond about 42 pp would have to come
from the comparison proof itself. I found no structural shortcut there: the six retained rows,
cutoff 2, endpoint reference and root bookkeeping are dictated by the analysis, not by N0.

**Outline (B), pages in parentheses:** 1 Introduction (3½): main theorems, method map, evidence
boundary in one paragraph. 2 Kernel and row calculus (3½): cardinal kernel; reflection, odd
charts, S_n, λ = S − Δ, projections; row identity and cotangent sums; digamma toolkit; one
quadrature lemma. 3 The corner value (7): exact rows; square reference, κ and its enclosure;
aggregate; proof of Theorem A. 4 Completed model and finite comparison (18½): cancellation; scalar
maximum with cusp; model losses and C_* = c₁² + κ; central pair; Thm 4.A and proof; Cor 4.B;
Cor 4.C. 5 Localization for n ≥ 512 (4½): floors; corner descent from 256; proof of Theorem B.
6 Finite completion (4¼): positive interpolation; 2..40; 41..511 with the interface table;
evidence. 7 Declarations and references (2).

---------------------------------------------------------------------------------------------------

## 7. Companion, record, and what must stay

**Ranked material to move out of the journal paper:** (1) if B, the sharper n ≥ 320 tail (near
column, radius-dependent floors F_near/F_small/F_h/F_w, annulus, E13 outer geometry) as a companion
appendix "Lowering the analytic onset to 320", an explanatory strengthening that is not a premise
because the certificates double-cover 320..511; (2) the PD-T271 Arb K = 64 evaluation, as a
cross-check in the reproducibility record; (3) execution narration and inventories in §5.3, to the
reproducibility notes; (4) the degree-one formula (optional); (5) long base-value lists
(ul:near-base style): keep only consumed numbers, derivations to the companion.

**Historical items that must stay** (a referee must verify the certificate predicates): the exact
41/64/160 floor formulas; the far-leaf guard π/2 with 192 and gap 3/100; the corner lemma (256,
π/4 square, 1/30); u′ = 1/32, v′ = 9/512 and the 3π/16 rectangle; both norm witnesses (TREE without
f leaves, GRID otherwise) and 784/663; the π bracket and the binary64 → rational conversion; the
2..40 / 41.. split; the parity, closed-chart, collision and seam conventions; the evidence boundary
(sampled 199/238, selective retention).

**Process cost to flag.** Every restructuring invalidates the structural parts of
consolidation-audit.md, section5-expansion-review.md and affirmative-style-review.md. It also
invalidates `check_correspondence.py` (13 statements, 90 displays, 211 blocks). The mathematical
acceptances (H, E12, E14, E15, G01) stay valid as records of their own statements.

## 8. Uncertainty and limits

All gate values in §2.3 are base-degree enclosures; the all-n monotone transfers for Cor 4.B,
Cor 4.C and Lem 5.1′(ii) are unwritten (they look routine, the same pattern as the paper's current
transfers, but are unproved here). The §2.2 grid scans are MEASURED, not enclosures. Cost and size
projections use recorded runs and are not cost laws. I inspected f leaves only at 199 and 238, not
every returned degree in 192..319; this does not affect the conclusions. Page estimates are ±1 pp.

Files in `s-code/`: kappa_hand.py, kappa_hand2.py, kappa_runs.txt, kappa_terms.txt, abs_tail.py
(+ _run.txt, _out.json), onset_variants.py (+ _run.txt), uniform_far.py (+ _run.txt),
b_arch_arb.py (+ _run.txt), b_onsets.py (+ _run.txt). Total scientific CPU was under 1 minute.
