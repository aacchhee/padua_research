# D3 — completed one-round execution and verification record

Date: 2026-11-12 UTC. Developer: Codex, assigned gpt-6.1-sol high.
Rules/input: `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`.
Root published preregistration at `db8c3cc` and explicitly sent GO before
execution. Code SHA256:
`b8ca61f9c46610f20e81ea234ae6a583b3003095947317951d74cf72fbd780db`.
No code-defect repair or result-bearing deviation occurred.

## Actually executed producer

Working directory `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 450s python -B topics/padua-3d-20261106/code/fd3_certify.py produce --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt topics/padua-3d-20261106/evidence/fd3-producer.json
```

Exit 0. Producer-internal wall time 1.753245 seconds; total recorded
elapsed 1.780589 seconds. Python 3.12.14, numpy 2.3.5, scipy 1.17.0,
mpmath 1.3.0. CPU details were not recorded and no portable timing claim
is made. Cloud runtime was observed connected/running with current
observations and enforced network policy; no network work was needed.

One of the allowed 12 starts was used, seed 20261112. The first candidate
passed after 36 LM iterations: squared Chebyshev residual
4.79234026951179e-31, min weight 0.004704059970944015, max coordinate
magnitude 0.9999235702883306, cubic monomial condition 95.75895306398917.
These numbers are proposal diagnostics only. Three Newton updates on the
fixed 56-coordinate square slice gave residual observations
8.3894e-17, 4.8133e-32, 1.7014e-61, 7.1437e-102, after which the
exact dyadic center/box was passed to the integer checker.

All exact predicates passed: 56 moment equations enclosed by a contracting
interval-Newton selfmap, positivity, strict interior and distinct node
boxes, modular cubic-center rank, rank transfer over the whole box, and
the rational-pair nonlattice obstruction. Exact canonical numerators
are in the receipts; [theory](theory.md) gives the proof and readable bounds.

The separately labelled MEASURED Lambda diagnostic returned
30.012095658454324 on 49791 queries with quality seed 20261113.
No optimization or additional start was performed.

## Actually executed developer certificate replay

```sh
timeout 120s python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt topics/padua-3d-20261106/evidence/fd3-replay.json
```

Exit 0, recorded elapsed 0.211540 seconds. All exact output fields matched
the producer's exact-check section. This mode uses standard-library
integer/Fraction arithmetic; Decimal is solely an untrusted inverse
proposal and its outputs undergo exact interval checking. The developer
replay is not called an independent rerun.

An additional developer Fraction conversion checked the reported strict
bounds q<3/10^17, z<4/10^55, q_V<2/10^17, each weight>47/10000 and
max |coordinate|<999924/1000000 directly against certificate endpoints
and canonical integer numerators. It performed no search or refinement.

## Evidence identities and storage

Machine-readable pins: `../evidence/fd3-manifest.json`.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| certificate | 5574 | 3677318c6dcf793f256750c0f270eb9be8eaa1143534428fcc096e497aa18a7d |
| producer | 2713 | 5033371c0250f6d58fc152c11f61b40afe4328c72d1ede2c0cd58fb3e0161ba3 |
| developer replay | 1433 | 0a6ff66ff4119ae99d004e55ea768338aa2c3c6ecc60b235927665abb5c6c065 |

All generated files are below the approved 32 KiB limit; no bulk outputs
or external archival dependency. The exact certificate and checker
suffice to regenerate the finite predicates without rerunning the search.

## Counter and next verification

D3 round counter **1/1 completed successfully**, unused 0. The search
ends. A distinct Astra xhigh agent's actual frozen replay and separate Fraction
reconstruction both passed, including two modular determinant checks and
four rejected mutations; see [audit](../final-check/d3-audit.md). The
independent-rerun obligation is discharged and the theory is PROVED.
Formal Claude audit: [audit-05](../audit-05.md). This
verification does not authorize further research or quality optimization.
