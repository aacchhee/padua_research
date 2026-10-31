# U1 retained candidates

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`; Codex development, 2026-10-31. Provisional labels only; no novelty claim. Empty registry and baseline read in full. Broad prior-art comparison remains pending.

## U1a — supplied arbitrary-field quasi-definiteness iff

- Aliases: HS checkerboard conjecture, alternation-functional criterion.
- Scope/mechanism: all m≥0, every field, labelled distinct axis nodes; source cutoff Δr, r=1,…,L−1 on both axes.
- Closest predecessor: Harris–Simanek ordered-real theorem, supplied hs_ff.py conjecture; no separating conjecture is claimed here.
- Separation: replace ordered-real positivity by the exact stated quasi-definiteness condition over arbitrary fields. One unisolvent board with any zero required minor, or singular board with every required minor nonzero, kills the iff.
- Cheapest test: characteristic 2 and m=0,1, then exact small symbolic determinant.
- Actual result: characteristic 2, m=1 refutes the iff, with an elementary explicit proof. The unrestricted conjecture is REJECTED: refuted; restriction to char≠2 is preserved explicitly as U1b, never substituted silently.
- Canonical negative: `PD-N?charter-u1-codex-01`, theory `char2-refutation.md`.
- Source scope caveat: finite odd-prime random agreement cannot detect the characteristic-2 obstruction.

## U1b — determinant product via tensor Gram

- Aliases: weighted checkerboard Gram; triangular product-moment determinant.
- Closest predecessor: source conjectured difference/Hankel factorization and Harris–Simanek discrete kernel; De Marchi–Usevich/earlier determinant literature under comparison.
- Separation: exact algebraic Gram identity, arbitrary characteristic except 2, no positivity or square-root normalization. Distinction is killed if this is already the predecessor's same formula/proof; mathematical route killed if a twist monomial of total degree≤2m survives.
- Cheapest test: barycentric identities in degrees below L−1, then total-degree inequality m+(m+1)>2m.
- Actual result: complete elementary proof and universal tensor determinant identity; independent reconstruction pending. After reading literature/U1-COMPARISON.md in full, classify as a reformulation/direct corollary of known Padua-like axis determinant factorization, with explicit characteristic transfer and cutoff bookkeeping. This is not a new mechanism.
- Canonical theory: `PD-T?charter-u1-codex-01`, `odd-characteristic-criterion.md`.

## U1c — corrected characteristic-free divided-alternation criterion

- Aliases: even-index barycentric Hankel minors; normalized alternation minors; complementary-minor symmetry.
- Mechanism/hypotheses: B_H(f)=Σeven f(h)/ω′(h), H_r=det B_H(t^(i+j)); for all fields require r=1,…,floor((L−2)/2). Empty ranges impose no condition. Both axes retain arbitrary distinct labelled nodes.
- Closest predecessor: U1a source conjecture and U1b determinant, classical Hankel complementary minors/subresultants; external determinant overlap pending.
- Separation: division by 2 is removed before specialization, and the corrected criterion remains meaningful in characteristic 2. Killed by any exact mismatch, failure of Δr=ΔL−r, or a residual power of 2 in the denominator.
- Cheapest decisive test, before substantial computation: derive complement relation termwise by Cauchy–Binet; count total 2-exponent against N; exact m=0,…,4 tests over odd prime fields and binary extension fields.
- Actual result: complete proof in the durable theory; exact field checks passed, symbolic check running. Full literature/U1-COMPARISON.md read: criterion is a known-axis-factor rewrite/direct corollary at mechanism level, with characteristic-free formulation and explicit cutoff bookkeeping locally proved. Whether this exact formula has appeared in print remains unverified; no novelty claim.
- Canonical theory: `PD-T?charter-u1-codex-02`, `all-characteristic-criterion.md`.

## U1d — parity-independent singularity and exact factors

- Scope: both parity choices have equal unisolvence status in every characteristic; explicit difference/minor multiplicities.
- Closest predecessor: Harris–Simanek both-parity result and source m=2 factors, U1b/U1c.
- Separation/kill: a parity disagreement over any exact field kills the universal assertion. It is a direct corollary of U1c, not a separate substantive direction or asserted new mechanism.
- Cheapest test: weighted determinant-square formula, then direct symbolic m=2,3,4 and exact specializations.
- Disposition: consolidate with U1c and its factorization record; no separate PD-N for equivalence/consolidation.

## U1e — Direct interpolation and discrete-product cubature corollary

- Scope/mechanism: use the already proved diagonal product Gram matrix to write the Lagrange kernel in monic orthogonal polynomials; the same twist vanishing gives discrete-product cubature through total degree 2m.
- Closest predecessor: Harris–Simanek kernel/cubature, classical weighted reproducing kernels and Padua product basis. This is a direct known-method corollary, no novelty claim or new substantive direction.
- Separation/kill frozen before derivation: no mathematical separation claimed; usefulness is explicit arbitrary-field hypotheses and absence of square-root normalization. Any zero required norm under the criterion, or failure of weighted evaluation times its proposed inverse, kills the formula.
- Cheapest test: exact matrix multiplication using VᵀWV=D/2 already proved, then degree counting for cubature.
- Actual result: complete elementary matrix proof; interpolation assumes char≠2 and the exact Hankel nonvanishing criterion. Cubature assumes char≠2 but does not assume quasi-definiteness. Discrete product alternation functional, not a continuous Chebyshev measure.
- Canonical theory: `PD-T?charter-u1-codex-03`, `kernel-cubature-corollary.md`.
