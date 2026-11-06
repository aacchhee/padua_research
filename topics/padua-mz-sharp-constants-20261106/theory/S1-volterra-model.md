# PD-T?mz-sharp-codex-S1-01 — the logarithmic primitive model norm

ID kind: PD-T.
Aliases: reciprocal CC primitive model; half-wave ground state.
Split from: supporting model calculation for PD-T020, not a case of it.
Split into: none.

## Statement

On L²(0,1), let (Vf)(x)=integral_0^x f(s) ds. Then

    ||V||=2/pi,
    inf_(f nonzero) (pi²/2)||f||²/||Vf||²=pi⁴/8.

The infimum is attained at f(x)=cos(pi*x/2). The two-copy model
V direct-sum V has the same norm. Its antisymmetric subspace (f,−f)
also attains this norm. Thus imposing this antisymmetry does not change
the model coefficient.

## Definitions and assumptions

Real or complex L², Lebesgue dx, integral primitives with F(0)=0.
No condition is imposed on F(1). This is a continuum operator statement,
not an asymptotic statement about a finite CC Gram matrix.

## Status by part

Overall status: PROVED (analytic development; independent audit required).

| Part | Status | Evidence |
|---|---|---|
| Exact model norm and extremizer | PROVED | Elementary one-sided Poincare argument below |

Candidate disposition: retained supporting model calculation.

## Depends on

Only elementary integration and density of smooth functions in H¹.
No literature theorem is imported.

## Checks and sources

No numerical computation is needed or claimed. Source/rules2143ad6.
Developer requested gpt-6.1-sol xhigh; runtime model metadata unexposed.
The [gate](../novelty-gate-S1.md) records bounded predecessor coverage.

## Proof

Put F=Vf and a=pi/2. For smooth F vanishing at0, complete the square:

    integral_0^1 (F'−a*cot(a*x)*F)² dx
      = integral_0^1 |F'|² dx − a² integral_0^1 |F|² dx.

For complex F use real parts in the cross term. The boundary term is
−a[cot(a*x)|F|²]_0^1=0: cot(a)=0, while F(x)=O(x) at0.
The coefficient identity is (a*cot(ax))²+(a*cot(ax))'=−a².
Approximation extends the inequality to every H¹ F with F(0)=0
(or apply it first on [epsilon,1] and pass by H¹ approximation).
Consequently ||F||²<=(4/pi²)||F'||². Equality holds at F(x)=sin(ax),
whose derivative is a*cos(ax). This proves the exact norm and quotient.
Orthogonal direct sums preserve the norm, and (f,−f) attains it.

## Scope and open items

The result identifies the coefficient of this exact continuum model.
It neither identifies the true finite-N limit nor proves model transfer.
Those obligations remain in [S1-model](S1-model.md), with PD-T020 OPEN.

## History

2026-11-06: first written model calculation, after the S1 gate. The model
derivation is local, without a historical novelty claim.
