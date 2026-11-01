# Independent review of allocation bookkeeping repair

Rules: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`, read in `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. Date: 2026-11-01 UTC. Auditor: independent Codex subagent. Requested model/effort: `gpt-6-astra`, high; runtime-resolved model metadata is unavailable. This is a separate review of the root Codex agent's mechanical repair, authorized by AC's instruction to fix all bookkeeping without another Claude round. The original pinned allocation reports and receipts remain unchanged.

**Result: PASS, all 30 assertions.** No blocking issue found in the reviewed repair. The default dry run now validates the installed allocation successfully without changing files. Its output exactly matches the committed map's block boundaries and next IDs. The pre-allocation path still succeeds on pinned pre-allocation inputs. The seven negative cases below reject malformed state without writing files.

## Reviewed identity and scope

The source remains `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`; the repair was an uncommitted worktree diff when inspected. The evidence pins every consumed worktree input by SHA-256, including:

| File | SHA-256 |
|---|---|
| `topics/programme-ideas-20261031/pr-prep/allocate.py` | `aedf30e280390d4fa7cdafda718a6ea2d6902eabc3b1f1d4fd11e9865e7c6861` |
| `topics/programme-ideas-20261031/pr-prep/id-map.json` | `1b4b6145235ad1b2e1d8f08b7aee65ec52881711e0ca855186ba2afdab503b44` |
| `topics/padua-batch-20261031/ALLOCATIONS.md` | `a3d907e2481a888d54c6d653ef49314d843ed4b87a7f78ebf5b22d9fac3f10b6` |

The installed branch recomputes the allocation, requires equality with the complete persisted JSON, validates one primary row per new ID and one crosswalk mapping per provisional ID, and validates the merged literature mappings. The default exit remains before every write. The installed `--apply` rejection was inspected in code, not executed. Assertions are active in every executed command; optimized Python is outside this test scope.

This review adds no mathematics or novelty content, so a new full-IDEAS novelty audit is not applicable. It checks identifier integrity, preservation of scientific content and dispositions, and the default execution behavior. It does not exercise allocation mutation.

## Executed checks

From repository root:

```bash
python3 -I topics/programme-ideas-20261031/audit-04-support/allocation-repair-check.py > topics/programme-ideas-20261031/audit-04-support/allocation-repair-results.json
```

The independent harness snapshots the actual repaired inputs, modifies only isolated temporary fixtures for negative cases, and invokes the unmodified repaired script with the same command in every case:

```bash
python3 -I topics/programme-ideas-20261031/pr-prep/allocate.py
```

| Isolated fixture | Exit | Outcome |
|---|---|---|
| Valid installed allocation | 0 | Block boundaries and next IDs match committed map |
| Pre-allocation inputs from `6954664fc0906b7e5c8ff0f1804b077bd3b5861f^`, repaired script | 0 | Same correct block boundaries and next IDs |
| Installed map changes PD-T081 mapping to PD-T082 | 1 | Rejected |
| Duplicate PD-T081 primary row | 1 | Rejected |
| Wrong final target in PD-T081's crosswalk row | 1 | Rejected |
| Wrong merged target for provisional literature row 48 | 1 | Rejected |
| Missing PD-T081 primary row | 1 | Rejected |
| Wrong provisional alias on PD-T081 primary row | 1 | Rejected |
| Missing installed map with already-allocated registries | 1 | Rejected as collisions |

All nine snapshots have identical file paths and byte hashes before and after execution. The harness also confirms that the actual worktree inputs did not change during the review. Results retain complete stdout/stderr, command arguments, Python version, changed fixture hashes, all consumed input hashes, and the assertion results. No invocation used `--apply`; no Git mutation was performed.

## Preservation and reservation

The allocation JSON is byte-identical to source `37820a5`. All final-ID and provisional-alias primary cells in the three registries are unchanged; all 208 crosswalk provisional/final cells are unchanged. Every PROOF_STATUS row retains every cell except audit metadata, and all primary IDEA rows retain every cell. Thus this repair changes neither scientific statuses nor candidate dispositions.

Of the 36 canonical PD/IDEA files, 35 are byte-identical to `37820a5`. The remaining canonical home, `tracks/lattice-unisolvence/README.md`, changes exactly two administrative sentences: the statements that IDs await PR preparation or remain provisional now explain the final allocation and retained aliases. The checker explicitly permits only those two literal replacements; the README's scientific content, status statements, canonical inventory and Final-ID line are unchanged. Reporting all 36 files as byte-identical would be inaccurate.

PR #11 is pinned to `97968d2c2d039cb0910e0ea50747fb2d9e01a262`. Its ledger confirms the LIT-293–LIT-299 reservation; the repaired local ledger cites this exact head and retains the reservation. The unchanged allocation map remains disjoint from it. The earlier independent allocation audit already checked the seven corresponding primary rows at that exact head.

This report supersedes the original audit's one-shot/default-dry-run limitation **only for the repaired script hash above**. The original receipt remains a correct account of the earlier source. Broader bookkeeping and integration readiness remain with the root review.

Suggested next prompt for AC: "Codex (gpt-6-astra, high): incorporate the independent allocation-repair check and complete the bookkeeping integration report."
