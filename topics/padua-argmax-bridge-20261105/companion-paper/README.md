# Explanatory companion — current onset-512 revision

The complete companion is **147 pages**, explaining the current 51-page paper
for a reader with some university analysis. It retains the same five sections,
formal statements, numbered formulas and bibliography, with intermediate
reasoning and worked examples throughout. [BUILD.md](BUILD.md) gives exact
current commands and historical preservation records.

Current default PDF:
`local-output/padua-argmax-bridge-20261105/onset512-companion-20261108/main.pdf`.
Download copy: `padua-companion-20261108-131012-Oslo.pdf` in that directory.
It is 1171187 bytes, SHA-256
`83ca42c8052ccd760c3929ff0c30cd1667971476ae111736fe371b30e4581af2`.

Final paired TeX/Bib source freeze: `24a98db4c3c4c4d0eede2e3929532956df87911b`.
The [accepted supplemental Sol max review](../manuscript-onset512-solmax-review.md)
accepts correctness and exposition at this source/PDF freeze, with E1/E2/E4
resolved. [Astra reviews](../independent-checks-onset512-response.md) accept the
analytic gates/constants, new finite campaign and independent arithmetic at
their stated scopes. These are distinct from the next substantive Claude audit
and PR readiness.

The proof uses [J01](../theory/J01-onset512-gates.md) analytically for n>=512,
[J02](../theory/J02-elementary-constant-enclosure.md) for elementary rational
constant bounds, Bernstein witnesses for2..40 and
[J03](../theory/J03-independent-phase-checker.md) for all942 complete phase
trees at471 degrees41..511. I25 uses its own finite-sum interval bounds under
explicit Python/Fraction, guarded NumPy and IEEE binary64 assumptions plus
named analytic lemmas. A distinct execution accepted six certificates. This
is not universal validation of historical native endpoints. The sharp corner
expansion remains analytic.

The off-Git I25 evidence dataset is 2,843,611 bytes, SHA-256
`d1d03156dde4248fecaa25d0144cd73c7c5414f28b66a39099342b31f2f7e0f8`;
[completed summary](../code/independent_phase_checker/independent-phase-summary.md)
and [deposit plan](../zenodo-deposit/README.md) give exact sources, commands,
942 input proofs, runtime/preregistration records and separate review bundle.
The canonical81,602,992-byte new native provenance return and its945,235-byte
certificate-only derivative remain distinct. Historical local native replay
completed all280 old degrees; it used the same engine and is not second arithmetic.

Both current source trees and built numbers agree:19 formal statements,
85 numbered display environments and116 labels. The retained48/162-page PDF
hashes also match. The companion147 pages is within five times the paper51;
AC treats page count as secondary to needed explanation. No step should appear
without its reasoning; named tools should be stated with hypotheses or cited.
Both use the unchanged verified publisher class/BST. All PDFs/build outputs
remain outside Git. AI declaration, ORCID and contributions are reserved to AC;
funding is confirmed. The reproduction source snapshot is prepared at a433c7d; AC's Zenodo DOI/publication,
independent durable retrieval and registry/PR preparation remain separate.

## Current build and correspondence

```sh
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh
python3 -B topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
```

Artifact mode requires explicit current output directories and both preserved
original PDF paths; see [revision record](CORRESPONDENCE-REVISION.md).
The helper checks both exact source baselines as well as paired blocks, then
all built numbers, actual page ratio and old PDF hashes. Builds perform no
mathematical verification. Default output directories protect the old artifacts.

## Historical companion record — superseded current instructions

The following dated-development snapshot describes the original162-page
companion and48-page paper. Its commands/page ceiling/source freeze are
historical, not current build or artifact-check instructions.

# Expanded explanatory companion

This separate manuscript develops the 48-page research article for a
reader with university analysis. It follows the same five sections and
subsections and retains every numbered statement and numbered formula.
Definitions, motivations, worked examples and intermediate calculations
are added in unnumbered prose and displays. AC permits up to 240 pages;
the length follows the explanation needed within that ceiling.

The original [paper](../paper/main.tex), its whole source directory and
its PDF remain intact. The baseline is commit
`c6e195fa5211d4504fd2638f3c7686368e28daee`; original directory tree
`ccb6e4568ec69bd3afbff3408f7659ac888ab14b`. Its 48-page PDF is 640116
bytes, SHA-256
`07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0`.

Build from the repository root:

```bash
bash topics/padua-argmax-bridge-20261105/companion-paper/build.sh
python3 topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py
```

When the preserved baseline PDF and its TeX auxiliary file are available
in the original local-output directory, also compare the built numbers
and check that the original PDF is intact:

```bash
python3 topics/padua-argmax-bridge-20261105/companion-paper/check_correspondence.py --artifacts
```

The companion uses the same verified Springer class and bibliography
style. Its build has a separate output/template directory under
`local-output/padua-argmax-bridge-20261105/companion-paper/`; all PDFs,
logs, previews and third-party dependencies stay outside Git. The original
build is never run into its existing output as part of this companion
workflow. [check_correspondence.py](check_correspondence.py) compares
the original source, headings, numbered statement/formula blocks and
actual compiled label numbers. It checks correspondence; mathematical
and reader-accessibility review is recorded separately in review.md.

The theorem assumptions and computational evidence scope remain those of
the research article. The development and audit history are recorded in
the topic log. Permanent public code/evidence release and final human
review remain publication tasks.

## Current expanded version

The complete companion is **162 pages**, about 3.4 times the original
48 pages and within the 240-page ceiling. Source freeze:
`ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8`. All five sections and
their subsections are retained, together with the same 13 formal
statements and 90 numbered display environments. All 113 compiled label
numbers match. The original paper directory and PDF are unchanged.

Explanations run throughout: definitions and linear algebra in Section 2;
row sums, quadrature and limit interchanges in Section 3; reflection
geometry, scalar models, coefficient ledgers and monotonicity in Section 4;
finite certificates, positive interpolation and arithmetic in Section 5.
The review includes a second whole-document depth pass after AC clarified
that the screenshot was an example of the standard for every section.

Current timestamped PDF:
`local-output/padua-argmax-bridge-20261105/companion-paper/padua-companion-20261107-222747-Oslo.pdf`.
It is 1153227 bytes, SHA-256
`2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7`.
[BUILD.md](BUILD.md) records build and inspection details;
[review.md](review.md) records the distinct Sol max review and its scope.
That review accepts the complete companion at the final source freeze,
with no unresolved findings.
