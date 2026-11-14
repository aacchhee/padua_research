# Campaign H supplementary mathematical support review

Date: 2026-11-07. Reviewer: independent Codex audit worker
`/root/h_support_review`. Parent-confirmed requested/API-accepted model
and effort: `gpt-6-astra`, xhigh; actual serving model/effort are not independently
exposed to this worker. Rules and initial input read at full branch head
`ee1480fb7eba11f45c202dd46c36b134051f432d` on
`codex/padua-argmax-bridge-20261105`. Concurrent development files are
identified by their complete SHA-256 values below, rather than assumed
to be committed at that initial head.

## Scope and decision

**ACCEPTED within supplementary mathematical scope:** H04's smooth
residual expansion and strict coefficient sign; H05's uniform centering,
one-sided weighted bound and correction estimates; H03's exact finite
identities and the mathematical diagnostic for its signed substitution.
No unresolved BLOCKING, MAJOR or MINOR mathematical finding was found
in these three records. Preliminary reconstructions were sent directly
to the root and H04/H05 owners before this report.

This review independently reconstructs the proofs, constants, endpoints,
parity coverage and exact normalization. It does not assess novelty,
historical priority, the developers' gate chronology or global target
completion. The WORKFLOW exception for an audit with no novelty content
applies: the complete IDEAS inventory was not reread. The completed
Campaign-H gate was read for scope and predecessor context; its verdict
is not inherited as mathematical proof or independently endorsed here.
Reading the idea/attempt records below identifies their mathematical
claims only. No candidate, new mechanism or negative-result allocation
is proposed.

The original corner target is not accepted by this support report.
H01/H06 assembly, remaining harmonic sums, constant identification,
the total first-order coefficient, and transfer to N=n+1/2 require their
own review. This supplementary Codex check does not replace the required
final Claude audit or registry/readiness review.

## H04 reconstruction

The object V_n is exactly F03 (8). From the original partial-row samples
with m=n+1, t=r/m and a=(1-t)/2, the midpoint cells have union
`[-t/(2n), t+t/(2n)]`. In particular the upper endpoint at r=n is
`(n+1/2)/(n+1)<1`; the lower extension is inside [-1/4,0] for n>=2.
No endpoint row or parity class is omitted.

After removal of the poles 0 and 1, the remaining poles are -h and h+1.
On [-1/4,5/4] their distances are at least 3h/4. Differentiating the
paired cotangent series therefore gives the claimed bounds |B'|<3 and
|B''|<5; |B|<5 follows from B(0)=1/pi. The paired series itself is
uniformly convergent there; its derivative series are absolutely
uniformly convergent. The W=t*cot(pi*t/2) series independently gives
`0<=W<1`, `|W'|<3` and `|W''|<5` with the displayed elementary series
majorants. The bounds cover the entire intervals on which they are used.

The inner midpoint error is at most `5r/(24n^2)<=5t/(16n)`.
Each extension costs `3t^2/(8n)`, so the stated row error
`|e_(n,r)|<=17t/(16n)` follows. The factor t cancels the outer cotangent
singularity before summation, yielding `|E_n|<=17/(4nm)`.

The integral definition J(t)=int_0^1 B(st)ds gives a regular outer
function F=WJ with `|F''|<36`; G=W(B+1/pi) has `|G''|<50`.
The endpoints are exactly
`F(0)=2/pi^2, F(1)=0, G(0)=4/pi^2, G(1)=0`.
Composite trapezoid errors hence give the remainder

    12/m^2 + 25/(3nm^2) + 17/(4nm).

The first endpoint charges combine by the exact identity
`-4/(pi^2*m)-4/(pi^2*n*m)=-4/(pi^2*n)`.
With y=n/m, multiplying the remainder by n^2 gives
`(11/3)y^2+(151/12)y<65/4<17`. This verifies the explicit 17/n^2
constant without replacing a denominator at an uncontrolled scale.

The sign proof also checks. Every derivative summand in B' is negative,
so B+1/pi is positive in the interior. The isolated-pole estimate yields
`B(t)+1/pi<(2-t^2)/(pi*(1+t))`; the canceled W identity yields
`W(t)<=(2/pi)*(1-t^2)/(1-t^2/4)`. Their product is strictly between
0 and `(4/pi^2)(1-t)` for 0<t<1. Integration verifies
`-4/pi^2<beta_B<0`. The nonzero coefficient is part of the written
support theorem and cannot be discarded by an assertion of centering.

## H05 reconstruction

The locally defined harmonic series is uniformly convergent on each
compact positive interval, as are the derivative series needed here.
Its differentiation and finite-shift recurrence are justified by uniform
integration. Independently reconstructed bounds are
`psi''(u)=-2 sum_(k>=0)(u+k)^-3` and
`|psi''(u)|<=u^-2+2u^-3`; psi'' is strictly increasing.

The shifted arguments are exactly
`m-cs=r+1/2-r/(2m)`, `cs=s-s/(2m)` and `m-q=m-s/(2m)`.
Taylor expansion keeps -psi(q) unchanged and gives the PLUS linear
contribution from -psi(m-q). Thus the exact correction is -J_s/(2m).
Writing the three integral remainders as R1, Rs, Rm, their signed
combination is `-rho_s=R1+Rs-Rm`. The equal shifts q in the last two
terms imply Rs<Rm<0, so rho_s>0 and `rho_s<=-R1-Rs`.

The actual lower arguments satisfy `r+q>=r` and `s-q>=3s/4`.
Consequently the first two costs are `3/(8m^2)` and `22/(27m^2)`;
their sum is `257/(216m^2)<5/(4m^2)`. The optional third cost
`14/(27m^2)` reproduces the earlier cruder triangle constant
`41/(24m^2)<2/m^2`. These inequalities hold for m=2 and for s=1 or
r=1, as well as throughout the index range.

The weights are positive and satisfy
`sum_s tan(pi*s/(2m))<(2m/pi)H_(m-1)`.
Multiplication by the actual prefactor 4/(pi*m) gives the final,
stronger written weighted bound

    0<Ccal_m-Hcal_m
      <=257 H_(m-1)/(27 pi^2 m^2)
      <10 H_(m-1)/(pi^2 m^2).

Thus the preliminary 16H/(pi^2*m^2) bound requested for review is
also valid, but is not the final theorem's sharpest displayed constant.
There is no hidden n-for-m or N-for-m replacement.

The finite-tail form of J_s follows directly by telescoping psi'.
Strict convexity of x^-2 on the unit cells proves
`r*psi'(r+1/2)<1`; the reciprocal-square tail is at most 2r/m.
This gives `0<J_s<1+2r/m<3`. The optional midpoint-defect kernel is
correct: on a unit cell its maximum is 1/8, and summing f''=6x^-4
gives `0<1-r*psi'(r+1/2)<=1/(4r^2)`.

The identification with the original corner contribution was also
checked directly from F03, rather than assumed from H01. With s=m-r,
F03 has `a_r=q` and `n-r+1-a_r=s-q=cs`. Its finite harmonic
difference is exactly D_s, its weight becomes tan(pi*s/(2m)), and
`4/(nm)` times the harmonic factor n/pi is exactly 4/(pi*m).
This verifies the normalization and both endpoints in the identification;
it supplies no asymptotic estimate for the remaining weighted main sum.

## H03 reconstruction

The weighted ordering count has lower-triangle weight j/2 in row j,
total parity weight m/2, and a missing 1/2 only in the final row before
the outer epsilon weight. Hence
`C=sum epsilon*eta*sign(y-x)=-(2n-1)/4`.
Substitution in the original PD-T159 formula leaves
`2C/(nm)+1/m=1/(2nm)`, proving the stated symmetric identity with
the original exceptional atom and half weights.

For the periodic odd board, the map d=mj-nk modulo 2nm is injective:
equality first gives j modulo n and k modulo m; the only two possible
representatives differ by simultaneous shifts (n,m), which switch parity.
The board and residue set each have 2nm points. The unique odd collision
maps to zero. With Q=nm and a=2n+1, the identity
`ad-e=2Q(j-k)` fixes the minus sign in cos(P)cos(T), including any
change from the actual d to its canonical residue. It also gives
`x-y=2 sin(a*q_d)sin(q_d)`. Since a^2=4Q+1, gcd(a,2Q)=1 and no
remaining displayed sine denominator vanishes. The periodization factor
is four for the endpoint-weighted board, proving formula (2).

For the signed substitution, PD-T226 at zero phase gives full signed
interior rows n, endpoint row -n^2 at k=0, and the sole polynomial
collision n at k=m. Removing that collision makes the last rational row
zero. Folding and the k=0 half weight give `R_y=n^2/4`.
The regular odd-board weight is Q/2-1/4 and
`R_y-R_x=-(Q/2-1/4)`. Multiplying R_y+R_x by four therefore gives
`sum Ktilde=4n^2+2n-1`, exactly as stated. At d=m the signed sine
is negative while the numerator is positive, so strict mass deletion
is established. The leading order of the deleted mass follows from
the explicitly named PD-T269/270 asymptotics.

This verifies only these exact identities and their stated diagnostic.
It does not establish that every reciprocity method fails, a faster
evaluator, or a sharp estimate for the retained absolute correlation.

## Complete-read input identities

All files in the following table were read in full; broad outputs that
truncated were followed by bounded rereads. Paths are repository-relative.
Hashes were obtained after completion of the three developer trios; both
H04 and H05 owners confirmed that no material proof edit remained planned.

| File | SHA-256 |
|---|---|
| AGENTS.md | c44a76f138fce01f02c06753b22fbc83fd5c1ee701785d49ba17cef5f8eee05b |
| agents/WORKFLOW.md | 65e6b7268f4df4c97a3271ead27199381747b940ebba5cce2796a0bf7b8b9209 |
| agents/codex/CODEX.md | 871b4f8e18d207c9ba25933ff413e7bedf32d1d036b2f7d5b4ecec397f257610 |
| topics/padua-argmax-bridge-20261105/campaign-H-gate.md | 5c2ee7050d221360c84e63568c1f3328a1de1541ab398439e09b62cc9b3205fc |
| topics/padua-argmax-bridge-20261105/theory/F03-origin-sign.md | ddccb0512f0f4abfb50531a762216a7fb71a038de6cd1b64e4f73e44de42d1ea |
| topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md | 3da8a12e841d3555af2a586909ed7a258c760f17c9ea4af2079c9f044568e263 |
| topics/padua-lebesgue-followups-20261103/theory/t4-01-corner-defect-limit.md | a40f61a44d787201ecfe82f08eccb9e57de02a9d3a18161741be7f2f8cde4b46 |
| topics/padua-lebesgue-followups-20261103/theory/t4-02-one-dimensional-remainder.md | ead57816c2b33e250462514e25bcd4e709902523b33bd4cf1a17c007a6ec2e28 |
| topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md | 957802f2b3060a704f5a8b72042951f2a623716e2f817eccbed2ee8a23595e8f |
| topics/padua-argmax-alln-20261101/theory/gated-codex-12-row-primitive-identity.md | 2692c28af71b4f5eeb129f3a2f32a24a5a3e7e8929279063e0c63f3edbaf3d92 |
| topics/padua-argmax-bridge-20261105/ideas/H03-reciprocity.md | 07844439a68bbc5bbf4df60676b555e90c6ec181af1987223f3be474da0b8b7a |
| topics/padua-argmax-bridge-20261105/attempts/H03-reciprocity.md | 758eaaf7bb768add95376fc1b8589466125856607e7cd36c2f1ba1059b543f79 |
| topics/padua-argmax-bridge-20261105/theory/H03-reciprocity.md | c1bae3c044e68d98041e4f9ead1b969f9e722fe4364ece38868a7e5224d9045d |
| topics/padua-argmax-bridge-20261105/ideas/H04-smooth-quadrature.md | 17737ba5468a63a5227a2afecf2743cf90968793f8d5881718cad397dd8464f9 |
| topics/padua-argmax-bridge-20261105/attempts/H04-smooth-quadrature.md | 65782c8f3c81d7e450a409c01dec2e103fa027975d8ba1acd49270769fce498e |
| topics/padua-argmax-bridge-20261105/theory/H04-smooth-quadrature.md | 25ffa263c0e66cd1bce983f7d9f7c29bb2e333884260ba00d49eb10f2e86a8bd |
| topics/padua-argmax-bridge-20261105/ideas/H05-digamma-centering.md | 6bc8e27c590b1e74d89eae99bfc2e8b59773b024d35682202d1d7261d248d777 |
| topics/padua-argmax-bridge-20261105/attempts/H05-digamma-centering.md | eeaefeb40a95d6022a2e1e201fe2f82890a5205366330826cc8bef633a063a25 |
| topics/padua-argmax-bridge-20261105/theory/H05-digamma-centering.md | 755e574e1653a3bbdac214a169e42668f7cf4f7e35d3020930b39091e600727c |

## Actions and remaining verification

Actions actually performed: repository discovery with `rg --files` and
`rg -n/-l`; full or bounded text reads with `cat` and `sed`; read-only
inspection of the branch-ref file for the full input SHA; `sha256sum`
for the listed inputs; and this sole owned report write using apply_patch.
The required cloud-runtime skill and environment-status tool were also
read/called for workspace setup. No Git command or mutation, source edit,
shared LOG/registry write, PDF, numerical experiment, scientific job,
native executable, import or independent computational rerun occurred.
The verification consists of independent written proof reconstruction.

No scientific rerun is needed for the accepted analytic statements.
Any material change to their mathematics requires a focused recheck.
The parent requested a separate H02 endpoint-support review after this
initial acceptance; its disposition will be recorded in a distinct
addendum and does not delay the H03/H04/H05 decision above.

## Separate H02 addendum — 2026-11-07

At the parent's subsequent request, the final H02 idea, attempt and
theory were read in full. **ACCEPTED within its written support scope:**
the upper adjacent-offset slice expansion (1), its artificial-cut parity
term, the fixed-index lower endpoint limit (2), and its explicitly
fixed-offset tails (14). No unresolved mathematical finding was found.
H02 remains separate from the main proof and is not an accepted proof
of the full all-offset target. The mathematical scope and novelty
exception above apply unchanged.

Independent reconstruction of the small-gap expression confirms the
exact A and B formulas. In the sinc expression for qA, every argument
on the full rectangle 0<=t,q<=1/2 lies in [0,pi/2]. The denominator
is consequently bounded away from zero and its required derivatives
are bounded. Logarithmic differentiation at q=0 yields exactly
`g*(1-2w*cot(w)+w*cot(2w))`; the apparent t=0 factors are removable.

For the reference term, the product q*cot(cq) is smooth. In the other
product, u=t-q and v=2t-q satisfy v>=t, so the derivative of u/v
is bounded by 1/t. The smooth bracket factors remain bounded through
v=1. This proves the retained O(q^2/t) remainder uniformly for
q<=t<=1/2, including r=1. The q coefficient of q(A-B) reduces to g
because `tan(w)*cot(2w)=(1-tan^2(w))/2`.

The actual prefactor is 4q/(1+q) on the q-scaled terms. Its expansion
therefore gives g-e=t*g, and the summed remainder is
`q*sum O(q^2/(rq))=O(q^2 H_R)`. The additional normalization error
is included at this same scale. The actual k=n row has eta_n=1.
Trapezoid endpoint terms at T=R/n and displacement
`T=1/2-chi/(2n)` give precisely
`2*(1-chi)*e(1/2)-2*e(0)+4*int_0^(1/2)t*g(t)dt`.
The values e(0)=1/2, e(1/2)=1/pi and the integral log(2)/pi^2
reproduce the stated coefficient for both parities. Compact derivative
bounds supply an absolute big-O constant; no numerical value for it
is claimed by H02. Since n>=2, the harmless fixed constants can be
absorbed in C*log(n)/n^2 also at the smallest n.

For fixed j,k, both trigonometric values differ from their quadratic
fractions by O_(j,k)(1), and the nonzero d=k^2-j^2 fixes the sign for
sufficiently large n. Differentiation of
`(1+q)^2/abs(k^2-j^2*(1+q)^2)` at zero gives
`2*sign(d)*k^2/d^2`. This verifies (2), including the exact zero
case k=0. The displayed plus/minus tails follow by ordinary rational
expansion with l fixed. The attempt's exact J_l+K_l extraction was
also checked algebraically; its tentative residual estimates are not
accepted as proved claims.

No uniformity in growing l, no summation of those fixed-l tails, and no
cancellation of H02's artificial parity term elsewhere is established
by this addendum. Such conclusions still require the separately written
all-offset or full-corner proof. No new scientific computation occurred.

| Additional complete-read file | SHA-256 |
|---|---|
| topics/padua-argmax-bridge-20261105/ideas/H02-endpoint.md | b0e764930a3a90c7e3cbb98ec5dfcb5f1bf662799fc48ecd17f4df1b8fe69af1 |
| topics/padua-argmax-bridge-20261105/attempts/H02-endpoint.md | 58854e5f5d23a575b970b6986b7bac38420fe4fae95739fa3fe5bad4944ee447 |
| topics/padua-argmax-bridge-20261105/theory/H02-endpoint.md | fb43b70c826980fd4133afa6cddb6469df021fd3f314a010eb16931fb6f50086 |
