# PR11 focused response audit: T2–T5 and König–Nielsen F3

Candidate and rules: `41bbc231be4b5ccc7c3f92e5818a53b950ccc25f`, read from the orchestrator's pinned target files on 2026-11-01. Independent Codex subagent; runtime does not separately expose model/effort. Read target AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md. No Git mutations or developer-file edits.

Scope: disposition of the first audit's translation/source findings and F3. No new mechanism or novelty clearance; parent owns the complete IDEAS/novelty review and T6. Relevant literature INDEX entries read before reopening sources. Previous evidence read: translation-source-check.md, comparison-primary-check.md and comparison-other-check.md under /workspace/pr11-audit.

**Result: no unresolved actionable finding within this assigned scope.**

| Item | Disposition | Independent check |
|---|---|---|
| T2 constants (translation.md:22) | RESOLVED | From lambda=norm^-2, c<=norm/log N<=C is exactly equivalent to C^-2<=lambda(log N)^2<=c^-2. Same-subspace and same-weight qualifications remain explicit. |
| T4 smoothing factor (lines 40–46; F1) | RESOLVED, conditional source translation | The truncated average is at most 2. Multipliers 2 C_src, (2 pi M)^2 and 2 from Delta_N<=2w give exactly 16 pi^2 M^2 C_src. The stated reciprocal lower bound follows. |
| T4 angular orientation (line 38) | RESOLVED | Absolute angular gaps repair the reversed ordering. |
| T4 choice of M and exactness (lines 42–48) | RESOLVED | Increasing M strengthens the upper-gap hypothesis. With M>=1, n<=N/(pi M)<N/2, hence deg(p^2)<=N and CC exactness gives both Gram extrema equal to 1. RELATED accurately describes this particular consequence; no beyond-exactness claim remains. |
| T5 c and endpoint condition (lines 56–63) | RESOLVED | c=N^-2 lies in the source's [0,1/2] range for N>=2. Endpoint spacings, endpoint derivative magnitudes and endpoint coefficients have the asserted orders. The fixed-sigma limitation is explicit. |
| LIT-294 exponent (additions.md:20–21; F3) | RESOLVED, primary statement checked | The primary definition of m and M=m' gives M=4(a+1)/(2a+1) for a=max(alpha,beta)>-1/2. The alpha-only proof explicitly assumes alpha>=beta. The example (0,1) gives 8/3. U-node critical p=3 and the same-weight versus mixed-weight distinction are correct. |

## Additional algebra supporting the T5 disposition

Use the ascending Lobatto order and L=1, as implicit in the displayed delta_j=t_(j+1)-t_(j-1). Write h=pi/N and u=sin(theta_j). At interior nodes delta_j=2u sin h and s=1-|cos(theta_j)|>=u^2/2, while u>=2/N. Thus

    (s+N^-2)/delta_j >= u/(4 sin h) >= 1/(2 pi).

At an endpoint delta=1-cos h<=h^2/2, so N^-2/delta>=2/pi^2. Consequently tau=1/(2 pi) works uniformly for (1.31), including N=2. Also N^-2<=u^2/4 at interior nodes, giving u^2/2<=s+N^-2<=5u^2/4; raising to any fixed admissible 2 sigma preserves comparability. The unscaled nodal polynomial has derivative magnitudes N internally and 2N at endpoints. Scaling it by a fixed normalization factor changes only absolute constants, so the second-coefficient ratio N^(2-4 sigma) at endpoints is correct.

The line-57 normalization inequality with constant 2 is valid on the actual range s+c<=5/4 (N>=2 and -1/2<sigma<1/2): sqrt(2)(s+c)^(1/2-sigma)<=sqrt(2)*5/4<2 when s+c>=1, and <=sqrt(2) otherwise. This tightens its stated coarse bound s+c<=2 without requiring a substantive change.

## Primary-source coverage and limits

- Reopened [König–Nielsen arXiv v1](https://arxiv.org/pdf/math/9208201): Theorem 1 and definitions, printed pp.3–4; alpha>=beta reduction and equations (18)–(19), p.15. The corrected finite upper endpoint and critical growth statements match. Journal version uninspected.
- Reopened [Lubinsky author manuscript](https://lubinsky.math.gatech.edu/Research%20papers/marzyg98Paper147.pdf): definitions (1.1), (1.4), (1.6), spacing (1.7), and Theorem 1.7, (1.29)–(1.32), PDF pp.6–7. The theorem permits c to vary and its constant is independent of c, consistent with c=N^-2. Text extraction has known garbled minus signs; prior audit's statement check and the surrounding formulas agree. No published-version pagination verification or full proof audit is claimed.
- Mastroianni–Totik pp.65–66 were not newly obtained. Its local implication is checked conditional on the printed source statement; the existing source-access limitation remains. No claim that this pass independently inspected the institutional PDF.

Executed: read-only cat/sed/rg/nl and sha256sum; web open/find of the two primary PDFs. No numerical rerun or computer-assisted proof is claimed. Sole created artifact is this audit note.

Target SHA-256 values:

- translation.md: `1f07addcf257f7a877977eaffde4594d532e578a38b3264edb46275ce2cdcc22`
- literature/records/mz-prior-art-2026-additions.md: `7370501b0c2cfddb26c34136f1845d82e6c20e08cb2c7bdff8d286983bde2d0d`
