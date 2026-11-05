# Supplementary independent mathematical reconstruction

2026-11-05. Codex, parent-assigned `gpt-6-astra high`, as expressly required
by handoff 01; runtime serving metadata is not independently exposed.
Role: supplementary checker, not developer or the required Claude auditor.
Rules read at `2fb2f7502bb8d1b46c0fe1089588c46a06df258d`:
`AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`.
Read handoff 01 and the pre-run plan. No Git mutation was performed.

## Finding and scope

No unresolved mathematical finding in the reviewed claims below. The
all-degree global target PD-T099 remains OPEN. This check does not certify
an H1 cover, validate a fitted remainder, or replace the Claude audit.
The numerical tests are MEASURED diagnostics, not outward-rounded proofs.

| Reviewed result | Independent assessment |
|---|---|
| Exact common primitive and finite sufficient cover | Endpoint multiplicities, corrected mode, parity, collision values and strictness predicates check |
| Conditional A0 arithmetic | Stated conditional roots and distinction from a proved threshold check |
| Exact boundary cotangent profile | CRT, collisions, vertices, all four edges and uniform 7/(12N²) remainder check |
| Leading-factor-only obstruction | Correct for arbitrary finite phase-independent b_n; no wider H2 impossibility follows |
| Defect radius extension | All eight lattice lines, parity and numerator budgets support radius 1/10 and lower bound 1/8192 for n>=48 |
| Aggregate corner energy | Written proof supports W_n<=10^10 n^4 Lambda_c for all n>=2; no individual gradient-ratio bound is inferred |
| Explicit global norm ratio and physical radius | Final T06/T07 checked: Lambda_n<=30000 Lambda_c and strict descent for H<=10^-11/n² |

The final global-norm and local-radius files were subsequently read in
full and added to this assessment. Final reviewed byte hashes are below.

## Reflection and the primitive

Independently start from the finite cosine polynomial with weights h_0=1,
h_a=2 for a>0 and the (n,0) coefficient reduced from 2 to 1. Applying
product-to-sum separately in both coordinates gives each cardinal as the
weighted average of four G copies, including collisions. Taking the
absolute value after averaging gives lambda; taking it before averaging
gives M. Their difference is precisely the full defect Delta. Pairing
first proves Delta>=Q_v,Q_h, not equality with either projection.

For a mesh endpoint, its two signed preimages coincide and each has
weight 1/2. At an interior residue there is one signed preimage of weight
1. Their two-coordinate product gives exactly one periodic copy per
residue, with factor 1/(2N). Signs preserve index parity. Translation by
an odd physical center takes the even board bijectively to the odd board;
this proves M=S_n with no boundary correction. The physical restrictions
on each center's phase chart must still be retained.

For the projected torus representation, writing
H_rs=G((r*pi+alpha)/n,(s*pi+beta)/m) and d(x,y)=|x|+|y|-|x+y| gives

    Q_v(K) = sum_odd d(H_rs,H_r,2K-s)/(4N),
    Q_h(J) = sum_odd d(H_rs,H_2J-r,s)/(4N),

with periodic indices. The phases retain their original signs in both
entries. The factor 1/4N accounts for both members of each reflected pair.
This was also independently compared with physical weighted projections.

The diagonal polynomial value is P'_n(cos u)-cos(nu), where
P_n=T_(n+1)+T_n. Thus G(0,0)=2N, G(pi,pi)=2n(-1)^n and G(0,pi)=0.
At zero phase F_(n,m)=n; the other odd-board entries in the row r=m vanish.
This distinguishes a removable collision from the neighboring zero row.
At every physical corner all four copies coincide. Odd corners give
S_n(0,0)=Lambda_c; node corners give 1 and lie at boundary phases of the
odd-center charts. At an edge only the corresponding pairs coincide.

The nearest-odd-vertex cover follows because the two L1 distances in each
mesh rectangle sum to 2. This includes ties and physical boundaries.
The finite-cover theorem is then a pointwise sufficient comparison:
strict far/defect predicates and a corner predicate strict off the corner
prove the asserted equality classification. It does not construct a cover.

## A0: arithmetic versus theorem

The inherited global inequality with a particular constant C is a
hypothesis, not supplied by measured values. For q=r²/(2pi²), the actual
conditional exclusion follows from

    q*((4/pi²)*t²-54) > C*(t+log(3/2)),  t=log n.

Its positive root agrees with the developer formula. For C=1.4..1.7,
the coarse leading roots are 279291.35..339139.49 at r=1/64, and
17455.71..21196.22 at r=1/16. The rigorous-lower-bound conditional roots
are slightly larger. These are values of log n, not degrees.

On the full diamond, minimizing 1-a over rho>=r gives exactly
1-cos(r/2), attained at |alpha|=|beta|=r/2. This follows from the product
formula for cos(alpha)+cos(beta), whose first cosine factor is nonnegative
on the diamond. Substituting the sharper value gives conditional roots
7075.53..8591.62 at r=1/16. It must be retained as a separate sharpening
rather than suppressed by a blanket statement that R1 cannot improve.
It supplies neither the hypothetical C nor an actual finite bridge.
The independently evaluated quadratic model omits its remainder and uses
c=1.846 rounded to three decimals; it is only a diagnostic. The exact
conditional lower-bound roots do not use that rounded constant.

## Boundary profile and its obstruction

For alpha=pi*t, beta=pi*(1-t), the numerator identity reduces to

    (-1)^j G(u,v) = sin(pi*t) cot((u+v)/2).

The cotangent has no pole for 0<t<1. Other cosine collisions are removable
by continuity along t; the original polynomial is used there. At the
midpoint t=1/2 even these cosine collisions are absent: both
m(2j+1)+n(2r+1) and m(2j+1)-n(2r+1) are odd.

The map (j,r)->mj+nr modulo 2N has the two-element kernel
{(0,0),(n,m)}. These elements have opposite index parity, so its restriction
to the odd board is a bijection. The additional integer shift n permutes
residues, giving the complete shifted cotangent sum. At t=0 or 1 exactly
one summand has a compensating simple pole and the limit is 1; substituting
zero times infinity would not be valid. Separate index reflections show
S is even in each phase, giving all four boundary edges.

For the uniform remainder, the paired reciprocal sum differs from
2log N+C(t) by the tail of its integral-minus-pair errors. Convexity places
each pair between the doubled midpoint and endpoint values; the midpoint
and trapezoid errors give at most 1/(3k³), hence total at most 1/(2N²).
The regular cotangent part v=cot-1/x has |v''|<1 on [0,pi/2], as verified
in the full inherited PD-T270 proof. Comparing both symmetric sample
values and the integral with their common midpoint linear Taylor part
gives error pi²/(24N²). Multiplying by sin(pi*t) yields

    (1/(2pi)+pi²/24)/N² < 7/(12N²).

Both endpoint extensions are continuous. At t=1/2 the exact sum is L_N,
and PD-T270 supplies its separate 1/(4N²) remainder. Since a=0 there,
any approximation a*b_n has error at least L_N, which diverges. This
refutes only the specified leading-factor-only absolute o(1) profile;
it does not refute profiles containing a phase-dependent logarithmic term.

## Enlarged defect radius

Read the full new proof and the full predecessor PD-T224. At rho<=1/10,
a>=399/400, the perturbation is at most 1/20, and the baseline 1±cos w
on [pi/8,3pi/4] exceeds 3/40. The resulting positive numerator floor
397/16000 exceeds 1/64. With span below 26/m or 26/n, the signed
half-kernel pair contributes at least m/832 or n/832.

Recomputed the eight displacement/parity formulas, including the
horizontal q=-1 selections. The maximal phase perturbations 49/480 and
1/10 are below pi/4. Their folded angle ranges, interior row indices and
row counts are valid at n=48 and improve with n. The horizontal numerator
uses the fixed periodic second angle; exchanging it with a target angle
would not be valid. Each thin case gives 1/6656. The remaining centers
meet the endpoint-distance hypothesis of inherited PD-T222 at rho<1/8,
giving 1/1536. Thus the claimed weaker 1/8192 follows. No comparison with
primitive excess, and no extension to rho=0.2 or 0.3, follows.

## Aggregate energy

Read the full new energy proof and full PD-T227. Direct subtraction of
the inherited gradient ratios gives

    q_y-q_x=-(2n+1)/2+(1-a)/d.

On j=k, the three singular leading coefficients cancel to exactly
-2m³/[n(2n+1)²]. The stated sinc ratio errors and the separate upper-half
angle estimates give |q_x|<30m², |q_y|<31m², including j=n. Their
weighted sum is below 10000 n⁴ Lambda_c.

For j!=k, parity implies L=|j-k|>=2. The bounds |d|>=DL/m²,
C>=2k²/m² and the sine numerators give the unsimplified constants
1250 m⁷/n³, 8 m⁵/n, and 51200 m⁹/n⁵. Since m/n<=3/2 these are
bounded by 22500 n⁴, 61 n⁴ and 2000000 n⁴. Independently checked the
multiplicity at most four for each (D,L), the harmonic sums, the
130000000 and 391000000 constants, and the separate removable-index
contribution. Finally H=1+log m<=11 Lambda_c follows from Lambda_c>=2
for log n<20 and the quadratic logarithmic lower bound for log n>=20.
The combined coefficient is below 10^10. This proof never requires
uniform individual gradient/value ratios, so PD-N085 remains consistent.

## Global norm ratio and physical n^-2 radius

Reviewed the complete final T06 and T07 files. The rotated torus map
(u,v) mod 2pi -> ((u+v)/2,(u-v)/2) mod pi has two inverse branches,
related by (pi,pi). Each product bin of side pi/m lifts into two
parallelograms, each contained in coordinate intervals of length 2pi/m.
Such intervals contain at most three points in each mesh coordinate,
including wrapping and boundaries, so at most eighteen full-mesh points
map into a bin. The sine-chord envelope B_l=m/(1+d_l) is valid in all
bins, including d_l=0. Its sum is at most 2m(1+log m).
Consequently the two product terms sum to at most 144m²(1+log m)²;
the corrected cosine contributes at most 4N. Normalizing by 2N gives
Lambda_n<=110(1+log m)². The logarithmic lower bound and Lambda_c>=2
imply (1+log m)²<=250 Lambda_c, giving the stated ratio below 30000.
No maximum-location assumption occurs in this argument.

For the local consequence, PD-T227's Taylor/sign-change inequality and
PD-T251's slopes give, with z=n²H,

    lambda/Lambda_c <= 1-z/8+(10^10+90000)z²/2.

At 0<z<=10^-11 the quadratic coefficient after dividing by z is at
most 0.05000045<1/16. This proves the claimed loss z/16. The domain is
physical H=h_x+h_y; the corner reflection is x for even n and y for odd n.
This closes the explicit n^-2 local-radius scale while leaving practical
coverage and global maximizer exclusion unresolved. The original
rho<=1/64 target is larger than what this coarse constant supplies.

## Executed independent checks

Command, from the repository root:

```sh
python topics/padua-argmax-effective-2-20261105/code/independent_math.py --output topics/padua-argmax-effective-2-20261105/evidence/independent-math.json
```

The checker imports no developer or inherited probe module. It constructs
the finite corrected spectral polynomial and direct cardinals separately,
using Chebyshev recurrence at 70 decimal digits. Exact integer/Fraction
assertions check the finite reflection multiplicities, CRT bijections and
diagonal cancellation. The high-precision path checks degrees 2 through 8:
7784 cardinal four-copy identities; 175 physical/periodic comparisons;
175 full orbit Lebesgue identities, 175 vertical and 175 horizontal
projected identities; 119 admissible
centers at one common phase; 476 signed midpoint identities; 63 general
boundary/profile samples including vertices, near vertices and cosine
collisions; and 138 independently evaluated spectral gradient ratios.
The receipt records actual counts, errors, scalar energy ratios, A0 roots,
Python/mpmath versions, code hash and the input head of the final run.
There is no randomness. The final expanded run took about 6.3 seconds.

Finite agreement is not the proof of any all-n assertion. No interval
certificate or finite maximum certificate is produced. The analytic
reconstructions above supply the mathematical assessment. Code and receipt
are each below 16 KiB; no large generated output needs archival.

## Predecessor and novelty coverage limits

This is a mathematical supplement, not a complete novelty or protocol
audit. Scanned complete registry headings and relevant argmax rows;
read the relevant full candidates in phase-1 `ideas/r1-r2-r5.md` and
`ideas/r6-slopes-affine.md`, and the current H2/H3 gate and candidate
comparison. Read full relevant negative records PD-N079, N080, N082,
N083, N084, N085 and N086 and their scoped dispositions. Reviewed full
inherited proofs PD-T185, T215, T216, T223, T224, T225, T227 and T270;
PD-T218 was read for the cover/reduction context. No literature theorem
was newly imported or attributed.

The full 955-line `state/IDEAS.md` was **not** read by this checker.
Consequently this report makes no claim to have completed the required
full-registry novelty audit, and gives no new priority or candidate-novelty
classification. The developer's broader gate is a separate record; Claude
must still perform the prescribed full audit. The narrow negative-profile
scope was checked directly against the stated predecessors and does not
upgrade their MEASURED obstructions into general impossibility theorems.

## Dated impact check — 2026-11-05

The initial T01 review pinned SHA-256
`6bc81da3a961a3aab65f7989e1b7f11069dfb44e7196525263955fc9c1870b98`,
verified against its bytes at checkpoint `d98613e`. Reviewed the complete
diff from that checkpoint to the current T01. The developer confirmed
that T01 is frozen before this refresh. The added T04/T07 continuation
and scope wording correctly preserve their reviewed domains.

The substantive addition is the full periodic formula

    lambda_JK = sum_odd |H_rs+H_2J-r,s+H_r,2K-s+H_2J-r,2K-s|/(8N).

Each reflection orbit has 4, 2 or 1 representatives according to whether
the corresponding physical node has zero, one or two endpoint indices.
Every representative produces the same four-term sum, with repeated
terms retained at fixed points. Its aggregate coefficient is exactly
e_j*f_k/(2N), matching the physical cardinal identity. Thus the formula
and its endpoint normalization are correct. The warning to sum the four
terms before taking the absolute-value enclosure also checks.

Added a separate comparison with the direct spectral cardinal sum and
actually reran the independent checker: all 175 full-orbit checks passed,
including physical edges and corners. All prior assertions also passed.
The updated code and receipt are pinned below; their earlier versions
remain at `d98613e`. All other reviewed theory hashes remain unchanged.
No unresolved mathematical finding after this impact check.

## Final reviewed identities

These hashes pin the actual bytes read/reconstructed. Later edits need an
impact check; the run receipt separately pins the independent checker.

| File (relative to this topic) | SHA-256 |
|---|---|
| `theory/phase-structure.md` | `130820b34725a58e3dfd78602917d4eb77eb45d9476cae62532aa2579c42cbe4` |
| `theory/localization-diagnosis.md` | `43bf9eedc2931fdc5fa146fbcba92c615fac6fff39650fd21a80d86ab7a513c9` |
| `theory/profile-boundary-cotangent.md` | `8ccc83649464a568a12acaf03e265719b58dc4274b345b4a3a9be61eec652a3e` |
| `theory/profile-leading-only-obstruction.md` | `2545c5047d0c0cc743953b2141ff3766b9f919566e4fbf8b69aa2b9a02c9575e` |
| `theory/defect-radius-extension.md` | `a56fedfb1897c7bdbd1d761d7016e2bd0a016ccc7264440d05aa35a0d5d60a0d` |
| `theory/corner-weighted-energy.md` | `445f2c46907992b5c3d7173850205d4de8981bd9edebbf0413f0f4062e72bdf5` |
| `theory/corner-global-norm-ratio.md` | `2e9c0590ceb6032f0796a3383579751f241c13914918676418e85cd9a2c8dc59` |
| `theory/corner-n2-local-radius.md` | `280cfe73bc4ca82485a5f8df58ebbb864fd471a91403ac1b7849cdb4065bb5ad` |
| `code/independent_math.py` | `8481576a5fa766f2686208ab1ecc126f54e70970d2f9c89d38e3e12019ab5c8d` |
| `evidence/independent-math.json` | `3b2dba6591adde80ffade9bfd34920b462e467cea438a4d0acd2a86711088655` |
