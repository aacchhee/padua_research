"""Scalar arithmetic for r03 explicit local constants; no proof/scan role."""
import hashlib
import json
import math
from pathlib import Path
import platform


def receipt():
    c2, c3, ce = 242000, 2048, 640
    rho = 1 / 64
    delta = math.pi / 4
    kappa = 1 - math.cos(delta / 2)
    d = kappa / 4096
    radius = kappa / 4
    log_degree = 10_000_000
    a = log_degree**2 / 100
    first = 27 * c3**4 / (32 * a**3)
    # H=1+log(n+1) <= L+2 for L>=1. Avoid exp(L) overflow.
    log_second_upper = 2 * math.log(ce) + 2 * math.log(log_degree + 2) - math.log(2 * a) - 2 * log_degree
    # Positive zero of L^2/25-c2*(L+1/2)-27/5.
    turnover = (25 * c2 + math.sqrt((25 * c2)**2 + 100 * (c2 / 2 + 27 / 5))) / 2
    return {
        "status": "MEASURED scalar arithmetic only; analytic proof is in r03-explicit-local.md",
        "python": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "constants": {"rho_star": rho, "C2": c2, "C3": c3, "Ce": ce},
        "regular_sum_constants": {"f_gradient": 1152, "f_hessian": 55296,
                                  "g_value": 24, "g_gradient": 216, "g_hessian": 1080,
                                  "path_second_derivative": 59000},
        "quadratic_bookkeeping": {"regular": 236000, "sign_changes": 5376,
                                  "collision_family_over_log3": 10 / math.log(3),
                                  "sum": 236000 + 5376 + 10 / math.log(3),
                                  "preliminary_240000_covers_this_sum": False,
                                  "final_242000_covers_this_sum": True},
        "defect_budget": {"delta": delta, "rho_delta": radius, "n_delta": 64,
                          "d_delta": d, "local_radius_compatible": rho < radius},
        "comparison": {"log_degree": log_degree, "A": a,
                       "quadratic_turnover_log_degree": turnover,
                       "cubic_over_quadratic_maximum": first,
                       "endpoint_component_log10_upper": log_second_upper / math.log(10),
                       "first_component_below_defect": first < d,
                       "finite_degree_coverage_inferred": False,
                       "global_phase_entry_quantified": False},
    }


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2))
