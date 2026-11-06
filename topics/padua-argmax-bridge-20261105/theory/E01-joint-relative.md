# PD-T?argmax-bridge-codex-E01-relative — Two retained-charge refinements of the accepted near allowance

ID kind: PD-T. Aliases: quadratic endpoint numerator inside the near outer
operator; retain the cosine multiplier on constant charges.
Split from: the E01 assessment of the OPEN D13 joint relative target.
Split into: none. This is a quantitative consequence of accepted D25,
D35 and D37 estimates, not completion of that original target.

## Statement, definitions and status

For every integer n>=32 put m=n+1, L=log n, H=1+L. Use the corrected
finite polynomial and odd-board primitive literally:

    h_0=1, h_i=2 (i>0),
    D_n(v1,v2)=sum_(i+j<=n) h_i h_j cos(i*v1)cos(j*v2),
    Gpoly=D_n-cos(n*v1), delta_r=(1-r) mod2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n, v_r=(r*pi+beta)/m,
    S_n=(nm)^(-1)sum_(r=0)^(2m-1)sum_(k=0)^(n-1)
                                  |(-1)^delta_r Gpoly(u_rk,v_r)/2|.

On the CLOSED signed near diamond rho=|alpha|+|beta|<=1/2 set

    a=(cos alpha+cos beta)/2, u=1-a,
    A_N=22/n+142/n^2+40H/(pi*n^2),
    C_N=A_N+20/n^2,
    K_E=[8H+(39/2)L+268/3]/n+4/n^2.                    (1)

M_infty is exactly the unchanged D02 completed model, including its full
logarithmic coefficient and true constant. E0(n) is exactly D16's actual
origin allowance, |S_n(0)-M_infty(0,L)|<=E0(n); S_n(0)=Lambda_c(n)
is the actual finite origin, not the model origin. Then

    S_n(phi)-S_n(0)
      <=M_infty(phi,L)-M_infty(0,L)
                         +C_N+K_E*rho+u[E0-A_N].           (2)

Overall status: **PROVED**, written analytic consequence below, requiring
distinct review before adoption. Relative to accepted D35, the right side
decreases by exactly 6rho/n+u A_N. No numerical assertion or improved
global onset is claimed. D13's absolute, fully vanishing joint remainder
remains OPEN. This one-sided result is not a parameter case of that target.

Signed phases use inherited separate evenness and absolute-phase comparison
objects. Unequal n,m meshes are never exchanged. The coefficient of the
highest first-coordinate mode is ONE. The original endpoint weights,
fixed labels and actual polynomial collision values are unchanged.

## Exact telescope and inherited charges

Initially alpha,beta>=0. Use the identical fixed set
A6={0,1,2m-2,2m-1,m-1,m}, its complement O6, and D05/D07 quantities

    Erow=S_n-K_fixed, Eout=K_fixed-Gint, Eret=J6-C2,
    delta_a X=X(phi)-aX(0), E=S_n-M_infty,
    P=sin alpha+sin beta, d=(sin beta-sin alpha)_+.

Gint denotes the scalar D07 intermediate, distinct from Gpoly. The exact
identity, with ordinary index k=2,...,m-2 and upper mesh index m-1=n, is

    delta_a E=delta_a Erow+delta_a Eout+delta_a Eret
                                  +delta_a Rmesh+(d/pi)Rlog.     (3)

The following accepted D35/D22/D13 inequalities are used without changing
their domains or operators:

    delta_a Erow <= 4a/n+20/n^2+40aH/(pi*n^2)
                                         +rho(8H+10)/n,
    delta_a Eret <= [18a+P(8+L)]/n+(142a+4P)/n^2,
    |delta_a Rmesh|+(d/pi)|Rlog| <= rho(L+7/3)/n.           (4)

Thus the central reference complement costs4a/n, including the different
parity transition labels. Both weighted-pole errors cost20/n^2 plus the
displayed a-dependent term. Endpoint reference subtraction includes the
entire Delta_2. All six retained polynomial rows are present; the dropped
origin central contribution has the legitimate sign -aJcen(0)<=0 in this
one-sided upper. No absolute relative-row estimate is inferred from it.

Only the following outer constant is reduced:

    |delta_a Eout| <= rho[(35/2)L+69]/n.                   (5)

The next calculation proves (5) by combining already accepted estimates.

## Reuse the quadratic endpoint numerator on the near domain

Use exactly D25's profiles, f(x)=Phi0(1/2+x/(2pi)), ce=cos(rho/2),
cd=cos((alpha-beta)/2), e=rho, delta=alpha-beta, and

    N_L=ce f(z+delta)+cd f(z-e),
    N_R=ce f(z-delta)+cd f(z+e), N0=2f(z),
    V_s=N_s-aN0, V0=U0-aU0(0).

D37-relative-wide (20), PROVED on rho<=1, gives

    |V0|<=e^2+delta^2<=2rho^2<=rho                     (6)

on the original near domain. In detail, f is even with f'(0)=0 and
|f''|<1 on the relevant open period. Also |f(0)|<=4 and
0<=ce+cd-2a<=(e^2+delta^2)/8. The two Taylor increments and the residual
coefficient therefore sum to at most e^2+delta^2. This is the same proved
endpoint estimate restricted to a smaller domain, not a radius extension.

D25 retains, on that near domain,

    |V_s|<=(9/2)rho,
    Var_[pi/2,pi] V_s<15rho.                            (7)

The latter includes all periodic derivative atoms; no cusp is assumed
smooth. On the central half the EXACT regular pole difference is

    Pdiff_s=V_s/(2sin(z/2))-V0/z.

The weights have the accepted bounds

    sup 1/(2sin(z/2))<3/4, Var 1/(2sin(z/2))<1/4,
    sup 1/z<2/3, Var 1/z<1/3.

Consequently (6)-(7), the BV product inequality, and the triangle inequality
give, with non-strict inequalities also covering rho=0,

    Var_[pi/2,pi] Pdiff_s
       <=[(3/4)15+(1/4)(9/2)+1/3]rho
        =(305/24)rho <=13rho,
    sup_[pi/2,pi]|Pdiff_s|
       <=[(3/4)(9/2)+2/3]rho=(97/24)rho <=(9/2)rho.   (8)

On the initial half the unchanged D25 bounds are variation at most
(9/2)rho log m+2rho per side and sup at most4rho. Combining both sides
therefore gives total variation at most rho(9log m+30).

The ACTUAL centered-cell geometry is unchanged: h=pi/m, t=beta/pi,
initial holes h(3/2+t),h(5/2-t), total4h; central holes h(3/2-t),
h(1/2+t), total2h. The midpoint charge is half the total variation/m;
the initial-hole charge remains16rho/m; the central-hole charge from
(8) is9rho/m. Thus the entire regular pole contribution is at most

    rho[(9/2)log m+40]/m.                              (9)

This replaces D25's +46 by +40 and changes nothing else in its operator.

## Preserve the other outer terms and the actual mesh shift

The exact D25 operator is

    Q_tau[f]=(1/m)sum_(k=2)^(m-2)f(h(k+tau))
                                          -(1/pi)integral_0^pi f,
    Eout=Q_t[F_L]+Q_(1-t)[F_R], F0=F_L(0)=F_R(0),
    W_s=F_s(phi)-aF0,
    delta_a Eout=Q_t[W_L]+Q_(1-t)[W_R]+Shift,
    Shift=(a/m)sum_(k=2)^(m-2)
       [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))].   (10)

In addition to (9), all D25 charges remain:

    L coefficient: 7rho L/(pi*m),
    cancellation including all roots and both holes:
                      rho[175/4+20log m]/(pi*m),
    actual-origin mesh shift:
                      (rho/m)[(8/3)L+(4/3)log m+40/3].  (11)

In particular no mesh shift is declared zero, no endpoint logarithm is
replaced by an uncharged value, and the root-free/small-mesh alternative
underlying the cancellation bound is the accepted D25 proof. From
(9)-(11), using pi>3,

    |delta_a Eout|
       <=(rho/m)[5L+(25/2)log m+815/12]
       <=(rho/n)[(35/2)L+69].                         (12)

Indeed log m<=L+1/32 and 815/12+25/64=13115/192<69.
Every bracket is positive. This proves (5), including both phase axes.

## Complete assembly and origin conversion

Insert (4)-(5) in (3) and use P<=rho, retaining the a factors on constant
charges. The constants sum to aA_N+20/n^2, and the linear coefficient is

    [8H+10+(8+L)+(L+7/3)+(35/2)L+69]/n+4/n^2=K_E.

Therefore delta_a E<=aA_N+20/n^2+K_E*rho. The exact conversion is

    E(phi)-E(0)=delta_a E-uE(0)
        <=aA_N+20/n^2+K_E*rho+uE0
         =C_N+K_E*rho+u(E0-A_N).

This is (2). The entire actual uE0 charge is paid before combining with
the model's -uT; such a combination would give -u(T-E0+A_N).
The theorem does not by itself assert monotonicity of this modified
coefficient in n. A later all-n assembly must check that obligation or
retain the weaker accepted V=T-E0 while using only K_E's improvement.

The complete row expression is continuous by D05. The proof of (4)
extends from dense collision-free phases only in that complete expression;
individual reference/pole samples are never assigned a collision value.
The outer terms use continuous weighted Phi and the accepted matching
root formulas. Thus (2) covers both parities, all actual collisions and
the closed rho=1/2 seam with original endpoint multiplicities. QED.

## Limits, dependencies, checks and next obligation

C_N and K_E are positive and decrease for real n>=32 by the same
elementary derivative checks as D35; the logarithmic coefficient of K_E
is27.5 and its constant exceeds27.5. No stronger wide-domain coefficient
is claimed. Retaining a in D37 alone similarly gives its unchanged wide
bound minus u[23/n+184/n^2+40H/(pi*n^2)], a direct bookkeeping consequence
that is not needed above.

Dependencies: accepted [D25](D25-outer-relative.md),
[D35 near](D35-relative-allowance.md), [D37 wide](D37-relative-wide.md),
and their exact D05/D07/D13/D16 identities and continuity premises.
No external theorem, new literature attribution, numerical premise or
new model is introduced. The accepted global theorem still starts at1024.

The remaining D13 obligation is the genuinely relative, collision-safe
joint control of the central reference, weighted-pole approximation and
six retained polynomial rows. Separate absolute allowances in (4) leave
C_N positive even at phase zero; neither (6) nor a coefficient refinement
removes that issue. This is a limit of this bound, not an impossibility
theorem. No all-degree argmax conclusion is rejected.

Checks: paper algebra only; no scalar, native, phase, degree, endpoint,
quadrature or scientific job ran. Root and the distinct reviewer control
adoption. Candidate/gate timing and the deferred stronger shift route are
recorded in [idea](../ideas/E01-joint-relative.md) and
[attempt](../attempts/E01-joint-relative.md).

2026-11-06, input/rules63c70b7c1c226be42a159b29d45de81fdeda22e4;
requested Astra ultra under the prospective E01 LOG justification;
serving metadata unexposed. Only the three assigned E01 files are written.
