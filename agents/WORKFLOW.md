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

Use agentic orchestration: delegate bounded development, independent checks, or audits when useful. Give each subagent its inputs, expected artifacts, model, scope, and acceptance criteria. Only the orchestrator changes Git state. Batch independent file reads and searches. Do not request unavailable models silently: report the limitation and any proposed substitute to AC before work whose required model is unavailable.

## Work cycle

One topic is one branch (`codex/<slug>` or `claude/<slug>`) and one PR, with a log at `topics/<slug>/LOG.md`. `New topic: <objective>.` starts WORK; `Continue <branch>.` follows the log's next step. A small job explicitly requested with `no audit` may omit the audit and log, while retaining branch and PR rules.

Record the stage in the topic log: WORK → AUDIT → PR. The developer sets AUDIT when development is complete; the other agent (Claude for Codex development, Codex for Claude development) writes `audit-NN.md`. An accepted audit sets PR; findings set WORK. The developer answers every finding in `response-NN.md`; material changes return to AUDIT, while an unchanged claim with a documented resolution may proceed to PR. Preserve disagreements for AC. Never edit the auditor's report to resolve it. An independent subagent check supplements this handoff. A draft PR may preserve work before the handoff is complete, with audit marked PENDING.

At session start, fetch current `main` and the topic head and reconcile the base before developing, recording the base SHA. Rebase unpublished local work when appropriate; merge `origin/main` into an already-pushed branch when updating it. Never rewrite published history. Checkpoint and push substantial checked results promptly, including honestly labeled unfinished work at step boundaries after roughly ten minutes of changes. Commits use `proof:`, `refute:`, `test:`, `code:`, `exp:`, `lit:` or `docs:` and trailers `Agent: <Codex | Claude>` and `Model: <actual model and effort>`; disclose any runtime-unexposed metadata.

1. Read the rules at the working branch head, record that SHA, inspect the task and existing evidence, and state the intended result. Allocate disjoint file ownership where agents run concurrently.
2. Run the novelty gate below before generating ideas. For a task that adds no novelty content, record why the gate does not apply.
3. Develop, test, and checkpoint substantial results. Record unsuccessful approaches and pending runs as they arise. Keep durable theory and evidence files synchronized with the actual result.
4. Request an independent audit with the exact candidate SHA or file hashes, scope, claimed statuses, dependencies, and reproducible commands. Respond to each finding with a fix, evidence-based rejection, or explicit unresolved item.
5. Prepare the PR, updating shared state and registries once at this stage. Commit and push the topic branch; open the PR yourself. A draft may be opened earlier with audit explicitly pending. Reaudit material changes to claims, proof, code, or evidence.

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
| `PARTIAL` | The mathematical parts include both PROVED and OPEN parts, and no other mathematical status. |
| `CONDITIONAL` | The stated conclusion depends on a named unproved hypothesis or unverified obligation. |
| `MEASURED` | A computed or empirical observation within a recorded finite scope, without a general proof claim. |
| `OPEN` | The mathematical claim remains unresolved; no proved subclaim is being asserted as partial progress. |
| `REJECTED` | A precisely scoped claim or candidate is refuted, equivalent, or abandoned for a recorded reason; distinguish these reasons. |

`LITERATURE` labels cited source facts and is not a proof status. State what the source establishes, where, and what was independently checked. A quoted or cited theorem is not a locally verified proof; any dependence on it remains explicit. Do not use `PARTIAL` merely for incomplete implementation, unfinished reading, or a suggestive experiment.

For an aggregate file status use the weakest mathematical-part status in the order PROVED > PARTIAL > CONDITIONAL > MEASURED > OPEN > REJECTED, except the PROVED-plus-OPEN-only case carries PARTIAL. Prefer separate theory files where the claims separate naturally. A verification record adding no new mathematical claim is labeled separately and does not weaken a theorem or become a proved dependency. A distinct measured claim gets its own durable registered home. Never upgrade a status without written proof. Every failed or rejected idea also gets a scoped `PD-Nnnn` theory file and an idea-registry entry.

## Computation and evidence

Separate planned runs, completed runs, and interpretation. For each completed run record the command, code revision, input identity, environment and relevant versions, seeds, scope, output location, and observed result. Put runs not actually executed under `Runs needed` with their purpose and exact next command where possible. Never fabricate success, timing, coverage, or independent verification.

Without a clone, fetch only required files at a pinned branch-head SHA, preserve their repository paths, and record that SHA and the complete fetched file list with the output. Do not mix unrecorded revisions. A later branch change does not change the provenance of an earlier run.

Independent reruns must actually execute separately from the developer's run and record their own inputs and outputs; reading the first output is review, not a rerun. For a computer-assisted proof, require a proved reduction from the mathematical claim to a finite check, exact arithmetic, committed checker code and evidence records, and an independent rerun. State the trusted dependencies and all remaining obligations. Numerical agreement alone earns `MEASURED`, not `PROVED`.

Generated outputs remain off-repository by default. AC chooses a Padua-specific cold-storage destination; until then use local working output and report archival work as pending. Use `templates/COLD_STORAGE.md` to manifest artifact path or locator, SHA-256, byte size, generating command, source commit/blob identifiers, checker command and checker output, plus retention and retrieval notes. A link without content identity is insufficient. Do not expose credentials in manifests.

A committed generated file must be necessary and no larger than 1 MB; all committed generated outputs together must remain under 5 MB. If evidence exceeds these limits, store it in cold storage and commit its manifest, small checker, and checker output/result. Such a verified, retrievable artifact may supply the large evidence component; state any resulting verification limitation. Do not claim a computer proof is complete while required code, evidence records, or independent checks are absent. Do not split files to evade limits. These limits do not authorize deleting historical artifacts.

## Audit and PR records

Use three visible PR sections:

- `WORK`: concrete changes, exact claims and statuses, source/rule SHA, developer model and effort, computed results, evidence paths, and Runs needed.
- `AUDIT`: auditor identity/model/effort, audited SHA or hashes, files and novelty scope read, independent reruns, findings by severity, dispositions, and remaining uncertainty. Say `PENDING` until the audit actually finishes.
- `PR`: base and head SHAs, scope, readiness, shared registry updates, verification commands, unresolved items, and the exact decision requested from AC.

Update `state/IDEAS.md`, shared state, global IDs, topic indexes, and allocation records at PR preparation after checking current `main` and active PRs. During exploration keep local records without repeatedly mutating shared registries. Do not let concurrent writers allocate the same ID or overwrite state. Material divergence from the audited SHA requires a recorded impact check and, where needed, a fresh audit.

When several PRs share registries or allocations, maintain a batch allocation ledger with reserved IDs, owners, bases, dependencies, and integration order. Rehearse the intended sequential squash integration in a disposable local branch without touching `main`, record resulting conflicts and semantic checks, and repair the topic branches before requesting AC's merge sequence. This batch procedure is required only for relevant multi-PR work and never authorizes merging, force-pushing, or rewriting published history.
