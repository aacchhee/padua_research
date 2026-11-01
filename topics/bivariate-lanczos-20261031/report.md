# Report — Lanczos in two commuting variables (bivariate-lanczos-20261031)

Orchestrator: Claude (configured `claude-opus-5-5`). Rules `d36722823441dc40c6e19d69a174459348dd309c`. Date 2026-11-01. **Every result below is a developer result; none is accepted.** Rank 4's span drift deserves AC's attention first: if the identification with published multivariate V+A holds, full reorthogonalization keeps orthogonality at 1e-15 yet computes a basis of a space ~1e-3 away from the graded polynomial space on rotated squares. Statuses are those in the theory files after the independent Claude reconstructions listed; the Codex (`gpt-6-astra`) audit is pending. No novelty is claimed: each survivor names its closest prior work and the separation that remains after the documented prior-art checks. Floating-point experiments are MEASURED only.

## 0. What the campaign asked and what it found

The object is the truncated bivariate Lanczos/Stieltjes window recurrence (Weisfeld 1959; Bartels–Jezioranski 1985; Huhtanen–Larsen 2002) for X = diag(x), Y = diag(y), one start vector, total-degree graded orthonormal basis. Huhtanen–Larsen SIMAX 2002 p. 1088 *observed* (not conjectured — Step 0 correction) that loss of orthogonality "appears closely connected" to Ritz convergence of the complex section N_k.

1. **Loss of orthogonality is not Ritz-governed in general** (L1). On non-product supports (rotated squares, disk, triangle, L-shape, annulus, Gaussian cloud, exp(8xy)-weighted square) it grows (log-loss convex in n) from degree ≈ 8–12 before any Ritz convergence, scales with u, and depends on the *selection rule* (which multiplication generates each new vector) by 10³–10⁸; no rule is best everywhere. The bare geometry dependence is prior art (Zaccaron 2014); the triangular "one relation per polynomial" framing is prior art (Barrio–Peña–Sauer 2010).
2. **Where Paige-type theory does transfer** (L1, L4, L2): exact local relations, a growing-block Paige identity, an exact 2D ω-recurrence, an L4 obstruction (not a band Krylov sequence of one commuting operator with fixed starts), and a semi-orthogonality theorem for the x-part of the sections — but a proved obstruction for the y-part (the commutator residual is not reset by reorthogonalization).
3. **Greenbaum-type backward interpretation** (L3), in the exact-representation reading: δ = 0 for overdetermined nodes; ≥ √ε necessary for square (interpolatory) sets; √ε attained for small n; and an **obstruction for every Padua degree n ≥ 3** (no representing measure within δ₀(n) of the nodes for any ε > 0), by explicit nonnegative certificates with double zeros and positive-definite Hessians at all Padua nodes. The loss-of-orthogonality ("Greenbaum") reading is OPEN.
4. **Givens updating** (L5, side note): Givens grows faster than HL with M (MEASURED), the 'largest' redundant-pivot rule is unsafe, and the suspected prefix-unisolvence mechanism is refuted.

## 1. Ranked survivors with development briefs

Ranking criterion: strength of the established statement × independence of verification × separation from prior art × value to AC's programme.

### Rank 1 — Padua backward obstruction for all n ≥ 3 (L3: PD-N?…-N301, PD-T?…-313, PD-N?…-N303)

- Statement: for Padua points of degree n ≥ 3 with cubature weights (square case M = N_n), there is δ₀(n) > 0 such that for every ε > 0 some consistent ε-perturbation of the exact degree-n sections has **no** positive representing measure supported within δ₀(n) of the nodes. Certificates: an explicit rational p* ∈ Π₇ for n = 3; for n ≥ 4, P_n = 9(g₁² − ½g₀g₂) + (g₂² − g₁g₃), g_m = T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y), with double zeros and PD Hessians at all nodes.
- Status: N301 PROVED (computer-assisted: exact certificate, independent exact rerun by reconstruction 01, rational interval radius); 313 PROVED, N303 PROVED under Padua unisolvence (LITERATURE dependency); independent exact checker n = 4..16 and hand-checked expansions (reconstruction 02). Rigorous δ₀(n) from 5.6e-4 (n = 4) to 6.5e-8 (n = 12) (reviewer computation).
- Prior art: no matching certificate found; the mechanism (PD-Hessian double zeros of a nonnegative annihilating polynomial obstruct perturbation) is in Di Dio–Schmüdgen and Blekherman 2012 Lemma 3.1.
- Brief: asymptotics of δ₀(n); independent rerun of the δ₀ computation; write as a short note together with Rank 2 (the rate theorem gives the framework, Rank 1 the striking instance: interpolatory Padua recurrences have no Greenbaum-type backward model).

### Rank 2 — Rate theorem and moment-cone reduction (L3: -302, -303, -N302, -304, -301, -305, -306, -310)

- Statement: perturbed consistent degree-n sections are exactly representable within δ ⟺ the perturbed functional on Π_{2n+1} lies in the moment cone over the δ-fattened nodes (inradius criterion r(δ) ≥ ε, c = 1); trichotomy: interior → δ = 0; no nonnegative annihilator → δ ≍ ε; annihilators exist → δ ≳ √ε (≍ √ε under condition (H)); PD-Hessian annihilator → obstruction. Square case: δ = O(ε) impossible (N302). √ε attained for n = 1, Padua n = 2, equispaced checkerboards n ≤ 7. Truncated Favard correspondence (301).
- Status: PROVED (developer), confirmed by reconstructions 01–02 with corrections applied; 304(c) isomorphism part MEASURED.
- Prior art: Tchakaloff; Di Dio–Schmüdgen Prop. 27, Thm 40, Lemma 37, Prop. 43; Blekherman 2012; Xu Trans. AMS 1994 Thm 4.2; Degani–Schiff–Tannor 2005 Thms 9–11. Not yet read and possibly relevant to 301: Delgado–Geronimo–Iliev–Marcellán SIMAX 2006; Cichoń–Stochel–Szafraniec JAT 2005 (pending-reference).
- Brief: explicit constants; degenerate PSD-singular case; prove S₁ = quadratic-generator family; read the two pending sources before any priority wording.

### Rank 3 — Loss of orthogonality: non-Ritz amplification and selection dependence (L1: PD-N?…-101(a), -105, -106; PD-T?…-108, -109, -113, -104, -106)

- Statement: on the listed non-product sets the loss exceeds u/ρ for every single, joint, oblique and N_k Ritz residual by 10²–10¹⁴ (frozen kill test: K2 fires; K1 inconclusive at u = 2⁻⁵³); it is an a-priori property of the exact recurrence for a fixed selection rule; changing the selection rule changes it by 10³–10⁸ (no rule best everywhere); support shape does not classify the regime. Exact rational certificate (dev rule): propagator growth G(12) ≥ 10⁶ G(6) on the triangle grid T_24 vs ≤ 10² on the square grid Q_24.
- Status: N101(a), N105, N106 MEASURED (independently rerun); 113 PROVED (finite exact certificate; independent two-way exact rerun); 104, 106, 108 PROVED and confirmed.
- Prior art: Zaccaron 2014 (geometry dependence observed); BPS 2010 (one-variable recurrence, Remark 9 selection matters, triangular-substitution bounds); Liu–Narayan 2023 (block Stieltjes). Separation: discrete Lanczos with window truncation, the quantified and set-dependent selection effect, the exact certificate, the node-row/ω link to orthogonality loss.
- Brief: a selection principle (minimise max_z‖L*(z)⁻¹‖) — the central open question handed to L2; all-n lower bound on the triangle family; M = 10⁵–10⁶ runs.

### Rank 4 — Section accuracy under reorthogonalization: x-part theorem, y-part obstruction (L2: PD-T?…-201, -202, -205; PD-N?…-201)

- Statement: under semi-orthogonality plus local orthogonality (two-pass window), the x-multiplication section is accurate to O(u) (201); the commutator residual of the injected y-part follows the Gram recursion with clamped columns and is not reset by reorthogonalization, giving a reference-free lower bound θ ≥ δ_J/(2‖J‖) on the distance of the computed spaces from S_n (202); coupled residuals for general selections (205). MEASURED: even CGS2 against all previous vectors leaves y-section errors up to 1.3e-2 and spans drifting from S_n (PD-N?…-201).
- Status: 201, 202 PROVED and confirmed by L2 reconstruction 01 (35 stress instances for 201; exact rational and 80-digit checks for 202, whose bound controls max_{s≤n} θ_s); 205 PROVED only under condition (C) + acyclicity after a high finding ((C) ⇒ acyclic OPEN, checked n ≤ 5, proved for BJ; the adaptive rule fails (C)). PD-N 201 MEASURED and **confirmed with independent well-conditioned references** (κ ≤ 7.8e2): own BJ + CGS2-against-all (loss 4e-16) drifts 3.6e-3 (rotπ/4, n = 24) and 1.3e-2 (triangle, n = 20); 7.7e-6 in long double, so the drift scales with working precision; it does not decay with M up to 1e5. The developer's original kill criterion was added after a smoke test (disclosed).
- Prior art (reviews/L2-prior-art-01.md; all four mechanisms partially known, nothing read contradicts or subsumes the drift): Zhu–Nakatsukasa 2026, Brubeck–Nakatsukasa–Trefethen 2021 and Hokanson 2020 prove nothing about the computed span or Hessenberg matrices in 2D (ZN's rounding content is the CGS2 orthogonality bound feeding a fit bound; ZN §5.2's 'unaffected by ill-conditioning' rests on 1D basis comparisons and 2D fit errors); Zhang–Su–Li 2024 is a 1D fitted-value bound. Span accuracy and fit accuracy can differ — the drift finding concerns the span. 1D analogue: Krylov backward stability plus subspace conditioning (Drkošová et al. 1995; Carpraux–Godunov–Kuznetsov 1996; Kuznetsov 1997; Paige 2010 — not read). Simon 1984 / Jia–Li 2021 templates for 201. Hokanson's 'smallest k' rule appears to match the dev (BJ) selection (to verify), so the CGS2 + dev runs would be Hokanson-type V+A. Not read and could limit novelty: ZN Appendix B, Simon LAA 61 Thm 5, Kreuzer–Poulisse–Robbiano 2009, Stetter 2004, Braconier–Langlois–Rioual 2000.
- Brief: online criterion to switch from one relation to two; explain PRO-2D-J's last-degree failure on the cubic checkerboard; M = 10⁶ runs on syvert (commands in LOG).

### Rank 5 — Product-type factorisation and the coefficient channel (L1: PD-T?…-105, -111, -114, -115)

- Statement: measures matching a product measure on Π_{2n} (incl. ordered Harris–Simanek checkerboards and Padua with cubature weights) have product-type coefficients and a factorised propagator (111, PROVED); at product-type points the first-order Gram derivative of the coefficient map is given by univariate data, with off-pattern gains up to 1e14 on clustered checkerboards (114 parts 1–4 PROVED); a closed-loop dot-product rounding model reproduces the clustered-checkerboard loss (115, MEASURED; reviewer resolution with actual double dot products).
- Prior art: BPS Remark 5 (product case, part 1 of 105). Brief: analytic damping of the closed loop (I − T)⁻¹; channel under other selection rules.

### Rank 6 — L4 placement (PD-T?…-401)

- Statement: with distinct nodes and U(2m+1), no operator commuting with X and Y and no fixed number m of start vectors puts S_m and S_{m+1} in one band Krylov sequence; S_0..S_n needs m ≥ n (affine A: n+1, attained by injecting one start per degree). Both hypotheses necessary.
- Status: PROVED, confirmed by reconstruction 01. Prior art: informal versions (Zhu–Nakatsukasa §3; Hokanson §2); Sinha 2026's block Paige identity covers the single-operator corollary of 103.
- Brief: relate to deflated band Lanczos with growing starts; small section in a paper with Rank 3/4.

### Rank 7 — Givens updating note (L5: PD-T?…-501, -502, -505; PD-N?…-503, -506–508)

- MEASURED: Givens error slope vs M ≈ 1.40 [1.01, 1.79] (Padua cubature) vs HL 0.73, CGS2 0.48, Householder 0.38; frozen kill test fires as written on the uniform-random family. 'Largest' redundant-pivot rule degrades (PD-N 506, scope n ≤ 10 for no-catastrophe); κ-pivot and magnitude rules fail (507); FIFO deferral fails (508); prefix-unisolvence mechanism refuted (503). PROVED: routine rotation-count bound (not an IEP backward-stability statement); all-prefix-unisolvent orders exist (505). OPEN: exact zero-pattern invariant proof for the fixed scheme.
- Brief: short negative note; more sizes; stage-structure M·u bound.

## 2. Failed and refuted routes (all preserved in direction records)

Ritz governance off product supports; single-section falsification by tensor grids (withdrawn); "selection, not truncation" (refuted, N105); support-shape classifier (refuted, N106); HL SIMAX windowed (N, N*) form (N102); universal propagator predictor, H_lin, two relations as an unconditional fix (N103); open-loop coefficient-noise estimates (N104); dilation/POVM route to the backward question (N304); quantitative Lin (no Krylov structure); "count decides (H)" (N306); R06 hypotheses (N307, N308); Greenbaum-width √ε parallel (withdrawn); rounding-only partial reorthogonalization trigger (L2 N202); one-relation selections keeping spans near S_n (L2 N203); exact window dot products against the coefficient channel (L2 N204); prefix mechanism for the 'largest' catastrophe (L5 N503); magnitude/κ-pivot and FIFO pivot rules (L5 N507, N508).

## 3. Literature baseline

71 Step 0 records (7 complete fulltexts read from AC's copies; 64 from notes, UNVERIFIED), an online resolution pass (36 statements, 17 records; WebFetch digests), Barrio–Peña–Sauer 2010 read from AC's copy, and four prior-art reviews (L1, L3). Key corrections: HL p. 1088 is an observation; Xu's block-Jacobi/Favard theory is Trans. AMS 343 (1994); Greenbaum 1989 interval-width accounts conflict (pending-reference); Koiran's "wide open" concerns exact commuting extensions of general pairs; Kachkovskiy–Safarov's √-bound confirmed but structure-free.

## 4. Independent checks performed

| Scope | Reviewer | Verdict summary |
|---|---|---|
| Input reproduction | Sonnet 5.5 high | All 12 scripts reproduce; three discrepancies |
| L1 R01–R03 | Opus 5.5 xhigh (recon 01) | Proofs confirmed; two blocking findings (B1, B2) applied |
| L1 response + R04–R07 | same reviewer (recon 02) | No blocking findings; T-113 exact rerun |
| L1 prior art | Opus 5.5 high | Partially known throughout; BPS 2010 then read |
| L3 R01–R03 | Opus 5.5 xhigh (recon 01) | No PROVED claim refuted; exact rerun of 306, N301 |
| L3 R04–R06 + response | Opus 5.5 xhigh (recon 02) | No high findings; 313/N303 confirmed n = 4..16 |
| L3 prior art | Opus 5.5 high | Partially known; Greenbaum width conflict |
| L5 R01–R03 | Opus 5.5 high (recon 01) | Five medium corrections applied |
| L2 R01–R03 | Opus 5.5 xhigh (recon 01) | Span drift confirmed; 201, 202 confirmed; high finding on 205 applied |
| L2 prior art | Opus 5.5 high | All four mechanisms partially known; drift in 2D under full CGS2 not found |

These Claude reconstructions supplement, and do not replace, the required Codex audit.

## 5. Runs needed (none executed here)

M = 10⁵–10⁶ experiments for L1/L2/L3 on syvert0/1/2 (exact commands in LOG.md and the direction records), L5 larger sizes and checkerboard orders, the reviewer's equispaced n = 8 certificate and δ₀(n) reruns.
