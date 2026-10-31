# Audit 02 — focused reaudit of response-01

- Auditor: Claude, independent auditor; Opus 5.5, high effort. This is the same configuration the runtime reported for audit-01. Protocol reaudit, so Opus 5.5 xhigh was not needed.
- Date: 2026-10-31.
- Rules read at: `73ec2bace241cb31b6c2ca9d155d736e86bd1b56` (branch head). The rules changed in this commit, so `AGENTS.md`, `agents/WORKFLOW.md` and `agents/claude/CLAUDE_ROLES.md` were reread in full.
- Audited candidate: `73ec2bace241cb31b6c2ca9d155d736e86bd1b56`, compared with `af9987f5da84299ecfff8ed9ceef4f7b84f2cd2e` (end of audit-01). Base `b2ec85f3fb2743a3b9292657fec9ac9da227d410` is still current `origin/main`.
- Read coverage: `response-01.md` in full; the full diff `af9987f..73ec2ba` across 12 files; the complete post-change text of `WORKFLOW.md`, `THEORY.md`, `IDEA.md`, `COLD_STORAGE.md`, `ID_CROSSWALK.md`, `PROOF_STATUS.md` and `state/CURRENT.md`; and the changed hunks of both role files, `LOG.md` and `technical-review.md`.
- Novelty scope: not applicable. Only protocol and schema changed; the registries are still empty.
- Verdict: **CHANGES REQUESTED, narrow.** Most dispositions are accepted. Two residual Medium issues remain in the M1 / Addendum A implementation. Both are one- or two-sentence fixes. Under L2 they are rule and registry-structure changes, so they need one more focused check.

## Checks actually run

| Check | Command (abridged) | Result |
|---|---|---|
| Whitespace | `git diff --check af9987f 73ec2ba` | Pass; confirms the response's claim |
| Audit-01 untouched | `git diff --quiet af9987f 73ec2ba -- topics/initialize-padua/audit-01.md` | Exit 0; confirms the response's claim |
| Links | Python walk of all `*.md` with inline-code spans removed, then resolving each relative `](…)` target | 33 links, 0 broken; 24 Markdown files. Matches the response's counts |
| Status vocabulary | `grep -rn 'REJECTED\|PARTIAL'` over agents, templates and registries | No remaining place treats `REJECTED` as an epistemic status; both role files mirror the workflow |
| Residue | Same scan as audit-01, excluding `topics/` | No matches |
| Commit trailers | `git log -1 --format=%B 73ec2ba \| git interpret-trailers --parse` | Only `Model:` parses; see R3 |
| Forbidden paths | `ls .github` | Absent |

## Dispositions of audit-01 findings

| Finding | Response | Reaudit verdict |
|---|---|---|
| M1 + Addendum A | Split by default; substantive PROVED claims keep PROVED; substantive-vs-minor test; original target preserved; split provenance; REJECTED moved to dispositions; PD-N status independent of the disposition | **Accepted, with residuals R1 and R2.** Items 1, 2, 4, 5 and 6 of Addendum A are implemented faithfully in `WORKFLOW.md:59-73`, `THEORY.md:3-40`, `ID_CROSSWALK.md:10-15` and `PROOF_STATUS.md:9`. Item 3 conflicts with the aggregation sentence (R1) |
| M2 | THEORY fields added | Accepted. ID kind, aliases, definitions, assumptions, split fields and PD-N scope are present; "next unresolved step" sits under Open items |
| M3 | Separation criterion and test discriminability split; cost ledger optional | Accepted. `IDEA.md:8,14-15` is now domain-neutral and matches `WORKFLOW.md:37` |
| L1 | Transient row removed; rule added at `WORKFLOW.md:31` | Accepted. `CURRENT.md:21` stays true after merge |
| L2 | Reaudit trigger extended | Accepted (`WORKFLOW.md:31`) |
| L3 | `no audit` guard | Accepted (`WORKFLOW.md:21`) |
| L4 | Provisional patterns for all four namespaces; ledger path; single allocation owner | Accepted (`WORKFLOW.md:97-99`, `ID_CROSSWALK.md:3-5`); see I3 |
| L5 | Kept open for AC; interim "not applicable — administrative disposition only" label | Accepted as a correct hold. The interim label avoids inventing a theorem. AC still has to decide |
| L6 | Source commit, retention and retrieval added | Accepted |
| L7 | Provenance wording corrected; loss of the original report disclosed | Accepted |
| I1 | Clarified external wrapper and temporary directory | Accepted |
| I2 | Left to AC; no settings changed | Accepted as a correct hold |

## New findings

### R1 (Medium) — The aggregation sentence can turn an OPEN main statement with minor proved steps into PARTIAL

Location: `agents/WORKFLOW.md:63` compared with `:67`; also `:55` and `:65`.

- Line 63 gives a file with minor routine proved steps "the status of its main statement". For an OPEN main statement, that status is OPEN.
- Line 67 then says that after classification, "legitimately co-located mathematical parts use the weakest-status order … with the PROVED-plus-OPEN-only case carrying PARTIAL". Minor proved steps plus an OPEN main statement are exactly such co-located PROVED and OPEN parts, so line 67 yields PARTIAL.
- This is the case Addendum A was written to settle: a tiny proved part must not change how the statement is labelled. `THEORY.md:24` says PARTIAL is "subject to … the minor-part exception", which supports OPEN, but the workflow text itself is ambiguous.
- There is a related overlap. Line 65 allows a preserved target to be PARTIAL "referencing a split-off PROVED part". Line 55 lets OPEN "not deny proved supporting results under their own IDs". The same target, with one proved split-off result and an open remainder, could therefore be labelled either PARTIAL or OPEN.

Requested fix: state explicitly that minor routine steps are excluded from aggregation and never make a main statement PARTIAL. Then define when a target is PARTIAL rather than OPEN. One suitable rule: PARTIAL when the target's own statement decomposes into explicitly identified parts (conjuncts, cases or parameter ranges), some of which are proved (split off and referenced by ID) and the rest OPEN. OPEN when the proved results are only supporting lemmas and not parts of the target's statement.

### R2 (Medium) — The canonical registry cannot show a refuted or rejected claim

Location: `PROOF_STATUS.md:11` compared with `WORKFLOW.md:71` and `THEORY.md:29-30`.

`REJECTED` is no longer a status. The theory template now records it as a separate "Candidate / claim disposition". The `PROOF_STATUS.md` table, though, still has only `Status` and `Status by mathematical part`. Consider a registered `PD-T` claim that is later refuted, for example a CONDITIONAL claim whose hypothesis turns out false. The registry would go on showing its old status with no visible rejection. A reader of the canonical registry could then rely on a refuted result. Before the change, a status of `REJECTED` would have flagged it.

Requested fix: add a `Disposition / reason` column to the `PROOF_STATUS.md` table (for example `— | REJECTED: refuted (see PD-Nnnn)`). State in `WORKFLOW.md:71` that a refuted registered claim must show its disposition and a link to the refuting `PD-N` in the registry.

### R3 (Low) — The `Agent:` trailer of `73ec2ba` does not parse as a Git trailer

Location: commit `73ec2ba`.

A blank line separates `Agent: Codex` from `Model: …`. Git therefore treats only the last paragraph, `Model:`, as trailers. `git interpret-trailers --parse` drops `Agent:`, whereas the same command on `9877b0b` returns both. Published history must not be rewritten, so leave this commit as it is. Put the trailers in one final paragraph from now on. Optionally, record the irregularity in the topic log so that tools reading trailers do not misattribute the commit.

### I3 (Info) — Provisional IDs contain `?`

Location: `WORKFLOW.md:97`.

The pattern `PD-T?charter-codex-01` is fine inside Markdown. But `?` is invalid in Windows file names and is a glob character in shells. The repository does not yet say how theory files are named. If they are named after provisional IDs, Codex's Windows/PowerShell environment will fail. Suggestion: in `tracks/README.md`, state that theory files are named by a slug or by final ID, never by a provisional ID.

### I4 (Info) — Template tidiness

Location: `templates/THEORY.md:22,30,36,40`.

`Rejection reason:` appears twice, under Status and under PD-N scope. The administrative "not applicable" value permitted at line 40 is missing from the `Overall status:` choices at line 22. Neither is harmful. Fold them in with R1/R2 if convenient.

## Remaining uncertainty

- This audit covers the consistency of the rule text. Whether the substantive-vs-minor test is workable will only show in the first real classification. The process for that (developer proposes, auditor checks, AC resolves) is in place.
- L5 and I2 are still AC decisions. Neither blocks readiness, because the interim rule and the hold are both consistent.

## Required development response

Codex answers R1–R3, plus I3 and I4 at its discretion, in `response-02.md`. R1 and R2 change rules and registry structure, so the stage returns to AUDIT for a check limited to those diffs. If they are fixed as requested and nothing else changes materially, I expect to accept and set the stage to PR.
