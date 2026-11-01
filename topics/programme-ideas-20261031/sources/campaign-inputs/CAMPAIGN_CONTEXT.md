# Campaign context for subagents — "Programme-scale research directions" (padua_research, branch claude/programme-ideas-20261031)

You are a reasoning subagent in an ideas campaign run by the orchestrator (Claude). Record at the top of every file you write: `Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator)`. You do NOT touch git. You only write the files you are assigned. Do not edit any file outside your assignment.

## Who AC is and what the campaign wants

AC = Andrey Chesnokov, co-author of Van Barel & Chesnokov, Numer. Algorithms 55 (2010) 383–402 (bivariate orthogonal-polynomial recurrence matrices via a Givens inverse eigenvalue problem; Padua points as nodes). Expertise: structured/semiseparable matrices, HSS (pySuperDC, a Python port of the SuperDC divide-and-conquer HSS eigensolver), unitary bulge chasing, inverse eigenvalue problems, plus an exact-arithmetic BTTB (two-level Toeplitz) solver programme (repo aacchhee/bttb-research, private; its recurring obstruction is the Õ(N^{(ω+1)/2}) "Popov curse"). Cite bttb-research items only by their IDs (EX-L1172, C3-T04, etc.) as they appear in the input notes; never copy their text.

Goal: find **programme-scale** research directions (2–5 years, several papers), not note-sized problems.

### What counts as a programme (every survivor must meet all five; say how)
1. A one-sentence central question that is open, with a mature one-dimensional or classical template theory that is missing in the bivariate/structured setting.
2. At least three substantive sub-problems with separate payoffs (papers), mixing at least two of: theory, algorithms, exact arithmetic, numerics/software.
3. Several entry points with cheap decisive tests (n ≤ 6–8, or seconds-long scripts), and a plausible first paper within about 6 months.
4. Not already owned: no group with a stated, active programme on exactly this. Give names, dates, links.
5. A clear fit with AC's expertise, and a 2–5-year horizon with escalating questions (the way the BTTB problem kept producing new tracks).

### Already running — do NOT propose these or close variants
- (a) Two-dimensional Schur/Levinson theory: complexity of bivariate moments/nodes → OPs/recurrence matrices, exact and below the curse exponent (Codex, bttb-research).
- (b) Finite-precision theory of the truncated bivariate Lanczos recurrence (Claude, this repo, branch claude/bivariate-lanczos-20261031).
- (c) Unisolvence of checkerboard/Padua-type sets over arbitrary fields via quasi-definite alternation functionals, plus finite-field Padua points (Codex, this repo, branch codex/charter-unisolvence-20261031).
- (d) Marcinkiewicz–Zygmund constants of Clenshaw–Curtis/Padua rules (Codex, this repo, branch codex/mz-constants-20261031).

### Already judged note-sized, solved or blocked — do NOT resurrect without a NEW mechanism that breaks the stated reason
- explicit Padua recurrences and Uvarov reweighting; Q-free downdating; conditioning of nodes → recurrences; empirical Christoffel functions via QR;
- multivariate Stieltjes in d ≥ 4; sketched Vandermonde-with-Arnoldi; histopolation on Padua triangles; Laurent bivariate OPs; moments → Jacobi as Prony;
- bivariate Hermite–Padé (it coincides with BTTB); measure modification (narrow); multiple-OP stability (Leuven's future work);
- 3D Padua points via cubature (Li–Sun–Xu conjecture against it); f(A,B) total-degree Krylov.
The stated reasons are in `reports/Round 3 open problems 2023 2026.md` (§3, §4.2) and `reports/Open problems verification.md` (§2).

## Inputs (all local, read-only)

- `/home/claude/inputs/padua/reports/Round 3 open problems 2023 2026.md` — current state of all candidates and verdicts (READ FULLY).
- `/home/claude/inputs/padua/reports/Open problems verification.md` — round 2 (READ FULLY).
- `/home/claude/inputs/padua/reports/Padua points research since 2010.md` — round 1 literature summary (long; the ranking is superseded but the literature summary stands).
- `/home/claude/inputs/padua/RESULTS.md` — AC's running working track (READ FULLY).
- `/home/claude/inputs/padua/research_notes/**` — detailed notes with page-level quotes behind the reports (consult as needed; do not re-derive what they already settle).
- `/home/claude/inputs/papers/*.pdf` with `/home/claude/inputs/papers/MAP.txt` — the paper PDFs AC owns. Read them locally when needed (Read tool with pages=...). NEVER copy fulltext passages into repo files; paraphrase and give page/theorem locators only.
- `/home/claude/inputs/branches/` — snapshots of the three parallel branches: their `state/IDEAS.md`, `literature/INDEX.md`, `literature/CORPUS.md`, topic `plan.md`/`LOG.md`/`baseline-candidates.md`, and literature records (`records_lanczos/`, `records_charter/`, read from fulltext by those branches). These define what is already owned inside the repo.
- Repo rules: `/home/claude/padua_research/AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`; templates in `/home/claude/padua_research/templates/` (IDEA.md, LITERATURE_RECORD.md, THEORY.md).

## Writing rules (binding)

- The repository is public: never commit third-party PDFs or fulltext extracts; paraphrase with locators.
- Status words: a computation gives `MEASURED` within its recorded finite scope; `PROVED` only with a written proof; `LITERATURE` labels cited facts and is not a proof status. Anything not checked against a fulltext is marked `UNVERIFIED`.
- Preserve every candidate (survivor, duplicate, rejected, deferred) in `templates/IDEA.md`-shaped records with its reason. Provisional IDs: `IDEA?programme-ideas-claude-NN`, `LIT?programme-ideas-claude-NN` (numbers assigned by the orchestrator at the end; use the local labels you are given).
- Never report an execution you did not perform. Never fabricate links, dates or author names; if you could not verify something, say so.
- Keep prose plain; no hype. Short paragraphs, tables where they help.

## Web access (AC's authorization, 2026-10-31 22:21)

AC approves reading and downloading from all websites that carry literature and papers (publisher pages, arXiv, HAL, Google Scholar, Semantic Scholar, zbMATH, ResearchGate, personal homepages, Lirias). Use WebSearch and WebFetch freely for prior-art and ownership checks. Record query, date and outcome. Do not commit any downloaded fulltext to the repository; keep it out of /home/claude/padua_research entirely (use /home/claude/inputs/web/ if you must save a page).
