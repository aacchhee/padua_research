# PD-T?argmax-bridge-codex-N4-01 — Unrestricted nonnegative transport is exactly the norm inequality

ID kind: PD-T.
Aliases: B5 formulation gate; positive/negative mass criterion; substochastic vector transport.
Split from: none; proves the explicitly requested unrestricted N4 gate.
Split into: none.

## Statement

Let v in R^r and w in R^s, with r,s positive integers. Write
P(v)=sum_j max(v_j,0) and Q(v)=sum_j max(-v_j,0), and similarly for w.
There exists a real s-by-r matrix M with nonnegative entries, each column
sum at most1, and Mv=w, **if and only if**

    P(w)<=P(v) and Q(w)<=Q(v).                                  (1)

In particular, if sum v=sum w=1, existence is equivalent to

    ||w||_1<=||v||_1.                                          (2)

This includes zero entries, zero negative mass, and, in(1), the zero
vector and zero positive mass. If v,w are rational and feasible, the
construction below gives rational M.

## Definitions and assumptions

Column sums, not row sums, are bounded. Vector dimensions may differ.
No Padua or sign-mask hypothesis is needed for(1). For the Padua
application v=L(c), w=L(z), partition of unity follows because
interpolation reproduces the constant polynomial1 (PD-T101).

## Status by part

Overall status: **PROVED**, elementary written proof below.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Criterion(1), including all zero-mass cases | PROVED | Written proof |
| Equal-unit-sum equivalence(2) and Padua specialization | PROVED | Exact mass identities and partition of unity |

Candidate disposition: the unrestricted N4 formulation is **equivalent**
to its norm target. This is not a failed mechanism theorem or PD-N.

## Depends on

Elementary inequalities only; PD-T101 solely for the Padua application.

## Proof

If M is feasible, write v=v^+-v^- with nonnegative parts. Since M>=0,
coordinatewise `(Mv)^+<=Mv^+` and `(Mv)^-<=Mv^-`. Summing and using
the column bounds proves P(w)<=P(v) and Q(w)<=Q(v).

Conversely, for every positive input coordinate v_j>0 set

    M_ij=w_i^+/P(v),

and for every negative input coordinate v_j<0 set

    M_ij=w_i^-/Q(v).

Set all columns with v_j=0 to zero. A denominator is used only when a
coordinate of its respective sign exists, so it is strictly positive.
The positive-column sums are P(w)/P(v)<=1; the negative-column sums
are Q(w)/Q(v)<=1. Summing M_ij v_j over positive columns gives w_i^+
if P(v)>0. If P(v)=0, (1) forces P(w)=0 and that same equality holds
with an empty sum. The negative columns give -w_i^- in the same way.
Thus Mv=w. If both masses of v vanish, (1) forces w=0 and M=0 works.

For a vector u of sum1,

    P(u)=1+Q(u),  ||u||_1=1+2Q(u).

Therefore both inequalities in(1) are equivalent to Q(w)<=Q(v),
which is equivalent to(2). When Q(v)=0, this simply requires w>=0
and sum w=1; the positive columns alone give the construction. No
corner zero or sign is divided by. QED.

## Checks and sources

No computation or external source is a proof premise. Parent supplied
the positive/negative-mass proof hint. Supplementary independent Astra
mathematical review requested through the coordinator; pending.

## Scope

For Padua cardinal vectors, unrestricted LP feasibility is exactly
lambda_n(z)<=Lambda_c(n), so a successful unrestricted LP has no extra
hypergroup/translation content. Unrestricted infeasibility would still
give a counterexample to that inequality. No such infeasibility is
claimed or computed.

## Open items

PD-T099 remains OPEN. A useful N4 proof needs an independently specified
structured operator and positivity proof; the displayed target-dependent
rank-at-most-two construction is not such a candidate.

## History

2026-11-05, N4 round1, Codex parent-assigned gpt-6.1-sol xhigh; serving
metadata not independently exposed. Rules read at
`98d6c00d8a474cf97602c9cfdea631a837191ac0`. Original B5 wording is
unchanged; dated refinement is separate in attempts/N4.md. No Git or
shared-record mutation by this worker.
