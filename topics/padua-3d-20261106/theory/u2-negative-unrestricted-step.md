# PD-N?padua-3d-20261106-codex-U2-01 — unrestricted U2-SN fails its pilot gate

ID kind: PD-N. Aliases: U2-SN first-trial collision; singular-penalty stop.
Split from: none. Split into: none.

## Statement

For the exact frozen U2-SN pilot at n2,4,6,8, its n6 and n8 outputs
equal the inherited localdet start. They fail the preregistered requirement
of at least5% fresh refined improvement at both n6/8. Thus this fixed
algorithm fails its finite practical extension gate. No all-method or
asymptotic impossibility is asserted.

## Definitions / assumptions

U2-SN and the assessment grids, seeds, starts, fallback, cost and quality
gates are exactly [usable2](../usable2.md), published at
fe23e002f25912b2ca2a09b225e385f596f824fe before execution. A singular
trial returns objective1e100 with zero gradient, as the frozen source
specifies. This penalty behavior is part of the tested implementation.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / limit |
|---|---|---|
| Fixed-rule finite quality gate failure and recorded collision trace | MEASURED | Pilot and separately executed diagnosis |
| Failure of every direct norm optimizer or all-degree quality | OPEN, outside statement | Not tested or inferred |

Candidate disposition: **REJECTED: failed** within this finite operational
gate. The isolated n4 gain remains in the separate measured home.

## Negative-result scope

Attempted mechanism: IDEA?padua-3d-20261106-codex-U2-01, the named
one-start unrestricted L-BFGS-B/zero-gradient singular-penalty update
from the unchanged one-sweep localdet set. Parameter scope: n2,4,6,8;
extension criterion only at n6/8. No n10/12 execution occurred. Changing
the update requires a new prospective record, not a reinterpretation of
this failure.

## Depends on / sources

[Pilot receipt](../evidence/u2-pilot.json),
[executed diagnosis](../evidence/u2-diagnosis.json),
[measured home](u2-sampled-norm.md). Established direct norm minimization
is attributed in the shared gate; no source theorem supplies this negative.

## Checks / evidence

At n6/8 the fresh refined values are17.669649678/24.124150806 for both
localdet and U2-SN. The frozen gradient check passes at5.838e-10.
Diagnosis reads actual saved trial coordinates rather than inferring
stationarity from a success flag:

| n | initial projected gradient inf | next-trial unique/N | max physical displacement | final observed termination |
|---:|---:|---:|---:|---|
|2|1.000000|9/10|1.000000|relative reduction, one iteration|
|6|2.000000|68/84|2.000000|relative reduction, one iteration|
|8|2.000000|129/165|2.000000|relative reduction, one iteration|

Each second evaluation raises `Singular matrix`; the third returns to
the identical initial coordinates. A positive projected gradient at that
initial point means the trace is not evidence of constrained stationarity.
The registered fallback preserves the valid starting set. Only the
specified numerical update has failed; the objective and broader direct
optimization route remain available for a changed, gated rule.

The first execution also hit the receipt size guard; its sources and
partial output are preserved. A serialization-only repair followed by a
whole fresh rerun reproduced the same scientific outcomes. The diagnosis
receipt records both raw identities and the exact executable command.
Independent supplementary execution remains separate.

## Scope / open items

This is a finite measured failure. No conclusion about a true local or
global optimum, the norm asymptotics, every bounded update, or an entire
point-set class follows. U2-AB is a separate prospective update based on
the actual training collision trace; it cannot retrospectively erase
this rule's failed gate. Exact continuous norm enclosure remains open.

## History

2026-11-07, Codex U2 developer, assigned gpt-6.1-sol xhigh; runtime
metadata not independently exposed. Rules3822720. R1 result from the
published protocol; no final ID allocated and no shared record edited.
