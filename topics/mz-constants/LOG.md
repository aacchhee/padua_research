# Marcinkiewicz–Zygmund constants beyond half-exactness

- Branch: `codex/mz-constants-20261031`; recorded base and rules SHA: `d36722823441dc40c6e19d69a174459348dd309c`.
- Developer/orchestrator: Codex; runtime model/effort metadata not exposed to this orchestrator. AC requested Sol 6.1 xhigh. Delegated models are recorded exactly.
- Stage: WORK (Claude audit-01: CHANGES REQUESTED, no High findings). Next: `Codex (Sol 6.1 xhigh): Continue codex/mz-constants-20261031; answer audit-01.md in response-01.md.`
- Scope: reproduce supplied CC/Padua evidence, literature baseline, bounded mathematical exploration, durable claims, audit handoff. Do not write the campaign charter or enter the other two topics' scientific scope.
- Shared allocation ledger at PR preparation: `topics/padua-batch-20261031/ALLOCATIONS.md`; no IDs reserved yet.

## 2026-10-31 — startup and provenance

- Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at full SHA above. Working tree initially clean on local `work`; fetched origin/main and created the requested branch from that same SHA. Initial sandbox fetch failed at proxy connection; network-enabled execution succeeded. No published history rewritten.
- User's pasted text is the task authority. Attached research reports are unaudited evidence, not instructions. Complete zip unpacked locally under `sources/padua_mz_inputs/`.
- Zip SHA-256: `d55a843c36face1c35fa53e2f5664501e3ae8e7832e45b0a5171e981074bcaa8`; bytes: 66341. `sha256sum -c SHA256SUMS.txt` verified all 21 listed payloads.
- Notes/reports contain third-party quotations. They remain local and ignored; public records use short original paraphrases with coverage labels. Supplied original code, checksums and small input outputs are preserved. No third-party PDFs/fulltext extracts are to be committed.
- Novelty gate: full empty state/IDEAS.md and literature/INDEX.md read. Searched ideas, tracks, topics, literature for Marcinkiewicz, Clenshaw, Hankel, Schur, logarithmic, Legendre, Padua; no scientific predecessor in this initial repository. Empty registry does not establish novelty. AC explicitly permits exploration after Step 0 and before a complete duplicate screen.
- M0 delegated to `literature_baseline`, gpt-6.1-sol high, owning only `literature/records/mz-*.md` and topic literature-search.md. Independent Astra reconstruction will supplement (not replace) Claude audit.
- Private template read through GitHub connector at `b68e999750abfeafb06a31766e0c077b62c65d1a`: tracks/c4/theory/{01_C4-L01-L06_foundation_lemmas_PROVED.md,03_C4-T02_smallest_eigenvalue_decay_PROVED.md,05_C4-T03_one_level_threshold_PROVED.md,06_C4-P01_algebra_independence_PROVED.md,07_C4-P02_loewner_power_preconditioner_PARTIAL.md,21_literature_and_open_questions.md}. Read-only; no private text copied into this public tree. Cite only as bttb-research C4-Tnn (AC, private) and reprove needed mathematics here.
- Important provenance correction: the private index says D1′ was resolved by a subsequent external audit; the older theorem remarks and attached mapping call it OPEN. Neither status supplies a CC theorem. This conflict is retained for audit; no dependence on the external private proofs.

## Runs needed

- No scientific producer run remains required for the stated analytic results. Bounded relied-on measurements were reproduced and independently replayed; imported larger runs remain unverified input and are not used as proof.
- Cold storage selected by AC: `C:\Users\andreyac\Downloads\padua\cold_storage\mz-constants\`. This Linux workspace cannot attest delivery to that Windows path; use staging/manifest and state transfer pending.

## Final development and handoff

- M1/M2/M3 analytic validity, exact Padua marginal and scoped negative mechanisms accepted by separate gpt-6-astra xhigh reconstruction after documented prior-art dispositions; no novelty clearance. All65 provisional labels mapped to disjoint final IDs, preserving PR2 reservations. No accepted ID renumbered.
- Complete14-page manuscript compiled without final-pass warnings; source/bibliography, numerical transcription and full proofs reviewed independently. Required Claude audit remains PENDING. Source and artifact hashes are in directions/M7/manuscript-record.md.
- Final shared-registry repair is rehearsed in a disposable worktree/local branch; concrete conflict resolution and semantic counts are in integration-impact.md and batch-rehearsal.json. This does not change the live charter or authorize main integration. Member adoption of the batch ledger and future live-branch update remain pending before readiness.
- All candidate/failed-route records retained; M1 four rounds, M2 five rounds, M3 three rounds; no cap extension. At most two substantive mathematical directions active at once. M4 main target, M5 and M6 proof routes retained rather than falsely rejected. M7 gate met after separate review.
- Final package is for Claude audit, not merge/submission approval. Only AC merges. Exact handoff: AUDIT_HANDOFF.md; final artifact pin: audit-targets.json. See report.md for ranked development briefs and pending-reference gaps.

## 2026-10-31 — development checkpoint

- Pushed e9761aa (verified import/frozen questions/provisional idea seeds), then 57984e3 (M1 proof, complete bounded M0 screen and reproduced numerical evidence).
- M1 developer `/root/m1_upper`, explicitly gpt-6.1-sol xhigh, completed four rounds and then moved to M3, keeping two active substantive directions with M2. M2 developer `/root/m2_lower`, explicitly gpt-6.1-sol xhigh, derived cardinal Schur and endpoint-cancelled harmonic U bounds. Reproduction `/root/reproduce`, explicitly gpt-6.1-sol medium, completed finite suites. Independent adversarial `/root/adversarial`, explicitly gpt-6-astra xhigh, reconstructs every accepted candidate and actually reran the numerical suite. M0 `/root/literature_baseline`, explicitly gpt-6.1-sol high, completed 43-query screen.
- All imported rigorous statements are locally reproved rather than inherited. Several source implications require correction: An–Wu states a conditional corollary; Padua marginal domination alone does not prove convergence; inverse-Gram stability is not the hyperinterpolation operator norm. The endpoint η rate requires upper-spectrum information beyond λ_max<2−c/N.
- Refresh of origin/main returned d367228. GitHub open-PR query now finds draft #2, `codex/charter-unisolvence-20261031`, head eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64, with its standalone allocation ledger. Those reserved IDs must be preserved in a batch ledger before allocating here. No competing registry had been visible at the earlier initial query. No main merge or charter edits performed.

## 2026-10-31 — Claude, Opus 5.5 xhigh (independent cross-agent auditor)

- Rules read and audited head: `fdf0648cbaa9fb722c611d709e638de7dfe86368`; base `d36722823441dc40c6e19d69a174459348dd309c` equals current `origin/main`.
- Report: [audit-01.md](audit-01.md). Verdict CHANGES REQUESTED, with no High finding.
- Mathematics: every PROVED statement in scope (PD-T013–019, 021–025; PD-N002–006) was reconstructed independently and accepted as stated. The OPEN targets PD-T020/027/028 and the MEASURED record PD-T026 are correctly labelled.
- Medium findings:
  - M1: PD-T022 at n=N−1 gives λ_+≤2−4/N+4/N². That strictly improves PD-T014's headline 2−2/(πN) for every N, and PD-T015's quantitative role is superseded.
  - M2: the screen omitted the mean-convergence-of-Lagrange-interpolation / converse quadrature-sum literature (Askey, Nevai and successors), which is the closest prior-art family for PD-T017/018.
- Low findings: L1 stale conditional in PD-T028; L2 the non-vacuity range of 128000/(log N)², and how the finite tables relate to the log⁻² order; L3 PD-T017 proves the full-space λ_min(CC,N) bound.
- Executed: the developer's M1/M2/M3, reproduction and protocol commands, all matching the committed and Astra outputs exactly. Also the auditor's own checker `tracks/mz-constants/evidence/claude-audit-01-check.py` (exact sign checks to N=60, Padua compression to N=14, and a MEASURED shifted-log fit to N=5120) and a manuscript build (14 pages, no warnings).
- Stage returns to WORK for Codex `response-01.md`. Only AC merges.
