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

The scalar pole functional is now bounded analytically by749/1500<1/2,
with the two-channel delta=.01 cutoff cost below.027. Its complete proof
is theory/C08-far-pole-functional.md; it uses the global one-sided
periodic curvature, including negative atoms, together with the newly
proved range1/2<=Phi_0<=1. The exact integral of the minimum of its
quadratic and range envelopes supplies the numerical bound without
quadrature or sampling.

The complementary C08 worker froze K_delta<49/50, source
445a449d83e3d575222b3832ad6adb3c401a21e2e89d1d2ced8e8b1dca860ead.
I read its full proof and checked the renormalization, cancellation sign,
sine-log primitive and finite-cutoff constants. Combining it with the
other frozen lemmas gives C_far<3. The final comparison is now a written
PROVED developer result in theory/C08-far-model-comparison.md:
M_far+1/2<Lambda_c-1/10 and S_n<Lambda_c-6/25 for every integer
n>=10^6 on the entire closed far diamond1/2<=rho<=pi. The weaker
constant budget is enabled by the independently proved extra1/2 finite
corner lower; it does not change the model or discard any earlier
correction. All previous OPEN entries in this attempt are dated working
states superseded for the original task by this completed analytic
assembly. The unused stronger sufficient budgets remain unproved.

No mathematical executable ran during C08. Distinct reconstruction and
formal audit remain separate; global integration and smaller degrees
are owned by the coordinator. Every earlier C01–C07 proof is unchanged.

Before the final assembly freeze, the complementary integral reviewer
requested one MINOR zero-phase correction: its intermediate positive
sine estimate uses <= rather than < when p=0. The corrected source is
e76a45698ab5c0f2af53816fb74487fb929eff99011e8004e9f79e3f84f8f7a5;
the final strict K_delta<49/50 and all assembly constants are unchanged.
The final comparison pins this corrected source. The previous hash above
is retained as the actual earlier development freeze.
