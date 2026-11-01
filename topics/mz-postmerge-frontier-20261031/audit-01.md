# Audit 01 — administrative post-merge frontier update (PR #5)

- Auditor: Claude, independent auditor (the other agent from the Codex developer). Model: Sonnet 5.5, high effort, as requested by AC. The session does not expose effort metadata, so the effort is the requested one.
- Reason for this choice: protocol and ordinary technical audit (`agents/WORKFLOW.md` model table allows Sonnet 5.5 high). The diff is administrative prose and verification records, with no mathematical claim, so neither Opus nor xhigh was needed.
- Date: 2026-10-31.
- Rules read at: `dc2694aa046d91ddefeb99687fabf80d3d80bc58` (branch head): `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`. The `agents/` tree (`24dd91ba…`) and `AGENTS.md` blob (`8c94c718…`) are identical at `8ee04f4`, `07c5f54` and `dc2694a`.
- Candidate: head `dc2694aa046d91ddefeb99687fabf80d3d80bc58` over base `07c5f5465d6de306aa81dbe8ca1f615295163864` (current `origin/main`, re-fetched during the audit). PR [#5](https://github.com/aacchhee/padua_research/pull/5): draft, GitHub reports mergeable/clean, 1 commit, 8 files, +229/−5.
- Read coverage: the full `git diff 07c5f54 dc2694a`; the six new or changed administrative files in full; `independent-protocol-01.md` in full; `PROOF_STATUS.md` rows PD-T014…PD-N006; `open-upper-limit.md` in full; `open-padua-target.md` lines 1–35; `m2-sharp-constant-open.md` lines 1–20 plus targeted grep; `mz-mean-convergence-screen.md` in full; `audit-01.md` verdict block and `audit-02.md` lines 1–80 of the MZ topic; the PR body.
- Novelty scope: not applicable. The diff adds no idea, mechanism, negative claim or priority claim and does not touch `state/IDEAS.md` (blob `e51ac0a…` identical at base and head). I therefore omitted the full `IDEAS.md` read, as `WORKFLOW.md` permits. I read only the IDEA-057/058 deferral rows to check one sentence. I verified no literature comparison; I only checked that the frontier restates `LIT-061–065` without strengthening it.
- Verdict: **ACCEPTED** for the administrative scope. There are no High or Medium findings. L1–L4 are Low, non-blocking, and recommended before AC merges. They are text-only; if the developer fixes them, a text-only impact check suffices and no fresh audit is required. This audit does not clear novelty and does not re-audit the unchanged mathematics.

## Independent checks actually run

All ran in the clone at `dc2694a` (Linux, git, `gh` REST, `/home/claude/venv312/bin/python`). No git command that changes state was run; `git fetch` and `git merge-tree --write-tree` were the only writes (objects only).

| Check | Command (abridged) | Result |
|---|---|---|
| Identity | `git rev-parse HEAD`; `git fetch origin main`; PR #5 via `gh api …/pulls/5` | HEAD `dc2694a`; `origin/main` still `07c5f54`; PR base/head match; draft; one commit |
| Diff shape | `git diff --name-status` and `--numstat 07c5f54 dc2694a` | 3 modified (`state/CURRENT.md` 1/1, `topics/mz-constants/LOG.md` 5/1, `ALLOCATIONS.md` 5/3), 5 added (`POST_MERGE.md`, 4 files in the new topic). Totals +229/−5 |
| Preservation, whole tree | `git ls-tree -r --name-only 07c5f54` minus the 3 modified paths, then `git diff --name-only 07c5f54 dc2694a -- <those paths>` | 311 tracked at base − 3 = **308**; 0 differ. Head has 316 = 311 + 5 added. This independently confirms "308" (I1) |
| Registry blobs | `git rev-parse {07c5f54,dc2694a}:<path>` for `PROOF_STATUS.md`, `ID_CROSSWALK.md`, `state/IDEAS.md`, `literature/INDEX.md`, `PAPER_MAP.md` | Identical blob IDs for all five |
| Science/rules dirs | `git diff --stat 07c5f54 dc2694a -- tracks literature agents templates AGENTS.md` | Empty: no theory, manuscript, source record, code, evidence, rule or template change |
| CURRENT charter part | `cmp` of lines 1–44 of `07c5f54:state/CURRENT.md` and `dc2694a:state/CURRENT.md`; `git diff -U0` | Identical; only line 45 (the MZ paragraph) changed |
| Ledger reservations | `cmp` of lines 14–24 (`## Final reservations`) of base and head `ALLOCATIONS.md`; `sha256sum` | Identical, sha256 `3601ca72…` on both |
| Ledger prose | `git diff --word-diff=porcelain` of the ledger | Changes only on line 3 (PR #2/#3 status clause), the PR #3 member row (l.30), the propagation paragraph (l.34) and one appended receipt line (l.41–42). Sections "Reconciled sources", "Final reservations" and the PR #2, programme-ideas and Lanczos rows are untouched. The owner designation inside line 3 is byte-identical, but line 3 itself was edited (I1) |
| Merge facts | `git show -s --format=%P%n%T 07c5f54`; `git rev-parse 07c5f54^{tree} 8ee04f4^{tree}`; `git merge-base --is-ancestor 8ee04f4 07c5f54`; `gh api …/pulls/3` | Parents `08fafe6…`, `8ee04f4…`; both trees `88108c08d0e4cd0584b262b9ac088ca592757896`; ancestor yes; GitHub: merged, `merged_at` 2026-10-31T22:20:47Z, merge SHA `07c5f54`, head `8ee04f4`, merged by `aacchhee` |
| Time zone | `TZ=Europe/Oslo date -d 2026-10-31T22:20:47Z` | 23:20:47 CET (+01:00), matching the "23:20:47 Europe/Oslo" wording. The merge commit's own timestamp is 23:20:46 |
| Frontier statuses | `grep` of `PROOF_STATUS.md` rows 40, 47, 48; read of the three theory files and `mz-mean-convergence-screen.md` | PD-T020, PD-T027, PD-T028 all OPEN. The 1/N gap, the "numerical lead 1.004437" wording, "complement of the univariate compression", the Nevai III + 1990 addendum "next decisive reading" and LIT-063 "pending" all match the records |
| Deferred routes | `grep` of `state/IDEAS.md` | IDEA-057 (rule classification) and IDEA-058 (fast/certified spectra) are `deferred`, as POST_MERGE says |
| Windows/novelty wording | `grep -n -i windows topics/mz-constants/*.md`; `tracks/mz-constants/paper/README.md:5` | Delivery is unconfirmed (`cold-storage.md:3,70`); the manuscript is a "15-page revised development draft", not submission-ready: both match POST_MERGE |
| JSON hashes | Python: for each entry in `checks.json`, `git show dc2694a:<path>` sha256 and byte length | 6/6 sha256 and byte lengths match; working tree equals the commit |
| Protocol-review hashes | Python: regex over the 17 table rows of `independent-protocol-01.md` against `git show dc2694a:<path>` | 17/17 match, including the late `checks.json` row |
| JSON validity | `json.load` on both files | Both parse |
| Links | Python walk of every `](…)` in the 6 changed `.md` files, resolved against `git ls-tree dc2694a` | 24 relative links, 0 broken (matches the PR's 24). External URLs not fetched |
| Whitespace/EOL | `git diff --check 07c5f54 dc2694a`; `git ls-files --eol` | rc 0, silent; all new files `i/lf` |
| Ledger copies | `git fetch origin claude/programme-ideas-20261031`, then `git rev-parse FETCH_HEAD:topics/padua-batch-20261031/ALLOCATIONS.md`; same for `claude/bivariate-lanczos-20261031` | Both `43c581fb242fd28ebe4d89ee4a42e3bbd660a159` (heads `2554433`, `f9bb099`; Lanczos advanced since audit-02 but its ledger path did not change). Base ledger is the same blob; this PR's is `33da4c3f…`. Reservation sections (l.14–24) are identical across all three |
| Propagation claim | `git merge-base --is-ancestor {07c5f54,8ee04f4} origin/<member>` | Neither member contains MZ main: no propagation happened, as the PR says |
| Conflict impact | `git merge-tree --write-tree --name-only <07c5f54 or dc2694a> origin/<member>` | programme-ideas: 0 conflicts with `07c5f54`, 1 with `dc2694a` (the ledger). Lanczos: 17 with `07c5f54`, 18 with `dc2694a` (ledger add/add). See L3 |
| Mergeability | `git merge-tree --write-tree origin/main dc2694a` | Clean |
| Trailers/author | `git show -s --format=… dc2694a`; `git interpret-trailers --parse` | Author and committer `Andrey Chesnokov <aacchhee@gmail.com>`; prefix `docs:`; `Agent: Codex`, `Model: requested gpt-6.1-sol medium; runtime metadata unexposed`. See L4 |

No scientific computation was in scope and none was run.

## Findings

### L1 — Superseded "audit pending" wording sits behind the new frontier page and is not disclosed

Location: `PROOF_STATUS.md:34` (PD-T014: "focused re-audit pending") and `:42` (PD-T022: "awaits focused re-audit"). Line 3 of each of the 21 files in `tracks/mz-constants/theory/`, including the three targets that `POST_MERGE.md:15-18` links, reads "Required Claude audit and unresolved literature/novelty coverage remain PENDING" (`git grep -c` returns 1 for each file).

Evidence: audit-02 M1 accepted the PD-T022 endpoint corollary (`audit-02.md`, "M1 — accepted"). `POST_MERGE.md:5` says the development, response and acceptance cycle is complete. A reader who follows the POST_MERGE links reaches a header saying the audit is pending. The PR is right not to edit these files, since AC's instruction preserves registry rows. The text is not wrong in this PR, only undisclosed.

Requested fix: add two sentences to `POST_MERGE.md` (an administrative file this PR owns) saying that these locations carry pre-acceptance wording superseded by audit-01/audit-02, and that "literature/novelty coverage PENDING" remains true. Any edit of the registry or theory headers should be a separate, AC-authorised metadata-only change.

### L2 — The rewritten CURRENT paragraph no longer names the accepted results by ID

Location: `state/CURRENT.md:45`.

Evidence: the base paragraph named PD-T014, PD-T022 (with the constant 2−4/N+4/N²), PD-T017/018, PD-T024, PD-N004, PD-T025 and PD-T021. The head names only PD-T020/T027/T028, and the links to `response-01.md` and `report.md` are gone. A grep of base and head `CURRENT.md` for `PD-[TN]01[3-9]|PD-[TN]02` returns 6 distinct IDs at base and 3 at head. The registry rows are intact and the prose claim "proofs, IDs and statuses are unchanged" is true. But the shared frontier no longer indexes the accepted MZ results, and `POST_MERGE.md` lists only the frontier.

Requested fix: restore the IDs inline, for example "CC upper bound (PD-T014, PD-T022), endpoint order (PD-T017/018), fixed-ratio constants (PD-T024), PD-N004, PD-T025, PD-T021". Optionally keep the two links.

### L3 — Ledger rows for the two member branches are now ambiguous, and the prose edit adds a ledger text conflict for each

Location: `ALLOCATIONS.md:31-32` ("Adopt these exact ledger bytes") against `:34` ("Later member branches must refresh from current main and reconcile this ledger"). `POST_MERGE.md:24` ("Programme-ideas and bivariate-Lanczos prepare their later integration from the MZ-bearing main").

Evidence: the member branches hold ledger blob `43c581f`. This branch's ledger is `33da4c3`, so "these exact bytes" no longer points to one blob. If this PR is merged, merging main into programme-ideas gains a ledger conflict (0 → 1) and Lanczos's ledger conflict becomes add/add (see the table). Neither member contains `07c5f54`, so "prepare" in POST_MERGE is intent, not a recorded fact.

Is this a "one ledger" problem? No. There is still one path, one named owner and one reservation table, and that table is byte-identical in the base, head and both member copies. Ownership and IDs are unchanged, so no reservation conflict exists to propagate under `WORKFLOW.md`. Only the integration-status prose diverges, and the PR says so and claims no propagation. Treat it as a drafting ambiguity, not a protocol violation.

Requested fix: reword rows 31–32 to say that the member's copy has the identical reservation table, and that on merging MZ-bearing main it should take main's prose. In POST_MERGE, replace "prepare" with "will prepare". Alternatively, record the expected conflict explicitly.

### L4 — Commit trailers are not parseable as one trailer block

Location: the message of `dc2694a`.

Evidence: `Agent: Codex` and `Model: …` are separated by a blank line. `git interpret-trailers --parse` returns only `Model:`. `8ee04f4` and `a27fdaf` return both. The content is present and the model disclosure is honest (requested configuration, runtime unexposed).

Requested fix: none on the published commit, because rewriting published history is forbidden. If AC squashes, the squash message should carry both trailers in one block.

### I1 — Wording precision in the PR's verification claims (no action)

- "308 protected tracked files unchanged" is correct, and I reproduced it. It means every tracked path at base except the three modified ones (it includes rules, charter and topic files). `checks.json` does not define "protected".
- "Ledger owner … unchanged" is true of the designation. Ledger line 3, which contains it, is not byte-identical; only the PR #2/#3 status clause changed.

### I2 — Topic log vs the template (no action)

`topics/mz-postmerge-frontier-20261031/LOG.md` has no Developer/Auditor header, no "Runs needed" section (the PR body says none) and no link to the ledger it edits. The stage line is correct for a new slug: `Stage: AUDIT; … Claude audit PENDING`, with branch, base, rules SHA and model recorded. The novelty-gate exemption is stated with its reason at LOG line 12.

### I3 — `independent-protocol-01.md` is framed correctly (no action)

It is labelled supplemental in its title, verdict and closing; the PR body repeats this. It is a Codex subagent, so it cannot replace this handoff, and it discloses that requested rather than runtime model metadata was recorded. It also says the GitHub timestamp was developer-reported. I re-queried it and it matches. Cosmetic: its last table row (`checks.json`) is separated from the table by a blank line and renders outside it.

### I4 — Integration form is described accurately (no action)

The records say "two-parent merge … no history rewritten" and never claim a squash. Older pre-merge lines in the MZ log that mention a planned squash are historical and untouched. Nothing in the diff upgrades a status, claims novelty clearance or claims propagation to the member branches. Windows delivery and the unresolved Nevai III / 1990 addendum comparison are kept explicit.

## Remaining uncertainty

- I did not verify the external literature (Nevai, Lubinsky, etc.) or re-derive any PD-T result. The audit covers only whether the frontier text matches the registered records.
- The wording "AC requested gpt-6.1-sol medium" in the log and commit cannot be checked from the repository.
- PR #4 (`codex/lattice-unisolvence-20261031`) carries its own older ledger copy (blob `eb0fd3fe…`) and conflicts with main with or without this PR (9 conflicts in both cases). This is outside PR #5's scope and is noted for AC's sequencing.
- Member branches move: Lanczos advanced to `f9bb099` during this audit. The ledger blob comparison holds only at the fetch time (2026-10-31).
- Hashes in `checks.json` pin `dc2694a`; any edit made for L1–L4 changes them and needs a text-only impact check.

## Requested next step and stage

Stage: **PR** (accepted audit). The PR stays draft until the orchestrator marks it ready. Under `WORKFLOW.md`, findings set WORK only if the developer chooses to act on L1–L4; if so, answer them in `response-01.md`, refresh `checks.json`, and record a text-only impact check. Otherwise record them as accepted-as-is in the PR's AUDIT section. AC alone decides the merge, and no decision beyond that is requested.

Suggested next prompt: `Codex (gpt-6.1-sol medium): Continue codex/mz-postmerge-frontier-20261031; answer audit-01 L1–L4 in response-01.md, then mark PR #5 ready for AC.`
