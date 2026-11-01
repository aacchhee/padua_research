# Independent reconstruction notes

Auditor: Codex adversarial subagent, assigned gpt-6-astra xhigh; runtime model metadata is not independently exposed. No ultra. Rules read at orchestrator-reported e949ef06895acd5463cdf8df7e0e5f795218f70f. No Git operations. These notes supplement the signed audit report and do not replace the required Claude handoff.

## Counting reconstructed before developer proof review

For primitive a modulo k, the homomorphism from (Z/k)^d onto Z/k is surjective by Bezout. Every fiber therefore has k^(d-1) residue tuples. Partition a box with sides n+b_j into full k-blocks and a boundary with O(n^(d-1)) points. A union of q fibers has q/k times the leading box volume, so its leading count is (q/k)n^d. The total-degree dimension has leading coefficient 1/d!, forcing q/k=1/d! along any unbounded sequence of exact matches. Fixed k, a, offsets and residue set are essential. This says nothing against changing moduli, nonconstant offsets, or other periodic geometries.

For the diagonal modulo-six family, write h_L for the six-vector of residue multiplicities. The relation h_(L+6)=h_L+u and u*v=(sum v)u implies the difference of the three-axis count vector at n+6 and n is uniform. Its uniform value is the volume difference divided by six, exactly the change in binomial(n+3,3). Thus the discrepancy from this dimension is six-periodic. Direct base enumeration gives rows (0,1,1,0,-1,-1), (-2,-1,1,2,1,-1), (0,-1,-1,0,1,1), and three zero rows. This supplies an infinite cardinality family, without an interpolation conclusion. The developer's final proof was then read and agrees.

A short axis of length L<=n gives the monic polynomial product_h(x_j-h), a nonzero kernel element of total degree L over every field. Its proof needs no positivity or characteristic assumption.

## Catalogue completeness

The catalogue fixes d=2,3; n=1,...,6; k=2,...,6; nonzero primitive coefficients; one residue; positive lengths at most n+3. Short axes are removed only using the proved obstruction above. Sort lengths and use unit rescaling, independent axis reversals, and permutations among equal-length coordinates. These bijections preserve counts and arbitrary-axis generic rank. They are not statements that a fixed ordered Chebyshev matrix is unchanged.

My fresh checker constructs connected components under individual group generators, rather than the developer's direct group formula. It enumerates the physical index tuples for every canonical representative rather than using the developer's residue convolution. All 77,616 raw parameters, 5,061 canonical parameters, 451 admissible representatives (39 in two dimensions; 412 in three), and explicit orbit members agree. All 4,610 count failures are retained with precise scope through row inheritance. This verifies completeness only in the frozen universe. Zero coefficients, coset unions, general boundary corrections and larger moduli are not searched.

## Exact ranks and generic lifting

My fresh rank checker reconstructs every selected index set and reversal map, forms the full total-degree monomial matrix in lexicographic order, and computes its row-space dimension by incremental elimination. All 2,184 recorded ranks for 364 representatives agree; there are 850 full-rank tests. Every one of the 412 source patterns is mapped and checked. The separate rerun of the developer's original code also reproduces every recorded rank and determinant.

For a fixed N-point index set, each determinant term uses every degree<=n monomial once. Hence the total degree is 3*binomial(n+3,4), and each axis block contributes binomial(n+3,4). A nonzero modular specialization proves the integral determinant polynomial is nonzero, so its product with all within-axis differences is nonzero over Q. The elementary infinite-field polynomial root argument then gives a nonempty open locus with distinct axes. This is a rigorous characteristic-zero generic lifting argument. It proves neither universal distinct-axis unisolvence nor a claim in every characteristic.

For truly uniform ordered distinct samples over F_p, each sequentially sampled variable has at least p-Lmax+1 possible values. Induction on the last variable, separating its leading coefficient, gives failure probability at most total_degree/(p-Lmax+1), truncated at one. The earlier-variable law remains the same sequential sampling law, so the conditioning is legitimate. The developer explicitly excludes interpreting the fixed pseudorandom seeds as a probability guarantee. A deficient finite sample alone does not prove that the determinant polynomial vanishes identically.

## Nontriviality and prior-art boundaries

All finite congruence instances satisfy property (a). Cardinality or generic nonzero determinant alone does not satisfy the intended structural/stability threshold. Property (b) must be supplied by a genuine axis factorization or informative structural criterion; computing an arbitrary full determinant is not by itself such a result. Property (c) needs an actual Lebesgue estimate or a bounded measured experiment. A finite low-degree result does not establish an infinite stable 3D Padua analogue. Lower-set interpolation, interlaced-grid factorization and Lissajous interpolation remain explicit predecessors, and a Lissajous spectral space cannot be silently replaced by total degree.

## C3 structure reconstructed separately

A selected coordinate-layer cover of size at most n yields a nonzero product annihilator. After removing q layers on one axis, fewer than binomial(n-q+2,2) remaining projected pairs yield a bivariate kernel by rank-nullity, multiplied by the removed-axis factors. Fresh recursive hitting-set and independent all-subset projection checks verify 127 and 86 certificates respectively. The nine remaining cases have no certificate in these mechanisms. A different subbox search, maximizing the selected z-layer counts for every fixed x/y subset and z-cardinality, independently verifies all nine reported subbox failures. This does not prove generic singularity of those nine cases.

If D factors into separate axis rational functions, every two-axis rectangle satisfies D_AA*D_BB-D_AB*D_BA=0 as a polynomial identity. Nonzero modular residues contradict that identity over Q. Fresh independent determinants verify all 426 rectangles and the 114 nonseparable representatives. Zero rectangle tests supply no factorization proof. For all 23 mixed n1 symbolic determinants, I also checked D*D_xy-D_x*D_y is nonzero for an explicit cross-axis variable pair, independently of a CAS irreducibility claim.

The explicit n1 matrix normalizes to determinant t-s. The two nonsingular choices (t,s)=(2,3),(3,2), together with the singular diagonal choice, refute even arbitrary conjunctions of independent axis predicates over Q. Formula specialization to equal Lobatto Y/Z lists proves exact singularity there.

For the isolated n2 (3,1,2) mod6 fibre, I checked the complete direct proof: three matching x-row differences contribute u^3*s*v; the remaining x^2 column contributes 1-u; the yz row reduction contributes w*s; subsequent z differences contribute s*(t-1)*(s-t-1); and the final four-row determinant contributes v*(w-1)*(v-w-1). The signs agree with the displayed negative product. Restoring affine scales requires exponent five on each axis, which matches all three homogeneous factors. Monotone real Y/Z make each additive bracket a sum of two differences with the same sign. This establishes property (b) at n2, with no infinite-degree consequence.

## C1 independent reconstruction

At n2, write f=A*y^2+(B*x+C)*y+q(x). Vanishing at two roots on each of three rows forces B*x_i+C=-A*s_i and q(x_i)=A*u_i*v_i. If A=0, f=0. Otherwise the first constraint is exactly affine interpolation of the root sums, while the second always has a quadratic solution. The determinant sign follows from the three inversions required to move the divided row differences below the original rows. This argument works in characteristic two. A fresh symbolic determinant check verifies the general nine-variable formula, not only the specific mod4 labels.

The four rational determinant values 0,16,-180,0 rule out a pure axis product by their crossed zero pattern. The n3 modular rectangle is independently verified as 544 modulo 1009. Both obstructions are degree-specific.

The modulo-four count vector changes uniformly under n->n+4. The four phase correction rows are (1,0,-1,0), (0,1,0,-1), and two zero rows. Therefore phase0 at odd n and phase1 at even n always have exactly the total-degree dimension. The complete-block y-residue permutation proves generic incidence equivalence of phases only where the stated full-block hypothesis holds; it does not preserve fixed Lobatto geometry.

For phase0/2 at n=2m with m odd, central inversion preserves the selected set with no fixed node. Its N/2 pairs give at most N/2 constraints on even-total-degree polynomials of dimension (m+1)^2, leaving a kernel of dimension at least (m+1)/2=(n+2)/4. This is exactly the proved singular subsequence. It does not apply to the antipodal-transversal phase choices.

For the general row-root reduction, each vanishing row polynomial is Q_i*g_i. Interpolation in x gives a unique polynomial with separate degrees at most n. The coefficient of y^b has x-degree at most n-b exactly when its first b weighted barycentric moments vanish. Rescaling g coefficients by the nonzero barycentric weights gives the stated M-by-M B matrix. The construction is injective and identifies the two kernels, including empty rows and q_i=n+1 rows. Two hundred independent finite-field nullity comparisons include those edge cases and characteristics two and three; all agree.

For the Chebyshev Gram reduction, normalized cosine modes are orthonormal on the full product Lobatto grid. The character sign changes under central inversion for phase0/odd and phase1/even, so its compression has only even/odd cross blocks. It is a contraction because it compresses a sign isometry. The Schur complement and positive weights prove unisolvence iff its largest singular value is strictly below one. Weighted Cauchy–Schwarz gives ||phi(z)||/sqrt(1-sigma), then at most 2*sqrt(N)/sqrt(1-sigma). The proof establishes this conditional inequality, not the missing strictness or a logarithmic bound. The finite geometric-sum formulas, including their resonance branch, were checked algebraically. Fresh direct normalized-grid calculations additionally verify the block and both determinant identities at seven small degrees.
