# T2/T3 verification receipt and reproducible commands

Rules/input: `3f5196cf3639407c25b021fa30f70cc1d3ae113a`; scientific base
`440d107`. Developer assigned Codex gpt-6.1-sol xhigh for mathematics.
Python 3.12.14, local managed Linux workspace; standard library only for
both certified routes. No random seeds, network service or external
machine. Small receipts are essential finite evidence, each under 4 KiB.

## Mathematical reduction and trusted arithmetic

Theory [t2-01](../theory/t2-01-edge-centre-minima.md) proves the exact
one-dimensional formulas for the inherited double integrals. Theory
[t3-01](../theory/t3-01-general-position-series.md) proves the series and
tails at every interior angle. The series evaluator performs finite exact
Fraction sums of those proved terms; it encloses sqrt by integer roots,
log by a positive atanh series with geometric tail after powers-of-two
reduction, and pi by the Machin alternating series. Machin's normalization
is also independently justified in inherited PD-T188. The final decimal
floor and ceiling are exact integer operations. These are the trusted
standard-library integer/Fraction operations.

The quadrature checker is a different numerical route. It uses F's
elementary logarithmic formula and direct tangent-integral quadrature for
K, avoiding T3's expansions. F and F(r)/r decrease, giving vertical
Darboux endpoint sums. For the horizontal inner integral the exact
reciprocal tangent split is

`K(sqrt(1-t²)) = 2 int_0^(1/sqrt(t)) [(1+x²)(1+t²x²)]^(-1/2) dx`.

Its integrand decreases; the outer K factor increases and 1/(1+y)
decreases, giving separate factor bounds on each cell. The remaining
strip y>1-epsilon, epsilon=1/4096, is bounded using t2-02's proved K
logarithm estimate by

`epsilon/(2-epsilon) * [log(4/q)+q/2+(1-log(epsilon))/2]`

before multiplication by 8/pi². Decimal42 algebra uses ROUND_FLOOR and
ROUND_CEILING. Decimal sqrt/ln are correctly rounded; enlarging by one
adjacent decimal encloses their exact values. Negation is exact
`copy_negate`; long sums are explicitly directed. These standard-library
Decimal guarantees are the additional trusted numerical dependency.

## Executed developer commands

From the repository root:

```sh
python topics/padua-lebesgue-followups-20261103/code/t3_series.py --terms 72 --digits 16 --output topics/padua-lebesgue-followups-20261103/evidence/t3-series-developer.json
python topics/padua-lebesgue-followups-20261103/code/t3_quadrature.py --series-receipt topics/padua-lebesgue-followups-20261103/evidence/t3-series-developer.json --output topics/padua-lebesgue-followups-20261103/evidence/t3-quadrature-developer.json
```

Both exited 0. The quadrature explicitly asserts containment of each of
the five exact-series enclosures. Source identities are embedded in the
JSON receipts. Final exact evaluator SHA256:
`55e2a9760e52f3ce522dddc707f87f60ff1d71877695ad2804485edd72cec259`.
Quadrature evaluator SHA256:
`7f8f5772576ed8fe765adb9bf5328e9f8b90b88f2499edf928b45d522a14f656`.
Final developer series receipt SHA256:
`06de81671732b4d487e4cf0fe3463f55ac23dc10928b66ebcc89de2e5f45d3b8`.
Final developer quadrature receipt SHA256:
`99d3ed87fc421818ff58a6d083f5109236062da2835df6a443cb603043d77edb`.
Final independent command/hash receipt SHA256:
`b4fa13a819c451d0feb973445b6e28d38a34764c2a8a729591720909e50faebc`.
The independent report records the final adaptive-sqrt code review and
separate reruns; the regenerated developer and independent JSON agree.

| cos² beta | beta in first half-edge | g_v enclosure | g_h enclosure |
|---|---|---|---|
| 0 | pi/2 | [0.5485148423995582, 0.5485148423995583] | [1,1] |
| 1/4 | pi/3 | [0.6941779799375061, 0.6941779799375062] | [1.0675180074406826, 1.0675180074406827] |
| 1/2 | pi/4 | [0.8827756416527839, 0.8827756416527840] | [1.1657259834417526, 1.1657259834417527] |
| 3/4 | pi/6 | [1.1684098246651837, 1.1684098246651838] | [1.3405785602591445, 1.3405785602591446] |
| 99/100 | arcsin(1/10) | [2.2009074981919784, 2.2009074981919785] | [2.2140396535603800, 2.2140396535603801] |

Default quadrature: 512 vertical cells, 64 outer horizontal cells, 128
inner tangent cells. Its widths are about 7.2e-5–0.01 vertically and
0.041–0.076 horizontally. They provide a coarse certified implementation
crosscheck. The 16-place digits come from the exact series and proved tails.

A separate boundary robustness check at m=1-2^-300 verifies that the
adaptive integer-square-root upper bound stays strictly below 1; this
prevents a spurious zero divisor in atanh(p). It was executed and passed.

## Independent checks and limits

Distinct Astra agent `/root/analytic_check` independently reconstructed
all three theory records and separately ran the exact evaluator and
outward quadrature. It also independently implemented a direct float64
quadrature of the original double integrals with their exact switches;
that finite diagnostic agrees within 3.6e-15 and remains MEASURED.
Commands, hashes and receipts are in
[independent-checks-analytic.md](../independent-checks-analytic.md).

The two analytic minima and endpoint theorems do not depend on numerical
evidence. The series identities/tails are proved independently of the
finite code run. Exact finite digits additionally use the committed
evaluator, small receipts and distinct replay. No finite-n ordering,
uniform endpoint convergence in degree or all-degree argmax is asserted.
Required Claude audit remains pending.
