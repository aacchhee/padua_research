# C08 — a guarded phase-box row enclosure with explicit ambiguity work

Rules 4b728b0; 2026-11-06. Local technical interval variant of N2/C02/C06.
Gate/preregistration: [ideas/C08-row-box.md](../ideas/C08-row-box.md).
**PROVED analytic interface, distinct review pending.** No executable,
performance result, full cover or new degree is claimed. C07 remains a
point-only implementation; this document does not change its API.

## 1. Domain, retained rows and statement

Let n>=2, m=n+1, N=nm, h=pi/n. Let B be a closed rectangle in
[0,pi]^2 and let P=B intersect {alpha+beta<=pi} be nonempty. P is the
actual phase set; enclosure arithmetic may use the larger rectangle B.
Its widths are w_alpha,w_beta. The same construction can first reflect
phase signs by the existing separate evenness, splitting at axes if
needed; no mesh-exchange symmetry is used.

Keep the physical row labels fixed. For r=0,...,2m-1 put

    delta=(1-r) mod 2 in {0,1},
    lambda=(delta+alpha/pi)/2,
    u_k=2pi*(k+lambda)/n,        0<=k<n,
    v=(r*pi+beta)/m,
    F_rk=(-1)^delta G_n(u_k,v)/2.

Do not replace lambda by a fractional part that changes labels at the
closed phase vertex. Put k=0 and k=n-1 into an optional seam/direct
set in each ordinary row; doing so costs at most two points per row and
removes any u=0 or 2pi edge convention from the core formulas.

Retain the four rows {0,2m-1,m-1,m} as n direct finite-primitive interval
evaluations each. They contain every possible v in pi*Z on the closed
domain. Carry the complete primitive balls, including C01/C03 tails and
roundoff. For other rows v avoids pi*Z throughout B.

For each ordinary row construct the closed index bands in section 2,
their direct integer set B_r, and the fixed signed cores in section 3.
If every required sign, coefficient and C06 call passes its stated guards,
section 4 returns an enclosure of every S_n(alpha,beta), (alpha,beta) in P.
For fixed backend orders and precision its scalar-operation count is

    O(n+sum_r |B_r|).                                    (1)

There are at most 12 fixed cotangent blocks in either channel per row.
This becomes O(n) only under an explicit aggregate ambiguity budget
sum_r|B_r|<=C*n, or the stronger per-row budget |B_r|<=C. No such
budget is assumed for arbitrary phase boxes. A failed numerical guard
does not return an enclosure; valid alternatives are described below.

## 2. Complete closed root bands in integer coordinates

Write A=cos alpha+cos beta, p=sin alpha, q=sin beta and

    c=A(1+cos v)+q sin v.

At regular points N2 gives

    F=(c-p sin u)/[2(cos u-cos v)].                       (2)

The denominator collision locations in the real k coordinate are exactly

    d_1=(n*v-alpha-delta*pi)/(2pi),
    d_2=(n*(2pi-v)-alpha-delta*pi)/(2pi).                  (3)

Enclose these affine functions over B by two closed intervals. Their
exact widths are both

    d_D=(w_alpha+(n/m)*w_beta)/(2pi)<1.                   (4)

Thus each exact collision band contains at most one integer, even for
the full quadrant widths w_alpha,w_beta<=pi. Numerical inflation must
be charged by the actual band width, not discarded using (4).

For numerator roots first permit a root-free test: if c-p sin u is
strictly positive or strictly negative for every real u and every phase
in P, it has no roots. For example, on the nonnegative phase domain,
lower(c)>upper(p) or upper(c)<-upper(p) suffices. These tests also cover
some boxes touching p=0 without division by p.

Otherwise require a certified p>=p0>0 on B and form a finite outward
enclosure Gamma for g=c/p over B. If Gamma misses [-1,1], there are no
numerator roots. Otherwise let K=Gamma intersect [-1,1], and define the
closed angular interval J=asin(K) in [-pi/2,pi/2]. Every possible
numerator root in 0<=u<=2pi belongs to one of

    J,            pi-J,             J+2pi.              (5)

The first/third alternatives handle the angular seam without choosing an
uncertain principal branch. For each of these three intervals enclose

    t=(n*u-alpha-delta*pi)/(2pi)                         (6)

over the phase box, and discard only bands proved to miss [0,n-1].
The two branches with opposite angle derivative have the same width
bound. If Delta=width(J), each band has width at most

    d_I=n*Delta/(2pi)+w_alpha/(2pi),                     (7)

before additional arithmetic inflation. Tangent roots at g=+/-1 remain
inside these closed bands. A phase at which no root exists causes no
problem: the bands may overinclude candidates, never omit an existing
root. Coincident or overlapping bands are merged for counting.

All band endpoints are outward real bounds; exact dyadic endpoint
extraction and exact integer ceil/floor may be used. For a closed band
[l,u], its direct indices are

    max(0,ceil l),...,min(n-1,floor u).                   (8)

Include equality at both endpoints. This is essential for a grid point
that is a zero/collision only on the closed boundary of P. If the range
is empty, the band still creates an integer cut at ceil l, clipped to
[0,n]. Dropping this cut would incorrectly merge opposite signs on the
two sides of a root lying strictly between adjacent grid points.

Define B_r as the union of (8) over all bands and the seam indices.
There are at most five root bands (two denominator, three numerator)
and two seam singleton bands. Consequently

    |B_r|<=min(n, 2+sum_j [floor(width_j)+1]).            (9)

With exact collision widths (4), the bound simplifies to

    |B_r|<=min(n, 7+3*floor(d_I)).                       (10)

If no numerator root band is needed, omit its contribution. Actual
outward widths replace d_D,d_I in (9) whenever rounding enlarges them.
The direct-set budget here is deliberately different from C07's point
guard |B_r|<=5; the in-progress C07 routine cannot simply be relabeled
as a box routine with that old assertion left unchanged.

## 3. Fixed cores, signs, wraps and interval backend offsets

Sort/merge the finite root bands and construct all integer cuts at their
direct-range endpoints, retaining the empty-band cuts just specified.
The remaining integer cores are consecutive sets a,...,b that contain
no direct sample and have no real root band between their endpoints.
There are at most eight such cores: at most seven band components
(including seam singletons) produce at most eight complements, with an
empty band acting as a cut rather than a removed component. The loose
12-block allowance therefore remains safe.

For a core, consider the connected domain [a,b] times P, with u defined
by the same real index parameter. Both numerator and denominator in (2)
are continuous and have no zero anywhere on this domain, by complete
root-band exclusion. Each therefore has a constant strict sign there.
Certify those two signs at one point of that domain, using exact or
validated arithmetic. This is enough to label the ENTIRE core for the
ENTIRE phase box. An unresolved numerical sign is failure/refinement,
not permission to choose the midpoint sign. A whole core that is proved
identically zero can instead be omitted.

The two cotangent channel wraps occur at u=v and u=2pi-v, precisely the
denominator roots already excluded by (3). Thus for each core and each
channel one exact integer ell is constant on [a,b] times P. With the
chosen sign +/- put

    y=a+lambda +/- n*v/(2pi)-n*ell,
    qcount=b-a+1.                                       (11)

Supply an outward interval enclosing this affine y over the WHOLE box
to native C06, and literally check

    0<y,              y+qcount-1<n.                     (12)

The exact width of y is d_D, independently of n. A guessed wrap may
propose ell but (12) must certify it; choose/store ell as an exact
integer. Different channels may require different ell. Guard (12)
proves every selected cotangent argument is strictly in (0,pi) for
every phase. No root, zero coefficient or exact cancellation excuses a
failed guard. The successful native C06 ball encloses the entire sum
for all y in its interval, including all phase dependence. This is the
accepted C06 interval contract, not an inference from a point evaluation.

The complete numerator-root coverage hypothesis must be respected.
If p can be zero and neither a root-free/identically-zero branch nor
another proved complete root cover is available, this construction must
fail or use a separately charged row fallback. In particular c=p=0
at a possible phase creates zeros for all real indices at that phase;
dividing a p ball containing zero or simply declaring I empty is invalid.

## 4. Whole-box row enclosure and all-row error charge

Use interval enclosures over P (or B) for

    C=(p-q-A*cot(v/2))/4,
    D=(p+q+A*cot(v/2))/4,
    T=n*[(cos alpha+cos beta)/2-(q/2)*cot(v/2)].         (13)

The cotangent in (13) is finite on every ordinary row. For its fixed
negative cores let Qminus,Qplus be the sums of successful C06 balls
from (11). At every direct index evaluate the COMPLETE finite primitive
as an interval over B, with F's fixed parity and factor 1/2. Then

    Rbox=T-2*C*Qminus-2*D*Qplus
                      +2*sum_(k in B_r) max(-F_rk,0)    (14)

encloses the exact absolute row over all phases in P. Formula (14)
is N2/C02's pointwise identity applied to one fixed decomposition that
has just been proved valid for all phases simultaneously. The omitted
cores are certified nonnegative. Every possible collision is in B_r,
and no direct index is also included in a cotangent block. The finite
primitive handles all exact/near collisions; no `0*infinity` appears.

Sum (14) and the four retained absolute row balls, then divide by N.
Intersect with [0,infinity) if useful. This gives a validated enclosure
of S_n(P). No gradient or differentiability of a moving integer block
is needed. All arithmetic and analytic radii in each C06/direct ball
remain in the result; no midpoint/radius drop is licensed.

For clarity a separate analytic charge can be reconstructed uniformly.
Let a_*>=sup_P |(cos alpha+cos beta)/2|, a_*<=1. The rowwise distance
bound proves, even with a supremum taken separately in each row,

    sum_r sup_P(|C_r|+|D_r|)
                     <=m*[2+(4*a_*/pi)*H_n].            (15)

Each ordinary core channel has at most n samples and 12 blocks. For
C02 orders J,K,Lh, with exact W,w', the complete truncation bound is

    E <=[7*pi^4*M_J/(2880*n^4)+48*eta_(K,Lh)/pi]
                               *[2+(4*a_*/pi)*H_n].    (16)

It charges ALL approximated rows. The interval widths due to the phase
box, numerical arithmetic, direct primitive series and coefficient
balls are additional; they are not reclassified as the small tail (16).

The frozen C06 uses J48/K32/L16 and approximates w' separately with
the uniform endpoint derivative tail

    tau=16/(9*pi^2)*4^-97*(195*4/3+8/9).

Each block therefore has a further h*tau/12 charge; 12 blocks/channel
give h*tau. Its extra normalized all-row analytic charge is at most

    [2*pi*tau/n^2]*[2+(4*a_*/pi)*H_n].                 (17)

This tail is already inside C06's returned ball. Equations (16)–(17)
are a transparent audit budget, not instructions to add the same error
twice. C06's present LP64 integer limit, precision, possible wide-ball
rejection and exact-rational moment cost remain its existing contract.

## 5. Width conditions, contraction and limitations

When a certified p>=p0>0 exists, let Gamma enclose g on B. If its root
part K lies in [-1+epsilon,1-epsilon], put
s0=min_(t in K) sqrt(1-t^2)>0. Then

    Delta<=width(Gamma)/s0.                            (18)

A convenient analytic width estimate, when |g|<=G on B, is

    width(g(B))<=L_alpha*w_alpha+L_beta*w_beta,
    L_alpha=2+G/p0,       L_beta=(3+3/m)/p0<=4/p0.      (19)

Indeed g_alpha=-(1+cos v)-g cot alpha, while
c_beta=-sin beta*(1+cos v)-(A/m)*sin v
       +cos beta*sin v+(sin beta/m)*cos v.
Use |A|<=2 and the sine/cosine bounds. Outward interval Gamma may be
wider than (19); the algorithm charges its actual width unless a valid
centered enclosure using (19) is substituted.

At a tangent threshold one always has the elementary Hölder bound

    Delta<=pi*sqrt(width(K)/2)
          <=pi*sqrt(width(Gamma)/2).                  (20)

To prove it, for angles 0<=s<=t<=pi with d=t-s, their cosine difference
is 2 sin((s+t)/2) sin(d/2)>=2 sin^2(d/2)>=2d^2/pi^2.
Apply this to the corresponding arccos endpoints. No differentiability
of asin at +/-1 is assumed.

Equations (7),(10),(18) show that uniformly transverse roots and phase
widths O(1/n), with uniform p0,s0,G, suffice for a bounded direct count
per row. Near arbitrary tangencies, width(g)=O(1/n^2) suffices by (20).
The constants and actual band-count guard must be supplied; the phrase
"small box" alone is not a quantitative hypothesis. p0 shrinking with n
or near-axis degeneracy can require still smaller widths.

At a fixed phase with 0<alpha<pi, shrinking closed boxes make the exact
root bands contract to their point roots, including tangent roots by
(20). Only a bounded number of integer samples can then remain direct.
With sufficient arithmetic precision, nonroot core signs and strict pole
distances become certifiable. Natural interval expressions converge to
their point expressions. With exact scalar functions the resulting
row enclosure contracts to the exact point value; with fixed C06 orders
there remains its explicit analytic tail and numerical radius floor.
Arbitrarily tight mathematical contraction requires those tails and
arithmetic radii to be reduced as well. This is a fixed-point statement,
not a degree-uniform box-width or accepted-leaf theorem.

The closed axes and vertices are never discarded. Exact singleton
vertices have S=1 by N2/PD-T365. On an axis, a proved root-free or
identically-zero numerator branch can be used; unresolved p=0 branches
may use a direct retained row or a coarse row bound, with that cost
recorded. Row enumeration costs n and may accumulate to O(n^2).
Alternatively return failure for subdivision. Coarse total fallback is
always available: the nonnegative coefficients of G have sum2N, so
|F|<=N, every row has 0<=R_r<=n*N, and 0<=S<=2N. Construct these caps
without overflowing native integers. They are valid enclosures, not
useful accuracy or acceptance promises.

The separate [scoped obstruction](C08-row-box-obstruction.md) proves that
direct enumeration of all swept numerator-root indices can require
Omega(n^2*w) work on actual fixed-width Padua phase boxes. That refutes
a uniform O(n) work claim for this specific enumeration route. It does
not refute S_n continuity, the guarded contract above, an aggregated
uncertain-band bound or another whole-box algorithm.

No corner-orbit or center-dependent defect is supplied by (14). Applying
an S upper bound in a far/discard predicate is legitimate after full
arithmetic review; using it as a corner-orbit cancellation bound or a
projected-defect lower bound requires a separate identity and budget.
