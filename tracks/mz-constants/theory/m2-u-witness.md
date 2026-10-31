# PD-T?mz-constants-codex-23 — exact U endpoint witness

ID kind: PD-T.
Aliases: second-kind Chebyshev endpoint test; odd harmonic norm identity.
Split from: the original M2 endpoint target; this supporting result has its own substantive statement.
Split into: the eta counterexample is PD-N?mz-constants-codex-24; matching log-squared upper order is PD-T?mz-constants-codex-22.

## Statement

For each integer N≥2, U_(N−1) has the exact Lebesgue and CC square norms

    ∫[-1,1] U_(N−1)(x)² dx =2Σ_(j=1)^N 1/(2j−1),
    Q_N(U_(N−1)²)=2                      if N is odd,
                       2N²/(N²−1)       if N is even.

Therefore its quotient is at most an explicit constant times 1/log N. This witness alone does not give the matching log-squared upper bound.

## Definitions

CC conventions as in PD-T?mz-constants-codex-21. U_r(cosθ)=sin((r+1)θ)/sinθ, continuously at 0 and π. Set S_N=Σ_(j=1)^N(2j−1)^−1.

## Assumptions

N≥2 integer; unnormalized Lebesgue measure and N+1 Lobatto nodes.

## Status by part

Overall status: PROVED (development; independent acceptance pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact norm and quotient | PROVED | Polynomial identity and endpoint weights |

Candidate / claim disposition: active as a simpler supporting result.

## Depends on

Exact endpoint weights from the elementary telescoping calculation in PD-T?mz-constants-codex-21; no spectrum estimate.

## Checks

`python tracks/mz-constants/code/m2_endpoint.py --exact 512` executed 2026-10-31 at rules/base SHA d36722823441dc40c6e19d69a174459348dd309c. It produced Q=524288/262143 and RQ=0.24384880648700108, with the exact rational comparison RQ<1/4 true. Rational code is a diagnostic; the analytic proof supplies the theorem without a finite-check dependency. Code hash and environment in direction log.

Runs needed: independent exact replay and proof audit.

## Sources

The same witness is named in the supplied `cc_mz_large.py`. Its reported computation is not relied on; the identities are rederived here. No literature novelty claimed.

## Proof or evidence

The product identity U_r²=Σ_(s=0)^r U_(2s) follows by a finite trigonometric geometric sum. Also

    ∫[-1,1]U_(2s)(x) dx=∫_0^π sin((2s+1)θ)dθ=2/(2s+1).

Integration proves the norm formula. The interior nodal values vanish because sin(Nθ_k)=0. The endpoint values are N and (−1)^(N−1)N. The exact endpoint weights are 1/N² for odd N and 1/(N²−1) for even N, proving the discrete formula. Finally S_N≥(1/2)H_N≥(1/2)log(N+1), proving the asserted O(1/log N) quotient.

## Scope

This exact result is simpler than the harmonic witness, and suffices for the finite eta counterexample. It supplies no optimal endpoint rate or upper-spectrum conclusion.

## Open items

Independent adversarial acceptance and source attribution screen.

## History

2026-10-31, Codex subagent, gpt-6.1-sol xhigh (explicit orchestrator assignment); base/rules SHA above. Independently reconstructed from the polynomial identity.
