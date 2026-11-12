"""Write or verify evidence-manifest.json for this topic (small committed evidence only).

Usage (from the repository root):
  python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py          # write
  python3 -B topics/padua-effective-cubature-20261112/code/evidence_manifest.py --verify # check hashes/sizes
"""
import hashlib, json, os, sys

TOPIC = "topics/padua-effective-cubature-20261112"
ENTRIES = {
    "evidence/q0c-d3-leverage.json": {
        "producer": "code/q0_d3_leverage.py",
        "command": "python -B topics/padua-effective-cubature-20261112/code/q0_d3_leverage.py --certificate topics/padua-3d-20261106/evidence/fd3-certificate.json --output topics/padua-effective-cubature-20261112/evidence/q0c-d3-leverage.json",
        "status": "MEASURED (50-digit floating evaluation at certified dyadic centres)", "used_by": "gates.md Q0c, Q1b"},
    "evidence/cap-critical-lattice.json": {
        "producer": "code/cap_critical_lattice.py",
        "command": "python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py topics/padua-effective-cubature-20261112/evidence/cap-critical-lattice.json",
        "status": "exact finite check (PROVED input of record -04 (a))", "used_by": "theory/lp-cap.md"},
    "evidence/lp-torus.json": {
        "producer": "code/lp_torus.py (runs) + code/lp_report.py (aggregation)",
        "command": "per run: python3 code/lp_torus.py --n N --extra E --out <scratch>/runs/nN_eE.json (cwd = topic dir); aggregate: python3 code/lp_report.py --scratch <scratch> --evidence evidence",
        "status": "MEASURED (cut-plane LP optima; four lp_torus.py SHA-256 values across runs, listed in the file)", "used_by": "gates.md Q1, Q2"},
    "evidence/lp-torus-delsarte-best.json": {
        "producer": "code/lp_torus.py + code/lp_report.py",
        "command": "python3 code/lp_torus.py --n 8 --extra 8 --out <scratch>/runs/n8_e8.json; then lp_report.py as above",
        "status": "MEASURED (n=8, K=22 Delsarte polynomial coefficients; nonnegativity not certified)", "used_by": "attempts/E1.md"},
    "evidence/lp-lattice.json": {
        "producer": "code/lp_lattice.py + code/lp_report.py",
        "command": "python3 code/lp_lattice.py --mode exhaust --ns 2..8; --mode rank1 --ns 9; --mode rank1 --ns 10..16 --start-factor 1.09 --dmax-factor 1.25 --samples 3000000",
        "status": "witnesses exact (re-verified by orchestrator); minimality MEASURED-exhaustive n=2..8 by the producer only; n=9..16 upper bounds", "used_by": "gates.md Q1b, theory/lp-cap.md, code/pdn_lattice_witness.py --extra"},
    "evidence/lp-cube.json": {
        "producer": "code/lp_cube.py + code/lp_report.py",
        "command": "python3 code/lp_cube.py --n 2 --tol 1e-8 --max-iter 40 --nref 60 --cand 10000; --n 3 --tol 1e-8 --max-iter 60 --nref 80 --cand 15000; --n 4 --tol 1e-7 --max-iter 60 --nref 80 --cand 15000",
        "status": "MEASURED (cut-plane relaxation values)", "used_by": "attempts/E3.md, gates.md Q1b"},
    "evidence/pdn-lattice-witness.json": {
        "producer": "code/pdn_check_ball.py (from the full output of code/pdn_lattice_witness.py)",
        "command": "cwd = topic dir: python3 -B code/pdn_lattice_witness.py --nmin 2 --nmax 140 --extra evidence/lp-lattice.json --perturb --out <scratch>/witness-final.json; python3 -B code/pdn_check_ball.py --full <scratch>/witness-final.json --out evidence/pdn-lattice-witness.json",
        "status": "exact witnesses (each verified by exhaustive coefficient-box enumeration); input of PD-N record -06", "used_by": "theory/limitation-torus-lp-finite.md"},
    "evidence/gamma-certificate.json": {
        "producer": "code/gamma_certificate.py",
        "command": "cwd = topic dir: python3 -B code/gamma_certificate.py --anc <scratch>/octa_double.func.cpp --alpha 1.001 --R 4 --RG 4 --out evidence/gamma-certificate.json  (input: arXiv:1510.02331v3 anc/octa_double.func.cpp, SHA-256 034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47; third-party, not committed)",
        "status": "computer-assisted certificate of record -07 (L): PASS (developer run)", "used_by": "theory/explicit-gamma.md"},
}
OFFREPO = [
    {"what": "LP per-run receipts runs/n*_e*.json, lat_*.json, cube[2-4].json, torus_f_n*_e*.npz",
     "location": "session scratchpad only (not archived; AC cold storage not reachable from this cloud session)",
     "regenerate": "commands above", "archival": "PENDING"},
    {"what": "gamma certificate leaf lists (leaves-final.npz, about 3 MB) and DGOV ancillary inputs (third-party)",
     "location": "session scratchpad only; inputs re-downloadable from https://arxiv.org/src/1510.02331v3/anc/",
     "regenerate": "gamma_certificate.py --leaves PATH", "archival": "PENDING (leaves); never (third-party inputs)"},
]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def build(root):
    files = {}
    for rel, meta in ENTRIES.items():
        p = os.path.join(root, TOPIC, rel)
        prod = meta["producer"].split(" ")[0]
        files[rel] = dict(meta, sha256=sha(p), bytes=os.path.getsize(p),
                          producer_sha256=sha(os.path.join(root, TOPIC, prod)))
    return {"schema": "padua-effective-cubature-evidence-manifest-v1",
            "generate": "python3 -B " + TOPIC + "/code/evidence_manifest.py",
            "verify": "python3 -B " + TOPIC + "/code/evidence_manifest.py --verify",
            "limit_bytes_per_file": 16384, "files": files, "off_repository": OFFREPO}


def main():
    root = os.getcwd()
    out = os.path.join(root, TOPIC, "evidence-manifest.json")
    if "--verify" in sys.argv:
        cur = json.load(open(out))
        ok = True
        for rel, m in cur["files"].items():
            p = os.path.join(root, TOPIC, rel)
            good = os.path.exists(p) and sha(p) == m["sha256"] and os.path.getsize(p) == m["bytes"] <= 16384
            print(("OK  " if good else "BAD ") + rel)
            ok &= good
        sys.exit(0 if ok else 1)
    json.dump(build(root), open(out, "w"), indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
