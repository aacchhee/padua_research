# T1 supplementary independent review and replay

Status: **IN PROGRESS; no fresh complete count accepted yet.** This is a verification record, not a new mathematical claim or the required Claude audit.

Reviewer: Codex `/root/t1_independent`, separately assigned from developer `/root/t1_certification`; mathematical review at requested `gpt-6-astra high` (serving metadata not independently exposed). Rules read at `3f5196cf3639407c25b021fa30f70cc1d3ae113a`. Working branch `codex/padua-lebesgue-followups-20261103`, base `440d1079e42c3ef21c40d1cf8870f5b206410c6a`. No Git mutations by this reviewer. Files owned: this record and `evidence/t1-independent*`; scratch `/workspace/scratch/lebesgue-t1-independent`.

Scope is completion of existing PD-T180/184 using frozen A5 acceptance predicates. No novelty-bearing candidate is introduced, so this supplementary check does not claim a fresh novelty audit. Read AGENTS, WORKFLOW, CODEX, handoff 01, topic LOG/attempt/gate, frozen schema and theories 15/18/53/60/61/64/65, frozen checker, cache/staged wrappers and controls, and relevant prior Claude audit/response and A5 subaudit records. Earlier audit acceptance did not cover the full n8 tree or boundary; their present obligations are independently reassessed below.

## Mathematical reduction and trusted base

The finite reduction has been reconstructed independently. For every point, `lambda=max_s sum_i s_i L_i`; every active signed polynomial has a strict local maximum at a strict maximum of lambda. At an interior point its gradient vanishes and its Hessian is negative semidefinite. Strict cardinal interval bounds force the appropriate signs, while ambiguous intervals retain both signs, including crease and crossing points. A finite prefix-free dyadic tree of Kraft mass one covers the square, with closed leaf faces harmlessly overlapping.

Each ordinary leaf must dispose of **every** compatible mask. Identically zero coordinate derivative excludes strict maxima by a constant coordinate line. A derivative interval excluding zero contradicts stationarity; a strictly positive Hessian diagonal or strictly negative determinant contradicts negative semidefiniteness. For a regular common-gradient factor, nonvanishing residual and regular squarefree factor produce a local stationary curve with constant polynomial value. For a regular-point exclusion, exact stationarity plus whole-hull injectivity forces the candidate to the exact node or regular cardinal zero, both excluded. These predicates never use mere singularity or smallness as an exclusion.

For root witnesses, strict Krawczyk inclusion and `||I-C H||_infinity<1` imply a unique gradient zero inside the rational root box. The rational preconditioner is explicitly nonsingular. Negative-definite Hessian and strict cardinal signs make this a strict lambda maximum. A root-reference hull contains the **entire** leaf and root box, so gradient injectivity identifies every stationary candidate with that root. Pairwise disjoint closed root boxes prove distinctness without proximity merging. The universal-gradient predicate reconstructs the forced polynomial and sums absolute derivative bounds for every ambiguous cardinal; it therefore covers all active masks, including zero cardinals. The node-cone proof uses the exact directional breakpoint minimum and radial Taylor remainder `R sum H_i < m`; face geometry and strict leaf containment preserve feasibility. At the node, partition of unity gives `lambda>=1=lambda(node)`.

On each open edge, exact squarefree union plus the multiplicity-one cover excludes every crease by the tangential sign-flip argument. Complete rational norm-root partitions, independently checked by Sturm counts, contain all chosen-embedding roots. Samples in every gap between norm-root intervals therefore include every actual sign region; conjugate roots only add gaps. All nonconstant sampled masks have every root of the derivative after removing arrangement factors covered. Dispositions require strict exclusion or positive curvature, or a unique tangent maximum with strict cardinal signs, negative second derivative and opposite endpoint derivative signs. Strict inward descent makes an accepted tangent maximum relative to the square; strict inward ascent excludes it. Zero/degenerate cases remain unresolved. At corners, nodes are excluded and **every** active sign choice must have both inward derivatives strictly negative. The four open edges, four corners and open interior exhaust the square.

The field proof PD-T179 establishes the physical embedding, not a numerical root selector: irreducible quartic/cubic generators of coprime degrees give degree 12; the tensor/primitive conversions are exact, and Chebyshev factorizations plus rational monotonicity brackets select the largest roots. The checker independently constructs the 45 by 45 Vandermonde inverse, all 2025 cardinal identities, partition of unity and quadratic reproduction. Thus producer kernel coefficients, measured maxima and literature counts are not premises.

Trusted implementation base: CPython integers/Fraction and execution semantics; SymPy exact algebra, DomainMatrix inverse, polynomial gcd/squarefree/factor/resultant operations; python-flint exact rational/integer arithmetic; the reviewed checker, exact outward 160-bit dyadic interval operations, and bit-identical cache implementation. Arb complex-root discovery is a producer proposal mechanism: checker Sturm coverage does not trust its root-selection output. The same frozen checker lineage is a residual common-mode risk; a different-agent execution is not a second independently written implementation. Claude audit remains required. No global-value assertion is added by this strict-count task.

## Code review and findings

Frozen `a5_checker_n8.py` SHA-256 `a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2` was read across field reconstruction, interval arithmetic, node cones, all leaf predicates, edges/corners, accounting and CLI. Frozen cache entry SHA-256 `996c8f4dede1a3d8efed79b982dc53a7c12136c7c9e6e7e3872c67f8007168e9` preserves ordered per-term multiplication and outward floor/ceiling rounding; caching only reuses immutable monomial intervals keyed by all endpoints and precision. Its mathematical operation identity was reviewed as well as tested.

`code/t1_boundary.py` extracts the unchanged frozen edge loop, checks its AST identity after adding only a checkpoint callback, and replaces corner symbolic substitution with native exact field polynomial evaluation. For each corner the same node identity, active zero signs, signed inward derivative sums and strict sign tests are preserved. Its native sums are algebraically identical by linearity of evaluation and differentiation; full boundary acceptance still requires the independent checker. Producer n4–7 crossvalidation is separately attributed to development until independently replayed.

Finding I1 (receipt integrity, resolved): the initial count-only wrapper let the frozen CLI publish a success-looking receipt before the wrapper's after-run guards. Development revised `code/t1_check.py` to route the frozen output into an unpublished temporary file and atomically publish only after checker/cache/wrapper source guards and input before/after hashes pass. Revised SHA-256 `0345e62ef9bb88fa11640e135d211648611c9536b85fec528d694e94ef57a69f` was reviewed and independently exercised. Seven publication controls passed: success/rejection return codes and flags preserved; checker exception, post-source-guard failure, input mutation, wrapper mutation, and counterfeit input binding leave no published receipt. Temporary cleanup also passed. These use a fake checker and claim **no mathematical acceptance**.

Finding I2 (optimized-mode guards, open): the parent noted that new entry wrappers use `assert` without refusing Python `-O`. Current executed commands use normal `python -B`, so the assertions are active and this does not invalidate those executions. Development must add an explicit optimized-mode refusal after in-flight jobs finish, preserve the exact executed old source hashes/blobs, and record/recheck the guard-only delta. Do not mutate sources while their running jobs guard them. In particular, `t1_join.py` binds the boundary wrapper to its physical source hash; a subsequent source edit must not silently relabel an older boundary artifact.

`code/t1_join.py` SHA-256 `a88b18f2a617d7dac03a5db7ba2a89a32cae731cd2f7b6c5a0ea400e5b554b61` preserves literal interior/boundary mathematical components, delegates frozen structural validation, checks raw inputs and ancestry, and explicitly emits `count_certified:false`. Its expansion of the source allowlist concerns known physical source identities, not a new proof predicate. Independent full checker replay is still mandatory. Thirteen independent synthetic controls (one positive, twelve rejected) verify literal copies, source/raw hash checks, missing/pending/unresolved cases, count accounting and preservation of an existing different output.

## Completed executions

All commands below ran from `/workspace/padua_research`; Python commands use `-B`. No seeds; fixtures and arithmetic are deterministic, timings are descriptive only.

1. Historical fixture restoration, exit 0:

   `python -B tools/cold_storage.py restore padua-proof-attempts-2-20261101 --dest /workspace/scratch/lebesgue-t1-independent/cold`

   The canonical tool restored and checked all 23 manifest-pinned artifacts. The n8 proposal initially supplied controls/runtime benchmarking; the parent subsequently authorized a separately labeled full historical replay as a runtime hedge, **not a replacement for fresh T1 evidence**. Its path under that destination is `topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz`, 637163 bytes, SHA-256 `a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324`.

2. Frozen exact-cache controls, exit 0, 26.65 seconds:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 600 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8_staged_cached_controls.py --interior /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz --interior-sha256 a3b4f278a322338fb65f60922b4251265288148e1a09fd22882215004e81c324 --output /workspace/padua_research/topics/padua-lebesgue-followups-20261103/evidence/t1-independent-cache-controls.json`

   [Receipt](evidence/t1-independent-cache-controls.json): all 4926 exact endpoint identities passed, including 333 polynomial vectors, 10 common boxes, 44 actual root boxes and four axis hulls, empty/repeated terms, points/cross-zero intervals, immutable cache, maximum size 512 and wrong-precision rejection. One hundred actual universal-gradient leaves took 6.66 seconds original / 2.40 seconds cached. This extrapolates to roughly an hour for the historical tree before extra ordinary-mask work; it is not a full replay.

3. New wrapper publication controls, exit 0:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps python -B topics/padua-lebesgue-followups-20261103/evidence/t1-independent-wrapper-controls.py --driver topics/padua-lebesgue-followups-20261103/code/t1_check.py --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-wrapper-controls.json`

   [Control source](evidence/t1-independent-wrapper-controls.py) and [receipt](evidence/t1-independent-wrapper-controls.json) preserve exact reviewed source identity and seven observed outcomes. These are structural fault controls only.

4. Frozen mathematical controls, exit 0, 98.03 seconds:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 1200 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n8_controls.py /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz --spatial-certificate /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz --output /workspace/padua_research/topics/padua-lebesgue-followups-20261103/evidence/t1-independent-frozen-controls.json`

   [Receipt](evidence/t1-independent-frozen-controls.json): 37 cases, including 30 rejected counterfeits. Every supplied node cone was independently reconstructed; embedding/conversion faults, missing node/direction/breakpoint, false gap/geometry/Hessian bounds, mixed leaf predicates, invalid universal-gradient axes, missing prefix/mask/Sturm coverage, singular root preconditioner and zero-Hessian false exclusion were rejected. Exact tensor norms and rational endpoint values agreed with independent native reference operations. Python 3.12.14, SymPy 1.14.0, python-flint 0.9.0, FLINT 3.6.0; original/control source after-hashes unchanged.

5. Independent producer-cache crossvalidation, exit 0, 20.70 seconds:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 600 python -B topics/padua-lebesgue-followups-20261103/code/t1_memo_controls.py --frozen-output-dir /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-memo-crossvalidation.json`

   [Receipt](evidence/t1-independent-memo-crossvalidation.json): 41172 exact endpoint equalities on frozen n4–7 certificate leaves, all root boxes and all signed root-polynomial derivatives, with endpoint payload hashes matching the developer's separately executed run. This is an actual second execution, not reading the first receipt. `code/t1_memo.py` SHA-256 `d910cb5857a0c09288330925ca833f820690ef76553d8e66402c3e5e352b7e35` was reviewed: captured frozen powers/products and identical four-product outward coefficient rounding preserve each original endpoint exactly. `code/t1_produce.py` SHA-256 `1ac5cbb83302d12006f35f042954fd6c76881e263ed6de065ca22c5302a77664` changes the field/module/node evaluator references and adds execution metadata, leaving the frozen solver/continuation and predicates intact.

6. Independent producer-cache edge cases, exit 0:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 300 python -B topics/padua-lebesgue-followups-20261103/evidence/t1-independent-memo-controls.py --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-memo-controls.json`

   [Source](evidence/t1-independent-memo-controls.py), [receipt](evidence/t1-independent-memo-controls.json): 5310 exact endpoint equalities over n4–8, including empty/repeated terms, negative and crossing intervals, point/subgrid cases, immutable cache, 512-entry bound and changed-scale/noninteger cache-miss rejection. The first harness invocation erroneously asked the degree-four reference to evaluate degree-eight monomials and exited with IndexError; the harness was corrected to each frozen reference's supported degree before the successful rerun. No producer defect or failed mathematical witness was inferred from that harness error.

7. Frozen continuation structural controls, exit 0:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 120 python -B topics/padua-proof-attempts-2-20261101/code/a5_n8_continue_controls.py --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-continuation-controls.json`

   [Receipt](evidence/t1-independent-continuation-controls.json) checks unchanged helper/traversal AST, prefix accounting, exact restoration and malformed lineage/root/mask/node/leaf records. Synthetic fixtures only; no mathematical witness is accepted and no search advances.

8. Native corner predicates against all frozen n4–7 certificates, exit 0:

   `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 600 python -B topics/padua-lebesgue-followups-20261103/code/t1_corner_certificate_controls.py --frozen-output-dir /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-corner-certificate-controls.json`

   [Receipt](evidence/t1-independent-corner-certificate-controls.json): all four corner records exactly match the frozen certificate at each degree; independently checked 8, 8, 16 and 16 all-active masks respectively. This verifies the native classification implementation independently against the previously certified outputs; no n8 count is inherited.

   An additional redundant direct symbolic `Poly.eval` comparison ran as `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 600 python -B topics/padua-lebesgue-followups-20261103/code/t1_corner_crossvalidate.py --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-corner-crossvalidation.json`. Degrees 4–6 completed with 180/252/336 exact value/derivative equalities. The degree-seven phase was intentionally terminated, exit 143, to free the fourth-core budget for the consequential fresh runs and full replays after the all-degree certificate comparison above had passed. [Interrupted-run receipt](evidence/t1-independent-corner-crossvalidation-interrupted.json) preserves those partial outputs and source identity; no all-degree pass or missing completed receipt is claimed.

9. New join wrapper, exit 0:

   `python -B topics/padua-lebesgue-followups-20261103/evidence/t1-independent-join-controls.py --driver topics/padua-lebesgue-followups-20261103/code/t1_join.py --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-join-controls.json`

   [Control source](evidence/t1-independent-join-controls.py), [receipt](evidence/t1-independent-join-controls.json): all thirteen synthetic structural controls passed, with no mathematical certificate acceptance.

## Runs in progress and needed

- Historical reference whole-interior replay launched separately on the above pinned proposal, with a 10800-second outer cap: `PYTHONPATH=/workspace/scratch/lebesgue-t1/deps timeout 10800 python -B topics/padua-lebesgue-followups-20261103/code/t1_check.py /workspace/scratch/lebesgue-t1-independent/cold/topics/padua-proof-attempts-2-20261101/outputs/a5_n8_interior_candidate.json.gz --allow-partial --output topics/padua-lebesgue-followups-20261103/evidence/t1-independent-reference-interior-check.json`. Stdout/stderr live under scratch as `reference-interior-check.stdout` / `.stderr`. A launched or partially printed run is not yet a pass.
- Native-corner controls are complete within the explicitly recorded scopes above; the redundant symbolic run's unexecuted n7 remainder is not needed for the already completed certificate comparison.
- Fresh producer interior and boundary artifacts are still in progress. Independently replay every fresh node/root/leaf/mask and all edge/corner candidates once complete, recording actual hashes, commands, source guards, exit codes and complete accounting. Neither partial-progress output nor an incomplete producer flag can close these obligations.
- Preserve bounded small receipts; large certificates/logs remain scratch or manifested cold storage. PROVED requires the durable finite reduction, committed reviewed checker/evidence records, retrievable certificate identity and **completed** different-agent replay. This record presently authorizes no upgrade of PD-T180 or PD-T184.
