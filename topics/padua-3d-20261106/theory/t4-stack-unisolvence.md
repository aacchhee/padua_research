# PD-T?padua-3d-codex-T4-01 — Padua-plane stack and Newton recursion

ID kind: PD-T. Aliases: Radon/Berzolari stack; plane removal.
Split from: none; supplied BRIEF E2 baseline. Split into: none.

## Statement

For every integer n>=0 and every sequence of distinct real heights
z_0,...,z_n in [-1,1], let

X_n = union_{k=0}^n (Pad_{n-k} x {z_k}),

where Pad_m is the even-checkerboard planar Padua set and Pad_0={(1,1)}.
Then |X_n|=binom(n+3,3) and evaluation on X_n is an isomorphism from the
real total-degree polynomial space Pi_n(R^3). The Newton recursion below
constructs its unique interpolant for arbitrary real node data.

## Definitions and assumptions

For m>=1, Pad_m={(cos(i*pi/m),cos(j*pi/(m+1))):0<=i<=m,
0<=j<=m+1, i+j even}. Denote its planar interpolation operator by A_m.
Its all-m unisolvence is the real specialization of PD-T004. Set A_0 g=g(1,1).
For arbitrary data f_k on Pad_{n-k}, let omega_0(z)=1 and
omega_k(z)=product_{j<k}(z-z_j). Define recursively

q_k = A_{n-k}[(f_k - sum_{i<k} omega_i(z_k)q_i)/omega_k(z_k)],
p(x,y,z)=sum_{k=0}^n omega_k(z)q_k(x,y).

The notation A applied to a vector means the unique polynomial interpolating
that vector. No nesting or commutation of the A_m is assumed.

## Status by part

Overall status: **PROVED**, developer-written analytic proof, pending
independent mathematical audit. Candidate retained as known-method baseline;
no historical novelty claim. Numeric checks are not proof dependencies.

## Depends on

PD-T004: exact canonical planar Padua unisolvence over R, with the displayed
node convention. Elementary polynomial division and dimension counting.

## Proof or evidence

The planes are disjoint and each Pad_m has binom(m+2,2) nodes, including m=0.
Their sum is binom(n+3,3). Suppose p in Pi_n vanishes on X_n. The restriction
p(x,y,z_0) has total degree <=n and vanishes on Pad_n, hence is identically
zero by planar unisolvence. Polynomial division in z (over R[x,y]) gives
p=(z-z_0)p_1, with p_1 in Pi_{n-1}. At every remaining node z=z_k the factor
z_k-z_0 is nonzero, so p_1 vanishes on the degree-(n-1),...0 tail stack.
Repeat the argument n+1 times. A degree<=n polynomial divisible by all n+1
distinct linear factors in z is zero. Thus evaluation is injective between
equal finite dimensions and is bijective.

For the constructive formula, q_k has planar degree<=n-k, so omega_k q_k
has total degree<=n. At layer k, terms i>k vanish because omega_i(z_k)=0;
the defining residual equation supplies the prescribed data from terms i<=k.
Every denominator omega_k(z_k) is nonzero. Thus p interpolates all data;
uniqueness is the preceding argument. This proof includes n=0.

## Checks / sources

The formula is the supplied Radon/Berzolari construction, reconstructed here
without importing an unread historical theorem. Source priority remains a
primary-fulltext gap in literature-T4.md. Topic-local numerical recursion
checks are planned; no run is claimed in this initial record.

## Scope and open items

This theorem holds for every height ordering; it proves no quality bound.
The O(log^3 n) quality target remains OPEN in t4-quality-target.md.
Independent audit of this hand proof remains pending.

## History

2026-11-06, Codex developer, assigned gpt-6.1-sol/xhigh (runtime model metadata
unexposed), rules/input ccd9e905d19c0c625c196c4a3f3e707058ed042a.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-computation.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
new response dispositions/ID-kind/evidence changes require focused re-audit,
not another approval of the unchanged accepted mathematics.


## Executed-check correction — 2026-11-06 — m5

The initial planned/no-run description is superseded: the producer compared
Newton and direct cardinal evaluation through n=4, maximum discrepancy
7.51e−14 (MEASURED; evidence/t4-mesh-*.json), and audit-01 independently
checked the construction. The all-n divisibility/Newton proof is analytic.
