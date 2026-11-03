# PD-N081 (PD-N?argmax-alln-prep-codex-01) — Measured failure of whole-diamond nearest-corner ordering screen

Final registration: **PD-N081**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-N.
Aliases: O-R numerical reversal;whole-diamond monotonicity screen.
Split from: the O-R portion of PD-T?argmax-alln-codex-06; retained original combined measured record is not deleted.
Split into: none.

## Statement

The existing float64 multistart O-R screen at n4,7,12 reports respectively6of10,16of42,and60of130nearest-corner neighbour comparisons reversing by more than10^-6. This crosses the chosen numerical kill threshold for pursuing that screened ordering. It does not prove the exact inequality between whole-diamond suprema fails,because an optimizer may miss a source maximum.

## Definitions

Use mesh coordinates(n theta/pi,(n+1)phi/pi),closed radius1 l1diamonds clipped to the square,neighbours differing by(±1,±1),and the same unique closest nonnode corner at both centres. O-R asks that whole-cell suprema not increase on steps farther from that corner. The definition differs from certified-list O-L/O-Lt and centreward-edge E-C.

## Assumptions

Float64 corrected-kernel evaluation; each diamond uses5×5rhombus-grid starts plus constrained Nelder–Mead from the best3,at most180iterations,with physical-square penalty. Numerical maxima are lower estimates,without outward error enclosures or an upper bound on the source supremum.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Threshold reversals in the recorded finite O-R screen | MEASURED | A missed source maximum can manufacture a reversal |

Candidate / claim disposition: **REJECTED: failed** for the stated finite screening/planning formulation.
Rejection reason: **failed**, supported by MEASURED evidence only; no exact universal negation is asserted.

## Negative-result scope

Attempted mechanism: IDEA?argmax-alln-codex-fallback-01,O-R whole-diamond unique-nearest-corner monotonicity. Parameter range:exactly the n4/7/12comparisons and stated float64 optimizer. Rejection is the finite numerical pursuit decision after reversals>10^-6; it is not a proof of the universal order's negation.

## Depends on

PD-T101 kernel; [measured pairing record](argmax-alln-codex-06-measured-pairing.md) and [pairing attempt](../attempts/P3-P5-and-pairing.md). No exact O-R obstruction is a dependency or conclusion.

## Checks

Original command: `OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/part3/pairing_screens.py --degrees 4 7 12 24 50 --output <scratch>/pairing_screens.json`. O-R ran only at4,7,12; n24/50arrays mean not run. Original source snapshot328be35e55143013047ec03a70e9906e82b95353. The existing measured record says no independent numerical replay at its publication; later Claude audit-01 accepts codex06 as MEASURED and reports its replay coverage. This preparation adds no numerical rerun.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Claude [audit-01](../audit-01.md) accepted the numerical claims at their recorded finite scopes; its F11 requested these durable homes. Historical payloads are pinned at source `1cecd68ac0a64b01ed7b2d262b6263a955a7d4d7` in [cold-storage.json](../cold-storage.json); retrieval is byte-exact, and the active integrity manifest must never be overwritten. Archived106,627B SHA256`f602acf48d82b91a26db422164836a4529828d027488f9f1b20e58497c8a93c2`. At n4,M_(3,0)-M_(4,1)≈.505255 using numerical maxima3.598293 and3.093038 away from corner(4,5). Interior-centre examples atn7have gains≈.226682 and.103182. These are sampled lower-value comparisons,not certified supremum reversals.

## Scope

Only the measured failure of this O-R screening formulation at4,7,12. It neither rejects ambiguous original IDEA03 nor any exact-list/edge ordering family or PD-T099.

## Open items

An exact O-R refutation would require an upper bound on the complete source diamond and a larger target lower bound. None is claimed here. Retain independent PROVED O-Lt and E-P obstructions separately.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
