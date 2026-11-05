# MathSciNet citation check for the priority-critical sources (2026-11-05)

Purpose: harden the "no matching result found in the documented search" verdicts of P1/P2. Earlier searches used Crossref, arXiv, author pages, reference lists and web search, but not MathSciNet. Done after response-01; no verdict changed.

## Forward citations

- **Kolomoitsev–Lomako 2021** (AMC 403, 126192): AC found one citing paper in MathSciNet, namely Y. Kolomoitsev, E. Liflyand, *Asymptotics of the Lebesgue constants for a d-dimensional simplex*, Proc. AMS 149(7) (2021) 2911–2926, [doi:10.1090/proc/15438](https://doi.org/10.1090/proc/15438). AC supplied it as `S0002-9939-2021-15438-5.pdf`; Claude read it. Record [kolomoitsev-liflyand-2021](../../../literature/records/kolomoitsev-liflyand-2021.md). Verdict: RELATED, DIFFERENT SETTING (Fourier partial sums over a simplex; not interpolation, not pointwise, remainder O(log log n₁ · log n₂)).
- **De Marchi 2022** (CMA 5, MR4410201): **0 citations** (AC, 2026-11-05). AC's MathSciNet check returned no indexed citing item for the open-problems list that holds the corner observation. This is a statement about that index query only, not evidence that no citing work exists: the index is incomplete (see Kuznetsova below), and Google Scholar and zbMATH were not searched. (Wording narrowed in response-02 to audit-02 F7; the earlier sentence inferred that nothing citing it had been published.)
- **SVZ 2008** (Numer. Algorithms 49): 9 citing items (AC's MathSciNet list). Triage:

  | Citing item | Check | Bearing |
  |---|---|---|
  | Caliari–De Marchi–Sommariva–Vianello, *Padua2DM*, Numer. Algorithms 56 (2011) 45–60, [doi:10.1007/s11075-010-9373-1](https://doi.org/10.1007/s11075-010-9373-1) | full-text keyword scan (Springer via NTNU) | p. 54: Padua cubature weights are not all positive, the negative ones are few and small, and the limit of Σ|λ_ξ| is 4 "as proved in" SVZ. p. 59: CC-like cubature behaviour is still unexplained in several variables. No identification of which weights are negative, and no formula. PD-T111: RELATED (unchanged). |
  | De Marchi–Vianello–Xu, *New cubature formulae and hyperinterpolation in three variables*, BIT 49 (2009) 55–73, [doi:10.1007/s10543-009-0210-7](https://doi.org/10.1007/s10543-009-0210-7) | full-text keyword scan | 3-D nontensorial CC-like cubature; no statement on negative weights or exactness beyond construction. RELATED, DIFFERENT SETTING (3-D). |
  | Bos–De Marchi–Vianello, *Trivariate polynomial approximation on Lissajous curves*, IMA J. Numer. Anal. 37 (2017) 519–541 | title/MSC only | 3-D Lissajous; not read. |
  | Festa–Sommariva, *Computing almost minimal formulas on the square*, JCAM 236 (2012) 4296–4302 | title/MSC only | positive almost-minimal formulas; not read (ScienceDirect). |
  | Cools–Poppe, *Chebyshev lattices*, BIT 51 (2011) | already in the repo (LIT-004) | no change. |
  | Poppe–Cools, *CHEBINT*, ACM TOMS 40 (2013) | title only | software. |
  | Sommariva–Vianello 2009 (Fekete points); Fenzi–Michiels 2019 (eigenvalue functions); Themistoclakis–Van Barel 2024 (kernel method) | title only | cite SVZ as a tool; outside scope. |

- **Kuznetsova 1995** (MR1353627): MathSciNet shows **0 citations** from references, although KL 2021 and Kolomoitsev–Liflyand 2021 both cite it (checked in their reference lists). MathSciNet's citation index is therefore incomplete for this paper, so a zero there is weak evidence.
- **Pimenova 1979** (MR0553982): 0 indexed citations (`cp:553982`).

## Keyword search

MathSciNet all-fields search "Padua points Lebesgue" returned 8 items. Five are already in the repository: De Marchi 2022; KL 2021; Bos et al. 2006; Caliari et al. 2005; Meurant–Sommariva 2019 (AC copy `1-s2.0-S0377042718304035-main.pdf`, unit disk). The three new items:
- Carnicer–Godés, *Multivariate polynomial interpolation using even and odd polynomials*, BIT 58 (2018) 27–49, [doi:10.1007/s10543-017-0674-9](https://doi.org/10.1007/s10543-017-0674-9). Per the MathSciNet review: Lebesgue constants of even/odd subproblems on subsets of the Padua set. No location statement in the review; full text not read.
- Vianello, *Dubiner distance and stability of Lebesgue constants*, J. Inequal. Spec. Funct. 10 (2019) 49–60 (review read): perturbation stability. RELATED.
- Suryanarayana–Cools–Nuyens (Fibonacci lattices): not relevant.

## Conclusion

No published proof of the Padua corner-maximum statement, and no corner-value lower bound, second term or exact corner formula, was found in MathSciNet either. The P1/P2 verdicts stand. The searches remain non-exhaustive: Google Scholar and zbMATH full text were not used, and MathSciNet's citation index is incomplete for older Russian papers.

Checks by Claude (claude-opus-5-5 high) in the built-in browser on AC's computer via NTNU access; AC's own MathSciNet checks as reported in chat.
