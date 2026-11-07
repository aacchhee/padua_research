# Independent supplementary review of N1 round 6

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Input head
`88e702321cd5d9c3395a551fc8a55a2f7cb8bc10`. AGENTS, WORKFLOW and CODEX
were read in the preceding reviews; their diff from the round-5 input
`fc8c2885f47b08cecc7f65328db0e740cbc205ea` is empty. This is a
supplementary mathematical review, not the required Claude audit.

## Frozen scope and method

| Source | SHA-256 |
|---|---|
| N1-13, `theory/N1-round6-regular-variation.md` | `722e4ce4c275fee5217f4b473384985fa84789b869019077be49c9b2319bc74f` |
| N1-14, `theory/N1-round6-central-log.md` | `9a3f4d3f123ce82be5199a7631c8ead317ed15415b29dee44d126ead8bbbceb1` |

Read both frozen proofs and `ideas/N1-round6.md`; the prior N1/N2
definitions and the supporting differentiated-series and variation
arguments were read in the preceding reviews. Their reports and all
developer sources remain untouched. `git rev-parse HEAD`, a read-only
rules diff, source reads and `sha256sum` establish provenance. No
numerical fit, mathematical program or computational rerun was performed.

This is a quantitative completion check within the same corrected
IDEA-337/459 model. No new mechanism, priority claim or registry
disposition is assessed. The workflow's no-novelty review exception
applies; a new full IDEAS read is not claimed.

## N1-13: accepted at the written regular-profile scope

No mathematical finding remains in the frozen N1-13 proof.

The two exact max formulas remain valid for the entire folded half,
since T=2a cot(z/2)>=0 through z=pi. Their max terms increase as T
decreases, while u=T-4a/z decreases from zero to -4a/pi. The combined
max-term variation is 2max(p,q). Thus the two normalized variations
sum to at most 2max(p,q)/pi+8a/pi²; either sup norm is at most
max(p,q)/pi+4a/pi². With max(p,q)<=1/2 and pi>31/10 these give
the claimed 6/5 and 3/5, including every branch switch.

The N1-10 differentiated R series bounds hold throughout 0<t<=1/2;
its denominators only used k²-t²>=3k²/4. Hence |Phi0''|<35 on each
open period. If c=2gamma-2log pi, the one-sided derivatives at an
integer are -c and c, so the derivative jump is exactly 2c and has
magnitude below 6. Each composed argument travels half a period at
speed 1/(2pi), giving derivative variation at most
(35/2+6)/(2pi)=47/(4pi). Combining both nonnegative weights yields
Var(N_s')<=47/(2pi). The inherited sup and Lipschitz bounds also give
||N_s||<=8, Lip(N_s)<=12/pi and Var(N_s)<=12. Possible seam crossings
and endpoint one-sided derivatives have not been omitted.

For d0=1/[2sin(z/2)]-1/z, its derivative is nonnegative exactly when
sin²x>=x² cos x, x=z/2. Differentiation of the latter difference gives
x²sin x-2cos x(x-sin x), bounded below by
x³(2/pi-1/3)>=0. Thus d0 increases from zero to 1/2-1/pi.
The quotient [N_s(z)-N_s(0)]/z equals integral_0^1 N_s'(tz)dt.
For any partition in z, integrating its variation sum bounds it by
Var(N_s'); no derivative at a seam is required. Product variation
then gives

    Var(P_s)<=47/(2pi)+(8+12)(1/2-1/pi)
             =10+7/(2pi),
    ||P_s||<=12/pi+8(1/2-1/pi)=4+4/pi.

These imply the combined bound 23 and the individual bound 6. The
z=0 limits are the previously derived +U1 and -U1. No inverse phase
distance enters any bound.

A center sample differs from its cell mean by at most half that cell's
variation. On disjoint cell unions, summing their variations costs at
most the whole-half variation, independently of the number of holes.
The normalization 1/m therefore gives [(6/5)L+23]/(2m) exactly.
At n>=10^6, log n/n decreases sufficiently that the bound is below
(16.8+23)/(2*10^6)=1.99e-5<1/50000. This review does not replace or
extend any cell boundary in applying that estimate.

## N1-14: accepted at the written central-logarithm scope

No mathematical finding remains in the frozen N1-14 proof.

For same-sign coefficients c=(u-s)/2,b=(u+s)/2, the two cancellation
intervals each have length epsilon and are split where
sin(2x+epsilon)=(s/u)sin epsilon. With
theta=arcsin((s/u)sin epsilon), the identities

    sin y0 cos y1=(1-s/u)sin epsilon/2,
    sin y1 cos y0=(1+s/u)sin epsilon/2

give c*sin epsilon/u and b*sin epsilon/u respectively. In the integrated
formula all log(sin epsilon) terms cancel, leaving precisely
2[c log(c/u)+b log(b/u)]. Thus the separation-independent entropy
formula and its factor two are correct. Its nonzero limit as epsilon
tends to zero is a subtracted-integral limit, not the coincident-pole
integral evaluated first.

For opposite signs (-c,b), with c=(s-u)/2,b=(s+u)/2, the numerator
of their sum on the positive long interval is
[u sin(2x+epsilon)-s sin epsilon]/2. If s sin epsilon>=u it is
nonpositive throughout and integration gives 2s log(sin epsilon).
Otherwise it changes sign at the stated x1,x2. On their intervening
interval the smaller channel changes from b cot(x+epsilon) to
c cot x. Its integrated correction is exactly
2[b log(cos x1/sin(x1+epsilon))
  -c log(cos(x1+epsilon)/sin x1)], since
sin(x2+epsilon)=cos x1 and sin x2=cos(x1+epsilon).
The other long interval always uses c. This reconstructs (3)-(4).

At the moving roots, b cot(x1+epsilon)=c cot x1 and
b tan x1=c tan(x1+epsilon), so root-motion terms cancel on
differentiation. With D=u cos theta, the remaining derivative of R
is exactly 2[u cos epsilon-D]/sin epsilon. Since s>u implies
D<=u cos epsilon, it is nonnegative; it increases with s until the
no-root value 2u cot epsilon. The other derivative is

    R_s=log[sin(theta-epsilon)/sin(theta+epsilon)]
       =log[(s cos epsilon-D)/(s cos epsilon+D)].

It lies between log((s-u)/(s+u)) and zero. In the same-sign regime,
direct differentiation of entropy gives log((u+s)/(u-s)). Thus the
common absolute derivative bound (8) is correct on both sides of s=u;
its singularity there is integrable.

As epsilon tends to zero in the opposite-sign root formula,
x1~c*epsilon/u and x1+epsilon~b*epsilon/u. Substitution gives exactly
R(u,s,0)=2[c log c+u log u-b log b]. Since b=c+u, the entropy
inequality bounds its magnitude by 2b log 2=(s+u)log 2. R increases
from this value to zero. The same-sign bound is 2u log 2. When u=0,
J=2s log(sin epsilon) and R=0 identically, so no division by u is used.

The integral in (9) is obtained directly by integrating the two logs;
the difference between x log x at S+u and S-u is bounded by
2u[1+log(S+u)]. Subtracting 2u log u gives the stated majorant.
It increases with u and at u=1/4 equals (1+log 6)/2<3/2.
Pointwise monotonicity of R_epsilon in s then dominates an arbitrary
path s(epsilon)<=S by the fixed S derivative, whose integral is
-R(u,S,0)<(S+u)log 2<21/20. These steps do not bound a small phase
logarithm independently and then drop it.

For the actual left central row, cot((pi-epsilon)/2)=tan(epsilon/2)
gives u=p/2 and s=q/2+a tan(epsilon/2); reflecting its separation
gives J. On the right, coefficient exchange replaces
q/2-a tan(epsilon/2) by its absolute value. The left path is monotone
and the right has at most two monotone pieces, all within [0,5/4].
Their parameter-motion variations total less than 3*(3/2), and the
two explicit-separation variations total less than 2*(21/20).
The resulting 33/5 bound is exactly (12). The integrable derivative
bounds permit passage through s=u and the root thresholds.

The common central coefficient is
k_s(0)=2(q/2-p/2)_+=(q-p)_+=d. Positive-part and absolute-value
Lipschitz continuity give |k_s-d|<=2a tan(epsilon/2), and
|k_s'|<=2a since sec²(epsilon/2)<=2. Therefore the decomposition
(13) is exact. For its last two terms, product variation costs
a*pi*log 2+a*pi/2+d log(pi/2)<81/20: the first integral is
(pi/2)log 2, while tan(epsilon/2)cot epsilon
=cos epsilon/(1+cos epsilon)<=1/2. Two copies plus 33/5 give
147/10<15, with no inverse d or p.

For the sup bound, |R|<21/20, tan(epsilon/2)<=epsilon and
epsilon log(pi/(2epsilon))<3/5 give at most 6/5 for the middle
term; the last term has magnitude below 1/4. Hence |Z_s|<5/2<3.
The last two terms tend to zero at the origin. At q=p>0, the
remaining entropy tends to zero on either side of s=u. At p=q=0,
R=0 and k_s=2a tan(epsilon/2), giving the same zero limit. For the
other fixed phases the displayed entropy formulas give the common
finite limit directly. They are continuous as coefficients vanish
using x log x->0. Thus no actual central sample or collision value
has been assigned from a divergent separate-channel expression.

## N1-15: accepted at the written fixed-count near-model scope

Additional frozen file `theory/N1-round6-near-model.md`, SHA-256
`ca3b98dc209a27fde2924ac9f4112111fe5be7b4e520d8b68ed0c8b20b50ea63`.
The full proof was read and its identity checked. No mathematical
finding remains in N1-15.

On rho<=1/2 the only integer offsets in 0<v<2pi occur at
v=pi-alpha+beta and v=pi+alpha+beta. Thus testing these two candidate
rows, adjoining m-1,m, and merging duplicates enumerates the complete
nonendpoint special set without a row scan. The test remains the actual
grid-pole condition, so an integer angular formula alone is not used
as an unchecked substitute. Both collision points are retained where
distinct; coincident points use the original polynomial convention.

After the strip cutoff, each folded half has ordinary indices
K_s+1,...,m-2. Their first cell starts at h(K_s+t_s+1/2), and their
last ends at h(m-3/2+t_s), exactly as in the model. The left and right
distances of the last endpoints from pi are (3/2-beta/pi)h and
(1/2+beta/pi)h. They are positive and at least h/2. In particular
beta=0 has one actual row at pi, already special, rather than two
ordinary folded samples. A collision-center removal removes its full
cell inside the same aligned cell union. Two collision rows create at
most two holes and at most four total component intervals. The initial
cell boundary is strictly greater than delta-h/2>499/500000.

The decomposition H=Q_L/z+L*f_s+P_s+I_s/pi is exact, with
Q_L=4aL/pi+U0. Normalized centered-cell quadrature has error kernel
h²/(8pi) against the absolute second derivative. On two halves the
integral of (1/z)'' is at most 2/ell², giving
pi*|Q_L|/(4m²ell²)<=(L+2pi)/(m²ell²). With log n<14 at n=10^6,
pi<4 and the fixed lower bound on ell, this is below 1/40000;
the scalar majorant decreases thereafter. N1-13 independently supplies
the regular error below 1/50000, without a multiplier for holes.

Splitting the I cells by centers at pi/2+h/2 ensures that every
central cell lies above pi/2 and every remaining cell lies below
pi/2+h<8/5. The complete numerator stays positive up to 8/5 using
cos z>=-3/100, a>=15/16 and P<=1/2. Beyond pi/2 this gives the
no-root condition in N1-14 for separation pi-z. Thus the endpoint
formula (2a cot(z/2)+q_s)log(sin z) remains valid over the slightly
extended endpoint cells; it is not used beyond its proved sign regime.

Differentiating that formula twice, with T=2a cot(z/2), gives
T'' log(sin z)+2T'cot z-(T+q_s)csc²z. The stated sine bounds imply
|T''|<=12a/z³, |2T'cot z|<=12a/z³, and the last term has magnitude
at most 16a/z³+4q/z². Hence the author's looser bound
14a[log(2/z)+2]/z³+4q/z² is valid. Integration over the two cell unions
is bounded by 14a[log(2/ell)+5/2]/ell²+8q/ell as claimed. Including
the extra I/pi factor gives normalization 1/(8m²), and ell's lower
bound with log(2/ell)<8 proves the error below 1/50000.

For the central residue, normalized BV quadrature is
Var(Z_L,Z_R)/(2pi*m)<15/(2pi*m)<1/400000. For the central logarithm,
the integrated absolute second derivative over the two cell unions
is at most 4/h. Multiplication by d*h²/(8pi²) gives exactly
d/(2pi*m)<1/10^6. This treatment keeps the actual half-cell distances
and never evaluates log zero. All six errors sum to
1/40000+2/50000+1/400000+1/10^6<1/14000.

For special-row harmonic compaction, the first eight reciprocal samples
are exact. The remaining centered cells start at y+15/2 and end at
y+q-1/2. The integral is exactly the displayed logarithm, and its
midpoint error is bounded by
(1/8) integral_(y+15/2)^infinity 2x^-3 dx
=1/[8(y+15/2)²]<=1/450. This bound is uniform as y approaches zero.
The reversed second progression has positive start n-e-t, so the
same estimate applies to both pole subtractions in every block.

The sign conditions have at most four arc endpoints. Even separately
allowing the two collision exclusions, the two exact numerator-zero
exclusions and a coordinate cut for either cotangent circle leaves
fewer than twelve contiguous blocks; tangent or coincident endpoints
cannot increase that count. If the numerator is identically zero,
N1-01's zero exclusion leaves no regular negative indices and hence
no blocks, rather than an unbounded list of zero exclusions.
Thus each channel's Q error is at most
24/(450*h_inner). The Rhat coefficients contribute a factor
2(|C|+|D|). All these rows lie within 1/2 of pi, where tan(1/4)<1/3
gives |C|+|D|<1. Four rows and h_inner=pi/n therefore give exactly
192/(450*pi*m)<1/10^6 after division by nm.

The signed-row term, W and w' terms are closed functions; the arcs give
a bounded number of scalar grid cutoffs. The collision values use
k sin(kv)/sin v with its finite endpoint limits, so their definition
does not require expanding a degree-n polynomial. These observations,
together with the already checked finite-h endpoint terms, confirm the
fixed evaluation count. The integrals remain exact model functions,
not a claim of completed interval evaluation.

The resulting additional error is below 1/14000+1/10^6<1/7000.
Adding the unchanged round-5 error below 1/14000 proves the stated
total <3/14000<1/4096. No fitted coefficient, added row correction,
discarded ordinary interval or growing hidden sum is used.

## Completion and limits

All three frozen proofs pass at their exact written scopes, with no
unresolved finding. The near-phase representation now has the stated
fixed count and uniform total error <3/14000. Certified evaluation of
its integrals/functions, a maximum comparison, far-phase coverage,
full B3 PASS and an effective onset remain open. No formal Claude audit
or computational verification is claimed. All developer sources and
earlier reports were left unchanged.
