# Publisher template provenance

Checked 2026-11-07. This draft uses the actual Springer Nature `sn-jnl`
authoring class with `pdflatex,sn-mathphys-num` options. It does not emulate a
publisher layout with an unrelated class.

The [Constructive Approximation instructions](https://link.springer.com/journal/365/submission-guidelines)
do not link a journal-specific class. They require an abstract, keywords,
current MSC numbers, alphabetically ordered numerical references, and a
consistent approved mathematical-statement numbering scheme. The manuscript
uses [Style A](https://my.vanderbilt.edu/castatementnumberingstyles/), a shared
counter within each section. The instructions say to submit the PDF and keep
the corresponding TeX source for acceptance. A data availability statement is
also required.

[Springer Nature's author support page](https://www.springernature.com/gp/authors/campaigns/latex-author-support)
currently links the December 2024 journal package (v3.1), suitable for Springer
Nature journals subject to each journal's instructions. Its
[official archive](https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12)
and the official Overleaf download returned HTTP 403 to the build environment.
Therefore `build.sh` retrieves only the class and bibliography style from the
[pinned public mirror](https://github.com/iftaken/anor-template/tree/dfeb5372e9211ef50b8d46023e64221f4a8c8de8).
That mirror's `anor-article.tex` identifies the class as v3.1, December 2024.
The mirrored files were **not** byte-compared against the inaccessible official
archive. The class's internal `ProvidesClass` date remains 2019/11/18 v0.1;
that internal date is not the template-package release date.

`dependencies.json` records exact retrieval URLs, SHA-256 hashes and byte sizes.
The mirror's example manuscript is not used in this research paper. The
downloaded class and style retain their upstream notices and remain outside
Git in `local-output/`; no third-party template text is committed here.
The class header states LPPL 1.3c-or-later terms; the downloaded files should
retain their notices when supplied for typesetting. This note does not replace
the upstream licence terms.

The math/physics numbered BST implements sorting; the draft's bibliography
must also be checked against the journal's alphabetical requirement. A manual
`thebibliography` list is acceptable when kept numerical and alphabetical.
