# Independent supplementary check — P4 denominator derivation

Date: 2026-11-06. Reviewer: distinct Codex supplementary agent, requested
`gpt-6-astra` high; actual serving-model/effort metadata are unexposed.
Rules and supplied fetched-tree input:
`f3c14d7599b4bf25118ca86bc62aeb5e0fcafe29`.

**PASS within the scope below.** No unresolved mathematical or citation
finding was found. This is the distinct supplementary check requested by
[handoff 05](handoffs/05-response-02.md) for audit-02 B2. The subsequent
focused Claude recheck remains separate; this is not PR readiness approval.

## Scope and frozen records

Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, handoff 05 and
[audit-02](audit-02.md). Reconstructed the denominator identities directly
from the canonical S2 basis and integral definition before reading the new
derivation or earlier supplementary reconstructions. Then compared every
step with the frozen new proof and the relevant S2/P4 citations, and read
the earlier independent-checks-S2-model.md and independent-checks-P4.md.

The following SHA-256 identities were actually checked with `sha256sum`
in `/workspace/sharp-work` after the developer's freeze:

| Record | SHA-256 |
|---|---|
| theory/P4-denominator-closed-form.md | 76a5b30ddec49c4e4d3a7586101d525d58c5de0359bcfa61087d11ee9b17a92f |
| theory/S2-endpoint-model.md | 4b9dccb0dca67d62aa08d41e3a76ec99550b903ba0e75f1dd1d8a87b6d142643 |
| theory/P4-certified-lower.md | dcfaeae4fbc09f514866a24260309aa6aac072a4475d86610ff815eeef6aab74 |

This bounded task makes an already accepted identity durable. It proposes
no candidate, mechanism, novelty or priority claim. Under WORKFLOW's
no-novelty audit exception, a new full IDEAS/literature search was not
needed or performed. No numerical campaign, certificate rerun or code
change was needed or performed. Prior execution claims remain attributed
to their existing records. Only this supplementary record was written;
Git and developer files were not changed.

## Independent reconstruction and comparison

Write a=pi*j, s_j=(-1)^j and

    f_j(t)=2s_j*a^2*sin(t)/[t(t^2-a^2)].

The local expressions give f_j(0)=-2s_j and f_j(a)=1. At a different
positive grid point the value is zero. The basis is continuous after
filling these values and decays as O(t^-3). Hence every product t f_i f_j
is absolutely integrable: O(t) at zero, continuous internally, O(t^-5)
at infinity. All finite quadratic-form expansions are consequently valid.

For a positive integer multiple a of pi, define

    H(x)=integral_0^x sin^2(v)/v dv=Cin(2x)/2,
    I(a)=integral_0^infinity sin^2(t)/[t(t^2-a^2)] dt,
    K(a)=integral_0^infinity t sin^2(t)/(t^2-a^2)^2 dt.

Both I and K are absolutely convergent. Their internal limits are 0 and
1/(4a), respectively; there is no principal-value operation.

**Common cutoff for I.** At the same R>a, partial fractions and translation
by a give exactly

    a^2 I_R(a)=[H(R-a)+H(R+a)]/2-H(R)-H(a).

The negative translated interval contributes -H(a), since sin^2(v)/v is
odd. The first three terms have absolute value at most

    [log(R/(R-a))+log((R+a)/R)]/2,

which tends to zero. Therefore I(a)=-Cin(2a)/(2a^2). The logarithmically
divergent pieces are combined before any infinite limit is taken. This
matches proof part 2, including its signs and bound.

**Unequal indices.** For A=a_i^2 and B=a_j^2,

    1/[(t^2-A)(t^2-B)]
      =[1/(t^2-A)-1/(t^2-B)]/(A-B).

Multiplication by sin^2(t)/t and the basis prefactor gives
4s_i*s_j*A*B*[I(a_i)-I(a_j)]/(A-B), and therefore exactly

    C_ij=2s_i*s_j*(A*d_j-B*d_i)/(A-B).

This proves both orders of every unequal positive integer pair. The
separated integrands have removable poles and are absolutely integrable,
so the integration used in proof part 3 is valid.

**The Si integral and diagonal.** Integrating by parts gives

    K(a)=(1/2)integral_0^infinity sin(2t)/(t^2-a^2) dt.

The boundary expression -sin^2(t)/[2(t^2-a^2)] tends to zero at 0,
infinity, and separately on each side of a. The new integrand has internal
limit 1/a and an absolutely integrable O(t^-2) tail. The derivation's
split-interval integration by parts therefore has no missing interior
boundary term. At a common finite R the linear-denominator translations
give

    integral_0^R sin(2t)/(t^2-a^2) dt
      =[2Si(2a)+Si(2(R-a))-Si(2(R+a))]/(2a).

The remaining Si difference is bounded in absolute value by
log((R+a)/(R-a)); its limit is zero. This proves K(a)=Si(2a)/(2a)
without assigning separate infinite values to the translated terms.

The directly checked diagonal partial fraction identity is equivalently

    1/[t(t^2-a^2)^2]
      =[t/(t^2-a^2)^2-1/(t(t^2-a^2))]/a^2.

It agrees algebraically with the displayed decomposition in proof part 4.
The bracketed 1/t-t/(t^2-a^2) terms there are kept together, so their
logarithmic divergences are never independently integrated to infinity.
Consequently

    C_jj=4a^2[K(a)-I(a)]=2[a*Si(2a)+Cin(2a)].

This is a direct diagonal calculation. No differentiation in the integer
frequency parameter or invalid continuous off-diagonal limit is used.

## Findings and limits

No findings. The new PROVED record covers all positive integer indices,
the diagonal, the off-diagonal, and every finite real quadratic form.
The absolute convergence, cutoff limits, translations and boundary terms
support that status. The S2 registered formula and P4 finite denominator
citations point to the correct new record and preserve their formulas.

This approval concerns the denominator identity and its local citations.
It does not re-audit the S2 limit theorem, P4 scalar certificate or its
one-sided lower bound, P1/P2/P3, other response edits, shared registries,
or the eventual PR application. It supplies no sharp upper bracket,
two-sided digits, arbitrary-frequency extension, or infinite coefficient
sum theorem. The focused Claude review of these new proof bytes remains
the next required mathematical review.
