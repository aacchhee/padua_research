# Claude audit-01 evidence manifest

Auditor: Claude Opus 5.5 xhigh, 2026-11-01. Candidate e847601c6c1f1261d4862d63360fdfdb0df8a15b. Commands and scope are in [audit-01.md](../../audit-01.md), section 'Independent executions'. Scripts were run from /home/claude/audit-scripts (check_t110.py imports claude_mz2d_audit_extra from there). Receipts were written outside the candidate tree and then copied here. The partial R3 receipt covers m10–30; m40 was still running at commit time.

| File | Bytes | SHA-256 |
|---|---:|---|
| `check-t110.log` | 61 | `f7e14f332dc0a1061901eee7df25d5a32e0c0f22dad2c1aec530f6968ccceaa2` |
| `check_t110.py` | 892 | `f83222c24af935da07e5b44993683f0e171d049bb6ddd96c5bfc89123dae16c6` |
| `claude-audit-check.log` | 276 | `eeb36c5a578bccbcc10c74096440a6866cc0bb7eb81617112cceb863bb05cc50` |
| `claude-audit-check.partial-m10-30.json` | 5969 | `9a26b5563104575845eda195c0e8e2f55a3fe1e690e2545b49fd6f709e9789f4` |
| `claude-audit-extra.json` | 12762 | `8074cda667df330ceb7bfff86b56ff8fca71f3ecbba17d3946902f93ce1b51ee` |
| `claude-audit-extra.log` | 86 | `bf2f2e8b3cbe01f6fbf51b36bfb0f453928d0e09dde76990b52dba7da04abec5` |
| `claude-dev-independent-functions.json` | 2650 | `6526988b4915e7399c7cd0a70f826f6a2af2fdf0bb9d848dc0baced764781ae2` |
| `claude-mz2d-spectra.json` | 31818 | `de3a6dc6726268ac5c0e61f46c79435e561be1514f76c60f6e79f17120f7bbbd` |
| `claude_mz2d_audit_check.py` | 12388 | `6a3d00d9233ba45a68987ccc3e225851a93ae7f0928e76cd7632131ec9a86a94` |
| `claude_mz2d_audit_extra.py` | 9225 | `0dfa2e26a3735f5527910fafc26377a773acf17c4065f8ab34f405fdf08cedc4` |
| `dev-indep.log` | 62 | `ec4f39327520e619c5d419756a07b761b6eaab6f820d5c4d0ba72eb9523af80e` |
| `exact-run.log` | 128 | `038fbddc6bf9b098a1b42df095caf9b88afc814bf090c2843190b816cf168908` |
| `final-validation.claude-rerun.json` | 18087 | `f8cc5398347a4e0961e39e8c1d952071ee42addd0d5b76fc6cfb1435b6fc14e9` |
| `run_dev_independent_functions.py` | 1668 | `a5df50b33f89da87e6169f0f97ef129bcd0bc256311919de1a4ebb699cdbc0e5` |
