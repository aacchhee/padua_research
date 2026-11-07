# F06/F07 — Supplemental mathematical-validity review

2026-11-07. Independent reviewer `/root/f01_math_review`; requested/API
assignment `gpt-6-astra`, high; actual serving model/effort metadata unexposed.
Rules/input SHA: `4a5de2012bad94601c713b2ff5517f2e3fb80af2`.
Observed starting HEAD: `122129580cf156cfdee48a87e359086ab7af00ce`.
The read-only rules comparison to that assigned SHA was unchanged.
Root owns Git, mathematical adoption and all source/execution releases.

## Scope and final disposition

**Mathematical ACCEPT for both exact frozen scopes**, with no unresolved
mathematical finding. F06 proves EACH stated distance-two projected floor
`Q>1/5-3r/20` for n>=128 and physical signedrho<=r<=pi/4. F07 proves
`Lambda_c-S>283/2850>9/100` for every integer n>=256 and the entire CLOSED
signed phase region `5/4<=rho<=pi`. Root's final freeze was received and
all six hashes rechecked before this verdict.

This is only a mathematical-validity/dependency/edge audit. Root explicitly
assigned no independent novelty, priority, complete-registry gate or protocol
verdict; WORKFLOW's scoped no-novelty audit exception applies. F06's canonical
local-inventory chronology remains disclosed and unwaived. Mathematical
acceptance cannot resolve that chronology, PR readiness or final Claude
judgment. No implementation, whole-cell integration or executable certificate
is within this review.

## Input identities and actual read coverage

The following hashes and byte counts were checked with read-only metadata
tools. Root supplied and confirmed all six exact frozen identities. The
F07 final identities match the full text independently reconstructed before
the freeze; the final freeze check introduced no unread changes.

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F06-phase-floor.md | 13264 | `758a4668011117f2b97d086699f20e4d8fff1d379d206e7c3158f44a65160fc0` |
| ideas/F06-phase-floor.md | 8167 | `c7d2853ee74e145714869e76091851a533fa70af8530b291bb7e78e63718f69e` |
| attempts/F06-phase-floor.md | 4607 | `e166a2d9b9a474b89a1f0d100fd33fc4b34ece53d266c44c72ecd6b1985247dd` |
| theory/F07-far-prune.md | 14307 | `f62a559c651af761979b0063e261b297899150865c6c1528e2aada07c44f48e7` |
| ideas/F07-far-prune.md | 5920 | `ae56a91621434235b971ea1d0938b6afdf9b7584f7c875a3b86fa3e994cc90e2` |
| attempts/F07-far-prune.md | 7037 | `ea109fbb1cffe64c9f2a8bab9582d8bd95024f6d3d764d918bfd63ee15b07ac2` |

All six frozen files were read in full. Fresh full predecessor reads cover
C02-defect-dense-band (a truncated middle was recovered by bounded reads),
all three D29 floor/radius theory files, PD-T366 defect-radius-extension,
N5-two-phase-defect, F01-seam-reanchor including its adoption, and
E08-origin-lower including its adoption. PD-T364 phase-structure and
C01-allclass's full exact-object/projection material were read earlier in
this same supplemental review session; C01's initially truncated conclusion
was recovered then. The earlier F01 review independently reconstructed its
complete physical envelope and the named global-model dependencies.
These accepted predecessor scopes are used as premises; their historical
computational dependencies are not independently rerun or recertified.

No full IDEAS/INDEX read or novelty gate is claimed for this scoped review.
The F06 idea/attempt chronology was read as a record, not adjudicated.

## F06 reconstruction: exact geometry and signs

The corrected divided-Chebyshev polynomial and subtraction of `cos(nu)`
give the signed half numerator
`a(1+cos v) - sin(alpha) sin(u)/2 + sin(beta) sin(v)/2`.
The exceptional subtraction after the common sign is `cos(alpha)`, not
one. Full periodic coefficient `1/(4nm)`, halving both kernels, and folding
the reflected physical coordinate produce coefficient `1/(nm)` with the
original physical endpoint half weights. The two periodic branches remain
distinct summands of that expression. No projection is added to another.

For either orientation, set the physical mesh M, periodic mesh L and phases
mu,eta exactly as in the theorem. At the upper endpoint the selected
physical row is M-l and the actual pair angles are `2pi-t-b` and `b-t`;
at the lower endpoint they are `t+b` and `t-b`. Thus their cosine targets
are always `cos(b+t),cos(b-t)`, but their sine signs depend on epsilon.
For `0<l<M`, positivity of `sin b sin t` orders these targets strictly.
The folded angle interval is exactly
`(|b-t|, min(b+t,2pi-b-t))`. Its upper endpoint exceeds its lower endpoint
even when b+t exceeds pi or b-t is negative.

The interior periodic representatives `R,2L-R` have actual angles
`w_+,2pi-w_-`; their folded angles are in `(0,pi)` since
`1<=R<=L-1` and `|eta|<=pi/4`. Strict monotonicity of cosine therefore
gives precisely the strict R bounds in (6), including the displayed
floor/ceiling conventions. The seam indices 0,L are disjoint from those
interior representatives and appear once each. Their folded angles
`|eta|/L,pi-|eta|/L` and original parity give the stated tests, while their
actual sines are retained. At l=0,M the paired kernels coincide. Equality
with a strict boundary is a polynomial collision; multiplying the rational
identity forces a zero numerator there but does not determine the finite
quotient. Omitting these nonnegative defects is legitimate.

At the lower distance-two center the other center is odd; at the upper
center it has parity `1-M`. The physical-row change to M-l converts both
cases to `R+l` odd, for both projections and either degree parity. For
each selected l the four indices from `R=l-1,l+1` and their reflections
are distinct, interior and have that parity. The bound

    |M(w_sigma-b)|+|xi| <= (129/128)(3pi/2+r)
                          <=903pi/512<2pi

follows directly from `|M-L|=1`, `l<=M/2`, and the joint phase-radius
constraint. It implies `|w_sigma-b|<t` even when xi is negative.
The selected band also has `b-t>0,b+t<pi`, uniformly from n=128.
Consequently all four terms are regular strict straddlers without relying
on a zero-phase enumeration remaining complete.

Vertically the actual periodic sine is `sigma sin w`, and the two physical
sines are `epsilon sin(b+t),-epsilon sin(b-t)`. Horizontally those physical
sines enter the first-coordinate perturbation and the second-coordinate
baseline remains `1+cos w`. This reproduces every sign in (9),(10).
In particular neither kernel transposition nor branch equality is used.

## F06 reconstruction: finite lower bound

Taylor's cosine lower bound and the sine Lipschitz bound give, separately
for each actual numerator,

    A/sin b >= a cot(b/2)-Pabs/2-(a+Pabs)t-a t^2 >= F(b).

Here `sin b>=1/2` accounts for both the quadratic baseline remainder and
the perturbed sine cost. The bounds `a>27/32`, `Pabs<4/5`, `T<1/18`
make F positive as claimed. For an interior cosine between the targets,
each denominator magnitude is at most their entire span `2sin b sin t`.
Since the numerator signs are positive and denominator signs opposite,
`d=2min(|H_+|,|H_-|)>=F(b)/t`. Four independently bounded terms and
their unchanged interior weights yield (15).

The positive descending grid inequality loses at most F(pi/6), whether
or not either band endpoint is a grid point. The exact cotangent integral
is `2log(1+sqrt(3))`; the written exponential-series bound proves that
it exceeds two. Also `a(2+sqrt(3))<15/4`. Substitution gives all three
losses of (17), namely `4(a+Pabs)/(3L)`, `4aD/(3LM)` and `15/(LD)`.
The leading factor remains M/L until its separate loss is charged.

The positive part of H uses `D<=9pi/4,pi^2<10`; its negative part uses
`D>=2pi,pi>3`. Hence
`H>16a/45-Pabs/9`, while `H<1/2`. Using `M/L>=1-1/n` then gives
the full loss below

    [1/2+12/5+1/12+5/2]/n =329/(60n)<11/(2n).

The inverse-square term was reduced only with n>=128. The actual phase
constraint supplies `a>=1-r^2/4,Pabs<=r`. Subtracting the desired floor
leaves `7/45+7r/180-4r^2/45>37/375`; this exceeds `11/256`, the largest
remaining loss. All inequality directions and displayed rational products
check on paper. Therefore EACH distance-two projection is strictly greater
than `1/5-3r/20`, for every n>=128 and the full signed radius guard.
No other endpoint distance, full fifth floor or global onset follows.

## F07 frozen-proof reconstruction

The frozen theory, idea and attempt have been read in full. Their literal
functions agree with the accepted F01 reanchor: all four Cb components,
both Cs brackets, the slope-three Cl, separate KD, and the WHOLE origin
allowance `D+Mesh+Bout+Rplus`. The pointwise replacement by j*=23/250 and
t*=221/500 is consistent throughout G*,K*,A*. The global model retains
the named accepted PD-T271 dependency; no limiting enclosure is silently
used as a finite-origin lower bound.

The new paper arithmetic has been reconstructed, including both atanh
series, the literal sine cutoff, entropy argument, every mesh tail and
the separate origin-positive-part comparison. At the sole base 256 the
written bounds give

    T>21/2, Cb<11/10, Cs<867/1000<9/10,
    Cl<1/3, KD<21/100, e0<143/750<1/5.

The four Cb bounds are respectively `7/50,47/100,47/100,1/50`; neither
the non-a ordinary term nor any of the six retained rows is omitted.
The ordinary KD includes its `2/pi` term. The mesh-tail estimates are
base-specific, with all three denominators bounded in the right direction.
The exact comparison `71*45*257<22*256^2` sets only Rplus to zero;
it supplies no sign for the full finite-origin error.

The original scalar functions, rather than frozen logarithm upper bounds,
are then used for the all-n transfer. The K bound precedes every division:

    K*>19/2+193/1500>0,
    G*>211/1250>1/6, A*<1563/1000<8/5,
    F*(256)>1/6-(8/5)^2/(4*(19/2))=283/2850>9/100.

The inherited monotonicity of G*,K* and the decrease of positive A* make
F* nondecreasing while K*>0. This transfers a complete sufficient gate,
not a monotonicity claim about actual finite S or Lambda_c. F01's closed
phase domain covers both seams, axes and polynomial collisions. The complete
regional primitive claim is therefore accepted. No full argmax256, new
certified finite degree, smaller global onset, runtime saving or source
integration follows from this regional mathematical theorem.

## Activity and remaining boundaries

Only text reads/searches, hash/byte metadata, collaboration and this owned
review-file patch were performed. No scientific script/import, calculator,
exact-arithmetic helper, scalar, phase, degree, endpoint, native, compiler,
quadrature or measurement job ran. Ordinary tool overhead is unmeasured.
No author proof, shared record, source, evidence, Git state or old review
was edited. Final Claude review and root adoption remain separate.
