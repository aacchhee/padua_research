# PD-T?padua-3d-20261106-codex-T10-02 — projection and extraction measurements

ID kind: PD-T. Aliases: T10.2; T10.3. Split from:none. Split into: PD-N?padua-3d-20261106-codex-r08-T10-extract-QR ([r08-negative-t10-extract-QR.md](r08-negative-t10-extract-QR.md)), frozen QR extraction failure; PD-N?padua-3d-20261106-codex-r08-T10-extract-boundary ([r08-negative-t10-extract-boundary.md](r08-negative-t10-extract-boundary.md)), frozen boundary extraction failure. Overall status:**MEASURED**.

## Statement, definitions and assumptions

For the frozen n2..10 candidates, `evidence/t10-quality.json` reports complete angular21³ and41³ mesh lower bounds for raw hyperinterpolation, weighted least squares where exact rank permits it, global tensor-mesh QR, discrete-Leja lower-set interpolation, and the frozen extractions through n7. These are not certified continuous maxima or degree-uniform bounds. The unscaled Chebyshev basis and global QR/Leja selection reproduce the inherited benchmark conventions.

Raw hyperinterpolation uses continuous orthogonality scaling. Degree2n−1 cubature does not guarantee reproduction of Π_n: its Gram aliases may make it a non-projection. Weighted LS inverts the discrete Gram only after exact rank and numerical condition/residual gates. Source-seed rank failures at n2,3,4,6,9 suppress LS rather than silently applying a pseudoinverse.

## Actual results

At n6 and7, best cubature LS mesh norms are8.14895 and9.23074; global QR interpolation gives22.42093 and27.56215; restricted QR extraction gives30.49906 and38.84272. At n10 best LS is12.10462, equal-order parity projection10.95974, global QR66.41113 and Leja99.14343. Thus the cubature projections are substantially better in this finite experiment, while extracting exactly N nodes loses that observed advantage. Minimum-det raw operators can look small while their LS corrections are poor: e.g. n5 raw6.61889 versus LS36.49846.

The structured boundary rule selected exactly N points, but its matrices violate the frozen condition<1e12 eligibility gate at n3..7 (conditions around1e17–1e19). They are labelled numerical failures; **no exact singularity or continuous norm comparison is asserted**. Consequently the operational extraction gate is reached at n6/7 for the eligible restricted-QR candidates; a literal mathematical statement that QR beats every possible extracted set is not supported. The route's recorded outcome is a finite measured comparison plus frozen numerical gate failure, not a whole-class obstruction. The alternative folded-count kill does not apply because the catalogue includes ratios below1.5.

## Proof-bound obligation and limits

T9-05 would transfer a projection bound to an interpolant only with a uniform bound for the inverse restricted sampling matrix C. These measurements neither establish that bound nor show it impossible. The failed boundary rule cannot be repaired adaptively and then counted as the preregistered rule. Continuous Λ maxima and exact algebraic rank of those rejected boundary subsets remain unresolved. All q41 meshes completed; timings are in the receipt. No feasibility fallback was needed.

Frozen command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t10_lattices.py quality --raw "$T10_TMP/census.json" --out topics/padua-3d-20261106/evidence/t10-quality.json --first 2 --last 10`. Source code and input hashes, raw regeneration identity and essential rows are in the receipt. Independent replay remains a separate root-checker obligation.

History:2026-11-06 initial actual comparisons, Codex Sol xhigh assigned. The theory target log³ remains OPEN in its separate record.

## Prospective high-degree extension, completed after round1

The identical projection/baseline rules completed n11..16 on both meshes, with extraction disabled by `--skip-extraction`; receipt `t10-quality-high.json`. At n16, best anisotropic LS is16.64112, equal-order parity projection14.22039, source-seed LS31.15199, inherited-reference QR161.50265 and Leja275.37391. The best LS/log(n+1)^3 ratio is0.73172 at n16. All meshes completed; slowest mesh evaluation8.37seconds, below120seconds, so no fallback was needed. These are finite lower bounds, not a growth-law fit or continuous supremum certification.

The global QR construction was corrected before the first pushed boundary to call the exact inherited degree-ordered basis; its q21 values match the primary benchmark, including n2=7, n3=8.320670615 and n8=43.88676861. Frozen restricted QR retains its original lexicographic basis ordering. The two orderings can break QR ties differently; this is explicit provenance, not a change of extraction after observing its outcome.

High command is the same producer with `--out topics/padua-3d-20261106/evidence/t10-quality-high.json --first 11 --last 16 --skip-extraction`. The sharp projection theorem now has a separate named-source-dependent conditional corollary; no numerical value changes its proof status.

## Final extraction addendum

`t10-extraction-complete.md` and its separate receipts now complete the unchanged two extraction rules through n16 and provide exact finite-field full-rank witnesses for all restricted-QR subsets n2..16. The slight restricted-QR mesh win at n8 is retained; n9..16 lose. The final route outcome relies on completed finite coverage rather than interpreting structured numerical ineligibility as the handoff's literal norm kill. Earlier n6/7 measurements are unchanged.

Audit04 note 2026-11-08: "log³ remains OPEN" and "conditional corollary" above are round06 labels; current proposed labels are in [t10-log3-target.md](t10-log3-target.md) and [t10-log3-corollary.md](t10-log3-corollary.md), pending AC's E4 decision ([../response-03.md](../response-03.md)). Audit03 companion T10-m5 ([../audit-03-fixes.md](../audit-03-fixes.md) §B) applies to line 15.

History 2026-11-12, audit04 G4: reciprocal split mapping recorded for the already separated negative claim(s); statements, proof and status unchanged. Final shared crosswalk application remains PR preparation.

## 2026-11-12 — settled E4 convention

The E4 convention is approved; earlier pending/proposal wording is historical. Existing locally proved statements and their separate source-dependent consequences keep distinct statuses. [Primary checks and AC decision](../final-d5/e4-verification.md).
