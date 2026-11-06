# S4 essential evidence / K3 measured comparison addendum

Date2026-11-06; model gpt-6.1-sol medium. Coordinator-authorized followup.
Status MEASURED. No2-D scan, alternate fit or new asymptotic claim.

## Compact essential evidence

`evidence/S4-essential-cc.json` is one7163-byte file retaining all42 raw rows:
N, minimum, maximum, both inverse-eigenvalue residuals, both degree-constraint
residuals. It retains the original raw SHA256/size, original source/proposal
hashes, Python/library/platform/thread environment, seed, solver tolerances
and guard definitions. No timing or work vectors. SHA256:
7e18253a25fb8ab3b78389ef444c8014313b0d4231b6fb0c2467aaa062edacfb.

This is a compact essential dataset, not a split full raw receipt. Full raw
55192bytes remains at /tmp/sharp-S4/raw-cc-scan.json pending AC-designated
archival, hash7ce16e5c61fb82fe1fc4125bbd9570fdc7579db7aa139cd116b4807322f500f2.
Deterministic generator and byte checker:

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_essential.py --raw /tmp/sharp-S4/raw-cc-scan.json --output topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --check
```

Original fit scripts are preserved byte-exactly as S4_k1_fit_original.py and
S4_k3_fit_original.py; their original SHA256s match original fit receipts,
which remain unchanged. Current fit scripts use S4_fit_inputs.py to accept
either the hash-pinned full raw or hash-pinned essential input. Their fit
calculations, windows, weights, SVD and acceptance criteria are unchanged.
New receipts S4-k1-fit-essential.json and S4-k3-fit-essential.json record
actual compact input/loader hashes; numeric `results` objects equal the
original receipts exactly.

Fresh repository-only commands (set the three BLAS thread variables1):

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_k1_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/S4-k1-replay.json
python topics/padua-mz-sharp-constants-20261106/code/S4_k3_fit.py --raw topics/padua-mz-sharp-constants-20261106/evidence/S4-essential-cc.json --output /tmp/S4-k3-replay.json
```

Actual fresh-file-tree check copied only the current two fit scripts,
loader, proposal, and essential data to /tmp/S4-repo-only, then executed
both scripts there. Both numerical result objects exactly matched original
full-raw outputs; see evidence/S4-repo-only-replay.json. Same installed
Python/NumPy environment, separate file tree; developer check, not an
independent-agent rerun. Independent checker was sent frozen hashes.

## Operational K3 comparison

The registered S2 model is its infinite endpoint norm; available numerical
estimate is only finiteJ512 Galerkin1.0044369188646673. Compared to finalB
fits1.0044369722946567 (even),1.0044369722985076 (odd), absolute discrepancies
are5.34299893218e-8 and5.34338402414e-8, below registered1e-3. K3 operational
**PASS**, explicitly MEASURED. The infinite Galerkin tail is not certified;
this comparison proves neither the full model norm nor the actual finite-CC
upper-limit convergence. No tail error was inferred from fit stability.

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_k3_compare.py --model topics/padua-mz-sharp-constants-20261106/evidence/S2-model.json --fit topics/padua-mz-sharp-constants-20261106/evidence/S4-k3-fit-essential.json --output topics/padua-mz-sharp-constants-20261106/evidence/S4-k3-comparison.json
```

Comparison code and receipt pin the exact finite model and fit inputs.
