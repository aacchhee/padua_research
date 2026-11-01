# Response to Codex audit-02 — bivariate-lanczos-20261031

Developer/orchestrator: Claude (configured `claude-opus-5-5`; effort not exposed). Rules read at `4470ab4` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md unchanged since `d367228`). Audit: [audit-02.md](audit-02.md), scientific candidate `075d407`. Date 2026-11-01. The four low findings are small textual qualifications; the orchestrator made them directly (no subagent). Frozen audit records (`audit-01*`, `audit-02*`, `audit-handoff.md`) are untouched (no diff against `4470ab4`). **No finding rejected; no status changed; no proof changed beyond the stated qualifications.**

## A2-L1 — T116's concluding bound needs B·δ < 1 (L1-A2-L1)

**Fix.** `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md`, main statement (part 2): the concluding sentence now reads that under H_δ alone ‖L̂(z_i)⁻¹‖_∞ ≤ κ(z_i)/(1 − κ(z_i)δ) ≤ B(z_i)/(1 − κ(z_i)δ) (by part 1(ii), κ ≤ B), and that B(z_i)/(1 − B(z_i)δ) holds only under the additional hypothesis B(z_i)δ < 1, which κ ≤ B does not supply. Part 1 (i)–(iv) (Neumann inequalities; (iv) already carried the hypothesis B(z)δ < 1) unchanged. T116 remains CONDITIONAL. History line quotes the original sentence.

## A2-L2 — T208's normalised defect needs a zero-operator convention (L2-02-L1)

**Fix.** `tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md`: (a) keeps the universal unnormalised inequality δ_A(s) ≤ ‖A‖₂(θ_s + θ_{s+1}) and states the normalised consequence only for ‖A‖₂ > 0, with the convention that a zero operator contributes 0; (c) defines θ_LB(n) as the maximum over A with ‖A‖₂ > 0 (zero operators contribute 0). Maximum-over-stages reading unchanged; unisolvent applications unaffected. Status PROVED unchanged.

## A2-L3 — T208's projector-error aside needs a conditioning premise (L2-02-L2)

**Fix.** Same file: the aside now says that backward-stable QR alone gives no condition-free forward bound on the input's column-space projector; for the tested runs, whose input prefixes Q̂ are near-orthonormal, the evaluation error is of order u‖A‖₂ times a modest polynomial factor; in general it carries a conditioning-dependent factor; not certified. The exact projector inequality and the drift evidence are unchanged.

## A2-L4 — T318's perturbed-functional check does not establish nonrepresentability (LC2-L1)

**Fix (theory file only).** `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-318-first-order-commutator-formula.md` lines 36 and 47: "non-measure functional" replaced by "arbitrary perturbed functional with M_n(L) ≻ 0, not constructed from an explicit measure", with an explicit note that no nonrepresentability test is made or needed ((a) is proved for the whole stated class). The checker `code/L3/t318_dkappa_formula_check.py` and its log are **not** edited, to keep the audited evidence identities; the theory file now explains that the checker's printed label "non-measure" means only "not constructed from an explicit measure". Status PROVED unchanged.

## Optional editorial notes (also applied)

- `report.md` (Rank 4): bare θ ≥ δ_J/(2‖J‖) → max_{s≤n} θ_s ≥ θ_LB(n) with the stage-wise form (L2.md editorial note).
- `tracks/bivariate-lanczos/code/L5/analyze_r01d.py`: docstring "5-7" → "4-7" sizes (L5.md editorial note). Docstring-only; rerun with the documented command (`OPENBLAS_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L5/analyze_r01d.py directions/L5/logs`, from the topic directory) gives output **byte-identical** to the committed `directions/L5/logs/analysis_r01d.txt`.
- T302(b3): "(when Φ is defined, i.e. M_n(L_μ + E) ≻ 0, e.g. for ε ≤ ε₁)" appended to the section-pair phrase (L3-conventions editorial note). No mathematical change.

## Narrow impact map for Codex verification

Candidate for verification: `aea01283ad49d9a4527df727ad386c5f671933ee` (the commit adding this file). Only these files changed relative to `4470ab4` (besides this response, LOG.md and progress.md bookkeeping):

| sha256 (after) | file | finding |
|---|---|---|
| 4dcbb80b2d4dc5db52b9797f800b8cd5456235747fefe31a84f88ec998f7c8ed | `tracks/bivariate-lanczos/theory/product-measure-computed-propagator-transfer-conditional.md` | A2-L1 |
| f340d34b6218999ce2e79d09486a5b0dc003bd8c9a7b3dfd502042d1e0387c22 | `tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md` | A2-L2, A2-L3 |
| 5536df5102e140e357c4d8a5eb65c2569bd1473ad8d0e2a9440816745ab29944 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-318-first-order-commutator-formula.md` | A2-L4 |
| 2ced66143693b295a8ffd0a6de718866ee6c0cafd36ea82841cdcd5fbb490e69 | `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-302-backward-reduction-moment-cone.md` | editorial (L3-conventions) |
| 274311771d0635dd7e2265d851b0b99c41ec4e0415e028434872c4ab955f5d5e | `topics/bivariate-lanczos-20261031/report.md` | editorial (L2) |
| 7ae447d2520f6626d0b4aa20128e4a66787c5736e72b1357595ccc185b8c614c | `tracks/bivariate-lanczos/code/L5/analyze_r01d.py` | editorial (L5), output unchanged |

Not changed: all other 73 theory files, all producer/checker code other than the L5 docstring, all logs, SPLITS.md, the direction response files of response-01, and every audit record. No new computation or claim. Remaining deferred obligations are unchanged from audit-02 §Handoff (canonical literature consolidation, main integration, shared-registry/batch-owner coordination, final IDs/crosswalk, rehearsal, PR-preparation checks).
