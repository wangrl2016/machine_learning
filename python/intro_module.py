# Import module with the following command.
import fibo
# from fibo import fib, fib2
# from fibo import *
# import fibo as fib
# from fibo import lib as fibonacci
import sys
import builtins

if __name__ == '__main__':
    fibo.fib(1000)

    result = fibo.fib2(100)
    print(result)

    print(fibo.__name__)

    # Assign it to a local name.
    fib = fibo.fib
    fib(500)

    # Modify `PYTHONPATH` using standard list operations.
    sys.path.append('/ufs/guido/lib/python')

    # `dir()` to find out which names a module defines.
    print(dir(fibo))

    # Without arguments, `dir()` lists the names you have defined currently.
    print(dir())

    # List the names of built-in functions and variables.
    print(dir(builtins))
