# PD-T?argmax-bridge-codex-D13-endpoint — Origin-cancelled fixed endpoint reference

ID kind: PD-T. Aliases: relative displaced digamma defect; finite endpoint
reference increment; D05 endpoint completion.
Split from: D13 full finite relative remainder, OPEN.
Split into: none. This is a supporting theorem, not the full target.

## Statement and definitions

Let n>=32 be an integer, m=n+1, H_n=sum_(k=1)^n 1/k, and

    alpha,beta>=0, rho=alpha+beta<=1/2,
    a=(cos alpha+cos beta)/2, x=alpha/pi, t=beta/pi,
    J=floor(n/2), J_L={2,...,J}, J_R={3,...,J}.

On the left use s=t and physical row r=j; on the right use s=-t and
physical row r=2m-j. These are exactly D05-relative-halfline's fixed
endpoint labels for R=2. In each row retain the actual corrected odd-board
mesh of D04-reference-matching and its symmetric cancellation quadrature
T0_j. Explicitly it uses the reference (-w,w), w=a cot(z/2)/2,
z=pi(j+s)/m, and the two actual offsets

    theta_+/-=(1-s+/-x)/2+(j+s)/(2m).

The polynomial underlying that reference is G_n=D_n-cos(nu); no
uncorrected whole kernel or off-grid rational collision value replaces it.
All selected offsets are strictly between0 and1, as proved in D05.
Thus no selected reference sample is a pole, including on either axis.

Define the unchanged exact endpoint constant

    nu=j+s, y_+/-=j+(1+s+/-x)/2,
    B_j=psi(y_+)+psi(y_-)-2log nu,
    Xi_j(s)=(2a/pi^2) B_j/nu,
    Delta_2=sum_(j=2)^infinity Xi_j(t)
                    +sum_(j=3)^infinity Xi_j(-t),
    Q_ep(phi)=(nm)^-1 sum_(j in J_L,J_R) T0_j(phi)-Delta_2(phi).

Every sum over J_L,J_R counts the two sides separately. The series is
the original D04 E_infty-E_2, not an added model correction. Then

    |Q_ep(phi)-a Q_ep(0)| <= a rho(2H_n+10)/n.             (1)

The same statement holds sectorwise on |alpha|+|beta|<=1/2 by evaluating
these folded objects at absolute phases. Both parities use their actual
J=floor(n/2) without exchanging n and m.

Overall status: **PROVED**, analytic developer result; distinct review
is required. The full S_n-M_infty relative remainder remains **OPEN**.

## Dependencies and exact distinction

D04-reference-matching gives Xi, Delta_2 and the displaced digamma
expression. D05-relative-halfline, equation(7), bounds only the relative
T0-Theta residual on these fixed labels by2a rho H_n/n. The new step
below controls the relative Theta/(nm)-Xi defect by8a rho/n and the
relative omitted Xi tails by2a rho/n. In particular D05's old bound is
a dependency, not the result relabeled.

No external source theorem or numerical premise is used. The positive
digamma derivative series follows by differentiating the defining
convergent harmonic finite part on compact positive intervals.

## Proof

### 1. Subtract the origin before bounding the finite displacement

Set c=2/pi^2 and, for each selected j,

    delta=nu/(2m), u=pi nu/(2m), tau=u cot u,
    U=psi(y_+-delta)-psi(y_+)
                      +psi(y_--delta)-psi(y_-)-2log(n/m),
    e_j(x,s)=c[(tau-1)B_j/nu+tau U/nu].               (2)

All offsets are unwrapped on the stated domain. D04's exact formula is

    Theta_j/(nm)=a cot(z/2)/(pi m) [B_j+U],
    Theta_j/(nm)-Xi_j=a e_j(x,s).                    (3)

Consequently the desired relative error in(3) is exactly
a[e_j(x,s)-e_j(0,0)]. This cancels its origin value algebraically;
there is no subtraction of two absolute D04 allowances.

Since x+|s|<=1/(2pi)<1/6 and j>=2,

    11j/12 <=nu<=13j/12, 0<u<pi/4,
    y_+/- >= j+5/12, y_+/- -delta >= j.

For the last inequality, j<=J implies nu<m/2 and delta<1/4.
The same inequalities hold along the straight phase path from0 to(x,s).
For y>=j>=2 the positive derivative series and integral comparison give

    0<psi'(y)<=1/j+1/j^2<=3/(2j),
    |psi''(y)|<=1/j^2+2/j^3<=2/j^2.                (4)

D04's elementary bound is |B_j|<=2/nu. Differentiating B_j and using(4)
gives

    |partial_x B_j|<=3/(2j), |partial_s B_j|<=4/j.

Let a dot denote derivative along lambda ->(lambda x,lambda s), and
write b=x+|s|. Then |dot B_j|<=4b/j. D04's displacement estimate also
gives |U|<=5/n. For clarity the derivative of U is estimated BEFORE
discarding its two differences: each
psi'(y-delta)-psi'(y) is at most2delta/j^2 in magnitude. Thus

    |partial_x U|<=2delta/j^2<2/(mj),
    |partial_s U|<=2delta/j^2+3/(2mj)<3/(mj),
    |dot U|<=3b/(mj).                               (5)

The constant -2log(n/m) has zero phase derivative. Dropping it before
the exact subtraction would be unnecessary and is not done here.

### 2. Uniform elementary prefactor derivatives

For0<u<=pi/4, 0<=1-tau<=u^2. Also

    |tau'(u)|=(u-sin u cos u)/sin^2 u<=2u.

Indeed the numerator is integral_0^u 2sin^2 v dv<=2u^3/3 and
sin u>=2u/pi; pi^2<12 gives the displayed inequality. Put
f(nu)=(tau-1)/nu and g(nu)=tau/nu. Using pi^2<10 and nu<m/2,

    |f|<=4nu/m^2, |f'|<=12/m^2,
    |g|<=1/nu,    |g'|<=3/nu^2.                    (6)

For example |d tau/d nu|<=pi^2 nu/(2m^2)<5nu/m^2;
then |g'|<=5/m^2+1/nu^2<3/nu^2. The deliberately loose constants
in(6) also cover the limit u=0, although no selected row uses that limit.

Differentiate(2) using dot nu=s and (4)--(6). On the whole phase path,

    |dot e_j| <= c b [24/(m^2 nu)+16nu/(m^2 j)
                                   +15/(n nu^2)+3/(m nu j)]
              <= c b [27/(m^2 j)+18/m^2
                                   +18/(n j^2)+4/(m j^2)].       (7)

The two finite label sets have fewer than m members in total; their
combined harmonic sum is at most2H_n and their combined inverse-square
sum is at most3/2. The latter follows from
sum_(j>=2)j^-2<=1/4+integral_2^infinity y^-2dy=3/4.
Integrating(7) in lambda and summing therefore gives

    sum_(J_L,J_R)|e_j(x,s)-e_j(0,0)|
      <= c b [54H_n/m^2+24/m+27/n]
      <= (2/9)(rho/3)(105/n)<8rho/n.               (8)

Here H_n<=n, m>n, pi>3 were used only for this final simplification.
Multiply by the actual a to obtain the promised finite displaced-
digamma bound8a rho/n. It vanishes at phase zero exactly.

### 3. Keep and compare the actual infinite endpoint tails

The part of Delta_2 absent from the finite Xi sum is exactly

    Tail(phi)=sum_(j=J+1)^infinity [Xi_j(t)+Xi_j(-t)].

No floor depending on phase occurs. Write Xi_j/a=c B_j/nu. The same
digamma estimates, now valid for all j>=2, give on the phase path

    |d/dlambda (Xi_j/a)|
      <=c b [4/(j nu)+2/nu^3] <=6c b/j^2.          (9)

Indeed nu>=11j/12 and j>=2 imply
48/11+1728/1331<6 for the coefficient of j^-2.
The summable uniform bound justifies termwise integration. Consequently

    |Tail(phi)-a Tail(0)|
      <=12a c b sum_(j=J+1)^infinity j^-2
      <=8a rho/(9J)<=2a rho/n.                    (10)

The last inequality uses J>= (n-1)/2 and n>=32; equivalently
16n/[9(n-1)]<=512/279<2. This controls the endpoint series itself;
it does not set a reference value at any polynomial collision.

### 4. Combine with the already proved half-line increment

D05-relative-halfline(7), on exactly J_L,J_R above, states

    (nm)^-1 sum |(T0_j-Theta_j)(phi)
                              -a(T0_j-Theta_j)(0)|<=2a rho H_n/n.

The identity Q_ep=sum(T0/(nm)-Xi)-Tail, together with(8),(10), proves
(1). Axes and phi=0 are literal in all scalar expressions; the no-wrap
proof and uniform bounds include the entire closed near triangle.

## Scope and remaining gaps

This theorem covers only these fixed endpoint rows of the SYMMETRIC
cancellation reference and its full Delta_2 series. It supplies no
relative estimate for the omitted central reference rows, weighted
single-pole approximation, regular outer quadrature or six retained
actual polynomial rows. In particular it is not a new whole-reference,
S-K_fixed or S-M_infty bound, and cannot lower an analytic onset alone.

Polynomial collision values elsewhere are not evaluated or replaced.
No smoothness of moving numerator roots, quadratic primitive modulus,
new model term or second near correction is assumed. All old proofs
remain frozen. The D10 true-constant fractional obstruction is untouched.

## Checks and history

Paper proof only; no scalar, native, board, quadrature, root, fitting or
degree job was executed. Distinct review of the actual finite offsets,
constants and precise excluded terms is the next verification step.
2026-11-06; rules/input e13a538bda80e6cc785f4835937b2ca338bc1d6f;
parent-requested Astra ultra, serving metadata unexposed. Candidate:
../ideas/D13-relative-remainder.md. Parent target:
D13-relative-remainder.md. No shared record or Git mutation by author.


### Supplementary review closure — 2026-11-06

Distinct Astra high mathematical reconstruction ACCEPTED the two support
scopes and the full target's OPEN status, no unresolved findings;
[independent-checks-D13-relative-support.md](../independent-checks-D13-relative-support.md),
report SHA256de9a18a24b1acc2c78ddfe71ab55f665f4145fb3fc3c5474d82f62dde396eaaf.
The display NOTE interprets strict intermediate estimates at positive rho;
at rho=0 the exact subtractions vanish. Final non-strict statements and
audited proof text are unchanged. No numerical jobs or new onset result.
