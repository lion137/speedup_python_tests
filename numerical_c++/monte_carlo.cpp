# pragma once
# include <iostream>
# include <random>
# include <cmath>

# include "utilities.h"
# include "utilities.cpp"

double monte_carlo_integral(int ntry)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);
    double left = 0;
    double right = 5;
    double s_sum = 0;
    double range = right - left;
    double rand_sample = 0;
    for (int n = 0; n < ntry; ++n) {
        rand_sample = dis(gen);
        rand_sample = left + range * rand_sample;
        s_sum += fun2(rand_sample);
    }
    return range * s_sum / ntry;
}


