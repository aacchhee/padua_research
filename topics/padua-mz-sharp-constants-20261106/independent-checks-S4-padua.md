# Independent changed-seed Padua minimum replay

Date: 2026-11-06. Separate Codex checker; requested gpt-6-astra high,
runtime model metadata not independently exposed. Rules/source:
`2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861`.

## Scope and frozen implementation

The coordinator authorized exactly one independent m=3000 minimum
process, using the freed second degree-process slot while the developer's
sequential minimum scan continued. No other degree or upper-eigenvalue
process is authorized by this record. The upper pilot's failure and
earlier K0/dense validations belong to their existing records.

The checker read the complete scan producer, its registered JSON
proposal, and the frozen PaduaOperator implementation before execution.
The independent wrapper asserts these SHA-256 code identities:

- `code/S4_padua_scan.py`:
  `a392135e3a538d90f3d368f8172facabf5c63ab9f941cd0aba2727e5fbe7773b`.
- `topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py`:
  `f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241`.
- `tracks/mz-constants/code/mz2d_spectra.py`:
  `623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76`.

The proposal identity at execution is
`3fc44adc5470e7ab9889fa218fc8b3dd14f6d83895de3638531717213dd6c59c`;
scan registration commit `ec52c16569ea959dfe682fcd7985378a2ef1cd42`.
The wrapper checks the numerical minimum settings explicitly and does
not hash-pin prose. Its extra operator subclass only prints a progress
observation after every twentieth completed matvec; the numerical
operator and scan solver are unchanged.

## Executed command and guards

From `/workspace/sharp-work`:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/check_S4_padua.py --output topics/padua-mz-sharp-constants-20261106/evidence/check-S4-padua-m3000.json
```

The independent process started at 2026-11-06T12:11:20.419114+00:00,
PID5918. It uses seed20261107, distinct from developer seed20261106;
m=3000, n=2999; ARPACK `which=SA`, ncv40, tol2e-11, maxiter20000.
Caps:500 total operator applications,21600 seconds wall,6GiB process
peak RSS. The unchanged scan normalizes the returned vector, recomputes
its Rayleigh quotient and Euclidean residual with another guarded
matvec, and requires finite scalars and

```text
||Av-(v^T Av)v||_2 <= 1e-8*max(1,abs(v^T Av)).
```

That is the actual registered guard; no2e-9 criterion was substituted.
The signed quadrature weights are not clipped. Their sum must differ
from4 by at most1e-11; negative count and mass are recorded. A cap,
solver exception, or failed residual cannot silently become an accepted
partial Ritz value. No vectors or tensor arrays are saved.

The compact receipt records the actual wrapper/source/proposal hashes,
command, timestamps, Python/NumPy/SciPy/platform versions, thread limits,
seed, numerical guards, operator count, memory, wall and CPU time.

## Outcome and comparison

**Completed successfully**, ending at
2026-11-06T12:22:08.847069+00:00. The separate process exited normally
after exactly this one degree and one extreme.

| Quantity | Observed result |
|---|---:|
| Dimension | 4501500 |
| Minimum Rayleigh value | -0.08132259681241015 |
| Recomputed residual2 | 1.2445327705887972e-12 |
| Registered residual guard | PASS |
| Matrix-vector products, including residual evaluation | 102 |
| Wall seconds | 648.4185477430001 |
| CPU seconds | 648.1276188730001 |
| Peak RSS, KiB | 2145492 |
| Sum of weights | 3.9999999999999996 |
| Negative-weight count | 6 |
| Absolute negative-weight mass | 1.1161169679531e-12 |

Environment: Python3.12.14, NumPy2.3.5, SciPy1.17.0, all three listed
thread settings equal one. Wrapper SHA-256:
`25ea2ab9cb046645948c4b905b43a11ab48acc8c1e3448b4bafa0bb512ef78f5`.
Compact result: [check-S4-padua-m3000.json](evidence/check-S4-padua-m3000.json).

At independent completion, the developer's sequential scan had
completed11 rows and was running m=2201, so comparison was initially
pending. The coordinator was told the independent process had finished
and its degree-process slot was free.

### Completed developer comparison

On the coordinator's later signal, the checker read the completed
m=3000 row from `/tmp/sharp-S4/padua-minima-raw.json`. The file then
contained15 completed rows with m=3001 still running; its snapshot
SHA-256 was
`1119a0e9eadc3aedddaaffba952c468e903203bb6f7d0a5bdf25d239514dc389`.
The numerical source/proposal hashes and solver settings match those
of the independent run; the starting seeds differ as intended.

The developer's value is -0.08132259681241012 with residual
1.4226775045102327e-12, seed20261106 and102 matvecs. The absolute
value difference is2.7755575615628914e-17, about3.41e-16 relative.
Both independently recomputed residuals pass the registered guard.
The developer's row is preserved in the comparison portion of the
independent receipt; all original independent timestamps, timings,
resource measurements and source identities remain unchanged.

**Outcome: measured changed-seed agreement.** No new solve or fit was
executed for this comparison. No full-grid acceptance or K4/K5 verdict
is inferred from the incomplete15-row snapshot.

## Interpretation limits

This is an independent execution with a changed starting vector, using
the same frozen numerical implementation. It checks reproducibility
of one new large-grid minimum calculation. Floating residuals and
changed-seed agreement are MEASURED evidence, not an outward enclosure
or a proof that no lower eigenvalue was missed. It is not a new fit,
K4/K5 gate decision, or premise of the analytic S3 limit theorem.

## Complete-data registered fit replay

After the separate complete-data signal, the checker verified all16
minimum rows were completed, had passing residual guards, and used
developer seed20261106. The essential input SHA-256 is
`6d7665a71d4afc42b909deb194596a4fd1873bc7208b2c4673f436d7bfd4cdad`.
The frozen fit producer SHA-256 is
`529ca7a310341e3a30c50446de1d605baf489e4654436fe5285b1553e309cb13`.
The exact registered command was executed separately:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py --essential topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json --output topics/padua-mz-sharp-constants-20261106/evidence/check-S4-padua-fit.json
```

The script was read in full and checked against the registered window,
scaling, rank, condition, sign, magnitude, residual, drift and parity
criteria. The independent receipt's complete result object equals the
developer's result object exactly. A centered-sum reconstruction of
the same OLS slopes also agrees to floating precision; this checks the
same fit and does not introduce an alternative regression model.

| Minimum fit quantity | Even m | Odd m |
|---|---:|---:|
| Window A slope | -0.09145256697320353 | -0.09203829367253583 |
| Window B slope | -0.09216539208358346 | -0.09249333593725202 |
| Relative window drift | 0.7734194953931048% | 0.4919730271431655% |
| Discrepancy from registered -0.1336 proxy | 31.013928081150105% | 30.76846112481136% |

Both parities pass the registered stability conditions. Accordingly
the negative-proxy operational verdict remains **KILL_HEURISTIC_PROXY**;
the check neither relaxes the10% threshold nor reclassifies the tested
windows after seeing their outcome. The final-window parity slope
difference is0.35455943971038355%, giving the registered K5 outcome
**MEASURED_WINDOW_PARITY_AGREEMENT**. This is finite-window agreement,
not a proof of equality of limiting constants.

The upper grid is incomplete after its capped failed pilot, so its
K4 and K5 outcomes remain **INCONCLUSIVE** and no upper fit is attempted.
These numerical gate outcomes, the finite-K128 proxy, and the exact
compact-operator theorem are distinct claims. This replay preserves
the operational rejection without asserting a new asymptotic
explanation or withdrawing an analytic proof on numerical evidence alone.

Receipt: [check-S4-padua-fit.json](evidence/check-S4-padua-fit.json),
including actual command, environment, source/input identities,
unchanged classifications, and independent comparison metadata.
