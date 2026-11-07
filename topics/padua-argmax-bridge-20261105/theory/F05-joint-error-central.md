# PD-T?argmax-bridge-codex-F05-joint-error-central — Complete signed first-row root crossover

ID kind: PD-T. Aliases: actual first transported row versus signed root
integral; uniform centered-grid logarithmic coefficient.
Split from: F05 complete error crossover. Split into: none.

## Statement and exact objects

For EVERY n>=32 let m=n+1,h=pi/m,L=log n,alpha=c*h,beta=0,
c in CLOSED[1/2,3/2]. Use EXACTLY the continuous fixed-origin-sign excesses
Y_r and the SIGNED entire central integral E_c of accepted E05/E06. Then

    |(4/(nm))sum_(r=1)^n Y_r(alpha)-E_c(alpha,0)
                         -[c(c-1)/pi^2]h^2 L|<=200h^2.       (1)

Both parities and the actual c=1 polynomial collision are included. Exact
real arithmetic, no numerical premise. Overall status: **PROVED developer
PAPER support**, distinct review/root adoption required. The genuine central
cusp and the signed background/model subtraction are separate terms.

## Depends on

E05-axis-central-excess gives the exact fixed masks and transport, actual
first-coordinate root-strip error, the same signed E(e)=J(p/2,a tan(e/2),e)
-2a tan(e/2)log sin e, and E_c=(2/pi^2)integral E. E06 proves E is convex
and decreasing on e>=alpha, extended by zero after its root threshold;
its e<alpha entropy piece is retained with sign. E03's exact linked
central finite vectors handle the actual first row. N1/C01 supply the
literal entropy and root integral formulas. Their old restricted full-error
estimates are NOT transferred to this larger phase band.

## Proof

Throughout h<1/10,alpha<3/20<2/5. Only the first possible inner row,
e_1=h (r=m-1=n), can cross its denominator boundary; e_s>=2h>alpha for
every s>=2. All nonzero root-strip rows lie inside the actual folded set.

### 1. The actual first row, including its two linked peaks

Its original negative-sign mask is empty. Thus Y_n is exactly the sum of
the negative parts of its ACTUAL finite samples. Put

    theta_-=(alpha-h)/2,theta_+=(alpha+h)/2,
    w=cos(alpha/2)/(2cos(h/2)),
    F_k=w[L_(n,k)(theta_-)+L_(n,k-1)(theta_+)],
    L_(n,k)(theta)=sin(theta)cot((k*pi+theta)/n).

These are the accepted linked finite vectors, with L_(n,0)(0)=n and all
n cyclic residues, for BOTH parities. In particular no off-grid rational
row formula is used at the polynomial collision. At c=1,k=0 this gives
F_0=(n-cos h)/2=(n+cos v_n)/2>0, its true finite value.

Here |theta_-|<=h/4,0<theta_+<=5h/4<1/8 and0<w<=1.
At k=0,1 the linked peak term is >=99n/100. The other term has magnitude
<2, respectively <1, because h*n<pi and the closest other denominator is
at least(pi-1/8)/n. Both complete samples are therefore positive at n>=32,
including theta_-=0. They contribute ZERO to Y_n.

For k other than0,1 compare with(p/2)cot(k*pi/n),p=sin alpha.
The coefficient equality
w(sin theta_-+sin theta_+)=p/2 is EXACT. For the first shift, the segment
distance from a cotangent pole is >=(23/8)d_k/n,
d_k=min(k,n-k), so csc^2<=n^2/(3d_k^2). Its summed weighted error is
<h^2*n/12<1. For the second shift let l_k=min(k-1,n-k)>=1. Its segment
stays at distance>=pi*l_k/n and has length<=pi/n, giving total weighted
error <=5pi*h*n/4<25/2. Both estimates use sum d^-2,sum l^-2<4.
Thus the sum of absolute sample errors is <14. Applying the negative-part
Lipschitz inequality retains every moving sample zero without a sign premise.

Finally, with q=floor((n-1)/2),

    sum_(k=1)^(n-1)(-cot(k*pi/n))_+=sum_(j=1)^q cot(j*pi/n),
    |sum_(j=1)^q cot(j*pi/n)-(n/pi)L|<=2n/pi<n.

The last estimate uses |H_q-L|<=1 and0<=1/x-cot x<=2/pi on
0<x<=pi/2. Its weighted error after multiplication by p/2 is <3.
Consequently the uniformly finite estimate

    |Y_n-(n*p/(2pi))L|<30                              (2)

holds across c=1 and both parities. The large positive linked peaks were
retained explicitly, not replaced by their off-grid removable values.

### 2. Isolate the logarithm in the SAME signed model profile

Extend E by zero after e_*=arccos(1-tan(alpha/2)); e_*<pi/4. For x>=0
put f(x)=E(hx)/h and W_c(x)=min(x,c). The following elementary uniform
local estimate will be useful:

    |f(x)-L*W_c(x)|<=50, 0<=x<=5/2.                    (3)

At x=0 use the finite entropy limit E(0)=-p log2; no log0 is evaluated.
Here are explicit checks. On the inner piece x<c the same-sign formula
has |J|/h<=3/2 and2s/h<=101x/100, with
|2s/h-x|<=2h^2*x. Also
|log(sin(hx)/(hx))|<=(hx)^2 and x|log x|<=3 on this compact interval.
If h<1/100, |log(1/h)-L|<2 and h^2 L<1/16 show that subtracting
L*x leaves magnitude <12. If h>=1/100, use L<log400<7,
log(pi/(2h))<log200<6 and x<=c<=3/2; the same signed entropy
expression gives magnitude <24 after subtraction. These use x log x=0
at zero and preserve its signed integral.

For x>=c the opposite-sign root formula is

    E(e)=p integral_X^1 sqrt((1-z^2)/(1-lambda^2*z^2)) dz/z,
    X=(1-cos e)/tan(alpha/2),lambda=tan(alpha/2)/tan(e/2)<=1,

with zero value when X>=1. On0<X<1 the difference of that integral
from log(1/X) has magnitude at most1/2: its integrand ratio lies between
sqrt(1-z^2) and1, and integrate(1-sqrt(1-z^2))/z<=z. If h<1/100,
X<=h*x^2/c<=1/8, and

    |log[X/(h*x^2/c)]|<1/10,
    |p/h-c|<=h^2, |log(c/x^2)|<3.

Thus subtracting cL leaves magnitude <12, uniformly even at x=c.
If h>=1/100, either the profile is zero or its positive majorant gives
0<=E/h<= (3/2)log(4/h)<21/2, while cL<21/2. This proves (3)
with the allocated50 margin, without an inverse coefficient separation.

### 3. The full e-grid error, not a separate positive boundary allowance

Use unit centered cells [s-1/2,s+1/2],s>=1 and the missing[0,1/2].
The EXACT paired grid-minus-integral functional for W_c has value

    g(c)={c(c-1)/2,                1/2<=c<=1,
          (c-1)(c-2)/2,            1<=c<=3/2}.           (4)

This follows by integrating the one cell containing its kink and the
missing initial half-cell. W_c is constant after c. Its separate infinite
sum/integral are NOT assigned values: every tail cell has zero matched
error, so the paired functional is finite. This also justifies applying it
to R(x)=f(x)-L*W_c(x), which is constant in the far tail.

For R, the first two centered cells and the missing initial half-cell
cost at most200+25 by (3). On x>=5/2, R'=E'(hx), because W_c is
constant. The accepted convexity of the SAME outer profile gives
Var_[5/2,infinity)(R')<=|E'(5h/2)|<4. To check the last bound at an
active point use E06's exact derivative formula. One has
lambda<=16/25,cos e>=31/32 and consequently
q=D/(s cos e)<=512/775<2/3. Thus atanh q<1,s'<1, and
2D/sin e<=p/sin e<=3pi/10<6/5. At an inactive point the derivative
is zero. Unit midpoint error is therefore <1 on all the remaining cells
together. This includes the full root endpoint and zero extension.

Combining these finite matched-cell estimates gives

    |h sum_(s>=1)E(sh)-integral_0^infinity E(e)de
                                      -h^2 L*g(c)|<=250h^2.    (5)

The SIGNED inner interval is inside (5); no theta*E(k0h) charge has been
detached from it. The c=1 entropy crossing and c=1/2,3/2 cell-boundary
cases are included by continuous limits in (3)--(4).

### 4. Match actual rows and combine every central contribution

For all rows s>=2, E05's first-coordinate quadrature argument is INSIDE
its literal outer strip e_s>alpha. Restricting its positive error sum to
these rows preserves the bound16alpha/(5n)<2h^2. No inner sample is
placed in that estimate. For the first row combine (2) and (3) at x=1:

    |(4/(nm))Y_n-(2/(pi*m))E(h)
                -(2/pi^2)h^2 L[c-min(1,c)]|<28h^2.       (6)

Indeed the row error is <120/(nm)<15h^2, the model remainder <100h^2/pi^2
<12h^2, and replacing p/h by c costs <h^2 using h^2L<1/16.
All actual finite origins, weights, n/m and linked values remain.

Multiply (5) by2/pi^2 and add (6) and the remaining outer-row charge.
The combined logarithmic coefficient is exactly

    (2/pi^2)[g(c)+c-min(1,c)]=c(c-1)/pi^2.

The total remainder is <28+500/pi^2+2<100, in units h^2. This proves
(1) with its allocated200 margin. No fixed-positive-alpha O_alpha term
or exchange of phase and degree limits is used anywhere.

## Scope, checks and history

This is a finite uniform statement at alpha~1/n across the first actual
transported inner row. The whole E_c integral and its negative inner entropy
part are retained; the background/model term and real ell_n cusp must still
be added for the COMPLETE error. No beta!=0 extension, onset or global D13
closure follows. The generic N2 mixed collision sign is not assumed positive.

Paper reasoning and owned prose only. No scientific source/script/import,
measurement/scalar/phase/degree/endpoint/native/quadrature/build/pack job.
2026-11-07, requested Sol xhigh, serving metadata unexposed, supplied
rules4a5de2012bad94601c713b2ff5517f2e3fb80af2. Gate, separate release,
coefficient refinement and unchanged target are in ideas/attempts
F05-joint-error-crossover.md. Distinct mathematical adoption remains separate.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F04-F05.md), final SHA256ccdb1d774bd3653aadb26df3382be462043a5a7256bba2f41c909967fcf080f4. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
