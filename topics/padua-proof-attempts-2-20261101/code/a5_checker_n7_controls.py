"""Negative node-cone/coverage controls and exact arithmetic cross-checks."""
import argparse
from collections import Counter
import copy
import gzip
import hashlib
import json
import lzma
from pathlib import Path
import time

import a5_checker_n7 as check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("node_certificate")
    parser.add_argument("--spatial-certificate")
    parser.add_argument("--global-file")
    parser.add_argument("--embedding-file")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    sources = {"checker_sha256": Path(check.__file__),
               "formal_field_helper_sha256": Path(check.__file__).with_name("a5_checker_n7_field.py"),
               "controls_sha256": Path(__file__)}
    source_hashes = {key: hashlib.sha256(path.read_bytes()).hexdigest()
                     for key, path in sources.items()}
    raw = Path(args.node_certificate).read_bytes()
    data = json.loads(check.decode_document(raw))
    nodes = data["nodes"] if "nodes" in data else data["node_cones"]
    if "field_embedding" in data:
        embedding = data["field_embedding"]
    else:
        check.require(args.embedding_file is not None or args.spatial_certificate is not None,
                      "node-only fixture needs a supplied embedding record")
        embedding_raw = Path(args.embedding_file or args.spatial_certificate).read_bytes()
        supplied_embedding = json.loads(check.decode_document(embedding_raw))
        embedding = supplied_embedding.get("embedding", supplied_embedding.get("field_embedding"))
    v = check.Verifier(embedding)
    positive = v.node_certificates(nodes)
    accepted = dict(v.node_cones)
    controls = [{"name": "all_supplied_exact_node_cones", "accepted": True, **positive}]
    container_fixture = b'{"lossless":"exact rational certificate","value":"1/7"}\n'
    check.require(all(check.decode_document(value) == container_fixture for value in
                      (container_fixture, gzip.compress(container_fixture, mtime=0),
                       lzma.compress(container_fixture))), "lossless document decoder changed JSON bytes")
    controls.append({"name": "raw_gzip_xz_decode_identical_json_bytes", "accepted": True})

    def reject(name, action):
        try:
            action()
        except check.Rejected as error:
            controls.append({"name": name, "rejected": True, "reason": str(error)})
        else:
            raise RuntimeError("Invalid witness was accepted: " + name)

    def embedding_case(name, change):
        altered = copy.deepcopy(embedding)
        change(altered)
        reject(name, lambda: check.verify_embedding(altered))

    embedding_case("wrong_native_minimal_polynomial", lambda r:
                   r["native_minpoly"].__setitem__(-1, "2"))
    embedding_case("counterfeit_tensor_conversion", lambda r:
                   r["native_to_tensor"][0].__setitem__(0, "2"))
    embedding_case("negative_principal_cubic_embedding", lambda r:
                   r.__setitem__("a_interval", [str(-check.rational(r["a_interval"][1])),
                                                str(-check.rational(r["a_interval"][0]))]))
    embedding_case("nonprincipal_quartic_root_embedding", lambda r:
                   r.__setitem__("b_interval", ["0", "1"]))
    embedding_case("incorrect_tensor_defining_polynomial", lambda r:
                   r["b_minpoly"].__setitem__(-1, 3))
    embedding_case("incorrect_tensor_basis_order", lambda r:
                   r.__setitem__("basis", "reversed"))
    embedding_case("incorrect_principal_root_accounting", lambda r:
                   r.__setitem__("b_U7_count_above", 1))
    reject("field_encoding_has_wrong_dimension", lambda:
           check.parse_native_field(["0"]*11))
    for polynomial in (
            check.sp.Poly.from_dict({(1,): check.A**2*check.B**3+1, (0,): check.B**2-check.A**2},
                                    check.x, domain=check.FIELD),
            check.sp.Poly.from_dict({(2,): check.A+check.B**2,
                                     (1,): check.A*check.B**2+check.B,
                                     (0,): 3*check.A*check.B-check.B**2+2},
                                    check.x, domain=check.FIELD)):
        check.require(check.rational_norm(polynomial) == polynomial.norm().sqf_part().monic(),
                      "independent tensor resultant disagrees with native norm control")
    controls.append({"name": "tensor_cubic_quartic_norm_vs_native_degree_twelve_norm",
                     "accepted": True, "polynomials": 2})

    def node_case(name, change):
        altered = copy.deepcopy(nodes)
        change(altered)
        reject(name, lambda: v.node_certificates(altered))

    q = next(i for i, record in enumerate(nodes) if record["status"] == "accepted")
    internal = next((i, j) for i, record in enumerate(nodes)
                    for j, segment in enumerate(record["segments"]) if len(segment["breaks"]) > 2)
    node_case("exact_node_coordinate_altered", lambda rows:
              rows[0]["node"][0].__setitem__(0, str(check.rational(rows[0]["node"][0][0])+1)))
    node_case("one_node_record_omitted", lambda rows: rows.pop())
    node_case("one_feasible_direction_side_omitted", lambda rows: rows[0]["segments"].pop())
    node_case("one_internal_directional_zero_breakpoint_omitted",
              lambda rows: rows[internal[0]]["segments"][internal[1]]["breaks"].pop(1))
    node_case("duplicated_direction_breakpoint", lambda rows:
              rows[0]["segments"][0]["breaks"].insert(1, copy.deepcopy(rows[0]["segments"][0]["breaks"][0])))
    node_case("false_positive_gap_lower_bound", lambda rows: rows[q].__setitem__("gap_lower", "1000000000"))

    def inactive_face(rows):
        node_x = check.parse_native_field(rows[q]["node"][0])
        if node_x == check.native(-1):
            rows[q]["B"][0][1] = "1"
        else:
            rows[q]["B"][0][0] = "-1"
    node_case("cone_rectangle_hits_inactive_square_face", inactive_face)
    node_case("radius_underestimates_whole_cone_rectangle", lambda rows:
              rows[q].__setitem__("R", str(check.rational(rows[q]["R"])/2)))
    node_case("false_whole_cone_node_cardinal_positivity_bound", lambda rows:
              rows[q].__setitem__("Lq_lower", "2"))
    h_index = next(i for i, value in enumerate(nodes[q]["H_i"]) if check.rational(value) > 0)
    node_case("one_cardinal_hessian_bound_underestimated", lambda rows:
              rows[q]["H_i"].__setitem__(h_index, "0"))
    node_case("radial_remainder_exceeds_exact_gap", lambda rows:
              rows[q].__setitem__("H", str(check.rational(rows[q]["gap_lower"])/
                                          check.rational(rows[q]["R"])+1)))

    v.node_cones = dict(accepted)
    reject("whole_leaf_not_inside_referenced_cone", lambda: v.leaf({"path": "", "node_cone": q}))
    bounds, _ = check.path_rectangle("0")
    v.node_cones = {q: bounds}
    reject("non_strict_leaf_cone_containment", lambda: v.leaf({"path": "0", "node_cone": q}))
    v.node_cones = {}
    reject("zero_gap_or_missing_cone_has_no_discard_authority",
           lambda: v.leaf({"path": "0", "node_cone": q}))
    v.node_cones = dict(accepted)
    reject("node_leaf_cannot_hide_ordinary_pattern_list",
           lambda: v.leaf({"path": "0", "node_cone": q, "patterns": []}))
    reject("node_leaf_cannot_hide_universal_gradient_disposition",
           lambda: v.leaf({"path": "0", "node_cone": q, "all_gradient": 0}))
    reject("universal_gradient_coordinate_must_be_physical",
           lambda: v.leaf({"path": "", "all_gradient": 2}))
    reject("universal_gradient_cannot_hide_ordinary_patterns",
           lambda: v.leaf({"path": "", "all_gradient": 0, "patterns": []}))
    reject("universal_gradient_cannot_exclude_the_whole_square",
           lambda: v.leaf({"path": "", "all_gradient": 0}))
    reject("overlapping_prefix_partition", lambda: check.partition(["0", "00", "1"]))
    check.require(check.partition(["0", "10", "11"]), "positive complete prefix partition failed")
    check.require(not check.partition(["0", "10"]), "missing subtree incorrectly complete")
    controls.append({"name": "complete_vs_missing_prefix_subtree", "accepted": True})
    bounds, box = check.path_rectangle("")
    reject("singular_zero_hessian_is_not_an_exclusion", lambda:
           v.disposition(0, {"code": "hessian"}, bounds, box))

    p = check.sp.Poly((check.x**2-2)*(check.x-1), check.x, domain=check.sp.QQ)
    intervals = [["-3/2", "-7/5"], ["1", "1"], ["7/5", "3/2"]]
    check.require(len(check.verify_root_partition(p, intervals)) == 3, "positive Sturm control failed")
    reject("one_sturm_projected_root_omitted", lambda: check.verify_root_partition(p, intervals[:-1]))
    evaluation_polynomials = (
        check.sp.Poly(0, check.x, domain=check.sp.QQ),
        check.sp.Poly(-7, check.x, domain=check.sp.QQ),
        check.sp.Poly((2*check.x**3-7*check.x+1)/13, check.x, domain=check.sp.QQ),
        check.sp.Poly((check.x-1)*(check.x+2), check.x, domain=check.sp.QQ),
        check.sp.Poly(17*check.x**7-23*check.x**2+5, check.x, domain=check.sp.ZZ))
    evaluation_points = tuple(map(check.Fraction, (-2, -1, 0, 1, 2))) + \
        (check.Fraction(-1, 10), check.Fraction(123456789012345678901, 1 << 80))
    for polynomial in evaluation_polynomials:
        for point in evaluation_points:
            expected = polynomial.eval(check.sp.Rational(point.numerator, point.denominator))
            value = check.exact_qq_value(polynomial, point)
            check.require(check.Fraction(str(value)) == check.Fraction(str(expected)) and
                          check.exact_qq_sign(polynomial, point) == int(check.sp.sign(expected)),
                          "exact FLINT rational evaluation differs from SymPy")
    controls.append({"name": "exact_flint_values_and_signs_vs_sympy_including_scaling_and_zeros",
                     "accepted": True, "evaluations": len(evaluation_polynomials)*len(evaluation_points)})
    masks = (0, 1, 3, 17, 255, 1024, 8191, 21845, 1 << 35, (1 << 36)-1)
    for mask in masks:
        coefficients = v.coefficients(mask)
        expression = sum(sum(check.sp.Rational(n, v.denominator)*basis
                             for n, basis in zip(coefficients[12*k:12*k+12],
                                                 tuple(check.FIELD.to_sympy(q) for q in check.NATIVE_TENSOR))) *
                         check.x**i*check.y**j for k, (i, j) in enumerate(v.monomials))
        check.require(check.sp.Poly(expression, check.x, check.y, domain=check.FIELD) ==
                      v.exact_pattern(mask)[0][0], "integer-mask polynomial differs from symbolic sum")
    controls.append({"name": "432_component_integer_vectors_vs_symbolic_masks",
                     "accepted": True, "masks": len(masks)})
    fixed_positive = (1 << 1) | (1 << 4) | (1 << 10)
    ambiguous = (0, 3, 7, 35)
    background = tuple(a + sum(v.integer_cardinals[i][k] for i in ambiguous)
                       for k, a in enumerate(v.coefficients(fixed_positive)))
    expression = sum(sum(check.sp.Rational(n, v.denominator)*check.FIELD.to_sympy(basis)
                         for n, basis in zip(background[12*k:12*k+12], check.NATIVE_TENSOR)) *
                     check.x**i*check.y**j for k, (i, j) in enumerate(v.monomials))
    expected = sum((1 if fixed_positive & (1 << i) else -1)*p
                   for i, p in enumerate(v.cardinals) if i not in ambiguous)
    check.require(check.sp.Poly(expression, check.x, check.y, domain=check.FIELD) == expected,
                  "universal-gradient fixed background differs from exact signed sum")
    controls.append({"name": "universal_gradient_background_vs_exact_fixed_signed_sum",
                     "accepted": True})

    if args.spatial_certificate:
        spatial_raw = Path(args.spatial_certificate).read_bytes()
        spatial = json.loads(check.decode_document(spatial_raw))
        v.implicit_masks = True
        ordinary = next(leaf for leaf in spatial["leaves"] if "patterns" in leaf)
        altered = copy.deepcopy(ordinary)
        altered["patterns"].pop()
        reject("ordinary_compatible_mask_omitted", lambda: v.leaf(altered))
        uniform = next((leaf for leaf in spatial["leaves"] if "all_gradient" in leaf), None)
        if uniform is not None:
            v.leaf(uniform)
            controls.append({"name": "supplied_universal_gradient_leaf", "accepted": True})
        check.require(check.partition([leaf["path"] for leaf in spatial["leaves"]]) ==
                      spatial["summary"].get("interior_complete", True), "spatial prefix summary mismatch")
        if spatial["summary"].get("interior_complete"):
            check.require(not check.partition([leaf["path"] for leaf in spatial["leaves"][:-1]]),
                          "deleting an actual full-tree leaf did not destroy coverage")
            controls.append({"name": "actual_complete_tree_leaf_deletion_loses_coverage", "accepted": True})
        if spatial["interior_roots"]:
            root = copy.deepcopy(spatial["interior_roots"][0])
            root["C"] = [["0", "0"], ["0", "0"]]
            reject("counterfeit_root_singular_preconditioner", lambda: v.root(root))

    if args.global_file:
        check.require(args.spatial_certificate is not None, "global controls need the complete spatial certificate")
        full = check.Verifier(embedding)
        count_result = full.run(spatial)
        global_raw = Path(args.global_file).read_bytes()
        global_data = json.loads(check.decode_document(global_raw))
        spatial_hash = hashlib.sha256(spatial_raw).hexdigest()
        full.global_values(spatial, global_data, spatial_hash, count_result)
        controls.append({"name": "complete_count_and_global_value_certificate", "accepted": True})
        reject("one_entire_edge_omitted", lambda:
               full.boundaries(spatial["edges"][:-1], spatial["corners"]))
        for leaf in spatial["leaves"]:
            candidate = next((record for record in leaf.get("patterns", [])
                              if record["code"] == "root"), None)
            if candidate is not None:
                root = full.roots[candidate["id"]]
                bounds, box = check.path_rectangle(leaf["path"])
                if not check.contains_rational(root["bounds"], bounds):
                    altered = copy.deepcopy(candidate)
                    altered["U"] = [[str(a), str(b)] for a, b in root["bounds"]]
                    reject("root_hull_must_include_whole_leaf", lambda:
                           full.disposition(root["mask"], altered, bounds, box))
                    break

        def global_case(name, change):
            altered = copy.deepcopy(global_data)
            change(altered)
            reject(name, lambda: full.global_values(spatial, altered, spatial_hash, count_result))

        global_case("global_certificate_bound_to_wrong_count_input", lambda g:
                    g.__setitem__("certificate_sha256", "0"*64))
        global_case("global_exception_code_coverage_omitted", lambda g:
                    g.__setitem__("bounded_codes", ["flat"]))
        global_case("global_flat_factor_occurrence_count_changed", lambda g:
                    g.__setitem__("exception_leaf_occurrences", g["exception_leaf_occurrences"]+1))
        if full.exception_occurrences:
            global_case("global_exception_upper_bound_counterfeit", lambda g:
                        g.__setitem__("exception_upper", "-1000000000"))
        global_case("global_exact_node_value_changed", lambda g: g.__setitem__("node_value", "2"))
        global_case("global_interior_value_row_omitted", lambda g: g["interior_values"].pop())
        global_case("global_edge_value_row_omitted", lambda g: g["edge_values"].pop())
        global_case("global_interior_value_enclosure_counterfeit", lambda g:
                    g["interior_values"][0].__setitem__("enclosure", ["-100", "-99"]))
        global_case("global_exact_corner_value_counterfeit", lambda g:
                    g["corner_value"].__setitem__(0, str(check.rational(g["corner_value"][0])+1)))

    check.require(all(hashlib.sha256(path.read_bytes()).hexdigest() == source_hashes[key]
                      for key, path in sources.items()), "verifier/control source changed during execution")
    result = {"all_controls_passed": True, "controls": controls,
              "node_certificate_sha256": hashlib.sha256(raw).hexdigest(),
              **source_hashes, "source_hashes_unchanged": True,
              "python": check.platform.python_version(), "sympy": check.sp.__version__,
              "python_flint": check.flint.__version__, "FLINT": check.flint.__FLINT_VERSION__,
              "seconds": time.monotonic()-started,
              "scope": "independent verifier controls; no degree-seven count"}
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
