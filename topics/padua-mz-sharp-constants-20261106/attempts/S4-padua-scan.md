# S4 Padua scan — live measurement record

Rules/input2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861; assigned gpt-6.1-sol medium.
Protocol published before execution: ec52c16569ea959dfe682fcd7985378a2ef1cd42.
All observations MEASURED, no interval enclosures or limit proof.

## Commands and controls

Three BLAS thread variables set to1. Frozen S4_padua_scan.py imports the
unchanged pinned PaduaOperator. It records seed, source/proposal/environment
hashes, dimension, signed-weight sum/count/mass, matvecs, CPU/wall time,
RSS, residual and failure status per row. Runtime stops before accepting a
value that exceeds the residual guard. Pilot matvec cap2000 includes final
residual product, wall1800s; other rows cap6h. Safety cap6GiB process RSS
and at most two concurrent degree processes protect the16GiB session.

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_scan.py --mode validate --output topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-validation.json
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_scan.py --mode maximum-pilot --output topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-upper-pilot.json
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_scan.py --mode minimum --m 800 801 1000 1001 1200 1201 1400 1401 1800 1801 2200 2201 2600 2601 3000 3001 --output /tmp/sharp-S4/padua-minima-raw.json
```

Finite validation completed first: m10/11/20/21 extrema agree with separately
assembled dense product-Legendre Gram within2.89e-15 relative; independent
Chebyshev moment-system weights10/11 pass1e-12 absolute and total4.
Initial script had a missing space in an else expression, caught as
SyntaxError before any numerical computation; corrected before validation.
No failed execution was reported as successful. Upper800 pilot launched
FIRST and saved its running receipt; one separate minima process launched
only afterward. Its fixed16-case list has no live skip/reshard control;
coordinator informed, keep it intact to avoid interrupting or duplicating
cases. No source changes after launch. Independent checker received hash
and changed-seed validation/rerun instructions, with memory coordination.

One essential receipt is regenerated from actual completed rows via
S4_padua_essential.py. It includes failures and CPU accounting; full raw
remains local, no vectors saved. No posthoc parameter retries or old-history
fits. S4_padua_fit.py is prepared but only syntax-checked while data incomplete;
no slope fit has run. Existing source receipts/gates are preserved.

## Upper pilot outcome — stopped without a maximum

Registered even800 FIRST pilot reached exactly2000matvec cap, wall336.519s,
CPU336.421s, peak314000KiB. Status FAILED/BudgetLimit:matvec cap; no accepted
Ritz value or final residual is reported. Receipt S4-padua-upper-pilot.json
retained. The30min limit was not reached; matvec cap stopped it first.
Operational upper K4 INCONCLUSIVE. No upper801, largerupper solve, or
parameter retry is authorized by this outcome, and none was launched.
Coordinator and independent checker informed immediately. Lower branch
continues independently on its registered complete grid.


## Completed lower grid / exact registered fits

All16 fresh-seed minima completed, both m parities through3000/3001;
every residual and weight guard passed. No row removed or substituted.
The upper pilot remained the sole upper attempt; no retry or continuation.
Full minima receipt remains local at /tmp/sharp-S4/padua-minima-raw.json,
with final hash/size in evidence/S4-padua-run-summary.json. One8666-byte
compact essential receipt retains all16rows, signed weight diagnostics,
seeds/source/environment hashes, residuals, CPU/costs and the failed pilot.
Regenerating it from frozen source receipts produces byte-identical output.
The fit uses only essential data plus committed proposal/code; no local raw
file is required to reproduce the fitted result in a fresh checkout.

Only after last3001 row completed, executed unchanged registered fit code:

```bash
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_essential.py --inputs /tmp/sharp-S4/padua-minima-raw.json topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-upper-pilot.json --output topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json
python topics/padua-mz-sharp-constants-20261106/code/S4_padua_fit.py --essential topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-essential.json --output topics/padua-mz-sharp-constants-20261106/evidence/S4-padua-fit.json
```

No old-history fit, alternate window, changed threshold, posthoc model
constant, fit weighting or parameter retry was used.

| parity/window | intercept at mref | log-slope | maxabs fit residual | scaled condition2 |
|---|---:|---:|---:|---:|
|even/window_A_even_m|0.04004324179931|-0.091452566973204|2.32808e-05|3.16161|
|even/window_B_even_m|-0.034231140778075|-0.092165392083583|1.27192e-05|3.14924|
|odd/window_A_even_m|-0.0058009757762966|-0.092038293672536|1.24537e-05|3.16148|
|odd/window_B_even_m|-0.080438355369245|-0.092493335937252|9.27456e-06|3.14918|

Both lower parities satisfy exact registered stability tests: slope drift
0.7734195% even and0.4919730% odd, versus5%; rank2 and scaled condition<=100;
all expected signs and residual thresholds pass. K4 operational
**KILL_MODEL for the finiteK128 −0.1336 proxy**: finalB discrepancies
31.0139281% even and30.7684611% odd exceed10%. The unchanged fit code uses
label KILL_HEURISTIC_PROXY to make this scope explicit. Preserve the rejection;
do not reinterpret it as model agreement because another theorem exists.
The exact operator theorem is a separate claim. No certified bound on either
finite-window asymptotic bias or the finiteK128 decimal tail links this
regression rejection to a refutation of that theorem or the exact spectrumB.

K5 lower: **MEASURED finite-window parity agreement**, finalB slope relative
difference0.3545594% below5%, with both parity windows stable. This does not
prove true asymptotic equality. Upper K4/K5 **INCONCLUSIVE**, no upper fit was
attempted because required rows are missing after the prescribed pilot cap.

Final residual maximum1.423e-12; peak RSS2181312KiB. Total completed
computation including failed upperpilot3291.64CPU-s (~0.914CPUh).
The m3000 developer result−0.08132259681241012 independently agrees with
changedseed20261107 result−0.08132259681241015 within2.78e-17 absolute;
both guards pass. See independent-checks-S4-padua.md. Fit code/data frozen
and complete-data signal sent for distinct fitted replay; that replay
remains separate from this developer's regeneration check.
