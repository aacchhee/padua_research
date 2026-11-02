# PD-T?argmax-alln-gated-codex-09 — Reduction to four shrinking corner boxes

ID kind: PD-T.
Aliases: direction1 round4 shrinking-corner localization; first four
angular mesh intervals; uniform gap beyond 4pi/n from a side endpoint.
Split from: supporting localization obligation for PD-T099; strengthens
the fixed-corner-neighborhood conclusion of gated-codex-04.
Split into: none. Comparison inside the shrinking boxes remains OPEN.

## Statement

For integer n>=2 define

\[
 K_n=\{(\theta,\phi)\in[0,\pi]^2:
 \min(\theta,\pi-\theta)\ge4\pi/n
 \ \hbox{or}\ \min(\phi,\pi-\phi)\ge4\pi/n\}.
\]

There exists an integer N_* such that, for every n>=N_*,

\[
 \sup_{K_n}\lambda_n\le\Lambda_c(n)-1/3072.              \tag{1}
\]

Consequently every global maximizer lies in one of the four relatively
open angle-corner boxes whose two side lengths are 4pi/n. The threshold
N_* is **non-effective in this record**: no numerical value or finite
coverage up to it is asserted. The full all-degree target PD-T099 remains
OPEN, including the comparison inside these boxes.

## Definitions and assumptions

Even-checkerboard Padua convention, corrected finite polynomial kernel,
positive endpoint weights and exact real arithmetic as in PD-T101 and
gated-codex-01/02/03/08. Lambda_c(n) is the nonnode corner value, attained
at a physical corner; it is not assumed to be the global maximum.
For n>=48 the four boxes are disjoint near their respective corners.

## Status by part

Overall status: **PROVED**, by the analytic sequence argument below with
explicitly cited proved dependencies. Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending).
No numerical experiment is a premise.

| Mathematical part | Status | Evidence / limitation |
|---|---|---|
| Uniform gap (1) on the moving sets K_n | PROVED | Phase cover, localization, local gain and finite adaptive defect |
| Global-maximizer inclusion in the four boxes | PROVED | A nonnode corner supplies value Lambda_c |

Candidate disposition: retained implementation variant of the existing
phase/gain/defect architecture. No novelty claim.

## Depends on

- Gated-codex-01: exact lambda=S-Delta and Delta>=Qv,Qh, and the reflected
  periodic identity for the same primitive.
- Gated-codex-02: global primitive estimate S<=a*Lambda_c+C*log(n+1) on
  the full odd-coset fundamental diamond.
- Gated-codex-03: a fixed local phase neighborhood on which
  sup(S-Lambda_c)=O(log^-2 n).
- Gated-codex-08: exact finite bound Qv or Qh>=1/1536 for n>=48,
  rho<=1/8 and the relevant coordinate endpoint distance >=4pi/n.
- PD-T156 (1) / PD-T157 (1): Lambda_c>=(4/pi^2)log^2 n-54.

The explicit but coarse local constants of gated-codex-07 are not needed
for the non-effective existence statement (1).

## Proof

### Same phases and same primitive at every physical point

Every physical angle point has an odd-coset representation

theta=(J*pi+alpha)/n, phi=(K*pi+beta)/(n+1),

with J,K physical mesh indices, J+K odd and |alpha|+|beta|<=pi.
Indeed choose a physical mesh rectangle containing the point; at a square
boundary choose the adjacent interior rectangle. In normalized fractional
coordinates x,y in [0,1], the distances to the two odd vertices are either
x+y and 2-x-y, or 1-x+y and 1+x-y. In each case their minimum is <=1.
Multiplying by pi gives the claimed closed diamond, with boundary ties
allowed. This argument also covers physical edges and corners.

Endpoint-weighted reflection of both physical meshes identifies the
four-copy majorant with the shifted even periodic lattice sum. Translation
by the selected odd (J,K) changes the board to the odd board of the two
primitive theorems. The corrected cosine mode is retained by the finite
identity; its common sign disappears inside the absolute value. Thus the
exact same S obeys both phase inequalities at these phases, and
lambda=S-Delta<=S. No smooth or unique choice of odd vertex is needed.

### Uniform contradiction argument on the shrinking complement

Put d=1/1536. If (1) fails for arbitrarily large degrees, choose a sequence
n tending to infinity and z_n in K_n with

\[
 \lambda_n(z_n)>\Lambda_c(n)-d/2.                        \tag{2}
\]

At its selected odd-coset phases the global primitive bound gives

\[
 (1-a_n)\Lambda_c(n)\le C\log(n+1)+d/2.
\]

On the diamond the individual phases are in [-pi,pi], so
1-a_n>=(alpha_n^2+beta_n^2)/pi^2. The corner lower bound grows
quadratically in log n. It follows that alpha_n,beta_n tend to zero.
In particular, eventually rho_n=|alpha_n|+|beta_n|<=1/8 and belongs
to the fixed local neighborhood of gated-codex-03. Its uniform local
gain theorem gives S_n(z_n)<=Lambda_c(n)+o(1) along this same sequence.

For each z_n in K_n, either the second coordinate has endpoint distance
at least 4pi/n or the first does. The finite adaptive theorem applies
in that orientation and gives Delta_n>=Qv>=d or Delta_n>=Qh>=d.
The estimate is uniform in the unused coordinate; the orientation may
change with n and no subsequence choice is needed. For all sufficiently
large terms of the sequence,

\[
 \lambda_n(z_n)=S_n(z_n)-\Delta_n(z_n)
                    \le\Lambda_c(n)-d+o(1),
\]

contradicting (2). This proves the existence of N_* for (1).

The Lebesgue function is continuous on the compact angle square because
it is a finite sum of absolute polynomial kernels, so global maximizers
exist. Its value at a nonnode corner is Lambda_c(n); hence every global
maximum is at least Lambda_c(n), whereas (1) bounds every point of K_n
strictly below it. Every maximizer therefore belongs to the complement
of K_n, exactly the union of the four stated relatively open corner
boxes. This proves the final conclusion.

## Checks, scope and open items

This strengthens a fixed-delta localization to a moving 4pi/n angular
scale without substituting delta=4pi/n into a compact-uniform limit.
Instead the finite adaptive rectangle supplies a constant positive
defect. All phase estimates are applied to the same maximizing or
near-level sequence; polynomial collisions, boundary points and changes
of strip orientation are retained by their cited identities.

There is no numerical N_*, no finite certification through an inferred
threshold, no equality classification inside a corner box, and no proof
that the node-corner boxes or nonnode-corner boxes contain only the
expected maximizers. The next corner task has a bounded scaled domain:
both angular distances from a chosen corner are <4pi/n. No such corner
comparison is developed in this record or by this worker in round 4.

## Sources, checks and history

Codex, assigned gpt-6.1-sol xhigh, 2026-11-02; runtime metadata not
independently exposed. Rules/snapshot
`2dde541f1e5af239cae6e93e4438b9be89d15d87`, scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`.
The full candidate/obstruction gate is retained in round 1; this is the
registered round-4 finite-geometry continuation, not a new source transfer.
Supplementary independent review is complete; Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending). No phase
scan, degree grid, fit, Git operation, shared registry change, future
round, or direction-2 work is a premise or execution of this worker.


### Documentation correction — 2026-11-02

F2: the original direct dependency “PD-T159: Lambda_c>=(4/pi^2)log^2 n-54” is corrected to PD-T156 (1) / PD-T157 (1). PD-T159 remains the corner-product comparison behind those bounds; no inequality changes.

N4: N_* in this record denotes only the shrinking-box gap threshold. It is a local symbol, distinct from the eventual exact global-argmax threshold N_* in gated-codex-15; no equality between these thresholds is asserted.

Current review scope (F3): [Claude audit-01](../audit-01.md) ACCEPTED the mathematics exactly as stated; its record/protocol findings and the protocol check of this response remain pending. Supplementary independent checks are complete and do not replace that Claude audit. No proof status, statement, checker predicate or certificate changes. Earlier publication-time review wording is preserved here as history:

> Supplementary independent
> mathematical review and required Claude audit pending at publication
> Independent review and required Claude audit remain pending
