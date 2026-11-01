# Primary-source verification for the two-dimensional Padua MZ campaign

Rules/base: `cf89b140530d5838bdb208a8c28f3e7aa676ace3`. Date: 2026-11-01.
Reader: Codex, mathematical worker allocated xhigh; runtime model metadata is
not independently exposed. Scope: source verification and convention matching,
not a proof audit, exhaustive novelty search, or mathematical status upgrade.
Only the orchestrator controls Git and shared registries.

## Foundation verdict

The campaign's signed Lebesgue rule is the integral of the degree-`m` Padua
interpolant. It has guaranteed total-degree exactness `m`, cardinality
`(m+1)(m+2)/2`, and mass four. It is distinct from the positive Padua rule for
the normalized product Chebyshev measure, whose degree of exactness is
`2m-1` and whose mass is one. Both constructions are classical. The
Chebyshev discrete orthogonality and checkerboard resonance are classical,
too. No all-degree signed Lebesgue `eta<1` theorem was found in the selected
primary portions below. This is a coverage-qualified report, not an absence
or novelty theorem.

The existing source reconstruction in
[definitions.md](definitions.md) matches the normalized primary foundation.
The correction on the exceptional highest mode must be retained. The
Sommariva--Vianello--Zanovello author preprint has a normalization discrepancy
in its displayed equation (25), detailed below; use the independently
normalized generating-curve theorem instead of copying that denominator.

## Exact conventions and formula to reproduce

Use the campaign convention

\[
z_{jk}=(\cos(j\pi/m),\cos(k\pi/(m+1))),\quad j+k\equiv0\pmod2,
\quad m\ge1.
\]

Let `c_j^(m)` be `1/2` at `j=0,m` and one otherwise. The positive Chebyshev
weights are

\[
a_{jk}=\frac{2c_j^{(m)}c_k^{(m+1)}}{m(m+1)}
=\frac1{m(m+1)}
\begin{cases}1/2&\text{vertex},\\1&\text{edge},\\2&\text{interior}.
\end{cases}
\]

Here `sum(a)=1`, and the measure is
`dmu_C=dx dy/(pi^2 sqrt(1-x^2)sqrt(1-y^2))`. Set
`p_rs=hat T_r(x)hat T_s(y)`, with `hat T_0=1` and
`hat T_r=sqrt(2)T_r` for `r>0`, and

\[
\mu_r=\int_{-1}^1\widehat T_r(t)\,dt=
\begin{cases}2&r=0,\\2\sqrt2/(1-r^2)&r>0\text{ even},\\0&r\text{ odd}.
\end{cases}
\]

Then the campaign's Lebesgue weights are

\[
w_{jk}=a_{jk}\left[
\sum_{r+s\le m}p_{rs}(z_{jk})\mu_r\mu_s
-\frac12p_{m0}(z_{jk})\mu_m\mu_0\right]. \tag{L1}
\]

Equivalently, for `h_r=integral T_r=2/(1-r^2)` at even `r` and zero at odd `r`,

\[
w_{jk}=a_{jk}\left[
\sum_{r+s\le m}2^{[r>0]+[s>0]}h_rh_sT_r(x_j)T_s(y_k)
-h_mh_0T_m(x_j)\right]. \tag{L2}
\]

These formulas follow by integrating the primary-source cardinal formula
`L_z=a_z(K_m(z,.)-T_m(x_z)T_m(x))`; this is an elementary convention
translation, not a new cubature construction. They imply the moment equations
in definitions.md and `sum(w)=4`. At odd `m` the exceptional integrated moment
vanishes, but the interpolation correction still matters as an operator.

The generating-curve paper uses the swapped orientation
`gamma_m=(cos(mt),cos((m+1)t))`; its exceptional coordinate is `y`, while the
campaign's is `x`. Swapping its coordinates gives exactly the campaign's even
checkerboard. SVZ equation (24) uses the odd checkerboard on the campaign's
axis sizes. Reflect the coordinate whose denominator is odd to obtain the
even checkerboard. Both measures are reflection invariant, and equations
(L1)--(L2) retain the displayed form.

The positive rule is exact on `Pi_(2m-1)`, and also on degree-`2m` polynomials
whose coefficient of `T_(2m)(x)` vanishes. Consequently standard Chebyshev
hyperinterpolation using this rule reproduces `Pi_(m-1)`. The corrected
degree-`m` interpolant reproduces `Pi_m`. These statements concern the
Chebyshev basis and measure; they do not make the signed Lebesgue
hyperinterpolant a projection on `Pi_(m-1)`.

## Source records

### LIT-312 — generating-curve foundation, primary published text read

Bos, **Caliari**, De Marchi, Vianello, Xu, *Bivariate Lagrange interpolation at
the Padua points: the generating curve approach*, J. Approx. Theory 143
(2006), 15--25. [DOI](https://doi.org/10.1016/j.jat.2006.03.008),
[published author copy](https://profs.scienze.univr.it/caliari/pdf/BCDMVX06.pdf),
[earlier preprint](https://www.math.unipd.it/~marcov/pdf/PaduaCurve3.pdf).

Coverage: published pp. 16--21, equations (1)--(9), Lemma 1 and Theorems 1--2;
preprint PDF pp. 3--9 inspected first. Theorem 1, published p. 19, gives
positive weights `{1/2,1,2}/[m(m+1)]` and exactness in `Pi_(2m)` excluding the
exceptional `T_(2m)(y)` coefficient. Published p. 20 explicitly identifies
precision `2m-1`. Theorem 2, pp. 20--21, gives the corrected cardinal kernel.
This directly supports (L1)--(L2) after swapping axes. The theorem proofs were
read for normalization and exceptional-mode bookkeeping, not independently
audited as an entire paper. No signed Lebesgue hyperinterpolation theorem is
being attributed to it.

### LIT-427 — signed Lebesgue cubature, author preprint read

Sommariva, Vianello, Zanovello, *Nontensorial Clenshaw--Curtis cubature*,
Numer. Algorithms 49 (2008), 409--427.
[DOI/journal](https://link.springer.com/article/10.1007/s11075-008-9203-x),
[author preprint](https://www.math.unipd.it/~marcov/pdf/hyperquad.pdf).

Coverage: preprint §§2--3.3 selected, especially equations (16)--(19),
(24)--(36), PDF pp. 6--12. Equations (19), (31), (33), (36) give normalized
Chebyshev moments, the half correction, integrated-interpolant weights, and
degree-`m` exactness. PDF p. 12 explicitly allows negative weights. Equation
(18) gives `sum(abs(w))->4`: this controls the integration functional.

**Preprint-specific discrepancy:** its equation (25), as extracted by the
public web tool, prints denominator `(n+2)(n+3)`. Its equation (24) has grid
denominators `n+1,n+2` and interpolation degree `m=n+1`; normalization instead
requires `(n+1)(n+2)=m(m+1)`, verified in record 01. The printed denominator
would multiply the unit Chebyshev mass by `(n+1)/(n+3)`. This discrepancy is
not called a journal error or erratum: the journal body was not compared.
Publisher access was subscription-preview only.

### LIT-428 — CDMV hyperinterpolation is at Xu points

Caliari, De Marchi, Vianello, *Hyperinterpolation on the square*, J. Comput.
Appl. Math. 210 (2007), 78--83.
[DOI](https://doi.org/10.1016/j.cam.2006.10.058),
[six-page article-in-press author copy](https://profs.scienze.univr.it/caliari/pdf/preCDMV06.pdf),
[earlier ten-page preprint](https://www.math.unipd.it/~marcov/pdf/hypXu.pdf).

Coverage: article-in-press §§1--3, equations (1)--(17), Theorem 1; not the
numerical table entries in detail. Its general definition assumes positive
weights and exactness through `2n`. Section 2 uses Xu/MPX square-grid points
for normalized product Chebyshev measure. For its odd degree `n`, the rule
has exactness `2n+1`, interior weights `2/(n+1)^2` and boundary weights
`1/(n+1)^2`, and yields degree-`n` hyperinterpolation. Theorem 1 bounds its
uniform-norm Lebesgue constant by `O(log^2 n)`. This paper is not a Padua
signed-Lebesgue hyperinterpolation theorem. The six-page article-in-press
copy agrees with the earlier preprint on these hypotheses; final pagination
was verified through journal metadata, not a separate final PDF comparison.

### LIT-014 — Dencker--Erb checkerboard orthogonality

Dencker, Erb, *Multivariate polynomial interpolation on Lissajous--Chebyshev
nodes*, J. Approx. Theory 219 (2017), 15--45.
[DOI/journal](https://doi.org/10.1016/j.jat.2017.03.003),
[primary v2 PDF](https://arxiv.org/pdf/1511.04564v2),
[primary HTML](https://arxiv.org/html/1511.04564).

Coverage: §2 definitions, Proposition 2.5/equations (2.12)--(2.18), Theorems
2.7--2.10 and Remark 2.11; PDF pp. 12--18 and corresponding HTML inspected.
For nonnegative frequency indices, Proposition 2.5 says that a discrete
product-cosine moment is nonzero precisely at `gamma_i=h_i n_i` with
`sum(h_i)` even, when it equals one. The weights in (2.13) are
`2^(number of interior coordinates)/(2 product(n_i))`. Theorem 2.7 gives
orthogonality with an exceptional endpoint mode; Theorem 2.10 derives
quadrature for normalized product Chebyshev measure. Taking
`(n_1,n_2)=(m,m+1)` recovers the positive checkerboard resonance behind D1.
These are direct prior sources for that mechanism, not signed Lebesgue
spectral estimates. The 2017 journal body was not separately compared.

### LIT-379 — Kolomoitsev--Lomako uniform Lebesgue asymptotics

Kolomoitsev, Lomako, *Asymptotics of the Lebesgue constants for bivariate
approximation processes*, Appl. Math. Comput. 403 (2021), 126192.
[DOI/journal](https://doi.org/10.1016/j.amc.2021.126192),
[primary v1 PDF](https://arxiv.org/pdf/2009.07114v1),
[primary HTML](https://arxiv.org/html/2009.07114).

Coverage: introduction, §2.1 definitions/cardinal formula, Theorem 2.1;
Lemma 3.4 and its use were inspected. The displayed Padua consequence is
`Lambda_m=(4/pi^2)log^2(m)+O(log m)`. This is the
`C([-1,1]^2)->C([-1,1]^2)` norm of an interpolation process. Lemma 3.4 is a
one-dimensional trigonometric `L1` sampling estimate, not a signed Lebesgue
quadratic-form bound. The printed anisotropic interpolation-space convention
must be translated before using its cardinal formula for a fixed total-degree
space; no such transfer is assumed here. The precise norm mismatch already
prevents treating this asymptotic as the campaign's endpoint Gram theorem.
Journal body inaccessible (403); theorem attribution is to the inspected
arXiv version, with published metadata only.

### LIT-314 — Xu 1996 MZ inequality uses Chebyshev measure and Xu nodes

Xu, *Lagrange interpolation on Chebyshev points of two variables*, J. Approx.
Theory 87 (1996), 220--238.
[DOI/journal](https://doi.org/10.1006/jath.1996.0102),
[author PDF](https://pages.uoregon.edu/yuan/paper/JAT96.pdf).

Coverage: introduction, node/space definitions (2.14),(2.19), §3 Theorems
3.1/3.3 and Lemma 3.5, author-PDF pp. 10--13; selected proof text, not a
full proof audit. Theorem 3.3 gives, for `1<p<=infinity`, a continuous
product-Chebyshev `Lp` norm bounded by the equally weighted nodal `lp` norm
on the specified Xu interpolation space `V_n`. Lemma 3.5 supplies the forward
inequality for `Pi_n`. Theorem 3.1 is continuous-input mean convergence.
The nodes are Xu near-minimal cubature nodes on a square Chebyshev grid,
not the campaign's adjacent-denominator Padua set. This is genuine bivariate
MZ prior art with different measure, nodes, and weights; it does not establish
a signed Lebesgue Padua MZ bound. Final journal PDF was not compared to the
author version.

### LIT-045 — ASV context independently checked in author text

An, Sommariva, Vianello, *On the role of weak Marcinkiewicz--Zygmund
constants in polynomial approximation by orthogonal bases*.
[arXiv v1](https://arxiv.org/html/2601.04708v1),
[author sixteen-page PDF](https://www.math.unipd.it/~marcov/pdf/MZ.pdf),
[published DOI](https://doi.org/10.1016/j.matcom.2026.10.001),
[journal locator](https://www.sciencedirect.com/science/article/pii/S0378475426004416).

Coverage: author PDF introduction/equations (1)--(11), §§3.1--3.2, selected
§3.6; arXiv introduction read independently. In §3.1, PDF p. 7, the authors
describe the observed CC range `floor(m/2)<n<=m-1`, then say that this
behaviour is, to their knowledge, “not known” and merits study. The explicit
sentence is in the **CC** discussion. Section 3.2, PDF p. 8, reports Padua
`eta<1` up to `n=m-1` in the finite experiment (`m<=20`, `n<=30`). The
general introduction assumes positive weights; this is not justification for
applying its positive-rule estimates to signed Padua weights. The published
version, MCS 252 (2027), 733--745, was read by the earlier campaign reader,
but its body was not independently reachable here. Its exact wording remains
a **reported published-source** fact; the author-text wording above is directly
verified.

## Coverage limits and follow-up references

The base records `literature/records/mz-*`, prior-art report/comparison/
translation, and M2 foundation were consulted. The full literature index was
accessed, its identifiers/source headings scanned, and MZ/Padua-relevant rows
read. Existing reports of fulltext access are not inherited as this reader's
own source inspection. No source PDF or complete extract is stored in Git.
Public web search/open/find tools supplied the reading; shell Internet access
was not used. Screenshot attempts failed or resolved unreliably and are not
claimed as visual confirmation.

Additional discovered lead: Kolomoitsev--Lomako--Prestin, *On Lp-error of
bivariate polynomial interpolation on the square*, JAT 229 (2018), 13--35,
[DOI/journal](https://doi.org/10.1016/j.jat.2018.02.005),
[author PDF](https://www.math.uni-luebeck.de/mitarbeiter/prestin/ps/biv-pol-inter.pdf).
The publisher abstract and author title/abstract were inspected; body retrieval
failed (502). Its theorems are **FULLTEXT UNVERIFIED** here.

The related four-author Dencker--Erb--Kolomoitsev--Lomako paper, *Lebesgue
constants for polyhedral sets and polynomial interpolation on
Lissajous--Chebyshev nodes*, J. Complexity 43 (2017), 1--27,
[DOI/journal](https://doi.org/10.1016/j.jco.2017.05.001),
[arXiv v2](https://arxiv.org/html/1608.03451), was reached and its
introduction/abstract inspected. It is another uniform Lebesgue-constant lead;
no theorem from its uninspected sections is used.

Final-version gaps: SVZ journal body; Dencker--Erb journal comparison;
Kolomoitsev--Lomako journal comparison; Xu journal comparison; independently
readable ASV published body. Each DOI and journal locator is supplied above.
These gaps do not prevent use of the directly inspected author-version
formulas with their stated provenance. No exhaustive novelty clearance follows.
