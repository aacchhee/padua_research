# PD-T?argmax-bridge-codex-D20-error — Full-phase regularized hybrid model allowance

ID kind: PD-T. Aliases: global D07 telescope with coarse retained rows;
interior-charge replacement. Split from: D20 far/global7000 target.
Split into: retained rows have their separate D20 result.

## Statement and exact scalar definitions

For every integer n>=32 and every signed phase pair
|alpha|+|beta|<=pi, use the UNCHANGED corrected primitive S_n and
completed D02 model M_infty. Define phases by their separate absolute
values, a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,P=p+q,
d=(q-p)_+. Put m=n+1,L=log n,H=1+L,b=4/pi^2,
r=log(5/2)+1/18 and

    D=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    KD=[352H/(3pi)+2/pi]/n,
    MA=1/pi+4/pi^2,
    g=1+log(2+8m/(3pi)),
    VB=23+[3g+14log m+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg
                                      +4log pi/(pi*m)+16/m,
    E6=(193+21L)/n+21600/n^2,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n^2-1)
             +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    W=[3log m+log2+2log pi+2]/(pi*m),
    Cnew=D+Gg+E6+Mesh+W.

Then throughout the FULL closed signed diamond

    |S_n(psi)-M_infty(psi,log n)|<=Cnew(n)+KD(n)*P.        (1)

Cnew and KD are positive and decreasing for every real n>=32.
Overall status: **PROVED**, developer analytic theorem; distinct review
pending. It is a new error allocation, not a changed D05 formula.

## Exact telescope and source domain

Accepted D05-fixed-special-rows at R2,n>=16 gives
|S-K_fixed|<=E_D04. Its ordinary labels are literally k=2,...,m-2
on each folded side. Accepted D07-global-outer on the FULL closed
signed diamond n>=16 gives |K_fixed-G_n|<=E_global. Accepted
D07-global-mesh, with those same rows/weights and continuous endpoint
constants, gives EXACTLY

    G_n-M_infty=(J6-C2)+Rmesh+(d/pi)Rlog,
    |Rmesh|<=Bmesh, |Rlog|<=Blog.

In particular its Delta_2=E_infty-E_2 has the accepted sign and its
E_2=C2+D0 H2+B0 G2 contains the C2 matched in D20-global-retained-rows.
The endpoint h/g constants are exact convergent constants, with actual
upper ordinary label m-2. The central logarithms use the exact positive-
argument Gamma product. The finite h is pi/m, not pi/n. Thus

    |S-M_infty|<=E_D04+E_global+E6+Bmesh+(d/pi)Blog.        (2)

No fixed-cutoff residue, I_n, old e_mesh, or extra D_pole is present:
those were charges for D05's different strip/interior assembly. Their
role is replaced by D07's complete regularized cell quadrature plus
the exact global mesh identity. E_D04 already pays its own ordinary
pole-profile remainder. D20's row lemma pays the actual six rows.
No collision charge is needed for the literal fixed ordinary set.

## Full-phase majorization of the global quadrature

This step uses D07-global-outer(2), NOT its near-only bound(4).
Its epsilon=3pi/(2m) lies in(0,pi/2), so the chord inequality gives
sin epsilon>=3/m and ell=-log(sin epsilon)<=log(m/3)<log m.
For its entropy, Sbar=1/2+2a/epsilon<=1/2+4m/(3pi) and

    Gpar=p[1+log(1+2Sbar/p)]<=g,

with continuous zero value at p=0. This follows from monotonicity in
p,Sbar>=0: for p>0 the p derivative is
1+log(1+x)-x/(1+x)>0,x=2Sbar/p; the Sbar derivative is nonnegative.
Therefore substituting p<=1,a<=1 gives exactly g, even at phase edges.
The other positive terms obey max(p,q)<=1,P<=2,d<=1,a<=1, whence

    M_A<=MA, V_A<=2MA,
    V_B<=23+[3g+(2+12)log m+26+20+2log2]/pi=VB,
    Q(P,2h)<=Qg, C_B<8.

Insertion in the FULL D07 formula gives E_global<=Gg. This is a
majorization of a previously valid scalar error formula after applying
the theorem at actual phases; no physical theorem is invoked at
fictitious independent values p=q=a=d=1,P=2.

The unchanged D04 expression with H_n<=H gives E_D04<=D+KD*P.
D07/N1's full-phase bounds |U0|<=8,B0<=b,|D0|<=4,|Z_n|<=5,
|h2(t)+h2(1-t)|<=2r give Bmesh<=Mesh. For completeness
D0=U0/pi+B0 log pi, Z_n=D0-B0 log(m/n), so the last absolute
bounds follow already from pi>3,pi^2>8,log pi<6/5,n>=32.
The h2 bound is N1-06's H_R^* at R2,t in[0,1]. Finally
(d/pi)Blog<=W. Combining these inequalities with(2) proves(1).

## Fresh real-n monotonicity

D,KD,Mesh and W have exactly the positive expressions checked in the
accepted D16-phase-allowance monotonicity proof on real n>=32; this
invokes its scalar proof, not its finite n10000 application. E6 has
derivative [21-193-21L]/n^2-43200/n^3<0.

For clarity expand only Gg into positive terms:

    Gg=[7MA*L+111/2
          +(63+log2+4log pi+7log m+16log(2m)+(3/2)g)/pi]/m.

L/m decreases since 1+1/n-L<0 at n>=32. log m/m and
log(2m)/m decrease there. If c=8/(3pi), then
m*g'=cm/(2+cm)<1<g, so g/m also decreases. Every remaining
coefficient is positive and independent of n. Hence Gg and Cnew
decrease on the entire claimed real domain.

## Scope, evidence and history

This global absolute theorem retains actual polynomial values on the
six rows, weighted Phi(integer)=1 on ordinary collisions, all closed
phase edges,a=0 and separate evenness without exchanging n,m. It
does not assert a full phase-relative finite remainder. No numerical
premise is needed for(1); the separate far target requires its own
frozen endpoint budget. No old source/data/formula is changed.
2026-11-06, parent-assigned Codex Sol xhigh; rules/input
ca8d52aa2a48c941473846ab884cccb25f1bdb9f, serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct review [D20](../independent-checks-D20-global-hybrid.md), SHA256 `e1284bce7f95e332cba284cbafa03c7667772d7518076aea3d3596331cb82398`, accepts all four split scopes, including exact global argmax at every n>=7000. Root adopts the result: far gap3/40, accepted D18 near gap1/400 and D17 actual-corner loss1/8. The complete closed physical cover and both parity equality sets are retained. This dated closure preserves reviewed text and first scalar evidence; final Claude audit remains separate.
