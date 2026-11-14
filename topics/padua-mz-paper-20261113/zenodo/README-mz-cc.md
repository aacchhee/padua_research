# Evidence for "Marcinkiewicz–Zygmund constants of Clenshaw–Curtis quadrature beyond half-exactness"

Andrey Chesnokov. Supplementary code and data for the paper (MZ-CC).
Source repository: https://github.com/aacchhee/padua_research, commit `{COMMIT}`.
[Paper reference and DOI: to be added by the author.]
Licence: GNU Affero General Public License, version 3 or (at your option) any later version (SPDX `AGPL-3.0-or-later`), for everything in this archive authored by Andrey Chesnokov. The full text is in `LICENSE`. Short quotations from published sources keep their authors' terms.

The paper's results are proved analytically. The exceptions are the one-sided bound Λ_edge ≥ 1.0044369 (Prop. 5.3, Appendix C), which is computer-assisted, and Table 1, which is a measurement. This archive lets you re-run both.

## Contents

| Path | What it is |
|---|---|
| `repository/` | The repository directories that the paper's availability statement names, at the commit above (`git archive`). It also holds every file the programs read or hash, and the paper source (`tracks/mz-constants/paper/`). That directory omits SIAM's class `siamart251216.cls` and style `siamplain.bst`, because SIAM permits distributing them only together with the full SIAM macro package. To build the PDF, download that package from SIAM's author resources. Paths in the paper are relative to this directory. |
| `data/table1/reproduction.json` | Output of the Table 1 script, regenerated for this archive (2026-11-14). |
| `data/table1/reproduction-historical-2b52b432.json` | The original output (Git blob at commit `2b52b432`, SHA-256 `b85b06fa…6d40`). It agrees with the regenerated file in every number. |
| `data/protocol-history/attempts-P4-d03e74dc.md` | The preregistered protocol of the certificate, as hashed in the producer receipt. Commit `d03e74dc` is in the merged pull request #31; the repository copy was later extended with results. |
| `verify.sh` | Re-runs everything below and compares the results with the committed receipts. |
| `tools/compare_receipts.py` | The comparison. It ignores run-specific fields (timings, paths, versions); exact numerators, denominators, enclosures and code hashes must agree. |
| `VERIFICATION-2026-11-14.log` | Console log of `verify.sh` run on a copy of this pack before packing |
| `LICENSE` | GNU AGPL v3 text; this archive is licensed under version 3 or later |
| `requirements.txt` | The pinned Python stack. |
| `MANIFEST-SHA256.txt` | SHA-256 of every file in the archive. |

## Map from the paper to the files (paths under `repository/`)

**Prop. 5.3 and Appendix C (Λ_edge ≥ 1.0044369; computer-assisted).** All paths are under `topics/padua-mz-sharp-constants-20261106/`.

| File | Role |
|---|---|
| `evidence/P4-trial-J512.json` | Exact dyadic trial vector, J = 512 |
| `code/P4_rayleigh.py` | Producer: outward dyadic interval arithmetic, with `code/interval_dyadic.py` |
| `evidence/P4-rayleigh.json` | Producer output |
| `code/P4_check_grouped.py` | Independent exact-rational checker |
| `evidence/P4-grouped-check.json`, `evidence/check-P4-independent.json` | Checker outputs |

The finite reduction is in Appendix C. The certified enclosure is 1.004436918864667280457774 ≤ q(u) ≤ …779.

**Table 1 (MEASURED).** `tracks/mz-constants/code/reproduce.py --suite all --max-N 1280`. It loads function definitions only from `topics/mz-constants/sources/padua_mz_inputs/code/`, which is pinned by `SHA256SUMS.txt` there.

## How to verify

Run these from the directory this README is in:

```sh
python3.12 -m venv venv && venv/bin/pip install -r requirements.txt
PY=venv/bin/python bash verify.sh            # about 1 minute
sha256sum -c MANIFEST-SHA256.txt             # integrity of the archive itself
```

`PY` may be a relative path like the one above (it is resolved against the directory you run the command from), an absolute path, or a command on your `PATH`; the default is `python3`.

The last line of the output is either `ALL REQUIRED CHECKS AGREE` (exit status 0) or `REQUIRED CHECKS FAILED` (exit status 1). The lines starting with `DIFFER` or `FAILED` above it say which check failed.

Run BLAS single-threaded (`verify.sh` sets this). The certificate uses exact or outward-rounded arithmetic, so its result does not depend on the platform. Table 1 is floating-point and was reproduced bit-for-bit on Linux x86-64 with the pinned stack.

## Provenance

The receipts in `repository/` are the originals of the research campaign. They were produced and independently re-run in separate sessions; the audit records are in `topics/padua-mz-sharp-constants-20261106/`. For this archive, `verify.sh` was run on the staged copy before packing, and its outputs agreed with the receipts.
