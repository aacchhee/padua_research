# PD-T?padua-argmax-bridge-20261105-codex-corner-01 — Per-degree aggregate corner radius reduction

ID kind: PD-T. Aliases: N3 practical corner radius; rational energy instantiation.
Split from: none; quantitative corollary of PD-T227 Scope (8).
Split into: finite arithmetic verification is recorded separately.

## Statement

For every integer n>=2 let Lambda_c, Lambda_n, W_n be exactly those of
PD-T227 at either parity-correct nonnode corner. Suppose real or rational
bounds satisfy 0<ell<=Lambda_c, W_n<=E and Lambda_n<=u. Define

    b=E/(n^4 ell), K=u/ell,
    kappa=min(1,1/[8(b+3K)]).

Then for inward physical h_x,h_y>=0 with c+h in the square and
0<H=h_x+h_y<=kappa/n^2,

    lambda_n(c+h)<=Lambda_c*(1-n^2 H/16)<Lambda_c.

## Definitions and assumptions

W_n=sum_(L_jk(c)!=0)(L_jk,x(c)^2+L_jk,y(c)^2)/|L_jk(c)|.
This omits precisely k=0,j>0 even, and includes 00. E bounds that
sum, not a sum of squared absolute-gradient totals. Coordinates H are
physical L1 increments. All arithmetic in the statement is exact.

## Status by part

Overall status: **PROVED** (analytic implication), supplementary review
and the required Claude audit pending. This claims no per-degree computer
bound. Candidate disposition: retained quantitative implementation variant.

## Depends on

PD-T227 (3), PD-T251 A_n,B_n<=-n^2 Lambda_c/8, and the named bound
hypotheses. PD-T368 supplies the optional exact choice

    u=110*(1+ceil(log2(n+1)))^2.

Indeed log(n+1)<=log2(n+1)<=ceil(log2(n+1)), since log 2<1.
The ceiling is computed by integer powers of two, not floating logs.

## Proof

W_n<=E<=b n^4 Lambda_c and Lambda_n<=u<=K Lambda_c follow from
ell<=Lambda_c. Put z=n^2 H. PD-T227 and the inherited slopes imply

    lambda_n(c+h)<=Lambda_c*[1-z/8+b z^2/2
                                  +K(exp(z)-1-z)].

For 0<=z<=1, the exponential series (or two integrations of exp)
gives exp(z)-1-z<=e z^2/2<3z^2/2. One elementary proof of e<3
is k!>=2^(k-1) for k>=1 with strict inequality for k>=3, hence
sum_(k>=0)1/k!<1+sum_(k>=1)2^(-(k-1))=3.
Since z<=kappa<=1 and z<=1/[8(b+3K)],

    (b+3K)z^2/2<=z/16.

Thus the bracket is at most 1-z/16. This proves the statement even
when affine or true cardinal signs change. The inherited reflection
permutation transfers the same Lambda_c and W_n to the second corner.

## Phase-box use (routine coordinate corollary)

In the corner-centered chart with scaled phases alpha=n*xi,
beta=(n+1)*eta, inward physical coordinates are

    h_x=2 sin^2(alpha/(2n)),
    h_y=2 sin^2(beta/(2(n+1))).

Consequently a phase box is covered if a rigorous upper bound on
their sum is <=kappa/n^2. A simple rational sufficient condition is

    alpha_max^2/2 + [n^2/(n+1)^2]*beta_max^2/2 <= kappa,

where alpha_max,beta_max bound the respective absolute phases. This
uses |sin t|<=|t|. For a symmetric box |alpha|,|beta|<=r, the
sufficient condition is r^2*(1+n^2/(n+1)^2)/2<=kappa.
Physical H, angular xi/eta and scaled alpha/beta are not interchangeable.

## Checks and sources

Pure elementary assembly of inherited local bounds; no computed value
is a premise. Per-degree finite bounds, reproducible commands and replay
status are in the separate N3-corner computation record. No external
source theorem or novelty claim.

## Scope and open items

This is local descent only. It does not certify a full degree, settle B2,
or change the global finite range. The larger-radius finite implementation
and distinct replay remain pending.

## History

2026-11-05, Codex, parent-assigned gpt-6.1-sol xhigh; input/rules
714f3cad18859c07cd13f31561f2a185f9591a7f. Actual serving metadata not
independently exposed. The algebra re-instantiates an existing mechanism.
