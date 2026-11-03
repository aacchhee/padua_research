"""Frozen A5 producer/continuation with bit-identical monomial memoization.

No source/predicate change. Metadata records every runtime replacement. All
frozen mathematical functions other than proven-identical evaluate are intact.
"""
import argparse,hashlib,importlib,sys
from pathlib import Path
from t1_memo import evaluator
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))
import a5_n8_field as field

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--phase',choices=['fresh','continue','left'],default='fresh')
    parser.add_argument('--resume');parser.add_argument('--original-v3');parser.add_argument('--input-sha256');parser.add_argument('--boxes',type=int,default=2000000);parser.add_argument('--seconds',type=int,default=3600)
    parser.add_argument('--depth',type=int,default=44);parser.add_argument('--ambiguity',type=int,default=8);parser.add_argument('--full-depth',type=int,default=44)
    parser.add_argument('--root-depth',type=int,default=12);parser.add_argument('--cache-masks',type=int,default=8000);parser.add_argument('--node-file');parser.add_argument('--output',required=True)
    args=parser.parse_args();args.certificate=True;args.boundary=False
    assert args.depth==44 and args.full_depth==44 and args.ambiguity==8 and args.root_depth==12
    assert args.seconds>0 and args.boxes>0 and args.cache_masks>0
    if args.phase!='fresh':assert args.resume
    if args.phase=='left':assert args.original_v3 and args.input_sha256 and args.seconds<=2400
    own=digest(__file__);memo=digest(Path(__file__).with_name('t1_memo.py'))
    module=importlib.import_module({'fresh':'a5_n8_boxes','continue':'a5_n8_continue','left':'a5_n8_continue_v5'}[args.phase])
    before={str(p):digest(p)for p in FROZEN.glob('a5_n8*.py')}
    evaluate,cache=evaluator(field)
    field.evaluate=evaluate;module.evaluate=evaluate
    import a5_n8_nodes as nodes
    nodes.evaluate=evaluate
    original_write=module.write_artifact
    def write(out,path):
        assert own==digest(__file__)and memo==digest(Path(__file__).with_name('t1_memo.py'))
        assert all(digest(p)==h for p,h in before.items())
        out['metadata']['execution']={'driver_sha256':own,'memo_source_sha256':memo,
            'backend':'bit-identical frozen power/products with bounded monomial reuse',
            'cache':cache.cache_info()._asdict(),'frozen_sources_unchanged':True}
        return original_write(out,path)
    module.write_artifact=write
    module.solve(args)
if __name__=='__main__':main()
