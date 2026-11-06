# PD-T540 — simple positive ground state and norm identity

2026-11-06 ID history: `PD-T?mz-sharp-codex-P1-02` → `PD-T540`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: two-step positivity; irreducible corner kernel; Perron ground state.
Split from: P1's kernel-identification and spectral-consequence target.
Split into: numerical certificates remain separate.

## Statement and definitions

Use exactly H, B and S_all,S_alt from P1-elliptic-kernel.md and put A=-B.
Then A is a nonzero compact selfadjoint operator with nonnegative integral
kernel. For every f in H with f>=0 almost everywhere and f nonzero,

    A^2 f > 0 almost everywhere on D.                    (1)

Writing r=||B||=||A||, one has

    r>0,   c_minus=inf spectrum(B)=-r.                  (2)

The eigenvalue c_minus is simple and has a real eigenfunction u>0 almost
everywhere. The sign of u may be fixed positive; after unit normalization
it is unique. Moreover -r is not an eigenvalue of A; with the already
proved S3-03 fact c_plus>0, this gives

    0<c_plus<r.                                        (3)

Positivity here means almost everywhere in the weighted triangle. The
kernel of A itself is not strictly positive on all pairs: (1), rather
than that stronger false property, supplies irreducibility.

## Assumptions and status

Overall status: **PROVED**, analytic development accepted with its kernel
dependency in [audit-02](../audit-02.md).

The hypotheses are those of the accepted S3-03 and new
P1-elliptic-kernel.md, with their exact measure and norm conventions.
No numerical eigenvector, decimal approximation or finite-m branch
identification is a premise. Candidate ../ideas/P1-kernel.md is retained;
no priority claim or PD-N is made.

## Depends on

- S3-03: compactness and selfadjointness of B, and c_plus>0 only for (3).
- P1-elliptic-kernel.md: equality with the explicit nonpositive integral
  kernel on H.
- The standard spectral theorem for a compact selfadjoint Hilbert-space
  operator: every nonzero spectral point is a real eigenvalue of finite
  multiplicity, accumulation can occur only at zero, and a nonzero compact
  selfadjoint operator has an eigenvalue of modulus its norm. This is a
  named basic functional-analytic fact, not a claimed new result or a
  source-paper theorem imported through an unread citation. The remaining
  positivity and simplicity arguments are written below.

## Proof

### Two-step positivity in the actual triangle

For interior x=(a,b), y=(a',b'), the displayed elliptic formulas imply

    A(x,y)>0 whenever a+a'>1 or b+b'>1,                 (4)

apart from irrelevant null singular sets. S_all is strictly positive
away from its diagonal, and S_alt is strictly positive precisely on the
open condition that its two arguments sum to more than 1.

Let f>=0 be nonzero. Since a'>0 almost everywhere on D, there exists
delta>0 such that {y: a'>delta, f(y)>0} has positive mu measure. For
almost every z=(s,t) in the positive-measure wedge s>1-delta inside D,
(4) makes Af(z)>0. Boundedness of A ensures the integral is finite almost
everywhere; positivity of the integrand on that subset makes it strict.

Now fix any interior x=(a,b). The wedge

    max(1-delta,1-a)<s<1,      0<t<1-s

has positive mu measure. On it, Af(z)>0 almost everywhere and A(x,z)>0.
Therefore A^2 f(x)>0 wherever the representing integral is finite. Again
boundedness implies finiteness almost everywhere. This proves (1).
Equivalently, any pair of interior points can communicate through a
positive-measure set of intermediate points near (1,0). Neither the
triangle boundary nor its coordinate axes have positive mu measure.

For reference, A is nonzero without any numerical premise: choose
nonnegative smooth bumps in two small interior sets with a+a'>1. Their
mutual A form is positive by (4), so ||A||>0.

### The norm is the positive spectral radius

By compact selfadjointness, there is a real eigenvector v with eigenvalue
lambda and |lambda|=r=||A||>0. Kernel nonnegativity gives

    r||v||^2=|<v,Av>| <= <|v|,A|v|> <= r||v||^2.

Thus |v| attains the top Rayleigh value r. This implies A|v|=r|v|:
rI-A is positive semidefinite and its zero quadratic form forces its
application to vanish, for example by
||(rI-A)w||^2<=2r<w,(rI-A)w>. Put u=|v|. Applying (1) to u and using
A^2u=r^2u shows u>0 almost everywhere. Consequently r is an eigenvalue
of A with a strictly positive eigenfunction, so (2) follows for B=-A.

### Simplicity and exclusion of the opposite norm endpoint

Suppose the eigenspace of A^2 at r^2 had dimension at least two. Since
it contains u>0, it would contain a nonzero real w orthogonal to u.
Then both w_+=max(w,0) and w_-=max(-w,0) are nonzero. By (1),

    <w_+,A^2 w_-> > 0.

Selfadjointness therefore gives

    <|w|,A^2|w|>-<w,A^2w>=4<w_+,A^2w_->>0.

The second term is r^2||w||^2, whereas the first is at most
||A^2||||w||^2=r^2||w||^2, a contradiction. Hence that eigenspace is
one-dimensional. It follows that r is simple for A and that -r cannot
be an eigenvalue: either would give another vector in the r^2 eigenspace.
The minimum eigenvalue -r of B is correspondingly simple.

Finally c_plus>0 is already established in S3-03, so inf spectrum(A)<0.
Compactness makes that negative infimum an eigenvalue. Since -r is
excluded, it is strictly greater than -r; after reversing the sign this
is exactly (3). QED.

## Checks and scope

No code or numerical calculation was executed. This proof establishes
the norm identity, almost-everywhere positivity and simplicity, not a
pointwise boundary value, regularity formula, finite-m eigenvector
identity or certified decimal. Focused independent checks and the later
Claude audit remain to be recorded separately. The new kernel proof was
frozen for distinct reconstruction before this consequence file was written.

## History

2026-11-06, bounded round 2. Codex P1 developer, requested gpt-6.1-sol
xhigh; runtime model/effort metadata unexposed. Rules/input
0205690b9c4e959a28e949083e9a1808735abf4b. The common intermediate wedge
and two-step property were checked explicitly instead of assuming A's
kernel is positive everywhere. Accepted S3 proofs remain unchanged.
