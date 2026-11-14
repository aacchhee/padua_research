# Audit2 module m2: the scalar H and fixed-model analytic chain

Interim Claude audit for handoff 10. Supplementary subagent module. It does not replace the orchestrator's audit-02.

- Auditor: Claude Opus 5.5, xhigh effort, acting as independent mathematical auditor. The model was chosen because this is an adversarial audit of a novel mechanism (WORKFLOW allocation table).
- Repository: `aacchhee/padua_research`. Branch `codex/padua-argmax-bridge-20261105`. Head and rules SHA `1b6aa31ae759022ce89bb8a3be70a881790e259f`, at which I read AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md.
- Changes: no repository file was edited and no state-changing git command was run. Read-only `git rev-parse` and `git status` were used.
- Novelty scope: this module audits proofs and makes no novelty claims, so the full read of `state/IDEAS.md` is omitted. The ideas task belongs to the orchestrator.
- Labels used below:
  - [D] = my own derivation;
  - [E] = my own execution;
  - [I] = inspection only.

## Verdict

**There are no BLOCKING and no MAJOR findings in this scope.** The following claims are supported at the stated closed domains:

- E07's scalar theorem: the strict third-derivative sign, the unique period maximum, and H(x)-H(0) <= -(pi-3)x^2/(4pi^3) on the closed period |x|<=pi.
- The E06 consequence map.
- The E10 unsplit root bound.
- The E11 paired-root bound with its exact negative beta baseline, and the closed rho<=pi/2 model extension.
- The rational chains of the E07 fixed-512 assembly.
- The E04-local-constant coefficients.
- The E05 axis-excess constants I re-derived.

I found one MINOR record-hygiene finding and several NOTEs. Each accepted status matches its review record's disposition text. None of those records accepts its theory "with conditions". The only nonblocking review notes, both labelled N1 (in the E06-H and E07-global512 reviews), are self-resolved strictness remarks.

## Execution record [E]

All scripts are in `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit2/m2-code/`.

- Environment: Python 3.13.18, with mpmath 1.3.0 and sympy 1.14.0 installed by `pip install --target audit2/pylib`.
- Wrapper: `run.sh <script>` runs `python3 -I` with pylib on the path, writes `<script>.out` and `.err`, and appends `exit=$?` and bash `times`.
- An initial attempt using `/usr/bin/time` exited 127 because the binary is absent. Nothing ran in that attempt.
- Every run below shows `exit=0`. Total CPU is about 65 s, well under the 15-minute cap.

| Script (sha256 prefix) | Content | User CPU |
|---|---|---|
| e07_scalar_check.py (a0215c43) | f closed form vs E07 (9); f''' (10) vs direct differentiation; ratio sup; B; J; g(0); H by (1) and (20) | 21.5 s |
| e07_H_gl.py (47495e3d) | H sampling redone with Gauss-Legendre after the cusp-cancellation diagnosis below | 4.6 s |
| hpi_debug.py (3d1a1b11) | diagnosis of the tanh-sinh endpoint cancellation at the cusp | 0.4 s |
| h0_kappa_cross.py (3a3d10a2) | H0 by direct quadrature at dps 40, then the kappa implied by E06(11) | 0.4 s |
| e06_e07_rationals.py (7c959b14) | 48 exact-Fraction/sympy checks for E06 consequences and the E07 global512 chain | 0.5 s |
| e10_e11_central_check.py (e9d6453c) | J closed form vs direct I; E<=Z; Ec grid on closed rho<=pi/2; x=0 identity; axis ratio; K and F kernels | 21.2 s |
| e11_grid_refine.py (07f11286), e11_grid_refine2.py (9a8a42d6) | J validated to 1e-16 with all kink breakpoints; relative slack of E11 (2) for x>0 | 8.3 s, 7.8 s |
| e10_e11_rationals.py (3058e75f) | 19 exact checks: E10/E11/E11-5/4/E04-local-constant/E05/E14 Bbeta coefficients | 0.5 s |
| iv_elementary.py (b3ec0e70) | mpmath `iv` outward interval checks of 14 elementary scalar constants | <0.1 s |

**Numerical caution [E].** mpmath's default tanh-sinh quadrature mis-evaluates H(pi): it returns -0.2882 to -0.2913 depending on the breakpoints. The cause is catastrophic cancellation in f(pi-v)-1, divided by sin(v/2), at nodes extremely close to v=0. Gauss-Legendre gives H(pi) = -0.28748647904650932731, which equals E06 (8), (2/pi)log(2/pi), to 25 digits. All H statements below use Gauss-Legendre. Any future numerical H check should avoid endpoint-clustering rules at the cusp, or use the endpoint expansion.

Audited theory prefixes: I recomputed the byte-prefix SHA256 of each audited file. All match the hash their review accepted:

| File | Prefix | SHA256 |
|---|---:|---|
| E07-f | 10945 B | e20d211d |
| E06-frontier | 10786 B | 64808c06 |
| E06-consequences | 16026 B | 1037878f |
| E10 | 13972 B | 28ff45c1 |
| E11-pair | 10942 B | dea44db8 |
| E11-halfpi | 10157 B | 695800c1 |
| E11-5/4 | 9450 B | ee98de67 |
| E07-global | 19080 B | 932b1bbc |
| E04-local-constant | 3684 B | 5cca41fa |
| E05-axis | 12863 B | 27c706d5 |

## 1. E07 scalar theorem (theory/E07-f-monotonicity.md)

**Definition of H [D, I].**
- N1 and E06-frontier (2) give Phi_0(t) = sin(pi t)[-psi(t)-psi(1-t)-2log pi]/pi.
- I re-derived that f(x) = Phi_0(1/2+x/(2pi)) = cos(x/2)/pi·[-psi(1/2+u)-psi(1/2-u)-2log pi], with u = x/(2pi).
- Expanding the digamma pair gives exactly E07 (4): k0+4x^2·sum over odd l of 1/(l(l^2pi^2-x^2)), with C0 = 2gamma+4log2. So the series is the same scalar, not a substitute.
- Endpoint values [D]: f(pi) = 1 and f'(pi-) = (log pi-gamma)/pi. Hence the derivative atom is -J·delta_pi with J = 2(log pi-gamma)/pi. Numerically [E], f'(pi-) from (9) matches (log pi-gamma)/pi to 15 digits.
- H is (1) as stated, with lambda0 = (2/pi)log(4/pi).

**Endpoint-cancelled integral, step by step [D].**
- (5): the product-to-sum evaluation is correct, including the (-1)^j sign. The l·pi/(l^2pi^2-x^2) and 1/(l·pi) pieces combine to x^2/(l·pi(l^2pi^2-x^2)).
- (6): the K_r formula is the real part of r·e^{i·pi·t}/(1+r^2·e^{2i·pi·t}), and |1+r^2e^{2iθ}|^2 = (1-r^2)^2+4r^2cos^2θ. The bound 5/(8cos) comes from (r+1/r)/4 <= 5/8 on [1/2,1).
- (8): the numerator bound is a mean-value bound; the denominator bound is Jordan's inequality. Together they give a uniform dominator of 5|x|/16. Abel's limit is legitimate by absolute convergence.
- (9) holds for |x|<pi and extends to the endpoint by continuity: at x = pi the integrand is identically 1, giving f(pi) = 1. No singular Fourier series is evaluated.
- [E] f from the closed form vs (9): maximum difference 1.9e-23 over 9 points, including x = pi-1e-8 and x = pi.
- (10): every x-derivative of cos(xt)-cos(x/2) vanishes at t = 1/2, so differentiation under the integral is dominated. The third-derivative formula is exact. [E] It matches mp.diff of the closed form to 1e-32.
- (11): R_t(x) = sin(tx)/sin(x/2) is increasing because z·cot z decreases on (0, pi/2], so R_t(x) <= R_t(pi) = sin(pi t).
- (14)-(17): the sign direction is correct, because a negative numerator divided by cos in (0,1] gets smaller. The pieces are 2∫_0^{1/4} = -549/8960 = 44/35840-1/16 and 2∫_{1/4}^{3/8} <= -37/2048. [E, exact Fraction] B < -311/71680.
- (13): f0 < 72/125 follows from C0 < 4, log pi > 11/10 and pi > 25/8. [E, interval] it holds.
- Conclusion: f''' < -(311/71680)sin(x/2) on (0,pi) is PROVED.
- [E] The sampled sup of f'''/sin(x/2) over 404 points is -0.103314. It is approached as x→pi-, equals B = -0.1033136 numerically, and is consistent with R_t increasing. The rational constant is about 24 times weaker than this but valid (NOTE N1).

**Unique maximum and the quadratic drop on the closed period [D].**
- The second-difference/triangular kernel integrates to W(t) = ∫_{|t|}^{pi} log cot(s/4) ds. I checked this by parts: K(v) = ∫_v^pi ds/(2sin(s/2)) = log cot(v/4).
- In (20) the atom contributes only at t = pi-|x| inside [-pi,pi]. At x = 0 both representatives carry W(pi) = 0, so nothing is double counted.
- Rearrangement on the circle: g - g(pi) is even, nonnegative and radially decreasing (by (2)), and W is even and decreasing. Arc intersections have length at most min(|A|,|B|), even when an intersection wraps around the circle. So W*g is maximal at 0.
- Remaining inputs:
  - f(x)-f(0) <= 3x^2/(2pi^2) (C04);
  - W(pi-x) >= x^2/4, since the derivative of the integrand is 1/(2cos(s/2)) >= 1/2;
  - 0 < lambda0 < 1/(2pi), equivalent to pi > 4e^{-1/4};
  - J > 1/pi.
- These give (3), including x = ±pi.
- [E] The C04 input is consistent: g(0) = f''(0) = 0.141064 < 3/pi^2 = 0.303964, and g(pi-) = -1/12 exactly, from (9) [D].

**Numerical cross-checks (sampled, not a proof) [E].**
- H via (1) and via (20) agree: H(0) = 0.310002264407 and H(2) = 0.0596339015 by both routes.
- Using Gauss-Legendre at 134 points (x = 1e-4…3e-2 and pi·k/128, k = 1…128), max[H(x)-H(0)+(pi-3)x^2/(4pi^3)] = -6.8e-10, attained at x = 1e-4. It is negative everywhere sampled.
- H is strictly decreasing on the 129-point grid.
- (H(x)-H0)/x^2 = -0.0688282 at x = 1e-4 and 1e-3, compared with the proved coefficient -0.0011416. The actual drop is about 60 times the proved drop (NOTE N2).
- H(pi-eps)-H(pi) > 0 at eps = 1e-2 and 1e-3, consistent with E06 (9): pi is a strict local minimum.
- The review record independent-checks-E07-H.md says ACCEPT with no finding [I], which matches the theory status.

## 2. E06 frontier, consequences and axis records

- **E06-H-frontier [D, E].**
  - (6) matches E07 (20).
  - (7): lambda_k = lambda0-(4/pi)·sum of 1/(2j-1), since I_k-I_{k-1} = 4/(2k-1).
  - (8): H(pi) = (2/pi)log(2/pi). [E, Gauss-Legendre] it agrees to 25 digits.
  - (11): H0 = kappa/2+(2k0/pi^2)log(2/pi). I re-derived the algebra: 2H0 = kappa+2k0·log(2/pi)/pi^2.
  - [E] My direct H0 = 0.31000226440731418510321202049923 implies kappa = 0.91971011838849253509951822579024. This lies inside PD-T271's 30-digit enclosure. The implied Cstar = 1.84616031042392607975983873794784 also lies inside its enclosure. This is an independent numerical, not interval-certified, corroboration of both the E06 identity and the PD-T271 constant.
- **E06-H-consequences [E, exact Fraction].** All rational steps in (3), (6)-(8), (10)-(11), (13) and (15) reproduce exactly, and the algebra of (4), (5), (9) and (13) re-derives [D].
  - The left side of (6) equals 196015/10^6 exactly at the rational input bounds. The claimed strict ">" holds for the true values because delta > 403/1000 and j > 23/250 are strict. This is a NOTE only; the strict difference is 651/10^6.
  - Under HM with eps = 0, the correlated bound gives ΔC∞ <= -j/2+sqrt(j^2/4+t0^2) < 0.3984 < 101/250 [D, E]. This uses only j > 23/250 and t0 < 221/500, independently of the Cstar lower bound.
  - [E, interval] Every elementary scalar used holds: log pi > 11/10, gamma < 3/5, C0 < 4, 161/100 < k0 < 9/5, t0 < 221/500, g0 < 43/125, d0 > 39/250, v0 > 0. With PD-T271's kappa, also 7/25 < H0 < 8/25 and j ∈ [0.143541, 0.143542] > 23/250.
  - Review NOTE N1 (strictness of (13) at u = 0) is correctly self-resolved.
- **E06-axis-boundary [I].** I read only the statement and domains. The shrinking closed domains 0 <= alpha <= min(2/5,h/2) and 0 <= alpha <= 1/(32nH^2), n >= 10^6, are nested as claimed [D]. The review says ACCEPT. This record does not feed the n >= 320 theorem; in my grep, no E14 file references it.

## 3. E10 and E11 central model

**E10 [D].**
- E <= Z for all v, s >= 0, with E = Z for s >= v. Both sides vanish at pi/2 and have the identical derivative -2·sqrt(...)/sin e. For s < v, J <= 0 by the entropy formula, and sqrt(v^2-s^2sin^2) >= s·cos.
- The translation steps hold: tan A - tan B >= tan(A-B), and Z decreases in s and in e.
- In (11), the Tonelli/substitution step uses the exact identity tan(t/2)sin t = 1-cos t. The second interchange gives arccos(1-tau·z) <= t.
- In (12), with w = cot t, the bound 2(1-k)^2 <= 2-k holds on [0,1]. The step in (13) uses ∫sqrt(1-z^2)z^{-1/2} dz = 2·I4.
- The constants (14)-(15) hold [E, exact]: I4 < 319/360; 3/8 and 5/12 from the products 51040 < 51417 and 306240 < 310275; 1/(aπ²) < 1/9 and < 2/15.
- The guard a >= 49/64 holds because cos(1/2) > 7/8 [E].

**E11 pair [D].**
- (7) is an exact identity: sL+sR-2s0 = 2(delta-s0)_+, and the support is exactly (0,b). So Bbeta >= 0 is a retained exact term, not a bound.
- (10): the substitution w = a·tan(e/2) gives Jacobian 2a/(a^2+w^2). Folding the "+delta" channel by w → -w, using that W_t and R_t are both even, gives the real-line correlation ∫W_t(w)R_t(w-delta) dw.
- (11) is the one-dimensional Hardy-Littlewood interval-overlap inequality. It is proved directly and correctly, for all a > 0 and v, delta >= 0.
- Conclusion: Ec <= (2/π²)F - Bbeta <= κp^{3/2}/sqrt(a) - Bbeta.
- **Handoff claim confirmed.** The whole paired integral is bounded before any majorization. This removes both of E10's artificial positive charges:
  - the discarded negative baseline (E10 replaced sL+sR by 2s0);
  - the e<b entropy charge -q·log(sin e) for the right channel, which gave E10's (q/π²)Lsin(b) term.
- At the same time it keeps the genuine fractional alpha cusp: κp^{3/2}/sqrt(a) is unchanged, and the axis coefficient κ is from C01/D10. The negative-beta baseline is preserved exactly. At x = 0, Ec(0,y) = -Bbeta exactly, because Z(0,·,·) = 0 and J(0,s,e) = 2s·log(sin e).
- No sign of E is assumed, and no Ec monotonicity in beta is claimed. I agree that none follows.

**Closed rho <= pi/2 model (E11-model-radius-halfpi) [D, I].**
- Domain identities: 2a = 2cos(rho/2)cos(d/2), P = 2sin(rho/2)cos(d/2), and 2a-P >= 0, strict for rho < pi/2.
- Hence a >= 1/2, v/a <= 1, and b <= rho <= pi/2, with b = pi/2 only at (0,pi/2). Also (T-q)sin t = 2a(1+cos t) - q·sin t >= 2a-q > p.
- These are exactly D37's no-root conditions. I inspected D37-constant-wide lines 24-45: its identity used only 2a-P > 0, T > P and (T-q)sin z > p; the 7/8 floor served those and the separate regular-increment table.
- The closed edge follows by the uniform dominator 10|log sin t|+4log2. That dominator holds because v <= 1/2, s <= 3/2 and s0 <= 1 on the domain.
- [E] Results on the closed rho <= pi/2 grid (axes and edge included; N = 10 gives 66 points; N = 12 for x > 0):
  - max over the grid of [Ec - (κp^{1.5}/sqrt(a) - Bbeta)] = 0, attained only on x = 0, where the identity is exact;
  - for x > 0 the maximum relative slack is -0.4548;
  - at the corner (pi/2,0), Ec-rhs = -0.637;
  - at (pi/4,pi/4), Ec-rhs = -0.203;
  - |Ec(0,y)+Bbeta| <= 2e-22 at y = 0.3, 1 and pi/2;
  - the E10 bound (2) holds on the rho <= 1 subset;
  - the 3/8, 5/12 and 9/20 forms hold on rho <= 1/2, 1 and 5/4;
  - the C06 closed-form J matches direct cancellation-integral quadrature to 1.1e-16 on 6 parameter triples, covering the root, no-root, s≈v and large-s cases;
  - the axis ratio Ec(x,0)/(κp^{1.5}/sqrt(a)) is 0.767, 0.906 and 0.964 at x = 1e-2, 1e-3 and 1e-4, which is consistent with a limit of 1.
- **Finite guards are not enlarged [I].**
  - E11-halfpi states this explicitly.
  - Downstream, E14-halfnear uses E11 only on r <= 1/2, and E14-annular only on r <= 1. Both are inside the model theorems' domains, and E14's finite allowances keep their own guards: r <= 1/2 for the E09 functions and r <= 1 for E14-wide/E04.
  - E14-outer says the E11 local model is not used on the outer diamond.
  - The only closed-pi/2 use is E12's corner diagonal, which pairs the model with the global absolute CEbar+KD·P error. The E12 review states this.
- E14-halfnear's Bbeta >= (1679/8000)y^2 re-derives [D, E]: the tan convexity chord, ∫(1-e/b)(-log e) = (b/2)(3/2+log(1/b)), q >= 23y/24, and b·[...] increasing in b.

## 4. Fixed-512 assembly (E07-global-assembly) [E, D]

- All 30 displayed rational links reproduce exactly:
  - T(512) > 69/5;
  - V > 27/2 and UN, UW > 1699/125;
  - C4 = 203/24576;
  - the kN and kW bounds;
  - the CE pieces, summing to 809/1000;
  - the Ah, Bh, Aw, Bw certificates;
  - the Fn and Fs comparisons (1120157500 > 1105854464);
  - Lh(21/40) and Lw(3/5) = 501/12500 > 1/25. This is tight but strict.
- The radial-line maximum formula e, f, g is verified symbolically by sympy.
- The radial quadratics also reproduce exactly in every region: the half-near e, f and g; discriminant (7), 37859375 > 37845000; BOX; LARGE, including the boundary values -13/160 and -733/1600 reached at equality but strict through strict inputs; FAR, giving -571/8000; and GO_H = 881/16000.
- n-monotonicity of the displayed families [D]: C4, kNx, kNy, kWx, kWy, KD and (67+19L)/n+318/n^2 decrease; T increases; Fn and Fs increase.
- I did not re-derive the monotonicity of CE, E0, D, Gg, Mesh, W or the Fh/Fw formulas, which come from E01/E02 (see the not-re-derived list).
- Review NOTE N1 is correct: p+r <= 51/14 at r = 1/2, and 711200 > 706401.
- This theorem is now superseded in range by E14 for n >= 320. E14 does not depend on it.

## 5. E05 and E04 pieces: closed guards and dispositions

- **E05-axis-central-excess [D].**
  - (2): csc^2 <= (225/784)n^2/k^2 < n^2/(3k^2), using pi > 3 in the decreasing function pi/(pi-1/5). This gives Rcen <= alpha^2/(3m).
  - (11): I re-derived the critical-point maximum: K_e/a peaks at (cos e - sqrt(1-λ^2))/(1+cos e), and λ <= 16alpha/(15e) because tan(alpha/2) <= 8alpha/15 on [0,2/5].
  - (12): centered-cell quadrature error <= Var/(2n) = max/n. The factor 1/2 is justified because |f(c) - avg over the cell| <= Var_cell/2.
  - (13) holds in both regimes, and 48/(5pi) < 16/5.
  - The closed domain 0 <= alpha <= 2/5 is retained. The main cusp-aware target (4) is correctly OPEN.
- **E05-cusp-aware-error [I].** Closed rho <= 1/(n+1)^2 with n >= 32 is the stated and accepted scope. I read the statement and the disposition; the proof is not re-derived.
- **E04-local-constant [D, E].** Every guard and coefficient reproduces exactly:
  - BOX: a >= 7/8, tau <= 2/7, 6a(2-tau) >= 9;
  - rho <= 7/8: a >= 207/256, tau <= 112/207, 6a(2-tau) = 453/64 > (21/8)^2;
  - Af, hx and hy bounds;
  - the full table: 17/20, 7/80, 151/120, 29/30; 189/200, 153/1600, 781/600, 2359/2400.
  - E07-global uses Qx = hx = 7/15 and Qy = 3hy/2 = 7/40, correctly without the 19/24 term.
- **E04-wide-retained-origin, radiusone-defect and wide-corner1 [I].**
  - The stated closed domains match the scopes accepted in independent-checks-E04-assembly640.md and independent-checks-E04-wide-retained-origin.md:
    - defect: n >= 64 for the min form and n >= 640 for > 1/200, with corners excluded;
    - corner: n >= 512 on the closed square 0 <= A,B <= 1;
    - retained origin: n >= 32 on closed signed rho <= 1.
  - Reviews accept the frozen prefixes: radiusone f6d0cbea, corner 501efd8e, local-constant 5cca41fa. Those are recorded as unchanged in the assembly review.
  - The dispositions read ACCEPT with no unresolved finding. The only note is a wording NOTE T1 in the 640 assembly review. No acceptance is conditional beyond the named upstream premises.

## 6. PD-T271: what it supplies and at what scope [I, E]

**Location.**
- topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md (sha256 957802f2…).
- PROOF_STATUS.md row 374.
- Accepted by that topic's Claude audit-01, line 17: "ACCEPTED, PROVED; κ and c brackets independently confirmed by a different rigorous route".
- Its trusted base is python-flint/Arb outward arithmetic: the series is summed to K = 64 at 320 bits with an analytic tail. Independent reruns are in independent-checks-analytic.md.

**Statement.** For n >= 32 and N = n+1/2,

    Λ_c(n) = (4/π²)log²N + b·log N + c + R_n,

with an explicit bound |R_n| <= 604n^{-1/5}+…. The constant c = c1²+κ comes with 30-digit enclosures of κ and c.

**What the E-chain uses it for.** Only the n-independent limiting origin constants:

- κ, entering through E06 (2): H0 = κ/2+(2k0/π²)log(2/π).
- Cstar = c, identified with C∞(0,0) by D08's limiting transfer.

The rational consequences actually consumed are:

- 9/10 < κ < 23/25. This gives 7/25 < H0 < 8/25 and j > 23/250. The constant j enters every n >= 320 E14 gate I inspected, through the term -j·u (half-near, annular, and the outer j* = 23/250).
- 923/500 < Cstar < 1847/1000. This gives C∞ < 9/4 and ΔC∞ < 101/250, which E07-global512 and E08-corner384 use. E14-outer uses the correlated (j*, t*) form instead.

**Scope.**
- Model origin only (rho = 0). No n floor is imported.
- PD-T271's finite remainder R_n is never used as a finite Λ_c lower bound. E06 disclaims this explicitly, as do E14-outer and E14-assembly. The finite origin costs come from E0/ebar (E01/E03/E08).
- The E07 scalar theorem itself does not use PD-T271.

**Precision actually needed [D, E].** The E14 chain needs only H0 > 7/25. The true H0 = 0.3100022644, so the margin is about 0.03, and true j = 0.14354 against the bound 0.092. So the dependency is very coarse (NOTE N3).

## Findings

| ID | Severity | Location | Finding and evidence | Recommendation |
|---|---|---|---|---|
| m2-M1 | MINOR (record hygiene) | theory/E04-radiusone-defect.md:234, E04-wide-corner1.md:182, E04-wide-retained-origin.md:368; similar in E03-*:323/398/332 and E05-cusp-aware-error.md:357 | Root-adoption appendices assert "Global onset remains 768, residual 719 … matched640 remain OPEN here". Every adoption in the campaign is dated 2026-11-07, so the date does not mark these lines as historical, and the files' own text now contradicts the current state (onset 320, residual 273). | Add a one-line dated pointer, e.g. "superseded: current onset in results/…", in each such appendix, or reword as "at adoption". No mathematics changes. |
| m2-N1 | NOTE | E07-f-monotonicity.md (2), (17) | The proved -311/71680 is about 24 times weaker than the observed sup of f'''/sin(x/2) = B = -0.10331 [E]. It is correct. | None required. |
| m2-N2 | NOTE | E07 (3), E06-consequences (9)-(10) | The observed (H(x)-H0)/x^2 = -0.06883 near 0 [E] is about 60 times the proved -(π-3)/(4π³) = -0.00114. Under E06 (9) the proved drop already adds ≤ -2·c_H·min(ce,cd)(x²+y²) ≈ -0.002(x²+y²) to ΔReg on rho <= 1, which the current assemblies drop. In finite gates T dominates, so the possible gain is a few percent of curvature. | An optional idea for the ideas record; not required. |
| m2-N3 | NOTE | E06 (1)-(3); E14 gates | The PD-T271 dependency of the n >= 320 chain reduces to the single scalar inequality H0 > 7/25, and E07 (1)/(9) make H0 a smooth 1-D integral. My non-certified quadrature reproduces PD-T271's κ to 30 digits. | Optional dependency reduction: a certified interval quadrature, or an elementary bound, of H0 > 7/25 would replace the Arb series premise. Keep PD-T271 explicit until such a certificate exists. |
| m2-N4 | NOTE | E06-consequences (6)-(7) | The displayed lower 196015/10^6 is attained exactly at the rational input bounds. Strictness comes from strict input inequalities. Same type as review NOTE N1. | None. |
| m2-N5 | NOTE | E10 (12)-(13), E11 | The kernel bound K(k) <= 1/sqrt(2k) is loose away from k = 0: K·sqrt(2k) = 0.99, 0.68 and 0.074 at k = 0.01, 0.3 and 0.9, and F divided by its bound = 0.92 and 0.71 at (v,a) = (1/4,0.9) and (1/2,1/2) [E]. Relative slack of E11 (2) is ≥ 45% at grid x >= π/24. This quantifies the deferred "kernel-moment sharpening". | Optional cost reduction; deferred status is appropriate. |
| m2-N6 | NOTE | tooling | The tanh-sinh cusp cancellation described in the execution record. | Use Gauss-Legendre or analytic endpoint handling in any future H numerics. |

## Not re-derived (read only or used as named premises), and remaining uncertainty

1. C04's distributional bound df' <= (3/π²)dx (C04-near). It is numerically consistent: g(0) = 0.141, and g is decreasing.
2. C08's λ0 < 1/(2π) proof and f(0) <= f <= 1. I checked these by interval and sampled evaluation, not by reading C08's proof.
3. N1's Phi_0 normalization, beyond the digamma form I re-derived.
4. D10, D24 and D37:
   - the exact decomposition C∞ = E∞+ce·H(d)+cd·H(e)-c·a+Ec, and E∞(0) = 1/3+B;
   - the weighted endpoint inequality E∞ <= a/3+B-d0·u-v0·z on rho <= pi;
   - D10's central coefficients 77/96, 1/12, 4/9 and 1/6;
   - D24's central coefficients 109/120, 3/32, 1/2 and 3/16;
   - D37's central coefficients 1, 1/10, 8/15 and 1/5;
   - D37's 19/24 regular increment and f4 table.
5. D02 continuity of the true C∞, and D08's limiting transfer C∞(0,0) = Cstar.
6. C06's generic J identities. I validated them numerically to 1e-16 but did not prove them. Also C01's axis asymptotic Ec(x,0)/x^{3/2} → κ, which is numerically consistent but converges slowly.
7. PD-T271 itself: t4-01/t4-02 proofs and the Arb evidence. I read the statement and the audit disposition lines only. The κ corroboration above is numerical, not certified.
8. All finite-n operator inputs:
   - the formulas for E01/E02/E03/E08 CE, E0, ebar, KD, D, Gg, Mesh, W and G0, and their n-monotonicity;
   - E01 Fh/Fw floors;
   - PD-T101/216/220/226/364 polynomial normalization, zero mask and physical cover;
   - E04-wide-retained-origin retained-row bounds, the E04-radiusone-defect floors, and the E04-wide-corner1 D08/D27 corner proof;
   - the E05-cusp-aware-error and E06-axis-boundary finite proofs;
   - E09/E13/E14 functions, beyond the specific E11 and Bbeta constants checked in section 3.
9. E07-global's "accepted D10 central radical bound for Ec" on r <= 1/2. The coefficients were taken as given.

Remaining uncertainty: within my scope it is confined to the upstream premises listed above. Every sampled numerical check is MEASURED evidence only. Each PROVED status I endorse rests on the written paper argument, re-derived where marked [D].
