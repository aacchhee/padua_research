# Independent supplementary review of the frozen N1 endpoint results

Reviewer: distinct Codex `/root/phase_math_review`, assigned gpt-6-astra
high; serving metadata are not independently exposed. Input head:
`c000899f3fb10d6ba0f1725341a045fe11ec943a`. AGENTS, WORKFLOW and CODEX were
already read at 3dda890; their diff to this input head is empty.

**Disposition: no mathematical finding; the three frozen supporting
statements pass this supplementary review at their written scopes.**
This is a distinct frozen-file review, not the required Claude audit and
not a proof of the full N1 profile, a model maximum, B3, or an effective
argmax onset. No mathematical computation, sample, fit or numerical
quadrature was performed. The executable operation was source identity
validation only.

## Frozen scope and reading

| Supporting result | Reviewed SHA-256 |
|---|---|
| N1-03, endpoint cancellation tail | `dead6c1d4b75aac5ced2ac37154c678bd38f331f03013a978e1ae63b1fe7496c` |
| N1-04, all-integer regularized pole | `f030f230fa8b0c8d5f5d8fda223327fb2d7fda035ebc938b7d25f58d6a683cdd` |
| N1-05, joint logarithmic endpoint profile | `aa05e4469b71e0d97228e4d418955bc32e7bf0946a7534ce2a3ecee1b3ce77f6` |

Read these three proofs in full and checked them against
`evidence/n1-round3-freeze.json`. Reread N1-01's actual row normalization,
coefficient sum and error assembly, and N1-02's integral, variation,
shifted mesh, special-row set and error assembly. Read PD-T270 in full
for its regularized cotangent second-derivative bound and PD-T365 in full
for its exact C(t) series and harmonic tail. These are local accepted
dependencies; no external source theorem is transferred. The elementary
uses of these dependencies are reconstructed below.

The campaign rules, handoff, plan and novelty baseline were read in the
preceding supplementary review. This task generates no new mechanism,
priority claim or novelty disposition, so the workflow's no-novelty review
exception applies. It does not audit the complete novelty history or the
chronology asserted by the freeze record. Frozen candidate/gate/attempt
identities were checked, without treating their claims as proof premises.

The accompanying [review receipt](evidence/n1-endpoint-review.json) records
the inspected byte identities and separates analytic work from the
hash-only execution. All developer files and prior review artifacts remain
unchanged.

## N1-03: cancellation perturbation and the endpoint tail

The reference pair (-s,s), s>=0, cancels only on (0,pi/2-v) and
(pi/2,pi-v) for 0<v<=pi/4. On the former the smaller magnitude is
s cot(x+v), and on the latter it is -s cot x. Direct integration gives
2s log(sin v) from each interval, hence exactly

    I(-s,s,v)=4s log(sin v).

The perturbation proof avoids an invalid integral of the singular
Lipschitz bound over the whole circle. Its two neighborhoods have radius
v/8, total length v/2, and are disjoint because their centers have circular
distance v. In either neighborhood the other pole is at distance between
7v/8 and 9v/8<pi/2. The other cotangent is bounded by 8/(7v), whereas the
own cotangent has magnitude at least 4/v.

For s>=4epsilon the coefficient signs remain the reference signs. The
own-channel magnitude is at least 3s/v and the other at most 10s/(7v),
so the same nonsingular channel determines both cancellations. Integrating
their pointwise difference 16epsilon/(7v) over total length v/2 yields
8epsilon/7. For s<4epsilon, the perturbed/reference coefficient bounds
5epsilon and 4epsilon instead give 144epsilon/(7v) pointwise and
72epsilon/7<11epsilon after integration. This second case includes s=0
and arbitrary perturbed coefficient signs.

On the complement, each cotangent's absolute integral is at most
-2log(sin(v/8))<=2log(4pi/v). The pointwise factor 2epsilon for the sum
of both cotangents therefore contributes 8epsilon log(4pi/v). The stated
stronger bound epsilon[11+8log(4pi/v)] follows. Setting epsilon=P/4 and
s=a cot(v/2)/2 gives the claimed P[3+2log(4pi/v)] envelope because
11/4<=3. The diamond ensures a>=0 and p,q>=0; no division by a or P is
introduced. If P=0, the actual pair is the reference pair and the error
is exactly zero. If a=0, the s<4epsilon argument applies and the reference
integral is zero.

At v=2pi-z, reflection x->-x shows I(C,D,2pi-z)=I(C,D,z).
Simultaneously reversing both coefficient signs preserves I and gives
coefficients within P/4 of (-a cot(z/2)/2,a cot(z/2)/2). Thus the same
reference and error hold at the second endpoint without a hidden phase
or parity restriction.

For the discrete bound, h=pi/m and the exclusion of rows 0,2m-1 are
essential. On the left, v_r>=rh for r>=1. On the right, with
k=2m-r-1>=1, z_r=((k+1)pi-beta)/m>=kh, including beta=pi.
Distinct rows give distinct positive integers. For the positive decreasing
envelope f, h f(kh)<=integral_((k-1)h)^(kh) f. Consequently either endpoint
sum, including any subset of rows, is at most integral_0^delta f/h.
That integral is delta[5+2log(4pi/delta)]. Normalization
1/(pi m)=h/pi² gives exactly T(P,delta), with the factor two for the two
endpoints. When delta<h the relevant rows are absent. The continuous
bound and the signed difference bound 2T follow by integration and the
triangle inequality. No row-count dependence remains in this residual
bound.

## N1-04: all parities, cusp and periodic constant profile

The two-pole regularization
b(x)=|cot x|-1/x-1/(pi-x) is symmetric, has endpoint value -1/pi,
and integrates to -2log pi. For x<pi/2 its second derivative has magnitude
at most 1+16/pi³<2 by PD-T270; reflection gives the other half. At pi/2
the one-sided derivatives are -1,+1: the derivatives of the two pole
subtractions cancel there. Subtracting |x-pi/2| removes precisely this
jump. The resulting C1 function has Lipschitz derivative, so the integral
Taylor estimate remains valid across the former cusp.

The paired relative positions t and 1-t have the same average linear
term as a cell's midpoint and integral average. Their second-order errors
are at most Mh²/8 and Mh²/24, giving Mh²/6. Taking M=2 gives
pi²/(3n²) after normalized summation. If n is even the absolute-value cusp
lies on a cell boundary and contributes no paired quadrature error. If n
is odd its sole central cell contributes exactly

    h(|t-1/2|-1/4)

before the outer 1/n normalization, with absolute value at most
pi/(4n²) afterward. This includes t=1/2, where the original cotangent
sample is exactly zero. There is no omitted parity case.

The two pole sums contribute [H_n(t)+H_n(1-t)]/pi exactly. The defining
series gives the same telescoping harmonic tail as PD-T365. Convexity
puts each paired value between the doubled midpoint and endpoint sum;
the midpoint/trapezoid errors imply the absolute summand bound 1/(3k³).
Summing gives 1/(6n²)+1/(3n³)<=1/(2n²). Combining with the regular part
therefore yields

    (pi²/3+pi/4+1/(2pi))/n² < 5/n².

All these bounds are uniform for 0<t<1. Multiplication by sin(pi t)
gives the sharper sine-weighted error. At either endpoint the unique
singular cotangent term has regularized limit 1, and the C(t) series has
the same limit. Hence the periodic extension has zero error at every
integer offset. It is an extension of the pole-profile function; it does
not authorize substituting it for a Padua polynomial collision row.

For 0<t<=1/2, reindexing the absolutely convergent series gives
C(t)=1/t+2gamma+R(t). The bounds k²-t²>=3k²/4 and sum k^-3<=3/2 give
R<=4t² and R'<=32t/3, with uniform convergence justifying differentiation.
Decomposing Phi_0 as sinc plus its constant sine term plus R times sine
gives sup norm <1+6/pi<3, safely within the stated 4. The corresponding
derivative bounds are <2, <5 and <=11/3, safely within 12. Reflection
and continuous endpoint matching give a global Lipschitz function even
when an offset crosses an integer or half-integer. No derivative matching
at a periodic seam is required for Lipschitz continuity.

## N1-05: exact logarithmic coefficient and joint residual

The half-angle identities reconstruct exactly:

    C(v)=-c_e cos((d+v)/2)/(2sin(v/2)),
    D(v)= c_d cos((e-v)/2)/(2sin(v/2)),
    a=c_e c_d,     0<=c_e,c_d<=1.

They preserve the original coefficient signs through the signed cosine
and the correct absolute values through the periodic sine regularization.
For nonspecial rows both offsets avoid integers. The N1-04 sine-weighted
error then gives 5(|C|+|D|)/n² for the sum of the two normalized pole
products, not a bound with an additional inverse offset distance.

The periodic identity

    Phi_L=Phi_0+(2L/pi)|sin(pi t)|

proves H(L,v)=A(v)L+B(v) exactly. A(v) has no approximation error and is
retained for arbitrary real L. In particular the residual statement is
about B, or equivalently H-A(v)L; it would not hold uniformly in L after
discarding or crudely perturbing A(v).

At v=0 and 2pi, periodicity gives the same constant numerator U0. The
two offset slopes have magnitude 1/(2pi), giving
|N_0(v)-U0|<=12z/pi and |U0|<=8. The elementary denominator estimates

    2sin(z/2)>=2z/pi,
    0<=1/(2sin(z/2))-1/z<=pi z/48

therefore give the stated 6+pi z/6 bound for the pole-profile difference.
For the integral reference, 1/x-cot x<=pi x/6 and
-log(sin z/z)<=z²/5 give

    |2a cot(z/2)log(sin z)-(4a/z)log z|
        <=az[(pi/6)|log z|+4/5]
        <=az(1+|log z|).

Since z<=pi/4<1, z(1+log(1/z))<=1. The constant contributions are thus
at most 6+pi²/24+1/pi<7. Adding N1-03's P-dependent envelope divided by
pi proves equation (2) at both endpoints. This is uniform as a tends to
zero, even when one offset tends to an integer: Lipschitz continuity
already covers that transition. At the edge a=0 the subtracted logarithm
vanishes; the U0/z term remains where appropriate and is not silently
discarded.

The same decreasing-envelope mesh argument now has normalization
1/m=h/pi. Its integral is exactly

    Q(P,delta)=(2delta/pi)[7+(P/pi)(5+2log(4pi/delta))].

It is independent of both degree and L. The two closest endpoint rows
remain excluded, and the central v=pi chart is not in these endpoint
arcs. The continuous residual tail has the same normalization and bound;
2Q bounds the signed difference. No exchange of divergent singular
integrals has occurred: only the integrable residual is being integrated
or removed. The unsummed singular term [U0+(4a/pi)log z]/z still requires
its separate treatment with the exceptional rows.

Finally, N1-02's exact row identity gives a normalized nonspecial-row
error bounded by

    5(|C_r|+|D_r|)/n² + 4 max(|C_r|,|D_r|)/(n|sin v_r|).

The second contribution sums to E_(n,R) after division by m. The first
uses N1-01's coefficient sum <=2m+4am H_n/pi and yields exactly
D_n=10/n²+20a H_n/(pi n²). Special rows use the original Rhat_r with
total error <=r_n; the two endpoint rows are exact. Thus the final bound
r_n+E_(n,R)+D_n has the correct nm/m normalizations and no duplicate
collision replacement. The conclusion also covers an empty nonspecial
set, possible at small n or large R. Separate phase evenness is used to
define the remaining quadrants consistently with N1-01/02.

## Limits and completion

No correction is requested for the three frozen statements. Their
constants, boundary cases and stated uniformities withstand this analytic
reconstruction. The finite degree-dependent sum in J_(n,R) is still
present. Singular endpoint summation with exceptional rows, the central
chart, interior outer quadrature, a complete compact model and its useful
maximum comparison remain unresolved exactly as the author states.
No B3 PASS, B4 projection, finite-degree acceptance or PD-T099 status
change follows from this review.

This bounded review is complete and frozen at the listed hashes. It
authorizes no next round and makes no finding about later altered files.
