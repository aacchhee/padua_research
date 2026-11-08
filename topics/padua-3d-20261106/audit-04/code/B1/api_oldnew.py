import importlib.util, sys, numpy as np
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
old = load(sys.argv[1], 'u1old'); new = load(sys.argv[2], 'u1new')
rng = np.random.default_rng(7); same = 0; bad = []
for n in (1, 2, 3, 6, 10):
    for eq in (False, True):
        M = len(new.parity_nodes(n, eq)[0])
        Y = rng.standard_normal((M, 3))
        for val in (Y[:, 0], Y[:, :1], Y, Y[:, 0].tolist(), Y.tolist(), (Y[:, 0]*(1-2j)), Y.astype(np.float32), np.asfortranarray(Y), Y[:, ::2], (Y > 0)):
            a = old.parity_fit(n, val, eq); b = new.parity_fit(n, val, eq)
            if a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes(): same += 1
            else: bad.append((n, eq, a.shape, b.shape))
print({'valid_identical': same, 'differ': bad})
