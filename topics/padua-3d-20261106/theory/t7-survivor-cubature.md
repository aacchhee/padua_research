# PD-N?padua-3d-20261106-codex-T7-07 — the fixed rank-two survivor fails the Padua cubature marker

ID kind: PD-N. Aliases: translated order20 quartic cubature obstruction.
Split from: none. Split into: none. Supports the OPEN T7 target.

## Statement and assumptions

For the specific20-node coset X of T7-06, no real weights supported
on X integrate every polynomial of total degree≤4 against normalized
product first-kind Chebyshev measure. In particular no positive-weight
degree5 rule, the n=3 Padua cubature marker, exists on these nodes.

Overall status: PROVED by the written identity and integral below.
Candidate IDEA?…T7-08 (using this isolated survivor as a Padua cubature
mechanism) is REJECTED within this scope: the necessary exactness
fails. Its Π3-unisolvence remains a separate positive result.

## Proof

The vector u=(2,−2,0) annihilates both subgroup generators:
u·g=0, u·h=1. At every angle θ∈a+H, put
A=4πθ_1, B=4πθ_2. Their difference is constant modulo2π:

    A−B=δ=−4π/101.

Set U=T_2(x), V=T_2(y), c=cosδ. Squaring the cosine addition
identity gives, for any A−B=δ,

    U²+V²−2cUV−(1−c²)=0.

This is a nonzero polynomial Q(x,y) of total degree4 (T2(t)=2t²−1).
Under the continuous product Chebyshev measure,
I(U²)=I(V²)=1/2 and I(UV)=0 by the one-variable cosine integrals.
Consequently I(Q)=c². Since 0<4π/101<π/2, c²>0. Any weights on X
give Q_X(Q)=0, proving the contradiction for degree4 and therefore5.
This holds without sign or positivity assumptions on the weights.

For comparison, the coset's own Haar pushforward already fails at
degree3: only the signs (1,1,−1) and its opposite in the xyz expansion
annihilate H, so Q_H(xyz)=cos(2π/101)/4≠0=I(xyz).
This last calculation is a hand check, not a numerical fit.

## Negative-result scope and D3

Attempted mechanism: IDEA?padua-3d-20261106-codex-T7-08, this exact
translated C10×C2 survivor carrying a degree5 Padua-type cubature.
Parameter range: the frozen group and phase only. A phase with
cosδ=0 would defeat this particular integral witness; other groups,
phases or interpolation without degree5 cubature are not excluded.
No lower bound on its Lebesgue constant follows from the witness.

The analogous two-coordinate identity has degree2max(|u_1|,|u_2|).
For 2D Padua the mixed shortest dual relation has max≥n+1, while pure
axis relations have degree≥2n (T7-02). Such witnesses do not exclude
its degree2n−1 cubature. This admits the actual Padua control and
explains why a cubic-degree interpolation survivor alone is insufficient.

## Checks / sources / history

Proof is elementary and independent of the finite rank certificate.
T7-06 identifies the actual candidate; T7-01 supplies the optional
Haar moment expansion. Independent mathematical check is recorded in
root's [new-math checks](../independent-checks-new-math.md). No imported
source theorem or novelty claim. Full all-coset cubic census is OPEN.

2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules e5b6445.
The explicit candidate and analytic marker test were prospectively
recorded in preregistration-T7.md before this final proof was written.
