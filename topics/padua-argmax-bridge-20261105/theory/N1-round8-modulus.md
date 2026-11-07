# PD-T?argmax-bridge-codex-N1-19 — The continuous residual comparison after the branch budget

ID kind: PD-T. Aliases: entropy/fractional near-origin modulus target;
remaining C1 phase increment. Split from: the original N1-17 residual
target. Split into: N1-18 proves a supporting branch-artifact envelope;
this main comparison remains OPEN, not PARTIAL.

## Exact statement still unresolved

Overall status: **OPEN**. All definitions and quantifiers of C1/N1-17
are preserved: integer n>=10^6, alpha,beta>=0, alpha+beta<=1/2,
and exactly the unchanged N1-15 M_near. With L=log n,

    F_n=[M_near-B_M L^2-b_M L](alpha,beta)
                       -[M_near-B_c L^2-b_c L](0,0),
    G_n=(B_c-B_M)L^2+(b_c-b_M)L,
    eta=107/3584000,

the sufficient target remains F_n<=G_n+eta. N1-18 constructs a
continuous increment Q_n, Q_n(0,0)=0, and proves

    |F_n-Q_n|<J_n, J_n=9/(2n).

Hence the exact remaining sufficient obligation is

    Q_n(alpha,beta)<=G_n(alpha,beta)+eta-J_n.          (C)

This is a phase-increment comparison for the specified function Q_n,
not an unspecified O(1) remainder. The helper gives the concrete
uniform positive allowance

    eta-J_n>1/40000, n>=10^6.                         (1)

Equation (1) is a rational comparison at n=10^6 and monotonicity of
J_n. It does not bound Q_n itself. No effective onset or C1 theorem
has been proved.

## What the first test settled

The parent's proposed seam identity survives: all singular and regular
A terms cancel exactly across a strip/outer cutoff, leaving only the
integral of the explicit endpoint residue E_s. The H8 branch error can
be charged once per phase, without a degree-growing transition count.
Actual noncentral collision marks fit a uniform O(1/n) envelope after
the exact polynomial values and removed cells are compared together.
The combined budget <9/(2n) is strictly below eta.

Thus an insufficient jump allowance is not the current obstruction.
The missing obligation is a quantitative phase modulus for Q_n after
all its endpoint, pole-profile and cancellation-integral terms have
been combined. Existing spatial BV bounds control z integration and
the jump estimate; they do not provide the needed second phase
derivatives or phase increments. Applying their sup bounds at two
phases gives only a fixed O(1) allowance, larger than (1). No small
coefficient is inferred from that inadequate sufficient estimate.

## An exact square-root transition warns against assuming C2 regularity

The following is a routine geometric calculation from N1-14, not a
claimed finite-part asymptotic. On beta=0 and 0<alpha<=1/2, write
epsilon=pi-z, a=(1+cos alpha)/2, u=sin alpha/2 and
s=a tan(epsilon/2). In the opposite-sign regime s>u, the root/no-root
threshold of N1-14 is s sin epsilon=u. The identities

    s>u iff epsilon>alpha,
    s sin epsilon=a(1-cos epsilon),

give the exact opposite-sign root band

    alpha<epsilon<epsilon_*(alpha),
    epsilon_*(alpha)=arccos[1-tan(alpha/2)].            (2)

The elementary cos/tan limits give epsilon_*(alpha)/sqrt(alpha)->1.
Thus this transition has a square-root phase width. A rho^(3/2)
contribution to its integrated phase increment must be allowed until
it is controlled or canceled explicitly. Formula (2) alone proves
neither a nonzero fractional coefficient nor failure of every C2
bound for the complete Q_n. Inherited PD-T217/221 already retain
square-root numerator-sign regions; no novelty claim is made here.

Likewise N1-14's entropy expressions contain x log x and may require
a term r2*|log rho|. PD-T220 requires the exact finite-degree linear
cusp to remain, of order log n/n. Its axis formula is not silently
transferred to the full two-phase Q_n. R7's prospective K0*r2-only
modulus was never proved; it is not being used as a premise or
rejected by the root geometry alone.

## Concrete falsifiable modulus contract

Let r2=alpha^2+beta^2, r=sqrt(r2), rho=alpha+beta. A possible sufficient
estimate, still entirely unproved, is

    Q_n<=K0*r2+k*rho^(3/2)+K1*r2*log(1/rho)+c_n*rho,  (M)

with nonnegative explicit constants/functions and zero values assigned
to all vanishing terms at rho=0. The original pure quadratic contract
is the special case k=K1=0; it is not assumed. Any proof must include
both permanent central rows, the finite-h endpoint block, fixed series
constants, ordinary integrals and their exact combined phase limits.

N1-16 gives

    G_n>=A(L)*r2, A(L)=47L^2/(48pi^2)+L/(24pi^2).

If D=A(L)-K0>0, choose positive D_f,D_e,D_l with sum D. The following
routine algebraic sufficient budget then tests (M) without sampling:

    27k^4/(32 D_f^3)
      +(K1/(2e))*exp(-2D_e/K1)
      +c_n^2/(2D_l) <= eta-J_n.                      (3)

Omit the entropy term when K1=0, and omit/reallocate any part whose
coefficient is zero. To verify (3), use rho<=sqrt(2)r. Direct
one-variable maximization gives

    sup_(r>=0) [c*r^(3/2)-A*r^2]=27c^4/(256A^3),
    sqrt(r)_critical=3c/(4A),

so replacing c by 2^(3/4)k gives the first term. With x=r2 and
rho>=r, the entropy term is <=(K1/2)x log(1/x); subtracting D_e*x
and maximizing gives the second. Completing the square gives the
third. These are conditional budget identities, not proved modulus
constants. No value of K0,k,K1 or c_n satisfying (M) has been supplied.

The cheap next kill test is to derive one complete combined phase
estimate, with its exact constants, and compare (3) at its claimed
onset. A violated sufficient budget rejects only that quantitative
certificate; it does not refute C1, the actual all-n argmax theorem,
or a sharper estimate of this same model. In particular a failed
K0*r2 proof cannot be repaired by simply declaring the entropy/fractional
terms zero. No second model correction is authorized.

## Bounded-round disposition and checks

R8's first jump test is analytically PROVED in N1-18 and passes its
eta budget. The continuous modulus (M), (C) and full C1 remain OPEN.
Development stops at this bounded helper/precise remaining contract;
there is no automatic next round, integrator or extra correction.

No mathematical computation, diagnostic, fit or numerical integral was
run in R8. The finite energy range2–128 was not extrapolated. Global
certified2–40, far phases, true-corner coherence, other center classes,
B3/B4 and all-n PD-T099 are unchanged. Distinct supplementary review
of the new frozen helper is separate from the formal Claude audit.

2026-11-06. Input/rules `a8fad0526779216d184463d046591fdfea6783f6`.
Codex, parent-assigned Sol xhigh; serving metadata unexposed. The
coordinator proposed the fractional maximization identity; it is
checked algebraically above, not assumed as a phase estimate.
