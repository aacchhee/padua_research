"""Separate source and output; reuse preserved independent runtime snapshot utility."""
import pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[4]
HERE=pathlib.Path(__file__).resolve().parent
OLD=HERE.parent/'phase_checker'
sys.path.insert(0,str(OLD))
import build_snapshot_r9 as pinned

def build():
    text=pathlib.Path(pinned.__file__).read_text()
    text=text.replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/cheap-C03'")
    text=text.replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_C03/prototype.cpp'")
    ns={'__file__':str(OLD/'build_snapshot_r9.py')};exec(compile(text,'<c01-prototype-snapshot>','exec'),ns)
    binary,manifest=ns['build']();return binary,manifest,ns['loaded_closure']
