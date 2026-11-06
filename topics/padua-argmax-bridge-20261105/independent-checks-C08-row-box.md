# C08 phase-box contract and enumeration obstruction — independent check

2026-11-06. Input head
`547a473a6e1c1268ff4f1ada7243b12afb02d0bc`, incorporating new main76ba421.
AGENTS/WORKFLOW/CODEX were read in this reviewer's preceding C07 work at
`e8fad1671fb736247e4c510284f6f935e6345efb`; the coordinator confirms those
rules are unchanged at this input. Distinct Codex supplementary reviewer,
assigned Astra high; actual serving model/effort metadata independently
unexposed. Formal Claude audit remains separate.

**ACCEPTED within the stated analytic scopes. No unresolved mathematical
finding.** The whole-box contract proves enclosure correctness when its
complete root covers, fixed-core signs, primitive enclosures and C06
guards hold. Its arithmetic work is O(n+sum_r|B_r|), with O(n) requiring
an explicit ambiguity budget. The separate actual-Padua family proves
the claimed lower bound for individual evaluation of all swept numerator
root indices. Neither result establishes uniform O(n) work on arbitrary
boxes, useful numerical contraction at fixed C06 orders, or an implemented
whole-box certifier.

Frozen files read and independently reconstructed:

| File | SHA256 |
| --- | --- |
| theory/C08-row-box-contract.md | `7c29e35b509cefcb9bb01f88a078ca46822221afce54c2a7bcd8d5de8565602f` |
| theory/C08-row-box-obstruction.md | `283eca3471dc74953af5ef246c84d38200dca6a554432e2bcd938c213b443256` |

Also read the C08 idea/attempt, accepted C02 mathematics and C06/C07
implementation contracts/reviews. This reviewer performed the latter
implementation reviews and retains their source/interface reconstruction.
The present review checks validity and scope of the frozen analytic
claims, not novelty, priority, or originality of alternatives. Accordingly
no new historical novelty claim or full registry gate is made. A focused
current-registry search covered NN-MOP, moving/swept roots, root bands,
whole boxes and uncertain-band/coefficient-relaxation terms; the NN-MOP
recurrence/conditioning additions do not change these mathematical
dependencies. The developer's older complete novelty-gate record is
historical, not represented as a refreshed gate at the merged head.

No executable was developed or run; no scalar experiment, timing fit,
degree test or full-board computation is a premise. Source hash checks
were read-only. Only this independent report was written; no author,
old-review, shared or Git state was changed.

## Closed bands and complete index coverage

P is a nonempty rectangle/half-plane intersection, hence convex and
connected, including degenerate segments and singleton vertices. The
physical labels lambda=(delta+alpha/pi)/2 remain continuous on P.
Replacing lambda by its fractional part could shift a label at lambda=1;
the contract correctly forbids that. Optional direct endpoints0,n-1
remove seam ambiguity at a cost of at most two samples per row.

For ordinary rows, the four retained labels cover every possible
v=0,pi,2pi throughout the whole rectangle B. Solving u=v and u=2pi-v
gives exactly the two affine denominator-root coordinates(3). Each has
absolute alpha coefficient1/(2pi) and absolute beta coefficient
n/(2pi m). Thus its exact interval width is

    d_D=(w_alpha+(n/m)w_beta)/(2pi)
        <=(1+n/m)/2<1.

A closed interval of length strictly below1 contains at most one integer.
Numerical enlargement is explicitly counted using the actual width;
the exact-width result does not justify dropping an extra rounded index.

The numerator formula F=(c-p*sin u)/(2(cos u-cos v)) has the N2 sign
and the correct factor1/2. On B, p>=0. Consequently lower(c)>upper(p)
or upper(c)<-upper(p) is a sufficient root-free test without division,
including some p=0 boxes. Otherwise the required positive lower bound
p>=p0 permits division and the resulting Gamma encloses the actual
threshold for every relevant phase. Discarding Gamma only when it misses
[-1,1] is valid; intersecting with that closed interval preserves all
thresholds at which a sine root exists.

For J=asin(Gamma intersect[-1,1]), every root in[0,2pi] is in J,pi-J,
or J+2pi. This covers both seam representatives and both tangent values.
The extra candidates when a phase has no true roots are conservative.
Taking the product with the alpha interval before the affine index map
may overestimate correlation, but never loses a root. Its width is at
most n*width(J)/(2pi)+w_alpha/(2pi), as stated in(7).

For a closed band[l,u], every possibly coinciding integer is exactly in
the clipped ceil(l)..floor(u) set. Equality must be retained and is
retained, including a zero/collision occurring only on the closed phase
boundary. If the integer set is empty, a root may still lie strictly
between two grid points; the cut at ceil(l) prevents their merger.
Clipping such a cut to0 or n only affects roots outside the sampled grid.

Each real root band contributes at most one removed contiguous integer
range, or one empty-band cut. Merging overlaps and duplicate direct
indices cannot increase this count. Adding two seam singleton bands
gives at most seven components/cuts and at most eight remaining integer
cores; the looser12-block allowance is safe. The construction partitions
all indices exactly once into direct samples and cores. Each direct
range gets cuts at its endpoints, so removing it cannot accidentally
remove neighboring nondirect samples.

The maximum number of integers in a closed width-d interval is
floor(d)+1, including integer d. This proves(9). With two collision
bands of width<1, three numerator bands of width<=d_I and two seam
samples, it gives2+2+3(floor(d_I)+1)=7+3floor(d_I), clipped by n,
exactly(10). This is a new box budget, not C07's point-only limit5.

## Whole-core signs, wraps and valid C06 input balls

For a remaining core[a,b], complete band exclusion removes every
numerator/denominator zero on[a,b] times P. Both functions are continuous
on that connected set. Each therefore has a single strict sign, so one
certified representative sign determines the whole core for all phases.
A sampled midpoint sign without certification would not suffice; the
contract expressly rejects that shortcut. A separately proved identically
zero core is also harmless. This argument does not assume the moving
integer selection is differentiable.

Both channel wraps occur at denominator collisions: u=v for the minus
channel and u=2pi-v for the plus channel. The excluded bands thus also
make the integer wrap constant on each connected core/phase domain.
With exact integer ell, the channel start

    y=a+lambda +/- n*v/(2pi)-n*ell

has the stated affine interval width d_D over B. The true core can be
root-free over P while a larger B enclosure is too wide; the resulting
C06 failure is an allowed conservative rejection. A proposed wrap is
usable only after the literal whole-ball guards0<y and y+qcount-1<n
certify it. They exclude both endpoints and every pole, regardless of
zero coefficients or possible cancellation in another expression.

The accepted C06 native contract encloses the entire image of its input
offset ball. Its exact-rational midpoint moments have a separately
proved derivative-times-input-radius extension; it is not merely a
point routine being reused with an interval parameter. Therefore every
phase's partial sum is enclosed by the one successful call. The original
LP64 n ceiling, fixed160/640 precisions, wide-ball rejection and rational
bit-cost caveat remain dependencies of any actual implementation.

If p can vanish and no complete special root cover is available, this
construction cannot infer an empty numerator-root set. At c=p=0 for
some phase, every real index is a numerator zero at that phase, which
would invalidate the preceding no-zero argument. The contract explicitly
requires failure or a proved, charged fallback instead. No axis or
closed-boundary phase is silently removed from the target domain.

## Row identity and full error budget

For every phase, the negative cores use the correct C,D pair and signed
row T from N2/C02. Their fixed decomposition is valid simultaneously
over P. Each direct index contributes2max(-F,0), retaining its parity,
factor1/2 and complete finite-primitive ball. Thus(14) is precisely

    sum|F| = sum F + 2sum(-F)_+

with each sample counted once. Interval max, multiplication and addition
preserve pointwise inclusion despite correlation. The four retained rows
use abs(F) directly. Dividing the full sum by positive N gives S(P).
Intersecting with[0,infinity) is valid because S is nonnegative.

For the separate analytic charge, the ordinary coefficient inequality
is |C|+|D|<=1+a_*|cot(v/2)|. For any beta in[0,pi], the row's distance
from0 or2pi is at least pi*min(r,2m-r-1)/m. Combining |cot(v/2)|<=2/dist
with two copies of each harmonic index1,...,n proves

    sum_r sup_P(|C_r|+|D_r|)
        <=2m+(4a_*m/pi)H_n.

Taking each row's supremum separately is therefore legitimate: the
distance bound holds uniformly row by row. No interchange of supremum
and a phase-dependent cancellation is being used.

In either channel, disjoint fixed negative cores contain at most n
samples and at most12 blocks. The C02 smooth error consequently sums
to7n*h^4*M_J/5760; harmonic error sums to24eta/h. Multiplying by
2(|C|+|D|), summing all ordinary rows and dividing by nm gives exactly

    [7*pi^4*M_J/(2880*n^4)+48eta/pi]
      *[2+(4a_*/pi)H_n].

The additional C06 derivative-series tail is tau at each endpoint.
The h/24 correction gives h*tau/12 per block, at most h*tau per
channel. The same coefficient sum and normalization then give

    (2*pi*tau/n^2)*[2+(4a_*/pi)H_n],

matching(17). Both errors already live in the C06 output balls and
must not be added twice. Coefficient uncertainty, phase variation,
arithmetic roundoff, input-radius propagation and retained/direct
primitive tails remain separate contributions carried by interval
arithmetic. Nothing pays for all ordinary rows with a special-row bound.

## Width bounds and convergence limits

Away from tangency, the derivative of asin is1/sqrt(1-t^2). On its
root interval K this is at most1/s0, proving Delta<=width(Gamma)/s0.
Differentiating g=c/p gives

    g_alpha=-(1+cos v)-g*cot alpha,

so |g_alpha|<=2+G/p0. Differentiation of c in beta produces the four
terms written in(19), bounded by2+2/m+1+1/m=3+3/m. Division by p0
gives L_beta, and m>=3 gives L_beta<=4/p0. The rectangle mean-value
bound follows. An unnecessarily wide interval Gamma is not entitled
to this smaller width unless a valid centered enclosure is constructed;
the contract makes that distinction explicitly.

For arccos endpoints s<=t and d=t-s, their mean angle lies in
[d/2,pi-d/2]. Hence sin((s+t)/2)>=sin(d/2), and

    cos s-cos t>=2sin^2(d/2)>=2d^2/pi^2.

This proves the stated global square-root bound for inverse sine,
including the endpoints. Thus widths O(1/n) under uniform transverse
constants, or threshold width O(1/n^2) near arbitrary tangency, are
sufficient for bounded direct counts. These are sufficient conditions
with explicit constants/guards, not universal necessary scales or a
claim that all shrinking phase boxes qualify uniformly in n.

At fixed interior alpha, exact bands contract to point roots, including
tangencies. The finite number of point roots leaves a bounded direct
set. Nonroot cores then have strict signs/pole distances that enough
precision can certify. Ideal exact evaluation contracts to the point
value; fixed C06 orders instead retain their analytic tail, and fixed
arithmetic retains a radius floor. The document explicitly requires
reducing both for arbitrarily tight contraction. Its fixed-phase
statement does not imply a useful accepted-leaf size or degree-uniform
work estimate.

## Actual Padua enumeration lower bound

On beta=0 and alpha in[3pi/4,3pi/4+w],0<w<=pi/16, choose all rows
with pi/3<=v<=2pi/3. There are at least m/3-1 such integers and none
of the four retained labels for n>=128. The actual threshold is

    g=cot(alpha/2)*(1+cos v).

Since1/2<=1+cos v<=3/2 and1/4<cot(alpha/2)<1/2 throughout the box,
the precise1/8<g<3/4 interval follows. The lower cot bound uses
13pi/32<5pi/12 and2-sqrt3>1/4; the upper bound uses sqrt2-1<1/2.
The first root theta=asin(g) is therefore an ordinary differentiable
real root, not a numerically inflated candidate band.

Its derivative satisfies g_alpha<=-1/4 and theta_alpha<=-1/4.
For t=(n*theta-alpha-delta*pi)/(2pi),

    -t_alpha>=n/(8pi)+1/(2pi),

so its continuous image has length at least n*w/(8pi). Furthermore,
theta>g>1/8 and lambda<=1 imply t>n/(16pi)-1>0 for n>=128;
theta<asin(3/4)<pi/3 implies t<n/6<n-1. Thus clipping removes none
of the swept integer indices.

Every closed interval of length L contains at least floor L integers,
and continuity means each such integer is attained at some actual
phase. Consequently every selected row obliges the specified method
to include at least floor(n*w/(8pi)) distinct direct indices. Rows
are distinct primitive entries, giving precisely

    sum_r |B_r| >=(m/3-1)*floor(n*w/(8pi)).

For example, n>=max(128,16pi/w) makes this at least n^2*w/(64pi),
which verifies the claimed fixed-w Omega(n^2*w) interpretation without
discarding the floor at small n*w. This is a count of mandatory
individual entries under the stated enumeration rule. A method that
rejects the box, subdivides it, or bounds a whole uncertain band
collectively has changed that rule and is not covered by the lower bound.

The separate tangent example uses odd n>=13, r=m/2, v=pi/2, beta=0,
and alpha starting at pi/2. Here g=cot(alpha/2) starts at1 and decreases
by at least w/2. Writing its endpoint as cos d and using
1-cos d<=d^2/2 yields d>=sqrt(w). The corresponding index decreases
by n*d/(2pi)+w/(2pi), hence by at least n*sqrt(w)/(2pi). This proves
actual square-root root motion. One such row contributes only
O(n*sqrt(w)) possible entries, so it does not alone establish a
quadratic total obstruction; the document correctly uses the many-row
family for that conclusion.

## Cost and remaining scope

Under the fixed-work accepted primitive/backend contracts, the four
retained rows cost4n evaluations. Each ordinary row has bounded-size
root/cut/sign work and at most12 calls per channel, plus exactly the
charged |B_r| direct evaluations. Interval integer ranges can be merged
in bounded work before enumeration. This gives O(n+sum_r|B_r|), with
O(n) only under the stated aggregate budget. Bit complexity and attempts
at refinement/increased precision are separate; no constant-cost oracle
for arbitrary rational bit lengths is implied.

Axis fallback by enumerating rows costs n each and can accumulate to
O(n^2), as disclosed. The crude alternative is valid: D_n's nonnegative
cosine coefficient sum is2N+1; removing one unit from its exceptional
cos(nu) coefficient leaves G_n's nonnegative sum2N. Hence |F|<=N,
each absolute row<=nN and S<=2N. These caps must be built without native
overflow. They provide enclosure existence, not useful accuracy.

Neither the contract nor the obstruction supplies corner-orbit
cancellation, phase gradients, center-dependent projected defects,
complete executable interval root handling, practical speed or a
production cover. Those interfaces remain OPEN. The accepted C07
executable remains point-only; this analytic interface does not expand
its API by implication.
