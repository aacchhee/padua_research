# PD-T?padua-3d-codex-T9-05 — interpolation correction norm

ID kind: PD-T. Aliases: T9-EXTRACT; near-Padua projection route.
Split from: none. Split into: none. T9 route5 is its task provenance.

## Statement / definitions

Suppose a projection H:C(K;R)→V, dim V=N, has the finite sampling
representation Hf(z)=Σ_{y∈Y}f(y)h_y(z), with distinct finite nodes
Y⊂K and h_y∈V. Let X={x₁,…,x_N}⊂Y, and let C_{ij}=h_{x_j}(x_i).
If C is invertible, X is V-unisolvent and its interpolation projection is

I_Xf(z)=[h_{x₁}(z),…,h_{x_N}(z)] C^{-1} f_X,

with **||I_X||≤||H||·||C^{-1}||_∞**, where the matrix norm is maximum
absolute row sum. No cubature or positive weight assumption is needed.

## Assumptions / status

K is compact metric, V⊂C(K;R) finite dimensional, H is a projection.
Overall status: PROVED. This is a standard finite-dimensional correction
lemma; no novelty claim. Candidate disposition: retained reduction,
explicit norm-controlled extraction DEFERRED.

## Depends on / sources

Elementary linear algebra; DMVX LIT322, WAM LIT382, and hyperinterpolation
LIT391 are context only. No unverified O(log³ n) source statement is used.

## Proof

The N functions h_{x_j} are linearly independent since their evaluation
matrix C is invertible. They therefore span V. The displayed combination
lies in V and takes the prescribed values on X, proving unisolvence and
the formula. For its cardinal row ℓ(z)=h_X(z)C^{-1},
Σ_j|ℓ_j(z)|≤(Σ_i|h_{x_i}(z)|)||C^{-1}||_∞.
For finite distinct sampling points the norm of H equals
sup_zΣ_{y∈Y}|h_y(z)|: finitely assigned signs extend by disjoint
continuous bumps of norm≤1. Taking sup_z proves the estimate.

## Scope / open items

Applied to total-degree V=Π_n³, the lemma identifies a sufficient missing
estimate: both a verified small norm of H and a selected N-node submatrix
with controlled ||C^{-1}||_∞. Invertibility alone is insufficient to
transfer the norm bound. The lemma does not prove that every frame has a
subset meeting this sufficient estimate, nor that this estimate is necessary.
Precision2n cubature gives a classical hyperinterpolation projection via
orthonormal moments. Precision2n−1 alone leaves top-degree Gram terms
uncontrolled; verify/correct that Gram matrix before invoking the lemma.

T5's bound for exact degree2n−1, using q=n−1, gives r+rank/2=12,24,41
at n3,4,5, below N=20,35,56; it does not exclude those target counts.
Thus the known near-minimal node count and commutator rank do not close
this norm gap. Route5 resumes with a concrete verified projection and
either an analytic C^{-1} bound or a preregistered finite extraction test
with matched QR/Leja controls. No such extraction was run in T9.

## Checks / history

Analytic proof, no executable premise. 2026-11-06 Codex: expose the exact
norm factor before proposing that ~1.5N-node hyperinterpolation transfers
to minimal interpolation; retain the original near-Padua target OPEN.
