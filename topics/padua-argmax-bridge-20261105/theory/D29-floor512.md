# PD-T?argmax-bridge-codex-D29-01 — A twentieth defect from degree512

ID kind: PD-T. Aliases: D29 n512 floor; existing-H_n onset corollary.
Split from: the two-target D29 local candidate.
Split into: none. The n41 and radius-dependent results are separate.

Status: **PROVED**, analytic developer corollary; distinct review
remains required before checker adoption.

## Statement and exact scope

Let n>=512 be an integer, m=n+1, N=nm. Let0<=J<=n,0<=K<=m be
integers with J+K odd. Let real alpha,beta satisfy

    |alpha|+|beta|<=1/2,
    theta=(J*pi+alpha)/n in[0,pi],
    phi=(K*pi+beta)/m in[0,pi].                       (1)

Use the full corrected-kernel S,Q_v,Q_h,Delta=S-lambda of equations
(2)-(3) of D29-floor41.md, including the exceptional highest mode in
the first coordinate and all polynomial collision values. Then

    Q_v>1/20 if0<K<m,
    Q_h>1/20 if0<J<n.                               (2)

Every noncorner odd center therefore has Delta>1/20 and
lambda<S-1/20. Actual corner centers remain excluded. This is a
strict finite analytic inequality on the whole radius-half domain.

## Dependencies and the degree-domain check

The exact identities/normalization are PD-T364, reconstructed in
C01-allclass-defect.md and C02-defect-dense-band.md. The only new
arithmetic obligation is the comparison at512 below. This is a
quantitative onset corollary of C02, not a new principle.

Use C02's three exhaustive cases for an applicable interior projection:
the four closest center-index distances, remaining gamma<pi/6, and
gamma>=pi/6. Here M,L denote its adjacent physical/periodic meshes,
chi its center angle, and gamma=min(chi,pi-chi).

For the first case C02(16), under its original n>=64 hypothesis, gives
Q>1/20. For the second case its original C02(18) also gives Q>1/20
for n>=64. These old estimates are valid for n>=512. In particular
this proof does not use the stronger C02(27) near-center numerator
whose explicit t<1/45 hypothesis is established only from n4096.

For gamma>=pi/6, C02's already derived capped reciprocal band

    a0=pi/100, b0=pi/4, c=2, T=4*log2

has the finite lower bound C02(29)

    H_n=(11/4)*(6/25)/(22/7)^2
        -(14/5)*(11/16)/[(157/50)*n]
        -8*(8/5)/[(157/50)*n]
        -8*(11/16)/[n^2*(3/100)].                    (3)

The middle-band derivation requires gamma>=pi/6, the phase radius
<=1/2, positive band functions, and M,L>=n. The elementary constants
in C02(28) are independent of n. No step of that derivation invokes
n4096; that onset was used only for the final 1/16 comparison and the
other two cases. Thus Q>=H_n applies here for every n>=512. This
domain check, rather than extrapolation of C02's 1/16 theorem, is the
reason (3) may be used at512.

## Written exact comparison at512

Every loss in (3) decreases with n; H_n is increasing for positive n.
At512 its four terms are

    H_512=1617/24200
          -385/(628*512)
          -640/(157*512)
          -550/(3*512^2).                            (4)

The following rational bounds require only the indicated integer
products:

    1617/24200>33/500,       808500>798600;
    385/(628*512)<1/800,     308000<321536;
    640/(157*512)<1/125,     80000<80384;
    550/(3*512^2)<7/10000,   5500000<5505024.         (5)

Consequently

    H_512>33/500-1/800-1/125-7/10000
          =1121/20000>1/20.                          (6)

This proves the middle case for all n>=512. The old C02 nearest and
small-angle cases complete(2). The exact full Delta identity then
gives the noncorner statement. No numerical endpoint evaluation or
threshold search has been performed.

## Interface, limitations and history

A whole phase box may use1/20 only under exact integer n>=512 and
maxabs(alpha interval)+maxabs(beta interval)<=1/2, and only for
admissible noncorner classes. Actual corner predicates stay separate.
The old C02 n4096 floor1/16 remains stronger on its original domain.

This new floor alone establishes no primitive-S upper comparison,
complete cover, global finite degree, or generic certifier. No
preexisting theory file, checker, source or receipt was changed.
Independent mathematical review is pending.

2026-11-06. Rules/input `09cc533678a22b38f40b70be95426ebbe81faa93`.
Assigned Codex auxiliary mathematics developer, requested Sol xhigh;
serving model metadata unexposed. Prospective scope, gate and
alternatives are in ../ideas/D29-defect-floors.md; exact history and
dependency hashes are in ../attempts/D29-defect-floors.md. This proof
uses only written rational arithmetic, with no scientific job.


## Root review closure — 2026-11-06

Distinct [D29 review](../independent-checks-D29-defect-floors.md), SHA256 `84fbde47c836c9d6689896b1610de3ef7d0628bf9722cf8ec7cafda16309b648`, accepts all three frozen scopes without unresolved findings. Root adopts the uniform1/512 floor from41, uniform1/20 from512, and guarded radius floor from41 at their exact physical/signed domains. No numerical job or generic finite instance is asserted. Reviewed prefix is preserved; final Claude audit remains separate.
