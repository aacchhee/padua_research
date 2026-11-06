# Independent supplementary review — actual residual axis limit

Reviewer: distinct Codex `/root/c01_near_review`, parent-assigned Astra high;
serving identity and effective effort are not independently exposed.
Date: 2026-11-06. Rules and input HEAD:
`4b728b04216a5490910780bc609a82b853058426`, branch
`codex/padua-argmax-bridge-20261105`.

**Disposition: accepted at both written scopes, with no mathematical
finding.** The actual limiting Q_n residual has the stated positive
fractional axis coefficient. The proposed uniform quadratic/entropy-only
modulus with vanishing degree errors is refuted in exactly the specified
sense. Neither conclusion closes or refutes C1. This independent check
supplements the required Claude formal audit, which remains pending.

## Frozen scope and method

| New source | SHA-256 |
|---|---|
| `theory/C01-near-axis-limit.md` | `0dcb039e5b7a913f6e00b3f7f1a86b28a428665824822e7b98cce7aa7848338c` |
| `theory/C01-near-quadratic-obstruction.md` | `a1e217f904857d4d301e28085b3b63e0f96e853df93c7d7abb8b92ff2cd5575b` |

Both records were read in full, their file identities checked, and their
mathematics reconstructed independently. The previously accepted central
majorant and normalization are recorded in
`independent-checks-C01-near-central.md`; its source remains
`ef5b3b62e5c079889525f291b4874bb6aff8b1033ef790de67aa62f62ee361b7`.

In addition to the rules, handoffs 05/06, LOG, full N1-05/14/16/18/19,
N1-15 model definitions, C1 and round-8 review already read for the central
component, this review read full N1-07, N1-09, N1-10, N1-11 and N1-13;
N1-06's constant definitions; N1-17's residual definition; and the complete
PD-N079 negative record to verify the distinction between the two ordered
limits. The C01 idea/attempt were refreshed. New dependency identities:

| Dependency | SHA-256 |
|---|---|
| N1-07 | `7f5c1b44ad6d502b85b5b89c6a563c2e2d90ad65d86bb205063e4a86f3703b61` |
| N1-10 | `c694f98b2c7f8f01b6911df409208d113e651801e875fe069fb454f92b76a928` |
| N1-11 | `cd81ff9539c3eba5c34d3361d855a371dafc7230c635087682541640c93851bf` |
| N1-13 | `722e4ce4c275fee5217f4b473384985fa84789b869019077be49c9b2319bc74f` |

The assigned scope is analytic validity of the two precise statements,
including the negative statement's quantifiers. Historical novelty,
priority, allocation and the author's search chronology are excluded.
No full state/IDEAS novelty audit is claimed; the pure mathematical
no-novelty review scope is retained from the first component. No numerical
integral, mathematical program, fit, diagnostic or computational proof was
used. Only source reads, searches, file hashes and this new report were
performed. No author source, earlier report, shared file or Git state was
changed.

## Degree limit of the actual fixed residual

Write L=log n and k=log(delta/pi). At beta=0 the two strip offsets are
exactly t_L=0,t_R=1 for every n. Thus Hstar and Gstar are fixed constants
from the J=4096 truncated definitions, independent of both n and alpha.
They must remain in the limiting formula; replacing them by the infinite
series would change the defined model. The submitted proof retains them.

For each side, log b_s=L+k+O(1/n) and Z_n=D0+O(1/n). Direct expansion of
N1-10's two singular primitives gives, after summing both sides,

    B0 L² + (2D0+2B0 k)L
      +D0(2k+Hstar)+B0(k²+Gstar)+o(1).

The error products with L tend to zero; floor values introduce no
persistent oscillatory constant. The regular strip term is exactly L
times its integral coefficient, up to O(L/n), since f is bounded and
the actual endpoints converge at rate O(1/n). On this axis q_s=0.
In fact U1=0 identically, because c_e=c_d and the two offsets in its
definition coincide. Thus no constant strip term was omitted.

The exact finite-h endpoint rows have limit C_R(alpha,0) by N1-07;
its error tends to zero with R fixed at 128. The right block has r=1,...,R
while the left has r=0,...,R-1, exactly matching the submitted C_R.
N1-09 confirms that the model retains the exact rows to which N1-07
applies. The remaining at most four H8/Rhat special rows contribute
O((1+L)/n), including polynomial collision values, so their H8 choice
and parity branches leave no constant term.

The outer lower endpoints tend to delta and the upper endpoints to pi;
at most two collision holes have total length O(1/n). The A integrands
are uniformly bounded on the resulting region away from zero, so their
integral errors multiplied by L vanish. The B integrands are integrable
up to pi by N1-14, so their removed-cell integrals vanish. On beta=0 its
central logarithmic coefficient (q-p)_+ is actually zero; retaining the
more general integrable-log argument is also valid, including alpha=0.
The resulting B integral is precisely the one over [delta,pi] in (2).

For M_jump, A2_b=-2ab/pi is zero on both sides because b=0. Every other
term has its explicit 1/n factor, a bounded integral or fixed truncated
constant, and at most log n growth. It therefore vanishes. The possible
half-angle cutoff and all other artifact corrections need not be assigned
an invented limit: the already proved |F_n-Q_n|<9/(2n) transfers the
computed limit of the original residual to Q_n directly.

N1-16's exact b_M is the sum of the strip and outer L coefficients just
identified. Subtracting B0 L²+b_M L thus leaves exactly r_infinity in
(2), for every fixed alpha in [0,1/2]. Taking the difference from alpha=0
and applying the artifact envelope proves (3) for the stated Q_n.
This uses integer n tending to infinity without a parity subsequence.

## Quadratic size of the other limiting terms

The finite endpoint profile uses only the finitely many denominators
(r*pi)²-(j*pi+alpha)² with |j|<=r-1. They remain separated from zero
near alpha=0. Pairing j and -j proves smooth even dependence; j=0
is itself even. The prefactor a is even and the closest-row limit is
1. Consequently its increment is O(alpha²).

B0 and D0 are smooth and even near zero: for U0 this follows from the
reciprocal-pair series and the equal beta=0 offsets near 1/2. The fixed
Hstar/Gstar introduce no further phase dependence. All their increments
in the limiting strip constant are therefore O(alpha²).

For the regularized pole numerator, let c=cos(alpha/2),
x=(pi-z)/(2pi), and t=alpha/(2pi). Periodicity and reflection give on
each folded side exactly

    N_s(z)=c[Phi0(x+t)+Phi0(x-t)].

Thus the sum of the two sides is twice this expression. The denominator
2sin(z/2) is bounded away from zero for delta<=z<=pi. N1-13 supplies
both the bounded second derivative on open periods and the finite
integer derivative jumps, so Phi0' has finite variation on a fixed
enlargement of the x interval containing all small translates.

For an absolutely continuous f with f' of variation V on that enlarged
interval, integration of

    f(x+t)+f(x-t)-2f(x)
       =integral_0^t [f'(x+s)-f'(x-s)] ds

gives the L1 bound Vt². The inner translation difference has L1 norm
at most 2sV, including the jump part of the derivative measure.
Multiplying by a bounded denominator weight preserves this O(t²) bound;
no derivative of the moving cusp is discarded. The factor c-1 is
O(alpha²), completing the pole-numerator estimate.

On delta<=z<=pi/2, N1-10's exact two-side cancellation sum is
4a cot(z/2)log(sin z). Its fixed-domain integral has an O(alpha²)
increment. The central baseline is a Ic(0,0), also with an O(alpha²)
increment. Therefore the only possible contribution of order
alpha^(3/2) is the exact central moving-root correction isolated in
section 3 of the source.

## Scaling the central correction

On beta=0, tau=u/a=tan(alpha/2), and s=a tan(e/2). For e<=alpha
the same-sign entropy formula bounds |J| by 2u log2 and s<=u.
Hence the integral of |E| on (0,alpha) is O(alpha²[1+log(1/alpha)]).
On (alpha,2alpha), E=H>=0 and H<=2u log(2/e) yields the same order.
Dividing these contributions by alpha^(3/2) makes them vanish.

For e>=2alpha, s>u and E equals the exact positive root integral.
Here lambda<=tan(alpha/2)/tan alpha=(1-tau²)/2<=1/2. Set
e=sqrt(alpha)y and extend the scaled function by zero outside its
actual e domain and root support. For each fixed y>0,

    x=(1-cos(sqrt(alpha)y))/tan(alpha/2) -> y²,
    lambda -> 0,  2u/alpha -> 1.

The scaled E/alpha therefore tends to h(y²) for 0<y<1 and to zero
for y>1. The value at y=1 is immaterial to integration.

The proposed domination is valid on the whole moving domain. The cosine
chord and tau<=8alpha/15 give

    x >= [15/(4pi²)]y² >= y²/3.

Thus nonzero support lies in y<sqrt(3). Also
h(x)<=log(1/x)<=log(2/x), and the denominator correction is at most
2/sqrt(3). Since 2u/alpha<=1, the source's bound
(2/sqrt(3))log(6/y²) on (0,sqrt(3)) is nonnegative, independent of
alpha and integrable at zero. Dominated convergence applies without
discarding a moving lower endpoint or assuming uniform pointwise
convergence there.

The measure change de=sqrt(alpha)dy yields

    lim alpha^(-3/2) integral E de = integral_0^1 h(y²)dy.

Differentiation gives d h(y²)/dy=-2sqrt(1-y^4)/y. Its integration-by-parts
boundary terms vanish: h(1)=0 and y h(y²)=O(y log(1/y)) at zero.
Consequently the last integral is 2I4. There are exactly two folded
copies, each with normalization pi^-2, so the coefficient is
kappa=4I4/pi². No additional half-kernel or phase-folding factor remains.

Strict integration of 1-y^4<sqrt(1-y^4)<1-y^4/2 on (0,1) gives
4/5<I4<9/10. With pi²<10 and pi²>49/5 this proves precisely
8/25<kappa<18/49. All other limiting contributions are o(alpha^(3/2)),
so the claimed asymptotic is for q_infinity itself.

## Negative quantifiers and scope

The rejected inequality fixes finite K0,K1 independently of n and alpha
and permits arbitrary nonnegative sequences c_n->0 and J_n->0. Fixing
any alpha>0 first allows both sequence terms to disappear as n tends to
infinity. The existence proof just checked supplies the resulting
inequality for q_infinity. Only after that limit does alpha tend to zero.
Dividing by alpha^(3/2) makes both alpha² and alpha²log(1/alpha)
terms tend to zero, while the left side tends to kappa>0. The
contradiction is valid without any uniform convergence rate in n.

The same argument with a retained k alpha^(3/2) proves the necessary
condition k>=kappa, and nothing sufficient. Fixed additive allowances,
n-growing quadratic coefficients, a nonvanishing linear coefficient or
adequately sized fractional terms are outside the stated rejection.
In particular G_n has growing favorable quadratic coefficients and the
C1 target has a positive fixed tolerance, so this obstruction neither
refutes nor proves Q_n-G_n<=1/40000. PD-N079 takes alpha to zero at
fixed n and concerns the primitive's linear cusp; the current ordered
limit and vanishing-error obstruction are not substituted for it.

## Findings and completion

No BLOCKING, MAJOR or MINOR mathematical finding in either frozen source.
No author repair was made or required before acceptance. The whole-axis
degree limit, the positive fractional asymptotic and the exact scoped
negative implication support their stated PROVED statuses. No finite-n
rate, complete upper modulus, C1 conclusion, effective onset or physical
argmax obstruction is accepted. Formal Claude audit remains pending.
