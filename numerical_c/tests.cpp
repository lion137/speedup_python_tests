# include <iostream>
# include <cassert>
# include <limits>
# include <chrono>

# include "utilities.cpp"
# include "utilities.h"
# include "bisection.h"
# include "bisection.cpp"


using namespace std;

// test macro
#define run_test(f_name)\
	printf("%s\n", #f_name);\
	f_name();

void test_zbrac()
{
    float left =  0.5;
    float right = 0.7;
    zbrac(fun, &left, &right, 50, 1.5);
    assert (equal_float(left, 0.5f, 0.00001f));
    assert (equal_float(right, 1.75f, 0.00001f));
}

void test_bisection_root()
{
    float left = 0.5;
    float right = 0.75;
    zbrac(fun, &left, &right, 50, 1.5);
    float accuracy =  0.000001f * (fabs(left) + fabs(right)) / 2;
    assert(equal_float(1.0f, bisection_root(fun, left, right, accuracy, 40), accuracy));
}

void time_bisection_root()
{
    int num_loops = 1000000L;
    float left = 0.5;   
    float right = 0.7;
    zbrac(fun, &left, &right, 50, 1.5);
    float accuracy =  0.000001f * (fabs(left) + fabs(right)) / 2;
    auto start = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < num_loops; ++i)
    {
        // bisection_root(fun, left, right, accuracy, 40);
        zbrac(fun, &left, &right, 50, 1.5);
        bisection_root(fun, left, right, accuracy, 50);
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time taken by bisection algorithm: "
         << duration.count() << " miliseconds, " ;
    std::cout << "After: " << num_loops <<" iterations\n";
}

int main() 
{
    cout << "------------------------------------------------------\n";
    run_test(test_zbrac);
    run_test(test_bisection_root);
    run_test(time_bisection_root);
    /*float left = 0.5;
    float right = 0.75;
    zbrac(fun, &left, &right, 50, 1.5);
    float accuracy =  0.000001f * (fabs(left) + fabs(right)) / 2;
    std::cout << left << ", " << right << ", " << accuracy <<"\n";
    bisection_root(fun, left, right, accuracy, 40);*/
    cout << "------------------------------------------------------\n";

    return 0;
}





