# PD-T?argmax-bridge-codex-C03-near-01 — A quadratic noncentral remainder with the actual truncation slope

ID kind: PD-T. Aliases: folded periodic second differences; telescoped
endpoint/strip/jump slope; numerical two-phase limiting remainder.
Split from: the sharper quantitative continuation of C02. Split into:
the near-comparison onset is in C03-near-onset.md.

## Statement and scope

Let T be exactly (3) of C02-near-explicit-onset.md, including R=128,
J=4096 and its stipulated finite truncated constants. Let I_c be the whole
central cancellation integral of C01-near-central-upper.md. For
alpha,beta>=0, rho=alpha+beta<=1/2 and r2=alpha²+beta²,

    [T-I_c](alpha,beta)-[T-I_c](0,0)<=25r2+10^-8 beta.       (1)

More precisely, the one-sided beta derivative at the origin exists, is the
number d specified in (9) below, and satisfies |d|<10^-9. Thus the
ordinary linear allowances of C02 cancel down to a small, explicitly
controlled residue of the actual fixed model. No assertion that d is zero
or nonpositive is made. This is a limiting-function bound, not a finite-n
cusp estimate and not the full n>=10^6 comparison.

**PROVED**, analytic developer helper. No numerical computation, fit,
quadrature or external theorem is a premise. Independent supplementary
review and formal Claude audit are separate. The prescribed continuation,
prospective bound and retained alternatives are in ../ideas/C03-near.md.
All previous frozen C01/C02 sources are unchanged.

Use all symbols from C02. In particular C0=2gamma+4log 2, and N1-16's
reciprocal-pair identity gives

    D=C(1/2+(alpha-beta)/(2pi))+C(1/2+(alpha+beta)/(2pi))-2C0>=0,
    D0=a(2C0+D)/pi².                                  (2)

The bounds 0<C0<4, |k| in (7,9), |h_J|<5, |g_J|<13 will be used.
Here gamma<3/5 follows directly from PD-T270's harmonic remainder at
m=10: H_10<2.93, log 10>2.3 and |r_10|<=1/800 give gamma<.582.
Together with log 2<7/10 this proves C0<4. The logarithm comparisons
follow from elementary positive exponential series. For h_J and g_J,
their original initial terms have magnitude below 4.9 and 4.9²/2,
since log(129)<4.9. The centered-cell corrections used in C02 have
total magnitude below 1/100. This proves the stated relaxed bounds.

## 1. Coupled periodic pole terms, with the integer cusp retained

Set x=(pi-z)/(2pi), t_-=(alpha-beta)/(2pi),
t_+=(alpha+beta)/(2pi), c_e=cos(pi t_+), c_d=cos(pi t_-).
Periodicity and reflection of Phi=Phi_0 give the exact identity

    N_L(z)+N_R(z)
      =c_e[Phi(x+t_-)+Phi(x-t_-)]
         +c_d[Phi(x+t_+)+Phi(x-t_+)].                   (3)

The two summands must be paired before estimating their phase dependence.
N1-13 gives |Phi''|<35 on each open period and an integer derivative
jump of magnitude below 6. For the x and t here, at most the integer
zero can be crossed. The triangular-kernel second-difference identity,
including the jump part of the derivative measure, gives

    |Phi(x+t)+Phi(x-t)-2Phi(x)|
             <=35t²+6(|t|-x)_+, x>=0.                (4)

Indeed the continuous part has total triangular-kernel mass t², and
the atom at zero has weight (|t|-x)_+. There is no moving-boundary
derivative discarded in (4).

Also Phi>=0. To verify this from the existing series, C(s)>=C0 for
0<s<1 follows by the reciprocal-pair expansion about 1/2, whose
nonconstant terms are nonnegative. The formula
Phi(s)=sin(pi s)[C(s)-2log pi]/pi, and C0>3>2log pi, gives positivity
on the open period. At an integer its continuous value is one. Thus the
baseline term 2(c_e+c_d-2)Phi(x) is nonpositive and can be dropped in
an upper bound. Since c_e,c_d<=1 and

    t_-²+t_+²=r2/(2pi²),

the smooth part of (4), integrated with the pole normalization
[2pi sin(z/2)]^-1 on [delta,pi], is at most

    (35r2/(4pi³)) integral_delta^pi csc(z/2) dz
       <315r2/(2pi³).

Here the integral is 2log cot(delta/4)<2log(4/delta)<18. The cusp
part is supported on z>=pi-1/2, where sin(z/2)>=31/32. For each t,
the change of variable dz=-2pi dx gives its normalized contribution
at most (96/31)t². Summing the two t values, both parts together are
less than

    [315/(2pi³)+48/(31pi²)]r2<6r2.                   (5)

This establishes a numerical quadratic upper for the entire regular
pole integral, including both axes and its moving integer cusp.

## 2. Endpoint rows: a quadratic remainder after their actual linear term

For each r>=1 put w=r*pi and c_j=(2j+1)pi, j=0,...,r-1. Partial
fractions in N1-07 give exactly

    ell_r(alpha,b)=sin b/(w+b)
       +4a/(w+b) sum_(j=0)^(r-1)
                      [1/(c_j+b-alpha)+1/(c_j+b+alpha)].      (6)

All denominators are positive on the phase domain. Since a<=1, dropping
a in the positive reciprocal part is an upper bound; it does not change
its value or first derivatives at the origin. The paired sine terms for
b=beta and b=-beta sum to
-2beta sin beta/(w²-beta²)<=0. The only unpaired sine term obeys

    -sin beta/(R*pi-beta)+beta/(R*pi)
            <=(beta-sin beta)/(R*pi)<=r2/(36R).

The closest row sinc beta<=1 contributes no positive increment.

For a reciprocal product in (6), put u=b/w and v=(b+/-alpha)/c_j.
Both have absolute value below 1/6. Taylor's formula along the radial
segment, applied to [(1+lambda u)(1+lambda v)]^-1, gives

    |product-1+u+v|
       <=(6/5)^4(u²+|uv|+v²)<(25/8)(u²+v²).

Averaging the two alpha signs replaces v² by r2/c_j²; u²<=r2/w².
Pairing b signs cancels their linear terms. Including the unpaired
r=R row with a harmless factor two, the total reciprocal remainder
is bounded by

    (50r2/pi^4) [sum_(r=1)^R H_odd(r)/r³
                             +sum_(r=1)^R S_odd,3(r)/r],

where H_odd(r)=sum_(j=0)^(r-1)(2j+1)^-1 and S_odd,3 is the analogous
inverse-cube sum. Use H_odd(r)<=r, sum r^-2<2,
S_odd,3(r)<(7/8)(5/4)=35/32, and H_R<=1+log R<6. The bracket
is below 137/16. With pi²>49/5 this reciprocal remainder plus the
unpaired sine remainder is below 5r2. Therefore

    C_R(alpha,beta)-C_R(0,0)<=d_C beta+5r2,
    d_C=-1/(R*pi)+8H_odd(R)/(R²pi³)
                         +8S_odd,2(R)/(R*pi³).        (7)

The linear coefficient follows either by differentiating (6) or by
retaining its Taylor terms; the paired rows and closest row have zero
beta derivative. The alpha derivative is zero.

## 3. The actual total linear coefficient is small

Write H(beta)=h_J(beta/pi)+h_J(1-beta/pi), and similarly G(beta).
Let q(t)=1/(R+t)²+1/(R+t+1/2), exactly the fixed one-summand jump
constant. The strip and jump derivatives at the origin are

    d_S=(2C0/pi²)H'(0)+(4/pi²)G'(0),
    d_J=(2/pi³)[q(1)-q(0)].                           (8)

The pole integral from section 1 and the endpoint cancellation integral
have zero derivatives at the origin. Hence the asserted derivative is

    d=d_C+d_S+d_J.                                   (9)

We bound this combined expression, not its three absolute summands.
Let f(x)=log x/x, z=J+1, and set

    e_h=1/z²-1/(z²-1/4),
    e_g=integral_(z-1/2)^(z+1/2) f'(x) dx-f'(z),
    e_q=1/(R+1)²-1/[(R+1)²-1/4].

Differentiating the finite telescoped constants from C02 gives the exact
identities

    pi H'(0)=-1/R²+e_h,
    pi G'(0)=(1-log R)/R²+e_g,
    q(1)-q(0)=-1/R²+e_q.

Let V_R=sum_(j=R)^infinity(2j+1)^-2. The identity
sum_(j=0)^infinity(2j+1)^-2=pi²/8, also used in PD-T269 and obtainable
by its locally proved cotangent partial fraction, rewrites (9) as

    d=[8H_odd(R)-2C0+2-4log R-8R V_R]/(pi³R²)
           +(2C0 e_h+4e_g+2e_q)/pi³.                (10)

This displays cancellation of the apparent (log R)/R² slope.

PD-T270 gives H_m=log m+gamma+1/(2m)+r_m with
-1/(8m²)<=r_m<=0. Therefore

    8H_odd(R)-2C0-4log R=8r_(2R)-4r_R,
    -1/(4R²)<=8r_(2R)-4r_R<=1/(2R²).

For V_R apply the centered-cell convexity remainder to x^-2/4 on
[R,infinity):

    0<=1/(4R)-V_R<=1/(16R³).

Thus 0<=2-8R V_R<=1/(2R²), and the first numerator in (10) has
absolute value at most 1/R². Also

    |e_h|<1/(3J^4), |e_g|<9/(4J^4), |e_q|<1/(4R^4).

For e_g this is the one-cell midpoint estimate applied to f', using
|f'''(x)|=|11-6log x|/x^4<54/J^4 on that cell. The other two
estimates follow directly from their displayed rational formulas.
Since C0<4 and pi>3, (10) consequently gives

    |d|<1/(18R^4)+1/J^4<10^-9.                      (11)

The first constant includes the |e_q| term: 1/pi³+1/(2pi³)<1/18.
For the J terms, (8/3+9)/pi³<1. Finally R=128 has R^4>10^8 and
J=4096 has J^4>10^12, so the last strict inequality follows directly.
No infinite h, g or q constant replaced any fixed truncated one.

## 4. Numerical quadratic remainders for the remaining smooth terms

The singular strip constant is exactly

    S=a/pi² [(2C0+D)(2k+H(beta))+4(k²+G(beta))].

Let W0=2C0(2k+H(0))+4(k²+G(0)). Since t=|k| lies in (7,9),
|H(0)|<10, |G(0)|<26 and C0<4,

    W0>4t²-16t-184>-100.

The a variation therefore contributes at most 25r2/pi²<3r2. The
D term is nonpositive because D>=0 and 2k+H(beta)<0.
Differentiating the finite h_J and g_J formulas twice gives

    |h_J''|<1/15000, |g_J''|<1/2500,
    |H(beta)-H(0)-H'(0)beta|<=beta²/120000,
    |G(beta)-G(0)-G'(0)beta|<=beta²/20000.

For the first two bounds, dominate 2sum_(j>=R)(j+t)^-3 by
1/127² and the boundary term by 1/J²; and dominate
sum f''(j+t) by integral_127^infinity 2log x/x³ dx
=(log127+1/2)/127², adding |f'(J+t+1/2)|<9/J².
The factors 1/pi² and the two sides then give the stated beta remainders.
Their contribution to S is below beta²/30000. Finally |d_S|<1,
so replacing a*d_S*beta by d_S*beta costs at most r2/8. Altogether

    S(alpha,beta)-S(0,0)<=d_S beta+4r2.              (12)

The endpoint-half cancellation integral is a times its origin value.
As in C02, its origin absolute value is at most
4pi^-2 log²(pi/(2delta))<256/pi². Since 1-a<=r2/4,
its increment is below 7r2.

For the limiting jump, put E(beta)=q(1-beta/pi)-q(beta/pi). The bounds
|q|<1/100 and |q'|<1/10000 imply |E|<1/50 and |E'|<1/15000.
Subtract d_J beta from 2a beta E(beta)/pi³. The a variation and
the E variation have combined absolute value below r2, uniformly.
Thus its increment is at most d_J beta+r2.

Combine (5), (7), (12), and these last two bounds. The quadratic
coefficients sum to 6+5+4+7+1=23<25, while the linear coefficient
is exactly d. Equation (11) proves (1). All statements extend to the
origin by non-strict inequalities and to the axes by continuity.

## Remaining obligation and history

This theorem sharpens C02's noncentral 1000rho allowance to a numerical
quadratic bound with a separately controlled fixed-truncation slope.
It does not turn the finite-n error into a phase-sensitive error. Nor
does 25r2 fit the coefficient budget at n=10^6. Both improvements remain
concrete obligations for the original sharper target. The positive
central fractional contribution is retained exactly as previously proved.

2026-11-06. Rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving identity and effective effort
unexposed. Only the coordinator-authorized new C03 records were written.
