import ctypes
import os


def function_wrap(lib, fname, rettype, paramtypes):
    func = lib.__getattr__(fname)
    func.restype = rettype
    func.argtypes = paramtypes
    return func


libname = os.path.abspath(os.path.join(os.path.dirname(__file__), "libcbisection.so"))

libc = ctypes.CDLL(libname)

equal_float = function_wrap(
    libc,
    "equal_float",
    ctypes.c_int,
    [ctypes.c_float, ctypes.c_float, ctypes.c_float],
)

get_interval = function_wrap(
    libc,
    "get_interval",
    ctypes.c_int,
    [
        ctypes.POINTER(ctypes.c_float),
        ctypes.POINTER(ctypes.c_float),
    ],
)

bisection_root = function_wrap(
    libc,
    "bisection_root",
    ctypes.c_float,
    [ctypes.c_float, ctypes.c_float],
)


def main():
    x1 = ctypes.c_float(0.5)
    x2 = ctypes.c_float(0.7)
    x1_ptr = ctypes.pointer(x1)
    x2_ptr = ctypes.pointer(x2)
    out = get_interval(x1_ptr, x2_ptr)
    assert out == 1
    assert equal_float(x2, ctypes.c_float(1.75), 0.00001)

    accuracy = ctypes.c_float(0.000001 * (abs(x1.value) + abs(x2.value)) / 2)

    print(bisection_root(0.5, 1.7))


if __name__ == "__main__":
    main()
