# Supplementary independent check — D06 actual four-copy rows

Rules/read input: `084a64f6465956f9c75b5538f83752c30318f151`.
Observed review HEADs: `f9b64a6351b58c40f3432b80dd4b24f88ab1c477`
and `2e4ac49fa0687a7736bc1df82c12e6483b1c7a94`.
The rules and state/IDEAS.md are unchanged from the recorded rules input.
Reviewer: distinct Codex subagent `/root/d01_far_review`, parent-requested
Astra xhigh; actual serving metadata unexposed. Formal Claude audit
remains separate.

## Verdict and frozen scope

**ACCEPTED as written; no unresolved mathematical finding.** For each
fixed physical point and integer n>=2, the actual cardinal norm has the
stated cubic-over-quartic parity-grid representation, with at most eight
open sign blocks per ordinary row, eight labelled cotangent channels per
block, at most six direct terms on each such row, and at most two wholly
retained rows. The absolute value is applied after combining all four
corrected copies. These are exact representation counts.

The theorem supplies neither an implementation nor a runtime or bit-cost
bound. Root/sign/equality decisions, outward arithmetic, newly weighted
partial-sum errors, finite-polynomial evaluation costs, whole-box motion
and usefulness as a certifier remain OPEN. No existing common-S radius,
benchmark or successful certificate transfers to this actual-function
formula merely because its partial sums have the same analytic form.

The three assigned records were read completely and their hashes matched:

| Record | SHA-256 |
| --- | --- |
| [D06-four-copy-rows.md](theory/D06-four-copy-rows.md) | `8eb7d781e91c52aaca80f160a24f5198a758b7c99fc397bbba3fd6178e7ca824` |
| [D06 idea](ideas/D06-four-copy-rows.md) | `758754921f45cb4a4e69e0a65397590a2f1e87f49e35a117761f6b6e00c8a943` |
| [D06 attempt](attempts/D06-four-copy-rows.md) | `2fb76e6ada9db7d0b9fd6494129e257db36b0a2ef68955a827cd9ccc6db638aa` |

The author records input `7db857380ab99e19998e01e4ce9832496b222a31`.
Its canonical source-read timing qualification is preserved in the
[attempt, Scope and fresh comparison](attempts/D06-four-copy-rows.md#scope-and-fresh-comparison).
This review does not retroactively upgrade that chronology.

## Independent reconstruction

**Original weights and board parity.** PD-T101's discrete Gram derivation
gives the original even-board weight w_pq=2e_p f_q/N and corrected
cardinal w_pq times the kernel with its highest x mode subtracted.
The cosine product formula therefore gives w_pq/4 times four G copies.
Under j=n-p and r=m-q, j+r is odd because n+m=2n+1; endpoint factors
are preserved. Separate evenness and 2pi periodicity convert the four
arguments to xi+/-t_j and zeta+/-b_r, including their multiplicities.
Thus L_pq=e_j f_r V_r/(2N), proving precisely the coefficient in (3).
The independent C02 normalization sum_four F=(-1)^j V_r/2 agrees.
Coincident endpoint copies do not remove either their multiplicity or
the mesh endpoint half weights.

**Corrected quotient and parity alias.** On a physical row,
(-1)^j=epsilon=(-1)^(r+1). With A=cos(n xi), E=sin(n xi),
cos(m xi)=A a-E b and sin(m xi)=E a+A b imply

    P_n(cos w)=epsilon[A(1+cos w)-E sin w],
    w=xi+sigma*t_j.

Subtracting epsilon A from the divided difference gives exactly
[k_tau-epsilon E sin w]/[cos w-y_tau], with
k_tau=epsilon A(1+y_tau)-P_n(y_tau). No remaining degree-growing
oscillation in j is hidden in this quotient. Its coefficients still
require the original degree-dependent values; no cost bound has been
proved for their construction. The identity is restricted to grid
values, as the theorem explicitly states.

**The two degree bounds.** Substituting z=tan(t/2) gives the displayed
quadratics h_(sigma,tau), d_(sigma,tau). A denominator could vanish
identically only if a=y_tau, b=0 and -a=y_tau, contradicting
a^2+b^2=1. Their product is therefore a nonzero polynomial; multiplying
out gives numerator and denominator degrees at most eight.

For the sharper version, put c=cos t, s=sin t. The two sigma
denominators are ac-y_tau-sigma*b*s. Their product is

    d_tau(c)=c^2-2a*y_tau*c+y_tau^2-b^2.

The paired numerator independently expands to

    2(k_tau-epsilon*E*b*c)(a*c-y_tau)
       -2epsilon*E*a*b*s^2
    =2[(a*k_tau+epsilon*E*b*y_tau)c
       -(k_tau*y_tau+epsilon*E*b*a)].

This is the asserted affine ell_tau, including the constant term and
both signs. Adding the two tau quotients gives U=ell_+ d_-+ell_- d_+
of degree at most three over W=d_+d_-, monic of degree four. Factoring
d_tau gives the two explicit cosines in the statement. The calculation
uses only trigonometric identities and covers a=0, b=0, E=0, repeated
tau values and all coefficient cancellations.

**Sign blocks and direct terms.** Cosine is strictly monotone on
(0,pi). Four denominator event locations and at most three distinct
numerator roots therefore make at most seven distinct interior cuts,
hence at most eight open intervals. Repeated roots and coincident cuts
reduce this number. A canceled denominator remains a direct-event
candidate because the alias equality was only established away from
the original denominators. If U is identically zero, every regular
grid value is zero; this is not an infinite root list. A regular grid
point at a numerator root contributes zero and needs no direct
four-copy evaluation. Grid indices strictly within each remaining
interval are a contiguous parity block.

At an original denominator event, the actual value is supplied by
G=P_n'(y)-T_n(y), including y=+/-1. There are at most four such
interior t values and two physical endpoints, so at most six direct
four-copy terms per nonretained row. Endpoints allowed by the parity
are included with e_j=1/2. Neither a pole multiplicity nor several
colliding copies at one index creates another physical term.

The exact adverse example in the proof checks independently. At
xi=zeta=0, r=m, epsilon=(-1)^n, both y_tau=-1 and k_tau=E=0. The
alias is zero off its denominator event, but t=pi is admitted and

    P_n'(-1)=(-1)^n(m^2-n^2),
    G_n(pi,pi)=2n*(-1)^n,
    V_m(pi)=8n*(-1)^n.

This proves the stated failure of alias continuation at that event.
The example is used only to enforce direct finite evaluation, not to
refute the pointwise theorem or any broader approximation route.

**Eight channels and the exact mesh.** The two elementary identities
for 1/(cos w-cos eta) and sin w/(cos w-cos eta) give coefficients

    epsilon*E/2-k_tau/(2sin eta_tau),
    epsilon*E/2+k_tau/(2sin eta_tau)

on the two half-angle cotangents of each copy. There are eight labelled
channels, allowing duplicates. A channel pole implies an original
denominator event; it cannot occur inside one of the open sign blocks.
Its pi wrap is consequently fixed there. On t_j=(delta+2k)pi/n the
channel increment is sigma*pi/n. Reversing the finite index block when
sigma=-1 changes its ordering, not its coefficient or sign. After a
fixed wrap every sample lies strictly between zero and pi. The general
C02/N5 partial-cotangent theorem covers that complete interval, even
when a block crosses pi/2: there is no extra midpoint subdivision
needed to justify the eight-channel object count.

Multiplying the complete signed channel sum by the constant sign of
U/W gives the sum of the actual absolute values on that block. This
does not invoke the old signed total of N2, take absolute values of
individual reflected copies, or replace the eight coefficient weights
by an old common-S coefficient budget. Every future enclosure must
propagate each newly weighted partial ball and all arithmetic errors.

**Degenerate rows and closed physical endpoints.** On zeta,b_r in
[0,pi], sin(zeta+/-b_r)=0 implies b_r=zeta or b_r=pi-zeta. The
possibilities with sum zero or 2pi and difference +/-pi are exactly
the endpoint cases already covered by this union. There can therefore
be at most two admitted row labels; coincident labels merge. Direct
retention of these complete rows also handles y=+/-1, where an ordinary
cotangent-only backend need not apply. In particular the y=1 expression
contains (1-epsilon A)csc^2(w/2)+epsilon E cot(w/2), so omitting the
retention rule would lose a genuine term.

There are n+2 physical rows and no more than n+1 samples in any row.
The conservative totals 64(n+2) cotangent-block objects and
2(n+1)+6(n+2) direct four-copy evaluations follow, including n=2.
Direct endpoint evaluation avoids tan(pi/2); the sharper partition is
in cosine and has no tangent-infinity exception. All closed physical
edges and corners are covered without an interior-angle assumption.

## Source, novelty and obstruction coverage

The entire 1112-line registry was already read during this review
assignment's D01 work. Its SHA-256 remains
`68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`;
this reuse is explicit, not another claimed full fresh reading. Fresh
D06 searches covered four copies/reflections, parity grids, rational
aliases, cubic rows, affine signs, two traces and root isolation in
the registry, topic records and literature INDEX. Search results were
scoped; no assertion of reading every matched file or of an exhaustive
external literature search is made.

The relevant mathematical source bodies were read in full: original
[PD-T101](../padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md),
[PD-T185](../padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-70-all-edge-kernel-formula.md),
[PD-T228](../padua-argmax-alln-20261101/theory/gated-codex-14-reflection-first-corner-bound.md),
[C02 corner](theory/C02-corner-halfdiamond.md),
[C02 partial sums](theory/C02-row-cotangent.md),
[N2 rows](theory/N2-row-decomposition.md),
[N5 partial sums](theory/N5-partial-cotangent.md),
[N5 two-phase defect](theory/N5-two-phase-defect.md),
[N6 obstruction](theory/N6-two-trace-obstruction.md), and
[PD-N085](../padua-argmax-effective-20261103/theory/argmax-effective-codex-06-affine-sign-obstruction.md).
The complete [C11 attempt](attempts/C11-row-order.md), the C02 corner,
C09/C12/C14/C15 and N5/N6 candidate records, IDEA331's full final atomic
entry and its original gated candidate body were also read for scope
comparison. C09/C14 mathematical proofs and C12/C15 executables are not
premises of this D06 acceptance; their candidate scopes already separate
their common-S coefficient-vertex uppers from this actual point equality.

The reflection identity, finite corrected kernel and cotangent method
are inherited. The specific refinement checked here is the parity-grid
pairing of the four actual copies to cubic-over-quartic form before
taking the absolute value. PD-N085 refutes a particular affine
per-cardinal sign-preservation shortcut; no such shortcut is assumed.
N6's fixed-parameter two-trace inequality is also unused. N5's projected
defect and C02's local corner comparison are different statements.
These comparisons support the author's technical-variant description,
without a historical-priority claim or a new external theorem premise.

## Execution and disposition

This was an analytic review. Tools read/search files, checked SHA-256
identities, inspected the read-only rules/registry diff and wrote this
report. No symbolic helper, scalar numerical diagnostic, native build,
board evaluation, quadrature, fit, cover or independent numerical rerun
was executed. Accordingly there is no scientific compute receipt or
measured runtime to report; the optional <=20 CPU-second diagnostic
allowance was unused. Historical measurements in predecessor records
were read as historical evidence, not reproduced or used as proof here.

Preliminary and completed findings were sent to the parent before report
completion. No mathematical fix was requested and no author source,
shared registry, prior review, Git branch or Git index was changed by
this reviewer. Only this assigned report was written. Acceptance is
supplementary and limited to the frozen analytic structural theorem;
the formal Claude audit and the separate cheap-certifier objective
remain outside this completed check.
