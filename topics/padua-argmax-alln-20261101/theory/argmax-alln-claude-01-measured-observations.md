# PD-T?argmax-alln-claude-01 — Float64 observations on the Padua majorant and the O(1) argmax gaps

ID kind: PD-T.
Aliases: majorant excess; interior gap ≈ 1.75; O(1)-gap observation.
Split from: none (supporting evidence for the OPEN target PD-T099).
Split into: none.

## Statement

In the float64 runs listed under Checks (n as stated, Padua conventions of PD-T101), the following were observed.

1. **Kernel check.** The reflected-lattice evaluation of λ_n in `code/maj.py` agrees with direct Vandermonde inversion at the points tested for n = 3, 4, to the 6 printed digits. That evaluation uses G_n with coefficients c_ab = h_a h_b for a+b ≤ n, except c_{n,0} = 1.
2. **Majorant excess.** Let S(t) = |Λ|⁻¹ Σ_λ |G_n(t+λ)| (equivalently Σ_B w_B ¼ Σ_σ |G_n(…)|). Its maximum over one fundamental cell, found by grid search and Nelder–Mead, exceeds S(coset) = Λ_c(n). The excess is 1.37e-3, 1.19e-3, 1.29e-3, 1.07e-3, 9.79e-4, 8.27e-4, 7.38e-4, 6.38e-4, 5.02e-4, 3.67e-4, 2.34e-4, 1.20e-4 and 9.22e-5 for n = 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 40. The maximiser lies within about 0.02·π/n of a coset point.
3. **Interior gap.** Λ_c(n) minus the maximum of λ_n over the central angle box [π/4, 3π/4]² (grid with about 6 points per π/n, then Nelder–Mead) is 1.7947, 1.8724, 1.8436, 1.7873, 1.7487 and 1.7479 for n = 8, 12, 16, 24, 32, 48.
4. **Coarse grid.** On the 161×161 angle grid the maximum of λ_n equals Λ_c(n) for n = 3, 4, 5, 6, 8, 12, 16, 24. This adds nothing to part 2's certified results for n ≤ 7 and is not a certificate for larger n.

No asymptotic rate, limit or universal statement is claimed.

## Definitions

Λ, G_n and the reflected-lattice identity (R) are as in [plan.md](../plan.md) §1. λ_n is the Padua Lebesgue function and Λ_c(n) its corner value (PD-T101). "Coset point" means a torus point (jπ/n, kπ/(n+1)) with j+k odd; the non-node corners belong to this class.

## Assumptions

Float64 NumPy linear algebra and SciPy Nelder–Mead. Identity (R) is used as an evaluation formula. Its proof as a lemma is still to be written, and it was checked only numerically at n = 3, 4 against Vandermonde inversion.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| 1 kernel agreement | MEASURED | outputs/check.out |
| 2 majorant excess | MEASURED | outputs/cell.out; local optimiser, no enclosure |
| 3 interior gap | MEASURED | outputs/interior.out; maximum over a box found by grid + local search, not certified |
| 4 coarse grid | MEASURED | outputs/maj.out |

Candidate disposition: part 2 is the evidence for IDEA?argmax-alln-claude-01, REJECTED: failed, MEASURED scope ([ideas.md](../ideas.md)).

## Depends on

PD-T101 (corner formula, used for the meaning of Λ_c). Nothing is used as a proof dependency.

## Checks

The commands were run from `topics/padua-argmax-alln-20261101/code/` with Python 3.13.18, NumPy 2.5.3 and SciPy 1.18.1 (outputs/environment.txt):

```text
python3 check.py > ../outputs/check.out
python3 cell.py 3 4 5 6 7 8 9 10 12 15 20 30 40 > ../outputs/cell.out
python3 interior.py 8 12 16 24 32 48 > ../outputs/interior.out
python3 maj.py 3 4 5 6 8 12 16 24 > ../outputs/maj.out
```

These were developer runs. The independent rerun is listed under Runs needed in the LOG.

## Sources

None beyond PD-T101 and the OPEN_TARGETS conventions.

## Proof or evidence

Evidence only: the committed outputs above.

## Scope and open items

These are float64 observations without enclosures. Part 2 would be refuted by an enclosure showing max S = S(coset). A certified version (interval maximisation of S on a cell) would turn part 2 into a scoped PD-N against IDEA?argmax-alln-claude-01. Part 3 indicates, but does not establish, that the deep-interior gap is O(1) rather than growing like log n.

## History

2026-11-01, Claude (claude-opus-5-5): created from chat exploration at AC's request; scripts rerun to capture the outputs committed here.
