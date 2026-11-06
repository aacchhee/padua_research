# PD-T?argmax-bridge-codex-D13-relative — Finite origin-relative remainder target

ID kind: PD-T. Aliases: full finite near-phase cancellation; normalized
finite remainder; relative S-minus-M_infty comparison.
Split from: the continuing D05 full relative-reference target.
Split into: PD-T?argmax-bridge-codex-D13-endpoint and
PD-T?argmax-bridge-codex-D13-mesh, both supporting results. They are
not proved parameter cases or conjuncts of the target below.

## Statement, definitions and status

Let n>=32 be an integer, m=n+1, L=log n, and

    rho=|alpha|+|beta|<=1/2,
    a=(cos alpha+cos beta)/2.

Use the actual corrected odd-board primitive of D05-fixed-special-rows:

    h_0=1, h_i=2 (i>0),
    D_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu) cos(jv),
    G_n(u,v)=D_n(u,v)-cos(nu),
    delta_r=(1-r) mod 2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m,
    R_r=sum_(k=0)^(n-1) |(-1)^delta_r G_n(u_rk,v_r)/2|,
    S_n=(nm)^-1 sum_(r=0)^(2m-1) R_r.

For signed phases use the inherited separate evenness of S_n and the
absolute-phase conventions of the comparison objects. No exchange of
the n and n+1 meshes is made. All polynomial collisions are evaluated
by the displayed finite polynomial, including its exceptional highest
first-coordinate mode. The inherited folding preserves the original
endpoint normalization; no endpoint weight is deleted.

The unchanged completed model is precisely D02-far-bias-identity's

    M_infty(phi,L)=B0(phi)L^2+b_full(phi)L+C_infty(phi),
    B0=4a/pi^2, C_infty=E_infty+K_0.

Its b_full, weighted continuous E_infty and regular finite part K_0
are the complete D02 definitions. Define, at the same integer n,

    Rrel_n(phi)=[S_n(phi)-a S_n(0)]
                 -[M_infty(phi,L)-a M_infty(0,L)].              (1)

The target is to exhibit explicit finite nonnegative constants K1,K2,
independent of n and phase, and prove throughout the stated domain

    |Rrel_n(phi)| <= K1*rho*(1+L)/n
                         +K2*rho^2*(1+L)^2/n.                 (2)

Overall status: **OPEN**. No values of K1,K2 satisfying (2) for the
complete primitive are established in this block. The target is not
rejected and is not PARTIAL: the supporting endpoint and scalar mesh
theorems do not prove a case or conjunct of (2). Its n>=32 floor is
part of the target and of those supporting statements, not a claimed
new argmax onset.

## Exact remaining decomposition

Retain D05's K_fixed at R=2, D07-global-outer's intermediate G_n
(here the scalar intermediate, distinct from the polynomial G_n(u,v)),
and D07-global-mesh's J6,C_2,Rmesh,Rlog. Put

    Erow=S_n-K_fixed, Eout=K_fixed-G_n, Eret=J6-C_2,
    delta_a X=X(phi)-a X(0), d=(sin beta-sin alpha)_+.

The exact D07 identity gives the minor algebraic identity

    Rrel_n=delta_a Erow+delta_a Eout+delta_a Eret
                         +delta_a Rmesh+(d/pi)Rlog.            (3)

Here d(0)=0. All terms in (3) retain the original full endpoint
constant, finite six rows and exact upper mesh index m-1=n. The
identity is valid at collisions by the established complete weighted
definitions. Subtracting the origin in this identity is not itself
an estimate for its unresolved terms.

| Component or supporting piece | Status and exact scope |
|---|---|
| Fixed endpoint reference inside Erow | D13-endpoint-reference PROVED developer result: its Q_ep increment is <=a*rho*(2H_n+10)/n, on J_L=2,...,floor(n/2), J_R=3,...,floor(n/2), including the entire unchanged Delta_2. Distinct review pending. |
| Scalar mesh terms in (3) | D13-mesh-support PROVED developer result: their combined absolute charge is <=rho*(L+7/3)/n. Distinct review pending. |
| Cancellation perturbation on actual ordinary rows | Existing D03 estimate <=112P H_n/(pi*n), P=sin alpha+sin beta<=rho. Its origin value is zero wherever the ordinary-row decomposition applies. This is an inherited support, not a D13 result or a complete Erow estimate. |
| Complete delta_a Erow | OPEN: central reference remainder and weighted pole approximation increment are not controlled here; a collision-safe assembly must retain the complete actual weighted row. |
| Complete delta_a Eout | OPEN: relative quadrature and missing-cell integrals for the regular F profile, with actual phase-shifted cells, need a uniform finite-n allowance. |
| Complete delta_a Eret | OPEN: all six actual polynomial rows minus the unchanged C_2 must cancel their actual origin values. Existing absolute row bounds do not supply this. |

The endpoint result is deliberately not identified with all of Erow.
For a central reference split away from collisions, its complementary
row set is O6 minus the fixed endpoint labels above, including the
parity-dependent transition rows. Separate unweighted pole or reference
terms need not be continuous at a collision even though the complete
weighted row is continuous. A proposed proof must account for their
cancellation or justify a complete-expression limiting argument.

## Preserved obstructions and unsuccessful shortcuts

D10-axis-obstruction gives a positive alpha^(3/2) term in the true
constant's origin-relative increment. That refutes the quadratic
true-constant shortcut in its stated scope. It does not refute (2),
which subtracts the true completed model and concerns a finite-n error.
PD-N079's nonquadratic finite-primitive behavior and PD-N132's required
full logarithmic coefficient likewise stay in force.

The accepted absolute allowance Ehat would give only
|Rrel_n|<=Ehat(phi)+a Ehat(0); that has no vanishing rho factor.
This inference is abandoned as a proof of (2), with no new negative
theorem. Similarly, the existing entropy variation allowance may
produce rho*log(1/rho)/n. Its displayed bound cannot be replaced by
K*rho/n uniformly as rho tends to zero. This is a limitation of that
estimate, not evidence that the exact relative outer remainder has
such a term.

## Dependencies, checks and next step

The candidate's completed inherited gate identifies D03, D04, D05,
D07, C11 and D10 as closest predecessors and preserves every considered
route. No historical-priority or exhaustive novelty claim is made.
The exact algebra (3) uses accepted D05/D07 definitions; the new two
supporting theorems are separately frozen for independent review.

No numerical job was run: no scalar control, board evaluation, native
call, phase cover, quadrature, root computation, degree scan or fit.
The next mathematical step is a proved uniform increment estimate for
one of the three unresolved complete terms in (3), with all origin
subtractions made before estimates. A useful bound on (2) additionally
requires their joint assembly and distinct review. No new onset,
finite certified range, near correction or old-source change follows.

## History

2026-11-06; rules/input e13a538bda80e6cc785f4835937b2ca338bc1d6f.
Parent-requested Astra ultra, prospectively justified in LOG D13;
runtime serving metadata unexposed. The interrupted paper-only block
was resumed with at most fifteen further minutes, not a fresh unlimited
block. The original full target is retained verbatim in mathematical
content; substantive support is split into the two files named above.
Root owns shared records, IDs and Git. Canonical attempt:
[D13-relative-remainder.md](../attempts/D13-relative-remainder.md).
