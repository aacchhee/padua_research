# PD-T?padua-3d-20261106-usable-U1-OLS — same-node covariance comparison

ID kind: PD-T. Aliases: ordinary least squares; Gauss–Markov right inverse.
Split from: none. Split into: none. No final ID allocated.

## Statement

For every real full-column-rank M by N matrix V, let
`C_0=(V^T V)^−1 V^T`. Every other linear reproducing coefficient map
C, meaning CV=I_N, satisfies

`C C^T − C_0 C_0^T = (C−C_0)(C−C_0)^T >=0`.

Consequently, with a continuously orthonormal output basis and iid
mean-zero noise of varianceσ² at the same M nodes, ordinary least squares
minimizes integrated variance among all linear reproducing maps. Its
integrated risk reduction relative to C is exactly
`sigma² ||C−C_0||_F²`. This applies to both parity Haar-WLS maps for all
n>=1. At a fixed total replication budget, multiply both same-node risks
by the common factor M/B; the ordering is unchanged.

## Definitions, assumptions and status

Overall status: **PROVED**, standard known Gauss–Markov algebra proved
here to match the actual operator/noise normalization. Reproduction is
unbiasedness for functions in the finite polynomial space, not absence
of approximation bias for arbitrary f. No Gaussian assumption is needed.

## Depends on

Elementary matrix algebra; parity full column rank follows from
[U1 recipe](u1-parity-recipe.md). No external source theorem or numerical
rank test is needed.

## Proof

Put D=C−C_0. Then DV=0, whence
`D C_0^T=D V (V^T V)^−1=0`, and its transpose also vanishes.
Expanding `(C_0+D)(C_0+D)^T` proves the identity and positive
semidefinite order. Orthonormality converts integrated variance to the
coefficient covariance trace as in [U1 noise](u1-noise-bound.md).
Taking traces gives `tr(D D^T)=||D||_F²` and the claimed reduction.

## Checks, sources and scope

The producer's Round2 uses economic Householder QR, not formed normal
equations, to compute the stated OLS map. It saves both actual operators,
checks reproduction and the covariance identity and reports the measured
size of the reduction, approximation changes and setup/application cost.
Those measurements remain separate from this proof. The method is known;
the shared gate records the relevant least-squares predecessors.

No conclusion says OLS improves deterministic function error, bounded
adversarial-noise amplification, or noise with unequal/correlated variances.
In particular the exact Haar moment formula may remain the useful solver
when its lower setup cost outweighs a finite iid-noise gain. Practical
replacement is decided only by the prospective comparison, not by this
variance theorem alone. Independent mathematical checking remains separate.

2026-11-08 audit04 wording note: "fixed total replication budget" above means balanced replication, B/M observations at every node with B divisible by M, as defined in [U1 noise](u1-noise-bound.md). Separately optimized unequal integer repeats at a fixed B are a different normalization; see [U1 continuation](../u1-continuation.md).

## History

2026-11-07, Codex developer, assigned Sol xhigh; prospectively registered
known solver comparison after published shared gate. No novelty claim.
