# PD-T367 (PD-T?argmax-effective-2-codex-05) — Uniform aggregate corner gradient energy

ID kind: PD-T.
Aliases: H3 weighted-energy closure; diagonal cancellation and off-diagonal summation.
Split from: the weighted-energy premise of PD-T227 / IDEA-330.
Split into: none; a local-radius consequence and its global-norm dependency belong in a separate record.

## Statement

For every integer n>=2, use the even-checkerboard Padua cardinals L_jk of PD-T101. Put m=n+1, N=nm, c=(-1,-1), and Lambda_c=lambda_n(c). Then the exact physical gradient energy of PD-T227 satisfies

    W_n = sum_(L_jk(c)!=0) (L_jk,x(c)^2+L_jk,y(c)^2)/|L_jk(c)|
        <= 10^10 n^4 Lambda_c.                                      (1)

The constant is deliberately coarse. No uniform per-cardinal gradient/value bound is asserted: PD-N085 remains valid. The same statement holds in inward coordinates at the other parity-correct nonnode corner, by the node-preserving reflection of PD-T251.

## Definitions and assumptions

All arithmetic is exact real arithmetic. Original physical node indices satisfy 0<=j<=n, 0<=k<=m, j+k even. Endpoint-weighted positive weights are w_jk=2 epsilon_j eta_k/N, hence w_jk<=2/N. By PD-T227, the nonzero cardinals comprise the removable index 00 and all indices with k>=1. Put, at a regular nonzero index,

    u=j*pi/n, v=k*pi/m, a=cos u, b=cos v,
    A=1-a, C=1-b, d=b-a, V=|L_jk(c)|=2w_jk C/|d|,
    q_x=L_jk,x(c)/L_jk(c), q_y=L_jk,y(c)/L_jk(c).

Then the contribution to W is V(q_x^2+q_y^2). Write H=1+log m and H_r=sum_(h=1)^r 1/h. Every sum below is finite unless explicitly bounded by a convergent positive series. The elementary estimates 8<pi^2<10 and sum_(r>=1) r^(-p)<=2 for p>=2 suffice.
Here N=nm is the mesh product, not PD-T101's node count; H denotes a
logarithmic factor, whereas H in T07 denotes the physical distance h_x+h_y.

## Status by part

Overall status: **PROVED** by the written analytic argument below.
Dated review note, 2026-11-05: Claude [audit-01](../audit-01.md) accepted
the original scope; the record response check is pending.

| Part | Status | Evidence / limit |
|---|---|---|
| Explicit all-n energy bound (1) | PROVED | Diagonal cancellation; off-diagonal weighted sums; separate removable index |
| Transfer to the second nonnode corner | PROVED (routine invariance) | PD-T228, end of §4; parity-preserving node/weight permutation and cardinal uniqueness |

Candidate disposition: retained quantitative continuation of IDEA-330. No priority claim. The original all-degree global argmax target remains OPEN.

## Depends on

- PD-T227: exact values and physical gradient/value formulas, zero mask, removable index.
- PD-T251 §1: Lambda_c>=2, hence also Lambda_c>=1 used in (14).
- PD-T228, end of proof §4: node-preserving corner reflections, also used in PD-T251.
- PD-T157: Lambda_c >= (4/pi^2) log^2 n -54.

The scalar lower bounds absorb H into Lambda_c; Lambda_c>=1 also
justifies the last inequality of (14). No global Lebesgue upper bound,
claimed argmax equality, fitted constant, numerical energy screen, or
unproved sign stability is used.

For the corner transfer, x-reflection sends j to n-j when n is even;
y-reflection sends k to m-k when n is odd (so m is even). Each preserves
j+k even and the endpoint weights. Uniqueness of interpolation permutes
the cardinals; inward derivatives and squared gradient magnitudes
therefore give the same Lambda_c, A_n, B_n and W_n at the second corner.
This spells out the invariance already cited in the statement.

## Proof

### 1. Exact ratio reduction

PD-T227 gives

    q_x=-n^2/2 + n(ab-1)/(Cd) - a/d + 2(1-a^2)/d^2.                (2)

Subtracting its two gradient formulas and using a^2-b^2=-(a+b)d gives the exact useful cancellation

    q_y-q_x=-(2n+1)/2 + A/d.                                     (3)

Separate the diagonal j=k>=1, the off-diagonal indices, and 00. The parity constraint makes every off-diagonal gap L=|j-k| at least 2.

### 2. Diagonal: cancellation before estimates

Let j=k>=1, u=j*pi/n, tau=n/m and v=tau*u. Thus d>0. First suppose u<=pi/2. Put

    s=(1+tau)u/2, t=(1-tau)u/2,
    C_0=tau^2*u^2/2, d_0=(1-tau^2)*u^2/2,
    E_0=(1+tau^2)*u^2/2.

With sinc z=sin z/z, define

    R_C=C/C_0=sinc^2(v/2),
    R_d=d/d_0=sinc(s)sinc(t),
    R_E=(1-ab)/E_0=(sin^2 s+sin^2 t)/(s^2+t^2),
    R_u=(1-a^2)/u^2=sinc^2 u.

All these ratios lie in (0,1]. Here 0<=t<=s<=u<=pi/2, and sinc is
positive and decreasing on [0,pi/2], with value 1 at zero.
R_E is the weighted average of sinc^2 s and sinc^2 t with weights
s^2,t^2, so R_E>=sinc^2 s. Sine's chord bound yields R_C,R_d>=4/pi^2>2/5. The Taylor estimates 0<=1-sinc z<=z^2/6 and 0<=1-sinc^2 z<=z^2/3 on 0<=z<=pi/2 yield

    1-R_C<=u^2/12, 1-R_d<=u^2/6,
    1-R_E<=u^2/3, 1-R_u<=u^2/3.

Consequently

    |R_E/(R_C R_d)-1| < 4u^2,
    |R_u/R_d^2-1| < 5u^2,
    |cos u/R_d-1| < 2u^2.                                      (4)

For example the first numerator error is at most (1/3+1/12+1/6)u^2=7u^2/12, and its denominator exceeds 4/25. The other two follow in the same way, with numerator bounds 2u^2/3 and denominator bounds 4/25 and 2/5 respectively.
For the second numerator use 1-R_d^2=(1-R_d)(1+R_d)<=2(1-R_d).

In (2), replace the three nonconstant rational terms by their leading expressions

    -2n(1+tau^2)/(tau^2(1-tau^2)u^2),
    -2/((1-tau^2)u^2),
     8/((1-tau^2)^2u^2).

Their coefficients add exactly to

    K_n=-2m^3/[n(2n+1)^2].                                     (5)

This cancellation is essential. Since n>=2,

    n/(1-tau^2)<=m^2/2,
    (1+tau^2)/tau^2<=13/4,
    1/(1-tau^2)=m^2/(2n+1)<=3m/5,
    |K_n|<2.

Thus (4) bounds the errors of those three terms by 13m^2, 12m/5, and 15m^2, respectively. Also u>=pi/n gives |K_n|/u^2<n^2/4. Inserting the constant term -n^2/2 in (2) proves

    |q_x| < 30m^2.

Moreover A/d <= 1/((1-tau^2)R_d) <=3m/2. Equation (3) therefore gives |q_y|<31m^2.

Now suppose pi/2<=u<=pi. Write delta=u/m, s=u-delta/2, t=delta/2. Here v>=pi/3, hence C>=1/2. One has t<=s<=pi-t, so sin s>=sin t>=delta/pi. Therefore

    d=2sin s sin t>=2delta^2/pi^2>=1/(2m^2),
    sin u <= sin s+sin t <=2sin s,
    (1-ab)/d=(sin^2 s+sin^2 t)/(2sin s sin t)
             <=sin s/sin t<=pi/delta<=2m.

It follows that the absolute values of the four terms in (2) are bounded by n^2/2, 4nm, 2m^2, and 8m^2. Hence |q_x|<15m^2. Equation (3), with A/d<=4m^2, gives |q_y|<20m^2. Both halves are covered by the weaker pair 30m^2,31m^2. Summing V and using m/n<=3/2 gives

    W_diag <=(30^2+31^2)m^4 sum_diag V
            <10000 n^4 Lambda_c.                              (6)

### 3. Off-diagonal geometry

For an off-diagonal index put

    L=|j-k|>=2,
    D=min(j+k,2n+1-j-k)>=1,
    s=(u+v)/2, t=|u-v|/2.

Both angle sums u+v and 2pi-u-v are bounded below by pi/m times their corresponding integer sums. Also |j/n-k/m|>=L/(2m): the j>k case is immediate, while j<k gives (nL-j)/N>=(L-1)/m>=L/(2m). Sine's chord bound now gives

    sin s>=D/m, sin t>=L/(2m), |d|>=DL/m^2.                     (7)

For upper estimates, sin s<=pi D/(2n) and sin t<=pi(L+1)/(2n)<=3pi L/(4n). The elementary index inequality L<=D+1<=2D then implies

    1-ab=sin^2 s+sin^2 t <=25D^2/n^2,
    |sin u|<=sin s+sin t<=2pi D/n,
    sin^4 u<=1600D^4/n^4.                                     (8)

Also C=2sin^2(v/2)>=2k^2/m^2. These estimates include j=0, j=n, and k=m; no endpoint weights are dropped upward except via w<=2/N.

### 4. Off-diagonal sums

Let T_2,T_3,T_4 denote the last three terms of (2), in order. From V<=4C/(N|d|), (7), (8), C<=2, and m/n<=3/2,

    V T_2^2 <=22500 n^4 D/(k^2 L^3),
    V T_3^2 <=61 n^4 /(D^3 L^3),
    V T_4^2 <=2000000 n^4 /(D L^5).                            (9)

For clarity the unsimplified constants are, respectively,

    1250(m^7/n^3) D/(k^2 L^3),
    8(m^5/n)/(D^3 L^3),
    51200(m^9/n^5)/(D L^5).

For the first sum, D<=j+k<=2k+L; each pair k,L allows at most two j. Extending positive sums to infinity and using sum r^(-p)<=2 gives

    sum_off D/(k^2L^3)
      <=2 sum_(k=1)^m sum_(L>=2) [2/(k L^3)+1/(k^2 L^2)]
      <=8H_m+8 <=16H.                                        (10)

Here H_m<=1+log m=H by the integral bound for the harmonic sum,
and H>=1 absorbs the additive 8.

For fixed L,D there are at most four index pairs: each of j=k+L and j=k-L has at most two solutions of D=min(j+k,2n+1-j-k). Therefore

    sum_off 1/(D^3L^3)<=16,
    sum_off 1/(D L^5)<=8H_(2n+1)<=16H.                        (11)

Equations (9)--(11) imply

    sum_off V T_2^2<=360000 n^4 H,
    sum_off V T_3^2<=976 n^4,
    sum_off V T_4^2<=32000000 n^4 H.

Using (r_1+r_2+r_3+r_4)^2<=4 sum r_i^2 in (2), and sum_off V<=Lambda_c, gives

    E_x,off:=sum_off V q_x^2
      <=n^4 Lambda_c+130000000 n^4 H.                         (12)

The unsimplified extra terms are 129440000 n^4 H+3904 n^4;
H>=1 absorbs 3904 into the unused 560000 n^4 H allowance in (12).

Set R=q_y-q_x. Equation (3) gives R^2<=2m^2+2A^2/d^2. The second estimate in (9) was proved using |a|<=1, so its proof also gives sum_off V/d^2<=976n^4. Since A<=2,

    sum_off V R^2 <=2m^2 Lambda_c+7808n^4.

Finally q_y^2<=(q_x+R)^2<=2q_x^2+2R^2, so (12) yields

    W_off <=3E_x,off+4m^2 Lambda_c+15616n^4
      <=6 n^4 Lambda_c+391000000 n^4 H.                       (13)

The final weakening uses 4m^2/n^4<=9/4 for n>=2, H>=1, and 15616<1000000.

### 5. Removable index and logarithmic absorption

PD-T227 gives |L_00(c)|=1/m, |L_00,x(c)|=(2n^2+1)/(6m), and |L_00,y(c)|=(2n+1)/6. Thus its energy is at most

    n^4/(4m)+mn^2/4 < n^4 <= n^4 Lambda_c.                    (14)

We claim H<=11 Lambda_c for every n>=2. If log n<20 then H<22, while Lambda_c>=2. If L=log n>=20 then

    Lambda_c >=(4/pi^2)L^2-54 >=.4L^2-54 >=.265L^2>5L,
    H<=1+L+log(3/2)<L+1.5<2L.

This proves the claim. Combining (6), (13), (14), and H<=11Lambda_c gives

    W_n <=[10007+11*391000000] n^4 Lambda_c
         <10^10 n^4 Lambda_c.

This is (1). QED.

## Checks

Analytic proof only. No new computation was executed for this claim; the earlier finite energy measurements were read as context, not used as premises. A separate agent should reconstruct (3), (5), diagonal bounds, the multiplicities in (10)--(11), and all endpoint cases. Supplementary check and Claude audit remain pending at creation.

## Sources and scope

No external theorem is imported and no historical originality is claimed. This is a quantitative continuation of the existing weighted-energy mechanism. It proves the n^4 Lambda_c energy scale with an explicit very loose constant; it does not prove the conjectural constant 1 from PD-T227.

The measured predecessor is [PD-T233](../../padua-argmax-alln-20261101/theory/prep-codex-02-d2-corner-screen.md),
the finite corner slope and weighted-energy screen. Its observations are
context only; no sampled value supplies this analytic all-degree bound.

The known per-cardinal affine obstruction remains intact. The pointwise Hessian/Markov shortcut controls Taylor remainders but does not by itself control affine sign crossings; (1) supplies the missing aggregate control through PD-T227's scalar inequality.

## Open items

A usable constant is not supplied: 10^10 is many orders above the measured energy. A local radius follows from PD-T227 and PD-T251 once a global norm ratio Lambda_n<=K Lambda_c is supplied; an explicit K gives an explicit radius. The present file does not import a non-effective K as an explicit number. Practical phase coverage, the effective global bridge, and PD-T099 remain separate.

## History

2026-11-05, Codex mathematical subagent, parent-assigned gpt-6-astra ultra under AC's explicit campaign allocation; input/rules ed21cc0bf205549936fccde90244a291bc6de324. Parent granted this file after an initial no-write analysis assignment. No Git operations, large compute, or edits outside this file. The result closes a previously specified quantitative premise rather than claiming a new historical mechanism; the surrounding H3 candidate/gate records are maintained by the parent.

2026-11-05 audit response, Codex, gpt-6-astra ultra: F6/F9 cite PD-T233
and the precise PD-T228 reflection argument, with a routine status row.
E2/E7 disambiguate symbols and spell out the sinc range, weighted-average,
square, harmonic and constant-absorption facts already used. The original
Statement and every numbered proof assertion are unchanged; these are
explanations of the accepted proof, not a new mathematical result or premise.
First-writing pending-review notes in Checks describe that historical stage;
audit-01 accepts the original scope, and the record response check is pending.

## Registration — 2026-11-05

Final ID: **PD-T367**. Preserved provisional alias: `PD-T?argmax-effective-2-codex-05`.
Registration input/rules: `5821c3f130ec0b1e33ad1d01620b67620e1f0be1`.

The existing every-n>=2 weighted-energy estimate is registered as completion of the PD-T227 premise. PD-T233 is a measured predecessor only, not a proof premise.

[Claude audit-01](../audit-01.md) accepted the mathematical scope;
[response-check-01](../response-check-01.md) accepted the record response.
Earlier provisional/no-final-ID and pending-response-check wording above
is retained as history and is superseded only administratively by this
registration. Every pre-existing paragraph after the heading, including
Statement, proof, status, displays and History, is preserved byte for byte.
The [final-ID map](../preparation/final-id-map.json) and
[registration notes](../preparation/registration-notes.md) record the mapping
and preparation limits. PD-T099 remains OPEN; the global certified range
remains exactly 2–32.
