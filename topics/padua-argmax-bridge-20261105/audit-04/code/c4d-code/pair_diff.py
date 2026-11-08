import tarfile, json, sys, re
tf = tarfile.open(sys.argv[1], "r:gz")
def get(n, role):
    for m in tf.getmembers():
        if m.name.endswith(f"jobs/{n}/{role}/essential-receipt.json"): return json.load(tf.extractfile(m))
for n in (41, 160, 300):
    a, b = get(n, "produce"), get(n, "verify")
    def walk(o, p=""):
        if isinstance(o, dict):
            for k, v in o.items(): yield from walk(v, p + "/" + k)
        else: yield p, json.dumps(o)[:80]
    da, db = dict(walk(a)), dict(walk(b))
    diff = [k for k in set(da) | set(db) if da.get(k) != db.get(k)]
    print(n, "top keys:", sorted(a.keys())[:8], "| differing leaf paths:", len(diff), sorted(diff)[:6])
