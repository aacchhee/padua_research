# Direction 1, round 6 — exact axis row resummation

Date: 2026-11-02. Codex, assigned gpt-6.1-sol xhigh; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
Contract: [round 6](r06-contract.md), retained candidate
[row-sum repair](r05-next-row-sum.md). Same IDEA-305 / Claude-02 /
fallback-04 quantitative primitive route, with the earlier full registry,
alias, obstruction and disposition gate reused. No external literature
theorem is transferred.

## Pre-execution optional correctness check

Before executing the script, fix degrees 2,3,4,8,16 and phases
0,+.17,-.17,+.4,-.4, beta=0. Check every periodic second row, with its
n parity first points, against the finite Fourier kernel. Check the
cotangent row representation, full signed row identity, endpoint row
formula and sign-interval absolute row. Polynomial collisions use their
actual finite values. Use Python float64 with no fitting, larger degree,
phase optimizer or additional phase grid. Every computed agreement is
MEASURED only; the proof is analytic.

The reproducible command will be

`python topics/padua-argmax-alln-20261101/code/gated/d1_rows_r06.py > topics/padua-argmax-alln-20261101/outputs/gated/d1_rows_r06.json`.

Source identity will be recorded below before execution.

Pre-execution source: `a9decfcd7293bcfd50ec474b9adb72f16854cf9d24d3aa9979c9fcaf9f394329`, 3490 bytes. Fixed scope above
was written before executing this source.

## Completed derivation and honest bound status

The exact formulas and complete proofs are preserved as
[theory12](../../theory/gated-codex-12-row-primitive-identity.md).
The full cotangent identity is derived from t^n-1, not imported from
unread literature. For every nonzero second row the signed sum is
exactly n*a, including the pi row by polynomial completion. The zero
row is exceptional: its signed sum is -n*(m-a), and its absolute sum
n*(m-a). Interior collisions have actual positive half value
(n+cos v)/2 and therefore contribute nothing to a negative-part sum.

For a folded row v in (0,pi), denominator-negative arc D=(v,2pi-v)
and numerator-negative arc I=(asin q,pi-asin q),
q=(1+cos v)/tan(|alpha|/2), completely determine the negative indices
by their symmetric difference. Take I empty if q>=1 or alpha=0.
Thus every interior absolute row is n*a plus twice its negative partial
cotangent sum; all endpoint and collision cases are included separately.

The pi endpoint admits the explicit bound
0<=R_pi-n*a<=n*|alpha|*H_floor(n/2)/(pi-1/5) on |alpha|<=.4.
This is a useful shrinking linear coefficient for that endpoint,
but it does not control the signed differences of the interior negative
partial sums. Those differences remain the central quantitative problem.
No sharper uniform two-phase primitive bound was obtained.

## Completed bounded correctness run

Actually executed the predeclared command above under Python 3.12.14,
Python binary64 math, deterministic inputs, no randomness. All 25
registered (degree,phase) pairs completed, totaling 380 periodic row
cases. Maximum absolute discrepancies were:

- cotangent terms versus finite kernel: 1.69286806795e-12;
- complete signed rows versus exact identity: 8.86402062861e-13;
- sign-interval/endpoint absolute rows versus finite kernel: 8.52651282912e-13.

These are MEASURED correctness checks, without outward rounding or an
independent rerun. They prove no uniform estimate or asymptotic rate.

Output: 6507 bytes, SHA-256 `560e2677d04a3ab6a2a6d0bbaa6e57ca5ab3e97835fefd15abb7d2e2c0ffb9dc`.

## Retained variants and gate

| Variant | Disposition / exact scope |
|---|---|
| Exact full row n*a | PROVED finite identity, retained as theory12; does not itself bound absolute rows. |
| Apply full cotangent formula to an absolute or signed partial interval | Insufficient: (8) sums all n equally spaced points, while a negative sign interval contains a changing subset. No such substitution is made. |
| Treat zero times an infinite cotangent as zero at a collision | Failed evaluation rule; the true finite value is (n+cos v)/2 at an interior collision and n at the pi endpoint. Polynomial values are retained. |
| Endpoint shrinking coefficient | PROVED only for the pi row; it does not establish the interior or two-phase repair. |
| Larger degree agreement as a reason for round 7 | Not pursued; it would not control the unresolved partial sums. |

**STOP this row-resummation repair; no automatic round 7.** The compact
exact identity collapses the signed row, but the actual gain still
contains uncontrolled interior negative partial cotangent differences.
No genuinely sharper uniform interior bound or distinct discriminating
analytic inequality was obtained in this bounded round. The endpoint
improvement and finite formulas are retained without treating them as a
positive continuation gate. Recommend closure of direction 1's current
repair sequence after independent review, so the orchestrator can proceed
to the already authorized corner direction in the required order.

PD-T099, exact corner dominance, effective thresholds and P6 remain OPEN.
No direction-2 work, future round, larger degree grid, fit, external
source transfer, Git action or shared registry update was executed here.

## Independent closure and notation clarification

The separate Astra reconstruction accepted the supporting identities and
the STOP recommendation. Its notation clarification is incorporated in
theory12: after folding the second angle, r_*=min(r,2m-r) has the same
parity as r, and n*v=r_* pi-v. This changes no formula or claim.
Direction 1 closes after six gated rounds; no round 7 or further work is
executed by this worker. Required Claude audit remains pending.
