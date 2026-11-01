# PD-N?lattice-c1-codex-02 — Infinite singular Chebyshev subsequence for the unshifted union

Final ID: **PD-N034** (allocated 2026-11-01 under AC's authorisation; the provisional ID above and in the text is retained as provenance — see ID_CROSSWALK.md).

ID kind: PD-N. Aliases: antipodal parity-dimension obstruction; phase0/2 mod4 Chebyshev failure.
Split from: none. Split into: none.

## Statement

Let n≡2mod4, n>=2. On Chebyshev–Lobatto axes `x_i=cos(pi*i/n)`, `y_j=cos(pi*j/(n+1))`, take the phase0 selection `i+j mod4 in{0,1}`. It has N=binom(n+2,2) nodes but its Pi_n evaluation map has kernel dimension at least `(n+2)/4`, so is singular. The same statement holds for phase2 (`{2,3}`). This is a negative statement for these fixed geometric specializations, not for arbitrary labels or shifted phases1/3.

## Definitions, assumptions and status

Work over R; n is an even positive integer in the stated congruence class. Overall status PROVED (developer analytic proof; independent Astra reconstruction pending). Candidate disposition: phase0/2 as an unisolvent Chebyshev family on these degrees REJECTED: failed. Lebesgue interpolation constant is unavailable on this singular subsequence.

## Negative-result scope and dependencies

Attempted mechanism: the fixed Chebyshev specializations of IDEA?lattice-c1-codex-01 phase0, with phase2 retained as its other symmetric phase. Depends on PD-T?lattice-c1-codex-02 for cardinality; symmetry/dimension proof below is elementary. The conclusion says nothing about the observed full generic ranks or odd n.

## Proof

Central inversion sends `(i,j)` to `(n-i,n+1-j)` and physical point `(x,y)` to `(-x,-y)`. Its sum residue is `2n+1-(i+j)≡1-(i+j) mod4`, preserving both phase0{0,1} and phase2{2,3}. The y axis has n+2 divisible4 nodes, hence even length and no zero node: j=(n+1)/2 is not an integer. Thus no selected physical point is fixed by central inversion, and the N nodes form N/2 antipodal pairs. Their cardinality is N by the count theorem.

Write n=2m with m odd. Polynomials containing only monomials of even total degree form a space of dimension `sum_(r=0)^m (2r+1)=(m+1)^2`. Every such polynomial takes the same value on each antipodal pair, so its evaluation image has dimension at most N/2. Rank-nullity therefore gives a kernel of dimension at least

`(m+1)^2 - (m+1)(2m+1)/2 = (m+1)/2 = (n+2)/4`.

This kernel lies inside Pi_n, proving singularity. At n2 one explicit kernel polynomial for phase0 is `3x²-3xy+2y²-2`, since the exact axes are X=(1,0,-1),Y=(1,1/2,-1/2,-1); its row roots are precisely the frozen six nodes.

Phase1 is sent to phase3 by central inversion. Hence their Chebyshev point sets are congruent, with equal true Lebesgue constants whenever unisolvent, and equal singular values in a Chebyshev product basis (row permutation and column signs). This equivalence does not establish their unisolvence or asymptotic stability; their finite tests are recorded separately.

## Checks, sources and scope

Developer float64 diagnostics give ranks5/6at n2 and26/28at n6, consistent with the proved lower bound. These observations do not prove equality in general and are not load bearing. C1/results.json and later shifted results retain all values. No cubature hypothesis is involved. No novelty claim; the dimension obstruction is standard symmetry reasoning.

## Open items and history

Independent reconstruction pending. Shifted phases1/3 escape this specific invariant-subspace obstruction and require separate tests; no negative extension to them is made.2026-10-31, Codex assigned gpt-6.1-sol xhigh, rules/source e949ef06895acd5463cdf8df7e0e5f795218f70f.

## Audit history addendum — 2026-11-01

The pre-acceptance pending wording above is historical. Supplementary [Astra reconstruction](../../../topics/lattice-unisolvence-20261031/independent/report.md) completed, and [Claude audit-01](../../../topics/lattice-unisolvence-20261031/audit-01.md) accepted this exact existing statement and epistemic status. [Response-01](../../../topics/lattice-unisolvence-20261031/response-01.md) changes audit/integration metadata only; no proof, hypothesis, status or finite observation is upgraded. Literature/novelty gaps remain unresolved where stated. Codex administrative response, requested gpt-6.1-sol high; runtime metadata unexposed.
