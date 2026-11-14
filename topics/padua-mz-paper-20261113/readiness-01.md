# Readiness 01 — response, allocations and regenerated evidence

- Auditor/orchestrator: Codex, `gpt-6-astra` high, 2026-11-14 (configured assignment; serving metadata not separately exposed).
- Rules and scientific/readiness input: `9705c75876a74ac6bcce5625d20a45e3676c1992`; rules unchanged from audit-01. Handoff 08, including its two licence addenda, is the authority. Checkpoint `26f80457` publishes support records only.
- Pack source: `90860ecdc12d9887f7d31c3b0440d3b14e8d6169`; frozen witness code: `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`.
- Scope: the response/merge/ID/registry readiness diff and the focused changed-evidence/package check. This is not a repeated mathematical or full novelty audit. No theorem, manuscript, scientific record, developer receipt, shared registry, licence or pack verifier was edited by the auditor.

## Disposition

**Not ready: return to Claude for two MAJOR verifier fixes and one MINOR shared-record cleanup.** The original audit findings F1–F5 are resolved. The new witness regeneration independently passes, and no allocation collision or changed analytic claim was found. The new findings concern archive verification entrypoints and reporting, not a refutation of PD-T376 or the other accepted theorems.

All default certificate and measurement checks actually run for the packs finish successfully. The two new failures were reproduced separately on the advertised optional/relative-interpreter paths. Passing the default numerical replay does not clear those packaging defects.

## Findings

### P1 — MAJOR: optional regeneration can disagree and still claim all checks agree

`zenodo/verify-mz-sp.sh:44,46` prints `DIFFER` on source-vector/payload mismatch but neither branch changes `fail`, exits nonzero, nor qualifies the final `ALL CHECKS AGREE`. An executable isolated control replaces only the expensive computations/predicates and preserves the actual mismatch consequences and final disposition: all six comparisons fail, yet exit status is zero and the final line reports agreement. See [pack review](audit-support/readiness-pack-review.md) and [failure control](audit-support/pack_verifier_control.py).

Platform-dependent proposal vectors may deliberately be nonfatal, because exact replay of the archived witness is the certificate. That does not justify claiming successful regeneration of mismatching payloads. **Required response:** propagate failures into the advertised all-checks outcome, or explicitly separate required certificate replay from optional regeneration diagnostics and report their outcomes accurately. Preserve the distinction between portability of the exact archived certificate and reproducibility of the floating proposal. This is a material verifier-acceptance change; it belongs to development and a bounded follow-up check, not an auditor's wording fix.

### P2 — MAJOR: both documented virtualenv commands fail after the verifier changes directory

Both `README-mz-cc.md` and `README-mz-sp.md` instruct the user to set `PY=venv/bin/python`. Both verifiers retain that relative value and then `cd "$HERE/repository"` before invoking it. A valid interpreter under the pack-root virtualenv is consequently sought under `repository/venv/` and cannot be found.

The orchestrator reproduced exit 127 with the **actual uploaded CC archive**: a valid relative interpreter symlink exists at invocation, but `verify.sh:16` cannot find it after changing directory. A separate minimal control using both unchanged scripts reproduces CC exit 127 and SP exit 127 at line 32. See [relative-interpreter control](audit-support/pack_relative_python_control.py). No scientific code needs to run to demonstrate the entrypoint failure.

**Required response:** resolve the interpreter before changing directories, or document an absolute interpreter path in every affected example, including the optional regeneration command. Check the actual fresh-pack command with a valid interpreter. The current default-PATH/absolute-interpreter executions remain valid; this finding does not allege a failure of their certificate calculations.

### R1 — MINOR: process instructions remain in new shared registry entries

The topic's new `RESULTS.md:618,631,633` and `state/CURRENT.md:340–341` retain draft/pending readiness or operational instructions for AC. WORKFLOW sends pending process to the topic log, handoff and PR; shared records keep claim content/status, dependencies/dispositions, evidence facts and completed audit links. The new PAPER_MAP rows at lines 21–22 also need their pending-readiness clauses reconciled. Full locations and the rule distinction are in [registry review](audit-support/readiness-registry-review.md).

**Required response:** clean only this topic's new shared sections while preserving the scientific content, mathematical OPEN items, evidence facts and other topics. Do not move AC-reserved publication decisions into a theorem statement or silently treat them as completed. The auditor did not edit shared files under this handoff's write scope.

## Task A — readiness diff

**A1, response F1–F5: PASS.** The exact response diff `303a564..a1a2949` fixes the archive wording, measured/trial distinction, negative raw coefficient, notation and stale check metadata. The subsequent prepared-archive wording is covered by task B. The substantive Statement/Definitions/Depends-on/Proof/Scope sections of both consequence records remain byte-identical. Bib files and ordered source label/theorem-environment sequences are unchanged. The licence additions change no mathematics.

Fresh builds give **32 CC / 50 SP pages**, no final LaTeX/BibTeX warnings or box issues, and no Type 3 fonts. All compiled label values match the prior audit builds (212 CC, 116 SP including equation/cref records). The actual frozen **non-cref** correspondence tables match 52/52 and 56/56 entries. Existing helper metadata in the frozen CC table sometimes names a cref type differently from actual compilation; the actual old/new compiled label values are identical, and every frozen ordinary number matches. No renumbering is inferred from source-count versus auxiliary-count differences.

**A2, main merge: PASS.** `fa956de` has the response and main `99a9b1d` as its two parents. A blob/set comparison confirms all 89 incoming main paths are precisely incorporated with no extra path or changed incoming blob. Published history was preserved.

**A3, reservation refresh: PASS.** The fresh all-state GitHub collection contained 34 PRs: open #27/#35 and 32 closed merged; none closed unmerged. Checked fetched heads:

| Scope | Head |
|---|---|
| main | `99a9b1d161e41a80c4fd425b63022c681fbe8779` |
| PR27 | `9d3f5e0f8b270d039d78d4ebc0df53269a7892ab` |
| PR35 input | `9705c75876a74ac6bcce5625d20a45e3676c1992` |

All **19 unique complete ledgers** were read; the full bytes of all four registries were scanned at each head. Coverage: 65 copies, including 53 ledger and 12 registry copies, 26 distinct blobs. Foreign maxima are T683/N250/IDEA765/LIT720; with this topic, T689/N250/IDEA765/LIT720. No foreign PD-T684–689 overlap or unknown retired range is found. Fixture/foreign aliases were excluded only after their actual context was checked. Reservation commit `88824fb` precedes assignments `06e544d`; Git verifies the ancestry and original range, while the historical push/PR-link timing remains the developer's recorded provenance, consistent with the current PR link. The auditor cannot reconstruct an independent timestamp for the earlier PR-body edit. See [full reservation record](audit-support/readiness-reservations.md), [checker](audit-support/readiness_reservations.py) and [receipt](audit-support/readiness-reservations.json).

**A4, scientific registry/ID application: PASS, with R1 hygiene.** PD-T684/685 map one-to-one to the audited consequence records; unused PD-T686–689 remain permanent gaps. The PD-T684 numerical interval's PD-T547 computer-assisted dependency is explicit. The PAPER_MAP scopes, source results and omitted PD-T531 agree with the READMEs; no source negative or measured result is promoted. Other-topic main content survives. LIT-045 records the developer's documented published (7)/(8) reading; LIT-056 changes DOI metadata only. No external PDF reread is claimed. The new evidence availability facts are accepted only within task B's actual checks below.

## Task B — focused evidence check

**B1, original witness regeneration: PASS.** [Independent witness replay](audit-support/readiness-witness-replay.md) actually runs the seeded eigensolves and both sign-check paths, rather than reading the developer's receipts as a rerun. All five relevant code files equal the frozen `39479ff` blobs. All three original source-vector SHA256, decompressed witness JSON SHA256 and exact-norm SHA256 match exactly. In this runtime the original historical gzip-container hashes also match; the later delivered package uses different containers, which is why decompressed identities are decisive. Both producers prove positive continuous norm and negative signed energy; all three separate checkers accept negative energy under the recorded IEEE/BLAS error model. Exact/proof-bearing receipt fields agree with the original committed receipts, not merely the later reconstruction receipts. Compact actual argv/code/input/runtime evidence is in [readiness-witness-replay.json](audit-support/readiness-witness-replay.json).

This resolves the prior absent-input replay limitation **for the independently regenerated pinned inputs**. It does not prove a deposit exists or establish the unread original SP ZIP's compressed bytes.

**B2, comparator/historical pins: PASS apart from P1/P2 entrypoint semantics.** Every actual `--ignore` is inspected: proposal source vector on archived replay, and the specific later-extended P4/P1 protocol/reduction hashes. Relevant acceptance booleans, signs, exact endpoints, code hashes and other nonignored fields remain compared. The archived original P4 protocol at `d03e74dc` and P1 protocol/reduction at `c1e6e59d` hash exactly to the committed receipts (both P1 instances). Runtime/status prose, intermediate bulk, receipt/container identity and paths are explicitly distinguished from mathematical predicates. See the pack review for hashes and coverage; no new prose-pinning policy is introduced.

**B3, package source/content: inspected PASS; runtime disposition below.** The complete committed manifests have exactly the declared source/data/template sets: 377 CC rows / 706 SP rows (plus manifest itself). All **368 CC + 678 SP repository-member hashes** match `90860ec`. Every manuscript-named checker, its dependencies, trial/receipts and the exact large witnesses/norms are represented; longer P2 measurements are expressly out of the verifier's scope.

The user supplied both delivered ZIPs during this check. The CC ZIP is downloaded, hash-checked against `6aa35fc7…2a48`, CRC-tested, freshly extracted, and **all 377 manifest members pass**. Its full default verifier finishes `ALL CHECKS AGREE`.

The supplied SP ZIP exceeds the download tool's **32 MiB executor transfer limit**; its recorded 40,708,593 bytes / `f04f65b5…6b2b` were **not independently read**. Under handoff 08's explicit fallback, the SP tree is rebuilt with `zenodo_pack.py` at the pinned `90860ec` source and independently regenerated data. Every repository/source member and all exact norm/vector/payload identities can be checked. Initial comparison to the committed delivered manifest matches 700/706 rows exactly; differences are the three gzip containers and two measurement JSONs with runtime metadata, plus the original delivered verification log, whose bytes are unavailable. Fresh runtime evidence is kept distinct from that historical log. No claim of matching the unread original SP ZIP or original measurement/log bytes is made.

**B4, wording/licensing: PASS within the stated source scope.** Both manuscripts say the archive is *prepared for deposit* with a DOI placeholder. No existing Zenodo deposit is asserted. Root and pack notices implement AC's AGPL-3.0-or-later instruction, and root/template LICENSE texts are identical. The SIAM macros and source quotations retain their exceptions. The packed code/evidence is unchanged from `ed385e9`; differences are the documented README/LICENSE and manuscript licence sentences, plus omitted SIAM files. All 1,046 packed repository hashes verify that content boundary. The existing two-of-eight SIAM repository distribution question remains expressly reserved to AC by handoff 08; it is not silently resolved here. Physical device delivery remains Claude's documented observation, not independently witnessed by this auditor.

### Completed package executions

| Actual run | Result |
|---|---|
| Uploaded CC ZIP, fresh extraction | Exact delivered ZIP SHA256, CRC and 377/377 manifest members pass; all four verifier comparisons agree, exit 0. |
| Independently staged CC pack | All four verifier comparisons agree, exit 0. |
| Independently rebuilt SP pack | All **25** default comparisons agree, exit 0: payload identities; three exact producer replays and three independent sign checks; all six bracket producers **and all six independent Fraction-pencil checks**, including m=80; both rectangle instances and historical pin checks; both measured suites. |
| Rebuilt SP ZIP integrity | Finalized locally with a new actual verification log, then checked as an archive: CRC and all **706/706** manifest members pass; the 707 total files match the verified staging contents. Its own identity is in the receipt, and is never presented as the unread uploaded SP ZIP identity. |

Only two generated Python bytecode caches were removed from the verified staging before finalizing the fallback ZIP; no source, data or numerical output changed. The two regenerated measurement **result** dictionaries also agree with the corresponding historical `2b52b432` output under the inspected runtime-field exclusions, not merely with another run generated during this review. Original delivered measurement JSON metadata and the delivered console log remain unread.

[readiness-reruns.json](audit-support/readiness-reruns.json) records actual build/package outcomes, source/checker identities, frozen-label counts, the uploaded CC ZIP identity and the fallback SP ZIP's separate identity. [summarize_readiness.py](audit-support/summarize_readiness.py) checks the actual receipts, logs and archive members before producing that compact record. It is a summary checker, not a replacement for the actual producer/checker executions. Trusted arithmetic and numerical model are unchanged from audit-01 and the focused witness-replay report: exact Python/FLINT/GMP and outward dyadic/Arb arithmetic, plus the independently documented IEEE/BLAS error model for the forward-error witness checker. Numerical proposal accuracy is not assumed as a certificate premise.

## Execution and next step

Commands actually used include the witness-replay report's full commands, fresh builds with `tools/build.sh`, `zenodo_pack.py stage --rev 90860ec...`, `bash verify.sh` on the uploaded CC fresh extraction and rebuilt SP staging, the reservation checker, and both isolated verifier controls. Python/flint/BLAS and source/runtime identities are recorded in the supporting receipts. No bulk outputs or ZIPs are added to Git; local regenerable output is not claimed as a new cold-storage delivery.

The full default SP execution was:

```sh
python topics/padua-mz-paper-20261113/tools/zenodo_pack.py stage --pack mz-sp --rev 90860ecdc12d9887f7d31c3b0440d3b14e8d6169 --data /tmp/mz-readiness-data --out /tmp/mz-readiness-packs
PYTHONPATH=/tmp/mz-python bash /tmp/mz-readiness-packs/padua-mz-sp-evidence/verify.sh /tmp/mz-readiness-verify-sp
```

The same invocation form ran the uploaded CC verifier at `/tmp/mz-readiness-upload-cc/padua-mz-cc-evidence/verify.sh`, output `/tmp/mz-readiness-upload-cc-rerun`. After SP verification, the SP run's log was copied to the fallback staging's `VERIFICATION-2026-11-14.log`, runtime bytecode caches were removed, and `zenodo_pack.py finalize --dir /tmp/mz-readiness-packs/padua-mz-sp-evidence` generated the separately identified fallback ZIP. ZIP member/manifest equality and a fresh extraction were checked; no second execution of unchanged numerical programs is claimed merely for extracting those identical bytes.

Claude should address P1/P2/R1 in a new response, rebuild the affected archive tooling/manifests and record replacement pack identities/delivery accurately. The follow-up is **bounded to the changed verifier/entrypoint/metadata and relevant package differences**; the accepted mathematics and unchanged sign/pencil/interval producers do not need a repeated full audit. Exercise success and mismatch outcomes, including the documented virtualenv invocation. Retain all valid evidence and exact payload pins. Draft PR #35 remains unready until that response/check is complete; AC's deposit, publication metadata, frozen-text confirmation, companions and merge decisions remain reserved as before.
