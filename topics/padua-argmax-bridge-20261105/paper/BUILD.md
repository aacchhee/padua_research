# Current journal paper build — 2026-11-08

Current paired source freeze: `24a98db4c3c4c4d0eede2e3929532956df87911b`.
Run `bash topics/padua-argmax-bridge-20261105/paper/build.sh` from the repository
root. The default is now
`local-output/padua-argmax-bridge-20261105/onset512-paper-20261108/`.
Set the documented output environment variable for another fresh directory;
the old48/162-page artifact directories are protected by the new defaults.
The verified publisher class/BST and stable timestamp settings are unchanged.
Current artifact: **51 pages, 733598 bytes**, SHA-256
`1346fc2891e2cdd5deb6db4b1a5928a2a7bac05c1838999b1a1dee1fc0db1d2c`. Download copy: `padua-manuscript-20261108-131012-Oslo.pdf`.

The final commands and actual checks are appended below. Everything in the
historical section retains its original source identity, output paths and
counts; do not use its superseded default paths for a new build.

## Historical build records — preserved verbatim

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

## Author metadata and supplied-template build — 7 November 2026

Author/front/back matter source commit
`fcf6132c6ba53c112c990946d067799d7a1a8567` supplies the authorized author
information and adapted disclosures. All seven mathematical/bibliography
identities and the input graph from the accepted Solmax review remain
unchanged; main.tex changes are metadata only.

The December2024 package supplied by AC is now verified: its class and
numbered math/physics BST exactly match the pinned dependency bytes.
Those local files were replaced from the ZIP. The ordinary build reported
up to date because the bytes are identical; a forced `latexmk -g` using
the same options/template paths/stable timestamp then actually recompiled
successfully. It uses the same SOURCE_DATE_EPOCH1794009600 and
FORCE_SOURCE_DATE=1 as build.sh. No class/style patch was needed.

Current PDF:46pages,631614 bytes, SHA-256
`cb78f3710fdd7cecd10c542053c5595390c189d41862308af0df7d1dd7df5d9a`.
It has Andrey Chesnokov in its PDF metadata and correctly rendered
correspondence/affiliation/ORCID/disclosures. There are no TeX errors,
undefined references/citations, overfull boxes or warnings. The previously
audited46-page PDF remains under `paper/audited-46-pages/main.pdf` in
local-output; all PDFs and the supplied901814-byte ZIP remain offGit.

## Affirmative prose and application context — 7 November 2026

Source commit `4050f6861a44a88ec5d7941787703fbbe9d9ce4a` edits the prose
throughout and adopts the three-source application paragraph. The explicit
alphabetical bibliography now has 13 entries. All 204 displayed math blocks
and both main theorem statements match the preceding source exactly.

`bash topics/padua-argmax-bridge-20261105/paper/build.sh` passes at 46 pages.
The log contains underfull-box diagnostics; the error, warning, undefined
reference/citation and overfull-box checks pass. Current PDF is 632068 bytes, SHA-256
`919058546f5d3ac09a64a05f24511da6cd0b91022fe28a459a2d23e8781cefd9`.
A timestamped copy for download is
`local-output/padua-argmax-bridge-20261105/paper/padua-manuscript-20261107-204352-Oslo.pdf`.
Its bytes match main.pdf. User-facing links use fresh Europe/Oslo timestamped
filenames to avoid the previously observed stale download. Both copies
remain outside Git. The focused Sol max meaning/style review in
affirmative-style-review.md accepts this source with no unresolved findings.

## Expanded Section 5 — 7 November 2026

The final source at `177be83bcb03204ae30c74355ad387ac52f42cb5`
expands Section 5 from three to five pages, as requested by AC. The whole
paper now has **48 pages**; Section 5 occupies pages 42–46 and the
bibliography begins on page 47. The class, fonts and layout are unchanged.

The developer's build and root's rebuild after final wording/spacing
polish pass. The final log contains underfull-box diagnostics; the error,
warning, undefined-reference/citation and overfull-box checks pass. Root
inspected rendered pages 43 and 46 and the final corner calculation on
page 45. All other TeX sources and the bibliography match the preceding
reviewed draft.

Section 5 source: 13274 bytes, SHA-256
`80c4e3e764e559d596d38ae5ee40702fd3ce9ba54ea1dbe43eb5c234d6ee6eea`.
Current PDF: 640116 bytes, SHA-256
`07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0`.
Fresh timestamped copy:
`local-output/padua-argmax-bridge-20261105/paper/padua-manuscript-20261107-212439-Oslo.pdf`.
Its bytes match main.pdf. Both PDFs and all build logs stay outside Git.
The focused Sol max review in section5-expansion-review.md accepts the
expanded derivations at this source freeze, with no unresolved findings.

## Final onset-512 build and artifact acceptance — 2026-11-08

Root actually built both final manuscripts with exit0 at source freeze
`24a98db4c3c4c4d0eede2e3929532956df87911b` using:

```sh
bash topics/padua-argmax-bridge-20261105/paper/build.sh
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py \
  --artifacts \
  --paper-output local-output/padua-argmax-bridge-20261105/onset512-paper-20261108 \
  --companion-output local-output/padua-argmax-bridge-20261105/onset512-companion-20261108 \
  --original-paper-pdf local-output/padua-argmax-bridge-20261105/paper/main.pdf \
  --original-companion-pdf local-output/padua-argmax-bridge-20261105/companion-paper/main.pdf
```

The artifact check passed19 statements,85 numbered display environments and
116 paired source/built labels. Actual lengths are51/147 pages, so147<=5*51.
Both original48/162-page PDFs retain their recorded hashes. Final converged
logs have no errors, warnings, undefined citations/references, multiply defined
labels or overfull boxes. Underfull-box diagnostics alone remain. Root viewed
the phase figure, trust table and arithmetic derivation and found them readable.
The distinct [Sol max review](../manuscript-onset512-solmax-review.md) accepts
correctness and exposition at these final sources/PDFs; report SHA-256
`fe935ea03a245dd6301370cc02b4ac826cacec55d036b8c99942a4d00d44dff9`.

This artifact:
`local-output/padua-argmax-bridge-20261105/onset512-paper-20261108/main.pdf`,
733598 bytes, SHA-256 `1346fc2891e2cdd5deb6db4b1a5928a2a7bac05c1838999b1a1dee1fc0db1d2c`; 51 pages.
The timestamped copy `padua-manuscript-20261108-131012-Oslo.pdf` is byte-equal to main.pdf.
Documentation integration independently read back both PDF/copy pairs and the
review report hashes; it performed no new build or scientific run. The unchanged
publisher-template identities remain in the template lock/provenance records.
The next substantive Claude audit, source-ZIP packaging, AC DOI/publication,
durable retrieval and PR readiness are separate from build acceptance.


## Audit-04 response build — 2026-11-13

Final paired TeX/Bib source freeze: `ad908acb21d3589d85635618ff68f63dd01cfbca`.
Codex root executed `bash topics/padua-argmax-bridge-20261105/paper/build.sh`
after the final proof, notation and layout fixes. The script now defaults to
a fresh audit04-paper-20261113 output directory, preserving earlier build
targets. Both final commands exit 0. TeX Live 2025/dev pdfTeX 1.40.26 and
latexmk 4.86; pinned publisher class/BST identities unchanged. The final logs
have no errors, warnings, undefined references/citations, multiply-defined
labels or overfull boxes; underfull diagnostics remain. The fixed
SOURCE_DATE_EPOCH is retained for reproducibility.

This PDF has **57 pages**, **786999 bytes**, SHA-256
`5616921e195f999eb8fa47d5393eff89b16f89b597f941e7dd41fde00fa74830`. Fresh download copy:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit04-paper-20261113/padua-manuscript-20261113-212438-Oslo.pdf`. Its bytes equal the corresponding `main.pdf`.
Both PDFs and build logs remain off Git.

The final source checker and all 7 paired-mutation controls pass in root and
a distinct Astra high rerun. Current built outputs have all 116 labels equal
and 19 statements/85 numbered display environments; 150<=5*57. Root checked
rendered paper pages 18/54 and companion pages 91/143 (phase diagram, row/pole
illustration and trust tables). The [supplementary manuscript review](../supplementary-manuscript-review-20261113.md)
records selected proof reconstruction, all 32 audited duplicate-pair integrity
checks, all 60 rational-table enclosures and its actual limits.

Historical 48/162 and 51/147 source freezes remain in Git. The original PDF
bytes are absent in this workspace: the full `--artifacts` preservation mode
was not run and historical PDF preservation is **not independently retested**.
Current auxiliary-number/page/identity comparisons were executed separately;
this distinction is deliberate, not a skipped condition reported as PASS.
The focused Claude review, missing new-range evidence ZIPs and external
publication/custody remain separate.


## Response-05 final build — 2026-11-13

Paired TeX/Bib source freeze: `8937d3b723c09c004f49d3e565d0b02976713a37`.
Root executed `bash topics/padua-argmax-bridge-20261105/paper/build.sh`;
this now defaults to a fresh audit05-paper-20261113 directory. Earlier
audit04 outputs and timestamped copies are preserved. Both commands exit 0
under TeX Live 2025/dev, pdfTeX 1.40.26/latexmk 4.86, with the same authenticated
publisher dependencies. No errors, warnings, overfull boxes or undefined
references/citations; underfull diagnostics remain.

This PDF: **58 pages**, 798493 bytes, SHA256
`1dc50b84b6ac6a7d92300370dde5e95b867b4e428708883c291d2b4cd089c657`. Fresh Oslo-timestamped copy, byte-equal to main.pdf:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit05-paper-20261113/padua-manuscript-20261113-232634-Oslo.pdf`. PDFs, renders and logs remain off Git.

Both current artifacts agree on 120 built labels, 19 statements and 86
numbered environments. The separately committed pointer update and seven
mutation controls pass in root and an independent reviewer; archival source
pairing also passes. Root's current-artifact comparison and the reviewer
confirm 58/152 pages and 152<=5*58. The six old B5-02 displays now numbered
11/20/26/40/51/55 have adjacent tags in each final PDF: all 12 placements were
actually rendered and inspected. Figure/roles/row/base table layouts were
also inspected; this evidence is distinct from no-overfull log checks.

[Supplementary review](../supplementary-manuscript-review-response05-20261113.md)
records exact source/PDF identities, independent analytic checks and the
returned/fixed table-pointer issue. Original PDF bytes remain unavailable;
full historical --artifacts mode is not claimed. Permanent post-repair
snapshot/DOI and missing new-range archive checks remain OPEN.


## Response-06 build checkpoint — 2026-11-14

Paired source freeze `36ac77252fb490e58b807767a6bd52f6f3f3dff4`;
source pointer installed separately in `cc2f9ad`. Root executed this tree's
`build.sh` with the fresh audit06 default directory: exit 0, **59 pages**,
803703 bytes, SHA256 `d978c5fe064421be6f38bb776c29190fbbbc62e3859d15945f29701d61a33ec4`.
Byte-equal timestamped copy: `/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit06-paper-20261114/padua-manuscript-20261114-010343-Oslo.pdf`.

Both artifacts match on 120 built labels, 19 statements and 86 numbered
environments; 152 <= 5 * 59. No overfull boxes, undefined references/citations
or badness-10000 hboxes; other underfull diagnostics remain. A distinct
reviewer inspected the affected final pages. Seven baseline controls and
the copied nine-type mutation harness behave as expected; current and
archival source checks pass. Historical PDF preservation mode was not run.
[Response-06](../response-06.md) and its linked review give exact scope.
This checkpoint predates AC-authorized paper-evidence regeneration; it
does not certify the later campaign or establish deposition/readiness.


## Paper-dependent evidence regeneration — 2026-11-14

Current paired freeze `e861c752218fc0a6648d4a4a67fea616ba5cbdd1`;
separate pointer `3e2805e`. Root fresh build.sh exits 0 in regenerated
output directory: **59 pages**, 804080 bytes, SHA256
`b0abf068834066e4494cbf9cedecbe2f2c94871233d16f2463816eb2c4501749`. Byte-equal timestamped copy:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/regenerated-paper-20261114/padua-manuscript-20261114-015102-Oslo.pdf`.
Both artifacts match on 120 built labels, 19 statements and 86 numbered
environments; 152 <= 5 * 59. Seven baseline controls and adapted nine-type
mutation harness behave as expected (13 scenarios; source changes reject,
unmodified/README-only pass). Harness SHA256
`190d2cf8a0e00117600aba2495b6a47c6561e9cb60e54e8b0b0b38aa08b318a4`.
The empty-map scanner confirms formal blocks unchanged from 36ac772.
No overfull, undefined or badness-10000 hbox diagnostics; other underfull
diagnostics remain. Distinct review visually inspects affected final pages.
The new paper evidence is available and recertified; historical-only PDF
byte preservation is no longer required by AC. [Regeneration record](../regeneration-20261114.md)
and its review distinguish actual verification from storage/ABI assumptions.
