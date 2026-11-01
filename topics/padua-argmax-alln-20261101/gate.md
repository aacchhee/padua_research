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
