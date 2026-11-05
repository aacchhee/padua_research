# Supplementary independent checks — initial finite extension and N6

2026-11-05. Distinct Codex checker `/root/check_initial`, requested
`gpt-6-astra high`; serving model/effort are not independently exposed.
Rules read at `95366c19562e88c11138f88aab0a6617d6b15305`.
Frozen scientific inputs: `0bca52bc1b8edf2e91d3749b710d2df285dc3e6b`.
The parent subsequently added n35/n36 by the hashes below, while HEAD was
`714f3cad18859c07cd13f31561f2a185f9591a7f`; their input identity is the
compressed-byte hash rather than an assumed commit membership.
This supplements, and does not replace, the required Claude audit.
No developer file, Git state, registry, shared log or gate was changed.

## Scope and reading

Read AGENTS, WORKFLOW, CODEX, handoff01, plan, LOG and the baseline gate.
The finite replay is an implementation/degree continuation of unchanged
PD-T210, with no new novelty claim. Read the complete PD-T210 reduction
and general-constructor appendix, PD-T101's cardinal proof, and the frozen
native checker README, `check.py`, `kernel.cpp` and `controls.py`.

For N6, read all 1015 lines of `state/IDEAS.md`, including every
obstruction/disposition table; registry SHA256
`948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6`.
Read full IDEA206, original and canonical IDEA319, IDEA341/342,
PD-N086, PD-T364, and the new N6 gate, candidate, two theory records and
exact checker. INDEX's relevant LIT014/312/379/380 rows and addenda were
inspected. No external fulltext, historical priority verdict or transfer
of a source theorem is claimed. The two-trace comparison is a specified
variant of deferred319/341; the covering-family identities are verification
of inherited algebra. N086's individual-sign obstruction does not imply
the new full-norm comparison failure.

## Finite-proof reduction and implementation inspection

The checked reduction is the full closed-square implication of PD-T210.
Nonnegative tensor Bernstein weights sum to one. Their cardinal absolute
coefficient sums strictly below the common corner value force strict
inequality on a bound leaf. On a corner leaf the exact vertex coefficient
is the cardinal value at that corner; all other coefficient sums are
strictly below the corner value. Its vertex Bernstein weight is one only
at that vertex, so no other equality point survives. Closed leaves retain
every split boundary.

The native kernel reconstructs every cardinal from the corrected PD-T101
weights and exceptional `(n,0)` coefficient one. Machin's rational arctangent
series, monotone cosine Taylor enclosures, integer Chebyshev recurrence,
sign-aware rational Bernstein transforms and outward midpoint subdivisions
use GMP exact integers/rationals. All rational transform-weight terms are
canonicalized. No floating sample enters a verdict. The valid parity
reflection identifies the two nonnode corner values, so intersecting their
value enclosures and using the larger lower bound is sound.

The Python driver checks source/dependency hashes, exact reconstructed
metadata, exact leaf records, type-sensitive degree/metadata/counters,
producer `accepted=false`, no pending leaves, and both parity-correct
corner leaves. A prefix-free frontier F and its proper ancestors A form a
complete binary partition when `|F|=|A|+1`: the rooted finite tree then has
exactly twice as many child edges as internal vertices, so every internal
vertex has two children. The native traversal also rejects an uncovered
child. The kernel receives only degree and paths and recomputes all bounds.

Trusted components remain the written PD-T101/210 mathematics, the inspected
frozen implementation, Python/GMP/compiler execution and hardware. This is
a different-agent execution of the existing independent arithmetic checker;
it is not a newly implemented third arithmetic kernel.

## Actual commands and finite results

All commands ran from `/workspace/padua_research`, with Python3.12.14,
g++14.2.0 (Debian14.2.0-19), and GMP development package
`2:6.3.0+dfsg-3`. Deterministic; no seeds.

```sh
mkdir -p local-output/argmax-bridge-20261105/check-initial
g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp -lgmpxx -lgmp -o local-output/argmax-bridge-20261105/check-initial/kernel
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n33.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output topics/padua-argmax-bridge-20261105/evidence/independent-n33.json
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n34.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output topics/padua-argmax-bridge-20261105/evidence/independent-n34.json
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n35.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output topics/padua-argmax-bridge-20261105/evidence/independent-n35.json
python topics/padua-argmax-effective-20261103/code/native_checker/check.py topics/padua-argmax-bridge-20261105/evidence/n36.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output topics/padua-argmax-bridge-20261105/evidence/independent-n36.json
python topics/padua-argmax-effective-20261103/code/native_checker/controls.py topics/padua-argmax-bridge-20261105/evidence/n33.json.gz --binary local-output/argmax-bridge-20261105/check-initial/kernel --output topics/padua-argmax-bridge-20261105/evidence/independent-controls.json
```

The binary was freshly compiled in this checker's local directory. Normal
n33–n36 replays ran as separate processes concurrently; none uses a
cached constructor. Checker internal elapsed times are wall measurements
under concurrent load, not CPU measurements.

| Input | Bytes | SHA256 |
|---|---:|---|
| `evidence/n33.json.gz` | 8141 | `090f650ae5d52d72716857e8a67a8fac7c330fa208ff81487368e1ef89d82f90` |
| `evidence/n34.json.gz` | 8253 | `8c4866e2bda66e331e4940f17ace71b9caeb8ecf0bdd091bf026d215b21acb2d` |
| `evidence/n35.json.gz` | 8485 | `cdf5058f476692d1fc3847b8b59ca44ffe9cecd9ffc3271a2d47b733464935bb` |
| `evidence/n36.json.gz` | 8679 | `067fcf2af8eb2f112f65f2689ecd7102b87f1b2cb31b2508d97ba09be0d9f22c` |

Checker SHA256 `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`;
kernel SHA256 `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`;
controls SHA256 `65f0b68079f8330dd5b350eb979bafdb185ef29a26b1d006c4cc3d9e9ba2b5d4`;
fresh binary SHA256 `f17fed2e69a98c952d1ad5e72de03c08b2ceb07970c49fc0db1b35396fe3e605`.
An independent byte comparison against `git show 0bca52b:<path>` matched
all three frozen checker files and both compressed certificate files.
Certificate source head is `328be35e55143013047ec03a70e9906e82b95353`;
the independently enforced historical n2-guard compatibility rule and all
four source hashes are unchanged. Dependency SHA256 is
`ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c`.

| Degree | Independent acceptance | Strict bound leaves | Corner leaves | Splits | Wall seconds |
|---|---|---:|---:|---:|---:|
| 33 | ACCEPTED | 284 | 2 | 285 | 805.616 |
| 34 | ACCEPTED | 288 | 2 | 289 | 813.230 |
| 35 | RUNNING | — | — | — | — |
| 36 | RUNNING | — | — | — | — |

The completed [n33](evidence/independent-n33.json) and
[n34](evidence/independent-n34.json) receipts both record
`complete_partition=true`, `all_supplied_bounds_verified=true` and
`accepted=true`. n33 reconstructs595 cardinals and corners(-1,-1),(-1,1);
n34 reconstructs630 cardinals and corners(-1,-1),(1,-1). These are separate
fresh arithmetic executions on every leaf, not acceptance inferred from
the producer's `complete` field.

During execution an environment transition invalidated the original tool
session handles. Original OS processes and files survived; no job was
restarted. The completed receipts were collected directly from disk and
rehashed. The shell exit statuses for these transitioned sessions are not
recoverable; acceptance is established by the checker-written completed
receipts, which are written only after all validations return successfully.

The original, unmodified n33 [controls suite](evidence/independent-controls.json)
PASSED in931.759 wall seconds. All36 negative cases were rejected:
28 envelope/metadata/predicate defects,3 lexical JSON defects, and5 direct
native protocol defects (invalid path, duplicate path, ancestor overlap,
uncovered child and empty frontier). The valid complete positive case was
accepted and the genuine partial positive case was not accepted, with all
supplied bounds verified. This is the entire frozen suite, not a subset.
Its own initial n33 arithmetic replay was fresh; within that suite only,
reconstructed arithmetic is cached for an identical degree and complete
frontier. Every mutated metadata/verdict comparison runs anew, and the
five native malformed-frontier invocations reconstruct independently.

## N6 result — accepted in its stated narrow scope

The unimodular angular map has inverse
`t=theta-phi, s=(n+1)phi-n theta` modulo2pi. Applying the cosine fibers
then gives exactly4/2/1 parameter pairs at interior/edge/corner points.
The fixed-trace membership and collision conditions follow by comparing
the four signed-angle pairs. At a corner the parity of
`(n+1)k-nj` agrees with its physical mesh-index sum, giving s=0 at node
corners and s=pi at nonnode corners. Frequencies satisfy
`|a(n+1) +/- bn| <= n(n+1)` and `|a +/- b| <= n`; the corrected top mode
has the same bounds. The finite-polynomial form handles singular-looking
quotients by continuity and retains four-copy cancellation before absolute
values. These are direct analytic checks, not sampled inferences.

Independently re-executed the frozen developer checker:

```sh
python -B topics/padua-argmax-bridge-20261105/code/n6_two_trace_exact.py --output local-output/argmax-bridge-20261105/check-initial/n6-two-trace.json
python -B topics/padua-argmax-bridge-20261105/code/check_initial.py
```

Both exited0. The second script imports no developer module: SymPy1.14.0
independently inverts the rational n2 Vandermonde and evaluates its six
cardinals at the three exact radical points. It checks all mathematical
fields of the separately executed frozen receipt against the original and
verifies that each frozen N6 source equals its bytes in commit0bca52b.
Its short receipt is [independent-math-initial.json](evidence/independent-math-initial.json).
The unchanged developer script hard-codes `independent_execution=false`
and its original input-head field in every output; those raw metadata are
preserved, with the actual independent run and frozen commit recorded in
the wrapper receipt and here.

The exact trace norms are `3/2+sqrt(2)/6`; the witness norm is
`1/3+sqrt(2)`. The gap `(5sqrt(2)-7)/6` is positive because50>49.
All six signs at each point agree with the written proof. In particular
`1/3-sqrt(2)/4<0` follows from2>16/9. Thus one exact n2 point refutes
the universal fixed-t two-trace comparison. It does not refute an
optimized trace supremum comparison, another family, broad N6 or PD-T099.

No unresolved finding in this N6 scope. Assertions in the unchanged
developer diagnostic ran enabled; the independent wrapper uses explicit
exceptions. The written analytic proof does not depend on that diagnostic.
N4/N5 were only read preliminarily here; their formal independent review
belongs to the separately assigned checker and is not included in this
acceptance.

## Remaining boundary

Finish the two remaining native invocations and record their actual results.
The parent integrates accepted degree claims and small essential evidence.
Bulk binary/raw replay output remains local; no cold-storage transfer was
performed. Required Claude audit and all-degree bridge closure remain open.
