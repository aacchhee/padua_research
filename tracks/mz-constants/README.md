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
