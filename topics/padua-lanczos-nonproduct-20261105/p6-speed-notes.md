# P6 bounded scalar-checker speed assessment — 2026-11-05

Rules/input head read: `dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc`.
Assigned technical developer: Codex, requested gpt-6.1-sol medium; runtime
serving metadata is not independently exposed. Only the assigned speed
files are changed. No Git operations, environment changes or network use.

## Scope and pre-run decision

This is a finite implementation comparison, with no new mechanism,
priority, endpoint, threshold, family or all-degree claim. Read AGENTS,
WORKFLOW, CODEX, topic plan, scan-methods, novelty-gate-P6 and P4-02 in full.
The existing P6 gate covers this scalar implementation variant; no new
novelty-bearing candidate is generated.

The closest checker is `code/p6_scalar_check.cpp`: independent scalar
`mpq_class` arithmetic, separately structured basis and frozen-response
loops. `code/p6_native.cpp` instead shares one denominator per vector and
uses integer-vector operations. Copying its arithmetic would defeat the
requested separate arithmetic-path check, so it is not proposed.

Before measurements, parent and n0_replay were told the only pilot change
would be exact zero fast paths, preserving scalar GMP rationals and every
node, source and prefix. n0_replay allocated one CPU slot while two producer
runs occupied other slots. Measurements are serial, not parallel. No
symmetry, support orbit, source reduction or representation change is used.
For any exact zero operand, `a*0=0` and `s+0=s` in Q; the pilot skips only
that multiplication/update after testing the actual stored scalar. Every
dot product still visits every original node, all Gram pairs remain checked,
and every source/prefix contributes its original nonzero energy. This is
ordinary redundant arithmetic removal, not a mathematical reduction.

## Pilot artifacts

`code/p6_speed_profile.cpp` copies the original scalar checker and adds only
three stderr phase timers. `code/p6_speed_scalar.cpp` additionally skips
known-zero products in weighted dot, projection, frozen responses, energy
and projector diagonal. It retains canonical per-entry mpq arithmetic.
Both retain all original guards, pivot tie policy, endpoints and JSON fields.
These are experimental comparison sources, **not an accepted replacement**.

Compile commands actually executed from repository root:

```sh
g++ -O3 -std=c++17 topics/padua-lanczos-nonproduct-20261105/code/p6_speed_profile.cpp -lgmpxx -lgmp -o /tmp/padua-lanczos-nonproduct-20261105/p6-speed/profile
g++ -O3 -std=c++17 topics/padua-lanczos-nonproduct-20261105/code/p6_speed_scalar.cpp -lgmpxx -lgmp -o /tmp/padua-lanczos-nonproduct-20261105/p6-speed/zero
```

Executed subprocess argv, wall times, source/input hashes, output hashes,
phase times and equality results are recorded in `evidence/p6-speed-pilot.json`.
Each process had a Python subprocess timeout of 60 seconds, with stdout and
stderr redirected to the correspondingly named local artifacts. Exact row
comparison removes only `elapsed_seconds` and compares every other JSON
field; no endpoint-only subset is used. A preliminary BJ6 profile completed
in 1.168 seconds (basis .415622, sources .590725, finish .128168); its files
were then overwritten by the recorded paired repeat. `/usr/bin/time` was
unavailable; an attempted wrapper failed before executing the checker.

## Assessment

No material speedup was observed. All six paired comparisons exactly match
all JSON fields except timing: BJ/mirror/alt/pivot through degree6, and
BJ/pivot through degree8, with every original node/source and all prefixes.

| Degree cap | Rule | Original arithmetic + timers (s) | Zero fast paths (s) |
| --- | --- | ---: | ---: |
| 6 | BJ | 1.067 | 1.067 |
| 6 | mirror | 1.168 | 1.319 |
| 6 | alternating | 1.469 | 1.368 |
| 6 | pivot | 1.719 | 1.468 |
| 8 | BJ | 7.338 | 7.285 |
| 8 | pivot | 10.093 | 12.467 |

The degree8 BJ source phase is 4.914 versus 4.905 seconds, so skipping
zeros does not address the dominant scalar cost in this example. One
measurement per pairing cannot resolve small performance differences;
the data give no basis for expecting the required multi-fold gain at16.
These timings include concurrent producer activity on other allocated
cores and do not establish isolated-machine benchmarks.

The pilot variant is **not recommended** for successor use. Retain it as
an unsuccessful finite implementation comparison, not a new checker
validation claim. No degree16 variant run was executed. Existing original
scalar 3600-second followups remain valid and should proceed unchanged.

Potential bigger changes were inspected but not implemented: shared-vector
common denominators would lose the requested arithmetic-path independence;
modular certificates require additional exact reconstruction/height bounds;
orbit/parity reduction needs preregistration and distinct mathematical
review and was outside this bounded implementation pilot. None is claimed
impossible or tested. Small loop/weight-caching changes alone have no
measured basis for a substantial gain and were not pursued.

## Runs needed

No more speed-variant runs are recommended. Full degree16 exact comparison
remains the owning worker's original scalar-checker3600s followup; this
record neither executes nor certifies that pending work. Distinct-agent
inspection of this assessment may confirm its limited no-switch decision;
no downstream endpoint result relies on the new experimental source.
