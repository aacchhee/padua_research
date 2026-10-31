# M3 actual checks and audit handoff

Rules/source commit: `d36722823441dc40c6e19d69a174459348dd309c`. Date 2026-10-31. Developer: Codex, assigned gpt-6.1-sol xhigh. No Git mutations. Inputs are integers N,n; no RNG or seed, no original-source code imports, no network access.

## Executed command and environment

Working directory `/workspace/padua_research`:

```sh
python tracks/mz-constants/code/m3_exact_check.py --max-n 25 --measure 20 40 80 160
```

Python3.12.14, NumPy2.3.5, SciPy1.17.0. Exact component uses standard-library fractions.Fraction. Code SHA-256: `246bd4b95226182b0231730d7ad6ae6d7716623d31b28193c0e44d932825d2dd`. Exit code0; actual stdout:

```text
EXACT: 324 pairs, 2<=N<=25, 0<=n<N: PASS
       filter plateau, degree cutoff, no-alias reproduction, upper Z signs and ratio bound.
script_sha256=246bd4b95226182b0231730d7ad6ae6d7716623d31b28193c0e44d932825d2dd
MEASURED: numpy=2.3.5, scipy=1.17.0
MEASURED: N=20 n=10: lo=1 hi=1 lower=4.32654716522e-05 upper=1
MEASURED: N=20 n=12: lo=0.995388681563 hi=1.00038632766 lower=2.76899018574e-05 upper=1.04
MEASURED: N=20 n=15: lo=0.958382503863 hi=1.00274370981 lower=1.08163679131e-05 upper=1.25
MEASURED: N=20 n=18: lo=0.759706499029 hi=1.0045746175 lower=1.73061886609e-06 upper=1.64
MEASURED: N=20 n=19: lo=0.31813873556 hi=1.00464925515 lower=4.32654716522e-07 upper=1.81
MEASURED: N=40 n=20: lo=1 hi=1 lower=4.32654716522e-05 upper=1
MEASURED: N=40 n=24: lo=0.997585829806 hi=1.00021658462 lower=2.76899018574e-05 upper=1.04
MEASURED: N=40 n=30: lo=0.972073168434 hi=1.00204741354 lower=1.08163679131e-05 upper=1.25
MEASURED: N=40 n=36: lo=0.843516957521 hi=1.00432726553 lower=1.73061886609e-06 upper=1.64
MEASURED: N=40 n=38: lo=0.672344883405 hi=1.00447112072 lower=4.32654716522e-07 upper=1.81
MEASURED: N=80 n=40: lo=1 hi=1 lower=4.32654716522e-05 upper=1
MEASURED: N=80 n=48: lo=0.99839660007 hi=1.00014976666 lower=2.76899018574e-05 upper=1.04
MEASURED: N=80 n=60: lo=0.977622933834 hi=1.00172100828 lower=1.08163679131e-05 upper=1.25
MEASURED: N=80 n=72: lo=0.873279216103 hi=1.0042848555 lower=1.73061886609e-06 upper=1.64
MEASURED: N=80 n=76: lo=0.756229826536 hi=1.0043738561 lower=4.32654716522e-07 upper=1.81
MEASURED: N=160 n=80: lo=1 hi=1 lower=4.32654716522e-05 upper=1
MEASURED: N=160 n=96: lo=0.998736137318 hi=1.00011995269 lower=2.76899018574e-05 upper=1.04
MEASURED: N=160 n=120: lo=0.980110305238 hi=1.00156338328 lower=1.08163679131e-05 upper=1.25
MEASURED: N=160 n=144: lo=0.885951406492 hi=1.00424108885 lower=1.73061886609e-06 upper=1.64
MEASURED: N=160 n=152: lo=0.786957076976 hi=1.00432815161 lower=4.32654716522e-07 upper=1.81
```

No all-N claim is inferred from these measurements. The universal exact formulas, trigonometric kernel estimates and weighted Schur proof are written analytically. In particular, the finite checker confirms plateau/alias/sign obligations in its scope; it does not computer-certify every all-N kernel estimate.

## Runs needed and audit boundary

- Independent actual rerun at the code hash above, plus reconstruction of every all-N proof and constants, particularly n=0, k=n filter plateau, circle versus half-circle factors, and half-open distance-shell counts.
- Confirm local CC-weight dependency PD-T017 is independently accepted under its exact hypotheses.
- Complete historical fixed-ratio weighted-MZ and operator-bound prior-art screen; lack of a matching local registry entry does not imply novelty.

The small output is reproduced here; no generated large artifact or cold-storage claim exists. The orchestrator records pinned theory hashes, final IDs and final acceptance separately. This worker wrote no manuscript and changed no shared registry or Git state.
