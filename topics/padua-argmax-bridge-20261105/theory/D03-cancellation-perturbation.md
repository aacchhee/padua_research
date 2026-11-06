# PD-T?argmax-bridge-codex-D03-cancel — Difference quadrature after symmetric-channel subtraction

ID kind: PD-T. Aliases: D03 cancellation perturbation; floor-free
sine-channel quadrature error; equal-opposite reference BV estimate.
Split from: D02-far-target, whose practical full residual remains OPEN.
Split into: none. This is a supporting lemma, not the sharp far theorem.

## Statement

Let v be real with v not in pi*Z and let
e=dist(v,pi*Z), so 0<e<=pi/2. Let w be any real number and let c,d be
real with |c|,|d|<=E, E>=0. On the circle R/(pi*Z) define

    g(C,D,v;x)=|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|,
    f(x)=g(-w+c,w+d,v;x)-g(-w,w,v;x).                    (1)

At the two cotangent poles give both g functions value zero. Then

    sup|f|<=4E*cot(e/2),
    Var_per(f)<=112E*cot(e/2)<=224E/e.                  (2)

For any shifted n-point mesh x_k=x0+k*pi/n avoiding both poles,

    |sum_k f(x_k)-(n/pi)*integral_0^pi f(x)dx|
         <=56E*cot(e/2)<=112E/e.                       (3)

No coefficient sign, positive lower bound on |w|, root separation or
smooth dependence on a parameter is assumed. At E=0 all quantities vanish.

For the corrected Padua phases alpha,beta>=0, alpha+beta<=pi, put
p=sin alpha, q=sin beta, P=p+q, a=(cos alpha+cos beta)/2 and

    w(v)=a*cot(v/2)/2,
    C(v)=-w(v)+(p-q)/4, D(v)=w(v)+(p+q)/4,
    g0(v;x)=g(-w(v),w(v),v;x).

Use N1-02's actual special rows A_R (first/last R, central m-1,m,
and all exact polynomial-collision rows), for any integers n>=2,
2<=R<=n and m=n+1. Let O be any subset of the remaining rows. For
v_r=(r*pi+beta)/m and the actual ordinary row mesh x_rk=(u_k-v_r)/2,
define the two exact cancellation quadrature errors

    T_r =sum_k g(C(v_r),D(v_r),v_r;x_rk)-(n/pi)*I(C,D,v_r),
    T0_r=sum_k g0(v_r;x_rk)-(n/pi)*integral_0^pi g0(v_r;x)dx.

Then

    |(1/(nm))*sum_(r in O)(T_r-T0_r)|
       <=112P*H_n/(pi*n) <=56P*H_n/n.                  (4)

This bound has no fixed-R floor and vanishes when P=0. Separate absolute
phases extend it to the signed diamond using the established phase-even
primitive convention; no exchange of n and n+1 meshes is made.

## Status and assumptions

Overall status: **PROVED**, exact-real elementary developer proof below.
Distinct mathematical review remains a publication obligation. The scope
is the difference of two cancellation quadrature errors, not the entire
S_n-M_infty remainder. In particular T0 itself is not bounded by (4).

Dependencies: N1-02's exact ordinary-row mesh, polynomial collision set
and shifted-BV midpoint inequality; N1-03's equal-opposite integral is
the closest predecessor. The new difference bound is proved directly.
No computation, fitting, quadrature run or external source is a premise.

## Proof

### Pointwise cancellation sandwich

Write X=cot x, Y=cot(x+v), and A=|w|. Each g is nonpositive and equals
-2min(|CX|,|DY|) if its channels have opposite signs, and zero otherwise.

If A>E, the two perturbed coefficient signs agree with the corresponding
reference signs. When X,Y have opposite signs, both cancellations are
zero. When X,Y have the same sign, their coefficient magnitudes lie in
[A-E,A+E]. Therefore the perturbed minimum lies between
(A-E)min(|X|,|Y|) and (A+E)min(|X|,|Y|), while the reference minimum
is A min(|X|,|Y|). Hence |f|<=2E min(|X|,|Y|).

If A<=E, the perturbed coefficient magnitudes are at most2E. Each of
the two nonpositive cancellations has magnitude at most4E min(|X|,|Y|).
Their difference in magnitude is bounded by the larger magnitude, so
|f|<=4E min(|X|,|Y|), including coefficient sign changes.

The two poles on the pi-circle have separation e. At least one of x
and x+v has distance at least e/2 from pi*Z. Its cotangent magnitude
is at most cot(e/2). Thus min(|X|,|Y|)<=cot(e/2), proving the first
bound in (2). It also proves finite one-sided limits at each pole.

### Finite sign complexity gives the variation bound

Partition the pi-circle at the two poles, the two cotangent zeros,
and the zeros of C cot x+D cot(x+v). There are at most six points.
Indeed its numerator after multiplication by sin x sin(x+v) is

    [(C+D)sin(2x+v)+(C-D)sin v]/2,

which has at most two zeros per pi period unless it is identically
zero. In that exceptional case C=D=0, and no extra partition is needed.
The symmetric reference numerator is -w*sin v and has no additional
zeros unless w=0, when its entire cancellation is zero.

On each of the at most six open arcs, all relevant signs are fixed,
so f is a linear combination b1*cot x+b2*cot(x+v). Its derivative
has at most one zero there. To see this when b1*b2<0, its zero equation
is [sin(x+v)/sin x]^2=-b2/b1. The ratio has constant sign on the arc
and derivative -sin v/sin^2 x, so its square is strictly monotone.
The remaining coefficient cases give a constant derivative sign or the
zero function. Thus f has at most two monotone pieces on each arc.

Let M=4E*cot(e/2), the proved uniform bound. Each monotone piece has
variation at most2M. The total arc variation is therefore at most24M.
At each pole, the assigned zero value costs at most2M between its two
one-sided limits; there are two poles. All other breakpoints are
continuous because absolute values of finite functions are continuous.
Hence Var_per(f)<=28M=112E*cot(e/2), including every pole jump and
every moving zero. Since cot(e/2)<=2/e, (2) follows.

N1-02's centered-cell BV inequality bounds a shifted sample-sum error
by half the periodic variation when samples avoid the poles. This
gives (3), including meshes passing through ordinary numerator zeros.

### Sum over the actual ordinary rows

For the Padua coefficients take E=P/4 in (3). It bounds the r-th
error difference by28P/e_r, e_r=dist(v_r,pi*Z). N1-02's special set
ensures v_r is neither endpoint nor pi and neither pole is sampled.
All exact polynomial collisions remain special; no value of their
polynomial row is replaced by the reference cancellation.

For r<=m-2 put k=r and l=m-r-1; for r>=m+1 put
k=2m-r-1 and l=r-m. All these integers are positive outside A_R,
and e_r>=pi*min(k,l)/m. Consequently

    1/e_r<=m/pi*(1/k+1/l),
    sum_(r outside A_R)1/e_r<=4m*H_n/pi,

because each positive k and l occurs at most twice and none exceeds n.
Summing28P/e_r and dividing by nm proves the first bound (4).
The weaker second bound follows from pi>2. Any subset O only lowers
the positive upper sum. Separate phase evenness provides the stated
signed extension with the same absolute phases and row convention. QED.

## Scope and unresolved reference

The actual weighted pole products and every special polynomial row
remain part of the full primitive. A symmetric A-only *whole-kernel*
reference has unweighted collision poles and cannot simply replace them.
Only its bounded cancellation g0 is used here. The actual full-phase
linear-logarithmic coefficient is retained, including its boundary term.

To obtain the practical D02 target, the remaining symmetric error T0
must be combined with the endpoint rows and their exact finite-part
limit before taking absolute values. Its finite-n evaluation is not
compactified or bounded here. N1-09's near-only positive-numerator
assumptions are not imported, and no old degree quantifier is extended.
An O(P*H_n/n) bound for the perturbation alone does not establish the
whole target or a useful global onset.

## Checks and history

Paper proof only; no numerical run. All roots and pole limits are
covered by the finite sign partition, rather than h-Taylor smoothness.
Gate and retained alternatives: ideas/D03-joint-finite-h.md. Exact
remaining obstruction and next test: attempts/D03-joint-finite-h.md.

2026-11-06, rules/input
`084a64f6465956f9c75b5538f83752c30318f151`; parent-requested Sol xhigh
mathematical work, serving metadata not independently exposed. This
bounded supporting lemma is the output of the initial capped D03
analytical block; timing limitations are recorded once in the attempt.
No code, shared registry or old proof was edited.
