# Assessment: Faghih–Rinelli–Van Barel–Vandebril–Vermeiren, SIAM J. Numer. Anal. 64(4) (2026) 1190–1216

- Source: "Krylov and Core Transformation Algorithms for an Inverse Eigenvalue Problem to Compute Recurrences of Multiple Orthogonal Polynomials". DOI [10.1137/25M1770965](https://doi.org/10.1137/25M1770965); preprint [arXiv 2506.19796](https://arxiv.org/abs/2506.19796). Received 23 June 2025, accepted 3 Feb 2026, published 9 July 2026. Public MATLAB code: [gitlab.kuleuven.be/numa/public/IEP-MOP](https://gitlab.kuleuven.be/numa/public/IEP-MOP).
- Copy: AC-supplied published PDF `Downloads\padua\papers\25m1770965.pdf` (27 pp.), staged and read by Claude (claude-opus-5-5) on 2026-11-03.
- Coverage:
  - read: §1 (pp. 1190–1193), §3.2 (pp. 1195–1198), §4 headings and §4.2–4.4 (pp. 1198–1203), §5 opening and Algorithm 5.1 (pp. 1203–1205), §6.2–6.3 (pp. 1210–1213), §7 (p. 1213), references;
  - not read line by line: the §2 proofs, the §4.1 proofs and the full §5 worked example.
- This is the existing repository source **LIT-347** (and LIT-119), recorded so far only from secondary notes as UNVERIFIED. The record updates are proposed below. No third-party text is reproduced here.

## What the paper does (paraphrase, with locators)

- Discrete multiple orthogonal polynomials (r = 2 measures on the same N real nodes), step-line recurrence. The recurrence matrix H_N is banded upper Hessenberg with r superdiagonals. Type I and type II MOPs are its right and left eigenvectors (§3.1–3.2).
- Biorthogonality: W^T V = I, with ZW = W H_N^T ⇔ H_N = W^T Z V (eq. 3.16). The first columns of W are recovered from the weights (Thm 3.4, p. 1197, after Van Assche). The IEP is stated as Problems 3.5/3.6 (p. 1197); uniqueness in the monic case is Prop. 4.2 (p. 1201).
- Algorithm IEP_KRYL (§4, Alg. 4.1, p. 1199): biorthogonal Lanczos with multiple starting vectors (type I ↔ block Krylov, type II ↔ standard Krylov). Variants with normalised vectors and (full) reorthogonalisation are in §4.3, and a moment-matrix formulation in §4.4.
- Algorithm IEP_CORE (§5, Alg. 5.1, p. 1205): non-unitary core transformations ("eliminators", 2×2 lower or upper triangular) applied to diag(Z). The steps are elimination, LU biorthogonalisation and chasing to banded form.
- Stability (§6.2, p. 1211):
  - For the Kravchuk and Hahn IEPs (multiple Hahn polynomials), all methods are weakly stable: forward error is comparable to the conditioning error.
  - Backward errors on nodes and weights are measured from the eigen-decomposition of the computed H in quadruple precision.
  - IEP_CORE and IEP_KRYLREORTH(full) are backward stable for most N < 25 and lose this for N ≥ 25. IEP_KRYL is not backward stable for any N considered.
  - On better-conditioned random-weight IEPs (§6.3), IEP_KRYLREORTH(full) gives the best accuracy, at a higher cost (§7, p. 1213).
- Stated future work (§7, p. 1213):
  - a theoretical analysis of the conditioning of the IEP;
  - updating and downdating (the companion arXiv 2608.25758 is LIT-348);
  - an extension of Laurie's continued-fraction approach via vector or branched continued fractions;
  - other recurrence relations, notably nearest-neighbour recurrences;
  - a comparison with Filipuk–Haneczok–Van Assche (2015) and ref. [35].
- No two-variable or bivariate setting is mentioned.

## Corrections to existing records (proposed for PR preparation)

- **LIT-347 / LIT-119.** The record says IEP_CORE "appears backward stable only for N < 25". The published §6.2 (p. 1211) states this for **both** IEP_CORE **and** IEP_KRYLREORTH(full), "for most values of N < 25", with instability for N ≥ 25. IEP_KRYL is never backward stable. Coverage can be upgraded from UNVERIFIED to fulltext-verified for these statements, with the locators above. Add the journal pages and the code URL.
- The record's "authors know no extension of Laurie's approach to MOPs" should be reworded. §7 says extending Laurie's approach is a possibility the paper did not discuss, and points to vector and branched continued fractions. That is not a statement that no extension is known. **Correction 2026-11-05 (response-01, audit-01 F6):** the introduction (p. 1192) does state that the authors are not aware of any extension of Laurie's approach to MOPs. The record's wording is therefore accurate as an author-limited statement and should be kept, with the §7 proposal added. The suggestion above to reword it was wrong.

## Relevance to the Padua IEP / bivariate-recurrence plans

The verdict: of moderate interest. It is not a new campaign by itself. Five concrete uses:

1. **Related work for the bivariate Lanczos and V+A papers.** It is the closest 1-D structured analogue: a nonsymmetric banded Hessenberg recurrence computed by biorthogonal Lanczos versus core transformations, with the same finding as our 2-D results that full reorthogonalisation is needed for accuracy. The contrast is also useful. In 1-D MOPs a backward error is well defined, through the eigenvalues and eigenvectors of the computed H. In 2-D the computed pair need not commute, and PD-T069/PD-N020/N022 show that the analogous exact backward reading fails on Padua points. Cite it in both notes.
2. **Backward-stability test methodology.** Their protocol (a high-precision reference, then backward errors on nodes and weights recovered from the computed recurrence) is a template for measuring the bivariate Givens updating (PD-T077–080, PD-N029–031) and the drift results. In 2-D, nodes are recovered from a nearly-commuting pair, which needs a joint-eigenvalue step. That step is an open design question in its own right.
3. **Their open problem, IEP conditioning, matches our tools.** The exact first-order span sensitivity of the drift campaign (PD-T13x line, PR #15) and the moment-cone conditioning in PD-T058/059 are the kind of analysis they ask for. A conditioning theory for the step-line MOP IEP is a plausible small joint project with Leuven, and the Kravchuk/Hahn ill-conditioning is a natural first test. It is not novelty-gated yet: it must be registered (an IDEA plus a gate) before any work.
4. **Paths in index space.** Step-line versus nearest-neighbour recurrences for MOPs is a choice of path in the multi-index lattice ℕ^r. That is structurally parallel to our one-relation selection rules and staircase selections in bivariate Lanczos (PD-T050/054, the selection principle, PR #15). The existing deferred entry IDEA?bivariate-lanczos-claude-041 (nearest-neighbour MOP IEP, "coordinate with Leuven") is the right home. Note the analogy there rather than opening a new topic.
5. **Core transformations for the bivariate IEP.** The 2010 Van Barel–Chesnokov algorithm uses unitary Givens updating. A non-unitary eliminator variant for generalized-Hessenberg pairs is conceivable. Their N ≥ 25 loss of backward stability with non-unitary eliminators is a warning, so any such variant must be tested against the unitary baseline.

Suggested actions:
- At this topic's PR: correct LIT-347/119, add the journal locators and code link, and cite the paper in the Lanczos and V+A briefs.
- Optionally, register the conditioning idea (point 3) through the novelty gate. Its natural home is a later IEP or Leuven-contact topic, not this literature campaign.
