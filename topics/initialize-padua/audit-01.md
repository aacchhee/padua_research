# Audit 01 — initialization scaffold

- Auditor: Claude, independent auditor (the other agent from the Codex developer). Model: Opus 5.5, high effort. The runtime session metadata reports the same model and effort.
- Reason for this choice: protocol and ordinary technical audit (`agents/WORKFLOW.md` model table). There are no mathematical claims, so Opus 5.5 xhigh was not needed.
- Date: 2026-10-31.
- Rules read at: `9877b0bbb477143617298f6ead2e37e2acda82a1` (branch head): `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`.
- Audited candidate: head `9877b0bbb477143617298f6ead2e37e2acda82a1` over base `b2ec85f3fb2743a3b9292657fec9ac9da227d410` (current `origin/main`). PR [aacchhee/padua_research#1](https://github.com/aacchhee/padua_research/pull/1); GitHub reports it mergeable, clean.
- Read coverage: all 23 files in the head tree, read in full, plus the base `README.md` and the three commit messages.
- Novelty scope: not applicable. `state/IDEAS.md` was read in full anyway; it has no entries and its tables are empty. The PR adds no idea, mechanism, negative claim, or priority claim.
- Verdict: **CHANGES REQUESTED.** There are no High findings. Medium findings M1–M3 change protocol semantics that every later topic will rely on. They are cheap text fixes and should be resolved before the registries are first used. Under the workflow, findings set the stage to WORK.

## Independent checks actually run

All of these ran in a fresh clone in this session (Linux, git, Python 3, `gh` REST).

| Check | Command (abridged) | Result |
|---|---|---|
| Base/head identity | `git rev-parse origin/main origin/codex/initialize-padua` | `b2ec85f…`, `9877b0b…`; PR base SHA equals current main |
| Reviewed-file hashes | `git show c74c70c:<f> \| sha256sum` and `sha256sum <f>` at head, for the 6 files in `technical-review.md` | All 6 match the recorded SHA-256 values, both at `c74c70c` and at head (LF bytes) |
| Change after technical review | `git diff --stat c74c70c HEAD` | Only `topics/initialize-padua/LOG.md` (+7) and `technical-review.md` (new); no protocol file changed |
| Relative links | Python walk of all `*.md` and resolution of every non-HTTP `](…)` target | 20 links, 0 broken |
| Backtick path references | `grep -ohE` over `*.md` | Every concrete path exists. Placeholders (`<slug>`, `NN`, `<key>`) and track-level files (`AUDIT_LOG.md`, `NEGATIVE_RESULTS.md`, `theory/`) are templates for future tracks, as intended |
| Residue scan | `grep -rniE 'bttb\|EX-[TCN][0-9]\|archive-2026\|pySuperDC\|state/state\|Terra\|padua-init\|PowerShell'` | Hits only in topic history (`LOG.md:14,17`, `technical-review.md:24-25`); none in rules, registries or templates |
| Line endings / file count | `git ls-files --eol`; `git ls-tree -r HEAD \| wc -l` | 23 files, all LF; `c74c70c` has 22 files, consistent with the review's count |
| Commit trailers | `git log --format=%B` | All three commits carry `Agent:` and `Model:` trailers and disclose effort that was not exposed; prefixes are `docs:` |
| Forbidden paths | `ls .github` | Absent; no workflow or settings changes |
| Repository state (read-only) | `gh api repos/…/branches/main`, `gh api repos/…` | `main` unprotected; squash, merge, and rebase merges all enabled (see I2) |

No scientific computation was in scope, and none was run.

## Findings

### M1 — Aggregate-status rule contradicts `OPEN` and blurs negative results

Location: `agents/WORKFLOW.md:47-60`; mirrored in `CLAUDE_ROLES.md:13` and `CODEX.md:13`.

- The weakest-part ordering puts `OPEN` below `PROVED`, `CONDITIONAL`, and `MEASURED`. A file with parts PROVED + CONDITIONAL + OPEN therefore aggregates to `OPEN`. But `OPEN` is defined as "no proved subclaim is being asserted as partial progress", and that file does assert one. The rule and the definition conflict.
- `REJECTED` is ranked as the weakest status. A file with a PROVED theorem and one refuted side conjecture aggregates to `REJECTED`, so the registry would show a proved result as rejected.
- The status of a `PD-Nnnn` file is undetermined. The negative statement ("mechanism M fails under H") may be PROVED, MEASURED, or CONDITIONAL, while the candidate it kills is REJECTED. The weakest-part rule then always gives `REJECTED`, which hides whether the obstruction is proved or only observed. Line 56 requires distinguishing refuted, equivalent, and abandoned, but no template field records that reason.

Requested fix:
1. Make `REJECTED` a disposition of a candidate or claim, and exclude it from the aggregate ordering, or define its place explicitly.
2. Restate `OPEN` as a part-level status, or define what the aggregate shows when proved parts coexist with CONDITIONAL, MEASURED, or OPEN parts.
3. State that a `PD-N` file's status is the status of its negative statement, with a separate rejection-reason field (`refuted | equivalent | abandoned`).

### M2 — `templates/THEORY.md` lacks fields the workflow requires

Location: `agents/WORKFLOW.md:45` compared with `templates/THEORY.md`.

The workflow requires these fields: "ID, title and aliases, exact statement and quantifiers, definitions, assumptions, dependencies, status, proof or obstruction, limitations, evidence, independent checks, and next unresolved step". The template has no Aliases line, no Definitions or Assumptions sections (they are folded into one placeholder), and no ID-kind marker (`PD-T` or `PD-N`). It also has no field for the rejection reason that M1 needs. Aliases matter most here: the novelty gate (`WORKFLOW.md:35`) requires scanning aliases, so a theory file without them cannot be found by the gate.

Requested fix: add `Aliases:`, `Definitions`, `Assumptions`, ID kind, and, for `PD-N` files, the attempted mechanism, parameter range, and rejection reason. `WORKFLOW.md:39` already requires these for negative entries.

### M3 — The idea template has no field for the workflow's separation criterion and carries domain-specific fields

Location: `agents/WORKFLOW.md:37` compared with `templates/IDEA.md:13-14`.

The workflow requires a falsifiable separation criterion: "which mathematical property, assumption, invariant, domain, or proof step distinguishes it from the closest prior entry, and what observation would kill that distinction". The template has no field for this. Its `Separation check` field means something else: whether "thresholds, dimensions, quantifiers, controls and precedence distinguish kill and survive outcomes at tested sizes", i.e. whether an experiment can tell the outcomes apart.

That field and `Construction and total cost ledger` presuppose a computational-cost, size-scaling style of research. This conflicts with the claim (README, PR body) that no subject-specific assumptions are preloaded. They read as structure carried over from an earlier campaign. They are not harmful, but they bias how future candidates are framed before AC has set the research question.

Requested fix:
1. Add `Separation criterion vs closest entry (and observation that kills it):`.
2. Rename the existing field to something like `Test discriminability:` and make it domain-neutral.
3. Make the cost ledger optional, or remove it until a charter needs it.

### L1 — Shared frontier will be stale after merge

Location: `state/CURRENT.md:21-23`, `LOG.md:4`.

After the squash merge, `main` would show the initialization topic at AUDIT with Claude's audit pending. The workflow updates shared state at PR preparation (`WORKFLOW.md:31,82`). At that step, update the row to reflect the post-merge state, or remove it.

### L2 — The re-audit trigger list omits protocol and template changes

Location: `agents/WORKFLOW.md:31`.

The trigger list reads "Reaudit material changes to claims, proof, code, or evidence". Rules, templates, and registry schemas are not on it. Lines 23 and 82 cover this only in general terms. For protocol PRs such as this one, the response to this audit will change exactly those files. Add "rules, templates, or registry structure" to the list.

### L3 — The `no audit` exemption could admit unaudited claims

Location: `agents/WORKFLOW.md:21` compared with `AGENTS.md:21`.

Nothing stops a `no audit` job from registering or upgrading a result status. Suggested fix: such jobs may not add or upgrade any `PD-T`, `PD-N`, `IDEA`, or `LIT` entry. Otherwise they must mark the row `unaudited` in the Evidence/audit column.

### L4 — ID-allocation mechanics are underspecified

Location: `ID_CROSSWALK.md:3`, `WORKFLOW.md:84`, `PROOF_STATUS.md:5`.

The "single coordinated ledger" for batch reservations has no defined path. Provisional formats are given only for `PD-T` (`PD-T?charter-codex-01`), not for `PD-N`, `IDEA`, or `LIT`. Concurrent PRs that each "check main and active allocations" can still collide without a fixed ledger location. Specify the path, for example `topics/<batch>/ALLOCATIONS.md` linked from `ID_CROSSWALK.md`, and give one provisional pattern for all four namespaces.

### L5 — A `PD-N` theory file for every rejected idea, including duplicates (question for AC)

Location: `WORKFLOW.md:60`, `state/IDEAS.md:11`.

Under the current rule, "equivalent to IDEA-004" or "deprioritized by AC" each consumes a `PD-Nnnn` and needs a full theory file. The negative-result namespace would then mix mathematical obstructions with bookkeeping. Option: require `PD-N` only for refuted or failed mechanisms, and record equivalent or abandoned candidates as `IDEA` dispositions with their aliases. This is a design choice for AC. If AC keeps the current rule, it is consistent as written.

### L6 — The cold-storage template does not cover all fields required at `WORKFLOW.md:70`

Location: `templates/COLD_STORAGE.md`.

The template lacks a source commit identifier (it has only script blob IDs), retention notes, and retrieval notes. "Regeneration and handoff" covers retrieval only partly. Add the missing columns or sections.

### L7 — Provenance wording of the technical review

Location: `topics/initialize-padua/technical-review.md:40`.

The file calls itself a "human-written review". `LOG.md:13` says the Codex orchestrator wrote it, summarizing the Astra reviewer's findings. The reviewer's own report is not preserved, and the six findings were fixed before the first push, so their pre-fix state cannot be inspected. Since the review only supplements this audit, this does not block. Correct the wording to "orchestrator-written summary of the reviewer's findings".

### I1 — Information: references to context outside the repository

Location: `LOG.md:14,17`.

"The older Terra routing in the project wrapper" and the local `padua-init/` directory refer to things outside the repository. As history they are honest and harmless. A short clarification that the wrapper is AC's Codex configuration outside this repository would keep the log self-contained.

### I2 — Information for AC: repository settings

`main` is unprotected, and merge commits and rebase merges are enabled alongside squash merges. The protocol assumes PR-only squash integration onto `main`. The rules correctly forbid agents from changing settings, so this is AC's decision. Branch protection (PR required, no force-push) and squash-only merges would enforce the protocol mechanically.

## Verified without finding

- Git authority. `main` is forbidden to agents and only AC merges. No tag, force-push, or `.github` operations are allowed. The bootstrap exception is recorded and does not continue. Authorization of the baseline commit `b2ec85f` is documented in its message and in `LOG.md:12`. The commit is authored by AC's account. I cannot independently verify AC's out-of-band authorization.
- Development/audit separation and the cross-agent handoff are symmetric across `AGENTS.md`, `WORKFLOW.md`, and both role files. The model allocations in the role files match the workflow table.
- The evidence, rerun, computer-proof, and size-limit rules are internally consistent. `LITERATURE` is separated from proof status throughout.
- No scientific content is present: all registries are empty, and the search for inherited identifiers found nothing outside topic history. The structural residue noted in M3 is the exception.
- The PR body's WORK/AUDIT/PR sections follow `WORKFLOW.md:76-80`. The AUDIT section was correctly marked PENDING.

## Remaining uncertainty

- This was a reading and consistency audit of protocol text. Whether the rules are workable in practice can only be tested by a first real topic.
- The Astra review's original findings could not be inspected (L7).

## Required development response

Codex answers each item in `response-01.md`, with a fix, an evidence-based rejection, or an item left open for AC. M1–M3 and L2 change rules or templates, so the stage returns to AUDIT for a focused re-audit of those diffs. L5 and I2 need AC's decisions.
