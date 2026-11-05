"""Inspect actual corrected C++ transform weights against independent Fractions."""
if not __debug__:
    raise RuntimeError('Scientific verification requires assertions; do not use -O.')

from fractions import Fraction
import hashlib
import json
from math import comb, gcd
from pathlib import Path
import subprocess
import time

REPO = Path(__file__).resolve().parents[4]
SOURCE = REPO / 'topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp'
EXPECTED = 'b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0'
OUT = Path('/workspace/padua-work/independent')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    started = time.monotonic()
    raw = SOURCE.read_bytes()
    assert sha(raw) == EXPECTED
    source = raw.decode()
    marker = ' Coeff coeff;'
    assert source.count(marker) == 1
    # Leave actual production weight construction verbatim. Stop immediately
    # afterwards; printing introduces no arithmetic used to construct w.
    probe = (' for(int kk=0;kk<=n;++kk)for(int ii=0;ii<=n;++ii)'
             'std::cout<<kk<<" "<<ii<<" "<<w[kk][ii].get_num()<<" "'
             '<<w[kk][ii].get_den()<<"\\n";return 0;\n')
    instrumented = OUT/'canonical-weight-probe.cpp'
    instrumented.write_text(source.replace(marker, probe+marker))
    binary = OUT/'canonical-weight-probe'
    command = ['g++', '-O3', '-std=c++17', str(instrumented), '-lgmpxx', '-lgmp', '-o', str(binary)]
    subprocess.run(command, check=True)
    rows = []
    for n in range(2, 41):
        proc = subprocess.run([str(binary), str(n)], check=True, text=True, capture_output=True, timeout=30)
        lines = proc.stdout.splitlines()
        assert len(lines) == (n+1)**2
        seen = set()
        for line in lines:
            k, i, num, den = map(int, line.split())
            assert (k, i) not in seen and 0 <= k <= n and 0 <= i <= n
            seen.add((k, i))
            assert den > 0 and gcd(abs(num), den) == 1, ('noncanonical', n, k, i)
            expected = sum((Fraction(comb(i, a)*(-1)**(i-a)*2**a*comb(k, a), comb(n, a))
                            for a in range(min(i, k)+1)), Fraction(0))
            assert Fraction(num, den) == expected, ('weight mismatch', n, k, i)
        rows.append(dict(n=n, weights=len(lines), exact_match=True, all_canonical=True,
                         stdout_sha256=sha(proc.stdout.encode())))
    assert SOURCE.read_bytes() == raw, 'source changed during differential'
    result = dict(format='padua-canonical-weight-differential-v1', source_sha256=EXPECTED,
                  instrumentation='print w immediately after unchanged production construction and exit',
                  instrumented_source_sha256=sha(instrumented.read_bytes()),
                  binary_sha256=sha(binary.read_bytes()), build_command=command,
                  expected_weights='independent standard-library Fraction/binomial formula; no reference imports',
                  degrees=rows, total_weights=sum(r['weights'] for r in rows),
                  seconds=time.monotonic()-started)
    output = OUT/'canonical-weight-differential.json'
    output.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    print(json.dumps(dict(output=str(output), bytes=output.stat().st_size, sha256=sha(output.read_bytes()),
                          degrees=[2, 40], total_weights=result['total_weights'], seconds=result['seconds'])))


if __name__ == '__main__':
    main()
