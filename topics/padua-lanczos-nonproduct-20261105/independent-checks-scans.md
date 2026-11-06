# Supplementary independent scan check — 2026-11-05

**Verdict: PASS within the finite implementation/replay scope below.** No
BLOCKING or MAJOR finding. This is the distinct supplementary check requested
by handoff01; it does not replace Claude's substantive audit or certify any
all-degree conclusion.

Checker: distinct Codex worker, assigned `gpt-6-astra high`; serving model
metadata is not independently exposed. Rules were read at full head
`698802430d333d559668d990123a317f33485064`. Read AGENTS, WORKFLOW, Codex role,
handoff01, plan, LOG and scan-methods; reviewed P4's weighted finite quotient
and continuous-capacity records, P1 triangle admission and P2 disk admission.
This scope is existing implementation verification, not a new mechanism,
novelty/disposition audit or priority claim. Accordingly the full IDEAS read
was omitted under the role's explicit no-novelty exception. No developer
source, theory, shared log, registry, handoff or Git state was changed.

## Scope and independence

The developer wrote both native arithmetic implementations. Here I actually
compiled and executed both again in a new directory, then compared their
scientific fields to each other and the developer's results. Separately I
wrote a Python Fraction implementation that imports no P6 formula code,
constructs the basis directly by monomial Gram–Schmidt, independently
reconstructs parent decisions/scales, and inverts each node's triangular
response recurrence. This third implementation checked degree3 on all three
families and four rules. Agreement at degree3 supports the formula mapping;
it does not imply a separate third implementation was run at degree16.

The inspected scientific source identities are in
[evidence/check-scans-source-hashes.json](evidence/check-scans-source-hashes.json).
The two main native sources are SHA-256
`41c11190b7b15bb5acd5070ccfdb1b66a4bad3739e02d727aba4a506cee2ed6d`
(producer) and
`58480a866b56e22c61add95d01f90774726b5f90e32186354ef1ab8f87b10b72`
(scalar checker). Their hashes match the developer's receipts. Execution
receipts identify the exact source/input/output bytes, commands, compiler
and runtime. The coordinator advanced the shared branch during this work;
final checker receipts record head
`dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc`. Those receipts and source hashes,
not an assertion that every file at that head was reviewed, define coverage.

Environment: Python3.12.14; g++ Debian14.2.0-19; GMP6.3.0; Linux x86_64,
glibc2.41. Exact rationals were used for comparisons, endpoints, logarithm
bounds and OLS extremization. No network data or remote computation was used.

## Executed results

| Independent execution | Coverage | Result |
|---|---|---|
| Fresh H24_222 native runs | degrees2–16, all4 rules, both backends | 60 exact row pairs match; 120 backend/reference comparisons match |
| Fresh D36x9 native runs | degrees2–8, all4 rules, both backends | 28 exact row pairs match; 56 backend/reference comparisons match |
| Third Fraction formula reconstruction | degree3, T24/H24_222/D36x9, all4 rules | all12 rows' four endpoints, choices and ties match |
| Independent N2 calculations | inherited T24 compact logs; new H24_222 exact rows | both INCONCLUSIVE |
| Negative controls | 15 Python interface rejections;10 native input rejections; native primitive test | all pass, including8 internal malformed native controls |

Receipts: [Hahn replay](evidence/check-scans-H24_222.json),
[disk replay](evidence/check-scans-D36x9.json),
[reference comparisons](evidence/check-scans-comparisons.json),
[formula reconstruction](evidence/check-scans-formulas.json),
[fits](evidence/check-scans-fits.json), and
[guards](evidence/check-scans-guards.json).
Each file is under16KiB. Raw fresh rows, compiler outputs and logs remain in
`/tmp/padua-lanczos-nonproduct-20261105/scan-review/`, with byte counts and
hashes in the replay receipts. They are not claimed to have been delivered
to external cold storage.

All scientific fields match exactly; only wall time and the count of Gram
pairs checked by the whole maximum-degree run were excluded from the
cross-run dictionary comparison. Gram coverage was separately checked by
the scan harness. Comparing elapsed times or total Gram counts across
different maximum-degree executions would not be a scientific equality test.

For H24_222, the slowest fresh producer/checker cases were5.04/14.41s;
for D36x9 degree8 they were4.30/22.66s. This check did not launch another disk
degree16 run. At inspection its developer receipt remained INCOMPLETE,
with only the BJ/mirror producer cases recorded complete. Neither those
partial outputs nor the degree8 replay support an N2 disk verdict. Any
later disk N2 result requires complete all-rule/both-path coverage and a
separate check of that new artifact.

## Formula and fit review

The generators reproduce the admitted data: T24/H24_222 have325 points;
the Hahn weight is `(i+1)(j+1)(25-i-j)/binom(29,5)`, summing to1. D36x9 has
324 distinct rational points with equal normalized weight. The checker
rebuilt these point/weight sets independently and compared them exactly
with the actual native inputs. The scans stay within the admitted degree
ranges and satisfy M>N_s.

The source scale in code is the squared weighted norm of the selected raw
coordinate product. The response sums include every nonconstant source
through the output prefix. The normal diagonal includes the node weight,
whereas v_hi has no extra node weight, agreeing with represented Euclidean
sources in P4-02. The code's Knode², KHS², row² and minimum upper² match the
stated lower/upper formulas. The source/rule convention remains consistent
across each ratio. The pivot rule compares residual-square/raw-square
exactly and chooses X on ties; the direct monomial construction confirmed
these choices and ties in the tested small cases.

For N2 I independently recomputed `L_BJ²/min_R U_R²` and
`U_BJ²/min_R L_R²`, including BJ in the four-rule comparator set as the
current plan specifies. Taking half-logarithms is necessary. A new local
rational-series implementation uses192-bit outward mantissa bounds and a
96-term atanh series with a proved geometric tail; its18 lower/upper log
bounds lie inside the developer's H24_222 reported bounds. Enumerating all32
corners in each five-degree window independently checks the signed OLS
coefficients `(-2,-1,0,1,2)/10`. Its slope extrema also lie within both of the
developer's rational-log paths' extrema. Thresholds are strict0.1 and0.02,
with the decision requiring both windows, exactly as preregistered.

| Family | 8–12 slope enclosure (decimal display) | 12–16 slope enclosure (decimal display) | N2 |
|---|---|---|---|
| T24, inherited compact logs | [0.137373742216312,1.802356877851230] | [-0.216477623410181,1.822813370740502] | INCONCLUSIVE |
| H24_222 | [0.055306901913349,1.539503505584218] | [-0.220202416458254,1.651201929678249] | INCONCLUSIVE |

These are interval screens of finite capacity bounds. They are neither
exact evaluations of the capacities/condition quantities nor proofs or
refutations of exponential or polynomial asymptotic growth. The N2
INCONCLUSIVE labels are supported; no pass/redirect is hidden by the check.

## Commands actually executed

All commands were run from `/workspace/padua_research`; the replay harness
records the expanded compiler and native commands. The relevant commands
were:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family H24_222 --max-degree 16 --seconds 600 --work-dir /tmp/padua-lanczos-nonproduct-20261105/scan-review/H24_222 --receipt topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-H24_222.json
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family D36x9 --max-degree 8 --seconds 120 --work-dir /tmp/padua-lanczos-nonproduct-20261105/scan-review/D36x9 --receipt topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-D36x9.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode compare --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-comparisons.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode formula --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-formulas.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode fits --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-fits.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_guards.py
```

The review checker was rerun after adding explicit input/output identity
checks and correcting command metadata; final receipts pin its final source.
No failed mathematical comparison occurred. Native replay directories must
be fresh when repeating the harness; choose new directories and receipts
instead of overwriting completed evidence.

## Notes and limits

- **NOTE — inherited provenance:** T24 compact table SHA-256
  `2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38`
  matches the accepted inherited evidence. Its source manifest and original
  large report are absent at their recorded local paths in this environment;
  the frozen logarithm code is present and matches its hash. I reproduced
  the new N2 extrema from all76 compact rows, but did not independently
  reconstruct the original high-degree T24 logarithms. This limitation is
  already explicit in the developer's inherited-scan receipt.
- **NOTE — disk completion:** degree16 remains outside this executed replay
  scope, and partial completion cannot establish a screen result. The
  completed degree8 replay validates only its recorded finite range.
- **NOTE — audit limits:** no new all-degree theorem, N3 recursion, P1/P2
  continuous moment probe, P3 radius or mechanism disposition was audited
  here. Admission and P4 records were read for the implementation's exact
  assumptions. Their full mathematical/novelty audit belongs to the required
  substantive handoff. Python guards were executed with assertions enabled,
  as in all recorded commands.

No requested developer correction arose within this scope. The independently
executed checks strengthen the finite evidence while leaving the stated
scientific and storage limits intact.

## Focused addition: untrusted basis export and generic FLINT inverse

Requested after published head `1753d3215a50ea3b908c592a3494d6df399bafa0`;
this addition preserves the earlier completed scope. Reviewed the working
sources `p6_basis_export.cpp` and `flint_disk_check.py`, plus the new explicit
specification route in `p6_scan.py` and D65x9 admission P2-04. Source/data hashes
are pinned in [generic timeouts](evidence/check-scans-flint-timeouts.json) and
[basis rejection controls](evidence/check-scans-flint-guards.json).
The original native mathematical kernels remain unchanged. D65x9 is a
separate324-point measure; it is never substituted for D36x9 in the results.

**Static reduction accepted; new degree8 endpoint replay incomplete.**
There is no mathematical mismatch or BLOCKING/MAJOR finding in this reviewed
variant. Generic inversion was not promoted to degree16. Both fresh
supplementary degree8 alternating cases timed out at their frozen120s cap,
without emitting completed endpoint rows; therefore this addition does not
claim an independent successful FLINT endpoint replay at degree8. The
subsequent pivot cases in those two harnesses never launched.

The basis exporter is derived from the producer and is consequently an
untrusted certificate supplier, not an independent arithmetic implementation.
The verifier independently reads all input points/positive normalized weights,
checks distinctness, exact start, grading, M>N_s, positive norms, every entry
of the weighted Gram identity, and every selected creator identity using
recomputed weighted inner products. For the adaptive rule it reconstructs
both admissible creators and compares exact source scales/scores, including
X-on-tie metadata. The selected alphas and squared source scales are checked
against those recomputed values.

Here is why those checks suffice without trusting the producer's basis.
Inductively b_0=1 and the admissible relation
`b_k=a_k b_parent−sum_(l<k)alpha_kl b_l` express every column as a polynomial
with the prescribed leading monomial and only earlier ordered monomials.
The coordinate/parent order has this triangular property. The full weighted
Gram identity makes b_k orthogonal to every earlier column; positivity and
triangularity identify the earlier span with earlier monomials. Hence the
column is the unique monic Gram–Schmidt residual. Recomputed inner products
certify its alphas, d_k and sigma². For an alternative admissible creator,
its leading monomial is the same, so the verified residual equality to b_k
certifies the candidate's residual norm too. Thus shared exported values
are acceptable only after these checks, rather than by a shared-source
assumption. The independently admitted input remains the external family
identity; arbitrary text in a JSON family label alone is no admission.

At each original node the verifier constructs the exact unit lower
triangular matrix `A=I+alpha−coordinate·parent`. Its inverse is unique;
checking `A*G=I` certifies the frozen response coefficients for every source.
The constant source column is omitted from the budget, while all
nonconstant source columns and every completed-degree prefix are retained.
Normal leverage, source scaling and endpoint formulas are unchanged from
the already reviewed P4-02 model. Full Gram certification is not a capacity
claim by itself, and an inverse computed for only some nodes is insufficient.

I actually executed15 malicious-export controls using a fresh pivot degree4
export and the verifier. These reject changed basis values, norms, constant
start, input coordinates/weights, parents, axes, alphas, scales, grading,
prefixes, choices, ties and rule. A coherent rescaling of a basis column and
its squared norm preserves Gram orthogonality but is rejected by the creator
identity, directly testing the monic-uniqueness safeguard. A separate exact
set reconstruction of the D65x9 input from integer pairs
(16,63),(25,60),(33,56),(39,52), axes and nine radii matches all324 actual
native nodes/weights. This is included in the same compact receipt.

Fresh replay commands were:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_flint_replay.py --family D36x9 --degree 8 --seconds 120
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_flint_replay.py --family D65x9 --degree 8 --seconds 120
PYTHONPATH=/tmp/padua-lanczos-nonproduct-20261105/deps python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_flint_guards.py
```

Both replay harnesses independently compiled the exporter. The timeout
receipt preserves the expanded commands, source/binary/input/basis/log
hashes and last progress: D36x9 verified its basis then reached node32/324;
D65x9 verified its basis then reached node128/324. All displayed progress is
partial. Python-flint0.9.0 / FLINT3.6.0 was loaded from the task-local deps
installation, one FLINT thread per process. No dependency was installed by
this checker.

Resource chronology: the two short supplementary jobs launched before the
coordinator's one-extra-process coordination message arrived, overlapping
with the helper and four long native cases. They finished by timeout and
no later case was launched. This contention is recorded, and their wall
times are not presented as an isolated speed benchmark. The coordinator
subsequently declined generic degree16 scaling and allowed the helper one
separate block-inverse cost experiment. That different implementation is
outside this addition until explicitly inspected and replayed.

### Block-inverse variant disposition

Subsequently inspected the exact diff for `flint_disk_block_check.py`:
only inversion, phase timing and method labels change. The recursion uses
`[[L,0],[C,R]]^-1=[[L^-1,0],[-R^-1 C L^-1,R^-1]]`, ending at the verified
unit diagonal singleton. Its slicing/reassembly agrees with this formula
for odd and even sizes. A is constructed unit lower triangular, and the
unchanged `A*G=I` check remains a separate exact certificate. Full basis,
source, node and prefix guards are retained. The generic reference reader's
later prefix support also checks contiguous degree coverage, requires the
reference reach the tested degree, and compares every resulting prefix row;
it does not accept missing tested degrees.

[Static review identities](evidence/check-scans-flint-block-static.json)
identify the inspected block source and developer receipts. I did not
independently execute this block endpoint path. The developer's BJ6 run
completed and its alt8 run timed out60s; both are correctly distinguished in
[flint-check-notes.md](flint-check-notes.md). The coordinator's bounded cost
screen therefore provides no reason to repeat degree8 or attempt degree16
on this variant. No further replay was launched here after the two generic
timeouts. This is an accepted static identity/guard review with successful
malformed-export executions, not a promoted disk16 checker or an independent
successful block endpoint rerun. The earlier native replay verdicts remain
unchanged.

## Focused addition: exact sign-reflection response reuse

**PASS conformity review and independently executed degree8 pilots.** This
is a new dated method variant, separate from the preserved generic/block
FLINT performance failures and original no-symmetry executions. The
coordinator provided the distinct mathematical review's acceptance of
[p6-reflection-methods.md](p6-reflection-methods.md), SHA-256
`a9b75c0c3597119f2305c659179025e531c072a516dc45f96873b1aedeba2f28`,
before these experiments. This checker inspected that proof and the frozen
`p6_reflection_scalar.cpp`, SHA-256
`09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088`.
No new mechanism/priority claim is made by this implementation review.

All seven mandatory guards conform on inspection and execution:

| Proof requirement | Actual implementation checked |
|---|---|
| Original normalized weighted measure and exact reflection group | Full input read, positive weights, sum1, distinct nodes, coordinate/weight matches, bijective/involutive/commuting sign permutations |
| Full-node basis and selection | Raw products, all candidate coefficients/scales/norms, selected diagonal/off-diagonal Gram, fixed rules and exact pivot ties on all324 nodes |
| Basis parity | Every column and original node tested under both generators, including fixed axis points |
| Coefficient and parent parity | Every candidate alpha slot tested; nonmatching parity forced exactly zero; actual parent exponent and axis relation checked |
| Exact orbit partition | Absolute-coordinate classes equal the generated sign orbit; actual representative, disjoint/full membership and size1/2/4 checks |
| All source snapshots and full expansion | Every original source h retained; representative v snapshots copied to every original i before totals/maxima; aggregate snapshot count checked |
| Original projector and endpoints | Actual full-node weighted normal diagonals, [0,1] bounds, trace M−N_s and lower/upper guards retained |

The only recurrence arrays shortened to90 representatives are g and its
squared energy. The code neither identifies reflected source coordinates
nor compresses the ambient projector. It uses no coordinate interchange.
Every original node/source contribution is restored before the unchanged
sum and maximum operations. Thus the proof's squared-response invariance
is applied exactly at its stated interface, not to the spectral capacity
itself or to a different source budget.

I compiled the frozen variant independently and executed all four rules
through8 on each of D36x9 and D65x9. The helper first finished and explicitly
released the shared extra CPU slot; these fresh executions were serial,
one native process at a time, with60s per-case caps. Original degree8
producer and scalar files supplied the comparisons. D36x9 references are
from my earlier independently executed full-node replay; D65x9 references
are the developer's accepted full-node degree8 run, on the separately
reconstructed/admitted D65 input. No D36 result is attributed to D65.

All56 computed prefix rows match both original paths:112 exact reference
comparisons. **Every original nonelapsed JSON field is compared, including
Gram count**, because each reference and fresh case has the same maximum
degree8. Counts per case are45 basis columns,29,160 basis-parity scalar
checks,44 original nonconstant source positions, and49,896 expanded
node/source/prefix snapshots. All cases have90 exact orbits:18 size2 and
72 size4, covering324 original nodes. Fixed-rule cases check44 parent
relations and990 alpha slots,750 of them cross-parity zeros; adaptive
cases check72 candidate parent relations and1,704 alpha slots,1,300 of them
cross-parity zeros. These counts are checked independently in the replay
harness against the declared degree and node count.

For each family I also executed two malformed full-input controls, retaining
324 nodes, positive weights and total mass1: a perturbed node breaking exact
reflection closure, and unequal reflected weights. Both reject with their
specific reflection diagnostics before basis/source propagation. The
binary's three internal reflection/parity rejection controls also pass.
Raw malformed inputs and commands are hashed in the receipts; these are
actual negative executions, not assertions that guards ought to reject.

Fresh case wall times: D36x9 BJ4.076s, mirror4.476s, alternating5.579s,
pivot6.084s; D65x9 BJ2.120s, mirror2.320s, alternating2.671s, pivot2.872s.
These are observed under the recorded shared-load setting, not a controlled
speed-factor theorem. The arithmetic equality and passed mandatory guards
support the coordinator's decision to attempt a separately bounded degree16
run. **No degree16 reflection run, completion or N2 disk result is claimed
by this supplementary addition.** The preregistered N2 model and thresholds
remain unchanged.

Executed commands, from the repository root:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_reflection.py --family D36x9
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_reflection.py --family D65x9
```

[Replay driver](code/check_scans_reflection.py) and compact receipts
[D36x9](evidence/check-scans-reflection-D36x9.json) and
[D65x9](evidence/check-scans-reflection-D65x9.json) record compiler, GMP,
Python, head, full commands, frozen source/binary/input/output/log hashes,
references, negative controls and actual guard counts. Both receipts are
under16KiB. Raw data stay in the task-local scan-review reflection
directories; no external archive delivery is asserted. No developer code,
proof, shared registry or Git state was edited by this checker.

## Continuation after UI reconnection: compact H24 evidence

Rules and role were reread at supplied head
`697863b9085f8e326e7b0c0c502e93127c318749`. The resumed supplementary reviewer
retains the assigned Codex Astra high role; serving metadata is not
independently exposed. This continuation inspects existing finite evidence
and introduces no novelty claim; the full IDEAS read remains outside scope.
The cloud-environment runtime skill and current readiness were also read.
No Git, developer source, proof, shared log, registry or handoff was changed.

**PASS H24 compact table.** The new
[compact reviewer](code/check_scans_compact.py) imports only the previous
supplementary reviewer's independent rational logarithm and corner routines.
It checks all120 endpoint half-logarithms against the actual accepted raw
rational rows, using192-bit mantissa bounds and96-term atanh series. Every
logarithm interval is enclosed by the table's outward integer bounds at
scale10^15. All60 producer/checker rows match in every nonelapsed field,
including Gram counts; all eight raw-output/source/digest provenance entries
are verified. The two compact N2 window extrema agree with a separate
32-corner enumeration and enclose both higher-precision primary slope paths.
The unchanged verdict is **INCONCLUSIVE**.

Actually executed in this continuation:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_compact.py --family H24_222
```

The final [receipt](evidence/check-scans-compact-H24_222.json) records27.40s,
source/data hashes and precise coverage. Its compact table SHA-256 is
`634f55266aa61a13ce095526c6b1c842de41e66b557a8b14e46c814bdb49ea57`.
An initial reviewer-only linkage assertion compared a relative path with
an absolute path after all120 logarithm checks passed. The reviewer fixed
that assertion to compare resolved paths after byte/hash checks and reran
successfully; no developer or mathematical mismatch was found. These
compact intervals permit repository-only N2 replay; rechecking their
original endpoint generation still needs the pinned raw rows or regeneration.

The earlier distinct reviewer had launched the supplementary D36 degree16
ALT/PIVOT runs before reconnection. On continuation, harness PID9491 and
native PIDs9506/9507 were still running with their original source/input
bytes and3600s per-case caps, maximum two native processes. Process metadata
recorded harness start2026-11-05 23:17:43UTC and native starts23:17:49UTC.
Those processes were neither relaunched nor overwritten by this reviewer.
Their completion and subsequent comparisons are recorded separately below
when available; this paragraph itself claims no completed high-degree row.

### Retained primary completion and independent disk N2 reconstruction

**PASS focused recovery review.** The primary native ALT/PIVOT outputs
completed, but the original primary receipt retained only seven cases and
INCOMPLETE status. The new artifact-only adapter
[primary harvest](code/p6_harvest_reflection.py), SHA-256
`00ab0de9c7a630773f296cb5a7a1647ab9bfbfa6ca75b0f5fadb29c510922410`,
preserves that original receipt and constructs the separate
[recovered acceptance](evidence/p6-disk16-recovered-acceptance.json), SHA-256
`aefa709edb828fd3157218c974b22cd09525f5909ca6d192cba858e7a0b95877`.
The native PIVOT harness wall time was not saved; the adapter keeps it
unknown and labels the rounded native timer separately. The original
parent's stop cause is unknown. Artifact collection is not another native
execution.

I inspected the adapter and independently verified all60 exact full-field
producer/checker row pairs, the seven unchanged original case records,
both reflection guard logs, source/input/output links and all three actual
native source hashes. BJ/mirror use the original scalar source
`58480a866b56e22c61add95d01f90774726b5f90e32186354ef1ab8f87b10b72`;
ALT/PIVOT use the reviewed reflection source `09d524f…`; all producers use
`41c11190b7b15bb5acd5070ccfdb1b66a4bad3739e02d727aba4a506cee2ed6d`.
The [focused review receipt](evidence/check-scans-continuation-recovery-review.json)
pins the complete hashes, recovery code and accepted data. This check has
no unresolved finding and does not replace the earlier incomplete receipt.

From these completed all-rule rows I separately reconstructed the two
squared BJ/best endpoint ratios at each degree8–16, computed rational
half-logarithm bounds and enumerated all32 signed OLS corners in each
window. All18 independent logarithm bounds lie inside the reported primary
bounds; independent slope extrema lie inside both original rational-log
paths. The unchanged N2 decision is **INCONCLUSIVE**. Decimal outward
summaries of my independent slope enclosures are:

| Window | Lower | Upper |
|---|---:|---:|
| 8–12 | -0.507848236139249 | 1.061047505157414 |
| 12–16 | -0.887372978742640 | 1.162463772216736 |

The exact [independent N2 receipt](evidence/check-scans-continuation-fits.json)
is authoritative. This verifies a finite endpoint-box screen, not exact
capacities, an asymptotic rate, or a disk-family rejection. The independent
high ALT/PIVOT replay collection remains a separately recorded obligation.

Executed continuation commands, without native launches:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_continuation.py --primary topics/padua-lanczos-nonproduct-20261105/evidence/p6-disk16-recovered-acceptance.json --mode recovery-review
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_continuation.py --primary topics/padua-lanczos-nonproduct-20261105/evidence/p6-disk16-recovered-acceptance.json --mode fits
```

### Final D36 compact validation and completed supplementary high replay

**PASS D36 compact table.** The same independent compact reviewer executed
on D36x9 after complete primary acceptance. All120 raw endpoint logarithm
enclosures,60 nonelapsed producer/checker row pairs, eight source/output
provenance entries and32 OLS corners per window pass. The compact intervals
enclose both higher-precision N2 slope paths and retain **INCONCLUSIVE**.
The [D36 compact review](evidence/check-scans-compact-D36x9.json) records26.08s
and table SHA-256
`6e9d31615ee5660752724018c9175a19c554c007fee71decc807dbfce829471d`.

**PASS collected earlier independent ALT/PIVOT degree16 executions.** Both
native runs started by the earlier distinct reviewer have now finished;
each emitted15 complete degree2–16 rows, all152 source progress records,
the complete reflection guards and its final finish marker. Their harness
ended with only PIVOT saved in the original execution receipt, whose
INCOMPLETE status is preserved. The new
[continuation collection receipt](evidence/check-scans-continuation-collect.json)
checks the completed raw files without relaunching either case and links
the original execution receipt, binary, source, input and producer bundle.
The native source remains the frozen `09d524f…` variant and the input remains
SHA-256 `48977eefea1c662c3ef23c8ed17d49e3cb0310a6d53321add8c51c91866313f6`.

All30 supplementary rows agree exactly with both the frozen original
producer bundle and the completed primary checker outputs. **Every
nonelapsed field is included**, particularly the full11628 Gram-pair count,
parent choices, pivot ties, all squared endpoints and exact normal trace.
The primary's all60 producer/checker row pairs were also rechecked. No
partial row or partial source prefix was accepted.

| Guard | ALT | PIVOT |
|---|---:|---:|
| Original nodes / representatives | 324 / 90 | 324 / 90 |
| Size2 / size4 orbits | 18 / 72 | 18 / 72 |
| Full basis parity scalar checks | 99144 | 99144 |
| Candidate parent checks | 152 | 272 |
| Candidate alpha slots | 11628 | 21488 |
| Verified cross-parity zeros | 8748 | 16200 |
| Original nonconstant source positions | 152 | 152 |
| Expanded node/source/prefix snapshots | 307800 | 307800 |

Each original case had a3600s cap, with at most two supplementary native
processes. PIVOT has the saved subprocess exit0 and harness wall time
1177.545742999s. ALT's subprocess return code and harness wall time were
not saved; they are not invented here. Its native phase timers report
106.769s basis,1462.76s source and22.0192s finishing, approximately1591.55s
in total. These rounded native times establish observed progress timing,
not a replacement for missing harness metadata or a controlled speed
benchmark. The complete output/guard validation is the acceptance evidence.
The parent was observed closed after native completion; the cause of its
incomplete harvesting remains unknown.

Fresh high-degree supplementary execution coverage is **ALT and PIVOT
only**, launched by the earlier reviewer. This resumed reviewer collected
and checked those executions; it did not launch them. BJ/mirror degree16
are reviewed primary artifacts, not fresh high supplementary reruns.
The separately documented earlier Hahn16/all-rule disk8 replays, formula
reconstructions and malformed-input controls retain exactly their earlier
coverage. No large endpoint job was repeated during this continuation.

Additional commands actually executed in this continuation:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_compact.py --family D36x9
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_continuation.py --primary topics/padua-lanczos-nonproduct-20261105/evidence/p6-disk16-recovered-acceptance.json --mode collect
```

All continuation receipts are below16KiB and pin their actual checker code
and data. Raw native outputs/logs remain under the named task-local `/tmp`
directories; no external archive delivery is claimed. No BLOCKING or MAJOR
finding remains within this supplementary finite implementation/evidence
scope. The required later Claude Opus5.5 xhigh substantive audit remains
pending; supplementary acceptance does not establish PR readiness or any
new all-degree theorem.
