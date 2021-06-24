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
Python time: 4.108937740325928
Cython time: 0.4154782295227051
Numba time: 0.7326419353485107
C extensions time: 0.44522833824157715 sec
Fibonacci times
Fibonacci Python time: 4.3231422901153564
Fibonacci Numba time: 0.049730777740478516
Monte Carlo times:
Monte Carlo Numba time: 0.45322465896606445
```
There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.     
```pypy``` is best with bisection: ```0.204``` secs; could be obtained here: https://www.pypy.org/download.html    
For that specific problem, (Monte Carlo) Numba's JIT doing great, better than C++ with optimization.




