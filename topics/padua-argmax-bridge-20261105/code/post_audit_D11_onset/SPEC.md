# D11 scalar contract — frozen before execution

Pure scalar sufficient-budget evaluation, no new finite degree certificate.
Primary N16000; sole unchanged fallback N20000 only after recorded failure.
Command: `python topics/padua-argmax-bridge-20261105/code/post_audit_D11_onset/evaluate.py 16000`.

The candidate and exact formulas are preregistered in ideas/D11-onset.md.
Evaluate all D08 Ehat components, all accepted full-phase D05 U_F
components, T=(4log²N-3logN)/pi², A=77/96,
B=((47/192)T-113/72)/2, J=27A^4/(256B³),
near slack1/16-2Ehat-J and far slack(191/6144)(T-22)-U_F-Ehat.
Pass iff B>0,T>22 and both lower slack endpoints>0.

The source reads but never executes D06 top-level code. Only definitions
directed,I,ilog,imax,atan_bounds,components are AST-selected after checking
the complete D06 source SHA256
9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413.
Decimal50 basic operations are directed; Decimal ln's documented correct
rounding is enclosed by its adjacent representables. Pi comes from exact
rational alternating Machin bounds (70terms q5,20terms q239).
Output saves full50digit interval endpoints, every component, code hash,
dependency hash and total process CPU including imports/helper extraction.
Aggregate scalar CPU<=5s, soft4/hard5 per process. No native, root,
phase-grid, integration, board, degree or old-case run. Source changes
after first execution require separate review; no retuning authorized.
