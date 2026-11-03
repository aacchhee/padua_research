# PD-N082 (PD-N?argmax-alln-prep-codex-02) — Measured failure of the T2 fixed interior raw-profile planning test

Final registration: **PD-N082**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-N.
Aliases: T2 raw-gap stabilization kill;9×9complementary-cell test.
Split from: T2 portion of PD-T?argmax-alln-codex-01; original combined measured record retained.
Split into: none.

## Statement

Under the fixed9×9macroscopic lattice/complementary-cell rounding and local-search convention below,32of81positions have |gap128-gap64|>.05. The largest recorded change is.382304500506 at the macro centre. Thus the registered finite stabilization criterion for pursuing the n-independent raw interior O(1)gap-profile form triggers. These finite observations do not prove nonconvergence or disprove the strict interior upper bound P4.

## Definitions

Positions are(a*pi/10,b*pi/10),a,b=1,…,9. At n32,64,128round to nearest complementary antinode j+k odd with the recorded tie rule. Search the half-mesh box using5×5phase-grid values{-1/2,-1/4,0,1/4,1/2}² and bounded Nelder–Mead(maxiter100,xatol1e-7,fatol1e-10),retaining rounded indices and phases. gap=Lambda_c-numerically found lambda maximum.

## Assumptions

NumPy/SciPy float64,finite grids and local optimization,no certified cell maximum or convergence-rate estimate. The original plan did not specify the lattice/rounding details; the2026-11-01dated operational convention was recorded separately rather than silently rewriting it.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 32finite threshold breaches | MEASURED | Registered>.05test at64→128; no divergence proof |

Candidate / claim disposition: **REJECTED: failed** for the stated finite screening/planning formulation.
Rejection reason: **failed**, supported by MEASURED evidence only; no exact universal negation is asserted.

## Negative-result scope

Attempted mechanism:the n-independent raw interior gap-profile form of original Claude02/P4,with registered stabilization threshold>.05fromn64to128. Parameter range:81fixed macroscopic positions and the exact n32/64/128cell convention. REJECTED:failed is the finite planning disposition; the all-n theorem remains unrefuted.

## Depends on

PD-T101 corrected kernel; [original measured record](argmax-alln-codex-01-measured-tests.md),[test attempt](../attempts/T1-T5.md),and plan v2 §6. The negative planning disposition concerns a raw-profile mechanism,not the OPEN PD-T099 target.

## Checks

Original command: `OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/part3/tests_T2_T3.py T2 <scratch>/tests_T2.json`. Source/rules snapshot328be35e55143013047ec03a70e9906e82b95353; source-newline and later-unused-helper qualifications remain in the attempt. Separate Astra high full T2 replay matched every non-time JSON field,as recorded in [independent-checks-part3](../independent-checks-part3.md). Claude audit-01 also accepts the finite scope. This preparation is record inspection only.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Archived69,566B SHA256`474a0aade64a06c2ec2976c40677189c93d369367bc3408482bdcf8fc40cb307`. At the centre the n32/64/128gaps are2.723873455357,3.098285732820,3.480590233326. Fixed zero-phase antinode gaps also change from3.103690474295 to3.484493175867 between64and128,so that central threshold breach is not solely the optimizer shift. Three-degree fits describe only those points; platform-sensitive least-squares leaves can differ by about5e-14,as disclosed in response-review-01N-a.

## Scope

The exact finite operational test and its measured failed criterion only. A larger gap supports rather than refutes P4 strict interior exclusion; no asymptotic/logarithmic growth theorem is inferred.

## Open items

General interior inequalities and effective thresholds require their separate analytic records. No new finite scan or attempt to prove nonconvergence is authorized by this disposition.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
