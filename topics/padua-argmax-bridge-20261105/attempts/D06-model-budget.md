# D06 model-budget application — quantitative outcome

Date: 2026-11-06. Input `7db857380ab99e19998e01e4ce9832496b222a31`.
Codex Sol xhigh, parent-requested quantitative application. Rules read
at a6d7a788, unchanged. No new mechanism or historical novelty claim;
the existing D05 gate is reused. D05 math acceptance report SHA256
`dd0cc60b9d84b6b288d2d508ee60f032d63e2a1fb6b20d36fdda51a2f39e7276`.

## Preregistration, actual execution and evidence

The exact scope/method/command was written BEFORE execution in
../ideas/D06-model-budget.md. Source freeze at 16:06:31 UTC:

    code/post_audit_D06_model_budget/evaluate.py
    SHA256 9ab068b7928d9976db4b5b26cddc902eb063e592f296dcfb143e999869301413

Executed once from the topic directory:

    python code/post_audit_D06_model_budget/evaluate.py

Exit0, scalar evaluator process CPU **0.097311284 seconds**, including
imports, interval/Machin helpers and both evaluations. Soft9/hard10 CPU
limit was active. No other numerical helper, native/build/board/
integration/phase-grid/fit run occurred. Read/hash tooling is not a
numerical evaluator. The original D05 proofs and all old sources stay
frozen. Root alone owns Git/shared records.

All 48 cases and EVERY displayed error component are retained in
../code/post_audit_D06_model_budget/evidence.csv (11121 bytes), SHA256
`52dfbb5b3babe61f71a76566428eb40e44b0145a56892874543af97fa0bd0566`.
Columns give E_D04, e_mesh, e_rows, e_collision, e4, I_n, D_pole,
four T_Z shares, T_Z and total. Top-level sums use e4 and T_Z once;
their separately printed shares are not added again.

## Inputs and epistemic distinction

R=2,delta=pi/8 throughout, no parameter rescue. All N>=512 satisfy
the theorem's literal n>=32 domain. Exact radian inputs are (0,0),
(1/4,1/4),(69/50,0),(29/20,29/20),(pi/2,pi/2). The last phase is a
symbolic irrational-radian phase, not an exact rational label.

The five phase bindings below are MEASURED mpmath80dps planning values;
their CSV results are not outward arithmetic or proofs of true errors.

| Phase | a | P | d | abs(U0) |
| --- | ---: | ---: | ---: | ---: |
| zero | 1 | 0 | 0 | 1.04250325291 |
| quarter | .968912421711 | .494807918509 | 0 | 1.04377765641 |
| axis | .594820415649 | .981853530372 | 0 | .997651057339 |
| diag145 | .120502769367 | 1.98542598208 | 0 | 1.01698205056 |
| midpoint | 0 | 2 | 0 | 1 |

The midpoint coefficients and Phi_0(integer)=1 limits are entered
literally. Other bindings use the actual formula for a,p,q,U0, not
independent conservative maxima; H_n uses mp.harmonic(n).

The uniform row instead deliberately uses independent conservative
a=1,p=1,P=2,d=1,abs(U0)=8,H_n<=1+log n. The abs(U0)<=8 premise is
explicit in N1-joint-endpoint-profile.md eq(6) and C06-far-compact-error
section1. All summands are nondecreasing in these nonnegative inputs;
the entropy term u[1+log(1+S/u)] increases in u and S with continuous
u=0 limit. No simultaneous-attainment claim is made.

Uniform rows use directed 50-digit Decimal interval arithmetic and
adjacent enclosures of correctly rounded ln endpoints; the saved upper
values are then rounded UP to 12 decimal places. Pi is independently
enclosed by alternating exact rational Machin series, 70/20 terms:

    [3.1415926535897932384626433832795028841971693993751,
     3.1415926535897932384626433832795028841971693993752].

This is a conservative upper enclosure under the Python Decimal
documented correctly rounded arithmetic/ln contract and the scalar
code. Independent implementation/source review remains required; no
sampled phase cover is asserted. Source avoids binary float divisions
in its interval branch and uses exact Decimal sign negation.

## Totals and binding terms

Five columns below are MEASURED evaluations of the proved formula;
the uniform column is its directed conservative upper endpoint.

| n | zero | quarter | axis | diag145 | midpoint | uniform upper |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 512 | 2.45107720 | 2.70744908 | 2.58459234 | 2.65661911 | 2.53910852 | 4.400114125755 |
| 1000 | 1.30498581 | 1.44863269 | 1.38167116 | 1.42421264 | 1.35875758 | 2.360338946680 |
| 2048 | .66865601 | .74527275 | .71048535 | .73425685 | .69954026 | 1.213897610297 |
| 4096 | .35083713 | .39227693 | .37388054 | .38722651 | .36853842 | .637902667878 |
| 10000 | .15277206 | .17139753 | .16333605 | .16957585 | .16122063 | .277965464778 |
| 20000 | .07997310 | .08992719 | .08569259 | .08911336 | .08466389 | .145523804161 |
| 50000 | .03390126 | .03822202 | .03642052 | .03794807 | .03602458 | .061683200166 |
| 100000 | .01767651 | .01996516 | .01902371 | .01984775 | .01883165 | .032158091315 |

At n10000 the I_n share binds at zero (.0857834), quarter (.0836787),
and axis (.0572245). E_D04 binds at diag145 (.0734098) and midpoint
(.0732376). Uniform I_n=.123069475502, E_D04=.082475491123,
e4=.051095759815 and T_Z=.021323988329 dominate; D_pole is below
7.6e-7. Within e4 the finite endpoint-row allowance e_rows=.03581565
is the largest share. Tightening floating precision cannot repair
these proof constants.

## Exact budget failures without floating premises

C02-defect-dense-band.md gives usable projected floors >1/32 for
n>=160 and >1/16 for n>=4096, ONLY for noncorner odd centers with
|alpha|+|beta|<=1/2 and the stated physical coordinate guards. The
quarter phase is exactly on this near-domain boundary. The far phases
axis/diag145/midpoint do not inherit those defect floors. Comparisons
here concern spending the ERROR allowance alone; a model-to-corner
comparison would need its own premise and may spend more budget.

The standalone developer PROVED formula-only obstruction is split into
../theory/D06-budget-obstruction.md. Its exact monotone e_rows proof
kills1/32 throughout32..10000 and1/16 throughout32..4096. Its separate
quarter-phase I_n argument kills1/16 throughout32..10000. These are
lower bounds on the accepted ERROR FORMULA, not on the true model
error. No measured value is a premise. The original true-error theorem
and all possible sharper/local/relative approaches remain untouched.

Among the requested degrees the uniform upper first falls below1/16
at50000; at100000 its upper is still above1/32, so that saved enclosure
does not certify a1/32 allowance there. No all-n passing threshold is
inferred: full-bound monotonicity was not proved or used for those
finite comparisons. All future-degree claims remain unmade.

No rigorous far model-to-corner margin at n<=100000 was found among
the cited premises. Existing C08 far comparison applies from1e6 to
the old M_far, with its own hypotheses/bias. No sampled margin or
old-quantifier transfer is used to suggest a new far exclusion here.

## Disposition and next gate

The D05 rate remains accepted and unchanged, but its present absolute
error formula fails the useful1e3--1e4 allowance gate. Do not release a
validated whole-phase cover on the basis of this budget. Binding work
would have to change actual endpoint-row or interior allocation, and
the a0 E_D04 coefficient; merely more precision or retuned R/delta is
not an authorized rescue. Any new mechanism needs its own fresh gate.
The separately owned relative comparison may address nonvanishing
phase constants, but no such theorem is assumed here. No global
degree/argmax/certificate change follows.
