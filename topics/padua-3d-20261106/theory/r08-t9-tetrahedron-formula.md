# PD-T?padua-3d-20261106-codex-T9-r06-04 — exact Lebesgue constant for a phased tetrahedron

ID kind: PD-T.
Aliases: T9-R06-TH02; fixed-dual tetrahedron; anisotropic degree-one coset.
Split from: PD-T?padua-3d-20261106-codex-T9-r06-02, t9-r06-phase-weight-boundaries.md section “Identical dual minimum…”; this record gives an already named claim its own durable home.
Split into: none. Provisional ID retained; no final allocation or shared crosswalk edit.

## Statement

For every 0<t<=1, the four-node set X_t={(t epsilon1,epsilon2,epsilon3):epsilon_j in {+1,-1}, epsilon1 epsilon2 epsilon3=1} is Pi_1-unisolvent and has

    Lambda(X_t)=max(1/t,(1/t+3)/2).

It is the cosine image of one fixed torus subgroup under phase (arccos t,0,0), with the same dual lattice L={k:k1=k2=k3 mod2} and shortest nonzero l1 norm2 for all t.

## Definitions

H is a finite subgroup of (R/(2pi Z))^3, L its annihilator in Z^3, a a phase in radians, X=cos(a+H) coordinatewise, and mu is normalized product Chebyshev measure. Pi_n means total degree<=n. Here the four sign triples have product+1, t>0, and Lambda is the continuous interpolation operator norm on the real cube.

## Assumptions

n=1 fixed; all real 0<t<=1; full four-node interpolation on Pi_1.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Unisolvence, fixed dual and exact continuous Lambda formula | PROVED | Explicit cardinal functions and vertex maximization |

Candidate disposition: retained exact example; no asymptotic assertion.

## Negative-result scope

Not applicable: positive standalone result; no negative allocation is created by the split.

## Depends on

Elementary affine interpolation and convexity. No external theorem. [Original combined proof](t9-r06-phase-weight-boundaries.md).

## Checks

No new numerical or optimizer run by this response worker. The local proof was read and reconstructed from the old combined body. [Audit03/T9](../audit-03/T9.md) independently accepted these scoped statements; [independent-checks-round06](../independent-checks-round06.md) records supplementary checks. The exact-algebra controls are [t9-r06-exact.json](../evidence/t9-r06-exact.json), with source/command identities in the old receipt manifest. Reading a historical output is not a new independent execution.

## Sources

[Round08 gate/source supplement](../novelty-gate-supplement-round08.md) records the actual predecessor bodies, source aliases and limits. External source dependencies appear explicitly below; no cited proof is inherited by citation.

## Proof or evidence

Take H to be the torus points with each coordinate0 orpi and an even number ofpi entries. Its annihilator is exactly L={k:k1=k2=k3 mod2}; (1,1,0) is not in L, while (2,0,0) is, so the minimum is2. Applying phase(arccos t,0,0) gives X_t. The four cardinal polynomials are

    l_epsilon(x,y,z)=(1+epsilon1*x/t+epsilon2*y+epsilon3*z)/4.

Direct evaluation gives the identity matrix and proves unisolvence. Their absolute sum is convex in each coordinate; repeated endpoint maximization reduces its cube maximum to the eight vertices. With b=1/t>=1, the two vertex sign classes give b and (b+3)/2, proving the formula.

## Scope and D3

D3: this is a fixed n1, dimension3 exact example, not an obstruction applying to a dimension2 Padua set. It is compatible with Padua stability because it varies a degenerating phase/axis scale outside a fixed Padua sequence.

## Open items

A selected nondegenerating phase sequence might have good quality. The formula supplies no degree-growing lower bound for all cosets and no impossibility theorem for a particular higher-degree construction.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Response08 completes audit03 novelty m2/m3 by splitting already named statements from combined bodies. Statements/statuses are retained; E4's source-label criterion belongs to root and AC. Old pinned bodies are unchanged by this worker.
