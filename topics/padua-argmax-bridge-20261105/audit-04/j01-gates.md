# Audit-04, part J01: the analytic tail from n>=512 (two scalar gates)

Auditor: Claude Opus 5.5, xhigh (substantive mathematical audit; adversarial
reading of an approved architecture). Role: independent auditor subagent of the
handoff-30 orchestrator. No state-changing Git command was run and no repository
file was created or edited. Outputs: this file and `j01-code/` beside it.

Labels: **[D]** my own derivation; **[E]** my own execution (commands below);
**[I]** inspection only. No novelty, mechanism or priority judgment is made
(approved architecture B), so the IDEAS/literature gate does not apply.

## 1. Identities audited

| Item | Identity |
|---|---|
| Rules read | AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at branch head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9` |
| Input head (handoff 30) | `f4c6229871a494b1b859d3140e81e9eb48b6b56a`. `git diff f4c6229 HEAD` is empty for every audited file [E] |
| TeX freeze | `24a98db4c3c4c4d0eede2e3929532956df87911b`. Paper sections at HEAD are byte-identical to it [E] |
| J01 | SHA-256 `2df76efb0e70535b08ade75ca4687e83ae6842d559203b5555a17585e3585840` |
| check.py / PREREGISTRATION | `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751` / `7c59d80a32c988ffe03c454fe7bc9a161c2afda0c998cd591fcc66b5ea9d665f`; both match receipt.json [E] |
| Paper comparison / localization / certification | `8ccd9883…bcf` / `14df874b…62` / `6fe37603…75` |

The distinct review pinned J01 `a74be3cf…ce56`. That is exactly the current
J01 truncated before "### Current status after distinct review"; I reproduced
the hash [E]. The paper sections changed after the review's `dcb27db`
association. I read the diff [I]: localization and certification gained
expository text only (the Bernstein inequality statement, de Casteljau, the
Taylor error and definitions), and no gate constant, guard or tail statement
changed. I audited the 24a text directly.

## 2. Coverage

Read in full [I]: J01; PREREGISTRATION; check.py; receipt.json;
`paper/sections/comparison-unified.tex` (all 1641 lines);
`localization-unified.tex` (all 432); `paper/section4-onset512-response.md`;
`audit-03/s-streamline.md`; handoff 30 and the onset512 brief; the rules.

Read in part [I]: `certification-unified.tex` l.140–440 (certificate, norms,
proxies, corner witness, far192, tables); the review's "Analytic gates" and
"Manuscript integration" sections (read after my reconstruction; I25, campaign
and E-01–E-04 sections are other parts' scope); the independent checker
`check.py` l.150–247; SECTION5-INTERFACE; J03 l.160–185; G01 l.1–80 and
140–240; report/results headers. J01 sources at statement/domain lines: E08
phase-global-error (3)–(4), E08-origin-lower, E14-wide-signed-outer, E15,
E12-corner256, C02-defect-dense-band (middle band), E01-near-frontier (E01-F2),
D29-floor512, C01-allclass-defect (exceptional x mode), D37-relative-wide,
E04-wide-retained-origin, E11 (both), E06/E07/H status lines, J02 §4, PD-T364
`padua-argmax-effective-2-20261105/theory/phase-structure.md`; audit-03 finding
lists and response-03 rows P-09, C3-03/04/15/16.

## 3. Executions (Python 3.13.18, mpmath 1.3.0, sympy 1.14.0; no Syvert, no native code, no archive code)

All scripts are in `j01-code/`. Library path for B and C:
`PYTHONPATH=…/scratchpad/audit3/pylib` (reused, not reinstalled).

| # | Command (cwd `j01-code/`) | Exit | User CPU |
|---|---|---|---|
| A | `python3 -B rerun/check_copy.py` (byte copy of frozen check.py, SHA `ff2859…1751`) | 0 | 0.19 s |
| B | `python3 -B j01_own.py` (my own Fraction/interval evaluator; does not import check.py) | 0 | 2.14 s |
| C | `python3 -B j01_supp.py` (corner-256 constants exact; scans MEASURED) | 0 | 3.23 s |
| D | `python3 -B j01_sym.py` (sympy identities) | 0 | 0.59 s |
| E | `python3 -B j01_slacks.py` (20-digit outward slacks) | 0 | 1.49 s |

Total CPU is about 7.6 s. Outputs are `*.out` and timings `*.time`.
- **Run A** reproduces every receipt interval: P512 max [0.040785, 0.040786],
  P512(1/2) [−0.143070, −0.143069], vertex [0.147341, 0.147342],
  G(512,1) [0.534264, 0.534265], G192 lower [0.098316, 0.098317],
  floor295 [0.050064, 0.050065], κ [0.917166, 0.921489],
  C* [1.841232, 1.847940]. Only the Python version differs (receipt 3.12.14).
- **Evaluator B was built independently.** π comes from Euler's
  arctan(1/2)+arctan(1/3) with alternating brackets. Logarithms use a 2^k
  reduction to [2/3, 4/3] with an atanh geometric tail, and log 2 =
  2 atanh(1/3). Sine and cosine use the Lagrange remainder. 1/√2 is an exact
  rational square bracket. γ uses M=2000, and outward rounding is on a 10^-60
  decimal grid.

## 4. Reconstruction

### 4.1 Radius-one quadratic (J01 §1–2; paper Cor. `uc:relative-gate`) [D, E]

- **The contract.** It is (uc:relative-comparison), n≥160, ρ≤1:
  S−Λc ≤ Ec − u(T−ē+A4+ρJW+𝔧) + C4 + kx·x + ky·y.
- **The contract's source checks out.** I re-summed the component table
  (uc:relative-components) with 𝖺=1−u and the one-sided origin bound. The
  results are 155/2 = 6+10+11+50+1/2, 152 = 148+4 and 19/2 = 8+3/2, and the
  −uA4 and −uρJW signs are correct.
- **Dropping terms.** u≥0, ρJW>0 and 𝔧>j0=23/250 allow dropping ρJW and
  replacing 𝔧 by j0.
- **The quadratic.** 1−cos z ≥ z²/2−z⁴/24 holds for all real z, so
  (1−cos z)/2 ≥ 11z²/48 on [0,1]. Since u=(1−cos x)/2+(1−cos y)/2 and
  U≥0, we get −uU ≤ −(11U/48)(x²+y²). Next, Ec ≤ (5/12)x^{3/2} − Bβ ≤
  (5/12)x^{3/2} (E11/`uc:central-pair-bounds`, ρ≤1<π/2). The central-pair
  constant 4I4/(π²√𝖺) < 4(319/360)/((197/20)(7/8)) ≈ 0.4113 < 5/12, with
  𝖺 ≥ cos²(1/2) > 49/64. Finally x^{3/2} ≤ x²+x/4. These give (1) with
  l1 = kx+5/48, d1 = 11U/48−5/12, l2 = ky and d2 = 11U/48. The asymmetric
  x-only Ec matches the n-mesh coordinate convention.
- **Identities.** Square completion (2), the maximum C4+g+f²/(4e) =
  C4+l1²/(4d1)+l2²/(4d2), the vertex f/(2e) = l1/(2d1)+l2/(2d2) and y* at
  ρ=1/2 are verified symbolically (run D).
- **All-real-n monotonicity [D].** n enters only through L=log n and m=n+1,
  both real.
  - Every (aL+c)/n^p term with p(aL+c)>a is decreasing. This covers kx, db,
    KD, D, C4, (64+16L)/n, and L/n, where c=0 requires L>1.
  - I checked the Mesh pieces by logarithmic derivatives. One example:
    b(n−1/2) < 2N(n+1/2) with N>b.
  - Gg and W are decreasing: log n/m (m/n ≤ 33/32 < L), log m/m,
    log(2m)/m and gn/m (m·gn′ < 1 < gn).
  - (T+A4)′ = (8L−3)/(π²n) − 4/n² − 40(1+2L)/(πn³) >
    (L/n³)(n²/2−4n−40). This uses π²<10, 8L−3 ≥ 5L, π>3 and 1+2L ≤ 3L. I
    re-derived it, and the bound is positive at 32 (=344·L/n³).
  - Hence U, d1, d2 increase and l1, l2, C4 decrease. Then max P_n and the
    vertex strictly decrease. Every base constant used beyond 512 has a
    monotone transfer: d1>1 (increasing), 0<db<5/48 (db decreasing), the
    tangent ratio (decreasing) and U≥0. The P_n(1/2) argument via the fixed
    segment x+y=1/2 is correct. Nothing fails between integers: every
    function is smooth in real n≥32. Measured on a 2800-point log grid over
    [160, 1.6·10⁹], all 14 monitored functions are strictly monotone in the
    proved direction (run C; MEASURED, not proof).
- **Bases at 512, exact (run B).** max P512 = 0.04078599976; slack below
  41/1000 is 2.1400024152e−4. P512(1/2) = −0.14306966912; slack below −1/7
  is 2.1252626552e−4. The vertex is 0.14734147572 < 3/20 < 1/2. Also
  d1 = 2.76291 > 1 and db = 5.0755e−4 < 5/48.
- **Tightness (MEASURED, run C).** 41/1000 first holds at n=511, −1/7 at
  n=512 and G(n,1)>1/2 at n=501. The constants are tuned to the onset. Exact
  arithmetic makes this rigorous (see J1-06).

### 4.2 Uniform floor Q>1/20 from 295 (J01 §3; paper `ul:selected-pairs`) [D, I, E]

- **Classes.** The three classes are exhaustive for n≥41. Endpoint index
  distance 1≤i≤4 forces θc ≤ (4π+1/2)/m̄ < 1/3 < π/6. Otherwise i≥5, which
  splits into θc<π/6 and θc≥π/6.
- **Class 1 (n≥64).** Q > 225/[1040(π+1/2)] ≈ 0.0594 > 1/20. I re-derived
  this from (m̄/n̄)(1/4−1/m̄)(2iA*)/(iπ+1/2) with A* ≥ 15/32, θc < 7/30, and
  the count m̄/4−1 times 2i.
- **Class 2 (n≥41).** Q ≥ (33/(16π√3))(1/6−1/m̄) > 35/656 > 1/20. Checked
  with π<22/7 and √3<26/15: 0.05387 > 0.05335.
- **Class 3, numerators.** Both projections and both endpoints were checked
  [D]. For r+s odd, (−1)^r G/2 = [𝖺(1+cos v) − (sin α/2)sin u +
  (sin β/2)sin v]/(cos u−cos v). Here v is always the m-mesh (second)
  coordinate, the "exceptional x mode" of C01:291 and D37. In the vertical
  projection v is the target; in the horizontal projection it is the selected
  periodic coordinate, shared by the pair. In both cases 1+cos v ≥
  1+cos(θc+b) ≥ 1−sin b, because θc ≤ π/2 and the upper endpoint uses the
  reflected physical index. So A(b) = a(1−sin b) − ρ̄/2 bounds both half
  numerators, with a ≥ 1−ρ̄²/4 since 𝖺 ≥ (1−ρ²/8)².
- **Class 3, the band formula.** I re-derived (`ul:band-formula`) [D]:
  - T_c = 4−2c+4 log c by splitting at 2/c−1;
  - the two-arc layer cake, n̄ T_c A/π − 2cA/w_b;
  - w_b ≥ (sin b)/2 from θc ≥ π/6;
  - mesh-sum errors f(b_−) for decreasing A and A/sin b;
  - m̄, n̄ ≥ n.
  The arcs have length 2 min(θc, b) and stay inside (0, π), so the formula
  holds without any b ≤ θc assumption.
- **New instance.** c=2, [π/100, π/4], ρ̄=1/2 [E, exact]:
  - all elementary inputs hold: sin(π/100) > 3/100; 11/4 < 4 log 2 < 14/5;
    cos(π/4) > 707/1000; 6π/25 > 471/625; log ratio 3.27213 < 10/3; and
    A(b) ≥ 7/320;
  - the substitutions are exact: 539/1936 = (11/4)(7/22)², 140/157 and
    400/157 come from π > 157/50, and 800/3 from sin b_− > 3/100;
  - A* = 211/320, I* = 19473/80000 and R* = 9511/6000, identical to
    E01-F2's Fh(1/2);
  - the true I, A(b_−) and R give a band value of 0.05140 at 295.
- **Result.** Fh(295) − 1/20 = **494837909/7694959360000** (≈ 6.43e−5) > 0,
  while Fh(294) − 1/20 = −402188497/143303973120000 < 0. So 295 is the exact
  integer onset of this bound. Fh increases in real n because A*, R* > 0.
  There is no radius interpolation (fixed ρ̄=1/2 covers every ρ≤1/2) and no
  sampled-degree extrapolation. Eligibility holds: every noncorner odd center
  has 0<J<n or 0<K<m. Hence λ < Λc + 41/1000 − 1/20 = Λc − 9/1000.

### 4.3 Absolute gate (J01 §4; paper Cor. `uc:absolute-gate`) [D, E]

- **Inequality (6).** Λc−S = E_n(0) + (M(0)−M(φ)) + (M(φ)−S(φ)).
  - E_n(0) > −ē, strict, n≥160.
  - M(0)−M(φ) = 4uL²/π² − (b_full−b_c)L − (C∞−C*) ≥ u(T+𝔧) − t0 sin x.
    This uses b_full−b_c ≤ 3u/π² with L>0, and C∞−C* ≤ −𝔧u + t0 p, where
    H0+v*>0 and z≥0.
  - The last bracket is ≥ −C̄E − KD(sin x+sin y) for n≥32.
  - Then 𝔧 > j0 and t0 < t (with u ≥ 0 and sin x ≥ 0) give (6), strictly.
- **The bracket.** With x=h+δ and y=h−δ, the bracket is exactly
  A cos δ + B sin δ, with A = Θcos h + C sin h, B = t cos h and C = t+2KD
  (symbolic identity verified, run D). It is ≤ √(A²+B²) for either sign of δ.
- **Monotonicity in h.** A′ = −Θ sin h + C cos h ≤ 0 iff tan h ≥ C/Θ, and
  B′ ≤ 0. Since A, B ≥ 0 on [0, π/2], R decreases on [h1, π/2].
- **The linearization is an upper bound, as required.** For a>0,
  (a+b²/(2a))² ≥ a²+b². Also B²/(2A) ≤ t²cos h1/(2Θ) because A ≥ Θ cos h1.
  At h1 = π/2, B=0 and R=A=C, so the bound is exact. This gives G exactly as
  stated.
- **Monotonicity in n.** Θ = T+j0 increases (8L−3>0). KD, C̄E and ē
  decrease. 1−cos h1 > 0 and sin h1, cos h1 ≥ 0. So G strictly increases in
  real n≥160, and C/Θ decreases, so the tangent condition persists.
- **Constant trace [I].**
  - T, D, Mesh, ē and KD are identical in paper `uc:constants`, E08 and E15.
  - E08's Gg = 7L·MAg/m + VBg/(2m) + (4/m)[7+(2/π)(5+2log 2m)] +
    4logπ/(πm) + 16/m expands exactly to the paper's grouped Gg: 111/2 and
    63 + log2 + 4logπ + 7log m + 16log(2m) + (3/2)g [D].
  - C̄E = CEold − 3H/n (E08 (4); paper l.1102–1113, where I re-checked
    2(A−3)(B−3) > 9).
  - Domains: global error n≥32 on the closed diamond; origin n≥160; model
    loss on the whole triangle.
  - j0 and t: J02 chain, inputs re-checked [E] with my own brackets.
    d* > 39/250, g0 < 43/125, H0 > 7/25 given κ > 9/10, and
    t0 = 2log2/π < 221/500. κ > 9/10 is J02's premise and is not
    re-checked in this part. All constants are valid at 192 and 512.
- **Bases [E].**
  - G(512,1) − 1/2 = 0.0342647023 with tan(1/2) − C/Θ = 0.49890.
  - G(192,π/2) − 3/100 = 0.0683166549 with the 707107/10^6 substitution
    (0.0683189868 with exact 1/√2), and 1 − C/Θ(192) = 0.90199.
  - The paper's intermediate claims C/Θ < 3/50 at (512,1) and < 1/10 at
    (192,π/2) are true (0.0474 and 0.0980).
  - The unlinearized √ gate gives 0.53442 and 0.09896, matching s-streamline's
    0.098958 planning value.

### 4.4 Seams, corners, ties, nodes, equality set (J01 §5; paper `ul:tail-location`) [D, I]

- **Coverage of each chart.** Noncorner charts with ρ ≤ 1/2 use 4.1+4.2.
  Every chart with 1/2 ≤ ρ ≤ 1 has S−Λc ≤ P_n(ρ) ≤ P_n(1/2) < −1/7: e>0, and
  the vertex is < 1/2. Every chart with 1 ≤ ρ ≤ π has S < Λc − 1/2.
  The closed seams at 1/2 and 1 are in both pieces.
- **Corner charts.** Every odd corner center is an actual nonnode corner:
  (n,m),(0,m) for even n and (n,m),(n,0) for odd n. (0,0) is even, and (n,0)
  is even for even n. The inward phases A=|α|=x, B=|β|=y and A+B ≤ 1/2 lie in
  [0,π/4]² ⊇ {A+B ≤ π/4}.
  - The corner lemma (n≥256) re-checked [E]: (1−cos(π/4))/2 > 7/48;
    T(256) > 107/10, ē < 1/5, KD < 1/5, C̄E < 3/2, C4 < 9/500,
    kWy < 93/100, M(256) < 26; δA−rUM > 2729/21000 (true 0.3219) and
    δD−2rUM > 49/1000 (true 0.1991); π⁴/6144 < rU; Ec(h,0) < 6/25 via
    4I4/π² < 9/25; Ec(h,h) < (9/25)/√2 < 4/15.
  - Both gates increase for real n≥256 [D: 8(qh−rU) > 3qh + (79/5)rU at L=1].
  - It therefore applies for every n≥512, strictly off the origin.
  - A corner chart with ρ in (1/2,1] is excluded by P_n, with ρ ≥ 1 by G. No
    part of the square beyond the diamond is needed.
- **Nodes.** A node lies on ρ=π of an adjacent odd chart, which the absolute
  gate covers (h1 ≤ h = π/2). PD-T364 also gives λ=1 there.
- **Conclusion.** The cover (PD-T364 and paper l.31–34, re-derived: the two
  odd-vertex index distances sum to 2) and the strict bounds leave exactly
  the corner origins. Parity reflection equates them, and compactness gives
  the maximum and the equality set for n≥512.

### 4.5 Integration and the source map [I, D]

- **Partition.** 2..40 (39 polynomial witnesses), 41..511 (471 degrees, 942
  trees) and ≥512 (J01). The tail's inputs are analytic comparisons, the M(n)
  analytic norm (not a certified norm) and five exact rational bases. There is
  **no finite-certificate premise**.
- **The frozen certificates' interface is consistent with J01.** The checker
  enforces:
  - far leaves only for n≥192 with a0+b0 ≥ 1/2 (ρ = π(a+b) ≥ π/2, no π
    needed), gap 3/100 and GRID norm;
  - ANALYTIC_E12_256 only for n≥256 on [0,π/4]²;
  - ACTUAL_THREE below 256 with u′=1/32, v′=9/512, 25/512 and the
    π/4×3π/16 rectangle;
  - floor tiers identical to `ul:finite-floors`. B_n's U/V/W/11711/48400
    constants are re-derived from the c=5/4 band [D], and
    max{a,min(b,c)} = min(b,max(a,c)) for a ≤ b, so the clamp is sound;
  - the π bracket 157/50 < π < 22/7 and 784/663 from π < 22/7.
  J01's G(n,π/2) covers exactly the consumed far contract for every n≥192.
- **Source map.**
  - Every retained estimate is used within its stated domain: E08 (3),(4),
    n≥32 closed diamond; E08-origin (4), n≥160; E14-wide-signed-outer (1),
    n≥32, ρ≤1; D37-relative-wide and E04-wide-retained-origin, n≥32, ρ≤1;
    E11 5/12, ρ≤1; E11 model, ρ≤π/2; E12, n≥256; E01-F2 Fh(r), n≥64.
  - No obsolete premise is silently required. E14 annular/halfnear320/
    outer320, the E13 geometry, E15's u-majorant, the near column, the 3/8
    specialization and the Bβ lower bound appear in no consumer chain.
  - Grep of all paper and companion TeX: no PD-T271, annulus, outer geometry,
    E13/E14, 21/40 or near column (only the certificate-table range
    "320:510").
  - G01 keeps the original n≥320 route and adds a dated onset512 alternative
    without PD-T271. report.md and the results file headers are current; the
    old wording sits under dated historical headings.
  - The frozen certificate metadata strings still name E15/PD-T271; this is
    disclosed (J1-04).
- **Response-03 rows.** P-09/C3-03 (outer-geometry block removed and
  replaced by G), C3-04 (tuple derived), C3-15 (derivative criterion) and
  C3-16 (radius-dependent tail floor removed; fixed 1/20 from 295) are
  confirmed by this reconstruction.

## 5. Findings

**J1-01 — NOTE (proof simplification, optional).**
- **Location:** J01 §2 and paper `comparison-unified.tex:1613–1640`.
- **Reason:** the consumers need neither "max P_n decreases" nor
  "P_n(1/2) decreases".
- **Simpler route:** on the closed quadrant x,y ≥ 0, the right side of (1),
  R_n(x,y) = C4 + l1x + l2y − d1x² − d2y², is strictly decreasing in real
  n≥512 at every point. C4, l1 and l2 decrease and d1, d2 increase, all
  already proved. Hence for every physical phase with ρ ≤ 1:
  S−Λc ≤ R_n ≤ R_512 ≤ P_512(ρ). The three base checks at 512 then give
  everything: max P_512 < 41/1000, vertex_512 < 1/2 (so P_512 decreases on
  [1/2,1]) and P_512(1/2) < −1/7.
- **Impact:** this removes identities (4) as a monotonicity tool, the
  optimizer-positivity argument and the db < 5/48 base check. The stated
  results stay correct as written.
- **Fix:** optional, a shorter paragraph. If adopted it is a proof change,
  so it needs a focused re-read.

**J1-02 — MINOR (manuscript proof steps implicit; J01 has them).**
- **Locations:** paper `comparison-unified.tex` lines 1597–1603, 1634–1635
  and 1536–1549.
- **Reason:** three one-line justifications are missing, against AC's
  "no step without its reasoning":
  - (a) Cor. `uc:relative-gate` defines U with j* but the proof only says
    "Dropping the positive ρJ_W". It omits replacing 𝔧 by j* (u ≥ 0 and
    𝔧 > j* from (uc:scalar-constants)).
  - (b) Positivity 0 < ℓx − ℓy = 5/48 − dβ for every n ≥ 512 rests on the
    base value dβ(512) < 5/48. The proof never states that dβ decreases;
    "all positive ℓ decrease" does not imply it.
  - (c) The absolute-gate proof uses 𝔧 > j*, t0 < t* (with sin x ≥ 0) and
    A ≥ Θ cos h without saying so. It also leaves implicit that R is
    evaluated at h1 = ρ1/2.
- **Impact:** none on validity; the gaps are in exposition. J01 §1–§4 and
  my derivations supply each step.
- **Fix:** insert "(using u≥0 and 𝔧>j_*)", "and d_β=(17L+27)/n² decreases",
  and "since 𝔧>j_*, t_0<t_*, sin x≥0 … and A(h_1)≥Θcos h_1" at those lines,
  with the companion mirrored. Adopting J1-01 removes (b).
- **Classification:** returned to the developer. It touches proof text, so it
  falls outside the auditor-fix limits.

**J1-03 — NOTE (dependency naming).**
- **Location:** J01 §5 table row "Limiting constants | J02 and analytic
  kappa/origin identities".
- **Reason:** j > 23/250 needs H0 > 7/25, which comes from
  (uc:origin-identity) C* = 4(γ+log(8/π))²/π² + κ. That identity in turn
  needs the sharp corner expansion H (Theorem 1.2; PROVED, analytic) and
  E_n(0) → 0 from the absolute error. I re-derived H0 = κ/2 + (2k0/π²)log(2/π)
  from C* = B − g0 + 2H0 [D]. The paper states the non-circularity (l.454–461).
- **Fix:** name H-sharp-corner-expansion and `uc:origin-identity` in that row.

**J1-04 — NOTE (frozen metadata).** Independent checker `check.py:182–186,
224–230` requires the frozen strings 'E15 general E09 u-majorant' and
'computer-assisted PD-T271' for far/corner leaves, although logically the far
branch is now J01 G(n,π/2) and the corner constants come from J02. Disclosed in
J03:175–180 and SECTION5-INTERFACE:45–46. Fix: one-line pointer to that
disclosure in J01's "Far branch" row; no evidence change.

**J1-05 — NOTE (checker versus printed paper claims).** `check.py` asserts
vertex<1/2 and the tangent conditions directly; the paper prints f/(2e)<3/20
(l.1624) and C/Θ<3/50, <1/10 (l.1559). These follow from the receipt's outward
six-place enclosures and I asserted them independently (runs B, C). Fix
(optional): assert the printed values verbatim in a future checker revision.

**J1-06 — NOTE (tight tuned onset).** Measured first-closing degrees: 511
(41/1000), 512 (−1/7), 501 (G(n,1)>1/2); exact slacks at 512 are about 2.1e−4,
and 295 is exact for Fh. Any later edit of C4, kx, ky, ē, CEbar, KD or j* can
silently break the onset. Fix: keep check.py in the reproduction set and rerun
it for any edit of `uc:constants`/`uc:uniform-allowance`.

**J1-07 — NOTE (provenance).** The receipt field "independent_execution:
PENDING" is historical pinned data, superseded by J01's dated addendum, the
distinct review and this rerun; the review's J01 hash is the pre-addendum J01
(§1). No action.

No BLOCKING or MAJOR finding. No auditor in-place fix was made: this subagent
has no write authority, and J1-02 is not fixable in place.

## 6. Verdict and dependency/trust conclusion

**ACCEPT J01 (PROVED) at its stated statement and dependency scope.** The
manuscript tail matches it. Every quantifier, sign and real-n transfer was
re-derived. The five finite bases were rerun with the frozen checker and
re-evaluated by an independent exact evaluator; all agree with the receipt.
For every integer n≥512 the tail rests on:
- the retained analytic comparisons, at their stated domains;
- the selected-pair lemma, at its existing proof plus the verified new band
  instance;
- E12-corner256, re-checked here;
- J02's elementary constants (J02 itself is outside this part; only the
  downstream j/t chain was re-checked here);
- the H corner expansion, via the origin identity;
- Python Fraction semantics for five short base comparisons.
It has no finite-certificate premise, and no removed n≥320 premise remains in
its chain. The far-192/corner-256/floor/norm/π/rectangle interface consumed
by the 41..511 certificates is consistent with J01 and the paper.

## 7. Not re-derived here (premises taken from accepted records)

- Internal proofs of the comparison theorem's components: (uc:telescope),
  pole/halfline errors, reference match, absolute/relative component tables,
  origin-lower internals, E14's signed outer bound, `uc:cancellation-lemma`,
  `uc:scalar-maximum`, the E11 convolution. Only statements, domains and
  assembly arithmetic (155/2, 152, 19/2, 3H/n, Gg) were checked.
- J02's κ>9/10 series and zeta/γ brackets (downstream j/t chain re-checked
  only); the H theorem and PD-T364 identities (inspected); C02 class-1/2
  counting beyond the displayed counts; the B_n^♯ tier margins; all finite
  certificates, I25/J03 and the native campaign (other audit parts).
