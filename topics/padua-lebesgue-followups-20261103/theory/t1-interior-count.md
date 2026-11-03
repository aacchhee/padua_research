# PD-T184 follow-up — complete degree-eight strict interior count

ID kind: PD-T (verification/completion record for existing PD-T184; no new ID).
Aliases: T1 interior; exactly44 degree-eight maxima.
Split from: PD-T180's interior stratum.
Split into: none. PD-T183's proved lower bound is preserved separately.

## Statement

For nodes (cos(jπ/8),cos(kπ/9)), 0≤j≤8, 0≤k≤9, j+k even, let L_i be the total-degree≤8 cardinal polynomials and λ=Σ_i|L_i|. The open square (-1,1)² contains exactly44 distinct strict local maxima of λ. This is the unchanged registered target;44 is never an acceptance requirement or discovery seed.

## Definitions

Exact physical field/embedding: PD-T179. The closed dyadic widest-side leaves cover the square; active sign masks are all choices of signs agreeing with each nonzero cardinal. Boundary leaves may also contain interior points. Root enclosures and leaf references use rational boxes and rational preconditioners at precision160.

## Assumptions

Frozen A5 finite predicates under PD-T167, PD-T170 and PD-T178; complete supplied exact finite partition, all compatible masks, exact independently reconstructed cardinal polynomials and chosen field embedding, positive node gaps with all breakpoint/remainder obligations, strict Krawczyk/Hessian/cardinal/injectivity root witnesses, and disjoint roots. Actual complete different-agent replay is required before promotion.

## Status by part

Overall status: OPEN. No complete fresh tree or replay yet. The existing independently proved lower bound PD-T183 is unchanged; supporting lemmas do not promote this target.

## Depends on

PD-T179 (field), PD-T167 (node-cone exclusion), PD-T170 (generic spatial-certificate correctness, source theory18), PD-T178 (universal compatible-gradient leaf), and PD-T183 (existing lower bound). ID mapping crosschecked against PROOF_STATUS at rules head.

## Checks

[Attempt](../attempts/T1.md), [pre-run gate](../gate-t1.md), frozen-schema `topics/padua-proof-attempts-2-20261101/code/a5_n8_schema.md`, and new count-only driver `../code/t1_check.py`. Source/environment receipts under evidence/t1*. Mathematical predicates remain frozen; runtime monomial memoization is bit-identical and separately crossvalidated on frozen n4–7 certificates.

## Sources

Registered A5 / IDEA-206 / IDEA-299; no external theorem or novelty claim. LIT-388 Table3 is comparison-only after the finite result.

## Proof or evidence

The written finite reduction is inherited from PD-T184, not re-proposed. Given an accepted complete certificate, take any strict interior maximum z and a closed leaf Q containing it. Because λ=max_s P_s for P_s=Σ_i s_i L_i, every active P_s at z also has a strict local maximum there; its gradient vanishes and its Hessian is negative semidefinite. Every such active mask is among the leaf's compatible masks, including zero-cardinal choices.

A verified universal-gradient leaf contradicts stationarity for every compatible mask. A node-cone leaf excludes strict maxima by the complete breakpoint gap/radial remainder/geometry proof. In an ordinary leaf, each compatible mask is disposed by the frozen exact predicate: nonzero gradient, strictly incompatible Hessian, exact regular-point or factor exclusion, flat polynomial exclusion from strict maxima, or a reference to an accepted strict root. Root references verify injectivity on a convex box containing the entire leaf and root enclosure, so any surviving stationary maximum equals that accepted root. No singular-Hessian-only exclusion, Newton-location assumption, symmetry shortcut or unverified progress prefix is used.

Every accepted root box supplies existence, uniqueness, negative-definite Hessian and strict cardinal signs. Pairwise-disjoint root boxes establish distinctness. Thus the number derived from complete verified root records is exactly the strict interior count. At present those finite hypotheses remain unverified for the new complete run, so no promotion is made.

## Scope

Degree8 strict interior maxima only; includes x=0. No boundary, global-value or all-degree conclusion.

## Open items

Complete fresh producer/continuation, complete direct frozen checker run, independent full replay and required Claude audit. Retain any failed/capped artifact and actual source hashes.

## History

2026-11-03, Codex /root/t1_certification, configured gpt-6.1-sol medium (parent-reported), rules3f5196cf3639407c25b021fa30f70cc1d3ae113a; unchanged target and OPEN status before finite completion.
