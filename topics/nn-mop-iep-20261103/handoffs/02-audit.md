# Handoff 02 — nearest-neighbour MOP IEP — independent Claude audit

- Status: open
- Previous handoff: 01-work.md
- Next agent / model / effort: Claude, Opus 5.5, xhigh.
- Role: independent auditor (Claude audits Codex development).
- Branch: codex/nn-mop-iep-20261103
- Input head SHA: `ae7e6187e8731b6f83aa444d4d702a0ef779c564`
- Main / base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`
- Stage: AUDIT
- Written by / date: Codex orchestrator, GPT-6 (exact backend/effort unexposed),
  2026-11-05. Developer allocations were gpt-6.1-sol xhigh (gate), medium
  (code); supplementary check gpt-6-astra high. Metadata limitations are in LOG.

## Task

Audit the scoped result answering AC's question B; do not assume that an open
draft or the Astra check constitutes acceptance. Fetch main and the topic,
read rules at the topic head, and record full source/rule/audited SHAs. Only
the orchestrator performs Git mutations; no branch rewriting or merge.

1. Read the complete state/IDEAS.md and obstruction/disposition tables because
   this audit concerns a mechanism/novelty gate. Read the shortlisted full
   entries and linked theory identified in gate.md, especially IDEA-117,
   IDEA-031/090/111/193 and PD-T057. Read literature/INDEX.md before primary
   sources. Check the gate's primary versus campaign-mediated coverage.
2. Reconstruct theory/finite-moment-formulation.md (PROVED, standard linear
   algebra, no novelty claim): normality, moment solvability, nonzero h
   denominators, independence of predecessors, axis/degree-zero cases,
   common coefficients for both directions and finite coefficient domain.
3. Reconstruct theory/terminal-division-obstruction.md (PROVED scoped negative):
   terminal normality selects the common node polynomial; d=b2-b1 vanishes
   at total degree N-1; interior nonvanishing needs the normal opposite corner.
   Ensure this rejects only the stated unmodified all-layer division rule,
   not published results under their own nondegeneracy hypotheses or the
   existence of a boundary-aware stable updater.
4. Challenge the dictionary: shifted zero curvature differs from fixed-site
   commutation. PD-T057 only has interior commutativity for truncated sections.
   Covariant shifts/lifted encodings are not ruled out. Check the two MEASURED
   records theory/finite-checks.md and theory/fixed-site-dictionary-failure.md
   against actual exact outputs and explicitly finite domains.
5. Verify literature locators and the corrected C4: FHV recursive shifted
   families plus second-measure boundary data, or marginal recurrences;
   two fixed lines do not fill the lattice. Check the newer Kozhan–Vaktnäs
   finite-rectangle hypotheses and why they cannot be imported for common
   support on a normal total-degree triangle. Inspect inverse/zero-curvature,
   tree and Toda predecessors, without broad novelty or absence claims.
6. Assess the early gate stop honestly. C1 is standard; C2's literal dictionary
   fails; C3 is deferred because no concrete distinct updater survives; C4 is
   known exact algebra after correction. No C3/C4 numerical comparison was
   run, and no cost/stability equivalence is claimed. The broader stable NN
   update question stays OPEN. If the stopping rationale is insufficient
   under AC's original scope, return a specific finding rather than marking
   unexecuted numerical work complete.
7. Independently execute the two checkers below. Separate your own runs from
   developer and Astra runs; record environment, source hash, commands,
   exit status, output identity and observed counts. Exact finite agreement
   is MEASURED; neither checker is offered as a general computer proof.
8. Review candidate retention, provisional theory/source IDs, evidence sizes,
   reservation provenance and result/report/log consistency. No final ID is
   assigned yet and no shared scientific registry was changed.

Commands from repository root (write regenerable output outside Git):

```sh
python topics/nn-mop-iep-20261103/code/exact_nn_mop.py > /tmp/nn-mop-claude-exact.json
python topics/nn-mop-iep-20261103/code/independent_nn_mop.py > /tmp/nn-mop-claude-small.json
```

The first uses Python standard-library Fraction; second requires SymPy.
Expected finite scope: 14 main cases N=2,...,8, 476 recurrences, 70 shifted
flatness squares, 112 nonzero fixed-site commutators, 70 terminal zero d;
separate checker includes N=1 and a different N=4 case. Use hashes/counts in
exact-runs.md and independent-check.md to verify provenance, not to skip runs.
The only final developer code change after Astra review was a comment; its
new hash and repeated output comparison are in exact-runs.md.

## Read first

- AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md.
- This topic's LOG.md, original handoff01, gate.md, literature.md,
  candidates.md, report.md, all four theory files, exact-runs.md,
  independent-check.md and both code files.
- results/nn-mop-iep-20261103.md, ALLOCATIONS.md, allocation-scan.json.
- Campaign sources read-only at `d669363c9bce16da2af0f3b7db05a031b911edd5`,
  as listed in gate.md. Fetch its branch if needed, do not merge it here.
- Draft PR: https://github.com/aacchhee/padua_research/pull/22.

## Scope limits

Write only audit-NN.md and necessary topic-owned short audit evidence, LOG.md,
this topic's results file, and the next numbered handoff/status transition.
Do not silently fix developer claims or modify another topic. Do not merge,
force-push, alter tags, touch .github or allocate final IDs during this audit.
Keep raw outputs local/regenerable; AC's cold-storage access is not required
for these short receipts. Do not contact Leuven or any external person.

Permanent reservation (not final assignments): T286–293, N100–103,
IDEA376–383, LIT562–573, first pushed a0abe8b7b5af6e8c53dc8b0353934537f891f1c9.
Preserve all older reservations and gaps. Fresh live scans are required before
later final assignment/readiness; this draft remains unready until then.

## Acceptance and outputs

Produce audit-01.md naming the exact audited SHA/hashes, model/effort,
coverage, independently executed commands, severity-ranked findings and
limits. Explicitly disposition each proof/status classification, candidate
and source/stopping issue. Update only this topic's log/results and PR22's
AUDIT status; keep the PR draft while findings or preparation remain.

If findings remain, set WORK and hand back to Codex gpt-6.1-sol xhigh for
response-NN.md and fixes (medium for purely technical/mechanical work).
If clean, set PR and hand back to Codex gpt-6.1-sol medium for preparation:
fresh main/open-PR union scan, same-source literature deduplication, final-ID
mapping and additive topic-only registry/index/results updates. Mathematics
changes require the appropriate renewed audit. Do not mark merge readiness
before those preparation obligations are met.

Commit audit outputs first. In a following commit change only this handoff's
status to done in the output SHA and add handoff03 (response or preparation),
with complete scope and acceptance instructions. Link it from the log before
the output commit. Push before replying, preserve one open handoff, and give
AC the short next-agent continuation prompt. Only AC merges.
