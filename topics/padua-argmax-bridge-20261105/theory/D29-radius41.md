# PD-T?argmax-bridge-codex-D29-03 — Radius-dependent defect from degree41

ID kind: PD-T. Aliases: D29 B_n domain extension; n41 clipped radius floor.
Split from: parent-directed radius continuation of the D29 candidate.
Split into: none. The substantive uniform n41 and n512 floors have
their own files and IDs.

Status: **PROVED**, analytic developer corollary; independent review
remains required before checker use.

## Statement

Let n>=41 be an integer, m=n+1. Use precisely the corrected full
kernel, projected defects and physical odd-center domain defined in
D29-floor41.md(1)-(3), but let any real r satisfy

    |alpha|+|beta|<=r<=1/2.

Set

    a=1-r^2/4,
    U=347*a/1000-157*r/500,
    V=17*a/20-r/2,
    W=779*a/750-5*r/6,
    B_n(r)=11711*U/48400-120*V/(157*n)
              -250*W/(157*n)-100*V/(3*n^2),
    F_n(r)=max(1/512,min(1/32,B_n(r))).                (1)

Then Q_v>=F_n(r) whenever0<K<m and Q_h>=F_n(r) whenever0<J<n.
Every noncorner odd center consequently satisfies

    Delta>=F_n(r), lambda<=S-F_n(r).                  (2)

Actual corner classes, n<41, and radii above1/2 are excluded. This
extends the degree domain of C02's middle formula; it does not extend
C02's old min(1/20,B_n(r)) statement below its n64 domain. The new cap
is1/32 because that is supported by the newly proved n41 nearest case.

## Dependencies and middle-band reconstruction

PD-T364 supplies the exact full identities. D29-floor41.md proves the
new n41 nearest, small-angle and uniform floor. The B_n formula and
elementary constants are C02-defect-dense-band.md(19)-(24). Its stated
theorem was n>=64; we check below that its middle-case argument has
no such lower-degree requirement. This is a quantitative/domain
continuation of the same method, not a new mathematical mechanism.

Use the physical/periodic M,L, gamma and fixed-v convention of
D29-floor41.md. The closest four center-index distances have Q>1/32
by its(14). Remaining centers with gamma<pi/6 have Q>1/20 by its(16).
Thus only gamma>=pi/6 needs a new argument for the clipped expression.

Select physical b in[a0,b0]=[pi/20,pi/4]. Set

    C=a-r/2, A(b)=C-a*sin b,
    A0=C-a*sin a0,
    I=C*(b0-a0)+a*(cos b0-cos a0),
    R=C*log[tan(b0/2)/tan(a0/2)]-a*(b0-a0).           (3)

Both actual half numerators are >=A(b), vertically and horizontally:
the physical cosine targets are z0+/-D with
z0=cos gamma*cos b>=0, D=sin gamma*sin b<=sin b. The periodic cosine
is selected inside this same band. Horizontally its fixed second
coordinate is therefore also >=-sin b, so no numerator swap is used.
Since a>=15/16, r<=1/2 and sin(pi/4)<11/15, A(b)>0.
Both A(b) and A(b)/sin b are positive and decreasing on the band.

For periodic cosine x strictly between z0-D,z0+D, the true pair defect
is at least2*A(b)/(D+|x-z0|). Retain the capped function

    f_b(x)=(A(b)/D)*min(c,2/(1+|x-z0|/D)), c=5/4,

and zero outside that open cosine band. Its integral in x is T*A(b),
where T=3/2+4*log(5/4), and its maximum is c*A(b)/D. The translated
parity-grid arc bound loses at most one point on each half-circle.
Layer cake and1/sqrt(1-x^2)>=1 therefore give the exact row estimate

    sum_row d >= (L*T/pi)*A(b)-2*c*A(b)/D.            (4)

For any positive decreasing f on[a0,b0], the physical mesh satisfies

    sum f >=(M/pi)*integral f-f(a0),
    sum f <=(M/pi)*integral f+f(a0).                  (5)

These finite mesh inequalities are independent of the absolute mesh
size. Using interior-row coefficient1/(ML), (4)-(5), sin gamma>=1/2,
and M,L>=n gives

    Q >= T*I/pi^2-T*A0/(pi*n)
                   -5*R/(pi*n)-5*A0/(n^2*sin a0).   (6)

In detail, before replacing M,L by n the three losses are
T*A0/(M*pi), 2*c*R/(L*pi*sin gamma), and
2*c*A0/(ML*sin gamma*sin a0). Thus all degree dependence is explicit.
Equations(3)-(6) have no n64 premise and are valid at n>=41.

## Exact elementary bounds and B_n

The elementary constants already proved in C02(24) are

    157/50<pi<22/7,
    sin(pi/20)>3/20,
    cos(pi/20)<247/250,
    cos(pi/4)>707/1000,
    239/100<T<12/5,
    log[tan(pi/8)/tan(pi/40)]<5/3.                   (7)

They come from Taylor inequalities, squaring and explicit positive
log/exponential series; none has a degree assumption. They imply

    I>U, A0<V, R<W.                                 (8)

For example b0-a0=pi/5, and

    I>(a-r/2)*(157/250)-281*a/1000=U;
    A0<a*(17/20)-r/2=V;
    R<(a-r/2)*(5/3)-157*a/250=W.

The right sides are positive for0<=r<=1/2: they decrease with r,
and their endpoint values are respectively2693/16000,35/64,
1337/2400. Substituting lower bounds into the positive term and upper
bounds into all losses in(6) gives exactly Q>=B_n(r), since

    (239/100)/(22/7)^2=11711/48400,
    (12/5)/(157/50)=120/157,
    5/(157/50)=250/157,
    5/(3/20)=100/3.                                  (9)

All substitutions have the correct sign. This proves the middle-case
bound throughout the newly admitted degree domain.

## Combination and checker interface

The nearest and small-angle cases give Q>1/32, and the middle case
gives Q>=B_n(r). Hence every applicable projection is at least
min(1/32,B_n(r)). Independently D29-floor41.md gives Q>1/512.
Their maximum is exactly F_n(r), proving(1)-(2).

For a whole phase box choose any validated r between
maxabs(alpha interval)+maxabs(beta interval) and1/2. Use exact or
outward arithmetic for(1), exact integer n>=41, and the admissible
noncorner center guard. The old C02 expression capped at1/20 remains
available on its original n>=64 domain, and the independent n512
constant1/20 remains available from D29-floor512.md. This file does
not weaken or silently change those original domains or constants.

No positivity of B_n(r) is required for validity; the uniform1/512
term protects the lower bound. Nor does a positive F_n(r) prove that
the primitive-S upper comparison succeeds on a finite cover. The
complete generic certificate, global argmax extension and all missing
upper comparisons remain outside this theorem.

## Verification and history

2026-11-06, rules/input `09cc533678a22b38f40b70be95426ebbe81faa93`.
Parent-directed continuation registered before proof freeze in
../ideas/D29-defect-floors.md. Assigned Codex auxiliary mathematics
developer, requested Sol xhigh; serving metadata unexposed. This is
written analytic reconstruction with rational identities, no numerical
script, native job or scan. Independent review remains pending.


## Root review closure — 2026-11-06

Distinct [D29 review](../independent-checks-D29-defect-floors.md), SHA256 `84fbde47c836c9d6689896b1610de3ef7d0628bf9722cf8ec7cafda16309b648`, accepts all three frozen scopes without unresolved findings. Root adopts the uniform1/512 floor from41, uniform1/20 from512, and guarded radius floor from41 at their exact physical/signed domains. No numerical job or generic finite instance is asserted. Reviewed prefix is preserved; final Claude audit remains separate.
