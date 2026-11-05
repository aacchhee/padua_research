# N3 round 2 — corner-patch and bounded outward observations

ID kind: provisional PD-T measurement record; no global ID assigned.
Aliases: N3 B2 finite float schedule with aggregate corner patch.
Split from/into: none; PD-T099 remains OPEN.

## Statement and scope

At n33/64/128 the unchanged first-order floating kernel completed all three
phase-cover searches using the local phase square |alpha|,|beta|<=1/128,
with respectively 2028/1908/1794 visited boxes and 12.22/47.46/162.65 CPU
seconds. Counts decrease across the three measured degrees. This satisfies
the finite float timing/count components of B2 in the stated test, not a
universal count-growth law or a validated numerical phase cover.

The execution began as explicitly conditional on the corner square. The
initial independent exact GMP replay reported that premise for all three
degrees, and an input-impact guard checked its exact interface and frozen
identities. Before publication the coordinator found an uncanonicalized
rational constructor in that checker and temporarily put the premise on HOLD.
The distinct owner fixed it and actually rebuilt/reran n2/33/64/128; all raw
outputs were byte-identical to the withdrawn run. **Current premise status is
restored PASS** under corrected receipt SHA-256
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`.
The first guard receipt
is preserved as `n3-round2-impact-initial.json`, tied only to those initial
hashes. `n3-round2-impact.json` records the successful corrected verification,
using receipt schema v2 and explicitly rejecting the initial checker hash.
The original conditional float receipt and timings remain unchanged; no
mathematical rerun is needed merely for corrected checker hashes. Even after
the premise is verified, floating arithmetic remains MEASURED.

## Status and dependencies

Overall status: **MEASURED** finite observations only. The helper's corner
reduction and independently verified finite energy bounds retain their own
statuses in N3-corner-radius-reduction.md and N3-corner-bounds.md. PD-T364
is the sufficient cover theorem. This record is not an accepted per-degree
instance of that theorem because its numerical enclosures are floating.

## Evidence and diagnostics

- `../evidence/n3-float-v2.json`: unchanged kernel, larger patch only;
  600 CPU-second caps, one-million visit cap, all three covers complete.
- `../evidence/n3-round2-impact.json`: premise/identity verification after
  different-agent corner acceptance; no repeat mathematical execution.
- `../evidence/n3-frontier-diagnosis.json`: all 344 old n128 pending boxes
  lie inside the proposed dyadic patch by exact rational endpoint comparison.
  Their largest absolute phase is about .0004792; floating H/old-radius ratios
  range 1.56–122.0. Eight sampled point-box upper bounds differ from stable
  sinc point values by up to .4884. This reflects point-enclosure/chart
  behavior in addition to box widths; no universal causal claim is made.
- `../evidence/n3-outward-bounded.json`: n17/24/32, each 32 visits and 31
  pending prefixes, with one outside leaf. CPU times 7.53/9.44/14.31 seconds.
  Separate narrow far, defect and local-corner leaves have complete prefix
  accounting with pending siblings and remain producer-unaccepted.

The independent phase checker uses a distinct arithmetic/formula path and
owns its acceptance/control records. No complete outward cover, new finite
global degree or all-degree onset is claimed here. A prematurely launched
duplicate v3 float campaign was terminated before any degree completed; it
supplies no result and is retained only as an execution-history note.

## Next obligation

Validate narrow arithmetic leaves and corruption controls on the independent
phase path, then choose a bounded full outward pilot using the verified corner
patch. Optimize measured arithmetic bottlenecks before an hours-long run.
No first-order growth/radius kill or second-order escalation has been inferred
from round 1's partial frontier. No source theorem is imported.

History: 2026-11-05, Codex requested Sol medium, serving metadata not exposed;
rules/input 3dda890275a7599caa707b0fb8c0b6e6f6a80643. Round 1 remains frozen
at that commit. Independent corner acceptance is attributed to /root/check_rows.
