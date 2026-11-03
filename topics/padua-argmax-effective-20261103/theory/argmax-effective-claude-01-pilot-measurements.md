# PD-T?argmax-effective-claude-01 — Pilot gate measurements for the effective Padua argmax

ID kind: PD-T.
Aliases: pilot G0–G3; true local corner constant; true global primitive constant; certifier timings n = 17–32.
Split from: none (supporting evidence for the OPEN target PD-T099).
Split into: none.

## Statement

In the runs listed under Checks (Padua conventions of PD-T101; corner c = (−1,−1), inward phases z_n(α,β) = (−cos(α/n), −cos(β/m)), m = n+1, a = ½(cos α + cos β), ρ = α+β), the following were observed.

1. **G2, local corner constant.** K(n) := max over the sampled α, β ≥ 0 with ρ ∈ {1/64, 1/256, 1/1024} (21 directions each) of (λ_n(z_n) − aΛ_c)/(ρ² log(n+1)).
   - K = 0.2893, 0.2775, 0.2593, 0.2464 and 0.2367 at n = 17, 24, 48, 96, 192, attained on the axis β = 0 and essentially constant in ρ.
   - The axis budget Λ_c/(4 log(n+1)) is 0.745, 0.767, 0.815, 0.869 and 0.926. On the diagonal both K and the budget halve (K ≈ 0.14, 0.14, 0.13, 0.12, 0.12).
   - (λ_n − Λ_c)/ρ² on the axis is −1.318, −1.575, −2.163, −2.847 and −3.629.
2. **G3, global primitive constant and far-coset margin.** On a 61×61 grid of phases (α,β) ∈ [−π,π]² with |α|+|β| ≤ π, with S_n evaluated at the torus point (π + α/n, π + β/m):
   - sup (S_n − aΛ_c)/log(n+1) = 1.5937, 1.5172, 1.4822 at n = 17, 48, 96, attained at (α,β) = (π/2, −π/2);
   - sup over grid points with |α|+|β| ≥ 1/2 of S_n − Λ_c = −0.147, −0.253, −0.340;
   - the grid maximum of S_n − Λ_c is 0, at (0,0).
3. **G0/G1, certifier timings.** The unchanged PD-T210 producer `finite_general_run.py` (source hashes below; default precision 192, depth 48) produced complete closed-square covers:

   | n | Leaves (bound + corner) | Max depth | Producer time | Checker |
   |---|---|---|---|---|
   | 17 | 106 (104 + 2) | 8 | 35.0 s | `finite_general_check.py` accepted = true, complete partition, 32.4 s |
   | 20 | 132 (130 + 2) | 10 | 87.0 s | not run |
   | 24 | 154 (152 + 2) | 10 | 229.6 s | not run |
   | 32 | PENDING | PENDING | PENDING | not run |

   The fitted cost exponent between n = 17 and 24 is about 5.5 (single process, shared container).

No degree is certified by this record. Producer and checker were run by the same agent (Claude), and there has been no independent replay. Under AGENTS.md these are MEASURED runs only.

## Definitions

λ_n, S_n and Λ_c(n) are as in PD-T101, PD-T215 and PD-T216. The float evaluator is `topics/padua-argmax-alln-20261101/code/maj.py` (the PD-T206 evaluator, checked against Vandermonde inversion at n = 3, 4).

## Assumptions

Parts 1–2 use float64 NumPy and finite grids; no enclosures, and maxima over a grid are not suprema. Part 3 uses the producer's own exact or outward arithmetic; only the timing and leaf counts are reported here.

## Status by part

Overall status: **MEASURED**.

| Part | Status | Evidence / remaining gap |
|---|---|---|
| 1 G2 | MEASURED | outputs/g2_pilot.out |
| 2 G3 | MEASURED | outputs/g3_pilot.out |
| 3 G0/G1 timings | MEASURED | outputs/certifier_pilot.md (summary); certificates regenerable, not committed. Certifying these degrees needs an independent replay |

## Depends on

PD-T101 (kernel), PD-T210 (certificate theorem; used only to describe what the producer computes), and the PD-T206 evaluator.

## Checks

From `topics/padua-argmax-effective-20261103/code/`:

```text
python3 g2_pilot.py 17 24 48 96 192 > ../outputs/g2_pilot.out
python3 g3_pilot.py 17 48 96 > ../outputs/g3_pilot.out
```

From `topics/padua-argmax-alln-20261101/code/part3/` (main `440d107`):

```text
python3 finite_general_run.py --n N --seconds 1500 --output <scratch>/nN.json.gz    # N = 17, 20, 24, 32
python3 finite_general_check.py <scratch>/n17.json.gz --output <scratch>/n17.check.json
```

Source SHA-256 values:
- finite_general_run.py `fe1647086b2db5c47d75e24d386cc6456782bb6ea36bc25acd39b75bd4752511`
- finite_general.py `b20b7f88ddfc0bbc92e68096063ef626664028c2a379c34d16dc9f84e17aa74a`
- finite_bernstein.py `a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f`
- finite_general_check.py `d2edd6bc5c1ef1193ad44a8fb5decd859e92d960717e1a696743e43c77f337cb`

The certificate's internal `source_head` field is the module's pinned constant `328be35…`, not the run checkout. The n = 17 certificate has SHA-256 `2f07c8668960957615297bb09e7c05f7771b49270348b3d54497c9d7061d6c08` (3760 bytes).

Environment: Python 3.13, NumPy 2.5.3, SciPy 1.18.1 (as in PD-T206's environment file).

## Sources

None.

## Scope and open items

These are planning measurements for handoff 01's gates. G0 certification of n = 17–24 requires an independent replay by a different agent. Rigorous versions of K(n) and C(n) are the targets of routes R1/R2/R6.

## History

2026-11-03, Claude (claude-opus-5-5): created at campaign setup.
