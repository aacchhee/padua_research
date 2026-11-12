# PD-T?padua-3d-20261106-codex-T10-07 — sharp projection bound from a named source theorem

ID kind:PD-T. Aliases: polyhedral-kernel transfer. Split from:none. Split into:none.

Task provenance: handoff06 T10.4 and the log³ target PD-T?padua-3d-20261106-codex-T10-06. This is a source-dependent implication with the dependencies below, not a split into target conjuncts.

## Statement and status

Assume the following named external result in precisely its inspected form: Kolomoitsev–Lomako arXiv1801.00608v1 Theorem4.1, pp18–19, bounds the normalized torus L1 norm of the Fourier Dirichlet kernel of each bounded convex polyhedron P contained in[0,N1]×[0,N2]×[0,N3] by C(s,3) product_j log(Nj+1), where s is a triangulation size. Then for alln>=1 the anisotropic parity-grid weighted least-squares projections of `t10-parity-log4.md` satisfy `||Pn||∞=O(log(n+2)^3)`, and the equal-order parity hyperinterpolants satisfy the same bound.

Overall status: **PROVED with explicit LITERATURE dependency**, proposed under response03 E4 for AC decision. The external statement and applicability were primary-verified; its full supporting §3 proof chain was not locally checked. This is a source-dependent corollary, not a new theorem about minimal interpolation and not an inherited proof of the external result. The self-contained local log⁴ result remains PROVED under its own ID.

## Local implication proof

Let W={t inR³:|t|1<=1}. The integer translation nW+(n,n,n) is contained in[0,2n]^3 and has a triangulation of fixed size independent ofn, obtained by scaling/translating a fixed triangulation ofW. Translating a finite integer Fourier frequency set multiplies its Dirichlet polynomial by a unit-modulus exponential, leaving its L1 norm unchanged. The named theorem therefore gives `||D_n||L1 <= C log(2n+1)^3`.

The fully written local Fejer sampling argument in T10-04 gives `||Hn||∞ <=13³||D_n||L1`; its exact Gram correction gives `||Pn−Hn||∞<=1`. Combining these inequalities proves the stated implication with constants independent ofn. For equal ordersn+1, Hn=Pn directly. No finite mesh norm is used in this proof.

## Dependencies, novelty and remaining obligations

Depends on PD-T?padua-3d-20261106-codex-T10-04's sampling/reflection/Gram proof and LIT?padua-3d-20261106-codex-T10-08's inspected theorem. The whole projection mechanism is established in Cools–Poppe and De Marchi–Vianello–Xu; sharp polyhedral kernels are classical, as the Travaglini lead confirms. No novelty or priority is claimed. Remaining obligation for a wholly self-contained sharp proof: check/reconstruct the external theorem's supporting lemmas or provide a direct octahedral L1 proof. This conclusion concerns roughly1.5N-node projection only; T9-05's inverse restriction bound is still missing for N-node interpolation. Independent mathematical audit remains required.

History:2026-11-06 primary-source addendum after the initial OPEN target record and the elementary log-four proof. The target's earlier gap was real when written; the named source statement now supplies a precise conditional route.

## Status by part and material history — 2026-11-06, response03

The polyhedral-kernel theorem is LITERATURE; the translation/triangulation,
sampling and Gram implication are local proofs. Overall: **PROVED with
explicit LITERATURE dependency**. This is a material proposed upgrade
from CONDITIONAL, based on the uniform source criterion in
[response03](../response-03.md), requiring focused re-audit and AC's
convention decision. Source coverage has not increased. A wholly local
octahedral log³ proof remains an OPEN follow-up; minimal-node interpolation
is also OPEN. Audit03 independently accepted applicability of Thm4.1.

## 2026-11-12 — settled E4 convention

The log³ projection consequence retains **PROVED with explicit LITERATURE dependency** after the fixed-triangulation and Haar-normalization premises were rechecked. [Primary checks and AC decision](../final-d5/e4-verification.md).
