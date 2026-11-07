# PD-T?argmax-bridge-C01-effective-global — a numerical global primitive constant

ID kind: PD-T.
Aliases: quantitative PD-T216; full-diamond explicit logarithmic remainder.
Split from: the numerical-constant obligation in the explicit continuation
of PD-T229/PD-T099. The argmax assembly is a separate record.
Split into: none.

## Statement

For every integer `n>=64`, let `m=n+1`, `N=nm`, and use exactly PD-T216's
corrected kernel and primitive:

\[
F_{jr}(\alpha,\beta)=\frac{(-1)^j}{2}
 G_n((j\pi+\alpha)/n,(r\pi+\beta)/m),\quad
S_n=\frac1N\sum_{\Gamma^-}|F_{jr}|,
\]
\[
\Gamma^-=\{0\le j<2n,\ 0\le r<2m:j+r\text{ odd}\},\quad
a=\frac{\cos\alpha+\cos\beta}{2}.
\]

For all real phases in the closed diamond `|alpha|+|beta|<=pi`,

\[
\boxed{S_n(\alpha,\beta)\le a\Lambda_c(n)
                         +10^6\log(n+1).}                 \tag{1}
\]

All collisions, exact zeros, phase-diamond vertices and boundaries are
included. The constant is intentionally loose.

## Definitions and assumptions

`G_n(u,v)=D_n(u,v)-cos(nu)`, where `D_n` is PD-T185's finite polynomial
divided difference of `P_n=T_m+T_n`. Every apparent quotient collision is
evaluated by this polynomial. Set `H=1+log m`. The physical odd board is
`O={(j,r):0<=j<=n,0<=r<=m,j+r odd}`; its endpoint factors `e_j,f_r`
are one half at an endpoint and one otherwise. Exact real arithmetic.
No maximizer, defect or energy assumption is made.

## Status by part

Overall status: **PROVED**, by the numerical analytic extraction below.
Distinct reconstruction is required before the parent publishes a global
argmax-onset conclusion; the present lemma has no numerical-run premise.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Explicit global primitive bound (1), `n>=64` | PROVED | Written strip, endpoint and far-mesh estimates below; no useful constant optimization claimed |

Candidate disposition: retained quantitative explicit-constant variant of
PD-T216, not a new mechanism or a historical novelty claim.

## Depends on

PD-T185's finite polynomial divided difference; PD-T216's exact phase
numerator and endpoint-weighted four-reflection identity; its zero-phase
normalization `S_n(0,0)=Lambda_c(n)` (PD-T189). The estimates needed to
replace every O-constant in PD-T216 are proved here with numerical bounds.

## Proof

### 1. Exact algebra and the partition

PD-T216 gives, including endpoint multiplicities,

\[
S_n=\frac1N\sum_O e_jf_r
           \sum_{\sigma,\tau=\pm1}|F_{jr}(\sigma\alpha,\tau\beta)|.
                                                               \tag{2}
\]

Write `u0=j*pi/n`, `v0=r*pi/m`. When the cosines differ, its numerator
identity is

\[
F=af-\tfrac12\sin\alpha\,g_u+\tfrac12\sin\beta\,g_v,
\quad f=\frac{1+\cos v}{\cos u-\cos v},\quad
g_u=\frac{\sin u}{\cos u-\cos v},\quad
g_v=\frac{\sin v}{\cos u-\cos v}.                         \tag{3}
\]

The phase signs in (3) are changed with the reflected phases. On the
closed diamond `0<=a<=1`, since
`a=cos((alpha+beta)/2)cos((alpha-beta)/2)`.

Partition `O` into the endpoint set `E` (a first or second endpoint), the
interior strip `B` defined by `|u0-v0|<=8*pi/n`, and the remaining interior
far set `R`. On interior indices every shifted angle belongs to `[0,pi]`:
the coordinate shifts have sizes at most `pi/n`, `pi/m`. The endpoint
set is treated by the polynomial or by a separated rational quotient.

In the strip, compare the shifted absolute sum and `a` times the
zero-phase absolute sum separately. On the far set compare (3) with
`a f(u0,v0)`; the denominator is then uniformly nonzero. At zero phase on
`R`, `F(0,0)=f(u0,v0)`. Thus the normalized zero-phase contributions
over all three sets add to precisely `a Lambda_c`; there is no missing
reference mass.

### 2. Elementary mesh sums

The sine chord inequality and the ordinary harmonic bounds give

\[
\sum_{j=1}^{n-1}\cot(u_0/2)\le nH,\qquad
\sum_{j=1}^{n-1}\csc^2(u_0/2)\le2n^2,\qquad
\sum_{j=1}^{n-1}\frac1{\sin u_0+1/n}\le nH.              \tag{4}
\]

Indeed `cot(j*pi/(2n))<=2n/(pi*j)` and
`sin(j*pi/(2n))>=j/n`. For the last sum use
`sin(j*pi/n)>=2 min(j,n-j)/n` and multiplicity at most two. The same
bounds with `m` replace `n` for the second mesh. We use
`sum k^-1<=1+log m=H` and `sum k^-2<=2`.

For a fixed first angle and a shifted second arithmetic mesh, retain only
terms with `|u-v|>=pi/m`. Since both angles are in `[0,pi]`,
`|sin((u-v)/2)|>=|u-v|/pi`. Each half-open distance shell
`q*pi/m<=|u-v|<(q+1)*pi/m`, `q>=1`, contains at most two mesh points.
Consequently

\[
\sum_r\csc^2((u-v)/2)\le8m^2,\qquad
\sum_r|\csc((u-v)/2)|\le4mH.                            \tag{5}
\]

The more direct bounds are `4m^2` and `2mH`; the displayed slack avoids
any endpoint convention issue. The analogous first-coordinate squared
sum is at most `8n^2`. We apply these bounds only after verifying the
retained far separation, so no fractional pole is allowed into a sum.

### 3. Interior diagonal strip, including polynomial collisions

For `|u0-v0|<=8*pi/n`, both shifted angles and the entire angular interval
between them lie within `10*pi/n` of `u0`. For any such angle `t`, put
`s=m sin t`. The Lipschitz bound for sine gives
`m sin u0<=s+11*pi`, because `m/n<=65/64`. Thus

\[
(1+m\sin u_0)\min(1,1/s)\le2+11\pi<37.                \tag{6}
\]

At `s=0` the minimum is interpreted as one. Since
`|T_k'(cos t)|<=min(k^2,k/|sin t|)` and `k<=m`,

\[
|P_n'(\cos t)|\le\frac{74m^2}{1+m\sin u_0}
              \le\frac{80n}{\sin u_0+1/n}.              \tag{7}
\]

For the second inequality, the ratio of
`m^2/(1+m z)` to `n^2/(1+n z)` is at most `(65/64)^2`, and
`74(65/64)^2<80`. The divided-difference mean-value theorem bounds
`|D_n(u,v)|` by (7), also at a collision by its derivative value.
After the factor one half and the bounded corrected cosine, the same
upper bound `80n/(sin u0+1/n)` safely bounds `|F|`: here
`n/(sin u0+1/n)>1`.

There are at most `16m/n+1<32` second indices in the strip for each
first index. Discarding parity and endpoint factors in positive errors,
the normalized strip sum over all four reflected phases is at most

\[
\frac{4\cdot32\cdot80n}{nm}
       \sum_{j=1}^{n-1}\frac1{\sin u_0+1/n}\le10240H.    \tag{8}
\]

The same bound applies at zero phase. Hence the strip contribution to
`S-a Lambda_c` is at most `20480H`. This includes all interior polynomial
collisions; no rational value is substituted there.

### 4. Endpoint rows and columns

Globally, the polynomial derivative bound gives

\[
|F|\le\tfrac12(m^2+n^2+1)\le m^2.                     \tag{9}
\]

For a first endpoint row, fold its first angle into `[0,pi]`. At the
lower endpoint its folded angle `u` is at most `pi/n`; for `r>=4` the
folded second angle satisfies `v>=(r-1)*pi/m`. Thus
`u/v<=65/192<3/8`. Using `pi^2<10`,

\[
\cos u-\cos v\ge(1/5-9/128)v^2>v^2/8.                 \tag{10}
\]

The numerator of `F` in the rational identity (3) has absolute value at
most `3`: its three terms are bounded by `2`, `1/2`, `1/2`.
Therefore for `r>=4`, since `pi^2>8`,

\[
|F|\le24/v^2\le\frac{3m^2}{(r-1)^2}.                 \tag{11}
\]

The four indices `r=0,1,2,3` cost at most `4m^2` by (9), including any
collisions. The tail in (11) costs at most `3m^2/2`, using
`sum_{s>=3}s^-2<=integral_2^infinity x^-2 dx=1/2`. Hence each first
endpoint row costs less than `10m^2`. The upper endpoint follows by
replacing the two folded angles by their complements and `r` by `m-r`;
the absolute numerator bound and cosine gap are unchanged.

For a second endpoint column, its folded angle is at most
`pi/m<=pi/n`, and the other angle is at least `(j-1)*pi/n`. The same
argument, with ratio at most `1/3`, bounds the tail by
`3n^2/(j-1)^2<=3m^2/(j-1)^2`; each column also costs less than `10m^2`.
It is harmless to count intersections twice. The union of four sides,
four phase reflections and normalization therefore cost at most
`160m^2/(nm)<256`. The zero-phase reference costs the same. Since
`0<=a<=1`, the full endpoint contribution to `S-a Lambda_c` is at most
`512`, hence at most `512H`.

### 5. Far denominators and the finite-deformation bound

Let `|u0-v0|>8*pi/n` and let `h,k` be shifts with
`|h|<=pi/n`, `|k|<=pi/m`. Along the coordinate rectangle, both angles
remain in `[0,pi]`. The difference, the sum and its distance from `2*pi`
are all bounded below at the base by `|u0-v0|`. A total displacement
at most `2*pi/n` therefore retains at least three quarters of each
relevant angular distance. Concavity of sine yields

\[
\sin((u+v)/2)\ge\tfrac34\sin((u_0+v_0)/2),\quad
|\sin((u-v)/2)|\ge\tfrac34|\sin((u_0-v_0)/2)|.           \tag{12}
\]

For a first-coordinate shift alone the factor is `7/8`. Before the
subsequent second-coordinate shift the separation exceeds `7*pi/n`;
its sine factors retain at least `6/7`, so the new cosine denominator
has magnitude at least one half of the preceding one. A first shift
has the same one-half denominator bound.

Put `T0=(u0-v0)/2`. Exact subtraction for the first shift, using
`|cos(u0+h)-cos u0|<=|h| sin u0+h^2/2`, gives

\[
|f(u_0+h,v_0)-f(u_0,v_0)|
\le2\{ |h|\cot(u_0/2)+h^2\csc^2(u_0/2)\}\csc^2T_0.    \tag{13}
\]

To check the coefficients directly, set
`D0=cos u0-cos v0=-2 sin((u0+v0)/2) sin T0` and use
`sin((u0+v0)/2)>=sin(u0/2)cos(v0/2)`. Then
`(1+cos v0)sin u0/D0^2<=cot(u0/2)csc^2T0` and
`(1+cos v0)/(2D0^2)<=csc^2(u0/2)csc^2T0/4`.

For the second shift the exact numerator is
`(1+cos(u0+h))(cos(v0+k)-cos v0)`. The corresponding inequality
`sin((u0+h+v0)/2)>=cos((u0+h)/2)sin(v0/2)` gives the same bound
in `v0`. The first shift's half-difference sine is at least `7/8` of
the original, so replacing it by `T0` costs less than two. Together,

\[
|f(u_0+h,v_0+k)-f(u_0,v_0)|
\le4\left[\frac\pi n\cot(u_0/2)+\frac{\pi^2}{n^2}\csc^2(u_0/2)
 +\frac\pi m\cot(v_0/2)+\frac{\pi^2}{m^2}\csc^2(v_0/2)\right]
 \csc^2T_0.                                            \tag{14}
\]

Sum (14) with (4)--(5), normalized by `1/N`, discarding parity. For
one phase the four bracket terms, including the factor four, cost at
most the following amounts; `m/n<=3/2`, `pi<4`, `pi^2<10` and `H>=1`
are sufficient for every entry.

| Term | Normalized upper bound |
|---|---:|
| first-coordinate cotangent | `192 H` |
| first-coordinate reciprocal square | `960 H` |
| second-coordinate cotangent | `128 H` |
| second-coordinate reciprocal square | `640 H` |

Their sum is `1920H`; four phases cost at most `7680H<8000H`.

For the two sine channels, for any `u,v in [0,pi]`,
`sin u,sin v<=2 sin((u+v)/2)`. Thus
`|g_u|,|g_v|<=|csc((u-v)/2)|`. Every far shifted difference exceeds
`6*pi/n`, so the first-power bound (5) applies. The channel sum in
(3) costs at most `4H` per phase, hence at most `16H` for four phases.

Finally `|F|-a|f0|<=a|f-f0|+|sine channels|`, with `a<=1`. This
proves the total stated far-set error without any signed differentiation
of an absolute value.

### 6. Combine

The endpoint, strip and far bounds give

\[
S_n-a\Lambda_c\le(512+20480+8000+16)H=29008H<30000H.
\]

Since `m>=3`, `H<=2 log m`. Hence the stronger numerical bound
`S_n<=a Lambda_c+60000 log m` follows, and certainly (1). QED.

## Checks, sources and scope

Analytic proof only. No finite-degree test, floating bound, fit or
unperformed numerical execution is a premise. The full PD-T216 proof was
read before extracting constants; (6)--(14) make its previously implicit
uniform estimates explicit. This file changes none of the old proof
records. The literal global argmax conclusion requires the separately
recorded local/defect/corner assembly and independent reconstruction.

No historical novelty or first-explicit-constant claim is made. The
candidate gate and considered alternatives are in
[ideas/C01-effective.md](../ideas/C01-effective.md).

## Open items and history

Distinct mathematical reconstruction and the campaign's required Claude
audit remain review obligations, not mathematical hypotheses. Any finding
must be recorded and answered before publishing the assembled onset.
2026-11-06, auxiliary Codex developer; parent-assigned mathematics,
serving model/effort not independently exposed. Rules/input
`4b728b04216a5490910780bc609a82b853058426`.
