# L7 external-source preparation — no numerical execution

Rules/input `8359bf7a047d9a212bd841224fb97a458cb7435e`; 2026-11-05, Codex gpt-6.1-sol medium. G0 FAIL stops G4 and all L7 experiments. No third-party code or PDF in Git. Managed cloud runtime/networking skill, observed enforced network policy and /etc/codex/network-policy.json were read before network access; inherited proxy retained. No messages to authors.

## polyrat — source/dependencies supplied by independent G0 worker

- Pin https://github.com/jeffrey-hokanson/polyrat commit `6903d7af9995c9d88e661fb229626696e00fdfba`, version0.2.2.
- Read-only setup paths reported by g0_replay: `/tmp/padua-lanczos-frontier-g0/polyrat`, helper deps `/tmp/padua-lanczos-frontier-g0/deps` (cached-property1.0.2; also python-flint0.9.0).
- G0 worker reports base NumPy2.3.5/SciPy1.17.0 and all four upstream hashes match prior E6. This worker has **not executed** the upstream source or independently certified those checks.
- Intended namespace-package loading is the prior e6_benchmark.load_upstream adapter, avoiding unrelated package imports; upstream numeric source stays unchanged.
- Tested historical NumPy pin2.3.5 remains required; >=2.4 excluded by prior measured upstream compatibility failures. No dependency was installed or changed by L7.
- Actual G4 command remains unrun: `PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e6_benchmark.py --external /tmp/padua-lanczos-frontier-g0/polyrat --sets rotpi4 triangle --output /tmp/padua-lanczos-frontier-l7/g4.json`.

## BNT — actual pinned source retrieved and completely inspected

URL https://raw.githubusercontent.com/chebfun/examples/f4b9ea46cfc2f52f20a844627f4a74d0bb10098c/linalg/VandermondeArnoldi.m . HTTP200,5657bytes, SHA256 `625f29c9f58c26699b664e9f88b7734d4ba74d29cfe9f7faefb314e5bc49d003`. Local `/tmp/padua-lanczos-frontier-l7/bnt.m`; fetched by Python stdlib urllib.request.urlopen(url,timeout=25), bytes written unchanged. Matches prior E6 identity. Header attributes Pablo Brubeck, Yuji Nakatsukasa, Nick Trefethen, January2020.

Complete source tutorial read. It defines univariate polyfitA/polyvalA with one modified Gram–Schmidt pass, and a Chebfun absolute-value degree80 example. It does not define a two-variable parent selection. Its Chebfun/quasimatrix constant, inner products and norms cannot silently be replaced with unnormalized numeric-vector operations. A numeric-vector extraction would require explicit adapter documentation and validation. No adapter was written/executed.

`command -v octave` returned no path. `apt-get update` was attempted with network enabled and failed exit100: `/var/lib/apt/lists/partial` missing, read-only filesystem, plus unreadable apt retry config. This tests the ordinary system install route only, not impossibility of installing Octave under a local prefix. No local-prefix install completed; G0 then stopped experiments. Actual BNT/Chebfun execution **NOT RUN**.

## Zhu–Nakatsukasa — bounded discovery, no identifiable code

Actual Python urllib requests, preserving proxy:

- https://arxiv.org/pdf/2301.12241 : proxy tunnel403, no PDF received/read.
- https://arxiv.org/pdf/1911.09988 : proxy tunnel403, no PDF received/read.
- https://api.github.com/search/repositories?q=Vandermonde+Arnoldi+Zhu and `?q=2301.12241`: proxy tunnel403.
- https://github.com/search?q=%22Vandermonde%22+%22Zhu%22&type=repositories : HTTP200; embedded result_count0/page_count0, logged_out.
- https://github.com/search?q=%22Nakatsukasa%22+%22Zhu%22&type=repositories : same zero repository result count.
- https://github.com/search?q=%222301.12241%22&type=code : HTTP200 logged-out code-search page; zero displayed results is inconclusive because code search may require sign-in.

HTML receipts retained outside Git at `/tmp/padua-lanczos-frontier-l7/zhu-gh*.html`; hashes in evidence/l7-preparation.json. These narrow searches establish no nonexistence claim. No Zhu–Nakatsukasa implementation was pinned, classified or executed. No fulltext-based paper/literature fitting task is claimed. Conditional Franke adaptation in preregistration remains NOT RUN because no full paper was obtained.

## Retention

Small source-access metadata only in Git. External source and HTML downloads are regenerable by URLs, with byte sizes/hashes in evidence/l7-preparation.json; local artifacts are pending AC-selected long-term Padua archive delivery. No external-machine storage invented. Source retrieval itself is not an experiment or G4 replay.
