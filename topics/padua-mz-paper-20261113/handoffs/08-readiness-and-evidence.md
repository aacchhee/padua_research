# Handoff 08 — readiness check of PR35 plus a focused check of the regenerated PD-T376 evidence and Zenodo packs

- Status: open
- Previous handoff: [07-readiness.md](07-readiness.md). It was superseded before it started; its tasks 1–4 are carried over unchanged as task A below.
- Next agent / model / effort: **Codex, gpt-6-astra high**. Task B is a focused evidence audit of computer-assisted certificate inputs, which is above a plain protocol check. Task A alone would be medium.
- Branch: `claude/padua-mz-paper-20261113` · Draft PR #35.
- Input head: the commit that publishes this handoff. Development outputs end at the commit before it.
- Main/base: `99a9b1d`, merged at `fa956de`.
- Stage: PR (readiness), with one focused re-audit item (WORKFLOW: a material evidence change).
- Written by/date: Claude, claude-opus-5-5 (configured xhigh) · 2026-11-14.

## AC's decision behind the change

AC, 2026-11-14 08:32: "there are no mz cleanup files. Regenerate the witness commit, and pack all needed evidence for zenodo, one pack per paper. If something is easier to regenerate, no worries, just regenerate".

## Task A — readiness check (as in handoff 07, tasks 1–5)

1. Review the response-01 diff (`303a564..a1a2949`).
2. Check the main merge (`fa956de`).
3. Refresh the full-union reservation for PD-T684–689. Reservation commit `88824fb` came before the assignments in `06e544d`.
4. Review the registry application (`fa956de..06e544d`, plus the later evidence-status edits to state/CURRENT, PAPER_MAP and RESULTS).
5. Write the disposition in `readiness-01.md`.

## Task B — focused check of the evidence change

Scope: [LOG entry "AC: there are no mz cleanup files…"](../LOG.md), [evidence/pd-t376-regeneration/](../evidence/pd-t376-regeneration/), [zenodo/README.md](../zenodo/README.md), [tools/zenodo_pack.py](../tools/zenodo_pack.py), the zenodo templates, verify scripts and comparator, and the two availability-statement edits (`ed385e9`).

1. **Regeneration.** Confirm the claim: at `39479ff` with the pinned stack, `g1_minimum.py` reproduces the three source-vector SHA-256 recorded in the original producer receipts. `rigorous_witness.py --vector` then reproduces the decompressed payload and exact-norm SHA-256 pinned in `topics/padua-mz-cleanup-20261105/evidence/witness-payload-identities.json` and the producer receipts. An independent rerun is proportionate: the eigensolves take about 3 minutes in total and the producers about 2 minutes.
2. **Comparator.** Check that `compare_receipts.py`'s ignore list skips only run-specific fields. Check each `--ignore` in the verify scripts:
   - source vector on witness replay;
   - P4 `protocol_sha256`;
   - P1 `protocol_sha256` and `reduction_sha256`.

   For the last two, confirm that the archived protocol versions (`d03e74dc`, `c1e6e59d`, from `refs/pull/31/head`) hash to the values in the committed receipts.
3. **Packs.** If the zips are available to you, check `MANIFEST-SHA256.txt` and run `verify.sh` from a fresh extraction; if not, rebuild them with `zenodo_pack.py` (the data recipe is in the LOG). Confirm that every file named in either availability statement is in its pack. The SHA-256 of both zips is in zenodo/README.md; the data recipe is deterministic, but a rebuilt witness gzip may differ (zlib), so compare manifests up to the documented container fields.
4. **Wording.** Both statements now say the files "form an evidence archive prepared for deposit ([Zenodo DOI to be added])". Check that no present-tense deposit claim was reintroduced (audit-01 F1). The packs are delivered to AC but not deposited.

## Disposition

- If A and B are clean, record readiness of the agent work in `readiness-01.md`. PR35 then waits only on AC's decisions:
  - the deposit;
  - the placeholders (report §5);
  - confirming the frozen texts;
  - the merge.
- Material defects go back to Claude.
- MINOR findings may be fixed in place only within WORKFLOW's limits.
- Preserve disagreements.

## Scope limits

As in handoff 07:
- Do not edit the manuscripts, theory records, response-01, audit-01 or the regenerated receipts.
- Do not touch `.github/`, settings, `main`, other branches or tags.
- Commits are authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers.
- Only AC merges.
- Agents create no deposit.
- Companions remain deferred until AC confirms the frozen texts.

## Outputs

- `readiness-01.md`, with heads and a disposition for each task.
- Updated PR body.
- Close this handoff with its output SHA in a following commit, and add the next numbered handoff.

## Addendum (2026-11-14 09:40, Claude, before this handoff started)

AC set the pack licence ("agpl 3.0 is the license").
- Both packs now carry `LICENSE`, the GNU AGPL v3 text, and a README line reading GNU AGPL v3.0 only (SPDX `AGPL-3.0-only`). They were repacked and redelivered under the same file names.
- The new hashes are in zenodo/README.md: `d089bc6f…` and `311621b3…`.
- Code, data and receipts are unchanged.
- **Use the current branch head as the input head** (`303c5f21` or later). In task B.3, also confirm that LICENSE and the README files are the only differences from the verified staging.

## Addendum 2 (2026-11-14 09:50, Claude, before this handoff started)

AC: "-or later, and licence everything under that".
- **Repository:** root `LICENSE`, the GNU AGPL v3 text, plus a README Licence section, `AGPL-3.0-or-later`. The SIAM macros and quoted source excerpts are excepted.
- **Manuscripts:** both availability statements add one licence sentence. Builds: 32/50 pp., frozen labels unchanged.
- **Packs:** the README lines read `AGPL-3.0-or-later`, and the MZ-CC pack omits SIAM's two files (their licence forbids distributing them alone). Repacked and redelivered: `6aa35fc7…` and `f04f65b5…`, see zenodo/README.md.
- **Additional checks for task A/B:**
  - the licence notice and its exceptions;
  - the two manuscript sentences;
  - that the pack differences from the verified staging are limited to the files listed in zenodo/README.md.
- **SIAM files in the repository:** these 2 of the 8-file SIAM package are flagged for AC, not changed. Do not resolve this yourself.
