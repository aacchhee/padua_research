# Handoff NN — <topic slug> — <step>

A new numbered file for each step. Never overwrite an earlier handoff; update only its status line. AC starts the step with `<Agent> (<model, effort>): Continue <branch>.`

- Status: open  <!-- then: done in <sha> | superseded by NN | withdrawn: <reason> -->
- Previous handoff: <NN-<step>.md, or none>

- Next agent / model / effort: <e.g. Codex, gpt-6-astra high>
- Role: <developer | auditor | orchestrator>
- Branch / head SHA / base: <branch> · `<full sha>` · main `<sha>`
- Stage: <WORK | AUDIT | PR>
- Written by / date: <agent, model> · <date>

## Task

<The complete instruction: what to do, in which order, with exact file paths and commands.>

## Read first

<Rules, log entries, records, audits, and maps the agent must read.>

## Scope limits

<What not to reopen or change; protected files; authority limits (e.g. only AC merges).>

## Acceptance and outputs

<Criteria for done; files to write (e.g. audit-NN.md, response-NN.md); PR body and log updates. When done: set this handoff's status to `done in <sha>` and open the next numbered handoff.>
