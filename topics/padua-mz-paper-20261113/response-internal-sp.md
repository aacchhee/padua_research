# Response to the internal referee round: MZ-SP

- Editor: Claude Sonnet 5.5 (`claude-sonnet-5-5`), high effort. No Git state changed.
- Edited files: `tracks/mz-constants/paper-sp/manuscript.tex` (head `8f08d9a`, sha256 before `956fdee6…50b5`, after `da76c6c0…6336`; `refs.bib` before `318b8320…`, after `bc40f600…`), `tracks/mz-constants/paper-sp/refs.bib`, and `topics/padua-mz-paper-20261113/notation-sp.md` (register corrections). `tracks/mz-constants/paper/` (MZ-CC) was only read.
- Inputs: `referee-sp-math.md` (F1–F15), `referee-sp-exposition.md` (A–I), `notation-sp.md`, `correspondence-sp.md`, `correspondence-cc.md` (frozen numbering), and the MZ-CC manuscript for the statements cited.
- Build: `tools/build.sh … /tmp/sp-ref`: 50 A4 pages (was 47), zero LaTeX and BibTeX warnings, no over/underfull boxes, no undefined references or citations.
- Diff: `/home/claude/mzwork/sp-referee.diff` (unified diff of `manuscript.tex` and `refs.bib` against the head `8f08d9a` copy).
- Numbering check: theorem-like labels (35: `thm:`, `lem:`, `prop:`, `cor:`, `rem:`), and in fact all 116 labels of `/tmp/mzb/sp3/manuscript.aux` (sections, equations, appendix subsections), have identical numbers before and after. The only label changes: `sec:data` removed (unused, unnumbered section), `tab:notation` added (new Table 1). No theorem-like statement was added, removed or renumbered. Page numbers changed.

## Orchestrator dispositions applied

Accepted as binding: math F1–F15 with the referee's fixes; exposition MAJOR abstract and introduction (with the source restriction); section openings and definitions; notation register items and the two register errors; process language (A4 table); the KLP18 and ASV27 softenings; cuts (§8.3 secant paragraph, data statement condensed with exact file paths kept, 77-digit integers moved to Appendix B.5 with the 24-digit decimals kept in Prop 6.9). Declined as instructed: replacing Appendix A.2 Step 1 by citations; demoting Prop 5.8; the Θ(log m) fixed-ratio statement (B6).

## Mathematics referee (F1–F15)

| # | Disposition | What and where |
|---|---|---|
| F1 | Accepted | Prop 2.2 now cites MZ-CC by statement: Cor 3.2 (λ₊ ≤ 2−4/N+4/N², "same holds on every Π_n with n<N"), Thm 4.3 (λ₋(N,N−1)→0), Prop 8.1 (λ₋(512,511)<1/4). Checked against the frozen table in `correspondence-cc.md` and the MZ-CC manuscript (`cor:ratio-endpoint` = 3.2, `thm:harmonic` = 4.3, `prop:counterexample` = 8.1). The pointers are repeated in the introduction paragraph "Clenshaw–Curtis inputs". The proposition heading no longer carries the citation (nested brackets); the citations sit in the statement. |
| F2 | Accepted | `refs.bib` MZ-CC title now "…of Clenshaw--Curtis quadrature beyond half-exactness". |
| F3 | Accepted | Abstract: "marginal of the rule in the first coordinate … with m intervals". Intro: "first-coordinate marginal". Item A: "for every rule on the Padua points that is exact on 𝒫_m, the weights summed over the second coordinate at each node abscissa equal twice the CC weights with m intervals". §3: one sentence after Thm 3.1 says the other marginal is in general not twice the CC weight with m+1 intervals. |
| F4 | Accepted | Abstract: "computer-assisted spectral brackets at six degrees between 10 and 80"; ratio range "1/2 < n/m < 1". |
| F5 | Accepted | §6 opening: the sign pattern is stated at fixed index distance from the corner (1,1), "one of the two active corners (Remark 6.5)", with the remark that the approach is only logarithmic and the pattern is not visible at moderate m. (The referee's alternative wording about both corners was shortened to the corner that Thm 4.2 actually covers.) |
| F6 | Accepted | §8.3 (3): "no rate usable at these degrees (the explicit bound of Remark 6.4 is far too coarse)". |
| F7 | Accepted | §8.3 (2): mode 2 = two-dimensional span of the eigenvectors of the third and fourth smallest eigenvalues of L_m (its second near-doublet, cf. Remark 6.5); weight = squared norm of the projection of the normalised computed minimizer. "Compressed branches" is gone with the secant paragraph. Added "We have no explanation of the size of this weight" (expo B14). |
| F8 | Accepted | The pointer `evidence/P2-b2-calibration.json` for the proxy b₂ is in the data-availability paragraph (not in the body); §8.3 (4) now writes −0.09553. |
| F9 | Accepted | Orientation sentence after Prop 5.8: κ^car₋ ≈ 0.02962, κ_new ≈ 0.02964, U₋ ≈ 0.0333; improvement "about 2·10⁻⁵, that is 0.07 %"; ceiling exceeds κ_new by "about 12 %". Computed here with the paper's formulas: J₋(1/4) = 1.352883, κ^car₋ = 0.0296218, κ_new = 0.0296418 (difference 1.995·10⁻⁵, 0.0673 %), U₋ = 0.0333167 (U₋/κ_new = 1.124). The optional measured supremum 0.029643 was not added (not recomputed here). |
| F10 | Accepted | Remark 6.5: eigenvalues of the finite-rank form converge, counted with multiplicity, to those of B_K⊕B_K⊕0⊕0 (Lemma A.4); each nonzero eigenvalue of B_K is the limit of two of them, the rest tend to zero. "Strip contributions" (expo B20) replaced by "the two terms". |
| F11 | Accepted | Cor 5.3 proof: sentence that the carriers lie in 𝒫_{⌊τm⌋}, their energy limits and norm bounds do not depend on the ambient degree, so the variational principle on 𝒫_{⌊τm⌋} gives the divergences. |
| F12 | Accepted | Thm 7.1 proof: t_0 = 2, t_r = −4/(4r²−1) restated ("the coefficients of the proof of Theorem 4.2"); A_R := Σ_{r+s≤R} t_r t_s defined first, the first display marked as an intermediate identity; induction justification for Σ(2i−1)⁻¹ ≤ (R+2)/3 (each new term 1/(2R+1) ≤ 1/3) and the check (R+2)/3 ≤ R(R+2)/M′; "affects only the pairs (0,s), (r,0) with r,s ≥ 1 on the coordinate axes, the only pairs with a negative product". I rechecked the inequalities by hand, including A_R ≥ −4/M′ (it follows from 8/(M′(M′+1)) = 4/((R+1)M′) and M′²−1 = 4R(R+1)). |
| F13 | Accepted | App B.1: "the integral equals ξ_s⁻¹K(1/ξ_s) directly". Lemma 5.5: "Abel's test gives uniform convergence in ϱ ≥ 0, which justifies the limit". "Obtained on the closures" → "approached on their closures" (in the rewritten paragraph after Prop 5.6). |
| F14 | Accepted | See the notation list below: g, κ, α/β, τ, Q_i and the enclosure endpoints L, U are renamed; the local reuses of L (r+1, ⌊R/2⌋), U (cube size, rectangles) and r (‖B‖, local) are left and listed in the register. |
| F15 | Accepted | Data statement: "the enclosure of the energy is `q_center` ± `q_absolute_error`; the printed `q_enclosure` field is rounded for display and must not be used". |

## Exposition referee

### MAJOR

| # | Disposition | What and where |
|---|---|---|
| A1 | Accepted, restricted to read sources | Introduction: Padua context (Lagrange interpolation [BCDMVX06, Thms 2 and 3: Lebesgue constant at most a multiple of (log m)²], [Xu96], [SVZ08]; point count about half the tensor grid; Lebesgue measure is the Galerkin measure). New An–Wu 2022 (`AW22`, LIT-046, same bib data and coverage as the MZ-CC bib) is cited in the first paragraph (defect below one is the hypothesis of the relaxed-exactness error bounds for positive weights) and in the §7 opening. Not cited: CDMV 2005, Sloan 1995, BDMVX 2007, CDMV 2008, Padua2DM, Erb 2016, LIT-387 (see Deferred). I did not use "the first explicit unisolvent set" (no read source states it). |
| A2 | Accepted | Notation list below. |
| A3 | Accepted | §1 defines Π_n and 𝒫_n at first use (definition removed from §3); "Clenshaw–Curtis (CC)" expanded at first use; "uniform strong MZ constant at degree ratio τ" defined in §1 and used in Result B, Cor 5.3, Remark 5.4 (the "weak constants in the terminology of [ASV27]" clause was not added: not verified at the read scope of ASV27); "carrier" and "signed energy" defined at the opening of §5; harmonic numbers H_q defined at first use (Thm 4.2 proof) and in the notation table; "mode 2" fixed (F7). New Table 1 (notation, 9 rows) at the end of §2. |
| A4 | Accepted, all rows | l.498, 594–595, 789–790, 793–796, 856–857, 1199, 1499 (heading "Proof (computer-assisted)"), 1519, 1523–1524, 1565–1569 (whole secant paragraph dropped), Remark 5.4 (now consequences, "Consequences and scope"), "receipts" ×4 → "certificate files"/"output files", "Code and evidence" → "Code and data". Disclaimers: kept inside Prop 5.6 l.758, Thm 6.3, Prop 8.1; shortened Prop 5.8 (one sentence "The bound concerns only these scalar trial families; it is not claimed to be optimal or attained"), the orientation sentence, and Remark 6.4. |
| A5 | Accepted | New abstract (certified not exact; computer-assisted labels on both finite results; ratio range 1/2 < n/m < 1 as in Cor 5.3; enclosure [0.0131, 0.478] fixes no digit; c± not determined). The enclosure endpoints in the abstract are outward roundings of the two 24-digit decimals. |
| A6 | Accepted in part | Lemma 6.2 is named a "two-variable, quantitative Mehler–Heine-type formula" (before the lemma and in App A.2 Step 2), **without citation**: no LIT record exists for Szegő or DLMF. Prop 6.7: "Perron–Frobenius argument, in the spirit of Jentzsch's theorem" named, **without citation** (no record). Lemma A.4 square-root bound: kept, not cited (no record for Bhatia). App A.2 Step 1: **declined** (orchestrator). |
| A7 | Accepted | §4 opening (corner weights drive the rest), §5 opening plus split into 5.1 "Carriers and the threshold" and 5.2 "Normalized one-sided constants" (subsections carry no theorem counter, so no numbering change), §6.1 heuristic (triangle, measure, Mehler–Heine), §7 opening (boundedness despite divergence; hyperinterpolation context). One correction to the referee text: the Fejér factors localise the carrier on a **bounded number of nodes** (width about 1/a indices), not "a window of O(m) indices"; I wrote the former. |

### MINOR

| # | Disposition | Where |
|---|---|---|
| B1 | Accepted | = F1. The optional MZ-CC Thm 3.3 (5/3) was not used (it would change checked constants). |
| B2 | Accepted (bib title); arXiv id Deferred | Replace "Preprint in preparation" once MZ-CC is posted. |
| B3 | Accepted | §3 uses w̃_{jk}, Q̃_m, G̃_{m,n} for an arbitrary exact rule; "in particular this applies to Q^P_m" in the theorem. |
| B4 | Accepted | §3 opening rewritten ("Every such rule, in particular the interpolatory rule Q^P_m, is compared with the CC rule…; no sign condition needed"); "Throughout the CC analysis" → "For the CC rule we write". |
| B5 | Accepted | Thm 7.1 proof (see F12); w^CC_{N,j} introduced in §2 ("where Padua weights also occur") and in Table 1, and glossed in the proof. |
| B6 | **Declined** | Unregistered claim; see Deferred. |
| B7 | Accepted | Prop 6.9 states r̲ = n_L/2^256, r̄ = n_U/2^256 with the integers "listed in Appendix B.5" and the 24-digit decimals; n_L, n_U are displayed in App B.5 (digits compared against the original: identical). |
| B8, B9 | Accepted | "the interpolatory (signed) Padua rule Q^P_m" in Thm 6.3 and Result B. |
| B10 | Accepted | λ^P_±(m,n) in all statements outside the generic §§1–2 discussion (Thm 3.1 uses λ_min(G̃_{m,n}) for the arbitrary rule). |
| B11 | Accepted | W_{jk} → w̃_{jk}; α_j, β_k (Lemma A.2) → w^CC_{m,j}, w^CC_{M,k}; w_{kl} (A.2 Step 3) → ϰ_{kl}; bins W_i (B.5) → sans-serif 𝖶_i (Ω is already the function of B.1). |
| B12 | Accepted | See the list below. |
| B13 | **Declined** | Every use carries the noun ("Lemma A.1", "Appendix B.5"), so no actual ambiguity; separate counters would be a visible restyling. |
| B14 | Accepted | = F7. |
| B15 | Accepted in part | Data statement condensed in wording, exact paths kept; `\path{P1_rectangle.py} \verb|--N 16 --theta 256|`. Not done (AC): curated `code/` directory or README in the deposit; confirming that the repository is public (see Deferred). |
| B16 | Accepted | The remark moved after Thm 4.2: "j,k are the raw grid indices, counted from the corner (1,1), so the majorant is weakest at the other corners; the fixed-index limit is stated only for indices that stay bounded". |
| B17 | **Declined** | Orchestrator (Prop 5.8 kept). |
| B18 | Accepted | MSC 47B38 and 65G20 added (AC to confirm the codes). |
| B19 | Accepted | The §6.2 measure is μ_𝒯 (dμ_𝒯 = ab da db); the §7 Chebyshev measure is ν_Ch; the plain μ stays the generic measure of §§1–2. |
| B20 | Accepted | = F10. |

### TYPO

| # | Disposition |
|---|---|
| C1 | Accepted: `\label{sec:data}` removed. |
| C2 | Accepted: Σ_t series index ℓ. |
| C3 | Accepted: `\path{P1_rectangle.py}` and `\verb`. |
| C4 | Accepted: superseded by F7. |
| C5 | Accepted: proof heading (A4). |
| C6 | Not needed: the printed reference reads "C. An, A. Sommariva, M. Vianello" (the bst abbreviates given names); the bib field is unchanged. AC may still prefer a full given name. |

### Notation (D1, D2; renames applied, minimal and local)

- 𝒥_t(U,U′) for the rectangle integrals (so J₀ is only Bessel); Φ_t(a;[u,v]) for the functions of (eq:I-t) (was I_t); ℐ_K for the index set (was I_K).
- Tail T_R → Ξ_R; τ, σ in Lemma A.1 and (S-remainder) → t̂, ŝ; E_K(m) (Remark 6.4, Lemma A.4) → 𝓔_K(m); density d_m → δ_m; c_a → 𝖼_a; Fejér-side h(x) → υ(x) and Δ⁴h → Δ⁴υ (h_a stays for the Chebyshev moments); Lemma 5.5's H_q(u) → Y_q(u) (H_q is now the harmonic number); Thm 7.1: g → 𝔤, κ → κ₀, d (dimension) → dim 𝒫_n, ν → ν_Ch.
- Prop 8.1 proof: ϱ(r,s) → 𝒬(r,s); distances A, B → r̄, s̄; matrices H, Q → 𝖬, 𝖬^P; B_t → Â_t; d_t → 𝖽_t. Prop 8.2 proof: N (squared norm) → ‖p‖². Lemma A.4: N = |𝒵| → N_𝒵; psd A, B → Y₁, Y₂; partial isometry W_m → 𝖴_m. B.2: ρ₁, ρ₂ → ℓ₁, ℓ₂; B.1/Prop 6.7: eigenfunction u → f₀; W_x → 𝒜_x. Prop 6.8: Q_i → Γ_i, F → ℱ. Prop 6.9 and B.5: L, U → r̲, r̄. A.3: β_K(m) → 𝖻_K(m). A.2 Step 3: Π_{kl} → Λ_{kl}. §5 (Thm 5.1 proof): "mesh denominator M, halfweights c_j, cosine polynomial h" → mesh with N ∈ {m,m+1} intervals, ε^{(N)}_j, f; h_r → Ψ_r; D_m → N_m. §8.3 fit parameters α, β → s₀, s₁.
- Not renamed (accepted local reuse, listed in the register update): U (cube size, rectangles U×V, U₋), r (‖B‖ and local), S, c_t/c_l/c_{jk}, P, F (Fejér F_r), σ, H_{m,n}, the integers n in Σ_t^ϱ (Fourier index).
- Register `notation-sp.md`: the two wrong entries corrected (Π_n listed as the total-degree space → 𝒫_n bivariate, Π_n univariate; η removed from the locally reusable letters), all renames above added as rows, and the accepted local reuses listed.

### Literature (E, F)

- E #6 (KLP18): wording replaced as the referee proposed ("recorded by [KLP18, Lemma 5.1] (for 1<p<∞ taken from Erb)… anisotropic interpolation space, with unspecified constants"); Erb is named in the text but not added to the bib (no record read).
- E #11 (ASV27, §8.1): replaced by "…report η<1 up to n=m−1 for a Padua-based cubature rule for Lebesgue measure with degree of exactness m ≤ 20. If that rule is the interpolatory rule studied here, the brackets certify their observation at m=10,20 and extend it to m=30,40,60,80." The conditional stays until AC confirms the rule from the PDF.
- E #3 (Xu96 "different polynomial space" note) and #4 ("(33) and (36)"): optional, not applied.
- F: the DOI checks (BCDMVX06, Xu96) remain for AC.

### Other items (G, H, I)

- G: see Deferred. H: placeholders (author names, commit, Zenodo DOI, "DOI to be added", `\date`, affiliations, CRediT, declarations) untouched (AC-reserved). I: cuts done as instructed (secant paragraph, data condensing, integers moved); the paper grew by 3 preprint pages because of the additions (introduction, §§4–7 openings, Table 1, definitions), more than the 1.5 to 2 pages estimated.

## Deferred to AC

1. **Unread items the referee wanted cited (not cited, not in the bib)**:
   - Caliari–De Marchi–Vianello 2005, Appl. Math. Comput. 165, 261–274 (origin of the Padua points): DOI [10.1016/j.amc.2004.07.001](https://doi.org/10.1016/j.amc.2004.07.001); free PDF [CDMV05.pdf](https://profs.scienze.univr.it/caliari/pdf/CDMV05.pdf).
   - Sloan 1995, J. Approx. Theory 83, 238–254 (hyperinterpolation): [doi:10.1006/jath.1995.1119](https://doi.org/10.1006/jath.1995.1119).
   - Bos–De Marchi–Vianello–Xu 2007, Numer. Math. 108, 43–57 (ideal theory; LIT-313 read only at excerpt scope): [arXiv:math/0604604](https://arxiv.org/abs/math/0604604), DOI to verify (probably 10.1007/s00211-007-0112-z).
   - Caliari–De Marchi–Vianello 2008, J. Comput. Appl. Math. 221, 284–292 (four families related by symmetries; LIT-330 preprint §2 read): [doi:10.1016/j.cam.2007.10.027](https://doi.org/10.1016/j.cam.2007.10.027).
   - Caliari–De Marchi–Sommariva–Vianello, Padua2DM, Numer. Algorithms 56 (2011) 45–60 (software; LIT-368 secondary, UNVERIFIED): preprint [preCDMSV09.pdf](https://profs.scienze.univr.it/caliari/pdf/preCDMSV09.pdf).
   - Erb 2016, Appl. Math. Comput. 289, 409–425 (source of KLP's L^p inequalities): [arXiv:1503.00895](https://arxiv.org/abs/1503.00895).
   - Sentences the referee proposed that depend on them (origin of the points, "four families", Sloan's definition, software) were therefore not added. If AC reads them, the intro paragraph and the §7 opening are the places.
2. **An–Ran–Wu survey (LIT-387)**: its §2.3 sentence on positive hyperinterpolation on Padua points was not used (outside the permitted sources; the record warns against citing it as saying the signed case is open or closed). [doi:10.25430/pupj-DRNA-2025-1-11](https://doi.org/10.25430/pupj-DRNA-2025-1-11).
3. **ASV27**: the page locator of the Padua experiment and whether their rule is Q^P_m (PDF `1-s2.0-S0378475426004416-main.pdf`, [doi:10.1016/j.matcom.2026.10.001](https://doi.org/10.1016/j.matcom.2026.10.001)); then drop the "If that rule is…" conditional in §8.1.
4. **Classical citations**, if AC wants them: Szegő, *Orthogonal Polynomials*, Thm 8.1.1, [DLMF 18.11](https://dlmf.nist.gov/18.11) and [DLMF 10.9](https://dlmf.nist.gov/10.9) (Mehler–Heine; Laplace and Poisson integrals); Reed–Simon IV §XIII.12 (Jentzsch/Krein–Rutman); Bhatia, *Matrix Analysis*, X.1 (‖A^{1/2}−B^{1/2}‖ ≤ ‖A−B‖^{1/2}, sharper than the 4√δ/π proved in Lemma A.4, which was kept).
5. **DOIs to resolver-check**: BCDMVX06 [10.1016/j.jat.2006.03.008](https://doi.org/10.1016/j.jat.2006.03.008) (the record has only the preprint URL), Xu96 [10.1006/jath.1996.0102](https://doi.org/10.1006/jath.1996.0102).
6. **Submission items**: MZ-CC arXiv id in the bib; confirm that `aacchhee/padua_research` is public, or give only the Zenodo DOI; commit hash and Zenodo DOI; "DOI to be added" after Prop 8.2; author names, affiliations, CRediT, declarations, `\date`; optional curated `paper-sp/code/` or deposit README (B15a); MSC 47B38/65G20 (B18).
7. **Optional A.2 Step 1 shortening** (about 0.8 page) and **Prop 5.8 demotion** (about 0.4 page) remain available if AC wants a shorter paper; both were declined by the orchestrator.
8. **Candidate for a future registered claim (B6, declined here)**: |λ^P_±(m,⌊τm⌋)| ≍ log m for every fixed τ ∈ (1/2,1). Sketch from the referee: carriers of Prop 5.6 with a+b small have degree below τm, so the lower bound follows from Cor 5.3-type carriers; the upper bound |λ^P_±(m,n)| ≤ 120 log R + 4096 for n < m follows from Thm 6.1 by restriction. It needs a register entry and a check before use. The related open question (does λ^P_±(m,⌊τm⌋)/log m converge, presumably to the extremes of the analogous operator on {a+b ≤ τ}?) could then be added to §9.
9. The referee's optional figure of m⁴w_{jk}/log m near (1,1) was not made; it would be a computation, not a proof.

## Process note

I made every edit by scripted exact-string replacement and range-restricted renames (scripts in `/tmp/sp-edit/`, not part of the repository), compared the result against the head copy, and rebuilt after each batch. One scripted rename needed manual fixes (spacing after `\le`, `\R^{N_𝒵}`, `B⁻f₀ = rf₀`), found by reading the diff.
