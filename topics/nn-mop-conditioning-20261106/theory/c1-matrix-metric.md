# PD-T504 — monic matrix spectral sensitivity bounds

ID kind: PD-T. Aliases: paper Hessenberg metric; box-to-spectral support;
integer-node affine conversion; diagonal witness in a matrix norm.
Split from: none. Split into: none.

## Statement and definitions

Let H(q) be the N by N monic step-line upper Hessenberg matrix, first e1
path, with H_(k,k)=beta_k, H_(k-1,k)=gamma_k,
H_(k-2,k)=delta_k and H_(k+1,k)=1. Indices start at zero and absent
entries are omitted. For a fixed input box define its relative spectral
condition

    K_2= sup_(|h_i|<=s_i) ||DH(q)[h]||_2 / ||H(q)||_2.

Writing L_jk=sum_i |(dH_jk/dq_i)|s_i gives exact bounds

    max_jk L_jk/||H||_2 <= K_2
       <= sqrt(sum_jk L_jk²)/||H||_2.                      (1)

For the exact rational benchmark families, let z_l=2l/(N-1)-1,
d=(N-1)/2, and use integer nodes x_l=d(z_l+1). Denote normalized-node
monic field scales by A_beta,A_gamma,A_delta, and its mixed-input
step-line fieldwise condition by K_z. Let T_x and T_w be the normalized
terminal balanced-beta row's absolute-node and relative-weight supports.
For the integer-node H with absolute integer-node scale one and relative
weights, for every N>=3,

    (T_x+d T_w)/||H||_2 <= K_2
      <= K_z sqrt(N[(d A_beta)²+(d² A_gamma)²
                                      +(d³ A_delta)²])/||H||_2.       (2)

If nodes are instead perturbed with normalized-node scale one, replace
the left numerator by d(T_x+T_w); the same upper remains valid.

For the fixed Krawtchouk p1=2/5,p2=1/2, set M=N-1, d=M/2 and

    R_N=sqrt(N[1+(6d/5)²+d^4+d^6/25]).

For every N>=3, either input-node convention satisfies the all-N bound

    K_2 >= d (4sqrt(6))^M /[20 R_N M(M-1)].                (3)

Thus the monic integer-node matrix spectral condition has exponential
liminf base at least 4sqrt(6). This is a theorem about this specific
matrix normalization, not the infimum over arbitrary matrix similarities.

## Assumptions and status

Overall status: PROVED, exact inequalities and written proof. Finite
evaluations in c1-summary.json are MEASURED, not outward enclosures.
Normality and positive weights as in PD-T432; N>=3 so d>=1. The
monic integer-node H is exactly the representation authenticated by C4's
executed M2 checks against the pinned archive's exact generator. C1 did
not independently read the full paper: that identification is a C4
source/code fidelity result, not an inherited literature stability theorem.

## Depends on

PD-T432's monic step-line map; PD-T437's explicit Krawtchouk coefficients
and parity witness; c1-gauge-invariants.md's balanced-terminal estimate.
No primary-source theorem is used in the proof. C4 owns the archive pin,
input-match check and M2 receipt.

## Proof

For any matrix E, max_jk |E_jk|<=||E||_2<=||E||_F. A maximizing input
sign pattern for any one scalar entry attains its row support, which
proves the left side of (1). Every entry is simultaneously bounded above
by its own support L_jk for every allowed h. Squaring and summing proves
the right side without assuming independent attainability of those
entry bounds.

The affine change and monic rescaling give

    beta_x=d(beta_z+1), gamma_x=d² gamma_z,
    delta_x=d³ delta_z, and subdiagonal=1.                  (4)

The constants d depend only on the fixed N. Integer-node displacement
one corresponds to normalized displacement 1/d<=1. Therefore each field
derivative row is bounded by d^r A_f K_z, where r=1,2,3, respectively.
There are at most N entries in each of the three variable fields. The
upper bound in (2) follows from (1). For the terminal diagonal entry,
integer-node gradients equal the normalized-node gradients, while its
weight gradients are multiplied by d. This yields the lower bound in
(2). With normalized node scale one, both parts are multiplied by d.

For (3), the exact formulas of PD-T437 give |beta_z|<=1/5, and

    0<=gamma_z<= (M+1)²/(4M²)<=1.

Indeed gamma_z=4(M-t+1)(n q1+m q2)/M², q_s<=1/4 and t=n+m,
so maximize t(M+1-t). Each a_s<=gamma_z<=1. In the step-line delta
formula, its degree-(t-2) b difference is at most 1/5, hence
|delta_z|<=1/5. Equation (4) consequently bounds ||H||_2 by its
Frobenius norm R_N. The balanced parity witness changes weights only;
its normalized terminal-beta derivative magnitude is at least
(4sqrt(6))^M/[20M(M-1)] by c1-gauge-invariants.md. Multiplying by d
and dividing by ||H||_2<=R_N proves (3). R_N is polynomial in N,
so taking Nth roots proves the liminf statement.

## Measurements and interpretation

`code/c1_summarize.py` constructs H from high-precision base coefficient
values, computes its spectral norm in NumPy binary64, and uses the
historical full monic K_z table as the upper bound in (2). Matrix lower
and upper fit ranges over N32–64 are numerically evaluated and broad;
the exact induced box-to-spectral norm is not calculated. The normalized
input model and the integer input model are both stated explicitly.

The matrix denominator includes the unit subdiagonal. Neither the
fieldwise ratio K_z nor a single entry row sum equals K_2 in general.
An arbitrary diagonal similarity would change ||H||_2 and is not covered
by (3); b invariance alone cannot cancel that changed denominator.

Forward error comparable with K_2*u is a diagnostic only. In particular,
a large lower bound for K_2*u does not prove weak stability, prove an
algorithm realizes a worst-case direction, or supply a useful
finite-epsilon bound. The paper's weak-stability observation is not
promoted to a local theorem.

## Checks and open items

M2 fidelity is in the C4 receipt, separately from solver forward errors.
The matrix inequalities need no computer premise. Independent checks of
the numerical bound assembly and the signed regression intervals are
recorded in the topic's independent-check file. Exact box-to-spectral
optimization and outward numerical norm enclosures remain open.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`.

## Final ID aliases (2026-11-06)

- `PD-T?nn-mop-cond-codex-C1-03` → `PD-T504`.
