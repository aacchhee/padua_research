# Focused independent check — PD-T376 witness regeneration

- Auditor: Codex, gpt-6-astra high (inherited configured assignment; serving metadata not separately exposed), 2026-11-14.
- Rules/input head: `9705c75876a74ac6bcce5625d20a45e3676c1992`. Read AGENTS.md, WORKFLOW, the Codex role and handoff 08. Scope is B.1 only: fresh reconstruction and sign checks of the existing three finite witnesses. No new idea, mechanism, novelty claim or theorem status is introduced; no new complete IDEAS read is needed for this unchanged-evidence scope.
- Frozen scientific code: `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`. The current branch's `g1_minimum.py`, `g1_spectral.py`, `rigorous_witness.py`, `independent_witness.py`, and imported `tracks/mz-constants/code/mz2d_spectra.py` were compared byte-for-byte with `git show` at that commit: all five are identical. Actual runs use those real files in the topic clone; no reconstructed implementation or receipt is substituted.

## Verdict

**PASS.** Fresh eigensolves at m=1101,1240,1600 reproduce all three original source-vector SHA-256 values. The exact dyadic producers reproduce all three decompressed witness payloads and exact-norm files byte-for-byte. In this runtime even the original gzip-container identities agree. Both the producer and independently written forward-error checker accept a negative energy at every degree, with positive continuous norm. The numerical/proof-relevant fields agree with the original committed receipts.

The prior audit's absent-input replay limitation is therefore resolved **for these regenerated inputs in this execution**. This worker does not assert delivery to AC, creation of a deposit, the identity of an inaccessible uploaded ZIP, or completion of the rest of the pack/readiness audit. Those are the orchestrator's separate checks.

## Actual independent execution

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0 / FLINT 3.6.0; Linux/glibc and exact code/input hashes in [readiness-witness-replay.json](readiness-witness-replay.json). `PYTHONPATH=/tmp/mz-python` supplies python-flint; all three BLAS thread variables were set to 1. Developer regeneration receipts were read for comparison but their artifacts were not reused.

Commands executed from the repository root:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PYTHONPATH=/tmp/mz-python
python topics/padua-mz-cleanup-20261105/code/g1_minimum.py --m 1101 1240 1600 --output /tmp/mz-readiness-data/audit-receipts/scan.json --vector-dir /tmp/mz-readiness-data/source-vectors
```

For each M in 1101,1240,1600, separately executed after its vector was written:

```sh
python topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m "$M" --vector "/tmp/mz-readiness-data/source-vectors/m$M-n$((M-1))-min.npy" --scratch "/tmp/mz-readiness-data/witnesses/cert-m$M" --output "/tmp/mz-readiness-data/audit-receipts/producer-m$M.json"
python topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness "/tmp/mz-readiness-data/witnesses/cert-m$M/witness.json.gz" --output "/tmp/mz-readiness-data/audit-receipts/independent-m$M.json"
```

The scan and the per-degree certificate pipeline overlapped after a vector became available; individual producer/checker commands were sequential per degree. Stdout/stderr logs remain in the same local audit-receipts scratch directory. All seven substantive commands exited 0. The original vectors were not acceptance premises of the exact sign checker; they only selected the exact polynomials.

The retained 8.5 KiB [summary receipt](readiness-witness-replay.json) was produced by [summarize_witness_replay.py](summarize_witness_replay.py), executed with `PYTHONPATH=/tmp/mz-python`. It fatally asserts the three independent identity tests (source vector, decompressed exact JSON, exact norm), negative producer/checker signs, positive exact norms, checker acceptance and receipt agreement; it does not rely on the pack verifier's optional nonfatal regeneration warnings. Source/code hashes and the actual argv are recorded there.

## Mathematical and comparison scope

The numerical eigensolve remains a MEASURED proposal only. Exact dyadic integer coefficients define the polynomial. The producer computes the rational Legendre norm and uses outward Arb node tables, fixed-point integer tensor products and explicit propagated errors to prove the signed energy negative. The separately written checker uses independently constructed ball node tables and binary64 contractions with analytic l1 forward bounds. Its acceptance retains the documented IEEE round-to-nearest/standard BLAS dot-product gamma_k model and underflow allowance. This execution reuses the previously audited mathematical reduction and unchanged code; it does not claim a new theorem or wholly independent arbitrary-precision arithmetic implementation.

Original comparisons use `topics/padua-mz-cleanup-20261105/evidence/witness-producer-mM.json`, `witness-independent-mM.json` and `witness-payload-identities.json`, not merely this topic's later regenerated receipts. The exact norm hashes are also checked against the original producer receipts. The comparator ignores runtime paths/timings/versions and container metadata; this worker additionally checks sign, `accepted`, exact norm positivity and all three decisive content identities explicitly. No source-vector-ignore option was needed for these fresh `--vector` runs. Scope of the comparator itself and its other pack ignore options belongs to the separate pack review.

## Available local outputs and limits

All three source vectors are in `/tmp/mz-readiness-data/source-vectors/`. All exact witness gzip/norm pairs are in `/tmp/mz-readiness-data/witnesses/cert-m1101`, `cert-m1240`, `cert-m1600`; the orchestrator may copy these closed files into the independently rebuilt pack. Fresh scan/producer/independent receipts and logs are in `/tmp/mz-readiness-data/audit-receipts/`. Full outputs remain regenerable local working evidence, not committed bulk data or a new claimed cold-storage delivery.

No Git state, manuscript, theory record, earlier audit or developer receipt was edited. No additional mathematical finding was found in this bounded reconstruction task. The half-exactness threshold, first crossing and other open asymptotic questions are unaffected by reproducing these three finite directions.
