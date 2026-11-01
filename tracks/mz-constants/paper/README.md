# M7 complete proof manuscript

Title: *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness*.

This is a complete revised development draft (15 pages at response-01; 16 pages after the 2026-11-01 prior-art revision) with proofs and bibliography, not a submission-ready paper. The independent Astra audit accepted the analytic M1/M2/M3 claims within its recorded scope. Claude audit-01 accepted the original mathematical statements. Focused Claude re-audit of the response, including its explicit endpoint corollary, is **PENDING**. Historical priority was screened in topic `mz-prior-art-20261101` (2026-11-01): §1's related-work paragraph now records fulltext-based verdicts (classical qualitative borderline failure and a small-ratio lower bound; no prior two-sided log order or explicit constants found in a documented, non-exhaustive search). Several fulltexts remain pending; see that topic's comparison.md. The draft makes no first-proof claim. Authorship and venue remain AC's decisions.

- [LaTeX source](manuscript.tex)
- [Bibliography](refs.bib)
- [Preserved original v1 PDF](../../../local-output/mz-constants/paper-v1-preserved/manuscript.pdf) and [preservation manifest](../../../local-output/mz-constants/paper-v1-preserved/preservation-manifest.json) (ignored; external archival pending AC's destination)
- [Response-01 PDF destination](../../../local-output/mz-constants/paper-response-01/manuscript.pdf) (compiled after all scientific and literature response edits; 15 A4 pages)
- [Development/readiness record](../../../topics/mz-constants/directions/M7/manuscript-record.md)
- [Independent scientific audit and source-reading coverage](../../../topics/mz-constants/independent-astra-01.md)
- [Literature search and unresolved full-text gaps](../../../topics/mz-constants/literature-search.md)
- [Final ID allocation map](../../../topics/mz-constants/final-id-map.json)

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
| Padua marginal/compression | PD-T021 | Exact marginal 2w_CC and isometric compression, valid for signed weights; only liminf eta_Padua>=1 |
| Numerical tables | PD-T026 (MEASURED) | CC N=40,...,1280; Padua construction degrees 10,20,30,40; independent replay recorded separately |
| Retained sharpenings | PD-T020, PD-T027, PD-T028 (OPEN) | Leading minimum-eigenvalue constant, sharp upper limit/uniform endpoint gap, genuine signed Padua targets |

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

Tables are transcribed, rounded, and checked against [the bounded reproduction](../evidence/reproduction.json) and [its durable measured record](../theory/reproduced-spectra.md). The manuscript worker reviewed these existing outputs; it did not rerun the numerical suite and does not call that review an independent execution.

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

Claude Opus 5.5 revised the status line, the last abstract sentence, the §1 related-work paragraph, a remark after Proposition 5.1 (PD-T019/PD-N004), and the opening of §4. It also updated bibliography notes and added LIT-058 and LIT-293–295. No theorem, proof or status changed. Build: `pdflatex; bibtex; pdflatex; pdflatex` on manuscript.tex: no errors and no warnings in the log, 16 A4 pages. Page 3 was rendered with pdftoppm and inspected. Build products are not committed. Codex audit of this revision: PENDING.
