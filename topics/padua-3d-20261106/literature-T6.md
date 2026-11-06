# T6 primary literature and exact coverage

Rules/input: `ccd9e905d19c0c625c196c4a3f3e707058ed042a`.
Reader: Codex, gpt-6.1-sol xhigh, 2026-11-06. Provisional IDs only;
coordinator owns the shared literature registry. No third-party fulltext
is copied into this repository.

The logarithmic-cubed universal cube lower bound is **LITERATURE**, not a
new T6 discovery. Subbotin's Theorem 1 supplies the general interpolation
comparison and his Corollary 3 supplies logarithmic growth. T6 retains
separate local analytic proofs with explicit constants. Those proofs use
no imported lower-bound theorem as a premise.

## LIT?padua-3d-codex-T6-01 — exact Fourier theorem coverage

Peter Dencker, Wolfgang Erb, Yurii Kolomoitsev and Tetiana Lomako,
*Lebesgue constants for polyhedral sets and polynomial interpolation on
Lissajous–Chebyshev nodes*, Journal of Complexity **43** (2017), 1–27,
DOI [10.1016/j.jco.2017.05.001](https://doi.org/10.1016/j.jco.2017.05.001).
Primary author preprint:
[arXiv 1608.03451v2](https://arxiv.org/abs/1608.03451v2), revised
10 November 2017; [PDF](https://arxiv.org/pdf/1608.03451).

- Status: LITERATURE; addendum/precise coverage for the existing aggregate
  LIT-380, not a claim that this is a previously absent source.
- Read: PDF lines 0–1037 (pp. 1–9 opening), 3368–3986 (pp. 20–23 opening),
  and 4288–5129 (pp. 25–29); abstract and institutional metadata.
  Theorem 2.3 statement and its complete main proof were read; intervening
  auxiliary proofs were not all read. Theorem 3.4 and its proof were read.
- Statement/hypotheses: Theorem 2.3, PDF p. 6, for fixed rational `r>0`
  and every integer side vector `m in N^d`, gives Fourier Lebesgue norms
  of both the nonnegative simplex `sum gamma_j/m_j<=r` and its sign
  symmetrization comparable to `product log(m_j+1)`. Constants may depend
  on d,r. This theorem has no pairwise-coprime hypothesis.
- Exact T6 match: `r=1,m_j=n` makes the symmetrization precisely
  `{k in Z^d:sum |k_j|<=n}`. The norm uses probability Haar measure.
- Transfer locator: equation (3.15), PDF pp. 26, uses factor `3^-d`
  and credits Subbotin's Theorem 1. Theorem 3.4 concerns its specified LC
  interpolation spaces; arbitrary total-degree nodes are not its statement.
- Gaps: complete auxiliary proof audit and journal/preprint comparison.

## LIT?padua-3d-codex-T6-02 — universal cube comparison and growth

Yu. N. Subbotin, *The Lebesgue constants of certain m-dimensional
interpolation polynomials*, Mathematics of the USSR-Sbornik **46**(4)
(1983), 561–570, DOI
[10.1070/SM1983v046n04ABEH002952](https://doi.org/10.1070/SM1983v046n04ABEH002952).
Original Russian publication: Matematicheskii Sbornik **118**(160),
4(8) (1982), 557–566. Primary
[Math-Net metadata](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=2832&wshow=paper)
and [English fulltext](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=2832&what=fullteng).

- Status: LITERATURE, new provisional source record; searched the shared
  INDEX/records for Subbotin, title and DOI with no existing match.
- Read: full English text layer, PDF pp. 1–10, lines 0–417. Definitions,
  Theorem 1, Lemmas 1–2, Corollary 1 and proof, and Corollary 3 were read
  closely (journal pp. 561–565). Later bivariate construction read at
  text-layer level, without independently checking its detailed estimates.
- Hypotheses: polynomial exponents are integer points of a convex region
  symmetric in coordinate hyperplanes; Remark 1 permits the corresponding
  coordinatewise downward-closed exponent condition. Nodes form a set of
  existence, meaning interpolation is uniquely solvable for all data.
- Statement: Theorem 1, journal p. 562, bounds every such interpolation
  norm below by `3^-d` times the associated full Fourier projection norm.
  Corollary 1, p. 564, covers arbitrary projections on the even space.
  Corollary 3, p. 565, gives `c_d log^d R` when the symmetric spectral
  region contains a Euclidean ball of radius R.
- Exact T6 match: the l1 ball of radius n is convex, sign symmetric,
  downward closed, and contains the Euclidean ball of radius `n/sqrt(d)`.
  Thus the universal total-degree cube logarithmic order is already known.
- Gaps: the cited Yudin lower-bound proof underlying Corollary 3 was not
  separately read. No priority claim for T6's displayed explicit constant.

## LIT?padua-3d-codex-T6-03 — original Padua introduction and its scope

Len Bos, Marco Caliari, Stefano De Marchi, Marco Vianello and Yuan Xu,
*Bivariate Lagrange interpolation at the Padua points: the generating
curve approach*, Journal of Approximation Theory **143**(1) (2006), 15–25,
DOI [10.1016/j.jat.2006.03.008](https://doi.org/10.1016/j.jat.2006.03.008).
Primary [IRIS record](https://iris.univr.it/handle/11562/312256) and
[author preprint PDF](https://iris.univr.it/retrieve/e14ff6e4-213a-0209-e053-6605fe0ad24c/preBCDMVX06.pdf).

- Status: LITERATURE, scope clarification for an existing Padua source;
  coordinator should link an existing source ID rather than duplicate it.
- Read: PDF lines 0–490, pp. 1–8 opening, including the introduction and
  total-degree definition. Remaining fulltext was not read in this task.
  The caliari site timed out; a later IRIS page request returned HTTP 403.
- Scope: the introduction's displayed `C(log n)^d` lower bound is stated
  for tensor-product polynomial interpolation. The following paragraph
  discusses attaining that rate in the total-degree setting. The displayed
  tensor inequality alone is not a proof for every total-degree node set.
- The nearby Sündermann citation concerns projections on the unit ball,
  not the cube. T6 does not import a cube theorem from that citation.
- Gap: no complete-paper or bibliography audit; these observations concern
  the inspected introductory passage only.

## Searches, inherited records and access limits

The initial survey preceded local proof development. Primary web searches
included Sündermann/Sundermann projection constants for polynomial spaces,
Lozinski/Kharshiladze projection lower bounds, total-degree cube Lebesgue
lower bounds, and polyhedral/simplex Fourier sums. The DEKL proof later
exposed the precise Subbotin attribution; that fulltext was then read and
the disposition strengthened to an explicit known-source match.

Full local predecessor records read: LIT-379 (Kolomoitsev–Lomako 2021),
LIT-488 (Kolomoitsev–Lomako–Prestin 2018), LIT-512
(Kolomoitsev–Liflyand 2021), and `dencker-erb-2017.md` (LIT-014).
Their inherited published-proof coverage is not enlarged by this task.
DEKL is distinct from the two-author Dencker–Erb interpolation paper.

Older leads not read as primary proofs: Baiborodov 1982, Podkorytov 1981,
Yudin 1979 and Travaglini 1993. The Travaglini primary PDF request at
`matwbn.icm.edu.pl/ksiazki/cm/cm65/cm65112.pdf` returned HTTP 403.
These are search leads, not verified premises or absence evidence.

## Relation to the retained local records

- PD-T?padua-3d-codex-T6-01 locally proves the same known `3^-d`
  comparison with every multiplier and real operator norm written out.
- PD-T?padua-3d-codex-T6-02 locally proves
  `||D_n^3||_1 >= H_floor(n/2)^3/(24*pi^3)` by a bounded dual test.
- Combining them gives `Lambda>=max(1,H_floor(n/2)^3/(648*pi^3))`.
  The explicit coefficient is coarse. No sharp constant or matching 3-D
  interpolation construction is supplied; the latter campaign target
  remains OPEN.

2026-11-06 history: survey, explicit local proofs and finite sanity;
subsequent source-trail refinement identified Subbotin's exact prior
comparison and general logarithmic lower bound. No registry edits.


## Audit-response coverage qualification — 2026-11-06 — m6/m15

Subbotin's Russian original is Mat.Sb.118(160):4(8) (1982),557–566;
1983 names the English translation Math.USSR-Sb.46(4),561–570. The
Theorem1/Cor1/Cor3 attribution above rests on the recorded developer primary
read. Cor3 uses Yudin's bound, whose source was not read. The supplementary
Astra check did not verify attribution; Claude audit-01 could not retrieve
Subbotin, and this response did not acquire it anew. The locally written
proofs were accepted independently and use no source theorem as a premise.
Do not describe this as independently established primary-source verification.
Dedicated Subbotin registration and DEKL's consolidation out of aggregate
LIT-380 are tasks for PR preparation, not ID allocation in this response.

Additional comparator LIT-391 reports Wang–Wang–Wang 2014 cube
hyperinterpolation norm O(log^d n), with UNVERIFIED secondary coverage in
INDEX and the programme baseline. It provides matching-order operator
context, not N-node total-degree interpolation or a locally verified source
upper bound. No new fulltext read is claimed.
