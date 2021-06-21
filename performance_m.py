import time

import bisection as bs
import bisection_python as bsp
import fibo as fb


def f(x):
    return x * x - 1


def main():

    left, right = bsp.get_interval_numba(0.5, 0.7)
    accuracy = 0.000001 * (abs(left) + abs(right)) / 2  # for stability
    print(f"Time taken by C++ program: 100 ms")
    print(f"Bisection times: ")
    st = time.time()
    for _ in range(1000000):
        left, right = bsp.get_interval_numba(0.5, 0.7)
        bsp.bisection_python(left, right, epsilon=accuracy)
    en = time.time()

    print(f"Python time: {en - st}")

    st = time.time()
    for _ in range(1000000):
        left, right = bs.get_interval(0.5, 0.7)
        bs.bisection_cython(left, right, epsilon=accuracy)
    en = time.time()

    print(f"Cython time: {en - st}")

    st = time.time()
    for _ in range(1000000):
        left, right = bsp.get_interval_numba(0.5, 0.7)
        bsp.bisection_python_numba(left, right, epsilon=accuracy)
    en = time.time()

    print(f"Numba time: {en - st}")

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


if __name__ == "__main__":
    main()
