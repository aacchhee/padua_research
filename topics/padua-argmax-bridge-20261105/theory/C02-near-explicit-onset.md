# PD-T?argmax-bridge-codex-C02-near-01 — An explicit onset for the unchanged near-model comparison

ID kind: PD-T. Aliases: quantitative fixed-model degree limit; coarse
near residual modulus; exponential near-comparison onset. Split from:
the OPEN N1-19 comparison at n>=10^6. Split into: none. This is a
comparison for exactly N1-15's already fixed model, not another model,
correction, global argmax theorem or expansion of the certified degree range.

## Statement

Use integer n>=10^6, L=log n, alpha,beta>=0, rho=alpha+beta<=1/2,
r2=alpha²+beta², and N1-18's continuous residual Q_n. At rho=0 interpret
r2 log(1/rho) as zero. Then the following completely numerical uniform
modulus holds:

    Q_n(alpha,beta)
      <=1000 rho+(15/32)rho^(3/2)+r2
                    +(1/2)r2 log(1/rho)+5,000,000(L+1)/n.     (1)

In particular, with N1-17/19's exact coefficient loss G_n,

    Q_n-G_n <1/40000                                      (2)

for every integer n with log n>=1,000,000, uniformly on the whole closed
near triangle. Thus N1-17's original near-model increment comparison
holds at the explicit onset ceil(exp(1,000,000)). This onset concerns
the near model only. It is not an argmax onset for the full domain.
The same comparison for every n>=10^6, full C1 at that requested
range and the global theorem remain OPEN. The certified finite range 2–40
is unchanged.

## Status and fixed inputs

**PROVED**, analytic developer helper; distinct supplementary review and
formal Claude audit are separate. No mathematical computation, fitted
constant, numerical integral, sampled value or energy extrapolation is
used. The exact falsifiable bound (1) and proposed log-onset were recorded
in `../ideas/C01-near.md` before this proof was written. The novelty gate,
read shortlist and ownership restrictions are recorded there. The result
is an effectivization of this fixed near residual and its previously
proved central majorant; no claim of a new global mechanism is made.

All symbols and constants retain the definitions of N1-05/07/10/11/15/16/18.
In particular R=128, delta=1/1000, J=4096, m=n+1, h=pi/m,
a=(cos alpha+cos beta)/2, B0=4a/pi², and

    t_L=beta/pi, t_R=1-beta/pi,
    k=log(delta/pi), D0=U0/pi+B0 log pi.

The truncated constants are not replaced by infinite-series constants.
Write h_J(t)=h_R^[J](t), g_J(t)=g_R^[J](t),
H_J=h_J(t_L)+h_J(t_R), G_J=g_J(t_L)+g_J(t_R), and

    q_R(t)=Q_R^[R](t)=1/(R+t)²+1/(R+t+1/2).

The last identity follows by telescoping the single summand in N1-11;
it does not change that model's truncation.

## 1. A quantitative degree limit of the actual fixed residual

Let B_s(z)=B(v_s(z)) be the constant coefficient of N1-05's H=A L+B.
Define a function of phase alone by

    T(alpha,beta)=C_R(alpha,beta)
      +D0(2k+H_J)+B0(k²+G_J)
      +(1/pi) integral_delta^pi [B_L(z)+B_R(z)] dz
      +(2a beta/pi³)[q_R(t_R)-q_R(t_L)].                    (3)

All integrals in (3) are improper integrals of the existing explicit
integrands. N1-14's central logarithm proves convergence, including the
axes, collisions and double origin. Let

    R_n=M_near-B0 L²-b_M L,

where b_M is exactly N1-16's coefficient. We prove the uniform estimate

    |R_n-T| <2,000,000(L+1)/n, n>=10^6.                  (4)

The large allowance is intentional: it is a proved rate, not an
asymptotic O constant. The pieces below refer to the exact decomposition
in N1-15 and charge each piece once.

**Finite endpoint rows.** N1-07, applied to N1-09/15's retained exact rows,
gives the error from C_R as at most

    (334818+1531 H_n)/n+110329830000/n².

Since H_n<=L+1 and n>=10^6, this is less than
1,000,000(L+1)/n. This use of the endpoint profiles is an auxiliary
comparison; the model still has the exact finite-h rows.

**Remaining special rows.** N1-16 bounds each of the at most four exact
special rows, after normalization by n*m, by 2(L+5)/m, including their
actual finite-polynomial collision values. N1-18 bounds the entire
H8/Rhat discrepancy by r_n+192/(450pi m)<1/n. Their combined model
contribution is therefore below 50(L+1)/n. Its limit is zero.

**Outer retained cells.** Compared to two copies of [delta,pi], the
total symmetric-difference length of N1-15's C_s is at most 5h. Indeed,
the two lower endpoint discrepancies total at most h, the two upper
omissions total exactly 2h because t_L+t_R=1, and the collision holes
have total length at most 2h. All these sets lie above delta-h/2>delta/2.
N1-13 gives there

    |A_s|<=8/(pi delta)+3/5<3000.

Thus replacing the outer A integrals by their limits costs at most
15000 L/n. For their B terms, the pole part is U0/z+P_s, with
|U0|<=8 and |P_s|<6. On z<=pi/2 the exact cancellation is
(2a cot(z/2)+q_s)log(sin z), where |q_s|<=1/2. Since cot(z/2)<=2/z,
sin z>=2z/pi and z>delta/2, its absolute value after division by pi is
less than (8000+1/2)*9/3. The pole part is below 16006. On the central
half N1-14 gives I_s=d log(pi-z)+Z_s, 0<=d<=1/2, |Z_s|<3.
Consequently on all the needed sets

    |B_s(z)|<50000+|log(pi-z)|.                         (5)

For sets of total measure M<=5h on two copies, the part where
0<epsilon=pi-z<1 has log integral at most
M[1+log(2/M)]. This follows by decreasing rearrangement on each copy
and the concavity of x log(1/x). This expression increases for M<2,
and 2/(5h)<n. Where epsilon>=1 use |log epsilon|<2. The total logarithm
integral is thus at most 5h(L+3). Equation (5) therefore costs less than
300000(L+1)/n. The combined outer cost is below 315000(L+1)/n.

**Singular strip primitives.** For the exact strip boundary b_s of N1-10,
write

    log b_s=L+k+e_s, |e_s|<5000/n,
    |Z_n-D0|<1/n, |Z_n|<5.                            (6)

For example b_s=delta*m/pi+d_s with |d_s|<=1/2, so its ratio to
delta*n/pi is 1+x, |x|<(1+500pi)/n<.002; the elementary bound
|log(1+x)|<=|x|/(1-|x|) proves (6). Also |k|<9 and |h_J(t)|<6,
as verified in section 2. For each side, replacing

    Z_n(log b_s+h_J(t_s))+(B0/2)log² b_s+B0 g_J(t_s)

by its exact polynomial expansion with log b_s replaced by L+k and
Z_n by D0 costs at most

    [(L+15)+25000+3000(L+10)]/n
       <4000(L+20)/n.

Here B0<=4/9, and the e_s² contribution is below 6/n because n>=10^6.
The two sides cost less than 160000(L+1)/n. Their limiting polynomial is

    B0 L²+(2D0+2B0 k)L+D0(2k+H_J)+B0(k²+G_J).        (7)

**Regular strip terms.** On [0,delta+h/2], N1-13 gives |f_s|<3/5.
The lower boundary l_s=h(R+t_s-1/2) is below 516/n and
|u_s-delta|<2/n. Replacing the f_s integral by its integral over
[0,delta], with its L/pi factor, costs less than 104L/n per side.
For the q_s log z term the corresponding lower integral is at most
516(L+1)/n, and the upper discrepancy at most 16/n. Multiplication by
|q_s|/pi²<=1/18 costs less than 30(L+1)/n per side. The two full limiting
q_s integrals cancel because q_L+q_R=0. Finally |U1|<4 from
|Phi_0'|<=12, and

    |N_s/m-delta/pi|<130/n.

The U_s terms cost less than 520/n per side and their full limiting
terms cancel because U_L+U_R=0. All three regular-strip costs sum to
less than 1500(L+1)/n. Their remaining contribution is exactly
(L/pi)integral_0^delta(f_L+f_R).

**Jump terms.** The two A2 terms in N1-11 have the limit appearing
last in (3). The bounds |A2_b|<=1/3, q_R(t)<1/100, b_K>=n/2 and
m/n<=2 show that the error from replacing m/n by one and dropping
1/b_K is below 1/n per side. Also |A1|<3/4,
|h_R^[R](t)|<6 and log b_K<=L. Their A1 terms cost less than
3(L+1)/n together. The two W_b integrals have integrands below 2 in
absolute value and interval lengths below 2, so their contributions
are below 4/n together. The entire jump error is below 10(L+1)/n.

Adding (7), the regular-strip L coefficient and the whole outer A
coefficient gives exactly B0 L²+b_M L by N1-16's coefficient identity.
There is therefore no leftover logarithm term in (4). The six costs
just established sum to less than

    [1000000+50+315000+160000+1500+10](L+1)/n
        <2000000(L+1)/n.

This proves (4), uniformly in phase, degree parity, all strip/collision
branches, and both axes. The increment definition F_n=R_n-R_n(0,0)
and N1-18's |F_n-Q_n|<9/(2n) now imply

    |Q_n-[T(alpha,beta)-T(0,0)]|
          <5000000(L+1)/n.                            (8)

This also establishes the degree limit of the actual fixed Q_n on the
whole triangle, with its fixed truncated constants explicitly retained.

## 2. An explicit modulus for the noncentral part of T

Write I_c=pi^-2 integral_0^(pi/2)(J_L+J_R)d epsilon, exactly as in
`C01-near-central-upper.md`. This is exactly the central-half
cancellation contribution to T. We prove

    |[T-I_c](alpha,beta)-[T-I_c](0,0)|<=1000 rho.       (9)

It suffices to bound each coordinate derivative of the remaining terms
almost everywhere, uniformly, and integrate along the straight segment
from the origin. The periodic Phi_0 terms are Lipschitz, hence absolutely
continuous on this segment even when an integer cusp is crossed.
All finite endpoint denominators stay positive. Thus no differentiability
at a cusp is assumed in this argument.

**Finite endpoint profile: 766.** In each summand of N1-07 put
w=r*pi+b, z=j*pi+alpha and D=w²-z². Here |j|<=r-1 and
alpha+|b|<=1/2. Consequently

    w-|z|>5/2, w+|z|>=w>(5/2)r, D>6r,
    |partial_alpha D|, |partial_b D|<8r.

There are r summands. Thus their reciprocal sum is at most 1/6 and
each coordinate derivative of this sum has absolute value below 2/9.
Since |partial a|<=1/4, each derivative of 8a times this sum is at
most 1/3+16/9. The derivative of sin b/w is at most
1/[(5/2)r]+(1/2)/[(25/4)r²]<=12/(25r)<1/2.
Each derivative of ell_r is therefore below 3. Finally
|d sinc(beta)/d beta|<=1/2. There are 255 nonzero-r rows, so each
coordinate derivative of C_R is below 766.

**Two singular strip constants: 74.** The bounds |Phi_0|<=4,
Lip(Phi_0)<=12 and |partial c_e|,|partial c_d|<=1/8 give
|partial U0|<5. Hence

    |D0|<4, |partial D0|<2, B0<=4/9, |partial B0|<1/9.

For transparency, telescoping N1-06's finite defining series gives

    h_J(t)=sum_(j=R)^J 1/(j+t)-log(J+t+1/2),
    g_J(t)=sum_(j=R)^J log(j+t)/(j+t)
                                      -(1/2)log²(J+t+1/2).

The initial terms in their original definitions are respectively
-log(R+t-1/2) and -(1/2)log²(R+t-1/2). The centered-cell remainder
bounds of N1-06 give total absolute corrections below one in both
cases: for h use 1/[8(R+t-1/2)²], and for g use
[log(R+t-1/2)+2]/[8(R+t-1/2)²]. Since log(129)<5, this proves
|h_J|<6 and |g_J|<14; the same argument gives |h_R^[R]|<6.
Differentiating the finite telescoped formulas gives

    |h_J'|<=1/127+1/4096<1/100,
    |g_J'|<6/127+9/4096<1/16.

For the second estimate one may dominate the sum by the integral of
log x/x² from 127 to infinity. Since t_s has beta derivative of
absolute value 1/pi, it follows that

    |partial_beta H_J|<1/100,
    |partial_beta G_J|<1/24.

Their alpha derivatives vanish. With |k|<9, the coordinate derivatives
of D0(2k+H_J) and B0(k²+G_J) are respectively below 61 and 13.

**Regular pole integral: 45.** Write its numerator N_s as in N1-13,
so its integrand is N_s/[2sin(z/2)]. Each phase derivative of N_s is
below 1+12/pi<5: the two cosine derivatives contribute at most one,
and the two translated Phi_0 derivatives contribute at most 12/pi.
Both folded sides together therefore give the normalized derivative
bound

    (5/pi) integral_delta^pi csc(z/2) dz
       <=5 integral_delta^pi dz/z=5log(pi/delta)<45.

**Endpoint-half cancellation integral: 8.** N1-10 gives the exact
sum I_L+I_R=4a cot(z/2)log(sin z) on [delta,pi/2]. Its coordinate
derivative after normalization is at most

    (1/pi²) integral_delta^(pi/2) cot(z/2)[-log(sin z)] dz
       <=pi^-2 log²(pi/(2delta))<8.

Here |4 partial a|<=1, cot(z/2)<=2/z, and the sine chord was used.

**Limiting jump: 1.** The explicit rational q_R satisfies q_R<1/100
and |q_R'|<1/10000 on [0,1]. Differentiating the last term in (3),
using beta<=1/2, a<=1, |partial a|<=1/4, and |partial_beta t_s|=1/pi,
shows each coordinate derivative is below one. No infinite jump
constant is substituted for the stipulated one-summand constant.

The five derivative bounds sum to 766+74+45+8+1=894<1000.
Integration along the phase segment proves (9). The already proved
whole-central-integral bound in `C01-near-central-upper.md` is

    I_c(alpha,beta)-I_c(0,0)
       <=(15/32)rho^(3/2)+r2+(1/2)r2 log(1/rho).

Together with (8) and (9), this proves the asserted modulus (1).

## 3. The explicit near-comparison onset

N1-16 gives

    G_n>=A(L)r2,
    A(L)=47L²/(48pi²)+L/(24pi²)>L²/11.

The last strict bound uses pi²<10. Suppose L>=1,000,000, so
A>9*10^10. Put c=15/32 and split the coefficient loss into three parts:

    D_l=A/2, D_f=A/4, D_e=A/4-1.

Since r2>=rho²/2, the following scalar estimates hold for every rho>0:

    1000rho-D_l r2 <=1000²/(2D_l)=10^6/A<1/90000,
    c rho^(3/2)-D_f r2 <=27c^4/(32D_f³)=54c^4/A³<10^-8,
    (1/2)r2 log(1/rho)-D_e r2
          <=(1/(4e)) exp(-4D_e)<10^-8.                (10)

For the last inequality, the left side is nonpositive where its bracket
is nonpositive; elsewhere use r2<=rho² and maximize
rho²[(1/2)log(1/rho)-D_e]. Its unrestricted maximum is exactly the
displayed value. D_e>10 and e>2 give the stated loose numerical bound.
The other two maxima follow by completing the square and setting
y=sqrt(rho), respectively. They also hold at rho=0 by continuity.

Finally, e^L>=L^6/720 and L+1<=2L give

    5,000,000(L+1)e^-L<=7,200,000,000/L^5<10^-8.

Equations (1) and (10) imply

    Q_n-G_n<1/90000+3/10^8<1/40000,

proving (2). Since N1-18 gives |F_n-Q_n|<9/(2n), and

    1/40000+9/(2n)<eta=107/3584000, n>=10^6,

the original increment satisfies F_n<=G_n+eta at this explicit onset.
This is exactly the N1-17 increment comparison, with no asserted
comparison outside the near triangle and no change to the origin
normalization or to the already spent representation allowance.

## Remaining sharper obligation and history

The linear constant 1000 in (1) is a coarse bound on smooth endpoint,
strip and pole terms. It is not evidence of a linear term of that size
in Q_n. The positive fractional term is necessary by the separate actual
axis-limit result; its coefficient cannot simply be deleted. To reach
the requested n>=10^6 bridge, the remaining task is to exploit the
quadratic cancellations and any small finite-truncation cusp in the
noncentral terms, and to sharpen the finite-degree comparison, with
numerical constants that fit N1-19's budget. The present theorem neither
assumes those cancellations nor refutes that stronger goal.

2026-11-06. Rules/input `4b728b04216a5490910780bc609a82b853058426`.
Codex mathematical worker, parent-requested Astra ultra; the coordinator
authorized this C02 continuation after the C01 component freezes. Serving identity
and effective effort are not independently exposed. All prior proof and
review files remain unchanged. No Git or shared-file operation was made.
