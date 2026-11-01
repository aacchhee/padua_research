"""Executed coverage and counterfeit-witness controls for the independent checker."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

import a5_checker_n4 as check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    start = time.monotonic()
    raw = Path(arguments.certificate).read_bytes()
    certificate = json.loads(gzip.decompress(raw))
    verifier = check.Verifier()
    verifier.implicit_masks = True
    controls = []

    def rejected(name, function):
        try:
            function()
        except check.Rejected as error:
            controls.append({"name": name, "rejected": True, "reason": str(error)})
        else:
            raise RuntimeError("Negative control was accepted: " + name)

    rejected("overlapping_prefix_partition", lambda: check.partition(["0", "00", "1"]))
    missing = dict(certificate)
    missing["leaves"] = certificate["leaves"][:-1]
    rejected("missing_square_leaf", lambda: verifier.run(missing, False))
    leaf = dict(certificate["leaves"][0])
    leaf["patterns"] = leaf["patterns"][:-1]
    rejected("missing_compatible_mask_disposition", lambda: verifier.leaf(leaf))
    root = dict(certificate["interior_roots"][0])
    root["C"] = [["0", "0"], ["0", "0"]]
    rejected("counterfeit_singular_preconditioner", lambda: verifier.root(root))
    bounds, box = check.path_rectangle("")
    rejected("false_flat_witness", lambda: verifier.disposition(
        certificate["interior_roots"][0]["mask"], {"code": "flat"}, bounds, box))
    rejected("zero_hessian_not_an_exclusion", lambda: verifier.disposition(
        0, {"code": "hessian"}, bounds, box))

    t = check.x
    polynomial = check.sp.Poly((t*t - 2) * (t - 1), t, domain=check.sp.QQ)
    intervals = [["-3/2", "-7/5"], ["1", "1"], ["7/5", "3/2"]]
    check.require(len(check.verify_root_partition(polynomial, intervals)) == 3,
                  "positive Sturm control failed")
    controls.append({"name": "sturm_rational_singleton_and_two_irrational_roots", "accepted": True})
    rejected("sturm_missing_real_root", lambda: check.verify_root_partition(
        polynomial, intervals[:-1]))
    rejected("sturm_interval_without_root", lambda: check.verify_root_partition(
        polynomial, intervals[:-1] + [["8/5", "17/10"]]))

    masks = (0, 1, 2, 3, 5, 17, 255, 1024, 8191, 10922, 16384, 21845, 32766, 32767)
    for mask in masks:
        symbolic = verifier.exact_pattern(mask)[0][0]
        coefficients = verifier.coefficients(mask)
        expression = 0
        for k, (i, j) in enumerate(verifier.monomials):
            coefficient = sum(check.sp.Rational(n, verifier.denominator) * basis
                              for n, basis in zip(coefficients[4*k:4*k+4],
                                                  (1, check.SQRT2, check.SQRT5, check.SQRT10)))
            expression += coefficient * check.x ** i * check.y ** j
        check.require(check.sp.Poly(expression, check.x, check.y, domain=check.FIELD) == symbolic,
                      "integer-vector construction disagrees with symbolic sum")
    controls.append({"name": "exact_integer_vector_vs_symbolic_polynomial",
                     "masks": len(masks), "accepted": True})

    verifier.dispositions["factor"] = 1
    rejected("strict_only_factor_cannot_supply_global_plateau_proof", lambda:
             verifier.global_values({}, {}, "irrelevant", {"count_certified": True}))
    result = {"checker_sha256": hashlib.sha256(Path(check.__file__).read_bytes()).hexdigest(),
              "controls_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "python": check.platform.python_version(), "sympy": check.sp.__version__,
              "checks": controls, "all_controls_passed": True,
              "seconds": time.monotonic() - start}
    Path(arguments.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
