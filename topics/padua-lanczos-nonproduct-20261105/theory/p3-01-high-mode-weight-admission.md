# PD-T?lanczos-nonproduct-codex-P3-01 — high-mode SH weight admission

ID kind: PD-T.
Aliases: sign checkerboard reweighting; full-support rank-two SH measure.
Split from: IDEA?lanczos-nonproduct-codex-P3-01 combined target; capacity/
radius is separately proved in P3-03.
Split into: none.

## Statement

For every integer n>=2, put m=n+2 and, for 1<=k,l<=m, define

    theta_k=k*pi/(m+1), s_k=cos(theta_k),
    v_k=2*sin(theta_k)^2/(m+1),
    a_k=U_(n+1)(s_k), z_kl=(s_k,2*s_k+s_l),
    w_eta,kl=v_k*v_l*(1+eta*a_k*a_l).

Here U_r is the second-kind Chebyshev polynomial, with U_0=1,
U_1=2s and U_(r+1)=2s U_r-U_(r-1). For every real eta with
0<|eta|<1, these weights define a positive probability measure mu_(n,eta)
on all M=m^2 distinct SH nodes. Its coordinate marginals in s=x,
t=y-2x are the original v_k measures. Evaluation of polynomials of total
degree <=n+1 is injective; in particular M>N_s=(s+1)(s+2)/2 for 0<=s<=n.
No invertible affine map of R^2 sends mu_(n,eta) to a product measure.
For algebraic eta the nodes and weights are exact algebraic data.

## Definitions

A finite measure is affine-product if an invertible affine map sends it
to nu_1 tensor nu_2, for positive probability measures nu_1,nu_2 on R.
The measure here has a two-dimensional convex hull, so any such factors
must each have at least two support points. This definition concerns the
weighted measure, not only its support.

## Assumptions

n>=2, 0<|eta|<1, real eta, and the displayed exact trigonometric nodes and
weights. There is no numerical rounding or node perturbation in the claim.

## Status by part

Overall status: PROVED (analytic admission; independent audit pending).

| Mathematical part | Status | Evidence |
|---|---|---|
| Positivity, normalization, marginals, algebraicity | PROVED | Finite sine identities below |
| Distinct nodes, injectivity, M>N_s | PROVED | Tensor interpolation argument below |
| Not affine-product | PROVED | Convex hull rigidity and a nonzero weight minor |

Candidate disposition: retained. At the round-1 boundary capacity and
uniform separation remained OPEN; the later P3-03 proves that separate target.

## Depends on

Only the elementary finite sine orthogonality reconstructed below. The
family is a weight variant of PD-T324's SH nodes; its nonproduct admission
is proved here, rather than inherited from that affine-product family.

## Checks

No computer-assisted proof or numerical experiment. Written proof only.
Independent review of hull rigidity and the rank criterion is requested.

## Sources

PD-T324 read fully for the predecessor family. No external theorem or
historical novelty assertion is a premise.

## Proof or evidence

For 1<=p<=m the vectors (sin(p*theta_k))_(k=1)^m are eigenvectors of
the symmetric path adjacency matrix with eigenvalues 2*cos(p*pi/(m+1)).
The eigenvalues are distinct, so these vectors are mutually orthogonal.
Their squared norm is (m+1)/2: write sin^2=(1-cos(2p*theta_k))/2
and use the finite geometric sum
sum_(k=1)^m cos(2p*k*pi/(m+1))=-1. Consequently

    sum_k v_k U_r(s_k) U_j(s_k) = delta_rj, 0<=r,j<=m-1.       (1)

Indeed sin(theta)U_r(cos(theta))=sin((r+1)theta), by the stated
recurrence. In particular sum v_k=1 and sum v_k U_(m-1)(s_k)=0.
Also

    a_k=sin(m*theta_k)/sin(theta_k)=(-1)^(k+1).                (2)

Thus every weight is positive, bounded between (1-|eta|)v_kv_l and
(1+|eta|)v_kv_l. Summing in either index annihilates its perturbation,
which proves the marginals and total mass. The s_k are distinct; the map
(s,t)->(s,2s+t) is invertible, so all nodes are distinct. Since cosines of
rational multiples of pi and their squared sines are algebraic, the data
are algebraic whenever eta is algebraic.

Suppose a polynomial p(x,y) of total degree <=n+1=m-1 vanishes at all
nodes. Its pullback q(s,t)=p(s,2s+t) has degree <=m-1 in each variable.
For fixed s=s_k, the polynomial q(s_k,t) vanishes at m distinct t values,
so it is zero. Write q(s,t)=sum_(j=0)^(m-1) c_j(s)t^j. Each c_j(s_k)=0
for every k and deg(c_j)<=m-1, hence every c_j=0. Therefore p=0.
Moreover m^2>(n+1)(n+2)/2=N_n, and N_s<=N_n for s<=n.

It remains to rule out a different affine-product representation. In
latent coordinates the support is S tensor S, S={s_1,...,s_m}; its hull is
the square [s_m,s_1]^2. Under any hypothetical affine map making the
measure a product, the product support is A tensor B, where A and B are
finite sets with at least two points. The image hull must therefore be
the axis-aligned rectangle conv(A) tensor conv(B). An invertible affine
map sends edges to edges and preserves their two parallel classes. Its
linear part consequently sends the two latent coordinate directions to
the two rectangle coordinate directions, in some order. Its matrix in
these coordinates has exactly one nonzero entry in each row and column.
Thus the two resulting coordinates are separate invertible affine
functions of s and t, possibly interchanged. Such changes only relabel
the rows and columns of the probability matrix. A product measure in
these axes would require the matrix (w_eta,kl) to have rank one.

Both signs in (2) occur. Choose rows k,k' with a_k=1,a_k'=-1 and
columns l,l' with a_l=1,a_l'=-1. The corresponding weight determinant is

    v_k v_k' v_l v_l' *
      [(1+eta*a_k*a_l)(1+eta*a_k'*a_l')
       -(1+eta*a_k*a_l')(1+eta*a_k'*a_l)]
      =4*eta*v_k*v_k'*v_l*v_l' != 0.

The weight matrix has rank at least two, a contradiction. This proves
non-affine-product admission for the full stated parameter range.

## Scope

This is an n-dependent weight family on affine-sheared tensor nodes. A
single fixed eta may be used for all n, but the density's polynomial
frequency changes with n. No conclusion about one fixed smooth density,
a nonlinear node map, or capacity equivalence follows from this admission.

## Open items

The later [P3-02](p3-02-exact-moments-creators.md) supplies matched moments/
creators and [P3-03](p3-03-uniform-capacity-radius.md) supplies the actual
normal-projected capacity/radius theorem. Independent audit and final
result-ID allocation belong to the coordinator.

## History

- 2026-11-05: Codex P3, assigned gpt-6.1-sol xhigh; rules/input
  ed5515ed84e0e7b12163175dce9f22a859c89c99. Gate followed proposal and
  preceded further pursuit; [canonical protocol disclosure](../LOG.md#canonical-protocol-disclosure--p3-gate-timing).
  Round-1 analytic admission, before capacity development.
- 2026-11-05: after round-2 development, linked the separate P3-02/03
  results; admission statement and proof unchanged.
