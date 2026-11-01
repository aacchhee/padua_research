# M7 manuscript development and readiness

Date: 2026-10-31. Role: Codex manuscript developer; inherited runtime model/effort metadata is not exposed to this worker. Ownership: `tracks/mz-constants/paper/` and this record only, plus ignored local compilation artifacts. No Git mutation or shared-registry edit was performed.

Rules were read at branch-head commit `2dc9264333cdf8372947448f4b9bdd3bb577d0e1` on `codex/mz-constants-20261031`: `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. A read-only diff confirmed these rules are unchanged from the campaign rule/base commit `d36722823441dc40c6e19d69a174459348dd309c`.

## Gate, source scope, and novelty boundary

The orchestrator explicitly activated M7 after independent Astra accepted the analytic M1/M2/M3 results and recorded their scoped prior-art dispositions. The complete independent report's final disposition table supplies that scientific prerequisite. This permits a complete development draft; it does not clear historical novelty or complete the required Claude handoff.

Before synthesis the developer read the complete 160-line seeded `state/IDEAS.md`, including every M0–M7 heading, aliases, full entries, and both obstruction/disposition tables; `literature/INDEX.md`; all ten `literature/records/mz-*.md` files; the complete M0 `literature-search.md`; the scientific theory records used below; and the bounded reproduction and independent audit records. Searches covered cardinal, harmonic, Fejér, sign, Z-matrix, logarithmic squared, eta, and marginal terms across the registry, theory, topics, and literature. This task synthesizes those existing mechanisms and proposes no new candidate or priority claim. Final identifiers come solely from `topics/mz-constants/final-id-map.json`; the orchestrator owns allocation and canonical replacements.

Source scope includes the M1 foundation, coefficient floor, upper threshold and full-degree obstruction; both M2 endpoint proofs, the U identity/counterexample, Padua compression and retained OPEN sharpenings; M3 upper/lower fixed-ratio estimates, eta assembly and hyperinterpolation; and the MEASURED reproduction record. Historical SS1978/80, interpolation-book, LMN/MT/survey, and Widom full texts remain pending-reference. The manuscript's ASV source context uses selected recorded primary coverage and separately attributes the already-known upper-MZ hyperinterpolation mechanism; it does not infer an exclusion from inaccessible literature. No third-party full text or private C4 text was copied, and no private theorem is a proof dependency.

## Completed deliverables

- `tracks/mz-constants/paper/manuscript.tex`: complete 14-page proof draft, not an outline.
- `tracks/mz-constants/paper/refs.bib`: twelve cited sources using only final LIT identifiers; source-reading limits are visible in the notes.
- `tracks/mz-constants/paper/README.md`: build instructions, claim scope, evidence links, limitations, and review handoff.
- Ignored `local-output/mz-constants/paper/manuscript.pdf`: local review artifact, not added to Git. External archival remains pending AC's chosen Padua-specific destination.

The manuscript gives full proofs of the off-diagonal sign/absolute-coefficient comparison, quantitative coefficient floor, cardinal-cell weighted Schur lower bound, degree- and parity-compatible harmonic-U upper bound, filtered Fejér weighted Schur fixed-ratio estimate, exact N=512 counterexample, positive-rule hyperinterpolation application, and signed-weight-safe Padua compression. It retains the exact CC parity ADE and keeps node index, exactness degree and point count distinct.

The conclusions are deliberately scoped: CC eta tends to one and its condition number has logarithmic squared order, but no rate of that order for `1−eta` and no eventual binding side are claimed. The leading endpoint constant and sharp upper limit/uniform endpoint gap remain OPEN. The Padua conclusion is only a liminf lower bound; signed two-dimensional positivity, upper spectrum, lower asymptotics and eta convergence remain OPEN. The An–Wu finite applicability counterexample does not dispute the validity of the source's conditional theorem. The ordinary hyperinterpolant is kept distinct from inverse-Gram least squares.

## Exact compilation and verification

All compilation ran from `/workspace/padua_research` on 2026-10-31. The full sequence executed successfully:

```sh
mkdir -p tracks/mz-constants/paper local-output/mz-constants/paper
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex
BIBINPUTS=tracks/mz-constants/paper: bibtex local-output/mz-constants/paper/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass2.txt
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass3.txt
```

An incremental fourth LaTeX pass applied wording/PDF metadata. BibTeX was rerun after narrowing its ASV coverage note to equations (7)–(8), followed by LaTeX passes 5 and 6. Two final reviewer-suggested clarity edits specified positive amplitudes for the alternating-data obstruction and described the *guaranteed* upper-bound gap, then LaTeX passes 7 and 8 executed:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass7.txt
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=local-output/mz-constants/paper tracks/mz-constants/paper/manuscript.tex > local-output/mz-constants/paper/pdflatex-pass8.txt
```

Versions actually queried: pdfTeX 3.141592653-2.6-1.40.26, BibTeX 0.99d, TeX Live 2025/dev/Debian, kpathsea 6.4.0/dev. `pdfinfo` reports 14 A4 pages. Final LaTeX and BibTeX logs have **zero** `Warning`, `Overfull`, `Underfull`, `undefined`, or leading-`!` error markers. Initial first-pass unresolved references were resolved by BibTeX and repeat LaTeX; no warning remains in the final pass.

Pages 1 and 9 were rendered by the commands below and visually inspected before the small final wording/metadata edits. The final pass was checked through its clean log.

```sh
pdftoppm -f 1 -l 1 -scale-to 1500 -png -singlefile local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/page-01
pdftoppm -f 9 -l 9 -scale-to 1500 -png -singlefile local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/page-09
pdftotext -layout local-output/mz-constants/paper/manuscript.pdf local-output/mz-constants/paper/manuscript.txt
```

A Python validation found no provisional identifiers and no final PD/LIT identifier outside the allocation map. All six CC and four Padua table rows were parsed from the LaTeX and checked against the existing reproduction JSON: maximum absolute rounding discrepancy `4.673308962033218e-10`, below `5.1e-10`; Padua degree and negative-weight counts matched. This is a transcription check, not a new spectral run. Its ignored output is `local-output/mz-constants/paper/table-transcription-check.json`.

The manuscript developer reviewed the recorded finite outputs but did not rerun the numerical suite. Actual separate replay belongs to the independent Astra report. The source tables remain MEASURED, and none of the analytic proofs depends on a float64 finite check.

## Final development pin

Hashes and byte counts below identify the stable manuscript input and the local PDF produced at 2026-10-31T21:10:03 UTC. The ignored `local-output/mz-constants/paper/build-manifest.json` also records log hashes and validation results. PDF timestamps/output identifiers can change its bytes on recompilation; retained TeX/BibTeX hashes identify the draft itself.

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| `tracks/mz-constants/paper/manuscript.tex` | `072ae4e52c2cea78f2ec13f6e48a3d9529234af6c99d7b747a40c44c31f08c7c` | 39310 |
| `tracks/mz-constants/paper/refs.bib` | `f2f4eb04dec45003a107deac7c91b2f0d4737e2707289d359fd3d0194aeb9bf8` | 4433 |
| `tracks/mz-constants/paper/README.md` | `f433fc6f10b3e0da3bdfec1da80e6e5a177b0967cf6802ec7e1b8217de2512d7` | 6491 |
| `local-output/mz-constants/paper/manuscript.pdf` | `a594ea305fc0f91bb3a2c49d9c6311288440fcffa6eb9e1e95177748d34d3155` | 419412 |

## Readiness and remaining work

M7 development is **COMPLETE**. The earlier independent scientific review accepted M1/M2/M3 analytic validity and recorded actual replays; it does not automatically audit the manuscript's translation. The manuscript's final pinned impact review is requested separately. Required Claude cross-provider audit is **PENDING**, historical novelty is **unresolved**, and the manuscript is **not for submission**. A draft PR may preserve the work with these limits; submission, final authorship, venue, merging, and archival destination are AC's decisions. No submission readiness or audit approval is conferred by this development record.
