# D16 sole prospective scalar contract

Frozen before execution, 2026-11-06, source/rules
8040e0b2c9869a7871ad1825e9b9c746186db084. Primary N=10000 ONLY;
no fallback, threshold search, parameter/precision change or retry.

Command from repository root:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D16_budget/evaluate.py --run-once

Evaluate EXACTLY D16-phase-allowance's D,KD,G,G0,M,W,C,K,E0, D11's
T=(4log^2N-3logN)/pi^2, A=77/96, B=((47/192)T-113/72)/2,
J=27A^4/(256B^3), and all D05 full U_F components, at R2,delta pi/8,
a=p=d=1,P=2,|U0|=8,H=1+logN. Pass iff B>0,T>22 and

    NearSlack=1/16-C-E0-8J-K^2/(2B)>0,
    FarSlack=(191/6144)(T-22)-U_F-E0>0.

Young algebra BEFORE evaluation: the maxima of
A*x^(3/2)-(B/2)x^2 and K*x-(B/2)x^2 over x>=0 are respectively
27A^4/(32B^3)=8J and K^2/(2B). No phase optimization runs.

The helper source is D06 evaluate.py SHA256
9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413.
Only AST-selected directed,I,ilog,imax,atan_bounds,components execute;
never its top-level main, mpmath, old cases or phase inputs. Decimal50
basic operations are directed; ln encloses the documented correctly
rounded result by adjacent representables. Pi is enclosed by exact
rational alternating Machin series,70 terms at1/5 and20 at1/239.
Total process CPU including startup/imports/helpers is capped5 seconds,
soft4/hard5. One fresh JSON receipt records all interval endpoints,
code/dependency hashes, clock and total CPU. No subprocess/helpers,
native/board/root/quadrature/phase-grid/degree job. Every failure retained;
source changes after first call require separate review. Independent
source/math/arithmetic reconstruction is required before any adoption.
