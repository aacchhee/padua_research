# Padua argmax bridge — current research results

The exact two-corner global argmax is proved for **degrees2–40** and
**every integer n>=16000**. Its equality set is {(-1,-1),(1,-1)} for
even n and {(-1,-1),(-1,1)} for odd n. The remaining gap **41–15999**
and all-degree PD-T099 stay OPEN. This is a sufficient upper boundary,
not a claim of the minimum onset.

[Global theorem](../topics/padua-argmax-bridge-20261105/theory/D11-global-comparison.md),
[independent reconstruction](../topics/padua-argmax-bridge-20261105/independent-checks-D11-onset.md).
The proof covers the full closed square, both parities, nodes, axes,
collisions and exact equality, without an energy premise or mass degree scan.
For n>=16000: far S<Lambda_c-19/100; near noncorner
lambda<Lambda_c-7/1000; actual corners
lambda<=Lambda_c-(alpha²+beta²)/4. New comparison domains and monotonicity
are proved; the primary16000 budget passed, no20000 fallback ran.
The new near argument uses the true fractional constant modulus directly.
PD-T271's certified corner constant is an explicit dependency. Final Claude
audit remains pending. Older D08/C13 theorems retain their stated scopes.

The guarded actual-Lebesgue point evaluator independently reproduced all13
fixed cases,10 finite-polynomial references and6 invalid controls in
12.008287CPU including build. Its n512 generic point takes2.093014CPU,
full Arb radius<2.584e-16, with3 safe whole-row fallbacks. This is a point
component; complete whole-box certification and new degrees remain OPEN.
[Replay](../topics/padua-argmax-bridge-20261105/independent-checks-D07-fourcopy-result.md).

A separate computer-assisted local theorem now certifies both actual
degree512 corner rectangles with lambda<=Lambda_c-(19/5)(alpha²+beta²),
using only three point losses and global norm34. Trial11.265079CPU,
independent fresh replay11.015692CPU. These rectangles cover rho<=1/2;
full degree512/global complement coverage remains OPEN.
[Patch proof](../topics/padua-argmax-bridge-20261105/theory/D09-corner-patch-512.md).

The new fixed-work checker PASSes all364 regions of the unchanged known
n32 certificate in **46.09totalCPU seconds**(45.23subprocess), versus
139.41subprocess previously: about3.08times faster. It recovers all76
preserved first-attempt failures, with no new tree, mode switch, retry,
producer or certified degree. All254 enumerated native/build, project-Python and recorded runtime
identities were checked; this excludes standard-library hashing and
is not a hermeticity claim.
[Whole-run outcome](../topics/padua-argmax-bridge-20261105/independent-checks-C03-cheap-n32.md).

Separately, guarded linear-work point and whole-box S-upper methods now
have mathematical and source checks. Point pilots take.150CPU at n128
and2.456CPU at n2048; timing scopes are recorded in the attempts. The
native whole-box API is limited to n<=4096 and nonnegative rational
rectangles contained in the closed phase triangle. It supplies no
standalone gradient, corner-orbit or defect certifier.

The shared eight-vertex variant has independently accepted source
validation but **mixed quality and roughly twice C12's n32 cost**.
Neither row bound certifies the two selected known far leaves. This
is enclosure insufficiency, not a mathematical counterexample. No full
replacement certifier, new degree or end-to-end scaling claim follows.
[Source review](../topics/padua-argmax-bridge-20261105/independent-checks-C15-global.md).

The original **15/15** coordinated rounds are complete. The new25-round
post-audit campaign continues; its ledger is the current count. Historical
D01–D06 paragraphs below retain the boundary known at each checkpoint. AC asks
for an INTERIM Claude audit with its own independent ideas, then WORK
with Codex implementing. A clean interim audit must not promote to PR.
PR27 remains draft WORK; final shared-registry application and final audit
are pending. Major archive cleanup remains a separate topic; no Syvert
pack is justified by point-only timings. See the
[report](../topics/padua-argmax-bridge-20261105/report.md) and
[campaign ledger](../topics/padua-argmax-bridge-20261105/campaign-20261106.md)
for exact proof dependencies, costs, failures and remaining work.

Post-audit campaign D01/25 is complete. Independent checks establish two
scoped restrictions: the frozen C07 corner envelope misses its K0<=4
target, and the unchanged fixed-cutoff far model has a genuine nonzero
midpoint bias, ruling out uniform C(1+log n)/n decay. The old half-million
result remains intact. Signed diagnostics expose geometry cancellation;
new joint/bias-aware estimates are the next task, not more precision on
the failed envelopes. [D01 record](../topics/padua-argmax-bridge-20261105/campaign-post-audit-20261106.md).

D02 is complete,2/25 new rounds. Independently accepted analytic proofs
give actual-corner descent lambda<=Lambda_c-(alpha²+beta²)/4 on both
inward rho<=1/2 patches for every n>=10000. This is local; global argmax
still starts at500000. The far work proves the exact full-phase cutoff
bias, identifies the uniform true limiting constant and gives an exact
all-n boundary error formula. Its practical interior rate remains OPEN.
[Corner review](../topics/padua-argmax-bridge-20261105/independent-checks-D02-corner.md),
[far review](../topics/padua-argmax-bridge-20261105/independent-checks-D02-far.md).
D03 continues with joint cancellation and cheap near-only feasibility.

D03 is complete,3/25. Its accepted cancellation-perturbation lemma has
error112P H_n/(pi n); the full reference estimate remains OPEN. The
n512 float pilot cost486.136CPU and reached both128-visit caps with
60/82 unresolved boxes. This measures incomplete feasibility, with no
new degree or exact-checker throughput claim.
[D03 result review](../topics/padua-argmax-bridge-20261105/independent-checks-D03-pilot-result.md).
D04 continues with the endpoint reference and fixed-work component adoption.

D04 is complete,4/25. Its accepted analytic row reduction has no
fixed-R floor and applies with at most8 special rows from n16.
The native component test stopped at65CPU on its first512box; no box
quality result completed. This motivates a different cost structure,
not a larger run of that source. D05's uniform shrinking-model error
has since passed review; the global threshold remains500000.
[D04 mathematics](../topics/padua-argmax-bridge-20261105/independent-checks-D04-row-reduction.md).

D05 is complete,5/25: an explicit full closed-phase O((1+log n)/n)
error bound for the completed far model is independently accepted from
n32. A fixed-special-set version needs only six exact rows; the full
relative near comparison and validated implementation remain OPEN.
Practical constants are being assessed in D06; this is not a new global
argmax threshold.
[D05 model-error review](../topics/padua-argmax-bridge-20261105/independent-checks-D05-outer-comparison.md).

D06 is complete,6/25. Exact formula obstructions show the frozen error
allowance cannot meet its desired small-degree budgets. A separate
accepted four-copy row identity reduces actual pointwise Lebesgue sums
to cubic/quartic sign blocks and cotangent partials. This is a new
structural component, not yet a fast or whole-box certifier. D07 continues
with sharper budgets and a guarded implementation; global argmax remains
2–40 and all n>=500000.
[Row-structure review](../topics/padua-argmax-bridge-20261105/independent-checks-D06-four-copy-rows.md).
