# D36 independent fresh degree-1023 result review

2026-11-06. Distinct mathematical/source/result reviewer. Requested Astra
high; actual serving model/effort metadata is unexposed. This report records
one independently released fresh verification, not a second production run.

## Direct completion observation (persisted before further review)

Root published the prospective registration at
`4d94c0b545da8c0e9c5e9af02f92c7940c30f07a` and explicitly released its exact
command once. The reviewer executed from `/workspace/padua_research`:

```
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D36_engine/engine.py --mode verify --n 1023 --certificate local-output/argmax-bridge-20261105/post-audit-D36/pilot1023/essential-receipt.json --output local-output/argmax-bridge-20261105/post-audit-D36/fresh1023 --run-once
```

Direct tool observation: initial exec chunk `c22b51`, session `95825`;
intermediate chunks `9fb213` and `457b79`; final `write_stdin` chunk
`c3f838` returned **exit_code=0**. This is the fresh outer process's directly
observed EXIT0, distinct from a worker returncode in an evidence file.
No retry, changed command, extra degree, separate controls invocation or
source/cap/precision/norm-method rescue occurred.

The separately read fresh `final-accounting.json` states
`FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW`, `complete=true`,
`first_failure=null`, CPU checkpoint `29.746529`. It records no live
children, fixed waited-child CPU `29.015777`, and absolute self CPU hard
limit `89`; therefore post-accounting serialization/write/return remain
within `29.015777+89<120` CPU seconds. The checkpoint is not misrepresented
as an exact final CPU measurement.

Fresh evidence in
`local-output/argmax-bridge-20261105/post-audit-D36/fresh1023/`:

| File | Bytes | SHA256 |
|---|---:|---|
| essential-receipt.json | 4948 | 5dcf41c0425b2a094ef8ae287f5038741ae06fd73359451a6b567f2e36f299e8 |
| final-accounting.json | 1468 | 3077a946b48acc860b4470c1c151c60e12738a29d17c83c9c9182ce9290b6c73 |
| raw-evidence.json | 153117 | 4621f68fbf7f8f0bd37e31bd81041bec0ee3c925b8569f37142cdef8fa2c30b3 |

The primary outer tool session/EXIT0 was lost to compaction and remains
unavailable. Primary persisted completion and its worker returncode0 do
not replace that missing observation. The primary essential receipt is
treated only as a candidate tree, retained keys and TREE norm method.
The fresh verification supplies its own numerical premises and completion.

## Registration, source, and candidate status

Prospective `code/post_audit_D36_result_review/SPEC.md`: 5568 B,
SHA256 `005935462289d237a910192da92c2a3f7af1bfc47f891ddd7ff4f0badbe26b5f`.
`INPUTS.sha256`: 2834 B,
SHA256 `6bd7f4ac81eeedf1af87bb6c1499a304fcf4d8e63cfa1520c93f507ae9d4e9a0`.
The prose hash is audit identification, not a machine scientific acceptance
condition. Source and numerical input identities are execution gates.
Read-only post-run `sha256sum -c` confirmed all registered source/data
identities, including the unchanged candidate, original primary raw,
primary account and worker-supervisor record. `cmp` confirmed the fresh
`original-certificate.json` preserves the candidate bytes exactly.

Accepted corrected D36 source was published at
`7975a0c84bc581fc2ccbc5a16fa6da96beb1cde9`. Its 7073 B FREEZE SHA256 is
`d74817158e9a08de67a89e2c790ea1e39b5729fc17c0df002b5b15564b5b2001`.
The distinct source/domain audit is `independent-checks-D36-engine-source.md`,
SHA256 `5296e003ef8127318a83342dcb25216b363169f9b345597814553998ed8841df`.
That report preserves the first rejected fixture and closes its single
fixture-only correction; production mathematics and resource limits were
unchanged. No repair followed this fresh invocation.

The 4958 B primary candidate SHA256 is
`bc003a7836ade524f56065d13dfdb268a16c01d41ace7edb674071b8f6ddce60`.
Its primary raw SHA256 is
`a8da7ad9c14c0ee9d149e10a77d3d7201c0b4f2d78983b73fca4a5c9ef029ad8`;
primary account SHA256 is
`dc2fcadad4511eb177d403b380d27d99812f5747e30d9e6e932d578415469e0d`.
Those files record CPU checkpoint30.182919, completion and child return0,
but cannot establish the missing primary outer observation. I do not
upgrade that primary execution to fully observed completion.

This limitation does not defeat the independent finite proof. Inspection
of unchanged `engine.py` and `checker.py` confirms that verify parses the
candidate's strict schema, degree, complete closed tree, canonical point
keys and chosen norm METHOD; it starts a new cache and freshly builds both
native libraries. Every retained numerical premise is obtained again.
Old M, L, vertex/actual uppers and verification numbers are diagnostic:
they neither supply fresh bounds nor determine a fresh mathematical pass.
The fresh TREE norm and every leaf and actual-corner inequality are
reconstructed and the new essential receipt is checked from its own
retained endpoints. Thus candidate generation can be incomplete or
untrusted without compromising this separately completed verification.
This is an independent execution and distinct source/domain review of the
accepted common checker, not a claim of independently implemented code.

## Native evidence and coverage

Both fresh builds use g++14.2.0 and separately retained translation units
and binaries in exclusive directories. The S source snapshot is6550 B,
SHA256 `6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9`;
its binary is95064 B,
`193b9e7a4dc124f462ca3e5c965044eaa6d604fb622d3231e6a13bfb7e30be99`.
The actual D07 source snapshot is9698 B,
`03dc79bbbc7563ba9066137c0a52467624c810a758f865f9931511c82985ff6f`;
its binary is162968 B,
`bbd5900ed3b5c310cfccaad695cf0d32b4a657b4eba02ae41520f6959d6f7f70`.
Their translation-unit hashes are respectively
`f3ad2f0c741e02f89e5106e8ed53b02da6081c82bffd3c71ac3f7f4c083aeb21` and
`c25f8454a7bbdaa3ee211f6efb227c4473f1f68adc12369902ffb54cd6c6437b`.
Full compiler/header/dependency identities and command lines are retained
inside the whole raw record. Both libraries were mapped from these fresh
build directories. Before/after loaded dependency and all-file mapping
identity lists agree; unchanged runtime also rechecks build artifacts,
headers, toolchain closure, dependencies and Python identity on close.

The fresh checkpoint has exactly47 S calls plus3 actual calls, all n1023,
all native returncodes0, no active unfinished call and no unused S call:
retained_S_count=total_unique_S_calls=47. Origin is included. The strict
keyset matches all final-tree mathematical vertices. No producer discovery,
refinement or alternative norm attempt occurs in verify. Read-only record
comparison found each fresh call's complete native returncode/hex triple/
counters and exact lower/upper/radius record identical to its unique
matching primary call. This agreement is corroboration, not a proof gate.
Timing fields are not required to match.

The S endpoint (0,1) legitimately has value1 and six zero counters. Other
S calls satisfy the source's n1023 closure4n=4092 and2(n+1)-4=2044 with
the unchanged direct/block guards. Actual calls report n+2=1025 rows and
the original13-counter guards. Physical actual keys are precisely
(1/4092,0), (0,3/16384), (1/4092,3/16384). No D07 guard is expanded:
1023<1024 and1023<=2048. The analytic D27 branch is not used here.

The unchanged included S producer uses its rigorous C23/D23 tail, with
J2,K8,LH4,WD16, and the separate actual library retains its original
arithmetic. This review relies on the accepted inclusion proof and recorded
Arb/FLINT/MPFR/GMP/compiler/runtime implementation; endpoint bit agreement
alone would not prove inclusion. No empirical error estimate or a bound
outside its stated degree domain is substituted for that theorem.

The corrected fixed synthetic controls passed in the released engine stage
with no native call. Controls CPU0.049526 and checker CPU29.63932 include
supervision. The complete whole raw153117 B record retains all calls,
radii, counters, caches, tree/norm/corner state, build manifests, runtime
maps, original candidate, controls and stage results without trimming or
splitting. Fresh essential4948 B is strictly below16 KiB; it includes all
47 required S uppers, origin lower, three actual uppers, tree and METHOD.
Binary/TU/runtime artifacts remain off Git and must be preserved along
with the full raw record. No statement of formal proof-assistant checking
or independence of the common arithmetic implementation is made.

## Exact finite mathematical result

The tree is the complete71-node midpoint preorder
`abababababab....b..a..ba...ab...bab....ab...bab....ab..b..bab..b..ab...`.
Its36 closed leaves comprise5 NEAR,29 FAR and2 OUTSIDE. Every nonoutside
leaf has theta<1. Applying its retained vertex upper bounds to the own-tree
absorption inequality gives

```
R_tree = 102745854336906991/3442879670484992
M = ceil(R_tree) = 30
L = 4195179000108131/140737488355328
minimum NEAR gap = 527707623611753/34480684647055360
minimum FAR gap = 84112940306975/6896136929411072
```

Both displayed margins are strictly positive. Here theta is
`(22/7)^2*((a_h-a_l)^2+(1023/1024)^2*(b_h-b_l)^2)/8`,
V is the maximum of the fresh vertex uppers and U=V+30theta. Closed
midpoint splitting covers the whole unit phase square. Only boxes whose
lower coordinate sum is strictly greater than1 are discarded; tangencies
remain covered. Period folding is (a,b)->(1-a,1-b) beyond the diagonal,
with swapping allowed only on its equality edge, not in the interior.
Thus physical phases in the closed triangle, including boundaries, are
covered with the accepted S symmetries. FAR proves U<L. NEAR proves
U-1/20<L on an entire proxy contained in the true near region. The accepted
generic checker also requires both relevant strict tests for a straddling
box; no such SPLIT leaf is needed in this certificate.

At n1023 the accepted D29-floor512 proof applies. Its1/20 defect bound is
used only for actual noncorner centers and actual signed near points with
rho<=r_B=min(1/2,(22/7)(a_h+b_h)). It is never asserted throughout an
outer phase proxy. The original corrected kernel, actual odd centers,
parity, boundary weights and coincident/tied image contributions remain
the D29/D32 hypotheses. The two projected corrections give the applicable
maximum lower bound; they are not added. Since the actual corner value
Lambda_c=S(0,0)>=L, strict comparison with L suffices for exclusion while
Lambda_c remains symbolic.

For actual corners, the three lower losses from the fresh origin lower
and actual uppers are

```
61538995298445/17592186044416
564287601973285/281474976710656
1543209776190237/281474976710656
```

With u'=1/32 and v'=9/512, the unrestricted D08/D32 actual three-point
criterion yields

```
q = 61538995298445/549755813888
threshold = 30*(22/7)^4/192 = 73205/4802
q-threshold = 127632690533730925/1319963709145088 > 0
radial squared coefficient lower =
127632690533730925/26076017764335616 > 0
```

The physical turns1/(4n),3/(16(n+1)) correspond to the accepted pi/4 by
3pi/16 corner rectangle. Its half-diamond coverage and the strict radial
loss exclude every noncentral point in each actual corner patch. This is
the actual three-point, pi-fourth loss argument, with final M30; no zero
actual-corner loss or asymptotic model transfer is used.

Accepted D32 then assembles the physical cover: all noncorner near cells,
far cells and both true corner patches. Since1023 is odd, equality is
attained exactly at (-1,-1) and(-1,1), and the maximum is their common
symbolic Lambda_c. The finite degree1023 computer-assisted theorem is
**ACCEPTED by this reviewer**, subject to the explicitly recorded accepted
mathematical inclusion/cover dependencies and trusted arithmetic runtime.
Missing primary outer EXIT0 is preserved as a primary-provenance limitation;
it is not an additional mathematical premise after this complete fresh
proof. No other finite degree, engine termination at other inputs, global
degree scan, analytic1024 result, or pack construction is asserted here.

## Distinct application audit and final verdict

I read all20653 B of `theory/D36-global1023.md`, frozen SHA256
`dbdd51c35e9234d620d61b3a63e07dcb3f3da8b8115d23a427493cd6604fcbb3`.
**ACCEPT** the application and its sufficient implication, with this fresh
result now discharging the explicitly pending execution/result obligations.
Its earlier OPEN wording and dated pre-audit update accurately preserve
history; they are not a competing mathematical conclusion. A later dated
PROVED/adoption closure may identify this review without rewriting that
frozen history or claiming a recovered primary observation.

The application correctly keeps N=1047552, n1023/m1024, original cardinal
normalization/weights and finite collision values; the full physical
odd-center cover; signed phase reduction without an interior coordinate
swap; global own-tree norm absorption; exact closed proxy semantics; the
D29-floor512 bound on actual noncorner near points only; symbolic true
Lambda_c at the interpolation origin; physical actual point scaling;
final-M pi-fourth strict criterion; half-diamond and parity reflection;
and equality exhaustion at exactly the two odd endpoint corners. All
displayed fresh constants agree with the authenticated fresh essential.
There is no import of D27/PD-T271 or the analytic1024 theorem into this
finite1023 actual-point proof. Its numerical inclusion/trusted-runtime,
resource, archival and missing-primary-observation limits are explicit.

Root's canonical copies in `evidence/post_audit_D36/` were inspected:
`fresh1023.json` and `fresh1023-final-accounting.json` have exactly the
fresh essential/account hashes recorded above. The580 B
`fresh1023-observation.json`, SHA256
`3cf3d93b8a7d0b98df74a8eaea6843bc745861e264c61d36f0c7ad6cfc816882`,
accurately records my direct session95825/chunkc3f838 EXIT0 observation
and keeps primary EXIT0 unobserved. Root's receipt of my observation is
not represented as root directly observing my execution.

Final distinct verdict: **ACCEPT D36 finite degree1023 result and frozen
application**. All required fresh numerical premises, source/domain
coverage, complete strict finite cover, actual corner witness, complete
final accounting and directly observed fresh outer EXIT0 are present.
No unresolved finding or requested numerical rerun remains. Root alone
controls publication/adoption. This review changed only its assigned
registration/result files and performed precisely the released fresh
verify invocation; subsequent commands were read-only evidence inspection,
hash/byte checks and report writing, with no extra scientific test.
