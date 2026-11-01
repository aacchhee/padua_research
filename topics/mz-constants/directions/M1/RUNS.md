# M1 executed checks and handoff

Rules/source commit: `d36722823441dc40c6e19d69a174459348dd309c`. Date: 2026-10-31. Developer: Codex, assigned gpt-6.1-sol xhigh; no Git mutations by this worker. Worktree has concurrent disjoint development; the exact code hash below pins this run. All generated output is the small text reproduced here, with no large artifacts requiring cold storage.

## Executed command

Working directory `/workspace/padua_research`:

```sh
python tracks/mz-constants/code/m1_exact_check.py --max-n 40 --float 2 3 4 5 6 10 20 40 80 160 320
```

Environment: Python 3.12.14 (separately executed `python --version`), numpy 2.3.5, scipy 1.17.0; exact component uses standard-library `fractions.Fraction`. No RNG, seed, supplied-code import, external theorem or network access. Input is integer N alone. Checker SHA-256: `7a9b32260a90684e16fcd023e031fd3b91d5ea21ecce2ff351bbc034d68552e3`.

Actual result, exit code 0:

```text
EXACT: N=2..40: defect, support/sign, Z-matrix, telescoping floor,
       weight bracket and full-degree obstruction checks PASS.
EXACT: N=5, row 2 unweighted diagonal-dominance margin = -2/35.
script_sha256=7a9b32260a90684e16fcd023e031fd3b91d5ea21ecce2ff351bbc034d68552e3
MEASURED: numpy=2.3.5, scipy=1.17.0
MEASURED: N=2: lambda_min=1, lambda_max=1, bound=1.68169011381621
MEASURED: N=3: lambda_min=0.625, lambda_max=1, bound=1.78779340921081
MEASURED: N=4: lambda_min=0.583333333333334, lambda_max=1, bound=1.8408450569081
MEASURED: N=5: lambda_min=0.508571183968259, lambda_max=1.00558897228174, bound=1.87267604552648
MEASURED: N=6: lambda_min=0.4850147194475, lambda_max=1.0091259055525, bound=1.8938967046054
MEASURED: N=10: lambda_min=0.39943363754825, lambda_max=1.00559088513866, bound=1.93633802276324
MEASURED: N=20: lambda_min=0.318138735560395, lambda_max=1.00464925515136, bound=1.96816901138162
MEASURED: N=40: lambda_min=0.259849024875495, lambda_max=1.00447112072207, bound=1.98408450569081
MEASURED: N=80: lambda_min=0.216153284009019, lambda_max=1.00443973472925, bound=1.99204225284541
MEASURED: N=160: lambda_min=0.182490276565944, lambda_max=1.00443910138807, bound=1.9960211264227
MEASURED: N=320: lambda_min=0.156015183642122, lambda_max=1.00443780095773, bound=1.99801056321135
```

These finite measurements illustrate the gap between the simple theorem and the apparent sharp constant. They do not establish a limiting constant. The exact finite checks support identities, but the universal proofs are written analytic arguments and are not computer-assisted extrapolations.

## Exploratory runs actually executed

Before writing the checker, an inline Python/numpy/scipy calculation of matrices for N in {2,3,4,5,6,10,20,50,100} measured the largest generalized eigenvalue, row-dominance margins, row sums and maximum off-diagonal entry of A=2M−R. It found every sampled off-diagonal nonpositive; the row-dominance margin was negative from N=5 in that sample. N=5 gave approximately −0.05714285714285716. The durable exact checker supersedes this exploratory output with the exact −2/35. That inline exploratory code is not used as a proof or independent rerun.

The environment tool was called and reported an enforced restricted network policy and no outbound identities/secrets. No network command was used by this worker. The cloud-runtime skill was read at task start. `python` imports reported numpy 2.3.5, scipy 1.17.0, sympy 1.14.0; sympy is not needed by the checker.

## Runs needed / audit boundary

1. Independent auditor: actually rerun the exact checker at the pinned hash and independently reconstruct every all-N proof, including the N=2 edge and the i=0 floor normalization. Merely reading this output is not a rerun.
2. Finish the historical prior-art screen for exact CC upper constants below two. The empty repository registry does not establish novelty.
3. Sharp limiting lambda_max near 1.004437 remains OPEN and is queued; no numerical proof is requested or implied.

The orchestrator records audited hashes and subsequent integration status separately. No final IDs, shared registry acceptance, or manuscript gate is changed by this run.
