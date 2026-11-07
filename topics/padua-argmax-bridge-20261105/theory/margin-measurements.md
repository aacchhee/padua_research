# PD-T?argmax-bridge-codex-M1 — Finite sampled bridge margin anatomy

ID kind: PD-T. Aliases: B1 seven-degree map; sub-.01 phase sampling.
Split from: none. Split into: none; certifier measurements are separate.

## Statement and definitions

For n in {33,48,64,96,128,192,256}, the deterministic finite schedule in
[margin-anatomy.md](../margin-anatomy.md) produced the values in its table.
It samples144 far diamond phases, selected physical odd centers at1782
far point/center pairs,161 near phases with every admissible noncorner
odd center, and720 corner-shell points per degree. The full near count
is10,989,153 admissible center/phase pairs across the seven degrees.

S,lambda,Lambda_c and the phase charts are exactly PD-T364's conventions;
the C implementations evaluate floating approximations. The comparison
1/8192−(S−Lambda_c) uses PD-T366's analytic constant only at n>=48.
The n33 analytic comparison is inapplicable, as explicitly recorded.

## Status and assumptions

Overall status: **MEASURED**. Ordinary binary64 arithmetic has no proved
rounding-error bound. These are finite sampled extrema only. Far actual
lambda uses19 selected centers, not all centers. No continuous region
maximum, strict tiny-shell sign, certificate or effective onset is asserted.

## Depends on

PD-T101/364 for conventions and the point/projection formulas; PD-T366
for the scope of its analytic defect constant. These dependencies do not
turn floating profile evaluations into rigorous bounds.

## Evidence and actual checks

[Code](../code/margin_b1.py), [frozen receipt](../evidence/b1-margins.json),
and [full schedule/results/limits](../margin-anatomy.md). Actual command:

```sh
OPENBLAS_NUM_THREADS=1 B0_PASS=1 python topics/padua-argmax-bridge-20261105/code/margin_b1.py
```

Source checkpoint95366c1 contains the executed script; receipt hashes pin
all imported code and raw files. Developer: requested Sol medium. The run
completed after B0 PASS, taking118.42 summed per-degree wall seconds.
The1672 direct-polynomial cross-formula checks have maximum absolute
lambda/S differences7.99e-15/3.73e-14, not certified error bounds.
The parent rehashed every source/raw object, checked all18641 raw rows
for finite floats and reconciled their counts. Neither action is an
independent mathematical rerun; independent audit remains pending.

The sampled near primitive excess is positive at every tested degree:
about1.018e-4 at33 to1.744e-5 at256. The sub-.01 grid recovers positive
values at128/256 missed by the predecessor's coarser radius grid. This
does not locate a maximum or establish a scaling law. Tiny-shell floating
differences reach cancellation scale, with minimum−1.17e-13; no exact
counterexample follows.

## Sources, scope and open items

Internal formula implementations only; no external source or novelty
claim. No new mechanism is proposed by repeating this inherited diagnostic.
Raw sample/detail/validation files are locally inventoried in
[cold-storage.json](../cold-storage.json); physical archival and durable
retention remain pending. Reproduction targets the recorded finite
mathematical fields, not original timing bytes.

Continuous extrema, certified derivative/enclosure bounds and global
argmax remain separate OPEN obligations. The B1 map has no pass/kill
verdict and supplies steering inputs to B3/B4 only. PD-T099 remains OPEN.

## History

2026-11-05, Codex coordinator, requested Astra high; actual serving metadata
unexposed. Records the already executed95366c1 B1 observations in a durable
MEASURED home. No mathematical or computational scope is expanded.
