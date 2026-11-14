Rules 70a50d7

# C4C: companion audit-04, the finite-row telescope (comparison-unified.tex L1990–4020)

- **Auditor:** Claude Opus 5.5, xhigh. This is a subagent of the substantive Claude audit-04 (handoff 30). It audits Codex development. No Git state was changed and no repository file was edited. Outputs are only this file and `c4c-code/`.
- **Rules read** at head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoff 30 and the brief `claude-audit-brief-onset512-20261108.md`. Also read companion-paper/README.md, audit-03/c2b-companion.md, response-03.md, notation-pass.md and theory/J01. BUILD.md, review.md and CORRESPONDENCE-REVISION.md were skimmed through their pointers only (their build and artifact content is B4's scope).
- **Novelty:** this audit makes no novelty or mechanism judgement, so the IDEAS gate does not apply.
- **Source identity:**
  - `companion-paper/sections/comparison-unified.tex` is blob `2219128f…` (180398 B, SHA-256 `78a5b1b9…55a5`).
  - The paper twin is blob `3ccde190…` (SHA-256 `8ccd9883…bcf`).
  - Both blobs are identical at the freeze `24a98db4…` and at the head.
  - J01 has SHA-256 `2df76efb…5840`.
- **Pages:** from B4's fresh build `$A/build/companion/main.pdf` (147 p). The range is companion pp. 80–104.
- **Labels:** [D] a defect, [E] an editorial or pedagogical judgement, [I] information or a passed check. Severities are BLOCKING, MAJOR, MINOR, NOTE and EDITORIAL.

## 1. Verdicts

**Mathematics (L1990–4020): SUPPORTED. No BLOCKING finding and no constant error.** I re-derived the following, mainly by hand:
- the cutoff recurrence and the π²/6 triangle;
- the 7-term reference-match ledger;
- the variation counts for g̃;
- the V_A and V_B tables;
- the retained near, far, closest and central rows;
- the mesh rewrite;
- the uniform saving and monotonicity;
- the one-sided origin bound;
- every relative row (e_j, the half-line residual, the endpoint table, the cyclic vectors, the mesh, the pole-regular part, the cancellation and the shift);
- the final assembly, and both scalar gates.

Every constant and every hand-off value reproduces with exact rational intervals (§3.1). All finite-sample identities and inequalities that I tested numerically hold (§3.3).

**Agreement with the paper and with J01: CONSISTENT.**
- All 18 labelled formal blocks in or feeding this range are textually identical in the paper and the companion. This was checked with a regex extraction (`envs.py`).
- The gate statements, the constants j\*=23/250 and t\*=221/500, the thresholds (n≥32, 148/160, 192, 512) and all base values equal J01 §1–4. My values fall inside the J01 receipt intervals.

**Companion pedagogy for this range: IMPROVED, BUT NOT YET AT AC'S TARGET. ACCEPT AFTER REVISION.**
- There are 3 MAJOR (pedagogical; the theorem is sound), 8 MINOR, 3 NOTE and 1 EDITORIAL findings.
- Most audit-03 local gaps are now closed: M2, M3(a,c,d,e,g), m1–m6, m8, m10, m11 and e1–e4.
- Not fixed:
  - the pervasive printing of each argument twice (C2B-m12);
  - the notation traps (C2B-M4);
  - the atomic row identities (part of C2B-M1);
  - the missing ledger/roadmap and worked column.
- The response-03 status "FIXED, reviewed scope" for C2B-M1, M3(b), M3(f), M4, m7, m9 and m12 is therefore **not supported in full**. Details are in §2.

## 2. Audit-03 dispositions checked against the text

| ID | Response-03 status | Text at 24a (line) | Audit-04 verdict |
|---|---|---|---|
| C2B-M1 | FIXED | Signed finite row (L3297–3302), positive-sample factorization (L3305), e_r assembly (L3307–3318), closest-row e₀ (L3320–3321), and Σ\|v\|=−Σv+2Σv₊ (L2538, L2613) are present and correct (numerically: e_r error 2.8e-13, signed sum 6e-11). Still asserted without work: f_j=4𝖺/(w²−z²) (L2536, needs the parity/sine-shift computation σ∓·sin=∓cos); Σf_j=−sin b/w (L2537); the positive set \|z\|<w ↔ j∈{−r+1,…,r−1} under ρ≤π; and the signed-row computation from Σcot=n cot (L3297, no steps). | **PARTIAL** → C4C-M3 |
| C2B-M2 | FIXED | r(w), 𝓔 and both bounds are derived (L3159–3242). The residual formula and the four inputs precede the coefficients (L3246–3256). All three coefficients reproduce, but only if 𝓔 in the 2Δw·Σ𝓔 term is taken at the origin label v₀ (§4 m4). | FIXED (minor ambiguity) |
| C2B-M3(a) M_A,V_A | FIXED | L2314–2324. πA_L=max(Z+q,p) and πA_R=max(Z−q,p,q−Z) are correct. | FIXED. The text does not say A_L=2(\|C₋\|+\|C₊\|)/π at v=z. |
| M3(b) N_s | FIXED | N_s is defined before use (L788). L2352–2353 still says "each of the two scalar channels has supremum at most four, so \|N_s\|≤2·4=8"; in fact f≤1 by (uc:scalar-bounds), so each channel is ≤1. | **NOT FIXED** → m1 |
| M3(c) central sup<4 | FIXED | L2443–2447 (repeated verbatim at L2485–2487). Correct. | FIXED |
| M3(d) hole envelopes | FIXED | L3711–3718 (s>v by integrating R_e from π/2; entropy formula for s≤v). The per-side envelope dominates. | FIXED |
| M3(e) J_cen | FIXED | L2666–2676. Correct (measured ratio 0.19), but the extra +2log π/π factor in L2671 is not explained. | FIXED (m5) |
| M3(f) omitted collisions | FIXED | L2106–2108 and L2140–2141 give the bound and "one per pole channel". They do not say what the event is, why it forces \|x−y\|≥π−v (so 𝖺≤Pv/2), or why there is at most one row per channel. | **PARTIAL** → m2 |
| M3(g) C_j,E_j | FIXED | L1996–2008 and L2061–2083 (definition, recurrence, cancellation, E_∞). Checked numerically: \|E_∞−E₂−Δ₂\|≤1.7e-9. | FIXED |
| C2B-M4 notation | FIXED ("no inventory added") | The renames ε̂,ℓ̂,ε_h,ℓ_h,ε_d and Ω₁,Ω₂ were applied. Several traps remain (C4C-M2). There is no symbol table for 4.2. | **PARTIAL** → C4C-M2 |
| m1 | FIXED | L2750–2751 ("separated upper bound"). | FIXED |
| m2 | FIXED | L3095–3096. | FIXED |
| m3 | FIXED | L3148 (j>⌊n/2⌋≥16). | FIXED |
| m4 | FIXED | L3017. | FIXED |
| m5 | FIXED | L3320–3321. | FIXED |
| m6 | FIXED | S_disp is defined at L2845. The definition is repeated at L3322. | FIXED |
| m7 | FIXED | b=ξ+\|s\|=ρ/π is stated (L3093). The result 145ρ/(27n)<8ρ/n is still stated (L3106–3107) before its derivation (L3139–3147). | PARTIAL → m6 |
| m8 | FIXED | L2551–2552. | FIXED |
| m9 | FIXED | A reference to (ul:projections) was added (L2783). "The finite reflection formula" (L2785) is still unlabelled. | PARTIAL → m6 |
| m10, m11 | FIXED | L2401–2402; L2093–2094. | FIXED |
| m12 pacing | FIXED | 19 summary/proof twin blocks remain (C4C-M1). | **NOT FIXED** |
| e1–e4 | FIXED | L2193 (\|C\|cot e); the duplicate sentence is gone; L2636 ("weaker bound"); L2071–2072 (ℓ₀=sinc y). | FIXED |
| n1–n3 | FIXED | Outside this range or no action needed. The closed-domain continuity text is at L3844–3856. | OK |
| Ledger table / worked column / figures A–C (§5) | "optional … not adopted" (C2A-11, C3-02) | There is a 4-output re-entry table after the proof (localization p.105) and three n=512 gate numbers. There is no ledger at the start of the proof, no worked column of comparison allowances, and no figure in the range. | Not adopted → C4C-M1(b) |

## 3. Independent verification (actual executions; all under `$A/c4c-code/`)

All commands ran with exit 0. Total CPU was under 1 minute; the longest wall time was 9 s.

| Script | Kind | Result |
|---|---|---|
| `handoff_exact.py` (Python Fraction only; the auditor's own π by Machin, log by atanh, sin/cos by alternating series, outward rounding to 1e-45) → `handoff_exact.out` | exact intervals | 0 failures out of 33 PASS assertions. |
| `c4c_symbolic.py`, `c4c_symbolic_fix.py` (sympy 1.14) | symbolic | 44 identities pass in the first file. Of its 3 FAIL lines, two were sympy branch artefacts (log(S−v) with the sign of S−v unknown); they pass in the fix file with S=v+w, w>0, where the direct integral is also checked. The third was my own mistyped target rational, and the fix file recomputes it (3583/1836<2). |
| `c4c_rows.py` | numeric (double; MEASURED) | All checks pass after one harness parity bug, which was mine and is fixed (odd-n index start). |
| `c4c_scalar.py`, `c4c_varf.py`, `c4c_delta2.py` (scipy/mpmath) | numeric (MEASURED) | All checks pass. One harness artefact (catastrophic cancellation at the cusp) was replaced by `c4c_varf.py`. |

### 3.1 Exact hand-off values (displayed formulas uc:constants, uc:uniform-allowance and the two gate corollaries)

| n | 𝔗 | ē | K_D | C̄_E | C₄ | k_Wx | k_Wy | d_β | M(n) |
|---|---|---|---|---|---|---|---|---|---|
| 160 | 8.8964 | 0.28273 | 0.29626 | 2.14636 | 0.028803 | 1.09421 | 1.09864 | 0.004425 | 23.55 |
| 192 | 9.6045 | 0.24113 | 0.25419 | 1.82144 | 0.023537 | 0.92732 | 0.93048 | 0.003157 | 24.20 |
| 256 | 10.7766 | 0.18743 | 0.19929 | 1.40524 | 0.017202 | 0.71401 | 0.71586 | 0.001850 | 25.39 |
| 512 | 13.8761 | 0.10175 | 0.11007 | 0.75034 | 0.008240 | 0.37966 | 0.38017 | 0.000508 | 28.98 |

**Gates (all PASS):**
- **Absolute gate at (512, 1):**
  - (t\*+2K_D)/Θ = 0.04740 < 3/50, and tan(1/2) = 0.5463 > 1/2.
  - G(512,1) ≥ 0.534264702 > 534264/10⁶ > 1/2.
- **Absolute gate at (192, π/2):**
  - (t\*+2K_D)/Θ = 0.09801 < 1/10.
  - G ≥ 0.0983166549 with the text's 707107/10⁶ substitution (and 0.0983190 with the exact 1/√2 bracket), so G > 98316/10⁶ > 3/100.
- **Relative polynomial at 512:**
  - U = 13.8745, d_x = 2.7629 > 1, d_y = 3.1796.
  - ℓ_x − ℓ_y = 5/48 − d_β ∈ (0, 5/48).
  - max P = 0.0407859997585 < 40786/10⁶ < 41/1000 (see n1).
  - Vertex = 0.1473414757 < 3/20; the vertex and max identities agree interval-wise.
  - P(1/2) = −0.1430696691 < −143069/10⁶ < −1/7, and x\*, y\* > 0.
- **J01 receipt intervals:** all five reproduce (max P, P(½), vertex, G(512,1), G(192,π/2)).
- **Localization n=256** (consumers of this range): 𝔗 > 107/10, ē < 1/5, K_D < 1/5, C̄_E < 3/2, C₄ < 9/500, k_Wy < 93/100 and M(256) < 26 all hold.
- **Origin:** 160·B_out = 0.51896 < 1. The bracket [71/n² − 22/(45m)]₊ vanishes from n = 147, so the text's "n≥148" is true.

### 3.2 Symbolic checks (sympy) and hand checks

**Symbolic checks.** All of the following pass:
- square completion on x+y=ρ;
- the max and vertex identities and x\*, y\*;
- the absolute-gate reduction uΘ − t sin x − K(sin x+sin y) = Θ − A cos δ − B sin δ, with 𝖺 = cos h cos δ;
- the R_mesh rewrite, with Tail = −Z_nT_h − B₀T_g;
- the δ_aR_mesh identity;
- μ/D_h − 1/D′ = (1/2m){…};
- the closed form of S_disp(0) and its value 56/(9π²);
- the convolution identity for j=1..6;
- ℓ_j − D₀/ν − B₀log ν/ν = Ξ_j;
- the two reflection-product identities;
- B_t(s): its endpoints and both extrema −(t−½)²/2, and mean K_t = t−½;
- the branch numerator and d/dt[sin(t+e)/sin t];
- the parameter integral and its S-derivative;
- d′(z), d = (c(z/4) − c(z/2))/2, (r₀\*)″ and A_s′;
- d/dn(nB_out);
- that termwise maximization of m·G_φ (with C_B<8, P≤2, Γ≤g_n, ℓ̂≤log m) equals m·G_g exactly;
- A = 398/(11π²);
- 155/2, 152, 25760/104329, 160000/1083, 39073/1200, 395/48, 193/48, 193/3 and 119π/(24m²).

**Hand checks.** All agree:
- the 7-row reference-match ledger (20+32=52; 2+2+3=7; the wrap condition ⇔ \|x−y\|≥π−v);
- the counts for the general variation and for g̃ (12𝖬_e);
- the V_B entries, including 20+7/π<23, 3Γ_φ, 2pℓ̂, 6Pℓ̂, 26𝖺, 19.5<20 and 2.57<4;
- the near rows (117, 72, 121, 75 → 7/n+317/n²) and far rows (18𝖺/n, 48pH_n, 24q, 3𝖺/n);
- the closest-row and central-row constants;
- the mesh bounds;
- the uniform saving (A+B−√(A²+B²)>3);
- monotonicity;
- V_F = L/2 + (25/2)log(2m) + 37/3;
- the origin holes (119π/24m², 1/(8n²)) and the central-hole sign (b/π < 2/39 − 49/121 < −7/20);
- e_j and its four product coefficients (144/5, 56/3, 108/5, 18/5);
- the residual coefficients (4π²/27, 80/(9π), 10πm/(27n), 16ρm/(3π²j));
- the endpoint table;
- the cyclic vectors (194/175, 25n/16, 5/7, 31/42);
- the relative mesh (1/3 + 13/168 + 5/96);
- the pole-regular block (289/100, 67/20, 395/48, 193/48);
- the cancellation (39/2 + 16ℓ_h, 175/4, 20);
- the shift (19/6, 83/6, 77/3);
- the T_out constant (49.49 < 50);
- the absolute and relative gate proofs.

### 3.3 Numerical checks (MEASURED; finite scope; worst ratio to the stated bound)

**Rows.** n ∈ {32, 33, 47, 64, 160, 161, 512}, 120 random phases each, full triangle and ρ≤1:
- the sinc-row multiset equals the actual cot-row (6e-11);
- signed sum = 𝖺/m − sin b·τ(v/2)/w (6e-11), and closest row = 𝖺/m − sinc y·τ;
- the intermediate step proposed in C4C-M3 (step 4) also holds (`c4c_signed_step.py`, 2e-10);
- the positive sets are exactly {0}, {0}, {±1} on ρ≤1, and the closest row has none;
- the e_r identity holds (2.8e-13);
- closest-row bound 0.30, |J_end − C₂| / bound 0.044, central R_r/n/(L+6) 0.20, J_cen 0.19.

**Origin samples** (n=32..399 plus four larger n): K/(49/50) 0.98, |H_h−1|/(19/n²) 0.30, ΣD_h⁻¹/(25/54) 0.62.

**Wide domain** (ρ≤1, 400 phases × 5 n): K 0.98, |H_h−1| 0.32, |Ḣ_h| 0.41, |d(1/D_h)| 0.86, |g_j| 0.89, reciprocal-product derivative 0.95, ΣD_h⁻¹ 0.55. Also w±z ≥ (17/8)k (margin 0.017) and μw±z ≥ (19/10)k (margin 0.05). The central-row coefficient errors give 0.84 (row m) and 0.91 (row m−1).

**Scalar profile:**
- sup|Φ′| = 1.34 (≤12), sup|Φ″| = 9.1 (<35), sup f = 1, f(0) = 0.5213;
- Var_per f′ = 0.855 (<4);
- |D₀ − 𝖺D₀(0)| ≤ 0.044·(5ρ/3), and indeed ≤ 0.09ρ².

**F₀** (n = 32…4096):
- sup|F₀′| on [2h, π−h] is 0.049 of the bound;
- Var F₀′ is 0.022 and 0.023 of the bounds (grid lower bound);
- the central hole has max F₀ ≤ −1.20 (claimed < −1/25);
- the initial-hole envelope holds (margin 2e-7 as z→0), with d/(z/16) = 0.89.

**Half-line** (n ∈ {32, 64, 160, 512}, 300 phases × 12 labels):
- |𝓔 − (½−t)r(v)|/(5h/24) is 0.31;
- θ± ∈ (0, 1) with margin 0.09, and Σ|θ±−θ₀| ≤ ρ/π;
- the single-row residual increment is 0.18 of the displayed bound.

**Δ₂ = E_∞ − E₂ = Σ{Ξ_j(t)+Ξ_{j+1}(−t)}** holds at 4 phases (mpmath 30 digits, |diff| ≤ 1.7e-9, which is nsum tail error), and the ψ-form of ℓ_j holds to 4e-31.

## 4. Findings, prioritized

### MAJOR (pedagogical; the mathematics is sound)

**C4C-M1 [D/E] The proof is printed twice and has no map. This is audit-03 C2B-m12 and §5-1, unresolved.**
- **Location:** pp. 80–102.
- **(a) Problem: twin blocks.** Nineteen blocks state a compressed argument (mostly the paper paragraph) and then re-derive it, often with different symbols or constants:
  - L2093–2113 vs 2115–2147 (the reference ledger is derived twice, and L2133 uses an undefined z);
  - L2180–2196 vs 2197–2207 (near-verbatim);
  - L2214–2222 vs 2224–2258;
  - L2345–2353 vs 2354–2394;
  - L2396–2407 vs 2408–2427;
  - L2433–2451 vs 2453–2494 (the supremum sentence appears verbatim twice, at L2443 and L2485);
  - L2553–2559 vs 2560–2583;
  - L2603–2609 vs 2622–2651;
  - L2689–2737 vs 2739–2745;
  - L2747–2785 vs 2787–2796;
  - L3089–3108 vs 3110–3157;
  - L3159–3209 vs 3164–3242;
  - L3252–3259 vs 3261–3283 (the coefficient and the first-row assembly, twice);
  - L3334–3359 vs 3361–3392;
  - L3436–3448 vs 3450–3499;
  - L3522–3527 vs 3529–3557;
  - L3596–3600 vs 3602–3610;
  - L3690–3726 vs 3728–3777 (the root-free case twice);
  - L3778–3797 vs 3799–3833.
- **(b) Problem: no map.** No ledger opens the 30-page proof (L1522–3883, pp. 73–102). No worked column shows the reader how large the allowances are.
- **Impact:** the reader cannot tell the summary from the proof. Inconsistencies between the twins mislead (see m1). The essential structure is never visible: five telescope terms × three uses.
- **Fix (a):** keep each paper sentence as a one-line claim, followed by one proof. `check_correspondence.py` constrains only headings, labels, statements and numbered blocks, and 42 paper lines are already dropped.
- **Fix (b):** at L1532, add a table. Its rows are E_row, E_out, E_ret, R_mesh and R_log. Its columns are the absolute bound (uc:absolute-components and the global error), the origin bound (≥ −D, −B_out, −[…]₊, −𝓜, 0) and the relative bound (uc:relative-components), each with its page.
- Also add a worked column from §3.1: at n=512, 𝔗 = 13.88 against C̄_E = 0.750, ē = 0.102, K_D = 0.110, C₄ = 0.0082 and k_Wx = 0.380. This shows that 30 pages of allowances amount to about 6% of the main loss.

**C4C-M2 [D] Notation traps remain in 4.2. This is audit-03 C2B-M4, partly fixed.**
- **Problem.** The meanings collide inside the range, several within a few pages:
  - F_j is the actual sample (L2519, L3300–3316) and also (τ_j−1)/ν (L3111), alongside G_j = τ_j/ν.
  - w = 𝖺cot(z/2) (L2404) is twice the reference w = 𝖺cot(v/2)/2 used at L795, L1924 and L3246–3250, for the same subtracted 2𝖺cot·log sin term. w is also the chart distance rπ+b (L2514) and the weights w₁, w₂ (L3650).
  - e = ρ (L3575, L3613) and e = π−z (L3671, also L2433, L2941) appear within 60 lines, beside the generic separation e and Euler's e.
  - b is the chart offset ±y (L2513), ρ/π (L3093), 2cot(z/2)−4/z (L2867), a translation (L3646) and b_s (L3677).
  - r is the half-line residual r(w) (L3160) and also c_e+c_d−2𝖺 (L3613).
  - K is the sinc product (L2587), the BV kernel, K_t, and L+25log(2m)+193/3 (L3012).
  - M is max(|C|,|D|) (L2180), sup|F₀′| (L3819) and M(n).
  - δ is x−y (L3575), (x−y)/2 (L3919), ν/(2m) (L2128), as well as δ_r and δ_a.
  - "Writing x=z/2" (L2904) appears while the phase x is live.
  - "support I_i" (L2251) is stale after the rename to Ω_i.
  - φ is used as a phase point (E_n(φ), S_disp(φ), I_s(φ,z)) but is never defined. Localization L92 defines φ as an angle.
  - I_s(φ,z) at L3586 is undefined.
- **Impact:** a reader who cross-checks w or F_j gets a wrong factor or a wrong object. These are traps, not merely load.
- **Fix:** add local renames, for example: \mathsf F_j or ϑ_j for (τ_j−1)/ν; W = 𝖺cot(z/2) with W = 2w stated; e_c = π−z; β = ρ/π; r_c = c_e+c_d−2𝖺; K_B for the L3012 K; M_F = sup|F₀′|; ζ = z/2; φ = (x,y) defined once; I_s defined as I(C₋(v_s),C₊(v_s),v_s). Add a one-page 4.2 symbol table (symbol, meaning, first line).

**C4C-M3 [D] The atomic row identities are still asserted. This is part of audit-03 C2B-M1.**
- **Location:** L2536–2540 (p.86) and L3297–3302 (p.96).
- **Problem:** four steps are given without their work:
  1. f_j = 4𝖺/(w²−z²). This needs (z∓w)/2 = (odd)π/2 + (x∓b)/2, so σ∓·sin((z∓w)/2) = ∓cos((x∓b)/2), and the weights multiply to 𝖺.
  2. Σ_j f_j = −sin b/w. This uses Σ_k 1/(A−2kπ) = ½cot(A/2) and tan α + tan β = sin(α+β)/(cos α cos β).
  3. (f_j)₊ > 0 ⇔ |z| < w ⇔ j ∈ {−r+1, …, r−1} when ρ ≤ π.
  4. (1/nm)ΣF_j = 𝖺/m − sin b·τ(v/2)/w. Here the cot-sum gives −(1/m)[C₋tan((x−b+v)/2) + C₊tan((x+b−v)/2)], which still has to be reduced trigonometrically.
- **Impact:** the endpoint, origin and relative charges on pp. 86–97 rest on these identities. The reader can only check them numerically.
- **Fix:** add about 10 unnumbered lines. Steps 1–3 go after L2536 and step 4 after L3298. Each step is verified in §3.3.

### MINOR

- **m1 [D], L2352–2353, L2345–2348, L2291, L2928, L3829.**
  - "Each of the two scalar channels has supremum at most four, so |N_s| ≤ 8" is a false reason. By (uc:scalar-bounds), ½ < f ≤ 1, so each channel is ≤ 1 and |N_s| ≤ c_e+c_d ≤ 2. The bound 8 is a valid overestimate.
  - "Var N_s ≤ 12 … follow from (uc:scalar-bounds)": Lip f < 2 gives only 4π > 12. The value 12 needs |Φ′| ≤ 11, i.e. Lip f ≤ 6/π, from the derivative table in the proof (L471–474). The paper L965 has the same issue; the total stays < 23 either way.
  - Likewise D̄_φ = 4(c_e+c_d)/π (L2291) and "|f| ≤ 4" (L2928, L3829) are unexplained 4× overestimates of U₀/π ≤ (c_e+c_d)/π and of f ≤ 1.
  - **Fix:** state the true bounds and say the constants are deliberately loose. The constants need not change.
- **m2 [D], L2106–2108, L2140–2141 (omitted collision references).**
  - **Problem:** the event is not explained. It occurs when an endpoint row has an actual pole offset of exactly 0 or 1 (the wrap boundary (1−s±ξ)/2 + ν/(2m) ∈ ℤ). This forces |x−y| ≥ π−v, hence ρ ≥ π−v and 𝖺 = (P/2)cot(ρ/2) ≤ Pv/2. Because t_d + v_r/(2π) increases strictly in r, there is at most one such row per channel.
  - **Fix:** add two sentences.
- **m3 [D], L2816–2825 ("Consequently E_ret(0) = −2/m + …").**
  - **Problem:** the −2/m comes from J_cen(0) = 2/m plus four endpoint terms −𝖺/m (three charts plus the closest row). Those terms come from the e_r identity, which is proved only at L3296–3321, 500 lines later.
  - **Fix:** add a forward reference and that one line of bookkeeping.
- **m4 [D], L3243–3251 (residual increment).**
  - The sentence "Since |r(v)| ≤ …, cot(v/2) ≤ …, the residual is 2wΣ𝓔" makes inputs read as reasons.
  - The identity residual = −2wΣ±𝓔(h\*,v,θ±) is not derived. Its derivation is the two half-line families Ω₁ (Y = X+v) and Ω₂ (Y = π−X), each equal to −2wΣcot(Y) on (v, π/2). The sign is immaterial.
  - Specify Δ(w𝓔) = Δw·𝓔(v₀,θ₀) + w(v)·Δ𝓔. With 𝓔 at the actual v, the coefficient 4π²/27 is not reproduced: there is an extra 4π𝖺y²/(27j²). The bound itself holds (measured 0.18).
- **m5 [D], small hidden steps and first uses.**
  - L2133: z is undefined (use v).
  - L2139–2140: "Ξ_j = O(𝖺ν⁻²), producing 2𝖺/n" should give the explicit sum 16𝖺(1+2/m)/(π²m) < 2𝖺/n.
  - L2861: K ≥ 49/50, |H_h−1| ≤ 19/n² and ΣD_h⁻¹ ≤ 25/54 are asserted.
  - L3526: |D₀ − 𝖺D₀(0)| ≤ 5ρ/3 is unexplained. It follows from |U₀ − 𝖺U₀(0)| ≤ (5/4)ρ².
  - L2671: the extra 2log π/π factor is unexplained.
  - L2178: "The ordinary perturbation has the sharp coefficient needed here." is a dangling sentence.
- **m6 [E], L3106–3107 and L2785.**
  - The result 145ρ/(27n) < 8ρ/n is announced before its derivation (L3139–3147). Swap the order.
  - Label the "finite reflection formula".
- **m7 [D], L2747–2756 (uniform constant).**
  - **Problem:** the text never shows that (64+16L)/n is not a bound for C_{6,φ} alone. The termwise maximum (42 + 2L + (49L̄+24)/π)/n ≈ (65.2+17.6L)/n exceeds it, and is covered only together with the 3L̄/n saving. The text also does not show that G_g is the termwise maximum with C_B < 8, which gives 111/2 and 63. J01 states this as the "combined correlated allowance"; the companion does not.
  - **Fix:** add a three-line display (verified in §3.2).
- **m8 [E], L3926–3930 and L3976–3982 (gate proofs).**
  - Say that R ≤ A + B²/(2A) is used at h = ρ₁/2.
  - In the relative gate, cite (uc:central-pair-bounds) and write E_c ≤ (5/12)x^{3/2} ≤ (5/12)x² + (5/48)x. This explains where −5/12 in d_x and +5/48 in ℓ_x come from.

### NOTE

- **n1 [I], L4004 (max P₅₁₂ < 40786/10⁶).** The exact value is 0.04078599976, a margin of 2.4×10⁻¹⁰. The bound is valid, but a reader rechecking with 6-place logarithms cannot confirm it. The needed bound 41/1000 has margin 2.1×10⁻⁴. Suggest stating < 4079/10⁵.
- **n2 [I].** Every hand-off constant and gate in §3.1 reproduces from the displayed formulas with exact rationals, and matches J01 and the paper.
- **n3 [I].** The paper shares m1 (L965, L928), m4 (L1285) and the e=ρ / e=π−z collision (L1376, L1430). Any fix should be paired.

### EDITORIAL

- **e1, L3716–3723.** "…envelopes …, respectively" is followed by three expressions (midpoint, initial, central). Label them.

## 5. Pedagogical verdict and fix list for L1990–4020

**Verdict: ACCEPT AFTER REVISION.**
- **Strengths:**
  - purposeful paragraph openings;
  - the ABC−A₀B₀C₀ ordering example;
  - the signed-outer favourable-sign argument;
  - the shift telescoping;
  - the exact cyclic-vector treatment of collisions;
  - complete gate proofs, with all-real-n monotonicity;
  - every allowance is now traceable.
- **Remaining failures for a reader with university analysis:** (i) duplication without a map, (ii) symbol traps, (iii) four asserted atomic identities.

**Prioritized fixes:**
1. C4C-M3 (≈10 lines).
2. C4C-M2 (renames plus symbol table).
3. C4C-M1 (merge the twins; ledger table; n=512 worked column from §3.1).
4. m1–m4.
5. m5–m8, n1, e1.

Optional figures (audit-03 Figures A–C, especially the endpoint-chart lattice for L3361–3370) would still help, but are not required.

## 6. Coverage and limits

- **Read every line:** companion L1990–4020.
- **Read for context:** L1–130, L296–372, L440–530, L685–834, L1420–1990, and corner L340–372.
- **Paper twin:** compared by line containment (42 paper lines intentionally absent) and by the labelled-block comparison. Paper L960–972 and L1268–1290 were read.
- **Also read:** J01 in full; localization L180–200 and L270–360 (companion) and L350–428 (paper).
- **PDF:** pp. 81 and 96 were rendered and inspected. Both are legible, and the ledger table renders.
- **Not done:**
  - no `check_correspondence.py` run (B4's scope);
  - no rerun of J02, the J01 checker, I25 or the native campaigns;
  - J02's j>23/250 and t₀<221/500 are taken as premises.
- **Limits:** the numerical checks are MEASURED, on finite grids and random samples. They corroborate; they do not replace the written proofs.
- **Repository:** untouched.
