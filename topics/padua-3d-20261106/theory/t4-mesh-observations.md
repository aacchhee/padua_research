# PD-N?padua-3d-codex-T4-02 — three Padua-stack orderings fail the finite D2 screen

ID kind: PD-N. Aliases: M/A/L plane heights; sampled competitive baseline.
Split from: none. Split into: none.

## Statement / negative-result scope

The three preregistered Padua-plane height orderings M (monotone), A
(alternating extremes) and L (greedy Leja, high-precision selected) were
evaluated in binary64 at every n=1,...,7, on the inherited 21^3 Lobatto mesh.
Each has sampled Lebesgue value above the inherited discrete-Leja lower-set
reference at both n=6 and n=7. Each therefore triggers the preregistered D2
KILL at n=7. This is a finite measured failure of the competitive screen,
not an asymptotic theorem or a rank-deficiency result.

Overall status: **MEASURED**. Candidate disposition: **REJECTED: failed**
as a competitive lead within this exact screen, separately for M, A and L.
The general all-n polylog target is OPEN. M's independent analytic
exponential lower theorem is recorded separately in t4-monotone-lower.md.

## Observations

| n | M | A | L | inherited Leja | inherited QR |
|---|---:|---:|---:|---:|---:|
|1|4.0000|4.0000|4.0000|5.0000|2.0000|
|2|13.6667|6.0607|6.0607|7.0000|7.0000|
|3|54.4706|12.8401|12.8401|13.1747|8.3207|
|4|253.7926|29.5126|18.5994|19.4982|11.2449|
|5|1490.5616|66.0962|33.5400|26.3366|13.8575|
|6|8902.3969|160.3045|44.2656|40.2764|22.1915|
|7|56185.8819|373.4147|51.7598|49.8126|26.9351|

The same inherited basis, mesh and QR candidate extraction were used. The
L ordering is materially better than M in this range, but does not pass
the frozen comparison criterion. No model fit was run after KILL.

## Checks / evidence / reproducibility

Actual command, executed 2026-11-06 from repository root:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t4_stacks.py --max-degree 12`

The preregistered stopping rule stopped every family after7; n8..12 were
not executed, and no n20 run was attempted. Elapsed producer time0.619s.
Environment, source/preregistration hashes and full compact rows are in
evidence/t4-mesh-M.json, t4-mesh-A.json, t4-mesh-L.json and t4-baselines.json.
All four are below6.5KiB. Code is code/t4_stacks.py; inherited code was
imported read-only. Numerical cardinals from the written Newton recursion
and direct Vandermonde solves agree in max absolute norm through n4:
M<=7.51e-14, A<=3.11e-15, L<=1.65e-15. The determinant factor comparison
through n4 differs by at most1.43e-14 in logarithms.

Across n1..7 the largest condition2 is40736.1 (M,n7). Maximum absolute
linear-system residual is1.82e-11 for M,1.06e-13 for A,2.53e-14 for L;
relative residuals are below7.3e-17. Nodal cardinality residual infinity
norms are below1.16e-11 (M),1.72e-13 (A),4.44e-14 (L). These are diagnostic
float residuals, not certified error bounds. No unreliable value needed
suppression at the threshold condition2>=1e12.

Node arrays and their path/hash/size manifest are local in
/tmp/padua-3d-20261106/t4-node-artifacts.json (SHA256
5e32d1cf5e57fe08315020d9caec074ae02a4d613a08177c39c43aee397eb504).
External archival delivery is pending. The compact essential evidence is
committed; code regenerates all arrays. No independent replay is claimed
by this developer. The coordinator arranges it separately.

## Depends on / limitations / history

The all-n unisolvence hypothesis is supplied by T4-01's hand proof; no
numerical rank is promoted to proof. Mesh maxima are MEASURED samples of
the true continuous Lebesgue function, not certified global maxima.
Closest predecessor is IDEA-187/PD-N037; this is a different non-fibre
node geometry with the identical controls. No historical novelty claim.
2026-11-06 Codex, assigned gpt-6.1-sol/xhigh, runtime metadata unexposed;
rules/input ccd9e905d19c0c625c196c4a3f3e707058ed042a. Audit/replay pending.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
new response dispositions/ID-kind/evidence changes require focused re-audit,
not another approval of the unchanged accepted mathematics.
