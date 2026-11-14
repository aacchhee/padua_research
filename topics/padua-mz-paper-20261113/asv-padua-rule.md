# Which Padua rule do An–Sommariva–Vianello (LIT-045) use? — source identification, 2026-11-14

Reader: Claude, claude-opus-5-5 (orchestrator). This answers the open item in report §5 on the ASV Padua rule and its page locator. It is a source identification only: **no manuscript text was changed**. Whether to drop the conditional in MZ-SP §8.1 is AC's choice (see the end).

## Published paper (LIT-045, MCS 252 (2027) 733–745)

The PDF is AC's copy in `Downloads\padua\papers`. The text was read in this session, not committed.
- **§3.2 "The square", p. 738.** The MZ constants are computed for rules on [−1,1]² with respect to Lebesgue measure. Among the alternative rules is the one "based on Padua points [18]", where [18] is the Padua2DM paper (Caliari–De Marchi–Sommariva–Vianello, Numer. Algorithms 56 (2011) 45–60). The observation is η < 1 up to n = m−1 for Padua points based cubature, for m = 1,…,20, with cond₂(G) < 10 for n < m.
- **Fig. 14, p. 743.** "Padua-points rule with ADE = 15" uses 136 = 16·17/2 nodes.
- **No weight formula or sign statement.** The paper does not define the rule beyond the citation, and gives no formula or sign statement for its weights.
- **Software.** The paper's software reference is [13]: A. Sommariva, *Matlab software for evaluating Marcinkiewicz–Zygmund constants*, https://github.com/alvisesommariva/MZ.

## The authors' code

- **Source.** https://github.com/alvisesommariva/MZ, commit `40fe3cd90c38f7e1e6a480c9c8e63f31595f4097` (2025-12-28). It ships `MZ_GENERAL_281225_COMPACT.zip`, SHA-256 `3143e3b2…f557`.
- **The demo.** `demo_MZ_square.m` (SHA-256 `888de608…cbfe9fcb`), case 2 "Cubature based on Padua Points", calls `cub_square_padua(deg,[-1 1 -1 1])` with `deg` = ADE.
- **`cub_square_padua.m`** (SHA-256 `cf852092…dc521`) is Padua2DM's `pdcub`, modified 2025-11-04, GPL-2.0-or-later.
  - **Nodes:** `pdpts(n)` gives (cos(jπ/n), cos(kπ/(n+1))), 0 ≤ j ≤ n, 0 ≤ k ≤ n+1, with **j+k odd**.
  - **Weights:** `pdwtsMM(n)` builds them from Chebyshev moments truncated to total degree ≤ n, with Padua2DM's halving of the last mode. This is cubature of the Padua interpolant.
- **Not committed:** the third-party code itself, under the repository's external-code policy.

## Check (float64; a numerical identification, not a certificate)

`pdpts` and `pdwtsMM` were ported to NumPy line by line, following MATLAB's column-major `find` and `(:)` ordering. The port is kept out of Git because it is a derivative of GPL code; its SHA-256 is `c0009795…a1f8`. Results for m = 10, 11 and 20:

- **Size:** the rule has (m+1)(m+2)/2 nodes and total weight 4.
- **Exactness:** it integrates every T_a(x)T_b(y) with a+b ≤ m exactly, with maximum error 2.5e−15.
- **Weights:** exactly two of them are negative.

The nodes are unisolvent for P_m, so a rule on them that is exact on P_m is unique. ASV's Padua rule is therefore the **interpolatory rule for Lebesgue measure on the Padua family with j+k odd**.

**Relation to MZ-SP.** MZ-SP's `eq:padua` uses j+k even. The reflection y ↦ −y (m even) or x ↦ −x (m odd) maps one family onto the other. Lebesgue measure and P_n are invariant under these reflections, so the two Gram matrices are orthogonally similar, and λ±, η and cond₂ coincide.

**Numerical confirmation.** The Gram spectra of the ported rule on P_{m−1}, in a Legendre-orthonormal basis, are:
- m = 10: λ₋ = 0.3561913826298, λ₊ = 1.6348566147838;
- m = 20: λ₋ = 0.2722330049581, λ₊ = 1.7233137316698.

These agree to about 1e−14 with the repository's own float reproduction of G^P_{m,m−1} (`reproduce.py --suite padua`).

## Consequence and suggested wording (for AC)

ASV's observation concerns the same spectra as MZ-SP's Q^P_m, so the certified brackets of Prop 8.1 certify it at m = 10 and 20, and the conditional "If that rule is the interpolatory rule studied here, …" (MZ-SP §8.1) could become definite. The identification rests on the authors' **published code**, not on the paper's text, so a definite sentence should cite the software. A possible replacement:

> An, Sommariva and Vianello \cite{ASV27} report $\eta<1$ up to $n=m-1$ for the Padua-points cubature rule for Lebesgue measure with degree of exactness $m\le20$ (\cite[§3.2]{ASV27}). In their published code this is the interpolatory rule on the reflected Padua family, so its Gram spectra are those of $Q^{\mathrm P}_m$; the brackets certify their observation at $m=10,20$ and extend it to $m=30,40,60,80$.

This would need a bibliography entry for the software and AC's agreement, and it is a manuscript wording change. The current conditional is correct as it stands.
