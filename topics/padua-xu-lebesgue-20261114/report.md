# Report — padua-xu-lebesgue-20261114

Orchestrator: Claude Opus 5.5. Researchers: Claude Fable 5.2 xhigh subagents, one per round. Code: Sonnet 5.5 high. Independent checks: separate Opus 5.5 instances. Rules `2d60e22`. Status vocabulary per AGENTS.md. Every PROVED item is **developer PROVED**: confirmed by an independent subagent check, with the formal audit (Opus 5.5 xhigh, distinct thread) pending.

## 1. X1: BCDMV 2006 Conjecture (17) for Xu points

**The conjecture as published** (Computing 76 (2006) p. 319, page image checked): Λ^Xu_n ≲ ((2/π) log(n+1))² as n → ∞, and the maximum is attained at the four vertices of the square. The setting is even n.

**Verdict: settled, in sharpened form** (theory/X1-01 … X1-07):
- **Λ^Xu_n = L_n² exactly for every n ≥ 1**, where L_n = (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)) is the Lebesgue constant of interpolation at the n zeros of T_n.
- **The maximizers are exactly the non-node vertices for every n ≥ 2.** For even n these are all four vertices. For odd n, a variant outside the published conjecture, they are (1,−1) and (−1,1).
- **The mechanism** is a tensor lift (X1-01). In u = (θ₁+θ₂)/2 and v = (θ₁−θ₂)/2, every Xu fundamental function is a fiber sum of products d_n(u−u_p) d_n(v−u_q) of 1-D trigonometric fundamental functions. Hence λ_n ≤ ω_n(u) ω_n(v) ≤ L_n², with equality only at the non-node vertices. No finite certificates are needed.
- **Expansion** (X1-07; N = n, valid from n₂ = 1): Λ^Xu_n = (4/π²) log² n + b log n + c + R_n, with b = (8/π²)(γ + log(8/π)) = 1.2255221257…, c = (4/π²)(γ + log(8/π))² = 0.9264501920…, and 0 < R_n < (log n + 1.55)/(18 n²). Also Λ^Xu_n ≤ ((2/π) log n + 1)². The literal inequality in (17) fails for every n, but the ratio tends to 1.
- **Relation to Padua:**
  - Λ_c^Padua(n) − Λ^Xu_n → κ (PD-T269);
  - the Xu vertex value equals PD-T159's same-mesh reference F_n, so the vertex expansion alone also follows from merged PD-T159 + PD-T270;
  - the new parts are the global identity and the argmax.
- **Novelty** (`literature-xu-mp.md` §5): no prior statement of the exact identity, the lift bound or the maximizers was found in the documented search. Precedents for the method: BdMV 2006 (a non-sharp product bound with coefficient 32/π²), Li–Sun–Xu 2009 (the lattice derivation, without Lebesgue statements), and Xu, JAT 2012 §6.2, which says the Xu-type case "cannot be deduced" from the 1-D constant. Coverage limit: the body of Xu's CUP 2025 book was not read (NTNU has no access); its chapter summaries were.
- **MEASURED** (X1-08): the runner-up is the edge midpoint, with deficit L_n² − λ_n(0,1) → ≈ 0.8913.
- **Independent check:** `independent-checks-X1.md`, own code, all records confirmed, MINOR wording fixes applied.

## 2. X2: Morrow–Patterson points (n even)

**Literature changed the target.**
- BRIEF target X2.1, Λ_MP ≥ c n², is already published: Beberok, JAT 311 (2025) 106191, Thm 0.1, with an existential c.
- BBDM, Constr. Approx. 63 (2026), §7.1, states two open problems: λ(x,y) = λ(−x,−y), and attainment at each corner. Their numerics report the corner value as (n+1)(n+2)/2.
- "MPX" variants are not defined in any source read, so target X2.3 is dropped.

**Results** (theory/X2-21 … X2-N30):
- λ_n(±1,−1) = n+1 exactly (X2-22). There is an exact closed form at (±1,1) with an explicit sign band (X2-23), and λ_n(±1,1) > n+1 (X2-24).
- **Sharp corner asymptotics** (X2-25): λ_n(1,1) = c*(n+5/2)² − (n+1) + O(log² n), with explicit two-sided bounds for every even n. Here c* = (2/π)∫₀^∞ |sin 2τ|·|d/dτ (sin τ/τ)²| dτ = 0.51695365336…, certified enclosure [0.5169536533663, 0.5169536533677].
- **Λ_n > c* n² for every even n ≥ 2** (X2-26), strengthening Beberok's existential constant; the computer-assisted part covers n ≤ 16.
- **Negative answers to BBDM §7.1, for every even n ≥ 2:**
  - λ(x,y) ≠ λ(−x,−y), and Λ_n is not attained at (±1,−1) (X2-N29);
  - no vertex value equals (n+1)(n+2)/2 (X2-N30); the ratio λ(1,1)/dim → 2c* ≈ 1.0339.
- **The argmax at (±1,1)** (X2-28) is OPEN. The G1-MP screen supports it for n ≤ 60 with a ≈ 40% margin. Round X2-3 is in progress (see §4).
- **Independent check:** `independent-checks-X2.md`, own code including ball arithmetic up to n = 60 and an independent c* integration; all records confirmed. M1 fixed: evidence committed, `evidence/mp-x2-corner-arb.json`.

## 3. Gate verdicts

Verdicts and evidence: `gates.md`.
- **G0 PASS** for both families.
- **G1:** vertex conjecture supported for n ≤ 60. MEASURED, now superseded by the X1-05 proof.
- **G1-MP:** argmax (±1,1) for n ≤ 60. MEASURED.
- **C-MP:** certified asymmetry for n ≤ 30 on two code paths.
- **G2 met (developer)** for X1 by X1-07.
- **G3 met (developer)** for X1 by an analytic all-n proof (X1-05), with onset 2 and no finite range.
- **G4** is moot as a new result (published). X2-26 is the explicit-constant strengthening.
- **G5:** respected. No constant comes from a fit, and "eventually" is kept apart from "every n".

## 4. Open

- The X2 argmax and lim Λ_MP/n² = c*: round X2-3.
- The X1-08 limit constant.
- MP for odd n, and EMP.

## 5. Is a manuscript warranted?

**X1: yes, a short paper.** "The Lebesgue constant of the Xu points" would carry the exact identity Λ = L_n², the argmax, the expansion and the resolution of Conjecture (17). It is self-contained, about 10–12 pages, and independent of the PR #27 Padua paper, which it can cite for contrast: Padua needs localization and certificates, Xu does not. A natural venue is J. Approx. Theory or Numer. Algorithms.

**X2: a separate note.** It would cover the MP corner values, the sharp constant c* at the corner, Λ > c* n², and the negative answers to BBDM §7.1. If X2-3 proves the argmax or lim Λ/n² = c*, the note gains its main theorem. A venue such as J. Approx. Theory, which published Beberok's lower bound, fits.

AC decides.
