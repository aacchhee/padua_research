#!/usr/bin/env python3
"""Verify cited byte-prefix SHA256 identities of the E14 global320 premise chain
(read-only).  Auditor: Claude Opus 5.5 xhigh.  Usage: python3 -I prefix_hashes.py <topic_dir>"""
import hashlib, sys, os
T = sys.argv[1]
cases = [
    ("theory/E14-assembly320.md", 2439, "d9be2ce468d35f1377829f83560d807b38ec3841689c8922aae200b89fac0f4a"),
    ("theory/E14-assembly320.md", 11628, "b348ec55ee8be86abc9b025be2f9f134bc6d3ba29692c8dee441ea539b3a15e6"),
    ("theory/E14-halfnear320.md", 8865, "b77c5f661f51a94c8d809dd853e4fb64304178ccd8c90d3fca3e6e1bed119364"),
    ("theory/E14-outer320.md", 5565, "17baa09b52687f0fe2ac5b1ecdf2a42094b445a2013d32278c268da490b809fc"),
    ("theory/E14-wide-signed-outer.md", 14318, "c7aeba3d6080f16cc8016e83949f27d6f9de6d36793d9a03cc4c5d171528e8a8"),
    ("theory/E14-annular320.md", 8402, "1ddf2e7cdbf688ae74a3e9ebe2afba133d7bcfc55a1c0e5ce0664680028e363e"),
    ("theory/E12-corner256.md", 9921, "586c4e07bf683b3a3cb7913666a51f3541b9c0c6fa484dd12a45890b56b3639d"),
    ("theory/E13-joint-radius-outer.md", 15350, "d78a57c047853c1b57cd2153d190d991cb9a7ed961cd09ef9db709274a181715"),
    ("independent-checks-E14-global320.md", None, "25529c8a5ad54111a679680d916c4d6ae76ad976edb528c042b06366dc50d3f2"),
    ("independent-checks-E14-global320.md", 19661, "2f390ef7c5f75f16c60bf72444d5b06a22af9b367b8cde7cb5a30d085a46b918"),
    ("independent-checks-E14-wide-signed.md", None, "d0c3699f97e34c43725b3276bb5585d4a9ccf477cb56413058bb8fd2ff55a266"),
    ("independent-checks-E12-corner-frontier.md", None, "b7436e8f4c5f2d6c1e7c2fc0d7313c1f136648a489cdfd0cee3e8ef71e97df2a"),
]
bad = 0
for path, nbytes, want in cases:
    p = os.path.join(T, path)
    data = open(p, "rb").read()
    blob = data if nbytes is None else data[:nbytes]
    got = hashlib.sha256(blob).hexdigest()
    ok = got == want
    bad += (not ok)
    print(("MATCH " if ok else "MISMATCH ") + f"{path} prefix={nbytes if nbytes else 'full'} size={len(data)} got={got[:16]} want={want[:16]}")
sys.exit(1 if bad else 0)
