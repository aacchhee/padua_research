# D1 gate and retained candidates — 2026-11-05

Rules/source head: 823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1.
Base: b4d292eea5eed373002506d5e16a3761bd7ae10e.
Developer allocation: gpt-6.1-sol xhigh; no Git authority.

## Search and reading scope

Read complete state/IDEAS.md section headings, aliases and summary rows,
including its campaign, historical seed, MZ, lattice, programme, bivariate
Lanczos, MZ2D, drift, PR12, argmax, cleanup and NN sections. Read obstruction
and disposition tables in those sections, including OBST01–15 and PD-N100's
literal-dictionary restriction. Relevant full entries: IDEA-031,090,117
(including alias IDEA?bivariate-lanczos-claude-041),193,376–379; full
predecessor gate/candidates and PD-T286/288/289/290 records. PD-T136/137 were
fetched at the pinned SHA after their paths were initially absent and read.
PD-T058/059's statements, conventions and proofs were consulted as context.
The predecessor numerical code and its exact-input convention were read.

Searched conditioning, condition number, sensitivity, Jacobian, moment cone,
block Krylov angles, normality, proportionality, Chebyshev system and rational
height across registry, predecessor topic, available theory, relevant
Faghih literature records and bivariate baseline candidates. INDEX rows
LIT119/347/348/562–568 were inspected before literature comparisons. The
coverage is repository-bounded; no exhaustive historical novelty is claimed.
No new PDF was cited or opened by D1. The classical NN closed-form formulas
were deliberately not used: family normality and the coarse bound are
proved from the specified weights and elementary binomial moments.

## Closest predecessors and domain restrictions

IDEA090 already proposes MOP conditioning through inter-Krylov angles;
IDEA117/379 and PD-T286/289 already define this exact NN map. PD-T136/137
differentiate an exact recurrence into a *span quotient* with Euclidean
injection norm. They do not give this coefficient map's weighted-l-infinity
induced norm. PD-T058/059 concern representing-measure moment cones and
residual normalization; their inradii are not substituted for this map's
forward sensitivity. PD-N100 kills only the literal commuting-pair reading.
Finite-support rank forbids a normality region beyond support size, and
positivity alone does not imply mixed normality. Terminal d=0 is an identity,
not a divisor used by C4 on the required triangle.

## Retained candidate records

### IDEA?nn-mop-stability-codex-D1-01 — explicit coefficient Jacobian

Aliases: moment derivative; AD-C4; induced row sum; monic path comparison.
Question: compute the NN and fixed monic step-line first-order condition
matching baseline E with a declared input perturbation norm.
Mechanism: differentiate the defining moment equations, h ratios and t
differences; evaluate the same derivative efficiently through exact C4
algebra with full 3N-column forward AD. Normality and positive field scales
are explicit assumptions. Closest predecessors: IDEA090/117/379,
PD-T286/289 and PD-T136/137. Separation: the precise coefficient-output
map and input scales differ from the existing span quotient; renaming
known differentiation is not a new mechanism. Verdict: standard variant.
Cheapest kill test: independently differentiated moments disagree at N4,
or precision escalation changes the induced norm materially. Actual result:
N4 AD-moment comparisons agree to more than250 absolute digits; full
N4,8,12,16,24,32,48,64 tables converge at180/260dps. Independent Fraction
check requested separately. Disposition: retained measured quantification
and a standard PROVED local derivative theorem. No stability theorem.

### IDEA?nn-mop-stability-codex-D1-02 — all-N rational-height bound

Aliases: binomial exponential Chebyshev normality; explicit coarse upper bound.
Question: at exact p1=2/5,p2=1/2 give an explicit all-N upper bound on the
primary NN condition. Mechanism: exponential-polynomial Chebyshev normality,
integer moment denominators, Hadamard cofactors, h determinant ratios and
analytic derivative estimates. Closest: standard defining moment systems,
IDEA376 and the local derivative candidate. Separation criterion: explicit
constants in this exact map/domain, not a new abstract perturbation method.
Kill test: a missing normality, invalid height denominator, zero field scale
or incorrect h bound invalidates the proof. Verdict: standard coarse variant.
Actual result: written proof in theory/conditioning-krawtchouk-bound.md.
Disposition: retained PROVED supporting bound, pending independent audit.
It neither proves a sharp rate nor silently closes the original growth target.

### IDEA?nn-mop-stability-codex-D1-03 — a single inverse-divisor mechanism

Aliases: G3 kappa proportional to1/min|d|; measure proximity screen.
Question/hypotheses: at fixed N8 in the two specified positive families,
does the preregistered single inverse-minimum-divisor prediction describe
the measured condition as the second parameter approaches the first?
Closest: PD-T288/289 explicitly allow small nonzero interior divisors;
IDEA090's angle mechanism is broader. Separation criterion: kappa*min|d|
should stay constant under literal proportionality; substantial systematic
variation kills this simple finite-screen description. Actual Krawtchouk
product changes from2.74e4 to8.49e11 over p gaps.1 to.005; Hahn products
change from8.68e4 to6.86e3 over beta gaps.5 to.025. Disposition: the literal
constant-product description fails over the sampled gaps; no universal
negative theorem or asymptotic exponent is inferred. No PD-N is allocated
for this finite diagnostic. Interpreting all growth as one inverse divisor
is abandoned; complete sensitivity remains retained.

### IDEA?nn-mop-stability-codex-D1-04 — sharp exponential growth law

Aliases: explicit rho(p1,p2); digits-lost theorem.
Question: prove an informative exponential lower bound and usable upper
bound for unrestricted independent input perturbations, at least on the
Krawtchouk family. Closest: IDEA090, measured tables and the coarse upper
bound. Separation: a written all-N inequality with explicit constants,
not a fit or a reparameterized family derivative. Cheapest test: derive
an exact signed Jacobian-row witness across N before estimating rates.
No all-N witness was established in round1. Disposition: deferred/OPEN;
resume with an exact sensitivity representation, not extrapolation.

## Limits and failed interpretations

Early code displayed fully componentwise output ratios at floating
near-zero coefficients. This produces precision-dependent enormous values
on exact zeros and was removed before final freeze. The mathematical
full-output condition is infinite whenever a zero output has nonzero
derivative, as already happens at Krawtchouk b2_(0,0). Componentwise-input
conditioning remains well-defined and separately tabulated. No theorem
or candidate was rejected merely because this reporting diagnostic failed.
