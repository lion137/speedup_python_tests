import bisection as bs
import bisection_python as bsp

def test_get_interval_python():
    left = 0.5
    right = 0.7
    e = 0.000001 * (abs(left) + abs(right)) / 2
    int_beg, int_end = bsp.get_interval(left, right)
    assert 0.5 - e < int_beg < 0.5 + e and 1.75 - e < int_end < 1.75 + e


def test_bisection_python():
    left, right = bsp.get_interval(0.5, 0.7)
    accuracy = 0.000001 * (abs(left) + abs(right)) / 2
    assert bsp.equal_float(
        bsp.bisection_python(left, right, accuracy, 50), 1.0, accuracy
    )


def test_monte_carlo_integral_numba():
    assert bsp.equal_float(bsp.monte_carlo_integral_numba(20000), 0.696, 0.02)


"""
left, right = bsp.get_interval(0.5, 0.75)
accuracy = 0.000001 * (abs(left) + abs(right)) / 2
print(left, right, accuracy)
bsp.bisection_python(left, right, accuracy, max_iter=50)
"""
