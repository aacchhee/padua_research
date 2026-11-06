# Handoff 06 — padua-lanczos-nonproduct-20261105 — PR preparation

- Status: done in 418b8166121d3717c4d1916ae6c4619953cb4573
- Previous handoff: [05-focused-audit.md](05-focused-audit.md)

- Next agent / model / effort: Codex, gpt-6-astra high, coordinator, per AC's 2026-11-05 allocation in handoff 01. Mechanical registry edits may use gpt-6.1-sol medium.
- Role: developer and topic orchestrator (PR preparation)
- Branch: codex/padua-lanczos-nonproduct-20261105
- Input head SHA: `c582791bcb88dcf1afd72c8fe04f5f75fed7d56f` (the audit-02 output commit; the commit that publishes this file comes later)
- Main / base: `be9a8318150204711d5446d2ea26284cf1ed0819`. Fetch main first; if it has moved, merge `origin/main` into the branch and resolve shared-registry conflicts by keeping every topic's content. Never rebase published history.
- Stage: PR
- Written by / date: Claude, claude-opus-5-5 high (configured) · 2026-11-06

## Task

Audit 01 (substantive) and [audit 02](../audit-02.md) (focused, A3) are complete. Every proof in scope is accepted at its stated scope, and AC decided Q1–Q3 on 2026-11-06 (LOG). Prepare the PR:

1. **Fix audit-02 MINOR B1.** At `theory/p3-03-uniform-capacity-radius.md:208`, reword so that |eta|=1 is clearly *outside* the admitted positive full-support family, for example: "so |eta|=1 lies outside the admitted positive full-support family". Wording only.
2. **Reserve final-ID ranges** under WORKFLOW's "Reserve fresh ranges; never reallocate" procedure:
   - **What to scan:** refresh main and every open PR, drafts included. At handoff time these were #27 `codex/padua-argmax-bridge-20261105` and #28 `codex/nn-mop-stability-20261105`; recheck, since others may have opened. Read each branch's ledgers and every final ID it uses in `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`, plus retired reservations and any closed, unmerged PR whose reservation is not yet recorded.
   - **How to size:** compute the maximum per namespace and start above it. Size each range with headroom.
   - **Where to record:** `topics/padua-lanczos-nonproduct-20261105/ALLOCATIONS.md` (namespace, range, count, branch, date, heads checked), linked from `ID_CROSSWALK.md`, and the PR body, in the reserving commit.
3. **Assign final IDs and record mappings.** Preserve every provisional-to-final mapping in `ID_CROSSWALK.md`. Disambiguate the colliding local labels in the crosswalk: PD-T/IDEA/PD-N P4-01, PD-T/IDEA P4-04, P2-03/P2-04, and the lowercase P5 theory labels. Do not renumber anything already accepted.
4. **Edit the shared registries directly**, to be reviewed by diff. They carry claim content, status, dependencies, dispositions and links only; no process stage.
   - **PROOF_STATUS.md, PROVED claims at their exact scopes:**
     - P3-01/02/03, with P3-03 titled "non-affine-product measures moment-equivalent to SH_n through degree 2n+1, with an n-dependent weight mode";
     - P5-01/02;
     - the P4 definition, weighted quotient (with terminal-block corollary), atomless capacity and transfer records;
     - the P1/P2 admissions and P2-02 covariance.
   - **PROOF_STATUS.md, PD-N:** the covariance obstruction, PROVED, with its candidate REJECTED: refuted, and the link in the disposition column.
   - **PROOF_STATUS.md, MEASURED records** at their scopes: the P1-02 probe (chain under BJ), the P2-03 probe, the P6 finite scans and the N2 screen, and the N0 replay if it is registered.
   - **PROOF_STATUS.md, OPEN targets:**
     - the continuous triangle and disk rates;
     - the P4 structural criterion;
     - the sharp Padua exponent and the alternating/pivot uppers;
     - the n-independent perturbation target.

     No supporting lemma upgrades an OPEN target to PARTIAL.
   - **`state/IDEAS.md`:** every candidate with its disposition. These include:
     - the successful P3 weaker variant, with its permanent timing qualifier;
     - the deferred n-independent perturbation, with its resume condition and no proof status;
     - D65 deferred;
     - all abandoned, equivalent and rejected candidates, with their aliases.
   - **`literature/INDEX.md`:** the provisional P1 LIT record or records, as a LITERATURE label only.
   - **`state/CURRENT.md`, if this topic warrants an entry:** content only.
   - **Root `RESULTS.md`:** append or replace only this topic's section, from `results/padua-lanczos-nonproduct-20261105.md`.
5. **Update the records.** Update the LOG, the topic results file and the PR #30 body (WORK/AUDIT/PR). The AUDIT section links audits 01 and 02 and AC's decisions. The PR section lists base/head SHAs, the reservation and heads checked, the registry diff range, and the decision requested from AC. Remove completed preparation tasks from any shared frontier.

## Read first

- AGENTS.md, agents/WORKFLOW.md (Work cycle step 5; Audit and PR records; reservation procedure; Proportionate audit and records) and agents/codex/CODEX.md at the branch head.
- [audit-01.md](../audit-01.md), [response-01.md](../response-01.md), [audit-02.md](../audit-02.md), and the LOG entries for AC's decisions.
- [Handoff 05](05-focused-audit.md), section "Readiness inputs for subsequent preparation".

## Scope limits

- **Do not reopen:** accepted proofs, the reflection method, the P6 outcomes, the N2 verdicts, AC's Q1–Q3 decisions, or the storage decision. Storage is a separate cleanup topic; take no cleaning action while the repository stays under 10 MB.
- **Materiality:** any change to a claim's statement, scope, status or evidence beyond the audited content is material and must be listed for focused review. Registry application of the audited content is not material.
- **Authority:** no rule or `.github/` changes, no force-push, no tags, no merge. Keep the PR as a draft until the readiness check passes. Only AC merges.

## Acceptance and outputs

- Registry edits, reservation ledger, crosswalk and results are committed.
- The PR body is updated.
- The LOG records the reservation commit and heads checked.

Commit the preparation outputs first. In a following commit, set this handoff's status to `done in <preparation-output-sha>` and add handoff 07: Claude, Opus 5.5 high, readiness check. That check reviews the registry `git diff` against base and refreshes the reservation scan against the then-current main and open PRs; it is not a further substantive audit. List any material change explicitly. Push, then reply with the short continuation prompt.
