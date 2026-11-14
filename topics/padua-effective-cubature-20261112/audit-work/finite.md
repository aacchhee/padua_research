# Finite-computation audit support

Codex subagent, `gpt-6-astra`, high, 2026-11-13. Rules read at
`8b27da5ea2e0d363d2a416482b176466dc33efa9`; candidate
`895d85fdd995e9f227dabaf8a212ba4d3b188db0`; base
`b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`.

Scope: record -06, the finite reduction to -04(b′), lattice checker code,
Q0/Q1 replays, evidence arithmetic and Q0–Q3 verdicts. No novelty/priority
assessment is made in this bounded computational review; the orchestrator owns
that review and the full IDEAS read. Development files were not edited. Only a
read-only `git show` was used, after the orchestrator permitted read-only Git.
All generated outputs are under `/tmp/padua-audit-finite/`.

## Findings

### MAJOR F1 — Q2's claimed preregistered KILL does not follow from the data

`gates.md:88–90` calls the plain torus LP KILL under the pre-registration. The
actual pre-registered condition at `gates.md:44` requires the fitted
`n*(rho_n-1)` to be non-increasing over the last four tested degrees, or a
literature/proof determination of the Turán constant. Neither is supplied.
Using `R_upper/m_n` in `evidence/lp-torus.json`, the final four values are:

| n | n(rho-1) |
|---|---:|
| 9 | 0.0000274105642244 |
| 10 | 0.0000264365832603 |
| 11 | 0.0000284971172324 |
| 12 | 0.0000324709330730 |

The verdict instead treats these as zero within tolerance, an additional rule
not in the pre-registration, and supplies no fit. The other listed kill
condition remains open. It is reasonable to stop investigating this numerically
unpromising route, but not to claim the pre-registered test was met.

Fix: retain the original gates, append a corrected verdict (not promising;
preregistered kill not established), and identify any discretionary
abandonment/deferment separately with its actual evidence. Synchronize dependent
Q2 summaries/dispositions (`report.md:19,40`, `attempts/E1.md:24,44`,
`rounds.md:10`, `LOG.md:57`, `results/padua-effective-cubature-20261112.md:33`,
and candidate records as appropriate). No proved -01–-07 conclusion depends on
these numerical observations.

### MAJOR F2 — summary overextends record -06 to the unresolved larger range

`report.md:89` names `4 <= n <= 217`, then specifically `110 <= n <= 217`,
and says “The torus route is proved useless there (-06).” Record -06 establishes
its limitation only at `2 <= n <= 109`; it explicitly leaves finite torus LP
values open above that. The summary therefore wrongly rules out a viable open
route on 110–217.

Fix: say explicitly that the torus route with the coarse conversion is ruled
out only at 4–109, while finite torus LPs and improved continuous constants
remain possible at 110–217. `report.md:20`'s “exactly the range left open by the
uniform bound” should likewise distinguish the unavoidable blind interval
through 109 (the cap) from the interval left open by the currently certified
constant (through 217).

### MINOR F3 — incorrect numerical envelope and B&B completion summary

`gates.md:89` and summaries (`report.md:19,40`, `LOG.md:58`,
`attempts/E1.md:34`, `results/padua-effective-cubature-20261112.md:30`) say every
plain ratio is within `3e-6` of 1. Stored upper values give:

- n=7: `377.002119/377 - 1 = 5.6206896553e-6`;
- n=8: `575.002643/575 - 1 = 4.5965217392e-6`;
- n=9: `833.002537/833 - 1 = 3.0456182472e-6`.

A `6e-6` envelope would cover the reported values. `gates.md:81` says B&B was
incomplete for every run; the three n=2 rows have `bnb_complete=true` and a
lower value 6.994 < Fisher 7. Fix those observations while retaining the correct
conclusion: no rigorous numerical lower bound above Fisher was obtained.

### MINOR F4 — Q1a reproduction command omits a required option

`handoffs/03-audit.md:62` invokes `lp_cube.py --q1a` without `--out`, but
`code/lp_cube.py:235` makes `--out` required. Supply
`--out <scratch>/q1a-cube.json` in the next handoff/reproduction record; preserve
the immutable old handoff instruction body.

## Reduction/code assessment

The finite limitation in -06 is correct. A witness lattice avoiding all
`0 < |k|_1 <= E` has a dual finite group G containing zero with
`|G|=|det A|`. Averaging any admissible f over G gives at most c0, while
nonnegativity gives an average at least `f(0)/|G|`. Thus
`f(0)/c0 <= |det A| <= 8*binom(n+3,3)` and the stated conversion cannot exclude
a package. The stronger witness E=2n-1 also caps E=2n-2. Equality is correctly
allowed. The statement excludes orbit-sensitive or cube-native improvements,
and does not claim package existence.

`pdn_lattice_witness.py` correctly bounds integer coefficients by
`floor(E*max_j |(A^-1)_ij|)`, using exact Fractions. The floating-point candidate
search only locates integer witnesses; their acceptance is exact. Extra row
bases are correctly transposed. `pdn_check_ball.py` enumerates every integer
point of the l1 ball and tests the adjugate congruence; its int64 guard bounds
each matrix-product sum safely. Determinant recomputation is correct. The
checker relies on generator-supplied `covered` flags rather than recomputing
the threshold, but the generator formula was inspected and my independent
check recomputes every strong-witness threshold and coverage flag.

The cap lattice check is sound: exact rational inverse gives coefficient
radius 3; exhaustive enumeration finds determinant -38/27, minimum 2 and 14
minimal vectors. The inverse bound includes every potential norm <2 vector.

Q0/Q1 formulas use the normalized product Chebyshev basis correctly. The cube
Q1a expands K² exactly and checks three rational diagonal evaluations; the
identity itself also follows directly from that expansion. These are sanity
checks, not a global numerical certificate of an optimized LP polynomial.
The LP symmetry restrictions preserve the objectives by group averaging.
Finite-grid optima are relaxation values, and all numerical lower estimates
remain MEASURED. No mathematical theorem here relies on them.

## Commands actually executed and results

Repository root is `/workspace/padua_research`; topic cwd is its
`topics/padua-effective-cubature-20261112`. Python is 3.12.14 in this audit
(the producer used 3.13.18). Missing `highspy` initially caused the two Q1a
commands to fail on import; installed with
`python3 -m pip install --target /tmp/padua-audit-finite/deps --no-deps highspy`,
then reran using `PYTHONPATH=/tmp/padua-audit-finite/deps` (HiGHS 1.16.0).

1. `python -B topics/padua-3d-20261106/code/fd1_controls.py --output /tmp/padua-audit-finite/fd1-controls-replay.json`.
   PASS; recursive comparison with committed evidence differs only in
   `seconds_measured` and the output path in the command.
2. `python -B topics/padua-3d-20261106/code/fd3_certify.py check --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --receipt /tmp/padua-audit-finite/fd3-replay.json`.
   `PASS_EXACT_INTERVAL_NEWTON_AND_RANK`, with recorded checker/certificate
   hashes unchanged.
3. `python -B topics/padua-effective-cubature-20261112/code/q0_d3_leverage.py --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --output /tmp/padua-audit-finite/q0c.json`.
   Sum p=10, sum p²=6.1132582411189500652, cap=1.6357889043093383045,
   M=160. Every recorded field matches except command/output path.
4. `python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py /tmp/padua-audit-finite/cap.json`.
   PASS, det=-38/27, minimum=2, 14 minimizers; only command differs.
5. `PYTHONPATH=/tmp/padua-audit-finite/deps python3 -B topics/padua-effective-cubature-20261112/code/lp_torus.py --q1a --workdir /tmp/padua-audit-finite/lp --out /tmp/padua-audit-finite/q1a-torus.json`.
   PASS n=2..8: exact ratios 7,25,63,129,231,377,575; spectrum checks true.
6. `PYTHONPATH=/tmp/padua-audit-finite/deps python3 -B topics/padua-effective-cubature-20261112/code/lp_cube.py --q1a --out /tmp/padua-audit-finite/q1a-cube.json`.
   PASS n=2..8: integral D=4,10,20,35,56,84,120; diagonal checks true;
   total degree exactly 2n-2.
7. An inline Python import of `lp_lattice.verify_basis` checked all 15 bases
   in `evidence/lp-lattice.json`: indices/avoidance PASS at n=2..16;
   output `lp-lattice-replay.json`. The exhaustive HNF *minimality* search
   was inspected, not rerun; the manifest correctly labels it producer-only
   MEASURED-exhaustive. The finite limitation needs only the witnesses.
8. `python3 -B topics/padua-effective-cubature-20261112/audit-work/finite_controls.py`.
   Independent SymPy inverse plus Python integer coefficient enumeration
   checked all 139 strong committed witnesses, their determinants, exact
   `8*binom(n+3,3)` thresholds and coverage flags: PASS. Direct-ball checker
   negative controls: Z³ fails at E=1; 7Z³ passes E=6 and fails E=7.
   All 32 recorded torus upper values lie between Fisher and their lattice
   reference. Output `independent_checks.json`. An initial output-serialization
   failure (SymPy integer) was corrected to Python int and the script rerun.
9. `git show 0abf5e7:topics/padua-effective-cubature-20261112/gates.md`.
   Comparing with head shows all pre-registration definitions unchanged;
   only the `(none yet)` verdict placeholder is replaced by verdicts/addenda.
10. From the topic cwd:
    `python3 -B code/pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb --out /tmp/padua-audit-finite/witness-full.json`,
    followed by
    `python3 -B code/pdn_check_ball.py --full /tmp/padua-audit-finite/witness-full.json --out /tmp/padua-audit-finite/pdn-check.json`.
    Both completed with exit 0. Direct-ball `check_failures=[]`: all 278
    witness checks across 139 degrees PASS. The 139 compact rows match the
    committed evidence exactly, including all indices, strong bases and
    both coverage flags. Recomputed coverage is 108 degrees 2..109 for
    E=2n-1 and 127 degrees 2..128 for E=2n-2. Strong n=109 has index
    1822682 <= 1823360, margin 678.
    The exclusion of all possible witnesses beyond n=109 uses the cited
    packing literature, not the failed heuristic searches beyond that degree.
11. From the topic cwd:
    `PYTHONPATH=/tmp/padua-audit-finite/deps OPENBLAS_NUM_THREADS=1 python3 -B code/lp_torus.py --n 5 --extra 5 --workdir /tmp/padua-audit-finite/lp --out /tmp/padua-audit-finite/n5-e5.json`.
    Completed in 134.9 seconds: upper=139.55249358897203,
    rho=1.0818022758835042, B&B incomplete, lower=40.9833 < Fisher 129.
    The stored early-code value is 139.553940 (relative difference 1.04e-5),
    so this reproduces the qualitative measurement, not the old receipt
    exactly. The documented mid-campaign code/default changes apply.
    Runtime NumPy 2.3.5, SciPy 1.17.0, HiGHS 1.16.0; final LP code SHA-256
    `81b7fcd38b7a668a0bc9e93a15b3e980573c62340d50e18dca1b6fe13edd75d1`.

The preserved independent support script is `audit-work/finite_controls.py`,
SHA-256 `7d112ef215715f393e9de0cc16d22f0f9acaec0ab5e66a80ed087102a8122440`.
It resolves the repository from its own location and accepts `--output`; its
receipt records this code identity.

## Verdict

Record -06's mathematical reduction and all 278 regenerated witnesses pass
both prescribed code paths; an independent coefficient-box check also passes
all 139 committed strong witnesses.
Q0 and Q1 sanity/reference checks pass. Q3's no-certificate verdict agrees with
the evidence. Q2's Delsarte INCONCLUSIVE verdict is consistent with the data,
while the plain-LP preregistered KILL needs the F1 correction. The finite
computer-proof full rerun is complete and supports the stated finite claim.

## Off-repository output identities

All files below are under `/tmp/padua-audit-finite/`; no raw outputs were
added to the repository. `audit-summary.json` records the same compact verdict
and artifact identities.

| File | Bytes | SHA-256 |
|---|---:|---|
| fd1-controls-replay.json | 3254 | `ef6dd1292359368627a7b0df955472395780e42be15e1aa21fcd4aa5be537cf2` |
| fd3-replay.json | 1433 | `11ec6fd9c051cc20f0211d18e906412e53da3ba2910ee60857639ce1110ba980` |
| q0c.json | 836 | `db82bb54435bdb32c71205497420c6f21dfaf9a4f171472279988201a390d908` |
| cap.json | 620 | `022116452d3d6e8ce3f53ef3a111ee59d153ccf63846c02b0480456204497a8e` |
| q1a-torus.json | 2017 | `d5dc50f42e4aa33bf17162f71e75d139ea6e9858ef8533d6dc5804828cc6c5ed` |
| q1a-cube.json | 2075 | `76783cda8761b73a9b8d1d66e8a19d11d9a46babe042498d4716c43f38bef304` |
| lp-lattice-replay.json | 942 | `b9b6aa28d715244dd7195d388e9e3f93ee80fca6cede81cb66ecae8eaaad311c` |
| independent_checks.json | 28813 | `c7874519fb7718a13aaa57fa9f7e5c802f7bb6b77d693ce8b9fb2965c5fc05e8` |
| n5-e5.json | 3142 | `6d8a19cbeb0d8ca7feceb0066a653609165fd1fb389e3a10419b619d8ac75ef5` |
| witness-full.json | 38684 | `5236d9b9fab75b2ff7bf2b211c2eb2f175452d0f7f02c80af43b832b855a4e5b` |
| pdn-check.json | 10952 | `c03edbb9f7a4d45e6941aee15c4eafa5b8465f09292a1bd6bf882bf0cd4f866c` |
