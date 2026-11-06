# PD-T?padua-3d-20261106-codex-T10-02 — projection and extraction measurements

ID kind: PD-T. Aliases: T10.2; T10.3. Split from:none. Split into:none. Overall status:**MEASURED**.

## Statement, definitions and assumptions

For the frozen n2..10 candidates, `evidence/t10-quality.json` reports complete angular21³ and41³ mesh lower bounds for raw hyperinterpolation, weighted least squares where exact rank permits it, global tensor-mesh QR, discrete-Leja lower-set interpolation, and the frozen extractions through n7. These are not certified continuous maxima or degree-uniform bounds. The unscaled Chebyshev basis and global QR/Leja selection reproduce the inherited benchmark conventions.

Raw hyperinterpolation uses continuous orthogonality scaling. Degree2n−1 cubature does not guarantee reproduction of Π_n: its Gram aliases may make it a non-projection. Weighted LS inverts the discrete Gram only after exact rank and numerical condition/residual gates. Source-seed rank failures at n2,3,4,6,9 suppress LS rather than silently applying a pseudoinverse.

## Actual results

At n6 and7, best cubature LS mesh norms are8.14895 and9.23074; global QR interpolation gives22.42093 and27.56215; restricted QR extraction gives30.49906 and38.84272. At n10 best LS is12.10462, equal-order parity projection10.95974, global QR66.41113 and Leja99.14343. Thus the cubature projections are substantially better in this finite experiment, while extracting exactly N nodes loses that observed advantage. Minimum-det raw operators can look small while their LS corrections are poor: e.g. n5 raw6.61889 versus LS36.49846.

The structured boundary rule selected exactly N points, but its matrices violate the frozen condition<1e12 eligibility gate at n3..7 (conditions around1e17–1e19). They are labelled numerical failures; **no exact singularity or continuous norm comparison is asserted**. Consequently the operational extraction gate is reached at n6/7 for the eligible restricted-QR candidates; a literal mathematical statement that QR beats every possible extracted set is not supported. The route's recorded outcome is a finite measured comparison plus frozen numerical gate failure, not a whole-class obstruction. The alternative folded-count kill does not apply because the catalogue includes ratios below1.5.

## Proof-bound obligation and limits

T9-05 would transfer a projection bound to an interpolant only with a uniform bound for the inverse restricted sampling matrix C. These measurements neither establish that bound nor show it impossible. The failed boundary rule cannot be repaired adaptively and then counted as the preregistered rule. Continuous Λ maxima and exact algebraic rank of those rejected boundary subsets remain unresolved. All q41 meshes completed; timings are in the receipt. No feasibility fallback was needed.

Frozen command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t10_lattices.py quality --raw "$T10_TMP/census.json" --out topics/padua-3d-20261106/evidence/t10-quality.json --first2 --last10` (write option values with spaces: `--first 2 --last 10`). Source code and input hashes, raw regeneration identity and essential rows are in the receipt. Independent replay remains a separate root-checker obligation.

History:2026-11-06 initial actual comparisons, Codex Sol xhigh assigned. The theory target log³ remains OPEN in its separate record.
