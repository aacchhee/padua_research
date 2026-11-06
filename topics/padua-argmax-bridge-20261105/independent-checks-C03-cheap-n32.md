# C03 mode0 — released complete known-n32 replay

2026-11-06. **PASS: the original 364-leaf candidate is accepted.**
The coordinator explicitly released exactly one full mode0 run after
distinct wrapper review and publication at
`e8fad1671fb736247e4c510284f6f935e6345efb`. This report records that run
and read-only postchecks. It does not replace the independent C03
mathematical/source reviews or the pending formal Claude audit.

## Frozen execution and outcome

Executed exactly once, with process exit0:

```text
python topics/padua-argmax-bridge-20261105/code/cheap_C03/replay.py --run-once --source-commit e8fad1671fb736247e4c510284f6f935e6345efb
```

Wrapper SHA256
`0e53a602103b6b5bf0afb80d338329ab8e3c442d7ab86e2051d3a88e9a447d37`,
22974 bytes; native source SHA256
`9e357b25efde553211563bb69147644c67b7752bc703bf05ac502141c82e0861`,
16881 bytes. The original decompressed candidate has21338 bytes and
SHA256 `97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e`.
The wrapper used the unchanged `check_r8.check(data, kernel)` acceptance
function, explicit fresh C03 kernel, and mode0 only. No leaf cap,
retry, rescue, mode change, producer, refinement or new degree occurred.

All364/364 leaves were checked, with zero pending and zero failures:
280 far,28 corner-orbit-plus-defect,24 maximum-exclusion-plus-defect,
and32 outside. The candidate's original ordered `(root,path,kind)` list
equals both the full C02 and C03 replay lists exactly. Every one of the
76 preserved C02 failures now passes:48 far and all28 corner-orbit.
The333 native calls have exactly the same ordered degree/box pairs as
the C02 trace, including the initial constants call.

The unchanged checker concludes that the global maximum equals the
corner value with exactly two nonnode corner maximizers, conditional on
its same published corner/bootstrap premises. This establishes a cheap
accepted replay for this known n32 candidate. It is not a new-degree
claim or evidence that every candidate or degree will meet this budget.
Historical novelty and external priority are outside this backend review.

## Strict margins and all-bound comparison

A separate postcheck reconstructed every box from the original root/path,
matched its native trace bounds, and recomputed all numerical predicates
using exact `Fraction` arithmetic. For all24 maximum-exclusion leaves it
also checked the full-box radius at most1/2. For all32 outside leaves it
recomputed the exact geometric exclusion. The constant bounds are
bit-identical in all332 bounded leaves.

| Predicate | Minimum positive margin | Root/path |
|---|---:|---|
| outside |3537118876014221/9007199254740992 = .39269908169872425|0/010010|
| far |6793119230151/562949953421312 = .012067003805340093|2/0101011011|
| corner-orbit |1235104191095/140737488355328 = .008775943108894069|3/0000000111|
| maximum exclusion |561502130767265/9007199254740992 = .06233925939539031|3/000000000|

Far margin is `Lc_lower-S_upper`; corner-orbit is the smaller of
`Lc_lower-C_upper` and `Lc_lower-S_upper+defect_lower`; maximum exclusion
uses the latter. All comparisons are strict.

Against C02, all332 S upper bounds improved. C upper bounds improved on304
leaves and weakened on28; defect lower bounds improved on44, weakened
on48, and stayed equal on240. Constants stayed equal throughout. Such
changes follow the valid lazy collector as well as tighter ratios; no
componentwise dominance is claimed. All final predicates nevertheless pass.
The first former failure, root0/path0101, now has
`S_upper=C_upper=10.52762339660344`, defect0, and
`Lc_lower=10.993594541100443`; its C02 S upper was11.467798411235936.

Against the previously accepted old-v3 replay, complete leaf order also
matches. Bounds remain weaker on324 S uppers,332 C uppers and226 defect
lowers; the other constant outputs do not weaken. Zero previously valid
leaves now fail. The cheap acceptance therefore does not rely on
reproducing the old bounds or intersecting with old finite-harmonic code.

## Cost and counters

Total group-plus-supervisor CPU was46.08976645s, consisting of
45.228637s subprocess CPU and .8611294500000001s supervisor CPU.
Wall time was45.46042339899941s. Worker accounting separately records
43.626414478s worker CPU and1.500444s compiler-helper CPU; native calls
used43.008296124s. These differently scoped counters are not asserted
to sum exactly to the supervisor's whole-lifetime subprocess measure.
The total stayed below180s; watchdog176s did not trigger, and the
worker soft/hard CPU limits remained178/179s. Errors were empty.

The old-v3 subprocess CPU was139.40540900000002s, approximately3.08224
times this run's45.228637s on the same candidate. This is an observed
single-run comparison, not a timing distribution. The earlier failed C02
run used31.965007579999998s total CPU and remains preserved as a failure.

Aggregate native counters, independently resummed from all333 trace rows:

| Counter | Count |
|---|---:|
| base ratio |9741780|
| sin/cos |21585196|
| base pole chart |17900|
| base fallback |0|
| lazy S |288|
| analytic floor |0|
| positive-pair profiles |45|
| boards |999|
| outer ratio |8439552|
| endpoint refinements |655240|
| centered refinements |0|
| ODE curvature caps |0|

Every native status was0, every returned bound finite, and every call's
centered/ODE counters zero. Source, build provenance and report all record
selected variant0; no mode switch occurred.

## Provenance and preserved artifacts

The wrapper checked all15 pinned input identities plus its own bytes
against the published commit before execution. It captured transitive
project Python sources, executed builder snapshot, native source,
preprocessed translation unit, binary, headers, toolchain and dependencies.
All254 closure entries, including8 actually loaded library mappings,
were verified before/after. The separate postcheck rehashed those entries,
the builder snapshot, Python runtime/project imports, input pins, old C02
raw report, and every new output identity in the receipt. The before-build
manifest equals the final report manifest, and the worker recorded stable
actually loaded mappings after execution. `source_runtime_checks_complete`
is true, with no provenance errors.

Essential receipt `evidence/c03-cheap-n32.json`,4729 bytes, SHA256
`e540444cd8455beab90f66338f774ebc62011a6d56dbc646d4e94fd92ff536df`.
The failed C02 receipt remains4417 bytes, SHA256
`924e8ebbe15ff8fd9a46e1d6c6887ae77e47fa4533af548df864fcea19bf3f41`.

Large local artifacts remain under
`local-output/argmax-bridge-20261105/cheap-C03/n32`:

- `checker-report.json`:163748 bytes, SHA256
  `18e6ec06d169335345c0f7a42663a39fc10046eff72d5edbe7a53991b8caa755`.
- `native-calls.jsonl`:128323 bytes, SHA256
  `bda630812248f6fdaeffa6711e56e504789a8ad97654ca9755ac7008fdb8af87`.
- Build/runtime closure, launch, worker accounting, stdout and stderr
  identities are in the essential receipt/full report; stdout/stderr are empty.

The read-only postcheck summary is `/tmp/c03-full-postcheck.json`; its
facts are transcribed above, and it invokes no acceptance function,
compiler or native kernel. No additional full job was performed.
Physical archive transfer remains pending. Sources, old reviews and old
receipts were not edited by this execution task.
