# M7 complete proof manuscript

Title: *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness*.

This is a complete development draft with analytic proofs, finite computer-assisted illustrations, and bibliography (25 A4 pages after the 2026-11-05 signed-Padua and cleanup-result integration), not a submission-ready paper. The new manuscript integration and cleanup results are pending the required Claude audit; the even-degree source results and uniform operator bound were accepted in PR #23. Independent Astra reconstruction and Claude audits 01–02 accepted the analytic M1/M2/M3 claims and scientific response within their recorded scopes. Codex audit-03 closes the literature-response corrections and final integration checks for PR #11. Historical priority remains screened, not cleared: the classical result is a qualitative full-space consequence conditional on its cited source; the single-U upper bound and the separate squared-log theorem are distinguished. The documented search is non-exhaustive and its source-specific reading limits remain. Authorship and venue remain AC’s decisions.

- [LaTeX source](manuscript.tex)
- [Bibliography](refs.bib)
- [Preserved original v1 PDF](../../../local-output/mz-constants/paper-v1-preserved/manuscript.pdf) and [preservation manifest](../../../local-output/mz-constants/paper-v1-preserved/preservation-manifest.json) (ignored; external archival pending AC's destination)
- [Response-01 PDF destination](../../../local-output/mz-constants/paper-response-01/manuscript.pdf) (compiled after all scientific and literature response edits; 15 A4 pages)
- [Development/readiness record](../../../topics/mz-constants/directions/M7/manuscript-record.md)
- [Independent scientific audit and source-reading coverage](../../../topics/mz-constants/independent-astra-01.md)
- [Literature search and unresolved full-text gaps](../../../topics/mz-constants/literature-search.md)
- [Final ID allocation map](../../../topics/mz-constants/COLD_STORAGE.md)

Only final PD/LIT identifiers occur in the manuscript and bibliography. The manuscript synthesizes the accepted analytic claims; writing it does not upgrade audit, historical novelty, or the OPEN sharpenings. No private theorem or third-party full-text extract is included.

## Mathematical scope

| Manuscript content | Durable claim | Scope |
|---|---|---|
| Exact CC weights, aliasing, parity exactness | PD-T013 | N indexes N+1 nodes; ADE is N for odd N, N+1 for even N |
| Upper spectrum below two and coefficient floor | PD-T014, PD-T015, PD-T022 | Endpoint bound lambda_plus(N,N−1)≤2−4/N+4/N² from PD-T022; N=2 exact value 1, N≥3 strict. Retained independent qualitative sign proof and mass-floor inequality/alternative weaker bound 2−2/(pi N) |
| Full-degree T_N obstruction | PD-T016 | Explicit quotient greater than two at degree N |
| Endpoint lower and upper comparisons | PD-T017, PD-T018 | Cardinal lower bound on the full space Π_N, hence Π_(N−1); harmonic-U upper comparison on Π_(N−1), giving order (1+log N)^−2. The constant 128000/log²N is below 1 only for log N>sqrt(128000)≈357.7709; finite tables determine no asymptotic leading constant |
| Exact U witness and three-quarter counterexample | PD-T019, PD-N004 | N=512, 513 points, degree n=511; conditional An–Wu theorem remains valid |
| Fixed-ratio upper/lower bounds and strong constants | PD-T022–PD-T024 | Complete explicit filtered Fejér weighted Schur proof; every fixed theta<1 |
| Hyperinterpolation application | PD-T025 | Positive rules, stated reproduction degree; B=1+rho_(N,n) and uniform CC error factor (1+sqrt(2))*sqrt(V). Generic upper-Gram mechanism already appears in ASV |
| Padua marginal/compression | PD-T021 | Exact marginal 2w_CC and isometric compression, valid for signed weights; retained as the first subsection of §6 |
| Signed Padua weight limit and carriers | PD-T295, PD-N105–PD-N107 | Full proofs: even-m fixed-node logarithmic weight asymptotics with whole-grid domination; opposite-sign polynomial carriers; both Gram extrema diverge at every fixed ratio above 1/2 along even m |
| Both-parity completion | [odd weight theorem](../../../topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md), [odd carriers](../../../topics/padua-mz-cleanup-20261105/theory/odd-carriers.md) | Odd-m fixed-index limit and majorant; carriers use the even y mesh m+1; endpoint and every fixed ratio >1/2 have extrema diverging over all integers m. Analytic development, Claude audit pending |
| Normalized growth bounds | [exact carrier norms](../../../topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md) | Explicit one-sided bounds with exact integral constants; raw 1/9 and 1/36 are energy coefficients, not normalized spectral constants. No sharp law claimed |
| Finite negative witness | [finite indefiniteness](../../../topics/padua-mz-cleanup-20261105/theory/finite-indefiniteness.md) | m1101,1240,1600 dyadic Legendre polynomials with negative rational trial-Rayleigh intervals; producer and separate forward-error checks. Computer-assisted development, Claude audit pending |
| Uniform signed coefficient operator | PD-T297 | Full weighted-L1/density-tail proof; every m≥2 and 0≤n<m; 2≤norm≤28.3763348311…<30, independently of signed Gram positivity |
| Exact finite Padua illustrations | PD-T298, PD-T299 | Strict rational brackets at m=60 and m=80; computer-assisted inertia reduction and repository checker trust are explicit |
| Numerical tables | PD-T026 (MEASURED) | CC N=40,...,1280; Padua construction degrees 10,20,30,40; independent replay recorded separately |
| Retained sharpenings | PD-T020, PD-T027 (OPEN) | CC leading minimum-eigenvalue constant and sharp upper limit/uniform endpoint gap; sharp Padua growth constants, first finite crossing/effective onset estimates, and sharp operator norms remain separate quantitative tasks |
| Rejected signed Padua conjectures | PD-T028, PD-T110, PD-T116 | Registry status OPEN is retained by AC, with binding REJECTED: refuted dispositions; positive endpoint orders, all-m positivity, upper threshold, and defect convergence to one must not be relied on |

The CC endpoint defect tends to one, and the condition number has logarithmic squared order. The draft does **not** assert a logarithmic squared rate for `1−eta` or eventual binding of the minimum-eigenvalue side; the proved upper gap is insufficient for those claims. The decimal near 1.004437 is a measured lead, not a proved limit. No N=20480 run is claimed as reproduced.

## Build and checks

Run from the repository root `/workspace/padua_research`:

```sh
mkdir -p local-output/mz-constants/paper-response-01
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper-response-01 tracks/mz-constants/paper/manuscript.tex
BIBINPUTS=tracks/mz-constants/paper: bibtex local-output/mz-constants/paper-response-01/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper-response-01 tracks/mz-constants/paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper-response-01 tracks/mz-constants/paper/manuscript.tex
```

The original v1 sequence, using `local-output/mz-constants/paper/`, was executed successfully on 2026-10-31, followed by incremental recompilation after wording/metadata and bibliography-coverage edits. The commands above use a distinct response-01 destination; that new build was executed successfully after integration of the scientific and literature response edits. Tool versions: pdfTeX 3.141592653-2.6-1.40.26 and BibTeX 0.99d, TeX Live 2025/dev/Debian. Final-pass log and BibTeX log contain no warnings, overfull/underfull boxes, undefined citations/references, or TeX errors. Initial passes had the expected unresolved references before BibTeX and repeat LaTeX passes; those were resolved.

The preserved original v1 PDF has 14 A4 pages. Pages 1 and 9 were rendered with `pdftoppm` and visually inspected for layout before the final wording/metadata edits; the final compilation was checked again by its logs. No plot or heavy numerical run was needed for manuscript synthesis. Local build artifacts, rendered pages, text extraction, and the build manifest stay under ignored `local-output/mz-constants/paper/`.

The original v1 artifact SHA-256 identities and byte sizes are recorded in `manuscript-record.md` and the ignored original `build-manifest.json`; the preserved PDF has SHA-256 `a594ea305fc0f91bb3a2c49d9c6311288440fcffa6eb9e1e95177748d34d3155` (419412 bytes). The ignored preservation manifest records its copied source, bibliography, README and original build manifest. Response source hashes and the explicit statement changes are recorded in `topics/mz-constants/scientific-response-01.md`; the integrated response build and exact artifact identities are recorded below. PDF byte hashes can change on rebuild because TeX embeds timestamps and an output identifier; the source hashes identify the retained draft.

## Numerical provenance

Tables are transcribed, rounded, and checked against [the bounded reproduction](../COLD_STORAGE.md) and [its durable measured record](../theory/reproduced-spectra.md). The manuscript worker reviewed these existing outputs; it did not rerun the numerical suite and does not call that review an independent execution.

The producer command, already executed by the reproduction developer and separately replayed by Astra, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output tracks/mz-constants/evidence/reproduction.json
```

Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0 are recorded in that output. The separate replay and comparisons are linked by the independent audit. Finite agreement and signed Padua tables remain MEASURED. The universal results use the written analytic proofs.

## Review handoff

Audit-01 requested the stronger endpoint corollary from PD-T022; the response preserves the original PD-T014 quantitative proof and PD-T015 mass inequality, and updates the headline bound and B=1+rho throughout. That added corollary and its manuscript translation require focused independent re-audit against the response file hashes. Complete historical duplicate comparison remains pending. No submission, publication, merge, or external archival is authorized or claimed by this directory.

## Integrated response-01 build receipt

The root executed the four commands above after integrating M1, M2 and L1–L3. pdfinfo reports 15 A4 pages. The final LaTeX/BibTeX logs have no warnings, undefined references, overfull or underfull boxes. The original v1 PDF remains preserved separately.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| tracks/mz-constants/paper/manuscript.tex | 42631 | c0037cf857895111b98282e400dd4c0af4d87b4cfdc5abba16f53071c58134af |
| tracks/mz-constants/paper/refs.bib | 6321 | ea5fbd9afabb30b090003199084aa1fd3448928dc00538375cc23cd678cae6c5 |
| local-output/mz-constants/paper-response-01/manuscript.pdf | 430932 | a34288ce1a0093c06299ba13ef06d023d11bfd80ace4bbe20535e0200a3a6c83 |

These hashes identify the actual response build; timestamps may change PDF bytes on regeneration. Focused independent review remains separate from compilation.

## 2026-11-01 prior-art revision (topic mz-prior-art-20261101)

Claude Opus 5.5 revised the status line, the last abstract sentence, the §1 related-work paragraph, a remark after Proposition 5.1 (PD-T019/PD-N004), and the opening of §4. It also updated bibliography notes and added LIT-058 and LIT-293–295. No theorem, proof or status changed. Build: `pdflatex; bibtex; pdflatex; pdflatex` on manuscript.tex: no errors and no warnings in the log; 16 A4 pages after the first pass, 17 after the second pass (LIT-050/296–298 added). Page 3 was rendered with pdftoppm and inspected. Build products are not committed. Codex audit of this revision: PENDING.

Response-01 to the PR #11 Codex audit (2026-11-01) revised the abstract's last sentence, the §1 source list (Sloan–Smith coverage, Mastroianni–Totik, Lubinsky–Máté–Nevai constant, Gauss-node versus CC attribution, new LIT-299, survey wording), the §4 opening and the remark after Prop. 5.1. Build: pdflatex/bibtex/pdflatex/pdflatex gives 17 A4 pages with no errors, warnings or over/underfull boxes. manuscript.tex SHA-256 d1ae93ae7044250877b359f560ee9b609d6a87e37a5667e7a0aaab8fb85742b2. No theorem or status changed.

Response-02 (audit-02 R1, 2026-11-01) revised the §1 bullet to separate the single-U upper bound O(1/log N) from the squared-log order (Theorems 3.2/3.3). Rebuilt on the main-merged tree: 17 pp., clean. manuscript.tex SHA-256 aa152cc6d76659934f49b6ecea43bc3cd79676c2ddd2801023937140958888f1.

## PR #11 final readiness (2026-11-01)

[Audit-03](../../../topics/mz-prior-art-20261101/audit-03.md) and [final preparation](../../../topics/mz-prior-art-20261101/pr-prep.md) close the assigned agent work after integrating current main. Earlier dated pending-review lines above are historical build records. The scientific response was accepted in [Claude audit-02](../../../topics/mz-constants/audit-02.md); no mathematical statement, proof or PD status is changed by the present status cleanup. The current manuscript build and hashes are recorded in the final preparation receipt. Only AC decides merge and submission.

## 2026-11-05 signed Padua integration (topic padua-mz-cleanup-20261105)

Section 6 now retains the exact compression and adds the accepted signed-weight asymptotic, both carrier countersequences, the sharp half-exactness ratio threshold, and the uniform direct signed coefficient norm. The abstract, introduction and section 7 distinguish these conclusions from the remaining quantitative questions. The finite m60/m80 brackets are explicitly computer-assisted illustrations, rather than asymptotic premises. Bibliography content is unchanged; no unmerged PR #21 source or historical priority claim was added. Thus no `% LIT pending PR21` sentence is needed. This pass contains no new C1 finite-witness or C2 odd-m claim.

The manuscript worker executed the following in the sandbox, preserving original v1 and response-01 artifacts:

```sh
mkdir -p /tmp/padua-mz-cleanup-paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
(cd /tmp/padua-mz-cleanup-paper && BIBINPUTS=/workspace/padua_research/tracks/mz-constants/paper: bibtex manuscript)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/padua-mz-cleanup-paper tracks/mz-constants/paper/manuscript.tex
```

pdfTeX 1.40.26 and BibTeX 0.99d (TeX Live 2025/dev/Debian) produced 22 A4 pages. Final LaTeX/BibTeX logs have zero warning, overfull/underfull, undefined-reference or error markers. Page 16 was rendered and visually checked; text extraction was also executed. No spectral experiment was rerun by the manuscript worker. Exact source/artifact hashes and claim-to-section mapping are in [manuscript changes](../../../topics/padua-mz-cleanup-20261105/manuscript-changes.md). Build outputs stay under `/tmp/padua-mz-cleanup-paper`; the PDF is not committed or represented as delivered cold storage.

## 2026-11-05 cleanup-result extension (intermediate 24-page build)

The preceding 22-page accepted-result receipt is historical and preserved. The current 24-page draft additionally proves the odd-m weight extension, switches the polynomial carrier to the even y mesh m+1 for odd m, and completes the all-integer divergence and sharp ratio classification. A separate proposition derives the exact continuous carrier norm limits and one-sided normalized logarithmic spectral bounds. It explicitly distinguishes raw energy suprema from normalized Rayleigh coefficients. Section7 includes the m1600 dyadic finite negative witness, its rational trial-quotient interval, the exact-integer/Arb producer and the independent forward-error check under its stated IEEE/BLAS model; the displayed interval is not a minimum-eigenvalue bracket. These cleanup results and their manuscript translation await Claude audit. No m1240 result is included in this build.

The existing build sequence was rerun for the changed source (bibliography unchanged), giving24 A4 pages and zero final warnings, undefined references, overfull/underfull boxes or error markers. Page22 was rendered and visually checked. Current input and PDF hashes are appended in [manuscript changes](../../../topics/padua-mz-cleanup-20261105/manuscript-changes.md); earlier build hashes remain historical. New results are identified by source-path comments until the orchestrator assigns final IDs.

## 2026-11-05 three-witness extension (current build)

The final current draft is25 A4 pages and includes the committed finite certificates at construction degrees1101,1240,1600, each with producer and independent acceptance. The table gives exact rational **trial-Rayleigh** intervals, never minimum-eigenvalue brackets. Construction degree1240 is the smallest even degree certified negative in this campaign, with no assertion of positivity at every smaller degree or first mathematical crossing. The worker inspected the committed finite theory and all six receipts; no independent numerical rerun is claimed by this manuscript translation. The current source/PDF receipt follows the preserved22- and24-page historical receipts in `manuscript-changes.md`. Final compilation and `git diff --check` pass with no warning, undefined-reference or layout markers; final page22 was rendered and visually checked. Bibliography remains unchanged and Claude audit remains pending.
