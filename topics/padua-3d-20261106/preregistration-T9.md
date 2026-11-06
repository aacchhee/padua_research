# T9 frozen checks

Written after novelty-gate-T9.md and before mechanism execution, 2026-11-06.
All floating point maxima are MEASURED lower samples, with no enclosure.

1. Reuse inherited QR approximate-Fekete nodes on tensor Lobatto(2n+1),
   and lower-set Cartesian discrete-Leja nodes, n=4,…,12. Preserve their
   deterministic binary64 tie choices. Compare Leja-height Padua stacks
   n=4,…,7 only. Freeze cyclic n4, z=(1,15,19), M69 as a measured control.
2. Report condition number and interpolation residual; suppress Λ if condition
   ≥10^12 or residual>10^-7. Evaluate on angular meshes21³ and41³, nested.
   Use chunks≤512. Refine the four best distinct mesh starts plus eight corners
   with L-BFGS-B on[0,π]³, analytic gradient, maxiter200/maxfun5000,
   ftol10^-12/gtol10^-8. Keep every value and optimizer success count. Mesh
   refinement must not lower a recorded maximum beyond10^-8 relative.
3. Local determinant controls n2,3,4: start with QR nodes, two sweeps of nodal
   replacement. For each cardinal column find its top four21³ mesh values,
   refine with L-BFGS-B plus current node, accept only |cardinal|>1+10^-10.
   Measure resulting sets by the same41³/local protocol. No global optimality.
4. Fit successful QR/Leja degrees4–12, using log response: polylog models
   logΛ=a+k loglog n with frozen k=1,2,3,4 versus polynomial logΛ=a+αlogn,
   α≥1. Report SSE, slope and all values. A lower SSE is descriptive only.
   D2 remains unmet unless exact unisolvence, all-degree measured advantage and
   the original fit criterion hold; binary64 does not supply exact unisolvence.
5. Bounds/checks: exact rational sums for the square-wave lower formula at
   n=1,2,4,8,16,32; harmonic threshold by high-precision scalar evaluation;
   packing inequality and first integer threshold; 2D subgroup counts n1–12.
   Analytic proofs carry theorem status; exact computations are sanity checks
   until independent rerun. No finite census of all 3D lattices is claimed.

Budget: at most20 CPU minutes for the complete numerical command, one BLAS
thread. If exceeded, retain completed cases, explicitly mark remainder exhausted,
and give identical resume command. No adaptive enlargement to chase fits.
