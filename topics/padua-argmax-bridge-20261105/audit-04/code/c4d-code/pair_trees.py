# data-only: compare primary (produce) and fresh (verify) certificate trees/keys in the original return
import tarfile, json, sys, re
tf = tarfile.open(sys.argv[1], "r:gz")
want = {}
for m in tf.getmembers():
    g = re.search(r"jobs/(\d+)/(produce|verify)/essential-receipt\.json$", m.name)
    if g: want[(int(g.group(1)), g.group(2))] = m
same_tree = same_keys = same_vals = total = 0
def find_cert(o):
    if isinstance(o, dict):
        if "tree" in o and "S_upper_rows" in o: return o
        for v in o.values():
            r = find_cert(v)
            if r: return r
    return None
for n in sorted({k[0] for k in want}):
    if (n, "produce") not in want or (n, "verify") not in want: continue
    a = find_cert(json.load(tf.extractfile(want[(n, "produce")])))
    b = find_cert(json.load(tf.extractfile(want[(n, "verify")])))
    if a is None or b is None: continue
    total += 1
    same_tree += a["tree"]["preorder"] == b["tree"]["preorder"]
    ka = [(r[0], r[1]) for r in a["S_upper_rows"]]; kb = [(r[0], r[1]) for r in b["S_upper_rows"]]
    same_keys += ka == kb
    same_vals += a["S_upper_rows"] == b["S_upper_rows"]
print("pairs:", total, "identical trees:", same_tree, "identical S keys:", same_keys, "identical stored S uppers:", same_vals)
