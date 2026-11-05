# Independent audit: F4 uniform signed Padua coefficient norm

Auditor: Claude (Opus 5.5), supplementary independent mathematical check,
subagent of the orchestrator. Not the required Claude audit record unless
the orchestrator adopts it as such. No git state changed; no repository
file edited.

- Repository: /home/user/padua_research, branch
  `codex/padua-mz-2d-frontier-20261105`, HEAD
  `ed9aaa9fc2546a54d7822b31f39dac7e141a9238`.
- Target: `topics/padua-mz-2d-frontier-20261105/theory/f4-uniform-density-bound.md`,
  SHA-256 `cee004269514e238499885ae32154deb0f6616e56d2e52806d37b282df8621b2`
  (same hash the Codex supplementary check reviewed).
- Read in full: target; `topics/padua-mz-2d-20261101/definitions.md`;
  PD-T112 (`mz2d-hyperinterpolation-absolute.md`), PD-T113, PD-T114,
  PD-T111 (`mz2d-lower-corner-weights.md`), PD-T017 (`m2-cardinal-lower.md`),
  PD-T022 (`m3-upper-ratio.md`); PD-T101 section 1 (cardinal normalization,
  `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`);
  PD-T013 positivity lines; `attempts/F4.md`, `ideas-f4.md`,
  `independent-checks-math.md` (F4 parts, used only for comparison),
  `code/independent_f4_check.py`.

## Verdict

**PASS. No blocking or major finding.** I reconstructed every step of the
proof and found it correct for every integer m>=2 and every 0<=n<=m-1,
with no hidden dependence on signed-weight positivity, signed Gram
positivity, or a signed spectral bound. The only spectral input is the
proved one-dimensional *positive* CC bound PD-T022. The constant
C* = 4 sqrt(2) pi/(pi-4/3) + (68/3)(1/2+1/pi) = 28.376334831123... is
right, and the rational bound 1336/45 < 30 is right. My findings are
editorial, or minor at most (citations, notation, a loosely worded
sentence, and stale "pending" wording). None of them affects the theorem,
the constant, or uniformity in m.

## Step-by-step reconstruction

### S0. Norm identity (PD-T112), domain/range — PASS
H_(m,n) f = sum_{|alpha|<=n} Q_m(f phi_alpha) phi_alpha (PD-T113), maps
C([-1,1]^2) (sup norm) into Pi_n with L2(dxdy). Coefficient duality gives
||Hf||_2 = sup_{||a||=1} |sum_z w_z f(z) p_a(z)| <= ||f||_inf sum |w_z||p_a(z)|.
The **upper** bound in (1) needs only this triangle-inequality direction.
Equality, which uses distinct nodes and continuous tents, is not needed
for either bound. The bound for p in Pi_(m-1) restricts to Pi_n, n<m
(line 239). PASS.

### S1. Density identity (2) — PASS
I derived the cardinal normalization independently. The discrete
checkerboard form with weights rho is diagonal on T_aT_b, a+b<=m. It
deviates from the continuous nu-tensor-nu form only at the mode (m,0):
the discrete squared norm of T_m(x) is 1, the continuous one is 1/2. So
L_B = rho_B[K_m - T_m(z1)T_m(B1)], with coefficient exactly 1 (not 2).
Integrating over dxdy gives the exceptional term -2 h_m T_m(B1), where
the factor 2 is the y-integral of 1. This gives (2). Also
c_{2r}h_{2r} = -4/(4r^2-1) = t_r, and the odd moments vanish. So the main
sum is the triangle r+s<=R=floor(m/2) of the absolutely convergent series
pi sin(theta) = 2 - 4 sum cos(2r theta)/(4r^2-1). Endpoints are covered
by uniform convergence (Weierstrass M-test). Sum |t_r| = 4. Numerically
confirmed (below) by two independent moment solves (Legendre and
Chebyshev bases). PASS.

### S2. Triangular sum (4), lower bound (5), absolute tail (6) — PASS
- (4) is PD-T111's identity; I re-proved it in exact rationals for R=1..400.
- S_R <= 1+(R-1)/3 = (R+2)/3 <= R(R+2)/(2R+1) iff R>=1. This gives
  A_R >= -4/N; equality holds at R=1 (A_1 = -4/3, N=3). The stated
  equivalence with S_R <= R(R+2)/N is exact.
- Sign bookkeeping: t_0>0 and t_r<0 for r>=1, so t_r t_s<0 exactly on the
  two coordinate axes minus the origin. The change is
  2*2*2*sum_{1..R}|t_r| = 8(2-2/N) = 16-16/N. The tail is
  16 - (A_R+16-16/N) = 16/N - A_R <= 20/N. N = m+1 (m even) or m (m odd),
  so 20/N <= 20/m. Verified exactly for R=1..400.
PASS.

### S3. Exceptional term and (7) — PASS
For odd m, h_m=0. For even m, 2|h_m| = 4/(m^2-1) <= 8/(3m) iff
(2m+1)(m-2)>=0, with equality at m=2. Since |T_a|<=1 on the whole square,
||d_m - g x g||_inf <= 20/m + 8/(3m) = 68/(3m), uniformly on
[-1,1]^2, not only at nodes. Exact-rational check of
tail + exceptional <= 68/(3m) for m=2..801. Float check on dense angle
grids: the actual sup of m|d_m - g x g| is at most 12.0 (m=3) and about
6.3 for large m, against 68/3 = 22.67. PASS.

### S4. Raw Chebyshev sampling estimate (8)-(9) — PASS
- Legendre: ||q||_inf^2 <= (sum_{l<m}(2l+1)/2)||q||^2 = (m^2/2)||q||^2 for
  deg q <= m-1. |P_l|<=1 via the Laplace integral is fine; it is
  classical anyway.
- Middle interval: sin t >= sin(1/m) >= 2/(pi m), since 1/m <= pi/2. This
  gives (1/pi)·(pi m/2)∫q^2 dx = (m/2)||q||^2. The end intervals have
  total length 2/m and give (1/pi)(2/m)(m^2/2) = m/pi. So kappa = 1/2+1/pi.
- 2D: Fubini in each coordinate (each coordinate degree <= m-1) gives
  kappa^2 m^2.
- Discrete exactness on Pi_(m-1): 2·1_{j+k even} = 1+(-1)^{j+k}. The full
  tensor trapezoid sums are exact for frequencies <2m and <2m+2. The
  alternating sum is nonzero only if the x-frequency ≡ m (mod 2m) and the
  y-frequency ≡ m+1 (mod 2m+2), which forces total degree >= 2m+1 > 2m-2.
  So sum rho p^2 = ∫p^2 d(nu x nu). sum rho = 1, and Cauchy–Schwarz gives
  (9).
PASS. (Wording note E3 below.)

### S5. CC sine floor (10) — PASS
PD-T017: interior W_{N,j} = (2/N)S_N(theta_j). The error is at most 1/N
(N odd) or N/(N^2-1) (N even). With sin theta_j >= sin(pi/N) >= 2/N, the
error is at most (2/3) sin theta_j for every N>=2 (N even needs N^2>=4).
So W >= (2/N)(pi/2-2/3) sin = (pi-4/3) sin/N. It applies to N=m and
N=m+1, both >=2. Numerically, over N=2..1200, the minimum of
W N/(a sin theta) is 1.4747 (at N=2, j=1), so the inequality holds with
room. PASS.

### S6. Main-density comparison (11) — PASS
At interior nodes, v = 2 pi^2 sin sin/(m(m+1)) <= (2 pi^2/a^2) W_{m,j}W_{m+1,k}.
At any node with j∈{0,m} or k∈{0,m+1}, v=0. CC weights are positive
(PD-T013; also PD-T017 (2)), which allows enlarging to the full grid and
multiplying the 1D inequality by W_{m+1,k}>=0. PD-T022 at n=N-1 gives
C_N(q^2) <= (1+(1-2/N)^2)∫q^2 < 2∫q^2, applied with N=m in x and N=m+1
in y. Total: 8 pi^2/a^2 ||p||^2. Pointwise domination was checked at
every node for the tested m. PASS.

### S7. Checkerboard mass (12) — PASS
The sum over the checkerboard is (pi^2/(m(m+1))) [prod of plain sine sums
+ prod of alternating sine sums]. For the odd one of m, m+1, the map
j->N-j is a fixed-point-free involution that flips the sign, so its
alternating sum is 0. sum_{j=1}^{N-1} sin(j pi/N) = cot(pi/(2N)), and
cot t <= 1/t gives <=4. The formula matched float sums to 1e-12.
(13): sqrt(4)·sqrt(8)pi/a = 4 sqrt(2) pi/a. PASS.

### S8. Assembly and constant — PASS
|w_z| = rho_z|d_m| <= rho_z(g x g + 68/(3m)) = v_z + (68/(3m))rho_z. This
uses only rho>=0 and g>=0; there is no sign assumption on w. Then
sum|w||p| <= (4 sqrt2 pi/a + (68/(3m))·kappa m)||p|| = C*||p||. The m
cancels exactly, so the bound is uniform in m. Value 28.376334831123
(first term 9.8279774110, second term 18.5483574202). Rational:
pi>3 gives pi/(pi-4/3) < 9/5, and kappa < 5/6, sqrt2 < 3/2, so
C* < 54/5 + 170/9 = 1336/45 = 29.689 < 30. PASS.

### S9. Lower bound 2 — PASS
Every phi_alpha has degree <= n <= m-1 <= m, so Q_m(phi_alpha) = ∫phi_alpha
and H1 = 1. Therefore ||H|| >= ||1||_{L2(dxdy)}/||1||_inf = 2 for every
0<=n<m, including n=0 (where ||H_{m,0}|| = tau_m/2 >= 2 exactly).
Enumeration shows the norm equals 2 exactly at m=2 (both n), so the
lower bound is attained. PASS.

### S10. Edge cases and quantifiers — PASS
- m=2: R=1, N=3. A_1 = -4/3 makes (5) an equality, and the exceptional
  bound is also an equality. Tail+exceptional = 8 <= 34/3. The CC axes
  are N=2 and N=3, and PD-T022 is exact at N=2. Corner weights are 0.
- m=3 (odd): h_m=0, N=m, tail = 20/3 <= 20/3. This is the tightest case
  of 20/N <= 20/m.
- Odd vs even m: N = m or m+1; the exceptional mode appears only for even
  m; one of m, m+1 is odd for the mass reflection. All are handled.
- Endpoint half weights: epsilon, eta enter rho. v=0 at boundary nodes, so
  half weights only matter in (9), where exactness handles them. (10) is
  used only at interior nodes.
- Node corners ((1,1) always; (-1,1) for even m; (1,-1) for odd m) are
  covered by the uniform sup bound: |w_c| <= 68/(3m)·rho_c, versus the
  actual |w_c| ~ 4 log m/m^4. Non-node corners are irrelevant.
- n=0 and all n<m: by restriction. m>=2 is needed only for R>=1 and
  N>=2. No claim is made for n=m or m=1.

## Findings

No blocking or major findings.

- **E1 (editorial / minor), lines 17, 62–71, 203.** The operator H_(m,n)
  is defined in PD-T113, not in definitions.md (which does not define
  H) or PD-T112 (which defines the generic H). Positivity of CC weights
  ("Both CC rules are positive", line 203) is used twice, for enlarging
  the sum and for multiplying the 1D bound by W_{m+1,k}. It has no
  citation: PD-T013 (or PD-T017 eq. (2)) supplies it. Correction: add
  PD-T113 (definition) and PD-T013 (CC positivity) to "Depends on".
  Mathematical effect: none.
- **E2 (editorial), notation collisions.**
  - N = 2R+1 (sec. 1) versus N as the CC axis parameter (sec. 3, (10)).
  - a as a Chebyshev index (eq. (2), c_a, h_a) versus a = pi-4/3.
  - S_R (odd harmonic sum) versus S_N(theta) (PD-T017 partial sum).
  - theta_j = j pi/m (line 32) versus theta_j = j pi/N in (10) (for the
    y axis this is phi_k).

  Rename them, e.g. M=2R+1, alpha_0 = pi-4/3, and sigma_R.
- **E3 (editorial), lines 176–179.** "simultaneous degree sums m and m+1"
  is loose. Precisely: the alternating sum of T_alpha(x)T_beta(y) is
  nonzero only when alpha ≡ m (mod 2m) and beta ≡ m+1 (mod 2m+2), so
  alpha+beta >= 2m+1 > 2m-2. The conclusion is correct.
- **E4 (editorial), line 98.** "including both endpoints by absolute
  convergence": PD-T017 states the series for 0<theta<pi. Extending to
  the endpoints needs continuity of both sides plus uniform convergence
  (M-test); this is implicit and true.
- **E5 (editorial / procedural), lines 50–51, 57, 252, 263.** These still
  say the independent check is pending, but `independent-checks-math.md`
  reviewed exactly this SHA-256. The orchestrator should update the
  status wording when integrating. Do not treat that check, or this one,
  as the required audit unless the workflow designates it.
- **Observation (not a defect).** Every inequality in the chain is
  coarse. The measured true norms are about 2.0–2.44, and the actual
  constants are below their bounds: m·sup|d-gxg| ≈ 6.3 vs 22.7;
  sqrt(lambda_raw)/m ≈ 0.18 vs 0.82; lambda_main ≈ 1.82 vs 24.1. The
  claimed "useful explicit value" (PD-T114) is therefore about 10x
  pessimistic, as the record itself states ("deliberately coarse"). The
  result is compatible with PD-N052, whose divergent majorant uses
  sum|w|p^2 rather than sum|w||p|, and with the F1/F2 signed-Gram
  divergence.

## Executed checks (MEASURED floats; exact rationals where stated)

My own code, all in the scratchpad directory, using Python 3.13.18 and
NumPy 2.5.3 (SciPy not available):

1. `python3 f4_exact.py`: exact Fraction checks for R=1..400 (m=2..801):
   - identity (4), telescoping, 1D tail 2/N, the axis change 16-16/N, the
     tail identity 16/N - A_R, A_R >= -4/N, and the S_R bound chain;
   - tail+exceptional <= 68/(3m) for both parities;
   - all true. max(-A_R N/4) = 1 (equality at R=1). 1336/45 = 29.6889.
     C* = 28.376334831123.
2. `python3 f4_numeric.py` (241 s), all assertions pass:
   - Weights by two independent moment solves, Legendre basis (rhs 4δ)
     and Chebyshev basis (rhs h_a h_b), for m=2..30, 35, 40, 45. Both
     match rho·d_m to <= 5.4e-15. sum w = 4. min w < 0 for m>=3 (e.g.
     m=3: -5.56e-2). This confirms (2), including the exceptional term
     with coefficient -2h_m.
   - m·sup|d_m - g x g| on dense angle grids (plus nodes), for m=2..40 and
     50, 63, 64, 99, 100, 127, 128, 200, 255, 256, 400, 401: worst 12.0
     (m=3), large-m value about 6.30, all <= 22.67.
   - 1D lambda_max(∫q^2 dnu/∫q^2 dx), deg<=m-1, for m up to 512: about
     0.336 m, versus kappa m = 0.818 m. The Legendre sup bound m^2/2 is
     attained at x=1.
   - 2D: checkerboard exactness on Pi_(m-1) (error <= 3e-15), discrete
     Gram equal to the continuous nu x nu Gram (<= 4e-14), and
     sqrt(lambda_raw) <= kappa m, for m=2..10, 15, 16, 25, 32, 40, 50, 64.
   - CC: exactness to degree N and positivity checked. The floor (10) has
     minimum ratio 1.4747 over N=2..1200.
   - PD-T022: lambda_+ <= 1+(1-2/N)^2 for 15 values of N up to 200
     (actual about 1.0045).
   - Main density: pointwise v <= 2pi^2/a^2·W W, mass equal to the cot
     formula and <= 4, lambda_main <= 24.15 (actual <= 1.82), tensor-CC
     lambda <= 4, for m = 2..8, 10, 16, 25, 32, 40, 50, 64.
3. `python3 f4_norm.py`: operator norms.
   - Exact sign-vertex enumeration (the maximum of a convex function on
     the cube is at a vertex) for m=2..6, all n<m:
     m=2: 2.0000000000, 2.0000000000 (n=0,1)
     m=3: 2.1111111111, 2.1198648920, 2.4355900241
     m=4: 2.0177777778, 2.0180127127, 2.0224157069, 2.3392876409
     m=5: 2.0207407407, 2.0210600378, 2.0221239971, 2.0507357856, 2.3659446501
     m=6: 2.0060468632, 2.0060742038, 2.0061653363, 2.0063658133,
          2.0601532516, 2.3358237445 (2^27 vertices per n, about 9 min)
     All lie in [2, C*]. The n=m-1 maximum over tested m is 2.4356 at m=3.
   - The n=0 value equals tau_m/2 exactly.
   - For m = 7..60, sign-ascent lower bounds (35 starts each) and the
     per-m proof bound sqrt(sum v·lambda_main) + max_z|d-gxg|·sqrt(lambda_raw):
     m in {7,8,9,10,11,12,15,16,20,21,25,30,31,40,41,50,60}:
     - lower bounds 2.250–2.324 (e.g. m=60: 2.3240), not certified
       maxima;
     - per-m proof bound 3.80–4.15 (m=7: 4.1454; m=60: 3.8377);
     - sqrt(tau beta_abs) 2.56–2.94, slowly growing as PD-N052 predicts;
     - tau_m -> 4.
     Here sqrt(tau beta_abs) is a valid upper bound for each fixed m but
     diverges like sqrt(log m). Weights for m <= 45 come from the moment
     solve, and from rho·d_m (validated) at m=50 and 60. Total runtime
     565 s, all assertions passed (exit 0).
   - Pointwise |w_z| <= v_z + (68/(3m))rho_z holds at every node.

The numbers agree with the Codex checker's reported m=2,3,4 values
(2.0000000000, 2.4355900241, 2.3392876409).

## Residual uncertainty

- The proof is analytic and closes as written. My numerics are finite
  float regressions and are not premises of the theorem. The exact
  rational checks cover only finitely many R; the general-R argument is
  the analytic one, which I re-derived by hand.
- Dependencies were checked at the level needed:
  - PD-T101 normalization: re-derived independently.
  - PD-T017 error display: re-derived.
  - PD-T022: proof read; inequality spot-checked numerically, not
    re-proved line by line, but its PROOF_STATUS row records Claude
    audit-02 acceptance.
  - PD-T112: only the trivial direction is used.
- Literature, novelty, and process compliance (gate, G5 disposition) were
  outside this mathematical audit.
