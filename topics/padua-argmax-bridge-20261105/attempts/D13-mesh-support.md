# D13 singular-mesh support — bounded paper outcome

Rules/input `e13a538bda80e6cc785f4835937b2ca338bc1d6f`.
2026-11-06, parent-assigned Codex Sol xhigh; serving metadata unexposed.

The supporting result is written in
[theory/D13-mesh-support.md](../theory/D13-mesh-support.md), with the
candidate/gate limits in
[ideas/D13-mesh-support.md](../ideas/D13-mesh-support.md).

Exact success: D07's unchanged scalar remainders obey, for n>=32 and
alpha,beta>=0, rho=alpha+beta<=1/2,

    |Rmesh(phi)-aRmesh(0)|<=rho/(2n),
    |Rmesh(phi)-aRmesh(0)|+(d/pi)|Rlog(phi)|
                                      <=rho[log n+7/3]/n.

This follows after exact B0 cancellation and pairing the upper h_n,g_n
constants. The only DeltaD coefficient is H_n+2log n=O(n^-2).
The retained exact eps=log((n+1)/n) multiplies the LOWER H_2 increment;
that term explains the harmless O(rho/n) mesh bound.

No failed theorem or universal negative claim is produced. The
two-independent-Bmesh allocation is abandoned for the relative target
because it leaves a phase-independent floor. Pairing first removes
that allocation defect. A sharper quadratic bound is not needed and
is not tested. Full-phase extension is deferred; full D13 remains OPEN.

Independent review needed: verify (4)--(5)'s signs, exact terminal index,
uniform differentiation of h/g, the paired derivative bounds, the
centered harmonic tail sign, and the U0 coefficient increment. This
author did not independently audit their own proof.

No numerical jobs occurred. Only repository reading/searches and prose
creation were performed; no model or near correction was changed.
