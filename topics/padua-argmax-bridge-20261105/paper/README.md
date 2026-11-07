# Unified Constructive Approximation draft

[main.tex](main.tex) builds the current **46-page** manuscript, reduced from
88 pages with the same Springer class, fonts and layout. The proof is
integrated into the article; the old appendices have not been relocated
to an uncounted supplement. [CONSOLIDATION.md](CONSOLIDATION.md) explains
the reorganization and what was removed.

Build using [BUILD.md](BUILD.md). The current PDF stays outside Git:
`local-output/padua-argmax-bridge-20261105/paper/main.pdf`.
The original full draft is preserved by commit
`a948b24c3faeba1e475ce64f4c7fc9d4123d42a5` and its local archived PDF.

## One proof chain

- `sections/introduction.tex` states the two main theorems once.
- `sections/preliminaries.tex` fixes the corrected cardinal and angular
  kernel, endpoint weights and exceptional mode.
- `sections/corner-unified.tex` derives the corner expansion in one
  argument, including the exact rows, κ and uniform first correction.
- `sections/localization-unified.tex` gives the exact reflection geometry,
  includes `comparison-unified.tex`, then applies one comparison to the
  selected-pair floors and all needed closed regions.
- `sections/comparison-unified.tex` supplies the common completed model,
  paired cancellation estimate and single finite-row error telescope.
- `sections/certification-unified.tex` uses one positive-interpolation
  principle for the finite completion and states the evidence boundary.

The analytic corner theorem is independent of argmax and numerical
constant enclosures. The global maximizer theorem retains the explicitly
computer-assisted finite cases and quantitative constant input. Its
finite41–63 defect derivation is now included explicitly. Unused generic
cutoffs, the unused512-plus finite tier, repeated theorem statements,
historical result families, discussion and long operational inventories
have been removed from the compiled article.

## Audit and small degrees

[consolidation-audit.md](consolidation-audit.md) is the distinct **Sol max**
correctness and redundancy audit requested by AC. It records the complete
compressed-proof review, findings, dispositions, source identities and
actual independent native small-degree checks. It is distinct from the
older [review.md](review.md), which describes the superseded88-page draft.
The broader historical research-batch audit and PR readiness remain
separate from this requested manuscript audit.

For degrees2–40, the paper now uses one corrected-cardinal Bernstein
certificate scheme. Fresh2–16 witnesses passed independent exact native
checking; accepted17–40 witnesses are reused. A two-literal metadata-only
repair reports the initial degree-2 cosine seed correctly, without changing
arithmetic, certificate data, strict predicates or the older frozen files.
The exact failure, repair, invariance argument and checks are in
[small-degree-unification.md](small-degree-unification.md) and its code/data
links. Degree1 has a direct affine formula; the executable still begins
at2 and the main theorem's n>=2 scope is unchanged.

## Reproducibility and publication scope

The source mathematical dependencies are the same canonical H/G01/E14,
PD-T101/159/269/270/271 and D29/C02 records used by the earlier draft;
[CONSOLIDATION.md](CONSOLIDATION.md) maps their reorganized roles. The
numerical κ input is now specified by its coefficient series and analytic
tail in the article, not only by an internal identifier. The bounded
literature comparison remains in `../literature-refresh-20261107.md`;
no exhaustive priority clearance is claimed.

All essential phase proofs are retained, but complete local histories and
fresh native replays cover only the two selected degrees199/238. Other
full histories remain server-local under AC's selective-retention policy.
The new small-degree certificates and short receipts are committed and
indexed. The essential evidence index has396 entries/32414 bytes, below
its reviewed32KiB limit. No raw histories, PDFs, template dependencies or
build logs belong in Git; tracked generated outputs remain below10MB.

Author information, ORCID, funding, conflicts and contributions are now
supplied from Paper F under AC's explicit authorization; the AI disclosure
is adapted to the actual Padua work. Final human review, permanent public
code/evidence release and final-ID cleanup at reviewed PR preparation remain. No submission or editor contact has taken place. The
publisher-template provenance is recorded in
[template/README.md](template/README.md): both used files now match the
user-supplied December2024 package byte for byte, resolving the initial
mirror comparison limitation.

## Author and template update — 7 November 2026

The author is Andrey Chesnokov, Department of Mathematical Sciences,
Norwegian University of Science and Technology,7491Trondheim,Norway;
correspondence and ORCID appear in the manuscript. Source: PaperF main.tex
at bttb-research commit5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54, read
under explicit permission to reuse these fields. F's science text and
its submitted-archive claim were not copied. No unperformed final human
checks are asserted; the Padua data-retention scope remains explicit.

Only main.tex front/back matter and PDF author metadata changed. Root
reviewed the diff against the source, verified the unchanged input graph
and all seven mathematical/bibliography source hashes from the accepted
Solmax review, and compiled the46-page update. No mathematical re-audit
or new scientific numerical execution was needed. The original audited
46-page PDF is preserved under local-output/.../paper/audited-46-pages/.
