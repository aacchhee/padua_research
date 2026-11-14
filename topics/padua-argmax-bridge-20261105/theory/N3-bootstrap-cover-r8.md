# PD-T?argmax-bridge-codex-N3-bootstrap-cover-r8 — A phase-cover sufficiency theorem with explicit maximum-exclusion leaves

ID kind: PD-T.
Aliases: N3 round8; holistic maximum-bootstrap cover; maximum-exclusion-plus-defect;
global-maximum-bootstrap; inward half-phase corner diamond.
Split from: none; explicit certificate integration of N3-bootstrap-corner.md
and PD-T364, whose previous statements and predicates remain unchanged.
Split into: numerical certificate instances and their verification records
are separate. No instance is asserted in this theorem.

## Statement

Fix an **integer 2<=n<=128**, put m=n+1 and N=nm, and use precisely
the even-checkerboard corrected cardinal polynomials of PD-T101. Let
lambda_n be their Lebesgue function on [-1,1]^2 and Lambda_c its value
at either of the two nonnode corners. Use the exact phase functions,
classes and domains defined below.

A complete finite phase certificate satisfying predicates F, O, L, X
and B below proves

    max lambda_n = Lambda_c,
    argmax lambda_n = {the two actual nonnode corners}.             (C)

Predicate B is a **maximum-exclusion** predicate for actual corner
classes together with a separate strict comparison for every noncorner
class. It is not pointwise corner descent before global closure.
Its energy premise is the already accepted fixed finite theorem
N3-bootstrap-finite.md for all integers2..128, authenticated by the
specific independent receipt below. No caller-selected energy assumption,
all-n energy theorem, existing global argmax or a-priori norm ratio is
part of the theorem.

The explicit new interface is

    format = "n3-phase-maximum-bootstrap-v2"
    mode   = "global-maximum-bootstrap"
    kind B = "maximum-exclusion-plus-defect".

This is a sufficient-certificate theorem, not a claim that a round8
certificate has been constructed or accepted at any degree.

## Definitions and assumptions

For physical angles theta,phi in [0,pi], let

    C = {(J,K):0<=J<=n, 0<=K<=m, J+K odd},
    D = {(alpha,beta): |alpha|+|beta|<=pi},
    D_JK = D intersect
           [-J*pi,(n-J)*pi] x [-K*pi,(m-K)*pi],
    theta=(J*pi+alpha)/n, phi=(K*pi+beta)/m.             (1)

The actual nonnode-corner centers form

    C_corner = {(n,m),(0,m)} if n is even,
               {(n,m),(n,0)} if n is odd.              (2)

All remaining members of C are noncorner centers, including centers
on a physical edge. A class of phase representations and a physical
point are different objects: one phase box is used at many centers.

Let G_n=D_n-cos(nu) be the corrected finite kernel of PD-T364, with
the exceptional (n,0) coefficient equal to one. On the odd periodic
board Gamma^-={(r,s):0<=r<2n,0<=s<2m,r+s odd}, put

    H_rs(alpha,beta)=G_n((r*pi+alpha)/n,(s*pi+beta)/m),
    S_n=(1/(2N))*sum_Gamma^- |H_rs|.

The exact full reflected-cardinal triangle defect at center (J,K) is
Delta_JK, as defined in PD-T364; its nonnegative projections are
Q_v(K), Q_h(J). Their exact relationships are

    lambda_JK = S_n-Delta_JK,
    Delta_JK>=max(0,Q_v(K),Q_h(J)).                    (3)

Here lambda_JK is lambda_n at the physical point in (1). The actual
corner-orbit value is

    C_n(alpha,beta)=(1/(8N))*sum_Gamma^-
       |H_rs+H_-r,s+H_r,-s+H_-r,-s|,                 (4)

with periodic indices. For either admissible actual corner center,
lambda_JK=C_n. Reflections are taken in integer indices with the phase
offsets unchanged; all four values are summed before absolute value.

Every accepted nonoutside leaf B_box is a closed rational rectangle
[a_lo,a_hi] x [b_lo,b_hi]. In implementation its endpoints are exact
rationals represented by finite binary64 numbers, not a floating
approximation used in a final inequality. Define

    a=max(|a_lo|,|a_hi|), b=max(|b_lo|,|b_hi|),
    rho_box=a+b.                                      (5)

The certificate provides independently valid bounds on the whole box:
U_S>=sup S_n, U_C>=sup C_n, and a lower bound d such that

    d<=Delta_JK(alpha,beta)

for every noncorner center (J,K) and every phase in B_box intersect
D_JK. A conservative lower screen is sufficient; it need not be sharp.
For example, form rigorous profile lower bounds for every J,K and take
the minimum over every possibly admissible noncorner center of
max(0,lower(Q_v(K)),lower(Q_h(J))). Omitting a center is allowed only
if its physical domain provably misses the box. Including an extra
nonphysical center can only weaken the screen. The optional PD-T366
floor1/8192 remains restricted to n>=48 and rho_box<=1/10.

Let pi_lo<=pi<=pi_hi and 0<L<=Lambda_c<=U_L be independently
validated constants. Every bound and every final inequality is exact or
outward validated. Supplied producer bound numbers are diagnostics;
the independent checker recomputes its own U_S,U_C,d,L and pi bounds.
The finite-polynomial collision values, zero terms, weights and
multiplicities of PD-T364 are retained.

## Exact predicates

Use four closed roots obtained from [-p,0] and [0,p] in each phase
coordinate, where the declared finite p>=pi_hi. A binary path fixes a
rectangle by the declared longest-side bisection and binary64 operation
order, with both children sharing the same midpoint. The leaves form
complete prefix-free partitions of all four roots, not just a sample.
Unknown kinds, gaps, duplicate/prefix-overlapping leaves, missing roots,
stagnant splits and any pending region prohibit acceptance.

The allowed leaf predicates are:

| Label / exact kind | Independently required predicate |
|---|---|
| X / `outside` | minabs([a_lo,a_hi])+minabs([b_lo,b_hi])>pi_hi. It has no admissible phase in D. |
| F / `far` | U_S<L. This gives strict comparison for every physical center. |
| O / `corner-orbit-plus-defect` | U_C<L and U_S-d<L. The two inequalities respectively handle actual-corner and noncorner centers. |
| L / `local-corner-plus-defect` | A valid **unchanged old pointwise local predicate** and U_S-d<L. The old predicate is specified below. |
| B / `maximum-exclusion-plus-defect` | rho_box<=1/2, the fixed finite bootstrap premise below, and U_S-d<L. Only actual-corner classes use maximum exclusion. |

The comparisons U_S<L, U_C<L and U_S-d<L are **strict** even on
degenerate boxes and phase-tree boundaries. The B geometry inequality
allows equality. Zero phase is not a blanket exception for noncorner
centers. A leaf within rho_box<=1/2 whose noncorner inequality fails
is unaccepted and must remain unresolved or be split.

For completeness the unchanged old local predicate is the union of:

    a^2/(2n^2)+b^2/(2m^2)
       <=max(1/(2N^3),1/(10^11 n^2)),                (L1)

and, only under its own fixed accepted n2..128 local-range premise,

    max(a,b)<=1/128,
    a^2/2+n^2*b^2/(2m^2)<=1/16000.                  (L2)

PD-T251/369 give (L1); N3-corner-batch.md and the old independent
receipt e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0
give (L2). Each proves pointwise strictness away from its actual corner.
The new bootstrap receipt does not silently authorize (L2), and neither
L1 nor L2 is enlarged to rho_box<=1/2.

## Fixed finite energy premise and parsing boundary

N3-bootstrap-finite.md establishes

    W_n<=(3/4)*n^4*Lambda_c, for every integer2<=n<=128,             (E)

using the distinct actual127-case GMP reconstruction. This theorem is
an accepted dependency, not an assertion inside a submitted certificate.
The implementation must resolve exactly its fixed published evidence:

| Required code/evidence | SHA256 | Bytes |
|---|---|---:|
| evidence/independent-bootstrap-energy.json | f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b |3190|
| code/check_bootstrap_energy.py | 915c6c7c40e8c9e0c748cf50c2fe278f6760d79a9e725939aed1553269030972 |7876|
| code/check_corner_exact.cpp | 3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3 |5725|

Paths in this table are relative to this topic. The guard reads one
immutable receipt snapshot, verifies its fixed identity before semantic
use, and verifies the actual fixed code bytes. It must not open an
arbitrary receipt-selected or caller-selected source path. No current
theory, idea, handoff, log, registry or audit prose is a runtime hash pin.
The local raw manifest is regenerable execution provenance, not a
required unique proof input; its receipt identity does not require its
presence in the replay workspace.

Semantic controls require the fixed format
`padua-independent-bootstrap-energy-v1`, accepted Boolean true,
exact integer degree_first2, degree_last128 and degree_count127,
every_integer_degree_checked true, all_new_predicates_passed true,
all_native_exit_statuses_zero true,
all_masks_cardinal_counts_and_positive_denominators_verified true,
independent_execution true and producer_endpoints_imported false.
The normalized threshold is exactly `3/4` and the predicate is exactly
`4*energy_upper <= 3*n^4*corner_lower`. Source/runner identities must
match the fixed table and the build's source identity. The n2 control
retains both_enclosed true, corner_exact `3`, energy_exact `331/18`,
nonzero_cardinals5 and zero_cardinals_omitted1. Typed booleans and
integers, not Python truth aliases, are required for these fields.
The identity guard authenticates the accepted aggregate receipt; it
does not claim that parsing metadata reruns the127 mathematical checks.

The new format, mode and degree are validated independently of these
contents. `type(n) is int` and2<=n<=128 are required; bools, floats,
strings and degrees outside that range reject. The candidate's required
`bootstrap_premise` descriptor is exactly

```json
{
  "receipt_sha256": "f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b",
  "degree_first": 2,
  "degree_last": 128,
  "normalized_threshold": "3/4",
  "phase_diamond_radius": "1/2"
}
```

It is descriptive redundancy and cannot supply (E). Missing/additional
keys or changed values reject; production separately authenticates the
fixed evidence. The old v1 format must reject B; the new format requires
its explicit mode and known leaf kinds. Duplicate JSON keys, NaN/Inf,
nonnumeric/Boolean endpoints, reversed intervals and malformed tree
addresses reject. Constants must enclose the checker's independently
computed pi and Lambda_c intervals. Roots and bisections are reconstructed
from validated constants and paths, so candidate leaf bounds cannot move
the geometry. A limited-leaf replay never reports global acceptance.

## Status by part

Overall status: **PROVED analytic sufficiency reduction**, under the
explicit valid-enclosure and complete-certificate hypotheses. The finite
energy theorem is an already established named dependency; no new
computer instance is claimed here.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Complete cover with F/O/L/X/B implies (C) for each fixed n2..128 | PROVED | Written holistic proof below |
| Rational B-box geometry and its inward physical containment | PROVED routine coordinate lemma | Exact sine argument below |
| Energy(E) throughout2..128 | Separate PROVED dependency | N3-bootstrap-finite.md and the fixed independent receipt |
| Any new complete round8 numerical certificate | Not asserted | Implementation/source review and actual independent replay are separate |
| Energy for all n>=2, effective global onset and PD-T099 | OPEN external targets | No finite extrapolation or all-n consequence |

Candidate disposition: retained explicit certificate variant of accepted
round7 and IDEA330/454/457. The Taylor bound, phase identity and
maximum-absorption mechanism are inherited. This file's new content is
the precise replacement of a pointwise Corner obligation by an explicitly
different maximum-exclusion leaf inside a holistic cover theorem.

## Depends on

- PD-T101: corrected finite cardinals, continuity, positive weights,
  cardinal interpolation and uniqueness under parity-preserving reflections.
- PD-T364: exact identities(3),(4), all physical odd-center coverage,
  endpoint weights and all-center projected profiles; its old finite
  pointwise predicates remain unchanged.
- PD-T227 and PD-T251: true-global-norm Taylor model, zero-cardinal
  inward slopes and A_n,B_n<=-n^2 Lambda_c/8. These are already assembled
  in N3-bootstrap-corner.md.
- N3-bootstrap-corner.md: under(E), no noncorner global maximizer with
  0<z=n^2(h_x+h_y)<=1/8 at either nonnode corner. Its proof is separately
  accepted in independent-checks-bootstrap.md.
- N3-bootstrap-finite.md: fixed finite(E), established by the actual
  independent receipt above. The old local L2 receipt supplies only L2.
- The unchanged outward enclosure algorithms and their source reviews
  supply the required valid numerical bounds when implemented; metadata
  alone cannot establish these bound hypotheses.

## Proof

### 1. All physical points have a covered odd-center representation

Given(theta,phi) in [0,pi]^2, choose a physical mesh rectangle containing
it, using an adjacent interior rectangle on any outer boundary. Normalize
within that rectangle to(x,y) in[0,1]^2. If its two odd vertices are
opposite, their L1 distances are x+y and2-x-y; in the other parity
orientation the distances are1-x+y and1+x-y. In each case the sum is2.
At least one odd vertex therefore has normalized L1 distance<=1.
The resulting (J,K) and phases in(1) belong to D_JK, including ties,
edges, physical nodes and mesh vertices. No nearest-center uniqueness is
assumed. This is the finite coverage argument of PD-T364/225, with no
asymptotic localization threshold.

Since p>=pi_hi>=pi, each such phase lies in at least one of the four
closed roots. Complete prefix-free bisection partitions cover every
point of each root. A closed shared midpoint belongs to at least one
child (in fact both); it is never omitted by the path description.
An X leaf cannot contain the selected admissible phase: for any phase
in that box, |alpha|+|beta|>=minabs(a interval)+minabs(b interval)>pi_hi
would contradict membership in D. Thus at least one selected leaf is
of kind F,O,L or B. Covering whole boxes, including possible extra phases
outside D, only strengthens the required enclosures.

### 2. Reflection, corner classes and exact inward geometry

Because m=n+1, the corner-index parity test gives exactly(2): (0,0)
is even, (n,m) is always odd, and exactly one of(n,0),(0,m) is odd.
The angular corner(pi,pi) is physical(-1,-1); the other is(0,pi)
when n is even or(pi,0) when n is odd.

For even n, replacing j by n-j preserves j+k parity and both endpoint
weights, so x reflection permutes the Padua node set. For odd n, m
is even and k mapped to m-k gives the corresponding y reflection.
Polynomial-space invariance and cardinal uniqueness imply that each
reflection permutes the cardinal polynomials. Consequently it preserves
lambda_n and Lambda_c. Physical derivative signs change with the
reflected coordinate, while their squared energy contributions and
inward first variations are preserved. It exchanges the two corners in
(2), so the fixed energy and maximum-exclusion theorem apply to both.
This uses no prior statement about their global optimality.

At an actual corner, J=0 requires alpha>=0 and J=n requires alpha<=0;
K=0 requires beta>=0 and K=m requires beta<=0. These are exactly the
physical-domain restrictions in D_JK. The nonnegative inward angular
distances are therefore xi=|alpha|/n and eta=|beta|/m. The physical
inward increments are exactly

    h_x=1-cos xi=2sin^2(alpha/(2n)),
    h_y=1-cos eta=2sin^2(beta/(2m)).                  (6)

For a B leaf, |alpha|<=a, |beta|<=b and a+b<=1/2 by the
**full-box rational** test, hence the actual phase rho is at most1/2.
If the phase is nonzero, at least one angular distance is positive.
The strict inequality |sin t|<|t| for nonzero real t then yields

    0<z=n^2(h_x+h_y)
       < [alpha^2+(n/m)^2 beta^2]/2
       <= (|alpha|+|beta|)^2/2
       <= (a+b)^2/2 <=1/8.                           (7)

The first strict inequality also follows directly from(6): in the
physical interval xi,eta in[0,pi], 1-cos vanishes only at zero.
At alpha=beta=0 one has z=0 and obtains exactly the center corner.
Thus the permitted boundary rho_box=1/2 lies within the accepted
bootstrap physical patch at every nonzero-phase admissible corner point.
No numerical pi, cosine evaluation, midpoint test or quadratic physical
approximation enters(7).

The orbit identity(4) is the exact actual-corner formula at both centers:
at J=0 or n, reflection2J-r is congruent to-r modulo2n;
at K=0 or m, reflection2K-s is congruent to-s modulo2m.
Endpoint multiplicities in PD-T364 are retained, including collisions
and the removable00 cardinal. The same full-box U_C therefore handles
either actual corner class in an O leaf.

### 3. Noncorner classes retain strict comparison at every leaf

Consider any selected representation with (J,K) outside C_corner.
An F leaf gives lambda_JK<=S_n<=U_S<L<=Lambda_c. At each of O,L,B,
equation(3) and the uniform lower screen give

    lambda_JK<=S_n-d<=U_S-d<L<=Lambda_c.              (8)

This includes zero phase at any noncorner odd center. No corner theorem
or exception is invoked in(8). The box lower screen may conservatively
include centers with empty exact intersection. The endpoint sign tests
may discard J=0 only when a_hi<0, J=n only when a_lo>0, and the
analogous K tests; each discarded center then has empty physical
intersection by(1). When a box merely touches phase zero the endpoint
center must be retained. This proves that the existing all-center
screen's conservative treatment is sufficient here.

At actual corner classes, F still gives strict comparison. O gives it
through lambda_JK=C_n<=U_C<L. L supplies its old pointwise theorem,
strict away from the actual corner. B at nonzero phase supplies only
the assertion from(7) and the accepted bootstrap that the physical
point cannot be a global maximizer. This is the precise semantic
difference; no pointwise value bound is substituted for it here.

### 4. Holistic global maximum and exactly two equalities

The Lebesgue function is a finite sum of absolute polynomials, hence is
continuous on the compact square. Its actual maximum M exists and
M>=Lambda_c>0 because both corners in(2) have that value by reflection
and the corner identity S_n(0,0)=Lambda_c.

Suppose an arbitrary global maximizer q is not either corner. Choose
the admissible odd-center representation and accepted leaf given by
part1. If its center is noncorner, (8) contradicts lambda_n(q)=M
and M>=Lambda_c. If its center is actual corner, the phase is nonzero:
zero phase would equal the center corner. F or O gives the same strict
contradiction; L gives old pointwise strictness; and B excludes global
maximality by the finite energy theorem and(7). All possibilities have
been exhausted. Thus every global maximizer is one of the two corners.

Both corners actually have the common value Lambda_c, so M=Lambda_c
and both are global maximizers. Conversely, any point with value
Lambda_c now realizes M and is a global maximizer; the preceding
exclusion proves it is one of those two points. This establishes(C),
including the exact equality set, all phase boundaries and both parities.
The two node corners are not hidden exceptions: interpolation gives
their value1, while Lambda_c>=2 by PD-T251's dependency, and in any
case they are covered by part1 as nonzero phases of odd-center charts.

At a putative B-corner global maximizer the accepted bootstrap uses the
same unknown M on both sides of PD-T227's inequality and absorbs its
remainder. It does not assume M=Lambda_c. Only **after** the complete
argument above may that identity be inserted to derive pointwise loss
on a B patch. This post-closure consequence cannot justify accepting an
incomplete partition or relabeling B as an old local predicate. QED.

## Implementation controls needed before a consequential replay

These are specified controls, not results of executions by this author.

1. Authenticate the fixed receipt and actual GMP source/runner bytes;
   corrupt receipt bytes, source bytes and each semantic range/threshold/
   independent-execution/mask/n2-control field in isolated semantic tests.
   Test both missing and duplicate/extra descriptor keys, candidate-selected
   receipt paths and caller-asserted energy flags. Production must reject
   before any such value authorizes B. No prose path may be opened.
2. Check n2,32,128 and reject1,129,True,False,32.0 and strings. On
   all four phase sign quadrants, verify rational rho_box=1/2 passes,
   one-ULP outward enlargement fails and a valid asymmetric box passes.
   Retain zero-width/origin and inward edge cases. Use all endpoint
   maxima, not a center/corner sample or binary64 sum for the final test.
3. Under the new format/mode a B leaf must fail when own U_S-d equals
   L or exceeds L, even with valid geometry and energy. Valid geometry
   alone never passes a noncorner class. A false U_C diagnostic has no
   role in B; changing an ignored diagnostic is not a meaningful control.
   Test the two n-parities' actual corner indices and inward signs;
   all noncorner zero-phase classes still require(8).
4. Old v1 checkers must reject B/new format; the new checker rejects an
   old or missing mode and unknown kinds. Old L predicates must reject
   large bootstrap-only boxes even when B would allow them. Compare
   the inherited arithmetic/bounds, tree rules and strict predicates
   against round6; no new C/Arb enclosure formula is authorized here.
5. Reject missing root/sibling, duplicate/prefix leaf, false outside,
   invalid bisection, false completion, pending regions and partial
   max-leaves replays. Reconstruct leaf boxes instead of trusting them.
   Check constants against the independent kernel, finite outputs and
   exact Fraction strictness. Origin exceptions never relax partition.
6. Preserve arithmetic independence: producer MPFR, checker reviewed
   Arb/GMP, with immutable input snapshots/fresh build and runtime
   provenance. A named producer evaluation flag may request defect
   computation even when its corner-orbit upper bound fails. In the
   unchanged C source the old `local` parameter controls only that early
   exit; setting it for (oldlocal OR bootstrap_geometry) requests a
   bound, not a theorem. Python dispatch must retain oldlocal alone for
   L acceptance and the separate full B conditions for B acceptance.

## Checks, scope and open items

This proof uses analytic arguments and the previously accepted finite
energy theorem. The author read the fixed evidence bytes and source
identities; no new energy reconstruction, phase kernel execution, parser
control campaign, full producer or independent replay was performed here.
The separate code/reviewer records must identify their own actual work.
Proof and protocol freeze identities are review provenance only and
must not be added as runtime prose pins.

Next: independent mathematical/source/premise review, then at most the
coordinator's separately preregistered one-degree n32 overlap calibration.
Known global range2..40 is unchanged. A complete accepted n32 calibration
would validate an already known degree; it would not establish a new
global degree or an all-n cost law. The finite energy theorem ends128;
there is no all-n energy, n>=10^6 bootstrap or effective onset here.
PD-T099 and the remaining all-degree bridge stay OPEN.

## History

2026-11-06, Codex mathematical developer, coordinator-assigned
mathematical allocation, actual serving model/effective effort unexposed.
Rules/input `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
The complete prospective gate and alternatives are retained in
`../ideas/N3-bootstrap-cover-r8.md`; attempt and unexecuted verification
plan are in `../attempts/N3-bootstrap-cover-r8.md`. The exact leaf
semantics and receipt identities were communicated to the disjoint
implementation worker before code finalization. All old source, prose,
proofs and receipts remain unchanged by this worker. No final ID or
independent-review acceptance is asserted in this author record.
