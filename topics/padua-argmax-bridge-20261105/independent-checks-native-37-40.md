# Supplementary exact native checks — degrees 37–40

2026-11-06. Distinct Codex checker `/root/check_native_37_40`; requested
Astra high supplementary check, serving model/effort not independently
exposed. Rules and published input read at
`bda45a4c1392bea87de0841b6b23e5c35b2a694b`. This is separate from the
producer worker and supplements the required Claude audit.

## Scope and mathematical review

Read AGENTS, WORKFLOW, CODEX, handoff03, `theory/native-finite-range.md`,
`independent-checks-initial.md`, native checker README, full `check.py`
and `kernel.cpp`, PD-T210 including its general constructor appendix,
and PD-T101 through its cardinal construction and proof. This is a
quantitative continuation of the unchanged finite-certificate mechanism;
no new idea, novelty claim, schema, or mathematical proof is proposed.
Therefore a new novelty search is outside this check's scope.

The reduction applies to the full closed square. Nonnegative tensor
Bernstein weights sum to one. Strict coefficient absolute sums below
the common corner value give strict inequality on each bound leaf.
A corner leaf's only exceptional coefficient is its exact vertex value;
the associated Bernstein weight equals one only at that vertex. Closed
leaf boxes retain split boundaries. PD-T101 gives the corrected cardinals
and the parity-preserving reflection gives equal values at both nonnode
corners. Thus a complete accepted replay establishes both the maximum
and its exact two-corner equality set for that degree.

The checker reconstructs rational Machin/cosine brackets, integer interval
cardinals, exact rational Bernstein transformations and outward midpoint
subdivision with GMP. Rational transform terms are canonicalized. It
recomputes every leaf bound and both corner predicates, exact metadata,
and the complete prefix partition; Python and native traversal both
check coverage. In particular producer `accepted=false` is mandatory.
No floating sample or producer approval supplies an acceptance premise.
This uses the existing separately authored arithmetic path; it is not
a newly authored third arithmetic implementation.

## Frozen implementation and execution protocol

Before fresh compilation and each execution, and again after completion,
the runner verifies both live source bytes and their bytes in the input
commit against these fixed SHA256 values:

- driver `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`;
- kernel `b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0`.

Fresh isolated build, from `/workspace/padua_research`:

```sh
python topics/padua-argmax-bridge-20261105/code/check_native_37_40.py --build
```

The actual compiler argv is preserved in each receipt's `build` object.
It uses `g++ -O3 -std=c++17` and links GMP, with exit status 0.
The resulting binary SHA256 is
`f17fed2e69a98c952d1ad5e72de03c08b2ceb07970c49fc0db1b35396fe3e605`.
Environment: Python 3.12.14; g++ (Debian 14.2.0-19) 14.2.0;
libgmp-dev `2:6.3.0+dfsg-3`. Deterministic, no seeds.

Each degree uses a separate fresh driver/native process with no arithmetic
cache. The runner checks certificate and binary identities before/after,
records actual argv, start time, exit status and elapsed wall time, and
measures child user+system CPU by `RUSAGE_CHILDREN` differences. This
includes the driver's waited-for native child. A per-process 1790-second
CPU limit is inherited by both driver and kernel; total measured replay
CPU must also be below the assigned 1800-second degree allowance. Native
exit 0 follows from the frozen driver's `subprocess.run(check=True)`
returning normally and writing its complete receipt. Raw output, binary,
build record and original checker receipts remain off Git under
`local-output/argmax-bridge-20261105/check-native-37-40/`.

The old unchanged n33 corruption suite is not rerun: its 36 rejected
defects and valid complete/partial controls are preserved in
[the initial check record](independent-checks-initial.md). This block
changes only degrees and candidate data, not that tested implementation.

## Results

| n | Result | Bound / corner / splits | CPU seconds | Wall seconds | Receipt |
|---|---|---|---:|---:|---|
|37|ACCEPTED, exit 0|316 / 2 / 317|897.768536|918.566803|[n37](evidence/independent-n37.json)|
|38|ACCEPTED, exit 0|320 / 2 / 321|1049.906113|1072.093637|[n38](evidence/independent-n38.json)|

The n37 candidate has 8905 compressed bytes and SHA256
`425fb779e3d476efe221f6d1bef118cb1752fa9f538a46110b7ea2b44f2cefae`.
The n38 candidate has 8973 compressed bytes and SHA256
`fcb900fab6b596b7d258668e0de49a4bf9b76bc9d3f4c879ebb358d7b792f1d2`.
Both retain producer `accepted=false`. Their separately generated receipts
record all supplied bounds verified, complete partition and acceptance.
Actual wrapper commands:

```sh
python topics/padua-argmax-bridge-20261105/code/check_native_37_40.py --degree 37
python topics/padua-argmax-bridge-20261105/code/check_native_37_40.py --degree 38
```

Pending: complete independent replays at n39–40. No pending degree is
accepted by this record until its receipt is complete.

## Boundary

Trusted dependencies are PD-T101/210, the frozen Python/C++ checker,
Python, compiler, GMP and hardware. The parent integrates only complete
accepted degrees and retains essential certificate bytes. No schema,
producer, historical evidence, shared log/gate, registry or Git state is
changed by this worker. This does not close PD-T099 or supply an effective
all-degree onset; the required Claude audit remains separate.
