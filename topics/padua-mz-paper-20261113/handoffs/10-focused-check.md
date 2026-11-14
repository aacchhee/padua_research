# Handoff 10 — focused check of the verifier fixes (P1, P2, R1) and the replacement packs

- Status: done in a087aadee3a28a7e2fff2fb513949a1c643aaa57
- Previous handoff: [09-verifier-response.md](09-verifier-response.md), done in `ccaf2cae3ac937a1f2b2a3dbd2c425059032e8cf`.
- Next agent / model / effort: **Codex, gpt-6-astra medium**: a protocol and technical check of shell entrypoints, records and archive differences. Raise the effort only if a finding touches a certificate.
- Branch: `claude/padua-mz-paper-20261113` · Draft PR #35.
- Input head: the commit that publishes this handoff. Development output: `ccaf2cae3ac937a1f2b2a3dbd2c425059032e8cf`. Pack source: `52030d1d22d6397a02c2831145a962e02105973b`.
- Main/base: `99a9b1d`, merged at `fa956de`.
- Stage: PR. This is a focused check of [readiness-01](../readiness-01.md)'s findings only.
- Written by/date: Claude, claude-opus-5-5 (configured xhigh) · 2026-11-14.

## Read first

- AGENTS.md, agents/WORKFLOW.md and the Codex role; the rules are unchanged since `c0e57a9`.
- [response-readiness-01.md](../response-readiness-01.md), the LOG entry for it, and [zenodo/README.md](../zenodo/README.md).

## Accepted, do not reopen

These stand as accepted in readiness-01:
- audit-01 F1–F5 resolved;
- PD-T684/685;
- the reservation PD-T684–689;
- the regenerated PD-T376 inputs and their independent replays;
- all default certificate and measurement replays;
- builds and frozen labels;
- the licence notices.

## Task

1. **P1.** Review `zenodo/verify-mz-sp.sh` and `verify-mz-cc.sh` (diff `9705c75..52030d1`). Check:
   - required checks alone decide `ALL REQUIRED CHECKS AGREE` / `REQUIRED CHECKS FAILED` (exit 0/1);
   - with `--regenerate`, source-vector differences are NOTEs and payload or norm differences are DIFFER with `OPTIONAL REGENERATION DID NOT REPRODUCE…` (exit 2 when the required checks agree);
   - a program that exits nonzero counts as a failure.

   Run `tools/verify_controls.py` on freshly staged packs, or your own controls, for both success and mismatch outcomes.
2. **P2.** Confirm that a path-like `PY` is resolved before `cd repository` and that a bare command still works. Run the README's documented commands from a fresh pack directory with a relative virtualenv:
   - the CC full run (about 1 minute);
   - at least the SP entrypoint, including the `--regenerate` form.

   The full SP run is optional, since its numerical programs are unchanged; the developer's full logs are in `evidence/verify-runs/`.
3. **R1.** Review this topic's sections in RESULTS.md, state/CURRENT.md and PAPER_MAP.md (diff `58697024..52030d1`). Process and AC-task text should be gone, and the scientific content, OPEN items, evidence facts and audit links kept.
4. **Packs.** The replacement zips are recorded in zenodo/README.md: CC `729fb953…`, SP `e8dfc5af…`.
   - Rebuild with `tools/zenodo_pack.py stage --rev 52030d1…` from exact inputs (yours from readiness-01, regenerated, or the data recipe in the LOG).
   - Compare with the committed manifests. Expected differences are the gzip containers, run-specific measurement JSON and the verification logs only.
   - If you can read the delivered CC zip, check it byte for byte.
5. **Reservation.** Refresh it only if main or another open PR's ledger changed since `9705c75`; otherwise record that nothing changed.
6. **Disposition.** Write `readiness-02.md`.
   - If clean, record readiness of the agent work and mark PR35 ready for review, if WORKFLOW allows; PR35 then waits only on AC: the deposit, the placeholders (report §5), confirming the frozen texts, the SIAM-file decision, the companions and the merge.
   - Otherwise return the findings to Claude.

## Scope limits

- Do not edit the manuscripts, theory records, the response, the audits or the receipts.
- Do not touch `.github/`, settings, `main`, other branches or tags.
- Agents create no deposit. Only AC merges.
- Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers.

## Outputs

- `readiness-02.md`.
- An updated PR body.
- Close this handoff with its output SHA in a following commit, then add the next numbered handoff if work remains.
