# Gates — frozen criteria and execution receipts

Original K0–K2 criteria remain in handoff 01 unchanged.

## K2 preregistration — 2026-11-05, before any m > 1600 run

Minimum-only grid: m=1600,2000,2400,3000, n=m-1. Fit ordinary least
squares y=alpha+beta log(m), separately on windows {800,1000,1200,1600}
and {1600,2000,2400,3000}. Compare absolute distance of each slope from
-1/9; call movement toward -1/9 only if the second distance is smaller.
Record both slopes and residuals. An incomplete grid is INCONCLUSIVE.

Normalization caveat discovered before execution: -1/9 is the optimized
unnormalized negative carrier energy coefficient. The inherited norm
bound alone does not establish it as a spectral coefficient. The fit
comparison is diagnostic only, and cannot prove or conjecturally identify
a sharp spectral constant without a separate normalization argument.

## K0 and K1

K0 PASS. Copied frozen minimum solver actually executed at m60,400,800,1600.
At m800 the Rayleigh value 0.04002526215157158 matches the recorded
0.0400252621515716 within 3e-17. m60 gives 0.18859348048909821, inside
the strict bracket (0.188593,0.188594). In a separate execution the
committed exact native certifier regenerated all four strict m60 endpoints
in 39.393 s. Receipts: evidence/k0-float-replay.json and
evidence/k0-exact-m60.json. The m1600 minimum regenerates as
-0.02341441659034573, still MEASURED until an outward certificate.

K1 pending: fixed-point interval witness producer is being implemented.
