# cold-storage-20261102 — current results

Branch: `claude/cold-storage-20261102`. 2026-11-02. Claude, Opus 5.5 xhigh. A Codex protocol audit is **PENDING**.

- **What changed.** On AC's instruction, every large regenerable generated output (16 KiB or more) left the branch head: 163 files, 15.4 MB, from 9 topic and track directories. Generated data at the head falls from 19.15 MB to 3.60 MB.
- **How it is recorded.** Each moved file is pinned by SHA-256 and by its Git blob at main `2b52b43`. Its generating command and its short summary are given in the owning directory's `cold-storage.json` and `COLD_STORAGE.md`.
- **Tool.** `tools/cold_storage.py` verifies, restores, cleans and exports the moved files.
- **What did not change.** No theory record, status or ID changed. Code and small receipts stay. The 13 registry/source data files first kept were also moved on AC's approval (176 files, 15.8 MB in total); generated data at the head is 3.30 MB, including the new manifests.
- **Pending.**
  - Export to AC's Padua cold storage.
  - The rule paragraph in `agents/WORKFLOW.md` is approved by AC.
  - History purge with force-push is approved by AC but waits until AC's cold-storage export is verified (Git history is the only copy now).

Next: Codex protocol audit ([handoff 02](../topics/cold-storage-20261102/handoffs/02-audit.md)).
