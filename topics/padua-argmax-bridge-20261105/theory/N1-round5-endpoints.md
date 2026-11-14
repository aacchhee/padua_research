# PD-T?argmax-bridge-codex-N1-10 — Retained-cell endpoint compactification

ID kind: PD-T. Aliases: next endpoint logarithm; exact half-cell cutoffs;
finite-h regular integral. Split from: the single round-5 correction.
Split into: none. This is the endpoint H-profile reduction, not its
outer jump sum or the central/interior outer certificate.

## Statement and fixed-count model

Use N1-05's H(L,v)=A(v)L+B(v), with alpha,beta>=0, rho<=1/2,
R=128, delta=1/1000, n>=10^6, m=n+1, L=log n and h=pi/m.
Put t_L=beta/pi, t_R=1-beta/pi and, for s=L,R,

    K_s=floor(delta/h-t_s), N_s=K_s-R+1,
    b_s=K_s+t_s+1/2,
    l_s=h*(R+t_s-1/2), u_s=h*b_s,
    q_L=q, q_R=-q, U_L=U1, U_R=-U1,
    U1=[c_e Phi_0'(1/2+(alpha-beta)/(2pi))
         -c_d Phi_0'(1/2+(alpha+beta)/(2pi))]/(2pi).

The quantities Phi_0,c_e,c_d,U0 come from N1-04/05. Define
B0=4a/pi^2, Z_n=U0/pi+B0*log(pi*n/m). Let h_R^[J],g_R^[J]
be N1-06's defining series truncated after index J=4096, including
their initial -log(R+t-1/2) and -(log(R+t-1/2))^2/2 terms.
For z in these cells put

    f_s(z)=[q_s+2a cot(z/2)-4a/z]/pi,
    W_a(z)=4a log(2sin(z/2)/z), W_a(0)=0.

Their integrals are explicit:

    integral_l^u f_s
       =[q_s*(u-l)+W_a(u)-W_a(l)]/pi.

Define the fixed-count model

    M_strip=sum_{s=L,R} {
       Z_n*[log b_s+h_R^[J](t_s)]
       +B0*[(log b_s)^2/2+g_R^[J](t_s)]
       +(L/pi)*integral_(l_s)^(u_s) f_s(z)dz
       +(q_s/pi^2)*integral_(l_s)^(u_s) log z dz
       +U_s*N_s/m } .                                (1)

Here integral log z=z log z-z. All sums have a number of terms
independent of n; the two scalar integer cutoffs are retained exactly.
The ordinary endpoint profile sum satisfies

    |(1/m)*sum_{s=L,R} sum_{k=R}^{K_s}
          H(L,v_s(h(k+t_s)))-M_strip| <1/32768,        (2)

where v_L(z)=z and v_R(z)=2pi-z. More precise explicit component bounds
are given below. The first/last R rows are not part of (2): round 5
retains their exact finite-h terms from N1-09. No R*log n/n estimate
for an omitted initial interval is used.

## Status, dependencies and provenance

Overall status: **PROVED**, analytic developer proof; distinct review
pending. N1-04/05 supply the regularized profile; N1-06 supplies the
uniform shifted-series tails; N1-09 supplies endpoint numerator
positivity. The next-term estimate below was developed by the existing
child /root/n1/endpoint_check under the preregistered round-5 target.
No numerical run, fitted constant or external theorem is a premise.

## Proof

### 1. Exact endpoint integral and next profile terms

Positive numerator on rho<=1/2 and 0<z<=pi/2 fixes the two cancellation
branches as in N1-09. Their exact integrals are

    I_L=(2a cot(z/2)+q)log(sin z),
    I_R=(2a cot(z/2)-q)log(sin z).                     (3)

For 0<z<=delta, subtracting the indicated leading terms and using sine
chords/Taylor inequalities gives

    (1/pi)*|I_s-(4a/z)log z-q_s log z|
      <=[a*z*|log z|]/[3pi*(1-delta^2/24)]
         +[(4a+q*delta)*z]/[pi*(6-delta^2)]
      <(z*|log z|)/9+z/4.                             (4)

Indeed 1/x-cot x<=x/[3(1-x^2/6)],
-log(sin z/z)<=z^2/(6-z^2), cot(z/2)<=2/z. The final constants follow
from a<=1,q<=1/2,delta=1/1000 and 3.14<pi.

We next bound the second derivative of Phi_0 on [1/4,3/4]. N1-04's
local series is C(t)=1/t+2gamma+R(t) for 0<t<=1/2, where

    R(t)=2t^2*sum_{k>=1}1/[k(k^2-t^2)].

Its already established bounds R<=1,R'<=16/3, together with

    R''(t)=4*sum k/(k^2-t^2)^2
                  +16t^2*sum k/(k^2-t^2)^3
       <=32/3+320/27=608/27,

follow from k^2-t^2>=3k^2/4, sum k^-3<=3/2 and sum k^-5<=5/4.
The summable bounds justify differentiation. Differentiate

    Phi_0(t)=sinc(pi*t)
       +(2gamma-2log pi)*sin(pi*t)/pi+R(t)*sin(pi*t)/pi.

The five second-derivative contributions have absolute bounds
10/3,10,608/81,32/3,10/3, respectively; use the sinc integral,
|2gamma-2log pi|<3 and 3<pi<10/3. Their sum is 2822/81<35.
Reflection gives

    |Phi_0''(t)|<35 on [1/4,3/4].                    (5)

All endpoint offsets here lie in that interval. The constant pole
numerator has value U0, derivative +U1 on the left and -U1 on the
right, and second derivative bounded by 35/(2pi^2). Its magnitude is
at most 8. Use Taylor expansion divided first by z, and then
0<=1/[2sin(z/2)]-1/z<=pi*z/48. The remainder after U0/z+U_s is at most

    [35/(4pi^2)+pi/6]*z <3z/2.                       (6)

Combining (4) and (6) proves the precise endpoint expansion

    B(v_s(z))={U0+(4a/pi)log z}/z
                         +(q_s/pi)log z+U_s+E_s(z),
    |E_s(z)| <=(7/4)z+(1/9)z|log z|.                 (7)

No arbitrary bounded remainder or inverse phase distance was used.

### 2. Uniform discrete residual tail

Define, for small positive x,

    G(x)=x^2/2*[7/4+{log(1/x)+1/2}/9], G(0)=0.

Its derivative is the positive increasing envelope in (7) throughout
the required interval. Forward cells of length h based at each sample
are disjoint. Since k>=R, their union is contained in [Rh,delta+h].
Consequently

    (1/m)*sum_both_strips |E_s(z_k)|
       <=(2/pi)*[G(delta+h)-G(Rh)]
       <=(2/pi)*G(delta+h)<1/10^6.                     (8)

For the last strict bound, delta+h<251/250000 and
log(1/(delta+h))<9 give the rational upper bound
6363101/6750000000000<1/10^6. This is a direct discrete enclosure,
not an assumed agreement between a sum and an integral.

### 3. Retained shifted sums and exact cell limits

In the two strips there are no coefficient switches: the switch angles
pi-alpha+beta, pi-alpha-beta and pi+alpha-beta all exceed pi-1/2.
Thus A_s(z)=4a/(pi z)+f_s(z) on every cell used here. The singular
A_s L and B terms combine exactly into

    Z_n*sum_{k=R}^{K_s}1/(k+t_s)
       +B0*sum_{k=R}^{K_s}log(k+t_s)/(k+t_s).           (9)

In particular the coefficient Z_n is bounded by 5 uniformly in n;
the L+log h cancellation is retained, not expanded into separate errors.
N1-06 bounds the error of replacing the sums in (9) by their b_s endpoint
expressions and infinite constants by

    e_HG=sum_s [5+B0*(log b_s+2)]/(8b_s^2).

Here b_s>=delta*m/pi-1/2>317. The decreasing function
[6+(log x)/2]/x^2 and log317<6 give

    e_HG<9/(4*317^2)<1/40000.                         (10)

Truncating both constants at J=4096 contributes at most

    e_const=sum_s [5+B0*(log(J+t_s+1/2)+2)]
                            /[8(J+t_s+1/2)^2]
       <1/10^6,                                      (11)

using log(4097.5)<9. These coefficients are bounded independently of L;
no growing coefficient-truncation error is omitted.

For the regular coefficient f_s, its nonconstant part is u(z)/pi,
where u=2a cot(z/2)-4a/z decreases from zero and
|u(z)|<=a*pi*z/6. The two cell-interval variations sum to at most
a*u_max/3, where u_max=max_s u_s<delta+h/2. Centered-cell BV quadrature
on the actual cell intervals therefore gives

    e_A <=a*L*u_max/(6m)<1/10^8.                       (12)

This keeps both finite-h cell endpoints and has no missing initial
interval. The elementary monotonicity of (log n)/n for n>e and
log(10^6)<14 proves the numerical bound uniformly for n>=10^6.

For log z, its second derivative has magnitude 1/z^2. The centered-cell
integral kernel used in N1-09 bounds the error in its sample sum by
h/(8l_s). After the coefficient q_s/(pi*m) is included, both sides cost

    e_log <=q/[4pi*m*(R-1/2)]<1/10^9.                 (13)

The constant U_s contribution is exactly U_s N_s/m. Equations
(7)-(13) prove (1)-(2), since

    1/40000+2/10^6+1/10^8+1/10^9 <1/32768.

## Scope, checks and history

This removes the growing H-profile sums in the endpoint strips, while
retaining the finite-h rows separately and the exact cell/cutoff terms.
It improves the previously discarded integrable tail by including the
preregistered q log z and U1 terms, not by fitting further coefficients.
The jump sum must still be compacted, and the central/interior outer
sum remains a separate OPEN obligation. No full B3 PASS, maximum
comparison, effective onset or B4 release follows.

No mathematical computation or fit was run. The explicit rational
budget comparisons are consequences of the written inequalities.
Independent review is pending. 2026-11-06, round 5 after fc8c288;
Codex requested gpt-6-astra ultra. The terms and budget were fixed in
../ideas/N1-round5.md before development.
