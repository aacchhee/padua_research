# Independent allocation integration check

Rules read at `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`: `AGENTS.md`, `agents/WORKFLOW.md`, and `agents/codex/CODEX.md`. Date: 2026-11-01 UTC. Role: independent Codex audit subagent; Claude developed the allocation. Requested model/effort: `gpt-6-astra`, high; runtime-resolved model metadata is unavailable. The root orchestrator alone owns Git mutations.

Scope: the final-ID allocation in `6954664fc0906b7e5c8ff0f1804b077bd3b5861f`, as delivered at `37820a528c863e5cfe2dc2f1f8879b4fd40cf210`, against main boundary `21e620ba8b5f0e0706f3a8c6613517df04d9d469` and accepted scientific baseline `f4e213390f66a8c9f0c6bd65131b97b78db873c8`. No accepted mathematics, literature priority or novelty judgment is reopened. The full-IDEAS novelty audit does not apply to this administrative mapping/status-preservation check; the complete registry file is parsed for IDs and relevant rows instead.

## Result

The committed allocation passes all 52 independent assertions. There is no allocation blocker within this scope. The generator is a one-shot allocation tool: its documented default dry run fails after allocation because it treats its own committed IDs as collisions. That is a reproducibility/usability limitation, not evidence of a collision with another campaign. No allocator mutation was executed, and no developer files were changed.

| Namespace | Lattice allocation | Programme allocation | Next unreserved |
|---|---|---|---|
| PD-T | PD-T081–094 (14) | PD-T095–100 (6) | PD-T101 |
| PD-N | PD-N032–038 (7) | PD-N039–043 (5) | PD-N044 |
| IDEA | IDEA-177–189 (13) | IDEA-190–209 (20) | IDEA-210 |
| LIT | LIT-300–331 (32) | LIT-332–426 (95) | LIT-427 |

The independent checker reconstructs the exact mapping from the provisional inventory and stated ordering. All 192 newly allocated IDs are unique, occur exactly once in their primary registry, and avoid the complete four-registry ID inventory on pinned main and the LIT-293–299 reservation. The map contains 66 lattice allocations and 126 programme allocations. All 16 programme literature merges agree with the two source relation maps and target IDs already present on main; there are no new IDs for those merges. This check establishes mapping consistency, not the scientific validity of literature deduplication (a separate audit scope).

All 208 provisional records have one crosswalk row with the correct final-ID column. New primary rows retain their provisional aliases. All 32 PD records and 33 IDEA entries have exactly one corresponding canonical `Final ID:` line immediately after their provisional heading. LIT baseline tables retain provisional provenance and a map notice; their primary final rows and full mapping live in the literature index and crosswalk. Both ledger ranges, counts, next boundaries, the two explicit AC instructions, the member-specific owner exception, and the retained PR #11 reservation agree with the committed map.

The 36 canonical PD/IDEA files are byte-identical to the allocation parent after removing only the inserted Final-ID paragraphs. All 32 PD epistemic-status cells are unchanged from both that parent and accepted baseline `f4e2133`; allocation also preserves status tokens for the mathematical parts. Compared with `f4e2133`, T01 contains an earlier stabilizer proof clarification attributed to audit-03 support T3. That change predates allocation, is not hidden by this check, and is left to the root's prior-audit provenance assessment.

The root fetched PR #11 head `97968d2c2d039cb0910e0ea50747fb2d9e01a262`; this subagent then read its pinned ledger and literature index directly. Its ledger explicitly reserves LIT-293–LIT-299 and no PD-T/PD-N/IDEA block. All seven primary LIT rows exist there, and its complete primary LIT inventory is disjoint from the new allocation. The two fetched-source file hashes are in the machine-readable manifest. All non-ID cells in the 192 newly allocated primary rows are unchanged from the allocation parent after translating provisional references, covering statuses, IDEA dispositions, and LITERATURE coverage labels as well as statements.

## Executed independent evidence

Reproduce from repository root:

```bash
python3 -I topics/programme-ideas-20261031/audit-04-support/allocation-check.py > topics/programme-ideas-20261031/audit-04-support/allocation-results.json
```

The checker reads pinned Git objects rather than trusting a changing worktree. It does not import the developer allocator. After static inspection established that writes start below the default-path early exit, it executed this exact default-only command in two isolated temporary snapshots:

```bash
python3 -I topics/programme-ideas-20261031/pr-prep/allocate.py
```

- Source snapshot `37820a5`, unchanged source script: exit 1 at line 87, `assert not clash`, with all 192 already-allocated IDs listed as clashes. No files added, deleted or changed in the snapshot.
- Allocation-parent inputs `6954664^` (the pre-allocation state), unchanged source script: exit 0; emitted blocks and next boundaries exactly equal the committed JSON. No files added, deleted or changed in the snapshot.

Neither invocation used `--apply`, optimized assertions, rewritten source, or monkey-patching. The current-source failure is expected: lines 82–87 compare proposed IDs against every current registry occurrence without recognizing an already-installed identical mapping. Lines 94–95 stop default execution before the first mutation at lines 98–99. The apply path also assumes pre-allocation headings and no existing Final-ID lines; it was inspected but not run. Making the script repeatable would be developer follow-up, not an auditor repair.

Additional actual commands included `git show --format=fuller --stat 6954664`, the T01 `git diff f4e2133 37820a5`, `nl -ba .../allocate.py`, `rg` checks of primary rows and the authorization log, and `sha256sum` of the source script/map/ledger. An initial `git rev-parse 97968d2` failed because the PR #11 object had not yet been fetched; no Git state was changed by this subagent.

The machine-readable result records every assertion, both complete subprocess outputs, Python version, all source SHA-256 hashes keyed by revision and path, and the source/boundary/baseline identities. It is small necessary audit evidence rather than bulk generated computation output.

| Audited source file | SHA-256 |
|---|---|
| `pr-prep/allocate.py` | `5fe1f97495b797f8fcc53bd92507f9cb68f9b49a870c354f9b7dbb0bf5cc44d4` |
| `pr-prep/id-map.json` | `1b4b6145235ad1b2e1d8f08b7aee65ec52881711e0ca855186ba2afdab503b44` |
| `topics/padua-batch-20261031/ALLOCATIONS.md` | `e8ab49cc91f58761d85c5d1fe5f0d5324e2d422562c5e11e715cae48562086fb` |

## Limits and handoff

This check does not certify other drafts' current reservations beyond exact PR #11 head `97968d2c2d039cb0910e0ea50747fb2d9e01a262`, globally refresh all remotes, approve literature equivalences, or authorize merging. Those live integration and audit-status checks belong to the root integration review. The shared programme registry still contains historical re-audit-pending wording; that wording is not silently treated as a current acceptance receipt here. Accepted scientific statuses have not been upgraded.

Suggested next prompt for AC: "Codex (gpt-6-astra, high): incorporate this allocation check into the focused PR #6 integration audit, preserving the documented one-shot dry-run limitation."
