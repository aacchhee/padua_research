# PD-T?argmax-bridge-codex-D37-wide — Fully charged actual-origin allowance through radius one

ID kind: PD-T. Aliases: wide D22/D25 telescope; radius-one shifted outer
and fixed-row allowance. Split from: D37 prospective1024 application.
Split into: none. The physical comparison is the separately owned lead
application; the fully vanishing D13 relative target remains OPEN.

## Exact statement and objects

For EVERY integer n>=32 put m=n+1,L=log n,H=1+L. Initially take
alpha,beta>=0 with rho=alpha+beta<=1, and put

    a=(cos alpha+cos beta)/2, u=1-a,
    p=sin alpha, q=sin beta, P=p+q, d=(q-p)_+,
    ce=cos(rho/2), cd=cos((alpha-beta)/2), a=ce*cd.

Use the SAME corrected polynomial and actual primitive as D05/D22:

    D_n(v1,v2)=sum_(i+j<=n) h_i h_j cos(i*v1)cos(j*v2),
    h_0=1, h_i=2 (i>0), Gpoly=D_n-cos(n*v1),
    delta_r=(1-r) mod2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n, v_r=(r*pi+beta)/m,
    R_r=sum_(k=0)^(n-1)|(-1)^delta_r Gpoly(u_rk,v_r)/2|,
    S_n=(nm)^(-1)sum_(r=0)^(2m-1)R_r.

Let M_infty be D02's unchanged completed model. The origin is the SAME
finite S_n(0)=Lambda_c(n). Let E0(n) be D16's unchanged complete
ACTUAL-origin allowance, |S_n(0)-M_infty(0,L)|<=E0(n). Define

    Cext=23/n+204/n^2+40H/(pi*n^2),
    Kext=[8H+20L+292/3]/n+4/n^2.

Then throughout the CLOSED signed diamond rho=|alpha|+|beta|<=1,

    S_n(phi)-S_n(0)
      <=M_infty(phi,L)-M_infty(0,L)+Cext+Kext*rho+uE0.       (1)

Signed objects use the existing separate-absolute-phase convention,
without interchanging the unequal n,m meshes. Both axes, both parities,
all actual polynomial collisions and rho=1 are included. Cext,Kext are
positive and decreasing for every real n>=32.

Overall status: **PROVED**, complete analytic developer proof below;
distinct independent review of THIS new domain is required before
adoption. D35's frozen ordinary perturbation theorem is an explicit
dependency; root reported its distinct acceptance during this block in
review SHA256
`781e1077eb52c87e4f9f1718a0d658c3f8a342b0db3733c15c8ac1851c31083e`.
No scalar premise, source/cap change or new onset is claimed here.

## 1. Match the exact operators before widening estimates

Use D05's fixed six labels

    A6={0,1,2m-2,2m-1,m-1,m}, O6={0,...,2m-1}\A6,

the same weighted K_fixed and Delta_2=E_infty-E_2, D07's intermediate
Gint, and the SAME J6,C2,Rmesh,Rlog. The notation Gint distinguishes
that intermediate from the polynomial Gpoly. Set

    Erow=S_n-K_fixed, Eout=K_fixed-Gint, Eret=J6-C2,
    delta_a X=X(phi)-aX(0), E=S_n-M_infty.

D07's exact full-domain identity, with ordinary index k=2,...,m-2,
gives literally

    delta_a E=delta_a Erow+delta_a Eout+delta_a Eret
                                      +delta_a Rmesh+(d/pi)Rlog.  (2)

No old error estimate is extended by this identity. The proof below
establishes the following NEW bounds on the larger domain:

    delta_a Erow<=4a/n+20/n^2+40aH/(pi*n^2)
                                      +rho[8H+10]/n,           (3)
    delta_a Eret<=[19a+P(12+L)]/n+(184a+4P)/n^2,              (4)
    |delta_a Rmesh|+(d/pi)|Rlog|<=rho(L+7/3)/n,                (5)
    |delta_a Eout|<=rho(18L+73)/n.                            (6)

The elementary new domain constants, used repeatedly, are

    ce,cd>=1-(1/2)^2/2=7/8,
    a>=49/64>=3/4, P<=rho<=1, 2a-P>=17/32,
    t=beta/pi<=1/pi<1/3.                                    (7)

These ensure positive weights but do not assume absence of central
numerator roots. All endpoint values use the original linked polynomial
limits or complete weighted continuations.

## 2. The endpoint reference, including its full infinite tail

Retain EXACTLY D13's J=floor(n/2), left j=2,...,J and right
j=3,...,J. Put x=alpha/pi and s=+t on the left, -t on the right.
Use the same folded z=pi(j+s)/m, actual offsets

    theta_+/−=(1-s+/−x)/2+(j+s)/(2m),

and the same Xi,Theta,T0,Delta_2 and Qep. D05-relative-halfline's
actual-offset result already has domain rho<=pi/2, so it applies here:
all these offsets are strictly in(0,1), z<=pi/2, no pole is sampled,
and the COMPLETE (T0-Theta) relative sum costs at most2a rho H_n/n.
That is an application within its stated domain, not a widened D13
quantifier. In particular j+s<m/2 since j<=n/2 and |s|<1/3<1/2.

For the displaced digamma part write exactly as in D13

    nu=j+s, y_+/−=j+(1+s+/−x)/2, delta=nu/(2m),
    B=psi(y_+)+psi(y_-)-2log nu,
    U=psi(y_+-delta)-psi(y_+)+psi(y_--delta)-psi(y_-)-2log(n/m),
    tau=(pi*nu/(2m))*cot(pi*nu/(2m)), c=2/pi^2,
    e_j=c[(tau-1)B/nu+tau U/nu],
    Theta_j/(nm)-Xi_j=a e_j.

On the straight phase path from0 to(x,s), the NEW bounds are

    5j/6<=nu<=7j/6, y_+/−>=j+1/3,
    delta<1/4, y_+/−-delta>=j, 0<pi*nu/(2m)<pi/4.

Thus the positive digamma derivative series still gives
psi'<=3/(2j), |psi''|<=2/j^2. D04's full-domain |B|<=2/nu and
|U|<=5/n apply, and direct differentiation gives, with b=x+|s|,

    |dot B|<=4b/j, |dot U|<=3b/(m*j).

For the first inequality, |partial_s B|<=3/(2j)+2/nu<=4/j;
the x derivative is <=3/(2j). For U, each derivative difference is
<=2delta/j^2, giving |partial_x U|<2/(mj) and
|partial_s U|<3/(mj). The phase-independent -2log(n/m) is retained.
The elementary prefactor bounds, valid because nu<m/2, remain

    |(tau-1)/nu|<=4nu/m^2, |[(tau-1)/nu]'|<=12/m^2,
    |tau/nu|<=1/nu, |(tau/nu)'|<=3/nu^2.

Consequently the NEW combined derivative bound is

    |dot e_j|<=c b[29/(m^2*j)+19/m^2+22/(n*j^2)+4/(m*j^2)].

Indeed these coefficients bound respectively24/nu,16nu/j,
15/nu^2 and3/(nu*j) using5j/6<=nu<=7j/6. The two finite label
sets have fewer than m members, combined harmonic sum<=2H_n, and
combined inverse-square sum<=3/2. Also H_n<=1+log n<=n/4 for n>=32:
the last difference increases there and log32<4. Therefore

    sum |e_j(x,s)-e_j(0,0)|
       <=c b[58H_n/m^2+25/m+33/n]
       <=(145/27)rho/n<8rho/n.                            (8)

The infinite tail starts at j=J+1>=17 on BOTH sides. Its exact phase
derivative satisfies

    |d(Xi_j/a)/dlambda|<=c b[4/(j*nu)+2/nu^3]<=6c b/j^2.

For j>=3 the last coefficient is at most24/5+432/(125j)<=744/125<6.
Uniform summability justifies integration; the two tails cost
12a c b/J<=8a rho/(9J)<=2a rho/n, as J>=(n-1)/2,n>=32.
Combine this with (8) and the actual half-line increment to obtain

    |delta_a Qep|<=a rho(2H_n+10)/n.                       (9)

The entire Delta_2 series and the fixed starting indices are retained.

## 3. Central reference complement and complete row increment

The complementary central reference labels are exactly left/right
j=J+1 onward, with total count2n-2J-1<=n as in D22. At the NEW phase
range their folded z obeys

    z>=pi/2-1/m,
    sin^2(z/2)>=(1-sin(1/m))/2>=(1-1/m)/2.

The actual symmetric-reference error obeys |T0_r|<=a/sin^2(v_r/2).
Therefore its normalized central sum Zcen satisfies

    |Zcen(phi)|<=2a/(m-1)=2a/n,
    |Zcen(0)|<=2/m, |delta_a Zcen|<=4a/n.             (10)

The origin ordinary rows are collision-free by the same coprime n,m
odd-board argument as D22; its actual origin is unchanged.

At a collision-free phase D04's exact decomposition of Erow holds.
D35 gives the ordinary perturbation6P H_n/n; its origin value is
EXACTLY zero. The two weighted-pole absolute errors remain
20/n^2+40aH/(pi*n^2). Adding (9),(10) proves (3) there.
D05 proves continuity of COMPLETE Erow on the full closed diamond,
and all collisions lie on finitely many affine lines. Pass to a dense
collision-free sequence only in that complete expression and (3).
No individual reference sample or unweighted pole is assigned a
polynomial-collision value. This proves (3) everywhere required.

## 4. Rebuild all six retained rows on the new domain

For the four endpoint rows use the SAME C2 as D30/D07, namely

    C2=ell_0(beta)+ell_1(alpha,beta)+ell_1(alpha,-beta)
                                                  +ell_2(alpha,-beta),
    ell_0=sinc beta,
    ell_r(alpha,b)=sin b/(r*pi+b)
        +8a sum_(j=-r+1,-r+3,...,r-1)
                             1/[(r*pi+b)^2-(j*pi+alpha)^2].

Here sinc0=1. With w=r*pi+b,z_j=j*pi+alpha,mu=n/m,eta=1/m,
the exact finite identities are the original corrected-polynomial ones:

    F_j=[a(1+cos(w/m))-(p/2)sin(z_j/n)+(sin b/2)sin(w/m)]
                                      /[cos(z_j/n)-cos(w/m)],
    sum_j F_j=n[a-(sin b/2)cot(w/(2m))].               (11)

For(r,b)=(1,beta),(1,-beta),(2,-beta), one has0<w<7. The COMPLETE
numerator in2F is >=2a-P>=17/32. For the proposed positive samples
j=0,0,-1,1, respectively, |z_j|<pi+1<17/4, and, for k=r+/−j in{1,3},

    w+/−z_j>=k*pi-rho>(17/8)k,
    mu*w+/−z_j>(17/8)k-7/33>(19/10)k.              (12)

Here pi>25/8 and505/264>19/10 justify the last two bounds. The first
excluded sample satisfies |z_j|>w>mu*w because pi>rho; all further
ones are excluded. Thus those are the COMPLETE positive sets, they
belong to the actual half-open n-point mesh, and no endpoint collision
occurs. For r0 all samples are negative and the same exact linked
formula is R0/(nm)=sinc(beta)*tau(beta/(2m))-a/m, with tau0=1;
at beta0 its finite polynomial value is n(m-a).

Use D30's exact algebraic finite-h identity, now on the newly proved
sign sets, with D=w^2-z^2,Dh=mu^2*w^2-z^2,

    K=sinc((z/n+w/m)/2)*sinc((z/n-w/m)/2),
    Hh=(1+cos(w/m))/(2K), g=-p sin(z/n)+(sin b)sin(w/m),
    e_r=R_r/(nm)-ell_r
       =-a/m+(sin b/w)[tau(w/(2m))-1]
        +8a sum[mu/Dh-1/D]+8mu*a sum(Hh-1)/Dh
                                      +2mu sum g/(Dh*K).       (13)

The four -a/m terms combine with the nonnegative displacement before
taking absolute values. Indeed

    mu/Dh-1/D=(eta/2)sum_+/− 1/[(mu*w+/−z)(w+/−z)],
    sum_samples 1/Dh<=(100/361)(8/3)=800/1083,
    S:=sum_samples,signs 1/[(mu*w+/−z)(w+/−z)]
                              <=(80/323)(56/9)=4480/2907<2.

Their combined signed contribution is(-4a+4aS)/m, with absolute
value<=4a/m. For |z/n|<17/(4n),w/m<7/n and n>=32, the sinc bounds give

    49/50<K<=1,
    |Hh-1|<=[(17/4)^2/12+49/3](50/49)/n^2<19/n^2.

Consequently the Hh error is at most121600a/(1083n^2)<113a/n^2.
Since |g|<=7P/n, its total error is at most
560000P/(53067n)<11P/n. The three nonzero w sum to4pi-beta.
On the NEW beta interval0<=beta<=1, sin beta>=5beta/6 and therefore
beta^2<=6q/5; one MUST NOT reuse beta^2<=q. The four tau errors
thus cost at most[q(4pi-beta)+beta^2]/(4m^2)<4P/n^2.
Equations(11)--(13) prove the fresh endpoint bound

    |Jend-C2|<=(4a+11P)/n+(113a+4P)/n^2.                 (14)

For the actual two central rows the full weighted-pole bound from C06
is valid at every interior angle, including v=pi and collisions by
complete-expression continuity. Their angles satisfy|v-pi|<=pi/m,
so sin(v/2)>99/100 and |cot(v/2)|<=pi/m. Using (7),

    ce+cd=a(1/ce+1/cd)<=16a/7,
    V(v)<=(3200/693)a<(14/3)a,
    |C|+|D|<=P/2+a*pi/m.

Exactly as a weighted-row SUM, rather than a central-integral substitute,

    Jcen<=28a/(3m)+2PL/(pi*m)+4aL/m^2
                                  +5P/(m*n^2)+10pi*a/(m^2*n^2)
          <=[11a+P(1+L)]/n.                            (15)

The last line uses L<=n/4 and the same elementary residual inequality
4L/m^2+10pi/(m^2n^2)<=1/n. Jcen>=0 by its actual definition.

At the ACTUAL origin the old D07 endpoint bound remains applicable:
|Jend(0)-C2(0)|<=4/n+71/n^2. Subtract a times that value in (14).
For the central pair retain the sign -aJcen(0)<=0 and use (15) only
at the phase. This gives (4), with184=113+71. No origin central norm
has been omitted from an absolute estimate.

## 5. The scalar singular-mesh increment on rho<=1

D13's exact algebraic remainder identity and paired h/g derivative
series are defined for0<=t<=1; our t<=1/pi is inside that domain.
The actual upper index remains n=m-1 and the exact log(m/n) shift
is retained. Write B=4a/pi^2,D=U0/pi+B log pi,eps0=log(m/n),
Z=D-B eps0 and use D13's H_j(t),Q_j(t). Its exact subtraction is

    delta_a Rmesh=-B eps0[H_2(t)-H_2(0)]
       -aZ0[H_n(t)-H_n(0)]-B[Q_n(t)-Q_n(0)]
                                -(D-aD0)[H_n(t)+2L].         (16)

The paired derivative bounds and |H_n(t)+2L|<1/n^2 use only0<=t<=1,
n>=32. The only old near-domain constant needing replacement is
|D-aD0|: the endpoint numerator formula and Lip(f)<=6/pi give

    |U0-aU00|<=12rho/pi+rho^2<=5rho,
    |D-aD0|<=5rho/3.

With B<=1/2,|Z0|<5, equation(16) now yields

    |delta_a Rmesh|
       <=rho[1/(3n)+(L+9)/(6(n-1)^2)+5/(3n^2)]<rho/(2n).

For n>=32 its coefficient after multiplying by n is bounded by
1/3+13/168+5/96<1/2. The old central logarithmic bound is full-domain:
|Rlog|<=[3log m+log2+2log pi+2]/m, giving
(d/pi)|Rlog|<=rho(L+11/6)/n. These prove (5), with equality zero
at rho0 by the exact subtraction.

## 6. Widen the exact shifted regular outer operator

Use EXACTLY D25's F_L,F_R, which are the following algebraic full-domain
D07 profiles evaluated on our new phase domain. For v_L(z)=z and
v_R(z)=2pi-z set

    C(v)=(p-q-2a cot(v/2))/4, D(v)=(p+q+2a cot(v/2))/4,
    A(v)=2(|C(v)|+|D(v)|)/pi,
    I_s(z)=integral_0^pi
       [|C(v_s)cot x+D(v_s)cot(x+v_s)|
                      -|C(v_s)cot x|-|D(v_s)cot(x+v_s)|]dx,
    B(v_s(z))=N_s(z)/(2sin(z/2))+I_s(z)/pi,
    F_s(L,z)=A(v_s(z))*L+B(v_s(z))
             -[U0+(4a/pi)(L+log z)]/z-(d/pi)log(pi-z).

Here N_s and U0=N_s(0) are explicitly given in section6a below. Every
Phi0 value has its weighted periodic continuation and the cancellation
integral is the ordinary bounded integral; arbitrary values at finitely
many poles do not affect it. The exact Q operator is

    h=pi/m, Q_tau[f]=(1/m)sum_(k=2)^(m-2)f(h(k+tau))
                                              -(1/pi)integral_0^pi f,
    Eout=Q_t[F_L]+Q_(1-t)[F_R], F0=F_L(0)=F_R(0),
    W_s=F_s(phi)-aF0.

The exact identity is still

    delta_a Eout=Q_t[W_L]+Q_(1-t)[W_R]+Shift,
    Shift=(a/m)sum_(k=2)^(m-2)
      [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))].       (17)

The sum shift is NOT zero by symmetry. The actual cells have initial
missing lengths h(3/2+t),h(5/2-t), total4h, and central lengths
h(3/2-t),h(1/2+t), total2h. Since0<=t<1/3, every retained cell
lies in[epsilon,pi-epsilon],epsilon=h/2; all initial gaps are<pi/4
and all central gaps<pi/2. Put ell=-log(sin epsilon)<=log m.

The coefficient-of-L identities hold directly on the new domain. Put
T=2a cot(z/2)>=0 and f_s=A(v_s)-4a/(pi*z). The exact absolute-value
formulas give A(v_L)=max(p,q+T)/pi and
A(v_R)=max(p,|q-T|)/pi. At the origin aA0=T/pi. Hence

    pi(f_L-a f0)=max(q,p-T),
    pi(f_R-a f0)=max(-q,p-T,q-2T).

Both increase with z; their combined variation is2max(p,q)<=2rho
and each sup in absolute value is<=rho. Midpoint variation plus the
EXACT total6h gap length therefore gives the contribution

    7rho L/(pi*m).                                      (18)

### 6a. Weighted periodic numerator, with its derivative atoms

Let f(x)=Phi0(1/2+x/(2pi)). The inherited global bounds are
|f|<=4,Lip(f)<2, |f''|<1 away from odd multiples of pi, and the
periodic variation of f' INCLUDING its atoms is<7. With ephase=rho,
delta=alpha-beta and r=ce+cd-2a,

    N_L=ce f(z+delta)+cd f(z-ephase),
    N_R=ce f(z-delta)+cd f(z+ephase), N0=2f(z),
    V_s=N_s-aN0, V0=U0-aU00,
    0<=r<=(ephase^2+delta^2)/8<=rho^2/4.

Translations and the residual coefficient give the NEW estimates

    |V_s|<=4rho+rho^2<=5rho,
    |V_s'|<=2rho+rho^2/2<=(5/2)rho  (0<=z<=pi/2).       (19)

All shifted arguments for the second estimate lie strictly inside
(-pi,pi), since pi/2+1<pi. Hence no derivative atom is crossed there.
At z0, evenness gives f'(0)=0 and |f(b)-f(0)|<=b^2/2 for|b|<=1.
This yields the sharper endpoint estimate

    |V0|<=ephase^2+delta^2<=2rho^2<=2rho.                 (20)

On I=[pi/2,pi], the BV translation argument integrates the measure
Df' over the shifted intervals. Their enlargement has length at most
pi/2+2<2pi, so its variation is at most one periodic total. Thus
Var_I[f(.+b)-f(.)]<=7|b| now for|b|<=1 as well, with every atom
included. Therefore

    Var_I V_s<=14rho+7rho^2/4<16rho.                    (21)

The exact regular pole difference is

    Pdiff_s=[V_s(z)-V0]/z+V_s(z)d0(z),
    d0(z)=1/(2sin(z/2))-1/z, 0<=d0<=1/5, d0 increasing.

On[epsilon,pi/2], (19) bounds quotient variation by5rho log m;
product variation is<=2rho and the whole sup is<=4rho. On the other
half use Pdiff_s=V_s/(2sin(z/2))-V0/z. Its first weight has sup<3/4
and variation<1/4; the second has sup<2/3 and variation<1/3. Thus
(19)--(21) give variation<(12+5/4+2/3)rho<14rho and sup<6rho.
Summing both sides, the total variation is<=rho(10log m+32).
Midpoint error costs half this divided by m. Initial/central gaps cost
16rho/m and12rho/m by their EXACT total lengths. Hence

    |Q_t[Pdiff_L]+Q_(1-t)[Pdiff_R]|
                                 <=rho[5log m+44]/m.        (22)

### 6b. Cancellation, including all moving roots and both gaps

Retain D25's EXACT generic continuous formula

    J(u0,s,e)=2(s-u0)_+ log(sin e)+R(u0,s,e),
    |R_s|<=log((u0+s)/|u0-s|),
    0<=R_e<=2u0 cot e for s>u0, R_e=0 for s<=u0,
    u0=p/2.

The log singularity at s=u0 is locally integrable and the original
root/no-root formulas match continuously there. For u0=0,R=0.

On0<z<=pi/2, s_L=a cot(z/2)+q/2 and
s_R=a cot(z/2)-q/2>0. The NEW root-free check is

    s_R sin z>=a-q/2>=u0+(a-P/2)>=u0+17/64.

The other side is larger. Thus the exact same identities hold:
I_L-aI_L(0)=q log(sin z), I_R-aI_R(0)=-q log(sin z).
After subtracting d log(pi-z), their combined variation on the
truncated initial half is at most2rho ell+2rho.

On the central half write e=pi-z,s0=a tan(e/2),
s_L=s0+q/2,s_R=|s0-q/2|. The cancellation difference is exactly

    Cdiff_s=I_s-aI_s(0)-d log(pi-z)
       =R(u0,s_s,e)+b_s(e)log(sin e)+d log(sin e/e),
    b_L=max(q-p,-2s0)-d,
    b_R=max(-p-q,q-p-4s0,-2s0)-d.

The b functions decrease from0. Their combined sup and variation are
each<=3rho and each individual sup<=2rho; these algebraic max bounds
require only p,q>=0. The s curves have at most three monotone pieces,
with0<=s<=S=a+q/2<=3/2. The parameter-integral charge is now bounded by

    G=p[1+log((S+p/2)/(p/2))]<=p[1+log(4/p)].            (23)

If rho<=epsilon^2/8, then for EVERY e>=epsilon up to pi/2,

    [a tan(e/2)-q/2]sin e
       >=(3/4)(e^2/5)-rho/2
       >=7e^2/80>=rho/2>=u0.                         (24)

Here1-cos e>=2e^2/pi^2>e^2/5, and rho<=e^2/8. The bracket is
positive. This proves the actual root-free condition, which is >=u0,
NOT the unnecessarily stronger >=rho. In this case R=2u0 log(sin e)
and its two-side variation is<=2p ell.

If rho>epsilon^2/8, use p log(rho/p)<=rho/exp(1)<rho/2 in (23):

    G<=rho[3/2+log(4/rho)]
      <=rho[11/2+2ell],                              (25)

since log32<4 and log(1/epsilon)<=ell. Thus the original D25 total
parameter/separation charge for R, rho[33/2+8ell], remains valid in
BOTH regimes. The b products cost6rho ell and the two d terms cost
rho. Together with the initial half, the full two-side variation of
Cdiff is<=rho[39/2+16ell], with all max/root transitions included.

The removed intervals must also be integrated. Initially the exact
no-root formula gives |Cdiff_s(z)|<=rho[log(pi/(2z))+log pi].
Centrally, repeat (24)--(25) at epsilon=e. Using
|R(u0,0,e)|=p log2<rho and integrating (23) gives the SAME bound
|Cdiff_s(pi-e)|<=rho[7+4ell_e],ell_e=-log(sin e).
These integrable envelopes, with the initial total4h and central
total2h, give exactly the complete D25 cancellation charge

    |Q_t[Cdiff_L/pi]+Q_(1-t)[Cdiff_R/pi]|
                       <=rho[175/4+20log m]/(pi*m).       (26)

For clarity, its midpoint part is rho[39/4+8log m]/(pi*m),
its initial-gap part is <=4rho(3+log m)/(pi*m), and its central-gap
part is <=rho[22+8log m]/(pi*m). Their sum is (26). No endpoint
value is substituted for an unbounded but integrable gap profile.

### 6c. The remaining actual-origin mesh shift

D25's explicit F0 and its derivative proof use no phase assumption.
Every path of an argument in Shift, now t<=1/pi<1, still lies in
[2h,pi-h]. Its absolute-continuity derivative bound is

    |F0'|<=(4/3)L+(2/3)log m+20/3.

Each argument moves by beta/m, so the unchanged fully paid shift is

    |Shift|<=rho/m[(8/3)L+(4/3)log m+40/3].             (27)

This is the shift of the actual origin mesh; it is not inferred from
the variation of W and it contains no duplicate gap integral.

### 6d. Add the complete outer charges

The exact W_s is its L coefficient plus Pdiff_s+Cdiff_s/pi. Equations
(17),(18),(22),(26),(27), using pi>3, give

    |delta_a Eout|
       <=rho/m[5L+13log m+863/12]
       <=rho/n[18L+73].                              (28)

Indeed log m<=L+1/32 and863/12+13/32<73. This proves (6) on the
closed larger domain. At rho0 the exact identity is zero. Periodic
weighted Phi and the continuous J formulas include all cusps, roots
and coefficient switches; actual polynomial collisions never acquire
separate unweighted pole values.

## 7. Assemble, convert the actual origin, and record the limits

Insert (3)--(6) in the EXACT telescope(2), use a<=1 and P<=rho.
The constants are

    (4+19)/n+(20+184)/n^2+40H/(pi*n^2)=Cext.

The linear terms are

    [8H+10+(12+L)+(L+7/3)+(18L+73)]/n+4/n^2
                               =[8H+20L+292/3]/n+4/n^2=Kext.

Finally E(phi)-E(0)=delta_a E-uE(0), and the SAME D16 origin
allowance gives -uE(0)<=uE0. This proves (1). The positive inverse
powers and H/n^2 in Cext decrease for n>=32. Write
Kext=[28log n+(8+292/3)]/n+4/n^2; its constant exceeds28, so its
derivative is negative already for n>=1.

The ordinary coefficient6 depends on D35-ordinary-perturbation, frozen
SHA256 `9b6a4136a16f1b26d0dd41fb8eff97d606e7c2c9675df78c9e73f79cc05e90d1`.
Other dependencies are the EXACT D04/D05/D07 identities; the scalar
D05 half-line theorem within rho<=pi/2; D13 derivative-series and
digamma algebra; D25's generic J/BV formulas and phase-independent F0;
D30's finite endpoint algebra; and D16's actual-origin allowance.
Every domain-sensitive estimate is rebuilt above; old frozen files
are unchanged. The fixed six rows, highest corrected mode, all
endpoint removals, unequal meshes, central reference complement,
weighted-pole errors and full origin conversion are retained.

The constant Cext is nonzero; D13's complete vanishing relative
remainder remains OPEN. No physical defect, corner, far comparison,
degree threshold, scalar endpoint or global theorem follows from this
operator support alone. No numerical/scalar/native/phase/root/board/
quadrature/source job was run. Written 2026-11-06 in the bounded D37
helper block, requested Astra ultra with serving metadata unexposed,
rules/input eb9329c28be18d77eeb817f634202d626ee11f92. The attempt records
gate, route dispositions and frozen review boundary; distinct review
is required before parent adoption.


## Current result and root final adoption — 2026-11-06

Current status: **PROVED** at this record's stated support/assembly scope. Final [D37 review](../independent-checks-D37-global1024.md), SHA256 `2ad8f232aa88bc15e360be7b61c1c110dd1f9ff2f667850167c7d456d57bcda5`, accepts the unchanged five paper scopes and sole primary/fresh independent1024 endpoints. All59intervals+pi,16domains,33controls,60containments pass. Root adopts exact two-corner global argmax EVERYintegern>=1024, near noncorner gap1/200 and complete closed far gap3/100, with accepted D27 actual-corner loss1/8. The harmless intermediate zero-phase strict-display NOTE W0 and explicit zero cases remain in the review. Historical conditional/OPEN endpoint wording above is preserved; no scope below1024 or minimal-onset claim follows. Final Claude audit remains separate.
