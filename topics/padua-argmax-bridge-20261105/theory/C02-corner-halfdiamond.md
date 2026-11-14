# PD-T?argmax-bridge-C02-corner — Explicit actual-corner bound on the half diamond

ID kind: PD-T.
Aliases: C02 corner orbit; radius-half reflection-first bound;24000 corner
remainder; direct actual-corner patch without energy.
Split from: quantitative domain/constant continuation of PD-T228. Its
original all-n radius1/64 theorem remains unchanged.
Split into: none. The strict-patch consequence below is routine algebra;
global localization and any global argmax onset remain separate.

## Statement

Use exactly the corrected even-checkerboard Padua cardinal polynomials of
PD-T101. For every integer `n>=64`, set `m=n+1`, `N=nm`, and

    z_n(alpha,beta)=(-cos(alpha/n),-cos(beta/m)),
    Lambda_c(n)=lambda_n(-1,-1),
    a=(cos alpha+cos beta)/2, rho=alpha+beta.

For every inward phase pair `alpha,beta>=0` with `rho<=1/2`,

    lambda_n(z_n(alpha,beta))
        <= a Lambda_c(n)+24000 rho^2 log(n+1).                    (1)

The identical estimate holds in inward phases at the other nonnode
corner. In particular, at both corners the entire punctured patch
`0<rho<=1/2` satisfies `lambda_n<Lambda_c` whenever

    Lambda_c(n)>240000 log(n+1).                                 (2)

A sufficient explicit condition for (2) is `log n>=610000`.
This is an impractical sufficient **corner-patch threshold**, not a
global argmax onset. The theorem makes no assertion that an arbitrary
global maximizer lies in these patches.

## Definitions and assumptions

All arithmetic and logarithms are exact real quantities. Write
`T_k(cos t)=cos(kt)`, `P_n=T_m+T_n`, and define the finite polynomial

    D_n(u,v)=[P_n(cos u)-P_n(cos v)]/[cos u-cos v],
    G_n(u,v)=D_n(u,v)-cos(nu).                                   (3)

The divided difference is its polynomial extension at equal arguments,
including derivatives on the diagonal. It is the PD-T185 kernel;
the correction is in the first coordinate and is not symmetrized.

Let `O={(j,r):0<=j<=n,0<=r<=m,j+r odd}` be the physical odd board,
and let `e_j,f_r` be1/2 at their own mesh endpoints and1 otherwise.
For arbitrary real phases put

    F_jr(alpha,beta)=(-1)^j G_n((j*pi+alpha)/n,(r*pi+beta)/m)/2.

Every such value is evaluated by (3), even at collisions. In proofs
below, signed phases of total absolute size at most1/2 are allowed,
although the physical conclusion (1) uses inward nonnegative phases.
No cardinal sign stability, weighted energy estimate, norm ratio,
approximation model or prior global argmax is assumed.

## Status by part

Overall status: **PROVED**, by the complete analytic developer proof
below. This status describes the written proof, not independent
acceptance. Separate reconstruction and formal campaign audit are pending.

| Mathematical part | Status | Evidence / limits |
|---|---|---|
| Actual-corner estimate (1), n>=64 and full closed rho<=1/2 | PROVED | Exact reflected cardinals, uniform regular geometry and finite collision bounds below |
| Strict-patch criterion (2), sufficient log n>=610000 and second-corner transfer | PROVED routine consequences | Cosine lower bound, PD-T157 and checkerboard-preserving reflection |

Candidate disposition: retained quantitative domain/constant variant of
IDEA331 / PD-T228; no new-mechanism or priority claim.

## Depends on

- PD-T101 and PD-T185: corrected cardinal formula and finite polynomial
  kernel, with the exceptional highest x mode retained as in (3).
- PD-T228: exact actual-corner four-reflection normalization and its
  finite B-family factorization. Both are reproduced below.
- PD-T221, proof sections1 and3: regular pointwise derivative bounds and
  finite B-family derivative method. The larger-radius geometry and all
  normalized constants used here are explicitly checked below; no old
  small-radius conclusion is silently extended.
- PD-T157: `Lambda_c>=(4/pi^2)log^2 n-54`, used only for the sufficient
  strict-patch threshold.

## Proof

### 1. Average the exact cardinal orbit first

An original even-board index `(p,q)` has `p+q` even and weight
`w_pq=2e_p f_q/N`. The corrected cardinal identity gives

    L_pq(cos theta,cos phi)
       =(w_pq/4) sum_(sigma,tau=+-1)
           G_n(theta+sigma*p*pi/n,phi+tau*q*pi/m).

At `theta=pi-alpha/n,phi=pi-beta/m`, reflect indices by
`j=n-p,r=m-q`. Since `n+m=2n+1` is odd, this is a bijection onto O.
The kernel is separately even and2pi-periodic in its angular arguments.
Its four copies reduce, with multiplicities, to the arguments in the
four `F_jr(+-alpha,+-beta)`. Their common factor `(-1)^j` does not
depend on either reflection sign. Thus, exactly,

    L_pq(z_n)=(e_j f_r/N)(-1)^j sum_four F_jr,
    lambda_n(z_n)=(1/N) sum_O e_j f_r |sum_four F_jr|,             (4)
    Lambda_c=(4/N) sum_O e_j f_r |F_jr(0,0)|.                     (5)

The absolute value in (4) is after the fourfold sum. These are finite
polynomial identities, valid when reflected copies coincide, at all
endpoints and at initially zero cardinals. The zero row `r=m,j<n`
has `F0=0` and is retained. The endpoint `(n,m)` has the finite value
`F0=n`; it is not replaced by a zero numerator divided by zero.

### 2. Larger-radius regular geometry, including overshoots

Remove the same collision family as PD-T228:

    B={(j,r) in O:r=j+1,j>=2n/3}, R=O minus B.

For `(j,r)` in R put

    L=|j-r|, d=min(j+r,2n+1-j-r),
    u0=j*pi/n, v0=r*pi/m,
    u=u0+gamma/n, v=v0+delta/m,
    P=(u+v)/2, T=(u-v)/2, b=sin P, t=|sin T|,

where `|gamma|+|delta|<=1/2`. The odd parity gives `L>=1`.
Both endpoint pairs `(0,0),(n,m)` are absent from R, so `d>=1`.
Also `L,d<=m` and `m/n<=65/64` throughout this proof. We prove

    0<P<pi, b>=5d/(6m), t>=L/(4m),
    |sin u|,|sin v|<=3b.                                        (6)

For P, the unperturbed distance to either0 orpi is at least
`pi*d/(2m)`. Its change is at most `1/(4n)`. In particular it stays
strictly between0 andpi. The sine chord bound then gives

    b >= d/m-1/(2*pi*n)
       >= [d-65/(128*pi)]/m >=5d/(6m),                           (7)

because `pi>25/8>195/64`, hence `65/(128*pi)<1/6`, and `d>=1`.

The absolute change of `u-v` is at most `1/(2n)<=65/(128m)`.
There are three cases for its unperturbed gap.

* If `j>r`, that gap is at least `pi*L/m`. After perturbation it
  exceeds `2L/m`, since `pi>3` and `65/128<1`.
* If `r-j=L>=3`, the gap is at least `pi*(L-1)/m`. Since
  `L-1>=2L/3`, after perturbation it exceeds
  `(2-65/384)L/m>(9/5)L/m`.
* If `r=j+1`, membership in R implies `j<2n/3`. With `h=n-j>n/3`,
  its unperturbed gap is `pi*h/(nm)>pi/(3m)`. Thus

      |T| > [pi/3-65/128]/(2m) >205/(768m),
      |T| < [pi+65/128]/(2m) <5/(2m)<=1/26.

  The Taylor bound `sin x>=x-x^3/6>=(99/100)x` for
  `0<=x<=1/26` gives
  `t>20295/(76800m)>1/(4m)`.

In the first two cases `|T|<=pi/2+1/256<8/5`. On `[0,8/5]`,
`sin x>=(3/5)x`: concavity reduces this to the upper endpoint,
where `sin(8/5)=cos(8/5-pi/2)>24/25` because
`0<8/5-pi/2<1/10`. This proves `t>=L/(4m)` there as well.
All regular denominators therefore remain nonzero for every signed
phase used below, including the closed half-diamond boundary.

For the sine numerator bound in (6), if both u and v lie in `[0,pi]`,
then `sin u,sin v<=2sin P`. For example, concavity in the other
coordinate shows `sin P>=min(sin(u/2),cos(u/2))>=sin u/2`.

An overshoot outside `[0,pi]` is possible only at a corresponding
mesh endpoint. Its magnitude `epsilon` is at most `1/(2n)`.
If the other coordinate remains inside, reflect both coordinates
aboutpi when needed, so that the first is `-epsilon` and the other
is `w in[0,pi]`. The other base index is not at the same endpoint:
`(0,0)` is not odd, and `(n,m)` was removed. Consequently

    w>=(pi-1/2)/m,
    epsilon/w <=65/[128(pi-1/2)]<1/5.

Concavity of sine on `[0,pi/2]` gives

    b=sin((w-epsilon)/2)>=(4/5)sin(w/2),
    sin w<=2sin(w/2)<3b.

The overshooting coordinate itself has
`|sin u|<=epsilon<=1/(2n)<5/(6m)<=b`. If both coordinates
overshoot, they cannot do so at the same endpoint on R. For opposite
endpoints, `|P-pi/2|<=1/(4n)<=1/256`, so `b>1/2` and both sine
magnitudes are at most `1<2b`. This exhausts all overshoot cases
and proves (6).

### 3. Pointwise derivatives and explicit normalized sums

On R define

    f=(1+cos v)/(cos u-cos v),
    g_u=sin u/(cos u-cos v), g_v=sin v/(cos u-cos v).

Direct substitution in (3), using odd j+r, gives the exact identity

    F=a f-(sin gamma/2)g_u+(sin delta/2)g_v.                       (8)

Here `a=(cos gamma+cos delta)/2` at the indicated signed phases.
Write ordinary coordinate derivatives with subscripts `i,j in{u,v}`.
The pointwise estimates used in PD-T221 remain valid under (6):

    max_i |f_i| <=2 b^(-1)t^(-2),
    max_ij |f_ij| <=8[b^(-2)t^(-2)+b^(-1)t^(-3)],                (9)
    |g_*| <=t^(-1)+b^(-1),
    max_i |(g_*)_i| <=t^(-2)+b^(-2),
    max_ij |(g_*)_ij| <=t^(-3)+b^(-3).                          (10)

For clarity, `cos u-cos v=-2b sin T`; differentiate the quotients
and use `|sin u|,|sin v|<=3b` and `1+cos u,1+cos v<=2`.
The first derivative coefficient is at most3/2. Second derivatives
have coefficients at most1/2 and9/2 for the two terms in (9),
or9/4 and9/2 in the mixed case; the displayed8 is larger.
For (10) use
`g_u=-(cot T+cot P)/2,g_v=-(cot T-cot P)/2`.
These differentiations involve no cardinal absolute value.

Let `H=1+log m`. For a fixed signed difference `j-r`, each d
has multiplicity at most2, so for fixed absolute L that multiplicity
is at most4. Fixed L has at most2m pairs and fixed d at most4m.
All sums can be enlarged to `1<=L,d<=m`. Using
`sum k^(-1)<=H,sum k^(-2)<=2,sum k^(-3)<=2`, the stronger
plus-angle bound of (6) gives

    sum_R b^(-1)t^(-2) <=(768/5)m^3 H,
    sum_R b^(-2)t^(-2) <=(9216/25)m^4,
    sum_R b^(-1)t^(-3) <=(3072/5)m^4 H.                         (11)

For example the first coefficient is
`4*(6/5)*16*2=768/5`; the other two are
`4*(36/25)*16*2*2=9216/25` and
`4*(6/5)*64*2=3072/5`. Thus (9), divided by the indicated
powers of n and the normalization N, yields

    (1/N)sum_R max_i|f_i|/n
       <=(1536/5)(65/64)^2 H=(2535/8)H<320H,
    (1/N)sum_R max_ij|f_ij|/n^2
       <=8(24576/25)(65/64)^3 H=(32955/4)H<8240H.               (12)

For (10) even the weaker `b>=d/(2m)` suffices. The unnormalized
sums of its three majorants are at most

    16m^2 H, 96m^3, 320m^4,

respectively: sum the t powers with at most2m pairs per L and
the b powers with at most4m per d. With `m/n<=3/2`, these give

| Sum normalized by1/N | Bound |
|---|---:|
| `sum_R |g_*|`, each channel separately | `24H` |
| `sum_R max_i |(g_*)_i|/n` | `216` |
| `sum_R max_ij |(g_*)_ij|/n^2` | `1080` |

All these bounds are uniform termwise majorants on the entire signed
half diamond. Endpoint factors are at most1 and may be retained
throughout. No supremum/sum interchange with an uncontrolled quantity
is needed.

### 4. The regular symmetric orbit remainder

Fix a signed direction `(alpha0,beta0)` of total size rho<=1/2 and set

    E_jr(s)=F_jr(s alpha0,s beta0)-a(s alpha0,s beta0)F_jr(0,0),
    -1<=s<=1.

Here `E(0)=0`; on R, `F0=f0`. The physical angular speed has
L1 norm at most `rho/n`. Also `|a|<=1` and
`|a'|,|a''|<=rho^2/2`. From (12), integration along the path gives
`(1/N)sum|f(s)-f0|<=320rho H`. The three product-rule terms
of `[a(f-f0)]''` therefore have normalized absolute sum at most

    160rho^3 H+320rho^3 H+8240rho^2 H.                         (13)

Each sine channel of (8) costs at most

    12rho^3 H+216rho^2+540rho^3.                               (14)

Indeed its scalar coefficient and first derivative are bounded by
`rho/2`, its second derivative by `rho^3/2`, and its g derivatives
along the path by the last table times rho orrho^2. There are two
such channels. Combining (13),(14), with rho<=1/2 and H>=1,

    (1/N)sum_R e_j f_r |E_jr''(s)|
       <=rho^2[(8240+504rho)H+432+1080rho]
       <=9464rho^2 H<9500rho^2 H.                             (15)

Symmetric Taylor, applied before any orbit absolute value, gives

    E(1)+E(-1)=integral_0^1 (1-s)[E''(s)+E''(-s)] ds.

Its total integral weight is1. Pair the `(+,+)` and `(-,-)` phases,
and the `(+,-)` and `(-,+)` phases. The triangle inequality and
(15) imply

    (1/N)sum_R e_j f_r |sum_four E_jr|
       <=19000rho^2 H.                                        (16)

This is an absolute remainder bound for the actual cardinal orbit.
It does not require that F, its numerator, f or any cardinal retain
a sign. In particular initially zero cardinals are included in (15).

### 5. The removed finite collision family

For `(j,r)` in B put `h=n-j`, so `0<=h<=n/3` and

    x_B=(h*pi-gamma)/n, y_B=(h*pi-delta)/m,
    X_B=(x_B+y_B)/2, T_B=(x_B-y_B)/2.

The exact finite-sum identity from PD-T185/228 is

    D_n=(-1)^n[V_n(X_B)U_m(T_B)+U_n(X_B)V_n(T_B)],
    U_k(z)=sin(kz)/sin z,
    V_n(z)=cos((2n+1)z/2)/cos(z/2).                            (17)

U is evaluated as its k-term Fourier sum at every sine zero. Thus
globally `|U_k^(q)|<=k^(q+1)` for q=0,1,2. The signed half-diamond
geometry gives

    |X_B|<=pi/3+1/(4n)<=pi/3+1/256<1.1,
    |T_B|<=pi/(6m)+1/(4n)<1.1.                                (18)

For `|z|<=1.1`, the zeroth, first and second derivatives of
`sec(z/2)` are bounded by5/4,5/8,1, respectively. For example,
`cos(z/2)>=1-(11/20)^2/2>4/5` and `|tan(z/2)|<1` give all
three bounds by differentiation. With `n+1/2<=5n/4`, this yields

    |V_n|<=5/4, |V_n'|<=2n, |V_n''|<=3n^2.                    (19)

For the second derivative, division by n^2 gives the bound
`125/64+25/32+1/4=191/64<3`; for the first it gives
`25/16+5/16<2`. These use only n>=2.

Every first phase derivative of X_B and T_B is at most1/(2n)
in magnitude and all their second phase derivatives vanish. Put
`r_*=m/n<=3/2`. Differentiating (17) twice gives

    |D_n,ij|
       <=(n/4)[3r_*+4r_*^2+(5/4)r_*^3+33/4]
       <=831n/128.                                           (20)

The first three coefficients in brackets are the product-rule costs
for `V_n(X_B)U_m(T_B)`; the final33/4 is
`(5/4)+4+3` for `U_n(X_B)V_n(T_B)`. The correction in (3) has
phase second derivatives of magnitude at most1. After the factor1/2
defining F, (20) therefore implies

    |F_jr,ij|<=4n, |F_jr(0,0)|<=2n.                           (21)

For the second bound, directly use (17),(19) to bound
`|D_n|<=(5/4)(m+n)<=25n/8`; then `(25n/8+1)/2<=2n` for n>=2.
All derivatives in (20),(21) are phase derivatives. They are finite
polynomial bounds at h=0 and every collision; no B-family positivity
or cardinal sign stability is used.

For the same remainder E as above, (21) and `|a''|<=rho^2/2`
give `|E''(s)|<=5n rho^2`. There are two symmetric pairs and at
most n indices in B. Since `N=nm`, their normalized contribution is

    (1/N)sum_B e_j f_r |sum_four E_jr|<=10rho^2.                 (22)

This includes `(n,m)`, its endpoint factors and its repeated orbit
copies exactly. No formal rational value is substituted there.

### 6. Assemble and prove the strict-patch consequence

For each physical odd index, `sum_four F=4aF0+sum_four E`.
Since a>0, equations (4),(5),(16),(22) give

    lambda_n(z_n)<=a Lambda_c+19000rho^2(1+log m)+10rho^2.       (23)

For m>=65, `log m>log64=6log2>4`, using the elementary
`log2>2/3` from strict convexity of1/x on `[1,2]`. Hence
`1+log m<=(5/4)log m` and
`10<(5/2)log m`. The coefficient in (23) is at most
`23750+5/2<24000` times log m. This proves (1), including rho=0
and the closed rho=1/2 boundary.

For `0<=t<=1/2`, cosine Taylor gives
`1-cos t>=t^2/2-t^4/24>=(2/5)t^2`. Consequently

    1-a >=(alpha^2+beta^2)/5>=rho^2/10.

Insert this into (1):

    lambda_n(z_n)
       <=Lambda_c-rho^2[Lambda_c/10-24000log m].               (24)

This proves strict comparison on `0<rho<=1/2` under (2). To check
the sufficient logarithmic condition, let `ell=log n>=610000`.
PD-T157 and `pi^2<10` give `Lambda_c>=(2/5)ell^2-54`, while
`log m<=ell+1`. On this range,

    (2/5)ell^2-54-240000(ell+1)
       >=4000ell-240054>0.

Thus (2) holds for every such integer n. No numerical exponential
evaluation or inference from finite degrees is involved.

For even n, x reflection preserves the even checkerboard, its weights
and corrected cardinal polynomials by interpolation uniqueness. It
maps `(-1,-1)` to the second nonnode corner. For odd n, y reflection
does so because m is even. In either case the reflection permutes
cardinals, preserves inward phase magnitudes and proves the identical
estimate and equality of corner values at that other corner. QED.

## Checks, scope and open items

Analytic proof only. No numerical kernel, phase, degree or energy test
is a premise. One standard-library Fraction check verified the displayed
scalar rational budgets; no phase or degree sample was evaluated. The
source gate, timing,
bounded alternatives and resource boundary are in
`../ideas/C02-corner.md`; actual work is in `../attempts/C02-corner.md`.
The proof uses no unspecified remainder constant.

This theorem supplies a direct pointwise actual-corner predicate on
the full inward half diamond. It covers every endpoint/collision
convention and both corner parities. It does not assert a global
equality set, a sharp first corner-patch threshold, a practical finite
bridge, a near-model validity onset, an all-n three-quarter energy
estimate or any extension of the finite exact global-degree range.

Any global assembly needs independent strict comparison at all
remaining physical centers and phases. Distinct mathematical review
must reconstruct the larger-radius geometry and complete scalar
budget before the parent uses (1) as an accepted new premise. Formal
Claude audit remains separate; the developer cannot self-approve it.

## Sources and history

No external source theorem or historical novelty claim. The underlying
reflection and finite derivative mechanism is explicitly PD-T228/221;
the contribution is the verified larger radius, n64 geometry and
numerical constant reduction. All C01 source proof bytes are unchanged.

2026-11-06, Codex auxiliary mathematical developer, parent allocation
inherited; serving model/effort independently unexposed. Rules/input
`4b728b04216a5490910780bc609a82b853058426`. Only assigned new
C02-corner files are written; no Git/shared/old-proof mutation or
subagent delegation. Separate independent reconstruction pending.
