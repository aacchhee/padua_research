# PD-T?argmax-bridge-codex-H-sharp — The sharp Padua corner expansion

ID kind: PD-T; provisional, no final allocation.
Aliases: H sharp target; original A3 completion; negative reciprocal
correction; half-integer centered corner asymptotics.
Split from: original PD-T098, the complete displayed asymptotic statement.
Split into: H01 harmonic aggregate, H04 smooth residual and H05 uniform
centering are supporting results, not parameter cases of this target.

## Statement

Use exactly PD-T101's corrected Padua convention. For integer n>=2 put

    N=n+1/2, a=2/pi, d=gamma+log(8/pi),
    c1=a*d, b=2*a*c1, c=c1^2+kappa,
    A(z)=a*(log z+d),

where kappa is the exact integral/series constant of PD-T269, and
Lambda_c(n)=lambda_n(-1,-1) is the true nonnode corner value. Then

    Lambda_c(n)=4/pi^2 log^2N+b logN+c-1/N+R_n,
    R_n=O(log N/N^2).                                      (1)

More precisely there exists a degree-independent finite constant C>0
such that |R_n|<=C log(N)/N^2 for every integer n>=2. Both parity
subsequences obey the same formula and constants. In particular,

    N*[Lambda_c(n)-A(N)^2-kappa] -> -1.                     (2)

The bigO theorem is the original target; no numerical value for the
remainder constant C or a sharp explicit onset is claimed.

## Definitions and assumptions

Natural logarithms and exact real analysis. The nodes are
(cos(j*pi/n),cos(k*pi/(n+1))) with j+k even, original endpoint weights
and exceptional first-coordinate coefficient ONE. No fitted coefficient,
argmax premise, finite-degree experiment or numerical constant enclosure
is assumed. The constant kappa is its proved analytic definition, not
the historical fitted decimal. PD-T271 supplies its optional separately
certified numerical enclosure.

## Status

**PROVED**, analytic, with distinct supplementary main/support review
and focused integration acceptance. Root adopts exactly statement (1),
its uniform remainder and both-parity scope. The original global registry
has not been edited; the substantive Claude audit and readiness remain
separate. No numerical premise is needed for the corner theorem.

## Dependencies and verification

- [PD-T159](../../padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md):
  positive corner sum and exact endpoint normalization.
- [F03](F03-origin-sign.md), routine exact partial-row/two-pole identities
  only; its formerly unresolved sign/one-index-evaluator targets are not
  assumptions.
- [H05](H05-digamma-centering.md): uniform centering of every harmonic row,
  with normalized aggregate error O(log m/m^2), including both endpoints.
- [H01](H01-exact-sum.md): complete weighted harmonic asymptotic and exact
  first-correction cancellation; [H06](H06-aggregate.md) independently
  reconstructs its derivation, not a second novelty claim.
- [H04](H04-smooth-quadrature.md): the exact remaining smooth contribution,
  including its nonzero first correction and error at most17/n^2.
- [PD-T269](../../padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md)
  and [PD-T270](../../padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md):
  identify the limiting constant as kappa.

Distinct [support review](../independent-checks-H-support.md) and
[full-proof review](../independent-checks-H-main.md) give their actual
coverage and findings. They supplement, rather than replace, the required
substantive Claude audit. No scientific computation was executed in H.

## Proof

Write m=n+1, w(x)=cot(pi*x/2), and

    B(x)=cot(pi*x)-1/(pi*x)+1/[pi*(1-x)],
    V_n=sum_(r=1)^n w(r/m)
                    sum_(l=0)^(r-1)B((l+(1-r/m)/2)/n).

The original exact partial-cotangent reduction, with every physical
endpoint and row retained, is

    Lambda_c=-1+2/m+Hcal_m+4V_n/(nm).                       (3)

No replacement by a complete signed row occurs. H05 reanchors the exact
harmonic row at integers and half-integers with a uniform O(m^-2)
remainder. Its actual positive weight sum is O(m log m), so after the
factor1/m in (3) the remainder is O(log m/m^2), not a fixed-index
formal expansion.

Let

    I1=integral_0^1 [w(x)/(1-x)-a/x] dx,
    I2=integral_0^1 x*w(x) dx,
    I_B=integral_0^1 x*w(x)*B(x) dx,
    c0=gamma+2log2.

H01, with its explicit endpoint-cell estimates, proves

    Hcal_m=A(m)^2+C_H+[-a^2 log m+beta_H]/m
                                      +O(log m/m^2),
    beta_H=-2-a^2*c0-a*(I1+I2).                            (4)

The logarithmic term in (4) is essential. The proof keeps the summable
small-index derivative correction and uses

    sum_(r>=1)[psi'(r+1/2)-1/r]=1+2log2-pi^2/4.

After removing the explicit singular terms, the remaining quadrature
function has |R''(x)|<=C'[1/x+1/(1-x)]. Estimating the two endpoint
cells directly and integrating the interior error yields the actual
O(log m/m^2) bound; bounded endpoint derivatives are not assumed.

H04 proves, with constants independent of n,

    4V_n/(nm)=C_B+beta_B/n+O(n^-2),
    beta_B=-a^2+2I_B+a I2.                                 (5)

Only this constant beta_B permits replacing1/n by1/m at O(m^-2) cost.
The exact combined integral identity in H01/H06 is

    2I_B-a I1=a^2-1+a^2 log(pi/2).                         (6)

It follows by combining the integrands BEFORE integration and using
w'=-(1+w^2)/a; the endpoint terms are retained. Equations (4)--(6) give

    2+beta_H+beta_B=-1-a^2*d.

Thus the normalization2/m in (3) and the logarithmic term in (4) yield

    Lambda_c=A(m)^2+C-[a^2 log m+1+a^2*d]/m
                                      +O(log m/m^2).        (7)

By PD-T269, Lambda_c-L_n^2 tends to kappa. PD-T270 gives
L_n^2-A(n)^2=O(log n/n^2), while A(m)^2-A(n)^2 tends to zero.
Consequently C=kappa in (7). This identifies the constant without
assuming (1) or recomputing its numerical value.

Finally N=m-1/2 and elementary log estimates give

    A(N)^2=A(m)^2-[a^2 log m+a^2*d]/m+O(log m/m^2),
    1/N=1/m+O(m^-2).

Insert these in (7) to obtain (1). Every estimate holds on the full
integer sequence m>=3, with a degree-independent constant; enlarging
that constant over any finite initial cases gives the stated all-n bound.
Multiplying the remainder in (1) by N proves (2).

## Relation to the global constant and limitations

The corner theorem is analytic and independent of argmax. The separately
proved [G01](G01-all-degrees.md) identifies Lambda(n)=Lambda_c(n) for
every n>=2, so the same expansion holds for the global Lebesgue constant,
with G01's explicit computer-assisted dependencies. An eventual argmax
already suffices for the asymptotic transfer; the finite bridge additionally
provides the exact maximizer statement at every degree.

This does not prove a next log(N)/N^2 coefficient, a smaller analytic
argmax onset, an exact O(n) corner evaluator, or a historical priority
claim. The optional H02 endpoint and H03 reciprocity identities are not
premises of this proof. Original PD-T098's statement/history is preserved;
global registration and final IDs await reviewed preparation.

## History

2026-11-07, AC authorizes up to20Hrounds. Six allocated PAPERONLY rounds
produce the complete candidate through H01/H04/H05, with independent
H06 reconstruction. Root owns this integration; requested Astrahigh
coordinator, Solxhigh development and specifically justified Solultra
H02/H06; actual serving metadata is unexposed. Final written independent
acceptance and root adoption are recorded in the dated disposition below.

## Dated root adoption —2026-11-07

The complete main audit independently accepts frozen H01/H04/H05, and
its focused addendum accepts this parent integration at candidate hash
e3d402944ab4bfab0d743db7328282fe039c143618c3ac0d59e9a68dff73101e.
The present status/disposition update was explicitly permitted by that
review; mathematical statements, proof and dependency scopes are unchanged.
Root adopts (1) as PROVED and (2) as its routine consequence. The
all-degree global transfer retains G01's computer-assisted assumptions.
Six rounds used, fourteen unallocated; campaign stops early on success.
Final Claude audit still covers H plus the deferred F/compact/G01 batch.
