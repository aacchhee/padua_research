# Focused review 02 — explicit compact-support witness

2026-11-13. Codex, `gpt-6-astra`, high. Candidate `6c178e9d657419467c8b6eed2909ffa1347a32eb`; current/rules head `4200087fbb30727a196e0ae86be29236f7d18917`. Previously read rules were checked unchanged by read-only diff against `8b27da5ea2e0d363d2a416482b176466dc33efa9`. Read handoff 05, response-01 A1/A4, audit-01 A1/A4, the revised target and compact script, their receipts, and the exact coefficient expansion imported from gamma_certificate.py. No development file or Git state was changed.

Scope is A1/A4 and their changed dependencies only. Accepted -02/-03/-04 claims are not reopened. The revised general gamma certificate is reviewed by another worker. Novelty claims are outside this bounded mathematical assignment.

## Verdict

**A1: the compact-support construction repairs the original mathematical mismatch.** Its analytic proof and code pass inspection and the scoped controls below. The status history now preserves the original OPEN target and identifies the earlier premature closure. A numerical display chain needs the MINOR correction C1 below. The actual theorem's numerical lower bound is consistent with the retained precise receipt.

**A4: fixed.** `theory/explicit-gamma-target.md:10` now gives the exact finite-route ratio, the correct counting identity and the conservative sufficient criterion, without claiming necessity.

**Replay limitation:** the coefficient-dependent compact-checker run was **not performed**. The pinned third-party ancillary input could not be retrieved (fresh HTTP 403). The 267048.4365… second-moment bound was checked for arithmetic consistency and code derivation, not independently regenerated from the 123 source coefficients. Acceptance of the data-dependent bound remains subject to the overall audit's treatment of that missing replay and of -07(L). Neither synthetic controls nor reading the developer's PASS receipt is called a replay here.

## C1 — MINOR: rounded loss does not imply the printed last decimal

Location: `theory/explicit-gamma-target.md:42`.

The displayed chain claims

```
gamma1 - 3.0043e-5 >= 0.0278115257.
```

Using the certified gamma1 interval in `evidence/gamma-certificate.json` gives instead

```
gamma1 - 3.0043e-5 = 0.0278115256907765546... < 0.0278115257.
```

This is only an intermediate rounding/display error: the precise loss receipt gives the stronger valid lower bound 0.0278115257416687140…, so the theorem at line 27 (>=0.02781152574) and excess over 1/36 survive. Requested fix: distinguish the coarse display estimate from the precise receipt, or retain sufficient digits of the loss in this chain. For example, the coarse chain may end at 0.0278115256, while the next sentence states that the precise receipt yields the theorem's value. No mathematical mechanism or principal threshold must change.

## Independent proof reconstruction

1. The centered order-four B-spline is nonnegative, supported on [-2,2], with M4(0)=2/3. For t>=0, its normalized form beta is `1-(3/2)t^2+(3/4)t^3` on [0,1] and `(2-t)^3/4` on [1,2], and zero afterward. Both pieces decrease, match at 1 with value 1/4, and give maximum 1 at zero. Reflection gives 0<=beta<=1 everywhere. Its Fourier transform is (3/2)sinc^4, nonnegative and integrable.
2. On |t|<=1 the deficit is `(3/2)t^2-(3/4)|t|^3`; outside that interval it is at most one. Therefore the stated global quadratic deficit bound holds. For numbers b_i in [0,1], telescoping `1-product b_i` gives at most `sum(1-b_i)`. Hence `1-g(eta)<=(3/2)|eta|^2`.
3. Multiplication by g(xi/R) preserves value one at zero, continuity, the sign outside the octahedron and compact support in [-2R,2R]^3. The Fourier transform is convolution with the nonnegative scaled transform of g. Both transforms are integrable, so the convolution identity is justified. No assertion that a Gaussian itself is compactly supported remains.
4. The integral loss is at most `(3/(2R^2))*integral |phi(xi)||xi|^2`. The dilation `x=alpha*xi/2` contributes three Jacobian powers and two moment powers, exactly `(2/alpha)^5/P(0)`; P(0)>0 is a dependency from -07(L).
5. Expanding P in even monomials and applying the triangle inequality gives the sum of absolute coefficients times `sum_i m(a+e_i)`. Integration by parts gives the one-dimensional recurrence `I_b=(2b-1)I_(b-1)/(2*pi)`, with I_0=1. Products yield the double-factorial formula in the record, including b_i=0 with (-1)!!=1.
6. The actual gamma_compact.py implements that sum with exact rational coefficients from P_in_y, arbitrary-size integer double factorials and Arb arithmetic. Multiplication by 3/4 for gamma produces loss factor `9/(8R^2)`. Comparing the whole Arb ball with exact 1/36 certifies the conclusion if all dependencies and inputs are valid.

## Receipt input and fixed scope

`code/gamma_compact.py:56` removes the printed uncertainty from `gamma1_lower`, then subtracts 1e-40. This is safely conservative for the **actual pinned receipt**: the omitted printed radius is 4.52e-78, and 256-bit decimal-conversion error is much smaller than 1e-40. An Arb comparison verifies that the entire resulting g1 ball lies strictly below the entire printed lower-end ball. The receipt hash stored in gamma-compact.json exactly matches the current gamma-certificate.json; the compact-script hash also matches. Both receipts and the theorem use alpha=1001/1000 and R=100000.

The CLI is not a general authenticated validator of arbitrary gamma receipts: it checks PASS, but does not itself validate the receipt's source hash/alpha or bound the discarded textual radius. Likewise arbitrary --alpha/--R inputs are not checked against the fixed theorem. These are coverage limits, not a counterexample to this pinned computation; the relevant identities and radius bound were checked explicitly here. No general-input guarantee is inferred.

## Executions and results

1. Fresh retrieval attempt:

```
curl -fLsS --max-time 30 https://arxiv.org/src/1510.02331v3/anc/octa_double.func.cpp -o /tmp/compact-audit-octa.cpp
```

Result: HTTP 403, exit 22. No source input was available under the searched readable workspace/scratch paths. The other gamma auditor independently reported the same access failure. Thus the handoff's real compact-checker command was not run.

2. Scoped controls, committed separately as audit code:

```
PYTHONPATH=/tmp/padua-audit-gamma/deps python3 -B topics/padua-effective-cubature-20261112/audit-work/compact-controls.py
```

Runtime: Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5, SymPy 1.14.0. The PYTHONPATH points to scratch dependencies retained from audit-01; it contains no mathematical input.

Final result: all controls passed. The script checks:

- exact B-spline pieces, endpoints, derivatives and the inner deficit identity;
- conservative parsing of the actual gamma lower-end receipt;
- conditional recomputation from the retained second-moment interval, returning compact gamma `[0.02781152574166871401325173912122604912485667291051482989941147222677235733499 +/- 6.02e-78]`, greater than both 0.02781152574 and 1/36;
- reproduction of C1's false rounded display inequality;
- execution of the **actual compact script's arithmetic**, with its source reader explicitly replaced by synthetic coefficients for `P=1-2|x|^2+3*sum x_i^4` and a synthetic receipt. An independent Gaussian-moment calculation gives `S=3/(2*pi)+15/(2*pi^2)+189/(8*pi^3)`, matching the actual script. With the synthetic receipt, R=100000 accepts and R=1 rejects as expected. These inputs have no asserted Delsarte sign properties and are not substitutes for the missing DGOV run.

The first draft of the audit control used interval overlap to compare a serialized lower endpoint with an independently evaluated full ball and failed that overly strong check. Endpoints from different valid evaluation orders need not overlap each other's tighter intervals. The control was corrected to bound the endpoint discrepancy by 1e-60; all final controls then passed. No development code changed in response to that audit-control correction.

No further substantive defect was found in the changed compact-support argument. The explicit bound and code remain conditional on verification of their actual source coefficients and the separately reviewed -07 certificate, with the missing replay clearly retained above.
