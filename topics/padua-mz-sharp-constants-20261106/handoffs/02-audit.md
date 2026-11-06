# Handoff 02 — substantive audit of sharp MZ operator limits

- Status: done in ed5acba02fa30eba7ca6c22b2e41b19c86792ba7
- Previous handoff: [01-work.md](01-work.md)
- Next agent / model / effort: Claude, Opus 5.5 xhigh.
- Role: independent substantive auditor; this is the first Claude audit of this batch.
- Branch: codex/padua-mz-sharp-constants-20261106
- Input head SHA: `5110954b07fd834982167780daa8cd22bef13ce1` (the output commit, distinct from this handoff's publication commit).
- Base main: 76ba4214b100c86a44941f5e9a662ce9ce48efb8. Root read rules at2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861; read current rules and agents/claude/CLAUDE_ROLES.md before acting.
- Stage: AUDIT
- Written by/date: Codex coordinator, gpt-6-astra high requested; serving metadata unexposed;2026-11-06.

## Objective and inputs

Audit the mathematical results, exact original-target scope, retained mechanisms, computed observations and provenance of [draft PR31](https://github.com/aacchhee/padua_research/pull/31). Read [report](../report.md), [LOG](../LOG.md), [gates](../gates.md), [rounds](../rounds.md), [manuscript proposal](../manuscript-insert.md), own results file, complete state/IDEAS.md and literature/INDEX.md, then the full shortlisted entries and linked theory. This is novelty/mechanism-bearing work; the complete novelty registry read is required. The bounded literature screen makes no exhaustive priority claim and explicitly reports unread classical sources.

All final IDs remain provisional, with no reservation. Shared registries and the manuscript are untouched. Evaluate whether each exact operator characterization meets its original target's value requirement, separately from validity of the proved mathematical statement and unperformed certified decimal evaluations. Do not silently narrow the original question.

## Claims requiring full independent reconstruction

1. S1: theory/S1-volterra-model.md and theory/S1-sharp-one-sided.md. Check exact parity-reflected degree cancellation, weights, pole-pairing bound, uniform cotangent error through the diagonal, oscillatory Jacobian factor, density and order of limits. The conclusion is only limsup(logN)^2 lambda_min<=pi^4/8, through all integers and each parity. No matching lower constant or minimum-limit existence is claimed. The equality model was operationally rejected; do not reopen its stopped route in this audit.
2. S2: theory/S2-uniform-upper.md, S2-eta-deficit.md, S2-endpoint-model.md, S2-fixed-trial-limit.md, S2-qualitative-limit.md and S2-finite-certificate.md. Challenge R=M−H+K signs, positive H, PD-T015 floor, both-parity constants, full critical-energy core density, weak two-endpoint profiles, compact K/Fatou H and escaping mass. Then verify all quantitative certificate constants, finite lower clipping/computability and epsilon_N convergence. Exact limit isLambda_edge,1<=Lambda_edge<=3/2, uniform all-N upper5/3. No finite certificate matrix was solved; finiteJ512 decimal is only MEASURED. A practical elementary rate/certified decimal interval is not claimed.
3. S3: theory/S3-normalized-carrier-improvement.md, S3-carrier-family-ceiling.md, S3-full-form-log-model.md, S3-corner-kernel-hard.md and S3-corner-operator-limit.md. Verify whole-grid signed strip error and exceptional term, CC floor/tensor conversion, elementary Legendre/Bessel error and every cross-corner phase, arbitrary-shell normtail120/K, signed finite Gram continuity, exact two identical active blocks, inactive zero coefficients, zero padding/dimension range and explicit finite-m comparison. Exact limiting constants are inf/sup spectrum ofB, equal across parities, with strict signs from accepted carriers. The inherited-family ceiling is only for fixed admissible parameters, not broader packets or finite-m slopes. FiniteK128 decimal proxies have no rigorous infinite-tail numerical accuracy.

Distinct Codex supplementary reports reconstruct these proofs and include actual numerical reruns. They are inputs, not a replacement for this substantive Claude audit. Development allocation, the separately developed Astra-ultra kernel, stopped S1 hard allocation, minor wording corrections and exact reviewed identities are recorded in LOG and independent-checks*.md.

## Computation and gates

Read all registered criteria and the final gate dispositions without changing thresholds or discarding failed receipts. The negative Padua slopes near−0.092 are stable within both parities but operationally reject the finiteK128−0.1336 proxy by31%; finite-window parity slopes agree, while the upper pilot was capped/inconclusive. The exact B theorem predates those fits and its decimals remain uncertified. Audit this discrepancy critically rather than hiding it or treating finite-window stability as a proof of asymptotic bias bounds. The bounded check in independent-checks-S3-transfer-diagnostic.md finds no tested normalization mismatch and observes a substantial full-form correction on selected trial vectors; it does not resolve the full minimum branch or undo the gate failure. No post-gate model revision was attempted. K0's original criterion and dated finite-norm clarification are preserved. K1/K2/K3 and final K4/K5 outcomes must remain MEASURED/operational, not proofs or refutations of the exact limiting theorems. Source model registration was saved before model computation; publication chronology is disclosed. No final Padua slopes informed the exact model.

Choose meaningful independent reruns. Reproduce consequential fast computations and selected large cases rather than automatically rerunning every expensive point. Commands below run from the full published handoff head; audit scientific outputs at the input SHA (code/data are unchanged by handoff publication). Use independent /tmp outputs and single-thread BLAS. Code/input hashes and finite scopes live in the committed receipts. There is no required off-machine raw artifact: complete essential numerical rows support all fit replays.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python topics/padua-mz-sharp-constants-20261106/code/evidence_manifest.py --checks
python topics/padua-mz-sharp-constants-20261106/code/S4_k0_replay.py --suite cc --output /tmp/mz-audit-k0-cc.json
python topics/padua-mz-sharp-constants-20261106/code/S4_k0_replay.py --suite carrier --output /tmp/mz-audit-k0-carrier.json
python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/mz-audit-k1.json
python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/mz-audit-k3.json
python topics/padua-mz-sharp-constants-20261106/code/S2_model.py --output /tmp/mz-audit-upper-model.json
python topics/padua-mz-sharp-constants-20261106/code/S3_corner_model.py --orders 128 192 --cuts 16 32 64 128 --output /tmp/mz-audit-corner-model.json
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py --essential topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json --output /tmp/mz-audit-padua-fits.json
```

Inspect script help before any optional large eigenvalue replay. The failed m800 upper pilot already hit its2000matvec cap; do not retry or launch an upper campaign. The separately executed changed-seedm3000 minimum checks the developer value. No Syvert use is authorized by this audit handoff. Retain the existing6h/run and cumulative48CPUh ceiling if further authorized local runs are needed; stop and report a concrete limitation rather than silently expanding resources.

## Publication, records and expected output

Write audit-01.md with exact candidate SHA/hashes, full files/novelty scope actually read, commands actually executed, findings BLOCKING/MAJOR/MINOR/NOTE and residual uncertainty. Do not modify scientific claims/assumptions/code/evidence in place while counting that as independent acceptance. Preserve disagreements for AC. This is one substantive audit batch; re-audit only material fixes, following current workflow. No registry allocation/readiness or merge is requested at this step.

Commit the audit outputs first, then close this handoff's status and add the next numbered handoff for response or PR preparation in a following commit, preserving old bodies. Only AC merges. The branch, own topic/results file and audit records are the write scope; do not touch another campaign, main, tags, workflows or settings. Use existing publishing authorization. AC explicitly permits the connector's GitHub noreply author email; do not ask again. Existing temporary10MB aggregate allowance and normal per-file discipline are canonically linked in LOG. No unrelated cleanup is authorized or needed.
