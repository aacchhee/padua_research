# Independent check 02: CC interpolation-norm corollary and SP corner-norm lower bounds

Checker: Claude Opus 5.5 (claude-opus-5-5), high effort, independent subagent. I did not write either record.
Date: 2026-11-13. Repository: /home/claude/padua_research, branch claude/padua-mz-paper-20261113, head 34b9315, plus the uncommitted file theory/sp-corner-norm-lower.md.
Scope: two provisional claims, PD-T?mz-paper-claude-01 part (d) together with the manuscript items that use parts (a) and (b), and PD-T?mz-paper-claude-02. I ran no git commands that change state. This file is the only file I wrote. My scratch scripts are in /tmp/chk, outside the repository.

Executed computations: (i) exact rational arithmetic (Python `fractions`) for S_N and q_N, N=2..400; (ii) binary64 evaluation of the interval endpoints and of 2√2/π²; (iii) a floating-point CC Gram eigenvalue sanity check, N=10..100; (iv) a 50-digit `decimal` evaluation of c_new, c₋^(379) and c₊^(379), plus a float Simpson cross-check of J₋(51/200) and J₊(1/8) from their integral forms. Items (iii) and (iv) are measurements for orientation. No proof step below rests on them.

---

## Claim 1 — PD-T?mz-paper-claude-01 (d), and its use in the manuscript

### Reconstruction of (d)

Setting (PD-T013): x_k=cos(kπ/N), 0≤k≤N, N≥2. The weights are w_k=∫ℓ_k dx, all w_k>0, and Q_N is exact on Π_N. Define λ₋(N,N)=inf_{0≠p∈Π_N} Q_N(|p|²)/∫|p|².

1. *Isometric identification.* Interpolation u ↦ p=𝓘_N u is a linear bijection from ℝ^{N+1} (or ℂ^{N+1}) onto Π_N, because the N+1 nodes are distinct. Since p(x_k)=u_k, we have Σ_k w_k|u_k|² = Q_N(|p|²). Positive weights make ‖u‖_w a norm.
2. *Norm equals the inverse minimum quotient.* ‖𝓘_N‖² = sup_{u≠0} ∫|𝓘_N u|²/‖u‖_w² = sup_{0≠p∈Π_N} ∫|p|²/Q_N(|p|²) = 1/λ₋(N,N). The minimum quotient is strictly positive: PD-T013 gives Q_N(p²)>0 for every nonzero real p∈Π_N, and the unit sphere is compact. For complex data, write p=a+ib with a,b real. Then Q_N(|p|²)=Q_N(a²)+Q_N(b²) and ∫|p|²=∫a²+∫b², so the complex infimum equals the real one. The real and complex operator norms therefore coincide. The identity holds for every N≥2, with no asymptotics.
3. *Quantifier: Π_N, not Π_{N−1}.* Step 2 needs the minimum over the full interpolation space Π_N. PD-T546 asserts the limit on Π_N explicitly ("The same limit holds on the full interpolation space Pi_N"). Its proof gives the liminf from the finite bound (2), which holds for every real or complex p∈Π_N with L≥16. The limsup follows from the monotonicity λ₋(N,N)≤λ₋(N,N−1) together with the S1-02 limsup on Π_{N−1}. Both hold through all integers N. Hence (log N)²λ₋(N,N)→π⁴/8.
4. *Limit.* ‖𝓘_N‖/log N = [(log N)²λ₋(N,N)]^{−1/2} → (π⁴/8)^{−1/2} = √8/π² = 2√2/π². Computed value: 0.2865795841253782, identical to (π⁴/8)^{−1/2} in binary64.

Sanity measurement, not a premise: float CC Gram eigenvalues give (log N)²λ₋(N,N) = 2.12, 2.86, 3.54, 3.86 and 4.33 at N = 10, 20, 40, 57 and 100. Thus ‖𝓘_100‖/log 100 ≈ 0.48, far from 0.2866. Convergence is slow, and the statement correctly claims no rate. In this range λ₋(N,N) and λ₋(N,N−1) agreed to 5 digits. This is not claimed anywhere and I make no claim about it.

### Manuscript `cor:interp-norm` (tracks/mz-constants/paper/manuscript.tex, lines 909–923)

- The statement uses real data in ℝ^{N+1}. This is consistent with `eq:variational`, which is real. By step 2, the complex norm would be the same.
- The proof is complete. It uses the bijection, the identity ‖u‖_w²=Q_N(p²), sup=1/inf, and Theorem `thm:sharp-min`. That theorem states the Π_N limit, and its proof (lines 892–903) obtains both the liminf and the limsup for λ₋(N,N) correctly. Positivity of λ₋(N,N) is available from `thm:cardinal`. Two facts are used implicitly: positivity of the weights (that ‖·‖_w is a norm) and λ₋(N,N)>0. Both are stated earlier in the paper, so this is acceptable. Optional: add "(the weights are positive, Lemma identities)".
- Nothing is overclaimed. The corollary asserts no rate, and `rem:rate` already says the finite bound is coarse.

### Manuscript `lem:U-exact` and the N≥57 claim

Proof reconstruction: U_r² = Σ_{s=0}^r U_{2s}, and ∫U_{2s} = 2/(2s+1), so ∫U_{N−1}² = 2S_N. On the nodes, U_{N−1}(cos θ)=sin(Nθ)/sin θ vanishes at every interior node, and |U_{N−1}(±1)|=N. The endpoint weights are 1/N² for odd N and 1/(N²−1) for even N, so Q_N(U_{N−1}²) = 2 or 2N²/(N²−1). Hence q_N=1/S_N for odd N and N²/[(N²−1)S_N] for even N, and λ₋(N,N−1)≤q_N because U_{N−1}∈Π_{N−1}. Correct.

My exact rational arithmetic (Python Fractions):

| Check | Result |
|---|---|
| S_57 > 3 | True (S_57 − 3 ≈ 0.003287) |
| S_58 > 3·58²/(58²−1) | True (margin ≈ 0.01109) |
| q_56 > 1/3 | True (S_56 ≈ 2.99444); q_55 > 1/3 also |
| {N ≤ 400 : q_N < 1/3} | exactly {57, …, 400}; the first N is 57, and no N<57 qualifies |

The monotonicity step is valid. S_N increases. For even N, N²/(N²−1) decreases, so q_N ≤ 58²/[(58²−1)S_58] < 1/3 for even N≥58. For odd N≥57, q_N=1/S_N≤1/S_57<1/3. The lemma's "q_N<1/3 for every N≥57" is proved for all N. The parenthetical "for N=56 one has q_N>1/3" is correct.

Floating measurement shows λ₋(N,N−1) already below 1/3 at N=20, so 1−η_N=λ₋ actually holds from much smaller N. Neither the record nor the manuscript says 57 is the true onset; both describe it as the U-witness threshold. No overclaim.

### Manuscript `cor:endpoint` (lines 1068–1093)

- `eq:defect-identity`: η=max{1−λ₋, λ₊−1}, so 1−η=min{λ₋, 2−λ₊}. Correct.
- Two-sided bound. Lower: λ₋(N,N−1)≥K_N^{-1} (`thm:cardinal`) and 2−λ₊≥1/3 (`thm:five-thirds`, all N≥2), giving min{K_N^{-1},1/3}. Upper: 1−η≤λ₋≤min{1 (constant polynomial, since Q_N(1)=2=∫1), 128000/(log N)² (`thm:harmonic`)}. Correct.
- For N≥57: λ₋≤q_N<1/3≤2−λ₊, so 1−η_N=λ₋(N,N−1). Correct.
- Limits: (log N)²(1−η_N) → π⁴/8 by `thm:sharp-min` (the Π_{N−1} version). κ₂=λ₊/λ₋ because λ₋>0. Then κ₂/(log N)² = λ₊/[(log N)²λ₋] → Λ_edge/(π⁴/8) = 8Λ_edge/π⁴ by `thm:edge-limit`. Correct.
- Numeric intervals, my binary64 values: 8/π⁴ = 0.0821278580, 8·1.0044369/π⁴ = 0.0824922511, 12/π⁴ = 0.1231917871. So [0.0824922…, 0.1231918…] ⊂ [0.08249, 0.12320] holds, with margins of about 2.3e-6 and 8.2e-6. These margins are far larger than binary64 error. The computer-free interval [8/π⁴,12/π⁴] uses only 1≤Λ_edge≤3/2 from `thm:edge-limit`. The narrower interval is labelled as resting on the computer-assisted `prop:edge-certified`. Correct, and labelled properly.
- The proof is complete for its stated content and does not overclaim.

### Record-level notes (cc-defect-condition-corollary.md)

1. In (d), λ₋(N,N) is used but never defined in the record. The record's Statement defines λ₋(N) only on Π_{N−1}. Add: "λ₋(N,N) = minimum Rayleigh quotient on Π_N".
2. The "Depends on" entry for PD-T546 lists only "(log N)²λ₋(N)→π⁴/8", which is the Π_{N−1} version. Part (d) uses PD-T546's Π_N clause. Cite that clause explicitly.
3. Editorial: (d) is listed before (c) in the Statement, and in the Proof it comes between (a) and (b). Reorder the parts.
4. (d) uses complex |u_k|², while the manuscript uses real data. Both are correct (see step 2). One sentence would make the record match the paper.

**Verdict, Claim 1: PASS with (minor, editorial) corrections.** The mathematics of (d) is correct. The quantifiers are right: Π_N, all N≥2 for the identity, the limit through all integers, real or complex data. The arithmetic (π⁴/8)^{−1/2}=2√2/π² is correct. The manuscript items `cor:interp-norm`, `lem:U-exact` and `cor:endpoint` are complete and do not overclaim. The exact-arithmetic N≥57 claim is confirmed.

---

## Claim 2 — PD-T?mz-paper-claude-02 (sp-corner-norm-lower.md)

### Normalization audit

| Source | Rule / measure | Space | Normalizer | Integers |
|---|---|---|---|---|
| PD-T381 (defines the common target) | unchanged even-checkerboard signed interpolatory Lebesgue Padua rule; unnormalized dxdy of mass four | Π_{m−1} total degree | log m | m≥2, both parities |
| PD-T536 (3) | "exact signed Lebesgue Padua rule of mass four", nodes (cos jπ/m, cos kπ/(m+1)), j+k even; unnormalized dxdy | Π_{m−1} | log m | all integers (both parities, same constants) |
| PD-T379 (4) | "Unnormalized Lebesgue dxdy, signed even-checkerboard Padua rule" (carrier: x with mesh m for even m, y with mesh m+1 for odd m, matching the same node set) | λ±(m,m−1) | log m | all integers |
| PD-T533 | "signed Lebesgue Padua rule and continuous unnormalized dxdy norm of PD-T381" | λ₋(m,m−1) | log m | all integers (each parity, then combined) |
| PD-T540 | same B and H=L²(D, ab da db) as PD-T536/PD-T539 | operator only | none | none |

All four sequence statements concern the same quantity λ±(m,m−1)/log m, with the same rule and measure, over all integers m. log R appears only inside PD-T534's internal estimates, where R=⌊m/2⌋. PD-T534 (3) converts these to log m with an explicit error of 4300/log m, and PD-T536's statement uses log m. In any case log R/log m→1, which would not change the limits. PD-T540's B is the same operator as PD-T536's: PD-T539 identifies the product-truncated norm limit literally. The Padua constants J₋ in PD-T379 and J in PD-T533 are the same function, [A+C(1/a)]/2, with C from PD-T379 (1).

### Reconstruction

(a) Let x_m=λ₋(m,m−1)/log m. PD-T536 gives x_m→c₋, a limit through all integers. PD-T533 gives limsup x_m ≤ −c_new through all integers. Since the limit exists, c₋=limsup x_m≤−c_new. PD-T540 (2) gives c₋=inf σ(B)=−‖B‖, so ‖B‖=−c₋≥c_new.

The limit/limsup combination is valid. The only requirement is that both statements concern the same full sequence, or at least that the bound holds along a subsequence of the convergent sequence. Both conditions hold here.

Admissibility in PD-T533: a=51/200, b↑49/200, a+b<1/2 for every fixed b<49/200. The bound is a scalar supremum over interior parameters, so no boundary family is assumed. I also spot-checked PD-T533's derivative inequality: N′(a)∈[−1/100,0] on [1/4,51/200]; a²(1/2−a)≥(1/16)(49/200); and −7/500+49/3200=21/16000>0. These are correct.

(b) Let y_m=λ₊(m,m−1)/log m. PD-T536 gives y_m→c₊, and PD-T379 (4)–(5) gives liminf y_m ≥ c₊^(379)=1/[36 A J₊(1/8)], so c₊ ≥ c₊^(379) > 0. The strict positivity of c₊^(379) is PD-T379's (J₊(1/8)>0). Valid.

Remark: PD-T536 §4 already states both inequalities in passing ("c_minus ≤ −c_new < 0", "c_plus ≥ c_plus(PD-T379) > 0"), where they serve as sign arguments. The new record's content beyond PD-T536 is the combination with PD-T540 into ‖B‖≥c_new. This is correctly described as a combination ("Combines …"). It is a corollary and makes no novelty claim.

### Numbers (computed by me)

50-digit `decimal` evaluation of the exact formulas (C(q) from PD-T379 (1), A=4 log 2):

| Quantity | Value |
|---|---|
| A | 2.772588722239781… |
| J₋(51/200) = [A+C(200/51)]/2 | 1.35143191429097537… |
| J₋(1/4) | 1.35288302274420920… |
| J₊(1/8) | 0.78400536769110933… |
| **c_new** = 16(51/200)(49/200)/[9A J₋(51/200)] | **0.02964176876275237885…** |
| c₋^(379) = 1/[9A J₋(1/4)] | 0.02962182359685996308… |
| **c₊^(379)** = 1/[36 A J₊(1/8)] | **0.01277888643955839765…** |

Plain binary64 gives c_new=0.02964176876275243 and c₊^(379)=0.012778886439557966, which agree to about 13 digits. Float Simpson quadrature of the integral forms (PD-T379 (7), truncated at u=3000, tail ≤8.9e-7) gives J₋(51/200)≈1.3514317 and J₊(1/8)≈0.7840053. These agree with the closed forms within the truncation error, so the closed-form transcription is confirmed.

Comparisons:
- The record's c_new = 0.0296417… and "0.029641768762…" match. PD-T533's display 0.029641769 matches. c_new > c₋^(379) ≈ 0.02962 holds, as PD-T533 claims.
- The PD-T542 lower endpoint for ‖B‖ is 0.013164946500379018…, and c_new/0.013164946500379 = 2.2516. The record's comparison sentence ("exceeds the rectangle certificate's lower bound") is correct, and the record correctly marks it as outside (a)/(b).
- My c₊^(379) agrees with the PD-T379 audit value 0.01277888643955839765 to all 20 digits shown.
- For consistency only: PD-T540 (3) gives 0<c₊<‖B‖, and the PD-T542 upper value 0.4778 bounds both. No contradiction. The record makes no claim relating c₊^(379) to PD-T542, which is correct, since c₊^(379)=0.01278 is smaller than 0.013165 and PD-T542 is a bound on ‖B‖, not on c₊.

### Record-level notes

1. "J as in PD-T533/PD-T537": J is defined in PD-T533 and PD-T379 (as J₋). PD-T537 is the carrier-ceiling record and is not needed. Suggest "J=J₋ of PD-T379, as used in PD-T533".
2. Optional: note that PD-T536 §4 already contains c₋≤−c_new and c₊≥c₊^(379). The record's new content is the ‖B‖ form via PD-T540.
3. The Scope wording is accurate. These are one-sided bounds only, with no decimal value of c±, and PD-T381's decimal conjunct remains OPEN.

**Verdict, Claim 2: PASS** (two optional editorial notes above; no mathematical correction needed). The normalizations agree across PD-T536, PD-T540, PD-T533, PD-T379 and PD-T381. The limit/limsup and limit/liminf combinations are valid through all integers m. The constants are transcribed correctly.

---

## Summary of verdicts

| Claim | Verdict | Corrections |
|---|---|---|
| 1. CC-01 (d) ‖𝓘_N‖=λ₋(N,N)^{−1/2}, ‖𝓘_N‖/log N→2√2/π²; manuscript `cor:interp-norm`, `lem:U-exact`, `cor:endpoint` | PASS with corrections (editorial) | Define λ₋(N,N) in the record. Cite PD-T546's Π_N clause in Depends on. Reorder parts (c)/(d). Optional real/complex sentence. |
| 2. SP-02 ‖B‖=−c₋≥c_new, c₊≥c₊^(379) | PASS | Optional: J reference (drop PD-T537); note that PD-T536 §4 already contains both inequalities. |
