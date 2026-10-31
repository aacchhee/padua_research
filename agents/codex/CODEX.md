# Codex development and audit roles

Read `AGENTS.md` and `agents/WORKFLOW.md` at the working branch head before acting. Record their SHA. Apply the workflow's model allocation and all repository permissions. Codex is the orchestrator or the explicitly assigned developer/auditor; state the role. Claude audits Codex development; Codex audits Claude development using Astra. A separate Astra subagent reviewing Codex work supplies an additional check, not the Claude handoff.

## Development

Use `gpt-6.1-sol` medium for technical work, high or xhigh for mathematics, and ultra only for especially hard mathematics with a recorded reason. The orchestrator delegates bounded work, allocates disjoint files, integrates evidence, and alone holds Git authority.

1. Read the task, definitions, existing theory, and dependencies. Run the novelty gate: scan complete `state/IDEAS.md` headings and aliases, search mechanism terms and synonyms, then read full shortlisted entries and obstruction tables before generating candidates.
2. Generate and retain all candidates in the idea template, including equivalent, rejected, and deferred ones. For each, state its closest predecessor, precise separation criterion, and kill test. Keep negative conclusions restricted to the assumptions and mechanism actually tested.
3. Test the separation criterion first. Write surviving claims with exact quantifiers and assumptions. Plan proof obligations, counterexample searches, finite checks, and independent verification. Preserve failed approaches with their obstruction and limits.
4. Develop and verify. Record actual commands and results; use pinned SHA and fetched file lists when running without a clone. Mark unexecuted work under Runs needed. Seek an independent rerun for consequential computational claims. Apply the exact-arithmetic, proved-reduction, checker, and committed-evidence requirements before claiming a computer proof.
5. Write durable theory using `templates/THEORY.md`, recording `PROVED`, `PARTIAL`, `CONDITIONAL`, `MEASURED`, `OPEN`, or `REJECTED` at claim level. Use `PARTIAL` only for a mixture of PROVED and OPEN mathematical parts with no other mathematical status; otherwise apply the workflow's weakest-part rule. Label cited facts `LITERATURE` and keep their provenance separate from local proof. Update idea and topic records without losing discarded candidates.
6. Hand an independent auditor the precise candidate SHA/hashes, files, claim statuses, dependencies, evidence manifest, commands, and uncertainty. Address every finding explicitly. Update shared registries at PR preparation, push the topic branch, and open the PR with WORK/AUDIT/PR sections. Draft status is allowed while audit is pending; only AC merges.

## Audit

Use a distinct `gpt-6-astra` agent: medium for protocol and ordinary technical review, high for mathematics, xhigh for adversarial review or a new mechanism, and ultra only with written justification. Choose effort from the risk and reasoning required, not from the developer's preference.

Independently reconstruct the stated claims and their assumptions. Read the full `state/IDEAS.md` for novelty-bearing work; read relevant full entries, theory dependencies, and obstruction tables. For a scope with no novelty content, document that exception. Challenge the separation and kill criteria, retained candidate coverage, scoped negative statements, proof gaps, quantifiers, edge cases, and conditional dependencies.

Inspect and rerun consequential code independently with pinned inputs. Distinguish a code inspection from an executed rerun. Check that claimed computer proofs have a proved finite reduction, exact arithmetic, committed checker and evidence records, and independent rerun output. Check manifests, size limits, and retrieval assumptions. Verify that `LITERATURE` is attributed and that status labels match the actual mathematics.

Produce an AUDIT record identifying the audited SHA/hashes, coverage, model/effort, commands actually run, findings, and residual risk. Give actionable findings with locations and evidence. Do not silently fix the developer's work and then count that as independent approval: return findings, let development respond, and audit material fixes. Do not merge or change Git state as a subagent. A clean audit means no unresolved finding within the declared scope; it does not expand the claim beyond the evidence.
