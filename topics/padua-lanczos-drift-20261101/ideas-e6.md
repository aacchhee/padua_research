# E6 retained comparisons

This direction implements the requested independent implementation benchmark. It introduces no new mathematical mechanism or priority claim; the novelty gate for generating new mechanisms is therefore inapplicable. Literature/INDEX, the Hokanson/ZN/BNT records, L2-prior-art review, and PD-N013, PD-N015, PD-T051 were read. Source-verification upgrades here concern code selection/order and actual execution only.

Response-01 (2026-11-01, Claude response to audit-01 E6-F5 and P-F7): the five entries were reformatted to `templates/IDEA.md`, relabelled with provisional IDs `IDEA?drift-codex-55` to `-59` (the old `E6-5x` labels are kept as aliases; numbers 55-59 were chosen so the idea labels cannot be confused with the record `PD-T?drift-codex-50`), and given disposition words. The old labels are mapped as follows. A grep of the repository found no use of the old labels outside this file, `directions/E6.md` line 3 (the record's own alias `E6-50`) and the record alias line.

| Old label | New provisional ID | Title |
|---|---|---|
| E6-50 | IDEA?drift-codex-55 | Upstream Hokanson benchmark (actual polyrat V+A) |
| E6-51 | IDEA?drift-codex-56 | Default coordinate orientation of upstream polyrat |
| E6-52 | IDEA?drift-codex-57 | Observed drift implies all fit problems fail |
| E6-53 | IDEA?drift-codex-58 | BNT as a multivariate upstream comparator |
| E6-54 | IDEA?drift-codex-59 | ZN actual implementation |

Registry note: the closest-entry lists name IDEA-086 and IDEA-116 (`state/IDEAS.md` rows 646 and 676; their linked rows in `topics/bivariate-lanczos-20261031/baseline-candidates.md`, candidates 010 and 040, were read) in addition to the original PD-N013/PD-T051 context (P-F7). I read the registry rows and those two baseline rows, not the full literature records behind them. The "read in full" marks for PD-N013, PD-T051, PD-N015 and the L2-prior-art review are inherited from the original Codex wording ("were read"); the Claude response-01 developer did not reread those records.

## IDEA?drift-codex-55 — Upstream Hokanson benchmark (actual polyrat V+A)

Aliases: E6-50 (old label); public V+A drift benchmark; actual `vandermonde_arnoldi_CGS`; upstream `[y,x]` as campaign dev.

- Question / scope: is the retrieved, unmodified polyrat 0.2.2 (commit `6903d7af9995c9d88e661fb229626696e00fdfba`) `vandermonde_arnoldi_CGS` with input `[y,x]` the campaign's dev selection with full CGS2, in selection, order and executed columns, and does it show the measured span drift on the frozen benchmark sets?
- Mechanism and hypotheses: inspect upstream `_update_rule` and the within-degree order; check every parent through n47; call the upstream function directly and compare columns entrywise with the own L2 dev run on the same weighted nodes. Requires NumPy below 2.5 (upstream `_update_rule`).
- Closest registry entries (read in full): PD-N013 and PD-T051 (with PD-N015) for the measured drift and selection comparison; IDEA-086 (the original truncated multivariate Vandermonde-with-Lanczos "new method", settled as the established multivariate window recurrence, priority background); IDEA-116 (Zaccaron/Meurant-Sommariva measured baselines for the HL recurrence; see candidate 040). Literature records LIT-281 and LIT-360 as cited in audit-01 (not re-read by this developer).
- Separation criterion vs closest entry (and observation that falsifies it): no new mechanism is claimed; the entry is an independently sourced implementation of an already-recorded rule. If the upstream `[y,x]` construction had a different parent, order or materially different span, the identification with the campaign dev fails. The observation is a nonzero entry difference or a different parent in the exhaustive check.
- Literature baseline and search limitations: statements about Hokanson's code come from reading the pinned source; paper statements stay at their recorded WebFetch-digest, UNVERIFIED level. No priority claim.
- Applicable obstructions and exact hypotheses broken: PD-N013 and PD-N015 (reorthogonalization does not restore the measured graded spans on the tested sets); none is broken, the entry only re-measures them with different code.
- Novelty gate verdict: duplicate (equivalent implementation of the PD-N013/PD-T051 dev+CGS2 benchmark); retained only as independent implementation confirmation.
- Cheapest decisive test: inspect the source and call it directly (done).
- Kill criterion written before testing: as recorded in the original table, a different upstream parent/order or materially different span would end the identification. The chronology of that wording relative to the measurement is not documented in LOG or provenance.
- Test discriminability: the exhaustive parent check through n47 decides selection and order exactly; the entrywise comparison decides column equality only in the executed environment. A different parent rule would give different columns or spans and so would be visible as a nonzero difference. Observed `upstream_yx_vs_dev_entry_max=0` on all sixteen case instances. Bitwise equality is platform dependent and is not a cross-library claim.
- Actual test results and committed evidence: `topics/padua-lanczos-drift-20261101/evidence/e6-benchmarks.json`, `e6-frozen-grids12.json`, `e6-frozen-grids.json`, `e6-provenance.json`; audit-01 reruns were case-identical and an independent long-double reference reproduced the rotpi4 n24 and triangle n20 gaps (n16 grids not independently rerun). Response-01 off-sample evidence: `evidence/response-01-e6-offsample.json`.
- Disposition and precise rejected scope, if any: equivalent algorithm, retained as independently sourced implementation confirmation (MEASURED bitwise equality in the executed environment). Nothing is rejected.
- Disposition reason: equivalent. Upstream `[y,x]` is the campaign dev rule with the same within-degree order and two classical Gram-Schmidt passes; scope is the pinned source and the executed environment (MEASURED, finite).
- Canonical theory / negative-result ID: PD-T?drift-codex-50 (MEASURED). No PD-N: equivalence is an IDEA disposition.
- Topic / audit / history: audit-01 E6-F5, P-F7 (IDEA-086, IDEA-116 added); see History below.

## IDEA?drift-codex-56 — Default coordinate orientation of upstream polyrat

Aliases: E6-51 (old label); upstream `[x,y]`; reversed within-degree order mirror.

- Question / scope: is upstream default input `[x,y]` numerically the same as the campaign's forward-order mirror selection, or does the reversed within-degree order matter?
- Mechanism and hypotheses: `[x,y]` gives the mirror parent rule with the within-degree order reversed relative to the campaign; the span of a full-CGS2 recurrence depends on the order of the orthogonalization sweeps.
- Closest registry entries (read in full): PD-T051 (mirror selection); PD-N015.
- Separation criterion vs closest entry (and observation that falsifies it): the same mirror parent rule under reversed within-degree order. If actual upstream `[x,y]` equals forward-order campaign mirror numerically (same gap on the same sets), the distinction disappears.
- Literature baseline and search limitations: none beyond the source reading; no claim that renaming coordinates is a new mechanism.
- Applicable obstructions and exact hypotheses broken: none; PD-N015 warns against universal ordering claims and remains in force.
- Novelty gate verdict: variant with difference (ordering only); no novelty claim.
- Cheapest decisive test: compare actual upstream `[x,y]` with campaign forward-order mirror on the same weighted nodes (done).
- Kill criterion written before testing: as in the original table, equality of the two gaps. Chronology relative to the measurement is not documented.
- Test discriminability: on rotpi4 n24 the upstream default gap is `0.0136183` and the own forward-order mirror gap is `0.937968`, a factor of about 70, so the comparison separates the two cases decisively there; it says nothing about a universal ordering or about other sets.
- Actual test results and committed evidence: `evidence/e6-benchmarks.json`; the auditor's independent run reproduced the upstream `[x,y]` gaps `0.0136183` and `0.0028935` (rotpi4, triangle).
- Disposition and precise rejected scope, if any: retained distinct ordering variant, MEASURED on the tested sets. Nothing is rejected.
- Disposition reason: retained (not one of refuted, failed, equivalent, abandoned or deferred); a measured ordering variant of PD-T051, scope the sets in `e6-benchmarks.json`.
- Canonical theory / negative-result ID: PD-T?drift-codex-50 (MEASURED); no PD-N.
- Topic / audit / history: audit-01 E6-F5.

## IDEA?drift-codex-57 — Observed drift implies all fit problems fail

Aliases: E6-52 (old label); drift implies inaccurate least-squares fits; worst-polynomial versus smooth-target contrast.

- Question / scope: does the measured span drift imply that fits of every target on the same nodes with the same code are inaccurate?
- Mechanism and hypotheses: compare the post-hoc worst polynomial (training residual equal to the gap by construction) with fixed smooth targets on the same nodes and code.
- Closest registry entries (read in full): PD-N013 (which explicitly excludes that inference).
- Separation criterion vs closest entry (and observation that falsifies it): the inference would survive if a fixed smooth target on the same nodes and code lost accuracy comparable to the gap. Observation that erases it: a fixed smooth target with error far below the gap, on the same sets.
- Literature baseline and search limitations: none; this is a scoped counter-test.
- Applicable obstructions and exact hypotheses broken: none.
- Novelty gate verdict: not applicable (a measured counterexample to an inference, not a mechanism).
- Cheapest decisive test: fit `exp(x+y)` with the same upstream functions on the same sets (done); response-01 adds a generic non-ridge target and non-midpoint test samples.
- Kill criterion written before testing: as in the original table, a smooth target losing accuracy comparable to the worst-polynomial loss. Chronology of the choice of `exp(x+y)` is not documented in LOG or provenance.
- Test discriminability: `exp(x+y)` is a ridge function aligned with the rotpi4 frame (univariate in the reference frame), so it is a weak probe there. The generic target `exp(x)cos(2y)+sin(3xy)` (fixed in `e6_offsample.py` before results) is approximation-limited at these degrees, so its error is equal to the reference-span error and does not by itself resolve algorithmic loss; it does show that its prediction differs from the reference-span prediction by at most `3.7e-13`. The test therefore decides the broad inference (counterexample exists), and nothing finer.
- Actual test results and committed evidence: `evidence/e6-smooth.json` (midpoint errors at most `2.2e-15`); `evidence/response-01-e6-offsample.json` (uniform interior at most `2.6e-14`, boundary-inclusive at most `1.3e-13` for `exp(x+y)`, against worst-polynomial errors `1.5e-2` and `2.5e-2` on the uniform sample).
- Disposition and precise rejected scope, if any: **REJECTED: refuted**, within the scope of the counterexample: the inference "observed drift in the tested rule makes every fit problem on these node sets inaccurate" is refuted by `exp(x+y)` (and the generic target) on rotpi4 and triangle (and rot0.3 for `exp(x+y)`). Scoped adversarial fit failures are retained as MEASURED in the record. No claim about all smooth functions or other node sets.
- Disposition reason: refuted (finite counterexample; MEASURED).
- Canonical theory / negative-result ID: PD-T?drift-codex-50 (MEASURED) holds the numbers; PD-N013 already excludes the inference. No new PD-N.
- Topic / audit / history: audit-01 E6-F1, E6-F4, E6-F5.

## IDEA?drift-codex-58 — BNT as a multivariate upstream comparator

Aliases: E6-53 (old label); Brubeck-Nakatsukasa-Trefethen Vandermonde-with-Arnoldi example.

- Question / scope: does the public BNT example supply a multivariate order/selection rule that can be benchmarked against polyrat and the campaign rules?
- Mechanism and hypotheses: inspect the actual public source for two-variable order and selection.
- Closest registry entries (read in full): L2-prior-art review (identifies BNT as univariate); LIT-285 as cited in audit-01.
- Separation criterion vs closest entry (and observation that falsifies it): a two-variable selection rule in the source would make it a comparator; the observation that erases the distinction is such a rule appearing in the file.
- Literature baseline and search limitations: source inspection of `chebfun/examples` commit `f4b9ea46cfc2f52f20a844627f4a74d0bb10098c`, file sha256 `625f29c9f58c26699b664e9f88b7734d4ba74d29cfe9f7faefb314e5bc49d003` (URL, commit and sha are the provenance; the local checkout path in `external-code.md` is not present in the audit workspace). Paper fulltext not reread.
- Applicable obstructions and exact hypotheses broken: none.
- Novelty gate verdict: not applicable (comparator classification, not a mechanism).
- Cheapest decisive test: read `polyfitA`/`polyvalA` (done); execution needs MATLAB/Octave plus Chebfun, which are unavailable here.
- Kill criterion written before testing: absence of a two-variable order or selection in the file ends the multivariate-comparator question. Chronology is not documented.
- Test discriminability: reading the whole file decides whether a two-variable rule exists in it; it does not test the numerical behaviour of the univariate example, which is unperformed.
- Actual test results and committed evidence: `external-code.md` (inspection only); not executed.
- Disposition and precise rejected scope, if any: inapplicable: univariate. The example multiplies by one scalar coordinate with one modified Gram-Schmidt pass, so it has no multivariate selection to classify; it is background only. Execution of the univariate example is deferred (no runtime).
- Disposition reason: inapplicable: univariate for the multivariate question (a scope statement, not an equivalence with any campaign rule); execution deferred, to resume when a supported MATLAB/Chebfun environment exists.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: audit-01 E6-F5 (the original wording "Equivalent univariate background only" was replaced).

## IDEA?drift-codex-59 — ZN actual implementation

Aliases: E6-54 (old label); Zhu-Nakatsukasa code; arXiv:2301.12241 implementation.

- Question / scope: does an identifiable author implementation of the Zhu-Nakatsukasa multivariate Vandermonde-with-Arnoldi method exist, and what order/selection does it use?
- Mechanism and hypotheses: retrieve identifiable author source, pin it, inspect order and selection, run it.
- Closest registry entries (read in full): the record's unverified code mapping (L2-prior-art); IDEA-116 (measured V+A/HL baselines) and IDEA-086 (the established window-recurrence priority chain); LIT-283, LIT-284 and LIT-361 as cited in audit-01.
- Separation criterion vs closest entry (and observation that falsifies it): the observation that decides is the order and parent rule found in the actual ZN source; polyrat results are not a substitute for it.
- Literature baseline and search limitations: bounded public GitHub searches and guessed profile/pages (some blocked by proxy 403) found no author repository; this does not show that no code exists.
- Applicable obstructions and exact hypotheses broken: none.
- Novelty gate verdict: not applicable.
- Cheapest decisive test: obtain an identifiable author code URL, pin and inspect it, then execute.
- Kill criterion written before testing: finding an authors' implementation with a different rule or order would end the use of polyrat as a stand-in; it cannot be killed by polyrat measurements.
- Test discriminability: only the actual source decides; absence from a bounded search decides nothing.
- Actual test results and committed evidence: access attempts in `external-code.md`; nothing executed.
- Disposition and precise rejected scope, if any: deferred. Nothing is rejected.
- Disposition reason: deferred. Author code was not located within the documented bounded search; resume when an identifiable ZN author-code URL (or an accessible paper/supplement containing it) is available, then pin, inspect and run it.
- Canonical theory / negative-result ID: none.
- Topic / audit / history: audit-01 E6-F5, P-F7 (IDEA-116, IDEA-086 added).

The finite benchmarks do not reject every one-relation method, every orthogonalization method, or polynomial fitting in general. Ill-conditioned/numerically rank-deficient reference outputs are explicitly noncertifying.

## History

- 2026-11-01 (Claude response-01, Claude Sonnet 5.5): reformatted all five entries to the IDEA template with provisional IDs `IDEA?drift-codex-55` to `-59` (E6-F5) and added IDEA-086 and IDEA-116 as closest entries (P-F7); original wording of the table rows (dispositions): E6-50 «Equivalent algorithm, retained as independently sourced implementation confirmation; MEASURED bitwise equality in current environment. No novelty.»; E6-51 «Retained distinct ordering variant; substantial measured difference on rotated square. No claim that renaming the coordinates is a new mechanism.»; E6-52 «REJECTED broad inference: exp(x+y) stays near machine precision on rotated square/triangle despite the worst-polynomial loss. Scoped adversarial fit failures retained MEASURED.»; E6-53 «Equivalent univariate background only; no multivariate classification. Runtime unavailable, run pending.»; E6-54 «DEFERRED: author code not located/accessed in documented bounded search. Runs needed retained.»
- 2026-11-01 (Claude response-01, Claude Sonnet 5.5): original table columns «Provisional candidate | Closest predecessor | Separation / cheapest test | Disposition» preserved in the entries above as Closest registry entries, Separation criterion, Cheapest decisive test and Disposition; original separation wording, E6-50: «If actual upstream `[y,x]` construction has a different parent/order or materially different span, campaign identification fails. Inspect source and call it directly.»; E6-52: «Compare a post-hoc worst polynomial with an independently fixed smooth target on the same nodes and code.»
