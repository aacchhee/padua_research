# Handoff NN — <topic slug> — <step>

A new numbered file for each step, opened by the orchestrator holding the previous handoff. Never overwrite an earlier handoff or alter its body; only the status line changes. AC starts the step with `<Agent> (<model, effort>): Continue <branch>.`

- Status: open  <!-- open while in progress; then: done in <output-commit-sha> | superseded by NN: <reason> | withdrawn: <reason> -->
- Previous handoff: <NN-<step>.md, or none>

- Next agent / model / effort: <e.g. Codex, gpt-6-astra high>
- Role: <developer | auditor | orchestrator>
- Branch: <branch>
- Input head SHA: `<full sha of the existing commit being handed off>` (the commit that publishes this file comes later)
- Main / base: `<sha>`
- Stage: <WORK | AUDIT | PR>
- Written by / date: <agent, model> · <date>

## Task

<The complete instruction: what to do, in which order, with exact file paths and commands.>

## Read first

<Rules, log entries, records, audits, and maps the agent must read.>

## Scope limits

<What not to reopen or change; protected files; authority limits (e.g. only AC merges).>

## Acceptance and outputs

<Criteria for done; files to write (e.g. audit-NN.md, response-NN.md); PR body and log updates. When done: commit the outputs; then, in a following commit, set this handoff's status to `done in <output-commit-sha>` and add the next numbered handoff in the same commit. If no work remains, close this handoff and record completion in the log (or in this status line for a log-exempt job), without opening a successor.>
