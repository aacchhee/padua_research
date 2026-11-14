# Padua argmax: public reproducibility package

This package accompanies the paper and companion in papers/. They state the
precise Padua interpolation result, definitions, finite reductions and analytic
premises. The finite certificate coverage is every integer degree 2 through 511;
the exact analytic gate and comparison checks support the reduction for degrees
512 and above. Read the PDFs for the mathematical statements and assumptions.

Start here after ordinary unzip. No repository clone, historical tar archive,
hash-object extraction, bundled operating system or native production run is
needed. The larger preservation archive is separate supplementary custody.

## Files

```text
  README.txt / README.md       this identical Markdown-compatible guide
  verify.py                   public integrity and replay command
  MANIFEST.json               source mapping, input identities and payload hashes
  SHA256SUMS                  checksums of every package file except itself
  phase/inputs/               942 ordinary JSON proof records, degrees 41..511
  phase/check.py              unchanged independent numerical checker
  phase/controls.py           unchanged arithmetic and corruption controls
  phase/runtime_probe.py      unchanged finite floating-point probes
  phase/expected-results.jsonl current accepted scientific outputs, without CPU
  phase/expected-summary.json counts and exact margin minima
  polynomial/inputs/          39 retained certificates, degrees 2..40
  polynomial/receipts/        accepted compact records (input inventory is MANIFEST.json)
  topics/                    small unchanged polynomial checker/provenance closure
  analytic/                  exact gate checker, comparison checker and two tables
  papers/                    current paper.pdf and companion.pdf

```

## Coverage and origin

There are 471 phase degrees and two proof records per degree, named produce and
verify. Both are retained byte for byte because the published execution checked
942 records. They have identical scientific content degree by degree and
represent 471 theorem cases, not 942 different degrees. All degrees 41..511 are
required. The 560 authenticated retained inputs and 382 regenerated inputs are
the origins of today's complete dataset, not obsolete and replacement datasets.
The manifest identifies each exact source; users replay one uniform directory.
The polynomial inputs cover all 39 degrees 2..40.

## Requirements

Python 3.12 or newer and NumPy (reference: Python 3.12.14, NumPy 2.3.5),
C++17 g++, and GMP C++ headers/libraries (reference: g++ 14.2, GMP 6.3).
The audit also passed with Python 3.13.18 and NumPy 2.5.3 for its selected
replays and controls; these tests do not establish universal conformance.
Polynomial degree 33 used about 1.7 GB RAM in that audit; allow more for higher
degrees. The quick smoke covers only polynomial degrees 2 and 17.
On Debian-compatible systems the compiler requirements are g++ and libgmp-dev.
A Python environment with NumPy suffices for phase replay; the integrity and
analytic commands use the standard library. Use ordinary Python, never -O/-OO.
Do not enable fast-math or change floating-point rounding modes. The independent
phase arithmetic assumes the binary64/NumPy behavior described in the papers;
finite same-process runtime probes check selected behavior, not universal IEEE
conformance. No compiler, interpreter, shared library or OS is bundled.

## Commands (from this package directory)

Check every checksum, exact input population and degree-pair correspondence:

```sh
python3 -E -B verify.py
```

Expected: PASS integrity: 942 phase records / 471 degrees; 39 polynomial certificates
then PASS requested verification. This checks stored bytes and records; it does
not rerun interval arithmetic.

Quick numerical smoke, including a fresh polynomial kernel build:

```sh
python3 -E -B verify.py --degrees 41,511 --polynomial-degrees 2,17 --analytic
```

Expected: PASS phase for both records of 41 and 511, PASS polynomial n=2 and n=17,
PASS analytic: exact gates and both 60-entry tables, then
PASS requested verification.
This bounded command is distinct from the earlier complete 942-record execution.

Full verification of retained inputs, without generating new native witnesses:

```sh
python3 -E -B verify.py --degrees all --polynomial-degrees all --analytic
```

Expected: 942 phase record PASS lines, 39 polynomial degree PASS lines,
PASS analytic: exact gates and both 60-entry tables, then
PASS requested verification.
The phase adapter runs sequentially. The earlier four-worker full phase run used
2770.54 CPU seconds and 768.46 wall seconds on its reference host. About 46 CPU
minutes is a planning reference for sequential phase replay, not a promise for
other machines. Polynomial costs depend strongly on degree; allow additional
time, historically a few additional hours for all 39 degrees. Integrity checks
are usually seconds; bounded smoke is much shorter than the full run.
Temporary polynomial builds and receipts are removed on exit.

Optional unchanged scientific corruption/substitution controls:

```sh
python3 -E -B verify.py --controls
```

This uses n199 for the existing degree-specific negative mutations and n41 for
three positive stored-endpoint substitutions. It is not a full witness replay.

## Trust and expected results

SHA256SUMS and MANIFEST.json are inside this package. PASS integrity establishes
internal consistency, including the file population against both lists; it does
not establish authenticity. Authenticate the ZIP against its externally
published checksum in a signed or otherwise trusted deposit record before use.
For degrees not replayed, confidence in stored results rests on that external
archive identity and the embedded checksums.

verify.py verifies SHA256SUMS, manifest hashes and complete scope before any
requested numerical work. Each phase record is passed to unchanged check.check
and its entire scientific output is compared exactly with the current expected row. Timing is
excluded. The cache is reused only within a degree and erased at degree change.
The string "None" in corner_gap for n >= 256 records the analytic E12 corner
branch: its closed [0, pi/4]^2 patches at both parity-correct actual corners
replace the three-point numerical corner descent check. The checker requires
that analytic metadata and no numerical lambda rows; see the PDFs for the
geometric covering and analytic premises. It is not a missing required check.
The independent checker substitutes independently computed enclosures; it does
not establish that every stored native endpoint is valid. Expected results
record that limitation explicitly. Recorded results are comparison targets,
not a substitute for executing verification. The package's construction does
not itself claim a new complete 942-record or 39-degree numerical rerun.

The polynomial driver and strict checker retain their original relative source
paths under topics/. The four part3 Python files, corner dependency text and
baseline kernel are read-only provenance inputs required by unchanged frozen
checks; their production functions are not imported or run. The metadata kernel
is freshly compiled; mathematical predicates are unchanged. For each selected
polynomial degree the fresh receipt must report accepted, complete_partition
and all_supplied_bounds_verified as true, and its certificate SHA256 and
bound/corner/split counts must equal the stored accepted record and input
manifest. This comparison covers the receipt formats for every degree 2..40;
only the explicitly selected degrees are numerically replayed. The analytic gate
checker uses exact Fraction arithmetic and asserts its gates. The comparison
checker reads only the two included table sections through explicit paths.
The PDFs explain the reduction from these checks to the mathematical result.

## Publication metadata

This package supplies no standalone license grant. License, author, funding
and archival metadata remain for the owner to supply under existing project
policy. This package invents no license, DOI or authorship and implies no upload.

## Retained paths and provenance

The pinned input bytes are preserved without redaction. The 560 retained phase
inputs include /home/ahomel/a/andreyac/num_tests/padua30/...; other records retain
/workspace/padua_research/... and receipts for degrees 37..40 retain
/opt/codex/runtimes/... paths. The required corner dependency text under topics/
retains internal provenance and process prose, including model names and audit
and PR references. These are historical execution/provenance strings, not
paths that users must recreate. The owner explicitly chose retention with this
disclosure. No sanitisation or upload is performed by this package.
