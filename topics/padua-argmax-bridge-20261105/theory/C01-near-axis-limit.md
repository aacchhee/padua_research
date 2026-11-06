# PD-T?argmax-bridge-codex-C01-near-02 — The unchanged residual has a positive fractional axis term

ID kind: PD-T. Aliases: actual limiting residual axis coefficient;
coalescing-root alpha^(3/2) term. Split from: N1-19's OPEN residual modulus.
Split into: the consequence for quadratic/entropy-only trial bounds is the
separate scoped negative record C01-near-quadratic-obstruction.md.

## Statement and status

Overall status: **PROVED**, analytic developer result. Independent review is
separate. Let Q_n be exactly N1-18's origin-normalized continuous increment,
and retain all N1-15 fixed choices R=128, delta=1/1000, J=4096. For every
fixed 0<=alpha<=1/2 the limit

    q_infinity(alpha)=lim_(integer n->infinity) Q_n(alpha,0)

exists. It has the exact small-phase asymptotic

    lim_(alpha down to 0) q_infinity(alpha)/alpha^(3/2)
          =kappa,  kappa=(4/pi²) integral_0^1 sqrt(1-y^4)dy>0.   (1)

In particular 8/25<kappa<18/49. This is a limit of the already specified
residual, not a new model, correction or approximation for finite n.
No quantitative rate in n or in (1) is asserted. The complete Q_n-G_n target
remains OPEN, and this positive fractional term does not contradict it.

## Dependencies

N1-07 finite endpoint-row limits; N1-10/11/15 exact fixed model;
N1-13's bounded second derivative of Phi0 on open periods and finite derivative
jump at integers; N1-14's exact cancellation formulas; N1-16's exact two
coefficients; N1-18's |F_n-Q_n|<9/(2n); and the positive integral in
C01-near-central-upper.md. The formulas used from those records are restated
where needed. Exact real arithmetic only; no computation, fit or source theorem.

## Proof

### 1. Take the degree limit in the existing residual

Restrict beta=0 and abbreviate

    a=(1+cos alpha)/2, B0=4a/pi²,
    D0=U0/pi+B0*log pi, k=log(delta/pi),
    Hstar=h_R^[4096](0)+h_R^[4096](1),
    Gstar=g_R^[4096](0)+g_R^[4096](1).

The starred quantities are exactly the fixed truncated series already used
by M_strip; they are not replaced by their infinite versions. Write
R_n=M_near-B0*(log n)²-b_M*log n. Its limit is

    r_infinity(alpha)=C_R(alpha,0)
        +D0*(2k+Hstar)+B0*(k²+Gstar)
        +(1/pi) integral_delta^pi [B(v_L(z))+B(v_R(z))]dz.       (2)

Here C_R is precisely N1-07's finite endpoint profile and B is N1-05's
constant profile. To verify (2), the exact finite-h endpoint rows tend to
C_R by N1-07's explicit error. The at most four remaining special rows are
O((1+log n)/n) after normalization, as bounded in N1-16. The two filled outer
intervals tend to [delta,pi]; any original collision holes have total length
O(1/n), and N1-14 gives an integrable central logarithm, so their B integrals
vanish. Their A integrals differ from the limiting integrals by O(1/n),
which remains negligible after multiplication by log n.

In each strip log b_s=log n+k+O(1/n) and Z_n=D0+O(1/n). Expanding its
two singular primitives gives exactly the constant terms in (2).
The regular strip coefficient contributes only to b_M: its finite endpoint
errors times log n tend to zero. At beta=0, the q_s log z terms vanish and
the U_L/U_R terms cancel in the limit. In M_jump the A2 terms vanish
identically and the others are O((1+log n)/n). Thus every term in the exact
model has been included, and N1-16's exact b_M cancels the remaining log n
coefficient. N1-18 then implies

    q_infinity(alpha)=r_infinity(alpha)-r_infinity(0).         (3)

### 2. All noncentral-cancellation terms in (2) have quadratic increments

The finite profile is

    C_R(alpha,0)=1+sum_(r=1)^(R-1) ell_r(alpha,0)
                         +sum_(r=1)^R ell_r(alpha,0),
    ell_r(alpha,0)=8a sum_(j=-r+1,-r+3,...,r-1)
                         1/[(r*pi)²-(j*pi+alpha)²].

Every denominator is separated from zero near alpha=0; pairing j with -j
shows this finite function is smooth and even there. It therefore changes
by O(alpha²). U0, D0 and B0 are likewise smooth and even, by the reciprocal
pair series in N1-16. The starred constants do not depend on alpha.

It remains to justify this statement for the regularized pole numerator
inside the B integral, since Phi0 has an integer derivative jump. On beta=0
both folded numerators agree and, by periodicity and reflection, their sum
is a smooth even weight times

    Phi0(x+t)+Phi0(x-t),
    x=(pi-z)/(2pi), t=alpha/(2pi).

The z-dependent denominator 2sin(z/2) is uniformly positive on [delta,pi].
N1-13 proves that Phi0 is Lipschitz and its first derivative has finite
variation on a period. If f' has finite variation V on the relevant bounded
interval, the elementary second-difference estimate is

    integral |f(x+t)+f(x-t)-2f(x)| dx <=V*t².                  (4)

For completeness, write the difference as
integral_0^t [f'(x+s)-f'(x-s)]ds; integration in x bounds the inner
L1 translation difference by 2sV, and integration in s gives (4).
One may enlarge the integration interval to include both translates and
take V over finitely many periods. Multiplication by the bounded positive
denominator weight preserves the O(t²) bound. The extra cos(alpha/2) weight
also changes by O(alpha²). Hence the entire pole-numerator integral has a
quadratic increment despite the moving integer cusp.

On delta<=z<=pi/2, the exact cancellation integral sum is
4a cot(z/2)log(sin z), so its increment is O(alpha²). Thus the only possible
term of order alpha^(3/2) in (2)--(3) comes from the whole central cancellation
integral Ic of C01-near-central-upper.md.

### 3. Scale the exact moving-root correction

On beta=0 put u=sin(alpha)/2, tau=u/a=tan(alpha/2),
s=a tan(e/2). Both folded integrals equal J(u,s,e). Let

    E(u,s,e)=J(u,s,e)-2s log(sin e).

The central baseline has a quadratic increment because it is a times its
origin value. For 0<e<2alpha, the same-sign entropy bound |J|<=2u log2
when e<=alpha, and the positive majorant H when alpha<e<2alpha, show

    integral_0^(2alpha) |E|de=O(alpha²[1+log(1/alpha)]).

For the first interval also use s<=a tan(alpha/2)=u and the integrable
bound -log(sin e)<=log(pi/(2e)); on the second use
H<=2u log(2/e). This contribution divided by alpha^(3/2) tends to zero.

For e>=2alpha, s>u and E=H. Set e=sqrt(alpha)*y. On its nonzero support,
the exact formula from C01-near-central-upper (10) is

    E/alpha=(2u/alpha) integral_x^1
              sqrt(1-z²)/[z sqrt(1-lambda² z²)] dz,
    x=(1-cos e)/tau, lambda=tau/tan(e/2).

For fixed y>0, x tends to y², lambda tends to zero, and 2u/alpha tends
to one. Thus the integrand after scaling tends to

    h(y²), 0<y<1;    0, y>1,
    h(x)=integral_x^1 sqrt(1-z²)/z dz.

Here is a uniform integrable domination, including the shrinking lower end.
For e>=2alpha, lambda<=1/2. Also 1-cos e>=2e²/pi² and
tau<=8alpha/15, so x>=y²/3. Nonzero support therefore has y<sqrt(3),
and h(x)<=log(2/x)<=log(6/y²). Since 2u/alpha<=1, the scaled expression
is bounded by (2/sqrt(3))*log(6/y²) on (0,sqrt(3)), extended by zero
elsewhere. This is integrable at zero. Dominated convergence now gives

    lim alpha^(-3/2) integral_0^(pi/2) E de
                               =integral_0^1 h(y²)dy=2 I4.

The last identity follows by integration by parts, using
d[h(y²)]/dy=-2sqrt(1-y^4)/y; its boundary products vanish.
There are two folded copies and the normalization is 1/pi². Therefore
the central contribution has coefficient 4I4/pi². Section 2 shows that
every other contribution is o(alpha^(3/2)), proving (1).

Finally 1-y^4<=sqrt(1-y^4)<1-y^4/2 for 0<y<1 gives
4/5<I4<9/10. Together with pi²<10 and pi²>49/5 these imply the stated
strict rational bounds 8/25<kappa<18/49.

## Scope, checks and history

This proves a positive fractional term for the actual limiting residual of
the unchanged model, not merely for the root-band geometry. It supplies no
uniform n-rate, no finite-n upper constant for the remaining components and
no effective comparison onset. The limits are ordered: n tends to infinity
at each fixed alpha, and alpha then tends to zero. No interchange is used.
No numerical integral or program was run. 2026-11-06, input/rules
4b728b04216a5490910780bc609a82b853058426; Codex, parent-assigned Astra ultra,
serving metadata unexposed. The original full target remains N1-19 OPEN.

