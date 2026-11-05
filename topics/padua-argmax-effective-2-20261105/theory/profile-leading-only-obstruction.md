# PD-N?argmax-effective-2-codex-01 — Leading phase factor alone has a divergent absolute error

ID kind: PD-N.
Aliases: omitted boundary logarithm; leading-factor-only profile obstruction.
Split from: the narrow trial profile in H2, not the unspecified original H2 target.
Split into: none. The positive boundary formula has its own PD-T record.

## Statement

Let S_n and N=n(n+1) be as in
[profile-boundary-cotangent.md](profile-boundary-cotangent.md), and put
a(alpha,beta)=(cos alpha+cos beta)/2. For every sequence of finite real
numbers b_n and every n>=2,

\[
\sup_{|\alpha|+|\beta|\le\pi}
 |S_n(\alpha,\beta)-a(\alpha,\beta)b_n|
\ge \frac2\pi\left(\log N+\gamma+\log\frac8\pi\right)
        -\frac1{4N^2}.                                  \tag{1}
\]

The right side tends to infinity. In particular a*Lambda_c, or a times
any corner logarithmic expansion, cannot have an absolute uniform
remainder tending to zero on the full diamond.

## Definitions and assumptions

Exact corrected primitive and diamond from the linked positive theorem;
integer n>=2. b_n may depend arbitrarily on n but not on the phases.

## Status by part

Overall status: **PROVED**, immediate consequence of the separately
proved boundary formula. Independent supplementary check and Claude audit
pending at first writing.

Candidate disposition: **REJECTED: refuted**, only for the explicitly
specified leading-factor-only vanishing-remainder trial.

## Negative-result scope

Attempted mechanism: IDEA?argmax-effective-2-codex-03, approximating the
primitive by a(alpha,beta)b_n with an absolute remainder tending to zero.
Parameter range: full phase diamond, all n>=2 and arbitrary finite b_n.
No impossibility is claimed for profiles with a phase-dependent logarithmic
term, piecewise boundary/interior representations, or a nonvanishing
O(log n) error. The original H2 did not specify this failed formula.

## Depends on

PD-T?argmax-effective-2-codex-03, exact midpoint value L_N and its
PD-T270 estimate.

## Checks and sources

Analytic implication only; no computation or fit. Gate:
`../novelty-gate-H2-H3.md`. No external source transfer.

## Proof

At alpha=beta=pi/2 one has a=0 and S_n=L_N. Evaluate the supremum
there and apply the lower half of (4) of the positive boundary theorem.
This proves (1) for every b_n. The divergence follows from log N -> infinity.

## Scope and open items

The obstruction requires a nonzero phase-dependent logarithmic correction
on the diamond boundary. Its midpoint coefficient relative to log n is
exactly 4/pi. This does not show that any particular corrected profile
works in the interior, refute H2 in general, or address PD-T099.
Independent reconstruction and required Claude audit remain pending.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra; rules/input
ed21cc0bf205549936fccde90244a291bc6de324. Trial specified and tested
analytically after the gate, before any fitting. No final ID allocated.
