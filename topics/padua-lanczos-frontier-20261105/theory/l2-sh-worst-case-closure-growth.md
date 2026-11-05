# PD-T?lanczos-frontier-codex-L2-04 — the saved worst-case X-closure target holds on every SH_n

ID kind: PD-T.
Aliases: SH_n smooth-rule adverse-source closure; final-degree X-closure chain.
Split from: saved W target in attempts/L2.md; original literal PD-T055 remains OPEN.
Split into: the full independent-sign expectation is a separate L2-05 record.

## Statement

For the exact saved SH_n family and R_smooth rule class below, for every
integer n>=2,

    C_n >= sqrt((4^n-1)/6)/cos(pi/(n+3)) >= 2^(n-4).        (1)

Thus the unchanged saved W target is true. C_n is the infimum over the
saved smooth exact-base BJ prior-subtraction rules of the unit-source
worst-case first-order maximum X-closure defect, divided by ||X||.
It is not span capacity. More precisely, for an arbitrary represented
vector f injected only at h=(n,0), the stage n-1 frame derivative has
zero columns below degree n-1 and degree-(n-1) columns

    D_X,n-1(:,(n-1-j,j))=-(-2)^j R_n f,  0<=j<n.          (2)

This same map holds for every member of the saved class. It will also
supply the separately proved expectation bound.

## Definitions and assumptions

Exactly the frozen family: m=n+2, theta_k=k*pi/(m+1), s_k=cos(theta_k),
v_k=2sin²(theta_k)/(m+1), physical nodes `(s_k,2s_k+s_l)`, weights
w_kl=v_k v_l, and M=(n+2)². Let X=S=diag(s_k), Y=2S+T and
N_d=(d+1)(d+2)/2. Weighted represented vectors are sqrt(w) times
polynomial values. Columns (r,j) are ordered by r+j then j.

The exact positive-leading orthonormal columns are
`q_rj=sqrt(w) U_r(s)U_j(t)`, with U_-1=0. BJ uses X from(r-1,0)
when j=0 and Y from(r,j-1) otherwise. The starting vector is exact.
Class R_smooth and source norm are precisely the saved ones, interpreted
on represented Euclidean vectors through L2-03:

    beta_hat_h q_hat_h=A_h q_hat_parent+epsilon f_h
                         -sum_(l<h)c_hat_hl q_hat_l,
    sum_h ||f_h||²/sigma_h²=1,
    sigma_h=||A_h q_parent(0)||.

The exact base basis is common to every rule. Coefficients and
normalizations are differentiable for each fixed source; no parent
revision, extra product or reference injection. Weights/nodes are fixed.
Let P_hat_s project onto the stored completed-degree span, P_s onto the
exact weighted polynomial space, R_s=I-P_s, and
`delta_X(s)=||(I-P_hat_(s+1))X P_hat_s||_2`.

C_n has exactly the saved inf-rule/sup-source/pointwise epsilon->0+
definition, with maximum over s=0,...,n-1. No finite-epsilon uniformity
or actual working-precision storage is assumed.

## Status by part

Overall status: PROVED, analytic complete proof below; distinct
supplementary mathematical check accepted; required Claude audit pending.

| Part | Status | Evidence |
|---|---|---|
| Exact final-degree-source closure map (2), all saved rules | PROVED | Weighted quotient invariance and both-projector calculation |
| Bound (1) and original W target for every n>=2 | PROVED | One explicit unit-budget normal source and exact geometric sum |

## Depends on

- Checked L1a, `l1-01-sheared-U-aggregate-separation.md`, for the SH_n
  positive normalized weights, injectivity through n+1, exact tensor basis
  and creator identities. Its immutable reviewed proof hash is
  `9f59217da265a433470bb6030074acf76e63e4ffb0a6590add800666a64de90d`;
  its separate acceptance is recorded in `independent-checks-sh.md`.
- L2-01 and its separate positive-weight extension L2-03, for arbitrary
  saved-rule projector derivatives and the actual closure map.

No span lower or converse of PD-T053 is used. The completed G2 finite
predicates were a protocol prerequisite, not a premise extrapolated to
this different family.

## Checks and sources

Analytic development only: no new numerical/symbolic experiment was run
by this worker. A distinct reviewer reconstructed and accepted the full
initial draft SHA256
`30cc4c6bab3c7dfd9dc617379f63e1a62f76bf4c0a098dbb0f5940beee9a3b74`,
including the source factors, actual two-projector closure, rule quantifiers
and degree range, with no mathematical finding. The separate review is
in independent-checks-l1-l2.md and does not replace the Claude audit.
Closest records and the
prospective unchanged W statement are in ideas-l2-continuation.md and
attempts/L2.md. No new original paper or historical-priority claim.

## Proof

The checked SH_n identities give

    X q_rj=(q_(r+1,j)+q_(r-1,j))/2,
    Y q_rj=q_(r+1,j)+q_(r-1,j)
                  +(q_(r,j+1)+q_(r,j-1))/2.                (3)

All creator pivots are1/2. For h=(n,0), its parent is(n-1,0), so
`sigma_h²=1/2` for n>=2. Also
`||X||=cos(pi/(n+3))`, strictly between0 and1.

**Frozen response of the selected source.** Write V^q for the frozen
normalized response, not the monic response: its equation is
`beta_k V^q_k=A_k V^q_parent-sum_l c_kl V^q_l+f_k`.
The weighted bridge gives `Z_s=R_s[V^q_k]_(deg k<=s)` for every rule.
When only h=(n,0) has source f, every earlier frozen response vanishes.
At that first column V^q_(n,0)=2f. For degree-n column(n-j,j), j>0,
the sole other degree-n column in its creator relation (3) is
(n-j+1,j-1), with coefficient1; all parent/lower-degree responses are
zero. Hence

    V^q_(n-j,j)=-2 V^q_(n-j+1,j-1)=2(-2)^j f,
                          j=0,...,n.                     (4)

Thus Z_(n-1)=0, and Z_n has only its degree-n columns nonzero, namely
`2(-2)^j R_n f`. Under an arbitrary smooth rule, earlier tangential
stored-column derivatives need not vanish; only the frozen responses
and the completed-prefix normal projector derivatives are asserted zero.

**Actual closure, not span growth.** The proved two-projector formula is

    D_X,n-1=R_n X Z_(n-1)-Z_n H_X,n-1,
    H_X,n-1=Q_n^T X Q_(n-1).                              (5)

The first term is zero here by Z_(n-1)=0. For input column
(n-1-j,j), (3) has degree-n coefficient1/2 at(n-j,j); its other
term has lower degree and multiplies a zero Z_n column. Equations
(4)–(5) therefore give (2). For input degrees at most n-2, X maps
into degree at most n-1, where Z_n is zero, proving the remaining
column assertion. The derivative of the full closure operator is
`D_X,n-1 Q_(n-1)^T` and has the same spectral norm.

Every nonzero column in (2) is a multiple of R_n f, so

    ||D_X,n-1||_2²=||D_X,n-1||_F²
       =||R_n f||² sum_(j=0)^(n-1)4^j
       =((4^n-1)/3)||R_n f||².                            (6)

Choose e=q_(n+1,0). The checked weighted orthogonality through n+1
gives ||e||=1 and R_n e=e. With f=e/sqrt(2), the full relative
source budget is exactly1 because sigma_h²=1/2 and all other sources
are zero. Formula (6) becomes `(4^n-1)/6`.

The same chosen source works at first order for every saved rule by the
weighted invariance theorem. The saved maximum over stages is at least
its stage n-1 term; taking the worst case and then the infimum therefore
proves the first inequality in (1). This uses pointwise derivative
limits only and no rule-independent nonlinear radius.

Finally ||X||<1 and `256(4^n-1)>=6*4^n` for n>=2, since this is
equivalent to `250*4^n>=256`. Taking square roots proves
`C_n>=2^(n-4)` with the original constant and degree range.

## Scope and open items

This proves the saved worst-case formal smooth-rule reading on the
explicit n-dependent weighted family. It does not settle the original
PD-T055 unrestricted working-precision assertion, every-error positive
drift, deterministic IEEE activation, scalar-operation realizability,
implicit-section accuracy, or uniform finite-u behavior. Different data
families or nonsmooth/exact-base-violating rules are outside the claim.
The R expectation is a separate theorem under its unchanged full law.
Supplementary independent mathematical reconstruction is accepted.
Required Claude protocol/scientific audit remains pending, including the
earlier campaign timing deviation.

## History

- 2026-11-05: Codex, configured gpt-6.1-sol xhigh. The original W target
  and final-degree actual-closure test were restated prospectively after
  actual independent G2 passes and the separate weighted bridge. This
  complete written proof establishes the developer's analytic PROVED
  status; separate mathematical review is requested. No experiment or
  span-to-closure inference is claimed.
- 2026-11-05: After distinct mathematical reconstruction accepted the
  complete initial draft, added verification metadata and clarified
  wording about the separate L1 review. Statement and proof are unchanged;
  required Claude audit and earlier protocol qualification remain pending.
