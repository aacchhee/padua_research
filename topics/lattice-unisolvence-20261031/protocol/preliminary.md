# Protocol review — preliminary checkpoint

Rules read at `9444c274d1ac06ef3b047e7bf2f9531d22b6d744`, unchanged from recorded original rules. Reviewer: separate Codex protocol subagent, assigned gpt-6-astra medium (orchestrator confirmed); runtime model/effort unexposed. Scope is metadata, evidence bookkeeping, public-source compliance, links, branch-stack and allocation coherence. Scientific novelty and mathematical reconstruction belong to the separate Astra xhigh reviewer; this review adds no novelty or mathematical claim and does not repeat the full IDEA novelty audit. Required final Claude audit remains PENDING. No acceptance decision or Git mutation performed.

This is an in-progress review, not a final-deliverables audit. The orchestrator is preparing registries, final manifests and stage transitions.

## Early hazards communicated

1. Inherited batch ledger links to MZ final-ID map and preallocation hashes point to files absent on this branch. Use pinned remote blob links or explicitly scoped external provenance.
2. Ledger names the old MZ allocation owner at top and a next-preparing-owner policy below. Clarify transfer at preparation without implying other member acknowledgement or merge readiness.
3. Historical short remote pins 2d8c3ab and 8f500db claim full pins in provenance.json, but that file now contains refreshed 6673669103d59c4a955071dd3301408604413ed8 and a02bc357e5f0eed479f7020b85fecc57fda9b47f. Preserve historical full observations or clearly date the updated rows.

## Checks actually executed

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, REQUEST.md, plan.md, LOG.md, provenance.json, batch ALLOCATIONS.md, IDEA and COLD_STORAGE templates, C0 frozen scope, literature search log and Cools–Poppe source record; inspected prepare_evidence.py. Used read-only `git rev-parse HEAD`, `git log --oneline -7`, `git status --short`, `git for-each-ref --format='%(refname) %(objectname)' refs/remotes`, `git ls-files -z`, and `git diff d367228 HEAD -- AGENTS.md agents/WORKFLOW.md agents/codex/CODEX.md`.

Python wrapped `git merge-base --is-ancestor` for both required base eb7bdcdf3a587dd49ea9d692b1d27c7af053fe64 and audited charter head 3bd9d4e8e7817eaf0abd5b7a750ea77eb8101342 against HEAD: both returned 0. Rules diff was empty. Read-only extension/path scan of tracked files found no PDF, HTML, EPUB, fulltext or extract files. This is a filename screening, supplemented by manual literature-record inspection, not a bytewise plagiarism classifier.

At this checkpoint tracked JSON/JSONL/CSV/TSV/OUT/NPZ/NPY files total 1,153,783 bytes; largest is C3 ranks.json at 535,224 bytes. This conservative extension subtotal is preliminary; final inventory must include other generated formats and newly committed evidence. No per-artifact size excess observed. Literature log differentiates excerpts from full reading and retains pending-reference labels. Plan/LOG separate predecessor scientific acceptance from unresolved protocol findings. Final hash chains, 5,061 inherited-schema pattern records, links, final sizes, Stage AUDIT and exact Claude Next remain to be checked after stabilization.
