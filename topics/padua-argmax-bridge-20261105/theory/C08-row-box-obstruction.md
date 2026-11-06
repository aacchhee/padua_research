# C08 — scoped work obstruction for direct moving-root enumeration

Rules 4b728b0; 2026-11-06. Technical route limitation, no new global
negative ID or historical novelty claim. Preregistered with the C08
contract. **PROVED analytic developer result; distinct review pending.**
No experiment, root count fit or full-board execution is a premise.

## Exact scope

Consider the particular whole-box row method that puts EVERY integer
index swept by a moving numerator root into a direct set and evaluates
that finite primitive individually. On the actual Padua phase boxes

    beta=0,    alpha in [3pi/4,3pi/4+w],
    0<w<=pi/16,    n>=128, m=n+1,                     (1)

the sum of those direct counts over ordinary rows satisfies

    sum_r |B_r| >= (m/3-1)*floor(n*w/(8pi)).            (2)

Thus for fixed w>0 this route can require Omega(n^2*w) direct work.
It is not a theorem that every validated whole-box S algorithm has
quadratic cost, nor that narrower boxes cannot meet C08's O(n) guard.
It does not reject the partial-sum backend, exact row identity or
any possible bound that aggregates uncertain samples without enumeration.

## Proof

Retain the row conventions and four extracted rows of C08's contract.
Choose every integer r such that

    pi/3<=v=r*pi/m<=2pi/3.

There are at least m/3-1 such integers. For n>=128 none is an extracted
endpoint or central row. On beta=0, p=sin alpha>0 and

    g=c/p=cot(alpha/2)*(1+cos v).                     (3)

For (1), 1/2<=1+cos v<=3/2. Also

    1/4 < cot(13pi/32) <= cot(alpha/2)
                       <=cot(3pi/8)=sqrt(2)-1<1/2.

For the strict lower bound, 13pi/32<5pi/12 and
cot(5pi/12)=2-sqrt(3)>1/4; the last comparison is equivalent to
sqrt(3)<7/4. Therefore 1/8<g<3/4 throughout the box. The first root
theta(alpha)=asin g is uniformly interior and differentiable. From (3),

    |g_alpha|=(1/2)csc^2(alpha/2)*(1+cos v)>=1/4,
    theta_alpha=g_alpha/sqrt(1-g^2)<=-1/4.

Its exact real index is

    t(alpha)=[n*theta(alpha)-alpha-delta*pi]/(2pi).

Thus t is decreasing and

    |t_alpha|>=n/(8pi)+1/(2pi),
    width(t([3pi/4,3pi/4+w]))>=n*w/(8pi).             (4)

This is a continuous image interval, so every integer inside it is
attained at some phase, not merely included by an overestimated ball.
The root stays inside the physical row index range: theta>g>1/8 and
lambda<=1 imply t>n/(16pi)-1>0 for n>=128 using pi<4. Also
theta<asin(3/4)<pi/3 implies t<n/6<n-1. There is no clipping loss.

Every closed interval of length L contains at least floor L integers.
Consequently each of these rows has at least floor(n*w/(8pi)) genuinely
swept root indices. They must all be direct under the method's defining
rule. Counts in different rows are distinct primitive entries, so adding
them proves (2). Ordinary denominator collisions can coincide with some
of these indices but do not remove their direct-evaluation obligation.
All phase points in (1) lie in the closed first-quadrant triangle.

## Tangency warning, separately scoped

The inverse-sine square-root width is also realized by actual Padua rows.
Take odd n>=13, beta=0, r=m/2 and

    alpha in [pi/2,pi/2+w],       0<w<=1/16.

Then v=pi/2, g=cot(alpha/2), and g starts at1. Since
|(cot(alpha/2))'|=(1/2)csc^2(alpha/2)>=1/2, its endpoint decrement is
at least w/2. If d=arccos(g_endpoint), the bound
1-cos d<=d^2/2 gives d>=sqrt(w). The root theta=asin g therefore
moves by at least sqrt(w); the root index n*theta/(2pi)-lambda moves
by at least n*sqrt(w)/(2pi). This explains why the generic tangent
band is not O(phasewidth), and why C08 uses the Hölder guard.

This last example is a one-row warning and does not by itself obstruct
O(n) TOTAL work: the unavoidable O(n) row/retained work can dominate
one O(n*sqrt(w)) band. The many-row lower bound (2), rather than this
single tangent example, supplies the quadratic fixed-width limitation.

No stronger lower bound, derivative obstruction for the finite polynomial,
or impossibility of a coefficient-relaxation/convexity alternative follows.
