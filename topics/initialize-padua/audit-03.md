# Audit 03 — focused check of response-02 and AC's L5 decision

- Auditor: Claude, independent auditor; Opus 5.5, high effort, the same session configuration as audits 01–02. Protocol check.
- Date: 2026-10-31.
- Rules read at: `1533b58836c2ff33da83903e7a0823d8bcf0e6ec` (branch head; the rules changed in this commit).
- Audited candidate: `1533b58836c2ff33da83903e7a0823d8bcf0e6ec`, compared with `c314ca6e105b3128656c34875e358e71c98946be`. Base `b2ec85f3fb2743a3b9292657fec9ac9da227d410` is still current `origin/main`.
- Read coverage: `response-02.md` in full; the full diff `c314ca6..1533b58` across 10 files: `WORKFLOW.md`, both role files, `THEORY.md`, `IDEA.md`, `PROOF_STATUS.md`, `state/IDEAS.md`, `tracks/README.md` and `LOG.md`.
- Novelty scope: not applicable. Only protocol and schema changed; the registries are still empty.
- Verdict: **ACCEPTED** for the declared scope, the initialization scaffold. Two non-blocking items, S1 and S2, are recorded below for AC. The topic moves to stage PR.

## Checks actually run

| Check | Result |
|---|---|
| `git diff --check c314ca6 1533b58` | Pass |
| `git diff --quiet c314ca6 1533b58 -- audit-01.md audit-02.md response-01.md` | Exit 0; the historical records are unchanged |
| Link walk over all `*.md` (inline code removed) | 26 Markdown files, 41 relative links, 0 broken. Matches response-02 |
| Scan of operative files for the old broad PD-N rule and the "administrative / not applicable" exception | None left. The remaining "not applicable" hits concern novelty gating and are correct |
| `PROOF_STATUS.md` table | 8 header columns and 8 separator columns, including `Disposition / reason` |
| `git log -1 --format=%B 1533b58 \| git interpret-trailers --parse` | Both `Agent:` and `Model:` parse |
| `ls .github` | Absent |

## Dispositions

| Finding | Verdict |
|---|---|
| R1 | **Accepted.** Minor routine steps are excluded from aggregation and never make an OPEN statement PARTIAL (`WORKFLOW.md:63`). PARTIAL now requires an explicit decomposition of the target's own statement (conjuncts, cases or ranges), with the proved parts split off by ID and the rest OPEN (`:52`, `:65`). Supporting lemmas alone leave the target OPEN. Line 67 limits the PROVED-plus-OPEN exception to that decomposition. The same rule is mirrored in both role files, `THEORY.md:24` and `PROOF_STATUS.md:9`. I tested the cases: minor proved step + OPEN main → OPEN; split-off proved case + OPEN remainder → PARTIAL; supporting lemma + OPEN target → OPEN; split-off proved part + CONDITIONAL part → CONDITIONAL. Each case has exactly one reading, consistent with Addendum A |
| R2 | **Accepted.** `PROOF_STATUS.md` has a `Disposition / reason` column. A refuted registered claim must show `REJECTED: refuted (see PD-Nnnn)`, and readers must check the disposition before relying on a row (`WORKFLOW.md:71`, `PROOF_STATUS.md:11`) |
| R3 | **Accepted.** The irregularity is recorded in `LOG.md`, history is not rewritten, and the new commit's trailers parse |
| I3 | **Accepted** (`tracks/README.md`) |
| I4 | **Accepted.** The duplicate field is removed. The "not applicable" status is no longer needed under L5 |
| AC L5 | **Accepted, consistent across the repository.** PD-N is limited to refuted or failed mechanisms with a scoped negative statement. Equivalent or abandoned candidates stay as IDEA dispositions and get no PD-N allocation (`WORKFLOW.md:73`, `state/IDEAS.md:11`, `THEORY.md`, `IDEA.md`, `tracks/README.md`, both role files). AGENTS' requirement to keep every considered candidate is still met through the IDEA registry |
| I2 | Closed by AC's decision; no agent action |

## Non-blocking items for AC

### S1 (Low) — The new disposition reason `failed` has no definition

Location: `WORKFLOW.md:71`, `THEORY.md:30`, `IDEA.md:18`.

The reason list has grown from `refuted | equivalent | abandoned` to `refuted | failed | equivalent | abandoned`. This follows the wording of AC's L5 decision ("refuted/failed mechanisms"), but `failed` is never distinguished from `refuted`. The risk is that someone records a registered `PD-T` target as `REJECTED: failed` after one proof route breaks down. `WORKFLOW.md:39` forbids exactly that ("A failure of one proof route does not reject a theorem…").

A one-sentence definition would remove the risk, for example:
- `refuted`: the claim's negation is established within a stated scope.
- `failed`: a mechanism or candidate is shown not to achieve its stated aim under stated hypotheses and range. It applies to candidates and mechanisms, never to a theorem whose proof attempt failed.

This is not blocking, because no record exists yet that could be mislabelled. AC can choose either option:
- Fix it now. That is a rule change, so it needs one more focused check.
- Fold it into the first charter topic.

### S2 (Info) — The disposition list does not cover deferred candidates

Location: `IDEA.md:18`.

`AGENTS.md:19` and `WORKFLOW.md:37` require keeping deferred candidates. `Disposition reason` offers only rejection reasons, so a deferred idea has no value to record. Adding `deferred (not rejected)` would close the gap. It can be fixed together with S1.

## Remaining uncertainty

The rules are consistent as text. Whether they work in practice, especially the substantive-vs-minor classification and the decomposition test for PARTIAL, will show only in the first real research topic.

## Readiness

There is no unresolved blocking finding within the declared scope. The stage moves to PR. The developer completes PR preparation: the PR description, and marking it ready when appropriate. Shared state needs no further update: `state/CURRENT.md` is already accurate for after the merge, and there are no registrations or allocations. Only AC merges, by squash. Readiness does not authorize a merge and does not widen the scaffold's claims.
