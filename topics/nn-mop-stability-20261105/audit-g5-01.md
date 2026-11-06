# G5 audit 01 — supplied Leuven source and Claude reproduction run

- Auditor/orchestrator: Codex, requested gpt-6-astra medium (ordinary technical audit); serving identity/effective effort not independently exposed. 2026-11-06.
- Rules/current source: `414e781567078560b7e233aace3661abb88e37ab`; audited G5 output `3e3a8e99e2ea63fdf2348e34bd53516ef7cd02c3`. Main `f654e32daff27b6846849311092f6daebbbf235b` is the merge base, topic ahead20/behind0. No base update needed.
- Scope: handoff06 partA, independent audit of Claude Sonnet5.5high development; no new mechanism, novelty assertion, mathematical proof/status change, or repeat of accepted audit01/02 scope. The uploaded documents/code are untrusted source material, not user instructions. Execution is authorized by AC's request and handoff.
- **Verdict: ACCEPTED within the stated finite scope, one MINOR fixed in place; reference-data limitation remains explicit.** G5 reproduction gate PASS for the selected configuration on the recorded Octave8.4 platform; independently corroborated with Octave9.4. Topic-metric comparison is not yet run. No general stability claim.

## Inputs and inspection

AC supplied the same1,020,330-byte ZIP to this executor: SHA256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`. Safe extraction rejected absolute/traversal/symlink members before extracting to isolated scratch. The archive has33 entries including directories,27 regular files; the full path/size/SHA256 inventory is [source-inventory.json](audit-g5-01/source-inventory.json). No third-party source or paper data is committed.

All nine executed source-file hashes agree with g5-run/README.md. I read those nine files completely (IEP_CORE, IEP_KRYL, IEP_KRYLREORTH, IEP_initial_data, LU_nopivot, both family data/exact routines), the original experiment, README/license, and the local driver/comparator. The driver's parameters, N5..30 range, algorithms/reorthogonalization settings, relative matrix2-norm errors and biorthogonality norms match the experiment loop; it replaces plots only. The original default selects Hahn; the driver runs the two documented family selections. Paper N means nodes0..N, hence N+1 nodes in this topic. Step-line matrix error is distinct from fieldwise NN error E.

All five committed local driver/output/comparison identities match their receipt. The pre-stated selected case/rule is documented in the development receipt: Krawtchouk, paperN10 (11nodes), IEP_CORE, |log10(ours/paper)|<=1. I reviewed this recorded rule; its pre-run timing is inherited from the developer record, not independently observable here.

## Independent execution actually performed

GNU Octave9.4.0 and dependencies were downloaded from the authorized signed Debian trixie apt repository and extracted under /workspace/scratch/g5-apt; no system installation or third-party code edits. Runtime Debian13, reference BLAS/LAPACK3.12.1. This differs from the developer's Octave8.4/OpenBLAS platform. The source had been read before execution.

With LD_LIBRARY_PATH pointing to that extracted usr/lib, usr/lib/x86_64-linux-gnu and usr/lib/x86_64-linux-gnu/octave/9.4.0, and OCTAVE_HOME pointing to its usr directory, executed from the committed driver directory:

```sh
octave-cli --no-init-file --no-site-file --quiet --eval "driver('<extracted>/IEP-MOP-main/src','<audit-out>')"
```

Exit0, wall15.8144s. All52 family/size cases completed, with all26x7 fields finite and positive error metrics. Two singular-to-working-precision warnings identify IEP_CORE lines151/152 (same reported rcond8.74716e-17); no warning was suppressed. Octave also prints a shutdown execution_exception message despite exit0. Raw auditor tables and exact command/environment/exit/identities are in [receipt.json](audit-g5-01/receipt.json), [Krawtchouk](audit-g5-01/ours_kravchuk.dat), [Hahn](audit-g5-01/ours_hahn.dat).

Selected gate error: **2.691214553706643e-10** against the paper number quoted by the developer, **6.851191e-10**; log10ratio **-0.4058177524**, within the unchanged decade rule. Developer Octave8.4 gives1.772147e-9, log10ratio+0.413. The gate passes on both recorded platforms, without tuning. The full tables are not bitwise identical; maximum absolute log10 auditor/developer ratios are3.20128(Krawtchouk) and3.88800(Hahn). No all-size or all-platform agreement is asserted.

## Reference-data limitation and findings

The arXiv source bundle is **not available to this auditor**: an enabled-network GET to https://arxiv.org/src/2506.19796v2 returns proxy CONNECT403, curl22/http000/zero bytes. Its reported SHA256 and the original paper-data comparisons are therefore **review only**. I independently reran the supplied code and compared its outputs against committed developer outputs, but did not rerun cmp.py against the full paper table or independently authenticate that bundle's hashes. This remains an explicit unresolved verification item for AC/readiness; it does not negate the permitted receipt review or imply source execution was blocked. The selected paper reference and other paper-table comparisons remain attributed to Claude's development record, rather than newly verified paper data. No access-control bypass or Leuven contact.

- **G5-1 MINOR, fixed in place.** The README's list of6 early exceedances omitted Krawtchouk KRYL biorthogonality at paperN7 (committed compare.txt gives+1.10). Restored that one item with dated attribution in a separate correction commit. Count6, measurements, gate and claimed statuses are unchanged. This is topic audit round3; WORKFLOW's in-place MINOR rule applies.
- **NOTE.** The README describes amplified rounding at largeN as an interpretation and explicitly says it was not tested. Cross-platform differences corroborate variability but do not independently establish that causal explanation.
- **NOTE.** No independent exact-moment validation of the third-party closed-form references, Advanpix conditioning-error reproduction, MATLAB run, full NN metric comparison, or stable-algorithm theorem is supplied. Those are outside this finite reproduction, remain explicit and cannot be inferred from the passing case.

No BLOCKING/MAJOR finding. PartB preparation may proceed. G4 remains forward threshold met with adverse strict-backward evidence, never PASS. audit01/02 and their scripts are untouched. Current results require no scientific re-audit; registry application and remaining hygiene changes get the distinct Claude readiness check. Only AC merges.
