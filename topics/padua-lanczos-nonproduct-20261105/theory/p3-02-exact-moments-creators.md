<a id="pd-tlanczos-nonproduct-codex-p3-02--exact-high-mode-moments-and-creators"></a>

# PD-T479 — exact high-mode moments and creators

Provisional alias: `PD-T?lanczos-nonproduct-codex-P3-02`.

ID kind: PD-T.
Aliases: invisible checkerboard moments; matched normalized SH creators.
Split from: IDEA-576 combined target.
Split into: none.

## Statement

Fix n>=2, m=n+2, and the measure mu_(n,eta) of
[P3-01](p3-01-high-mode-weight-admission.md), 0<|eta|<1. Let nu_n denote
the original SH measure (eta=0). Then mu and nu agree on every physical
polynomial of total degree <=2n+1. They do not agree on all polynomials
of degree 2n+2.

Order (r,j) by increasing d=r+j and then increasing j, corresponding to
the monomial x^r*y^j. For d<=n the exact graded orthonormal columns for
both prescribed rules, represented in ordinary Euclidean coordinates, are

    q_rj^eta = (sqrt(w_eta,kl)*U_r(s_k)*U_j(s_l))_kl.

The monic polynomial is b_rj(x,y)=2^(-d)U_r(x)U_j(y-2x), with squared
weighted norm d_rj=4^(-d). For parents (a,b) of degree <=n-1,

    Xq_ab=(q_(a+1,b)+q_(a-1,b))/2,
    Yq_ab=q_(a+1,b)+q_(a-1,b)
                 +(q_(a,b+1)+q_(a,b-1))/2,                  (1)

where X=diag(s_k), Y=2X+T and T=diag(s_l); a negative index denotes zero.
Both BJ and mirror have positive target pivot beta=1/2. Their exact
relative-raw-product source scales are

    sigma_X,ab^2=(1+1_(a>=1))/4,
    sigma_Y,ab^2=1+1_(a>=1)+(1+1_(b>=1))/4.                 (2)

Finally e=q_(n+1,0)^eta has Euclidean norm one and is orthogonal to
the represented Pi_n space for every eta in this interval.

## Definitions

BJ chooses X from (r-1,0) when j=0 and Y from (r,j-1) when j>0.
Mirror chooses X from (r-1,j) when r>0 and Y from (0,j-1) when r=0.
All-prior exact projection and positive normalization are used in this
order. sigma is the norm of the raw product A q_parent at the exact run,
not the residual norm beta. The two rules retain their own sigma values.

## Assumptions

The exact finite positive measure and operators above. Sources and
capacity are not needed to state the moment and creator identities.

## Status by part

Overall status: PROVED (written analytic proof; accepted at stated scope in [audit 01](../audit-01.md)).

| Mathematical part | Status | Evidence |
|---|---|---|
| Moment equality through 2n+1 and strict difference at 2n+2 | PROVED | Separable finite sum below |
| Exact bases, monic factors, pivots, creators and scales | PROVED | Matched moments and recurrence |
| Unit normal vector e | PROVED | Degree 2n+1 pairing and sign identity |

Candidate disposition: retained. Capacity application is a separate result.

## Depends on

[P3-01](p3-01-high-mode-weight-admission.md), including its proved sine
orthogonality and a_k=U_(n+1)(s_k)=(-1)^(k+1). The creator identities
are the exact PD-T324 identities, justified for these new weights here.

## Checks

Analytic proof only; no symbolic/numerical experiment or finite scan.
Independent mathematical reconstruction was accepted in [audit 01](../audit-01.md).

## Sources

PD-T039 is the moment-matching predecessor, not a capacity-transfer premise.
PD-T324 supplies the reference order/rules. No external theorem is used.

## Proof or evidence

Let L(f)=sum_k v_k f(s_k), and write a=U_(n+1). P3-01 proves that
L(a*p)=0 for every univariate polynomial p of degree <=n, because
U_0,...,U_n span that space and are orthogonal to a. For a latent
monomial s^A*t^B, the change in its integral is exactly

    eta*L(a(s)*s^A)*L(a(t)*t^B).                             (3)

If A+B<=2n+1, at least one of A,B is <=n, so (3) is zero. By linearity
all latent polynomials of that total degree match. The invertible linear
substitution s=x,t=y-2x preserves total degree, proving physical matching.
At degree 2n+2 the polynomial a(s)a(t) has nu-integral zero and mu-integral
eta*L(a^2)^2=eta, using a_k^2=1. Thus the asserted boundary is exact.

Products of any two U_r(s)U_j(t) of degree <=n have total degree <=2n.
Their Gram matrix under mu is therefore the same identity matrix as under
nu. The top homogeneous part is 2^d*x^r*(y-2x)^j; it has coefficient
2^d at x^r*y^j and only earlier monomials otherwise. These orthonormal
polynomials consequently are exactly the graded Gram–Schmidt columns.
Dividing by 2^d gives the unique monic polynomials and their norm 4^-d.

Multiplication by s or t and the U recurrence give (1) as polynomial
identities before representation. Every nonzero term when applied to a
parent of degree <=n-1 has degree <=n, so its represented orthogonality
has just been proved. In an X creator the other term precedes the target.
In either Y creator the term q_(r+1,j-1), when present, has the same
degree but smaller j, and the other non-target terms have smaller degree.
All-prior projection hence leaves exactly (1/2)q_target. Squaring the
orthogonal coefficients in (1) gives (2). In particular BJ's source at
(n,0) has sigma=1/sqrt(2), while every mirror source has

    0<sigma_h<=sqrt(3/2).                                  (4)

The vector e represents the polynomial a(s), of degree n+1. For any
p in Pi_n, a(s)p(s,t) has degree <=2n+1 and so has the same mu integral
as nu integral, which is zero by univariate orthogonality. This proves
normality. Since a_k^2=1 pointwise, ||e||^2=sum_kl w_eta,kl=1.
No assertion that all degree-(n+1) product-U columns remain orthogonal
has been made: the two pure high-mode columns already have inner product
eta. Only the normal vector actually used is claimed.

## Scope

The combined P3 result concerns non-affine-product measures moment-equivalent
to SH_n through degree 2n+1, with an n-dependent weight mode; see the
[capacity result's Scope](p3-03-uniform-capacity-radius.md#scope).

These are exact matched moments/coefficients on an n-dependent family;
matching them does not identify the full ambient projectors or capacities.
The density is between 1-|eta| and 1+|eta| relative to nu_n, but no
capacity equivalence is inferred from that fact alone. The normalized
source/monic conversion is handled in the capacity application.

## Open items

The separate [P3-03](p3-03-uniform-capacity-radius.md) applies the actual
normal vector and all-source comparator. The [completed audit](../audit-01.md)
accepts all three at their stated scopes; final IDs remain unallocated.

## History

- 2026-11-05: Codex P3, assigned gpt-6.1-sol xhigh; rules/input
  ed5515ed84e0e7b12163175dce9f22a859c89c99. Developed after pushed
  round-1 checkpoint 6988024. Gate followed the initial proposal; see
  [canonical protocol disclosure](../LOG.md#canonical-protocol-disclosure--p3-gate-timing).

- 2026-11-06: audit-response Scope wording, metadata and spacing only; accepted
  theorem Statement and proof unchanged.
