# Supplementary independent scan check — 2026-11-05

**Verdict: PASS within the finite implementation/replay scope below.** No
BLOCKING or MAJOR finding. This is the distinct supplementary check requested
by handoff01; it does not replace Claude's substantive audit or certify any
all-degree conclusion.

Checker: distinct Codex worker, assigned `gpt-6-astra high`; serving model
metadata is not independently exposed. Rules were read at full head
`698802430d333d559668d990123a317f33485064`. Read AGENTS, WORKFLOW, Codex role,
handoff01, plan, LOG and scan-methods; reviewed P4's weighted finite quotient
and continuous-capacity records, P1 triangle admission and P2 disk admission.
This scope is existing implementation verification, not a new mechanism,
novelty/disposition audit or priority claim. Accordingly the full IDEAS read
was omitted under the role's explicit no-novelty exception. No developer
source, theory, shared log, registry, handoff or Git state was changed.

## Scope and independence

The developer wrote both native arithmetic implementations. Here I actually
compiled and executed both again in a new directory, then compared their
scientific fields to each other and the developer's results. Separately I
wrote a Python Fraction implementation that imports no P6 formula code,
constructs the basis directly by monomial Gram–Schmidt, independently
reconstructs parent decisions/scales, and inverts each node's triangular
response recurrence. This third implementation checked degree3 on all three
families and four rules. Agreement at degree3 supports the formula mapping;
it does not imply a separate third implementation was run at degree16.

The inspected scientific source identities are in
[evidence/check-scans-source-hashes.json](evidence/check-scans-source-hashes.json).
The two main native sources are SHA-256
`41c11190b7b15bb5acd5070ccfdb1b66a4bad3739e02d727aba4a506cee2ed6d`
(producer) and
`58480a866b56e22c61add95d01f90774726b5f90e32186354ef1ab8f87b10b72`
(scalar checker). Their hashes match the developer's receipts. Execution
receipts identify the exact source/input/output bytes, commands, compiler
and runtime. The coordinator advanced the shared branch during this work;
final checker receipts record head
`dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc`. Those receipts and source hashes,
not an assertion that every file at that head was reviewed, define coverage.

Environment: Python3.12.14; g++ Debian14.2.0-19; GMP6.3.0; Linux x86_64,
glibc2.41. Exact rationals were used for comparisons, endpoints, logarithm
bounds and OLS extremization. No network data or remote computation was used.

## Executed results

| Independent execution | Coverage | Result |
|---|---|---|
| Fresh H24_222 native runs | degrees2–16, all4 rules, both backends | 60 exact row pairs match; 120 backend/reference comparisons match |
| Fresh D36x9 native runs | degrees2–8, all4 rules, both backends | 28 exact row pairs match; 56 backend/reference comparisons match |
| Third Fraction formula reconstruction | degree3, T24/H24_222/D36x9, all4 rules | all12 rows' four endpoints, choices and ties match |
| Independent N2 calculations | inherited T24 compact logs; new H24_222 exact rows | both INCONCLUSIVE |
| Negative controls | 15 Python interface rejections;10 native input rejections; native primitive test | all pass, including8 internal malformed native controls |

Receipts: [Hahn replay](evidence/check-scans-H24_222.json),
[disk replay](evidence/check-scans-D36x9.json),
[reference comparisons](evidence/check-scans-comparisons.json),
[formula reconstruction](evidence/check-scans-formulas.json),
[fits](evidence/check-scans-fits.json), and
[guards](evidence/check-scans-guards.json).
Each file is under16KiB. Raw fresh rows, compiler outputs and logs remain in
`/tmp/padua-lanczos-nonproduct-20261105/scan-review/`, with byte counts and
hashes in the replay receipts. They are not claimed to have been delivered
to external cold storage.

All scientific fields match exactly; only wall time and the count of Gram
pairs checked by the whole maximum-degree run were excluded from the
cross-run dictionary comparison. Gram coverage was separately checked by
the scan harness. Comparing elapsed times or total Gram counts across
different maximum-degree executions would not be a scientific equality test.

For H24_222, the slowest fresh producer/checker cases were5.04/14.41s;
for D36x9 degree8 they were4.30/22.66s. This check did not launch another disk
degree16 run. At inspection its developer receipt remained INCOMPLETE,
with only the BJ/mirror producer cases recorded complete. Neither those
partial outputs nor the degree8 replay support an N2 disk verdict. Any
later disk N2 result requires complete all-rule/both-path coverage and a
separate check of that new artifact.

## Formula and fit review

The generators reproduce the admitted data: T24/H24_222 have325 points;
the Hahn weight is `(i+1)(j+1)(25-i-j)/binom(29,5)`, summing to1. D36x9 has
324 distinct rational points with equal normalized weight. The checker
rebuilt these point/weight sets independently and compared them exactly
with the actual native inputs. The scans stay within the admitted degree
ranges and satisfy M>N_s.

The source scale in code is the squared weighted norm of the selected raw
coordinate product. The response sums include every nonconstant source
through the output prefix. The normal diagonal includes the node weight,
whereas v_hi has no extra node weight, agreeing with represented Euclidean
sources in P4-02. The code's Knode², KHS², row² and minimum upper² match the
stated lower/upper formulas. The source/rule convention remains consistent
across each ratio. The pivot rule compares residual-square/raw-square
exactly and chooses X on ties; the direct monomial construction confirmed
these choices and ties in the tested small cases.

For N2 I independently recomputed `L_BJ²/min_R U_R²` and
`U_BJ²/min_R L_R²`, including BJ in the four-rule comparator set as the
current plan specifies. Taking half-logarithms is necessary. A new local
rational-series implementation uses192-bit outward mantissa bounds and a
96-term atanh series with a proved geometric tail; its18 lower/upper log
bounds lie inside the developer's H24_222 reported bounds. Enumerating all32
corners in each five-degree window independently checks the signed OLS
coefficients `(-2,-1,0,1,2)/10`. Its slope extrema also lie within both of the
developer's rational-log paths' extrema. Thresholds are strict0.1 and0.02,
with the decision requiring both windows, exactly as preregistered.

| Family | 8–12 slope enclosure (decimal display) | 12–16 slope enclosure (decimal display) | N2 |
|---|---|---|---|
| T24, inherited compact logs | [0.137373742216312,1.802356877851230] | [-0.216477623410181,1.822813370740502] | INCONCLUSIVE |
| H24_222 | [0.055306901913349,1.539503505584218] | [-0.220202416458254,1.651201929678249] | INCONCLUSIVE |

These are interval screens of finite capacity bounds. They are neither
exact evaluations of the capacities/condition quantities nor proofs or
refutations of exponential or polynomial asymptotic growth. The N2
INCONCLUSIVE labels are supported; no pass/redirect is hidden by the check.

## Commands actually executed

All commands were run from `/workspace/padua_research`; the replay harness
records the expanded compiler and native commands. The relevant commands
were:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family H24_222 --max-degree 16 --seconds 600 --work-dir /tmp/padua-lanczos-nonproduct-20261105/scan-review/H24_222 --receipt topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-H24_222.json
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family D36x9 --max-degree 8 --seconds 120 --work-dir /tmp/padua-lanczos-nonproduct-20261105/scan-review/D36x9 --receipt topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-D36x9.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode compare --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-comparisons.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode formula --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-formulas.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_review.py --mode fits --output topics/padua-lanczos-nonproduct-20261105/evidence/check-scans-fits.json
python -B topics/padua-lanczos-nonproduct-20261105/code/check_scans_guards.py
```

The review checker was rerun after adding explicit input/output identity
checks and correcting command metadata; final receipts pin its final source.
No failed mathematical comparison occurred. Native replay directories must
be fresh when repeating the harness; choose new directories and receipts
instead of overwriting completed evidence.

## Notes and limits

- **NOTE — inherited provenance:** T24 compact table SHA-256
  `2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38`
  matches the accepted inherited evidence. Its source manifest and original
  large report are absent at their recorded local paths in this environment;
  the frozen logarithm code is present and matches its hash. I reproduced
  the new N2 extrema from all76 compact rows, but did not independently
  reconstruct the original high-degree T24 logarithms. This limitation is
  already explicit in the developer's inherited-scan receipt.
- **NOTE — disk completion:** degree16 remains outside this executed replay
  scope, and partial completion cannot establish a screen result. The
  completed degree8 replay validates only its recorded finite range.
- **NOTE — audit limits:** no new all-degree theorem, N3 recursion, P1/P2
  continuous moment probe, P3 radius or mechanism disposition was audited
  here. Admission and P4 records were read for the implementation's exact
  assumptions. Their full mathematical/novelty audit belongs to the required
  substantive handoff. Python guards were executed with assertions enabled,
  as in all recorded commands.

No requested developer correction arose within this scope. The independently
executed checks strengthen the finite evidence while leaving the stated
scientific and storage limits intact.
