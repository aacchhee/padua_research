# MZ constants of Clenshaw–Curtis and Padua rules

Question: when does a quadrature rule of degree below twice the approximation degree still satisfy η=‖I−G‖₂<1, and how do its extreme Gram eigenvalues behave?

For Clenshaw–Curtis, Q_N is the interpolatory rule at cos(kπ/N), k=0,…,N, for dx on [−1,1]. G_(N,n) uses orthonormal Legendre polynomials through degree n. Padua means the interpolatory Lebesgue rule on [−1,1]² and total-degree polynomial spaces, including its signed weights. Node counts, quadrature exactness degree and polynomial degree are distinct.

This is a track within the campaign; it does not replace the repository charter. AC excludes Lanczos/recurrence finite-precision theory, finite-field unisolvence and bivariate moments-to-OP complexity.

- [Plan, frozen questions and round ledger](../../topics/mz-constants/plan.md)
- [Progress](../../topics/mz-constants/progress.md)
- [Literature coverage](../../topics/mz-constants/literature-search.md)
- [Development log and recovery](../../topics/mz-constants/LOG.md)
- [Durable theory](theory/)
- [Reproduction code](code/)
- [Evidence](evidence/)
- [Independent audit log](AUDIT_LOG.md)
- [Scoped negative results](NEGATIVE_RESULTS.md)

Development used provisional IDs; PR preparation allocated final PD-T013–028, PD-N002–006, LIT-042–060 and IDEA-052–076 through the shared batch ledger. Status and acceptance are distinct: the declared analytic claims passed independent Astra reconstruction, while the required Claude handoff remains pending. Numerical observations are MEASURED. No novelty or exhaustive-literature claim follows from a proof's correctness.

Audit-01 response: the headline explicit endpoint upper bound is now PD-T022's2−4/N+4/N² specialization; PD-T014 retains its short qualitative proof and PD-T015 its independent mass inequality. Original claims passed Claude's mathematical audit; focused review of the response and the new named literature gaps is pending.

## Padua MZ 2D campaign — PR14 final registration

[Two-dimensional signed Padua development](../../topics/padua-mz-2d-20261101/report.md) is registered in PD-T106–117/PD-N044–053 with their individual statuses; IDEA-210–227 retains all candidates. Exact four-size certificates and the m30 eta>3/4 witness have separate actual execution receipts. Universal signed Padua spectral bounds remain OPEN. Claude audit-01 accepted the scoped mathematics; documentation-only response-01 complete. Stage PR, draft pending AC merge order; acceptance of earlier MZ manuscript/results is unchanged.

## Signed Padua MZ frontier — audited preparation, 2026-11-05

[Frontier report](../../topics/padua-mz-2d-frontier-20261105/report.md), [Claude audit-01](../../topics/padua-mz-2d-frontier-20261105/audit-01.md) and [response-01](../../topics/padua-mz-2d-frontier-20261105/response-01.md) supersede the historical universal-OPEN wording in the PR14 section above. PD-N105/106 prove that the signed spectral extremes diverge in opposite directions along even m; PD-N107 gives the sharp fixed-ratio threshold: theta<=1/2 is exact and every fixed theta>1/2 fails. PD-T028/110/116 keep AC's registry Status OPEN with REJECTED: refuted dispositions, linking the PROVED negative records. Their original statements/history remain visible and are not usable positive dependencies.

[PD-T297](../../topics/padua-mz-2d-frontier-20261105/theory/f4-uniform-density-bound.md) resolves the unchanged PD-T114 norm target: every m>=2,0<=n<m has actual C→L2 norm below30. This is consistent with the signed spectral divergence and with PD-N052's failed absolute-Gram majorants. [PD-T296](../../topics/padua-mz-2d-frontier-20261105/theory/f3-smooth-diamond-reference.md) is a separate positive-reference theorem, never a signed transfer. Supporting weight/localization results are PD-T294/295; the scoped one-dimensional sign-discard obstruction is PD-N104. The genuine one-dimensional PD-T027 upper-limit/uniform-gap target remains OPEN.

The new exact finite cases [PD-T298 m60](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension.md) and [PD-T299 m80](../../topics/padua-mz-2d-frontier-20261105/theory/cert-finite-extension-m80.md) have actual independent acceptances, in addition to inherited m10/20/30/40. This is no gap-free certified2..80 range. [PD-T300](../../topics/padua-mz-2d-frontier-20261105/theory/frontier-measurements.md) preserves only the original finite measurements and gate dispositions. The later [MZ cleanup](../../topics/padua-mz-cleanup-20261105/report.md), [results](../../results/padua-mz-cleanup-20261105.md) and [manuscript changes](../../topics/padua-mz-cleanup-20261105/manuscript-changes.md) record subsequent finite-witness/parity work at its own status and audit scope. The [manuscript scope and build](paper/README.md) now include signed Padua logarithmic spectral countersequences beyond half-exactness and the uniform C→L2 coefficient norm. Sharp growth constants, effective all-degree thresholds, PD-T027 and historical novelty retain their explicitly recorded unresolved scope. [Cold-storage delivery](../../topics/padua-mz-cleanup-20261105/COLD_STORAGE.md) remains pending; no external delivery is implied by a local stage.
