# PD-T?padua-3d-20261106-codex-D4-minima — packing-free n4..7 determinant minima

ID kind: PD-T. Aliases: C4 restart; R08 dependency removal n4..7.
Split from: R08-minima, its n4..7 cases with the same exact statement.
Split into: none. Original R08-minima wording/status is preserved in its
canonical file; the orchestrator owns any application of this split.

## Statement and definitions

Among all full-rank sublattices L⊂Z³ with shortest nonzero l1 norm≥2n,
the following are the exact determinant minima, with the stated counts of
row-HNF minimizers. Folding at a determinant minimum is a separate column,
not a global folded or full-rank minimum.

| n | elementary cutoff | minimum determinant | HNF minimizers | fold of each minimizer |
|---:|---:|---:|---:|---:|
|4|88|92|24|47|
|5|170|178|24|90|
|6|292|304|8|153|
|7|462|486|24|244|

## Status by part

Overall status: **PROVED**, computer-assisted finite result, with no
LITERATURE dependency. Analytic cutoff: [double-Lee bound](double-lee-bound.md).
Exact finite reduction: existing audited R08 HNF reduction. The producer
and independently written audit04 enumerator both actually ran on the
whole cutoff-to-minimum windows and produced identical per-q counts and
complete minimizer HNF sets. A single developer executing both is not
itself a distinct-agent independent audit. Historical Claude audit04 A1
also executed its own enumerator from q=1 through the minima, strictly
containing all these windows. The current focused final audit is pending.

## Depends on

The local [R08 reduction](../theory/r08-lattice-reduction.md), which proves
uniqueness/completeness of upper row HNF and exact short-vector tests;
local double-Lee injectivity. No18/19 density statement or other external
lower cutoff. The known witness determinant is only a finite upper search
endpoint, not assumed optimal. No catalogue optimality label is used.

## Executed checks and evidence

Preregistered at the orchestrator's pushed9cf64ef before run GO; rules
04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b. Command:

```
python topics/padua-3d-20261106/code/fd4_lee.py --scratch /tmp/padua-fd4-lee-r1 --output topics/padua-3d-20261106/evidence/fd4-lee.json
```

[fd4-lee.json](../evidence/fd4-lee.json) retains every per-q mathematical
HNF/admissible count, every minimizer HNF, exact fold histograms, code and
binary identities, actual command, scratch output identity and time. Code
fd4_lee.py SHA256acc2328ddafeec1cc90c76e0f97ffb7257f1f5dfa74282076f8a34eaa0f2b69e.
Unpruned HNF counts in the four windows:86622,526403,2298312,11384989.
All determinants before the last have zero admissible lattices. The final
determinant is searched completely, including every minimizer.
Producer times0.0044/0.0155/0.0733/0.5067s; independent-code times
0.0047/0.0184/0.0736/0.5607s, measured on this machine under concurrent
work. Neither cap120 was approached. Scratch is regenerate-only; its
small essential mathematical output is committed in the receipt.

## Sources, limits and open items

[Audit04 A1](../audit-04/A1.md), N1: independent from-q1 coverage already
suggested this dependency removal. The new anticode proof and direct
restart make that conclusion inspectable without trusting an imported
packing theorem. No claim is made here above n7, or about global folded
minima, determining rank, phases, weights or non-lattice sets. Optional
unreplicated audit04 N3 probes are not promoted or silently added to D4.

## History

2026-11-12, Codex assigned gpt-6.1-sol high; runtime identifier unexposed.
D4 round1 of maximum2; completed this exact restart. R08 n4..16 was
previously PROVED with explicit LITERATURE dependency. This split removes
that dependency only for n4..7, with identical statements/numerical values.
