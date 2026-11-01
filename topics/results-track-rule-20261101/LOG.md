# Local working-track rule (RESULTS.md overwrites)

- Branch: `claude/results-track-rule-20261101` · Base: `0d058fb410166bd97b178be57910f2d256d0b529` (= `origin/main`, 2026-11-01) · Developer: Claude · Auditor: Codex
- Stage: AUDIT · Next: `Codex (gpt-6-astra medium): Audit claude/results-track-rule-20261101 (protocol rule amendment).`
- Claims: none (protocol rule only).

## Rule amendment

AC explicitly asks to change the rules (2026-11-01): "looks like we need a rule about results.md as they get constantly overwritten. keep own, unite at PR?"

Reason: on 2026-11-01 several concurrent sessions wrote AC's local `Downloads\padua\RESULTS.md`; at least one rewrote the file from an older copy and removed other topics' entries (the programme-ideas entries, their correction, and a cross-campaign summary line). The programme-ideas section was re-added by its orchestrator; the other lost text belongs to other topics.

### agents/WORKFLOW.md — "Computation and evidence", one paragraph added before the paragraph beginning "A committed generated file must be necessary"

Before: no rule on local files outside Git besides cold storage.

After (added paragraph, nothing removed):

```
AC's local working track lives in AC's Padua folder outside Git (`Downloads\padua` on AC's computer). Each topic keeps its own file `results/<topic-slug>.md` there; only that topic's orchestrator writes it, appending or revising its own entries. The shared `RESULTS.md` is a merged view: a topic changes only its own section there, and only at PR preparation or after AC merges its PR, by appending or replacing that section from its own results file. Before any write to a shared local file, stage the current bytes, merge into them, and write with the modification-time guard; on a guard rejection, stage and merge again, never force. Never rewrite another topic's section or regenerate a shared file from an older copy. A lost section is restored from that topic's own results file. Local files carrying third-party text or private material stay out of Git.
```

Other rule files are unchanged. The rule governs files outside the repository; it needs no repository change beyond this paragraph.

## 2026-11-01 — Claude (claude-opus-5-5; effort not exposed)

- Rules read at `0d058fb` (AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md). Separate small branch so that the rule can merge independently of the topics in audit.
- Adoption on AC's computer by the programme-ideas topic: its entries are moved into `results/programme-ideas-20261031.md`; `RESULTS.md` keeps its current section until that topic's PR is prepared.

## Runs needed

None.
