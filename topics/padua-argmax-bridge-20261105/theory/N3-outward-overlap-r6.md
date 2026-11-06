# N3 outward overlap calibration at degrees24 and32

Verification record; no new global result ID. These degrees already have
accepted native corner-argmax proofs. This validates the separate phase
route using PD-T364 and the existing mathematical/source reduction; it
does not change the all-degree target. Timing claims are MEASURED.

## Fixed instances and premises

Both MPFR producers use unchanged C/header interval arithmetic, a fresh
immutable build closure, first-order whole-sum bounds, exact outside
geometry and the accepted finite local patch:2<=n<=128, kappa>=1/16000,
phase-square1/128. The latter comes from the independently executed127
integer cases in independent-corner-range.json, fixed SHA e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0.
No candidate or caller can assert that premise. New checker code/data
guards are separately reviewed; they do not hash-pin prose.

## Actual complete outcomes

| n | Producer visits/leaves | Producer search CPU | Separate checker leaves | Checker CPU | Build/helper CPU | Exit |
|---|---:|---:|---:|---:|---:|---:|
|24|2036/1020|363.070|1020/1020|202.067842|1.164960|0|
|32|1980/992|619.326638|992/992|382.569138|1.093550|0|

Both have0failed/0pending, complete=true and checker accepted=true.
The producers remain accepted=false. Each ran once at its preregistered
parameters; no retry, internal rescue or modified arithmetic was used.
The checker used the reviewed Arb v2 via explicit round5 selection.
No producer bound or diagnostic number supplies checker acceptance.

Essential complete candidates: [n24](../evidence/n3-phase-n24-r6.json.gz)
(5070bytes), [n32](../evidence/n3-phase-n32-r6.json.gz) (4989bytes).
Plain SHA-256 respectively8c984dc87c9170ae07f106a530a7915596bca30f273371bb2de2f89c8443ec92
and1cedd123ca9bfb69c200036161c521b5cbe1fca8e7197c4dd5ec557b640fa234.
Projection removes only ignored numeric diagnostics; every tree/kind/degree/
geometry/provenance field is preserved. No splitting to evade size limits.

Acceptance receipts [n24](../evidence/phase-r6-n24.json) and
[n32](../evidence/phase-r6-n32.json) preserve exact argv, original input
snapshot, fresh source/binary/runtime closure, worker code/CPU cap, raw
identity, actual exit and all counts. Full diagnostics remain local and
regenerable. See [independent executions](../independent-checks-phase-r6.md),
[premise review](../independent-checks-phase-r6-premise.md), and
[producer inventory](../evidence/n3-r6-producer.json). The essential
inputs/checker and short acceptance evidence are committed. Trusted
components are the inherited reduction, checked source, compiler, Arb/FLINT
and GMP outward arithmetic and elementary functions, plus Python parsing.

## Interpretation and limits

This is now a three-degree known-range validation ladder17/24/32.
Historical n17 used only the much smaller inherited patch, so its1288
leaves/109.45checkerCPU-s cannot establish an unchanged-design growth law
against these larger-patch instances. The matched24/32 pair has decreasing
leaf counts; two cases are not an all-n complexity law. Original B2's
finite floating33/64/128 pass remains separate. No new n33+ phase-route
certificate, effective onset, B3 pass or B4 release is inferred.

The new fixed-range premise is not extended beyond128. The per-degree
local theorem is pointwise, so no bootstrap/max-principle premise is used
in these two acceptance runs. A separately gated maximum-bootstrap idea
may change the local cover reduction later; it is not retroactively part
of these certificates. Required Claude audit remains separate.

2026-11-06, producer requested Sol medium; distinct checker Sol medium and
focused premise/math reviewer Astra high. Serving metadata unexposed.
