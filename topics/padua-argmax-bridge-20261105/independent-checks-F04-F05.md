# Independent mathematical checks — F04 entropy cells and F05 transport band

2026-11-07. Distinct Codex supplementary auditor; requested/API-accepted
`gpt-6-astra` ultra, actual serving metadata unexposed. Root's prior written
hard-mathematics justification is in LOG. Rules read at the supplied full
baseline `4a5de2012bad94601c713b2ff5517f2e3fb80af2`; observed HEAD during
dependency review was `7cf34bcee4be9bdd5b4a871426083333a89b7c15`.

Scope is **mathematical validity, definitions, dependencies and edge cases
only**. No novelty/priority judgment, complete novelty-gate certification,
protocol waiver, final-ID review or PR-readiness decision is supplied.
Accordingly the complete ideas registry is not reread for a novelty verdict;
the actual mathematical dependencies and current idea/attempt contracts are
read. F04's chronology remains canonical in
[its attempt](attempts/F04-entropy-cell.md), without disposition here.
Final Claude audit remains separate. Root alone owns Git and shared records.

## Review in progress; no final verdict

Root's exact F04/F05 freeze is required before a final verdict. Moving draft
files are not approved by this preliminary record. Only this audit file is
owned or edited by this auditor. No scientific script/import, numerical or
scalar evaluation, selected degree/endpoint, native or quadrature job ran.

The rules, handoff11, current campaign F contracts, F04/F05 local idea/attempt
records, accepted F01 review and all three F01 EM2 records were read. Relevant
mathematical predecessors read include C06-far-compact-error's generic J,
E12-signed-outer-coupling, E14-wide-signed-outer, E03-joint-row-origin,
E03-joint-outer-log, E05-axis-central-excess and E06-axis-boundary. Accepted
predecessors remain named dependencies; this review is not a recursive
re-certification of every earlier proof or numerical enclosure.

The literal Q operator has m-3 samples, centers h(k+tau), k=2,...,m-2,
and omitted lengths h(3/2+tau) and h(3/2-tau). The paired offsets t,1-t
therefore retain initial total4h and central total2h. For cancellation B,
the exact correction in F04 cancels the constant endpoint part of each
actual hole individually. Other logarithms, pole profiles, fixed-origin
Shift and the separate mesh component do not enter this scalar estimate.

F01's accepted entropy obstruction applies to these unchanged B profiles:
finite global Var(B') cannot be used. F04's proposed proof instead needs an
integrable first-derivative envelope on singular cells and variation only
on the union of cells a positive distance from the complete feature set.

For F05, the accepted exact starting point is the E05 identity

    E_n(alpha,0)-E_n(0)-ell_n sin(alpha)
      = B_n(alpha)-B_n(0)-M_nc(alpha)+M_nc(0)
        + Rcen + (4/(nm)) sum_r Y_r - E_c(alpha,0).

The fixed origin signs define continuous transported Y_r through alpha=e_s;
the natural moving-sign pieces individually have finite opposite jumps.
The signed inner model integral, full smooth background and finite ell_n
cannot be dropped. E06's finite convex-cell estimate has alpha<=h/2 and
cannot certify the new closed c interval through c=1 by substitution.

Further freeze-specific reconstruction and findings will be recorded below.

## F04 frozen reconstruction and verdict

Root explicitly confirmed the final F04 freeze. Independent `sha256sum`
and `wc -c` checks matched all three supplied identities, and the complete
theory was reread after that confirmation:

| File under this topic | Bytes | SHA-256 |
| --- | ---: | --- |
| theory/F04-entropy-cell.md | 14365 | `5408e6a26bb0588a2398cc6c78bae040890f3b5f7817ae97177572cc2aeda330` |
| ideas/F04-entropy-cell.md | 8530 | `49d1e469d8c3112a140dace859cc5c8a857c7d0061ed2ef318b498ea9b9b380a` |
| attempts/F04-entropy-cell.md | 4326 | `ccb336cdba14c52d26efe4dee0d799afc28a2716ecb0bd627a188a243fedb90f` |

The frozen outcome additions to idea/attempt were also read. The generic
N1-round6-central-log formulas were read in full, with D37 section6's
radius-one application checked separately; N1's older half-radius bounds
were not silently extended. A read-only Git comparison reports no change
to the three rule files between the supplied rule SHA and observed HEAD.

The central identity follows by substituting
`J=2(s-u)_+ log(sin e)+R` and subtracting the exact origin
`2a tan(e/2)log(sin e)`. Thus `b_s(0)=0` and the signs of the added
initial logarithms in equation(2) are correct. At zero the initial
formula has limit `-d log pi`; at pi the only nonzero limiting terms
are the finite entropy R and `sigma_s q log pi`. The logarithmic products
with b_s vanish there. These are profile limits, not substitutes for
actual retained polynomial rows.

For `s>u`, writing `D=sqrt(u^2-s^2 sin^2 e)` gives
`(u cos e)^2-D^2=(s^2-u^2)sin^2 e`. The elementary inequality
`A-B<=sqrt(A^2-B^2)` for `A>=B>=0` proves `R_e<=2s` in the root
branch; `u<=s sin e` proves it in the no-root branch. When u=0,
R is identically zero. On every affine-sign piece the nonzero slope
of s with respect to e has magnitude at least a/2>1/3. A coefficient
zero, or the endpoint of a piece containing no zero, therefore controls
the denominator in `log((u+s)/|u-s|)` by distance to a listed feature.
This proves the uniform distance envelope without a lower bound on p,
root separation or distance of a feature from a sample.

The quartic P is genuinely nonzero, since `u^2-4a^2<0`. Its four-root
bound applies across the right absolute-value switch because s^2 has
the same polynomial on both sides. Coefficient zeros and the switch
give at most8/10 total sites after endpoints and the join are included.
The derivative-critical equations were reconstructed directly:

    (R_s)'=0 implies 2X'P-XP'=0,
    (R_e)'=0 implies 2P-xP'=2u(1+x^2)sqrt(P).

The first polynomial has degree at most6 and the squared second has
degree at most8. Squaring is used only for an upper bound on candidates.
In the identically-zero first case the ratio sqrt(P)/X is constant on
each root interval. In the identically-zero second case the unsquared
left side cannot change sign while P>0 and u>0; the original derivative
is consequently identically zero or strictly negative. The same-sign
and no-root pieces are monotone directly. Adding the coefficient and
quartic boundaries gives the stated12/14 pieces per affine piece,
hence24/28 per side. Values agree at the finite root transitions;
the divergent coefficient-zero sites are excluded from the good set.
Repeated and coalescing roots only reduce the partition count.

The total variation on disconnected good intervals is correctly defined
without variation across gaps. Restrictions of one monotone piece spend
at most its full range, even if a number of gaps cut that piece. Product
variation then gives52A for R_s*s',84 for R_e,24A for b_s'log(sin e),
14A for b_s cot e, and the stated smooth and initial/join charges.
Thus each side costs at most90A+94, and their sum is below400A for A>1.
No claim of globally finite Var(B') is made.

For a singular cell, integrating the distance logarithm over an arbitrary
interval gives the bound at its actual center, including equality of a
sample and feature. Absolute continuity follows by truncating at finitely
many features, using their continuous limits and the integrable envelope.
At most100 bad cells is conservative: a site affects only centers in an
interval of length3h. The remaining actual cells use the centered Peano
kernel with maximum h^2/8. This is a fixed-sample estimate, not a
translation-averaged estimate.

The four omitted intervals have their literal lengths in[h/2,5h/2].
After the endpoint correction, their total cost is bounded by1125 times
`(h^2/pi)[1+log(24/h)]`. The bad and good cells add6000 and50 in the
same units. Their sum is7175. Since `h^2/pi=pi/m^2`, `pi<4`, and
`log(24/pi)<log8<3`, the resulting bound is strictly below
`114800(1+log m)/m^2`, hence below the claimed120000 bound. These
comparisons were reconstructed as written inequalities, without a scalar
evaluation or selected-degree job.

**F04 ACCEPT:** no unresolved mathematical finding in the frozen claim.
The accepted scope is precisely all integer n>=32 and the closed signed
band1/32<=rho<=1, with separate absolute phases, both parities, axes and
coincident features. For boxes extending beyond this band only their
intersection is covered. This certifies the cancellation-block feasibility
bound and its four endpoint corrections. It supplies no useful onset,
five-fourths extension, full I06/D13 estimate, implementation or numerical
certificate. F04 chronology, novelty/priority and final Claude audit remain
outside this mathematical verdict. F05 is still awaiting its exact freeze.
