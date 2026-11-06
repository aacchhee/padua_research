# T5 exact pipeline pre-registration

Written before any T5 mathematical execution; 2026-11-06.

Use normalized product arcsine measure
`d mu_d = pi^(-d) product (1-x_i^2)^(-1/2) dx_i` on `[-1,1]^d`.
Odd one-dimensional monomial moments vanish; moment `x^(2k)` is
`binom(2k,k)/4^k`. All computations below use exact rational arithmetic or
an explicitly defined finite algebraic ring; floats cannot certify a claim.

1. D4: check product three-point Chebyshev Gaussian rules in dimensions 2 and
   3 through total degree five. Optionally check an explicit symmetric
   fourteen-point degree-five cube rule, if its exact moment system is solved.
   Every monomial of total degree at most the claimed exactness is checked.
   Existence must pass before any nonexistence claim.
2. Compute coordinate multiplication sections on `Pi_q`, q=0..4, d=2,3,
   using tensor products of unnormalized `T_k`. Check self-adjointness in
   their exact diagonal Gram metric. Compute all pair commutator ranks and
   the standard extension-size lower bound `dim Pi_q + max(rank)/2`.
   Also record joint image dimension as a diagnostic, with no unproved
   inference to extension size. Known mechanism only.
3. Support probe: use `G_m={cos(j*pi/m):0<=j<=m}^3`, m=3,4,5,
   and only explicitly stated subsets of those grids. First verify the
   same-parity union known positive rule (where an exact algebraic checker
   is feasible). Search exact annihilators or positive-weight dual witnesses;
   one failed solver run does not certify infeasibility.
4. If arbitrary-support near-minimal completion equations do not admit a
   tractable exact reduction, stop that route without a negative theorem.
   A useful bounded fallback is an exact, sharply scoped symmetry or support
   obstruction with a written proof.

T5 budget: at most eight coordinator-pushed rounds, and kill by round three
without a working exact pipeline. Initial acceptance is MEASURED for computed
tables until an independent actual replay. Analytic identities with a written
proof may be PROVED separately. Broad universal cube minimal cubature stays OPEN.

After D4, before the bounded support run: refine step 3 to the three-point
Gaussian tensor grid at degree five, as registered in T5-05. Check all 56
Chebyshev-basis rows on 27 nodes, exact rank/nullity and kernel identity.
Count zeros of the resulting one-parameter weights and solve positivity
exactly. The Lobatto m4/m5 follow-up is deferred if this yields a complete
finite-support theorem. Completed-section norm minimization remains a distinct
task and is not implied by a rank lower bound.
