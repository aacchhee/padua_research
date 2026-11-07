# Independent supplementary review of the near-edge criterion

Reviewer: distinct Codex `/root/review_n1_round4`, requested Astra high;
serving metadata are not independently exposed. Input head
`fc1095361aaade1d25b015a2fb8212898271e12a`. The previously read AGENTS,
WORKFLOW and CODEX have no diff from the round-6 input `88e7023`.

**Disposition: accepted at the written conditional-comparison scope;
no mathematical finding.** This is routine assembly of accepted inputs,
with no new mechanism or novelty claim; no additional novelty gate is
needed. This supplements, and does not replace, the required Claude audit.

Read the entire frozen corollary and N5-04, checked the relevant N1-15
statement already independently reviewed, and verified these identities
with `sha256sum`:

| File | SHA-256 |
|---|---|
| `theory/near-edge-model-criterion.md` | `407905230e640cdf3689fd14995b315cd75461bd7156bf331b3519dc6051d4ab` |
| `theory/N1-round6-near-model.md` | `ca3b98dc209a27fde2924ac9f4112111fe5be7b4e520d8b68ed0c8b20b50ea63` |
| `theory/N5-two-phase-defect.md` | `de47e7d806f6c4d5107148516c7bec6686ba27c60b1d872572564ec94b7e0646` |

For J=0 the N5 physical phase is +alpha. For J=n it is -alpha,
since theta=pi-alpha/n gives x=-cos(alpha/n). In both cases the
absolute phase radius is alpha+|beta|<=1/2. Since q is interior,
pi-1/2<=q*pi+beta<=m*pi-pi+1/2, so the second angle remains strictly
inside (0,pi). The degree assumption implies N5's n>=64 hypothesis.

Reindexing an even physical checkerboard by the complementary center
gives periodic indices r=J±j and s=q±k. Their parity is odd because
j+k is even and J+q is odd. The resulting primitive is exactly
(1/(nm)) sum_odd |G_n(u_r,v_s)/2|, the N1 normalization. N5's H is
the same half-kernel: (-1)^r G_n/2, because
cos(nu_r)=(-1)^r cos(alpha). The exceptional term is thus retained
without a factor-two or constant-one substitution. Reflecting either
periodic index preserves odd parity; G is even in each angular
coordinate. Consequently S_n(-alpha,beta)=S_n(alpha,beta) and
S_n(alpha,-beta)=S_n(alpha,beta), exactly the S_n(alpha,|beta|)
to which the N1-15 model applies. No exchange of meshes is used.

The two accepted errors combine directly:

    lambda < S_n-1/2048
           < M_near+3/14000-1/2048
           = M_near-491/1792000.

The first difference has numerator 875-384=491 on denominator
1792000. Subtracting 1/4096 from that margin gives numerator
982-875=107 on denominator 3584000, which is positive. Therefore
both strict inequalities in (1) follow, and inserting the proposed
model upper bound gives lambda<Lambda_c-107/3584000. The older N5
finite-cotangent model error is not charged again.

The model maximum inequality remains an explicit OPEN premise.
The uniform conditional implication concerns exactly the displayed
interior complementary vertical-edge classes and integer-degree range.
It supplies no actual onset, far-phase bound, true-corner treatment,
other-class exclusion or full B3 PASS.

No mathematical program, numerical optimization or fit was run; the
arithmetic above was reconstructed analytically. Only this new review
file was written. The corollary, source proofs, earlier reviews, Git
state and shared records were left unchanged. Review is complete at
the listed hashes.
