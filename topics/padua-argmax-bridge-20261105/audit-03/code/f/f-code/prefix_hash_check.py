#!/usr/bin/env python3
"""F-audit: check that each currently checked-out F file begins with the exact
frozen bytes recorded in the independent-check tables (prefix preservation).
Read-only. Usage: python3 prefix_hash_check.py <topic_dir>"""
import hashlib, pathlib, re, sys
topic = pathlib.Path(sys.argv[1])
rows = {}
for rv in sorted(topic.glob("independent-checks-F*.md")):
    for line in rv.read_text().splitlines():
        m = re.match(r"\|\s*((?:theory|ideas|attempts)/F\d\d[^|]*?)\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{64})`", line)
        if m:
            rows.setdefault(m.group(1), set()).add((int(m.group(2)), m.group(3), rv.name))
for path, recs in sorted(rows.items()):
    data = (topic / path).read_bytes()
    for size, h, rv in sorted(recs):
        full = hashlib.sha256(data).hexdigest() == h and len(data) == size
        pre = hashlib.sha256(data[:size]).hexdigest() == h
        tail = data[size:].decode(errors="replace")
        heads = re.findall(r"^## .*", tail, re.M)
        print(f"{path:48s} frozen={size:6d} now={len(data):6d} full={full!s:5s} prefix={pre!s:5s} [{rv}] appended={heads}")
