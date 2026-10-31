# PD-T?charter-u0-codex-05 — Evaluation-code dimension, weighted dual and distance bound

ID kind: PD-T. Aliases: Padua codes, footprint lower bound.
Split from: supplied finite_field_padua.md §4 general claims.
Split into: [code-distances.md](code-distances.md), `PD-T?charter-u0-codex-07`, contains only finite measured distances.

## Statement

Let the canonical `Pad_n` consist of `N=(n+1)(n+2)/2` rational points over `F_q` in good characteristic. For every integer `0<=k<=n`, the linear evaluation code `C_k=ev_(Pad_n)(P_k(F_q))` has dimension `K=(k+1)(k+2)/2`, and

`C_k^perp = W span{ev(T_a(x)T_b(y)): k<a+b<=n}`

for the ordinary coordinate dot product, where `W` is the invertible diagonal weight matrix in `PD-T?charter-u0-codex-01`. Its minimum nonzero Hamming weight satisfies `d(C_k)>=dim P_(n-k)=(n-k+1)(n-k+2)/2`.

## Definitions and assumptions

Hamming weight counts nonzero coordinates. This statement does not claim any exact distance or optimality among codes of the same length and dimension.

## Status by part

Overall status: **PROVED** (developer derivation; independent acceptance PENDING). No novelty claim.

## Depends on

[gram-unisolvence.md](gram-unisolvence.md), `PD-T?charter-u0-codex-01`, and its explicit Gram identity. No Gröbner-basis or external coding theorem is required.

## Proof

The evaluation map is injective on `P_n`, so also on its subspace `P_k`, giving dimension `K`. By the diagonal Gram identity, every column of degree greater than `k`, after multiplication by `W`, is dot-orthogonal to every column of degree at most `k`. There are `N-K` such columns; they are independent because all columns of `V` are independent and `W` is invertible. They therefore span the whole orthogonal complement, which has dimension `N-K`. This also covers `k=n`, where both spaces are zero.

For the lower bound, take a nonzero polynomial `f in P_k` and let `s` be the support size of its evaluation vector. The map `g -> ev(fg)` from `P_(n-k)` is injective: a zero evaluation implies `fg=0`, because its degree is at most `n` and evaluation there is injective, and hence `g=0` in the polynomial domain. Every image vector is supported on the same `s` coordinates where `f` is nonzero. This vector space has dimension at most `s`, so `s>=dim P_(n-k)`. Minimize over nonzero `f`.

## Checks and sources

Supplied code checks weighted duality for `k=n-1` at `(q,n)=(7,3),(11,5),(13,6),(17,8),(5,2),(31,4)`. Exact distances are separated into [code-distances.md](code-distances.md). Source §4 cites affine-variety/Cartesian/downset-code literature, whose original sources this developer did not inspect; no external theorem is used above.

## Scope and open items

The multiplication proof shows the same distance lower bound for every `P_n`-unisolvent set, so the bound alone does not distinguish Padua codes. The independent adversary has supplied a separate self-contained all-code bound, `PD-T?charter-u0audit-codex-01`, in `independent/u0/code-optimality-bounds.md`; integrating and accepting that bound is the orchestrator's handoff. The finite attainment observations stay in `07`. Independent acceptance pending.

## History

2026-10-31, Codex U0; rules/base `d36722823441dc40c6e19d69a174459348dd309c`; assigned `gpt-6.1-sol xhigh`. Split general structure (written proof) from finite distance observations; obtained the lower bound directly from unisolvence.
