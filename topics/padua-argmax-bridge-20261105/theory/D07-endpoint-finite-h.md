# PD-T?argmax-bridge-codex-D07-end — Small R2 endpoint finite-h allowance

ID kind: PD-T. Aliases: four positive samples; paired signed-displacement
bound; short finite endpoint comparison. Split from: D07 six retained
rows. Split into: none.

## Statement and status

Let integer n>=32, m=n+1, alpha,beta>=0, alpha+beta<=1/2, and

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta, P=p+q.

Use exactly D05-fixed-special-rows.md's corrected polynomial G_n,
actual signed row values F and absolute row norms R_r. In particular
G_n=D_n-cos(nu), with the exceptional highest first-coordinate mode
retained. Define

    J_end=[R_0+R_1+R_(2m-2)+R_(2m-1)]/(nm),
    C2=ell_0(beta)+ell_1(alpha,beta)+ell_1(alpha,-beta)
                                           +ell_2(alpha,-beta),
    ell_0(beta)=sin(beta)/beta, ell_0(0)=1,
    ell_r(alpha,b)=sin(b)/(r*pi+b)
           +8a sum_{j=-r+1,-r+3,...,r-1}
                    1/[(r*pi+b)^2-(j*pi+alpha)^2].

This C2 is exactly N1-07/C08's C_R at R=2, not a new reference.
On the stated near-phase domain its displayed nonzero-row denominators
are positive; the only remaining linked limit is ell_0(0)=1. Then

    |J_end-C2| <= (4a+7P)/n+(71a+4P)/n^2.             (1)

For signed phases define J_end and C2 by their values at the separate
absolute phases, as in the fixed-row model. Then (1) extends to
|alpha|+|beta|<=1/2. This is the reflected model convention, not a
claim about unreflected fixed row labels at negative beta. No n/m mesh
exchange is used.

Status: **PROVED**, analytic developer result, distinct review pending.
The exact short-sign formula is inherited N1-09, not a new result.
The new claim is the explicit small-R allowance (1). No numerical
calculation, fitting, native job or implementation is a premise.

## 1. Inherited exact finite row and sign set

For signed b=beta or -beta, put

    w=r*pi+b, z=j*pi+alpha, u=z/n, v=w/m,
    F_j=[a(1+cos v)-(p/2)sin u+(sin b/2)sin v]
                                           /(cos u-cos v),
    T_r=n[a-(sin b/2)cot(w/(2m))].

Use (r,b)=(1,beta),(1,-beta),(2,-beta). N1-09 proves that the
complete numerator, multiplied by two, is at least 2a-P>0 whenever
0<=v<=pi/2, and that the positive-denominator mesh indices are exactly
j=-r+1,-r+3,...,r-1 when n>=8R. Here R=2 and n>=32 satisfy those
hypotheses. Thus these three index sets are respectively {0},{0},
{-1,1}. There are no endpoint collisions on this near-phase domain.
The whole signed-row identity and the absolute rows are exactly

    sum_j F_j=T_r,
    R_r^(b)=-T_r+2 sum_{j in positive set}F_j.        (2)

The right rows are the original rows 2m-r by evenness in v.
For the closest row N1-09 gives

    R_0/(nm)=sinc(beta)*tau(beta/(2m))-a/m,
    sinc y=sin y/y, sinc 0=1,
    tau y=y cot y, tau 0=1.                          (3)

In particular at beta=0 its signed row is n(a-m), so its absolute
row is n(m-a). Setting sin(beta)*cot(beta/(2m)) to zero would give
the wrong row. Formula (3) retains the linked polynomial limit.
These identities use four positive samples in total; their bounded
expression count was already part of N1-09/12.

## 2. Exact error identity and elementary denominators

Put h=1/n, mu=n/m, eta=1/m and, on each of the four positive samples,

    D=w^2-z^2, D_h=mu^2*w^2-z^2,
    K=sinc((u+v)/2)*sinc((u-v)/2),
    H=(1+cos v)/(2K), g=-p sin u+(sin b)sin v.

Cosine factorization gives cos u-cos v=h^2 D_h K/2. Consequently
subtracting the displayed ell_r from (2)/(nm) gives the exact identity

    e_r=-a/m+(sin b/w)[tau(v/2)-1]
          +8a sum_j[mu/D_h-1/D]
          +8mu*a sum_j(H-1)/D_h
          +2mu sum_j g/(D_h K).                     (4)

For r=0, its corresponding error is

    e_0=-a/m+sinc(beta)[tau(beta/(2m))-1].            (5)

Identity (4) is the same finite-h identity as C05-finiteh-endpoint-
increment.md, now bounded directly on the four R2 samples. Its
reciprocal displacement is exactly

    mu/D_h-1/D
       =(eta/2)[1/((mu*w-z)(w-z))
                           +1/((mu*w+z)(w+z))].    (6)

One verifies (6) by the two linear partial fractions of 1/(w^2-z^2).
It is nonnegative here.

For either sign put k=r+/-j, so the possible k are 1 and 3.
Using 25/8<pi<22/7, alpha+|b|<=1/2, w<7 and m>=33 gives

    w+/-z >=k*pi-1/2 >(21/8)k,
    mu*w+/-z=(w+/-z)-w/m >(12/5)k.                 (7)

For the second inequality use 21/8-12/5=9/40>7/33.
In particular all D and D_h are positive, uniformly at both axes.
Also |z|<4, |u|<4/n, 0<v<7/n. The two sinc arguments therefore
have magnitude <11/(2n)<=11/64<1/5. Since sinc y>=1-y^2/6,

    49/50<K<=1,
    sum_{four positive samples}1/D_h
                     <=(25/144)(1+1+1/3+1/3)=25/54. (8)

## 3. Join the four signed terms to the displacement

The sum of reciprocal products on the right of (6), over both signs
and all four samples, is bounded by

    (10/63)[2+2+(2+2/9)]=560/567<1.                 (9)

Indeed (7) gives the product lower (21/8)(12/5)k^2=(63/10)k^2.
The k lists are two copies of (1,1), followed by (1,3) and (3,1).
Thus the total displacement term in (4) lies between zero and 4a/m.
The four signed terms from (4)-(5) total exactly -4a/m. Their SUM
therefore has absolute value at most 4a/m<=4a/n. Bounding these
terms separately would lose this saving.

## 4. Bound the remaining geometry and sine terms

For |y|<=pi/4,

    0<=1-tau(y)<=y^2.

For y>=0 this follows from sin y-y cos y<=y^3/3 and
sin y>=2y/pi; evenness gives negative y. The three nonzero w values
sum to 4pi-beta. Also beta^2<=sin beta=q for 0<=beta<=1/2, by the
sine chord and pi<4. Therefore all tau terms in (4)-(5) together cost
at most

    [q(4pi-beta)+beta^2]/(4m^2)<=4P/n^2.            (10)

For K, the sinc estimate gives 1-K<=(u^2+v^2)/12. Hence

    |H-1| <=[u^2/12+v^2/3]/K
            <=(50/49)(16/12+49/3)/n^2<19/n^2.

Using (8), the total H-1 term in (4) is at most

    8a*(19/n^2)*(25/54)=(1900/27)a/n^2<71a/n^2.   (11)

Finally |g|<=p|u|+q|v|<=7P/n, and (8) implies

    2mu sum_j1/(D_h K)
             <=2*(50/49)*(25/54)=1250/1323<1.

Thus the four sine-numerator terms cost at most 7P/n. Combine this,
(9)-(11), and the signed-displacement bound to obtain (1).

## Scope, provenance and checks

All estimates cover the closed near half diamond and both parities;
no moving-root differentiation, inverse phase factor or unweighted
collision value is used. The central rows are not included in (1).
The parent full S-a*S(0) target and the other ordinary/outer allowances
remain separate. No old near model or correction is changed.

Candidate/gate: ../ideas/D07-short-endpoints.md. Rules/input: parent
checkpoint 2e4ac49fa0687a7736bc1df82c12e6483b1c7a94, unchanged rules/catalog hashes recorded in the
attempt. 2026-11-06, parent-requested Astra ultra, serving metadata
unexposed. Paper proof only; independent review remains required.

2026-11-06 review correction: equation (10) now uses <=, since at
P=0 both sides are zero. This resolves the distinct reviewer's MINOR
display finding without changing statement (1), its constants or its
proof bound. The first frozen version, SHA256
075cf0546af581538543d15ac5e7dd37d920c19b2c44538093d967289b3b7c2c,
is preserved in root's checkpoint cbfdb04. No numerical run occurred.
