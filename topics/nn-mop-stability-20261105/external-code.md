# External-code provenance and G5 access state

2026-11-05, Codex D7 developer, dispatched gpt-6.1-sol medium.
Current response check: 2026-11-06; see the dated addendum below.
Rules/source `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`.
Current status (2026-11-06, after supplied-source run and Codex audit): **G5 reproduction gate PASS (one configuration, Octave 8.4, to the decade); large-N variation measured; topic-metric comparison not yet run**. Earlier access/runtime observations below are historical, superseded by the current addendum.

## Original requested external source identity (historical)

- Requested repository: [Leuven IEP-MOP](https://gitlab.kuleuven.be/numa/public/IEP-MOP).
- Alternative located through the [publisher's supplementary-material section](https://epubs.siam.org/doi/10.1137/25M1770965): [supp_materials.zip](https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip).
- Git commit: **unavailable, not pinned**. Default branch: **unverified**.
- Archive/file SHA-256 and file list: **unavailable; no bytes fetched**.
- Local third-party checkout/archive: **none**. Nothing third-party is to be committed.
- Paper: [DOI](https://doi.org/10.1137/25M1770965), [journal page](https://epubs.siam.org/doi/10.1137/25M1770965), [arXiv v2](https://arxiv.org/pdf/2506.19796v2).

The publisher lists an approximately 993 KB ZIP, including the named solvers,
experiment_Hahn_Kravchuk.m, nodes_weights.m and multiprecision variants.
This is catalogue metadata inspected on the publisher page, not code inspection.
The ZIP's identity cannot be substituted for a Git commit without recording
its actual hash and file list after download.

## Historical access checks (2026-11-05)

Default-sandbox curl could not reach inherited proxy:8080 (exit 7).
Network-enabled execution, preserving proxy and CA, then established the
concrete policy blocker. Exact commands (both actually executed):

```sh
curl -sS -I --connect-timeout 5 --max-time 15 https://gitlab.kuleuven.be/numa/public/IEP-MOP
curl -sS -I --connect-timeout 5 --max-time 15 https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip
```

Each returned `HTTP/1.1 403 Forbidden` from the CONNECT proxy, curl exit 56.
The tool calls used `sandbox_permissions:with_additional_permissions` with
`additional_permissions.network.enabled:true`; no proxy variables changed.
The same enabled network route to https://deb.debian.org/debian/ returned 200.
The environment status was current, running, and policy enforced/restricted;
its effective allowed-host list excludes GitLab Leuven, arXiv and SIAM.
No direct route, alternate proxy, credential alteration or new plugin was used.

The supported web connector accessed the SIAM landing page and arXiv PDF.
It could not open the GitLab project, raw README, master commits, lowercase
project path or API project endpoint. Clicking the publisher's actual ZIP
link resolved the URL above but returned `Unsupported content-type:
application/zip` (400). Searches for IEP_CORE GitHub, IEP_KRYLREORTH
nodes_weights and experiment_Hahn_Kravchuk.m found no usable mirror.
That bounded search does not establish that no mirror exists.

## Original runtime feasibility (historical)

`command -v octave` and `command -v octave-cli` found neither executable;
`dpkg-query -W octave octave-common` found no installed packages.
`apt-cache policy octave` had no package entry and warned that an apt
configuration file was unreadable. UID is 1000. Default apt sources point
to snapshot.debian.org; there are no usable local package indexes for Octave.
Installation was **not attempted**: once source access was concretely blocked,
the coordinator deferred installation. It remains PENDING, not proved
impossible. Debian mirror connectivity works with the enabled network route;
a later authorised local package setup may be feasible.

## Original G5 reproduction ledger (historical)

No source was executed; no paper configuration or accuracy was reproduced.
G5 is **BLOCKED**, neither PASS nor a numerical mismatch/KILL. Octave support
and MATLAB/Advanpix compatibility are untested. No claim of an equivalent
local Python implementation counts as reproduction of these external codes.

When source access is available, first fetch the actual archive/checkout in
local temporary storage and record commit (if Git), SHA-256, byte size and
complete required file list. Inspect licence and actual experiment driver;
record any Octave adaptation as a separate patch and hash. Select one original
family/N, node scale, weight convention, solver option, reference precision,
error norm and paper ordinate **before** running. Only then reproduce the
paper's accuracy level and consider conversion to the whole NN triangle.
A lone step-line recurrence must not be said to determine all NN data without
the extra shifts/boundary data required by PD-T289/FHV.

## Originally proposed retrieval steps (historical)

Once the same URLs are policy-authorised and reachable, suggested fetch:

```sh
curl --fail --location --output /tmp/nn-mop-stability-supp_materials.zip https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip
sha256sum /tmp/nn-mop-stability-supp_materials.zip
unzip -l /tmp/nn-mop-stability-supp_materials.zip
```

An exact Octave driver command cannot honestly be fixed until the archive is
read. Do not invent entry-point arguments or claim a completed compatibility test.

## 2026-11-06 response access check — historical source-retrieval block

AC's retrieval and execution authorization is recorded once in
[LOG.md](LOG.md) (the
2026-11-06 canonical decision entry). Authorization does not change the active
runtime policy. The current Codex runtime has current observations and an
**enforced restricted package_managers preset**, with no custom allowed hosts;
GitLab Leuven, SIAM and arXiv are excluded. It differs from the Claude personal
environment described in handoff04. The cloud plugin exposes status and
read-only diagnostics here, with no callable configuration mutation workflow.

At 08:25:51 UTC, fresh enabled-network GET requests to the exact GitLab project,
SIAM supplement ZIP and arXiv HTML all received proxy CONNECT `403 Forbidden`,
with curl `--fail` exit **22**, `http_code=000` and zero downloaded bytes.
The enabled-network Debian control returned HTTP 200 and 6153 bytes. Proxy and
CA settings were preserved. These are current runtime policy refusals, not an
observed Cloudflare challenge or an upstream reset. No source was obtained.

The supported web connector read the arXiv HTML and publisher catalogue. GitLab
returned only a project title/Loading shell; raw README probes (main/master),
master tree, recursive repository API and a raw IEP_CORE.m probe were
inaccessible. The publisher's actual ZIP link returned `400 Unsupported
content-type: application/zip`. Bounded web and GitHub connector searches found
no usable mirror. The official Momentum software page's “github” label points
to the same GitLab project. These searches do not prove no mirror exists.

Fresh `command -v matlab`, `command -v octave` and `command -v octave-cli`
checks found no executable. No installation was attempted with source retrieval
blocked; Octave installability and toolbox compatibility remain untested.
**G5 remains BLOCKED by current runtime source retrieval**, not by absent AC
authorization. No source configuration, solver, paper accuracy or topic metric
was executed. The original paper-configuration-first gate remains in force.
Exact commands, observations, receipt hashes and remaining work are in
[response-01/g5-access.md](response-01/g5-access.md). No third-party source,
text or PDF is added to Git, and no storage cleanup was performed.

## 2026-11-06 supplied archive, execution and independent audit

**G5 reproduction gate PASS (one configuration, Octave 8.4, to the decade); large-N variation measured; topic-metric comparison not yet run.**

AC supplied IEP-MOP-main.zip:1,020,330 bytes, SHA256`cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`, MIT licence. Its Git revision is unknown; the archive hash identifies the exact supplied bytes, not a verified remote branch. It contains27 regular files/33 entries including directories. Complete per-file identity inventory: [audit source inventory](audit-g5-01/source-inventory.json). Executed source pins and the paper-reference source identities are in [development receipt](g5-run/README.md); third-party source/data remain outside Git.

Claude's headless Octave8.4 driver preserves the original experiment formulas, running both families over paperN5..30 (N+1 nodes). The selected Krawtchouk paperN10 IEP_CORE case gives1.772147e-9 against reported6.851191e-10, log10ratio+0.413: PASS under the fixed decade rule. This is a step-line matrix2-norm measurement, distinct from this topic's NN fieldwise metric. No all-size/platform reproduction or stable algorithm is established.

[Independent Codex audit](audit-g5-01.md) inspected every executed source file and reran all52 cases with isolated Octave9.4/reference BLAS on Debian13: gate2.691214553706643e-10, log10ratio-0.4058, PASS; full tables differ by platform. The auditor cannot fetch the arXiv source bundle (CONNECT403), so direct paper-data/hash verification and cmp.py against that bundle remain review only/unresolved. No source-access block is inferred for the supplied archive. No contact/bypass/cleanup. Remaining work: the separately scoped topic-metric comparison with the required path/boundary conversion; MATLAB/Advanpix and exact closed-form-reference checks are not claimed.
