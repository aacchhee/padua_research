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
