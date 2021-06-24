Compilation of C++ part in file ```test.sh```, works under linux Ubuntu/WLS.    
Python part works with Python3.9, installation:    
```pip install -r requirements.txt```    
Run tests:    
```pytest tests.py```    
Performance:     
```python performance_m.py```     
Outcome:      
```
Time taken by C++ bisection: 100 ms
Time taken by C++ bisection, (optimization on): 75 ms
Time taken by C++ Monte Carlo: 1300 ms
Time taken by C++ Monte Carlo, (optimization on): 560 ms
Bisection times:
Python time: 4.107430696487427
Cython time: 0.42247796058654785
Numba time: 0.7463068962097168
C extensions time: 0.4468255043029785 sec
Fibonacci times
Fibonacci Python time: 4.375149488449097
Fibonacci Numba time: 0.050522804260253906
Monte Carlo times:
Monte Carlo Cython time: 5.285279035568237
Monte Carlo Numba time: 0.8551747798919678
```
There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.     
```pypy``` is best with bisection: ```0.204``` secs; could be obtained here: https://www.pypy.org/download.html    
For that specific problem, (Monte Carlo) Numba's doing great, close to C++ with optimization.



