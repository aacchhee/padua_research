import json, sys
def strip(o, drop):
    if isinstance(o, dict):
        return {k: strip(v, drop) for k, v in o.items() if k not in drop}
    if isinstance(o, list):
        return [strip(v, drop) for v in o]
    return o
def diff(a, b, path=''):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in set(a) | set(b):
            if k not in a or k not in b:
                out.append(path + '/' + k + ' missing'); continue
            out += diff(a[k], b[k], path + '/' + k)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): out.append(path + ' len'); return out
        for i, (x, y) in enumerate(zip(a, b)): out += diff(x, y, path + '[%d]' % i)
    elif isinstance(a, float) and isinstance(b, float):
        if abs(a - b) > 1e-9 * max(1, abs(a)): out.append('%s %r %r' % (path, a, b))
        elif a != b: out.append('%s FLOATULP %r %r' % (path, a, b))
    elif a != b:
        out.append('%s %r %r' % (path, a, b))
    return out
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
drop = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else set()
d = diff(strip(a, drop), strip(b, drop))
big = [x for x in d if 'FLOATULP' not in x]
print(len(d), 'diffs;', len(big), 'beyond 1e-9 rel')
for x in big[:40]: print(' ', x)
ulp = [x for x in d if 'FLOATULP' in x]
print(' ulp-level examples:', ulp[:3])
