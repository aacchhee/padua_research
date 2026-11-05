#!/bin/sh
set -eu
# Run from repository root. Dependency binaries/headers remain untracked.
r=local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr
out=local-output/argmax-bridge-20261105/phase-checker
c++ -std=c++17 -O3 -Wall -Wextra -fPIC -shared -I"$r/include" \
 topics/padua-argmax-bridge-20261105/code/phase_checker/arb_kernel.cpp \
 -L"$r/lib/x86_64-linux-gnu" -Wl,-rpath,"$PWD/$r/lib/x86_64-linux-gnu" \
 -lflint -lgmp -o "$out/libphase_checker.so"
