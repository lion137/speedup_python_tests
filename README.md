
Compilation of C++ part in file ```test.sh```, works under linux Ubuntu/WLS. As a testing algorithm is root finding via bisection and Fibonacci.
Python part works with Python3.9, installation:
```pip install -r requirements.txt```
Compile:
```python setup.py build_ext --inplace```
Run tests:
```pytest tests.py```
Performance:
```python performance_m.py```
Outcome:
```
Time taken by C++ bisection program: 0.1 s
Bisection times:
Python time: 4.310690402984619 s
Cython time: 0.6177973747253418 s
Numba time: 0.8303954601287842 s
Fibonacci times
Fibonacci Python time: 4.473325967788696 s
Fibonacci Numba time: 0.058374643325805664 s
```

There is no a Fibonacci Cython due to the big integers involved.        
Bisection does at most ```30``` iterations, Fibonacci does more and there is seen a bigger performance improvement.

Acctually, the top perfomer is ```pypy```, bisection time: ```0.204``` secs.    
Could be obtained here: https://www.pypy.org/download.html     

