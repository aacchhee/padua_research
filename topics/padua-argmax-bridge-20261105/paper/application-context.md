# Application context for the introduction

Adopted in the introduction on 7 November 2026, source commit
4050f6861a44a88ec5d7941787703fbbe9d9ce4a. The following records the
proposal and its source checks. AC asks whether the original
Van Barel–Chesnokov paper can be cited naturally, alongside a few Padua
applications. The approved paragraph supplies application context for the existing
interpolation results. Its three citations are included in the bibliography.

Place one short paragraph after the opening discussion of stability and
the general Padua construction, before the main theorems. Group concrete
computational uses of Padua sampling; three references are sufficient.

> Padua sampling has also been used in computations of discrete bivariate
> orthogonal polynomials and least-squares approximations [Van Barel and
> Chesnokov, 2010], in Nyström and collocation methods for two-dimensional
> Fredholm integral equations [Laguardia and Russo, 2022], and in
> continuous-variable quantum tomography [Landon-Cardinal, Govia and Clerk,
> 2018]. These applications motivate a precise understanding of the
> associated interpolation operator and its sensitivity to errors in the
> sampled data.

The existing operator-norm explanation gives the bridge: perturbing all
sample values by at most epsilon changes their interpolant by at most
Lambda_n epsilon in uniform norm. The 2010 reference supplies computational
context for orthogonal bases and least-squares examples. Its algorithm's
rounding-error analysis and the norm of a truncated least-squares projector
are separate questions; do not attribute such conclusions to the present
Lebesgue theorem. The tomography paper is particularly close because its
Eq.(5) explicitly invokes the Lebesgue constant in reconstruction error.

## Sources and exact reading scope

- M. Van Barel and A. Chesnokov, *A method to compute recurrence relation
  coefficients for bivariate orthogonal polynomials by unitary matrix
  transformations*, Numerical Algorithms55(2010),383–402,
  DOI10.1007/s11075-010-9392-y.
  Existing fulltext reading record: literature/records/vanbarel-chesnokov-2010.md,
  especially LIT-200/201, §5 Examples1/2, pp.396–399. Fresh publisher page
  confirms metadata, discrete orthogonal-polynomial/least-squares purpose
  and Padua keyword; fulltext is subscription-only in the fresh fetch.
  https://link.springer.com/article/10.1007/s11075-010-9392-y
- A. L. Laguardia and M. G. Russo, *Numerical methods for Fredholm integral
  equations based on Padua points*, Dolomites Research Notes on
  Approximation15(2022),39–50. Fresh primary PDF firstpage/abstract and
  introduction, plus §2.1 definition and corrected kernel, pp.39–40:
  Nyström and collocation methods on the square. No complete proof review
  or fresh numerical reproduction is claimed.
  https://emis.de/ft/41450
- O. Landon-Cardinal, L. C. G. Govia and A. A. Clerk, *Quantitative
  Tomography for Continuous Variable Quantum Systems*, Physical Review
  Letters120(2018),090501, DOI10.1103/PhysRevLett.120.090501.
  Fresh publisher-hosted accepted manuscript: abstract/introduction,
  reconstruction discussion and Eq.(5), manuscriptpp.1–2 (PDFpp.2–3).
  Padua interpolation reconstructs Wigner/Husimi-Q functions; Eq.(5)
  uses the Lebesgue constant. Do not repeat its optimal-sampling conjecture
  as a new theorem or infer final density-matrix guarantees here.
  https://link.aps.org/accepted/10.1103/PhysRevLett.120.090501

The sources were actually searched/opened using the web connector. This
is a bounded application-context check, not exhaustive literature/priority
clearance. No final LIT IDs or shared registry changes. If adopted, add
these bibliography entries and refresh the explicit alphabetical nocite
list; preserve the mathematical text and author/template changes.
