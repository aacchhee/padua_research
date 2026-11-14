# E07 scalar monotonicity and H maximum: independent audit

2026-11-07. **ACCEPT**, with no unresolved finding in the frozen scope
below. Distinct reviewer requested Codex Astra high; actual serving
model/effort metadata is unexposed. The supplied exact integral and
sign proof were amenable to this focused mathematical audit; no model
or effort change was made. This is part of ONE coordinated E07 round,
not the separate required Claude audit.

## Frozen candidate and exact accepted scope

| File | Bytes | SHA256 |
|---|---:|---|
| theory/E07-f-monotonicity.md |10945|e20d211d4e4c7c7895d132b7405f552afebad3e8d926145ded3fcc9aafb230cf|
| ideas/E07-f-monotonicity.md |4507|754bae97245bbd074f85cae713301b9903ff3687b839e99ecf9a3c7f9b5fccf1|
| attempts/E07-f-monotonicity.md |2851|9eb63acd588037495958d8bcc1b180676c8e5d9d45fc3c1b0049d2ae858a004d|

For the exact scalar f(x)=Phi_0(1/2+x/(2pi)), with the original
continuous even2pi-periodic extension, the accepted result is

    f'''(x)<−(311/71680)sin(x/2)<0, 0<x<pi,
    H(x)−H(0)<=−(pi−3)x^2/(4pi^3), |x|<=pi.

H is precisely C08's finite-part pole functional with
lambda0=(2/pi)log(4/pi), not the different row profile called H.
Its unique maximizer on the closed principal period is0; its real-line
maximizers are exactly2pi times the integers. Both endpoints±pi are
included in the H inequality. Ordinary derivatives of f at the smooth
interior are distinguished from its periodic distributional derivative.

The stronger claim H(x)<=cos(x/2)H(0) remains OPEN. No finite-n
remainder, complete D13 theorem, new global Padua onset or disappearance
of the separate fractional/finite-cusp terms is accepted here. Those
are different objects and obligations.

No PD-T271 numerical enclosure is a premise of these two scalar
inequalities or of their maximum conclusion. They use the accepted
elementary scalar identities/bounds listed below. Numerical bounds on
H(0) or subsequent completed-constant applications retain their own
dependencies and require separate scope matching.

## Authority, reading and gate coverage

Root assigned a paper-only audit and owns publication/adoption, shared
records and all mutable Git. Only this report was written. No script,
mathematical source execution/import, scalar, endpoint, threshold,
native, phase, board, quadrature, compile, pack or numerical job was
performed. No author file was edited and no other artifact was created.

Read the current LOG through E07's prospective bounded helper allocation
and preceding accepted E04/E05 scopes. The initial read-only branch head
was3cdaaaf157c7de9c2c9954fc71cf3f5a62b3fdec. The unchanged rules fully
read in this continuing session remain those recorded by the E01/E02/E04
reviews. Current full registry/current/INDEX identities were checked:

    IDEAS d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef
    CURRENT 2e55a2875340ec46f88167b9c21e5834ad085b7c09e73b0aac441e6c66edf4b4
    INDEX 1f6f2acea05a6c65e11ba54646a6db46dbd5b947bb058f233d11bc542401ae61

The previously COMPLETE registry headings/aliases/summaries and every
obstruction/disposition table are reused at these identical bytes.
Fresh mechanism searches covered Abel sums, cosine integrals, third
derivatives, H maximum/shape, scalar pole functionals, convolution and
periodic derivative atoms. The complete E06-H-frontier and its idea,
new E07 idea/attempt/theory, C08 pole-functional proof and integral/
comparison ideas, and N1 regularized-pole proof were read. D10's exact
reciprocal series/local-H argument and C04's full-period distributional
derivative proof were refreshed in their relevant complete sections.
The E06 implication was checked directly, rather than treating its
previously unproved condition as an accepted premise.

The E06 frontier remains unchanged at
64808c06bb6550f16512ca6b54b59537647a7f4b083f107543a4be8eafa6f1f8.
Its earlier OPEN Hmax disposition is historical, now resolved by this
new theorem; its separate stronger cosine-shape question is not silently
resolved. C08 already named that stronger shape as deferred. This is
an explicit continuation of that known scalar frontier, with no claimed
novelty of Abel summation, circular rearrangement or calculus. The failed
inference that a positive reciprocal series keeps a favorable sign
after three product derivatives remains abandoned, not retrospectively
treated as a valid proof or a refutation. Literature coverage stays at
the authenticated repository/source-specific scope; no external primary
theorem or historical priority claim is introduced.

The author's prospective clock and final freeze are disclosed in its
record. The audit observed the announced final identities and read the
small prefreeze endpoint-wording correction. A draft was not accepted
as frozen evidence. No claim of an independently measured serving model
or development duration is made here.

## Exact cosine integral and Abel factor

I independently derived the odd-frequency integral from product-to-sum.
For l=2j+1 and |x|<pi,

    integral_0^(1/2) cos(xt)cos(l*pi*t)dt
        =(-1)^j cos(x/2)l*pi/(l^2*pi^2−x^2).

Subtracting cos(x/2) times the integral of cos(l*pi*t) leaves exactly

    I_l(x)=(-1)^j cos(x/2)x^2/[l*pi*(l^2*pi^2−x^2)].

Thus the nonconstant part of the original reciprocal-pair series is
4*sum_j(-1)^j I_(2j+1). Its terms are absolutely summable for each
fixed |x|<pi. The cos(x/2), pi normalization and factor4 all match
the SAME N1/C08 profile; no different pole scalar is substituted.

With the ODD Abel powers r^(2j+1), the real geometric sum is

    K_r(t)=r(1+r^2)cos(pi*t)/
             [(1−r^2)^2+4r^2*cos^2(pi*t)].

This is nonnegative, tends to1/(2cos(pi*t)) for t<1/2, and is
bounded by5/(8cos(pi*t)) for1/2<=r<1. The bound follows from
(r+1/r)/4<=5/8; the odd power convention is essential to that
particular formula. For fixed r the geometric series is uniformly
convergent, so its integration is justified before taking a limit.

The numerator N_x(t)=cos(xt)−cos(x/2) satisfies
|N_x(t)|<=|x|(1/2−t), while cos(pi*t)>=2(1/2−t).
Their ratio, and hence N_x*K_r, has a uniform integrable bound for
|x|<=pi. Dominated convergence and absolute convergence of the I_l
series therefore give the exact factor2 representation

    f(x)=f0*cos(x/2)+2 integral_0^(1/2)
                         N_x(t)/cos(pi*t)dt.

The representation is first obtained for |x|<pi, then extended by
continuity. At x=pi its integral is2 times the interval length1/2,
giving precisely the original endpoint value1. There is no evaluation
of an uncancelled divergent Fourier series at that endpoint.

## Endpoint differentiation, sine ratio and rational sign

For each q=0,1,2,3, the q-th x derivative of N_x(t) is ZERO at
t=1/2. Its t derivative is uniformly bounded on the compact x,t
rectangle. The mean value theorem therefore supplies the same linear
endpoint factor1/2−t for each differentiated numerator. Dividing by
cos(pi*t) leaves a uniform integrable bound. Repeated ordinary
differentiation is justified on the interior, with finite one-sided
limits at±pi; it does not assert smoothness of the periodic extension.

The entire third derivative is

    (f0/8)sin(x/2)+2 integral_0^(1/2)
        [t^3 sin(tx)−(1/8)sin(x/2)]/cos(pi*t)dt.

For0<t<1/2, the ratio sin(tx)/sin(x/2) increases on0<x<=pi.
Indeed z*cot(z) strictly decreases on0<z<=pi/2, so
t*cot(tx)−(1/2)cot(x/2)>0. Its upper endpoint value is sin(pi*t).
The limiting cases t=0 and1/2 are correct by continuity. Since the
multipliers are nonnegative, this bounds f'''(x)/sin(x/2) ABOVE by
the stated B, with the same cancelled endpoint numerator.

The elementary bound f0<72/125<3/5 follows from C0<4,
log(pi)>11/10 andpi>25/8. It needs no computed corner deformation.
For0<=t<1/2 the numerator t^3 sin(pi*t)−1/8 is negative. Since
0<cos(pi*t)<=1, division makes that negative expression smaller;
the proof's upper-inequality direction is correct.

On[0,1/4], the integrated upper is44/35840−1/16. On[1/4,3/8],
t^3 sin(pi*t)<=27/512 gives the upper−37/2048. The remaining
integral is negative and may be dropped in an upper bound. The exact
rational sum has common denominator71680 and numerator

    5376+88−4480−1295=−311.

The strict f0 bound therefore gives B<−311/71680, proving the
claimed strict third-derivative sign everywhere0<x<pi. The weak
comparison at t=0 in the final frozen text is consistent; the strict
final sign does not depend on a false strict inequality at that endpoint.

## Smooth convolution and the negative periodic atom

From the N1 endpoint expansion, f'(pi−)=(log(pi)−gamma)/pi and
f'(−pi+)=−(log(pi)−gamma)/pi. Hence the actual derivative jump
on the circle is NEGATIVE, with magnitude

    J=2(log(pi)−gamma)/pi>1/pi.

The distributional identity is df'=g(x)dx−J*delta_pi, where
g is the ordinary f'' from the smooth principal interval. The integral
representation gives finite endpoint limits; evenness gives matching
g values at the two representatives. The new sign proof makes g
radially decreasing. The periodic derivative f' has finite variation,
which also follows directly from this piecewise smooth representation
and its one finite jump. The jump is counted once, not twice.

For W(t)=integral_|t|^pi log cot(s/4)ds, the triangular-measure
identity gives the exact convolution formula

    H(x)=lambda0*f(x)+(1/pi)integral_(-pi)^pi W(t)g(x+t)dt
                         −(J/pi)W(pi−|x|).

I checked its normalization: integrating(v−|t|)_+ against
1/[2sin(v/2)] gives W(t), since both vanish at|t|=pi and have
derivative log tan(|t|/4). W is bounded and nonnegative, so Fubini
against total variation is legitimate. Its logarithmic derivative at0
is integrable. The kernel value at the duplicated endpoint is zero;
the displayed negative atom contribution is the complete one.

Subtracting the finite constant g(pi) leaves an even nonnegative
radially decreasing function on the circle. Together with W, its
layer-cake representation reduces the convolution maximum to overlap
lengths of circular arcs. Such a length is at most the smaller arc's
length, attained when the two arcs are concentric. Thus W*g is
maximized at0, including large arcs and endpoint levels. Adding back
the constant has no effect on the maximizing location.

Consequently

    H(x)−H(0)<=lambda0[f(x)−f(0)]−(J/pi)W(pi−|x|).

The accepted full-period distributional bound df'<=(3/pi^2)dx,
with f'(0)=0, gives f(x)−f(0)<=3x^2/(2pi^2). The other term
satisfies W(pi−x)>=x^2/4 for0<=x<=pi, because the derivative of
log cot((pi−s)/4) is1/[2cos(s/2)]>=1/2 and its value at0 is0.
At s=pi the logarithmic endpoint is integrable; no finite derivative
there is presumed. Finally0<lambda0<1/(2pi), J>1/pi give exactly

    H(x)−H(0)<=[3/(4pi^3)−1/(4pi^2)]x^2
                 =−(pi−3)x^2/(4pi^3).

All expressions extend continuously to the closed endpoints. At0 the
original equality is retained; away from0 the right side is negative.
This proves the complete maximum assertion without deleting the atom
or assuming a smooth periodic derivative. The stronger cosine shape
does not follow from this coefficient and is correctly left OPEN.

## Disposition and limits

No BLOCKING, MAJOR, MINOR or nonblocking correction remains. Accept the
exact integral representation, strict smooth-part sign and atom-inclusive
global H inequality at the frozen hashes. Root may adopt these scalar
results independently of any numerical H(0) enclosure. Subsequent
completed-constant or finite-degree consequences must keep their own
normalizations, domains and charges and receive their assigned review.

Actual tools used were read-only git rev-parse, text search/read and
cryptographic/size metadata inspection, plus apply_patch for this report.
No mathematical execution or author/shared/Git mutation occurred. The
separate Claude audit obligation remains explicit.
