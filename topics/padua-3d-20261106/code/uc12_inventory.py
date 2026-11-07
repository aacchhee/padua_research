#!/usr/bin/env python3
"""Build a data-only inventory for the independent array checker."""
import argparse
import json
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("campaign", choices=("U1", "U2"))
    p.add_argument("--receipts", nargs="+", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = {"campaign": a.campaign, "sources": [str(Path(__file__).resolve())], "cases": []}
    for path in a.receipts:
        data = json.loads(path.read_text())
        out["sources"].append(str(path.resolve()))
        out["sources"] += [str(ROOT/key) for key in data["sources"]]
        if a.campaign == "U1":
            raw = Path(data["raw"]["directory"])
            for values in data["rows"]:
                row = dict(zip(data["columns"], values))
                assert row["eligible"], "ineligible producer case requires an explicit failure disposition"
                n, family = row["n"], row["family"]
                archive = raw/f"{data['mode']}-n{n}-{family}.npz"
                metadata = archive.with_suffix(".json")
                case = {"n": n, "family": family+("-OLS" if data["mode"] == "round2" else "-Haar" if family in ("aniso", "equal") else ""),
                        "solver": "ols" if data["mode"] == "round2" else "weighted",
                        "nodes": {"path": str(archive), "key": "points"},
                        "weights": {"path": str(archive), "key": "weights"},
                        "operator": {"path": str(archive), "key": "operator"}}
                if family in ("aniso", "equal"):
                    case["parity"] = family
                    case["api"] = str(TOP/"code/u1_usable.py")
                    case["indices"] = {"path": str(metadata), "keys": ["construction", "indices"]}
                    case["multiplicities"] = {"path": str(metadata), "keys": ["construction", "multiplicities"]}
                else:
                    out["sources"].append(str(metadata))
                out["cases"].append(case)
        else:
            raw = Path(data["scratch"])
            for values in data["rows"]:
                row = dict(zip(data["row_columns"], values))
                assert row["eligible"]
                out["cases"].append({"n": row["n"], "family": row["family"], "solver": "weighted",
                                     "nodes": {"path": str(raw/f"n{row['n']}-{row['family']}-nodes.npy")}})
    out["sources"] = sorted(set(out["sources"]))
    a.output.write_text(json.dumps(out, separators=(",", ":"))+"\n")


if __name__ == "__main__":
    main()
