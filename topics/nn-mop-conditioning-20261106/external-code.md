# External source availability and normalization review — 2026-11-06

Worker: Codex; assigned technical development gpt-6.1-sol medium; serving metadata not independently exposed. Rules/source head `b4a04981d42c7cd872957facf5e3995e4096ca67`. No Git operations or third-party commits by this worker.

## Source identity and current blocker

Required AC archive: `IEP-MOP-main.zip`, 1,020,330 bytes, SHA256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`. The accepted predecessor [G5 receipt](../nn-mop-stability-20261105/g5-run/README.md), [audit](../nn-mop-stability-20261105/audit-g5-01.md), and [complete per-member inventory](../nn-mop-stability-20261105/audit-g5-01/source-inventory.json) pin those bytes; they do not supply the bytes in this workspace. Repository revision of the archive is unknown.

The coordinator's workspace search and this worker's `rg --files /workspace` filename search found no archive/extracted source. The latter does not cover hidden files. `command -v octave-cli` found no executable. Octave installation was not attempted because source execution is blocked independently; installability has not been disproved.

On this turn the supported web connector returned inaccessible/Internal Error for the [public GitLab project](https://gitlab.kuleuven.be/numa/public/IEP-MOP), its main archive, raw `src/utils/kravchuk_exact.m`, and the [SIAM supplement](https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip). Bounded searches for `"IEP-MOP" github`, `"IEP_initial_data.m"`, and `"IEP-MOP-main.zip"` returned no useful source. GitHub fetch rejected the generic repository-search endpoint as unsupported (HTTP400); this is a connector endpoint limitation, not evidence that no mirror exists. No network-policy bypass, proxy removal, contact, or download was performed. Prior shell proxy failure is coordinator evidence, not a new worker shell request.

**Current M4: BLOCKED, not FAIL.** Historical G5 PASS is retained; it is not a new reproduction. **M2: BLOCKED, not numerical mismatch.** No LIT-347 metric table, condition number, or external comparison was run or claimed.

## Fulltext coverage (LIT-347 access addendum, no new LIT identity)

The supported web connector accessed [arXiv v2 fulltext](https://arxiv.org/html/2506.19796v2), 2265 parsed lines, on 2026-11-06. Read relevant fulltext portions: §3.1 equations12–16; §4.2 normalization discussion/equations28–30; all Algorithm2 in §4.3; §6.1–6.2. This is not a claim to read the complete article or authenticate the published PDF/source bundle. The existing [assessment](../padua-literature-20261103/notes/faghih-sinum-2026-assessment.md) was also inspected; its published-paper observations remain attributed there.

LITERATURE, bounded to the portions read: equation14 uses an upper Hessenberg matrix with unit subdiagonal; equation29 converts a nonunit matrix by diagonal similarity. Equation30 permits local products rather than a full accumulated diagonal. Algorithm2 includes monic conversion, while §6.1 retains scaled bases for CORE/REORTH. Equation34 uses relative spectral matrix norm. Section6.2's conditioning error is obtained from a perturbation experiment, not an induced worst-case Jacobian norm. The archive is needed to identify exactly which returned matrices/bases each driver uses.

The HTML Example1 expression and size notation must not override the inspected-source convention in the accepted G5 receipt: that code uses integer nodes0..paperN, hence paperN+1 topic nodes. Likewise reconstruct binomial factors and input preparation from the pinned data functions, not a possibly malformed HTML formula. The local source-family generator includes the binomial factor and normalized nodes. Source fidelity remains M2's job.

## Required restart sequence

1. Supply the exact pinned archive in this executor; verify SHA and all inventory members. Safely extract outside Git and read every executed source file before running.
2. Establish Octave platform and run unchanged predecessor G5 driver/selected paperN10 Kravchuk CORE case against its fixed decade rule. Only actual execution can re-pass M4.
3. Compare local monic reconstruction against pinned `kravchuk_exact`/`hahn_exact` and returned matrices for one configuration to relative1e-12; state node units, path, orientation, scaling and norm. Mismatch kills the LIT metric claim.
4. Only after both pass run requested N4–32 identical-input comparisons. A single step-line matrix omits off-path NN information; obtaining the whole NN triangle requires the additional shifted paths/boundary data. Never fill unobserved NN fields with a reconstruction from insufficient data.
