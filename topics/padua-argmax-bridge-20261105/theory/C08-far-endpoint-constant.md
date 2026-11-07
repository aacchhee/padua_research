# PD-T?argmax-bridge-codex-C08-far-03 — Exact endpoint constant and a uniform paired tail

ID kind: PD-T. Aliases: triangular harmonic convolution; paired cutoff
increment; renormalized H4 endpoint constant. Split from: the C08 compact
constant comparison, still OPEN. Split into: none.

## Statement and status

Use exactly N1-06/07's full-phase quantities C_R,h_R,g_R,B0,D0, with
alpha,beta>=0, alpha+beta<=pi. Put

    t=beta/pi, t_d=1/2+(alpha-beta)/(2pi),
    t_e=1/2+(alpha+beta)/(2pi), a=(cos alpha+cos beta)/2,
    E_R=C_R+D0[h_R(t)+h_R(1-t)]
               +B0[g_R(t)+g_R(1-t)],
    E_infty=a/3+a C(t_d)C(t_e)/pi^2.                   (1)

The weighted products in E_infty use their continuous limits, as proved
below. For every integer R>=64,

    |E_R-E_infty|<1/(R-1)^2,                          (2)
    E_infty<49/25.                                   (3)

In particular E_64<49/25+1/3000. These are full closed-triangle bounds,
including a=0, both vertices, and every finite sinc collision.

**PROVED**, written analytic developer result. Independent reconstruction
and formal audit are separate. It supplies only the endpoint part of
C_far: the remaining renormalized integral is not bounded here. No
mathematical program, quadrature, fit or finite-degree sample was run.

Dependencies: full N1-06/07 definitions and proofs; the C08-far-01
weighted scalar inequality; the locally proved cotangent partial fraction
in PD-T269. All elementary shifted-sum identities used below are proved
from convergent series. Gate: ../ideas/C08-far-comparison.md.

## 1. Shifted harmonic notation and uniform elementary error

For x>0 define

    psi(x)=lim_(M->infty)[log M-sum_(k=0)^(M-1)1/(x+k)].

The limit exists by integral comparison. Direct subtraction gives

    H_r(q):=sum_(k=0)^(r-1)1/(k+q)=psi(r+q)-psi(q),
    psi(x+1)=psi(x)+1/x,
    C(q)=-psi(q)-psi(1-q), 0<q<1.                    (4)

The last equality follows by matching N1-04's absolutely convergent
series and psi(1)=-gamma. Cotangent partial fractions give the reflection
identity

    psi(1-q)-psi(q)=pi cot(pi q).                    (5)

For example subtract the two defining series in (4); the resulting
sum1/q+sum_(k>=1)[1/(q+k)+1/(q-k)] is exactly that partial fraction.

We will need the real-shift version of the elementary harmonic error:

    0<=log x-1/(2x)-psi(x)<=1/(8x^2), x>0.          (6)

To prove it, apply the trapezoid error identity for f(u)=1/u on each
unit interval[x+k,x+k+1]. Convexity gives a nonnegative error, bounded
by(1/8)integral f'' because the integral-remainder kernel is at most1/8.
Sum all intervals and let their number tend to infinity. The integral
and two half-endpoint terms give exactly the middle expression in (6),
while(1/8)integral_x^infty f''=1/(8x^2).

For r>=64 and0<=q<=1, (6) and elementary logarithm expansion imply

    psi(r+q)=log r+(q-1/2)/r+epsilon_(r,q),
    |epsilon_(r,q)|<=5/(8r^2).                    (7)

Indeed log(1+q/r)-q/r lies between-q^2/(2r^2) and0;
-1/[2(r+q)]+1/(2r) lies between0 and q/(2r^2); and the remainder
in (6) lies between-1/(8r^2) and0. Thus their sum lies between
-5/(8r^2) and1/(2r^2), proving (7).

## 2. Exact finite-row convolution and constant cancellation

First work in the open phase triangle, so every small shifted parameter
below is positive. For b in{beta,-beta}, write s=b/pi, x=alpha/pi,

    q_-=(1+s-x)/2, q_+=(1+s+x)/2.

N1-07's exact finite profile, after factoring its rational denominator,
is

    ell_r(alpha,b)=sin b/[pi(r+s)]
       +(2a/pi^2)[H_r(q_-)+H_r(q_+)]/(r+s).         (8)

To verify the factor, the two partial fractions of each
8a/[w^2-(j*pi+alpha)^2] produce the odd denominators
(2k+1)pi+b-alpha and(2k+1)pi+b+alpha, k=0,...,r-1.
Equivalently, since q_-+q_+=1+s,

    [H_r(q_-)+H_r(q_+)]/(r+s)
          =sum_(k+l=r-1)1/[(k+q_-)(l+q_+)].        (9)

There is also an exact cancellation in the constant numerator of (8):

    sin b/pi-(2a/pi^2)[psi(q_-)+psi(q_+)]=D0.       (10)

For b=beta the parameters are q_-=1-t_d,q_+=t_e. The difference
between the left side and D0=a[C(t_d)+C(t_e)]/pi^2 equals

    sin beta/pi+(a/pi)[cot(pi*t_e)-cot(pi*t_d)]=0,

because sin(pi*t_e)sin(pi*t_d)=a and
cot(pi*t_e)-cot(pi*t_d)=-sin beta/a. Formula (5) supplies the
preceding subtraction. For b=-beta the two small parameters are
1-t_e,t_d, and the same computation with the opposite sign proves
(10). This cancellation is why no uncancelled linear cutoff tail remains.

Consequently the exact row formula also reads

    ell_r(alpha,b)=[D0+(2a/pi^2)
                   (psi(r+q_-)+psi(r+q_+))]/(r+s). (11)

Every equality initially used positive small parameters only. At closed
boundary phases N1-07 defines ell_r by its continuous finite sinc chart.
The right side of (11) has only large arguments r+q and the continuous
coefficient D0, so it extends there directly for r>=64. No unweighted
divergent psi value is assigned at q=0.

## 3. Identify the limit exactly

For fixed p,q>0, consider the triangular sum

    T_R(p,q)=sum_(k,l>=0,k+l<=R-1)1/[(k+p)(l+q)].

The square sum H_R(p)H_R(q) has the expansion

    log^2 R-[psi(p)+psi(q)]log R+psi(p)psi(q)+o(1).

The difference between that square and T_R tends to pi^2/6. Here is
an endpoint-aware justification of this elementary two-dimensional
Riemann limit. In the complementary upper triangle, on k/R,l/R>=eta,
ordinary Riemann sums converge to1/(uv) integrated over
0<u,v<1,u+v>1. The portion k/R<eta has only at most k+2 allowable
l values, each with l>=R(1-eta)-2. For fixed p,q, its sum is bounded
by a constant times

    (1/R)sum_(k<=eta*R)(k+2)/(k+p).

Its limit superior is O(eta); the logarithmic residual divided by R
tends to zero. The other thin side is identical. Thus the improper
Riemann limit holds, and its integral is

    integral_0^1 [-log(1-u)]/u du=sum_(j>=1)1/j^2=pi^2/6.

Termwise integration uses nonnegative terms. The last sum follows
from the same cotangent partial fraction at zero and cot z=1/z-z/3+O(z^3).
Changing the triangle cutoff by one layer costs O(log R/R) for fixed
p,q and therefore does not affect this limit. We have proved

    T_R(p,q)=log^2 R-[psi(p)+psi(q)]log R
                           +psi(p)psi(q)-pi^2/6+o(1). (12)

Use (9),(12) for the two orientations in C_R. The remaining signed
sine sum, together with ell_0, tends to

    sin beta/beta+(sin beta/pi)sum_(r>=1)
                         [1/(r+t)-1/(r-t)]=cos beta,          (13)

by (4),(5). The unequal last row changes this limit by a term tending
to zero. N1-06's definitions give
h_R(t)=-psi(R+t)=-log R+o(1),
g_R(t)=-(1/2)log^2 R+o(1). Its explicit centered-cell tail proves
the latter assertion directly. Therefore (12),(13) yield

    lim E_R=cos beta+(2a/pi^2)
       [psi(1-t_d)psi(t_e)+psi(1-t_e)psi(t_d)-pi^2/3]. (14)

Write the two psi values at each complementary pair in terms of their
sum-C(t) and difference pi cot(pi*t). Then

    psi(1-t_d)psi(t_e)+psi(1-t_e)psi(t_d)
        =[C(t_d)C(t_e)-pi^2 cot(pi*t_d)cot(pi*t_e)]/2.

Also a cot(pi*t_d)cot(pi*t_e)
=sin((alpha-beta)/2)sin((alpha+beta)/2)
=(cos beta-cos alpha)/2. Substituting in (14) gives exactly
E_infty=a/3+a C(t_d)C(t_e)/pi^2, as in (1).

This identifies the limit pointwise in the open triangle. Uniformity
up to every boundary will follow from the explicit tail in the next step;
no uniform improper-sum limit has been presumed here.

## 4. Pair the two cutoff increments before summing

N1-06's convergent series give exactly

    h_R(t)-h_(R+1)(t)=1/(R+t),
    g_R(t)-g_(R+1)(t)=log(R+t)/(R+t).

Increasing R in C_R adds ell_R(alpha,beta)+ell_(R+1)(alpha,-beta).
Using (11) and the just displayed recurrences gives

    E_(R+1)-E_R=(2a/pi^2)[J_R(t)+J_(R+1)(-t)],       (15)
    J_r(s)=[psi(r+(1+s-x)/2)+psi(r+(1+s+x)/2)
                                     -2log(r+s)]/(r+s).

All shifted parameters in the psi terms lie in[0,1] after subtracting r.
By (7), their sum is2log r+s/r plus an error at most5/(4r^2).
For |s|<=1,

    |log(r+s)-log r-s/r|<=1/[2r^2(1-1/r)].

Thus the numerator of J_r(s) is-s/r plus an error at most
(5/4+64/63)/r^2<23/(10r^2). Division by r+s>=r-1 yields

    J_r(s)=-s/[r(r+s)]+e_r(s), |e_r(s)|<5/(2r^3). (16)

The two leading terms in (16) cancel to

    -t/[R(R+t)]+t/[(R+1)(R+1-t)]
       =-t(1-t)(2R+1)/[R(R+t)(R+1)(R+1-t)],        (17)

whose magnitude is less than1/R^3 for R>=64. The two remainders
cost less than5/R^3. Since2a/pi^2<2/9, (15)–(17) give uniformly

    |E_(R+1)-E_R|<2/R^3.

The summed tail is less than
integral_(R-1)^infty 2u^(-3)du=1/(R-1)^2. Thus E_R converges
uniformly on the closed phase triangle and obeys (2). Its limit equals
(14) on the open triangle. The functions cos(theta/2)C(1/2+theta/(2pi))
have finite continuous limits pi at theta=+/-pi by C08-far-01, so
E_infty has the stated continuous extension. Density and uniform
convergence identify the same limit on all edges and vertices. This
also verifies that no phase collision or w=0 endpoint is lost.

## 5. A uniform upper below two

Let C0=C(1/2)=2gamma+4log2. The elementary constants already proved
in N1-16 and C06 satisfy7/2<C0<4. For the upper, gamma<3/5 and
log2<7/10 suffice; exp(7/10)>2 follows from its positive series
through degree4. For the lower, gamma>23/40 and log2>69/100 suffice.

C08-far-01 implies for |theta|<=pi

    cos(theta/2) C(1/2+theta/(2pi))
       <=C0 cos(theta/2)+(7/2)(1-cos(theta/2))<=C0.

The factors here are positive: C is positive by its symmetric series,
and the boundary factors tend to pi. Therefore

    E_infty<=1/3+C0^2/pi^2
                  <1/3+320/197=1157/591<49/25,

using pi^2>197/20. This proves (3). At R=64,
1/(R-1)^2=1/3969<1/3000, giving the stated finite-cutoff bound.

## Scope, verification and history

This theorem retains the exact R64 endpoint family used by C06; the
limit is an analytic bounding device, not a replacement model or a new
correction. The integral contribution
B0 log^2(delta/pi)+2D0 log(delta/pi)+(1/pi)integral B remains separate.
An upper bound53/100 for that quantity would combine with this theorem
to give C_far<5/2, but no such upper is assumed or established here.

No computational proof or numerical execution was used. The elementary
cutoff limit is identified pointwise first, then extended uniformly by a
separately proved paired tail. Independent review must reconstruct the
sine/reflection cancellation, triangular complement constant and tail
normalization before this helper is used as an accepted premise.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.
