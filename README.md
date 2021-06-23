Compilation of C++ part in file ```test.sh```, works under linux Ubuntu/WLS.    
Python part works with Python3.9, installation:    
```pip install -r requirements.txt```    
Run tests:    
```pytest tests.py```    
Performance:     
```python performance_m.py```     
Outcome:      
```
Time taken by C++ program: 100 ms
Bisection times:
Python time: 5.384427070617676
Cython time: 0.6508324146270752
Numba time: 1.0673410892486572
C extensions times: 1.3348870277404785 sec
Fibonacci times
Fibonacci Python time: 5.962206125259399
Fibonacci Numba time: 0.06793999671936035
```
There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.
Acctually, the top perfomer is ```pypy```, bisection time: ```0.204``` secs.    
Could be obtained here: https://www.pypy.org/download.html


