# PD-T?argmax-bridge-C06-effective-argmax — Exact two-corner global argmax above exp(256)

ID kind: PD-T.
Aliases: C06 global assembly; explicit global upper boundary exp256;
full far / near noncorner / actual corner comparison.
Split from: the effective large-degree range of PD-T099, whose all-degree
statement remains OPEN. This improves the C03 sufficient boundary.
Split into: none; every supporting inequality retains its own source.

## Statement

Set the exact integer threshold

    N_* = ceil(exp(256)).

For every integer `n>=N_*`, use exactly PD-T101's corrected
even-checkerboard Padua cardinal polynomials. Their Lebesgue function
satisfies

    max_[-1,1]^2 lambda_n = Lambda_c(n),
    Lambda_c(n)=lambda_n(-1,-1),

and its global equality set is exactly

    {(-1,-1),(1,-1)}  if n is even,
    {(-1,-1),(-1,1)}  if n is odd.

This is an actual global argmax threshold. It remains astronomically
large; the finite gap `41<=n<N_*` is not closed. The existing finite
global range2--40 and the OPEN all-degree target PD-T099 are unchanged.

## Definitions and assumptions

All quantities are exact real numbers; logarithms are natural. Put
`m=n+1`, `N=nm`, `ell=log n`. Here N is the mesh product, not the
number of Padua nodes. Let `h_0=1,h_i=2` for i>0, and define the finite
corrected kernel

    D_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu)cos(jv),
    G_n(u,v)=D_n(u,v)-cos(nu).

Thus the exceptional coefficient at mode `(n,0)` is one. No mesh
interchange or symmetrization of that correction is made. Polynomial
values define every collision and zero throughout this argument.

Physical angles satisfy `theta,phi in[0,pi]`, with physical point
`(cos theta,cos phi)`. A physical odd center is

    0<=J<=n, 0<=K<=m, J+K odd,
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m,
    rho=|alpha|+|beta|<=pi.                                    (1)

The representation is required to be physical: both displayed angles
remain in `[0,pi]`. Define the odd periodic board
`Gamma^-={(r,s):0<=r<2n,0<=s<2m,r+s odd}` and primitive

    S_n(alpha,beta)=(1/(2N))sum_Gamma^-
         |G_n((r*pi+alpha)/n,(s*pi+beta)/m)|.                   (2)

The full four-copy triangle defect associated with (1) is denoted
`Delta_JK`. With exactly the positive endpoint weights of PD-T101,
PD-T215/364 give the identities

    lambda_n(cos theta,cos phi)
         =S_n(alpha,beta)-Delta_JK(alpha,beta),
    Delta_JK>=0, Delta_JK>=max(Q_v(K),Q_h(J)).                 (3)

The projected defects give lower bounds for the full defect; they are
not substituted as equalities in (3). The primitive is separately even
in its phases. The defect remains attached to its actual signed phases
and center. No assumption about a global maximizer, energy, cardinal
sign stability, sampled maximum or numerical approximation is made.

## Status and dependency boundary

Overall status: **PROVED** analytic assembly; supplementary independent
check pending. A complete proof under the explicitly stated, already
reviewed dependencies is written below. This is not the developer's
independent acceptance. The parent-required distinct reconstruction and
the campaign's formal Claude audit remain separate.

This is routine integration of existing results, with no new mechanism,
candidate generation, historical novelty or priority claim. The previous
[C03 assembly](C03-effective-argmax.md) is a predecessor; its old
constants and near-model onset are not premises here.

Load-bearing inputs, at their exact scopes:

1. [C06 full far profile](C06-far-full-profile.md) and
   [C06 far comparison](C06-far-comparison.md), independently accepted
   in [the C06 report](../independent-checks-C06-far.md): for integer
   `n>=ceil(exp(256))`, all signed phases with `1/2<=rho<=pi` satisfy

       Lambda_c-S_n > P(ell),
       P(ell)=191ell^2/15360-22ell/15-200>=3592/15.              (4)

   This is the actual finite primitive, on the whole closed far
   diamond, including its vertices and all polynomial collisions.
2. [C05 finite near-model comparison](C05-finiteh-model-comparison.md),
   independently accepted in [its report](../independent-checks-C05-finiteh.md):
   for every integer `n>=10^6`, `rho<=1/2`, the actual unchanged
   N1-15 model satisfies

       M_near(|alpha|,|beta|,log n)<Lambda_c+1/32,
       S_n(alpha,beta)<M_near(|alpha|,|beta|,log n)+3/14000.     (5)

   Its exact noncorner consequence is (8) below. This uses the
   finite-degree conclusion, not a limiting model or a validity onset.
3. [C02 dense-band defect](C02-defect-dense-band.md), independently
   accepted in [its report](../independent-checks-C02-defect.md): for
   integer `n>=4096`, every physical odd center with at least one
   interior coordinate and every physical signed phase `rho<=1/2`
   satisfies `max(Q_v,Q_h)>1/16`, hence `Delta_JK>1/16`.
4. [C05 actual-corner comparison](C05-corner-quarterangle-bound.md),
   independently accepted in [its report](../independent-checks-C05-corner.md):
   at each of the two actual nonnode corners, for every integer
   `n>=10^6` and inward `A,B>=0,A+B<=1/2`,

       lambda_n <= a Lambda_c+[log(n+1)/3+38](A^2+B^2),
       a=(cos A+cos B)/2.                                    (6)

   Its direct strict consequence is `lambda_n<Lambda_c` throughout
   the punctured patch `0<A+B<=1/2` whenever `log n>=25`.
   Its four reflected copies remain inside each cardinal absolute
   value, including initially zero cardinals and the corner collision.
5. PD-T101/215/225 and [PD-T364](../../padua-argmax-effective-2-20261105/theory/phase-structure.md):
   corrected cardinal normalization, endpoint reflection, exact
   full-defect identity, closed physical odd-center cover and equality
   of the two nonnode-corner values. The needed structural arguments
   are restated below.

The explicit source/report identities checked before this assembly are
recorded in `../attempts/C06-effective.md`. No supporting proof or report
is edited by this integration.

## Proof

### 1. Every numerical hypothesis is met

If `n>=ceil(exp(256))`, monotonicity of the logarithm gives
`ell>=256`. Also `e>2` implies

    exp(256)>2^256>2^20=1048576>10^6.

Thus `n>=10^6`, in particular `n>=4096`, and `ell>=25`.
These meet simultaneously the C06 far threshold, both C05 degree
floors, the strong C02 defect floor and the C05 corner strictness
threshold. No degree or model-validity threshold is relabeled as an
argmax threshold; the conclusion follows only after all cases below.

For reference, the exact scalar far budget obeys

    P(256)=3592/15>0,
    P'(256)=49/10>0, P''=191/7680>0.                           (7)

Consequently (4) has a strictly positive gap on its whole degree
domain, including its lower endpoint.

### 2. Closed physical cover and the exact common primitive

Choose a closed mesh rectangle containing `(theta,phi)`; at a square
boundary use an adjacent interior rectangle. In coordinates normalized
to that rectangle, write `X,Y in[0,1]`. Its two odd vertices are
opposite. Their L1 distances from `(X,Y)` are either
`X+Y,2-X-Y` or `1-X+Y,1+X-Y`. In either case the sum is two,
so at least one distance is at most one. Choose that odd vertex.
Multiplying its signed coordinate differences by pi gives a physical
representation (1) with `rho<=pi`.

This construction includes edges, corners, nodes, tied distances and
mesh boundaries. No uniqueness or strict inequality is required.
At an endpoint index the physical domain imposes the inward phase
sign: `J=0` gives alpha>=0, `J=n` gives alpha<=0, and similarly
for K and beta.

For completeness, let an original even-board node have indices p,q,
endpoint factors e_p,f_q and weight `w_pq=2e_p f_q/N`. The exact
cardinal formula is `L_pq=(w_pq/4)sum_four G_n`. Hence the weighted
sum of the four absolute values minus lambda is exactly the full
defect Delta, with each summand nonnegative. For each residue r mod2n,

    sum_(0<=p<=n,sigma=+-1:sigma*p=r mod2n) e_p=1.

Interior residues have one reflected preimage; the two endpoint
residues each have two coincident copies of weight1/2. The identical
identity holds on the m mesh. Thus the weighted absolute majorant
is exactly `(1/(2N))sum_even-periodic-board |G_n|`.
Translation by the odd vertex `(J,K)` turns that board into Gamma^-.
This proves (3) with precisely the primitive (2), retaining every
endpoint multiplicity and the corrected x mode.

Separate phase evenness follows by reindexing r to -r mod2n or
s to -s mod2m and using that G_n is separately even and periodic.
This permits absolute phases in (5), without changing the actual
signed center defect in (3). Every step is a finite polynomial
identity, so collisions and initially zero terms require no limiting
or sign-preservation assumption.

### 3. Far phases exclude every center class

If the chosen representation has `1/2<=rho<=pi`, apply (4) and
`Delta_JK>=0` from (3):

    lambda_n <=S_n<Lambda_c-P(ell)<=Lambda_c-3592/15.

This covers every physical center, both parities, the whole closed
fundamental-diamond boundary and its vertices. No positive lower
bound on a or inverse-a estimate is used.

In particular each physical Padua node lies in this far case.
Its mesh indices have even sum; the chosen center has odd sum.
The index L1 distance is therefore a positive odd integer, and the
cover makes it at most one. It equals one, so rho=pi. This includes
the two node corners. Their exact interpolatory values and all
boundary multiplicities are consequently consistent with the same
strict exclusion.

### 4. Near phases exclude every noncorner odd center

Suppose `rho<=1/2` and the selected odd center has at least one
interior coordinate. From (5), the strong C02 floor and (3),

    lambda_n=S_n-Delta_JK
       <Lambda_c+1/32+3/14000-1/16
       =Lambda_c-869/28000<Lambda_c.                          (8)

This is precisely the actual finite-degree noncorner consequence of
C05. Both the origin allowance in its model proof and the additional
phasewise primitive allowance in (5) are retained in that accepted
proof; neither is silently removed here. The floor applies separately
whenever J is interior or K is interior, hence to every noncorner
odd center, including centers on all four physical edges and all
near-endpoint parity classes. It is not a floor asserted at an actual
corner, and two projected floors are not added.

The bound includes zero phase at these noncorner centers, both axes,
all signed phases in the physical domain and the closed rho=1/2
boundary. Its use is pointwise under the exact radius condition;
no phase-box intersection is treated as a whole-box bound.

### 5. Actual corner phases and the exact equality set

The only remaining odd centers have both coordinates at endpoints.
The odd endpoint pairs are exactly

    (n,m) always;
    (0,m) if n is even;
    (n,0) if n is odd.

Under the cosine map they are the two corners listed in the statement.
The physical phase signs at each such center make
`A=|alpha|,B=|beta|` its nonnegative inward scaled angle distances.
At `(n,m)` the point is `(-cos(A/n),-cos(B/m))`.
For the other center it is the x reflection of that point when n
is even, or the y reflection when n is odd.

Since `ell>=256>=25`, the direct C05 strict corner consequence
applies whenever `0<rho=A+B<=1/2`. It gives
`lambda_n<Lambda_c` at every such point, including arbitrarily small
nonzero phases. No fixed positive primitive error is applied at the
corner origin; no energy or assumed global norm is used.

At `rho=0` the point is the actual nonnode corner itself. Its value
at `(-1,-1)` is Lambda_c by definition. For even n, x reflection
preserves the even checkerboard and endpoint weights; for odd n, y
reflection does so because m is even. Interpolation uniqueness makes
that reflection permute the corrected cardinal polynomials. Therefore
the two corner values are equal. This is a parity-preserving node
reflection, with no exchange of the two meshes or exceptional mode.

All other physical points are strictly excluded by the far case,
the noncorner near case or the punctured actual-corner case. The
shared rho=1/2 boundary is in the proved domains of both cases,
and the closed cover leaves no unassigned edge, node or tie. The
cosine map covers the entire closed square. Thus the maximum is
Lambda_c and its equality set consists exactly of the two stated
corners. QED.

## Checks, limitations and next step

The assembly is analytic, with already accepted mathematical premises.
No finite-degree or phase scan, numerical kernel evaluation, fitting,
energy extrapolation, runtime implementation or certificate cover is
part of this proof. Exact scalar bookkeeping is recorded in the attempt
file and does not replace the dependency or physical-cover argument.

Independent supplementary reconstruction of this particular assembly is
pending; the author has not reviewed or approved their own work. The
separate formal Claude campaign audit remains pending. This proof does
not validate executable corner/defect guards or certifier complexity.

The new sufficient upper boundary is much lower than C03's
`ceil(exp(10^7))`, but still astronomical. The finite gap
`41<=n<ceil(exp(256))`, practical onset reduction, cheap validated
degree-block methods and the all-degree PD-T099 conclusion remain OPEN.

## History

2026-11-06, auxiliary Codex mathematical integration worker, parent
allocation inherited; serving model/effort independently unexposed.
Rules read at `4b728b04216a5490910780bc609a82b853058426`; supplied C06
scientific inputs record `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`.
Only `theory/C06-effective-argmax.md` and `attempts/C06-effective.md`
are written. All supporting proofs/reports, shared files and Git state
are unchanged by this worker. No new novelty claim or subagent work.
