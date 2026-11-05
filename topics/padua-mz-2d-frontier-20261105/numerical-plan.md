# Numerical pre-registration — 2026-11-05

Input/rules SHA: `83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Owner: Codex numerical subagent. This file is written before numerical runs and before any new m>100 spectra. All floating results are MEASURED; no interval enclosure is claimed. G0 authorization from the orchestrator is required before execution.

## Scope and predecessor gate

This is an implementation/measurement extension of frozen `mz2d_spectra.py`, PD-T106/108, and IDEA-058, not a proposed new proof mechanism. Inspected rules, handoff, plan, frozen definitions and producer/exact code; scanned complete IDEA headings/aliases and the Padua IDEA-210–227 and obstruction dispositions. Closest: IDEA-210 exact alias mechanism, IDEA-214 parity control (deferred), IDEA-217 corner leverage (continuous subtraction fails), IDEA-227 tensor control. We do not infer signed positivity from positive tensor data, absolute weights, continuous corner subtraction, or coefficient signs (PD-N045–053). No novelty claim. Cheapest test is full small-m matrix equality against independent dense assembly. DCT-I evaluation of the same finite cosine polynomial only changes implementation, not a mathematical mechanism.

## G1 solver and validation

Use normalized Legendre products so the continuous matrix H is exactly identity algebraically. Store only the rectangular coefficient array, one-dimensional evaluation matrices, signed weights, and Lanczos vectors, never the full Gram. Padua weight polynomial is evaluated using two DCT-I transforms with endpoint factors accounted for. Matvecs use tensor BLAS; their arithmetic cost is O(m^3), storage O(m^2), so this is matrix-free but not a fast Legendre transform. Validate m=10,20,30,40 against explicit frozen nodal Gram, and DCT weights against frozen weights; demand extrema error <1e-9 and vector discrepancy <1e-10. Target eigsh residual <=1e-9; record actual residual, matvec counts, memory high water mark, threads and versions. Seed 20261105, tol 2e-11, ncv 40 initially. Repeat or increase ncv only when residuals/convergence justify it. Try m1000, stop if observed resource cost is excessive. Bulk vectors and output under `/tmp/g1-frontier/`.

Native exact-port extension is secondary to trusted floating G2/G3/G4. An unimplemented port is OPEN, never a failed or successful certification. Sandbox-only compute.

## G2 candidate laws and fixed selection rule

Endpoint n=m−1. Planned m: 60,80,100,120,150,200,250,300,400,600,800,1000 where feasible. Known m<=100 values are context, not heldout evidence. Fit using m=60,80,100,120,150,200,250,300,400 (training); withhold m=600,800,1000. At least three heldout points are required for a winner; otherwise inconclusive. For each positive quantity y=2−lambda_plus or lambda_minus fit log y with equal weight per m, so selection measures relative rather than absolute error. Use scipy least_squares for nonlinear fits with deterministic starting points and positive leading parameters.

Upper candidates: constant gap y=L+a/log(m), L>0 and y>0 on training and heldout; inverse log y=A/log(m)*(1+B/log(m)); inverse log squared y=A/log(m)^2*(1+B/log(m)); other y=A/log(m)^p, 0<=p<=8. Require A>0 and positive model predictions. Lower candidates: inverse log squared and inverse log fourth y=A/log(m)^q*(1+B/log(m)), q=2,4; other free power p as above. No unregistered fitting window changes.

Score is heldout RMS(log prediction−log observation). A candidate wins only if score <=80% of every competing score and max heldout relative prediction error <=5%; otherwise inconclusive. For upper, if inverse-log or inverse-log-squared wins this rule, kill the R1 positive limiting gap claim as the handoff directs. A free-power win is “other,” with reported exponent and no asymptotic proof. Report parameter identifiability and finite-window limitations; diagnostic fits on other ranges must be labeled post hoc and cannot change the original verdict.

## G3 mass geometry and quadrature

At m=100,200,400 use each normalized endpoint eigenvector. Angles alpha,beta in [0,pi], physical mass |p(cos alpha,cos beta)|² sin(alpha)sin(beta) d alpha d beta. Put d_alpha=min(alpha,pi−alpha), similarly beta. Corner region: both d_alpha,d_beta<=K/m (union of four corner squares, L-infinity angular metric). Edge region: either distance<=K/m, including corners. Also report edge-only=edge−corner and bulk=1−edge. K=2,5,10. Thus “corner and edge neighbourhood” is precisely the edge union, not their sum.

Integrate in physical x,y by tensor Gauss-Legendre on the three intervals [-1,-cos(K/m)],[-cos(K/m),cos(K/m)],[cos(K/m),1]. Use n+1 nodes per interval initially: degree of p² in each coordinate is <=2n, so this tensor rule is algebraically exact apart from floating arithmetic. Re-evaluate with n+9 nodes per interval and report maximum absolute fraction discrepancy and total-mass discrepancy from coefficient norm. Evaluate tensors in batches to limit memory. No sampled nodal/weight mass is substituted for continuous L2 mass. Record corner and edge fractions separately. Apply original pass >=90% at K10 at all three m for both eigenvectors; kill if <50% edge mass at m400; intermediate outcome is inconclusive.

## G4

Support both n=m−1 and n=m−2. Planned complete floating scan all integers m=2..300 for both degrees, subject to recorded compute cost. Endpoint n=0 cases use dense one-dimensional matrices. Any lambda_min<=0 or lambda_max>=2 triggers exact certification, not an automatic counterexample claim. Report actual tested list and omissions, never interpolate coverage from a sparse grid.
