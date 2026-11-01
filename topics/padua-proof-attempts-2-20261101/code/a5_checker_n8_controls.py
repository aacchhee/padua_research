"""Negative node-cone/coverage controls and exact arithmetic cross-checks."""
import argparse
from collections import Counter
import copy
import gzip
import hashlib
import json
from pathlib import Path
import time

CONTROL_SHA_AT_IMPORT = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
CHECKER_SHA_BEFORE_IMPORT = hashlib.sha256(Path(__file__).with_name("a5_checker_n8.py").read_bytes()).hexdigest()
import a5_checker_n8 as check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("node_certificate")
    parser.add_argument("--spatial-certificate")
    parser.add_argument("--global-file")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    raw = Path(args.node_certificate).read_bytes()
    data = json.loads(check.decode_payload(raw), object_pairs_hook=check.unique_object)
    nodes = data["nodes"] if "nodes" in data else data["node_cones"]
    if "field_embedding" in data:
        embedding = data["field_embedding"]
    else:
        check.require(args.spatial_certificate is not None, "node-only fixture needs a spatial embedding")
        embedding_raw = Path(args.spatial_certificate).read_bytes()
        embedding = json.loads(check.decode_payload(embedding_raw),
                               object_pairs_hook=check.unique_object)["field_embedding"]
    v = check.Verifier(embedding)
    positive = v.node_certificates(nodes)
    accepted = dict(v.node_cones)
    controls = [{"name": "all_supplied_exact_node_cones", "accepted": True, **positive}]

    def reject(name, action):
        try:
            action()
        except check.Rejected as error:
            controls.append({"name": name, "rejected": True, "reason": str(error)})
        else:
            raise RuntimeError("Invalid witness was accepted: " + name)

    byte_fixture = b'{"n":8,"exact":["1/3","0"]}\n'
    for encoded in (byte_fixture, gzip.compress(byte_fixture), check.lzma.compress(byte_fixture)):
        check.require(check.decode_payload(encoded) == byte_fixture, "compression changed decoded bytes")
    controls.append({"name":"raw_gzip_XZ_decoding_preserves_exact_payload_bytes","accepted":True})
    reject("truncated_XZ_payload_rejected", lambda:
           check.decode_payload(check.lzma.compress(byte_fixture)[:-7]))

    def embedding_case(name, change):
        altered = copy.deepcopy(embedding)
        change(altered)
        reject(name, lambda: check.verify_embedding(altered))

    embedding_case("wrong_native_minimal_polynomial", lambda r:
                   r["native_minpoly"].__setitem__(-1, "2"))
    embedding_case("counterfeit_tensor_conversion", lambda r:
                   r["native_to_tensor"][0].__setitem__(0, "2"))
    embedding_case("negative_quartic_root_embedding", lambda r:
                   r.__setitem__("a_interval", [str(-check.rational(r["a_interval"][1])),
                                                str(-check.rational(r["a_interval"][0]))]))
    embedding_case("nonprincipal_cubic_root_embedding", lambda r:
                   r.__setitem__("b_interval", ["0", "1"]))
    embedding_case("incorrect_principal_root_accounting", lambda r:
                   r.__setitem__("b_U8_count_above", 1))
    reject("field_encoding_has_wrong_dimension", lambda:
           check.parse_native_field(["0"]*11))
    for polynomial in (
            check.sp.Poly.from_dict({(1,): check.A*check.B+1, (0,): check.B**2-check.A},
                                    check.x, domain=check.FIELD),
            check.sp.Poly.from_dict({(2,): check.A+check.B**2,
                                     (1,): check.A*check.B**2+check.B,
                                     (0,): 3*check.A*check.B-check.B**2+2},
                                    check.x, domain=check.FIELD)):
        check.require(check.rational_norm(polynomial) == polynomial.norm().sqf_part().monic(),
                      "independent tensor resultant disagrees with native norm control")
    controls.append({"name": "tensor_quartic_cubic_norm_vs_native_degree_twelve_norm",
                     "accepted": True, "polynomials": 2})

    def node_case(name, change):
        altered = copy.deepcopy(nodes)
        change(altered)
        reject(name, lambda: v.node_certificates(altered))

    q = next(i for i, record in enumerate(nodes) if record["status"] == "accepted")
    internal = next((i, j) for i, record in enumerate(nodes)
                    for j, segment in enumerate(record["segments"]) if len(segment["breaks"]) > 2)
    node_case("one_node_record_omitted", lambda rows: rows.pop())
    node_case("one_feasible_direction_side_omitted", lambda rows: rows[0]["segments"].pop())
    node_case("one_internal_directional_zero_breakpoint_omitted",
              lambda rows: rows[internal[0]]["segments"][internal[1]]["breaks"].pop(1))
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
    reject("node_leaf_cannot_hide_universal_gradient",
           lambda: v.leaf({"path":"0","node_cone":q,"all_gradient":0}))
    reject("ordinary_leaf_cannot_hide_universal_gradient",
           lambda: v.leaf({"path":"0","patterns":[],"all_gradient":0}))
    reject("universal_gradient_coordinate_must_be_zero_or_one",
           lambda: v.leaf({"path":"","all_gradient":2}))
    reject("universal_gradient_coordinate_is_not_boolean",
           lambda: v.leaf({"path":"","all_gradient":True}))
    reject("universal_gradient_on_whole_square_is_not_an_exclusion",
           lambda: v.leaf({"path":"","all_gradient":0}))
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
    rational_polynomials = list(check.sturm_chain(p)) + [
        check.sp.Poly(-check.sp.Rational(7,13)*check.x**5 + check.sp.Rational(2,3)*check.x**2
                      -check.sp.Rational(11,17), check.x, domain=check.sp.QQ),
        check.sp.Poly(0,check.x,domain=check.sp.QQ)]
    points = tuple(map(check.rational, ("-1","0","1","3/7","-3/7",
                                      "123456789012345678901/1208925819614629174706176")))
    for polynomial in rational_polynomials:
        for point in points:
            reference = polynomial.eval(check.sp.Rational(point.numerator,point.denominator))
            expected = check.fmpq(int(reference.p),int(reference.q))
            check.require(check.exact_qq_value(polynomial,point) == expected,
                          "exact FLINT QQ evaluation differs from SymPy rational identity")
    controls.append({"name":"exact_FLINT_QQ_values_vs_SymPy_including_scaled_and_zero_polynomials",
                     "accepted":True,"identities":len(rational_polynomials)*len(points)})
    masks = (0, 1, 3, 17, 255, 1024, 8191, 21845, 1 << 44, (1 << 45)-1)
    for mask in masks:
        coefficients = v.coefficients(mask)
        expression = sum(sum(check.sp.Rational(n, v.denominator)*basis
                             for n, basis in zip(coefficients[12*k:12*k+12],
                                                 tuple(check.FIELD.to_sympy(q) for q in check.NATIVE_TENSOR))) *
                         check.x**i*check.y**j for k, (i, j) in enumerate(v.monomials))
        check.require(check.sp.Poly(expression, check.x, check.y, domain=check.FIELD) ==
                      v.exact_pattern(mask)[0][0], "integer-mask polynomial differs from symbolic sum")
    controls.append({"name": "540_component_integer_vectors_vs_symbolic_masks",
                     "accepted": True, "masks": len(masks)})

    if args.spatial_certificate:
        spatial_raw = Path(args.spatial_certificate).read_bytes()
        spatial = json.loads(check.decode_payload(spatial_raw), object_pairs_hook=check.unique_object)
        v.implicit_masks = True
        ordinary = next(leaf for leaf in spatial["leaves"] if "patterns" in leaf)
        altered = copy.deepcopy(ordinary)
        altered["patterns"].pop()
        reject("ordinary_compatible_mask_omitted", lambda: v.leaf(altered))
        direct = next((leaf for leaf in spatial["leaves"] if "all_gradient" in leaf), None)
        if direct is not None:
            v.leaf(direct)
            controls.append({"name":"supplied_universal_gradient_leaf_all_patterns",
                             "accepted":True,"path":direct["path"]})
        root = (copy.deepcopy(spatial["interior_roots"][0]) if spatial["interior_roots"] else
                {"id":0,"mask":0,"R":[["-1/2","1/2"],["-1/2","1/2"]]})
        root["C"] = [["0", "0"], ["0", "0"]]
        reject("counterfeit_root_singular_preconditioner", lambda: v.root(root))

    if args.global_file:
        check.require(args.spatial_certificate is not None, "global controls need the complete spatial certificate")
        full = check.Verifier(embedding)
        count_result = full.run(spatial)
        global_raw = Path(args.global_file).read_bytes()
        global_data = json.loads(check.decode_payload(global_raw), object_pairs_hook=check.unique_object)
        spatial_hash = hashlib.sha256(spatial_raw).hexdigest()
        full.global_values(spatial, global_data, spatial_hash, count_result)
        controls.append({"name": "complete_count_and_global_value_certificate", "accepted": True})

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

    checker_after = hashlib.sha256(Path(check.__file__).read_bytes()).hexdigest()
    controls_after = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    unchanged = (checker_after == CHECKER_SHA_BEFORE_IMPORT == check.SOURCE_SHA_AT_IMPORT and
                 controls_after == CONTROL_SHA_AT_IMPORT)
    result = {"all_controls_passed": unchanged, "controls": controls,
              "node_certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "checker_sha256": CHECKER_SHA_BEFORE_IMPORT,
              "checker_sha256_after": checker_after,
              "controls_sha256": CONTROL_SHA_AT_IMPORT,
              "controls_sha256_after": controls_after,
              "sources_unchanged": unchanged,
              "python": check.platform.python_version(), "sympy": check.sp.__version__,
              "python_flint": check.flint.__version__, "FLINT": check.flint.__FLINT_VERSION__,
              "seconds": time.monotonic()-started,
              "scope": "independent verifier controls; no degree-eight count"}
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))
    return 0 if unchanged else 1


if __name__ == "__main__":
    raise SystemExit(main())
