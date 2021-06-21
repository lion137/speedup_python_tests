import time
from numba import jit


def fibonacci(n):
    a = 0
    b = 1
    for x in range(n):
        a, b = a + b, a
    return a


@jit(nopython=True)
def fibonacci_numba(n):
    a = 0
    b = 1
    for x in range(n):
        a, b = a + b, a
    return a


def main():
    st = time.time()
    for n in range(10000):
        fibonacci(n)
    en = time.time()
    print(f"Python Fibonacci time: {en - st}")
    st = time.time()
    for n in range(10000):
        fibonacci_numba(n)
    en = time.time()
    print(f"Numba Fibonacci time: {en - st}")


if __name__ == "__main__":
    main()
