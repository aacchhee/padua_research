# MZ-SP restructuring plan (task 2)

Target: J. Approx. Theory (`elsarticle`, numeric citations). arXiv and journal versions identical. Cites MZ-CC as a preprint for the CC inputs, with a one-page recap.

## Title and headline

**Title (proposal):** *Marcinkiewicz–Zygmund constants of signed Padua rules beyond half-exactness*.

**Headline:** for the interpolatory (signed) Lebesgue Padua cubature of construction degree m and its Gram form on total degree ≤ n:
1. the factor-two CC marginal and compression: the Padua Gram spectrum dominates the CC one, for every degree-m exact rule, signed or not;
2. exact half-exactness threshold: at every fixed ratio n/m > 1/2 both extreme eigenvalues diverge (−∞ and +∞), over all integers m; at n ≤ m/2 the Gram matrix is the identity;
3. sharp logarithmic growth at the endpoint: λ_±(m,m−1)/log m → inf/sup σ(B) for an explicit compact selfadjoint corner operator B on L²(triangle, ab da db), with ‖B−B_K‖ ≤ 120/K, an elliptic-integral kernel, c₋=−‖B‖ simple and 0<c₊<‖B‖; certified 0.01316 ≤ ‖B‖ ≤ 0.47781 (no useful digits);
4. nevertheless the direct signed hyperinterpolation operator has C→L² norm ≤ 28.38 uniformly.

## Abstract (≈ 200 words)

Results 1–4 with scope; the signed weights' logarithmic boundary asymptotics as the mechanism; what is open (decimal values of c±, first crossing, effective onsets). Positive Padua/Chebyshev cubature and tensor CC are not covered.

## Outline, location of each result, target length

Target: about 28–32 pages in `elsarticle` preprint 12pt (JAT has no strict limit). Current SP baseline: 11 A4 pages in `article`.

| § | Content | Results (IDs) | Source |
|---|---|---|---|
| 1 | **Introduction.** MZ constants beyond half-exactness; Padua points and their signed interpolatory rule (literature: Bos, Caliari, De Marchi, Vianello, Xu, Sommariva; ASV's numerics); why signed weights matter; main theorems up front: Thm 1.1 (compression), Thm 1.2 (threshold), Thm 1.3 (corner-operator limits with properties of B), Thm 1.4 (uniform coefficient norm). Outline. | statements | old abstract + §6 intros |
| 2 | **Clenshaw–Curtis recap and conventions** (≈1 page): CC nodes, weights, Gram notation, the two CC inputs (weight comparison; λ_+<2, λ_−(N,N−1)→0, N=512 value), cited to MZ-CC. Padua support, rule, density lemma d_m. | PD-T101/T111 (lemma) | current §1 + §2.2 |
| 3 | **Marginal compression.** | PD-T021 | old §6.1 |
| 4 | **Signed weights.** Integrated cardinal density; boundary-weight limit and whole-grid majorant, even m (Thm 4.2) and odd m (Prop. 4.3). | PD-T295, PD-T377 | old §6.2 |
| 5 | **Carriers and the exact threshold.** Fejér carriers, even and odd m (Thm 5.1, Prop. 5.2), sharp ratio threshold (Cor 5.3), normalized one-sided bounds (Prop. 5.4), strict improvement within the scalar family (Prop. 5.5) and its global ceiling below 1/24 (Prop. 5.6). Remark on the refuted conjectures (PD-T028/110/116), phrased as "refuted". | PD-N105, PD-N106, PD-T378, PD-N107, PD-T379, PD-T533, PD-T537 | old §6.3 + PR #31 S3-01/S3-04 |
| 6 | **The corner operator and logarithmic limits.** Whole-grid reduction to the logarithmic form L_m (Thm 6.1: errors 4096 and 4300/log m, ‖L_m‖≤120); corner kernel limit (Lemma 6.2, Bessel/Legendre); compact operator B and the limits (Thm 6.3, with explicit finite comparison (4) as a remark); elliptic kernel (Prop. 6.4); positivity improvement, simplicity, c₋=−‖B‖, 0<c₊<‖B‖ (Prop. 6.5); rectangle certificate and the certified enclosure (Prop. 6.6, computer-assisted, "no useful digits" stated). Long proofs in Appendices A–B. | PD-T534, PD-T535, PD-T536, PD-T539, PD-T540, PD-T541, PD-T542 | PR #31 S3/P1 |
| 7 | **A uniform signed hyperinterpolation norm.** | PD-T297 | old §6.4 |
| 8 | **Finite results.** Exact rational brackets m=60, 80 (computer-assisted, PD-T298/299); finite negative witnesses m=1101, 1240, 1600 (PD-T376, computer-assisted; no first-crossing claim); measured spectra (PD-T026 Padua rows), the companion campaign rows (PD-T380) and the PR #31 finite measurements (PD-T538, PD-T543) only as MEASURED, with the explicit statement that finite-window slopes (≈ −0.092) are not the limits. | PD-T298, PD-T299, PD-T376; MEASURED PD-T026, PD-T380, PD-T538, PD-T543 | old §7 + PR #31 |
| 9 | **Open problems.** Decimal values of c± (PD-T381 decimal conjunct OPEN); first sign-change degree; effective onsets; sharp direct-operator norms and endpoint fixed-function convergence. | OPEN | old §7 |
| A | Proofs for §6.1–6.3 (signed whole-grid reduction, kernel lemma, operator limit). | | PR #31 S3 |
| B | Proofs for Props. 6.4–6.6 (elliptic kernel, positivity, rectangle reduction and the exact instance; checker named). | | PR #31 P1 |
| — | Data and code availability; AC-reserved items. | | new |

Development-status box and in-heading PD IDs removed for submission (moved to comments and `correspondence-sp.md`).

## Literature (task 5)

Padua points and cubature literature (from `literature/INDEX.md` and PR #21 records): Caliari–De Marchi–Vianello (2005), Bos–Caliari–De Marchi–Vianello–Xu (2006), Bos–De Marchi–Vianello–Xu (2007), Caliari–De Marchi–Sommariva–Vianello (Padua2DM), Sommariva–Vianello hyperinterpolation papers, ASV (2026), Basor–Ehrhardt LIT-633 if used. Cite only with fulltext-read LIT coverage; otherwise list for AC with DOI links.

## Risks

- The corner-operator proofs (≈ 45 KB of records) are long; Appendix A may run 8–10 pages. Required: every stated theorem proved in the paper.
- Normalization traps: raw energies 1/9 and 1/36 versus normalized Rayleigh constants (PD-T379 note); "two active corners do not double the constants" (PD-T536).
- BRIEF §0 and §2 list PD-T544/545 under "signed Padua log limits". They are the CC signed-remainder and discrete-primitive lemmas (P3, used for π⁴/8) and belong to MZ-CC. The SP corner theorem uses PD-T534/535/536 and P1's PD-T539/540/541/542. Recorded in the LOG.
