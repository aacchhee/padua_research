# Build the Constructive Approximation draft

From the repository root:

```sh
bash topics/padua-argmax-bridge-20261105/paper/build.sh
```

Prerequisites: Python 3, curl, `latexmk`, pdfLaTeX and the ordinary LaTeX
packages used by Springer Nature `sn-jnl` (a recent TeX Live installation with
the recommended and extra LaTeX packages is suitable). The observed environment
has pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev/Debian, and `latexmk`
4.86 (11 December 2024).
XeLaTeX is also installed; Tectonic is not. Neither is needed for this build.

The script validates the two pinned dependencies in
[template/dependencies.json](template/dependencies.json), downloading missing or
different files into `local-output/padua-argmax-bridge-20261105/paper/template/`.
It runs `latexmk -norc -pdf -interaction=nonstopmode -halt-on-error
-file-line-error` on `main.tex` with all output under that same `paper/` output
directory. The PDF is `local-output/padua-argmax-bridge-20261105/paper/main.pdf`.
No generated PDF, logs, auxiliary files, class or BST belongs in Git.

For dependency retrieval alone:

```sh
bash topics/padua-argmax-bridge-20261105/paper/build.sh --fetch-only
```

To place output elsewhere, set `PADUA_PAPER_OUTPUT_DIR` to an absolute path.
Set `SOURCE_DATE_EPOCH` to override the default stable timestamp, 1794009600
(2026-11-07 00:00 UTC). This supports repeatable timestamps; byte-identical
PDFs additionally require the same TeX engine and package versions. Hash
validation makes the downloaded template bytes reproducible.

The [template provenance note](template/README.md) records the official source,
the access limitation, and the pinned mirror used for the build. Use the
publisher's official package in a final submission if available, checking any
class/style change by rebuilding. This draft is an internal manuscript; author
metadata and submission readiness remain separate from successful compilation.

Dependency verification on 2026-11-07: `build.sh --fetch-only` verified both
SHA-256 hashes, and `bash -n build.sh` passed. An untracked one-page smoke
document using the pinned class, `amsmath`, `amssymb`, a section-numbered
theorem and a proof compiled successfully with pdfLaTeX. This checks template
and installed package compatibility; it does not check the research claims.

## Integrated manuscript build — 2026-11-07

The complete manuscript compiled successfully with the command above at
TeX/bibliography source commit
`a948b24c3faeba1e475ce64f4c7fc9d4123d42a5`. The final converged log has
no undefined references/citations, multiply defined labels, overfull boxes
or TeX errors. Ten numerical bibliography entries are ordered
alphabetically by the explicit ordered `nocite` list before the first
textual citation, preserving the unmodified publisher BST.

Artifact: `local-output/padua-argmax-bridge-20261105/paper/main.pdf`
(837560 bytes; SHA-256
`668a96ad2d314099180537925b7a398230d58c450de26ae2f1c51de6c47cbc10`).
There are 88 PDF pages; the first appendix begins on page18. The main text
occupies pages1–17 including the title/abstract page. First-two-page
rendering was inspected and is legible. The remaining pages contain the
supporting proof appendices, temporary traceability appendix and references.

The PDF is a regenerable local working artifact, not a verified durable
cold-storage release. Its source is committed; its bytes, dependency
downloads, auxiliary files, previews and logs remain outside Git. The
recorded build command and template pins reproduce the document, subject
to the already documented TeX/package version dependence of PDF bytes.

## Superseding unified build — 2026-11-07

The integrated source at commit
`eddf2276ad33937b69c4374b56510686c978e23a` supersedes the88-page build above.
The same command, class, fonts and layout now produce **46 pages**:42pages
removed, about48% shorter. There is no uncounted proof supplement.

Current artifact: `local-output/padua-argmax-bridge-20261105/paper/main.pdf`,
628901 bytes, SHA-256
`7beea935ea68b0e7aaaf5b6bb0fad4d597eb256cdb27c8c0dc9a840901f78d2c`.
The root integrated build has no undefined references/citations,
multiply-defined labels, TeX errors or overfull boxes. Worker-only wrapper
counts were45pages;46 is the measured complete root build including its
actual front/back matter and bibliography. The46-page count is authoritative.
A rendered middle proof page was inspected for readable ordinary type and
unclipped formulas. The earlier88-page PDF is preserved offGit at
`local-output/padua-argmax-bridge-20261105/paper/original-88-pages/main.pdf`.

The current source layout is described in README.md and the proof cuts in
CONSOLIDATION.md. Sol max audits the final mathematical correctness and
redundancy in consolidation-audit.md. The new common small-degree replays
are scientific checks recorded separately in small-degree-unification.md;
they are not inferred from successful TeX compilation.
