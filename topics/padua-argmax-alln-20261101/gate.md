# Novelty gate — padua-argmax-alln-20261101

Claude (claude-opus-5-5), 2026-11-01, rules read at `28aaa20861d08074b77efc74eaef75cdcb36234d` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md).

## Scan performed (relaxed start-of-topic gate)

- `grep -niE '^#{2,4} |alias' state/IDEAS.md`: 198 heading/alias lines read.
- Mechanism keywords searched in `state/IDEAS.md`: `argmax|majorant|brutman|profile|lattice sum|shifted|anti-node|corner|edge gap|generating curve|monoton`.
- Also searched: programme-ideas topic files (proposal-1, adversarial-gen4-2), for `majorant|reflected|shift-sum|Brutman`.
- Obstruction and disposition tables read: the programme-ideas table, the MZ 2D (PR14) rows near IDEA-213…222, and the PD-N rows for PD-N046/048/052.

## Closest entries

- **IDEA-206 / IDEA?programme-ideas-claude-17**: Lebesgue theory of checkerboard (Padua-type) interpolation, proposal-1. It owns the A4 target (PD-T099), the corner expansion (PD-T098) and the counts (PD-T100). This topic is a proof strategy for its OPEN argmax target, not a new programme.
- **IDEA-048**: geometry of the Padua Lebesgue function, interior maxima (contextual; Białas-Cież–De Marchi–Suder arXiv 2605.23299).
- **IDEA-047**: Morrow–Patterson Lebesgue order. Different node family, not applicable.
- **PD-N046/052 and IDEA-213/222**: these majorants concern MZ Gram and hyperinterpolation quantities, not λ_n. They are a different object, but a reminder that pointwise majorants can fail by small margins.
- Part 2 (unmerged, pinned `b5bba7c`): records 70–73 (exact edge kernel, edge gaps) and records 01–04 (A2). Strategy (A)–(C) reuses them.

## Verdicts

| Candidate | Verdict | Difference from the closest entry |
|---|---|---|
| IDEA?argmax-alln-claude-01: shifted-lattice majorant maximal at the coset | variant of IDEA-206 | New mechanism for PD-T099; MEASURED failure as stated (max off-coset by ≤1.4e-3) |
| IDEA?argmax-alln-claude-02: scaled local profiles + n-independent cell certificates + finite certifier | variant of IDEA-206 | Uniform O(1) profile asymptotics in every regime, not only at the corner (PD-T098 / A2) |
| IDEA?argmax-alln-claude-03: Brutman-type monotone decrease of cell maxima toward the corner | new within this search | Exact all-n comparison; untested |
| IDEA?argmax-alln-claude-04: generating-curve numerator factorisation | new within this search | 2D analogue of the 1D common-factor trick; untested |

Cheapest decisive tests and kill criteria are in [plan.md](plan.md) §5 and [ideas.md](ideas.md). No literature priority claim is made. Literature on the 1D analogues has not been read yet (plan §5.4).

## Gate refresh — 2026-11-01, handoff 01 (main `2b52b43`)

- Rules unchanged since `28aaa20` (`git diff --stat 28aaa20 2b52b43 -- AGENTS.md agents/ templates/` is empty).
- Registry grown to 701 non-empty lines. Rescanned headings and alias lines and the PR12 addenda (IDEA-286…311, PD-N072/073 obstruction table).
- Keyword search repeated: `triangle defect|phase locali|primitive|central envelope|R_cen|argmax|majorant|monoton|profile`.
- New closest entries:
  - **IDEA-305** (uniform phase/gain/defect assembly for the central envelope; PD-T189–192);
  - **IDEA-303/304** (all-edge kernel, complementary-grid defect, constant g);
  - **IDEA-290…302** (finite complete certification), with **IDEA-299** (n = 8 cover) deferred.
- Verdicts, also recorded in ideas.md:

| Candidate | Verdict | Difference |
|---|---|---|
| IDEA?argmax-alln-claude-01 | unchanged (REJECTED: failed, MEASURED; sub-tool) | consistent with PD-T190 |
| IDEA?argmax-alln-claude-02 | variant of IDEA-305 | all regimes + effective n₀ (plan v2 P1–P6) |
| IDEA?argmax-alln-claude-03 | new within search (unchanged) | the edge profile is compatible; untested |
| IDEA?argmax-alln-claude-04 | new within search (unchanged) | untested |
| IDEA?argmax-alln-claude-05 (new) | variant of IDEA-290…302 | global maximum only, no counting |

- No literature claim. The 1-D Lebesgue-function literature (plan v1 §5.4) is still unread and is assigned to part 3 before P3.

## Part3 scope refresh — 2026-11-01, Codex

This step develops the already gated candidates, with no priority or new-programme claim. The edge worker scanned complete registry headings/aliases and obstruction/disposition tables and read full shortlists IDEA206/303–305 plus their linked PD-T185–192 proofs. Finite work read IDEA290–302 and the exact degree-specific field/certificate dependencies. The supplementary Astra mathematical reviewer read the complete state/IDEAS.md and the relevant source proofs.

The tensor Bernstein bound/corner certificate is retained as a sufficient global-max-only variant under Claude-05, distinct from completeness/counting machinery. The newly precise O-L/O-Lt/O-R/E-C formulations are separately retained in ideas-codex-fallback.md; N01 refutes only O-Lt, with the post-inspection origin disclosed. No ambiguous pairing suggestion is declared refuted. T2/T3 planning failures remain measured and do not reject the original argmax target.

No 1-D literature theorem was transferred, and the missing source reading remains a prerequisite for such a transfer. Exact finite algebra and extension of the already local edge proof use only explicitly cited accepted local dependencies. Final dispositions and scope are in report.md; required independent Claude audit remains pending.
