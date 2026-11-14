# PD-T?argmax-bridge-codex-C04-near-01 — A noncentral quadratic constant of eight

ID kind: PD-T. Aliases: negative periodic derivative atom; retained endpoint
cosine loss; coupled strip and endpoint cancellation. Split from: C03's
noncentral bound. Split into: C04-near-limit-comparison.md.

## Statement and status

Use precisely C02's limiting function T and C01's whole central integral
I_c, on alpha,beta>=0, rho=alpha+beta<=1/2. Put r2=alpha²+beta².
With d equal to the actual combined beta slope in C03, one has

    [T-I_c](alpha,beta)-[T-I_c](0,0)<=8r2+d beta
                                      <=8r2+10^-9 beta.       (1)

**PROVED**, analytic developer helper. The exact fixed constants R=128,
J=4096 and delta=1/1000 are retained. C03's proved |d|<10^-9 is used,
not an assumption that the slope vanishes. No finite-n phase error bound,
new model, numerical computation, integral evaluation or fitted coefficient
is a premise. Independent supplementary review and formal Claude audit are
separate. The continuation and scope are recorded in ../ideas/C04-near.md.

All notation is as in C03. The proof improves its numerical allocation by
retaining three favorable signs. Its existing bound and all older frozen
sources remain unchanged.

## 1. A one-sided second derivative bound for the periodic pole profile

On 0<t<=1/2, N1-04 gives

    Phi(t)=sinc(pi t)+k0 sin(pi t)/pi+R(t)sin(pi t)/pi,
    k0=2gamma-2log pi,
    R(t)=2 sum_(j=1)^infinity zeta(2j+1)t^(2j).

The uniformly convergent differentiated series justify all derivatives used
below. All coefficients of R are positive. Since zeta(2j+1)<5/4,

    R'(t)<=5t/(1-t²)².

Also R'' is increasing, and the reciprocal-pair formula at 1/2 gives

    R''(1/2)=28zeta(3)-16<19.

The sinc integral representation and cos x>=1-x²/2 give

    [sinc(pi t)]''=-pi² integral_0^1 u² cos(pi t u)du
       <=-pi²(1/3-pi²/40)<=-pi²/12.

The last comparison uses pi²<10. We have gamma>23/40 from N1-16,
and log pi<6/5; hence -k0<5/4. Drop the negative term
-pi R(t)sin(pi t) in the second derivative of the last product.
For the remaining derivative term, use cos(pi t)<=pi(1/2-t) and

    t(1/2-t)/(1-t²)²<=3/40, 0<=t<=1/2.

The latter follows because
3(1-t²)²-40t(1/2-t)=3+34t²+3t^4-20t>0:
the quadratic part has minimum 3-100/34>0. Consequently

    2R'(t)cos(pi t)<=3pi/4,
    Phi''(t)<=-pi²/12+2pi+19/pi<12.                  (2)

For the final scalar comparison use 31/10<pi<22/7. Reflection proves
(2) on the other half of each open period. Its derivative is continuous
at the half-integer because Phi is symmetric there. At an integer the
derivative jump is 2k0<0, since gamma<3/5<log pi. Thus, as a measure,
the distributional second derivative satisfies

    Phi'' <=12 dt,

including all integer derivative atoms. Integrating against the positive
triangular kernel yields the global upper bound

    Phi(x+t)+Phi(x-t)-2Phi(x)<=12t².                 (3)

There is no omitted positive cusp allowance: the actual atom is negative.

Apply (3) to the exact two-phase paired numerator (3) of C03. As already
proved there, Phi>=0, so its baseline cosine change is nonpositive. Since
t_-²+t_+²=r2/(2pi²), the entire normalized regular pole increment is at most

    (12r2/(4pi³)) integral_delta^pi csc(z/2) dz
       <=54r2/pi³<=(15/8)r2.                         (4)

## 2. Retaining the endpoint cosine loss

Write the positive reciprocal part of C03(6), summed over all retained
rows and with a omitted, as P(alpha,beta). Its origin value P0 obeys

    P0=(16/pi²)sum_(r=1)^(R-1) H_odd(r)/r
                            +8H_odd(R)/(Rpi²)>16.   (5)

Here is an explicit proof of the lower bound. PD-T270 gives

    H_odd(r)=H_(2r)-(1/2)H_r
       >=(1/2)log r+log 2+gamma/2-1/(32r²).

Use log 2>69/100, gamma>23/40, and H_(R-1)>=log R>24/5.
Since log x/x decreases for x>=3,

    sum_(r=1)^(R-1) log r/r
       >=(1/2)log² R-(1/2)log²3+(1/2)log2
       >(1/2)log² R-1/3.

The last comparison uses log3<11/10 and log2>69/100. Therefore

    sum_(r=1)^(R-1)H_odd(r)/r
       >(1/4)(24/5)²-1/6+(391/400)(24/5)-5/128>10.

Multiplication by 16/pi²>8/5 proves (5).

C03's reciprocal Taylor bound gives
P-P0<=d_P beta+K_P r2, where d_P>0 is the derivative of the
unpaired b=-beta row, and K_P plus the unpaired sine remainder is
less than 5. Restore the actual factor a:

    aP-P0=a(P-P0)-(1-a)P0
       <=d_P beta+K_P r2-16(1-a).

This uses a<=1 and d_P beta>=0. The closest row and paired sine terms
remain nonpositive; add the same unpaired sine remainder and linear
term as C03. Its d_C is therefore unchanged. N1-16 gives
1-a>=47r2/192, so

    C_R(alpha,beta)-C_R(0,0)
       <=d_C beta+[5-16(47/192)]r2
        =d_C beta+(13/12)r2.                         (6)

## 3. Couple the strip constant and endpoint cancellation integral

Set J_delta=integral_delta^(pi/2) cot(z/2)log(sin z)dz<0,
t=|k|=log(1000pi), and b=log 2. Let H(beta),G(beta),S and D have
their exact C03 meanings. The strip plus endpoint-half cancellation is

    E=a/pi²[(2C0+D)(2k+H(beta))
                           +4(k²+G(beta))+4J_delta].

The elementary bounds needed here are

    8<t<81/10, 69/100<b<7/10,
    |H(0)|<10, |G(0)|<26, C0<4,
    -H(beta)>2log(127.5)>48/5.                        (7)

The h_J initial term is -log(R+t_s-1/2), and each centered convex
reciprocal correction is nonpositive, proving the last inequality.
The remaining constant bounds were proved in C03, except the sharpened
range for t. For that range, the elementary exponential estimates
e<68/25 and e>19/7 suffice: (68/25)^8<3000<1000pi, while
(19/7)^8(11/10)>22000/7>1000pi and exp(1/10)>11/10.
These are integer comparisons after clearing denominators. Also
exp(24/5)<(68/25)^5/(6/5)<127.5, giving the logarithm in (7).

The endpoint sine-chord estimate gives

    -J_delta<=log²(pi/(2delta))=(t-b)².

Let W0=2C0(2k+H(0))+4(k²+G(0))+4J_delta. By (7),

    -W0<=4t(C0-2b)+20C0+104+4b²
         <4(81/10)(4-138/100)+80+104+4(7/10)²
          =33856/125.

Thus its baseline a variation costs at most

    (1-a)(-W0)/pi²<=8464r2/(125pi²)<=169280r2/24625,   (8)

using pi²>197/20. The remaining D term has the favorable sign. The
j=0 term of the reciprocal-pair series gives D>=8r2/pi², while
a>=15/16 and -(2k+H(beta))>16+48/5=128/5. Consequently

    aD(2k+H(beta))/pi²<=-192r2/pi^4<=-(48/25)r2.      (9)

The beta-dependent strip remainder is exactly the one in C03. Its
quadratic part is bounded by beta²/30000 after subtracting d_S beta.
Moreover |d_S|<1/10: C02 gives |H'|<1/100 and |G'|<1/24,
and D0(0)<1, B0(0)<1/2. Restoring its factor a therefore adds at
most r2/80. Equations (8)–(9) give

    E(alpha,beta)-E(0,0)
       <=d_S beta+[169280/24625-48/25+1/80+1/30000]r2
        <=d_S beta+5r2.                              (10)

The final rational coefficient is strictly below five. Unlike separate
absolute bounds, (10) retains the common endpoint logarithm and the
negative D contribution; no term of the fixed model is removed.

## 4. Sum the allocation

For the limiting jump set U(beta)=q(1-beta/pi)-q(beta/pi). The C03
bounds |U|<1/50 and |U'|<1/15000 show, after its linear d_J beta
term is subtracted, that the absolute remainder is at most

    (2r2/27)(1/400+1/15000)<=r2/1000.                (11)

Add (4), (6), (10) and (11). Their quadratic coefficients satisfy

    15/8+13/12+5+1/1000=191/24+1/1000<8.

Their linear terms sum to exactly C03's d, with |d|<10^-9. This proves
(1), including both axes and the origin, where all inequalities are
interpreted non-strictly. The favorable fractional central term has not
been replaced by a quadratic term; it remains outside this theorem.

## Scope and history

This is a numerical bound for the same limiting noncentral residual.
A separate finite-degree phase error is still needed to prove the actual
Q_n comparison for n>=10^6. The finite certified degree range and global
argmax question are unchanged. No assumption of a positive limiting
uniform margin away from the origin is used.

2026-11-06. Rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving metadata unexposed. The
coordinator was informed of the exact continuation and proposed label.
