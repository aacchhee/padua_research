# PD-T?padua-3d-20261106-codex-D4-intervals — finite certified Lebesgue intervals

ID kind: PD-T. Aliases: C3; QR fallback enclosures; optimized n12 enclosure.
Split from: none. Split into: none.

## Statement and definitions

The following are whole-cube Lebesgue enclosures for total-degree
interpolation at the exact retained dyadic nodes. The QR family is the
fresh deterministic fallback specified by fd4_certify.py, not the missing
historical optimized sets. Every displayed decimal endpoint is rounded
OUTWARD to6 places from an exact Fraction endpoint. N=binom(n+3,3).

| n | N | QR lower | QR upper | exhaustive m2 mesh points | certificate seconds |
|---:|---:|---:|---:|---:|---:|
|4|35|11.244802|15.902765|729|0.0032|
|5|56|13.804602|19.523102|1331|0.0075|
|6|84|21.684824|30.668185|2197|0.0217|
|7|120|26.644954|37.684096|3375|0.0567|
|8|165|33.478157|47.350139|4913|0.1636|
|9|220|42.480005|60.086602|6859|0.4133|
|10|286|62.173106|87.947684|9261|0.9388|
|11|364|78.563560|111.141672|12167|2.0526|
|12|455|112.854819|159.677658|15625|4.1215|
|13|560|113.877971|161.151500|19683|8.6635|
|14|680|112.301049|158.962638|24389|16.5692|
|15|816|139.790531|197.902582|29791|28.4364|
|16|969|165.464514|234.340286|35937|53.6584|

For the **retained optimized n12/N455 set**, whose coordinate SHA256 is
1dbd239694d98bee67c861633e03c311c52496af745d8cd43e7bb584ef53c534,
the intersection of the two independently exhaustive mesh enclosures is

    25.961333 <= Lambda <= 29.062900.

The m2 enclosure alone is[25.961333,36.726474]
and the m3 enclosure alone is[25.161254,29.062900].
These meshes are not nested: the intersection uses the m2 lower bound
and m3 upper bound, not a monotonic-mesh claim. This certifies the
actual stored set, whose previous searched lower sample was about26.0073;
it does not certify that sample as the exact supremum or a global optimum.

## Status by part

Overall status: **PROVED with explicit LITERATURE dependency**,
computer-assisted finite enclosures. The [independent supplemental audit](../final-check-d4/audit.md)
completed every QR/n12 m2/m3 replay and its separate exact-rational,
integer and scalar-cosine checks. Formal Claude audit remains separate.
The local exact error/residual argument is in
[certificate-reduction.md](certificate-reduction.md); the only imported
continuum statement is Białas-Cież–Kenne–Sommariva–Vianello,
arXiv2311.18656v1, Lemma1/Proposition1 pp3–4, primary statement and
application checked by D5 in source-records.md. The external proof itself
is not locally verified. This label is never shortened to bare PROVED.
The independent rerun availability is recorded explicitly under Checks.

## Depends on

The exact reduction and the actual essential coordinate payloads
[fd4-qr-n4-nodes.json](../evidence/fd4-qr-n4-nodes.json) through
[fd4-qr-n16-nodes.json](../evidence/fd4-qr-n16-nodes.json), and the existing
[u2-degree12-nodes.json](../evidence/u2-degree12-nodes.json).
Each payload stores little-endian binary64 bytes losslessly as base85,
interpreted as exact dyadic coordinates. No proposed Vandermonde inverse,
QR rank decision or floating eigenvalue is trusted as an invertibility
proof: the exact bounded residual proves it.

## Checks and evidence

Round1 was published/pushed9cf64ef before execution. The complete commands
and frozen code identity7e1ff950b5d26338fb0cd9bbbdd7d4bb605001cd4f274c628b5dd28926fa8750
appear in [fd4-qr.json](../evidence/fd4-qr.json) and
[fd4-payload-m2.json](../evidence/fd4-payload-m2.json). Round2 n12m3 was
separately published/pushed0971807 before execution;
[fd4-payload-m3.json](../evidence/fd4-payload-m3.json) records its exact
command, all50653 mesh points, rational endpoints and elapsed13.2216s.
The m2 optimized-n12 run took5.2944s for15625 points. Largest QR
certificate cost was n16, within the120-wall-second per-set cap; no cap,
partial mesh, overflow rejection or inverse guard failure occurred.
Total QR construction+diagnostic+certificate time was138.8956s across13
sets; this is not a120-second aggregate cap. Times depend on this machine
and concurrent work. No random seed; BLAS/OpenMP threads requested1.

Independent checker: final_check_d4 separately executes every QR mesh and
the retained optimized-n12 m2/m3 meshes from the retained payloads, and
performs exact Fraction/Python-bigint controls, underflow-slack and
actual-range checks. Its receipts and final report are owned by that
worker; the final result must cite its completion record, not assume a
queued execution has completed. Producer receipt status strings retain
the chronology 'PENDING_INDEPENDENT_RERUN'; they are not rewritten after
later checks. Current completion is stated in the independent report.
Formal Claude handoff audit is still pending and is not claimed here.

## Scope, original target and limitations

The requested table on the topic's historical best optimized sets at
all n4..16 remains **OPEN** where those coordinates are absent. This
supporting fallback family does not turn that target PARTIAL. The actual
five absent source scratch paths and one retained optimized payload are
in [fd4-input-inventory.json](../evidence/fd4-input-inventory.json): a
MEASURED data-availability boundary, not mathematical infeasibility or a
claim of universal unrecoverability. Regeneration of the QR fallback was
actually attempted and completed at every requested degree; no existing
optimization campaign was reopened or extra rounds spent.

The intervals are for finite exact point sets, not all-degree quality,
optimality, asymptotic log³ growth or a Riesz-basis conclusion. The QR
basis order and floating pivot ties can change proposals on another
platform, which is why their exact payloads are retained. The stored
nodes, rather than a regeneration that changes the hash, define each
claim. The Gram diagnostics are separately MEASURED in
[gram-diagnostics.md](gram-diagnostics.md).

## History

2026-11-12, Codex assigned gpt-6.1-sol high; runtime identifier unexposed.
Rules04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b. D4 rounds1/2 and2/2
actually completed. No further D4 experiment is registered or authorized.
