# Audit-04 / J2: elementary constants (J02), F03 identities, H04 majorant, response-03 dispositions

Auditor: Claude Opus 5.5 (subagent, instructed xhigh; effective effort not exposed). Role:
independent mathematical auditor, distinct from the Codex developers and the Astra/Sol reviewers.
No Git state change, no repository edit, no Syvert or remote access. Outputs only here and in `j02-code/`.
Labels: [D] own derivation, [E] executed by me, [I] inspection only.

## 1. Identities and coverage

- Branch `codex/padua-argmax-bridge-20261105`, head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`
  (handoff input `f4c6229…`; the diff f4c6229..70a50d7 touches only handoffs 29/30). Rules read at
  70a50d7: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoff 30, brief
  `claude-audit-brief-onset512-20261108.md`, audit-03.md, audit-03/h-corner.md (findings), response-03.md.
- TeX at head is byte-identical to the freeze 24a98db for every section I used (sha256 prefixes:
  paper comparison-unified 8ccd9883, corner-unified f8a2a115, introduction 95ad6bd5,
  localization-unified 14df874b, certification-unified 6fe37603; companion comparison-unified 78a5b1b9).
- Theory files audited (sha256 prefixes of committed bytes): J02 1683a4fd, J01 2df76efb (consumers
  only), F03-identities-support 32caa1fe, F03-origin-sign 39becf07, H04 47f54cf7, H-sharp 7c1b1cfd,
  H01 10ea378b, H05 cca45123, H06 646d3f66, G01 3fba640d; response-03 bb062966; checker
  `code/onset512_analytic/check.py` ff2859ee (= receipt pin), PREREGISTRATION 7c59d80a (= receipt pin).
- Read in full: J02, check.py, PREREGISTRATION, receipt, F03-identities-support, H-sharp, J01 (for
  consumers), response-03; the relevant parts of F03-origin-sign, H01/H04/H05/H06, G01, E06/E07/E08/E12
  (constant dependencies), PD-T269/PD-T271 statements, the J01/J02 and F03/H04 sections of
  independent-checks-onset512-response.md, paper Sections 1 (constants), 3.1, 4.1 (scalar lemma,
  model, `uc:master` and its proof, `uc:finite-bounds` statement, both gates), the corner-256 lemma,
  Section 5 far leaves and trust table, and the paired companion constant section.
- No novelty content: no new mechanism or priority judgement, so the full IDEAS read is omitted.

## 2. Executed checks [E]

All runs from scratch copies; cwd `$A/j02-code`; Python 3.13.18; mpmath 1.3.0, sympy 1.14.0 from
`$A/../audit3/pylib` (no install). Every script was read in full before running.

| Command | User CPU | Exit | Result |
|---|---:|---:|---|
| `python3 -I -B dev_copy/check.py` (byte copy, sha ff2859ee) | 0.20 s | 0 | Same receipt values as the developer and Astra runs: kappa_K3 [0.917166, 0.921489], Cstar [1.841232, 1.847940], gates unchanged |
| `python3 -I -B brackets.py` (own, sha 4638a5e5; 1st version failed 2 sanity checks, see below) | 0.42 s | 0 | 44/44 certified checks PASS |
| `python3 -B mp_cross.py` (sha 97b01ed2) | 4.24 s | 0 | ALL_PASS (cross-checks only) |
| `python3 -B f03_check.py` (sha 52a7b8b4) | 4.55 s | 0 | ALL_PASS, n = 2..12, 15, 16, 20, 21, 31, 32 |

Total about 10 CPU-s. Outputs: `brackets.out` (0dd8c139…), `mp_cross.out` (c79ce132…),
`f03_check.out` (b069a7db…), `dev_copy/dev_run.out` (bd22eb01…).
Failed attempt (preserved here): the first `brackets.py` run exited 1 because two sanity checks
(`0<a_p<=4^-p` and `|c_k|<2*4^-k`, p,k <= 14) were undecidable for p >= 12. At my zeta precision the
a_p intervals are about 5e-8 wide, while a_14 is about 4e-9. This was not a mathematical failure.
I restricted those two exact checks to p <= 10, k <= 12 and moved the full range (p,q,k <= 80) to the
mpmath cross-check. No consumed check changed.

**Own bracket computation (`brackets.py`).** It uses no floating point and no mpmath, and is
independent of check.py in its interval class and in every series. It uses integer dyadic endpoints on a
2^-320 grid with directed rounding, including division and a rounded-up isqrt.
- pi: Hutton's identity pi/4 = 2 atan(1/3) + atan(1/7), with the next-term remainder.
- log 2: sum 1/(k 2^k), with the tail 1/((K+1)2^K).
- Other logs: reduction to [2/3, 4/3), then 2atanh with a geometric tail.
- gamma: my own two-sided bound H_M - log M - 1/(2M) <= gamma <= H_M - log M - 1/(2(M+1)), M = 1000
  [D]. The lower side is the trapezoid convexity of 1/t. For the upper side, log((k+1)/k) >= 1/(k+1/2),
  so each increment is at most -1/((k+1)(2k+1)) < -(1/2)(1/(k+1) - 1/(k+2)).
- zeta(s): monotone integral test with m = 3000.
- kappa: the J02 series at K = 14, plus K = 3 for comparison.

Certified results:

| Quantity | Own enclosure | Consumed claim | Margin (mp) |
|---|---|---|---|
| kappa | [0.919710061, 0.919710176] (K=14) | > 9/10 | 0.0197 |
| C_* | [1.846160151, 1.846160878] | < 4629/2500 | 0.00544 |
| j = H0 + d0 - g0 | [0.143541748, 0.143542338] | > 23/250 | 0.0515 |
| t0 = 2 log2/pi | 0.4412712003… (width 2e-94) | 0 < t0 < 221/500 | 7.3e-4 |
| C_* - j/2 + sqrt(j^2/4 + t0^2) | [2.221458698, 2.221459767] | < 9/4 | 0.0285 |
| H0, d0, g0 | 0.3100023, 0.1699071, 0.3363675 | > 7/25, > 39/250, < 43/125 | |

Also certified:
- Every J02 (9) input: gamma, log2, log pi, k0, log(pi/2), pi and pi^2.
- Every exact rational step of J02 section 4 and paper `uc:scalar-constants`. These include 828/4925,
  9/20 - 828/4925 > 7/25, (80/197)(…) < 43/125, the j identity, 9/4 - 4629/2500 = 249/625 and (10) = 71/6250000.
- The paper's displayed 917166/10^6 < kappa < 921489/10^6 and C_* < 1847940/10^6. These hold
  strictly, so the outward six-place rounding is harmless.
- Other constants consumed in the same paper lemmas: 3/2 < gamma + log(8/pi) < 8/5; log(28/11) > 37/40
  via two atanh terms; log pi > 11/10; J_0 > 1/pi; lambda_0 < 1/(2pi); zeta(3) < 5/4;
  28 zeta(3) - 16 < 19; frak k < -1; k0 in (pi/2, 2); 4 I_4/pi^2 < 9/25.

**Cross-checks (`mp_cross.py`, MEASURED corroboration only).**
- kappa by direct tanh-sinh quadrature of the defining integral (odd sum in digamma closed form, itself
  checked against nsum) is 0.91971011838849253509951822579. The K = 80 series agrees to 1e-53.
- The actual K = 3 truncation error is 4.01e-4, against the analytic radius 1/480 = 2.08e-3. The tail
  bound (4) holds at K = 1, 2, 3, 5, 8.
- Majorants hold for all p, q, k <= 80: 0 < a_p <= 4^-p, -9^-q < b_q < 0, and |c_k| < 2·4^-k. In fact
  max_k |c_k| 4^k = c_0 = 1.0518.
- The two series identities hold at t = 0.37, 0.9, 0.999, and a_p = 2 sum (4r^2)^-p/(4r^2-1) holds.
- The introduction decimals kappa ≈ 0.919710118388, b ≈ 1.225522125742 and c ≈ 1.846160310424 are all
  correct to 12 places.
- sympy confirms the origin identity: `uc:origin-identity` holds if and only if C_* = B - g0 + 2H0,
  with C_* = c1^2 + kappa.

## 3. Reconstruction of J02 [D]

1. **Endpoint cancellation and the series.** The cotangent partial fraction is
   cot(pi t/2) = 2/(pi t) - (4t/pi) sum 1/(4r^2 - t^2). Expanding 1/(4r^2 - t^2) gives
   t^2 cot(pi t/2) = (2t/pi)[1 - 2 sum_m zeta(2m) t^2m / 4^m]. Dividing by 1 - t^2 gives exactly
   a_p = 1 - 2 sum_{r<=p} zeta(2r)/4^r. Telescoping, using 1 = 2 sum 1/(4r^2 - 1) and
   1/(4r^2 - 1) = sum_{m>=1} (4r^2)^-m, gives a_p = 2 sum_r (4r^2)^-p/(4r^2 - 1), so 0 < a_p <= 4^-p.
   In (1 - t^2) sum_{l odd} 1/(l(l^2 - t^2)) the l = 1 term is 1 exactly. The t^0 coefficient is
   (1 - 2^-3) zeta(3). For q >= 1 the coefficient is lambda(2q+3) - lambda(2q+1) with
   lambda(s) = (1 - 2^-s) zeta(s), so b_q = -sum_{l odd>=3} (l^2 - 1)/l^(2q+3).
   - The bound |b_q| < 9^-(q-1)(1/27 + 1/18) = (5/6) 9^-q holds.
   - zeta(3) < 1 + 1/8 + 1/8 = 5/4, so b_0 < 35/32 < 10/9.
   - |c_k| < 4^-k (10/9 + 4/5) = (86/45) 4^-k < 2·4^-k.
   - Integrating (2t/pi) t^2k termwise gives kappa = (8/pi^2) sum c_k/(k+1).
   - The tail is (8/pi^2)·2·(4^-K/3)/(K+2) < 8/(3(K+2)4^(K+1)), equal to 1/480 at K = 3.
   - Uniform absolute convergence on the closed [0,1] justifies the Cauchy product and the termwise
     integral. This is consistent with PD-T269 (1) and (3).
2. **Brackets.**
   - Machin: tan 4a = 120/119 and (120·239 - 119)/(119·239 + 120) = 28561/28561. The angle lies in
     (0, 4/5) and pi > 8/3 > 8/5, so the angle is pi/4.
   - The atanh log series and its tail 2x^(2J+1)/((2J+1)(1-x^2)) are correct.
   - gamma: the sequences H_M - log(M+1) increase and H_M - log(M+1/2) decrease, as J02 states.
   - zeta: trapezoid convexity on [10, inf) gives the lower bound and midpoint convexity on
     [k-1/2, k+1/2] gives the upper bound. Even and odd zeta values are treated alike.
   - The interval rules in check.py are correct: floor/ceil on the 2^-128 grid, four-product
     multiplication, sign-checked reciprocal, and lower log at lo and upper at hi.
   - check.py takes the zeta brackets for exactly s = 2,4,6 (a_1..a_3) and s = 3,5,7,9 (b_0..b_3), as
     displayed in the paper.
3. **Section 4 chain.** All directions are correct.
   - C0 > 391/100 and C0 - 7/2 > 41/100, so d0 > 39/250, using pi^2 < 10.
   - H0 > 9/20 - 828/4925 = 7/25 + 37/19700, using k0 > 0, log(pi/2) > 0 and pi^2 > 197/20.
   - g0 < 43/125 - 7/24625, using log pi > log 2 > 0.
   - Then j > 23/250.
   - Since j > 0 and u >= (1 - cos x)/2: max_x [(j/2) cos x + t0 sin x] <= sqrt(j^2/4 + t0^2). The
     resulting bound decreases in j and increases in t0 and C_*. With delta > 249/625, identity (10)
     gives delta^2 + delta·j > t0^2, hence C_inf < 9/4.
   - No upper bound on H0 or j, no lower bound on C_*, and no kappa < 23/25 is used. The only upper
     bound on kappa is the proved K = 3 one, used solely inside C_*.

**Exactly which consumer uses which constant** [D, I]:

| Constant (direction) | Consumers in the current route |
|---|---|
| kappa > 9/10 | H0 > 7/25 through `uc:origin-identity`, then j |
| kappa < 0.921489 (proved, internal) | C_* < 4629/2500 only |
| C_* < 4629/2500 | C_inf < 9/4 only. C_* cancels from M_inf(phi) - M_inf(0) in both gates |
| j > j_* = 23/250 | Relative gate U = T - ebar + A_4 + j_* (drops rho J_W >= 0 and j - j_* >= 0 under -u). Absolute gate Theta = T + j_*, which gives G(512,1) > 1/2 and the far-192 leaves G(192,pi/2) > 3/100. Corner-256 delta_A, delta_D, with coefficient +q_h. C_inf bound |
| t0 < t_* = 221/500 (t0 > 0, sin x >= 0) | Absolute gate (t_* sin x, C = t_* + 2K_D, B = t_* cos h). C_inf bound. Not in the relative or regular loss (E_c absorbs it) |
| C_inf < 9/4 | M(n) in `uc:analytic-norm`, then M(256) < 26 inside corner-256 (tail and frozen corner branch 256..511) |
| H0 > 0 (from 7/25) | -(H_0 + v_*) z <= 0 in `uc:model-loss` / `uc:regular-loss` |

Every needed direction is a lower bound for kappa, j and H0 and an upper bound for t0, C_* and C_inf.

**Definition consistency.** kappa is defined identically in paper `eq:main-kappa` (introduction.tex:125),
companion introduction:282, J02 and PD-T269 (1), and H-sharp cites "the exact integral/series constant of
PD-T269". The series `uc:kappa-series` (paper :475, companion :1244) equals PD-T269 (3) and J02 (4).
c = c1^2 + kappa = C_* (H-sharp, eq:main-constants, J02). The origin identity in J02,
H0 = kappa/2 - (2k0/pi^2) log(pi/2), equals paper :460.

**Grep for retired premises.** Patterns: PD-T271, Arb, kappa<23/25, H0<, 1847/1000, 4383/2420, and lower
bounds on C_*. Scope: paper, companion and current records.
- Paper certification-unified.tex:431 and companion :1589 name Arb only as software for the
  certificate search, not as a constant premise. NOTE.
- J02:3, 33-34, 42, 248, 256, 288 are disclaimers.
- J01:253 says "no PD-T271 computation".
- J03:176 is the pinned certificate-metadata string `computer-assisted PD-T271`, explained as schema
  identity only.
- H-sharp:40-41 has "PD-T271 supplies its optional separately certified numerical enclosure". This is
  not a premise.
- **G01:75-77 has an unqualified current-tense retention statement.** See J2-04.
- results:49 and report.md:420/472 are historical sections.
- The frozen E06/E10-E15 records keep their historical PD-T271 strings, as intended.
- No manuscript hit uses kappa<23/25, an upper bound on H0, a lower bound on C_*, or the old decimals
  as a premise.

## 4. F03 identities support [D, E]

Derivation from the cardinal formula, independent of F03, with the notation of my derivation:
- L_xi(x) = w_xi [K_n(xi,x) - T_n(xi_1) T_n(x_1)] with the diamond kernel. At the corner, T_p(-1) = (-1)^p
  turns K into D_n(theta', phi') = sum_{|p|+|q|<=n} e^{i(p theta' + q phi')}, where
  theta' = J pi/n, phi' = K pi/m, J = n - j, K = m - k, and J + K is odd.
- With N = n + 1/2, D(x) = sin(Nx)/sin(x/2) and D(x+pi) = (-1)^n cos(Nx)/cos(x/2).
- cos(N theta') = sigma cos(theta'/2) and cos(N phi') = -sigma cos(phi'/2), with sigma = (-1)^J.
- The product-to-sum formulas give (1/2)[D(s)D(d) + D(s+pi)D(d+pi)]
  = -sigma (2 + cos theta' + cos phi')/(cos phi' - cos theta').
- Hence **L_xi(c) = 2 sigma w_xi F_K(theta')** with F_r(u) = (1 + cos v_r)/(cos u - cos v_r).
  This is valid for 1 <= K <= n, since coprimality excludes cos theta' = cos phi'.
- Row K = 0: R_0 = sum_{J odd mod 2n} csc^2(J pi/(2n)) = n^2, which gives n/m.
- Row K = m: F vanishes except at the opposite vertex (1,1). There the "coefficient one" correction
  gives |1 + 4 sum_t (-1)^t t - (-1)^n| = 2n with weight 1/(2nm), which gives 1/m.

This proves (3). (1) holds since r - 1 < nr/m < r. For (2), the full signed row
(w/2)·2n tan(v/2) equals n. (4) follows from cot A + cot B = sin(A+B)/(sin A sin B) and j = r - 1 - 2l.
(5) is the multiplication formula. For (6), Z_r = P_r - n with Z_{n-1} = 1 and Z_n = 0. (7) holds by
pole subtraction, with B(0) = 1/pi and B(1) = -1/pi. The coarse 8M/pi bound in section 3 is correct.
All of this matches paper corner-unified.tex:46-199. That proof is self-contained, so the manuscript
does not depend on F03 prose.

Executed corroboration (`f03_check.py`, mpmath 30 digits, n = 2..12, 15, 16, 20, 21, 31, 32):
- The cardinal property holds to 1e-30 for n <= 7.
- Lambda_c(2) = 3.
- The positive sets match exactly.
- The per-row correspondence holds: row k = m - r carries (2/(nm)) R_r, and the edge rows give n/m and 1/m.
- (2), (4), (5), (6), (7), (3) and H-sharp (3), Lambda_c = -1 + 2/m + Hcal_m + 4V_n/(nm), all hold
  with errors below 6e-27.
- Z_r > 0 for r < n.

**Status mapping.** H01:35/52/59, H04:38/66, H05:85, H06:31/46/65 and H-sharp:55-60 now cite
F03-identities-support with PD-T159/PD-T226. G01:166-170, campaign-F-summary:70-74 and results:14 are
corrected. The OPEN sign target (T) and the useful-lower target are a premise nowhere.
- H05:87 lists it explicitly as "not imported".
- The paper uses only E_n(0) > -ebar (`uc:origin-lower`, E08).
- No current record links F03-origin-sign as a dependency. The only links are in the brief, response,
  reviews, the support's "Split from" and ideas files.

## 5. H04 majorant (audit-03 H-C03) [D, E]

- sympy confirms f_k'' = 8k^2(4k^2 + 3t^2)/(4k^2 - t^2)^3 = 8k^2/(4k^2 - t^2)^2 + 32k^2 t^2/(4k^2 - t^2)^3,
  with f_k'' >= 0 and |W''| = (4/pi) sum f_k''.
- Bounding the two summands separately with 4k^2 - t^2 >= 3k^2 (k >= 1, t <= 1) gives 8/(9k^2) + 32/(27k^4).
  This is the **historical** order (8/pi)[(4/9)S2 + (16/27)S4]. It is valid.
- Bounding the combined numerator by 4k^2 + 3 gives 32/(27k^2) + 8/(9k^4), the **revised** order.
  It is also valid.
- revised - historical = (8/27)(k^2 - 1)/k^4 >= 0 termwise, so the revised bound is weaker. Exact-series
  values are 3.4949 (historical) and 3.7072 (revised), against the measured sup|W''| = pi (attained at
  t = 1, where W''(1) = -pi). The coarse bounds with S2 <= 2, S4 <= 4/3 and pi > 3 are 1088/243 and 128/27, both < 5.
- Downstream: ||F''|| <= 25 + 9 + 5/3 < 36 and ||G''|| <= 5(16/3) + 18 + 5 < 50 give R_F <= 12/m^2 and
  R_G <= 25/(3nm^2). (21) becomes (11/3)y^2 + (151/12)y < 65/4 < 17, so 17/n^2 stands.
- The audit-03 description of the old line as swapped was a false positive. Response-03's
  "FIXED/DISPUTED" is correct and preserves both pins.

## 6. Response-03 dispositions checked against the files [I, plus D where marked]

| IDs | Claimed | Verified |
|---|---|---|
| G-1 | FIXED, scoped (I25 route) | Present: G01 "Current direct-sum verification route" addendum. Section 5 states the direct-sum route, and table `cert:trust` names the analytic, IEEE, NumPy and Python premises. Historical D23/C02/N5/C06/D06/C11 are named in G01. The "root refreshes older G01 wording" part is only partly done; see J2-04 |
| F-01, H-C02 | FIXED | Present and correct [D, E]. The split is verbatim per the Astra pin. Header hygiene: J2-05 |
| H-C01 | FIXED | Dated addenda in H01:329, H04 and H05:304 |
| H-C03 | FIXED/DISPUTED | Correct; see section 5 |
| H-C04, H-C05, H-C07, H-C08 | DECISION | Consistent. H-C05's "corroboration not premise" wording is at F03-support:171-173. The H-C07 typos ("at most17/n^2", "factor1/m") remain, as decided |
| H-C06 | FIXED, scoped | Partly. D_n became calligraphic and S,T became u_±, but several collisions remain; see J2-08 |
| G-2 | FIXED | G01 dated correction, plus a native-finite-range header note added after 24a (prose only) |
| G-3 | FIXED | G01 floor-tier map present |
| G-4 | FIXED, scoped | G01:147-151 and the paper trust table present |
| G-5 | FIXED | True for both manuscripts: corner-256 and far-192 consume only `uc:master` constants (J02). G01:75 is stale (J2-04) |
| G-6 | FIXED, scoped | de Casteljau averaging stated in paper certification-unified.tex:71 |
| E-01..E-04 | FIXED | Code present: `--expect-plan`, MAX_TOTAL checked before read, alias size charged, fresh tree and key checks. Not rerun by me; see the operational sub-audit |
| E-05 | FIXED, wording | Preregistration:39-40 scopes PA1. The campaign summary does not mention PA1, contrary to the row text (J2-10, NOTE) |
| E-06 | FIXED, scoped | Consistent with replay276 and J03 |
| E-07 | FIXED | compact-return.md:117 |
| E-08, E-09 | DECISION | Consistent |
| E-10 | PENDING, custody | cold-storage.json is now 4,244 B and COLD_STORAGE.md 15,598 B, both below 16 KiB. Custody is still pending, as stated |
| F-03, F-04 | PENDING (registry, PR) | Consistent; nothing claimed |
| F-05, F-06 | DECISION | Consistent. "231" appears nowhere in the manuscripts, G01 or J01 |
| X-17 | FIXED | paper-positioning.md:119 |
| P-03 (related to (a)) | FIXED | Arb premise gone; kappa<23/25 and the H0 upper bound deleted from both texts |
| P-02 (related to (a)) | FIXED | Abstracts state computer assistance; kappa≈ is illustrative (J2-09) |
| C2A-07 (related to (a)) | FIXED | Companion :1268-1290 gives the bracket rules and the gamma and zeta reasons |

No claimed fix is absent. None conflicts with a pinned historical record: old pins are kept at b45e29f
and in audit-03. Provenance note J2-07 applies.

## 7. Findings

- **J2-01 MINOR (paper; companion; J02 list).** log pi > 11/10 is consumed but not stated in the paper.
  - Location: paper comparison-unified.tex:123 (J_0 = 2(log pi - gamma)/pi > 1/pi) and :149
    ("frak k + Q < 0"). Both need log pi - gamma > 1/2. The paper gives no reason, and its elementary
    input list (:521-523) has only log pi < 23/20.
  - The companion states "log pi > 11/10" at :454 but omits it from its own list (:1295-1297).
    E07:43 uses it.
  - J02 (9) calls its list "the only consumed checks". That is true for J02's own outputs, but the
    manuscript lemma consumes this bracket too.
  - Impact: none on truth (log pi = 1.14473; certified in `brackets.py`). It is a stated-premise
    completeness gap.
  - Fix: add "log pi > 11/10" to both input lists and cite it at :123 and :149. Optionally note in J02
    that the scalar-maximum lemma additionally consumes it.
- **J2-02 EDITORIAL with a concrete restructuring.** The elementary brackets are consumed before they
  are proved.
  - gamma > 23/40, log 2 > 69/100 and log pi < 23/20 are used at :160-163. The gamma bounds and pi < 22/7
    are used at :423-426, and pi^2 > 197/20 at :600. All are proved only at :494-527, inside the proof of
    `uc:master`, with no forward pointer. The companion has the same ordering.
  - Improvement: move `ul:log-series`, the Machin/atan, zeta and gamma brackets and one complete
    consumed list (including J2-01) into a short "Elementary constants" lemma at the start of §4.1.
    Cite it from the scalar maximum, `uc:master`, both gates and corner-256. This removes every forward
    use and makes the J02 dependency visible at one point.
- **J2-03 MINOR (both texts, disclosure).** The machine evaluation of the base comparisons is not
  disclosed.
  - The J01 base values and the J02 K = 3 outputs were evaluated by the exact-rational script
    `code/onset512_analytic/check.py` (Python Fraction). They are not practical by hand: the 10-term
    zeta, 48-term log and 40-term atan rationals are large.
  - Neither text says so. The introduction calls n >= 512 "analytic estimates", and `cert:trust` lists
    only "The stated rational checks".
  - Fix: one sentence in §4.1 and the gate proofs, plus the `cert:trust` row. Name the script path, its
    Python integer/Fraction trust, and the receipt.
- **J2-04 MINOR (G01 record; eligible for an in-place MINOR fix by the root auditor).** G01:75-77 says,
  unqualified, "PD-T271 remains a named computer-assisted dependency of the analytic constants/branches".
  The onset-512 addendum then says "the same … native evaluator premises listed above". Only the later
  addendum (:152-155) and J03:176-180 say J02 replaces PD-T271.
  - Fix: add a dated line at :75: "historical onset-320/native route; for the onset-512/I25 route J02
    supplies j>23/250, t0<221/500 and C_inf<9/4 to the tail, corner-256 and far-192, and PD-T271 is not
    a premise".
- **J2-05 MINOR (record hygiene; eligible in-place fix).** F03-origin-sign.md:6 still reads "Split from:
  none. Split into: none.", contradicting its own dated correction (:225-231). WORKFLOW requires
  Split into in the theory file.
  - Fix: append "(superseded 2026-11-08: split into F03-identities-support; see the dated correction)".
    Optionally mark :35-38 "routine … neither complete the target" as superseded in the same way.
- **J2-06 NOTE (H-C03).** I confirm that both majorants are valid and that the historical one is
  tighter. Recommendation for the response ledger: record H-C03 as "audit characterization withdrawn
  (audit-04); canonical order adopted, harmless". In H04, the audit-03 H-C01 addendum still says the
  display "is swapped … not applied here". A one-line pointer to the following majorant-alignment
  addendum would avoid confusion. EDITORIAL.
- **J2-07 NOTE (provenance).** Some reviewed bytes cannot be recovered from Git.
  - The distinct-review pins for J02 (d4fc185a) and J01 (a74be3cf) are exact prefixes of the committed
    files (lines 1-279 and 1-315). The post-review change is a pure appended status section, which I
    verified.
  - The pins for F03-identities-support (fbdeed2e) and H04 (cd8a9462) are not prefixes and were never
    committed. Their post-review edits sit inside the text and cannot be reconstructed from Git.
  - My audit covers the committed bytes listed in §1, so nothing rests on that gap.
  - Optional: have reviewers pin committed blobs, or log that the edits are status-link only.
- **J2-08 EDITORIAL (H-C06 only partly fixed).** Paper Section 3 still overloads several symbols:
  - d (eq:main-constants), d_r (corner-unified.tex:206) and d_0 (:421);
  - F_r (:166), F (:422) and F_B (:502);
  - Q (preliminaries) and Q_{m,r} (:425);
  - the node B (:52, preliminaries:37) and the function B(x) (:120).
  - In `uc:master`, p and q are sin x and sin y (comparison :14, used in the same lemma) and are reused
    as the summation indices of the a_p, b_q and c_k series (:468-472). Rename the indices, for
    example to i and l.
- **J2-09 EDITORIAL.** After PD-T271's removal, the 12-digit kappa, b and c in the abstract and
  introduction (paper main.tex:33, introduction.tex:164-165) have no source in the paper. They are
  correct (§2). Add "(numerical values; not used in any proof)" or cite their computation.
- **J2-10 NOTE.** In response-03, row E-05 says the "campaign summary" scopes PA1. Only the
  preregistration does (:39-40). This is a wording slip.
- **J2-11 NOTE.** The coarse J02 chain is exact but tight. The squared C_inf gap is 71/6250000. With
  every coarse threshold at its limit, 9/4 minus the bound is 1.28e-5, against a true margin of 0.0285.
  The t0 margin is 7.3e-4. No action needed. The derived H0, d0 and g0 bounds are text cross-multiplications
  that check.py does not assert. I verified them exactly.

No BLOCKING or MAJOR finding. J2-01 to J2-05 are wording or record level. Each leaves the stated
inequalities, their proofs and every consumer unchanged.

## 8. Verdict

**J02: ACCEPTED (PROVED at its stated scope).**
- I reconstructed the endpoint cancellation, the uniform series, the coefficient signs and the
  convolution, the analytic K = 3 radius 1/480, and every elementary bracket for pi, log 2, log pi,
  gamma, zeta(2,4,6) and zeta(3,5,7,9).
- My own independent dyadic computation certifies kappa > 9/10, j > 23/250, 0 < t0 < 221/500,
  C_* < 4629/2500 and C_inf < 9/4, each with the correct consumer direction.
- No retired PD-T271 or Arb premise, kappa < 23/25, or upper bound on H0 is consumed by the current
  paper, the companion or J01/J02.

**F03-identities-support: ACCEPTED (PROVED).** I re-derived it from the cardinal formula and confirmed it
numerically at 17 degrees, both parities. It is correctly split, and the OPEN F03 target is not a
premise anywhere.

**H04 correction: ACCEPTED.** Both coefficient orders are valid, the revised one is weaker, and |W''| < 5
and 17/n^2 are unchanged.

**Response-03 dispositions in scope: ACCEPTED**, with J2-04, J2-05, J2-08 and J2-10 as corrections to
the stated status.

## 9. Not re-derived or not tested

- J01's all-real-n monotonicity and gate arithmetic. I used only J01's consumers of the constants;
  J01 itself is the sibling audit's scope.
- The E06/E07 scalar maximum and `uc:master`'s inequality C_inf - C_* <= -j u + t0 p, beyond the
  term bookkeeping in §3. I read it and checked its constant inputs only.
- The finite-error comparison `uc:finite-bounds` and its claimed non-circularity with
  `uc:origin-identity`. Inspection only.
- PD-T269 §2-3, which identifies the limit with kappa, and PD-T270.
- The corner-256 and far-192 numeric gates. Their constant inputs were checked; their arithmetic was not.
- E-01..E-04 verifier reruns, I25 and manuscript-wide pedagogy, all assigned elsewhere.
- No novelty, literature or priority judgement.
