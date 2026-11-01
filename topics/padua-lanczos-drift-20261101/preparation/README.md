# PR-preparation record: padua-lanczos-drift-20261101 (PR #15)

- **Preparer.** Claude orchestrator, configured `claude-opus-5-5`, effort high; no subagents.
- **Handoff.** [11-pr-preparation](../handoffs/11-pr-preparation.md). Rules (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`) read at fetched head `918f41ce719e9fe8c5336a338692f1fac14a2018`.
- **Accepted source.** `02bd97b892ed409ec64e9b281130c71a85e914e9` (Codex [audit-04](../audit-04.md) ACCEPT, no findings).
- **Pre-preparation commit.** `918f41c`.
- **Base.** Main `28aaa20861d08074b77efc74eaef75cdcb36234d`, unchanged since the PR16 merge, so no new merge was needed.

## Union and allocation

The fresh scan is [union-scan.json](union-scan.json), result **PASS**. It covered main `28aaa20`, PR12 `f4c5c9e` (the only other open PR, a draft) and PR15 `918f41c`, reading the ledger, PROOF_STATUS, IDEAS, INDEX, CROSSWALK, CURRENT and PAPER_MAP at each head plus every record header under `tracks/`.
- No reserved ID has a final use anywhere.
- No PR is closed without merging; all closed PRs were merged.
- PR12's registry bytes equal main's.

The reservation, first published in `6920ba632843597c37e1493d077c1df2e89f54cb`, is unchanged:

| Namespace | Reserved | Assigned | Permanent gap |
|---|---|---|---|
| PD-T | PD-T136–155 | PD-T136–146 (11) | PD-T147–155 |
| PD-N | PD-N062–071 | PD-N062–063 (2) | PD-N064–071 |
| IDEA | IDEA-246–285 | IDEA-246–267 (22) | IDEA-268–285 |
| LIT | LIT-445–459 | none | LIT-445–459 |

The complete provisional-to-final map is [final-id-map.json](final-id-map.json). The withdrawn draft `PD-N?drift-codex-14` receives no PD-N; its content is IDEA-253.

## What was done

All of this was done by [prepare.py](prepare.py) (receipt: [prepare-receipt.json](prepare-receipt.json)), except the declared administrative edits listed in the last item.

1. **Literal approved proposals.** All 15 OLD/NEW blocks of `proposed-record-changes.md`, plus the Block-7 History anchor, were applied in file order, each OLD unique. The targets are:
   - PD-T055, PD-T054, PD-T056;
   - PD-T075 (three blocks, then Blocks 1–4);
   - PD-N013, PD-N015;
   - PD-T069 (Blocks 5–6);
   - PD-T061 (Block 7 and its History anchor).

   Placeholders are filled with "2026-11-01, Claude PR preparation (configured claude-opus-5-5, high)", and provisional IDs inside NEW text are replaced by final IDs. **PD-T075 is now PARTIAL**: (U1) PROVED in PD-T144, (U2) OPEN. All 69 other inherited theory files are byte-identical to main.
2. **Final IDs in current developer prose.** These files changed only by ID substitution:
   - the 13 drift records, with a `Provisional alias:` line inserted after each header;
   - the four IDEA files;
   - directions E1–E6;
   - independent-checks and external-code;
   - the code README.

   Quoted original wording («…») is never altered. The withdrawn ID `PD-N?drift-codex-14` is deliberately not substituted. Immutable files are not touched: audits, responses, developer and reviewer reports, evidence, code, handoff bodies and LOG history.
3. **Tombstone removed.** `drift-codex-e4-14-noiseless-quantifier-refutation.md` is deleted, with its full content retained in IDEA-253.
4. **Registries.**
   - **New sections:** a "PR15 final registration" section is appended to PROOF_STATUS (13 record rows plus a separate PARTIAL target row for PD-T140), state/IDEAS (22 rows), state/CURRENT, PAPER_MAP, topics/README, tracks/bivariate-lanczos/README and the batch ALLOCATIONS ledger.
   - **ID_CROSSWALK:** this topic's own reservation section is replaced by the reservation plus the final map, the withdrawn-ID row and the split relations.
   - **Named in-place updates:** the PD-T075 row in PROOF_STATUS (now PARTIAL) and the IDEA-151 row in IDEAS (the PD-T054 open-item note proposed in response-01 for audit-01 E34-F8).
5. **Root RESULTS.md.** Only this topic's section is appended; the other sections are byte-preserved.
6. **Declared administrative edits,** current-state synchronization only:
   - the report and plan stage headers;
   - the "Applied at PR preparation" note in proposed-record-changes;
   - E4.md's "file removed" wording;
   - the results file: final IDs, status and next step.

## Status integration

These are exactly the accepted classifications:
- **PD-T141** is PROVED (finite computer-assisted, formal scalar model).
- **PD-T140** is MEASURED (the experiment). Its both-grid sufficient test is INCONCLUSIVE, and its separately labelled factor-ten target is PARTIAL: the T24 conjunct is PROVED in PD-T141(c), and the rotQ24 conjunct is OPEN.
- **PD-T144** splits PD-T075(U1).
- **PD-N062 and PD-N063** are scoped negative mathematical statements.
- **IDEA-253** is the rejected quantifier reading, with no PD-N.
- **Still OPEN:** all-degree drift (E2), general staircase safety, PD-T055, PD-T075(U2) and PD-T056(G). No actual-IEEE claim is made.

## Checks

[validate.py](validate.py) works on committed objects (pre-preparation `918f41c` → prepared head), and its receipt is [validation.json](validation.json). It is a new preparation checker; the pre-preparation `integration_check.py` is not reused, because it requires unchanged registries. It checks:
- the map: unique IDs, within the own ranges, counts 11/2/22, record 14 unmapped;
- the record headers and alias lines, and the tombstone deletion;
- every literal target, recomputed independently from base, plus the other inherited theory identical to main;
- that each prose file equals ID substitution of its base, or is one of the declared administrative files (listed with changed-line counts);
- registry preservation: append-only, or the named in-place rows only;
- the RESULTS.md prefix;
- the registry row counts: PROOF_STATUS 14, IDEAS 22, CROSSWALK 36;
- that protected files are unchanged;
- that relative links resolve;
- a disposable squash rehearsal onto main (tree equals head);
- merge-tree against PR12.

No scientific claim, proof, code or evidence was changed, so the expensive campaign checks were not rerun. Accepted audit-04 regeneration and the earlier independent coverage remain the attributed evidence.

## Remaining limits

Codex's original development ZIP (`27476b62…`) and raw artifacts are verified in the Codex workspace (audit-02), but not yet delivered to AC's Windows cold storage. This is a separate archival item; the committed compact evidence plus regeneration needs no hidden input.
