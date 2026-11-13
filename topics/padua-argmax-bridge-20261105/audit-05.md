# Claude audit-05: focused audit of response-04 (handoff 32)

Companion record for the manuscripts: [audit-05-manuscripts.md](audit-05-manuscripts.md). Review reports and
auditor scripts: [audit-05/](audit-05/). Audit round 5, after [audit-04](audit-04.md) and
[response-04](response-04.md). It is **not** a readiness decision, waives nothing, and PR 27 stays a draft.
Only AC merges. Scope: the material changes since audit-04 only; unchanged analytic components were not re-audited.

## Decision

**Mathematics: ACCEPTED.** No reviewer found a mathematical error in any changed text (restored Lemma 4.2
reasons, the row-average and four row identities, the gate clauses of Cor 4.6/4.7, the corner-loss chains, the
base-value table, the elementary-constant explanations). Every number recomputed reproduces.

**Evidence readers:** the E4-01..E4-04 repairs hold on the original return with the real authenticated `padua30.zip`
and no adapter, but the repaired onset-512 reader has a **new MAJOR (E5-01)**: it would reject the canonical 320..510
archive that its own campaign writes. The canonical ZIP, the I25 bundle and the native histories are still absent, so
degrees 320..510 remain **not accepted** by this audit.

**Manuscripts:** builds, correspondence, freeze and baseline separation, mutation controls and bibliography are
accepted. Remaining items are wording and exposition, including a false clause in a proof in both texts (M5A-01), a stale
custody statement in the companion (M5B-01) and several response-04 rows that overstate what changed. All of it returns to
development as one paired batch with a new freeze.

Because MAJOR findings are open (E5-01, M5B-01, M5A-01), the stage returns to **WORK**.

| Verdict | Result |
|---|---|
| 1. Mathematics | **Accepted** for all changed text; no error found |
| 2. Evidence readers | E4-01..E4-04 repairs **accepted**; **E5-01 MAJOR** (reader rejects canonical-run files); 320..510 evidence **not yet accepted** |
| 3. Paper (57 pp) / companion (150 pp) | Mathematics accepted; paired wording batch required (see audit-05-manuscripts.md) |
| 4. Agreement and baselines | **Agrees**: 19 statements, 85 numbered environments (86 equation numbers), 116 labels; baseline controls pass; paired silent mutations fail the freeze |
| 5. Disposition accuracy | Several response-04 rows **overstate** what changed (details below) |

## Identity, rules and disclosures

- **Models.** Orchestrator `claude-sonnet-5-5` (the session model was switched with `/model`; the prompt named Opus 5.5
  xhigh); all audit work by **four Claude Opus 5.5 subagents instructed at xhigh** (effective effort not exposed): M5A, M5B,
  E5, B5; distinct from the Codex developers and reviewers. Supplementary Astra reviews were read as evidence, not as the
  required Claude audit.
- **Rules** read at be9a831; AGENTS.md, agents/, templates/ byte-identical at the audited head.
- **Candidate.** `codex/padua-argmax-bridge-20261105` at `33b9eca8167980cad0b0a491da7de64280c9a158` (handoff input head
  `f81682557c104e18497d2e08278a99bb97572773`); final TeX/Bib freeze `ad908acb21d3589d85635618ff68f63dd01cfbca` (no `.tex` or
  `.bib` changed after it; the baseline update is the separate commit `98261ae`); main `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`
  merged at `941aa33`.
- **Inputs supplied by AC this round (authenticated by the orchestrator):** the two parts of the original return (joined
  36,045,486 B, sha256 `b00fd57f…`, byte-identical to the earlier copy) and `padua30.zip` (25,111,335 B, sha256
  `aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2`, 257 members; the reviewer authenticated all 250
  manifest rows against manifest `5b89fa66…`; used as data only, no launch script run). **Not supplied:** the canonical
  `onset512-return-20261108.zip` (`da63280a…`), the I25 bundle (`d1d03156…`; AC does not know where it is — not asked
  again), the derivative, inventory and review ZIPs, historical PDF bytes and the 632 MiB native histories.
- No Syvert access, no native degree campaign, no retry or rescue, no changed thresholds.

## Executed checks

[E] executed by the auditors; all outputs in fresh scratch paths; every consequential command run once under a `wait4`
observer where an engine or archive was involved.

| Review | What ran | CPU | Result |
|---|---|---|---|
| E5 | `check_reader_repairs.py` (exit 0, 40 controls); `runtime_probe.py` (exit 0, 31 controls, 4 probes); `onset512_analytic/check.py` (exit 0, enclosures identical to the receipt); repaired `verify_compact.py` on the original return with the real package: `--expect-plan all` exit 0 (280 pairs, exactly 41..319 plus 511, sample [199,238], stdout identical to the recorded one, `3f6605da…`), `--expect-plan small` exit 1, no plan exit 0 `completed_subset`; audit-03 30-control suite 30/30; reader and runner under `-O`, `PYTHONOPTIMIZE=1`, `-E -O`, `-OO` all exit 1 with no output; 14 own reader controls and 13 own in-process verifier controls and 7 end-to-end archive runs (hardlink alias, alias before target, symlink, directory, 800 aliases hitting the size cap, `jobs/999` under `-O` and normally), all rejected as preregistered; the reader's typed parser accepts all 3,978 authentic engine JSON records | about 165 s | all as stated |
| E5 | Own read-only per-path budget accounting; `evidence_index.py --check` | small | PASS 396 entries; figures reproduce |
| B5 | Fresh builds of both PDFs; `check_correspondence.py` (default and `--archival`); `check_baseline_controls.py`; own `.aux` parser; mutation harness in copy trees; rename-aware scanner against 24a98db | under 2 min | 57 and 150 pages, 0 errors/undefined references/overfull boxes; PASS 19/85/116 and 13/90/113; 7 controls pass; all paired mutations fail the freeze |
| M5A | Exact and interval recomputation of Lemma 4.2, rows, termwise maximum, gates at n = 192, 256, 295, 512; 32 duplicate pairs diffed by hand against 24a98db | about 6 min | all reproduce; one false clause found (M5A-01) |
| M5B | `onset512_analytic/check.py` from a byte copy; mpmath 80-digit intervals for all 60 base-value entries and the gates; corner-256 chains in exact rationals | under 1 min | all reproduce |

## Findings: evidence and records

### MAJOR

- **E5-01. The repaired onset reader rejects files its own campaign writes, so the required canonical rerun cannot pass as
  committed.** `return_bundle.py` lines 171–216: the member allowlist has no `storage-dedup.json` and no top-level
  `.preserve.lock`. Both runner versions (historical `459d0728` line 120, current line 124) call
  `compact_pack/storage.py deduplicate()` after every validated pass, which always writes `<pass>/storage-dedup.json`
  (line 62) and creates `<output>/.preserve.lock` (line 44); the exporter adds both to the archive. The reviewer's controls
  reject exactly these names ("unregistered campaign member: out/.preserve.lock", "unregistered pass member"). Corroboration:
  the original return's sampled pass directories contain `storage-dedup.json`, and the recorded 11,713 members fit 60 per
  case (191 x 60 = 11,460) only if that file is present. The rejection is a safe failure, but the documented deposit command
  will fail on the canonical ZIP. **Derived from the code and the member-count check, not observed on the canonical ZIP**
  (still absent). Fix: allow and schema-check both names, add a round-trip control (real `deduplicate()` + `export()` + reader
  on a synthetic campaign tree), re-review, then run on the actual ZIP. Material change.

### MINOR

- **E5-02** `code/onset512_analytic/check.py` relies on 28 asserts and always prints `assertions: PASS`; under
  `PYTHONOPTIMIZE=1` a copy with a falsified gate printed PASS and exited 0 (normal mode exits 1). Recorded results are
  unaffected. Document `python3 -E -B`; an optimization guard would be a material change.
- **E5-03** the budget attribution is one-sided (figures reproduce exactly). Main `b5388c2` alone totals 9,733,758 B, under
  10 MB; this topic's own counted share is **1,995,804 B** (exactly HEAD minus main); merging PR 27 would take main to
  11,729,562 B. The records say the excess arrived with Padua3D but do not state this topic's own share. The "actual" figure also
  leaves out the topic's own 2,087 B `FREEZE.md` exception (11,731,649 B by the topic's convention, against the bound
  11,751,309 B). Report the budget limitation as is; no unrelated evidence was deleted or relabelled (no file outside this topic
  differs from main).
- **E5-04** the runtime probe's gradual-underflow check cannot detect flush-to-zero when denormals-are-zero is also on: with
  MXCSR FTZ|DAZ set, `2^-1022/2` is bitwise zero, yet the probe reports all four true and its 31 controls pass. FTZ alone and
  round-toward-zero are detected. J03 lines 264–267 and the J3-05 disposition overstate the scope; state it, or compare bit
  patterns.

### NOTE / EDITORIAL

- E5-05 `verify_compact` needs no optimization refusal (no asserts on its path; identical output under `-O`). E5-06 metadata
  accepted as data: symlink-mode and directory-mode ZIP members under allowed names, and an inventoried extra file in a pass
  directory; none is extracted. E5-07 the export-side `completed()` accepts `false` as an exit code (producer path only). E5-09
  the reader can only ever read the one historical archive (degrees 320..510, runner 459d0728).
- **E5-08 (editorial)** `code/local_onset512_campaign/README.md` should say the campaign ran runner 459d0728 and the current
  runner `a198b651` has run nothing; deposit README lines 170–175 should say the onset command fails until E5-01 is fixed;
  lines 227–231 should label 24a98db historical (superseded by ad908ac). A dated addendum for these is committed with this audit.

### Adapter-dependent audit-04 results now confirmed without the adapter

The three compact-verifier runs (plan all / none / small), the 30 controls, the own-corruption classes, and the 136 previously
unchecked header reads (now byte-checked against the real package). Still adapter-only: every positive result for the
onset-512 reader (E5's 191-pair positive run exists only under the developer's arithmetic adapter).

## Disposition accuracy (response-04)

Rows the audit found **overstated or not supported by the text**: B4-01 / P4-14 (paper Figure 2 still collides, B5-01,
M5B-06); B4-04 / X-13 (marked verified on the grounds of "no overfull boxes", but the finding was equation numbers on their own
line: (11), (20), (25), (39), (50), (54) still do, B5-02); B4-05 (explicit pi bracket still absent from the companion, B5-03);
P4-01, P4-08, P4-12 (fixed in the paper only, the companion unchanged, M5B-01/02); C4A-01 (consolidation lost unique reasons,
M5B-04); C4D-05 (companion cell lists the IEEE rounding model under "Proved in the text", M5B-03); C4C-n3 (collisions
"corrected in both texts" but e, r(w), tau remain in the paper and w in the companion, M5A-05); the supplementary review's
"retained" rows B5, C1, C10 (three one-line reasons still lost, M5A-02). Confirmed: C4B-01, C4B-03, C4B-04, C4C-M1, C4C-M3,
m3..m8, J1-02, J2-01..J2-03, J2-08, P4-06, P4-07, C4D-12, P4-05, N4-12, and the model/runtime, 471-distinct-trees,
native-endpoint, split trust table and Popen/ECHILD wording in the paper.

## Auditor in-place MINOR fixes (third-and-later round rule)

Dated addenda only (stale process text and links), committed separately from this report:
1. `report.md` (end): B5-08, "all 942 phase trees" means 942 records over 471 distinct trees (J3-01).
2. `code/local_onset512_campaign/README.md` and `zenodo-deposit/README.md` (end): E5-08 (runner identity, the onset command fails
   until E5-01 is fixed, 24a98db is historical).

Not fixed in place: E5-01 (code), E5-02..E5-04 (recipe or code scope), every TeX edit (any change breaks the ad908acb byte freeze and
needs a new paired freeze and baseline update), response-04 rows.

## Budget and readiness limitations

The global generated-class bound (11,751,309 B; actual classified sum 11,729,562 B) exceeds the inherited 10,000,000 B cap. This
topic's own counted share is 1,995,804 B; main alone is 9,733,758 B. Report as a budget limitation and AC's decision; do not
remove another topic's evidence or invent a cold-storage destination. Reservations unchanged; a union refresh is required before
any future ID assignment or readiness.

## Limits and not done

- Not examined (files absent): canonical 320..510 return and its reader run, I25 bundle and data-only checks of 320/384/458/510,
  derivative/inventory/review ZIPs, historical 48/162 and 51/147 PDFs (so `--artifacts` mode did not run), the 632 MiB native
  histories. No custody claim: deposit preparation is not delivery, no Zenodo record or DOI exists.
- Not re-audited: unchanged analytic components, J01/J02 internals, the native Arb kernels.
- The Pimenova Math-Net ID and any DOI could not be resolved from this session (Crossref and mathnet blocked).

## Prioritized response plan

1. **E5-01 first** (material code change with a round-trip control), then E5-02..E5-04, E5-08 wording; focused re-review; only then
   the canonical-ZIP reader run (needs the ZIP and the package).
2. **One paired wording batch** (new freeze, rename-aware baseline, rebuild): M5A-01 (false collision clause), M5B-01 (companion custody
   wording), M5B-02..07, M5A-02..07, B5-01..05, B5-09/10 — see [audit-05-manuscripts.md](audit-05-manuscripts.md).
3. Correct or honestly re-label the overstated response-04 rows in `response-05.md`; correct the supplementary review's "retained"
   rows by dated note.
4. Budget: put the global 11.75 MB bound and this topic's 1,995,804 B share in front of AC.
5. Data: AC supplies or confirms unavailable the canonical ZIP and the I25 bundle (Claude runs the preregistered checks in
   `audit-04/WHEN-INPUTS-ARRIVE.md`), and decides the Zenodo deposit, the post-repair snapshot to cite in the data statements and the
   native-history custody.

2026-11-13 · orchestrator `claude-sonnet-5-5`; audit work by four Claude Opus 5.5 subagents (instructed xhigh) · rules read at be9a831,
unchanged at 33b9eca.
