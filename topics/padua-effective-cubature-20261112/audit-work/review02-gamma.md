# Focused review 02: A2 gamma-certificate repair

Auditor: Codex, gpt-6-astra, high; mathematical audit subagent, 2026-11-13. Rules/working head: `4200087fbb30727a196e0ae86be29236f7d18917`. Candidate: `6c178e9d657419467c8b6eed2909ffa1347a32eb`. Compared with `6a12cf8ba5532fec2283ec3d79e260d7173ce805`. Rules were read previously and checked unchanged by diff; AGENTS, Codex role, workflow, handoff 05 and response-01/A2 were reread. No Git mutation or development edit.

Scope: the material repair of `code/gamma_certificate.py`, its changed proof description and receipt, and retrieval/replay of the two sign certificates and Fourier cross-check. This is not a renewed novelty audit or a new mathematics campaign. Previously accepted unrelated claims are not reopened. The compact witness has a separate assigned reviewer.

## Verdict

**A2's specific coefficient-conversion defect is repaired on inspection, with independent bounded controls passing.** Every G coefficient now carries a certified Arb-based radius, P uses an exact Fraction error, and both bulk and tail propagate the radii. The old unsupported assumption of correct rounding from a 60-digit mpmath calculation is gone. This is acceptance of the repair within the inspected, pinned parameter regime, not a fresh DGOV certificate PASS.

**Full cross-agent replay remains unperformed:** the required input download still returns HTTP403 in this environment and no local copy exists. Consequently this report does not independently reproduce the revised 138-second run or either original complete certificate. Prior independent/developer receipts remain reviewed records of those agents' executions. The response correctly preserves that distinction.

One MINOR new numerical-bound wording issue is listed below. No new mathematical counterexample or additional material defect was found in this focused scope.

## MINOR G02-1: round the displayed error upper bound outward

`theory/explicit-gamma.md:86` says the maximum P coefficient error satisfies `e <= 2.7e-11`. The regenerated receipt `evidence/gamma-certificate.json:9` records `2.7019722407582253e-11`, which is larger. `response-01.md:49` similarly uses `2.70e-11` as an upper bound. Use `2.71e-11` or an approximation sign. The actual checker uses the individual stored radii, so this is a prose rounding error; it does not change the certificate computation or gamma conclusion.

## Inspection details

### Coefficient conversion

- `gamma_certificate.py:323–333`: each exact rational P coefficient is converted to a double, and its error is computed exactly as a Fraction. G's exact rational polynomial in inverse pi is evaluated as a 256-bit Arb ball. The difference between that ball and the selected double is bounded with `abs_upper()`.
- `:326`: for finite nonnegative values in the audited range, multiplication by `1+2^-50` safely exceeds the possible downward error of conversion to binary64 and the subsequent multiplication; the `1e-300` additive term covers tiny values. The exact dyadic double used in the Arb difference is represented through its integer numerator and power-of-two denominator; the conversion no longer assumes the rounded midpoint equals the unknown coefficient.
- I executed the actual AST-selected conversion block from `main`, rather than a copied substitute, on three rational P coefficients and three exact expressions in Q[1/pi]. The examples include cancellation and tiny coefficients. Exact Fraction comparison and independent 512-bit Arb evaluation confirmed containment of all six coefficients. These are synthetic controls, not a check of the unavailable 560 DGOV coefficients.

### Error propagation and Taylor arithmetic

- `:171–200`: `Eten` is added through the nonnegative monomial majorant `sum_a e_a (M+R)^a`. This bounds the discrepancy of the exact polynomial and the nominal double polynomial throughout the nonnegative y-box. A zero nominal polynomial with a nonzero degree-13 radius tensor is also handled, as independently tested.
- `:147–161`, `:185–190`: the former power-library calls in the Taylor core have been replaced with repeated multiplication. Total degree is 13, not 13 independently in each coordinate. This matters to the error count: along a contributing monomial the powers/binomial factors together need at most 13 elementary rounding factors, while the three length-at-most-14 contractions give at most 42 more. Thus the `<60u` shift estimate is conservative in normal arithmetic, including a small allowance to compare the exact absolute majorant with its computed counterpart.
- The radius products have at most 13 degree-dependent rounding factors. The remaining margin in `2^-46=128u`, together with the `1+2^-40` factor at `:197`, covers the subsequent radius/positive-sum operations in the standard NumPy pairwise reduction used for the contiguous sum operands. A length-2744 pairwise sum of the standard eight-accumulator/128-block implementation has less than 32 rounding factors along a path; this leaves room below 128u for the shift, weights, sum, subtraction and endpoint operations. An arbitrary naive 2744-term sequential sum would require a different bound. This review inherits the explicit NumPy/IEEE arithmetic trust base; it is not a formal verification of every backend implementation. The synthetic controls ran with NumPy 2.3.5; the developer receipt records 2.5.3.
- Exact rational Taylor expansion independently checked six boxes for the dense polynomial `(sum y_i - 3)^13/97`, in dimensions two and three, including near-cancellation at M=(1,...,1) with radii 2^-14. Every returned interval enclosed the exact rational Taylor interval. This tests the actual changed enclosure routine, including its coefficient-error term; it does not establish the complete DGOV result by sampling.

### Boxes and tails (pinned parameters R=RG=4, alpha=1001/1000)

- `:203–207`, `:228`: in `[0,4]`, endpoints on a dyadic grid with width at least 2^-24 have at most 26 significant numerator bits. Their squares have at most 52, and the common-denominator sum used for the centre at most 53, so the square/centre/radius operations are exact. The assert is executed before the enclosure can certify a box. The committed receipt reports minimum certified widths 2^-14 (P) and 2^-10 (G); those are developer observations, not freshly reproduced here.
- `:354`: the assertion that the binary64 alpha does not exceed the exact rational alpha makes the bulk l1 discard conservative. On these dyadic grids the three-coordinate upper-end sum is exact, so no additional threshold slack is needed.
- `:263–283`: each homogeneous part restricted to the face receives the matching coefficient radius; there is no lost index or erroneous summation of different homogeneous degrees. The existing positive linear transformation in the radius-squared variable therefore propagates valid lower/upper coefficient bounds.
- `:260`, `:275–276` still contain powers, but for the pinned radius 4 their base is 16 and these entries are exactly representable integer-binomial multiples of powers of two. They do not reintroduce the old uncontrolled power evaluation in this parameter regime. The 2^-40 allowance in `:286–288` comfortably covers the length-14 final matrix products.
- The tail starts on `[0,1]^2`, bisects every surviving box synchronously along a longest side, and stops after the common maximum width falls below 2^-24. Thus the finest evaluated side is at worst 2^-25; its face endpoints/squared centres are still exact with fewer bits than in the bulk. The tail need not have the bulk's explicit width assertion for this pinned algorithm. No acceptance is claimed for arbitrary user-supplied radii/minimum-width settings.
- Synthetic tail controls passed with small coefficient radii and failed as expected after enlarging the leading coefficient radius enough to destroy its sign. This checks that `Eten` is actually used in the tail branch.

## Actual execution and identities

Fresh retrieval command:

```
curl -fSL --max-time 60 -o /tmp/padua-audit-gamma02/octa_double.func.cpp https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp
```

Observed: curl exit 22, HTTP403. No bypass was attempted. A search of `/workspace` and readable `/tmp` files found no evaluator copy; one unrelated protected temporary directory could not be read. The previous audit's web attempt had returned an unsupported C++ content type, and no retrieved coefficient bytes are available here.

Executed bounded control:

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/audit-work/review02_gamma_controls.py > /tmp/padua-audit-gamma02/controls.json
```

Exit 0; verdict PASS. Output records 3 P and 3 G conversion checks; six exact Taylor boxes; an error-only tensor check; and tail-radius propagation controls. Python 3.12.14, NumPy 2.3.5, python-flint 0.9.0; dependencies reuse the temporary installation documented in `gamma.md`. The preserved control is [`review02_gamma_controls.py`](review02_gamma_controls.py), SHA-256 `ddfb4ad40e6cbfda2e83403f7e9ac88b5e1bb0f652913fec21dafa7e9e7d4959` (under 16KiB).

Source hashes recomputed:

| File | SHA-256 |
| --- | --- |
| `gamma_certificate.py` | `52c8c9d9123afdeba2080ee37a456af193fb460051cf596f994a6b52d28fc6ff` |
| `gamma_certificate_indep.py` | `635077161ada17c14c8e866ba36dc6d90ea971b52f7b47073431a6a4cc826f76` |
| `gamma_ft_check.py` | `3f6dbd05c4fbab1d72b8bb717030e194e2b38cb92f64b111f30d8e434da4c1fa` |

The independent Bernstein checker and Fourier cross-check are unchanged. They were not redundantly re-audited as new implementations.

## Runs not executed

Once the expected ancillary bytes are available, the outstanding commands (repository-root cwd) are:

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_certificate.py --anc /tmp/padua-audit-gamma02/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4 --out /tmp/padua-audit-gamma02/gamma-dev.json
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_certificate_indep.py --input /tmp/padua-audit-gamma02/octa_double.func.cpp --out /tmp/padua-audit-gamma02/gamma-indep.json
PYTHONPATH=/tmp/padua-audit-gamma/deps python -B topics/padua-effective-cubature-20261112/code/gamma_ft_check.py --anc /tmp/padua-audit-gamma02/octa_double.func.cpp
```

Input SHA-256 must be `034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47`. The absence of these executions is a continuing retrieval/audit-coverage limitation, not a claimed FAIL of either mathematical certificate. Handoff 05 explicitly allows this to be reported as missing if retrieval remains unavailable; no missing run is counted as PASS.
