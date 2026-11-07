# D03 near-only pilot: independent pre-execution source review

2026-11-06. Rules/input commit `f1ba23cfbfb557dd491730f9837f5efe413e7c75`.
Distinct Codex technical/source reviewer, requested `gpt-6-astra`, medium
(parent-confirmed allocation); serving model metadata is not exposed. This supplements,
and does not replace, the cross-family audit handoff.

**Verdict: PASS for the bounded floating pilot's source/domain contract at the
final hashes below. No pilot, native build, or board evaluation was executed by
this reviewer.** Root retains execution authority. This is neither a numerical
validation nor approval of an exact certificate, all-degree claim, or projected
throughput.

## Scope and frozen inputs

Technical-only novelty-gate exception: this review checks implementation of an
already specified finite measurement, inherited API, resource supervision and
use of an existing theorem. It proposes no mathematical mechanism, assigns no
novelty/duplicate classification, and makes no negative mathematical claim.
Consequently the full IDEAS novelty audit is outside this review.

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md; full pilot SPEC and
driver; full unchanged n3_float_v3.py, n3_meanvalue.c, box_pilot.c,
phase_probe.c; full PD-T369 corner-n2-local-radius.md; SOURCES.json.

| Reviewed artifact | SHA-256 |
|---|---|
| final pilot.py | `32c6940afc45023b6a9c9082f59586db77634d31f3bad8301e4698269737c1e9` |
| final SPEC.md | `3d6284e5be463a93014e0da92f42e506b535aea83f810d19ea6371b8b4496cd1` |
| final SOURCES.json | `f2c23f946f873cec3233f1c0542be242e1b2e63a6e3a6a02b3a01f670a59d3a9` |
| n3_meanvalue.c | `4739e36d05d75ce4389118364a2e2a693d2b14d87a8b79e84aa5199d6bb6a86a` |
| phase_probe.c | `692d4afd89d3bbda3bac3daaeef7c56aa4ecdde0f9cdd32b9fefa0e296adc365` |
| box_pilot.c | `92f111e0c58c59de32490118a30d88b26de356a93e0ec7251928059e1f2f4d0b` |

Initial driver candidate `70b11d63b0bb2dc666fe6304970acf9cd62e9377813bac9762abc5efae3bedb8`
was not cleared; its unexecuted freeze is retained in the source inventory.
The author, not this reviewer, made the fixes below.

## Findings and disposition

1. **MAJOR, resolved:** initial launch polled termination before draining PIPE
   output. Sufficient compiler/helper output can block indefinitely without
   increasing child CPU. Final launch sends both streams directly to files and
   adds the documented fixed command wall deadline. A separately executed
   one-MiB Python-output test of the extracted final launch function completed.
2. **MAJOR, resolved:** initial control references were not checked for NaN or
   infinity; a NaN violation bypassed `violation > tolerance`. Final driver
   checks corner references, point references, comparison differences and
   margins for finiteness, and rejects nonpositive corner reference/epsilon.
   Four separately injected NaN reference positions now raise RuntimeError.
3. **MAJOR, resolved:** initial checkpoint write truncated the previous JSON
   before completing its replacement, contrary to hard-stop retention. Final
   save writes a temporary file and atomically replaces the old file, with
   nonfinite JSON forbidden. Failed serialization preserved prior valid JSON
   in the focused test. This is process-kill retention, not power-loss durability.

4. **MINOR, resolved (root observation):** the board has O(n²) entries/kernel
   calls, but rp() can perform O(n) fallback work per entry, so total board
   arithmetic need not be O(n²). The author added a dated SPEC qualifier;
   profile loops remain separately O(n³). This is wording only; driver bytes
   and reviewed execution contract are unchanged.

No unresolved MAJOR/BLOCKING technical finding at the final source hash.

## Domain, API and scheduling checks

The four signed quadrant roots cover [-rho,rho]^2 for rho=1/2 and1/8. Strict
minabs-sum exclusion leaves diamond boundary boxes included. Whole-box bounds
on straddling boxes are conservative for domain coverage only; ordinary double
arithmetic remains nonrigorous. Breadth-first, longest-side/alpha-tie splitting,
lower child first and128 visited boxes match the specified schedule. The two
cases remain fixed at n512, half before eighth; no extra degree or retry is added.

PD-T369 applies for every integer n>=2 at both parity-correct nonnode corners.
The rational guard evaluates a^2/(2n^2)+b^2/(2(n+1)^2)<=1/(10^11 n^2)
exactly on binary endpoint rationals. The cosine inequality gives a sufficient
physical inward-radius bound for either sign. Zero phase is equality, not a
strict descent assertion. This does not transfer the old n128 phase patch or
extend a loss coefficient outside its radius. The local branch still requires
the separate noncorner-defect comparison.

The ctypes signature matches the six-double-output kernel. The wrapper retains
all six outputs and explicitly records the profile flag. Early return with zero
defect/profile is not treated as a measured positive defect. Its acceptance
order matches the inherited predicates; epsilon is only a floating diagnostic
cushion. Point controls compare separately implemented sums at the registered
three n32 points, not a degree certificate or interval proof.

The structural checker reconstructs rational root/path geometry, rejects
prefix overlaps, missing siblings/roots and duplicates, and rechecks strict
outside-near exclusions. It checks geometry only, not bound correctness. Its
separate CPU field and null exact-checker CPU avoid a throughput projection.

Final supervisor counts live process-group CPU plus waited-child/self usage;
compiler and helpers are inside the aggregate budget. The1790 safety trigger,
1800 total contract,60/10/10/60 helper caps,720 case soft stop,739/740 worker
limits and750 supervisor cap are explicit. A single native call is checked
against60 CPU seconds after it completes, as specified; it is not asynchronously
interrupted at60. The fixed wall deadline is an additional stop. Checkpoints
retain the uncomputed current box if killed within native work. A kill before
the first checkpoint has no completed partition to preserve.

Source pins cover the unchanged C closure; -MD records compilation headers
(the last translation unit includes math.h, the first unit's sole include).
The runtime records hash the executable, imported module files and mapped
shared objects, including the built library. These are planned provenance
records until execution; no observed compiler format, binary, loaded closure,
numerical consistency or measured CPU is asserted by this review. Parent should
verify the runtime manifests if the pilot is run. Existing preregistration
refuses rerun; worker entry points are internal to that registered invocation.

## Actually executed independent checks

Only AST-extracted pure-Python functions and tiny Python child processes were
executed, without importing/executing the full pilot module or loading native
code. Local scratch commands:

- `python3 /tmp/D03_pilot_review/check.py`: two valid quadrant partitions,
  eight rejected corruptions (missing root, duplicate, geometry mismatch,
  invalid outside-near), three H3 guards; initial NaN-expression loophole and
  generic undrained-pipe blockage reproduced. Structural function snapshot
  `2713294ae5c2b6915f81c49c0b38c21c3609fd38f834fd55a5281fe017c221a4`
  was an intermediate author revision; those functions are unchanged in final.
  Aggregate test CPU0.058324 seconds.
- `python3 /tmp/D03_pilot_review/focused.py`: final source hash above; one-MiB
  direct-file output, NaN/infinity guards, four NaN reference injections and
  previous-JSON retention after failed serialization all passed. Aggregate
  test CPU0.075647 seconds.

Combined test CPU0.133971 seconds, below the delegated10-second allowance.
The five SOURCES.json code identities were independently recomputed and match
current bytes. Scratch tests are supplemental implementation checks, not numerical evidence.
No Git mutation, author-file edit, pilot invocation or native build was done.
