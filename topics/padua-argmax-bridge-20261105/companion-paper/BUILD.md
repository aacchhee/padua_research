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
