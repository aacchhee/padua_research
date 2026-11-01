# Response 03: narrow answers to audit-03

- **Developer and orchestrator.** Claude. Configured model `claude-opus-5-5`, requested effort high; the runtime does not expose the serving variant. No subagents were used.
- **Handoff and rules.** [09-response-03.md](handoffs/09-response-03.md). Rules (`AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`) were read at branch head `3cca9b929ac006a5ed4295b3beba909dfd602271`; they are unchanged since `1df5f89`.
- **Audit.** [audit-03.md](audit-03.md): 0 high, 0 medium, 3 low. Audited candidate `ea829d9`.
- **Accepted and not reopened.** Record 06 is PROVED; record 05's factor-ten target is PARTIAL; the MEASURED experiment, the INCONCLUSIVE both-grid test and the OPEN rotQ24 conjunct stand.
- **Not independent acceptance.** These are Claude development fixes. A bounded Codex re-audit follows (handoff 10).

## A03-L1: requested regeneration must require its files. FIXED

**Change.** In `tracks/bivariate-lanczos/code/drift/e1_scalar_finite_check.py`, `check_regenerated`:
- the pass flag now starts from whether the directory exists;
- each absent comparator-upper or reproduction file sets it false and is listed in a new `missing_required` field;
- `directory_exists` is reported;
- the CLI now exits with status 1 whenever `all_pass` is false. The JSON is still written.

Mode without `--regenerated` is unchanged: it checks only the committed certificates. The record-06 Checks paragraph and the README state the new contract. The mathematical reduction is unchanged.

**Fresh regeneration.** Developer executions, not independent reruns. Done 2026-11-01, 18:40:53–18:45:00 UTC; CPython 3.13.18, python-flint 0.9.0, `PYTHONPATH=/workspace/padua-drift-runs/python-deps`, `OPENBLAS_NUM_THREADS=1`. Outputs are in `/workspace/padua-drift-runs/response-03/E1/`, outside Git. All four commands are the record-06/README commands, and all exited 0:

| Output | Command | Wall time |
|---|---|---|
| reproduce-triangle | `e1_reproduce.py --set triangle` | 2.4 s |
| cgs2-triangle-n12-pivot | `e1_cgs2.py --set triangle --degree 12 --rule pivot` | 3.3 s |
| reproduce-rotated | `e1_reproduce.py --set rotated` | 162 s |
| cgs2-rotated-n12-alt | `e1_cgs2.py --set rotated --degree 12 --rule alt` | 243 s, run concurrently |

These runs are separate from the response-02 regeneration recorded in `response-02-e1-scalar-finite.json`. That receipt is unchanged; its file entries show all four outputs present when it was produced. By now the response-02 working directory (outside Git) no longer held `reproduce-triangle.json`, so it was not reused.

**Checker cases.** Receipt: `evidence/response-03-e1-regeneration-check.json` (5151 bytes; result PASS).

| Case | Invocation | `all_pass` | Exit |
|---|---|---|---|
| None | no `--regenerated` | true | 0 |
| Absent | `--regenerated` with a nonexistent directory | false; directory_exists false; all four files in `missing_required` | 1 |
| Partial | directory holding both fresh uppers and `reproduce-triangle.json` only | false; `missing_required = [reproduce-rotated.json]` | 1 |
| Complete | the fresh directory | true | 0 |

In the complete case, both regenerated uppers equal U_T and U_R exactly, and both reproductions PASS with every pin matching.

## A03-L2: scope the reversal to the target it settles. FIXED

In record 05's status table, the rotQ24-conjunct row now:
- names the target, K_BJ > 10 min(K_alt, K_pivot), and the bound conventions L_X² ≤ K_X² ≤ U_X²;
- gives the **proof** condition: L_BJ² > 100 U_X² for some comparator X, since min ≤ K_X;
- gives the **refutation** condition: U_BJ² ≤ 100 min(L_alt², L_pivot²), which needs lower bounds on both comparators;
- scopes the alt-only reversal U_BJ² ≤ 100 L_alt² to the separate named-comparator statement K_BJ > 10 K_alt;
- quotes the audit's logical countermodel (9, 1, 1/10), noting that it is not rotQ24 data.

The original wording is preserved in History. The PARTIAL classification, the MEASURED file status and the INCONCLUSIVE test outcome are unchanged. `directions/E1.md:65` already used the both-comparator DEAD condition and is unchanged.

## A03-L3: qualify IDEA17's outside-span assertion. FIXED

In `ideas-e3-e4.md`, the separation criterion of IDEA?drift-claude-17 now:
- describes the extra information accurately: the independently built extended-precision reference R_(≤p);
- marks the displayed correction −(I−R_(≤p)R_(≤p)^T)q̂_p as taken before normalization;
- states that an external reference does not by itself place the correction or q̃_p−q̂_p outside the stored span;
- quotes the audit's exact orthonormal countermodel (γ_p = 3/5, where both lie in Ŝ);
- makes separation conditional on a recorded nonzero normal component ‖(I−P_Ŝ)(q̃_p−q̂_p)‖, and otherwise counts the step as an in-span (R17a-type) parent change.

Unchanged: the R17a/R17b recipes, the γ guard, H17, the deferred disposition and the no-run/no-novelty statements. The original wording is in History.

This narrows an existing claim and adds no mechanism or novelty statement, so no new full `state/IDEAS.md` gate was run. The response-02 full read of IDEAS, PD-T055, PD-T043 and PD-N013 for this entry still applies.

## Integration and limits

- **Integration refresh.** `integration_check.py` was rerun at the response output commit against main `28aaa20` and PR12 `7f226c1`, the only other open PR; the result is in LOG.
- **Size.** Tracked campaign bytes are 4,577,549, under 5 MB, and no file exceeds 1 MB.
- **Frozen files.** Audits, earlier responses, reports, evidence and handoff bodies are unchanged.
- **Not done.** No final IDs, registry edits or Windows writes were made. Cold-storage delivery of Codex's original ZIP is still pending, separately.
