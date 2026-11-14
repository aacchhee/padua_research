# M5A — focused audit-05 of the Section 4.1–4.2 comparison text (both manuscripts)

- **Auditor:** Claude Opus 5.5, xhigh. This is an independent subagent in the focused Claude audit-05 (handoff 32). It audits Codex's response-04.
- **Rules:** read at branch head `33b9eca8167980cad0b0a491da7de64280c9a158`. Files read: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md and handoff 32.
- **Other inputs read:** response-04, audit-04, audit-04-manuscripts, and the audit-04 reports C4B, C4C, J01, N4 (findings sections) and P4 (P4-06/07 via audit-04-manuscripts).
- **Novelty:** no novelty or mechanism content is in scope, so the IDEAS gate is not applicable.
- **Git and repository:** no state-changing git command was run and no repository file was written. All outputs are this file and `m5a-code/`.

**Audited sources.** Both `comparison-unified.tex` files are byte-identical at the freeze `ad908acb` and at the head `33b9eca`.

| File | SHA-256 (verified) | Lines |
|---|---|---|
| paper `sections/comparison-unified.tex` | `9175a020…9234` | 1839 |
| companion `sections/comparison-unified.tex` | `d56a34a9…15af` | 4123 |
| paper localization | `cac0abf4…9e86` | |
| companion localization | `e2c527a2…df3a` | |
| originals at `24a98db` | paper `8ccd9883…7bcf`, companion `78a5b1b9…55a5` | |

These match `supplementary-manuscript-review-20261113.md`. Page numbers come from B5's fresh build text (`$A/build/text/*.txt`, `page-index.md`): companion §4.1 is pp. 50–71 and §4.2 is pp. 72–103; paper §4.1 is pp. 18–26 and §4.2 is pp. 27–38.

**Labels.** [D] = derived by hand here. [E] = executed here; the script is named. [I] = inference or judgement. A numerical agreement is MEASURED evidence at the sampled points, not a proof.

## 1. Verdict

**Mathematics of the changed §4.1–4.2 text: SOUND. No BLOCKING and no MAJOR finding.**

All of the following were independently reconstructed and are correct:
- the restored Lemma 4.2 reasons;
- the row-average and four atomic row identities;
- the interior/boundary qualification;
- the termwise-maximum and correlated-saving algebra;
- the J1/J2 gate clauses;
- the elementary-constant explanations.

All consequences check exactly or to interval precision at n = 192, 256, 295 and 512 (§3). The C4B-01 regression (MAJOR) is repaired, and C4C-M3 and C4B-02 (core display) are repaired. C4C-M1 is repaired: the 19 pairs are merged, and a ledger and an n = 512 column were added.

**Pedagogy against AC's criteria: much improved; ACCEPT after a small paired MINOR batch.** Ten findings: 7 MINOR, 1 EDITORIAL, 2 NOTE. One of them (M5A-01) corrects a false intermediate clause in both texts.

Response-04 claims "unique reasons retained" for the duplicate-pair consolidation. Three one-line reasons were in fact still lost; the supplementary review also marks these three pairs as retained (M5A-02). Two disposition statements are overstated (M5A-05, M5A-06).

**Paper/companion agreement: CONSISTENT.**
- All 35 formal blocks (statements and numbered displays) and all 56 labels of the two comparison files are textually identical at `ad908acb` [E s5].
- The only formal blocks changed since `24a98db` are:
  - `ul:log-series` (moved before Lemma 4.2; local renames);
  - `uc:kappa-series` (index renames);
  - Theorem 4.5 (inline definition of the signed board sum);
  - `uc:signed-outer` (h→h_m);
  - Cor 4.6 and Cor 4.7 (gate renames) [E s5b].
- Each change preserves meaning [D] (§4).

## 2. Reconstruction of the restored and added reasons [D]

**Lemma 4.2 (companion 455–789, pp. 58–64; paper 180–300).**

*Third-derivative argument.*
- The f‴ formula is verified (companion 649–650).
- f(0) = 𝔨₀/π follows from (uc:f-series) at w = 0.
- Since 𝔨₀ < 9/5 from the elementary brackets (now at 319, before the lemma), f(0)/8 < 9/(40π) < 3/40 because π > 3.
- For 0 < t < ½, the sine-ratio step gives (log R_t)′ = t cot(tw) − ½cot(w/2) > 0, since r cot r decreases on (0, π/2] and tw < w/2 < π/2. Hence R_t(w) ≤ R_t(π) = sin πt.
- The numerator t³ sin πt − 1/8 is ≤ 0 (with equality only at t = ½), and 0 < cos πt ≤ 1. Therefore dividing by cos πt only lowers the bound.
- The interval bounds are 2∫₀^{1/4}((22/7)t⁴ − 1/8) = 44/(35·1024) − 1/16 and 2(1/8)(27/512 − 1/8) = −37/2048. The total is −311/71680, exactly [E s1].
- |f‴| ≤ 23/40 + 3/40 = 13/20, using |∂ₜ| ≤ 3/4 + π/8 < 23/20 and cos πt ≥ 2(½ − t).

*Curvature bound.*
- 3/40 − t(½ − t)/(1 − t²)² = (3 + 34t² + 3t⁴ − 20t)/(40(1 − t²)²), and the numerator equals 34(t − 5/17)² + 1/17 + 3t⁴.
- With Q′ ≤ 5t/(1 − t²)² and cos πt ≤ π(½ − t), this gives 2Q′cos πt ≤ 10π·3/40 = 3π/4 [E s1, sympy].
- The upper bound on Φ″ is −π²/3 + π⁴/40 + 5π/4 + 3π/4 + 19/π ≤ −π²/12 + 2π + 19/π = 11.51 < 12.

*The 𝒲 bound and the closing chain.*
- g(s) = log cot((π − s)/4) has g′ = 1/(2cos(s/2)) ≥ ½, so 𝒲(π − w) ≥ w²/4 [E s1].
- The closing chain is H(w) − H₀ ≤ λ₀(f(w) − f(0)) − (J₀/π)𝒲(π − w) ≤ 3λ₀w²/(2π²) − J₀w²/(4π) ≤ −(π − 3)w²/(4π³). It uses λ₀ ≥ 0, f(w) − f(0) ≤ 3w²/(2π²) and maximality of the curvature convolution at 0.
- λ₀ < 1/(2π) holds because 4/π < 32/25 < 41/32 ≤ e^{1/4}. J₀ > 1/π holds because log π − γ > 11/10 − 3/5 = ½, and log π > 11/10 is now listed (J2-01).
- The cusp atom sits at w + s ≡ π. It contributes −(J₀/π)𝒲(π − |w|), which vanishes at w = 0, so it is counted once.
- The closed endpoints are fine: the convolution formula is stated on |w| ≤ π, and continuity is an extra safeguard.

*Measured confirmation [E s1, mpmath, 30–40 digits].*
- f‴/sin(w/2) ≤ −0.1041 < −311/71680.
- max|f‴| = 0.1056.
- H(w) − H₀ + (π − 3)w²/(4π³) ≤ −0.0046 at 12 points.
- H₀ = 0.310002264407.

The paper (pp. 21–22) states the same reasons more tersely and agrees with the companion.

**Row identity and row average (C4B-02; companion 1606–1654, p. 75; paper 722–754, p. 28).**
- The divided-difference evaluation G_n = [P_n(cos u) − P_n(cos v)]/(cos u − cos v) − cos(nu) has nu ≡ δ_rπ + x and nv_r = rπ + y − v_r, with (−1)^r = −(−1)^{δ_r}. With these, (−1)^{δ_r}G_n/2 = [𝖺(1 + cos v) − (p/2)sin u + (q/2)sin v]/(cos u − cos v) = C₋cot((u−v)/2) + C₊cot((u+v)/2).
- The −cos(nu) term cancels cos x·(cos u − cos v). The comparison text does not say so; see M5A-09.
- The weight identities: c_e cos((x−y+v)/2) = ½[2𝖺cos(v/2) + (q−p)sin(v/2)], hence C₋ = −c_e sin πη₋/(2 sin(v/2)), and similarly for C₊.
- The row average: |A+B| = |A| + |B| + g gives R_r/n = |C₋|𝒩_n(η₋)/n + |C₊|𝒩_n(η₊)/n + n⁻¹Σg.
- The pole profile (2L + 𝒞(η) − 2 log π)/π multiplied by |C∓| gives 2|C∓|L/π + c_{e,d}Φ(η∓)/(2 sin(v/2)), using the periodic extension of Φ for η ∉ [0,1]. The Riemann average of g gives I/π. Their sum is exactly A(v)L + ℬ(v).
- [E s2] confirms all of this at n = 192/256/512 over 40 random rows each:
  - the cot identity holds to 7e-11;
  - the offsets agree mod 1;
  - the C-identities hold to 1e-14;
  - the decomposition holds to 1e-11;
  - max n²·|pole error| = 0.347 ≤ 5;
  - the quoted row r = 253 at (0.4, 0.3), n = 512 has R/n = 5.2654934 against 𝒱 = 5.2654742.

**Four atomic row identities and the boundary qualification (C4C-M3; companion 2557–2584, p. 87; paper 1104–1130, p. 32).**
- Since j ≡ 1 − r, j − r and j + r are odd. This gives σ₋sin((z−w)/2) = −cos((x−b)/2) and σ₊sin((z+w)/2) = cos((x+b)/2).
- These cosines are the swapped weights (c_e = cos((x+b)/2), c_d = cos((x−b)/2)), so each channel has weight product 𝖺, and f_j = 4𝖺/(w² − z²).
- Σ_k 1/((2k+1)π + c) = −½tan(c/2) symmetrically. With tan α + tan β = sin(α+β)/(cos α cos β) and cos((b−x)/2)cos((b+x)/2) = 𝖺, this gives Σf_j = −sin b/w.
- Positive set: on ρ < π, 𝖺 > 0 and, for the three charts, |jπ + x| < w exactly for j ∈ {−r+1, …, r−1}. Strictness holds because x + |b| < π. On 𝖺 = 0 strict positivity fails (SR-M1's example), and both texts restrict to the interior and continue by linked sinc limits.
- The (1, −π, 0) value f₀ = 1, f_j = 0 is reproduced along the linked path [D], and Σ|f_j| → 1 = ℓ₁.
- Signed row: Σ_k cot((kπ+θ)/n) = n cot θ, with θ∓ = (δ∓r)π/2 + (x∓b±v)/2 and δ ± r odd, gives −(1/m){C₋tan + C₊tan}. The braces reduce to −𝖺 + (sin b/2)cot(v/2) = −𝖺 + (m/w) sin b·τ(v/2).
- [E s2 and s2b] all four hold at n = 192/256/512 over 60 random phases and 3 charts:
  - f_j to 7e-16;
  - Σf_j to 2.5e-8 (tail-limited);
  - positive sets exact;
  - signed row and intermediate form to 8e-15;
  - braces identity at 50 digits with exact rational inputs.

**Termwise maxima and correlated saving (C4C-m7 / P4-07; companion 2785–2818, p. 90; paper 1206–1235, p. 35).**
- The maximum of C_{6,φ} over 𝖺, p, q ≤ 1 is (42 + 2L + (49L̄ + 24)/π)/n + (317 + 5/12)/n². Its components are 21 + 21𝖺 (from 9 + 12, with 𝖺 ≤ 1) and (1 + 48p)L̄ + 24q ≤ 49L̄ + 24.
- The gap is 64 + 16L + 3L̄ − {…} = 25 + 17L − (73 + 49L)/π > (275 + 219L)/157 (using 1/π < 50/157), exactly as displayed [E s3, Fraction].
- The termwise maximum is ≈ (65.24 + 17.60L)/n, so (64 + 16L)/n alone is not a bound. The text says this.
- I re-derived C_{E,sep} − C_{E,φ} term by term:
  - D − D_φ = (1 − 𝖺)D_a;
  - G_g − G_φ ≥ 7L(M_A − M_A^φ)/m ≥ 28L(1 − 𝖺)/(π²m);
  - the C₆ gap ≥ 48L̄(1 − p)/(πn).
- A = 796/(11π²)·½ = 398/(11π²) > 18/5 and B = 48/π > 15. The minimum A + B − √(A² + B²) = 3.232 > 3, equivalent to 2(A − 3)(B − 3) > 9 [E s3].

**Gate clauses (J1-02 / P4-06; companion 3948–4123, pp. 104–106; paper 1664–1839, pp. 39–41).**
- Cor 4.6 states u ≥ 0, 𝔧 > 𝔧*, t₀ < t* and sin x ≥ 0.
- The bracket identity is A cos δ + B sin δ with A = 𝔗* cos h + C sin h and B = t* cos h. A and B are nonnegative and decreasing on [h₁, π/2] by the tangent condition, so R(h) ≤ R(h₁). Also A(h₁) ≥ 𝔗* cos h₁ gives B²/(2A) ≤ t*² cos h₁/(2𝔗*).
- The 707107/10⁶ substitution enters only adverse terms.
- Cor 4.7 states u ≥ 0, 𝔧 > 𝔧*, U* ≥ 0, and that d_β = (17L+27)/n² is positive and decreasing. Hence 0 < ℓ_x − ℓ_y = 5/48 − d_β. The 5/12 and 5/48 come from E_c ≤ (5/12)x^{3/2} ≤ (5/12)x² + (5/48)x.
- (𝔗 + A₄)′ > (L/n³)(n²/2 − 4n − 40) [D; E s3 at sample n].

[E s3, mpmath interval arithmetic, 60 digits, own implementation of uc:constants and uc:uniform-allowance] reproduces every gate base and all 60 Table-1 enclosures:
- G(512,1) = 0.5342647023;
- C/𝔗* = 0.0474 and 0.0980;
- G(192,π/2) = 0.0983190 exactly, and 0.0983166549 with the 707107 substitution;
- max 𝔭₅₁₂ = 0.040785999758 (margin 2.4e-10 under 40786/10⁶);
- vertex 0.147341;
- 𝔭₅₁₂(½) = −0.1430696691;
- d_x(512) = 2.7629 and d_β(512) = 5.08e-4;
- all 60 enclosures at 192/256/295/512 contain the recomputed intervals.
- The square-completion, maximum, vertex and x* identities hold symbolically.

**Elementary constants and other added reasons [D].**
- The ζ trapezoid/midpoint brackets are correct.
- The H_M − log(M+1) and H_M − log(M+½) monotonicity arguments are correct.
- e^{1/4} ≥ 41/32 is correct.
- e > 8/3 gives γ + log(8/π) < 8/5.
- log(28/11) > 37/40 holds via 2atanh(17/39).
- 𝖺D ≤ (7/2)(u − z) holds.
- C∞ < 9/4: δ² + δ𝔧 − t₀² = 71/6250000 exactly [E s6].
- |U₀ − 𝖺U₀(0)| ≤ (5/4)ρ²: since f′(0) = 0 and |f″| < 1, the bound is (Δ_x² + ρ²)/2 + r_c ≤ 5ρ²/4.
- Var N_s ≤ 12 and Var N_s′ ≤ 47/(2π) hold, using |Φ′| ≤ 12, |Φ″| < 35 over half a period, and a jump < 6.
- K_sinc ≥ 1 − 15/(2n²) and S_disp(0) ≥ 56/(9π²) hold, with 4·56/(9π²) − 2 > 22/45 because π² < 10.
- The cyclic-vector constants are correct: 2n/(5|k|) + 11n/(50k²), 194/175, 25n/16 and 9/(14c).
- The relative-mesh constants 1/3 + 13/168 + 5/96 are correct.
- The root-free threshold 3e²/20 − ρ/2 ≥ 7e²/80 ≥ ρ/2 is correct.
- The shift total 19/6, 83/6 and 77/3 ≤ 17L + 27 is correct.
- The C₄ assembly 155/2, 152 and 19/2 is correct.

## 3. Executed checks (all in `m5a-code/`, `PYTHONPATH=$A/pylib`, Python 3.13.18, mpmath 1.3.0, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1)

| Command (cwd `m5a-code`) | Exit | CPU | Result |
|---|---|---|---|
| `python3 -B s1_scalar.py` | 0 | 6 s | 25/25 PASS (Lemma 4.2 exact and mpmath items above) → `s1_scalar.out` |
| `python3 -B s2_rows.py` | 0 | 2 s | 32 numeric PASS; 2 symbolic FAIL lines were my harness (float inputs at a 1e-25 tolerance). Re-done in `s2b_symbolic.py` with exact rationals at 50 digits: PASS (0e-159) |
| `python3 -B s3_gates.py` | 0 | 1 s | ALL PASS. The first run had my own bug (ρ₁ = π passed for π/2); fixed in place and rerun → `s3_gates.out` |
| `python3 -B s4_pairs.py src` | 0 | 93 s | Sentence-level fuzzy survival listing for all 32 old pairs → `s4_pairs.out`; each flagged sentence inspected by hand (§5) |
| `python3 -B s5_blocks.py src`; `python3 -B s5b_bylabel.py src` | 0 | <1 s | Paired formal blocks 35/35 and labels 56/56 identical (old and new); 6 changed blocks listed above |
| `python3 -B s6_worked.py` | 0 | 205 s | Companion worked table reproduced: J(1,½,e) = −1.12467 (3 values of e), J(½,2,0.1) = −8.55698, J(½,2,1.2) = −0.28152, E∞ = 1.862235, b_full = 1.217561, C∞ = 1.801591 (quad error 8e-7; SciPy warnings on the cusp integrals, values agree to all printed digits), E₁₆₀ = 0.0100, E₅₁₂ = 0.0041, and 71/6250000 exact |
| `python3 -B s7_paper_adds.py src` | 0 | <1 min | Paper-added lines lacking a companion counterpart → `s7_paper_adds.out` (inspected; M5A-03) |
| `python3 -B s8_collision.py` | 0 | <1 s | Counterexample for M5A-01 at n = 32/192/512 |

Total CPU is about 6 min. Not run here: `check_correspondence.py`, builds, and the mutation controls. These are B5's scope; my s5 is an independent formal-block comparison of the comparison files only.

## 4. Notation changes preserve meaning (rename map `paper/notation-renames-audit04.json`, 31 entries) [D/E]

- **Gate renames.** Θ→𝔗*, G(n,·)→𝒢(n,·), P_n(ρ)→𝔭_n(ρ), U→U*, j*→𝔧*: each substitution occurs only in the gate objects (Cor 4.6/4.7, (74)–(75), Fig. 2, localization 104–140/469, certification 319). The Chebyshev P_n = T_{n+1}+T_n stays in the kernel evaluation (localization 23–24, comparison 726). No `𝔭_n(cos` occurs [E grep]. Θ now denotes only the half-line constant (uc:halfline). G_n denotes only the kernel.
- **Series indices.** p, q → i, ℓ for 𝔞, 𝔟, c_k, and ℓ→r for the odd index in (uc:kappa-series). 𝔞_0 = 1 agrees with the i ≥ 0 formula. The local log rule J_log, w_log, z_log, 𝒜_N and ζ₁₀ are consistent with the original truncation (J = 48, 40 Machin terms).
- **e_j, f_k → ε_j, η_k** (localization weights): consistent. Comparison text F_j stays as the actual sample; (τ_j−1)/ν and τ_j/ν become 𝖥_j and 𝖦_j.
- **Further renames in the comparison text:**
  - e_j → ε̂_j;
  - b = ρ/π → β_ρ (companion);
  - e = ρ → e_ρ and e = π − z → e_c (companion);
  - r → r_hl and r_c;
  - K → K_sinc and K_B;
  - M → M_C and M_F;
  - δ = x−y → Δ_x (companion 4.2);
  - x = z/2 → ζ.

  Each was checked at its definition and use. Meanings are preserved. Residual and new collisions are listed in M5A-04/05.
- **Theorem 4.5:** the added inline (2𝖭)⁻¹Σ_{Γ⁻}ε_{rs}H_{rs} matches the localization definitions of Γ⁻ and H_{rs} (S_n = (2𝖭)⁻¹Σ|H_{rs}|).

## 5. Duplicate-pair consolidations: own diff before reading the ledgers

I checked all 13 C4B and all 19 C4C pairs, not just the required 12, against the `24a98db` text.
- **Method:** s4 lists every old sentence without a close match. I then read by hand the flagged sentences and the retained derivations.
- **Hand reads in full:** B2, B4, B5, B6, B7, B9, B10, B11, B12, B13, C1, C3, C4, C5, C6, C10, C11, C12, C13, C14, C15, C16, C18 and C19, plus the reviewer-returned items in B2, C1, C5, C6, C18 and C19.
- **Result:** every restoration that the supplementary reviewer requested is present and correct:
  - B2: E = R − 2v log sin e, its derivative and the v = 0 case;
  - C1: wrap ⇒ ρ ≥ π − v ⇒ 𝖺 ≤ Pv/2, and the central-reference BV chain;
  - C5: the S < v branch;
  - C6: tan(e_c/2)cot e_c ≤ ½ and sup t|log t| = 1/e;
  - C18: s_s ≤ 3/2 and p log(ρ/p) ≤ ρ/e;
  - C19: the V domain [h_m, π−h_m] and log m ≤ L + 1/32.
- **Still lost:** three one-line reasons are lost (M5A-02). The supplementary table marks exactly these three pairs (C1 "tau", B5 "logarithmic primitive", C10 "quantified correlation minimum") as retained.
- **No other unique reason lost.** All other flagged sentences are either rephrased with the same content or were themselves duplicates.

## 6. First use and named tools in §4.1–4.2 (N4-01/02 list)

| Item | Paper | Companion |
|---|---|---|
| ρ, A, B, x, y, gate polynomial in roadmap/Fig. 2 | FIXED (loc 38, 79, 87–91, 104 before table/fig.) | FIXED (loc 277–296 before table/fig. at 322) |
| φ | FIXED (17) | FIXED (28) |
| I_s | FIXED (1523, before use) | FIXED (3653) |
| M in M tan(e/2) | FIXED (956) | FIXED (M_C, 2225) |
| c | FIXED (1484–1486) | FIXED (3508–3510) |
| θ₀ | FIXED (1407) | FIXED (3310) |
| U_{n−1} | FIXED (1466–1468) | already defined (3480) |
| Li₂ | FIXED (495) | FIXED (1159) |
| D_φ | FIXED (641, before the theorem) | **used in the new ledger table at 1557 (p. 74), defined at 2302/2310 (p. 84)** → M5A-06 |
| J_end/J_cen | FIXED (758–760) | FIXED (1629–1631) |
| L_{jk} | FIXED (corner 52) | FIXED (corner 112) |
| dot derivative | FIXED (1360), **but τ reused** → M5A-05 | FIXED (λ path, 3159–3161) |
| tangent partial fraction, second difference, BV quadrature, alternating sine/cos remainder | stated (451, 289, 1013, Elementary constants) | stated, except the alternating-remainder rule (M5A-03) |

## 7. Findings

**M5A-01 — MINOR (both texts; false intermediate reason in an added sentence).**
- **Location:**
  - companion `comparison-unified.tex:2178–2180` (§4.2, p. 82): "An omitted collision reference occurs when … It forces |x−y| ≥ π−v, hence 𝖺 ≤ Pv/2";
  - paper `:936–938` (p. 31): "This forces |x−y| ≥ π−v, hence ρ ≥ π−v …".
- **Reason [D, E s8]:**
  - On the right endpoint side (s = −y/π, rows 2m−j) the η₊ channel collides exactly when x + y = π − v. At such phases |x − y| can be far smaller than π − v.
  - Example at n = 32, 192, 512 with x = π − v − 0.4 and y = 0.4: η₊ ∈ ℤ, cos u = cos v_r at an actual sample, and |x−y| ≈ 2.3 < π − v ≈ 3.1.
  - The correct consequence is ρ ≥ π − v (one of x−y, y−x, x+y equals π − v). This still gives 𝖺 = (P/2)cot(ρ/2) ≤ Pv/2, so the charge 2P/(πn) and every constant stand. The at-most-one-row-per-channel count also stands, because the η₋ channel can collide on only one side.
  - This wording came from audit-04's own C4C-m2 suggestion.
- **Impact:** a false sentence in a proof; no claim affected.
- **Fix (paired prose):** "It forces ρ ≥ π − v (one of x ± y or y − x equals π − v), hence 𝖺 ≤ Pv/2." In the paper, also split the comma splice "cost 2𝖺/n, an exact collision occurs".

**M5A-02 — MINOR (companion; necessary one-line reasons lost in three consolidations; the ledger records them as retained).**
- **(a) C-pair 1, 2167–2175 (p. 82).**
  - The old text identified the prefactor: "The normalized prefactor is 2𝖺τ(v/2)/(π²ν), τ(w) = w cot w".
  - It also gave the per-row wrap cost 8P/(3πm(j−1)), which sums to 16PH_n/(3πn).
  - Both are now gone. "The prefactor difference uses 1−τ(v/2) ≤ v²/4" no longer says which prefactor. τ is used 360 lines before its in-text definition (2525); only the §4.2 table (1435) precedes it.
  - The paper keeps both (930–934).
- **(b) B-pair 5, 978–990 (p. 65).** The primitive ∫T_t dt = 4𝖺 log sin(t/2) is gone. The display passes from ∫T_t to 4𝖺 log 𝖺 − 8𝖺 log sin(ε/2) without it.
- **(c) C-pair 10, 2814–2818 (p. 90).** "The lower bound … follows from A cos x + B sin x ≤ √(A²+B²)" is gone. The text states "The minimum is A+B−√(A²+B²)" with no reason.
- **Impact:** AC's "needed derivations kept"; same failure mode as C4B-01, smaller.
- **Fix:** restore the three clauses verbatim from `24a98db` (companion only).
- **Evidence record:** correct the corresponding rows (B5, C1, C10) of `supplementary-manuscript-review-20261113.md` and `manuscript-duplicate-dispositions-20261113.md` by a dated note.

**M5A-03 — MINOR (companion less explicit than the paper; C4B-06 residuals).**
- **(a)** 932–936 (p. 65) still read "The sine chord gives a pole remainder at most 6+πt/6". The paper now names it: "the chord bound sin t ≥ 2t/π on [0,π/2]" (380). Also in this companion paragraph:
  - |N_s| ≤ 8 has no reason until 2384 (p. 85);
  - the pole decomposition and the sum to 7 in (uc:endpoint-envelope) are not displayed (C4B-06 item 826–830).
- **(b)** The gate proof (3993, p. 105) uses "the sine and cosine alternating series". Its remainder rule is stated in the paper's Elementary constants but not before this point in the companion.
- **(c)** Still unexplained:
  - 999 (p. 66) "The max formulas bound each subtracted integrand by one";
  - 1310–1311, the amplitude–phase step (Cauchy–Schwarz);
  - 620, the concavity reason for cos πt ≥ 2(½−t).
- **Fix:** copy the paper's two clauses. Add one line each for (c), together with a pointer for |N_s| ≤ c_e + c_d ≤ 2.
- **Disposition:** response-04 marks C4B-06 "DEVELOPED … expanded". It is partly done.

**M5A-04 — MINOR (both texts; new notation trap in a numbered display).**
- **Location:** companion 1662, 1708, 1715, 2352–2353 and 3662 (`uc:signed-outer`); paper 761, 787, 794, 1018–1019 and 1534.
- **Problem:**
  - "For t = y/π, h_m = π/m, set h_j(t) = …" defines the number h_m and the series family h_j(t) in one sentence.
  - After the audit-04 rename (map entry `F_0(h(`→`F_0(h_m(`), the products h_m(k+τ) and F_0(h_m(k+t)) read syntactically as the series h_m evaluated at k+τ.
- **Fix:** write π(k+τ)/m, or rename the cell width (e.g. ϑ_m) or the series (e.g. 𝗁_j). Paired; touches `uc:signed-outer`, so a new freeze is needed.

**M5A-05 — MINOR (remaining and new collisions; disposition C4C-n3 overstated).**
- **(a) Paper still has the shared collisions that C4C-n3 named.** Response-04 says "collisions corrected in both texts"; this is not true for the paper.
  - e = ρ (1513) and e = π − z (1569), 56 lines apart, are still present.
  - r(w) = cot w − 1/w (1384) and r = c_e + c_d − 2𝖺 (1551) are still present.
  - The companion fixed both (e_ρ/e_c, r_hl/r_c).
- **(b) Paper introduces a new τ collision.** The dot-derivative definition "(x,y) ↦ (τx, τy)" (1360–1361) uses τ right after τ_j (1355) and τ(w) = w cot w (930). The companion uses λ.
- **(c) Companion w trap persists (C4C-M2 residual).**
  - The §4.2 table (1435) gives w only as "endpoint distance rπ+b".
  - In 3311–3326 (p. 96), w is the half-amplitude 𝖺cot(v/2)/2 (|w| ≤ 4𝖺m/(3πj)).
  - In 3376–3402 (p. 97), w = rπ + b.
  - The definition of the half-amplitude is 1300 lines back (1976).
- **(d) Companion minor reuse:**
  - η± = log(1±c/n) (2753), 100 lines before Fig. 3's offsets η±;
  - e = π − z at 3027 and 3872 beside e_c;
  - ζ = z/2 (in the d′ computation) in a file where ζ(s) is the Riemann function;
  - the paper's D̄_φ factor-4 looseness note (C4C-m1, companion 2332–2335) is absent from the paper.
- **Fix:** paired local renames (e_ρ, e_c, r_hl, r_c, λ). Write w_r or 𝗐 at 3311–3326 and list both meanings in the table. Correct the C4C-n3 disposition.

**M5A-06 — MINOR (companion; first use in the new ledger table).**
- **Location:** 1553–1563 (p. 74).
- **Problem:** the table uses D_φ, G_φ, C_{6,φ}, 𝓜_φ and B_out before their definitions: (uc:phase-allowance) is at 2308 (p. 84) and B_out at 3068 (p. 94). There is no forward pointer. The paper defines D_φ before the theorem (641).
- **Fix:** add a caption clause "(defined in (uc:phase-allowance) and the origin estimate)", or define D_φ before the theorem as in the paper.

**M5A-07 — MINOR (companion; placement and provenance of the new figure/table).**
- Fig. 3 (row against its poles) and the worked-number table sit at pp. 90–91, after the uniform-constant proof. The row decomposition they illustrate is at p. 75.
- Fig. 3 has no `\label` and is never referenced. B5's page index also misses it.
- The table's lead-in says "the independent audit's direct finite-sum illustrations". That is project-internal provenance in a manuscript.
- The η arrows in Fig. 3 run from sample to pole, whereas η₋ ≡ n(u−v)/(2π) is measured from the pole. This is harmless because Φ(t) = Φ(1−t).
- I reproduced every number in the table [E s6].
- **Fix:** move both next to 1642 and add `\label`/`\ref`. Replace the lead-in with "Direct floating-point evaluation (not a proof input) gives". Either relabel the arrows or say "distance to the nearest sample".

**M5A-08 — EDITORIAL (eligible for an orchestrator in-place wording fix).**
- Companion 2920–2922: the merge artefact "…can be summed without estimating each term: Here S_disp denotes…". The monotonicity reason is stated twice (2919 and 2930).
- Companion 2578: "the prescribed parity gives f_j > 0 ⟺ |jπ+x| < rπ+b". The first equivalence comes from 𝖺 > 0 (the sign of 4𝖺/(w²−z²)); parity gives the second. The paper's wording is right.
- Paper 948: the dangling "The ordinary perturbation has the sharp coefficient needed here." (removed from the companion under C4C-m5).

**M5A-09 — NOTE (C4B-02 sub-item / N4-10 still open; not claimed fixed).** Both row identities (companion 1607, paper 723) cite `eq:angular-kernel`, which is the double-sum definition (7), as "the divided-difference kernel". The evaluation form is unlabelled (localization paper 23–24, companion 68–69). The cancellation of −cos(nu) = −(−1)^{δ_r}cos x is not mentioned; the companion localization (466–468) has it. **Fix:** label the evaluation form, cite it, and add the one clause.

**M5A-10 — NOTE.** The unnumbered termwise-maximum display differs between the texts: companion 2793 has (317+5/12)/n², paper 1214 has 318/n². Both are valid, and C̄_E uses 318. No action required. Note also that max 𝔭₅₁₂ < 40786/10⁶ keeps its 2.4e-10 margin (DECISION C4C-n1/P4-05). It is rigorous only through the exact checker or interval arithmetic, which s3 reproduces.

## 8. Response-04 dispositions in this range, checked against the text

| Row | Response-04 | Verdict |
|---|---|---|
| C4B-01 | DEVELOPED | **Confirmed.** All four reasons and the atom context are restored and correct (§2) |
| C4B-02 | DEVELOPED | Decomposition, weight identities and row lines confirmed. Label/citation sub-item open (M5A-09) |
| C4B-03 | DEVELOPED | Confirmed (1186, "For T_t ≥ 0") |
| C4B-04 | DEVELOPED | Confirmed (𝔭_n; §4) |
| C4B-05 | DEVELOPED, "unique … reasons retained" | **Partly.** B5 primitive lost (M5A-02b) |
| C4B-06 | DEVELOPED | **Partly** (M5A-03). Toolkit precedes the lemma; λ₀, 𝖺D, U₀ substitution, e > 8/3, log π > 11/10, 𝖺 ≥ 49/64, Z ≤ 2v log(2/e) and 2𝖺 ≥ p+q are now present |
| C4B-07 | DEVELOPED | Mostly. t_d/t_e are defined first, 𝖪/𝗄 → N_cot/q_cot/L_cot, and the p, q indices are renamed. h_m is a new trap (M5A-04); w is a residual (M5A-05c) |
| C4B-08 | DEVELOPED | Confirmed: f″ typography, the Lip attribution "first-derivative bounds", "independent of" wording gone |
| C4B-09 | DEVELOPED illustration | Present and numerically confirmed [E s6]; placement and provenance M5A-07 |
| C4B-10 | VERIFIED pairing | Consistent with my s5 (35 blocks / 56 labels in the comparison files) |
| C4C-M1 | DEVELOPED | Confirmed: 19 pairs merged, ledger and n = 512 column (values match Table 1). Lost reasons C1 and C10: M5A-02 |
| C4C-M2 | DEVELOPED | **Partly**: table plus F_j, e, b, r, K, M, δ, x = z/2, Ω_i, φ, I_s fixed; w and paper residuals remain (M5A-05) |
| C4C-M3 | DEVELOPED / checked | **Confirmed** (§2) |
| C4C-m1 | DEVELOPED | Confirmed in the companion and for N_s in the paper. Paper D̄_φ note absent (M5A-05d) |
| C4C-m2 | DEVELOPED | Event, count and conclusion present. **False clause** (M5A-01) |
| C4C-m3 | DEVELOPED | Confirmed (2895–2898; paper 1255–1261) |
| C4C-m4 | DEVELOPED | Confirmed (Δ(w𝓔) at the v₀, θ₀ reference; θ₀ defined) |
| C4C-m5 | DEVELOPED | Confirmed in the companion (z, explicit tail 16𝖺(1+2/m)/(π²m) < 2𝖺/n, K_sinc/H_h/ΣD_h⁻¹, 5ρ/3, 2 log π/π). The paper keeps its 948 sentence |
| C4C-m6 | DEVELOPED | Confirmed (145ρ/(27n) after derivation; reflection cites `ul:cardinal-reflection`) |
| C4C-m7, P4-07 | DEVELOPED | **Confirmed** (§2) |
| C4C-m8, J1-02, P4-06 | DEVELOPED | **Confirmed** in both texts (§2) |
| C4C-e1 | DEVELOPED | Confirmed (midpoint, initial and central labelled, 3801–3822) |
| C4C-n1/n2 | DECISION / RETAINED | Acceptable; the bounds are verified (s3) |
| C4C-n3 | DEVELOPED, "corrected in both texts" | **Overstated**: the paper e/r collisions remain (M5A-05a) |
| J2-01/02/03/08 | DEVELOPED | Confirmed (log π > 11/10 listed; toolkit before Lemma 4.2; checker/receipt named; J_log/w_log/z_log/ζ₁₀) |
| N4-01 (§4.1–4.2 items) | DEVELOPED | Fixed except D_φ in the companion ledger (M5A-06) and paper τ (M5A-05b) |
| N4-02 (§4.1–4.2 tools) | DEVELOPED | Fixed in the paper; companion alternating-remainder pointer missing (M5A-03b) |
| N4-03/05 | DEVELOPED | Confirmed for gates, series and the Cor 4.6 locals. h_m new (M5A-04) |
| Reopened C2B-M1, M3(b), M3(f), M4, m7, m9, m12; C2A-05/07/09/10 | DEVELOPED / recheck due | M1, M3(b), M3(f), m7, m9 confirmed. M4/C2A-10 partly (M5A-04/05). m12/C2A-09 confirmed, except M5A-02. C2A-05/07 partly (M5A-03) |

No row in this range is labelled FIXED. The overstated statements are C4C-n3 and the "reasons retained" claim behind C4B-05 / C4C-M1 (and the supplementary table).

## 9. Coverage and limits

- **Read in full:**
  - companion comparison 1–1450 and 1540–4123;
  - companion 1450–1540 (constants);
  - paper comparison 1–300, 450–560, 630–800, 900–1260, 1340–1600 and 1640–1839, plus all of the paper diff.
- **Read for context:** localization paper 1–145 and companion 40–80, 270–345 and 455–475.
- **Rendered pages:** inspected via B5's text extraction only (pp. 61–62 typesetting checked). I viewed no PDF images.
- **Not re-audited:** unchanged audit-04-verified derivations, except where a consolidation touched them; the certification/localization chapters (C4D range); the build and mutation controls (B5).
- **Measurement limits:** numerical checks are MEASURED at finite samples. The exact Fraction/interval checks cover the displayed rational identities and the gate and table bases only. The worked-table quadratures carry SciPy cusp warnings but agree to the printed digits.
