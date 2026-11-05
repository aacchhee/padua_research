# Independent native-certificate check — 2026-11-05

Rules/input SHA: `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`.
Codex subagent `/root/replay`, delegated `gpt-6.1-sol` medium technical
effort. No Git mutations or developer source edits. No new mathematical
mechanism or novelty claim: this is independent execution of the existing
PD-T106 pencil and PD-T107 exact finite reduction. The novelty-generation
gate does not apply. The supplementary Astra check and Claude audit remain
separate obligations.

Read the native producer `code/cert_pencil.c` and driver
`code/cert_native.py`, plus the previously read rules, workflow, frozen
definitions, handoff, plan and PD-T107 reduction. The independent checker
`code/independent_cert.py` does not import either producer source.

## Independence and acceptance

The C producer builds rational matrices using GMP modular-fold moments.
This checker reconstructs the whole pencil using Python Fraction and a
separate repeated-reflection alias implementation, independently computes
the product-to-sum entries, and verifies every offblock entry is zero.
It compares every within-block H/Q entry as an exact rational with the C
ASCII file (positive common denominators are checked). It then uses its
own reconstructed matrices and fresh SciPy-proposed integer congruences
at scale 10^13, different from the producer's 10^12. The producer transforms
and floating matrix file are not read.

Acceptance is independently implemented exact signed diagonal dominance:
for each endpoint and block, form the integer congruence of Q−tH, verify
symmetry, and require `2|B_ii|−sum_j|B_ij| > 0`. Count negative diagonal
entries and check full-pencil counts `(0,1,N−1,N)` at the four endpoints.
The analytic implication is exactly PD-T107's Sylvester-inertia reduction.
No floating tolerance is an acceptance premise. Fresh float eigenvectors
only propose integer transformations. Endpoints come from the producer
receipt but must pass the independent exact checks, so they are untrusted
proposals rather than trusted certificate facts.

Independence limits: this checker shares Python, SciPy proposals and FLINT
integer arithmetic with the producer driver, and shares the same
mathematical signed-dominance acceptance predicate. It is a separate
implementation and actual rerun with a different rational reconstruction,
not a different proof predicate. Exact LDL was not attempted; it is not
needed for the existing PD-T107 finite reduction. These checks certify
only the explicitly run degrees; no universal or asymptotic claim follows.

## Actual commands and environment

Working directory `/workspace/padua_research`, Python without `-O`.
Dependency target `/tmp/padua-g0-deps` was installed during G0 (see its
receipt). Commands actually executed:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m60.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m60.json > /tmp/padua-independent-cert-m60.log 2>&1
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m10.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m10.json > /tmp/padua-independent-cert-m10.log 2>&1
for m in 20 30 40; do PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m${m}.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m${m}.json || exit; done > /tmp/padua-independent-cert-baselines.log 2>&1
```

An executed separate import-and-call check tested `signs()` on zero,
boundary-singular, nonsymmetric and indefinite-nondominant matrices; all
four were rejected. `[[-3,1],[1,3]]` was accepted with inertia `(1,0,1)`
and minimum margin 2. Output `/tmp/padua-independent-cert-controls.json`,
copied unchanged to `evidence/independent-cert-controls.json`.
The command actually executed was:

```sh
PYTHONPATH=/tmp/padua-g0-deps python - <<'PY'
import importlib.util,json
from pathlib import Path
p=Path('topics/padua-mz-2d-frontier-20261105/code/independent_cert.py');s=importlib.util.spec_from_file_location('ic',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
cases={'zero':[[0]],'boundary':[[1,1],[1,1]],'nonsymmetric':[[2,0],[1,2]],'indefinite_without_dominance':[[1,2],[2,-1]]};out={}
for name,a in cases.items():
    try:m.signs(m.fmpz_mat(a))
    except ArithmeticError as e:out[name]=str(e)
    else:raise RuntimeError('accepted malformed control '+name)
out['mixed_sign_dominant']=m.signs(m.fmpz_mat([[-3,1],[1,3]]))
Path('/tmp/padua-independent-cert-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
PY
```

Python 3.12.14 (Clang 22.1.3), NumPy 2.3.5, SciPy 1.17.0,
python-flint 0.9.0, FLINT 3.6.0;
Linux-6.18.57-x86_64-with-glibc2.41. OPENBLAS_NUM_THREADS=1 and
OMP_NUM_THREADS=1. No RNG is used. Full command and versions are in each
small receipt; bulk fresh transforms stay under `/tmp/padua-independent-cert/`.
Cold-storage delivery remains pending.

## Source identities (SHA-256)

| Source | SHA-256 |
| --- | --- |
| independent_cert.py | `28228bf2fe412d13c9a581e907aed56385a914b3e51227126b110a9c6b4348cc` |
| cert_pencil.c | `95993b761794306b41b67f6e7741fd9cd38817c08e5ec218c2f21fb08846d51e` |
| cert_native.py | `6651de795706c0e2aa2689a58b9dd928835e2dbe9de0740b237b377d68b095ae` |
| Frozen definitions | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |

## Results

All four PD-T107 baselines passed, with identical exact rational brackets.
Times are actual wall times under concurrent sandbox load, not a controlled
performance comparison.

| m | Dimension | Offblock pairs | H/Q entries compared | Seconds |
| --- | --- | --- | --- | --- |
| 10 | 55 | 750 | 3050 | 0.146 |
| 20 | 210 | 11000 | 44200 | 2.205 |
| 30 | 465 | 54000 | 216450 | 28.772 |
| 40 | 820 | 168000 | 672800 | 24.800 |
| 60 | 1830 | 837000 | 3349800 | 232.594 |
| 80 | 3240 | 2624000 | 10499200 | 569.136 |

| Small receipt | Bytes | SHA-256 |
| --- | --- | --- |
| independent-cert-m10.json | 3850 | `91525efb9dc4da880e4f63fdfc7784553607780430d142c85e441edff7b0b370` |
| independent-cert-m20.json | 4059 | `992f82d553a2310195ad3543874d97584c7d54d1e655863d051b5c3d4dac3137` |
| independent-cert-m30.json | 4260 | `c69afa7dacb0712d8f120fb37459a6e62baf15dff83c3230e6d2ac8b3bbf16c3` |
| independent-cert-m40.json | 4467 | `603124a88c8ca9f22534f4e46c7f553ef8d66d79e7563831911dd99319c3c0f3` |
| independent-cert-m60.json | 4878 | `931f2c632943af1bd5d0772d3d7218f8883d08504c7c7bb2e949d616f4dcae23` |
| independent-cert-m80.json | 5300 | `7b57e74e0e3e919a79262067427e35afa97a637d5d39e0cc17620c93e99cd5fe` |

**PASS m60 independent certification.** The exact strict intervals are
`(188593/1000000,188594/1000000)` and
`(1802011/1000000,1802012/1000000)`. Endpoint inertias summed over the
930/900-dimensional blocks have negative counts `(0,1,1829,1830)` and no
zero counts, respectively. Every independently reconstructed pencil entry
agreed with the C producer. No discrepancy was observed. The independent
finite-execution obligation is met at m10/20/30/40/60; audit and written
claim-level integration remain the orchestrator's separate obligations.

## Additional requested m80 run

After m60 passed, the orchestrator requested m80 if cost remained reasonable.
Observed m60 memory during execution was about 255 MiB; projected m80 cost
was 10–25 minutes / roughly 0.6–1 GiB under shared load, reported before the
run. The observed completed wall time was 569.136 seconds (9.49 minutes).
The memory estimate was low: sampled RSS reached approximately 2.1 GiB
during the second block, because prior FLINT congruences coexist with the
next Fraction reconstruction. This is a sampled observation, not a measured
peak. Available sandbox memory was checked; the run stayed within its
16 GiB limit. The following command completed with exit 0:

```sh
PYTHONPATH=/tmp/padua-g0-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-2d-frontier-20261105/code/independent_cert.py --producer-receipt topics/padua-mz-2d-frontier-20261105/evidence/cert-m80.json --scratch /tmp/padua-independent-cert --output topics/padua-mz-2d-frontier-20261105/evidence/independent-cert-m80.json > /tmp/padua-independent-cert-m80.log 2>&1
```

**PASS m80 independent certification.** All 2624000 offblock pairs were
zero and all 10499200 H/Q entries matched the C producer as exact rationals.
Fresh transforms in blocks of dimensions 1640 and 1600 passed exact
strict-dominance acceptance at each endpoint. The summed negative counts
were `(0,1,3239,3240)`, with no zero eigenvalues at the endpoints, proving
the strict finite brackets `(0.172730,0.172731)` and
`(1.816497,1.816498)` through PD-T107's existing reduction. No mismatch
was observed. The independently checked degree set is exactly
`{10,20,30,40,60,80}`; this is not an independent replay of every integer
below 80. Required audit, registry claims and cold-storage integration
remain separate. No m>100 computation was performed by this worker.
