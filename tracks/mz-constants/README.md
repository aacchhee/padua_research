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

All results use provisional IDs during development. Status and acceptance are distinct: a complete development proof remains subject to the independent reconstruction and Claude handoff. Numerical observations are MEASURED. No novelty or exhaustive-literature claim follows from a proof's correctness.
