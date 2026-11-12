# D2 prospective protocol — three rounds maximum

Rules `04ef28b`; developer Codex gpt-6.1-sol xhigh. Planned 2026-11-12,
before scientific execution. The coordinator must publish this protocol and
the current code hashes in gates.md, then send run-go before execution.
Every later driver is hash-published before its own execution. Each round
executes in order; caps are implementation limits, never impossibility proofs.

## Round 1: Padua calibration, then exact algebra

1. Derive exact linear syzygies of rational Chebyshev Padua generators at
   n2,3,4. Check that the (n+2)×(n+1) Hilbert–Burch matrix annihilates the
   generator vector and its signed maximal minors reproduce the generators
   up to one nonzero constant. Retain the actual matrices and sparsity.
2. At n2,3,4 use p=1000003 and Q, both EN (n+3)×(n+1) and symmetric size
   n+2. For each, attempt one random and one structured pencil in both fields.
   Random seed `202611120201 + 100*n + 10*type + domain` (type EN=0,
   symmetric=1; domain GF=0,Q=1). Coefficients uniform integers −2..2.
   Structured baseline is general-position natural-lattice geometry; all
   minors are generated. The exact algebra is a calibration, not a new family.
3. Grevlex Groebner, quotient dimension, all degree≤n monomials standard,
   radicality via squarefree characteristic polynomial of multiplication by
   x+2y+3z. If that form does not separate, report inconclusive, not nonradical.
   Each algebra subprocess: wall≤30 s, CPU≤25 s, memory≤2 GiB. Padua
   calibration: wall≤120 s, CPU≤100 s. Round total wall≤900 s, CPU≤750 s.
   No solver replacement or changed seed after an observed failure.

## Round 2: concrete all-real searches

1. Start from the primary ORSV 4×4 quartic real-node matrix, source-pinned
   by D5, check its 10-node corank-two set, then try its specified 5×5/6×6
   diagonal/rank-one extension. Keep original and extension provenance apart.
2. For n3/4 test known general-position natural-lattice EN/symmetric pencils,
   including explicit rational planes, and affinely normalize coordinates to
   the cube. Check full count, distinctness, rank and evaluation rank.
3. Concrete IDEA-120 probe: build tensor-product Chebyshev multiplication
   sections on Π_(n−1), append the degree-n block to N=binom(n+3,3), and
   minimize the three commutator residuals over symmetric last blocks with
   fixed lower Jacobi entries. n3/4, seeds `202611120202 + n`, two starts,
   at most150 function evaluations/start and60 CPU s/start. Extract nodes
   only after commutator norm<1e−8 and full joint-diagonalization checks;
   otherwise retain the failed residual, never advertise a real node set.
4. Round wall≤600 s, CPU≤500 s, 2 GiB. Exact witnesses are retained only
   as small rational inputs/check outputs. Floating configurations are MEASURED.

## Round 3: measured matrix-parameter optimization

Optimize Λ over coefficients of the surviving all-real pencil family,
parameterizing the generating planes when that is the known calibration.
At n3/4 use four starts, fixed seeds `202611120203+n`, 500 objective
evaluations/start; local derivative-free optimizer or fixed-budget stochastic
coordinate search selected and hash-published before execution. Reject
collisions, singular triples and rank loss. Optimize on a 13³ Chebyshev mesh;
evaluate initial and final candidates on the 41³ Chebyshev mesh, plus512
seeded uniform points (`202611120204+n`). Normalize every candidate by its
axis bounding box into [−1,1]³; the objective is measured on the whole cube,
not merely the hull. Record all starts, losses and best parameters. No
claim of global optimum or certified supremum. Wall≤600 s, CPU≤500 s.

## Acceptance and stopping

The ordered four steps all receive actual bounded attempts. No early kill
before Round3. Kill the tested construction programme if no all-real-in-cube
configuration is found at either n3 or n4. The other kill requires BOTH no
exploitable Padua-specific 2D structure AND best measured Λ>8.10 at n3 AND
>10.18 at n4. Finite timeouts or a failed Jacobi ansatz alone do not establish
nonexistence. If the ceiling is reached with an unproved transfer, keep the
original broad target OPEN and preserve every failed/unrun obligation.

Each JSON≤32768 bytes; generated repository allowance10MB. Raw scratch
data live under /tmp and are regenerate-only. No external archival delivery
or independent rerun is claimed by this developer.

## Round 2 implementation freeze (before execution)

Driver `code/fd2_real.py`, SHA256
`6532327613545db69d568ebf984947654c497f041f885cac9b01ec8d52b7d03c`.
Only py_compile was run while preparing it. ORSV input is D5's primary-read
§2 p7 (rho,sigma)=(10,10) matrix; exact coefficients are embedded. Chart is
x0+2x1+4x2+8x3=1. For size5/6, border couplings are .1 constant and .03*x,
extra diagonal entries use moment-curve normals with t5/6. These are attempted
extensions, with no inherited all-real existence theorem. Search uses all
principal Schur charts,32 starts/chart (origin+31 uniform[−3,3]³),20 Newton
steps/start, deterministic backtracking 1,1/2,…,1/32. Found nodes are lower
counts; no completeness from multistart convergence.

Jacobi implementation fixes precisely the Π_(n−1) multiplication sections;
couplings from its top degree to the extra degree-n-sized block are free,
and compatibility sets couplings from degree≤n−2 to zero. This avoids the
stronger, unjustified assumption that the unknown degree-2n Gram is identity.
Variables are these cross blocks and symmetric last blocks for all3 matrices.
Analytic commutator Jacobian, scipy least_squares/LSMR,150 evaluations/start;
two starts use seed202611120202+n and that seed+1000, perturbations .02/.2.
Each Jacobi child CPU60s, wall75s,2GiB; progress is checkpointed before caps.
The two start seeds refine the original seed declaration, before execution.

Command: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python
topics/padua-3d-20261106/code/fd2_real.py --output
topics/padua-3d-20261106/evidence/fd2-real.json`.

The exact natural-lattice certificate uses moment-curve planes
x+t*y+t²*z−t³ (t0..n+2), all triples and all four-plane augmented determinants,
and literal product-cardinal evaluation over Q. It separately closes the
R1 baseline radicality check if its dimension equals the counted distinct
zeros. No failed random n4 case is silently completed by that baseline.
