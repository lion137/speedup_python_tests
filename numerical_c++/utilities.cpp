# pragma once

# include <cstdio>
# include <cstdlib>
# include <cmath>
# include <chrono>

int zbrac(float (*func)(float), float *x1, float *x2, int ntry, float factor)
// set x1 and x2 to interval with root for function func

{
    int j;
    float f1,f2;
    if (*x1 == *x2) perror("Bad initial range in zbrac");
    f1=(*func)(*x1);
    f2=(*func)(*x2);
    for (j = 1; j <= ntry; j++) 
    {
        if (f1 * f2 < 0.0) return 1;
        if (fabs(f1) < fabs(f2))
            f1 = (*func)(*x1 += factor * (*x1-*x2));
        else
            f2 = (*func)(*x2 += factor * (*x2-*x1));
    }
    return 0;
}

bool equal_float(float left, float right, float epsilon)
{
    if (fabs(left - right) < epsilon)
        return true;
    return false;
}

bool equal_double(double left, double right, double epsilon)
{
    if (fabs(left - right) < epsilon) 
        return true;
    return false;
}

float fun(float val)
// example to bisection_root
{
    return val * val - 1;
}

double fun2(double x)
// example fun to monte carlo integral
{
    return (pow(M_E , -x)) / (1 + (x - 1) * (x - 1));
}


