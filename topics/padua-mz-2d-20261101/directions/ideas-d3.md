# D3 candidate memory

Rules/base and complete gate scope: [D3.md](D3.md). All identifiers are
provisional. The bounded rounds were activated only after D1's PASS.

## IDEA?mz2d-codex-20 — Marginal harmonic witness

Aliases: coordinate compression; endpoint-cancelled U packet.

- Question / scope: a Padua minimum-eigenvalue upper estimate.
- Mechanism and hypotheses: use the exact isometry `p(x)/sqrt(2)` and PD-T018.
- Closest registry entries read in full: IDEA-066/072; PD-T018/021.
- Separation criterion: none; it is exactly their composition. A genuinely two-dimensional improvement would require a smaller asymptotic quotient than this compression establishes.
- Literature baseline / limits: known local mechanism, historical priority unresolved.
- Applicable obstruction: compression has the wrong direction for a positive lower bound.
- Novelty gate verdict: duplicate/equivalent.
- Cheapest decisive test / prewritten kill criterion: identify its Rayleigh quotient algebraically; equality with the CC quotient kills separation.
- Test discriminability: an exact identity settles equivalence, without fitting spectra.
- Actual result: the quotient is exactly CC by PD-T021.
- Disposition: equivalent; no further development and no PD-N for equivalence.
- Canonical theory: PD-T018 and PD-T021, no new ID.
- History: pre-round dependency inspection, 2026-11-01.

## IDEA?mz2d-codex-21 — Multiply two critical coordinate packets

Aliases: naive tensor log-four witness; split-degree U product.

- Question / scope: can two copies of the univariate critical witness give a total-degree Padua `log^-4` upper estimate?
- Mechanism and hypotheses: multiply x/y critical harmonic U witnesses; alternatively allocate their degrees between coordinates.
- Closest entries read: IDEA-066/072; M2 harmonic construction; PD-T101 product-U rhombus identity.
- Separation criterion: both factors must remain critical for the actual meshes m and m+1 while their product lies in `Pi_(m-1)`. Loss of either property kills the claimed tensorization.
- Literature baseline / limits: classical product construction; no novelty claim.
- Applicable obstructions: total degree is not tensor degree; the marginal fixes the x mesh; the y mesh cannot be silently replaced.
- Novelty gate verdict: variant with a testable degree distinction.
- Cheapest decisive test: compute the leading degrees before any norms.
- Kill criterion written before testing: degree above m-1, or both factors becoming fixed-ratio oversampled after a balanced split, kills this specific route to two critical logarithmic losses.
- Test discriminability: distinguishes an admissible tensor witness from an interpolation polynomial on an unrelated smaller grid.
- Actual result: critical meshes give degree 2m-1; balanced actual-mesh tensor factors have the fixed positive lower bound epsilon^4/C_*^2.
- Disposition: REJECTED: failed for the specified tensorization mechanism, with signed Padua cancellation outside its scope.
- Canonical theory / negative ID: PD-N?mz2d-codex-20, `mz2d-endpoint-tensor-obstruction.md`, PROVED.
- History: preregistered 2026-11-01 after D1 PASS.

## IDEA?mz2d-codex-22 — Control signed corners by leverage

Aliases: rank-two downdate; positive-node Schur complement; negative-corner leverage.

- Question / scope: prove positive definiteness of the restricted signed form.
- Mechanism and hypotheses: split actual signed weights into their positive part and a finite negative-corner correction. Do not assume two negatives for all m; that is a separate sign-classification obligation.
- Closest entries read: IDEA-056/065/072; PD-T101 cardinal kernel; finite MZ signed spectra. Rank updates themselves are classical.
- Separation criterion: prove the negative-corner leverage matrix has norm strictly below one in the actual positive-node metric. A bound only in the continuous metric or in the absolute-weight form does not establish this.
- Literature baseline / limits: no source sign theorem is assumed; primary-source worker handles sign coverage.
- Applicable obstruction escaped: the argument retains signed weights and the restricted degree constraints explicitly. A2 `L-infinity` bounds do not supply this metric.
- Novelty gate verdict: variant with a specified signed-metric obligation, no priority claim.
- Cheapest decisive test: derive the rank-update criterion, compute small-m leverage, and test the crude continuous Christoffel majorant.
- Kill criterion written before testing: a leverage eigenvalue at least one refutes positivity at that m; a growing crude negative-weight times continuous-corner-Christoffel product kills only that crude sufficient comparison.
- Test discriminability: finite leverage above one would give an actual counterexample; finite values below one do not prove all-m positivity.
- Actual results: exact corner weights are strictly negative for every m>=3 and have magnitude (4log m+O(1))/m^4. Their continuous rank-one norm is (log m)/6+O(1), so the crude fixed-constant subtraction fails. Positive-node leverage eigenvalues are below .424 in the actual bounded diagnostic m2,3,4,5,8,9,16,17,32; no all-m inference.
- Disposition: retained exact supporting formula; REJECTED: failed for the crude continuous-metric subroute; positive-node leverage deferred until an all-m metric estimate is supplied.
- Canonical theory: PD-T?mz2d-codex-20 exact corner formula and PD-N?mz2d-codex-21 continuous-metric obstruction, both PROVED analytically. Universal positivity/order remain OPEN.
- History: preregistered after D0 reported two negative corners in its even m10..100 measurements; root suggested the same route independently.

## IDEA?mz2d-codex-23 — Symmetrized rotated harmonic packet

Aliases: rhombus harmonic product; sum-difference U packet.

- Question / scope: seek a genuinely two-dimensional endpoint witness within total degree m-1.
- Mechanism and hypotheses: use `S=(theta+phi)/2`, `T=(theta-phi)/2`; choose same-parity cosine harmonic packets A(S),A(T) and symmetrize so the Fourier support gives a real polynomial even separately in theta and phi.
- Closest entries read: PD-T101 rhombus/product-U factorization; A2 same-mesh square comparison (audit pending); IDEA-066 harmonic witness.
- Separation criterion: both rotated factors may have frequency m-1 while every Cartesian mode still has |a|+|b|<=m-1. The resulting polynomial must have a smaller quotient than coordinate compression to support a new rate.
- Literature baseline / limits: rhombus factorization is accepted classical machinery; no historical novelty claim. A2 is contextual only.
- Applicable obstruction: polynomial symmetry and nodal parity must be checked; a large corner Lebesgue value alone says nothing about the signed Rayleigh quotient.
- Novelty gate verdict: variant with a distinct support geometry.
- Cheapest decisive test: choose an explicit finite packet and verify its Cartesian support/symmetry, then evaluate a bounded exact or floating quotient before any asymptotic claim.
- Kill criterion written before testing: invalid degree/symmetry kills the packet; quotient bounded away from zero in the tested sequence stops this bounded candidate without disproving other rhombus packets.
- Test discriminability: checks the precise admissible polynomial, not a rotated function outside the polynomial space.
- Actual results: the explicit packet F_m=p_m(cos S)p_m(cos T) is admissible by the exact support formula, but its measured quotients increase from .8817 to .9420 at m8,16,32,64,128.
- Disposition: REJECTED: failed for this packet's bounded improvement screen; no whole-family or all-m conclusion.
- Canonical theory: PD-N?mz2d-codex-22, `mz2d-endpoint-rhombus-packet.md`, MEASURED with explicit finite scope.
- History: preregistered 2026-11-01.
