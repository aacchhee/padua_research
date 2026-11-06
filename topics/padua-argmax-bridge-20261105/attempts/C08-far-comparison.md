# C08 far comparison — current work

Fresh full H4 and boundary/obstruction reads completed; PR30 tables and
aliases refreshed under the unchanged whole-registry coverage. The exact
model contract is C06's full-phase R64,delta.01 family, with no new
correction. Existing diagnostic output was inspected, not rerun and not
promoted to proof.

The weighted reciprocal-pair coefficient bound is now a written
developer proof in theory/C08-far-weighted-coefficient.md. It gives
b_full-b_c<=3(1-a)/pi^2, including a=0, and makes the logarithmic
comparison strictly decrease for L>3/8 away from the origin. This is
a substantive auxiliary lemma, separately labeled PROVED pending
independent reconstruction; the full comparison remains OPEN.

The exact remaining sufficient obligation is C_far<=5/2 on the closed
phase triangle. Together with the coefficient bound and C07's finite
corner lower bound it would give M_far+1/2<Lambda_c with rational
slack greater than1/10 for every n>=10^6,rho>=1/2. The degree reduction
is complete; the compact constant is being investigated analytically.
No executable, new numerical integral, phase sampling or fit has run.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.

The endpoint part now has a separate complete analytic developer proof
in theory/C08-far-endpoint-constant.md. Exact harmonic convolution gives
E_infty=a/3+a C(t_d)C(t_e)/pi^2<49/25. Pairing the two cutoff
increments after the sine/digamma constant cancellation gives the uniform
tail |E_R-E_infty|<1/(R-1)^2 for every R>=64. In particular the actual
model's E_64 is below49/25+1/3000. The integral constant is owned by
the complementary C08 worker; an upper53/100 now suffices. That bound
is not yet supplied, so the original model comparison remains OPEN.
No computation has run. The new NN-MOP530–555 table, all changed older
IDEA090/117/378 entries and current registry headings were read and
recorded in the candidate addendum; they do not change the Padua scope.

A useful independent fallback is now written in
theory/C08-far-corner-margin.md: retain only adjacent finite deformation
pairs on the central strip[.1,.9]. C07's sign pairing makes all omitted
pairs nonnegative. PD-T269's actual term and derivative bounds give the
explicit normalization loss28000/(n+1), while its positive cotangent
identity gives retained mass>(16/25)n/(n+1). Thus the finite corner
correction exceeds1/2 for every n>=10^6, without numerical quadrature.
This gives Lambda_c>=A_n^2+1/2-.001 and relaxes the sufficient integral
target to K<=1. The original far inequality is still OPEN pending that
integral bound; all auxiliary proofs require distinct acceptance.
