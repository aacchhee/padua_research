# PD-T436 — finite exact Hahn normality, N=4,...,64

ID kind: PD-T. Aliases: all 61 Hahn triangles; exact interior-divisor certificate.
Split from: none. Split into: none.
Depends on: [conditioning-normality-certificate.md](conditioning-normality-certificate.md),
the generic exact certificate applied below.

## Statement

For every integer N with 4<=N<=64, let M=N−1 and z_k=2k/M−1,
k=0,...,M. Put beta1=1, beta2=3/2, gamma=1 and

    w_(s,k)=(beta_s+1)_k/k! * (gamma+1)_(M−k)/(M−k)!.

Every mixed moment index (n,m) with n+m<=N is normal. Thus the NN map
and its local derivative in conditioning-local.md are defined on a
neighborhood of each of these 61 exact rational inputs.

## Definitions and assumptions

Normality is invertibility of the mixed moment matrix of PD-T286. The
weights are the exact rational PD-T290 Hahn inputs, not their floating
conversions. The theorem covers exactly the 61 stated sizes and both
measures. It makes no claim about other N or other Hahn parameters.

## Status by part

Overall status: PROVED — finite computer-assisted theorem, with exact
arithmetic, written reduction, compact essential evidence below, source
producer/checker code and a separate full independent execution. Developer
claim is published in the completed round2 output; mandatory Claude
reconstruction is completed in audit-01.md, priority2. Source and receipt hashes are below.
Candidate disposition: retained finite application of the standard
normality converse. The all-N Hahn-family theorem remains outside scope.

## Depends on

PD-T286; the separate PROVED generic implication in
[conditioning-normality-certificate.md](conditioning-normality-certificate.md).
That implication assumes no target-degree normality. Marginal positivity
is proved analytically there. No floating derivative table is a premise.

## Proof or evidence

The weights are strictly positive rational numbers and the nodes are distinct
rational numbers.
For each N, the exact scalar producer computes the C4 coefficients only
through degree N−2 and checks all N(N−1)/2 interior d values nonzero.
The generic theorem's degree induction then proves all normalities through
N: known degree k−1 systems determine the true d on degree k−2; the
identity h_(eta+e1,2)=d_eta h_(eta,2) and a bordered determinant prove the
next opposite-corner normality. No terminal d at degree N−1 is used.

Every one of the 43,676 exact checks passed. The table below commits the
61 check counts, exact-input identity and full exact coefficient-payload
identity. No bulk coefficient triangle is required to reproduce the proof:
the frozen rational input generator and producer recreate it exactly, and
the checker recomputes all nonzero tests and compares every digest/count.
The proof does not rely on approximate determinants or precision fits.

### Essential finite receipt

| N | Interior checks | Input SHA-256 | Exact coefficient payload SHA-256 |
|---|---|---|---|
| 4 | 6 | `e5558865cb6eef2913ee27622d251d05a614db7fc509418d9c11779863c55f12` | `d5ce13bbaf152d90dd2061aff211071fd7036351fec1ffe3b1a342aec8e885b3` |
| 5 | 10 | `e4e2c0452d5cd802449e09f87243ae9266281dbd6dac51c1de38f30158c0e6bb` | `b4988a004dd907b261aabd4f3f0a602161f0769fb1a87f702276117bae38a66f` |
| 6 | 15 | `3be4a94175845a8db88a16eb22f8ad0425b800b70d1c80888e4c36d5217185ea` | `0a2b42081e789ee18c072a175771c5da0e64cacdce05544d81d39b24c1cf8a68` |
| 7 | 21 | `f73147ec1c40cac795445d5e4804313923637823ac9954ff616284ec740a79c3` | `1000426eb8a2ae0db5f2414c5ec8be7beb7e34351a940f22acfdc9b7cb54f306` |
| 8 | 28 | `452dde0851f7bdd766176b8f554d60d40c7c63f676e43f796b4c1de8719c4af1` | `f57576ba25d9b2fe8da1bdf259d5125c54f9a8a6d8baac2d5c466d3b3eb1ddc8` |
| 9 | 36 | `5cd7fce27a54f36e65b118eccdd5eef1c29dd18ba87937a569715edc883c27f4` | `0792b8a135f6e6caeec5c9efc2587bd86e8429f02333bf2d6d78ad4b8d37e303` |
| 10 | 45 | `51b084dbcd0bf503c71b9462d8374c79e76e5c0eec20667d8a8efe5953a6bb3c` | `2e7375d1c189c62447ade27f7331171142248250d6d43a6a787c7d6a1ba64391` |
| 11 | 55 | `eb4f3ab4cd13cedeebfefa66e74713a5e708516716b53b233cfa00049e27d7b9` | `6ef8215e091123edf5fffb8f5884eab21388321ee174d892c44283e8089133d2` |
| 12 | 66 | `f95fb44fb4adeb29a25653f244d56c43ce0299650c037d08d10fee0d81b50336` | `f6bc5d5d9cc9245d91a33bf9b1fe65cc3d497a07cf7829e8041d48e611d57754` |
| 13 | 78 | `e41d4b5e1adb5cac2395689604a4c7b78d0fbcf66d96c2b2cd3593d501f46898` | `83a799d892e00955a0017e75e1bf25e36a002bd023968eba06762056c58bf1cd` |
| 14 | 91 | `35c6152fb0cdfff1a13e9f11165b652da7dd113d7319f018f3fa1e10132c5bd1` | `20d9b196caa54ff683d3ccd2e367f4f42291facaead3b731e41f3e2db2a34ab8` |
| 15 | 105 | `ce4ba94e59ab42d4bb04e7bd815e9cf929e1f6569d140163dfd865cf15715d81` | `b935b65445bb6bf8d4728e2c7ba07a0f0d69e50ed6237f5e8ce6c25a1cf07ed7` |
| 16 | 120 | `2d4e8883120041c0221408d62f103ff307fbbaf9946e2387df429dd9fd936482` | `8d5ce8460229bd24848972d256c9957fce2f2e3b11890b76d52609c3207cb353` |
| 17 | 136 | `c2116cacad3a40065bdc63bae21414c842bb67839f201165bc00ba077e9a04ee` | `ed5dc6979c688872a6100e41b7a4eab26042c9b3b3c69fc5ebf1f49867d9e7d0` |
| 18 | 153 | `f3d21047386edfeb764758a9c0ef85d1392a473c528ae86f01398b4f59321b0a` | `93f6771ccfe461bd7489804c0e46ef4fd4ec08a7bcd4565fa313169060e25241` |
| 19 | 171 | `0caff812b0122f01401f5a7c9d5f51e03d58e5baadeb36e7a9e1d2e9a0d1bd90` | `827d701236f1a59cec8acc44d70743b8a87d6f5411d0167b6447830847c5556e` |
| 20 | 190 | `b93eb2167ef13da2c3c2e820544544c14fff1e794d8b8ab4102810c7c87bae39` | `684a883205f8b85903dc38553cea18dd740d094c4e92304dd2fec83a782c80a0` |
| 21 | 210 | `cf998feea6f441e0162504735f1878a94f4b39f36968f6d4863991156fc4efee` | `0d9c2978fa8ba4b8b726e8f2e7767f0d26d5a67d01ebd4a0274f750351991928` |
| 22 | 231 | `545805ef8427ea811dbbcaa2ba2c0d5926cbc06e3e2022b39b0fd3751d3e84a2` | `c08b4663b43cd73b5c288b7a07555d13fe2b49ccbfb2cec06bbec0ba4fbc375a` |
| 23 | 253 | `4d95fe9e8e13c5e60b36ad28dd72d01b23e5b6986ab29645b5dd922e484ec0b1` | `4e56686d0b24bfa51ec8c90935196169bbb61da495f1c6e2cc11c65b0fb408b5` |
| 24 | 276 | `0fe9100b2fad839f38ed92e6b01ffb5f40d03028c12875187e35fdbede22afca` | `0d60c60ec34be0197e25cf779269b33dda791474f988cd807c2cd8825e736271` |
| 25 | 300 | `8c53357b307a981fe4f055b699239072948205213b6a7c3e4d30213c9be9fe52` | `1c6a47b8305cff572c446e1f1b4a23d6e857389c46c643e3e60bea92ae0043f4` |
| 26 | 325 | `b54fb6e32479a80355ad70fbcdd5e2c82125d13ebbd36d8e8778cd23aecc0d8a` | `e09227333b671f23ee18b2bbb027efcdf5b7f18e32c9258d69d25fa365cf10e1` |
| 27 | 351 | `2612eacb6b34d387e31dba6084f0da025656b9fbc543145e1ca515cefc516cda` | `a0c2715e0dc7878c044a5ea170f65e488a1929caef2d56c15615391ec384e282` |
| 28 | 378 | `bc097ec4513e817173b6bcf792914ec91aa2a7ef9779c961f077ba7459c2b8db` | `d044e3e4c7e87547f9a50ece4471f26c2fc67f7c227bcd9803507cdbce927e3f` |
| 29 | 406 | `01e3afa6d3e208916042aa40bce49b9114f31c5dff50a0332990c6c68f2ff943` | `7b0a1873ad5c28ae97f5c26ca69ad65d0b9282c92ba2565207411d7733dc3969` |
| 30 | 435 | `1a1cb1f409a700a028a5e2e1f926f235658eaca7aa4640d62b4b19a90c14902a` | `6aa83395f3b42ccd88ab0d70bebb551f24dac189eab5c7db95338d035765dc85` |
| 31 | 465 | `78e69c032a003510670a314cb2e5b3b31440a8de0d0dfa0252d7f890ff6f47b6` | `c1bf03d05430203a44e8a477664d2b87a719896df83a28d79ee22747dc70e89c` |
| 32 | 496 | `bacc69beb9e0ba2a5927752123b21020a1118d1d830d241cf9457cced6ab0a86` | `c3b109f607b01757de46cdd607aebb977b25fc763d1c4925631a32655c338a7a` |
| 33 | 528 | `f43bc7f9f933b575bfd76539c2561770745b1e0e25b49bf0e7eb60be7024072b` | `4f4e35c399f3db4614ca53fa65d28016bae8677220532aa50bd12978f38861ef` |
| 34 | 561 | `39ec18cb621a3b76a99f21935168e401bf23694b02c4835455b15f5ba30a8231` | `3509f0fcb008f3f8c719de8bed5865a10cce0e95b503904effbf5001b258bc5f` |
| 35 | 595 | `2f11a25e5f1c4c99473103a9eaf5a1448aa4414e118521d2d058e1abf5654021` | `222546abf23ca96f453f72acad03eba365f5f626891fc084bcfffa1c070fdba0` |
| 36 | 630 | `bd8ad64ad55309b91b03b2d457bc218924849ffa50eaa6c25a9249ac87650395` | `8d64d9ca37f9f90ce77d320e330a7b8fbda98a0d558e0479c1cf6e5015370631` |
| 37 | 666 | `7e7d431118f9d979ba451a889862646e1d939ed9554f5fd0fcd09c050a03798b` | `830686038eb15c1af35b2a192233f393a5b9ed8b4ee5f8407140d733ff84f76a` |
| 38 | 703 | `355d72797facb98d75b70b4192a991f3ccd592ee1d6a07681fe246e7a7ad05ef` | `e0772d5a4c7051a1174503768aa89792c56a10477e15107e2cd6a6562bf0babd` |
| 39 | 741 | `ec3f0674c2de044e756d9d74bf864c6c3aab00007c6daccbcddfcdc7dd77112f` | `4e3f7effa6bd0b877a06741d8d98db9f3413c98b4e178dc9a3e036c8fdbb452f` |
| 40 | 780 | `5c597e2ddbe5a046b2c3a6e7fdc0ae3a3eb2d526aec7b3b9d9cd2311ac722ddf` | `cb35f7df4e55cdfc3d3d7625a39b207d80e49146fce71e92b5c918280228e620` |
| 41 | 820 | `bb963398e5eff238686b07e5b647f27402603119da73278422ad2964145b4d0c` | `1b0267ce788465516f1a55b83d88bdfb6a54759e4e1700343a263d0f9dbb0482` |
| 42 | 861 | `a178520c5d29f835711abfc4d8993fc4abd64eae35d1c3ed09f3db943c051089` | `e8d8abc9178d5bce4f4ea85bc145bbb9f4571fca5db8d544dac224548966f668` |
| 43 | 903 | `f7658623ef6b716189aacc571a68cd4196c0ff73593a1b531ff17b9d1d1cc87c` | `a59abdd39e8c3fa8b7d1c4aaec18fb2f919b501162582a386cf9cd41d8266c94` |
| 44 | 946 | `ff8394d44b27c185eb09feba1110704812107df97a506c5cb53b5d3a8533cbce` | `63b71f710fdf2a63afc6ef327e2a44d125cbf285d8f360e363361b29ab415445` |
| 45 | 990 | `a597adb3c3698dadc78e0a2537ba869fa0f47bb146f0d6af5979ad5cf3dcb167` | `e67d975357fcac6f9694c6a95c9ef71c695b41111d12ab6f41f8e3e802eb721b` |
| 46 | 1035 | `87ce78baff1629a4533235f82f64078661b5c9a7340741eed9a64c9f436f9354` | `f13ef6abc4af52aec6dd431e2a39b3acc40be1c9f04eb08b41fd4fc880af3332` |
| 47 | 1081 | `bff28e0a5ad1b497ce2ce9618ef2ca6fde5f8ecef10d81cc5d7cca0f42c2dc13` | `6072dca90d967a57a28cc21bf27d55b2379e0d8152fe91fd46338e411ee56a17` |
| 48 | 1128 | `1894fd2878980d4e3bb7d08d357c1ba75ecec1d32ed57dbe690aa60af12f4f3d` | `a153b2483529f1beac99cd5b6097edb9d3617bdbbdc1e7d15b282945032a5944` |
| 49 | 1176 | `55e5c276e9f603f95ce0dea102e96b081be6f18b1e408ee4caa78b90687dd02e` | `918f41cfc6581accce6884bb898d1534c478a5fee9f6b48af317b18a205076ab` |
| 50 | 1225 | `808871002ebcf6539db152d34553b583e88f5f22a5ffabcc9ecdaf5e3303252c` | `11fe9788653725539157ddfe41447e18ba4d7a6beeeb4e8d0a6d63c8671ac609` |
| 51 | 1275 | `4b2c38d978c07164a6a03b2b837dbc2477cb2998a58bc8472fff0c8472bbc003` | `b088c7f5b0a381ed8d44b2719c2e8e3ec81e03359339ffd19bd773bb9a2fbbaf` |
| 52 | 1326 | `efd1fda1eca5dc8d907dd203f0ac7407778b53f9f41a393764ce6f255742afc5` | `d3909f758ef6dbe5bf1f465df8708f806e18038e3215cb4833f1e26d6992597f` |
| 53 | 1378 | `c9b29277f4b5f1296c9f9098e72e7ee3ca9dbca60f74e12b3da46156cfe4ce43` | `91b9a31c2827c95154e3e98f2cbcce0925706ccdd7b1efae679fb9ddd02a4305` |
| 54 | 1431 | `d84efac5652ceb65f43968835418dfc9ab2e9eee5a151df65ef20193cc3b1aa3` | `c33e8459d17871f7fee7c92d1c471c15b74ad57fa09d43c597454b3633559191` |
| 55 | 1485 | `05ae47a14e820a021e6359765fe63121a4297866adbe843f329a466e76e6c1ee` | `f35b23b1810edf2c46d961dc92df4edc3e797696e55bb7a27f57fb5bdf2dc2d0` |
| 56 | 1540 | `892e8d34680c34a786745d0f29008713d637fbe2377209082e8eda0765361992` | `30a4f9a3a78c46b053ceb75fa544768c603a68d1550908f6c3c373ed109b7844` |
| 57 | 1596 | `4d29b6a122c1d2b2f2ad02ee8c391c99e467d68673adc1ac2acd4fd3cdb30bc7` | `80e534b72f0f1f32c721cad1236b984e7f3aac2c0f94947d1c7ff69d33b4efc9` |
| 58 | 1653 | `cd00d7e6ed35fc797106cbc0fa0ffbe149deecef099731cebc16104f721d225f` | `b577e670d1a9819560b048ae896a35fbb55419d0c2ccecdc16bf86ec87fa632a` |
| 59 | 1711 | `5d8d5d8d55402378b91cac8ca134b6fafc02ccd1ab7c862aef45476205b471ec` | `289f24432c9f8221a33940cfadf24e781f52b670233172673307c78eddf1d50a` |
| 60 | 1770 | `25d37a3eb2856826c54c6b4479ffaee2b0806f003fbe1a378eeb870a0e5ed8f5` | `db30c4f52b1138e66daadfafc4084d977fabae3d1f18458ff110f3e14d28e8ed` |
| 61 | 1830 | `e2101a1aab43faa69b4555c07d0aa8c9eb2fad79d35b8ea8035fb4080a04c762` | `4b34a8890dc84f7dbec0404e60d2a9ad0d937449cd6f36c4a23c4852840efe1f` |
| 62 | 1891 | `06a9ae21468476da782358ae8c227aea21b9869a9dd38e5d5490a7fc82ec8928` | `0d4f8686f8f60c5edae2388e51b55fe9270b8b6f5cca49c0e430302f6cde80b1` |
| 63 | 1953 | `7407f8eb9ad3564e3b6df705f4aff6e05b563c2a3cc92c09eac65525ec5e34a6` | `5df5777af02e0350ee6e0c8905d463befffcc0b46d8603f13b3a4be8f81a0597` |
| 64 | 2016 | `cc7abbb4ae2add83d728ec56e71109905e602fdcd947a19a0e926c742c91ecef` | `03acf79d9ac7eb9dce5fb95f4608f75d82440941b867923898799f001eb34eb2` |

## Checks

Producer: code/conditioning_exact_normality.py. It uses fractions.Fraction
for every scalar operation, checks positivity/distinctness and Fraction types,
then checks every d nonzero. The exact generic scalar graph is imported from
conditioning.py; only its zero/one constructor is replaced in that process.
Checker: code/conditioning_verify_normality.py recomputes the finite result
and compares all 61 counts/input hashes/payload hashes to this table.

Source hashes:

- `conditioning_exact_normality.py`: `795e1c1114587d5aa5066f278cb76e7bf08356402d78a5ce03fe4f8910aa5f3c`.
- `conditioning.py`: `11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c`.
- `c4_float_baseline.py`: `9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8`.

Actual developer command:

```bash
python3 topics/nn-mop-stability-20261105/code/conditioning_timed.py /tmp/conditioning-exact-hahn-full.time.json topics/nn-mop-stability-20261105/code/conditioning_exact_normality.py --family hahn --sizes {4..64} > /tmp/conditioning-exact-hahn-full.json 2> /tmp/conditioning-exact-hahn-full.log
```

It returned exit 0: 61 passes, 43,676 nonzero interior checks. Raw receipt
`/tmp/conditioning-exact-hahn-full.json`: 24,905 bytes, SHA-256
`af758c00c3bc5d5c6b34d53d5355e307b3e2868996c0e5752849940452e00b4e`.
Wall time 5.2859s; user CPU 4.2151s; system CPU 0.0127s; peak RSS 19,052KiB.

A distinct Astra-high worker independently read the reduction and executed
the complete 61-size producer separately: [independent-checks-02.md](../independent-checks-02.md).
All scientific fields match the developer receipt after removing only elapsed
timings. Its raw receipt is 24,906 bytes, SHA-256
`aa880df02ce17f664aad81412a78d2c8e7f743534774973ed3c5996b39cf8d69`.
For N=64, min exact |d| is 524/10614807, and the coefficient digest is the
last table row. The earlier independent exact moment derivative checks at
N=3,4,6 separately corroborate the scalar graph on small inputs.

The separate compact-receipt checker was also executed historically, with
source at commit `4e87fc0a771fc13c6d5791f0f4c2e746e4eb9a71`. The command
below identifies that historical execution; the verifier at the same path
has since changed. Current identities are in
[evidence-manifest.json](../evidence-manifest.json):

```bash
python3 topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py > /tmp/conditioning-normality-receipt-check.json
```

It returned PASS for all 61 sizes and 43,676 exact checks. Checker SHA-256:
`f9403f537c67a64cadaedd376d430e960b21ab6b806be2092df824a8ba61e9db`.

## Sources

PD-T290 supplies the source input convention; no new literature theorem.

## Scope

This is a finite exact theorem, separate from the MEASURED floating condition
numbers. It neither proves all-N Hahn normality nor supplies a stability bound.
Raw timings/logs are regenerable and remain outside Git; the compact table and
rational generating/checker code are the essential finite evidence.

## Open items

An all-N Hahn-family normality proof is not needed
for the stated finite theorem and is not implied by it.

## History

2026-11-05 D1 round2, Codex, requested gpt-6.1-sol xhigh. Backend metadata
is not independently exposed. Source/rules 823cf6a; development checkpoint
f75964bd71336aee2a05f4ebb39eb31215be360a. The coordinator publishes this
file with the source/checker and essential receipt at the next boundary.

2026-11-06, response to audit-01 MINOR1/12: explicit runtime checks replace removable asserts; the verifier now enforces all three code pins. The producer pin is updated here in the same reviewed commit. Statement, 61 exact inputs, counts and coefficient payload fingerprints are unchanged. Completed independent certification: audit-01.md, priority2.

The historical Nov5 raw receipt/timings above used producer SHA7aa4115143a51bd3abcea50abd4ea7b8de9a7507bea711ca7e19ab662a2be24a. The current pin changes only input/type guard checks; all 61 exact payload fingerprints remain unchanged. The response verification uses the new pin and is recorded in response-01.md.

## Identifier mapping — 2026-11-06

Final identifiers use the permanent topic reservation; the provisional labels remain aliases:

- `PD-T?nn-mop-stability-codex-D1-05` → `PD-T436`.
