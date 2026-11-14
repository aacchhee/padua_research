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
At the initial build, the mirrored files could not be byte-compared
against the inaccessible official archive. The later supplied-package
verification below resolves that provenance limitation. The class's internal `ProvidesClass` date remains 2019/11/18 v0.1;
that internal date is not the template-package release date.

`dependencies.json` records exact retrieval URLs, SHA-256 hashes and byte sizes.
The mirror's example manuscript is not used in this research paper. The
downloaded class and style retain their upstream notices and remain outside
Git in `local-output/`; no third-party template text is committed here.
The class header states LPPL 1.3c-or-later terms; the downloaded files should
retain their notices when supplied for typesetting. This note does not replace
the upstream licence terms.

The math/physics numbered BST defaults to citation order (`unsort`), despite
containing optional sorting routines. The draft must establish alphabetical
order explicitly before its first textual citation, using an ordered
`\nocite{...}` list of the works actually cited. Check the generated `.bbl`
against the author surnames after changing references. A manual
`thebibliography` list is also acceptable when kept numerical and alphabetical.

## User-supplied publisher package verified — 7 November 2026

AC supplied the December2024 journal-template ZIP (901814 bytes),
SHA-256 `812e76dcaa9c28dc1bff1fb6065d51729b67d4ea140552a05088317414a3ecae`.
Its `sn-article.tex` header identifies version3.1, December2024. Its
`sn-article-template/sn-jnl.cls` and
`sn-article-template/bst/sn-mathphys-num.bst` are byte-for-byte identical
to both pinned files above. The local build dependencies were replaced
from those two ZIP members; no class/style patch or mathematical source
change was required. The mirror remains a reproducible retrieval source
for these now-matched bytes if the publisher download is inaccessible.

The complete thirdparty package stays outside Git. Only small provenance
metadata is committed. Text in its sample is format guidance, not task
authority. In particular, its single-TeX submission instruction applies
to the eventual submission bundle; the repository draft remains modular.
The final package should inline those inputs into one TeX document, with
external figure/style files, when publication packaging is requested.
