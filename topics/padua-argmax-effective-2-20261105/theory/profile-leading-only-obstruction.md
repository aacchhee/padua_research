# PD-N132 (PD-N?argmax-effective-2-codex-01) — Leading phase factor alone has a divergent absolute error

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
proved boundary formula. Dated review note, 2026-11-05: Claude
[audit-01](../audit-01.md) accepted this original scope; the record response
check is pending.

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

Boundary-profile remark (using T03, beyond this midpoint proof):
[T03 equations (2)–(4)](profile-boundary-cotangent.md) have a=0 all along
the boundary, S_n=1 at its vertices and S_n=L_N at its midpoints.
Consequently a phase-independent correction cannot give a vanishing
absolute uniform error there: the required logarithmic correction varies
with phase, with midpoint coefficient 4/pi relative to log n. The midpoint
argument above alone establishes only (1). Neither observation shows that
any particular corrected profile works in the interior, refutes H2 in
general, or addresses PD-T099. Audit-01 accepted the original negative
statement; the record response check remains pending.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra; rules/input
ed21cc0bf205549936fccde90244a291bc6de324. Trial specified and tested
analytically after the gate, before any fitting. No final ID allocated.

2026-11-05 audit response, Codex, gpt-6-astra ultra: F10 labels the
boundary-profile discussion as a remark and supplies its T03 attribution.
The earlier unqualified wording attributed too much to the midpoint
obstruction alone. The negative statement, proof, constants, PROVED
status and scoped REJECTED: refuted disposition are unchanged.

## Registration — 2026-11-05

Final ID: **PD-N132**. Preserved provisional alias: `PD-N?argmax-effective-2-codex-01`.
Registration input/rules: `5821c3f130ec0b1e33ad1d01620b67620e1f0be1`.

The negative statement is PROVED; IDEA-456 is REJECTED: refuted only for the specified leading-factor-only a*b_n vanishing-remainder form. Neither PD-T099 nor the full H2 target is refuted.

[Claude audit-01](../audit-01.md) accepted the mathematical scope;
[response-check-01](../response-check-01.md) accepted the record response.
Earlier provisional/no-final-ID and pending-response-check wording above
is retained as history and is superseded only administratively by this
registration. Every pre-existing paragraph after the heading, including
Statement, proof, status, displays and History, is preserved byte for byte.
The [final-ID map](../preparation/final-id-map.json) and
[registration notes](../preparation/registration-notes.md) record the mapping
and preparation limits. PD-T099 remains OPEN; the global certified range
remains exactly 2–32.
