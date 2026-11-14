# PD-T?argmax-bridge-codex-F03-identities — Exact endpoint-complete origin identities

ID kind: PD-T; provisional supporting result, no global allocation.
Aliases: F03 exact origin rows; partial cotangent sum; two-pole subtraction.
Split from: [F03-origin-sign](F03-origin-sign.md), sections 1–3.
Split into: none.

## Statement and scope

For every integer n>=2, set m=n+1 and use PD-T159's corrected Padua corner,
original endpoint half weights and exceptional polynomial contribution 1/m.
The exact origin-row identities (1)–(8) below hold, with the partial positive
rows, both polynomial endpoint rows and the two-pole smooth residual retained.
In particular Lambda_c=1-2n/m+4 sum_r P_r/(nm), P_r=w_r T_(n,r), and
T_(n,r) has the exact harmonic-plus-smooth decomposition (7). The identities
hold for both parities; they do not assert a sign of the compensated corner.

## Status

**PROVED**, analytic supporting identities. This substantive result is split
out because H01/H04/H05/H06 and H-sharp use its exact reduction. Its proof is
the unchanged sections 1–3 reproduced below, whose mathematics was accepted
in [the F02/F03 review](../independent-checks-F02-F03.md) and independently
re-derived in [audit-03 H, section 1](../audit-03/h-corner.md) and
[audit-03 F](../audit-03/f-series.md). Independent review of this split and
its dependency mapping is accepted by the [focused distinct review](../independent-checks-onset512-response.md#f03-source-split-and-h04-majorants--accepted-focused-response).

The all-n sign and useful improved lower target remain **OPEN** in
[F03-origin-sign](F03-origin-sign.md). Neither is an assumption here or in H.
The commentary below on failed substitutions and coarse bounds describes
the limits of these exact identities; it supplies no finite sign estimate,
finite one-index evaluator or impossibility theorem.

## Definitions, assumptions and dependencies

PD-T159 supplies the corrected finite corner identity and endpoint weights;
PD-T226 supplies the signed periodic row and its polynomial endpoint rows.
Their accepted exact formulas, rather than numerical observations, are the
premises. All symbols in (1)–(8) are defined in the proof. PD-T269/270 are
used only for the explicitly attributed asymptotic comparison after (6),
not for the exact finite identities. No external theorem or code is imported.

## Proof (historical sections 1–3 reproduced verbatim)

### 1. Actual origin rows, including both exceptional endpoints

For 1<=r<=n set v_r=r*pi/m. In the periodic first-coordinate grid the
origin samples are

    u_j=j*pi/n, j=1-r mod2, considered modulo2n,
    F_r(u_j)=(1+cos v_r)/(cos u_j-cos v_r).

There is no collision in these folded interior rows: n,m are coprime
and 0<r<m. Since their numerator is strictly positive, their positive
samples have centered representatives |j|<nr/m. Now
r-1<nr/m<r, so the positive set is EXACTLY

    j=-r+1,-r+3,...,r-1.                              (1)

It has r samples, for either parity of n or r. Define their sum P_r.
PD-T226's signed full row is n; hence its absolute row is

    R_r=2P_r-n.                                      (2)

The actual polynomial endpoint rows are R_0=n^2 and R_m=n. Fold the
remaining periodic rows into their two equal copies, without exchanging
the n and m meshes. The exact corner value is therefore

    Lambda_c=1/m+n/m+(2/(nm))sum_(r=1)^n(2P_r-n)
            =1-2n/m+(4/(nm))sum_(r=1)^n P_r.          (3)

The first1/m is displayed separately in the first line: it is the SAME
exceptional polynomial contribution in PD-T159. The n/m is the other
actual endpoint row. Folding the periodic mesh is exactly equivalent
to its original first-coordinate half weights and second-coordinate
endpoint half weights; no endpoint is silently discarded. Formula(3)
also follows by writing the original first-coordinate weighted Cauchy
row as one half of R_r, with its k=0 half row and the exceptional k=m
value kept separately. Thus(3) is an inherited exact normalization,
not a new corner formula assumed from finite comparisons.

### 2. The surviving partial cotangent sum

Put

    t_r=r/m, a_r=(1-t_r)/2, w_r=cot(pi*r/(2m)),
    T_(n,r)=sum_(l=0)^(r-1)cot(pi*(l+a_r)/n).

Then exactly

    P_r=w_r*T_(n,r).                                 (4)

To verify this without a pole assignment, on the positive set(1) use

    F_r(u)=(cot(v_r/2)/2)
                 [cot((v_r-u)/2)+cot((v_r+u)/2)].

The set is symmetric in u, so its two cotangent sums agree. Enumerating
j=r-1-2l gives (v_r-u_j)/2=pi*(l+a_r)/n and proves(4).
Every displayed cotangent is regular. This calculation preserves the
complete positive/negative-row split; it does not turn an absolute row
into a signed row.

The complete n-term cotangent identity, locally proved in PD-T226,
instead gives

    sum_(l=0)^(n-1)cot(pi*(l+a_r)/n)
                   =n*cot(pi*a_r)=n*tan(v_r/2).       (5)

Thus replacing the partial sum in(4) by(5) gives P_r^full=n. This is
exact only for r=n; for every r<n the actual row has negative samples
and P_r>n. Indeed the exact omitted quantity is

    Z_r=P_r-n=sum_(negative samples)(-F_r)>0 (r<n),
    Z_n=0,
    Lambda_c=1+2n/m+(4/(nm))sum_(r=1)^n Z_r.           (6)

These are the origin instances of IDEA329/PD-T226's OLD absolute
partial-row obstruction. They are not a new negative mechanism.
Replacing every partial by its complete signed sum gives only
1+2n/m<3. The omitted mass is Lambda_c-1-2n/m; by the inherited
PD269/270 asymptotics it is asymptotic to (4/pi^2)log^2 n. It is not
a permissible vanishing remainder for either target(T) or its fallback.
This rules out THAT substitution, not another endpoint-complete identity.

### 3. Two-sided digamma subtraction does not by itself collapse the row

For a>0 define H_r(a)=sum_(l=0)^(r-1)1/(l+a). If desired this equals
psi(a+r)-psi(a), with psi defined by its convergent harmonic series;
subtracting the two series telescopes and proves that equality locally.
For 0<x<1 put

    B(x)=cot(pi*x)-1/(pi*x)+1/(pi*(1-x)).

The two singularities cancel: B extends continuously (in fact
analytically) to [0,1], with B(0)=1/pi and B(1)=-1/pi. Exact algebra
in every term of(4) gives

    T_(n,r)=(n/pi)[H_r(a_r)-H_r(n-r+1-a_r)]
                       +sum_(l=0)^(r-1)B((l+a_r)/n). (7)

The two H terms have positive arguments. All endpoint and parity terms
are retained. Subtracting only1/(pi*x) would leave the pole at x=1;
one cannot infer smoothness at BOTH endpoints from that subtraction.
Subtracting both poles really does regularize the summand, as(7) shows.

But the weighted smooth residual

    V_n=sum_(r=1)^n w_r
                       sum_(l=0)^(r-1)B((l+a_r)/n)   (8)

still contains n(n+1)/2 indexed terms. Writing a partial cotangent as
an incomplete product derivative or leaving(8) under a new function
name would not establish the registered genuinely one-dimensional
finite expression or its proposed O(n) evaluation cost.

Even the elementary boundedness of B is insufficient as a final error
allocation: if |B|<=M, using w_r<=2m/(pi*r) gives

    (4/(nm))*sum_r w_r*|sum_l B((l+a_r)/n)|<=8M/pi.

This only supplies a nonvanishing constant charge. It does not provide
the required signed quadrature comparison and normalization compensation
at scale log(n)/n. No assertion that the TRUE residual has constant
size as an approximation error follows from this coarse bound.


## Verification, limitations and next step

This is a prose split of existing proved mathematics, not new research.
No scientific execution, numerical evaluation or native job was performed
for this correction. Existing measured checks remain in the cited auditor
reports; they are corroboration, not premises. The remaining step is distinct
review of the split and downstream source mapping, then registry/crosswalk
application by the orchestrator at PR preparation. No final ID is assigned.

## History — 2026-11-08 correction for F-01 and H-C02

Original source: F03-origin-sign.md sections 1–3 at input commit
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`; those old bytes and audit source
pins remain available in Git. The old file is retained with a dated addendum
identifying this as the canonical PROVED support. The earlier classification
as only routine identities is superseded because H depends on them, under
WORKFLOW's substantive-result split rule. This does not narrow or resolve
the original sign/useful-lower target. No claim of novelty or priority is made.
