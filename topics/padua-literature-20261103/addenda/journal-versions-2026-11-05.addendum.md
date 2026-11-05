# Addendum 2026-11-05: journal versions of A11–A14 (AC-supplied PDFs)

Pass 2 ingest. A Claude Sonnet 5.5 subagent read the four AC-supplied journal PDFs and mapped every locator the repository cites onto journal pages. The orchestrator (Claude, claude-opus-5-5) then spot-checked three items on the PDFs:
- Xu 1996 Theorem 3.3 reads "Let 1 < p < ∞", checked on a rendered image of p. 231;
- CDMV 2007 eq. (13) is on p. 80;
- BCDMVX 2006 Theorem 1 is on p. 19 and Theorem 2 on p. 20.

The free versions were not re-opened in this pass (arxiv.org returned 403 to the subagent). The comparison therefore establishes that **labels and numbering coincide**, and gives journal pages; it does not diff wording.

## A11 — Kolomoitsev–Lomako–Prestin, JAT 229 (2018) 13–35, [doi](https://doi.org/10.1016/j.jat.2018.02.005)

- Record: `literature/records/kolomoitsev-lomako-prestin-2018.md` (LIT?padua-literature-claude-20; this topic's record).
- Coverage: journal pp. 13–35. Pp. 13–26 and 30–35 were read in full; pp. 27–29 (the smoothness lemmas 5.4–5.9) were screened by heading.
- Dates: received 7 Dec 2016, revised 17 Aug 2017, accepted 20 Feb 2018, communicated by A. Kroó.
- Every theorem, lemma and equation label cited in the record (arXiv v1) has the same number in the journal.

| Cited item | arXiv v1 (recorded) | Journal page |
|---|---|---|
| Padua = LC_{n, n+1} remark | p. 2 | p. 14 |
| Theorem 2.1; Theorem 2.2, eq. (2.7) | pp. 3–5 | p. 17 (2.2 continues to p. 18; definitions (2.1)–(2.2) on p. 16) |
| (1.6) HBV rate; mechanism via Lemma 5.10 | p. 3 | p. 15 (Lemma 5.10 on p. 30) |
| LC_{m,n} definition; Proposition 3.1 ("See [10]" = Erb, AMC 289 (2016)) | pp. 5–7 | p. 18 |
| Π^L_{m,n}, Γ^L_{m,n}; weights (3.2); Theorem 3.1 | pp. 6–7 | p. 19 |
| Theorem 3.2 (from DEKL [7]) | — | pp. 19–20 |
| L^p_w; Theorem 4.1 | p. 7 | p. 20 |
| Theorem 4.2; Corollary 4.1; Theorem 4.3 and Remark 4.1; Theorems 4.4–4.5 and Remarks 4.2–4.3 | pp. 8–11 | pp. 21; 22; 23; 24 |
| Lemma 5.1, (5.1)–(5.2), (5.4); Lemma 5.2 | pp. 11–12 | p. 25 |
| Lemma 5.3 (sixfold grid, constant 1/(36mn)) | p. 12 | p. 26 |
| Lemmas 5.10–5.11 | p. 16 | p. 30 |
| §5.6 final remarks | p. 19 | p. 34 |

Additions:
- **Attribution of Lemma 5.1.** (5.1) for all p, and (5.2) for 1 < p < ∞, are quoted from [10] (Erb 2016). The p = 1 case combines (5.3) with (5.4), and (5.4) is itself quoted "from [10] (see also [7])".
- **Padua L^p bound.** The introduction (p. 15) credits the Padua-point bound ‖f − L(f, Pad_n)‖_{L^{p,w}} ≤ C_p E(f, Π²_n)_∞ to [3] = Bos–De Marchi–Vianello–Xu, Numer. Math. 108 (2007). This is a citation inside KLP, not a KLP result.
- **Reference [7].** It is printed incompletely ("J. Complexity 1 (2017)"). The repository's "vol. 43, pp. 1–27" for DEKL is not confirmed by this PDF.

## A12 — Xu, Lagrange interpolation on Chebyshev points of two variables, JAT 87 (1996) 220–238, [doi](https://doi.org/10.1006/jath.1996.0102)

- Records: `literature/lattice-unisolvence/records/xu-1996.md` (LIT?lattice-codex-15); LIT-314 in `topics/padua-mz-2d-20261101/literature.md`.
- Coverage: journal pp. 220–238 in full. Received 26 May 1995, accepted 3 Nov 1995.

| Cited item | Journal page |
|---|---|
| Introduction, choice of space | pp. 220–222 |
| Kernel formulas (2.1)–(2.2); cubature (2.4) (n = 2m) and (2.5) (n = 2m−1) | pp. 223–224 |
| Space V_{2n} (2.11); Lagrange formula (2.12); weights (2.13) | p. 227 |
| Nodes (2.14) (n = 2m), (2.19) (n = 2m−1); K*_n and weights (2.15)–(2.21) | pp. 228–230 |
| Theorem 3.1 (mean convergence, 0 < p < ∞); Corollary 3.2; **Theorem 3.3 (MZ inequality (3.1) on V_{2n}, for 1 < p < ∞)** | p. 231 |
| Lemma 3.4 | p. 232 |
| Lemma 3.5 (forward inequality on Π²_n, 1 ≤ p ≤ ∞) | statement p. 234, proof pp. 234–235 |
| Proofs of Theorems 3.3 and 3.1 | pp. 235–238 |

Correction (proposed below): LIT-314's text "Theorem 3.3 … for 1<p<=infinity" should read **1 < p < ∞**. Only Lemma 3.5 is stated up to p = ∞.

Index note for comparisons with A13: Xu's n is the cubature-degree parameter (degree 2n − 1). CDMV's odd n corresponds to n_Xu = n_CDMV + 1, the (2.14) case.

## A13 — Caliari–De Marchi–Vianello, Hyperinterpolation on the square, JCAM 210 (2007) 78–83, [doi](https://doi.org/10.1016/j.cam.2006.10.058)

- Record: `literature/records/mz2d-caliari-demarchi-vianello-2007.md` (LIT-428).
- Coverage: journal pp. 78–83 in full. Received 12 Sep 2005, revised 24 Jan 2006.
- Every equation (1)–(17), §1–3 and Theorem 1 coincides with the numbering used in the record.

| Cited item | Journal page |
|---|---|
| Hyperinterpolation definition (3)–(4); error and Λ_n (5); measure (6) | p. 79 |
| Xu points for odd n, eqs. (7)–(8) | pp. 79–80 |
| Rule exact on Π²_{2n+1} with weights 2/(n+1)² and 1/(n+1)² (9); kernel (10)–(11) | p. 80 |
| Theorem 1 and the **explicit bound (13)**: Λ_n ≤ 8a_n² + 5a_n + 2 with a_n = (2/π)log(n+1) + 5 | p. 80 (proof continues p. 81) |
| (14); (15)–(17) | p. 81; p. 82 |
| Tables 1–2; 3–4 | p. 81; p. 83 |

Addition: Theorem 1's proof gives only the first step, saying the rest is "very close to" Bos–De Marchi–Vianello, JAT 141 (2006) 134–141. This is a coverage caveat for anyone citing the bound.

## A14 — Bos–Caliari–De Marchi–Vianello–Xu, JAT 143 (2006) 15–25, [doi](https://doi.org/10.1016/j.jat.2006.03.008)

- Records: `literature/lattice-unisolvence/records/padua-2006.md` (LIT-312); LIT-312 in `topics/padua-mz-2d-20261101/literature.md`.
- Coverage: journal pp. 15–25 in full. Received 20 Oct 2005, accepted 3 Mar 2006.

| Cited item | Preprint (recorded) | Journal page |
|---|---|---|
| Curve γ_n and points, eqs. (1)–(3) | — | pp. 16–17 |
| Interior, vertex and edge point formulas; inner product (4) | — | p. 18 |
| Lemma 1; Theorem 1 (weights {1/2, 1, 2}/(n(n+1))) | pp. 5–6 | p. 19 (proof to p. 20) |
| "Precision 2n − 1" remark | — | p. 20 |
| Theorem 2 (L_B = w_B[K_n − T_n(y)T_n(y_B)], (6)–(7)) | p. 8 | statement p. 20, proof p. 21 |
| (9); Lemmas 2–3 | — | p. 21; p. 22 |
| Theorem 3 (Λ ≤ C log² n) | p. 10 | statement p. 22, proof pp. 23–24 |

Notes:
- Theorem 3 gives an order bound only, with no 4/π². This confirms the record's caveat; the constant is Kolomoitsev–Lomako's.
- The orientation swap is already stated in `literature.md`: x has denominator n + 1 here, the repository uses n. The exceptional T_{2n}(y) here is the repository's x-mode.
- The weights are normalized to sum 1 (p. 21).

## Bibliographic data

The bib fragments already carried the correct volume, pages, year and DOI for all four (checked against the printed headers). Their `note` fields were updated in this pass.
- Issue numbers are not printed in the PDFs. The issue numbers 87(2) and 143(1) are confirmed by the A11 reference list; 210(1–2) is unverified.
