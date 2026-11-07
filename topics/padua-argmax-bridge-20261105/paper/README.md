# Constructive Approximation manuscript draft

[main.tex](main.tex) is the manuscript source. Build it using
[BUILD.md](BUILD.md); the compiled PDF stays outside Git at
`local-output/padua-argmax-bridge-20261105/paper/main.pdf`.

The user selected Constructive Approximation, permitted intermediate IDs,
and supplied the Morrow–Patterson paper as a style reference. The opening
therefore starts from interpolation and stability, gives the two main
results early, and explains the proof mechanisms before estimates.
Technical support is collected in appendices rather than interleaved
through the main narrative. The attached paper is not copied or committed.

## Mathematical scope

The two results are the sharp corner expansion H and exact all-degree
maximizer theorem G01. The corner expansion is analytic and independent
of the maximizer theorem. Its global transfer uses G01. The all-degree
maximizer result has explicit computer-assisted dependencies, including
a constant enclosure in the quantitative tail and finite certificates.
An eventual maximizer theorem already suffices for asymptotic transfer;
the finite bridge adds the all-degree equality classification.

The sharp expansion keeps the canonical constants:

- `N=n+1/2`, `a=2/pi`, `d=gamma+log(8/pi)`;
- `c1=a*d`, `b=2*a*c1`, `c=c1^2+kappa`;
- `Lambda_c = 4/pi^2 log^2 N + b log N + c - 1/N + O(log N/N^2)`.

The nodes are the even checkerboard at `(cos(j*pi/n),cos(k*pi/(n+1)))`.
The coefficient of the highest first-coordinate cardinal mode is one.
The exact two nonnode-corner maximizers depend on parity. The theorem
concerns the whole closed square, not the interpolation nodes alone.

## Source map

- `sections/preliminaries.tex`: PD-T101 normalization reconstructed by
  finite cosine orthogonality; classical published antecedents cited.
- `sections/corner-formula.tex`: PD-T159 positive Cauchy formula, F03
  exact partial rows, PD-T269/270 reference square and defect constant.
- `sections/asymptotics.tex` and `asymptotics-details.tex`: canonical
  `../theory/H-sharp-corner-expansion.md`, H01/H04/H05, with H06 as
  an independent development reconstruction. The exact analytic κ
  definition is used; its decimal enclosure is not a corner-proof premise.
- `sections/argmax.tex`, `argmax-details.tex`, `row-estimates.tex`,
  `model-estimates.tex`, `scalar-estimates.tex`: G01 and E14 analytic
  assembly, closed physical cover, quantitative row/model/defect support.
- `sections/certificates.tex`: `../compact-return.md`, G01,
  `../theory/native-finite-range.md`, frozen final hybrid-engine
  specifications, mathematical reduction and selective-retention boundary.
- `references.bib`: published node construction, leading asymptotics,
  corner observations, related geometry and generic mesh antecedents.
  Attribution is based on the bounded search in
  `../literature-refresh-20261107.md`; exhaustive priority is not claimed.

Earlier source locations for the corner formula and constants:
`topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md`,
`topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md`,
`topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md`,
and `t4-02-one-dimensional-remainder.md` in that last directory.

## Before submission

This is a research manuscript draft, not a submission-ready or independently
Claude-audited paper. Author names, affiliations, funding, contributions,
conflict disclosures and final AI-assistance wording must be completed by
the human authors. Source identifiers remain provisional where authorized;
normalization of IDs is deferred to PR preparation.

A complete standalone proof check and the pending substantive Claude audit
must assess the manuscript alongside its canonical theory and computational
records. The article must eventually include every needed supporting proof
or cite a suitable permanent, complete companion; an internal result ID
alone cannot fill that role. Any remaining explicit exposition obligations
are to be tracked below rather than silently treated as journal-ready.
A durable public code/evidence release and persistent locator also remain
to be arranged. Selective retention is intentional: all essential proofs
are returned, but only two sampled complete histories are retained locally.

The current Springer class and bibliography interface are used with pinned
mirror dependencies because official package downloads were blocked. See
[template provenance](template/README.md) for the exact access/version limit.
The official package should be compared or refreshed before submission.

## Build and review record

To be completed after the integrated build and supplemental manuscript check.
