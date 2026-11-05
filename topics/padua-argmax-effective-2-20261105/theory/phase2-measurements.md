# PD-T370 (PD-T?argmax-effective-2-codex-08) — Finite phase, projection and capped-box measurements

ID kind: PD-T (provisional T08; registration proposed, no final ID assigned).
Aliases: phase-2 finite diagnostics; A1 capped pilot; A2 all-center projection samples.
Split from: the already recorded measurements in `../phase-probe.md`,
`../projection-probe.md` and `../box-pilot.md`; no mathematical target is narrowed.
Split into: none. Analytic results and the OPEN PD-T099 target remain separate.

## Statement

Under the corrected even-checkerboard Padua convention of PD-T101, the
following observations were obtained in the existing deterministic
floating-point runs. This file transcribes their accepted finite scope;
it records no new measurement or status.

1. **Phase probe:** at n=17,32,48,64,96,128,192,256, each degree used
   19 odd centers, 49 distinct phases and 655 physically admissible
   center/phase samples. The largest sampled S−Λ_c values are respectively
   about 2.68456·10^-4, 1.03911·10^-4, 7.99764·10^-5, 4.76682·10^-5,
   1.50859·10^-5, −3.55·10^-15, −1.78·10^-14 and 4.26·10^-14.
   Across the full probe, sampled λ−Λ_c never exceeds 5.7·10^-14.
   These residuals have no rigorous error bound and establish no sign
   near zero, continuous maximum or counterexample.
2. **Projection probe:** all physically admissible odd centers were
   enumerated at the same 49 phases for n=48,96,192, giving respectively
   58,255, 229,399 and 910,375 center/phase samples (1,198,029 total).
   The smallest sampled noncorner values of
   max(Q_h,Q_v)−(S−Λ_c) were approximately 0.566547, 0.557083 and
   0.552633. These are sampled margins only, not lower bounds over a
   continuous phase region.
3. **Box pilot:** the original natural-interval, breadth-first run at
   n=17,32,64,128,256 stopped at 2000 visited boxes or 60 process-CPU
   seconds per degree, whichever came first. Every cover was INCOMPLETE.
   Its recorded visits and unresolved frontiers are:

   | n | Visited boxes | Unresolved frontier | Stop |
   |---|---:|---:|---|
   | 17 | 2000 | 880 | box cap |
   | 32 | 2000 | 902 | box cap |
   | 64 | 2000 | 774 | box cap |
   | 128 | 2000 | 802 | box cap |
   | 256 | 802 | 308 | CPU cap |

   No degree completed even its floating cover. Partial accepted leaves
   provide neither an A1 pass nor the original growth-law kill, an exact
   runtime projection or a certified finite degree.

## Definitions

Write m=n+1. Λ_c is λ at a nonnode corner; S is the full odd-torus
primitive; Δ=S−λ is the full reflection defect. Q_h and Q_v are the
projected pair-defect quantities from PD-T215/223 and
`phase-structure.md`; their analytic inequalities are separate from
floating evaluations. The phase radius is ρ=|α|+|β|.

The 49 phases use radii 0,.01,.03,.06,.1,.2,.3 on both signed axes and
four signed diagonals. Physical-angle admissibility restricts center
and phase pairs. The phase probe samples corner, edge, near-corner
interior and central classes; the projection probe exhausts admissible
centers only at those prescribed phases. Exact selection rules are in
the three source records and their committed producers.

The pilot starts from four closed quadrants of [−π,π]², uses
longest-side breadth-first bisection and retains every unresolved
rectangle at the cap. It uses ε=10^-10(1+Λ_c) as a diagnostic budget,
the universal H3 radius 10^-11/n², and the constant 1/8192 in its
n≥48, ρ≤1/10 branch. That branch substitutes the constant for the
projected-profile bound rather than taking their maximum. No measured
energy radius enlargement is used.

## Assumptions

The original runs use Python 3.12.14, NumPy 2.3.5, ordinary double
arithmetic and cc 14.2.0, on the Linux platform recorded in the receipts.
There is no random seed because schedules and inputs are deterministic.
There is no directed rounding or certified trigonometric error bound.
The pilot's CPU cap, timings and CPU-stopped frontier depend on hardware
and load; they are not portable cost guarantees.

## Status by part

Overall status: **MEASURED**, unchanged from the original source records.

| Part | Status | Evidence / limits |
|---|---|---|
| Finite phase observations | MEASURED | Eight listed degrees and finite samples only |
| Finite all-center projection observations | MEASURED | Three listed degrees, all admissible centers at 49 phases each |
| Capped pilot implementation outcome | MEASURED | Every cover incomplete; no outward error control or exact checker |

Candidate disposition: H1 remains retained/OPEN; the cap is not a
failed-mechanism theorem or a new PD-N. No substantive analytic result
is relabeled by this measurement record.

## Depends on

- PD-T101 and PD-T215/216/223 for the mathematical conventions and
  quantities evaluated; their proofs are separate.
- T01 for the phase-cover specification, T04 for the analytic defect
  constant, and T07 for the universal corner predicate used by the
  floating implementation. These dependencies do not certify floating
  arithmetic or complete the pilot's uncovered regions.
- Predecessors: [PD-T232](../../padua-argmax-alln-20261101/theory/prep-codex-01-d1-phase-defect-screen.md)
  and [PD-T247](../../padua-argmax-effective-20261103/theory/argmax-effective-codex-02-gate-measurements.md)
  are earlier finite phase/defect screens. [PD-T233](../../padua-argmax-alln-20261101/theory/prep-codex-02-d2-corner-screen.md)
  is the separate finite energy-screen predecessor to T05; this T08
  record does not rehome or rerun its energy measurements.

## Checks

Original commands, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/phase_probe.py
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/projection_probe.py
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/box_pilot.py
```

The projection and box scripts import `phase_probe` from their own
directory and must run without `-I`. They write receipts as well as raw
outputs; independent reruns should use a disposable checkout and retain
their own outputs. This response did not execute these commands.

The compact receipts
[phase-probe.json](../evidence/phase-probe.json),
[projection-probe.json](../evidence/projection-probe.json) and
[box-pilot.json](../evidence/box-pilot.json) pin commands, source hashes,
input identities, versions, finite counts, timings and raw output hashes.
Their accepted scientific bytes are in audited input
`352daad8c164617331c34ae81a7ce7331f501bb9`; audit-01 confirms equality
with enclosing source `7d394fd`. The producer files are `phase_probe.py/.c`,
`projection_probe.py/.c` and `box_pilot.py/.c` under `../code/`.

Developer cross-formula checks used the direct cosine polynomial:
71 phase-validation points at n=3,4,5,6,17,32; 262 projection checks at
n=3,4,5,6,17; and 412 box comparisons at n=3,4,5,6,17. These are
developer numerical validations, not separate-agent rigorous checkers.

Claude [audit-01](../audit-01.md), “Runs executed by this audit,” records
separate executed reruns and accepts the observations as MEASURED.
Phase/projection scientific fields and the first four pilot outcomes
agree. Its n=256 CPU cap instead stopped at 543 visits and 213
unresolved boxes; both runs remain incomplete. The original receipt's
802/308 outcome is preserved, with its hardware-dependent scope.

## Sources

No external theorem or literature priority claim. This is the durable
record requested by audit-01 F6, following the earlier PD-T232/233
rehoming pattern. Internal source reports do not become proof premises.

## Proof or evidence

Evidence consists of the unchanged compact receipts and source records
linked above. Raw artifacts, byte identities and current retention
state are in [COLD_STORAGE.md](../COLD_STORAGE.md) and
[cold-storage.json](../cold-storage.json). A local file or receipt hash
does not establish delivery to AC's cold storage. No proof of numerical
enclosure or independent exact phase-box checker is claimed.

## Scope

Only the recorded finite observations and capped implementation
outcomes. No global C, full-diamond remainder, continuum defect bound,
effective N1, complete-cover cost law or new global certificate follows.
PD-T099 remains OPEN; the certified global range stays exactly 2–32.
T03–T07 keep their separate accepted analytic statuses.

## Open items

Validated phase-box predicates, a complete cover, an independent
checker and its corruption controls remain future H1 work. The
full-diamond H2 profile and effective bridge remain OPEN. No new run is
requested or represented as completed by this record transcription.
The optional degree-40 cross-check was not attempted.

## History

2026-11-05, Codex response worker, AC-requested gpt-6-astra ultra for
wording and attribution; serving metadata not independently exposed.
Response input `183abfc9864444870cbc0b18e1e6601bd756dc0a`.
Created for audit-01 F6 from the three already accepted MEASURED records.
No new statement beyond those finite observations, proof step, constant,
scientific status, code, evidence payload or execution was introduced.
Final registration is proposed only in `../proposed-record-changes.md`.

## Registration — 2026-11-05

Final ID: **PD-T370**. Preserved provisional alias: `PD-T?argmax-effective-2-codex-08`.
Registration input/rules: `5821c3f130ec0b1e33ad1d01620b67620e1f0be1`.

Only the already accepted finite phase/projection observations and INCOMPLETE capped-box pilot are registered. This supplies no continuous bound, new certified degree, A1 pass/kill, inferred global constant or analytic proof dependency.

[Claude audit-01](../audit-01.md) accepted the mathematical scope;
[response-check-01](../response-check-01.md) accepted the record response.
Earlier provisional/no-final-ID and pending-response-check wording above
is retained as history and is superseded only administratively by this
registration. Every pre-existing paragraph after the heading, including
Statement, proof, status, displays and History, is preserved byte for byte.
The [final-ID map](../preparation/final-id-map.json) and
[registration notes](../preparation/registration-notes.md) record the mapping
and preparation limits. PD-T099 remains OPEN; the global certified range
remains exactly 2–32.
