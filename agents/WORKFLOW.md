# Research workflow

## Roles and model allocation

The orchestrator owns scope, task allocation, integration, Git, and the PR. Developers produce claims, code, proofs, and evidence. A distinct agent audits them; the developer cannot approve its own work. The auditor chooses the appropriate audit depth and records the model and effort used. AC alone merges.

| Task | Codex model and effort | Claude model and effort |
| --- | --- | --- |
| Technical development and code | `gpt-6.1-sol`, medium | Sonnet 5.5, high |
| Mechanical edits and routine checks | `gpt-6.1-sol`, medium | Sonnet 5.5, medium |
| Mathematical development | `gpt-6.1-sol`, high or xhigh | Opus 5.5, high or xhigh |
| Especially hard mathematics | `gpt-6.1-sol`, ultra, with written justification | Opus 5.5, xhigh |
| Protocol and ordinary technical audit | `gpt-6-astra`, medium | Auditor chooses Sonnet 5.5 high or Opus 5.5 high |
| Mathematical audit | `gpt-6-astra`, high | Opus 5.5, high or xhigh |
| Adversarial audit, novel mechanism, or a stalled proof | `gpt-6-astra`, xhigh; ultra only with written justification | Opus 5.5, xhigh |
| Ideas campaigns: conceptual generation, gating and adversarial idea checks | unchanged (rows above apply) | Fable 5.1, xhigh (added 2026-10-31 at AC's explicit request); Opus 5.5 xhigh remains allowed |

The Fable 5.1 row is restricted to ideas campaigns: brief writing, candidate generation, duplicate gating and adversarial idea checks. It does not change the developer/auditor separation, the evidence rules, the status words or the Codex column. Where an ideas campaign runs a tiny sanity script, Sonnet 5.5 high remains the development model for it. Record the actual model and effort in every commit trailer and log entry.

Use agentic orchestration: delegate bounded development, independent checks, or audits when useful. Give each subagent its inputs, expected artifacts, model, scope, and acceptance criteria. Only the orchestrator changes Git state. Batch independent file reads and searches. Do not request unavailable models silently: report the limitation and any proposed substitute to AC before work whose required model is unavailable.

## Work cycle

One topic is one branch (`codex/<slug>` or `claude/<slug>`) and one PR, with a log at `topics/<slug>/LOG.md`. `New topic: <objective>.` starts WORK; `Continue <branch>.` means: read the rules, the log (if the topic has one) and the open handoff in `topics/<slug>/handoffs/` at the branch head, and carry out that handoff. A small job explicitly requested with `no audit` may omit the audit and log, while retaining branch and PR rules. It does not waive a numbered handoff when further agent work remains; without a log, the necessary context and the handoff chain live in the handoff files. This exemption must not add or upgrade any `PD-T`, `PD-N`, `IDEA`, or `LIT` entry, or change rules, templates or registry schemas; such work follows the ordinary audit cycle.

**Handoff files.** Each topic keeps numbered handoffs in `topics/<slug>/handoffs/NN-<step>.md` (`01-audit.md`, `02-response.md`, …), following `templates/HANDOFF.md`. The orchestrator of the session that passes work to another agent or session opens a **new** handoff with the next number. That orchestrator is the developer's, the auditor's or the topic orchestrator, whoever holds the open handoff. The handoff contains the complete instruction for the next step:
- the next agent, model and effort;
- the branch and the input head SHA, i.e. the existing commit being handed off, as distinct from the later commit that publishes the handoff;
- the stage, scope and inputs to read;
- what to do and what not to reopen;
- the acceptance criteria and expected outputs.

Never overwrite or delete an earlier handoff, and never alter its instruction body; only its status line changes.
- **Numbering.** Only the orchestrator holding the open handoff allocates the next number and changes statuses. Parallel workers and subagents return their results to that orchestrator and never open handoffs of their own. Two independent orchestrators never work one branch at the same time.
- **Open while in progress.** A handoff stays `open` while its step is being worked.
- **Completion.** Commit the step's outputs first. Then, in a following commit, change only the old handoff's status to `done in <output-commit-sha>` and add the next numbered handoff, in the same commit.
- **Redirection.** If AC's message adds to or changes the instruction, AC's message takes precedence. Record the change in the log and in a new numbered handoff, and set the old status to `superseded by NN: <reason>`.
- **Cancellation** uses `withdrawn: <reason>`.
- **One open handoff.** At every published step boundary, a topic with remaining work has exactly one open handoff. This includes a topic waiting for PR preparation or a requested follow-up. Only AC merges.
- **Closing a topic.** When all assigned work is complete or AC withdraws the topic, close its last handoff and record completion or withdrawal in the log, or in the final handoff's status line for a log-exempt job. The topic then has no open handoff and needs no continuation prompt.
- **Before replying.** Commit and push the new handoff before replying to AC. The reply then ends only with the short `Continue <branch>.` prompt. The log links each handoff with one line.

Record the stage in the topic log: WORK → AUDIT → PR. The developer sets AUDIT when development is complete; the other agent (Claude for Codex development, Codex for Claude development) writes `audit-NN.md`. An accepted audit sets PR; findings set WORK. The developer answers every finding in `response-NN.md`. Audit rounds are limited as follows (see **Proportionate audit and records** below):
- One substantive independent audit per batch, with independent reruns of consequential computation. A batch is the set of changes submitted together for one audit: a topic's candidate head, or several PRs audited together.
- A **material change** returns to AUDIT for a focused re-audit of that change only. A material change is any change to a claim's statement, assumptions, definitions, quantifiers, scope, dependencies, proof, status or disposition; to a threshold, final ID or ID mapping; to result-bearing code, inputs or evidence; or to rules, templates or registry structure. In doubt, treat a change as material.
- A response that only fixes MINOR findings proceeds to PR; the readiness check confirms those fixes by diff, and no new audit round is needed. If that diff shows any material change, the topic returns to AUDIT.
- A response that changes no claim and rejects, or leaves unresolved, a finding with documented reasons also proceeds to PR. The disagreement is preserved for AC.
- From the third audit round of a topic onward, the auditor fixes each MINOR finding it can fix within the limits in **Proportionate audit and records**, lists each fix in its audit report, and returns all other findings to the developer.
- Severities are BLOCKING, MAJOR, MINOR and NOTE. BLOCKING means a claimed status or result is not supported; MAJOR must be fixed before PR; MINOR is wording or record hygiene; NOTE needs no action.

Preserve disagreements for AC. Never edit the auditor's report to resolve it. An independent subagent check supplements this handoff. A draft PR may preserve work before the handoff is complete, with audit marked PENDING.

At session start, fetch current `main` and the topic head and reconcile the base before developing, recording the base SHA. Rebase unpublished local work when appropriate; merge `origin/main` into an already-pushed branch when updating it. Never rewrite published history. Checkpoint and push substantial checked results promptly, including honestly labeled unfinished work at step boundaries after roughly ten minutes of changes. Commits use `proof:`, `refute:`, `test:`, `code:`, `exp:`, `lit:` or `docs:` and trailers `Agent: <Codex | Claude>` and `Model: <actual model and effort>`; disclose any runtime-unexposed metadata.

1. Read the rules at the working branch head, record that SHA, inspect the task and existing evidence, and state the intended result. Allocate disjoint file ownership where agents run concurrently.
2. Run the novelty gate below before generating ideas. For a task that adds no novelty content, record why the gate does not apply.
3. Develop, test, and checkpoint substantial results. Record unsuccessful approaches and pending runs as they arise. Keep durable theory and evidence files synchronized with the actual result.
4. Request an independent audit with the exact candidate SHA or file hashes, scope, claimed statuses, dependencies, and reproducible commands. Respond to each finding with a fix, evidence-based rejection, or explicit unresolved item.
5. Prepare the PR, updating shared state and registries once at this stage. Commit and push the topic branch; open the PR yourself. A draft may be opened earlier with audit explicitly pending. Reaudit material changes to claims, proof, code, evidence, rules, templates, or registry structure. Registry application, final-ID assignment and the reservation check are verified in one readiness check by the auditor (a reviewed `git diff` of the shared files plus the reservation refresh). This is not a separate audit round, unless the application makes a material change (see **Work cycle**) beyond the audited scope. Before requesting merge, remove completed initialization/preparation tasks from the shared frontier or describe their post-merge state; retain the detailed pre-merge stage in the topic log and PR.

## Novelty gate and candidate discipline

Before generating a new mechanism, scan the headings, identifiers, aliases, and summaries of the complete `state/IDEAS.md`, and read every obstruction and disposition table in full. Search mechanism terms and synonyms across ideas, theory, topic logs, literature, and negative results. Then read the full shortlisted entries and their linked theory. Read `literature/INDEX.md` before priority, novelty or attribution claims and before opening a PDF. Log the search scope, terms, shortlist, and differences. A title-only scan or an exact-word search is insufficient.

Generate candidates only after that gate. Give every candidate a provisional record following `templates/IDEA.md`, allocating its final `IDEA-nnn` at PR preparation and retaining unsuccessful, equivalent, deferred, and rejected candidates. Record the closest entries, applicable obstructions and exact hypotheses escaped, a duplicate/variant/new verdict, and cheapest decisive test. Do not pursue duplicates. State a falsifiable separation criterion: which mathematical property, assumption, invariant, domain, or proof step distinguishes it from the closest prior entry, and what observation would kill that distinction. Renaming or changing notation does not establish novelty.

Test the separation criterion first with the cheapest decisive argument or experiment. Reject or consolidate equivalent candidates while retaining their records and aliases. For surviving candidates, write the exact claim, assumptions, intended proof route, counterexample search, and verification plan before expensive work. Negative entries must specify the attempted mechanism, assumptions, parameter range, obstruction, evidence, and limits. A failure of one proof route does not reject a theorem or an entire family of approaches.

An audit involving ideas, novelty, mechanisms, or negative claims reads the full `state/IDEAS.md`, then relevant full entries and obstruction tables. An audit with no novelty content may omit the full read only after explicitly stating its scope and reason. Verify literature comparisons through inspectable sources; record coverage limits and avoid claims of exhaustive novelty without supporting evidence.

## Durable records and status

Use `templates/THEORY.md` for every durable mathematical result or obstruction. Record its global `PD-Tnnn` theory or `PD-Nnnn` negative-result ID, title and aliases, exact statement and quantifiers, definitions, assumptions, dependencies, status, proof or obstruction, limitations, evidence, independent checks, and next unresolved step. Use `templates/TOPIC_LOG.md` for working history and Runs needed; use `templates/LITERATURE_RECORD.md` for `LIT-nnn` source records. Allocate globally unique IDs at PR preparation, checking current base state and other active allocations; do not renumber accepted IDs. Temporary local labels are acceptable during development.

These are claim-level statuses; mixed documents must label their individual claims:

| Status | Meaning |
| --- | --- |
| `PROVED` | A complete proof under explicit assumptions is written and checkable. |
| `PARTIAL` | The target's own statement decomposes into explicitly identified conjuncts, cases or parameter ranges, some PROVED under split-off result IDs and all the rest OPEN; no other epistemic status occurs among those parts. Supporting lemmas or minor routine steps alone do not qualify. |
| `CONDITIONAL` | The stated conclusion depends on a named unproved hypothesis or unverified obligation. |
| `MEASURED` | A computed or empirical observation within a recorded finite scope, without a general proof claim. |
| `OPEN` | The stated mathematical part or target remains unresolved. This does not deny proved supporting results under their own IDs or minor routine steps labeled inside the file. |

`LITERATURE` labels cited source facts and is not a proof status. State what the source establishes, where, and what was independently checked. A quoted or cited theorem is not a locally verified proof; any dependence on it remains explicit. Do not use `PARTIAL` merely for incomplete implementation, unfinished reading, or a suggestive experiment.

### Split results before assigning a file status

Split by default. A substantive PROVED claim keeps its exact statement, its own theory file and ID, and PROVED status. Move CONDITIONAL, MEASURED or OPEN claims into separate files and refuted side conjectures into scoped `PD-N` files. Never let a weakest-part calculation relabel a substantive proved result.

A proved part is substantive if another result depends on it, if it would be reported on its own in `state/CURRENT.md`, `PAPER_MAP.md` or a manuscript, or if its proof is more than a routine step of the main argument. Only minor routine proved steps or lemmas may stay mixed with a main statement; label their statuses individually and give the file the status of its main statement. Minor routine steps are excluded from aggregation and never turn an OPEN main statement into PARTIAL. The developer proposes the classification, the auditor checks it, and disputes go to AC.

If the original combined target still matters, keep it registered with its true status (OPEN, CONDITIONAL, PARTIAL, or another applicable epistemic status) and dependencies on the split-off results. PARTIAL applies only to an explicit decomposition of the target's own statement into conjuncts, cases or parameter ranges, some PROVED under split-off IDs and the remainder OPEN, with no other epistemic status. Reference the proved parts without duplicating their substantive claims or proofs. When proved dependencies are only supporting lemmas rather than parts of the target's statement, the unresolved target remains OPEN. Record `Split from:` and `Split into:` in the theory files and original-to-split mappings in `ID_CROSSWALK.md`. Do not narrow or reword an original claim silently: preserve its original wording, the change and the reason in History.

Only after splitting, excluding minor routine steps and distinguishing parts of the target from supporting dependencies may remaining parts of its own statement use the weakest-status order PROVED > PARTIAL > CONDITIONAL > MEASURED > OPEN. The sole PROVED-plus-OPEN exception is the explicit target decomposition defining PARTIAL above; it never applies to routine steps or supporting lemmas. This describes the main target's remaining obligations, not the status of a separate proved dependency. A verification record adding no new mathematical claim is labeled separately and does not weaken a theorem or become a proved dependency. A distinct measured claim gets its own durable registered home. Never upgrade a status without written proof.

### Candidate dispositions and negative statements

REJECTED is a candidate/claim disposition, not an epistemic status and never part of the weakest-status ordering. Record the reason separately as `refuted | failed | equivalent | abandoned`, with evidence and exact scope. `refuted`: the claim's negation is established within a stated scope. `failed`: a mechanism or candidate is shown not to achieve its stated aim under stated hypotheses and parameter range. It applies to candidates and mechanisms only, never to a theorem or target whose proof attempt failed (a failed proof route does not reject a theorem; see above). `equivalent` and `abandoned` are IDEA dispositions. A deferred candidate is not rejected: record its IDEA disposition as `deferred`, with the reason and the condition for resuming it. A refuted registered claim must show `REJECTED: refuted` and a link to the refuting `PD-N` in `PROOF_STATUS.md`'s `Disposition / reason` column; update its theory record and idea disposition too. An old epistemic status is historical context, not permission to rely on a rejected claim: readers must check the disposition before using a registry row as a dependency. A `PD-N` file's status is the status of its negative mathematical statement (for example, the claim that a specified mechanism fails under stated hypotheses), which can be PROVED, CONDITIONAL, MEASURED or OPEN as warranted; the killed candidate's REJECTED disposition does not replace that status.

AC's L5 decision: reserve `PD-Nnnn` for refuted or failed mechanisms with a scoped negative mathematical statement and evidence. Record the precise assumptions and tested range; a measured failure does not become a universal refutation. Equivalent or abandoned candidates stay as IDEA dispositions with their aliases, reasons and references; equivalence or abandonment alone never creates a PD-N file or allocation. Do not create administrative PD-N records with a not-applicable status. A separate evidenced mechanism failure still gets its own PD-N even if the candidate is later abandoned.

## Computation and evidence

Separate planned runs, completed runs, and interpretation. For each completed run record the command, code revision, input identity, environment and relevant versions, seeds, scope, output location, and observed result. Put runs not actually executed under `Runs needed` with their purpose and exact next command where possible. Never fabricate success, timing, coverage, or independent verification.

Without a clone, fetch only required files at a pinned branch-head SHA, preserve their repository paths, and record that SHA and the complete fetched file list with the output. Do not mix unrecorded revisions. A later branch change does not change the provenance of an earlier run.

Independent reruns must actually execute separately from the developer's run and record their own inputs and outputs; reading the first output is review, not a rerun. For a computer-assisted proof, require a proved reduction from the mathematical claim to a finite check, exact arithmetic, committed checker code and evidence records, and an independent rerun. State the trusted dependencies and all remaining obligations. Numerical agreement alone earns `MEASURED`, not `PROVED`.

Generated outputs remain off-repository by default. AC chooses a Padua-specific cold-storage destination; until then use local working output and report archival work as pending. Use `templates/COLD_STORAGE.md` to manifest artifact path or locator, SHA-256, byte size, generating command, source commit/blob identifiers, checker command and checker output, plus retention and retrieval notes. A link without content identity is insufficient. Do not expose credentials in manifests.

Results tracking is repository-only. Each topic keeps its results file `results/<topic-slug>.md` in the repository, committed on the topic branch. Only that topic's orchestrator writes it, appending or revising its own entries: meaningful results with status, final or provisional IDs and links to the durable records and evidence, plus the current next step. The repository-root `RESULTS.md` is the merged view: it holds one section per topic, headed by the topic slug. A topic changes only its own section there, and only at PR preparation, in its own PR, by appending or replacing that section from its own results file. Never rewrite another topic's section or regenerate `RESULTS.md` from an older copy. A conflict in it is reconciled at integration like any shared registry, keeping every topic's section. A lost section is restored from that topic's results file. These are short hand-written summaries, not generated outputs. All agent work, including results, logs, handoffs, registries, code and committed evidence, must be possible from a cloud session with only the repository and the network. AC's computer (`Downloads\padua`) is needed only for reference papers that cannot be fetched (`Downloads\padua\papers`) and for the Padua cold storage of large artifacts (`Downloads\padua\cold_storage\<slug>\`). Agents write to it only through the cold-storage procedure above, or at AC's explicit request; when it is unreachable, they record the pending item and continue. Local files carrying third-party text or private material stay out of Git.

Do not store large outputs that can be regenerated (AC, 2026-11-02). Commit all code needed to regenerate and check outputs. Commit only short summaries, receipts and small essential evidence (normally under 16 KiB per file). Committed generated outputs of the whole repository together stay well below 5 MB; AC judged 18 MB too much.

Move larger outputs to cold storage, including logs, raw screens, reruns and copies, bulk certificates and large manifests. Record each moved file in `<topic>/cold-storage.json` and `<topic>/COLD_STORAGE.md` with:
- its SHA-256 and byte size;
- its Git blob at a pushed source commit, or its cold-storage locator;
- its frozen generating command and checker command;
- where its short summary lives.

`tools/cold_storage.py` plans, verifies, restores, cleans and exports these files.

A verified, retrievable artifact may supply the large evidence component of a claim; state any resulting verification limitation. Do not claim a computer proof is complete while required code, evidence records, or independent checks are absent.

Do not split files to evade limits. Moving a file to cold storage with its pinned bytes is not deleting a historical artifact. Rewriting Git history to purge blobs is AC's decision alone.

## Audit and PR records

Use three visible PR sections:

- `WORK`: concrete changes, exact claims and statuses, source/rule SHA, developer model and effort, computed results, evidence paths, and Runs needed.
- `AUDIT`: auditor identity/model/effort, audited SHA or hashes, files and novelty scope read, independent reruns, findings by severity, dispositions, and remaining uncertainty. Say `PENDING` until the audit actually finishes.
- `PR`: base and head SHAs, scope, readiness, shared registry updates, verification commands, unresolved items, and the exact decision requested from AC.

Update `state/IDEAS.md`, shared state, global IDs, topic indexes, and allocation records at PR preparation after checking current `main` and active PRs. During exploration keep local records without repeatedly mutating shared registries. Do not let concurrent writers allocate the same ID or overwrite state. Material divergence from the audited SHA requires a recorded impact check and, where needed, a focused re-audit.

Use provisional IDs `<namespace>?<topic-slug>-<agent>-<local-number>` for all four namespaces: `PD-T?charter-codex-01`, `PD-N?charter-codex-01`, `IDEA?charter-codex-01`, and `LIT?charter-codex-01`. Final IDs are assigned during PR preparation from the topic's reserved ranges (below). Retain every provisional-to-final mapping.

**Reserve fresh ranges; never reallocate.** Reserve the final-ID ranges a topic needs when it first needs final IDs (normally at PR preparation), and whenever it needs more. A draft PR does not need a reservation. The full reservation check below is run once at reservation time and once more at readiness, immediately before the PR is marked ready for merge.
1. Refresh `main` and every open PR, drafts included.
2. Read the ledger copy on each of those branches, plus every final ID they already use in `PROOF_STATUS.md`, `state/IDEAS.md`, `literature/INDEX.md` and `ID_CROSSWALK.md`. Also read the retired reservations recorded in those ledgers (see below), and the ledger of any closed, unmerged PR whose reservation is not yet recorded as retired.
3. Compute the maximum separately in each namespace. Start each new range above the highest ID that `main`, any open PR or any retired reservation uses or reserves. Never reuse, overlap or renumber an ID that another branch has reserved or allocated, even if that branch is unmerged or closed.
4. Record the reservation at once in the ledger on the reserving branch and in its PR body: namespace, range, count, branch, date, and the heads checked. Size each range with headroom; unused IDs remain permanent gaps.
5. If a topic needs more IDs later, it reserves a new range by the same procedure; it never shifts existing ranges.
6. After a merge, other branches merge `main` and keep their own reservations.
7. At readiness, repeat steps 1–3 against current heads, including newly closed unmerged PRs, and record the heads checked. If `main` or any open PR's ledger changes between readiness and AC's merge, repeat the check before the merge.

**Priority and collisions.** A reservation's priority is the pushed commit that records it, as linked from the PR. A date alone does not establish priority. On a genuine collision:
- preserve accepted IDs and the earlier published reservation;
- give the later, conflicting reservation a replacement by the fresh-range procedure;
- record that reservation's old-to-new mapping in the ledger and the crosswalk.

If priority is unclear, or if either repair would renumber an accepted ID, refer the conflict to AC before any further allocation.

**Retired reservations.** Reservations remain in force after a PR closes, is abandoned or loses its branch. Before an agent closes or abandons a topic, or deletes the only live reference to its reservation, it preserves that reservation as a *retired reservation* in the continuing batch ledger: namespace, range, owner, first published commit and PR locator. Later integrations keep these records. An agent that finds a closed, unmerged PR with an unrecorded reservation records it in the same way. If a past reservation cannot be reconstructed, stop allocation in the affected namespace and ask AC; never infer that the range is free.

**Transition (adopted 2026-11-01).** This procedure supersedes older ledger prose that requires a single allocation owner or that owner's confirmation.
- Keep that prose as historical provenance, and add a dated supersession note the next time the ledger is maintained.
- All existing recorded ranges and AC-specific instructions remain in force.
- Each open topic adopts this procedure at its next continuation, before any new reservation, final-ID assignment or readiness decision.
- Existing reservations are imported unchanged, with missing provenance (count, heads checked, commit) filled in. They are not reserved again, and no headroom is added retrospectively.
- A topic that needs no final IDs records "no range".
- Reservation-only ledger and PR-body updates are allowed when a draft is opened. They do not authorise earlier changes to scientific registries, or any final-ID assignment outside PR preparation.

When several PRs share registries or allocations, use a single ledger at `topics/<batch-slug>/ALLOCATIONS.md`, linked from `ID_CROSSWALK.md` and every member PR/log. The ledger records reserved IDs, owners, pinned bases/heads, dependencies and integration order. Reserve ranges by the procedure above: each reserving branch is the owner of its own ranges, and the authority is the union of all branches' recorded reservations, including retired ones. Writers on different branches never share or split a range. A collision that occurs anyway is resolved before any affected PR becomes ready, under **Priority and collisions** above. With no batch, record reservations at `topics/<topic-slug>/ALLOCATIONS.md` and link them from `ID_CROSSWALK.md` as soon as allocations exist. No ledger is needed while no IDs are reserved.

## Proportionate audit and records (adopted 2026-11-05 at AC's request)

These rules keep the checks that find real problems and drop process that only maintains itself. They apply from each open topic's next continuation. Existing records need not be rewritten.

- **Audit rounds.** One substantive independent audit per batch, with independent reruns, plus the readiness check (registry diff and reservation refresh). Re-audit only material changes. From the third audit round onward the auditor fixes MINOR findings in place within the limits below; see **Work cycle**.
- **Auditor fixes.** An in-place fix by the auditor is limited to MINOR findings:
  - wording and formatting;
  - links;
  - stale process text;
  - recording an already documented decision, with a link to it.

  It never makes a material change (see **Work cycle**). The audit report lists every such fix with its location, and the fixes are committed separately from the report so the readiness diff shows them on their own. Listed fixes need no further audit round. The developer may dispute any of them; disputes go to AC. A finding that cannot be fixed within these limits, or whose classification is in doubt, is returned as MAJOR.
- **No process stage in shared registries.** `PROOF_STATUS.md`, `state/IDEAS.md`, `state/CURRENT.md`, `ID_CROSSWALK.md`, `RESULTS.md` and literature records carry only:
  - claim content and status;
  - dependencies and dispositions;
  - links to the durable theory, evidence and completed audit records.

  Pending or in-progress process belongs in the topic log, the handoff and the PR body. That covers audit pending, response due, draft or PR state, and preparation tasks.
- **Hash-pin code and data, not prose.** Checkers may pin the hashes of code, inputs, certificates and evidence, whatever their file format. New checkers do not pin prose records: logs, theory, handoffs, audits and registries. Audit requests and reports still identify audited prose by commit SHA or file hash. Correct prose with a dated addendum in place. To correct an already pinned prose record, either update the pin in the same reviewed commit or add a dated companion note.
- **Registry application by reviewed diff.** At PR preparation edit the shared registries directly. The readiness check reviews the resulting `git diff`. Literal OLD→NEW proposal files, re-application scripts and application receipts are not required.
- **Disclose once.** A protocol deviation, process limitation or AC decision is recorded in one canonical place: the topic log or one named record. Other records link to it in at most one line instead of repeating it. A claim's scope, limitations and verification limitations always stay in its own theory record; registries link to it.
- **Handoffs.** Write a new numbered handoff only when work passes to a different agent or session.
  - Ending a session, or replying to AC with a `Continue` prompt, always passes work on.
  - Subagents of the current orchestrator are not a different agent for this purpose.
  - While one session carries several steps, the open handoff stays open and is closed `done in <sha>` when work passes on.

  The rules for numbering, status lines and one open handoff otherwise stay as above.

Rehearse the intended sequential squash integration in a disposable local branch without touching `main`, record resulting conflicts and semantic checks, and repair the topic branches before requesting AC's merge sequence. This batch rehearsal is required only for relevant multi-PR work and never authorizes merging, force-pushing, or rewriting published history. AC integrates ready PRs by squash merge; agents never perform that merge.
