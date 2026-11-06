# C4 coordinate interface validation

ID kind: verification record; no new mathematical-result ID.
Aliases: monic Hessenberg bridge; integer-node coordinate conversion.
Split from: none. Split into: none.

## Statement

For the six finite cases (both frozen PD-T290 families, N=4,6,8), exact rational computation verifies the implemented NN-to-monic upper Hessenberg extraction by evaluation at every node; fixed nonzero diagonal similarity followed by monic normalization recovers the original matrix; affine conversion from normalized nodes to integer nodes equals an independently reconstructed matrix. This is local implementation evidence, never external-source fidelity.

## Definitions and assumptions

Path nu_k=(ceil(k/2),floor(k/2)), first e1. Matrix columns encode x Q_k=Q_(k+1)+beta_k Q_k+gamma_k Q_(k-1)+delta_k Q_(k-2). Diagonal beta, first superdiagonal gamma, second superdiagonal delta, subdiagonal1. All underlying mixed systems in these cases are solved exactly over Fraction by the predecessor auditor's defining-moment routine.

For explicit D, similarity means D^-1 H D. A raw four-term matrix with subdiagonal a_i is made monic by leaving its diagonal, multiplying superdiagonal i by a_i, and second superdiagonal i by a_i a_(i+1), setting subdiagonal to1. A zero subdiagonal is rejected. These operations do not determine which gauge an external solver returns.

For t=s z+b, monic polynomials transform as R_k(t)=s^k Q_k((t-b)/s). Thus beta_t=s beta_z+b, gamma_t=s^2 gamma_z, delta_t=s^3 delta_z, and subdiagonal remains1. In matrix form use D=diag(s^k) and H_t=D^-1(s H_z+b I)D. A naive s H_z+b I does not preserve the unit subdiagonal. Topic conversion has s=b=(N-1)/2. No norm is invariant under a general diagonal similarity; translation also changes a relative matrix denominator.

## Status by part

Overall status: MEASURED (six exact finite implementation checks; no all-N computer proof, external metric or new theorem).

## Depends on

PD-T432 extraction formula, PD-T286/289 definitions. The checker uses the frozen predecessor exact-moment polynomial construction, not third-party code.

## Checks and evidence

Executed from repository root:

`python3 topics/nn-mop-conditioning-20261106/code/c4_normalization.py > topics/nn-mop-conditioning-20261106/c4-interface-check.json`

Exit0. [Receipt](../c4-interface-check.json) pins checker and dependency SHA256, Python version, case list and all three exact identities. An initial development run used the inverse affine diagonal and failed the affine identity; corrected to D=diag(s^k), then all six cases passed. No external solver ran. This worker's own check is not an independent audit.

## Sources

Local definitions above suffice for the algebra. External fulltext access and the precise coverage limits are recorded in [external-code.md](../external-code.md), not used to waive fidelity gates.

## Scope and open items

This interface is useful preparation for M2. It does not return a full NN triangle from one step-line path, does not implement IEP-MOP, and does not claim a LIT-347 condition number or stability comparison. M4 external rerun and M2 fidelity remain BLOCKED by missing archive.

## History

2026-11-06: Codex, assigned gpt-6.1-sol medium; rules/source b4a04981d42c7cd872957facf5e3995e4096ca67. New finite verification record only.
