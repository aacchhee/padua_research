# Review of the MZ-SP plan (plan-sp.md, correspondence-sp.md)

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), effort high. I did not write the material reviewed.
**Commit and branch:** `claude/padua-mz-paper-20261113` @ `761e884`.
**Read:**
- BRIEF, plan-sp, correspondence-sp, split-map;
- `tracks/mz-constants/paper-sp/manuscript.tex` (preamble ignored);
- `manuscript-insert.md` and final-id-map;
- the S3, P1 and P2 theory records (PD-T533–543), and the cleanup records for PD-T376–381;
- the PROOF_STATUS rows requested, plus PD-T106/107/112–114/296;
- `literature/INDEX.md`, with the padua-literature-20261103 addenda and bib;
- MZ-CC's weight lemma, for comparison.

**What I did and did not run:** no reruns. I did one floating-point evaluation of the PD-T379/533/537 closed forms, for orientation only. This file is the only file I wrote.

**Verdict:** the outline is coherent for a JAT reader. The section order is right, and the scopes are mostly exact. Before the PR #31 text is inserted, the plan needs:
- 5 MAJOR fixes (F1, F2, F7, F11, F12);
- one item that blocks submission (F13);
- a notation register (F12).

## (a) Structure, order, CC recap

**F1 MAJOR — the 1-page recap omits a CC fact that the new §6 proofs need.** Every place an SP proof uses a CC fact:

| SP proof | CC fact used | In the current recap? |
|---|---|---|
| Thm 3.1 (PD-T021) | w_j=∫ℓ_j; λ₋(N,N−1)→0 (PD-T018); λ₋(512,511)<1/4 (PD-N004) | yes |
| Thm 6.1 (PD-T534 §3), Thm 6.3 (PD-T536 §1) | **floor w_j ≥ (1+min(j,N−j))/N² for all 0≤j≤N**, on meshes N=m and N=m+1. This also gives positivity, which the coordinatewise argument needs. Plus λ₊(N,n)≤2 for n<N, applied in each coordinate, which gives the tensor bound 4. | **floor: no.** MZ-CC's lemma states "w_j ≥ m_j/N²", but the SP recap dropped that sentence. The upper bound is recapped. |
| Thm 7.1 (PD-T297) | w_j ≥ (π−4/3)sinθ_j/N at interior nodes. This needs "error ≤ (2/3)sinθ_j", which is in MZ-CC's *proof*, not its statement. Plus λ₊≤2 on meshes m and m+1. | only partly: the reader must redo the step |
| weights, carriers, kernel, operator, P1 | none: the Lobatto sums and the cosine series are proved inside SP | — |

Two recap items are never used: d_N (eq:ade) and the upper bound w_j ≤ 5 sinθ_j/N. d_N also clashes with d_m and d_j.

*Recommendation:*
- Make one recap lemma, "CC weights", and prove it in SP; the proof is about 12 lines, MZ-CC's proof plus one line. Its parts:
  - the formula;
  - the endpoint weights 1/N² (N odd) and 1/(N²−1) (N even);
  - the bracket error;
  - the bound with π−4/3;
  - the floor (1+min(j,N−j))/N².
- Cite MZ-CC only for the spectral proposition.
- With that, about 1.2 pages is sufficient.

**F2 MAJOR — the central theorems rest on an unrefereed companion paper.** PD-T014 (λ₊ ≤ 2−4/N+4/N²) is a premise of Thms 6.1, 6.3 and 7.1. Its MZ-CC proof is about 1.5 pages (Lemma 2.1 and Thm 2.3). *Recommendation:* reproduce it as Appendix C, cross-cited, or put MZ-CC on arXiv first and state the dependence in §1 (AC's choice). Either way, cite stable MZ-CC labels: plan-cc renumbers Lemma 3.1 to 2.2.

**F3 NOTE — keep the corner operator after the carriers.** The order is forced by the proofs:
- PD-T536 §4 takes c₋<0 from PD-T533 (c₋ ≤ −c_new) and c₊>0 from PD-T379.
- PD-T540's "0<c₊" uses PD-T536.
- Only the carriers give the fixed-ratio threshold (Cor 5.3).

§7 (PD-T297) is independent of §6. Its "nevertheless" position works.

**F4 MINOR — the weight estimates are proved twice.** PD-T534 §1–2 is a uniform nodal estimate, (6) and (8), valid on both parities. It implies the fixed-index limits and majorants of PD-T295 and PD-T377, because D_jk ≤ (1+j)(1+k) and mMR² ≳ m⁴/4. The plan proves the V_R strip estimates twice: in §4 and again in App. A.
- *Option:* prove (8) once in §4 and derive Thm 4.1 and Prop 4.2 as corollaries, with the statements verbatim. This saves about 1.5 pp.
- It is a new proof route, so it needs a short record and an audit.

**F5 MINOR — statement count in §§5–6.**
- Merge Props 5.4–5.6 into one "scalar-carrier bounds" proposition with parts (a), (b) and (c).
- Keep only these in §6:
  - the definition of B;
  - the limit theorem, PD-T536 (2)–(3);
  - a structure theorem, PD-T539 with PD-T540;
  - the certificate proposition.
- Move PD-T534 and PD-T535 to Lemmas A.1 and A.2, with a one-paragraph proof route in §6.

**F6 MINOR — internal process language in the current text.** Phrases such as "accepted … in Claude cleanup audit 01", "An independent Astra agent separately reran", "The accepted exact rational-pencil computations" and "audit" have to go, in addition to the status box and the IDs.

## (b) Statement scopes against the records

**Checks that pass:**
- No decimals of c± in the headline or abstract.
- No first-crossing claim.
- The constants match the records: 120/K, 4096, 4300/log m, ‖L_m‖≤120, C/m, 28.376…, and the outward-rounded [0.01316, 0.47781].
- The raw 1/9 and 1/36 paragraph is present.
- PD-T544/545 are correctly moved to MZ-CC. BRIEF §0/§2 still list them under SP and should be fixed.

**F7 MAJOR — the ‖B‖ enclosure is weaker than what the paper itself proves.**
- PD-T542's lower endpoint is only the rectangle bound, 0.013164….
- PD-T536 §4 proves c₋ ≤ −c_new and c₊ ≥ c₊^(379), and PD-T540 gives c₋=−‖B‖. Hence ‖B‖ ≥ c_new = 16(51/200)(49/200)/[9A·J(51/200)] ≈ 0.02964.
- PD-T542 itself says stronger analytic bounds "may be combined". Also c₊ ≥ 1/[36A·J₊(1/8)] ≈ 0.01278.
- J(a)=[A+C(1/a)]/2, and C is a fourth difference of x² log x. So c_new and PD-T379's c₋ are closed forms in logarithms of rationals, and certifying two digits takes a few lines.

*Recommendation:* state the certificate verbatim, then add a corollary:

c_new ≤ ‖B‖ = −c₋ ≤ 0.47781, and c₊^(379) ≤ c₊ < ‖B‖,

with exact forms, and decimals marked "≈" unless certified. It still gives "no useful digits". The combination is outside the literal PROOF_STATUS scopes, so register it or give it as a remark with its one-line proof.

**F8 MINOR — no slot for "two active corners do not double".** Add a remark after Thm 6.3 saying:
- Exactly two corner patches are active: (±1,1) for even m and (1,±1) for odd m.
- Their Gram blocks are identical (audit A7), so every eigenvalue of B is doubled in *multiplicity*, not in value.
- c± are the extremes of the single-corner B. The factor −16 already contains both strip contributions.

This remark is also needed to explain the "doublets" of PD-T543.

**F9 MINOR — §8 measured material.**
1. PD-T543's Q_min-secant criterion was essentially postdictive (audit-02 B1). Only the mode-weight, L-distance and branch-rate tests were prospective. Say so, or leave PD-T543 out.
2. If the B_K proxies (−0.1336, +0.0456, b₂=−0.0955) appear, label them MEASURED and note that the tail bound 120/128 certifies nothing.
3. Do not reproduce PD-T380's "moves toward raw −1/9" diagnostic, unless you also say that −1/9 is a raw energy and not a spectral constant.
4. Do not present 1238–1240 as a sign window: m=1238 is measured, not certified positive. Note that the odd witness at m=1101 comes before 1240.

**F10 MINOR — headline wording.**
- Item 1: "every degree-m exact rule" needs "supported on X_m", because the marginal identity depends on the support.
- Item 2: the registered scope is fixed 1/2<θ<1 with n=⌊θm⌋, plus n=m−1; "n/m>1/2" is broader.

## (c) Appendices: feasibility, length, shortening

**Calibration:** the current SP source (35.7 KB) builds to 15 pp in `elsarticle` preprint 12pt, so about 2.4 KB per page.

| Appendix | Proof text in the records | Pages |
|---|---|---|
| A | PD-T534 4.7 KB + PD-T535 6.3 KB + PD-T536 8.2 KB | about 8, plus 0.5 of glue |
| B | PD-T539 8.6 KB + PD-T540 3.0 KB + PD-T541 6.2 KB + PD-T542 about 3 KB | about 8.5 |

Both appendices are feasible. A realistic total is **35–40 pp**, not 28–32: the main text runs 21–23 pp. Update the estimate (MINOR); AC ranks coherence above page count.

**Ways to shorten without losing rigor:**
- **PD-T541:** keep (1)–(5) and (9)–(12), with interval Darboux evaluation. Drop the moduli (6)–(7), which PD-T542 does not use. Saves about 0.7 pp.
- **PD-T536 (4):** keep it as a remark with its proof (about 0.8 pp), or omit it, since it certifies no practical window. AC's choice.
- **PD-T535 §1:** this section reproves the Legendre normalization and the Laplace and Bessel integrals. Citing them instead would save about 1 pp, but the repository's rules would then require LIT records. Given AC's preference for keeping derivations, keep it and compress it.
- **F4 and F5:** apply them.

## (d) Title, abstract, headline

**Title options:**
1. *Signed Padua cubature beyond half-exactness: a sharp threshold and exact logarithmic Marcinkiewicz–Zygmund growth*
2. *Marcinkiewicz–Zygmund inequalities for nontensorial Clenshaw–Curtis cubature at the Padua points*

The search terms "Padua points" and "nontensorial Clenshaw–Curtis" (the name used by SVZ 2008) should appear in the title or the abstract.

**Headline order:**
1. Half-exactness is the sharp threshold.
2. The exact rate is inf/sup σ(B), for an explicit compact operator with an elliptic kernel; c₋=−‖B‖ is simple and 0<c₊<‖B‖.
3. The uniform signed hyperinterpolation norm is at most 28.38.
4. The mechanism is the boundary weights, w ~ −16e_je_k(−1)^j·log m/m⁴.

Marginal compression is a tool, not a headline. Drop "Analytic proofs are included."

**Abstract skeleton:** rule and spaces → threshold → λ±/log m → inf/sup σ(B), with B's properties → coarse enclosure, with decimals open → uniform norm → finite certificates → "positive Padua rules and tensor CC are not covered".

## (e) Notation conflicts (MAJOR F12: build the register before inserting the PR #31 text)

| Symbol | Competing meanings | Suggestion |
|---|---|---|
| **J₀, J** | Bessel J₀; rectangle integrals J_t(U,V) with t=0 (PD-T541): **J₀(U,V) collides directly**; J±(a), J(a) (PD-T379/533/537); isometry J (Thm 3.1) | rectangle → 𝒥_t; isometry → ι |
| m vs N | Thm 3.1 uses N, §4 "m=N" | m for Padua throughout; N∈{m,m+1} only for CC meshes; MZ-CC's floor index m_j → (1+d_j) |
| λ± | CC λ±(N,n); the records use λ±(m,m−1) for Padua | λ^P±(m,n) |
| endpoint factors | ε_j, γ_k (SP); γ_j (recap); eta_k (records); e_j (limit); e_k=min(k,M−k) (PD-T534/536); γ_m (PD-T536 coefficients) | one ε^{(N)}_j for all Lobatto meshes; keep e_j for the limit factor; distances d_j, d′_k |
| weights | W_jk, w_j, w_jk/w_z, α_j/β_k, w^CC; w_a(t) arcsine density; w_kl (PD-T535) | arcsine density → ω_a |
| ρ | ρ_jk; Abel parameter (PD-T539); angular mesh width (PD-T541); MZ-CC's ρ_{N,n} | Abel parameter → ϱ; mesh width → δ_θ |
| C | C₀=(1+π⁴)/2; C_P; C(q); C, C_U; C_m, C_∞; operator C; C_{f,r,s}; MZ-CC's own C₀ | C(q) → Δ⁴h(q); the operator C → B directly |
| B | corner operator; "positive matrices A,B" (PD-T536 §5); MZ-CC's Gram bound B (never recap it) | rename the matrices X, Y |
| K | truncation index; kernel K_{m−1}; elliptic K(k); MZ-CC's K_N | 𝒦_{m−1}; **K**(k) |
| c | c_a (Chebyshev normalizers); c_j (trapezoid halfweights); c±; c_new; c±(379) | keep c± for the sharp limits only; κ^car± and κ_* for the carrier constants |
| A | 4 log 2; A=−B; A (kernel error); A_R | write 4 log 2 explicitly; A=−B → B⁻ |
| θ | angles θ_j; ratio θ (Cor 5.3); angle in PD-T541; grid "theta=256" | ratio → τ, and rename PD-T534's folded angles |
| M | m+1; 2R+1 (Thm 7.1, ≠ m+1 for odd m); trapezoid denominator; Schur row bound | M := m+1 only |
| η, κ, ν, g, h, U, L, S, D, d, H, Q, P, V, σ, r, T, E, I | each has at least 2 meanings across §§4–7 and the appendices | resolve in the register |

## (f) Results the plan forgot

- **PD-T107 (MINOR)**, PROVED: certified strict brackets at m=10, 20, 30, 40. Use it to replace the float Table 2 (PD-T026), and merge it with PD-T298/299 into one certified table for m=10…80.
- **c₋ ≤ −c_new and c₊ ≥ c₊^(379)**: see F7.
- **PD-T113 and PD-N051 (MINOR).** The remark after Thm 7.1 ("reproduction on 𝒫_k for k ≤ min(n,m−n)") is stated without proof. Add the one-line degree argument. PD-N051 shows that quadratics are not reproduced at n=m−1, for every m≥3; cite it if sharpness is claimed.
- **NOTE: a corollary the plan could add.** Write τ_m=Σ_z|w_z|; then τ_m ∈ [4, 4+68/(3m)].
  - It follows at once from PD-T297's proof: |w_z| ≤ v_z+(68/3m)ρ_z, Σv_z ≤ 4, Σρ_z=1, Σw_z=4.
  - It proves SVZ 2008's statement that Σ|λ*|→4 for the interpolatory weights, which SVZ give without proof (LIT-427, p. 419).
  - It is not registered. Register it, audit it and screen priority before use.
- **PD-T296 (NOTE):** positive-reference MZ at every ratio; optional, as a contrast.
- **PD-T106 (NOTE):** the certificate paragraph should say how the quadrature Gram matrix Q is computed exactly.

**F13 BLOCKING (for submission, not for writing).** PD-T376's witness arrays and exact-norm files are not in Git, and cold storage is pending. As it stands, Prop 8.1 cannot be checked from public material. Options:
- AC creates the deposit (Zenodo) before submission;
- regenerate the witness deterministically from committed code;
- drop Prop 8.1 and keep PD-T380 as MEASURED.

The checkers for PD-T542 (`P1_rectangle.py`, `interval_dyadic.py`, receipts), PD-T298/299 and PD-T107 are committed; name them precisely.

## (g) Literature for the introduction

**F11 MAJOR — the density lemma needs attribution.** Lemma 2.3 (w=ρ·d_m) is SVZ 2008's weight formula (33). The discrete orthogonality and kernel behind it are in BCDMVX 2006 Thm 2 and CDMV 2008 (9)–(10). The current text states and proves the lemma with no attribution. Cite SVZ and BCDMVX, both read; CDMV 2008 is unread.

Coverage of the sources: ✓ = fulltext-read at a usable scope; ◐ = partial; ✗ = not read.

| Source | LIT | Coverage | DOI |
|---|---|---|---|
| Caliari–De Marchi–Vianello, AMC 165 (2005): origin of the Padua points | **none** | ✗ | 10.1016/j.amc.2004.07.001 |
| Bos–Caliari–De Marchi–Vianello–Xu, JAT 143 (2006) | 312 | ✓ journal pp. 15–25 | 10.1016/j.jat.2006.03.008 |
| Bos–De Marchi–Vianello–Xu, Numer. Math. 108 (2007) | 313/002 | ✗ excerpts only | 10.1007/s00211-007-0112-z |
| Sommariva–Vianello–Zanovello, Numer. Alg. 49 (2008): the signed rule, few negative weights (p. 421) | 427 | ✓ pp. 409–421 | 10.1007/s11075-008-9203-x |
| Caliari–De Marchi–Vianello, JCAM 210 (2007), hyperinterpolation on the square | 428 | ✓ journal | 10.1016/j.cam.2006.10.058 |
| Caliari–De Marchi–Vianello, JCAM 221 (2008), computational aspects | 330/003/366 | ✗ | not in repo |
| Padua2DM, Numer. Alg. 56 (2011) | 368 | ✗ (keyword scan only) | 10.1007/s11075-010-9373-1 |
| Xu, JAT 87 (1996) | 314 | ✓ full | 10.1006/jath.1996.0102 |
| Kolomoitsev–Lomako–Prestin, JAT 229 (2018): positive-weight L^p MZ at Padua nodes, the key contrast | 488 | ✓ most pages | 10.1016/j.jat.2018.02.005 |
| Dencker–Erb, JAT 219 (2017) | 014 | ◐ §§2.1–2.3 | 10.1016/j.jat.2017.03.003 |
| An–Sommariva–Vianello, MCS 252 (2027): finite Padua η<1 for m≤20 | 045 | ◐ author text §§3.1–3.2; journal body not read | 10.1016/j.matcom.2026.10.001 |
| De Marchi survey, CMA 5 (2022) | 326/377 | ◐ §3.3 | 10.33205/cma.1070020 |
| Kolomoitsev–Lomako, AMC 403 (2021) (optional) | 379 | ◐ arXiv v1 lemmas | 10.1016/j.amc.2021.126192 |
| An–Ran–Wu, arXiv 2510.04904: says Padua hyperinterpolation is "open"; relevant to Thm 7.1 | 387 | ✗ — read before citing | arXiv |
| Wu, AML 182 (2026) (motivation); De Marchi–Kroó (2018) | 489/490 | ✓ / ◐ | 10.1016/j.aml.2026.110033; 10.1007/s10474-017-0769-4 |
| Sloan (1995), hyperinterpolation | none | ✗ | not in repo |

LIT-633 (Basor–Ehrhardt) is not needed in MZ-SP.
