# PD-T?argmax-bridge-C06-far-compact — A full-phase fixed-count model with error9/25

ID kind: PD-T.
Aliases: uncorrected H4 full-diamond completion; full-phase central BV;
constant-size far model with explicit finite-degree error.
Split from: the primary n>=10^6 far-comparison target, which stays OPEN.
Split into: the model maximum comparison is separately owned C08 work.

## Exact statement and model contract

For every integer n>=10^6 and every real pair |alpha|+|beta|<=pi, use
absolute phases in the following definitions. Let L=log n, a=(cos alpha+
cos beta)/2, R=64 and delta=1/100. Put

    M_far(alpha,beta,L)=(4a/pi^2)L^2+b_full(alpha,beta)L+C_far,
    C_far=C_R+c_mesh+(1/pi)integral_delta^(2pi-delta) B(v)dv.   (1)

Then

    |S_n(alpha,beta)-M_far(alpha,beta,log n)|<9/25<1/2.        (2)

All phases, axes, vertices, a=0, polynomial collisions and both parities
are included. No exchange of the n and n+1 meshes is assumed.

Here are the complete fixed-count definitions. Phi_0 is N1-04's continuous
periodic function, with value1 at integer arguments. For0<t<1 it is

    Phi_0(t)=sin(pi*t)/pi*[Cseries(t)-2log pi],
    Cseries(t)=2gamma+1/t+1/(1-t)
          +sum_{k=1}^infinity[1/(k+t)+1/(k+1-t)-2/k].

This fixes the exact pole-series convention as well as its integer
extension. Set

    c_e=cos((alpha+beta)/2), c_d=cos((alpha-beta)/2),
    eta_-(v)=1/2+(alpha-beta+v)/(2pi),
    eta_+(v)=1/2+(alpha+beta-v)/(2pi),
    U0=c_e Phi_0(eta_-(0))+c_d Phi_0(eta_+(0)),
    V(v)=[c_e Phi_0(eta_-(v))+c_d Phi_0(eta_+(v))]
                                                   /[2sin(v/2)],
    C(v)=[sin alpha-sin beta-2a cot(v/2)]/4,
    D(v)=[sin alpha+sin beta+2a cot(v/2)]/4,
    I(C,D,v)=integral_0^pi (|C cot x+D cot(x+v)|
                                -|C cot x|-|D cot(x+v)|)dx,
    B(v)=V(v)+I(C(v),D(v),v)/pi.                              (3)

The cancellation integrand has its ordinary one-sided finite values at
its two pole positions; changing point values does not change I. At v=pi
the outer integral in (1) is the improper integral of the full function.
Its explicitly integrable logarithm is proved below. Separate singular
channel integrals are never used. N2/N1-02 provide finite sign-arc/logarithm
formulas for I, so no degree-dependent sum is concealed in (3).

Use the exact full-domain coefficient from C06-far-full-profile:

    b_full=2U0/pi+[8a log2+4a loga
                   +2(alpha sin alpha+beta sin beta)]/pi^2,  (4)

with a loga=0 at a=0. Define B0=4a/pi^2, D0=U0/pi+B0 log pi,
kappa=log(delta/pi), t_L=beta/pi, t_R=1-beta/pi, and

    c_mesh=B0 kappa^2+2D0 kappa
                  +D0[h_R(t_L)+h_R(t_R)]
                  +B0[g_R(t_L)+g_R(t_R)].                    (5)

For0<=t<=1, with x_k=k+t and q_R=R+t-1/2, the exact convergent constants are

    h_R(t)=-log q_R+sum_{k=R}^infinity
                         [1/x_k-log((x_k+1/2)/(x_k-1/2))],
    g_R(t)=-(log q_R)^2/2+sum_{k=R}^infinity
             [log(x_k)/x_k-{log²(x_k+1/2)-log²(x_k-1/2)}/2].   (6)

N1-06 bounds the tails after K>=R by1/[8(K+t+1/2)^2] and
[log(K+t+1/2)+2]/[8(K+t+1/2)^2], respectively. Every numerical use must
multiply these errors by the coefficients in (5); (1) uses the exact
constants, not the diagnostic's truncations.

Finally let ell_0(beta)=sin beta/beta, with value1 at beta=0. For r>=1,
b in{beta,-beta} and w=r*pi+b>0 set z_j=j*pi+alpha and

    f_j(alpha,b,r)= [cos((alpha+b)/2)*sigma_-*sinc((z_j-w)/2)
                   +cos((alpha-b)/2)*sigma_+*sinc((z_j+w)/2)]/w,
    sigma_-=(-1)^((r-j-1)/2), sigma_+=(-1)^((j+r-1)/2),
    ell_r(alpha,b)=sin b/w+2 sum_{j=-r+1,-r+3,...,r-1} f_j,
    C_R=ell_0(beta)+sum_{r=1}^{R-1}ell_r(alpha,beta)
                                  +sum_{r=1}^R ell_r(alpha,-beta). (7)

These are exactly N1-07's finite endpoint profiles: away from removable
points f_j=4a/[w²-z_j²]. Formula (7), with sinc0=1, defines those
removable points without a zero-times-infinity convention. The only
w=0 case is r=1,b=-pi,alpha=0, where ell_1(0,-pi)=1. N1-07 proves
its uniform continuous extension. Thus (1) has O(R²) finite terms,
fixed convergent series with explicit tails and fixed integrals; its
only degree argument is L. In particular no floor/ceil depending on n
is needed to evaluate this model.

## Status, assumptions and dependencies

Overall status: **PROVED**, by the analytic derivation below; distinct
supplementary review and formal Claude audit remain publication obligations.
The primary far maximum comparison, including n>=10^6, remains OPEN here.
A numerical evaluation of (1) is not a proof of that comparison.

Exact corrected kernel, odd board and S normalization are those in
C06-far-full-profile.md. Dependencies are the original full-domain
N1-02/04/05/06/07/08, and C06-far-full-profile's exact coefficient
integration and polynomial-continuity upper. The algebraic general
J identities and differentiated pole-series arguments in N1-10/13/14
are reconstructed below on their actually needed full parameter ranges.
Their near-domain statements are not assumed globally. The fixed near
model, its one correction and every old proof remain unchanged.

## Proof

### 1. Full-domain regular pole bounds

For each folded half v_L(z)=z,v_R(z)=2pi-z define

    N_s(z)=c_e Phi_0(eta_-(v_s(z)))+c_d Phi_0(eta_+(v_s(z))),
    P_s(z)=N_s(z)/[2sin(z/2)]-U0/z.

The following bounds hold for the entire phase triangle:

    sup|P_s|<6,       Var(P_L)+Var(P_R)<23.                    (8)

Here is the domain verification. On0<t<=1/2 write
Phi_0(t)=sinc(pi t)+(2gamma-2log pi)sin(pi t)/pi+R(t)sin(pi t)/pi.
The N1-04 series has R<=1,R'<=16/3 and R''<=608/27 throughout this
whole half interval: k²-t²>=3k²/4 justifies differentiating the summable
series. The five second-derivative contributions are bounded by
10/3,10,608/81,32/3,10/3, summing to2822/81<35. Reflection gives
|Phi_0''|<35 on every open period. The derivative jump at an integer
has magnitude below6, and Phi_0 is globally12-Lipschitz.

Each eta traverses half a period as z traverses[0,pi], meeting at most
one integer jump. With0<=c_e,c_d<=1 this proves

    sup|N_s|<=8, Lip(N_s)<=12/pi,
    Var(N_s)<=12, Var(N_s')<=47/(2pi).

Let d0(z)=1/[2sin(z/2)]-1/z. It increases from0 to1/2-1/pi. Its
monotonicity follows from sin²x>=x²cos x on[0,pi/2], whose derivative
comparison uses sin x>=2x/pi and x-sin x<=x³/6. The identity

    P_s(z)=integral_0^1 N_s'(tz)dt+N_s(z)d0(z)

then gives sup|P_s|<=4+4/pi<6 and
Var(P_s)<=47/(2pi)+20(1/2-1/pi)=10+7/(2pi).
One-sided derivative values at integer crossings suffice; all derivative
jumps are included. This proves (8) without a small-phase assumption.

### 2. The generic cancellation identity and full central range

Put J(u,s,e)=I((u-s)/2,(u+s)/2,e), where u,s>=0,0<e<=pi/2.
Exchanging the channels, reversing both signs and replacing e by-e
leave I unchanged, by changes of integration variable on the cotangent
circle. For s<=u, with c=(u-s)/2,b=(u+s)/2, direct cotangent integration
on its two opposite-sign intervals gives

    J=2[c log(c/u)+b log(b/u)],                              (9)

interpreting0log0 as0. When s>u, put c=(s-u)/2,b=(s+u)/2 and
R=J-2(s-u)log(sin e). If s sin e>=u, then J=2s log(sin e).
Otherwise set theta=arcsin(s sin e/u),x1=(theta-e)/2. Splitting the
long cancellation interval at its two equality roots gives

    J=2s log(sin e)+2[b log(cos x1/sin(x1+e))
                         -c log(cos(x1+e)/sin x1)].           (10)

The roots are obtained from sin(2x+e)=s sin e/u; on each sign piece
I is-2 times the smaller cotangent channel, whose integral is a log sine.
This verifies (9)--(10), including their continuous limiting cases.
Set R=J when s<=u. These formulas imply

    J=2(s-u)_+ log(sin e)+R,
    |R|<=max(2u,s+u)log2,
    |R_s|<=log((u+s)/|u-s|),                              (11)
    R_e=2[u cos e-sqrt((u²-s²sin²e)_+)]/sin e>=0 for s>u,
    R_e=0 for s<=u.

In the no-root s>u case the square root is zero; the derivative is
increasing with s at fixed u,e. The finite e=0 value for s>u is
2[c log c+u log u-b log b], while R(u,s,pi/2)=0. These follow by
differentiation of (10); moving-root boundary terms cancel. The displayed
integrable parameter bound handles s=u and u=0 by limits.

For the central folded curves use e=pi-z and

    u=p/2<=1/2,
    s_L(e)=q/2+a tan(e/2), s_R(e)=|q/2-a tan(e/2)|,
    d=(q-p)_+<=1.

Both s values lie in[0,3/2]. The first is monotone, the second has at
most two monotone pieces. For S>=u,

    integral_0^S log((u+s)/|u-s|)ds
       <=2u[1+log((S+u)/u)].                                (12)

At u<=1/2,S=3/2 this is less than1+log4<5/2. Thus parameter motion
costs less than15/2 over the two curves. Monotonicity of R_e before
integration bounds each separation-motion cost by(S+u)log2<3/2.
Together their R variations are below21/2.

Writing k_s(e)=2(s_s(e)-u)_+, one has k_s(0)=d,
|k_s'|<=2a and |k_s-d|<=2a tan(e/2). Therefore

    Z_s(e)=I(v_s(pi-e))-d log e
       =R(u,s_s(e),e)+(k_s(e)-d)log(sin e)
                                      +d log(sin e/e).        (13)

The last two terms have variation at most

    a*pi*log2+a*pi/2+d*log(pi/2)<9/2

on each half. Indeed integral_0^(pi/2)-log(sin e)de=(pi/2)log2,
and tan(e/2)cot e=cos e/(1+cos e)<=1/2. Thus

    sup|Z_s|<4,       Var(Z_L)+Var(Z_R)<20.                    (14)

For the sup bound use |R|<3/2,
e[-log(sin e)]<=e log(pi/(2e))<3/5, tan(e/2)<=e and
log(pi/2)<1/2. The two last terms tend to zero as e->0; both R curves
have the same finite limit. This proves continuous central extensions,
including p=q, zero phases and a=0. The enlarged bounds(14) were derived
for u<=1/2,S=3/2; no near-domain theorem was extended without proof.

### 3. A single regular part on the interior and expanded cells

Let h=pi/m and write z=min(v,2pi-v). All selected interior centered
cells lie in z>=delta-h/2>delta/2. Define

    ell(v)=log(2|v-pi|/pi) if |v-pi|<=pi/2,
           0 otherwise,
    W(v)=V(v)+[I(C(v),D(v),v)-d ell(v)]/pi.

The central finite extension of W is used. We claim on
[delta/2,2pi-delta/2]

    sup A<300, Var(A)<600,
    sup|W|<4000, Var(W)<12000.                               (15)

The A bounds follow from the exact full-phase max formulas in the earlier
C06 profile proof: T=2a cot(z/2)<=4/z<=800, sup A<801/pi<300
and Var(A)<=2T(delta/2)/pi<1600/pi<600.

For V=U0/z+P, (8) and |U0|<=8 give
sup|V|<1606<1700 and Var(V)<3200+23=3223.
In the endpoint halves delta/2<=z<=pi/2, the generic J parameters are

    s_L(z)=q/2+a cot(z/2), s_R(z)=|q/2-a cot(z/2)|,
    u=p/2, 0<=s_s<=401.

Their total variation is below800, with at most three monotone pieces.
Hence k_s=2(s_s-u)_+ has total variation below1600 and sup k_s<=802.
Also -log(sin z)<log(400)<7. The product k_s log(sin z) consequently
has total variation below

    7*1600+2*802*7=22428.

Equation(12), now S=401,u<=1/2, bounds the three parameter-motion
costs for R by3(1+log803)<24. The two separation-motion costs are
below2*(401+1/2)log2<604. Thus the endpoint I variations total less
than23056<24000, and |I|<802*7+302<6000 there. The central part
I-d ell is Z_s+d log(pi/2), with sup below5 and total variation below20
by(14). It matches I at the two cutoff points, because ell=0 there,
and its two central limits agree. Therefore

    sup|I-d ell|<6000, Var(I-d ell)<25000.

Combining these with the V bounds proves(15), using pi>3.
The elementary numerical logarithm bounds here follow, for example,
from e>8/3, (8/3)^7>803 and (8/3)^8>1600.

### 4. Interior quadrature, missing cells and actual special rows

The special row set is exactly N1-02's first/last R rows, the two
central rows r=m-1,m, and every collision row. The first/last R rows
have z<delta because n>=10^6. At most four special rows remain in the
interior: two central and at most two collision rows. For every ordinary
interior row approximate the actual row by H(L,v)=A(v)L+W(v)+d ell(v)/pi.
The full ordinary-row error, including endpoint ordinary rows as well,
is bounded by

    E_n+D_n,
    E_n=2(p+q)H_n/n+2am/[n(R-1)],
    D_n=10/n²+20a H_n/(pi n²),                               (16)

exactly by N1-02/N1-05. Use exact polynomial rows on the special set,
so there is no Rhat/r_n error.

Let U be the union of centered cells for the ordinary interior rows and
D=(delta,2pi-delta). For H_reg=A L+W, (15) and BV midpoint quadrature
show that the normalized sample sum differs from integral_U H_reg/pi by
at most(300L+6000)/m. The symmetric difference U triangle D consists
of at most four missing cells and two boundary pieces of combined length
at most h; thus it has length at most5h. Its H_reg integral costs at most
(1500L+20000)/m.

The actual interior special rows are bounded by the polynomial-continuity
row upper in C06-far-full-profile: R_r/n<=A L+V plus their pole-profile
error. Their four normalized norms total at most(1200L+6800)/m plus
their share of D_n. These errors are disjoint from the ordinary shares
in(16), so (6) in that proof still bounds the total by D_n once.

It remains to charge ell, including its missing central cells. Ordinary
sample distances from pi are at least h, since r=m-1,m were excluded;
their cells have distance at least h/2. The variation of ell on the two
truncated halves is at most2log m. Its normalized midpoint error, after
d/pi, is at most log m/(pi m). The exterior boundary pieces have ell=0.
The missing cells have combined length at most4h. The integral of|ell|
over any set of that measure is largest on the interval centered at pi;
it is bounded by

    4h[1+log(pi/(4h))]<=4h(1+log m).

This follows directly by integrating the decreasing function of distance
from pi (or by its interval superlevel sets). After normalization and d/pi
its cost is at most4(1+log m)/(pi m). Since log m<L+1, the two log costs
sum to less than(2L+3)/m.

All terms together prove the absolute interior replacement error

    E_interior<(3002L+32803)/m<3/40=.075,                    (17)

apart from the single shared E_n+D_n budget. The last inequality uses
log(10^6)<14 and monotonicity of(c log n+d)/(n+1) on n>=10^6.
No integral over an uncharged central singularity or collision hole remains.

### 5. Endpoint block and final scalar budget

N1-08, with R=64,delta=1/100, replaces the exact endpoint block E by
B0 L²+b_end L+C_R+c_mesh with error e4. N1-05 charges its omitted
endpoint residual by Q, and (16) already charges the cancellation error.
The interior coefficient integral joins b_end to exactly b_full by the
full-domain computation in C06-far-full-profile. Thus the model is (1),
and its complete absolute error is at most

    e4+Q+E_n+D_n+E_interior.                                (18)

Here Q=(2delta/pi)[7+(p+q)/pi*(5+2log(4pi/delta))]<7/50=.14:
use pi>3,p+q<=2,4pi/delta<1600 and log1600<8.
Also E_n<4*15/10^6+2(1+10^-6)/63<4/125=.032, and D_n<10^-9.

For clarity the small e4 uses N1-08's sharper component formula, not
its coarse K4 coefficient. H_n<=15 at the base in all decreasing ratios.
The finite-row part is at most

    18/10^6+127*[763/10^6+55,770,000/10^12]<.104002.

For the mesh part X=m/(100pi) satisfies
1/(X-1/2)<=101pi/m<318/m and log(X+1/2)<L+1. Also H_R^*<5.
N1-06's formula therefore gives

    e_mesh <=131L/(2m)+[5+(L+1)/2]*318/m
              +[6+(L+1)/2]*318²/(4m²)+13/n+1/(2n²)
            <.004906.

The collision-hole correction in N1-08 is below .000059, since
log(4m/R)<L+1 and its bracket is below7+(2/3)(3+2(L+1)).
Every ratio used decreases from n=10^6, and the n^-2 terms decrease too.
Thus e4<.11. Inserting these bounds and(17) into(18) yields

    |S_n-M_far|<.11+.14+.032+10^-9+.075
               =.357000001<9/25.

This proves (2). The series and finite sums in(5)--(7) retain their fixed
R=64 count, and the exact improper integral has an integrable log by(14),
so (1) is a well-defined count-independent model. QED.

## Checks, limitations and history

The analytic proof is independent of the diagnostic. The preregistered
35-case binary64 run at L=log(10^6) took .385327435CPU-s and returned no
integration warnings; its largest model-minus-corner-polynomial value was
-2.4822305655 at alpha=beta=1/4. Four direct integral controls had maximum
discrepancy1.8796e-9. These are MEASURED observations only; the corner used
there included the limiting constant c and was not a finite-n lower bound.
Source/receipt: ../code/c06_far_profile_diagnostic.py and
../evidence/c06-far-profile-diagnostic.json. The raw18,441B output remains
at its recorded /tmp path; physical archival delivery is not claimed.

The exact model maximum, a finite-n corner lower strong enough for it,
and monotonicity in L are separate C08 obligations. No sampled margin
proves them, and no global n>=10^6 argmax conclusion is claimed here.
Distinct Astra review is needed before this developer claim is published.

2026-11-06, C06 developer, requested Astra ultra under parent's prior
hard-math allocation; runtime metadata unexposed. Rules/input
b6e67b3c78cb668b6d2f9da5a5560537d2960bf3. The follow-up candidate and
error1/2 target were registered in ../ideas/C06-far.md before this proof;
9/25 is the stronger result of the explicit budget. No old proof edited.
