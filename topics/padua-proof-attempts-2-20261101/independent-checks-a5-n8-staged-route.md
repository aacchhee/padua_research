# Bounded review of the staged immutable N8 verifier

Reviewer: Codex `/root/a2_independent_route`, requested gpt-6.1-sol xhigh; runtime-resolved metadata are not separately exposed. Date: 2026-11-01. This is supplementary mathematical/operational code inspection, **not the required Claude audit**, an execution receipt, or an n8 count/global acceptance. Only this new receipt was written. No search, mathematical computation, source edit, Git operation or handoff was performed.

## Scope and own source hashes

Read the FULL staged driver, the complete frozen `Verifier.run` and `Verifier.global_values` functions, the verifier constructor, state-mutating node/leaf/disposition/root/boundary routines relevant to staging, and the original CLI call sequence. Read the supporting generic18 and uniform-gradient53 arguments as needed. This review concerns reordering execution of existing predicates, with no new mechanism or novelty content; it is not a fresh review of every field/arithmetic line of the immutable1318-line verifier.

Own source SHA-256 reads, refreshed at 2026-11-01T14:27:36Z, were:

| File under `code/` | SHA-256 |
|---|---|
| `a5_checker_n8_staged.py` | `82385dd392513c476e83ed7c5a59c63e602e77d50279fb51a3976ac5857021ef` |
| `a5_checker_n8.py` | `a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2` |
| `a5_checker_n8_controls.py` | `7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2` |

The driver's expected original tail AST pin is `14ec9c77c3afef4d585b3017a0d3b2f32f6cf0b705ff73c188fea92f4c2be7a5`. I inspected its extraction/compilation logic and the full original tail; I did not execute that logic or independently compute an AST hash. The driver checks both the original raw-source hash and this tail hash before using it. Structural controls and actual different-executor runs reported by root belong to their own records, not this receipt.

## Conclusion

**No blocking semantic or mathematical finding.** Under the frozen source guards and the stated final-input identity checks, the staged path executes the same interior, boundary, summary and global acceptance predicates on the same verifier state as the original complete run. An incomplete/failed phase never supplies complete count acceptance.

## Phase1 genuinely checks the whole interior

The driver validates an interior-only input: no edges/corners/boundary summary, no pending or unresolved paths, interior_complete=true, complete=false, and no existing mechanical-join metadata. It binds the exact raw interior bytes to a supplied SHA-256 before decoding, rejecting duplicate JSON keys through the old loader.

It constructs the original Verifier, so the original field/embedding/cardinal reconstruction executes. It then calls the ORIGINAL `verifier.run(original, allow_partial=True)`, which verifies every supplied node record, root, leaf and compatible mask/universal predicate, and calculates the exact prefix partition. Although allow_partial permits incomplete inputs in general, the staged driver subsequently requires complete_prefix_partition=true and interior_complete=true, with boundary_complete=false and count_certified=false. Thus allow_partial does not waive interior completeness in this route. Root accounting is additionally matched to both the list length and summary.

The phase1 receipt is atomically written as interior-only, without a count/global claim. A missing READY marker, deadline, source change or invalid final pair cannot turn it into a complete certificate. The process does not deserialize a verifier from that receipt; the same live object must survive into phase2. A restarted process therefore reruns phase1 rather than accepting a saved progress receipt as mathematical state.

## All needed mutable state survives exactly once

The same Verifier instance retains:

- Independently reconstructed field/cardinals, coefficient and derivative data, implicit-mask mode, and pure exact-pattern/interval caches.
- The complete verified root dictionary, masks, boxes, rational preconditioners and root-value intervals.
- Ordinary disposition/pattern counters, node cones/statuses/node-leaf count, universal-gradient counters/methods and the full flat/factor exception-occurrence lists.

The first original run has no boundary keys, so it never calls `boundaries`: `edge_flat_values` remains empty. The extracted phase2 tail calls `boundaries` once, populating that list once and returning edge/corner root/value records. It does not repeat node/root/leaf processing, so interior counters and exception occurrences are neither reset nor doubled. Boundary operations can fill pure exact-pattern caches without changing their mathematical meaning.

The original node routine returns exactly the four keys named by NODE_RESULT_KEYS. The driver copies their ACTUAL verified values from phase1, not reconstructed guesses. The tail's other incoming locals are self, certificate, allow_partial, leaves and complete_partition. Each is supplied explicitly: the same verifier, final certificate, false, typed-identical leaves, and the already verified true partition flag. All remaining tail locals are assigned within the extracted original body. No earlier original-run local or hidden closure is missing.

## Typed identity justifies not rechecking the interior

The final object has exactly the original top-level fields plus edges, corners and boundary_summary. Every original field except summary/metadata must be canonical-JSON identical, including field embedding, roots, node records, every leaf/pattern/hull, pending paths and unresolved paths. Canonical serialization separates boolean/integer/float encodings and rejects nonfinite numbers. Rational strings are compared literally, which is stricter than mathematical equality.

The only summary changes permitted are complete plus the added/recomputed edge/corner/total fields. Every other original summary field is typed-identical, including interior completeness and actual interior counts. Metadata may add only the specified mechanical_join object and change its source SHA; all other metadata fields remain typed-identical. The join object binds the original raw interior hash, byte count and original source identity. Thus the reused mathematical inputs cannot change between phase1 and the final tail.

READY is exactly schema-checked and bound to that same interior SHA. The actual final raw count/global bytes must match READY's two hashes before decoding. The original global checker is passed the actual final raw count SHA, preserving its count/global binding. At completion the driver rereads all three input files and requires unchanged raw hashes, checks the deadline and source pins again, then records the exact accepted pair and marker bytes. A later change of READY itself does not alter the already loaded/recorded pair; the mathematical inputs are the verified in-memory bytes and bound paths.

## The literal original tail and global predicates are preserved

The extractor selects the complete original run body from assignment to `no_unresolved` through return. It deep-copies that AST into a wrapper with the explicit incoming locals and compiles it in the original module namespace. Raw-source and expected AST guards make an unintended altered tail fail closed.

With allow_partial=false, the tail recomputes unresolved/pending status, invokes the original four-edge/corner verification, checks all old interior counters against the final unchanged summary, checks exact edge/corner/total counts and boundary disposition totals, and requires complete coverage. Supplying complete_partition=true is justified by phase1 plus literal leaf identity; no new unverified partition assertion is introduced.

The original `global_values` then uses the SAME roots and flat/factor occurrence list from phase1 and the edge-flat/root/corner data produced by this exact tail. Its complete occurrence counts, whole-leaf value bounds, all root-ID value enclosures, exact edge-constant values, corner identities and strict cut are unchanged. The uniform-gradient weak-maximum exclusions and node radial-ascent arguments were already verified on all identical leaves in phase1. No predicate or region is omitted by moving the wait between the two portions.

## Identity/reporting limits, without a new acceptance condition

The driver verifies the final literal boundary mathematics rather than trusting a boundary-input provenance claim. Mechanical-join boundary-source/input hash fields are checked for permitted shape and valid hash syntax; their claimed external pre-join artifact identities are not independently established merely by this driver. Those provenance claims need their separate join/manifest records. This does not weaken final count/global soundness, because the actual final boundary data are fully replayed and the final raw pair is explicitly bound.

The staged JSON is not byte-identical to the original CLI report. In particular the constructor still executes embedding verification, but the staged report does not copy every `embedding_result` diagnostic field that the old CLI appends. This is an output/reporting difference, not an omitted verification predicate. Final consumers must use the recorded accepted/count/global flags and exact input/source bindings, not treat an interior-only phase receipt as a complete result.

## Execution boundary

No staged driver, old checker, structural control or actual pair was executed by this reviewer. The source-hash checks above are provenance only. The requested hard deadline remains15:19UTC, and actual driver runs/final controls and the required Claude audit remain the orchestrator's separate obligations. Active verification did not need to wait for this routine receipt prose.

## Read-only addendum: bit-identical cached evaluator entry

At 2026-11-01T14:49:37Z, read FULL `a5_checker_n8_staged_cached.py` and its FULL controls source, and reread the old `evaluate`, `Interval.power`, `Interval.__mul__`, `interval_sum` and centered evaluation semantics. Own source hashes were:

| File under `code/` | SHA-256 |
|---|---|
| `a5_checker_n8_staged_cached.py` | `996c8f4dede1a3d8efed79b982dc53a7c12136c7c9e6e7e3872c67f8007168e9` |
| `a5_checker_n8_staged_cached_controls.py` | `e0baeaf38c69261cd20ede3c0d5df00ad78311ee4af5f844ee6f2f0ba6859ad4` |

**No blocking finding.** This entry changes the interval evaluator's execution implementation while preserving its returned dyadic endpoints exactly for the frozen checker's valid inputs. It is correctly disclosed as a runtime replacement; the unchanged old source bytes alone are not presented as proof that no runtime function was replaced.

### Exact endpoint equivalence

The old evaluator directly constructs powers x^0,...,x^8 and y^0,...,y^8 using `Interval.power`, then forms `c*(xp[i]*yp[j])` separately for every term and sums the resulting integer endpoints.

The new table uses the SAME direct powers and SAME `Interval.__mul__` to precompute each `xp[i]*yp[j]`. The cache key contains all four exact integer coordinate endpoints and precision. Thus its monomial interval for a requested pair is exactly the old intermediate interval, not a regrouped exact monomial or a tighter independently rounded bound.

For that interval m and coefficient interval c, old multiplication returns lower endpoint

`min(c.lo*m.lo,c.lo*m.hi,c.hi*m.lo,c.hi*m.hi)//UNIT`

and upper endpoint `ceil_div(max(the same four products),UNIT)`. The new loop performs precisely these operations for EACH term before adding to the accumulators. It does not move floor/ceiling outside the sum, combine repeated terms, cancel coefficients, or change multiplication association. Therefore each summand has the same endpoints and their integer sums are identical. Empty terms return (0,0) in both versions; repeated terms are retained separately. Negative, zero-crossing and point intervals use the same four-product and power rules. Python exact integers introduce no overflow/associativity change.

The frozen verifier only supplies exponents0,...,8 and exact integer dyadic endpoints at precision160. The new table enforces the frozen precision/UNIT relation on construction. It has maxsize512; eviction merely recomputes the same table. Nested tuples and the old frozen Interval dataclass make returned entries immutable. The table depends only on coordinates/precision, so it does not cache a mask, coefficient, sign, field embedding or acceptance predicate. Changes of coefficient data cannot reuse a wrong coefficient product through this cache.

### Installation, source guards and staged state

The entry imports the pinned base staged driver823 and its original checker a9, captures the original evaluate function, and requires that exact function before installation. It replaces only `check.evaluate`, the staged guard wrapper, and the receipt-writing wrapper. Fresh actual jobs begin with the original verifier state; the controls' benchmark verifier/counters are not reused by the real entry.

The new guard calls the ORIGINAL base guard, preserving its a9 main, old controls7 and driver823 checks. It additionally checks the new entry/control source stability and that the runtime evaluator is the installed cached function. The original tail extraction, leaf/mask enumeration, node/root/edge/global predicates, input identity checks and same-Verifier state flow remain unchanged. Old module functions resolve the new global evaluate function, whose exact output equivalence was proved above; pure cached derivatives/coefficient data are unaffected.

The receipt wrapper adds the actual execution-entry hash, new controls hash, base823 identity, explicit runtime replacement/backend label and cache statistics to RESULT metadata only. It does not mutate proof inputs or accepted/count/global flags. Phase1 and final receipts therefore distinguish the new entry from an unmodified runtime evaluator despite identical old file hashes.

### What was not executed here

The controls source compares old/new exact endpoints over actual and synthetic cases, immutable/bounded-cache and wrong-precision cases, and supplied universal leaves; its benchmark is explicitly not a count. Root reported two actual different-agent control executions with4926 endpoint comparisons and measured speedups. I did not execute or independently validate those outputs or timings. No inference about finishing before15:19UTC follows from this mathematical equivalence review.

The old slow runs' termination/nonacceptance and the new full runs starting afresh require their own execution records. This addendum accepts no partial old state as a replacement for phase1 and no complete count/global result before the original staged predicates finish successfully. No source, input, Git state or other path was edited by this reviewer.
