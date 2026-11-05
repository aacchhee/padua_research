# PD-T?lanczos-nonproduct-codex-P6-02 — finite interval growth screens

ID kind: PD-T (provisional). Aliases: new-plan N2 endpoint reanalysis.
Split from: P6 finite scans; their endpoint evidence is P6-01.
Split into: none.

## Statement

Under the coordinator's unchanged preregistered N2 convention, both the
inherited uniform T24 scan and the fresh H24_222 scan give **INCONCLUSIVE**
finite interval screens. The deterministic least-squares slopes of
log(kappa_BJ/min_R kappa_R) against degree, with R ranging over BJ,mirror,
alternating,pivot, have the following certified enclosures from the computed
capacity endpoint intervals:

| Family / provenance | Degrees8–12 | Degrees12–16 | Verdict |
|---|---|---|---|
| T24 / inherited PD-T338 | [.1373737422163122,1.8023568778512298] | [-.2164776234101806,1.8228133707405016] | INCONCLUSIVE |
| H24_222 / fresh complete two-path2–16 | [.05530690191334968,1.5395035055842174] | [-.22020241645825334,1.651201929678248] | INCONCLUSIVE |

Displayed decimals are approximate summaries; exact rational outward bounds
in the receipts are authoritative. Neither family passes both lower slopes
>.1; neither has both upper slopes<.02. INCONCLUSIVE is not a family
rejection, an asymptotic result or a polynomial-bound proof.

## Definitions

For each stage, P4-02 yields rational squared capacity endpoints L_R²,U_R².
Use q^-=L_BJ²/min_R U_R² and q^+=U_BJ²/min_R L_R². The logratio is enclosed
by [log(q^-)/2,log(q^+)/2]. The comparator includes all four rules as in
this topic's plan, including BJ. For a window, signed OLS coefficients
are (s−mean(s))/sum(s−mean(s))². Extremize each coefficient independently
at the appropriate interval endpoint. Windows are8–12 and12–16, sharing12.

## Assumptions

Complete exact all-source endpoint evidence for every degree8–16 and all
four rules, source/output model preserved, rational outward logarithms,
and the written family admission. Unknown true capacities remain bounded
objects; they are not numerically evaluated by this screen.

## Status by part

Overall status: MEASURED.

| Part | Status | Evidence |
|---|---|---|
| Two finite INCONCLUSIVE screen outcomes | MEASURED | Exact receipts and separate arithmetic algorithms |

## Depends on

P6-01 fresh weighted endpoint rows, inherited accepted PD-T338 T24 compact
log-enclosure evidence, P1 admission and P4-02. The new screen differs from
the historical PD-T338 universal interval kill predicate; no old verdict
is rewritten.

## Checks

T24: exact Fraction signed-OLS implementation and a separately reconstructed
plain-integer enumeration of all32 corners of each five-stage interval box
agree exactly. Logarithm enclosures are inherited, not freshly recomputed.
The source compact input has SHA256
`2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38`.

H24: the complete two-path scan receipt and all pinned raw endpoint outputs
are checked before logarithms. The unchanged accepted predecessor
`g1_fit.logq` and `g1_fit_independent.logq` independently compute outward
128-bit rational logarithms. Signed Fraction OLS and32-corner enumeration
using the second log path produce consistent enclosures and identical
threshold verdicts. These are actual separate arithmetic algorithms run
by one worker; distinct-agent review/rerun remains separate.

## Sources and evidence

No external source/priority claim. Frozen convention: `../plan.md` and
`../scan-methods.md`. Executed code/receipts:

- `../code/p6_n2_compact.py`, `../evidence/p6-n2-inherited-T24.json`.
- `../code/p6_n2_exact.py`, `../evidence/p6-n2-H24_222.json`.
- Raw H24 provenance: `../evidence/p6-full16-H24_222.json`.

The receipts contain exact commands, source/input/output hashes, precision,
comparator set and exact rational window enclosures. No prose hash is pinned
by a mathematical checker.

## Scope

Only these finite endpoint-box screens. Positive descriptive slopes do not
prove a rate; endpoint uncertainty can prevent a gate verdict. No claim is
made about exact capacities, their asymptotic growth, actual IEEE errors,
continuous-simplex transfer or every selection's stability.

## Open items

Disk16 scan and N2 screen; any useful tightening of broad capacity intervals;
distinct-agent reruns/audit. No new scan is required merely to duplicate the
inherited T24 evidence.

## History

2026-11-05, Codex technical developer, requested gpt-6.1-sol medium; serving
metadata not independently exposed. New-plan conventions and family
admission preceded execution. Full degree windows were checked before fits.
