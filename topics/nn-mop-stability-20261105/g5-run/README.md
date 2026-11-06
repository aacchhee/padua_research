# G5 run — reproduction of one LIT-347 configuration (Claude development)

- **Status:** MEASURED, Claude development; accepted within finite scope by [Codex audit](../audit-g5-01.md), including its direct paper-data verification limitation. This is a finite reproduction receipt. It makes no claim about stability, about MATLAB, or about other platforms.
- **Developer:** Claude, Sonnet 5.5 high subagent, under the Claude Opus 5.5 xhigh orchestrator. Technical-development row of the allocation table. 2026-11-06.
- **Why Claude:** At development time AC had uploaded the source archive only to the Claude session. AC has since supplied the identical archive to Codex, enabling its independent source rerun. The developer/auditor separation is kept by assigning the audit to Codex.
- **Authorization:** AC 2026-11-06, "G5: access is allowed" (canonical LOG entry). No Leuven contact. No access control was bypassed.

## Criterion and the pre-stated rule

handoffs/01-work.md:130: "Before running new problems, reproduce one LIT-347 configuration (one family, one N) to the paper's reported accuracy level. Kill: a mismatch stops G5 until it is explained."

The configuration and acceptance rule were fixed in the run brief before any result was seen:
- **Configuration:** Kravchuk, paper N = 10, IEP_CORE, forward error e_N = ‖H − Ĥ‖₂/‖H‖₂.
- **Rule:** "the paper's reported accuracy level" means the same order of magnitude, |log10(ours/paper)| ≤ 1, because BLAS and platform rounding differ.

## Inputs (third-party; not committed)

**Code.** `IEP-MOP-main.zip`, uploaded by AC.
- 1,020,330 bytes; SHA-256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`.
- MIT licence, © 2024 Robbe Vermeiren / KU Leuven NUMA.
- It was extracted into an isolated scratch directory, and every executed file was read first.
- Executed files and their SHA-256:

| File (in `src/`) | SHA-256 |
| --- | --- |
| algorithms/IEP_CORE.m | `1c58dcc89f65c8f3885efc174773f7113deeacca47f95d9f7856948d1d852acd` |
| algorithms/IEP_KRYL.m | `434415e46af42e7443015836424a99c0400a03647d4805f30b8841a51b435384` |
| algorithms/IEP_KRYLREORTH.m | `4af870386b7afc920e4fb66cce08076d5d7c9bf7c62fdf1888a2c7ee61449e90` |
| utils/IEP_initial_data.m | `29cbe9a8756757cc6573107c5392d31216edbf385960ebcdab8f04d797a93261` |
| utils/LU_nopivot.m | `cc695426ad242421a7e44b01367df47bc5a08fdbcc82257a366acfe36a5415c4` |
| utils/kravchuk_data.m | `3c53e00e3209068d072ad886d5c3171616fdfb7719286a73c9b9e531c8a7d1d8` |
| utils/kravchuk_exact.m | `d776d82f902f7f75de8a1a724495eb236dc27f8320f7faf303b34fb4db0f482f` |
| utils/hahn_data.m | `f22c26e47304e6d4d33fde1cc8661c8335275d87cbee09044db013ea3b4d0fa6` |
| utils/hahn_exact.m | `3e7de6c4423b44d2352e14d42b472efac3cef9a9625f4d3dee6a575acd4d4d03` |

`experiments/experiment_Hahn_Kravchuk.m` (SHA-256 prefix `59afdb58`) was read but not executed. It contains plotting, which the headless driver replaces. `nodes_weights.m` is not called by this experiment; it does not parse under Octave and was not run.

**Paper reference values.** The arXiv source bundle `https://arxiv.org/src/2506.19796v2`.
- 88,273 bytes; SHA-256 `f736e8f03b536382141c2c98620c3cd408e0ff2c772ce58f47030e944864d461`.
- It contains no code. The files used are `Experiments/experiment1/data_experiment1_kravchuk.dat` (SHA-256 `0ae382c8…`) and `data_experiment1_hahn.dat` (SHA-256 `a4ec9d6a…`).
- Columns: N, e_N for IEP_CORE, IEP_KRYL and IEP_KRYLREORTH(full); ‖WᵀV − I‖₂ for the same three; and the conditioning error. N runs from 5 to 30. These are the data plotted in the paper's Fig. "experiment1" (main.tex:1253).

**Size convention.** `kravchuk_data(N,…)` uses the integer nodes 0..N, i.e. N+1 nodes, with p1 = 0.4, p2 = 0.5. Hahn uses β1 = 1, β2 = 1.5, γ = 1. So **paper N ↔ this topic's N+1 nodes**: paper N = 10 is this topic's N = 11. The paper's metric is the 2-norm relative error of the whole step-line Hessenberg matrix. That is not this topic's fieldwise NN metric E, so no cross-metric comparison is made here.

## Runtime and commands

- **Platform:** Ubuntu 24.04. GNU Octave 8.4.0, installed with `apt-get install -y octave`. LAPACK 3.12.0. BLAS is probably OpenBLAS (pthread): the `update-alternatives` link points there, but this was not confirmed from inside Octave. The machine has 4 cores.
- **Driver:** [driver.m](driver.m), SHA-256 `5ea1a2d157ed4d9d2314a064009f68cf72a93e69b194dc5395f681dddb36df12`. It is a headless replica of the experiment loop with the same parameters, the same three algorithms (`IEP_KRYLREORTH(…,'full',1)`) and the same error formulas. It applies no shims and modifies no third-party file.

```sh
cd <dir-with-driver.m>
octave --no-gui --eval "driver('<extracted>/IEP-MOP-main/src','<outdir>')"
python3 -I cmp.py <arxiv-src>/Experiments/experiment1 <outdir>
```

- **Timing:** about 21 s wall (Krawtchouk 10.6 s, Hahn 10.4 s).
- **Warning:** Octave printed one warning, "matrix singular to machine precision, rcond = 8.7e-17", from IEP_CORE.m lines 151–152. Which N triggered it was not traced.
- **Repeatability:** the orchestrator re-executed the driver in a separate output directory, and the outputs were byte-identical. This is a repeatability check on the same platform, not an independent rerun.
- **Outputs (committed, small):**
  - [ours_kravchuk.dat](ours_kravchuk.dat): SHA-256 `e582ce82c398c75da06ae200fec7a088ae04a0ea0cda0e386715ef7ff59ec26a`;
  - [ours_hahn.dat](ours_hahn.dat): SHA-256 `46b52790e89311982f49a26d2c4e7b4c232c67f183551c1d0e81284c3a428632`;
  - [compare.txt](compare.txt): SHA-256 `4b7e182a384244664f228cbb1a4a961f6ef11fb7a63728a620213b1a6c1841ae`, holding the log10(ours/paper) values for every N and column;
  - [cmp.py](cmp.py): SHA-256 `be32ae6c7b182622805e76eaf6a6aad20618fe977268e7f1f67a38cf8bbed260`.

## Result

**Gate (pre-stated rule): PASS.** For Kravchuk, paper N = 10, IEP_CORE, the paper reports e_N = 6.851191e-10 and this run gives 1.772147e-09. log10(ours/paper) = +0.41.

**Full comparison, N = 5..30** (MEASURED):

| Family | Column | max \|log10 ratio\| | N with \|log10\| > 1 |
| --- | --- | --- | --- |
| Krawtchouk | e_N IEP_CORE | 2.56 | 8, 18, 25, 27 |
| Krawtchouk | e_N IEP_KRYL | 3.78 | 23, 24, 26, 27, 30 |
| Krawtchouk | e_N IEP_KRYLREORTH | 2.89 | 19, 21, 23, 26, 28, 29 |
| Krawtchouk | biorth. CORE | 1.46 | 25, 26, 27 |
| Krawtchouk | biorth. KRYL | 3.39 | 7, 23, 25, 27, 30 |
| Krawtchouk | biorth. REORTH | 1.11 | 21, 28 |
| Hahn | e_N IEP_CORE | 2.17 | 18, 20, 23, 26, 28 |
| Hahn | e_N IEP_KRYL | 1.90 | 11, 14, 18, 25 |
| Hahn | e_N IEP_KRYLREORTH | 3.13 | 22, 27, 30 |
| Hahn | biorth. CORE | 2.01 | 28 |
| Hahn | biorth. KRYL | 1.62 | 11, 14, 18, 26 |
| Hahn | biorth. REORTH | 1.39 | 30 |

- **N ≤ 16** (2 families × 6 columns × 12 values of N = 144 entries): 6 entries exceed one decade, by at most 0.62 beyond it. They are Krawtchouk CORE e_N at N=8, Krawtchouk KRYL biorthogonality at N=7, and Hahn KRYL e_N and biorthogonality at N=11 and N=14.
- **N ≥ 17:** exceedances become frequent, up to 3.8 decades. This is where the paper reports that all digits are lost, around N = 15–20 (main.tex:1268), so these values are dominated by amplified rounding, and they are not expected to reproduce to the decade across MATLAB and Octave or across BLAS libraries. This explanation is an interpretation and was not tested.
- **Qualitative pattern:** it matches the paper.
  - IEP_KRYL is the least accurate, and its error grows fastest.
  - IEP_CORE and IEP_KRYLREORTH have similar error growth.
  - The REORTH biorthogonality loss stays near 1e-16 to 1e-15.

## Limitations

- Octave with OpenBLAS, against the authors' MATLAB. Agreement is to the decade only, as pre-stated; it is not bitwise.
- Only one configuration is the gate, as the criterion requires. The remaining table is descriptive and grants no "reproduced for all N" claim.
- The paper's `error_cond` (conditioning-error) column was not reproduced, because it needs Advanpix.
- The exact references `kravchuk_exact`/`hahn_exact` were not independently checked against an exact Fraction step-line computation; the step-line convention was not pinned. Indirect consistency: IEP_CORE and IEP_KRYLREORTH match them to about 1e-15 at N = 5.
- Comparison with this topic's NN metric, or with C4 and the native designs on the same inputs, is the next G5 task. It is not part of this reproduction.

2026-11-06 Codex audit correction (G5-1): restored the omitted Krawtchouk KRYL biorthogonality N=7 entry in the enumeration above; the count6, tables, thresholds and outputs are unchanged. Independent rerun/limitations: [audit-g5-01.md](../audit-g5-01.md).
