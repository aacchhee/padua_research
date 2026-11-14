# Handoff 06 — respond to the MZ manuscript audit and prepare the PR

- Status: done in 06e544dc9361de3a8c7e7495b43cb6603880b63e
- Previous handoff: [05-audit.md](05-audit.md), done in the output commit below.
- Next agent / model / effort: **Claude, Opus 5.5 xhigh**, orchestrator and manuscript developer. Sonnet 5.5 high may perform bounded LaTeX/record mechanics; Sonnet 5.5 medium for small mechanical edits. Use the repository's available-model policy and record actual metadata.
- Branch: `claude/padua-mz-paper-20261113` · Draft PR #35.
- Input head SHA: `f9bf997447922645bba9f411d470e0d1ec4d82ce` (audit outputs; this handoff is published later).
- Main/base at audit: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`.
- Stage: WORK (audit response), then PR preparation/readiness as permitted below.
- Written by/date: Codex, gpt-6-astra high · 2026-11-14.

## Read first

AGENTS.md, agents/WORKFLOW.md and your role at the current branch head; LOG; [audit-01.md](../audit-01.md) and its linked audit-support coverage/rerun records; the two provisional theory records; both correspondence maps; report.md §§5–6; the previous plans/internal responses only as needed to preserve already decided scope. AC's venue, publication-order, deposit and companion decisions in BRIEF remain binding.

## Task

1. Write `topics/padua-mz-paper-20261113/response-01.md`, answering **F1–F5 individually** with locations and exact dispositions. Do not edit audit-01 or its supplementary reports. The independent audit found no unsupported analytic theorem and reconstructed both new consequence proofs successfully.
2. Repair the actual draft:
   - **F1 (MAJOR):** correct both manuscripts' present-tense archive/deposit/README assertions and their README assurances. Separate committed code/small receipts from missing witness inputs and a planned future Zenodo deposit. No deposit exists, no witness delivery was verified, and no archive README was found. Retain honest missing-package identities in report §6.2. Agents create no deposit.
   - The exact PD-T376 arrays/norms could not be replayed. Do not count receipt inspection as retrieval or replay. Before claiming accessible complete witness evidence at submission, retrieve the exact package and replay its committed checkers, or explicitly resolve the affected publication scope. Do not silently replace it with a newly generated witness or convert a source theorem to a measured statement. Record any unresolved availability issue plainly in the response/PR and handoff; proceed with unaffected corrections/preparation. The audit does not require inventing a delivery or reopening the accepted analytic theorem.
   - **F2 (MAJOR in the root report, with the subreviewer disagreement preserved):** remove or qualify the m=1600 parenthesis in SP §8.3. The *computed* minimum agrees with the certified trial quotient at printed precision; Prop 8.2 supplies no lower endpoint for the true minimum. Keep both the measured-only disclaimer and the explicit trial/eigenvalue distinction. No new eigensolve is needed.
   - **F3:** change the raw signed-energy supremum sentence to magnitudes, or state the negative infimum/positive supremum correctly. The substantive normalized bounds stay intact.
   - **F4:** correct the listed J/upsilon/N_Z/mathcal E_K notation remnants without changing bounds.
   - **F5:** label opening correspondence planning tables historical or refresh their current mapping, and reconcile stale independent-check-pending metadata in the provisional records. Do not rewrite historical handoff bodies or reports.
3. Clean-build both papers and verify frozen statement labels after the changes. Use `tools/build.sh`; required packages include `texlive-publishers`, `texlive-science`, scalable EC fonts (`cm-super`). Expected 32/50 pages, 52/56 frozen non-cref labels before wording changes. A page-count shift caused by wording is not itself a defect; preserve statement numbers or explicitly record any unavoidable change. Do not commit PDFs/build outputs. No reason exists to repeat unchanged exact certificates merely for wording fixes.
4. Prepare PR #35 after the response:
   - Refresh main/topic and reconcile without rewriting published history. Do not touch other open branches.
   - Reserve fresh final-ID ranges for the two provisional claims using WORKFLOW's full union of current main, every open PR/draft and retired allocations. No range has yet been reserved for this topic. Preserve all existing allocations. Record provisional-to-final mappings and update TeX comments and shared registries only at this preparation step.
   - Apply the reviewed final scope directly to PROOF_STATUS, PAPER_MAP, state/CURRENT.md, ID_CROSSWALK and the topic's RESULTS section as required; canonical LIT-045 and LIT-056 addenda remain to apply from the documented readings. Do not invent source reread provenance. Remove stale initialization tasks from the shared frontier as appropriate.
   - Update current LOG/results/report/PR metadata. Do not infer that an audited proof resolves missing witness delivery or AC-reserved submission metadata.
5. Obtain the proportionate readiness check. The audit asks for a diff-based check of wording/metadata corrections within the already stated scopes, plus the normal registry/final-ID/reservation verification. If the response actually changes a theorem, assumption, proof, status, bound, evidence or another material item, request a **focused** Codex re-audit of that item under WORKFLOW; do not repeat the full manuscript/registry audit without a concrete reason. Preserve unresolved disagreements for AC. Remain draft/unready while major findings or material evidence obligations are unresolved.

## Scope limits

Assigned writes: this topic directory, `results/padua-mz-paper-20261113.md`, both paper directories, and the M7 manuscript record append; shared files only during PR preparation. Audit reports are immutable to development. No new 23/15 bound, fixed-ratio Theta(log m) result or other declined strengthening as an editorial fix. Keep the existing theorem scopes and exact identities. Do not modify `.github/`, settings, `main`, other branches, tags or published history. Commits remain authored by Andrey Chesnokov <aacchhee@gmail.com>, with Agent/Model trailers. Only AC merges.

Companions remain separate future Claude work after AC confirms the frozen texts, under BRIEF §5 item 3. This response does not authorize submission, public posting, deposits or changes to AC-reserved author/AI/funding/ORCID material.

## Acceptance and outputs

- A response for every F1–F5 finding; honest evidence-availability disposition.
- Corrected manuscripts/metadata, clean builds and frozen-number check, with no silent mathematical change.
- Final-ID reservation and reviewed registry application when preparation is reached; updated draft PR with WORK/AUDIT/PR sections and explicit unresolved items.
- A bounded readiness request or focused re-audit instruction at the exact candidate head; no repeated full audit without material justification.
- Commit and push outputs to this branch. When passing to the next agent/session, close this handoff in a **following** commit using the actual output SHA and add the next numbered handoff. Leave exactly one open handoff while work remains. End with the short continuation prompt for that next agent/model; only AC merges.
