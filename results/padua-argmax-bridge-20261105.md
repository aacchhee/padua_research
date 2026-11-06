# Padua argmax bridge — current research results

The exact two-corner global argmax is proved for **degrees2–40** and
**every integer n>=500000**. Its equality set is {(-1,-1),(1,-1)} for
even n and {(-1,-1),(-1,1)} for odd n. The remaining gap **41–499999**
and all-degree PD-T099 stay OPEN. This is a sufficient upper boundary,
not a claim of the minimum onset.

[Global theorem](../topics/padua-argmax-bridge-20261105/theory/C13-onset-budget.md),
[independent reconstruction and focused repair review](../topics/padua-argmax-bridge-20261105/independent-checks-C13-onset.md).
The proof covers the full closed square, both parities, nodes, axes,
collisions and exact equality; it uses no energy premise or mass degree scan.

At every n>=500000 the three cases are:

- Far phases: S<Lambda_c-1/2000.
- Near noncorner centers: lambda<Lambda_c-1/32.
- Both inward actual-corner patches: lambda<=Lambda_c-(alpha²+beta²)/6.

The unchanged fixed models are controlled by explicit analytic errors,
weighted coefficient bounds, finite endpoint/collision estimates and a
stronger corner lower bound. Lower-domain conditions were rechecked
rather than inferred from the older n>=10^6 theorems. The single near
correction remains the only one; original tighter C1 is still OPEN and
unnecessary for this actual global result. C13's split/baseline review
findings are resolved. An INTERIM Claude audit-01 found no BLOCKING/MAJOR finding (nine MINOR record findings to answer); the formal final Claude audit remains PENDING.

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

All **15/15** newly authorized coordinated rounds are complete. AC asks
for an INTERIM Claude audit with its own independent ideas, then WORK
with Codex implementing. A clean interim audit must not promote to PR.
PR27 remains draft WORK; final shared-registry application and final audit
are pending. Major archive cleanup remains a separate topic; no Syvert
pack is justified by point-only timings. See the
[report](../topics/padua-argmax-bridge-20261105/report.md) and
[campaign ledger](../topics/padua-argmax-bridge-20261105/campaign-20261106.md)
for exact proof dependencies, costs, failures and remaining work.
