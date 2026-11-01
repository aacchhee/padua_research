# E6 external code provenance and access limits

Rules/base: `806cc7b4509fd93bae652f9545d32d95529f8281`. Developer: Codex, requested gpt-6.1-sol medium; runtime exact model/effort not independently exposed. Date: 2026-11-01. Status words below distinguish source inspection from execution.

## Hokanson polyrat: inspected and executed

- URL: https://github.com/jeffrey-hokanson/polyrat ; commit `6903d7af9995c9d88e661fb229626696e00fdfba`; package version `0.2.2`.
- External checkout: `/workspace/padua-drift-external/polyrat`; no third-party source is copied into Git.
- Source files used, SHA256:
  - `polyrat/arnoldi.py`: `e51f356170dc5e1403f1065daf5bc331e7ce470cac1b9161f5ecb9efccf68d86`.
  - `polyrat/index.py`: `84df400c73a2aacf922ff38c0a591b525c2ac1f9b7a9f958f4111d4ceb88d10d`.
  - `polyrat/basis.py`: `9ce50feba7cfaa706db3bb94bbe2b34f065d9dbde28a18a3eee021d11e8ec478`.
  - `polyrat/version.py`: `1d13b63cb7af46b37f80ac0d695be5f795c2db5ce6e66dea34143da4cb434439`.
- `vandermonde_arnoldi_CGS(P[:,order], n, weight=np.sqrt(w))` and `vandermonde_arnoldi_eval(test[:,order], H, indices)` are actual unmodified upstream function calls. `_update_rule` and `total_degree_index` are also called, not reproduced. No numerical algorithm in upstream source is edited.
- Our loader inserts a namespace `polyrat` package, then imports the actual `arnoldi`, `index`, and `basis` modules. This avoids unrelated imports in upstream `__init__.py` (cvxopt, cvxpy, iterprinter), absent in this environment. Upstream `basis.py` needs `backports.cached-property==1.0.2`, installed outside Git at `/workspace/padua-drift-external/deps`. Namespace loading is an adapter; it is not a full package-install test.
- Source-verified ordering is `(0,t),(1,t-1),...,(t,0)` within each degree. `_update_rule` chooses the smallest array index having multi-index difference one. For input `[x,y]`, this is mirror selection in **reverse campaign within-degree order**. Swapping to `[y,x]` gives exactly campaign dev selection and order. Every parent is checked through n=47 in our adapter. Input order matters: default xy is not numerically interchangeable with campaign mirror in forward order. The source does two classical Gram–Schmidt passes against every earlier column.
- All polyrat upstream_yx versus our L2 dev runs have entrywise difference exactly zero in this execution. This is measured agreement, beyond the selection identity; it is not a claim of bitwise reproducibility across libraries/platforms.

## Brubeck–Nakatsukasa–Trefethen: source inspected, execution pending

- Actual author-attributed public source retrieved by cloning https://github.com/chebfun/examples at commit `f4b9ea46cfc2f52f20a844627f4a74d0bb10098c` into `/workspace/padua-drift-external/chebfun-examples`.
- File: https://github.com/chebfun/examples/blob/f4b9ea46cfc2f52f20a844627f4a74d0bb10098c/linalg/VandermondeArnoldi.m . Header names Pablo Brubeck, Yuji Nakatsukasa, Nick Trefethen, January 2020. SHA256 `625f29c9f58c26699b664e9f88b7734d4ba74d29cfe9f7faefb314e5bc49d003`.
- Inspected local functions `polyfitA` and `polyvalA`: they multiply by one scalar coordinate and perform one modified Gram–Schmidt pass. This file is univariate, uses Chebfun quasimatrices in its surrounding example, and supplies no two-variable selection to classify. It is not the multivariate CGS2 implementation used above.
- Neither `command -v octave` nor `command -v matlab` returned a runtime. **Not executed.** Runs needed: install/use a supported MATLAB/Chebfun environment and run this unmodified example; assess a separately labeled numeric-vector extraction only after recording the adapter. This missing run does not affect the actual polyrat measurements.

## Zhu–Nakatsukasa: identifiable paper, code unresolved

Paper: arXiv:2301.12241; DOI https://doi.org/10.1093/imanum/draf055 ; IMA J. Numer. Anal. 46(4) (2026), 2072–2106 (metadata inherited from the existing record, not freshly verified here). No author-code repository was identified in bounded public GitHub repository searches. This is **not** a claim that no code exists. No ZN code was run or selection classification assigned.

Access attempts on 2026-11-01, through preserved injected proxy:

- GitHub repository search `"Vandermonde" "Zhu"`, `Zhu Nakatsukasa`, `Vandermonde irregular`, `Brubeck Arnoldi`: no matching author repository found. General `Vandermonde Arnoldi` returned unrelated implementations, not asserted to be authors' code.
- Guessed GitHub profiles `yujinakatsukasa`, `WeizhuMath`: HTTP404. `Weizhu` exists but identity/connection to this paper was not established.
- `https://people.maths.ox.ac.uk/nakatsukasa/codes.html` and `https://people.maths.ox.ac.uk/trefethen/VA/`: proxy CONNECT403 Forbidden. These were destination-policy failures; no bypass attempted.
- Initial guessed raw paths `chebfun/examples/master/approx/VandermondeArnoldi.m`, `.../fun/VandermondeArnoldi.m`, and `chebfun/chebfun/master/+chebfun/VAorthog.m`: HTTP404; actual BNT path found subsequently by inspecting the examples clone.
- Later GitHub searches `1911.09988 in:readme`, `VAorthog in:readme`: HTTP429. `2301.12241 in:readme` search returned unrelated numeric-token matches and was not treated as evidence.

Runs needed: obtain an identifiable ZN authors' code URL (or accessible paper/supplement containing that URL), pin its source, inspect its actual order/selection and execute it. Do not substitute polyrat results for a ZN implementation run.

## Reproduction and retention

`evidence/e6-provenance.json` manifests code/output hashes, environment and exact commands. Small JSON evidence totals below 1 MB, each file below 1 MB. External source checkouts are locally retained; long-term archival awaits AC's cold-storage destination. Source identities above permit re-fetching. Network skill and `/etc/codex/network-policy.json` were read first; current runtime reported enforced restricted HTTP policy. Network calls used `with_additional_permissions` plus `network.enabled=true`, retaining inherited proxy/CA settings. No contacts or messages were sent to paper authors.
