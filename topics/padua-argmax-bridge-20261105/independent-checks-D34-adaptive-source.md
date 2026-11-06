# Independent D34 first-source prerelease audit

2026-11-06. Parent-assigned distinct mathematical/domain/technical review,
requested Astra high; actual serving model/effort metadata is unexposed.
Rules previously read at4f8c169171e55b7d5f00f57a8b3ce8340a498960;
read-only HEAD observed later as eb9329c28be18d77eeb817f634202d626ee11f92
during root integration. Root alone owns Git, publication and release.
Only this report was changed.

## First-freeze verdict

**NOT ACCEPTED FOR RELEASE: two unresolved protocol findings.** The
mathematical implementation matches the accepted D32/D29 contract on
inspection, and no additional mathematical or numerical-domain finding
was identified. However, the controller uses a different exclusive
attempt path and longer wall limits than the frozen SPEC/FREEZE declare.
Do not execute this unchanged first candidate.

Root has explicitly directed preservation/publication of this first
unreleased candidate and findings before an author path/resource-only
correction. The canonical declared values are the adaptive directory,
checker wall900seconds and whole wall1000seconds. A corrected source
requires a new authenticated freeze and focused distinct review; this
report does not preaccept an unseen patch. There has been no scientific
attempt, control-stage consumption or primary lock creation.

## Findings with exact locations and correction requirements

**D34-F1 — Exclusive attempt path differs from the frozen contract.**
`code/post_audit_D34_adaptive/controller.py:6` sets OUT to
`local-output/argmax-bridge-20261105/post-audit-D34/static`.
SPEC instead declares
`local-output/argmax-bridge-20261105/post-audit-D34/adaptive`, also the
builder's default. All controller/worker registration, stage, raw and
final-account files follow the former path. Native later sets BUILD.LOCAL
to OUT, so this is a consistent execution at the wrong registered path,
not merely an unused cosmetic constant.

The no-retry lock is OUT.mkdir(exist_ok=False) at controller.py:184.
Using a different path changes which attempt is consumed and which
receipts the prescribed workflow observes. Correct the controller to the
already declared adaptive path, preserve the first freeze, and publish
the changed source/new freeze for focused verification. Do not consume,
remove or reuse either attempt directory as part of this correction.

**D34-F2 — Enforced wall limits exceed the registered limits.**
`controller.py:76` assigns checker wall1000 instead of900;
`controller.py:85` uses whole wall1100 instead of1000. SPEC/FREEZE and
the controller's own preregistration at line186 all declare15/900/1000
for controls/checker/whole. Thus the preserved preregistration would
misdescribe the supervisor actually running and could allow work beyond
the declared wall stop. CPU limits are separate and do not cure that
resource-contract discrepancy.

Correct the two actual supervision constants to900 and1000, retaining
the controls15, CPU policy, source/precision/degree/geometry and all
other frozen choices. Authenticate the resulting controller/new freeze
and verify declared and enforced values agree before any release. This
is a prerelease source correction, not authorization for a larger cap or
a scientific retry.

## Frozen identities and scope of inspection

Observed first-candidate identities match the assignment:

| File under code/post_audit_D34_adaptive | SHA256 |
|---|---|
| FREEZE.json | `28897ba9df5b3fc30475b8a7ecfda5c43b2a22b19628f67bff998e2fb1c94e6b` |
| SPEC.md | `88c9006a6f35d6a1417d6b0fe9437cf70476c194c22b3cc7b5cb0aecf8fa97e2` |
| SOURCE.md | `25ad5a1cc1ec63cec18f504ff95969ac97fa15d50eb7ee4135e24ab45c88a6ee` |
| checker.py | `7f54fc433f39fc56ae09855a33ab6cdbc3ff78d0c39f1820ccca2d6eea041520` |
| controller.py | `05d41911cff591714d3c91d28cdb34f03855a22461f665a98975d1a935f80a7b` |

All13 executable/native/helper entries in FREEZE.code_data had their
SHA256 and byte counts inspected and matched, including D23 point/partial,
D07 point, original C11 point/partial, D09 controller and setup.py.
The six new Python modules, SPEC, SOURCE, FREEZE and D34 idea/attempt
were read in full. D23 point/partial and D07 point were read fully;
the original C11 partial differs from D23 partial only in the four
declared order constants, as shown by a read-only exact diff. D09's
specific reused endpoint/CPU/identity/atomic-save/subreaper/group/reaping
helpers and import guard were inspected, as was the complete setup.py.
No claim of reauditing every unrelated D09 execution path is made.

Complete current1154-line IDEA/obstruction/disposition and rule readings
are reused from this reviewer's D29/D32 reports. Registry SHA256 remains
d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef.
D34 is the assigned standard D15/D14/D19/D23/D29/D32 implementation
composition. Its candidate preserves prior alternatives and obstruction
boundaries. Full PD-N079/PD-N183 readings remain applicable: no squared
smoothness of S or unproved sampled-to-global norm is used. No priority
or external literature claim is made.

## Mathematical matching: exact checker and producer

The checker fixes N41,kappa41/42 and157/50<=pi<=22/7. All proof
arithmetic uses Fraction. Exact finite binary64 outward endpoints are
converted by Fraction.from_float; canonical hex roundtrip and finite
checks prevent nonfinite or ambiguous retained endpoints. Stored decimal
approximations do not decide a proof predicate.

Canonicalization folds only above a+b=1 and reverses coordinates only
on that hypotenuse. The original unequal meshes are never interchanged
in the interior. Thirteen sorted canonical quarter-triangle keys support
the actual D14 norm ceil(784 maxupper/663), with a positive fresh LOWER
at S(0,0). The cache is created in the one worker, never loaded from old
evidence, and every call uses literal41. The freeze/n/API cache identity
is retained. Native and wrapper independently prohibit duplicate new
calls and calls beyond256S/3lambda; cached duplicates do not call native.

The sole producer is lower-child-first depth-first, not breadth-first.
This agrees with the detailed frozen SPEC/FREEZE. It uses the coarse
global norm throughout discovery, requests sorted missing vertex keys,
and splits the larger squared weighted width, ties a, at an exact
midpoint. It counts every node, records PENDING before work, and fails
at an unaccepted depth18 leaf, more than2047nodes or the point cap. It
does not run FLOAT, prune, optimize polygons or restart on final failure.

The decoder independently reconstructs both closed children and rejects
missing children, bad degree including bool, bad tokens, excessive
depth/node count and trailing subtrees. OUTSIDE is strictly al+bl>1;
tangent boxes remain. Tree keys include all retained physical box vertex
representatives. Finite midpoint depth makes every split positive.

The full-box Peano coefficient is
theta=(22/7)^2(wa^2+kappa^2 wb^2)/8. The full upper V+theta M is valid
also outside T, using the unrestricted D08 signed-component theorem.
FAR uses strict U<L. NEAR additionally requires2p_hi high<=1 and
strict U-delta<L. SPLIT tests the closed rational outer proxies via
low<=1/(2p_lo) and high>=1/(2p_hi), retaining equality. Those proxies
cannot both be empty on a nonempty P because low<=high and
1/(2p_hi)<=1/(2p_lo). Thus there is no vacuous leaf acceptance gap.
The conservative same full-box upper for both branches is allowed by
D32; its possible cost or failure is not a soundness issue.

The radius-floor code exactly reproduces D29 at n41:
r=min(1/2,p_hi(ah+bh)), a=1-r^2/4,
U0=347a/1000-157r/500, V0=17a/20-r/2,
W0=779a/750-5r/6 and
B=11711U0/48400-120V0/(157*41)-250W0/(157*41)-100V0/(3*41^2).
It uses max(1/512,min(1/32,B)). Its logical use is exactly D32's
ACTUAL near noncorner branch; no floor is asserted on every Q_N point
or at the actual corners, and projections are never summed.

D32's accepted full physical odd-center cover, signed phases, both
parities, original weights/corrected exceptional coefficient and finite
collision identities remain the theorem bridge. The source need not
enumerate physical centers to invoke that accepted implication. At n41
the eventual candidate equality set is(-1,-1),(-1,1), conditional on
completed valid evidence and fresh replay.

## Actual corner and final norm

The actual API keys are exactly(1/164,0),(0,1/224),(1/164,1/224),
the physical turns1/(4n),3/(16m). They are not phase turns1/4,3/16.
The ordered three upper values and actual origin lower enter
q=min((L-Wx)/(1/32),(L-Wy)/(9/512),(L-Wxy)/(1/32+9/512)).
The threshold is M p_hi^4 max(1/32,kappa^4*9/512)/6=M p_hi^4/192,
and acceptance requires strictly positive q-threshold. Zero losses or
threshold equality fail. The radial squared coefficient is correctly
(q-threshold)/(2p_hi^2), retaining symbolic TRUE origin in the theorem.
The D08 rectangle covers the inward half diamond at both parity corners.
No analytic D17/D27 low-degree substitution is made.

The coarse-norm preliminary corner calculation has require=False and
records only a diagnostic. It is not final acceptance and does not
trigger a rescue. Once the tree completes, a tree norm is available iff
every retained theta<1; then R=max V/(1-theta), Mtree=ceil(R).
The one predeclared choice is the minimum of the valid coarse/tree
ceilings, TREE winning ties. ALL final phase leaves and the actual
corner criterion are recomputed with that chosen M before success.

GRID retains all13grid uppers in addition to final vertices; TREE
retains exactly its final vertex union. The origin is always a needed
vertex and its fresh lower is separately retained. The kept-proof
checker independently reconstructs the selected sufficient norm and
every final predicate. It deliberately does not prove that selected M
is minimal against an omitted alternative: such minimality is not a
mathematical premise. Raw evidence retains both candidates and the
actual predeclared selection. No discarded child/grid margin supplies
a hidden norm or corner premise.

## Numerical domain, build and endpoint provenance

The two builds choose different source origins. Cheap S includes D23's
local partial with J2,K8,LH4,WD16; actual lambda includes D07 and ORIGINAL
C11 partial with J16,K32,LH16,WD96. Both preserve P160,CP640,MP640.
Quoted include resolution uses the original source parent as an include
directory; copying the top-level source into a fresh work directory does
not redirect the actual-lambda include to cheap partials. The two unique
CDLL paths expose c07_point and d07_point separately; internal mathematical
functions are static. No FLOAT/reference/scalar API is bound or called.

D23's full error inclusion is valid from n2 with its exact row/block/
pole guards. Source partial() adds harmonic, derivative and midpoint
tails to the returned Arb ball and retains full numerical uncertainty.
No2e-7 small uniform n160 error allowance appears in the D34 acceptance
path. Source degree guards remain S2..2147483647 and actual2..2048,
so41 is admitted without a source-domain extension. D07's certified
root/sign handling and internal full-row fallback remain unchanged and
charged; there is no external retry or cheap-tail actual-lambda route.

Native export uses directed arf lower FLOOR/upper CEIL; radius is a
diagnostic and never an acceptance-width substitute. Runtime saves
every raw returncode/hex/counter/cost record before postchecks, then
rejects nonfinite or inverted endpoints, negative radius/lower and bad
counter closures. S retained164/ordinary80 and endpoint-zero counters
match n41; actual rows43, no node/corner shortcut and guarded counts
match the three registered physical points. All13actual counters remain
in raw output. Endpoint authentication is not inferred from hex alone.

Build snapshots, preprocessed translation units, compiler/tools/header/
linked dependency identities and before/after loaded file maps are
retained/rechecked. LP64/binary64 is explicit. Loaded SONAME reuse must
match expected bytes. Runtime close checks loaded/mapped/Python identity
and manifest artifacts; controller repeatedly rechecks frozen code.
Provisioning, if needed, is the unchanged pinned package setup inside
the budget and still requires its cloud-runtime guidance before actual
use. No setup/network action was performed here. This remains an
explicit trusted compiler/Arb/system-runtime contract, not hermetic
or formally verified machine execution.

## CPU/failure accounting and retained evidence

Apart from F1/F2, inspection matches the declared CPU path: whole120,
controls2,worker100,safety110,completed-call10,unfinished-call15,poll.25.
Native duration starts before its active-call checkpoint, conservatively
charging that write. Every completed call record is persisted before
returncode/duration/counter rejection. Worker limits and supervisor group
CPU checks include builds and descendants. Stage completion requires
exit0,no stop,complete reaping,stage CPU bound and COMPLETE checkpoint.

The Linux subreaper kills/reaps the process group on stops and after
stage return. Before finalization, wait4 establishes ECHILD, fixes waited
child CPU c and prohibits later child launches. The absolute parent
hard limit is at most floor(120-c)-1, so c+selfHard<=119<120, with
two CPU seconds of required headroom. Incomplete accounting cannot
accept. Postreceipt, postsummary/output and postfinal-account-serialization
CPU checks remain. Atomic final rename prevents a partially written
successful final-accounting file; actual observed exit0 is additionally
required. Provisional checkpoint/summary/essential success is insufficient.

The ONE whole raw-evidence.json contains the complete available checker
state, every native raw record, unused points/cache, producer trace,
grid/norm selection, controls and stage results, both build manifests,
runtime identities and full before/after maps. Failure paths use the
last available authenticated checkpoint; an interrupted native call
retains its active-call record rather than inventing an output. The
separate stdout/stderr, descendant records and manifested binary/TU
artifacts remain on disk as operational provenance. Raw packaging checks
the supervisor's immutable checkpoint identity. It does not trim or
split point records to satisfy the essential-evidence cap.

The essential proof keeps ALL selected mathematical S uppers, origin
lower, three keyed actual uppers, full tree, norm/floor/corner/source
identity and reconstructed verification. The parent reruns the pure
kept-proof checker before serialization and demands exact verification
agreement. The WHOLE serialized certificate must be strictly<16384bytes
or fail; no pruning, point-dropping or split-output rescue follows.
Returned source/freeze identities and later fresh replay are still
needed to authenticate inclusion of those endpoints. Counts, hashes
or passing tags alone are not treated as mathematical premises.

First worker failure is retained before reraising; controller preserves
the first failure across raw/essential/finalization errors. Failed stages
cannot launch the later scientific stage or produce accepted accounting.
The exclusive directory is the one-shot lock, subject to F1's correction.
No actual n41 result or cost was observed in this review. A successful
future primary would still require independent FRESH replay of every
retained S/origin/actual point and all final proof checks before adoption.

## Review execution record and next obligation

Only read-only text/search/diff/hash/byte-count/Git-identity inspection
and this prose write occurred. No import, synthetic arithmetic helper,
author controls, compiler, native call, producer/controller, scalar,
phase/degree/root/quadrature job or primary directory action occurred.
No reviewer synthetic test ran;
the two findings are directly visible literal source discrepancies.
Author controls were read but their PASS is not claimed.

Retain this first freeze and both findings. Correct only the declared
path/wall mismatches in a new reviewed freeze before root release.
Mathematical soundness matching above is scoped source inspection;
the release verdict remains blocked until focused correction review.
Final Claude audit and any later independent finite-result replay are
separate obligations.
