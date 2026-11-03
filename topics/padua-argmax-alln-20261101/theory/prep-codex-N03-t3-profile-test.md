# PD-N083 (PD-N?argmax-alln-prep-codex-03) — Measured failure of the T3 raw angular corner-profile planning test

Final registration: **PD-N083**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-N.
Aliases: T3 raw angular profile drift;13×13corner-offset screen.
Split from: T3 portion of PD-T?argmax-alln-codex-01; original combined measured record retained.
Split into: none.

## Statement

At n16,64,256,on the registered13×13angular-offset grid,the raw corner profile lambda_n-Lambda_c has substantial finite degree dependence. At(xi,eta)=(.25,0),values are-.761788147,-1.445328813,-2.357884098; at(.5,.5),-5.176100973,-9.707866456,-15.912499857. This is the recorded measured KILL of the assumed n-independent raw-profile planning form,not a proof of nonconvergence. No off-origin sampled gap has magnitude<1e-6.

## Definitions

For these even degrees,use(theta,phi)=(xi*pi/n,pi-eta*pi/n)near the nonnode corner(0,pi);reflection represents |xi|,|eta|<=3 by xi,eta∈{0,.25,…,3}. The1e-6second-nearzero diagnostic is a dated finite operational choice; the original does-not-converge criterion has no finite tolerance.

## Assumptions

Float64 evaluation of the corrected kernel on the fixed3×169samples,no optimizer,outward bounds or unsampled-neighborhood guarantee. Angular offsets do not represent a Cartesian fixed-displacement profile. Additional n-dependent normalization would define a different candidate.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Finite raw-profile drift | MEASURED | No mathematical nonconvergence/divergence claim |
| No sampled second nearzero point | MEASURED | Only the registered grid; threshold1e-6 |

Candidate / claim disposition: **REJECTED: failed** for the stated finite screening/planning formulation.
Rejection reason: **failed**, supported by MEASURED evidence only; no exact universal negation is asserted.

## Negative-result scope

Attempted mechanism:the n-independent local raw angular-profile form of original Claude02/P3. Parameter range:even n16/64/256and the13×13offset grid,with the recorded diagnostic threshold only for a second nearzero sample. REJECTED:failed records the finite planning verdict; no finite tolerance is invented as a nonconvergence proof.

## Depends on

PD-T101 corrected kernel; [measured record](argmax-alln-codex-01-measured-tests.md),[test attempt](../attempts/T1-T5.md)and plan v2 §6. P3 strict corner inequality is a distinct target.

## Checks

Original command: `OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/part3/tests_T2_T3.py T3 <scratch>/tests_T3.json`. Source/rules snapshot328be35e55143013047ec03a70e9906e82b95353 with the preserved newline qualification in the attempt. Separate Astra high full T3 replay matched every non-time JSON field; [independent-checks-part3](../independent-checks-part3.md) and Claude audit-01 record accepted finite MEASURED coverage. No new numerical replay occurred during this rehoming.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Archived83,548B SHA256`964b22ae3d0dbf5f4bdc39cc57d6357a52beeba1beb3d16850c953ffceb5fc98`. At(1,1),the three gaps are-2.550325109,-3.615806036,-4.738611618. The nearest off-origin sample is(.25,0)at all3degrees. The exact origin has zero gap. Raw finite drift and absence of a sampled near-tie do not enclose the continuum.

## Scope

Only the original unnormalized angular-profile planning mechanism in the specified finite test. Neither a convergence theorem nor an exact counterexample to P3,PD-T099,normalized-profile variants or later local analytic bounds is asserted.

## Open items

Any new normalized-profile or all-degree comparison requires its own statement and evidence. The accepted eventual corner theorem remains separate; no additional research round is introduced.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
