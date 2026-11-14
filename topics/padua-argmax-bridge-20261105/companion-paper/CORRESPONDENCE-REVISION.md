# Final paired source and artifact baseline — 2026-11-08

Current source freeze and working helper FINAL_BASELINE:
`24a98db4c3c4c4d0eede2e3929532956df87911b`. Root advanced the earlier dcb candidate after the reviewed
arithmetic/exposition revisions. Final artifact mode passed19 exact formal
statements,85 numbered display environments and116 source/built labels.
Both original48/162-page PDF hashes remain unchanged; final current PDFs are
51/147 pages and147<=5*51. Exact new hashes/commands are in
[paper BUILD](../paper/BUILD.md) and [companion BUILD](BUILD.md).
The complete source/PDF freeze has accepted supplemental Sol max correctness
and exposition review. Any later material TeX/Bib change requires a new source
commit and subsequent static helper-baseline update in a reviewed batch.

README/BUILD prose is excluded from the source freeze. Build defaults now use
the separate onset512 revision directories; artifact verification still requires
explicit current output paths and original PDF paths. The two-ordered-commit
reason and actual earlier tests below remain preserved history. Pending/current
phrases in that older checkpoint are superseded by this final record.

## Historical dcb checkpoint — preserved verbatim

# Paired source baseline revision — 2026-11-08

AC authorized final rebaselining after the coordinated audit-03 manuscript
revision. This is a two-commit boundary within one reviewed batch: root first
commits the final paired TeX/Bib sources, then installs that existing commit
SHA as `FINAL_BASELINE` in check_correspondence.py. A commit cannot contain
its own hash. The candidate source baseline is now `dcb27db7d159ca0eac66e5fb48623589035a31ef`.
Root supplied this existing final paired-source commit on 2026-11-08;
installation in the helper is a subsequent reviewed change. A later material
source revision requires advancing this baseline after a new source commit.

Current mode freezes the exact TeX/Bib file sets and bytes of **both** source
trees, then compares paired headings, statements, numbered display blocks,
labels, section counters, bibliography and both main numbering/input setups.
README/BUILD/other explanatory records are excluded from the source freeze;
subsequent record edits therefore do not require freezing the entire paper
directory again. Identical silent statement changes in both texts still fail
the source baseline even when their pairwise comparison passes.

Artifact verification is read-only and requires explicit output directories.
Build the revision into fresh paths using the existing scripts' output
variables; this checker performs no build and writes no output. With the installed candidate source SHA, the intended artifact command is:

```sh
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py \
  --artifacts --paper-output /ABSOLUTE/NEW-PAPER-OUTPUT \
  --companion-output /ABSOLUTE/NEW-COMPANION-OUTPUT \
  --original-paper-pdf /ABSOLUTE/PRESERVED-48-PAGE/main.pdf \
  --original-companion-pdf /ABSOLUTE/PRESERVED-162-PAGE/main.pdf
```

New PDF paths must be separate from both original PDF paths and from each
other. All source labels must have equal compiled numbers. The companion
limit is five times the **actual revised paper page count**, obtained from
pdfinfo; it is no longer fixed at 240 pages. The checker verifies both old
PDF identities separately, retaining their original sizes/hashes from the
historical BUILD records.

Explicit archival mode reads the historical paper TeX/Bib source from
`c6e195fa5211d4504fd2638f3c7686368e28daee` and historical companion source from
`ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8`, without comparing current revised
sources or current documentation against those old trees. Their immutable Git
source snapshots remain retrievable. Executed here, exit 0:

```sh
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py \
  --archival --artifacts \
  --paper-output local-output/padua-argmax-bridge-20261105/paper \
  --companion-output local-output/padua-argmax-bridge-20261105/companion-paper
```

Result: both original PDF hashes match, 48/162 pages, all 113 compiled labels
match, 13 statements and 90 numbered display environments agree. These paths
were read only; no output was overwritten. Preserve their old bytes separately
before using any fresh revision output directory.

A developer synthetic control was also executed: load both archival source
snapshots as dictionaries, insert `SYNTHETIC SILENT STATEMENT MUTATION` inside
the same first formal statement in `sections/certification-unified.tex` in
both maps, and call compare_pair. The paired comparison passes; calling
check_source_freeze on the mutated paper map against its original snapshot
raises `paper: TeX/Bib source changed: sections/certification-unified.tex`.
This checks the failure that mere pairwise equality would miss. Before baseline installation, a separate current-mode invocation failed with
the explicit pending-baseline message; that observation is historical.
These are source/metadata checks, not a mathematical audit or manuscript build.
Root now obtains helper review and runs the revised artifact check after
final builds. Revised PDF identities remain pending; no current build or artifact
check was performed by this update.

After installing the supplied candidate SHA, current source-only checking
actually exited 0: 19 statements, 85 numbered display environments and 116
labels, matching headings and bibliography. The archival artifact command above
was repeated and exited 0 with both original hashes and all 113 built numbers
unchanged. Current revised artifacts remain for root's new builds.
