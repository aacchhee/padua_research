# Response 02 — developer answers to audit-02

- **Developer and orchestrator.** Claude. The orchestrator ran on the configured `claude-opus-5-5` at xhigh. The developer subagents were:
  - E1: Opus 5.5 xhigh;
  - E3/E4: Opus 5.5 xhigh;
  - E5: Opus 5.5 high;
  - E6: Sonnet 5.5 high.
- **Handoff.** [07-response-02.md](handoffs/07-response-02.md). Rules were read at branch head `1df5f89fe52f62c49d5addd58dcfea7246c5a688`; WORKFLOW changed only by the merged PR16 results rule.
- **Audited scientific response.** `cef79d6`. Audit record: [audit-02.md](audit-02.md), 0 high, 2 medium and 8 low findings.
- **Response commits:**

  | Commit | Content |
  |---|---|
  | `b216cb3` | L8 |
  | `99cc9f9` | E6 |
  | `a7a9b77` | E5 |
  | `20bbb65` | E3/E4 |
  | `b94e5a1` | E1 |

  The candidate for the next re-audit is named in handoff 08.
- **Developer reports.** These give exact lines, commands and pins: [checks/response-02/](checks/response-02/).
- **Not independent acceptance.** These are Claude development fixes. Material proof, status or scope changes need a Codex re-audit. Frozen files are unchanged: audit-01/02, response-01, all reviewer/developer reports and their evidence.

## Dispositions

**A02-M1 — FIXED (record 15).** The asserted equality δ_(A_m)(t)/u → ‖v_m‖ is replaced by display (13): δ_A(t)/u = κ_A‖v_m‖/√(b² + u²‖v_m‖²) → (κ_A/b)‖v_m‖.
- For the forming operator this is ≥ ‖v_m‖, with equality iff κ_(A_m) = b, as in the original T₃/v₂₁ instance (κ_Y = b, squared limit 3/2).
- For a source in v₂₀ the squared limit is 88/15, against ‖v₂₀‖² = 22/5.
- The core (a)–(d), the no-o(u) result and the PROVED status are unchanged. The original wording is in History.
- New exact regression `e4_response02_check.py` writes `evidence/response-02-e4-creator-limit.json`: 25 instances, PASS. It is a developer check. `e4_closure_check.py` is untouched.

**A02-M2 — FIXED (split; status decision for re-audit).** The finite exact scalar inequalities formerly carried in MEASURED record05 are now PD-T?drift-codex-06 (new file `tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md`). It is a precisely scoped computer-assisted PROVED record in record03's formal model (independent formal relative operation errors |delta|<=1, l-infinity source, first-order normal map, spectral output). It contains:
- (a) full-graph comparator uppers K_pivot(T24)² ≤ U_T < 2.4e10 and K_alt(rotQ24)² ≤ U_R < 1.36e10;
- (b) explicit BJ node-sign witnesses K_BJ(T24)² ≥ G_T > 1.57e16 and K_BJ(rotQ24)² ≥ G_R > 8.4e11;
- (c) G_T/U_T = 657331.077… ⇒ K_BJ > 800 K_pivot on T24 (and factor > 10 against the better comparator), and G_R/U_R = 62.0855… ⇒ K_BJ > 7 K_alt on rotQ24;
- (d) G_R/U_R < 100, so these bounds do not settle factor ten on rotQ24.

The written reduction from record03 is: absolute-sum/Frobenius upper, and the attained target-column gain for any sign vector, so validity does not depend on the greedy rule. Thresholds, targets and comparators were chosen post hoc or exploratorily. This is stated as provenance and does not lower the status. No IEEE lower bound, implementation behaviour, exact K or all-degree claim is made.

Evidence and checks:
- Essential evidence (unchanged): e1-scalar-cgs2.json and e1-multinode-certificates.json.
- New exact checker `e1_scalar_finite_check.py` (Fraction only; pins verified; 65 checks plus agreement with the reused independent evidence), output `evidence/response-02-e1-scalar-finite.json`, all PASS.
- Reused independent executions, with their source pins: independent-scalar-01.json, the audit-01 ind_scalar.py run, and the audit-02 E1 reconstruction (audit-02-e1-checks.json).
- New in response-02 (developer execution, not independent): `e1_reproduce.py` on both sets (PASS) and `e1_cgs2.py` for both comparators (exactly equal uppers), 16:42–16:50 UTC.

Record05 keeps the MEASURED experiment, its post-hoc history and the both-grid factor-ten test outcome INCONCLUSIVE, with "Split into: PD-T?drift-codex-06". Its factor-ten target is written out as its two conjuncts and labelled PARTIAL (T24 PROVED in -06, rotQ24 OPEN); the file status stays MEASURED. Original wording is preserved in History. E1/E2 directions and IDEA?drift-codex-05 were updated. The developer agrees with the substantiveness classification, so no disagreement is recorded.

**A02-L1 — FIXED (corrected, and the missing replay executed).** The committed audit-01 `first_principles.py` replays record03's full scalar trajectory only at degree 3 (partC is guarded by `n == 3`); its degree-4 cases run records 01/02 only. Record03 Checks/Open items, record05 Open items, E1/E2 and IDEA?drift-codex-04 now read: degree 3 (audit-01; re-executed by audit-02) and degree 4 (response-02, developer execution, not independent).

The new driver `tracks/bivariate-lanczos/code/drift/e1_replay_n4.py` calls the unchanged audit-01 functions by path (hash-pinned, file not edited) with the seeds the script's loop would use. Results: 20 generic rational nodes, all four rules, 17710 formal operations per case, maximum discrepancy 2.4e-80 at 80 digits, all checks pass. The degree-3 control reproduces the audit-02 receipt field for field. Evidence: `evidence/response-02-e1-replay-n4.json`, run 2026-11-01 16:51:35–16:52:47 UTC (72 s). An earlier identical run, 16:44–16:45 UTC, was overwritten after a one-line no-bytecode change. No degree-12 replay is claimed.

**A02-L2 — FIXED (IDEA?drift-claude-17 stays deferred).** Two nonzero repair arms are now defined; no experiment was run.
- **R17a** is an in-span control against the stored columns strictly before the parent's graded index.
- **R17b** projects the parent onto an extended-precision nested reference basis of the exact span of the monomials through its index. This is the only step where information from outside the stored columns enters.

The degenerate readings are excluded, including the zero repair the audit flagged. The PD-T055 proposal note is aligned. The full IDEAS.md, PD-T055, PD-T043 and PD-N013 were reread for the gate; the verdict is a variant, with no novelty claim.

**A02-L3 — FIXED (record 30).** a₋ = (4π³/9)(5−√2) and a₊ = (4π³/9)(5+√2). The interval, the limit quadratic and the constant 219.5413805… are unchanged.

**A02-L4 — FIXED (record 30).** For a ≤ 0 the statement is now eventual-only:
- for fixed a < 0 the leading limit is positive, so P_n > 0 for all large n;
- at a = 0 the point is the node and P_n = 0.

The fixed-parameter finite counterexample is stated explicitly: a* = 20π³/9 − 512π at n = 4 gives ζ₄(a*) = ζ₄(a) by 2π-periodicity, and Arb-384 certifies P₄ = −0.10421866… < 0. The general form a* = 20π³/9 − 2πn₀⁴ is also stated. The main theorem is unaffected. New checker `e5_response02_check.py` writes `evidence/response-02-e5-checks.json`, PASS. It pins the P_n definition against record 30 and PD-T069, checks the labels exactly, shows the point coincidence exactly (SymPy) and numerically (Arb), and gives a strictly negative ball in two forms.

**A02-L5 — FIXED (record 50, E6.md, e6_offsample.py docstring).**
- Only the iid native-square midpoint has a product triangular density.
- The iid-triangle midpoint has an overlap-area, piecewise-quadratic density.
- The T24/Q24 midpoint sets are deterministic.

The numbers, sample construction and chronology disclosures are unchanged. Because the script's hash is pinned in frozen evidence, it was rerun to `evidence/response-02-e6-offsample-rerun.json`. All 387 compared leaves (370 numeric) equal the frozen response-01 evidence exactly (`e6_offsample_compare.py`). The masked fields are /command, /python (identical value), /elapsed_seconds and /code_sha256.

**A02-L6 — FIXED.** The tested pin is `numpy==2.3.5`, with NumPy ≥ 2.4 excluded, citing the audit-02 probes of 2.4.0 and 2.4.1. It is applied consistently in the README, external-code.md, record 50, E6.md and IDEA55. Upstream is not patched.

**A02-L7 — FIXED.** IDEA57's kill direction is reversed: one target fitted accurately on the same nodes and code falsifies "drift implies every fit fails". The REJECTED disposition, the evidence and the chronology/post-hoc qualifications are kept.

**A02-L8 — FIXED (b216cb3).** The active Windows-results obligations are superseded by the repository-only results rule in proposed-record-changes (the results paragraph), plan:35, report (the remaining-steps paragraph) and COLD_STORAGE.md. The topic results file is `results/padua-lanczos-drift-20261101.md`; its root RESULTS.md section is added only at PR preparation, preserving every other topic's section. Windows cold-storage delivery of Codex's original ZIP and raw files stays a separate pending item. Those files exist only in the Codex workspace, so they must be delivered from there or by AC. Historical receipts and handoff bodies are unchanged.

## Integration refresh

`integration_check.py` was run at head `b94e5a1` against main `28aaa20` and PR12 `146babe`, the only other open PR: PASS (`evidence/response-02-integration-20261101.json`).
- No final assignment of any reserved ID.
- Clean merge-tree with PR12.
- The squash tree equals the head tree.
- The 77 old theory files and protected paths are unchanged.

## Material items for the Codex re-audit

1. **Record 15.** Display (13) and its general form; the IDEA-17 repair definitions.
2. **Record 06** (new PROVED computer-assisted record). Check its reduction, scope, evidence pins and the reuse-versus-new-execution distinction. Also judge **record 05's factor-ten target label PARTIAL** (T24 conjunct PROVED in -06, rotQ24 conjunct OPEN). The handoff asked to keep the both-grid factor-ten verdict INCONCLUSIVE: the test outcome stays INCONCLUSIVE and record 05's file status stays MEASURED. The target is written as its two conjuncts so the split follows the PARTIAL rule. If the re-audit prefers OPEN, the change is one label.
3. **Record 30.** The a ≤ 0 eventual-only wording and the counterexample.
4. **Record 50.** The midpoint-law wording and the rerun equality.
5. **Degree-4 replay.** The replay and the corrected coverage statements.

## Remaining uncertainty

- New checks are developer executions. Independence rests on the earlier audit reconstructions cited in each record.
- Codex's original artifacts are not yet in Windows cold storage.
- No degree-12 trajectory replay, IEEE realization, all-degree theorem, general staircase safety, PD-T055, U2 or reading (G) is claimed.
