"""R02 driver: identity checks (PD-T?...-103/-104), exact omega-recurrence sources (PD-T?...-106).
MEASURED only.  Usage: python3 -I l1_r02_main.py > logs/r02_identities.log"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L
import l1_identities as I

print(f"# l1_r02_main.py numpy={np.__version__} python={sys.version.split()[0]}")
P, w = L.nodes_random(1681, 0)
I.run('random1681_s0 (product-like support)', P, w, 32, [24, 32])
I.run('random1681_s0 rotated 0.3 (non-product support)', L.rotate(P, 0.3), w, 20, [12, 16, 20])
P2, w2 = L.nodes_tensor_cheb(41)
I.run('tensorcheb41', P2, w2, 32, [24, 32])
for nm, PP in [('random1681_s0', P), ('random1681_s0 rotated 0.3', L.rotate(P, 0.3))]:
    I.omega_sources(nm, PP, w, 18)
