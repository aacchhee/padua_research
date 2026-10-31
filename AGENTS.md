# Padua research: agent instructions

This is the independent research repository `aacchhee/padua_research`. AC is the human owner and final decision maker. Scientific definitions and assumptions must be stated in this repository; no external project supplies implicit context or proof.

## Start and authority

Before work, read this file, `agents/WORKFLOW.md`, and your role file at the branch head: `agents/codex/CODEX.md` for Codex or `agents/claude/CLAUDE_ROLES.md` for Claude. Record the full commit SHA in the work log. Re-read changed rules when switching branches. AC's explicit task instructions take precedence; otherwise these files are binding. Resolve an actual conflict with AC before the conflicting action, while continuing independent work.

The first line of every user-facing reply is `Rules <short-sha>`, using the commit at which the rules were read. The second line states how you interpret the request. End with an exact suggested next prompt for AC, naming the agent and model. Give a useful progress update about every five minutes during sustained work and checkpoint substantial results in durable files.

## Repository permissions

AC preauthorizes creating topic branches, committing and pushing to them, and opening pull requests against `main` for assigned work. The orchestrator performs these operations without asking again. Never commit or push to `main`. Never merge a PR, force-push, or create, move, or delete tags. Only AC merges. Do not change repository settings, branch protection, workflows, or anything under `.github/` unless AC specifically requests it. Do not treat a missing base branch as permission to initialize or write `main`; report the concrete bootstrap requirement to AC.

Use a task branch from a recorded base SHA. Keep unrelated work intact. Agents must not share mutable Git operations: only the orchestrator controls Git, branches, commits, pushes, and PRs. Subagents work on assigned disjoint files or return patches/results. Coordinate ownership before writing shared files.

## Research obligations

Apply the novelty gate before proposing new ideas or claiming novelty. Preserve every considered candidate, including failed and deferred ones, with a scoped reason. Maintain durable theory files with explicit proof status; a topic log alone is insufficient for a mathematical result. Distinguish proof, conditional reasoning, measurement, and literature reports. Never report an execution you did not perform or promote a source's claim into an inherited proof.

Use the model allocation, development/audit separation, evidence rules, and PR procedure in `agents/WORKFLOW.md`. Claude audits Codex development and Codex audits Claude development. Independent subagent checks supplement that handoff. Draft PRs may open while audit is pending if clearly labeled; readiness requires the audit record and dispositions. Only AC decides whether to merge.

Generated outputs stay outside Git by default in Padua-specific cold storage chosen by AC. Do not invent or reuse an unrelated storage location. Commit small necessary evidence only under the limits and manifest requirements in the workflow.
