# PD-T?nn-mop-cond-codex-C3-02 — forward weak-stability target

ID kind: PD-T. This is a distinct OPEN forward-error target related to
PD-T449, whose strict backward and correction/data targets retain their
original home in the predecessor `theory/stable-solver-target.md`.
Aliases: A-LU rounding analysis; common-input residual transfer.
Split from: none. Split into: none. No stability theorem is claimed.
The forward inequality below is not substituted for PD-T449's backward
models; the algorithms and conditioning dependencies overlap.

## Statement, definitions and assumptions

The unresolved target is an informative bound

    E(A_LU(p;u),F(p)) <= C_N kappa(p) u + O_p,N(u^2),

for an expressly specified arithmetic algorithm and input domain, with
explicit useful C_N, for example polynomial in N. Here F contains all four
monic NN fields through degree N-1. E is PD-T290's maximum of four fieldwise
relative sup errors; kappa is PD-T432's induced condition for absolute node
perturbations at scale one and componentwise relative weight perturbations.
The weights are positive, nodes distinct, and all mixed indices through
degree N normal. Two mass-scaling directions are null. A remainder constant
and a precision radius are also needed for an informative finite-u claim.
The concrete candidate is the unchanged A-LU in predecessor
`code/native_mixed.py`, not a newly claimed coupled updater.

## Status by part

Overall status: **OPEN**. The measured finite-grid comparison has a separate
home, [c3-grid-measurements.md](c3-grid-measurements.md). No C is proved and
M3 is not activated. The routine linearization below identifies a proof
obligation; it is not a weak-stability theorem or a PARTIAL target case.

## Depends on

PD-T286 (normal mixed defining systems), PD-T432 (physical-input Jacobian
and field norm), PD-T440 (exact identity of A and measured implementations),
PD-T441 (actual common-data image and local projection), PD-N163 (one raw
array has infinite strict backward error), and PD-T449 (original target).

## Routine reduction and the missing estimate

Fix the base input p and an exact degree-ordered polynomial basis, frozen
for this differential calculation. For each nu=(n,m), s=n+m<N, write the
monic mixed polynomial using s free lower coefficients c_nu. Stack all
these coefficients in c. The mixed orthogonality equations are

    M_nu(p)c_nu + v_nu(p) = 0.

All M_nu are invertible by normality. Let M be their block diagonal stack,
and let H be the derivative of the stacked equations with respect to p,
holding c fixed at its exact value. Differentiation gives

    Dc(p) = -M^(-1) H.

Row scaling merely replaces M,H and residual coordinates consistently.
For an approximate polynomial stack c+dc at the original p, its defining
residual is exactly r=M dc, since the equations are affine in c. Thus
dc=M^(-1)r. This identity does not say that r is induced by nearby common
nodes and weights.

The exact coefficient-extraction map G(c,p) is smooth near the exact polynomial
stack when its predecessor-column matrices retain full rank. Its explicit
p argument includes the degree-N node polynomial and any input-dependent
multiplication or terminal representation. In A this is
the multiplication relation, extraction of b from the leading coordinate,
and full-rank one/two-column least squares for a, averaged over successors.
At normal data the two interior predecessors are independent: their monic
leading terms agree and their difference is a nonzero multiple of the
preceding polynomial, by the nonzero interior divisor in PD-T288. Write
L=D_cG and Q=D_pG, with the other argument held fixed in each derivative.
The physical output linearization is

    DF = Q - L M^(-1) H.

For an arbitrary nearby polynomial stack and an explicit extraction-input
change dp_direct, the first-order output change is

    dF_alg = L M^(-1) r + Q dp_direct
             + e_extract + e_basis + higher order.

Here the last terms account for additional extraction and basis arithmetic;
no bounds for these sources are asserted. If S scales physical input coordinates and
W divides each output coordinate by its field sup norm, then

    kappa = || W (Q - L M^(-1) H) S ||_(infinity -> infinity).

In particular the terminal derivative is an explicit Q term because the
stack c excludes degree N. A completed analysis
must bound the actual algorithmic source operator T in

    || W T ||_(infinity -> infinity) <= C_N kappa,

including formation, solves, extraction, basis generation and terminal
extension. Even granting standard local LU residual bounds does not supply
this comparison: those bounds address independent matrix perturbations,
whereas H uses the same common input at every mixed index. Substituting
`C=||WT||/kappa` defines an unknown amplification ratio; it proves no useful
uniform bound on C_N. A measured ratio E/(kappa*u) is a different object.

There is also a simple rank warning. The residual stack has

    d_c = sum_(s=1)^(N-1) s(s+1) = N(N-1)(N+1)/3

coordinates. Physical input dimension after mass gauges is 3N-2, so
rank(H)<=3N-2. For N>=3, d_c>3N-2. Hence some independent residual
directions are outside range(H). This proves only that one cannot represent
every independent mixed-system residual by a common first-order input
change. It does **not** prove that A-LU realizes those directions, that L
does not annihilate them, or that a forward kappa bound is impossible.

## Projection does not close this gap

PD-T441 supplies a local nearest-compatible map in a frozen positive
definite coefficient norm. Its input derivative is A_W^+ and its image
derivative is A A_W^+, where A=DF(p). To turn this into joint O(u) stability,
one still needs bounds for both the tangential and normal algorithmic error
and for the input pseudoinverse in the declared norms. The existence of a
finite local inverse constant, with unrestricted input/N dependence, is
insufficient. PD-N163 already prevents a literal strict backward reading
of every unchanged rounded output. Neither fact refutes forward stability.

## Algorithm-domain issue to resolve before a general theorem

The frozen implementation accepts N and a family name, builds an
equidistant uniform-grid basis, and sets every degree-N polynomial's lower
coordinates to zero. This is the exact terminal representation for that
fixed grid. It is suitable for the stated frozen-family experiment. A
general nearby-input algorithm must specify how it accepts perturbed nodes,
constructs the common basis, and updates the degree-N node polynomial.
One cannot silently apply the current zero-lower-coordinate terminal rule
to arbitrary perturbed nodes. This observation changes no frozen run.

## Sources, checks, scope and next step

No fresh primary-source stability theorem is imported. LIT-347's weak
stability observations are repository-mediated context and use their
step-line normalization; they do not prove this NN assertion. The reduction
is elementary differentiation and dimension counting, not a computer proof.

The next bounded mathematical task would be a concrete bound for the full
algorithmic source operator T relative to the physical Jacobian, after
fixing the nearby-input and terminal conventions. An all-input or all-N
weak-stability theorem, a uniform joint correction/data bound, and a proved
C4 excess-loss obstruction all remain OPEN. No arbitrary dimension-only
constant, extrapolated fit, or conditional residual inequality is reported
as a weak-stability result.

## History

2026-11-06; Codex gpt-6.1-sol xhigh; rules/source
`b4a04981d42c7cd872957facf5e3995e4096ca67`. C3 preserves the original
target and records the missing norm transfer after two proof routes made
no substantive progress; candidate dispositions are in `attempts/C3.md`.

## Response clarification — 2026-11-06

Audit-01 MINOR-8: the forward target now has its own provisional ID. Its
inequality and OPEN status are unchanged. PD-T449 retains its original
strict raw-array and correction/data backward targets; shared algorithmic
dependencies do not make the forward statement an equivalent reformulation.
