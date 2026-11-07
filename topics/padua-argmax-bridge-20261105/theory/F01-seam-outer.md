# PD-T?argmax-bridge-codex-F01-seam-outer — Signed joint outer block through five fourths

ID kind: PD-T. Aliases: I07 wider signed outer; atom-inclusive pole continuation;
complete root and four-hole outer charge.
Split from: F01 complete finite relative allowance in F01-seam-finite.md.
Split into: none.

## Statement and definitions

For EVERY integer n>=32 and CLOSED signed rho=|alpha|+|beta|<=5/4 put
m=n+1,L=log n,a=(cos alpha+cos beta)/2,p=sin|alpha|,q=sin|beta|,
d=(q-p)_+. Use EXACTLY E14's literal joint operator

    T_n=Eout(phi)-aEout(0)+(d/pi)Rlog.

Then

    T_n<=rho[((23/3)L+52)/n]+|beta|(17L+27)/n^2.            (1)

The same actual corrected primitive, unequal meshes, exceptional top mode ONE,
endpoint weights, six labels, four holes and complete collision continuations
are retained. Rmesh is NOT inside T_n. Exact real arithmetic, no numerical
premise. Overall status: **PROVED developer PAPER theorem**, distinct review
and adoption required. No endpoint or global-onset claim.

## Depends on and exact interface

E14-wide-signed-outer supplies the full exact decomposition and global smooth
and measure bounds for f(z)=Phi0(1/2+z/(2pi)):0<f<=1,Lip f<2,
|f''|<1 on smooth periods,|f'''|<13/20 inside(-pi,pi), and total
variation of the FULL periodic derivative measure df' is<4, INCLUDING its
negative atom. D37's generic J formulas and full charge bookkeeping and
E02's fixed-origin Shift identity are unchanged. Their old phase-domain
constants are re-proved below wherever needed.

## Proof

Initially alpha,beta>=0. Let e=rho,delta=alpha-beta,ce=cos(e/2),
cd=cos(delta/2),r=ce+cd-2a. As in F01-seam-retained,
ce,cd>=103/128,a>=10609/16384>5/8,P=p+q<=rho,2a-P>0.
Also t=beta/pi<2/5<1/2. The literal operator remains

    Q_tau[G]=(1/m)sum_(k=2)^(m-2)G(h(k+tau))
                                  -(1/pi)int_0^pi G, h=pi/m.

Both offsets t,1-t have m-3 samples, so Q_tau[1]=-3/m. The initial
holes are h(3/2+t),h(5/2-t), total4h; the central holes are
h(3/2-t),h(1/2+t), total2h. Each initial hole is at most5h/2<pi/4,
each central hole at most3h/2<pi/2, and all retained cells lie in
[h/2,pi-h/2]. No omitted row or hole is added or deleted.

### 1. Exact nonpositive logarithmic coefficient

With Z=2a cot(z/2), E14's exact relative profiles obey

    pi*g_L=max(q,p-Z), pi*g_R=max(-q,p-Z,q-2Z).

Subtract q/pi from the first and add q/pi to the second. The resulting
profiles are nonnegative and nondecreasing because a>0. Right-rectangle
integration on each actual shifted sample interval gives Q_tau<=0 for
each. The constants cancel exactly because the two Q_tau[1] coincide.
Thus their entire paired L coefficient is<=0. No near-only derivative
estimate or smoothness through a max switch is needed.

The exact remaining decomposition is

    T=L(Q_t[g_L]+Q_(1-t)[g_R])+Pole
       +(Q_t[C_L]+Q_(1-t)[C_R])/pi+Shift+(d/pi)Rlog,
    C_s=I_s-aI_s(0)-d log(pi-z).

Every term keeps E14's literal masks and normalization. In particular the
last scalar logarithm is charged once.

### 2. New pole estimate, including the periodic derivative atom

Use N_L=ce f(z+delta)+cd f(z-e),N_R=ce f(z-delta)+cd f(z+e),
V_s=N_s-2a f and V0=V_s(0). The global bounds give

    0<=r<=(e^2+delta^2)/8<=rho^2/4<=5rho/16,
    |V_s|<=4rho+r<=69rho/16,
    |V0|<=5rho^2/4<=25rho/16.                             (2)

On the initial half every translation path stays strictly inside(-pi,pi):
pi/2+5/4<pi. Thus no periodic atom is crossed there and

    |V_s'|<=2rho+2r<=21rho/8,
    |V_s''|<=(13/10)rho+r<=129rho/80.

For the intact pole P_s=(V_s-V0)/z+V_s*d0, with d0 increasing from0
to at most1/5, the quotient identity
[(V_s-V0)/z]'=z^-2 int_0^z w V_s''(w)dw gives variation
<=129pi*rho/320<129rho/100. The product variation is at most
[69/80+21pi/80]rho<=27rho/16. Therefore the full initial variation
is<3rho and its supremum is<=279rho/80<7rho/2.

On I=[pi/2,pi], the interval containing I and all translated paths has
length<=pi/2+5/2<2pi. Tonelli against the COMPLETE df' measure gives
Var_I[f(.+b)-f(.)]<=4|b|. This counts its negative atom. Consequently
Var_I(V_s)<=8rho+pi*r<=37rho/4. With
P_s=V_s/[2sin(z/2)]-V0/z and the same weight sup/variations as E14,

    Var_I P_s<=(1639/192)rho,
    sup_I |P_s|<=(821/192)rho.                            (3)

The initial and central pieces join continuously. The midpoint charge for
the two sides is one copy of the combined variation divided by m. The
actual holes cost their total lengths4h and2h times the respective suprema.
Hence the COMPLETE pole charge is

    |Pole|<=rho/m[3+1639/192+4(7/2)+2(821/192)]
             =(6545/192)rho/m<35rho/m.                   (4)

No separate rho/z singularity has been introduced, and no polynomial
collision receives an unweighted-pole value.

### 3. Every cancellation/root charge on the new domain

The initial half remains genuinely root-free: with u0=p/2 and
s_R=a cot(z/2)-q/2, one has
s_R sin z>=a-q/2>=u0+(a-P/2)>u0. Thus the SAME exact initial identities
I_L-aI_L(0)=q log(sin z),I_R-aI_R(0)=-q log(sin z) hold.

On the central half, e0=pi-z,s0=a tan(e0/2),
s_L=s0+q/2,s_R=|s0-q/2| are still in[0,3/2], with at most three
monotone pieces. The exact generic J, b_L,b_R and logarithm subtraction
are those in D37 section6b; their algebraic sup/variation bounds require
only p,q>=0,a<=1. Their parameter integral obeys
G<=p[1+log(4/p)]. At p=0 use its continuous zero value.

The only domain-dependent small-phase guard in that proof is freshly
checked. Put epsilon=h/2. If rho<=epsilon^2/8 and e0>=epsilon, then

    [a tan(e0/2)-q/2]sin e0
       >=(5/8)e0^2/5-rho/2>=e0^2/16>=rho/2>=u0.          (5)

Here1-cos e0>=2e0^2/pi^2>e0^2/5. Thus the root-free alternative is
valid with its SAME cutoff; no inverse root derivative is taken. In the
other regime the unchanged entropy step gives
G<=rho[3/2+log(4/rho)]<=rho[11/2+2ell],ell=-log sin epsilon,
using p log(rho/p)<=rho/exp(1)<rho/2 and rho>epsilon^2/8.

Consequently the full D37 variation accounting survives: two-sided
variation<=rho[39/2+16ell]. The initial removed-interval envelope is
rho[log(pi/(2z))+log pi]; repeating (5) with epsilon=e0 gives the
central integrable envelope rho[7+4(-log sin e0)]. These are applied to
the actual holes above, not to fictitious endpoint samples. The midpoint,
initial-hole and central-hole charges are respectively

    rho[39/4+8log m]/(pi*m),
    4rho[3+log m]/(pi*m),
    rho[22+8log m]/(pi*m).

Their COMPLETE sum remains rho[175/4+20log m]/(pi*m). This explicitly
checks the formerly rho<=1 step (5); all remaining bounds in that exact
bookkeeping have the same parameter range, masks and hole lengths.

In particular no hidden t<1/3 condition is used in those hole charges.
For initial lengths l1+l2=4h, integrate the stated logarithmic envelope
and use concavity of l[1+log(pi^2/(2l))]. Its maximum is at l1=l2=2h,
giving a charge at most4rho[1+log(pi*m/4)]/(pi*m), smaller than the
displayed4rho[3+log m]/(pi*m). For central lengths l1+l2=2h, use
sin e0>=2e0/pi in their envelope. Concavity at l1=l2=h bounds the
charge by rho[22+8log(m/2)]/(pi*m), smaller than the displayed central
charge. Thus the actual larger offsets introduce no uncharged gap cost.

### 4. Fixed-origin Shift, scalar logarithm and the final coefficient

E02's exact finite regrouping has two boundary first differences and
interior second differences. Its intervals are disjoint when2beta<pi,
which holds at beta<=5/4, and all paths remain in[2h,pi-h]. The F0
derivative and derivative-variation proof is phase independent. Thus its
FULL bound is unchanged:

    |Shift|<=beta(17L+27)/m^2.

The full-domain scalar logarithm remains
|Rlog|<=[3log m+log2+2log pi+2]/m, with d<=rho.
Combine these charges, (4), and the nonpositive L term:

    T<=rho/m{35+[23log m+175/4+log2+2log pi+2]/pi}
                                      +beta(17L+27)/m^2.

Using pi>3,log2<7/10,log pi<23/20,log m<=L+1/32, the braces are
at most(23/3)L+4943/96<(23/3)L+52. Positive m denominators can be
replaced by n. At rho=0 all exact terms vanish. This proves (1) on
the closed signed domain by the inherited absolute-phase convention.

## Scope, checks and history

The explicit scalar RHS decreases for every real n>=32 at fixed phase;
this says nothing about monotonicity of the actual finite operator. Rmesh,
ordinary/retained rows and actual-origin conversion are separate charges.
Full D13 and the stronger interior mixed target remain OPEN.

Paper reasoning and owned prose only, 2026-11-07. No scientific execution
or endpoint/base-degree evaluation. Requested Sol xhigh, serving metadata
unexposed; supplied rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2.
Gate, separate release, prospective coefficients, failed/deferred alternatives
and activity boundary are in ideas/attempts F01-seam-domain.md. Distinct
mathematical review/root adoption remain separate from this developer proof.
