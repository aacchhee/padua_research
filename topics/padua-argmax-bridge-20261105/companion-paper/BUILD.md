# Current explanatory companion build — 2026-11-08

Current paired source freeze: `24a98db4c3c4c4d0eede2e3929532956df87911b`.
Run `bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh` from the repository
root. The default is now
`local-output/padua-argmax-bridge-20261105/onset512-companion-20261108/`.
Set the documented output environment variable for another fresh directory;
the old48/162-page artifact directories are protected by the new defaults.
The verified publisher class/BST and stable timestamp settings are unchanged.
Current artifact: **147 pages, 1171187 bytes**, SHA-256
`83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2`. Download copy: `padua-companion-20261108-131012-Oslo.pdf`.

The final commands and actual checks are appended below. Everything in the
historical section retains its original source identity, output paths and
counts; do not use its superseded default paths for a new build.

## Historical build records — preserved verbatim

# Expanded companion build and preservation record

Final manuscript source freeze:
`ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8`.
The original research article remains frozen at
`c6e195fa5211d4504fd2638f3c7686368e28daee` with its complete 20-file
paper directory and 48-page PDF intact.

## Build and numbering

```bash
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh
python3 topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --artifacts
```

The root integrated build produces **162 pages** with the original
Springer class, fonts and layout. The companion uses a separate source
directory and output/template directory. The same pinned class/BST bytes
are verified through the original build script's fetch-only operation,
with the companion output selected explicitly. Original output files are
never build targets of this workflow. Stable TeX timestamps use
SOURCE_DATE_EPOCH=1794009600 and FORCE_SOURCE_DATE=1, as in the research
article; PDF bytes still depend on the TeX/package versions.

The correspondence check passes: all original paper files and its PDF
are intact; section/subsection commands, 13 formal statements, 90
numbered display environments, 113 source labels and bibliography match.
Every compiled label number matches the original. The companion's 162
pages are below the allowed 240. The source-only mode is also available
without local PDF/auxiliary files, as described in README.md.

## Artifact and inspection

Off-Git PDF:
`local-output/padua-argmax-bridge-20261105/companion-paper/main.pdf`,
1153227 bytes, SHA-256
`2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7`.

Fresh user-facing download copy, verified byte-for-byte against main.pdf:
`local-output/padua-argmax-bridge-20261105/companion-paper/padua-companion-20261107-222747-Oslo.pdf`.
Use fresh Europe/Oslo timestamped filenames for subsequent revisions.

Final main.log: 50013 bytes, SHA-256
`3e131145fe231bad2cd12cea7940482f2f64e03516b97e3889f58824ffef2c72`.
There are no errors, warnings, undefined references/citations,
multiply-defined labels or overfull boxes. Underfull-box diagnostics
remain. Four overwide new unnumbered displays were split across lines;
their equations and the original numbered blocks are preserved.
A final minor diagram fix moves the phase-coordinate label clear of
the diagonal boundary. The diagram's domains and all numbering are unchanged.

Root inspected rendered pages 14 (Gram calculation), 100 (endpoint error),
144 (phase introduction) and 145 (phase diagram and bounds). The original
point plot is retained; the added phase diagram is unnumbered. The
typesetting is legible and the formulas fit. The distinct reviewer's
artifact inspection and complete mathematical/accessibility review are
recorded in review.md. No native certificate campaign was rerun for this
expository expansion.
The distinct Sol max review accepts the complete companion at the final
source freeze, with no unresolved findings. Root read the full report
and verified all eight frozen source identities and the download bytes.

All PDFs, TeX dependencies, auxiliary files, logs and rendered previews
remain outside Git. This is a local working artifact with committed
regenerating source; final human review and a permanent publication
release remain the existing publication tasks.

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
`local-output/padua-argmax-bridge-20261105/onset512-companion-20261108/main.pdf`,
1171187 bytes, SHA-256 `83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2`; 147 pages.
The timestamped copy `padua-companion-20261108-131012-Oslo.pdf` is byte-equal to main.pdf.
Documentation integration independently read back both PDF/copy pairs and the
review report hashes; it performed no new build or scientific run. The unchanged
publisher-template identities remain in the template lock/provenance records.
The next substantive Claude audit, source-ZIP packaging, AC DOI/publication,
durable retrieval and PR readiness are separate from build acceptance.


## Audit-04 response build — 2026-11-13

Final paired TeX/Bib source freeze: `ad908acb21d3589d85635618ff68f63dd01cfbca`.
Codex root executed `bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh`
after the final proof, notation and layout fixes. The script now defaults to
a fresh audit04-companion-20261113 output directory, preserving earlier build
targets. Both final commands exit 0. TeX Live 2025/dev pdfTeX 1.40.26 and
latexmk 4.86; pinned publisher class/BST identities unchanged. The final logs
have no errors, warnings, undefined references/citations, multiply-defined
labels or overfull boxes; underfull diagnostics remain. The fixed
SOURCE_DATE_EPOCH is retained for reproducibility.

This PDF has **150 pages**, **1216528 bytes**, SHA-256
`b6898b2eba447b2bf89765d4693aa672c5c7c5e737fed3865e00c0fbe592bc94`. Fresh download copy:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit04-companion-20261113/padua-companion-20261113-212438-Oslo.pdf`. Its bytes equal the corresponding `main.pdf`.
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
Root executed `bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh`;
this now defaults to a fresh audit05-companion-20261113 directory. Earlier
audit04 outputs and timestamped copies are preserved. Both commands exit 0
under TeX Live 2025/dev, pdfTeX 1.40.26/latexmk 4.86, with the same authenticated
publisher dependencies. No errors, warnings, overfull boxes or undefined
references/citations; underfull diagnostics remain.

This PDF: **152 pages**, 1215607 bytes, SHA256
`9bd922db9599a46577fe5af5a19499e96f338946ad7b5a7c55f79210e5809a1c`. Fresh Oslo-timestamped copy, byte-equal to main.pdf:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit05-companion-20261113/padua-companion-20261113-232634-Oslo.pdf`. PDFs, renders and logs remain off Git.

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
`build.sh` with the fresh audit06 default directory: exit 0, **152 pages**,
1221098 bytes, SHA256 `54245f25277e01dfb4d8d76ea06305b794362fe302db0f6e7361f3193f6dba4b`.
Byte-equal timestamped copy: `/workspace/padua_research/local-output/padua-argmax-bridge-20261105/audit06-companion-20261114/padua-companion-20261114-010343-Oslo.pdf`.

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
output directory: **152 pages**, 1223975 bytes, SHA256
`3c7a114a9eb33f6211b8e1d522033cf0f0fbbc1a938e206ba1341792feb920ec`. Byte-equal timestamped copy:
`/workspace/padua_research/local-output/padua-argmax-bridge-20261105/regenerated-companion-20261114/padua-companion-20261114-015102-Oslo.pdf`.
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
