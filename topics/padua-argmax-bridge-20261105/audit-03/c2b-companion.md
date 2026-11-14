# C2B: companion audit, the finite-row telescope (comparison-unified.tex lines 2001-4037)

- **Auditor:** Claude Opus 5.5, xhigh. This is a subagent of the substantive Claude audit (handoff 28). It audits Codex's development and makes no Git changes and no repository edits.
- **Rules read:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md at head `f366535e1fa4ede566cb83bdc554220c12b307cf`. Also read `claude-audit-brief-20261108.md` in full (section 3 is this agent's task) and the companion README.md, BUILD.md and review.md.
- **Novelty scope:** this audit covers exposition and mathematics only. It has no novelty content, so the IDEAS gate does not apply.
- **Source identity:** `companion-paper/sections/comparison-unified.tex` is 177184 bytes, SHA-256 `6fa8e0b2…a092`. This equals the frozen identity in review.md. The paper counterpart `paper/sections/comparison-unified.tex` has SHA-256 `be20756e…0ce`.
- **Pages:** from X's fresh build `audit3/build/companion/main.pdf` (pdftotext). This range is companion pp. 79–110, inside subsection 4.2 (pp. 70–110).

Status labels:
- **[D]** a defect.
- **[E]** an editorial or pedagogical judgement.
- **[I]** information, for example a check that passed.

Severities follow the brief: BLOCKING, MAJOR, MINOR, NOTE and EDITORIAL.

## 1. Verdicts

**Mathematics of this range: SUPPORTED. No BLOCKING finding.**

- I redid every added derivation, table entry and rational constant in lines 2001–4037 by hand, with exact `Fraction` arithmetic or with high-precision numerics.
- None of them changes a constant of Proposition 4.5. None changes a constant handed to Section 4.
- The added explanations contain no sign, constant or quantifier error that affects a stated bound. Three minor imprecisions are listed in §3.
- I also checked the four added identities most likely to hide an error end to end against the original regular-sample cotangent row formula (§2.2):
  - the exact endpoint error e_r (L3330–3341);
  - J_cen(0)=2/m;
  - the E_ret(0) formula;
  - Σ|f_j|=ℓ_r.

**Pedagogy of this range: GOOD LOCAL MOTIVATION, NOT YET AT THE TARGET DEPTH.**

- Nearly every paragraph block opens with a clear purpose statement, for example L2344–2358, L2818–2832, L3057–3078, L3316–3325 and L3609–3622.
- The numerical ledgers are now explicit and correct.
- The intended reader still cannot rebuild some load-bearing steps:
  - Several identities are asserted rather than derived: "partial fractions show", "the signed-row sum … give", and the structure of the half-line residual.
  - Several allowances are stated without proof (M_A^φ, V_A^φ, the hole envelopes, J_cen, the "omitted collision" charge).
  - Symbols are reused many times within one subsection.
  - The original compressed argument and the expanded one are repeatedly printed back to back.
- Rating for this range: **ACCEPT AFTER REVISION**, with 4 MAJOR (pedagogical), 12 MINOR, 4 EDITORIAL and 3 NOTE findings.
- The MAJOR items are clarity failures for the intended reader. In each case the underlying theorem is sound.

**Agreement with the paper and with the later sections: CONSISTENT.**

- Every original paper line of this part is present in order. difflib finds only 6 split lines, at paper lines 54, 760, 842, 908, 1038 and 1165, which are the insertion points.
- The constants and thresholds of Prop. 4.5 (`uc:global-error`, `uc:analytic-norm`, `uc:origin-lower` for n≥160, and `uc:relative-comparison` for n≥160 with radii 1/2 and 1) are unchanged.
- I recomputed the Section 4 hand-off enclosures at n=320, 256 and 192 from this subsection's definitions. All hold (§2.3).

## 2. Independent verification (what was actually run)

### 2.1 Exact or elementary arithmetic

The script is `c2b-code/c2b_exact.py`; its output is in `c2b_exact.out`.

- **Result:** 130 checks pass. One check fails as expected and is explained below (C2B-m3).
- **Coverage, by block:**
  - **Reference ledger:** 20+32=52 and 2+2+3=7.
  - **Ordinary variation:** 12M*.
  - **V_B pole part:** 20+7/π<23; 47/(2π); 10+7/(2π); sup<6.
  - **Central cancellation pieces:** 3(1+log4)<15/2; aπlog2+aπ/2+d₊log(π/2)<9/2; 21/2+9<20; 3a and 7a.
  - **Near-index ledger:** even sums Σz²≤45π² and Σ|z|≤13π, odd sums 24π² and 8π, checked by grid over x∈[0,π]; 117, 72, 121, 75, then 7/n+317/n².
  - **Far ledger:** 20/9, 3/8, 18a, 1024/255≤81/20, and π²/24<5/12.
  - **Uniform saving:** A=398/(11π²), B=48/π, A+B−√(A²+B²)=3.23>3.
  - **Origin, retained rows:** S_disp(0)·π²≥56/9 for μ∈(1/2,1]; 4·56/90−2=22/45; 8·19·25/54<71.
  - **Origin, outer term:** 119π/(24m²); 1/(8n²); 391/392, 28/391 and 2/39−49/121<−7/20; 193/3.
  - **Origin thresholds:**
    - The bracket [71/n²−22/(45m)]₊ vanishes from **n=147**; the text says "for n≥148", which is true.
    - nB_out decreases on [32,4000] and is below 1 from **n=75**; at n=160 it equals 0.519.
  - **Relative endpoint references:** 29, 19, 22, 4; 145/π³; 6/j² and 24/(π³J).
  - **Half-line residual:** 5/3; 32/27+32/51+85/612=1.951<2.
  - **Product-rule tables:** 25760/104329 and 335/2646. Multiplied by 6+2/27 they give 1.49976<3/2 and 0.769<4/5.
  - **Geometric and sine columns:** 25/54 and 800/1083; Ḣ coefficient 4.79<5; 6250/81<78 and 160000/1083<148; 6.61<7 and 10.55<11; τ term.
  - **Central cyclic vectors:** 194/175<9/8; H₃₂≥7/2; 5/7 and 31/42.
  - **Relative mesh:** 13/168; 1/3+13/168+5/96<1/2.
  - **Pole-regular table:** all 16 entries, 731/96, 337/96, 395/48, 193/48, and the two sums 71089/2400<30 and 39073/1200<33.
  - **Cancellation charge:** 7/80; 39/2+16ℓ; 175/4; 20.
  - **Shift term:** 19/6, 83/6, 77/3; 77/3+83/192<27; 20/3.
  - **T_out constant:** 16.49, which gives 47 and 50.
  - **Assembly:** 677/10, 155/2, 82, 152, 19/2.
- **Hand checks with no script:**
  - The identity for R_mesh (L2739–2743), derived from the definitions.
  - The δ_a R_mesh identity (L3565–3570).
  - The partial-fraction expansion of ℓ_j (L2047–2071): both reflection cancellations, and cot(πt_e)−cot(πt_d)=−sin y/a.
  - The cutoff recurrence (L2073–2080).
  - The convolution identity and the π²/6 triangle (L2087–2131).
  - The sine sum giving cos y.
  - The limit equal to E_∞: the log²j terms cancel because B₀=4a/π², and the log j terms because D₀=a(𝒞(t_d)+𝒞(t_e))/π².
  - The digamma and trapezoid argument (L2024–2036).
  - The stationary equations and the derivative of sin(t+e)/sin t (L2307–2319).
  - The parameter integral (L2448–2457).
  - The weights of the cyclic vector, A+B−a≤aρ²/6 and the m−1 coefficient bound.
  - The Shift regrouping (L3937–3946).
  - The model drop −u(T+j)+E_c.
  - The weighted-to-ordinary conversion at L3999.

### 2.2 Numerical checks (MEASURED; finite grids, supporting the explanation only)

The scripts are `c2b_rows.py`, `c2b_scalar.py`, `c2b_misc.py`, `c2b_defect.py` and `c2b_origin_conv.py`. Their outputs are the matching `*.out` files. Each test below gives the worst value found.

**Row identities**
- e_r identity (L3330–3341), for all three charts and the closest row. Rows were built from the original identity (−1)^δ G_n/2 = C cot((u−v)/2)+D cot((u+v)/2), at n∈{32,33,47,160,321} with 60 random phases on ρ≤1.
  - The largest |actual−formula| is 8.7e−14.
  - The positive sample sets are exactly {0},{0},{−1,1}.
  - The closest row has no positive sample on ρ≤1.
- Σ_j|f_j| = ℓ_r: holds to truncation error 2e−6.
- The reference row equals 4a/(w²−z²) at every index j: error 4.5e−14 (see C2B-M1).
- Boundary value at (1,−π,0): the reference row is f₀=1 and f_j=0 otherwise.
- J_cen(0)=2/m: the deviation is O(phase), for example 9e−7 at phase 1e−6.
- E_ret(0): the formula matches the rows. The actual values of m·E_ret(0) are 0.445 at n=32 and 0.501 at n=160, while the proved lower bound 22/45−71m/n² is 0.042 at n=160.
- Σ_{r∉A₆}1/|sin v_r| ≤ 2mH_n: worst ratio 0.52.

**Scalar profile and cancellation bounds**
- sup of the L-coefficient over M_A^φ: **0.9989**. The combined variation over V_A^φ: **0.9989**. Both bounds hold and are nearly sharp, which is why they need a derivation (C2B-M3).
- Central cancellation: sup per side 0.73 (claimed <4); variation over both sides 2.6 (claimed <20).
- Relative hole envelopes (L3855–3856): ratios 0.33 (central) and 0.95 (initial). b_s nonincreasing ✓; combined sup ≤ 0.66·3ρ.

**F_0 bounds** (n=32…5000)
- Initial-hole envelope: ratio 0.26.
- F_0 on z≥21π/22: at most −1.20 (claimed <−1/25).
- Var F₀′/V ≤ 0.023 and sup|F₀′|/M ≤ 0.05.

**Pole-regular table**
- All 16 entries, on 300 random phases per radius and both signs: worst ratio 0.20.

**Variation and quadrature bounds**
- Var f/(24ε/sin e) ≤ 0.29 and Var g/(8max/sin e) ≤ 0.994 (sharp).
- Matched-cell defect (exact primitive plus digamma tail): |𝓔−(1/2−t)r(v)|/(5h_*/24) ≤ 0.42.

**Elementary inequalities used in the added text**
- 1/z−cot z ≤ πz/6; −log(sin z/z) ≤ z²/3; |f_a′|≤a and |f_a|≤az.
- 0 ≤ [2m sin(w/2m)]⁻¹−1/w ≤ w/(20m²).
- 1−τ ≤ 2t²/5; 1−u cot u ≤ u² and |(u cot u)′| ≤ 2u.
- (c_e+c_d)/w ≤ 1, with equality only in the limit.
- |h₂| ≤ r₀ (0.95); far-index K > 1/6 and |H_h−1| ≤ u².
- ‖L_n′‖₁ ≤ (9/8)nH_n (0.43).
- cot(v/2) ≤ 8/(3v₀) and the cotangent-difference bound.

A harness error of mine produced two spurious failures (wrong index parity, and a truncated tail). Both were corrected and the scripts rerun. The `.out` files record the corrected runs.

### 2.3 Hand-off constants (`c2b_handoff.py`, mpmath at 40 digits, j at its proved floor 23/250)

**n=320, against ul:near-base.** All 13 enclosures hold:

| Quantity | Computed | Bound |
|---|---|---|
| T | 11.7319 | >293/25 |
| D | 0.13383 | <27/200 |
| 𝓜 | 0.017109 | <7/400 |
| ē | 0.154066 | <249/1600 |
| C₄ | 0.0135369 | <677/50000 |
| k_Nx | 0.551497 | <705963/1280000 and <11031/20000 |
| k_Ny | 0.552718 | <56602113/102400000 and <11056/20000 |
| U_N | base margin 0.0147 | J_N=0.04249>21/500 |
| k_Wx | 0.58281 | <583/1000 |
| k_Wy | 0.58403 | <117/200 |
| T−ē+j | margin 0.0148 | >2331/200 |

**n=256.** Every bound holds: T>107/10, ē<1/5, K_D<1/5, C̄_E=1.405<3/2, C₄<9/500, k_Wy=0.716<93/100 and M(256)=25.39<26.

**n=192.** T=9.604>19/2, ē=0.241<1/4 and K_D=0.254<13/50.

The 1/20000, 3/1000, 99/2500, 13/500 and 1/30 gaps named in the task do not occur in lines 2001–4037; they are in localization. I verified only the inputs that this range supplies to them, listed above. I did not reopen theory/E12, E14 or E15.

**Interface fact to state.** M(n) is not monotone: M(320)=26.45 exceeds M(256). The localization text handles this correctly at L1745–1774, through the gate polynomial.

## 3. Findings, prioritized

### MAJOR (pedagogical; the mathematics is sound)

**C2B-M1 [D] Load-bearing row identities are asserted, not derived.** Locations: L2572 (p.89) and L3328–3341 (p.100).

- **Problem.** L2572 says only that "Partial fractions show Σ_j|f_j|=ℓ_r". L3328 says only that "the signed-row sum and its positive samples give … the finite identity" e_r. These two identities connect the actual board to the reference C₂. Every retained-row, origin and relative endpoint charge depends on them. The reader has (uc:sinc-row) and nothing else.
- **Missing steps**, all verified numerically above:
  1. When w≠|z|, the sinc formula reduces exactly to **f_j = 4a/(w²−z²)**. For r=1, b=±y this uses c_e+c_d = 2cos(x/2)cos(b/2) and a=(cos x+cos b)/2.
  2. By the cotangent partial fraction, Σ_{j≡1−r} 4a/(w²−(jπ+x)²) = −sin b/w. For r=1 this is (1/(4w))·2 sin w/(cos x−cos w)·4a, with sin w=−sin b and cos w=−cos b.
  3. With Σ|v_j| = −Σv_j + 2Σ(v_j)₊ (stated at L2645), this gives ℓ_r = sin b/w + 8aΣ_{|z|<w}1/(w²−z²).
  4. For the actual row, Σ_k cot((kπ+θ)/n) = n cot θ (used only at L2839) gives the signed sum, (1/nm)ΣF_j = a/m − sin b·τ(v/2)/w.
  5. With cos u − cos v = −(u²−v²)K/2, each sample is F_j/(nm) = 4μaH_h/D_h + μg_j/(D_hK).
  6. Subtraction then gives e_r term by term.
- **Impact.** The reader cannot check pp. 88–102, which take the identity as given.
- **Fix.** Insert steps 1–6 (about 12 lines, unnumbered displays) after L2574 and before L3330. Coordinated remedy for the paper: one clause at paper L931, "here f_j=4a/(w²−z²)".

**C2B-M2 [D] The half-line residual increment has no visible source formula.** Location: L3276–3290 (p.99).

- **Problem.** The single-row increment has three coefficients: 16ρm/(3π²j), (4π²/27+80/(9π))y/j and (10πm/(27n))y/j². None can be rebuilt from the text, because the text never says what the residual is in terms of 𝓔.
- **Reconstruction.** I recovered all three coefficients after inferring the following:
  - residual = 2w·Σ_±𝓔(h_*,v,θ_±);
  - Δ(residual) = 2Δw·Σ𝓔 + 2w·ΣΔ𝓔, with |w| ≤ 4am/(3πj) and |Δw| ≤ 4amy/(9j²);
  - |𝓔| ≤ |r(v)|/2+5h/24, with |r(v)| ≤ πv/6;
  - Lipschitz constants 4/π+5h/3 ≤ 2 and 5/3.
- **Fix.** Write the residual formula and these four bounds as a short derivation. Then each displayed coefficient becomes a product the reader can check.

**C2B-M3 [D] Several allowances are stated with no derivation in either manuscript.** Each needs a short proof or a pointer. Each value was verified numerically in §2.2. The locations, with a fix for each:

- **(a) M_A^φ and V_A^φ** (L2364–2365, p.85). These are nearly sharp (ratio 0.9989). Fix: derive them from πA_L = max(Z+q,p) and πA_R = max(Z−q,p,q−Z), with Z=2a cot(z/2), together with 0 ≤ 2/z−cot(z/2) ≤ 2/π. These formulas already appear as πg_L, πg_R at L3634, but only for the relative case.
- **(b) The pole numerator N_s** is used at L2386–2435 (and at L830) but is defined only at L3628. On top of that, L2394 says "each of the two scalar channels has supremum at most four". Since f≤1, each channel c·f is at most 1, so |N_s|≤2, and the stated 8 is a convenient overestimate. Fix: define N_s=c_e f(z±δ)+c_d f(z∓ρ) at first use, and correct the explanation.
- **(c)** "Central cancellation supremum below four" (L2483, L2521, p.87) is never derived. Fix: |R| ≤ p·max(log2,−log sin e), plus the b_s and d₊ terms.
- **(d)** The hole envelopes ρ[log(π/(2z))+log π] and ρ[7+4(−log sin e)] (L3855–3856, p.108) are not derived. Fix: |R(p/2,s,e)| ≤ p(−log sin e) follows by integrating R_e from π/2, and it covers the s≤v case through the entropy formula.
- **(e)** J_cen ≤ (12+2L)/n (L2699–2701, p.90) rests only on "the weighted pole bound applied before taking linked limits". Fix: show that each row sum is at most (|C|+|D|)(2L/π)+2·max(c/(2 sin(v/2)))·Φ + O(n⁻²).
- **(f)** "Omitted collision references cost 2P/(πn)" (L2178, L2193, L2211, p.82). The text never says what an omitted collision reference is, when it is omitted, or how many there are. Fix: name the event, give its count, and show the bound.
- **(g)** The "temporary cutoff" reference C_j and E_j (L2073) is used without definition. Fix: state that C_j = sinc y + Σ_{r<j}ℓ_r(x,y) + Σ_{r≤j}ℓ_r(x,−y), E_j = C_j + D₀𝓗_j + B₀𝒬_j, and display the cancellation of log²j and log j in the limit (L2142–2154). The reader is told only that this cancellation "displays each constant".

**C2B-M4 [E] Symbols are reused many times within subsection 4.2, and two meanings are redefined locally.**

- **Local redefinition.** At L3835 (p.108), "ε=h/2, ℓ=−log sin ε" is redefined locally. This happens while the global ε=3π/(2m) and ℓ from (uc:phase-allowance) are still live in G_φ, and L3890–3901 then replaces this ℓ by log m. There is no mathematical error, because both ℓ's are at most log m, but the reader is trapped.
- **Other collisions inside pp. 79–110:**

  | Symbol | Meanings in this range |
  |---|---|
  | ε | P/4 (L2245); ε_n=log(m/n); 3π/(2m); h/2 |
  | e | separation; Euler's number (4a/e, ρ/e); e_j, e_r, e₀ |
  | b | chart offset; b(z)=2cot(z/2)−4/z; ξ+\|s\| (L3132); b_L, b_R; b₀; b_full |
  | u | 1−a; sample angle u_j |
  | k | wrap index k_±; distance index k=r±j; residue index; sample index |
  | K | sinc product; BV kernel K(z), K_t; K_D; L+25log(2m)+193/3 (L3044) |
  | M | M(n); M=sup\|F₀′\| (L3957); M_*; M_A; M_i |
  | T | T; T₀; T_R; T=2tan(e/2) (L2975); T_out; T_τ; T_g |
  | H | H; H_n; H_h; H(w); H_j(q); H_R |
  | ℓ | ℓ_r; −log sin ε; ℓ₀ (undefined) |
  | D | D(v); D; D₀; D_h; D′; D_φ |

- **Fix.** Add a one-page notation table at the start of 4.2, with symbol, meaning and first use. Rename the local quantities, for example ε_c=h/2 and ℓ_c (and state that the global ε=3π/(2m) is the first initial cell edge h(3/2)), K_n for the L3044 K, and β for b=ρ/π. Avoid e as a separation wherever Euler's e appears.

### MINOR

1. **C2B-m1 [D], L2776 (p.92).** "Termwise maximization gives the separated sum C_{E,sep}=C̄_E+3H/n" should read "≤". The C₆ term alone has a termwise maximum strictly below its share: at n=32, n·C₆,sep=136.1 against 142.8. Fix: write ≤, or define C_{E,sep} as C̄_E+3H/n.
2. **C2B-m2 [D], L3172 (p.97).** "u=πν/(2m)<π/4" does not follow from the stated 5j/6≤ν≤7j/6, which would allow u up to 7π/24. It follows from j≤⌊n/2⌋ and |s|≤1/π, so ν≤n/2+1/π. Fix: state that.
3. **C2B-m3 [D], L3189–3190 (p.98).** The inequality (2b/π²)(4/(jν)+2/ν³) ≤ 12b/(π²j²) fails at j=2 (ratio 6.53/6) and holds for j≥3. It is used only for j>⌊n/2⌋. Fix: add "for j≥3 (here j>n/2)".
4. **C2B-m4 [E], L3049–3053 (p.96).** "The threshold 160 has a specific arithmetic role. By that degree…" overstates. The geometric bracket vanishes from n=147 and nB_out<1 holds from n=75. So 160 is a convenient round onset (see L1572), not the first degree at which the argument works. Fix: say so.
5. **C2B-m5 [D], L3341 (p.100).** The closest-row formula e₀ omits positive samples. That is correct on ρ≤1, but unexplained: a positive sample would need μy+x>π. In the absolute version (L2684) positive samples can exist. Fix: one sentence.
6. **C2B-m6 [E], L2866 (p.93).** S_disp(0) is used about 480 lines before S_disp is defined at L3342. Fix: define it at L2862.
7. **C2B-m7 [E], L3132/L3144 (p.97).** The substitution b=ξ+|s|=ρ/π is silent. It is what turns 145b/(π²n) into 145ρ/(π³n). The same result, 145ρ/(27n)<8ρ/n, is stated at L3144 and derived only at L3176–3181. Fix: state b=ρ/π, and put the derivation before the result.
8. **C2B-m8 [E], L2585 (p.89).** The bound (c_e+c_d)/w ≤ 1 is not obvious for the chart (1,−y) as y→π, where w→0. Fix: give c_e+c_d=2cos(x/2)cos(b/2) ≤ π−y=w.
9. **C2B-m9 [E], L2803–2805 (p.92).** "phase folding" and "the finite reflection formula" are invoked without statement or cross-reference. They are needed to pass from the triangle to every signed cardinal sum in (uc:analytic-norm). Fix: add the label references.
10. **C2B-m10 [E], L2448–2458 (p.87).** The parameter-integral evaluation treats only S≥v. Fix: add that for S<v the integral is monotone in S and at most 2v log 2.
11. **C2B-m11 [E], L2167–2217 (pp.82–83).** "Per row" charges mix unnormalized T₀ units (16|w|/π) with normalized units (10a/(π²nν)). Fix: state the normalization 1/(nm) once, at L2185.
12. **C2B-m12 [E], pacing across the whole range.** The original compressed argument and its expansion appear back to back, repeating the same proof:
    - L2250–2266 vs 2267–2277;
    - L2386–2392 vs 2393–2435;
    - L2756–2762 vs 2766–2769;
    - L3248–3250 vs 3252–3269;
    - L3662–3756 vs 3757–3787, where the pole-regular table is derived twice;
    - L2078–2080 vs 2073–2078.

    The reader cannot tell the summary from the proof. check_correspondence.py enforces only headings, labels, numbered statements and numbered displays, so the prose can be merged. Fix: keep each original sentence as a one-line claim, then give one proof.

### EDITORIAL

1. **C2B-e1, L2277 (p.84), also paper L827.** "C cot e" should be "|C| cot e".
2. **C2B-e2, L2078–2080.** The sentence "The h_j,g_j recurrences therefore show…" repeats the previous sentence.
3. **C2B-e3, L2669–2670.** The text gives 40a/(9π²m). With the stated Σz⁻²≤3/(8π²) the charge is 10a/(3π²m), so the text uses Σ≤1/(2π²) instead. The bound is still valid; align the two.
4. **C2B-e4, L2143.** "ℓ₀" is undefined. It means sinc y, the r=0 term.

### NOTE

- **C2B-n1 [I], the phase diagram** (certification, p.145; outside this range, checked because the task asks).
  - The diagram is accurate. Near region a+b≤1/(2π) ⟺ ρ≤1/2; analytic-far region a+b≥1/2 ⟺ ρ≥π/2, eligible from n≥192; the unshaded band uses predicates. The labels agree with the text.
  - Suggestion: add a dashed line a+b=1/π for the wide radius ρ≤1 used by the second line of (uc:relative-comparison), and note that a,b there are not the comparison's a=c_ec_d.
- **C2B-n2 [I].** The continuity passage to closed domains (L3982–3994) is correct. Collisions lie on finitely many lines, and both sides of each bound are continuous, including Γ_φ at p=0. One sentence naming the continuity of the right-hand sides would complete it.
- **C2B-n3 [I].** I found no discrepancy with the paper: hypotheses, constants, thresholds (n≥32 for allowances, n≥160 for origin and relative bounds) and both radii agree.

## 4. Block-by-block assessment (purpose, prerequisites, definitions, gaps)

| Lines (pp.) | Block | Assessment |
|---|---|---|
| 2001–2229 (79–83) | Δ₂ identification, digamma bounds, partial fractions, cutoff recurrence, convolution and π²/6, finite charge ledger | The purpose and the triangle/square picture (L2095–2099) are very good. Gaps: M3(f,g), m11, e2, e4. All algebra checked. |
| 2231–2342 (83–85) | BV principle; perturbed-cancellation variation | A usable BV statement, with hypotheses (L2232–2239). The four-cut count is clear and correct. Pacing issue m12. |
| 2344–2530 (85–88) | Absolute outer charges, V_B table | A good roadmap (L2351–2358). Gaps: M3(a,b,c). The other constants are verified. |
| 2532–2701 (88–90) | Retained endpoint rows | The ABC−A₀B₀C₀ ordering example (L2576–2583) is excellent. Gaps: M1, m8, e3, M3(e). |
| 2703–2816 (91–92) | Mesh tails, R_log, uniform constant, monotonicity | Algebra exact; the correlation-saving argument is clear. Issues: m1, m9. The monotonicity proof is adequate. |
| 2818–3056 (92–96) | One-sided origin bound | The best-motivated block, explaining why it is one-sided and where the signs come from. All arithmetic is exact. Issues: m4, m6. |
| 3057–3315 (96–100) | Relative row charges | The motivation for fixed labels and the straight path (L3111–3117) is clear. Issues: M2, m2, m3, m7. |
| 3316–3550 (100–103) | Exact endpoint sets; central cyclic vectors | The membership argument is good. The U_{n−1} explanation is clear. Issues: M1(b), m5. |
| 3551–3607 (103–104) | Relative mesh | Complete and checkable. |
| 3609–3985 (104–110) | Signed outer increment | The favourable L-sign argument (L3652–3660) and the Shift telescoping (L3937–3958) are exemplary. Issues: M3(d), M4, m12. |
| 3987–4037 (110) | Assembly | Term-by-term matching is complete and correct. |

**Prerequisites used by this range.** The range assumes the following without restating it:
- Riemann–Stieltjes integration against dF for BV functions. It is used in the cell-kernel identities. A one-line statement of the integration-by-parts formula ∫B dF′ would make L3266–3268 self-contained.
- The digamma series and recurrence (stated earlier).
- The Chebyshev U_{n−1} definition (given at L3459).
- The finite sum Σ_k cot((kπ+θ)/n) = n cot θ. It is used twice but never proved; it deserves a two-line proof or a citation.

**Hidden-work phrases still present.**
- "Partial fractions show" (L2572): see M1.
- "follow directly" (L2611): adequate.
- "Direct differentiation gives" (L3198; L2938 is fine): adequate.
- "the same argument" / "the same bound" (L2211, omitted collisions): see M3(f).
- "the weighted pole bound applied before…" (L2699): see M3(e).
- "Integrating them and using midpoint BV error" (L3857): the envelopes themselves are not derived, see M3(d).
- "Termwise maximization" (L2775): see m1.
- "Splitting the mesh terms…proves their decrease" (L2801): acceptable.

## 5. Figures and worked examples that would most help

1. **A ledger table at the start of 4.2 (highest value).** Rows: E_row, E_out, E_ret, R_mesh, R_log. Columns: absolute bound, origin (one-sided) bound and relative bound, each with its formula label and page. The reader then always knows where they are in a 40-page proof.
2. **A worked numerical column at n=320 (and n=32).** Give the actual sizes D, 𝓜, ē, B_out, C̄_E, K_D, C₄, J_N, k_Nx and T, using the values in §2.3. This shows which allowances matter: T≈11.7 against corrections of about 0.15–0.6.
3. **Figure A, the cancellation geometry of one row.** Plot |C cot t| and |D cot(t+e)| on [0,π]. Mark the supports I₁, I₂, the minimum −2min, and the at most four cuts. This serves L2250–2329.
4. **Figure B, the two offset cell families on [0,π].** Mark the initial holes (total 4h) and the central holes (total 2h). This one figure explains the hole terms in G_φ, B_out, the pole-regular quadrature and the cancellation charge.
5. **Figure C, the four endpoint charts.** Draw (w,z) lattice points for (1,±y) and (2,−y), with the positive samples |z|<μw marked and k₋,k₊ labelled. This visualises the L3384–3390 table.

## 6. Prioritized fix list for this range

1. **M1:** derive f_j=4a/(w²−z²), Σ|f_j|=ℓ_r, the signed row sum and e_r (about 15 lines). Make the coordinated one-clause addition to the paper.
2. **M3:** supply the derivations of M_A^φ/V_A^φ, N_s and its bound, the central supremum, the hole envelopes, J_cen, omitted collisions, and C_j/E_j with the logarithmic cancellation.
3. **M2:** state the residual = 2wΣ𝓔 formula and the four input bounds.
4. **M4:** add the notation table and rename the local ε, ℓ, K, b and M.
5. **m12:** merge the duplicated summary and proof pairs. Add the §5 ledger table and the worked n=320 column; optionally add Figures A–C.
6. **Remaining items:** m1–m11, e1–e4 and n1.

## 7. Coverage and limits

- **Read:** every line from 2001 to 4037 of the companion comparison section. Lines 1460–2000 were read for context only, and they are another agent's range. Also read paper lines 1–530 for definitions, the corresponding paper text, and the hand-off blocks in localization (L1005–1030, 1498–1512, 1720–1774). The phase diagram source (certification L640–700) was read.
- **Not verified in this range:** these are original paper claims that the companion does not expand.
  - The proof of (uc:halfline), which is before L2001.
  - The absolute closest-row positive-part estimate (L2684–2690).
  - The interior of the J_cen bound, beyond a plausibility check.
  - The count behind the "omitted collisions" charge.
- **Excluded:** E12, E14 and E15 theory records were not reopened. No native certificate or degree campaign was run. I did not build the PDF; page numbers come from X's build.
- **CPU:** about 3 CPU-minutes in total.
- **Repository state:** no repository file was created or edited. `git status` is clean at the head above.
