# PD-T?argmax-bridge-codex-M2 — First-order floating phase-cover measurements

ID kind: PD-T. Aliases: whole-sum mean-value pilot; N3 round1 throughput.
Split from / into: none. This records a finite measured implementation.

## Statement, definitions and status

Overall status: **MEASURED**. The frozen N3 first-order diagnostic completed
its declared rectangle cover at n33 and n64, and retained an unresolved
frontier at n128's600-process-CPU-second cap:

| n | Visited | Split | Unresolved | CPU seconds | Maximum bisection depth |
|---|---:|---:|---:|---:|---:|
|33|2796|1396|0|16.368|29|
|64|3634|1815|0|92.966|41|
|128|5512|2926|344|600.140|51|

The implemented predicates are PD-T364's sufficient far/corner/defect
forms, evaluated with floating interval differentiation and a whole-sum
mean-value bound. Four reflected values/derivatives are summed before
absolute values. The initially zero terms use a symmetric derivative hull.
Corner-local leaves use the exact inherited domain
H<=max(1/(2[n(n+1)]^3),10^-11/n²), not an inferred true-sign radius.
The float receipt's shorter H3-only wording is corrected explicitly in
[attempt N3](../attempts/N3.md); its historical bytes are not rewritten.

## Assumptions and limits

Ordinary binary64 interval endpoints have no directed-rounding guarantee;
the diagnostic tolerance is not a rigorous error bound. A completed float
cover is not a computer-assisted maximum proof. A remaining frontier is
not a counterexample. No complete n128 count, empirical asymptotic growth
law, B2 pass or growth/radius kill is inferred from these capped data.

## Depends on and actual checks

PD-T101/364 for definitions/predicates, PD-T251/369 for their distinct
local domains, PD-T366 only within its n>=48 and rho<=.1 hypotheses.
[Enclosure derivation](N3-enclosure-spec.md), [gate](../novelty-gate-N3.md),
[frozen receipt](../evidence/n3-float-v1.json), and
[round1 source inventory](../evidence/n3-round1-freeze.json).
The receipt gives actual commands, source/input/raw hashes, environment,
caps, accepted predicate counts and complete unresolved frontiers.

Direct-polynomial derivative controls checked1296 scalar comparisons per
implementation against the finite kernel, including collisions/endpoints.
Those are developer formula diagnostics, not proof of interval validity
or independent checker acceptance. No outward full-cover run occurred.
The prospective outward code and its one-box calibration remain separate
development artifacts and supply no maximum theorem.

## Sources, scope and open items

This is an implementation variant of IDEA320/343/454; no external theorem
or novelty claim. The separate exact native Bernstein certificates have
their own proof record and checker receipts; they do not validate the new
phase-cover arithmetic. Raw traces/frontiers stay off Git with archival
transfer pending. B2 is incomplete until its complete three-degree scope
and the required outward/checker work are resolved.

## History

2026-11-05, measured implementation by Codex requested Sol medium; durable
record by coordinator requested Astra high. Serving metadata unexposed.
The N3 frozen first-round source/receipt hashes define the measured scope;
no scaling fit, new certified degree or continuous error claim is added.
