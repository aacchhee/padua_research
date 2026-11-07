# PD-T?argmax-bridge-E06-H — Exact scalar kernel and a conditional maximum criterion

Status: **PROVED partial identities and conditional implication** below.
The unconditional assertions H(x)<=H(0) and
H(x)<=cos(x/2)H(0) on |x|<=pi remain **OPEN**. In particular this
record does not assert a new global constant, onset, or finite-degree result.
The stronger shape question was already explicitly deferred in C08; no
novelty or priority claim is made for this quantitative continuation.

Requested Astra ultra, serving metadata unexposed. Bounded PAPER block
2026-11-07 00:43:05–00:58:05 UTC; rules last read at91b3acea. Root owns
shared records and Git. Only the three same-stem E06 prose files are owned.
No source, script, import, scalar execution, numerical quadrature, endpoint,
native, degree, compile, threshold, pack or Git action was run here.

## 1. Exact object and dependencies

Use C08-far-pole-functional's scalar, not the row profile with the same
letter. Set

    f(x)=Phi_0(1/2+x/(2pi)),
    lambda0=(2/pi)log(4/pi),
    H(x)=lambda0 f(x)+(1/pi)integral_0^pi
           [f(x+v)+f(x-v)-2f(x)]/[2sin(v/2)]dv.       (1)

Here f is even and 2pi-periodic. N1-regularized-pole gives, for0<t<1,

    Phi_0(t)=sin(pi t)[C(t)-2log pi]/pi,
    C(t)=2gamma+1/t+1/(1-t)
          +sum_(k>=1)[1/(k+t)+1/(k+1-t)-2/k].        (2)

The regular series and its needed derivatives converge locally uniformly.
C04's full-period distributional bound, already used by C08, is

    d f' <= (3/pi^2)dx.                              (3)

It includes the negative derivative atom at each periodic integer offset;
it is not an assertion that f is globally twice continuously differentiable.
C08 gives f(0)<=f(x)<=1, f(0)>1/2, and
0<lambda0<1/(2pi). The exact endpoint expansion in N1 is

    Phi_0(t)=sin(pi t)/(pi t)
          +(2gamma-2log pi)sin(pi t)/pi+O(t^3).

Consequently, writing g for ordinary f'' on (-pi,pi), periodically
continued, its endpoint limits are finite and

    d f'=g(x)dx-J delta_pi,
    J=2(log pi-gamma)/pi>0.                          (4)

The atom is counted once on the circle. In particular f' has bounded
variation: (3), periodicity and zero total derivative mass give finite
positive and negative masses. The endpoint expansion also directly gives
bounded g. These facts justify the measure manipulations below.

Other dependencies, used only in Section5, are D02's exact completed
constant and uniform true-constant limit, D10's cutoff-free decomposition,
and the EXISTING accepted PD-T269/PD-T271 corner normalization/enclosure.
The latter is an inherited proved computational enclosure, not a new
execution or a decimal guessed here. The idea and attempt records give
the refreshed gate and its exact limitations.

## 2. An exact positive convolution kernel, including the atom

Define an even 2pi-periodic kernel by

    W(t)=integral_(|t|)^pi log cot(s/4) ds,
                       -pi<=t<=pi.                 (5)

It is continuous, bounded, nonnegative, and decreasing on [0,pi],
with W(pi)=0. Its weak derivative is integrable: on0<t<pi,
W'(t)=-log cot(t/4), whose only singularity is logarithmic at0.
Then, for every |x|<=pi,

    H(x)=lambda0 f(x)+(1/pi)integral_(-pi)^pi
                            W(t)g(x+t)dt
                        -(J/pi)W(pi-|x|).           (6)

Proof. The second difference of a continuous function with derivative
of bounded variation has the exact measure representation

    f(x+v)+f(x-v)-2f(x)
       =integral_(-v)^v (v-|t|)d f'(x+t).

Integrating the triangular kernel first gives

    integral_(|t|)^pi (v-|t|)/[2sin(v/2)]dv=W(t).

Indeed the left side has derivative log tan(|t|/4) with respect to
|t| and vanishes atpi, exactly as does (5). Fubini applies to total
variation because W is bounded. Insert (4). The distance from x to the
atom on the circle is pi-|x|. At a boundary representative the kernel
vanishes, so there is no double counting. This proves (6), including
x=0 and the cusp positions x=+-pi.

This representation is exact, but positivity of W alone does not identify
the maximum of its convolution with the signed, as yet uncontrolled g.

## 3. Fourier diagnostic and the periodic endpoint

The operator in (1), on a single Fourier mode cos(kx), has eigenvalue

    lambda_k=lambda0-(4/pi)sum_(j=1)^k 1/(2j-1),
                   k>=1; lambda_0=lambda0.         (7)

For completeness, set I_k=integral_0^pi(1-cos(kv))/sin(v/2)dv.
Then I_0=0 and

    I_k-I_(k-1)=2 integral_0^pi sin((2k-1)v/2)dv
               =4/(2k-1).

Substitution in (1) proves (7). Every nonconstant multiplier is negative.
This is a mode identity, not a pointwise maximum theorem: no sign pattern
for all Fourier coefficients of f has been established here, and such a
pattern cannot be inferred merely from f's minimum at0.

At the opposite periodic endpoint the exact value is

    H(pi)=(2/pi)log(2/pi)<0.                         (8)

To verify the normalization without a singular numerical integral, use
C08's equivalent finite part and put epsilon=delta/(2pi). Periodicity
and (2) give

    H(pi)=(1/pi)lim_(epsilon->0+)
      {integral_epsilon^(1-epsilon)[C(t)-2log pi]dt
                                                +2log(2epsilon)}.

The pole terms contribute -2log epsilon+o(1). For the regular series,
termwise integration is justified by uniform O(k^-2) bounds, and

    2gamma+2sum_(k>=1)[log(1+1/k)-1/k]=0,

because the partial sum is 2gamma+2log(K+1)-2H_K, tending to0.
Thus the limit is 2log2-2log pi, proving (8).

There is also a genuine non-smooth endpoint regime:

    H(pi-epsilon)-H(pi)
       =(J/pi)epsilon log(1/epsilon)+O(epsilon),
                         epsilon->0+.              (9)

In (6) the convolution with bounded g is Lipschitz, since W' is L1;
lambda0 f is Lipschitz too. The atom term changes by
(J/pi)[W(0)-W(epsilon)], and
log cot(s/4)=log(4/s)+O(s^2) gives (9). Hence pi is a strict local
minimum. This special regime supports neither a counterexample nor a
proof of either full-domain maximum or cosine shape. It does rule out
discarding the endpoint atom or assuming a smooth periodic derivative.

## 4. A sufficient remaining one-dimensional condition

The following implication is proved, with its hypothesis explicit:

    IF g=f'' on(0,pi) is nonincreasing, THEN
    H(x)-H(0)<=-(pi-3)x^2/(4pi^3), |x|<=pi.         (10)

The hypothesis itself is **NOT PROVED** in this block.

Proof of the implication. Under the hypothesis, g is even and radially
nonincreasing on the circle. Subtract the constant g(pi) to make it
nonnegative. The convolution with W has its maximum at0: layer-cake
representations reduce this to centered circular arcs, whose intersection
has maximal length when their centers agree. Adding back the constant
does not change the location of the maximum. Thus (6), using W(pi)=0,
gives

    H(x)-H(0)<=lambda0[f(x)-f(0)]-(J/pi)W(pi-|x|).

By (3), evenness, and f'(0)=0,
f(x)-f(0)<=3x^2/(2pi^2). Also

    W(pi-x)=integral_0^x log cot((pi-s)/4)ds>=x^2/4,
                              0<=x<=pi,

since the integrand vanishes at0 and its derivative is
1/[2cos(s/2)]>=1/2. The accepted elementary bounds
log pi>11/10 and gamma<3/5 imply J>1/pi. Together with
lambda0<1/(2pi) this gives (10). No extension through the atom was used.

The explicit remaining condition can equivalently be tested as
Phi_0'''(t)>=0 for0<t<1/2, using symmetry about1/2. It is not supplied
by the semiconcavity upper bound (3). A naive proof by expanding
Phi_0 as a sinc term plus a positive reciprocal-power series is unfinished:
after three derivatives, products with sin(pi t) contain terms of both
signs. Positivity of the original series does not settle the derivative.
This failed inference is preserved; there is no claimed counterexample.

Even if (10) were made unconditional, the displayed drop is not sufficient
as written to establish H(x)<=cos(x/2)H(0). The stronger question remains
separate. A still weaker useful scalar target, communicated by the disjoint
constant-consequence helper, is H<=H(0)+1/400; that implication is not a
premise or a proof of any such scalar inequality here.

## 5. The exact origin value and a rational enclosure

Let C0=2gamma+4log2 and k0=C0-2log pi. Write kappa for PD-T269's
corner deformation, with PD-T271's accepted enclosure. Then

    H(0)=kappa/2+(2k0/pi^2)log(2/pi),               (11)
    7/25 < H(0) < 8/25.                            (12)

For normalization, D02's uniform true-constant limit, at the actual origin,
identifies its completed constant with PD-T271's parity-independent
corner constant Cstar. Changing log(n+1/2) to log n changes no constant
term. The exact D10 decomposition at that origin has zero cancellation
excess, hence

    Cstar=C0^2/pi^2+2H(0)
                     -(4/pi^2)(log^2 pi-log^2 2).

PD-T271 gives Cstar=(4/pi^2)(gamma+log(8/pi))^2+kappa.
Subtracting these two identities and expanding proves (11). This uses
the exact origin normalization, not an arbitrary phase coordinate swap.

Only the very coarse inherited inequalities9/10<kappa<23/25 are needed
for (12). For the upper bound, C08 proves k0>161/100, pi>25/8 and
pi^2<10. The strict integral midpoint bound gives

    log(pi/2)>log(25/16)>2(25/16-1)/(25/16+1)=18/41.

Thus

    H(0)<23/50-2(161/100)(18/41)/10
         =1633/5125<8/25.

For the lower bound use C0<4, log pi>11/10, hence k0<9/5;
log pi<23/20, log2>69/100, hence log(pi/2)<23/50;
and pi^2>197/20. All are the elementary scalar inequalities already
used in the C08/D10 predecessor proofs. Therefore

    H(0)>9/20-2(9/5)(23/50)/(197/20)
         =5553/19700>7/25.

For transparent provenance, the stronger accepted PD-T271 input is
0.919710118388492535099518225790<kappa
<0.919710118388492535099518225791. Those are quoted inherited bounds;
no scalar program was run, altered, previewed or proposed here.

## 6. Disposition and cheapest next paper task

The exact identities (4), (6), (7), (8), (9), (11), enclosure (12),
and conditional implication (10) are the complete partial result.
Unconditional Hmax and cosine shape remain OPEN. The cheap endpoint
test found no obstruction to either; the spectral sign alone is
inconclusive. The explicit, potentially decisive next paper task is to
prove or refute monotonicity of the smooth g on(0,pi), retaining its
negative periodic atom separately. It is a sufficient condition only;
failure of that condition would not refute Hmax. Alternatively, a direct
estimate of the exact signed difference (6) may prove the weaker
H<=H(0)+1/400 without settling g monotonicity.

No unconditional C_infty<9/4 or improvement of D10's near increment is
claimed. Those consequences require a further scalar hypothesis and
are developed separately. Complete D13 and whole-diamond E05 finite
error targets are unaffected and remain OPEN.
