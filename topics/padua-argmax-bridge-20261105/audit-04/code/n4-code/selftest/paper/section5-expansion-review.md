# Section 5 expansion review

Status: **ACCEPT for the final Section 5 expansion**, 7 November 2026.
No unresolved finding within the scope below.

Auditor: distinct Codex review agent, requested Sol, max effort, under
AC's explicit continuing model preference. Actual serving-model metadata
is not independently exposed. Rules read at
`2245e6d9317b53a38976d6f9d6a304ea8fd15c0d`: `AGENTS.md`,
`agents/WORKFLOW.md`, and `agents/codex/CODEX.md`; their bytes match the
previously fully read rules. The orchestrator controls Git. This reviewer
owns only this report and made no manuscript, code, evidence or Git
mutation. No native job or independent manuscript build was run.

## Reviewed scope and outcome

Reviewed the complete Section 5 diff from
`2245e6d9317b53a38976d6f9d6a304ea8fd15c0d` to
`177be83bcb03204ae30c74355ad387ac52f42cb5`, including the entire expanded
section and its mathematical context. The initial substantive candidate
was `b22d98b62e4f0e7e13676bab846677681788a726`; the final intervening diff
contains only the announced wording and spacing improvements.

The expansion supplies useful derivations: the signed-sum identity,
two-coordinate interpolation error, strict Bernstein corner loss, complete
closed partition, true-norm absorption, quarter-grid allowance, rational
near/far proxies, normalized corner-loss algebra and final chart assembly.
These additions make the certificate implication easier to reconstruct.
They preserve the common small-degree scheme and the previously accepted
mathematical and computational premises.

The orchestrator's final built artifact has **48 total pages**, against
the accepted 46-page baseline. Section 5 occupies printed pages **42--46**,
with its evidence subsection beginning on 46; references begin on 47.
The requested approximately two-page expansion is therefore realized in
the compiled article. Class, layout, fonts, other active TeX sources and
bibliography are unchanged.

This is expansion of existing proof exposition, with no new mechanism,
degree result, novelty/priority assertion or computation. The full IDEAS
novelty gate does not apply. New displayed derivations were reconstructed
within this focused review; earlier unrelated mathematics was not reopened.

## Mathematical and fidelity checks

No BLOCKING, MAJOR or MINOR finding remains. This auditor made no
manuscript fix.

1. **Signed sums and positive interpolation.** The finite identity
   `sum |h_l| = max_epsilon sum epsilon_l h_l` is exact, including zero
   components and changing maximizing signs. Each complete signed sum
   stays smooth. The added decomposition
   `f - I_a I_b f = (f - I_a f) + I_a(f - I_b f)` correctly gives the
   two Peano terms: positivity transfers the second-coordinate bound and
   the vertex bounds. The common error bound is independent of the sign
   vector, so the subsequent maximum is valid.

2. **Strict Bernstein corner comparison.** On a designated corner leaf,
   the true exceptional coefficient sum is the exact corner value `C`.
   All other sums are bounded by `D_R < L_c <= C`. Hence the upper bound
   `C - (C-D_R)(1-w_*)` is strictly below `C` whenever `w_* < 1`.
   The endpoint tensor Bernstein weight equals one precisely at its own
   vertex. This proves strictness arbitrarily close to the corner and
   allows its exact value at the corner. Ordinary leaves and the complete
   closed midpoint tree give the asserted global equality classification,
   including shared boundaries. The two designated vertices and their
   parity-preserving reflection are unchanged.

3. **Phase derivatives and norm certification.** The normalized signed
   board definition matches the corrected finite kernel. Its frequency
   bounds in `(a,b)` are `pi` and `pi*k`, yielding the displayed second
   derivative bounds. The full-leaf allowance retains
   `theta_R = pi^2(width_a^2 + k^2 width_b^2)/8`. Folding and compactness
   first establish a finite true global norm `M_*`; the tree argument
   then absorbs `theta_R*M_*` at a leaf containing a maximizer. Thus the
   numerical norm does not enter its own proof as an assumed estimate.

4. **Grid alternative.** The ten quarter-squares cover the closed
   triangle. Every outside vertex folds into the stated set `E` under
   the established phase symmetry. Their error is
   `pi^2(1+k^2)M_*/128 <= pi^2 M_*/64`, giving the retained absorption
   factor and rational bound `784/663`. A tree containing an analytic
   far leaf is explicitly required to use this independent grid norm.
   Every triangle-meeting leaf in the wholly numerical tree construction
   must supply its numerical vertex bounds.

5. **Closed proxies and physical defect radius.** For the positive
   bracket `p_- <= pi <= p_+`, the new near proxy
   `a+b <= 1/(2p_-)` contains every actual near point; the far proxy
   `a+b >= 1/(2p_+)` contains every actual far point. They overlap at
   the true cut. Strict comparisons on these enclosing sets are
   sufficient. The defect floor is invoked only for an actual near
   point at a noncorner center. Its radius
   `min(1/2,p_+(a_1+b_1))` is a valid outward bound on that point's
   radius and matches the retained checker's rule. The selected-pair
   floors supply every finite tier from degree 41. Tangencies, closed
   seams, eligible projections and direct corner witnesses are retained.

6. **Corner-loss scaling.** The three validated losses are at least
   `q*u'`, `q*v'`, and `q*(u'+v')`. Since
   `U=pi^2*u'` and `V=pi^2*v'`, choosing `c=q/pi^2` in the existing
   squared-variable Peano bound gives exactly

   `g = q - (M*pi^4/6)*max(u',k^4*v')`

   and loss coefficient `g/(2*pi^2)` multiplying `A^2+B^2`.
   Both factors of `pi^2` and the factor two are correct. The stated
   rectangle has endpoints `pi/4` and `3pi/16`, so it contains the inward
   half diamond. Complete signed cardinal sums have the required separate
   evenness, bandwidths `1,k`, and global bound supplied through
   `lambda_n <= S_n`. The strict test `g>0` therefore proves the claimed
   punctured-corner descent, and parity reflection transfers the witness.

7. **Final coverage and evidence scope.** The degree-256 analytic corner
   implication and degree-192 far implication retain their complete
   closed guards and strictness. In particular, an analytic far leaf
   requires its entire triangle intersection to satisfy `rho >= pi/2`.
   The final odd-chart argument applies the appropriate near, far or
   actual-corner comparison and keeps every chart tie and subdivision
   boundary. Finite degrees `2..319` and the analytic tail from 320
   remain consecutive. The degree-one affine explanation remains separate
   from the unchanged executable's degree range.

The evidence paragraph retains the same 280 primary/fresh pairs, 560
essential reconstructions, trusted arithmetic/compiler/native components
and selective retention. Complete histories at 199 and 238 are described
as inspected, with fresh native verification at both degrees and distinct
review. The exact new small-degree inventory remains in its companion
record: fresh independent `2..16` verification and reused `17..40`
acceptance. No broader native execution, history retention or public release
is asserted by the expansion.

The exposition adds proof detail without recreating the historical
certifier atlas or defensive nonclaims. Its extra space is used for
mathematical implications that a reader can check directly.

## Inputs and checks actually performed

Read the preceding accepted
[consolidation audit](consolidation-audit.md) and
[affirmative prose review](affirmative-style-review.md), and the complete
[small-degree unification note](small-degree-unification.md). Mathematical
cross-checks used the current localization definitions/squared-variable
descent and the relevant parts of:

- [PD-T210 Bernstein certificate correctness](../../padua-argmax-alln-20261101/theory/argmax-alln-codex-03-finite-certificate-correctness.md),
  including the strict corner-weight proof and outward general constructor;
- [D08 positive/squared-phase interpolation](../theory/D08-point-box.md);
- [D14 grid norm](../theory/D14-grid-norm.md);
- [D10 cover contract](../theory/D10-cover-contract.md), particularly closed
  proxies and the normalized three-point corner premise;
- the actual norm, floor, corner, closed leaf and analytic-far predicates
  in [the retained checker](../code/final_hybrid_engine/checker.py).

Executed read-only `git show`, complete and bounded `git diff`/file reads,
source inventories, Python byte/hash/reference checks, `git diff --check`,
`pdfinfo` and `pdftotext -layout` inspection of the orchestrator's artifact.
In particular:

- All eight original Section 5 display blocks remain byte-identical and
  in order; seven displayed derivations were added, for fifteen total.
  The original positive-interpolation lemma statement is unchanged.
- The other six active TeX sources and bibliography are byte-identical
  to the baseline. No result-bearing code, input or evidence file changed
  in the reviewed commit range.
- All 113 labels remain distinct, all reference targets exist, the
  thirteen-key citation set is unchanged, and whitespace checking passed.
- The existing build log contains no LaTeX/package warning, error,
  undefined reference/citation, multiply defined label or overfull box.
  Underfull-box diagnostics remain. This was inspection of the completed
  build, not a separate compilation or native replay.

## Final identities and limits

Final source commit:
`177be83bcb03204ae30c74355ad387ac52f42cb5`.
`sections/certification-unified.tex`: **13274 bytes**, SHA-256
`80c4e3e764e559d596d38ae5ee40702fd3ce9ba54ea1dbe43eb5c234d6ee6eea`.
Its working bytes matched the frozen commit after the review.

Observed off-Git `local-output/padua-argmax-bridge-20261105/paper/main.pdf`:
**640116 bytes**, SHA-256
`07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0`.
The timestamped copy `padua-manuscript-20261107-212439-Oslo.pdf` in the
same directory has identical bytes. The corresponding `main.log` is
**40188 bytes**, SHA-256
`d6f6368c95dae73bd3f605dd3a2e78da3320b71605b66cd63e75cefc3494d0a8`.

This verdict accepts the expanded explanation and its derivations under
the established computational premises. The previous reviews' separate
whole-batch audit, native, priority, human-review and publication-release
boundaries remain in force.
