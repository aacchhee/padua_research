# Audit-01 — results-in-repo-20261101

- Decision: **WORK — three findings in the migrated results summary.** The repository-only rule change is accepted within this protocol scope. PR #16 stays draft until the findings are answered.
- Auditor / step orchestrator: Codex, requested `gpt-6-astra`, medium; appropriate for protocol and transcription review. The runtime does not independently attest the serving model or effort. This auditor is distinct from the Claude developer.
- Date: 2026-11-01, Europe/Oslo.
- Candidate: `715b1823bee0c5053c8376310a39b1f12c48e3ac`.
- Rules read / publication head: `f628a1f873572d43a625befda422ba0af49d5c48`. The four deliverable files are byte-identical at the candidate and publication heads.
- Refreshed main / base: `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`, already an ancestor of the branch; no merge needed.
- No novelty content: this changes storage instructions and summarizes previously accepted records. The full `state/IDEAS.md` read and novelty gate are omitted on that explicit basis. No new IDs: **no range**.

## Coverage and accepted portions

Read `AGENTS.md`, `agents/WORKFLOW.md`, both role files, every template, this topic's log and handoffs, PR #16's body, and all three new results files. Compared the rule against the two AC instructions quoted in the log. Read PR14's report, audit-01 including Addendum A1, response-01, handoff05, and its 22 new registry rows. Checked the statements of PD-T111/112/113/115 directly for summary fidelity. This is not a fresh mathematical audit of those accepted results.

1. **AC's storage instructions: PASS.** WORKFLOW line 105 explicitly places each `results/<topic-slug>.md` and the root `RESULTS.md` in Git. Topic ownership, updates in the topic PR, and preserving all sections during conflicts are clear. The existing integration rules remain applicable.
2. **Cloud operation: PASS for the active rules/templates.** A full search of `AGENTS.md`, `agents/`, and `templates/` found no other requirement to use AC's computer for routine agent work. Local execution in a cloud workspace is permitted. Unfetchable papers and large-artifact cold storage are the explicit exceptions; pending delivery does not block independent work. Historical topic reports/handoffs still describing local results are historical records, not amended by this PR; migrations remain outside this audit.
3. **Evidence rules: PASS.** The default off-Git generated-output policy and 1 MB per file / 5 MB aggregate limits are byte-identical. The new exception describes short handwritten summaries, not generated evidence. No scientific registry, theory, code, template or protected workflow was changed.
4. **Merge and result provenance: mostly PASS, subject to findings below.** GitHub reports PR14 merged at `2026-11-01T15:19:41Z`, i.e. 16:19 Europe/Oslo, as `e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9`. Fetched PR14 head `635ba4fd537be9a4dbc060617fbc0535db4d72ad` has exactly the same tree. The counts 17 PROVED / 2 MEASURED / 3 OPEN refer to its 22 new records; the fourth OPEN item in the summary is the pre-existing PD-T028. Brackets, finite measurements, negative-corner asymptotic, scoped failures and retained OPEN targets match the merged records. The text consists of research summaries and repository metadata; no third-party fulltext, private material or credentials were found in these files. This is content inspection, not a claim about the uninspected local originals.

## Findings

### F1 — P2: restore the constraints in the operator summary

Location: `results/padua-mz-2d-20261101.md:35`.

The displayed supremum has no domain or unit-norm constraint. PD-T112 states the supremum over `p in Pi_n` with `||p||_L2(dx dy)=1`; without normalization, scaling a nonzero constant makes the displayed expression unbounded. Also, PD-T113 requires **both** `0 <= r <= n` and `n+r <= m` for reproduction. The summary drops the first condition. The edge case `m=1,n=0,r=1` satisfies the displayed condition but the operator has constant range and cannot reproduce `Pi_1`; the source explicitly treats this case with `r=0`.

Requested response: transcribe the source constraints, or replace the abbreviated formula with a faithful linked verbal summary. Define `tau` and `beta_abs` briefly if retaining the bound, or link their definitions. No source theorem or status needs changing.

### F2 — P3: distinguish the actual m40 audit method

Location: `results/padua-mz-2d-20261101.md:31`.

The sentence attributes the listed brackets collectively to a second certification by Sylvester leading minors. In audit-01, R3 completed that method only at m10/20/30. Addendum A1 says the m40 run stopped without a verdict and was replaced by an independent Cholesky-proposed integer congruence plus exact positive strict row-dominance check. A1 explicitly discloses that this shares the developer's general congruence/dominance principle. Line 12 correctly notes A1, but line 31 loses that method distinction.

Requested response: state the two ranges/methods accurately, link A1, and retain its methodological caveat. All eight brackets remain accepted; no rerun is requested.

### F3 — P3: make the migrated topic file link to its records and evidence

Location: `results/padua-mz-2d-20261101.md:14` and its result bullets at lines 20–42.

The file contains **zero Markdown links**. The audit/evidence paths are code-formatted text; result IDs have no linked durable homes. This does not meet the new WORKFLOW line 105 requirement for “links to the durable records and evidence,” repeated in `results/README.md`. The root merged view links to this topic file, so it currently leads to another summary with no clickable source trail.

Requested response: add repository-relative links to the existing report/registry and the relevant durable records, audit and compact evidence. A compact grouped set is sufficient; do not copy proofs or evidence into the summary. Verify that the targets resolve from `results/`.

## Executions and evidence

Actual commands included:

```sh
git fetch origin '+refs/heads/*:refs/remotes/origin/*'
git diff origin/main..715b182 -- agents/WORKFLOW.md
git diff 715b182..f628a1f
rg -n -i 'Downloads|Windows|machine|local|cold.storage|results' AGENTS.md agents templates
git fetch origin refs/pull/14/head:refs/remotes/origin/pr14-audit-reference
git diff --quiet e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9 refs/remotes/origin/pr14-audit-reference
git diff origin/main..HEAD --check
```

Also executed an inline Python/subprocess check for base ancestry, candidate/publication blob equality, the single changed WORKFLOW line, unchanged protected paths, existing Markdown link resolution, and SHA-256 identities. Its observed results and file identities are committed in [audit-checks-01.json](audit-checks-01.json). The initial default-sandbox fetch attempts failed to connect to the proxy; the normal proxy path succeeded with network access enabled for the command. No bypass or credential changes were used.

GitHub connector reads independently established PR14's merge metadata and PR16's head/base/body. No numerical or exact scientific producer was rerun: this audit tests transcription against accepted records, not those proofs or computations. No local machine was accessed, no other topic was migrated, and no main push, merge, tag, force-push or `.github` change occurred.

## Disposition and next step

Claude should answer F1–F3 in `response-01.md`, making only the specified summary corrections and links. The rules themselves need no revision. These exact transcriptions and links do not change accepted mathematical claims, dependencies, statuses, code or evidence; a documented resolution with source comparison and link checks may proceed to PR under the ordinary workflow without another scientific audit. Any wider statement or rule change returns to AUDIT.

Keep PR #16 draft while findings remain. At preparation, record the topic's own concise outcome in `results/results-in-repo-20261101.md` and, if updating the merged view, change only this topic's section; preserve the migrated PR14 section. Other local-only migrations remain outside scope. No reservation or scientific integration work is introduced. Only AC merges.
