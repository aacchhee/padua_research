# PD-T369 (PD-T?argmax-effective-2-codex-07) — All-degree physical corner descent at scale n^-2

ID kind: PD-T.
Aliases: H3 fixed scaled local radius; aggregate sign-change corner comparison.
Split from: PD-T227/IDEA-330's uniform physical corner-radius obligation.
Split into: energy and global-norm estimates are separate PD-T records.

## Statement

For every integer n>=2 and every h_x,h_y>=0 with
0<H=h_x+h_y<=10^-11/n^2, the even-checkerboard Padua Lebesgue function
at the nonnode corner c=(-1,-1) satisfies

\[
\lambda_n(c+(h_x,h_y))
\le\Lambda_c(n)-\frac1{16}n^2\Lambda_c(n)H<\Lambda_c(n).     \tag{1}
\]

The identical statement holds in inward coordinates at the other
parity-correct nonnode corner, for both parities. The radius constant
10^-11 is explicit and independent of n.

## Definitions and assumptions

Use PD-T101's corrected cardinal polynomials, PD-T227's inward slopes
A_n,B_n and weighted energy W_n, and Lambda_n=max lambda_n. h_x,h_y are
physical, not angular, increments. Exact arithmetic, no sign-stability
or global argmax hypothesis. This radius lies inside the physical square.
Here H=h_x+h_y denotes physical L1 distance, whereas H in T05/T06 is
1+log(n+1). In the scope comparison below N=n(n+1) is the mesh product,
not PD-T101's node count.

## Status by part

Overall status: **PROVED**, using the separately stated PROVED
dependencies below, with no unresolved mathematical hypothesis. Dated
review note, 2026-11-05: Claude [audit-01](../audit-01.md) accepted T07
at its original scope, including its dependence on T05/T06 as accepted
in that audit. First-writing review-pending wording is superseded;
the record response check remains pending.

| Part | Status | Evidence / limitation |
|---|---|---|
| Descent and loss (1) on the stated radius | PROVED | Accepted PD-T251, T05/T06 and PD-T227 (3) |
| Transfer to the second nonnode corner | PROVED (routine invariance) | PD-T228, end of §4; node/weight permutation, detailed below |

Candidate disposition: retained local theorem. PD-T099 is still OPEN.

## Depends on

- PD-T251: A_n,B_n<=-n^2 Lambda_c/8 for all n>=2.
- [corner-weighted-energy.md](corner-weighted-energy.md), provisional T05:
  W_n<=10^10 n^4 Lambda_c for all n>=2.
- [corner-global-norm-ratio.md](corner-global-norm-ratio.md), provisional T06:
  Lambda_n<=30000 Lambda_c for all n>=2.
- PD-T227, inequality (3), including its initially zero cardinals and
  its scalar absolute-value bound across affine sign changes.

## Checks and sources

Pure analytic assembly; no numerical data, runtime projection or fitted
constant. The supplementary reconstruction and Claude audit-01 cover
the original assembly and dependencies. No external theorem or priority claim.

Closest predecessors are [PD-T227 §Scope, (8)](../../padua-argmax-alln-20261101/theory/gated-codex-13-corner-first-variation.md)
and [PD-T228](../../padua-argmax-alln-20261101/theory/gated-codex-14-reflection-first-corner-bound.md).
The former already gives kappa=min(1,a/(b+eK)) under its slope, energy
and norm premises; T07 instantiates that mechanism with a=1/8,
b=10^10 and K=30000. PD-T228 already supplies physical radius
2^-17/n² under its condition (2), in particular for log n>=10^7.
T07's distinction is an explicit constant valid for every n>=2; it
does not introduce the n^-2 scale or improve PD-T228's eventual constant.

## Proof

PD-T227 gives, without requiring any cardinal to keep its sign,

\[
\lambda_n(c+h)\le\Lambda_c+A_n h_x+B_n h_y+\tfrac12W_n H^2
 +\Lambda_n[\exp(n^2H)-1-n^2H].                            \tag{2}
\]

Let z=n^2H. Since 0<z<=10^-11<1 and e<3,
exp z-1-z<=3z^2/2. Insert the three explicit dependency bounds in (2):

\[
\lambda_n(c+h)\le\Lambda_c
 \left[1-\frac z8+\frac{10^{10}+90000}{2}z^2\right].       \tag{3}
\]

For z<=10^-11,
(10^10+90000)z/2<=0.05000045<1/16.
Thus the bracket in (3) is at most 1-z/16, proving (1).
The node-preserving x reflection for even n and y reflection for odd n
transfers the same cardinals, slopes and energy to the second nonnode
corner. Explicitly j maps to n-j for even n, or k to m-k for odd n
(when m is even): both maps preserve j+k even and endpoint weights,
and interpolation uniqueness permutes the cardinals, preserving inward
slopes and energy. This is PD-T228's proof §4, final paragraph.
No third corner is included in this statement.

## Scope

This closes the existence of an explicit all-degree physical radius of
order n^-2. It does not establish descent on the larger rho<=1/64 zone
proposed in H1/H2, nor certify a degree outside the inherited finite
global range. The proven constant is too small to infer a practical
box-count or runtime pass without the actual H1 cover measurements.
PD-N085 remains valid: the proof allows individual affine sign changes
and controls their aggregate cost via W_n.

Range comparison and recorded combination of accepted theorems (not a new
target or a replacement of (1)): PD-T251 gives strict descent for physical
H<=1/(2N³), while T07 gives (1) for H<=10^-11/n². The usable all-degree
strict-descent radius from these two results is therefore
max(1/(2N³),10^-11/n²). T07's radius is larger exactly for integer n>=473;
PD-T251's is larger for 2<=n<=472. Each theorem retains its own loss
estimate on its own domain: the stronger loss in (1) is not asserted on
the whole maximum radius. PD-T228's larger eventual radius remains
available under its separate stated condition.

## Open items

Record response check; sharper radius
constants or per-degree corner bounds for practical H1 coverage; full
near-coset and far-region assembly. PD-T099 remains OPEN.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra; rules/input
ed21cc0bf205549936fccde90244a291bc6de324. This strengthens the radius
scale beyond PD-T251's physical n^-6 neighborhood while retaining its
all-degree slope theorem as a dependency. Original H3's larger practical
corner-box objective remains recorded; no final ID allocated.

2026-11-05 audit response, Codex, gpt-6-astra ultra: F2 qualifies the
first-writing "strengthens" description above by the exact n>=473 radius
comparison and cites PD-T227/228. The scale existed already in PD-T228;
the distinction is all-degree validity. The usable max radius is only a
recorded combination of accepted strict-descent theorems, not a new claim
registration or an extension of (1)'s loss bound. F9 and E1/E2 add the
existing reflection justification, accepted-dependency review note and
notation. The original Statement, constants and PROVED status remain
unchanged; the sole proof-body addition explains the already cited symmetry.

## Registration — 2026-11-05

Final ID: **PD-T369**. Preserved provisional alias: `PD-T?argmax-effective-2-codex-07`.
Registration input/rules: `5821c3f130ec0b1e33ad1d01620b67620e1f0be1`.

The explicit every-n>=2 instantiation of PD-T227 Scope (8) is registered, with its loss bound confined to radius 10^-11/n^2. PD-T228 already gives an eventual n^-2 radius; combining strict-descent domains with PD-T251 does not extend either loss estimate.

[Claude audit-01](../audit-01.md) accepted the mathematical scope;
[response-check-01](../response-check-01.md) accepted the record response.
Earlier provisional/no-final-ID and pending-response-check wording above
is retained as history and is superseded only administratively by this
registration. Every pre-existing paragraph after the heading, including
Statement, proof, status, displays and History, is preserved byte for byte.
The [final-ID map](../preparation/final-id-map.json) and
[registration notes](../preparation/registration-notes.md) record the mapping
and preparation limits. PD-T099 remains OPEN; the global certified range
remains exactly 2–32.
