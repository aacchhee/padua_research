# H04 smooth-residual quadrature — prospective PAPERONLY attempt

Rules/input ad257038cdff1d66f6e9c03d7ed43405c76cf6b0, 2026-11-07.
Parent-assigned mathematical developer; inherited serving metadata not
independently exposed. Root owns Git/LOG/shared state. This worker owns
only ideas/attempts/theory H04-smooth-quadrature.md. No subagents or jobs.

## Preregistration before derivation

Write m=n+1, t_r=r/m, a_r=(1-t_r)/2, w_r=cot(pi t_r/2), and

    B(x)=cot(pi x)-1/(pi x)+1/[pi(1-x)],
    V_n=sum_(r=1)^n w_r sum_(l=0)^(r-1) B((l+a_r)/n).

Target, for all integer n>=2 and both parities: constants C0,C1 and a
concrete finite uniform K such that

    |4 V_n/(nm)-C0-C1/n| <= K(1+log n)/n^2,

or a stronger bound. The constants may be elementary one-dimensional
integrals of the smooth pole-subtracted B, with every endpoint defined.
No exact one-index evaluator is assumed. A_n is precisely PD-T270's
(2/pi)(log n+gamma+log(8/pi)); the harmonic part of F03 (7), its use with
A_n, and the full normalization compensation are outside H04's target.

Read before registration: AGENTS/WORKFLOW/CODEX; complete accepted
campaign-H-gate.md and campaign-H release; complete F03 trio and
PD-T269/270/271; H01/H02/H03 registrations. The support route is a
quantitative variant under that completed gate, with no priority claim.

First test: exact center and midpoint-cell union for each actual partial
row; derive the signed endpoint-displacement coefficient and outer zero
endpoint removal before bounding errors. In particular test the possible
vanishing 1/n coefficient instead of presuming it from symmetry.

Kill/defer: wrong center/cell limits, discarded endpoint or parity,
unremoved cotangent singularity, or no uniform summed remainder at
O(log n/n^2). Preserve any established lemma and exact remaining gap;
do not refute PD-T098 because this support route fails.

At registration only read/search/metadata and owned prose writes occurred.
No numerical/scalar/native/degree/endpoint/quadrature/compiler/source job,
code, import, external theorem/PDF, Git or shared-file mutation.

## Work record

The parent's suggested cell-center algebra was treated as an unchecked
question and independently verified after registration. The r sample
cells have exact union [-t/(2n),t+t/(2n)] and exact center t/2. Their
endpoint displacement produces the first term in

    inner=n I(t)+(t/2)(B(t)+1/pi)+e_(n,r),
    |e_(n,r)|<=17t/(16n).

The locally proved bounds |B|<=5,|B'|<=3,|B''|<=5 on [-1/4,5/4]
and W=t*cot(pi*t/2)<=1,|W'|<=3,|W''|<=5 on [0,1] make this uniform.
For F=cot(pi*t/2)I(t) and G=W(B+1/pi), the outer removable endpoints
are F(0)=2/pi^2,F(1)=0,G(0)=4/pi^2,G(1)=0; F''<=36,G''<=50 in
absolute value. Composite trapezoid estimates give exactly

    4V_n/(nm)=C_B+beta_B/n+R_n, |R_n|<=17/n^2,
    C_B=4 integral_0^1 cot(pi*t/2)I(t)dt,
    beta_B=-4/pi^2+2 integral_0^1 G(t)dt.

The exact endpoint charges combine as
-4/(pi^2*m)-4/(pi^2*n*m)=-4/(pi^2*n); no uncontrolled n versus m
substitution occurs. The proof covers all n>=2 and both parities.

The optional zero-coefficient subguess fails: elementary cotangent
inequalities give 0<G(t)<(4/pi^2)(1-t), hence -4/pi^2<beta_B<0.
This is an analytic strict inequality, not an evaluated fit.

The complete proof is ../theory/H04-smooth-quadrature.md. The support
target is PROVED in development, with distinct review still separate.
The harmonic part of F03 (7) and the full corner target remain outside
this lane. Formulas were sent early to the root, H01/H02/H03 and H06.
No unsuccessful alternate route or new H round was launched. The
nonvanishing first coefficient is retained rather than removed by a
centering assumption. No scientific computation, code or Git action.

## Runs needed

None authorized or planned: PAPERONLY. Distinct mathematical review is
needed before root adoption of any substantive proof.
