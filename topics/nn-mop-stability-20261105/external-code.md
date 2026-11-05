# External-code provenance and G5 access state

2026-11-05, Codex D7 developer, dispatched gpt-6.1-sol medium.
Rules/source `823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1`.
Status: **BLOCKED — source bytes unavailable; no external comparison run**.

## Exact external source identity

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

## Actual access checks

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

## Runtime feasibility

`command -v octave` and `command -v octave-cli` found neither executable;
`dpkg-query -W octave octave-common` found no installed packages.
`apt-cache policy octave` had no package entry and warned that an apt
configuration file was unreadable. UID is 1000. Default apt sources point
to snapshot.debian.org; there are no usable local package indexes for Octave.
Installation was **not attempted**: once source access was concretely blocked,
the coordinator deferred installation. It remains PENDING, not proved
impossible. Debian mirror connectivity works with the enabled network route;
a later authorised local package setup may be feasible.

## G5 reproduction ledger

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

## Runs needed (not executed)

Once the same URLs are policy-authorised and reachable, suggested fetch:

```sh
curl --fail --location --output /tmp/nn-mop-stability-supp_materials.zip https://epubs.siam.org/doi/suppl/10.1137/25M1770965/suppl_file/supp_materials.zip
sha256sum /tmp/nn-mop-stability-supp_materials.zip
unzip -l /tmp/nn-mop-stability-supp_materials.zip
```

An exact Octave driver command cannot honestly be fixed until the archive is
read. Do not invent entry-point arguments or claim a completed compatibility test.
