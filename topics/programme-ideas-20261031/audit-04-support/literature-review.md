# Audit-04 literature integration support

Rules/candidate: `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`.
Auditor: independent Codex literature integration subagent; assigned `gpt-6-astra`, high (runtime model metadata not separately exposed). Date: 2026-11-01.

Scope: integration following main merge `3e0100f` from main `21e620b`, first dedupe `ad45de2`, second dedupe `af3881b`, and final literature allocation. Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the candidate. No new idea, mechanism, novelty claim or mathematical result is generated; the novelty gate/full IDEAS reread does not apply to this bounded registration audit. Accepted mathematics is not reopened. No external search, PDF retrieval or new fulltext reading was performed. Only new audit-04-support/literature-* files were written; Git operations were read-only.

## Decision

**Changes required: one P2 integration finding.** The dedupe inventory and declared open comparison flags are retained, but three imported statement rows lost essential fields through pipe splitting. These are new registration defects; they are distinct from the twenty explicitly open source-comparison flags, which this audit neither clears nor treats as newly discovered mathematical problems.

## LIT-I1 (P2): restore three incorrectly parsed literature rows and remove formula-derived source keys

The baseline uses internal absolute-value/cardinality pipes in rows 16, 52 and 73. Integration treated these as column boundaries. At the pinned candidate:

| Baseline | Final row | INDEX line | Observed corruption |
|---|---|---|---|
| 16 | LIT-342 | 155 | Statement stops at `condition (`; source is `c`; locator is `+`; coverage is `)/(; s; overlaps LIT-022`. The hyper-rotation condition, instability qualification, source locator and VERIFIED-fulltext evidence are missing. |
| 52 | LIT-369 | 182 | Statement stops before the cardinality hypothesis; source is `Y`; locator is `=`; statement fragments replace coverage. The actual locator and the explicit limit that the cubature-weight formula was not checked disappear. |
| 73 | LIT-389 | 202 | Statement stops before the weight factor; source is `x±y`; locator contains the remainder of the statement; original UNVERIFIED label disappears. |

The same parser error introduced CORPUS rows with keys `c` (line 84), `Y` (line 90), and `x±y` (line 107), carrying formula fragments as reading coverage. These are not bibliography keys. The first integration map JSON correctly identifies the real keys (`egk-1991`, `harris-simanek-2021`, and `xu-2024-minimal; xu-2025`), so neither new reading nor mathematical adjudication is necessary to repair this.

The checker parses all seven original baseline columns using their literal space-pipe-space delimiters and compares statement, source, locator and verification fields for all 95 retained rows. After normalizing existing provisional-to-final reference aliases, exactly these three rows fail retention: twelve field mismatches. The other 92 retained rows preserve those fields. The original baseline text remains available at lines 44, 90 and 111 respectively.

Acceptance criteria for the developer response:

1. Keep LIT-342, LIT-369 and LIT-389 and their current provisional aliases. Restore their complete baseline statements, hypotheses, sources, locators and statement-specific coverage. Escape internal pipes for valid Markdown tables without changing their mathematical meaning. Preserve their overlap links and all existing scope/conflict qualifications, including row 73's paper/book conflation flag.
2. Remove the three bogus CORPUS keys, retaining the proper existing EGK and Harris-Simanek entries. Resolve row 73 through the explicitly documented Xu keys/alias without representing the paper/book attribution issue as resolved. Do not invent a source or coverage claim to replace the formula fragments.
3. Preserve the 95/32 allocation ranges, all 16 merger aliases, row 58's retained overlap, and all 20 open second-pass flags. Rerun the checker at the corrected commit and independently inspect the repaired Markdown rendering/columns. No fulltext search or new proof is required.

## Dedupe and retention checks accepted in their bounded scope

The first map has 111 rows: 2 same, 51 overlap, 58 new. The second map has 55 rows: 14 same, 38 overlap, 3 unrelated. The second-pass Markdown preserves the helper's earlier 15-same enumeration but explicitly records the developer override and actual 14/38/3 disposition; the JSON, crosswalk and applied IDs agree with the latter.

Exactly sixteen baseline IDs merge without new IDs: 48→002, 60→010; 01→193, 03→195, 04→197, 06→198, 09→199, 17→183, 30→174, 32→148, 33→149, 35→152, 36→153, 37→161, 44→099, 78→130 (targets have the LIT- prefix). All crosswalk rows retain baseline links. The other 95 programme rows occupy LIT-332–426; the 32 lattice rows occupy LIT-300–331. All 111 original programme IDs are accounted for once across retained allocations and mergers. Every inherited main INDEX row is byte-for-byte unchanged.

The published facts of all sixteen merger pairs were compared with their current target rows and linked records, not just their titles. Important qualifications survive:

- The first-pass merge criterion explicitly excludes extra round-note inferences. Row 60's cubic Padua inference remains in the baseline; LIT-010 remains an UNVERIFIED author conjecture, expressly not an obstruction theorem or finite-n certificate. Row 48's source/theorem/secondary qualification remains in the baseline and linked ideal-theory record.
- Row 01's Q=WΦ and recurrence relations are in the linked LIT-193 record; row 09's comparison with HL and point-by-point updating are in the linked LIT-199 record. They are not all repeated in the shortened INDEX cells.
- Row 06 has a known wording difference (`corners` versus the source record's printed `edges` and two-line estimate). Its conflict remains one of the twenty flags; deduplication does not certify the conflicting geometrical wording as resolved. The zero-pivot statement and lack of a zero threshold agree. This accepted alias is subject to the explicitly retained wording correction.
- Rows 17 and 78 retain open-question status. Row 78's stronger programme spot-check evidence stays in its linked baseline; it does not silently upgrade the existing LIT-130 row, which remains secondary/UNVERIFIED.
- Rows 32–37 retain the exact-arithmetic hypotheses/window length, absence of a published total flop count, garbled/UNVERIFIED tolerance, observation-level finite-precision wording, and distinction between the BIT observation and SIMAX Ritz-value observation. No observation is promoted to a proved theorem or author conjecture.
- Row 44 remains univariate, secondary and citation-qualified; merging it into a broader target does not import that target's other clauses as independently checked programme claims.

Row 58 is correctly excluded from the merger set and retained as LIT-375. Its JSON relation is `overlap` with LIT-141 and LIT-142, and both its INDEX row and comparison map retain the unsupported Pitman RN 312 attribution issue. The map points to LIT-230/231 as evidence limits; no source attribution is newly adjudicated here.

All twenty second-pass conflict strings remain in the JSON map. Nineteen retained rows explicitly carry `flag in integration-map-pr10`; the twentieth is merged row 06, whose conflict remains in the map. INDEX lines 139–141 explicitly state that the flags remain open after allocation. The first-pass flags also remain listed at lines 131–137. These open issues include locator/hypothesis/coverage differences and cannot be counted as cleared by final IDs.

CORPUS cleanup of the 34 exact keys named at line 77 is sound: each now occurs exactly once under that exact key, and its retained full row is byte-for-byte identical to main `21e620b`. Source-specific reading limits and gaps were not dropped by that cleanup. The five preexisting key aliases and the two declared lattice-paper aliases remain documented. This acceptance of the 34-key cleanup does not excuse the three separate formula-derived bogus keys above or claim all placeholders have complete bibliography.

## Reproducibility and evidence identity

Executed with Python 3.12.14 from the repository root:

```text
python topics/programme-ideas-20261031/audit-04-support/literature-check.py > topics/programme-ideas-20261031/audit-04-support/literature-check.json
```

Exit status was **1**, intentionally signalling the twelve recorded retention mismatches and three bogus CORPUS rows. All inventory, alias, inherited-index, 34-key cleanup and flag-retention assertions passed. This is an independent integration check, not a mathematical experiment or independent re-reading of the cited publications. Optional first argument selects a later pinned commit for a developer-response rerun.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| literature-check.py | 6672 | `6e5a19ce8774791ace443242cb104a09eb9ed72ffdbd5684400b8873c425f479` |
| literature-check.json | 16158 | `a26b8fed0dcf392dcdf0c4556d35acd47855546afadf6954ad44718a950f8ed3` |

The receipt hashes every input consumed by the checker, including both maps/Markdown companions, baseline, INDEX, CORPUS, crosswalk, allocation map, ten linked literature records, and main's INDEX/CORPUS. No generated evidence beyond these small necessary checker artifacts is needed. Existing source coverage, unavailable PDFs and source attribution limitations remain as previously recorded.
