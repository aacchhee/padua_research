# PD-T?mz-sharp-codex-P4-01 — certified endpoint lower decimal

ID kind: PD-T.
Aliases: exact J512 Rayleigh lower certificate.
Split from: numerical-value refinement of accepted S2 endpoint model.
Split into: a practical sharp upper enclosure remains OPEN and separate.

## Statement

For the exact endpoint variational norm Lambda_edge defined in
[S2-endpoint-model.md](S2-endpoint-model.md) and identified with the
common-parity CC upper spectral limit in S2-05,

    Lambda_edge >= 10044369/10000000 = 1.0044369.

Overall status: **PROVED**, computer-assisted local development with
distinct supplementary reconstruction and actual rerun PASS. Required
Claude audit remains separate. This is one-sided; no seven-digit or
three-digit two-sided approximation of Lambda_edge is asserted.

## Definitions, assumptions and dependencies

Exact unnormalized Lebesgue CC on degree at most N-1, as in S2-03/04/05.
Use the accepted finite matrices C_J,D_J with J=512. C_J is positive
definite by [S2-fixed-trial-limit.md](S2-fixed-trial-limit.md), and the
variational definition gives Lambda_edge >= u^T D_J u/(u^T C_J u) for
every nonzero finite vector u. The exact vector here is the sequence of
binary rationals encoded by the hex strings in
[P4-trial-J512.json](../evidence/P4-trial-J512.json).
The approximate generalized eigenvalue solver only selected that vector;
its accuracy, residual and eigenvalue ordering have no proof role.

## Finite reduction and proof

For s_j=(-1)^j, a_j=pi*j and d_j=Cin(2*pi*j), use the accepted formulas

    D=diag(2[s_j+a_j*Si(a_j)])+4ss^T,
    C_jj=2[a_j*Si(2*a_j)+d_j],
    C_ij=2s_i*s_j*(i²*d_j-j²*d_i)/(i²-j²), i!=j.

The exact finite check has two obligations: enclose numerator and
denominator by outward intervals with positive denominator, and compare
the lower quotient endpoint to the rational target. The implementation
uses unbounded Python integers on the 2^-256 endpoint grid; all products
and divisions round outwards with exact integer floor/ceiling.

Pi is enclosed by Machin's arctangent formula. Small Si/Cin arguments use
entire Taylor series with a geometric remainder after decreasing term
ratios become at most 1/2. Large integer-multiple-pi Si/Ci arguments use
20-term Laplace/geometric expansions with explicit factorial remainder
integrals. A Cin(16*pi) anchor cancels Euler's constant from d_j. Rational
logarithms use range reduction and the convergent atanh series. Complete
developer scalar derivations, exact protocol and chronology are in
[attempts/P4.md](../attempts/P4.md); these were independently reconstructed
as recorded below. No floating special-function value enters the check.

The producer gives the strictly positive denominator enclosure

    0.999999999999999917507138 <= u^T C_J u
                             <= 0.999999999999999917507142

and the trial quotient enclosure (outward decimal rounding of its exact
dyadic integer endpoints)

    1.004436918864667280457774 <= q(u)
                            <= 1.004436918864667280457779.

The exact integer comparison of the lower endpoint with
10044369/10000000 passes. Consequently Lambda_edge>=q(u)>=1.0044369.
The quotient's upper endpoint bounds only q(u), not Lambda_edge.

## Committed evidence, identities and actual checks

Protocol and all three source scripts were committed before evaluation at
`d03e74dcf94020ba26d9fae84d3ff6c5519db901`. The later completion addendum
does not replace the historical preregistration blob; its SHA-256 was
`101bc61acd673f71195b1e0c002101106f1e6d15dbc7b2b679eb614807d84a77`.

| Input / trusted source | SHA-256 |
|---|---|
| exact trial P4-trial-J512.json | a472d397b6a802d7bfe9c06bdb25d2f572d18134726b8dad9f695772f0956da8 |
| producer P4_rayleigh.py | 7bcf4032590cf07c12943ecd5b9bf1f3cef18f32240d884acba60ad5047947eb |
| interval/scalar interval_dyadic.py | 8a90618d19ffd8f8efde50bc9002b0b0e26f62d243b4086c674cedcf657945fc |
| independent actual rerun receipt | 28bb283a2cc3ca65153fd3afbb4a4b0473a7f3f6e96075a52d91a27d8c471a8e |

Producer command and exact endpoint integers are in
[P4-rayleigh.json](../evidence/P4-rayleigh.json); preparation command,
versions and identities are in P4-trial-preparation.json. The developer
executed the producer (5.672 wall seconds) and the alternate exact
Fraction-grouped quadratic-form checker (3.235 seconds), recorded in
P4-grouped-check.json. The alternate checker shares scalar/interval code;
it supplies an independent form assembly, not a separate scalar library.

The distinct reviewer independently retrieved the published code, verified
bytes, reconstructed the finite reduction, closed-form C entries, scalar
identities, remainder estimates and directed integer arithmetic, and
actually reran the grouped checker (3.256 seconds). See
[independent-checks-P4.md](../independent-checks-P4.md) for its PASS and
independent receipt location/hash. The coordinator integrated the
unchanged actual rerun receipt as
[check-P4-independent.json](../evidence/check-P4-independent.json), with
the SHA-256 recorded above. Required subsequent Claude audit is not
replaced by this supplementary check.

Trusted dependencies are the accepted S2 mathematical formulas, reviewed
scalar proofs and committed scripts, Python 3.12.14 integer/Fraction and
exact binary64 hex parsing, and ordinary filesystem execution. NumPy and
SciPy selected the finite vector only. Hardware/software or correlated
review errors cannot be excluded by numerical agreement alone; the
explicit reduction and source inspection supply the proof obligations.

## Limitations and open items

No upper-side finite certificate was solved. Existing analytic upper
bounds remain background; the practical upper bracket and certified
two-sided digits stay OPEN. The original PD-T027 registry interpretation
is for AC and is unchanged here. No final ID or shared registry was edited.

## History

2026-11-06, P4 technical round 1; rules read at
0205690b9c4e959a28e949083e9a1808735abf4b; R clearance
17ca9f441cece178354e70504a6c739df501a224. Requested Codex gpt-6.1-sol
medium, serving-model metadata unexposed. Distinct supplementary
review_response check passed after actual execution. No tuning, failed
numerical instance, threshold revision or extra J value occurred.
