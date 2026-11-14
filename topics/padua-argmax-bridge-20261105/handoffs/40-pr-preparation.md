# Handoff 40: PR preparation plan, final freeze batch (both gated on AC)

- Status: open
- Previous handoff: 39-claude-review-response07.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator; Sol medium for TeX/README/tooling edits; a distinct Astra high agent for the focused re-check.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `e40d643fda01fc1d80aed186666f09f0414532e5` (audit-08 outputs; in-place MINOR fixes at `63109a8`); this handoff is the following handoff-only commit
- Main / base: `99a9b1d161e41a80c4fd425b63022c681fbe8779`, merged
- Stage: WORK (PR preparation not started; readiness not offered)
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; review work by three Claude Opus 5.5 subagents instructed at xhigh (disclosure in audit-08.md). · 2026-11-14

## State

[audit-08.md](../audit-08.md) accepts response-07: the audit-07 MAJOR (data statements versus the public kit) is resolved, no BLOCKING or MAJOR finding, no change to mathematics, evidence or the numerical core. The delivered public ZIP (5,149,206 B, `b341e6a1…adbaa`) was independently checked and replayed. P7-02 is resolved by AC (retain with explicit disclosure); do not ask again or sanitise.

## Authority

Working-branch commits and pushes and PR metadata stay authorized. No main push, merge, force-push, tag, `.github` or settings change, no external submission or contact, no invented licence, authorship, storage or DOI, no upload. Only AC merges or publishes. AI declaration, ORCID, contributions, funding and the draft marker are AC's. No native campaign, certificate production, retry, rescue, threshold or theorem change; no full numerical replay.

## Read first

AGENTS.md, agents/WORKFLOW.md (PR procedure, reservation check, registry application by reviewed diff), agents/codex/CODEX.md at the current head (record the SHA); [audit-08.md](../audit-08.md) and its reports.

## Task A: PR preparation (gated on AC's authorization of final-ID assignment)

No shared-registry change exists yet (`PROOF_STATUS.md`, `ID_CROSSWALK.md`, `RESULTS.md`, `state/`, literature index). The reservation (`ALLOCATIONS.md`: PD-T392–431, PD-N146–161, IDEA-490–529, LIT-598–613) is still unassigned. If AC's prompt to you does not state that final IDs may be assigned, report this gate and do only Tasks B (preparation) and C. If it does: apply the registries by editing the shared files directly, repeat the reservation check against the current heads of main and every open PR (record the heads), and leave the reviewed `git diff` and the reservation refresh for the readiness check by the auditor (Claude). Reaudit applies only to a material change beyond the audited scope.

## Task B: one final freeze batch (gated on AC's own edits)

AC will edit the AI involvement paragraph, the draft marker and DOI/data-statement text, which changes both PDFs and therefore the public ZIP. Do the following once, with those edits, not before:

1. Returned MINORs. **M8-02** both data statements: the preservation archive contains the native histories of the regenerated records (320–510), not "the full native histories" of all records; **M8-03** restore "The recorded interpreter, libraries, operating system and hardware are trusted" in both trust-table footnotes; **M8-06** name the repository before "Repository paths below"; optional **M8-04/M8-05** (identify the archives by size/hash if AC wishes; say verify.py is a new adapter).
2. Tooling **M8-01**: `check_correspondence.py --built-labels` must check document identity (paper aux in the companion directory must fail), aux freshness, page counts and the 152 ≤ 5×59 ratio it cites, and fail cleanly on a missing aux.
3. Kit **P8-01** reject empty `--degrees`/`--polynomial-degrees` selections (and consider `allow_abbrev=False`, strict value patterns: **P8-02**); **E8-01** correct the README sentence about hash/count comparison; **P8-03/E8-08** README PASS-line order and line lengths; **E8-05** remove "the audit"; **P8-05** add n=34 ≈ 1.93 GB and say higher degrees were not measured; **P8-04** optionally name `/root/a1_develop` and the MANIFEST PDF source paths. Any adapter change gives a new identity: freeze a new source commit, rebuild once, new ZIP hash, one bounded smoke, a distinct-agent check of the ZIP delta. New paired TeX/Bib freeze, separate pointer commit, correspondence default, `--archival`, `--built-labels`, baseline controls, mutation scenarios, scanner (empty map), rendered changed pages.
4. NOTEs (E8-06, E8-07, P8-06..08) in `response-08.md` as dispositions.
Then a final diff review by Claude (data statements, this list and the ZIP delta only).

## Task C (now)

Write `response-08.md` with one disposition per audit-08 finding (accepted-bundled, deferred or declined with reason); update `pr-update-20261113.md` (audit-08 result, the corrected budget figures, the gates above). Do not edit earlier audit reports, handoff bodies or the dated Claude notes.

## Open decisions for AC (not yours)

(1) Budget: bound 11,870,763 B against 10,000,000 B (main 9,787,481; topic share 2,061,004; tree 11,848,485): exception, cold-storage destination or share reduction. (2) Upload, DOI, licence, AI declaration (omits Sonnet 5.5, which orchestrated audits 02–08), ORCID, contributions, funding, draft marker. (3) Authorization to assign final IDs and apply the registries.

## Frozen

All mathematics, E01–E15, J01..J03, the finite theorems and certificates, the hybrid engine freeze `0d9ce0a5…`, the numerical core, both archives (public `15885d34…` and `b341e6a1…`, preservation `d3452a17…` unchanged), earlier freezes and all audit reports.

## Publication

Commit outputs first; then in a separate commit close this handoff as `done in <sha>` and open the next numbered handoff; exactly one stays open while work remains. PR 27 stays a draft.
