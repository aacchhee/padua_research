# D2 candidate gate and bounded round ledger

Rules read: `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; unchanged rules at the campaign main update `806cc7b4509fd93bae652f9545d32d95529f8281`. Developer: Codex, requested gpt-6.1-sol xhigh. No Git authority or final-ID allocation.

## Gate completed before D2 mechanisms

Inspected the complete headings, IDs, aliases and summaries of `state/IDEAS.md`, and read its full canonical/historical/seed/current MZ, lattice, programme and bivariate-Lanczos obstruction and disposition tables. Screened `literature/INDEX.md` for Padua, signed weights, Lebesgue, Hankel, Schur, tensor, alias, Z-matrix, positive, spectral, Marcinkiewicz and Fejer terminology. Read full IDEA-053/055/056/060–064/072–076 and their linked M1/M3 proofs, the Padua marginal foundation, PD-T021/028, negative records PD-N002/003, campaign definitions, existing MZ code and manuscript. Closest predecessor is the accepted one-dimensional absolute-coefficient comparison, not an unexamined source proposal. Literature primary-source checks are assigned separately; this worker claims no exhaustive historical coverage or priority.

D1's finite-family decomposition verdict PASS was received before generating D2 mechanisms. D1 supplies finitely many tensor Toeplitz/Hankel kernels under triangular masks, with generic logarithmic mask bounds, not the mass-normalized threshold below two.

## IDEA-212 — transfer the one-dimensional coefficient sign proof

Aliases: signed-Padua Z-matrix; absolute-coefficient comparison; diagonal sign switching.

- Question / scope: prove `Q_m(p²)<2 integral(p²)` on total degree `m−1`, all `m>=2`, by the exact M1 sign-replacement step, allowing a diagonal switch of coefficient signs.
- Mechanism and hypotheses: in the product-Chebyshev basis, require `A=2H−R` to have nonpositive off-diagonals after sign switching; combine with a favorable defect quadratic form on nonnegative coefficients.
- Closest registry entries (read in full): IDEA-060/062/063/073, PD-T014/022 and PD-N002/003.
- Separation criterion vs closest entry: the two-dimensional signed form would retain the same switchable off-diagonal sign property. One positive sign product around an odd cycle kills that property, invariant under every diagonal sign switch.
- Literature baseline and search limitations: local proof transfer only; classical Z-matrix arguments are known; no novelty claim.
- Applicable obstructions and exact hypotheses broken: tensor mass entries can be positive when both coordinates change; signed quadrature cannot supply positivity.
- Novelty gate verdict: variant with an explicit two-dimensional sign-property test.
- Cheapest decisive test: inspect the three modes `1,T2(x),T2(y)` in the exactness range before forming a large matrix.
- Kill criterion written before proof: a three-cycle with product of its three nonzero off-diagonal signs positive disproves switchability to a Z-matrix.
- Test discriminability: this kills the specified coefficient comparison, not positive definiteness of A or the universal upper target.
- Actual test results and committed evidence: exact cycle `1,T2(x),T2(y)` has positive off-diagonal sign product for every `m>=3`, invariant under every switch. At `m=4`, `H−R` also has entries `−4/9` and `2/15`. Complete written proof in the linked PD-N.
- Disposition and precise rejected scope, if any: **REJECTED: failed**, for this coefficient-sign transfer on every `m>=3`; no spectral threshold is refuted.
- Disposition reason: PROVED failure of the required switchable Z-matrix property; a separate exact mixed-sign witness kills the inherited defect sign.
- Canonical theory / negative-result ID: [PD-N045](../../tracks/mz-constants/theory/mz2d-upper-sign-obstruction.md), PROVED analytic mechanism failure.
- Topic / audit / history: D2; Claude audit pending.

## IDEA-213 — direct nodal domination by doubled tensor CC

Aliases: checkerboard density bound; tensor Lebesgue weight majorant.

- Question / scope: can the signed Padua form first be controlled by the positive tensor rule using `wPad(j,k)<=2 wCC_m(j) wCC_(m+1)(k)` at every retained node?
- Mechanism and hypotheses: discard negative weights and use a nonnegative nodal majorant. Any subsequent tensor estimate must still account for total degree; this weight condition alone does not prove the desired threshold.
- Closest registry entries (read in full): IDEA-056/072 and PD-T021, plus M1/M3 positive-weight bounds; D0's same-grid tensor control is measured only.
- Separation criterion vs closest entry: a pointwise upper majorant controls complementary modes, whereas marginal compression does not. A retained node whose ratio exceeds two kills the proposed nodal majorant.
- Literature baseline and search limitations: elementary standard comparison, no priority claim; no primary theorem is imported.
- Applicable obstructions and exact hypotheses broken: signed weights prohibit weighted Cauchy–Schwarz; a one-sided majorant can still hold despite negative weights.
- Novelty gate verdict: variant with a specific pointwise inequality.
- Cheapest decisive test: inspect nodewise ratios for `m=2..20`; replace any detected failure by a hand-checkable small-degree exact calculation.
- Kill criterion written before testing: one positive retained weight strictly larger than twice its tensor counterpart rejects this exact pointwise statement.
- Test discriminability: a nodewise failure does not refute a polynomial-space Loewner comparison or any spectral threshold.
- Actual test results and committed evidence: floating `m=2..20` diagnostic found ratios above two; the exact `m=2` node `(0,−1)` has Padua weight `4/9` and tensor weight `4/27`, ratio three. Hand-checkable cardinal and moment proof is in the linked PD-N; full diagnostic command/provenance in directions/D2.md.
- Disposition and precise rejected scope, if any: **REJECTED: refuted**, universal pointwise factor-two majorant.
- Disposition reason: PROVED exact counterexample at `m=2`; a restricted polynomial-space Loewner comparison is not refuted.
- Canonical theory / negative-result ID: [PD-N046](../../tracks/mz-constants/theory/mz2d-upper-tensor-obstruction.md), PROVED analytic counterexample.
- Topic / audit / history: D2; bounded second round; independent audit pending.

## IDEA-214 — parity-block Schur control with tensor diagonal blocks

Aliases: mixed-parity alias block; normalized cross contraction; block Schur complement.

- Question / scope: bound the signed mixed-parity block without replacing each tensor moment by its absolute value, and close `2H−R>0` for every m.
- Mechanism and hypotheses: for even m split each preserved x-parity block by y parity; for odd m interchange coordinates. Set `A=2H−R`, `D=diag(A00,A11)`, and `C=A01`. The exact target is equivalent to positive diagonal blocks and `||A00^(−1/2) C A11^(−1/2)||<1` in each block. A useful new route must reduce these obligations to explicit one-dimensional kernels with bounds uniform in m; merely restating Schur positivity is not a theorem.
- Closest registry entries (read in full): IDEA-056/073, D1 decomposition and PD-T014/022; standard Schur complements are not new.
- Separation criterion vs closest entry: preserve cross-block cancellation lost by entrywise absolute values and produce an actual one-dimensional contraction inequality. Failure to derive such an inequality within the bounded round leaves the target OPEN and this route deferred.
- Literature baseline and search limitations: standard operator comparison and D1 local formulas only; no novelty claim.
- Applicable obstructions and exact hypotheses broken: the Z-matrix cycle obstruction is escaped by retaining blocks, but signed weights and triangular masks still require independent mass estimates.
- Novelty gate verdict: variant with a specified block organization; survival requires a concrete estimate, not the equivalent Schur statement.
- Cheapest decisive test: write the parity block kernels and compare their diagonal terms and mixed alias supports before any large experiment.
- Kill criterion written before testing: an actual nonpositive A block refutes that block target; otherwise stop after the bounded analytic round if no mass-normalized contraction bound results. Lack of proof is deferred, not a PD-N.
- Test discriminability: exact block formulas isolate the missing inequality; finite positive examples cannot prove uniform contraction.
- Actual test results and committed evidence: exact parity and mixed-kernel formulas written in the OPEN theory record. Small floating `m=3..15` Schur diagnostics were below one, with maximum about `.685`; provenance and all values in directions/D2.md. No all-degree positive diagonal-block or mass-normalized contraction estimate was derived.
- Disposition and precise rejected scope, if any: **deferred**, after the bounded third round; universal upper target **OPEN**.
- Disposition reason: no proved mass-normalized contraction inequality. Resume with an actual one-dimensional estimate of the combined mixed kernel and diagonal-block floors; finite agreement and generic logarithmic mask bounds are insufficient. This is not a PD-N.
- Canonical theory / negative-result ID: [PD-T110](../../tracks/mz-constants/theory/mz2d-upper-open.md), OPEN; no negative ID for mere deferral.
- Topic / audit / history: D2; at most one final bounded analytic round; independent audit pending.

## Round ledger

1. Sign comparison: exact invariant triangle kills direct transfer for every `m>=3`; scoped PD-N045 retained.
2. Pointwise tensor weight comparison: exact `m=2` ratio three kills doubled nodal majorant; scoped PD-N046 retained.
3. Parity-block comparison: remaining mass-normalized contraction and diagonal positivity are unproved; route deferred, target OPEN. **D2 STOP.**
