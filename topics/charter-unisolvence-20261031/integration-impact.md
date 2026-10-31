# Scientific-checkpoint integration impact

U0 original reviewed proof content is retrievable at `4f3d247c64d8c74a923b50f5ff575f83b5401cb8`; U1 proof/checker at `d5a5efbc6228ea21ef38b438ef976260f90ea83e`. Independent reports pin their own exact pre-integration file hashes. Historical staging paths and provisional IDs in those reports are intentional provenance, resolved through ID_CROSSWALK.md.

The orchestrator moved staging theory into tracks/unisolvence/theory at PR preparation, copied the independent code-bound proof to its canonical home, and substituted exact IDs using final-id-map.json. integration-impact.json records original/final SHA256 and source commit for all13 theory files. An actual byte comparison verified each canonical file equals its original bytes after those ID substitutions and the explicitly listed editorial replacements. Editorial replacements expand old local suffix references to final IDs and reconcile completed supplementary checks with pending Claude acceptance; their exact old/new strings are in the JSON. No mathematical statement, proof step, parameter range or epistemic status was changed. The independent original reports/checkers/outputs remain untouched.

A canonical file's old phrase “independent audit pending” describes the required acceptance stage; current supplementary Astra results are recorded in tracks/unisolvence/AUDIT_LOG.md. Claude's distinct cross-agent audit remains PENDING. This impact check does not replace it.

Retrieve an original file using `git show SOURCE_COMMIT:OLD_PATH` and verify its before_sha256; apply the explicit mapping and listed editorial replacements in order, then compare after_sha256. This also resolves frozen-hash inventories whose old staging paths no longer exist in the final tree.
