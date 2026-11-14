# Handoff 02 — padua-xu-lebesgue-20261114 — Opus 5.5 xhigh audit of session 1 (X1 resolved; X2 vertex theory and partial argmax)

- Status: open
- Previous handoff: [01-work.md](01-work.md) (done; see its status line)

- Next agent / model / effort: **Claude, Opus 5.5, xhigh**, in a **fresh thread that did not develop this work** (AC ruling 2026-11-14, in place of the default Codex audit; see LOG). The developer was this topic's orchestrator (Opus 5.5) with Fable 5.2 xhigh research subagents and Sonnet 5.5 code subagents. The pre-audit independent subagent checks (Opus 5.5) are supplementary; they do not replace this audit.
- Role: independent auditor. The auditor may delegate bounded reruns to subagents; Git operations stay with the auditor thread.
- Branch: `claude/padua-xu-lebesgue-20261114`, draft [PR #36](https://github.com/aacchhee/padua_research/pull/36)
- Input head SHA: `971beb79b8edb93835b20d1b9148e93d4ba3aba4` (the commit that publishes this file comes later)
- Main / base: `99a9b1d` (recheck `origin/main` at start)
- Stage: AUDIT
- Written by / date: Claude, claude-opus-5-5 (orchestrator) · 2026-11-14

## Task

Run the single substantive audit of every claim of session 1 and write `topics/padua-xu-lebesgue-20261114/audit-01.md`. Follow AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md ("Independent audit"). Novelty claims are present, so read the complete `state/IDEAS.md` and the novelty gates.

### Claims (provisional IDs `PD-T?padua-xu-lebesgue-20261114-claude-NN`, `PD-N?…`)

| NN | Record (`theory/`) | Claimed status | Audit focus |
|---|---|---|---|
| 01 | X1-01-tensor-lift.md | PROVED | Fibers and orbits of Γ, the count 2^{3−β}, the symmetrized interpolant lies in V_n with the right σ, unisolvence (independent check F7: implicit surjectivity) |
| 02 | X1-02-trig-lebesgue-function.md | PROVED | 1-D maximum and equality case (classical facts re-proved; attribution) |
| 03 | X1-03-vertex-value.md | PROVED | Signs of every ℓ_ξ(v); λ_n(v) = L_n², both parities |
| 04 | X1-04-exact-lebesgue-constant.md | PROVED | Identity λ = ω(u)ω(v) − Δ and Δ ≥ 0; coverage of Q by (u, v); **headline Λ^Xu_n = L_n²** |
| 05 | X1-05-argmax-set.md | PROVED | Equality case: only V* survives, for every n ≥ 2 and both parities (Steps 2–3) |
| 06 | X1-06-chebyshev-constant-expansion.md | PROVED | Series (1) and the two-sided n⁻⁴ enclosure; dependency on PD-T269 eq. (9) |
| 07 | X1-07-expansion-and-conjecture-17.md | PROVED | Constants b, c, the remainder, and (d) the verdict on Conj. (17), with "≲" read as asymptotic (page image: BCDMV p. 319); (e) relation to the Padua value |
| 08 | X1-08-edge-deficit-measured.md | MEASURED | Labelling only |
| 21 | X2-21-corner-kernel.md | PROVED | Self-contained Lagrange property; corner kernel (re-derives Beberok eq. (2) without inheriting it) |
| 22 | X2-22-lower-vertices.md | PROVED | λ_n(±1,−1) = n+1 via (−1)^{m+1} = U_n(x_m) |
| 23 | X2-23-upper-vertex-closed-form.md | PROVED | Closed form and sign band B; (f) cites a cyclotomic fact from memory (Washington locator unchecked) |
| 24 | X2-24-upper-exceeds-lower.md | PROVED | |
| 25 | X2-25-upper-vertex-asymptotics.md | PROVED (computer-assisted c* enclosure) | Definition of c*, Steps A–E constants (thin margins, e.g. T₂), the enclosure; evidence `evidence/mp-x2-corner-arb.json` |
| 26 | X2-26-explicit-lower-bound.md | PROVED (ball arithmetic for n ≤ 16) | Analytic part for n ≥ 18; "strengthening of Beberok 2025" wording; Beberok's constant ≈ 7.5e−4 rests on the orchestrator's transcription (m3) |
| 27 | X2-27-vertex-remainder-measured.md | MEASURED | Labelling |
| 28 | X2-28-argmax-open.md (+ round-3 addendum) | OPEN | Honest OPEN; measured D_x, D_y claims (m4) |
| N29 | X2-N29-no-central-symmetry.md | PROVED negative; BBDM §7.1 symmetry and all-corner statements REJECTED: refuted | Scope of the negative statement |
| N30 | X2-N30-vertex-value-not-dimension.md | PROVED negative (ball arithmetic for n ≤ 40) | Scope; analytic for n ≥ 42 |
| 31 | X2-31-first-variation-closed-form.md | PROVED | Closed-form derivatives N_x, N_y; D_x, D_y > 0 ⇒ strict local maximum |
| 32 | X2-32-local-max-certified.md | PROVED (computer-assisted, every even n ≤ 3000) | **Independent rerun required (G3)**: the finite reduction, arb certificates, and a separate code path. Evidence summary `evidence/mp-x2r3-first-variation.json`; the full output is regenerable with the command recorded there (~106 s) |
| 33 | X2-33-far-field-bound.md | PROVED | Step 2 lattice-sum lemma and Step 4 (the researcher flags these as the hardest) |
| 34 | X2-34-translation-formula.md | PROVED (tool) | |
| N35 | X2-N35-shift-rigidity-fails.md | MEASURED negative | PD-N eligibility: a measured scoped mechanism failure |

### Also audit

- **Literature and novelty.** Check the `literature-xu-mp.md` §§3–5 verdicts, `novelty-gate-X1.md`, `novelty-gate-X2.md` and `lit-notes/` against inspectable sources.
  - The "not found" claim for Λ^Xu_n = L_n² is the most consequential. Coverage limits:
    - the body of Xu's CUP 2025 book was not read;
    - Szili–Vértesi 2009 was not read;
    - Della Vecchia–Mastroianni–Vértesi 2009 was read as an abstract only;
    - the arXiv papers were read through WebFetch digests.
  - Fulltexts are in AC's `Downloads\padua\papers` (BdMV 2006, BCDMV 2006, Xu 1996, BBDM 2026) when that folder is reachable. Otherwise use open copies.
- **Gates.** Check G0–G5 and their verdicts in `gates.md`. Do G0 and G1 hold as pre-registered (the X1 G1 superseded by X1-05)?
- **Independent checks already done.** Read `independent-checks-X1.md` and `independent-checks-X2.md`. They do not cover X2-31…N35, so X2-32 needs a fresh independent rerun.
- **Evidence hygiene.** File sizes (normally < 16 KiB) and hashes, AGPL-3.0-or-later applicability, and that no PDFs or extracts are committed.

### Reruns expected

Run with actual execution and record commands and outputs:
- `python3 code/xu/g0_check.py --nmax 12`;
- `python3 code/mp/g0_check.py`;
- `python3 code/mp/cmp_check.py`;
- `python3 code/mp/research/x2_corner_arb.py --nmax 60 --out /tmp/a/arb.json` (compare with the committed JSON);
- `python3 code/mp/research/x2r3_first_variation_arb.py --band --nmin 2 --nmax 3000 --out /tmp/a/fv.json` (compare its hash and flags with `evidence/mp-x2r3-first-variation.json`);
- an independent re-implementation, on a separate code path, of at least the X2-32 band sums for a spread of n up to 3000;
- the independent check scripts in `code/xu/independent/` and `code/mp/independent/`.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md at the branch head; record the SHA.
- The topic's BRIEF.md, LOG.md, rounds.md, gates.md, literature-xu-mp.md, novelty-gate-X1.md, novelty-gate-X2.md, report.md, independent-checks-X1.md, independent-checks-X2.md, attempts/X1-round2.md, attempts/X2-round2.md, attempts/X2-round3.md, and every `theory/` record listed above.
- `results/padua-xu-lebesgue-20261114.md`.
- The merged dependencies used as lemmas: PD-T159, PD-T269, PD-T270 (`PROOF_STATUS.md` links).

## Scope limits

- Do not develop new mathematics. Do not reopen the AC decisions recorded in the LOG: the model allocation, the Claude auditor, and the dropped MPX target.
- The X2 argmax (X2-28) stays OPEN. Its continuation (P1 tail; W1–W3) is a later development step, not part of this audit.
- Fix MINOR findings in place only from the third audit round onward (WORKFLOW). In this first round, report them.
- Never edit developer records to resolve a disagreement; preserve it for AC. Write only `audit-01.md`, your own rerun scripts (e.g. `code/audit/`) and small evidence. Then, in a following commit, change this handoff's status line and add handoff 03.
- No commits to main, merges, force-pushes, tags, or edits under `.github/`. Only AC merges. Commits are authored as Andrey Chesnokov <aacchhee@gmail.com>, with trailers `Agent: Claude`, `Model: claude-opus-5-5 xhigh`, and the session lines.

## Acceptance and outputs

- `audit-01.md` contains:
  - the auditor's identity, model and effort;
  - the audited SHA, `971beb7…`, plus any later head inspected;
  - the files read, with their novelty scope;
  - the reruns, with commands and observed results;
  - findings by severity (BLOCKING / MAJOR / MINOR / NOTE) with locators;
  - a per-claim verdict;
  - remaining uncertainty.
- Update the PR #36 AUDIT section with a summary.
- Set the LOG stage: **PR** if the audit is accepted with at most MINOR findings, otherwise **WORK**.
- Then, in a following commit:
  1. set this handoff's status to `done in <audit-commit-sha>`;
  2. add handoff 03. On findings that is the developer response, with Claude as orchestrator: Opus 5.5 for the response; Fable 5.2 xhigh only for genuinely hard repairs. On acceptance it is PR preparation: final-ID reservation by the WORKFLOW procedure, registry edits, and the readiness check.
  3. Reply to AC with the short Continue prompt only.
