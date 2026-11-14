"""Finite runtime identity for prospective freezing and in-process verification."""
import hashlib
from pathlib import Path
import sys
import numpy as np

def identity():
    executable=Path(sys.executable).resolve()
    extension=Path(np._core._multiarray_umath.__file__).resolve()
    return {'python':sys.version,'python_executable':str(executable),
            'python_sha256':hashlib.sha256(executable.read_bytes()).hexdigest(),
            'numpy':np.__version__,'numpy_core_extension':str(extension),
            'numpy_core_sha256':hashlib.sha256(extension.read_bytes()).hexdigest()}
