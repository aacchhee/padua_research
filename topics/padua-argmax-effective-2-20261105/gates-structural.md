# A0 / A1 structural checkpoint — 2026-11-05

Input and rules: `ed21cc0bf205549936fccde90244a291bc6de324`.
Developer: Codex mathematical worker, AC-requested gpt-6-astra ultra; runtime metadata not independently exposed. Python 3.12.14. Independent checks are separate and the required Claude audit remains pending. No final IDs assigned.

## A0 — conditional arithmetic diagnosis confirmed, with a sharper diagnostic retained

Executed:

```text
python topics/padua-argmax-effective-2-20261105/code/a0.py
```

SHA-256 of a0.py: `9032b20218b4e9816773b30bbb6d08644053ba16b92d0efe5673dac786d540dc`.
No randomness or external inputs. The command uses floating standard-library arithmetic; its roots are not outward enclosures.

For hypothetical C=1.4–1.7, the original sufficient localization inequality and the rigorous quadratic corner lower bound give log n approximately 279291.75–339139.90 at ρ=1/64, and 17456.12–21196.63 at ρ=1/16. The claimed order 3×10⁵ is correct for the **written coarse route**. Neither radius meets the original 10⁴ reopening threshold. A specified C in this interval has not been proved globally.

The exact geometric lower factor 1−cos(ρ/2) sharpens those arithmetic ranges to 113193.50–137449.16 and 7075.53–8591.62 respectively. The latter crosses 10⁴ and is preserved as a separate refinement, not concealed by a general rejection of R1. It still does not close the bridge: the inherited defect radius is 1/64 and its local corner proof requires log n≥10⁷. The new 1/10 defect lemma below enlarges the defect radius, but supplies neither the missing global C nor the missing efficient corner comparison. All roots refer to log n, so even the refined values are far beyond enumeration.

Exact formulas and status: `theory/localization-diagnosis.md` (CONDITIONAL). Zero-remainder corner quadratic roots are explicitly diagnostics, not certified asymptotics or maximum thresholds.

## A1 — structure accepted; cost gate not evaluated

Executed:

```text
python topics/padua-argmax-effective-2-20261105/code/structure_probe.py
```

SHA-256: `9a4b717f36ff655b34ff2c49524fd3fefee87c54d61ed342357a73ea8cd8d48a`.
Arithmetic: exact `fractions.Fraction` group algebra modulo z^(2L)−1, with L=4 lcm(n,n+1). No floating trigonometric signs; equality is checked before absolute values.

| n | physical points | exact cardinal identities | weighted multisets | collision identities | zero cases |
|---:|---:|---:|---:|---:|---:|
| 3 | 26 | 260 | 26 | 8 | 1 |
| 4 | 36 | 540 | 36 | 8 | 1 |
| 5 | 48 | 1008 | 48 | 8 | 1 |
| 6 | 62 | 1736 | 62 | 8 | 1 |

All checks accepted. The program additionally checks G(0,0)=2n(n+1) and G(π,π)=2n(−1)^n at each degree. Physical points include both parities, all odd centers, nonzero admissible phase shifts, edges, corners and diamond-boundary ties. These are formula checks, not finite maximum certificates.

The analytic all-n result in `theory/phase-structure.md` proves exact λ=S_n−Δ for the full reflection defect, endpoint multiplicities and sufficient finite class/box predicates. Using Q_v/Q_h gives only an upper bound. The new PD-T269 signed deformation is a different quantity despite the inherited Δ notation.

**A1 structural prerequisite: PASS. A1 full cost/cover verdict: NOT EVALUATED.** At the initial checkpoint the shared safety margins and fixed scaled corner predicate were unspecified. The subsequent H3 theorem now provides an explicit physical 10⁻¹¹/n² radius; `attempts/H1.md` records a separately dated bounded float-box pilot specification. This closes the mathematical scale obligation, but not the cost/coverage test. No complete n=17–256 floating box cover or exact n=256 timing projection is claimed here. The point/projection probes elsewhere in this topic remain measurements.

## A2 — preregistered radius and analytic ingredient

Target radius for the noncorner primitive/defect comparison: **ρ₁=1/10**, the first listed A2 radius and wider than the previously measured primitive-cusp location around 0.06. This selection does not assert the far primitive comparison for ρ≥1/10; that needs its own bound. Radii 0.2 and 0.3 remain the handoff's diagnostic extensions.

Following the initial structural/gate review, the exact larger-radius theorem in `theory/defect-radius-extension.md` proves Δ≥1/8192 for n≥48, ρ≤1/10, all admissible noncorner centers. The analytic proof uses the same eight finite lines as PD-T224 with revised numerator estimates. No sample is a premise. Supplementary review and Claude audit are pending.

This is an available lower-bound ingredient, **not an A2 pass**: one must still compare it with an upper bound for S−Λ_c throughout the relevant phase set. The all-center projected sample screen and its phase/radius coverage are recorded separately. Failure of this particular sufficient budget would not constitute a counterexample to PD-T099.

## Unexecuted dependent gates

A3 depends on a predefined profile and a genuine uniform error estimate; A4 cannot turn a fitted remainder into a proved N₁. A5 cannot turn a failed primitive/defect sufficient predicate into a Lebesgue-function counterexample. This structural work supplies none of those gate conclusions and leaves PD-T099 OPEN.
