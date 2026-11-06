# C05 actual-corner continuation — explicit quarter-angle result

The exact quarter-angle identity passes. The full analytic proof in
theory/C05-corner-quarterangle-bound.md establishes

    lambda_n(z_n)<=a Lambda_c+[(1/3)log(n+1)+38]r2,
       n>=10^6, rho<=1/2,

at both actual nonnode corners. It implies strict comparison on the
entire punctured inward half diamond for log n>=25. This is a corner-patch
onset only; a global argmax conclusion still needs a complementary proof.
The original strict comparison at every n>=10^6 remains OPEN.

The important quantitative step is summing with g=|j-r+j/n| before taking
its worst value. In the r=j+1 regular strip, the variation away from
g=1 is integrable after its factor j/n cancels the summand's 1/j. Its
cost is constant rather than a large logarithmic coefficient. Rectangular
averaging permits pure coordinate second derivatives and factors out a
exactly. The sine channels and polynomial B family are charged separately,
including initially zero cardinals and all endpoint/collision multiplicities.

No mathematical computation, numerical kernel evaluation or fit was run.
All previous proof/review bytes are unchanged. Distinct reconstruction
and the formal Claude audit are separate; no developer self-approval.

The remaining constant38 is mostly the coarse negative-l=1 tail and
finite collision family. A later smaller-onset refinement could vary their
split or use their signs more sharply, but neither an optimized split nor
an n>=10^6 strict theorem is claimed. The weighted-energy alternative
remains unpursued and unassumed; finite2–128 evidence is not extrapolated.

2026-11-06, rules/input 4b728b04216a5490910780bc609a82b853058426.
Codex, parent-requested Astra ultra; serving metadata unexposed.
