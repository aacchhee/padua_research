# Handoff 02 — padua-mz-cleanup-20261105 — independent mathematical and computational audit

- Status: open
- Previous handoff: 01-work.md
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: independent auditor and topic orchestrator for this step
- Branch: codex/padua-mz-cleanup-20261105
- Input head SHA: `10898ad99882248e5e6f9d76641624146af97454`
- Main / base: `aff30e8ad5542c94fab642ae024dc9aab4fa7ad7` (original base21dbfc9; merged without conflicts)
- Stage: AUDIT
- Written by / date: Codex, gpt-6.1-sol xhigh · 2026-11-05

## Task

Audit the completed cleanup development candidate, not its own acceptance.
The required Claude audit has not yet occurred. The PR remains draft:
[PR26](https://github.com/aacchhee/padua_research/pull/26).

1. Reconstruct C1's computer-assisted finite theorem at m1101,1240,1600.
   Check degree/norm/positive-direction reduction, the exact signed kernel
   including the exceptional mode, outward table predicates, integer
   contractions and global energy-error bound. Inspect the independently
   implemented forward-error path and its explicit IEEE/BLAS assumption.
   Verify both paths imply the rational trial-Rayleigh brackets, rather
   than eigenvalue brackets. Default printed checker intervals lose digits:
   reconstruct q_center +/- q_absolute_error and divide the saved exact
   norm to check the tighter rational brackets. The supplementary finite
   report gives the executed procedure and all identities.
2. Reconstruct C2's odd-m fixed-node logarithmic weight limit and whole-grid
   majorant, then the y-mesh carriers with their total-degree budget.
   Check all-integer endpoint/fixed-ratio divergence, and preserve exact
   identity for theta<=1/2. Neither corner negativity alone nor an axis
   swap of the signed cardinal formula suffices.
3. Reconstruct C3's continuous carrier norm limits and the cosine-transform
   identity, including the boundary-parameter supremum argument. The
   proved normalized one-sided constants are approximately0.02962182360
   and0.01277888644. Raw1/9 and1/36 optimize unnormalized energy and
   are not sharp spectral coefficients. Sharp limits remain OPEN.
4. Check all23 MEASURED rows and the fixed K2 diagnostic. The measured
   even crossing is1238–1240;1240 is the smallest even degree certified
   **in this campaign**, not a proof of globally earliest negativity.
   Six odd probes are negative; no odd first crossing is located.
   Historical and higher fitted slopes are-0.091530043047304 and
   -0.09212159619973995. Their movement toward raw-1/9 proves no limit.
5. Audit manuscript translation, especially its all-m statements, distinct
   trial quotients/eigenvalues, normalization, proof scopes and open items.
   The final source builds to25 A4 pages, no provisional IDs or unmerged
   PR21 citations, unchanged bibliography, preserved earlier PDFs untouched.
6. Check small evidence/source inventories, artifact identities, pending
   delivery language and literal shared-file proposals. Final IDs are
   still provisional; no shared registry application is authorized at
   this audit. Permanent reservation is T376–391/N138–145/IDEA466–489,
   no LIT, first publication ee49035. Recheck ranges before later preparation.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md and template
  HANDOFF.md at the candidate; LOG.md and handoff01 (its body unchanged).
- report.md, results/padua-mz-cleanup-20261105.md, plan.md, gates.md,
  attempts/C1–C6.md, all five theory files, novelty-gate-math.md.
- The complete current state/IDEAS.md, every obstruction/disposition table,
  closest IDEA210–227/384–397 records and their relevant full proofs.
  C2/C3 introduce gated variants, so a no-novelty full-read exemption does
  not apply. No historical priority claim or new literature source is made.
- Frozen definitions, PD-T101/106/111/295/297, PD-N105/106/107 and the
  exact source dependencies cited by the new records. Read their proofs
  to the degree required to audit the new changes; do not reopen accepted
  unrelated research.
- code/rigorous_witness.py, independent_witness.py, independent_odd_check.py,
  g1_minimum.py, g1_spectral.py, summarize_scans.py, evidence_manifest.py;
  certifier-design.md and every evidence/witness-*.json receipt.
- independent-checks-witness.md, independent-checks-math.md,
  independent-checks-finite-astra.md. Supplementary checks are complete
  at their explicit scopes; none replaces this Claude audit.
- manuscript-changes.md and the complete current manuscript/README;
  M7's appended history, proposed-record-changes.md, ALLOCATIONS.md,
  allocation-scan.json, COLD_STORAGE.md, cold-storage.json and
  evidence-manifest.json.

## Reproducible checks

From repository root:

```sh
python topics/padua-mz-cleanup-20261105/code/evidence_manifest.py
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m 60 --witness /tmp/mz-cleanup/cert-m60/witness.json.gz --scratch /tmp/mz-audit/cert60 --output /tmp/mz-audit/producer60.json
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness /tmp/mz-cleanup/cert-m60/witness.json.gz --output /tmp/mz-audit/independent60.json
```

python-flint0.9.0 was installed in the scratch dependency path. Adapt the
path in a fresh cloud session; do not depend on AC's computer. The small
odd checker and exact reproduction commands are recorded in its report.
For a new large finite rerun use the same commands with1101/1240/1600;
producer timings are40/50/95s. The initial minimum runner can regenerate
proposals if artifacts are absent; a newly generated vector may differ
across numerical libraries and requires its own new acceptance receipt.
Do not claim an old witness identity from a different regenerated vector.

The159,265,962B verified C1 package and44,618,351B verified final scan
supplement are staged under /tmp/mz-cleanup/transfer-stage, with full
inventories and SHA-256 in the storage manifest. External delivery remains
pending. In a fresh environment explicitly distinguish missing exact
artifact retrieval from a separately executed regenerated certificate.

## Scope limits

- Auditor writes audit-01.md and its own disjoint support/evidence only;
  update LOG/results/PR audit metadata as needed. Do not silently edit
  developer proofs/code and count that as independent approval.
- Do not apply shared proposals, assign final IDs, edit other topics,
  start C6, add new mechanisms, perform submission or change rules.
- Sandbox-only runs, at most4h wall/run and about24h cumulative CPU,
  as AC authorized in handoff01/LOG. Ask AC before any external machine.
- No main push, merge, force-push, tags, settings or .github changes.

## Acceptance and outputs

Write audit-01.md with actual model/effort, exact candidate/source hashes,
reading/novelty coverage, actual commands and independent reruns, findings
and residual trust/artifact limits. Every finding must have actionable
scope and evidence. An audit of existing receipts is not a new execution.
Update this topic's results and PR26's AUDIT section honestly.

Findings set WORK and a new numbered response handoff for Codex
gpt-6.1-sol xhigh; clean acceptance sets PR and a new numbered preparation
handoff for Codex gpt-6.1-sol xhigh. Preparation must refresh main/live
reservations, assign final IDs, apply scoped shared changes, refresh the
inventory and perform required integration/protocol checks. No merge
decision is requested until that later step. Commit outputs first; then
in a separate commit close this handoff's status at that exact SHA and
add the next numbered handoff. Push both before replying. Only AC merges.
