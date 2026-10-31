# PD-T?charter-unisolvence-u1-independent-02 — Original U1 is valid outside characteristic two

ID kind: PD-T; provisional independent verification label, to be consolidated with the producer result.
Aliases: odd-characteristic alternation Hankel iff.
Split from: original arbitrary-field U1 iff, separating its valid non-characteristic-two case.
Split into: none.

## Statement

For every field K with char K≠2, every m≥0, and each e∈{0,1}, let X and Y have lengths m+1 and m+2 with distinct entries within each list. Then S_e is unisolvent for Π_m if and only if the signed-alternation Hankel minors Δ_{H,r} are nonzero for H=X,Y and 1≤r≤|H|−1. The characteristic-zero case is included in the phrase “outside characteristic two.”

## Definitions and assumptions

Use the definitions and notation of `reconstruction-allchar.md`, including Δ_{H,r}=det(A_H(z^{a+b}))_{a,b<r}. No ordering or positivity is needed. The minor ranges are finite; the full minor Δ_{H,|H|} is automatically one, and later minors vanish because the functional has finite support.

## Status by part

Overall status: PROVED. Both necessity and sufficiency follow from the exact determinant identity below. Acceptance and the final Claude audit remain separate.

## Depends on

The independently reconstructed hand proof of the parity Gram/tensor identity, equation (8) of `reconstruction-allchar.md`. Neither normalized central factors nor an assumed nonzero-minor hypothesis is needed for that identity.

## Proof

Equation (8) states

\[
2^N(-1)^{eN}\det(E_e)^2\prod_{S_e}\frac1{\omega_X'\omega_Y'}
=\prod_{r=1}^{|X|-1}\Delta_{X,r}\prod_{r=1}^{|Y|-1}\Delta_{Y,r}.
\]

In a field of characteristic different from two, every factor on the left other than det(E_e)² is nonzero. The product on the right is nonzero if and only if each listed factor is nonzero. Therefore det(E_e)≠0 if and only if all required minors are nonzero. This treats all m, including m=0 and its empty X minor range, and both parities. It also avoids an invalid necessity argument from Gram orthogonalization under a hypothesis that already assumes all minors nonzero: the determinant identity itself was established as a universal polynomial identity before specialization.

## Checks

Independent exact comparisons over Q and F_3,F_5,F_7,F_11,F_17 passed in the recorded scope, including exhaustive F_5 labelled axis pairs at m=2 with 2,400 singular pairs among 7,200. Details are in `evidence.md` and `check-output.txt`. These are MEASURED checks of a hand theorem.

## Sources and scope

No novelty claim. The literature comparison with De Marchi–Usevich 2014 remains explicitly separate. The arbitrary-field original iff has the characteristic-two counterexample in `reconstruction-char2.md`, while original sufficiency over all fields follows from this theorem plus the impossibility of its antecedent in characteristic two.

## Open items and history

Producer-proof comparison and final Claude audit pending at independent freeze. Written 2026-10-31 by Codex gpt-6-astra xhigh at supplied rules/base d36722823441dc40c6e19d69a174459348dd309c; no producer U1 files or Git commands used before this reconstruction.
