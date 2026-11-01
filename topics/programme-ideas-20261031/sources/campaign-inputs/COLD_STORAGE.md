# Cold-storage manifest — programme-ideas-20261031

Response-01 (audit-01 A8), 2026-11-01, claude-opus-5-5. Location agreed with AC for this campaign family: `C:\Users\andreyac\Downloads\padua\cold_storage\<slug>\` (Padua-specific; other topics use sibling folders). Only the file below was actually delivered; it was written through the desktop bridge and read back, and the read-back bytes match the SHA-256 below.

| File | Actual storage path | Bytes | SHA-256 | Source commit | Frozen generating command | Script blob IDs | Checker command / result |
|---|---|---|---|---|---|---|---|
| `programme-ideas-20261031-inputs-snapshot.zip` | `C:\Users\andreyac\Downloads\padua\cold_storage\programme-ideas-20261031\programme-ideas-20261031-inputs-snapshot.zip` | 369196 | `7e9b349282374630199c95dc362aeb3c4d2d64e231233a1511490ca6dfe2f5bc` | not a repository artefact: snapshot of the orchestrator's read-only input mirror `/home/claude/inputs/padua/` (mirrored from `Downloads\padua` on 2026-10-31) | `cd /home/claude/inputs && TZ=UTC zip -X -q -r inputs-snapshot.zip padua/RESULTS.md padua/research_notes` | — (no script) | read-back via the bridge and `sha256sum`: identical (2026-11-01) |

Why not committed: `RESULTS.md` and `research_notes/` are AC's private working notes; they contain page-level quotations from third-party papers and mappings of the private bttb-research repository, which the public repository must not carry.

### Members of the snapshot (bytes, SHA-256)

| Member | Bytes | SHA-256 |
|---|---|---|
| `padua/RESULTS.md` | 13399 | 4464ff97e2a5975b13698ce859695f3ef53c1dc61d99fea26c92a3307310e973 |
| `padua/research_notes/Open problems verification/ingest_OP_computation_papers.md` | 34158 | 831962df32c4e5abd0ead4e75b0d12eb3a798306046a736bd3e66adefa6e87a9 |
| `padua/research_notes/Open problems verification/ingest_nodes_cubature_papers.md` | 32364 | 92e7a80e5420c1c4ff2e6e9d282e2fab4e643a7bae0f5c3a8125d20a3c22482d |
| `padua/research_notes/Open problems verification/verify_algorithmic_problems.md` | 25428 | 3ba6d85b125245a4b68ea8247e5c92be5cf2bfdfd59d5829602216790eadf66d |
| `padua/research_notes/Open problems verification/verify_padua_problems.md` | 21089 | 6da28785aa7d96a1b1132d7acf3f304fd0af2982954670730d34f02043baed71 |
| `padua/research_notes/Open problems verification/verify_remaining_problems.md` | 24322 | 14d503ec9ea8db0b4b02bf1808ed40c75db4222f4f1c11811ee0dde975bab92b |
| `padua/research_notes/Recent open problems 2023 2026/adv_F1_F6_F3.md` | 26606 | 17a78964b3b220149e6a203688dccc8b981ed5c63f0e921682381049bbe5fa50 |
| `padua/research_notes/Recent open problems 2023 2026/adv_F2_F5_F10_F9.md` | 23881 | 9d4a80a98316fff4f650f9027e53451eecd80b66cae8d1f4164ee4a41dab608d |
| `padua/research_notes/Recent open problems 2023 2026/adv_F7_F8_F11_F12_F4.md` | 25078 | 47b14878d3bad08a355e3409342a03220f016a78de5b539a267453318c62e235 |
| `padua/research_notes/Recent open problems 2023 2026/adv_exact_X1_X3_X7.md` | 25284 | a861f0096be72ed9e19b8d2d628df487d70b019704fe1e042312e47cbb5c2a0d |
| `padua/research_notes/Recent open problems 2023 2026/adv_exact_frontier.md` | 29329 | d153bdf0a45d6eb8366806e984347d15de1f2f5f440100cf1e3fbfe388de90d0 |
| `padua/research_notes/Recent open problems 2023 2026/bttb_repo_exact_mapping.md` | 34485 | c664c6ce66fa960edc6b5f36e9b554a539096561088474ffeeee54e58f8aaa82 |
| `padua/research_notes/Recent open problems 2023 2026/bttb_repo_numeric_mapping.md` | 23985 | 7c03d5af7e699fc35e6b26c2ec7b965e237076a20072d6f4cfcb194076015bad |
| `padua/research_notes/Recent open problems 2023 2026/exact_arithmetic_catalog.md` | 45243 | 9329d7aaf127f76e571d5c14cbc447e09b0e269a7e235d642a676e81f9cfb527 |
| `padua/research_notes/Recent open problems 2023 2026/exact_arithmetic_ideas.md` | 35738 | 9cca484b4185fd544a1371dff2ee5b0379e9c5b1cd86bf5ffbc3e217b202f007 |
| `padua/research_notes/Recent open problems 2023 2026/finite_field_padua.md` | 18926 | e874d6a5559aebaaec3ea4f7d71b38c5605d4a45057bd838db0540eb879e562f |
| `padua/research_notes/Recent open problems 2023 2026/ingest_classic_papers.md` | 38342 | 14aaa879bcbe7e011e7c06d7e7b3ecb145d23b54972acb04a870ecb10becda84 |
| `padua/research_notes/Recent open problems 2023 2026/ingest_humet_thesis.md` | 27675 | 4b70010c850276c1d84a2ec1e7b0ace677984bec49d25247f786c00f2cf6581a |
| `padua/research_notes/Recent open problems 2023 2026/recent_adjacent_areas.md` | 38153 | 3078592798e673e9a39976853a5e0555d704c8435d10fefbb12244bcd89898b3 |
| `padua/research_notes/Recent open problems 2023 2026/recent_exact_arithmetic.md` | 29766 | b2d316372db12d7c015f7a16521b25b6d24f6acbc8de7bb0850f1cc54ecb2415 |
| `padua/research_notes/Recent open problems 2023 2026/recent_multivariate_NLA.md` | 36195 | 03a390b5342d4c4fa81cb3b1f34c17d6e9892aca8942e2d26a779ca64e77a7cd |
| `padua/research_notes/Recent open problems 2023 2026/recent_padua_cubature_theory.md` | 35786 | d29351d4955d8eb03aff783e08ad135de871a868baa1a224dcc7b63355f7adb9 |
| `padua/research_notes/citation_tracking.md` | 52067 | 36feabbd00e5945b40e298d41cb39e66d6bc1b664c91bd87577084c0b7429205 |
| `padua/research_notes/discrete_multivariate_OP_computation.md` | 56037 | aeae97fe5b533d04e31184d2e881f32f719011de1184ac06eaed4707b13f3575 |
| `padua/research_notes/optimal_point_sets.md` | 65588 | b93cde20bd5b6ac36e7d20652ab01dff84b0e62a2b4758a44716d24c4bf568fa |
| `padua/research_notes/padua_algorithms_applications.md` | 52025 | ac32689195bfe1e5944380a1c0166de8f2a930efdf230c434904561ef118507d |
| `padua/research_notes/padua_lissajous_theory.md` | 57792 | b4bd325eb765eca81e023dad84ef259abc01c68cfa6ef952ba4b0a1127ec97db |

`padua/RESULTS.md` above is the version read by the campaign agents (13399 bytes). The live `Downloads\padua\RESULTS.md` has since been appended by later sessions; its earlier bytes are those of this member.

### Local papers read by the agents (not stored here)

The paper PDFs are AC's own copies in `C:\Users\andreyac\Downloads\padua\papers\` (mirrored to `/home/claude/inputs/papers/` with `MAP.txt` mapping file names to citations). They are third-party works and are neither committed nor copied to cold storage; the hashes identify the exact files read.

| File | Bytes | SHA-256 |
|---|---|---|
| `0612024.pdf` | 2520478 | 40229e796e6234edbdb9266132e4cdad96cc8c5a1e58c693a53bbac5c0dc158a |
| `1-s2.0-S0377042718304035-main.pdf` | 470547 | 849a4ea4672871ccc873b41d7f3dc6d55f409134ba54dbec2c6aa7ba83cccf4e |
| `214408.214410.pdf` | 791633 | 8c8b1dcca83600e1caf3c15916583648e785f2b6d23925c097e702393ea2edba |
| `A_1021907210628.pdf` | 456509 | ec445fcf156f20c3dfd44e65b9b12179dfec2c8bcdf0b756df53015c3415ec6a |
| `Compression of Multivariate Discrete Measures and Applications.pdf` | 910650 | 965fbea8e0318610818503d944012bbc5bc0be6242f28fc4fa05bff3fcb89e64 |
| `MAP.txt` | 1687 | cdc7554a5f4f89ffa42538215b970ec7f849450de8d7c16c413bd75ac71e46f4 |
| `S0002-9939-2021-15414-2.pdf` | 225594 | 9ccacb4e7b2f02af9266ce10f6407d2489037f72fbd573f419e26e8d7eee31b9 |
| `TW629.pdf` | 2916708 | 4914ca09cc60d9b3e100ba0e3e5559765fc70f7e759329c5ee0a72d66ccfcbce |
| `s0036141092237200.pdf` | 1156316 | dd9a2f5aab5f27dd9d82af30d112b3bb009e7d25cbfaaa0e33287638fe5e92cf |
| `s0895479800398468.pdf` | 275502 | 69b995f91a5e3ae89d1819eee0743a243fdb049ae103c5cdad5d77c8c92ef709 |
| `s0895479801384561.pdf` | 1435908 | 932449435b6324806ea8c4c39f8167ac2ae50a868ec63fde581c8614d3d704d6 |
| `s10543-010-0300-6.pdf` | 654703 | 010779e3ae03794260741148f65c905d8042ab37fd6e60887c226eda44967560 |
| `s11075-007-9112-4.pdf` | 426755 | ecceaaa23bb74f136e7f8ec085cc2fbbd5abd7799d600b76d983e392376fa1de |
| `s11075-010-9392-y.pdf` | 1200986 | 2c2dc4f0b4aacf59e2bad7b7a3daf5c485d7e77249e216c168d7e5deb51dd371 |
| `s11075-018-0592-1.pdf` | 552412 | ab76c7defda4fc60c62161278ec1aa75b8f88370ab4862741390a8265198b584 |
| `thesis_Humet_v01.pdf` | 16072846 | 31282df409428c21714333db5bcd3e8deab4622dfb6a7d57dbb0ef2c19c6241e |

## Committed checker output

`provenance.json` (this directory, generated by `provenance.py`) identifies every other input file the agents read: 164 files of the input mirror outside `papers/`, `web/` and `padua/`; 159 are byte-identical to blobs in this repository's history (commit and path recorded per file), and the remaining 5 are the campaign prompt files committed in this directory by response-01 (`CAMPAIGN_CONTEXT.md`, `GENERATOR_COMMON.md`, `ADVERSARIAL_COMMON.md`, `DECISIVE_COMMON.md`, `BRANCH_SNAPSHOT_NOTE.md`). The three source reports are in `../` with `../SHA256SUMS.txt`.

## Regeneration and handoff

The zip cannot be regenerated from the repository. To verify: stage the stored file and compare its SHA-256 with the table; unzip and compare member hashes.

## Retention

Retain at least until the programme-ideas PR is merged or closed by AC and any follow-up project (proposal-1) is decided; custodian AC. No expiry is set by the developer.

## Retrieval

On AC's computer at the path above (requires access to that machine or the desktop bridge). Verify the retrieved bytes with `sha256sum` against this manifest.
