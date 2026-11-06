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
