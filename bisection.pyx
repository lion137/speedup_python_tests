import cython
import random
import math

cpdef f(cython.float x):
    return x * x - 1


cpdef tuple get_interval(cython.float left, cython.float right):
    val_left: cython.float
    val_right: cython.float
    val_left = f(left)
    val_right = f(right)
    for j in range(50):
        if val_left * val_right < 0.0: 
            return left, right
        if abs(val_left) < abs(val_right):
            left += 1.5 * (left - right)
            val_left = f(left)
        else:
            right += 1.5 * (right - left)
            val_right = f(right)
    return left, right

cpdef float bisection_cython(cython.float left, cython.float right, cython.float epsilon):
    # interval finding part
    val_left = f(left)
    val_right = f(right)
    for j in range(50):
        if val_left * val_right < 0.0: 
            break
        if abs(val_left) < abs(val_right):
            left += 1.5 * (left - right)
            val_left = f(left)
        else:
            right += 1.5 * (right - left)
            val_right = f(right)
    # end
    cython.float: dx
    cython.float: g
    cython.float: fmid
    cython.float: xmid
    cython.float: rtb
    g = f(left)
    fmid = f(right)
    if g < 0.0:
        dx = right - left
        rtb = left
    else:
        dx = left - right
        rtb = right
    for j in range(50):
        dx *= 0.5
        xmid = rtb + dx
        fmid = f(xmid)
        if fmid < 0.0:
            rtb = xmid
        if abs(dx) < epsilon or fmid == 0.0:
            return rtb
    raise Exception("To many iterations")


cpdef cython.float monte_carlo_integral_cython(int ntry):
    cython.float: left 
    cython.float: right 
    cython.float: s_sum 
    cython.float: range_int
    left = 0
    right = 5
    s_sum = 0
    range_int = right - left
    for n in range(ntry):
        cython.float: rand_sample 
        rand_sample = random.uniform(0, 1)
        rand_sample = left + range_int * rand_sample;
        s_sum += (math.e ** (-rand_sample)) / (1 + (rand_sample - 1) * (rand_sample - 1))
    return range_int * s_sum / ntry