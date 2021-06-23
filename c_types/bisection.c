#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX_ITER 50
#define FACTOR 1.5

float fun(float val)
// example test bisection_root
{
    return val * val - 1;
}

int equal_float(float left, float right, float epsilon)
{
    if (fabs(left - right) < epsilon)
        return 1;
    return 0;
}

int get_interval(float* x1, float* x2)
{
    int j;
    float f1, f2;
    f1 = fun(*x1);
    f2 = fun(*x2);
    for (j = 1; j <= MAX_ITER; j++) {
        if (f1 * f2 < 0.0)
            return 1;
        if (fabs(f1) < fabs(f2))
            f1 = fun(*x1 += FACTOR * (*x1 - *x2));
        else
            f2 = fun(*x2 += FACTOR * (*x2 - *x1));
    }
    return 0;
}

float bisection_root(float left, float right, float epsilon)
{
    float dx, f, fmid, xmid, rtb;

    f = fun(left);
    fmid = fun(right);

    // if (f * fmid >= 0.0f)
    // perror("Inetrval must change sign");
    rtb = f < 0.0f ? (dx = right - left, left) : (dx = left - right, right);
    for (int j = 0; j < MAX_ITER; ++j) {
        dx *= 0.5f;
        xmid = rtb + dx;
        fmid = fun(xmid);
        if (fmid <= 0.0f)
            rtb = xmid;
        if (fabs(dx) < epsilon || fmid == 0.0f)
            return rtb;
    }
    perror("To many ietrations, no convergence");
    return 0.0; // never get
}



