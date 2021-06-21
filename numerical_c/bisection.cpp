# include <iostream>
# include <vector>
# include <cmath>
# include <cstdio>

# include "utilities.cpp"
# include "utilities.h"

float bisection_root(float (*func)(float), float left, float right, float epsilon, int max_iter)
{
    float dx, f, fmid, xmid, rtb;
    
    f = (*func)(left);
    fmid = (*func)(right);

    if (f * fmid >= 0.0f) 
        perror("Inetrval must change sign");
    rtb = f < 0.0f ? (dx = right - left, left) : (dx = left - right, right);
    for(int j = 0; j < max_iter; ++j) 
    {
        dx *= 0.5f;
        xmid = rtb + dx;
        fmid = (*func) (xmid);
        if (fmid <= 0.0f)
            rtb = xmid;
        if (fabs(dx) < epsilon || fmid == 0.0f)
            return rtb;
    }
    perror("To many ietrations, no convergence");
    return 0.0;   // never get
}





