# PD-T?argmax-bridge-codex-D08-box — Actual vertex values with common phase-interpolation remainders

ID kind: PD-T. Aliases: signed-dual Peano phase box; even squared-phase
corner box; point-to-box enclosure. Split from: the D08 point-to-box
target. Split into: independent global norm in D08-point-box-norm.md;
origin-loss application in D08-point-box-corner.md.

## Statement

Fix n>=2, m=n+1 and kappa=n/m. Use exactly the corrected finite G_n,
odd-board S_n and actual Padua cardinals of D08-point-box-norm.md and
PD-T101/364. Let proved constants M_S,M_lambda satisfy

    S_n(alpha,beta)<=M_S for ALL real alpha,beta,
    lambda_n(x,y)<=M_lambda for ALL (x,y) in [-1,1]^2. (1)

One may unconditionally take M_S=M_lambda=sqrt(2n(n+1)) by the split
norm theorem; also any valid M_S is a valid M_lambda. No sampled maximum
or unproved argmax value is an allowed substitution in (1).

For any finite closed real rectangle B=[a,b] times[c,d], write I_B h
for bilinear interpolation of its four vertex values, with positive
weights summing to one. Zero-width intervals use the identity in that
coordinate. Then at every (alpha,beta) in B,

    S_n(alpha,beta)<=I_B S_n(alpha,beta)
       +(M_S/2)[(alpha-a)(b-alpha)
                     +kappa^2*(beta-c)(d-beta)],       (2)

and hence

    sup_B S_n<=max_(vertices B) S_n
                    +(M_S/8)[(b-a)^2+kappa^2*(d-c)^2]. (3)

For the actual nonnode-corner chart define

    Lambda(alpha,beta)=lambda_n(-cos(alpha/n),-cos(beta/m)).

Let 0<=a<=b and 0<=c<=d be finite. Set

    u=alpha^2/2, v=beta^2/2,
    A=a^2/2, B0=b^2/2, C=c^2/2, D=d^2/2,
    H(u,v)=Lambda(sqrt(2u),sqrt(2v)).

With I_sq denoting positive bilinear interpolation of the four ACTUAL
Lambda vertex values in coordinates (u,v),

    Lambda(alpha,beta)<=I_sq Lambda(alpha,beta)
       +(M_lambda/6)[(u-A)(B0-u)
                              +kappa^4*(v-C)(D-v)],   (4)

and consequently

    sup_[a,b]x[c,d] Lambda<=max_(four vertices) Lambda
       +(M_lambda/96)[(b^2-a^2)^2+kappa^4*(d^2-c^2)^2]. (5)

The same assertions hold at the other parity-correct nonnode corner by
the accepted node-preserving reflection. They include both phase axes,
the origin, collisions, zero cardinals and zero-width rectangles.

The squared chart in (4)-(5) applies to the smooth even signed cardinal
polynomials, not to S_n. Neither S_n nor Lambda is assumed C^2. No
individual cardinal sign stays fixed, and no factor counting cardinals
or board points occurs in these bounds.

Status: **PROVED**, analytic developer enclosure theorem; distinct review
pending. Source adoption, a complete cover and practical cost remain OPEN.

## 1. Finite proof of the Bernstein bound used here

For a real or complex trigonometric polynomial T of integer degree at
most q>=1, put

    t_k=(2k-1)*pi/(2q),
    c_k=(-1)^(k-1)/[4q*sin^2(t_k/2)], 1<=k<=2q.

The finite Riesz differentiation identity is

    T'(x)=sum_(k=1)^(2q) c_k*T(x+t_k),
    sum_k |c_k|=q.                                   (6)

Here is a basis verification including both endpoint frequencies. On
the 2q half-shifted roots, finite Fourier orthogonality first gives

    c_k=(1/(2q))*sum_(ell=-q+1)^q i*ell*exp(-i*ell*t_k).

Indeed insertion into sum_k c_k exp(i*p*t_k) gives i*p for every
integer -q+1<=p<=q. With r=exp(-i*t_k), r^(2q)=-1. Differentiate
the finite geometric sum

    sum_(ell=-q+1)^q r^ell=r^(1-q)*(1-r^(2q))/(1-r)

BEFORE substituting r^(2q)=-1. It gives

    sum_(ell=-q+1)^q ell*r^ell=2r^(1-q)/(1-r)^2.

Thus c_k=i*z^(q+1)/[q*(z-1)^2], z=exp(i*t_k). Using
z^q=i*(-1)^(k-1) and (z-1)^2=-4z*sin^2(t_k/2) gives the real
coefficient in (6). The missing basis frequency p=-q is also exact:
exp(-iq*t_k)=-exp(iq*t_k), so its multiplier is -iq, as required.
Linearity proves the identity for every T of degree at most q.

The finite sine-product identity, obtained by factoring the roots of
unity in exp(2ix), implies after two logarithmic differentiations

    sum_(k=0)^(p-1) csc^2(x+k*pi/p)=p^2*csc^2(px).

Take p=2q and x=pi/(4q). Then the sum is 4q^2, proving the second
identity of (6). This is the same finite product calculation used in
PD-T227, and supplies an elementary proof rather than an imported norm
theorem. Taking absolute values in (6) and iterating on derivatives gives

    ||T^(r)||_infinity<=q^r*||T||_infinity.            (7)

If the frequencies are ell/s, |ell|<=q, rescaling the variable gives
(q/s)^r in place of q^r. The supremum is over the whole real line;
a merely local point bound cannot be used in this argument.

## 2. Signed families control the aggregate derivative norm

Let f=(f_1,...,f_J) be a finite real vector function with

    ||f(alpha,beta)||_1=sum_i|f_i(alpha,beta)|<=M

for all real phases, and suppose each component has alpha frequencies
ell/n and beta frequencies ell/m, |ell|<=n. For every constant sign
vector epsilon, the signed polynomial p_epsilon=sum_i epsilon_i f_i
satisfies |p_epsilon|<=M globally. Applying (7), and at each target
point choosing signs of its derivative components, proves

    ||partial_alpha^r f||_1<=M,
    ||partial_beta^r f||_1<=kappa^r*M,                (8)

pointwise for every r>=0. One can equivalently apply the finite operator
(6) directly in the l1 norm. The signs may vary with the derivative
evaluation point: no one sign vector is asserted to work everywhere.
Equation (8) is not the sum of individual component supremum bounds.
It avoids a factor J because one signed combination is bounded by M.

For S_n take one component for each odd-board point,

    f_jr(alpha,beta)=G_n((j*pi+alpha)/n,(r*pi+beta)/m)/(2nm).

Then ||f||_1=S_n exactly, including all finite polynomial collisions.
The total-degree G_n has coordinate degrees at most n, so the stated
frequency bounds hold, with the exceptional mode retained. Assumption
(1) therefore supplies (8) with M=M_S.

For the actual corner take the components

    f_i(alpha,beta)=L_i(-cos(alpha/n),-cos(beta/m)).    (9)

They have the same frequency bounds because each corrected cardinal
has polynomial degree at most n in each coordinate. For all real
alpha,beta the physical arguments stay in the square, so their l1
norm is globally bounded by M_lambda. Every component of (9) is even
separately in alpha and beta. These are statements about the smooth
signed polynomials before taking their absolute values.

## 3. A common Peano kernel, with no component-count multiplier

For a C^2 vector function on [a,b] and x in that interval, positive
linear interpolation I_x satisfies

    f(x)-I_x f(x)=-integral_a^b K_x(t) f''(t)dt,
    K_x(t)=(b-x)(t-a)/(b-a) for t<=x,
           (x-a)(b-t)/(b-a) for t>=x,
    integral K_x=(x-a)(b-x)/2.                       (10)

Two integrations of f'' give (10), or one checks the endpoint Green
function directly. Its kernel is nonnegative and is COMMON to all
components. Therefore a pointwise bound ||f''||_1<=E gives
||f-I_x f||_1<=E*(x-a)(b-x)/2. Summing separate component suprema
is neither necessary nor the estimate used here.

On a rectangle, write I_x,I_y for the two positive interpolation
operators. The exact identity

    f-I_x I_y f=(f-I_x f)+I_x(f-I_y f)

and their nonnegative weights prove, if ||f_xx||_1<=E_x and
||f_yy||_1<=E_y throughout that rectangle,

    ||f(x,y)||_1<=I_x I_y(||f||_1)(x,y)
        +E_x*(x-a)(b-x)/2+E_y*(y-c)(d-y)/2.           (11)

The interpolated norm on the right is bounded by its largest vertex
value. Each product is at most the squared interval width divided by
four. Applying (8) with r=2 to the primitive vector proves (2)-(3).
The proof never differentiates S_n. Degenerate intervals follow by
continuity, with interpolation the identity and zero remainder there.

## 4. The even squared-phase chart and its origin limit

Use the actual-cardinal vector (9) and set h(u,v)=f(sqrt(2u),sqrt(2v)).
Each component is analytic in u,v at their axes: cos(sqrt(2u)/n) has
its convergent even power series in sqrt(2u), and the cardinal is a
finite polynomial. Thus no singular derivative is assigned at u=0.

For alpha>0, keeping beta fixed, direct differentiation gives

    h_uu=[alpha*f_alphaalpha-f_alpha]/alpha^3.

Evenness gives f_alpha(0,beta)=f_alphaalphaalpha(0,beta)=0. Hence,
component by component but with the SAME integral kernel,

    h_uu=(1/alpha^3)*integral_0^alpha t
                         *integral_0^t f_alphaalphaalphaalpha(s,beta)ds dt.
                                                               (12)

Its nonnegative kernel has mass 1/3, since
alpha^(-3)*integral_0^alpha t^2 dt=1/3. Equation (8) with r=4 and
the l1 integral triangle inequality give

    ||h_uu||_1<=M_lambda/3,
    ||h_vv||_1<=kappa^4*M_lambda/3.                 (13)

For clarity, after substituting t=alpha*r,s=alpha*z, (12) is
integral_0^1 r*integral_0^r f_alphaalphaalphaalpha(alpha*z,beta)dz dr.
At alpha=0 its continuous value is f_alphaalphaalphaalpha(0,beta)/3.
This proves the same bound at the origin, with no division by alpha.
The beta argument is identical and retains its kappa^4 factor.

Apply (11) to h in coordinates u,v using (13). Since ||h||_1 is
exactly the actual Lambda, this gives (4). The u-width is (b^2-a^2)/2
and the v-width is (d^2-c^2)/2. Taking the largest vertex and maximum
Peano product gives M_lambda/(3*8*4)=M_lambda/96, proving (5).
This includes both closed axes and the doubly zero origin. Zero cardinal
values remain in the l1 norm throughout.

The node-preserving x reflection for even n, or y reflection for odd n,
permutes the accepted cardinals and maps the canonical nonnode corner
to the other one. It does not exchange n and m. It therefore transfers
the same actual chart values and the inequalities just proved.

## Scope and evaluation obligations

Full outward upper bounds at the four vertices may replace their exact
values in (2)-(5), retaining the positive weights. The GLOBAL M must
also be enclosed upward. If coordinates are given in units of pi, all
widths and squared widths in these formulas are still in radians; the
corresponding pi^2 or pi^4 factors must be enclosed. The actual D07
point API uses inward turns alpha/(n*pi), beta/(m*pi), not alpha/pi
and beta/pi. Its literal degree/input/failure guards remain unchanged.

These mathematical rectangles may meet or cross a fundamental-domain
edge because (1) is global. A source restricted to an older triangular
API is not automatically extended by this theorem. For corner boxes
crossing phase axes, one may split/use separate evenness before a
nonnegative squared chart; no unproved squared-coordinate smoothness
of S_n is used. PD-N079/085/086 remain intact.

This result supplies value enclosures only. It is not the old energy
radius, maximum-exclusion predicate or a completed equality-set proof.
The point-dependent origin application has its own explicit sufficient
conditions in D08-point-box-corner.md. No four point calls, native run,
quadrature, cover, source adoption, degree extension, runtime bound or
effective global onset is asserted here.

## Verification and provenance

Analytic finite Fourier, signed-family and integral algebra only. The
Riesz identity includes both endpoint frequencies; the Peano kernel is
common to every component; the squared-origin factor is explicitly 1/3.
No numerical/code job or imported external theorem is a premise.

Rules/input `d4956aea3bda9d5ff9917a5b410778fc7adf4fb7`, 2026-11-06.
Parent-assigned ordinary Sol xhigh analytical cap, serving metadata
unexposed. Fresh prospective gate is in the owned D08 idea/attempt.
Root alone owns Git/shared records. Developer-PROVED, distinct review
pending; all earlier source and proof files remain unchanged.


### Supplementary review closure — 2026-11-06

Distinct Astra xhigh reconstruction ACCEPTED the preceding unchanged
developer text, with no unresolved finding. See
[independent-checks-D09-point-box.md](../independent-checks-D09-point-box.md),
report SHA256486f58f8a7d460134922c26c02889e1eca69f482359ed66d7618b34d8b43535a.
This closes the pending supplementary mathematical review only; successful
point premises, source adoption, complete covers and final Claude audit
remain separate obligations. No numerical instance ran for this proof.
