# PD-N?padua-3d-codex-T8-03 — E fails the frozen quality gate

ID kind: PD-N. Aliases: odd-degree even half-grid lex selector; E.
Split from: none. Split into: none.

## Statement and status

Overall status: **MEASURED**. The preregistered E selector reaches its
literal D2 quality kill at degrees 7 and 9. This rejects the specified
algorithmic family under the empirical gate; it proves no asymptotic
nonexistence theorem for other even-order cyclic generators. The minimum
six fitting rows were not reached, so every growth fit is INCONCLUSIVE.
E is not promising. Independent rerun is required for verification.

## Attempted mechanism and exact scope

Let N=binom(n+3,3). For odd n>=3, set M=2N-2 and choose the
lexicographically first (1,b,c), 1<=b<c<=N-1, b+c odd, with full-rank
integer evaluation dictionary. Only rank determines the choice. The
first unit coordinate proves exactly N distinct cosine nodes; the
half-period eigenspace argument in t8-even-parity.md explains the odd
degree and parity requirements. The rule was prospectively appended
after round1 commit 51c031, before any E quality or higher even-order run.
The cubic rank success was disclosed as known; its quality was unseen.

The closest predecessors and novelty limits are in novelty-gate-T8.md,
candidate T8-06. E changes the odd-order slice to an endpoint half-grid,
but makes no new lattice-architecture or historical-priority claim.

## Measured results

The mesh is the same fixed 21^3 Lobatto mesh for E and both controls.
Values below are sampled Lebesgue functions, not certified continuum
suprema. Every selected dictionary has a full modular-rank certificate;
every earlier deficient modular case receives exact rational RREF/null
verification. A bad prime therefore cannot create a negative selection.

| n | M | Selected (1,b,c) | Candidates visited | E | Leja | QR |
|---:|---:|---|---:|---:|---:|---:|
| 3 | 38 | (1,6,17) | 47 | 12.231433 | 13.174720 | 8.320671 |
| 5 | 110 | (1,11,46) | 268 | 123.751678 | 26.336615 | 13.857502 |
| 7 | 238 | (1,19,44) | 1003 | 539.946336 | 49.812588 | 26.935072 |
| 9 | 438 | (1,14,121) | 1435 | 831.006959 | 84.458024 | 44.179823 |

The n=5 QR loss already makes the family non-promising. The n=7 and n=9
Leja losses are two consecutive tested admissible degrees >=6, triggering
the frozen D2 kill. Degree 11 was not run. No quality optimization,
alternative generator splice, extrapolated fit or resource exhaustion
was used to obtain this stop.

Floating cardinality residuals range from 3.6e-15 to 7.2e-13; reported
condition numbers are approximately 8.39, 88.58, 256.01 and 565.84.
These residuals support the finite numerical calculation but do not
certify global Lebesgue constants. Rank and selector completeness are
separate exact finite claims awaiting independent rerun.

## Reproduction and limitations

Actual command from the repository root:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_even_family.py`

The run completed with exit 0 in 101.282 seconds; the four rank searches
took 0.049, 0.985, 16.223 and 83.508 seconds. Each search completed to the
selected first full-rank member. evidence/t8-even-family.json records
source, core, preregistration and raw-data SHA256 values, package versions,
unrounded values and the literal stop key. Full visited candidates and
exact deficient nulls remain regenerate-only under /tmp; no raw table is
required in Git. The receipt binds the round2 preregistration version;
round1 receipts continue to bind their historical preregistration.

No other generators at a tested degree were quality screened. No claim is
made about best possible quality in this finite class, all odd degrees,
or the broad minimal polylogarithmic target. A resumption must supply a
new uniform structural reason and new prospective gate, rather than
select generators after inspecting quality.

## History

2026-11-06, Codex T8, assigned gpt-6.1-sol high, rules e5b64450.
Recorded after the prospective selector stopped; root owns status
integration and independent verification. No external theorem is used;
literature-T8.md retains the primary-reading and priority limitations.
