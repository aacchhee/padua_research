# Native finite-certifier implementation candidates

2026-11-03. Rules/input:`8a1f394739293953e1566fd24a0a193cc78ff26f`; base:`440d107`. This is a retrospective implementation ledger, compiled by the Codex gates worker (gpt-6.1-sol medium) from the two developers' attempts and READMEs. It does not retrospectively preregister tests or claim that this worker executed their runs. Owners' receipts and final independent checks govern the accepted range.

The full [IDEA-320 final entry](../../padua-argmax-alln-20261101/FINAL_CANDIDATES.md#idea-320), its [original formulation and execution history](../../padua-argmax-alln-20261101/ideas.md), and its registry row were read. Both candidates implement the existing PD-T210 sufficient criterion. Neither proposes new mathematics or novelty. A fresh mathematical ideas-generation gate is unnecessary for these bounded ports; the campaign's broader novelty/audit obligations remain with root.

<a id="idea-343"></a>

## IDEA-343 — Compiled exact heavy path for IDEA-320

Provisional alias: `IDEA?argmax-effective-native-producer`.

Aliases: C/GMP producer; native PD-T210 branch and bound; compiled tensor Bernstein construction.

- Question / scope: can the existing global-maximum-only finite certifier run faster within the sandbox while preserving its exact/outward acceptance criterion and certificate schema?
- Mechanism and hypotheses: C/GMP implements corrected cardinal monomial construction, both exact-rational tensor Bernstein transforms, de Casteljau subdivision, absolute-interval sums and corner/bound predicates. Python supplies exact rational cosine seeds/constants, orchestration and JSON. Fixed-point scale2^192 and the reference arithmetic operation order are preserved. The current implementation inherits2<=n<=100; this range is an implementation limit, not a promise of completed certificates.
- Closest registry entries (read in full): IDEA-320 and its original candidate. PD-T210 is the inherited implication being implemented; IDEA-290–302 are background predecessors cited there, without a new comparative or priority claim here.
- Separation criterion vs closest entry: implementation-language and storage-lifetime changes only. The mathematical target, sufficient condition and leaf meaning are unchanged. There is no intended mathematical separation; coefficient, metadata or leaf-verdict disagreement would invalidate the claimed faithful implementation until resolved.
- Literature baseline and search limitations: no external literature technique or novelty claim; no additional literature search was performed for this port ledger.
- Applicable obstructions and exact hypotheses broken: non-effectivity of the all-n localization argument is untouched. Faster finite certificates do not supply an effective n0. Interval widening or a search timeout can leave a partial cover; neither is a counterexample to PD-T099.
- Novelty gate verdict: **variant with implementation difference**, mathematically the same IDEA-320 criterion.
- Cheapest decisive test: exact initial-coefficient and metadata equality with the Python reference at small degrees, unchanged-checker acceptance, and deliberate-corruption rejection before using larger certificates.
- Kill criterion recorded before testing: handoff02 requires reference-checker agreement on the overlap degrees and independent large-degree acceptance. A discrepant bound, incomplete cover or unvalidated acceptance blocks a finite theorem upgrade. This ledger adds no retrospective runtime cutoff.
- Test discriminability: integer-for-integer agreement checks rounding order as well as formulas; independent acceptance verifies the actual cover. Passing small degrees does not prove every future implementation output correct or imply a speedup at large n.
- Actual test results and evidence: the producer developer reports coefficient equality at n2 and9 (54 and5500 intervals), reference acceptance and14 rejected corruption cases, plus honest rejection of acceptance for a partial cover. Subsequent overlap/final-source runs are described in [the producer attempt](../attempts/native-producer.md), which owns current completion status, and [README](../code/native_producer/README.md). This compiler of the ledger has not independently executed those runs. Final-source provenance snapshots supersede interim artifacts.
- Disposition: **retained as a bounded implementation variant**, supported at its documented finite scope by PD-T246 and the accepted [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md). No new mathematical rejection or all-degree claim.
- Disposition reason: the documented small exact equality/control checks support continued use within the validated scope; actual finite-range conclusions belong in separate theorem records supported by accepted evidence.
- Canonical theory / negative-result ID: PD-T210 inherited; finite degree-range continuation is PD-T246. No PD-N is warranted by a faithful port or unfinished run.
- Topic / audit / history: authorized in handoff02's C/FLINT-or-GMP amendment. C/GMP used because it satisfies the permitted exact-arithmetic alternative. Developer identity/model disclosures and measured costs remain in the attempt; root owns G1 projections, commits and cold-storage manifests.

<a id="idea-344"></a>

## IDEA-344 — Independently implemented compiled replay

Provisional alias: `IDEA?argmax-effective-native-checker`.

Aliases: C++/GMP checker; native certificate verifier; separate arithmetic replay.

- Question / scope: independently reconstruct PD-T210 certificates through a compiled arithmetic path so faster production does not rely solely on producer self-validation.
- Mechanism and hypotheses: a separate developer implements rational Machin/Taylor enclosures,192-bit outward integer construction, corrected cardinals, exact Bernstein transforms, subdivision and leaf predicates in C++/GMP. Python parses JSON/gzip, checks provenance/strict types and prefix covers, and records receipts. The checker does not import or link the native producer arithmetic kernel; it shares the mathematical formulas, schema and prescribed rounding sequence.
- Closest registry entries (read in full): IDEA-320 and its original formulation. This is verification machinery for its PD-T210 implementation, not a distinct extremal theorem or new mathematical certificate criterion.
- Separation criterion vs closest entry: independently written arithmetic reconstruction and strict envelope checks, rather than producer-generated bounds being trusted. This implementation independence is erased if producer arithmetic is called or copied as the checking path; the developer explicitly documents not doing so. Agreement can still share formula/specification mistakes and does not replace mathematical audit.
- Literature baseline and search limitations: no new external source or priority comparison. The reference checker and PD-T210 are the specification.
- Applicable obstructions and exact hypotheses broken: no analytic obstruction is escaped. Complete prefix coverage and strict corner/bound predicates remain mandatory. A producer's `accepted=false` cannot be upgraded merely because its metadata parses; partial covers must remain unaccepted.
- Novelty gate verdict: **variant with implementation difference / verification machinery**, no new mathematics.
- Cheapest decisive test: reconstruct historical n9–16 and producer overlap certificates exactly; run all historical corruption controls plus malformed-protocol/strict-type controls; verify valid partial positives remain unaccepted.
- Kill criterion recorded before testing: the checker developer's [attempt](../attempts/native-checker.md) states that any metadata or leaf-bound mismatch blocks finite extension claims until explained and fixed. Handoff02 additionally requires corruption-control cross-validation and a different subagent's replay.
- Test discriminability: checking every integer bound and complete frontier can detect arithmetic, rounding, subdivision and coverage errors. Negative controls exercise those predicates but cannot establish absence of every bug. Reproducing the reference rounding sequence creates shared specification dependence even with separately written code.
- Actual test results and evidence: the developer reports historical n9–16 acceptance and native overlap n9–24 acceptance, all14 historical corruptions plus22 added malformed cases rejected at n9 and17, the36 n9 controls repeated under optimized Python, and compiled arithmetic units passed. Larger replay updates belong to [the checker attempt](../attempts/native-checker.md); independent worker coverage belongs to [independent-checks-01](../independent-checks-01.md). These are attributed reports, not runs by this ledger's writer. [README](../code/native_checker/README.md) describes commands and the exact shared-machinery boundary.
- Disposition: **retained as independent implementation machinery within documented validation**, with completed replay and the accepted [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) tracked separately. No blanket acceptance of all n<=100 outputs.
- Disposition reason: separate arithmetic and explicit corruption controls improve the evidence path for finite certificates; scientific status depends on completed per-certificate checks and their theorem reduction.
- Canonical theory / negative-result ID: PD-T210 inherited; finite degree-range continuation is PD-T246. No negative-result ID is allocated for checker development.
- Topic / audit / history: developed independently of the native producer kernel, with shared formulas/schema/rounding convention disclosed. Root owns final frozen hashes, accepted range and durable evidence publication. A passing supplementary check does not replace Claude audit.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
