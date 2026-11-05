# Handoff 01 — padua-lebesgue-followups-20261103 — small follow-ups for the Padua argmax / Lebesgue-function paper

- Status: done in 5b2e36710144d5ab8dd1b8ee9dc2e8b0f1e13033
- Previous handoff: none

- Next agent / model / effort: Codex. Mathematics: gpt-6.1-sol xhigh (ultra only with a written justification in LOG). Code, certification runs and replays: gpt-6.1-sol medium. Supplementary independent checks: gpt-6-astra high.
- Role: orchestrator and developer
- Branch: codex/padua-lebesgue-followups-20261103
- Input head SHA: `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (main, PR #17 merged; this branch adds only this handoff, LOG and results stub)
- Main / base: `440d107`
- Stage: WORK
- Written by / date: Claude, claude-opus-5-5 · 2026-11-03

## Context

AC has divided the remaining Padua Lebesgue work into three pieces:

1. **Effective all-degree argmax.** A separate, parallel campaign, `codex/padua-argmax-effective-20261103`. **Do not work on PD-T099's finite bridge here.**
2. **This topic: four bounded follow-ups.** Each strengthens the planned paper on the Padua Lebesgue function. That paper rests on PD-T101, PD-T156–159, PD-T161–192 and PD-T209–231.
3. **Writing the manuscript.** Later, separately.

Each target is small and precisely stated. Treat each as a bounded attempt with its own time box: stop at its done criterion, at a scoped counterexample, or at the box. Then record what was proved, the exact obstacle, and the next step. Targets may run in parallel subagents with disjoint file ownership. Order of priority: T1, T2, T3, T4.

## Targets

### T1 — certified degree-8 maxima count (PD-T180, PD-T184; IDEA-299 deferred). Box: about 6 h wall.

- **State.**
  - PD-T183 (PROVED): at least 44 strict interior maxima at n = 8.
  - PD-T181 (PROVED): the n = 8 global maximum, through the PD-T210 global-max certifier.
  - The exact count (MEASURED, census: 44 interior / 16 edge / 2 corner = 62) and the exactly-44-interior statement are OPEN.
  - Part 2's A5 n = 8 run stopped at its deadline. The v3 cap after 3600 s had 34127 disposed leaves, 8 pending and 0 unresolved. Prepared but unused tools: a continuation script `a5_n8_continue.py` with independently replayed structural controls, and the x-reflection identities PD-T182 for a half-square strategy. See `topics/padua-proof-attempts-2-20261101/attempts/T-A5-n8.md`.
- **Task.** Finish the n = 8 certification with the existing frozen A5 machinery: the continuation from a fresh complete-interior run, with or without the reflection half-square, plus the boundary. Do not invent new acceptance predicates.
  - The large intermediate trees are regenerable and live in scratch or cold storage.
  - Certify both the interior count (PD-T184) and the closed-square count (PD-T180).
  - Require an independent replay by a different subagent, as for n = 3–7.
  - If runtime is the blocker, a faster exact backend (python-flint or arb) is allowed for the hot loops. It must keep the predicates unchanged and be cross-validated on n = 4–7 against the frozen certificates.
- **Done.** PD-T184 and PD-T180 are PROVED with independent replays. Write the certified comparison with arXiv 2605.23299 Table 3 (n = 8: interior 38, total 56; LIT-388), worded as a certified candidate correction. Make no contact with the authors.

### T2 — centre-minimality of the edge-defect integrals (OPEN). Box: about 4 h.

- **State.**
  - PD-T211 defines g_v(β) = (2/π²)∫₀^π∫₀^π h_β(cos u, b) du db, which is positive and continuous on (0, π), with only the crude bound min_{[δ, π−δ]} g_v ≥ δ²[1−cos(δ/2)]/(16π²).
  - PD-T212/230 give g_h(α) for the horizontal edges, with no numerical evaluation recorded.
  - The value g = g_v(π/2) ≈ 0.548514842 is pinned by PD-T187/188.
  - Measured: the vertical-edge gap is smallest at the centre and rises toward the ends, about 0.87 at 25 % and about 1.4–1.5 at 10 % (PD-T207, PD-T208 T1 to n = 399). The horizontal-edge gap is about 0.95–0.99 near the centre.
- **Task.** Prove:
  - min_{0<β<π} g_v(β) = g_v(π/2) = g, attained only at β = π/2 (or the strongest true variant);
  - the same for g_h, with an explicit certified value of g_h(π/2).
  - Exploit the symmetry β ↦ π − β, monotonicity on (0, π/2], or convexity of the integrand in β, and computer-assisted interval integration where analysis stops (exact or outward arithmetic, committed checker, independent rerun).
  - Also record the behaviour as β → 0⁺ (the measured growth like log near the node end).
- **Done.** A PROVED centre-minimality theorem for g_v and g_h, or a certified counterexample (scoped PD-N), or a precise PARTIAL split (for example, monotone on [β₀, π/2] with certified values below β₀).

### T3 — general-β series for g_v and g_h (OPEN). Box: about 3 h; may share T2's subagent.

- **State.** PD-T188 gives g = g_v(π/2) as (8/π²)∫₀¹(arsinh x + x/(1+√(1+x²))) artanh x dx = (8/π²)Σ(−1)^k a_k J_k, with positive rational a_k, J_k and alternating enclosures. No general-β formula exists.
- **Task.** Derive a one-dimensional integral and a rapidly convergent series (with rigorous truncation bounds) for g_v(β) and g_h(α) at general position. Check it against direct certified quadrature at several β, and against PD-T188 at β = π/2. If T2 succeeds analytically, this may be its by-product.
- **Done.** PROVED formula(s) with computable enclosures, or a precise obstruction.

### T4 — the constant term of the corner expansion (PD-T098 OPEN, the "A3" target). Box: about 5 h.

- **State.** PD-T098 conjectures, with N = n + ½:

  Λ_c(n) = (4/π²) log² N + b log N + c − 1/N + O(log N / N²),

  with b = (8/π²)(γ + log(8/π)) and c independent of the parity of n.
  - Proved: the b-term with |error| ≤ 68 (PD-T158), and |Λ_c − L_n²| ≤ 54 (PD-T159), where L_n = (2/n) Σ_{r odd ≤ n} d_r csc(rπ/2n) is a 1-D Chebyshev-type Lebesgue sum.
  - Measured (post-registration fits only): c ≈ 1.846160310424 within the N = n + ½ model. The question of κ = c − c₁², with c₁ = (2/π)(γ + log(8/π)) the 1-D constant, is open: is there a closed form, or a proof that κ is not a small-height combination of standard constants?
- **Task.**
  1. Prove that the limit κ = lim_{n→∞} (Λ_c(n) − L_n²) exists, separately for even and odd n, and that both limits agree. Give an explicit integral or series for κ with certified enclosure, together with the 1-D expansion of L_n with explicit remainder (classical; cite only after a fulltext check).
  2. Then prove the c-term with an explicit remainder rate. The −1/N term and the O(log N/N²) remainder are stretch goals.
  3. Search for a closed form of κ (integer-relation searches are MEASURED evidence only). If none is found, record that, without a universal claim.
- **Done.** κ (hence c) characterised by a PROVED formula with certified digits and parity independence, or the precise remaining obligation. Do not touch PD-T099.

## Read first

- AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md at the branch head.
- From `topics/padua-proof-attempts-2-20261101/`:
  - attempts/T-A5-n8.md and T-A5*.md;
  - theory 01–04 (PD-T156–159), 60–65 (PD-T179–184) and 70–77 (PD-T185–192);
  - code/a5_n8_*;
  - audit-01.md and response-01.md.
- From `topics/padua-argmax-alln-20261101/`: theory argmax-alln-codex-04/05 (PD-T211/212), gated-codex-16 (PD-T230), PD-T207/208, and report.md.
- `topics/programme-ideas-20261031/theory/programme-ideas-claude-04-padua-corner-expansion.md` (PD-T098) and OPEN_TARGETS A3.
- PROOF_STATUS rows PD-T098–101, PD-T156–235 and PD-N072–083. IDEAS entries IDEA-206, 286–311 and 316–335.
- literature/INDEX.md, including LIT-379 (Kolomoitsev–Lomako; page locators flagged unconfirmed by part 2's audit F6) and LIT-388 (arXiv 2605.23299).

## Scope limits

- Write only inside `topics/padua-lebesgue-followups-20261103/` and `results/padua-lebesgue-followups-20261103.md`.
  - Do not edit merged topic, theory, code or registry files. Frozen A5 sources are imported or copied, never modified.
  - Put proposed shared-record changes as literal old→new blocks in `proposed-record-changes.md`.
  - Do not write to `codex/padua-argmax-effective-20261103`. If a result here would help that campaign, note it in the report; its orchestrator decides.
- Novelty gate (relaxed scan, WORKFLOW) before each target's first mechanism. Record closest entries, applicable obstructions, the verdict and the cheapest test.
- Provisional IDs: `PD-T?lebesgue-followups-codex-NN`, and likewise for PD-N, IDEA and LIT. When the draft PR opens, reserve final ranges by the fresh-range procedure. It must include the open effective-argmax branch and its PR, which runs in parallel and will reserve its own ranges.
- Statuses follow AGENTS.md: floating-point fits and integer-relation searches are MEASURED.
  - Computer-assisted claims need a written reduction, exact or outward arithmetic, committed checker code, small evidence, and an independent rerun by a different subagent.
  - Storage follows WORKFLOW (PR #18): small receipts in Git, regenerable or large outputs to cold storage via `tools/cold_storage.py`.
- Literature: you may open any public page holding relevant literature. Cite a source only after reading its fulltext, and record LIT entries. List unreachable fulltexts for AC with DOI and journal link. Never commit third-party PDFs or extracts (the repo is public).
- Compute only in your sandbox. Ask AC before using NTNU servers or any other machine.
- Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Codex` and `Model: <exact model and effort>`. Never commit to main, merge, force-push, create tags or touch .github/. Only AC merges.

## Acceptance and outputs

- `LOG.md` with an entry per target boundary.
- `plan.md` with time boxes and kill criteria written before each run.
- `attempts/T1…T4.md`, `theory/` records in THEORY-template form, `independent-checks*.md`, `evidence-manifest.json`, `results/padua-lebesgue-followups-20261103.md` (kept current), and `report.md` at the end.
- Push at every target boundary and at least every ~10 minutes while something has changed.
- Open a draft PR to main early, with WORK / AUDIT (PENDING) / PR sections and the ID reservation.
- The report includes a short "for the paper" paragraph per target: what can be stated as a theorem and its exact dependencies.
- When done, commit the outputs. Then, in a following commit, set this status to `done in <sha>` and open handoff 02 for the audit by Claude, Opus 5.5 high or xhigh as the auditor chooses, which reads the complete state/IDEAS.md. Reply to AC only with `Claude (Opus 5.5 xhigh): Continue codex/padua-lebesgue-followups-20261103.`
