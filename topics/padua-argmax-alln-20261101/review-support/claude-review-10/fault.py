import importlib.util, os, sys, json
from pathlib import Path
repo = Path(sys.argv[1]); dest = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location('cs', str(repo/'tools/cold_storage.py')); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
orig = m.SafeTree.write_new
def corrupt(self, path, data):
    orig(self, path, data)
    if path.endswith('c.bin'):
        with self.parent(path) as (p, name):
            fd = os.open(name, os.O_WRONLY | os.O_TRUNC, dir_fd=p); os.write(fd, b'X'); os.close(fd)
m.SafeTree.write_new = corrupt
sys.argv = ['cold_storage.py', 'export', 'demo', '--dest', str(dest)]
m.main()
