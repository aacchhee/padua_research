# PD-T?argmax-bridge-codex-N1-06 — Compact endpoint mesh profile

ID kind: PD-T. Aliases: joint shifted harmonic/logarithmic sum;
endpoint logarithmic coefficient quadrature. Split from: round-4 H4,
whose finite polynomial rows and collision corrections are separate.
Split into: none. No reviewed N1 proof is changed.

## Statement and definitions

Use the first phase quadrant and a,p,q,A(v),U0 of N1-05. Let R>=2 be an
integer, 0<delta<=pi/4, n>=ceil(2pi R/delta), m=n+1, L=log n, h=pi/m,
X=delta/h. Define t_L=beta/pi, t_R=1-beta/pi and
K_s=floor(X-t_s). Thus K_s>=R. Set A_L(z)=A(z), A_R(z)=A(2pi-z),

    f_s(z)=A_s(z)-4a/(pi z),
    B0=4a/pi^2, D0=U0/pi+B0 log pi, kappa=log(delta/pi).

For 0<=t<=1 define convergent series, with x_k=k+t and a_R=R+t-1/2,

    h_R(t)=-log a_R+
      sum_{k=R}^infinity [1/x_k-log((x_k+1/2)/(x_k-1/2))],
    g_R(t)=-(log a_R)^2/2+
      sum_{k=R}^infinity [log(x_k)/x_k
        -{log^2(x_k+1/2)-log^2(x_k-1/2)}/2].            (1)

Write h_sum=h_R(t_L)+h_R(t_R), g_sum=g_R(t_L)+g_R(t_R), and

    b=2B0*kappa+2D0+(1/pi)*integral_0^delta(f_L+f_R),
    c_mesh=B0*kappa^2+2D0*kappa+D0*h_sum+B0*g_sum.       (2)

Then the entire unperforated endpoint mesh sum

    M_mesh=(1/m)*sum_{s=L,R} sum_{k=R}^{K_s}
       [A_s(h(k+t_s))*L
         +{U0+(4a/pi)*log(h(k+t_s))}/{h(k+t_s)}]

satisfies

    |M_mesh-[B0 L^2+b L+c_mesh]| <= e_mesh(n;R,delta),   (3)

with the following explicit phase-uniform error. Put

    H_R^*=log(R+1/2)+1/[8(R-1/2)^2],
    C_X=[5+(1/2)log(X+1/2)]/[2(X-1/2)]
            +[6+(1/2)log(X+1/2)]/[8(X-1/2)^2].

One may take

    e_mesh=(2R+3)*L/(2m)+2C_X+(8+H_R^*)/n+1/(2n^2).

In particular,

    e_mesh <=[R+10+H_R^*+10pi/delta]*(1+L)/n.          (4)

The coefficient formulas contain no degree-dependent summation count.
The series in (1) have explicit tails below; their truncation errors
must still be multiplied by their displayed coefficient factors.
Equations (3)-(4) are valid at a=0 and at either phase vertex.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof below; distinct
review pending. Exact real arithmetic. No numerical fit, run or imported
source theorem is a premise. Definitions and |U0|<=8 come from N1-05
and N1-04. The elementary shifted sums and variation argument below were
developed in parallel by /root/n1/endpoint_check under the preregistered
[round-4 candidate](../ideas/N1-round4.md), then assembled here.

## Proof

### 1. Uniform shifted constants and tails

For a twice differentiable f, Taylor's integral remainder gives the exact
centered-cell identity

    f(x)-integral_(x-1/2)^(x+1/2) f(y)dy
      =-(1/2)*integral_(-1/2)^(1/2)
            (1/2-|u|)^2 f''(x+u)du.

The kernel magnitude is at most 1/8. For f(x)=1/x it follows that, for
b_K=K+t+1/2 and K>=R,

    sum_{k=R}^K 1/(k+t)=log b_K+h_R(t)+epsilon_h,
    0<=epsilon_h<=1/(8b_K^2).                          (5)

For f(x)=log(x)/x, use x>=R-1/2>=3/2 and

    |f''(x)|<= (2log x+3)/x^3,
    integral_b^infinity (2log x+3)/x^3 dx
         =(log b+2)/b^2.

Thus

    sum_{k=R}^K log(k+t)/(k+t)
       =(log b_K)^2/2+g_R(t)+epsilon_g,
    |epsilon_g|<=(log b_K+2)/(8b_K^2).                 (6)

These also bound the tails of the defining series after K. Their bounds
are uniform in t by replacing b_K with K+1/2. This proves uniform
convergence, including t=0,1, and

    |h_R(t)|<=H_R^*.

### 2. Exact regular coefficient and bounded boundary layer

The identity |x-y|+|x+y|=2max(|x|,|y|), applied to the actual N1 row
coefficients, gives for 0<z<=delta

    A_L(z)=max(p,q+T(z))/pi,
    A_R(z)=max(p,|q-T(z)|)/pi,
    T(z)=2a cot(z/2).

Put u(z)=T(z)-4a/z. Then u decreases from zero, since
u'=-a csc^2(z/2)+4a/z^2<=0. Also

    0<=-u(z)<=a*pi*z/6,                               (7)

by 1/x-cot x<=pi x/6, obtained from
sin x-x cos x=integral_0^x t sin t dt and the sine chord.
Consequently

    pi*f_L=max(q,p-T)+u,
    pi*f_R=max(-q,p-T,q-2T)+u.

The max terms are increasing in z. With
M=max(p,q)/pi+a delta/6, these formulas imply

    |f_L|,|f_R|<=M<1/2,
    Var(f_L)<=(p-q)_+/pi+a delta/6,
    Var(f_R)<=[q+max(p,q)]/pi+a delta/6,
    Var(f_L)+Var(f_R)<=2M.                             (8)

At a=0, p=q and both f functions are exactly p/pi. For a>0 their
endpoint limits are q/pi and -q/pi. A joint limit at (a,z)=(0,0) is not
asserted; the bounded variation estimate includes this boundary layer.

For completeness the integrals in (2) have finite elementary formulas.
When a>0, let

    c_L=min(delta,pi-alpha+beta),
    c_1=min(delta,pi-alpha-beta),
    c_2=min(delta,pi+alpha-beta),
    W(z)=4a log(2sin(z/2)/z), W(0)=0.

All three c values are positive, c_1<=c_2, and W'=u. The exact switches
in the max formulas above give

    pi*integral f_L = q*c_L+W(c_L)+p*(delta-c_L)
                        -4a log(delta/c_L),
    pi*integral f_R = -q*c_1+W(c_1)+p*(c_2-c_1)
                        -4a log(c_2/c_1)
                      +q*(delta-c_2)-W(delta)+W(c_2)
                        -8a log(delta/c_2).            (9)

Each integral is from 0 to delta. Empty pieces contribute zero. At a=0
use p*delta/pi for either integral. Uniform boundedness in (8), followed
by removing an arbitrarily short initial interval, shows these integral
formulas extend continuously to a=0. There is no inverse-a estimate.

For any one shifted mesh, centered-cell BV quadrature gives

    |h*sum_{k=R}^{K} f(h(k+t))-integral_0^delta f|
       <=h*[Var(f)/2+(R+1)M].                         (10)

One rigorous endpoint convention is to extend f constantly past delta
when the final centered cell crosses it. This does not increase M or
variation. The omitted initial interval has length at most h(R+1/2),
and the final excess or missing interval has length at most h/2. The
centered-cell Stieltjes error has weight at most h/2. This proves (10)
using only values of f on [0,delta]. Combining both sides gives the
first error term of e_mesh after multiplication by L/pi.

### 3. Joint cancellation and the polynomial in L

For one endpoint, its singular coefficient sum is exactly

    Z_n*sum_{k=R}^K 1/(k+t)
             +B0*sum_{k=R}^K log(k+t)/(k+t),
    Z_n=U0/pi+B0*(L+log h)=D0-B0*epsilon,
    epsilon=log(m/n), 0<=epsilon<=1/n.                 (11)

In particular its harmonic coefficient contains no growing L. This is
the cancellation lost by expanding the A and constant-profile terms
independently. Write b_K=X+lambda, |lambda|<=1/2. Equations (5)-(6)
first replace the finite sums by
Z_n(log b_K+h_R)+B0((log b_K)^2/2+g_R).
Use |Z_n|<=5, 0<=B0<1/2 and b_K>=X-1/2 to bound their tail error by
the second term in C_X. Replacing log b_K by log X costs at most its
first term, by the mean value theorem applied to
Z_n log y+B0(log y)^2/2. Here X>=2R>=4.

Since log X=L+kappa+epsilon, the resulting expression equals

    (B0/2)*(L+kappa)^2+D0*(L+kappa+h_R)+B0*g_R
       +epsilon*(D0-B0*h_R)-(B0/2)*epsilon^2.          (12)

The potentially growing epsilon*L terms cancel exactly. Because
|D0|<=4 and |h_R|<=H_R^*, the last two terms cost at most
(4+H_R^*/2)/n+1/(4n^2). Add the two endpoint expressions and (10).
Their coefficients are exactly (2), proving (3).

Finally X-1/2>=7X/8, log(X+1/2)<=log m<=L+1, and X>=4 give
C_X<=5(1+L)/X. Using 1/X<=pi/(delta*n) in (3) proves (4).

## Scope and history

This is a genuine removal of the growing endpoint mesh sums with a
uniform error, not a change of special-function notation. It does not
include the first/last R polynomial rows or collision holes transferred
to those rows in H4. Those must be added before claiming H4. The central
chart, interior quadrature, complete model error and effective argmax
onset remain OPEN. No B3/B4 verdict follows from this component.

2026-11-06, after parent-pushed bda45a4; Codex N1 under the retained
requested gpt-6-astra ultra allocation. No new mathematical execution or
fit occurred. The accepted round-3 proofs remain unchanged.
