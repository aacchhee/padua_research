# PD-T?argmax-bridge-codex-E07-f — Smooth-part monotonicity and the scalar H maximum

Aliases: endpoint-cancelled cosine representation; strict third-derivative
sign; scalar finite-part maximum. Status: **PROVED**, developer paper proof,
distinct mathematical review required before adoption. Split from: the
explicit unresolved smooth-part condition in E06-H-frontier. Split into:
none. E06's frozen text and its historical OPEN dispositions are unchanged.

## Statement

Let f(x)=Phi_0(1/2+x/(2pi)) be the exact even,2pi-periodic scalar profile
of N1 and C08, with its original continuous endpoint values. Let

    H(x)=lambda0 f(x)+(1/pi)integral_0^pi
       [f(x+v)+f(x-v)-2f(x)]/[2sin(v/2)]dv,
    lambda0=(2/pi)log(4/pi).                         (1)

This is C08's finite-part scalar, not the row profile named H elsewhere.
Its smooth part satisfies the explicit strict inequality

    f'''(x)<-(311/71680)sin(x/2)<0,  0<x<pi.        (2)

Consequently, on the entire closed principal period,

    H(x)-H(0)<=-(pi-3)x^2/(4pi^3),  |x|<=pi.      (3)

In particular H has its unique maximum on that period at0; on the real
line the maximizers are exactly2pi times the integers. Endpoints +-pi
are included in (3). Neither (2) nor its proof asserts smoothness of the
periodic f through pi. The negative derivative atom is retained below.

The stronger shape H(x)<=cos(x/2)H(0) remains **OPEN** in this record.
No finite-n estimate, global argmax onset or complete finite-error theorem
is asserted here. In particular the D10 fractional central correction and
E03 finite logarithmic cusp are unaffected by the scalar result.

## Dependencies and proof scope

The exact global reciprocal-pair series is C08-far-pole-functional (6),
also used in D10-relative-constant. N1 supplies the periodic definition and
endpoint expansion. C04 supplies the full-period distributional bound
d f'<=(3/pi^2)dx, including its negative atoms, as used by C08. Accepted
elementary constants are C0=2gamma+4log2<4, log pi>11/10, gamma<3/5,
pi>25/8 and pi<22/7; C08 also proves
0<lambda0<1/(2pi). No new special-function enclosure or computational
premise is needed for this theorem. In particular PD-T271's numerical
corner enclosure is not a dependency of (2) or (3).

E06 proved a sufficient convolution implication with an unproved scalar
sign hypothesis. The relevant kernel argument is reconstructed in
Section4, so that no unproved E06 condition is used as an assumption.
The parent's proposed integral route is independently derived below;
it was a candidate, not an inherited theorem.

## 1. Derive the endpoint-cancelled integral exactly

Write k0=C0-2log pi and f0=f(0)=k0/pi. C08's global series is

    f(x)=cos(x/2)/pi *
       [k0+4x^2 sum_(l odd>=1)1/[l(l^2*pi^2-x^2)]],
                                      |x|<pi.      (4)

For l=2j+1, elementary product-to-sum integration gives

    I_l(x):=integral_0^(1/2)
           [cos(xt)-cos(x/2)]cos(l*pi*t)dt
       =(-1)^j cos(x/2)x^2/[l*pi*(l^2*pi^2-x^2)].  (5)

Indeed the integral of the first product is
(-1)^j cos(x/2)l*pi/(l^2*pi^2-x^2), whereas the second term integrates
to(-1)^j cos(x/2)/(l*pi). Their difference is exactly (5).
Thus the part of (4) beyond f0 cos(x/2) equals4 sum_j(-1)^j I_(2j+1)(x),
an absolutely convergent series for each |x|<pi.

To exchange that sum with integration legitimately, introduce0<r<1:

    K_r(t)=sum_(j>=0)(-1)^j r^(2j+1)cos((2j+1)pi t)
          =r(1+r^2)cos(pi t)/
             [(1-r^2)^2+4r^2 cos^2(pi t)].          (6)

The first equality converges uniformly for fixed r. The second follows
by taking the real part of r exp(i*pi*t)/(1+r^2 exp(2i*pi*t)).
For0<=t<1/2,

    lim_(r->1-)K_r(t)=1/[2cos(pi t)],
    0<=K_r(t)<=5/[8cos(pi t)],  1/2<=r<1.          (7)

For the upper bound, drop the nonnegative(1-r^2)^2 from the denominator
and use(r+1/r)/4<=5/8 on[1/2,1]. The apparent singularity is cancelled:

    |cos(xt)-cos(x/2)|<=|x|(1/2-t),
    cos(pi t)=sin(pi(1/2-t))>=2(1/2-t).            (8)

Hence the integrands after multiplication by K_r are uniformly bounded
for |x|<=pi. Dominated convergence applies, while the absolutely
convergent series of I_l also permits r->1. Combining (4)–(8) gives

    f(x)=f0 cos(x/2)+2 integral_0^(1/2)
                  [cos(xt)-cos(x/2)]/cos(pi t)dt,
                                      |x|<=pi.     (9)

The endpoint values follow by continuity: at x=pi the integral is
2 integral_0^(1/2)1 dt=1, the actual continuous f(pi). Evenness gives
the opposite endpoint. No ordinary Fourier series was evaluated at its
singular endpoint without the cancellation in (8).

## 2. Differentiate while preserving endpoint cancellation

For each integer0<=q<=3, the q-th x derivative of
cos(xt)-cos(x/2) vanishes identically at t=1/2. Its t derivative is
uniformly bounded for |x|<=pi and0<=t<=1/2. The mean value theorem
therefore bounds that differentiated numerator by a constant times
1/2-t. Dividing by cos(pi t) and using (8) gives an integrable uniform
bound. Repeated differentiation under the integral is justified.

On0<x<pi, the complete third derivative is consequently

    f'''(x)=(f0/8)sin(x/2)
         +2 integral_0^(1/2)
              [t^3 sin(tx)-(1/8)sin(x/2)]/cos(pi t)dt. (10)

The same integral has one-sided limits as x approaches pi. This is
ordinary differentiation of the endpoint-cancelled formula on the
principal interval; it does not identify derivatives across the periodic
cusp. No term from the differentiated integrand is discarded here.

For0<t<1/2, consider R_t(x)=sin(tx)/sin(x/2),0<x<=pi. It increases
with x. To see this, z cot z decreases strictly on0<z<=pi/2 because

    (z cot z)'=[sin z cos z-z]/sin^2 z<0.

The last inequality follows from sin(2z)<2z forz>0. Therefore

    (log R_t)'=t cot(tx)-(1/2)cot(x/2)>0,
    R_t(x)<=R_t(pi)=sin(pi t).                     (11)

The endpoint t=0 follows by continuity and t=1/2 gives equality.
Since all t^3 and reciprocal cosines in (10) are nonnegative, divide
by sin(x/2)>0 and apply (11) to obtain

    f'''(x)/sin(x/2)<=B,
    B=f0/8+2 integral_0^(1/2)
                     [t^3 sin(pi t)-1/8]/cos(pi t)dt. (12)

The numerator still vanishes at t=1/2; this is a finite integral.

## 3. An exact rational negative bound

First,

    f0=(C0-2log pi)/pi<(9/5)/(25/8)=72/125<3/5.  (13)

For every0<=t<1/2, t^3 sin(pi t)-1/8<0. As0<cos(pi t)<=1,
division by cos(pi t) makes this negative quantity smaller, so

    [t^3 sin(pi t)-1/8]/cos(pi t)
                       <=t^3 sin(pi t)-1/8.         (14)

This sign is essential. On[0,1/4], sin(pi t)<=pi t<=(22/7)t gives

    2 integral_0^(1/4)
        [t^3 sin(pi t)-1/8]/cos(pi t)dt
       <=2 integral_0^(1/4)[(22/7)t^4-1/8]dt
        =44/(35*1024)-1/16.                        (15)

On[1/4,3/8], use t^3 sin(pi t)<=27/512 in (14), giving

    2 integral_(1/4)^(3/8)
        [t^3 sin(pi t)-1/8]/cos(pi t)dt
        <=-37/2048.                                (16)

The integral over[3/8,1/2] is negative; dropping it gives a valid upper
bound. Combining (12)–(16) proves the purely rational estimate

    B<3/40+44/35840-1/16-37/2048
      =-311/71680<0.                               (17)

All constants are literal rationals. Equation (2) now follows from
(12) and (17), and the ordinary g=f'' is strictly decreasing on(0,pi).
The mixed signs that defeated the naive differentiated-series inference
are handled by the complete integral, not by claiming their positivity.

## 4. Close the periodic H maximum implication

For completeness the relevant E06 implication is reproduced with its
atom, normalization and signs. The N1 endpoint expansion gives

    d f'=g(x)dx-J delta_pi,
    J=2(log pi-gamma)/pi>1/pi,                       (18)

where g is the ordinary f'' on(-pi,pi), continued periodically, and
the negative atom is counted once on the circle. The bound on J uses
log pi>11/10 and gamma<3/5. The integral representation above ensures
that g has finite one-sided endpoint limits. It is even by symmetry and,
by (2), radially decreasing on[0,pi]. The periodic f is continuous;
its derivative is of bounded variation, as is also supplied by C04/N1.

Define the even periodic kernel

    W(t)=integral_(|t|)^pi log cot(s/4)ds,
                                       |t|<=pi.    (19)

It is nonnegative, bounded, radially decreasing, and W(pi)=0.
The triangular-measure identity for second differences gives

    H(x)=lambda0 f(x)+(1/pi)integral_(-pi)^pi
                             W(t)g(x+t)dt
                         -(J/pi)W(pi-|x|), |x|<=pi. (20)

Indeed the second-difference kernel is(v-|t|)_+, and integrating it
against1/[2sin(v/2)] gives exactly W(t). Bounded W permits Fubini
against the total variation of d f'. The point mass in (18) contributes
the displayed negative term; endpoint representatives with W(pi)=0
produce no double counting.

The convolution W*g has its maximum at0. Subtract the finite constant
g(pi) to make g nonnegative; both remaining functions are even and
radially decreasing on the circle. Their layer-cake representations
reduce the assertion to intersections of translates of centered circular arcs.
Any intersection has length at most the smaller arc; concentric arcs
attain that length. Integrating gives the claimed maximum. Adding the
constant back does not affect the assertion.

Consequently (20) implies

    H(x)-H(0)<=lambda0[f(x)-f(0)]-(J/pi)W(pi-|x|). (21)

C04's full-period distributional semiconcavity bound and f'(0)=0 give
f(x)-f(0)<=3x^2/(2pi^2) on|x|<=pi. Also, for0<=x<=pi,

    W(pi-x)=integral_0^x log cot((pi-s)/4)ds>=x^2/4,

because the integrand vanishes at0 and its derivative is
1/[2cos(s/2)]>=1/2. Finally0<lambda0<1/(2pi) and J>1/pi give

    H(x)-H(0)<=[3/(4pi^3)-1/(4pi^2)]x^2,

which is (3). At x=0 equality holds; for every other principal phase
the right side is negative since pi>3. Periodicity gives the stated
complete set of maximizers. This proof retains the negative atom
throughout and applies to the closed endpoints by continuity.

## Scope, verification and history

This closes the particular smooth-part sign condition isolated in E06,
and therefore proves Hmax; it does not prove the stronger cosine shape.
The E06-H-consequences paper records separate algebraic consequences
of Hmax. Their use in a new finite theorem requires exact domain/charge
matching and independent review; none is asserted by this scalar file.

Requested Astra ultra, serving metadata unexposed. Root supplied the
unadopted integral test; the developer independently checked (4)–(21).
Start2026-11-07 00:58:24 UTC, cutoff01:13:24 UTC. Root's prospective
E07 LOG justification and the refreshed gate preceded derivation; details
and candidate dispositions are in the owned idea/attempt. Only these
three new E07 prose files were changed. No source, script/import,
mathematical/scalar/numerical/endpoint/native/pack job, Git operation,
shared-record mutation or subagent was used. Distinct audit is separate.


## Root adoption —2026-11-07

Root adopts the exact10945B frozen proof above, SHA256 e20d211d4e4c7c7895d132b7405f552afebad3e8d926145ded3fcc9aafb230cf, after distinct [E07 H ACCEPT](../independent-checks-E07-H.md), report11902B461214a5a9fb01c446add34a3bbf3cc41ed2594c333d577f33e2079535bb40b3. The full derivative sign and closed-period H maximum/drop are PROVED; original prefix is preserved. No PD-T271 numerical enclosure is needed for these scalar conclusions. The separate consequences and finite-n assembly require their own accepted proofs; stronger cosine shape remains OPEN. Final Claude audit remains separate.
