"""Verify browser C source natively against the shared vectors (requires GCC)."""
import ctypes
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(dir=ROOT) as temporary:
    library = Path(temporary) / 'algorithms.so'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-shared', '-fPIC',
                    str(ROOT / 'web/c/algorithms.c'), '-o', str(library)], check=True)
    runtime = ctypes.CDLL(str(library))
    count = 0
    for task, spec in json.loads((ROOT / 'specs/vectors.json').read_text()).items():
        solve = getattr(runtime, 'lab_' + task)
        solve.argtypes = [ctypes.c_int] * (2 if task == 'gcd' else 1)
        solve.restype = ctypes.c_int
        for args, expected in zip(spec['cases'], spec['expected']):
            actual = solve(*args)
            if actual != expected:
                raise AssertionError((task, args, expected, actual))
            count += 1
    print(f'PASS C browser algorithm sources: {count} shared cases')
