# Supplementary independent mathematical audit: F3 positive-reference diamond theorem, threshold classification, warmups

Auditor: Claude Opus 5.5 (subagent, supplementary check; not the required primary Claude audit record).
Rules read at branch head `ed9aaa9fc2546a54d7822b31f39dac7e141a9238` (AGENTS.md, CLAUDE_ROLES.md, relevant WORKFLOW.md §91 on REJECTED display).
Role: independent auditor. No git state change, no repository file edited.
Novelty scope: the full `state/IDEAS.md` gate was NOT re-read. This check covers mathematics, quantifiers, statuses and display only. The primary audit must still run the novelty gate.

## Files and hashes audited (current working tree = HEAD ed9aaa9)

| File | SHA-256 |
|---|---|
| theory/f3-smooth-diamond-reference.md | dfbc44a3ec0589f794457fe14c3212b730d62a26c66bffa3e1d4a7295e62550d |
| theory/f3-fixed-ratio-threshold.md | 3dbde58f88a2c96c7239b701a03d812006ad2aac06f79b6bb539255bc0e6dbc4 |
| theory/f3-signed-target-open.md | 6635eb81c45e44b975fa4cb6d4edfd8e875a9f064a1144687f2b01e9c0c448d6 |
| theory/f12-1d-sign-discard-obstruction.md | c62228ba0957c0d3398e2c3706109150e71abf95b1132abe333755d79aab45f9 |
| theory/f12-harmonic-boundary-escape.md | 84b2ff2e24258608bab7d0f636fdcbe6196ab56ecbcc35ca23f860ed2a174395 |
| theory/f12-eventual-negative-carrier.md | 0ef7c078dc8a71bac882e6d61669211b89e1295b33be7f51f0488073b5bae09d |
| theory/f12-eventual-upper-carrier.md | b57334029a4676c5ddea0827e9c34e5c07cc931fdc2dbe8457340380439cd3fb |
| theory/f12-local-weight-asymptotic.md | ec60d98c4bbaefe5daf3281efb5a32fe742687ee4ac8fc7a789f2d0a66867b8d |
| code/independent_f3_check.py | f46d0297cc00d3848a5df0378115fcb12989257b12256a00dd35308a474361a4 |
| proposed-record-changes.md | cb5fd3ff0884b305a0cd126953134da65f8d55143816873ec5c8beb92ccd9b71 |

I also read: definitions.md, PD-T115 (mz2d-fixed-ratio-diamond-reconstruction.md), PD-T116 (mz2d-fixed-ratio.md), PD-T028 (open-padua-target.md), PD-T110 (mz2d-upper-open.md), ideas-f3.md, attempts/F3.md, the F3 and addendum sections of independent-checks-math.md, handoffs/02-audit.md, and the PROOF_STATUS.md header conventions (line 11).

## Executed checks (all actually run here)

Scripts are in `/tmp/claude-0/-home-user-padua-research/db3e20db-75fd-57b6-8cbd-fa0690855b88/scratchpad/`.

1. `python3 check_diamond.py` (8.4 s), float64, independent of the repo checker:
   - Plateau/cutoff of K from an FFT of the closed form, all m=1..60 and n<m: max error 5.7e-14.
   - Decay (4): max over t of |K|(1+md)^4/(m eps^-4) is 0.056*A (worst case m=4,n=0).
   - Envelope (7): 160k random (t,z) pairs per (m,n) for m in {1,2,3,5,8,13,21,40} and n in {0, m/2, m-1}, biased toward sin=0. Max of |H|sqrt(nu(t)/nu(z))/(m^2 eps^-8 E) is 1.4e-6*A^2.
   - Lift sum (9): over 400 centres per m (m=1..30, 50, 80), including lift points and mid-squares. Max sum J*J is 0.0999*4B^2. The discrete (10) N_m*int E dmu_Gamma reaches the same ratio 0.0999 of 2B^2.
   - 1-D regularisation (§6), via a generalised eigenproblem for r=0..59: max of int f(cos t)^2 dt/((r+1) int sin t f^2) is 0.611*(1+pi/2).
   - Reconstruction (5): random diamond-supported q, m in {1,2,3,4,7,10,15}, all n. Max error 3.0e-13.
   - Actual Gram of S_m in the Legendre basis, m up to 24: all eigenvalues lie in [0.41, 3.70], far inside the bound [C(eps)^-1, C_2^2 C(eps)].
2. `python3 topics/.../code/independent_f3_check.py <scratch>/rerun-f3-check.json` (1.8 s): PASS, with 300 pairs / 379900 / 92064 / 205311 tests, matching the receipt counts. The receipt now records the current theory hash dfbc44a3....
3. `python3 check_threshold.py` (43 s):
   - (A) Direct interpolatory weights from the moment solve, compared with formula (3) of PD-T?…-12 for even m=2..30: relative error 4.4e-14. The exceptional coefficient `2h_m` is correct; the alternative `4h_m` is off by 4e-3. At m=10, sum(w)=4. The m=3 weights include -1/18, which is consistent with PD-N045.
   - (B) eta(m, floor(m/2)) is at most 5e-13 for every m=1..20 (both parities). eta(m, floor(m/2)+1) is nonzero, e.g. 0.53 at m=3 and 0.007 at m=20.
   - (C) Majorant (2) of -12: max |w|/majorant is 180 (<=4096) over the whole grid for m=4..512. Single-node formula weights for m=2^10..2^22: two-point fits in 1/log m extrapolate to -4.0, 16.0, -8.0, -16.0, 16.0, -8.0 at (j,k)=(0,0),(1,1),(2,0),(2,2),(3,1),(4,0), matching -16 e_j e_k (-1)^j. Raw values are still far off at m=2^22, e.g. +37.7 at (2,2) against a limit of -16, because of the O(1/log m) term pi^4 jk/log m.
   - (D) Carrier energies use an O(m log m) FFT evaluation of the exact formula (validated against the full weight matrix at m=64, error 2e-15), for theta=0.75 and 0.95, m up to 2^20. Continuous norms are 3.84 (negative carrier) and 2.18 (positive carrier), both <= C_0^2.
   - (E) The infinite profile sums equal a/3, 2a/3, 0 and a/6 to 1e-15 (a=0.05, 0.1, 0.2).
   - (F) Degree admissibility, i.e. m/2+2r, m/2+3r <= floor(theta m) with 2r<m and 4r<m: 0 violations over 400 thetas in (0.5001, 0.9999) and all even m <= 4000.
4. `python3 fit_carriers.py` (2 min 16 s): Q_m(p^2) at m=2^12..2^23, with a linear fit in log m over the last 5 points:

| theta | sign | fitted slope | predicted (-d^2/9, +d^2/18) | intercept | log m where Q=0 (negative carrier) |
|---|---|---|---|---|---|
| 0.60 | - | -0.00111 | -0.00111 | 3.847 | about 3464 |
| 0.60 | + | 0.00053 | 0.00056 | 2.174 | - |
| 0.75 | - | -0.00694 | -0.00694 | 3.857 | about 555 |
| 0.75 | + | 0.00346 | 0.00347 | 2.166 | - |
| 0.95 | - | -0.02250 | -0.02250 | 3.870 | about 172 |
| 0.95 | + | 0.01124 | 0.01125 | 2.148 | - |

   These are MEASURED extrapolations, not proofs. They confirm the signs and the values of constants (2) and (U).
5. `python3 check_warmups.py`: 1-D sign-discard N=3..501. Formula (4) for ||q_L||^2 holds to 1e-11, ||p_L||^2 >= L/16 holds, the ratio is far below bound (2) and tends to 0 (0.0104 at N=501), and the actual signed ratio is about 1. Harmonic escape N=3..401: max |p_N(cos t)|/(pi N) <= 0.19 (claim <=1). The endpoint mass at K=1,5 is <= 0.02 pi^2 K^2 (claim <= pi^2 K^2). C_N(p^2)/||p||^2 decreases slowly, consistent with the inherited PD-T018 bounds.

## A. Primary target: f3-smooth-diamond-reference.md, step by step

| Step | Verdict | Notes |
|---|---|---|
| Setup and normalisation: N_m=2m(m+1); S_m = pi^2 D | PASS | m=1 check: S_1(c^2)/(4c^2) = 3.701 (6 pi^2/16), as computed |
| (3) L=ceil(g/4): 4(L-1) <= g-1, L >= eps m/4 | PASS | |
| Fejér coefficients 1-\|r\|/L; F_L^2 nonnegative, degree b=2L-2, mass L^2; plateau \|k\|<=M-b=n, cutoff M+b=n+4L-4<=m-1; L=1 gives K=D_n | PASS | rechecked exactly by the repo checker (m<=24) and in float by me (m<=60) |
| (4) \|D_M\| <= 2M+1 = 2n+4L-3 <= n+m <= 2m-1; F_L/L <= min(1, pi^2/(Ld)^2); min(1,pi^4/x^4) <= (1+pi)^4/(1+x)^4; 1+Ld >= (eps/4)(1+md); A=2*4^4*(1+pi)^4=512(1+pi)^4 | PASS | measured slack is a factor of about 18 |
| §2 parity projection: Hhat(a,b)=Khat(a+b)Khat(a-b); periodicity; plateau on \|a\|+\|b\|<=n; support <=m-1 via max(\|a+b\|,\|a-b\|)=\|a\|+\|b\| | PASS | |
| Character average = indicator of Lambda_m; nonzero alias l1 >= 2m (2m+1 on the shifted coset); couplings need \|a-c\|_1 <= n+m-1 <= 2m-2 | PASS | |
| (5) both reconstruction identities, reflection preserving checkerboard parity (2m-j, 2m+2-k) | PASS | numerical error 3e-13 |
| (6) \|sin\|+1/m is 1-Lipschitz in circle distance and >= 1/m; each factor ratio <= 1+m(d_u+d_v); sqrt of the product <= 1+m(d_u+d_v) <= (1+md_u)(1+md_v); applied branchwise with branch-specific representatives (u+pi, v+pi for branch 2); symmetric under interchange | PASS | |
| (7) envelope A^2 eps^-8 m^2 E | PASS | measured slack is huge |
| (8) phi(u,v)=(u+v,u-v) has kernel {0,(pi,pi)} and pushes Haar to Haar; int E dmu = (int J dmu_1)^2 <= 1/(4 pi^2 m^2) | PASS | |
| Lifts: exactly 2N_m; at most one per half-open square of side a=pi/(2(m+1)), since original differences are < 2a = pi/(m+1) < pi/m and lifts of one node differ by (pi,pi) | PASS | repo checker covers m<=8 pairwise; my lift sums cover m<=80 |
| (9) shell count 4(sum(1+k pi/4)^-3)^2 <= 4B^2 with ma >= pi/4; series <= 1+2/pi | PASS (editorial E2) | |
| (10)/(11): (1/N_m)*(1/2)*4B^2 = 2B^2/N_m; times A^2 eps^-8 m^2 gives A^2B^2 eps^-8 * m/(m+1) <= M_eps; continuous side A^2 eps^-8/(4pi^2) <= M_eps | PASS | |
| (12) Schur in both orientations (row discrete/column continuous and the reverse), positive measures only | PASS | |
| (13) Legendre evaluation bound (r+1)^2/2; endpoint intervals contribute (r+1) int f^2; middle sin t >= 2 delta/pi; factor (1+pi/2)(r+1); r+1 <= m gives C_2=2+pi/2; tensorised by slices of degree <= n; pi^2 V = regularised angular integral over [0,pi]^2 | PASS (minor M1) | measured 1-D constant is 0.61 of the bound |
| Assembly: S_m >= \|\|p\|\|^2/M^2 and S_m <= M^2 C_2^2 \|\|p\|\|^2, C(eps)=M_eps^2=A^4B^4 eps^-16; monotone in eps, so C(1-theta) works for n <= theta m | PASS | |
| Quantifiers | PASS | every m>=1 (both parities, no parity used), every 0<=n<m, every fixed 0<=theta<1 with n<=theta m. The constant diverges as theta->1 and no endpoint claim is made |
| Positive reference versus signed transfer | PASS | S_m has weights pi^2 nu/N_m > 0 and is explicitly not Q_m (Statement, Scope, "No inequality for Q_m follows"). No signed weight enters Cauchy–Schwarz. I found no sentence that transfers the result to Q_m |

Findings for the diamond file:
- **M1 (minor), §6 lines 333-339.** |P_k|<=1 is "justified" by the Laplace integral, whose identification with P_k is only sketched ("follows by the binomial expansion (or its generating series)"). The fact is classical and true. Either complete the derivation in two lines (sum h^k times the integrand, then use int_0^pi dphi/(alpha - beta cos phi) = pi/sqrt(alpha^2-beta^2) to get (1-2hx+h^2)^{-1/2}), or label it as a standard fact. This is not a correctness gap.
- **M2 (minor, provenance), Checks lines 117-131.** The receipt pins input hash a55b401d…, which is not any committed version of the file. Git has only dbd61460… (cab4c41) and dfbc44a3… (dee6384). So "proof and constants unchanged" cannot be replayed from Git. The diff between the two committed versions is metadata-only. My rerun of the checker at the current hash passes, and my reconstruction applies to the current text.
- **E1 (editorial), lines 93-96.** "Subsequent separate carrier countersequences refute its positive assertion": "its" grammatically points at "This theorem". Replace it with "PD-T116's positive assertion". Also, "no uniform positive signed extension" (line 382) is vague. Suggest "no uniform signed eta(theta)<1 for any theta>1/2".
- **E2 (editorial), lines 274-277.** The shells as written ("two oriented directions", half-open) cover the centre twice and leave out the antipode, which is then "assigned to a single interval". That makes the assigned interval closed. It is harmless, but the clean form is: shell k = {d in [ka,(k+1)a)}, each a union of two subsets of half-open length-a intervals, with the antipode in its own degenerate shell k=2(m+1), which the infinite series already includes.
- **E3 (editorial), lines 243-245.** After the weight loss, any exponent >1 per diagonal variable would be summable. The real point is that pre-ratio decay >2 (here 4) survives a one-power loss per variable; the inverse-square Fejér envelope loses a logarithm.
- **E4 (editorial), line 112.** "No mathematical program … was executed for this analytic result" sits right before a paragraph reporting an executed checker. Say "by this developer".

Verdict on the diamond theorem: **PROVED as stated** (positive reference only). I found no blocking or major issue.

## B. f3-fixed-ratio-threshold.md

(i) theta <= 1/2: n <= theta m <= m/2 gives 2n <= m, for odd m too (2n <= m-1). Every Gram entry Q_m(phi_ab phi_cd) has degree <= 2n <= m, so G=I exactly and eta=0. **PASS**, measured ~1e-13 for m<=20 in both parities.

(ii) theta > 1/2, a = delta/4 < 1/8:
- Negative carrier: degree m/2+2r <= (1/2+delta/2)m < theta m, hence <= floor(theta m). We have 2r < m and 2s < m+1.
- Positive carrier: degree m/2+3r <= (1/2+3delta/4)m < theta m. Here 2a+b = 3delta/4 < 3/8, 4r < m, and r >= 1 eventually for nonvanishing.
- **PASS**, with 0 numerical violations.
- Norm: ||p||^2 <= C_0^2 holds because the carriers satisfy |carrier| <= 1 and int F^2 dx <= (1+pi^4)/2. PASS.
- (7): -8(B_x A_y + A_x B_y) with A_x=B_x=a/3, A_y=2a/3, B_y=0 gives -16a^2/9 = -delta^2/9. Upper: 16(a/6)(a/3) = 8a^2/9 = delta^2/18. PASS, analytically, and the measured slopes agree to 3-4 digits.
- Domination by (1+j)^-3(1+k)^-3 + (1+j)^-4(1+k)^-4 on the whole grid, with zero extension and moving endpoints: PASS.
- Rayleigh directions (negative numerator over the norm upper bound, and the reverse): PASS.

Dependency PD-T?…-12, reconstructed:
- Formula (3), including 2h_m: numerically exact.
- Rectangle-minus-triangle (4).
- Tail (6).
- Triangle bound (7): split pieces give 64H/(9R^2) twice plus 256/(9R^2), and |t_a| <= 4/(3a^2).
- Constant in (8): 4+256 = 260, plus 16/3 from m=2.
- Thin strips (9) with R->inf before delta->0.

All PASS. Carriers -13 and -14: DCT constants D_r, top coefficient 2/(r+1)^2, c_0(h_r) = D_r/2 - 1/(2(r+1)^2), and parity selection: PASS.

(iii) Scope:
- PD-T116's universal assertion (all theta<1) is refuted at every theta>1/2 by even m alone. PASS.
- PD-T110's "lambda_+(m,m-1)<2 for all m>=2" is refuted by -14. PASS.
- PD-T028: all four "determine whether" questions are answered negatively along even m (lambda_max<2 for all m, lambda_min>0 for all m, lambda_min ≍ (1+log m)^-2, eta->1). PASS.
- Remaining OPEN: the odd-m behaviour (whether lambda_min(m, floor(theta m)) is bounded below, or lambda_max above, along odd m); an effective onset or explicit finite violation; sharp growth constants of the true extrema; and the 1-D PD-T027.

Findings for the threshold file:
- **T1 (minor), Scope / Open items / Negative-result scope.** The odd-m classification is never listed as OPEN in this file. It is only implicit in "along even m" and "Only an even-m countersequence is needed". The carrier files and proposed-record-changes.md do list it. Because the title says "exact threshold", add an explicit OPEN odd-m item here.
- **T2 (minor, informational), Scope.** The measured onset of the explicit carriers is astronomically late. The negative carrier first has Q<0 at log m ≈ 172 (theta=0.95), 555 (0.75) and 3464 (0.6), i.e. m ≳ 10^75. For the positive carrier, the Rayleigh quotient reaches 2 only at log m ≈ 630 (theta=0.75). The file correctly says "noneffective". Recommend recording that these explicit carriers cannot serve as finite witnesses at any accessible m. Also note that the uncertified m1600 float minimum (n=m-1) is unrelated to them.
- **T3 (editorial), lines 72-74.** "The entire positive strong-MZ assertion of PD-T116 is REJECTED" can be misread as also rejecting the true theta<=1/2 restriction. Say "the universal (all theta<1) assertion". Also, the PD-N statement embeds a positive routine part (theta<=1/2). That is acceptable as labelled, but should stay outside the negative statement proper.

## C. f3-signed-target-open.md and display coherence (proposed-record-changes.md)

- I verified by diff that the historical block is a byte-identical copy of the first committed body (cab4c41), except that the original H1 title ("…signed Padua fixed-ratio target remains OPEN") was replaced. **E5 (editorial):** keep the original title in the historical block.
- The display "Status = OPEN (historical) + Disposition = REJECTED: refuted (see PD-N…)" matches WORKFLOW.md §91 and the PROOF_STATUS.md line-11 convention ("a rejected claim is not a usable dependency even if its earlier epistemic status remains"). The old label does not make the refuted claim usable: the disposition column carries the PD-N links. **Coherent.**
- **M3 (minor):**
  - The proposed PD-T110 row keeps the statement title "endpoint Padua upper spectrum remains open", and the PD-T110 theory file's H1 says the same. After refutation that title is false, not merely historical.
  - The PD-T116 and PD-T028 rows show "OPEN" right next to "Counterexample alternative resolved" or "…are false".
  - Recommendation: mark the status cell "OPEN (historical; see disposition)" or similar, and retitle or annotate the PD-T110 title. This is not a mathematical issue.
- The proposed addenda correctly list odd m, onset, sharp constants and PD-T027 as open. PASS.

## D. Warmups

- **f12-1d-sign-discard-obstruction.md: PASS.**
  - Checked: q_L = (1+U_{N-1})/2; U_{N-1}^2 = sum U_{2k}; int U_{2k} = 2/(2k+1); int U_{N-1} = 2/N (N odd); formula (4); the harmonic bound; (5); the substitution t=pi/2+u giving p_L = sum cos(2ju); (6) >= L/16; and the ratio bound 32(2+log 2N)/L.
  - Strict positivity uses only PD-T014. The statement is correctly scoped to the intermediary (1), and PD-T027 is explicitly kept OPEN.
  - **E6 (editorial):** the disposition "REJECTED: failed" fits the mechanism IDEA, while the claim (1) itself is refuted. Consider stating both.
- **f12-harmonic-boundary-escape.md: PASS.**
  - Checked: |F_j| <= 4jt; |p_N| <= 4Mt/sin t <= pi N on (0, pi/2], with symmetry from parity N-1; the endpoint mass <= pi^2 K^2 (with K/N <= pi/2); the use of the inherited PD-T018 bounds (log N >= 128); the lift norm identity; the y-edge factor 1-cos(K/m) <= K^2/(2m^2); and Q_m(P^2) = C_m(p^2) via the uniquely determined x-marginal 2C_m.
  - It makes no claim about actual eigenvectors or PD-T027.
- **M2b (minor, provenance):** independent-checks-math.md records the warmup hashes 79763179… and 665c853d…, but the current files are c62228ba… and 84b2ff2e…. `git diff 0a2ba7c dee6384` shows status/Open-items metadata changes only. Unlike the diamond file, the checks record does not note this post-review update.

## E. Severity summary

- Blocking: none.
- Major: none.
- Minor: M1 (Legendre bound sketch), M2/M2b (hash provenance), M3 (registry "remains open" title/status display), T1 (odd-m OPEN item missing in the threshold file), T2 (record that the explicit carriers have an astronomically late measured onset).
- Editorial: E1-E6, T3.

## F. Residual uncertainty

- The numerics are float64 regressions and extrapolations (MEASURED), not proofs. The analytic verdicts rest on my line-by-line reconstruction.
- I did not independently re-derive the PD-T101/111 cardinal formula from first principles; I confirmed formula (3) numerically against direct moment solves (m<=30).
- I did not re-read PD-T014/018/021 proofs; they are inherited dependencies of the warmups.
- The novelty gate (full IDEAS.md) and literature attribution were not audited.
- The other agent's review (independent-checks-math.md) agrees with my conclusions. I did not rely on it.
