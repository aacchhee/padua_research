import importlib.util, json, sys, hashlib, base64
from pathlib import Path
B = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("am", B/"src/topics/padua-3d-20261106/code/artifact_manifest.py")
am = importlib.util.module_from_spec(spec); spec.loader.exec_module(am)
def invert(m):
    rows = {}
    for g, entries in m.items():
        for k, (size, h) in entries.items():
            p = f"code/{k}.py" if g == "code" else f"evidence/{k}.json" if g == "evidence" else k
            assert p not in rows, p
            rows[p] = (size, base64.b85decode(h).hex())
    return rows
for c in sys.argv[2:]:
    top = B/"hist"/c/"topics/padua-3d-20261106"
    saved = json.loads((top/"evidence-manifest.json").read_text())
    dec = am.decode_manifest(saved)
    fresh = {r["path"]: (r["bytes"], r["sha256"]) for r in
             (am.identity(p, top) for p in sorted(x for d in ("code","evidence") for x in top.joinpath(d).rglob("*") if x.is_file() and "__pycache__" not in x.parts and x.suffix != ".pyc"))}
    inv = invert(dec)
    own = B/"hist"/f"{c}.ownlist.json"
    ownok = None
    try:
        ownok = json.loads(own.read_text()) == dec
    except Exception:
        ownok = "n/a"
    # re-encode via current v7 encoder and decode back
    rows = [{"path": p, "bytes": s, "sha256": h} for p, (s, h) in inv.items()]
    rt = am.packed(am.decode_rows(am.encode_rows(rows))) == dec
    print(c, saved["schema"], "entries", len(inv), "inverse==fresh:", inv == fresh, "own --list==current decode:", ownok, "v7 roundtrip:", rt)
# synthetic edge cases for the v4 map inversion
edge = ["code/x.py.py", "code/.py", "code/a", "code/a.py", "code/a/b.py", "code/a.b/c.py", "code/x.PY", "evidence/a.json.json", "evidence/a.json", "evidence/a", "evidence/.json", "code/ü.py", "evidence/x.py", "code/x.json"]
rows = [{"path": p, "bytes": i, "sha256": hashlib.sha256(p.encode()).hexdigest()} for i, p in enumerate(edge)]
m = am.packed(am.decode_rows(am.encode_rows(rows)))
inv = invert(m)
print("edge-case inversion lossless:", inv == {r["path"]: (r["bytes"], r["sha256"]) for r in rows})
