import ctypes
import os

import bisection_ctype as bp


libname = os.path.abspath(os.path.join(os.path.dirname(__file__), "libcbisection.so"))

libc = ctypes.CDLL(libname)

equal_float = bp.function_wrap(
    libc,
    "equal_float",
    ctypes.c_int,
    [ctypes.c_float, ctypes.c_float, ctypes.c_float],
)

get_interval = bp.function_wrap(
    libc,
    "get_interval",
    ctypes.c_int,
    [
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
    ],
)


bisection_root = bp.function_wrap(
    libc,
    "bisection_root",
    ctypes.c_float,
    [ctypes.c_float, ctypes.c_float, ctypes.c_float],
)


def test_equal_float_call():
    assert equal_float(1.01, 1.09, 0.080001) == 1
    assert equal_float(1.00001, 1.00002, 0.00001) == 0


def test_get_interval():
    x1 = ctypes.c_float(0.5)
    x2 = ctypes.c_float(0.7)
    x1_ptr = ctypes.pointer(x1)
    x2_ptr = ctypes.pointer(x2)
    out = get_interval(x1_ptr, x2_ptr)
    assert out == 1
    assert bool(equal_float(x2, ctypes.c_float(1.75), 0.00001))


def test_bisection_root():
    x1 = ctypes.c_float(0.5)
    x2 = ctypes.c_float(0.7)
    x1_ptr = ctypes.pointer(x1)
    x2_ptr = ctypes.pointer(x2)
    get_interval(x1_ptr, x2_ptr)
    accuracy = ctypes.c_float(0.000001 * (abs(x1.value) + abs(x2.value)) / 2)
    root = bisection_root(x1, x2, accuracy)
    assert bool(equal_float(root, 1.0, accuracy))


