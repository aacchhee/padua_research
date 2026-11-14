#!/usr/bin/env python3
"""Round9 backend only: frozen r8 acceptance with independently refined Arb defects."""
import argparse, ctypes, hashlib, json, pathlib, sys, time
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import build_snapshot_r9 as build
import check_r8 as acceptance
import check_r6 as legacy
import build_snapshot as legacy_build

ROOT=pathlib.Path(__file__).resolve().parents[4]


def python_sources():
    # Include transitive imports even when their Kernel classes are not used.
    return [build.identity(pathlib.Path(module.__file__)) for module in
            (sys.modules[__name__],build,acceptance,legacy,legacy_build)]


def verify(entries):
    for entry in entries:
        if build.identity(pathlib.Path(entry['path']))!=entry:
            raise acceptance.Invalid('source/build/runtime identity changed: '+entry['path'])


class Kernel:
    def __init__(self,kernel_variant='round9'):
        binary,self.provenance=build.build(kernel_variant)
        self.lib=ctypes.CDLL(str(binary));self.fn=self.lib.phase_bounds
        self.provenance['loaded_dependency_closure']=build.loaded_closure(self.provenance)
        self.fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ctypes.POINTER(ctypes.c_double)]
        self.fn.restype=ctypes.c_int
    def bounds(self,n,b):
        out=(ctypes.c_double*7)()
        if self.fn(n,*b,out):raise acceptance.Invalid('round9 Arb kernel rejected inputs')
        return list(out)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=pathlib.Path)
    ap.add_argument('--output',type=pathlib.Path);ap.add_argument('--max-leaves',type=int)
    ap.add_argument('--kernel',choices=('round9',),default='round9');args=ap.parse_args()
    started=time.process_time();raw=args.candidate.read_bytes();sources=python_sources()
    native=build.identity(pathlib.Path(__file__).with_name('hybrid_kernel_v3.cpp'))
    provenance=None
    try:
        data=acceptance.strict_json(raw);kernel=Kernel(args.kernel);provenance=kernel.provenance
        # No monkeypatch: exact frozen r8 predicates receive an explicit backend.
        report=acceptance.check(data,kernel,args.max_leaves)
        verify(sources+[native])
        for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):
            verify([provenance[key]])
        for key in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs',
                    'linked_dependency_closure','loaded_dependency_closure'):
            verify(provenance[key])
    except (acceptance.Invalid,ValueError,KeyError,TypeError,RuntimeError,OSError) as exc:
        report={'accepted':False,'error':str(exc)}
    report.update(candidate_sha256=hashlib.sha256(raw).hexdigest(),candidate_bytes=len(raw),
                  build_provenance=provenance,checker_python_sources=sources,
                  native_source=native,cpu_seconds=time.process_time()-started,
                  acceptance_source='unchanged frozen check_r8.check; new explicit round9 Kernel only')
    text=json.dumps(report,indent=2)
    if args.output:
        if args.output.exists():raise acceptance.Invalid('refusing to overwrite checker report')
        args.output.write_text(text+'\n')
    print(text);return 0 if report.get('accepted') else 1

if __name__=='__main__':raise SystemExit(main())
