# Independent D36 generic-engine first-source audit

2026-11-06. Distinct reviewer requested Astra high; actual serving
model/effort metadata is unexposed. Root owns Git, shared records,
publication and release. This reviewer owns only this report for this
audit; no author source, attempt lock or scientific artifact was changed.

## First-freeze verdict

**NOT ACCEPTED FOR RELEASE: one unresolved fixture finding, D36-F1.**
The frozen controls necessarily raise an uncaught positive-premise error
before the native stage. No additional mathematical, degree-domain,
fresh-verification, source-provenance or CPU/evidence-accounting issue
was identified in the complete inspection described below.

This is a static finding; no module, control, compiler/native, arithmetic
script, engine, driver or producer was executed. Root has
directed preservation/publication of this first candidate and finding
before an author fixture-only correction. Do not release unchanged.
The corrected candidate will need a new frozen identity and focused
distinct review; this report does not preaccept an unseen edit.

## D36-F1: strict-leaf control violates its positive-L premise

Location: `code/post_audit_D36_engine/controls.py:42-43`, calling
`checker.py:81-85` through the fixed controls stage at engine.py:29-31.

The fixture fixes n1023 and tiny=[0,1/8]x[0,1/8], obtains delta=1/20,
then calls leaf with V=0,M=1,L=theta-delta and expects its returned
tag to be None. But with kappa=1023/1024<1,

    theta=(22/7)^2*(1+kappa^2)/512
          < (22/7)^2/256 = 121/3136 < 1/20.

The last rational inequality is exact because2420<3136. Therefore
L=theta-1/20<0. The leaf checker correctly raises
ValueError('exact Peano premises') at checker.py:85, before any strict
phase comparison is evaluated. The assertion does not wrap that call
in the reject helper, so controls.run() cannot complete. Engine
stage failure then prevents native checker/pilot execution, as intended
by its first-failure protocol.

Preserve the intended equality fixture by shifting BOTH V and L by1:

    V=1, M=1, L=1+theta-delta.

Now L>0, while U-delta=L remains exact, so the test reaches the
intended strict comparison. This is an actionable minimal correction,
not a change to the production checker, floor, geometry, resource cap or
degree. Preserve the original controls/source freeze and update only
the necessary fixture and its frozen bytes/hash after publication.
No author file was patched by this reviewer.

## First candidate identities and complete inspection coverage

Observed assignment identities match:

| File under code/post_audit_D36_engine | SHA256 |
|---|---|
| FREEZE.json | `89bc06b73067de13a1ed805d817b467f841844b408dbcf058326314487d6ff07` |
| SPEC.md | `e7348dc8d470b42da1c6a0cff33d87f7784f7e91542fdf6bae0d9eff91b90c67` |
| SOURCE.md | `0c074314e2df14ef350f12703c88e124711a8ab6bc7d07e072d4abb1cfcabfaf` |
| controls.py | `03a19bc5f787561490e858a119d0b7730c1c4f925b2879dbfe144382bcd87330` |

All seven new Python files and the full SPEC/FREEZE/SOURCE/idea/attempt
were inspected. All14 code_data hashes matched their frozen rows; the
seven new file byte counts also matched. The new builder differs from
the previously fully audited D34 builder only in its unused default
output base. The engine overwrites that base with the invocation's
exclusive OUT before building. All native D23/D07/original-C11 and
D09/setup helper hashes match the already audited D34 closure; complete
prior reads and source-domain reconstruction are reused at those exact
unchanged bytes, not claimed as a new native run.

AGENTS/WORKFLOW/CODEX hashes were checked unchanged against this
reviewer's D34 report. Their complete readings and the complete1154-line
IDEA/obstruction/disposition reading from D29/D32 are reused.
The registry still hashes
d7ec3aa6cf36f72e8057bcb90d8ac6eae8bf285a5b17f12526b26472ff4bddef.
The LOG continuation through D36 allocation/D37 prerelease was read;
observed read-only HEAD was ea078d27790b515e5d2d4043e2e681973d5a1345.

D36 is the assigned standard parameterization of the accepted D34/D32
mechanism. No unrelated full-source or external-literature reading or
priority claim is made. D34's source/result histories remain unchanged.
The deferred selected-arc1/64-from41 proposal is explicitly UNVERIFIED
and is not used in the source. The prior PD-N079/PD-N183 and fixed-sign
obstruction scopes remain respected: signed smooth components receive
Peano, the true global norm precedes absorption, and floors are not
inferred from rational proxy membership or summed projections.

## Degree-dependent mathematics and floor boundary audit

checker.degree accepts exactly type-int41..4095; bool, Fraction,
float and out-of-domain values cannot masquerade as a degree. The
CLI produces an int and every mathematical/runtime entry validates it.
Tree n, configuration n, state/cache n and native-call n are all explicit
and cross-checked. Searches plus complete source reads found no stale
41/42/164/224/43/80 substitution in production formulas, keys or counts.

The Peano coefficient and weighted split use n/(n+1), corner fourth
derivatives use its fourth power, and every B_n denominator uses n or
n^2. The half-diamond radius remains in radians and pi conversion uses
the exact157/50,22/7 bracket. Floor boundary dispatch is correct:

| Domain | Selected floor | Mathematical dependency |
|---|---|---|
| 41..63 | max(1/512,min(1/32,B_n(r_B))) | accepted D29-radius41 |
| 64..159 | max(1/64,min(1/20,B_n(r_B))) | original accepted C02 |
| 160..511 | max(1/32,min(1/20,B_n(r_B))) | original accepted C02 stronger tier |
| 512..4095 |1/20| accepted D29-floor512 |

Thus63/64,159/160 and511/512 take the correct sides;4095 is included
and4096 is rejected rather than importing C02's higher tier into the
declared engine domain. The41 lower bound comes from the independently
accepted new D29 proof, not a relabeled old C02 n64 assertion.

The code retains r_B=min(1/2,p_hi(ah+bh)) and the exact accepted scalar
coefficients of B_n(r). D32 proves rho<=r_B only on an ACTUAL near
physical subset, including boxes crossing the near/far seam. The
floor is for noncorner centers only, never all Q_N points or actual
corners. No monotonicity of B_n(r) is assumed. This correctly uses
Delta>=max(Q_h,Q_v) and at least one interior coordinate, not a sum.

The ordinary full-box Peano upper V+theta*M remains valid outside T
and at folded vertices. FAR is strict U<L; whole-NEAR additionally
requires2p_hi*high<=1 and U-delta<L; SPLIT checks every nonempty
closed proxy using low<=1/(2p_lo) and high>=1/(2p_hi). Equality is
retained. On a nonempty box, both proxy branches cannot be empty since
low<=high and1/(2p_hi)<=1/(2p_lo). There is no vacuous acceptance gap.

Complete binary midpoint syntax, both closed children, positive rational
widths, node/depth caps, no trailing/pending tokens, and strict
OUTSIDE al+bl>1 preserve the closed cover and tangencies. Canonical
keys fold above the hypotenuse and reverse only ON it; unequal meshes
are not exchanged in the interior. Folding does not change geometry.

Accepted D32/PD-T364 supplies both parities, signed physical charts,
original weights, exceptional coefficient ONE, nodes/edges/ties and
finite collisions. This is a conditional correctness mapping, not a
successful certificate at every supported n.

## Actual and analytic corner branches

Below1024, actual_keys derives precisely1/(4n),3/(16(n+1)), including
n1023 keys1/4092 and3/16384. These are PHYSICAL turn parameters for
phase endpoints pi/4,3pi/16. The actual-corner criterion keeps
u'=1/32,v'=9/512 and threshold M*p_hi^4/192; no pi^2 substitution
or fixed41 denominator remains. The true symbolic Lambda_c remains
the interpolation origin; fresh lower L only bounds nonorigin losses.
Zero/threshold-equality gaps fail. Unrestricted D08 covers both parity
corner half diamonds with strict descent off origin.

At1024 the branch switches to accepted D27's closed pi/4 inward
squares with loss(A^2+B^2)/8 for every n>=1024. The strict descriptor
includes both parity corners, analytic norm, D20 full-phase error,
D16 actual-origin allowance, completed model, computer-assisted PD-T271
and D02 uniform-limit dependencies. This is not a numerical substitution
for a missing actual evaluation or a purely analytic removal of PD271.
The phase-cover M does not artificially enter that independent corner
theorem. The accepted D27 review830eaf21... supplies this domain.

The runtime's build loop, CDLL/function binding, actual-key loop,
expected-call count and parser actual-row count all use the same
n<1024 boundary. For1024..4095 it builds/loads/binds ONLY S, requires
zero actual rows and cannot call the absent lambda function. For the
actual branch, n<=1023 is inside unchanged D07's2..2048 guard.
The redundant runtime2048 check does not widen either domain. No
actual native source precision, inclusion or guard was modified.

## Fresh verification and retained proof integrity

engine verify mode preserves original certificate bytes with exclusive
creation and compares their bytes/hash with the preregistered input.
The source input is reauthenticated before/after stages and finalization.
Strict JSON rejects duplicate/nonfinite entries. D36-kept-proof-v1,
exact top-level key set, degree/pi/schema, source SHA/bytes, point column
units, floor/corner identities and same-degree tree are checked; legacy
D34 versions fail. Source path is not required to match an old absolute
checkout path, while SHA/bytes must match the current accepted freeze.
That preserves the intended portability without a Git metadata dependency.

Canonical rational keys must be unique and equal EXACTLY the supporting
set. TREE retains all final nonempty leaf vertices; GRID adds all13
coarse-grid keys. The origin must be present. Actual keys and order are
exact below1024; analytic certificates must contain none. Endpoint hex
is canonical finite binary64 converted to exact Fraction; bad types,
noncanonical rationals and negative upper diagnostics are rejected.

Old numeric verification entries are parsed for schema/diagnostic shape,
not trusted as proof. In particular engine.py:58-84 freshly queries ALL
parsed S keys and obtains L from the fresh origin LOWER. It freshly
queries all applicable actual points. It retains the original tree and
METHOD, then independently recomputes GRID M from fresh13keys or TREE
M from fresh final corners and valid theta<1. Old M/L/uppers/margins
and bit-equality flags do not enter those fresh acceptance inequalities.
No equality of old/fresh bits or improvement of M is required.

Only the selected method is tried; a failed fresh tree absorption,
phase or actual-corner check ends the attempt. There is no producer
discovery, pruning, alternate method or old-degree cache rescue in
verify mode. Importing the producer module does not invoke its routine.
Each mode builds a new invocation-local n/source-scoped cache, and the
native runtime separately prevents duplicate new calls and cap excess.
No old endpoint is seeded into that cache.

The fresh certificate carries freshly retained uppers/lower/actual values
and fresh verification. Before emission, verify_essential reconstructs
ALL final math from that new certificate and requires exact agreement
with the completed worker verification. Its origin consistency, positive
norm and strict corner/phase predicates are independently enforced.
Historical primary-account acceptance is not needed to infer new proof
from valid geometry plus fresh included endpoints; the current invocation
still needs its own accepted account and actual EXIT0. A mode named
verify alone does not make its operator independent.

Produce mode retains corrected D34's13-key discovery grid, true-global
D14 norm, deterministic larger weighted-width midpoint DFS, lower child
first and sorted missing queries. It selects the predeclared minimum of
valid coarse/tree ceilings, TREE winning ties, before ALL final tests.
Preliminary coarse corner diagnostics are not final acceptance and do
not trigger a fallback. Every selected norm premise is retained; the
final tree proof does not secretly use discarded grid/parent values.

## Numerical closure, resources and evidence

The unchanged numerical sources remain D23 S/local partial
J2,K8,LH4,WD16 and D07 actual with ORIGINAL C11
J16,K32,LH16,WD96, with P160,CP640,MP640. Full harmonic, midpoint,
endpoint-derivative and arithmetic radii stay in the returned balls.
The general D23 inclusion holds from2; its small160+ uniform error
is not imported below160. Outward arf FLOOR/CEIL exports and exact
binary64-to-Fraction conversion remain. Radius diagnostics are not
substituted for mathematical endpoints.

Counter checks are parameterized: S retained4n and ordinary2(n+1)-4,
actual rows n+2, and the existing direct/block/fallback/root/sign/axis
limits. All6/13counter entries and raw returncodes/endpoints/radii/CPU
are recorded before postchecks. D07 internal certified row recovery
remains fully recorded/charged; it is not an external source retry.
The separate builders resolve the correct original include trees.

Fresh source snapshots, preprocessed TUs, toolchain/header/dependency
hashes, linked/loaded SONAME bytes, Python identity and before/after
maps are recorded/rechecked. The generic code calls no Git command
or Git metadata API. Checkout relocation is therefore compatible with
relative source closure and fresh runtime recording. Compiler/Arb/
Linux/LP64/system behavior remain explicit trusted dependencies;
portability is not a hermetic or formally verified execution claim.
Provisioning is only the unchanged pinned setup path within budget,
requiring cloud-runtime guidance if actually invoked later.

The driver accepts only --run-once and passes fixed1023/produce/pilot1023
to the engine in the SAME process. No queue or alternate degree is run.
Explicit resolved output is exclusive; existing paths fail. Generic
API availability does not authorize other degree runs.

Declared and enforced controls/checker/whole wall literals are15/900/1000,
with whole120CPU, controls2,worker100,safety110,native10/15 and poll.25.
The previous D34 path/wall mismatches do not recur. Node2047/depth18
and256uniqueS/at most3actual caps remain fail-closed. Driver/import,
provisioning/build/children/native/verification/serialization/supervision
costs are included through absolute process CPU accounting.

The accepted group-kill/subreaper/reap protocol and stage completion
checks are retained. ECHILD fixes waited-child CPU c and no later
children launch; absolute selfHard<=floor(120-c)-1 gives total<=119<120
with required headroom. Incomplete accounting cannot accept. Freeze,
configuration/original-input/loaded identities and postserialization
CPU gates persist through finalization. Atomic final-account rename
plus directly observed EXIT0 is required; provisional receipts and
summary Booleans are insufficient. Produce and verify have distinct
final result labels and further result-review obligations.

One whole raw record retains complete available calls/cache/trace,
original input, selection candidates, controls/stages/build/runtime/maps,
including failure/active-call state. Original input bytes are additionally
preserved unchanged. Manifested binaries/TUs remain off Git. The fresh
essential proof retains ALL chosen mathematical inputs and self-checks
before its strict whole<16384byte gate. Overflow is a failure, never
permission to trim points, split outputs or rescue the case. First
failure remains canonical across later finalization errors.

## Execution record and required next step

Only text/search/diff/hash/byte-count/read-only Git inspection and
written algebra occurred. No optional metadata job, module/control
import, compiler/native/scalar/phase/degree/root/quadrature/engine/
driver/producer job or primary lock action occurred. The fixture
failure follows from exact formulas, not an actual control execution.

Publish/preserve first FREEZE89bc06b7... and this finding before the
minimal fixture-only repair. Focused review must authenticate the new
controls/freeze and preserved original history before root releases the
sole fixed1023 pilot. No scientific success, new degree or generic
existence/cost guarantee follows from this source inspection. Final
Claude audit remains separate.


## Focused fixture correction closure — 2026-11-06

**ACCEPTED: D36-F1 CLOSED; no remaining finding.** Before this append,
the original report was verified as exactly16357bytes with SHA256
`172731fb5508ba14bc655609a0093ae4f4f1a8b1b3e08780f256df218c78c375`.
That entire first-review prefix is preserved unchanged.

Read-only comparison against first publication
`cb73c95f12b2a1c34c0768b1a1060c428802017d` confirms ONE code-line change:
controls.py now supplies V=1,L=1+theta-delta instead of V=0,L=theta-delta.
Geometry,M,n,case count and the equality U-delta=L remain unchanged.
Since theta>=0 and delta=1/20, L>=19/20>0. FAR cannot pass because
U=L+delta>L; the closed near-proxy test rejects the intended equality.
The fixture therefore reaches the production strict predicate with valid
premises and returns the expected None, by direct source/algebra review.
No actual control execution is claimed.

Corrected controls.py is2801bytes, SHA256
`7063f8cd4ce7bfda9a3d10b96d8659402cf7adac62a430c7eafd626fa1406bc4`.
Corrected FREEZE is7073bytes, SHA256
`d74817158e9a08de67a89e2c790ea1e39b5729fc17c0df002b5b15564b5b2001`;
only its controls byte-count/hash row changed. SPEC is unchanged at
`e7348dc8d470b42da1c6a0cff33d87f7784f7e91542fdf6bae0d9eff91b90c67`.
All other production/native/helper code, mathematics, guards, inputs,
resource caps and pilot remain unchanged. SOURCE/attempt only append
repair provenance; their four original Git blob references were checked.

No imports, metadata/control test, compiler/native/scientific job,
engine/driver/pilot or lock action occurred in this focused review.
This is a prerelease fixture repair, not a scientific retry. Root
publication and explicit fixed1023 release remain separate; acceptance
of this source supplies no completed pilot, finite degree result or
all-degree existence/cost claim. Final Claude audit remains separate.
