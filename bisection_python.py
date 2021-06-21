# bisection algorithms to find roots
from numba import jit
import pdb

# helper and example functions


def f(x):
    return x * x - 1


def equal_float(left, right, epsilon):
    if abs(left - right) < epsilon:
        return True
    return False


def get_interval(left, right, ntry=50, factor=1.5):
    """Takes initial interval, [left, right],
    returns interval includes root of f"""
    val_left = f(left)
    val_right = f(right)
    for j in range(ntry):
        if val_left * val_right < 0.0:
            return left, right
        if abs(val_left) < abs(val_right):
            left += factor * (left - right)
            val_left = f(left)
        else:
            right += factor * (right - left)
            val_right = f(right)
    return left, right


@jit(nopython=True)
def get_interval_numba(left, right, ntry=50, factor=1.5):
    """Takes function f, and initial interval, [left, right],
    returns interval includes root of f"""

    def f(x):
        return x * x - 1

    val_left = f(left)
    val_right = f(right)
    for j in range(ntry):
        if val_left * val_right < 0.0:
            return left, right
        if abs(val_left) < abs(val_right):
            left += factor * (left - right)
            val_left = f(left)
        else:
            right += factor * (right - left)
            val_right = f(right)
    return left, right


def bisection_python(left, right, epsilon, max_iter=50):
    dx = None
    g = None
    fmid = None
    xmid = None
    rtb = None
    # pdb.set_trace()
    g = f(left)
    fmid = f(right)
    assert g * fmid < 0.0
    if g < 0.0:
        dx = right - left
        rtb = left
    else:
        dx = left - right
        rtb = right
    for j in range(max_iter):
        dx *= 0.5
        xmid = rtb + dx
        fmid = f(xmid)
        if fmid <= 0.0:
            rtb = xmid
        if abs(dx) < epsilon or fmid == 0.0:
            return rtb
    raise Exception("To many interations")


@jit(nopython=True)
def bisection_python_numba(left, right, epsilon, max_iter=50):
    def f(x):
        return x * x - 1

    dx = None
    g = None
    fmid = None
    xmid = None
    rtb = None
    # pdb.set_trace()
    g = f(left)
    fmid = f(right)
    assert g * fmid < 0.0
    if g < 0.0:
        dx = right - left
        rtb = left
    else:
        dx = left - right
        rtb = right
    for j in range(max_iter):
        dx *= 0.5
        xmid = rtb + dx
        fmid = f(xmid)
        if fmid <= 0.0:
            rtb = xmid
        if abs(dx) < epsilon or fmid == 0.0:
            return rtb
    raise Exception("To many interations")
