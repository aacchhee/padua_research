# C03 — sharp pole-chart ranges and centered ratio jets

Rules 4b728b0; 2026-11-06. Mathematical developer proof; distinct review
pending. Classification: backend tightness variant, no new global ID or
historical trigonometric novelty claim. Gate and prospective claim:
[ideas/C03-ratio.md](../ideas/C03-ratio.md). C01/C02 formulas and evidence
are preserved. No implementation or cover is a premise of this record.

## Contract and status

For an integer k>=1 let R_k(z) be C01's entire finite trigonometric
polynomial, equal to sin(kz)/sin z off the removable poles. Given a
finite real interval Z, retain any valid finite pair V0,D0 enclosing
R_k(Z),R'_k(Z), initially C01's global caps if necessary. The following
optional candidates use bounded work at fixed precision/order:

1. On C01's literal pole chart, the value range is determined by two
   folded endpoints. Derivative signs are known on either side of the
   chart center. Their proof includes the first numerator zero.
2. On any finite Z, one bounded-work point jet and C01's closed second
   derivative cap give a centered Taylor value/derivative pair.
3. Away from sine zeros, the closed differential equation optionally
   lowers the second derivative cap before the same Taylor step.

Intersect admitted valid candidates. A nonfinite optional candidate is
ignored; finite disjoint candidates are an error, never a fallback
success. Always retain a finite valid pair. The mathematical enclosure
contract is **PROVED** below. Distinct review, executable conformance,
selected failing-box recovery and performance are separate requirements.
No assertion is made that all previously accepted boxes remain accepted.

The new endpoint value range is sharp in exact arithmetic on the admitted
residual interval: it equals its exact image, rather than the natural
interval extension of a quotient or Horner polynomial. Point arithmetic
and outward residual inflation add their ordinary enclosure widths.

## 1. Monotonicity on exactly the admitted chart

Define F_k(r)=R_k(r). For k>=2 set

    b_k=min(3/2,4/k).

Then F_k is even, F_k(0)=k, F'_k(0)=0, and

    F'_k(r)<0       for 0<r<=b_k.                    (1)

In particular F_k is strictly decreasing in |r| throughout this chart,
including its first zero when that zero is in the chart. This is not a
global monotonicity claim. For k=1 the pair is exactly (1,0).

**Proof.** Evenness and the data at zero follow from the finite cosine
polynomial. For 0<t<pi put f(t)=t cot t, continuously f(0)=1. Its
derivative has the sign of sin t cos t-t. The derivative of that numerator
is -2 sin^2 t and its value at zero is zero. Thus f is strictly decreasing
on (0,pi). Throughout the stated positive chart, 0<r<=3/2<pi/2, so
sin r and cos r are positive and f(r)<=1.

Write x=kr. If 0<x<pi, k>=2 gives r<x, F_k(r)>0 and

    F'_k(r)=F_k(r)*[f(x)-f(r)]/r<0.                 (2)

This identity is used here only where sin x is nonzero. At x=pi use
the uncancelled quotient derivative directly:

    F'_k(r)=[k*cos x*sin r-sin x*cos r]/sin^2 r
            =-k/sin r<0.                           (3)

If pi<x<=4, let y=x-pi. Elementary pi>3 implies
0<y<=4-pi<pi/3. Cotangent decreases on (0,pi), so

    f(x)=x*cot y > pi/sqrt(3)>1>=f(r).

Here F_k(r)<0 because pi<x<=4<3pi/2. Equation (2), now on the
negative lobe, again gives F'_k(r)<0. There is no division by sin x
at x=pi; (3) covers that point. These three cases prove (1).
Continuity and strict derivative sign on (0,b_k] imply strict decrease
on the closed interval [0,b_k]. QED.

The negative-residual derivative has the opposite sign by oddness of
F'_k. At r=0 it is zero; the theorem does not assert a strictly negative
derivative there. For k=2 the whole admitted chart has kr<=3<pi;
the negative-lobe proof is not needed in that case.

## 2. Exact turns, folded endpoints and endpoint enclosures

Choose any exact integer ell. Let Pi be an outward enclosure of exact pi
and construct A=Z-ell*Pi outward. This contains every true residual
r=z-ell*pi. Literal admission remains precisely

    sup|A|<=3/2,          k*sup|A|<=4.               (4)

Use exact integer parity:

    eps=(-1)^(ell*(k-1)),
    R_k(ell*pi+r)=eps*F_k(r),
    R'_k(ell*pi+r)=eps*F'_k(r).                      (5)

In code eps=-1 exactly when ell is odd and k is even, including negative
odd ell. No large signed product is needed. No nearest-pole assumption
or exact-pi floating representation is used in (4)–(5).

Let A=[a,b] as a real interval, and define its folded range

    rho_max=max(|a|,|b|),
    rho_min=0                         if a<=0<=b,
            min(|a|,|b|)             otherwise.

The exact image of F_k on A is

    [F_k(rho_max), F_k(rho_min)].                    (6)

Indeed |A| has exactly that folded interval as image, and section 1 is
continuous and strictly decreasing in its argument. If zero is crossed,
the upper endpoint is exactly k, not an interval sinc evaluation at a
range of arguments. Negative F_k values near the edge kr=4 are retained.
No positivity assumption on F_k is made.

For an outward implementation choose exact dyadic numbers l,u with

    0<=l<=rho_min<=rho_max<=u,
    u<=3/2,       k*u<=4.                            (7)

They may be exact outward endpoints of a validated absolute-value ball.
Check (7) on those actual extracted endpoints. In particular, an inward
rounded absolute radius is forbidden. Let E_l,E_u be valid point value
enclosures of F_k(l),F_k(u). A valid candidate for (6) is

    [lower(E_u), upper(E_l)],

multiplied by eps with endpoint order reversed if eps=-1. It is valid
also when (7) merely expands the true folded interval. At l=0 use exactly
F_k(l)=k. At other endpoints use a bounded-work C01 point evaluator or
its fixed J32 sinc value polynomial, with its proved remainder and positive
denominator. The J32 point error scales with k as in C01; it is not
silently treated as zero.

**Nonrecursive point evaluation is mandatory.** The endpoint routine
must call a base point evaluator, not itself request new endpoint/Taylor
refinements. Two endpoint values cost at most two base point evaluations,
and one is omitted when l=0 or the endpoints coincide. The derivative
need not be evaluated at these two endpoints merely to obtain (6).

When A is one-sided, (1) also gives a derivative sign candidate:

    A subset [0,infinity)   => eps*R'_k(Z)<=0,
    A subset (-infinity,0]  => eps*R'_k(Z)>=0.         (8)

Intersect with the appropriate half of [-C1,C1], C1=floor(k^2/2).
If A={0}, the derivative is exactly zero. If A contains both negative
and positive residuals, (8) gives no one-sided derivative sign.
The notation eps*R' in (8) is justified by eps^2=1 and (5).

Equations (4)–(8) are valid at every removable pole and numerator zero.
They require no logarithmic derivative at a zero and no division by
F_k. They do not apply outside the admitted residual chart. If its guard
fails, retain other valid candidates and the finite global fallback.

## 3. Centered Taylor jet on arbitrary finite intervals

This is C01 section 5's already proved optional refinement, restated as an
executable contract rather than a new candidate mechanism. The closed cap

    C2=k*(k^2-1)/3 >=sup_(real z) |R''_k(z)|          (9)

is exact, with no runtime frequency sum. Choose an exact dyadic center c
and form T=Z-c outward. Let H be any outward upper bound on sup|T|.
Let Vc,Dc be valid finite enclosures of R_k(c),R'_k(c) from one base
point evaluator. Then

    V_T=Vc+Dc*T+[-C2*H^2/2,C2*H^2/2],
    D_T=Dc+[-C2*H,C2*H]                              (10)

enclose R_k(Z),R'_k(Z). Taylor's integral remainder proves the value
formula, and the mean-value/integral derivative formula proves the other.
The error from uncertain Dc is included by the interval product Dc*T.

The exact interval midpoint minimizes H; however correctness only needs
the stated containment. A rounded floating proposal may be chosen as an
exact dyadic c provided the actual outward T,H are used. It is invalid to
pair a rounded c with an unadjusted theoretical half-width. With the
global C2 cap, (10) is valid even if c is outside Z. All cap products
must be overflow checked or formed with exact arbitrary-precision integers.

At k=1 return exactly (1,0), avoiding all unnecessary formulas. If Z is
a point already, (10) can be omitted. No recursive midpoint refinement
or k-term harmonic enumeration occurs. The base point evaluator may
use the separated quotient, the admitted sinc chart or finite global
caps according to C01's total contract. Wide base point caps remain
valid but can make this optional refinement ineffective.

## 4. Optional local curvature from the closed differential equation

If a validated J containing both Z and c has sin(J) excluding zero,
and valid V_J,D_J enclose R_k(J),R'_k(J), form outward

    K_J=(1-k^2)*V_J-2*cot(J)*D_J,
    M=min(C2, upper(abs(K_J))).                     (11)

Both scalar bounds in the minimum are upper bounds on sup_J|R''_k|.
Thus M may replace C2 in (10). The identity follows by differentiating
sin z*R_k(z)=sin(kz) twice and dividing by the nonzero sin z:

    R''_k=(1-k^2)R_k-2 cot z R'_k.                  (12)

Use only validated separated cotangent arithmetic in (11). An interval
containing a sine zero rejects this optional candidate, even if the
underlying function is removable. An indeterminate or very wide K_J is
ignored in favor of C2. The input V_J,D_J can be the preexisting pair;
there is no curvature/Taylor recursion. If c is the exact midpoint in Z,
take J=Z. Otherwise supply the larger validated hull. A curvature bound
proved only on Z cannot justify Taylor paths through an exterior c.

No claim is made that (11) usually beats C2; interval cancellation can
make it much worse. It is optional and should be omitted if its scalar
cost exceeds its observed benefit. Polynomial second jets near zero are
not needed for this proof and are not proposed as an unreviewed shortcut.

## 5. Implementation staging and review cases

The mathematical intersection contract can be implemented as follows:

1. Validate k/input finiteness and initialize C01's global finite pair.
2. Obtain the existing separated quotient and/or sinc pair when their
   actual guards admit them.
3. If the pole-chart guard admits the actual residual interval, obtain
   endpoint value and sign candidates from section 2. Their correctness
   is independent of whether step 2 used a quotient. In particular an
   unconditional early return after a successful quotient would skip
   this intended tightening on many separated near-pole intervals.
4. Optionally obtain the one-center Taylor pair in section 3, globally
   or with a validated section 4 curvature bound. Intersect value and
   derivative candidates with the existing valid pair.
5. Commit finite intersections; reject finite contradictions. A value-only
   candidate can be staged as a pair with the unchanged valid derivative,
   and similarly for a derivative-only sign candidate. It is unnecessary
   to require both components to become strictly narrower in one stage.

All candidates are mathematical supersets of the same true images.
Their exact intersection therefore preserves validity and never enlarges
the prior sets. Conversion to a finite-precision ball can reintroduce a
tiny outward radius; exported scalar upper/lower bounds may retain the
appropriate minimum/maximum to preserve a previously valid scalar bound.
Empty valid finite intersections must not be accepted as a width win.

The first logical controls are already settled by the proof:

* k=1: constant 1 and derivative 0, every turn and argument.
* r=0: value eps*k, derivative 0; zero-crossing intervals include this
  extremum. A strict derivative sign is asserted only for r!=0.
* kr=pi: value 0 and derivative -eps*k/sin(pi/k) on the positive side;
  use the direct derivative, not an undefined cotangent factor.
* pi<kr<=4: values are negative before turn parity; they continue to
  decrease. Clipping them to a positive sinc range would be wrong.
* negative r: value even before parity, derivative odd. The negative-side
  derivative sign in (8) is the reverse of the positive-side sign.
* negative odd ell and even k: eps=-1, reversing the value range and both
  one-sided derivative inequalities. Odd k always has eps=1.
* outside (4): no monotonicity candidate. For example R_3(r)=1+2cos(2r)
  is increasing at r=2, so global extrapolation would be false.

This closes the rigorous range/jet specification and the logical edge
cases before implementation. It does not guarantee how much S or a
corner orbit improves: primitive products and the whole-sum gradient
still have their own interval dependencies. Root0/path0101 and any
additional selected failure controls must be measured separately under
the independent review and CPU budgets. No full replay is authorized by
this helper theorem, and failed C01/C02 receipts remain intact.
