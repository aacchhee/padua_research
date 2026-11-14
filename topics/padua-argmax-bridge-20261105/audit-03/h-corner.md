# Audit-03 component H: sharp Padua corner expansion

Auditor: Claude Opus 5.5, xhigh. This is an independent mathematical subagent of the Claude audit-03 orchestrator, working on the first bullet of brief section 1. Opus xhigh was chosen because the brief asks for an adversarial reconstruction of a novel analytic chain. Repository `aacchhee/padua_research`, branch `codex/padua-argmax-bridge-20261105`, head `f366535e1fa4ede566cb83bdc554220c12b307cf`. I read the rules (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md) and the brief at that head.

No Git state was changed and no repository file was edited. Outputs are this file and `$A/h-corner-code/`, where $A is `/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit3`.

Labels: [D] my own derivation, [E] my own execution, [I] inspection only.

Novelty scope: the brief limits this component to mathematical correctness. I did not read state/IDEAS.md in full and make no novelty or priority judgement. The H candidates do keep their dispositions in the files I inspected: H02 and H03 are DEFERRED, H06 is consolidated into H01, and H04 and H05 are PROVED support [I].

Audited file hashes (SHA-256). These match the hashes accepted by the main and support reviews:

| File | SHA-256 |
|---|---|
| H01 | a57e3e1d… |
| H04 | 25ffa263… |
| H05 | 755e574e… |
| H06 | 75a56f85… |
| F03 | ddccb051… |
| PD-T269/270/271 | a40f61a4… / ead57816… / 957802f2… |

The canonical theory file H-sharp-corner-expansion.md has hash b31aae94… (see H-C04).

## Verdict

**SUPPORTED: the analytic proof holds at its stated scope, with no BLOCKING or MAJOR finding.** The statement is

    Lambda_c(n) = (4/pi^2)(log N + gamma + log(8/pi))^2 + kappa - 1/N + O(log N / N^2),   N = n + 1/2.

It holds for every integer n >= 2 and both parities, with a degree-independent constant that is finite but not given numerically.

- I re-derived the exact finite corner sum independently from the definition and compared it with direct interpolation [D,E].
- I re-derived the two first-order coefficients beta_H and beta_B (β_B by a different route than H04), the cancellation identity and the half-step shift [D]. The structure of every O-term holds up.
- Numerics up to n = 204801 agree with the expansion at the claimed scale, in both parities [E, MEASURED]. The 1/N coefficient is not off by any constant: N*R = -7.2e-6 at n = 2.05e5.
- A separate numerical constant chain reproduces kappa to 30 digits without using PD-T269 [E].

The findings are MINOR or NOTE: stale status words, dependency-list completeness, one swapped coefficient in a majorant whose conclusion is unaffected, provenance of the canonical-file hash, and notation.

## 1. Independent reconstruction of the exact finite corner sum [D, then E]

**Convention.** The nodes are (cos(j pi/n), cos(k pi/(n+1))) with j+k even. Interpolation is in Pi_n (total degree n). The cardinal form is L_xi = w_xi [K_n - T_n(x1) T_n(xi1)], with weights w = (2/(n(n+1))) eps_j eta_k and multiplicities nu_0 = 1, nu_r = 2. So the (n,0) first-coordinate coefficient is one.

**Unisolvence and the exceptional coefficient.** I checked the Gram argument of preliminaries.tex. The alternating part vanishes because p+r = n and q+s = n+1 would force a total of 2n+1 > 2n. The diagonal is h_p^(n) h_q^(n+1), and its inverse is nu_p nu_q except at (n,0), where it is 1 [D].

**Reflection.** Reflect about (-1,-1): u = pi - theta, v = pi - phi. The reflected indices satisfy j'+k' odd. On the corner, Sum_{p+q<=n} nu_p nu_q cos(pu) cos(qv) equals 2[cos(Nu)cos(u/2) - cos(Nv)cos(v/2)]/(cos u - cos v). At mesh angles, cos(Nu) = (-1)^{j'} cos(u/2) and cos(Nv) = (-1)^{k'} cos(v/2). Removing the exceptional mode cos(nu) = (-1)^{j'} gives [D]

    |L| = w * 2cos^2(v/2) / |cos^2(u/2) - cos^2(v/2)|
        = w * cot(q) |cot(q+p) + cot(q-p)|,      p = u/2, q = v/2.

This equals the paper's 2f(theta,phi) form (corner-unified.tex:43-45).

**The collision.** The only collision is (j',k') = (n, n+1), the node (1,1). There the kernel value is (-1)^n(2n+1). After the exceptional subtraction its absolute value is 2n, with weight 1/(2nm), so it contributes exactly 1/m. Every other entry of the k'=n+1 row vanishes because cot(pi/2) = 0 [D].

**Row folding.** The functions are even about p = 0 and p = pi/2, so each row can be unfolded to a full period. The half weights eps_j at j=0 and j=n are exactly the trapezoid folding factors. The full-period sum is

    Sum_{l<n} cot(z + l pi/n) = n cot(nz).

With z = q + pi r/(2n) and r of parity k+1, cot(nq + pi r/2) = tan q, so the signed row is exactly n. The positive samples are those with j <= k-1 of opposite parity. The k=0 row is Sum_{odd} csc^2(pi j/(2n)) = n^2. Altogether [D]:

    Lambda_c = -1 + 2/m + (4/(nm)) Sum_{r=1}^{n} cot(pi r/(2m)) T_{n,r},
    T_{n,r} = Sum_{l=0}^{r-1} cot(pi(l + alpha_r)/n),   alpha_r = (1 - r/m)/2.

This is H01 (2) and paper (cu:exact) letter for letter. Splitting off the two poles with digammas reproduces D_{m,r} and V_n exactly, which is H-sharp (3) [D]. The endpoint weights, the r = n row, the k = 0 row with eta_0 = 1/2, and the exceptional 1/m are all retained. The paper's first identity 1 - 2n/m = -1 + 2/m checks.

**Executed checks [E]:**

- **brute.py.** Solves the interpolation system V^T l = phi(-1,-1) at 40 digits, with no cardinal formula. This agrees with my row formula and with the closed cardinal sum to 1e-39 for n = 2..12. For example, Lambda_c(3) = 3.776142374915396699201125816…
- **Repository float kernel.** phase_s(n,0,0) from ../padua-argmax-effective-2-20261105/code/phase_probe.c (included verbatim) agrees to about 4e-15 relative for n in {2,3,4,12,20,21,40,41,100,101,1600,1601}.
- **sidechecks.py, n = 2..15, 24, 31.** The same-mesh square (cu:square) holds to 1e-39. The deformation bound (cu:deform) is satisfied with max ratio <= 0.203. H03's identities (1), (2) and (3), including Sum K~ = 4n^2+2n-1, hold to 1e-35.

## 2. Reconstruction of the expansion [D]

**H05 centering.** I re-did the three Taylor shifts. The shifted arguments are r+q, s-q and m-q, with q = s/(2m). The remainder signs follow from psi'' < 0 being increasing. The constants are (h^2/2)[(x-h)^-2 + 2(x-h)^-3] at the lower arguments r and 3s/4, giving 3/8 + 22/27 = 257/216. The weighted bound uses cot x < 1/x. All of this is correct and uniform in 1 <= r, s <= m-1 with m >= 2.

**H01 aggregate.** Reconstructed line by line:

- (8): the psi(s) and -psi(m) scalars give -1/(2s) + 1/(2m), and the derivative bracket is 1 + x + u(r) + O(1/s + 1/m), so the net term is -x/(2m). The remainder O(s^-2 + (ms)^-1 + m^-2) is uniform.
- (10): split at m/2 using w <= am/r and w <= 2s/m (tan is convex), giving O(log m/m^2).
- (11): e contributes the constant a*S_e and no 1/m term. u contributes a*S_u/(2m).
- (16)-(19): R(0) = a(pi^2/4 - 1), R(1) = pi - a*c0, and R'' = O(1/x + 1/(1-x)). The endpoint cells cost O(log m/m^2) because R - R(0) = O(x|log x|). The log m/m terms cancel between Sum log r/r and the -a log m H_{m-1} term. The 1/m coefficient is -(pi + a c1)/2.
- Assembly: 2a[...] gives -a^2 log m/m + beta_H/m with beta_H = -2 - a^2(gamma + 2log2) - a(I1 + I2), using c1 + S_u = 2log2.

**beta_B by a different route.** H04 uses midpoint cells. I used the offset Euler-Maclaurin formula instead:

    Sum_{l<r} g(l+theta) = Int_0^r g + B1(theta)[g(r) - g(0)] + (B2(theta)/2)[g'(r) - g'(0)] + O(r * sup|g''|),
    with g(t) = B(t/n), theta - 1/2 = -r/(2m).

The row sum then becomes nI(t) + (t/2)(B(t) + B(0)) + O(t/n), the same as H04 (13). Next, w*I and W*(B + 1/pi) are analytic on [0,1], the cell is r/n = t(1 + 1/n), and the endpoint values are F(0) = a^2/2 and G(0) = a^2. The trapezoid rule then gives C_B = 4 Int w I and beta_B = -a^2 + 2 I_B + a I2, as in H04.

H04's explicit constants check: (6) |B'| <= 3, |B''| <= 5; (11)-(13) 17t/(16n); (19)-(21) 17/n^2. The one exception is H-C03.

**Cancellation identity and ledger.** The identity 2 I_B - a I1 = a^2 - 1 + a^2 log(pi/2) was re-derived from the combined integrand x(w^2-1) - 2aw + a^2/x and w' = -(1+w^2)/a. The endpoint term a*eps*w(eps) tends to a^2. The ledger of 1/m terms [D]:

- the base contributes +2;
- beta_H contributes -2 (= -a*pi, from R(1)), -a^2 c0 and -a(I1 + I2);
- beta_B contributes -a^2 + 2I_B + aI2;
- by the identity, the total is -1 - a^2 d.

**Why exactly -1/N.** The terms -(a^2 log m + a^2 d)/m equal -a A(m)/m. That is precisely the first-order shift from A(m)^2 to A(m - 1/2)^2. So N = m - 1/2 absorbs every logarithmic and d-dependent 1/m term. The pure -1 remains, and 1/N - 1/m = O(m^-2).

The -1 has a simple source. The ±a^2 terms cancel, beta_H's -2 cancels the base +2, and what is left is exactly Int_0^1 (-2x) dx = -1 from the combined integrand. No other 1/N-type term can remain, because every other first-order contribution is either a constant multiple of 1/n, which costs O(m^-2) to rewrite as 1/m, or part of -a A(m)/m.

**Limit interchanges.** Every step is a finite-sum inequality with absolute constants. The only limits taken are:

- absolutely convergent series: S_e, S_u, the psi series, and the cotangent partial fractions;
- the identification C = kappa, which uses only two sequence limits. Those are PD-T269 (Lambda_c - L_n^2 -> kappa) and PD-T270 (|L_n - A_n| <= 1/(4n^2)); A(m)^2 - A(n)^2 -> 0 is elementary.

PD-T269 handles its own exchange quantitatively: fixed-offset limits, endpoint strips via pi^2 n/(2l^2), and l-tails. That proof was audited earlier (Claude audit-01), and I read it [I]. No O-constant depends on a varying parameter outside its proved range. H05 holds uniformly in (r,s); H01's C's come from fixed functions or pointwise uniform bounds; H04's is explicit.

## 3. Constants and forms

- kappa = (8/pi) Int_0^1 t^2 cot(pi t/2) Sum_{l odd} 1/(l(l^2 - t^2)) dt (PD-T269 (1); paper eq:main-kappa, identical) [I].
- Using Sum_{l odd} t^2/(l(l^2 - t^2)) = (1/4)[2psi(1/2) - psi((1-t)/2) - psi((1+t)/2)] [D], quadrature gives kappa = 0.91971011838849253509951822579024 [E]. This is inside PD-T271's enclosure (0.919710118388492535099518225790, …791).
- b = 2a c1 = (8/pi^2)(gamma + log(8/pi)) = 1.225522125742012093966889 [E].
- c = c1^2 + kappa = (4/pi^2)(gamma + log(8/pi))^2 + kappa = 1.84616031042392607975983873795 [E]. This is inside PD-T271 (2).
- Expanding A(N)^2 + kappa - 1/N gives (4/pi^2)log^2 N + b log N + c - 1/N exactly [D].
- The same constants appear in H-sharp (1), the paper (eq:main-constants and Theorem thm:main-expansion), PD-T271's statement, the PD-T098 target as quoted in campaign-H-gate, and H01 (22). The m-form A(m)^2 + kappa - [1 + aA(m)]/m (main review) is algebraically the same [D].
- C13-corner-value-lower.md's Lambda_c > A_n^2 + d(n) - 1/1000 for n >= 5e5 is weaker and consistent with these constants: d(n) -> 16/25 < kappa. No constant is inconsistent.

Numerical quadrature (constants.py) of the coefficient integrals [E]:

    I1 = 0.74545690504804200238
    I2 = 0.44127120030530318679
    I_B = 0.031438458310111748085
    C_B = 0.33789871169461370905
    beta_B = -0.0614858468583960840   (inside H04's (-4/pi^2, 0))
    beta_H = -3.55127521601260996301

Identity (6) holds to 1e-46. 2 + beta_H + beta_B = -1 - a^2 d = -1.612761062871006 holds to 30 digits. S_u = 1 + 2log2 - pi^2/4 holds to 30 digits.

**Independent constant chain [D,E].** H01's structure gives C_K = gamma_1 (Stieltjes) and C_M = Int R + a gamma_1 + a c0 gamma. Then C_H = 2a C_M + 2a^2 S_e - a^2 d^2 and C = -1 + C_H + C_B. The values S_e = 0.0446658779921 and Int R = 1.26637992627437 give C = 0.91971011838849253509951822579. This matches kappa within 3e-31 (constant_chain.py). It confirms the identification C = kappa by a route that does not use PD-T269 (MEASURED).

## 4. Numerical consistency (MEASURED; not a proof)

**Evaluators.** corner.py "direct" is my O(n^2) row formula in Arb balls at 128 bits. "fast" is H01's split: an exact digamma part plus Euler-Maclaurin for the analytic B part, with K Bernoulli terms. Its truncation is not rigorously bounded; it was validated against direct:

- K = 16 for n < 2000: equal to about 1e-33 at n = 100..3201;
- K = 8 at n = 3200, 3201;
- K = 6 for n >= 6400: direct 6400/6401 differ from fast by 8e-30.

The fast evaluator also returns Hcal_m and 4V/(nm) separately.

**Remainder test.** R(n) = Lambda_c - [A(N)^2 + kappa - 1/N], with kappa the midpoint of the PD-T271 enclosure (error < 5e-31). Nothing was fitted. Excerpt of analyze.out (all n = 2..64 were also computed):

| n | Lambda_c | R | N*R | N^2 R/log N | N^2 R |
|---|---|---|---|---|---|
| 2 | 3.0 | 9.06e-2 | 0.2266 | 0.6182 | 0.5665 |
| 3 | 3.776142374915396699 | 4.43e-2 | 0.1552 | 0.4336 | 0.5433 |
| 40 | 11.909859409709588907 | 1.10e-4 | 0.00444 | 0.0485 | 0.1797 |
| 41 | 12.013758288146747993 | 1.02e-4 | 0.00422 | 0.0470 | 0.1752 |
| 400 | 23.742701126289361756 | -1.590e-6 | -6.37e-4 | -0.04255 | -0.2550 |
| 401 | 23.757879536571202236 | -1.585e-6 | -6.36e-4 | -0.04261 | -0.2555 |
| 6400 | 43.716561061004126915 | -1.935e-8 | -1.238e-4 | -0.09045 | -0.7927 |
| 6401 | 43.717862370025744756 | -1.934e-8 | -1.238e-4 | -0.09045 | -0.7927 |
| 51200 | 62.789119660597303539 | -4.566e-10 | -2.338e-5 | -0.11038 | -1.19694 |
| 51201 | 62.789315261529347689 | -4.566e-10 | -2.338e-5 | -0.11038 | -1.19695 |
| 102400 | 69.925622619137291407 | -1.2700e-10 | -1.3005e-5 | -0.11543 | -1.33172 |
| 204800 | 77.451582946064537407 | -3.4964e-11 | -7.1606e-6 | -0.119911 | -1.466491 |
| 204801 | 77.451637333614810162 | -3.4963e-11 | -7.1606e-6 | -0.119911 | -1.466492 |

- **The 1/N coefficient.** N*R tends to 0 monotonically: 0.23 at n = 2, -7.2e-6 at n = 2.05e5. A coefficient -1 + delta would give N*R -> delta, so |delta| < 1e-5 in range.
- **Bounded remainder.** N^2|R|/log N <= 0.62 for every tested n; the maximum is at n = 2. For n >= 6400, N^2 R decreases by an almost constant 0.1348 per doubling. This is consistent with a nonzero next log N/N^2 term; I estimate no coefficient.
- **Parity.** Adjacent even and odd n differ in N^2 R only by the smooth drift, about 1e-6 at 2e5. No alternating term is visible.
- **Components.** m^2 [Hcal - A_m^2 - C_H - (-a^2 log m + beta_H)/m]/log m stays in [-0.27, -0.25] for 6400..204801, with C_H = kappa + 1 - C_B. n^2 [4V/(nm) - C_B - beta_B/n] equals 0.0609 (H04 claims <= 17).
- **Side observation.** F03's E_n(0) = Lambda_c - A_n^2 - kappa > 0 at every sampled n, and n*E_n(0) is close to a^2(log n + d) - 1, as H predicts (origin_sign.out).

## 5. Dependencies and status words

The chain is: H-sharp (3) <- PD-T159 (positive sum, exceptional 1/m), F03 routine identities, and PD-T226 (signed periodic row = n). Then H01 (uses H05), H04, the identity (6), and C = kappa from PD-T269/270.

- No lemma is used outside its domain. H05 needs m >= 2 and 1 <= s <= m-1, and is used there. H04 needs n >= 2 and is used there. H01 uses m >= 3, which is n >= 2.
- PD-T269's rate bound needs n >= 32, but only its limit is used.
- PD-T270 holds for all n >= 1.
- Status words: the canonical H-sharp file and campaign-H-summary say PROVED. The reviews (independent-checks-H-main, Codex gpt-6-astra xhigh, and the integration addendum; and independent-checks-H-support) accept without conditions or unresolved findings.
- The frozen support files still carry development status words; see H-C01. F03 is overall OPEN, and only its routine identities are root-accepted (F03:222); see H-C02.
- Neither review executed numerics. Both missed H-C03.

## 6. Paper Section 3 versus the canonical theory (brief)

**Agreement.** The statement (intro lines 111-133), hypotheses, constants and the all-n, both-parity quantifier agree with H-sharp. The equations match H01/H04/H05 and the H-sharp integration:

| Paper (corner-unified.tex) | Theory |
|---|---|
| (cu:positive), (cu:exact) | H01 (2) |
| (cu:center) | H05 (1) |
| (cu:row-expand) | H01 (8) |
| (cu:H-to-M) | H01 (13) |
| M_m | H01 (19) |
| (cu:V) | H04 (2) |
| (cu:cancel) | H01 (20) |
| final ledger | H-sharp (7) |

**Self-containedness.** The paper is more self-contained than the theory. It derives the exact reduction directly (lines 25-107, which I verified) and proves the quadrature lemma.

**Completeness for a specialist.**
- Adequate overall.
- The most compressed passages are:
  - the kappa limit (lines 180-204), a sketch of PD-T269 §1-3, which is sufficient because only
    the limit is needed;
  - "These analytic factors prove R(0), R(1) and the derivative bounds" (lines 364-366).
- Nothing essential is deferred to the companion.
- The paper gives O(n^-2) for (cu:V) without H04's explicit 17. That is acceptable, since no value is claimed. Notation: see H-C06.

## 7. Findings

**H-C01 (MINOR). Stale status words in the frozen essential lemmas.**
- Location: theory/H01-exact-sum.md:40 ("Overall status: OPEN during development / not yet adopted"); H04-smooth-quadrature.md:53-54 ("distinct mathematical review has not yet occurred"); H05-digamma-centering.md:7, 74-77, 283-288 ("full corner expansion remains a separate OPEN target").
- Reason: the PROVED parent depends on H01, which declares itself OPEN. WORKFLOW says to "Correct prose with a dated addendum in place", and audit reports pin prose by SHA, so freezing old status words is not required.
- Impact: a reader following the dependency chain meets an OPEN status on the essential lemma. The mathematics is unaffected.
- Fix: append dated status addenda to H01, H04 and H05. Each should give the current status (PROVED supporting result) and link the accepting reviews with their hashes and this audit. Leave the proof text unchanged.

**H-C02 (MINOR). The exact reduction routes through an OPEN-status file, and PD-T226 is missing from H's dependencies.**
- Location: H-sharp-corner-expansion.md:53-57, and H01 §1. They cite F03 and PD-T159, but the signed periodic row = n (PD-T226) and the k=0 row = n^2 are also used. The main review uses PD-T226 explicitly.
- Impact: provenance only. The identity is correct (section 1, [D,E]).
- Fix: add PD-T226 to H's dependencies. Better, put the paper's self-contained derivation (corner-unified.tex:83-107) into H01 §1 or H-sharp, so that the PROVED chain does not rest on prose inside F03, whose overall status is OPEN.

**H-C03 (MINOR). Swapped coefficients in the |W''| majorant.**
- Location: H04-smooth-quadrature.md:129.
- Reason: (t^2/(4k^2 - t^2))'' = 8k^2(4k^2 + 3t^2)/(4k^2 - t^2)^3 (sympy, minor_checks.out). The majorant is therefore (8/pi)[(16/27) Sum k^-2 + (4/9) Sum k^-4], not (8/pi)[(4/9) Sum k^-2 + (16/27) Sum k^-4].
- Impact: none on conclusions. With Sum k^-2 <= 2, Sum k^-4 <= 4/3 and pi > 3 the corrected bound is <= 4.74 < 5, and numerically sup|W''| is about pi. So (9), (15), (19) and 17/n^2 stand.
- Fix: swap the two coefficients and add the crude bound used for Sum k^-2.

**H-C04 (NOTE). Hash provenance of the canonical file.**
- The integration acceptance pins H-sharp at e3d40294…. The committed (and only) Git version, commit 20d78a4, has hash b31aae94….
- The change is described as the permitted status/adoption update (H-sharp:175-180) and is not diffable in Git.
- I read the committed text in full. Its statement, proof and dependencies agree with the accepted H01/H04/H05 hashes, which match exactly.
- Optional fix: record the committed hash next to the accepted one in the LOG or summary.

**H-C05 (NOTE). No independent computation existed before this audit.**
- H-sharp:72 and campaign-H-summary say no computation ran in Campaign H. Section 4 is now an independent MEASURED corroboration at the claimed scale.
- Fix: link it as corroboration only, not as a premise.

**H-C06 (EDITORIAL). Notation collisions in paper Section 3.**
- d (a constant, eq:main-constants) vs d_r (weights, line 114) vs d_0 (line 321).
- D_n (diamond kernel, line 26) vs D_{m,r} (line 75).
- S, T (angles, line 28) vs T_{n,r} (line 64) and S_e, S_u.
- F_r (line 87), F (line 322), F_B (line 402).
- Q (the square, preliminaries) vs Q_M and Q_{m,r} (line 326).
- Impact: readability only.
- Fix: rename, for example a calligraphic kernel, delta_r for the weights, and sigma/tau for the angles.

**H-C07 (EDITORIAL). Missing spaces in the H files.**
- Examples: "at most17/n^2" (H-sharp:65), "factor1/m" (:88), "up to20Hrounds" (:168), "Astrahigh", "Solxhigh", "PAPERONLY", "bigO" (H-sharp and campaign-H-summary).
- Fix: typography only.

**H-C08 (NOTE). The remainder order looks sharp.**
- The near-constant per-doubling change in N^2 R (section 4) indicates a genuine log N/N^2 term. "O(log N/N^2)" therefore probably cannot be improved to O(N^-2). This is MEASURED, not proved.
- The theory correctly claims no next coefficient.

## 8. Proof ideas and simplifications

1. **Cardinal form.** |L| = w cot q |cot(q+p) + cot(q-p)|, together with Sum cot(z + l pi/n) = n cot(nz) evaluated at nq + pi r/2 (= tan q mod pi), gives the whole reduction (3) in about 10 lines from the kernel. This is a one-paragraph replacement for the F03/PD-T226/PD-T159 citation chain (H-C02).
2. **H04 via offset Euler-Maclaurin.** B is analytic within distance 1 of [0,1], and w·I and W·(B + 1/pi) are analytic. So 4V/(nm) has a full asymptotic expansion in powers of 1/n with no logarithms. All log N/N^k terms come from the harmonic part. The same argument with |B^(K)| <= (K!/pi)·2·(4/3)^{K+1}·zeta(K+1) gives a rigorous truncation bound. Combined with the exact digamma part, that would make an O(nK) **certified** evaluator of Lambda_c (an enclosure, not a closed form). corner.py is the uncertified prototype.
3. **Explicit constant.** Every H01 constant can be made explicit, as H04 (17) and H05 (257/216) already are. An explicit C turns H into E_n(0) = [a^2(log N + d) - 1]/N + O(log N/N^2) with an explicit onset. That would settle F03's sign target (T) beyond an explicit n0, and could lower the analytic argmax onset.
4. **Next term.** Navot-type Euler-Maclaurin for the endpoint log singularities of R, together with the next term of Sum log r/r and of A(m - 1/2)^2, would give the log N/N^2 coefficient that section 4 suggests is nonzero.

## 9. Commands, CPU and exit codes [E]

Environment: Python 3.13.18; mpmath 1.3.0; sympy 1.14.0; python-flint 0.9.0 (Arb), all from the existing $A/pylib. I ran no pip install; the packages were already present. gcc 13.3.0. Wall times come from bash `time`, since /usr/bin/time is absent. All runs exited with code 0.

| Command (cwd $A/h-corner-code, PYTHONPATH=$A/pylib) | User CPU (s) | Output |
|---|---|---|
| python3 brute.py 12 | 3.2 | brute.out |
| python3 corner.py direct 50 100 300 1000; python3 corner.py fast 50 100 300 1000 | 0.8; 2.8 | direct_check.out, fast_check.out |
| inline timing/K test at n=3000 (corner.lam_fast K=16,8,6,5; lam_direct) | about 26 | console |
| 4 parallel runs: python3 corner.py fast 204800 / 204801 / 102400 102401 / 6400 6401 12800 12801 25600 25601 51200 51201 | 101 + 102 + 101 + 95 | run_p1..p4.out |
| python3 corner.py direct $(seq 2 64) 100 101 200 201 400 401 800 801 1600 1601 3200 3201 | 13.7 | run_direct.out |
| python3 corner.py fast 20 21 40 41 100 101 … 3200 3201 | 15.4 | run_fast_small.out |
| python3 corner.py direct 6400 6401 | 40.1 | run_direct6400.out |
| python3 constants.py | 11.0 | constants.out |
| python3 constant_chain.py | 12.0 | constant_chain.out |
| gcc -O2 -o xcheck_float xcheck_float.c -lm; ./xcheck_float 2 3 4 12 20 21 40 41 100 101 1600 1601 | 0.9 | xcheck_float.out |
| PYTHONPATH=$A/pylib:$A/h-corner-code python3 sidechecks.py | 0.8 | sidechecks.out |
| python3 minor_checks.py | about 1 | minor_checks.out |
| python3 analyze.py run_direct.out run_fast_small.out run_p4.out run_p3.out run_p1.out run_p2.out | <0.1 | analyze.out |
| python3 origin_sign.py (same inputs) | <0.1 | origin_sign.out |

Total is about 530 CPU-s (8.8 CPU-min), within the 30-minute cap.

Script SHA-256 (prefixes): analyze.py 18f5b76d, brute.py 0eea004b, constants.py 89bc3348, corner.py d83d1f1f, minor_checks.py ebe3d795, sidechecks.py 23129244, xcheck_float.c 7341a282. The rest are in $A/h-corner-code.

## 10. Limits and items not re-derived

- **Read, not re-derived:**
  - PD-T269's quantitative kappa-limit proof §2-§3 and its series (3).
  - PD-T270's 1/(4n^2) constant.
  - PD-T271's Arb enclosure. I checked its value only by my own quadrature.
  - H02, H03 and H06's proofs, which are not premises. H03's three identities were only
    checked numerically.
  - F03's prose, apart from the identities I re-derived.
  - The paper sections other than §3 and preliminaries.
- **Constants:** not made explicit. In H01 (8)-(19) I verified that each constant exists and is uniform, not its size.
- **Euler-Maclaurin truncation:** in the fast evaluator it is validated empirically, not bounded. Numerical agreement over n <= 204801 is MEASURED and proves nothing beyond that range.
- **Out of scope:** no novelty, literature, G01/argmax or companion assessment.
