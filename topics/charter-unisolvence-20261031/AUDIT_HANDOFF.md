# Claude audit handoff — historical input to completed audit-01

- Historical stage at handoff: **AUDIT**. Claude audit-01 subsequently accepted the mathematics at eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64. Current stage/readiness and finding dispositions are in response-01.md; the original handoff instructions below remain historical.
- Branch: `codex/charter-unisolvence-20261031`; base/rules `d36722823441dc40c6e19d69a174459348dd309c`.
- Audit exact canonical file identities in [audit-targets.json](audit-targets.json). Verify all SHA256 values before review; use the pushed branch head containing this dossier. Final PR head is recorded in Git/PR metadata, avoiding a self-referential hash in this file.
- Source checkpoints: U0 `4f3d247c64d8c74a923b50f5ff575f83b5401cb8`; U1 `d5a5efbc6228ea21ef38b438ef976260f90ea83e`; independent U1 receipts `e626f63ac2728a7d7112640282d2e49b316fe2fe`; input code `5123a32774110e9290c42bc1cf3c6838ee6c3d35`.

## Scope and claimed statuses

Read AGENTS.md, WORKFLOW and Claude role file at the audited head. Read complete state/IDEAS.md including contextual dispositions and obstruction tables, literature/INDEX.md, exact shortlisted source records and U1-COMPARISON.md. AC's explicit Step0 baseline override is preserved in LOG.md; no exhaustive novelty claim is made.

PD-T001/002: PROVED odd-characteristic iff and corrected every-field criterion, including exact determinant-square identities, both parities/m, small degrees and field specialization. PD-N001: PROVED failure of original arbitrary-field necessity, with original iff candidate REJECTED: refuted; global sufficiency survives, vacuously in characteristic2. PD-T003: PROVED classical monic-OP kernel and discrete-product cubature consequence, characteristic≠2.

PD-T004–008: PROVED canonical good-characteristic Padua Gram/unisolvence, rationality/sign types, Dickson discriminant (including scoped integral bad-prime reduction), quadratic-character formula, code structure/dual/lower bound. PD-T009/010: MEASURED finite observations/distances, no completed computer-proof claim. PD-T011: OPEN deferred source ideal/recurrence and unrestricted-length transform targets. PD-T012: PROVED elementary universal linear-code upper bounds; matching Padua attainments stay MEASURED.

Ten PROVED records (nine positive and one negative), two MEASURED, one OPEN. Final IDs are allocation identities, not acceptance. Mathematical dependencies are explicit in each file; no source claim, finite sample or unread fulltext is an inherited proof dependency.

## Independent work already performed

- [U0 Astra high report](independent/u0/audit.md): reconstruction before reading producer proof, separately written exact checker, actual source/producer reruns, frozen hashes, evidence check; five core proofs found sound. Its final producer evidence prose was outside the initial scientific review; review that prose now.
- [U1 Astra xhigh report](independent/u1/report.md): independent derivation, own9336pair/18672board exact checks, separately executed frozen producer finite/symbolic modes, compact factor/sign/multiplicity verification. Four proof files found sound.
- [U0 bound review](directions/U0/bound-review.md): separate Sol xhigh reconstruction of Astra's elementary code bounds.
- [Integration impact](integration-impact.md): source blobs verified; only exact ID substitutions and listed editorial references/audit metadata differ in canonical files. Historical independent reports retain original provisional IDs/staging paths; use crosswalk/source commit to recover exact reviewed bytes.
- [Protocol supplement](independent/protocol/report.md): provenance, statuses, IDs, links, evidence sizes and documented transforms. This is supplementary, not the required Claude acceptance report.

## Highest-value adversarial questions

1. Check the weighted parity Gram cancellation through degree2m, generic tensor-moment polynomial identity, complementary-minor signs, automatic central minors, exponent cancellation of exactly2^N and localized-Z specialization with only node-difference denominators. Check m0/1 and both m/e parities.
2. Compare exact Hankel factors with De Marchi–Usevich2014/Camargo2015; do not accept axis separation as a new mechanism. Check conservative attribution and the corrected solved status of HSConj3. Missing/paywalled Floater journal text is pending-reference, not a proof stop.
3. Check Padua root/rationality necessity via full projections, n1 sign collapse, Dickson normalization/boundary count/integral reduction, q3/q9 character endpoints, and code-bound scope restricted to linear codes.
4. Check that every source candidate, failed route and correction survives in the idea records, and that MEASURED/OPEN parts do not weaken separate proved statements or acquire proof status from execution.
5. Check frozen code/output identities, independently executed reruns, source runner failure-propagation caveat, symbolic scope (full direct m2; formula plus direct slices m3/4), and actual staged storage versus pending Windows receipt.

## Reproducible commands

Run from the repository root. These were executed during development/independent checking; auditor should choose reruns appropriate to risk and record new outputs separately. Python3.12.14, numpy2.3.5, sympy1.14.0; exact U1 fields implemented locally.

```sh
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --samples 20 --output /tmp/claude-u1-fields.json
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output /tmp/claude-u1-symbolic.json
python3 topics/charter-unisolvence-20261031/independent/u1/check_u1.py
python3 -I topics/charter-unisolvence-20261031/directions/U0/verify_exact.py
python3 topics/charter-unisolvence-20261031/independent/u0/exact_check.py
python3 topics/charter-unisolvence-20261031/verify_cold_storage.py /workspace/padua-cold/charter-unisolvence-20261031
```

For source-script reruns copy committed input-code/ff_padua/*.py to a new off-repository directory, then use directions/U0/replay_source.py with the copy and a fresh output directory; run_all alone hides child exits. Exact original commands/environments/seeds and helper hashes are in the individual evidence records. Do not overwrite existing cold evidence.

## Deliverable and decision

Write `audit-01.md` with actual model/effort, exact audited SHA/hashes, files/novelty scope read, independently executed commands, findings by severity and residual uncertainty. Findings return Stage WORK; developer replies in response-01.md without editing your report. Acceptance sets Stage PR under repository workflow. Only AC merges. No initialization/frontier task remains erroneously pending: charter/import/track preparation is complete; the scientific frontier lists only genuine unresolved questions.

Cold-storage handoff is [COLD_STORAGE.md](COLD_STORAGE.md); user ZIP and full outputs are outside Git. A portable handoff is staged for AC's Windows destination, with integrity-check receipt; actual Windows delivery is unconfirmed.

Next: `Claude (Opus 5.5 xhigh): Continue codex/charter-unisolvence-20261031.`
