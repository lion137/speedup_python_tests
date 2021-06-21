# pragma once

// set x1 and x2 to interval with root for function func
int zbrac(float (*func)(float), float *x1, float *x2, int ntry, float factor);

bool equal_float(float left, float right, float epsilon);

float fun(float val);  // test zbrac, bisection_root helper
