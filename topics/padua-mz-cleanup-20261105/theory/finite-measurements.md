# PD-T?mz-cleanup-codex-05 — finite minimum scans and logarithmic diagnostic

ID kind: PD-T. Aliases: even crossing window; odd-window sign probes;
higher-window slope comparison. Split from: C1/C3 measured observations,
separate from the computer-assisted finite theorem and analytic growth bounds.
Split into: none.

## Statement and status

**MEASURED**, not a computer proof:23 completed minimum-only eigenvalue
observations at n=m-1, with the exact grids in attempts/C1.md and gates.md.
The local even scan gives positive0.00012076189285820084 at m1238 and
negative-0.000027148072763036893 at1240. All even integers1230..1240
were scanned. All six odd probes1101,1201,1241,1281,1401,1601 are
negative. No spectral monotonicity, smaller-degree positivity or global
first crossing is established. The certified witnesses at1101/1240/1600
belong to the separate PD-T?mz-cleanup-codex-01 record.

The predeclared higher grid completes with:

| m | minimum Rayleigh value | residual 2-norm |
|---|---|---|
| 1600 | -0.02341441659034573 | 1.9496e-13 |
| 2000 | -0.04393586815914023 | 2.2836e-14 |
| 2400 | -0.06073249283457495 | 3.0020e-15 |
| 3000 | -0.08132259681241004 | 1.6109e-15 |

Least-squares fitting y=alpha+beta log m gives beta=-0.091530043047304
on800/1000/1200/1600 and beta=-0.09212159619973995 on1600/2000/2400/3000.
Maximum residuals are3.2222e-5 and1.7599e-5. Distances from raw-1/9
are0.0195810680638071 and0.0189895149113712, so the preregistered
diagnostic says **moves toward raw-1/9**. Raw-1/9 is an unnormalized
carrier-energy optimum, not an established spectral constant. This fit
neither identifies a limit nor supplies any proof premise.

## Definitions, assumptions and dependencies

Frozen signed Lebesgue Padua even checkerboard, unnormalized dxdy and
orthonormal product Legendre basis of total degree at most m-1. Copied
matrix-free PaduaOperator is unchanged from main21dbfc9; the imported
frozen spectra/definitions are included in the small evidence inventory.
NumPy2.3.5, SciPy1.17.0, Python3.12.14; seed20261105, eigsh tolerance
2e-11, ncv40, one BLAS/OMP thread. Floating arithmetic is unvalidated.

## Evidence and reproduction

The compact evidence/scan-summary.json records every executed row,
vector identity, residual, time, command, code hash, raw receipt identity,
historical baseline identity and fit coefficients. The minimum runner's
legacy exploratory_scope field is inherited unchanged; this topic's
plan/gates establish its prospective scope. Historical baseline rows are
the accepted parent MEASURED record PD-T300, not newly executed m1000.

The final summary command actually executed from repository root:

```sh
python topics/padua-mz-cleanup-20261105/code/summarize_scans.py --scratch /tmp/mz-cleanup --output topics/padua-mz-cleanup-20261105/evidence/scan-summary.json
```

Raw outputs and vectors are in the two manifested local packages;
delivery to AC's Padua cold storage is pending. All jobs completed in the
sandbox, no other machine was used, and no numerical job remains active.
The largest individual completed solve was m3000 at648.397s, below the
four-hour allowance. All measured claims remain subject to required
Claude review; no independent rerun of all23 float scans is credited.

## Open items and history

First crossings, global positivity ranges, monotonicity, sharp growth
limits and opposite-direction logarithmic bounds remain open. No novelty
or historical-priority claim is added. This is the planned diagnostic,
not a newly generated mechanism.

2026-11-05, Codex, gpt-6.1-sol xhigh; rules ad503cb; base21dbfc9 with
unrelated aff30e8 integrated. Measurements were recorded only after each
actual execution; the higher-window grid and fit rule were written before
any m>1600 run.
