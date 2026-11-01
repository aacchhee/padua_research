# Audit 02 — focused re-audit of response-01 (MZ constants)

- Auditor: Claude, the independent auditor; the Codex developer is a separate agent. Model: Opus 5.5, xhigh effort, as requested in `Claude (Opus 5.5 xhigh): Continue codex/mz-constants-20261031; focused re-audit response-01.md.`
- Date: 2026-10-31.
- Rules were read at the branch head `a27fdafce835a9710fcf2f18560557788c5c9ee4`. `AGENTS.md`, `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` are unchanged since audit-01.
- Candidate: head `a27fdaf`. Current `origin/main` is `08fafe6` (PR #2, the merged charter). It is an ancestor of the head, and `git merge-tree --write-tree origin/main HEAD` is clean.
- Scope. This audit covers the response's own commits `bc85509`, `b56c7d6`, `2cc1918` and `a27fdaf`, against [audit-01](audit-01.md) findings M1, M2, L1–L3 and P1–P7.
  - Mathematical content changed in one place only: the endpoint corollary of PD-T022.
  - Unchanged proofs that audit-01 accepted were not re-derived.
  - The merged charter content was checked for preservation only; it was not re-audited.
  - The supplementary Astra review (`independent-response-01.md`) was not relied on.
- **Verdict: ACCEPTED for the response scope.** No finding blocks readiness. Four Informational notes follow. The stage moves to PR. Only AC merges.

## Checks actually run

Environment: Python 3.12.3, NumPy 2.3.5 and SciPy 1.17.0, in a fresh fetch at `a27fdaf`.

| Check | Command (abridged) | Result |
|---|---|---|
| Response checker, the exact command from the handoff | `python topics/mz-constants/check_response_01.py --require-targets --output <local>` | rc 0. It reports 105 charter files and 54 charter registry rows preserved, 140 response targets and 123 historical targets verified, ledger blob `43c581fb…`, and both propagated member heads. |
| M3 exact checker | `python tracks/mz-constants/code/m3_exact_check.py --max-n 25` | `EXACT: 324 pairs … PASS` |
| Auditor's checker (unchanged) | `python -I tracks/mz-constants/evidence/claude-audit-01-check.py` | E2: 0 violations of the A_ρ sign condition for N≤60. E4: true. |
| Ledger identity on the live branches | `git rev-parse FETCH_HEAD:topics/padua-batch-20261031/ALLOCATIONS.md` for the MZ, programme-ideas and Lanczos branches | All three are blob `43c581fb242fd28ebe4d89ee4a42e3bbd660a159`. Both Claude branches have since advanced to `2554433` and `fba4d2f` with that blob unchanged. |
| Propagation commits | `git show --stat c989031`, `git show --stat 48f7a02`; `merge-base --is-ancestor` | Each is a normal single-parent commit touching only the ledger path, and each is an ancestor of its live branch, so no force push occurred. |
| Charter preservation | `git diff --stat origin/main HEAD -- tracks/unisolvence topics/charter-unisolvence-20261031` | empty |
| Registry preamble and rows | A Python comparison against `d367228:PROOF_STATUS.md` and `origin/main:PROOF_STATUS.md` | All four original policy paragraphs are verbatim; the fifth, the empty-registry line, is correctly gone. The 13 main PD rows are verbatim. No MZ row contains placeholder text. The PD-N rows read IDEA-060/068 `REJECTED: refuted` and IDEA-061/069/070 `REJECTED: failed`, each with a linked PD-N. |
| Idea registry | `grep -n` on `state/IDEAS.md` | There is a current table for IDEA-052…076 (from line 393). The historical seed table is retained under its own label. |
| Manuscript build | the README sequence into the ignored `local-output/mz-constants/paper-r1/` | 15 pages. No LaTeX or BibTeX warnings and no undefined references. The citations LIT-061…065 resolve. |
| Primary source spot check | Smith 1986, Bull. Austral. Math. Soc. (Cambridge Core) | Theorem 1 uses Lobatto nodes (zeros of the ρ-OP plus ±1), continuous f and mean weight w=ρ/(1−x²); the introduction names the CC points. This matches LIT-065's stated limits. |
| Old protocol checker | `python tracks/mz-constants/evidence/protocol-check.py` | Fails at HEAD on its hard-coded `==65` mapping count. See I1. |

Hashes of the key reviewed files (SHA-256 prefixes) at `a27fdaf`:

| File | SHA-256 prefix |
|---|---|
| `response-01.md` | `a5eb3a33d9dcc623` |
| `m3-upper-ratio.md` | `dd8512d6041ecba8` |
| `manuscript.tex` | `c0037cf857895111` |
| `ALLOCATIONS.md` | `39dfc9a9abcffcc7` |
| `PROOF_STATUS.md` | `1b1041f42b03c687` |
| `state/IDEAS.md` | `eeb673d99cce8ed3` |
| `mz-mean-convergence-screen.md` | `58270d1eec08635d` |

## Finding-by-finding disposition

- **M1 — accepted.**
  - The new endpoint corollary (2) in PD-T022 is correct. Substituting n=N−1 gives ρ=(1−2/N)². At N=2 we have 2n=N and ρ=0, and exactness gives λ_+(2,1)=1, so equality holds. For N≥3, PD-T022's strict inequality holds for each nonzero p, and the maximum over the compact unit sphere is attained, so λ_+ is strictly below the bound.
  - Dominance over the old constant follows from 4−4/N≥2>2/π, and it extends to every n<N by monotonicity of ρ in n. So simplifying PD-T025's B to 1+ρ is exact.
  - The manuscript translation is non-circular. Theorem 2.3 forward-references Theorem 4.1, and Theorem 4.1's proof is now self-contained: it no longer says "as in Theorem 2.3". The historical 2−2/(πN) proof is kept as a labelled alternative.
  - Keeping PD-T015 as PROVED and substantive is acceptable. It is an independent inequality with its own proof, and being quantitatively dominated is not a reason to downgrade it. The classification is accepted.
- **M2 — accepted as a named unresolved gap after an actual screen.**
  - Five LIT records (061–065) have source-specific coverage. Mastroianni–Russo and Xu are named as bibliography-level pointers.
  - The comparison criteria are stated precisely: nodal CC-ℓ² to L²(dx), Lobatto endpoints, degree range and the critical logarithm.
  - The manuscript's §1 names the family. "Self-contained proof, novelty unresolved" is the correct wording. The next decisive reading (Nevai III and its 1990 addendum) is named.
- **L1 — accepted.** PD-T028 now states the liminf unconditionally via PD-T021 and PD-T018.
- **L2 — accepted.** The exact threshold log N > √128000 ≈ 357.7709 appears in PD-T018 and in the manuscript, together with the statement that the finite table does not determine the constant. The developer's reason for avoiding "all computable N" is fair.
- **L3 — accepted.** λ_min(CC,N) ≥ 1/K_N is stated, and restriction gives the degree-(N−1) bound, with the inequality direction correct.
- **P1 — accepted.**
  - One ledger, one named owner and AC's stated order (charter first, MZ second).
  - Disjoint blocks; the next free IDs are PD-T029, PD-N007, LIT-066 and IDEA-077.
  - The ledger was actually propagated, with identical bytes on all active members.
- **P2 / P3 — accepted** (verified above).
- **P4 — accepted.**
  - The reciprocal links use IDs.
  - The text distinguishes "separation of a discussion" from "decomposition of a statement", so no false PARTIAL is created.
- **P5 — accepted.** The policy text is restored verbatim, and one ledger authority is named.
- **P6 — accepted.**
  - The pins are refreshed (charter head `317a265`, main `08fafe6`).
  - The historical `eb7bdcd` pin is kept under an explicit key.
  - The branch now contains main, and merge-tree is clean.
- **P7 — accepted.** The PR body will request a squash-merge decision after acceptance.

## Informational notes (no action required for readiness)

- **I1.** `tracks/mz-constants/evidence/protocol-check.py` is the historical `fdf0648` checker and fails at HEAD, because it asserts exactly 65 mappings while there are now 70. The current handoff correctly lists `check_response_01.py` instead. A one-line note in the checker's manifest or README ("historical; valid at fdf0648 only") would stop future readers mistaking the failure for a regression.
- **I2.** `state/IDEAS.md` uses "retained" for IDEA-053/054/055/059/062/063/065/066/073, where WORKFLOW's vocabulary is active/deferred plus REJECTED reasons. The meaning ("successful candidate whose result is registered") is clear. Consider "active (PROVED outcome)" when the registry is next touched.
- **I3.** Codex made ledger-only commits on the two Claude member branches. Audit-01 P1 requested this propagation, and both branches have since built on it without changing the ledger, so the sessions that own those branches have effectively adopted it. Future reservations for those branches must go through the named owner, as the ledger states.
- **I4.** Novelty remains unresolved. That is acceptable for readiness of a development PR, but not for submission. Before any priority wording, the Nevai III and addendum reading named in LIT-063 is the decisive next step.

## Requested next step

Stage: **PR**. Codex records audit-02 in PR #3's AUDIT section, confirms the rehearsal against current main (which is already clean here), marks the PR ready, and asks AC for the squash-merge decision. AC alone decides the merge.
