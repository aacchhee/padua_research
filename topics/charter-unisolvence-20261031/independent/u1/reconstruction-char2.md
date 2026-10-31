# PD-N?charter-unisolvence-u1-independent-01 — Original U1 necessity fails in characteristic two

ID kind: PD-N; independent verification label, to be consolidated with the producer's corresponding negative result.
Aliases: U1 characteristic-two obstruction; signed alternation loses parity.
Split from: original U1 iff over arbitrary fields.
Split into: none.

## Statement

The assertion that every labelled checkerboard S_e is unisolvent for Π_m if and only if all signed-alternation leading Hankel minors for X and Y of orders 1,...,|H|−1 are nonzero is false when characteristic two is included. The necessity direction fails already for m=0 over F_2, for each e.

## Definitions and assumptions

Use X=(h_0,...,h_m), Y=(g_0,...,g_{m+1}), distinct within each list, and A_H(f)=Σ_i(-1)^i f(t_i)/ω_H'(t_i). No ordering is assumed. Characteristic two is essential to the obstruction below.

## Status by part

Overall status: PROVED by an ordinary hand counterexample.
Candidate disposition: original arbitrary-field U1 iff REJECTED: refuted within the stated scope. This is not a refutation of the odd-characteristic statement or of all-field sufficiency.

## Negative-result scope

Attempted mechanism: necessity of nonzero signed-alternation minors, U1a.
Parameter range: characteristic-two fields; the general signed order-one failure is established for every list length L≥2; an unisolvent counterexample is explicit at m=0 over F_2 and at m=1 over F_4.

## Proof

In characteristic two all signs (-1)^i are one. Lagrange interpolation implies Σ_i1/ω_H'(t_i)=0 whenever L≥2: it is the coefficient of z^{L−1} in the constant polynomial one. Thus the required order-one minor of Y always vanishes, at every m≥0.

For m=0 over F_2 choose X=(0), Y=(0,1). Then S_0={(0,0)} and S_1={(0,1)}. Evaluation on constants is the 1×1 matrix (1) for either parity, hence is invertible. But A_Y(1)=1+1=0. This is the complete counterexample.

For a positive-degree example, let F_4=F_2[a]/(a²+a+1), X=(0,1), Y=(0,1,a). Then S_0={(0,0),(0,a),(1,1)} and S_1={(0,1),(1,0),(1,a)}. The evaluation determinants on (1,x,y) are respectively a and a in characteristic two, both nonzero. Again both signed order-one functionals vanish. This example is optional corroboration; it is not needed for the m=0 refutation.

## Depends on

Elementary Lagrange interpolation and direct determinants only.

## Checks

The independent checker separately executed exhaustive labelled configurations over F_2 at m=0 and F_4 at m=0,1,2. Output is recorded in `check-output.txt`, with full provenance in `evidence.md`. In particular all 4 labelled F_2 axis pairs at m=0 and all 288 labelled F_4 axis pairs at m=1 are unisolvent for both parities while failing the original iff. The hand proof does not depend on exhaustive computation.

## Sources

No external result beyond elementary interpolation is used. No novelty claim.

## Scope and open items

The failure is of necessity. Signed quasi-definiteness is impossible in characteristic two because Y has at least two elements, so sufficiency there is vacuous. Odd-characteristic necessity and sufficiency are proved in `reconstruction-oddchar.md`; the useful all-field replacement is `reconstruction-allchar.md`. Final Claude audit remains pending.

## History

2026-10-31, Codex gpt-6-astra xhigh, rules/base d36722823441dc40c6e19d69a174459348dd309c. Reconstructed before producer proof inspection; no Git operation.
