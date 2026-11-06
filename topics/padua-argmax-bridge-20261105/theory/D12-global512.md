# PD-T?argmax-bridge-codex-D12-global512 — Exact two-corner global argmax at degree512

ID kind: PD-T. Aliases: first complete D11 point-cover instance;
degree512 ordinary-phase Peano certificate.
Split from: the accepted D10 finite-cover sufficient implication.
Split into: none. This is a finite computational APPLICATION of that
implication, not a new mechanism or an all-degree theorem.

## Statement

Fix n=512,m=513 and use EXACTLY PD-T101/PD-T364's corrected
even-checkerboard Padua cardinal polynomials, with coefficient one at
the exceptional highest x mode, original endpoint weights and actual
finite-polynomial collision values. Write

    Lambda_c=lambda_512(-1,-1).

The completed author certificate and the independently accepted
mathematical/source premises establish

    max_[-1,1]^2 lambda_512=Lambda_c,
    argmax_[-1,1]^2 lambda_512={(-1,-1),(1,-1)}.       (1)

## Status and assumptions

Overall status: **PROVED (developer computer-assisted application)**.
The distinct fresh-build replay of the53 actual primitive point
enclosures, and independent acceptance of THIS theorem application,
are **PENDING** at this file's freeze. This records the complete
developer reduction and author evidence; it does not report independent
replay complete or authorize root's adoption of degree512 before that
review. Final Claude audit remains a separate obligation.

Exact real analytic arithmetic is used in the reduction; every final
certificate comparison is exact rational arithmetic. The numerical
trusted base and reproducibility requirements are explicit below.
No conclusion at another degree, extension of the analytic onset,
uniform positive gap at the two corner limits, runtime complexity or
historical speedup claim is part of (1).

## Accepted dependencies and exact instance inputs

1. [PD-T364](../../padua-argmax-effective-2-20261105/theory/phase-structure.md)
   supplies the exact closed all-physical-center cover, corrected common
   primitive S, lambda=S-Delta,Delta>=0 and S(0,0)=Lambda_c. The
   [D10 adapter](D10-cover-contract.md) specializes the sufficient
   predicates to512; its distinct supplementary mathematical review
   is ACCEPTED, report
   [independent-checks-D10-cover-contract.md](../independent-checks-D10-cover-contract.md),
   SHA256 `bbe827a02277d9dcdee9dca89861b9374e199e86674fdb1954a7308b2d49421b`.
2. [D09 global norm](D09-global-norm.md) independently proves
   S_512(alpha,beta)<34 for ALL real phases and the required signed
   families. Its accepted review is
   [independent-checks-D09-global-norm.md](../independent-checks-D09-global-norm.md).
   Thus M=34 is available BEFORE this argmax computation; no unknown
   global maximum or sampled point maximum supplies the interpolation norm.
3. [D08 ordinary-phase Peano bound](D08-point-box.md), used through
   D10, bounds S on an enclosing phase rectangle by four ACTUAL
   primitive vertex uppers plus its explicit curvature charge. The
   primitive is not interpolated in squared phases.
4. [C02 dense-band physical floor](C02-defect-dense-band.md) gives
   Delta>1/32 at every physical odd NONCORNER center when n>=160
   and the ACTUAL signed radius rho=|alpha|+|beta|<=1/2. This floor
   is never applied outside that guard or at an actual corner.
5. [D09 actual-corner patch](D09-corner-patch-512.md) gives, at BOTH
   actual degree512 nonnode corners and on the CLOSED inward rectangle
   0<=A<=pi/4,0<=B<=3pi/16,

       lambda_512<=Lambda_c-(19/5)(A^2+B^2).          (2)

   Both rectangles contain the entire inward half diamond A+B<=1/2.
   Its actual three-point computational premise is the immutable
   [d09-threepoint.json](../evidence/d09-threepoint.json), SHA256
   `34553e6d91dc77285f1bbb277a0f519c5a8a5da5f27a8f43501c7caf13631509`.
   The distinct fresh replay AND local application are already ACCEPTED:
   [independent-checks-D09-threepoint-result.md](../independent-checks-D09-threepoint-result.md),
   SHA256 `a54927a81158f8f1094057c0fc1f21b2e39bd922f8c0784567d3cabada2e85ca`.
   This premise is an actual lambda bound, not an S bound or a claimed
   global argmax. The new checker validates the essential repository
   receipt, exact endpoint hex identities, physical rational-turn inputs,
   and all three losses and q/pi^4 criterion; no old raw cache or old
   native binary is required as a runtime premise.
6. The accepted C11 point-source contract supplies outward enclosures
   of the ACTUAL corrected S at exact rational multiples of pi, including
   all partial-sum tails, endpoint rows and removable polynomial
   collisions. The D11 implementation integrates that contract with an
   exact checker independently reviewed in
   [independent-checks-D11-point-cover-source.md](../independent-checks-D11-point-cover-source.md),
   SHA256 `34c3270769d57fe89d383ded490d6c6554bd9332277c702e228e6b72f65c3f93`.
   Source acceptance alone did not certify an instance; the actual author
   run below supplies the new finite evidence, with distinct result replay
   still pending.

The rational constants are p_lo=157/50<pi<p_hi=22/7,
kappa=512/513 and the retained certified corner lower is

    Lc=7112277937770225/281474976710656<=Lambda_c.    (3)

This is the accepted D09 actual corner lower endpoint, not a rounded
corner upper or a finite inequality inferred from a limiting constant.

## Exact certificate, arithmetic and author evidence

The complete essential certificate is
[d12-point-cover-tree.json](../evidence/d12-point-cover-tree.json),
147bytes, SHA256
`62a0f35a51730ab57b0a0931122b9cab7c6ca1d113ea38dc779a059ade3eda2e`.
Its exact format is D11-midpoint-v1, integer n512, and the83-character
preorder string

    abababababab..b..a..ba...a..bab....ab...bab....ab...bab...a..ab..b..bab..b..aba....

The root is[0,1]^2. Token a or b splits the corresponding side at its
exact rational midpoint, then recursively supplies BOTH child subtrees;
a dot is a leaf. The decoder rejects missing siblings, invalid degree,
unknown/trailing tokens and nonprogress, and independently reconstructs
all boxes. There are83nodes,41internal nodes and42leaves, maximum
depth12. The closed child union is its parent, so this is a complete
binary partition, with no pending region. Leaves are clipped to

    T={(a,b):a>=0,b>=0,a+b<=1}.

The checker uses53distinct exact canonical primitive point inputs.
For all integers p,q with p+q even, finite-board reindexing gives
S^t(a+p,b+q)=S^t(a,b), and S is separately even, where
S^t(a,b)=S(pi*a,pi*b). Raw rectangle vertices outside T are first
folded by(a,b)->(1-a,1-b), then canonically selected within their
signed even-lattice orbit. No n,m mesh exchange is used. Only the
S INPUT is folded; the physical center, clipped rectangle and actual
radius guard retain their original geometry.

For B=[a_l,a_h]x[b_l,b_h], each actual vertex upper U_ij is an
outward C11 ball endpoint. The exact bound used on all of B is

    U_B=max_ij U_ij+(34*p_hi^2/8)
                  [(a_h-a_l)^2+kappa^2(b_h-b_l)^2]. (4)

D10's ordinary-phase Peano theorem proves S^t<=U_B even when B
extends outside T. Native operations use Arb/FLINT rigorous balls;
their ARF floor/ceil conversion yields outward binary64 endpoints.
Fraction.from_float retains those endpoints as EXACT dyadic rationals
before (4) or any strict comparison. A displayed decimal, FLOAT
producer value, reconstructed midpoint/radius or point success flag
is never used as an exact acceptance premise. All complete C11
partial-sum tails are already included in each returned ball.

The observed exact leaf classifications and minimum required margins
are retained in [d12-point-cover.json](../evidence/d12-point-cover.json),
SHA256 `5404f0b9679db125640ece212c85f86dfa7cfac13a41a9956c290e2804fe33c4`:

| Leaf predicate | Count | Minimum exact positive comparison margin |
|---|---:|---|
| FAR: U_B<Lc | 31 | `935713367702180327/453712364894045601792` |
| NEAR: U_B-1/32<Lc with the full actual-radius guard | 8 | `19706796211663228105/3629698919152364814336` |
| OUTSIDE: a_l+b_l>1 | 3 | Exact empty intersection with T |

FAR is the name of a primitive exclusion predicate; it does not assert
that every phase of that leaf has rho>=1/2. The strict outside test
uses >, so tangencies a_l+b_l=1 remain in the cover. Every NEAR leaf
also satisfies, exactly,

    2*p_hi*min(a_h+b_h,1)<=1,                         (5)

which proves pi(a+b)<=1/2 for every point of its clipped patch.
The general checker also implements D10's rational OUTER proxies
a+b<=1/(2p_lo) and a+b>=1/(2p_hi) at cut-crossing leaves, applying
the defect only on the actual near intersection and requiring the
far predicate on the actual far intersection. This instance has no
SPLIT leaf; its eight whole-near guards and31 full primitive exclusions
suffice. No floating cut classification or unguarded defect subtraction
enters these margins.

The first and only primary run used the frozen source released at
`e13a538bda80e6cc785f4835937b2ca338bc1d6f`, with command

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D11_point_cover/controller.py --run-once

It completed without a failure, pending leaf or cap stop. The FLOAT
producer used4.503105 inclusive CPU seconds; the separate fresh-build
exact checker used40.079552. The total through-summary CPU sample
was44.626205seconds, including supervision and descendants. The final
tiny accounting write was outside that last sample and remained bounded
by the supervisor's398CPU limit. Wall time was41.286455seconds. These
are measured instance costs, with no extrapolation to another degree
or historical speedup claim. The primary once-only command is consumed
and must not be rerun to reproduce an independent check.

The metadata postprocessor separately reconstructed all rational
predicates from retained dyadic outputs, with zero native calls. During
this theory application a second bounded2CPU metadata-only Python check
loaded the pure checker and retained53uppers, reconstructed the tree,
and recomputed (4)--(5) and both exact minimum margins above. It returned
83visited,53vertices and31FAR/8NEAR/3OUTSIDE, matching the essential
record. These checks are retained-data validation, NOT a fresh point
replay or independent validation of the53 native enclosures.

## Proof of the global equality classification

Fix an arbitrary physical point(theta,phi) in[0,pi]^2. PD-T364 gives a
physical odd center from

    C={(J,K):0<=J<=512,0<=K<=513,J+K odd},

a set of131841centers, and signed phases with

    theta=(J*pi+alpha)/512, phi=(K*pi+beta)/513,
    rho=|alpha|+|beta|<=pi.

Indeed the normalized L1 distances to the two odd vertices of a
containing mesh rectangle sum to2. One distance is at most1. An adjacent
interior rectangle handles square boundaries, and both tied charts are
allowed. This covers every center class without enumerating or sampling
their defect minima. Put a=|alpha|/pi,b=|beta|/pi. Then(a,b) belongs to
T, and separate evenness gives S(alpha,beta)=S^t(a,b).

Choose a closed certificate leaf containing(a,b). It cannot be an
OUTSIDE leaf. If its tag is FAR, (4) and its exact positive margin give

    lambda=S-Delta<=S<=U_B<Lc<=Lambda_c.             (6)

This works at every center, without a radius or defect assumption.
If its tag is NEAR, (5) proves the ACTUAL signed radius is<=1/2.
When the physical center is noncorner, at least one of0<J<512 or
0<K<513 holds. C02 applies since512>=160 and gives
Delta>=max(Q_h,Q_v)>1/32. Only ONE applicable projected floor is
subtracted; the projections are not added. Therefore

    lambda<=S-1/32<=U_B-1/32<Lc<=Lambda_c.           (7)

If instead this near center is an actual nonnode corner, its admissible
phase signs are inward. The independently accepted D09 patch (2)
applies and gives strict lambda<Lambda_c unless alpha=beta=0.
Its closed rectangle contains the entire actual near half diamond,
including axes and rho=1/2. At that zero phase the physical point
is precisely the actual corner, where PD-T364 gives Delta=0 and
S(0)=Lambda_c. No noncorner floor is applied there.

The only odd endpoint centers at this even degree are(512,513)
and(0,513), whose cosine images are(-1,-1) and(1,-1). The x
reflection preserves the node/cardinal system and their equal values.
Equations (6)--(7) and the corner patch make every other physical
point strictly lower. This proves (1).

All proofs use closed coverage: the cut rho=1/2, shared leaf edges,
tangencies, chart ties, square edges and nodes are included. In
particular a node corner is covered by a nonzero odd-center phase;
it is not another zero-phase nonnode corner. Finite-polynomial kernel
collisions and initially zero cardinals remain in PD-T364 and C11;
no pole quotient, sign-stability assumption, energy bound or presumed
maximizer localization replaces them.

## Trusted base, reproducibility and remaining review

The immutable source manifests are
[FREEZE.json](../code/post_audit_D11_point_cover/FREEZE.json), SHA256
`3c361e44db34babd168cdca0c785fe101abb80c5441cbf9e1c7314e52c73c8c1`,
and [SOURCES.json](../code/post_audit_D11_point_cover/SOURCES.json), SHA256
`0c9297f4cc6166d841440392f32f1c5e8a1abe479e2f3ba4a19a8371fcb27c2a`.
The frozen scientific/source contract is
[SPEC.md](../code/post_audit_D11_point_cover/SPEC.md), SHA256
`9993904b92226a64936a8affb9189e5c7d61ddb953000fc4f66f9d65a341eb78`.
Their historical UNEXECUTED language describes source-freeze time;
the subsequent primary outcome is recorded above and in the attempt.

The trusted implementation includes Python/Fraction, C++ compilation,
Arb/FLINT with GMP/MPFR, C11's accepted finite row/partial-sum arithmetic,
the accepted C02/D08/D09 mathematical premises, and the checker/source
integration. Complete build, preprocessed translation units, headers,
compiler/linker closure and actual loaded-file identities were retained
and rechecked at start/end. No hermeticity is claimed. The FLOAT producer
supplies only the tree; its arithmetic is not a proof premise.

The essential repository tree, code/manifests, accepted D09 receipt and
compact result record suffice to regenerate the complete checker result
in a clean cloud build. The original whole checker cache is37857bytes,
SHA256 `b1747afae4b6cbd6f53eb4604e214056b8aa128ffbbbf2033a39b714e7658bb8`,
under local-output/argmax-bridge-20261105/post-audit-D11/point-cover/.
All raw enclosures/counters, builds, maps and resource records stay whole
off Git, with paths/hashes in the compact result record. Permanent
cold-storage retrieval remains pending; no old raw output or old binary
is needed as an executable proof premise. Files are not split to evade
the essential-evidence limit.

The distinct result reviewer must actually rebuild and replay all53
required C11 point enclosures on this immutable147byte certificate,
validate the same source/data/corner inputs, and independently recompute
the exact closed geometry and strict predicates. Reading the author
cache or source audit alone does not meet that obligation. The reviewer
owns its separate frozen fixed-certificate command and receipt; it must
not rerun the consumed producer controller. Root adopts degree512 only
after the distinct native result/application review closes. Final Claude
audit, shared records and final IDs remain separate root responsibilities.

## Scope, novelty gate and history

This is the already-gated
[D11 point-cover application](../ideas/D11-point-cover.md) of D10/PD-T364,
using accepted ordinary-phase interpolation, C11, C02 and D09. No new
candidate or mathematical mechanism is generated, so a fresh exhaustive
unrelated-registry/literature gate is not claimed. The existing exact
tree/independent checker separation is the relevant implementation
criterion; an incomplete cover or failed outward enclosure would have
killed this INSTANCE. Existing failed/deferred methods and all older
proofs retain their scoped dispositions and quantifiers.

2026-11-06, parent-assigned Codex Sol xhigh mathematical metadata
application, bounded15min; serving metadata unexposed. Rules were read
at `5ecf97801631192fd10d84089c5a8c79bfb95138`; this instance's frozen
release/input head is `e13a538bda80e6cc785f4835937b2ca338bc1d6f`.
Only this new theory file is owned here. No native, board, producer,
phase-grid, root or quadrature job was executed for this application;
no old source/evidence, shared registry or mutable Git state was changed.


### Supplementary fresh-replay/application closure — 2026-11-06

The independent full53-point fresh-build replay and separate exact
geometry/application reconstruction are ACCEPTED, no unresolved findings:
[independent-checks-D12-point-cover-result.md](../independent-checks-D12-point-cover-result.md),
report SHA256775868b580d8285f3a441749725bc7251335ce6ea947df5bb48dd73833d228ce.
All exact endpoint/radius/counter rows are in the committed12,078-byte
independent receipt31d319bd...; the complete tree is147bytes62a0f35a....
The original independent worker completed its native replay before an
environment restart; its successor performed only the documented metadata
completion and final mathematical review. Neither native run was repeated.
This closes the earlier pending supplementary check and establishes the
finite degree512 instance. Final Claude audit remains separate.
