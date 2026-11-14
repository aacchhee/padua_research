# PD-T?argmax-bridge-codex-C05-finiteh-01 — The retained endpoint phase increment

ID kind: PD-T. Aliases: finite-h reciprocal displacement; paired endpoint
Hessian; unpaired last-row slope. Rules/input
`4b728b04216a5490910780bc609a82b853058426`.

Status: **PROVED analytic developer helper; independent review required**.
This is an endpoint component theorem for exactly N1-15's existing model.
The full finite-degree error of Q_n remains OPEN in this record.

## Statement

Let integer n>=10^6, m=n+1, R=128, alpha,beta>=0,
rho=alpha+beta<=1/2 and r2=alpha^2+beta^2. Let

    E_end(n,alpha,beta)
       =[sum of N1-15's exact retained endpoint rows]/(n*m)
         -C_R(alpha,beta),                            (1)

where the rows are exactly N1-09(5), left r=0,...,127 with b=beta,
right r=1,...,128 with b=-beta, and C_R is N1-07's finite profile.
Then

    |E_end(n,alpha,beta)-E_end(n,0,0)|
       <=45000*r2/n+40*beta/n.                        (2)

The coefficient 40 charges the unpaired r128 row; it is not set to
zero by an unproved symmetry. The full function E_end is even in alpha,
and its Hessian entries have absolute value <45000/n throughout the
phase triangle. Its beta slope at the origin has magnitude <35/n.

There is no extra jump allowance in (2): these finitely many endpoint
rows have fixed signs and no collisions on this domain. The polynomial
exceptional mode and the exact zero-phase continuation are retained.
The bound contributes to both F_n and Q_n with the same endpoint
normalization. N1-18's 9/(2n) is not recharged here: its decomposition
does not remove or alter this endpoint component.

This is a quantitative continuation of the same model, not a second
correction. No limit fit, numerical row evaluation, energy extrapolation
or degree scan is used. The full C1 comparison, and even the separately
registered weaker full-model 1/32 comparison, require the other model
components and are not claimed by this helper.

## 1. Exact finite formula on the sign-fixed rows

N1-09 proves positive complete numerator and the exact positive index
set j=-r+1,-r+3,...,r-1 on all these nonzero rows. Thus

    R_r=-T_r+2*sum_j F_j,
    T_r=n*[a-(sin b/2)*cot(w/(2m))],
    a=(cos alpha+cos b)/2, w=r*pi+b, z=j*pi+alpha,
    F_j=[a*(1+cos v)-(sin alpha/2)*sin u
                         +(sin b/2)*sin v]/(cos u-cos v),
    u=z/n, v=w/m.                                    (3)

The complete corrected first-coordinate highest mode is contained in
this formula; in particular the signed term is a, not a substituted
constant. The finite profile is

    ell_r=sin b/w+8a*sum_j 1/(w^2-z^2).               (4)

Write h=1/n, mu=n/m, eta=1/m=1-mu and

    D=w^2-z^2, D_h=mu^2*w^2-z^2,
    K=sinc((u+v)/2)*sinc((u-v)/2),
    H=(1+cos v)/(2K),
    g=-sin alpha*sin u+sin b*sin v,
    tau(y)=y*cot y, tau(0)=1.                         (5)

Cosine factorization gives cos u-cos v=h^2*D_h*K/2. Therefore, exactly,

    e_r:=R_r/(n*m)-ell_r
       =-a/m+(sin b/w)*[tau(v/2)-1]
          +8a*sum_j [mu/D_h-1/D]
          +8mu*a*sum_j [(H-1)/D_h]
          +2mu*sum_j g/(D_h*K).                      (6)

For r=0 the exact continuation is instead

    e_0=-a/m+sinc(beta)*[tau(beta/(2m))-1].            (7)

The quantity in (1) is e_0+sum_(r=1)^127[e_r(alpha,beta)
+e_r(alpha,-beta)]+e_128(alpha,-beta). Every formula here is smooth
on the auxiliary diamond |alpha|+|b|<=1/2. No polynomial collision or
absolute-value sign transition occurs in these rows, by N1-09's proof.

## 2. Denominators and elementary small-angle bounds

For either sign set k=r+/-j. These k are the positive odd integers
1,3,...,2r-1. On the auxiliary diamond,

    d_+/-=w+/-z > (5/2)*k,
    d_h,+/-=mu*w+/-z >(12/5)*k,
    mu*w>(12/5)*r,
    |u|,|v|<=4r*h, r<=128.                           (8)

Indeed k*pi+b+/-alpha>=(pi-1/2)k>(5/2)k, while
eta*w<4r/n<=512/10^6. Subtract this from d_+/- to get d_h,+/-;
the same bound proves the estimate for mu*w. In particular all D,D_h
are strictly positive. All arguments (u+/-v)/2 have magnitude <1/1000.

The sinc integral gives |sinc x|<=1, sinc x>=1-x^2/6,
|sinc'(x)|<=|x|/3, and |sinc''(x)|<=1/3. Differentiate with respect
to either phase coordinate (alpha,b), keeping n and j,r fixed. It
follows that

    K>=99/100, |K-1|<=(8/3)*r^2*h^2,
    |K_i|<=(4/3)*r*h^2, |K_ij|<=h^2/4,
    |(1/K)_i|<=2r*h^2, |(1/K)_ij|<=h^2,
    |H-1|<=7r^2*h^2, |H_i|<=4r*h^2, |H_ij|<=h^2.    (9)

Here and below i,j on a derivative denote phase coordinates, not the
summation index. To verify the last line, put N=(1+cos v)/2. Then
|N-1|<=4r^2h^2, |N_i|<=2rh^2 and |N_ij|<=h^2/2, and apply the
quotient rule to N/K. The two leading second derivative bounds are
(1/2)/(99/100)+(1/4)/(99/100)^2<77/100; the remaining terms have an
extra factor r^2h^2<=128^2/10^12 and their sum is <1/100. This proves
the displayed bound h^2 with room to spare. The other estimates follow
by the same product rule; |K_ij|<=h^2/6+(8/9)r^2h^4<h^2/4.

For |y|<=1/1000 we will also use

    |tau(y)-1|<=y^2, |tau'(y)|<=2|y|, |tau''(y)|<=2. (10)

These follow directly by differentiating the locally convergent
partial fraction tau(y)=1-2*sum_(k>=1)y^2/(k^2*pi^2-y^2), using
pi>3 and sum k^-2<=2. Uniformly summable derivative majorants justify
the differentiation. These estimates include the values at zero.

## 3. The reciprocal displacement has uniform row derivatives

The key exact identity is

    mu/D_h-1/D
       =(eta/2)*{1/[(mu*w-z)*(w-z)]
                       +1/[(mu*w+z)*(w+z)]}.        (11)

For verification, write each reciprocal quadratic as the sum of its
two linear partial fractions with common prefactor 1/(2w), and
subtract. This retains the mesh displacement before bounding it.

For either product q=1/(d_h*d), (8) and the fact that both linear
factors have phase slopes of absolute value <=1 give

    |q|<=1/(6k^2), |q_i|<1/(7k^3), |q_ij|<1/(5k^4). (12)

For the last inequality the product rule gives
2q*[d^-2+(d*d_h)^-1+d_h^-2]; substituting 2/5 and 5/12 for the
reciprocal constants yields a coefficient <1/5. The first derivative
coefficient is at most 49/360<1/7. Since
sum_(k positive odd) k^-2<4/3, and the two signs in (11) each traverse
the same odd list, S=sum_(j,+/-)q satisfies

    |S|<=4/9, |S_i|<=8/21, |S_ij|<=8/15.             (13)

For example the odd square sum is bounded by
1+1/9+integral_1^infinity(2x+1)^-2 dx=23/18<4/3;
higher powers only reduce it. As |a_i|<=1/4, |a_ij|<=1/2,
(11)-(13) show that the third term of (6), 4eta*a*S, obeys

    |partial_i(4eta*a*S)|<2/n,
    |partial_ij(4eta*a*S)|<4/n.                      (14)

The second derivative coefficient is at most
4*(2/9+4/21+8/15)=1192/315<4. In particular no factor growing with r
is present in this principal mesh displacement estimate.

## 4. The remaining smooth terms have explicit row bounds

Put E=1/D_h. Its partial fraction and (8) give

    sum_j E<2/r, sum_j |E_i|<2/r,
    sum_j |E_ij|<3/r.                                (15)

Indeed sum E <=[5/(24r)]*(5/6)*H_odd(r)<2/r, using
H_odd(r)<=1+log r<6 for r<=128. The derivative multipliers are at
most 5/6 for the first derivative and 25/24 for the second. Combining
(15) and the inverse-K bounds in (9), with F=E/K, gives

    sum_j |F|<4/r, sum_j |F_i|<5/r,
    sum_j |F_ij|<7/r.                                (16)

For the fourth term in (6), product differentiation of a*(H-1)*E,
followed by (9),(15), bounds its Hessian by

    8*[35r+20+2/r]*h^2<=456r*h^2<512r/n^2.          (17)

The summands inside the bracket arise respectively from a_ij,
a_i/a_j, (H-1)_ij, and E_ij and their two cross products; explicitly
their total is 7r+4+7r+2/r+16+21r.

For the last term of (6), direct differentiation of its numerator gives

    |g|<=2rh, |g_i|<=5rh, |g_ij|<=5rh.               (18)

Use |sin alpha|+|sin b|<=1/2, |u|,|v|<=4rh, and the phase slopes
|u_alpha|=h, |v_b|<=h. Mixed second derivatives of g are zero.
Equations (16),(18) therefore bound its Hessian by

    2*[5rh*(4/r)+2*5rh*(5/r)+2rh*(7/r)]
         =168/n.                                    (19)

The first term -a/m in (6) has Hessian bounded by 1/(2n). For the
second term write k(w)=[tau(w/(2m))-1]/w. Equation (10) yields
|k|<=r/m^2, |k'|<=3/(4m^2), |k''|<=4/(5r*m^2).
Product differentiation of sin b*k(w) bounds its only nonzero
Hessian entry by 3r/n^2. In (7), the corresponding closest-row
product has Hessian <=1/n^2; this follows from
|sinc'|<=1/2, |sinc''|<=1/3 and (10).

There are 255 nonzero-r rows and one closest row. Their r-weighted
sum is 2*sum_(r=1)^127 r+128=128^2. Combining (14),(17),(19) and
the signed-term bounds proves the following bound on every Hessian
entry of (1):

    128/n+255*(4+168)/n+(512+3)*128^2/n^2+1/n^2
       <45000/n, n>=10^6.                            (20)

All estimates are for the whole fixed endpoint collection, not for a
growing number of blocks or sign transitions.

## 5. Only the unpaired last row contributes a linear term

Each e_r is even in alpha. In (3), pair the summation index with its
negative when replacing alpha by -alpha; the two sine signs reverse
together, and every other term is unchanged. Formula (7) is also
even in alpha and beta. The paired b=+/-beta rows r1,...,127 are
even in beta. Consequently the alpha slope of E_end at the origin
is zero, and its beta slope is exactly minus the b slope of e_128.

At alpha=b=0 the derivatives of a vanish and g=0. The five terms in
(6) have b slopes bounded respectively by

    0, r/n^2, 2/n, 176r/n^2, 32/n.                  (21)

The fourth bound follows directly from
8[(4rh^2)*(2/r)+(7r^2h^2)*(2/r)]<=176rh^2.
For the last bound use |g_b|=|sin v|<=4rh and sum|F|<4/r.
Thus |partial_b e_128(0,0)|<34/n+177*128/n^2<35/n.

Apply one-variable Taylor's integral formula along the segment
t->(t alpha,t beta). By (20), its second derivative has absolute
value <(45000/n)*(alpha+beta)^2. Therefore

    |E_end(phase)-E_end(origin)|
       <=35*beta/n+(22500/n)*(alpha+beta)^2
       <=40*beta/n+(45000/n)*(alpha^2+beta^2),

which is (2). This is a finite-degree phase estimate for the exact
retained rows. The old N1-07 absolute whole-row approximation error
has not been used as an increment bound or charged a second time.

## Scope and remaining assembly

To control the full Q_n relative to T-T(0), the other terms of the same
model still need finite-degree increment estimates: the paired retained
strip/outer integrals and their lower cell boundaries, both permanently
special central rows and omitted central integrals, finite jump terms,
fixed series constants and the specific N1-18 proof corrections. That
decomposition already charged its discontinuous artifacts. A result for
Q_n must include its actual continuous corrections without adding a
second 9/(2n) envelope by default; a passage back to F_n charges the
known envelope once.

No full C1, larger-budget full comparison, global argmax onset, new
certificate cover or checker change follows from this endpoint helper.
The primary original budget and conditional 1/32 target remain OPEN.
No mathematical numerical computation was needed for this proof.
