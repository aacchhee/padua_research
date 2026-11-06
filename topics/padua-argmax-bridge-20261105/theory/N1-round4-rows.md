# PD-T?argmax-bridge-codex-N1-07 — Uniform finite endpoint-row charts

ID kind: PD-T. Aliases: collision-safe sinc row limit; finite exceptional
h chart; closest-row sinc profile. Split from: round-4 H4. Split into:
none. All earlier N1 statements and proofs remain unchanged.

## Statement and definitions

Use the corrected finite polynomial G_n=D_n-cos(nu), m=n+1, and
alpha,beta>=0, alpha+beta<=pi. Let R>=2 and n>=8R be integers. For a
signed phase b with alpha+|b|<=pi and an integer r>=1, write

    w=r*pi+b, delta_r=(1-r) mod 2,
    u_j=(j*pi+alpha)/n, v=w/m,
    F_j=(-1)^delta_r G_n(u_j,v)/2,
    R_r^(b)=sum_j |F_j|.

The sum is over the n integers j congruent to delta_r modulo 2 for which
-pi<=u_j<pi. This half-open convention avoids duplicate representatives.
The admissible rows here are either b=beta, 1<=r<=R-1, or b=-beta,
1<=r<=R. Their right-end interpretation is exact:
R_r^(-beta) equals original row 2m-r by evenness of G in v.
In particular 0<=w<=pi R. Put a=(cos alpha+cos b)/2.

For w>0 define the explicit finite profile

    ell_r(alpha,b)=sin(b)/w
       +8a*sum_{j=-r+1,-r+3,...,r-1}
                   1/[w^2-(j*pi+alpha)^2].             (1)

Every removable product in this finite sum is interpreted continuously,
as specified in the proof's sinc formula. The only possible w=0 in the
stated rows is r=1,b=-pi,alpha=0; set ell_1(0,-pi)=1 there. Then

    |R_r^(b)/(nm)-ell_r(alpha,b)| <= e_row(n,R),          (2)
    e_row=(10R+33+6H_n)/n
                    +200(R+2)(R+1)^2/n^2,

where H_n=sum_{k=1}^n 1/k. This bound is uniform over every phase and
all polynomial collisions; no inverse phase-distance constant occurs.

The closest left row, r=0 with v=beta/m, has the sharper profile

    ell_0(beta)=sin(beta)/beta, ell_0(0)=1,
    |R_0^(beta)/(nm)-ell_0(beta)| <=(3+H_n)/n.           (3)

Thus all first/last R endpoint rows together have the fixed-size profile

    C_R=ell_0(beta)+sum_{r=1}^{R-1}ell_r(alpha,beta)
                         +sum_{r=1}^{R}ell_r(alpha,-beta),

with total error

    e_rows=(3+H_n)/n+(2R-1)*e_row(n,R).                 (4)

There are O(R^2) terms in C_R, independent of n. The corrected (n,0)
mode and every collision value are retained.

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; distinct review
pending. The exact finite numerator and signed row are N2/N1-01's
identities, with their polynomial continuation. No external theorem,
fit or computation is used. This proves the finite-row component of H4;
its mesh component is N1-06 and the final collision-hole assembly is
separate. Candidate: ../ideas/N1-round4.md.

## Proof

### 1. A polynomial-compatible sinc chart

Define sinc x=sin x/x, sinc 0=1, T(y)=y cot y, T(0)=1, and

    c_e=cos((alpha+b)/2), c_d=cos((alpha-b)/2), a=c_e*c_d,
    z=j*pi+alpha,
    sigma_- =(-1)^((r-j-1)/2),
    sigma_+ =(-1)^((j+r-1)/2).

The exponents are integers because j and r have opposite parity. For
0<w<=pi R the exact row identity is

    F_j/n^2 = 1/[2n sin(v/2)] *
      [c_e*sigma_-*sinc((z-nv)/2)*T((z/n-v)/2)
       +c_d*sigma_+*sinc((z+nv)/2)*T((z/n+v)/2)].        (5)

To verify it away from poles, N1-05's coefficient formulas and

    alpha-b+v=z-nv+(r-j)pi,
    alpha+b-v=z+nv-(j+r)pi

replace each coefficient cosine by its indicated signed sine. Then use
sin(nt)cot t=n sinc(nt)T(t). The expression in (5) is continuous at
t=0, and agrees with the finite polynomial on a dense phase set, so it
also supplies its actual collision values. Since |u_j|<=pi and
v<=pi/8, none of its T arguments reaches another cotangent pole.

The limiting reference is

    f_j=[c_e*sigma_-*sinc((z-w)/2)
                  +c_d*sigma_+*sinc((z+w)/2)]/w.        (6)

Away from removable zeros this is exactly

    f_j=4a/[w^2-z^2].                                  (7)

The signed sine factors in (6) prove (7) directly. Formula (6), rather
than zero times an infinite rational term, defines every removable
value. For the stated row domains

    0<=c_e,c_d<=1,       (c_e+c_d)/w<=2.                (8)

Indeed w>=pi except possibly the right row r=1. In that case
w=pi-beta and 0<=alpha<=w; the two cosines equal
sin((w+alpha)/2) and sin((w-alpha)/2), whose sum is <=w.
The weaker constant 2 in (8) is sufficient throughout.

### 2. Uniform comparison on the finite signed mesh

Put J=2R+2. Every admissible j with |j|<=J lies in the signed mesh
because n>=8R. There are at most 2R+4 such indices. Let
A_n=1/[2n sin(w/(2m))], x=w/(2m). Since x<=pi/16<1/4,
sin x>=x(1-x^2/6) gives

    A_n<=2/w,
    0<=A_n-1/w<=1/(nw)+w/(10n^2).                     (9)

The global bound |sinc'|<=1/2 follows by differentiating
sinc x=integral_0^1 cos(tx)dt. The arguments in (5) and (6) differ
by w/(2m). Their T arguments y have |y|<2 on the near set. On [-2,2],
concavity and sin 2>=2/3 imply |sin y|>=|y|/3; integrating t sin t
therefore gives |T(y)-1|<=y^2. From (8)-(9), the three errors from the
prefactor, sinc shift and T factor are bounded, per near index, by

    2/n+pi^2 R^2/(5n^2),
    1/n,
    9pi^2(R+1)^2/n^2,

respectively. Hence their sum is at most
3/n+10pi^2(R+1)^2/n^2. Summing the near indices and using pi^2<10 gives

    near error <=(6R+12)/n
                         +200(R+2)(R+1)^2/n^2.         (10)

For the remaining mesh indices |j|>J, put u=z/n. Then |z|>=2w and
v<=|u|/2. Define

    K=sinc((|u|+v)/2)*sinc((|u|-v)/2).

Sine chords on [0,3pi/4] and [0,pi/2] give
K>=4sqrt(2)/(3pi^2)>1/6. Also
1-K<=(u^2+v^2)/12. Therefore

    |(1+cos v)/(2K)-1|
       <=[u^2/12+v^2/3]/K<=u^2.                       (11)

The exact numerator is

    F=[2a(1+cos v)-sin(alpha)sin u+sin(b)sin v]
                                      /[2(cos u-cos v)].

Using cos v-cos u=(u^2-v^2)K/2, (11) compares its A term divided by
n^2 with 4a/[(nv)^2-z^2], at cost <=16a/(3n^2) per index. The total
is <=6/n. Replacing nv by w costs at most

    15a*w^2/(n*z^4)

per index: use w^2-(nv)^2<=2w^2/n and both denominators >=3z^2/4.
The elementary sums

    sum_far 1/z^2 <=2/[pi^2(J-1)],
    sum_far 1/|z| <=2H_n/pi,
    w*sum_far 1/z^2 <=1/pi                             (12)

follow from |z|>=pi(|j|-1) and integral comparison. They also give
sum_far w^2/z^4<=1/[2pi^2(J-1)]. Thus the mesh-shift cost is <=1/n.
Finally cos v-cos u>=u^2/16 bounds the two sine terms by

    8/(n|z|)+8w/(nz^2).

Their sum is at most (6H_n+3)/n by (12). Together with the A term and
mesh shift, the far error is therefore <=(10+6H_n)/n.

### 3. Infinite tail, finite profile and normalization

The infinite reference outside the half-open n-point mesh has |z|>=pi n
and w<=pi n/8. Equation (7) bounds its magnitude by 5/z^2. The two
tails, of spacing 2pi, have combined sum

    sum 1/z^2 <=2/(pi^2 n^2)+1/(pi^2 n)<=2/(pi^2 n).

Thus the omitted absolute reference tail is <=2/n. The same comparison
shows sum_j |f_j|<=4R+9: the near terms are each <=2 by (6),(8), and
the far reference sum is <1 by (7),(12). Consequently (10), the far
error and the omitted tail prove

    |R_r^(b)/n^2-sum_j |f_j||
       <=(6R+24+6H_n)/n+200(R+2)(R+1)^2/n^2.

Replacing n^2 by nm costs at most (4R+9)/n in this comparison. This
gives exactly the bound in (2).

It remains to identify the infinite reference with (1). The same
absolute comparison also justifies passage to the limit in the signed
row. The exact signed identity is

    sum_j F_j=n*[a-(sin(b)/2)cot(w/(2m))].

For fixed phases with w>0 its n^-2 limit is -sin(b)/w, so
sum_j f_j=-sin(b)/w. In the interior of the phase diamond, (7) is
positive exactly for j=-r+1,-r+3,...,r-1, and negative outside: the two
factors z-w and z+w have fixed signs because j-r and j+r are odd.
Thus |f|=-f+2f_+ gives precisely (1). Uniform tail bounds and (6) extend
this identity continuously to all boundary phases and removable zeros.

At r=1,b=-pi,alpha=0,w=0, the unique limiting reference has f_0=1 and
all other f_j=0. Explicitly its finite profile becomes, for nearby phases,

    -sin w/w
       +2*sinc((w+alpha)/2)*sinc((w-alpha)/2),

which tends to 1 uniformly for 0<=alpha<=w. The finite polynomial row
is continuous as well; the phase-uniform bound already proved passes to
this endpoint. This completes (1)-(2).

### 4. The closest left row

Here v=beta/m and every regular odd-grid u satisfies cos u<cos v,
because |u|>v on its signed representative mesh. The sole endpoint
exception is treated by polynomial continuity. Put p=sin alpha,q=sin beta.
Since a>=0 and q sin v>=0, a positive F requires sin u>0 and obeys

    F_+<=p sin u/[2(cos v-cos u)]<=p/(u-v).

The last step uses cotangent addition and cot x<=1/x: the sum of the
two cotangents is at most twice cot((u-v)/2). The relevant positive u
are ((2k+1)pi+alpha)/n, k>=0. Since beta<=pi-alpha,

    u-v >=(2k*pi+2alpha)/n.

For k=0 use p<=alpha, giving a bound n/2, including alpha=0 by continuity.
The remaining terms sum to at most n H_n/(2pi). Hence

    2*sum F_+/(nm)<=(1+H_n/pi)/m.

The negative signed row, divided by nm, is
q cot(beta/(2m))/(2m)-a/m. Its difference from q/beta has magnitude
at most 1/m+pi^2/(24m^2), again by 1/x-cot x<=pi x/6. Since
R_0=-sum F+2sum F_+, this proves the slightly stronger bound
(2+H_n/pi)/m+pi^2/(24m^2), and therefore (3). Complete polynomial
continuity covers beta=0 and both phase vertices. Summing all 2R row
errors gives (4).

## Checks, limits and history

A bounded parallel developer cross-check reconstructed the sinc signs,
near/far constants, half-open mesh and w=0 convention and found no
definite gap. It is not approval of this frozen file or of H4. No
mathematical numerical run was used. Distinct review remains pending.

This result removes n from the evaluation count of the finite endpoint
rows, with an explicit full-phase remainder. It does not handle all
outer rows or prove an argmax comparison. The r-dependence is explicit
and must be included in any later choice of R and error budget.
2026-11-06, round 4 after bda45a4, Codex requested gpt-6-astra ultra.
