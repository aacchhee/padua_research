# Exact rational evaluation of theory73 — plan before execution

Rules were read at `3062f77f5ead1d888fa319a7c3a20371d4f305f7`.
Executor: Codex `/root/input_manifest`, requested gpt-6.1-sol medium;
separate serving-model metadata is not exposed. No new derivation is supplied.
Full written theory73 was read at SHA-256
`2477b42d34c1802b67a6b6c516ddc617688655e33d763f192a9d937d7843c13b`.
It supplies the analytic series and strict tail theorem before this code.

## Preregistered finite scope

Use Python standard-library Fraction arithmetic only, K=64 exactly. Compute
all rational a_k,J_k and S64,S65 from theory73. Check positivity and decreasing
products in this finite range, S1=47/72, S2=1651/2400 and
S64-S65=a65*J65 exactly. The analytic theorem gives
8*S65 < pi²*g < 8*S64; computation does not prove the infinite tail theorem.

Bound each arctan(1/d), d=5,239, by its alternating sums with64 and65 terms.
Apply Machin's classical identity pi=16*arctan(1/5)-4*arctan(1/239), using
opposite endpoints for the negative coefficient. Round that exact rational
pi enclosure outward to denominator10^20. Using these outward pi bounds and
the positive series endpoints gives rational lower/upper bounds for g.
Round only the reported g interval outward to denominator10^12; internally
all comparisons and rounding use integers/Fraction. Report the exact pi²*g
bounds and omitted-term coefficient, the rational pi enclosure and rational
g enclosure. No floats, decimal approximation routines, quadrature or fits.

Freeze source SHA-256 before its first actual execution; the script requires
that identity and verifies itself after calculation. Stop on any exact
identity failure or source drift. Retain one small JSON output and require an
actual different-agent replay into a distinct output, comparing all fields
except elapsed-time metadata. Old regression sources13e/978f remain frozen
and are neither imported nor executed. This supplements73 only; no central
envelope, searched runner-up, global argmax or audit conclusion follows.

## Frozen source and first actual command

Before the first mathematical execution, new source SHA-256 is frozen at
`510955136172a93206861f3a8252aa36460daa8c7965770d0fd6354209104ab9`.
No local source is imported. Execute from `/workspace/padua_research`:

```sh
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a4g_series.py --source-sha256 510955136172a93206861f3a8252aa36460daa8c7965770d0fd6354209104ab9 > topics/padua-proof-attempts-2-20261101/outputs/a4g_series_developer.json
```

## Actual developer execution

The command above actually completed successfully (exit 0); reported elapsed
time 0.003861 s. Timing alone uses a clock; all mathematical arithmetic is
exact Fraction/integer arithmetic. Runtime Python 3.12.14, standard library
only. Frozen source guard before/after passed and external post-run SHA-256
also matched. No old regression source was executed or revised.

Developer JSON: `outputs/a4g_series_developer.json`, 1754 bytes, SHA-256
`1f05b126bdd7ab13b2c1fb889019455d3f02ab9cce95bb76e369340c57e1f24c`.
It retains both exact rational endpoints for pi²*g and their exact difference.
The finite positivity/decrease checks, first partial-sum identities and
S64-S65 omitted-term identity all passed.

The outward rational pi enclosure obtained from exact Machin alternating
bounds is

`157079632679489661923/50000000000000000000 < pi < 314159265358979323847/100000000000000000000`.

The resulting outward rational enclosure is

`54850498619/100000000000 < g < 109705011071/200000000000`,

with reported width `4013833/200000000000`. Strictness follows from the
analytic strict alternating bounds in73, with positive pi bounds and outward
rounding. These finite computations assume that written analytic theorem;
they do not validate its derivation by computation. Actual separate-agent
replay was requested; output comparison remains pending its completion.

## Independent file comparison (execution confirmation pending)

The distinct output `outputs/a4g_series_independent.json` exists complete,
1754 bytes, SHA-256
`5032027b25a848c0fc08be9b03408d1f2ae40511f6975d61584734c79d2a15f9`,
reporting elapsed 0.004015 s. I actually loaded both completed JSON files and
compared them after removing only `elapsed_seconds`: every remaining field
agrees exactly. The source externally reread remains frozen `510955...04ab9`.
This is a file comparison; actual distinct executor/exit confirmation is
still pending the lead's report and is not inferred from the file alone.
No third mathematical run or output overwrite was performed.

### Actual different-agent execution confirmed

The lead `/root/a5_develop` subsequently explicitly confirmed that they
ACTUALLY executed the exact frozen `510955...04ab9` CLI and their tool returned
`exit_code: 0`. Their actual command was the developer command above with only
the final redirection changed to the distinct topic output
`outputs/a4g_series_independent.json`. Reported time, size, SHA-256 and
unchanged source guards match the independent file comparison above.
Thus two actual separate-agent executions passed, and their outputs agree
except elapsed-time metadata. Both outputs together occupy 3508 bytes.
No additional replay was made. The previously pending confirmation is now
complete; the conditional finite-evaluation scope is unchanged.
