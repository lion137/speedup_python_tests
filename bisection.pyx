import cython

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