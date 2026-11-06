# Claude audit 02 — independent check code

Independent focused re-audit scripts for [audit-02](../../audit-02.md), written by Claude audit workers. Their outputs are regenerable and were not committed.

Environment: Python 3.13.18, SymPy 1.14.0, mpmath 1.3.0, NumPy 2.5.3, SciPy 1.18.1, single-threaded BLAS. Paths assume the audit checkout `/workspace/padua_research`.

| Script | Scope | Result in the audit run |
|---|---|---|
| G/gauge_exact.py | Full NN triangle in exact Fractions with all 3N derivatives; six gauged fields assembled from s_ν; computes K, v_i, d_i, r_i, L_i, H_i and t* | Ran `python -I G/gauge_exact.py fr krawtchouk 2,...,12` and `... fr hahn 2,...,14`: 138 model-cases. In each, (3) holds and κ_s(t*) = K exactly. The generic assembly equals formula (2) at six t values. |
| G/b2scale.py | Exact ‖b2‖ against the developer's b2 scales | Equal in all 16 cases |
| G/fd_gauge.py | Black-box central differences at 70 dps (reuses audit-01/claude/C/indep_nn.py) | κ_FD = K to ≤ 7e-13 relative at N=3, 4, 6, both families |
| G/dominance_mp.py | Dominance at 100 dps for Hahn N15–24 and Krawtchouk N16/20, six models | K/max r ≥ 1.6e13 (Hahn) and ≥ 2.1e12 (Krawtchouk) |
| G/analytic_checks.py | Variance formula, bound (9), 5^M ≥ 5M², A_M ≥ 2^M(M−1), f_M monotonicity and onset, M=1 spacing | All hold |
| G/random_general.py | Random generic inputs, N3–5 | Formula (2) exact. Dominance fails in 4 of 12 cases, and there t* does not attain K. |
| K/mal.py | 19 malformed native variants run through c4_compare.py; set `AUDIT_SCRATCH` first | Statuses and blank metrics as tabulated in audit-02 |
| R/negs.py | Exact r5 counterexample and r6 loss bound, M=2..18 | ΔU(0) = −6 at M=3, t=1; ‖D‖∞ ≥ 2^M/[M(M+1)] |
