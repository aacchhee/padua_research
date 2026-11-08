# Supplementary independent review of the onset-512 response

Rules/input: `b45e29fa1fe3dbfa2517ff8043e5d9c440870530`, read 2026-11-08.
Role: distinct supplementary Codex reviewer; requested Astra xhigh because the
scope includes adversarial arithmetic and a new independent checker. Actual
serving model/effort metadata are not exposed. Root alone owns Git. This is
not the required substantive Claude audit and does not make PR 27 ready.

## Scope and prospective checks

Review only: the local frozen-engine 320..510 campaign and compact return;
J01/J02 analytic gates and elementary constants; I25's independent phase
checker and its prospective pilot/full-run protocols; the F03 support split
and both H04 derivative majorants. Historical audits and findings remain
unchanged. No native certificate computation is authorized by this report.

Read AGENTS, WORKFLOW, CODEX, handoff 29 including AC's dated decisions,
audit-03, the streamline architecture, I25 and its closest verification
predecessor IDEA-344, the complete IDEA registry (including its obstruction
and disposition tables), and the relevant paper formulas. This implements
approved I25 and architecture B; no new mechanism or novelty claim is made.

Before execution, the following cheap independent checks are registered here:

1. Run the registered Fraction-only J01/J02 checker once at source SHA-256
   `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751`,
   saving independent stdout/stderr/exit and source identity under
   `/tmp/onset512-independent-review/`. Reconstruct its all-real-n steps,
   elementary constant brackets and exact rational consequences separately.
2. Run only synthetic scalar, interval and cover checks of I25: compare its
   sine intervals at fixed rational angles with independently constructed
   rational Machin/Taylor enclosures; test exact interval operations,
   removable ratios, and degenerate/closed polygon examples. No complete
   degree certificate is included in this independent smoke scope. Preserve
   all failures; do not alter developer sources.
3. Re-run process controls using the registered local runner's `controls`
   action in an exclusive scratch directory; this invokes no native engine.
   After the compact ZIP is complete, independently check its content hashes,
   exact population, primary/fresh equality, exits and accounting, then run
   the frozen data-only verifier. Any extra controls modify scratch copies.

Computations and proof adoption remain provisional until the corresponding
review below is complete. Source inspection, developer-reported execution,
and this reviewer's actual execution are distinguished throughout.

## Initial observations (before independent executions)

- The campaign runner's 260-second `RLIMIT_CPU` bounds wrapper self CPU,
  not the aggregate CPU of descendants. The unchanged engine separately
  enforces each pass's 120-second aggregate budget. The developer clarified
  this wording; no native computation needs repeating for that clarification.
- The preregistration records the validator identity but the runner does not
  enforce it at stage entry, and does not prospectively pin every imported
  operational helper. Root confirms the helpers were not edited during this
  epoch. The developer's during-run helper snapshot is explicitly supplemental
  evidence, not a retrospective preregistration.
- I25 reconstructs its own upper and lower bounds and recertifies the entire
  stored tree. The weaker comparisons `lo <= native_upper` are diagnostic
  consistency checks only; they do not validate the original native endpoints.
- Both H04 derivative majorants are valid. The former coefficient ordering
  is stronger. Replacing it by the requested ordering is not a repair of an
  invalid mathematical inequality.

## Results

### Analytic gates and elementary constants — accepted at the written scope

Reviewed frozen J01 SHA-256
`a74be3cfb90b03f24325c09c737166e17fced17d4ec7c5fd9a2f185d5923ce56`,
J02 `d4fc185afc308fc7363e3c82919f85a94e10215c997578ce807b31dae774c0ac`,
and checker `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751`.
The exact command was `python3 topics/padua-argmax-bridge-20261105/code/onset512_analytic/check.py`
(the subprocess used that path resolved under the repository root). It ran
once independently, observed exit 0, Python 3.12.14, about 0.23 seconds wall.
Own output is `/tmp/onset512-independent-review/analytic.stdout`, SHA-256
`8ec242fede846448e4063f1d2d545b4d5192e55f7e917113542141f2f6424c55`;
stderr is empty; `analytic-observation.json` records command and identity.

| Exact outward receipt | Lower | Upper |
|---|---:|---:|
| maximum P512 | 0.040785 | 0.040786 |
| P512(1/2) | -0.143070 | -0.143069 |
| vertex radius | 0.147341 | 0.147342 |
| G(512,1) | 0.534264 | 0.534265 |
| lower surrogate for G(192,pi/2) | 0.098316 | 0.098317 |
| middle-class floor at 295 | 0.050064 | 0.050065 |
| kappa, K=3 | 0.917166 | 0.921489 |
| Cstar | 1.841232 | 1.847940 |

The proof review is separate from these finite evaluations. The decreasing
allowances and increasing T+A4 imply increasing U,d1,d2. Formula (4)
proves the unrestricted maximum and vertex decrease. For P(1/2), the
optimizer remains in the fixed nonnegative segment; pointwise decrease
there, with the uniform positive drop in C4, proves strict decrease of
the maximum. This covers every real n>=512, not a sampled integer grid.
The absolute-gate amplitude decreases in radius under the stated tangent
condition; its coefficient ratio decreases with n. Each term in G has the
claimed sign of n-variation. The floor has positive inverse-power losses
and therefore increases; its remaining two center classes are the unchanged
finite proofs. The closed half-radius, radius-one and far boundaries overlap.
Corner-256 retains the pi/4 square and 1/30 loss; far-192 retains its pi/2
guard and 3/100 gap. Finite coverage through 511 remains a separate obligation.

I reconstructed the endpoint cancellation, positive ap formula and geometric
ck tail, including radius 1/480 at K=3. Machin's identity, consecutive
arctangent sums, the positive atanh logarithm series, harmonic gamma bounds,
and convex trapezoid/midpoint zeta tails supply every scalar bracket. Even
zeta special values, Arb constants and numerical quadrature are absent.
Independent rational cross-multiplications give H0's extra margin
37/19700 above 7/25, g0's margin 7/24625 below 43/125, and the final
squared C_infinity gap 71/6250000. Thus j>23/250 and C_infinity<9/4
follow without an upper kappa<23/25 premise. No unresolved finding remains
in J01/J02; root may adopt PROVED at these stated scopes. This acceptance
does not adopt the new finite computation or remove the next Claude audit.

### F03 source split and H04 majorants — accepted focused response

The new supporting F03 file has SHA-256
`fbdeed2ef9ca419c84b3ba4ee99cd9832369998829b81356864edd227baf7efa`.
A read-only comparison against `git show b45e29fa1fe3dbfa2517ff8043e5d9c440870530:topics/padua-argmax-bridge-20261105/theory/F03-origin-sign.md`
confirms sections 1--3 are verbatim. H01/H04/H05/H06/H-sharp now identify
that PROVED support and its PD-T159/PD-T226 normalization. H05 distinguishes
its abstract series estimate from the corner identification. The original
sign/useful-lower target and proposed one-index evaluator remain OPEN;
neither becomes an H premise. This is an appropriate substantive split.

For H04 (reviewed SHA-256
`cd8a9462b0a3afe3a38dc324e82756ff5a5e39bd869c45e24cc7690c704e4b05`),
direct differentiation of f_k=t^2/(4k^2-t^2) gives

    f_k''=8k^2/(4k^2-t^2)^2+32k^2*t^2/(4k^2-t^2)^3.

Bounding those summands separately gives the historical coefficient ordering.
Bounding its combined numerator gives the requested new ordering. The new
summand exceeds the old one by `(4/27)(k^-2-k^-4)>=0` inside the common
8/pi factor. With the stated crude series bounds the old majorant is
<1088/243<5 and the new one is <128/27<5. Both are mathematically valid;
the historical inequality must not be labeled false. The new addendum
preserves that distinction and all downstream constants. Own exact results
are in `/tmp/onset512-independent-review/exact-support-checks.json`.

One preliminary text-comparison command failed because I assumed a different
heading depth and H06 filename; it made no scientific calculation or source
change. After inspecting the actual headings/path, the corrected comparison
above passed. No developer failure is inferred from that reviewer mistake.

### I25 — initial pilot gate and arithmetic review

The I25 **pilot gate is accepted**, before any consequential pilot launch, for
core `add4f1cb1246e71fd38f67b802a4e61dfb8ebe9244dda49326290b779030d485`,
controls `628096010388fb3a1860726092e91156e98e17f1c35055bbe31990d7a14af5ac`,
runner `0ad0021a40253a78935663af7aff6f548b986919acc0f50e45767097d800c019`,
J03 `008b7fe2fd4674d6b6471671b487e8fb14411de156861c83e4bfa2d15a85b20e`,
and preregistration
`e1fa7ab9788b0ebde8847ec12755444b8452d5f064a0e5bf6c2faf9ae7844398`
plus prospective amendment 01
`6cefeb23852752cb6ee74735f8a9056bc275448850afcd009c21aaf43a7aba03`.
The amendment supplies the originally missing outer wall timeout and runtime
identity; it changes no checker source or scientific population. The total
pilot cap is 3600 CPU seconds, with 3500 for its process and 100 for smoke
work. Both passes at exactly 41,199,238,511 and all 27 corruptions are required.

I independently reconstructed the finite diamond-to-product kernel identity,
both coordinate endpoint weights, four-reflection addition before absolute
value, exact collision parity, and Python-int guards before int64 operations.
For Taylor sine, each monomial has at most 38 rounding/conversion factors;
the coefficient majorant gives <77u*t, the remainder <u*t and argument
reduction <6u*t. The implemented 128u*t therefore encloses the exact result
under J03's explicit binary64 round-to-nearest/gradual-underflow model.
Nextafter-widened general operations and explicit pairwise sums preserve
inclusion. This is conditional on the stated computational semantics, not
an assertion that hardware arithmetic is exact.

The parser retains both closed children, exact tangencies and every
required folded key. Independent GRID/TREE norms bound every signed family.
The rational polygon routine includes all vertices, every true edge's
stationary maximum and nonsingular interior stationary points; a singular
interior maximum has a flat direction reaching the boundary. Near/far proxies
overlap at the physical seam. The actual three corner points and analytic
256/192 guards are reconstructed exactly. Stored endpoint comparisons are
only consistency diagnostics; each tree is recertified using the new bounds.
Native endpoint containment is expressly not claimed.

Own command `python3 -B /tmp/onset512-independent-review/scalar_controls.py`
passed **98** synthetic controls in about 5 CPU seconds. Outputs and both test
versions remain in that directory. Coverage includes independent exact
Machin/Taylor sine enclosures at 54 rational arguments (negative turns,
half-pi, tiny angles and denominators near 2^51), removable ratios, signed
pairwise sums, basic interval operations including subnormals, a singular
Hessian, a point intersection, malformed prefix covers and four closed
quarters. No complete certificate or native engine was run. The first test
version incorrectly demanded enclosure of its own overwide Taylor upper
above 1 at pi/2; intersecting that reference with the known [0,1] range fixed
the test. The initial failure and script are retained; checker bytes never
changed. This was a reviewer-test defect, not a hidden certificate retry.

At this initial gate the full run still needed a separate preregistration and exact 942-input
inventory; the pilot runner's initial additional-directory interface alone
does not enforce that scope. Pilot outcome and full-run acceptance were
pending. Legacy PD-T271 strings inside frozen certificate metadata are schema
identities; J02 can replace their analytic numerical premise without editing
the historical certificate bytes. This distinction must remain explicit.

The campaign's cheap process controls were independently executed with
`runner.py controls /tmp/onset512-independent-review/process-controls`:
observed exit 7 stayed 7, an already reaped child was refused, inherited
ignored SIGCHLD was refused, and cleanup left no descendants. The control
record hash is `ccb80d7fb80f679801bb8ba864ce768ea519bc41c822073393d031856cc4efde`.
The real campaign and compact ZIP were pending at that boundary.

### I25 — preserved v1 failure, prospective v2 correction and accepted pilot

The first pilot stopped at n=41 before any numeric S evaluation: the checker
required 66 keys while the certificate retained 64. Its missing seam points
were (3/4,1/4) and (1,0); the exact antipodal partners were present. My
independent data-only diagnosis confirmed this. The observed exit was 1,
about 0.684 CPU seconds. The failed output and observation remain at
`local-output/argmax-bridge-20261105/i25-pilot-v1-20261108T105100Z*`;
the observation hash is
`ee84df55ca1b599c493c7b4dbaefe3060c45848b7ed3ce78d0dda80037fee2da`.
The earlier gate acceptance did not predict that compatibility failure.

Prospective amendment 02,
`2d736f83ed3f9abe17307b5c0b1720e96e7bf188d5ccb3457bada1ab5d8b8dda`,
canonically reflects the closed seam when a>b, consistently in the required
keys, GRID and lookups. This uses the paper's exact antipodal identity.
All required keys must occur; any extra retained key must lie in the triangle
and is independently evaluated. No region, guard or arithmetic bound is
weakened. Frozen v2 core is
`f2d3a1e91c13f4015819a661c5cec81852e63b5e307803613353191bd84f6fa3`,
controls `c1810bd1dc6ddcbb3501c0589f099c89fa50fd6bd2e79b77f06030d8cc114bd1`,
and the pilot runner remains `0ad0021a40253a78935663af7aff6f548b986919acc0f50e45767097d800c019`.
Core length is 255 lines; all three Python files total exactly 400 lines.
Own 15 exact seam controls passed, including both directions, idempotence,
the midpoint and lexicographic representative. I accepted this focused gate
before v2 launch. Its 3400 CPU-second limit preserves the original total
3600 allowance including the failed attempt and smoke work.

V2 then passed all eight registered certificates, all 31 arithmetic controls
and all 27 certificate corruptions. I independently checked the exact eight
input byte identities against the historical tar, all recorded output hashes,
the n/pass population, positive rational margins and observed exit 0.
Inclusive CPU was 21.010049836 seconds, wall 21.031955808, peak RSS
144084 KiB. Observation hash:
`2de69f5d4b9e53541618630ea5c9b16222737c1eaffcf5f11ac8466ca24a961f`.
Own record check is `/tmp/onset512-independent-review/pilot-v2-record-check.json`,
hash `76a96ca9949d04abed9814f79440dfcf2debf47290c8067bb8205ac5c9a33e5e`.
This is inspection of the developer's actual pilot records, not a second
independent certificate run. My own execution remains the synthetic checks.

The pilot is accepted as substituted-bound recertification of the complete
closed trees. The implication `new upper <= stored upper` proves 63/64 original S upper
bounds at 41 and 44/45 at each other pilot degree. This is a bound comparison,
not containment of the stored endpoint in the new interval. A universal native
endpoint validation is therefore expressly **not** established. The implication
`stored lower <= new lower` proves the original lower bound in each pilot. The full 942-certificate outcome remains separate.

### Local native campaign and compact return — accepted at recorded scope

The completed population is exactly n=320..510, each with a primary and
fresh verification pass: 191 pairs, 382 successful passes, no failed or
unstarted case. All observed exits are 0; stage and attempt ECHILD/cleanup
records are quiescent. The preregistration hash is
`532e5af6af478d48546b4134635c296cd0aac5207de4df2955dda8b0fb7781a3`;
runner `459d0728a0cb264d241bc76d270209842fc2aa55c0fadd32e23f8e3b0523af9e`
and engine FREEZE `0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb`
are unchanged. Own `campaign_accounting.py` checked all degree/pass records,
registered pins, helper snapshots against the input Git bytes, summary rows
against observed wrapper records, raw/receipt links, strict margins and the
complete primary/fresh equality fields. The verified certificate's original
input bytes equal the primary certificate. No native process was rerun.

Inclusive wrapper CPU sums to 2825.091458 seconds; pass child CPU sums to
2700.875169 seconds. The largest pass used 9.003991 seconds and maximum
wrapper RSS was 112688 KiB. Every pass has completed accounting, no first
failure, hard aggregate cap 120, and the final self-plus-waited-child limit
at most 119. All trees have 51 nodes. The smallest stored strict margin is
`232344484034217493/58629478430225203200`.
Own accounting receipt hash is
`5b4053140771cff7d4c54f8590cdfa231236e4712c0e0237ba4ea9c5caf969bb`.
The helper snapshot remains supplemental observation, as disclosed above;
the verified unchanged input bytes and root's no-edit epoch statement do not
turn it into a retrospective preregistration.

The canonical ZIP is
`local-output/argmax-bridge-20261105/onset512-return-20261108.zip`,
81602992 bytes, SHA-256
`da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e`.
Exporter/verifier source hash is
`d1dba2340e06f8750628ef129ce52f604b09e704a085f4f63c9d190c46c129d3`.
Its 11713 members contain all 382 essential proofs and every small history.
The once-persisted post-completion seed
`cb52b5324c8fa5bca69665affe22016950ca48661a429a3fa4b6e4a77bfadcdb`
reproduces sample [475,458]; both carry complete native dependency closures.
This is a transport/review sample, not statistical evidence. Other full
histories remain in the local campaign directory. Trusted source/runtime
files are authenticated separately, never by executable archive contents.

My actual command `python3 -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/return_bundle.py verify local-output/argmax-bridge-20261105/onset512-return-20261108.zip`
observed exit 0 and empty stderr, with 191 pairs/382 proofs and both closures
accepted. Output is `/tmp/onset512-independent-review/compact-verify.stdout`.
The developer separately reports a successful relocated trusted-root run;
I did not repeat that portability run. My own independent inventory/hash
check confirmed the exact population, payload hashes and sample membership.
Twelve mutated in-memory byte payloads through the same data-only verifier
were all rejected: checksum, duplicate/absolute/parent names, an omitted
certificate, wrong degree, incomplete tree, nonzero exit, altered budget,
helper pin, summary row and missing sampled native closure. These controls
use a synthetic ZIP-reader adapter; the positive archive check above uses
the actual ZIP parser. No archive code was executed. Receipt:
`/tmp/onset512-independent-review/archive-controls.json`, hash
`4e93f44d3c0b2bf0430c70f137758a859d3b32969cb92d16bc3bbd07db847a7b`.

The additional certificate-only ZIP, 945235 bytes, hash
`c22d600cb67462918587b01f2ef5adcbf9030b825fb0f2cc79c1b9c27c7da8c8`,
contains 382 certificates independently checked byte-equal to the canonical
return. It is a convenience derivative, not a replacement for the evidence
closure. Two first versions of my record-reading checks failed on assumed
filename/null encodings; corrected readers use the actual `n320-produce.json`
name and the string `None` for an analytic corner. Those reader
failures are retained in scratch and caused no scientific retry or source edit.

This review accepts the new finite campaign and return under the unchanged
native evaluator trust boundary. The separate I25 full run can replace that
numerical dependency for its accepted inputs; it does not erase the historical
native process record or the required later substantive audit.

### I25 — full 942-input gate accepted before launch

Preregistration `9e4da4615cc40c7e23f8061a560e2f3fd8e696d13c64db3f0249ebb489e9cb4a`
and prospective amendment `228fd0230efd1e76661d02c03d886b5dbf80d41df844b3e2ffd7346a90c73f18`
were reviewed before launch. Frozen core:
`1501ce9435a17e9cc4b0954f3ce90f47450252d58027e08468ce905528fdc8be`;
runner `c55b77d2ea79bfa7ada07ac95ab10e439fcbf6e1245c7f25d64a7d43be24ca78`;
launcher `8779ab2a6632143aac8038f07c4e11483aecacd23e1dd1ab8a85028d7f1e9596`;
controls unchanged from v2. Independently comparing the accepted pilot commit
4846913 confirms exact nonblank-byte identity of the core: only nine blank
lines were removed. The three checker/driver/control files total 400 lines;
the separate 53-line launcher contains orchestration only.

The runner authenticates the historical tar, exact 560 old pairs, the new
382-entry inventory `d7cea34dd64d9df329d1398c2418fbf984a9084b135cad695866a9c437551740`,
regular filenames and every new content hash. It requires the complete raw
942 n/pass set before filtering. My separate data check verified all 382
mirror bytes against the accepted canonical ZIP. Four deterministic disjoint
groups have 118,118,118,117 degrees; their union is every integer 41..511.
Each degree keeps both passes together, with a fresh process per worker and
no persisted cache. Failure terminates remaining process groups; no further
admission, retry or altered thresholds is authorized.

I identified that the original source-bound calculation 4*2671+80 omitted
the four GNU timeout processes. Amendment 01, accepted by root and reviewed
before launch, corrects the claim: 10800 CPU seconds is a measured total
campaign budget/acceptance threshold, not a kernel aggregate cap. Worker
2670/2671-second CPU and 2-GiB address limits, supervisor soft80, worker
7200-second wall and outer7350-second wall limits are separately enforced.
Inclusive final accounting includes waited timeout/worker CPU; an excess is
failure, with preserved outputs. This clarification changes no source or
scientific acceptance predicate. Full execution remains **pending** here.

### Audit-03 E-01–E-04 — focused operational repair accepted

Root added this focused scope after the native campaign became quiescent.
I reviewed the diff from the input SHA, the reused admission/history helpers,
and [the developer's response](compact-verifier-audit03-response.md).
Candidate `compact_pack/verify_compact.py` has SHA-256
`5867ac0c6d6e1d380d72c118262177a10b617631e039da11f489e45c93ff61b6`;
control script `a256cb9abc0e0610b36880aa5eed09e3c5b90c8e9ab518cd406982ce9a8017d3`.

The reader authenticates the separate trusted package before loading checker
code; returned names cannot shadow its files. Ledger/history validation,
summary/status/freeze/receipt and server-attempt/raw-hash links are now checked.
Fresh tree, key sets and norm method must agree while independently recomputed
numeric endpoints may differ. `--expect-plan all` enforces the entire original
280-degree plan; default completed-subset verification remains explicit.
The unchanged 24-GiB logical cap is checked before each regular payload read
or hardlink alias addition. It is an early total limit, not a low-memory claim.
Unsampled absent raw histories remain server-recorded identities; the reader
does not claim to hash their absent bytes.

I independently executed both exact commands in the developer response,
using the actual old tar and complete separately trusted package, with a fresh
control output `/tmp/onset512-independent-review/e01-e04-controls.json`.
The direct `--expect-plan all` run observed exit 0, 5.192408 CPU seconds,
280 pairs/560 rational proofs and complete sampled closures 199,238. The
control run observed exit 0, 13.108591 inclusive child CPU seconds; all 30
controls passed, including rehashed semantic corruptions, subset/full-plan
separation and early size rejection before the second payload read.
Both stderr files are empty. Own control receipt SHA-256:
`7400d4f930886f73c3e031b4ed5bf59f32456bdb055c199ce503dd1c0affda85`.
Own commands/exits/resources are in `e01-e04-*-observation.json` in that scratch
directory. No missing-file adapter, archive executable, compiler or native
calculation was used. Imported helper bytes match the historical release.

E-01–E-04 may be closed for this source-tree candidate. The old trusted
package still authenticates its old verifier; this review does not relabel
new code as historically used or repin that package. Any later operational
release needs its own current source identity. Historical audit findings and
the separate new-mathematics/independent-arithmetic audit obligation remain.

### E-10 — focused custody-index/deposit preparation check

The small custody index and deposit template are accepted as local preparation,
with external delivery still pending. My own readback verifies all ten populated
deposit-file identities and all four pending-local rows. The historical
23904-byte manifest matches its exact b45e29f Git blob and SHA, so the full
70-row historical inventory remains recoverable without committing another
bulk copy. The inspected active index is 3050 bytes, with empty delivered
`entries` and `total_bytes: 0`. `python3 -B tools/cold_storage.py verify padua-argmax-bridge-20261105`
actually exited 0; with no delivered entries that establishes only compatible
index/source metadata. Own details are in
`/tmp/onset512-independent-review/custody-check.json`.

No Windows delivery, upload, DOI reservation or remote retrieval was performed
or inferred. Three final source/I25 deposit artifacts remain explicit placeholders.
The derivative certificate ZIP remains distinct from the canonical provenance
ZIP. I notified root of stale draft pilot-v1/pending-review wording for update
with the accepted pilot and current reviews; it does not change verified bytes
or custody. The size/index part of E-10 is addressed; durable data access still
awaits AC's actual deposit and independent retrieval.

### Prospective independent six-certificate replay

After the above checks, root explicitly extended this review to one independent
complete-cover execution of both passes at 41,458,511, after the frozen full
campaign finishes. This adds the numerical-corner/TREE branch, a selected new
campaign degree and the largest degree. It is not a statistical validation
of untested inputs. Before execution I registered exact source/input hashes,
the fresh output `local-output/argmax-bridge-20261105/i25-independent-six-20261108T111930Z`,
and the command in `/tmp/onset512-independent-review/six-preregistration.json`,
SHA-256 `14c096c0fb10d8400c9dbb4a69d22cc84a81fbe348e8d595a07403f96d5d50c8`.
The frozen from-paper runner receives `--degrees 41,458,511 --cpu-limit 290`;
its existing exact old560/new382 inventory checks run before filtering.

The total allowance is 300 CPU seconds and 600 seconds wall. Child CPU is
290 soft/291 hard, reviewer wrapper CPU is 5 soft/6 hard, child address space
2 GiB, and the external observer kills the process group at 590 seconds.
Observed `wait4` status and child usage are required, with default SIGCHLD;
source pins are checked before and after. A fresh interpreter carries no
pilot/full-run cache; exact within-degree primary/fresh reuse remains explicit.
No native engine, compiler, Syvert call, retry or scientific source change is
permitted. All six exact inputs, the automatic 31 arithmetic controls, exit 0
and resource bounds are required. Outcome is **pending** at registration.

### I25 — completed full outcome and actual independent replay accepted

The frozen full campaign completed exactly 942 certificates: both passes for
every n=41..511, with no failure or retry. My own `full_records.py` checked
all 942 input hashes against the historical tar/new mirror, all 25 manifested
output identities, four disjoint assignments and observed worker exits 0,
unchanged source hashes, 31 arithmetic controls per worker, empty worker
stderr and every recorded positive rational margin. Inclusive CPU is
2519.420775278 seconds, wall 646.839168173, maximum child RSS 154176 KiB.
The parent separately observed the outer command exit 0. Full-summary hash:
`46944f9ae15f344bbf5d38c1cf8c2d3b20ca1e24ee4b5b708d3c2976255a7bff`;
outer-observation hash:
`791a460b6238f68939393baf1071cee4d6f8f10f54ce92df0e80b31c1a8382e2`.
Own exact minima and checks are in
`/tmp/onset512-independent-review/full-record-check.json`.
The least near margin is approximately 0.00578243477 at 42; far margin
0.16511789590 and actual-corner gap 31.803121593 occur at 41. These
are the independent checker's recomputed predicates, not copied native margins.

The separate six-certificate replay above then actually ran once under its
prospective registration. Command:
`python3 -B /tmp/onset512-independent-review/six_runner.py 14c096c0fb10d8400c9dbb4a69d22cc84a81fbe348e8d595a07403f96d5d50c8`.
Direct `wait4` observed child exit 0, no timeout, 27.276321227 inclusive CPU
seconds, 27.240665118 seconds wall and 152000 KiB maximum child RSS.
All six complete closed-tree checks and 31 automatic arithmetic controls
passed. Every mathematical result field equals the corresponding full-run
field; timings alone differ. The exact six inputs, source pins before/after,
Python/NumPy runtime and fresh output identities match the preregistration.
The reviewer wrapper itself also exited 0 with empty stderr. This is an
actual independent execution of the reviewed second checker, not another
independent implementation or a statistical claim about the other inputs.

The independent-six observation SHA-256 is
`bd7d08e97139d78c1b699a6212508e4229a78793971fcc4198588432333ab970`;
summary `2773d1894faefb305273e1420f0cefdec900eb37b9aba09c70d49dd0ef32c92f`;
append-only result log
`1b0f18c8565290903bbd5587cbea1667e51436739650cfb139e2abfe004b51f0`.
Own post-run comparison is `six-record-check.json` in the scratch review folder.
No native engine, compiler, library-trigonometric evaluation or Syvert call ran.

The full outcome is **accepted** as recertification of all 942 complete closed
trees with independently constructed numerical bounds. This replaces the old
native-evaluator numerical premises for that finite range, under J03's explicit
IEEE/NumPy/exact-rational model and the separately named analytic lemmas.
It preserves the native computation as historical evidence. Exactly 42174 of
43116 original S upper bounds satisfy `new upper <= stored upper`; all 942
original origin lower bounds satisfy `stored lower <= new lower`. The 942
remaining original S upper bounds are not validated by the weaker consistency
test. Their new upper bounds nevertheless prove the full strict trees, which
is the accepted alternative. No universal validation of original endpoints,
new analytic lemma, general checker range beyond 41..511, completed external
deposit or completed substantive Claude audit is claimed.

The computational review scripts, outputs, preserved reviewer-test failures and
actual independent-six records are retained together off Git in
`local-output/argmax-bridge-20261105/onset512-independent-review-20261108.zip`:
51749 bytes, SHA-256
`96f84b294b724b74bc33c112a2633bde14fed5c9220cb11196c60dae5c12ab28`.
Its 50 payload files and inventory passed complete ZIP readback. This is a
small supplementary review bundle; canonical production/full-I25 evidence and
trusted source remain separate. Original local outputs were preserved, and
no external delivery or deposit is implied.

### Focused manuscript mathematical integration — accepted at these bytes

I compared the new elementary-constant and analytic-gate arguments in both
manuscripts with the reviewed J01/J02 proofs, and the new finite-verification
interface with J03 and the actual accepted runs. Reviewed section hashes:

| Section | Paper SHA-256 | Companion SHA-256 |
|---|---|---|
| comparison-unified.tex | `0e22315ead9e83b75dc89fb7353089022086be91036c66bf18dffe938cefc234` | `ca7736cfa25879c4198cebd5496be62dcf55be163b41757dc8a34f27c19fa1a6` |
| localization-unified.tex | `56f49bdffc85fe209f1c24f461d3595f948478a1e81052b5602e84a03a07ef86` | `16557b9db159ca5887db7badcf4169f6b439e5e5e7440b0cfb6bec2ae7b85868` |
| certification-unified.tex | `74d079d655debb2c59ea8a15b5050c26b782b5fa5ed2ccb8340463ddea6c1c1b` | `ec0813dfe54c7948c14ee05b3d636fe60470bfd100e580ce2174928fac629789` |

The endpoint-cancelled K=3 coefficient series, elementary pi/log/gamma/zeta
brackets and 1/480 tail reproduce the accepted constants. The all-real-degree
argument retains the increasing T+A4 step and the fixed positive optimizer
segment needed for P_n(1/2). The increasing 295 half-radius floor, retained
192 far/256 corner guards and closed seams give the advertised onset512 with
the finite bridge ending at511. No former native constant-enclosure premise
is reintroduced. The constant identity uses the separately proved absolute
finite error without its later model-loss constants, avoiding circularity.

The finite section now uses direct finite kernel/cardinal sums, addition of
four reflections before absolute value, exact weights/collisions, its own
vertex bounds/origin lower/norm and every closed-tree predicate. It states
IEEE round-to-nearest, gradual underflow, correct nextafter and the exact
Python/NumPy/rational interface. Selected-pair floors and the analytic branches
remain mathematical premises. The old Arb implementation is correctly
historical search evidence. The 942/471 counts and six independent replays
match actual records. No numerical or mathematical mismatch remains in this
focused integration. Root must associate these bytes with its final source
freeze; later substantive changes require their own focused review. Build,
layout, paired-numbering and general presentation acceptance are separate.
