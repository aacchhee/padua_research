# Audit-03 component: F01–F10 analytic campaign (handoff 28, deferred scope of handoffs 13/15/16)

Auditor: Claude Opus 5.5, xhigh (independent mathematical auditor; subagent of the Claude audit orchestrator; no Git
state changed, no repository file edited). Date 2026-11-08. Repository head audited:
`f366535e1fa4ede566cb83bdc554220c12b307cf` on `codex/padua-argmax-bridge-20261105`; rules (AGENTS.md,
agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md) read at that head. Base/main and the `state/IDEAS.md` /
`literature/INDEX.md` blobs equal `f70a260e…` (the IDEAS SHA-256 `d7ec3aa6…` and INDEX `1f6f2ace…` match the F gate
baselines). Labels: [D] derived by hand by this auditor, [E] executed by this auditor, [I] inherited/read and not
independently re-derived. Code and raw outputs: `audit3/f-code/` (11 scripts, 11 `.out` files); Python 3.13.18, mpmath
1.3.0, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1. Total CPU used ≈ 2.5 min.

## 0. Verdict

**Mathematics: ACCEPT, with no BLOCKING finding.** Within the depth stated in §8, every F claim I reconstructed holds
at its stated quantifiers. The explicit constants I could extract were rechecked by interval arithmetic or exact
algebra, and some by direct numerical evaluation of the defined objects. All of them pass, most with a large margin.
The negative statements (F01 entropy, F02 mesh) are correctly limited to their named recipes. Later F results bear
this out: F04 and F06 succeed by exactly the alternative routes those negatives left open.

**Records: one MAJOR finding (F-01).** Campaign F is called "not premises, not used downstream". That is true for G01.
It is not true for the H sharp corner theorem, which explicitly depends on F03's exact identities, and those
identities sit inside a file whose status is OPEN. There are five further NOTE/MINOR items (F-02 to F-06).

**Onset: none follows.** No F result lowers the analytic onset 320. The useful-K≤100 target (F08) stays OPEN. None of
the F results should enter the journal paper.

## 1. Claim table (task 1)

Status words are those of the frozen prefix plus the appended root disposition. "Uses" means a premise of G01, H, the
paper or the companion. All five reviews are by Codex `gpt-6-astra` and are paper-only, with no scientific execution.
F04/F05 were reviewed at "ultra"; all other rounds at "high".

| ID | Claim (exact scope) | Status | Key deps (PD-T271?) | Review | Uses downstream |
|---|---|---|---|---|---|
| F01-seam-finite | δ_aE ≤ B_F, every n≥32, closed signed ρ≤5/4; B_F≤(3/2)B_old coefficientwise | PROVED | D05/D07/D35/D37/E08-origin; retained+outer supports (no 271) | F01 (accept) | none |
| F01-seam-retained / -outer | six retained rows; literal outer T ≤ ρ[(23/3)L+52]/n+β(17L+27)/n², ρ≤5/4 | PROVED | E04/E14/E02/D13 | F01 | via finite only |
| F01-seam-reanchor | generic: K(N)>0, F(N)>0 ⇒ Λ_c−S ≥ F(N) on 5/4≤ρ≤π for every n≥N | PROVED (implication) | E08, E13, C08, E06/E07 master **incl. PD-T271** | F01 | F07 |
| F01-em2-mesh | 0≤Γ_mesh≤ρ/24; \|δ_aRmesh−Γ_mesh/m\|≤(9/2)ρ(1+L)/m², ρ≤1 | PROVED | D13, D37 | F01 | none |
| F01-em2-entropy-obstruction (PD-N) | balanced α=β=c∈[1/64,1/4]: lim B_R′=−∞ at z0=π−2c ⇒ Var(B_R′)=∞ | PROVED neg.; certificate REJECTED: refuted | N1-14, E12 | F01 | none |
| F01-em2-operator-contract | exact operator identities only | OPEN (implementation) | D02/D07/E03/E12 | F01 | none |
| F02 (PD-N) | J=1,K=2, zero phase: Q_n/log n→16/(3π²); (g_v−Q_n)/log n→(8log2−16/3)/π²>0 ⇒ no uniform C/n (or bounded) loss vs unmodified full-band integral | PROVED neg.; reference REJECTED: failed | PD-T211/266/267, PD-T364/C01 | F02/F03 | none |
| F03 | target E_n(0)≥0 (n≥160), fallback ≥−ēbar/4; routine identities (3)–(8) | OPEN / DEFERRED | PD-T159/226/269/270 | F02/F03 | **identities are premises of H01/H04/H05/H06/H** (F-01) |
| F04 | entropy-cell (T), K=120000, every n≥32, closed 1/32≤ρ≤1 | PROVED (feasibility) | N1-14/C06, E12, E14/D07 | F04/F05 (ultra) | F09 |
| F05-background / -central / -crossover | β=0, α=ch, c∈[1/2,3/2]: \|D_n+(c/π²)h²L\|≤10000h², D_n≤70000ch/n | PROVED | E03, E05, E06, E08/E02, D16 | F04/F05 (one MINOR resolved) | none |
| F06 | distance-two projections Q>1/5−3r/20, n≥128, signed ρ≤r≤π/4 | PROVED | PD-T364/C01/C02/D29 | F06/F07 | none |
| F07 | Λ_c−S>283/2850>9/100, every n≥256, closed 5/4≤ρ≤π | PROVED | F01-reanchor (**PD-T271** via j>23/250), E15/E14 context | F06/F07 | F10 only; **not integrated** in source |
| F08 (target) | balanced box K≤100 | OPEN | F04 | F08–F10 | none |
| F08-coefficients / -kernel | two-sided entropy coefficient; diagonal 10e bound; exact \|x−r\|log\|x−r\| cell/hole moments | PROVED (supports) | N1-14, C06, F04 | F08–F10 (domain MINOR fixed) | none |
| F09 | T_n=[−(2p/π)log n+Γ_T]/(n+1)+R, \|R\|≤41000(1+log m)/m², n≥32, closed ρ≤1 | PROVED | F04 extended to ρ<1/32, E12/E14/E02, C04 | F08–F10 | none |
| F10 | conditional: A1 guard (s(B)≥2/5 at n≥256) gives T1 ⊂ T0 by subtree replacement; D_1⊂D_0, Q_1⊂Q_0 | PROVED (conditional) | F07, E15, D14, D19, D32/PD-T364 | F08–F10 | none; contract only |

Counts: 15 PROVED supports, 2 PD-N, and 3 OPEN target/interface records, 20 files in all. This agrees with the
campaign text. [E] All 42 review-frozen identities are exact byte prefixes of the current files: 20 theory, 11 idea
and 11 attempt files (`prefix_hash_check.out`). The only additions are the appended "Root disposition" sections. The
review-file SHA-256 values cited in those dispositions (39dcb7fb…, ccdb1d77…, 832ec81c…, 1e63875c…) match the files.

## 2. Independent reconstructions (task 2)

### 2a. F01 entropy obstruction and F01 reanchor

- **Entropy obstruction.** [D] With J=2[c0 log(c0/u)+b0 log(b0/u)], the derivative is ∂_sJ=log((u+s)/(u−s)). Also
  a·tan c=q, so s_R(2c)=u, and s_R′→1/(2cos c)>0 as ε rises to 2c. The subtracted terms I_R(0,·) and q log z are
  smooth at z0, and d=0.
  - [E] Direct tanh-sinh quadrature of the N1-02 integral I(C,D,v) confirms the same-sign formula, with deviation
    ≤2e−31 over 12 random (u,s,ε). It confirms the no-root identity R=2u log sin ε (≤4e−31). It confirms the
    root-regime J_s formula by finite differences (≤5e−12).
  - [E] Along the actual curve at c=1/64, 1/8 and 1/4, dJ/dε equals the predicted log((u+s)/(u−s))·s′ to 6 digits. It
    grows by ≈1.15 per decade of ε0−ε, i.e. log-divergent (`entropy_J_check.out`).
  - Quantifiers are correct. "Infinite variation on every interval with z0 in the interior" follows from
    unboundedness.
- **Reanchor geometry (§1).** [D] I re-derived (2)–(4):
  - 103/128≤cos(5/8)<13/16 and 1/2<sin(5/8)<3/5;
  - the three-branch cap p,q≤3/5+(3/2)√v;
  - \|p−q\|=2√(ce²−a²)≤3√v;
  - the Cauchy bound P≤2√(2u−u²), and its concave tangent at 3/16 (value √87/8<6/5, slope 26/√87<3).

  [E] Fraction checks of the Taylor rationals pass. A 251,001-point grid on the closed domain 5/4≤x+y≤π (axes, ρ=5/4 and
  ρ=π included) shows margins −0.048, −0.062 and −0.034 respectively (`f01_reanchor_geometry.out`).
- **Envelope mapping (§2).** [D] I transcribed the literal E08 CEphi pieces restated in E13 §2 (Dphi, Gphi, C6phi,
  Mphi, dW) and KD·P. Each √v and v increment maps exactly onto C_s and onto C_l=[9ℓ+12(5+2log 2m)]/(πm). Slope three
  replaces E13's slope four, with no leftover term. The Γ-tangent needs γ_b>0 and an intercept p0·C/(p0+C)>0, and both
  hold.

  [E] The literal CEphi+KD·P stays below C_b+P0·KD+C_s√v+(C_l+3KD)v on that grid for n ∈ {32, 33, 64, 128, 256, 257,
  10³, 10⁵}. The worst margin is −2.1e−4 at n=10⁵, and it is negative throughout.
- **Gap identity and scalar directions.** [D] I re-derived the gap inequality Λ_c−S ≥ G_b+Kv−A√v. The whole e0 is
  charged once. The weakening j*=23/250<j and t*=221/500>t0=2log2/π=0.44127 is in the safe direction. I re-derived the
  directions m·ℓ′=ε cot ε<1<ℓ, mΓ_b′<p0≤Γ_b and mγ_b′<1<γ_b, and the fact that R+=[71/n²−22/(45m)]_+ is nonincreasing.

  [E] A 60,000-point float scan on real n∈[32, 3.4e14] finds no violation of "G*,K* increasing; A* decreasing; F*
  increasing where K*>0".

### 2b. F03 origin identities

[D] I re-derived the following:
- the positive set j=−r+1,…,r−1 (r terms), from r−1<nr/m<r;
- P_r=w_rT_{n,r};
- the complete-sum identity Σ_{l<n}cot(π(l+a)/n)=n·cot(πa)=n·tan(v_r/2);
- the equivalence of (3) and (6);
- the two-pole split (7), with B(0)=1/π and B(1)=−1/π;
- the coarse 8M/π bound.

[E] The direct check is convention-free. I formed the Lagrange basis of total degree n at {(cos jπ/n, cos kπ/(n+1)):
j+k even} and evaluated the Lebesgue function at (−1,−1), for n=2…20, 25, 31, 40 and 48. It equals F03(3) to ≤1.7e−13
(cond V≈2.3–3). The identities (4), (5) and (7) hold to ≤2e−26, with Z_r≥1>0 for r<n and Z_n=0
(`f03_origin_check.out`).

[E] I also measured the target itself. E_n(0)=Λ_c−A_n²−κ is positive at n=32…4000 (12 values; n·E_n(0) rises from 1.03
to 2.97). It matches (4/π²)[(log N+c)²−(log n+c)²]−1/N, with N=n+1/2 and c=γ+log(8/π), up to a residual ≈1e−4·log n/n
(`f03_target_trend.out`).

### 2c. F08 entropy constants (kernel and coefficients)

- [D] The cell moment is A(θ)=\|θ\|−(1/4+θ²)=−(1/2−\|θ\|)². B is bracketed by P(y)=(y²/2)log y−y²/4, which is ≤0 on
  [0,1] with P(1)=−1/4. The exterior Peano monotonicity argument is valid. The exterior endpoint value is
  h²(1/4−log2/2). The hole coefficient is A0=(1−ζ)²−1/2. The exterior constants are 9/4 and 7/4, from
  ∫(ℓ−t)(3+log(1/t))dt=ℓ²[(1/2)log(1/ℓ)+9/4].
- [E] sympy confirms A and A0 symbolically. Quadrature confirms (1) and (4) exactly (≤4e−25 relative). The bounds (2),
  (3), (4) and (5) are reached at most 0.84, 0.66, 0.89 and 0.75 of their stated values. Sharpness holds: M/(h²\|log
  h\|)→1/4 and E(r=0)=P(ℓ) (`f08_kernel_check.out`).
- **Coefficients (1).** [D] Integrating the two branch derivatives gives \|v\|log\|v\|−(1+log 2u)\|v\|+2v_+log tan e*.

  [E] The quadrature residual divided by \|v\| decays linearly in \|v\| on both sides, at (u,e*)=(0.1,0.7) and
  (0.05,1.2). The diagonal 10e estimate (3) was checked only by hand (the 8e and 9e assembly); see §8.

### 2d. F09 outer EM2

- [D/E] The g endpoint ledger and A=(3/2−t)(p−q)_++(1/2+t)(p+q+d) were checked, as was the identity −A+q(2t−1)+2d=−2p
  in both cases p≥q and p<q. The Γ_T constant in (G) is reassembled from E[B] together with Alog(t)−Alog(1−t) and
  Dlog(t)+Dlog(1−t); the d coefficient is 4logπ+log 2π−6logπ=log(2/π). Both reductions pass in sympy.
- [E] The exact finite products Q_τ[log z] and Q_τ[log(π−z)] were checked for m=33…199 plus five larger m, at 21
  values of τ. Here max m²·\|error\| is 1.10 and 3.16, against the claimed ≤10. Binet/Stirling 0<r(x)<1/(12x) holds at
  the spot points.
- [E] The aggregate 41000(1+l)−[40000(1+l)+81l+443] equals 919l+557>0. The hole squares give Σℓ²/h²=4t²−4t+11≤11; the
  proof uses the safe 13 and 25.
- [D] The F04/F09 entropy budget (100 bad cells ×60, 50 good, 1125 holes; 7175π[1+log(24m/π)]<114800(1+log m)) and the
  truncated-variation tallies 90A+94 and 400A re-add correctly. The extension to ρ<1/32 uses only a≥49/64 and
  a−(p+q)/2≥17/64, together with the nonzero quartic (leading coefficient u²−4a²<0). Neither depends on a lower bound
  on ρ.

### 2e. F06, F07 and F10 (phase floor, far prune, prune contract)

- **F07.** [E] I evaluated every literal F01/F07 function at n=256 in 120-bit interval arithmetic
  (`f07_reanchor_check.out`). All 26 written rational bounds hold, including:
  - T>21/2, e0<143/750, KD<21/100, C_b<11/10, C_s<867/1000, C_l<1/3;
  - K*>14443/1500, G*>211/1250, A*<1563/1000 and F*>283/2850.

  The interval values are T=10.7766, e0=0.18487, C_b=1.05593, K*=9.9662, G*=0.29270, A*=1.48911 and
  **F*(256)=0.237074**. So the certified 283/2850≈0.0993 carries a margin of 2.4×. R+ at 256 is certified negative
  (−8.19e−4).
- **F06.** [D] I re-derived (7)–(8): (129/128)(7π/4)=903π/512<2π. Also:
  - (13): F(b)>11/32−1/324>1/3;
  - (16): ∫cot(b/2)=2log(1+√3)>2, with e<87/32<30/11<1+√3;
  - the loss sum 329/(60n)<11/(2n);
  - (20): 7/45+7r/180−4r²/45≥0.1298>37/375>11/256.

  [E] I evaluated the defined projected defect (3) directly in float64, using a collision-stable divided difference.
  That covers 400 samples at n∈{128, 129, 160, 255, 256}, both projections, both orientations, signed phases including
  the radius-π/4 axes; the minimum of Q−(1/5−3r/20) is +1.89. This floor is loose. The more searching check is of the
  proof's key step (14), d≥F(b)/t, over all 45,984 selected terms. There min d·t/F(b) is 1.178, and no case has F≤0.
- **F10 pruning predicate soundness.** [D] On every physical point of B∩T the guard s(B)=a_l+b_l≥2/5 gives a+b≥2/5.
  Hence ρ=π(a+b)≥2π/5>5/4, by π>157/50>25/8, and ρ≤π. F07 then gives λ≤S<Λ_c−283/2850, a **strict** inequality. This
  holds on the closed boundary s=2/5, at tangency s=1 and on every clipped patch, and no maximizer (ρ=0) can lie in a
  pruned patch.

  [E] The convention a=α/π is confirmed in source: `checker.py` line 33 reads 'abs(alpha/pi)+abs(beta/pi)>=1/2', and
  line 42 is the E15 guard.

  The premises needed are:
    - (i) F07, and through it F01-reanchor ← E08, E13, C08, E06/E07 and the computer-assisted PD-T271 (j>23/250);
    - (ii) PD-T364 per-chart λ≤S and the D32 physical cover;
    - (iii) the fixed-premise coupling (the same U-map, L, 13 grid keys, Mcoarse, split rule and traversal);
    - (iv) an old f leaf, so that GRID is retained.

  The structural induction (paths, not preorder IDs) is correct, and D_1⊂D_0 and Q_1⊂Q_0 follow from it. No strict
  saving is claimed, and correctly so.

### 2f. Secondary checks

- **F02, measured.** [E] The full defined Q_n at J=1, K=2 and zero phase, with every z and k summed, was computed for
  n=128…4096. Successive doubling differences go 0.3705→0.3743, against the predicted (16/(3π²))log2=0.37456. Adaptive
  quadrature of g_v(2π/(n+1)) gives doubling differences 0.3889→0.3893, against (8log2/π²)log2=0.38944. The gap
  g_v−Q_n grows by ≈0.0149 per doubling, against 0.01488 predicted (`f02_slope_check.out`). The discrete coefficient
  (11) is min(2/(1·π²), 2/(3π²))·2=4/(3π²) [D].
- **F01-seam-finite arithmetic.** [D] I re-added 8+9/5=49/5 and 10+22+1/2+52=169/2. The retained (2) gives
  (103/128)²=10609/16384 and 2a−P≥369/8192. The outer gives 6545/192<35 and 4943/96<52. Also 1251/2688 =
  1/3+13/168+7/128 = 1/2−31/896.

  The (3/2)B_old comparison is purely coefficientwise. It is a comparison of bounds and has no further content.
- **F05 assembly.** [D] The background coefficient −c²h²L/π² plus the central c(c−1)h²L/π² gives −ch²L/π². Then
  2000+200+1<10000, and nh/c≤2π<7 gives the 70000 corollary.

## 3. Scope of the negative statements (task 3)

Both PD-N records follow the registry pattern of PD-N084/085/086: a negative statement whose status is PROVED, plus a
separate candidate disposition (REJECTED: refuted or failed) with explicit assumptions.
- **F01** kills only the "finite Var(B_R′) for the merely log-subtracted residue" certificate. It explicitly does not
  refute an h²(1+log m)² quadrature error, an entropy subtraction, a singular-cell treatment or I06. F04 then proves
  exactly such a charged-cell remainder.
- **F02** kills only Q≥g_v−C/n against the unmodified exact full-band integral, on one admissible sequence. It
  explicitly disclaims any floor refutation, and Q_n itself grows. F06 then proves a direct finite distance-two floor.

Neither overreaches. See F-05 on the "refuted" versus "failed" wording.

## 4. Novelty-gate spot check (task 4)

Coverage. I scanned all 65 IDEAS headings. I read the PR17/PR19/T2–T4/PR25 argmax rows (lines 856–1020) and the scoped
obstruction table in full, and cross-checked PD-N079/132 in PROOF_STATUS. I did **not** read all 313 KB of IDEAS in
full; this is a coverage limit.

Term searches over IDEAS for Euler–Maclaurin/EM2, entropy, phase/fifth/projected floor, distance-two, prun*,
(re)anchor, crossing/singular cell, origin sign and BV-derivative return 0 hits. "Common-S/query set" returns 5 hits,
which belong to IDEA-320/454. The mechanisms therefore live only in this topic's local, not yet registered N/C/D/E
records, which the F idea files cite.

Every F idea verdict is "variant/continuation/quantitative application"; no novelty or priority is claimed. The cited
registry ancestors exist: IDEA-206/287/288/320/327/329/333/336/337/358/454/459, PD-N079/132 and
PD-T159/215/226/266/267/269/271/364. I found **no duplicate** and no claimed novelty to adjudicate. Two omissions are
noted under F-04.

## 5. Process: independent reconstruction for each component (task 5)

- Every F round has a distinct (Codex Astra) mathematical review, pinned by hash. Four of the five reviews share one
  reviewer instance; F04/F05 had a separate ultra reviewer. All five state "no scientific script, no numerical
  calculator, no execution".
- **All ten rounds were therefore accepted on paper reconstruction and arithmetic only.** That includes the rounds
  with explicit decisive constants: F01-reanchor/F07 (F*(256)), F06 (the floor), F09 (the log products and the 41000
  aggregate) and F08 (the kernel constants).
- For PAPER theorems this complies with WORKFLOW: no computation was performed, so none needed a rerun. This audit has
  now independently executed checks for F01, F02, F03, F06, F07, F08 and F09 (§2).
- Components with no independent reconstruction beyond the Codex review are listed in §8.
- No review gives a novelty verdict. The F01 reviewer's initial IDEAS/INDEX reads were truncated, a limit that
  reviewer disclosed. §4 is the only independent gate look. Chronology deviations remain canonical and unwaived; I did
  not re-adjudicate them:
  - F04 and F06: local idea/attempt records were created after the first algebra;
  - F03: disclosed incremental reading.

## 6. Integration and onset assessment (task 6)

- **Should any F result be integrated into the manuscripts?** No.
  - F03's identities already appear, re-derived, in `paper/sections/corner-unified.tex` (around lines 58–103).
  - F07/F10 could shrink certificate work for n=256..319 only. That would need a new source contract, a
    re-certification and a new audit, all for degrees that the accepted compact return already closes.
  - A companion remark explaining why plain Euler–Maclaurin/BV fails, using F01/F02 with F04/F06 as the remedies, is
    optional.
- **Is the far-outer region binding?** No. [E] The same F01 gate already closes at integer N=231 (float evaluation,
  not certified): F*(231)≈0.005, F*(240)≈0.093, F*(256)≈0.237.
- **Lower onset: nothing follows.**
  - The half-near barrier at 320 is untouched.
  - F04, F09 and F05 are feasibility constants (120000, 41000, 70000), two to three orders of magnitude too large.
  - F08's K≤100 target is OPEN. The missing piece is the joint off-diagonal entropy counterterm in \|α−β\|/h, matched
    to the p=q endpoint law.
  - F03's every-n origin sign is OPEN. [D] H only implies E_n(0)=[(4/π²)(log n+γ+log 8/π)−1]/n+O(log n/n²)>0 for
    sufficiently large n, which is non-effective. Removing the e0≈0.18 charge would require exactly this sign.
- Because G01 already covers every n≥2, a lower analytic onset now has value only for shortening the proof. It does
  not affect the theorem.

## 7. Findings

**F-01 — MAJOR (record structure and dependency disclosure; not a correctness defect).**
- **Location.** `theory/F03-origin-sign.md`. Its status is OPEN, and it says "routine origin specializations… neither
  complete the target nor give it PARTIAL status". Yet its eqs. (3), (4), (6), (7) and (8) are cited as dependencies
  in:
  - `theory/H01-exact-sum.md` (§"Assumptions, dependencies": "F03's exact partial-cotangent and two-pole
    decomposition"; §1 eq. (2));
  - `theory/H-sharp-corner-expansion.md` ("F03, routine exact partial-row/two-pole identities only");
  - `theory/H04-smooth-quadrature.md` (title and line 38: "V_n is exactly the residual in F03 (8)");
  - H05 and H06.

  `independent-checks-H-main.md` pins F03 at SHA-256 ddccb051…. `campaign-F-summary.md`, `G01` (around line 111),
  `results/padua-argmax-bridge-20261105.md` and the audit brief all describe F01–F10 as "separate supports", "not
  premises". That holds for G01 but is silent about H.
- **Reason.** WORKFLOW ("Split results…") counts a proved part as substantive if another result depends on it, and
  requires its own file, ID and PROVED status. A main theorem currently depends on content held in an OPEN target
  record.
- **Impact.** At registry application, H's dependency row would point at an OPEN F03 entry. The "F not used
  downstream" statements are inaccurate. The mathematics is sound: [D] the identities were re-derived, and [E] (3) and
  (6) match a convention-free direct Lebesgue computation to ≤1.7e−13 at 23 degrees.
- **Fix (developer).**
  - Split F03 §1–3 into a PROVED supporting record (provisionally "F03-origin-reduction"), with Split from/Split into
    lines and a crosswalk entry. Keep F03 (T) OPEN/DEFERRED.
  - Repoint the H01/H04/H05/H06/H dependency links.
  - Amend the summary/G01/results wording to "not premises of G01; F03's routine identities, re-derived in the paper's
    corner section, are premises of H".

**F-02 — NOTE (consequence not recorded).**
- **Location.** F03 statement (T) and its root disposition.
- **Reason.** The later PROVED H gives E_n(0)>0 for all sufficiently large n, non-effectively [D]. [E] Positivity is
  measured at 12 degrees from 32 to 4000, matching H's leading terms.
- **Impact.** This is context for anyone resuming I10/F03. It is not recorded anywhere.
- **Fix.** Optionally add a dated addendum ("eventually true by H; every n≥160 still OPEN"). This is a new corollary
  claim, so it is the developer's to write and review. It is not an auditor in-place fix.

**F-03 — MINOR (status-word hygiene).**
- **Location.** Every F theory frozen prefix: "PROVED developer PAPER theorem… distinct review/root adoption pending"
  and "Overall status: OPEN during development" (H01-style). Only the appended disposition records acceptance.
- **Impact.** A reader of the frozen prefix sees "pending".
- **Fix.** At PR preparation, registries should carry plain PROVED/OPEN/PD-N statuses with links to the review and
  disposition. No prose rewrite is needed; the prefixes are hash-pinned.

**F-04 — NOTE (gate and literature hygiene; no novelty claim is affected).**
- (a) F06/F02's registry-level ancestors (IDEA-327/328/356/458, PD-T215/219) are reachable only through the local
  C02/D29/N5 records. List them in the final IDEA entries.
- (b) F04, F08 and F09 use classical-type midpoint/Euler–Maclaurin analysis for x·log x and \|x−r\|·log\|x−r\|
  singularities. No source of this kind (e.g. Navot; Lyness–Ninham; Sidi) appears in `literature/INDEX.md`. If any of
  these results is ever put into a manuscript, cite such standard generalized Euler–Maclaurin literature and claim
  only the specific operator bounds.

**F-05 — NOTE (disposition wording).**
- **Location.** F01 uses "REJECTED: refuted" for its killed certificate, while F02 uses "REJECTED: failed" for its
  killed reference.
- **Reason.** Both are defensible. F01 negates an asserted premise, Var(B_R′)<∞; F02 shows that a mechanism misses its
  aim. They are consistent with PD-N084 and PD-N085.
- **Fix.** Optionally harmonize the wording at registry application.

**F-06 — NOTE (the margin is the argument's, not the gate's).**
- **Location.** F07 §6.
- **Reason.** The certified F*(256)>283/2850 uses coarse rational majorants; the interval value is 0.2371. The
  preregistered single-base gate is legitimate.
- **Fix.** Do not cite the float threshold 231 (§6) as a result without an exact certificate.

No other mathematical defect was found in any reconstructed step.

## 8. Not re-derived (honest depth)

Read in full:
- theory: F01-seam-reanchor, F01-seam-finite, F01-em2-entropy, F02, F03, F04, F05-crossover, F06, F07, all three F08
  files, F09 and F10;
- reviews: F01 (full); F06/F07 (full); F08–F10 (full);
- campaign: the F summary and campaign texts.

Read in part: F01-em2-mesh (statement and first proof step); F01-seam-retained/outer (spot rationals only);
F01-em2-operator-contract (status lines only); F05-background (statement only); the F02/F03 and F04/F05 reviews (header
and verdict lines); idea files (gate sections or grep); attempts (grep).

Inherited [I] and not independently checked:
- **E08.** The literal E08 CEphi formulas and their proof. I used them exactly as restated in E13 §2.
- **Global model.** E13 and C08; the E06/E07 global model master with j>23/250; and the PD-T271 computer-assisted
  constant. G01 also uses these.
- **Physical charts.** PD-T364 per-chart λ≤S and the D32 physical cover.
- **Profiles behind F04/F09.** The E12/E14/E02 decomposition of T, the endpoint values of B and P (H, ±q log π, w and
  Pc), and the profile identity (2)/(C).
- **Monotone-piece counts.** The count for the degree-≤6/8 critical polynomials in F04/F09 was checked only for
  consistency of the tallies.
- **F09 pole bounds.** The pole-profile bounds (J) and (P): \|df′\|<4, Var 16, 104 and 400/m².
- **F08.** The diagonal 10e estimate (3) was checked only by hand.
- **F05.** The proofs of the background (2000h²) and central (200h²) supports. M_∞ was not implemented, so F05 has no
  numerical check.
- **F01 seam.** The detailed proofs of the retained and outer supports.
- **F01-em2-mesh.** The predecessor bounds in its (4), and its remainder (9/2)ρ(1+L)/m², checked only in outline.
- **F01 contract.** The exact identities of the operator contract.
- **F06.** The equality of definition (3) with the PD-T364/C01 projected defect.
- **F10.** The source/runtime behaviour beyond checker.py lines 33–42; F10 is a contract, not an implementation.

Commands run (from `audit3/f-code`, PYTHONPATH=audit3/pylib where mpmath/sympy is needed): `prefix_hash_check.py <topic>`,
`f07_reanchor_check.py`, `f01_reanchor_geometry.py`, `entropy_J_check.py`, `f08_kernel_check.py`, `f09_ledger_check.py`,
`f03_origin_check.py`, `f03_target_trend.py`, `f06_floor_check.py`, `f06_selected_terms.py`, `f02_slope_check.py`.
Each run's output is in the matching `.out` file. All runs are MEASURED or verification evidence for paper theorems.
None is a proof premise.
