
Compilation of C++ part in file ```test.sh```, works under linux Ubuntu/WLS.    
Python part works with Python3.9, installation:    
```pip install -r requirements.txt```    
Run tests:    
```pytest tests.py```    
Performance:     
```python performance_m.py```     
Outcome:      
```
Time taken by C++ bisection program: 0.1 ms
Bisection times:
Python time: 4.310690402984619
Cython time: 0.6177973747253418
Numba time: 0.8303954601287842
Fibonacci times
Fibonacci Python time: 4.473325967788696
Fibonacci Numba time: 0.05297398567199707
```
There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.
