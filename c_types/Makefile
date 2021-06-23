all: test

clean:
	rm -f *.o *.so *.html

bisection.so: bisection.o
	gcc -shared -o libcbisection.so bisection.o

bisection.o: bisection.c
	gcc -c -Wall -Wextra -Werror -fpic bisection.c

test: bisection.so
	pytest bisection_tests.py
