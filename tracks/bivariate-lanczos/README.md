# Track: bivariate Lanczos (truncated recurrence in two commuting variables)

Opened by topic [bivariate-lanczos-20261031](../../topics/bivariate-lanczos-20261031/LOG.md) (Claude development, Codex audit pending).

## Question

Finite-precision behaviour of the truncated bivariate Lanczos/Stieltjes recurrence (Weisfeld 1959; Bartels–Jezioranski 1985; Huhtanen–Larsen 2002) for X = diag(x_i), Y = diag(y_i) and one start vector √w: what governs loss of orthogonality (single-section or joint Ritz pairs of the computed sections H_x, H_y), which reorthogonalization criteria are provable, whether a Greenbaum-type backward interpretation (exact recurrence for a nearby larger node set) exists, how the recurrence relates to band/block Lanczos, and the accuracy and pivot rules of the 2010 Givens updating (Van Barel–Chesnokov, Numer. Algorithms 55 (2010) 383–402).

## Assumptions and scope

Real distinct nodes, positive weights, total-degree graded order; exact-arithmetic, floating-point and labelled idealized models as defined in [plan.md](../../topics/bivariate-lanczos-20261031/plan.md). Out of scope: finite-field unisolvence; bivariate moments → OP complexity; 3D Padua points; Marcinkiewicz–Zygmund constants.

## Results

Theory files live in [theory/](theory/) with provisional IDs `PD-T?bivariate-lanczos-claude-nnn` / `PD-N?…` until PR preparation. See [NEGATIVE_RESULTS.md](NEGATIVE_RESULTS.md) and [AUDIT_LOG.md](AUDIT_LOG.md).

## Code

`code/inputs/` holds unchanged copies of the AC-supplied scripts that this track re-runs (see its MANIFEST); `code/` holds the track's own scripts.
