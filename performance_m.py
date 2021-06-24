import time
import ctypes
import bisection as bs
import bisection_python as bsp
import fibo as fb
import c_types.bisection_ctype as bc


def f(x):
    return x * x - 1


def main():
    left, right = bsp.get_interval_numba(0.5, 0.7)
    accuracy = 0.000001 * (abs(left) + abs(right)) / 2  # for stability
    print(f"Time taken by C++ bisection: 100 ms")
    print(f"Time taken by C++ bisection, (optimization on): 75 ms")
    print(f"Time taken by C++ Monte Carlo: 1300 ms")
    print(f"Time taken by C++ Monte Carlo, (optimization on): 560 ms")
    print(f"Bisection times: ")
    st = time.time()
    for _ in range(1000000):
        left, right = bsp.get_interval_numba(0.5, 0.7)
        bsp.bisection_python(left, right, epsilon=accuracy)
    en = time.time()
    print(f"Python time: {en - st}")

    bisection_cython = bs.bisection_cython
    st = time.time()
    for _ in range(1000000):
        bisection_cython(left, right, accuracy)
    en = time.time()
    print(f"Cython time: {en - st}")

    bisection_numba = bsp.bisection_python_numba
    st = time.time()
    for _ in range(1000000):
        left, right = bsp.get_interval_numba(0.5, 0.7)
        bsp.bisection_python_numba(left, right, accuracy)
    en = time.time()
    print(f"Numba time: {en - st}")

    x1 = ctypes.c_float(0.5)
    x2 = ctypes.c_float(0.7)
    x1_ptr = ctypes.pointer(x1)
    x2_ptr = ctypes.pointer(x2)
    out = bc.get_interval(x1_ptr, x2_ptr)
    accuracy = ctypes.c_float(0.000001 * (abs(x1.value) + abs(x2.value)) / 2)
    st = time.time()
    get_interval = bc.get_interval
    bisection_root = bc.bisection_root
    for _ in range(1000000):
        bisection_root(0.5, 1.7)
    en = time.time()
    print(f"C extensions time: {en - st} sec")
    
    print(f"Fibonacci times")

    st = time.time()
    for n in range(10000):
        fb.fibonacci(n)
    en = time.time()
    print(f"Fibonacci Python time: {en - st}")

    st = time.time()
    for n in range(10000):
        fb.fibonacci_numba(n)
    en = time.time()
    print(f"Fibonacci Numba time: {en - st}")


    print(f"Monte Carlo times: ")
    mcc = bs.monte_carlo_integral_cython
    st = time.time()
    for n in range(1000):
        mcc(20000)
    en = time.time()
    print(f"Monte Carlo Cython time: {en - st}")

    mcn = bsp.monte_carlo_integral_numba
    st = time.time()
    for n in range(1000):
        mcn(40000)
    en = time.time()
    print(f"Monte Carlo Numba time: {en - st}")
    


if __name__ == "__main__":
    main()
