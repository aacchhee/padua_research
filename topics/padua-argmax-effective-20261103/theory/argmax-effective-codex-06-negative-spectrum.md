# PD-N084 — Complete corner-active spectral positivity fails

ID kind: PD-N.
Aliases: R6 all-positive cosine coefficients; corner-active spectral majorant. PD-N?argmax-effective-codex-06a.
Split from: R6 initial coefficientwise-positivity candidate.
Split into: the retained positive mixed spectrum is PD-T250.

## Statement

For the canonical inward corner-active polynomial defined in
PD-T250, complete nonnegativity of its transformed
Chebyshev coefficients fails. In degree n=3 its nonconstant coefficient is

    C_01=(1-2*sqrt(2))/6 < 0.

Thus the proposed sufficient proof step asserting all C_ab>=0, even
after ignoring the constant term, is false.

## Definitions and assumptions

Exactly the canonical zero-row signs and corrected kernel of codex-06a;
degree n=3. This concerns the signed polynomial P_n, not lambda itself.

## Status by part

Overall status: **PROVED**. [Supplementary independent reconstruction](../independent-math-checks-01.md)
is complete and accepted; Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Negative nonconstant coefficient at n=3 | PROVED | Exact substitution below |

Candidate disposition: **REJECTED: refuted** for complete coefficientwise
positivity. The mixed-spectrum variant is retained separately.

## Negative-result scope

Attempted mechanism: R6 all-positive transformed spectrum as a sufficient
local comparison step. Parameter range: its universal n>=2 claim,
refuted at the single degree n=3. No obstruction to mixed positivity,
grouped coefficients, local comparison or global PD-T099 follows.

## Depends on

PD-T250 exact coefficient formula, derived from
PD-T101 and PD-T227.

## Proof or evidence

Insert n=3, m=4, b=1 into the C_0b formula:

    C_01=(1/6)*[2/(1+cos(pi/4))-3]
         =(1/6)*[4-2*sqrt(2)-3].

Since sqrt(2)>1, this is strictly negative. QED.

## Checks and sources

Exact symbolic arithmetic and the displayed analytic calculation; no
floating output is a proof premise and no external source is used.

## Scope and open items

The actual corner comparison remains open on the fixed phase zone.
The retained codex-06a/06b positivity after row/column grouping proves
all-degree negative corner slopes despite this negative coefficient.

## History

2026-11-03, Codex gpt-6-astra ultra, rules/input
8a1f394739293953e1566fd24a0a193cc78ff26f. Failed initial candidate retained;
no change to the all-degree global conjecture.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
