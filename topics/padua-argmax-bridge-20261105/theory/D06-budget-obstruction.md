# PD-N?argmax-bridge-codex-D06-budget — Obstruction to spending the frozen D05 allowance

ID kind: PD-N. Aliases: positive endpoint-row budget obstruction;
quarter-phase interior allowance floor; unmodified D05 budget kill.
Split from: D06 quantitative application, not from the true-error theorem.
Split into: none.

## Exact statement and negative scope

Let B_n(alpha,beta) be exactly the NONNEGATIVE right side in (2) of
D05-outer-comparison.md, with fixed R=2 and delta=pi/8:

    B_n=E_D04+e4+I_n+D_pole+T_Z.

Every term is the proved error FORMULA, not the actual error. For the
entire closed phase diamond, by separate absolute phases, one has

    B_n>1/32 for every integer 32<=n<=10000,             (1)
    B_n>1/16 for every integer 32<=n<=4096.             (2)

At the particular admissible near-boundary phase alpha=beta=1/4
(exact rational radians), the stronger formula obstruction is

    B_n(1/4,1/4)>1/16 for every integer 32<=n<=10000.   (3)

Status: **PROVED**, elementary analytic formula-only obstruction;
distinct review pending. Candidate disposition: the UNMODIFIED D05
absolute-allowance route fails the stated small-degree budget gate.

This does not assert |S_n-M_infty| exceeds either budget, and does not
refute the accepted D05 upper bound or rate, the exact model, phase-local
future bounds, phase-relative cancellation or any argmax theorem.
It only shows that spending this particular positive error formula
cannot certify those allowances in the specified ranges.

## Dependencies and applicable budgets

D05-outer-comparison.md gives all formula definitions and their domain
n>=32 for R2,delta=pi/8. The useful projected defect floors >1/32
(n>=160) and >1/16 (n>=4096) are exactly C02-defect-dense-band.md's
near-half-diamond, noncorner-odd-center statements with their coordinate
guards. The mathematical formula inequalities here also cover smaller
n>=32; no defect floor is claimed there. The quarter phase has
|alpha|+|beta|=1/2 and belongs to that phase guard. Far phases do not
inherit those projected floors.

Only elementary bounds pi<4, pi^2<10, log10000>9, log4096>8 and
log32>3 enter the proof. For a direct verification of the logarithmic
bounds, e=sum1/k! satisfies e<11/4 (the tail from k=4 is at most
(1/24)sum_(j>=0)4^-j=1/18), hence e^9<(11/4)^9<10000 and
e^8<(11/4)^8<4096. Also e^3<(11/4)^3<32. These are rational
inequalities. The familiar pi bounds are also contained in the
upstream C02 estimates; no numerical evaluator output is a premise.

## Proof

All summands of B_n are nonnegative on the stated domain. The R2
finite endpoint-row term simplifies exactly to

    e_rows(n)=(181+19log n)/n+21600/n^2.

Its derivative is

    [19-181-19log n]/n^2-43200/n^3<0   for n>=1.

At n10000 use log10000>9 to get

    e_rows(10000)>352/10000>1/32.

At n4096 use log4096>8 to get

    e_rows(4096)>333/4096>256/4096=1/16.

Monotonicity and B_n>=e_rows prove (1)--(2), with all degree floors
inside the actual D05 theorem domain.

For (3), a=cos(1/4)>=1-(1/4)^2/2=31/32. At delta=pi/8 the
coefficient of L=log n in I_n is exactly

    VA/2+9Astar=9/pi+640a/pi^2>9/4+62=257/4.

The other interior definitions give Vstar>=6,VV>=23,Jstar>=5,
VJ>=20. Thus the non-L part satisfies

    VW/2+5Wstar+4Vstar>=131/2+35/pi>297/4.

All remaining central-log charges are nonnegative. Consequently

    I_n(1/4,1/4)>f(n):=[257log n+297]/[4(n+1)].

For n>=32, the derivative numerator of f is
257(1+1/n-log n)-297<0, using log32>3 and 1+1/n<2.
Therefore for every 32<=n<=10000,

    B_n>=I_n>f(n)>=f(10000)>1305/20002>1/16.

This proves (3), without any sampled phase values or numerical
integration. The proof does not lower-bound the true model error.

## Evidence, limitations and next gate

No computational premise or external literature theorem is used.
The separate D06 CSV contains MEASURED actual-phase planning values
and conservative directed uniform upper endpoints; it is not evidence
needed for (1)--(3). Those arithmetic/source claims require their own
independent check. No parameter retuning, old-source retry or model
correction is proposed by this negative result. The next route must
change an actual allocation/cancellation or separately prove a new
local/relative allowance, under a fresh gate.

History: 2026-11-06, parent-requested Codex Sol xhigh, input
`7db857380ab99e19998e01e4ce9832496b222a31`. Split at root's explicit
request from attempts/D06-model-budget.md; no old D05 claim changed.
