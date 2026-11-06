# D6/D7 source access and coverage

Codex, dispatched gpt-6.1-sol medium, 2026-11-05; rules/source
`823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`. This is an access record,
not a new LIT allocation or primary full-paper verification.

| Source | Actually inspected this round | Limits |
|---|---|---|
| LIT-347/119 [arXiv 2506.19796v2](https://arxiv.org/pdf/2506.19796v2) | Web connector PDF, 28 pp, v2 4 March 2026: opening definitions and §6.1–6.2 experiments, PDF pp20–22 | Bounded fulltext reading, not complete paper/proofs or published-PDF verification; no local PDF bytes/hash. Screenshot calls were made but yielded no inspectable image content in this interface, so no image verification is claimed. |
| [SIAM journal page](https://epubs.siam.org/doi/10.1137/25M1770965) | Metadata, abstract and complete supplementary-material listing | Published article fulltext not obtained here; inherited repository assessment remains attributed to its reader. |
| [DOI resolver](https://doi.org/10.1137/25M1770965) | Access attempted via web connector | Connector returned inaccessible; journal page succeeded separately. |
| [Leuven source](https://gitlab.kuleuven.be/numa/public/IEP-MOP) | Access attempts only | Source not read, no commit; shell CONNECT403; connector inaccessible. |
| [Publisher code ZIP](https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip) | Publisher listing read and download link clicked | Connector rejects ZIP content type; shell CONNECT403. No code bytes or hash. |
| LIT-562–568 | Existing literature/INDEX.md and predecessor source/gate records | No fresh primary theorem reading or upgraded coverage this round. |

LIT-347 bounded primary report: §6 uses p1=.4,p2=.5 for Kravchuk and
beta1=1,beta2=1.5,gamma=1 for Hahn, N=5…30. Forward error is a matrix
2-norm relative error; biorthogonality is measured separately. §6.2 uses
Advanpix quadruple computations for a reference/conditioning diagnostic.
These are source reports, not local proof, derivative certification or
external-code reproduction. Their matrix metric differs from the local
maximum of four NN field sup-norm relative errors.

Configuration issue for G5: the preprint's extracted Kravchuk weight formula
and its N indexing are not sufficient to certify agreement with the inherited
normalized Binomial(N−1,p) inputs; text extraction may be incomplete, and the
published source/driver has not been read. Do not alter the inherited baseline
or assert a paper error from this extraction. Inspect actual nodes_weights.m,
kravchuk_data.m and experiment driver, together with the published formula,
before selecting a reproduction. Hahn is a plausible first configuration,
but no configuration has been reproduced or passed.

The repository's existing
[assessment](../padua-literature-20261103/notes/faghih-sinum-2026-assessment.md)
was read as an inherited report, with its original reader and selected
coverage preserved. No contact with the authors or anyone else was made.
Access blockers are capability/policy observations, not proof of source
nonexistence. Public DOI, journal, preprint and code links above are the
concrete sources for resuming the task.
