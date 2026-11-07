import json, sys
def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from flat(v, f"{p}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from flat(v, f"{p}[{i}]")
    else: yield p, x
a = dict(flat(json.load(open(sys.argv[1])))); b = dict(flat(json.load(open(sys.argv[2]))))
diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
print(len(a), len(b), "differing fields:", diff)
for k in diff: print(" ", k, "| committed:", a.get(k), "| rerun:", b.get(k))
