# padua-mz-paper-20261113 — finalizing the MZ papers (MZ-CC, MZ-SP)

This file is written only by the topic orchestrator. Branch `claude/padua-mz-paper-20261113`; draft PR #35.

## Status (2026-11-14): WORK, draft PR #35; both papers complete internal drafts, Codex audit pending

Target: split *Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness* (AC, 2026-11-13) into two submission-ready manuscripts for AC's decision:

- **MZ-CC:** Clenshaw–Curtis, with the sharp endpoint constants;
- **MZ-SP:** signed Padua, beyond half-exactness.

MZ-CC comes first. The work:

- integrate PR #31's sharp results: lim (log N)²λ_min = π⁴/8; λ_max ≤ 5/3 for all N; the CC upper limit as an endpoint-operator norm; the signed Padua log limits as inf/sup spectrum of a compact corner operator;
- restructure around them;
- finish the literature after PR #21;
- meet AC's manuscript criteria.

Plan: [BRIEF](../topics/padua-mz-paper-20261113/BRIEF.md) and [handoff 01](../topics/padua-mz-paper-20261113/handoffs/01-work.md).

## Results so far (current, 2026-11-14)

Manuscript state at head `a0206a8` (later wording cleanup at `a03a4f7`); independent audit at `be28d3267bf6117878190b10f2d29840e524eac7`. Details: [audit-01](../topics/padua-mz-paper-20261113/audit-01.md), [report for AC](../topics/padua-mz-paper-20261113/report.md), [LOG](../topics/padua-mz-paper-20261113/LOG.md), scope tables in the two READMEs.

- **Codex audit complete; response required.** Two MAJOR groups (unsupported archival availability; measured minimum versus certified trial interval) and three MINOR groups. No unsupported analytic theorem found; both provisional consequence proofs pass. Fresh exact certificate reruns and all six moderate-degree brackets pass; both papers rebuild cleanly at 32/50 pp. and all 52/56 frozen labels match. No PD-T376 byte-pinned witness replay: exact inputs remain unavailable. Draft PR #35 remains unready; no final IDs or shared registries were changed by the auditor.

- **Both papers are complete internal drafts**, each after two internal referee rounds (mathematics: no CRITICAL or MAJOR finding, certificates rerun bit-identically; exposition) with responses ([CC](../topics/padua-mz-paper-20261113/response-internal-cc.md), [SP](../topics/padua-mz-paper-20261113/response-internal-sp.md)). Statement numbering is **frozen** in correspondence-cc.md and correspondence-sp.md (verified against the compiled `.aux`, 52 and 56 labels). Fresh clean builds: MZ-CC 32 pp. (`siamart251216`), MZ-SP 50 pp. (`elsarticle`); hashes in the [M7 manuscript record](../topics/mz-constants/directions/M7/manuscript-record.md). No PDF in Git. Not submitted.
  - **MZ-CC** ([README](../tracks/mz-constants/paper/README.md)), SIAM J. Numer. Anal.: PROVED uniform λ₊ ≤ 5/3 (PD-T526); lim (log N)²λ₋(N,N−1) = π⁴/8 (PD-T546/523/522/544/545, closes PD-T020); lim λ₊(N,N−1) = Λ_edge ∈ [1, 3/2] (PD-T530, PD-T529 weakened); Λ_edge ≥ 1.0044369, computer-assisted and one-sided (PD-T547/548); PD-T527 and PD-T013–T019, T022–T025 at their scopes. PD-T531 omitted. Open: decimal of Λ_edge (PD-T027 decimal conjunct), rates, operator identification. MEASURED: Table 1 (PD-T026), J-Galerkin proxy (PD-T532).
  - **MZ-SP** ([README](../tracks/mz-constants/paper-sp/README.md)), J. Approx. Theory: PROVED marginal compression (PD-T021), weight asymptotics (PD-T295/T377), carriers and the sharp ratio threshold (PD-N105–107, PD-T378), normalized bounds (PD-T379, T533, T537), corner-operator limits (PD-T534/535/536, T539, T540), uniform coefficient norm (PD-T297), PD-N051; computer-assisted: ‖B‖ enclosure (PD-T541/542), brackets m = 10…80 (PD-T107/298/299), negative witnesses m = 1101/1240/1600 (PD-T376, no first crossing). Open: decimals of c_± (PD-T381 decimal conjunct), first sign change, effective onsets. MEASURED: PD-T026, PD-T538, PD-T543.
- **Provisional claims** (final IDs not yet reserved), each PROVED by the developer with independent checks and Codex mathematical reconstruction PASS; whole-manuscript findings remain to answer:
  - PD-T?mz-paper-claude-01 ([record](../topics/padua-mz-paper-20261113/theory/cc-defect-condition-corollary.md)): 1−η_N = λ₋ for N ≥ 57, (log N)²(1−η_N) → π⁴/8, κ₂/(log N)² → 8Λ_edge/π⁴, ‖𝓘_N‖/log N → 2√2/π², hyperinterpolation factor (1+√(5/3))√2. In MZ-CC.
  - PD-T?mz-paper-claude-02 ([record](../topics/padua-mz-paper-20261113/theory/sp-corner-norm-lower.md)): ‖B‖ ≥ 0.02964…, c₊ ≥ 0.01277…. In MZ-SP.
- **Also reconstructed in the audit:** PD-T523 proof-route change; MZ-CC Lemma 2.4; weakened PD-T529 and PD-T539; the (2+C_P)E_k(f) bound and "η < 0.83" in MZ-SP. No substantive finding on those items.
- **Declined strengthenings (candidates only):** sup λ₊(N,N−1) ≤ 23/15 (MZ-CC); |λ^P_±(m,⌊τm⌋)| ≍ log m (MZ-SP).
- **Deposit:** AC creates the Zenodo deposit; the file list with hashes is in report.md §6. The PD-T376 witness arrays and exact-norm files are not yet delivered to cold storage.
- **Decisions and placeholders for AC:** report.md §5 (placeholders, unread sources with links, DOI checks, arXiv order MZ-CC then MZ-SP).

## History: results at 2026-11-13 (superseded by the section above, kept)

### Results so far (2026-11-13, as written then)

- Split done (gate W0 PASS): MZ-CC → SIAM J. Numer. Anal. (`siamart251216`); MZ-SP → J. Approx. Theory (`elsarticle`). [split-map](../topics/padua-mz-paper-20261113/split-map.md).
- MZ-CC now contains, with full proofs at their record scopes:
  - the uniform bound λ_max ≤ 5/3 (PD-T526);
  - the sharp limit (log N)²λ_min → π⁴/8 with its finite bound (PD-T546, PD-T523, PD-T522/544/545; Appendix A);
  - λ_max → Λ_edge ∈ [1,3/2] (PD-T530, PD-T529 weakened; Appendix B).
  Since handoff 03, MZ-CC is complete to draft (30 siamart pp.): it also has the certified Λ_edge ≥ 1.0044369 (Appendix C), the interpolation-norm and defect/condition corollaries, and a new title, abstract, introduction, §9 and availability statement. Still to do: the notation pass, the literature scope check and the internal referee round.
- New provisional claim PD-T?mz-paper-claude-01 ([record](../topics/padua-mz-paper-20261113/theory/cc-defect-condition-corollary.md)), PROVED by the developer:
  - 1−η_N = λ_min(G_{N,N−1}) for every N ≥ 57, and (log N)²(1−η_N) → π⁴/8;
  - κ₂(G_N)/(log N)² → 8Λ_edge/π⁴;
  - ‖𝓘_N‖_{ℓ²_w→L²}/log N → 2√2/π²;
  - CC hyperinterpolation factor (1+√(5/3))√2.
  Independent checks passed for (a)–(d). Codex audit pending.
- New provisional claim PD-T?mz-paper-claude-02 ([record](../topics/padua-mz-paper-20261113/theory/sp-corner-norm-lower.md)): ‖B‖ = −c₋ ≥ c_new = 0.02964… and c₊ ≥ 0.01277…, both analytic, for MZ-SP. Independent check PASS; Codex audit pending.
- MZ-SP: post-split text in `elsarticle`; integration not started.

## Next step

`Claude (Opus 5.5 xhigh): Continue claude/padua-mz-paper-20261113.`
