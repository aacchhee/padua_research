# Common instructions for generator agents (Step 2)

Effort: xhigh. Read, in this order: /home/claude/inputs/CAMPAIGN_CONTEXT.md, /home/claude/padua_research/topics/programme-ideas-20261031/brief.md, /home/claude/padua_research/templates/IDEA.md. Then read the two shorter reports in /home/claude/inputs/padua/reports/ ("Round 3 ..." and "Open problems verification") in full, and RESULTS.md. Consult the long report, research_notes, the parallel-branch IDEAS.md files (/home/claude/inputs/branches/*/state/IDEAS.md — scan all headings and alias lines) and the PDFs when a candidate touches them. Web search is allowed and encouraged for checking whether a template theory already has a bivariate version or whether a group owns it; record query, date (2026-10-31) and result.

You own exactly one angle. Stay out of the other three angles (they are run by sibling agents) and out of every exclusion in CAMPAIGN_CONTEXT.md. If a candidate idea straddles angles, keep it only if its central question is squarely in your angle; otherwise note it in one line in your final reply as "handed to angle X" and do not write a draft for it.

## Output

Write every candidate to /home/claude/padua_research/topics/programme-ideas-20261031/checks/state/gen<i>-draft-<n>.md THE MOMENT IT IS FORMED (before refining it), where <i> is your angle letter's number (A=1, B=2, C=3, D=4) and <n> counts from 1. A rejected or weak idea is still written (then marked so at the bottom). Return 2–4 candidates in your final reply, but keep every draft file, including the ones you decide not to return.

Each draft file has these sections, in this order, with these exact headers:

```
# <Working title>
Model: claude-fable-5-1, effort xhigh · Angle <letter> · 2026-10-31 · Status: <returned | not returned (reason)>

## Central question
<one sentence; must be an open question>

## Template theory
<the mature 1D/classical theory that is missing in the bivariate/structured setting; name its key theorems and what a bivariate version would have to deliver>

## Sub-problems (≥3, each with a separate payoff)
| # | Sub-problem | Kind (theory / algorithms / exact arithmetic / numerics-software) | Payoff (what paper) |

## Entry points and cheap decisive tests
<at least two: each n ≤ 6–8 or a seconds-long script, with the exact quantity to compute and the pre-written kill criterion>

## Plausible first paper (≈6 months)
<title-level statement, what it would contain, why it is reachable>

## Closest prior work
<named papers/groups with years; what they did; what they did NOT do. Mark anything from memory as UNVERIFIED and anything web-checked with the query and date>

## Why it is not an exclusion
<go through (a)–(d) and the "already judged" list; say which item is nearest and the mechanism/property that separates this candidate from it; state the observation that would collapse the separation>

## Fit with AC's expertise and 2–5-year horizon
<escalating questions, in order>

## Risks and obstructions
<which recorded obstruction (brief §3) is nearest, with its exact hypothesis, and why this candidate escapes or does not>

## IDEA-template record
<fill /home/claude/padua_research/templates/IDEA.md fields, provisional label IDEA?programme-ideas-claude-<i>-<n>; leave "Actual test results" empty; Disposition: pending gate>
```

## Quality bar

- Programme-scale: each candidate must carry at least three papers and a 2–5-year escalation path. A single theorem or a single algorithm is a note, not a programme: do not return it (you may still write the draft file and mark it "not returned (note-sized)").
- Honest ownership check: if you suspect a group already runs this programme, say so with names/years and still write the draft; the gate and adversarial steps decide.
- No renaming: a known mechanism with new notation is not new. The separation criterion must be a mathematical property, assumption, invariant, domain or proof step.
- No fulltext quotes from PDFs or from bttb-research; locators and IDs only.

## Final reply

List your returned candidates (file names, titles, central questions, one-line separation from the nearest exclusion), then the not-returned drafts with reasons, then "handed to angle X" items, then the web searches you ran (query, date, outcome).
