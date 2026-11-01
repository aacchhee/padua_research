# U0 independent review of the adversary's all-code bounds

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`; reviewer Codex U0, assigned `gpt-6.1-sol xhigh`; 2026-10-31.

Reviewed complete `topics/charter-unisolvence-20261031/independent/u0/code-optimality-bounds.md`, SHA-256 `10f7973b684e6d9fbdfe71da09b156ae8700386f2c8297cab25a8c4c8fab280c`. This is a hand-proof review, not a new execution or an inherited source theorem. No change made to the adversary's file.

Result: no mathematical finding. Reconstructed the two arguments independently: a dependent triple of columns of a rank-three generator gives a nonzero word of weight at most7, while ten independent projective columns would require nine distinct lines through one point although only eight exist. For dimension6, a hypothetical distance at least5 forces independence of every six generator columns. The dual has parameters `[10,4,7]`, using the explicitly proved Singleton bound. Its nonzero coordinate functional allows shortening to `[9,3,7]`; a zero coordinate functional would itself violate Singleton after puncturing. The shortened generator defines a nine-point arc in `PG(2,7)`. All eight lines through each arc point are secants, so there are no tangents. An external point exists and its eight lines partition the nine arc points into intersections of sizes0 or2, a contradiction.

All duality, shortening and projective-count steps are justified in the reviewed text. The bounds concern linear codes only. They remain separate from the developer's MEASURED Padua attainment observations. Root/Claude final acceptance is outside this review.
