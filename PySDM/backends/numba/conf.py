"""
Created at 08.08.2019
"""

import numba
import warnings
import os
    
JIT_FLAGS = dict(
    parallel=True,
    fastmath=True,
    error_model='numpy',
    cache=True
)

try:
    numba.parfors.parfor.ensure_parallel_support()
except numba.core.errors.UnsupportedParforsError:
    if 'CI' not in os.environ:
        warnings.warn("Numba version used does not support parallel for (32 bits?)")
    JIT_FLAGS['parallel']=False

