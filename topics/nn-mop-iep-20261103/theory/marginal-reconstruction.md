# PD-T?nn-mop-iep-codex-04 — marginal Jacobi data reconstruct the normal finite NN triangle

ID kind: PD-T.
Aliases: finite CC algorithm; finite FHV layer recursion; terminal boundary equality.
Split from: the terminal equality of PD-N?nn-mop-iep-codex-01,
[historical record](terminal-division-obstruction.md), together with the
corrected positive interpretation of C4. Interior nonvanishing is a
separate substantive dependency, PD-T?nn-mop-iep-codex-03.
Split into: none.

## Statement

Let two positive discrete measures have the same N>=1 distinct real
support points, and assume every multi-index of total degree at most N
is normal in the convention of PD-T?nn-mop-iep-codex-01. In exact
arithmetic, the marginal monic Jacobi coefficients through index N-1
uniquely determine and reconstruct all four NN coefficients

    a_(nu,1), a_(nu,2), b_(nu,1), b_(nu,2),   |nu|<=N-1,

by the layer recursion below. Every divisor is d_eta=b_(eta,2)-b_(eta,1)
with |eta|<=N-2 and is nonzero. No division at degree N-1 is required.

At the final coefficient layer, every such input necessarily satisfies

    P_(nu+e_1)=P_(nu+e_2)=F=product_l(x-x_l),
    b_(nu,1)=b_(nu,2),   |nu|=N-1.

This equality is a necessary final boundary condition on the reconstructed
array, not an obstruction to reconstructing its stated domain.

## Definitions and assumptions

Let L_j(f)=sum_l w_(j,l)f(x_l), with w_(j,l)>0, and let P_nu be the
monic type-II polynomial from the invertible mixed moment system.
The NN convention is

    x P_nu = P_(nu+e_j) + b_(nu,j)P_nu
             + a_(nu,1)P_(nu-e_1) + a_(nu,2)P_(nu-e_2), j=1,2.

An absent predecessor has coefficient zero. Write

    d_nu=b_(nu,2)-b_(nu,1),   S_nu=a_(nu,1)+a_(nu,2).

The supplied marginal coefficients alpha_(j,k), beta_(j,k) use

    x p_(j,k)=p_(j,k+1)+beta_(j,k)p_(j,k)+alpha_(j,k)p_(j,k-1),
    p_(j,0)=1, p_(j,-1)=0, alpha_(j,0)=0, 0<=k<=N-1.

If symmetric Jacobi matrices are supplied, alpha is the square of the
off-diagonal entry. Individual mass normalizations are immaterial.
The input is assumed to come from the stated normal finite measures;
this theorem does not characterize arbitrary proposed arrays.

## Status by part

Overall status: PROVED. Independent Claude re-audit PENDING.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Reconstruction through degree N-1, using only interior divisors | PROVED | Algebra and induction below; substantive nonvanishing dependency split into PD-T?nn-mop-iep-codex-03 |
| Necessary final boundary equality | PROVED | Vanishing polynomial and normality argument below |

Candidate / claim disposition: none. This is the finite-domain application
of established compatibility algebra, without a novelty claim, a new
candidate or a new stable updater.

## Depends on

- PD-T?nn-mop-iep-codex-01: existence, uniqueness and NN identities through
  degree N-1; accepted in audit-01 and unchanged by this response.
- [PD-T?nn-mop-iep-codex-03](interior-divisor-nonvanishing.md):
  d_eta != 0 whenever |eta|<=N-2.
- Elementary polynomial algebra and linear algebra.

No external theorem or finite checker is used as an unverified proof step.

## Proof

### 1. Compatibility relations, independently reconstructed

Subtracting the two NN identities gives

    P_(nu+e_1)-P_(nu+e_2)=d_nu P_nu.                 (D)

Fix |nu|=s<=N-2. Every recurrence used next is based at degree at most
N-1, and its opposite successor P_(nu+e_1+e_2) has degree at most N.
Compute x times the left side of (D), using direction 2 at nu+e_1
and direction 1 at nu+e_2. The two opposite successors cancel.
For nu_2>0 use (D) at nu-e_2 to substitute

    P_(nu+e_1-e_2)=P_nu+d_(nu-e_2)P_(nu-e_2).

For nu_1>0 use (D) at nu-e_1 to substitute

    P_(nu-e_1+e_2)=P_nu-d_(nu-e_1)P_(nu-e_1).

If a coordinate is zero, the corresponding absent-polynomial term has
coefficient zero and is simply omitted. Finally replace
P_(nu+e_2) by P_(nu+e_1)-d_nu P_nu. The resulting expression is

    x(P_(nu+e_1)-P_(nu+e_2))
      = [b_(nu+e_1,2)-b_(nu+e_2,1)] P_(nu+e_1)
        + [d_nu b_(nu+e_2,1)+S_(nu+e_1)-S_(nu+e_2)] P_nu
        + a_(nu+e_2,1)d_(nu-e_1) P_(nu-e_1)
        + a_(nu+e_1,2)d_(nu-e_2) P_(nu-e_2).      (E)

The right side of x times (D), expanded in direction 1 at nu, is

    d_nu x P_nu
      = d_nu P_(nu+e_1)+d_nu b_(nu,1)P_nu
        + d_nu a_(nu,1)P_(nu-e_1)
        + d_nu a_(nu,2)P_(nu-e_2).               (F)

Coefficient comparison is valid. The first two polynomials have distinct
degrees s+1 and s, above every predecessor. When n,m>0, the two
predecessors are independent: otherwise their monic polynomials would
coincide in a degree s-1 polynomial satisfying the union of their
conditions, namely all conditions at nu, contradicting normality of
M_nu. On an axis there is one predecessor of degree s-1; at nu=0
there are none. Thus the displayed family, with absent terms removed,
is independent in every case.

Equating (E) and (F) proves

    a_(nu+e_1,2)d_(nu-e_2)=d_nu a_(nu,2),   nu_2>0,
    a_(nu+e_2,1)d_(nu-e_1)=d_nu a_(nu,1),   nu_1>0.  (A)

    b_(nu+e_1,2)-b_(nu+e_2,1)=d_nu.                 (B1)

    d_nu b_(nu+e_2,1)
      = d_nu b_(nu,1)-[S_(nu+e_1)-S_(nu+e_2)].     (B2)

These are the auditor's (A)/(B1)/(B2), obtained here from the NN identities
and a justified independent polynomial family, rather than assumed from
the audit or inferred from a finite run.

### 2. Axis data and layer induction

The marginal data give, for 0<=k<=N-1,

    a_((k,0),1)=alpha_(1,k),   a_((k,0),2)=0,
    b_((k,0),1)=beta_(1,k),
    a_((0,k),1)=0,            a_((0,k),2)=alpha_(2,k),
    b_((0,k),2)=beta_(2,k).

At degree zero this initializes every coefficient, including both b's.
If N=1, the target domain consists only of this site, so reconstruction
is complete without any division.

For N>=2, suppose all layers through s are reconstructed, where
0<=s<=N-2. To produce layer s+1, first fill its axis a's as above.
For any mixed eta=(n,m) on that layer, (A) gives

    a_(eta,1)=a_(eta-e_2,1) d_(eta-e_2)/d_(eta-e_1-e_2),
    a_(eta,2)=a_(eta-e_1,2) d_(eta-e_1)/d_(eta-e_1-e_2).

Their denominators have degree s-1; mixed eta occur only if s>=1.
Their other coefficients are on layer s. Thus every a on layer s+1
is known before any of that layer's unknown b's is computed.

For each nu on layer s, compute

    q=b_(nu,1)-[S_(nu+e_1)-S_(nu+e_2)]/d_nu,
    b_(nu+e_2,1)=q,   b_(nu+e_1,2)=q+d_nu.

These are (B2) and (B1); their denominators have degree s. They cover
exactly the b_(eta,1) with eta_2>0 and b_(eta,2) with eta_1>0.
The remaining axis b's come from the marginal data. Every new coefficient
is therefore computed, with no unknown coefficient on the right.

All divisors are nonzero by PD-T?nn-mop-iep-codex-03. Since the genuine
coefficients satisfy these identities and the marginal initial data,
induction proves that the reconstruction equals them. The same induction
proves their determination by the marginal data. It does not assume a
converse theorem for arbitrary boundary arrays.

| Target coefficient layer t | Needed divisors | Largest degree over t<=N-1 |
|---|---|---|
| Mixed a's, t>=2 | d at degree t-2 | N-3, when N>=3 |
| Unknown b's, t>=1 | d at degree t-1 | N-2, when N>=2 |
| Axis data and layer zero | none | none |

In particular d at degree N-1 is never divided by, nor used as a numerator,
in constructing the required triangle. This is exactly the layer
organization in FHV, rather than a boundary modification of it.

### 3. Final boundary condition

The monic degree-N polynomial F vanishes at all support points, hence
L_j(x^i F)=0 for all i>=0 and both j. At every normal eta of degree N,
uniqueness therefore gives P_eta=F. At |nu|=N-1 both successors equal
F; (D) then gives d_nu P_nu=0. Since P_nu is monic and nonzero,
d_nu=0, proving the final equality. This proof includes N=1.

The defined NN array stops at degree N-1. A degree-N NN site would need
degree-(N+1) successors. No such index is normal here: its moment matrix
factors through evaluations on N points and has rank at most N. Assigning
formal, nonunique extensions beyond the domain is not part of this
reconstruction theorem. A rule dividing by terminal d to propagate there
does not identify a failure of C4 on its actual domain.

## Checks

The proof is analytic exact algebra, not a computer proof. Audit-01's
independent layer checker reported finite MEASURED corroboration; that
checker was not rerun by this mathematical worker. This response rechecked
the primary equations and full induction at the locators below.
No numerical stability experiment is claimed in this record.

## Sources and comparison

LITERATURE: FHV 2015, arXiv:1406.0364v2, §3.1 Theorem 3.1 and
(3.3)–(3.10), printed pp. 16–18; §3.3 (3.11)–(3.15), Theorem 3.3
and its proof, printed pp. 20–21. Their lower-coefficient step uses
layer-(t-2) divisors; the diagonal step uses layer-(t-1) divisors to
produce layer t. Van Assche 2011, arXiv:1104.3778v1, Theorem 3.1,
(3.1)–(3.5), printed pp. 9–10, supplies the r=2 compatibility pattern.
See [source-recheck-01.md](../source-recheck-01.md) for reading coverage.

Kozhan–Vaktnäs, arXiv:2407.13946v2, Definition 2.8 (printed p. 8)
requires normality on 0<=nu_j<=N_j, where N_j is the marginal
finite-functional size (§2.2, p. 5). Theorem 3.6 and Remarks 3.7–3.8
(pp. 16–17) give the finite-perfect-system CC algorithm, using only
differences whose opposite corners are in that rectangle.

For our common N-point measures, N_1=N_2=N. At (N,N) the mixed
moment matrix has 2N columns but rank at most N by evaluation factorization,
so it is singular. Thus common-support triangular normality does not
satisfy that theorem's perfect-rectangle hypothesis. Nevertheless the
source confirms that finite NN reconstruction already exists in its
stated domain. The present proof applies the same local compatibility
organization to a different, explicitly assumed normal domain; it makes
no absence, priority or novelty claim. The interior lemma is also covered
in stronger local form by that source's Lemma 2.18(b), p. 11.

## Scope and open items

Nonzero divisors need not be well separated from zero. This exact
reconstruction result supplies no rounding-error bound, stable updater,
optimal complexity claim, or converse positive-measure characterization.
The terminal equality is necessary, not a sufficient inverse criterion.
It neither determines arbitrary marginal masses nor covers partially
normal inputs. Stability and coupled updating remain outside this record.
Independent Claude re-audit and final-ID/registry preparation are pending.

## History

2026-11-05: Codex bounded mathematical developer; rules/head
`9ec2a54c5b6af56514feaf11c9fc329f19a88820`. Requested allocation:
gpt-6.1-sol xhigh; exact backend model/effort metadata is not exposed.

The former record's terminal wording was
"P_(nu+e_1)=P_(nu+e_2)=F, b_(nu,1)=b_(nu,2)" at degree N-1.
That equality is retained here as a positive boundary fact. The former
description of C4 as a failed all-layer propagation mechanism is withdrawn
by response-01: its actual layer recursion never uses the terminal divisor.
The historical file preserves the complete original statement and scope.
The independent substantive interior assertion is split into
PD-T?nn-mop-iep-codex-03; it is a supporting dependency of this PROVED
reconstruction result, not an unresolved conjunct or a reason for PARTIAL.
