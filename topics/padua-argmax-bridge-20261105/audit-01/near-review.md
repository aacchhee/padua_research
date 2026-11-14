# Interim Claude audit — C13 near noncorner case (n >= 500000)

Auditor: Claude Opus 5.5, xhigh (independent subagent auditor; adversarial mathematical audit of Codex development).
Repository/branch: `codex/padua-argmax-bridge-20261105`, HEAD `02beaef2b22f8232286713dab0a1b7c95582ce13` (rules AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md read at this SHA). No git state changed; no repository file edited.
Novelty scope: none. These are proof records with no idea, novelty or mechanism claim, so the full `state/IDEAS.md` read is omitted.

Audited files (SHA-256 at HEAD):
- `T/theory/C13-near-representation.md` fa861e59…8e74b
- `T/theory/C13-near-comparison.md` 44f412f3…0096c
(these match the hashes accepted in `independent-checks-C13-onset.md`, which I read only after doing my own reconstruction)

Upstream read in full: N1-06 (round4-mesh), N1-09 (round5-jumps), N1-10 (round5-endpoints), N1-11 (round5-jump-sum), N1-12 (round5-assembly), N1-13 (round6-regular-variation), N1-15 (round6-near-model), N1-16 (round7-coefficients), N1-17 (round7-comparison), C05-finiteh-endpoint-increment, C05-finiteh-model-comparison, C04-near-limit-comparison, C02-near-explicit-onset §1, and C02-defect-dense-band statement plus the n4096 section.
Upstream read in part: N1-14 statement; C04-near-sharp-remainder statement; C01-near-central-upper statement; C03 slope statement; PD-T364 statement lines; degree-floor greps of N1-01/02/04/05.

## Verdict

**No BLOCKING or MAJOR finding.** I checked every degree-dependent step in my scope myself. The near representation (eta0 < 1/1000) and the near comparison (S_n < Lambda_c + 383/12500, lambda_n < Lambda_c - 1/32 at all physical odd noncorner centres) hold at every integer n >= 500000, on the basis of the upstream inequalities as written. Four MINOR record or wording findings and several NOTEs follow. The verdict is interim: I did not re-derive the upstream proofs below their degree-dependent steps (see Remaining uncertainty).

## 1. Degree-dependent upstream steps (task 1)

V = verified by my own derivation; C = verified by executed exact computation (§6); I = inspection only.

| Step (C13 location) | Upstream source and actual requirement | Result |
|---|---|---|
| Endpoint rows exact, z <= pi/8 (rep:63) | N1-09 statement: n >= 8R = 1024 only | V |
| First/last 128 rows have z <= 128pi/m < delta (rep:80) | Left rows r <= 127: z <= (127pi+1/2)/m < 128pi/m. Right rows r' <= 128 (b = -beta, beta >= 0): z <= 128pi/m. Needs m > 128000pi ≈ 402124 | V, C |
| K_s >= R (rep:64) | K_s = floor(X - t_s) >= X - 2, so X >= 129 suffices. X = delta*m/pi > 159.09 at n0 (pi < 22/7). The stated n >= 405429 is sufficient | V, C |
| N1-06 tail identities (rep:65,73-77) | N1-06's **theorem** needs n >= ceil(2piR/delta) = 804248, so it fails on [500000, 804247]. Its identities (5)-(6), however, need only K >= R and x >= R-1/2 >= 3/2. N1-10's e_HG uses only these and |Z_n| <= 5 (n-free). The X >= 2R condition enters only N1-06's log b_K -> log X step, which N1-10/C13 do not use. C13 handles this correctly | V |
| b_s > 317 -> b_s > 158 (rep:100-103) | b_s = K_s+t_s+1/2 >= X-1/2 > 158.59. The function (6+log x/2)/x^2 decreases; log 158 < 6. Bound: 2[5+B0(log b+2)]/(8b^2) <= 9/(4*158^2) using B0 = 4a/pi^2 < 1/2 | V, C |
| J4096 truncation (rep:103-104) | N1-10 (11) is n-free; K_s < J was already true at 10^6 | V |
| Discrete residual (rep:105-112) | Needs only samples z_k <= delta (the envelope is used at samples; cells are forward). delta+h < 126/125000, log(1/x) < 9, (2/pi)(1/2)(7/4+19/18) < 101/108 | V, C (9.502e-7 < 1e-6) |
| e_A, e_log (rep:115-116) | L*u_max/(6m) with u_max < delta+h/2, and q/[4pi m(R-1/2)] <= 1/(1020pi m) < 1/(3060n) | V, C |
| E5, r_n, D_n (rep:93-98) | N1-09 (3) with a <= 1, P <= 1/2, m/n <= tau0, H_n <= 1+L; N1-12's D_n with pi > 3. N1-01/04 have floor n >= 2 | V |
| Jump error (rep:126) | N1-11: tails 0.145/n^3 + 0.239/n^3 < 1/n^3; regular 2/(nm); J = R truncation <= 1/(27R^3)+1/(16nR^2). Only b_K >= n/2, m/n <= 9/8 (not 2, see NOTE 4), pi > 3 | V |
| Outer singular (rep:137) | N1-15 (7) gives (L+2pi)/(m^2 ell^2) <= (L+8)/(n^2 ell0^2), with ell = delta-h/2 > 249/250000 | V, C |
| Outer regular (rep:138) | N1-13 (2) is degree-free: [(6/5)L+23]/(2m) | V |
| Endpoint-I (rep:139) | 14a[log(2/ell)+5/2]/ell^2 + 8q/ell, divided by 8m^2; log(2/ell0) = log 2008.03 < 8; the integral re-derived | V, C |
| Central residue/log (rep:140) | 15/(2pi m) < 5/(2n) and (1/2)/(2pi m) < 1/(12n); N1-14 is n-free | V |
| H8 special rows (rep:151) | 192/(450pi m) < 64/(450n) = 32/(225n); 1/[8(y+15/2)^2] <= 1/450 for y >= 0 | V |
| C05 sinc argument (comp:79-84) | The old 4rh bound gives 512/n = 1.024e-3 > 1/1000 at n0, so it **does** fail and the refinement is needed. Refinement: (|u|+|v|)/2 < [(2r-1)pi+1]/(2n) <= 5617/14/n < 403/n | V, C |
| d_h > (12/5)k (comp:84-86) | (pi-1/2)k - 512/n >= (12/5)k for k >= 1 | V |
| Quotient Hessian of H = N/K (comp:91-93) | I derived the quotient rule: N_ij/K + N K_ij/K^2 + 2|N_i K_j|/K^2 + 2N K_i K_j/K^3 gives exactly the displayed coefficients; value 0.7601 with r^2/n^2 < 1e-7. The other (9) bounds (K_ij, (1/K)_ij, H_i, H-1) also hold at r^2h^2 < 1e-7 | V, C |
| Endpoint Hessian, slope (comp:98-99) | C05 (20): 128+255*172 = 43988 and 515*128^2+1 = 8437761; 43988+8437761/n0 < 45000. Slope 34+22656/n0 < 35. Taylor along the segment gives (13) | V, C |
| Seam E_s < 3/1000 (comp:107-112) | The N1-10 (4)/(6) constants hold for z <= 1.01e-3 (delta+h/2 < 101/100000) and offsets in [1/4, 3/4] | V |
| 15000/n <= 3/100 (comp:115-119) | (L/pi^2)·2·(pi/6)·l^2/2 with l < 516/n gives < 15000L/n^2; equality 3/100 at n0. 1/60 would need n >= 900000. New total [18+3/1000+(109/300)L]/n < 5(L+1)/n for L > 2.8 | V, C |
| Holes 10(L+1)/n (comp:121-123) | M(1+log(2/M)) <= 4h(1+log(m/(2pi))) <= 4h(L+1); [4(L+6)+(2/3)(L+1)]/m | V, C |
| Special rows 50(L+1)/n (comp:123-124) | N1-16 2(L+5)/m per row from N1-04 (n >= 2), plus H8 < 1/n | V for the arithmetic, I for N1-16's 2(L+5) row bound |
| Jumps 10(L+1)/n (comp:124-125) | C02-near-explicit §1 jump paragraph is n-free: A2 error 0.135/n per side, A1 <= 0.48(L+6)/n, W_b <= 8/(pi n) | V |
| E_rest 75 = 5+10+50+10; 2·75 <= 200 (comp:128-133) | Checked against C05-model (18) and its decomposition; nothing omitted | V for the arithmetic, I for decomposition completeness |
| 11270/n (comp:175) | From (15): 45000·r2/n + 40·beta/n with r2 <= rho^2 <= 1/4 and beta <= 1/2, giving 11250+20 (same as C05-model (19)) | V, C |

**No upstream step in scope silently uses n >= 10^6 or L >= 13.8 without a recheck.** The only places such a floor occurs are N1-06's theorem domain, C05's 4rh <= 1/1000 and 15000/n < 1/60, N1-10's b > 317, N1-15's ell > 499/500000, and the rational budgets. All are addressed above.

## 2. Monotonicity (task 2)

Every variable term in (7)-(11), (13)-(15) and (18) is nonincreasing on n >= n0, and L < 14 is used only at n0:
- the (cL+d)/n^j forms;
- c = 0 forms (4/n, 3/n^2, 32/(225n), 8437761/n^2, 15000/n);
- L·(delta+h/2)/(6m), a product of two decreasing factors;
- (2/pi)G(delta+h), since G is increasing near 0 and h decreases;
- bounds that use monotone geometry: b_s >= X-1/2 and ell >= delta-h/2 both increase; m/n <= tau0 decreases.

The lemma at rep:54-57 and comp:63-66 is stated only for c, d > 0, so it does not literally cover the last three kinds (MINOR F3). A(L) increases in L, so A(L) >= A(131/10) on the whole range. The step L >= 3 in (14) uses only a lower bound.

## 3. Exact recomputations (task 3)

- **eta0** (rep:161) equals the sum of (7)-(11) at n = 500000, L = 14, m = n+1, tau0 = 1001/1000, ell0 = 249/250000, exactly: Fraction equality True; value 3.3875e-4 < 1/1000 (margin 6.6e-4). Component sizes: E5 3.85e-5, strip 9.21e-5, outer 2.08e-4, special 2.84e-7, jump 1.77e-8, r_n and D_n below 1e-9.
- **(18)** 2/1000 + 1/10000 + 11270/500000 + 3000/500000 = 383/12500 exactly; 1/32 - 383/12500 = 6.1e-4. Also 383/12500 - 1/16 = -1593/50000 < -1/32.
- **(17)** A(131/10) = 16.8580625. A - 1225/144 - 32/9 = 76729/16000 = 4.7955625 > 19/4 (tight, margin 0.0456). A - 395/48 = 8.63 > 8. The maximum 27c^4/[256(19/4)^3] = 1366875/28768731136 ≈ 4.7513e-5 < 1/20000; I re-derived the formula for max(cx^{3/2} - kx^2). c·e^-12 + (32/9)e^-16 ≈ 3.28e-6 < 1e-5 (rigorous via e > 8/3). The entropy maximum is e^{-(18k+1)}/18 = e^-144/(18e) for k = 8 (re-derived). Total < 5e-5 + 1.5e-9 < 1e-4.
- **Case split** (comp:158-167): alpha >= e^-8 versus 0 < alpha < e^-8, plus alpha = 0 (zero value) and beta handled jointly for all beta in [0, 1/2]. The split is complete. G_n >= A·(alpha^2+beta^2) splits additively.
- **(16)** is identical to C04-near-limit-comparison.md eq. (3): 8+1/16+4/9 = 1225/144 and 8+1/16+1/6 = 395/48. It is phase-only on alpha, beta >= 0 with alpha+beta <= 1/2: it rests on C01-near-central-upper (1) plus C04-near-sharp-remainder (1) with C03 |d| < 1e-9, all limit or phase statements with R, J, delta fixed. It is **not** C04's headline n >= 10^6 statement (1); C13 says so but does not cite the equation number (MINOR F4).
- **log n0**: log10 > 23/10 (C08-far-model-comparison:106-107; my rational partial sums give 2.30163) and log2 < 7/10 give log n0 > 131/10. The upper bound log n0 < 14 does **not** follow from those two bounds; it follows from N1-16's log10 < 2303/1000, or from (27/10)^14 > 10^6 (MINOR F2).

## 4. Comparison logic (task 4)

- **N1-17 identity.** Write M(phase) - M(0) = (B_M - B_c)L^2 + (b_M - b_c)L + F_n, using B_M(0) = B_c and b_M(0) = b_c (N1-16 (12) gives 0 at a = 1, D = 0). This yields M - Lambda_c = [M(0) - Lambda_c] + F_n - G_n, an exact identity with no degree floor. With S(0,0) = Lambda_c (PD-T364 (5)), S - Lambda_c = [S - M(|phase|)] + [M(0) - S(0)] + F_n - G_n, so the representation error is charged exactly twice (phase and origin). Correct.
- **G_n lower bound.** G_n >= r2[47L^2/(48pi^2) + L/(24pi^2)] >= A(L)·r2, from N1-16 (2) (phase-only) and pi^2 < 10.
- **Defect.** C02-defect-dense-band (2), (4): for n >= 4096 and |alpha|+|beta| <= r <= 1/2 (closed), Q_v > 1/16 if 0 < K < m and Q_h > 1/16 if 0 < J < n. This holds for every physical (theta, phi) in [0, pi]^2, both centre parities, edges (J in {0, n} with interior K, or K in {0, m} with interior J), polynomial collisions, and the exceptional first-coordinate mode (C02:99). The (29)-(30) rational bound increases with n. Noncorner ("at least one interior coordinate", comp:17-18) is exactly the hypothesis of (2). PD-T364 gives lambda <= S - Q_v and lambda <= S - Q_h, so lambda < Lambda_c + 383/12500 - 1/16 < Lambda_c - 1/32. Correct.
- **Corners.** Corners (J in {0, n} and K in {0, m}) are excluded from (4). No defect is claimed there. The parity-correct corners lie outside this file's conclusion, as intended.
- **Coverage.** (2) and (4) are universally quantified over all signed phases with rho <= 1/2 and all noncorner centres, so the near case has no centre-class gap. Assigning each physical point to a near or far representation belongs to the global record, outside my scope.

## 5. Geometry (task 5)

- **Special set.** B = {m-1, m} plus at most two collision rows, all within 1/2 of pi (collision angles pi-alpha+beta and pi+alpha+beta), so disjoint from the E_R rows and the strips.
- **Holes.** At most two collision cells and an upper-end omission of exactly 2h (t_L + t_R = 1), all in z > 5/2.
- **Outer cells.** Lower endpoints >= delta - h/2 > ell0.
- **Duplicates and holes.** Duplicates merged; holes not multiplied by any count (BV and variation bounds are over unions).
- **Endpoint rows.** z <= 128pi/m < delta.
- **Closed boundary rho = 1/2.** a >= (1+cos(1/2))/2 = 0.9388 >= 15/16 and P <= 1/2, so 2a > P still holds at the boundary.
- **Origin and axes.** Continuous values, by the model conventions.

Every n-dependent geometric fact above holds for n >= n0 (V, C).

## Findings

**F1 — MINOR (stale status).** The two near files still say the focused F1/F2 check is pending:
- `C13-near-representation.md:25-27`: "Its F1/F2 record repairs are being submitted for a focused check; that check is **pending**."
- `C13-near-comparison.md:33-35`: the same text.

`independent-checks-C13-onset.md:361-367` records that focused review as ACCEPTED for exactly these hashes (fa861e59…, 44f412f3…). Update both files to link the accepted supplementary check. Formal Claude audit stays pending.

**F2 — MINOR (citation/derivation wording).** `rep:49-52` and `comp:58-61`: "log10>23/10 and log2<7/10 … give … log n0<14". The upper bound does not follow from those two inequalities. Cite N1-16's log10 < 2303/1000 (6·2303/1000 < 14), or e > 27/10 with (27/10)^14 > n0. The conclusion is true.

**F3 — MINOR (lemma scope).** The monotonicity lemma (`rep:54-57`, `comp:63-66`) covers only (c log n + d)/n^j with c, d > 0. The proofs also use the forms listed in §2: c = 0 forms, products such as L(delta+h/2)/(6m), the (2/pi)G(delta+h) value, and constants drawn from monotone geometry (b_s >= X-1/2, ell >= delta-h/2, m/n <= tau0). I checked all of them; they are valid. Add one sentence covering them.

**F4 — MINOR (traceability).** Three sources are not traceable from the text:
- `comp:142-145`: the bound (16) should be cited as C04-near-limit-comparison.md eq. (3), the C01 directional bound plus C04-near-01 (1), phase-only, rather than "C04's phase-only bound".
- `comp:175`: the 11270/n term is not derived in the text. It is 45000·(1/4) + 40·(1/2), from (15) with r2 <= rho^2 <= 1/4 and beta <= 1/2.
- `comp:116-117`: "the old n>900000 rounding" should cite C05-model (11).

**NOTE 1.** N1-06's published domain (n >= 804248) also excludes [500000, 804247]. The near files correctly use only its K >= R identities (`rep:73-77`). I confirmed that N1-10 needs nothing else from N1-06.

**NOTE 2.** The C05 refinement to 403/n is genuinely needed: the original 4rh bound gives 1.024e-3 > 1/1000 at n0.

**NOTE 3.** Margins are tight at two places but strictly positive with exact arithmetic:
- A(131/10) - 1225/144 - 32/9 - 19/4 = 0.0456;
- log n0 - 131/10 ≈ 0.022.

Other margins are large: eta0 is about 1/3 of its 1/1000 budget, and the (18) total is 6.1e-4 below 1/32.

**NOTE 4.** `rep:123` says N1-11 uses "m/n<=2". Its tail step actually uses m/n <= 9/8, which is true for n >= 8. This is harmless.

**NOTE 5.** Upstream records C05-finiteh-01/02, C04-near-02 and C02-defect-01 carry "PROVED developer; independent review required". Supplementary Codex/Astra checks accepted them, but formal Claude audit of those records is a separate obligation, outside this interim scope.

## 6. Executed computations

Environment: Python 3.13.18, standard-library `fractions` only, on this container. Scripts are in `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/near-code/`:
- `eta0.py` (sha256 c0dd5844…f5d5)
- `misc.py` (sha256 8b96726f…b34)

Each run took well under 1 CPU-second.

`python3 eta0.py` printed, among other lines:
- `total 12989329736187619160983471/38345245772322816000000000000 0.00033874681135994116`
- `equal? True` and `<1/1000? True`
- `(18) 383/12500 True True -1593/50000 True -1593/50000`
- `11270? 11270`
- `hess 43988 8437761 22002437761/500000 True`
- `slope 22656 True`
- `quot 0.7601274283036008 True`
- `arg 5617/14 True True`
- `15000/n True`
- `A 16.8580625 76729/16000 4.7955625 True True`
- `alpha max 1366875/28768731136 4.751252300764663e-05 True`

`python3 misc.py` printed True for every check:
- log10 lower bound 2.30163; exp(0.7) lower bound 2.01217; (2.7)^14 = 1094189.9 > n0;
- X >= 159.09 > 159, and X - 1/2 > 158;
- 128pi/m < delta;
- delta - h/2 > 249/250000;
- delta + h < 126/125000 and delta + h/2 < 101/100000;
- G = 9.502e-7 < 1e-6;
- log(2/ell0) < 8; log 158 < 6;
- e_A = 4.68e-9; e_log < 1e-9;
- 516^2/18 < 15000;
- the (14), (15) and (16) comparisons at L = 3, 13.1 and 14;
- the exp terms: 3.28e-6 and 5.9e-65.

All other checks were by derivation or inspection, as marked in §1.

## Remaining uncertainty

- I verified each degree-dependent step and the arithmetic. I did **not** re-derive from first principles the n-independent cores of the upstream proofs. Those were taken as written in their records: N1-13's variation constants, N1-14's central formula, N1-16's 2(L+5) row bound and coefficient identity, C05's partial-fraction and product-rule bounds (15)-(19), C05-model's exact strip/outer cancellation algebra (6)-(9), C01, C04-near-01, C03's slope, and C02-defect's dense-band construction.
- The completeness of the E_rest decomposition (that every M_near term is charged once) was checked by structured inspection, not by an independent symbolic expansion.
- I did not read N1-01/02/04/05/07 beyond their degree hypotheses (n >= 2).
