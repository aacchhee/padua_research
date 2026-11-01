# T-B5 — generic pattern commutant

- Rules/base: `cadb35066160e466cb1704b9791ad6f374446422`.
- Developer: Codex `/root/a1_develop`, requested gpt-6.1-sol xhigh; resolved runtime metadata unexposed.
- Result: **PROVED for every n≥2**, with sufficient pointwise condition that all x coordinates are distinct; [PD-T?proof-attempts-codex-02](../theory/proof-attempts-codex-02-generic-commutant.md).
- Stop: all-n done criterion reached; exact rational instances n=2,…,6 also checked. Claude audit-01 ACCEPTED; minor wording dispositions are in response-01.md.

## Gate and route

The A1 gate covered the complete registry, aliases and obstruction/disposition tables and the literature index before mathematical development. For this target additionally read programme IDEA-08, finite Favard -01, universal commutant counterexample -N04 and its exact code, `m2_common.py`, `m2_favard_commutant.py`, OPEN_TARGETS B5. Searched `commutant`, `cyclic`, `first column`, `generic`, `three-dimensional`, `spectral` in state, theory, tracks, topics and literature. Closest entries: programme IDEA-08 and the two source records; charter IDEA-014/039/051 concern neighboring pivot/ideal/implicit-Q mechanisms. This is completion of the explicitly existing B5 question. No historical novelty claim.

Root proposed the short all-n route after A1 was finished: distinct x coordinates make e_0 cyclic for H_x; a commuting matrix is determined by its first column; the first column of P_y has only three permitted entries. This closes the upper bound in every degree. P_x⊆P_y and the positive first pivots supply three independent elements I,H_x,H_y. The proof includes real-analytic Cholesky dependence and a global polynomial exceptional set, so it does not rely on extending a local nonzero analytic minor across a possibly disconnected parameter domain.

## Exact rational witnesses and executed check

Use nodes (t,t^(n+1)), t=1,…,N, w=1/N. The written sparse-polynomial/Rolle argument proves unisolvence for every n. Code independently constructs V and inverts it rationally for n=2,…,6, constructs rational monic sections by LDLᵀ, checks support, commutation, positive norms and positive orthonormal pivots, then computes the reduced spectral constraint rank.

```text
python topics/padua-proof-attempts-20261101/code/b5_exact_instances.py > topics/padua-proof-attempts-20261101/outputs/b5_exact_instances.json
```

Executed successfully with Python 3.12.14, SymPy 1.14.0. No random seed, tolerances or floating-point arithmetic. All pair assertions passed. At n=2,3,4,5,6, N=6,10,15,21,28; reduced ranks are 3,7,12,18,25. The all-n proof gives original map ranks 14,33,62,103,158 and commutant dimension three in each instance. The last N−3 rows of an invertible V⁻¹ always have rank N−3, so the reduced-rank calculation does not independently test that dimension. The witness checks establish unisolvence, positive norms/pivots, pattern and commutation. The large full radical-valued commutator matrix was **not** formed. Rank invariance under diagonal similarity and the exact reduction to the last N−3 rows of V⁻¹ are proved in the theory file.

Receipt: [b5_exact_instances.json](../outputs/b5_exact_instances.json), 5,327 bytes, SHA-256 `251496a1a117054608dd55d32c7dfa5441c5af34cf7cb00d1f99ec0e9e80da02`. Script SHA-256 `fb56be6166ce10ecae213cd1c4e169594a52b0a922058e52934b88ccd0edf18b`. Pair hashes and exact Vandermonde determinants appear in the receipt.

## Failed and deferred routes

No mathematical route failed. A full symbolic commutator rank with Cholesky square roots was avoided after the proved rational spectral reduction made it unnecessary. The all-n stretch did not block the finite witnesses: both were completed. Colliding x coordinates and the Padua exceptional commutants remain outside the sufficient pointwise theorem; the original universal PD-N remains valid.

## Runs needed

- Claude audit-01 is ACCEPTED. Remaining PR integration is described in pr-prep.md.
- Independent exact regression and proof inspection are complete; see independent-checks.md and audit-01.md.

Next: `Codex (gpt-6.1-sol medium): Continue codex/padua-proof-attempts-20261101 — reconcile PR #9 after PR #6 integration.`
