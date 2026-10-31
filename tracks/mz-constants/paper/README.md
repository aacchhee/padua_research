# M7 complete proof manuscript

Title: *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness*.

This is a complete 14-page development draft with proofs and bibliography, not a submission-ready paper. The independent Astra audit accepted the analytic M1/M2/M3 claims within its recorded scope. The required Claude cross-provider audit is **PENDING**. Historical novelty remains unresolved because the named interpolation/MZ full texts have not been checked. The draft makes no first-proof claim. Authorship and venue remain AC's decisions.

- [LaTeX source](manuscript.tex)
- [Bibliography](refs.bib)
- [Local compiled PDF](../../../local-output/mz-constants/paper/manuscript.pdf) (ignored, regenerable; external archival pending AC's destination)
- [Development/readiness record](../../../topics/mz-constants/directions/M7/manuscript-record.md)
- [Independent scientific audit and source-reading coverage](../../../topics/mz-constants/independent-astra-01.md)
- [Literature search and unresolved full-text gaps](../../../topics/mz-constants/literature-search.md)
- [Final ID allocation map](../../../topics/mz-constants/final-id-map.json)

Only final PD/LIT identifiers occur in the manuscript and bibliography. The manuscript synthesizes the accepted analytic claims; writing it does not upgrade audit, historical novelty, or the OPEN sharpenings. No private theorem or third-party full-text extract is included.

## Mathematical scope

| Manuscript content | Durable claim | Scope |
|---|---|---|
| Exact CC weights, aliasing, parity exactness | PD-T013 | N indexes N+1 nodes; ADE is N for odd N, N+1 for even N |
| Upper spectrum below two and coefficient floor | PD-T014, PD-T015 | Complete Z-matrix sign-comparison and telescoping proofs through degree N−1 |
| Full-degree T_N obstruction | PD-T016 | Explicit quotient greater than two at degree N |
| Endpoint lower and upper comparisons | PD-T017, PD-T018 | Complete weighted cardinal-cell Schur and parity-compatible harmonic-U proofs; lambda_min has order (1+log N)^−2 |
| Exact U witness and three-quarter counterexample | PD-T019, PD-N004 | N=512, 513 points, degree n=511; conditional An–Wu theorem remains valid |
| Fixed-ratio upper/lower bounds and strong constants | PD-T022–PD-T024 | Complete explicit filtered Fejér weighted Schur proof; every fixed theta<1 |
| Hyperinterpolation application | PD-T025 | Positive rules, stated reproduction degree; uniform CC error factor (1+sqrt(2))*sqrt(V). Generic upper-Gram mechanism already appears in ASV |
| Padua marginal/compression | PD-T021 | Exact marginal 2w_CC and isometric compression, valid for signed weights; only liminf eta_Padua>=1 |
| Numerical tables | PD-T026 (MEASURED) | CC N=40,...,1280; Padua construction degrees 10,20,30,40; independent replay recorded separately |
| Retained sharpenings | PD-T020, PD-T027, PD-T028 (OPEN) | Leading minimum-eigenvalue constant, sharp upper limit/uniform endpoint gap, genuine signed Padua targets |

The CC endpoint defect tends to one, and the condition number has logarithmic squared order. The draft does **not** assert a logarithmic squared rate for `1−eta` or eventual binding of the minimum-eigenvalue side; the proved upper gap is insufficient for those claims. The decimal near 1.004437 is a measured lead, not a proved limit. No N=20480 run is claimed as reproduced.

## Build and checks

Run from the repository root `/workspace/padua_research`:

```sh
mkdir -p local-output/mz-constants/paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex
BIBINPUTS=tracks/mz-constants/paper: bibtex local-output/mz-constants/paper/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex
```

The complete sequence was executed successfully on 2026-10-31, followed by incremental recompilation after wording/metadata and bibliography-coverage edits. Tool versions: pdfTeX 3.141592653-2.6-1.40.26 and BibTeX 0.99d, TeX Live 2025/dev/Debian. Final-pass log and BibTeX log contain no warnings, overfull/underfull boxes, undefined citations/references, or TeX errors. Initial passes had the expected unresolved references before BibTeX and repeat LaTeX passes; those were resolved.

The PDF has 14 A4 pages. Pages 1 and 9 were rendered with `pdftoppm` and visually inspected for layout before the final wording/metadata edits; the final compilation was checked again by its logs. No plot or heavy numerical run was needed for manuscript synthesis. Local build artifacts, rendered pages, text extraction, and the build manifest stay under ignored `local-output/mz-constants/paper/`.

Final artifact SHA-256 identities and byte sizes are recorded in `manuscript-record.md` and the ignored `build-manifest.json`. PDF byte hashes can change on rebuild because TeX embeds timestamps and an output identifier; the source hashes identify the retained draft.

## Numerical provenance

Tables are transcribed, rounded, and checked against [the bounded reproduction](../evidence/reproduction.json) and [its durable measured record](../theory/reproduced-spectra.md). The manuscript worker reviewed these existing outputs; it did not rerun the numerical suite and does not call that review an independent execution.

The producer command, already executed by the reproduction developer and separately replayed by Astra, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output tracks/mz-constants/evidence/reproduction.json
```

Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0 are recorded in that output. The separate replay and comparisons are linked by the independent audit. Finite agreement and signed Padua tables remain MEASURED. The universal results use the written analytic proofs.

## Review handoff

The manuscript itself was not part of the earlier scientific proof pin. Its translation of those proofs needs an impact review against the source hashes in the manuscript record. Required Claude audit and complete historical duplicate comparison remain pending. No submission, publication, merge, or external archival is authorized or claimed by this directory.
