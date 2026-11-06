# Padua argmax bridge — current research results

The exact two-corner global argmax is proved for **degrees2–40** and
**every integer n>=1000000**. Its equality set is {(-1,-1),(1,-1)} for
even n and {(-1,-1),(-1,1)} for odd n. The remaining gap41–999999 and
all-degree PD-T099 remain OPEN. The analytic threshold has fallen from
the initial exp(10^12) to one million, without a mass finite-degree scan.

- [Global theorem](../topics/padua-argmax-bridge-20261105/theory/C08-effective-million.md) and [independent reconstruction](../topics/padua-argmax-bridge-20261105/independent-checks-C08-global.md).
- [Far comparison](../topics/padua-argmax-bridge-20261105/theory/C08-far-model-comparison.md): S<Lambda_c-6/25 throughout rho>=1/2, n>=10^6.
- [Actual near noncorner comparison](../topics/padua-argmax-bridge-20261105/theory/C05-finiteh-model-comparison.md): lambda<Lambda_c-869/28000.
- [Actual corner comparison](../topics/padua-argmax-bridge-20261105/theory/C07-corner-million-onset.md): lambda<=Lambda_c-(alpha²+beta²) on both inward half diamonds.

The full closed cover, axes, nodes, collisions, parity and exact equality
set are included. The far proof uses a fixed-count full-phase model,
uniform error<9/25, exact coefficient/endpoint/integral bounds and a
stronger finite corner lower bound. Every component is analytically
proved and independently reconstructed; floating diagnostics are not
proof premises. A same-model onset audit is investigating smaller
thresholds; none is claimed yet.

The near comparison uses the unchanged fixed-count model, its proved
3/14000 primitive error and a sufficient model allowance1/32, together
with all-class projected defect>1/16. Original tight C1 with1/4096 is
still OPEN at n>=10^6. No second correction was introduced. A separate
finite positive-deformation result proves Lambda_c>=(nL_n²+1)/(n+1)
for every n>=2, improving the usable corner lower bound without changing
the existing asymptotic remainder theorem.

The new cheap checker **PASSes all364 regions of the unchanged known
n32 certificate in46.09totalCPU seconds** (45.23subprocess), versus
139.41subprocess for the previous accepted checker: about3.08times faster.
It recovers all76 failures of the preserved first fixed-work attempt,
without changing the tree, running a producer, switching modes or adding
a new certified degree. All254 build/runtime identities were checked.
[Independent whole-run outcome](../topics/padua-argmax-bridge-20261105/independent-checks-C03-cheap-n32.md).
This finite known-case result is not a scaling theorem; original producer
cost222.81CPU has not yet been reduced by that checker result.

The [exact-real row reduction](../topics/padua-argmax-bridge-20261105/theory/C02-row-cotangent.md)
offers an O(n) point representation. Its partial-cotangent backend passed
independent LP64 source/control review,76 native cases and784 exact moment
checks in2.69CPU seconds. Guarded full point-S integration has now passed independent review.
Its first prototype was slow(n128:11.55CPU seconds). Independently
accepted interval moment evaluation and fixed J16 tuning now give
0.150CPU at n128 and2.456CPU at n2048 in bounded point pilots. These
are point costs, not whole-certifier costs. Direct moving-root whole-box
enumeration has a proved fixed-width quadratic obstruction; the guarded
linear-work convexity escape is independently accepted mathematically
and its implementation is in progress. The new MPFR producer component has passed
independent review after a geometry guard repair; its complete known-case
producer run is not yet released.

Finite energy2–128 and its analytic tail, N4/N6 scoped failures, N5's OPEN
quarter target and earlier failed mechanisms remain preserved in their
records. They do not close the finite global gap. No practical Syvert pack
is ready. Major archive cleanup remains a separate topic.

Eleven fresh coordinated rounds are complete; useful C12/C13/C14 work continues
within AC's authorized allowance of15. Formal **Claude Opus5.5 xhigh audit
is PENDING**; independent Astra checks supplement it. PR27 remains draft
WORK with final shared-registry application pending. See the
[current report](../topics/padua-argmax-bridge-20261105/report.md) and
[campaign ledger](../topics/padua-argmax-bridge-20261105/campaign-20261106.md)
for exact scopes, costs and remaining work.
