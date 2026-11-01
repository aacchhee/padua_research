# Codex audit-03 — narrow verification of response-02

Date: 2026-11-01 (Europe/Oslo). **Verdict: CLEAN within the requested scope. A2-L1–A2-L4 are resolved; proceed to PR preparation.** No new finding or additional experiment is required by this verification.

Response candidate: `aea01283ad49d9a4527df727ad386c5f671933ee`. Published response/rules head: `63ffc67f8bc60bd30abcd94769b6aa1d1e783d88`. Audit-02 baseline: `4470ab4857050b3acab114ddcbffc8996d4f2d88`. Current main fetched at `9739a0c56b7a3976422ce60a8441bfbbfd6554df`; integration remains at the previously recorded preparation boundary.

Independent Codex root review and a separate continuing audit worker, distinct from the Claude developer. The worker retains its explicit `gpt-6-astra`, `xhigh` launch configuration; runtime metadata is not independently exposed, and root runtime identity is separately unexposed. Rules were read at the start of this verification and confirmed byte-identical at the published head. The auditors make no developer-science or historical-evidence correction.

## Dispositions

| Finding | Verified correction | Disposition |
|---|---|---|
| A2-L1, T116 bound | Under H_delta the denominator remains `1-kappa*delta`; replacing kappa by B in the numerator is valid. The B-denominator bound explicitly requires `B*delta<1`. The correct Neumann inequalities and CONDITIONAL status are preserved. | **Resolved** |
| A2-L2, T208 zero operator | The unnormalized inequality remains universal. Its quotient is used only for positive operator norm; zero operators contribute zero to the normalized bound. The convention is propagated to the maximum-over-stages definition. | **Resolved** |
| A2-L3, T208 projector evaluation | The numerical aside explicitly rejects a condition-free forward guarantee from backward-stable QR, restricts the modest-error statement to tested near-orthonormal prefixes, retains general conditioning dependence, and does not claim certification. | **Resolved** |
| A2-L4, T318 evidence label | The current theory calls the input an arbitrary perturbed positive-moment functional and expressly says no nonrepresentability test was made or needed. Its explanation of the historical checker/log label preserves the evidence bytes. No positive-measure nonexistence is credited to that check. | **Resolved** |

The three named editorials are also verified: report Rank4 uses the stage maximum; T302(b3) repeats Phi's positive-moment-matrix domain; the L5 driver docstring gives the correct 4–7 size range. No theorem status, failed criterion or OPEN/CONDITIONAL obligation is changed by these edits. The unchanged proofs and empirical scopes retain the preceding audits' conclusions and limits.

## Impact-map and evidence checks

The root inspected every changed file and executed [check_response.py](audit-03/check_response.py); [impact-check.json](audit-03/impact-check.json) records **PASS**:

- All six mapped paths and SHA-256 values match the response candidate and working files. The entire baseline-to-candidate diff consists of those six files plus response-02, LOG and progress bookkeeping; no hidden path is added.
- Exactly four of the 77 theory files changed; the other 73 are byte-identical, and all four overall statuses are unchanged. The published-head delta only pins the candidate SHA in LOG/response-02.
- All audit-01/audit-02 artifacts and handoff records are preserved. Their 130 previously manifested artifact identities still match. The rules, IDEAS, literature registries and SPLITS bytes are unchanged.
- The only code diff is the L5 module docstring. Removing that docstring gives an identical Python AST; the T318 checker/log and all other producer/checker implementations are unchanged.

Actual root execution from `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B -I tracks/bivariate-lanczos/code/L5/analyze_r01d.py topics/bivariate-lanczos-20261031/directions/L5/logs > topics/bivariate-lanczos-20261031/audit-03/analysis-rerun.txt
cmp topics/bivariate-lanczos-20261031/audit-03/analysis-rerun.txt topics/bivariate-lanczos-20261031/directions/L5/logs/analysis_r01d.txt
python3 topics/bivariate-lanczos-20261031/audit-03/check_response.py > topics/bivariate-lanczos-20261031/audit-03/impact-check.json
```

All three commands completed with exit 0. The rerun output is byte-identical, SHA-256 `d295f49b523ea0d81f8cee017186ce7e615d66bbf38fa917bce1aa1a36ff8604`. Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 were used, matching the preceding audit environment. This is reanalysis of unchanged experiment logs, not a new experiment or a status upgrade.

The [independent verification](audit-03/independent-verification.md) separately inspected the full nine-file diff, the statement context and all six hashes. It concurs with every disposition above and explicitly accepts the theory-only interpretation correction for A2-L4. That auditor performed no experiment rerun; the L5 execution above belongs to the root.

The final [artifact manifest](audit-03/artifact-manifest.json) records the small retained verification envelope and cumulative budget check. The earlier broad proof, certificate and numerical suites were not repeated for textual qualifications. No novelty claim or new primary-source reading is involved; prior registry reads are reused after identity checks.

## Next stage

Set **PR — preparation pending**. Canonical source consolidation, main integration, shared-registry/batch-owner coordination, final IDs/crosswalk and integration rehearsal remain the previously recorded preparation work. Material changes introduced there require a focused impact review. The existing mathematical OPEN/CONDITIONAL targets and numerical coverage limits remain explicit; AC retains merge authority.

Suggested next prompt: `Claude (Opus 5.5 xhigh): Continue claude/bivariate-lanczos-20261031; complete the recorded PR-preparation obligations using audit-03's clean response-02 verification, preserve all audit records and scientific statuses, and return material integration changes for Codex review.`
