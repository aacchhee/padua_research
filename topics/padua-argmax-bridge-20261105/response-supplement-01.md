# Responses to supplementary findings

These responses do not edit either independent review report. The required
Claude audit remains pending.

## Row supplement R1 — relative output paths

**Fixed.** `code/n2_rows.py` now resolves paths before generating locators,
records the actual argv, and creates the requested receipt directory. The
mathematical loops, thresholds and cases are unchanged. The original run
receipt remains frozen at its historical source hash.

Executed the previously failing relative-path use:

```sh
OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n2_rows.py --output local-output/argmax-bridge-20261105/N2/relative-cli-recheck.json --receipt topics/padua-argmax-bridge-20261105/evidence/n2-cli-recheck.json
```

Exit0; all195 cases complete, zero sign disagreements, receipt written.
[New receipt](evidence/n2-cli-recheck.json) pins the changed metadata/path
code and current theorem hash. This is a coordinator regression check,
not a new independent mathematical rerun.

## Corner supplement C1 — define rho

**Fixed.** N1 round2 now explicitly defines rho=|alpha|+|beta|, equal to
alpha+beta in its first-quadrant derivation. This is exactly the convention
the reviewer reconstructed. Removing the added definition paragraph
reproduces the reviewed mathematical file hash
`5be3cca27524eea360668386636388dd109e85165b4c87fcaeb8769953e9052a`.
No formula, quantifier, proof step or status changes.

## Independent-corner checker canonicalization

During coordinator source inspection, the initially frozen GMP checker was
found to perform rational arithmetic on `Q(4,n*m)` before canonicalizing it.
The denominator can share a factor with4, so that violates GMP's documented
canonical-operand requirement. The coordinator put proved use of the initial
PASS on hold and requested a corrected independent checker execution.
The checker author owns that correction and its replay/report; the original
producer and conditional floating-run data are preserved. A later corrected
acceptance must be cited explicitly; the initial PASS alone is insufficient.

The independent checker author corrected the operand immediately, audited all
two-integer rational constructors, and actually rebuilt and replayed n2,33,64,128.
The four output files are byte-identical to the withdrawn execution, as an
executed comparison establishes. Corrected checker SHA256
`3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3`;
replacement receipt SHA256
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`.
Scoped acceptance is restored solely on that corrected execution. The initial
source/receipt/report/binary/outputs are retained locally as withdrawn history;
[the independent report](independent-checks-corner.md) gives the exact record.
