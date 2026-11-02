# Repository cold-storage cleanup (AC instruction 2026-11-02)

- Branch: `claude/cold-storage-20261102` · Base: main `2b52b432fe59c9a50aef9deebe5152c5d6874465`
- Orchestrator/developer: Claude. Auditor: Codex (required protocol audit).
- Stage: AUDIT · [handoff 02](handoffs/02-audit.md) is open for the Codex protocol audit (01 superseded by AC's approvals).
- Claims: none. This topic changes no theory record, no status and no ID. Its only rule change is the evidence-size paragraph of `agents/WORKFLOW.md`, which AC approved on 2026-11-02 (audit still required).
- Final IDs and reservations: none needed ("no range").

## 2026-11-02 — Claude, claude-opus-5-5 xhigh (configured)

- **Trigger.** Two instructions from AC, given while the audit of PR #17 was running:
  - "I do not think that we have to store large outputs that can be regenerated. Make sure that all needed code is in the repo, some short summaries are stored and expunge the large data files (cold storage)."
  - "18 mb per repo is too much."
- **Rules.** Read at `9fcdc21` (unchanged at main `2b52b43` for `AGENTS.md`, `agents/` and `templates/`). Role: orchestrator and developer.
- **Inventory.** On main, generated-data files (anything other than md/py/sh/tex/bib/svg) total 19,154,906 bytes in 1,023 files.
- **Policy applied.** Every generated data file of 16 KiB or more leaves the branch head. Two kinds of file stay:
  - cold-storage manifests;
  - hand- or agent-authored registry and source data that committed code reads, or that registries link (13 files, 0.43 MB, listed per topic with reasons).
- **Moved.** 163 files, 15,419,537 bytes, from 9 directories:

  | Directory | Files | Bytes |
  |---|---:|---:|
  | bivariate-lanczos | 47 | 2,274,436 |
  | charter-unisolvence | 2 | 42,142 |
  | lattice-unisolvence | 25 | 2,917,679 |
  | mz-constants | 3 | 135,927 |
  | padua-lanczos-drift | 30 | 2,963,704 |
  | padua-mz-2d | 12 | 1,525,001 |
  | padua-proof-attempts-2 | 22 | 4,030,911 |
  | programme-ideas | 17 | 1,387,384 |
  | tracks/mz-constants | 5 | 141,753 |

- **Result.** Generated data at the head is now 3,603,026 bytes.
- **How each moved file is recorded.** Each directory has a `cold-storage.json` and a dated section in its `COLD_STORAGE.md` (appended to the file where one already existed). Every entry gives:
  - path, bytes and SHA-256;
  - its Git blob at pushed main `2b52b43`;
  - the frozen generating command as recorded in that topic's own records, or "none recorded" with the reason;
  - the location of its short committed summary;
  - notes, including which committed checkers must restore the file first.
- **Where the metadata came from.** Five read-only Sonnet 5.5 high workers gathered it, one or two directories each, with no Git authority. The orchestrator applied it with a scratch script.
- **Tool and links.**
  - New `tools/cold_storage.py` (plan, verify, restore, clean, export), standard library only.
  - 76 markdown links in 45 files were redirected from moved files to the owning `COLD_STORAGE.md`. Only the link target changed; no text changed. The files include audit reports and `ID_CROSSWALK.md`, `PROOF_STATUS.md` and `RESULTS.md` rows.
- **Checks executed.**
  - `tools/cold_storage.py verify` accepted all 163 entries in all 9 directories against their Git objects.
  - Relative-link scan: 629 unresolved targets before and after. That number is pre-existing on main; no new broken link was introduced.
- **Limits.**
  - Delivery to AC's `C:\Users\andreyac\Downloads\padua\cold_storage\<slug>\` is PENDING. AC runs `python tools/cold_storage.py export <slug> --dest ...` for each slug.
  - Git history is not rewritten, so clone size does not shrink. Purging history is AC's decision alone.
  - Committed checkers that read moved files now need `restore` first. This is listed per topic.
  - Several generating commands are inferred from file contents, or not recorded at all. Each such case is marked in its row.
- **This topic's own PR #17 work.** The same cleanup was applied to `padua-argmax-alln-20261101` on its own branch (36 files, 2.53 MB). It uses the identical `tools/cold_storage.py`.

## 2026-11-02 — Claude, claude-opus-5-5 xhigh (configured) — AC decisions

- **AC's message:** "yes, I approve workflow wording. remove 13 files, I approve force-push".
- **Workflow wording.** The `agents/WORKFLOW.md` evidence paragraph is approved by AC. The Codex protocol audit is still required for the change set.
- **The 13 retained files.** These were kept in the first pass as hand- or agent-authored registry and source data:
  - ID maps;
  - `registry-semantics.json`;
  - the literature dedupe maps;
  - the provenance and impact records;
  - charter's earlier `cold-storage-manifest.json` and the U0 evidence manifest.

  They are now moved too: 13 files, 377,215 bytes. Each is pinned in its directory's `cold-storage.json`, with a dated addendum in `COLD_STORAGE.md` naming the scripts that must restore it first.
- **Links.** 17 more markdown link targets are redirected, in RESULTS.md, PROOF_STATUS.md, ID_CROSSWALK.md, the batch ALLOCATIONS ledger and topic records. Only the targets changed.
- **Checks.** `verify` accepts all 176 entries. Generated data at the head is now 3,300,628 bytes, including 124,754 bytes of the new `cold-storage.json` manifests. No other generated file of 16 KiB or more remains.
- **Force-push.** Approved by AC, but not yet executed. The prerequisite is in the 2026-11-02 reply, and the [handoff 02](handoffs/02-audit.md) scope notes record it:
  - Today Git history is the only stored copy of the moved files. AC's Padua cold storage has not received them.
  - A history purge would destroy them and turn every manifest locator into a dead link.
  - It would also change every commit SHA cited in the repository's records.
  - So the purge waits for a hash-verified export to AC's cold storage.
