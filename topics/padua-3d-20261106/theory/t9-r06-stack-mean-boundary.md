# PD-N?padua-3d-20261106-codex-T9-r06-02 — exact limit of the all-order stack mean argument

Aliases: T9-R06-B; T9-R06-PDN02; stack mean-method obstruction. This is a provisional local ID, not a global allocation.

Status: **PROVED method obstruction**, not a quality theorem for every stack ordering.

Use the stack and determinant notation of `t4-stack-determinant.md` and `t4-monotone-lower.md`. Let the n+1 heights be h_a=cos(a pi/n), let N_j=binom(n-j+2,2), N=binom(n+3,3), S=binom(n+3,4), and

```
A_n=((n+1)log n+(3-n^2)log 2)/(n(n+1)).
log D(pi)=sum_(i<j) N_j log|h_pi(j)-h_pi(i)|.
```

For every permutation pi the established determinant comparison gives

```
log Lambda(pi) >= max(0,(S A_n-log D(pi))/N).
```

Under a uniformly random permutation, each pair (h_pi(i),h_pi(j)) is uniformly distributed over the unordered height pairs. The mean logarithmic pair distance is A_n, and sum_(i<j)N_j=S. Therefore the exact permutation mean of log D(pi) is S A_n. At least one permutation pi_max has log D(pi_max)>=S A_n. For that permutation the displayed lower bound is precisely zero.

Consequently this **specific mean-determinant comparison cannot prove a strictly positive lower bound simultaneously for every stack ordering**, in any degree n>=1. Increasing permutation search size cannot repair that algebraic loss. This resolves the all-order mean-comparison mechanism, rather than leaving 'new premises required' as an untested route. It does not imply Lambda(pi_max)=1, does not disprove an exponential class lower bound obtained by another method, and does not promote the previously measured alternating-order rate to a theorem. The existing monotone-order theorem remains a proper subclass result. The phase-uniform annihilator and its limitations for cosets are in `t9-r06-phase-weight-boundaries.md`.
