# PD-T?padua-3d-20261106-codex-T9-r06-03 — phase-uniform low-degree annihilator

ID kind: PD-T.
Aliases: T9-R06-PB; phase-uniform product of sign relations.
Split from: PD-T?padua-3d-20261106-codex-T9-r06-02, t9-r06-phase-weight-boundaries.md section “A phase-uniform annihilator”; this record gives an already named claim its own durable home.
Split into: none. Provisional ID retained; no final allocation or shared crosswalk edit.

## Statement

For every nonzero k in L, set r=||k||_1, s=|supp(k)| and m=2^(s-1). There is a nonzero real polynomial p of total degree<=mr vanishing on X. Thus mr<=n prevents Pi_n-unisolvence. Exact product-Chebyshev cubature on X with arbitrary real weights is impossible if 2mr<=D, where D is the requested exactness degree. If a=0, arbitrary-weight exactness is already impossible when mr<=D.

## Definitions

H is a finite subgroup of (R/(2pi Z))^3, L its annihilator in Z^3, a a phase in radians, X=cos(a+H) coordinatewise, and mu is normalized product Chebyshev measure. Pi_n means total degree<=n.

## Assumptions

Finite H; arbitrary a; nonzero integral k in L. The arbitrary-weight conclusion uses exactness for all polynomials of total degree<=D, including constants and p^2.

## Status by part

Overall status: **PROVED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Annihilator and three stated implications | PROVED | Local finite product and positivity of integral |

Candidate disposition: retained local supporting result; no whole-coset rejection.

## Negative-result scope

Not applicable: positive standalone result; no negative allocation is created by the split.

## Depends on

Elementary Fourier/Chebyshev reflection invariants and positivity of integral of a nonzero polynomial squared. No external theorem. The old combined body remains [phase-weight boundaries](t9-r06-phase-weight-boundaries.md).

## Checks

No new numerical or optimizer run by this response worker. The local proof was read and reconstructed from the old combined body. [Audit03/T9](../audit-03/T9.md) independently accepted these scoped statements; [independent-checks-round06](../independent-checks-round06.md) records supplementary checks. The exact-algebra controls are [t9-r06-exact.json](../evidence/t9-r06-exact.json), with source/command identities in the old receipt manifest. Reading a historical output is not a new independent execution.

## Sources

[Round08 gate/source supplement](../novelty-gate-supplement-round08.md) records the actual predecessor bodies, source aliases and limits. External source dependencies appear explicitly below; no cited proof is inherited by citation.

## Proof or evidence

Choose one epsilon from every pair epsilon,-epsilon of sign vectors on supp(k), and set

    F(theta)=product_epsilon [cos(sum_j epsilon_j k_j theta_j)-cos(k.a)].

Independent coordinate reflections permute the factors, with the overall sign irrelevant to cosine. The Laurent support has l1 degree<=mr, so the reflection-invariant Laurent polynomial is p(cos(theta)) for a real polynomial of total degree<=mr. Each factor is a nonzero analytic function; their finite product is not identically zero. On a+H the all-plus factor vanishes, because k is a dual relation. This proves the annihilator.

If mr<=n it lies in the interpolation kernel. If 2mr<=D, exactness on p^2 is impossible: every weighted nodal value is zero, while integral p^2>0. At a=0 use instead product_epsilon(1-cos(sum_j epsilon_j k_j theta_j)), itself nonnegative and nonzero, of degree<=mr. Its nodal values vanish and its integral is positive, giving the improved unshifted threshold.

## Scope and D3

D3: in dimension2 the same argument uses at most two sign classes. The standard degree-n Padua torus dual is {((n+1)u,nv):u+v even}; its shortest nonzero l1 norm is2n. Hence every mr>=2n>n and 2mr>=4n>2n-1. Neither obstruction falsely excludes Padua. The exact formula for that dual follows by reducing the order2n(n+1), generator(n,n+1) congruence modulo n and n+1.

## Open items

The bound need not be sharp; its failure to trigger proves nothing about rank or weights. A coset Lebesgue lower bound requires a separately specified kernel estimate; this annihilator is only a rank/exactness result.

## History

2026-11-06 — Codex records worker, assigned gpt-6.1-sol xhigh; runtime metadata not independently exposed. Rules/input `9042e1c42964150f30fdbe8563c12ba6c6a8692a`. Response08 completes audit03 novelty m2/m3 by splitting already named statements from combined bodies. Statements/statuses are retained; E4's source-label criterion belongs to root and AC. Old pinned bodies are unchanged by this worker.
