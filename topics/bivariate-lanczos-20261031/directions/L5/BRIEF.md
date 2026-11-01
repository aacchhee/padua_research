# Side direction L5 brief — 2010 Givens updating: accuracy deficit and pivot rules

Developer: Sonnet 5.5, high (experiments and routine analysis); any non-routine proof is escalated to the orchestrator. Common rules: [../COMMON_RULES.md](../COMMON_RULES.md) with direction number 5 (IDs `…-5nn`, code in `tracks/bivariate-lanczos/code/L5/`, logs in `directions/L5/logs/`).

## Goal (short note)

Explain the 0.6–1.1-digit deficit of the Van Barel–Chesnokov 2010 Givens updating against HL (reported error ∝ M vs ∝ √M, MEASURED in the inputs), the "larger redundant pivot" catastrophe caused by non-unisolvent intermediate prefixes, and give safe pivot/deflation rules. Settled background not to re-derive: Q-free downdating = classical R-factor downdating; conditioning = routine Fischer 1998 extension.

## Frozen first question

See `../../plan.md` §L5-Q1 (do not reword).
