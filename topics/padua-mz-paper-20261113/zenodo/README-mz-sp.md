# Evidence for "Marcinkiewicz–Zygmund constants of signed Padua rules beyond half-exactness"

Andrey Chesnokov. Supplementary code and data for the paper (MZ-SP).
Source repository: https://github.com/aacchhee/padua_research, commit `{COMMIT}`.
[Paper reference and DOI: to be added by the author.]
Licence: GNU Affero General Public License v3.0 only (SPDX `AGPL-3.0-only`), for the code and data in this archive; full text in `LICENSE`.

The paper's results are proved analytically, except the following:
- **Computer-assisted:**
  - the certified brackets of Prop. 8.1 (m = 10, 20, 30, 40, 60, 80);
  - the negative trial quotients of Prop. 8.2 (m = 1101, 1240, 1600);
  - the rectangle enclosure of ‖B‖ in Props. 6.8 and 6.9.
- **Measurements:** Section 8.3.

This archive holds the programs, their outputs and the large witness files of Prop. 8.2, which are not in the Git repository.

## Contents

| Path | What it is |
|---|---|
| `repository/` | The repository directories that the paper's availability statement names, at the commit above (`git archive`). It also holds every file the programs read or hash, and the paper source (`tracks/mz-constants/paper-sp/`). Paths in the paper are relative to this directory. |
| `data/witnesses/cert-m{1101,1240,1600}/witness.json.gz` | Prop. 8.2: exact integer coefficient arrays C_ab of the trial polynomials, as gzip-compressed JSON |
| `data/witnesses/cert-m{1101,1240,1600}/exact-norm.txt` | Prop. 8.2: exact rational ‖p‖² |
| `data/witnesses/PAYLOAD-SHA256.txt` | The identities pinned in the repository: the SHA-256 of the *decompressed* JSON, and of each norm file |
| `data/source-vectors/m*-min.npy` | The float eigenvector proposals that the witnesses were rounded from (binary64; not part of any proof) |
| `data/regeneration-receipts/` | Receipts of the 2026-11-14 regeneration (see Provenance) |
| `data/measurements/reproduction-{padua,marginal}.json` | Section 8.3 item (1), regenerated for this archive |
| `data/protocol-history/*-c1e6e59d.md` | The versions of the rectangle protocol and of its finite reduction that the receipts of Props. 6.8 and 6.9 hash. Commit `c1e6e59d` is in the merged pull request #31; the repository copies were later extended. |
| `verify.sh` | Re-runs the checks below and compares the results with the committed receipts |
| `tools/compare_receipts.py` | The comparison. It ignores run-specific fields (timings, paths, versions, gzip container hashes); exact values, signs, enclosures and code/payload hashes must agree. |
| `VERIFICATION-2026-11-14.log` | Console log of `verify.sh` run on a copy of this pack before packing |
| `LICENSE` | GNU AGPL v3.0 (the author's choice, 2026-11-14) |
| `requirements.txt`, `MANIFEST-SHA256.txt` | Pinned Python stack; SHA-256 of every file |

## Map from the paper to the files (paths under `repository/`)

**Prop. 8.1 (brackets)**
- Producer: `topics/padua-mz-2d-frontier-20261105/code/cert_native.py` with `cert_pencil.c`. It needs a C compiler and GMP.
- Checker: `independent_cert.py`.
- Outputs: `evidence/cert-m*.json` and `evidence/independent-cert-m*.json`.
- For m ≤ 40 there is a second exact-rational path: `tracks/mz-constants/code/mz2d_exact.py` with `mz2d_independent_check.py`.

**Prop. 8.2 (negative witnesses, PD-T376)**
- Producer: `topics/padua-mz-cleanup-20261105/code/rigorous_witness.py` (FLINT exact integers and rationals, Arb outward balls).
- Separate checker: `independent_witness.py` (Arb-certified tables plus binary64 contractions under a stated IEEE/BLAS error model).
- Receipts: `evidence/witness-producer-m*.json` and `evidence/witness-independent-m*.json`.
- Payload identities: `evidence/witness-payload-identities.json`.
- In the checker files, the enclosure is `q_center ± q_absolute_error`. The `q_enclosure` field is rounded for display.

**Props. 6.8 and 6.9 (‖B‖ enclosure)**
- `topics/padua-mz-sharp-constants-20261106/code/P1_rectangle.py --N 16 --theta 256`, with `code/interval_dyadic.py`.
- Outputs: `evidence/P1-rectangle-N16.json` (the instance used), `P1-rectangle-N8.json`, and `check-P1-independent-N16.json`.

**Section 8.3 (MEASURED)**
- Item (1): `tracks/mz-constants/code/reproduce.py --suite padua|marginal`.
- Item (2) and the mode weights: `topics/padua-mz-sharp-constants-20261106/code/P2_modes.py run --m M`, with outputs `evidence/P2-m{1600,1601,3000,3001}.json`.
- Item (4): `P2_modes.py model` → `evidence/P2-b2-calibration.json`.
- Items (3) and (4): `code/S4_padua_fit.py` → `evidence/S4-padua-fit.json`, and `code/S3_corner_model.py` → `evidence/S3-corner-model.json`.

The P2 runs at m = 3000 are long and are not part of `verify.sh`. Their commands are recorded in the output files.

## How to verify

```sh
python3.12 -m venv venv && venv/bin/pip install -r requirements.txt   # plus: a C compiler and libgmp-dev
PY=venv/bin/python bash verify.sh                  # about 20 minutes (2 cores); ends with "ALL CHECKS AGREE"
PY=venv/bin/python bash verify.sh out --regenerate # also rebuilds the witnesses from scratch (+5 minutes)
sha256sum -c MANIFEST-SHA256.txt
```

`verify.sh` does the following:
1. Checks the witness payloads against the pinned identities.
2. Replays the exact producer on each archived witness and runs the independent checker. Both must report a negative energy, and their receipts must agree with the committed ones.
3. Re-runs all six bracket certificates and both rectangle instances.
4. Repeats measurement item (1).

## Provenance

The witness arrays of Prop. 8.2 were computed on 2026-11-05 in the campaign `padua-mz-cleanup-20261105`, at source commit `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`. That campaign's transfer copy was not retained. For this archive they were **regenerated on 2026-11-14** from the same commit with the pinned stack (Python 3.12, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0, one BLAS thread). The regeneration reproduced the originals exactly:
- The seeded Lanczos eigensolver (`g1_minimum.py`) returned the three source vectors with exactly the SHA-256 recorded in the original receipts.
- The exact producer rounded them to witness payloads and exact-norm files whose SHA-256 equal the identities pinned in the repository.
- Only the gzip container bytes differ from the 2026-11-05 files, because they depend on the zlib build.
- The producer and the independent checker both accept all three witnesses as negative.

Receipts of the regeneration are in `data/regeneration-receipts/`. The certificate is the exact replay of the archived witness, which does not depend on the platform. A fresh eigensolve on another platform may give different float vectors.
