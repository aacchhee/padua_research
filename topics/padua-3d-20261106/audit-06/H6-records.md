# Audit-06 focused record/provenance check (R): response05 at 57f4669

Auditor: Claude Opus 5.5 (`claude-opus-5-5`), high. Date 2026-11-12. Read-only on the repository. All execution happened in an isolated `git archive` copy at `.../scratchpad/a6-R/tree`, with a second copy at `.../scratchpad/a6-R/mut` for mutations. Nothing was run in `rerun6`.

- Focused diff: `ae4ab4741265f55ac10847659af89dad05441274` → `57f4669be083ec286d84b0f1e2f14b3b50ed14ca`.
- `c889c1a` changes only the handoff-21 status line (to `done in 57f4669…`) and adds handoff 22.
- Exactly one handoff (22) is open.

**Scope:** H6; the manuscript split and bibliography; the D3 disposition reason; the split headers; provenance (A-M7/M8/M9); storage; trailers.
**Not covered:** H1–H5 mathematics and attribution wording beyond spot checks.

## Verdict

No BLOCKING or MAJOR findings. Three MINOR wording/pointer items (fix texts below) and five NOTEs. Every returned item in scope is resolved as stated.

## Checks and evidence

### H6: PASS

`frontier-dispositions-20261112.md` is a new dated companion, and the protected records are untouched:
- `git diff ae4ab47 57f4669 -- frontier-assessment.md frontier-2026-11-08/` is empty.
- Neither the earlier audit/fix records nor any old handoff body changed.

Dispositions:
- **C5** is deferred. The record states that it is "**not subsumed** by D1" because D1 does not prove the n³/4 coefficient, and the historical conditional subsumption is "not adopted". Resume condition: AC explicitly reopens it, with a bounded proof task, classification sources or a local classification, and an exact folding/count statement separated from D1/T9. More determinant trials do not count.
- **C6** is deferred. Resume condition: a concrete phase/union class, an exact hypothesis that escapes T1/T7, a decisive test, and explicit reopening.
- **C8** is "completed record work, retained with source gaps", with an explicit no-restart resume condition.
- No final IDs or PD-N allocations are made, and no frontier theorem is claimed.

### Manuscript/process split: PASS, one MINOR

I grepped `paper-note-draft.md` for `\.md|IDEA|handoff|Claude|supplemental|audit|PD-[TN]|LIT-|Codex|commit|SHA` and found **zero hits**. I also grepped for D1–5, T#, C#, LOG, frontier, worker, orchestrator, reviewer and response. The only process residue is "the topic's historical5.54" at line 85 (MINOR-1).

Repository IDs, the claim ledger, artifacts, review states and source maps now live in `paper-repository-context.md`. Theorem A (line 28) and the abstract state that all nodes lie in the closed cube.

### Bibliography: PASS, one NOTE

There are exactly **28** entries (lines 95–122). After the list, the minimal-cubature leads (Noskov–Schmid, Hirao–Sawa, Schmid) are given as explicit gaps. Entries with unknown titles or journals say so explicitly: Białas-Cież et al., Carnicer–Sauer, Kolountzakis, Lyubich, and the Belgian chapter (locator-only).

The external network was blocked (the Crossref host does not resolve), so I traced metadata against the repository's own source records instead:
- **Xu 2003**, J. Complexity 19, 392–402: audit-05/D1b.md:26 and final-d1/sources.md:45.
- **Lyness 2003**, J. Complexity 19, 321–331, DOI S0885-064X(03)00005-0: novelty-gate.md:60, source-records.md:104 and literature-3d.md:18.
- **Wang–Wang–Wang**, CAMWA 68(5), 632–638, DOI camwa.2014.07.009: source-records.md:25 and frontier-2026-11-08/S1.md:11.
- **Cools–Lyness 2001**, Math. Comp. 70, 1549–1567: novelty-gate.md:17 and literature-round06/t10-sources.md:7.
- **Horak–AlBdaiwi**, IEEE IT 58, 5490–5499: source-records.md:55.
- Also traced: Li–Sun–Xu, Li–Xu, Greenfeld–Lev, Lev–Matolcsi, Dencker–Erb, DEKL, Cools–Poppe, Dolbeault–Chkifa (S3.md:11), and Hirao–Sawa/Schmid (LIT-413).

I found no fabricated detail. The one untraced field is NOTE-1.

### D3 disposition reason: PASS

`final-d3/candidate.md:47-50` adds only the "Disposition reason" field. `git diff -- final-d3/theory.md` is empty, so the theorem and status are unchanged.

### Split headers: PASS

All four headers carry the full provisional IDs and are reciprocal, each with a local link:
- `t7-finite-reduction.md:4` gives "Split into: PD-N?…-codex-T7-09"; `t7-one-phase-refutation.md:4` gives "Split from: …PD-T?…-codex-T7-03".
- `r08-lattice-minima.md:4` gives "Split into: PD-T?…-codex-D4-minima"; `finite-minima.md:4` gives "Split from: PD-T?…-codex-R08-minima".

In `finite-minima.md`, only line 4 changed.

### Provenance: PASS

Historical evidence is untouched:
- `git diff ae4ab47 57f4669 -- evidence/fd4-manifest.json evidence/fdr-d2-quality-replay.json` is empty.
- Measured identities: 5,386 B, `f4c10b53…`; 721 B, `ecb06674…`. Both match the provenance note.

The A-M7 retirement of all nine prose pins is in `response-05-provenance.md` §A-M7. It is dated, and the D4 header edit is part of the same commit (NOTE-3).

The enumerator source `audit-04/code/A1/aud_enum.cpp` is unchanged since 1cb3841 (10,115 B, `d39563b9…`). It is now the third entry of `inherited_inputs`:
- `artifact_manifest.py` gains one line (+1).
- The master gains that entry (+382 B, from 18,976 to 19,358 B).

g++ is recorded only as a "current observation" (Debian 14.2.0), with the historical version marked unrecoverable. The binary-identity claims check out against the receipts:
- The producer binary (27,824 B, `6a2af8df…`) and the auditor binary (30,448 B, `2fe30339…`) each appear in both `fd4-lee.json` and `fdq-lee-replay.json`.
- The two binaries differ from each other.

### Storage: PASS

From `git ls-tree -r -l 57f4669`, summing json/txt/out/gz/stdout/csv/jsonl:
- Repository generated-output class: **8,685,984 B** across 1,763 files. That is ≤ 10 MB and +10,600 B over baseline (8,675,384 B).
- The increase equals the two new receipts (2,715 + 7,503 B) plus the master growth (382 B).
- Topic class: 1,689,805 B.
- Master: **19,358 B**, within the 32 KiB limit.
- The only files over 32 KiB belong to other topics and predate this diff.

### Trailers: PASS

`git interpret-trailers --parse` on 57f4669 and c889c1a yields both `Agent: Codex` and `Model: …`. The audit-05 blank-line NOTE is resolved.

## Commands run (in the copy; venv Python 3.13.18, NumPy 2.3.5, SciPy 1.17.0, `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1`, `-B`)

1. `artifact_manifest.py --verify` gives `{"verdict":"PASS","artifacts":366,"bytes":2301750}`.
2. Single-bit XOR mutations (size-preserving), with a restore after each. Every mutation gives `FAIL: code/data set or identities changed`, rc=1, and every restore gives PASS:
   - `audit-04/code/A1/aud_enum.cpp` (the new inherited input);
   - `tracks/lattice-unisolvence/code/c3_rank.py`;
   - `code/fd4_lee.py`;
   - `evidence/fd4-manifest.json`;
   - `evidence/r05-d2-quality-replay.json`.
3. Two further mutations:
   - Adding `evidence/extra.txt` gives FAIL.
   - Deleting `aud_enum.cpp` makes the checker stop with `FileNotFoundError` (non-zero exit). Restoring it gives PASS.
4. `r05_quality_replay.py --output …/a6-R/q.json` passes with values bit-identical to the committed receipt:
   - **n3 = 5478.148340739174** and **n4 = 546899.5809121559**, each over 69,433 queries.
   - Relative differences 3.1046e-14 and 3.6229e-13.
   - All five guards true.
5. `r05_manifest_replay.py --output …/a6-R/m.json` (TMPDIR inside scratchpad) passes:
   - 44 codec controls, with `checks` identical to the committed receipt.
   - The mutation of `aud_enum.cpp` is rejected, giving the return-code sequence [0, 0, 1, 0, 0].
   - `live_master_unchanged` is true.
6. **No mutation of the live tree.** SHA256 inventories of the whole copy taken before steps 1/4/5 and after them are identical, and `find -newer` finds nothing.

The receipts contain:
- the command argv;
- source and input identities (path, bytes, SHA256);
- the historical receipt identities;
- Python, platform, NumPy and SciPy versions;
- thread environment, seed and start time;
- a labelled note that the nested `input_head` (`6d894d50…`) is historical.

## Findings

**MINOR-1. Manuscript process residue.** `paper-note-draft.md:85`, "…a stronger n4 value than the topic's historical5.54." "The topic" is a repository reference inside the manuscript. Eligible fix:
- Old: `these include a stronger n4 value than the topic's historical5.54.`
- New: `these include a stronger n4 value than the earlier value5.54 obtained in this work.`

**MINOR-2. Stale prose that the provenance note supersedes, with no pointer.** `final-d4/results.md:78-79` still says "The manifest identifies all worker artifacts and generated bytes". `response-05-provenance.md` §A-M7 supersedes this, but a reader of results.md is not directed there. Eligible fix, appended after `raw scratch remains regenerate-only.` (line 79):
- `Dated note 2026-11-12: the nine final-d4 prose rows of evidence/fd4-manifest.json are retired as acceptance pins by [response-05-provenance.md](../response-05-provenance.md#a-m7--retire-historical-prose-acceptance-pins); current code/data integrity is the master manifest's --verify.`

**MINOR-3. Rounding in the provenance note.** `response-05-provenance.md:86` says "`3.11e-14` and `3.63e-13` or less". The receipt gives 3.104616718e-14 and 3.622948063e-13. "Or less" keeps the sentence true, but the figures do not match the receipt. Eligible fix:
- Old: `` `3.11e-14` and `3.63e-13` or less``
- New: `` `3.10e-14` and `3.62e-13` ``

**NOTE-1. One bibliography field with no repository source record.** The Caliari–De Marchi–Vianello entry (`paper-note-draft.md:98`) gives "Computers & Mathematics with Applications55 (2008)", but no repository record carries that venue or volume: audit-03/T10.md:61 and S5.md:41 give only the title and year. To my knowledge the field is correct, but I could not check it here. Either add a source record for it, or mark the venue "(venue not established by the retained record)".

**NOTE-2. The committed manifest receipt is a snapshot from before the final tree.** In `r05-manifest-replay.json`, `verified.bytes` is 2,301,684. Verifying the committed tree gives 2,301,750, a difference of 66 B. The likely cause is self-reference: the receipt lies inside the covered `evidence/` tree and was rewritten after the run. The 366-artifact count, the controls and the inherited inputs all agree. This does not affect integrity, which the live `--verify` establishes.

**NOTE-3. "Precedes" is document-level, not chronological.** Provenance §A-M7 says the retirement "precedes the response05 split-header correction". Both are in the single commit 57f4669, so the precedence is the note's effective statement, not separate commit order. The wording is acceptable.

**NOTE-4. Stale constant in the master generator, outside this diff.** `artifact_manifest.py:255` hardcodes `rules_input_sha` as `38227202…`, which was not refreshed in this round. It is administrative metadata only.

**NOTE-5. No network.** Bibliography checks were limited to tracing against repository records (see NOTE-1).

## Residual uncertainty

- Bibliographic correctness of the traced entries rests on repository records, not live publisher metadata.
- H1–H5 mathematical and attribution wording was not re-audited here.
