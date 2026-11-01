# MZ prior-art and fulltext closure (CC / Padua MZ manuscript)

- Branch: `claude/mz-prior-art-20261101` · Base: main `9739a0c56b7a3976422ce60a8441bfbbfd6554df` · Developer: Claude (orchestrator) · Auditor: Codex `gpt-6-astra`, high (PENDING)
- Stage: WORK · Next: `Claude (Opus 5.5 high): Continue claude/mz-prior-art-20261101.`
- Claims: none new. Literature topic only; no PD-T/PD-N status changes (literature verdicts never change a PD status).
- For the PR: literature records for LIT-047–065 updates; new LIT IDs (next free LIT-066) only through the shared ledger `topics/padua-batch-20261031/ALLOCATIONS.md`; manuscript related-work wording; `literature/INDEX.md`, `CORPUS.md`, `topics/mz-constants/literature-search.md`.
- Open for AC: missing fulltexts (see local working track `Downloads\padua\results\mz-prior-art-20261101.md`).

## 2026-11-01 — Claude, Opus 5.5 (orchestrator)

- Rules read at `9739a0c56b7a3976422ce60a8441bfbbfd6554df` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). Role: orchestrator and literature developer.
- Task prompt: AC's "New topic: MZ prior-art and fulltext closure" (first copy truncated in Step 3; AC supplied the complete copy at 09:38).
- Read first: topics/mz-constants/POST_MERGE.md, report.md, literature-search.md, literature-response-01.md; all literature/records/mz-*.md; manuscript §1 related-work paragraph and refs.bib; PROOF_STATUS rows PD-T013–PD-T028, PD-N004; batch ledger.
- ID reconciliation: open PR #6 (programme-ideas, draft) and branches codex/padua-proof-attempts-20261101 (967131d), claude/programme-ideas-20261031 (0ef90ed), claude/bivariate-lanczos-20261031 (cf01449), claude/results-track-rule-20261101 (6eeec5b) mention only the next-free IDs PD-T029, PD-N007, LIT-066, IDEA-077; none reserves beyond them. No allocation made yet.
- Novelty gate: not applicable to new mechanisms — this topic generates no candidate, mechanism or theorem. It makes priority/attribution statements, so the audit must read the complete state/IDEAS.md.

### Step 1 — local inventory (orchestrator, directly)

- `Downloads\padua\papers`: 16 PDFs, each identified by first-page text (staged to the session workspace only): EGK 1991 SIMAX; Barrio–Peña–Sauer JAT 2010; Meurant et al. JCAM 2019 (disk points); Bartels–Jezioranski TOMS; Huhtanen–Larsen BIT 2002; Sommariva–Vianello NFAO 2015; Harris–Simanek PAMS 2021; Xu SIMA 1994; two SIMAX 2002 Lanczos/normal-matrix papers; Cools–Poppe BIT 2011; Sauer NA 2007; Van Barel–Chesnokov NA 2010; Marco–Martínez–Viaña NA 2019; Humet thesis; Mach–Van Barel–Vandebril TW629. **None is on the MZ target list.**
- `Downloads\bttb\papers` (access granted by AC's prompt; listed by filename only): ~250 Toeplitz/algebra PDFs. No filename matches any target DOI (BF01398509, BF01403676, BF01889904, S0002-9947-1984-0732113-4, 0518041, s003659900123, s003659910002, S000497270001025X, S0002-9947-1966-0187099-X, S0002-9939-1966-0189237-7, 0731079, jath.1993.1019, 0021-9045(90)90065-X). Not opened.

### Step 2 — target verification (in progress)

- Three Sonnet 5.5 high literature-verification workers (metadata + legal access only, no repo writes): group A (Nevai III/addendum, Askey 1972, Lubinsky 147, Erdős–Feldheim preceding note, LMN 1987, Mastroianni–Totik 2000, Lubinsky survey); group B (Sloan–Smith 1978/1980 and companions, Smith 1986, Mastroianni–Milovanović, Mastroianni–Russo, Xu I/II, Widom, Widom–Wilf, Don–Gottlieb); group C (ASV published, An–Wu published/corrections, An–Sommariva–Xue, forward citations 2010–2026).

## Runs needed

None (literature topic; no computation planned).
