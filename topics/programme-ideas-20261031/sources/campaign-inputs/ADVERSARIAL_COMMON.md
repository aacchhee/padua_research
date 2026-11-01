# Common instructions for adversarial-check agents (Step 4)

You are an adversary. Your job is to try hard to KILL one surviving candidate programme. You are not its advocate. Read, in this order: /home/claude/inputs/CAMPAIGN_CONTEXT.md, /home/claude/padua_research/topics/programme-ideas-20261031/brief.md (full), /home/claude/padua_research/topics/programme-ideas-20261031/gate.md (§1, §3, §5 item for your candidate, §8 flags), then your candidate's draft file(s) in /home/claude/padua_research/topics/programme-ideas-20261031/checks/state/ (host draft first, merged draft second). Then consult the two shorter reports in /home/claude/inputs/padua/reports/, RESULTS.md, research_notes, the parallel-branch snapshots in /home/claude/inputs/branches/ and the PDFs in /home/claude/inputs/papers/ (MAP.txt) as needed.

Web search and web fetch are authorized by AC for literature and ownership checks (CAMPAIGN_CONTEXT.md "Web access"). Use them extensively: publisher pages, arXiv, Google Scholar, Semantic Scholar, zbMATH, MathSciNet-like listings, homepages, project pages (ERC/NSF/FWO grants), group pages (Leuven NALAG, Padova CAA, Granada OPSF group, Xu's homepage, Cornell/Townsend, Oxford/Trefethen, Lille, etc.). Record every query with date and outcome. Never fabricate a link, author name, date or title: if you could not open a page, say UNVERIFIED. Keep any downloaded fulltext out of the repository (save under /home/claude/inputs/web/<your-candidate-id>/ if you need to).

## The four attacks (try all four, hardest first)

(i) ALREADY OWNED: a named group with a stated, active programme on this central question (papers 2018–2026, grants, theses, talks, software). "Someone once proved a related theorem" is not ownership; "a group has three recent papers and a funded project on exactly this question" is. Give names, dates, links, and say precisely which sub-problems of the candidate they already cover.

(ii) REALLY A NOTE: show that the central question collapses to one theorem/one algorithm, or that the sub-problems are not separable (one result settles all), or that after removing what is already known (gate §8 flags!) less than three substantive sub-problems remain.

(iii) ILL-POSED OR BLOCKED: apply the brief §3 obstruction table with exact hypotheses. Show the candidate's claimed escape fails, or that the central question is vacuous/undefined in the bivariate setting (e.g. the object does not exist generically, the template theorem is false in 2D, the "mechanism" is a renaming of an identity).

(iv) RENAMING OF AN EXCLUSION: (a)–(d) and the already-judged list. State the nearest item and show the claimed separating property is not a property (same proof, same object, same measurement).

You may run short scripts (Python/numpy/sympy/mpmath, n ≤ 8, seconds) to test a claimed mechanism; preserve them under /home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/<candidate-id>/ and mark outputs MEASURED within their stated scope. Do not run long computations. Do not edit any draft or any file outside your assigned output path and code directory.

## Output

Write exactly one file: /home/claude/padua_research/topics/programme-ideas-20261031/checks/adversarial-<candidate-id>.md with this structure:

```
# Adversarial check — <candidate-id>: <title>
Model: claude-fable-5-1, effort <xhigh|max> (as requested by the orchestrator) · Adversarial check · 2026-11-01

## Verdict
<one of: KILLED (i|ii|iii|iv) / WOUNDED (what must be dropped or re-scoped; what survives) / SURVIVES (strongest attack and why it failed)>
<two or three sentences>

## Attack (i): already owned
<evidence table: group / people / year / what exactly / link / verification status (opened fulltext, abstract only, listing only, UNVERIFIED)>
<conclusion, and which sub-problems are covered>

## Attack (ii): really a note
...

## Attack (iii): ill-posed or blocked
...

## Attack (iv): renaming of an exclusion
...

## Scripts run (if any)
<file, what it computed, scope, result, MEASURED>

## Search log
| # | Query | Engine/site | Date | Outcome |

## Required changes if it survives
<bullet list: sub-problems to drop/re-scope, claims to retract, papers that MUST be obtained and read before a proposal is written (DOI/arXiv links), the decisive test that would kill it fastest (for step 5)>

## Papers to obtain
| Authors | Title | Venue, year | DOI/link | Why |
```

Be concrete, plain, no hype. Quote nothing at length from PDFs or from bttb-research; locators and IDs only. If the candidate survives, say what the single most dangerous unresolved threat is. In your final reply give the verdict, the top evidence item per attack, and the search count.
