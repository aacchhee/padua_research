# C08 — Uniform comparison of the fixed full-phase model

Parent allocation: hard Astra ultra continuation, justified in shared LOG
before activation. Own only new C08-far comparison records; C07 and all
earlier proof bytes remain frozen. The target is

    M_far(alpha,beta;log n)+1/2<Lambda_c(n),
      n>=10^6, 1/2<=alpha+beta<=pi, alpha,beta>=0.

M_far is exactly the uncorrected full-phase H4 family specified by C06:
R=64, delta=1/100, exact infinite h_R,g_R constants, exact continuous
finite sinc endpoint profiles, and the full integral of B on the retained
interior interval. Its independent error proof is owned by C06. No
additional correction or altered family is introduced here.

## Gate and source coverage

The complete current1075-line IDEAS headings, identifiers, aliases and
summaries and every obstruction/disposition table were read in C01.
Its unchanged SHA256 is
1aecb5461537870de64711fc8f48daa683dea57c6298cbf07bda51d4c52d2718.
This whole-registry coverage is reused explicitly, including PR30.
For C08 the complete final PR30 tables and retained unnumbered aliases
were refreshed. Searches used full-phase/far-phase, constant maximum,
weighted pole/cosine profile, secant product, tangent partial fractions,
same-mesh and signed deformation across the registry, literature INDEX,
current ideas, theory and logs. No literature priority claim is made.

Full shortlisted proofs read: C06 far-profile/comparison and candidate;
N1-04/05 and the entire H4 N1-06/07/08 assembly, including its corrected
double collision; full PD-T365 and PD-N132, and all H2-H3 candidate
entries. PD-T159 and PD-T269/270/271 were read in full immediately before
this allocation in C07 and remain the exact corner-normalization sources.
N1-16 and C01–C04 near proofs are known predecessors, whose near-domain
statements will not be extended without a new proof. The diagnostic
source and existing35-case receipt/raw output were read; no new run was
performed, and those floating results supply no bound.

Closest mechanism: IDEA459 / C06's full logarithmic profile. This is
quantitative proof completion, not a novelty claim. PD-N132 rules out
dropping the phase-dependent linear logarithm. The boundary midpoint
also disproves b_full<=b_c; that stronger inequality is not pursued.

## Candidate C08-weighted-coefficient

Use the exact weighted reciprocal-pair series to prove

    cos(theta/2)[C(1/2+theta/(2pi))-C(1/2)]
                          <=(7/2)(1-cos(theta/2)), |theta|<=pi.

Endpoint products use their continuous limits. The distinction from
N1-16 is the full closed interval, with an explicitly retained positive
linear-coefficient excess. A negative sign assumption for b_full-b_c
would fail the boundary test. The cheapest exact test is a tangent
partial-fraction bound on (1-y^2)/cos(pi*y/2), followed by the positive
odd reciprocal sum. It passes analytically and implies
b_full-b_c<=3(1-a)/pi^2. This paper derivation occurred before this
durable candidate was written; no prospective timing before that
derivation is claimed. No executable was used.

## Candidate C08-constant-budget

After the degree monotonicity reduction, a sufficient exact claim is

    C_far(alpha,beta)<=5/2 on alpha,beta>=0, alpha+beta<=pi,

where C_far=C_R+c_mesh+(1/pi)integral_delta^(2pi-delta) B.
This claim is currently OPEN. It preserves the endpoint/integral
cancellations: bounding the three pieces independently by their coarse
global absolute values does not pass the budget. The cheapest analytic
test is a cancellation-preserving upper for that exact combined constant,
including a=0 and the two phase vertices. Failure of this sufficient
5/2 budget would not refute the requested model comparison.

An alternative is a validated fixed-domain enclosure after an exact
reduction and independently reviewed interval source. No such source,
run or computational proof is currently authorized as completed work.
Any proposed run must specify its finite cover, endpoint/collision
enclosures, quadrature tails and resource cap first. Finite samples,
adaptive floating error estimates and an unbounded degree scan cannot
establish the target. The existing diagnostic is MEASURED only.

## Other alternatives and current disposition

- Global b_full<=b_c: rejected as an inference by the exact midpoint
  b_full=4/pi; the weighted excess route replaces it explicitly.
- A phase-blind C06 constant200: valid predecessor, insufficient for
  the million-degree target; changing the degree alone is not this task.
- Transfer the near-only C04 theorem across rho=1/2: excluded without
  a new domain proof; its numerical constant is contextual only.
- Full compact constant comparison: active; target OPEN until an actual
  uniform analytic or validated enclosure is supplied.

2026-11-06, rules/input4b728b04216a5490910780bc609a82b853058426.
Codex, coordinator-requested Astra ultra; serving metadata unexposed.

## C08 endpoint continuation and updated-registry addendum

The newly merged NN-MOP registry has1112 lines, SHA256
68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d.
All its headings were rescanned, the full added IDEA530–555 disposition
table and retained scope paragraphs were read, and the changed IDEA090,
IDEA117 and IDEA378 summaries were read. Their NN coefficient-condition,
common-data and coupled-update scopes provide no competing Padua
endpoint mechanism. The earlier complete unchanged registry coverage,
including every older obstruction table, remains the baseline. No new
external theorem or attribution claim follows from this addendum.

For the compact constant, the endpoint cancellation is now a separate
candidate: set E_R=C_R+D0*h_sum+B0*g_sum and seek the exact limit

    E_infty=a/3+a C(t_d)C(t_e)/pi^2,
    |E_R-E_infty|<1/(R-1)^2 for every integer R>=64,

uniformly on the closed phase triangle, with weighted endpoint products.
This is a harmonic-convolution variant of the already read PD-T159
same-mesh square and H4 finite-row formulas, not a new family. The exact
distinction is retaining the signed sine-channel constant so it cancels
with the cotangent reflection terms, then pairing the two R-tail
increments before summing. A surviving O(1/R) unpaired tail or wrong
endpoint extension kills this numerical allocation. The algebraic
convolution and paired-tail test passed on paper before this written
candidate; no earlier prospective registration of that derivation is
claimed. No computation was run. The remaining integral is separately
owned by the complementary C08 worker; it is not assumed nonpositive.

## C08 finite corner margin alternative

The already read PD-T269 central-strip approximation, combined with
C07's nonnegative finite unordered pairs, suggests the specific retained
fallback Delta_n>=1/2 for every n>=10^6. Retain only adjacent pairs
j,j+1 with both j/n and(j+1)/n in[1/10,9/10]; charge the shifted
second endpoint and the full Riemann error. This is a quantitative
variant of PD-T269/C07, not a new mechanism. A missing factor4, a
negative omitted pair, or a retained-strip error exceeding the positive
integral budget kills this allocation. The analytic constants pass before
durable proof writing, with no run. This stronger corner lower would
allow the relaxed sufficient constant budget C_far<=3, or K<=1 with
the endpoint theorem, while preserving the original target M_far+1/2.

## C08 regularized pole functional

The complementary integral worker requested an upper for the one-variable
functional H defined in C08-far-pole-functional.md. The considered sharp
variant H(x)<=cos(x/2)H(0) is deferred: it is unnecessary if a uniform
H<1/2 bound closes the enlarged corner-margin budget. The retained exact
target is H(x)<1/2 for all real x. Its cheapest test uses the already
proved global distributional Phi_0''<=12, including negative integer
atoms, and the range1/2<=Phi_0<=1. The scalar kernel is bounded by
1/v+v/16 and the positive second-difference envelope is integrated
exactly. This differs from a coarse Lipschitz bound by preserving the
quadratic upper at short distance and the range bound at long distance.
It would fail if an uncharged positive derivative atom existed or the
explicit scalar integral exceeded1/2. The analytic test passes with
749/1500; no numerical integration is performed. The previous stronger
cosine-shaped conjecture is neither proved nor refuted.

## Completed analytic comparison

The complementary worker froze K_delta<49/50 in
theory/C08-far-integral-bound.md. Together with E_64<49/25+1/3000
this proves C_far<3. The original task is now a complete written
developer theorem in theory/C08-far-model-comparison.md:

    M_far+1/2<Lambda_c-1/10,
    S_n<Lambda_c-6/25,
      n>=10^6, 1/2<=|alpha|+|beta|<=pi.

The proof uses the original fixed model without another correction.
The stronger sufficient C_far<=5/2, K_delta<=1/2 and cosine-shaped H
variants remain unproved and are not used. The exact endpoint theorem,
weighted coefficient, finite corner margin and uniform H estimate are
retained as separate substantive results. No computational route was
needed or executed. Distinct review of the final assembly and formal
audit remain separate from this developer proof completion.
