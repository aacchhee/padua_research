# Topic report — MZ prior-art and fulltext closure

Claude Opus 5.5 (orchestrator), 2026-11-01, rules `9739a0c` (unchanged at `64c3c79`). Codex audit-01: CHANGES REQUIRED; answered in [response-01](response-01.md); focused re-audit **PENDING**. Literature topic: no PD status changes.

## What is now verified

- **Read in full or in the relevant parts**:
  - fulltext via AC's NTNU access: Askey 1972 (journal), Sloan–Smith 1978 and 1980 (the latter section- and keyword-screened in full in response-01), Lubinsky 1999 (published), Mastroianni–Totik 2000, Lubinsky 1998 survey, Mastroianni–Milovanović ch. 2/4/5, Mastroianni–Russo 1999, An–Wu (published);
  - open texts: Smith 1986, Nevai III, Widom, Widom–Wilf, König–Nielsen (arXiv), Don–Gottlieb (ICASE), Niu et al.
- **Translations written as proofs** ([translation.md](translation.md)): λ_− = 1/‖L_N‖² for the CC-weighted nodal ℓ²→L²(dx) norm; CC weights ≍ √(1−x²)/N + 1/N² (factors ½ and 5); the Mastroianni–Totik consequence (no stronger than exactness); why Lubinsky's theorem stops at the CC borderline; the Mastroianni–Milovanović–Notarangelo specialization (T6).
- **Per-claim verdicts**: [comparison.md](comparison.md).

## What each fulltext changed

| Source | Change |
|---|---|
| Mastroianni–Totik 2000 | First recorded as IMPLIES PART. After audit-01 F1 it is **RELATED**: its CC window n≤N/(πM), with admissible M≥1, lies inside half-exactness, where exactness already gives λ_±=1. Manuscript §1 and §4 now say so. |
| Mastroianni–Russo 1999 (LIT-293), König–Nielsen (LIT-294), Xu (LIT-296) | Analogous classical borderline phenomena (Gauss nodes or same-weight). After audit-01 F4 they are no longer used to attribute the CC statement. |
| Mastroianni–Milovanović–Notarangelo 2012 (LIT-299, audit-01 lead) | The closest classical statement: Jacobi zeros plus ±1. At CC, Lebesgue, p=2 its strict condition fails at the endpoint, so inf_N λ_−(N,N)=0 on Π_N is classical (T6; necessity proof unaudited). No rate, no every-N limit, nothing on Π_{N−1}. |
| Lubinsky 1999 | The "right form" concern is resolved: the CC/Lebesgue case is exactly the excluded endpoint σ=1/2. |
| Nevai III, Askey, Smith, Erdős–Feldheim | Uniform-input theorems: RELATED, DIFFERENT SETTING. Nevai's quasi-Lagrange theorem does include the CC nodes. |
| Sloan–Smith, Widom, Widom–Wilf, Don–Gottlieb, the Mastroianni–Milovanović book | Different norms or matrix problems in the inspected portions; coverage is per source. |
| An–Wu published | PD-N004 reading confirmed against the published Corollary 4.1. |
| Lubinsky–Máté–Nevai 1987 (AC-supplied) | Forward inequality: at CC it gives λ_+≤C (unspecified) for all degrees ≤lN. Uniform boundedness of the upper constant is classical; our <2 threshold and explicit constants are not implied. Manuscript §1 now says so. |
| Xu I/II (AC-supplied, OCR) | Sufficient conditions at Gauss nodes; the same borderline obstruction as Mastroianni–Russo; sharpness open (Xu's Remark 3.1). |
| Nevai 1990 | Justifies one step of Nevai III; no change. |
| Sloan–Smith 1982, Smith–Sloan 1980 | Uniform-input / weight-sum results: RELATED. |
| Published ASV | Numerical. It adds an eigenvalue characterization and a Gaussian-rule η≥1 theorem, and states that the CC behaviour beyond half-exactness is, to the authors' knowledge, not known theoretically (p. 738). |

## Is the endpoint log-rate result classical?

**In part.** That λ_−(N,N) is not bounded below at the CC nodes on the full space Π_N is classical: Mastroianni–Milovanović–Notarangelo 2012 Cor. 2.2, necessity part (translation.md T6). Analogous Gauss-node and same-weight borderlines are in Mastroianni–Russo, Xu and König–Nielsen. The every-N limit on Π_{N−1} and the 1/log N rate come from our exact U_{N−1} evaluation (PD-T019). The **two-sided order** λ_−(N,N−1) ≍ (1+log N)^{−2} with CC weights, and the PD-T018 log² witness inside Π_{N−1}, were not found in the documented search. That search is not exhaustive. Xu I/II have now been read (no quantitative borderline). Mastroianni–Russo 2000 is the most likely remaining place.

## What remains missing

Mastroianni–Russo 2000 (Hadronic Press, no online copy), Della Vecchia–Mastroianni–Vértesi 1995 (IDOMAT proceedings), Wu (Appl. Math. Lett. 182, 2026), the journal versions of König–Nielsen and Don–Gottlieb, and Feldheim C. R. 203 p. 650. AC supplied the other SIAM/ScienceDirect items the same morning; they are read and recorded. The list for AC is in the local working track `Downloads\padua\results\mz-prior-art-20261101.md`. Bot checks at ScienceDirect and SIAM block the automated browser.

## What to tell ASV (no contact made)

- **Theirs**: the question, the weak/strong MZ distinction, the finite CC/Padua experiments beyond half-exactness, and the generic upper-Gram hyperinterpolation estimate (their eq. (7)).
- **Their own published assessment**: the CC behaviour beyond half-exactness is "not known" theoretically (MCS 252, p. 738).
- **New relative to them** (proved here, self-contained): the all-N CC upper constant 2−4/N+4/N² below 2 on Π_{N−1}; the endpoint order (1+log N)^{−2} for λ_min, both sides; explicit strong constants for every fixed ratio θ<1; the exact Padua marginal compression; and the N=512 certificate that η≤3/4 fails at the endpoint (relevant to An–Wu's assumed η).
- **Classical context to acknowledge**: Mastroianni–Milovanović–Notarangelo for the qualitative full-space failure at CC nodes; Lubinsky–Máté–Nevai for boundedness of the upper constant; Mastroianni–Russo, Xu and König–Nielsen for analogous borderlines.
- **Questions for them**: whether the An–Sommariva–Xue manuscript ("MZ stability under relaxed quadrature exactness") already contains any all-N CC bound; whether they know of a quantitative borderline converse-MZ result (Xu, Mastroianni–Russo 2000); and how their published version differs from arXiv v1.
