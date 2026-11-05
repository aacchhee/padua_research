# PD-T?argmax-effective-2-codex-07 — All-degree physical corner descent at scale n^-2

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

## Status by part

Overall status: **PROVED**, using the separately stated PROVED
dependencies below, with no unresolved mathematical hypothesis.
Supplementary final-file check and required Claude audit pending at
first writing; independent checker has accepted the antecedent arguments.

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
constant. The independent checker must review this final assembly and
the exact dependency hashes. No external theorem or priority claim.

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
corner. No third corner is included in this statement.

## Scope

This closes the existence of an explicit all-degree physical radius of
order n^-2. It does not establish descent on the larger rho<=1/64 zone
proposed in H1/H2, nor certify a degree outside the inherited finite
global range. The proven constant is too small to infer a practical
box-count or runtime pass without the actual H1 cover measurements.
PD-N085 remains valid: the proof allows individual affine sign changes
and controls their aggregate cost via W_n.

## Open items

Independent final-file check and required Claude audit; sharper radius
constants or per-degree corner bounds for practical H1 coverage; full
near-coset and far-region assembly. PD-T099 remains OPEN.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra; rules/input
ed21cc0bf205549936fccde90244a291bc6de324. This strengthens the radius
scale beyond PD-T251's physical n^-6 neighborhood while retaining its
all-degree slope theorem as a dependency. Original H3's larger practical
corner-box objective remains recorded; no final ID allocated.
