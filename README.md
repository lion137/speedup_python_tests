Compilation of C++ part in file ```test.sh```, works under linux Ubuntu/WLS.    
Python part works with Python3.9, installation:    
```pip install -r requirements.txt```    
Run tests:    
```pytest tests.py```    
Performance:     
```python performance_m.py```     
Outcome:      
```
Time taken by C++ program: 0.1 sec
Bisection times:
Python time: 4.196092367172241
Cython time: 0.4356851577758789
Numba time: 0.7862272262573242
C extensions time: 0.46351170539855957 sec
Fibonacci times
Fibonacci Python time: 4.440826177597046
Fibonacci Numba time: 0.05439305305480957
```
There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.     
Acctually, the top perfomer is ```pypy```, bisection time: ```0.204``` secs; could be obtained here: https://www.pypy.org/download.html



