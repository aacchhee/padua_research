# PD-T?proof-attempts-2-codex-40 — Exact tensor representation and principal embedding for degree six

Final ID: **PD-T172**. Provisional ID `PD-T?proof-attempts-2-codex-40` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

Dated status supersession, 2026-11-01 (response to audit-01 F8): Count41 and global42 are PROVED for n=6. Claude audit-01 accepted these cases and this supporting result. Later OPEN/checks-needed lines retain the earlier development checkpoint and are superseded by this note; no mathematical status or proof changes.

ID kind: PD-T.
Aliases: A5 n6 field; sqrt3/cos(pi/7) tensor basis; native ANP conversion without numerical embedding selection.
Split from: arithmetic/real-embedding obligation in the n6 case of programme A5.
Split into: actual n6 counts and global values remain separate OPEN targets.

## Statement

Put a=sqrt3>0 and let b be the largest real root of p(t)=t³−t²−2t+1. Then b=2cos(pi/7), [Q(a,b):Q]=6, and

B=(1,b,b²,a,ab,ab²)

is a rational basis of that field. For θ=a+b, the minimal polynomial is

f(t)=t⁶−2t⁵−12t⁴+18t³+23t²−16t+1.

The conversion from ascending θ-power coefficients to B-coordinates is the rational matrix T displayed below. Therefore any exact native power-basis representation modulo f can be converted to B and evaluated in the chosen real embedding using rational outward intervals for a and b, without trusting an approximate symbolic root selector.

The principal b is the unique root of U6(t/2) in(9/5,181/100), and U6(t/2) has no larger real root. Any rational sub-bracket of this interval with p(lower)<0<p(upper) encloses that same principal b. A positive rational bracket whose squares straddle3 similarly encloses a. Inclusion-preserving rational interval arithmetic on the tensor representation encloses every field coefficient in this embedding.

## Definitions

U6 is the usual degree-six Chebyshev polynomial of the second kind; its roots in the t variable are 2cos(k*pi/7), k=1,…,6. Native power coefficients are ordered constant through θ⁵. Tensor coordinates use B in the stated order. An exact native implementation must verify its defining polynomial, the identities a²=3 and p(b)=0, θ=a+b, and the conversion identities; an arbitrary unverified isomorphic polynomial encoding is not enough to identify a real embedding.

## Assumptions

Characteristic zero, exact rational/field arithmetic, and outward arithmetic for every interval operation. The final computer certificate must independently verify its finite coordinate/conversion/bracket data; this analytic theorem does not assert that a particular code run passed a checker.

## Status by part

Overall status: **PROVED** (written algebraic/analytic representation theorem; required Claude audit pending).

| Part | Status | Evidence |
|---|---|---|
| field degree, tensor basis and primitive polynomial | PROVED | degree and rational reconstruction argument below |
| explicit native-to-tensor conversion | PROVED | binomial expansion reduced by a²=3 and p(b)=0 |
| principal real embedding and outward coefficient interpretation | PROVED | rational monotonicity bounds and Chebyshev roots below |

Actual n6 node/certificate computations remain separately unverified until an independent checker and actual different-agent execution are recorded.

## Depends on

Elementary field degrees, rational-root test, polynomial identities, Chebyshev recurrence/root identity, and elementary monotonicity/interval arithmetic. No part1 mathematical result is needed for this field theorem. The later corrected-kernel cardinal construction cites `PD-T?proof-attempts-codex-01 (audit pending)` separately, with the task's dated audit qualification.

## Checks

New implementation: `../code/a5_n6_field.py`. It constructs native exact field elements, verifies conversion identities and uses112-bit outward fixed dyadics. It also checks the principal bracket with exact Sturm counts as a redundant finite check; the written argument below does not depend on an unexecuted or numerical Sturm calculation. Actual code executions, hashes and independent reruns belong to the n6 evidence record. No n6 maxima count is asserted here.

## Sources

Registered A5 / programme IDEA17 and source06 at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e; gate in T-A5-n6.md. This is exact implementation support for a registered proof target; no novelty/priority claim.

## Proof or evidence

The monic cubic p has no rational root: its only possible integer roots are±1, and p(1)=−1,p(−1)=1. Hence p is irreducible overQ and [Q(b):Q]=3. The quadratic a²−3 is irreducible overQ. Moreover a cannot lie in Q(b), because then its degree2 would divide3. Thus adjoining a to Q(b) has degree2, the compositum degree is6, and the displayed tensor monomials form a basis.

Let θ=a+b. Substituting b=θ−a into p(b)=0 and reducing a²=3 gives

θ³−θ²+7θ−2=a(3θ²−2θ+1).

The denominator D=3θ²−2θ+1 is positive for real θ (its discriminant is−8). Hence a=(θ³−θ²+7θ−2)/D and b=θ−a belong to Q(θ). Therefore θ generates the degree-six field. Squaring this identity and subtracting3D² gives exactly f(θ)=0. Since f is monic of degree6, it is the minimal polynomial.

Expanding θ^r=(a+b)^r for r=0,…,5 and reducing a²=3,b³=b²+2b−1 gives the matrix T whose columns are those tensor-coordinate vectors:

```text
1 0 3 -1  8 -33
0 1 0 11  1 110
0 0 1  1 21  34
0 1 0  3 -4   4
0 0 2  0 20   5
0 0 0  3  4  45
```

Both coordinate lists are bases, so this matrix is invertible. These explicit polynomial identities also let a checker reconstruct the conversion independently, rather than import a developer matrix inverse or symbolic trigonometric simplifier.

For the embedding, direct polynomial multiplication gives

U6(t/2)=(t³−t²−2t+1)(t³+t²−2t−1)=p(t)q(t).

At9/5, p=−1/125 and p'=103/25>0; p' is increasing thereafter because p''=6t−2>0. At181/100, p=33641/10^6>0. Thus p has exactly one root in that bracket and no root above its upper endpoint. Also q(9/5)=559/125>0,q'(9/5)=283/25>0, and q' is increasing thereafter. Consequently q has no root at or above9/5. The bracketed p root is therefore the largest real root of U6(t/2), namely2cos(pi/7). The positive square root a is likewise the largest root of t²−3.

Every conjugate of the tensor field maps a to±sqrt3 and b to one of the three real p roots, so all embeddings are real. Specifying these two largest roots determines the desired embedding; equivalently θ is the largest of the six conjugate sums. Exact interval evaluation of the tensor polynomial at enclosing a,b intervals then gives an inclusion-preserving enclosure, by induction over additions and multiplications. Fixed-dyadic floor/ceiling rounding preserves these inclusions. No approximation returned by a symbolic field constructor participates in this identification. ∎

## Scope

Exactly the degree-six coefficient field needed for n6 Padua nodes, with a precise principal embedding. The native-to-tensor method may generalize, but no n7/n8 field or count is asserted here.

## Open items

Independent checker of the implementation's exact field/conversion/bracket data and actual different-agent execution; complete n6 spatial/edge/node certificate; required Claude audit.

## History

2026-11-01, Codex `/root/a5_n4` now assignedn6, inherited gpt-6.1-sol xhigh; rules38db12bc1cee57902c67f62e022af83e0880f699. Written separately from count claims so a successful field representation does not relabel an incomplete n6 count PARTIAL.
