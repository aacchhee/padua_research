# D09 three-point actual-corner predicate: preparation contract

**PREPARATION ONLY. No compile, root solve or point call authorized yet.**
Rules/input9d5e8c7a1a8fab6017d5dd9406daec0d834b0bbf,2026-11-06.
Codex parent-assigned Sol medium,20-minute preparation cap; serving
metadata unexposed. Root owns Git/shared state. Distinct review of D08
mathematics, the global norm input and this source must precede root
numerical release. Neither a developer proof nor this source authorizes
an actual mathematical instance.

## Mathematical dependencies and exact criterion

Read complete D08-point-box-norm.md, D08-point-box.md and
D08-point-box-corner.md plus their idea/attempt. These developer-PROVED
contracts await distinct reconstruction at preparation. They supply the
global norm adapter, even squared-phase actual-cardinal interpolation
and the three-loss sufficient condition. They do NOT assert our numerical
premises pass. The function is actual lambda, not common S or a smooth
squared-coordinate interpretation of S.

Let n=512,m=n+1,kappa=n/m. For phase endpoints A=pi*a, B=pi*b set
u'=a²/2, v'=b²/2. Evaluate the actual x-axis, y-axis and diagonal
vertices at inward turns

    (a/n,0), (0,b/m), (a/n,b/m).

Use the unchanged C11 pointS(n,0,0) identity for the actual nonnode-corner
value Lambda_c. Its outward LOWER endpoint L and the three actual point
UPPER endpoints Ux,Uy,Uxy give exact rational lower losses

    dx=L-Ux, dy=L-Uy, dxy=L-Uxy,
    q=min(dx/u',dy/v',dxy/(u'+v')).

With a proved global physical norm upper M, the exact acceptance test is

    q > (22/7)^4 * M * max(u', (n/m)^4*v') / 6.       (G)

All these operations use Fraction/integer arithmetic, with strict >.
There is no tolerance or rounded decimal substitution. The pi^4 factor
is essential: physical U=pi²u', V=pi²v', and c=q/pi² in D08. (G)
implies the rational strict barrier coefficient lower

    epsilon_lower=[q-threshold]/(22/7)^2 > 0.

This is safe because q>0, pi<22/7, and the same pi_upper enlarges the
remainder. The true origin stays symbolic Lambda_c; a rounded upper
at the origin is never substituted. No global argmax is presumed.

## Fixed primary and only permitted fallback

Primary a=1/4,b=3/16, hence u'=1/32,v'=9/512 exactly. Preserve all
three point uppers/losses and the primary criterion, including failure.
Only if the COMPLETE primary criterion is false may the single fixed
fallback a=1/6,b=5/31 be attempted. It has u'=1/72,v'=25/1922.
There is no search, precision retry, intermediate rectangle or second
fallback. An unfinished/native/control failure does not license fallback.

For each rectangle, prove its whole positive phase sides exceed1/2
using a*(157/50)>1/2 and b*(157/50)>1/2;157/50<pi is the elementary
repository bound (C02-defect-dense-band.md(24)). Thus either successful
rectangle contains the complete positive inward rho<=1/2 diamond.
The other parity-correct nonnode corner is transferred only through
D08's accepted node-preserving reflection. This is a local corner
patch, not a complement cover, whole-degree theorem or global bridge.

## Global norm: exact input, pending mathematical release

SOURCES.json fixes n32 upper46 (46²>2*32*33) and prospective n512
model upper34 supplied analytically by root. The latter's final proof/hash
and distinct review are pending at preparation; it must not be adopted
or executed until root release after acceptance. It is not inferred
from point values, measured maxima or presumed corner maximality.

The controller computes the independent CS integer upper as
ceil(sqrt(2n(n+1))) using math.isqrt and an exact square comparison.
It then takes min(CS upper,the supplied positive exact rational upper).
These are46 at32 and725 at512 before the model minimum. At512 the
supplied prospective34 would be selected IF its global proof is accepted.
The machine norm contract is immutable within a run. Updating a bound
requires a new freeze/review before release; no automatic norm estimate
or hidden data-dependent adjustment is present.

## Unchanged D07 API and rigor of endpoint conversion

The full accepted D07 point/root/reference source and focused source
review were inspected, together with its executed evidence. The native
source, controls, C11 point.cpp/partial.cpp, precision, root certificates,
fallbacks and all returned error balls remain unchanged. The D09 worker
imports the frozen D07 build.py and changes ONLY its in-memory LOCAL
output destination to the new D09 namespace. Source/include paths,
compiler flags, arithmetic and library APIs remain the same; this
output-location override is recorded in the fresh build manifest.

D07 export7 calls arb_get_lbound_arf/ubound_arf then arf_get_d with
ARF_RND_FLOOR/CEIL. Consequently its finite binary64 outputs are outward
endpoints of the complete Arb enclosure, including every C11 tail.
C11 c07_point uses the same outward extraction. No native print/source
change is necessary. Python retrieves exact binary64 values and uses
Fraction.from_float on LOWER/UPPER endpoints; its resulting dyadic
rational is exactly that stored endpoint. Each is saved as numerator/
denominator text and float.hex. Decimal-looking display is not used
for mathematical arithmetic. In particular Fraction(str(float)) is
forbidden. Nonfinite, reversed or invalid intervals fail the run.

Only n32(control) and n512(new) may call point routines. First run one
n32 generic complete finite-reference control via unchanged d07_compare,
xi=1/512,zeta=1/1056, requiring its entire independent512-bit reference
ball to be contained. This checks the new controller/API path, not a
new n32 certificate or the three-point criterion there. Then one n512
C11 S0 corner call, followed by three primary actual D07 points; at most
three fallback points follow under the exact condition above. Thus at
most eight native calls including the control and corner. D07 work
counters/fallbacks/radii are retained, and C11 corner counters remain
separately labeled. No whole-box native API, large finite reference,
old C08 run or speedup comparison occurs.

## Controller resource, retention and source-review gates

After final mathematical/source acceptance and root release ONLY:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D09_threepoint/controller.py --run-once

Cap60 aggregate CPU-s including pure preparation controls, fresh build/
helpers, native control, corner/vertices, supervisor and finalization.
Reserve1CPU for pure controls (hard process limit1, below root's5CPU
allowance), leaving a later run cap59. Safety trigger54, worker57 hard
limit, parent59 hard limit; wall cap180s. Before another native call
require worker+supervisor aggregate<44. Stop the entire run after the
first completed call>20CPU-s; kill an unfinished call at25CPU-s. These
stops may leave the mathematical predicate unresolved. No source/precision
change, rescue or automatic repeat is allowed. The root release may
withhold running entirely if the global bound remains unaccepted.

Linux subreaper setup and full orphan-helper wait4 reaping reuse the
reviewed D07 controller contract. Final descendant CPU is labeled complete
only after no children remain; incomplete cleanup is a lower bound and
never success. Direct immutable stdout/stderr avoid pipe deadlock.
Exclusive registration/worker locks refuse reuse. Atomic checkpoints
retain pending vertex labels, every completed result, raw first output
repr, first exception and the primary/fallback decisions. Vertex results
are committed and removed from pending BEFORE a completed-cost stop.
A killed combined n32 point/reference API exposes no intermediate result.

FREEZE.md is a MACHINE-READABLE JSON CODE/DATA MANIFEST despite its file
extension, not a pinned scientific prose record. It pins this controller,
SOURCES.json and native/evidence ancestors; SPEC/theory/idea/attempt hashes
are passive review provenance only. Worker start/end checks the registered
FREEZE.md identity and code/data identities. No proof prose is enforced
as a runtime input. Source review must inspect SPEC/controller consistency.
All scientific dependency acceptance still belongs to the distinct review
and root release, not a self-asserted Boolean in code.

Fresh output is confined to local-output/argmax-bridge-20261105/
post-audit-D09/threepoint/. Capture the preprocessed TU, complete compiler/
header/native linked closure and actual loaded mappings before/after,
exact inputs, dyadic intervals, all calls/times/counters, selected global
norm and rational losses/q/threshold/gap/epsilon. No larger essential file
than16KiB is planned. Existing primary records are never overwritten.

## Preparation verification

Only static source inspection, hashing and AST parsing precede this
SPEC. After this SPEC, pure Python controller tests may exercise
synthetic dyadic endpoints, arithmetic predicates, conditional fallback
logic and completion retention. They must not compile/load a research
library, evaluate actual n512 points or manufacture scientific losses.
No point, root solve, native build or actual three-point instance has
run at preparation. Independent source review remains required.

Pure-test invocation (no native/API activity):

    python3 topics/padua-argmax-bridge-20261105/code/post_audit_D09_threepoint/controller.py --pure-test

It tests synthetic exact dyadic endpoint recovery, NaN rejection, normalized
pi^4 arithmetic with fake losses, fallback-side coverage and completion
ledger ordering. It creates its own exclusive preparation registration
and reports CPU. It never evaluates an actual three-point instance.
